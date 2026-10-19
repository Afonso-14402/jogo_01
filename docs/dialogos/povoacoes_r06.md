# Povoações da Região 6 — diálogos e missões

Os NPCs que vivem nos andares 51–60 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r06_oceano.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap06_oceano.md`.

**Gente do mar**: os do Porto são **ex-piratas** (Torrenses do mar): falam alto, juram muito ("Por mil
alforrecas!"), riem-se de tudo, desconfiam de quem tem a roupa seca. Os de Coralina (sereias e tritões) falam devagar
e com cerimónia; dizem "os de cima" aos humanos. Bips: os do porto, roucos; os de Coralina, com um eco de água.

---

## 1. Porto Arquipélago (andar 52)

Primeira chegada: cena **C6-02**. Tem **estalagem** (a taberna da Rosa), **cristal**, **estaleiro** e **loja**.

### 1.1 Capitã Marisa Vento-Sul

| | |
|---|---|
| Voz | bips graves e lentos; sorri de lado; nunca levanta a voz, nem a ameaçar |
| Quem é | 50 anos, ex-capitã pirata do navio "Desaforo". Perdeu um olho numa luta com o **Barba-Lodo** (o antigo capitão dela, que a traiu). Mudou-se para "o lado honesto do mar" e fundou o porto. Tem um olho de vidro azul que tira para assustar os clientes que não pagam |
| Repete | "Por mil alforrecas.", "O mar não perdoa. Eu às vezes." |

| ID | Condição | Fala |
|---|---|---|
| `marisa_01` | — | "O mar é a única coisa honesta na torre. Se te quer matar, avisa: fica cinzento." |
| `marisa_02` | — | "Fui pirata vinte anos. Roubei a reis, a mercadores e a outros piratas. Agora vendo peixe. Durmo melhor. Ganho menos. É justo." |
| `marisa_03` | antes de R6_13 | "Há um navio fantasma que aparece nas noites de nevoeiro. O capitão tem barba de algas. Chamava-se meu capitão. Agora chama-se Barba-Lodo. Deve-me um olho." |
| `marisa_04` | `missao(R6_13) == concluida` | "O Barba-Lodo caiu. Fiquei com o olho dele? Não, ele não tinha. Fiquei com o chapéu. Serve-te melhor a ti. Guarda-o." |
| `marisa_05` | `flag(kai_desaparecido)` | "O meu bote ainda está no navio fantasma? Deixa-o lá. Se o rapaz voltar, tem com que fugir." |
| `marisa_06` | evento Ataque Pirata | "PIRATAS! Os de verdade! Os maus! Às armas, que os bons somos nós! Mais ou menos!" |
| `marisa_curta` | já falaste hoje | "O mar está calmo. Eu estou ocupada. Até amanhã." |

### 1.2 Joaquim, o Lobo-do-Mar — cartógrafo

| ID | Condição | Fala |
|---|---|---|
| `joaquim_01` | — | "Setenta anos a desenhar o mar. O mar muda. Eu também. Ele mais depressa." |
| `joaquim_02` | antes de R6_02 | "Cinco ilhas. Preciso de alguém que as visite todas e me diga se ainda lá estão. As ilhas daqui às vezes mudam de sítio. Juro." |
| `joaquim_03` | `missao(R6_02) == concluida` | "A carta náutica, com as correntes todas. Segue as setas azuis: o mar empurra-te de graça. Contra as setas, rema e chora." |

### 1.3 Tomé — carpinteiro naval

| ID | Condição | Fala |
|---|---|---|
| `tome_01` | — | "Um barco é como um cão: se o tratas bem, leva-te a casa. Se não, morde. Os barcos mordem afundando." |
| `tome_02` | depois de cada parte da R6_03 | "Pronto! Agora vai mais depressa, aguenta mais e dispara mais. Três coisas que eu também queria para mim." |

### 1.4 Rosa — taberna do porto

| | |
|---|---|
| Quem é | 40 anos, ex-cozinheira de navio pirata ("cozinhei para cem bandidos e nenhum morreu da comida, que é mais do que se pode dizer das espadas"). Dona da taberna e estalagem do porto |
| Loja | estalagem (40 por noite) · comida do mar · Sementes de Ananás · receitas (Caldeirada do Porto, Ananás Grelhado) |

| ID | Condição | Fala |
|---|---|---|
| `rosa_01` | — | "Caldeirada! Com peixe de três sítios e tomate de um. Senta-te. Come. Conta-me uma mentira, que eu conto-te um rumor." |
| `rosa_rumor_01` | — | "Dizem que no fundo da fossa há um ovo do tamanho de uma casa. Eu não acredito. Já vi muitos ovos. Nenhum desse tamanho." |
| `rosa_rumor_02` | — | "O Barba-Lodo só aparece com nevoeiro. Se vires uma lanterna verde no mar à noite, rema para o outro lado. Ou para lá, se fores maluc{o/a}." |
| `rosa_rumor_03` | — | "Uma ostra gigante no recife só abre a quem lhe canta. Tens boa voz? Não? Arranja uma concha que cante por ti." |
| `rosa_02` | `flag(kai_desaparecido)` | "O rapaz do casaco azul comeu aqui antes de ir. Pediu dois pratos. Pagou três. Disse 'o terceiro é para quando eu voltar'. Ainda tenho o prato guardado." |

### 1.5 Tiago — grumete de 13 anos

| ID | Condição | Fala |
|---|---|---|
| `tiago_01` | antes de R6_04 | "Leva-me! Sei dar nós! Sei remar! Sei limpar peixe! Sei… muitas coisas! Leva-me!" |
| `tiago_02` | antes de R6_04 | "O meu pai era pirata. Do Barba-Lodo. Não voltou. Eu não quero ser pirata. Quero ser capitão. É diferente. Os capitães voltam." |
| `tiago_03` | no barco (depois de R6_04) | "Leme a estibordo! …Isso é a direita. Acho. Sim. A direita." |
| `tiago_04` | no barco, tempestade | "Isto é normal?! Diz-me que é normal! NÃO É NORMAL!" |
| `tiago_05` | `missao(R6_13) == concluida` | "O Barba-Lodo… O meu pai estava na tripulação dele? Viste-o? …Não digas. Prefiro não saber. Prefiro pensar que fugiu e tem um barco só dele." |

---

## 2. Vila das Pérolas (andar 54)

Ilha de mergulhadores no meio do recife. Tem **cabana**, **cristal** e **loja**.

### 2.1 Ama Kaia — mergulhadora

| | |
|---|---|
| Quem é | 55 anos, a melhor mergulhadora da vila: aguenta 5 minutos debaixo de água. Ri-se muito e fala pouco ("debaixo de água não se fala; aprendi a calar-me") |

| ID | Condição | Fala |
|---|---|---|
| `kaia_01` | — | "Respira fundo. Mais. Mais. Agora segura. Isso. Já consegues dez segundos. Eu consigo trezentos. Treina." |
| `kaia_02` | antes de R6_06 | "Queres aprender? Dez pérolas no recife. Num dia. Sem morrer. É o exame." |
| `kaia_03` | `missao(R6_06) == concluida` | "Toma a máscara. Era da minha filha. Agora ela tem guelras de tanto mergulhar. Brincadeira. Tem uma loja em Coralina." |

### 2.2 Ourives Pérola

| ID | Condição | Fala |
|---|---|---|
| `perola_01` | — | "Chamo-me Pérola. Os meus pais eram mergulhadores. Não tinham muita imaginação." |
| `perola_02` | antes de R6_07 | "Cinco pérolas e uma negra. Faço-te um colar que até a Rainha de Coralina vai querer." |
| `perola_03` | `missao(R6_07) == concluida` | "Fica-te bem. As pérolas ficam bem a toda a gente. É a vantagem de serem redondas." |

### 2.3 Velho Nalu — contador de histórias

| ID | Condição | Fala |
|---|---|---|
| `nalu_01` | — | "O mar tem memória. Lembra-se de cada barco que afundou e de cada peixe que fugiu. Eu também. Sou mais velho do que o mar. Mentira. Quase." |
| `nalu_02` | — | "O Leviatã do andar 60 não é mau. É o último. Os outros foram comidos pela torre há muito. Ninguém gosta de ser o último de nada." |
| `nalu_03` | antes de R6_15 | "Há um polvo na floresta de algas que pôs um ovo e morreu. Os tubarões andam à volta. Se alguém levasse o ovo para a bolha de ar…" |
| `nalu_04` | `boss_derrotado(leviata)` | "O último do mar. Afundou-se. Fiquei a noite toda na praia. Às vezes a coisa certa e a coisa triste são a mesma." |

---

## 3. Coralina, a Cidade Submersa (andar 57)

Primeira chegada: cena **C6-07**. Dentro da cúpula não há barra de Ar. Tem **estalagem**, **cristal**, **forja de coral**
e **loja**. A **concha do Nereu** está na Rua das Marés.

### 3.1 Rainha Coralina

| | |
|---|---|
| Voz | bips lentos e musicais, sempre no mesmo tom; quando se zanga, fica mais lenta ainda |
| Quem é | sereia de cabelo branco, rainha há 200 anos (as sereias vivem muito). Séria, protetora, cansada das coisas que caem de cima e "magoam os meus". Troca pérolas por itens raros |

| ID | Condição | Fala |
|---|---|---|
| `coralina_01` | — | "Os de cima caem. Nós apanhamos. Há mil anos que é assim. Não há agradecimentos. Só mais coisas a cair." |
| `coralina_02` | — | "O meu filho quer ver o céu. Todos os jovens querem. Os que vão, não voltam. Já perdi muitos jovens para o céu." |
| `coralina_03` | `missao(R6_09) == concluida` | "Levaste o Maré à praia e trouxeste-o de volta. Molhado e feliz. Obrigada. Não lhe digas, mas chorei." |
| `coralina_04` | `boss_derrotado(leviata)` | "O Leviatã. Era antigo quando eu nasci. Era antigo quando a minha avó nasceu. Agora é uma história. Odeio quando os antigos viram histórias." |

**Perguntar sobre…**
- *O Nereu*: "Era filho de dois que caíram de cima, numa noite de tempestade. Cresceu aqui, entre nós. Nadava como uma sereia e cantava pior do que um tritão. Foi-se embora com o da janela triste. A concha dele ainda está na rua. Ninguém a tira."
- *O da janela triste*: "Não sei o nome. Ninguém sabe. Ficou cá uma estação. Desenhava mapas de sítios que não existem. Nunca dizia o nome. Dizia que o nome era para quando voltasse a casa."

### 3.2 Príncipe Maré

| ID | Condição | Fala |
|---|---|---|
| `mare_01` | antes de R6_09 | "Como é o céu? É azul? Tem fim? Tem peixes? Os de cima dizem que tem pássaros. Os pássaros são peixes que voam? EXPLICA!" |
| `mare_02` | `missao(R6_09) == concluida` | "Vi o céu! É ENORME! E o sol queima a cauda! Quero voltar! A mãe diz que não! A mãe diz sempre que não!" |

### 3.3 Nerissa — ferreira abissal

| ID | Condição | Fala |
|---|---|---|
| `nerissa_01` | abrir loja | "Coral abissal. Mais duro do que o aço, mais leve do que a prata. Forjo debaixo de água. Ninguém acredita até ver." |
| `nerissa_02` | — | "A forja funciona com o calor das fontes do 58. Não há fogo debaixo de água. Há coisa melhor." |

### 3.4 Lirael — cantora

| ID | Condição | Fala |
|---|---|---|
| `lirael_01` | antes de R6_10 | "Há quatro conchas no mar que cantam sozinhas. Se mas trouxeres, faço-te um instrumento. Uma concha que canta por ti." |
| `lirael_02` | `missao(R6_10) == concluida` | "A Concha do Mar. Toca-a e o mar escuta. Os peixes, as ostras, até os tubarões param um bocadinho." |

**Canções da Concha do Mar** (tocar com [usar]; 1 de cada vez; 10 min)

| Canção | Efeito |
|---|---|
| Canção da Maré | +20% velocidade a nadar |
| Canção da Ostra | abre a ostra gigante do andar 54 (Pérola Negra) |
| Canção da Calmaria | os monstros do mar demoram mais a reparar em ti |
| Canção do Nereu *(ensinada pela Rainha, com `ouviu_nereu` e R6_09 feita)* | sem efeito; é bonita. A Rainha chora a ouvi-la |

### 3.5 Oceanus — guarda-tritão

| ID | Condição | Fala |
|---|---|---|
| `oceanus_01` | — | "Lutas debaixo de água? Não. Debates-te debaixo de água. Eu luto. Queres aprender? Desafia-me." |
| `oceanus_02` | depois de o venceres na Arena | "Venceste-me. Na água. Sou o melhor tritão de Coralina. Era. Agora sou o segundo. Vou ter de treinar até ser outra vez." |

---

## 4. Missões da região, passo a passo

### R6_01 — Um Barco para Ti
| | |
|---|---|
| Quem dá | Capitã Marisa (C6-02) |
| Recompensa | **Barco** (o teu próprio barco: navegar entre ilhas, chegar ao andar 53) |

1. **Pedir** — C6-02.
2. **Passo**: no estaleiro, o **Tomé** mostra o barco velho. Entregar **20 Madeira de Naufrágio + 10 Fio de Alga-Prata + 5 Lingote de Prata**.
   - **Tomé**: "Madeira de naufrágio para um barco. Há coisas que voltam ao sítio onde nasceram."
3. **Entregar** — 🎬 o barco desce para a água. Flutua. O Tomé suspira de alívio.
   - **Marisa** *(normal)*: "Dá-lhe um nome. Barco sem nome é barco que se perde." ⚙ escolher o nome do barco. `tut_barco`: `[Sistema] Barco: [interagir] no cais para embarcar. Vira com [mover]. Âncora com [esquivar].`

### R6_02 — Cartas Náuticas
| | |
|---|---|
| Quem dá | Joaquim |
| Recompensa | **Carta Náutica** (o mapa do mar mostra as correntes) |

1. **Pedir** — `joaquim_02`.
2. **Passo**: visitar as **5 ilhas** do andar 52 (a Ilha da Névoa só aparece com o farol aceso; ver o mapa). Em cada uma, tocar no marco de pedra.
3. **Entregar** — `joaquim_03`.

### R6_03 — Melhorar o Barco (3 partes)
| | |
|---|---|
| Quem dá | Tomé |
| Recompensa | cada parte melhora o barco |

| Parte | Materiais | O que muda |
|---|---|---|
| **Velas** | 10 Fio de Alga-Prata + 5 Madeira de Naufrágio + 5 Pano Velho | +40% de velocidade |
| **Canhões** | 6 Barra de Coral Abissal + 10 Pólvora | 2 canhões (para a luta do Leviatã e as Serpentes) |
| **Casco** | 10 Coral Abissal + 10 Madeira de Naufrágio | aguenta tempestades e o dobro de dano |

### R6_04 — O Grumete
| | |
|---|---|
| Quem dá | Tiago |
| Recompensa | o **Tiago** fica no barco (repara-o durante as lutas e dispara um dos canhões) |

1. **Pedir** — `tiago_01`.
2. **Passo**: levar o Tiago em **3 viagens** de barco: à Ilha do Farol, ao Recife (andar 54, pela escada do mar) e numa noite de tempestade (qualquer andar com mar).
3. **Entregar** — **Tiago** *(feliz)*: "Três viagens e não vomitei! Duas. Vomitei uma. Fico contigo! Sou o teu imediato! …Posso ser o teu imediato?"

### R6_05 — Fantasmas do Navio (história)
= **H_14**. Ver as cenas **C6-03 a C6-05** em `docs/guiao/cap06_oceano.md`.

### R6_06 — Aprender a Mergulhar
| | |
|---|---|
| Quem dá | Ama Kaia |
| Recompensa | **Máscara de Mergulho** (+50% de Ar) |

1. **Pedir** — `kaia_02`.
2. **Passo**: apanhar **10 Pérolas** no andar 54 num só dia (abrir ostras com a **Faca de Mergulho**, que a Kaia empresta).
3. **Entregar** — `kaia_03`.

### R6_07 — Colar de Pérolas
Ourives Pérola. Entregar **5 Pérolas + 1 Pérola Negra** → **Colar de Pérolas** (+15% MP).

### R6_08 — O Tesouro da Garrafa
| | |
|---|---|
| Quem dá | (a garrafa na areia do andar 51) |
| Recompensa | baú de ouro · **Óculo de Pirata** (vê mais longe no mar: os ícones do mapa aparecem a 50 m) |

1. **Começa** ao apanhar a garrafa: `[Sistema] Mapa do Tesouro: "O farol da caveira, ao meio-dia, onde a sombra do olho cai."`
2. **Passo**: no andar 52, ir ao **Farol da Caveira** ao meio-dia (12:00–12:30) e escavar onde cai a sombra do "olho" da caveira pintada.
3. **No baú**: o óculo e uma nota: *"Se encontraste isto, o tesouro era a viagem. Brincadeira. Também há ouro. — Capitão Vasco, nº 298"* (o mesmo capitão do diário de bordo).

### R6_09 — O Príncipe Maré
| | |
|---|---|
| Quem dá | Príncipe Maré (Coralina) |
| Recompensa | ❤️ Rainha Coralina · **Coroa de Conchas** (cosmético) |

1. **Pedir** — `mare_01`, depois: "Leva-me à praia! A do 51! Eu tenho cauda, não ando, mas tu tens um barco! Só não me deixes secar!"
2. **Passo**: levar o Maré no barco (num balde grande) até à praia do andar 51. Ele tem uma barra de **Água**: desce fora de água; molhá-lo no mar ou passar por chuva enche-a.
3. **Na praia** — 🎬 o Maré olha para o céu, de boca aberta, deitado na rebentação. **Maré**: "…É tão grande. Como é que não cai?"
4. **Entregar** — levá-lo de volta a Coralina. `coralina_03`.

### R6_10 — Canções de Lirael
Lirael. Encontrar **4 conchas cantantes** (andares 51, 54, 56, 59: ouvem-se a 15 m) → **Concha do Mar** (instrumento; ver secção 3.4).

### R6_11 — Escafandro
Dada pelo **Gizmo**. Falas em `docs/dialogos/gizmo.md`. **10 Gel Elétrico + 5 Barra de Coral Abissal + 1 Lanterna Abissal** → **Capacete de Escafandro** (Ar infinito e aguenta a pressão do 58).

### R6_12 — Pinça de Ouro
Dada pelo **Barão Coaxim** (andar 26). Vencer o **Caranguejo Rei Pinça-de-Ouro** (andares 51 e 54) e levar-lhe a pinça.
- **Barão** *(ao receber)*: "Pinça de ouro, pinça brilhante, para a Galeria, que é importante! Seis mil moedas, contadas a cantar! …Ou ficas com ela? Que pena. Croac."
- **Escolha**: 6 000 ouro **ou** ficar com a pinça (decoração para a casa).

### R6_13 — Barba-Lodo
| | |
|---|---|
| Quem dá | Capitã Marisa (rank A; = `G_A_03`) |
| Recompensa | **Chapéu de Barba-Lodo** (+5% dano no mar) · **Bússola Amaldiçoada** |

1. **Pedir** — `marisa_03`, depois: "Vence-o. Não pelo olho. Pelos rapazes que ele levou. O pai do Tiago era um deles."
2. **Passo**: nos andares 52 ou 53, numa **noite de nevoeiro**, navegar até à lanterna verde. Abordar o navio fantasma pequeno do **Barba-Lodo** e vencê-lo no convés (o navio dispara canhões; a tripulação fantasma ajuda-o).
   - **Barba-Lodo** *(feliz, voz de afogado)*: "Um visitante! Seco! Vamos resolver isso!"
   - *(aos 10%)* **Barba-Lodo** *(triste)*: "A Marisa… ainda tem o olho de vidro? Diz-lhe… diz-lhe que lhe devo um. Que lhe devia muitos."
3. **Entregar** — `marisa_04` · `tiago_05`.

### R6_14 — O Cavalo-marinho Ferido
Dada pelo **Zed**. Falas em `docs/dialogos/zed.md`. No andar 56, encontrar o cavalo-marinho ferido (perto da Clareira das Lontras) e dar-lhe **Alga Doce 3 dias seguidos** → **Montada Cavalo-marinho Gigante**.

### R6_15 — O Ovo de Polvo
| | |
|---|---|
| Quem dá | Velho Nalu |
| Recompensa | **Polvo Bebé** (animal de estimação) |

1. **Pedir** — `nalu_03`.
2. **Passo 1**: no andar 56, resolver o puzzle das **lontras** (dar-lhes as conchas por ordem de tamanho) para abrir a gruta do ovo.
3. **Passo 2**: levar o ovo até à **Bolha de Ar** (zona segura). Homens-Tubarão atacam pelo caminho (3 ondas). Se o ovo levar 3 golpes, racha e volta à gruta.
4. **Entregar** — 🎬 dentro da bolha, o ovo abre-se. Um polvo pequenino agarra-se à cara do herói. **Nalu** *(ao voltar)*: "Gostou de ti. Os polvos escolhem com os oito braços. Ninguém lhes diz que não."

---

## 5. Missões da Guilda (rank A) da região

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_A_03 Barba-Lodo (R6_13) | "PROCURA-SE: Barba-Lodo, pirata fantasma. Ataca barcos nas noites de nevoeiro (andares 52–53). Cuidado com os canhões." | "Um pirata fantasma! Com canhões fantasmas! As balas também são fantasmas? Dói na mesma? Não respondas." | "Venceste-o! A Capitã do porto mandou uma carta. Só diz 'Obrigada. M.' e tem um desenho de um olho a piscar. Não percebi. Tu percebeste?" |
