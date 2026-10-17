# Engenheiro IA

Projeto de estudo para reconstruir competência prática em
engenharia de IA, com foco em entrevista técnica.

## Contexto

Engenheiro mecatrônico, trabalho com IA aplicada em produção
(agentes, MCP, LLM APIs). Sei codar, mas estou enferrujado em
fundamentos. O objetivo NÃO é entregar software: é reconstruir
memória muscular e ter artefatos defensáveis em entrevista.

Alvo: Engenheiro de IA e Forward Deployed Engineer. As entrevistas
acontecem ao longo dos meses, sem data fixa: o projeto tem que estar
defensável a qualquer momento.

Tempo: 2h/dia, pós-trabalho. Segunda a sexta: construção. Sábado:
candidaturas. Domingo: dia de entrevista (2h).

Prazo: blocos A a E de 2026-10-06 a 2026-12-12. O prazo final continua
2027-01-31, e a diferença é folga para o ritmo real. Reavaliar em
2026-10-17, no fim do bloco A, com o ritmo medido.

Replanejado em 2026-10-06 (sessão 18). O roteiro de 7 fases não chegava
em LLM e RAG no ritmo medido (o item 1 levou 18 sessões), e as vagas
tratam LLM com RAG e agente como eliminatório.

## O que estou construindo

Um assistente de dados para a reitoria de uma universidade com cerca de
7.000 alunos. É um agente que responde perguntas sobre o transporte dos
alunos consultando um star schema em Postgres (text-to-SQL com
guardrails) e documentos da reitoria (RAG). Ele é servido por API async,
medido por evals e publicado em cloud. Cada bloco adiciona uma camada.

## Blocos

| Bloco | Datas | Foco | Entregável |
|-------|-------|------|------------|
| A | 06/10 a 17/10 | Python de produção + dado | Gerador sintético tipado e testado, 5M viagens carregadas |
| B | 20/10 a 31/10 | Agente | Golden set + agente text-to-SQL com guardrails, exposto via MCP |
| C | 03/11 a 14/11 | API + container | FastAPI async na frente do agente, Docker multi-stage |
| D | 17/11 a 28/11 | Evals + RAG | Execution accuracy em CI + RAG em pgvector medido |
| E | 01/12 a 12/12 | Operar e mostrar | Langfuse, deploy no Cloud Run, CI, repo público |

SQL não é bloco: entra em cada bloco por necessidade do projeto.
Airflow, dbt, K8s, Terraform e MLOps ficam como conceito de entrevista
(ver CURRICULO). ML clássico continua fora: só entra se eu voltar a
mirar indústria, energia ou saúde.

## Stack

Python 3.14 (fixo em `.python-version`, via uv), Pydantic, pytest, FastAPI, Postgres + pgvector, Docker,
MCP, Langfuse, GitHub Actions, GCP (Cloud Run).

## Custo

Conta GCP criada no bloco E, não antes: os $300 de crédito valem 90
dias a partir da criação. Até lá, tudo local em Docker.
Do bloco B em diante há custo de API de LLM: definir um teto mensal
antes da primeira chamada.

## Comandos

```bash
uv sync          # cria o .venv com o Python e as dependências fixos
uv run pytest    # roda os testes
```

## Estado atual

Bloco A, semana 2 de 2. Star schema concluído (sessão 18). Primeiro
Python na sessão 21: contrato `Viagem` (Pydantic) em `src/assistente/`,
com 2 testes em `tests/`. Postgres 18 local via `modelo/docker-compose.yml`;
`modelo/schema.sql` com o star schema completo rodando no banco:
`fato_transportes` (9 FKs, 3 métricas) e 6 dimensões (`dim_modal`,
`dim_categoria`, `dim_hora`, `dim_local`, `dim_data`, `dim_usuario`).
`dim_usuario` é SCD tipo 2 (`aluno_id` + `atual`). Fato ainda vazio.