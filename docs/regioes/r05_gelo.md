# Região 5 — Gelo (andares 41–50)

> Estrutura igual às outras regiões. Bosses grandes (Yeti Ancião e Dragão de Gelo) em `docs/BOSSES.md`.
> No andar 46 encontra-se o **diário da antiga equipa do Mestre Gorvan** (ver `docs/HISTORIA.md`).

---

## 1. Identidade

| | |
|---|---|
| Tema | O norte gelado de um mundo engolido: tundra, pinhais com neve, lagos congelados, glaciares, auroras, um castelo de gelo |
| Sensação | Silêncio, frio, beleza, solidão; o calor das aldeias como refúgio |
| Material das armas | **Gelo Eterno** (tier 5) — um gelo que nunca derrete |
| Monstros fracos a | **Fogo** |
| Cores principais | brancos `#ffffff` `#c7dcd0`, azuis `#8fd3ff` `#4d9be6` `#4d65b4`, aurora `#30e1b9` `#a884f3`, fogueiras `#f79617` |
| Luz | luz branca e fria refletida pela neve; dias curtos; noites com aurora verde e roxa; fogueiras laranja |
| Clima | Neve 50% · Céu limpo 25% · Nevão 20% · Nevoeiro gelado 5% |
| Música | `tundra_silencio`, `pinhal_aldeia`, `aurora`, `yeti`, `dragao_gelo` |
| Níveis | monstros 41–51; mini-boss 47; boss 53 |
| Mecânica da região | **Temperatura** (ver abaixo). **Neve funda**: andas 30% mais devagar (Raquetes de Neve anulam). **Gelo escorregadio**: demoras a travar (Botas de Pico anulam). **Avalanches** em encostas |
| Animal de estimação | Pinguim |
| Montada | **Lobo de Gelo** |

### Temperatura
- Barra de **Temperatura** de 0 a 100 (aparece só nesta região).
- Ao ar livre desce **1 ponto a cada 3 s**; com nevão **1 por segundo**; dentro de água gelada **10 por segundo**.
- Perto de uma **fogueira**, lareira ou sauna sobe **5 por segundo**.
- Abaixo de **50**: −10% de velocidade. Abaixo de **25**: ganhas 1 Frio a cada 10 s. Em **0**: Congelado 1,5 s a cada 10 s e −1% HP por segundo.
- **Casaco de Lã** ou **Capa de Presa-Branca**: a temperatura desce metade. **Comida quente** (Sopa, Chá Quente): +40. **Pedra Quente** (item): não desce durante 5 min.

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Fragmento de Gelo Eterno | blocos azuis que nunca derretem (44, 47, 49) | Picareta de Prata+ | Barra de Gelo Eterno (3 fragmentos + 1 Carvão para aquecer o molde) |
| Pinheiro Nevado | 42, 46 | Machado | **madeira** da região |
| Pele de Urso Polar | Urso Polar | drop | **couro** da região, casacos |
| Lã de Mamute | Mamute Jovem | drop | **fio** da região |
| Lágrima de Aurora | cristais que só aparecem com aurora (48) | Picareta | **cristal** da região |
| Safira | grutas azuis (44) | Picareta | gema de **Gelo** |
| Flor-de-Neve | 41, 48 | à mão | Poção Quente, presentes |
| Musgo Ártico | 41, 47 | à mão | poções |
| Bagas de Inverno | arbustos (42, 46) | à mão | Chá Quente, acalmar o Mamute |
| Marfim | Mamute, Morsa | drop | joalharia, decoração |
| Pena Gélida | Harpia Gélida | drop | flechas, chapéus |
| Brasa Eterna | fogueira do iglu secreto (41) | missão | receita Pedra Quente |

---

## 3. Monstros

### 3.1 Lobo de Gelo
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, alcateia de 3–5 |
| Andares | 41, 42, 47, 48 |
| Comportamento | Como os lobos da floresta, mas mordem com gelo. Atacam em ondas: dois à frente, dois pelos lados |
| Ataques | **Mordida Gelada**: Frio (aviso 0,35 s) · **Investida** de 6 m (aviso 0,6 s) · **Sopro** (só o líder: cone de Frio) |
| Fraco / Imune | Fogo / Gelo |
| Drops | Pele de Lobo de Gelo 55% · Presa Gelada 25% |
| Elite | **Lobo Aurora**: pelo que muda de cor; teletransporta-se |
| Animações | parado (4), correr (6), mordida (4), sopro (4), uivo (4), dano (1), morrer (4) |

### 3.2 Urso Polar
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque**, sozinho |
| Andares | 41, 43, 45, 46 |
| Comportamento | Pesca nos buracos do gelo; ataca se chegares perto. Levanta-se nas patas de trás antes dos golpes fortes |
| Ataques | **Patada** (×1,5; aviso 0,6 s) · **Abraço**: agarra-te 2 s · **Rugido** de pé: Medo 1,5 s (aviso 1 s) |
| Fraco / Resiste | Fogo / Gelo |
| Drops | Pele de Urso Polar 60% · Garra de Urso 25% · Carne 50% |
| Elite | **Urso de Gelo Azul**: carapaça de gelo nas costas (Fogo derrete-a) |
| Animações | pescar (4), parado (4), mover (6), patada (4), abraço (4), rugido de pé (6), dano (1), morrer (5) |

### 3.3 Golem de Gelo
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 44, 47, 49, 50 |
| Comportamento | Bloco de gelo eterno com um núcleo azul. Ao morrer **explode** em estilhaços |
| Ataques | **Murro** (×1,4) · **Estacas de Gelo**: linha de estacas a sair do chão (aviso 0,8 s: rachas azuis) · **Explosão** ao morrer: área de Frio 3 m |
| Fraco / Imune | Fogo, Martelo / Gelo, Veneno |
| Drops | Fragmento de Gelo Eterno 40% · Núcleo Gelado 15% |
| Elite | **Golem de Gelo Negro**: as estacas congelam logo |
| Animações | parado (4), mover (4), murro (4), estacas (5), dano (1), explodir (5) |

### 3.4 Espírito da Neve
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago + Voador** |
| Andares | 41, 42, 48 |
| Comportamento | Dança no ar com flocos de neve; some-se nos nevões |
| Ataques | **Bola de Neve**: Frio · **Nevão**: área de 4 m que dá Frio enquanto lá estás · **Desaparecer** |
| Fraco / Imune | Fogo, Luz / Gelo |
| Drops | Essência de Neve 50% · Lágrima de Aurora 5% |
| Elite | **Espírito do Nevão**: o nevão segue-te |
| Animações | flutuar (4), atacar (4), nevão (4), desaparecer (4), dano (1), morrer (4) |

### 3.5 Harpia Gélida
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Voador**, 2–3 |
| Andares | 43, 47, 49 |
| Comportamento | Voa em círculos alto e mergulha. Quando uma grita, vêm as outras |
| Ataques | **Garras** (mergulho; aviso 0,5 s) · **Penas de Gelo**: 3 projéteis · **Grito**: Frio em área e chama outras harpias |
| Fraco / Resiste | Fogo, Raio / Gelo |
| Drops | Pena Gélida 50% · Garra de Harpia 20% |
| Elite | **Harpia Rainha**: penas de gelo em espiral |
| Animações | voar (4), mergulho (4), atirar penas (4), grito (4), dano (1), morrer (4) |

### 3.6 Caçador Congelado
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal** (morto-vivo), aos pares |
| Andares | 42, 46, 49 |
| Comportamento | Caçadores da aldeia que morreram no gelo e "continuam a caçar". Põem armadilhas e disparam de longe |
| Ataques | **Flecha de Gelo**: Frio · **Lança** · **Armadilha de Urso**: prende-te 2 s (aviso: brilho no chão) |
| Fraco / Imune | Fogo, Luz / Gelo, Veneno |
| Drops | Pele Velha 40% · Flechas 30% · **Diário de Caçador** 10% (lore e missão R5_15) |
| Elite | **Caçador-Chefe Congelado**: chama 2 Lobos de Gelo |
| Animações | parado (4), mover (6), arco (4), lança (4), armadilha (4), dano (1), morrer (5: parte-se como gelo) |

### 3.7 Pinguim Guerreiro
| | |
|---|---|
| Tamanho | 32×32 (pequenos, ~18 px de altura) |
| Tipo | **Fraco**, bandos de 3–6 |
| Andares | 43, 44, 45 |
| Comportamento | Engraçados e corajosos: capacetes de concha e lanças de gelo. **Deslizam de barriga** no gelo |
| Ataques | **Deslizar**: investida longa em linha (×1,2; aviso 0,5 s: deitam-se) · **Bicada** · **Bola de Neve** |
| Fraco / Resiste | Fogo / Gelo |
| Drops | Pena de Pinguim 50% · Peixe 30% |
| Elite | **Pinguim Imperador**: coroa; organiza o bando em formação |
| Animações | parado (4: bamboleia), mover (4), deslizar (4), bicada (4), atirar (4), dano (1), morrer (4) |

### 3.8 Mamute Jovem
| | |
|---|---|
| Tamanho | 64×64 |
| Tipo | **Tanque**, manadas de 2–4 **pacíficas** (só atacam se as provocares) |
| Andares | 41, 47, 48 |
| Comportamento | Pastam musgo debaixo da neve. Se atacares um, a manada toda carrega |
| Ataques | **Tromba**: empurra muito · **Carga** de 10 m (×1,7; aviso 1 s: barrita) · **Pisotear**: área (aviso 0,8 s) |
| Fraco / Resiste | Fogo / Gelo, Físico (−10%) |
| Drops | Lã de Mamute 55% · Marfim 20% · Carne 50% |
| Elite | **Mamute Ferido**: furioso, ataca à vista |
| Animações | pastar (4), parado (4), mover (6), tromba (4), carga (4), pisotear (5), dano (1), morrer (6) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Presa-Branca** | andares 41, 42, 48, noites de nevão, 5% | lobo branco enorme (64×64) com cicatrizes azuis que brilham | Uivo chama a alcateia · sopro gelado em cone · some-se no nevão | **Capa de Presa-Branca** (a temperatura desce metade) · **Cria de Presa-Branca** (1.ª vez: missão R5_07 → montada) |
| **Mamute Ancião Tundra** | andares 41, 47, 3% | mamute gigante (128×128) com musgo e pássaros nas costas | **Pacífico**. Se o atacares: tremores de terra, carga que atravessa o andar | Se o **acalmares** (missão R5_11): Lã Ancestral ×5 e título *Amigo dos Gigantes*. Se o matares: Marfim Ancestral |

---

## 5. Os andares

### Andar 41 — Tundra Gelada
| | |
|---|---|
| Tamanho / Nível | 280×280 m · nível 41 |
| Bioma | Planície branca sem fim, vento a levantar neve, pedras altas como dentes, uma costa gelada com morsas, mamutes ao longe |
| Zonas | **Planície Branca** · **Terra da Manada** · **Pedras de Vento** · **Costa Gelada** |
| Mecânica especial | **Temperatura** começa aqui. **Neve funda**. **Vento**: rajadas que empurram e baixam a temperatura |
| Monstros | Lobo de Gelo, Urso Polar, Espírito da Neve, Mamute Jovem |
| Recursos | Flor-de-Neve, Musgo Ártico, Pinheiro (poucos), Fragmento de Gelo (raro) |
| Guardião | **Morsa Gigante** (na Costa Gelada) |
| Segredo | Um **iglu escondido** entre as Pedras de Vento com uma **fogueira que nunca apaga** (ponto de calor) e um baú de ouro |
| Puzzle | **Porta de Gelo**: acender 4 fogueiras de pedra à volta derrete a porta de uma gruta |
| Página de lore 41 | *"O frio aqui não é só frio. É esquecimento. Já não me lembro da cara da minha mãe."* |
| Desafios | Atravessar a planície sem deixar a temperatura passar de 25 · Não atacar nenhum mamute |
| Peças especiais | pedra-dente alta, iglu, fogueira de pedra, banco de neve, costa de gelo |

### Andar 42 — Pinhal Nevado
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 42 |
| Bioma | Pinhal denso coberto de neve, rio meio gelado, uma aldeia de casas de troncos com fumo nas chaminés |
| Zonas | **Pinhal** · **Pinhal-do-Norte** (povoação) · **Serração Gelada** · **Lago das Saunas** |
| Mecânica especial | **Neve nos pinheiros**: bater num tronco faz cair a neve (soterra inimigos por baixo ou revela itens). **Trenó de cães** (depois da missão R5_04) |
| Monstros | Lobo de Gelo, Espírito da Neve, Caçador Congelado, Urso Polar |
| Recursos | **Pinheiro Nevado**, Bagas de Inverno, Flor-de-Neve, peixes |
| Povoação | **Pinhal-do-Norte** (secção 7.1) |
| Guardião | **Alce Fantasma** |
| Segredo | Um pinheiro dourado: bater-lhe faz cair um **Ninho de Gaio** com uma gema |
| Puzzle | **Troncos no rio**: empurrar troncos para fazer uma ponte até à ilha da serração |
| Página de lore 42 | *"Nesta aldeia ninguém sabe o que é uma janela azul. São felizes. Fiquei uma semana. Depois a janela mandou-me subir."* |
| Desafios | Soterrar 5 inimigos com neve · Usar a sauna com a temperatura em 0 |
| Peças especiais | casa de troncos, sauna, salão comunal, pinheiro com neve, trenó |

### Andar 43 — Lago Congelado
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 43 |
| Bioma | Um lago enorme todo congelado, liso e azul, com buracos de pesca, uma ilha com um farol e zonas de gelo fino |
| Zonas | **Superfície Lisa** · **Buracos de Pesca** · **Ilha do Farol** · **Gelo Fino** |
| Mecânica especial | **Gelo escorregadio**. **Gelo fino**: racha se ficares parado 1 s (cais na água: temperatura −30). **Pesca no gelo** |
| Monstros | Pinguim Guerreiro, Harpia Gélida, Urso Polar |
| Recursos | peixes, Pena de Pinguim, Fragmento de Gelo |
| Guardião | **Kraken do Gelo** |
| Segredo | O **ninho de pinguins** atrás do farol: missão R5_03 |
| Puzzle | **Farol**: acender o farol (subir a escada em espiral) mostra o caminho seguro pelo gelo fino |
| Página de lore 43 | *"Debaixo do gelo vi luzes a mexer. O lago sonha."* |
| Desafios | Atravessar o Gelo Fino sem cair · Pescar 5 peixes diferentes |
| Peças especiais | gelo liso, gelo fino rachado, buraco de pesca, farol, ninho de pinguins |

### Andar 44 — Grutas de Gelo Azul
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 44 |
| Bioma | Grutas de gelo transparente azul onde a luz passa; criaturas e tesouros presos dentro das paredes; uma cascata congelada |
| Zonas | **Túneis Azuis** · **Sala dos Congelados** · **Cascata Congelada** · **Câmara Prismática** |
| Mecânica especial | **Derreter gelo** com fogo (tocha, feitiço, arma de fogo) abre caminhos e liberta o que está preso (às vezes um tesouro, às vezes um monstro!) |
| Monstros | Golem de Gelo, Pinguim Guerreiro, Espírito da Neve |
| Recursos | **Safira**, Fragmento de Gelo Eterno, Cristal de Gruta |
| Guardião | **Coração de Cristal Azul** |
| Segredo | Na Sala dos Congelados há um **aventureiro congelado vivo**: derretê-lo dá uma missão de resgate (vai viver para Ascendia) |
| Puzzle | **Luz Prismática**: derreter as paredes certas para levar a luz até 3 cristais |
| Página de lore 44 | *"Há pessoas presas no gelo. Algumas ainda pestanejam."* |
| Desafios | Libertar 10 coisas presas no gelo · Atravessar sem derreter nada |
| Peças especiais | parede de gelo transparente (com coisa presa), cascata congelada, cristal azul gigante, túnel de gelo |

### Andar 45 — Covil do Yeti 💀
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 45 |
| Bioma | Encosta de montanha com neve profunda, ossos de presas, pegadas enormes, uma gruta escura no topo |
| Zonas | **Encosta das Avalanches** · **Ossos de Presas** · **Gruta do Yeti** (arena) |
| Mecânica especial | **Avalanches**: rolam pela encosta de 30 em 30 s (abrigos de pedra ou fugir para os lados) |
| Monstros | Urso Polar, Pinguim Guerreiro, Lobo de Gelo |
| Recursos | Fragmento de Gelo, Marfim, Osso |
| Mini-boss | **Yeti Ancião** (ver `docs/BOSSES.md`) → arma única **Punhos do Yeti** (manoplas) |
| Segredo | Na gruta, atrás do Yeti, há os **brinquedos** que o Yeti guardava (uma boneca de um Jogador antigo — lore e presente para a Mia) |
| Página de lore 45 | *"O Yeti guardava coisas de Jogadores mortos. Não para as comer. Para se lembrar deles."* |
| Desafios | Subir sem ser apanhado por uma avalanche · Vencer o Yeti sem Poção Quente |
| Peças especiais | abrigo de pedra, pegadas gigantes, presas no chão, entrada de gruta com neve |

### Andar 46 — Aldeia dos Caçadores
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 46 |
| Bioma | Aldeia de caçadores abandonada, neve até às janelas, uma torre com sino, uma cabana com fumo (a da Inga), floresta escura à volta |
| Zonas | **Aldeia Abandonada** · **Torre do Sino** · **Cabana da Inga** · **Floresta dos Caçadores** |
| Mecânica especial | **Reconstruir a aldeia** (cadeia de missões R5_05): cada edifício reconstruído traz NPCs e serviços. **Nevasca à noite**: aparece o Wendigo |
| Monstros | Caçador Congelado, Lobo de Gelo, Urso Polar, Espírito da Neve |
| Recursos | Pinheiro Nevado, Pele, Bagas de Inverno |
| Povoação | **Aldeia dos Caçadores** (secção 7.2) |
| Guardião | **Wendigo** |
| Segredo | No sino da torre está o **Diário da Equipa de Gorvan** (missão de história R5_06) |
| Puzzle | **Sino**: tocar o sino 3 vezes à meia-noite faz os Caçadores Congelados pararem (e alguns falarem) |
| Página de lore 46 | *"Os caçadores disseram-me para não ir ao andar 74. Eu fui à mesma. A janela mandou."* |
| Desafios | Reconstruir os 5 edifícios · Vencer o Wendigo durante a nevasca |
| Peças especiais | casa de caçador (em ruína e reconstruída), torre do sino, armadilhas, cabana com fumo |

### Andar 47 — Glaciar Rachado
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 47 |
| Bioma | Glaciar azul e branco cheio de fendas profundas, pontes de gelo, cavernas azuis dentro do gelo, um pico ao fundo |
| Zonas | **Fendas** · **Pontes de Gelo** · **Interior do Glaciar** · **Pico** |
| Mecânica especial | **Fendas** (cair: dano e voltas ao início da fenda; o **Gancho** atravessa). **Pontes de gelo** partem depois de passares. **Paredes de escalada** (com Picareta) |
| Monstros | Golem de Gelo, Harpia Gélida, Lobo de Gelo, Mamute Jovem |
| Recursos | **Fragmento de Gelo Eterno** (muito), Musgo Ártico, Safira |
| Guardião | **Tartaruga-Glaciar** |
| Segredo | O **Interior do Glaciar** tem a entrada selada da masmorra escondida (3 Brasas Eternas) |
| Puzzle | **Pontes**: atravessar uma série de pontes que partem, pela ordem certa (há uma ordem que deixa voltar) |
| Página de lore 47 | *"Dentro do glaciar há um rei. Dorme há mil anos. Não o acordei."* |
| Desafios | Atravessar sem usar o Gancho · Chegar ao Pico |
| Peças especiais | fenda, ponte de gelo, parede de escalada, caverna azul, pico com bandeira |

### Andar 48 — Campos da Aurora
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 48 · **noite eterna** |
| Bioma | Campos de neve debaixo de uma aurora boreal enorme verde, azul e roxa; pedras que cantam; um mosteiro; um lago que reflete o céu |
| Zonas | **Campo Aberto** · **Mosteiro da Aurora** (povoação) · **Lago-Espelho do Céu** · **Pedras Cantantes** |
| Mecânica especial | **Cores da aurora**: a aurora muda de cor a cada 2 minutos. Verde: +regeneração · Azul: +MP · Roxo: monstros mais fortes mas drops melhores. As **Pedras Cantantes** só cantam com a cor certa |
| Monstros | Espírito da Neve, Lobo de Gelo (muitos Lobos Aurora), Mamute Jovem |
| Recursos | **Lágrima de Aurora**, Flor-de-Neve |
| Povoação | **Mosteiro da Aurora** (secção 7.3) |
| Guardião | **Raposa Aurora** |
| Segredo | Com **aurora dourada** (evento raro), o Lago-Espelho deixa-te **andar dentro do reflexo**: um andar ao contrário com um baú de ouro |
| Puzzle | **Pedras Cantantes**: tocar as 4 pedras quando a aurora tem a cor de cada uma (missão R5_08) |
| Página de lore 48 | *"Aqui nunca é dia. Os monges dizem que a aurora são as almas dos Jogadores que desistiram."* |
| Desafios | Ver as 4 cores da aurora · Vencer a Raposa com a aurora roxa |
| Peças especiais | pedra cantante, mosteiro de pedra, lago-espelho, sinos de vento |

### Andar 49 — Fortaleza de Gelo
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 49 |
| Bioma | Um castelo inteiro feito de gelo azul, com muralhas, torres, estandartes congelados e um salão do trono vazio |
| Zonas | **Muralhas** · **Pátio** · **Torres** · **Salão do Trono Vazio** |
| Mecânica especial | **Balistas de gelo**: as torres têm balistas que disparam contra ti — mas **podes usá-las** contra os inimigos. **Portões**: abrir com alavancas nas torres |
| Monstros | Golem de Gelo, Harpia Gélida, Caçador Congelado, Soldado de Gelo (golem pequeno) |
| Recursos | Fragmento de Gelo Eterno, Safira, armas antigas de gelo |
| Guardião | **Cavaleiro de Gelo** |
| Segredo | O trono vazio tem uma **coroa de gelo**: pô-la na cabeça (interagir) mostra fantasmas da corte a dançar e dá o título *Rei por Um Minuto* |
| Puzzle | **Portões em cadeia**: 3 alavancas em 3 torres; cada uma abre um portão e fecha outro |
| Página de lore 49 | *"Um castelo sem ninguém. Os reis de gelo esperam um rei que não vem."* |
| Desafios | Derrubar 10 Harpias com as balistas · Entrar sem abrir o portão principal |
| Peças especiais | muralha de gelo, torre de gelo, balista, portão de gelo, trono de gelo |

### Andar 50 — Trono do Inverno 👑
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 50 |
| Bioma | Uma escadaria de gelo até ao topo de uma montanha; uma ponte estreita no vento; um ninho enorme feito de gelo e ossos lá em cima |
| Zonas | **Escadaria de Gelo** · **Ponte do Vento** · **Ninho do Dragão** (arena no pico) |
| Mecânica especial | **Vento forte** na ponte. Na arena, o dragão **voa** e ataca de cima; as estacas de gelo que ele faz servem de abrigo |
| Monstros | Golem de Gelo, Harpia Gélida |
| Boss | **Dragão de Gelo** (ver `docs/BOSSES.md`) → arma única **Sopro Gélido** (katana) |
| Depois do boss | **Dia da Subida** (meio da torre!). Grande festa em Ascendia, e o Lucien compõe "A Balada do Andar 50" |
| Página de lore 50 | *"Metade. O dragão disse que eu era o primeiro a chegar aqui sozinho. 'Os outros vinham com amigos', disse."* |
| Desafios | Vencer sem ser congelado · Vencer em menos de 5 min |
| Peças especiais | escadaria de gelo, ponte estreita, ninho de gelo e ossos, estacas de gelo grandes |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 41 | **Morsa Gigante** | morsa castanha enorme (64×64) com presas compridas | Presas (golpe para baixo) · Deslizar de barriga · Bater no gelo (abre rachas) | Fogo | **Presas de Morsa** (adaga): +20% dano em inimigos com Frio ou Congelados |
| 42 | **Alce Fantasma** | alce branco meio transparente (48×48) com chifres de gelo | Carga · Chifres de Gelo (área) · Desaparecer entre os pinheiros | Fogo, Luz | **Arco de Chifre** (arco): as flechas atravessam 1 inimigo |
| 43 | **Kraken do Gelo** | só se veem tentáculos (64×64) a sair dos buracos do gelo | Tentáculos (saem dos buracos) · **Partir o gelo** (abre buracos novos) · Tinta (Cegueira) | Fogo, Raio | **Lança Tentáculo** (lança): as estocadas puxam o alvo para ti |
| 44 | **Coração de Cristal Azul** | figura de gelo a flutuar (48×48) com estilhaços em órbita | Estilhaços em órbita · Raio de Gelo · Prisão de Gelo (congela uma área) | Fogo | **Cajado Gélido** (cajado): 25% de causar Frio |
| 46 | **Wendigo** | criatura magra e alta de gelo (48×48) com crânio de alce | Garras · Grito (Medo) · Corre a quatro patas · invisível na nevasca | Fogo, Luz | **Foice do Wendigo** (foice): 10% de causar Medo |
| 47 | **Tartaruga-Glaciar** | tartaruga gigante (64×64) com um glaciar como carapaça | **Esconder** (invencível: ataca as patas quando as põe de fora) · Rolar · Chuva de Gelo | Fogo, Martelo | **Martelo Glaciar** (martelo): os golpes gelam o chão e os inimigos escorregam |
| 48 | **Raposa Aurora** | raposa branca (48×48) com várias caudas que brilham como a aurora | Fogos-fátuos coloridos · Ilusões (cópias) · Teletransporte | Sombra | **Katana Aurora** (katana): os críticos libertam uma pequena explosão de Luz |
| 49 | **Cavaleiro de Gelo** | armadura de gelo vazia (48×48) com espada grande | Golpe Glacial · Escudo de Gelo (reflete projéteis) · Chamar 2 Soldados de Gelo | Fogo | **Lâmina do Cavaleiro Gélido** (espada grande): +10% DEF e imune a Frio |

---

## 7. Povoações

### 7.1 Pinhal-do-Norte (andar 42)
Aldeia de **gente do norte** (Torrenses do frio): casas de troncos com telhados de relva cobertos de neve, salão comunal
com lareira enorme, sauna à beira do lago. Tem **salão** (dormir), **cristal**, **loja** e **sauna**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Ulf Barba-Gelo** | chefe da aldeia, barba branca com gelo | Missões; o Kraken do lago (R5_09) |
| **Sigrid** | dona da sauna | **Sauna**: a temperatura não desce durante 1 dia (depois da missão R5_02) |
| **Erik Trenó** | condutor de trenós de cães | **Trenó**: viagem rápida entre as Zonas Seguras da região (R5_04) |
| **Velha Astrid** | tricota tudo | Casacos, luvas, gorros, **Raquetes de Neve** |
| **Leif** | rapaz de 9 anos | Quer um pinguim (R5_03) |

### 7.2 Aldeia dos Caçadores (andar 46) — reconstrução
Começa **abandonada**: só lá vive a **Caçadora Inga**. A cadeia de missões **R5_05** reconstrói 5 edifícios:

| Edifício | Materiais | Quem volta | O que abre |
|---|---|---|---|
| Cabana Comum | 30 Pinheiro + 10 Pedra | caçadores | cama e cristal |
| Forja do Caçador | 20 Pedra + 10 Barra de Gelo Eterno | **Ferreiro Gunnar** | forja de Gelo Eterno, melhorias |
| Casa da Curandeira | 20 Pinheiro + 10 Flor-de-Neve | **Curandeira Helka** | poções, cura de estados |
| Armazém | 30 Pinheiro + 10 Pele de Urso | **Comerciante Sven** | loja |
| Torre do Sino | 20 Pedra + 5 Lingote de Prata | **Sineiro Olaf** | evento: o sino afasta os Caçadores Congelados à noite |

| NPC | Quem é | O que faz |
|---|---|---|
| **Caçadora Inga** | última sobrevivente, dura e calada | Missões de reconstrução; treina arco e armadilhas; companheira de caça |
| **Gunnar, Helka, Sven, Olaf** | voltam com a reconstrução | serviços (ver tabela) |

### 7.3 Mosteiro da Aurora (andar 48)
Mosteiro de pedra onde monges estudam a aurora em silêncio. Tem **celas** (dormir), **cristal** e **chá quente**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Mestre Kael** | abade, calmo e sábio | Ensina a skill **Meditação** (R5_08) |
| **Monge Tenzin** | jovem monge brincalhão | Desafios de equilíbrio (gelo fino, R5_10) |
| **Irmã Noor** | guarda a biblioteca do mosteiro | Livros de receitas de chás; lore da aurora |

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R5_01 | Casaco Quente | Velha Astrid | 10 Lã de Mamute + 5 Pele de Lobo de Gelo | **Casaco de Lã** (temperatura desce metade) |
| R5_02 | A Sauna da Sigrid | Sigrid | 20 Pinheiro Nevado + 10 Pedra | Sauna aberta |
| R5_03 | Um Pinguim para o Leif | Leif | Trazer 2 ovos de pinguim do andar 43 sem os deixar arrefecer (passar por fogueiras) | **Pinguim** (animal de estimação) — o Leif fica com o outro |
| R5_04 | Os Cães do Erik | Erik Trenó | Encontrar 4 cães perdidos (andares 41–42) | **Trenó** (viagem rápida na região) |
| R5_05 | Reconstruir a Aldeia (5 partes) | Caçadora Inga | Os 5 edifícios da secção 7.2 | Aldeia viva · festa · **Arco de Gelo Eterno Épico** |
| R5_06 | **O Diário de Gorvan** (história) | (encontrar no sino) | Levar o diário ao Mestre Gorvan | Cena da história · ❤️❤️ Gorvan |
| R5_07 | A Cria de Presa-Branca | Zed (depois de vencer o Presa-Branca) | Levar a cria a Ascendia sem a deixar arrefecer | **Montada Lobo de Gelo** |
| R5_08 | Meditação | Mestre Kael | Tocar nas 4 Pedras Cantantes com a aurora certa | Skill passiva **Meditação** (parado 2 s: MP regenera ×3) |
| R5_09 | O Kraken do Lago | Ulf Barba-Gelo | Vencer o Kraken sem partir o gelo à volta do farol | **Arpão** (pesca de peixes grandes) |
| R5_10 | Gelo Fino | Monge Tenzin | Atravessar o Gelo Fino do andar 43 em 60 s | **Botas de Pico** (não escorregas no gelo) |
| R5_11 | O Gigante Gentil | Capitã Freya (rank B) | **Escolha**: vencer o Mamute Ancião **ou** acalmá-lo com 20 Bagas de Inverno | Matar: Marfim Ancestral · Acalmar: Lã Ancestral ×5 e título *Amigo dos Gigantes* |
| R5_12 | Fogueira Eterna | Velho Fausto | Trazer uma Brasa Eterna do iglu (andar 41) | Receita **Pedra Quente** |
| R5_13 | Chá de Bagas | Dona Marta | 10 Bagas de Inverno | Receita **Chá Quente** (+40 temperatura, +regeneração) |
| R5_14 | Balistas | Capitã Freya | Derrubar 10 Harpias com as balistas do andar 49 | Besta Pesada de Gelo Eterno (épica) |
| R5_15 | Descanso para os Caçadores | Caçadora Inga | Dar descanso a 10 Caçadores Congelados (Fogo ou Luz) e enterrar 5 diários | **Amuleto do Caçador** (+15% dano a monstros que te não viram) |

---

## 9. Masmorra escondida — Cripta do Rei do Inverno (andar 47)

| | |
|---|---|
| Entrada | Interior do Glaciar; derreter o selo com 3 Brasas Eternas |
| Sala 1 | **Corredor do Vento Uivante**: vento que empurra para trás, com abrigos atrás de colunas |
| Sala 2 | **Salão dos Guerreiros Congelados**: 12 guerreiros no gelo que acordam um a um quando passas perto |
| Sala 3 | **Espelhos de Gelo**: rodar espelhos para levar um raio de luz até ao selo do rei |
| Boss extra | **Rei do Inverno Esquecido** (64×64): rei-esqueleto de gelo com coroa; chama nevões e guerreiros, e congela metade da sala de cada vez |
| Recompensa | **Lança do Inverno Eterno** (arma secreta, lança): os inimigos ficam Congelados com 2 acumulações de Frio (em vez de 3) · baú de ouro · página de lore extra "O Rei que Esperou" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Caranguejo-Neve | Costa Gelada (41) | dia | comum | 110 |
| Bacalhau Ártico | buracos do andar 43 | dia | comum | 120 |
| Salmão do Gelo | rio do andar 42 | Outono | incomum | 260 |
| Peixe-Lanterna Gelado | poças do andar 44 | sempre | raro | 520 |
| Truta Aurora | Lago-Espelho (48) | aurora verde | raro | 600 |
| **Narval Real** (lendário) | andar 43, só com **Arpão** | nevão, 4:00–6:00 | lendário | 7 000 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Bagas de Inverno | arbustos do andar 42 | 8 (dá sempre) | Outono, **Inverno** | chá, acalmar animais |
| Couve do Norte | Astrid | 6 | Inverno | sopas |
| Flor-de-Neve | andar 41 | 7 | **Inverno** | Poção Quente, presentes |
| Musgo Ártico | andar 47 | 5 | Inverno (à sombra) | poções |

### Animais
- **Pinguim** (animal de estimação): missão R5_03. Desliza contra os inimigos e **empurra-os**; no gelo dá-te +10% velocidade.
- **Lobo de Gelo** (montada): missão R5_07. Corre 11 m/s, **não escorrega no gelo**, a temperatura não desce enquanto montas.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Nevão | 20% ao entrar num andar ao ar livre | Visão 10 m, temperatura desce depressa, Presa-Branca pode aparecer |
| Avalanche | encostas, de vez em quando | Uma onda de neve desce a encosta: abrigar-te ou fugir para os lados |
| Aurora Dourada | rara (1 vez por estação) no andar 48 | Drops ×2; o reflexo do lago abre-se |
| Lago Rachado | andar 43, 1 dia em cada 7 | Icebergs a flutuar; o Narval aparece mais |
| Festa do Solstício | Inverno, dia 14, em Pinhal-do-Norte | Fogueiras, comida quente, concurso de esculturas de gelo |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 28): neve ×3, gelo liso, gelo fino, neve funda, rocha com neve ×3, falésia de gelo, pinheiro nevado ×2, arbusto de bagas,
  bloco de gelo eterno, árvore cortável, erva/flor-de-neve, baú, fogueira, cristal, casa de troncos, ponte de gelo, estaca de gelo, banco de neve
- [ ] **Peças especiais dos andares** (≈ 45)
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Presa-Branca, Mamute Ancião Tundra
- [ ] **8 guardiões**
- [ ] **Mini-boss** Yeti Ancião e **boss** Dragão de Gelo
- [ ] **Boss da masmorra** Rei do Inverno Esquecido
- [ ] **Armas**: 12 de Gelo Eterno + 2 únicas + 8 de guardião + 1 secreta = **23 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 24), **peixes** (6), **plantas** (4 × 4 fases)
- [ ] **NPCs**: Ulf, Sigrid, Erik, Astrid, Leif, Inga, Gunnar, Helka, Sven, Olaf, Kael, Tenzin, Noor (+ retratos)
- [ ] **Animais**: Pinguim, Lobo de Gelo (montada)
- [ ] **Conjunto de armadura** de Pele de Urso Polar (5 ícones)
- [ ] **Interface**: barra de Temperatura
