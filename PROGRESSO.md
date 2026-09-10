# Progresso

Escrito pelo professor ao fim de cada sessão. Não editar à mão.

## Pontos frágeis (revisar)

- **"Métrica" como palavra** — sabe o conceito (aponta R$ 138 como métrica na
  hora), mas erra a frase "métrica mora no fato" toda vez que a pergunta é
  abstrata. Quarta inversão na sessão 3. Só acerta quando ancorado num exemplo
  concreto. Perguntar sempre com exemplo junto, nunca no abstrato.
- **Nome de tabela carregando fornecedor** — propôs `fato_uber`, depois
  `tabela_uber`, depois `dim_carro`. Três vezes o mesmo erro: o nome não
  comporta o segundo caso (ônibus, metrô). Consumiu ~10 rodadas.
- **Prefixo `fato_` / `dim_`** — não viu que prefixo igual em todas as tabelas
  não carrega informação. Convenção entregue pronta, não deduzida.
- **Grão com valor específico** — escreve o grão colando um valor concreto
  dentro dele. Errou duas vezes na sessão 2, corrigiu nas duas.
- **Teste de unicidade do grão** — chegou na conclusão certa pelo raciocínio
  errado ("duplicata é irreal"). Duplicata real é o que prova o grão errado.
- **Análise dimensional** — inverteu divisão e multiplicação no fim da conta
  (multiplicou 78 dias/abastecimento por 365 em vez de dividir), resultado
  28.579 abastecimentos/ano. Os dois primeiros passos estavam certos. É terreno
  de mecatrônico; não deveria escapar.
- **Fato snapshot periódico e métrica semi-aditiva** — visto na sessão 2. Não
  testado ainda.

## Resolvido

- **Fato vs dimensão** (sessão 2) — 10/10 no drill fechado, com os três erros
  iniciais corrigidos por dedução, não por dica.
- **Hábito de olhar o dado** (sessão 2) — abriu a fatura, trouxe o inteiro (3) e
  descreveu as três linhas com estabelecimento, valor e data.
- **Separar métrica de dimensão ao escrever** (sessão 3) — colapsou tudo em
  "métricas" na primeira tentativa; separou correto na segunda, aplicando a
  própria régua item por item.

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

### Sessão 3 — 2026-09-09
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - **Primeira tabela fato do projeto escolhida por volume, não por gosto.**
    Derivou por análise dimensional: 7 km/dia reais -> um tanque dura 77 dias ->
    ~5 abastecimentos/ano. Contra 730 corridas/ano. Placar do domínio:
    abastecimento 5, manutenção 2, multa 3, corrida 730.
  - Descoberta importante e dele: **o domínio tem dois lados.** O transporte por
    app é dado real que ele vive; o carro é cenário simulado. Dado sintético não
    dispensa realismo — obriga a declarar a premissa (km/dia, km/l, tanque).
  - Métricas do fato definidas: valor (R$), distância (km), duração (min).
    Reconheceu que duração é métrica de decisão, não enfeite: é quanto da vida
    dele vai em deslocamento.
  - Dimensões levantadas: data, hora do dia (via tarifa dinâmica), local,
    categoria de serviço, modal, motorista (marcada como duvidosa por ele
    mesmo — não filtraria por ela).
  - **Dimensão com papel duplo** (role-playing): viu sozinho que origem e destino
    apontam para a MESMA dimensão de local.
  - Renomeou o fato de `fato_uber` para transporte, ao perceber que ônibus não
    caberia — mesmo teste que usou para consertar o grão da corrida.
  - Conceitos novos: role-playing dimension; convenção `fato_`/`dim_`; premissa
    declarada em dado sintético; "modal" como termo do setor.
  - Zero linha de código. Correto para a etapa.
- Quebrou:
  - Quarta inversão de "métrica mora no fato". Diagnóstico mudou: o conceito está
    certo, a palavra é que está solta. Com exemplo concreto ele acerta na hora.
  - Nomeação de tabela: ~10 rodadas, três nomes errados, rendimento baixo.
    Convenção `fato_`/`dim_` teve que ser entregue pronta.
  - Ao escrever o schema, jogou data/origem/destino/categoria dentro de
    "métricas". Corrigiu sozinho quando perguntado se soma `origem`.
  - Esqueceu `dim_modal` dois minutos depois de nomeá-la. Sinal de fadiga —
    sessão encerrada nesse ponto, de propósito.
- Aberto (decidir na próxima):
  - O schema está incompleto: faltam `dim_modal` e `dim_categoria`, e
    origem/destino ainda estão apontando para duas dimensões separadas em vez de
    uma `dim_local` só.
  - **730 linhas/ano é pouco** para exercitar particionamento, backfill e
    query plan. Decidir como gerar volume defensável: simular vários anos,
    várias pessoas, ou frota. Não inventar volume sem premissa.
- Retomo em:
  1. Revisão com exemplo concreto (nunca abstrata): métrica mora onde.
  2. Fechar o star schema: `fato_transporte` + todas as dimensões nomeadas,
     com origem e destino apontando para a mesma `dim_local`.
  3. Decidir a estratégia de volume do gerador sintético.
