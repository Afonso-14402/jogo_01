# Região 1 — Floresta (andares 1–10)

> Como ler este ficheiro: a **identidade** diz como a região se parece e soa; depois vêm os
> **materiais**, os **monstros**, os **10 andares** (cada um com o seu guardião), as **povoações**,
> as **missões**, a **masmorra escondida**, os **peixes e plantas** e, no fim, a **lista de arte**.
> Os números de vida e dano vêm das fórmulas de `docs/SISTEMAS.md`. Os bosses grandes
> (Javali-Rei e Ent Ancião) estão em `docs/BOSSES.md`.

---

## 1. Identidade

| | |
|---|---|
| Tema | Uma floresta mágica, verde e luminosa: o primeiro mundo que a torre engoliu |
| Sensação | Calma, descoberta, aventura a começar |
| Material das armas | **Cobre** (tier 1) |
| Monstros fracos a | **Fogo** |
| Cores principais | verdes `#239063` `#1ebc73` `#91db69`, castanhos `#9e4539` `#cd683d`, céu `#8fd3ff` |
| Luz | sol quente a passar pelas folhas (raios de luz), noites azuis com vaga-lumes |
| Clima | Sol 50% · Chuva 30% · Nevoeiro 20% |
| Música | `floresta_dia`, `floresta_noite`, `floresta_perigo` (combate), `javali_rei`, `ent_anciao` |
| Níveis | monstros 1–11; guardiões 2–10; mini-boss 7; boss 13 |
| Animal de estimação | Slime Bebé, Raposa da Floresta |

---

## 2. Materiais e recursos

| Recurso | Onde | Como | Usos |
|---|---|---|---|
| Minério de Cobre | rochas com veios laranja (andares 1, 3, 5, 8) | Picareta | Lingote de Cobre (3 minérios + 1 Carvalho, na forja) |
| Madeira de Carvalho | árvores largas (todos os andares) | Machado | cabos, arcos, cajados, móveis, combustível da forja |
| Seiva Cristalizada | árvores antigas do andar 7 e 10 (raro) | Machado | **cristal** da região (melhorias +6 a +10, cajados) |
| Couro de Javali | Javali | drop | manoplas, armaduras de couro |
| Linho Bravo | plantas altas (andares 1, 2, 6) | à mão | **fio** da região (arcos, roupa) |
| Erva Verde | em todo o lado | à mão | Poção de Vida |
| Flor de Mel | andar 6 | à mão | doces, Poção de Estamina |
| Cogumelo Luminoso | andares 2, 4 (brilha à noite) | à mão | Poção de MP, cozinha |
| Mel Azul | colmeias do andar 6 | à mão (as abelhas atacam) | cozinha, presentes |
| Pó de Fada | Fada Travessa | drop | encantamentos fracos, Poção de Velocidade |
| Bolota Dourada | Treant Jovem (raro) | drop | semente da Árvore Dourada (quinta) |
| Rubi pequeno | minério de cobre (1%) | Picareta | gema de Fogo (fraca) |

---

## 3. Monstros

### 3.1 Slime Verde
| | |
|---|---|
| Tamanho | 32×32 (o corpo ocupa ~18×14) |
| Tipo | **Fraco**, grupos de 3–5 |
| Andares | 1, 2, 3, 4 |
| Comportamento | Salta na tua direção a cada 1,2 s quando estás a menos de 6 m. Não persegue mais de 12 m |
| Ataques | **Salto** (×1,0; aviso 0,4 s: encolhe-se) |
| Fraco / Resiste | Fogo / Veneno |
| Drops | Gel de Slime 70% (1–2) · Erva Verde 15% |
| Elite | **Slime Esmeralda**: ao morrer divide-se em 2 slimes pequenos |
| Animações | parado (4), mover (4: esmagar e esticar), atacar (4), dano (1), morrer (4: derrete) |

### 3.2 Coelho-Chifre
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, sozinho ou aos pares, **cobarde** (foge com pouca vida) |
| Andares | 1, 2, 3, 6 |
| Comportamento | Pasta; quando te vê fica a olhar 1 s e depois ataca ou foge (50/50) |
| Ataques | **Chifrada**: investida de 4 m (×1,2; aviso 0,5 s: baixa a cabeça e raspa o chão) |
| Fraco / Resiste | Fogo / — |
| Drops | Chifre Pequeno 50% · Carne de Coelho 40% · Pelo Macio 20% |
| Elite | **Coelho Lunar** (branco, só à noite): investida dupla |
| Animações | parado (4: orelhas mexem), mover (4: aos saltos), atacar (4), dano (1), morrer (4) |

### 3.3 Lobo Cinzento
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Rápido**, alcateia de 2–4 (um é o líder, maior) |
| Andares | 2, 3, 5, 7, 9 (o dobro à noite) |
| Comportamento | Rodeiam-te; atacam um de cada vez; o líder uiva quando um lobo morre |
| Ataques | **Mordida** (×1,0; aviso 0,35 s) · **Investida** de 6 m (×1,4; aviso 0,6 s: agacha-se) · **Uivo** (só o líder: chama lobos a 20 m; aviso 1 s) |
| Fraco / Resiste | Fogo / — |
| Drops | Pele de Lobo 60% · Presa de Lobo 25% · Carne 30% |
| Elite | **Lobo de Sombra**: fica invisível 2 s antes de atacar |
| Animações | parado (4), mover (6), atacar (4), uivar (4), dano (1), morrer (4) |

### 3.4 Javali
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 3, 5, 6 |
| Comportamento | Ignora-te até chegares a 5 m ou o atacares. Depois carrega em linha reta |
| Ataques | **Carga** de 8 m (×1,6; empurra muito; aviso 0,8 s: raspa a pata e bufa). **Se bater numa árvore ou rocha fica atordoado 2 s.** · **Cabeçada** (×1,1; aviso 0,4 s) |
| Fraco / Resiste | Fogo / Físico de frente (−20%) |
| Drops | Couro de Javali 60% · Presa de Javali 30% · Carne de Javali 50% |
| Elite | **Javali Ferro-Pelo**: carga tripla seguida |
| Animações | parado (4), mover (4), carga (4), cabeçada (4), atordoado (2), dano (1), morrer (4) |

### 3.5 Cogumelo Andante
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Normal**, grupos de 2–3 |
| Andares | 2, 4, 9 |
| Comportamento | Finge ser um cogumelo normal (parado no chão). Acorda quando passas a 3 m |
| Ataques | **Bofetada** (×1,0; aviso 0,4 s) · **Nuvem de Esporos**: área de 2 m que **envenena** e dura 4 s (aviso 0,6 s: incha) |
| Fraco / Imune | Fogo / Veneno |
| Drops | Esporo 60% · Cogumelo Luminoso 30% · Chapéu de Cogumelo 15% |
| Elite | **Cogumelo Real** (vermelho): a nuvem também causa Lentidão |
| Animações | disfarce (1), acordar (4), parado (4), mover (4), atacar (4), esporos (4), dano (1), morrer (4) |

### 3.6 Fada Travessa
| | |
|---|---|
| Tamanho | 32×32 (a fada tem ~12 px, com brilho à volta) |
| Tipo | **Voador + Mago**, sozinha |
| Andares | 4, 6, 7, 9 |
| Comportamento | Fica a 6 m, teletransporta-se 3 m quando chegas perto, ri-se |
| Ataques | **Faísca**: projétil lento mágico (×1,0; aviso 0,4 s) · **Pó Brilhante**: Cegueira 2 s (aviso 0,6 s) · **Roubo**: rouba 1 consumível da barra rápida e foge (aviso 0,3 s) — mata-a para o recuperar |
| Fraco / Resiste | Fogo / Luz |
| Drops | Pó de Fada 50% · Asa de Fada 20% · o item roubado |
| Elite | **Fada Rainha Pequena**: chama 2 fadas |
| Animações | parado (4: a voar), mover (4), atacar (4), roubar (4), teletransporte (4), dano (1), morrer (4) |

### 3.7 Abelha-Gigante
| | |
|---|---|
| Tamanho | 32×32 |
| Tipo | **Voador**, enxame de 3–5 |
| Andares | 6, 8 |
| Comportamento | Só ataca se te aproximares das colmeias ou atacares uma abelha; então ataca o enxame todo |
| Ataques | **Ferrão** (×1,0; 30% Veneno; aviso 0,4 s) · **Mergulho** em linha (×1,3; aviso 0,6 s) |
| Fraco / Resiste | Fogo / Veneno |
| Drops | Mel 40% · Ferrão 30% · Cera 25% |
| Elite | **Abelha Soldado**: maior, carapaça (DEF ×2) |
| Animações | parado (2: asas), mover (4), atacar (4), dano (1), morrer (4) |

### 3.8 Treant Jovem
| | |
|---|---|
| Tamanho | 48×48 |
| Tipo | **Tanque** |
| Andares | 7, 8, 10 |
| Comportamento | **Disfarçado de árvore**: só acorda quando chegas a 3 m ou lhe bates com o machado (susto!) |
| Ataques | **Galhada**: área à frente de 3 m (×1,3; aviso 0,7 s) · **Raízes**: linha de raízes no chão que causa Lentidão (×0,8; aviso 0,8 s: marca no chão) · **Bolotas**: 3 projéteis em leque (×0,7; aviso 0,5 s) |
| Fraco / Resiste | Fogo (a queimadura dura o dobro) / Água, Físico (−10%) |
| Drops | Madeira Viva 50% · Seiva 40% · Bolota Dourada 10% |
| Elite | **Treant de Musgo**: cura-se 2% por segundo se estiver em cima de musgo |
| Animações | disfarce (1), acordar (6), parado (4), mover (4), galhada (5), raízes (4), bolotas (4), dano (1), morrer (6) |

---

## 4. Monstros com nome

| Nome | Onde e quando | Aspeto | Luta | Drops |
|---|---|---|---|---|
| **Slime Rei** | andares 1–4, 3% ao entrar no andar, numa clareira | slime 64×64 com coroa de ouro e um peixe lá dentro | Saltos que fazem ondas de choque; aos 50% divide-se em 4 slimes médios | Coroa de Gel (acessório: +5% HP) · Gel Real (material raro) · 100% Slime Bebé (ovo) na 1.ª vez |
| **Lobo Cicatriz** | andares 2, 7, 9, só à noite, 5% (lua cheia 20%) | lobo preto 48×48 com cicatriz branca no olho | Chama alcateia; investida tripla; uivo dá-lhes +20% ATQ | Manto Cicatriz (capa: +5% velocidade à noite) · Presa Negra |

Quando aparecem: `[Sistema] Um monstro com nome apareceu neste andar: Slime Rei.`

---

## 5. Os andares

### Andar 1 — Prado do Despertar
| | |
|---|---|
| Tamanho / Nível | 150×150 m · nível 1 |
| Bioma | Prado de erva alta a ondular ao vento, flores brancas, colinas suaves, céu muito azul. Pedras antigas em círculo no cimo de uma colina |
| Zonas | **Colina do Despertar** (onde acordas no prólogo) · **Campo de Erva Alta** · **Moinho Abandonado** · **Círculo de Pedras** (escada para o andar 2) |
| Mecânica especial | **Erva alta**: esconde monstros e itens. Cortar erva com a arma dá às vezes Erva Verde, sementes ou ouro |
| Monstros | Slime Verde, Coelho-Chifre (e um Lobo Cinzento só na cena do prólogo) |
| Recursos | Erva Verde (muita), Linho Bravo, Carvalho (poucos), Minério de Cobre (3 rochas) |
| NPCs | **Kai** (prólogo) · **Tibério** na Zona Segura (depois do prólogo) |
| Guardião | **Coelho-Chifre Ancião** (ver tabela da secção 6) |
| Segredo | Dentro do moinho: puxar a corda faz rodar as pás e abre um alçapão com um **baú de prata** |
| Puzzle | Tutorial: empurrar uma pedra para tapar um buraco e passar |
| Página de lore 1 | *"Dia 1. Acordei num prado. Uma janela azul diz que sou o Jogador nº 1. Não há mais ninguém."* |
| Desafios | Matar 10 slimes sem levar dano · Cortar 100 tufos de erva |
| Peças especiais | moinho com pás que rodam, círculo de pedras, erva alta (com vento) |

### Andar 2 — Bosque dos Sussurros
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 2 |
| Bioma | Floresta densa, troncos escuros, pouca luz; raios de sol aqui e ali; à noite cheio de vaga-lumes |
| Zonas | **Trilho dos Lenhadores** · **Acampamento dos Lenhadores** (povoação) · **Bosque Escuro** · **Clareira dos Sussurros** |
| Mecânica especial | **Árvores que sussurram**: perto de certas árvores ouve-se uma frase. São **dicas de segredos** (deste e de outros andares). **Bosque Escuro**: apanhar vaga-lumes num frasco dá luz durante 3 minutos |
| Monstros | Lobo Cinzento, Cogumelo Andante, Coelho-Chifre, Slime Verde |
| Recursos | Carvalho (muito), Erva Verde, Cogumelo Luminoso, Linho Bravo |
| Povoação | **Acampamento dos Lenhadores** (secção 7.1) |
| Guardião | **Coruja Sombria** |
| Segredo | Uma árvore oca no Bosque Escuro tem o **Anel do Sussurro** (+3% hipótese de encontrar segredos) |
| Puzzle | **Os 3 Sussurros**: três árvores dizem uma ordem; tocar em 3 pedras nessa ordem abre um baú de prata |
| Página de lore 2 | *"Os lobos aqui não são normais. Os olhos brilham quando a janela azul aparece."* |
| Desafios | Atravessar o Bosque Escuro sem frasco de luz · Matar uma alcateia inteira em 20 s |
| Peças especiais | árvore oca, árvore com cara (sussurrante), tendas e serração do acampamento |

### Andar 3 — Ribeiro Cristalino
| | |
|---|---|
| Tamanho / Nível | 220×180 m · nível 3 |
| Bioma | Rio de água transparente com pedras, pontes de madeira, cascatas, salpicos de luz. Libélulas |
| Zonas | **Margem Norte** · **Pontes de Madeira** · **Cascata Alta** · **Bacia Funda** · **Ilhota** |
| Mecânica especial | **Água**: a rasa deixa andar devagar; a funda leva-te rio abaixo (volta-se a subir pela margem). **Pesca** abre aqui |
| Monstros | Slime Verde, Lobo Cinzento, Javali, Coelho-Chifre |
| Recursos | Minério de Cobre (muito, junto à cascata), Juncos, Erva Verde, pedras de rio |
| NPCs | **Pip** (primeira vez que o encontras; ensina a pescar) |
| Guardião | **Lagostim Couraçado** |
| Segredo | Gruta atrás da Cascata Alta com **baú de ouro** (a chave está num ninho na Ilhota) |
| Puzzle | **Comportas**: rodar 3 rodas de madeira pela ordem certa baixa a água e abre o caminho para a Ilhota |
| Página de lore 3 | *"Bebi do ribeiro. A água sabe a metal… como se a torre tivesse sido construída por cima de outro mundo."* |
| Desafios | Pescar 3 peixes diferentes · Atravessar o rio sem tocar na água funda |
| Peças especiais | cascata (com shader de água), comportas com rodas, pontes de tábuas, rochas de rio |

### Andar 4 — Clareira dos Cogumelos
| | |
|---|---|
| Tamanho / Nível | 200×200 m · nível 4 |
| Bioma | Cogumelos gigantes (até 10 m) de chapéu vermelho, azul e roxo; à noite tudo brilha; esporos a flutuar |
| Zonas | **Anel de Fadas** · **Bosque Gigante** (sobe-se pelos cogumelos) · **Pântano de Esporos** · **Cogumelo Oco** |
| Mecânica especial | **Cogumelos-trampolim**: saltam-te para cima de outros cogumelos. **Pântano de Esporos**: envenena enquanto lá estás (Antídoto ou Máscara de Linho). **Anel de Fadas**: entrar à meia-noite leva-te à **Clareira Secreta das Fadas** (loja de fadas) |
| Monstros | Cogumelo Andante, Fada Travessa, Slime Verde |
| Recursos | Cogumelo Luminoso (muito), Esporo, Erva Verde, Carvalho |
| Guardião | **Rainha dos Esporos** |
| Segredo | O Cogumelo Oco tem uma sala com **Livro de Receitas: Sopas** |
| Puzzle | **Luzes dos cogumelos**: acender 5 cogumelos-lanterna (bater-lhes) na ordem das cores do arco-íris |
| Página de lore 4 | *"Os cogumelos falam entre si com luz. Acho que me estão a seguir."* |
| Desafios | Chegar ao cimo do cogumelo mais alto · Derrotar o guardião sem usar Antídotos |
| Peças especiais | cogumelos gigantes (3 tipos), cogumelo-trampolim, anel de cogumelos pequenos, cogumelo oco |

### Andar 5 — Toca do Javali-Rei 💀
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 5 |
| Bioma | Colinas de terra revolvida, buracos de tocas, lama, um pomar selvagem com maçãs vermelhas |
| Zonas | **Colinas das Tocas** · **Lamaçal** · **Pomar Selvagem** · **Grande Toca** (arena do mini-boss) |
| Mecânica especial | **Lama**: Lentidão enquanto andas nela. **Maçãs**: atirar uma maçã faz os javalis irem comê-la (distrai 5 s) |
| Monstros | Javali (muitos), Lobo Cinzento, Coelho-Chifre |
| Recursos | Minério de Cobre, Maçã Selvagem, Carvalho |
| Mini-boss | **Javali-Rei** (ver `docs/BOSSES.md`) → arma única **Presa do Javali-Rei** (machado) |
| Segredo | Uma toca pequena só se atravessa a rastejar depois de beber a **Poção de Encolher** (Selene) — tem um **Ovo de Ouro do Javali** (comida especial para animais: +50 de felicidade) |
| Página de lore 5 | *"Venci um javali do tamanho de uma carroça. A janela deu-me 'XP'. Isto é um jogo? Quem o joga?"* |
| Desafios | Fazer 5 javalis baterem em árvores · Vencer o Javali-Rei sem usar poções |
| Peças especiais | tocas (entrada de buraco), árvores de fruto, lamaçal, cerca de troncos da arena |

### Andar 6 — Colinas Floridas
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 6 |
| Bioma | Colinas cobertas de flores que **mudam de cor com a estação**; colmeias gigantes de cera dourada; rio de mel |
| Zonas | **Campos de Flores** · **Colmeias Gigantes** · **Jardim das Estátuas** · **Rio de Mel** |
| Mecânica especial | **Flores de pólen**: passar por elas dá bónus de 30 s (vermelha +10% ATQ, azul +MP, amarela +velocidade). **Rio de mel**: prende (Lentidão forte) |
| Monstros | Abelha-Gigante, Coelho-Chifre, Fada Travessa, Javali |
| Recursos | Flor de Mel, Mel Azul (colmeias), Linho Bravo, Cera |
| Guardião | **Abelha-Rainha Melífera** |
| Segredo | No Jardim das Estátuas, uma estátua tem um vaso vazio: pôr uma **Flor de Mel** abre uma passagem com **baú de ouro** |
| Puzzle | **Colmeia labirinto**: dentro da maior colmeia, empurrar favos para abrir caminho até ao Mel Real |
| Página de lore 6 | *"Encontrei colmeias com abelhas que fazem mel azul. Guardei um pouco. Lembra-me casa."* |
| Desafios | Apanhar 10 Mel Azul sem ser picado · Usar os 3 bónus de flores ao mesmo tempo |
| Peças especiais | colmeias gigantes, favos, estátuas de jardim, flores grandes (3 cores) |

### Andar 7 — Floresta Antiga
| | |
|---|---|
| Tamanho / Nível | 260×260 m · nível 7 |
| Bioma | Árvores gigantes (troncos de 20 m de largura), raízes como pontes, musgo, luz verde e dourada lá do alto |
| Zonas | **Raízes Gigantes** · **Folhalta** (aldeia élfica nas árvores) · **Poço da Lua** · **Raiz Oca** (entrada da masmorra escondida) |
| Mecânica especial | **Caminhos em altura**: pontes de raízes e plataformas; cair leva-te ao chão da floresta (mais monstros). Elevadores de cesto dos elfos |
| Monstros | Treant Jovem, Lobo Cinzento, Fada Travessa, Cogumelo Andante |
| Recursos | Carvalho, **Seiva Cristalizada**, Madeira Viva, Cogumelo Luminoso |
| Povoação | **Folhalta** (secção 7.2) |
| Guardião | **Guardião de Musgo** |
| Segredo | O Poço da Lua, numa noite de lua cheia, mostra o caminho para a **Raiz Oca** |
| Puzzle | **4 Cristais de Seiva** a pôr nos 4 altares à volta da Raiz Oca abrem a masmorra |
| Página de lore 7 | *"Elfos! Dizem que a floresta deles 'caiu do céu' há uma semana. A torre engole mundos."* |
| Desafios | Atravessar o andar sem tocar no chão · Encontrar os 4 Cristais de Seiva |
| Peças especiais | tronco gigante, raiz-ponte, casas nas árvores, elevador de cesto, poço com luz |

### Andar 8 — Ruínas Cobertas de Musgo
| | |
|---|---|
| Tamanho / Nível | 220×220 m · nível 8 |
| Bioma | Restos de uma aldeia de pedra antiga, colunas partidas, hera, estátuas de cavaleiros. Símbolos azuis do Sistema gravados nas paredes |
| Zonas | **Portão Partido** · **Praça das Estátuas** · **Templo Enterrado** · **Torre de Vigia** |
| Mecânica especial | **Estátuas que andam quando não olhas**: na Praça, as estátuas aproximam-se quando a câmara não as vê (puzzle e susto) |
| Monstros | Treant Jovem, Lobo Cinzento, Abelha-Gigante, Slime Verde |
| Recursos | Minério de Cobre, pedra trabalhada, Carvalho, Hera |
| Guardião | **Cavaleiro de Pedra Musgosa** |
| Segredo | No cimo da Torre de Vigia vê-se, de dia, um **brilho** num telhado: lá está a **Chave das Ruínas** (baú de ouro do Templo) |
| Puzzle | **Estátuas**: levar as 4 estátuas até aos 4 pedestais olhando para elas só quando chegam (andam quando não olhas) |
| Página de lore 8 | *"As ruínas têm o mesmo símbolo que a janela azul. Alguém já esteve aqui antes de mim?"* |
| Desafios | Resolver o puzzle das estátuas em menos de 2 min · Derrotar o guardião só com ataques carregados |
| Peças especiais | colunas partidas, estátua de cavaleiro, portão em ruínas, torre de vigia, pedras com símbolos |

### Andar 9 — Lago da Névoa
| | |
|---|---|
| Tamanho / Nível | 240×240 m · nível 9 |
| Bioma | Grande lago calmo com nevoeiro branco, juncos, ilhas pequenas com salgueiros, um cais velho. À noite, fogos-fátuos azuis |
| Zonas | **Margem dos Juncos** · **Ilhas dos Salgueiros** · **Cais Velho** · **Ilha Central** (templo pequeno) |
| Mecânica especial | **Nevoeiro**: visão 6 m. **Barco a remos** no Cais Velho para ir entre ilhas. **Troncos que afundam** se ficares parado 2 s. À noite os **fogos-fátuos** levam a segredos |
| Monstros | Lobo Cinzento (noite), Fada Travessa, Cogumelo Andante, Slime Verde |
| Recursos | Juncos, Erva Verde, Salgueiro (madeira), peixes |
| Guardião | **Serpente da Névoa** |
| Segredo | Seguir os fogos-fátuos às 3:00 leva a uma ilha que só aparece de noite com o **Altar do Reflexo** (página de lore extra e Amuleto da Névoa) |
| Puzzle | **Sinos do lago**: tocar 3 sinos de barco em 3 ilhas no mesmo minuto (é preciso remar depressa) abre o templo |
| Página de lore 9 | *"Vi no lago o reflexo de uma cidade que não existe. Ou que ainda não existe."* |
| Desafios | Pescar o Rei do Lago Nevoento · Visitar todas as ilhas em 5 min |
| Peças especiais | barco a remos, cais de madeira, salgueiro, sinos de barco, templo pequeno de pedra branca |

### Andar 10 — Coração da Floresta 👑
| | |
|---|---|
| Tamanho / Nível | 180×180 m · nível 10 |
| Bioma | Bosque sagrado com lanternas de pedra, árvores brancas, folhas douradas a cair, e ao centro a **Árvore-Mãe**, gigante e meio morta |
| Zonas | **Caminho das Lanternas** · **Bosque Sagrado** · **Raízes da Árvore-Mãe** (arena do boss) |
| Mecânica especial | **Lanternas**: acender as 8 lanternas do caminho (fogo) dá 10% de dano extra contra o boss |
| Monstros | Treant Jovem, Lobo Cinzento, Fada Travessa |
| Recursos | Seiva Cristalizada, Madeira Viva, Folha Dourada |
| Boss | **Ent Ancião** (ver `docs/BOSSES.md`) → arma única **Raiz Ancestral** (cajado) |
| Depois do boss | Cena: a Árvore-Mãe fala contigo antes de morrer. Ao voltar à cidade há o **Dia da Subida** (festa) |
| Página de lore 10 | *"A árvore-mãe morreu nos meus braços. Disse-me: 'Não sejas como o anterior.' O anterior… quem?"* |
| Desafios | Acender todas as lanternas antes do boss · Vencer o boss em menos de 3 min |
| Peças especiais | Árvore-Mãe (peça enorme), lanternas de pedra, árvores brancas, altar de raízes |

---

## 6. Guardiões dos andares

Cada guardião guarda a escada para o andar seguinte. Tamanho 48×48 (ou 64×64), nível do andar +1,
HP ×6 (ver `SISTEMAS.md`). A **arma de guardião** cai com 30% de hipótese (100% na 1.ª vitória se fizeres o desafio do guardião).

| Andar | Guardião | Aspeto | Ataques | Fraco a | Arma de guardião |
|---|---|---|---|---|---|
| 1 | **Coelho-Chifre Ancião** | coelho cinzento enorme (48×48) com um chifre partido e cicatrizes | Salto Esmagador (salta e cai: área 3 m) · Chifrada tripla · Bater o pé (chama 3 coelhos) | Fogo | **Chifre Partido** (adaga): +10% velocidade de movimento |
| 2 | **Coruja Sombria** | coruja negra com olhos amarelos (48×48), voa | Mergulho · Pio Estridente (Cegueira 3 s, área) · Chuva de Penas (5 projéteis) | Fogo, Raio | **Pena-Noturna** (arco): +30% dano em inimigos que ainda não te viram |
| 3 | **Lagostim Couraçado** | lagostim azul-escuro com pinças grandes (48×48) | Pinçada dupla · Jato de Água (Encharcado, linha 8 m) · Carapaça (fecha-se: DEF ×3 durante 4 s) | Raio | **Martelo Pinça** (martelo): +30% dano a inimigos do tipo Tanque |
| 4 | **Rainha dos Esporos** | cogumelo gigante com "vestido" de lamelas e coroa de esporos (64×64) | Nuvem Real (veneno + lentidão, área 5 m) · Chamar 4 Cogumelos · Pulo Esmagador | Fogo | **Esporo-Luz** (cajado): os projéteis deixam esporos venenosos no chão |
| 6 | **Abelha-Rainha Melífera** | abelha enorme dourada e azul (48×48) com coroa de cera | Ferrão Real (veneno forte) · Chamar Enxame (5 abelhas) · Chuva de Mel (Lentidão em área) | Fogo | **Ferrão-de-Mel** (lança): 15% Veneno; matar um inimigo cura 2% HP |
| 7 | **Guardião de Musgo** | golem de raízes e pedra coberto de musgo (64×64), olhos verdes | Raízes em Linha (Lentidão) · Abraço (agarra 2 s: carregar botões para soltar) · Regenerar (no musgo, 3% HP/s — tira-o do musgo!) | Fogo | **Tronco-Velho** (espada grande): +15% HP máximo enquanto equipada |
| 8 | **Cavaleiro de Pedra Musgosa** | estátua de cavaleiro que ganhou vida (48×48), espada partida | Corte Giratório (área 3 m) · Escudo (bloqueia ataques de frente: ataca pelas costas) · Investida com escudo | Raio | **Lâmina do Cavaleiro Esquecido** (espada): combo de 4 golpes em vez de 3 |
| 9 | **Serpente da Névoa** | serpente branca de água (64×64), sai e entra no lago | Mordida · Névoa (fica invisível 3 s; só se vê a ondulação) · Cuspe de Água (3 jatos) | Raio | **Foice Bruma** (foice): cada golpe tem 10% de te tornar invisível 1 s (os inimigos perdem-te) |

---

## 7. Povoações

### 7.1 Acampamento dos Lenhadores (andar 2)
Pequeno acampamento de gente de Ascendia que vem cortar madeira para a cidade. Tendas, uma serração
a água, pilhas de troncos, uma fogueira grande. Tem **cama** (dormir e gravar) e **cristal de teletransporte**.

| NPC | Quem é | O que faz |
|---|---|---|
| **Bruno Machadão** | chefe dos lenhadores; enorme, barba ruiva, ri alto | Loja: machados de ferramenta, Carvalho, comida simples. Missões de madeira |
| **Tina** | filha do Bruno, 14 anos, sonha ser alquimista | Pede-te para lhe levares livros da Selene; mais tarde vai para a cidade e trabalha na alquimia |
| **Velho Cass** | lenhador reformado que conta histórias | Rumores e lore da floresta; missão das estátuas do andar 8 |
| **Tronco** | cão do acampamento | Se lhe deres carne 5 dias seguidos segue-te até à saída do andar (piada: não pode sair) |

### 7.2 Folhalta, a Aldeia Élfica (andar 7)
Aldeia de **elfos da floresta** que vivem no cimo das árvores gigantes. A floresta deles "caiu do céu"
(a torre engoliu-a). Casas redondas nos ramos, pontes de corda, lanternas de seiva, elevadores de cesto.
Tem **estalagem**, **cristal** e **loja élfica**. É a terra natal da **Selene** (alquimista de Ascendia).

| NPC | Quem é | O que faz |
|---|---|---|
| **Anciã Lothiel** | chefe da aldeia, cabelo branco até aos pés | Sabe que a floresta foi engolida; dá a missão "O Mal das Raízes" |
| **Faelan** | arqueiro élfico, sério, poucas palavras | Treino de arco: +1 nível de Manejo de Arco por treino (até nível 3); vende arcos de madeira |
| **Mira Folha-de-Prata** | comerciante | Sementes raras, Poção Élfica, Linho fino |
| **Eldrin** | irmão mais novo da Selene, alegre | Missão "Cartas para Selene" |
| **Tilly** | criança élfica | Missão "A Raposa Perdida" → animal de estimação **Raposa da Floresta** |

Loja élfica: Arco Curto de Carvalho (tier 1, Incomum), Sementes de Morango Silvestre, Sementes de Árvore Dourada (rara),
Poção Élfica (cura 20% HP e 20% MP), Linho Fino (fio de qualidade).

---

## 8. Missões da região

| ID | Nome | Quem dá | Objetivo | Recompensa |
|---|---|---|---|---|
| R1_01 | Lobos à Noite | Bruno (andar 2) | Matar 8 Lobos Cinzentos à noite no andar 2 | 200 ouro · Machado de Cobre (qualidade Boa) |
| R1_02 | Madeira para a Ponte | Bruno | Entregar 40 Carvalho | 150 ouro · abre o projeto **Ponte do Rio** em Ascendia |
| R1_03 | Aprende a Pescar | Pip (andar 3) | Pescar 3 peixes no andar 3 | Cana de Bambu · receita Truta Grelhada |
| R1_04 | O Anel de Fadas | Fada Lumi (Clareira Secreta, andar 4) | Encontrar 5 Pós de Fada Dourados escondidos no andar 4 | A loja das fadas fica sempre aberta · Asas de Fada (cosmético) |
| R1_05 | Mel Azul | Dona Marta (Ascendia) | Trazer 5 Mel Azul do andar 6 | Receita Panquecas de Mel Azul · ❤️ Dona Marta |
| R1_06 | A Raposa Perdida | Tilly (Folhalta) | Seguir as pegadas no andar 7 e trazer a raposa | **Raposa da Floresta** (animal de estimação) |
| R1_07 | Cartas para Selene | Eldrin (Folhalta) | Levar a carta à Selene e trazer a resposta | Receita Poção Élfica · ❤️ Selene |
| R1_08 | O Mal das Raízes | Anciã Lothiel | Investigar a Raiz Oca e limpar a masmorra | **Arco Raiz-Viva** (arma secreta) · 800 ouro |
| R1_09 | As Estátuas que Andam | Velho Cass (andar 2) | Resolver o puzzle das estátuas do andar 8 | Anel do Vigia (+10% visão no nevoeiro e no escuro) |
| R1_10 | O Rei do Lago | Pip | Pescar o Rei do Lago Nevoento (andar 9) | Título *Rei do Lago* · Isco Dourado ×5 |
| R1_11 | Caça ao Slime Rei | Quadro da Guilda (rank E) | Derrotar o Slime Rei | 500 ouro · Coroa de Gel |
| R1_12 | Uivos de Cicatriz | Capitã Freya | Derrotar o Lobo Cicatriz | 600 ouro · Manto Cicatriz |
| R1_13 | Livros para a Tina | Tina (andar 2) | Levar 3 livros da biblioteca do Velho Fausto | A Tina muda-se para Ascendia (nova ajudante da alquimia: poções 10% mais baratas) |

---

## 9. Masmorra escondida — Toca das Raízes (andar 7)

| | |
|---|---|
| Entrada | Raiz Oca, aberta com os 4 Cristais de Seiva (andar 7) |
| Tamanho | 3 salas + sala do boss (masmorra fechada, sem céu) |
| Sala 1 | **Corredor das Raízes**: raízes saem do chão em padrões (esquivar no momento certo) |
| Sala 2 | **Ninho de Larvas**: muitas larvas pequenas (fracas) + 2 Treants de Musgo |
| Sala 3 | **Câmara do Âmbar**: puzzle de luz — rodar 3 espelhos de âmbar para levar a luz ao selo |
| Boss extra | **Larva Ancestral**: verme gigante de madeira podre (64×64) que escava e sai do chão; cospe ácido (veneno); aos 50% chama larvas |
| Recompensa | **Arco Raiz-Viva** (arma secreta, arco): as flechas prendem o alvo com raízes (Lentidão 2 s, 20%) · Baú de ouro · página de lore extra "Raízes" |

---

## 10. Peixes, plantas e animais

### Peixes
| Peixe | Onde | Quando | Raridade | Preço |
|---|---|---|---|---|
| Truta do Ribeiro | andar 3 | dia | comum | 25 |
| Perca Prateada | andar 3 e rio de Ascendia | sempre | comum | 20 |
| Peixe-Folha | andar 2 (riacho) | com chuva | incomum | 45 |
| Carpa Dourada | andar 9 | manhã (6:00–10:00) | raro | 120 |
| Enguia do Musgo | andar 8 (fontes) | noite | incomum | 60 |
| **Rei do Lago Nevoento** (lendário) | andar 9 | com nevoeiro, 5:00–7:00 | lendário | 1 500 |

### Plantas (quinta)
| Planta | Semente vem de | Dias a crescer | Estação | Usos |
|---|---|---|---|---|
| Nabo Bravo | Hana (loja) | 4 | Primavera | cozinha |
| Morango Silvestre | Folhalta | 6 (dá mais vezes) | Primavera, Verão | cozinha, presentes |
| Batata da Pradaria | erva alta do andar 1 (raro) | 6 | Primavera, Outono | cozinha |
| Flor de Mel | andar 6 | 5 | Primavera, Verão | doces, poções |
| Árvore Dourada | Bolota Dourada | 28 (árvore) | todas | dá 1 Maçã Dourada por semana (cozinha de luxo; a **primeira** maçã que comes dá +1 ponto de atributo) |

### Animais
- **Slime Bebé** (animal de estimação): do Slime Rei (1.ª vez). Apanha itens do chão à tua volta (raio 4 m).
- **Raposa da Floresta** (animal de estimação): missão R1_06. Fareja ervas e baús escondidos (mostra um "!" quando estás perto).

---

## 11. Eventos da região

| Evento | Quando | O que acontece |
|---|---|---|
| Lua Cheia | 1 noite em cada 7 | Lobos ×2 e Lobo Cicatriz com 20% de hipótese |
| Chuva de Pétalas | Primavera, andar 6 | Os bónus das flores duram o dobro |
| Fadas em Festa | sexta-feira à meia-noite, andar 4 | As fadas não atacam e vendem coisas raras |
| Mercador Errante | 5% ao entrar num andar | Vende itens raros de outras regiões |
| Tempestade | chuva com trovões | Raios caem em árvores: às vezes deixam **Madeira Fulminada** (rara) |

---

## 12. Arte desta região (lista de trabalho)

- [ ] **Kit de peças** (Blender): chão de relva ×3, caminho de terra, borda/falésia, rampa, escada de pedra,
  ponte de madeira, arco de pedra, carvalho ×2, pinheiro, bétula, rocha ×3, arbusto ×2, minério de cobre,
  árvore cortável, erva, baú, fogueira, cristal, tronco caído, toco, cerca de madeira, flores, cogumelos pequenos (≈ 28 peças)
- [ ] **Peças especiais dos andares** (≈ 40): ver a linha "Peças especiais" de cada andar
- [ ] **8 monstros** com todas as animações
- [ ] **2 monstros com nome**: Slime Rei, Lobo Cicatriz
- [ ] **8 guardiões** (48×48 ou 64×64): parado, mover, 3 ataques, dano, morrer
- [ ] **Mini-boss** Javali-Rei e **boss** Ent Ancião (ver `docs/BOSSES.md`)
- [ ] **Boss da masmorra** Larva Ancestral
- [ ] **Armas**: 12 de Cobre + 2 únicas + 8 de guardião + 1 secreta = **23 armas** (+ 23 ícones)
- [ ] **Ícones de materiais** (≈ 20), **peixes** (6), **plantas** (5 × 4 fases)
- [ ] **NPCs**: Bruno, Tina, Velho Cass, Tronco, Lothiel, Faelan, Mira, Eldrin, Tilly, Fada Lumi (+ retratos dos principais)
- [ ] **Animais**: Slime Bebé, Raposa da Floresta
- [ ] **Conjunto de armadura** de Couro de Javali (5 ícones)
