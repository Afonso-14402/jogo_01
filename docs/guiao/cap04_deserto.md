# Guião — Capítulo 4: Deserto (andares 31–40)

Missões: **H_10 Os Hieróglifos** (= R4_07), **H_11 O Que Também Subiu**. Povoações e missões secundárias:
`docs/dialogos/povoacoes_r04.md`. Mapas: `docs/mapas/r04_deserto.md`.

**O que este capítulo conta**: a primeira grande verdade. Na pirâmide, os hieróglifos mostram que a torre **já teve
vários reis**, os **Administradores**, e que **todos foram Jogadores**. O Faraó Eterno é um deles. Ninguém sabe ainda
quem manda **agora**. O Kai começa a pensar que "alguém lá em cima sabe o caminho para casa".

Cenas de amizade que costumam acontecer neste capítulo (não são obrigatórias): **Lyra 6 ❤️** (o acampamento do pai,
andar 31: `docs/dialogos/lyra.md`) e o **Rook** em Zahra (`rook_mae_zahra`: `docs/dialogos/rook.md`).

**Flags deste capítulo**: `kai_estrelas` e `kai_sem_ti` (C4-03), `sabe_administradores` (C4-11).

---

## C4-01 — O Mar de Areia

| | |
|---|---|
| ID | `cena_c4_01_dunas` |
| Quando | entrar pela primeira vez no andar 31 |
| Onde | andar 31, Mar de Dunas |
| Quem | herói, Caravaneiro Yusuf (ao longe) |
| Música | `dunas` |

🎥 A escada de luz abre-se no alto de uma duna. Areia dourada até ao horizonte. Um sol enorme, branco. O ar treme.
🎬 O herói dá um passo e escorrega duna abaixo, a deslizar de pé, até parar ao fundo, coberto de areia.
- `[Sistema] Aviso: sol do deserto. Entre as 10:00 e as 16:00, ao sol, perdes vida.`
- `tut_sol_deserto`: `[Sistema] Procura sombra ou bebe Cacto-Água. Um Cantil, um Turbante ou um Lenço do Deserto protegem-te do sol.`
- `tut_dunas`: `[Sistema] Nas dunas, desce a correr para deslizar. Subir é lento.`
🎬 Ao longe, fumo preto. Uma caravana virada, carroças partidas. Um homem de turbante sentado na sombra de uma roda, a abanar-se com o chapéu.
- **Yusuf** *(de longe, a acenar)*: "Ei! Tu! Não és uma miragem? Diz que não és uma miragem!"

⚙ Primeira conversa com o **Caravaneiro Yusuf** (`docs/dialogos/povoacoes_r04.md`, secção 1). Missão R4_02 disponível.

---

## C4-02 — Zahra

| | |
|---|---|
| ID | `cena_c4_02_zahra` |
| Quando | entrar pela primeira vez no Oásis de Zahra (andar 32) |
| Onde | andar 32, portão de Zahra → bazar |
| Quem | herói, Sultana Amira, Velho Omar, Torrenses |
| Música | `bazar_zahra` |

🎥 Depois do Campo das Miragens, uma lagoa azul verdadeira. À volta, centenas de tendas de todas as cores, um palácio pequeno de cúpula branca, cheiro a especiarias.
🎬 Um guarda de lança cruzada para o herói ao portão. Olha-lhe para a mochila, para a arma, para a cara.
- **Guarda** *(normal)*: "Um descido. Há meses que não vinha nenhum. A Sultana vai querer ver-te."
- `[Sistema] Nova povoação: Oásis de Zahra.`
🎬 No bazar, as pessoas param para olhar. Uma criança aponta para cima e depois para o herói e ri-se.
🎬 Uma mulher de véu dourado desce as escadas do palácio, seguida de dois guardas e de um velho de barba branca.
- **Sultana Amira** *(feliz)*: "Bem-vind{o/a} a Zahra, descid{o/a}. Aqui chamamos-vos assim: os que descem do céu da escada."
- **Sultana Amira** *(normal)*: "Nós nascemos aqui. Os nossos pais, e os pais deles. Nunca vimos o vosso céu. Diz-me uma coisa: é verdade que lá em baixo o céu não tem fim?"

▶ **"É verdade. Não tem fim."**
▶ **"Tem estrelas que se mexem."**
▶ **"Também nunca o vi bem. Só cheguei há pouco."**

- *(sem fim)* **Amira** *(surpresa)*: "Sem fim… Que medo. Aqui, à noite, o céu é um teto bonito. Sabemos onde acaba."
- *(estrelas)* **Amira** *(feliz)*: "Mexem-se? As nossas estão sempre no mesmo sítio. O Omar diz que alguém as pregou. Não sei se acredito no Omar."
- *(pouco)* **Amira** *(normal)*: "Então somos dois que não conhecem o vosso céu. Fica. Conta-me quando o conheceres."
- 🎬 O velho de barba branca dá um passo em frente.
- **Velho Omar** *(normal)*: "Os descidos sobem sempre. Há mil histórias sobre isso. A mais velha diz que, no princípio, o primeiro deles chegou ao topo e o fizeram rei."
- **Velho Omar** *(normal)*: "E que depois veio outro. E outro. Reis de cima, todos com a janela azul. Mas isso é só uma história. As histórias são de areia: mudam com o vento."
- **Sultana Amira** *(normal)*: "Omar. Não assustes a visita no primeiro dia."

⚙ Desbloqueia o **Oásis de Zahra** (estalagem, cristal, bazar, forja, banhos). Missões R4_01, R4_03 (depois do andar 35), R4_04, R4_10, R4_11, R4_14 disponíveis.

---

## C4-03 — As Estrelas Pregadas

| | |
|---|---|
| ID | `cena_c4_03_estrelas` |
| Quando | 1.ª noite (21:00–23:00) no Oásis de Zahra, depois da C4-02 |
| Onde | andar 32, telhado da estalagem |
| Quem | herói, Kai |
| Música | `bazar_zahra` (versão noturna: só alaúde) → `tema_kai` |

🎬 Noite azul e fria. O bazar fechado. No telhado plano da estalagem, alguém está deitado de costas a olhar para cima: o Kai, com o casaco azul a servir de almofada.
- **Kai** *(normal)*: "Ah. És tu. Senta-te. Ou deita-te. Aqui deita-se."
- **Kai** *(normal)*: "Estou a contar as estrelas. Contei-as ontem também. São as mesmas. No mesmo sítio. Não rodam. Estão pregadas."
- 🎬 Pausa. Ao longe, um cão ladra.
- **Kai** *(sério)*: "Quando passei o 30, a janela disse 'Bom ritmo'. Ontem, aqui, disse outra coisa. 'Faltam 68 andares, Jogador nº 9 999.'"
- **Kai** *(sério)*: "Nunca me tinha dito quantos faltavam. Está a contar comigo. Ou por mim. Não sei qual é pior."
- **Kai** *(normal)*: "Posso fazer-te uma pergunta parva?"
- **Kai** *(normal)*: "Se a janela te dissesse amanhã: 'Podes ir para casa. Agora. Só tu.' Ias? Sem te despedires de ninguém?"

▶ **"Ia. Sem pensar duas vezes."**
▶ **"Não sem me despedir."**
▶ **"Não sem ti."** (só com `coracoes(kai) >= 4`)

- *(ia)* **Kai** *(surpresa, depois ri-se)*: "Mentiros{o/a}. Tu despedias-te até do Tobias." ⚙ flag `kai_estrelas`
- *(despedir)* **Kai** *(normal)*: "Pois. Eu também acho que me despedia. Da Lyra, da Dona Marta… do Brom não, que ele grita." ⚙ +20 · flag `kai_estrelas`
- *(sem ti)* **Kai** *(surpresa)*: 🎬 fica calado. Vira a cara para o outro lado. "…Parv{o/a}. Não se diz isso a ninguém." 🎬 a voz falha um bocadinho. "…Obrigado." ⚙ +50 · flags `kai_estrelas` e `kai_sem_ti` (conta para a terceira resposta do duelo do andar 68, ver `docs/BOSSES.md`, secção 14)
- **Kai** *(normal)*: "Vai dormir. Amanhã o sol mata-nos aos dois. Eu fico aqui mais um bocado. A contar."

⚙ Sem missão. Se o herói não dormir na estalagem nessa noite, a cena acontece na noite seguinte.

---

## C4-04 — A Professora

| | |
|---|---|
| ID | `cena_c4_04_iris` |
| Quando | chegar ao Acampamento dos Escavadores (andar 34) pela primeira vez |
| Onde | andar 34, Acampamento dos Escavadores |
| Quem | herói, Professora Íris Pá-Velha, Beto |
| Música | `dunas` (versão calma, com pás a cavar) |

🎬 Andaimes de madeira encostados a uma cúpula que sai da areia. Tendas com mesas cheias de cacos. Um escavador (Beto) a dormir dentro de um buraco, com o chapéu na cara.
🎬 Uma mulher magra, de óculos enormes e chapéu de abas largas, sai de dentro de um buraco com um pincel na boca.
- **Íris** *(surpresa)*: "Um descido! Não, não és do acampamento. Do acampamento conheço as caras todas. São três. Uma está a dormir."
- **Íris** *(feliz)*: "Professora Íris Pá-Velha. Arqueóloga. Amiga do Fausto, o da biblioteca. Ele manda-me chá. Eu mando-lhe cacos. É uma amizade muito antiga e muito suja."
- **Íris** *(normal)*: "Escuta. Mais acima, no 38 e no 39, há uma pirâmide. Lá dentro há paredes escritas. Hieróglifos azuis que brilham. Eu não consigo lá chegar: tenho sessenta e dois anos e um joelho de oitenta."
- **Íris** *(normal)*: "Se lá chegares, copia-os para mim. Seis painéis. Eu e o Fausto traduzimos. Ele diz que é o achado do século. Eu digo que é do milénio. Discutimos muito."

▶ **"Eu copio."**
▶ **"Porque é que são importantes?"**

- *(copio)* **Íris** *(feliz)*: "Esplêndido! Toma este caderno de papel de arroz e este carvão. Copia tudo. Até as manchas. As manchas também dizem coisas."
- *(importantes)* **Íris** *(séria)*: "Porque são a única coisa na torre escrita por quem a governava. Tudo o resto foi escrito por quem a sofria."

⚙ Missão **H_10 / R4_07 Os Hieróglifos** ativa. Recebe o **Caderno de Papel de Arroz** (item de missão). `[Sistema] Missão: copia os 6 painéis da pirâmide (andar 39).`

---

## C4-05 — A Marca na Carapaça

| | |
|---|---|
| ID | `cena_c4_05_imperador` |
| Quando | vencer o Escorpião Imperador (andar 35) |
| Onde | andar 35, Cratera do Ninho |
| Quem | herói |
| Música | `escorpiao_imperador` → vento |

🎬 O escorpião negro e dourado cai de lado. As pinças abrem-se devagar.
🎬 Na carapaça, a **marca azul** (um quadrado com um círculo e três riscos) brilha mais forte, como se alguém a estivesse a olhar. Depois apaga-se de uma vez, como uma luz desligada.
- `[Sistema] Mini-boss derrotado: Escorpião Imperador.`
- `[Sistema] Unidade de guarda 35: desativada.`
🎬 O herói olha para a janela. A mensagem desaparece mais depressa do que as outras.

⚙ Sem falas. Recompensas normais: **Ferrão Imperial**, título *Destronador*. (A página 35 fala da mesma marca.)
⚙ Primeira vez que o Sistema usa a palavra **"unidade"** para um guardião.

---

## C4-06 — O Olho da Tempestade

| | |
|---|---|
| ID | `cena_c4_06_olho` |
| Quando | entrar pela primeira vez no Olho da Tempestade (andar 36) |
| Onde | andar 36, centro da tempestade |
| Quem | herói, Djinn da Tempestade (ao fundo) |
| Música | vento forte → silêncio total |

🎬 O herói atravessa a última parede de areia e cai de joelhos. Silêncio. O céu lá em cima é limpo e azul. À volta, a tempestade gira como uma parede.
🎬 Ao centro, o farol de pedra. Ao pé dele, a flutuar de pernas cruzadas, um espírito azul de turbante, de olhos fechados.
🎬 O herói fica parado. No silêncio, ouve-se um zumbido muito baixo, como uma máquina enorme muito longe. E, por baixo do zumbido, uma voz que não diz palavras. Por um segundo, só uma palavra se percebe:
- *(sussurro, sem quem fale)*: "…próximo…"
- `[Sistema] …`
🎬 O Djinn abre os olhos.
- **Djinn** *(feliz, voz que ecoa)*: "Ouviste? Poucos ouvem. É a torre a pensar. Pensa devagar e em voz alta. Agora: lutamos, ou fazemos de conta que não ouviste nada?"

⚙ Luta com o guardião **Djinn da Tempestade**. Se tiveres a **Lâmpada Velha** (R4_11), o Djinn não luta: cena da missão R4_11 (`docs/dialogos/povoacoes_r04.md`).

---

## C4-07 — A Porta dos Nomes

| | |
|---|---|
| ID | `cena_c4_07_nomes` |
| Quando | abrir o portão da pirâmide (puzzle dos espelhos solares, andar 38) |
| Onde | andar 38, Fachada |
| Quem | herói |
| Música | `piramide` (entra devagar) |

🎬 A luz do último espelho bate no portão de ouro. O portão range e abre-se para dentro. Lá dentro, escuro e frio.
🎬 Ao lado do portão, numa parede lisa, colunas e colunas de **nomes** gravados, todos na mesma escrita azul e estranha dos hieróglifos (ninguém a sabe ler). Ao lado de cada nome, o símbolo da janela.
🎥 A câmara desce devagar pela lista. São dezenas.
🎬 O **penúltimo** nome brilha um bocadinho mais do que os outros, como se ainda estivesse aceso.
🎬 O **último** foi **raspado** à força: só sobram riscos fundos na pedra e pó azul no chão. Por baixo dele, a parede continua lisa, à espera.
- `[Sistema] Texto ilegível.` *(em cada nome, ao passar a mão)*
- `[Sistema] Dados apagados.` *(no nome raspado)*
🎬 O herói toca nos riscos. Um bocadinho de pó azul fica-lhe nos dedos e apaga-se.

⚙ Sem falas. A página 38 está no chão, ao pé do nome raspado. O Fausto (`fausto_rumor_05`) e a Arquivista (região 10) falam deste nome.
⚙ Se tiveres o **Olho do Sistema** (Skill Única), aparecem mais duas linhas: no nome raspado, `[Sistema] Registo 0: acesso negado.`; no penúltimo, `[Sistema] Registo ativo: acesso negado.`
> Para quem escreve: a lista é dos Jogadores que **chegaram ao topo**. O penúltimo nome é o **Aren** (o Administrador de agora: por isso
> brilha). O raspado é o **Jogador Sem Número**, que recusou há 300 anos. Quando o Aren passou aqui (página 38), a lista acabava
> no Administrador antes dele e por baixo havia espaço: o nome dele ainda não estava lá.

---

## C4-08 — Os Hieróglifos

| | |
|---|---|
| ID | `cena_c4_08_hieroglifos` |
| Quando | copiar os 6 painéis da Câmara dos Hieróglifos (andar 39), com H_10 ativa |
| Onde | andar 39, Câmara dos Hieróglifos |
| Quem | herói |
| Música | `piramide` (versão com coro baixo) |

🎬 Uma sala redonda e alta. Seis painéis de pedra à volta, pintados com figuras e cheios de símbolos azuis que brilham no escuro.
🎬 Cada painel copia-se com [interagir] (o herói encosta o papel e esfrega o carvão: 3 s). Ao copiar, a câmara aproxima-se do painel:

| Painel | O desenho |
|---|---|
| 1 | Uma figura pequena cai do céu. À volta da cabeça, um quadrado azul |
| 2 | A figura sobe uma escada sem fim. Monstros de cada lado. Os monstros curvam-se ao quadrado azul |
| 3 | No topo, uma figura alta e cansada põe uma coroa na cabeça da pequena |
| 4 | A figura coroada está sentada num trono. Por baixo dela, a torre cresce: mundos inteiros entram por baixo, como comida |
| 5 | A figura coroada está muito velha. Olha para baixo. Do céu cai **outra** figura pequena, com outro quadrado azul |
| 6 | A nova figura recebe a coroa. A velha desfaz-se em pó. Por baixo do pó, a mesma escada recomeça |

- `[Sistema] Painel copiado. (1/6)` … `(6/6)`
🎬 Ao copiar o último, o herói recua para ver os seis juntos. São uma roda: o painel 6 termina onde o 1 começa.
- `[Sistema] Missão: leva as cópias ao Velho Fausto, em Ascendia.`

### Na Biblioteca (entregar as cópias)
🎬 O Fausto e a Íris (que desceu de propósito) estão à mesma mesa, cheia de livros abertos. Discutem.
- **Íris** *(zangada)*: "É uma coroa, Fausto!" · **Fausto** *(zangado)*: "É um chapéu cerimonial!" · **Íris**: "Que diferença faz?!" · **Fausto**: "Toda!"
🎬 Veem o herói. Calam-se. Estendem as mãos ao mesmo tempo para as cópias.
- **Fausto** *(feliz)*: "Os seis! Inteiros! Jovem, nem sabes o que trouxeste."
- **Íris** *(normal)*: "Nós também não. Ainda. Dá-nos uns dias. E vai lá abaixo… quer dizer, lá acima. Ao 40. Há uma sala com um sarcófago. Os painéis falam dele."
- **Fausto** *(normal)*: "Quando voltares, terei a tradução. Prometo. A Íris não promete nada. A Íris nunca promete."
- **Íris** *(normal)*: "Prometo não lhe bater até lá. É o máximo."

⚙ Entrega as cópias. H_10 fica **à espera** (conclui-se na C4-10). Missão **H_11 O Que Também Subiu** ativa.

---

## C4-09 — O Que Também Subiu

| | |
|---|---|
| ID | `cena_c4_09_farao` |
| Quando | entrar na Sala do Sarcófago (andar 40) |
| Onde | andar 40, Sala do Sarcófago |
| Quem | herói, Faraó Eterno |
| Música | silêncio → `farao_eterno` |

🎬 Uma escadaria dourada desce até uma câmara enorme. Estátuas de deuses com cabeças de animais. Ao centro, um sarcófago de ouro.
🎬 A tampa do sarcófago desliza sozinha e cai com um estrondo. Uma figura de ligaduras douradas senta-se devagar. Por trás da máscara de ouro, dois olhos **azuis**, da cor exata da janela do Sistema.
- **Faraó Eterno** *(normal, voz seca como areia)*: "Outro. Outra vez. Com a janela."
- **Faraó Eterno** *(normal)*: "Sentes o quadrado azul atrás dos olhos? Eu também o sentia. Agora sinto-o à frente."
- **Faraó Eterno** *(zangado)*: "Ninguém passa por mim. Foi o que me mandaram. Há tanto tempo que já não me lembro de quem mandou."
- `[Sistema] Boss: Faraó Eterno, O Que Também Subiu.`

⚙ Luta (ver `docs/BOSSES.md`, secção 8).
- *(fase 3, a areia começa a encher)* **Faraó** *(triste)*: "A areia… sempre a areia. Tanto tempo a contar grãos."

## C4-10 — Pó

| | |
|---|---|
| ID | `cena_c4_10_po` |
| Quando | vencer o Faraó Eterno |
| Onde | andar 40, Sala do Sarcófago |
| Quem | herói, Faraó Eterno |
| Música | `vitoria` (curta e abafada) → silêncio |

🎬 O Faraó cai de joelhos na areia. A máscara de ouro estala ao meio e cai. Por baixo não há cara: só ligaduras e luz azul a sair pelas frestas.
- **Faraó Eterno** *(normal, quase a sussurrar)*: "Eu também subi."
- **Faraó Eterno** *(triste)*: "Eu também quis voltar."
- 🎬 A luz azul dos olhos pisca, como uma janela a fechar.
- **Faraó Eterno** *(normal)*: "Diz-lhe… diz ao de cima… que eu…"
- 🎬 Vira pó. O pó escorre por entre os degraus como água. Fica só o cetro e a Khopesh, em cima das ligaduras vazias.
- `[Sistema] Boss derrotado: Faraó Eterno.`
- `[Sistema] Obtiveste: Khopesh do Faraó.`
- `[Sistema] Título obtido: Quebra-Maldições.`
- `[Sistema] Região 4 concluída. Andar 41 desbloqueado.`

⚙ Missão **H_11** concluída. A página 40 aparece em cima do sarcófago vazio.

---

## C4-11 — A Tradução

| | |
|---|---|
| ID | `cena_c4_11_traducao` |
| Quando | voltar a Ascendia depois do Faraó; entrar na Biblioteca (antes ou depois da festa) |
| Onde | Biblioteca do Fausto, à noite |
| Quem | herói, Velho Fausto, Professora Íris, (Gorvan, à porta) |
| Música | `ascendia_noite` → `tema_fausto` (lento) |

🎬 A biblioteca às escuras, menos uma mesa com três velas. O Fausto e a Íris estão sentados lado a lado, calados. Não discutem. Há chávenas de chá frio por todo o lado.
- **Fausto** *(normal)*: "Senta-te, jovem. Acabámos."
- **Íris** *(séria)*: "Três noites sem dormir. E não por causa da discussão. Discutimos pouco. Isso devia dizer-te alguma coisa."
- 🎬 O Fausto empurra uma folha para o herói. Letra pequena e certinha.
- **Fausto** *(normal)*: "Os desenhos têm legendas. Os símbolos azuis. Demorámos a perceber: são sempre os mesmos seis ou sete, repetidos. A palavra que mais aparece é esta."
- 🎬 Aponta para um símbolo: o quadrado com o círculo e os três riscos.
- **Fausto** *(normal)*: "A Íris lê 'janela'. Eu leio 'sistema'. Concordámos em discordar."
- **Íris** *(normal)*: "A segunda palavra que mais aparece é a da figura coroada. Quer dizer 'o que administra'. 'O que mantém'. Nós escrevemos: **Administrador**."
- **Fausto** *(sério)*: "Ouve o que dizem os painéis, todos seguidos."

📜 **Página especial "Os Administradores"** (aparece no ecrã como uma folha do Fausto; fica no Diário → Páginas):

> *Do céu cai um que tem a janela.*
> *Sobe. Os guardas curvam-se à janela, não a ele.*
> *No topo, o que administra está cansado. Dá-lhe a coroa.*
> *O novo administra. A torre come mundos e cresce.*
> *O que administra fica velho. Chama do céu outro que tenha a janela.*
> *O novo recebe a coroa. O velho é pó.*
> *E a escada recomeça.*
>
> *— traduzido por F. e Í., com muitas dúvidas e pouco chá*

- **Íris** *(séria)*: "Uma roda. Não houve um rei. Houve muitos. E todos caíram do céu com a janela."
- **Fausto** *(triste)*: "Todos foram Jogadores, jovem. Como tu. Como o Kai. O Faraó que venceste… era um deles. Um dos velhos. A torre não o deixou ser pó em paz: pô-lo a guardar a porta."

▶ **"Então quem manda agora também foi Jogador?"**
▶ **"Porque é que nos trazem?"**
▶ *(ficar calad{o/a})*

- *(quem manda)* **Fausto** *(normal)*: "Se a roda não parou… sim. Há alguém lá em cima. Com a janela. E com uma coroa. Há quanto tempo, não sei."
- *(porquê)* **Íris** *(séria)*: "O painel 5 diz 'chama do céu outro'. Chama. Não é por acaso que vocês caem. Alguém vos chama." · **Fausto**: "Para quê, ainda não sabemos. E eu odeio não saber."
- *(calado)* 🎬 O Fausto acena devagar. **Fausto**: "Também fiquei assim. Três noites."
- 🎬 Uma tábua range. O **Gorvan** está à porta, encostado ao batente. Ninguém o ouviu entrar.
- **Gorvan** *(normal)*: "Hmm." 🎬 pausa. "Isto fica nesta sala. Por agora. A cidade já tem medo que chegue."
- **Fausto** *(zangado)*: "O conhecimento não é teu para fechar numa sala, Gorvan!"
- **Gorvan** *(normal)*: "Não. Mas o medo é meu para não espalhar." 🎬 vira-se e sai.
- **Íris** *(baixinho)*: "Ele tem razão. Detesto quando os militares têm razão."

⚙ Missão **H_10 Os Hieróglifos** concluída: **Página especial "Os Administradores"** · 2 000 ouro. Flag `sabe_administradores`.
⚙ A partir daqui o **Fausto** passa a ter falas sobre "a roda" e o Diário → Páginas mostra uma nova secção: *Os Administradores*.

---

## C4-12 — Dia da Subida: Montadas

| | |
|---|---|
| ID | `cena_c4_12_dia_subida` |
| Quando | voltar a Ascendia depois do Faraó (a festa acontece no mesmo dia da C4-11, de dia) |
| Onde | Praça da Torre (Dia da Subida, F_05) → Rancho do Zed |
| Quem | herói, Aldric, Lucien, Zed, Kai |
| Música | `dia_da_subida` |

🎬 A Praça em festa. Uma estátua nova: um faraó de madeira pintada de dourado, com a máscara torta.
- **Governador Aldric** *(no palco)*: "Cidadãos! O deserto foi vencido! Areia! Muita areia! E… e a partir de hoje, o Rancho do senhor Zed tem montadas! Pode-se ir à torre… sentado!"
- **Lucien** *(do palco)*: "♪ Quarenta degraus de ouro e um faraó no fim! Ele subiu, ele ficou… mas tu voltaste para mim! Para nós! Para a cidade! ♪"
- 🎬 Ao pé do palco, o **Zed** com um lagarto enorme pela trela. O lagarto tenta comer o chapéu do Aldric.
- **Zed** *(normal)*: "Lagarto da Areia. Para quem o merecer. Tu mereces. Ele ainda não sabe. Vem ao rancho."
- 🎬 O Kai está sentado na beira da fonte, sozinho, a olhar para a torre.
- **Kai** *(sério)*: "O Fausto contou-me. O Gorvan não queria que se soubesse, por isso o Fausto contou-me logo. Os reis da torre eram Jogadores."
- **Kai** *(sério)*: "Pensa nisto: se quem manda lá em cima foi Jogador, sabe o caminho para casa. Sabe. E não o usa. Ou não deixa usar."
- **Kai** *(normal)*: "Vou perguntar-lhe. Quando lá chegar. Vou perguntar-lhe com muita educação. E depois com a espada."
- *(se `kai_sem_ti`)* **Kai** *(normal)*: "…E se me disser que só pode ir um, pergunto outra vez. Até dar dois."

⚙ O **Zed** passa a vender e a tratar **montadas** (missão R4_03 e o Rancho: `docs/dialogos/zed.md`). `tut_montada` aparece ao receber a primeira.
⚙ `[Sistema] Capítulo 5: O Gelo.` (título grande no ecrã)
