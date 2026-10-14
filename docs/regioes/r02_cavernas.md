# Região 2 — Cavernas e Minas (andares 11–20)

> Mesma estrutura de todas as regiões: identidade → materiais → monstros → andares → guardiões →
> povoações → missões → masmorra escondida → peixes e plantas → eventos → lista de arte.
> Bosses grandes (Aranha-Mãe e Golem de Cristal) em `docs/BOSSES.md`.

---

## 1. Identidade

| | |
|---|---|
| Tema | Debaixo da terra: minas abandonadas, grutas de cristal, rios escuros, uma forja de anões |
| Sensação | Escuro, apertado, um pouco de medo; tesouros a brilhar |
| Material das armas | **Ferro** (tier 2) |
| Monstros fracos a | **Raio** |
| Cores principais | cinzentos `#3e3546` `#625565`, castanho `#694f62`, luz de tocha `#f79617`, cristais `#30e1b9` `#a884f3` `#4d9be6` |
| Luz | **Escuridão**: só se vê à volta de luzes (tochas, cristais, fungos, lanterna). Luz quente e laranja das tochas, luz fria dos cristais |
| Clima | não há céu; às vezes **pó a cair** e **pingos de água** |
| Música | `minas_eco`, `cristal_canto`, `forja_ana`, `aranha_mae`, `golem_cristal` |
| Níveis | monstros 11–21; mini-boss 17; boss 23 |
| Mecânica da região | **Escuridão e luz**: sem luz vês 3 m. **Tocha** (consumível, 3 min, 10 ouro) · **Lanterna** (Gizmo, permanente) · cristais e fungos iluminam |
| Animal de estimação | Morceguinho |

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Minério de Ferro | todos os andares | Picareta (Cobre ou melhor) | Lingote de Ferro (3 minérios + 1 Carvão) |
| Carvão | veios pretos (11, 12, 18) | Picareta | combustível da forja a partir de agora; tochas |
| Escora Velha | vigas de madeira das minas (11, 12) | Machado | **madeira** da região (cabos, bestas) |
| Fungo-Lenho | caules de fungos gigantes (16) | Machado | **madeira** de qualidade (cajados, arcos) |
| Couro de Toupeira | Toupeira Gigante | drop | manoplas, armaduras |
| Seda de Aranha | Aranha da Caverna, teias (15) | drop / à mão | **fio** da região (arcos, roupa fina) |
| Cristal de Gruta | 13, 19 | Picareta | **cristal** da região (melhorias, cajados, luz) |
| Topázio | 13 (raro) | Picareta | gema de **Raio** |
| Rubi | 18 (raro) | Picareta | gema de **Fogo** |
| Ametista | sala violeta (13) | Picareta | joalharia |
| Musgo Luminoso | paredes (12, 16) | à mão | Poção de Visão Noturna |
| Raiz-Pedra | 11, 17 | à mão | Poção de Defesa |
| Engrenagem | Goblins, Kobolds | drop | engenhocas do Gizmo |
| Guano | Morcegos | drop | fertilizante da quinta (+1 qualidade) |

---

## 3. Monstros

### 3.1 Morcego
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Voador + Fraco**, bandos de 4–6 |
| Andares | 11–19 |
| Comportamento | Dormem pendurados no teto. Acordam com luz forte ou barulho (combate a menos de 8 m). Voam aos ziguezagues |
| Ataques | **Mordida** (×0,8; aviso 0,3 s) · **Voo Rasante** em linha (×1,1; aviso 0,5 s: guincho) |
| Fraco / Resiste | Raio, Luz / — |
| Drops | Asa de Morcego 50% · Guano 30% |
| Elite | **Morcego Vampiro**: rouba 20% do dano que faz |
| Animações | dormir (2), acordar (3), voar (4), atacar (4), dano (1), morrer (4) |

### 3.2 Goblin Mineiro
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, grupos de 2–4 (um leva lanterna) |
| Andares | 11, 12, 14, 18 |
| Comportamento | Trabalham a picar a parede. Quando te veem, um foge para chamar mais. Se o da lanterna morrer, os outros ficam às escuras (atacam pior) |
| Ataques | **Picaretada** (×1,1; aviso 0,4 s) · **Pedrada** (projétil; aviso 0,5 s) · **Bomba de Pó** (só o *Goblin Bombista*: atira uma bomba com rastilho de 1,5 s, área 3 m, ×1,8) |
| Fraco / Resiste | Raio / — |
| Drops | Minério de Ferro 40% · Engrenagem 20% · Pano Velho 25% · ouro extra |
| Elite | **Goblin Capataz**: chicote; os goblins perto dele ficam 30% mais rápidos |
| Animações | trabalhar (4), parado (4), mover (6), picaretada (4), atirar (4), dano (1), morrer (4) |

### 3.3 Golem de Pedra
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 12, 13, 17, 19, 20 |
| Comportamento | Disfarçado de pedregulho; levanta-se quando chegas a 4 m. Lento mas aguenta muito |
| Ataques | **Murro** (×1,4; aviso 0,6 s) · **Pisão**: área 2,5 m, 20% Atordoado (aviso 0,8 s: levanta o pé) · **Atirar Rocha** (aviso 1 s: arranca uma rocha do chão) |
| Fraco / Imune | Raio, **Martelo** (×1,5) / Veneno |
| Drops | Pedra 80% · Minério de Ferro 50% · Núcleo de Golem 15% |
| Elite | **Golem de Ferro**: DEF ×2, mas Raio faz ×2 |
| Animações | disfarce (1), levantar (6), parado (4), mover (4), murro (4), pisão (5), atirar (6), dano (1), morrer (6: desfaz-se em pedras) |

### 3.4 Toupeira Gigante
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido** |
| Andares | 11, 12, 16, 19 |
| Comportamento | Anda **debaixo do chão** (só se vê um monte de terra a mexer). Sai para atacar e volta a enterrar-se |
| Ataques | **Sair da Terra**: área pequena por baixo de ti (×1,3; aviso 0,7 s: o chão treme e racha) · **Garras** (combo de 2, ×1,0) |
| Fraco / Resiste | Raio, Água / Terra (−20% de Martelo) |
| Drops | Couro de Toupeira 55% · Garra de Toupeira 25% · minério aleatório 20% |
| Elite | **Toupeira Blindada**: placas de pedra nas costas |
| Animações | montículo (4), sair (4), parado (4), garras (4), enterrar (4), dano (1), morrer (4) |

### 3.5 Aranha da Caverna
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, grupos de 2–3 |
| Andares | 13, 14, 15, 17 |
| Comportamento | **Desce do teto** num fio quando passas por baixo (aviso: um fio de seda a brilhar). Depois ataca e recua |
| Ataques | **Mordida**: 40% Veneno (aviso 0,35 s) · **Teia**: projétil que causa Lentidão (aviso 0,5 s) · **Salto** de 4 m (aviso 0,5 s) |
| Fraco / Resiste | Fogo, Raio / Veneno |
| Drops | Seda de Aranha 60% · Glândula de Veneno 25% · Olho de Aranha 15% |
| Elite | **Aranha Saltadora**: saltos de 8 m |
| Animações | descer (4), parado (4), mover (4: 8 patas), morder (4), teia (4), saltar (4), dano (1), morrer (4) |

### 3.6 Kobold
| | |
|---|---|
| Tamanho | 32×32 (pequenos, ~20 px de altura) |
| Tipo | **Fraco**, grupos de 3–6 |
| Andares | 11, 14, 16, 18 |
| Comportamento | Homenzinhos-lagarto com lanternas e lanças. Põem **armadilhas** e fogem. Um deles tenta **soprar a tua tocha** |
| Ataques | **Estocada** (×0,9) · **Armadilha**: deixa no chão uma armadilha de espinhos (Atordoado 1 s se pisares) · **Sopro**: apaga a tua tocha (aviso 0,6 s: enche as bochechas) |
| Fraco / Resiste | Raio / Fogo |
| Drops | Engrenagem 30% · Carvão 40% · Lanterna Partida 20% |
| Elite | **Kobold Xamã**: cura os outros |
| Animações | parado (4), mover (6), estocada (4), pôr armadilha (4), soprar (4), dano (1), morrer (4) |

### 3.7 Lagarta de Cristal
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 13, 19 |
| Comportamento | Lagarta com cristais nas costas que **brilham** (ilumina à volta). Os cristais **refletem a magia** |
| Ataques | **Rolar**: vira uma bola de cristal e rola em linha (×1,4; aviso 0,8 s: enrola-se) · **Espinhos**: cristais saem à volta dela (área 2 m, aviso 0,6 s) · **Brilho**: Cegueira 2 s (aviso 0,5 s) |
| Fraco / Resiste | Raio, Martelo / **Magia (RES ×2)** |
| Drops | Escama de Cristal 50% · Cristal de Gruta 30% · Topázio 3% |
| Elite | **Lagarta Prismática**: os cristais mudam de cor e de elemento |
| Animações | parado (4), mover (6), enrolar (4), rolar (4), espinhos (4), brilho (3), dano (1), morrer (5) |

### 3.8 Fantasma Mineiro
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago + Voador** (atravessa paredes) |
| Andares | 12, 18 |
| Comportamento | Só aparece **no escuro**. **Só pode ser atingido quando está iluminado** (tocha, lanterna, cristal, fungo). Na luz fica lento e transparente |
| Ataques | **Toque Frio**: Frio (aviso 0,4 s) · **Lamento**: Medo 1 s em área (aviso 1 s: abre a boca) · **Picareta Fantasma**: projétil que gira e volta |
| Fraco / Imune | Luz, Raio / Veneno, Físico (no escuro) |
| Drops | Ectoplasma 50% · Capacete de Mineiro Velho 5% (cosmético) · página "Diário de Mineiro" 10% |
| Elite | **Capataz Fantasma**: chama 2 fantasmas |
| Animações | aparecer (4), flutuar (4), atacar (4), lamento (4), dano (1), desaparecer (4) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Rei Goblin Gruk** | andares 11, 12, 18, 3% (5% numa Invasão Goblin) | goblin gordo 48×48 com coroa de latão e um martelo de vagoneta | Martelo que faz ondas · chama 6 goblins · atira bombas grandes | Coroa de Latão (+10% ouro) · Martelo de Vagoneta (martelo raro) |
| **Toupeira Dourada** | qualquer andar da região, 2% | toupeira pequena de pelo dourado | **Não ataca**: foge debaixo do chão; tens 30 s para a apanhar (atordoa-a e bate-lhe) | 1 500 ouro · Pá Dourada (ferramenta: escava pontos de tesouro) · Garra Dourada |

---

## 5. Os andares

### Andar 11 — Entrada da Mina
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 11 |
| Bioma | Começa numa encosta rochosa com luz cinzenta; depois a boca de uma mina com carris, vagonetas, lanternas penduradas e vigas de madeira |
| Zonas | **Boca da Mina** · **Posto Mineiro Fundo-Rocha** (povoação) · **Galerias Altas** · **Estação de Vagonetas** |
| Mecânica especial | **Vagonetas**: entrar numa vagoneta faz uma **corrida nos carris** (inclinar para apanhar cristais e baixar nas vigas). Serve de atalho. **A escuridão começa** aqui |
| Monstros | Morcego, Goblin Mineiro, Toupeira Gigante, Kobold |
| Recursos | Minério de Ferro, Carvão, Escora Velha, Raiz-Pedra |
| Povoação | **Posto Mineiro Fundo-Rocha** (secção 7.1) |
| Guardião | **Vagoneta Assombrada** |
| Segredo | Um carril tapado com tábuas (partir com martelo ou machado) leva a um vagão perdido com **baú de prata** |
| Puzzle | **Agulhas dos carris**: mudar 4 alavancas para levar a vagoneta de minério até ao elevador |
| Página de lore 11 | *"A partir daqui é escuro. A janela azul brilha mais quando estou com medo."* |
| Desafios | Ganhar a corrida de vagonetas em menos de 60 s · Atravessar o andar sem acender tochas |
| Peças especiais | carris (reto, curva, cruzamento), vagoneta, elevador de mina, vigas de madeira, lanterna pendurada |

### Andar 12 — Túneis dos Mineiros Perdidos
| | |
|---|---|
| Tamanho / Nível | 240×240 m em 3 pisos · nível 12 |
| Bioma | Labirinto de túneis estreitos com vigas, mesas e ferramentas abandonadas, esqueletos de mineiros, uma galeria inundada |
| Zonas | **Labirinto Norte** · **Poço do Elevador** (liga os 3 pisos) · **Acampamento Perdido** · **Galeria Inundada** |
| Mecânica especial | **Portas de madeira** que os goblins abrem e fecham (o labirinto muda). **Giz de Mineiro**: marca setas nas paredes (aparecem no mapa) |
| Monstros | Goblin Mineiro, Fantasma Mineiro, Golem de Pedra, Toupeira Gigante, Morcego |
| Recursos | Minério de Ferro, Carvão, Musgo Luminoso, Escora Velha |
| Guardião | **Touro das Galerias** |
| Segredo | Os 3 diários do Acampamento Perdido têm cada um **um número**: são o código do **cofre do capataz** (baú de ouro + Picareta de Ferro Boa) |
| Puzzle | O cofre (código de 3 números) |
| Página de lore 12 | *"Encontrei mineiros que vieram antes de mim. Não tinham janela azul. Eram deste mundo… ou de outro já engolido."* |
| Desafios | Encontrar a saída sem usar o mapa · Matar 5 fantasmas com luz de cristal |
| Peças especiais | túnel estreito (reto, curva, T), porta de madeira de mina, mesa de mineiro, esqueleto, galeria com água |

### Andar 13 — Gruta de Cristal
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 13 |
| Bioma | Gruta enorme cheia de cristais gigantes de várias cores que dão luz; estalactites; reflexos coloridos nas paredes |
| Zonas | **Salão das Cores** · **Jardim de Estalactites** · **Ponte de Quartzo** · **Coração Prismático** |
| Mecânica especial | **Cristais de cor**: bater num cristal muda a cor da luz da sala (vermelho, azul, amarelo). Há **pontes e portas que só existem com uma cor** |
| Monstros | Lagarta de Cristal, Aranha da Caverna, Golem de Pedra, Morcego |
| Recursos | Cristal de Gruta (muito), Topázio, Minério de Ferro, Ametista (sala secreta) |
| Guardião | **Prisma Vivo** |
| Segredo | Misturar **vermelho + azul** (dois cristais ao mesmo tempo) dá **violeta**, que mostra a **Sala Violeta** com a Ametista Grande |
| Puzzle | **Ponte de Quartzo**: atravessar mudando a cor no momento certo (a ponte tem partes de cores diferentes) |
| Página de lore 13 | *"Os cristais cantam quando lhes toco. A nota é a mesma do som da janela azul."* |
| Desafios | Atravessar a Ponte de Quartzo sem cair · Encontrar a Sala Violeta |
| Peças especiais | cristais gigantes (3 cores), estalactites, ponte de quartzo, cristal-interruptor |

### Andar 14 — Rio Subterrâneo
| | |
|---|---|
| Tamanho / Nível | 260×200 m · nível 14 |
| Bioma | Rio negro que corre numa gruta enorme; cais de madeira, barcos, pontes de corda, uma cascata escura, peixes cegos que brilham |
| Zonas | **Cais da Gruta** · **Pontes de Corda** · **Cascata Escura** · **Ilha dos Ossos** |
| Mecânica especial | **Barco de corrente**: o barco segue o rio e escolhes o caminho nas bifurcações. **Pontes de corda** balançam e os Kobolds tentam cortá-las |
| Monstros | Aranha da Caverna, Kobold, Goblin Mineiro, Morcego |
| Recursos | Minério de Ferro, Seda de Aranha, peixes, Musgo |
| Guardião | **Barqueiro Afogado** |
| Segredo | Atrás da Cascata Escura há uma gruta com o **Remo Dourado** (decoração para a casa) e um baú de prata |
| Puzzle | **Boias de luz**: acender 3 boias na ordem certa abre a eclusa para a Ilha dos Ossos |
| Página de lore 14 | *"Remei durante horas. O rio corre em círculo. A torre gosta de círculos."* |
| Desafios | Fazer o rio todo de barco sem cair · Pescar um Peixe-Cego |
| Peças especiais | cais de madeira, barco, ponte de corda, cascata escura, boia de luz, ossos grandes |

### Andar 15 — Ninho das Aranhas 💀
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 15 |
| Bioma | Gruta coberta de teias brancas, casulos pendurados, ovos que pulsam, luz roxa e fria |
| Zonas | **Teias da Entrada** · **Casulos** · **Câmara dos Ovos** · **O Ninho** (arena do mini-boss) |
| Mecânica especial | **Teias**: andar em teia causa Lentidão. **Queimar** teias com tocha ou fogo abre caminhos. **Casulos**: 3 têm aventureiros presos (resgatar) |
| Monstros | Aranha da Caverna (muitas), Morcego |
| Recursos | Seda de Aranha (muita), Glândula de Veneno, Cristal de Gruta |
| Mini-boss | **Aranha-Mãe** (ver `docs/BOSSES.md`) → arma única **Presa Venenosa** (adaga). É o sprite de referência em `arte/referencia/aranha_mae/` |
| Segredo | Um casulo dourado tem um **ovo de aranha**: o Zed choca-o e dá uma **Aranha de Seda** (decoração viva para a casa: faz Seda de Aranha todos os dias) |
| Página de lore 15 | *"Ela protegia os filhos. Eu protegia-me a mim. A janela disse 'Vitória'. Não me senti vitorioso."* |
| Desafios | Libertar os 3 aventureiros · Vencer a Aranha-Mãe sem queimar as teias da arena |
| Peças especiais | teias (parede, chão, canto), casulos, ovos, teia gigante da arena |

### Andar 16 — Cavernas Fúngicas
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 16 |
| Bioma | Floresta subterrânea de fungos gigantes azuis e verdes que brilham; esporos a flutuar como neve luminosa; lagos que brilham |
| Zonas | **Floresta de Fungos** · **Mycélia** (povoação) · **Lago Bioluminescente** · **Raízes Profundas** |
| Mecânica especial | **Fungos-luz**: tocar num fungo ilumina à volta durante 30 s. **Esporos-trampolim** levam a plataformas altas |
| Monstros | Toupeira Gigante, Kobold, Morcego, Lagarta de Cristal |
| Recursos | **Fungo-Lenho**, Musgo Luminoso, Cogumelo Luminoso, peixes |
| Povoação | **Mycélia, Cidade dos Fungoides** (secção 7.2) |
| Guardião | **Água-Viva Fúngica** |
| Segredo | No fundo do Lago Bioluminescente (mergulhar com a Poção de Respirar) há uma **Pérola Azul** (presente que todos adoram) |
| Puzzle | **Coro dos fungos**: tocar em 5 fungos que fazem notas para repetir a melodia que o Ancião canta |
| Página de lore 16 | *"Os Fungoides dizem que a torre é um ser vivo. Que nós somos o que ela come."* |
| Desafios | Atravessar o andar só com a luz dos fungos · Repetir a melodia à primeira |
| Peças especiais | fungos gigantes (3 tipos), casas-cogumelo, lago luminoso, esporo-trampolim |

### Andar 17 — Fosso dos Ecos
| | |
|---|---|
| Tamanho / Nível | 120×120 m de largura e **150 m de profundidade** · nível 17 |
| Bioma | Um poço gigante vertical: plataformas de pedra nas paredes, correntes, elevadores velhos, ninhos de morcegos, vento a subir |
| Zonas | **Borda Superior** · **Plataformas Suspensas** · **Ninhos de Morcegos** · **Fundo do Fosso** (a escada está no fundo) |
| Mecânica especial | **Descer**: plataformas, elevadores de corrente e correntes de ar que travam a queda. **Pontos de eco**: gritar (interagir) mostra plataformas invisíveis durante 5 s. Com o **Gancho** há atalhos |
| Monstros | Morcego (muitos), Golem de Pedra, Aranha da Caverna |
| Recursos | Raiz-Pedra, Minério de Ferro, Guano, ovos de morcego |
| Guardião | **Morcego-Rei dos Ecos** |
| Segredo | Um ninho na parede, só alcançável com o Gancho, tem o **ovo do Morceguinho** (animal de estimação) |
| Puzzle | **Plataformas invisíveis**: usar os pontos de eco para descer pela parede norte até à sala do Gancho |
| Página de lore 17 | *"Gritei o meu nome no fosso. O eco respondeu com outro nome."* |
| Desafios | Chegar ao fundo sem levar dano de queda · Chegar ao fundo em menos de 2 min |
| Peças especiais | plataforma de parede, corrente com gancho, elevador de corrente, ninho de morcego, ponto de eco (pedra com espiral) |

### Andar 18 — Forja Anã Abandonada
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 18 |
| Bioma | Salões de pedra enormes esculpidos por anões, colunas com caras de anões, fornalhas apagadas, rios de metal frio, runas |
| Zonas | **Grande Portão Anão** · **Salão das Forjas** · **Minas Profundas Anãs** · **Câmara do Mestre** |
| Mecânica especial | **Reacender as fornalhas**: acender 3 fornalhas (com Carvão) ilumina o salão e liga elevadores e portas. **Fantasmas anões amigáveis** (só se veem com luz) contam histórias |
| Monstros | Goblin Mineiro, Kobold, Fantasma Mineiro, Golem de Pedra |
| Recursos | Minério de Ferro, Carvão, **Rubi**, Lingotes antigos (baús) |
| NPCs | **Fantasma de Grimbold** (pai do Brom) e fantasmas anões |
| Guardião | **Sentinela Anã** |
| Segredo | O **Livro de Runas Anãs** (receitas de armas de ferro superiores) e a entrada da masmorra escondida |
| Puzzle | **Runas do portão**: rodar 4 anéis de pedra com runas até formarem o nome "BROM" (pista: a missão do martelo) |
| Página de lore 18 | *"Os anões forjavam aqui as armas de outros Jogadores. Então houve outros antes de mim. Muitos."* |
| Desafios | Reacender as 3 fornalhas em menos de 3 min · Derrotar a Sentinela sem a deixar sobreaquecer |
| Peças especiais | fornalha anã, coluna com cara, portão com anéis de runas, bigorna gigante, rio de metal |

### Andar 19 — Lago de Cristal Negro
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 19 |
| Bioma | Um lago que **cristalizou**: superfície negra e lisa como um espelho onde se anda; estalagmites; o teu reflexo segue-te por baixo |
| Zonas | **Margem de Vidro Negro** · **Lago Espelhado** · **Ilhas de Estalagmites** · **Altar do Reflexo** |
| Mecânica especial | **O reflexo**: às vezes o teu reflexo faz coisas diferentes de ti — aponta para segredos. **Buracos de pesca** no cristal |
| Monstros | Lagarta de Cristal, Golem de Pedra, Toupeira Gigante, Fantasma Mineiro |
| Recursos | Cristal de Gruta, Cristal Negro (raro), Minério de Ferro, peixes |
| Guardião | **Reflexo Negro** |
| Segredo | Seguir o que o reflexo aponta leva a 3 **fendas** com baús de prata |
| Puzzle | **Espelhos**: rodar 4 estalagmites espelhadas para levar a luz do teu cristal até ao altar |
| Página de lore 19 | *"O meu reflexo sorriu antes de mim. Quem é que está a copiar quem?"* |
| Desafios | Pescar o Peixe de Vidro · Derrotar o Reflexo Negro sem poções |
| Peças especiais | chão de cristal negro, estalagmite espelhada, buraco de pesca, altar do reflexo |

### Andar 20 — Trono do Golem 👑
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 20 |
| Bioma | Um salão gigante com uma escadaria de degraus enormes (feita para gigantes), colunas de cristal e um trono de pedra |
| Zonas | **Escadaria dos Gigantes** · **Salão das Colunas** · **Sala do Trono** (arena do boss) |
| Mecânica especial | **Colunas de cristal**: o boss usa-as como escudo; partir as colunas tira-lhe o escudo |
| Monstros | Golem de Pedra, Golem de Ferro (elite), Lagarta de Cristal |
| Recursos | Cristal de Gruta, Núcleo de Golem, Minério de Ferro |
| Boss | **Golem de Cristal** (ver `docs/BOSSES.md`) → arma única **Núcleo de Cristal** (martelo) |
| Depois do boss | **Dia da Subida**. O Governador Aldric oferece-te uma **casa** em Ascendia (abre a casa própria) |
| Página de lore 20 | *"O Golem ajoelhou-se antes de cair. Não para mim. Para a janela azul."* |
| Desafios | Vencer o boss sem partir colunas · Vencer em menos de 4 min |
| Peças especiais | degraus gigantes, colunas de cristal, trono de pedra |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 11 | **Vagoneta Assombrada** | vagoneta de ferro com olhos de brasa à frente e dentes de carril (48×48) | Atropelar (anda nos carris: sai dos carris!) · Atirar Carvão (3 projéteis) · Apito (chama morcegos). Mudar as agulhas dos carris faz descarrilar → fica atordoada 4 s | Raio | **Martelo Carril** (martelo): o ataque carregado faz uma onda de choque em linha |
| 12 | **Touro das Galerias** | homem-touro mineiro (64×64) com capacete e picareta gigante | Investida no túnel (bate na parede: atordoado 3 s) · Picareta Giratória · Rugido (pedras caem do teto) | Raio | **Chifre-Picareta** (machado): também minera como uma picareta de tier 3 |
| 13 | **Prisma Vivo** | cristal flutuante (48×48) com núcleo que muda de cor | Laser que ressalta nos cristais · Estilhaços · Brilho (Cegueira). Muda de cor a cada 10 s: a cor diz o elemento que lhe faz ×2 | muda | **Cajado Prisma** (cajado): cada projétil tem elemento ao acaso (Fogo, Gelo ou Raio) |
| 14 | **Barqueiro Afogado** | esqueleto de capa num barco com lanterna verde (48×48) | Remada (área) · Lanterna de Fogo-Fátuo (projétil que persegue) · Mãos da Água (puxam-te para a água) | Luz, Raio | **Remo do Barqueiro** (lança): empurra muito; +20% dano em inimigos na água |
| 16 | **Água-Viva Fúngica** | fungo flutuante em forma de medusa (64×64) com tentáculos luminosos | Tentáculos (Veneno + Lentidão) · Chuva de Esporos Luminosos (Cegueira) · Pulso de Luz (empurra) | Fogo | **Foice Micélio** (foice): os golpes deixam esporos no chão que te curam 1% por segundo |
| 17 | **Morcego-Rei dos Ecos** | morcego gigante (64×64) com orelhas enormes | Onda Sonora (anel que cresce: esquivar) · **Eco** (repete o teu último ataque contra ti) · Mergulho | Raio, Luz | **Besta Ressonante** (besta): os virotes ressaltam para mais 1 inimigo |
| 18 | **Sentinela Anã** | autómato anão de bronze (48×48) com fornalha no peito | Martelada · Jato de Fogo (cone) · **Sobreaquecer**: fica vermelha (faz ×1,5 e leva ×1,5) | Gelo, Raio | **Manoplas da Fornalha** (manoplas): o 6.º golpe do combo causa Queimadura |
| 19 | **Reflexo Negro** | silhueta negra de ti mesmo (32×32) com olhos roxos | **Copia a tua arma e as tuas skills**; troca de lugar contigo (teletransporte) | Luz | **Lâmina Reflexo** (katana): 15% de hipótese de o golpe se repetir (eco) |

---

## 7. Povoações

### 7.1 Posto Mineiro Fundo-Rocha (andar 11)
Posto de mineiros de Ascendia (humanos e alguns anões) na boca da mina. Casas de madeira encostadas à rocha,
uma forja pequena, uma cantina, montes de minério. Tem **cama**, **cristal**, **forja simples** (fazer lingotes).

| NPC | Quem é | O que faz |
|---|---|---|
| **Hilda Fundo-Rocha** | anã, chefe do posto; braços enormes, trança ruiva | Loja: picaretas, **tochas**, Giz de Mineiro, Carvão. Missões. Organiza a corrida de vagonetas |
| **Pedrito** | rapaz de 16 anos, aprendiz de ferreiro | Quer aprender com o Brom (missão R2_13) |
| **Dona Graça** | cozinheira | Vende Sopa de Mineiro (+20% DEF 5 min); ensina a receita com 4 corações |
| **Senhor Ruivo** | mineiro velho e meio cego | Sabe tudo dos túneis: missão dos mineiros perdidos; vende mapas |

### 7.2 Mycélia, Cidade dos Fungoides (andar 16)
Cidade de **Fungoides**: seres-cogumelo pequenos e pacíficos que falam devagar e comunicam com luz.
Casas dentro de fungos gigantes, pontes de lamelas, lagos luminosos. Tem **estalagem-cogumelo**, **cristal** e **loja**.
Os Fungoides gostam de trocas: aceitam **Cogumelos Luminosos** como dinheiro.

| NPC | Quem é | O que faz |
|---|---|---|
| **Ancião Gorro-Azul** | o fungoide mais velho, fala muuuito devagar (há opção para acelerar) | Missão "Luz para Mycélia"; sabe que a torre é "viva" |
| **Pila** | fungoide comerciante | Esporos de Fungo Azul (sementes), Poção de Visão Noturna, Poção de Luz |
| **Mestre Lamela** | professor de cogumelos | Ensina receitas com cogumelos (cozinha e alquimia) |
| **Bolota** | jovem fungoide curioso | Quer ver o sol (missão R2_06) |

### 7.3 Fantasmas da Forja Anã (andar 18)
Não é uma povoação viva: são **fantasmas de anões** que continuam a "trabalhar". Com luz, falam contigo.
- **Grimbold Martelo-Forte**: pai do Brom; missão "O Martelo do Pai".
- **Os Ferreiros Fantasmas**: se reacenderes as fornalhas, vendem **Lingotes Antigos** (ferro de qualidade Boa).

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R2_01 | Tochas para Todos | Hilda | Entregar 20 Carvão | 200 ouro · 10 Tochas · Giz de Mineiro |
| R2_02 | O Gancho | Gizmo (Ascendia) | Trazer 5 Engrenagens e 10 Lingotes de Ferro | **Gancho** |
| R2_03 | Mineiros Perdidos | Senhor Ruivo | Encontrar os 4 diários dos mineiros no andar 12 | Mapa dos Túneis · 400 ouro |
| R2_04 | Resgate no Ninho | Capitã Freya | Libertar os 3 aventureiros dos casulos (andar 15) | 600 ouro · 30 pontos de Guilda · os 3 vão viver para Ascendia |
| R2_05 | O Martelo do Pai | Brom | Encontrar o fantasma do pai e o Martelo Forte-Rocha (andar 18) | ❤️❤️ Brom · Brom ensina **Forja Anã** (+10% de sucesso nas melhorias) |
| R2_06 | Bolota Quer Ver o Sol | Bolota (Mycélia) | Levar o Bolota até Ascendia | O Bolota vive na quinta da Hana · Esporos de Fungo Azul ×10 |
| R2_07 | Luz para Mycélia | Ancião Gorro-Azul | Entregar 30 Cogumelos Luminosos | Receita Poção de Visão Noturna |
| R2_08 | A Cor Violeta | Velho Fausto (Ascendia) | Encontrar a Sala Violeta (andar 13) | Ametista Grande · página de lore extra |
| R2_09 | Corrida de Vagonetas | Hilda | Ganhar a corrida em menos de 60 s | Capacete de Mineiro (luz própria de 4 m) · 300 ouro |
| R2_10 | O Rei Goblin | Quadro da Guilda (rank D) | Derrotar o Rei Goblin Gruk | 900 ouro · Coroa de Latão |
| R2_11 | A Toupeira Dourada | Tobias | Apanhar a Toupeira Dourada | Pá Dourada · 1 000 ouro |
| R2_12 | O Outro Eu | Madame Oriel | Derrotar o Reflexo Negro sem usar poções | Amuleto do Espelho (reflete 10% do dano mágico) |
| R2_13 | Aprendiz do Brom | Pedrito | Levar o Pedrito a Ascendia e convencer o Brom (escolha de diálogo) | O Pedrito trabalha na forja: melhorias +1 a +5 ficam 20% mais baratas |
| R2_14 | Sopa de Mineiro | Dona Graça | Trazer 5 Carne + 5 Raiz-Pedra + 1 Cogumelo Luminoso | Receita Sopa de Mineiro |

---

## 9. Masmorra escondida — Mina do Rei Anão (andar 18)

| | |
|---|---|
| Entrada | Debaixo do Salão das Forjas; abre com o **Livro de Runas Anãs** |
| Sala 1 | **Ponte que Cai**: as pedras caem 1 s depois de as pisares |
| Sala 2 | **Corredor das Lâminas**: lâminas anãs que saem das paredes em ritmo |
| Sala 3 | **Câmara do Ouro**: 4 Golens de Ferro guardam montes de ouro; não se pode apanhar o ouro antes de os vencer |
| Boss extra | **Rei Anão Esquecido**: fantasma de um rei anão (64×64) com machado de duas mãos. Golpes enormes em área, chama fantasmas, fica invisível sem luz (tem de haver luz na sala: acender os 4 braseiros) |
| Recompensa | **Machado do Rei Sob a Montanha** (arma secreta, machado): +25% de dano a golems e minera como uma picareta de tier 5 · baú de ouro · página de lore extra "A Coroa" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Peixe-Cego | andar 14 | sempre | comum | 40 |
| Caranguejo de Gruta | cais do andar 14 | sempre | comum | 45 |
| Carpa de Cristal | poças do andar 13 | sempre | incomum | 90 |
| Truta Fúngica | lago do andar 16 | sempre | incomum | 80 |
| Enguia Elétrica | andar 14 | com o rio "agitado" (evento) | raro | 220 |
| **Peixe de Vidro** (lendário) | buracos do andar 19 | 0:00–3:00 | lendário | 2 500 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Fungo Azul | Mycélia | 3 (dá mais vezes) | todas, **à sombra** (estufa escura) | cozinha, poções de luz |
| Raiz-Pedra | andar 11/17 (raiz com terra) | 7 | Outono, Inverno | Poção de Defesa |
| Batata Roxa da Gruta | Hilda | 5 | todas, à sombra | cozinha (Sopa de Mineiro) |

### Animais
- **Morceguinho** (animal de estimação): ovo do ninho secreto do andar 17. **Ilumina** 6 m à tua volta (já não precisas de tochas).
- **Aranha de Seda** (decoração viva da casa): ovo dourado do andar 15. Dá 2 Sedas de Aranha por dia.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Desmoronamento | 10% ao entrar num andar | Um caminho fica tapado; aparece outro caminho com um baú |
| Veio Brilhante | 1 por dia num andar ao acaso | Um nó de minério brilha: dá 5× minério e uma gema garantida |
| Invasão Goblin | 1 vez por semana | Ondas de goblins atacam o **Posto Mineiro**; defendê-lo dá recompensas e um desconto na loja |
| Silêncio | 5% por hora nos andares 12 e 18 | Todas as tochas apagam-se 30 s e aparecem fantasmas |
| Rio Agitado | 1 dia em cada 5, andar 14 | Correnteza forte; aparece a Enguia Elétrica |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 28): parede de rocha, chão de rocha ×3, túnel (reto, curva, T), viga de mina, carris (reto, curva, cruzamento),
  estalactite, estalagmite, rocha ×3, minério de ferro, veio de carvão, escora (cortável), cristal (3 cores), baú, fogueira, cristal de teletransporte, tocha de parede, lanterna, ponte de corda, escada de madeira
- [ ] **Peças especiais dos andares** (≈ 45): ver cada andar
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Rei Goblin Gruk, Toupeira Dourada
- [ ] **8 guardiões**
- [ ] **Mini-boss** Aranha-Mãe (já há referência) e **boss** Golem de Cristal
- [ ] **Boss da masmorra** Rei Anão Esquecido
- [ ] **Armas**: 12 de Ferro + 2 únicas + 8 de guardião + 1 secreta = **23 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 22), **peixes** (6), **plantas** (3 × 4 fases)
- [ ] **NPCs**: Hilda, Pedrito, Dona Graça, Senhor Ruivo, Gorro-Azul, Pila, Lamela, Bolota, Grimbold (+ retratos dos principais)
- [ ] **Animais**: Morceguinho, Aranha de Seda
- [ ] **Conjunto de armadura** de Ferro (5 ícones)
