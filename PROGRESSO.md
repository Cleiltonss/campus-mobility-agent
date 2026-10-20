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
  Sessão 12: respondeu sobre a sessão 10 quando a pergunta era a 11; fez a
  revisão do `CHECK` com o `schema.sql` aberto e a linha 12 (a do `CHECK`)
  selecionada; escreveu `check_id` para a coluna `hora_id`; "onde que ta?"
  para dois cabeçalhos de tabela três mensagens acima. Com os dois cabeçalhos
  repostos lado a lado, acertou na hora.
  Sessão 13, quatro vezes: "pegaria sábado da coluna `dia`" com `dia = 15`
  desenhado na tela; "20032026 é menor" que 15042026, de cabeça; "tem sim"
  para o `CHECK` estar no banco (não estava); procurou o `LINE 2` do erro no
  arquivo em vez do terminal. **Colando, acertou nas três vezes em que
  colou** (o `15`, os dois números um embaixo do outro, o `\d`). Uma vez
  recusou colar ("puxe vc"): repus as duas frases lado a lado e ele achou
  o comum na hora.
  Sessão 14, cinco vezes: "tem sim" para `ordem_dia` estar no banco sem ter
  rodado o `\d` (tinha digitado só `\`), mesma frase e mesmo erro da 13;
  `data_id`, uma coluna, para uma pergunta sobre linha; `quantidade` como
  nome de coluna que não existe; `endereco, bairro e cidade` para "qual
  coluna do **fato**"; `PK` no lugar do tipo. **Colando ou com a lista na
  tela, acertou nas três vezes**: a linha 45 colada deu o `-1`; a lista das
  9 chaves do fato deu `origem_id`; as duas colunas da `dim_usuario` lado a
  lado deram `usuario_id`.
  Sessão 15, três vezes: "mas que 6 dimensões?" com o `schema.sql` aberto
  no editor; "ele saiu às 22h?" para `origem_id`, com a linha
  `dim_local | origem_id, destino_id` três mensagens acima; "n lembro" para
  `duracao`, numa tabela que bastava rolar a tela para ver. **Colando,
  acertou nas três vezes**: as linhas `CREATE TABLE` deram as 6 dimensões;
  a linha da `dim_local` colada deu "porra nenhuma" para o `7 + 15`; a
  linha `local_id INTEGER PRIMARY KEY` colada deu os `REFERENCES` certos.
  Sessão 16, cinco vezes, com o `schema.sql` aberto e linhas selecionadas
  no editor: `dim_local` como a tabela onde moram `origem_id`, `destino_id`
  **e** `local_id`; `endereco, bairro e cidade (3)` para a coluna apontada,
  com `(local_id)` no fim da linha 43; "universidades" para o papel da Rua
  A na volta (respondeu quem era a origem); colou o bloco Pinheiros ×
  Butantã quando pedido o de ida/volta; `dim_origem` para a Universidade da
  ida, com `destino = Universidade` escrito. **Colando ou lendo a linha
  pedida, acertou nas três vezes**: linha 43 → `fato_transportes`; linha
  43 colada → `local_id`; a palavra antes de `= Universidade` → `destino`.
  Sessão 19, quatro vezes, todas numa data escrita na própria pergunta:
  `01` e `2026` para "12 de março de 2027"; ano `2026` de novo, com
  `2027` na linha de cima; `20270211` para 11/01. **Mandado copiar o
  número da linha, acertou**; o `20270211` ele consertou sozinho com
  "que dia e que mês é esse?".
  Sessão 20, três vezes: `15/04/2027` para a data que vem primeiro no
  calendário, com 20/03 e 15/04 escritas uma embaixo da outra; "`Noturno
  | ?` -> false" no lugar da pergunta feita (quantas linhas casam no
  `JOIN`); "o período de março" para a coluna `periodo`, que é turno.
  **Mandado ler o mês ou copiar a coluna, acertou nas três.**
  Sessão 21, duas vezes: "primeira" para quantas linhas casam com
  `usuario_id = 101`, com os dois `101` na tela; abriu o
  `.python-version` (o do projeto) para responder que versão o **Mac**
  roda. **Mandado copiar a coluna ou rodar `python3 --version`, acertou
  nas duas.**
  Sessão 22, três vezes: pedida a viagem com números, deu a regra;
  pedido para comparar as linhas 23 e 25 do contrato, respondeu com a
  ideia de criar um `viagem_possivel()`; "é a classe `Viagem`" com
  `self = Viagem(hora_saida_id=7, ...)` colado por ele mesmo. **Copiando,
  acertou nas três vezes em que colou**: a linha do `src/` deu o
  arquivo (na segunda tentativa: primeiro colou a do `NameError`); as
  linhas 23 e 25 lado a lado deram o `self`; a linha `self = ` com a
  ponte do `INSERT` deu "insert".
  Sessão 23, quatro vezes: "atributo" para "o `self` é ___", logo
  depois de responder "uma" viagem; mandado copiar a frase, "então eu
  não sei o que o self é" (não colou); mandado copiar a frase do "para
  ali", colou a pista da mensagem anterior; "n lembro" para a linha 25
  ter rodado, com a resposta duas linhas acima. **Com a frase reposta
  por mim, "n" na hora.**
- **Inventar valor para não deixar coluna vazia** — duas vezes na sessão 4
  (número da linha do metrô, "híbrido ou não" no ônibus). O caso "não existe
  valor" é o caso que importa: é ele que gera NULL em FK.
  Sessão 13, **o inverso: inventou ausência para um valor que existe.**
  Perguntado que valor 15/07 (quarta de férias) recebe na coluna "é
  feriado?", respondeu `NULL` e depois `-1`. O valor é **não**, e é
  conhecido. Perguntado "15/07 é feriado?" em sim/não, respondeu "n" na hora.
  `NULL` e `-1` são para quando a informação falta.
  Sessão 15: com metrô e Uber numa linha só, preencheu `modal_id` com
  `transporte`, que não é modal (é o nome do fato). Valor genérico para não
  escolher entre dois. A linha `42 | ?` com um lugar só resolveu: "duas".
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
  Sessão 12, duas vezes: respondeu "não" (a rua não volta) e "sim" (o
  endereço chega no bairro) e, na pergunta seguinte, escolheu bairro. E
  defendeu `UNIQUE` em `bairro` com a frase "mais de um endereço pode
  existir em um bairro", que é o argumento contra.
  Sessão 13: respondeu "15/07 não é feriado" e, duas mensagens depois,
  propôs como pergunta da coluna "esses dias são feriado?". Disse "eu já
  rodei e passou" para um `INSERT` que nunca chegou ao banco (0 linhas): não
  conferiu, e a tela não tinha dado nem erro nem `INSERT 0 1`.
  Sessão 15, versão arquivo: respondeu `duracao` "inteiro", em "min", e no
  disco ficou `duracao NUMERIC (10,2)`, igual às duas linhas de baixo. Não
  avisou nem defendeu a troca. Pode ser decisão (minuto fracionado), pode
  ser cópia da linha vizinha: perguntar.
  Sessão 17: "decisão minha", defendida com "horas e minutos"; com 1h30 →
  `90`, viu que não precisava de casa decimal. Linha virou `NUMERIC (10)`.
  Sessão 18, versão arquivo de novo: derivou a chave natural ("deveria
  guardar numa coluna id original do aluno") e escreveu a `dim_usuario`
  sem ela; perguntado onde estava, apontou a linha 36 (`usuario_id`, que
  ele tinha acabado de dizer que tem dois valores para o mesmo aluno). E
  respondeu "pra antiga e nova" para o `usuario_id` de uma linha do fato,
  minutos depois de dizer, sobre o `modal_id`, "a coluna só guarda um".
  Com a frase dele citada de volta: "aponta para a 101".
  Sessão 21: escreveu a regra com `hora_saida < hora_chegada` e
  respondeu "deixa" para a viagem 7h10 → 7h40 (7 < 7). Copiando a linha
  da regra com os números: "falso" → `<=`.
  Sessão 22, três vezes: disse que o teste da viagem válida não usa
  `pytest.raises` e, duas mensagens depois, "abriria um novo `with`";
  abriu a sessão com "a viagem do mesmo dia derruba o arquivo" e previu
  "passa" para um teste de mesmo dia; disse que 10/12 → 11/12 dava
  `NameError` e, três passos depois, que quebravam "todas as viagens de
  mesma data".
  Sessão 23, duas vezes: disse que a linha 23 dá falso para data igual
  e, na resposta seguinte, que a viagem de data igual "entraria dentro
  do erro antes do elif"; com `20261210 > 20261210` → "falso". E
  "aceitou" para a viagem 12/01 → 11/01, três mensagens depois de dar
  "verdadeiro" para a linha 23 dela. A segunda já no fim, cansado.
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
  Sessão 15: perguntado **em que unidade** ficam `duracao`, `distancia` e
  `preco`, respondeu o tipo ("inteiro, inteiro, flutuante"). Mesmo desvio
  da sessão 13 (tipo quando a pergunta era valor). Com a pergunta repetida
  e a linha do 42 na tela, "min, km, reais" de primeira. E 23h50 + 20 min =
  "0h20", de cabeça; a conclusão (chegou no dia 16) estava certa.
  Sessão 16: "duas" para "quantas colunas do fato apontam para quantas da
  `dim_local`", e com o formato pedido de novo, "apontam pra `dim_local`"
  (tabela no lugar de coluna). E **rótulo errado no lugar de rótulo
  nenhum**: "duas origens" para o que eram dois bairros, com "pinheiros e
  butantã" escrito por ele seis mensagens antes.
- **Vírgula sobrando antes do fecha-parêntese** — quatro vezes na sessão 6,
  em três tabelas. Mecânico, não conceitual, mas para o arquivo inteiro. Ele
  ainda não rodou o SQL em banco nenhum — é erro que sumiria sozinho no
  primeiro `psql`.
  Sessão 7, mais três da mesma família: `==` em vez de `=`, `;` faltando nos
  três `INSERT`, nome de coluna inventado. **Sétima sessão sem rodar nada.**
  Sessão 12: duas vírgulas faltando na `dim_local`, e 2 valores para 4
  colunas no `INSERT` do `-1`. Previu "passa" nas duas; o banco pegou as
  duas e ele consertou sozinho. Rodando, esse item deixa de ser problema.
  Sessão 13: `;` faltando duas vezes (`DROP`, `INSERT`), `INSERT INT`,
  `INTEGER TEXT`. Leu e consertou os quatro. **Novo e mais caro:** no `psql`
  interativo, comando sem `;` não dá erro; o prompt vira `transportes-#` e
  fica esperando. Ele tomou o silêncio por sucesso. Regra entregue: **`-#`
  = nada foi para o banco.**
  Sessão 14: `CHECK (... OR -1)`, consertado sozinho para `OR ordem_dia =
  -1` antes de rodar; `INSERT` com 7 valores para 6 colunas, que o banco
  pegou e ele leu e consertou sozinho. **A `dim_usuario` passou de
  primeira, como ele previu.**
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
  Sessão 12: 1 vez. O `INSERT` do `-1` certo no editor e no banco, e o disco
  com a versão de 2 valores. Salvou ao ser avisado. Nas outras três, salvou.
  Sessão 13: **zero.** Conferido no disco seis vezes, salvo nas seis.
  Primeira sessão limpa. Continuar conferindo.
  Sessão 14: zero de novo, em quatro conferências.
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
  Sessão 11: recusou as 3 frases ("to mt cansado").
  Sessão 12: 0 de 3 na primeira tentativa (sintaxe do `UNIQUE` composto,
  "4 colunas = 4 valores", "só o conjunto é único"). Com uma pergunta ("por
  que nenhuma das três pode ser `UNIQUE` sozinha?") a terceira saiu com
  mecanismo e exemplo próprio: Rua X 13 em duas cidades é outro lugar, e o
  `UNIQUE` sozinho barraria. Endereço × bairro e válido × proibido não
  apareceram.
  Sessão 13: 1 de 3 com o "para quê" (`nome_dia`: a reitoria vê o sábado).
  As outras duas, fato ("'10' fica entre '1' e '3'") e repetição da 12
  (`UNIQUE` composto). Com uma pergunta, a consequência saiu certa (março
  pedido, outros meses entram), mas o mecanismo saiu errado: "porque '0' é
  menor que '1'". Ver "Ordem de texto × ordem de número". Chave
  `AAAAMMDD`, `feriado` × `tem_aula` e o `-#` do `psql` não apareceram.
  Sessão 14: 1 de 3 com o porquê (nome fora: a reitoria quer quantidade,
  não indivíduo). A segunda com meio porquê ("já está na `dim_local`"; o
  forte era o aluno 42, Pinheiros × Bela Vista). A terceira, fato
  ("considerar o integral"); com uma pergunta, o porquê saiu errado
  (matutino = `origem_id`, vespertino = `destino_id`), quando era horário:
  o integral chega com o matutino e sai depois do vespertino. **As três
  vieram da última meia hora**: `ordem_dia`, texto × número e a defesa do
  gerador não apareceram.
  Sessão 15: 1 de 3 com o porquê (`float` guarda aproximação, o filtro de
  igualdade perde a linha; disse "arredondamento exato", e `NUMERIC` não
  arredonda). A segunda trocou `duracao` por `distancia` e perdeu o porquê
  que ele tinha escrito melhor uma hora antes; com uma pergunta, "joga fora
  os minutos" voltou. A primeira saiu **invertida**: "uma coluna do fato
  associada a duas colunas de outras tabelas", quando é uma coluna da
  dimensão (`local_id`) com duas colunas do fato apontando para ela.
  Sessão 16: abriu o fechamento com "aprendi que eu sou burro". Depois, 1
  frase de 3: "nas colunas de saída e destino, havia uma ambiguidade se n
  fossem isoladas. algo assim". Recusou as outras duas ("muito difícil de
  entender"). A frase é ambígua (ver "Role-playing: direção e porquê"), e
  o mecanismo da sessão (uma tabela por papel duplica o lugar) não
  apareceu.
  Sessões 17 e 18: recusou as 3 frases. Sessão 19: 1 frase, **com
  mecanismo**, a melhor em semanas: com só `NOT NULL` e `REFERENCES`, o
  banco aceita viagem impossível, porque o erro só aparece comparando
  duas colunas da mesma linha. **O fim saiu trocado**: "aceita os casos
  onde a data de saída acontece antes da data de chegada", que é a
  viagem normal. Perguntado, disse certo ("se a chegada acontecer
  primeiro, seria impossível") e defendeu que a frase estava certa. O
  entendimento está certo; a frase escrita nomeia o caso errado. Mesma
  família da frase invertida da sessão 15.
  Sessão 20: recusou ("to mt morto"). Três recusas em quatro sessões
  (17, 18, 20).
  **Sessão 21: 2 de 3 com mecanismo, a melhor até aqui.** (1)
  `AAAAMMDD` "pra evitar o caso 20/03 > 15/05", sem o zero; (2) o brew
  muda o Python do Mac, o uv usa o do projeto pelo `.python-version`, e
  o projeto não é afetado. (3) `self` "permite a função trazer os
  objetos criados pra aquela classe": plural, quando `self` é **o**
  objeto que está sendo conferido agora. Nenhuma em sintaxe pura.
  Sessão 22: recusou ("vamos pular essa revisão e você recapitula e
  reforça tudo amanhã comigo mais descansado"). Quatro recusas em seis
  sessões (17, 18, 20, 22).
  Sessão 23: 1 de 3, com mecanismo, e meio emprestada: "gerador, pois
  toda linha do fato passa pela `Viagem` antes de entrar no banco"
  repete a minha frase da mensagem anterior. O fim dele saiu trocado
  ("evitando erros de linhas que não foram inseridas"); com uma
  pergunta, "linhas que não atendem as restrições da viagem". A frase
  do teste verde não fechou (ver "Caso que ilustra"); a do `self` não
  foi pedida.
- **`latest` × versão fixa** — revisão da sessão 9, sem andaime: sabia o fato
  ("pega a versão mais atual"), não sabia a consequência. Respondeu repetindo
  a diferença de versão e tratando o problema como "o meu está
  desatualizado". "Não sei" para "por que você não consegue descobrir o erro
  do colega". Com o problema diminuído (o erro acontece na sua máquina? o que é
  diferente? o arquivo diz que é o 19?) chegou em "eu não sei qual versão ele
  está" e no contrafactual com `postgres:18`. Mecanismo alcançado com
  andaime, então ainda está frágil. Revisar sem andaime.
  Sessão 11, sem andaime: as duas primeiras certas de primeira (o arquivo
  igual sobe Postgres diferente; "a da versão que ele está utilizando").
  A terceira parou no meio ("agora eu sei em que versão ele está"), "n
  lembro" para a consequência, e com uma pergunta de sim/não chegou em "a
  versão não pode ser a culpada". Melhorou muito. Falta dizer sozinho o
  último passo: fixar a versão tira um suspeito da investigação.
  Sessão 21, versão Python: "o 3.14.5 do Homebrew é o `18` ou o
  `latest`?" → "latest" de primeira. Escolheu 3.14 "porque é a versão em
  que meu Mac roda" (o argumento do `latest` de novo); com "e quando o
  brew trouxer o 3.15?" → "n manda n"; com os fatos de suporte, 3.14 pelo
  período de correção. **A evidência veio sozinha:** o `brew install uv`
  desinstalou o `python@3.14`; o `python3` do Mac virou o 3.9.6 da Apple,
  e o pytest rodou no 3.14.8 do uv. Mecanismo primeiro errado ("o brew
  está barrado de atualizar por conta do `.python-version`"); com o
  caminho do log (`~/.local/share/uv/python/...`) → "uv". Dois Pythons,
  um do Mac e um do projeto. **História pronta para o `HISTORIAS.md`.**
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
  Sessão 13: "20032026 é menor" que 15042026, sem comparar. Escrevendo um
  embaixo do outro e olhando o primeiro dígito, acertou na hora (e xingou o
  trabalho de escrever, mas foi o escrever que achou o erro).
- **Chutar premissa em vez de derivar** — sessão 4: inventou "1 a 2
  abastecimentos por semana" e reaproveitou o 7 de "7 km/dia" como capacidade de
  tanque (7 L). Dado sintético exige premissa com fonte, não número de cabeça.
  Sessão 11, versão calendário: "estender o projeto até dezembro", depois
  "31 de dezembro", sem conta. A data ficava 4 dias **antes** do fim
  original (4/jan/2027): uma extensão que encurtava. Mandado escrever a
  conta, mandou só a data; no passo seguinte pediu para eu redefinir.
  Sessão 13: "março tem 30 dias" (tem 31), usado como base da query de
  março. Daí saiu a melhor pergunta da revisão: com 30, as viagens do dia 31
  somem sem erro.
- **"Métrica" como palavra** — sabe o conceito (aponta R$ 138 como métrica na
  hora), mas erra a frase "métrica mora no fato" toda vez que a pergunta é
  abstrata. Quarta inversão na sessão 3. Só acerta quando ancorado num exemplo
  concreto. Perguntar sempre com exemplo junto, nunca no abstrato.
  Sessão 15: perguntado que métricas a linha do 42 guarda, com as 9 chaves
  recém-listadas na tela: "todas n?". O exemplo concreto resolveu de novo:
  `origem_id` `7 + 15 = 22` → "porra nenhuma". Depois, `duracao` (com a
  tabela reposta), `preco` e `distancia` (com R$ 30 e 8 km na frase).
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
  Sessão 12, melhorou: leu sozinho "Cannot connect to the Docker daemon"
  ("docker n está ativo"); consertou sozinho o `syntax error at or near
  "bairro"` e disse que a vírgula faltava na linha de cima; leu "more
  target columns than expressions" com só as duas palavras traduzidas.
  Regra entregue: **o erro aponta onde o banco percebeu, não onde o erro
  está; se a palavra apontada parece certa, olhar a linha de cima.**
  Sessão 22, primeiro traceback de Python: com o `NameError` apontando
  `src/assistente/contrato.py:25`, **mexeu no teste** (pôs `with
  pytest():` na linha 23, contra a regra do pytest que tinha acabado de
  receber). O erro virou outro (`TypeError: 'module' object is not
  callable`), que ele não viu: rodei eu, conferindo o disco. Mandado
  copiar a linha que diz onde, copiou a que diz o quê (`NameError: name
  ... is not defined`); com "a que diz onde começa com `src/`", acertou.
  Regra entregue: **no traceback do pytest, a linha com `src/` diz o
  arquivo e a linha; a com `E` diz o que deu errado.** Mesma família de
  trocar o dado para caber na regra (sessão 13): mexeu no lado que ele
  controlava em vez de ler qual lado quebrou.
- **`CHECK`: lista do válido × lista do proibido** — revisão da sessão 12.
  Pergunta 1 certa (o banco recusa; disse "tabela" querendo dizer linha).
  Pergunta 2 com andaime: em vez do porquê, escreveu a versão proibida como
  `check_id < 0 AND check_id > 23`, um `AND` que nenhum número satisfaz.
  Testando com 99, viu que essa lista não proíbe nada, que o 99 entra e que o
  banco não avisa ("erro silencioso", palavra dele). Fechou com lacuna:
  **a lista do proibido erra calada, a do válido erra fazendo barulho.**
  Argumento melhor que o da sessão 7 (lista infinita). Pergunta 3 certa sem
  andaime: na versão B o `-1` aparece como caso à parte para quem lê depois;
  na A fica "inibido" no intervalo (schema é documentação).
- **Grão da dimensão: guardar o mais fino** — sessão 12, `dim_local`.
  Escolheu bairro, "não sei defender", "n sei" para a rua do ponto de
  embarque. Destravou com as duas versões desenhadas: na de bairro, "Rua A"
  não aparece em linha nenhuma; na de endereço, o `GROUP BY bairro` ainda
  funciona. Escolheu bairro de novo, com "serve de filtro", argumento que
  vale para as duas versões. Chegou em endereço com "eu sei o local exato e
  o bairro". Regra entregue: **guarda o grão mais fino que você tem; o fino
  sobe com `GROUP BY`, o grosso nunca desce.** Revisar sem andaime em outra
  dimensão (`dim_data`).
  Revisão da sessão 13, `dim_data`: **escolheu dia de primeira, sem
  andaime.** O motivo veio furado ("uma viagem é feita em um determinado
  dia", que vale também para mês, o mesmo defeito do "serve de filtro").
  Pergunta 2 certa. Pergunta 3 (março com tabela por dia): direção certa,
  fato errado (30 dias), e chegou em "a linha precisa ter o mês" com um
  passo. A escolha virou dele; a defesa ainda não.
- **Ordem de texto × ordem de número** — sessão 13. Previu que `'10'` não
  entra em `BETWEEN '1' AND '3'` (achava que `BETWEEN` em texto testa
  igualdade com os valores do intervalo). Rodou: `t`. Leu `t`/`f` como "dois
  erros". Chegou em "prioriza o primeiro caractere" e em `'1' < '10' < '3'`,
  mas nas 3 frases o porquê virou "porque '0' é menor que '1'". **Parte disso
  é culpa minha** (ver falha do professor da sessão 13). Nunca respondeu o
  contraexemplo `'9'` × `'10'`. Revisar com previsão e execução:
  `SELECT '9' < '10';`.
  Revisão da sessão 14: `'9' < '10'` → `f` de primeira. O porquê veio com o
  zero de novo ("'0' < '1' < '9'"), mas com a conclusão certa
  (`'1' < '10' < '9'`). O teste sem zero (`'9' < '19'` → `f`) tirou o zero:
  "o primeiro algarismo foi o mais importante". Recusou rodar ("n vou
  rodar, mas as duas são falsas"); estavam certas. **Aplicou sozinho ao
  `nome_dia`**: escreveu os 7 nomes e achou `terça` por último. Daí saiu a
  `ordem_dia`. Melhorou muito; o zero ainda aparece antes de sumir.
  Sessão 20: o zero voltou como porquê da chave `AAAAMMDD` ("evitando o
  caso de número com 0 como primeiro algarismo"). Com `20032027` ×
  `15042027`, sem zero nenhum: o menor de primeira, a data mais cedo
  errada (ver "Não olhar a tela"), e o mecanismo saiu dele ("mesmo que
  20 > 15"). **O zero é o porquê que volta quando o outro não vem.**
  Sessão 21, sem pergunta nenhuma, duas vezes: na decisão do contrato
  ("20/03 > 15/05, o que não é verdade") e nas 3 frases. **Sem o zero
  nas duas.**
- **Copiar a forma da solução e perder o significado** — sessão 7 (chave `2`
  nos `INSERT` do `-1`). Sessão 13, duas vezes: `data_id = 15` (a regra da
  `dim_hora`, "a chave é o próprio valor", sem testar o segundo dia 15); e
  `OR tem_aula = -1`, copiado da linha 12, numa coluna de texto cuja linha
  `-1` diz `'Não se aplica'`. E, para fazer a regra errada passar, **trocou o
  dado** (`tem_aula = -1` no `INSERT`) em vez da regra. O relatório da
  reitoria com uma linha `-1` resolveu: "nada".
  **Sessão 19, a chave `AAAAMMDD` não voltou sem andaime.** Mesmo
  caminho da 13, inteiro: `13h` e `12 de janeiro` numa coluna `INTEGER`;
  `data_saida_id = 12` (a regra da `dim_hora` de novo); `12032027`
  (`DDMMAAAA`, o formato que ele mesmo descartou na 13). Com os dois
  números um embaixo do outro (`12032027` × `01042027`), viu que o menor
  é a data mais tarde, e "ano, mês, dia" saiu de primeira. Seis passos
  para uma decisão dele. Revisar: "que número vai na `data_id` de
  05/11/2027, e por que nessa ordem?".
  **Sessão 20: `20271105` de primeira, sem andaime.** A decisão virou
  dele; o porquê ainda não (o zero de novo, ver "Ordem de texto × ordem
  de número").
- **Lista do válido sem o membro `-1`** — sessão 14, duas vezes: válidos de
  `ordem_dia` = "1 a 7" e de `periodo` = "manha, tarde, noite", as duas sem
  a linha `-1` que ele tinha acabado de definir. Mesmo conflito do `CHECK`
  da `dim_hora` na sessão 7. Nas duas, uma pergunta ("reescreva levando em
  conta a linha `-1`") consertou.
- **Restrição no banco × garantia no processo** — sessão 14. Viu sozinho,
  restrição por restrição, que `segunda | ordem_dia = 5` entra no banco.
  Depois: "o que impede de fato? isso ainda n entendi". Chegou com muitos
  passos: a `dim_data` é escrita só pelo gerador, que calcula `nome_dia` e
  `ordem_dia` da mesma data; bug no gerador erra as 52 segundas, e uma
  semana conferida mostra; uma linha errada sozinha só nasce de `INSERT` à
  mão, e essa exige conferir as 365. A resposta ao entrevistador saiu pela
  metade ("o gerador designa o número correto"), sem o risco que sobra.
  Revisar: "o que impede uma segunda com `ordem_dia = 5`?".
  Revisão da sessão 15, sem andaime, com o objetivo dito antes: "aceita" e
  "o `CHECK` só olha a `ordem_dia`" de primeira; "um gerador" de primeira,
  com um furo: o gerador "**recebe** a `nome_dia`" (se recebe, alguém
  digitou). Com uma pergunta: "interpreta dia, mês e ano". **O risco que
  sobra ("`INSERT` à mão") saiu sozinho**, o que não aconteceu na 14. Na
  resposta ao entrevistador, a primeira frase cobria só a `nome_dia`;
  reescrita, cobriu as duas, com "correlacionado" no lugar do verbo.
  Melhorou muito; falta a frase curta ("calcula as duas da mesma data").
  Sessão 20, versão contrato × `CHECK` (carga de 5M com a viagem
  impossível na posição 3.200.000): "checa uma a uma"; "são ignoradas"
  para as 3.199.999, lido como rollback, com a evidência da sessão 18.
  O que o contrato muda saiu vago ("só checa uma possibilidade") até a
  pergunta concreta "em que momento você fica sabendo?" → "no momento
  que eu ponho o `>=`". **O risco que sobra não voltou:** "excelente
  pergunta kkk", "não lembro"; com o `INSERT` à mão no `psql` posto na
  tela, "isso tá sendo visto pelo sql". Saiu sozinho na 15 e com andaime
  na 20. A frase de entrevista ("os dois: o contrato na entrada, o
  `CHECK` como última linha") fui eu que montei.
- **Role-playing: direção e porquê** — frase invertida no fim da sessão 15;
  revisada na 16, com o objetivo dito antes ("o que é uma role-playing
  dimension?").
  - **Direção:** pôs as três colunas na `dim_local`, sem separar onde a
    coluna mora (`origem_id` e `destino_id` moram no fato) e para onde ela
    aponta. Colando a linha 43, chegou em "duas colunas do fato apontam pra
    1 coluna da `dim_local`".
  - **Porquê:** com o aluno 42 (ida: Rua A, 120 → Universidade; volta: o
    contrário), viu que com `dim_origem` + `dim_destino` a Rua A entra nas
    duas, e que corrigir o bairro em uma só dá "duas" respostas
    (Pinheiros, Butantã). **Ideia errada nova:** "uma representa a ida, a
    outra a volta" (tabela por viagem, não por papel). A ida sozinha já
    usa as duas tabelas; copiando a palavra antes de `= Universidade`,
    viu isso.
  - **Furo da primeira frase dele:** "sem repetições desnecessárias,
    preservando a unicidade". Reescrita com o caso, descreveu o sintoma
    (Rua A com dois bairros), que também acontece com uma `dim_local` só:
    o `UNIQUE (endereco, bairro, cidade)` não barra `Rua A, 120 |
    Butantã` × `Rua A, 120 | Pinheiros`. O que é exclusivo do desenho com
    duas tabelas é a repetição **sem ninguém errar nada**.
  - **A frase final fui eu que montei**, com as peças dele. Não fixou: no
    fechamento saiu "ambiguidade se n fossem isoladas". Lida como "colunas
    separadas no fato", é o argumento da sessão 15 (`42 | ?` com dois
    lugares); lida como "tabelas separadas", é o contrário do de hoje.
  - Entra no teste frio com a pergunta de entrevista, sem andaime.
  - Sessão 17, 1ª tentativa: "usada somente uma vez numa tabela fato"
    (contradiz o próprio exemplo) e "não precisa" no lugar do risco.
  - **Sessão 18, caso novo (`dim_data_saida` × `dim_data_chegada`), sem
    andaime: passou.** Levou o argumento sozinho para outra dimensão:
    "uma modificação feita em alguma tabela não foi propagada pra
    segunda". Vago: "inconsistência nos resultados", sem dizer qual. Ter
    o exemplo pronto (21/04 com `tem_aula` diferente nas duas).
- **Onde estou: `%` × `transportes=#`** — sessão 14: digitou `DROP TABLE`
  duas vezes no terminal do Mac (`zsh: command not found: DROP`). Regra
  entregue: **SQL só depois do `transportes=#`; o `%` é o Mac.** Mesma
  família de cliente × servidor (sessão 7) e do `cd` (sessão 10).
- **Grão com valor específico** — escreve o grão colando um valor concreto
  dentro dele. Errou duas vezes na sessão 2, corrigiu nas duas.
- **Teste de unicidade do grão** — chegou na conclusão certa pelo raciocínio
  errado ("duplicata é irreal"). Duplicata real é o que prova o grão errado.
- **Caso que ilustra × caso que prova** — sessão 18, teste frio do grão.
  Pedido "um caso que prova que o grão está certo", deu uma viagem de um
  modal só (João, SJC → SP de Uber), que cabe em qualquer grão. Com "cabe
  em qualquer grão, me dá um que daria errado sem o 'único modal'",
  repetiu a **mesma viagem** trocando "Uber Priority" por "carro de
  aplicativo". Com "quantos modais?" e "como a viagem teria que ser?",
  montou carro de app + ônibus, e o argumento saiu dele ("a linha
  representa dois modais e a coluna só guarda um"). Mesma raiz do
  "teste de unicidade" acima: o caso que importa é o que quebra a
  alternativa, não o que confirma a regra.
  Sessão 21, versão teste: o único teste é a viagem impossível, e ele
  só passa pelo primeiro `if`. O `elif` tem `data_chegada_id` sem
  `self.`, e **toda viagem válida** (12/01 7h → 12/01 8h) dá `NameError`,
  não `ValidationError`. Conferido por mim, dito a ele só como isca.
  Teste verde prova o caso testado, não o arquivo. Falta o teste da
  viagem que **tem que passar**.
  Sessão 22: escreveu esse teste (10/12/2026 7h → 8h), previu "passa",
  deu `NameError`, consertou o `self.`, previu "dois", `2 passed`. **O
  porquê não fechou.** Abriu a sessão com "era a viagem do mesmo dia".
  Com a viagem 10/12 23h → 11/12 1h, "daria `NameError`" de primeira, e
  "linha 23 dá falso → vai para a 25" com uma pergunta cada. Perguntado
  quais viagens quebravam: "todas de mesma data"; depois "saída menor
  que a chegada" (faltou o igual). "n sei" para o que o `1 passed` da 21
  provava. Encerrou em "a viagem 12/01 → 11/01 parava na linha 23 ou
  chegava à 25?". Ver "Ler o código pela intenção".
  Sessão 23: **o que o `1 passed` provava não fechou de novo.** "Não
  lembro"; `20270112 > 20270111` → "verdadeiro"; "n lembro" para a 25
  ter rodado; com a frase reposta, "n". Lacuna "o `1 passed` provava só
  que ___" → "que havia um problema na lógica" (verde lido como sinal
  de problema). Sim/não "foi aceita ou recusada?" → "aceitou".
  **Ideia errada provável:** com `pytest.raises`, verde quer dizer que o
  erro esperado aconteceu, ou seja, que a viagem foi recusada; ele
  parece ler verde como "a viagem passou". O fato da 22 ("verde = a
  função chega ao fim sem erro") não cobre o `with pytest.raises`.
  Revisar com essa pergunta só: "teste com `pytest.raises` ficou verde:
  a viagem foi aceita ou recusada?".
- **SCD tipo 2** — sessão 18, primeira vez. "Já aprendi": tipo 1 certo
  (sobrescreve, o histórico muda junto); tipo 2 parou na ação ("fecha a
  linha antiga e cria uma nova"), sem o efeito no histórico, e com
  `cidade` numa `dim_usuario` que não tem cidade. Derivou com andaime
  curto: chave por versão, fato antigo aponta para a versão antiga,
  chave natural, `atual`. Revisar frio: "o que acontece no seu modelo
  quando o aluno muda de turno?".
  Sessão 19: revisão encolhida para essa pergunta só, e recusada ("n
  quero, segue"). Pulada duas sessões seguidas (18 e 19). O gerador
  precisa disso: viagem de março tem que apontar para a versão de março.
  **Sessão 20, frio, enfim. Passou com andaime:**
  - "criou uma nova coluna id": coluna no lugar de linha. Com a tabela
    de uma linha desenhada, "uma" e depois "duas".
  - Na linha nova, `usuario_id = 101` de novo: **a chave por versão não
    voltou.**
  - **Ideia errada nova sobre `JOIN`:** com dois `101`, "pode inibir
    alguma dessas linhas, provavelmente a primeira". Fato entregue: o
    `JOIN` devolve uma linha por casamento e não escolhe. Com a coluna
    copiada: "nossa, tem noturno e matutino" (a viagem de março contada
    duas vezes, uma com o turno errado, sem erro). Daí `102` de primeira.
  - Frase de entrevista: "recebe um segundo identificador para sinalizar
    a mudança", sem "linha nova" e sem porquê. Perguntado por que não um
    `UPDATE` no 101, o porquê saiu dele: "nunca encontraríamos que o
    aluno pertenceu anteriormente a outro período".
  - Revisar com outra pergunta: "por que a linha nova não pode
    reaproveitar o `usuario_id`?".
  - Sessão 21, essa pergunta, como pista do "o que quebrou na 20":
    respondeu por que existe linha nova, não por que o número muda. **O
    `JOIN` que esconde linha voltou** ("se fizermos um JOIN haveria a
    informação omitida") e "primeira" para quantas casam. Copiando a
    coluna: "as duas", "duas linhas de mesmo usuário contando
    informações diferentes". Hipótese: é o NULL em FK generalizado
    errado. Lá a linha some (0 casamentos); aqui duplica (2). Regra
    única: o `JOIN` devolve uma linha por casamento.
- **Análise dimensional** — inverteu divisão e multiplicação no fim da conta
  (multiplicou 78 dias/abastecimento por 365 em vez de dividir), resultado
  28.579 abastecimentos/ano. Os dois primeiros passos estavam certos. É terreno
  de mecatrônico; não deveria escapar.
- **Fato snapshot periódico e métrica semi-aditiva** — visto na sessão 2. Não
  testado ainda.
- **Python: classe, objeto, `self`, e os rótulos** — sessão 21, primeira
  vez. "Sei os conceitos de programação em Python, mas não lembro como
  usar os objetos." Ponte que funcionou: SQL (`class` = `CREATE TABLE`,
  `Viagem(...)` = `INSERT`, validador = `CHECK`, `ValidationError` = o
  erro do banco) e chamada de função com argumento nomeado. Perguntas
  boas dele: o que o `@model_validator` faz; por que `self` ("o self
  puxa os objetos pra serem permitidos usar dentro da função?", quase
  certo). Rótulos trocados: "pasta `assistente` que armazena uma
  **classe** `contrato` e importa a **função** `viagem`" (a pasta
  existe; `contrato` é arquivo; `Viagem` é classe); `.env` × `.venv`
  ("não subir a `.venv` pra não subir as chaves de API"); `AND` do SQL
  no `if` (consertou sozinho, rodando). Revisar frio: "no seu
  validador, o que é `self`, e o que `self.data_saida_id` devolve quando
  o Pydantic confere a viagem do 42?".
  Sessão 22, essa revisão, frio: "`self` é o indicador que permite que
  as variáveis construídas na classe sejam usadas nas funções" (acesso,
  e "da classe"). Com `self = Viagem(hora_saida_id=7, ...)` do
  traceback colado por ele: "é a classe `Viagem`". Pela ponte
  (`CREATE TABLE` × `INSERT`): "insert". Pediu a definição ("por
  definição de programação, o que é o self mesmo?"); entregue como
  fato: o objeto sobre o qual o método foi chamado; no validador, a
  viagem que o Pydantic acabou de montar. Depois, "`data_chegada_id`
  sem `self.` é de qual viagem?" → "nenhuma!". Rótulo trocado de novo:
  "a classe `Viagem` tem como **objetos** cada um desses 4 campos". E
  "abrir um `Viagem2` ou comentar o `Viagem` antigo?" para escrever o
  segundo teste (classe × teste); a ponte "dois `INSERT` na mesma
  tabela" resolveu. Fatos entregues: cada teste é um `def test_...`;
  quem chama a função é o pytest; verde = a função chega ao fim sem
  erro. Revisar frio: "o que é `self`?" e "na sua `Viagem`, o que é
  classe, o que é objeto e o que é campo?".
  Sessão 23, essa revisão, frio: "um objeto que permite usar os
  atributos de uma classe" (objeto, enfim; acesso e "da classe" de
  novo). Para o `self` do `Viagem(hora_saida_id=7, ...)`: "os
  componentes" (os campos); "quantas viagens cria?" → "uma"; na lacuna
  "o `self` é ___", "atributo". Na múltipla escolha, "a classe"; com a
  tabela dos dois testes (mesma classe, `13` × `7`), não respondeu o
  número e passou por "self é um campo?" até "self é a viagem? n faz
  sentido!". **Hipótese:** "viagem" e `Viagem` são a mesma palavra
  falada; "self é a viagem" soa como "self é a classe", que eu tinha
  acabado de dizer que não era. A ponte com a linha (`self` → a linha
  que o `CHECK` confere agora) deu "entendi", conferido só de lado
  ("`data_chegada_id` sem `self.` é de qual viagem?" → "nenhuma").
  Revisar frio: "seus dois testes usam a mesma classe: quantos `self`
  existem, e quanto vale `self.hora_saida_id` em cada um?".
- **Ler o código pela intenção, não pela execução** — sessão 22. Leu o
  `elif self.data_saida_id == data_chegada_id and ...` como "a linha das
  viagens do mesmo dia" e concluiu que só elas quebravam. O Python não
  lê intenção: roda a condição para **toda** viagem em que o `if` de
  cima deu falso, e quebra ao ler o nome antes de saber se é o mesmo
  dia. Cada passo saiu certo com uma pergunta (linha 23 dá falso; vai
  para a 25); a conclusão voltou para "mesma data" duas vezes. Revisar
  com o arquivo antigo na tela: "quais viagens chegam na linha 25?".
  Sessão 23, com o arquivo antigo na tela: a linha 23 dá falso para
  "data de saída igual à chegada ou menor", de primeira; escorregou
  ("igual entraria no erro antes do elif") e consertou com os números;
  "nenhuma" para o dono do `data_chegada_id` sem `self.`. **A cadeia
  fechou pela execução**, mas a conclusão ("toda viagem normal
  quebrava") fui eu que disse.

## Resolvido

- **Fato vs dimensão** (sessão 2) — 10/10 no drill fechado, com os três erros
  iniciais corrigidos por dedução, não por dica.
- **Hábito de olhar o dado** (sessão 2) — abriu a fatura, trouxe o inteiro (3) e
  descreveu as três linhas com estabelecimento, valor e data.
- **NULL em FK dentro de JOIN** (sessão 6) — o teste marcado na sessão 5
  ("daqui a duas sessões, sem andaime") foi aplicado uma sessão depois e passou
  frio: NULL não casa com nada, a linha não aparece no INNER JOIN, o `SUM` não
  soma o valor dela e o número chega errado no relatório **sem erro nenhum**.
  Três perguntas, três acertos, zero andaime. Regrediu na sessão 15
  (mecanismo errado: "entra na contagem, de forma silenciosa"; dois
  passos) e na 17 (só a consequência). Passou frio com caso novo na 18
  (`modal_id`). **Voltou ao "Resolvido" na sessão 22**, rotação limpa
  com `origem_id`: `30` de primeira (o total real era 55); "NULL não
  permite identificar um `local_id` equivalente"; `-1` no `origem_id`
  (hesitou com `'Não se aplica'` e separou sozinho). O "sem erro" fui eu
  que disse, antes de perguntar. Próxima rotação: o mesmo `JOIN` com 2
  casamentos (o `101` duplicado do SCD).
- **Separar métrica de dimensão ao escrever** (sessão 3) — colapsou tudo em
  "métricas" na primeira tentativa; separou correto na segunda, aplicando a
  própria régua item por item.

## Nota de método

"Responder a especificação inteira" saiu da lista de pontos frágeis: parte das
respostas parciais era sobrecarga do enunciado, não desatenção. A partir da
sessão 2 o formato é **uma pergunta por vez, com o enunciado repetido junto**.
Rendimento subiu na hora.

**Sessão sem registro deixa a próxima conversa cega** (sessões 17 e 18). A 17
terminou sem PROGRESSO e sem commit; uma conversa nova reaplicou um teste que
ele tinha reprovado um minuto antes, sem saber, e declarou "passou". Na 18 eu
abri pedindo o teste de novo pelo mesmo motivo. Antes de abrir sessão:
conferir se o último log do PROGRESSO bate com `git log`, `git status` e a
data das conversas. Se não bater, ler as conversas antes da primeira pergunta.

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

### Sessão 11 — 2026-09-30
- Fase: 1, semana 4 de 8 (calendário redefinido nesta sessão)
- Feito:
  - **A sessão 10 tinha terminado sem commit.** Ele confirmou ("n"). Não
    lembrava `git add` / `git commit` (entregues como fato). Commit
    `7ce6491`, com a mensagem `sessao10`, que não diz nada.
  - **Revisão `latest` × `18`**: 2 de 3 sem andaime, e a 3ª com um passo.
    Ver pontos frágeis. Melhor resultado de revisão até aqui.
  - **Calendário, finalmente (estava adiado havia 3 sessões).** Números
    mostrados: semana 4 de 4, 0 de 10 itens do CURRICULO marcados, 10
    sessões. Ele escolheu estender, com motivo próprio: tem emprego, não tem
    prazo forçado, quer "aprender de fato". Argumento meu, que ele não usou:
    a fase 1 é a #1 do ranking de vagas. Furo apontado: "aprender de fato"
    não tem fim. Decisão final: **+4 semanas na fase 1, até 2026-11-02;
    projeto com 21 semanas, até ~2027-01-31; reavaliar em 2026-11-02 com o
    ritmo medido.** README atualizado (tabela de fases, GCP na semana 12).
- Quebrou:
  - "31 de dezembro" chutado. Ver "Chutar premissa".
  - **Senha:** "vamos deixar o repositório privado". Privado resolve hoje.
    O furo é que o README diz que o repo existe para ser aberto em
    entrevista. Perguntado se o entrevistador acharia `12345` depois de a
    linha ser apagada, respondeu "ignora, vamos seguir com a sessão".
  - Disse "localhost" querendo dizer "local" (máquina × endereço de rede).
  - Recusou as 3 frases. **Zero artefato: regra da sessão 5 quebrada.**
  - Disse ele mesmo, e está certo: "n teve nenhuma evolução do projeto".
- Falha do professor:
  - **Sessão inteira em meta:** commit, push, senha, calendário. O
    calendário era obrigatório, mas ocupou o lugar do artefato.
  - **Conta do calendário em passos** ("17 semanas são quantos dias?") com
    ele já frustrado. Calendário não é matéria da fase. Devia ter entregue a
    conta direto, como fato de documentação. Ele cortou ("redefine o tempo
    baseado na data que passei"), e a conta direta + 3 opções resolveu em
    uma troca.
  - Abri com enigma ("prevê a mensagem do último commit") → "que?". A
    versão sim/não funcionou na hora.
- Aberto:
  - **Senha `12345` no histórico** (`efbe161`, `7ce6491`). Sem remote; ele
    quer subir para o GitHub, como privado, para contar os commits.
    Resolver antes de o repo ficar visível para qualquer pessoa.
  - **`dim_local`, pergunta já feita e sem resposta:** Rua A, 120, Pinheiros
    e Rua B, 45, Pinheiros: uma linha ou duas?
  - Herdados: `-1` um membro ou dois; `data_fim_id` / `hora_fim_id`
    (oitava sessão em aberto); nomear a universidade; `modelo_database` e
    onde o compose deveria ficar.
- Retomo em:
  1. Revisão curta, no máximo 15 min, 3 perguntas.
  2. **`dim_local`: a pergunta das duas ruas em Pinheiros.** Depois disso,
     a tabela escrita no `schema.sql` e rodada no banco **na mesma sessão**.
     Duas sessões seguidas sem artefato não podem acontecer.
  3. `dim_usuario` e `dim_data`, se der tempo.

### Sessão 12 — 2026-10-02
- Fase: 1, semana 4 de 8 — modelagem dimensional, `dim_local`
- Feito:
  - **O que quebrou na 11**, nas palavras dele: "só definimos datas". Mais a
    reclamação procedente da conta de calendário em passos (falha minha, já
    registrada).
  - **Revisão do `CHECK` da `dim_hora`**: 1 e 3 certas, 2 com andaime. Ver
    pontos frágeis. Saiu um argumento novo e melhor: o proibido erra calado,
    o válido erra fazendo barulho.
  - **`dim_local` decidida, escrita e rodada no banco.** Primeiro artefato
    desde a sessão 10.
    - Grão: **uma linha por endereço**, com `bairro` e `cidade` como colunas.
      Defesa: endereço responde rua e bairro; bairro responde só bairro.
    - `cidade` entrou pelo furo dos dois Centros (São Paulo e Osasco): sem
      ela, o `GROUP BY bairro` soma as duas cidades numa linha só, sem erro.
      Propôs `estado` primeiro; preenchendo a tabelinha, viu que é SP nas duas.
    - **`UNIQUE` composto `(endereco, bairro, cidade)`**, derivado por três
      testes: `endereco` sozinho barra a Rua X de Osasco; `bairro + cidade`
      barra a Rua B de Pinheiros; `endereco + cidade` barra a Rua X de outro
      bairro de SP. Separou sozinho `UNIQUE` em cada coluna (A) de um
      `UNIQUE` sobre as três (B). Sintaxe entregue com exemplo de fora
      (`chamada`, `turma + numero`).
    - Tirou o `UNIQUE` da linha do `endereco` sem eu pedir.
    - Membro `-1` com `'Não se aplica'` nas três colunas de texto.
  - **Prever e rodar, duas vezes, duas previsões erradas** ("passa sim"), as
    duas pegas pelo banco e consertadas por ele.
  - **Arquivo × banco**: perguntado qual `dim_local` estava no banco depois
    de mudar o arquivo, respondeu "velha" na hora. `DROP TABLE` + `CREATE`
    de novo (tabela vazia), conferido com `\d dim_local`.
  - `\dt` agora com 4 tabelas.
- Quebrou:
  - "n sei" 4 vezes (defender bairro, rua do ponto, quantos Centros,
    combinação do `UNIQUE`). Todas destravaram encolhendo o exemplo.
  - Escolheu bairro contra as próprias respostas. Ver pontos frágeis.
  - "fica tudo em osasco" para o estado das duas cidades; lacuna resolveu.
  - 3 frases: zero de três com mecanismo na primeira. Ver pontos frágeis.
- Método:
  - **Tabela de 2 linhas desenhada** destravou todos os "n sei" da sessão.
    Melhor que qualquer pergunta abstrata.
  - **Rodar só o bloco novo no `psql` interativo**, para o erro não se
    misturar com "already exists" das tabelas antigas.
  - Previsão sim/não antes de rodar, mesmo quando ele acerta pouco: as duas
    erradas foram as duas lições de sintaxe que mais pegaram.
- Aberto:
  - **O `schema.sql` não roda duas vezes.** Rodado inteiro hoje, daria
    "already exists" nas 4 tabelas e chave duplicada nos 4 `-1`. Gancho para
    idempotência (CURRICULO, item do Airflow) e para migração (o `DROP` só
    serviu porque a tabela estava vazia).
  - **Endereço de casa de 7.000 alunos.** Dado pessoal. A reitoria precisa
    do número da casa para escolher o ponto de embarque? Isca de revisão
    hostil, não levantada.
  - **"Rua X, 10" × "R. X, 10" × "rua x 10"**: o `UNIQUE` composto não pega
    o mesmo lugar escrito de dois jeitos. Gancho para dado sujo.
  - `-1`: um membro ou dois. Agora com caso forte na `dim_local`: o destino
    do metrô sem registro de saída é **desconhecido**, não "não se aplica".
  - Faltam `dim_data`, `dim_usuario` e `fato_transporte`.
  - Herdados: `data_fim_id` / `hora_fim_id` (nona sessão em aberto); nomear a
    universidade; senha `12345` no histórico antes de qualquer push;
    `modelo_database` e onde o compose deveria ficar.
- Retomo em:
  1. Revisão curta, sem andaime, e já em outra dimensão: **`dim_data`, uma
     linha por dia ou por mês?** Testa se a regra do grão mais fino virou
     dele.
  2. `dim_data` escrita e rodada no banco na mesma sessão.
  3. `dim_usuario`, se der tempo.

### Sessão 13 — 2026-10-03
- Fase: 1, semana 4 de 8 — modelagem dimensional, `dim_data`
- Feito:
  - **O que quebrou na 12**, nas palavras dele: `UNIQUE` separado ×
    composto. O que estava marcado como frágil era o grão (bairro ×
    endereço).
  - **Revisão sem andaime, em outra dimensão: escolheu dia de primeira.**
    Ver "Grão da dimensão". Melhor que a 12.
  - **Colunas pela regra "cada coluna responde uma pergunta da reitoria"**,
    dele na hora de listar:
    - `ano` entrou pelo teste de 15/03/2026 × 15/03/2027 (mesmo `dia` e
      `mes`). Mesmo furo dos dois Centros.
    - `nome_dia` entrou pela decisão do fretado no sábado. Ele queria tirar
      o sábado da coluna `dia`; colou o valor (`15`) e viu que o
      `GROUP BY dia` junta os dias 15.
    - `dia` ficou por outro motivo: a pergunta dele para a coluna era
      "quantas viagens todo dia 15", que ninguém faz; sem ela, 15/03/2026
      não tem resposta. **Coluna que só serve junto com outras.**
    - **`tem_aula`, pelo segundo caso.** Propôs `feriado` para 21/04
      (Tiradentes). 15/07 (quarta de férias) não é feriado e entra na média
      do fretado. Com as duas frases lado a lado: "não tem aula nas duas".
      Nome dele.
  - **Chave `AAAAMMDD` derivada por ele.** `15` (regra da `dim_hora`) →
    colide com 15/04. "Difícil" → encolhido para "escreva sem as barras" →
    `15032026` ("AHHHHHH"). Teste de ordem: `01042026` é menor que
    `15032026`. Culpou o zero; o contraexemplo sem zero (20/03 × 15/04)
    mostrou que o culpado é o dia vir primeiro. "Ano, mês e dia" →
    `20260315`. Ganho: `BETWEEN 20260301 AND 20260331` pega março, porque a
    ordem do número é a do calendário.
  - **`UNIQUE (dia, mes, ano)` sem eu pedir.** A sessão 12 virou dele.
  - **`TEXT` × `INTEGER`, previsto e rodado.** Previu que `'10'` não entra
    em `BETWEEN '1' AND '3'`; `SELECT` deu `t`. Trocou para `INTEGER` antes
    de saber defender; a defesa veio depois. Ver "Ordem de texto × ordem de
    número".
  - **`tem_aula` com `CHECK`.** Viu os 3 grupos de `'sim'`/`'Sim'`/`'s'`.
    Escolheu o `CHECK` sozinho, mas com `BETWEEN 'SIM' AND 'NÃO'` (intervalo
    de dicionário: `pato` passaria). Sintaxe do `IN` entregue com exemplo de
    fora (`tamanho`). Final:
    `CHECK (tem_aula IN ('Sim', 'Não') OR tem_aula = 'Não se aplica')`,
    no mesmo formato da linha 12.
  - **Membro `-1`:** `-1` em `dia`/`mes`/`ano` (propôs "qualquer coisa acima
    de 31, de 12, abaixo de zero"; critério certo, três regras; chegou em
    `-1`); `'Não se aplica'` nas de texto, pelo relatório da reitoria
    (uma linha `-1` no `GROUP BY tem_aula` "não diz nada").
  - Leu sozinho: `no configuration file provided` (resolveu com `cd modelo`;
    na sessão 10 não sabia o que era `cd`), o erro de `INTEGER` no `INSERT`,
    a violação de `CHECK`, e achou o `;` faltando no `DROP`.
  - **Disco = banco**, conferido: `dim_data` com `CHECK` e a linha `-1`.
    `\dt` com **5 tabelas**.
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (4), inventar ausência (`NULL`/`-1`
    para um "não"), responder contra o que derivou, `20032026` de cabeça,
    "março tem 30 dias", copiar a forma (`15`, `OR tem_aula = -1`) e
    **trocar o dado para caber na regra**.
  - Respondeu tipo quando a pergunta era valor ("inteiro" para o `data_id`).
  - `t`/`f` lidos como "dois erros".
  - "Já rodei e passou" para um `INSERT` preso no `-#`. Não conferiu.
  - "Derrubar o banco" para trocar uma tabela. Lembrou certo que as tabelas
    sobrevivem ao `down`/`up` ("se mantém"), o que desmontou a ideia.
  - "n lembro" para `DROP TABLE` (feito na 12).
  - Frustração alta duas vezes ("vai se fuder claude, que trampo";
    "entendi porra nenhuma"). A primeira foi no passo certo (o escrever
    achou o erro). A segunda foi minha (ver abaixo).
  - 3 frases: 1 de 3 com o "para quê". Ver pontos frágeis.
- Método:
  - **Coluna ↔ pergunta da reitoria** como régua de lista: a pergunta
    honesta que ele escreveu para `dia` ("todo dia 15") expôs a coluna
    sozinha. Usar em `dim_usuario` e no fato.
  - **Segundo caso concreto** (15/07 depois de 21/04) derrubou `feriado` sem
    eu dizer que estava errado.
  - **Uma linha só, com o nome das colunas em cima**, destravou o
    "entendi porra nenhuma" em uma troca. Mesmo resultado da tabela de 2
    linhas da 12.
  - **Previsão + `SELECT` de uma linha** para comportamento de SQL: o `t`
    ensinou mais que a explicação que veio depois.
- Falha do professor:
  - **Analogia do dicionário com mapeamento quebrado.** Troquei `a→1`,
    `b→0`, `c→3`, e isso põe o `0` depois do `1`, o que é falso em texto. Ele
    tropeçou no `0` ("porque ficaria 1 0 3 n?") e o `0` voltou como o
    porquê errado nas 3 frases. Devia ter rodado `SELECT '9' < '10';` com
    previsão, que não tem zero nenhum. **Analogia que eu não testei é pior
    que nenhuma.**
  - **"Copie a linha 12 e diga como se aplica"** seguido de "copie o valor do
    `DETAIL`": duas coisas, duas fontes → "entendi porra nenhuma". Mesmo erro
    das sessões 8 e 10.
  - Mandei comparar dois números de 8 dígitos de cabeça antes de mandar
    escrever. A régua (escrever antes de comparar) já existia.
- Aberto:
  - **`ORDER BY nome_dia` sai em ordem alfabética** (domingo, quarta,
    quinta, sábado, segunda, sexta, terça). Isca: o relatório da reitoria
    por dia da semana sai embaralhado, sem erro. Mesma família de texto ×
    número.
  - **`data_id` e `dia`/`mes`/`ano` dizem a mesma coisa duas vezes.** Nada
    impede `data_id = 20260315` com `dia = 16`. Mesma redundância de
    `data_fim_id`, com uma diferença a defender: a `dim_data` é gerada uma
    vez e o calendário não muda.
  - **Sem `CHECK` em `dia`, `mes`, `ano`.** `mes = 13` entra calado. Aplicar
    a lista do válido.
  - **Quem preenche a `dim_data`?** 365 linhas por ano não se escrevem à
    mão. Gancho para o gerador. E `tem_aula` exige o calendário acadêmico da
    universidade: premissa com fonte. Sábado tem aula?
  - `'Não se aplica'` × `'Desconhecido'` agora também em `tem_aula`.
  - `UNIQUE (dia, mes, ano)` no meio da lista de colunas. Funciona; quem lê
    procura no fim.
  - **Mensagens de commit:** `e6f07ff` foi com o texto do molde,
    `<o que mudou no projeto>`; `a09f067` diz "adição da `dim_local`" e só
    tem o PROGRESSO. A do schema ficou sem descrição.
  - `schema.sql` continua não rodando duas vezes, agora com 5 tabelas.
  - Faltam `dim_usuario` e `fato_transporte`.
  - Herdados: `data_fim_id` / `hora_fim_id` (décima sessão em aberto);
    nomear a universidade; senha `12345` no histórico antes de qualquer
    push; `modelo_database` e onde o compose fica; endereço de casa como
    dado pessoal; "Rua X" × "R. X".
  - **Ritmo para a reavaliação de 2026-11-02:** 13 sessões, 5 de 7 tabelas,
    0 de 10 itens do CURRICULO marcados. Ritmo atual: ~1 tabela por sessão.
- Retomo em:
  1. Revisão, previsão antes de rodar: `SELECT '9' < '10';`. Explicar o
     resultado sem falar em zero.
  2. `ORDER BY nome_dia`: prever a ordem, rodar com 7 linhas, decidir.
  3. `dim_usuario` escrita e rodada, com a régua coluna ↔ pergunta.

### Sessão 14 — 2026-10-03
- Fase: 1, semana 4 de 8 — modelagem dimensional, `ordem_dia` e `dim_usuario`
- Feito:
  - **O que quebrou na 13:** "n lembro". Com a pista (`'10'` em
    `BETWEEN '1' AND '3'` deu `t`), virou a revisão.
  - **Revisão texto × número.** Ver pontos frágeis. Melhor que a 13.
  - **`ORDER BY nome_dia` desmontado e consertado.** Escreveu os 7 nomes e
    achou `terça` por último. "Formato de data" caiu com o caso das 52
    segundas numa linha só do relatório. Com a tabela de 2 linhas
    (`segunda | ?`, `terça | ?`) chegou num número de ordem: `ordem_dia`.
  - **Domingo primeiro, decisão dele, com motivo:** o leitor é uma reitoria
    brasileira. Fato entregue: calendário brasileiro (domingo primeiro;
    "segunda-feira" é o segundo dia) × ISO 8601 (segunda `1`, domingo `7`).
    Escolheu `1 a 7` em vez de `0 a 6`: "na `dim_data` toda contagem começa
    em 1", como `dia` e `mes`.
  - **`ordem_dia INTEGER NOT NULL CHECK (ordem_dia BETWEEN 1 AND 7 OR
    ordem_dia = -1)`**, com `-1` no `INSERT`. Consertou o `OR -1` sozinho; o
    banco pegou 7 valores para 6 colunas e ele consertou. `DROP` + `CREATE`
    + `INSERT`; disco = banco, conferido. O banco reescreveu o `BETWEEN`
    como `>= 1 AND <= 7`, o que respondeu à pergunta dele ("between é >= ou
    >?").
  - **Revisão hostil `segunda | 5`.** Ver "Restrição no banco × garantia no
    processo".
  - **`dim_usuario` decidida, escrita e rodada, de primeira.** Régua coluna
    ↔ pergunta da reitoria:
    - `periodo` entra: muda o horário do fretado.
    - Endereço sai. Propôs rua/bairro/cidade/estado; com a lista das 9
      chaves do fato na tela, viu que isso chega pelo `origem_id` na
      `dim_local`. Caso do aluno 42 (mora em Pinheiros, às terças sai do
      estágio na Bela Vista): o endereço de casa erraria o ponto; a origem
      da viagem acerta.
    - Nome sai: "na verdade ela perguntaria por quantidade de alunos". Conta
      alunos pelo `usuario_id`, sem saber quem. De quebra, não guarda dado
      pessoal de 7.000 alunos.
    - Integral, pelo caso da aluna 77 (Medicina, manhã e tarde): o padrão de
      viagem não é o de quem só estuda de manhã. Listou sozinho as
      combinações dos 3 turnos (faltou `noite`, 7 no total). A lista vem da
      universidade, não da combinatória; fato de domínio entregue. Decisão
      dele: `Matutino`, `Vespertino`, `Noturno`, `Integral` e
      `Não se aplica`.
    - Previu "passa"; passou.
  - **`\dt` com 6 tabelas: todas as dimensões.** Falta só o
    `fato_transporte`.
  - **Perguntou se está atrasado.** Números entregues: semana 4 de 8, 0 de
    10 itens, 6 de 7 tabelas, ~14 sessões até 02/11 (12/10 e 02/11 são
    feriados), e nada do pipeline (gerador, dado, query). No ritmo atual
    chega em 02/11 com o star schema e pouco mais. Recomendação minha: não
    redecidir o prazo antes de 02/11; fechar o fato em 1–2 sessões e ir
    direto para dado e SQL de consulta. **Sessão num sábado**, contra o
    README (fim de semana é para candidatura).
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (5), lista do válido sem `-1` (2),
    `DROP` no `%`, restrição × processo, 3 frases.
  - "a primeiro e o b despercebido", invertido; mas a pergunta era ambígua
    (falha minha, abaixo).
  - Frustração duas vezes: "vsf claude, para com essa porra" (paginador) e
    "qual o objetivo dessa pergunta?". As duas foram minhas.
- Método:
  - **Escrever a lista**, de novo: os 7 nomes → `terça`; 1 a 7 com nomes →
    "quinta é 5".
  - **Tabela de 2 linhas com `?`** destravou o "n sei" da coluna nova.
  - **Mostrar a lista das chaves do fato** destravou `origem_id` em uma
    troca.
  - **Caso concreto com id de aluno** (42, 77) derrubou o endereço e testou
    a lista de turnos.
  - Previsão antes de rodar, 3 vezes: `f` (certa), "agora vai" (errou no
    `INSERT`), "s" na `dim_usuario` (certa).
- Falha do professor:
  - **Paginador do `psql`.** Mandei rolar com espaço e `q` → "vsf claude".
    Devia ter dado `\pset pager off` antes, ou conferido eu mesmo, como fiz
    na mensagem seguinte.
  - **Pergunta ambígua que eu não testei:** "qual você percebe no primeiro
    relatório?" — nos dois casos aparece algo estranho. Troquei por
    "quantas linhas você precisa conferir", que funcionou. Mesmo erro da
    analogia da sessão 13.
  - **Sequência longa sem dizer o objetivo.** ~12 trocas na defesa do
    gerador até ele perguntar "qual o objetivo dessa pergunta?". Dito o
    objetivo (a pergunta do entrevistador), ele engajou. Dizer no começo.
  - Li errado a referência dele a "id começar em zero" e atribuí à sessão 6.
- Aberto:
  - **Aluno que muda de turno** (noturno → matutino no meio do curso). Um
    `UPDATE` em `periodo` reclassifica as viagens antigas, feitas no
    noturno. Isca para dimensão de mudança lenta (SCD tipo 1 × tipo 2),
    clássico de entrevista.
  - **`periodo` × `hora_inicio_id`:** o fato já diz a hora de cada viagem,
    o mesmo argumento que tirou o endereço da `dim_usuario`. O que `periodo`
    responde que a hora da viagem não responde? (Defesa possível: aluno sem
    viagem nenhuma; planejamento do semestre seguinte.)
  - **`periodo` (`dim_usuario`) × `periodo_dia` (`dim_hora`):** nomes quase
    iguais, significados diferentes, lado a lado na mesma query.
  - **Endereço exato na `dim_local`:** tirou o endereço de casa da
    `dim_usuario`, mas o `origem_id` aponta para "Rua A, 120", que é a casa
    do aluno. Dado pessoal continua no schema.
  - **"Só o gerador escreve na `dim_data`"** não está escrito em lugar
    nenhum. E `EXTRACT(DOW)` devolve 0–6 com domingo 0; a escolha dele é
    1–7: o gerador precisa somar 1.
  - Turnos oferecidos entram na lista de premissas com fonte, junto com
    nomear a universidade e o calendário acadêmico (`tem_aula`).
  - Herdados: **`data_fim_id` / `hora_fim_id` (11ª sessão em aberto: decide
    na próxima, escrevendo o fato)**; `-1` um membro ou dois; `mes = 13` sem
    `CHECK`; `data_id` × `dia`/`mes`/`ano`; `schema.sql` não roda duas vezes
    (agora com 6 tabelas); `UNIQUE` no meio da lista; senha `12345` no
    histórico; `modelo_database`; "Rua X" × "R. X"; mensagens de commit.
  - **Ritmo para 2026-11-02:** 14 sessões, 6 de 7 tabelas, 0 de 10 itens do
    CURRICULO.
- Retomo em:
  1. Revisão curta, no máximo 10 min, sem andaime: "o que impede uma
     segunda com `ordem_dia = 5` na sua `dim_data`?". Dizer o objetivo
     antes da primeira pergunta.
  2. **`fato_transporte` escrito e rodado.** Decidir `data_fim_id` /
     `hora_fim_id` enquanto escreve. Sintaxe nova: `REFERENCES` (FK). Com o
     fato, o star schema fecha.
  3. Se der tempo: aluno que muda de turno.

### Sessão 15 — 2026-10-03
- Fase: 1, semana 4 de 8 — `fato_transporte`; star schema fechado
- Feito:
  - **O que quebrou na 14**, nas palavras dele: o endereço na
    `dim_usuario`, "sendo que a `dim_local` já traz". É o meio porquê; o
    caso do aluno 42 (casa × estágio) não voltou.
  - **Revisão `segunda | 5`.** Ver "Restrição no banco × garantia no
    processo". Melhor que a 14.
  - **Perguntou se o fato fechado fecha o item 1 do CURRICULO.** Resposta:
    fecha o artefato; o item só é marcado depois de um teste frio (5
    perguntas, sem o arquivo). Proposta minha: SCD (aluno que muda de
    turno) antes do teste, porque entrevistador pergunta.
  - **Grão rederivado.** "Deslocamento de um indivíduo" → metrô + Uber do
    42 = "uma" → `modal_id = transporte` → `42 | ?` com um lugar só →
    "duas". Frase dele: "por um meio de transporte"; o "único" (da sessão
    4, dele) fui eu que repus.
  - **9 chaves derivadas dimensão por dimensão**, numa tabela
    `dimensão | colunas no fato`. `local_id` → com `42 | ?` e dois locais →
    `origem_id`, `destino_id`. Hora: saída 7h, chegada 8h → `saida_id`,
    `chegada_id` → posto lado a lado com `data_saida_id`, viu que faltava a
    dimensão no nome → `hora_saida_id`, `hora_chegada_id`.
  - **`data_fim_id` / `hora_fim_id`: FECHADO, depois de 11 sessões
    aberto.** Caso de uma linha: saiu 7h50, durou 20 min; o fato guarda
    `hora_saida_id = 7`, `duracao = 20`; "7h20, o que estaria errado" (o
    real é 8h10). Frase dele: "hora de chegada precisa ficar, pois
    `hora_saida_id` conserva somente o valor da hora, ignorando os
    minutos". Mesmo teste na data: 23h50 de 15/03 + 20 min → a conta dá dia
    15, o real é dia 16. **As duas ficam**, com o nome saída/chegada no
    lugar de início/fim. O argumento da sessão 4 ("redundante, deriva de
    início + duração") só valia se a hora guardasse minutos: o grão da
    `dim_hora` derrubou a redundância.
  - **Métricas:** `duracao` (min), `distancia` (km), `preco` (reais), sem o
    "da viagem" no nome (argumento do `HD_`, dito por mim).
  - **Tipos, previstos:**
    - `distancia` inteira: previu `8` para 8,4 ("eu sei", sem rodar);
      certo, o Postgres arredonda. → decimal.
    - `preco` em `float`: recusou rodar ("n velho, n vou rodar"). Pedida só
      a previsão, eu rodei: previu `0,3`, saiu `0.30000000000000004`, e a
      comparação com `0.30` deu `f`. "N aparece" para o
      `WHERE preco = 0.30`: falha silenciosa. `NUMERIC(10, 2)` entregue
      como fato de documentação.
    - `distancia` também `NUMERIC`, com argumento dele (filtro que não
      acha a linha).
  - **`REFERENCES` entregue** com exemplo de fora (`venda`,
    `comprador_id` → `cliente (cliente_id)`), com o nome do papel
    diferente do nome da coluna lá, de propósito.
  - **Escreveu o fato.** Primeira linha: `dim_modal INTEGER REFERENCES
    modal (modal_id)`, com o nome da dimensão no lugar da coluna e a tabela
    sem `dim_`. A posição da coluna consertou com a linha encaixada no
    exemplo; `modal` → `dim_modal` ele consertou sozinho. **Decidiu testar
    duas linhas antes das doze** (passo pequeno, iniciativa dele). Travou
    em "quem está com quem"; a lacuna "a coluna ___ do fato aponta para a
    coluna ___ da tabela ___" destravou. As 9 `REFERENCES` saíram certas,
    as três de role-playing apontando para `local_id`, `hora_id` e
    `data_id`.
  - Previu "não passa" sem motivo; **passou de primeira.** `\dt` com **7
    tabelas: star schema fechado.**
  - **Revisão hostil, 1 de 4: `NOT NULL`.** Viu no `\d` que as chaves
    aceitam `NULL` ("mas n deveria"). Mecanismo em dois passos (ver pontos
    frágeis). Pôs `NOT NULL` nas 9 chaves e **fez o `DROP` + `CREATE`
    sozinho, sem eu pedir**. Disco = banco, conferido nos dois.
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (3), `transporte` como modal,
    "todas" as colunas como métrica, tipo no lugar de unidade, "0h20",
    `NULL` no `JOIN`, `duracao` inteiro no chat e `NUMERIC` no disco, 3
    frases (1 invertida).
  - "entendi porra nenhuma" e "ainda n entendi o que preciso responder":
    as duas por enunciado meu (abaixo).
- Método:
  - **Uma linha com `?`** (`42 | ?`) destravou grão, `dim_local` e hora de
    chegada. A melhor ferramenta da sessão, de novo.
  - **Lacuna em português para sintaxe** ("a coluna ___ do fato aponta
    para ___") destravou o `REFERENCES`.
  - **Duas linhas lado a lado** (`saida_id` × `data_saida_id`) mostraram o
    nome faltando sem eu dizer.
  - **Uma linha de exemplo preenchida** numa tabela vazia transformou "não
    sei o que responder" em resposta.
  - **Quando ele recusa rodar:** pedir só a previsão, rodar eu mesmo
    (`docker exec ... psql -c`), mostrar a saída. A surpresa ensina igual.
- Falha do professor:
  - **Mensagem com quatro peças** (`dim_modal` desenhada, linha `4`
    inventada, pergunta da reitoria, pergunta final) → "entendi porra
    nenhuma". Quinta vez (8, 10, 13, 14, 15). A versão de uma linha
    resolveu na hora. **Antes de mandar, contar as peças.**
  - **Tabela vazia sem linha de exemplo** → "ainda n entendi o que preciso
    responder".
  - **Desenhei `origem_id, destino_id` na mesma linha da tabela**, e ele
    perguntou, com razão, se iam na mesma linha do `CREATE TABLE`.
  - Repus "um único modal" no grão em vez de perguntar.
- Aberto:
  - **Revisão hostil, 2 a 4:**
    - `duracao NUMERIC (10,2)` no disco contra "inteiro, min" no chat.
    - `fato_transportes` no plural, com as 6 dimensões no singular e o
      grão falado como `fato_transporte`.
    - **O fato não tem `PRIMARY KEY`.** Duas linhas idênticas entram.
      Duplicata legítima ou erro? Chave substituta?
  - **Métricas aceitam `NULL`.** Metrô sem registro de saída:
    `hora_chegada_id` vai para `-1`, mas e a `duracao`? `NULL` (o `SUM`
    ignora) × `0` (o `SUM` mente). Contraste com a FK, que não pode ser
    `NULL`. E esse `-1` é **desconhecido**, não "não se aplica": caso forte
    para o membro duplo.
  - **Nada impede `data_chegada_id` < `data_saida_id`**, nem chegada
    incoerente com a `duracao`. Mesma família de restrição × processo.
  - `NUMERIC(10,2)` em `distancia`: 10 dígitos para km é exagero.
  - SCD (aluno que muda de turno), depois teste frio de star schema →
    marcar o item 1 do CURRICULO.
  - **Depois do item 1: dado e query.** O fato está vazio. Gerador
    sintético e o primeiro `SELECT` com `JOIN` levam a window functions e
    CTE (item 2).
  - `schema.sql` não roda duas vezes, agora com 7 tabelas.
  - Herdados: `-1` um membro ou dois; `mes = 13` sem `CHECK`; `data_id` ×
    `dia`/`mes`/`ano`; `UNIQUE` no meio da lista; senha `12345` no
    histórico; `modelo_database`; "Rua X" × "R. X"; endereço exato na
    `dim_local` como dado pessoal; `periodo` × `periodo_dia`; "só o gerador
    escreve na `dim_data`" não está escrito; `EXTRACT(DOW)` + 1; premissas
    com fonte (universidade, calendário, turnos).
  - **Ritmo para 2026-11-02:** 15 sessões, **7 de 7 tabelas**, 0 de 10
    itens do CURRICULO. Terceira sessão no sábado 03/10, contra o README.
- Retomo em:
  1. Revisão curta: a frase 1 invertida. Escrever `origem_id`,
     `destino_id` e `local_id` um embaixo do outro: quantas apontam para
     quantas, e por quê.
  2. Revisão hostil 2 a 4: `duracao`, nome no plural, `PRIMARY KEY`. Um
     `DROP` + `CREATE` só, no fim, com os três consertos.
  3. SCD: o aluno que muda de turno.

### Sessão 16 — 2026-10-03 (terminou depois da meia-noite)
- Fase: 1, semana 4 de 8 — revisão de role-playing
- Contexto: quarta sessão do sábado 03/10 (13 a 16), contra o README. Eu
  registrei isso na abertura e segui.
- Feito:
  - **O que quebrou na 15**, nas palavras dele: "usar `saida_hora` +
    `duracao` [...] não sabia sobre o erro acumulado no número flutuante".
    **Misturou dois mecanismos**: o da hora de chegada (grão da
    `dim_hora` perde os minutos) e o do float (`preco`). Com o caso da
    sessão 15 na tela (7h50, `hora_saida_id = 7`, `duracao = 20`) e a
    pergunta "onde aparece o float nessa conta?", separou sozinho: "não
    aparece, os minutos são ignorados". Depois localizou o float no
    `preco` e defendeu o `NUMERIC` contra "ninguém perde dinheiro com
    0,00000000000000004": o `WHERE preco = 0.30` não acha a linha. Disse
    `JOIN` querendo dizer filtro. **Os melhores 10 minutos da sessão.**
  - **Revisão de role-playing.** Ver pontos frágeis. Direção consertada
    colando a linha 43; porquê derivado com o aluno 42; frase final
    montada por mim.
  - **Ele quis seguir "até fechar o primeiro tópico".** Mostrei o que
    falta para marcar o item 1 (revisão hostil 2 a 4, SCD, teste frio) e
    que o teste frio não pode ser no mesmo dia em que se trabalhou o
    assunto: depois de quatro sessões de star schema, acertar mediria
    memória de minutos atrás. Com o item 1 fora do alcance de hoje,
    encerrou. **A opção de um conserto de 10 minutos para ter artefato
    não o motivou; fechar o item, sim.**
  - **Zero artefato.** Regra da sessão 5 quebrada pela segunda vez (11 e
    16). A pergunta da revisão hostil 2 ficou feita e sem resposta:
    `duracao NUMERIC (10,2)` foi decisão ou cópia da linha de baixo?
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (5), número sem rótulo, role-
    playing, 3 frases (1 de 3).
  - "n lembro", "entendi nd", "n entendi" e respostas de uma palavra na
    segunda metade, depois da meia-noite.
  - "aprendi que eu sou burro". Respondido com a evidência da sessão: o
    raciocínio da abertura funcionou, e os erros da segunda metade sumiram
    todos quando ele colou o texto. Quando é burrice, colar o texto não
    conserta nada.
- Método:
  - **Colar a linha** de novo destravou tudo o que a pergunta não
    destravou (linha 43 duas vezes, a palavra antes de `= Universidade`).
  - **Repor o bloco eu mesmo** quando ele cola o bloco errado.
  - **O caso da sessão anterior com uma pergunta** ("onde aparece o float
    nessa conta?") separou dois mecanismos misturados em uma troca.
- Falha do professor:
  - **Ida/volta + hipótese de duas tabelas + pergunta** numa mensagem →
    "entendi nd". Sexta vez (8, 10, 13, 14, 15, 16). Encolhido para "na
    ida, a Rua A é origem ou destino?", funcionou.
  - **Pergunta em duas partes** ("na ida...? e na volta?") → respondeu a
    segunda sobre outra coisa.
  - **Molde com duas lacunas** → "n entendi". Uma lacuna por vez resolveu.
  - **Montei a frase final por ele.** É o sinal da regra da sessão 4
    (comecei a entregar resposta → a sessão já tinha acabado). O
    fechamento confirmou: não fixou.
  - **Quarta sessão do dia, aberta e levada até depois da meia-noite.**
    Registrar o sábado e seguir não adiantou. A sessão rendeu uma revisão
    e nenhum artefato.
- Aberto:
  - **Revisão hostil 2 a 4**, sem mudança: `duracao` (pergunta já feita),
    `fato_transportes` no plural, fato sem `PRIMARY KEY`.
  - Todo o resto do "Aberto" da sessão 15 continua aberto.
  - **Ritmo para 2026-11-02:** 16 sessões, 7 de 7 tabelas, 0 de 10 itens
    do CURRICULO.
- Retomo em (**em outro dia**, não no mesmo dia de outra sessão):
  1. **Teste frio do star schema**, 5 perguntas, sem o arquivo, uma por
     vez. Inclui role-playing com a pergunta de entrevista e NULL em FK
     no `JOIN`. Dizer o objetivo antes: é o teste para marcar o item 1.
  2. Revisão hostil 2 a 4, começando pela resposta à pergunta do
     `duracao`. Um `DROP` + `CREATE` só. **Artefato.**
  3. SCD: o aluno que muda de turno. Com o teste frio passado e o SCD
     feito, o item 1 do CURRICULO é marcado.

### Sessão 17 — 2026-10-05 (registrada na 18, a partir das conversas)
- Fase: 1, semana 4 de 8 — teste frio do star schema
- Contexto: terminou sem as 3 frases, sem log e sem commit. Este registro
  foi escrito na sessão 18, lendo as duas conversas da noite de 05/10.
- Feito:
  - **O que quebrou na 16**, nas palavras dele: o float (`0,1 + 0,2`).
    Escreveu "NUMERIC para **aproximar**"; com uma pergunta, "float
    aproxima e NUMERIC pega o valor exato". Consertou o "arredondamento
    exato" da sessão 15.
  - **Teste frio, 1ª tentativa: não passou.** P2 (`preco` no fato,
    `periodo` na dimensão) limpa. P1 grão sem o modal; P3 NULL só com a
    consequência; P4 role-playing com "usada somente uma vez" (contradiz
    o próprio exemplo), e abriu o `schema.sql` no meio; P5 "não precisa"
    no lugar do risco.
  - Pediu para eu não travar nos testes. Recebeu as quatro correções numa
    mensagem. **Um minuto depois abriu outra conversa e pediu o teste de
    novo.** Essa conversa não sabia da primeira e declarou "passou". P1, P3
    e P4 repetiram as minhas palavras ("único modal", "não casa com
    nenhuma linha", "risco"). Válidas: P2 de novo e P5, pergunta nova
    (chave substituta: rename em 1 linha, grafias `Onibus`/`ONIBUS`,
    bytes), limpa.
  - P4 refeita com andaime: "posso estar indicando duas respostas
    diferentes", frase dele.
  - `duracao` → `NUMERIC (10)`. Ver "Responder contra o que derivou".
  - SCD aberto (aluno 42, noturno → matutino). Encerrou na 1ª pergunta.
- Falha do professor:
  - **"Passou" num teste refeito um minuto depois das respostas.** Mede
    memória de um minuto, o mesmo motivo que tirou o teste da sessão 16.
    A conversa que disse isso não tinha como saber da primeira: ver "Nota
    de método".
  - Sessão fechada sem PROGRESSO e sem commit. As 3 frases foram pedidas e
    não vieram.

### Sessão 18 — 2026-10-06
- Fase: 1, semana 5 de 8 — reteste frio e SCD. **Item 1 do CURRICULO
  marcado.**
- Feito:
  - Abri pedindo o teste, sem saber da 17. Ele: "já respondi o
    questionário". Li as conversas de 05/10 e mostrei o que contava: P2 e
    P5 valem; 1, 3 e 4 refeitas hoje, com casos novos.
  - **Reteste.** P1 grão: frase certa de primeira; o caso que prova
    precisou de dois empurrões (ver "Caso que ilustra × caso que
    prova"). P2 NULL no `JOIN` com `modal_id`: limpa. P3 role-playing
    com `dim_data`: limpa. **Teste frio: passou**, com a P1 frágil.
  - **Resposta final do grão** escrita com vocabulário que ele nunca usou
    ("trecho", "deslocamento contínuo", travessão). Disse que escreveu;
    aceito. Defendida linha por linha: "as somas continuam batendo com o
    total da viagem" vale para o preço e **não para a duração**: 20 + 50 =
    70 min contra 90 min. Os 20 min de espera na rodoviária não moram em
    linha nenhuma. "Não tinha calculado antes."
  - **SCD.** Ver pontos frágeis. Tipo 1 × tipo 2; chave por versão (101,
    102); a viagem de março aponta para a 101 ("surrogate key de
    versão", palavra dele); chave natural; `atual` booleano.
  - **Arquivo:** `dim_usuario` com `aluno_id INTEGER NOT NULL` e `atual
    BOOLEAN NOT NULL`; `INSERT` do `-1` com 4 valores (`aluno_id = -1`,
    `atual = true`).
  - **Recusou rodar** ("n vou rodar"). Rodei eu, numa transação só
    (`--single-transaction`, `ON_ERROR_STOP`), conferindo antes que o fato
    estava vazio e a `dim_usuario` só tinha o `-1`. 1ª vez: `INSERT has
    more expressions than target columns` → rollback, nada mudou. Ele
    consertou. 2ª: `DROP` × 2, `CREATE`, `INSERT 0 1`, `CREATE`. Disco =
    banco, 7 tabelas.
- Quebrou:
  - Ver pontos frágeis: caso que ilustra, "pra antiga e nova", chave
    natural que não chegou ao arquivo, `cidade` no exemplo de SCD.
  - Frustração alta e crescente: "foco!", "n viaja", "eu escrevi porra!",
    "MANO", "já chega", "vai se fuder, sai hoje sim, acelera porra!".
    Quis encerrar e, quando ouviu que o check não saía, voltou.
  - **3 frases: recusou** ("pulas as 3 frases de hoje"). Segunda sessão
    seguida sem elas (17 e 18).
- Método:
  - **Teste refeito com caso novo** (outra coluna, outra dimensão) separa
    entendimento de memória: as duas perguntas que ele tinha repetido
    palavra por palavra ontem saíram certas com palavras dele hoje.
  - **Citar a frase dele de volta** ("a coluna só guarda um") resolveu o
    "pra antiga e nova" em uma troca.
  - **Quando ele recusa rodar**, rodar eu numa transação só: o erro
    aparece e o banco não fica pela metade.
- Falha do professor:
  - Abri a sessão sem conferir que a 17 existia. A pista estava no `git
    status` (`schema.sql` modificado, sem commit) e na pasta de conversas.
  - "Escreva as duas linhas com as colunas da sua tabela", com ele já no
    limite, gerou o "MANO". Preencher as linhas eu mesmo, como fiz na
    mensagem seguinte, resolveu.
- Aberto:
  - **`atual` sem data.** O gerador vai gravar viagens de março depois que
    o 42 virou matutino. Com só `atual`, que versão ele escolhe para uma
    data passada? Leva a `valido_de`/`valido_ate` e a backfill (item 4).
  - **Nada impede duas linhas do mesmo `aluno_id` com `atual = true`.**
    Restrição × processo, de novo.
  - `aluno_id` com sufixo `_id` parece FK para uma `dim_aluno` que não
    existe.
  - **Tempo de espera entre trechos** não mora em linha nenhuma. Se a
    reitoria quiser tempo porta a porta, falta o que agrupa os trechos de
    uma viagem.
  - `duracao NUMERIC (10)` × `INTEGER`.
  - Revisão hostil 3 e 4, não feitas: `fato_transportes` no plural, fato
    sem `PRIMARY KEY`.
  - Herdados da 15: `-1` um membro ou dois; `mes = 13` sem `CHECK`;
    `schema.sql` não roda duas vezes; senha `12345` no histórico;
    endereço exato como dado pessoal; premissas com fonte.
  - **Ritmo:** 18 sessões para o item 1. Ver "Replanejamento" abaixo.
- **Replanejamento (fim da sessão, plano aprovado por ele):**
  - Motivo dele: "necessidade real". As vagas de Eng. IA e FDE pedem LLM,
    RAG, agente, evals, deploy e prova pública; Python em produção mais
    que SQL. Motivo dos números: 18 sessões no item 1, com 48 itens no
    CURRICULO, faziam LLM e RAG nunca chegarem.
  - Furos apontados: "SQL longe de LLM/RAG" é falso (pgvector, busca
    híbrida, julgar o SQL do text-to-SQL; a própria lista dele põe SQL
    em #2). "Evals primeiro" não dá sem sistema; o golden set, sim.
    Trocar de domínio custaria as 18 sessões.
  - Decisões dele: transporte + sintético; projeto público e processo
    privado; SQL e Python juntos; live coding de SQL "provável que não
    role", então SQL entra só por necessidade do projeto.
  - **Roteiro novo, blocos de 2 semanas:** A Python de produção + dado
    (06/10 a 17/10), B agente (20/10 a 31/10), C API + container (03/11 a
    14/11), D evals + RAG (17/11 a 28/11), E operar e mostrar (01/12 a
    12/12). O agente vem antes da API: a FastAPI serve o agente, e é aí
    que `async` faz sentido. Airflow, dbt, K8s, Terraform e MLOps ficam
    como conceito.
  - **Domingo vira dia de entrevista** (2h): live coding Python, design
    de IA, deep dive estilo Amazon em inglês. Pedido dele, a partir da
    entrevista da Amazon ("muitas perguntas de detalhamento de projeto").
    `ARQUITETURA.md` (escada de 5 perguntas por decisão) e `HISTORIAS.md`
    (8 histórias STAR) criados como moldes vazios; o conteúdo é dele.
  - README, CURRICULO e CLAUDE.md atualizados ("fase" → "bloco"; sábado
    candidaturas, domingo entrevista).
  - **Próxima reavaliação: 2026-10-17**, fim do bloco A, com o ritmo
    medido. Substitui a de 02/11.
- Retomo em:
  1. Revisão curta: SCD, 3 perguntas, no máximo 10 min (ele pediu para
     pular; é regra do CLAUDE.md).
  2. **Bloco A, sessão 1.** O `pyproject` e as pastas são boilerplate,
     então eu escrevo. Ele escreve o modelo Pydantic de uma viagem, com os
     campos tirados do `fato_transportes`, e o primeiro teste pytest que
     falha com uma viagem inválida. Antes de codar, ele explica em texto
     o que o contrato barra e por quê.
  3. Commit.
  - Primeiro domingo de entrevista: 2026-10-11. Começar pelo pitch e por
    uma entrada do `ARQUITETURA.md` (sugestão: `NUMERIC` × float, que
    ele já defende bem).

### Sessão 19 — 2026-10-07
- Bloco A, semana 1 de 2, sessão 1 do bloco — contrato de dado
- Duração: ~20 min (21h46 a 22h04). Encerrou ele, no meio de uma pergunta.
- Contexto: abriu como "Sessão 18". Conferi `git log` e as conversas: a 18
  estava registrada e commitada, então esta é a 19.
- Feito:
  - Pulou "o que quebrou na 18" e a revisão de SCD, mesmo encolhida para
    uma pergunta. Ver "SCD tipo 2".
  - Perguntou "estamos no bloco 2?". Contexto entregue: bloco A, o que é
    o contrato e por que vem antes do gerador.
  - **Caso da viagem impossível, dele: chegar antes de sair.** Primeiro
    fora do domínio (avião para Roma; "domínio" era palavra nova). No
    domínio, depois de refazer a chave `AAAAMMDD` (ver "Copiar a forma"):
    ```
    hora_saida_id | hora_chegada_id | data_saida_id | data_chegada_id
    13            | 11              | 20270112      | 20270111
    ```
  - **Vínculo novo:** a chave `AAAAMMDD` não serve só para o `BETWEEN` de
    março. É ela que faz a regra "a chegada não vem antes da saída"
    funcionar como comparação de números; em `DDMMAAAA`, a regra erraria
    calada.
  - **Por que o banco aceita, dele:** "eles só olham para as tabelas
    `dim_`". Mecanismo fechado com uma pergunta: o impossível aparece
    olhando "duas [colunas] do mesmo tipo", e `NOT NULL` e `REFERENCES`
    olham uma coluna por vez.
  - 3 frases: 1, com mecanismo. Ver "Fecha a sessão em sintaxe".
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (4), chave `AAAAMMDD` (6 passos),
    frase final trocada, SCD pulado.
  - **Zero artefato e zero Python** na sessão 1 do bloco de Python.
    Terceira sessão sem artefato (11, 16, 19).
- Falha do professor:
  - **A volta pela chave `AAAAMMDD` levou ~10 trocas, e o porquê dela só
    foi dito no fim.** Devia ter dito antes ("a regra do contrato compara
    duas datas; o número precisa estar na ordem do calendário"), como diz
    a regra de dizer o objetivo da sequência. Numa sessão de 20 min, comeu
    a sessão.
  - Pergunta em duas partes ("qual é menor? e qual vem primeiro no
    calendário?") → respondeu só a primeira. Mesmo erro da 16.
  - "No domínio" sem dizer o que é domínio.
- Aberto:
  - **Pergunta em que ele encerrou:** o `CHECK (data_chegada_id >=
    data_saida_id)` existe e barra a linha. Com 5 milhões de viagens numa
    carga só e a impossível na posição 3.200.000, se a única proteção é o
    `CHECK`, o que acontece? (A carga inteira volta, e o erro aparece no
    fim, longe do código que gerou a viagem. O contrato barra a viagem
    quando ela nasce, com o campo e o motivo. Resposta de entrevista: os
    dois, o contrato na entrada e o `CHECK` como última linha.)
  - **Hora sozinha não prova nada:** `hora_chegada_id = 0` com
    `hora_saida_id = 23` é a viagem que vira a meia-noite. A regra precisa
    comparar data e hora juntas. Isca para quando ele escrever o validador.
  - **O contrato modela o quê?** Uma linha do fato (chaves inteiras) ou a
    viagem como ela acontece (data e hora com minuto, nome do modal)? Com
    minuto, o contrato confere `duracao` contra saída e chegada, coisa que
    o banco não consegue (o grão da `dim_hora` perdeu os minutos). Decisão
    dele, antes de codar.
  - **Python 3.14.5 no Mac (Homebrew), README diz 3.12, sem `uv`.** Decidir
    antes do `pyproject`. É o `latest` × `18` de novo, agora em Python.
  - Herdados da 18: `atual` sem data; duas linhas `atual = true` para o
    mesmo aluno; `aluno_id` com sufixo `_id`; espera entre trechos;
    `duracao NUMERIC (10)`; plural do fato; fato sem `PRIMARY KEY`; e os
    da 15.
  - **Ritmo do bloco A:** 1 sessão de ~9 (até 17/10), zero linha de
    Python. Entregável: gerador tipado e testado, 5M viagens carregadas.
- Retomo em:
  1. Revisão: SCD, uma pergunta, frio ("o aluno 42 era noturno e virou
     matutino em maio; o que acontece na sua `dim_usuario`?"). Pulada
     duas vezes.
  2. Resposta à pergunta da carga (posição 3.200.000). Depois, a lista do
     que o contrato barra, regra por regra, cada uma com "banco, Python
     ou os dois?".
  3. Versão do Python decidida. `pyproject` e pastas (eu escrevo). Ele
     escreve o modelo Pydantic e o primeiro teste que falha com a viagem
     `20270112 → 20270111`. **A sessão não termina sem esse teste no
     disco, mesmo falhando.**

### Sessão 20 — 2026-10-14
- Bloco A, semana 2 de 2, sessão 2 do bloco — revisões e contrato × `CHECK`
- Duração: ~27 min (21h16 a 21h43). Encerrou ele ("to mt morto"), sem as
  3 frases.
- Contexto: 7 dias sem sessão desde a 19 (07/10). O domingo de entrevista
  de 11/10 não aconteceu. Minutos antes, numa outra conversa, perguntou se
  o projeto vai ter camadas de ML. Lá a resposta foi o escopo da sessão 18
  e a pergunta "curiosidade ou vaga?", que ficou sem resposta.
- Feito:
  - **O que quebrou na 19:** "nem ideia". Com a pista (`12032027`), virou
    revisão da chave: `20271105` de primeira, porquê com o zero. Ver
    pontos frágeis.
  - **Revisão de SCD, enfim** (pulada na 18 e na 19). Passou com andaime;
    o porquê final (`UPDATE` apaga o histórico) saiu dele. Ver pontos
    frágeis.
  - **Contrato × `CHECK`, a pergunta em que ele encerrou a 19.** Ver
    "Restrição no banco × garantia no processo".
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (3), o zero de novo, coluna ×
    linha no SCD, `JOIN` que "inibe" uma linha, risco que sobra.
  - **Zero artefato e zero Python, segunda sessão seguida no bloco de
    Python.** Quarta sessão sem artefato (11, 16, 19, 20). "A sessão só
    termina com o teste no disco" foi dito na abertura e não se cumpriu.
- Falha do professor:
  - **A abertura comeu a sessão.** "O que quebrou" virou uma revisão
    inteira (`AAAAMMDD`, ~8 trocas), depois veio a de SCD (~12) e depois a
    pergunta conceitual da carga (~8). Três revisões em 27 min, e ele
    cansou na pergunta da versão do Python, a primeira do caminho para o
    arquivo. Mesmo erro da sessão 5, e contra a memória "sessão precisa
    de artefato" (revisão ~15 min, depois arquivo). A pista do "o que
    quebrou" devia ter parado no `20271105` certo.
  - **Montei duas respostas de entrevista** com as peças dele (o inteiro
    compara da esquerda; "os dois, o contrato na entrada e o `CHECK` como
    última linha"). É o sinal da regra da sessão 4, e a sessão acabou
    duas mensagens depois.
- Aberto:
  - **Pergunta em que ele encerrou:** "o Python do Homebrew (3.14.5, que
    atualiza a cada `brew upgrade`) é o `postgres:18` ou o
    `postgres:latest`?". Depois, decidir 3.12 × 3.14 e onde a versão fica
    fixa (`requires-python`, `.python-version`, `uv`).
  - **O contrato modela o quê?** Linha do fato (chaves inteiras) × viagem
    com minuto. Sem mudança desde a 19.
  - Hora sozinha não prova nada (23h → 0h). Sem mudança.
  - **O escopo do bloco A não cabe no prazo.** Entregável: gerador tipado
    e testado, 5M viagens carregadas. Sobram 15/10 e 16/10, com zero
    Python. A regra do CLAUDE.md é cortar escopo, não estender prazo:
    a reavaliação de 17/10 decide o corte, com o ritmo medido.
  - Pergunta de ML (outra conversa): curiosidade ou vaga? Levar para a
    reavaliação de 17/10, que é onde se mexe no escopo.
  - Herdados da 19 e da 18, sem mudança.
  - **Ritmo do bloco A:** 2 sessões de ~9 (19 e 20), zero linha de Python.
- Retomo em (15/10, quinta):
  1. "O que quebrou na 20" + revisão de rotação, **no máximo 10 min,
     cronometrados**. Rotação: NULL em FK no `JOIN` (falta uma rotação
     limpa para voltar ao "Resolvido"). Se a pista do "o que quebrou"
     destravar, parar ali; não vira segunda revisão.
  2. A pergunta da versão (Homebrew = `18` ou `latest`?) e a decisão
     3.12 × 3.14. Eu escrevo `pyproject`, `.python-version`, pastas e o
     arquivo de teste vazio.
  3. Decisão "o contrato modela o quê?", em texto, com o porquê. Ele
     escreve o modelo Pydantic e o primeiro teste que falha com a viagem
     que chega antes de sair. **Primeiro arquivo dele antes dos 30 min de
     sessão.**

### Sessão 21 — 2026-10-15
- Bloco A, semana 2 de 2, sessão 3 do bloco — primeiro Python
- Duração: ~1h25 (20h51 a ~22h15). Encerrou ele, com o teste verde.
- Feito:
  - **O que quebrou na 20:** "n lembro". Com a pista (o segundo `101`),
    virou meia revisão. Ver "SCD tipo 2". Parada às 21h00, no relógio.
  - **Revisão de rotação (NULL em FK): não feita.** Adiada para depois
    do arquivo pelo limite de 10 min, e a sessão acabou antes.
  - **Versão do Python: 3.14, fixa.** Ver "`latest` × versão fixa".
  - **Boilerplate (eu):** `pyproject.toml` (hatchling, layout `src/`,
    Pydantic, pytest no grupo `dev`), `.python-version` (`3.14`),
    `src/assistente/__init__.py`, `tests/test_contrato.py` vazio,
    `.gitignore` com `.venv`, README com 3.14 e os comandos. Ele rodou
    `brew install uv && uv sync`: CPython 3.14.8 do uv; `uv.lock` com
    Pydantic 2.14.1 e pytest 9.1.1.
  - **O contrato modela o quê: A, a linha do fato.** Propôs A com a hora
    em minutos (`13*60 + 40 = 820`); com a FK para a `dim_hora` (0 a 23)
    na tela: "não está", hora inteira. Defendeu a data `AAAAMMDD` com
    20/03 × 15/05, sem o zero. Disse que B "gera complexidade,
    geralmente se quebra data e hora": vale para o fato, não para o
    contrato. Não discutido.
  - **Regra derivada antes de codar, por casos:** "qualquer hora desde
    que `data_chegada > data_saida`" barrava a viagem do mesmo dia; três
    linhas com `<` barravam 7h10 → 7h40 (ver "Responder contra o que
    derivou") → `<=`. Final: chegada em data posterior, qualquer hora;
    mesma data, `hora_saida <= hora_chegada`; chegada antes, não existe.
  - **Teste primeiro.** `tests/test_contrato.py`,
    `test_viagem_impossivel` (12/01 13h → 11/01 11h) com
    `pytest.raises(ValidationError)`. Previsão "falha" certa, com os
    rótulos trocados. `ModuleNotFoundError: No module named
    'assistente.contrato'`: vermelho. **Primeiro arquivo Python do
    projeto, às 21h46** (a meta era 21h21).
  - **Modelo:** `src/assistente/contrato.py`, `Viagem(BaseModel)` com as
    4 chaves `int` e um `@model_validator(mode="after")`. Escreveu a
    regra como o proibido (saída depois da chegada; ou mesma data e hora
    de saída maior), que é a negação exata da regra dele. Previu
    "passa"; rodou, consertou sozinho (`AND` → `and`, um `self.`),
    **`1 passed`**.
  - **3 frases: 2 de 3 com mecanismo.** Ver "Fecha a sessão em sintaxe".
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (2), responder contra a regra
    (7 < 7), `JOIN` que esconde linha, rótulos de Python, `.env` ×
    `.venv`.
  - **O arquivo verde está quebrado.** Linha 25: `data_chegada_id` sem
    `self.`. Toda viagem válida dá `NameError`. Conferido por mim; dito
    a ele só como isca ("existe uma viagem normal que derruba esse
    arquivo").
- Método:
  - **Ponte SQL → Python** (`CREATE TABLE`/`INSERT`/`CHECK`/erro do
    banco) destravou classe, objeto e `self`. Usar de novo para `Field`,
    `Literal` e fixture.
  - **Prever e rodar `python3 --version`** depois do brew: "oxe, 3.9".
    A lição do `latest` saiu da máquina dele, não de mim.
  - **Caso concreto contra a regra antes de codar** (mesmo dia; mesma
    hora) achou dois furos sem uma linha de código.
  - Copiar: a coluna do `101` e a linha `7 < 7`, as duas certas.
- Falha do professor:
  - **Primeiro arquivo aos 55 min, contra a meta de 30.** As duas
    decisões (versão, contrato) e o "explica do zero" couberam; a
    revisão de rotação, não. Decisão que só precisa de texto (versão,
    modelo) pode ser pedida no fim da sessão anterior.
  - Mandei "cole o exemplo da turma e troque três coisas": o exemplo
    ficou comentado no topo dos dois arquivos.
- Aberto:
  - **Isca:** a viagem normal que dá `NameError`. Próximo teste: uma
    viagem válida que **tem que passar**.
  - **O que a opção A não pega:** mesma data, mesma hora, 7h40 → 7h10.
    `7 <= 7` deixa passar. O minuto se perdeu no grão da `dim_hora`. É
    o argumento para B voltar, com evidência.
  - **Falso verde à vista:** quando o modelo tiver as 12 colunas
    obrigatórias, `test_viagem_impossivel` (4 colunas) continua verde
    pelo motivo errado: coluna faltando também é `ValidationError`.
  - Mensagem de erro `"impossivel"`, sem campo nem valor. O argumento
    dele para o contrato (sessão 20) era "o erro vem com o campo e o
    motivo".
  - Validador escrito como lista do proibido: aqui está completo, mas é
    a lista que erra calada (sessão 12).
  - Exemplo da turma comentado nos dois arquivos: código morto.
  - `python3` do Mac agora é o 3.9.6 da Apple: scripts do trabalho que
    chamam `python3` mudaram de versão.
  - Revisão de rotação NULL em FK, pendente. Juntar com o `JOIN` que
    "omite": 0 casamentos some, 2 casamentos duplica.
  - Domingo 18/10: candidata a primeira entrada do `ARQUITETURA.md` e
    primeira história do `HISTORIAS.md`: o brew trocou o Python do Mac e
    o projeto não caiu.
  - **Reavaliação de 17/10:** o bloco A, em 3 sessões, tem o contrato
    com 1 teste. Gerador e 5M viagens não cabem em uma sessão. Cortar
    escopo, não estender prazo.
- Retomo em (16/10, sexta, última sessão do bloco A):
  1. "O que quebrou na 21" + revisão de rotação: NULL em FK no `JOIN`,
     rodado no banco com 3 linhas, junto com o `101` duplicado. 10 min.
  2. A isca: ele escreve o teste da viagem 12/01 7h → 12/01 8h, que tem
     que passar. Prever, rodar, ler o `NameError`, consertar.
  3. O teste 7h40 → 7h10 na mesma hora: A deixa passar. Decidir A × B
     com o teste vermelho na tela.
  4. Commit. A reavaliação do bloco é no sábado, 17/10.
- Depois do fechamento: **repositório público no GitHub**,
  `Cleiltonss/campus-mobility-agent` (nome dele, escolhido entre 4).
  Avisado de que o histórico leva o PROGRESSO, o CLAUDE.md, as mensagens
  "sessão N" e a senha `12345`, e de que apagar do arquivo não apaga do
  histórico. Decisão dele: subir como está ("é tudo dado mockado e
  fictício") e ajeitar durante o projeto. README em português; só o nome
  em inglês. Pendente para o bloco E ("repo público"): separar processo
  de projeto, senha para `.env`, README só do sistema, `name` do
  `pyproject.toml` ainda `assistente-reitoria`. Em repo público,
  reescrever o histórico depois não apaga o que já foi clonado.

### Sessão 22 — 2026-10-16
- Bloco A, semana 2 de 2, sessão 4 do bloco (a última) — teste da
  viagem válida
- Duração: ~35 min (21h56 a 22h31). Encerrou ele, no meio de uma
  pergunta, sem as 3 frases.
- Feito:
  - Conferido antes de abrir: o último log (21) bate com o `git log` e
    com as conversas; a conversa de 15/10 de madrugada (UTC) é a 20.
  - **O que quebrou na 21:** "lembro de nada". Com a pista (teste verde,
    viagem normal que derruba o arquivo): "era a viagem do mesmo dia".
    Meio certo; ficou para o item 2.
  - **Revisão de rotação, NULL em FK: 3 de 3, frio, em 7 min** (21h56 a
    22h03). Voltou ao "Resolvido".
  - **Teste da viagem válida.** A regra da 21 veio certa de cabeça;
    pedida a viagem, deu a regra; depois `7 | 8 | 20261210 | 20261210`.
    "Não entendi" para "usa `pytest.raises`? por quê?"; encolhido
    ("espera que recuse ou aceite?") → "aceite" → "não". Duas regras do
    pytest entregues como fato, depois de ele reclamar com razão (ver
    Falha do professor). `test_viagem_possivel` **no disco às 22h11,
    antes da meta de 22h26. Primeira vez que a meta de arquivo foi
    cumprida.**
  - Previu "passa"; `1 failed, 1 passed`, `NameError` na linha 25 do
    contrato. Mexeu no teste (`with pytest():`); copiando a linha do
    `src/`, achou o arquivo; copiando as linhas 23 e 25, achou o
    `self.`. Revisão de `self` (ver pontos frágeis). Consertou as duas
    linhas; previu "dois"; **`2 passed`**. Disco conferido.
  - **Por que toda viagem válida quebrava:** cadeia de 6 perguntas, não
    fechou. Ver "Ler o código pela intenção".
  - 3 frases: recusou. Pediu que eu recapitule e reforce amanhã, com ele
    descansado.
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (3), responder contra o que
    derivou (3), mexer no teste com o erro no contrato, `self` = "a
    classe", "objetos" para campos, `Viagem2` para o segundo teste,
    leitura do `elif` pela intenção, "n sei" para o `1 passed`.
- Método:
  - **Abertura com hora para acabar** (até 22h06) acabou às 22h03, e o
    arquivo saiu às 22h11. A meta de 30 min funcionou na primeira vez em
    que a abertura teve hora marcada.
  - **Copiar a linha do traceback** destravou as três leituras de erro.
  - **Ponte SQL** de novo: dois `INSERT` na mesma tabela (o segundo
    teste) e `CREATE TABLE` × `INSERT` (o `self` é uma linha).
  - **O traceback do pytest como evidência:** a linha
    `self = Viagem(hora_saida_id=7, ...)` mostrou o que é `self`.
- Falha do professor:
  - **"Desse bloco, o que entra no teste novo?"** sem ter dito como o
    pytest decide verde. Ele: "n tem como saber, sem saber a sintaxe,
    vc viajou". Certo: é fato de documentação, e devia ter vindo junto
    com o pedido do teste.
  - **A cadeia "por que toda viagem válida quebrava"** começou às 22h25
    sem dizer o objetivo (a pergunta de entrevista "seu teste estava
    verde e o código quebrado: como?") e foi até ele encerrar no "n
    sei". Mesmo padrão das sessões 19 e 20: cadeia longa no fim.
- Aberto:
  - **Pergunta em que encerrou:** "a viagem `20270112` → `20270111`
    parava na linha 23 ou chegava à 25?". Leva a: o `1 passed` da 21
    provava só que essa viagem é recusada, e o resto do arquivo nunca
    tinha rodado. A resposta de entrevista quem monta é ele.
  - **Item 3 da 21, não feito:** 7h40 → 7h10 na mesma hora. A opção A
    deixa passar (`7 <= 7`). Decidir A × B com o teste vermelho.
  - Falso verde à vista (12 colunas), mensagem `"impossivel"` sem campo,
    validador como lista do proibido, exemplo da turma comentado nos
    dois arquivos: sem mudança.
  - `101` duplicado no `JOIN` (2 casamentos): próxima rotação.
  - Domingo 18/10: primeira entrada do `ARQUITETURA.md` e primeira
    história do `HISTORIAS.md` (o brew e os dois Pythons).
  - **Ritmo do bloco A, fechado:** 4 sessões (19 a 22), ~2h50 somadas.
    Entregue: contrato `Viagem` com 4 campos e 1 validador, 2 testes
    (recusa a impossível, aceita a válida). Não entregue: gerador, 5M
    viagens, dado sujo, window functions, query plan. O bloco B começa
    em 20/10, e o agente text-to-SQL consulta um fato que ainda está
    vazio.
- Retomo em (17/10, sábado, reavaliação do bloco A):
  1. **Recapitulação, como ele pediu, mas falada por ele:** as 3 frases
     da 22 em 3 perguntas (o que é `self`; por que toda viagem válida
     quebrava; o que o `1 passed` da 21 provava). Eu não recapitulo por
     ele.
  2. **Reavaliação do bloco A com os números acima.** Decidir o corte:
     o que do bloco A o agente do bloco B precisa (dado no fato) e o que
     vira só conceito. Regra do CLAUDE.md: cortar escopo, não estender
     prazo.
  3. Commit.

### Sessão 23 — 2026-10-19
- Bloco A, reavaliação (fim do bloco), na véspera do bloco B
- Duração: ~50 min (20h28 a 21h18). Encerrei eu, quando ele começou a
  responder contra as próprias respostas.
- Contexto: conferido antes de abrir: o último log (22) bate com o `git
  log`. A reavaliação de sábado (17/10) e o domingo de entrevista
  (18/10) não aconteceram; a conversa de 18/10 é de trabalho.
- Feito:
  - **O que quebrou + revisão:** as 3 perguntas da 22, que ele tinha
    pedido para eu recapitular, respondidas por ele, com o objetivo dito
    antes (a pergunta de entrevista "teste verde, código quebrado:
    como?").
    - `self`: ~15 min. Ver "Python: classe, objeto, `self`".
    - Por que toda viagem válida quebrava: fechou pela execução. Ver
      "Ler o código pela intenção".
    - O que o `1 passed` da 21 provava: não fechou. Ver "Caso que
      ilustra × caso que prova".
  - A abertura com hora marcada (20h40) estourou: acabou às 20h59.
  - **Reavaliação do bloco A.** Números: 10 sessões planejadas × 4
    feitas; ~20h × ~2h50; gerador + 5M × contrato com 2 testes.
    Perguntado se o ritmo daqui para frente fica perto do planejado ou
    do real: "to muito cansado durante os dias. mas continuo aqui.
    vamos seguir no planejamento". Lido como: as datas ficam (o B
    começa em 20/10) e, pela regra do CLAUDE.md, corta-se escopo.
    - O que o B precisa do A: "minha resiliência em não desistir"
      (desvio). Encolhido para "a reitoria pergunta e o fato tem zero
      linhas": "0". Falha silenciosa, agora no agente.
    - **Decisão: gerador pequeno** (centenas de viagens, cada uma pela
      `Viagem`, gravadas no Postgres) × seed à mão (~30 `INSERT`).
      Perguntou "qual é a mais profissional?"; respondido com o
      argumento dele das sessões 15 e 20 (o `INSERT` à mão é o risco
      que passa por fora do contrato). Frase dele, com a primeira
      metade minha: "gerador, pois toda linha do fato passa pela
      `Viagem` antes de entrar no banco". O fim, consertado com uma
      pergunta: o contrato barra "linhas que não atendem as restrições
      da viagem".
    - Saem do A: 5M viagens, `COPY` × `INSERT`, dado sujo, window
      functions, query plan. Voltam por necessidade do projeto ou como
      conceito. README e CURRICULO atualizados por mim, com a decisão
      dele.
  - 3 frases: 1 de 3. Ver "Fecha a sessão em sintaxe".
- Quebrou:
  - Ver pontos frágeis: não olhar a tela (4), responder contra o que
    derivou (2), `self` (classe, campo, atributo), o que o verde com
    `pytest.raises` prova.
  - Zero código. Quinta sessão sem artefato de código (11, 16, 19, 20,
    23); hoje o item planejado era a reavaliação.
- Método:
  - **Repor a frase eu mesmo** quando ele cola a linha errada: "n" na
    hora (o mesmo da sessão 16).
  - **Encolher para um número** ("a reitoria recebe o quê?") destravou
    o desvio da resiliência em uma troca.
  - **Múltipla escolha não funcionou** para o `self`: ele passou pelas
    opções uma a uma (a classe, o campo, a viagem). Quando o conceito
    não está lá, a opção vira chute.
  - A tabela dos dois testes (13 × 7) ficou sem resposta; o que
    destravou foi a ponte SQL, de novo.
- Falha do professor:
  - **Mensagem das opções do gerador** com duas opções, custo, o que
    sai do A, recomendação e pergunta → "o que a gente tá decidindo
    mesmo?". Sétima vez (8, 10, 13, 14, 15, 16, 23). A versão de uma
    linha resolveu.
  - **Pus o argumento na boca dele:** a frase da decisão repete a
    minha mensagem anterior. Devia ter perguntado "qual o risco do seed
    à mão?" antes de dizer.
  - **Cadeia no fim, com ele cansado** (o `1 passed`, ~8 trocas depois
    das 21h05), o mesmo padrão das sessões 19, 20 e 22. Com a abertura
    estourada, a pergunta devia ter ido direto para a próxima sessão.
  - Li "seguir no planejamento" como "as datas ficam, o escopo corta"
    sem confirmar com ele que o B também vai encolher.
- Aberto:
  - **Pergunta em que encerrou:** "teste com `pytest.raises` ficou
    verde: a viagem 12/01 → 11/01 foi aceita ou recusada?". Depois, a
    lacuna "o `1 passed` provava só que ___" e a resposta de entrevista,
    montada por ele.
  - **Corte do bloco B:** no ritmo medido, o gerador come de 2 a 3 das
    ~4 sessões do B. Golden set, agente, guardrails e MCP não cabem no
    que sobra. Decidir na primeira sessão do B, com opções de uma linha
    cada.
  - **Ritmo:** o README diz 2h/dia, e o medido é ~1h30 por semana. Ele
    quer manter o plano.
  - `contrato.py`, linhas 29 a 31: um `viagem_possivel` comentado e pela
    metade. Código morto, junto com o exemplo da turma.
  - Item 3 da 21 (7h40 → 7h10, A × B), falso verde à vista (12
    colunas), mensagem `"impossivel"` sem campo, validador como lista
    do proibido: sem mudança. O gerador vai mexer nisso, porque vai
    gerar as 12 colunas.
  - `101` duplicado no `JOIN`: próxima rotação.
  - Domingo 25/10: primeiro domingo de entrevista (os de 11/10 e 18/10
    não aconteceram). Primeira entrada do `ARQUITETURA.md` e primeira
    história do `HISTORIAS.md` (o brew e os dois Pythons).
- Retomo em (20/10, terça, sessão 1 do bloco B):
  1. "O que quebrou na 23" = a pergunta do verde com `pytest.raises` e
     a lacuna do `1 passed`. **Até 10 min, com hora marcada.** Se não
     fechar, vai para o domingo.
  2. Corte do bloco B, com opções de uma linha. A decisão é dele.
  3. Gerador: antes de codar, ele explica em texto o que vai fazer
     (quantas viagens, de onde sai cada uma das 12 colunas, onde a
     `Viagem` entra, como grava no banco), e eu aponto o furo. Eu
     escrevo o arquivo de teste vazio do gerador.
  4. Commit.
