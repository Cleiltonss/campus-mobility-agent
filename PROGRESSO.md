# Progresso

Escrito pelo professor ao fim de cada sessão. Não editar à mão.

## Pontos frágeis (revisar)

- **Não olhar a tela** — respondeu "n sei"/"n lembro" 4 vezes na sessão 4 para
  informação escrita 2-3 mensagens acima. Não é memória, é não reler. Reincidiu
  na sessão 6 na forma mais crua possível: respondeu "3" três vezes seguidas
  para uma contagem cuja resposta era 1, com as duas tabelas desenhadas na tela.
  **Antídoto que funcionou, e é ferramenta padrão a partir de agora: mandar ele
  copiar e colar as linhas em vez de contar de cabeça.** Resolveu em uma
  tentativa o que três perguntas não resolveram. Sessão 7, três vezes: respondeu
  `dim_local` a uma pergunta sobre hora; escreveu chave `2` nos três `INSERT`
  de uma seção intitulada "os `INSERT` do membro `-1`"; inventou a coluna
  `periodo` com `periodo_dia` escrita duas linhas abaixo na tela. **E duas
  vezes respondeu de cabeça depois de mandado escrever a lista** — o antídoto
  só funciona se ele de fato escrever.
  Sessão 8: perguntou "onde eu checo a porta?" com `5432` na primeira linha
  da minha mensagem anterior; não achou a aba Docker Hub que aparecia no
  próprio print; disse "n sei" para o nome do serviço que ele mesmo tinha
  respondido duas mensagens antes ("banco"). Colou quando mandado (o
  `CREATE TABLE`) — e aí acertou.
  Sessão 9: escreveu `USER`, `PASSWORD`, `DB` no arquivo com
  `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` em negrito na minha
  mensagem anterior. Mandado copiar os três nomes, copiou certo na primeira.
  Mandado copiar a linha `image:` do disco, copiou certo. **O antídoto
  funcionou nas duas vezes em que ele de fato colou.**
  Sessão 10: respondeu `Postgres` para "o dono que aparece na linha 2", com
  `database:` colado por ele duas mensagens antes. Pedido o endereço do erro,
  copiou o caminho do arquivo. Colou quando mandado (linhas 2, 7, 9, os dois
  endereços lado a lado) e acertou em todas.
- **Inventar valor para não deixar coluna vazia** — duas vezes na sessão 4
  (número da linha do metrô, "híbrido ou não" no ônibus). O caso "não existe
  valor" é o caso que importa: é ele que gera NULL em FK.
- **Responder contra o que acabou de derivar** — sessão 5, duas vezes seguidas:
  disse que `0 = 0` é verdadeiro e que a linha entra no SUM, e no passo seguinte
  respondeu que a soma continuava 35. Não é desconhecimento, é não reler a
  própria resposta de duas linhas acima. Mesma raiz de "não olhar a tela".
  Sessão 6, três vezes na mesma tabela: concluiu "`hora_id` pode ser a própria
  hora" e colou `dim_hora` com `hora_dia` junto, duas vezes depois de apontado.
  Sessão 7: afirmou "não existe" caso de `-1` em `dim_hora` e, dois passos
  depois, deu `-1` para a viagem de metrô sem registro de saída.
  Sessão 8, versão arquivo: derivou `postgres:18` contra `latest` com o
  argumento certo, e no disco ficou `postgres:latest`. Decidiu `banco` como
  nome do serviço, e no disco ficou `<nome_do_servico>`. **Decisão tomada no
  chat que não chega ao arquivo.**
  Sessão 9: os dois consertados no disco. Mas do nome do serviço não lembrava
  nem o valor nem o critério ("zero ideia"); rederivou pelo teste do segundo
  caso (Airflow e API no mesmo compose) e chegou em `database`.
  Sessão 10, duas vezes: completou `services.database.volumes` para a linha
  10 e respondeu "linha 10" logo depois, duas vezes, para um erro cujo
  endereço era só `volumes`. E a mais cara: concluiu na revisão que o dado
  tem que ficar "fora" do container, escreveu o volume, e apostou que as
  tabelas **não** sobreviveriam ao `down`/`up`. Versão arquivo, de novo: na
  linha 13 aplicou a primeira resposta dele ("valor na mesma linha"), que
  estava errada, e não a segunda (os dois-pontos), que estava certa.
- **Número sem rótulo** (nome novo para "aritmética contaminada") — os três erros
  de conta das sessões 3 e 4 são o mesmo mecanismo: levou o número e deixou a
  unidade para trás. `7` sem `km/dia`, `8.640` sem `horas/ano`, `24` sem
  `linhas`. Regra fixada por ele: número entra na conta com o rótulo colado; se
  não souber escrever o rótulo, não pode usar o número ainda. Reincidiu na
  sessão 6: perguntado **em quantas linhas** um texto aparecia, montou
  `2.000.000 × 12 ÷ 25` com os bytes do exercício anterior, que já tinha
  acabado. A unidade até fechava em `linhas` — respondia outra pergunta. Sinal
  novo: número que sobrou na tela é matéria-prima de conta inventada. Sessão 7: pedido
  o resultado no formato `nome_modal | soma`, respondeu `10`.
- **Vírgula sobrando antes do fecha-parêntese** — quatro vezes na sessão 6,
  em três tabelas. Mecânico, não conceitual, mas para o arquivo inteiro. Ele
  ainda não rodou o SQL em banco nenhum — é erro que sumiria sozinho no
  primeiro `psql`.
  Sessão 7, mais três da mesma família: `==` em vez de `=`, `;` faltando nos
  três `INSERT`, nome de coluna inventado. **Sétima sessão sem rodar nada.**
- **Número lido como posição, não como valor** — sessão 7: disse que
  `hora_id = 99` era "posição 100", numa tabela vazia. `PRIMARY KEY` não
  numera posição e não sabe quantas linhas existem. Mesma raiz do off-by-one da
  sessão 6 (7h → 6), e reincidiu na mesma troca: respondeu "0 a 23" e "24
  valores" certo, e logo depois que `24` estava entre os válidos.
- **Arquivo não salvo** — sessão 6 e sessão 7 (2 vezes). Cola do buffer e diz
  que está pronto. Verificar no disco antes de aceitar, sempre. Sessão 8:
  salvou nas duas vezes pedidas. Melhorou — mas ver "decisão que não chega ao
  arquivo" em "Responder contra o que acabou de derivar".
  Sessão 9: 1 vez em 6 ("pronto" com `postgres:latest` ainda no disco). A
  pista da bolinha na aba do VS Code resolveu na segunda.
  Sessão 10: 1 vez (colou `- Airflow:database` do buffer; o disco ainda tinha
  `<nome_vol>:<caminho>`). Nas outras quatro, salvou.
- **Servidor × esquema** — sessão 8: derivou sozinho que o servidor sobe
  antes das tabelas e existe sem elas. Mesmo assim pôs as tabelas dentro do
  `docker-compose.yml` três vezes (na mensagem ao colega, em "o que precisa
  conter no servidor", em "monta toda a estrutura de banco"). Compose sobe
  servidor vazio; `schema.sql` cria as tabelas.
- **Fecha a sessão em sintaxe, não em mecanismo** — as 3 frases da sessão 7
  foram todas forma (`CHECK` valida, `-1` é não se aplica, `INSERT INTO` é
  assim). O porquê que ele tinha derivado 20 min antes não voltou nem na
  segunda tentativa. Sinal de que o raciocínio da sessão não virou memória.
  Sessão 8: 1 de 3 com mecanismo (servidor antes das tabelas, "pois sem
  banco não dá pra criar tabelas"). As outras duas foram estrutura e fato. O
  melhor da sessão — reprodutibilidade, `18` × `latest`, imagem × container —
  não apareceu em nenhuma.
  Sessão 9: de novo 1 de 3 com mecanismo (`latest`: "não saberia o que o
  colega está tendo de problema"), e com a palavra trocada: "reversibilidade"
  no lugar de reprodutibilidade. As outras duas foram fato: "postgres é
  armazenamento" sem o porquê (RAM some com o processo, disco não) e "prefixo
  `POSTGRES_`" sem o porquê (a imagem ignora, calada, nome que não reconhece).
  Chamou a imagem de "postgres desktop".
  Sessão 10: 1 de 3 pela terceira sessão seguida. A com mecanismo é a melhor
  das três sessões ("por conter o mesmo volume com endereço, eu recupero
  minhas tabelas"), mas sem dizer onde o volume mora. As outras duas foram
  estrutura ("services é a hierarquia pai") e descrição de comando. RAM ×
  disco, que abriu a sessão, não apareceu.
- **`latest` × versão fixa** — revisão da sessão 9, sem andaime: sabia o fato
  ("pega a versão mais atual"), não sabia a consequência. Respondeu repetindo
  a diferença de versão e tratando o problema como "o meu está
  desatualizado". "Não sei" para "por que você não consegue descobrir o erro
  do colega". Com o problema diminuído (o erro acontece na sua máquina? o que é
  diferente? o arquivo diz que é o 19?) chegou em "eu não sei qual versão ele
  está" e no contrafactual com `postgres:18`. Mecanismo alcançado com
  andaime, então ainda está frágil. Revisar sem andaime.
- **Para que serve um banco (memória × persistência)** — sessão 9. Deu como
  papel do Postgres "documentar" e depois "reflete o valor". Previu que uma
  lista Python sobrevive ao fim do script ("salvou as informações"). Rodou
  `python3 -c` duas vezes, viu `NameError`, e ainda leu "not defined" ao pé
  da letra ("não foi definida?"). Chegou em "gerado sem armazenamento" e
  então em "armazenamento". É a base de tudo o que ele está construindo:
  revisar com o mesmo experimento, sem eu rodar a conta por ele.
  Revisão da sessão 10: previu o `NameError` certo pelo motivo errado ("não
  houve armazenamento na memória"; houve). Achava que a RAM guarda o valor
  depois do fim do processo ("reativar o python3 para resgatar", "está
  armazenada em outro lugar?", "na memória ram"). **Fato entregue: processo
  termina → o sistema operacional toma a RAM de volta.** Ideia errada nova:
  "o Postgres salva as informações na nuvem". Disco saiu com andaime ("um
  arquivo?" → "HD?"). A 3ª pergunta (container apagado leva o disco de
  dentro junto) saiu certa sem andaime. **E depois rodou o experimento real:
  `down`/`up`, apostou que as tabelas sumiriam, viu as três no `\dt`.**
  Continua frágil, mas agora tem uma evidência que ele mesmo produziu.
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
  Sessão 9, sexta e sétima vez: `POSTGRES_DB: Subway` (metrô), e depois
  `Modal`, que é o nome de uma dimensão só, para um banco que guarda alunos e
  bairros também. Chegou em `transportes` com a dica de `fato_uber` →
  `fato_transporte`. O teste do segundo caso ele aplica quando mandado, mas
  ainda não sozinho.
- **Prefixo `fato_` / `dim_`** — não viu que prefixo igual em todas as tabelas
  não carrega informação. Convenção entregue pronta, não deduzida.
  Sessão 10, **primeira vez deduzido por ele**: propôs `HD_externo` para o
  volume (nome pelo mecanismo, não pelo dono); o teste do segundo caso
  (volume do Airflow) gerou `HD_Airflow`; perguntado o que `HD_` diz se está
  em todos, respondeu "é redundante". Depois disso: "n sei" para o nome e
  `Airflow` escrito no volume do Postgres. Chegou em `database` copiando a
  linha 2.
- **Botão Run do Docker Desktop** — 3 vezes (duas na sessão 8, uma na 10). Na
  10, deduziu pela evidência que o Run não lê o compose: `docker ps -a`
  mostrou `IMAGE postgres:latest` contra `18` no arquivo, e erro de senha com
  senha na linha 8. Frase dele: "ele não rodou meu compose". Regra fixada:
  **Docker Desktop é só para olhar; quem lê o arquivo é `docker compose`.**
- **Ler mensagem de erro** — sessão 10. Leu `services.ports must be a
  mapping` respondendo "mapping?"; tomou o caminho do arquivo pelo endereço;
  a palavra "endereço" colidiu com caminho de disco. Destravou com lacuna
  (`_____._____.volumes`) e com a pergunta reduzida ("que palavra vem antes do
  ponto?"). Mas, entendida a hierarquia, **consertou a indentação no arquivo
  antes de responder**, e explicou certo depois. Habilidade nova, frágil.
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
- **NULL em FK dentro de JOIN** (sessão 6) — o teste marcado na sessão 5
  ("daqui a duas sessões, sem andaime") foi aplicado uma sessão depois e passou
  frio: NULL não casa com nada, a linha não aparece no INNER JOIN, o `SUM` não
  soma o valor dela e o número chega errado no relatório **sem erro nenhum**.
  Três perguntas, três acertos, zero andaime.
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

### Sessão 6 — 2026-09-15
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - **`modelo/schema.sql` existe. Primeiro artefato de código do projeto**, na
    sexta sessão. Três dimensões escritas por ele, linha por linha:
    `dim_modal`, `dim_categoria`, `dim_hora`. SQL válido.
  - **FK NULL em JOIN: aprovado sem andaime.** Ver "Resolvido".
  - **Defesa da chave substituta derivada inteira, nas duas pernas.**
    Espaço: 25 bytes de texto contra 4 de inteiro = 21 bytes/linha ×
    5.000.000 de linhas = 105 MB, por coluna, e o fato tem 9 colunas de chave.
    Manutenção: renomear um modal é `UPDATE` em **1** linha contra
    **2.000.000**. Terceira perna entregue por mim: enquanto 2.000.000 são
    reescritas, o relatório mostra dois modais onde existe um.
  - **`UNIQUE` em coluna de nome.** Viu que `PRIMARY KEY` protege só o id e que
    `NOT NULL` não impede repetição — `1│ônibus` e `7│ônibus` passam, e o
    relatório mostra dois ônibus com metade do gasto cada. Mesmo estrago do
    rename pela metade, por outra porta, de novo silencioso.
  - **Régua fixada: `UNIQUE` vai na coluna que identifica a linha, não na que
    agrupa linhas.** Derivada por teste concreto: com `UNIQUE` em `periodo_dia`,
    `dim_hora` nunca passaria de ~5 linhas, e precisa de 24.
  - **Chave natural × chave substituta.** Escolheu `hora_id` = a própria hora
    (0–23) em vez de id inventado, pelos dois motivos certos: a hora já é única
    e nunca muda de nome. Modal muda de nome, hora não.
  - **Membro "Não se aplica" mudou de `0` para `-1`**, proposta dele. O
    argumento ele não achou sozinho (perguntado qual dimensão tem `0` como valor
    real, respondeu `dim_usuario`), mas fechou depois: `hora_id = 0` é
    meia-noite, hora real e cara. Regra uniformizada: `-1` em todas as
    dimensões.
  - **Dimensão de rótulo.** Viu que `dim_hora` só com `hora_id` não serve pra
    nada, porque a reitoria não pergunta "quantas viagens às 7h", pergunta
    "quantas no pico da manhã". `periodo_dia` entrou por isso.
  - **Convenção de nome fechada: sufixo `_id`**, e ele deu a razão certa — a
    parte antes do `_id` nomeia o **papel**, não a tabela. É o que faz
    `origem_id` e `destino_id` conviverem apontando pra `dim_local`.
  - **Ordem das tabelas no arquivo: dimensões primeiro.** Chegou na ordem certa
    pela razão errada ("servem de filtro" — isso é tempo de query). A razão é
    tempo de criação: a FK do fato referencia uma tabela que precisa já existir.
  - **Role-playing: errou e se corrigiu sozinho.** Escreveu `dim_hora` com
    `hora_partida` e `hora_chegada` dentro — os papéis dentro da dimensão.
    Lembrado da própria frase da sessão 4 ("uma tabela não é uma coluna"),
    consertou sem eu dar a resposta.
- Quebrou:
  - **Contagem de 5 linhas errada três vezes seguidas.** Ver "Não olhar a tela".
  - **Conta inventada com bytes** numa pergunta que era de contagem. Ver
    "Número sem rótulo".
  - **`hora_dia` mantida três vezes** depois de concluir que era redundante.
  - **Off-by-one nos valores da hora:** 7 da manhã → escreveu 6; 23h → 22.
    Levou a posição na lista em vez do valor. Mesmo mecanismo, outra roupa.
  - **"n sei" antes de tentar, 2 vezes** — inclusive para "quais são os 24
    valores de uma tabela de horas".
  - Vírgula sobrando antes do `)`, 4 vezes.
  - Não percebeu que o arquivo não tinha sido salvo; colava do buffer.
- Método:
  - **Encolher o problema funcionou de novo.** 5.000.000 de linhas → 5 linhas
    na tela, e o raciocínio destravou na hora.
  - **Copiar e colar em vez de contar de cabeça** é a descoberta de método da
    sessão. Adotar sempre que vier resposta contra o que está escrito na tela.
  - Ele pediu a sintaxe de `CREATE TABLE` ("não conheço"). Entregue como
    gramática + exemplo de um domínio que não é o dele (`dim_cor`). Decisão
    correta: sintaxe é conhecimento, modelagem é raciocínio.
- Aberto (decidir na próxima):
  - **`CHECK` em `dim_hora`** para travar `hora_id` entre 0 e 23. Deixado como
    isca para abrir a sessão 7 — ele foi avisado.
  - `INSERT` do membro `-1` em cada dimensão. Nenhum foi escrito ainda.
  - Faltam `dim_local`, `dim_data`, `dim_usuario` e `fato_transporte`.
  - **`data_fim_id` / `hora_fim_id` ficam ou saem — terceira sessão em aberto.**
    Decidir quando escrever o fato, não antes.
  - Nomear a universidade e declarar as premissas do gerador por escrito.
- Retomo em:
  1. `CHECK` em `dim_hora`: qual restrição impede `hora_id = 99`.
  2. Escrever `dim_usuario` e `dim_local` — e `dim_local` levanta pergunta nova:
     o que é uma linha dela, um endereço ou um bairro?
  3. Os `INSERT`s do membro `-1`.

### Sessão 7 — 2026-09-16
- Fase: 1, semana 1 — modelagem dimensional e star schema
- Feito:
  - **Primeiro `CHECK` do projeto**, escrito e defendido por ele:
    `CHECK (hora_id BETWEEN 0 AND 23 OR hora_id = -1)`.
  - **`CHECK` descreve o válido, não o proibido.** Derivado por contagem: 24
    valores válidos contra lista infinita de inválidos nos dois sentidos
    (`24, 25, …` e `-1, -2, …`). Proibido não se lista.
  - **Conflito entre duas decisões dele mesmo, achado e resolvido.** O
    `CHECK (hora_id >= 0 AND hora_id <= 23)` bloqueava o membro `-1` decidido
    na sessão 6. Ele afirmou "não existe caso de -1 na dim_hora" e dois passos
    depois, diante do caso concreto (catraca do metrô registra entrada e não
    registra saída), respondeu `-1` sem hesitar.
  - **Escolheu a versão B do `CHECK` com argumento próprio.** Entre
    `>= -1 AND <= 23` e `BETWEEN 0 AND 23 OR = -1` — que aceitam e recusam
    exatamente os mesmos valores — escolheu a segunda ao ver que a primeira faz
    o `-1` parecer hora legítima. Reconheceu o schema como documentação.
  - **Três `INSERT` do membro `-1` escritos e salvos.**
  - **Rótulo do membro `-1` corrigido por ele.** Escreveu primeiro
    `(-1, 'onibus')`; levado ao significado da linha, viu que ela dizia "quando
    não sei o modal, o modal é ônibus", e que isso soma viagem desconhecida
    dentro do ônibus no relatório da reitoria, sem erro nenhum.
  - `modelo/schema.sql` alterado e salvo. Regra da sessão 5 cumprida.
- Quebrou:
  - **Role-playing: lembrou o resultado, não o mecanismo.** Sabia QUAIS colunas
    tinha tirado da `dim_hora` (`hora_partida`, `hora_chegada`); as duas razões
    que deu estavam erradas (meia-noite 0/24; "reitor só quer o período" — essa
    é a razão de `periodo_dia` entrar, não das outras saírem). Precisou de 5
    perguntas até "uma linha dessa tabela descreve um deslocamento", e ainda
    assim não nomeou o que a tabela virava: um segundo fato.
  - **`dim_local` como resposta a uma pergunta sobre hora**, com
    `fato_transporte` colado por ele três mensagens acima.
  - **Chave `2` nos três `INSERT`**, numa seção cujo título era "os `INSERT` do
    membro `-1`". Copiou a forma do exemplo e perdeu o enunciado.
  - **Número lido como posição.** Disse que `hora_id = 99` era "posição 100",
    em tabela vazia. Mesma raiz do off-by-one de ontem: número como lugar numa
    lista, não como valor. `PRIMARY KEY` não numera posição.
  - **Off-by-one na mesma troca.** Respondeu "0 a 23" e "24 valores"
    corretamente, e em seguida afirmou que `24` está entre os válidos.
  - **Não escreveu a lista quando mandado, 2 vezes.** Respondeu de cabeça o que
    devia ter copiado. O antídoto da sessão 6 só funciona se ele escrever.
  - **Número sem rótulo.** Pedido o resultado no formato `nome_modal | soma`,
    respondeu `10`.
  - **Arquivo não salvo, 2 vezes.** Reincidência direta da sessão 6.
  - **Sintaxe:** `==` em vez de `=`; `;` faltando nos três `INSERT`; nome de
    coluna inventado (`periodo` em vez de `periodo_dia`, com a coluna certa
    duas linhas abaixo na tela). Tudo sumiria no primeiro `psql`.
  - **As 3 frases de fechamento saíram todas em sintaxe.** "CHECK é um
    validador de condicional" é decoreba; o porquê (lista infinita de
    inválidos) ele tinha derivado 20 minutos antes e não recuperou, nem na
    segunda tentativa.
- Método:
  - **Travou de verdade uma vez** ("não to entendendo porra alguma"), quando
    empilhei duas tabelas + JOIN + agregação numa pergunta só. O que destravou
    foi **remover o JOIN**, não reduzir linhas: voltar a uma tabela e perguntar
    o que a linha `-1` significa. Encolher não é só diminuir o número de
    linhas — é tirar uma operação inteira. Falha do enunciado, minha.
  - Isca plantada para a sessão 8, e ele foi avisado: "Não se aplica" e
    "Desconhecido" não são a mesma coisa. Metrô não tem categoria de serviço
    (não se aplica); a hora de saída do metrô existe e não foi registrada
    (desconhecida). Se as duas caem em `-1`, a diferença some.
- Aberto (decidir na próxima):
  - `-1` é um membro só ou dois ("Não se aplica" × "Desconhecido")?
  - Faltam `dim_local`, `dim_data`, `dim_usuario` e `fato_transporte`.
    `dim_local` levanta pergunta nova: uma linha dela é um endereço ou um
    bairro?
  - **`data_fim_id` / `hora_fim_id` ficam ou saem — quarta sessão em aberto.**
    Argumento novo de hoje: o caso do metrô mostra que a hora de fim pode ser
    desconhecida já no dado de origem.
  - Nomear a universidade e declarar as premissas do gerador por escrito.
  - **Rodar o `schema.sql` num Postgres.** Sete sessões, zero execução. Metade
    dos erros de hoje morreria sozinha no primeiro `psql`.
- Falha do professor (minha, segunda vez; ele me pegou nas duas):
  - Decidido que o banco sobe em Docker (**argumento dele**: "configura o
    projeto, não só a minha máquina" — reprodutibilidade). Eu então **escrevi o
    `docker-compose.yml` inteiro por ele**, apoiado na exceção de "YAML de
    infra". Ele cortou na hora: "n mano, vc n ia me ensinar?". Certo. A exceção
    existe para poupar burocracia, não para tirar dele algo que ele quer
    aprender — e código que ele não escreveu é código que ele não defende.
    Arquivo apagado. **Ele escreve na sessão 8.**
  - Mesmo sinal da sessão 4: comecei a entregar resposta pronta → sessão já
    tinha acabado. A regra existe e eu não a apliquei.
  - Antes disso ele fez duas perguntas que valeram mais que meia sessão:
    "em prod não é tudo Docker?" (derrubou meu plano de `brew install`) e
    "ou é feito mais pelo VS mesmo?" (confusão cliente × servidor, mesma
    família do Cloud Run × warehouse da sessão 1 — corrigida na hora).
- Retomo em:
  1. **Ele escreve o `docker-compose.yml`** e sobe o Postgres. Defender: por que
     volume nomeado, por que healthcheck, por que a imagem `pgvector` e não a
     `postgres` pura.
  2. `psql -f modelo/schema.sql` — ler os erros do banco e consertar sozinho.
  3. Revisão sem andaime: por que o `CHECK` descreve o válido e não o proibido.
  4. `-1`: um membro ou dois.
  5. `dim_local` — o que é uma linha dela.

### Sessão 8 — 2026-09-27
- Fase: 1, semana 1 — Postgres local em Docker
- Contexto: 11 dias sem sessão. Abriu com "lembro de nada"; com uma pista
  ("n mano, vc n ia me ensinar?") recuperou que eu tinha gerado o `.yml`.
- Feito:
  - **Docker × `brew install`, fechado com evidência.** Partiu de "simular
    produção" (vago). Rodou `git ls-files`: o Postgres do `brew` não está no
    repositório; o que viaja no clone é o `docker-compose.yml`. Frase dele:
    "a própria receita em código do banco". Palavra entregue:
    reprodutibilidade.
  - **Servidor antes das tabelas, com a assimetria, sozinho:** "sem banco não
    dá pra criar tabelas, mas sem tabelas o banco ativo ainda pode existir."
    Mesma lógica das dimensões antes do fato (sessão 6).
  - **Receita em 4 itens, derivada por ele:** porta (chamou de "rota"),
    usuário/senha, versão (chegou por "a data" → atualização de app no
    celular), volume (chegou por "localhost": ideia certa — fora do container
    —, palavra errada). "Container é descartável" entregue como fato.
  - **Imagem × container** pela analogia `class Carro` / `meu_carro =
    Carro()`. O print do Desktop não destravou; Python destravou em 2
    perguntas.
  - **`postgres:18` e não `latest`:** "latest é sempre a versão mais
    atualizada" → o mesmo arquivo sobe Postgres diferente conforme o dia.
    Descartou `19beta4` sozinho ao traduzir "beta" = teste.
  - **Nome do serviço pelo papel.** Propôs `Transportation_Services`; o teste
    do segundo caso (Airflow e API também são do projeto) derrubou. Chegou em
    `banco` pelo papel: "airflow são os fluxos de trabalho".
  - **Porta do host é escolha, não fato da máquina.** Achava que existia "o
    número da minha máquina". Escolheu `5432:5432` — "é mais fácil pra
    lembrar".
  - `modelo/docker-compose.yml` criado e salvo, parcial.
- Quebrou:
  - **Clicou Run no Docker Desktop duas vezes**, a segunda logo depois de
    avisado. Container `Engenheiro_IA` nasceu do clique e morreu sem senha.
    O erro foi aproveitado: leu o log e apontou `password` como o item da
    receita que faltou.
  - `latest` lido como nome da imagem.
  - Tabelas dentro do compose, 3 vezes. Ver "Servidor × esquema".
  - "n sei" 5 vezes na segunda metade.
  - `postgres:latest` e `<nome_do_servico>` no disco na hora das 3 frases,
    contra as próprias decisões.
- Falha do professor:
  - **Mandei caçar a porta na documentação**, no navegador e depois no
    Docker Desktop, cuja página da imagem é truncada (a nota no topo avisa).
    ~20 min de fricção, frustração ("para de me mandar pro navegador, vai ser
    tudo desktop"), e os dois cliques em Run aconteceram no meio da caça.
    Porta, nome de variável e caminho são fato de documentação: entregar em
    uma linha e guardar as perguntas para as decisões.
  - A mensagem com os três fatos tinha 4 parágrafos + lista. Ele não leu a
    primeira linha dela. "Uma pergunta por vez" vale para instrução também.
- Método:
  - **Analogia com código que ele já escreve** destrava conceito de infra.
  - Sessão encerrada na sequência de "n sei", antes de eu entregar resposta.
- Calendário (fato, não decisão): 8 sessões desde 2026-09-08, 11 dias
  parado entre a 7 e a 8. O conteúdo ainda é de semana 1; pelo README a fase
  1 vai até a semana 4 (~2026-10-05). Conversar na sessão 9 — sem mudar de
  fase.
- Aberto:
  - Preencher `environment` (`POSTGRES_USER`, `POSTGRES_PASSWORD`,
    `POSTGRES_DB`) e `volumes` (caminho `/var/lib/postgresql` no 18). Nome do
    volume é decisão dele — e há um volume anônimo de hash para mostrar por
    que nomear.
  - **Senha em texto puro num arquivo que vai para o GitHub.** Ainda não
    levantado. Isca da revisão hostil.
  - Há um erro estrutural no arquivo que não apontei de propósito: o
    `docker compose up` vai acusar, e ele lê o erro.
  - Arquivo em `modelo/`; foi pedido na raiz. Ele defende onde fica.
  - Quando não usar `5432` do lado do Mac.
  - Herdados: `-1` um membro ou dois; `dim_local`; `data_fim_id` /
    `hora_fim_id` (quinta sessão em aberto); nomear a universidade.
- Retomo em:
  1. Revisão sem andaime, com exemplo: por que `postgres:18` e não
     `postgres:latest`.
  2. Variáveis e volume, `docker compose up`, ler o erro sozinho.
  3. `schema.sql` rodando dentro do banco. Oito sessões, zero execução.

### Sessão 9 — 2026-09-29
- Fase: 1, semana 1 — Postgres local em Docker
- Feito:
  - **Revisão `postgres:18` × `latest`**, com andaime. Ver pontos frágeis.
    Mecanismo final, dele: "eu não sei qual versão ele está", e com `18` no
    arquivo, "agora eu sei". Palavra: reprodutibilidade.
  - **Primeira execução do projeto** (não do schema): `python3 -c` duas vezes
    para testar se uma lista sobrevive ao fim do processo. Previu que sim,
    rodou, leu o `NameError`. Memória (RAM) × disco saiu da execução, não da
    minha explicação.
  - **Papel do Postgres derivado:** "armazenamento". Daí o nome do serviço,
    rederivado pelo teste do segundo caso: `database`.
  - **`docker-compose.yml` no disco com as decisões dele:** `postgres:18`,
    serviço `database`, `POSTGRES_USER: alfred`, `POSTGRES_DB: transportes`,
    tudo em minúsculo (fato entregue: Postgres converte para minúsculo o nome
    sem aspas em SQL).
- Quebrou:
  - "Não sei" em 2 das 4 perguntas da revisão, antes de diminuir o problema.
  - Papel do Postgres: "documentar", "reflete o valor".
  - Variáveis sem o prefixo `POSTGRES_`, com os nomes na tela.
  - Nome do banco: `Subway`, depois `Modal`. Ver pontos frágeis.
  - Nome do serviço: não lembrava nem o valor nem o critério da sessão 8.
- Método:
  - **Prever e rodar.** Três tentativas verbais erradas sobre o papel do
    Postgres; um experimento de dois comandos, com previsão escrita antes,
    destravou. Ele errou a previsão, e isso foi o que ensinou. Usar sempre
    que a dúvida puder ser rodada em menos de 1 minuto.
  - Copiar e colar funcionou nas duas vezes em que ele colou.
- Falha do professor:
  - Expliquei o que acontece com `PASSWORD` sem prefixo (a imagem ignora e
    o container morre sem senha) em vez de deixar o `docker compose up`
    mostrar. Eu tinha acabado de descobrir que prever e rodar funciona, e não
    usei.
  - A conversa de calendário prevista para esta sessão não aconteceu.
- Aberto:
  - **`POSTGRES_PASSWORD: 12345` em texto puro, num repositório que é
    portfólio.** A pergunta "quem consegue ler essa senha depois do push?"
    ficou sem resposta: ele encerrou a sessão nela. Se o commit de hoje levar
    a senha, `git log -p` mostra que ela fica no histórico mesmo depois de
    apagada do arquivo: usar isso como exemplo concreto.
  - Erro estrutural no arquivo, ainda não apontado: `image`, `ports`,
    `environment` e `volumes` estão no mesmo nível de `database:`, não
    dentro dele. O `docker compose up` vai acusar, e ele lê o erro.
  - Volume: nome é decisão dele; caminho é fato (`/var/lib/postgresql` no
    18). O `<nome_vol>` do bloco `volumes:` do fim também está sem `:`.
  - Arquivo em `modelo/`, e não na raiz. Ele defende onde fica.
  - **Calendário:** fase 1 vai até a semana 4 (~2026-10-05) pelo README. O
    conteúdo ainda é de semana 1, e o `schema.sql` nunca rodou. Conversar na
    sessão 10, sem mudar de fase.
  - Herdados: `-1` um membro ou dois; `dim_local`; `data_fim_id` /
    `hora_fim_id` (sexta sessão em aberto); nomear a universidade.
- Retomo em:
  1. Revisão sem andaime, com o mesmo experimento: o que acontece com uma
     lista Python quando o script termina, e por que o Postgres existe.
  2. A senha na linha 8: quem lê depois do push, e onde ela deveria morar.
  3. Volume, `docker compose up`, ler o erro estrutural sozinho.
  4. `schema.sql` rodando dentro do banco. Nove sessões, zero execução.
  5. Conversa de calendário.

### Sessão 10 — 2026-09-30
- Fase: 1, semana 1 — Postgres local em Docker
- Feito:
  - **Revisão memória × persistência**, 3 perguntas. Ver pontos frágeis.
  - **Volume nomeado escrito por ele:** `database:/var/lib/postgresql`, nome
    pelo dono, com o bloco `volumes:` de fora declarando o volume. Deduziu
    sozinho que o prefixo `HD_` seria redundante.
  - **Run do Docker Desktop desmontado com evidência.** Ver pontos frágeis.
  - **Primeiro erro de compose lido e consertado por ele.**
    `services.ports must be a mapping` → hierarquia por indentação (frase
    dele: "services > database > componentes"). Depois `volumes must be a
    mapping` → linha 13 → faltavam os dois-pontos (mapping = dicionário
    Python).
  - **Primeiro `docker compose up` do projeto:** `postgres:18`, volume
    `modelo_database`, "ready to accept connections".
  - **Primeira execução do `schema.sql`, dez sessões depois.** 3 `CREATE
    TABLE`, 3 `INSERT`, zero erro. Corrigiu `exce` → `exec` sozinho.
  - **Experimento `down`/`up`:** apostou que as tabelas sumiriam. Container
    novo (conferido pela data de criação), `\dt` mostrou as três. Explicou
    pela linha 11; com andaime chegou em "o container novo foi ligado ao
    mesmo volume".
  - `modelo/docker-compose.yml` completo e válido (`docker compose config`).
- Quebrou:
  - Revisão: RAM persistindo depois do processo; "Postgres salva na nuvem".
  - "Linha 10" duas vezes contra a própria derivação; aposta do `down`/`up`
    contra a própria revisão. Ver pontos frágeis.
  - Nome do volume: `HD_externo`, `HD_Airflow`, "n sei", `Airflow`,
    `Postgres`, até `database`.
  - **Não sabia o que é `cd`** ("como eu dei cd modelo? onde tá criado?").
    Terminal básico ainda não é chão firme.
  - "n sei" 4 vezes; no fim, "diminui mais". Pedir menor em vez de travar é
    melhor que "n sei", mas foi o sinal para fechar.
  - 3 frases: 1 com mecanismo. Ver pontos frágeis.
- Método:
  - **Prever e rodar, 3 vezes.** "vai dar certo" (errou: erro de
    indentação), "sobe" (errou: erro dos dois-pontos), "roda" (acertou),
    "não vão estar" (errou, e foi o melhor momento da sessão).
  - **Lacuna em vez de palavra ambígua.** "Endereço" virou caminho de disco
    na cabeça dele; `_____._____.volumes` resolveu na hora.
  - Copiar e colar: funcionou nas quatro vezes em que ele colou.
  - Ele perguntou se eu o fiz errar de propósito. Resposta dada: os erros já
    estavam no arquivo desde a sessão 8; o que eu fiz de propósito foi não
    apontar, para a mensagem de erro apontar.
- Falha do professor:
  - **Mensagem do `schema.sql` com quatro coisas** (segundo terminal, `cd`,
    comando, lacunas) → "entendi nada da pergunta". Mesmo erro da sessão 8.
    Uma coisa por mensagem vale para instrução, não só para pergunta.
  - Frase confusa ("o `HD_` está sendo o `fato_uber` desta sessão ao
    contrário") logo antes de um "n sei". Analogia que precisa ser decifrada
    não ajuda.
  - **Conversa de calendário não aconteceu pela segunda sessão seguida.**
- Aberto:
  - **Senha `12345` em texto puro.** Já está no histórico (commit `efbe161`
    e o de hoje). Não há remote: nada vazou ainda. **Resolver antes do
    primeiro push**, com `git log -p` como exemplo concreto do histórico.
  - **Nome do projeto no compose é `modelo`**, o nome da pasta: daí
    `modelo_database` e `modelo-database-1`. Gancho concreto para decidir se
    o compose fica em `modelo/` ou na raiz.
  - `\dt` mostra 3 tabelas. Faltam `dim_local`, `dim_data`, `dim_usuario` e
    `fato_transporte`.
  - O Postgres ficou rodando em segundo plano (`up -d`).
  - Herdados: `-1` um membro ou dois; `dim_local`; `data_fim_id` /
    `hora_fim_id` (sétima sessão em aberto); nomear a universidade.
  - **Calendário:** fase 1 termina ~2026-10-05 pelo README. Nenhum item do
    CURRICULO da fase 1 marcado. O conteúdo ainda é star schema + Postgres
    local.
- Retomo em:
  1. Revisão sem andaime: `latest` × `18`. Ele mesmo nomeou como o que
     quebrou na sessão 9.
  2. **Conversa de calendário, antes de qualquer código.** Terceira vez
     adiada.
  3. A senha: quem lê depois do push, e onde ela deveria morar.
  4. `modelo_database`: de onde veio esse nome, e onde o compose deveria
     ficar.
  5. `dim_local`: o que é uma linha dela.
