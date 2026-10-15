# Povoações da Região 9 — diálogos e missões

Os NPCs que vivem nos andares 81–90 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r09_ceu.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap09_ceu.md`.

**Os Alados** nasceram no céu da torre e nunca pisaram chão firme ("Chão é o que cai"). Falam leve, riem-se de quem
tem medo das alturas e acham estranhíssimo andar a pé. **Os astrónomos** falam baixo, por números e por estrelas.
Bips: os Alados, agudos e aos saltinhos; os astrónomos, lentos e redondos.

---

## 1. Aerópolis (andar 82)

Primeira chegada: cena **C9-02**. Tem **estalagem**, **cristal**, **forja de Oricalco**, **loja** e **porto de balões**.

### 1.1 Imperatriz Celestia

| | |
|---|---|
| Voz | bips claros e altos, sempre calmos |
| Quem é | governante dos Alados, asas brancas enormes, coroa de penas. Viu muitos da janela passar. Acha que são mais felizes os que ficam a aprender a planar. Não os impede de subir: diz-lhes a verdade e deixa-os escolher |

| ID | Condição | Fala |
|---|---|---|
| `celestia_01` | — | "Aqui não há chão. Há ilhas. Há pontes. Há o céu entre elas. Se caíres, as nuvens apanham-te. Se não caíres, também ficas bem." |
| `celestia_02` | — | "Os meus avós contavam de um rapaz que passou aqui sozinho, há muito, muito tempo. Não ficou. Dizem que, ao partir, chorou a olhar para baixo." |
| `celestia_03` | antes de R9_12 | "A Tempestade Viva voltou ao 87. Come balões. Come Alados. Ninguém lhe chega ao olho. Tu talvez." |
| `celestia_04` | `missao(R9_03) == concluida` | "A pequena Pena voa. Todos os Alados viram. Não havia uma criança em Aerópolis que não voasse há cem anos. Obrigada." |
| `celestia_05` | `flag(sabe_sucessor)` | "Então é isso que está lá em cima. Um rei cansado. Quando lá chegares, diz-lhe que cá em baixo, nas nuvens, há sempre lugar para quem quiser aprender a planar. Até para ele." |

### 1.2 Zéfiro — mestre de voo

| ID | Condição | Fala |
|---|---|---|
| `zefiro_01` | antes de R9_01 | "Planar é cair devagar e com estilo. O devagar ensino eu. O estilo vem com os anos. Ou não vem. Já vi Alados sem estilo nenhum." |
| `zefiro_02` | durante R9_01 | "Segura o salto! Segura! Mais! Isso! Estás a planar! Estás a… estás a cair. Também conta." |
| `zefiro_03` | `missao(R9_01) == concluida` | "Toma a capa. Não é uma asa. É uma promessa de asa. Usa-a bem. E nunca planes em calmaria: sem vento, uma capa é só um lençol." |

### 1.3 Nimbo — balonista

| ID | Condição | Fala |
|---|---|---|
| `nimbo_01` | antes de R9_02 | "Três balões rotos. Fio de nuvem para a lona, madeira-nuvem para os cestos. Dez e dez de cada. Os Alados não precisam de balões. Os que não voam sim. Como tu." |
| `nimbo_02` | `missao(R9_02) == concluida` | "Sobe! Para onde? Para qualquer ilha dos andares 81 a 89. Não para cima do 90. Os balões têm medo. Eu também." |

### 1.4 Brisa — mercadora

| ID | Condição | Fala |
|---|---|---|
| `brisa_01` | abrir loja | "Penas, frutos, sementes, sementes de frutos, frutos de sementes. Tudo do céu. Nada do chão. O chão é sujo." |
| `brisa_02` | — | "Um Pêssego Celeste por dia e nunca mais tens medo das alturas. É mentira. Mas são muito bons." |

### 1.5 Cúmulo — escultor de nuvens

| ID | Condição | Fala |
|---|---|---|
| `cumulo_01` | — | "Esculpo nuvens. Duram uma semana. Depois choram e vão-se. A arte é assim: bonita e breve." |
| `cumulo_02` | `missao(R9_13) == concluida` | "Três esculturas para a tua casa. Fiz-lhes um feitiço de ar: não choram. Duram para sempre. A arte também pode ser assim." |

### 1.6 Pena — criança alada que não voa

| | |
|---|---|
| Quem é | 9 anos, asas pequenas e fracas. É a única criança de Aerópolis que não voa. Corre pelas pontes a bater as asas com toda a força. Nunca desiste |

| ID | Condição | Fala |
|---|---|---|
| `pena_01` | antes de R9_03 | "Não voo. Ainda. Os outros dizem que as minhas asas são pequenas. São do tamanho certo para mim. O vento é que não sabe." |
| `pena_02` | antes de R9_03 | "O avô dizia que há cinco penas do vento escondidas no céu. Quem as tiver, o vento obedece. Vais procurar? Eu vou contigo! Não posso. Não voo. Vais tu." |
| `pena_03` | `missao(R9_03) == concluida` | *(a voar à volta do herói, aos gritos)* "ESTOU A VOAR! ESTOU A VOAR! Não sei parar! Como se para?!" |

---

## 2. Observatório Celeste (andar 86)

Primeira chegada: cena **C9-04** (o telescópio grande). Tem **cama**, **cristal** e **loja** (lentes, mapas). Foi a casa
da **Madame Oriel**, antes de descer.

### 2.1 Astrónoma Vega

| | |
|---|---|
| Voz | bips secos e rápidos; resmunga |
| Quem é | 65 anos, cabelo grisalho apanhado com lápis. Amiga e colega da Oriel durante vinte anos. Quando a Oriel desceu, ficou zangada com ela (e com ela própria, por não ter tido coragem). Guarda o telescópio pequeno da Oriel… não: a Oriel é que guarda o dela |

| ID | Condição | Fala |
|---|---|---|
| `vega_01` | — | "Não toques no telescópio. Se tocares, toca com cuidado. Se partires, vais morar para o 81. Lá fora. Numa nuvem." |
| `vega_02` | — | "As estrelas não se contam. Contam-se, mas nunca acabam. Por isso conto. É o meu passatempo e o meu castigo." |
| `vega_03` | antes de R9_06 | "As estátuas do anfiteatro apontavam para as constelações. Alguém as rodou. Põe-nas a apontar certo. Cinco. O céu fica mais arrumado." |
| `vega_04` | `missao(R9_06) == concluida` | "Toma um telescópio pequeno para a tua casa. À noite mostra onde está o Mercador Errante. Ele também é uma estrela. Uma estrela que vende coisas." |
| `vega_05` | `missao(R9_08) == concluida` | "Respondi à Oriel. Três linhas. Ela vai chorar. Eu chorei ao escrever. Não lhe digas." |

**A carta da Oriel** (R9_08, com a **Carta da Oriel** no inventário)
- 🎬 A Vega pega na carta. Reconhece a letra redonda da Oriel e fica muito quieta.
- **Vega** *(zangada)*: "Trinta anos. Trinta anos e manda uma carta por um estranho." 🎬 lê. *(triste)* "…Ela pede desculpa por ter descido sem mim."
- **Vega** *(normal)*: "Eu também vi o número. Naquela noite. Dez mil. Vi-o e tive medo e calei-me. Ela viu-o e teve medo e desceu para te esperar."
- **Vega** *(triste)*: "Ela foi a corajosa. Eu fui a que ficou a ter razão sozinha. Não é a mesma coisa."
- 🎬 Escreve três linhas, dobra-as, embrulha-as num baralho de cartas de prata.
- **Vega** *(normal)*: "Leva-lhe isto. O Baralho Celeste. Era da mãe dela. Fiquei com ele quando desceu. Para ter a certeza de que um dia ela mo vinha pedir."
- ⚙ Recebe a **Resposta da Vega** e o **Baralho Celeste** (levar à Oriel: `docs/dialogos/oriel.md`, R9_08).

### 2.2 Orion — assistente

| ID | Condição | Fala |
|---|---|---|
| `orion_01` | — | "Faço telescópios. E para-raios. E chá. A Vega diz que o meu chá é o pior do céu. Bebe dois por dia." |
| `orion_02` | antes de R9_10 | "No 87 há uma tempestade que nunca para. Se lá pusermos para-raios de cobre, os raios vão para onde nós quisermos. Os raios gostam de cobre. Toda a gente gosta de alguma coisa." |
| `orion_03` | `missao(R9_10) == concluida` | "Quatro para-raios! A tempestade continua zangada, mas agora zanga-se com os para-raios e não contigo. É o melhor que se consegue com tempestades." |

### 2.3 Velho Altair — o astrónomo cego

| ID | Condição | Fala |
|---|---|---|
| `altair_01` | — | "Fiquei cego a olhar para o sol. Agora ouço as estrelas. Fazem um zumbido. Cada uma o seu. Como abelhas a contar histórias." |
| `altair_02` | antes de R9_15 | "Esta noite vai cair uma. Uma estrela cadente. Ouço-a a despedir-se. Apanha-a para mim. Quero ouvi-la de perto, antes que se cale." |
| `altair_03` | `missao(R9_15) == concluida` | *(com a estrela nas mãos, de olhos fechados)* "Ouves? Não ouves. Eu ouço. É um mundo inteiro. Pequenino. À espera. Cada estrela é um mundo à espera." |

---

## 3. Outros

### 3.1 Monges do Templo dos Ventos (andar 88)

| ID | Condição | Fala |
|---|---|---|
| `monge_vento_01` | — | "O vento é a respiração dos Administradores antigos. Quando sopra forte, estão zangados. Quando para, estão a ouvir." |
| `monge_vento_02` | antes de R9_14 | "Os seis moinhos estão virados ao contrário. O vento anda às voltas e o templo não descansa. Roda-os. Pela ordem das bandeiras." |
| `monge_vento_03` | `missao(R9_14) == concluida` | "O vento passa direito. O templo respira. Toma: um sino de vento. Pendura-o à janela. Quando tocar sozinho, é alguém lá de cima a respirar contigo." |

---

## 4. Missões da região, passo a passo

### R9_01 — Aprender a Planar
| | |
|---|---|
| Quem dá | Zéfiro |
| Recompensa | **Capa Planadora** (`tut_planar`) |

1. **Pedir** — `zefiro_01`.
2. **Passo**: 3 percursos de voo no campo dos aros de Aerópolis: saltar das plataformas e passar por todos os aros de cada um a planar (segurar [esquivar] no ar).
   - **Percurso 1**: 5 aros em linha reta, a descer.
   - **Percurso 2**: 6 aros com curvas (inclinar com [mover]).
   - **Percurso 3**: 8 aros com uma corrente de ar a meio (sobe-se com ela).
3. **Entregar** — `zefiro_03`.

### R9_02 — Os Balões
Nimbo. **10 Fio de Nuvem + 10 Madeira-Nuvem por balão** (3 balões) → **viagem de balão** entre as ilhas e os andares 81–89 (`nimbo_02`).

### R9_03 — A Pena que Não Voa
| | |
|---|---|
| Quem dá | Pena |
| Recompensa | a Pena voa · ❤️ Celestia · **Pena Dourada** (acessório: +10% planar) |

1. **Pedir** — `pena_02`.
2. **Passo 1**: encontrar as **5 Penas do Vento** (andares 81, 83, 84, 86 e 88: cada uma num sítio alto, só alcançável a planar).
3. **Passo 2**: levar a Pena ao campo dos aros e fazer o percurso 1 **com ela** (ela segue-te a planar; se cair, recomeça). As penas do vento vão-se colando às asas dela à medida que passa nos aros.
4. **Entregar** — 🎬 no último aro, as asas da Pena brilham e ela sobe sozinha, alto, por cima das cúpulas. `pena_03`. Toda a Aerópolis sai à rua.

### R9_04 — O Ovo Abandonado
Dada pelo **Zed**. Falas em `docs/dialogos/zed.md`. No andar 85, o ovo de grifo caído **fora** do ninho: levá-lo até ao cristal e a Ascendia **sem tocar em nenhum ovo dos ninhos** (os grifos atacam) → **Grifo Bebé**.

### R9_05 — Domar o Grifo
Dada pelo **Zed** (depois do andar 85). **20 Carne + 5 Pêssego Celeste** para o grifo selvagem do andar 85, e montá-lo 3 vezes sem cair (minijogo como o do laço do Lagarto da Areia, mas no ar) → **Montada Grifo**.

### R9_06 — Constelações
Astrónoma Vega. Rodar as **5 estátuas** do andar 86 para apontarem às 5 constelações (as constelações veem-se no teto do Observatório) → **Telescópio** para a casa (`vega_04`).

### R9_07 — A Verdade do Serafim (história)
= **H_21**. Ver as cenas **C9-06 e C9-07** em `docs/guiao/cap09_ceu.md`.

### R9_08 — A Carta da Oriel
Dada pela **Madame Oriel** (6 ❤️). Levar a **Carta da Oriel** à Vega (secção 2.1) e trazer a **Resposta da Vega** e o **Baralho Celeste**.

### R9_09 — Pêssegos Celestes
Dada pela **Dona Marta**. Falas em `docs/dialogos/marta.md`. **10 Pêssegos Celestes** → receita **Tarte Celeste** (+5% XP durante 1 dia).

### R9_10 — Para-raios
Orion. Instalar **4 para-raios** no andar 87 (**20 Lingote de Cobre**: o cobre conduz) nas 4 ilhas marcadas → zona segura maior no 87 · **Anel Para-raios** (imune a Choque) · `orion_03`.

### R9_11 — O Duelo de Sigrun
| | |
|---|---|
| Quem dá | Capitã Freya (rank S; = `G_S_01`) |
| Recompensa | **Asas de Sigrun** (cosmético que melhora o planar) · **Lança Relâmpago** |

1. **Pedir** — falas em `docs/dialogos/freya.md`.
2. **Passo**: encontrar a **Valquíria Sigrun** (andares 84, 88, 89; 3%; 30% com a missão) e aceitar o **duelo justo**: sem atacar pelas costas, sem companheiros, sem deixar outros monstros ajudar (se acontecer, ela fica furiosa: +50% ATQ).
   - **Sigrun** *(normal)*: "Um duelo. De frente. Como se fazia antes de haver janelas. Aceitas?"
   - *(se ganhares de forma justa)* **Sigrun** *(feliz)*: "Bem lutado. A Capitã que te mandou… diz-lhe que a Sigrun se lembra dela. Do 62. Ela sabe."
3. **Entregar** — à Freya.

### R9_12 — A Tempestade Viva
Imperatriz Celestia. Vencer a **Tempestade Viva** (andar 87, 5%; 50% com a missão): só se lhe acerta no **olho** do centro, que se abre de 20 em 20 s → **Olho da Tempestade** · 8 000 ouro.

### R9_13 — Esculturas de Nuvem
Cúmulo. **10 Fio de Nuvem + 5 Essência de Ar** → **3 esculturas de nuvem** para a casa (flutuam).

### R9_14 — Os Moinhos
Monges do Templo dos Ventos (andar 88). Rodar os **6 moinhos** pela ordem das bandeiras de oração (cores: branca, azul, verde, amarela, vermelha, negra) → o Templo fica calmo (atalhos) · **Sino de Vento** (decoração) · `monge_vento_03`.

### R9_15 — A Estrela Cadente
Velho Altair. Apanhar uma **Estrela Cadente** (cai à noite nos andares 81 e 86; durante a Chuva de Estrelas há muitas) → lore e **Pó de Estrela ×5** (joalharia lendária) · `altair_03`.

---

## 5. Missões da Guilda (rank S) da região

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_S_01 O Duelo de Sigrun (R9_11) | "A Valquíria Sigrun desafia aventureiros para duelos justos nos andares 84, 88 e 89. Quem a vencer, honra a Guilda." | "Uma valquíria! Com asas douradas! Lutas de frente, está bem? Ela não gosta de batota. Eu também não. A Freya também não. Ninguém gosta, na verdade." | "Ela mandou cumprimentos à Capitã! A Capitã leu e saiu. Foi para a muralha. Acho que estava a sorrir. Não tenho a certeza. Nunca a vi sorrir." |
