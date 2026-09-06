# Engenheiro IA

Projeto de estudo para reconstruir competência prática em
engenharia de IA, com foco em entrevista técnica.

## Contexto

Engenheiro mecatrônico, trabalho com IA aplicada em produção
(agentes, MCP, LLM APIs). Sei codar, mas estou enferrujado em
fundamentos. O objetivo NÃO é entregar software: é reconstruir
memória muscular e ter artefatos defensáveis em entrevista.

Tempo: 2h/dia, pós-trabalho. 17 semanas.
Fins de semana são para candidaturas, não para este projeto.

## O que estou construindo

Plataforma de agentes sobre dados operacionais. Ingere dado bruto,
modela, expõe via API async, sobe em cluster, serve um agente com
ferramentas e mede a si mesma. Cada fase adiciona uma camada.

## Fases

Ordem = ranking de exigência de vagas.

| Fase | Semanas | Ranking | Foco | Entregável |
|------|---------|---------|------|------------|
| 1 | 1-4 | #1 | Engenharia de dados e SQL | Pipeline Airflow/dbt + modelagem dimensional |
| 2 | 5-7 | #2 | Python de produção | API FastAPI async, testada e perfilada |
| 3 | 8-11 | #3 | Cloud e containers | Docker, K8s, Terraform, IAM |
| 4 | 12-13 | #4 | LLM em produção | Roteamento, structured output, cache, fallback |
| 5 | 14-15 | #6 | Agentes e orquestração | Agente com tools, MCP, human-in-the-loop |
| 6 | 16 | #7 | MLOps | Versionamento, CI/CD, canary, rollback |
| 7 | 17 | #8, #9 | Evals e RAG | Golden set + RAG híbrido medido |

ML clássico (#5) está fora do escopo destas 17 semanas.
Decisão consciente: só entra se eu voltar a mirar indústria,
energia ou saúde.

## Stack

Python 3.12, FastAPI, Postgres + pgvector, Airflow, dbt,
Docker, Kubernetes, Terraform, GCP, MLflow, Langfuse.

## Custo

Conta GCP criada na fase 3 (semana 8), não antes: os $300 de
crédito valem 90 dias a partir da criação e precisam cobrir as
fases 3 e 6. Fora dessa janela, cluster local (kind/k3d).

## Comandos

```bash
# preencher conforme o projeto cresce
```

## Estado atual

Fase 1, semana 1. Nada construído.