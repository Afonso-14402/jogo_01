# Móveis e decoração

Todos os **móveis** da casa (cerca de 215). Resumo e regras gerais: `docs/ITENS.md`, secção 10. A casa e as suas
melhorias: `docs/CIDADES.md`. Os IDs passam para `dados/itens/moveis.json`.

---

## 1. Regras

| Regra | Valor |
|---|---|
| Onde se fazem | na **Bancada de Carpintaria** da casa (melhoria da casa; o Brom ou o Gizmo ensinam a usá-la) |
| Receitas | as **básicas** sabem-se desde o início; as **de cada região** aprendem-se ao chegar à povoação principal dessa região (1.ª visita) |
| Tempo | os móveis fazem-se na hora (é um minijogo curto de serrar e pregar, opcional: se correr bem, sai em qualidade **Excelente**, que vale +25% e conta mais no Concurso da Casa Mais Bonita) |
| Valor | o **valor** é o que vale para vender (30% nas lojas) e para o Concurso. Os das regiões valem **1,5 × o preço dos materiais** (`docs/LOJAS.md`, secção 1) |
| Efeitos | as **camas** dão um bónus ao acordar (só conta uma: a última em que dormiste). O resto é só bonito (e alguns fazem coisas pequenas: tocam, brilham, mexem-se) |
| Limite | a casa tem espaço para 60 móveis no início; cada melhoria da casa dá mais 30 |

---

## 2. Móveis das regiões (100)

Dez por região: cadeira, mesa, cama, tapete, candeeiro, estante e quatro peças especiais da região.

### 2.1 Região 1 — Floresta

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r01_01` | Cadeira de Tronco | um tronco cortado com encosto de ramos | 3 Carvalho | 36 |
| `movel_r01_02` | Mesa de Carvalho | redonda, com um nó no meio que parece um olho | 5 Carvalho | 60 |
| `movel_r01_03` | Cama de Musgo | colchão de musgo e linho; +5% Estamina ao acordar | 4 Carvalho + 3 Linho Bravo | 84 |
| `movel_r01_04` | Tapete de Folhas | folhas secas cosidas em linho; muda de cor com as estações | 4 Linho Bravo | 48 |
| `movel_r01_05` | Candeeiro de Cogumelo | um Cogumelo Luminoso dentro de um frasco | 1 Carvalho + 1 Seiva Cristalizada | 162 |
| `movel_r01_06` | Estante de Ramos | prateleiras tortas que aguentam tudo | 6 Carvalho | 72 |
| `movel_r01_07` | Baú de Lenhador | como o do Bruno: guarda 20 itens | 4 Carvalho + 1 Lingote de Cobre | 93 |
| `movel_r01_08` | Cabeça de Javali (madeira) | esculpida pelo Velho Cass; não é troféu, é "homenagem" | 3 Carvalho + 1 Couro de Javali | 48 |
| `movel_r01_09` | Casa de Fadas | uma casinha pequenina com luzes; à noite ouve-se rir | 2 Carvalho + 2 Seiva Cristalizada | 324 |
| `movel_r01_10` | Colmeia de Parede | decoração; às vezes aparece uma abelha a passear | 3 Carvalho + 1 Linho Bravo | 48 |

### 2.2 Região 2 — Cavernas

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r02_01` | Banco de Fungo | um cogumelo gigante cortado; fofo | 3 Fungo-Lenho | 144 |
| `movel_r02_02` | Mesa de Vagoneta | uma vagoneta virada ao contrário | 2 Fungo-Lenho + 2 Lingote de Ferro | 456 |
| `movel_r02_03` | Cama de Seda | seda de aranha: macia e fresca; +5% HP ao acordar | 3 Fungo-Lenho + 4 Seda de Aranha | 336 |
| `movel_r02_04` | Tapete de Toupeira | castanho e quente | 4 Couro de Toupeira | 192 |
| `movel_r02_05` | Lanterna de Mineiro | a luz não se apaga com o vento | 1 Lingote de Ferro + 1 Cristal de Gruta | 780 |
| `movel_r02_06` | Prateleira de Escoras | madeira velha das minas, com marcas de picareta | 5 Fungo-Lenho | 240 |
| `movel_r02_07` | Bigorna Pequena | decoração anã; o Brom aprova | 4 Lingote de Ferro | 720 |
| `movel_r02_08` | Cristal de Gruta Grande | canta baixinho à noite | 4 Cristal de Gruta | 2 400 |
| `movel_r02_09` | Mapa das Minas | emoldurado; tem um "X" a lápis | 1 Fungo-Lenho + 2 Seda de Aranha | 144 |
| `movel_r02_10` | Estátua de Gnomo Fungoide | sorri sempre. Sempre | 4 Fungo-Lenho + 1 Cristal de Gruta | 792 |

### 2.3 Região 3 — Pântano

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r03_01` | Cadeira de Liana | baloiça um bocadinho | 2 Mangue + 2 Fibra de Liana | 432 |
| `movel_r03_02` | Mesa de Mangue | raízes como pernas | 5 Mangue | 540 |
| `movel_r03_03` | Rede de Dormir | entre dois postes; +5% Estamina ao acordar | 5 Fibra de Liana + 2 Mangue | 756 |
| `movel_r03_04` | Tapete de Crocodilo | escamas verdes; ninguém pisa a cabeça | 4 Pele de Crocodilo | 432 |
| `movel_r03_05` | Lanterna de Âmbar | luz cor de mel com um mosquito lá dentro | 2 Âmbar do Pântano | 2 700 |
| `movel_r03_06` | Estante de Bambu | leve e torta | 5 Mangue | 540 |
| `movel_r03_07` | Tambor Sssar | tocá-lo faz o animal de estimação dançar | 2 Pele de Crocodilo + 2 Mangue | 432 |
| `movel_r03_08` | Ídolo de Jade (cópia) | uma cópia do Ídolo do Fausto | 2 Âmbar do Pântano + 1 Lingote de Aço | 3 105 |
| `movel_r03_09` | Vaso de Lírio do Pântano | floresce de noite | 1 Mangue + 1 Âmbar do Pântano | 1 458 |
| `movel_r03_10` | Coaxófono | um instrumento do Coro dos Sapos; coaxa quando lhe tocas | 2 Mangue + 1 Pele de Crocodilo | 324 |

### 2.4 Região 4 — Deserto

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r04_01` | Almofadão de Zahra | vermelho e dourado | 3 Ligadura Antiga + 1 Couro de Chacal | 768 |
| `movel_r04_02` | Mesa Baixa de Acácia | para chá de menta | 4 Acácia | 768 |
| `movel_r04_03` | Cama de Dossel | com véus; +5% MP ao acordar | 4 Acácia + 4 Ligadura Antiga | 1 536 |
| `movel_r04_04` | Tapete do Deserto | padrões de dunas; voa? Não. Quase | 5 Ligadura Antiga | 960 |
| `movel_r04_05` | Lâmpada de Hakim | não tem Djinn. Acho | 1 Lingote de Prata + 1 Vidro Solar | 3 120 |
| `movel_r04_06` | Estante de Pergaminhos | cheia de rolos (vazios) | 5 Acácia + 1 Ligadura Antiga | 1 152 |
| `movel_r04_07` | Ampulheta de Vidro Solar | a areia é dourada | 2 Vidro Solar + 1 Acácia | 4 992 |
| `movel_r04_08` | Sarcófago Pequeno | decoração; abre e tem um gato de pedra | 3 Acácia + 2 Lingote de Prata | 2 016 |
| `movel_r04_09` | Cacto em Vaso | não precisa de água; não gosta de abraços | 1 Acácia | 192 |
| `movel_r04_10` | Mapa das Estrelas Pregadas | o céu pintado de Zahra, com os buracos escuros | 2 Ligadura Antiga + 1 Vidro Solar | 2 784 |

### 2.5 Região 5 — Gelo

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r05_01` | Cadeira de Pinheiro | cheira a Natal | 3 Pinheiro Nevado | 900 |
| `movel_r05_02` | Mesa de Tronco Nevado | com geada que não derrete | 5 Pinheiro Nevado | 1 500 |
| `movel_r05_03` | Cama de Peles | pele de urso e lã; +5% HP ao acordar; imune a Frio a dormir | 3 Pele de Urso Polar + 3 Lã de Mamute | 1 800 |
| `movel_r05_04` | Tapete de Lã de Mamute | gigante e quente | 5 Lã de Mamute | 1 500 |
| `movel_r05_05` | Lareira de Gelo | fogo azul que aquece e não derrete | 2 Barra de Gelo Eterno + 1 Lágrima de Aurora | 6 000 |
| `movel_r05_06` | Estante de Gelo Eterno | transparente | 3 Barra de Gelo Eterno | 3 375 |
| `movel_r05_07` | Trenó de Parede | decoração dos caçadores | 4 Pinheiro Nevado + 1 Pele de Urso Polar | 1 500 |
| `movel_r05_08` | Boneco de Neve | nunca derrete; muda de chapéu nos festivais | 1 Lágrima de Aurora | 3 750 |
| `movel_r05_09` | Lanterna de Aurora | luzes verdes e roxas no teto | 3 Lágrima de Aurora | 11 250 |
| `movel_r05_10` | Corneta dos Caçadores | tocá-la chama o animal de estimação | 1 Pinheiro Nevado + 1 Pele de Urso Polar + 1 Barra de Gelo Eterno | 1 725 |

### 2.6 Região 6 — Oceano

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r06_01` | Cadeira de Concha | uma concha gigante aberta | 2 Pérola + 1 Madeira de Naufrágio | 11 232 |
| `movel_r06_02` | Mesa de Naufrágio | tábuas de navio com pregos velhos | 5 Madeira de Naufrágio | 2 160 |
| `movel_r06_03` | Cama de Coral | rosa e branca; +5% MP ao acordar | 2 Barra de Coral Abissal + 3 Fio de Alga-Prata | 4 536 |
| `movel_r06_04` | Tapete de Algas | verde-prata; nunca seca, nunca molha | 5 Fio de Alga-Prata | 2 160 |
| `movel_r06_05` | Candeeiro de Água-Viva | uma água-viva num aquário, a brilhar | 2 Pérola | 10 800 |
| `movel_r06_06` | Estante de Navio | com redes e boias | 4 Madeira de Naufrágio + 1 Fio de Alga-Prata | 2 160 |
| `movel_r06_07` | Leme de Parede | do Barba-Lodo? Não. Parecido | 4 Madeira de Naufrágio | 1 728 |
| `movel_r06_08` | Aquário Pequeno | põe lá um peixe que pescaste | 2 Pérola + 2 Madeira de Naufrágio | 11 664 |
| `movel_r06_09` | Âncora Decorativa | pesadíssima | 3 Barra de Coral Abissal | 4 860 |
| `movel_r06_10` | Concha Que Canta | encostar ao ouvido: ouve-se Coralina | 1 Pérola | 5 400 |

### 2.7 Região 7 — Vulcão

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r07_01` | Cadeira de Obsidiana | preta e brilhante; fresca, estranhamente | 2 Barra de Obsidiana | 4 410 |
| `movel_r07_02` | Mesa de Lenho-Brasa | quente ao toque; aquece o chá | 5 Lenho-Brasa | 2 940 |
| `movel_r07_03` | Cama Ignífuga | seda ignífuga; +5% Estamina ao acordar | 4 Seda Ignífuga + 2 Lenho-Brasa | 3 528 |
| `movel_r07_04` | Tapete de Salamandra | vermelho com manchas amarelas | 4 Couro de Salamandra | 2 352 |
| `movel_r07_05` | Candeeiro de Lava | lava num vidro que sobe e desce | 2 Cristal de Magma + 1 Barra de Obsidiana | 16 905 |
| `movel_r07_06` | Estante da Forja | prateleiras com ferramentas anãs | 2 Barra de Obsidiana + 3 Lenho-Brasa | 6 174 |
| `movel_r07_07` | Bigorna de Obsidiana | a do Ragnar é maior | 5 Barra de Obsidiana | 11 025 |
| `movel_r07_08` | Géiser de Mesa | faz "fuu" de hora a hora | 1 Cristal de Magma + 1 Barra de Obsidiana | 9 555 |
| `movel_r07_09` | Pintura de Cinza | das termas; diferente cada vez que a fazes | 2 Seda Ignífuga + 1 Cristal de Magma | 8 526 |
| `movel_r07_10` | Toalha das Termas | pendurada; cheira a enxofre e a descanso | 2 Seda Ignífuga | 1 176 |

### 2.8 Região 8 — Reino Assombrado

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r08_01` | Cadeirão de Ébano | encosto alto, gótico | 4 Ébano Morto + 1 Asa de Gárgula | 3 840 |
| `movel_r08_02` | Mesa de Banquete | comprida; cabem dez fantasmas | 8 Ébano Morto | 6 144 |
| `movel_r08_03` | Cama com Dossel Negro | cortinas de fio espectral; +5% MP ao acordar | 4 Ébano Morto + 4 Fio Espectral | 6 144 |
| `movel_r08_04` | Tapete Real | vermelho com uma coroa bordada | 5 Fio Espectral | 3 840 |
| `movel_r08_05` | Candelabro | velas que nunca acabam | 2 Lingote de Mitril + 1 Lágrima de Fantasma | 15 360 |
| `movel_r08_06` | Estante da Biblioteca | com livros que às vezes mudam de sítio | 6 Ébano Morto | 4 608 |
| `movel_r08_07` | Órgão Pequeno | tocável (minijogo de ritmo curto) | 5 Ébano Morto + 2 Lingote de Mitril | 9 600 |
| `movel_r08_08` | Vitral | luz colorida no chão de manhã | 3 Lágrima de Fantasma | 28 800 |
| `movel_r08_09` | Armadura Vazia | decoração. Vazia. Garantido | 4 Lingote de Mitril | 11 520 |
| `movel_r08_10` | Caixa de Música Fantasma | toca a música da Cidade Fantasma | 1 Ébano Morto + 2 Lágrima de Fantasma | 19 968 |

### 2.9 Região 9 — Céu

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r09_01` | Nuvem-Sofá | fofo; afunda-se e volta | 5 Fio de Nuvem | 4 860 |
| `movel_r09_02` | Mesa de Madeira-Nuvem | flutua um palmo acima do chão | 5 Madeira-Nuvem | 4 860 |
| `movel_r09_03` | Cama de Nuvem | +5% a tudo durante a manhã | 5 Fio de Nuvem + 2 Madeira-Nuvem | 6 804 |
| `movel_r09_04` | Tapete de Penas | penas brancas e douradas | 3 Fio de Nuvem + 1 Pele de Pássaro-Trovão | 3 888 |
| `movel_r09_05` | Lanterna Celeste | como as do Festival; sobe e desce devagar | 1 Fio de Nuvem + 1 Cristal Celeste | 13 122 |
| `movel_r09_06` | Estante Flutuante | prateleiras soltas no ar | 5 Madeira-Nuvem + 1 Cristal Celeste | 17 010 |
| `movel_r09_07` | Cata-Vento dos Monges | roda sozinho sem vento | 2 Madeira-Nuvem + 1 Lingote de Oricalco | 5 589 |
| `movel_r09_08` | Globo Celeste | as constelações do 86 a girar | 2 Lingote de Oricalco + 2 Cristal Celeste | 31 590 |
| `movel_r09_09` | Balão Pequeno | um balão do Nimbo do tamanho de uma cadeira | 3 Fio de Nuvem + 2 Madeira-Nuvem | 4 860 |
| `movel_r09_10` | Harpa dos Alados | tocável (som de vento) | 3 Madeira-Nuvem + 2 Fio de Nuvem | 4 860 |

### 2.10 Região 10 — Abismo

| ID | Móvel | Como é | Receita | Valor |
|---|---|---|---|---|
| `movel_r10_01` | Cadeira do Vazio | preta, com estrelas dentro | 2 Pele do Vazio + 1 Madeira do Tempo | 3 600 |
| `movel_r10_02` | Mesa do Tempo | a madeira muda de cor ao longo do dia | 5 Madeira do Tempo | 6 000 |
| `movel_r10_03` | Cama Estelar | +5% a tudo de manhã; sonhos com o prado | 4 Fio de Luz Estelar + 1 Lingote Estelar | 9 300 |
| `movel_r10_04` | Tapete de Constelações | o céu do 92 no chão | 5 Fio de Luz Estelar | 6 000 |
| `movel_r10_05` | Âncora de Luz | a estrelinha que dorme; acorda quando chegas a casa | 1 Lingote Estelar + 1 Núcleo do Vazio | 19 500 |
| `movel_r10_06` | Estante do Mundo | um livro de cada região (decoração) | 6 Madeira do Tempo | 7 200 |
| `movel_r10_07` | Relógio Estelar | os ponteiros andam para trás ao domingo | 2 Madeira do Tempo + 2 Lingote Estelar | 11 400 |
| `movel_r10_08` | Espelho de Moldura Dourada | mostra-te com a arma na outra mão | 1 Núcleo do Vazio + 1 Lingote Estelar | 19 500 |
| `movel_r10_09` | Janela Azul de Parede | uma janela do Sistema pequenina que diz "Bom dia." | 2 Núcleo do Vazio | 30 000 |
| `movel_r10_10` | Cachecol da Praça (pedaço) | um metro do cachecol da Mãe Dois, emoldurado | 3 Fio de Luz Estelar | 3 600 |

---

## 3. Básicos (30)

Vendem-se no **Tobias** (Mercado). Também se fazem na bancada com Carvalho (metade do preço em materiais).

| ID | Móvel | Preço | ID | Móvel | Preço |
|---|---|---|---|---|---|
| `movel_b01` | Cama simples | 300 | `movel_b16` | Cortinas (4 cores) | 80 |
| `movel_b02` | Cama de casal | 800 | `movel_b17` | Espelho de parede | 250 |
| `movel_b03` | Mesa de cozinha | 200 | `movel_b18` | Relógio de parede | 300 |
| `movel_b04` | Mesa de cabeceira | 120 | `movel_b19` | Quadro de paisagem | 200 |
| `movel_b05` | Cadeira de madeira | 80 | `movel_b20` | Vaso com flores | 60 |
| `movel_b06` | Banco | 50 | `movel_b21` | Planta grande | 150 |
| `movel_b07` | Sofá | 700 | `movel_b22` | Lareira de pedra | 1 200 |
| `movel_b08` | Poltrona | 400 | `movel_b23` | Fogão de cozinha (permite cozinhar em casa) | 1 500 |
| `movel_b09` | Tapete redondo (4 cores) | 150 | `movel_b24` | Armário de cozinha | 350 |
| `movel_b10` | Tapete comprido (4 cores) | 200 | `movel_b25` | Baú (guarda 30 itens) | 400 |
| `movel_b11` | Candeeiro de pé | 180 | `movel_b26` | Cabide | 60 |
| `movel_b12` | Vela | 20 | `movel_b27` | Caixa de correio (recebes as cartas dos NPCs) | 100 |
| `movel_b13` | Estante pequena | 250 | `movel_b28` | Gira-discos (toca as músicas que tens) | 2 000 |
| `movel_b14` | Estante grande | 500 | `movel_b29` | Bancada de Carpintaria | 1 000 |
| `movel_b15` | Secretária | 300 | `movel_b30` | Placa com o teu nome | 50 |

---

## 4. Troféus (40)

Ganham-se na **1.ª vitória**. Não se vendem.

### 4.1 Os 20 bosses
Os troféus de cada boss estão na ficha dele (`docs/BOSSES.md`): Cabeça do Javali-Rei · Ramo do Ent · Teia Dourada ·
Fragmento do Núcleo · Coroa de Pedra da Serpente · Três Dentes da Hidra · Carapaça Imperial · Máscara do Faraó · Colar
do Yeti · Escama de Dragão de Gelo · Chapéu do Capitão · Escama do Leviatã · Bigorna Infernal · Pedra-Coração do Titã ·
Óculos do Lich · A Coroa do Reino · Pena Real do Grifo · Asa do Serafim · Relógio Parado · A Primeira Janela.
Os **Bosses Despertos** (pós-jogo) dão uma **moldura azul** para o troféu do mesmo boss.

### 4.2 Os 20 monstros com nome
Cada um dá um **cartaz de caça emoldurado** (o cartaz da Guilda, com um carimbo vermelho "CAÇADO" e a assinatura da
Freya). ID `trofeu_cartaz_{monstro}`. O cartaz tem um desenho diferente em cada um (desenhado pela Lyra: são maus,
e por isso mesmo são bons):

| Região | Cartazes |
|---|---|
| 1 | Slime Rei · Lobo Cicatriz |
| 2 | Rei Goblin Gruk · Toupeira Dourada |
| 3 | Mãe-Crocodilo Mandíbula · Rei Macaco Bobo |
| 4 | Sultão Bandido Kasim · Verme Colosso |
| 5 | Presa-Branca · Mamute Ancião Tundra (se o acalmaste, o carimbo diz "AMIGO", em verde) |
| 6 | Caranguejo Rei Pinça-de-Ouro · Barba-Lodo |
| 7 | Tricéfalo · Golem Forjado Nº 7 |
| 8 | Condessa Sangria · O Jardineiro |
| 9 | Valquíria Sigrun (o carimbo diz "DUELO") · Tempestade Viva |
| 10 | Devorador Ancestral · O Jogador Sem Número (o carimbo diz "OUVIDO", e o nome Simão está escrito à mão) |

---

## 5. Decorações de missões (25)

| Decoração | De onde vem |
|---|---|
| Remo Dourado | região 6 (`docs/textos/itens.md`) |
| Pinturas de Cinza | R7 (termas) |
| Fotografias dos andares | Gil (R7_07): uma por região |
| Machado do Gorvan | C8-04 |
| Cálice de Prata | andar 79 |
| Espada Benta | andar 77 |
| Esculturas de Nuvem (×3) | R9_13 |
| Telescópio | R9_06 |
| Sino de Vento | R9_14 |
| Espelho Mágico | R10_04 |
| A Crónica da Subida | R10_05 |
| Disco "Casa" | R10_14 |
| Museu da Subida | os 9 objetos do andar 94 |
| Objetos do Mundo Real | Mercado das Memórias (andar 97) |
| Caderno do Aren | depois de um final |
| Machado da Equipa | 10 ❤️ Gorvan |
| Insígnia da Capitã (cópia de parede) | 10 ❤️ Freya |
| Retrato do Herói (pintado pelo Lucien… mal) | 10 ❤️ Lucien |
| Mapa de Ascendia do Aldric | 10 ❤️ Aldric |
| Vestido de Alvorada (manequim) | 10 ❤️ Elva |
| Árvore de trigo dourado (vaso) | 10 ❤️ Hana |
| Maquete da torre do Gizmo (com luzes) | 10 ❤️ Gizmo |
| Livro de receitas da Dona Marta | 10 ❤️ Marta |
| Baralho da Oriel (moldura) | 10 ❤️ Oriel |
| Estandarte da Guarda | Grande Invasão (`docs/textos/eventos.md`) |

---

## 6. Festivais (20)

| Festival | Decorações (compram-se na banca do festival ou ganham-se nos jogos) |
|---|---|
| Festa das Flores (F_01) | coroa de flores de parede · arco de flores · vaso de tulipas de Ascendia · bandeirinhas de primavera · prémio "Flor Mais Bonita" (só ganhando) |
| Festival da Pesca (F_02) | troféu do maior peixe (com o teu peixe) · rede decorativa · cana de bambu cruzada · prémio "Rei da Pesca" (só ganhando) |
| Noite dos Espíritos (F_03) | lanterna de abóbora (3 caras) · fantasma de pano · teia de festa · vela negra · prémio "Melhor Lanterna" (só ganhando) |
| Festival da Estrela (F_04) | árvore da estrela · estrela de palha · meias penduradas · fogo de artifício de parede · prémio "Amigo Secreto" (o presente que recebeste, emoldurado) |
| Noite das Lanternas (F_07) | lanterna do rio (com o nome de quem escolheres) |

---

## 7. Coleções (automáticas)

Não se fazem: aparecem na casa (melhorias da casa) quando completas uma coleção (`docs/ATIVIDADES.md`):
**Parede das Armas** (mostra as armas únicas que tens) · **Aquário** (os peixes raros e lendários) · **Museu** (os
objetos de lore) · **Estante do Diário** (as 100 páginas, numa caixa de vidro, com a 68 a lápis e as azuis a brilhar).
