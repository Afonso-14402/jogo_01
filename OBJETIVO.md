# Objetivo do jogo

Este é **o plano oficial** do jogo. Tudo o que fazemos (código, arte, mapas) segue este documento.
Se quisermos mudar alguma coisa, muda-se **aqui primeiro**.

> Nome provisório: **A Torre** — ❓ escolher o nome final.

---

## 1. A ideia numa frase

Um RPG **isekai** em **2.5D**: acordas noutro mundo, numa **cidade** construída à volta de uma
**torre gigante**. Dizem que quem chegar ao topo pode voltar a casa. Sobes a torre andar a andar,
ficas mais forte, **recolhes materiais** e **fazes (crafting)** as tuas armas.

Inspirações: Sword Art Online (Aincrad), Tower of God, DanMachi, Ragnarok Online, Octopath Traveler.

---

## 2. Os 3 pilares (a regra para decidir tudo)

Qualquer ideia nova tem de servir pelo menos um destes pilares. Se não servir nenhum, fica de fora.

1. **A torre é o objetivo.** Tudo serve para subir: o crafting, os níveis, a cidade.
2. **Ficar mais forte vê-se.** Números a subir, armas novas no boneco, a cidade a crescer.
3. **Tem de caber em duas pessoas.** Se for trabalho a mais, simplifica-se ou fica para depois.

---

## 3. O ciclo do jogo

```
   Cidade ──► Entrar na torre ──► Lutar + recolher materiais ──► Boss do andar
     ▲                                                              │
     └──── Ferreiro faz arma melhor ◄── Voltar à cidade ◄── Drops ──┘
```

Os materiais de cada andar servem para fazer o equipamento que precisas para o andar seguinte.

---

## 4. O que torna o jogo especial

- **O "Sistema" isekai.** Mensagens no ecrã ao estilo anime:
  `[Sistema] Obtiveste a skill: Manejo de Espada Nv.1`.
  Janela de **Status** azul com nível, atributos e skills.
- **Cristal de Avaliação.** No início, na Guilda, tocas num cristal e ele revela a tua
  **Skill Única** (sorteada de uma lista). Cada partida começa um pouco diferente.
- **As skills sobem com o uso.** Se lutas com espada, sobe "Manejo de Espada". Se minas, sobe
  "Mineração" (dá mais minério). Nível do personagem e nível das skills são coisas separadas.
- **A cidade cresce contigo.** Ao derrotar bosses, abrem lojas novas, aparecem NPCs e o
  ferreiro aprende receitas. A torre vê-se de toda a cidade.
- **Rank de aventureiro** (F → S). Sobe com as missões da Guilda e desbloqueia andares e lojas.

---

## 5. Estilo visual: 2.5D / "HD-2D"

- **Mundo em 3D** (Blender): cidade, torre, andares, casas, rochas, árvores.
- **Bonecos em 2D** (pixel art): herói, NPCs, monstros e armas são *sprites* sempre virados
  para a câmara (*billboard*).
- **Câmara fixa**, inclinada por cima, a seguir o jogador (tipo Ragnarok). Dá para fazer zoom.
  A câmara **não roda**, senão cada boneco precisava de 8 direções desenhadas.
- Luzes, sombras e partículas 3D (fogo, magia, poeira) dão o aspeto "HD-2D".

---

## 6. Ferramentas (decidido)

| Parte do jogo | Ferramenta | Custo |
|---|---|---|
| Motor do jogo | **Godot 4** (versão estável mais recente) | Grátis |
| Linguagem | **GDScript** | Grátis |
| Mundo 3D | **Blender**, exportar em `.glb` | Grátis |
| Bonecos, monstros, armas, ícones, UI | **Pixelorama** para começar; **Aseprite** se quiseres o melhor | Grátis / ~20 € |
| Texturas do mundo | Pixelorama / Aseprite | — |
| Efeitos sonoros | **jsfxr** / **ChipTone** | Grátis |
| Música | **BeepBox** | Grátis |
| Arte provisória | **Kenney.nl**, **itch.io**, **OpenGameArt** | Grátis |
| Paleta de cores | **Lospec**: *Resurrect 64* | Grátis |
| Código e versões | **Git + GitHub** | Grátis |
| Builds automáticas | **GitHub Actions** | Grátis |

```
Blender  ──(.glb)──────────────►  Godot  ◄──(.png sprite sheet)──  Pixelorama / Aseprite
 cidade, torre, peças              junta tudo,                      herói, monstros, NPCs,
 dos andares                       código, câmara, luzes            armas, ícones, UI
```

---

## 7. Regras da arte

### Bonecos (2D)
- **Tamanho**: herói e NPCs 32×32 px; monstros 32×32 a 64×64; bosses até 128×128.
- **Direções do herói e NPCs**: baixo, cima e lado. O **lado é desenhado uma vez e espelhado**,
  por isso só desenhas **3 direções** em vez de 4.
- **Monstros**: só **lado** (espelhado) e, se der, baixo.
- **Animações do herói**: parado (2–4 frames), andar (4), atacar (3–4), levar dano (1–2), morrer (3–4).
- **Armas**: sprite **separado**, por cima do boneco, para a arma equipada aparecer no jogo.
  Ícone do inventário 16×16 px.
- **Paleta**: só cores da *Resurrect 64*.
- **Atalho opcional**: modelar o boneco no Blender e renderizar em pixel art, como no teu jogo
  anterior. Serve para bosses grandes.

### Mundo (3D)
- Modelos **low-poly** com texturas pixel art de 16×16 ou 32×32 (sem desfocar).
- **1 unidade do Blender = 1 metro** no Godot. O herói tem cerca de 1,6 m de altura.
- Os andares são feitos com um **kit de peças** do Blender (chão, parede, canto, porta, escada,
  rocha, árvore…) montadas no Godot com **GridMap**. Fazes as peças uma vez e montas muitos andares.

---

## 8. Decisões de jogo (decidido)

| Tema | Decisão | Porquê |
|---|---|---|
| Combate | **Tempo real** (ação), com esquiva e skills numa barra | É como em SAO e como no teu jogo anterior |
| Classe | **Livre no início.** No nível 10 escolhes a classe na Guilda (Espadachim, Arqueiro, Mago, Tanque) | Dá tempo ao jogador para experimentar armas antes de escolher |
| Andares | **Misto**: andares montados à mão com o kit de peças, com monstros, materiais e baús em posições aleatórias; **bosses sempre feitos à mão** | Os andares parecem desenhados mas cada visita é diferente |
| Câmara | **Fixa** (com zoom) | Menos arte a desenhar |
| Morrer | Acordas na estalagem e **perdes parte dos materiais** do andar (o ouro não) | Castiga sem frustrar |
| Multijogador | **Mais tarde** (depois da versão 1.0). O código fica preparado para isso | Faz o jogo demorar o dobro |
| Plataformas | **PC (Windows) e Android primeiro**, **Web** como demo com gráficos mais simples, **iOS** só no fim | O iOS precisa de um Mac e de uma conta Apple paga (~99 €/ano). O Godot na Web só usa o modo gráfico mais simples |

---

## 9. Mundo

### A cidade (zona segura)
- **Guilda de Aventureiros**: Cristal de Avaliação, missões, rank F → S, escolher classe.
- **Ferreiro**: crafting e melhoria de armas e armaduras.
- **Alquimista**: poções a partir de ervas e materiais.
- **Mercado**: comprar e vender.
- **Estalagem**: dormir, guardar o jogo, voltar a viver depois de morrer.
- **Entrada da torre**, no centro.

### A torre
- Cada andar tem monstros, pontos de recolha (minério, madeira, ervas) e a escada para cima.
- **De 5 em 5 andares há um boss.** Ao derrotá-lo ficas com um **teletransporte** da cidade
  para esse andar.
- Biomas por grupos de andares: 1–5 floresta · 6–10 cavernas · 11–15 deserto ·
  16–20 gelo · 21–25 vulcão · (mais depois).

---

## 10. Versão 1.0 (o que tem de estar feito)

Para o projeto não crescer para sempre, a primeira versão completa tem **só isto**:

- [ ] Cidade com Guilda, Ferreiro, Alquimista, Mercado e Estalagem
- [ ] Andares 1–10 (2 biomas) e 2 bosses (andar 5 e andar 10)
- [ ] 8 tipos de monstros
- [ ] Cerca de 15 armas (espada, arco, cajado, lança…) com raridades
- [ ] Recolher (minério, madeira, ervas) + crafting com receitas
- [ ] Status, níveis, skills que sobem com o uso e 4 classes
- [ ] Missões da Guilda e rank F → C
- [ ] Guardar e carregar o jogo
- [ ] PC + Android (+ demo Web)

Tudo o resto (mais andares, multijogador, companheiros de equipa, casas, pesca…) vai para a
**lista de ideias para depois** (secção 13).

---

## 11. Etapas (por esta ordem)

Cada etapa acaba com **algo que se pode jogar**.

1. [ ] **Protótipo cinzento**: projeto Godot, chão 3D, herói provisório (sprite) a andar, câmara a seguir. *(Claude)*
2. [ ] **Primeira arte**: o teu herói 32×32 + peças do kit no Blender a aparecer no jogo. *(tu + Claude)*
3. [ ] **Combate**: atacar, esquivar, 1 monstro com IA, dano, morrer, XP.
4. [ ] **Sistema isekai**: janela de Status, níveis, mensagens `[Sistema]`, skills que sobem com o uso.
5. [ ] **Recolher + inventário + crafting**: picareta, minério, ferreiro faz uma espada.
6. [ ] **Cidade**: os 5 edifícios, Cristal de Avaliação, guardar o jogo.
7. [ ] **Andares 1–5 + primeiro boss**: kit de peças, posições aleatórias, teletransporte.
8. [ ] **Telemóvel + builds automáticas**: controlos de toque, PC / Android / Web.
9. [ ] **Andares 6–10 + segundo boss**, classes, missões, resto das armas → **versão 1.0**.

---

## 12. Quem faz o quê

**Claude:** todo o código, a estrutura do projeto Godot, as tabelas de dados (itens, armas,
receitas, monstros, andares), sprites provisórios, testes automáticos e equilíbrio, builds e
explicações passo a passo do Godot, do Blender e do Pixelorama.

**Tu:** a arte final (bonecos, armas, kit de peças e cidade no Blender), a música (opcional) e
**jogar e dizer o que é divertido**.

---

## 13. Ideias para depois da 1.0

- Jogar a 2 (cooperativo)
- Companheiros recrutáveis na Guilda
- Mais andares e biomas (gelo, vulcão, céu…)
- Casa própria na cidade
- Pesca, cozinha
- Ciclo dia/noite
- História dos outros "isekaiados" que vivem na cidade
- iOS
