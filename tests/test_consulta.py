"""Testes da ferramenta do agente. Os que usam o banco precisam do Postgres
no ar e da senha do agent:

    uv run --env-file .env pytest
"""

import os

import psycopg
import pytest

from assistente.consulta import ConsultaRecusada, conectar_agente, rodar_sql, um_comando


@pytest.fixture(scope="module")
def banco():
    if not os.environ.get("AGENTE_SENHA"):
        pytest.skip("sem AGENTE_SENHA: rode com uv run --env-file .env pytest")
    try:
        conectar_agente().close()
    except psycopg.OperationalError:
        pytest.skip("Postgres fora do ar: docker compose up -d em modelo/")


# --- sem banco ---------------------------------------------------------------

def test_um_comando_tira_o_ponto_e_virgula_do_fim():
    assert um_comando("  SELECT 1;  ") == "SELECT 1"


def test_um_comando_recusa_dois_comandos():
    # o segundo comando desligaria o teto de tempo
    with pytest.raises(ConsultaRecusada):
        um_comando("SELECT 1; SET statement_timeout = 0")


def test_um_comando_recusa_vazio():
    with pytest.raises(ConsultaRecusada):
        um_comando(" ; ")


# --- com banco ---------------------------------------------------------------

def test_le_o_banco(banco):
    resultado = rodar_sql("SELECT COUNT(*) AS modais FROM dim_modal")
    # 8 modais + o membro -1
    assert resultado == {"colunas": ["modais"], "linhas": [[9]], "cortado": False}


def test_corta_no_limite_de_linhas(banco):
    resultado = rodar_sql("SELECT hora_id FROM dim_hora ORDER BY hora_id", limite_linhas=10)
    # a dim_hora tem 25 linhas (-1 e 0 a 23): voltam 10 e o aviso de corte
    assert resultado["linhas"] == [[-1]] + [[hora] for hora in range(9)]
    assert resultado["cortado"] is True


@pytest.mark.parametrize("sql", [
    "DELETE FROM dim_modal WHERE modal_id = 999",
    "UPDATE dim_modal SET nome_modal = 'x' WHERE modal_id = 999",
    "INSERT INTO dim_modal (modal_id, nome_modal) VALUES (999, 'teste')",
    "TRUNCATE dim_modal",
    "DROP TABLE dim_modal",
])
def test_usuario_agent_nao_escreve(banco, sql):
    # direto no banco, sem a transação read-only do rodar_sql: testa só a
    # permissão do usuário (a última linha). WHERE 999 e a transação desfeita
    # garantem que nada muda se a permissão estiver errada.
    with conectar_agente() as conexao:
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            with conexao.transaction():
                conexao.execute(sql)


def test_rodar_sql_recusa_escrita(banco):
    with pytest.raises(psycopg.Error):
        rodar_sql("DELETE FROM dim_modal WHERE modal_id = 999")


def test_comando_sem_linhas_e_recusado(banco):
    with pytest.raises(ConsultaRecusada):
        rodar_sql("SET statement_timeout = 0")


def test_teto_de_tempo(banco):
    with pytest.raises(psycopg.errors.QueryCanceled):
        rodar_sql("SELECT pg_sleep(2)", tempo_limite_ms=200)
