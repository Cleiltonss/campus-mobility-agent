import argparse
import os
import time

import psycopg

from assistente.gerador import gerar_dados


# na ordem da carga: dimensões antes do fato, por causa das FKs.
# A primeira coluna de cada dimensão é a chave.
COLUNAS = {
    "dim_modal": ["modal_id", "nome_modal"],
    "dim_categoria": ["categoria_id", "nome_categoria"],
    "dim_hora": ["hora_id", "periodo_dia"],
    "dim_local": ["local_id", "endereco", "bairro", "cidade"],
    "dim_data": ["data_id", "nome_dia", "dia", "mes", "ano", "tem_aula", "ordem_dia"],
    "dim_usuario": ["usuario_id", "aluno_id", "periodo", "atual"],
    "fato_transportes": [
        "modal_id", "categoria_id", "origem_id", "destino_id",
        "hora_saida_id", "hora_chegada_id", "data_saida_id", "data_chegada_id",
        "usuario_id", "duracao", "distancia", "preco",
    ],
}


def conectar():
    # a senha vem do PGPASSWORD, que o driver lê sozinho: não fica no código
    url = os.environ.get("DATABASE_URL", "postgresql://alfred@localhost:5432/transportes")
    return psycopg.connect(url)


def carregar(conexao, dados):
    contagem = {}
    # uma transação só: ou a carga inteira entra, ou o banco fica como estava
    with conexao.transaction(), conexao.cursor() as cursor:
        # recarga do zero, sem apagar os membros -1 do schema.sql.
        # TRUNCATE, não DELETE: o DELETE deixa milhões de linhas mortas no fato,
        # e cada linha apagada de uma dimensão varre o fato atrás de referência
        # (a FK não tem índice). Medido: 55 s com TRUNCATE, 576 s com DELETE.
        cursor.execute("TRUNCATE fato_transportes")
        for tabela, colunas in COLUNAS.items():
            if tabela != "fato_transportes":
                cursor.execute(f"DELETE FROM {tabela} WHERE {colunas[0]} <> -1")

        # COPY em vez de um INSERT por linha: milhões de linhas num fluxo só
        for tabela, colunas in COLUNAS.items():
            total = 0
            with cursor.copy(f"COPY {tabela} ({', '.join(colunas)}) FROM STDIN") as copia:
                for linha in dados[tabela]:
                    copia.write_row([linha[coluna] for coluna in colunas])
                    total += 1
            contagem[tabela] = total
    return contagem


def main():
    parser = argparse.ArgumentParser(description="Gera os dados sintéticos e carrega no Postgres.")
    parser.add_argument("--alunos", type=int, default=7000)
    parser.add_argument("--semente", type=int, default=42)
    args = parser.parse_args()

    inicio = time.perf_counter()
    with conectar() as conexao:
        contagem = carregar(conexao, gerar_dados(args.alunos, args.semente))
        conexao.execute("ANALYZE")  # estatísticas novas para o planejador de queries
    for tabela, total in contagem.items():
        print(f"{tabela}: {total} linhas")
    print(f"tempo: {time.perf_counter() - inicio:.0f} s")


if __name__ == "__main__":
    main()
