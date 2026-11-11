"""Agente text-to-SQL da reitoria.

A reitoria pergunta em português; o LLM escreve um SELECT; a ferramenta
`rodar_sql` roda como o usuário `agent` (só leitura); o resultado volta para o
LLM, que escreve a resposta. Uma pergunta custa no mínimo duas chamadas ao LLM,
e cada chamada reenvia a conversa inteira: a API não guarda estado.

Uso:
    uv run --env-file .env python -m assistente.agente "quantas chegadas ao campus no ano?"
"""

import argparse
import json
from pathlib import Path

import anthropic
import psycopg
from pydantic import BaseModel

from assistente.consulta import ConsultaRecusada, rodar_sql

MODELO = "claude-opus-5-5"
PRECO_ENTRADA_USD = 4 / 1_000_000   # por token, Opus 5.5
PRECO_SAIDA_USD = 20 / 1_000_000

# Limite de passos: quantas chamadas ao LLM uma pergunta pode fazer. É a
# primeira linha contra o loop infinito; a última é o limite de gasto mensal
# no console do provedor (US$ 55), que não depende deste código.
MAX_PASSOS = 8

SCHEMA = (Path(__file__).resolve().parents[2] / "modelo" / "schema.sql").read_text()

SISTEMA = f"""Você é o assistente de dados da reitoria de uma universidade com cerca de \
7.000 alunos. Você responde perguntas sobre o transporte dos alunos consultando um \
Postgres (star schema) com a ferramenta rodar_sql.

Como trabalhar:
- Todo número da sua resposta vem de um resultado de rodar_sql. Não estime nem \
complete com conhecimento geral.
- Agregue no SQL (COUNT, SUM, AVG, GROUP BY) em vez de trazer linhas cruas: a \
ferramenta devolve no máximo 50 linhas.
- Se o SQL der erro, leia a mensagem, corrija e tente de novo.
- Se o banco não tem o dado que a pergunta pede, diga o que falta em vez de \
responder outra pergunta.

O que as tabelas significam:
- Cada linha de fato_transportes é um trecho: um deslocamento contínuo em um único \
modal. A ida de um aluno de casa à universidade pode ter vários trechos (por \
exemplo, metrô até uma estação e ônibus até o campus).
- A universidade é o local de dim_local com endereco = 'Av. da Universidade, 1000'. \
Uma chegada à universidade é um trecho com destino_id nesse local.
- data_id é AAAAMMDD (20260315 = 15/03/2026). O banco tem o ano de 2026.
- hora_saida_id e hora_chegada_id são a hora cheia, de 0 a 23; os minutos não são \
guardados.
- A chave -1 é o membro 'Não se aplica' de toda dimensão (por exemplo, \
categoria_id = -1 em modais que não são aplicativo).
- dim_usuario é dimensão de mudança lenta tipo 2: usuario_id é uma versão do aluno \
e aluno_id é o aluno. O turno (periodo) de uma viagem é o da versão para a qual o \
fato aponta. Para contar alunos, conte aluno_id distinto, não linhas.
- dim_data.tem_aula vale 'Sim' ou 'Não'. dim_data.ordem_dia vai de 1 (domingo) a 7 \
(sábado); ordene dias da semana por ela, não por nome_dia.
- Um bairro só é identificado junto com a cidade: há bairros com o mesmo nome em \
cidades diferentes.
- duracao está em minutos, distancia em km e preco em reais.

Resposta: em português, curta, com cada número acompanhado do que ele conta \
(trechos, alunos, viagens por dia) e com as premissas que você assumiu.

Schema:
{SCHEMA}"""

FERRAMENTA_SQL = {
    "name": "rodar_sql",
    "description": (
        "Roda um único SELECT no Postgres da reitoria, com um usuário que só tem "
        "permissão de leitura, e devolve as colunas e até 50 linhas do resultado "
        "(o campo 'cortado' diz se havia mais). Um comando por vez, sem ';' no meio. "
        "A consulta é cancelada depois de 5 segundos. Erros de SQL voltam como "
        "mensagem do banco, para você corrigir."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "sql": {"type": "string", "description": "Um SELECT (ou WITH ... SELECT) em SQL do Postgres."},
        },
        "required": ["sql"],
        "additionalProperties": False,
    },
    "strict": True,
}


class Resposta(BaseModel):
    texto: str
    sqls: list[str]
    passos: int              # chamadas ao LLM feitas
    parada: str              # end_turn, refusal, max_tokens ou limite_de_passos
    tokens_entrada: int
    tokens_saida: int

    @property
    def custo_usd(self):
        return self.tokens_entrada * PRECO_ENTRADA_USD + self.tokens_saida * PRECO_SAIDA_USD


def executar_ferramenta(bloco):
    """Roda um pedido de ferramenta e devolve o tool_result para o LLM."""
    resultado = {"type": "tool_result", "tool_use_id": bloco.id}
    if bloco.name != "rodar_sql":
        return resultado | {"content": f"Ferramenta desconhecida: {bloco.name}", "is_error": True}
    try:
        linhas = rodar_sql(bloco.input["sql"])
    except (ConsultaRecusada, psycopg.Error) as erro:
        # o erro volta para o LLM corrigir (coluna inventada, sintaxe, tempo)
        return resultado | {"content": str(erro).strip(), "is_error": True}
    # default=str: NUMERIC chega como Decimal, que o json não serializa
    return resultado | {"content": json.dumps(linhas, ensure_ascii=False, default=str)}


def responder(pergunta, cliente=None, max_passos=MAX_PASSOS):
    cliente = cliente or anthropic.Anthropic()
    mensagens = [{"role": "user", "content": pergunta}]
    sqls = []
    tokens_entrada = tokens_saida = 0

    # o contador é o próprio range, fora do corpo: nada dentro da volta o zera
    for passo in range(1, max_passos + 1):
        resposta = cliente.beta.messages.create(
            model=MODELO,
            max_tokens=16000,
            system=SISTEMA,
            tools=[FERRAMENTA_SQL],
            messages=mensagens,
            output_config={"effort": "medium"},
            # se o modelo recusar, o provedor tenta de novo em outro modelo
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
        tokens_entrada += resposta.usage.input_tokens
        tokens_saida += resposta.usage.output_tokens
        # o conteúdo inteiro volta na próxima chamada, inclusive o raciocínio
        mensagens.append({"role": "assistant", "content": resposta.content})

        if resposta.stop_reason != "tool_use":
            texto = "".join(b.text for b in resposta.content if b.type == "text")
            return Resposta(
                texto=texto, sqls=sqls, passos=passo, parada=resposta.stop_reason,
                tokens_entrada=tokens_entrada, tokens_saida=tokens_saida,
            )

        pedidos = [b for b in resposta.content if b.type == "tool_use"]
        sqls += [b.input.get("sql", "") for b in pedidos]
        # todos os resultados numa mensagem só, na ordem dos pedidos
        mensagens.append({"role": "user", "content": [executar_ferramenta(b) for b in pedidos]})

    return Resposta(
        texto=f"Parei sem resposta: a pergunta passou de {max_passos} chamadas ao LLM.",
        sqls=sqls, passos=max_passos, parada="limite_de_passos",
        tokens_entrada=tokens_entrada, tokens_saida=tokens_saida,
    )


def main():
    parser = argparse.ArgumentParser(description="Pergunta ao assistente da reitoria.")
    parser.add_argument("pergunta")
    args = parser.parse_args()

    resposta = responder(args.pergunta)
    print(resposta.texto)
    print()
    for i, sql in enumerate(resposta.sqls, start=1):
        print(f"-- SQL {i}\n{sql}\n")
    print(
        f"passos: {resposta.passos} | parada: {resposta.parada} | "
        f"tokens: {resposta.tokens_entrada} entrada, {resposta.tokens_saida} saída | "
        f"custo: US$ {resposta.custo_usd:.4f}"
    )


if __name__ == "__main__":
    main()
