# Madame Oriel — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.16. Dados: `dados/dialogos/oriel.json`. Serviços: `docs/LOJAS.md`, secção 2.13.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | graves e com eco, como se viessem de longe; fazem um "plim" de pulseiras no fim |
| Como fala | por enigmas, com pausas dramáticas; depois estraga o mistério com uma piada seca |
| Repete | "As cartas dizem…", "Ou não.", "Interessante. Para mim. Para ti, talvez não." |
| Tiques | baralha as cartas sem parar (animação `baralhar`); pulseiras a tilintar |
| Nunca diz | o que viu nas estrelas antes dos 8 corações; a idade |
| Chama ao herói | "Dez Mil" (sempre, desde o início; é ela quem mais insiste no número) |
| Quem é | foi astrónoma no **Observatório Celeste** (andar 86). Há 30 anos viu nas estrelas uma coisa que a fez descer. Desceu (descer não precisa de Jogador) e abriu a tenda para **esperar** |
| Rotina | dorme de manhã · tenda 14:00–2:00 · ao Domingo, à meia-noite, sobe ao telhado da Biblioteca para ver as estrelas |

---

## 2. Primeira conversa

- 🎬 Antes de o herói falar, a Oriel vira uma carta: *A Torre*.
- **Madame Oriel** *(normal)*: "Dez Mil. Finalmente. Estás atrasad{o/a} trinta anos. Ou adiantad{o/a}. Depende de quem conta."
- **Madame Oriel** *(feliz)*: "Senta-te. Não, não te vou adivinhar o futuro de graça. Ninguém vive de enigmas grátis."
- **Madame Oriel** *(normal)*: "Vendo três coisas: sorte para o dia, segredos para a subida e a morada de uma tartaruga gigante. Tudo verdade. Às vezes."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Serviços (carta do dia, profecias, Cidade Errante) · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `oriel_dia_01` | `hora entre 14 e 16` | normal | "Acabei de acordar. As estrelas dormem de dia. Eu imito-as." |
| `oriel_dia_02` | `hora entre 22 e 2` | feliz | "A melhor hora. As cartas falam mais alto à noite. Ou eu ouço melhor. É a mesma coisa." |
| `oriel_dia_03` | — | normal | "Vejo… um baú. Ou uma caixa. Ou um caixão. As cartas não são precisas." |
| `oriel_dia_04` | — | normal | "O teu número tem quatro zeros. Isso diz-me tudo. E nada. Sobretudo tudo." |
| `oriel_dia_05` | — | feliz | "Previ que virias hoje. Também previ ontem. E anteontem. Acabo sempre por acertar." |
| `oriel_dia_06` | — | normal | "O Tobias pediu-me os números da sorte. Dei-lhe sete. Ele perdeu sete moedas. Os números estavam certos: perdeu sete." |
| `oriel_dia_07` | — | normal | "O futuro é como o nevoeiro. Vê-se melhor de longe. De perto só se vê os pés." |
| `oriel_dia_08` | — | feliz | "A Lyra pergunta-me todas as semanas pelo amor. As cartas respondem sempre 'gato'. Ela tem um gato. As cartas não mentem." |
| `oriel_dia_09` | `dia_semana == domingo` | normal | "Hoje à meia-noite subo ao telhado da biblioteca. O Fausto deixa. Diz que as estrelas também são livros." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `oriel_dia_20` | `estacao == primavera` | normal | "Primavera: as constelações do caçador. Bom tempo para subir. Mau tempo para alergias." |
| `oriel_dia_21` | `estacao == verao` | feliz | "No verão as estrelas estão mais perto. É mentira. Mas parece." |
| `oriel_dia_22` | `estacao == outono` | normal | "Outono. As estrelas caem mais. Se vires uma cadente, guarda-ma. Literalmente: elas caem na torre." |
| `oriel_dia_23` | `estacao == inverno` | normal | "No inverno o céu está limpo e frio. Como a verdade. E também me dá constipações." |
| `oriel_dia_24` | `clima == nevoeiro` | zangado | "Nevoeiro. Sem estrelas. Sem cartas boas. Hoje as profecias têm desconto. Por serem piores." |
| `oriel_dia_25` | `clima == trovoada` | feliz | "Trovoada! Os raios desenham letras no céu. Hoje estão a escrever 'cuidado'. Ou 'cuidados'. Letra má." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `oriel_dia_40` | `andar_maximo >= 19 && missao(R2_12) != concluida` | normal | "Há um lago no andar 19 onde o teu reflexo tem ideias próprias. Encontra-o. Vence-o. Sem poções. O reflexo também não as tem." |
| `oriel_dia_41` | `andar_maximo >= 38` | normal | "Um nome raspado numa porta. As cartas tremem quando falo dele. Eu também." |
| `oriel_dia_42` | `missao(H_14) == concluida && missao(H_16) != concluida` | triste | "Tirei a carta do rapaz de casaco azul. Saiu ao contrário. Não quer dizer morte. Quer dizer 'perdido'. Ainda há caminho." |
| `oriel_dia_43` | `andar_maximo >= 81` | feliz | "Chegaste ao céu. À minha terra. Se fores ao Observatório, não olhes para o telescópio grande. Ou olha. Depois vem falar comigo." |
| `oriel_dia_44` | `missao(H_21) == concluida` | triste | "Agora sabes. Sabes porque é que eu desci e esperei. Senta-te. Hoje não cobro." |
| `oriel_dia_45` | `andar_maximo >= 95` | normal | "Já não preciso das cartas para saber onde estás. Estás no fim. As cartas ficam quietas no fim." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `oriel_dia_60` | `coracoes(oriel) >= 2` | feliz | "Tirei a tua carta da sorte antes de chegares. Já está paga. Pelas estrelas." |
| `oriel_dia_61` | `coracoes(oriel) >= 4` | normal | "Já não te leio as cartas por dinheiro. Leio por curiosidade. É mais caro para mim." |
| `oriel_dia_62` | `coracoes(oriel) >= 6` | feliz | "Gosto de ti, Dez Mil. Não te habitues. As videntes não gostam de ninguém. É má para o negócio." |
| `oriel_dia_63` | `coracoes(oriel) >= 8` | triste | "Às vezes olho para ti e vejo outra pessoa. Uma pessoa muito antiga. Não te preocupes. Não és tu. Ainda." |
| `oriel_dia_64` | `coracoes(oriel) >= 10` | feliz | "Já não sei o teu futuro. Deixei de o ver. Sabes o que isso quer dizer? Que és tu que o escreves." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `oriel_dia_70` | `origem == dormir` | normal | "Foste trazid{o/a} a sonhar. Os que chegam a dormir veem coisas que os outros não veem. Toma nota dos teus sonhos." |
| `oriel_dia_71` | `origem == jogador` | feliz | "No teu mundo havia jogos com profecias? E eram verdade? Então não eram profecias. Eram spoilers." |
| `oriel_dia_72` | `skill_unica == sorte_do_heroi` | feliz | "Sorte do Herói. Tens sorte por natureza. Sabes como isso me irrita? As cartas ficam sem trabalho." |
| `oriel_dia_73` | `skill_unica == olho_do_sistema` | normal | "Vês o que a janela vê. Cuidado. Quem vê com os olhos da torre começa a pensar como ela." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `oriel_curta_1` | normal | "As cartas já falaram hoje. Amanhã falam outra vez." |
| `oriel_curta_2` | feliz | "Previ que voltavas. Acertei. Outra vez." |
| `oriel_curta_3` | normal | "Shhh. Estou a ouvir as estrelas. Não, não é o Fausto a ressonar. Talvez." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Madame Oriel** *(normal)*: "A torre é uma pergunta. Cada andar é uma resposta errada. O último andar é a pergunta outra vez."
- **Madame Oriel** *(feliz)*: "Não percebeste? Ótimo. Eu também não percebi. Mas soa bem, não soa?"

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "Na floresta há uma árvore que te vai dizer uma frase. Lembra-te dela. Vais precisar no fim." |
| 2 Cavernas | "Debaixo da terra há um lago negro. O teu reflexo lá dentro sabe coisas. Não confies nele. Ouve-o." |
| 3 Pântano | "Vais ter de escolher entre a ordem e o que está certo. As cartas não te dizem qual escolher. Só que vais lembrar-te da escolha." |
| 4 Deserto | "Uma porta com nomes. O último raspado. As cartas recusam-se a dizer-mo. Isso nunca me acontece." |
| 5 Gelo | "No gelo o tempo passa devagar e as memórias congelam. Leva uma fotografia. Ou uma flor. Qualquer coisa que te lembre de casa." |
| 6 Oceano | "No mar vais perder alguém. Não para sempre. Mas vais perder. Prepara-te. Não há preparação. Prepara-te na mesma." |
| 7 Vulcão | "No fogo vais encontrar quem perdeste. E vais ter de escolher entre vencer e salvar. As cartas gostam desta parte. Eu não." |
| 8 Reino Assombrado | "Os mortos do reino não sabem que morreram. Os vivos também às vezes não sabem que estão vivos." |
| 9 Céu | "A minha terra. O Observatório. Diz à Vega que ainda tenho o telescópio pequeno dela. Não o devolvo." |
| 10 Abismo | "Aí as cartas ficam em branco. Todas. Ninguém vê o que está no fim. Nem eu. Sobretudo eu." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `oriel_rumor_01` | — | "A Cidade Errante anda nas costas de uma tartaruga. Pergunta-me onde está. Custa vinte moedas. Ou um sorriso. Vinte moedas." |
| `oriel_rumor_02` | — | "O meu baralho tinha vinte e duas cartas. Agora tem vinte e uma. A que falta anda por aí, numa tartaruga." |
| `oriel_rumor_03` | `andar_maximo >= 10` | "Há monstros com nome que só aparecem com lua cheia. Eu sei quando há lua cheia. Também sei onde. Isso é que custa." |
| `oriel_rumor_04` | `andar_maximo >= 20` | "Posso voltar a sortear a tua Skill Única. Uma vez. É caro. As estrelas cobram juros." |
| `oriel_rumor_05` | `andar_maximo >= 41` | "Um mamute ancião anda pelo gelo. Podes matá-lo. Ou acalmá-lo. As cartas preferem a segunda. Eu também." |
| `oriel_rumor_06` | `andar_maximo >= 86` | "No Observatório há uma carta minha escondida. A Vega guarda-a. Pede-lha por mim. Educadamente. Ela morde." |

### 4.4 A vida dela
| Corações | Fala |
|---|---|
| 0 | "A minha vida? Isso é segredo profissional. Pago para o guardar." |
| 2 | "Nasci no céu, numa ilha de nuvens. Contava estrelas no Observatório. Era astrónoma. As cartas vieram depois, quando as estrelas me assustaram." |
| 4 | "As cartas não preveem nada. Ajudam as pessoas a dizer em voz alta o que já sabiam. Não contes a ninguém. Perco a clientela." |
| 6 | "A Vega era a minha mestra. Ainda lhe escrevo. Ela não responde. Ou responde e as cartas não chegam. Prefiro a segunda." |
| 8 | "Desci há trinta anos. Por causa de uma coisa que vi. Ainda não te digo. Mas é sobre ti." |
| 10 | "Agora já sabes tudo o que eu sei. E sabes mais do que eu. É a primeira vez que um cliente sai daqui mais sábio do que a vidente." |

---

## 5. Presentes

**Adora:** Estrela Cadente, Cristal Celeste, cartas antigas · **Gosta:** cristais, chá · **Detesta:** céticos — a escolha
de diálogo "Isso é tudo mentira" dá −30 (há uma em cada cena de coração e às vezes na carta do dia).

| Reação | Falas |
|---|---|
| Adora | "Previ que me ias dar isto. Não previ. Mas digo que previ. É o meu trabalho." · "Uma estrela cadente! Faz um pedido. Não, faço eu. Já fiz. Não te digo qual." |
| Gosta | "Um cristal. Bom para meditar. Ou para atirar a quem não paga." |
| Neutro | "Obrigada. As cartas dizem que vou usar isto. Não dizem quando." |
| Não gosta | "Hmm. As cartas também não gostaram." |
| Detesta | "Isto tem má energia. E mau cheiro. Sobretudo mau cheiro." |

| Item | Fala |
|---|---|
| A 22.ª carta (missão) | ver N_ORIEL_3 |
| Telescópio (decoração) | "Um telescópio! Não te vou dizer o que vejo com ele. Vou só dizer 'obrigada' e olhar muito tempo." |

---

## 6. Aniversário e festivais

**Aniversário (Inverno, dia 28 — o último dia do ano):**
- Sem presente: "Faço anos no último dia do ano. É uma piada das estrelas. Acabo sempre com tudo a acabar."
- Com presente que adora: "Um presente! Previ que alguém se ia lembrar. Previ errado: previ que ninguém se lembrava. Ainda bem."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Leio o futuro nas pétalas. Bem-me-quer, mal-me-quer. É astronomia de jardim." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "As cartas disseram que ia dançar hoje. Pensei que era com o Fausto. Que alívio." ⚙ +100 |
| F_02 Festival da Pesca | "Prevejo que o Pip vai mentir sobre o tamanho do peixe. Não é profecia. É estatística." |
| F_03 Noite dos Espíritos | "Esta noite as cartas falam com os mortos. Não leio as cartas esta noite. Os mortos falam demais." |
| F_04 Festival da Estrela | "O meu festival. Esta noite subo ao telhado e conto estrelas. Vem comigo. Contamos até nos enganarmos." |
| F_05 Dia da Subida | "Previ a tua vitória. Também previ a derrota. Ganhei a aposta comigo mesma." |
| F_06 Concurso da Casa | "Um conselho: põe a cama virada para norte. Não por magia. Por causa do sol da manhã." |
| F_07 Noite das Lanternas | "As lanternas no rio parecem estrelas caídas. Ponho uma pela Vega. Ainda está viva. Ponho na mesma. É para ela me escrever." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "As cartas disseram 'javali'. Também disseram 'rei'. Juntei as duas. Sou boa nisto." |
| Ent Ancião (10) | "'Não sejas como o anterior.' Guarda essa frase. Daqui a muito tempo vais perceber quem era o anterior. Eu já percebi. Não te digo." |
| Aranha-Mãe (15) | "Protegia os filhos. A carta dela é a Mãe. Saiu-me três vezes esta semana. Coitada." |
| Golem de Cristal (20) | "Ajoelhou-se perante a janela. As cartas também se ajoelham, às vezes. Quando caem." |
| Serpente do Lodo (25) | "Um ovo com uma janela azul lá dentro… A torre faz cópias de si mesma. Pequeninas. Isso não me deixa dormir. Durmo de dia, mas mesmo assim." |
| Hidra do Pântano (30) | "Cada cabeça que cortas, nascem duas. Cada pergunta que respondes, nascem duas. Bem-vind{o/a} ao meu trabalho." |
| Escorpião Imperador (35) | "A marca da janela na carapaça. A torre marca o que é dela. Verifica as tuas costas. Não, é piada. Ou não." |
| Faraó Eterno (40) | "'Eu também subi. Eu também quis voltar.' As cartas choraram. Não choram. Mas ficaram húmidas." |
| Yeti Ancião (45) | "Um monstro que guardava memórias. Há mais memória num yeti do que numa vidente. Eu esqueço tudo menos o futuro." |
| Dragão de Gelo (50) | "Metade. As cartas viraram-se todas ao mesmo tempo. Nunca tinham feito isso. Estão a ficar entusiasmadas." |
| Capitão Esqueleto (55) | "Os fantasmas tinham números. Contei-os nas cartas. Muitos. Demasiados." |
| Leviatã (60) | "O mar está calmo. O rapaz continua perdido. Não para sempre. As cartas prometeram. E as cartas cumprem quando querem." |
| Ferreiro Infernal (65) | "Uma arma com o teu número, feita antes de chegares. Eu disse-te. O teu número diz tudo." |
| Kai — salvo (68) | "A carta dele voltou a ficar direita. Eu sabia. Bem, esperava. Esperar é saber com medo." |
| Kai — vencido (68) | "A carta dele desapareceu do baralho. Não ardeu. Desapareceu. Quer dizer que ainda não acabou. Lembra-te disso." |
| Titã de Magma (70) | "O titã dorme. Os cultistas choram. As cartas riem-se. Têm mau feitio." |
| Lich Bibliotecário (75) | "Um morto que guardava livros. O Fausto daqui a cem anos. Não lhe digas que eu disse isto." |
| Rei Sem Coroa (80) | "'Talvez tu.' Ele disse 'talvez tu'. As estrelas disseram-me o mesmo há trinta anos." |
| Grifo Real (85) | "Passaste pela minha terra. Viste o Observatório? Viste a Vega? Ela perguntou por mim? Não perguntou. Claro que não." |
| Serafim Caído (90) | "Agora sabes o que eu vi nas estrelas. Ou parte. Senta-te. Hoje não há cartas. Só chá." |
| Guardião do Tempo (95) | "O tempo disse-te que te viu passar mil vezes. Eu só te vi passar uma. Chega-me." |

---

## 8. Cenas de coração

### ❤️ 2 — A previsão que acertou

| | |
|---|---|
| ID | `cena_oriel_2` |
| Quando | 2 ❤️ · entrar na Tenda depois de ter morrido **ou** de ter encontrado um baú de ouro nesse dia |
| Onde | Tenda da Vidente |
| Quem | herói, Madame Oriel |
| Música | `ascendia_noite` (com sinos) |

🎬 A Oriel tem uma carta virada na mesa antes de o herói entrar. Aponta para ela sem levantar os olhos.
🎬 A carta mostra exatamente o que aconteceu ao herói nesse dia (um baú ou uma queda).

- **Madame Oriel** *(feliz)*: "Tirei esta carta de manhã. Antes de saíres de casa. Diz-me que não acertei."

▶ **"Acertaste."**
▶ **"Isso é tudo mentira."**

- *(acertaste)* **Oriel** *(feliz)*: "Claro que acertei. Às vezes acerto. Hoje acertei. Vou guardar esta carta numa moldura." ⚙ +30
- *(mentira)* **Oriel** *(zangado)*: "Mentira? Ótimo. Então paga a próxima a dobrar. Os céticos pagam a dobrar." ⚙ −30

⚙ 5% de desconto nos serviços da tenda.

### ❤️ 4 — As cartas a sério

| | |
|---|---|
| ID | `cena_oriel_4` |
| Quando | 4 ❤️ · entrar na Tenda depois da meia-noite |
| Onde | Tenda, só com a luz de uma bola de vidro |
| Quem | herói, Madame Oriel |
| Música | `revelacao` (suave) |

🎬 A Oriel tira as pulseiras uma a uma. Fica em silêncio. É a primeira vez que não faz piadas.

- **Madame Oriel** *(normal)*: "Esta noite leio-te a sério. Sem graça. Sem dinheiro. Três cartas."
- 🎬 Primeira carta: *O Viajante*. **Oriel**: "Vieste de longe. Não por escolha. Vais escolher muito, a partir de agora."
- 🎬 Segunda carta: *Os Dois*. **Oriel**: "Há alguém que sobe ao teu lado. Vai cair. Vais ter de decidir se o apanhas."
- 🎬 Terceira carta: *A Cadeira Vazia*. **Oriel** *(triste)*: "E esta… esta é uma carta que eu nunca tinha tirado. Uma cadeira, no alto, à espera."
- **Oriel** *(normal)*: "Não sei o que quer dizer. Mentira: sei um bocadinho. Mas não to digo. Ainda."

▶ **"Vou apanhá-lo."**
▶ **"E se eu não quiser a cadeira?"**

- *(apanhá-lo)* **Oriel** *(feliz)*: "Então lembra-te disto quando chegar a altura. Lembra-te que disseste." ⚙ +30 · flag `oriel_aviso_kai`
- *(cadeira)* **Oriel** *(triste)*: "Então és a primeira pessoa que mo diz antes de a ver. Isso é bom sinal. Acho." ⚙ +30

⚙ Recebe o **Baralho Pequeno** (decoração) e a **carta do dia** passa a dar o dobro do bónus às sextas.

### ❤️ 6 — A Carta da Oriel

| | |
|---|---|
| ID | `cena_oriel_6` |
| Quando | 6 ❤️ · `andar_maximo >= 81` · falar com ela |
| Onde | Tenda |
| Quem | herói, Madame Oriel |
| Música | `aeropolis` (versão com cordas) |

- **Madame Oriel** *(nervosa)*: "Vais passar pelo Observatório, não vais? Leva isto à Vega. É uma carta. Não, não é profecia. É uma carta normal. Com desculpas."
- **Madame Oriel** *(triste)*: "Saí de lá a meio da noite, sem me despedir. Trinta anos. Ela deve estar furiosa. Ou morta. Não, morta não. Furiosa."

⚙ Missão **R9_08 A Carta da Oriel** (secção 9). A Oriel aceita jantar em tua casa (lê-te as cartas à sobremesa).

### ❤️ 8 — O que ela viu nas estrelas

| | |
|---|---|
| ID | `cena_oriel_8` |
| Quando | 8 ❤️ · Domingo, meia-noite, telhado da Biblioteca |
| Onde | telhado da Biblioteca, céu limpo |
| Quem | herói, Madame Oriel |
| Música | `mar_de_estrelas` (versão calma) |

🎬 A Oriel está deitada no telhado a olhar para cima. Faz sinal ao herói para se deitar também.
🎥 A câmara roda para cima e mostra o céu de Ascendia, com a torre a cortar as estrelas ao meio.

- **Madame Oriel** *(normal)*: "Há trinta anos, no Observatório, as estrelas mexeram-se. Numa noite só. Fizeram um desenho."
- **Madame Oriel** *(normal)*: "Era um número. 10 000. Durou uma hora. Depois as estrelas voltaram ao sítio e ninguém acreditou em mim."
- **Madame Oriel** *(triste)*: "Por baixo do número, as estrelas fizeram outra coisa: uma porta. Aberta. E ninguém a passar."
- **Madame Oriel** *(normal)*: "Desci para esperar por ti. Abri uma tenda, aprendi a fazer piadas e a ler cartas, e esperei. Trinta anos."

▶ **"Porque é que esperaste?"**
▶ **"O que quer dizer a porta?"**

- *(esperaste)* **Oriel** *(feliz)*: "Porque alguém tinha de te dizer que eras esperad{o/a}. Não pela torre. Por uma pessoa. Pronto. Já disse." ⚙ +30
- *(porta)* **Oriel** *(normal)*: "Não sei. Acho que quer dizer que há uma saída que ninguém usou. Ou que ninguém quis usar. Descobre tu." ⚙ +30 · flag `oriel_porta` (conta para uma fala no final secreto "A Ponte")

⚙ 15% de desconto. Passa a mandar **cartas** (verdadeiras: uma carta do baralho por semana, que dá um bónus pequeno no dia em que a abres).

### ❤️ 10 — A Bola de Cristal

| | |
|---|---|
| ID | `cena_oriel_10` |
| Quando | 10 ❤️ · `missao(N_ORIEL_3) == concluida` · entrar na Tenda |
| Onde | Tenda, com o baralho completo (22 cartas) espalhado na mesa |
| Quem | herói, Madame Oriel |
| Música | `tema_oriel` (sinos, harpa e uma voz sem palavras) |

- **Madame Oriel** *(feliz)*: "Vinte e duas. O baralho completo. Há trinta anos que não o via assim."
- 🎬 Tira a carta 22, a que o herói trouxe: mostra uma pessoa a sair por uma porta com um saco às costas. *O Regresso*.
- **Madame Oriel** *(normal)*: "Era esta que faltava. Claro que era esta. A torre esconde sempre a carta da saída."
- 🎬 Tira de debaixo da mesa uma bola de cristal pequena, embrulhada num lenço com estrelas.
- **Madame Oriel** *(normal)*: "A minha bola de cristal. Não mostra o futuro. Mostra o que está escondido à tua volta. É mais útil. E mais honesto."
- **Madame Oriel** *(feliz)*: "Leva-a. Eu já não preciso. O que eu esperava já chegou."

▶ **"Obrigad{o/a}, Oriel."**
▶ **"Isso é tudo mentira."** (só para rir)

- *(obrigado)* **Oriel** *(feliz)*: "Não agradeças. Volta e conta-me o fim. É o único futuro que eu ainda quero ver."
- *(mentira)* **Oriel** *(feliz, a rir)*: "Pronto. Agora sim, és dos meus." *(não perde amizade nesta cena)*

⚙ **Bola de Cristal**: 1 vez por dia mostra no mapa todos os segredos do andar onde estás. Título *Lid{o/a} pelas Estrelas*.

---

## 9. Missões

### R2_12 — O Outro Eu (`andar_maximo >= 19`)
- **Pedir** — **Oriel**: "O lago negro do andar 19 tem um reflexo que se soltou. O teu. Vence-o sem poções. Ele não tem poções. Seria batota."
- **Passo**: vencer o **Reflexo Negro** (guardião do andar 19) **sem usar poções**.
- **Entregar** — **Oriel** *(feliz)*: "Venceste-te a ti. É mais difícil do que parece. Toma: um espelho que devolve feitiços. Para ninguém te vencer a ti." ⚙ **Amuleto do Espelho** · +100

### R9_08 — A Carta da Oriel (6 ❤️, `andar_maximo >= 86`)
- **Passos**: levar a **Carta da Oriel** à **Astrónoma Vega** (Observatório Celeste, andar 86; falas em `docs/dialogos/povoacoes_r09.md`) · trazer a resposta e o **Baralho Celeste**.
- **Entregar** — **Oriel** *(feliz, a chorar)*: "Ela… ela diz que também viu o número. Que não disse nada porque teve medo. E que me perdoa por ter sido corajosa." ⚙ **Baralho Celeste** (as profecias passam a mostrar também os segredos de um andar ao acaso) · +200 (❤️❤️)

### N_ORIEL_3 — A Carta Que Falta (8 ❤️, Cidade Errante desbloqueada)
- **Pedir** — **Oriel**: "A 22.ª carta do meu baralho. Perdi-a num jogo das conchas, na Cidade Errante, há trinta anos. Perdi-a para uma tartaruga. Não perguntes."
- **Passos**: na Cidade Errante, vencer o **jogo das conchas** 3 vezes seguidas (o Troca-Tudo só troca a carta por "uma coisa de outro mundo": qualquer **curiosidade do mundo real** do Tobias, ver `docs/LOJAS.md`) · trazer a **Carta 22**.
- **Entregar** — ver a **cena de 10 ❤️** (se tiveres 10 ❤️); senão: **Oriel**: "Vinte e duas. Obrigada. Guardo-a para o dia certo." · +150

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `oriel_estado_vida` | `vida_pct < 30` | normal | "Vejo sangue no teu futuro. E no teu presente. Vai à Igreja, não precisas de vidente para isso." |
| `oriel_estado_maldito` | `estado(amaldicoado)` | feliz | "Uma maldição! Que bonita. Roxa. Não toques em nada meu." |
| `oriel_estado_cansado` | `estado(cansado)` | normal | "As cartas dizem: cama. As cartas raramente são tão claras." |
| `oriel_ceptico` | escolher "Isso é tudo mentira" fora das cenas | zangado | "Mentira? Então diz-me tu o meu futuro. Não sabes? Pois. Fica calad{o/a}." ⚙ −30 |
| `oriel_comp_kai` | `companheiro(kai)` | feliz | "O rapaz da carta Os Dois. Voltou. Eu disse que voltava. Disse-o a mim, mas disse." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `oriel_serv_abrir` | abrir serviços | normal | "Escolhe. Sorte, segredos ou tartaruga." |
| `oriel_serv_carta_dia` | carta da sorte do dia | feliz | "Saiu-te {carta}. Hoje {bónus}. Amanhã, quem sabe." |
| `oriel_serv_profecia` | profecia | normal | "Vejo… no andar {andar}… {pista}. Mais do que isto, só se me pagares o jantar." |
| `oriel_serv_vagar` | onde está a Cidade Errante | normal | "A tartaruga está no andar {andar}. Fica lá mais {n} dias. Leva algas. Ela gosta de algas." |
| `oriel_serv_nome` | monstro com nome da semana | normal | "Esta semana, {monstro}, no andar {andar}, {condição}. Leva poções. E coragem. Coragem não vendo." |
| `oriel_serv_sortear` | voltar a sortear a Skill Única | surpresa | "Tens a certeza? As estrelas não dão terceiras oportunidades. Nem segundas, normalmente. Hoje estão generosas." |
| `oriel_serv_sem_ouro` | sem ouro | normal | "Prevejo que não tens dinheiro. Acertei. Essa foi de graça." |
| `oriel_serv_fechado` | 2:00–14:00 | — | `[Sistema] A tenda está fechada. Lá dentro, alguém ressona com elegância.` |
