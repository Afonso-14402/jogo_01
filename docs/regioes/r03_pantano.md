# Região 3 — Pântano e Selva (andares 21–30)

> Estrutura igual às outras regiões. Bosses grandes (Serpente do Lodo e Hidra do Pântano) em `docs/BOSSES.md`.
> Esta região tem a **primeira grande escolha** da história (andar 24, ver `docs/HISTORIA.md`).

---

## 1. Identidade

| | |
|---|---|
| Tema | Pântanos verdes e selva quente: água parada, raízes, ruínas antigas de um povo-serpente |
| Sensação | Calor, humidade, perigo escondido debaixo de água e entre as folhas |
| Material das armas | **Aço** (tier 3) |
| Monstros fracos a | **Fogo** |
| Cores principais | verdes escuros `#165a4c` `#239063`, verde tóxico `#a2a947` `#d5e04b`, lama `#4c3e24` `#676633`, flores `#c32454` `#f68181` |
| Luz | sol filtrado e esverdeado, nevoeiro baixo de manhã, pirilampos à noite |
| Clima | Sol 30% · Chuva 45% · Trovoada 10% · Nevoeiro 15% |
| Música | `pantano_lodo`, `selva_tambores`, `aldeia_sssar`, `serpente_lodo`, `hidra` |
| Níveis | monstros 21–31; mini-boss 27; boss 33 |
| Mecânica da região | **Vegetação densa**: armas de corte (espada, katana, machado, foice) abrem caminho. **Água do pântano**: lenta e com sanguessugas. **Calor**: a Estamina recupera 20% mais devagar (beber água ou Água de Coco anula durante 5 min) |
| Animal de estimação | Sapinho |

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Minério de Ferro Negro | rochas no lodo (21, 25, 27) | Picareta de Ferro+ | Lingote de Aço (3 Ferro Negro + 1 Carvão) |
| Madeira de Mangue | 21, 26 | Machado | **madeira** da região (resiste à água: barcos, arcos) |
| Pele de Crocodilo | Crocodilo | drop | **couro** da região |
| Fibra de Liana | lianas (23, 27, 28) | lâmina | **fio** da região |
| Âmbar do Pântano | resina antiga (23, 27) | Picareta | **cristal** da região |
| Esmeralda | grutas da cascata (27) | Picareta | gema de **Veneno** |
| Lírio do Pântano | 21, 22 | à mão | Poção Purificadora, presentes |
| Musgo Medicinal | 26, 29 | à mão | Poção de Vida Média |
| Banana / Cacau / Café da Selva | 23, 28 | à mão | cozinha (e sementes para a quinta) |
| Coco | 26, 28 | atirar uma pedra ou bater | Água de Coco (anula o calor) |
| Escama de Lagarto | Homem-Lagarto | drop | armaduras leves, Poção de Escamas |
| Pétala Carnívora | Flor Carnívora | drop | alquimia, Bomba de Pólen |

---

## 3. Monstros

### 3.1 Sapo Venenoso
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, grupos de 2–4 |
| Andares | 21, 22, 26, 29 |
| Comportamento | Salta entre nenúfares; prefere atacar de longe com a língua |
| Ataques | **Língua**: puxa-te 2 m para ele (×0,9; aviso 0,4 s: abre a boca) · **Cuspe**: projétil que deixa uma poça de veneno 4 s · **Salto** de 5 m |
| Fraco / Imune | Fogo / Veneno |
| Drops | Pele de Sapo 50% · Muco de Sapo 30% |
| Elite | **Sapo Dourado**: veneno fortíssimo; deixa cair **Pele Dourada** (vale 800 ouro) |
| Animações | parado (4: papo a inchar), saltar (4), língua (4), cuspir (4), dano (1), morrer (4) |

### 3.2 Homem-Lagarto Renegado
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, grupos de 2–3 (um com arco) |
| Andares | 21, 23, 24 (se a aldeia for inimiga), 25 |
| Comportamento | Exilados da Aldeia Sssar. Lutam em formação: um bloqueia com escudo de carapaça, outro ataca, o arqueiro fica atrás |
| Ataques | **Lança** (×1,1; aviso 0,4 s) · **Escudo**: bloqueia à frente (ataca de lado) · **Grito de Guerra**: +20% ATQ aos aliados 8 s · **Flecha** (arqueiro) |
| Fraco / Resiste | Fogo, Gelo (o Frio dura o dobro: sangue frio) / Água |
| Drops | Escama de Lagarto 50% · Dente de Lagarto 20% · Lança Tribal de Aço 5% |
| Elite | **Campeão Renegado**: escudo e lança, e um grito que causa Medo |
| Animações | parado (4), mover (6), lança (4), escudo (2), grito (4), arco (4), dano (1), morrer (4) |

### 3.3 Flor Carnívora
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Torre** (não se mexe; usa os valores de Tanque) |
| Andares | 23, 27, 29 |
| Comportamento | Enraizada. Morde quem chega a 4 m; de longe cospe sementes. Às vezes parece uma flor normal fechada |
| Ataques | **Dentada** (×1,5; aviso 0,6 s: abre a boca e baba) · **Sementes**: 3 projéteis em leque · **Pólen**: área 3 m com Lentidão e Cegueira (aviso 0,8 s: incha) |
| Fraco / Resiste | Fogo (×2) / Água, Veneno |
| Drops | Pétala Carnívora 55% · Néctar 30% · Semente Carnívora 5% (planta de guarda para a quinta) |
| Elite | **Flor Gigante**: puxa-te com vinhas |
| Animações | fechada (1), abrir (4), parado (4), dentada (4), sementes (4), pólen (4), dano (1), morrer (5) |

### 3.4 Mosquito Gigante
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Voador + Fraco**, nuvens de 3–6 (o dobro à noite) |
| Andares | 21, 22, 23, 26 |
| Comportamento | Zumbe à tua volta, pica e afasta-se. O zumbido atrai outros mosquitos |
| Ataques | **Picada**: rouba 30% do dano que faz (aviso 0,3 s) |
| Fraco / Resiste | Fogo, Raio / — |
| Drops | Probóscide 40% · Asa de Mosquito 30% |
| Elite | **Mosquito Rainha**: chama 4 mosquitos |
| Animações | voar (2), picar (4), dano (1), morrer (3) |

### 3.5 Crocodilo
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 21, 22, 25, 26 |
| Comportamento | **Emboscada**: fica debaixo de água, só com os olhos de fora. Ataca quando passas na margem |
| Ataques | **Dentada**: agarra-te 1,5 s (×1,6; aviso 0,5 s: os olhos afundam) · **Rodopio** (se te agarrou: dano por segundo; carrega nos botões para soltar) · **Cauda**: área atrás dele |
| Fraco / Resiste | Fogo, Raio / Físico por cima (−20%) |
| Drops | Pele de Crocodilo 55% · Dente de Crocodilo 30% · Carne 40% |
| Elite | **Crocodilo Albino**: branco, mais rápido, raro |
| Animações | olhos (2), emergir (4), parado (4), mover (4), dentada (4), rodopio (4), cauda (4), dano (1), morrer (4) |

### 3.6 Macaco Ladrão
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, **cobarde**, grupos de 2–3 |
| Andares | 23, 27, 28 |
| Comportamento | Desce das árvores, **rouba ouro** (5% do teu ouro, até 200) e foge para as copas a rir. Atira cocos de cima |
| Ataques | **Roubo** (aviso 0,3 s) · **Coco**: projétil, 10% Atordoado · **Guincho**: chama os amigos |
| Fraco / Resiste | Fogo / — |
| Drops | Pelo de Macaco 40% · Banana 30% · **o ouro que roubou ×1,2** |
| Elite | **Macaco Prateado**: bate no peito (+30% ATQ) e luta em vez de fugir |
| Animações | parado (4), correr (6), roubar (4), atirar (4), rir (4), dano (1), morrer (4) |

### 3.7 Sanguessuga Gigante
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Fraco**, aparece na água |
| Andares | 22, 26, 29 |
| Comportamento | Escondida na água; salta e **agarra-se** a ti. Agarrada, tira HP até a sacudires (esquivar 2 vezes) |
| Ataques | **Agarrar** (aviso 0,5 s: salta da água) · **Sugar**: −2% HP por segundo |
| Fraco / Resiste | Fogo, **Sal** (item: atirar Sal mata logo) / — |
| Drops | Sanguessuga 40% (alquimia: Poção de Regeneração) |
| Elite | **Sanguessuga Rainha**: depois de sugar cresce e fica com mais vida |
| Animações | nadar (4), saltar (3), agarrada (2), dano (1), morrer (3) |

### 3.8 Bruxa do Pântano
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago**, sozinha |
| Andares | 22, 25, 29 |
| Comportamento | Fica longe com o caldeirão. Quando chegas perto, afunda-se na lama e aparece noutro sítio |
| Ataques | **Maldição** (Maldição 10 s; aviso 0,8 s: aponta o dedo) · **Bola de Lodo**: Lentidão · **Chamar Sapos** (2) · **Poção Atirada**: área de veneno 3 m |
| Fraco / Resiste | Fogo, Luz / Veneno, Sombra |
| Drops | Ingredientes de Bruxa 40% · Chapéu de Bruxa 10% (cosmético) · receita ao acaso 5% |
| Elite | **Bruxa Anciã**: transforma-te em sapo 3 s (só podes saltar) |
| Animações | parado (4: mexe o caldeirão), mover (4), maldição (4), atirar (4), afundar (4), aparecer (4), dano (1), morrer (5) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Mãe-Crocodilo Mandíbula** | andares 21, 22, 26, 3% | crocodilo velho 64×64 coberto de algas e conchas | Afunda e aparece noutro sítio; dentada que agarra 3 s; chama 3 crias | **Bolsa de Couro Real** (+10 espaços na mochila) · Dente de Mandíbula |
| **Rei Macaco Bobo** | andares 23, 28, 4% | macaco com coroa feita de cascas de banana e capa de folhas | Rouba e foge pelos ramos; atira frutas que explodem; tens de o encurralar | Coroa de Casca (cosmético) · título *Mais Bobo que o Rei* · 2 000 ouro (o que roubou a toda a gente) |

---

## 5. Os andares

### Andar 21 — Margem do Pântano
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 21 |
| Bioma | Água baixa castanha, juncos altos, passadiços de madeira velha, árvores de mangue, nevoeiro de manhã |
| Zonas | **Passadiços de Madeira** · **Juncal Alto** · **Cabana do Pescador** (abandonada) · **Ilhotas de Lama** |
| Mecânica especial | **Passadiços podres**: algumas tábuas partem quando passas (caes na água). **Água baixa**: andas mais devagar |
| Monstros | Sapo Venenoso, Mosquito Gigante, Crocodilo, Homem-Lagarto Renegado |
| Recursos | Mangue, Junco, Lírio do Pântano, Minério de Ferro Negro |
| Guardião | **Garça-Lança** |
| Segredo | Na Cabana do Pescador há um alçapão com a **Cana de Mangue** (cana boa) e o diário do pescador |
| Puzzle | **Passadiço partido**: trazer 5 tábuas (de caixotes partidos) para reparar a ponte até à ilhota do baú de prata |
| Página de lore 21 | *"O ar pesa. Até a janela azul parece embaciada."* |
| Desafios | Atravessar sem cair na água · Matar 3 crocodilos antes de eles saírem da água |
| Peças especiais | passadiço (inteiro e partido), cabana em estacas, juncos altos, árvore de mangue, caixotes |

### Andar 22 — Charco Venenoso
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 22 |
| Bioma | Água verde-fluorescente que borbulha, árvores mortas, ossadas de animais gigantes, nevoeiro verde |
| Zonas | **Lagoa Verde** · **Ossada** · **Nevoeiro Tóxico** · **Casa da Bruxa** |
| Mecânica especial | **Água tóxica**: tira 1% do HP por segundo. **Lírio Branco**: bater-lhe limpa a água à volta durante 20 s. Poção Purificadora dá imunidade 3 min |
| Monstros | Sapo Venenoso, Sanguessuga Gigante, Bruxa do Pântano, Mosquito Gigante, Crocodilo |
| Recursos | Lírio do Pântano, Muco de Sapo, Ossos, Ferro Negro |
| Guardião | **Lodo Tóxico** |
| Segredo | A **Casa da Bruxa** tem o livro com a receita da **Poção Purificadora** |
| Puzzle | **Caldeirão**: pôr 3 ingredientes na ordem que o livro diz (rima com pistas) abre a cave com um baú de ouro |
| Página de lore 22 | *"A água aqui foi envenenada de propósito. Para proteger alguma coisa? Ou alguém?"* |
| Desafios | Atravessar a Lagoa Verde sem Poção Purificadora · Vencer 3 bruxas |
| Peças especiais | árvore morta, costela gigante, caldeirão, casa torta da bruxa, lírio branco |

### Andar 23 — Selva Profunda
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 23 |
| Bioma | Selva densíssima, folhas enormes, lianas, flores coloridas, ruínas de pedra verde (pirâmide pequena), borboletas gigantes |
| Zonas | **Muralha Verde** · **Ruínas de Pedra Verde** · **Clareira das Borboletas** · **Rio Lento** |
| Mecânica especial | **Cortar vegetação** para abrir caminhos. **Borboletas gigantes**: se tocares numa, cura 10% (fogem). **Calor** forte |
| Monstros | Macaco Ladrão, Flor Carnívora, Homem-Lagarto Renegado, Mosquito Gigante |
| Recursos | Banana, Cacau, Café da Selva, Liana, Âmbar, Mangue |
| Guardião | **Pantera de Jade** |
| Segredo | Nas ruínas, uma escadaria escondida atrás de vinhas leva ao **Ídolo de Jade** (missão R3_15) e à entrada da masmorra escondida |
| Puzzle | **Pedras dos animais**: carregar em 4 pedras (macaco, sapo, lagarto, pássaro) pela ordem do mural |
| Página de lore 23 | *"Um povo de serpentes construiu isto. As serpentes também tinham uma janela azul, pintada nas paredes."* |
| Desafios | Atravessar a Muralha Verde em 2 min · Tocar em 5 borboletas |
| Peças especiais | folhas gigantes, lianas, pirâmide pequena de pedra verde, mural, pedras com animais |

### Andar 24 — Aldeia dos Homens-Lagarto
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 24 |
| Bioma | Lagoa grande com cabanas de estacas, totens pintados, fogueiras, canoas. Do outro lado, o acampamento dos renegados |
| Zonas | **Estacas** (aldeia) · **Lagoa Sagrada** · **Campo de Treino** · **Acampamento Renegado** |
| Mecânica especial | **A Escolha** (história): a Guilda manda expulsar os Homens-Lagarto (missão "Ordem da Guilda"); o Chefe Ssark pede ajuda contra os renegados. Ver `docs/HISTORIA.md` |
| Monstros | Homem-Lagarto Renegado, Crocodilo, Sapo Venenoso, Mosquito Gigante |
| Recursos | Mangue, Escama de Lagarto, peixes |
| Povoação | **Aldeia Sssar** (secção 7.1) — se ajudares a aldeia |
| Guardião | **Totem Vivo de Sssar** |
| Segredo | No fundo da Lagoa Sagrada (Poção de Respirar) está a **Escama do Primeiro Rei** (acessório: imune a Veneno) |
| Puzzle | **Canoas**: levar 3 canoas até à margem certa para fazer uma ponte (só se a aldeia for amiga; senão é preciso lutar) |
| Página de lore 24 | *"Os Homens-Lagarto chamam-nos 'os da janela'. Já viram muitos de nós. Nenhum voltou para casa."* |
| Desafios | Vencer o Campeão Renegado num duelo · Ganhar a corrida de canoas |
| Peças especiais | cabana de estacas, totem, canoa, fogueira tribal, paliçada |

### Andar 25 — Templo Afundado 💀
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 25 |
| Bioma | Templo de pedra verde meio debaixo de água; estátuas de serpentes; salas alagadas com luz a entrar por buracos do teto |
| Zonas | **Escadaria Submersa** · **Pátio das Serpentes** · **Salas Alagadas** · **Altar Inundado** (arena) |
| Mecânica especial | **Nível da água**: alavancas sobem ou descem a água nas salas. Debaixo de água andas devagar e não podes esquivar |
| Monstros | Crocodilo, Homem-Lagarto Renegado, Bruxa do Pântano, Sanguessuga Gigante |
| Recursos | Ferro Negro, Âmbar, Esmeralda (rara) |
| Mini-boss | **Serpente do Lodo** (ver `docs/BOSSES.md`) → arma única **Língua de Serpente** (lança) |
| Segredo | Baixar a água da sala norte revela uma porta com o **Anel da Serpente** (+10% velocidade de ataque) |
| Página de lore 25 | *"A serpente guardava um ovo de pedra. Dentro, uma janela azul pequenina. Partiu-se quando lhe toquei."* |
| Desafios | Vencer a Serpente com a sala cheia de água · Resolver as salas sem morrer afogado |
| Peças especiais | estátua de serpente, coluna de templo, alavanca de água, escadaria submersa, altar |

### Andar 26 — Mangue das Raízes
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 26 |
| Bioma | Floresta de mangue: raízes gigantes em arco por cima da água, canais, garças, uma vila de sapos em nenúfares gigantes |
| Zonas | **Raízes Altas** · **Canais** · **Vila Coaxa** (povoação) · **Ilha das Garças** |
| Mecânica especial | **Maré**: a água sobe e desce a cada 6 horas de jogo. Na **maré baixa** aparecem caminhos de lama e tesouros; na **alta** só há raízes e barco |
| Monstros | Sapo Venenoso, Crocodilo, Sanguessuga Gigante, Mosquito Gigante |
| Recursos | Mangue, Musgo Medicinal, Coco, peixes |
| Povoação | **Vila Coaxa** (secção 7.2) |
| Guardião | **Caranguejo-Violinista Gigante** |
| Segredo | Na maré baixa da madrugada aparece um **barco afundado** com um baú de ouro |
| Puzzle | **Eclusas de raízes**: com a maré a subir, abrir 3 comportas para encher o canal seco e passar de barco |
| Página de lore 26 | *"A torre respira. A maré sobe e desce como um peito a dormir."* |
| Desafios | Atravessar na maré alta sem barco · Apanhar 3 tesouros numa só maré baixa |
| Peças especiais | raiz de mangue em arco, nenúfar gigante, casas de sapo, comporta de raízes, barco afundado |

### Andar 27 — Cascata Esmeralda
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 27 |
| Bioma | Um lago verde-esmeralda com cinco cascatas altas, arco-íris, rochas cobertas de musgo, grutas atrás das quedas de água |
| Zonas | **Lago Esmeralda** · **As Cinco Cascatas** · **Grutas por Trás** · **Miradouro** |
| Mecânica especial | **Grutas atrás das cascatas**: cada uma tem um tesouro ou um inimigo. **Arco-íris** (12:00–14:00 com sol) mostra um símbolo na parede |
| Monstros | Macaco Ladrão, Flor Carnívora, Homem-Lagarto Renegado, Mosquito Gigante |
| Recursos | **Esmeralda**, Âmbar, Liana, Ferro Negro |
| Guardião | **Ninfa da Cascata** |
| Segredo | O símbolo do arco-íris diz qual das cascatas tem a **6.ª gruta** escondida: a **Fonte Esmeralda** (bebida que dá +5% HP máx. para sempre, uma vez) |
| Puzzle | **Pedras flutuantes**: saltar por pedras que afundam ao ritmo das cascatas |
| Página de lore 27 | *"Bebi da fonte e senti-me mais forte. A janela azul disse: 'Bónus permanente.' Até a natureza é um menu."* |
| Desafios | Entrar nas 6 grutas · Vencer a Ninfa sem sair da água |
| Peças especiais | cascata alta, rocha com musgo, gruta atrás de cascata, pedra flutuante, miradouro de madeira |

### Andar 28 — Copas das Árvores
| | |
|---|---|
| Tamanho / Nível | 240×240 m, sobretudo **lá em cima** (30 m de altura) · nível 28 |
| Bioma | O topo da selva: plataformas de madeira, pontes de corda, ninhos gigantes, flores no alto, o chão escuro lá em baixo |
| Zonas | **Refúgio das Copas** (povoação) · **Pontes Suspensas** · **Ninho Gigante** · **Chão da Selva** (lá em baixo) |
| Mecânica especial | **Tirolesas** entre árvores (depois da missão R3_10). **Cair** leva-te ao Chão da Selva, cheio de Flores Carnívoras e Crocodilos (e com tesouros) |
| Monstros | Macaco Ladrão, Mosquito Gigante, Flor Carnívora (no chão), Bruxa do Pântano |
| Recursos | Banana, Cacau, Café, Liana, ovos de pássaro |
| Povoação | **Refúgio das Copas** (secção 7.3) |
| Guardião | **Grande Bugio** |
| Segredo | No Ninho Gigante há um ovo de pássaro gigante: devolvê-lo ao ninho certo (há 3) dá a **Pena Arco-Íris** (cosmético: chapéu) |
| Puzzle | **Pontes**: rodar 3 plataformas giratórias para ligar as pontes até ao ninho |
| Página de lore 28 | *"Lá de cima vi o teto da torre. Não, não era teto. Era o fundo do andar seguinte."* |
| Desafios | Atravessar sem cair · Usar todas as tirolesas |
| Peças especiais | plataforma de árvore, ponte de corda, tirolesa, ninho gigante, plataforma giratória |

### Andar 29 — Ninho das Flores Carnívoras
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 29 |
| Bioma | Um jardim selvagem e perigoso: flores carnívoras gigantes, vinhas com espinhos, uma cúpula natural de vinhas, pólen dourado no ar |
| Zonas | **Jardim Devorador** · **Estufa Natural** (cúpula) · **Pântano Florido** · **Coração do Ninho** |
| Mecânica especial | **Flores-armadilha**: algumas flores no chão fecham-se e prendem-te (carregar nos botões). **Pólen tonto**: nuvens douradas que **trocam os controlos** durante 3 s |
| Monstros | Flor Carnívora, Sapo Venenoso, Bruxa do Pântano, Sanguessuga Gigante |
| Recursos | Pétala Carnívora, Néctar, Musgo Medicinal, sementes raras |
| Guardião | **Dríade Corrompida** |
| Segredo | Na Estufa Natural vive o **Sapo Tenor** perdido (missão R3_06) |
| Puzzle | **Rega**: levar água em 3 regadores até 3 flores-porta, que se abrem e deixam passar |
| Página de lore 29 | *"As flores comem tudo o que cai dos andares de cima. Nada se perde na torre."* |
| Desafios | Atravessar o Jardim sem ser preso · Vencer a Dríade sem queimar as flores |
| Peças especiais | flor carnívora gigante, vinha com espinhos, cúpula de vinhas, flor-armadilha, regador |

### Andar 30 — Altar da Hidra 👑
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 30 |
| Bioma | Uma calçada de pedra antiga sobre o pântano até um lago ritual rodeado de braseiros e estátuas de cabeças de serpente |
| Zonas | **Calçada de Pedra** · **Lago Ritual** · **O Altar** (arena) |
| Mecânica especial | **Braseiros**: a Hidra faz crescer de novo as cabeças cortadas; queimar o pescoço (fogo, ou empurrá-la para um braseiro aceso) impede isso |
| Monstros | Crocodilo, Homem-Lagarto Renegado, Bruxa do Pântano |
| Recursos | Ferro Negro, Âmbar, Esmeralda |
| Boss | **Hidra do Pântano** (ver `docs/BOSSES.md`) → arma única **Arco da Hidra** (arco) |
| Depois do boss | **Dia da Subida**. A **Arena** de Ascendia abre a categoria Prata e a **Taberna** começa os minijogos |
| Página de lore 30 | *"Cortei uma cabeça e nasceram duas. A torre é assim: cada andar que venço dá-me mais perguntas."* |
| Desafios | Vencer sem deixar nascer nenhuma cabeça nova · Vencer em menos de 5 min |
| Peças especiais | calçada de pedra, braseiro grande, estátua de cabeça de serpente, altar no lago |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 21 | **Garça-Lança** | garça cinzenta gigante (48×48) com bico comprido como uma lança | Bicada-Lança (linha de 5 m) · Voo e Mergulho · Bater de Asas (vento que empurra) | Fogo, Raio | **Bico da Garça** (lança): +15% crítico |
| 22 | **Lodo Tóxico** | slime gigante verde-fluorescente (64×64) com ossos a boiar lá dentro | Onda Tóxica · Dividir-se (2 lodos médios) · Absorver (come os lodos pequenos e cresce) | Fogo | **Cajado Lodoso** (cajado): os projéteis deixam uma poça de veneno |
| 23 | **Pantera de Jade** | felino verde-escuro (48×48) com manchas que brilham | Desaparecer na vegetação · Salto com Garras · Rugido (Medo) | Fogo | **Garras de Jade** (manoplas): ataques pelas costas fazem ×2 |
| 24 | **Totem Vivo de Sssar** | totem de madeira com 3 cabeças esculpidas (64×64), acordado pelos renegados | Raios do Totem (Choque) · Rodar as cabeças (disparos em 3 direções) · Chamar Espíritos | Fogo | **Machado Totémico** (machado): matar um inimigo dá +5% ATQ por 10 s (acumula 3 vezes) |
| 26 | **Caranguejo-Violinista Gigante** | caranguejo laranja (64×64) com uma pinça enorme | Pinça Gigante (área à frente) · Bolhas (Encharcado) · Esconder no buraco (só sai na maré baixa) | Raio | **Pinça Maior** (espada grande): +20% DEF enquanto carregas o ataque |
| 27 | **Ninfa da Cascata** | espírito de água (48×48) com cabelo que é uma cascata | Jato de Água · Nevoeiro Curativo (cura-se 15%) · Ondas | Raio | **Arco Cascata** (arco): as flechas deixam o alvo Encharcado |
| 28 | **Grande Bugio** | macaco gigante (64×64) de pelo castanho e cara vermelha | Salto entre ramos · Atirar Troncos · Bater no Peito (as pontes abanam) | Fogo | **Martelo Bugio** (martelo): os ataques carregados atordoam sempre |
| 29 | **Dríade Corrompida** | mulher-planta (48×48) com vinhas e uma flor carnívora no lugar do cabelo | Vinhas (prendem) · Pólen (Cegueira) · Chamar Flores Carnívoras | Fogo | **Foice de Espinhos** (foice): 20% de causar Sangrar |

---

## 7. Povoações

### 7.1 Aldeia Sssar (andar 24) — dos Homens-Lagarto
Cabanas de estacas sobre a lagoa, totens pintados, canoas. Os Homens-Lagarto falam a sibilar ("Sssim, Jogador").
Tem **cabana de hóspedes** (dormir), **cristal** e **loja tribal**.
**Se escolheres a Guilda** (expulsá-los), a aldeia fica vazia e ocupada pelos renegados, e o Ssark só volta a aparecer
no andar 97 (Cidade dos Perdidos).

| NPC | Quem é | O que faz |
|---|---|---|
| **Chefe Ssark** | guerreiro velho e honrado, uma cicatriz no focinho | Missão "Os Renegados"; depois pode ser **companheiro** (tanque) |
| **Xamã Ilssa** | curandeira | Cura estados; ensina a **Poção de Escamas** (+DEF) |
| **Kesh** | jovem caçador, competitivo | Desafios de caça (R3_05) |
| **Zith** | mercadora | Escamas, armas tribais de aço, pimenta, Água de Coco |

### 7.2 Vila Coaxa (andar 26) — dos Homens-Sapo
Vila de **Homens-Sapo** comerciantes e cómicos, com casas em nenúfares gigantes e pontes de juncos.
À noite, o Coro dos Sapos canta. Tem **estalagem-nenúfar**, **cristal**, **loja** e **aluguer de barcos**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Barão Coaxim** | sapo gordo e rico que fala sempre em rimas | Compra tesouros caros; loja com itens raros depois da missão R3_07 |
| **Rã-Rã** | pescadora que pesca com a língua | Concurso de Pesca de Coaxa (R3_16) → **Sapinho** |
| **Doutor Girino** | inventor de poções esquisitas | Vende **Poções Surpresa** (efeito ao acaso) |
| **Coro dos Sapos** | 3 sapos cantores | Perderam o 4.º cantor (R3_06) |

### 7.3 Refúgio das Copas (andar 28)
Posto de exploradores de Ascendia no topo das árvores: plataformas, redes, um telescópio.
Tem **cama**, **cristal** e **loja**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Vera Liana** | cartógrafa | Paga ouro pela % de andares explorados; missão R3_09 |
| **Tom Tirolesa** | construtor | Missão das tirolesas (R3_10) |
| **Irmã Nara** | enfermeira da Igreja de Ascendia | Vende poções e cura estados |

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R3_01 | Repara os Passadiços | Quadro da Guilda | Entregar 20 Mangue | 300 ouro · atalho no andar 21 |
| R3_02 | **Ordem da Guilda** (história) | Mestre Gorvan | **Escolha**: expulsar os Homens-Lagarto **ou** defender a aldeia | ver `docs/HISTORIA.md` e `docs/MISSOES.md` |
| R3_03 | Os Renegados | Chefe Ssark | Derrotar o Campeão Renegado e o Totem Vivo | **Ssark** como companheiro · Lança de Ssark (rara) |
| R3_04 | Escamas Fortes | Xamã Ilssa | 10 Escama de Lagarto + 5 Lírio do Pântano | Receita Poção de Escamas |
| R3_05 | Caçada com o Kesh | Kesh | Caçar 10 sapos antes do Kesh | Arco Tribal de Aço (raro) |
| R3_06 | O Quarto Cantor | Coro dos Sapos | Encontrar o Sapo Tenor (andar 29) | Concerto à noite · **Ocarina** (tocar atrai peixes raros) |
| R3_07 | A Riqueza do Barão | Barão Coaxim | Trazer o Ídolo de Jade (ou 3 tesouros raros) | 3 000 ouro · loja de itens raros do Barão |
| R3_08 | Poções Surpresa | Doutor Girino | Beber 5 Poções Surpresa e sobreviver | Título *Cobaia* · receita Poção Arco-Íris (todos os bónus pequenos) |
| R3_09 | Mapa da Selva | Vera Liana | Explorar 100% dos andares 23 e 28 | **Bússola de Explorador** (mostra segredos a 20 m no mapa) · 1 500 ouro |
| R3_10 | Tirolesas | Tom Tirolesa | 30 Liana + 10 Lingote de Aço | Tirolesas ativas no andar 28 |
| R3_11 | Mandíbula | Capitã Freya (rank C) | Derrotar a Mãe-Crocodilo Mandíbula | Bolsa de Couro Real · 1 200 ouro |
| R3_12 | O Rei Bobo | Rook | Recuperar o ouro do Rei Macaco Bobo | 2 000 ouro · **escolha**: dar metade ao Rook (❤️❤️ Rook) ou ficar com tudo |
| R3_13 | Café da Selva | Lucien | Trazer 10 Café da Selva | Receita Café Forte (+velocidade de ataque) |
| R3_14 | Chocolate! | Hana | Trazer 5 Cacau | Sementes de Cacau · receita Chocolate Quente |
| R3_15 | O Ídolo de Jade | Velho Fausto | Entregar-lhe o Ídolo de Jade (em vez de o vender) | Página de lore extra "O Povo-Serpente" · ❤️ Fausto |
| R3_16 | Concurso de Pesca de Coaxa | Rã-Rã | Ganhar o concurso (maior peixe em 5 min) | **Sapinho** (animal de estimação) |

---

## 9. Masmorra escondida — Santuário do Jaguar (andar 23)

| | |
|---|---|
| Entrada | Atrás das vinhas das Ruínas de Pedra Verde, depois do puzzle das pedras dos animais |
| Sala 1 | **Corredor dos Dardos**: armadilhas de dardos venenosos ativadas por placas no chão |
| Sala 2 | **Sala da Água que Sobe**: a sala enche-se; sobe por plataformas antes de a água chegar ao teto |
| Sala 3 | **Sala do Ídolo**: ao apanhar o ídolo, uma **pedra gigante** rola atrás de ti — foge! |
| Boss extra | **Jaguar de Pedra Solar**: estátua de jaguar dourado (64×64) que corre pelas paredes; raios de sol entram pelos buracos do teto e queimam onde batem |
| Recompensa | **Katana Garra-do-Sol** (arma secreta, katana): o ataque carregado solta uma onda de **Luz** (×1,5 contra mortos-vivos) · baú de ouro · página de lore extra "O Sol Pintado" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Bagre do Lodo | andar 21 | noite | comum | 60 |
| Enguia de Lama | andar 22 | sempre | comum | 55 |
| Piranha | rio do andar 23 | dia | incomum | 110 |
| Pirarucu | canais do andar 26 | maré alta | raro | 300 |
| Peixe-Arco-Íris | lago do andar 27 | com sol, 12:00–14:00 | raro | 350 |
| **O Velho Bigodes** (lendário) | andar 26 | maré alta, à noite, com chuva | lendário | 3 500 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Cacau | missão R3_14 | 10 (árvore pequena, dá sempre) | Verão, Outono | Chocolate |
| Café da Selva | Zith | 8 (arbusto, dá sempre) | Verão | Café Forte |
| Bananeira | Refúgio das Copas | 14 (árvore) | Verão | cozinha |
| Pimenta da Selva | Zith | 6 | Verão | cozinha picante (+ATQ) |
| Lírio do Pântano | andar 21 | 5 (precisa de água: plantar junto ao rio da quinta) | Primavera, Verão | poções, presentes |

### Animais
- **Sapinho** (animal de estimação): ganhar o concurso de pesca de Coaxa. Os inimigos em que ele salta ficam **envenenados**.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Chuva Torrencial | com trovoada | A água sobe; tudo fica Encharcado; mais crocodilos |
| Floração | Primavera | As Flores Carnívoras dormem de dia mas soltam mais pólen |
| Nuvem de Mosquitos | noites de Verão | Mosquitos ×3; o fumo das fogueiras afasta-os |
| Maré Viva | lua cheia, andar 26 | Maré mais baixa do que nunca: aparecem 3 tesouros extra |
| Festa na Aldeia | 1 vez por estação (se a aldeia for amiga) | Corrida de canoas, comida e uma loja especial em Sssar |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 28): água de pântano, lama, chão de selva ×2, passadiço, raiz, árvore de mangue, palmeira, árvore da selva ×2,
  folhas gigantes, lianas, juncos, nenúfar, rocha com musgo ×2, minério de ferro negro, árvore cortável, erva, baú, fogueira, cristal, ponte de corda, vegetação cortável
- [ ] **Peças especiais dos andares** (≈ 45)
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Mãe-Crocodilo Mandíbula, Rei Macaco Bobo
- [ ] **8 guardiões**
- [ ] **Mini-boss** Serpente do Lodo e **boss** Hidra do Pântano
- [ ] **Boss da masmorra** Jaguar de Pedra Solar
- [ ] **Armas**: 12 de Aço + 2 únicas + 8 de guardião + 1 secreta = **23 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 24), **peixes** (6), **plantas** (5 × 4 fases)
- [ ] **NPCs**: Ssark, Ilssa, Kesh, Zith, Barão Coaxim, Rã-Rã, Doutor Girino, Coro dos Sapos, Vera Liana, Tom, Irmã Nara (+ retratos)
- [ ] **Animal**: Sapinho
- [ ] **Conjunto de armadura** de Pele de Crocodilo (5 ícones)
