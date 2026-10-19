# Povoações da Região 8 — diálogos e missões

Os NPCs que vivem nos andares 71–80 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r08_reino_assombrado.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap08_reino_assombrado.md`.

**Os fantasmas cidadãos** (Mercado Fantasma) **não sabem que morreram**: falam como se fosse um dia normal de há
muito tempo, repetem rotinas, ficam confusos quando algo não bate certo. Nunca se lhes diz a verdade (o jogo não deixa);
algumas missões deixam-nos **seguir em frente** sozinhos. Bips: abafados, com um eco de caixa de música.
**A Ordem da Luz** fala com calma e firmeza; humor seco de quem já viu muitos mortos levantarem-se.

---

## 1. Mercado Fantasma (andar 72) — só à noite

Primeira noite: cena **C8-02**. Das 21:00 às 4:00 (depois da R8_02, também de dia). Tem **hotel fantasma** (dormir
dá **sonhos** com lore: ver secção 1.6) e **lojas** (ouro ou **Lágrimas de Fantasma**).

### 1.1 Burgomestre Aldous

| | |
|---|---|
| Voz | bips solenes e redondos; pigarreia antes de cada frase importante |
| Quem é | presidente da câmara da cidade, fantasma de bigode enorme e faixa ao peito. Preocupa-se com o relógio parado, com o lixo das ruas e com "estes forasteiros novos que aparecem e desaparecem" |

| ID | Condição | Fala |
|---|---|---|
| `aldous_01` | — | "Hm-hm. Bem-vindo ao mercado. O mercado mais antigo do reino. Tem… tem a idade do reino. Que idade tem o reino? Ah. Muita." |
| `aldous_02` | antes de R8_02 | "O relógio da torre parou às doze. Os relojoeiros não o conseguem arranjar. Os relojoeiros… onde estão os relojoeiros? Hm." |
| `aldous_03` | — | "Às vezes acordo e tenho a sensação de que ontem foi igual a hoje. E anteontem também. Deve ser a idade." |
| `aldous_04` | `missao(R8_02) == concluida` | *(muito transparente, a sorrir)* "O relógio anda! Tique, taque! Vai ser amanhã! Há tanto tempo que não havia amanhã!" |
| `aldous_05` | `boss_derrotado(rei_sem_coroa)` | "Dizem que o rei… descansou? Que estranho. Sinto-me mais leve. Sinto-me… a ir. Boa noite, forasteiro. Boa noite." |

### 1.2 Mortimer — lojista

| ID | Condição | Fala |
|---|---|---|
| `mortimer_01` | abrir loja | "Coisas antigas para gente moderna! Ou coisas modernas para gente antiga. Já não me lembro do letreiro." |
| `mortimer_02` | antes de R8_15 | "Tenho uma carta para entregar. Da menina Rosalinda para o cavaleiro Gaspar. Há… há algum tempo. Ele está no castelo. Eu não posso ir ao castelo. Não sei porquê." |
| `mortimer_03` | `missao(R8_15) == concluida` | "Encontraram-se? Que bom. Que bom. A loja ficou mais vazia. Ficou mais leve." |

### 1.3 Elise — menina fantasma

| ID | Condição | Fala |
|---|---|---|
| `elise_01` | antes de R8_03 | "Perdi a Matilde. A minha boneca. Fui ao cemitério ver a avó e deixei-a lá. A mãe diz que não posso ir sozinha ao cemitério. Vais tu?" |
| `elise_02` | antes de R8_03 | "O meu gato é cinzento e às vezes vê-se através dele. Chama-se Fumo. Os gatos são assim." |
| `elise_03` | `missao(R8_03) == concluida` | *(com a boneca, a brilhar)* "A Matilde! Agora posso ir ter com a avó. A avó está à espera. Fica com o Fumo, está bem? Ele gosta de ti. Dá-lhe leite. Ele não bebe, mas gosta." |

### 1.4 Hugo — padeiro

| ID | Condição | Fala |
|---|---|---|
| `hugo_01` | — | "Pão quente! Saído do forno! O forno está frio, mas o pão está quente! Não perguntes. Come." |
| `hugo_02` | antes de R8_04 | "Queres a receita do pão fantasma? Cinco de farinha e três de… daquilo verde. Ectoplasma. Os forasteiros chamam-lhe assim. Eu chamo-lhe fermento." |

### 1.5 Fantasmas cidadãos (sem nome)

| ID | Quem | Fala |
|---|---|---|
| `fantasma_senhora_01` | senhora de chapéu | "Boa noite! Que tempo, não é? Sempre igual. Sempre bonito. Sempre meia-noite." |
| `fantasma_crianca_01` | criança | "Jogas à apanhada? Eu atravesso as paredes. É batota? Não é batota. É jeito." |
| `fantasma_guarda_01` | guarda da cidade | "Alto! Quem vem lá? …Ah, um forasteiro. Passe. O rei mandou fechar os portões. Para nossa proteção. O rei é sábio." |
| `fantasma_casal_01` | casal a passear | "Casámos ontem. Ou anteontem. Os dias parecem todos o mesmo dia. Mas é um dia bom." |

### 1.6 Sonhos do hotel fantasma (dormir no hotel; 1 sonho por noite, pela ordem)

| Nº | O sonho (o ecrã fica a sépia; sem falas) |
|---|---|
| 1 | O reino de dia, cheio de cor, com o rei a rir numa varanda e a rainha a plantar rosas. |
| 2 | O rei a mandar fechar os portões. Do lado de fora, figuras com janelas azuis por cima da cabeça, a bater. |
| 3 | Uma cela com Jogadores lá dentro. O rei a trazer-lhes pão com as próprias mãos. |
| 4 | O céu a rachar como vidro. A torre a engolir o reino, devagar, de baixo para cima. A rainha a correr para o jardim. |
| 5 | A meia-noite a bater no relógio da torre. Os ponteiros param. Toda a gente fica parada a meio do que fazia. |

---

## 2. Mosteiro da Ordem da Luz (andar 77)

Primeira chegada: cena **C8-06**. Tem **celas** (dormir), **cristal**, **loja** e **forja de Mitril** (purificação).
É o mosteiro onde a **Irmã Célia** nasceu e aprendeu.

### 2.1 Abadessa Lumina

| | |
|---|---|
| Voz | bips baixos e lentos; uma pausa antes de cada frase, como quem escolhe as palavras |
| Quem é | 75 anos, líder da Ordem. Caçadora de mortos-vivos durante 40 anos (uma cicatriz de garra no queixo). Encontrou a Célia num cesto à porta do mosteiro. Teimosa, seca, com um humor que só aparece de vez em quando |

| ID | Condição | Fala |
|---|---|---|
| `lumina_01` | — | "A luz não mata os mortos. Lembra-lhes que já morreram. Isso basta." |
| `lumina_02` | — | "Rezamos de manhã, curamos à tarde e lutamos à noite. Por essa ordem. A Célia aprendeu ao contrário. Saiu-lhe bem na mesma." |
| `lumina_03` | antes de R8_01 | "No cemitério real, as sepulturas não deixam os mortos descansar. Consagra-as. Dez. Toma a água benta. Não a bebas. Já houve quem bebesse." |
| `lumina_04` | `missao(R8_14) == concluida` | "Os sinos tocaram certos. A luz entrou na catedral inteira. Há setenta anos que eu não via aquilo. Obrigada." |
| `lumina_05` | `boss_derrotado(rei_sem_coroa)` | "O rei descansou. Era um homem com medo. O medo faz reis maus e homens tristes. Ele era as duas coisas." |

**A carta da Célia** (N_CELIA_3, com a **Carta da Célia** no inventário)
- 🎬 A Abadessa reconhece a letra no envelope antes de o abrir. Senta-se num banco do claustro. Lê devagar.
- **Lumina** *(normal)*: "Vinte anos. Vinte anos e escreve 'desculpe a demora'." 🎬 pausa. *(feliz, raro)* "Teimosa."
- **Lumina** *(normal)*: "Eu soube no dia em que desceu. Os sinos tocaram sozinhos. Esperei que me escrevesse primeiro. Ela esperou o mesmo. Duas teimosas."
- 🎬 Escreve uma resposta curta, dobra-a, entrega-a ao herói.
- **Lumina** *(normal)*: "Leva-lhe isto. E diz-lhe que come pouco. Sei que come pouco. Sempre comeu pouco."
- ⚙ Recebe a **Resposta da Abadessa** (levar à Célia: `docs/dialogos/celia.md`, N_CELIA_3).

### 2.2 Irmão Bento — ferreiro abençoado

| ID | Condição | Fala |
|---|---|---|
| `bento_01` | abrir loja | "Mitril. O metal mais leve e mais forte. Aqui vem amaldiçoado. Eu tiro-lhe a maldição com água benta e paciência. Muita paciência." |
| `bento_02` | antes de R8_12 | "Traz-me mitril cru e água benta. Eu purifico. Fazemos-te um anel. Os anéis de mitril não pesam nada. Os pecados sim." |

### 2.3 Irmã Clara — vitralista

| ID | Condição | Fala |
|---|---|---|
| `clara_01` | antes de R8_06 | "Os vitrais da catedral partiram-se quando a torre engoliu o reino. Faço vidro novo, de cor. Preciso de seis peças. A luz entra melhor pelas cores." |
| `clara_02` | `missao(R8_06) == concluida` | "Olha. A nave inteira cheia de cor. Os mortos não entram. Os vivos não querem sair." |

### 2.4 Caçador Van

| | |
|---|---|
| Quem é | 50 anos, caçador de vampiros, chapéu de abas largas, bigode, uma besta de prata às costas. Fala por provérbios de caçador e desconfia de toda a gente pálida ("Tu és pálid{o/a}? Não? Ótimo.") |

| ID | Condição | Fala |
|---|---|---|
| `van_01` | — | "Regra um: os vampiros dormem de dia. Regra dois: os caixões não se abrem sozinhos. Regra três: se se abrirem, corre." |
| `van_02` | antes de R8_07 | "Três caixões escondidos na cidade e no castelo. De dia, um golpe chega. De noite, nem cem." |
| `van_03` | `missao(R8_08) == concluida` | "A Condessa. Andei atrás dela trinta anos. Venceste-a numa noite. Vou reformar-me. Não vou. Mas vou pensar nisso." |

---

## 3. Missões da região, passo a passo

### R8_01 — Consagrar
| | |
|---|---|
| Quem dá | Abadessa Lumina |
| Recompensa | Água Benta ×20 · receita **Água Benta** · abre a **Cripta da Rainha** (masmorra) à meia-noite |

1. **Pedir** — `lumina_03`.
2. **Passo**: no andar 73, consagrar **10 sepulturas** ([interagir] com Água Benta). Os corvos que te virem crocitam e acordam os mortos da zona.
3. **Entregar** — **Lumina**: "Dez. Os mortos do cemitério dormem. Os reis também. Leva a receita. A água benta faz-se com sálvia e com fé. A sálvia vende-se no claustro. A fé não."

### R8_02 — O Relógio Parado
| | |
|---|---|
| Quem dá | Burgomestre Aldous |
| Recompensa | os fantasmas podem **seguir em frente** (cena) · o Mercado Fantasma passa a abrir também **de dia** |

1. **Pedir** — `aldous_02`.
2. **Passo 1**: entregar **10 Engrenagens + 5 Lingote de Mitril** (purificado).
3. **Passo 2**: subir à **Torre do Relógio** e pôr as engrenagens no sítio (puzzle: 5 rodas de tamanhos diferentes têm de rodar todas; ver o mapa).
4. **Entregar** — 🎬 meia-noite. O relógio bate as doze. E depois, pela primeira vez, **a uma**. Os fantasmas da praça param, olham para cima, sorriem. Alguns ficam mais transparentes e desaparecem devagar, um a um, como velas a apagar. Outros ficam (os que ainda têm coisas por fazer).
   - `aldous_04`.

### R8_03 — A Boneca da Elise
| | |
|---|---|
| Quem dá | Elise |
| Recompensa | **Gato Fantasma** (animal de estimação) |

1. **Pedir** — `elise_01`.
2. **Passo**: no andar 73, a boneca **Matilde** está em cima da campa da avó da Elise (a campa tem uma boneca desenhada na pedra), nos Mausoléus. Só aparece **depois** de consagrares essa campa.
3. **Entregar** — `elise_03`. 🎬 A Elise sobe devagar, a abraçar a boneca, e desaparece. O gato fica a olhar para cima. Depois esfrega-se nas pernas do herói. `tut_animal`.

### R8_04 — Pão Fantasma
Hugo. **5 Farinha + 3 Ectoplasma** → receita **Pão Fantasma** (durante 10 s atravessas paredes finas).

### R8_05 — O Passado de Gorvan (história)
= **H_19**. Ver as cenas **C8-03 e C8-04** em `docs/guiao/cap08_reino_assombrado.md`.

### R8_06 — Vitrais
Irmã Clara. **6 Vidro Colorido** (alquimia: Vidro Solar + 1 gema de cada cor) → a catedral inteira fica **zona de luz** (`clara_02`).

### R8_07 — Caça ao Vampiro
| | |
|---|---|
| Quem dá | Caçador Van |
| Recompensa | **Besta de Mitril Abençoada** (Épica, Luz) |

1. **Pedir** — `van_02`.
2. **Passo**: **de dia**, encontrar os **3 caixões** (Cidade Fantasma: numa cave; Masmorras do Castelo: no Poço; Jardins Mortos: na Estufa Partida) e abri-los. De dia, o vampiro lá dentro morre de um golpe. De noite, os caixões estão vazios e os vampiros andam à solta.
3. **Entregar** — **Van**: "Três! Toma a minha segunda besta. A primeira não dou. Tem nome. Chama-se Clementina."

### R8_08 — A Condessa
Caçador Van (rank A; = `G_A_02`). Vencer a **Condessa Sangria** (andares 72, 76, 78, à noite; 4%; 30% com a missão; 100% num Eclipse Lunar) → Leque da Condessa · Rosa de Sangue. `van_03`.
- **Condessa** *(ao aparecer, a abanar o leque)*: "Um convidado! E eu sem vestido novo. Tanto faz. Dança comigo. É a última dança. Para um de nós."

### R8_09 — O Jardineiro
Dada pela **Hana**. Falas em `docs/dialogos/hana.md`. Vencer **O Jardineiro** (andar 76, ao entardecer: esconder-te nas sebes e atacá-lo pelas costas) e trazer as **sementes** que ele guardava num saco à cintura → Sementes de Rosa Negra · Chapéu de Palha do Jardineiro.
- **O Jardineiro** *(a rir, a cortar sebes)*: "Ervas daninhas! Ervas daninhas por todo o lado! Ah… não. És tu. Também serves."

### R8_10 — Livros Perdidos
Dada pelo **Velho Fausto**. Falas em `docs/dialogos/fausto.md`. Trazer **5 livros** do Arquivo Selado (andar 75; cena C8-05). Os livros estão nas estantes altas: mover as escadas de rodas sem fazer barulho (correr acorda os livros) → página especial "O Reino Antes da Torre" · ❤️❤️ Fausto.

### R8_11 — Os Prisioneiros
| | |
|---|---|
| Quem dá | Abadessa Lumina |
| Recompensa | os 4 prisioneiros vivos vão para Ascendia (um é cozinheiro: 5 receitas novas na Estalagem) |

1. **Pedir** — **Lumina**: "Nas masmorras do castelo há gente viva. Presa há tanto tempo que já não sabe se é dia. Tira-os de lá."
2. **Passos**: no andar 78, juntar as **3 partes da chave mestra** (cada uma com um guarda que patrulha: furtividade ou luta) e abrir as 4 celas com gente viva:
   - **Teresa** — cozinheira de uma vila engolida há 40 anos ("Há quarenta anos que cozinho ratos. Sei cozinhar ratos de doze maneiras."). Vai trabalhar com a Dona Marta.
   - **Gualter** — ferreiro velho. Vai para a forja do Brom (os dois discutem o dia todo; ficam amigos).
   - **Íngrid e Mateus** — dois irmãos de 10 e 12 anos, nascidos na cela. Nunca viram o sol. Vão para a Igreja da Célia.
3. **Entregar** — 🎬 em Ascendia, os irmãos veem o sol pela primeira vez na Praça. Ficam parados, de olhos fechados, com a cara para cima. A Mia vai logo ter com eles e mostra-lhes o rio.

### R8_12 — Mitril Puro
Irmão Bento. **10 Minério de Mitril + 5 Água Benta** → o Bento passa a purificar o teu Mitril · **Anel de Mitril** (+10% RES).

### R8_13 — O Banquete
| | |
|---|---|
| Quem dá | (os fantasmas do andar 79) |
| Recompensa | título *Convidado dos Mortos* · Cálice de Prata (decoração) · na luta do Rei Sem Coroa, os cavaleiros lutam ao teu lado (fase 3) |

1. **Começa** ao entrares no Salão de Banquetes: há uma cadeira vazia à mesa, com o teu nome escrito num cartão.
2. **Passo**: sentar ([interagir]) e **ouvir o brinde até ao fim** (não te levantes; 2 minutos de jogo; se te levantares, recomeça).
   - **Comandante (fantasma, de copo no ar)**: "Ao rei, que nos fechou as portas para nos salvar. À rainha, que plantava rosas. Aos que estão lá fora e não puderam entrar. E aos que ainda vão subir." 🎬 todos bebem. "Que a torre os deixe chegar."
3. **No fim** — os cavaleiros levantam-se e fazem continência ao herói.

### R8_14 — Os Sinos da Catedral
Abadessa Lumina. Tocar os **3 sinos** da torre da catedral (andar 77) pela ordem dos tamanhos, do maior para o menor → **Bênção da Luz** (+10% de dano de Luz para sempre) · `lumina_04`.

### R8_15 — Cartas de Amor
| | |
|---|---|
| Quem dá | Mortimer |
| Recompensa | **Anel de Noivado Fantasma** (presente) · os dois seguem em frente |

1. **Pedir** — `mortimer_02`.
2. **Passos**: levar a carta da **Rosalinda** (fantasma do andar 72, à janela de uma casa da Rua Principal) ao **cavaleiro Gaspar** (fantasma do andar 79, de guarda à porta do Arsenal) e trazer a resposta. Três viagens (3 cartas de cada um).
   - **Gaspar** *(a ler a 3.ª carta)*: "Ela diz que me espera na fonte. Na fonte da praça. Ao meio-dia. …Há quanto tempo é que ela espera?"
3. **Entregar** — 🎬 com o relógio a funcionar (R8_02), ao meio-dia, na fonte da praça do andar 72: o Gaspar aparece. A Rosalinda desce. Dão as mãos. Desaparecem os dois. Na borda da fonte fica um anel.

### Estandarte de Alvorada (andar 76, opcional)
Com a flag `elva_alvorada` (cena de 8 ❤️ da Elva), aparece no **Labirinto de Sebes** um estandarte rasgado com um sol a
nascer, preso numa sebe. Trazê-lo à **Elva** (ver `docs/dialogos/elva.md`, N_ELVA_3). O Reino Assombrado **não** é Alvorada.

---

## 4. Missões da Guilda (rank A) da região

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_A_02 A Condessa (R8_08) | "PROCURA-SE: Condessa Sangria. Vampira. Vestido vermelho, leque preto. Ataca à noite nos andares 72, 76 e 78." | "Uma vampira! Leva alho. Não, isso é mentira. Leva luz. E não a deixes olhar-te nos olhos. A sério." | "O leque dela! É lindo. É horrível. É lindo. Vou guardá-lo numa gaveta e nunca mais abrir a gaveta." |
