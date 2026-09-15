# Progresso

Escrito pelo professor ao fim de cada sessão. Não editar à mão.

## Pontos frágeis (revisar)

- **Não olhar a tela** — respondeu "n sei"/"n lembro" 4 vezes na sessão 4 para
  informação escrita 2-3 mensagens acima. Não é memória, é não reler. Antes de
  aceitar "n lembro", mandar ele olhar.
- **Inventar valor para não deixar coluna vazia** — duas vezes na sessão 4
  (número da linha do metrô, "híbrido ou não" no ônibus). O caso "não existe
  valor" é o caso que importa: é ele que gera NULL em FK.
- **NULL em FK dentro de JOIN** — derivado por inteiro na sessão 5, mas o ponto
  de partida continua errado: chutou 65 (soma tudo) antes de rodar o JOIN. Sabe
  derivar, não sabe de cara. Testar de novo daqui a duas sessões, sem andaime.
- **Responder contra o que acabou de derivar** — sessão 5, duas vezes seguidas:
  disse que `0 = 0` é verdadeiro e que a linha entra no SUM, e no passo seguinte
  respondeu que a soma continuava 35. Não é desconhecimento, é não reler a
  própria resposta de duas linhas acima. Mesma raiz de "não olhar a tela".
- **Número sem rótulo** (nome novo para "aritmética contaminada") — os três erros
  de conta das sessões 3 e 4 são o mesmo mecanismo: levou o número e deixou a
  unidade para trás. `7` sem `km/dia`, `8.640` sem `horas/ano`, `24` sem
  `linhas`. Regra fixada por ele: número entra na conta com o rótulo colado; se
  não souber escrever o rótulo, não pode usar o número ainda.
- **Julgar número antes de calcular** — disse "é um número muito alto" antes de
  dividir 5.000.000 por 730. Deu 6.849, que é uma empresa média.
- **Chutar premissa em vez de derivar** — sessão 4: inventou "1 a 2
  abastecimentos por semana" e reaproveitou o 7 de "7 km/dia" como capacidade de
  tanque (7 L). Dado sintético exige premissa com fonte, não número de cabeça.
- **"Métrica" como palavra** — sabe o conceito (aponta R$ 138 como métrica na
  hora), mas erra a frase "métrica mora no fato" toda vez que a pergunta é
  abstrata. Quarta inversão na sessão 3. Só acerta quando ancorado num exemplo
  concreto. Perguntar sempre com exemplo junto, nunca no abstrato.
- **Nome de tabela carregando fornecedor** — propôs `fato_uber`, depois
  `tabela_uber`, depois `dim_carro`. Na sessão 4 reincidiu duas vezes: chamou o
  fato de "tabela de corridas de uber" e escreveu "uber" dentro do próprio grão.
  Cinco vezes o mesmo erro: o nome não comporta o segundo caso (ônibus, metrô).
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

### Sessão 4 — 2026-09-14
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - **`fato_transporte` fechado.** 7 colunas de chave e 3 métricas:
    - chaves: `origem_id`, `destino_id` (role-playing sobre `dim_local`),
      `data_inicio_id`, `data_fim_id` (role-playing sobre `dim_data`),
      `modal_id`, `categoria_id`, `usuario_id`
    - métricas: `distancia`, `duracao`, `valor`
  - **Grão travado:** "uma linha de `fato_transporte` é um deslocamento de um
    ponto a outro em um único modal." Derivado pelo teste metrô + Uber = duas
    linhas, não uma. Ele acertou o teste antes de saber escrever a frase.
  - **Role-playing generalizado por ele.** Aplicou o conceito a `dim_data`
    (saída/chegada) sem ser pedido, depois de derivar em `dim_local`.
  - **Regra fixada:** role-playing = uma tabela de dimensão, várias colunas de
    chave no fato. Uma tabela não é uma coluna.
  - **`dim_categoria` descoberta.** Viu que UberX/Comfort/Black não são modais:
    "são categorias de uber". Modal é o meio; categoria é o nível de serviço.
  - **FK de fato não aceita NULL.** Dimensão ganha membro "Não se aplica" com
    chave conhecida (0 ou -1). Ele respondeu `0` — resposta padrão, e foi dele.
  - **Estratégia de volume decidida:** população simulada. 730 linhas/ano × N
    pessoas. 5.000.000 / 730 = 6.849 pessoas. `dim_usuario` entra no schema.
  - Zero linha de código. Correto para a etapa.
- Quebrou:
  - **Lacuna de 5 dias = perda total de contexto.** Abriu a sessão com "lembro
    nada". Não recuperou nada da sessão 3 sem andaime.
  - **Nome carregando fornecedor: 4ª e 5ª vez.** Chamou o fato de "tabela de
    corridas de uber"; mais tarde escreveu "uber" dentro do próprio grão.
  - **Número chutado.** Disse 730 abastecimentos/ano ("1 a 2 por semana") sem
    derivar — e o número contradizia a própria conclusão dele.
  - **Número contaminado.** Usou 7 L como capacidade de tanque, reaproveitando
    o 7 de "7 km/dia" que estava na tela.
  - **Unidade trocada.** Pedido litro, respondeu R$ 270.
  - **"n sei / n lembro" para informação visível na tela**, 4 vezes. Não era
    memória: era não olhar.
  - **Inventou valor pra não deixar coluna vazia, 2 vezes** (número da linha do
    metrô, "híbrido ou não" no ônibus). Fugiu do caso "não existe valor".
  - **Achou que NULL em JOIN vira 0.** Vira linha sumida — e relatório errado
    sem erro nenhum. Modo de falha silencioso.
  - **Chutou "é um número muito alto" antes de dividir.** A conta deu 6.849,
    que é uma empresa média. A aritmética derrubou o palpite em 5 segundos.
- Método:
  - Pediu duas vezes pra seguir depois do ponto de fadiga, contra recomendação
    explícita. Rendimento da segunda metade foi baixo: passo mínimo, muita
    repetição, respostas de uma palavra. A sessão 3 foi encerrada nesse mesmo
    sinal e rendeu mais.
  - Sessão encerrada por estouro de tempo dele, sem as 3 frases de consolidação.
- Aberto (decidir na próxima):
  - `dim_hora` (tarifa dinâmica) foi levantada na sessão 3 e não entrou no
    schema. Decidir se entra ou se vira atributo de `dim_data`.
  - `data_fim_id` é derivável de `data_inicio` + `duracao`. Decidir se fica.
    Coluna redundante pode ficar inconsistente.
  - Nomear o grupo real de ~7.000 pessoas. Premissa declarada, não número solto.
- Retomo em:
  1. Revisão com exemplo concreto: FK NULL num JOIN — o que acontece com a linha.
  2. Fechar os 3 itens em aberto acima.
  3. Escrever o star schema completo em um arquivo do repositório. Primeiro
     artefato versionado do projeto.

### Sessão 4 — continuação (mesmo dia, 2026-09-14)
Retomada a pedido dele, depois do encerramento. Substitui o "Retomo em" acima.

- Feito:
  - **Premissa de volume fechada, com dono e decisão.** Universidade de ~7.000
    alunos; a reitoria decide frota e rotas de fretado. Saiu de "7.000 pessoas"
    solto para premissa defensável em entrevista.
  - **Furo achado e consertado.** A decisão que ele propôs primeiro ("quantos
    ônibus comportam 7.000 alunos") é uma divisão, não precisa de histórico
    nenhum. As decisões que exigem o fato são **onde** fica o ponto de embarque
    (agrupar por bairro de origem, `dim_local`) e **que horas** o fretado sai.
  - **Item em aberto nº 1 fechado, por argumento dele:** `dim_hora` separada,
    24 linhas, congelada pra sempre; `dim_data` continua 365/ano. O desenho
    fundido (8.640 linhas/ano) não economiza nada, porque a coluna `hora` tem
    que existir nos dois desenhos. Ele escolheu fundido primeiro e virou sozinho
    quando viu isso.
  - **Role-playing aplicado pela terceira vez, sem ajuda:** `hora_inicio_id` e
    `hora_fim_id`. Fato vai a **9 colunas de chave** e 3 métricas.
  - **Redundância identificada:** `data_fim`/`hora_fim` são deriváveis de início
    + `duracao`. Numa linha com início 7h00, duração 30min e fim 9h00, ele viu
    que não há como saber qual dos três está errado.
- Quebrou:
  - **Aritmética contaminada, 2 vezes.** `8640*365*24` (8.640 já era horas/ano,
    contou três vezes) e `24*12*265` para uma tabela que tem 24 linhas. Mesmo
    padrão do tanque de 7 L: número da tela entra na conta sem checar unidade.
  - **"n sei"/"n lembro" para coisas triviais** — inclusive "quantas vezes as 7h
    acontecem num ano".
- Falha do professor (minha, não dele):
  - Entreguei resposta pronta pelo menos 3 vezes no fim (`365`, `hora`, `24`)
    em vez de fazer pergunta. Ele apontou isso sozinho e estava certo.
  - Causa: sessão esticada muito além do sinal de fadiga. Ele pediu pra seguir
    3 vezes; eu segui. A sessão 3 foi cortada no mesmo sinal e rendeu mais.
  - **Regra nova: quando eu começar a entregar resposta, a sessão acabou.**
    Esse é o sinal objetivo, não o cansaço declarado.
- Aberto (decidir na próxima):
  - `data_fim`/`hora_fim` ficam ou saem? Redundância que pode ficar
    inconsistente contra 4 colunas a menos e cálculo em query time.
  - Nomear a universidade e declarar as premissas do gerador por escrito.
- Retomo em:
  1. Revisão com exemplo concreto: FK NULL num JOIN — o que acontece com a linha.
  2. Decidir `data_fim`/`hora_fim`.
  3. Escrever o star schema completo em arquivo versionado do repositório.
     Primeiro artefato do projeto. **Sem começar sessão nova antes disso.**

### Sessão 5 — 2026-09-14
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - **Diagnóstico dos erros de conta fechado, e por dedução dele.** Partiu de
    "erros de unidade" (que é o sintoma) e chegou em "levei só o número" (que é
    o mecanismo) depois de tentar converter 7 km/dia em litros e ver que não
    existe fator. Regra que saiu disso está nos pontos frágeis.
  - **FK NULL num JOIN derivado até o fim, com exemplo de 3 linhas.** Rodou o
    JOIN na mão: NULL não casa com nada, a linha não entra, `SUM` devolve 35 e
    o total real é 65. Depois fechou o contraste: query que estoura é barata,
    query que devolve número errado sem reclamar roda seis meses.
  - **Nome do modo de falha aprendido: falha silenciosa.**
  - **Membro "Não se aplica" validado no mesmo exemplo.** Com `origem_id = 0` e
    a linha `0 | Não se aplica` na dimensão, `0 = 0` casa, a linha sobrevive e
    o relatório volta a 65. A FK sem NULL deixou de ser regra decorada.
  - **Tela A vs Tela B.** Confusão legítima, e o enunciado era meu: separar a
    tabela crua (que o professor mostra) do relatório agregado (que o analista
    recebe). Ele estava certo sobre o que via.
  - Zero linha de código. **Pela quinta vez — e dessa vez não está correto.**
- Quebrou:
  - Chutou 65 antes de rodar o JOIN, e chutou "erro" no caso da chave 0. Nos
    dois, a derivação passo a passo consertou em 3 perguntas.
  - "N sei" antes de tentar, na pergunta sobre o uso de `hora_fim`. Com o
    problema reduzido ("que horas o aluno chega"), respondeu certo na hora.
  - Respondeu contra a própria derivação, 2 vezes.
- Ponto levantado por ele, e procedente:
  - **"Por que não avançamos pros códigos?"** O diagnóstico dele ("estudo
    superficial em conceito") está errado — o conceito é que estava sendo
    testado, e ele errou 35 vs 65. Mas a cobrança está certa: 5 sessões, 4
    markdowns de processo, nenhum artefato do projeto no repositório.
  - **Falha do professor: sequenciamento.** O item 3 da sessão 4 já era escrever
    o schema em arquivo, marcado "sem começar sessão nova antes disso", e a
    sessão 5 abriu com revisão em vez do arquivo. A revisão valia — mas devia
    ter sido 15 minutos, não a sessão inteira.
  - **Regra nova: nenhuma sessão da fase 1 termina sem arquivo novo ou arquivo
    alterado no repositório.** Markdown de processo não conta.
- Aberto (decidir na próxima):
  - `data_fim_id` / `hora_fim_id` ficam ou saem. Chegou até "a coluna é útil, a
    reitoria precisa da hora de chegada" e até "dá pra calcular de
    `hora_inicio + duracao`". Faltou o último passo: o que se ganha guardando,
    em 5 milhões de linhas, contra o risco de os três campos discordarem.
  - Formato do artefato: `schema.md` ou `schema.sql`. Recomendação minha é
    `.sql` — é código real, é o que o entrevistador abre, e ele escreve.
  - Nomear a universidade e declarar as premissas do gerador por escrito.
- Retomo em:
  1. **Escrever o schema em arquivo versionado. Primeiro item da sessão, antes
     de qualquer revisão.** `fato_transporte` com as 9 chaves e 3 métricas, mais
     as dimensões: `dim_local`, `dim_data`, `dim_hora`, `dim_modal`,
     `dim_categoria`, `dim_usuario`.
  2. Fechar `data_fim`/`hora_fim` enquanto escreve — a decisão vira ou não vira
     coluna no arquivo.
  3. Revisão hostil do que ele escreveu: tipo, PK, FK, membro 0 em cada
     dimensão.
