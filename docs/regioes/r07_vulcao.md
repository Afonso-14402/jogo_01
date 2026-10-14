# Região 7 — Vulcão (andares 61–70)

> Estrutura igual às outras regiões. Bosses grandes (Ferreiro Infernal e Titã de Magma) em `docs/BOSSES.md`.
> No andar 68 há o **duelo com o Kai** (ver `docs/HISTORIA.md` e `docs/BOSSES.md`).

---

## 1. Identidade

| | |
|---|---|
| Tema | Um vulcão gigante de um mundo de fogo: planícies de cinza, rios de lava, uma floresta queimada, anões do fogo, cultistas e um titã |
| Sensação | Perigo constante, calor, força bruta; e esperança a renascer das cinzas |
| Material das armas | **Obsidiana** (tier 7) |
| Monstros fracos a | **Gelo** |
| Cores principais | pretos `#2e222f` `#3e3546`, lava `#ea4f36` `#fb6b1d` `#f79617` `#f9c22b`, cinza `#625565` `#7f708a`, brasas `#b33831` |
| Luz | céu vermelho-escuro com fumo, luz laranja da lava a vir de baixo, faúlhas no ar, sombras longas |
| Clima | Cinza a cair 50% · Céu de fumo 30% · Chuva de brasas 15% · Erupção 5% |
| Música | `cinzas`, `rios_de_lava`, `bastiao_brasa`, `duelo_kai`, `ferreiro_infernal`, `tita_magma` |
| Níveis | monstros 61–71; mini-boss 67; boss 73 |
| Mecânica da região | **Calor** (ver abaixo). **Lava**: tocar dá muito dano e Queimadura (só a Salamandra Gigante anda por cima). **Erupções**: rochas de fogo caem do céu (sombra no chão 1 s antes). **Cinza**: visão 15 m |
| Animal de estimação | Salamandra |
| Montada | **Salamandra Gigante** (anda por cima da lava) |

### Calor
- Barra de **Calor** de 0 a 100 (o contrário da Temperatura da Região 5).
- Nos andares desta região sobe **1 ponto a cada 3 s**; perto de lava (menos de 3 m) **5 por segundo**.
- **Água**, **Poção Fresca**, lagos e termas baixam o Calor (−40, ou até 0 nas termas).
- A partir de **75**: −10% de velocidade e a Estamina recupera metade. Em **100**: Queimadura contínua.
- **Armadura de Couro de Salamandra** ou **Seda Ignífuga**: o Calor sobe metade.

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Obsidiana | rochas negras e brilhantes (62, 64, 67) | Picareta de Coral+ | Barra de Obsidiana (3 Obsidiana + 1 Brasa de Lava) |
| Brasa de Lava | margens de lava (62, 67) | Picareta | **combustível** desta região (substitui o carvão) |
| Lenho-Brasa | árvores negras que não ardem (63) | Machado | **madeira** da região |
| Couro de Salamandra | Salamandra | drop | **couro** da região (resiste ao Calor) |
| Seda Ignífuga | casulos ignífugos (63) | à mão | **fio** da região |
| Cristal de Magma | lava que arrefeceu (62, 70) | Picareta | **cristal** da região |
| Rubi | veios do andar 64 | Picareta | gema de **Fogo** |
| Pimenta-Lava | 61, 66 | à mão | cozinha (+ATQ), muito picante |
| Flor de Cinza | 61, 63 | à mão | Poção Fresca, presentes |
| Enxofre | géiseres (66) | Picareta | pólvora, bombas |
| Núcleo de Magma | Golem de Magma | drop | engenhocas, armas de fogo |

---

## 3. Monstros

### 3.1 Salamandra
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, 2–3 |
| Andares | 61, 62, 64, 67 |
| Comportamento | Nada dentro da lava; sai para cuspir fogo e volta a mergulhar |
| Ataques | **Cuspe de Fogo**: Queimadura (aviso 0,5 s) · **Mergulho na Lava**: aparece noutro sítio · **Cauda** |
| Fraco / Imune | Gelo / Fogo |
| Drops | Couro de Salamandra 55% · Escama Ardente 25% |
| Elite | **Salamandra Negra**: o cuspe deixa uma poça de lava |
| Animações | nadar na lava (4), sair (4), parado (4), cuspir (4), cauda (4), mergulhar (4), dano (1), morrer (4) |

### 3.2 Elemental de Fogo
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago** |
| Andares | 62, 65, 69, 70 |
| Comportamento | Uma chama viva com olhos. Ao morrer **explode** |
| Ataques | **Bola de Fogo** · **Anel de Fogo**: área à volta dele (aviso 0,8 s: cresce) · **Explosão** ao morrer |
| Fraco / Imune | Gelo, **Água** (Encharcado apaga-o 3 s: fica fraco e lento) / Fogo, Veneno |
| Drops | Essência de Fogo 50% · Cinza Mágica 30% |
| Elite | **Elemental Azul**: fogo azul, mais quente (Queimadura dupla) |
| Animações | arder (4), mover (4), bola de fogo (4), anel (4), apagado (2), dano (1), explodir (5) |

### 3.3 Diabrete
| | |
|---|---|
| Tamanho | 32×32 (pequenos, ~18 px) |
| Tipo | **Rápido + Fraco**, grupos de 3–5 |
| Andares | 61, 63, 65, 68 |
| Comportamento | Demoniozinhos travessos com tridentes; riem-se e fazem **partidas** |
| Ataques | **Tridente** · **Bolinha de Fogo** · **Partida**: troca a tua arma equipada pela secundária (aviso 0,4 s: estala os dedos) |
| Fraco / Resiste | Gelo, Luz / Fogo |
| Drops | Chifre de Diabrete 40% · Enxofre 30% |
| Elite | **Diabrete Chefe**: chama mais 3 diabretes |
| Animações | parado (4), voar/saltitar (4), tridente (4), atirar (4), estalar dedos (4), rir (4), dano (1), morrer (4) |

### 3.4 Golem de Magma
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 62, 64, 67, 70 |
| Comportamento | Rocha com lava a correr por dentro. Deixa **poças de lava** onde pisa. Quando arrefece fica de pedra |
| Ataques | **Murro de Lava** (×1,5; Queimadura) · **Pisada**: deixa uma poça de lava 5 s · **Arrefecer**: fica de pedra (DEF ×3, lento); o Gelo parte-o (×2) |
| Fraco / Imune | Gelo, Martelo / Fogo |
| Drops | Obsidiana 40% · Cristal de Magma 20% · Núcleo de Magma 15% |
| Elite | **Golem de Magma Branco**: tão quente que derrete o chão à volta |
| Animações | parado (4), mover (4), murro (4), pisada (4), arrefecer (4), dano (1), morrer (6) |

### 3.5 Cão Infernal
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, matilha de 2–4 |
| Andares | 61, 63, 66, 68 |
| Comportamento | Correm em matilha; atacam ao mesmo tempo de lados diferentes |
| Ataques | **Mordida de Fogo**: Queimadura · **Sopro de Fogo**: cone (aviso 0,6 s: abre a boca a brilhar) · **Investida** |
| Fraco / Imune | Gelo / Fogo |
| Drops | Pele de Cão Infernal 50% · Presa Ardente 25% |
| Elite | **Cão Infernal Alfa**: o sopro deixa o chão a arder |
| Animações | parado (4), correr (6), mordida (4), sopro (4), dano (1), morrer (4) |

### 3.6 Morcego de Cinza
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Voador + Fraco**, bandos de 4–6 |
| Andares | 61, 64, 67, 69 |
| Comportamento | Saem das nuvens de cinza; deixam um rasto de cinza no ar |
| Ataques | **Mordida** · **Rasto de Cinza**: quem passa pelo rasto fica com Cegueira 2 s |
| Fraco / Resiste | Gelo, Raio / Fogo |
| Drops | Asa de Cinza 50% · Cinza 40% |
| Elite | **Morcego de Brasa**: o rasto queima |
| Animações | voar (4), mordida (4), dano (1), morrer (3) |

### 3.7 Escorpião de Lava
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Tanque** |
| Andares | 62, 66, 67 |
| Comportamento | Carapaça de rocha; ferrão incandescente |
| Ataques | **Pinças** · **Ferrão de Lava**: Queimadura e Veneno ao mesmo tempo (aviso 0,6 s) · **Enterrar-se** na cinza |
| Fraco / Resiste | Gelo, Martelo / Fogo, Físico (−20%) |
| Drops | Carapaça de Rocha 45% · Ferrão de Lava 25% |
| Elite | **Escorpião de Obsidiana**: carapaça de vidro negro (o Martelo parte-a) |
| Animações | parado (4), mover (6), pinças (4), ferrão (5), enterrar (4), dano (1), morrer (4) |

### 3.8 Cultista do Fogo
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago** (humano), grupos de 2–3 |
| Andares | 65, 68, 69 |
| Comportamento | Adoram o Titã de Magma. Fazem **rituais**: se um ritual chegar ao fim, aparece um Elemental de Fogo |
| Ataques | **Chama** (projétil) · **Ritual**: canaliza 5 s (interrompe-o batendo-lhe) · **Escudo de Fogo**: quem lhe bate corpo a corpo queima-se |
| Fraco / Resiste | Gelo / Fogo |
| Drops | Pergaminho de Fogo 20% · Túnica de Cultista 10% (cosmético) · ouro |
| Elite | **Sumo-Cultista**: o ritual chama 2 elementais |
| Animações | parado (4), mover (6), chama (4), ritual (4), escudo (4), dano (1), morrer (5) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Tricéfalo** | andares 61, 66, 68, 3% | cão infernal de **três cabeças** (64×64): uma de fogo, uma de fumo, uma de lava | Cada cabeça tem o seu ataque (sopro de fogo, nuvem de fumo que cega, cuspe de lava). Cortar uma cabeça (cada uma tem a sua vida) tira-lhe esse ataque | **Coleira de Tricéfalo** (+10% de dano elemental) · Presa Tripla |
| **Golem Forjado Nº 7** | andares 64, 65, 4% | golem de obsidiana polida (64×64) com um "7" gravado no peito | Raio de magma pelo peito · murros-foguete · **o ponto fraco é o núcleo nas costas** | **Placa Nº 7** (material lendário para armaduras) · Núcleo de Obsidiana (missão R7_14) |

---

## 5. Os andares

### Andar 61 — Planícies de Cinza
| | |
|---|---|
| Tamanho / Nível | 280×280 m · nível 61 |
| Bioma | Planície cinzenta coberta de cinza fofa, árvores petrificadas, cinza a cair como neve escura, o vulcão gigante ao fundo |
| Zonas | **Mar de Cinza** · **Árvores Petrificadas** · **Acampamento das Cinzas** (povoação) · **Cratera Pequena** |
| Mecânica especial | **Calor** começa aqui. **Dunas de cinza** escondem itens (pisar descobre-os). **Cinza a cair**: visão 15 m |
| Monstros | Diabrete, Cão Infernal, Morcego de Cinza, Salamandra |
| Recursos | Flor de Cinza, Pimenta-Lava, Obsidiana (pouca), Cinza |
| Povoação | **Acampamento das Cinzas** (secção 7.1) |
| Guardião | **Fénix de Cinza** |
| Segredo | Uma árvore petrificada é oca: dentro, o **último broto verde** do mundo queimado (missão R7_01 começa aqui) |
| Puzzle | **Sinos de cinza**: limpar a cinza de 4 sinos de pedra e tocá-los; o som afasta a cinza e mostra um baú de ouro |
| Página de lore 61 | *"Este mundo ardeu quando a torre o engoliu. A torre não engole com cuidado."* |
| Desafios | Atravessar sem deixar o Calor passar de 75 · Encontrar 10 itens nas dunas de cinza |
| Peças especiais | árvore petrificada, duna de cinza, sino de pedra, tenda de refugiados, cratera pequena |

### Andar 62 — Rios de Lava
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 62 |
| Bioma | Terra de basalto negro cortada por rios de lava brilhante, ilhas de rocha, uma cascata de lava, fumo a subir |
| Zonas | **Margens Negras** · **Pontes de Pedra** · **Ilhas de Basalto** · **Cascata de Lava** |
| Mecânica especial | **Pedras flutuantes**: afundam na lava 2 s depois de as pisares. **Erupções** pequenas. **Pesca na lava** (Cana Ignífuga) |
| Monstros | Salamandra, Elemental de Fogo, Golem de Magma, Escorpião de Lava |
| Recursos | **Obsidiana**, **Brasa de Lava**, Cristal de Magma |
| Guardião | **Serpente de Lava** |
| Segredo | Atrás da Cascata de Lava (só passando montado na Salamandra Gigante, ou com a Poção Ignífuga) há uma gruta fresca com **gelo eterno** (impossível, e no entanto…) e um baú de ouro |
| Puzzle | **Comportas de basalto**: desviar um rio de lava com 3 comportas para secar o caminho até à ilha central |
| Página de lore 62 | *"A lava corre para cima em alguns sítios. A torre não respeita as regras de nenhum mundo."* |
| Desafios | Atravessar só pelas pedras flutuantes · Pescar um Peixe-Brasa |
| Peças especiais | rio de lava (com shader), pedra flutuante, cascata de lava, comporta de basalto, ilha de basalto |

### Andar 63 — Floresta Queimada
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 63 |
| Bioma | Floresta de troncos negros a fumegar, brasas no chão, casulos brancos pendurados, um lago de águas escuras |
| Zonas | **Troncos Negros** · **Clareira das Brasas** · **Casulos Ignífugos** · **Lago Negro** |
| Mecânica especial | **Árvores em brasa** que caem (estalam antes de cair). **Fogos** que se reacendem. Com a missão R7_01 a floresta **volta a ficar verde aos poucos** |
| Monstros | Diabrete, Cão Infernal, Salamandra, Elemental de Fogo |
| Recursos | **Lenho-Brasa**, **Seda Ignífuga**, Flor de Cinza |
| Guardião | **Ent Carbonizado** |
| Segredo | Debaixo do Lago Negro há raízes ainda vivas: regá-las com **Água da Fonte Esmeralda** (andar 27) faz nascer uma **Árvore Verde** com frutos que dão +1% HP máx. (uma vez cada) |
| Puzzle | **Brasas**: apagar as brasas pela ordem certa para o fogo não se reacender (cada brasa acesa reacende as vizinhas) |
| Página de lore 63 | *"Encontrei um Ent queimado. Era primo da Árvore-Mãe. A torre junta família que nunca se conheceu."* |
| Desafios | Atravessar sem ser atingido por árvores · Plantar 10 sementes |
| Peças especiais | tronco queimado (em pé e caído), casulo ignífugo, brasas no chão, broto verde, árvore verde (depois da missão) |

### Andar 64 — Minas de Obsidiana
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 64 |
| Bioma | Galerias de vidro negro que brilha à luz da lava, carris de anões, uma fortaleza escavada na rocha (o Bastião) |
| Zonas | **Bastião de Obsidiana** (povoação) · **Galerias de Vidro Negro** · **Forno do Clã** · **Veios Profundos** |
| Mecânica especial | **Obsidiana afiada**: encostar às paredes corta (Sangrar). **Vagonetas anãs** (depois da missão R7_04) |
| Monstros | Golem de Magma, Morcego de Cinza, Salamandra, Escorpião de Lava |
| Recursos | **Obsidiana** (muita), **Rubi**, Brasa de Lava |
| Povoação | **Bastião de Obsidiana** (secção 7.2) |
| Guardião | **Escavadora Anã Possuída** |
| Segredo | Nos Veios Profundos, a **porta de runas** da masmorra escondida (Forja Primordial) |
| Puzzle | **Fornos**: acender 3 fornos com Brasa de Lava na ordem do calor (o mais quente primeiro) para abrir o Forno do Clã |
| Página de lore 64 | *"Os anões do fogo forjaram as armas dos primeiros Jogadores. Guardam os moldes. O meu nome não está lá. Ainda."* |
| Desafios | Atravessar as galerias sem tocar nas paredes · Minerar 5 Rubis |
| Peças especiais | parede de obsidiana, portão do bastião, forno anão, carris anões, porta de runas |

### Andar 65 — Forja Infernal 💀
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 65 |
| Bioma | Uma forja gigante e demoníaca: bigornas enormes, correntes, canais de metal fundido, martelos mecânicos a bater |
| Zonas | **Bigornas dos Demónios** · **Correntes de Metal Fundido** · **Arena-Forja** (arena do mini-boss) |
| Mecânica especial | **Canais de metal fundido** que mudam de direção com alavancas. **Martelos mecânicos** que esmagam em ritmo |
| Monstros | Diabrete, Cultista do Fogo, Elemental de Fogo |
| Recursos | Obsidiana, Barras antigas, Núcleo de Magma |
| Mini-boss | **Ferreiro Infernal** (ver `docs/BOSSES.md`) → arma única **Martelo da Forja** (martelo) |
| Segredo | Numa bigorna há uma **arma inacabada** com o número 10 000 gravado: é para ti (lore; o Brom acaba-a mais tarde — ver `docs/NPCS.md`) |
| Página de lore 65 | *"O Ferreiro forjava armas para os Jogadores que ainda não tinham chegado. Havia uma com o meu número."* |
| Desafios | Vencer o Ferreiro sem ser atingido pelos martelos · Desviar o metal fundido contra ele 3 vezes |
| Peças especiais | bigorna gigante, martelo mecânico, canal de metal, correntes penduradas, alavanca de forja |

### Andar 66 — Campos de Géiseres
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 66 |
| Bioma | Terra branca e amarela com géiseres a jorrar, lagos quentes de cores incríveis (azul, laranja, verde), vapor por todo o lado, uma estância termal |
| Zonas | **Termas dos Géiseres** (povoação) · **Campo de Géiseres** · **Lagos de Cores** · **Ninho dos Sapos-Vulcão** |
| Mecânica especial | **Géiseres**: jorram de 10 em 10 s e **atiram-te para o ar** (alcanças plataformas altas). **Lagos de cores**: cada cor tem um efeito (azul arrefece, laranja queima, verde envenena) |
| Monstros | Cão Infernal, Escorpião de Lava, Salamandra, Elemental de Fogo |
| Recursos | **Enxofre**, Pimenta-Lava, ovos de Sapo-Vulcão |
| Povoação | **Termas dos Géiseres** (secção 7.3) |
| Guardião | **Sapo-Vulcão** |
| Segredo | Saltar de géiser em géiser até ao topo de uma rocha alta: um **ninho de fénix** com uma **Pena de Fénix** (revive-te uma vez, item raro) |
| Puzzle | **Géiseres em cadeia**: tapar géiseres com pedras para que a pressão saia por um só, que te leva à rocha alta |
| Página de lore 66 | *"Tomei banho nas termas. Por uma hora fui só uma pessoa, não um Jogador."* |
| Desafios | Chegar ao ninho de fénix · Usar os 3 lagos de cores |
| Peças especiais | géiser, lago de cor (3 cores), casa termal, rocha alta, ninho de fénix |

### Andar 67 — Ponte sobre o Magma
| | |
|---|---|
| Tamanho / Nível | 300×120 m · nível 67 |
| Bioma | Uma ponte de pedra muito comprida por cima de um mar de magma, pilares enormes, estátuas de anões a segurar a ponte, rochas a voar |
| Zonas | **Cabeceira** · **A Ponte** · **Pilares** (descer para plataformas laterais) · **Outra Margem** |
| Mecânica especial | **Partes da ponte que caem** (racham antes). **Ventos quentes** que empurram. **Erupções** lançam rochas para a ponte |
| Monstros | Golem de Magma, Morcego de Cinza, Salamandra, Escorpião de Lava |
| Recursos | Obsidiana, Brasa de Lava, Cristal de Magma |
| Guardião | **Golem Portão de Obsidiana** (bloqueia a ponte) |
| Segredo | Num pilar, uma estátua de anão tem a mão aberta: pôr-lhe um **Rubi** abre uma escada para uma sala com baú de ouro e uma Placa Nº 3 (lore dos golens) |
| Puzzle | **Ponte quebrada**: rodar 3 estátuas-guindaste para pôr 3 secções da ponte no sítio |
| Página de lore 67 | *"Atravessei a ponte sozinho. Não havia ninguém para me ver cair. Isso dá mais medo do que a lava."* |
| Desafios | Atravessar sem cair · Atravessar em menos de 2 min |
| Peças especiais | ponte de pedra (secções), pilar com estátua de anão, estátua-guindaste, mar de magma |

### Andar 68 — Cratera Interior
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 68 |
| Bioma | Dentro da cratera do vulcão: paredes enormes, um lago de magma no centro que sobe e desce, ilhas negras, uma plataforma redonda |
| Zonas | **Paredes da Cratera** · **Lago de Magma Central** · **Ilhas Negras** · **Plataforma do Duelo** |
| Mecânica especial | **O magma respira**: sobe e desce a cada 2 min; as ilhas baixas afundam quando ele sobe |
| Monstros | Cão Infernal, Diabrete, Cultista do Fogo |
| Recursos | Cristal de Magma, Obsidiana |
| Guardião (especial) | **Kai, Jogador nº 9 999** — duelo da história (ver `docs/BOSSES.md`). Se tiveres amizade alta com o Kai, **podes salvá-lo** |
| Página de lore 68 | *"Hoje lutei contra um amigo. A janela azul chamou-lhe 'Inimigo'. A janela mente."* |
| Desafios | Salvar o Kai · Vencer o duelo sem usar poções |
| Peças especiais | plataforma redonda de duelo, ilhas negras, paredes da cratera, lago de magma |

### Andar 69 — Templo do Fogo
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 69 |
| Bioma | Templo esculpido na rocha do vulcão, com chamas que nunca apagam, estátuas do Titã, cultistas a cantar, um altar ao centro |
| Zonas | **Escadaria das Chamas Eternas** · **Salão dos Cultistas** · **Altar do Ritual** · **Câmaras dos Votos** |
| Mecânica especial | **Chamas eternas** (tocar dá Queimadura). **Apagar braseiros** com água ou gelo abre portas. **Rituais**: interromper 3 rituais antes do guardião |
| Monstros | Cultista do Fogo, Elemental de Fogo, Diabrete, Morcego de Cinza |
| Recursos | Rubi, Pergaminhos de Fogo |
| Guardião | **Sumo-Sacerdote das Chamas** |
| Segredo | Nas Câmaras dos Votos, uma parede tem os **nomes de todos os Jogadores** que passaram por aqui; o último é o do Kai |
| Puzzle | **Braseiros**: apagar os braseiros certos para a luz formar o símbolo da porta |
| Página de lore 69 | *"Os cultistas adoram o Titã porque ele é forte. Eu adoro… não sei. Talvez a ideia de casa."* |
| Desafios | Interromper os 3 rituais · Apagar todos os braseiros |
| Peças especiais | estátua do Titã, braseiro eterno, altar do ritual, parede com nomes |

### Andar 70 — Coração do Vulcão 👑
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 70 |
| Bioma | A garganta do vulcão: um poço de magma gigante, ilhas de rocha a flutuar, calor a tremer no ar, uma luz branca e laranja |
| Zonas | **Garganta do Vulcão** · **Câmara do Magma** · **O Coração** (arena) |
| Mecânica especial | O chão são **ilhas sobre magma**; o Titã sai do magma e afunda ilhas |
| Monstros | Golem de Magma, Elemental de Fogo |
| Boss | **Titã de Magma** (ver `docs/BOSSES.md`) → arma única **Coração de Magma** (espada grande) |
| Depois do boss | **Dia da Subida**. Se salvaste o Kai, ele aparece na festa (ainda envergonhado). O vulcão adormece: os andares 61–69 ficam menos quentes (o Calor sobe metade) |
| Página de lore 70 | *"O Titã adormeceu. Toda a região respirou. Eu também."* |
| Desafios | Vencer sem perder nenhuma ilha · Vencer em menos de 6 min |
| Peças especiais | ilha de rocha flutuante, poço de magma, paredes da garganta |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 61 | **Fénix de Cinza** | pássaro feito de cinza e brasas (48×48) | Mergulho em Chamas · Chuva de Cinza · **Renascer**: ao morrer renasce com 30% (congelar as cinzas impede) | Gelo | **Arco Fénix** (arco): uma vez por dia, se morreres, renasces com 20% de vida |
| 62 | **Serpente de Lava** | serpente de rocha e lava (64×64) que nada no magma | Salto de Lava · Cuspe de Magma · Onda de Lava | Gelo | **Lança de Magma** (lança): as estocadas deixam um rasto de fogo no chão |
| 63 | **Ent Carbonizado** | ent queimado em brasa (64×64), primo da Árvore-Mãe | Galhos em Brasa · Raízes de Fogo · Explosão de Faúlhas | Gelo, Água | **Machado Brasa-Viva** (machado): 20% de causar Queimadura |
| 64 | **Escavadora Anã Possuída** | máquina de minas anã com uma broca enorme (64×64), olhos de cultista | Broca · Carga nos Carris · Chuva de Rochas | Gelo, Raio | **Martelo-Broca** (martelo): minera como picareta de tier 8 e ignora 20% da DEF |
| 66 | **Sapo-Vulcão** | sapo enorme (48×48) com um géiser nas costas | **Géiser** (atira-te ao ar) · Língua de Fogo · Salto Esmagador | Gelo | **Manoplas Géiser** (manoplas): o último golpe do combo atira o inimigo ao ar (atordoado) |
| 67 | **Golem Portão de Obsidiana** | um portão vivo de obsidiana com runas (64×64) | Esmagar · Raios de Magma pelas runas · **Fechar** (invencível: partir as 4 runas) | Gelo | **Espada Grande Portão** (espada grande): +20% DEF enquanto carregas o ataque |
| 68 | **Kai** (duelo da história) | ver `docs/BOSSES.md` | — | — | Se o venceres até ao fim: **Lâmina do Kai** (espada). Se o salvares: **Amuleto da Amizade** (+10% a tudo quando um companheiro está contigo) |
| 69 | **Sumo-Sacerdote das Chamas** | cultista principal com máscara dourada (48×48) | Ritual (chama Elementais) · Muralha de Fogo · Chamas Sagradas (área) | Gelo, Água | **Cajado do Sumo-Sacerdote** (cajado): a Bola de Fogo tem +30% de área |

---

## 7. Povoações

### 7.1 Acampamento das Cinzas (andar 61)
Refugiados de uma cidade que ardeu quando a torre engoliu o vulcão deles. Tendas cinzentas, uma fogueira grande,
crianças a brincar com cinza. Tem **tenda**, **cristal** e **loja básica**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Mãe Brasa** | matriarca dos refugiados | Missão "Sementes de Esperança" (R7_01) |
| **Fuligem** | órfão espertalhão | Vende **mapas errados** (R7_02) |
| **Curandeiro Carvão** | médico do acampamento | Cura Queimaduras; vende Poção Fresca |
| **Lena Cinza** | pintora | Pinta com cinza (R7_15): quadros para a casa |

### 7.2 Bastião de Obsidiana (andar 64) — do Clã Brasa
Fortaleza escavada na rocha do **Clã Brasa**, anões do fogo — **família distante do Brom**. Salões de obsidiana,
fornos sempre acesos, rios de lava canalizados. Tem **estalagem**, **cristal**, **loja** e a **Forja de Obsidiana**
(a melhor forja até aqui: +5% de sucesso nas melhorias).

| NPC | Quem é | O que faz |
|---|---|---|
| **Rainha-Forja Hildur Brasa** | líder do clã | Missão dos rubis (R7_05) |
| **Mestre Ragnar Brasa** | **tio do Brom**, barba trançada com contas de rubi | Ensina a **Forja de Obsidiana**; vende a **Cana Ignífuga** |
| **Ruby Brasa** | gemóloga | Encantamentos de Fogo, rubis |
| **Ash** | mineiro | Missão da Escavadora (R7_04) |

### 7.3 Termas dos Géiseres (andar 66)
Uma **estância termal** no meio dos géiseres, gerida por um gnomo: piscinas quentes, toalhas, cadeiras, um
restaurante de ovos cozidos no géiser. Tem **estalagem**, **cristal**, **loja** e **termas**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Senhor Vapor** | gnomo, primo do Gizmo | Missão dos canos (R7_06); **termas**: cura tudo e Calor a 0 durante 1 dia |
| **Massagista Lava** | homenzarrão simpático | Massagem: +10% Estamina máx. durante 1 dia |
| **Gil** | turista Torrense perdido, com uma câmara antiga | Missão R7_07 → **Modo Foto** |
| **Cozinheira Fumarola** | cozinha no géiser | Receitas com ovos (R7_08) |

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R7_01 | Sementes de Esperança | Mãe Brasa | Plantar 10 Sementes de Lenho-Brasa no andar 63 e regá-las com água trazida de fora | A floresta começa a ficar verde · ❤️ · Lenho-Brasa sem fim |
| R7_02 | Os Mapas do Fuligem | Fuligem | Seguir um mapa do Fuligem (está tudo errado) | Encontras um tesouro **por acaso** · título *Sortudo* |
| R7_03 | O Tio Ragnar | Brom | Levar uma carta ao Mestre Ragnar | **Forja de Obsidiana** (+5% nas melhorias) · ❤️❤️ Brom |
| R7_04 | A Escavadora | Ash | Vencer a Escavadora Possuída e recuperar a Peça Mestra | Vagonetas do clã a funcionar (atalhos no 64) |
| R7_05 | Rubis para a Rainha | Rainha Hildur | 5 Rubis + 3 Barras de Obsidiana | **Anel de Rubi da Rainha** (+15% de dano de Fogo) · abre a masmorra (com R7_03) |
| R7_06 | As Termas | Senhor Vapor | Reparar 3 canos de géiser (10 Lingote de Prata + 5 Gel Elétrico) | Termas abertas |
| R7_07 | O Turista Perdido | Gil | Levar o Gil até à Zona Segura do andar 67 | **Modo Foto** (tirar fotos no jogo, com filtros) |
| R7_08 | Ovos de Géiser | Cozinheira Fumarola | 10 ovos de Sapo-Vulcão | Receita **Ovos de Géiser** (o Calor sobe metade 5 min) |
| R7_09 | A Salamandrazinha | Zed | Salvar uma Salamandra bebé presa numa ilha a afundar (andar 62) | **Salamandra** (animal de estimação) |
| R7_10 | Montar na Lava | Zed | Domar uma Salamandra Gigante no andar 66 (acalmá-la com Pimenta-Lava) | **Montada Salamandra Gigante** |
| R7_11 | **O Kai** (história) | (andar 68) | O duelo: **salvar** ou **vencer** o Kai | ver `docs/HISTORIA.md` |
| R7_12 | Rituais Interrompidos | Irmã Célia | Interromper os 3 rituais do andar 69 | Água Benta ×10 · ❤️ Célia |
| R7_13 | Três Cabeças | Capitã Freya (rank A) | Vencer o Tricéfalo | Coleira de Tricéfalo · 4 000 ouro |
| R7_14 | O Número 7 | Gizmo | Trazer o Núcleo de Obsidiana do Golem Forjado Nº 7 | **Autómato de Quinta** (rega a quinta sozinho todos os dias) |
| R7_15 | Arte de Cinza | Lena Cinza | 20 Cinza Mágica + 5 Flor de Cinza | 3 quadros para a casa |

---

## 9. Masmorra escondida — Forja Primordial (andar 64)

| | |
|---|---|
| Entrada | Porta de runas dos Veios Profundos; abre depois das missões R7_03 e R7_05 (o Ragnar dá a runa) |
| Sala 1 | **Ponte de Correntes**: plataformas penduradas por correntes a baloiçar sobre o magma |
| Sala 2 | **Sala dos Moldes**: verter metal fundido nos moldes certos (as formas das armas dos primeiros Jogadores) |
| Sala 3 | **Câmara do Fole**: foles gigantes sopram ar quente que empurra; passar entre as rajadas |
| Boss extra | **Autómato da Forja Primordial** (64×64): autómato anão antiquíssimo com um martelo no lugar de um braço e uma fornalha no peito |
| Recompensa | **Martelo Primordial** (arma secreta, martelo): o ataque carregado cria uma **erupção** (área de fogo de 4 m) · baú de ouro · página de lore extra "As Armas dos Jogadores" |

---

## 10. Peixes, plantas e animais

### Peixes (a pesca na lava precisa da **Cana Ignífuga**)
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Caranguejo de Basalto | margens do andar 62 | sempre | comum | 250 |
| Peixe dos Géiseres | lagos azuis do 66 | sempre | comum | 280 |
| Carpa Negra | Lago Negro (63) | noite | incomum | 520 |
| Peixe-Brasa | lava do andar 62 | dia | raro | 1 100 |
| Enguia de Magma | lava do andar 67 | erupção | raro | 1 300 |
| **Fénix das Profundezas** (lendário) | poço de magma do andar 70 (depois do boss) | 12:00–13:00 | lendário | 12 000 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Pimenta-Lava | andar 61 | 7 | Verão | cozinha (+ATQ), acalmar salamandras |
| Flor de Cinza | andar 63 | 6 | todas | Poção Fresca, presentes |
| Lenho-Brasa | Mãe Brasa | 21 (árvore) | todas | madeira que não arde |
| Batata Vulcânica | Fumarola | 6 | Verão, Outono | cozinha (aquece) |

### Animais
- **Salamandra** (animal de estimação): missão R7_09. Os ataques dela causam **Queimadura**; perto dela não tens Frio nem Temperatura baixa.
- **Salamandra Gigante** (montada): missão R7_10. 10 m/s, **anda por cima da lava**, o Calor não sobe enquanto montas.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Erupção | 5% por hora | Rochas de fogo caem em todo o andar; aparecem Enguias de Magma |
| Chuva de Brasas | 15% | Brasas caem: tudo o que é de madeira arde (pontes, árvores) |
| Noite Vermelha | 1 vez por semana | Céu vermelho; os cultistas fazem rituais por todo o lado |
| Rio Desviado | 1 dia em cada 5, andar 62 | Os rios de lava mudam de caminho: novas zonas abertas |
| Festival da Forja | 1 vez por estação no Bastião | Concurso de forja: melhorar uma arma sem falhar dá prémios |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 28): chão de basalto ×3, cinza ×2, lava, rocha vulcânica ×3, falésia negra, árvore petrificada, tronco queimado ×2,
  obsidiana (minério), lenho-brasa (cortável), flor de cinza, baú, fogueira, cristal, ponte de pedra, pedra flutuante, géiser, braseiro, parede de obsidiana
- [ ] **Peças especiais dos andares** (≈ 45)
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Tricéfalo, Golem Forjado Nº 7
- [ ] **7 guardiões** (+ o Kai, que é desenhado como personagem — ver `docs/NPCS.md`)
- [ ] **Mini-boss** Ferreiro Infernal e **boss** Titã de Magma
- [ ] **Boss da masmorra** Autómato da Forja Primordial
- [ ] **Armas**: 12 de Obsidiana + 2 únicas + 7 de guardião + Lâmina do Kai + 1 secreta = **23 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 24), **peixes** (6), **plantas** (4 × 4 fases)
- [ ] **NPCs**: Mãe Brasa, Fuligem, Carvão, Lena, Hildur, Ragnar, Ruby, Ash, Senhor Vapor, Massagista Lava, Gil, Fumarola (+ retratos)
- [ ] **Animais**: Salamandra, Salamandra Gigante (montada)
- [ ] **Conjunto de armadura** de Couro de Salamandra (5 ícones)
- [ ] **Interface**: barra de Calor
