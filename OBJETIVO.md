# Objetivo do jogo (versão 0 — antes de programar)

Documento de planeamento. Vai mudando à medida que decidimos as coisas.
As partes marcadas com **❓** ainda estão por decidir.

---

## 1. A ideia numa frase

Um RPG **isekai** em **2.5D**: acordas noutro mundo, numa **cidade** construída à volta de uma
**torre gigante**. Para voltar a casa tens de **subir a torre andar a andar**, ficar mais forte,
**recolher materiais** e **fazer (crafting)** as tuas armas e equipamento.

Inspirações: Sword Art Online (Aincrad), Tower of God, DanMachi, Ragnarok Online, Octopath Traveler.

---

## 2. Estilo visual: 2.5D / "HD-2D"

- **Mundo em 3D**: cidade, torre, chão, casas, árvores e masmorras são modelos 3D (feitos no Blender).
- **Bonecos em 2D**: o herói, os NPCs, os monstros e as armas são **sprites pixel art** desenhados,
  colocados dentro do mundo 3D e sempre virados para a câmara (*billboard*).
- **Câmara** inclinada por cima, a seguir o jogador (tipo Ragnarok / Octopath).
- Luzes, sombras e partículas 3D (fogo, magia, poeira) dão o aspeto "HD-2D".

---

## 3. Ferramentas

| Parte do jogo | Ferramenta | Grátis? | Notas |
|---|---|---|---|
| Motor do jogo | **Godot 4** | Sim | Faz bem o 3D + sprites 2D. Exporta para PC, Web, Android e iOS. |
| Linguagem | **GDScript** | Sim | Parecida com Python. Sou eu que escrevo a maior parte. |
| Mundo 3D (cidade, torre, andares) | **Blender** | Sim | Modelos *low-poly* exportados em `.glb`. O Godot importa-os diretamente. |
| Bonecos, monstros, armas | **Aseprite** (~20 €) ou **Pixelorama** | Pixelorama é | Pixel art com animação. Exporta *sprite sheets* que o Godot lê. |
| Texturas do mundo | Aseprite / Pixelorama | — | Texturas pequenas (16×16 ou 32×32) em pixel art, sem desfocar (*nearest*). |
| Ícones e interface (UI) | Aseprite / Pixelorama | — | Inventário, janela de *Status* estilo isekai, botões. |
| Efeitos sonoros | **jsfxr** / **ChipTone** | Sim | Golpes, apanhar itens, subir de nível. |
| Música | **BeepBox** (ou LMMS) | Sim | |
| Arte provisória | **Kenney.nl**, **itch.io**, **OpenGameArt** | Sim | Para testar o jogo antes da arte final estar pronta. |
| Paletas de cores | **Lospec** | Sim | Uma paleta fixa para tudo ter o mesmo estilo. |
| Código e versões | **Git + GitHub** | Sim | Este repositório. |
| Builds automáticas | **GitHub Actions** | Sim | Gera as versões PC / Web / Android sozinho, como no jogo anterior. |

### Como as coisas passam de uma ferramenta para a outra

```
Blender  ──(.glb)──────────────►  Godot  ◄──(.png sprite sheet)──  Aseprite / Pixelorama
 cidade, torre, andares,          junta tudo,                       herói, monstros, NPCs,
 casas, rochas, árvores           código, câmara, luzes             armas, ícones, UI
```

---

## 4. Regras da arte (para tudo bater certo)

- **Tamanho dos bonecos**: 32×32 px (herói e NPCs), monstros entre 32×32 e 64×64, bosses maiores.
- **Direções**: 4 direções (baixo, cima, esquerda, direita). Mais tarde, se a câmara rodar, 8.
- **Animações mínimas por boneco**: parado, andar, atacar, levar dano, morrer.
- **Armas**: sprite **separado** por cima do boneco, para a arma que equipas aparecer no jogo.
  - Ícone do inventário: 16×16 px.
- **Paleta**: uma só paleta para o jogo inteiro (proposta: *Resurrect 64* ou *Endesga 32* da Lospec).
- **Blender**: modelos simples (*low-poly*) com texturas pixel art. 1 unidade do Blender = 1 metro no Godot.

---

## 5. Mundo

### A cidade (zona segura, início do jogo)
- **Guilda de Aventureiros**: missões, *rank* de aventureiro (F → E → D → C → B → A → S).
- **Ferreiro**: crafting e melhoria de armas e armaduras.
- **Alquimista**: poções a partir de ervas e materiais.
- **Loja / mercado**: comprar e vender.
- **Estalagem**: dormir e guardar o jogo.
- **Entrada da torre**, no centro da cidade.

### A torre
- Cada **andar** é uma zona 3D (feita no Blender) com monstros, materiais para recolher e uma saída.
- De **5 em 5 andares** há um **boss**. Derrotá-lo desbloqueia o andar seguinte e um teletransporte.
- Os andares mudam de bioma: floresta → cavernas → deserto → gelo → vulcão → …
- ❓ Andares **feitos à mão** no Blender ou partes **geradas aleatoriamente** com código?

---

## 6. Mecânicas (primeira versão)

**Isekai**
- Janela de **Status** (estilo anime): nível, XP, HP, MP, Força, Agilidade, etc.
- **Subir de nível** e distribuir pontos.
- **Skills** que se desbloqueiam com o nível ou com o uso.
- ❓ **Classe** escolhida no início (espadachim, arqueiro, mago…) ou livre?

**Recolher e crafting**
- Recolher: minérios (picareta), madeira (machado), ervas e *drops* dos monstros.
- Crafting no ferreiro e no alquimista com receitas.
- Armas com **raridade** (Comum → Raro → Épico → Lendário).

**Combate**
- ❓ Em **tempo real** (como o teu jogo anterior) ou **por turnos**?

---

## 7. Quem faz o quê

**O Claude ajuda com:**
- Todo o código em Godot (movimento, câmara, combate, inimigos, IA, inventário, crafting, status, níveis, guardar o jogo, controlos de toque).
- Estrutura do projeto Godot e as cenas.
- Tabelas de dados (itens, armas, receitas, monstros, andares) em ficheiros fáceis de editar.
- Sprites **provisórios** gerados por código, para testar já.
- Equilíbrio do jogo (dano, XP, preços) com testes automáticos.
- Builds automáticas para PC / Web / Android.
- Explicar como usar o Blender, o Aseprite e o Godot passo a passo.

**Tu fazes:**
- A arte final: desenhar os bonecos e as armas, modelar a cidade e a torre no Blender.
- A música, se quiseres.
- Jogar e dizer o que é divertido e o que não é.

---

## 8. Plano por etapas

1. **Protótipo cinzento**: projeto Godot com o chão em 3D, o herói como sprite provisório a andar, câmara a seguir. *(Claude)*
2. **Primeira arte**: o herói 32×32 desenhado por ti + uma casa e um chão do Blender a aparecer no jogo.
3. **Combate**: atacar, um monstro, dano, morrer, XP.
4. **Status e níveis**: janela de Status isekai.
5. **Recolher + inventário + crafting**: picareta, minério, ferreiro faz uma espada.
6. **Cidade**: guilda, ferreiro, loja, estalagem (guardar).
7. **Torre andares 1–5 + primeiro boss**.
8. **Telemóvel e Web**: controlos de toque e builds.
9. Mais andares, mais armas, mais skills…

---

## 9. Perguntas em aberto ❓

1. Nome do jogo?
2. Combate em tempo real ou por turnos?
3. Classes no início ou personagem livre?
4. Andares da torre feitos à mão, aleatórios, ou misto?
5. A câmara roda à volta do jogador ou fica fixa?
6. Jogar a 2 (multijogador) desde o início ou só mais tarde?
7. Aseprite (pago, melhor) ou Pixelorama (grátis)?
