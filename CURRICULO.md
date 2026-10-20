# Currículo

Marque só o que você sabe explicar sem consultar o código.

Replanejado em 2026-10-06 (sessão 18): a ordem segue o que o sistema
precisa para ser construído, e a prioridade vem das vagas de Engenheiro
de IA e Forward Deployed Engineer. SQL não é bloco: entra em cada bloco
por necessidade do projeto.

## Concluído

- [x] Modelagem dimensional, star schema (sessão 18)

## Bloco A — Python de produção + dado (06/10 a 17/10)

- [ ] Estrutura de projeto e packaging
- [ ] Pydantic e tipagem
- [ ] Contrato de dado
- [ ] pytest e fixture
- [ ] Batching (`COPY` × `INSERT` linha a linha, medido)
- [ ] Dado sujo: gap, outlier, dessincronia
- [ ] Window functions, CTE (dedup, espera entre trechos)
- [ ] Leitura de query plan e otimização

Cortado na reavaliação de 2026-10-19 (sessão 23): batching, dado sujo,
window functions e query plan saem do bloco A. Voltam quando o projeto
precisar ou como conceito de entrevista. O gerador pequeno passa para o
início do bloco B.

## Bloco B — Agente (20/10 a 31/10)

- [ ] Golden set versionado (escrito antes do agente)
- [ ] Design de ferramenta: descrição, schema, granularidade
- [ ] Loop do agente: planejamento, parada, limite de passos
- [ ] Memória e engenharia de contexto
- [ ] Structured output com schema
- [ ] Rate limit, retry com backoff, fallback entre providers
- [ ] Modos de falha e versionamento de API
- [ ] MCP como padrão de conector

## Bloco C — API + container (03/11 a 14/11)

- [ ] async/await, código I/O-bound, quando NÃO usar
- [ ] FastAPI
- [ ] Mock de chamada externa (LLM) no teste
- [ ] Connection pooling
- [ ] Streaming e latência percebida
- [ ] Profiling
- [ ] Docker multi-stage, imagem enxuta, reprodutibilidade

## Bloco D — Evals + RAG (17/11 a 28/11)

- [ ] recall@k e precision@k separados de groundedness
- [ ] RAGAS, LLM-as-a-judge e seus vieses
- [ ] Regressão em CI, prompt versionado
- [ ] Chunking hierárquico com metadado
- [ ] pgvector: índice, HNSW vs IVFFlat
- [ ] Busca híbrida (BM25 + densa) e reranking (se sobrar)

## Bloco E — Operar e mostrar (01/12 a 12/12)

- [ ] Tracing, custo e latência por request
- [ ] Serverless vs orquestrado: quando cada um
- [ ] IAM e rede
- [ ] Controle de custo
- [ ] CI/CD do sistema (testes + evals no GitHub Actions)
- [ ] Canary e rollback (revisões do Cloud Run)

## Prontidão para entrevista (contínuo, domingo)

- [ ] `ARQUITETURA.md`: escada de 5 perguntas em cada decisão
- [ ] `HISTORIAS.md`: 8 histórias STAR completas
- [ ] Pitch de 2 min do projeto, em inglês, sem ler
- [ ] Deep dive de 45 min sem travar numa decisão

## Só conceito (1 sessão cada, para responder em entrevista)

Não serão construídos. Motivo: no ritmo medido (18 sessões no item 1),
construir tudo isso empurraria LLM, agente e evals para depois de 2027.

- [ ] Airflow ou Dagster: DAG, retry, backfill, idempotência
- [ ] dbt: model, test, lineage
- [ ] ETL vs ELT
- [ ] Batch vs streaming (Kafka opcional)
- [ ] Parquet, particionamento
- [ ] K8s: deployment, service, probes, HPA, secrets, resource limits
- [ ] Rolling update e rollback no K8s
- [ ] Terraform
- [ ] Roteamento de modelo por tarefa e custo
- [ ] Cache de prompt e cache semântico
- [ ] Human-in-the-loop e portão de aprovação (o agente só lê)
- [ ] Idempotência e side effects em agente
- [ ] Versionamento de modelo e dado (MLflow ou DVC)
- [ ] Drift e gatilho de retreino

## Fora de escopo (decisão consciente)

ML clássico (#5), séries temporais, visão computacional,
protocolo industrial, otimização, governança regulada,
dado clínico. Frontend Next.js (só se sobrar tempo depois do
bloco E). Dado real e troca de domínio (decisão da sessão 18).
