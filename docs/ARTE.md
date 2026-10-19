# Regras da arte

Segue estas regras para tudo o que desenhares ou modelares entrar no jogo **sem ter de ser refeito**.

---

## 0. O padrão da arte (decidido)

- **Quem desenha é o Claude** (mudado a pedido do utilizador). Toda a arte (bonecos, monstros, bosses, armas,
  ícones, NPCs, retratos) é feita **píxel a píxel** por scripts em `ferramentas/arte/`, que geram os `.png` em
  `arte/`. O utilizador **vê cada desenho animado e aprova** (ou pede mudanças). Qualquer desenho pode ser
  retocado à mão no **Pixelorama** ou no **Aseprite** (nesse caso, o `.png` retocado passa a ser o oficial e o
  script deixa de o gerar).
- **O estilo de referência é a Aranha-Mãe "pixel a pixel"**, em `arte/referencia/aranha_mae/`:
  - formas grandes e simples que se leem de longe;
  - luz sempre a vir de **cima à esquerda**, com um brilho forte e marcado;
  - **contorno escuro** (`#2e222f`) à volta de cada peça (corpo, cabeça, pernas…);
  - as partes do corpo **bem separadas** (as pernas não tapam o corpo);
  - pormenores de cor viva **só onde interessa** (olhos, marcas, veneno).
- **Tudo é animado.** Nenhum boneco, monstro ou NPC entra no jogo parado: cada um tem pelo menos as
  animações da sua lista (secções 2 e 3). Desenha as poses **uma a uma** (antecipação → ação → volta).
- **Ver sempre a animação a correr antes de dar por acabado**, no **Visualizador de Sprites**:
  - no repositório: `ferramentas/visualizador.html` (abre no browser com duplo clique);
  - ou online: https://claude.ai/artifact/BBE65E9dT8pp4xc81Q9zE8
  - Abres o PNG, vês a animação, ligas o *onion skin* para comparar frames, e ele verifica
    o nome do ficheiro, o tamanho dos frames, o fundo transparente e as cores da paleta.
- **O que é feito por código (não se desenha):** piscar a branco ao levar dano, tremer o ecrã,
  sombras, brilhos de raridade, versões Elite (mudança de cor), partículas e o movimento pelo mapa.
  Os monstros também respiram, saltitam a andar, agacham-se no aviso do ataque, esticam-se no golpe, encolhem ao
  levar um golpe e desfazem-se num "puf" de fumo ao morrer (`arte/efeitos/fumo_morte.png`); os bosses piscam e
  rebentam aos bocados ao morrer e brilham ao mudar de fase.
- **Golpes e skills** (feito por código, `scripts/personagens/boneco_arma.gd` e `scripts/combate/skill_fx.gd`): a arma
  prepara (puxa atrás), varre depressa e acompanha, com um **rasto** (3 cópias claras nos ângulos de há pouco); as skills
  mostram um **círculo mágico** aos pés (`conjurar_<elemento>`), uma **onda no chão** nas de área (`onda_<elemento>`,
  ampliada 1–4× conforme o raio), **chuva** de flechas ou estrelas (`queda_flecha`, `queda_estrela`), **fantasmas** na
  investida, o **grito** do Provocar e a câmara treme. O "físico" das explosões é uma onda de pó, não uma bola.
- **Companheiros** (`docs/SISTEMAS.md`, secção 20): além de parado e andar, têm os 6 golpes e `dano` com as poses do
  herói, no corpo e na cara deles (`ferramentas/arte/companheiros_combate.py`).
- **Humanoides grandes** (guardiões, mini-bosses e bosses de 48 px ou mais): molde `ferramentas/arte/heroico.py`,
  com proporções de adulto (cabeça pequena, ombros largos, armadura, capa, arma grande, olhos a brilhar), desenhados
  já no tamanho certo (nunca ampliados). Os humanoides pequenos continuam com o corpo do herói (`humanoide.py`).

---

## 1. Regras gerais

- **Paleta**: só as cores da **Resurrect 64** (Lospec). Importa-a no Pixelorama / Aseprite.
- **Formato**: `.png` com fundo **transparente**.
- **Nunca** desfocar, suavizar ou redimensionar com filtro: só pixel art "dura".
- **Nomes dos ficheiros**: tudo em **minúsculas**, **sem espaços** e **sem acentos**, com `_` a separar.
  - ✅ `lobo_cinzento_andar_lado.png` · ❌ `Lobo Cinzento (andar).PNG`
- Guarda **também o ficheiro de trabalho** (`.pxo` do Pixelorama ou `.aseprite`) ao lado do `.png`.

---

## 2. Herói

- **Tamanho**: 32×32 px por frame. O herói ocupa cerca de 16 px de largura e 26 px de altura,
  com os **pés no fundo do quadro** (centro em baixo).
- **Direções**: `baixo`, `cima`, `lado`. O lado é virado para a **direita**; a esquerda é espelhada no jogo.
- **O herói desenha-se SEM arma.** A arma é um sprite separado (ver secção 4).

| Animação | Frames | Notas |
|---|---|---|
| `parado` | 4 | respirar |
| `andar` | 6 | |
| `esquiva` | 4 | rolar / dash |
| `dano` | 2 | |
| `morrer` | 5 | |
| `recolher` | 4 | minar / cortar / apanhar |
| `ataque_corte` | 4 | espada, adaga, katana, foice |
| `ataque_pesado` | 5 | espada grande, machado, martelo |
| `ataque_estocada` | 4 | lança |
| `ataque_disparo` | 4 | arco, besta |
| `ataque_magia` | 4 | cajado |
| `ataque_soco` | 4 | manoplas |
| `nadar` | 6 | debaixo de água (região 6) |
| `planar` | 2 | com a Capa Planadora (região 9) |
| `montar` | 2 | sentado na montada (a montada mexe-se por baixo) |
| `pescar` | 4 | lançar, esperar, puxar |
| `beber` | 3 | poções |
| `celebrar` | 4 | subir de nível, vitória |
| `sentar` | 1 | bancos, jantares |

Total: cerca de **72 frames × 3 direções ≈ 216 frames**.

**Exportar**: uma tira horizontal por animação e direção, ex.: `heroi_andar_baixo.png` (6 frames de 32×32 = 192×32 px).

**Criação de personagem** (8 penteados, 6 tons de pele, 10 cores de cabelo, 6 cores de olhos, 4 roupas do mundo real):
`arte/heroi/aparencia/heroi_<anim>_<dir>_<penteado>.png` usa **cores-índice** (cada parte tem cores só suas) e o jogo
troca-as com um shader de paleta lendo `arte/heroi/paletas.json` (gerados por `ferramentas/arte/heroi_aparencia.py`).

---

## 3. Monstros e NPCs

| Tipo | Tamanho | Direções |
|---|---|---|
| NPCs da cidade | 32×32 | `baixo`, `cima`, `lado` (só `parado` e `andar`) |
| Monstros normais | 32×32 ou 48×48 | só `lado` (espelhado) |
| Guardiões dos andares | 48×48 ou 64×64 | `lado` |
| Monstros com nome | 48×48 a 128×128 | `lado` |
| Mini-bosses | 64×64 | `lado` |
| Bosses | 96×96 a 128×128 | `lado` (+ `baixo` se der) |
| Bosses das masmorras | 64×64 | `lado` |

| Animação | Frames |
|---|---|
| `parado` | 2–4 |
| `mover` | 4 |
| `atacar` | 4 |
| `dano` | 1 |
| `morrer` | 4 |
| Guardiões e monstros com nome: `ataque_1`, `ataque_2`, `ataque_3` | 4–6 cada |
| Bosses: `especial_1` … `especial_6`, `mudar_fase` | 4–8 cada |

Cada monstro tem também as animações **especiais** escritas na ficha dele (ex.: `disfarce`, `acordar`, `enterrar`).

**Exportar**: `lobo_cinzento_mover_lado.png`, `ent_anciao_especial_1_lado.png`, etc.

---

## 4. Armas

- **Uma imagem por arma** (sem animação). O jogo roda e mexe a arma durante o ataque.
- **Posição**: arma **na vertical, a apontar para cima**, com o **punho no centro em baixo** do quadro.
  (Arco e besta: na vertical, com o meio da arma no centro do quadro.)
- **Tamanhos**: 32×32 ou 48×48 conforme o tipo (ver `docs/ARMAS.md`).
- **Ícone do inventário**: 16×16, arma **na diagonal** (punho em baixo à esquerda).
- **Raridade**: **não** desenhes versões diferentes; o brilho é feito pelo jogo.

**Nomes**: `espada_cobre.png` + `espada_cobre_icone.png`, `arco_hidra.png` + `arco_hidra_icone.png`.

Por região: **12 normais + 2 únicas + 8 de guardião + 1 secreta = 23 armas** (e 23 ícones), mais as raras e as míticas
(ver `docs/ARMAS.md`).

Também são precisos: **flecha** e **virote** (projéteis), e um efeito de magia por elemento.

---

## 5. Ícones e interface

- **Ícones de itens** (materiais, poções, armaduras, comida, peixes, sementes): 16×16.
- **Ícones de skills**: 24×24 (120 de classe + 36 de armas + 12 Skills Únicas).
- **Janelas do Sistema**: estilo isekai azul translúcido (ver `docs/INTERFACE.md`); o Claude faz uma versão provisória.

---

## 6. Mundo 3D (Blender)

### Regras
- **Escala**: 1 unidade = 1 metro. O herói tem ~1,6 m. Uma porta tem ~2,2 m.
- **Grelha**: as peças do kit encaixam numa **grelha de 2×2 m** (chão 2×2, parede 2 m de largura).
- **Origem** de cada peça **no centro em baixo**. Antes de exportar: *Apply → All Transforms*.
- **Low-poly**: o mínimo de polígonos que fique bem.
- **Texturas**: pixel art de 32×32 px (ou 64×64 para coisas grandes), no Blender com interpolação **Closest**.
- **Exportar**: `File → Export → glTF 2.0 (.glb)`, uma peça por ficheiro.
- Guarda **também o `.blend`**.

### Kit de peças de cada região (~25 peças)

| Grupo | Peças |
|---|---|
| Chão | 3 variações + 1 caminho + 1 borda |
| Paredes / falésias | parede, canto, rampa, escada |
| Passagens | ponte, porta / arco, escada para o andar seguinte |
| Natureza | 3 árvores (ou equivalente do bioma), 3 rochas, 2 arbustos / plantas |
| Recolha | ponto de minério, árvore que se corta, erva |
| Objetos | baú, fogueira da Zona Segura, cristal de teletransporte |
| Decoração | 3–5 peças do tema (ex.: cogumelo gigante, vagoneta, coral) |

E por cada **andar**: 3–5 peças especiais só desse andar (linha "Peças especiais" de cada andar em `docs/regioes/`).

**Nomes**: `r01_chao_1.glb`, `r01_arvore_2.glb`, `a04_cogumelo_gigante.glb` (a04 = andar 4).

### 6.1 Natureza e vida dos andares (pixel art)

O que é **vivo** no mundo desenha-se em pixel art, como os bonecos (16 px = 1 m), e fica de frente para a câmara:
- **Chão**: 4 texturas de 64×64 por região (base, variante, terra, caminho), misturadas no jogo com bordas
  recortadas, manchas grandes de cor e sombras de nuvens a passar. Nas colinas, a erva de cima "cai" 2–4 píxeis
  pelo lado (com uma linha escura por baixo), a borda de cima tem uma linha clara e o chão ao pé de uma parede
  fica mais escuro; as paredes de rocha têm camadas (estratos). → `ferramentas/arte/natureza.py`
- **Plantas e rochas**: árvores, arbustos, erva, flores, rochas e pedrinhas de cada região (sprites). Abanam ao
  vento (as rígidas — cactos, árvores mortas, coral — quase nada). Quando o herói passa por trás de uma
  árvore (ou de uma casa), ela fica inteira mas abre-se uma **janela redonda** à volta dele, com a borda aos
  quadradinhos do tamanho dos píxeis do desenho. À volta do mapa há sempre várias filas de árvores (ou água / vazio), para nunca se ver o fim do mundo.
  Todas as regiões têm os seus desenhos (nada de peças 3D fotografadas para a natureza): por exemplo estalagmites
  altas e cristais grandes nas grutas, rochas de mármore com relva e veios de ouro e balões de ar quente no Céu,
  árvores negras com folhas de luz, copas cor da noite com estrelas e cristais roxos no Abismo.
- **Vida** (`dados/vida.json`, `ferramentas/arte/vida.py`): bichos pequenos que não se lutam — borboletas,
  pássaros, coelhos, morcegos, libelinhas, sapos, lagartos, caranguejos — que fogem do herói; peixes a saltar
  na água; bandos de pássaros a passar; e partículas no ar (pirilampos à noite, pólen, esporos, brasas,
  fogos-fátuos, folhas a cair). Cada região tem os seus (tabela em `ferramentas/dados/vida.py`).

- **Detalhes e objetos** (`ferramentas/arte/objetos.py`): troncos caídos, tocos, cogumelos, erva alta, juncos,
  cristais, ossos, conchas; cercas, placas, barris, caixotes, carroças, pilares partidos, menires, tendas, campas…
- **Cenários**: pequenos grupos destes objetos que contam uma história (acampamento abandonado, ruína, círculo de
  cogumelos, carroça partida, cemitério…), 2 a 9 por andar, longe da Zona Segura. Também há pequenos bosques no
  meio dos prados e juncos à beira da água. Nenhum sítio do mapa deve ficar vazio.
- **Água**: mais clara junto à margem, mais escura no fundo, com espuma a mexer-se encostada à terra.

As peças 3D (Blender) ficam para o que é **grande e construído**: muralhas, pontes, casas, baús, cristais.

### Cidade
Guilda, Ferreiro, Alquimista, Mercado, Estalagem, casas genéricas (3), base da torre, fonte, bancas, candeeiros.

---

## 7. Arte extra (NPCs, atividades)

| O quê | Tamanho | Quantidade | Notas |
|---|---|---|---|
| **Retratos dos NPCs** (caixa de diálogo) | 64×64 | 20 NPCs × 4 emoções | `normal`, `feliz`, `zangado`, `triste` + 1 do herói e do Kai |
| **NPCs principais** (sprites) | 32×32 | 20 | `parado` e `andar`, 3 direções |
| **Aldeões** | 32×32 | ~10 | Podem ser **mudanças de cor** de 3 bases |
| **NPCs das povoações** | 32×32 | ~90 | ver a secção 7 de cada região; os genéricos são **mudanças de cor** de 3 bases por povo |
| **Animais de estimação** | 16×16 a 32×32 | 12 | `parado`, `mover`, `atacar`, só `lado` |
| **Animais da quinta** | 32×32 | 5 | galinha, vaca, cabra, ovelha, abelhas |
| **Montadas** | 48×48 | 5 | `parado`, `mover`, `lado` (o herói vai em cima) |
| **Peixes** (ícones) | 16×16 | 60 | |
| **Comida, poções, sementes, gemas, materiais** (ícones) | 16×16 | ~500 | |
| **Plantas da quinta** | 16×16 | ~50 | 4 fases de crescimento cada |
| **Móveis da casa** | Blender + pixel art | ~200 | ver `docs/ITENS.md`, secção 10. No 2D, os básicos mais usados (cama, mesa, cadeira, banco, estantes, secretária, lareira, armário, baú, tapetes, candeeiro, vela, plantas, quadro) são desenhados em pixel art por `ferramentas/arte/moveis2d.py` (4 rotações; a vela e a lareira com a chama animada); os da região usam o desenho do básico |
| **Edifícios de Ascendia** | Blender | ~40 | ver `docs/CIDADES.md` |
| **Povoações** | Blender | ~8 peças por povoação (26) | casas e objetos de cada povo |
| **Cidade Errante** | Blender | 1 tartaruga gigante + ~10 peças | |
| **Roupas e cores do herói** | — | — | Feitas no jogo **trocando as cores** do herói (sem desenho novo) |
| **Caixa de diálogo e janelas do Sistema** | — | — | O Claude faz uma versão provisória |

---

## 8. Pastas

```
arte/
  heroi/                     heroi_andar_baixo.png, ...
  npcs/                      brom_parado_baixo.png, ...
  retratos/                  brom_normal.png, brom_zangado.png, ...
  animais/                   slime_bebe_mover_lado.png, lagarto_areia_mover_lado.png, ...
  moveis/                    cama_simples.blend, cama_simples.glb, ...
  armas/                     espada_cobre.png, espada_cobre_icone.png, ...
  icones/                    minerio_cobre.png, pocao_vida.png, ...
  ui/
  masmorras/                 armadilha_raiz.png, armadilha_lamina.png, ... (ferramentas/arte/armadilhas.py)
  cidade/                    guilda.blend, guilda.glb, ...
  regioes/
    r01_floresta/
      monstros/              slime_verde_mover_lado.png, ...
      kit/                   r01_chao_1.blend, r01_chao_1.glb, ...
      andares/               a04_cogumelo_gigante.glb, ...
    r02_cavernas/
    ...
    r10_abismo/
  sons/
  musica/
```

---

## 9. Ordem de trabalho (Fase A)

Faz por esta ordem e **mostra-me cada parte** quando acabares, para eu a pôr no protótipo:

1. **Herói**: só `parado` e `andar` (3 direções). → testar no jogo
2. **1 peça de chão + 1 árvore + 1 rocha** da Região 1. → testar no jogo (escala, cores, câmara)
3. Resto das animações do herói
4. **Espada de Cobre** + ícone. → testar na mão do herói
5. Resto do **kit da Região 1**
6. **8 monstros** da Região 1 (e os 2 monstros com nome)
7. **23 armas** da Região 1 (12 de cobre, 2 únicas, 8 de guardião, 1 secreta) + ícones
8. **8 guardiões**, **Javali-Rei**, **Ent Ancião** e **Larva Ancestral**
9. Peças especiais dos andares 1–10
10. **Cidade** (edifícios da Demo)
11. **NPCs da Demo** + retratos: Lyra, Gorvan, Brom, Selene, Tobias, Dona Marta, Kai, Pip, Mia
12. Ícones de comida, poções, peixes e materiais da Região 1

> Os passos 1, 2 e 4 são os mais importantes: se o tamanho ou o estilo não ficar bem no jogo,
> corrige-se logo, **antes** de haver centenas de desenhos feitos.

---

## 10. Checklist por região

Cada ficheiro de região tem, na **secção 12**, a lista exata do que desenhar. Em geral:

- [ ] Kit de peças (~28) e peças especiais dos 10 andares (~45)
- [ ] 8 monstros, 2 monstros com nome, 8 guardiões (todas as animações)
- [ ] Mini-boss, boss e boss da masmorra escondida
- [ ] 23 armas + ícones
- [ ] Ícones dos materiais, peixes (6), plantas (4 fases)
- [ ] NPCs das povoações + retratos
- [ ] Animais de estimação / montadas
- [ ] Conjunto de armadura (5 ícones)
- [ ] Música da região (opcional)

---

## 11. Lista total de arte (para a 1.0)

Isto é **tudo** o que o jogo completo precisa. A **Demo** é só a Região 1 e a cidade (cerca de 1/10).

| O quê | Quantidade | Frames / peças (aprox.) |
|---|---|---|
| Herói | 1 (+ variações de cor) | ~216 frames |
| Monstros normais | 80 | ~2 000 frames |
| Monstros com nome | 20 | ~600 frames |
| Guardiões | 79 | ~2 400 frames |
| Mini-bosses e bosses | 20 | ~1 200 frames |
| Bosses das masmorras | 10 | ~350 frames |
| NPCs principais | 20 | ~600 frames |
| NPCs das povoações | ~90 | ~1 800 frames (muitos são mudanças de cor) |
| Retratos | ~160 | 64×64 |
| Animais (estimação, montadas, quinta) | 22 | ~300 frames |
| Armas | ~258 | 258 sprites + 258 ícones |
| Ícones (itens, armaduras, acessórios, skills) | ~900 | 16×16 e 24×24 |
| Plantas | ~50 | 200 imagens |
| Kits de peças 3D | 10 | ~280 peças |
| Peças especiais dos andares | 100 andares | ~460 peças |
| Cidade, povoações, Cidade Errante | — | ~250 peças |
| Móveis | ~200 | peças 3D |
| Efeitos (projéteis, magias, partículas) | — | ~60 |

### O que **não** se desenha (o jogo reutiliza)
- **Elites**: mudança de cor + brilho dos monstros normais.
- **Ecos** (região 10), **Clone Espelhado** e **Reflexo Negro**: sprites existentes com um *shader*.
- **Eco dos Guardiões** e **estátuas dos bosses** (andar 99): sprites existentes com *shader*.
- **Raridades das armas**: brilho feito pelo jogo.
- **Cores do herói e dos aldeões**: troca de paleta.
- **Andar 94** e **Andares do Eco**: reutilizam os kits de todas as regiões.
