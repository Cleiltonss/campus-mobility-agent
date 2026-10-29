# campus-mobility-agent

Assistente de dados para a reitoria de uma universidade com cerca de
7.000 alunos. Responde perguntas sobre o transporte dos alunos
consultando um star schema em Postgres (text-to-SQL com guardrails) e
documentos da reitoria (RAG).

Os dados são sintéticos.

## Estado atual

Em construção. Já existem:

- Star schema em `modelo/schema.sql`: `fato_transportes` (9 chaves, 3
  métricas) e 6 dimensões (`dim_modal`, `dim_categoria`, `dim_hora`,
  `dim_local`, `dim_data` e `dim_usuario`, esta como SCD tipo 2).
  Postgres 18 local via `modelo/docker-compose.yml`.
- Contrato `Viagem` (Pydantic) em `src/assistente/contrato.py`, que
  recusa a viagem que chega antes de sair.
- Gerador de dados sintéticos em `src/assistente/gerador.py`: 7.000
  alunos em 21 bairros de São Paulo, Osasco e Taboão da Serra, ano letivo
  de 2026, cerca de 2,7 milhões de trechos no fato. Cada linha do fato
  passa pela `Viagem` antes de existir. As premissas (velocidade, tarifa,
  turnos, calendário) ficam declaradas no topo do arquivo. Mesma semente,
  mesmos dados.
- Carga no Postgres em `src/assistente/carga.py`: `COPY` numa transação
  só, que pode rodar de novo e recarrega do zero.

Ainda não existem: o agente, a API, os evals e o RAG.

## Stack

Python 3.14 (fixo em `.python-version`, via uv), Pydantic, pytest,
FastAPI, Postgres + pgvector, Docker, MCP, Langfuse, GitHub Actions,
GCP (Cloud Run).

## Comandos

```bash
uv sync          # cria o .venv com o Python e as dependências fixos
uv run pytest    # roda os testes

# sobe o Postgres e cria o schema (só na primeira vez)
cd modelo && docker compose up -d && cd ..
docker compose -f modelo/docker-compose.yml exec -T database \
  psql -U alfred -d transportes < modelo/schema.sql

# gera os dados e carrega
export PGPASSWORD=<senha do compose>
uv run python -m assistente.carga                            # 7.000 alunos, cerca de 1 min
uv run python -m assistente.carga --alunos 500 --semente 1   # carga menor
```
