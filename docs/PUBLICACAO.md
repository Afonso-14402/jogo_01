# Publicação

Os textos para **mostrar o jogo ao mundo**: a página do itch.io (Demo), as descrições curtas, as palavras-chave,
os créditos e o que preparar antes de lançar. O nome do jogo é **Ascendia** (onde está `{NOME}`, entra
**Ascendia**).

> Os textos não estragam o segredo da história: nunca dizem "Aren", "Administrador", "sucessor" nem "diário".

---

## 1. Descrições

### 1.1 Uma frase (para redes sociais e para o cartão do itch.io)

| PT | EN |
|---|---|
| Acordaste noutro mundo, numa cidade ao pé de uma torre de 100 andares. Dizem que quem chega ao topo pode voltar a casa. | You woke up in another world, in a city at the foot of a 100-floor tower. They say whoever reaches the top can go home. |

### 1.2 Curta (até 300 letras)

**PT**
> Um RPG de ação isekai em 2.5D, com bonecos desenhados à mão. Sobe uma torre de 100 andares, onde cada andar é um
> mundo engolido. Forja as tuas armas, faz amigos em Ascendia e descobre porque é que uma janela azul te chama
> "Jogador nº 10 000".

**EN**
> A hand-drawn 2.5D isekai action RPG. Climb a 100-floor tower where every floor is a swallowed world. Forge your
> weapons, make friends in Ascendia, and find out why a blue window keeps calling you "Player No. 10,000".

### 1.3 Longa (página do itch.io)

**PT**

> **Acordas num prado. Uma janela azul diz: "Bem-vindo, Jogador nº 10 000."**
>
> À tua frente há uma cidade, Ascendia, construída à volta de uma torre tão alta que se perde nas nuvens. Cem
> andares. Dizem que cada andar é um pedaço de um mundo que a torre engoliu. Dizem que quem chegar ao topo pode voltar
> a casa. Ninguém chega ao topo há trezentos anos.
>
> **O que vais fazer:**
> - **Subir** 10 andares nesta Demo (100 no jogo completo), cada um com o seu bioma, segredos, puzzles e um guardião.
> - **Lutar** com 12 tipos de armas: espadas, lanças, foices, arcos, manoplas… e esquivar os ataques dos bosses.
> - **Forjar** as tuas armas com os materiais que encontras, e melhorá-las na forja do Brom.
> - **Fazer amigos**: 20 pessoas em Ascendia, cada uma com a sua história, os seus presentes preferidos e cenas
>   especiais. Os teus amigos mudam o fim.
> - **Pescar, cozinhar, plantar** na tua quinta, decorar a tua casa, apanhar o Bestiário inteiro.
> - **Descobrir** o que é a janela azul. E quem escreve as páginas que encontras em cada andar.
>
> Feito por uma pessoa a aprender, com bonecos desenhados à mão, pixel a pixel, e um mundo em 3D.

**EN**

> **You wake up in a meadow. A blue window says: "Welcome, Player No. 10,000."**
>
> Ahead of you there's a city, Ascendia, built around a tower so tall it disappears into the clouds. One hundred
> floors. They say each floor is a piece of a world the tower swallowed. They say whoever reaches the top can go
> home. No one has reached the top in three hundred years.
>
> **What you'll do:**
> - **Climb** 10 floors in this Demo (100 in the full game), each with its own biome, secrets, puzzles and a guardian.
> - **Fight** with 12 kinds of weapons: swords, spears, scythes, bows, gauntlets… and dodge the bosses' attacks.
> - **Forge** your weapons from the materials you find, and upgrade them at Brom's forge.
> - **Make friends**: 20 people in Ascendia, each with their own story, favourite gifts and special scenes. Your
>   friends change the ending.
> - **Fish, cook, farm**, decorate your house, fill the whole Bestiary.
> - **Find out** what the blue window is. And who wrote the pages you find on every floor.
>
> Made by one person learning as they go, with hand-drawn pixel-art characters in a 3D world.

---

## 2. Palavras-chave e categorias

| Onde | O quê |
|---|---|
| Género (itch.io) | Role Playing |
| Etiquetas (tags) | Action RPG · Isekai · Pixel Art · 2.5D · Crafting · Farming · Fishing · Story Rich · Singleplayer · Fantasy · Dungeon Crawler · Godot |
| Plataformas | Windows · Android · Web (HTML5) |
| Idiomas | Português (Portugal) · English |
| Classificação | para todas as idades a partir dos 10 anos (fantasia com monstros, sem sangue) |
| Preço da Demo | grátis |

---

## 3. Imagens e vídeo (lista para preparar)

| Peça | Tamanho | O que mostra | Feito |
|---|---|---|---|
| Capa (itch.io) | 630×500 | o herói de costas, pequenino, a olhar para a torre a partir da Praça de Ascendia, ao pôr do sol | [x] `capa.png` (+ `capa.gif` animada) |
| Banner da página | 960×300 | a torre a subir pelo meio, com as cores das 10 regiões em faixas | [x] `banner.png` (+ `banner.gif`) |
| 5 capturas de ecrã | 1920×1080 | o despertar no prado · combate com o Javali-Rei · a Praça de Ascendia com gente · a forja do Brom · a janela do Sistema a abrir | [x] `captura_1_despertar.png` … `captura_5_status.png` |
| GIF animado | 640×360, 6 s | uma esquiva perfeita e um golpe (mostra que tudo é animado) | [x] `esquiva_golpe.gif` |
| Trailer | 60–90 s | 1. ecrã preto, a janela azul: "Bem-vindo, Jogador nº 10 000." · 2. a torre · 3. combate · 4. amigos e cidade · 5. bosses · 6. a frase: "Dizem que quem chega ao topo pode voltar a casa." · 7. o nome | [ ] |
| Ícone (telemóvel) | 512×512 | a janela azul com uma torre pequenina dentro | [x] `icone.png` (também é o ícone do projeto e das exportações: `arte/ui/icone_*`) |

Tudo em `arte/publicacao/`. A capa, o banner e o ícone são desenhados por `ferramentas/arte/publicacao.py`
(pixel art ampliada sem desfocar); as capturas e o GIF vêm do jogo a sério, tirados pelo robô de capturas
(`testes/robo_captura.gd`, modos `p2`, `esquiva`, `praca`, `forja` e `status`, com `ROBO_TAM=1920x1080` e
`ROBO_ZOOM`) e juntos pelo mesmo script (`publicacao.py gif` e `publicacao.py capturas`).

A **arte é tua**: a capa e as capturas usam só arte acabada (nada de arte provisória).

---

## 4. Créditos (ecrã do jogo)

Aparecem no menu **Créditos** e no fim de cada final (por cima das imagens dos epílogos: `docs/guiao/finais.md`, secção 6).

```
{NOME}

Ideia, arte, animação e direção
    {o teu nome ou nome artístico}

Programação, escrita dos textos e ajuda em tudo
    Claude (Anthropic), com {o teu nome}

Música e sons
    {quem fizer a música; ou as bibliotecas usadas, com as licenças}

Feito com
    Godot Engine · Blender · Pixelorama / Aseprite

Fontes de letra
    {nome da fonte e licença}

Obrigado a
    {quem testou, família, amigos}
    e a ti, que jogaste até ao fim.

    — A.
```

> O "— A." no fim dos créditos é de propósito: só quem acabou o jogo percebe.
> Tudo o que **não for teu** (sons, músicas, fontes) tem de ter licença que deixe usar num jogo, e tem de ter o nome do
> autor nos créditos se a licença o pedir. Guarda as licenças numa pasta `licencas/` no projeto.

---

## 5. Antes de lançar a Demo (lista)

- [ ] O jogo abre e fecha bem em Windows, Android e no navegador.
- [ ] Grava e carrega sem perder nada (testar fechar o jogo a meio).
- [ ] Os 10 andares acabam-se do princípio ao fim sem bloquear.
- [ ] Os textos estão todos em PT e EN (sem chaves de tradução à vista).
- [ ] Os créditos e as licenças estão completos.
- [x] As capturas de ecrã, a capa e o GIF estão prontos.
- [ ] Um amigo que nunca viu o jogo jogou 30 minutos sem ajuda (e tu viste onde ficou preso).
- [ ] A página do itch.io está escrita (secção 1.3) e tem um link para mandar sugestões.
- [x] O nome do jogo está escolhido: **Ascendia**.
