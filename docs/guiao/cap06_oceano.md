# Guião — Capítulo 6: Oceano (andares 51–60)

Missões: **H_14 Fantasmas do Navio** (= R6_05), **H_15 O Último do Mar**. Povoações e missões secundárias:
`docs/dialogos/povoacoes_r06.md`. Mapas: `docs/mapas/r06_oceano.md`.

**O que este capítulo conta**: o mar é o sítio mais bonito da torre e o capítulo mais triste até aqui. No Navio
Fantasma, o herói liberta **cinco Jogadores antigos** que nunca saíram. O diário de bordo fala de Jogadores que subiam
"para o Administrador" — e o **último registo é do Kai**, que desaparece. Em Coralina, a cidade das sereias, ouve-se
falar de um rapaz que, há muito tempo, subiu com "um da janela" e nunca voltou (o **Nereu**, amigo do Aren — ninguém
liga as duas coisas). O Leviatã não quer lutar: é o **Sistema** que o obriga.

**Flags deste capítulo**: `fantasmas_livres` (C6-04), `kai_desaparecido` (C6-05), `ouviu_nereu` (C6-07).

---

## C6-01 — O Mar

| | |
|---|---|
| ID | `cena_c6_01_praia` |
| Quando | entrar pela primeira vez no andar 51 |
| Onde | andar 51, Areal Branco |
| Quem | herói |
| Música | `praia` |

🎥 A escada de luz abre-se numa praia de areia branca. Mar turquesa até ao horizonte. Palmeiras. O som das ondas. Depois do gelo, a luz quase cega.
🎬 O herói fica parado. Tira as botas. Anda até à água. As ondas molham-lhe os pés.
- `[Sistema] Nova região: Oceano.`
🎬 Na areia molhada, perto das rochas, há letras grandes escritas com um pau, meio apagadas pelas ondas:
- *"KAI ESTEVE AQUI. Nº 9 999. ATRASAD{O/A}!"*
🎬 Ao lado, uma seta a apontar para o mar. A onda seguinte apaga metade.
- `tut_ar`: *(só ao entrar na água funda pela primeira vez)* `[Sistema] Debaixo de água tens uma barra de Ar. Sem ar, perdes vida. Procura bolhas.`

⚙ Sem falas.

---

## C6-02 — O Porto dos Piratas Reformados

| | |
|---|---|
| ID | `cena_c6_02_porto` |
| Quando | entrar pela primeira vez no Porto Arquipélago (andar 52) |
| Onde | andar 52, cais do porto |
| Quem | herói, Capitã Marisa Vento-Sul, Tiago |
| Música | `porto_piratas` |

🎬 Casas coloridas em cima de estacas. Redes a secar. Gaivotas. Um rapaz (Tiago) a correr pelo cais com um balde de peixe.
🎬 Uma mulher de chapéu de três bicos e um olho de vidro está sentada num barril, a afiar uma faca. Olha o herói de cima a baixo com o olho bom.
- **Capitã Marisa** *(normal)*: "Mais um de casaco seco. Os da escada chegam sempre secos e saem sempre molhados."
- **Capitã Marisa** *(normal)*: "Marisa Vento-Sul. Mando no porto. Fui pirata. Agora sou mercadora. É a mesma coisa com menos facadas."
- **Capitã Marisa** *(séria)*: "Há uns dias passou por cá um rapaz de casaco azul. Alugou o meu bote mais rápido e pagou o dobro. Perguntou pelo **navio fantasma**, no 53."
- **Capitã Marisa** *(séria)*: "Ninguém vai ao navio fantasma. Disse-lhe isso. Ele riu-se e disse: 'Então vou ser o primeiro.' O bote ainda não voltou."

▶ **"É o Kai. Tenho de ir atrás dele."**
▶ **"Ele sabe tomar conta de si."**

- *(atrás dele)* **Marisa** *(normal)*: "Então precisas de um barco. Não te empresto o meu. Mas há um velho no estaleiro que, com madeira e paciência, ainda flutua."
- *(sabe)* **Marisa** *(normal)*: "Toda a gente sabe tomar conta de si até ao dia em que não sabe. Precisas de um barco na mesma. Há um velho no estaleiro."

⚙ Desbloqueia o **Porto Arquipélago**. Missão **R6_01 Um Barco para Ti** ativa (o barco é preciso para chegar ao navio do andar 53). `[Sistema] Missão: arranja um barco.`

---

## C6-03 — O Navio no Nevoeiro

| | |
|---|---|
| ID | `cena_c6_03_navio` |
| Quando | chegar de barco ao Navio Fantasma (andar 53) |
| Onde | andar 53, Mar de Nevoeiro → Convés |
| Quem | herói, fantasmas |
| Música | silêncio → `capitao_esqueleto` (versão lenta, sem percussão) |

🎬 Nevoeiro verde. O barco do herói avança devagar. O mar está parado como um espelho.
🎬 Uma sombra enorme aparece no nevoeiro: um galeão encalhado num banco de areia, inclinado, velas rasgadas, lanternas verdes a balançar.
🎬 Encostado ao casco, o **bote da Capitã Marisa**, vazio, preso por uma corda.
🎬 O herói sobe pela escada de corda. No convés, figuras transparentes a fazer coisas: um a esfregar o chão, outro a dar nós numa corda, outro sentado a olhar para o mar. Todos com uma **janela azul pálida** por cima da cabeça, com um número.
- `[Sistema] Detetados: 5 Jogadores. Estado: ——.`
🎬 Os fantasmas param e olham para o herói ao mesmo tempo.
- **Fantasma nº 8 820** *(feliz, voz com eco)*: "Um novo! Bem-vindo a bordo! Estamos quase a partir. Amanhã, de certeza. Subimos amanhã!"

⚙ Missão **H_14 Fantasmas do Navio** ativa. `[Sistema] Missão: liberta os Jogadores do navio.`

---

## C6-04 — Os Cinco

Cada fantasma está preso a uma coisa que não acabou. Ajudar cada um (por qualquer ordem) liberta-o: o fantasma diz a
última frase, sorri e **segue em frente** (fica luz, depois nada). Ao libertar os cinco, flag `fantasmas_livres`.

### Nº 312 — o marinheiro da canção

| | |
|---|---|
| Quem era | o Jogador mais antigo a bordo: chegou há uns **900 anos**. Pescador no mundo dele. Desistiu de subir no andar 52 e ficou no navio a cantar |
| Onde | ao leme, a cantar sempre a mesma estrofe |
| O que falta | o fim da canção: esqueceu-se do último verso |

- **Nº 312** *(normal, a cantar)*: "♪ Ó mar que me levas, ó mar que me tens… ♪ …e depois? Há novecentos anos que não me lembro do depois."
- **Passo**: encontrar o resto da canção. Está escrito na porta do porão 2, riscado com uma faca, por ele mesmo, antes de morrer.
- ▶ *(cantar o verso)* **Herói** *(o texto aparece)*: "♪ …leva-me a casa, que é lá que me esperam os meus. ♪"
- **Nº 312** *(feliz)*: "Isso! Os meus! Era isso!" 🎬 desaparece a cantar.

### Nº 1 450 — a mulher da carta

| | |
|---|---|
| Quem era | professora no mundo dela. Escreveu uma carta à filha todos os dias, durante seis anos de torre |
| Onde | sentada num caixote do convés, a escrever no ar com uma pena que não tem tinta |
| O que falta | que alguém leia a última carta em voz alta |

- **Nº 1 450** *(triste)*: "A minha última carta. Está na minha arca, no porão. Nunca a mandei. Não há correio na torre. Lês-ma? Em voz alta. Uma vez. Só para ela existir."
- **Passo**: trazer a **carta** da arca dela (porão 1, atrás de barris que rolam).
- 🎬 O herói lê (o texto aparece): *"Inês. Hoje vi o mar. Lembrei-me de ti a fugir das ondas. Ainda tenho medo de que te esqueças da minha cara. Eu não me esqueço da tua. Nunca. A mãe."*
- **Nº 1 450** *(feliz, a chorar)*: "Pronto. Agora existe." 🎬 desaparece.

### Nº 3 377 — o rapaz sem nome

| | |
|---|---|
| Quem era | um rapaz de 14 anos. Morreu tão depressa que nunca chegou a dizer o nome a ninguém na torre. Agora esqueceu-se dele |
| Onde | encolhido na proa, a abraçar os joelhos |
| O que falta | o nome |

- **Nº 3 377** *(triste)*: "Toda a gente me chama três mil trezentos e setenta e sete. Eu tinha um nome. Juro que tinha. Começava por… não sei."
- **Passo**: no porão 3, a mochila dele (com um caderno da escola). Na capa, o nome: **Duarte**.
- ▶ **"Chamas-te Duarte."**
- **Duarte** *(surpresa, depois feliz)*: "Duarte. DUARTE! A minha avó chamava-me Duartinho. Odiava. Agora gosto." 🎬 desaparece a rir.

### Nº 6 001 — o soldado que não se rendeu

| | |
|---|---|
| Quem era | soldado no mundo dele. Jurou "nunca me render" e morreu a lutar contra o Imediato, que o prendeu ao navio |
| Onde | a guardar a porta da Cabine do Capitão, de espada na mão |
| O que falta | descansar (precisa que alguém vença o Imediato por ele) |

- **Nº 6 001** *(zangado)*: "Ninguém passa! O Imediato ainda anda por aí. Enquanto ele andar, eu fico de guarda. Jurei."
- **Passo**: vencer **O Imediato Fantasma** (guardião do andar, no porão 3).
- **Nº 6 001** *(normal)*: "Caiu? Caiu mesmo?" 🎬 pousa a espada no chão. "Então posso parar. Que cansaço, Jogador. Que cansaço." 🎬 desaparece. A porta da Cabine fica livre.

### Nº 8 820 — o que ainda não sabe

| | |
|---|---|
| Quem era | o mais novo a bordo: chegou há cerca de **cem anos**. Rapaz alegre, sempre "quase a partir". **Não sabe que morreu** |
| Onde | em todo o lado: corre pelo convés a preparar a partida |
| O que falta | perceber |

- **Nº 8 820** *(feliz)*: "Já tenho a mochila feita! Amanhã subimos. O capitão disse. Ele diz isso todos os dias, mas amanhã é a sério!"
- **Passo**: só depois dos outros quatro. Ele repara que o navio está vazio.
- **Nº 8 820** *(surpresa)*: "Onde foram todos? Partiram sem mim?"

▶ **"Partiram. Tu também podes ir."**
▶ **"Olha para as tuas mãos."**

- *(podes ir)* **Nº 8 820** *(normal)*: "Ir para onde? Para cima? …Não. Não é para cima, pois não?" 🎬 sorri devagar. "Está bem. Estava farto de esperar pelo amanhã."
- *(mãos)* 🎬 Ele olha para as mãos. Vê através delas. **Nº 8 820** *(triste)*: "Ah. Há quanto tempo?" 🎬 o herói não responde. "Muito, não é? Pronto. Obrigado por não mentires."
- 🎬 Desaparece. A janela azul por cima dele fica um segundo a flutuar sozinha e depois apaga-se.
- `[Sistema] Jogador nº 8 820: estado atualizado.`

⚙ Os cinco libertados: flag `fantasmas_livres` · a porta da Cabine do Capitão abre (se ainda não estava).

---

## C6-05 — O Último Registo

| | |
|---|---|
| ID | `cena_c6_05_diario_bordo` |
| Quando | entrar na Cabine do Capitão (andar 53) com os 5 fantasmas libertados |
| Onde | andar 53, Cabine do Capitão |
| Quem | herói |
| Música | silêncio → `tema_kai` (só piano, muito lento) |

🎬 Uma cabine pequena e torta. Uma mesa com mapas. Uma vela meio derretida, **ainda morna**. Ao lado, um livro grosso aberto: o **diário de bordo**.
🎬 O herói folheia. Muitas letras diferentes, ao longo de centenas de anos. A câmara para em algumas linhas:
- 📜 *"Ano 1 do navio. Somos onze. Todos com a janela. Vamos subir juntos. — Capitão Vasco, nº 298"*
- 📜 *"Dizem que lá em cima há um Administrador. Que quem chega ao topo fala com ele. Alguns de nós querem chegar primeiro, para lhe pedir coisas. Eu só quero ir para casa."*
- 📜 *"Ficámos. Não sei explicar. O mar é bonito e lá em cima dá medo. Amanhã subimos. — nº 312"*
- 📜 *"Amanhã. — nº 8 820"*
🎬 Na última página escrita, a tinta ainda está fresca. A letra é rápida e inclinada. O herói reconhece-a das mensagens na areia.
- 📜 *"Li isto tudo. Novecentos anos de 'amanhã'. Ninguém saiu. Nenhum."*
- 📜 *"Esta noite a janela falou comigo outra vez. Não com as frases do costume. Disse: 'Há outro caminho, Jogador nº 9 999. Mais rápido. Só para um.' Perguntei qual. Disse que me mostrava se eu fosse sozinho."*
- 📜 *"Eu sei. Eu sei que parece uma armadilha. Mas a Yui tem seis anos e eu já perdi a conta aos dias."*
- 📜 *"Se o 10 000 ler isto: não venhas atrás de mim. A sério. Volto quando souber o caminho. Prometo."*
- 📜 *"— Kai, nº 9 999"*
- *(se `kai_prometeu_voltar`)* 📜 *(mais abaixo, mais pequeno)* *"Prometi-te que voltava. Não me esqueci."*
🎬 O herói fecha o livro. Por baixo dele, em cima da mesa, o **porta-chaves do gato** do Kai *(só se não o tiver dado ao herói na cena de 8 ❤️; se já o deu, fica lá o fio de couro de onde ele pendia)*.
- `[Sistema] Jogador nº 9 999: localização desconhecida.`
- `[Sistema] …`

⚙ Missão **H_14** concluída: **Página especial "Diário de Bordo"** · flag `kai_desaparecido`. O Kai entra na **fase B** (`docs/dialogos/kai.md`).
⚙ A partir daqui, nas Zonas Seguras dos andares 53–60 não há encontros com o Kai.

---

## C6-06 — A Cidade sem o Kai

| | |
|---|---|
| ID | `cena_c6_06_sem_kai` |
| Quando | voltar a Ascendia depois da C6-05 (primeira vez) |
| Onde | Guilda → Estalagem |
| Quem | herói, Lyra, Gorvan, Dona Marta, Mia |
| Música | `ascendia_dia` (versão lenta) |

🎬 Na Guilda, a Lyra tem o registo do Kai aberto à frente. Já escreveu "desaparecido" três vezes e riscou as três.
- **Lyra** *(triste)*: "Não consigo escrever. Se escrever, fica verdade."
- **Lyra** *(nervosa)*: "O Mestre diz que não se manda equipa de resgate atrás de um Jogador que foi sozinho e de propósito. Que é a regra. Eu odeio esta regra."
- 🎬 O Gorvan sai do gabinete. Para ao pé do balcão.
- **Gorvan** *(normal)*: "Escreve 'em missão'." 🎬 pausa. "É verdade. Ele está em missão. A dele."
- **Lyra** *(triste, a escrever)*: "Em… missão."
- **Gorvan** *(normal, para o herói)*: "Os teimosos voltam. Eu voltei." 🎬 vira as costas. "…Mal. Mas voltei."
🎬 Na Estalagem, a Dona Marta está à porta do quarto do Kai, com um pano na mão.
- **Dona Marta** *(triste)*: "Limpo-lhe o quarto todos os dias. Para quando voltar. A cama feita, a janela aberta. Ele detesta a janela aberta. Para ele vir fechá-la."
🎬 À noite, na Praça, a **Mia** treina sozinha no sítio onde o Kai costumava treinar. Golpes com um pau, a chorar e a fingir que não.
- **Mia** *(zangada)*: "Ele prometeu ensinar-me o golpe da espada que vira ao contrário. Prometeu! Os crescidos prometem e depois vão-se embora!"

▶ **"Ele volta. Prometeu."**
▶ **"Eu ensino-te."**

- *(volta)* **Mia** *(triste)*: "…Promete tu também. Que o trazes." ⚙ +30 Mia
- *(ensino)* **Mia** *(surpresa)*: "Tu sabes?! …Não sabes, pois não? Está bem. Ensinas mal. Aprendo na mesma." ⚙ +30 Mia

⚙ As falas de "cidade sem o Kai" dos NPCs ficam ativas (fase B; ver cada NPC).

---

## C6-07 — Os Que Caem

| | |
|---|---|
| ID | `cena_c6_07_coralina` |
| Quando | entrar pela primeira vez em Coralina (andar 57) |
| Onde | andar 57, Portões de Coral → Palácio de Pérola |
| Quem | herói, Rainha Coralina, Príncipe Maré |
| Música | `debaixo_de_agua` → versão de palácio (harpa) |

🎥 Debaixo de água. Uma cúpula de ar gigante como uma bola de sabão. Lá dentro, uma cidade de coral rosa e branco, conchas como telhados, peixes a nadar por cima das ruas.
🎬 O herói atravessa a parede da cúpula e cai no chão, a respirar fundo. A barra de Ar desaparece.
🎬 Guardas-tritões levam-no ao palácio. Num trono de madrepérola, uma sereia de cabelo branco e coroa de coral. Ao lado, um tritão jovem que não para quieto.
- **Rainha Coralina** *(séria)*: "Um da janela. Com os pés secos e a cara assustada. Bem-vind{o/a} a Coralina."
- **Rainha Coralina** *(normal)*: "Os de cima caem. Sempre caíram. Barcos, casas, cidades inteiras. Nós apanhamos o que cai. Às vezes apanhamos Jogadores."
- **Príncipe Maré** *(feliz)*: "E às vezes os Jogadores apanham-nos a nós! Conta, mãe! A história do Nereu!"
- **Rainha Coralina** *(normal, com um suspiro)*: "O meu filho gosta de histórias velhas. Esta é muito velha."
- **Rainha Coralina** *(normal)*: "Há muito, muito tempo, quando Coralina era só metade do que é, vivia aqui um rapaz. Humano, filho de humanos que tinham caído. Nunca tinha visto um céu verdadeiro: só a cúpula."
- **Rainha Coralina** *(triste)*: "Chamava-se **Nereu**. Um dia passou por cá um da janela, sozinho e triste. Ficaram amigos. Quando o da janela subiu, o Nereu foi com ele. Para ver o céu."
- **Rainha Coralina** *(normal)*: "Nunca voltou. A família dele esperou a vida toda. Ainda há uma concha com o nome dele na Rua das Marés. Ninguém a tira."
- **Príncipe Maré** *(feliz)*: "Eu também quero ver o céu! Leva-me!"
- **Rainha Coralina** *(zangada)*: "Maré!"

⚙ Desbloqueia **Coralina** (estalagem, cristal, forja de coral, loja). Missões R6_09, R6_10 disponíveis. Flag `ouviu_nereu`.
⚙ A **concha do Nereu** (Rua das Marés) pode ser vista: `[Sistema] "Nereu. Foi ver o céu."` (só isto).

> Para quem escreve: o "da janela, sozinho e triste" é o **Aren**. A Rainha não sabe o nome dele e nunca o diz.
> O jogador só liga as duas coisas no fim (Arquivista, região 10).

---

## C6-08 — O Coração da Torre

| | |
|---|---|
| ID | `cena_c6_08_fossa` |
| Quando | chegar ao Fundo Escuro (andar 58) pela primeira vez |
| Onde | andar 58, fundo da fossa |
| Quem | herói |
| Música | `abismo` → silêncio |

🎬 Escuridão total. Só a luz do herói e, longe, pontinhos de criaturas que brilham.
🎬 O herói chega ao fundo. Silêncio. Depois, muito grave, muito lento, sente-se mais do que se ouve: **BUM**. A areia do fundo salta. As criaturas apagam-se todas ao mesmo tempo.
🎬 Muito tempo depois, voltam a acender-se, uma a uma.
- `[Sistema] …`
🎬 Nas fontes quentes, ao longe, uma luz vermelha. Lá no meio, um **ovo** enorme, do tamanho de uma casa, a pulsar devagar.

⚙ Sem falas. O "bum" repete-se **uma vez por hora de jogo** enquanto estiveres no andar 58. (Ver a página 58.) O ovo é de um Leviatã: não se pode apanhar.

---

## C6-09 — O Último do Mar

| | |
|---|---|
| ID | `cena_c6_09_leviata` |
| Quando | entrar no Mar Aberto do andar 60, no barco |
| Onde | andar 60, Mar Aberto |
| Quem | herói (e o Tiago, se estiver no barco), Leviatã |
| Música | trovão → silêncio → `leviata` |

🎬 Mar escuro. Trovões. Ao longe, um redemoinho enorme e, no centro, uma ilha de rocha com um trono partido.
🎬 Uma barbatana do tamanho de uma vela passa ao lado do barco. Um olho enorme, triste, abre-se debaixo de água e olha para o herói.
🎬 O Leviatã afasta-se. Mergulha. Volta à superfície mais longe. **Está a fugir.**
- *(com o Tiago)* **Tiago** *(nervoso)*: "Está a fugir de nós? Uma coisa daquele tamanho a fugir de NÓS?"
🎬 Por um momento, nada. Depois, por cima do herói, a janela do Sistema abre-se sozinha:
- `[Sistema] Unidade de guarda 60: modo de combate.`
🎬 Lá longe, o olho do Leviatã muda de cor: de verde-escuro para **azul**, a cor da janela. A criatura vira-se e vem direita ao barco.
- `[Sistema] Boss: Leviatã, O Último do Mar.`

⚙ Luta (ver `docs/BOSSES.md`, secção 12).

## C6-10 — Medo

| | |
|---|---|
| ID | `cena_c6_10_leviata_depois` |
| Quando | vencer o Leviatã |
| Onde | andar 60, O Trono |
| Quem | herói |
| Música | `vitoria` (muito curta, cortada) → ondas |

🎬 O Leviatã cai ao lado da ilha. O azul sai-lhe dos olhos devagar, como tinta na água. Os olhos voltam a ser verdes e tristes.
🎬 Olha para o herói. Depois olha para cima dele, para onde estava a janela. Fecha os olhos. Afunda-se devagar.
- `[Sistema] Boss derrotado: Leviatã.`
- `[Sistema] Obtiveste: Tridente do Leviatã.`
- `[Sistema] Título obtido: Senhor dos Mares.`
- `[Sistema] Boa, Jogador.`
🎬 O herói fica a olhar para a mensagem "Boa, Jogador." A mensagem fica no ar mais tempo do que devia. Depois fecha-se.
- `[Sistema] Região 6 concluída. Andar 61 desbloqueado.`

⚙ Missão **H_15** concluída. A página 60 aparece no trono.

---

## C6-11 — Dia da Subida: A Canção Sem Nome

| | |
|---|---|
| ID | `cena_c6_11_dia_subida` |
| Quando | voltar a Ascendia depois do Leviatã |
| Onde | Praça da Torre (Dia da Subida, F_05 — a festa **mais calada** do jogo) |
| Quem | herói, Aldric, Lucien, Lyra, Mia, Gorvan, Dona Marta |
| Música | `dia_da_subida` (versão lenta, menos instrumentos) |

🎬 A Praça tem bandeiras, mas menos gente. A estátua nova é pequena: uma serpente do mar de madeira, pintada de azul.
- **Governador Aldric** *(no palco)*: "Cidadãos. O mar está… vencido. Sessenta andares." 🎬 olha para a multidão, para o sítio onde o Kai costumava estar. "Este ano o discurso é curto. Há um lugar vazio. Todos sabemos qual."
- 🎬 O Lucien sobe ao palco sem o alaúde ao ombro. Pega nele devagar.
- **Lucien** *(normal)*: "Esta canção não tem nome. Vai ter, quando ele voltar. Até lá, é só música."
- 🎵 Uma melodia simples, sem letra, que é o `tema_kai` tocado devagar no alaúde. A Praça fica em silêncio. A Mia agarra-se à saia da Dona Marta.
- 🎬 No fim, ninguém aplaude logo. Depois o Gorvan bate palmas, devagar, sozinho. Os outros seguem-no.
- 🎬 A Lyra aproxima-se do herói com um papel na mão.
- **Lyra** *(normal)*: "Pus um anúncio no quadro da Guilda. 'Procura-se: Kai, Jogador nº 9 999. Casaco azul. Mau feitio. Recompensa: um jantar da Dona Marta e um abraço meu.'"
- **Lyra** *(triste)*: "O Mestre disse que não era um anúncio oficial. Eu disse que agora era."

⚙ `[Sistema] Capítulo 7: O Vulcão.` (título grande no ecrã)
