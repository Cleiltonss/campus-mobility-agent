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
- Agente text-to-SQL em `src/assistente/agente.py`: o LLM escreve um
  `SELECT`, a ferramenta `rodar_sql` (`src/assistente/consulta.py`) roda
  com o usuário `agent`, que só tem permissão de leitura
  (`modelo/leitor.sql`), e o resultado volta para o LLM escrever a
  resposta. Guardrails: usuário read-only, transação read-only, um comando
  por vez, teto de 5 s por consulta e de 50 linhas por resultado, e limite
  de 8 chamadas ao LLM por pergunta. O LLM é o qwen3:8b, rodando local
  pelo Ollama (sem custo por token). Os testes do loop usam um LLM falso.

- Documentos da reitoria para o RAG em `documentos/` (sintéticos): o
  regulamento e o quadro de horários do fretado estudantil, o guia do
  transporte público até o campus, o guia dos setores do campus e as
  regras do auxílio-transporte. O golden set da busca, com 10 perguntas e
  os documentos que respondem cada uma, está em
  `avaliacao/golden_set_rag.yaml`.

Ainda não existem: a API, os evals e a busca do RAG (ingestão,
embeddings e pgvector).

## Stack

Python 3.14 (fixo em `.python-version`, via uv), Pydantic, pytest,
Ollama (qwen3:8b, via Anthropic SDK), FastAPI, Postgres + pgvector, Docker, Langfuse, GitHub Actions,
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

# usuário do agente (só na primeira vez); senhas no .env, ver .env.example
cp .env.example .env    # preencha AGENTE_SENHA
set -a && source .env && set +a
docker compose -f modelo/docker-compose.yml exec -T database \
  psql -U alfred -d transportes -v ON_ERROR_STOP=1 -v senha="$AGENTE_SENHA" < modelo/leitor.sql

# pergunta ao agente (o Ollama precisa estar rodando), e os testes que usam o banco
ollama pull qwen3:8b    # só na primeira vez, 5,2 GB
uv run --env-file .env python -m assistente.agente "quantas chegadas ao campus no ano?"
uv run --env-file .env pytest
```
