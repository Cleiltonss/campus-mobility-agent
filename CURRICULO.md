# Currículo

Ordem = ranking de exigência de vagas.
Marque só o que você sabe explicar sem consultar o código.

## Fase 1 — Engenharia de dados e SQL (sem 1-4) — #1

- [x] Modelagem dimensional, star schema
- [ ] Window functions, CTE
- [ ] Leitura de query plan e otimização
- [ ] Airflow ou Dagster: DAG, retry, backfill, idempotência
- [ ] dbt: model, test, lineage
- [ ] Contrato de dado
- [ ] ETL vs ELT
- [ ] Batch vs streaming (conceito; Kafka opcional)
- [ ] Dado sujo: gap, outlier, dessincronia
- [ ] Parquet, particionamento

## Fase 2 — Python de produção (sem 5-7) — #2

- [ ] async/await, código I/O-bound, quando NÃO usar
- [ ] FastAPI, Pydantic, tipagem
- [ ] pytest, fixture, mock de chamada externa
- [ ] Estrutura de projeto e packaging
- [ ] Profiling
- [ ] Batching e connection pooling

## Fase 3 — Cloud e containers (sem 8-11) — #3

- [ ] Docker multi-stage, imagem enxuta, reprodutibilidade
- [ ] Serverless vs orquestrado: quando cada um
- [ ] K8s: deployment, service, probes
- [ ] K8s: HPA, secrets, resource limits
- [ ] Rolling update e rollback
- [ ] Terraform do zero
- [ ] IAM e rede
- [ ] Controle de custo

## Fase 4 — LLM em produção (sem 12-13) — #4

- [ ] Roteamento de modelo por tarefa e custo
- [ ] Structured output com schema
- [ ] Streaming e latência percebida
- [ ] Cache de prompt e cache semântico
- [ ] Rate limit, retry com backoff, fallback entre providers
- [ ] Modos de falha e versionamento de API

## Fase 5 — Agentes e orquestração (sem 14-15) — #6

- [ ] Design de ferramenta: descrição, schema, granularidade
- [ ] Loop do agente: planejamento, parada, limite de passos
- [ ] Memória e engenharia de contexto
- [ ] Human-in-the-loop e portão de aprovação
- [ ] Idempotência e side effects
- [ ] MCP como padrão de conector

## Fase 6 — MLOps (sem 16) — #7

- [ ] Versionamento de modelo e dado (MLflow ou DVC)
- [ ] CI/CD de modelo
- [ ] Canary e rollback
- [ ] Drift e gatilho de retreino (conceito)

## Fase 7 — Evals e RAG (sem 17) — #8, #9

- [ ] Golden set versionado
- [ ] recall@k e precision@k separados de groundedness
- [ ] RAGAS, LLM-as-a-judge e seus vieses
- [ ] Regressão em CI, prompt versionado
- [ ] Tracing, custo e latência por request
- [ ] Chunking hierárquico com metadado
- [ ] pgvector: índice, HNSW vs IVFFlat
- [ ] Busca híbrida (BM25 + densa) e reranking

## Fora de escopo (decisão consciente)

ML clássico (#5), séries temporais, visão computacional,
protocolo industrial, otimização, governança regulada,
dado clínico.