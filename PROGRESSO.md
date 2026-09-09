# Progresso

Escrito pelo professor ao fim de cada sessão. Não editar à mão.

## Pontos frágeis (revisar)

- **Fato vs dimensão** — não separa evento (aconteceu, tem hora) de entidade
  (existe). Deu "um carro" e "um copo" como exemplos de evento. Chamou uma
  lista de especificações de veículo de tabela fato.
- **Grão vs métrica** — definiu grão como "quanto eu gastei num dia". Grão é
  o que a linha é; métrica é o que se soma.
- **Teste de unicidade do grão** — não aplica: se duas linhas podem ter o
  mesmo grão, o grão está errado.
- **Hábito de olhar o dado** — perguntado quantas linhas tinha a fatura,
  respondeu "tem várias". Não abriu a fonte. Respondeu de memória.
- **Responder a especificação inteira** — entregou parte do pedido em 3 de 5
  rodadas (pulou B.2, B.3, e os itens 2, 3, 4).

## Log

### Sessão 1 — 2026-09-08
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - Escolheu e trocou o domínio: ecommerce -> automobilístico. Motivação real
    e sustentável: decidir a compra de um carro e comparar custo de posse
    contra Uber/transporte público.
  - Conceitos introduzidos: grão; fato vs dimensão; verbo vs substantivo;
    dupla contagem por escopo misturado (exemplo do frete_pedido); dois
    processos = dois grãos = duas tabelas fato; dimensão conformada.
  - Zero linha de código. Correto para a etapa.
- Quebrou:
  - O domínio ainda não tem tabela fato. Os eventos propostos (pintura por
    sol, pane após 2 anos, sinistro de seguro) são exceções raras, ~1 linha
    por ano somadas. Não sustentam pipeline, backfill nem particionamento.
  - Exercício da fatura do cartão não foi executado.
  - Confundiu Cloud Run com warehouse.
- Decisões tomadas:
  - Não usar dado real da Solomon: dado de terceiro, provável PII, e
    inviabiliza o repositório como portfólio. Fonte será gerador sintético.
  - Sem GCP até a semana 8, conforme README (janela de 90 dias dos $300).
  - Devs da Solomon podem ser consultados sobre domínio, nunca sobre código.
  - O domínio automobilístico foi a última troca gratuita.
- Retomo em:
  1. Drill fechado de classificação fato vs dimensão. Sem busca de domínio.
  2. Trazer o número de linhas da fatura do cartão. Um inteiro.
