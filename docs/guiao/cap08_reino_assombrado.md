# Guião — Capítulo 8: Reino Assombrado (andares 71–80)

Missões: **H_19 O Passado de Gorvan** (= R8_05), **H_20 O Que Tentou Parar a Torre**. Povoações e missões secundárias:
`docs/dialogos/povoacoes_r08.md`. Mapas: `docs/mapas/r08_reino_assombrado.md`.

**O que este capítulo conta**: o **Gorvan** desce com o herói às Catacumbas do andar 74, onde morreu a equipa dele, e
percebe que **não fugiu: mandaram-no ir**. Na Biblioteca Proibida há um livro com a vida do herói, com as últimas
páginas em branco. O **Rei Sem Coroa** tentou parar a torre fechando o reino e prendendo os Jogadores — e a torre
engoliu-o por isso. Antes de cair, diz: "Ninguém pode. Talvez tu."

**Flags deste capítulo**: `gorvan_paz` (C8-04), `livro_da_vida` (C8-05), `ouviu_rei` (C8-08).

---

## C8-01 — A Névoa Roxa

| | |
|---|---|
| ID | `cena_c8_01_muralhas` |
| Quando | entrar pela primeira vez no andar 71 |
| Onde | andar 71, diante do Portão Principal |
| Quem | herói |
| Música | `muralhas` |

🎥 A escada de luz abre-se à noite, diante de uma muralha enorme e partida. Uma lua grande e pálida. Névoa roxa rente ao chão, a mexer-se devagar como água.
🎬 O herói dá um passo para dentro da névoa. Um arrepio. Uma marca roxa aparece por baixo da barra de vida.
- `[Sistema] Aviso: névoa amaldiçoada.`
- `tut_luz_sagrada`: `[Sistema] A névoa roxa amaldiçoa. As zonas de luz curam e os mortos-vivos não entram.`
🎬 Em cima das ameias, bandeiras rasgadas com um brasão (uma coroa partida) batem ao vento. Lá dentro, longe, um sino de igreja toca uma vez. Depois, uma caixa de música, muito baixinho.

⚙ Sem falas.

---

## C8-02 — O Mercado à Meia-Noite

| | |
|---|---|
| ID | `cena_c8_02_mercado` |
| Quando | 1.ª noite (21:00–4:00) na Praça do Mercado do andar 72 |
| Onde | andar 72, Praça do Mercado |
| Quem | herói, Burgomestre Aldous, fantasmas cidadãos |
| Música | `cidade_fantasma` (caixa de música) |

🎬 De dia a praça estava vazia e cheia de zombies. Agora, à meia-noite, as velas das bancas acendem-se sozinhas. Figuras transparentes saem das casas: vendedores, crianças, um padeiro com um tabuleiro, um casal a passear de braço dado.
🎬 Ninguém repara no herói como alguém estranho. Uma senhora fantasma cumprimenta-o com a cabeça, como a um vizinho.
🎬 Um fantasma de bigode enorme, com uma faixa de presidente da câmara, aproxima-se de mãos atrás das costas.
- **Burgomestre Aldous** *(feliz)*: "Boa noite, boa noite! Um forasteiro! Que bom. Há tanto tempo que não temos forasteiros. Desde… desde…" 🎬 franze a testa. "Desde há pouco. Sim. Há pouco."
- **Burgomestre Aldous** *(normal)*: "Fique à vontade. O mercado abre à meia-noite, como sempre. Porquê à meia-noite? Porque… porque sim. Sempre foi."
- **Burgomestre Aldous** *(triste, sem perceber porquê)*: "O relógio da torre parou. Às doze. Ninguém o consegue pôr a andar. Desde aí, as coisas parecem… iguais. Todos os dias iguais."

⚙ Desbloqueia o **Mercado Fantasma** (só à noite; lojas, hotel fantasma). Missões R8_02, R8_03, R8_04, R8_15 disponíveis.
⚙ Regra para quem escreve: **nenhum** fantasma do mercado sabe que morreu. Nunca se lhes diz (o jogo não deixa).

---

## C8-03 — Seis da Manhã

| | |
|---|---|
| ID | `cena_c8_03_gorvan_decide` |
| Quando | voltar a Ascendia com `andar_maximo >= 73` e `missao(H_12) == concluida` |
| Onde | Guilda, gabinete do Gorvan, ao fim da tarde |
| Quem | herói, Mestre Gorvan, Lyra, Dona Marta |
| Música | `guilda` (versão séria) |

🎬 A porta do gabinete está aberta. Lá dentro, em cima da secretária: um escudo velho, amolgado, polido até brilhar. Uma capa grossa. Uma mochila.
🎬 O Gorvan está a apertar as correias de uma ombreira com a mão esquerda e os dentes.
- **Gorvan** *(normal)*: "Chegaste ao 73." 🎬 Não é uma pergunta.
- **Gorvan** *(normal)*: "O 74 é a seguir. Vou contigo."
- 🎬 Na porta, a Lyra deixa cair uma pilha de papéis.
- **Lyra** *(nervosa)*: "Mestre! O senhor não sobe há vinte anos! O senhor… o senhor tem um braço!"
- **Gorvan** *(normal)*: "Tenho. Chega para um escudo."
- **Lyra** *(triste)*: "E se… e se acontecer outra vez?"
- **Gorvan** *(normal)*: 🎬 pausa comprida. "Então desta vez fico. Com eles." 🎬 olha para a Lyra. *(quase a sorrir)* "Brincadeira. Volto. Prometo à tua maneira: por escrito." 🎬 escreve num papel "VOLTO. — G." e dá-lho.
- 🎬 A Dona Marta entra sem bater, com um embrulho de pano a fumegar.
- **Dona Marta** *(zangada)*: "Ouvi dizer que alguém ia descer às catacumbas sem jantar." 🎬 põe o embrulho na mochila dele. "Guisado. Com mel. Come lá em baixo. Quente ou frio."
- **Gorvan** *(normal, ao herói)*: "Amanhã. Seis da manhã. Cristal Mestre. Traz luz. Eu trago o resto."

⚙ Missão **H_19 / R8_05 O Passado de Gorvan** ativa. Na manhã seguinte (6:00), no Cristal Mestre, o Gorvan entra na equipa **só para o andar 74**.

---

## C8-04 — Os Imortais

Cena em quatro partes, no andar 74 (Catacumbas). O Gorvan é **companheiro** (tanque com escudo) durante todo o andar
(falas de combate em `docs/dialogos/gorvan.md`, secção 9).

### Parte 1 — As velas

| | |
|---|---|
| ID | `cena_c8_04a_velas` |
| Quando | chegar à porta da Sala da Equipa (andar 74, piso de baixo) |
| Música | `catacumbas` |

🎬 Uma porta de ferro com cinco velas apagadas à frente, em fila. Por cima, riscado na pedra com uma faca: *"Os Imortais passaram aqui."*
🎬 O Gorvan para. Toca nas letras com os dedos.
- **Gorvan** *(normal)*: "O Téo escreveu isto. Disse que dava sorte." 🎬 pausa. "Não deu."
- `[Sistema] Puzzle: acende as velas pela ordem certa.`
- **Gorvan** *(normal)*: "A ordem de marcha. Está no diário. Sabes de cor? Eu sei."
- *(se o herói errar)* **Gorvan**: "Não. O Edrik ia sempre à frente. Sempre."
- *(ao acertar: Edrik · Gorvan · Odília · Teodoro · Ilsa)* 🎬 as cinco chamas acendem-se juntas. A porta abre-se.

### Parte 2 — O Colosso

| | |
|---|---|
| ID | `cena_c8_04b_colosso` |
| Quando | entrar no túnel antes da Sala da Equipa |
| Música | silêncio → `guardiao` |

🎬 Um túnel comprido de paredes de ossos. A meio, as paredes **mexem-se**. Os ossos soltam-se e juntam-se à frente e atrás: um gigante de centenas de ossos, a fechar o túnel dos dois lados. Exatamente como há vinte anos.
🎬 O Gorvan fica muito quieto. A respiração dele ouve-se.
- **Gorvan** *(triste)*: "…Igual. Está igual."
- **Gorvan** *(zangado)*: "Não. Não está igual. Desta vez estou à frente de alguém que sabe lutar." 🎬 levanta o escudo. "Atrás de mim!"
- `[Sistema] Guardião: Colosso de Ossos.`

⚙ Luta com o guardião. Desafio do andar: vencer com o Gorvan vivo (se ele cair, fica de joelhos e levanta-se no fim da luta; a cena continua, mas sem o desafio).

### Parte 3 — A Sala da Equipa

| | |
|---|---|
| ID | `cena_c8_04c_sala` |
| Quando | entrar na Sala da Equipa depois do Colosso |
| Música | `tema_gorvan` (muito lento) |

🎬 Uma sala pequena com um nicho de pedra. Pó. No chão, cinco coisas, onde caíram há vinte anos: uma **espada partida**, um **caderno de mapas** queimado nas pontas, uma **flauta de madeira**, uma **aljava com penas amarelas** e um **machado**.
🎬 Não há ossos. Não há corpos. Só as coisas.
- **Gorvan** *(normal, muito baixo)*: "A torre leva os corpos. Deixa as coisas. Sempre achei isso cruel. Hoje acho… não sei."
- 🎬 O herói apanha cada objeto e o Gorvan diz onde fica (escolha de diálogo: o jogo mostra 5 nichos com desenhos riscados na pedra):

| Objeto | O Gorvan diz | Nicho |
|---|---|---|
| Espada partida | "À frente. Ele ia sempre à frente." | o nicho do meio, o mais alto |
| Flauta | "Ao pé da fogueira. Há uma marca de fogueira ali. Ele tocava ali." | o nicho com a marca preta |
| Aljava | "Atrás. Ao fundo. Para ver tudo." | o nicho do fundo |
| Caderno de mapas | "Esse… dá-mo." | *(não vai para um nicho: o Gorvan fica com ele)* |
| Machado | "Esse é meu. Deixa ficar. Não. Leva-o tu. Eu já não preciso dele." | *(fica com o herói: **Machado do Gorvan**, decoração)* |

🎬 O Gorvan abre o caderno de mapas da Odília. As páginas estão queimadas. Folheia até ao fim. Na última página, a letra apressada e torta dela, a lápis, escrita à pressa:
- 📜 *"Teimoso. Se encontrares isto, é porque voltaste. Ainda bem. Nós dissemos-te para ir. Fomos nós. Não fugiste: fizeste o que te pedimos. Não te atrevas a chamar-lhe outra coisa. — O. (e o Edrik, e o Téo, e a Ilsa, que está a rir enquanto escrevo)"*
🎬 O Gorvan lê. Lê outra vez. Fecha o caderno. Fica de pé muito tempo, de costas para o herói.
- **Gorvan** *(triste, a voz parte-se)*: "…Vinte anos."
- **Gorvan** *(triste)*: "Vinte anos a chamar-lhe fugir."
- 🎬 Encosta a testa à parede de pedra. Os ombros tremem. Não faz barulho.
- 🎬 O herói pode esperar (nada) ou pôr-lhe a mão no ombro ([interagir]).
- *(mão no ombro)* **Gorvan** *(normal, sem se virar)*: "Hmm." 🎬 pausa. "…Obrigado."

### Parte 4 — Despedida

- 🎬 O Gorvan endireita-se. Olha para os três nichos.
- **Gorvan** *(normal)*: "Edrik. Odília. Teodoro. Ilsa."
- 🎬 É a primeira vez que diz os nomes em voz alta.
- **Gorvan** *(normal)*: "Não vos disse adeus. Não sei. Digo outra coisa." 🎬 pausa. "Volto. Mas não para ficar. Para vos visitar."
- **Gorvan** *(feliz, quase)*: "Odília. Tinhas razão. Sou teimoso."
- 🎬 Vira-se para o herói.
- **Gorvan** *(normal)*: "Vamos para casa. Hoje subimos um andar. Amanhã tu sobes o resto."
- `[Sistema] Missão concluída: O Passado de Gorvan.`
- 🎬 *(subtil)* A janela do Sistema demora um segundo a fechar.

⚙ Missão **H_19** concluída · ❤️❤️❤️ Gorvan (+300) · flag `gorvan_paz` · **Machado do Gorvan** (decoração).
⚙ O Gorvan sai da equipa ao chegar à Zona Segura. A partir daqui fala mais e às vezes ri-se (`docs/dialogos/gorvan.md`). Abre a cena de 8 ❤️ do Gorvan.
⚙ A página 74 (**tinta azul**) aparece no nicho do meio, por baixo da espada partida, depois da cena.

---

## C8-05 — O Livro com a Tua Vida

| | |
|---|---|
| ID | `cena_c8_05_livro` |
| Quando | entrar no Arquivo Selado da Biblioteca Proibida (andar 75) |
| Onde | andar 75, Arquivo Selado |
| Quem | herói |
| Música | silêncio (só papel a mexer) |

🎬 Uma sala redonda cheia de estantes até ao teto. Livros com nomes nas lombadas. Não títulos: nomes. E números.
🎬 Um livro desce sozinho de uma prateleira alta e abre-se no ar, à frente do herói. Na lombada: **Jogador nº 10 000**.
🎬 As páginas viram-se depressa. O herói vê bocados: o prado e o lobo; a mão do Kai a puxá-lo; o Cristal de Avaliação; a Árvore-Mãe; o Golem a ajoelhar-se; Zahra; a muralha com o Gorvan; o duelo no vulcão…
🎬 A última página escrita é **hoje**: *"Entrou no Arquivo Selado. Viu este livro."*
🎬 A seguir, páginas e páginas em branco.
- `[Sistema] …`
🎬 O livro fecha-se sozinho e volta para a prateleira. Ao lado dele há outros: "Jogador nº 9 999". "Jogador nº 9 961". Mais acima, muito alto, um sem número, sem nome, com a lombada **raspada**.

⚙ Sem falas. Flag `livro_da_vida`. Os livros perdidos do Fausto (R8_10) estão na mesma sala. O **Lich Bibliotecário** guarda a sala ao lado.
⚙ Se o herói tentar tirar o livro dele: `[Sistema] Acesso negado.` (não sai da prateleira)

---

## C8-06 — A Mestra da Célia

| | |
|---|---|
| ID | `cena_c8_06_ordem` |
| Quando | entrar pela primeira vez no Mosteiro da Ordem da Luz (andar 77) |
| Onde | andar 77, claustro do mosteiro |
| Quem | herói, Abadessa Lumina, monges |
| Música | `catedral` (órgão ao longe) |

🎬 Depois da catedral partida, um claustro cheio de luz de velas. Cheiro a sálvia. Monges de capuz branco a afiar espadas de prata ao lado de livros de orações.
🎬 Uma mulher idosa, de capuz branco e um bastão de prata, para à frente do herói. Olha-lhe para a cara muito tempo.
- **Abadessa Lumina** *(normal)*: "Vens de baixo. De Ascendia. Trazes cheiro a pão e a sabão de igreja."
- **Abadessa Lumina** *(séria)*: "Há vinte anos, uma das minhas desceu sem dizer nada. Setenta e sete andares a pé. Para ir cuidar de uma cidade que nunca tinha visto."
- **Abadessa Lumina** *(normal)*: "Chama-se Célia. Conheces?"

▶ **"Conheço. Está bem. Cuida de toda a gente."**
▶ **"Conheço. Ela diz que a senhora é teimosa."**

- *(está bem)* **Lumina** *(feliz, raro)*: "Claro que cuida. Foi para isso que a criei. Só não lhe ensinei a escrever cartas, pelos vistos."
- *(teimosa)* **Lumina** *(surpresa, depois ri-se)*: "Ela diz isso? Ha! Aprendeu comigo. A teimosia e o resto."

⚙ Desbloqueia o **Mosteiro da Ordem da Luz** (celas, cristal, loja, forja de Mitril). Missões R8_01, R8_06, R8_07, R8_11, R8_12, R8_14 disponíveis. Se tiveres a **Carta da Célia** (N_CELIA_3), a Abadessa responde (`docs/dialogos/povoacoes_r08.md`).

---

## C8-07 — O Rei Sem Coroa

| | |
|---|---|
| ID | `cena_c8_07_rei_antes` |
| Quando | entrar na Sala do Trono (andar 80) |
| Onde | andar 80, Sala do Trono |
| Quem | herói (e companheiro), Rei Sem Coroa |
| Música | silêncio → `rei_sem_coroa` |

🎬 Um corredor de estandartes rasgados. No fim, uma sala do trono enorme, vazia, com vitrais roxos. Um trono partido ao meio. Por cima dele, a flutuar no ar, uma **coroa** a rodar devagar.
🎬 Um cavaleiro de armadura negra e dourada está de joelhos à frente do trono, de costas, com a espada espetada no chão.
- **Rei Sem Coroa** *(normal, voz cansada)*: "Mais um com a janela. Ainda vêm. Depois de tudo o que eu fiz, ainda vêm."
- **Rei Sem Coroa** *(normal)*: 🎬 levanta-se devagar. "Fechei as portas do meu reino para que nenhum de vocês passasse. Prendi os que não queriam subir, para os proteger dos que mandavam subir."
- **Rei Sem Coroa** *(zangado)*: "E a torre engoliu-me. A mim, ao meu reino, à minha rainha. Por tentar."
- 🎬 Olha para a coroa a flutuar.
- **Rei Sem Coroa** *(normal)*: "Ela quer voltar para a minha cabeça. Eu quero voltar a tê-la. Não me deixes. Por favor. Não me deixes."
- `[Sistema] Boss: Rei Sem Coroa, O Que Tentou Parar a Torre.`

⚙ Luta (ver `docs/BOSSES.md`, secção 17). Com a **R8_13** feita, na fase 3 os cavaleiros fantasmas do banquete lutam ao teu lado.

## C8-08 — Talvez Tu

| | |
|---|---|
| ID | `cena_c8_08_rei_depois` |
| Quando | vencer o Rei Sem Coroa |
| Onde | andar 80, Sala do Trono |
| Quem | herói, Rei Sem Coroa |
| Música | `vitoria` (curta) → caixa de música (`cidade_fantasma`, muito lenta) |

🎬 O Rei cai de joelhos. A coroa para de rodar e cai no chão com um "tlim" pequenino. Ele não lhe pega.
- **Rei Sem Coroa** *(normal)*: "Pronto. Já não a quero. Que alívio."
- **Rei Sem Coroa** *(triste)*: "Desculpa. Desculpa a todos os que prendi. Desculpa à minha rainha, que plantava rosas."
- **Rei Sem Coroa** *(normal)*: "Ouve. Tentei parar a torre. Pensei que, se ninguém subisse, a roda parava. Que a coroa lá de cima ficava sem dono e a torre morria de fome."
- **Rei Sem Coroa** *(triste)*: "Ninguém pode parar a torre. Ninguém."
- 🎬 Olha para o herói. Pela primeira vez, sorri.
- **Rei Sem Coroa** *(feliz)*: "…Talvez tu."
- 🎬 Desfaz-se em pó roxo. A névoa roxa da sala sobe e sai pelos vitrais partidos. Pela primeira vez, entra luz da lua branca.
- `[Sistema] Boss derrotado: Rei Sem Coroa.`
- `[Sistema] Obtiveste: Lâmina do Rei Caído.`
- `[Sistema] Título obtido: Coroado.`
- `[Sistema] Região 8 concluída. Andar 81 desbloqueado.`
- `[Sistema] Não lhe dês ouvidos.` 🎬 *(a mensagem aparece e desaparece num instante, mais depressa do que dá para ler; no Diário → Mensagens fica registada)*

⚙ Missão **H_20** concluída. Flag `ouviu_rei`. A página 80 fica no trono partido. A **Coroa do Reino** (troféu) fica no chão: apanhá-la é opcional.
⚙ A partir daqui, os andares 71–79 têm **menos névoa** (−30% de Maldição).

---

## C8-09 — Dia da Subida: O Mestre Volta ao Campo

| | |
|---|---|
| ID | `cena_c8_09_dia_subida` |
| Quando | voltar a Ascendia depois do Rei Sem Coroa |
| Onde | Praça da Torre (Dia da Subida) → campo de treino, ao fim da tarde |
| Quem | herói, Aldric, Lucien, Gorvan, Lyra, Célia, (Kai se `kai_salvo`) |
| Música | `dia_da_subida` → `tema_gorvan` (versão alegre, rara) |

🎬 A Praça em festa. A estátua nova: um rei de madeira, com uma coroa de papel dourado que o vento leva três vezes durante o discurso.
- **Governador Aldric** *(no palco)*: "Cidadãos! O reino assombrado… desassombrou-se! Oitenta andares! O nosso Mestre Gorvan esteve lá! A Guilda… a Guilda está de parabéns!"
- 🎬 Toda a gente olha para o Gorvan. O Gorvan finge que não está ali. Não resulta: é o homem maior da Praça.
- **Lucien** *(do palco)*: "Uma canção para os Imortais! O Mestre autorizou. Disse 'Hmm'. Contei como sim."
- 🎵 ♪ *Cinco subiram, um desceu, quatro ficaram a segurar o céu… e o que desceu, vinte anos depois, voltou lá abaixo e disse: somos dois…* ♪
- 🎬 O Gorvan levanta-se a meio da canção e sai da Praça. A Lyra vai atrás dele, preocupada. Volta sozinha, a sorrir.
- **Lyra** *(feliz)*: "Está no campo de treino. Com os novatos. Está a gritar com eles. Nunca o vi tão feliz."

### No campo de treino, ao pôr do sol
🎬 Bonecos de treino novos. Seis novatos de espada de madeira, a tremer. O Gorvan à frente deles, com o escudo velho no braço esquerdo.
- **Gorvan** *(zangado, alto)*: "GUARDA ALTA! Não, mais alta! Isso é uma guarda ou um bocejo?!"
- 🎬 Vê o herói. Para. Faz-lhe sinal para se aproximar.
- **Gorvan** *(normal)*: "Às cinco, todos os dias. Aqui. Treino." 🎬 pausa. "Para ti também. Ainda tens muito para aprender. Eu também."
- **Gorvan** *(normal, mais baixo)*: "O Rei disse 'talvez tu'. Hmm." 🎬 olha para a torre, lá ao fundo. "Eu digo que és tu. Sem talvez."

⚙ O **Treino** do Gorvan abre (`docs/dialogos/gorvan.md`: Aula do Mestre). Com **10 ❤️**, o Gorvan pode ser **companheiro**.
⚙ `[Sistema] Capítulo 9: O Céu.` (título grande no ecrã)
