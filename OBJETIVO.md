# Objetivo do jogo

Este é **o plano oficial** do jogo. Tudo o que fazemos (código, arte, mapas) segue este documento.
Se quisermos mudar alguma coisa, muda-se **aqui primeiro**.

> Nome provisório: **A Torre** — ❓ escolher o nome final (propostas em [`docs/PROPOSTAS.md`](docs/PROPOSTAS.md)).

Documentos que fazem parte do plano (o **índice completo**, com a ordem de leitura, está em [`docs/README.md`](docs/README.md)):

| Documento | O que tem |
|---|---|
| [`docs/TORRE.md`](docs/TORRE.md) | Visão geral dos **100 andares** (tabela de todos os andares) |
| [`docs/regioes/`](docs/regioes/) | **As 10 regiões**, andar a andar: monstros, guardiões, povoações, missões, segredos, peixes, arte |
| [`docs/BOSSES.md`](docs/BOSSES.md) | Os **20 bosses** com fases e ataques, e o duelo com o Kai |
| [`docs/CIDADES.md`](docs/CIDADES.md) | **Ascendia**, a tua casa, a quinta, as **26 povoações** e a **Cidade Errante** |
| [`docs/NPCS.md`](docs/NPCS.md) | Os **20 NPCs** de Ascendia com perfil completo, diálogo, amizade e companheiros |
| [`docs/HISTORIA.md`](docs/HISTORIA.md) | A **história** toda, os segredos e os **4 finais** |
| [`docs/MISSOES.md`](docs/MISSOES.md) | História principal, Guilda, festivais (~270 missões no total) |
| [`docs/ARMAS.md`](docs/ARMAS.md) | **~258 armas** com stats, preços e receitas |
| [`docs/EQUIPAMENTO.md`](docs/EQUIPAMENTO.md) | Armaduras, acessórios, gemas e encantamentos |
| [`docs/ITENS.md`](docs/ITENS.md) | Poções, comida, materiais, plantas, quinta, móveis, presentes |
| [`docs/PROGRESSAO.md`](docs/PROGRESSAO.md) | Status, Skill Única, **20 classes com 120 skills**, skills de armas e de vida |
| [`docs/ATIVIDADES.md`](docs/ATIVIDADES.md) | Minijogos, coleções, títulos, conquistas, pós-jogo |
| [`docs/SISTEMAS.md`](docs/SISTEMAS.md) | **Todas as regras e fórmulas** (combate, XP, drops, economia, tempo…) |
| [`docs/PROGRAMACAO.md`](docs/PROGRAMACAO.md) | **Guia técnico do Godot**: pastas, cenas, dados, ordem de implementação |
| [`docs/INTERFACE.md`](docs/INTERFACE.md) | Todos os ecrãs e menus (PC e telemóvel) |
| [`docs/AUDIO.md`](docs/AUDIO.md) | Músicas e efeitos sonoros |
| [`docs/ARTE.md`](docs/ARTE.md) | **Regras da arte** e a **lista total de arte** |
| [`docs/guiao/`](docs/guiao/) · [`docs/dialogos/`](docs/dialogos/) · [`docs/textos/`](docs/textos/) | O **guião** de todas as cenas e dos 4 finais, os **diálogos** de toda a gente e os **textos** do jogo |
| [`docs/PUBLICACAO.md`](docs/PUBLICACAO.md) · [`docs/TRADUCAO.md`](docs/TRADUCAO.md) | Textos para publicar a Demo e regras da tradução para inglês |

---

## 1. A ideia numa frase

Um RPG **isekai** em **2.5D**: acordas noutro mundo, numa **cidade** construída à volta de uma
**torre de 100 andares**. Dizem que quem chegar ao topo pode voltar a casa. Cada andar é
**um mundo grande, com o seu próprio bioma**. Sobes a torre, ficas mais forte, **recolhes
materiais** e **fazes (crafting)** as tuas armas.

Inspirações: Sword Art Online (Aincrad), Tower of God, DanMachi, Ragnarok Online, Octopath Traveler.

---

## 2. Os 3 pilares (a regra para decidir tudo)

Qualquer ideia nova tem de servir pelo menos um destes pilares. Se não servir nenhum, fica de fora.

1. **A torre é o objetivo.** Tudo serve para subir: o crafting, os níveis, a cidade.
2. **Ficar mais forte vê-se.** Números a subir, armas novas na mão do boneco, a cidade a crescer.
3. **Uma região de cada vez.** A torre faz-se por **regiões de 10 andares**. Uma região só
   começa quando a anterior está acabada (arte + jogo). Assim o jogo está sempre jogável.

---

## 3. O ciclo do jogo

```
   Cidade ──► Entrar na torre ──► Explorar o andar, lutar, recolher ──► Boss
     ▲                                                                   │
     └──── Ferreiro faz arma melhor ◄── Voltar à cidade ◄──── Drops ─────┘
```

Os materiais de cada região servem para fazer as armas que precisas para a região seguinte.

---

## 4. O que torna o jogo especial

- **O "Sistema" isekai.** Mensagens no ecrã ao estilo anime:
  `[Sistema] Obtiveste a skill: Manejo de Espada Nv.1`.
  Janela de **Status** azul com nível, atributos e skills.
- **Cristal de Avaliação.** No início, na Guilda, tocas num cristal e ele revela a tua
  **Skill Única** (sorteada de uma lista). Cada partida começa um pouco diferente.
- **As skills sobem com o uso.** Se lutas com espada, sobe "Manejo de Espada". Se minas, sobe
  "Mineração". Nível do personagem e nível das skills são coisas separadas.
- **A cidade cresce contigo.** Ao derrotar bosses, abrem lojas novas, aparecem NPCs e o
  ferreiro aprende receitas. A torre vê-se de toda a cidade.
- **Rank de aventureiro** (F → SSS). Sobe com as missões da Guilda.
- **100 andares, 100 sítios diferentes.** Cada andar tem nome, paisagem e segredos próprios.
- **Cada andar é um pedaço de um mundo que a torre engoliu.** Há povos, ruínas e segredos lá dentro.
- **Uma cidade viva**: 20 NPCs com personalidade, rotinas de dia e noite, amizade, presentes,
  cartas e festivais. As tuas escolhas mudam a história.
- **Muito para fazer além de lutar**: pesca, quinta, cozinha, casa própria, animais de estimação,
  montadas, arena, minijogos e coleções (ver `docs/ATIVIDADES.md`).
- **4 finais** (um deles secreto), que dependem das tuas escolhas e amizades (ver `docs/HISTORIA.md`).
- **Um guardião em cada andar** e **20 bosses** com fases (ver `docs/BOSSES.md`).
- **26 povoações dentro da torre** (elfos, fungoides, homens-lagarto, sereias, alados, fantasmas…) e a
  **Cidade Errante**, que aparece num andar ao acaso todas as semanas (ver `docs/CIDADES.md`).
- **Masmorras escondidas** (uma por região) com bosses extra e armas secretas.

---

## 5. Estilo visual: 2.5D / "HD-2D"

- **Mundo em 3D** (Blender): cidade, torre, andares, casas, rochas, árvores.
- **Bonecos em 2D** (pixel art): herói, NPCs, monstros e armas são *sprites* sempre virados
  para a câmara (*billboard*).
- **Câmara fixa**, inclinada por cima, a seguir o jogador (tipo Ragnarok). Dá para fazer zoom.
- Luzes, sombras, nevoeiro e partículas 3D dão o aspeto "HD-2D" e mudam em cada bioma.

Todas as regras de tamanhos, animações e ficheiros estão em [`docs/ARTE.md`](docs/ARTE.md).

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
| Paleta de cores | **Lospec**: *Resurrect 64* | Grátis |
| Código e versões | **Git + GitHub** | Grátis |
| Builds automáticas | **GitHub Actions** | Grátis |

```
Blender  ──(.glb)──────────────►  Godot  ◄──(.png sprite sheet)──  Pixelorama / Aseprite
 cidade, torre, kits               junta tudo,                      herói, monstros, NPCs,
 de cada região                    código, câmara, luzes            armas, ícones, UI
```

---

## 7. Decisões de jogo (decidido)

| Tema | Decisão |
|---|---|
| Torre | **100 andares**, em **10 regiões de 10 andares**. Cada região tem um tema e cada andar tem o seu próprio bioma |
| Tamanho dos andares | **Grandes**: entre 150×150 m e 300×300 m, cerca de 10–20 minutos para explorar um andar |
| Bosses | **Mini-boss** nos andares 5, 15, 25… e **boss** nos andares 10, 20, 30… (20 no total) |
| Zona Segura | Cada andar tem um **acampamento** com fogueira e **teletransporte** para a cidade |
| Combate | **Tempo real** (ação), com esquiva e skills numa barra |
| Monstros | **8 por região** (80) + versões Elite + **20 monstros com nome** |
| Guardiões | **1 guardião por andar** (79 + o duelo do Kai), cada um com a sua **arma de guardião** |
| Armas | **12 tipos** × **10 materiais** + únicas, de guardião, secretas, raras, de amizade e míticas (**~258**). Ver `docs/ARMAS.md` |
| Armaduras | **Só ícone** (16×16) com stats; **não aparecem no boneco**. As armas aparecem |
| Classe | **Livre no início.** No nível 10 escolhes 1 de 4 classes; evoluem nos níveis 40 e 70 (**20 classes**, 120 skills) |
| Arte | **Tu desenhas tudo à mão**, no estilo da Aranha-Mãe de referência, e **tudo é animado** (ver `docs/ARTE.md`, secção 0) |
| NPCs | Diálogo com **retrato**, **escolhas** e **amizade** (0–10 corações). Diálogos em ficheiros de texto (PT e EN) |
| Dia e noite | **Sim**, desde a Demo. 1 dia ≈ 20 min reais, 4 estações, tempo (chuva, neve…) |
| Companheiros | Até **2** companheiros controlados pelo jogo |
| Conteúdo novo | Cada atividade entra no jogo **na região em que aparece** (coluna "Quando" em `docs/ATIVIDADES.md`) |
| Andares | Feitos **à mão** com o **kit de peças** da região; monstros, materiais e baús em posições aleatórias |
| Câmara | **Fixa** (com zoom) |
| Morrer | Acordas na estalagem e **perdes parte dos materiais** do andar (o ouro não) |
| Multijogador | **Mais tarde.** O código fica preparado para isso |
| Plataformas | **PC (Windows) e Android primeiro**, **Web** como demo com gráficos mais simples, **iOS** no fim (precisa de Mac e conta Apple paga) |

---

## 8. Mundo

### A cidade (zona segura, base do jogador)
- **Guilda de Aventureiros**: Cristal de Avaliação, missões, rank, escolher classe.
- **Ferreiro**: crafting e melhoria de armas e armaduras.
- **Alquimista**: poções a partir de ervas e materiais.
- **Mercado**: comprar e vender.
- **Estalagem**: dormir, guardar o jogo, voltar a viver depois de morrer, cozinha.
- **Entrada da torre**, no centro.
- E mais: Igreja, Biblioteca, Taberna, Quartel da Guarda e Arena, Quinta, Domador,
  Oficina do Gizmo, Costureira, Vidente, Câmara do Governador, Bairro Baixo, Rio, a tua Casa.
  Muitos destes edifícios **abrem à medida que sobes a torre** (ver `docs/CIDADES.md`).

### A torre
Lista completa dos 100 andares em [`docs/TORRE.md`](docs/TORRE.md).

| Região | Andares | Tema | Material |
|---|---|---|---|
| 1 | 1–10 | Floresta | Cobre |
| 2 | 11–20 | Cavernas e Minas | Ferro |
| 3 | 21–30 | Pântano e Selva | Aço |
| 4 | 31–40 | Deserto | Prata |
| 5 | 41–50 | Gelo | Gelo Eterno |
| 6 | 51–60 | Oceano | Coral Abissal |
| 7 | 61–70 | Vulcão | Obsidiana |
| 8 | 71–80 | Reino Assombrado | Mitril |
| 9 | 81–90 | Céu | Oricalco |
| 10 | 91–100 | Abismo / Coração da Torre | Estelar |

---

## 9. Versões (lançar aos bocados)

| Versão | Conteúdo |
|---|---|
| **Demo** | Cidade + **Região 1** (andares 1–10) + NPCs, diálogo, missões, pesca, cozinha, dia/noite. Pode ir para o itch.io |
| **Atualizações** | Cada região nova (2, 3, 4…) é uma atualização |
| **1.0** | Os **100 andares** completos e o final |

---

## 10. Etapas (por esta ordem)

### Fase A — Arte da base *(Claude faz, tu aprovas)*
1. [ ] **Herói** com todas as animações (ver `docs/ARTE.md`)
2. [ ] **Região 1 completa** (lista na secção 12 de `docs/regioes/r01_floresta.md`): kit de peças no Blender,
   8 monstros, 2 monstros com nome, 8 guardiões, Javali-Rei, Ent Ancião, Larva Ancestral, 23 armas, ícones, NPCs
3. [ ] **Cidade**: os edifícios da Demo e a base da torre no Blender
4. [ ] **NPCs da Demo** + retratos (Lyra, Gorvan, Brom, Selene, Tobias, Dona Marta, Kai, Pip, Mia)

> Enquanto desenhas, o Claude faz um **protótipo cinzento** (etapa B1) para poderes pôr a tua
> arte no jogo e ver se o tamanho, as cores e o ângulo da câmara ficam bem **antes** de
> desenhares as outras regiões.

### Fase B — Programar o jogo base *(Claude + tu)* — passos detalhados em `docs/PROGRAMACAO.md`, secção 9
1. [ ] **Protótipo cinzento**: projeto Godot, chão 3D, herói a andar, câmara a seguir
2. [ ] **Combate**: atacar com as 12 armas, esquivar, monstros com IA, dano, morrer, XP
3. [ ] **Sistema isekai**: Status, níveis, Skill Única, mensagens `[Sistema]`, skills que sobem com o uso
4. [ ] **Recolher + inventário + crafting** (ferraria, alquimia, cozinha)
5. [ ] **NPCs**: diálogo com retratos e escolhas, amizade, presentes, rotinas
6. [ ] **Dia e noite**, tempo e calendário
7. [ ] **Cidade**: edifícios, Cristal de Avaliação, missões da Guilda e dos NPCs, guardar o jogo
8. [ ] **Pesca**, bestiário, páginas de lore, títulos e conquistas
9. [ ] **Andares 1–10** montados com o kit, Zonas Seguras, segredos, puzzles, mini-boss e boss
10. [ ] **Telemóvel + builds automáticas** (PC / Android / Web)
11. [ ] **Demo lançada**

### Fase C — Subir a torre *(uma região de cada vez)*
Para cada região de 2 a 10: arte (kit, monstros, bosses, armas) → dados → montar os 10 andares →
**atividades novas dessa região** (ver `docs/ATIVIDADES.md`) → capítulo da história → atualização.

- [ ] Região 2 · [ ] Região 3 · [ ] Região 4 · [ ] Região 5 · [ ] Região 6
- [ ] Região 7 · [ ] Região 8 · [ ] Região 9 · [ ] Região 10 → **1.0**

---

## 11. Quem faz o quê

**Claude:** todo o código, a estrutura do projeto Godot, as tabelas de dados (itens, armas,
receitas, monstros, andares), **a arte** (herói, NPCs e retratos, monstros, armas, ícones, kits das
regiões em Blender por script, cidade), testes automáticos e equilíbrio, builds.

**Tu:** **aprovar a arte** (ou pedir mudanças), a música (opcional) e **jogar e dizer o que é divertido**.

**Os dois:** escrever os diálogos dos NPCs (o Claude faz o rascunho, tu dás o teu estilo).

---

## 12. Ideias para depois da 1.0

- Jogar a 2 (cooperativo)
- Armaduras visíveis no boneco
- iOS
- Mais andares no pós-jogo, para além dos Andares do Eco
