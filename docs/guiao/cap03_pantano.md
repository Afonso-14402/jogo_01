# Guião — Capítulo 3: Pântano e Selva (andares 21–30)

Missões: **H_08 🔀 Ordem da Guilda** (= R3_02), **H_09 A Que Não Morre**. Povoações e missões secundárias:
`docs/dialogos/povoacoes_r03.md`. Mapas: `docs/mapas/r03_pantano.md`.

**O que este capítulo conta**: a **primeira grande escolha**. A Guilda manda expulsar os Homens-Lagarto; o chefe deles
pede ajuda contra os renegados. Ninguém está totalmente certo. O Kai mostra pela primeira vez que faz **qualquer coisa**
para subir mais depressa — uma pista do que vai fazer no capítulo 7.

**Flags desta escolha**: `sssar_defendida` (B) ou `sssar_expulsa` (A). Conta para o **final secreto** (precisa de B).

---

## C3-01 — O Calor

| | |
|---|---|
| ID | `cena_c3_01_pantano` |
| Quando | entrar pela primeira vez no andar 21 |
| Onde | andar 21, Passadiços de Madeira |
| Quem | herói |
| Música | `pantano_lodo` |

🎥 A escada de luz abre para uma manhã verde e húmida. Nevoeiro baixo sobre a água. Passadiços de madeira podre a perder de vista.
🎬 O herói dá três passos. Uma tábua parte-se. Ele cai na água até aos joelhos. Uma sanguessuga salta-lhe para a perna.
- `[Sistema] Estado: Agarrado (Sanguessuga). Esquiva duas vezes para a sacudires.`
- `[Sistema] Aviso: calor. A Estamina recupera mais devagar.`
- `tut_calor_pantano`: `[Sistema] Calor: a Estamina recupera mais devagar. Bebe água ou Água de Coco para o aguentar (5 min).`
🎬 Ao longe, num poste, uma placa velha da Guilda: *"Cuidado: Homens-Lagarto hostis a partir do andar 23. — Guilda de Ascendia"*. Alguém riscou "hostis" e escreveu por cima, com outra letra: *"alguns"*.

⚙ Sem falas. Missão **H_08** ainda não ativa (abre na cena C3-02).

---

## C3-02 — A Ordem

| | |
|---|---|
| ID | `cena_c3_02_ordem` |
| Quando | voltar a Ascendia com `andar_maximo >= 23` |
| Onde | Guilda, gabinete do Mestre Gorvan |
| Quem | herói, Mestre Gorvan, Lyra |
| Música | `guilda` (versão séria, tambor lento) |

🎬 A Lyra está à porta do gabinete, a mexer nos óculos. Faz sinal ao herói para entrar. Não sorri.
🎬 O Gorvan está de pé, de costas, a olhar para um mapa do pântano pregado na parede. Há três alfinetes vermelhos no andar 24.
- **Gorvan** *(normal)*: "Três equipas de exploradores atacadas no andar 23 este mês. Homens-Lagarto. Escamas, lanças, gritos."
- **Gorvan** *(normal)*: "A aldeia deles fica no 24. A Guilda decidiu. Vão ser expulsos. Para cima. Para longe dos caminhos."
- 🎬 Vira-se.
- **Gorvan** *(normal)*: "Vais tu. Rank C chega. Leva a ordem. Eles podem sair a bem."
- **Lyra** *(nervosa, da porta)*: "Mestre… os relatórios dos exploradores dizem que os atacantes tinham pinturas vermelhas. Os da aldeia usam azul. Eu… escrevi isso no relatório."
- **Gorvan** *(normal)*: "Eu li."
- 🎬 Silêncio. O Gorvan entrega um papel com o selo da Guilda: *ORDEM DE EXPULSÃO*.
- **Gorvan** *(normal)*: "A ordem é da Guilda. A decisão, lá em cima, é tua. Não morras."

▶ **"Cumpro a ordem."**
▶ **"Vou primeiro ouvir o que eles dizem."**

- *(cumpro)* **Gorvan** *(normal)*: "Hmm."
- *(ouvir)* **Gorvan** *(normal)*: "Hmm." 🎬 Por meio segundo, quase sorri. **Lyra** *(baixinho)*: "Obrigada."

⚙ Missão **H_08 / R3_02 Ordem da Guilda** ativa. `[Sistema] Missão: leva a ordem à Aldeia Sssar (andar 24).`
⚙ Recebe a **Ordem de Expulsão** (item de missão).

---

## C3-03 — Sssim, Jogador

| | |
|---|---|
| ID | `cena_c3_03_sssar` |
| Quando | chegar à Aldeia Sssar (andar 24) com H_08 ativa |
| Onde | andar 24, Estacas |
| Quem | herói, Chefe Ssark, Xamã Ilssa, Kesh, Homens-Lagarto |
| Música | `aldeia_sssar` (tambores de água) |

🎬 Uma aldeia de cabanas sobre estacas, por cima de uma lagoa. Totens pintados de azul. Canoas.
🎬 Ao ver o herói, os guerreiros levantam as lanças. Um jovem (Kesh) aponta um arco.
- **Kesh** *(zangado)*: "Um da janela! Com o papel da Guilda na mão! Eu sabia, eu sabia!"
- 🎬 Um Homem-Lagarto velho, enorme, com uma cicatriz no focinho, pousa a mão na lança do Kesh e baixa-a.
- **Chefe Ssark** *(normal, sibilando)*: "Baixa a lança, Kessh. Um papel não morde. Ainda."
- **Chefe Ssark** *(normal)*: "Sssou o Ssark. Chefe dos Sssar. Sei o que dizz o teu papel. Os da Guilda já cá vieram dizê-lo. Ssem papel."
- **Chefe Ssark** *(triste)*: "Os que atacam os teuss exploradores não são dos nossos. São os Renegados. Exilados. Pintam-se de vermelho. Querem ssangue e ouro."
- **Chefe Ssark** *(normal)*: "Expulsámo-los há três luas. Agora atacam os teuss para que a Guilda nos expulsse a nós. E ficam com a aldeia."

▶ **"Tens provas?"**
▶ **"Acredito em ti."**
▶ **"A ordem é a ordem."**

- *(provas)* **Ssark**: "Provass… Os Renegados têm um acampamento a leste. Traz a insígnia do Campeão deles. A Guilda lê insígnias melhor do que lê lagartos."
- *(acredito)* **Ssark** *(surpresa)*: "Um da janela que acredita sem provas. É raro. Ou é tolo. Ou é as duas coisass." ⚙ +amizade escondida com a aldeia
- *(a ordem)* **Ssark** *(triste)*: "Então vem amanhã com a tua espada. Esta noite, pelo menos, dorme na cabana de hósspedes. Ninguém dorme ao relento em Sssar. Nem os inimigos."

⚙ `[Sistema] Missão: decide o destino da Aldeia Sssar.` A cena C3-04 acontece **na primeira noite** passada no andar 24 (dormir na cabana de hóspedes ou ficar até às 21:00).

---

## C3-04 — A Aldeia à Noite

| | |
|---|---|
| ID | `cena_c3_04_noite` |
| Quando | 21:00 no andar 24, com H_08 ativa |
| Onde | Aldeia Sssar, cais da lagoa, à noite |
| Quem | herói, Kai, Ssark (ao longe), crianças-lagarto |
| Música | `aldeia_sssar` (versão noturna: só água e um tambor) |

🎬 Noite. Pirilampos sobre a lagoa. Na aldeia, crianças-lagarto brincam a atirar pedras para a água. Uma velha canta.
🎬 O herói está no cais. Passos atrás dele: o Kai, com uma lanterna, sem fôlego.
- **Kai** *(normal)*: "Soube pela Lyra. Uma ordem de expulsão. És tu que a fazes?"
- **Kai** *(normal)*: "A Guilda paga o dobro por esta. E dá cem pontos de rank. Cem! Com isso passas para B. Mais missões. Mais andares. Mais depressa."
- 🎬 Uma criança-lagarto corre atrás de um sapo, cai, ri-se. O Kai olha para ela. Desvia os olhos.
- **Kai** *(sério)*: "Eu fazia. Não por maldade. Porque cada dia aqui é um dia que a Yui está sem mim. Tudo o que me põe mais perto do topo, eu faço."
- **Kai** *(triste)*: "É horrível dizer isto, não é? É horrível e é verdade."

▶ **"Não vou fazer mal a quem não fez nada."**
▶ **"Também quero subir depressa."**
▶ **"A Yui ia querer que fizesses isto?"** (só com `kai_promessa_1`)

- *(não vou)* **Kai** *(normal)*: "Pois. Tu és assim. …Às vezes queria ser assim." ⚙ +30 · flag `kai_viu_escolha`
- *(depressa)* **Kai** *(normal)*: "Então sabes do que falo. Faz a tua escolha. Eu não te julgo. Ninguém aqui tem as mãos limpas."
- *(Yui)* **Kai** *(zangado, depois triste)*: "Não metas a Yui nisto. …Não. Não ia. Ia ficar zangada comigo uma semana." ⚙ +30 · flag `kai_viu_escolha`
- 🎬 O Kai vai-se embora pela escada. Para a meio, sem se virar.
- **Kai** *(normal)*: "Seja o que for que escolhas… escolhe tu. Não deixes a janela escolher por ti."

### A escolha

🎬 Na mesma noite, o herói volta para a cabana. No meio do caminho, o Ssark espera-o, sentado num totem.
- **Ssark** *(normal)*: "Amanhã de manhã decidess. Eu não peço. Os Ssar não pedem. Só esperam."

▶ **A) Cumprir a ordem da Guilda.** *(expulsar a aldeia)*
▶ **B) Defender a aldeia e provar que os Renegados são os culpados.**

⚙ O jogo **grava** antes desta escolha (`[Sistema] Progresso guardado.`) e pede confirmação: *"Esta escolha não se pode desfazer. Tens a certeza?"*

---

## C3-05A — Cumprir a Ordem

| | |
|---|---|
| ID | `cena_c3_05a_expulsar` |
| Quando | escolha A |
| Onde | Aldeia Sssar, manhã |
| Quem | herói, Ssark, guerreiros Sssar |
| Música | `aldeia_sssar` → `guardiao` |

🎬 De manhã, o herói entrega a ordem ao Ssark. O Ssark lê-a devagar. Dobra-a. Guarda-a.
- **Ssark** *(triste)*: "Assim sseja. Os Ssar não lutam contra quem os vem expulsar com um papel. Lutam contra quem vem com uma espada."
- **Ssark** *(normal)*: "Tu vieste com as duas. Então lutamos. Uma vez. Para que os nossos filhos saibam que não fugimos."
⚙ Luta contra os guerreiros da aldeia e o **Totem Vivo de Sssar** (o guardião do andar). Os guerreiros caem de joelhos, não morrem.
🎬 No fim, os Homens-Lagarto carregam as canoas e partem pela lagoa, para cima. As crianças olham para trás. O Kesh aponta o arco ao herói e depois baixa-o.
- **Ssark** *(normal, da última canoa)*: "Lembrar-me-ei de ti, Jogador{/a}. Não com ódio. Com cansaço."
🎬 Horas depois, pinturas vermelhas aparecem nos totens: os **Renegados** ocupam a aldeia vazia.
- `[Sistema] Missão concluída: Ordem da Guilda.`
- `[Sistema] +100 pontos de Guilda.`

⚙ Flag `sssar_expulsa`. A aldeia fica com **Renegados** (inimigos). O Ssark só volta a aparecer no **andar 97** (Cidade dos Perdidos).
⚙ Na Guilda: **Gorvan** *(normal)*: "Cumpriste." 🎬 não diz mais nada. A Lyra não olha para o herói nesse dia.

---

## C3-05B — Defender a Aldeia

| | |
|---|---|
| ID | `cena_c3_05b_defender` |
| Quando | escolha B |
| Onde | Acampamento Renegado (andar 24) → Guilda |
| Quem | herói, Ssark, Kesh, Campeão Renegado, depois Gorvan |
| Música | `selva_tambores` → `guardiao` |

🎬 De manhã, o herói rasga a ordem à frente do Ssark. O Ssark não diz nada durante muito tempo.
- **Ssark** *(feliz, raro)*: "Rassgaste um papel da Guilda. Os teuss vão ficar zangados. Vamos dar-lhes uma razão para ficarem contentess."
⚙ Missão **R3_03 Os Renegados** (`docs/dialogos/povoacoes_r03.md`): o Ssark e o Kesh lutam a teu lado. Vencer o **Campeão Renegado** no acampamento e o **Totem Vivo** (que os renegados tinham roubado e corrompido).
🎬 O Campeão Renegado cai. Na armadura dele, a **insígnia vermelha** e um saco com coisas roubadas aos exploradores (bússolas, cantis com o símbolo da Guilda).
- **Ssark** *(normal)*: "Leva isto à tua Guilda. A prova. Eles leem insígnias."

### Na Guilda
🎬 O herói põe a insígnia vermelha e o saco em cima da mesa do Gorvan. O Gorvan pega numa bússola com o símbolo da Guilda. Vira-a nas mãos.
- **Gorvan** *(normal)*: "Hmm."
- **Gorvan** *(normal)*: "Desobedeceste a uma ordem da Guilda."
- **Gorvan** *(normal)*: "Fizeste bem." 🎬 pausa. "Desobedeceste bem."
- 🎬 Rasga a ordem de expulsão original, que ainda tinha na gaveta.
- **Gorvan** *(normal)*: "Vou escrever à Guilda. Vão pedir desculpa aos lagartos. Por escrito. Vão odiar."
- **Lyra** *(da porta, a chorar de alegria)*: "Eu sabia! Eu SABIA! Pinturas vermelhas! Eu escrevi!"

⚙ Flag `sssar_defendida`. A aldeia fica **amiga** (loja tribal, cabana, Festa na Aldeia). O **Ssark pode ser companheiro** (R3_03 concluída). **Gorvan +100** (❤️).
⚙ `[Sistema] Missão concluída: Ordem da Guilda.` (sem pontos de Guilda: "a Guilda não paga desobediências, mesmo boas").

---

## C3-06 — O Ovo de Pedra

| | |
|---|---|
| ID | `cena_c3_06_serpente` |
| Quando | vencer a Serpente do Lodo (andar 25) |
| Onde | andar 25, Altar Inundado |
| Quem | herói |
| Música | `serpente_lodo` → silêncio |

🎬 A serpente afunda devagar no lodo. Quando a água baixa, no altar fica à vista um **ovo de pedra** do tamanho de uma melancia, rachado.
🎬 O herói aproxima-se. Dentro da racha, uma luz azul. Pela fenda vê-se uma **janela azul pequenina**, como a do Sistema, a piscar.
- `[Sistema] Objeto desconhecido.`
🎬 O herói toca-lhe. O ovo desfaz-se em pó. A janelinha apaga-se como uma vela.
- `[Sistema] …`
- `[Sistema] Mini-boss derrotado: Serpente do Lodo.`

⚙ Sem falas. (A página 25 do diário fala do mesmo ovo.) Recompensas normais: **Língua de Serpente**, título *Encantador de Serpentes*.

---

## C3-07 — A Vila dos Sapos

| | |
|---|---|
| ID | `cena_c3_07_coaxa` |
| Quando | entrar na Vila Coaxa (andar 26) pela primeira vez |
| Onde | andar 26, Vila Coaxa |
| Quem | herói, Barão Coaxim, Coro dos Sapos |
| Música | `pantano_lodo` (versão alegre, com coaxar ritmado) |

🎬 Casas em cima de nenúfares gigantes. Pontes de juncos. Sapos de chapéu a vender coisas aos gritos.
🎬 Três sapos num palco de nenúfar tentam cantar; falta uma voz e a canção sai torta.
🎬 Um sapo enorme, de colete dourado e monóculo, aproxima-se, a abanar um leque.
- **Barão Coaxim** *(feliz)*: "Ora viva, ora viva, quem chega à minha vila? Um Jogador valente, de olhar pouco tranquilo!"
- **Barão Coaxim** *(normal)*: "Sou o Barão Coaxim, o mais rico do lugar. Se tiveres tesouros raros… eu tenho ouro a dar!"
- **Coro dos Sapos** *(tristes, em coro)*: "♪ Croac… croac… falta… o… tenor… ♪"

⚙ Desbloqueia a **Vila Coaxa** (estalagem-nenúfar, cristal, loja, barcos). Missões R3_06, R3_07, R3_08, R3_16 disponíveis.

---

## C3-08 — A Que Não Morre

| | |
|---|---|
| ID | `cena_c3_08_hidra_antes` |
| Quando | entrar n'O Altar (andar 30) |
| Onde | andar 30, Lago Ritual |
| Quem | herói, Hidra do Pântano (e o Ssark, se for teu companheiro) |
| Música | silêncio → `hidra` |

🎬 Um lago redondo com ilhas de pedra. Seis braseiros apagados à volta.
🎬 A água borbulha. Sobe uma cabeça verde. Depois uma roxa. Depois uma amarela. Por baixo, um corpo do tamanho de uma casa.
- `[Sistema] Boss: Hidra do Pântano, A Que Não Morre.`
- *(com o Ssark na equipa)* **Ssark** *(normal)*: "Os nossos avós chamavam-lhe 'a Que Come os Reis'. Queima os pescoços, Jogador{/a}. Queima-os. Sem fogo, ela nunca acaba."
- `[Sistema] Dica: acende os braseiros. O fogo impede as cabeças de voltarem a crescer.` *(só na 1.ª tentativa)*

⚙ Luta (ver `docs/BOSSES.md`, secção 6).

## C3-09 — A Que Morreu

| | |
|---|---|
| ID | `cena_c3_09_hidra_depois` |
| Quando | vencer a Hidra |
| Onde | andar 30, O Altar |
| Quem | herói (e o Ssark) |
| Música | `vitoria` → `pantano_lodo` (calmo) |

🎬 A última cabeça cai. O corpo afunda devagar no lago. Bolhas. Depois nada. Os braseiros continuam acesos.
- `[Sistema] Boss derrotado: Hidra do Pântano.`
- `[Sistema] Obtiveste: Arco da Hidra.`
- `[Sistema] Título obtido: Corta-Cabeças.`
- `[Sistema] Região 3 concluída. Andar 31 desbloqueado.`
- *(com o Ssark)* **Ssark** *(feliz)*: "Os avós vão dormir melhor esta noite. Eu também. Obrigado, Jogador{/a}. Nos Ssar, um obrigado vale uma lança."

⚙ Missão **H_09** concluída.

---

## C3-10 — Dia da Subida: A Arena

| | |
|---|---|
| ID | `cena_c3_10_dia_subida` |
| Quando | voltar a Ascendia depois da Hidra |
| Onde | Praça da Torre (Dia da Subida, F_05) → Arena |
| Quem | herói, Aldric, Freya, Lucien, Kai, (Ssark, se a aldeia for amiga) |
| Música | `dia_da_subida` |

🎬 A Praça em festa. Uma estátua nova: uma hidra de três cabeças, pequena, com uma cabeça torta (o escultor enganou-se).
- **Governador Aldric** *(no palco)*: "Cidadãos! O pântano está seguro! E… e a Arena abre a categoria Prata! A Capitã Freya pediu-me para dizer isto. Disse-mo três vezes."
- **Lucien** *(do palco)*: "♪ Sete cabeças e um herói! Contem comigo! Uma, duas… ♪" 🎬 a multidão conta até nove.
- *(se `sssar_defendida`)* 🎬 Na Praça, um grupo de Homens-Lagarto com colares azuis, desconfiados, a provar espetadas. O Ssark acena ao herói. **Ssark**: "Viemos ver a vossa festa. É barulhenta. Gostamos." · Os aldeões ficam espantados; a Mia vai logo ter com o Kesh para comparar "armas".
- 🎬 A Freya aparece ao lado do herói, de braços cruzados.
- **Freya** *(normal)*: "Arena de Prata. Este fim de semana. Inscreve-te. Vou estar a ver."
- 🎬 O Kai, ao pé da fonte, a afiar a espada.
- *(se `sssar_defendida`)* **Kai** *(normal)*: "Defendeste os lagartos. A Guilda pediu desculpa. A Guilda! …Eu não tinha feito isso. Ainda bem que foste tu lá acima, e não eu."
- *(se `sssar_expulsa`)* **Kai** *(normal)*: "Cumpriste a ordem. Eu também tinha cumprido. …Não te sintas mal. Ou sente. Eu sentia-me. Sinto."
- **Kai** *(sério)*: "Sabes o que me disse a janela, ontem? Quando passei o 30? 'Bom ritmo, Jogador nº 9 999.' Bom ritmo. Como se estivesse a contar."

⚙ Abre a **Arena (Prata)** e os **minijogos da Taberna**. Flag `kai_bom_ritmo` (primeira vez que o Sistema "fala" com o Kai de forma diferente: pista para o acordo do capítulo 7).
⚙ `[Sistema] Capítulo 4: O Deserto.` (título grande no ecrã)
