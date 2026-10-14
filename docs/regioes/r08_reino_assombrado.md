# Região 8 — Reino Assombrado (andares 71–80)

> Estrutura igual às outras regiões. Bosses grandes (Lich Bibliotecário e Rei Sem Coroa) em `docs/BOSSES.md`.
> No andar 74 o **Mestre Gorvan** junta-se a ti para enfrentar o passado (ver `docs/HISTORIA.md`).

---

## 1. Identidade

| | |
|---|---|
| Tema | Um reino medieval engolido pela torre e amaldiçoado: muralhas, uma cidade fantasma, cemitérios, uma biblioteca proibida, uma catedral partida, um castelo |
| Sensação | Arrepios, tristeza, histórias por acabar; e a luz como esperança |
| Material das armas | **Mitril** (tier 8) — aqui está amaldiçoado e tem de ser **purificado** |
| Monstros fracos a | **Luz** |
| Cores principais | roxos `#45293f` `#6b3e75` `#905ea9`, cinzentos azulados `#323353` `#484a77`, verde fantasma `#8ff8e2`, velas `#fbb954`, sangue escuro `#831c5d` |
| Luz | lua grande e pálida, névoa roxa rente ao chão, velas e lanternas quentes, raios coloridos dos vitrais |
| Clima | Nevoeiro roxo 50% · Céu nublado 30% · Chuva 15% · Noite sem lua 5% |
| Música | `muralhas`, `cidade_fantasma` (caixa de música), `catacumbas`, `catedral`, `lich`, `rei_sem_coroa` |
| Níveis | monstros 71–81; mini-boss 77; boss 83 |
| Mecânica da região | **Névoa roxa**: dentro dela ganhas Maldição a cada 5 s. **Zonas de luz** (lanternas sagradas, vitrais, velas) curam 1% por segundo e os mortos-vivos não entram. **Sepulturas** fazem os mortos-vivos voltar a aparecer: **consagrá-las** com Água Benta impede-o nessa zona. **Lanterna Sagrada** (item da Ordem da Luz): leva a luz contigo 5 min |
| Animal de estimação | Gato Fantasma |

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Minério de Mitril (amaldiçoado) | veios prateados com brilho roxo (71, 74, 78) | Picareta de Obsidiana+ | Lingote de Mitril (3 minérios + 1 **Água Benta** para purificar) |
| Ébano Morto | árvores negras (73, 76) | Machado | **madeira** da região |
| Asa de Gárgula | Gárgula | drop | **couro** da região (couro de pedra flexível) |
| Fio Espectral | Ectoplasma tecido no tear | tear (Elva ou Ordem da Luz) | **fio** da região |
| Lágrima de Fantasma | Fantasma, Banshee | drop | **cristal** da região |
| Ónix | catacumbas (74) | Picareta | gema de **Sombra** |
| Diamante | vitrais partidos (77, raro) | Picareta | gema de **Luz** |
| Rosa Negra | jardins (76) | à mão | presentes, Poção das Sombras |
| Sálvia Sagrada | claustro do mosteiro (77) | à mão | **Água Benta** (com Água Limpa) |
| Lírio da Lua | 73 (só à noite) | à mão | poções de MP |
| Ectoplasma | Fantasmas | drop | Fio Espectral, alquimia |
| Página Antiga | Livro Possuído | drop | receitas, lore |

---

## 3. Monstros

### 3.1 Fantasma
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago + Voador** (atravessa paredes) |
| Andares | 71, 72, 73, 74, 78 |
| Comportamento | Flutua através das paredes; às vezes **possui** um objeto (uma armadura, uma cadeira, um quadro) que ganha vida e ataca |
| Ataques | **Toque Gelado**: Maldição · **Grito** (aviso 0,8 s) · **Possuir**: entra num objeto perto (o objeto passa a ser o inimigo até o partires) |
| Fraco / Resiste | **Luz (×2)** / Físico (−50%), Veneno (imune) |
| Drops | Ectoplasma 50% · Lágrima de Fantasma 15% |
| Elite | **Fantasma Nobre**: possui 2 objetos ao mesmo tempo |
| Animações | flutuar (4), atacar (4), gritar (4), entrar num objeto (4), dano (1), desaparecer (4) |

### 3.2 Zombie
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, grupos de 3–6 |
| Andares | 71, 73, 74, 76 |
| Comportamento | Lentos mas muitos; **saem das sepulturas** (as mãos saem primeiro) |
| Ataques | **Agarrar** (prende 1 s) · **Mordida**: Maldição · **Arranhar** |
| Fraco / Resiste | Fogo, Luz / Veneno (imune) |
| Drops | Trapo 40% · Osso 30% · Dente 20% |
| Elite | **Zombie Inchado**: ao morrer explode numa nuvem de veneno |
| Animações | sair da terra (6), parado (4), mover (6: a coxear), agarrar (4), morder (4), dano (1), morrer (5) |

### 3.3 Cavaleiro Esqueleto
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal** (armadura pesada: DEF ×1,5) |
| Andares | 71, 78, 79, 80 |
| Comportamento | Antigos cavaleiros do reino. Lutam com honra (um de cada vez). **Remontam-se** se não lhes partires o crânio |
| Ataques | **Espada** (combo de 3) · **Escudo** · **Carga com escudo** (aviso 0,7 s) |
| Fraco / Imune | Luz, Martelo / Veneno |
| Drops | Osso 50% · Armadura Velha 20% · Fragmento de Mitril 5% |
| Elite | **Cavaleiro Negro**: a espada causa Maldição |
| Animações | parado (4), mover (6), espada (4), escudo (2), carga (4), dano (1), desmontar (4), remontar (6) |

### 3.4 Gárgula
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque + Voador** |
| Andares | 71, 77, 79 |
| Comportamento | Parece uma estátua nos telhados e muralhas. De vez em quando **vira pedra** (invencível 3 s) e no fim ataca |
| Ataques | **Mergulho** · **Garras** · **Petrificar**: invencível 3 s e depois um golpe forte à volta |
| Fraco / Resiste | Luz, Martelo / Físico (−20%) |
| Drops | Asa de Gárgula 45% · Pedra Esculpida 30% |
| Elite | **Gárgula Ancestral**: cospe ácido |
| Animações | estátua (1), acordar (4), voar (4), mergulho (4), garras (4), petrificar (3), dano (1), morrer (5: parte-se) |

### 3.5 Vampiro
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido + Mago**, sozinho |
| Andares | 72 (noite), 73, 76, 78 |
| Comportamento | Elegante e rápido; desfaz-se em morcegos para fugir. **De dia dorme em caixões**: encontrar o caixão de dia e abri-lo mata-o com um golpe |
| Ataques | **Mordida**: rouba 50% do dano · **Enxame de Morcegos** (área) · **Hipnose**: és puxado para ele 2 s (aviso 0,8 s: olhos vermelhos) |
| Fraco / Resiste | Luz, Fogo / Sombra |
| Drops | Presa de Vampiro 30% · Sangue Antigo 20% · Capa de Vampiro 10% (cosmético) |
| Elite | **Vampiro Ancião**: chama 2 Vampiros |
| Animações | parado (4), mover (6), mordida (4), morcegos (6), hipnose (4), dano (1), morrer (5: vira pó) |

### 3.6 Livro Possuído
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Fraco + Mago**, grupos de 2–4 |
| Andares | 75, 77, 78 |
| Comportamento | Voam a bater as capas. **Barulho** (correr, lutar) acorda os livros das estantes |
| Ataques | **Morder** com as páginas · **Feitiço ao acaso**: Fogo, Gelo ou Raio (a cor das páginas avisa) |
| Fraco / Resiste | Fogo (×2), Luz / — |
| Drops | Página Antiga 50% · Tinta Mágica 25% · **Livro de Receitas** 3% |
| Elite | **Grimório**: chama 3 livros |
| Animações | fechado (1), voar (4), morder (4), feitiço (4), dano (1), morrer (4: as páginas voam) |

### 3.7 Banshee
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago + Voador** |
| Andares | 73, 74, 76, 80 |
| Comportamento | Espírito de mulher com cabelo comprido a flutuar; chora antes de gritar |
| Ataques | **Grito**: Medo e dano em área grande (aviso 1 s: chora mais alto) · **Lamento**: −20% ATQ durante 8 s |
| Fraco / Resiste | Luz / Físico (−30%) |
| Drops | Véu de Banshee 30% · Lágrima de Fantasma 20% |
| Elite | **Banshee Rainha**: o grito parte objetos e paredes finas |
| Animações | flutuar (4), chorar (4), gritar (5), dano (1), desaparecer (4) |

### 3.8 Armadura Viva
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 77, 79, 80 |
| Comportamento | Uma armadura vazia com um fantasma dentro. Ao partires a armadura, sai o **fantasma** (2.ª fase, mais fraca) |
| Ataques | **Alabarda** (área à frente) · **Investida** · **Escudo** |
| Fraco / Resiste | Luz, Martelo, Raio / Físico (−20%) |
| Drops | Placa de Mitril 30% · Elmo Vazio 10% |
| Elite | **Armadura Real**: dourada; o fantasma de dentro é um Fantasma Nobre |
| Animações | parada (1), acordar (4), mover (4), alabarda (5), investida (4), escudo (2), partir-se (6) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Condessa Sangria** | andares 72, 76, 78, à noite, 4% | vampira de vestido vermelho e leque preto | Vira nuvem de morcegos · chama vampiros · "dança" (ataques em círculo) · hipnose dupla | **Leque da Condessa** (roubo de vida 3%) · **Rosa de Sangue** (presente lendário) |
| **O Jardineiro** | andar 76, ao entardecer, 5% | zombie gigante com chapéu de palha e uma tesoura de poda enorme | Persegue-te pelo labirinto de sebes, corta as sebes, ri-se; não pode ser parado, só **escondendo-te** e atacando-o pelas costas | **Foice-Tesoura** (foice rara) · **Chapéu de Palha do Jardineiro** (+1 colheita na quinta) |

---

## 5. Os andares

### Andar 71 — Muralhas em Ruínas
| | |
|---|---|
| Tamanho / Nível | 280×200 m · nível 71 |
| Bioma | Muralhas enormes de pedra cinzenta partidas, ameias, um portão gigante fechado, um fosso, névoa roxa rente ao chão, lua grande |
| Zonas | **Portão Principal** · **Ameias** · **Brecha na Muralha** · **Fosso** |
| Mecânica especial | **Névoa roxa** começa aqui. **Ameias**: subir às muralhas por escadas e torres; lá em cima não há névoa |
| Monstros | Zombie, Cavaleiro Esqueleto, Gárgula, Fantasma |
| Recursos | Minério de Mitril, Pedra Esculpida, Ébano Morto (pouco) |
| Guardião | **Sentinela da Muralha** |
| Segredo | O portão nunca abre: entra-se pela Brecha. Mas **por dentro**, uma roda dentada abre o portão — e do lado de fora estava à espera um **baú de ouro** |
| Puzzle | **Ponte levadiça**: baixar a ponte do fosso com duas manivelas em duas torres |
| Página de lore 71 | *"Um reino inteiro. Com bandeiras. Com um rei. A torre engoliu-o e ele continua a fingir que governa."* |
| Desafios | Atravessar só pelas ameias · Não ganhar Maldição |
| Peças especiais | muralha (reta, partida), torre de muralha, portão gigante, ponte levadiça, ameias |

### Andar 72 — Cidade Fantasma
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 72 |
| Bioma | Uma cidade medieval de casas de madeira e pedra, ruas de calçada, uma praça com mercado e uma torre do relógio parada à meia-noite |
| Zonas | **Rua Principal** · **Praça do Mercado** · **Casas Abandonadas** · **Torre do Relógio** |
| Mecânica especial | **De dia**: cidade vazia com zombies. **De noite**: aparecem os **fantasmas cidadãos** (amigáveis!) e abre o **Mercado Fantasma** (povoação) |
| Monstros | Zombie (dia), Vampiro (noite), Fantasma (hostis só nas casas), Banshee |
| Recursos | Ébano Morto, Ectoplasma, Lírio da Lua |
| Povoação | **Mercado Fantasma** (secção 7.1), só à noite |
| Guardião | **O Pregoeiro Fantasma** |
| Segredo | Numa casa abandonada, um **piano** que toca sozinho: tocar a melodia certa (a da caixa de música da música do andar) abre a cave com um baú de ouro |
| Puzzle | **Torre do Relógio**: pôr as engrenagens no sítio (missão R8_02) |
| Página de lore 72 | *"Os fantasmas daqui não sabem que morreram. Compram pão, cumprimentam-se. São felizes. Deixei-os assim."* |
| Desafios | Comprar algo no Mercado Fantasma · Atravessar a cidade de dia sem lutar |
| Peças especiais | casa medieval (3), torre do relógio, bancas de mercado fantasma, poço, piano |

### Andar 73 — Cemitério Real
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 73 |
| Bioma | Um cemitério enorme com campas tortas, mausoléus de reis, árvores negras, corvos, uma capela e uma cripta de mármore |
| Zonas | **Campas** · **Mausoléus Reais** · **Capela do Coveiro** · **Cripta da Rainha** |
| Mecânica especial | **Sepulturas** fazem mortos-vivos voltar; **consagrá-las** (Água Benta) acaba com isso. **Corvos**: se te veem, crocitam e os mortos acordam |
| Monstros | Zombie, Fantasma, Banshee, Vampiro |
| Recursos | Ébano Morto, Lírio da Lua, Osso |
| Guardião | **Coveiro Ghoul** |
| Segredo | A **Cripta da Rainha** só abre à meia-noite depois de consagrares 10 sepulturas: é a masmorra escondida |
| Puzzle | **Mausoléus**: os 4 reis têm 4 brasões; pôr flores nas campas pela ordem da árvore genealógica (pintada na capela) |
| Página de lore 73 | *"Contei as campas. Muitas têm o símbolo da janela azul. Jogadores enterrados por gente que gostava deles."* |
| Desafios | Consagrar 10 sepulturas · Atravessar sem os corvos te verem |
| Peças especiais | campa (3), mausoléu, árvore negra com corvos, capela, entrada de cripta |

### Andar 74 — Catacumbas
| | |
|---|---|
| Tamanho / Nível | 240×240 m em 2 pisos · nível 74 |
| Bioma | Túneis escuros com paredes feitas de ossos e crânios, velas antigas, nichos, um abismo de ossos, uma sala com armas e mochilas velhas de aventureiros |
| Zonas | **Ossário** · **Túneis de Crânios** · **Sala da Equipa** · **Abismo de Ossos** |
| Mecânica especial | **O Mestre Gorvan junta-se a ti** como companheiro (cena). **Paredes de ossos** que se mexem. **Escuridão** |
| Monstros | Zombie, Fantasma, Banshee, Cavaleiro Esqueleto |
| Recursos | **Ónix**, Minério de Mitril, Osso |
| NPCs | **Mestre Gorvan** (companheiro neste andar) |
| Guardião | **Colosso de Ossos** |
| Segredo | Na **Sala da Equipa** estão as coisas da antiga equipa do Gorvan. Devolver cada objeto a quem o Gorvan disser (diálogo) dá a cena de despedida e o **Machado do Gorvan** como lembrança (decoração) |
| Puzzle | **Velas**: acender as velas pela ordem dos nomes da equipa (no diário do andar 46) para abrir a Sala da Equipa |
| Página de lore 74 | *(tinta azul)* *"Aqui morreu uma equipa inteira. O sobrevivente perdeu um braço e a vontade de subir. Ele ainda vai voltar. Sei que vai."* |
| Desafios | Vencer o Colosso com o Gorvan vivo · Encontrar os 5 objetos da equipa |
| Peças especiais | parede de ossos, nicho com crânio, velas antigas, abismo de ossos, sala com equipamento velho |

### Andar 75 — Biblioteca Proibida 💀
| | |
|---|---|
| Tamanho / Nível | 200×200 m, com estantes de 20 m de altura · nível 75 |
| Bioma | Uma biblioteca gigante com estantes até ao teto, escadas de rodas, livros a voar, velas a flutuar, poeira dourada |
| Zonas | **Salão de Leitura** · **Labirinto de Estantes** · **Arquivo Selado** · **Sala do Lich** (arena) |
| Mecânica especial | **Silêncio**: correr e lutar fazem barulho e acordam os livros. **Escadas de rodas** que se movem nas estantes (levar para onde precisas) |
| Monstros | Livro Possuído (muitos), Fantasma, Banshee |
| Recursos | Página Antiga, Tinta Mágica, Livros de Receitas |
| Mini-boss | **Lich Bibliotecário** (ver `docs/BOSSES.md`) → arma única **Grimório Proibido** (cajado) |
| Segredo | No Arquivo Selado: os **livros perdidos** do Velho Fausto (missão R8_10) |
| Página de lore 75 | *"Na biblioteca há um livro com a minha vida. As páginas do fim estão em branco."* |
| Desafios | Atravessar o Salão sem acordar nenhum livro · Vencer o Lich sem deixar que ele leia 3 feitiços seguidos |
| Peças especiais | estante gigante, escada de rodas, mesa de leitura, livros a flutuar, vela flutuante |

### Andar 76 — Jardins Mortos
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 76 |
| Bioma | Jardins de palácio secos e cinzentos: labirinto de sebes, estátuas de jardim, uma estufa de vidro partido, uma fonte sem água, um roseiral de rosas negras |
| Zonas | **Labirinto de Sebes** · **Estufa Partida** · **Fonte Seca** · **Roseiral Negro** |
| Mecânica especial | **O labirinto muda** ao entardecer (as sebes mexem-se). **Rosas negras**: tocar dá Maldição. **O Jardineiro** (monstro com nome) anda por aqui |
| Monstros | Zombie, Vampiro, Banshee, Gárgula |
| Recursos | **Rosa Negra**, Ébano Morto, sementes estranhas |
| Guardião | **Rainha das Rosas Negras** |
| Segredo | Na lua nova, a Fonte Seca **enche-se de água negra**: aparece o peixe lendário da região |
| Puzzle | **Estátuas do jardim**: rodar 4 estátuas para que todas olhem para a fonte |
| Página de lore 76 | *"A rainha plantava rosas. Quando o rei se perdeu, as rosas ficaram negras. Até as flores têm saudades."* |
| Desafios | Sair do labirinto em 3 min · Fugir do Jardineiro sem lutar |
| Peças especiais | sebe (reta, curva, cruzamento), estátua de jardim, estufa de vidro, fonte seca, roseira negra |

### Andar 77 — Catedral Partida
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 77 |
| Bioma | Uma catedral gótica enorme com o teto meio caído, vitrais partidos que deixam entrar luz colorida, órgão, torre dos sinos; ao lado, um mosteiro ainda vivo |
| Zonas | **Nave Central** · **Vitrais Partidos** · **Torre dos Sinos** · **Mosteiro da Catedral** (povoação) |
| Mecânica especial | **Luz dos vitrais**: zonas de luz colorida no chão. A luz **branca** cura e afasta mortos-vivos. **Restaurar os vitrais** (missão R8_06) aumenta as zonas de luz |
| Monstros | Gárgula, Livro Possuído, Armadura Viva, Fantasma |
| Recursos | **Diamante** (vitrais partidos), **Sálvia Sagrada** (claustro), Minério de Mitril |
| Povoação | **Mosteiro da Ordem da Luz** (secção 7.2) |
| Guardião | **Anjo Caído de Vitral** |
| Segredo | O **órgão**: tocar as notas certas (pista nos vitrais) abre a cripta debaixo do altar com a **Espada Benta** (decoração e lore) |
| Puzzle | **Sinos**: tocar os 3 sinos da torre pela ordem dos tamanhos (missão R8_14) |
| Página de lore 77 | *"Rezei na catedral. Não sei a quem. Mas a janela azul não apareceu durante uma hora inteira."* |
| Desafios | Atravessar a nave só pela luz · Tocar a melodia do órgão |
| Peças especiais | coluna gótica, vitral (inteiro e partido), órgão, altar, sino, banco de igreja |

### Andar 78 — Masmorras do Castelo
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 78 |
| Bioma | Corredores húmidos de pedra, celas com grades, correntes, tochas, um poço fundo; alguns prisioneiros ainda vivos |
| Zonas | **Celas** · **Sala dos Castigos** (correntes e grilhetas) · **Prisioneiros Fantasmas** · **Poço** |
| Mecânica especial | **Chaves**: encontrar chaves para abrir celas (umas têm prisioneiros vivos, outras monstros). **Guardas**: patrulham; esconder-te nas celas abertas e nas sombras (furtividade) |
| Monstros | Cavaleiro Esqueleto, Vampiro, Fantasma, Zombie |
| Recursos | Minério de Mitril, Ferro velho, Ónix |
| Guardião | **Carcereiro** |
| Segredo | O **Poço** desce até um rio subterrâneo com o caixão de um Vampiro Ancião (de dia: um só golpe) |
| Puzzle | **Celas**: a chave mestra está dividida em 3 partes, guardadas por 3 guardas que patrulham |
| Página de lore 78 | *"Os prisioneiros eram Jogadores que se recusaram a subir. O reino prendia-os. O rei tinha medo da torre."* |
| Desafios | Libertar os 4 prisioneiros vivos · Atravessar sem seres visto |
| Peças especiais | cela com grades, corrente na parede, poço, porta de masmorra, tocha de parede |

### Andar 79 — Salão dos Cavaleiros Caídos
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 79 |
| Bioma | Um castelo por dentro: galeria de armaduras, salão de banquetes com uma mesa enorme e fantasmas a comer, arsenal, uma varanda com vista para o reino |
| Zonas | **Galeria de Armaduras** · **Salão de Banquetes Fantasma** · **Arsenal** · **Varanda Real** |
| Mecânica especial | **Armaduras paradas**: algumas são Armaduras Vivas — a **luz** mostra quais (o fantasma brilha dentro). **Banquete fantasma**: sentar-te à mesa e ouvir o brinde (missão R8_13) |
| Monstros | Armadura Viva, Cavaleiro Esqueleto, Gárgula |
| Recursos | Placa de Mitril, armas antigas, Minério de Mitril |
| Guardião | **Comandante dos Cavaleiros Caídos** |
| Segredo | No Arsenal, a armadura do **Comandante quando era vivo** (decoração) e uma carta para a Rainha (missão R8_15) |
| Puzzle | **Estandartes**: pendurar os 4 estandartes das casas nobres no sítio certo (brasões nas portas) |
| Página de lore 79 | *"Os cavaleiros juraram defender o rei até ao fim. A torre levou isso à letra."* |
| Desafios | Encontrar todas as Armaduras Vivas antes de acordarem · Vencer o Comandante sem destruir os estandartes |
| Peças especiais | armadura em pedestal, mesa de banquete, estandarte, suporte de armas, varanda |

### Andar 80 — Sala do Trono 👑
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 80 |
| Bioma | Um corredor de estandartes rasgados até uma sala do trono enorme e vazia, com vitrais roxos, um trono partido e uma coroa a flutuar no ar |
| Zonas | **Corredor dos Estandartes** · **Antecâmara Real** · **Sala do Trono** (arena) |
| Mecânica especial | **A coroa flutuante**: o Rei luta para a alcançar; se ela tocar no trono ele recupera vida (empurrá-la para longe com ataques) |
| Monstros | Armadura Viva, Cavaleiro Esqueleto, Banshee |
| Boss | **Rei Sem Coroa** (ver `docs/BOSSES.md`) → arma única **Lâmina do Rei Caído** (espada grande) |
| Depois do boss | **Dia da Subida**. O Gorvan fala contigo em Ascendia (cena) e volta a treinar — e pode ser **companheiro** |
| Página de lore 80 | *"O rei pediu-me desculpa. Disse que tentou parar a torre. Disse que ninguém pode. Depois sorriu: 'Talvez tu.'"* |
| Desafios | Vencer sem deixar a coroa tocar no trono · Vencer em menos de 6 min |
| Peças especiais | trono partido, coroa flutuante, estandartes rasgados, vitral roxo grande |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 71 | **Sentinela da Muralha** | fantasma de arqueiro gigante (48×48) nas ameias | Chuva de Flechas Fantasma · Teletransporte entre torres · Grito de Alerta (acorda tudo) | Luz | **Arco da Sentinela** (arco): as flechas ignoram 30% da DEF |
| 72 | **O Pregoeiro Fantasma** | fantasma gordo com um sino gigante (48×48) | Sino (ondas de som: Atordoado) · Proclamação (os fantasmas cidadãos ficam hostis 20 s) · Voo | Luz | **Martelo-Sino** (martelo): 10% de atordoar todos os inimigos à volta |
| 73 | **Coveiro Ghoul** | ghoul curvado com uma pá (48×48) | Pá (área) · Cavar (desaparece e sai noutro sítio) · Levantar Mortos (3 zombies) | Luz, Fogo | **Pá-Machado do Coveiro** (machado): também escava pontos de tesouro |
| 74 | **Colosso de Ossos** | gigante feito de centenas de ossos (64×64) | Braços de Ossos · **Desfazer-se** (vira enxame de ossos e volta a montar-se) · Chuva de Crânios | Luz, Martelo | **Espada Grande de Ossos** (espada grande): o ataque carregado lança 3 crânios que perseguem inimigos |
| 76 | **Rainha das Rosas Negras** | espírito de rainha feita de rosas e espinhos (48×48) | Espinhos (Sangrar) · Pétalas Negras (Maldição em área) · Rosas que Prendem | Fogo, Luz | **Adaga Rosa Negra** (adaga): os críticos causam Maldição |
| 77 | **Anjo Caído de Vitral** | anjo feito de vidro de vitral partido e colorido (48×48) | Raios de Luz Colorida (cada cor é um elemento) · Estilhaços · Asas Cortantes | Sombra | **Katana Vitral** (katana): cada golpe muda de elemento (Fogo → Gelo → Raio → Luz) |
| 78 | **Carcereiro** | brutamontes de capuz com chaves e uma bola com corrente (48×48) | Bola com Corrente (área em círculo) · **Fechar a Cela** (prende-te numa cela: parte a porta) · Chicote | Luz | **Manoplas do Carcereiro** (manoplas): o 6.º golpe prende o inimigo 1 s com uma corrente |
| 79 | **Comandante dos Cavaleiros Caídos** | cavaleiro negro com estandarte rasgado (48×48) | Estandarte (dá força às Armaduras Vivas) · Lança de Cavalaria · Carga · Grito de Comando | Luz | **Lança do Comandante** (lança): +10% ATQ aos teus companheiros |

---

## 7. Povoações

### 7.1 Mercado Fantasma (andar 72) — só à noite
À noite, os **fantasmas cidadãos** voltam à vida de antes: a praça enche-se de bancas com velas, música de
caixa de música, fantasmas a passear. Ninguém sabe que morreu. Tem **hotel fantasma** (dormir dá sonhos com lore)
e **lojas** (aceitam ouro e **Lágrimas de Fantasma**).

| NPC | Quem é | O que faz |
|---|---|---|
| **Burgomestre Aldous** | presidente da câmara, fantasma de bigode | Missão do relógio (R8_02) |
| **Mortimer** | lojista fantasma | Itens antigos e raros; missão das cartas de amor (R8_15) |
| **Elise** | menina fantasma | Perdeu a boneca (R8_03) → **Gato Fantasma** |
| **Hugo** | padeiro fantasma | **Pão Fantasma** (R8_04): durante 10 s atravessas paredes finas |

### 7.2 Mosteiro da Ordem da Luz (andar 77)
Mosteiro de **monges caçadores de mortos-vivos**, encostado à catedral. É a ordem onde a **Irmã Célia**
(Ascendia) aprendeu. Claustro com sálvia, velas por todo o lado, sinos. Tem **celas** (dormir), **cristal**,
**loja** e **forja de Mitril** (purificação).

| NPC | Quem é | O que faz |
|---|---|---|
| **Abadessa Lumina** | líder da Ordem, foi mestra da Irmã Célia | Missões de consagrar e de libertar prisioneiros |
| **Irmão Bento** | ferreiro abençoado | Purifica Mitril (R8_12); encantamentos de Luz |
| **Irmã Clara** | vitralista | Restaurar os vitrais (R8_06) |
| **Caçador Van** | caçador de vampiros, chapéu de abas largas | Caça aos vampiros e à Condessa (R8_07, R8_08) |

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R8_01 | Consagrar | Abadessa Lumina | Consagrar 10 sepulturas no andar 73 | Água Benta ×20 · receita **Água Benta** |
| R8_02 | O Relógio Parado | Burgomestre Aldous | Consertar a Torre do Relógio (10 Engrenagens + 5 Lingote de Mitril) | Os fantasmas podem "seguir em frente" (cena) · o Mercado abre também de dia |
| R8_03 | A Boneca da Elise | Elise | Encontrar a boneca no Cemitério (andar 73) | A Elise segue em frente; o gato dela fica contigo: **Gato Fantasma** |
| R8_04 | Pão Fantasma | Hugo | 5 Farinha + 3 Ectoplasma | Receita **Pão Fantasma** |
| R8_05 | **O Passado de Gorvan** (história) | Mestre Gorvan | Ir às Catacumbas com o Gorvan, vencer o Colosso e encontrar a Sala da Equipa | Cena · o Gorvan fica teu companheiro · ❤️❤️❤️ Gorvan |
| R8_06 | Vitrais | Irmã Clara | 6 Vidro Colorido (Vidro Solar + gemas, na alquimia) | A catedral fica uma grande zona de luz |
| R8_07 | Caça ao Vampiro | Caçador Van | Encontrar 3 caixões de dia e acabar com os vampiros | **Besta de Mitril Abençoada** (épica, Luz) |
| R8_08 | A Condessa | Caçador Van (rank A) | Vencer a Condessa Sangria | Leque da Condessa · Rosa de Sangue |
| R8_09 | O Jardineiro | Hana | Vencer o Jardineiro e trazer as sementes que ele guardava | **Sementes de Rosa Negra** · Chapéu de Palha do Jardineiro |
| R8_10 | Livros Perdidos | Velho Fausto | Trazer 5 livros do Arquivo Selado (andar 75) | Página especial "O Reino Antes da Torre" · ❤️❤️ Fausto |
| R8_11 | Os Prisioneiros | Abadessa Lumina | Libertar os 4 prisioneiros vivos (andar 78) | Vão para Ascendia (um é cozinheiro: 5 receitas novas na estalagem) |
| R8_12 | Mitril Puro | Irmão Bento | 10 Minério de Mitril + 5 Água Benta | O Bento purifica o teu Mitril · **Anel de Mitril** (+10% RES) |
| R8_13 | O Banquete | (fantasmas do andar 79) | Sentar à mesa e ouvir o brinde até ao fim | Título *Convidado dos Mortos* · Cálice de Prata (decoração) |
| R8_14 | Os Sinos da Catedral | Abadessa Lumina | Tocar os 3 sinos pela ordem certa | **Bênção da Luz** (+10% de dano de Luz para sempre) |
| R8_15 | Cartas de Amor | Mortimer | Levar cartas entre dois fantasmas apaixonados (andares 72 e 79) | Reencontram-se e seguem em frente · Anel de Noivado Fantasma (presente) |

---

## 9. Masmorra escondida — Cripta da Rainha (andar 73)

| | |
|---|---|
| Entrada | Cripta da Rainha, à meia-noite, depois de consagrares 10 sepulturas (R8_01) |
| Sala 1 | **Corredor dos Retratos**: os retratos seguem-te com os olhos; quando os olhos ficam vermelhos, disparam |
| Sala 2 | **Salão de Baile Fantasma**: os fantasmas dançam; tens de atravessar a dançar ao ritmo (setas no chão); errar dá dano |
| Sala 3 | **Câmara da Rainha**: espelhos que mostram o reino antes da torre |
| Boss extra | **Rainha Sem Rei** (64×64): fantasma triste da rainha; ataques de lágrimas, espelhos que te copiam, e uma fase em que não ataca — só chora (falar com ela acaba a luta) |
| Recompensa | **Foice da Rainha Viúva** (arma secreta, foice): cada inimigo que matas liberta um fantasma aliado que luta 10 s · baú de ouro · página de lore extra "O Rei e a Rainha" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Lúcio Assombrado | fosso do andar 71 | noite | comum | 380 |
| Peixe-Fantasma | canais da Cidade Fantasma (72) | noite | incomum | 650 |
| Enguia da Cripta | água das catacumbas (74) | sempre | incomum | 700 |
| Peixe-Vitral | lago do mosteiro (77) | dia com sol | raro | 1 400 |
| Truta de Prata Negra | rio do poço (78) | sempre | raro | 1 500 |
| **Peixe da Lua Negra** (lendário) | Fonte Seca do 76 (só cheia na lua nova) | lua nova, meia-noite | lendário | 15 000 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Rosa Negra | missão R8_09 | 8 | Outono | presentes, Poção das Sombras |
| Sálvia Sagrada | Irmão Bento | 6 | Primavera, Verão | Água Benta |
| Abóbora | Hana (Outono) | 10 | **Outono** | cozinha, Noite dos Espíritos (lanternas) |
| Lírio da Lua | andar 73 | 7 (só floresce à noite) | todas | poções de MP |

### Animais
- **Gato Fantasma** (animal de estimação): missão R8_03. **Vê segredos**: paredes falsas e baús escondidos brilham quando ele está perto; à noite é quase invisível.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Noite Sem Lua | 1 noite em cada 7 | Mortos-vivos ×2; a névoa roxa sobe |
| Procissão Fantasma | sexta-feira à meia-noite, andar 72 | Uma fila de fantasmas atravessa a cidade; segui-la até ao fim leva a um tesouro |
| Eclipse Lunar | raro | A Condessa Sangria aparece de certeza |
| Névoa Densa | 20% | Visão 10 m e mais Maldição |
| Noite dos Espíritos | Outono, dia 26 (festival de Ascendia) | Os fantasmas do Reino ficam todos amigáveis por uma noite e dão presentes |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 30): calçada, terra de cemitério, chão de castelo ×2, muralha, parede de pedra ×2, árvore negra ×2, campa ×3,
  minério de mitril, ébano (cortável), rosa negra, baú, fogueira (lanterna sagrada), cristal, porta medieval, janela gótica, coluna, grade, vela grande
- [ ] **Peças especiais dos andares** (≈ 50)
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Condessa Sangria, O Jardineiro
- [ ] **8 guardiões**
- [ ] **Mini-boss** Lich Bibliotecário e **boss** Rei Sem Coroa
- [ ] **Boss da masmorra** Rainha Sem Rei
- [ ] **Armas**: 12 de Mitril + 2 únicas + 8 de guardião + 1 secreta = **23 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 24), **peixes** (6), **plantas** (4 × 4 fases)
- [ ] **NPCs**: Aldous, Mortimer, Elise, Hugo, fantasmas cidadãos (3 bases), Lumina, Bento, Clara, Van, 4 prisioneiros (+ retratos)
- [ ] **Animal**: Gato Fantasma
- [ ] **Conjunto de armadura** de Asa de Gárgula / Mitril (5 ícones)
