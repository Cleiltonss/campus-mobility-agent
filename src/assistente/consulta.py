"""Ferramenta do agente: roda um SELECT no banco como o usuário `agent`.

Três camadas, da mais forte para a mais fraca:

1. O usuário `agent` só tem SELECT (modelo/leitor.sql). É a última linha:
   vale mesmo que este arquivo tenha bug.
2. A transação é read-only: o Postgres recusa escrita antes de olhar a
   permissão.
3. Este código aceita um comando por vez, com teto de tempo e de linhas.
"""

import os

import psycopg

LIMITE_LINHAS = 50          # o que volta para o LLM vira token de entrada
TEMPO_LIMITE_MS = 5000      # um SELECT de leitura ainda trava o banco


class ConsultaRecusada(Exception):
    """O SQL foi barrado antes de chegar ao banco."""


def conectar_agente():
    # a senha vem do ambiente (.env), nunca do código
    url = os.environ.get("AGENTE_DATABASE_URL", "postgresql://agent@localhost:5432/transportes")
    return psycopg.connect(url, password=os.environ.get("AGENTE_SENHA"))


def um_comando(sql):
    """Tira o ';' do fim e recusa se sobrar outro.

    Com mais de um comando, o segundo poderia ser um `SET statement_timeout = 0`
    e desligar o teto de tempo. Custo: um ';' dentro de um texto entre aspas
    também é recusado; neste banco nenhuma pergunta precisa disso.
    """
    comando = sql.strip().rstrip(";").strip()
    if not comando:
        raise ConsultaRecusada("SQL vazio.")
    if ";" in comando:
        raise ConsultaRecusada("Um comando por vez: mande um SELECT só, sem ';' no meio.")
    return comando


def rodar_sql(sql, limite_linhas=LIMITE_LINHAS, tempo_limite_ms=TEMPO_LIMITE_MS):
    """Roda um SELECT e devolve colunas, até `limite_linhas` linhas e se cortou."""
    comando = um_comando(sql)
    with conectar_agente() as conexao:
        conexao.read_only = True
        with conexao.transaction(), conexao.cursor() as cursor:
            # SET LOCAL vale só nesta transação, e é refeito em toda chamada
            cursor.execute(f"SET LOCAL statement_timeout = {int(tempo_limite_ms)}")
            cursor.execute(comando)
            if cursor.description is None:
                raise ConsultaRecusada("O comando não devolveu linhas: use um SELECT.")
            colunas = [coluna.name for coluna in cursor.description]
            # uma a mais que o limite, só para saber se havia mais
            linhas = cursor.fetchmany(limite_linhas + 1)
    return {
        "colunas": colunas,
        "linhas": [list(linha) for linha in linhas[:limite_linhas]],
        "cortado": len(linhas) > limite_linhas,
    }
