# Progresso

Escrito pelo professor ao fim de cada sessão. Não editar à mão.

## Pontos frágeis (revisar)

- **Grão com valor específico** — escreve o grão colando um valor concreto dentro
  dele: "uma corrida de Uber casa -> trabalho", "abastecimento no posto Shell da
  Av. Brasil". O valor específico é coluna, não grão. Errou duas vezes na mesma
  sessão, corrigiu nas duas.
- **Teste de unicidade do grão** — chegou na conclusão certa ("o grão está
  errado") pelo raciocínio errado ("duplicata é irreal"). Duplicata real é
  justamente o que prova o grão errado. Ainda não é reflexo.
- **Métrica mora no fato** — inverteu três vezes seguidas antes de fixar, inclusive
  contra duas premissas que ele mesmo tinha acabado de aceitar. Fixou depois com
  a regra de bolso, mas revisar na próxima sessão sem aviso.
- **Fato snapshot periódico e métrica semi-aditiva** — visto hoje pela primeira
  vez (FIPE mês a mês). Não testado.

## Resolvido nesta sessão

- **Fato vs dimensão** (era frágil desde a sessão 1) — 10/10 no drill fechado, com
  os três erros iniciais (5, 6, 9) corrigidos por dedução, não por dica.
- **Hábito de olhar o dado** (era frágil) — abriu a fatura, trouxe o inteiro (3) e
  descreveu as três linhas com estabelecimento, valor e data.

## Nota de método

"Responder a especificação inteira" saiu da lista de pontos frágeis: parte das
respostas parciais era sobrecarga do enunciado, não desatenção. A partir da
sessão 2 o formato é **uma pergunta por vez, com o enunciado repetido junto**.
Rendimento subiu na hora.

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

### Sessão 2 — 2026-09-09
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - Dívida da sessão 1 paga: abriu a fatura do cartão. 3 linhas (Assaí R$ 138 em
    06/08, Uber R$ 20 em 04/08, DIA R$ 38,50 em 01/08).
  - Drill fechado de 10 itens: 7/10 na primeira tentativa, 10/10 após correção
    por dedução. Erros iniciais: Uber classificado como dimensão, calendário
    como "nem um nem outro", FIPE mês a mês como dimensão.
  - Regra de bolso fixada: **número que soma -> fato; palavra que filtra ->
    dimensão**.
  - Descobriu sozinho, ao tentar classificar a tabela FIPE, que uma linha de fato
    é feita de **chaves de dimensão + métricas**. Foi o melhor momento da sessão.
  - Grãos escritos e corrigidos para: fatura, corrida de Uber, abastecimento,
    manutenção, multa.
  - Decisão de modelagem correta e sem ajuda: uma tabela única de manutenção com
    coluna `tipo_de_serviço`, em vez de uma tabela por tipo de serviço.
  - Conceitos novos: dimensão de data; fato snapshot periódico; métrica
    semi-aditiva.
  - Zero linha de código. Correto para a etapa.
- Quebrou:
  - Inverteu "métrica mora no fato" três vezes seguidas, inclusive depois de
    aceitar as duas premissas que levavam à conclusão oposta. Só fixou quando a
    definição foi dada explicitamente.
  - Inventou um terceiro tipo de tabela ("tabela de métrica") para escapar do
    binário fato/dimensão.
  - Colou valor específico dentro do grão duas vezes.
  - A.1 respondida sem o número de linhas por ano que foi pedido.
- Decisões tomadas:
  - Formato da aula muda: uma pergunta por vez, com o enunciado repetido junto.
    Pedido dele, e o rendimento confirmou.
- Retomo em:
  1. Revisão sem aviso: métrica mora em qual tabela, e por quê.
  2. O domínio ainda não tem tabela fato de volume real. Definir os processos de
     negócio do domínio automobilístico que geram evento frequente
     (abastecimento, corrida de Uber/transporte, manutenção, multa) e escolher
     qual vira a primeira tabela fato do projeto.
  3. Primeiro esboço de star schema no papel: 1 fato + as dimensões que o cercam.
