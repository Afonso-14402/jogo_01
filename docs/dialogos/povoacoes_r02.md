# Povoações da Região 2 — diálogos e missões

Os NPCs que vivem nos andares 11–20 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r02_cavernas.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap02_cavernas.md`.

---

## 1. Posto Mineiro Fundo-Rocha (andar 11)

Primeira chegada: cena **C2-01** (a Hilda e as três tochas).

### 1.1 Hilda Fundo-Rocha — chefe do posto

| | |
|---|---|
| Voz | bips graves e fortes; ri como quem parte pedra; diz tudo como se estivesse a ralhar, mesmo quando elogia |
| Quem é | anã de 90 anos (nova, para uma anã), trança ruiva até à cintura, braços enormes. Mineira de Ascendia, prima afastada de ninguém ("os anões de Ascendia são poucos, somos todos primos") |
| Repete | "Luz primeiro, pergunta depois.", "Pela minha picareta!", "Bem-vind{o/a}, mais ou menos." |
| Loja | picaretas, tochas, Giz de Mineiro, Carvão (ver `docs/LOJAS.md`, secção 3.3) · organiza a **corrida de vagonetas** |

| ID | Condição | Fala |
|---|---|---|
| `hilda_01` | — | "Luz primeiro, pergunta depois. É a regra número um da mina. A número dois é: não lambas os cristais." |
| `hilda_02` | — | "Os goblins roubam-nos o minério e depois vendem-no aos kobolds. Os kobolds vendem-no a nós. É uma economia." |
| `hilda_03` | — | "Pela minha picareta! Outra vez sem tochas?" |
| `hilda_04` | `hora entre 6 e 8` | "Turno da manhã! Toda a gente para dentro! Tu também, se quiseres trabalhar. Não queres. Ninguém quer." |
| `hilda_05` | `hora entre 20 e 23` | "À noite a mina geme. Não são fantasmas. Quase nunca são fantasmas." |
| `hilda_06` | `missao(R2_01) == concluida` | "Com o teu carvão, as tochas chegam para o mês todo. Os rapazes já não têm medo do escuro. Têm medo de mim. Melhor." |
| `hilda_07` | `missao(R2_03) == concluida` | "Os diários dos meus mineiros perdidos… Pus os nomes deles numa tábua à entrada. Agora passam por eles todos os dias." |
| `hilda_08` | `boss_derrotado(golem_cristal)` | "O Golem caiu! Já se pode ir à sala do trono buscar cristais! Não se pode? Pode-se! Eu vou!" |
| `hilda_09` | `missao(R2_13) == concluida` | "O Pedrito escreve-me da cidade. Diz que o Brom grita com ele todos os dias. Está feliz da vida." |
| `hilda_10` | invasão goblin (evento) ativa | "GOBLINS! Às picaretas! E tu, à espada! Ou ao que trazes! Defende o posto!" |
| `hilda_curta` | já falaste hoje | "Mais tochas? Dez moedas." |

**Perguntar sobre…**
- *A torre*: "A torre é uma montanha que alguém virou do avesso. Ou uma mina ao contrário. Cava-se para cima."
- *Rumores*: "Há uma toupeira dourada que aparece nas minas. O Tobias da cidade paga mil moedas. Eu pagava dois mil se ma trouxessem viva. Para lhe perguntar onde está o ouro." · "Lá em baixo, no 18, havia uma forja de anões. Ninguém entra lá há cento e trinta anos. Dizem que o portão tem um nome escrito."

### 1.2 Pedrito — aprendiz de ferreiro

| | |
|---|---|
| Voz | bips médios, rápidos, a gaguejar quando está entusiasmado |
| Quem é | 16 anos, órfão do posto, cresceu entre mineiros. Faz pregos e ferraduras na forja simples. Sonha aprender com o Brom ("o melhor ferreiro do mundo! dos dois mundos! dos três!") |

| ID | Condição | Fala |
|---|---|---|
| `pedrito_01` | — | "Fiz cem pregos hoje! Noventa estão tortos. Mas os dez direitos são MESMO direitos." |
| `pedrito_02` | — | "Conheces o Brom? O da cidade? Ele fez uma espada que cortou uma bigorna! Não sei se é verdade. Quero que seja." |
| `pedrito_03` | `arma_tipo == martelo` | "Um martelo! Posso pegar? Só pegar. Não bato em nada. Prometo." |
| `pedrito_04` | `missao(R2_13) == concluida` | *(na Forja do Brom, em Ascendia)* "Estou a varrer! Varri a forja quarenta vezes! Amanhã ele deixa-me segurar as tenazes!" |

### 1.3 Dona Graça — cozinheira

| | |
|---|---|
| Voz | bips redondos e calmos |
| Quem é | 70 anos, irmã da Dona Marta ("a Marta cozinha para heróis; eu cozinho para quem trabalha"). Vende Sopa de Mineiro; com 4 corações ensina a receita |
| Amizade | tem **corações** simples (só para a receita): +20 por conversa, +45 por presente de carne ou legumes |

| ID | Condição | Fala |
|---|---|---|
| `graca_01` | — | "Sopa de Mineiro! Quente, grossa, com pedras. Brincadeira. Com raiz-pedra. É parecido." |
| `graca_02` | — | "A minha irmã Marta escreve-me a dizer que tens bom apetite. Vamos ver." |
| `graca_03` | `vida_pct < 30` | "Senta-te. Come. Depois falas. É de família, esta frase." |
| `graca_04` | `coracoes(graca) >= 4` | "Toma. A receita. Não dês à Marta. Ela diz que a dela é melhor. A dela é melhor. Não lhe digas." |

### 1.4 Senhor Ruivo — mineiro velho

| | |
|---|---|
| Voz | bips lentos e roucos; fala para o lado errado (é meio cego) |
| Quem é | 82 anos, mineiro há 60. Já não vê bem, mas conhece os túneis pelo cheiro e pelo eco. Vende mapas dos túneis (desenhados de memória) |

| ID | Condição | Fala |
|---|---|---|
| `ruivo_01` | — | "Quem está aí? Cheiras a cidade. E a coragem. A coragem cheira a suor." |
| `ruivo_02` | — | "Os túneis do 12 mudam. Os goblins abrem e fecham portas. Mas a rocha não muda. Ouve a rocha." |
| `ruivo_03` | — | "Perdi quatro amigos no 12. Há trinta anos. Ninguém os foi buscar. Eu já não vejo para ir." |
| `ruivo_04` | `missao(R2_03) == concluida` | "Os diários. Leste-mos. Ouvi as palavras deles na tua voz. Obrigado. Agora já os posso esquecer em paz. Não. Nunca os vou esquecer. Em paz." |

### 1.5 Corrida de Vagonetas (R2_09)

| | |
|---|---|
| Onde | Estação de Vagonetas (andar 11) |
| Como | minijogo: a vagoneta anda nos carris; inclinar para os lados para apanhar cristais e baixar a cabeça nas vigas. Bifurcações escolhem o caminho |
| Recorde inicial | **58 s — Kai** (escrito a giz no quadro da estação) |

- **Hilda** *(ao começar)*: "Três, dois, um… VAI! E não vomites dentro da vagoneta!"
- *(menos de 60 s)* **Hilda**: "Pela minha picareta! Menos de um minuto!" *(se bateres o Kai)* "E bateste o rapaz do casaco azul! Vou apagar o nome dele com gosto."
- *(mais de 60 s)* **Hilda**: "Devagar demais. A minha avó fazia em setenta. Com setenta anos."

---

## 2. Mycélia, Cidade dos Fungoides (andar 16)

Primeira chegada: cena **C2-05**. Os fungoides falam **devagar**: há uma opção de **Acelerar** em todas as conversas
(o fungoide pisca os olhos, ofendido, mas não perde amizade). Aceitam **Cogumelos Luminosos** como dinheiro.

### 2.1 Ancião Gorro-Azul

| ID | Condição | Fala |
|---|---|---|
| `gorro_01` | — | "Filho… da… janela. Senta-te. Não há… pressa. Nunca há pressa… em Mycélia." |
| `gorro_02` | — | "A torre… respira. Ponho a raiz no chão… e ouço. Uma vez… por muito tempo." |
| `gorro_03` | — | "Os nossos avós… caíram aqui. Do céu deles… ficou só a luz. Nos nossos chapéus." |
| `gorro_04` | `missao(R2_07) == concluida` | "A cidade… brilha mais. Os pequenos… já não têm medo… do escuro de cima." |
| `gorro_05` | `missao(R2_06) == concluida` | "O Bolota… viu o sol. Escreveu-nos. Diz que o sol… é quente. E grande. E que lhe deu… espirros." |
| `gorro_06` | `boss_derrotado(golem_cristal)` | "O rei de pedra… ajoelhou-se. Nós sentimos… pelas raízes. Ajoelhou-se… a quem?" |

### 2.2 Pila — comerciante

| | |
|---|---|
| Loja | Esporos de Fungo Azul (sementes), Poção de Visão Noturna, Poção de Luz; aceita cogumelos (1 Cogumelo Luminoso = 5 ouro) |

| ID | Condição | Fala |
|---|---|---|
| `pila_01` | abrir loja | "Trocas… trocas. Cogumelos… por coisas. Coisas… por cogumelos." |
| `pila_02` | comprar | "Bom… negócio. Para os dois. Mais… para mim." |
| `pila_03` | pagar em ouro | "Moedas… redondas… brilham… mas não se comem. Aceito… na mesma." |

### 2.3 Mestre Lamela — professor de cogumelos

| ID | Condição | Fala |
|---|---|---|
| `lamela_01` | — | "Há… trezentos e doze… cogumelos. Duzentos e cinco… comem-se. Os outros… comem-te a ti." |
| `lamela_02` | ensinar receita | "Pão de Fungo. Farinha… e fungo azul. Coze-se… devagar. Como tudo… o que é bom." |
| `lamela_03` | — | "Os teus cogumelos de cima… são tristes. Não brilham. Não cantam. Coitados." |

### 2.4 Bolota — jovem fungoide

| | |
|---|---|
| Voz | bips agudos e **rápidos** (o único fungoide que fala depressa: os outros acham-no "agitado") |
| Quem é | fungoide jovem, curioso, quer ver o sol. Depois de R2_06 vive na quinta da Hana |

| ID | Condição | Fala |
|---|---|---|
| `bolota_01` | `missao(R2_06) != concluida` | "O SOL! Como é o sol? É redondo? Brilha mais do que os chapéus? Queima? Queima POUCO?" |
| `bolota_02` | `missao(R2_06) != concluida` | "O Ancião diz que o sol faz mal aos fungoides. O Ancião diz isso de tudo. Até da pressa." |
| `bolota_03` | `missao(R2_06) == concluida` | *(na quinta da Hana)* "VI O SOL! Espirrei! A Hana diz que é alergia! É FELICIDADE!" |
| `bolota_04` | `missao(R2_06) == concluida` | *(na quinta)* "Planto fungos à sombra do celeiro! Vendo! Queres fungo? Fungo azul? É o melhor fungo de cima!" |

---

## 3. Fantasmas da Forja Anã (andar 18)

Só se veem **com luz** (as 3 fornalhas acesas). Primeira chegada: cena **C2-07**.

### 3.1 Ferreiros Fantasmas

| ID | Condição | Fala |
|---|---|---|
| `fferreiro_01` | — | "Martela… martela… o ferro não espera. Mesmo morto, o ferro não espera." |
| `fferreiro_02` | — | "Forjávamos para números. 4 112. 7 680. 9 961. Nunca vimos as caras." |
| `fferreiro_03` | abrir loja | "Lingotes antigos. Ferro de antes. Ferro de quando as forjas cantavam." |
| `fferreiro_04` | `missao(R2_05) == concluida` | "O filho do Grimbold mandou-te. Sentimos. As forjas aquecem quando um Martelo-Forte se lembra delas." |

### 3.2 Grimbold Martelo-Forte (missão R2_05)

| | |
|---|---|
| Voz | bips muito graves, com eco de caverna; fala devagar e com orgulho |
| Quem é | o pai do Brom. Mestre da Forja Anã. Morreu há 130 anos a segurar o Grande Portão para os outros fugirem, quando a **mina profunda acordou** (os Golens de Ferro do **Rei Anão Esquecido**, ver a masmorra). Fechou o portão com o nome do filho |
| Onde | Câmara do Mestre, ao pé de uma bigorna com um martelo partido |

**Conversa** (`cena_grimbold`, com R2_05 ativa e as 3 fornalhas acesas)

- 🎬 O fantasma de Grimbold está a martelar uma espada que não existe. Para quando o herói entra.
- **Grimbold** *(normal)*: "Tu outra vez. Não és o meu rapaz. Mas cheiras à forja dele. A carvão e a mau feitio."
- **Grimbold** *(surpresa)*: "Foi ele que te mandou? O Brom? O meu Brom está vivo?"

▶ **"Está vivo. Tem uma forja em Ascendia."**

- **Grimbold** *(feliz)*: "Uma forja! Claro que tem uma forja! Os Martelo-Forte não sabem fazer outra coisa."
- **Grimbold** *(triste)*: "Há cento e trinta anos a mina profunda acordou. Os golens do rei esquecido subiram pelas escadas. Tudo a arder."
- **Grimbold** *(normal)*: "Mandei toda a gente fugir pelo portão. O Brom tinha dez anos. Não queria ir. Atirei-o lá para fora pela gola."
- **Grimbold** *(normal)*: "Depois fechei o portão por dentro. Com as runas do nome dele. Só um Brom, ou quem um Brom mandasse, o voltaria a abrir."
- **Grimbold** *(feliz)*: "E o portão aguentou. Os golens nunca passaram. Ficaram lá em baixo, a dormir."

▶ **"O Brom nunca soube o que te aconteceu."**
▶ **"Ele ainda tem saudades tuas."**

- **Grimbold** *(triste)*: "Pois. Era melhor assim. Se soubesse, voltava. E morria aqui comigo. Os filhos não devem voltar às portas que os pais fecham."
- **Grimbold** *(normal)*: "Leva-lhe o meu martelo. O Forte-Rocha. Está partido. Ele arranja. Ele arranja tudo, aquele rapaz. Até o que não tem arranjo."
- **Grimbold** *(feliz)*: "E diz-lhe… diz ao meu rapaz que o portão aguentou. E que eu o ouvia cantar. Todas as manhãs, na forja. Cantava mal. Cantava como a mãe."
- 🎬 O fantasma pousa a mão no martelo partido. Fica mais transparente.
- **Grimbold** *(normal)*: "Agora posso descansar. Cento e trinta anos é muito tempo para segurar uma porta."
- 🎬 Desaparece em faíscas, como uma brasa a apagar-se.

⚙ Recebe o **Martelo Forte-Rocha** (item de missão). O resto da missão está em `docs/dialogos/brom.md` (secção 9).
⚙ Os Ferreiros Fantasmas passam a ter a fala `fferreiro_04`.

---

## 4. Missões da região, passo a passo

### R2_01 — Tochas para Todos
| | |
|---|---|
| Quem dá | Hilda (andar 11) |
| Recompensa | 200 ouro · 10 Tochas · Giz de Mineiro |

1. **Pedir** — **Hilda**: "Estamos sem carvão. Sem carvão não há tochas. Sem tochas, os rapazes trabalham às apalpadelas. Traz-me vinte."
2. **Passo**: entregar **20 Carvão** (veios pretos dos andares 11, 12 e 18; drop de Kobold).
3. **Entregar** — **Hilda** *(feliz)*: "Vinte! Os rapazes vão poder ver o que partem! Toma: tochas e um giz. Marca as paredes. Nunca te percas."

### R2_02 — O Gancho
Dada pelo **Gizmo** (Ascendia). Falas em `docs/dialogos/gizmo.md`. Engrenagens: drop de Goblin Mineiro (20%) e Kobold (30%).

### R2_03 — Mineiros Perdidos
| | |
|---|---|
| Quem dá | Senhor Ruivo (andar 11) |
| Recompensa | Mapa dos Túneis (mostra o labirinto do andar 12) · 400 ouro |

1. **Pedir** — **Senhor Ruivo**: "Quatro amigos meus ficaram no 12. Cada um tinha um diário. Traz-mos. Quero ouvir o que escreveram."
2. **Passos**: encontrar os **4 diários** no andar 12:
   - 3 no **Acampamento Perdido** (cena C2-02), junto aos esqueletos — cada um tem um **número** escrito na última página (são o código do cofre do capataz: segredo do andar);
   - o 4.º na **Galeria Inundada**, dentro de um capacete a flutuar (é preciso esvaziar a galeria rodando uma bomba de água).
3. **Entregar** — 🎬 o Senhor Ruivo pede ao herói que leia. O herói lê (o texto aparece). Ao 4.º diário, o velho chora.
   - **Senhor Ruivo**: "O Zé escrevia mal. Sempre escreveu mal. Até ao fim. Obrigado." ⚙ Mapa dos Túneis · 400 ouro · os nomes vão para a tábua do posto (`hilda_07`)

### R2_04 — Resgate no Ninho
| | |
|---|---|
| Quem dá | Capitã Freya (Ascendia, rank D) |
| Recompensa | 600 ouro · 30 pontos de Guilda · os 3 aventureiros vão viver para Ascendia (dão aulas na Escola de Aventureiros, quando existir) |

1. **Pedir** — **Freya**: "Três aventureiros da Guilda estão presos em casulos no ninho das aranhas, no 15. Vivos, espero. Traz-mos."
2. **Passos**: no andar 15, encontrar os **3 casulos que gemem** (Casulos e Câmara dos Ovos) e rasgá-los (bater 5 vezes; a Aranha-Mãe não pode estar a ver: se estiver na mesma sala, desce do teto).
   - Os 3: **Dália** (arqueira), **Ivo** (espadachim), **Brás** (curandeiro).
3. **Entregar** — os três voltam a Ascendia sozinhos depois da Aranha-Mãe (cena C2-04). **Freya** *(feliz, raro)*: "Três para três. Ninguém ficou para trás. É assim que se faz."

### R2_05 — O Martelo do Pai
Dada pelo **Brom** (6 ❤️). Falas do Brom em `docs/dialogos/brom.md`; a conversa com o fantasma está na secção 3.2 acima.

### R2_06 — Bolota Quer Ver o Sol
| | |
|---|---|
| Quem dá | Bolota (Mycélia) |
| Recompensa | o Bolota vive na quinta da Hana · Esporos de Fungo Azul ×10 |

1. **Pedir** — **Bolota**: "Leva-me lá acima! Ao SOL! O Ancião diz que não! Mas o Ancião diz que não a tudo! Leva-me!"
   - ▶ **"Tens a certeza?"** → "TENHO! Tenho a certeza há trinta anos!"
2. **Passos** (escolta):
   - o Bolota segue-te do andar 16 até ao cristal (se levar dano 3 vezes, encolhe-se e tens de lhe dar um Cogumelo Luminoso para continuar);
   - em Ascendia, **não o deixes ao sol** mais de 10 s seguidos (a barra "Sol" do Bolota aparece por cima dele): leva-o pela sombra até à quinta da Hana.
3. **Entregar** — cena curta na quinta: o Bolota vê o céu, espirra, e chora de alegria. A Hana adota-o (`docs/dialogos/hana.md`, secção 9).

### R2_07 — Luz para Mycélia
| | |
|---|---|
| Quem dá | Ancião Gorro-Azul |
| Recompensa | receita Poção de Visão Noturna |

1. **Pedir** — **Ancião**: "A luz… da cidade… está fraca. Os chapéus velhos… apagam-se. Trinta… cogumelos luminosos… dão luz… para os pequenos."
2. **Passo**: entregar **30 Cogumelo Luminoso** (andares 2, 4 e 16).
3. **Entregar** — 🎬 os fungoides comem os cogumelos e os chapéus deles acendem-se todos, mais fortes. A cidade inteira brilha.

### R2_08 — A Cor Violeta
Dada pelo **Velho Fausto**. Falas em `docs/dialogos/fausto.md`.

### R2_09 — Corrida de Vagonetas
Ver secção 1.5. Recompensa: **Capacete de Mineiro** (luz própria de 4 m) · 300 ouro.

### R2_10 — O Rei Goblin
| | |
|---|---|
| Quem dá | quadro da Guilda (rank D) — dada pela Freya (`docs/dialogos/freya.md`) |
| Recompensa | 900 ouro · Coroa de Latão |

1. **Quadro** — `"PROCURA-SE: Rei Goblin Gruk. Coroa de latão, martelo de vagoneta, mau hálito. Assalta mineiros nos andares 11, 12 e 18."`
2. **Passo**: vencer o **Rei Goblin Gruk** (3%; 15% com a missão ativa; 50% durante uma Invasão Goblin no Posto).
3. **Ao aparecer** — **Gruk** *(zangado, voz goblin)*: "GRUK É REI! Rei de tudo o que brilha! Tu brilhas? Não? Então sai!"

### R2_11 — A Toupeira Dourada
Dada pelo **Tobias** (Ascendia). Falas em `docs/dialogos/tobias.md`. A toupeira **não ataca**: foge debaixo do chão; tens 30 s para a atordoar.

### R2_12 — O Outro Eu
Dada pela **Madame Oriel**. Falas em `docs/dialogos/oriel.md`. Vencer o **Reflexo Negro** (guardião do andar 19) sem poções.

### R2_13 — Aprendiz do Brom
| | |
|---|---|
| Quem dá | Pedrito (andar 11) |
| Recompensa | o Pedrito trabalha na Forja do Brom: melhorias +1 a +5 20% mais baratas |

1. **Pedir** — **Pedrito** *(a gaguejar)*: "Le-levas-me à cidade? Ao Brom? Eu faço qualquer coisa! Varro! Carrego! Sou bom a carregar!"
2. **Passo 1**: levar o Pedrito pelo cristal até Ascendia (ele segue-te).
3. **Passo 2**: convencer o Brom (escolha de diálogo, em `docs/dialogos/brom.md`).
4. **Entregar** — **Hilda** (depois, no posto): "O miúdo foi? Ainda bem. Eu ensinava-o a cavar. O Brom ensina-o a ser alguém."

### R2_14 — Sopa de Mineiro
| | |
|---|---|
| Quem dá | Dona Graça (andar 11, 4 corações com ela) |
| Recompensa | receita Sopa de Mineiro |

1. **Pedir** — **Dona Graça**: "Queres a receita? Traz-me os ingredientes uma vez. Cinco carnes, cinco raízes-pedra e um cogumelo que brilhe. Faço-a contigo."
2. **Passo**: entregar **5 Carne + 5 Raiz-Pedra + 1 Cogumelo Luminoso**.
3. **Entregar** — 🎬 cozinham juntas (corte rápido). **Dona Graça** *(feliz)*: "Agora sabes. Não digas à Marta que te ensinei. Diz que adivinhaste."

---

## 5. Missões da Guilda (rank D) da região

Os objetivos e recompensas estão em `docs/MISSOES.md` (secção 3). Aqui ficam o texto do quadro e as falas da Lyra.

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_D_01 Goblins na Mina | "Goblins Mineiros roubam minério nos andares 11 e 12. Afastar 15. A Hilda agradece. Aos gritos." | "Goblins! Cuidado com os bolsos. Eles roubam tudo o que brilha. Até botões." | "Quinze! A Hilda escreveu: 'Finalmente.' É o elogio mais comprido que ela já mandou." |
| G_D_02 O Rei Goblin (R2_10) | ver a missão R2_10 (secção 4) | "O Rei Gruk! Diz-se que tem mau hálito. Não respires perto dele. Ou respira pouco." | "A coroa de latão! Vou pô-la na vitrine da Guilda. Ao lado da do Slime Rei. Temos uma coleção de coroas!" |
| G_D_03 Seda para a Elva | "A costureira Elva precisa de 15 Seda de Aranha. Andar 15. Cuidado com o teto." | "Seda de aranha! A Elva faz mochilas com ela. Mochilas que não rasgam. Nunca. Já experimentei com uma tesoura." | "A Elva disse que a seda está perfeita. E fez-te uma mochila maior. Disse que era 'para caberes mais tralha'." |
