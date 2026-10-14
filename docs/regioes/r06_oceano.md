# Região 6 — Oceano (andares 51–60)

> Estrutura igual às outras regiões. Bosses grandes (Capitão Esqueleto e Leviatã) em `docs/BOSSES.md`.
> No **Navio Fantasma** (andar 53) o **Kai desaparece** (ver `docs/HISTORIA.md`).

---

## 1. Identidade

| | |
|---|---|
| Tema | Um mar tropical engolido pela torre: praias, ilhas, piratas, recifes de coral, cidades debaixo de água, o abismo |
| Sensação | Liberdade de navegar, aventura de piratas, maravilha e medo do fundo do mar |
| Material das armas | **Coral Abissal** (tier 6) |
| Monstros fracos a | **Raio** |
| Cores principais | turquesas `#0eaf9b` `#30e1b9` `#8ff8e2`, azuis profundos `#0b5e65` `#323353` `#484a77`, areia `#fdcbb0`, coral `#f68181` `#ed8099` |
| Luz | sol brilhante com reflexos na água; debaixo de água raios de luz ondulantes (*caustics*); no abismo, escuridão com luzes vivas |
| Clima | Sol 55% · Chuva 20% · Tempestade no mar 15% · Nevoeiro 10% |
| Música | `praia`, `porto_piratas`, `debaixo_de_agua`, `abismo`, `capitao_esqueleto`, `leviata` |
| Níveis | monstros 51–61; mini-boss 57; boss 63 |
| Mecânica da região | **Barco** (navegar entre ilhas). **Debaixo de água**: barra de **Ar** de 30 s; sem ar perdes 5% do HP por segundo; **bolhas de ar** enchem a barra; andas e atacas 30% mais devagar; ficas sempre **Encharcado** (Raio faz-te ×1,5 também a ti!). **Marés** nas praias |
| Animal de estimação | Polvo Bebé |
| Montada | **Cavalo-marinho Gigante** (só na água) |

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Coral Abissal | recifes fundos (54, 57, 58) | Picareta de Gelo Eterno+ | Barra de Coral Abissal (3 Coral + 1 Sal, polido na forja) |
| Madeira de Naufrágio | destroços (51, 52, 53, 56) | Machado | **madeira** da região (barcos, arcos) |
| Pele de Tubarão | Homem-Tubarão | drop | **couro** da região |
| Fio de Alga-Prata | algas brilhantes (56) | lâmina | **fio** da região |
| Pérola | ostras (54, 57) | abrir ostras (Faca de Mergulho) | **cristal** da região |
| Pérola Negra | ostras gigantes (raro) | idem | joalharia de luxo, presentes |
| Sal Marinho | rochas da maré (51) | à mão | cozinha, polir coral |
| Alga Doce | 54, 56 | à mão | cozinha, comida do Cavalo-marinho |
| Anémona | 54, 59 | à mão | alquimia (Poção de Respirar) |
| Concha Rara | praias (51) e recife (54) | à mão | coleção, decoração, presentes |
| Gel Elétrico | Alforreca Elétrica | drop | engenhocas (baterias) |
| Moeda Antiga | Pirata Esqueleto | drop | vale 50 ouro; coleção |

---

## 3. Monstros

### 3.1 Caranguejo Gigante
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 51, 52, 54, 55 |
| Comportamento | Anda **de lado**. A carapaça da frente protege-o: ataca-o de lado |
| Ataques | **Pinça**: agarra-te 1,5 s (aviso 0,6 s: abre a pinça) · **Bolhas**: Encharcado · **Esconder**: DEF ×3 durante 3 s |
| Fraco / Resiste | Raio, Martelo / Físico de frente (−40%) |
| Drops | Carapaça de Caranguejo 50% · Carne de Caranguejo 45% · Pinça 20% |
| Elite | **Caranguejo Ermitão**: usa um crânio gigante como concha |
| Animações | parado (4), andar de lado (4), pinça (4), bolhas (4), esconder (2), dano (1), morrer (4) |

### 3.2 Sereia Sombria
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago** |
| Andares | 51 (noite), 54, 56, 57 (fora da cidade), 59 |
| Comportamento | Sentada nas rochas ou a nadar. Canta para te puxar para a água |
| Ataques | **Canto**: durante 2 s és puxado devagar na direção dela (aviso 0,8 s: abre os braços) · **Bola de Água**: Encharcado · **Onda**: empurra |
| Fraco / Resiste | Raio / Água |
| Drops | Escama de Sereia 45% · Pérola 15% · Lágrima de Sereia 5% |
| Elite | **Sereia Abissal**: o canto também causa Medo |
| Animações | parado (4), nadar (4), cantar (4), atacar (4), mergulhar (4), dano (1), morrer (4) |

### 3.3 Homem-Tubarão
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, 2–3 |
| Andares | 52 (mar), 54, 56, 58 |
| Comportamento | Muito rápido na água; na terra salta da água para atacar. Fica em **frenesim** se o alvo estiver a sangrar |
| Ataques | **Dentada**: Sangrar · **Investida Aquática** em linha · **Frenesim**: +30% velocidade se o alvo sangrar |
| Fraco / Resiste | Raio / Água |
| Drops | Pele de Tubarão 55% · Dente de Tubarão 30% |
| Elite | **Tubarão-Martelo**: a investida atordoa |
| Animações | nadar (4), saltar (4), parado (4), dentada (4), investida (4), dano (1), morrer (4) |

### 3.4 Pirata Esqueleto
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, 3–4 |
| Andares | 52 (ilhas), 53, 55 |
| Comportamento | Gritam "Arrr!" e atacam em grupo. Um tem **pistola** (tiro forte e lento a carregar) |
| Ataques | **Sabre** (combo de 2) · **Pistola**: projétil forte (×1,8; aviso 1,2 s: aponta e brilha) · **Bomba de Pólvora** (área) |
| Fraco / Imune | Luz, Raio, Martelo / Veneno |
| Drops | Osso 50% · Moeda Antiga 40% · Chapéu de Pirata 5% · Mapa do Tesouro 3% |
| Elite | **Pirata Contramestre**: dá ordens; os piratas perto atacam mais depressa |
| Animações | parado (4), mover (6), sabre (4), pistola (6), atirar bomba (4), dano (1), morrer (4: desfaz-se) |

### 3.5 Polvo
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Normal** |
| Andares | 54, 56, 57, 58 |
| Comportamento | **Camuflado** no coral (muda de cor). Agarra quem passa |
| Ataques | **Tentáculos**: prende-te 2 s · **Tinta**: nuvem que causa Cegueira · **Camuflagem**: fica invisível 3 s |
| Fraco / Resiste | Raio / — |
| Drops | Tentáculo 50% · Tinta de Polvo 30% |
| Elite | **Polvo Gigante**: 2 agarrões ao mesmo tempo |
| Animações | camuflado (2), parado (4), mover (4), tentáculos (5), tinta (4), dano (1), morrer (4) |

### 3.6 Alforreca Elétrica
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Fraco + Voador** (flutua), grupos de 3–6 |
| Andares | 54, 56, 58 (e praias à noite) |
| Comportamento | Flutuam devagar na tua direção; brilham antes de dar choque |
| Ataques | **Choque**: Choque (salta para quem está perto, incluindo tu!) |
| Fraco / Imune | Gelo / **Raio** |
| Drops | Gel Elétrico 50% · Tentáculo Fino 30% |
| Elite | **Alforreca Rainha**: choque em área grande |
| Animações | flutuar (4), brilhar (2), choque (3), dano (1), morrer (3) |

### 3.7 Peixe-Lanterna
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago**, sozinho |
| Andares | 58, 59 |
| Comportamento | No escuro só se vê a luz da antena. A luz **parece um baú ou um tesouro** (é uma isca) |
| Ataques | **Isca de Luz**: atrai-te (ilusão) · **Dentada Enorme** (×2,0; aviso 0,7 s: abre a boca toda) |
| Fraco / Resiste | Raio, Luz / Sombra |
| Drops | Lanterna Abissal 40% (luz de 6 m) · Dente Abissal 25% |
| Elite | **Peixe-Lanterna Rei**: a luz cega |
| Animações | nadar (4), isca (2), dentada (4), dano (1), morrer (4) |

### 3.8 Serpente Marinha Jovem
| | |
|---|---|
| Tamanho | 64×64 |
| Tipo | **Tanque**, sozinha |
| Andares | 52 (mar), 56, 59 |
| Comportamento | Nada à volta do barco ou de ti; aparece e desaparece |
| Ataques | **Mordida** · **Constrição**: enrola-se à tua volta (dano por segundo; esquivar 3 vezes para soltar) · **Jato de Água** |
| Fraco / Resiste | Raio / Água |
| Drops | Escama de Serpente Marinha 50% · Barbatana 25% |
| Elite | **Serpente das Tempestades**: aparece em tempestades e atrai raios |
| Animações | nadar (4), emergir (4), mordida (4), constrição (4), jato (4), dano (1), morrer (5) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Caranguejo Rei Pinça-de-Ouro** | andares 51, 54, 3% | caranguejo dourado (64×64) com coroa e uma pinça de ouro maciço | Agarra e atira; esconde-se na areia; chama caranguejos | **Pinça de Ouro** (vale 6 000 ouro ou decoração) · Coroa de Pinça (cosmético) |
| **Barba-Lodo** | andares 52, 53, noites de nevoeiro, 5% | pirata fantasma com barba de algas e um pequeno navio fantasma | Luta no convés do navio dele; o navio dispara canhões; chama a tripulação | **Chapéu de Barba-Lodo** (+5% de dano no mar) · **Bússola Amaldiçoada** (aponta para tesouros enterrados da região) |

---

## 5. Os andares

### Andar 51 — Praia das Conchas
| | |
|---|---|
| Tamanho / Nível | 260×200 m · nível 51 |
| Bioma | Areia branca, mar turquesa, palmeiras, rochas com poças da maré, um barco destruído na areia, conchas por todo o lado |
| Zonas | **Areal Branco** · **Rochas da Maré** · **Palmeiral** · **Destroços do Barco** |
| Mecânica especial | **Maré**: a praia cresce e encolhe; com a maré baixa aparecem poças com conchas raras e caranguejos. **Conchas** para colecionar |
| Monstros | Caranguejo Gigante, Sereia Sombria (à noite nas rochas), Alforreca Elétrica (à noite na água) |
| Recursos | Sal Marinho, Concha Rara, Madeira de Naufrágio, Coco |
| Guardião | **Tartaruga-Marinha Anciã** |
| Segredo | Uma **garrafa com mensagem** na areia: um mapa do tesouro do Farol da Caveira (andar 52) |
| Puzzle | **Conchas-sino**: 5 conchas gigantes que soam quando lhes tocas; a ordem está desenhada no barco destruído |
| Página de lore 51 | *"O mar! Sentei-me na areia e chorei. Por um minuto esqueci-me de que estava dentro de uma torre."* |
| Desafios | Encontrar 10 conchas raras · Apanhar 5 caranguejos na maré baixa |
| Peças especiais | barco destruído, poças de maré, palmeira inclinada, concha gigante, garrafa |

### Andar 52 — Arquipélago
| | |
|---|---|
| Tamanho / Nível | 300×300 m (a maior parte é mar) · nível 52 |
| Bioma | Mar azul com cinco ilhas, um porto de casas coloridas em palafitas, um farol com uma caveira desenhada, gaivotas |
| Zonas | **Porto Arquipélago** (povoação) · **Ilhas Pequenas** (5) · **Farol da Caveira** · **Mar Aberto** |
| Mecânica especial | **Barco** (missão R6_01): navegar entre ilhas; **correntes** que te levam; **tempestades** no mar aberto |
| Monstros | Pirata Esqueleto (ilhas), Homem-Tubarão (mar), Serpente Marinha Jovem (mar), Caranguejo Gigante |
| Recursos | Madeira de Naufrágio, Coco, peixes, Moeda Antiga |
| Povoação | **Porto Arquipélago** (secção 7.1) |
| Guardião | **Gaivota Gigante Ladra** |
| Segredo | O tesouro da garrafa (andar 51) está enterrado ao pé do **Farol da Caveira** |
| Puzzle | **Farol**: acender o farol e rodar o espelho para iluminar uma ilha que só aparece com luz (ilha da névoa) |
| Página de lore 52 | *"Os piratas daqui eram Jogadores. Desistiram de subir e ficaram a roubar os que subiam."* |
| Desafios | Visitar as 5 ilhas num só dia · Vencer uma Serpente Marinha a partir do barco |
| Peças especiais | casas em palafitas, cais, estaleiro, farol, ilha pequena, barco do jogador |

### Andar 53 — Navio Fantasma
| | |
|---|---|
| Tamanho / Nível | 200×200 m (o navio tem 80 m) · nível 53 |
| Bioma | Um enorme galeão encalhado num banco de areia, envolto em nevoeiro verde; velas rasgadas, luzes de fantasmas, mar parado |
| Zonas | **Convés** · **Porões** (3 níveis) · **Cabine do Capitão** · **Mar de Nevoeiro** |
| Mecânica especial | **O navio balança**: o chão inclina de um lado para o outro e os barris rolam. **Fantasmas de Jogadores antigos** presos a bordo: falar com eles e libertá-los (história) |
| Monstros | Pirata Esqueleto, Polvo (porões inundados), Alforreca Elétrica, Sereia Sombria (à volta) |
| Recursos | Madeira de Naufrágio, Moeda Antiga, Ectoplasma |
| NPCs | **5 fantasmas de Jogadores** (nº 312, nº 1 450, nº 3 377, nº 6 001, nº 8 820) |
| Guardião | **O Imediato Fantasma** |
| Segredo | O **diário de bordo** na Cabine do Capitão fala de "Jogadores que subiam para o Administrador" — e o último registo é do **Kai** |
| Puzzle | **Leme**: rodar o leme para inclinar o navio e fazer rolar um barril até partir uma porta |
| Página de lore 53 | *"Os fantasmas do navio têm números como eu. O mais novo tinha o nº 8 820. Ainda não percebeu que morreu."* |
| Desafios | Libertar os 5 fantasmas · Atravessar o porão sem ser atingido por barris |
| Peças especiais | galeão (casco, mastros, velas rasgadas), barril, leme, porão inundado, lanterna fantasma |

### Andar 54 — Recife de Coral
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 54 |
| Bioma | Recife colorido em água baixa e transparente; peixes de todas as cores; uma lagoa azul; um paredão que cai para o azul escuro |
| Zonas | **Recife Raso** · **Lagoa Azul** · **Vila das Pérolas** (povoação) · **Paredão** |
| Mecânica especial | **Mergulho** (Ar). **Coral vivo**: correr por cima corta (Sangrar). **Ostras**: abrir com a Faca de Mergulho dá pérolas |
| Monstros | Polvo, Alforreca Elétrica, Caranguejo Gigante, Homem-Tubarão, Sereia Sombria |
| Recursos | **Pérola**, Coral Abissal (no paredão), Alga Doce, Anémona, Concha Rara |
| Povoação | **Vila das Pérolas** (secção 7.2) |
| Guardião | **Peixe-Leão Rei** |
| Segredo | Uma **ostra gigante** no fundo do paredão só abre ao ouvir uma canção (Concha do Mar, missão R6_10): **Pérola Negra** |
| Puzzle | **Correntes**: abrir 3 comportas de coral para mudar a corrente e chegar à gruta da lagoa |
| Página de lore 54 | *"Debaixo de água a janela azul fica verde. Acho que até a torre se molha."* |
| Desafios | Apanhar 10 pérolas num só mergulho · Atravessar o recife sem tocar no coral |
| Peças especiais | coral (3 cores), anémona, ostra gigante, casas da vila das pérolas, comporta de coral |

### Andar 55 — Gruta dos Piratas 💀
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 55 |
| Bioma | Enseada escondida que entra por uma gruta: túneis de contrabando, montes de ouro, canhões, um navio pirata atracado dentro da gruta |
| Zonas | **Enseada Escondida** · **Túneis do Contrabando** · **Sala do Tesouro** · **Cais do Capitão** (arena: o convés do navio atracado) |
| Mecânica especial | **Armadilhas piratas** (cordas, redes, barris explosivos). **Canhões** que podes usar. **Maré na gruta** |
| Monstros | Pirata Esqueleto, Caranguejo Gigante, Homem-Tubarão |
| Recursos | Moeda Antiga, Madeira de Naufrágio, Pólvora |
| Mini-boss | **Capitão Esqueleto** (ver `docs/BOSSES.md`) → arma única **Sabre do Afogado** (espada) |
| Segredo | A **Chave do Almirante** (abre a masmorra escondida do andar 56) está no cofre do Capitão |
| Página de lore 55 | *"O Capitão contava ouro que não podia gastar. A torre também conta: andares, Jogadores, mortes."* |
| Desafios | Vencer o Capitão usando os canhões · Apanhar o tesouro todo da Sala do Tesouro |
| Peças especiais | navio pirata (menor), canhão, montes de ouro, túnel de contrabando, barril explosivo |

### Andar 56 — Floresta de Algas
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 56 · **todo debaixo de água** |
| Bioma | Floresta de algas gigantes (kelp) a ondular, raios de sol lá de cima, lontras, um naufrágio antigo, uma bolha de ar enorme |
| Zonas | **Bolha de Ar** (zona segura dentro de uma bolha gigante) · **Algas Gigantes** · **Clareira das Lontras** · **Naufrágio Antigo** |
| Mecânica especial | **Debaixo de água** (Ar). **Bolhas de ar** espalhadas para respirar. **Algas que prendem** (cortá-las). **Correntes** que te levam |
| Monstros | Polvo, Homem-Tubarão, Alforreca Elétrica, Serpente Marinha Jovem |
| Recursos | **Fio de Alga-Prata**, Alga Doce, Madeira de Naufrágio |
| Guardião | **Dragão-Marinho Folhado** |
| Segredo | No **Naufrágio Antigo**, a porta do cofre abre com a **Chave do Almirante** (masmorra escondida) |
| Puzzle | **Lontras**: as lontras amigáveis trazem-te conchas; dar-lhes as conchas na ordem do tamanho abre uma gruta com o **ovo de polvo** (R6_15) |
| Página de lore 56 | *"As lontras brincam com coisas dos Jogadores: um relógio, um óculos, um sapato. Coisas do meu mundo."* |
| Desafios | Atravessar sem usar bolhas de ar · Encontrar 5 coisas do "mundo real" que as lontras têm |
| Peças especiais | alga gigante, bolha de ar gigante, naufrágio antigo, rocha do fundo, lontras (NPC animal) |

### Andar 57 — Cidade Submersa
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 57 · **debaixo de água** com cúpulas de ar |
| Bioma | Uma cidade de coral e conchas dentro de uma cúpula de ar gigante; à volta, ruínas de uma cidade mais antiga; um palácio de pérola |
| Zonas | **Portões de Coral** · **Coralina** (povoação, dentro da cúpula) · **Ruínas Antigas** · **Palácio de Pérola** |
| Mecânica especial | **Cúpulas de ar**: dentro não há barra de Ar. **Correntes-elevador**: colunas de água que te levam para cima e para baixo |
| Monstros | Polvo, Sereia Sombria, Homem-Tubarão (fora da cúpula) |
| Recursos | Coral Abissal, Pérola, Anémona |
| Povoação | **Coralina** (secção 7.3) |
| Guardião | **Golem de Coral** (defesa da cidade que enlouqueceu) |
| Segredo | As **Ruínas Antigas** debaixo da cidade têm murais de uma cidade humana: a cidade das sereias foi construída **por cima** de outro mundo engolido |
| Puzzle | **Correntes**: ligar 4 correntes-elevador para chegar ao topo do Palácio |
| Página de lore 57 | *"A Rainha das sereias disse: 'Os de cima caem. Nós apanhamos o que cai. Às vezes apanhamos Jogadores.'"* |
| Desafios | Visitar todas as lojas de Coralina · Vencer o Golem sem sair da cúpula |
| Peças especiais | cúpula de ar, casas de coral, palácio de pérola, coluna de corrente, ruína humana submersa |

### Andar 58 — Fossa Abissal
| | |
|---|---|
| Tamanho / Nível | 200×200 m de largura e **150 m de profundidade** · nível 58 |
| Bioma | Um abismo escuro no fundo do mar; só há luz das criaturas; no fundo, fontes quentes com luz vermelha e bichos estranhos |
| Zonas | **Borda da Fossa** · **Descida** · **Fundo Escuro** · **Fontes Hidrotermais** |
| Mecânica especial | **Escuridão total** (luz: Lanterna Abissal, Morceguinho, Capacete de Mineiro). **Pressão**: abaixo dos 100 m perdes 2% de HP por segundo sem o **Capacete de Escafandro** (missão R6_11) |
| Monstros | Peixe-Lanterna, Alforreca Elétrica, Homem-Tubarão, Polvo |
| Recursos | Coral Abissal (muito), Lanterna Abissal, Pérola Negra (rara) |
| Guardião | **Tamboril Abissal** |
| Segredo | Nas fontes quentes há um **ovo enorme** a pulsar: é um ovo de Leviatã (lore; não se pode apanhar) |
| Puzzle | **Luzes do fundo**: acender 5 corais luminosos para formar a constelação que está no Palácio de Pérola |
| Página de lore 58 | *"No fundo do mar ouvi o coração da torre. Bate devagar, uma vez por hora."* |
| Desafios | Chegar ao fundo sem luz · Vencer o Tamboril sem levar dentadas |
| Peças especiais | parede da fossa, fonte hidrotermal, coral luminoso, ovo gigante, rocha do abismo |

### Andar 59 — Templo do Mar
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 59 |
| Bioma | Templo branco e azul de pérola e coral, metade dentro e metade fora de água, com um jardim de anémonas e estátuas de tritões |
| Zonas | **Escadaria de Pérola** · **Sala das Marés** · **Jardim de Anémonas** · **Santuário** |
| Mecânica especial | **Marés do templo**: conchas-alavanca enchem uma sala e esvaziam outra (cheia = nadar com Ar; vazia = andar) |
| Monstros | Sereia Sombria, Serpente Marinha Jovem, Peixe-Lanterna, Polvo |
| Recursos | Pérola, Anémona, Coral Abissal |
| Guardião | **Guardião das Marés** |
| Segredo | No Santuário, uma **concha gigante** fala: é a voz do templo e dá uma bênção (+10% HP máx. até sair da região) |
| Puzzle | **Marés**: deixar cheias e vazias as salas certas para chegar ao Santuário |
| Página de lore 59 | *"O templo era para um deus do mar. Mas o deus também foi engolido. Agora só há o Leviatã."* |
| Desafios | Resolver as marés com menos de 10 mudanças · Atravessar o jardim sem tocar nas anémonas |
| Peças especiais | estátua de tritão, concha-alavanca, colunas de pérola, anémona gigante, concha falante |

### Andar 60 — Trono do Leviatã 👑
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 60 |
| Bioma | Mar aberto escuro com um redemoinho enorme; no centro, ruínas de um trono numa ilha de rocha; trovões |
| Zonas | **Mar Aberto** (no teu barco) · **Redemoinho** · **O Trono** (ilha-arena) |
| Mecânica especial | **Luta no mar**: começas no barco (canhões); depois na ilha do trono. O redemoinho puxa tudo para o centro |
| Monstros | Serpente Marinha Jovem, Homem-Tubarão |
| Boss | **Leviatã** (ver `docs/BOSSES.md`) → arma única **Tridente do Leviatã** (lança) |
| Depois do boss | **Dia da Subida**. Mas o **Kai continua desaparecido** (a história avança) |
| Página de lore 60 | *"O Leviatã não queria lutar. Tinha medo de mim. Ou da janela azul atrás de mim."* |
| Desafios | Vencer sem o barco afundar · Vencer em menos de 6 min |
| Peças especiais | redemoinho, ilha-trono, ruínas de trono, barco do jogador com canhões |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 51 | **Tartaruga-Marinha Anciã** | tartaruga enorme (64×64) com uma ilha de palmeiras nas costas | Onda (empurra) · Esconder · Chamar Caranguejos | Raio | **Martelo Casco de Tartaruga** (martelo): +15% DEF |
| 52 | **Gaivota Gigante Ladra** | gaivota enorme (48×48) com um lenço de pirata | **Rouba** um consumível · Mergulho · Bombardeio de Conchas | Raio | **Arco Gaivota** (arco): flechas 30% mais rápidas e +10% velocidade de movimento |
| 53 | **O Imediato Fantasma** | fantasma de pirata gigante (64×64) com uma âncora | Âncora (atira e puxa) · Correntes · Chamar Tripulação Fantasma | Luz | **Âncora do Imediato** (martelo): o ataque carregado puxa os inimigos à volta para ti |
| 54 | **Peixe-Leão Rei** | peixe-leão listrado (48×48) com barbatanas de espinhos | Espinhos Venenosos em leque · Investida · Camuflagem no coral | Raio | **Adaga Peixe-Leão** (adaga): 25% de causar Veneno |
| 56 | **Dragão-Marinho Folhado** | cavalo-marinho-dragão (64×64) coberto de "folhas" | Folhas-Lâmina · Jato de Água · Camuflagem nas algas | Raio | **Lança de Alga** (lança): as estocadas deixam o alvo Encharcado |
| 57 | **Golem de Coral** | golem de coral rosa e branco (64×64) | Socos de Coral · Muralha de Coral (bloqueia caminhos) · Regenerar (o coral cresce) | Raio, Martelo | **Manoplas de Coral** (manoplas): cada golpe cura 1% do HP |
| 58 | **Tamboril Abissal** | peixe-diabo enorme (64×64) com uma luz na antena | **Escuridão** (só se vê a luz dele) · Engolir (agarra) · Dentes | Raio, Luz | **Cajado Lanterna Abissal** (cajado): ilumina 8 m e +15% dano no escuro |
| 59 | **Guardião das Marés** | estátua de tritão feita de pérola (48×48) com tridente | Tridente · **Maré** (enche a sala de água) · Raio do Mar (Choque) | Sombra | **Foice das Marés** (foice): os golpes empurram uma onda à frente (área ×1,2) |

---

## 7. Povoações

### 7.1 Porto Arquipélago (andar 52)
Porto de **ex-piratas** que agora são mercadores (Torrenses do mar). Casas coloridas em palafitas, tabernas,
um estaleiro, redes a secar. Tem **estalagem**, **cristal**, **estaleiro** e **loja**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Capitã Marisa Vento-Sul** | chefe do porto, ex-pirata, um olho de vidro | Dá-te o **Barco** (R6_01); missão do Barba-Lodo |
| **Joaquim, o Lobo-do-Mar** | velho cartógrafo do mar | Cartas náuticas (R6_02) |
| **Tomé** | carpinteiro naval | **Melhorias do barco**: velas, canhões, casco (R6_03) |
| **Rosa** | dona da taberna do porto | Rumores, comida do mar, receitas |
| **Tiago** | grumete de 13 anos | Quer navegar contigo (R6_04) |

### 7.2 Vila das Pérolas (andar 54)
Ilha de **mergulhadores de pérolas** no meio do recife: cabanas de palha, barcos pequenos, colares a secar.
Tem **cabana**, **cristal** e **loja**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Ama Kaia** | mergulhadora campeã | Ensina mergulho (R6_06): Máscara de Mergulho |
| **Ourives Pérola** | faz joias | Joalharia com pérolas (R6_07) |
| **Velho Nalu** | contador de histórias do mar | Ovo de polvo (R6_15); lendas do Leviatã |

### 7.3 Coralina, a Cidade Submersa (andar 57)
Cidade das **sereias e tritões** dentro de uma cúpula de ar: casas de coral e conchas, ruas de areia branca,
peixes a passar por cima, um palácio de pérola. Tem **estalagem**, **cristal**, **forja de coral** e **loja**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Rainha Coralina** | rainha das sereias, séria e protetora | Missões debaixo de água; troca pérolas por itens raros |
| **Príncipe Maré** | filho da rainha, curioso | Quer ver a superfície (R6_09) |
| **Nerissa** | ferreira abissal | Forja de **Coral Abissal**, melhorias |
| **Lirael** | cantora | Canções que dão bónus (R6_10) |
| **Oceanus** | guarda-tritão | Desafios de combate debaixo de água |

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R6_01 | Um Barco para Ti | Capitã Marisa | Reparar um barco velho: 20 Madeira de Naufrágio + 10 Fio de Alga-Prata + 5 Lingote de Prata | **Barco** |
| R6_02 | Cartas Náuticas | Joaquim | Visitar as 5 ilhas do andar 52 | Carta Náutica (mapa do mar com correntes) |
| R6_03 | Melhorar o Barco (3 partes) | Tomé | Velas (tecido + madeira) · Canhões (lingotes + pólvora) · Casco (coral + madeira) | Barco mais rápido · canhões · aguenta tempestades |
| R6_04 | O Grumete | Tiago | Levar o Tiago em 3 viagens | O Tiago fica no barco (repara-o e dispara os canhões) |
| R6_05 | **Fantasmas do Navio** (história) | (no andar 53) | Libertar os 5 fantasmas de Jogadores | Cena: o **Kai desaparece** · página especial |
| R6_06 | Aprender a Mergulhar | Ama Kaia | Apanhar 10 pérolas no andar 54 | **Máscara de Mergulho** (+50% de Ar) |
| R6_07 | Colar de Pérolas | Ourives Pérola | 5 Pérolas + 1 Pérola Negra | Colar de Pérolas (acessório: +15% MP) |
| R6_08 | O Tesouro da Garrafa | (garrafa no andar 51) | Seguir o mapa até ao Farol da Caveira | Baú de ouro · Óculo de Pirata (vê mais longe no mar) |
| R6_09 | O Príncipe Maré | Príncipe Maré | Levá-lo à praia do andar 51 sem o deixar secar (passar por água pelo caminho) | ❤️ Rainha Coralina · Coroa de Conchas (cosmético) |
| R6_10 | Canções de Lirael | Lirael | Encontrar 4 conchas cantantes | **Concha do Mar** (instrumento: canções com bónus) |
| R6_11 | Escafandro | Gizmo | 10 Gel Elétrico + 5 Barra de Coral Abissal + 1 Lanterna Abissal | **Capacete de Escafandro** (Ar infinito e aguenta a pressão) |
| R6_12 | Pinça de Ouro | Barão Coaxim (andar 26) | Vencer o Caranguejo Rei Pinça-de-Ouro e trazer-lhe a pinça | 6 000 ouro (ou ficas com a pinça) |
| R6_13 | Barba-Lodo | Capitã Marisa | Vencer o Barba-Lodo | Chapéu de Barba-Lodo · Bússola Amaldiçoada |
| R6_14 | O Cavalo-marinho Ferido | Zed | Encontrar um Cavalo-marinho Gigante ferido (andar 56) e alimentá-lo 3 dias com Alga Doce | **Montada Cavalo-marinho Gigante** |
| R6_15 | O Ovo de Polvo | Velho Nalu | Encontrar o ovo de polvo (andar 56) e protegê-lo dos tubarões até à bolha de ar | **Polvo Bebé** (animal de estimação) |

---

## 9. Masmorra escondida — Cofre do Almirante Afogado (andar 56)

| | |
|---|---|
| Entrada | Porta do cofre no Naufrágio Antigo; abre com a **Chave do Almirante** (andar 55) |
| Sala 1 | **Corredores Inundados**: pouco ar, bolhas escondidas, portas que se fecham com a corrente |
| Sala 2 | **Sala dos Canhões**: canhões velhos disparam em padrões; passar entre os tiros |
| Sala 3 | **O Cofre**: uma balança gigante; pôr moedas e lingotes até equilibrar o peso escrito na porta |
| Boss extra | **Almirante Afogado** (64×64): fantasma de almirante com dois sabres e uma mão de caranguejo; chama marés e afoga partes da sala |
| Recompensa | **Besta Arpão do Almirante** (arma secreta, besta): os virotes puxam os inimigos e não perdem força debaixo de água · baú de ouro · página de lore extra "O Almirante" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Sardinha | praia do andar 51 | sempre | comum | 130 |
| Robalo | mar do andar 52 | dia | comum | 160 |
| Peixe-Palhaço | recife do andar 54 | dia | incomum | 320 |
| Atum Azul | mar aberto do 52 (do barco) | manhã | raro | 800 |
| Peixe-Lua | andar 56 | sol forte | raro | 900 |
| **Celacanto Ancião** (lendário) | fontes quentes do 58 | sempre (muito raro) | lendário | 9 000 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Alga Doce | andar 54 (precisa do **lago da quinta**) | 4 (dá sempre) | todas | cozinha, comida do Cavalo-marinho |
| Ananás da Ilha | Rosa (taberna) | 12 | Verão | cozinha, presentes |
| Batata-Doce da Ilha | Vila das Pérolas | 6 | Verão, Outono | cozinha |

### Animais
- **Polvo Bebé** (animal de estimação): missão R6_15. Debaixo de água o teu **Ar dura o triplo**; a tinta dele cega inimigos.
- **Cavalo-marinho Gigante** (montada): missão R6_14. Só na água e debaixo de água: 12 m/s e **Ar infinito** enquanto montas.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Tempestade no Mar | 15% no mar aberto | Ondas grandes, raios (perigosos: estás Encharcado!), Serpente das Tempestades |
| Maré Viva | lua cheia | Marés enormes nas praias: tesouros e Caranguejo Rei mais provável |
| Navio Mercante | 1 vez por semana no andar 52 | Um navio vende itens de todas as regiões |
| Noite das Medusas | Verão, noites quentes | As alforrecas brilham no mar; peixes raros aparecem mais |
| Ataque Pirata | 1 vez por estação | Piratas atacam o Porto Arquipélago; defendê-lo dá desconto e o título *Herói do Porto* |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 30): areia branca ×2, mar raso, mar fundo, rocha da maré ×3, palmeira, recife de coral ×3, alga pequena, alga gigante,
  fundo do mar ×2, minério de coral, madeira de naufrágio (cortável), ostra, baú, fogueira, cristal, casa de palafita, cais, bolha de ar, cúpula de ar
- [ ] **Peças especiais dos andares** (≈ 50, incluindo o galeão e o barco do jogador)
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Caranguejo Rei Pinça-de-Ouro, Barba-Lodo
- [ ] **8 guardiões**
- [ ] **Mini-boss** Capitão Esqueleto e **boss** Leviatã
- [ ] **Boss da masmorra** Almirante Afogado
- [ ] **Armas**: 12 de Coral Abissal + 2 únicas + 8 de guardião + 1 secreta = **23 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 24), **peixes** (6), **plantas** (3 × 4 fases)
- [ ] **NPCs**: Marisa, Joaquim, Tomé, Rosa, Tiago, Kaia, Ourives Pérola, Nalu, Coralina, Maré, Nerissa, Lirael, Oceanus, 5 fantasmas de Jogadores (+ retratos)
- [ ] **Animais**: Polvo Bebé, Cavalo-marinho Gigante (montada)
- [ ] **Conjunto de armadura** de Pele de Tubarão (5 ícones)
- [ ] **Interface**: barra de Ar; herói a **nadar** (animação extra do herói: `nadar` 6 frames × 3 direções)
