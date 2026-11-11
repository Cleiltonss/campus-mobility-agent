"""Testes do loop do agente com um LLM falso: não chamam a API e não custam nada."""

from types import SimpleNamespace as NS

import psycopg
import pytest

from assistente import agente

SQL = "SELECT COUNT(*) AS chegadas FROM fato_transportes"


def texto(conteudo):
    return NS(type="text", text=conteudo)


def pedido(sql, id_="pedido_1"):
    return NS(type="tool_use", id=id_, name="rodar_sql", input={"sql": sql})


def mensagem(conteudo, parada):
    return NS(content=conteudo, stop_reason=parada, usage=NS(input_tokens=2000, output_tokens=200))


class ClienteFalso:
    """Devolve as mensagens roteirizadas e guarda o que recebeu em cada chamada."""

    def __init__(self, roteiro):
        self.roteiro = roteiro          # função: número da chamada -> mensagem
        self.chamadas = []
        self.beta = NS(messages=NS(create=self.create))

    def create(self, **kwargs):
        # cópia da lista: o agente continua mexendo nela depois da chamada
        self.chamadas.append({**kwargs, "messages": list(kwargs["messages"])})
        return self.roteiro(len(self.chamadas))


@pytest.fixture
def banco_falso(monkeypatch):
    monkeypatch.setattr(
        agente, "rodar_sql",
        lambda sql: {"colunas": ["chegadas"], "linhas": [[1083433]], "cortado": False},
    )


def test_pergunta_em_duas_chamadas(banco_falso):
    roteiro = {
        1: mensagem([pedido(SQL)], "tool_use"),
        2: mensagem([texto("1.083.433 chegadas ao campus em 2026.")], "end_turn"),
    }
    cliente = ClienteFalso(roteiro.get)

    resposta = agente.responder("quantas chegadas ao campus no ano?", cliente=cliente)

    assert resposta.passos == 2
    assert resposta.parada == "end_turn"
    assert resposta.sqls == [SQL]
    assert resposta.texto == "1.083.433 chegadas ao campus em 2026."
    # a segunda chamada reenvia tudo: pergunta, pedido do LLM e o resultado
    segunda = cliente.chamadas[1]["messages"]
    assert [m["role"] for m in segunda] == ["user", "assistant", "user"]
    resultado = segunda[2]["content"][0]
    assert resultado["tool_use_id"] == "pedido_1"
    assert "1083433" in resultado["content"]


def test_para_no_limite_de_passos(banco_falso):
    # o bug da madrugada: o LLM pede a ferramenta para sempre
    cliente = ClienteFalso(lambda n: mensagem([pedido(SQL, id_=f"pedido_{n}")], "tool_use"))

    resposta = agente.responder("pergunta qualquer", cliente=cliente, max_passos=3)

    assert resposta.parada == "limite_de_passos"
    assert len(cliente.chamadas) == 3


def test_erro_do_sql_volta_para_o_llm(monkeypatch):
    def coluna_inventada(sql):
        raise psycopg.errors.UndefinedColumn('column "bairro_casa" does not exist')

    monkeypatch.setattr(agente, "rodar_sql", coluna_inventada)
    roteiro = {
        1: mensagem([pedido("SELECT bairro_casa FROM dim_usuario")], "tool_use"),
        2: mensagem([texto("O banco não guarda o bairro da casa do aluno.")], "end_turn"),
    }
    cliente = ClienteFalso(roteiro.get)

    agente.responder("de que bairro são os alunos?", cliente=cliente)

    resultado = cliente.chamadas[1]["messages"][2]["content"][0]
    assert resultado["is_error"] is True
    assert "does not exist" in resultado["content"]


def test_custo_de_uma_chamada():
    # a conta da sessão 34: 2.000 tokens de entrada e 200 de saída no Opus 5.5
    resposta = agente.Resposta(
        texto="", sqls=[], passos=1, parada="end_turn", tokens_entrada=2000, tokens_saida=200,
    )
    assert resposta.custo_usd == pytest.approx(0.012)
