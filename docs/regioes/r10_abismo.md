# Região 10 — Abismo / Coração da Torre (andares 91–100)

> Estrutura igual às outras regiões. Bosses grandes (Guardião do Tempo e O Administrador) em `docs/BOSSES.md`.
> Esta região tem o **fim da história** e os **4 finais** (ver `docs/HISTORIA.md`).

---

## 1. Identidade

| | |
|---|---|
| Tema | O interior da própria torre: o vazio entre mundos, estrelas, espelhos, ecos de tudo o que já se viu, o tempo, a cidade de quem desistiu, a biblioteca de todos os mundos e o topo |
| Sensação | Estranheza, maravilha, melancolia e decisão final |
| Material das armas | **Estelar** (tier 10) |
| Monstros fracos a | **Luz** |
| Cores principais | preto do vazio `#2e222f`, roxos `#45293f` `#6b3e75` `#a884f3`, estrelas `#ffffff` `#8fd3ff` `#fbff86`, azul do Sistema `#4d9be6` `#4d65b4` |
| Luz | escuro profundo com estrelas e nebulosas; luz que vem dos objetos (âncoras, estrelas, ecos); o azul do Sistema por todo o lado no topo |
| Clima | não há clima; há **Falhas do Sistema** (ver abaixo) |
| Música | `vazio`, `mar_de_estrelas`, `ecos` (pedaços das músicas de todas as regiões), `cidade_dos_perdidos`, `guardiao_do_tempo`, `administrador`, `casa` |
| Níveis | monstros 91–101; mini-boss 97; boss 103 |
| Mecânica da região | **Escuridão do vazio**: fora das ilhas e zonas iluminadas não se vê nada. **Âncoras de luz**: acendê-las torna a zona estável e segura. **Falhas do Sistema** (*glitches*): zonas com quadrados coloridos onde as coisas falham — o chão desaparece por instantes, inimigos copiam-se, a interface mostra valores errados, o mapa mente. Quanto mais perto do topo, mais falhas |
| Animal de estimação | Mini-Estrela |

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Fragmento Estelar | estrelas caídas, Devoradores (92, 94, 99) | Picareta de Oricalco+ | Lingote Estelar (3 Fragmentos + 1 Núcleo do Vazio) |
| Núcleo do Vazio | Olho do Vazio, fendas do vazio (91, 98) | drop / Picareta | **cristal** da região e **combustível** da Forja Estelar |
| Madeira do Tempo | Árvores do Tempo (95) | Machado | **madeira** da região |
| Pele do Vazio | Sombra | drop | **couro** da região |
| Fio de Luz Estelar | Anjo do Vazio, nebulosa (92) | drop / à mão | **fio** da região |
| Gema Prismática | centro do andar 94 (rara) | Picareta | gema de **todos os elementos** (armas míticas) |
| Fragmento de Sistema | zonas de Falha (todas) | interagir com a falha | armas míticas, missão do Doutor |
| Fragmento de Eco | Ecos | drop | trocar no Mercado das Memórias por materiais de qualquer região |
| Lótus Estelar | lagos de luz (92, 95) | à mão | Elixir Estelar |
| Areia do Tempo | Relógio Vivo, ampulheta (95) | drop | poções de tempo |

---

## 3. Monstros

### 3.1 Sombra
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, 2–4 |
| Andares | 91, 93, 96, 99 |
| Comportamento | Silhuetas escuras com olhos brancos. **Só levam dano normal na luz**; no escuro levam metade. Entram **na tua sombra** e saem atrás de ti |
| Ataques | **Golpe Sombrio** · **Entrar na Sombra**: teletransporte para trás de ti (aviso 0,5 s: a tua sombra mexe-se) · **Agarrar**: Medo |
| Fraco / Resiste | **Luz (×2)** / Físico no escuro (−50%) |
| Drops | Essência de Sombra 50% · Pele do Vazio 20% |
| Elite | **Sombra Maior**: duas ao mesmo tempo saem da tua sombra |
| Animações | parado (4), mover (6), golpe (4), afundar na sombra (4), sair (4), dano (1), desfazer (4) |

### 3.2 Olho do Vazio
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago + Voador** |
| Andares | 91, 92, 94, 98 |
| Comportamento | Um olho gigante com tentáculos que flutua. **Vê-te de muito longe** (15 m) |
| Ataques | **Olhar**: laser que te segue durante 2 s (aviso 0,8 s: a pupila encolhe) · **Piscar**: teletransporte · **Hipnose**: Lentidão |
| Fraco / Resiste | Luz / Sombra |
| Drops | Lente do Vazio 40% · Núcleo do Vazio 10% |
| Elite | **Olho Ancião**: 3 lasers |
| Animações | flutuar (4), olhar (4), piscar (3), hipnose (4), dano (1), morrer (5) |

### 3.3 Clone Espelhado
| | |
|---|---|
| Tamanho | 32×32 (tamanho do herói) |
| Tipo | **Normal** |
| Andares | 93, 96, 99 |
| Comportamento | **Uma cópia de ti** feita de vidro: usa a tua arma equipada (com metade da força) e **repete as tuas ações** meio segundo depois |
| Ataques | os teus |
| Fraco / Resiste | Martelo (o vidro parte), Luz / — |
| Drops | Estilhaço de Espelho 50% · Fragmento Estelar 20% |
| Elite | **Clone Perfeito**: força igual à tua |
| Animações | usa as animações do herói com um shader de vidro (não precisa de desenho novo) |

### 3.4 Devorador de Estrelas
| | |
|---|---|
| Tamanho | 64×64 |
| Tipo | **Tanque** |
| Andares | 92, 94, 99 |
| Comportamento | Criatura enorme e escura que **come a luz**: apaga âncoras, lanternas e a tua luz |
| Ataques | **Engolir a Luz**: Cegueira e apaga a tua luz 10 s (aviso 1 s: abre a boca e as estrelas são sugadas) · **Mordida** · **Gravidade**: puxa-te |
| Fraco / Resiste | Luz / Sombra |
| Drops | Fragmento Estelar 45% · Dente Estelar 20% |
| Elite | **Devorador de Galáxias**: puxa com mais força |
| Animações | parado (4), mover (4), sugar (6), mordida (4), dano (1), morrer (6) |

### 3.5 Relógio Vivo
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal + Mago** |
| Andares | 95, 98, 99 |
| Comportamento | Um relógio de pé com braços e pernas. Brinca com o tempo |
| Ataques | **Ponteiros** (golpes) · **Parar o Tempo**: ficas **Parado** 1 s (aviso: o tique-taque fica mais alto) · **Acelerar**: ele fica 2× mais rápido 3 s · **Rebobinar**: volta à vida que tinha 5 s antes (uma vez) |
| Fraco / Resiste | Martelo, Raio / — |
| Drops | Engrenagem do Tempo 40% · Areia do Tempo 25% |
| Elite | **Relógio de Ouro**: para o tempo 2 s |
| Animações | parado (4: pêndulo), mover (4), ponteiros (4), parar o tempo (4), rebobinar (6 ao contrário), dano (1), morrer (5) |

### 3.6 Eco
| | |
|---|---|
| Tamanho | igual ao monstro original (32–48) |
| Tipo | o do monstro original |
| Andares | 94 (sobretudo), 97 (arredores), 99 |
| Comportamento | **Versões escuras de monstros das regiões anteriores** (Slime Eco, Lobo Eco, Múmia Eco, Pinguim Eco…). Fazem os ataques do original e às vezes **repetem** o ataque |
| Fraco / Resiste | Luz / — |
| Drops | Fragmento de Eco 50% |
| Elite | **Eco Brilhante**: repete sempre |
| Animações | **usam os sprites dos monstros originais** com um shader roxo escuro (não precisa de desenho novo) |

### 3.7 Anjo do Vazio
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Mago + Voador** |
| Andares | 98, 99, 100 |
| Comportamento | Anjos negros com asas cheias de estrelas: os **servos do Administrador** |
| Ataques | **Lança Estelar** · **Buraco Negro Pequeno**: puxa tudo durante 3 s · **Selo**: ficas em **Silêncio** 3 s (não podes usar skills) |
| Fraco / Resiste | Luz / Sombra |
| Drops | Pena Estelar 40% · Fio de Luz Estelar 20% |
| Elite | **Anjo do Vazio Superior**: dois buracos negros |
| Animações | voar (4), lança (4), buraco negro (6), selo (4), dano (1), morrer (5) |

### 3.8 Fragmento de Mundo
| | |
|---|---|
| Tamanho | 64×64 |
| Tipo | **Tanque** |
| Andares | 94, 96, 97 |
| Comportamento | Um golem feito de **pedaços de todos os biomas** (uma perna de gelo, um braço de lava, a cabeça de coral, as costas de areia…). **Muda de elemento** a cada golpe que dá (a cor mostra qual) |
| Ataques | **Pisão** · **Lançar um Pedaço** (com o elemento do momento) · **Trocar de Bioma**: o chão à volta vira esse bioma 5 s |
| Fraco / Resiste | o elemento **oposto** ao que tem no momento (Fogo↔Gelo, Raio↔Veneno, Luz↔Sombra) |
| Drops | 1 material ao acaso de qualquer região · Fragmento Estelar 30% |
| Elite | **Fragmento de Continente**: muda de elemento a cada 2 s |
| Animações | parado (4), mover (4), pisão (5), lançar (5), trocar (4), dano (1), morrer (6: desfaz-se em biomas) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Devorador Ancestral** | andares 92, 99, 3% | devorador gigante (128×128) que **come as estrelas do céu do andar** | O andar vai escurecendo; luta-se com fragmentos de luz que se apanham do chão e se atiram | **Coração Estelar** (material das armas míticas) · título *Guardião das Estrelas* |
| **O Jogador Sem Número** | andares 93, 97, 99, 2% | figura com máscara branca; a janela azul por cima dele mostra "????" | Usa armas diferentes a cada fase; **fala contigo durante a luta**: tenta convencer-te a recusar o Sistema. É o nome **raspado** da porta da pirâmide (andar 38). Chama-se **Teodoro** (só o diz no fim: cena C10-13) | **Máscara Sem Número** (imune a Parado e a Silêncio) · página de lore secreta "O Nome Raspado" |

---

## 5. Os andares

### Andar 91 — Porta do Vazio
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 91 |
| Bioma | Ilhas de pedra a flutuar no escuro total, com estrelas muito longe; um acampamento abandonado; uma ponte para o nada; um portão gigante cheio de estrelas |
| Zonas | **Último Posto** (povoação) · **Ponte para o Nada** · **Portão Estelar** · **Ilhas no Escuro** |
| Mecânica especial | **Escuridão do vazio**. **Âncoras de luz** (acender 5: missão R10_01). **Falhas do Sistema** começam (poucas) |
| Monstros | Sombra, Olho do Vazio |
| Recursos | Núcleo do Vazio, Fragmento Estelar (pouco), Fragmento de Sistema |
| Povoação | **Último Posto** (secção 7.1) |
| Guardião | **Porteiro do Vazio** |
| Segredo | No fim da Ponte para o Nada, saltar para o escuro (com coragem) leva a uma ilha invisível com um baú de ouro e uma mensagem da última expedição da Guilda, de há 60 anos |
| Puzzle | **Âncoras**: acender as âncoras pela ordem em que as estrelas piscam |
| Página de lore 91 | *"Aqui acaba a torre que se vê. O resto é a torre por dentro."* |
| Desafios | Acender as 5 âncoras · Atravessar a Ponte para o Nada sem luz |
| Peças especiais | ilha de pedra no vazio, âncora de luz, portão estelar, ponte para o nada, tendas abandonadas |

### Andar 92 — Mar de Estrelas
| | |
|---|---|
| Tamanho / Nível | 300×300 m · nível 92 |
| Bioma | Andar **por cima do espaço**: caminhos feitos de estrelas, nebulosas coloridas, cometas a passar, planetas pequeninos com gravidade própria |
| Zonas | **Caminho de Estrelas** · **Nebulosa** · **Cemitério de Cometas** · **Planeta Pequeno** |
| Mecânica especial | **Caminhos de estrelas**: aparecem quando ligas uma constelação (tocar nas estrelas pela ordem). **Planetas pequenos**: anda-se à volta deles (gravidade redonda!). **Nebulosa**: dentro dela curas-te, mas a câmara roda |
| Monstros | Olho do Vazio, Devorador de Estrelas, Sombra |
| Recursos | **Fragmento Estelar**, **Fio de Luz Estelar**, Lótus Estelar |
| Guardião | **Baleia Estelar** |
| Segredo | No Planeta Pequeno, dar uma volta completa a andar (sem parar) abre um alçapão com a **Mini-Estrela** (missão R10_15) |
| Puzzle | **Constelações**: ligar 5 constelações para fazer o caminho até ao Planeta Pequeno (R10_03) |
| Página de lore 92 | *"Andei por cima das estrelas. Lá em baixo, um planeta azul parecido com o meu. Não era o meu."* |
| Desafios | Ligar as 5 constelações · Dar a volta ao planeta em menos de 30 s |
| Peças especiais | caminho de estrelas, nebulosa (efeito), cometa, planeta pequeno (esfera), estrela grande |

### Andar 93 — Labirinto de Espelhos
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 93 |
| Bioma | Um labirinto infinito de espelhos com molduras douradas; reflexos de ti por todo o lado; alguns espelhos partidos mostram outros sítios |
| Zonas | **Galeria de Espelhos** · **Sala dos Mil Reflexos** · **Espelho Partido** · **Saída Verdadeira** |
| Mecânica especial | **Espelhos-porta**: alguns espelhos atravessam-se (mostram um reflexo diferente do teu). **Os teus reflexos atacam** (Clones Espelhados) |
| Monstros | Clone Espelhado, Sombra |
| Recursos | Estilhaço de Espelho, Fragmento Estelar |
| Guardião | **Rainha dos Espelhos** |
| Segredo | O **Espelho Partido**: juntar os 7 estilhaços espalhados pelo andar (R10_04) mostra o teu reflexo **do mundo real** |
| Puzzle | **Reflexo diferente**: os espelhos-porta são os que mostram o teu reflexo **com a arma na outra mão** |
| Página de lore 93 | *"Num espelho vi-me velho, com uma coroa. Num outro, vi-me em casa. Escolhi não olhar mais."* |
| Desafios | Sair do labirinto em 4 min · Vencer 10 clones |
| Peças especiais | espelho com moldura (inteiro, porta, partido), corredor de espelhos, sala circular de espelhos |

### Andar 94 — Ecos dos Andares
| | |
|---|---|
| Tamanho / Nível | 300×300 m · nível 94 |
| Bioma | **Pedaços distorcidos de todas as regiões** a flutuar no vazio: um bocado de floresta, uma gruta de cristal, um pântano, uma duna, gelo, mar, lava, um cemitério, nuvens — ligados por pontes de luz |
| Zonas | **10 Pedaços** (um de cada região) · **Pontes entre Ecos** · **O Centro** |
| Mecânica especial | Cada pedaço tem a **mecânica da sua região** em versão curta (escuro, calor, frio, água, névoa roxa, cair das nuvens…). **Reutiliza os kits** de todas as regiões |
| Monstros | **Eco** (de todas as regiões), Fragmento de Mundo, Olho do Vazio, Devorador de Estrelas |
| Recursos | Fragmento de Eco, **Gema Prismática** (no Centro), materiais de todas as regiões |
| Guardião | **Eco dos Guardiões** |
| Segredo | Em cada pedaço há um objeto de um NPC dessa região (a boneca da Elise, a picareta da Hilda, a concha da Lirael…): juntá-los todos dá a decoração **Museu da Subida** para a casa |
| Puzzle | **Ordem da subida**: atravessar os pedaços pela ordem das regiões (1 a 9) abre o Centro |
| Página de lore 94 | *"A torre lembra-se de tudo o que comeu. Lembra-se até de mim a passar por lá."* |
| Desafios | Visitar os 10 pedaços · Vencer um Eco de cada região |
| Peças especiais | (reutiliza os kits de todas as regiões) + pontes de luz, bordas desfeitas dos pedaços |

### Andar 95 — Jardim do Tempo 💀
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 95 |
| Bioma | Um jardim com relógios de sol gigantes, árvores cada uma numa estação diferente, uma ampulheta enorme com areia a cair para cima, engrenagens no chão |
| Zonas | **Relógios de Sol Gigantes** · **Árvores do Tempo** · **Ampulheta Gigante** · **Arena das Engrenagens** (arena do mini-boss) |
| Mecânica especial | **Bolhas de tempo**: zonas lentas (tudo lento) e rápidas (tudo acelera). **Árvores do Tempo**: tocar muda a estação da árvore |
| Monstros | Relógio Vivo, Sombra, Anjo do Vazio |
| Recursos | **Madeira do Tempo**, **Areia do Tempo**, Lótus Estelar |
| Mini-boss | **Guardião do Tempo** (ver `docs/BOSSES.md`) → arma única **Segundo Parado** (adaga) |
| Segredo | Pôr as 4 Árvores do Tempo nas 4 estações diferentes ao mesmo tempo dá a **Flor do Tempo** (R10_06) |
| Página de lore 95 | *"O Guardião do Tempo disse que já me viu passar aqui mil vezes. Que eu volto sempre. Que é sempre a primeira vez para mim."* |
| Desafios | Vencer o Guardião sem ficar Parado · Usar as bolhas rápidas para atravessar em 1 min |
| Peças especiais | relógio de sol gigante, árvore do tempo (4 estações), ampulheta gigante, engrenagem no chão |

### Andar 96 — Planície Invertida
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 96 |
| Bioma | O céu está em baixo e o chão está em cima: montanhas penduradas, um lago no "teto", árvores ao contrário, nuvens a passar por baixo dos pés |
| Zonas | **Chão-Céu** · **Montanhas Penduradas** · **Lago no Teto** · **Ponto de Inversão** |
| Mecânica especial | **Portais de gravidade**: atravessá-los **inverte a gravidade** (passas a andar no "teto"). Cair = cair para cima. A câmara roda suavemente quando inverte |
| Monstros | Sombra, Clone Espelhado, Fragmento de Mundo |
| Recursos | Fragmento Estelar, Fragmento de Sistema, Madeira do Tempo |
| Guardião | **Gigante Invertido** |
| Segredo | No Lago no Teto pesca-se **para cima** (Peixe Invertido) e no fundo do lago há um baú de ouro |
| Puzzle | **Inversões**: chegar a uma plataforma usando 3 portais pela ordem certa |
| Página de lore 96 | *"De pernas para o ar, a torre parece um poço. Talvez eu não esteja a subir. Talvez esteja a cair."* |
| Desafios | Atravessar usando no máximo 4 inversões · Pescar o Peixe Invertido |
| Peças especiais | montanha pendurada, árvore invertida, portal de gravidade, lago no teto |

### Andar 97 — Cidade dos Perdidos
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 97 |
| Bioma | Uma cidade cinzenta e silenciosa de casas iguais com **números** nas portas, uma praça com um relógio sem ponteiros, um mercado de objetos do mundo real |
| Zonas | **Portão dos Perdidos** · **Bairro dos Números** · **Praça do Desistir** · **Mercado das Memórias** |
| Mecânica especial | **Os Perdidos**: Jogadores que desistiram de subir. Podem ser **convencidos a voltar a subir** (missão R10_07) — isto conta para o final |
| Monstros | poucos: Eco e Fragmento de Mundo nos arredores |
| Recursos | Fragmento de Eco, objetos do mundo real (decoração) |
| Povoação | **Cidade dos Perdidos** (secção 7.2) |
| Guardião | **O Desistente** (Jogador nº 7 777) |
| Segredo | Uma casa sem número: lá dentro, o quarto de um Jogador **igualzinho ao teu quarto do mundo real** (cena) |
| Puzzle | **Relógio sem ponteiros**: encontrar os 2 ponteiros (um com o Rafa, outro com a Nina) e pô-lo a andar — a cidade ganha cor |
| Página de lore 97 | *(tinta azul)* *"Construí esta cidade para quem desistiu. Eu também quis desistir. Fiquei com medo de ficar aqui para sempre."* |
| Desafios | Convencer 5 Perdidos · Pôr o relógio a andar |
| Peças especiais | casa com número, relógio sem ponteiros, bancas do mercado das memórias, portão cinzento |

### Andar 98 — Biblioteca do Mundo
| | |
|---|---|
| Tamanho / Nível | 240×240 m com estantes infinitas · nível 98 |
| Bioma | Uma biblioteca sem fim: estantes que sobem e descem para sempre, escadas em espiral, um corredor por cada mundo engolido, livros com luz azul |
| Zonas | **Átrio Infinito** · **Estantes dos Mundos** · **Sala do Diário** · **Catálogo** |
| Mecânica especial | **Escadas em ciclo**: as escadas repetem-se (sobes e voltas ao mesmo sítio) até seguires o caminho das **páginas de lore** que tens. Cada corredor conta a história de um mundo |
| Monstros | Anjo do Vazio, Olho do Vazio, Relógio Vivo |
| Recursos | Núcleo do Vazio, Página Antiga, Fio de Luz Estelar |
| NPCs | **A Arquivista** (secção 7.3) |
| Guardião | **Índice Vivo** |
| Segredo | Um livro na Sala do Diário é uma **porta**: leva à masmorra escondida **O Andar Zero** |
| Puzzle | **Catálogo**: encontrar 3 livros pelo título que a Arquivista diz, usando o catálogo (ordem alfabética e por mundo) |
| Página de lore 98 | *(tinta azul)* *"Escrevi cem páginas. Deixei-as pela torre para o próximo. Para ti. Olá, Jogador nº 10 000."* |
| Desafios | Ler um livro de cada mundo · Encontrar a porta-livro |
| Peças especiais | estante infinita, escada em espiral, livro gigante, mesa do catálogo, porta-livro |

### Andar 99 — Escada Final
| | |
|---|---|
| Tamanho / Nível | 150 m de largura e **400 m de subida** · nível 99 |
| Bioma | Uma escadaria de luz azul que sobe no vazio, com patamares onde estão **estátuas de todos os bosses** que venceste; ao fundo, uma porta pequena |
| Zonas | **Base** · **Patamares das Estátuas** · **Ponto Sem Retorno** · **Porta do Topo** |
| Mecânica especial | **O Sistema fala contigo** a cada patamar (mensagens azuis cada vez mais pessoais). **Ponto Sem Retorno**: último sítio para gravar e voltar à cidade antes do fim |
| Monstros | Anjo do Vazio, Sombra, Clone Espelhado, Devorador de Estrelas |
| Recursos | Fragmento Estelar, Fragmento de Sistema |
| Guardião | **O Guardião da Escada** |
| Segredo | Cada estátua de boss tem uma placa; ler as 20 dá o título *Memória da Torre* |
| Página de lore 99 | *"Daqui a pouco vou ver quem me trouxe. Se fores tu a ler isto, sabe que eu também tive medo."* |
| Desafios | Ler as 20 placas · Subir sem usar poções |
| Peças especiais | degrau de luz azul, patamar com estátua (20 estátuas dos bosses: versões cinzentas dos sprites), porta pequena |

### Andar 100 — Topo da Torre 👑
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 100 |
| Bioma | Surpresa: no topo há um **jardim pequeno e calmo**, igual ao Prado do Despertar do andar 1. Depois, uma sala cheia de **janelas azuis do Sistema** a flutuar, e um trono simples |
| Zonas | **Jardim do Topo** · **Sala do Sistema** · **O Trono do Administrador** (arena) |
| Mecânica especial | Na luta, o **Sistema falha** cada vez mais: a interface desaparece, os números mentem, o chão vira janelas azuis |
| Boss | **O Administrador** (ver `docs/BOSSES.md`) → arma única **Chave do Sistema** (espada) |
| Depois do boss | **A escolha final** e um dos **4 finais** (ver `docs/HISTORIA.md`) |
| Página de lore 100 | *(tinta azul)* *"Chamo-me Aren. Fui o Jogador nº 1. Fiquei no topo mil anos à espera de alguém que quisesse ficar com isto. Ou de alguém que o acabasse."* |
| Desafios | Vencer sem a interface (o Sistema esconde-a) · Vencer sem morrer nenhuma vez em toda a região |
| Peças especiais | jardim do topo (reutiliza o kit da região 1), janelas azuis flutuantes, trono simples |

---

## 6. Guardiões dos andares

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 91 | **Porteiro do Vazio** | figura alta de capuz estrelado (48×48) com uma chave enorme | Golpe de Chave · Abrir Portais (saem inimigos) · **Fechar a Porta**: prende-te numa mini-dimensão 5 s | Luz | **Chave-Espada do Porteiro** (espada): 10% de abrir um portal que faz ×2 de dano |
| 92 | **Baleia Estelar** | baleia feita de constelações (64×64) | Canto Cósmico (Atordoado) · Cometas · Engolir Estrelas (escuridão) | Sombra | **Arpão Cometa** (lança): o ataque carregado lança um cometa |
| 93 | **Rainha dos Espelhos** | figura de vidro com coroa (48×48), aparece em todos os espelhos | **Reflexos**: só a verdadeira tem a coroa a brilhar · Estilhaços · Trocar de lugar contigo | Martelo, Luz | **Adaga Espelho** (adaga): 15% de criar uma cópia tua que ataca 3 s |
| 94 | **Eco dos Guardiões** | muda de forma: é um guardião antigo diferente a cada 20% de vida | Os ataques do guardião em que estiver transformado | Luz | **Lâmina dos Ecos** (katana): cada golpe usa um elemento ao acaso |
| 96 | **Gigante Invertido** | gigante de cabeça para baixo que anda no "céu" (64×64) | Mãos que descem · **Inverter a Gravidade** (passas para o outro lado) · Pedras que caem para cima | Luz | **Martelo da Gravidade** (martelo): o ataque carregado puxa os inimigos à volta para o centro |
| 97 | **O Desistente** | Jogador nº 7 777, armadura velha e muitas armas às costas (48×48) | Troca de arma a cada fase · fala contigo ("Para quê subir?") · no fim pede para parar | — | **Arco do Desistente** (arco): +30% dano quando tens menos de 50% de vida |
| 98 | **Índice Vivo** | livro gigante com olhos e páginas a voar (48×48) | Páginas Cortantes · **Citar**: usa um ataque de um boss antigo lido de uma página · Fechar-se (escudo) | Fogo, Luz | **Cajado do Índice** (cajado): cada 5.º projétil é um feitiço de um boss ao acaso |
| 99 | **O Guardião da Escada** | anjo do vazio enorme com 4 asas e espada estelar (64×64) | Corte Estelar · Chuva de Estrelas · **Animar Estátua**: uma estátua de boss ganha vida 10 s e faz um ataque | Luz | **Espada Grande da Escada Final** (espada grande): +2% de dano por cada boss diferente que já venceste (máx. +40%) |

---

## 7. Povoações

### 7.1 Último Posto (andar 91)
O acampamento final das expedições da Guilda, **abandonado há 60 anos** (a última expedição que chegou tão alto nunca voltou; ninguém subiu tanto desde então, nem a equipa do Gorvan, que caiu no andar 74).
Volta à vida quando chegas: a Guilda manda gente. Tem **cama**, **cristal**, **Forja Estelar** e **loja**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Sargento Bruma** | veterana da Guilda, cabelo grisalho curto | Reativar o posto (R10_01) |
| **Tibério** | o mercador de sempre | Loja |
| **Dorn** | ferreiro itinerante, cego de um olho | **Forja Estelar** (R10_02) e armas míticas (R10_11) |
| **Kai** | se o salvaste no andar 68 | Vive aqui, treina contigo, companheiro |

### 7.2 Cidade dos Perdidos (andar 97)
Cidade dos **Jogadores que desistiram**. Casas iguais com números, ruas silenciosas, um relógio sem ponteiros.
Tem **casa vazia** (dormir), **cristal** e o **Mercado das Memórias** (troca Fragmentos de Eco por materiais de qualquer região
e vende objetos do mundo real como decoração).

| NPC | Quem é | O que faz |
|---|---|---|
| **"Mãe Dois"** (nº 2 048) | a mais velha, líder da cidade | Missão "Os Perdidos" (R10_07) |
| **Rafa** (nº 5 150) | músico que toca músicas do mundo real | Precisa de uma guitarra nova (Madeira do Tempo + Fio de Luz Estelar) · R10_14 |
| **"Doutor"** (nº 3 001) | cientista que estuda o Sistema | Explica o que cada final faz; pede Fragmentos de Sistema |
| **Nina** (nº 9 000) | jovem que desistiu há pouco tempo | Pode voltar a subir contigo: **companheira** (R10_08) |
| **O Desistente** (nº 7 777) | o guardião, depois de vencido | Ajuda a convencer outros Perdidos |
| **Bia** (nº 6 080), **Velho Ulisses** (nº 4 444), **Lino e Lia** (nº 8 501 e 8 502) | Perdidos | Três dos 5 Perdidos da R10_07 (os outros dois são o Rafa e o Doutor) |
| **Chico das Memórias** (nº 2 999) | vendedor | Mercado das Memórias |
| **Ssark** | **só se** expulsaste os Homens-Lagarto no andar 24 | Cena triste; pode ser convencido a voltar |

### 7.3 A Arquivista (andar 98)
NPC único: uma mulher sem idade, de óculos e roupa de papel, que guarda a Biblioteca do Mundo.
Conta a história de cada mundo engolido e junta as **100 páginas do diário** (R10_10).

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R10_01 | Reativar o Último Posto | Sargento Bruma | Acender as 5 âncoras de luz do andar 91 | Posto ativo (cama, cristal, loja) |
| R10_02 | A Forja Estelar | Dorn | 10 Fragmento Estelar + 3 Núcleo do Vazio | **Forja Estelar** (tier 10) |
| R10_03 | Constelações do Mar | (andar 92) | Ligar 5 constelações | Caminho para o Planeta Pequeno · baú de ouro |
| R10_04 | O Espelho Partido | (andar 93) | Juntar os 7 estilhaços | **Espelho Mágico** para a casa (mostra o teu reflexo do mundo real) |
| R10_05 | Ecos de Casa | Velho Fausto | Trazer 10 Fragmentos de Eco, um de cada região | O Fausto escreve **"A Crónica da Subida"** (livro na casa que conta a tua aventura) · ❤️❤️ |
| R10_06 | O Tempo Perdido | (andar 95) | Pôr as 4 Árvores do Tempo nas 4 estações ao mesmo tempo | **Flor do Tempo** (imune a Parado) |
| R10_07 | **Os Perdidos** (história, várias partes) | "Mãe Dois" | Convencer 5 Perdidos a voltar a subir (ajudar cada um com o seu problema) | **Conta para os finais** · título *Esperança dos Perdidos* |
| R10_08 | A Nina | Nina | Levá-la até à Escada Final sem ela desistir (falar com ela nos patamares) | **Nina** como companheira · ❤️ |
| R10_09 | O Desistente | (andar 97) | Vencer o Desistente e ouvir a história dele até ao fim | Arco do Desistente · ele ajuda na R10_07 |
| R10_10 | O Diário de A. | A Arquivista | Ter **90 ou mais** páginas de lore | A Arquivista junta o diário: cena antes do topo e o nome **Aren** |
| R10_11 | Armas Míticas (12 partes) | Dorn + Brom | Fazer as 12 armas míticas (ver `docs/ARMAS.md`) | 12 armas míticas · título *Lenda Forjada* |
| R10_12 | O Nome Raspado | (encontrar o Jogador Sem Número) | Ouvi-lo até ao fim da luta | Máscara Sem Número · lore secreta |
| R10_13 | O Devorador Ancestral | Capitã Freya (rank SS) | Vencer o Devorador Ancestral | Coração Estelar · 15 000 ouro |
| R10_14 | A Última Música | Rafa | Tocar com ele na praça (minijogo de ritmo) | Música **"Casa"** para o gira-discos da casa |
| R10_15 | A Mini-Estrela | Zed | Encontrar a estrela bebé no Planeta Pequeno (andar 92) | **Mini-Estrela** (animal de estimação) |

---

## 9. Masmorra escondida — O Andar Zero (pela Biblioteca, andar 98)

| | |
|---|---|
| Entrada | Um livro da Sala do Diário que é uma porta |
| Sala 1 | **Sala de Código**: paredes cheias de "código" azul do Sistema; encontrar e **corrigir 3 erros** (símbolos fora do sítio) |
| Sala 2 | **Sala dos Jogadores**: estátuas pequenas de todos os 10 000 Jogadores, com os números; a tua está lá, ainda sem cara |
| Sala 3 | **O Núcleo**: uma esfera azul que pulsa |
| Boss extra | **O Primeiro Erro** (64×64): um *bug* do Sistema; muda de forma para outros bosses durante 1 frame, teletransporta-se, os ataques vêm de sítios errados |
| Recompensa | **Katana do Erro** (arma secreta, katana): cada golpe tem 1% de fazer **9 999** de dano · baú de ouro · página de lore extra "O Andar Zero" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Peixe-Cometa | Mar de Estrelas (92) | sempre | incomum | 2 000 |
| Peixe-Espelho | poça de espelho (93) | sempre | incomum | 2 200 |
| Carpa do Tempo | ampulheta do 95 (nada para trás) | sempre | raro | 3 500 |
| Peixe Invertido | Lago no Teto (96) — **pesca-se para cima** | sempre | raro | 3 800 |
| Peixe-Memória | fonte da Cidade dos Perdidos (97) | noite | raro | 4 000 |
| **O Peixe do Princípio** (lendário) | lago do Jardim do Topo (100) | só depois de um final | lendário | 50 000 |

### Plantas
| Planta | Semente vem de | Dias | Estação | Usos |
|---|---|---|---|---|
| Lótus Estelar | andar 92 (precisa do lago da quinta) | 10 | todas | Elixir Estelar |
| Flor do Tempo | missão R10_06 | 4 (muda de estação sozinha) | todas | presentes, poções de tempo |
| Semente do Mundo | Mercado das Memórias | 7 | todas | dá uma colheita **ao acaso** de qualquer região |
| Árvore Estelar | Dorn | 28 (árvore) | todas | dá 1 Fragmento Estelar por semana |

### Animais
- **Mini-Estrela** (animal de estimação): missão R10_15. **+5% a tudo** (ATQ, DEF, velocidade, drops, XP) e ilumina à tua volta.

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Grande Falha | 10% ao entrar num andar | Muitas falhas do Sistema ao mesmo tempo; mais Fragmentos de Sistema |
| Chuva de Meteoros | 1 vez por semana | Meteoros caem (perigo) e deixam Fragmentos Estelares |
| Eclipse Total | raro | Só há luz das âncoras: os Devoradores ficam mais fortes |
| Silêncio do Sistema | raro | A janela azul (interface) **desaparece durante 1 minuto** |
| Visita dos Ecos | 1 por dia | Um Eco de um **boss antigo** aparece num andar ao acaso (drop raro) |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (≈ 25): ilha de pedra do vazio ×3, caminho de estrelas, chão de vidro, chão de luz azul, espelho, estante, relógio de sol,
  âncora de luz, fragmento estelar (minério), madeira do tempo (cortável), lótus, baú, cristal, ponte de luz, portal de gravidade, janela azul do Sistema
- [ ] **Peças especiais dos andares** (≈ 40) — o andar 94 **reutiliza os kits de todas as regiões** e o 100 reutiliza o kit da região 1
- [ ] **8 monstros**: Sombra, Olho do Vazio, Devorador de Estrelas, Relógio Vivo, Anjo do Vazio, Fragmento de Mundo
  (o **Clone Espelhado** e o **Eco** usam sprites que já existem com um shader)
- [ ] **2 monstros com nome**: Devorador Ancestral, O Jogador Sem Número
- [ ] **8 guardiões** (o Eco dos Guardiões reutiliza os sprites dos guardiões antigos)
- [ ] **Mini-boss** Guardião do Tempo e **boss** O Administrador
- [ ] **Boss da masmorra** O Primeiro Erro
- [ ] **Armas**: 12 Estelares + 2 únicas + 8 de guardião + 1 secreta + **12 míticas** = **35 armas** (+ ícones)
- [ ] **Ícones de materiais** (≈ 22), **peixes** (6), **plantas** (4 × 4 fases)
- [ ] **NPCs**: Bruma, Dorn, "Mãe Dois", Rafa, "Doutor", Nina, O Desistente, Bia, Ulisses, Lino e Lia, Chico, A Arquivista, Perdidos genéricos (3 bases), Aren (o Administrador sem máscara) (+ retratos)
- [ ] **Animal**: Mini-Estrela
- [ ] **Conjunto de armadura** Estelar (5 ícones)
- [ ] **20 estátuas** dos bosses (versões cinzentas dos sprites, para o andar 99)
