# Povoações da Região 7 — diálogos e missões

Os NPCs que vivem nos andares 61–70 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r07_vulcao.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap07_vulcao.md`.

**Gente do fogo**: os **refugiados das Cinzas** falam baixo, com humor seco, e não perguntam pelo passado. Os anões do
**Clã Brasa** gritam como o Brom (são família). Nas **Termas**, toda a gente está de férias, mesmo quem trabalha.

---

## 1. Acampamento das Cinzas (andar 61)

Primeira chegada: cena **C7-01**. Tem **tenda**, **cristal** e **loja básica**. A C7-02 (o Kai) acontece aqui.

### 1.1 Mãe Brasa — matriarca

| | |
|---|---|
| Voz | bips graves e calmos, com uma tosse de cinza de vez em quando |
| Quem é | 60 anos, era padeira na cidade que ardeu. Pôs-se à frente dos refugiados no dia do fogo "porque mais ninguém se pôs". Guarda uma caixa de sementes da cidade como se fosse ouro |
| Repete | "Bebe primeiro.", "Não se pergunta pelo que ardeu." |

| ID | Condição | Fala |
|---|---|---|
| `maebrasa_01` | — | "Bebe primeiro. Depois falas. Aqui a água vale mais do que o ouro. O ouro derrete." |
| `maebrasa_02` | — | "Fazíamos pão. A cidade inteira cheirava a pão às seis da manhã. Agora cheira a cinza. Um dia volta a cheirar a pão. Prometi às crianças." |
| `maebrasa_03` | antes de R7_01 | "Tenho sementes de lenho-brasa, a árvore que não arde. Se alguém as plantasse na floresta queimada e lhes desse água de fora… talvez." |
| `maebrasa_04` | `missao(R7_01) == concluida` | "Verde. Na floresta. Fui ver com os meus olhos. Chorei. As crianças nunca tinham visto verde. Perguntaram se era doença." |
| `maebrasa_05` | `flag(kai_voltou)` | "O rapaz dos olhos azuis esteve aqui. Bebeu água e não agradeceu. Não era mal-educado. Parecia que já não sabia como." |
| `maebrasa_06` | `boss_derrotado(tita_magma)` | "O vulcão adormeceu. Esta noite fiz pão. O primeiro em vinte anos. Saiu queimado. Comemos todos." |

### 1.2 Fuligem — órfão espertalhão

| ID | Condição | Fala |
|---|---|---|
| `fuligem_01` | abrir loja | "Mapas! Mapas verdadeiros! Desenhados por mim! Com a mão esquerda! Sou destro!" |
| `fuligem_02` | — | "Não tenho pais. Tenho a Mãe Brasa, que é mãe de toda a gente. Dá para muita gente. Às vezes não dá para mim." |
| `fuligem_03` | `missao(R7_02) == concluida` | "Encontraste um tesouro com o MEU mapa?! O mapa estava errado! Encontraste por acaso?! …Metade é minha. É a regra. Inventei agora." |

### 1.3 Curandeiro Carvão

| ID | Condição | Fala |
|---|---|---|
| `carvao_01` | — | "Queimaduras: água fria, não manteiga. Toda a gente põe manteiga. Toda a gente está errada." |
| `carvao_02` | `estado(queimadura)` | "Senta-te. Não, aí não, que está quente. Ali. Bebe isto. É Poção Fresca. Sabe a hortelã e a arrependimento." |

### 1.4 Lena Cinza — pintora

| ID | Condição | Fala |
|---|---|---|
| `lena_01` | — | "Pinto com cinza e água. É a única tinta que temos. Os quadros são todos cinzentos. Mas são bonitos. Cinzento tem cem cores, se olhares bem." |
| `lena_02` | `missao(R7_15) == concluida` | "Três quadros para a tua casa. Um da cidade como era. Um do acampamento. E um de ti. Saíste cinzent{o/a}. Toda a gente sai." |

---

## 2. Bastião de Obsidiana (andar 64) — Clã Brasa

Primeira chegada: cena **C7-03**. Tem **estalagem**, **cristal**, **loja** e a **Forja de Obsidiana** (+5% de sucesso
nas melhorias). Os anões do Clã Brasa são **família distante do Brom**.

### 2.1 Rainha-Forja Hildur Brasa

| ID | Condição | Fala |
|---|---|---|
| `hildur_01` | — | "O Clã Brasa forja desde antes de haver números. Os primeiros da janela vinham buscar armas aqui. Não pagavam. Os reis nunca pagam." |
| `hildur_02` | antes de R7_05 | "A minha coroa perdeu os rubis numa erupção. Cinco rubis e três barras de obsidiana. Uma rainha sem rubis é uma anã com um chapéu." |
| `hildur_03` | `missao(R7_05) == concluida` | "A coroa brilha outra vez. Toma o anel que fiz com o que sobrou. E toma isto: a runa da Forja Primordial. O Ragnar disse que mereces. O Ragnar nunca diz isso." |
| `hildur_04` | `flag(kai_salvo)` | "O rapaz de olhos azuis voltou a passar. Os olhos eram castanhos. Os fornos não se apagaram. Ainda bem. Gosto dos meus fornos acesos." |

### 2.2 Mestre Ragnar Brasa — tio do Brom

| | |
|---|---|
| Voz | bips enormes, ri-se como uma explosão ("HA-HA-HÁ!") |
| Quem é | 200 anos (anão), tio do Brom do lado da mãe. A barba trançada tem uma conta de rubi por cada arma lendária que forjou (doze). Grita tudo. Chora com facilidade, sobretudo a falar da família |
| Serviço | Forja de Obsidiana (depois de R7_03) · vende a **Cana Ignífuga** |

| ID | Condição | Fala |
|---|---|---|
| `ragnar_01` | — | "HA! O amigo do pequeno Brom! Ele ainda canta mal? CANTA! Os Martelo-Forte cantam todos mal. É sangue!" |
| `ragnar_02` | antes de R7_03 | "O Brom nunca me escreve. Há cento e trinta anos que não sei dele. Pensei que tinha morrido com o pai no portão." |
| `ragnar_03` | `missao(R7_03) == concluida` | *(a chorar e a rir)* "Ele está vivo! Tem uma forja! E um aprendiz que gagueja! Vou descer! Pelo cristal! Sentado! HA-HA-HÁ!" |
| `ragnar_04` | `flag(arma_10000)` | "Uma arma com o teu número, por acabar? Leva-a ao Brom. Só um Martelo-Forte acaba o que o Ferreiro começou. É uma regra. É a minha regra." |

### 2.3 Ruby Brasa — gemóloga

| ID | Condição | Fala |
|---|---|---|
| `ruby_01` | abrir loja | "Rubis, encantamentos de fogo, e uma lupa que eu não empresto. Escolhe." |
| `ruby_02` | — | "Chamo-me Ruby porque nasci com o cabelo vermelho. O meu irmão chama-se Carvão porque nasceu sujo. Os anões não têm imaginação para nomes." |

### 2.4 Ash — mineiro

| ID | Condição | Fala |
|---|---|---|
| `ash_01` | antes de R7_04 | "A escavadora grande endoideceu. Uns encapuzados meteram-lhe uma coisa dentro e agora escava sozinha. Escava pessoas, se apanhar." |
| `ash_02` | `missao(R7_04) == concluida` | "As vagonetas andam outra vez! Atalho até aos Veios Profundos! Sobe! Segura-te! Não te seguras? Problema teu!" |

---

## 3. Termas dos Géiseres (andar 66)

Estância termal de um gnomo. Tem **estalagem**, **cristal**, **loja** e **termas** (depois de R7_06).

### 3.1 Senhor Vapor — gnomo, primo do Gizmo

| ID | Condição | Fala |
|---|---|---|
| `vapor_01` | — | "Bem-vind{o/a} às Termas dos Géiseres! Toalha? Chinelos? Um ovo cozido no géiser? Tudo incluído! Menos o ovo. E os chinelos." |
| `vapor_02` | antes de R7_06 | "Os canos dos géiseres rebentaram. Sem canos não há termas. Sem termas não há clientes. Sem clientes não há… eu. O meu primo Gizmo fazia isto num dia. Eu demoro um ano. Ajudas?" |
| `vapor_03` | `missao(R7_06) == concluida` | "TERMAS ABERTAS! Entra! Sai! Entra outra vez! O calor desaparece, as dores desaparecem, as preocupações… essas ficam. Mas ficam mais leves." |
| `vapor_04` | — | "O Gizmo ainda explode coisas? Diz-lhe que a família tem orgulho. E medo. Mas orgulho." |

### 3.2 Massagista Lava

| ID | Condição | Fala |
|---|---|---|
| `lava_01` | — | "Deita-te. Relaxa. Isto vai doer um bocadinho. Depois deixa de doer. Depois dói outra vez, mas é bom." |
| `lava_02` | depois da massagem | "Os teus ombros têm nós do tamanho de rubis. Carregas muito. Pousa um bocadinho. Só aqui. Só hoje." |

### 3.3 Gil — turista perdido

| ID | Condição | Fala |
|---|---|---|
| `gil_01` | antes de R7_07 | *(com uma câmara antiga ao pescoço)* "Vim tirar fotografias aos géiseres e perdi-me. Há três meses. As fotografias estão ótimas. A volta para casa nem tanto." |
| `gil_02` | durante R7_07 | "Espera! Aquela cratera! Que luz! Só uma fotografia! …Ou duas. Os monstros podem esperar? Não podem. Corre." |
| `gil_03` | `missao(R7_07) == concluida` | "Toma a minha câmara velha. Comprei uma nova no Bastião. Aponta, carrega, e o mundo fica parado. É a única magia que eu sei fazer." |

### 3.4 Cozinheira Fumarola

| ID | Condição | Fala |
|---|---|---|
| `fumarola_01` | — | "Ovos cozidos no géiser! Três minutos de géiser e sai perfeito. Quatro minutos e sai pedra. Cinco minutos e sai voando." |
| `fumarola_02` | antes de R7_08 | "Dez ovos de Sapo-Vulcão e ensino-te o meu segredo. O segredo é: não é preciso sal. O géiser já é salgado." |

---

## 4. Missões da região, passo a passo

### R7_01 — Sementes de Esperança
| | |
|---|---|
| Quem dá | Mãe Brasa |
| Recompensa | a Floresta Queimada (63) começa a ficar verde · ❤️ (com toda a gente do acampamento) · **Lenho-Brasa** sem fim (as árvores plantadas dão madeira todos os dias) |

1. **Pedir** — `maebrasa_03`. Recebe **10 Sementes de Lenho-Brasa**.
2. **Passo 1**: encontrar o **último broto verde** dentro da árvore petrificada oca (andar 61, segredo).
3. **Passo 2**: no andar 63, plantar as 10 sementes nos sítios marcados com pedras brancas (Clareira das Brasas) e **regá-las com água de fora da região** (Cantil Infinito, água da quinta, Água de Coco…: a água da região evapora-se).
4. **Entregar** — 🎬 corte de tempo: sete dias depois, a Clareira das Brasas tem dez árvores pequenas, verdes, no meio do negro. `maebrasa_04`.

### R7_02 — Os Mapas do Fuligem
| | |
|---|---|
| Quem dá | Fuligem |
| Recompensa | um tesouro **por acaso** (baú de ouro) · título *Sortudo* |

1. **Pedir** — **Fuligem**: "Compra um mapa! Dez moedas! Leva a um tesouro! Se não levar, devolvo… cinco."
2. **Passo**: seguir o mapa (andar 61). Está tudo errado: o X está no meio de um lago de cinza. Ao chegar, uma **duna de cinza** abate e revela um baú verdadeiro, noutro sítio.
3. **Entregar** — `fuligem_03`.

### R7_03 — O Tio Ragnar
Dada pelo **Brom** (com `andar_maximo >= 64`). Falas em `docs/dialogos/brom.md`. Levar a **Carta do Brom** ao Mestre Ragnar (andar 64) → **Forja de Obsidiana** e ❤️❤️ Brom. Cena: `ragnar_03`.

### R7_04 — A Escavadora
| | |
|---|---|
| Quem dá | Ash |
| Recompensa | vagonetas do clã a funcionar (atalhos no andar 64) |

1. **Pedir** — `ash_01`.
2. **Passo**: vencer a **Escavadora Anã Possuída** (guardião do andar 64) e apanhar a **Peça Mestra** (cai dela). Dentro da peça, uma pedra com o símbolo dos cultistas (lore para o andar 69).
3. **Entregar** — `ash_02`.

### R7_05 — Rubis para a Rainha
| | |
|---|---|
| Quem dá | Rainha Hildur |
| Recompensa | **Anel de Rubi da Rainha** (+15% de dano de Fogo) · com R7_03, a **runa da masmorra** (Forja Primordial) |

1. **Pedir** — `hildur_02`.
2. **Passo**: entregar **5 Rubis** (andar 64; o desafio do andar pede o mesmo) + **3 Barras de Obsidiana**.
3. **Entregar** — `hildur_03`.

### R7_06 — As Termas
Senhor Vapor. Entregar **10 Lingote de Prata + 5 Gel Elétrico** e reparar os **3 canos** (puzzle: rodar as válvulas até a pressão das três ficar no verde) → **Termas abertas** (Calor a 0 e cura tudo durante 1 dia; 50 ouro).

### R7_07 — O Turista Perdido
| | |
|---|---|
| Quem dá | Gil |
| Recompensa | **Modo Foto** (tirar fotografias no jogo, com filtros; ver `docs/INTERFACE.md`) |

1. **Pedir** — `gil_01`, depois: "Levas-me até à ponte grande, no 67? Dizem que tem a melhor vista da torre. E uma Zona Segura com cristal. Quero ir para casa. Mas primeiro a vista."
2. **Passo**: escolta do Gil do andar 66 até à Zona Segura do andar 67. Ele **para para tirar fotografias** em 5 sítios (o jogo mostra a foto dele no canto). Se levar dano 3 vezes, senta-se e não anda até lhe dares uma Poção.
3. **Entregar** — `gil_03`. `tut_foto`: `[Sistema] Modo Foto: [foto] para abrir. Muda os filtros com [mover]. Carrega em [aceitar] para guardar.`

### R7_08 — Ovos de Géiser
Cozinheira Fumarola. **10 ovos de Sapo-Vulcão** (ninhos do andar 66; os sapos defendem-nos) → receita **Ovos de Géiser** (o Calor sobe metade durante 5 min).

### R7_09 — A Salamandrazinha
Dada pelo **Zed**. Falas em `docs/dialogos/zed.md`. No andar 62, a salamandra bebé está numa ilha de basalto que **afunda devagar** (60 s): chegar lá pelas pedras flutuantes e trazê-la → **Salamandra** (animal de estimação).

### R7_10 — Montar na Lava
Dada pelo **Zed**. No andar 66, acalmar uma **Salamandra Gigante** dando-lhe **Pimenta-Lava** (aproximar devagar, 5 pimentas, sem atacar) → **Montada Salamandra Gigante**.

### R7_11 — O Kai (história)
= **H_17**. Ver as cenas **C7-05 e C7-06** em `docs/guiao/cap07_vulcao.md` e as falas em `docs/dialogos/kai.md`.

### R7_12 — Rituais Interrompidos
Dada pela **Irmã Célia**. Falas em `docs/dialogos/celia.md`. No andar 69, interromper os **3 rituais** dos cultistas (vencer o cultista que canta no centro de cada círculo antes de a barra do ritual encher) → Água Benta ×10 · ❤️ Célia.

### R7_13 — Três Cabeças
Dada pela **Capitã Freya** (rank A; = `G_A_01`). Falas em `docs/dialogos/freya.md`. Vencer o **Tricéfalo** (andares 61, 66, 68; 3%; 20% com a missão) → Coleira de Tricéfalo · 4 000 ouro.

### R7_14 — O Número 7
Dada pelo **Gizmo**. Falas em `docs/dialogos/gizmo.md`. Vencer o **Golem Forjado Nº 7** (andares 64 e 65) e trazer o **Núcleo de Obsidiana** → **Autómato de Quinta** (rega a quinta sozinho todos os dias).
- O Gizmo reconhece o golem: assinou o projeto do Nº 7 em Engrenópolis (ver `gizmo.md`).

### R7_15 — Arte de Cinza
Lena Cinza. **20 Cinza Mágica + 5 Flor de Cinza** → **3 quadros** para a casa (`lena_02`).

---

## 5. Missões da Guilda (rank A) da região

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_A_01 Três Cabeças (R7_13) | "PROCURA-SE: Tricéfalo, cão infernal de três cabeças. Visto nos andares 61, 66 e 68. Cada cabeça morde à sua maneira." | "Três cabeças! Três vezes mais dentes! Leva três poções. Não, leva nove." | "A coleira! Do tamanho de um pneu de carroça! Vou pô-la… não vou pô-la em lado nenhum. Ainda cheira a fumo." |
