# Lucien — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.17. Dados: `dados/dialogos/lucien.json`. Taberna: `docs/LOJAS.md`, secção 2.14.
O Lucien canta uma **canção nova em cada Dia da Subida** (secção 7: os títulos e os versos principais).

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | cantados: sobem e descem como uma melodia; às vezes um acorde de alaúde no fim da frase |
| Como fala | dramático, faz rimas más de propósito (e às vezes sem querer), exagera tudo; quando fala da terra dele, deixa de rimar |
| Repete | "Ó herói…", "A rima vem depois. Primeiro vem a emoção.", "Isto dava uma canção." |
| Tiques | dedilha o alaúde enquanto fala (animação `dedilhar`); tira o chapéu num gesto largo ao cumprimentar |
| Nunca diz | uma coisa sem a exagerar (exceto na cena de 8 ❤️) |
| Chama ao herói | "Ó herói", "Ó Dez Mil", "musa" (a partir dos 4 corações) |
| Quem é | 28 anos. Nasceu numa caravana de músicos da **Cidade Errante** (Vagar). Desceu da tartaruga em Ascendia há 6 anos "porque aqui há heróis para cantar". A família continua na caravana |
| Rotina | Praça de manhã (9:00–12:00, a compor no banco da fonte) · dorme à tarde · Taberna 16:00–2:00. Sexta: canção nova. Quando a Cidade Errante está num andar, vai lá no 1.º dia ver a família |

---

## 2. Primeira conversa

- 🎬 O Lucien salta para cima de uma mesa da Taberna e toca três acordes.
- **Lucien** *(feliz)*: "♪ Ó Jogador nº dez mil, que vieste de longe e de… de… ♪ …Não rima nada com mil. Vou ter de mudar o número."
- **Lucien** *(normal)*: "Lucien, bardo, poeta, cronista das subidas desta cidade. Tu sobes, eu canto. É uma parceria."
- **Lucien** *(feliz)*: "Traz-me histórias! Monstros, quedas, vitórias, derrotas engraçadas. Sobretudo as derrotas engraçadas. Essas vendem."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Rumor do dia · Pedir uma canção · Minijogos** (depois do andar 30) **· Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lucien_dia_01` | `hora entre 9 e 12` | normal | *(na Praça)* "Estou a compor. Preciso de uma palavra que rime com 'torre'. Não me digas 'morre'. Toda a gente diz 'morre'." |
| `lucien_dia_02` | `hora entre 16 e 18` | feliz | "A taberna abriu! Ainda está vazia. O público chega às oito. O talento chega às oito e meia." |
| `lucien_dia_03` | `hora entre 22 e 2` | feliz | "♪ A noite é jovem, o vinho é velho, e eu sou… mais ou menos. ♪" |
| `lucien_dia_04` | — | feliz | "♪ Ó herói que sobe aos céus, com a espada e… e os pés! ♪ É um rascunho." |
| `lucien_dia_05` | — | normal | "A rima vem depois. Primeiro vem a emoção." |
| `lucien_dia_06` | — | feliz | "O Brom chorou na minha última canção. Disse que era fumo. A taberna não tem fumo. Tem o Brom." |
| `lucien_dia_07` | — | normal | "A Freya prendeu-me uma hora por rimar 'Freya' com 'cadeia'. Foi a melhor crítica que já recebi." |
| `lucien_dia_08` | — | feliz | "O Governador pediu-me um hino para a cidade. Fiz dezassete versões. Ele aprovou a primeira. Em triplicado." |
| `lucien_dia_09` | `dia_semana == sexta` | feliz | "Sexta! Canção nova esta noite! Ainda não está escrita. É assim que se faz arte: com pânico." |
| `lucien_dia_10` | `dia_semana == domingo` | normal | "Domingo o Kai vem comer e pede-me 'música do mundo dele'. Toco qualquer coisa. Ele diz que está perto. Mente bem." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lucien_dia_20` | `estacao == primavera` | feliz | "Primavera! Canções de amor! Não, este jogo é sobre amizade. Canções de amizade! Rimam menos." |
| `lucien_dia_21` | `estacao == verao` | feliz | "Verão: canto na Praça até tarde. As cigarras fazem o coro. Desafinam menos do que os clientes." |
| `lucien_dia_22` | `estacao == outono` | triste | "Outono. As canções ficam mais lentas. Não sou eu. São as folhas." |
| `lucien_dia_23` | `estacao == inverno` | normal | "No inverno a taberna enche. As pessoas cantam comigo para aquecer. Mal. Mas aquecem." |
| `lucien_dia_24` | `clima == chuva` | feliz | "Chuva no telhado da taberna: o melhor tambor da cidade. Toco por cima." |
| `lucien_dia_25` | `clima == nevoeiro` | normal | "Nevoeiro. Bom tempo para baladas misteriosas. Mau tempo para encontrar o caminho para casa." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lucien_dia_40` | `andar_maximo < 5` | normal | "Ainda não tens canção. Precisas de um feito. Um javali, talvez. Os javalis rimam com 'avais'… não rimam." |
| `lucien_dia_41` | `andar_maximo >= 30` | feliz | "Já podes jogar às cartas na taberna! E aos dados! E ao braço de ferro com a Freya, se tiveres seguro." |
| `lucien_dia_42` | `missao(H_14) == concluida && missao(H_16) != concluida` | triste | "Compus uma canção para o Kai. Para quando voltar. Ensaio-a todas as noites. Ainda não a toquei. Vou tocá-la quando ele estiver cá." |
| `lucien_dia_43` | `flag(kai_salvo)` | feliz | "Toquei a canção do Kai. Ele fingiu que não gostou. Pediu-a três vezes." |
| `lucien_dia_44` | `andar_maximo >= 72` | normal | "Há um mercado de fantasmas que paga em lágrimas. Imagina um concerto lá. Choravam e pagavam. É o sonho." |
| `lucien_dia_45` | `missao(H_21) == concluida` | triste | "Não sei que canção fazer para isto. Pela primeira vez, não sei. Talvez seja uma canção sem palavras." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lucien_dia_60` | `coracoes(lucien) >= 2` | feliz | "Guardei-te a mesa ao pé do palco. Assim ouves as notas boas antes de as estragar." |
| `lucien_dia_61` | `coracoes(lucien) >= 4` | normal | "Musa. Posso chamar-te musa? Já chamei. Desculpa. Não desculpes." |
| `lucien_dia_62` | `coracoes(lucien) >= 6` | feliz | "As minhas canções sobre ti são as que mais pedem. Não por causa das rimas. Por causa de ti." |
| `lucien_dia_63` | `coracoes(lucien) >= 8` | triste | "Às vezes quero voltar para a caravana. Depois lembro-me de que lá ninguém sobe. Aqui alguém sobe. Alguém tem de cantar isso." |
| `lucien_dia_64` | `coracoes(lucien) >= 10` | feliz | "A Balada já se canta em três andares. O Bruno canta-a no 2. A Hilda no 11. Os fungoides cantam-na devagar no 16." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lucien_dia_70` | `origem == jogador` | feliz | "No teu mundo havia jogos com música? Canta-me uma! …Isso é uma música? Só tem 'piu piu' e 'tum tum'. Gosto." |
| `lucien_dia_71` | `origem == dormir` | normal | "Vieste a dormir. 'O herói que acordou noutro mundo.' É o melhor começo de canção que existe. Já está escrito." |
| `lucien_dia_72` | `origem == atrasado` | feliz | "'O herói atrasado, que corria para a escola e caiu numa torre.' Ainda não decidi se é comédia ou tragédia." |
| `lucien_dia_73` | `skill_unica == lamina_espiritual` | feliz | "A tua espada solta ondas de luz! Isso é tão… teatral. Gosto de ti cada vez mais." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `lucien_curta_1` | feliz | "♪ Outra vez, outra vez… ♪ É o refrão. Não tem mais." |
| `lucien_curta_2` | normal | "Estou a afinar. O alaúde. Eu já não tenho afinação." |
| `lucien_curta_3` | feliz | "Volta quando tiveres uma história nova!" |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Lucien** *(feliz)*: "A torre é a maior canção do mundo! Cem andares, cem versos. E ninguém sabe o refrão."
- **Lucien** *(normal)*: "Na caravana dizíamos que a torre é um instrumento. Que cada mundo que engole é uma nota. E que um dia vai tocar a música toda."
- **Lucien** *(triste)*: "Espero estar cá para ouvir. E espero que seja bonita."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "♪ Na floresta verde, o herói entrou, um javali bufou, e o herói… ♪ Fugiu? Não fugiste. Vou mudar." |
| 2 Cavernas | "Nas minas a música tem eco. Canta lá dentro. Ouves-te três vezes. Duas a mais do que devias." |
| 3 Pântano | "Os Homens-Sapo cantam em coro à noite. São melhores do que eu. Não digas a ninguém." |
| 4 Deserto | "Zahra tem tambores de areia. Traz-me um ritmo de lá. Assobia-o. Eu aprendo." |
| 5 Gelo | "No norte cantam canções de caça à volta da lareira. Tristes e bonitas. Como o frio." |
| 6 Oceano | "Canções de marinheiro! Os piratas reformados do Porto sabem duzentas. Diz-lhes que o Lucien quer aprender. Leva rum." |
| 7 Vulcão | "Os anões do fogo martelam a cantar. Cada martelada é uma nota. Uma forja inteira é uma orquestra." |
| 8 Reino Assombrado | "Há uma cidade fantasma com uma caixa de música. Toca a mesma canção há mil anos. Imagina a paciência do público." |
| 9 Céu | "Os Alados cantam ao vento. As pontes de luz seguem uma música. Aprende-a. Assobia-ma. Por favor." |
| 10 Abismo | "Dizem que lá em cima há silêncio. Silêncio total. É a coisa mais assustadora que conheço." |

### 4.3 Rumores (o "Rumor do dia", 30 ouro, ou de graça com 4+ ❤️)
| ID | Condição | Rumor |
|---|---|---|
| `lucien_rumor_01` | — | "Um cliente jura que viu luzes a dançar no andar 4 à meia-noite. Estava bêbedo. Mas os bêbedos às vezes veem bem." |
| `lucien_rumor_02` | `andar_maximo >= 9` | "O Pip diz que o Rei do Lago só aparece com nevoeiro de manhã cedo. O Pip diz muitas coisas. Esta pode ser verdade." |
| `lucien_rumor_03` | `andar_maximo >= 11` | "A corrida de vagonetas do andar 11 tem um atalho. Inclina-te para a esquerda na terceira curva. Não me perguntes como sei." |
| `lucien_rumor_04` | `andar_maximo >= 26` | "Na Vila Coaxa vendem uma poção-surpresa. Uma vez fiquei com voz de sapo dois dias. Foi o meu melhor concerto." |
| `lucien_rumor_05` | `andar_maximo >= 44` | "Há um aventureiro congelado no gelo do 44 há anos. Dizem que ainda pestaneja. Se o salvares, compõe-te uma canção. Ou eu." |
| `lucien_rumor_06` | `andar_maximo >= 52` | "No Porto Arquipélago há uma ex-pirata chamada Rosa que faz a melhor caldeirada da torre. A Dona Marta não pode saber que eu disse isto." |
| `lucien_rumor_07` | `andar_maximo >= 83` | "As pontes de luz do céu seguem uma melodia. Quem a canta, passa. Eu sei as primeiras notas. Pagas o jantar e ensino-tas." |

### 4.4 A vida dele
| Corações | Fala |
|---|---|
| 0 | "A minha vida é uma canção! Ainda a estou a compor. Vai no terceiro verso." |
| 2 | "Nasci numa caravana em cima de uma tartaruga. A Cidade Errante. Os meus pais tocam lá: o pai tambor, a mãe violino." |
| 4 | "Desci em Ascendia há seis anos. A tartaruga parou cá dois dias e eu fiquei. Escrevi aos meus pais. Eles responderam com uma canção zangada." |
| 6 | "Queria cantar heróis. Na caravana só cantávamos mercadores. 'O Mercador e o Tapete'. 'O Mercador e o Desconto'. Precisava de dragões." |
| 8 | ver a **cena de 8 ❤️** |
| 10 | "A minha mãe ouviu a Balada numa taberna do andar 52. Escreveu-me: 'Agora já percebo porque ficaste.' Chorei. Rimou." |

---

## 5. Presentes

**Adora:** Café da Selva, histórias de bosses (dar-lhe um **troféu** para ver conta como presente "adora" e não o perdes), instrumentos (Ocarina, Concha do Mar) ·
**Gosta:** doces, flores · **Detesta:** silêncio (presentes "silenciosos": Pedra, Algodão, Rolhas — e ficar calado nas escolhas dele).

| Reação | Falas |
|---|---|
| Adora | "♪ Ó presente maravilhoso, ó herói generoso! ♪ …Está bem, é óbvio. Mas é sincero." · "Uma concha que canta! Vou pô-la ao ouvido em todos os concertos. Para ouvir o aplauso do mar." |
| Gosta | "Doces! Para a garganta. É medicinal. É o que digo à Dona Marta." |
| Neutro | "Obrigado! Vou… pendurá-lo no palco. Tudo fica bem num palco." |
| Não gosta | "Hmm. Isto não faz som nenhum. Que coisa triste." |
| Detesta | "Algodão? Para os OUVIDOS? Estás a dizer-me alguma coisa?" |

| Item | Fala |
|---|---|
| Café da Selva | "Café! O combustível dos poetas! Esta noite não durmo. Esta noite escrevo um épico." |
| Troféu de um boss (mostrar) | "Isto é… a cabeça do {boss}? De verdade? Conta-me tudo. Não, espera. Deixa-me pegar no alaúde. Agora conta." |

---

## 6. Aniversário e festivais

**Aniversário (Verão, dia 19):**
- Sem presente: "Faço anos! Fiz uma canção sobre mim. É curta. 'Lucien, Lucien, que bonito és tu.' Tem só isso. É perfeita."
- Com presente que adora: "♪ Parabéns a mim, e obrigado a ti! ♪ Rimou! Rimou à primeira! Este é o melhor dia do ano!"

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Toco a música do baile! Escolhe um par. Se não tiveres, eu toco mais devagar para teres tempo de arranjar." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Eu? Mas quem toca? …Toca o Pip. Mal. Mas toca. Vamos!" ⚙ +100 |
| F_02 Festival da Pesca | "Compus a 'Canção do Peixe Que Fugiu'. Toco-a ao Pip todos os anos. Ele chora." |
| F_03 Noite dos Espíritos | "Canto baladas de fantasmas! Os fantasmas amigáveis vêm ouvir. Aplaudem sem fazer barulho. O público ideal." |
| F_04 Festival da Estrela | "Concerto de inverno na Praça! Todas as canções do ano, uma atrás da outra. Traz um casaco. E paciência." |
| F_05 Dia da Subida | ver secção 7: canção nova em cada um |
| F_06 Concurso da Casa | "Sou jurado com o Aldric. Ele vê as paredes. Eu vejo a alma da casa. Uma casa sem música não tem alma." |
| F_07 Noite das Lanternas | "Nesta noite não canto. Toco só o alaúde, baixinho, enquanto as lanternas descem o rio. É a música mais bonita que sei. Não tem letra." |

---

## 7. Depois dos bosses (as canções do Dia da Subida)

Nos **bosses** (andares 10, 20, …, 90) o Lucien estreia uma canção no palco da Praça (F_05). Nos mini-bosses comenta.

| Boss | Fala / canção |
|---|---|
| Javali-Rei (5) | "Um javali do tamanho de uma carroça! E tu caíste em cima dele. O Kai contou. É a primeira estrofe." |
| Ent Ancião (10) | **"A Árvore que Falava"** — ♪ *Subiu o herói pela floresta a arder, / ouviu uma árvore antiga a dizer: / 'não sejas como o outro, o que nunca voltou' / e o herói chorou, e o herói ficou.* ♪ |
| Aranha-Mãe (15) | "Aranhas! Rima com 'manhas'. E com 'entranhas'. Vou deixar esta para o outono." |
| Golem de Cristal (20) | **"O Rei Sentado"** — ♪ *Na sala das colunas, o rei de cristal / ajoelhou-se ao azul, que é coisa fatal…* ♪ "…'fatal' não estava no rascunho. Saiu assim." |
| Serpente do Lodo (25) | "Lodo. Nada rima com lodo. 'Todo'. 'Modo'. 'Engodo'. Vou cantar só a parte da fuga." |
| Hidra do Pântano (30) | **"Sete Cabeças e Um Herói"** — canção para o público contar as cabeças em coro. Os bêbedos chegam sempre a nove. |
| Escorpião Imperador (35) | "Um imperador com cauda! Os imperadores normais não têm cauda. Ou têm e escondem." |
| Faraó Eterno (40) | **"O Rei Que Também Subiu"** — balada triste. ♪ *Eu também subi, eu também quis voltar…* ♪ "O Fausto pediu-me para não a cantar outra vez. Chorou duas vezes." |
| Yeti Ancião (45) | "Um yeti que guardava memórias. Vou fazer-lhe uma canção de embalar. Os yetis também dormem." |
| Dragão de Gelo (50) | **"Metade do Céu"** — a canção mais pedida da taberna. Refrão: ♪ *Metade! Metade! O resto é saudade!* ♪ |
| Capitão Esqueleto (55) | "Uma canção de marinheiro sobre um capitão de ossos! Os piratas do Porto vão adorar. Vou mandar-lha." |
| Leviatã (60) | **"O Mar Calmo"** — sem refrão. "Não consigo cantar a parte do Kai. Deixei-a em branco. O público canta um 'lá-lá-lá' por cima. É bonito." |
| Ferreiro Infernal (65) | "O Brom pediu-me para não fazer canção sobre isto. É a primeira vez que alguém me pede isso. Vou respeitar. Toco só o alaúde." |
| Kai — salvo (68) | "A canção do Kai! Finalmente! ♪ *Dois Jogadores, um nove e um zero…* ♪ Ele saiu da taberna a meio. Voltou para o fim." |
| Kai — vencido (68) | "Não há canção. Há silêncio. Às vezes o silêncio é a canção. Odeio quando isso é verdade." |
| Titã de Magma (70) | **"O Coração do Vulcão"** — com tambores. A taberna inteira bate nas mesas. A Dona Marta proíbe. Ninguém lhe obedece. |
| Lich Bibliotecário (75) | "Uma canção sobre silêncio para um lich que queria silêncio. Cantei-a baixinho. O Fausto aplaudiu sem fazer barulho." |
| Rei Sem Coroa (80) | **"O Rei Que Pediu Desculpa"** — a canção preferida do Gorvan. Ele nunca o disse. Pede-a com a cabeça. |
| Grifo Real (85) | "Voaste num grifo?! ♪ *E o herói subiu, nas asas de ouro…* ♪ Pronto, já tenho o primeiro verso. O resto inventa-se." |
| Serafim Caído (90) | **"Sem Palavras"** — só alaúde. O Dia da Subida silencioso. "Desta vez não há letra. Não há rima para o que ouviste." |
| Guardião do Tempo (95) | "Cinco andares. Já estou a compor a última canção. Tenho medo de a acabar. Volta para eu a poder cantar." |

---

## 8. Cenas de coração

### ❤️ 2 — A canção exagerada

| | |
|---|---|
| ID | `cena_lucien_2` |
| Quando | 2 ❤️ · entrar na Taberna numa sexta, 20:00–23:00 |
| Onde | Taberna, cheia |
| Quem | herói, Lucien, clientes (Brom, Tobias, Kai se estiver na cidade) |
| Música | `taberna` → a canção do Lucien |

🎬 O Lucien vê o herói entrar e para a música a meio. Aponta.
- **Lucien** *(feliz)*: "Senhoras e senhores! {Ele/Ela} chegou! A estrela da minha nova canção!"
- 🎬 Toca. ♪ *Com uma espada de treino e um olhar de leão, / derrotou mil javalis com uma só mão! / E quando o Ent Ancião o tentou esmagar, / o herói disse 'não' e pôs-se a dançar!* ♪
- **Brom** *(da mesa)*: "Isso não aconteceu!"
- **Lucien** *(feliz)*: "Aconteceu na canção!"

▶ **"Não foi bem assim…"**
▶ **(Fazer uma vénia.)**

- *(não foi)* **Lucien** *(normal)*: "Claro que não foi! A verdade é pequena. As canções são grandes. É para isso que servem." ⚙ +30
- *(vénia)* 🎬 a taberna aplaude. **Lucien** *(feliz)*: "Isso! Tens jeito de palco! Vou escrever-te um papel no teatro!" ⚙ +30

⚙ 5% de desconto na Taberna.

### ❤️ 4 — Conta-me uma história

| | |
|---|---|
| ID | `cena_lucien_4` |
| Quando | 4 ❤️ · Praça, 9:00–12:00, banco da fonte |
| Onde | Praça da Torre |
| Quem | herói, Lucien |
| Música | `ascendia_dia` (só alaúde) |

- **Lucien** *(normal)*: "Senta-te. Estou bloqueado. Preciso de uma história verdadeira. Não exagerada. Uma tua. Pequena."

▶ **"A noite em que o Kai me salvou do lobo."**
▶ **"O primeiro jantar na estalagem."**
▶ **"O dia em que caí ao rio do andar 3."**

- *(lobo)* **Lucien** *(feliz)*: "O rival que salva! É a melhor história que existe. Vou chamar-lhe 'O Número Redondo'." ⚙ canção nova na Taberna
- *(jantar)* **Lucien** *(feliz)*: "Uma canção sobre sopa! Ninguém faz canções sobre sopa! Vai ser a primeira!" ⚙ a Dona Marta fica com +30 amizade quando a ouve
- *(rio)* **Lucien** *(a rir)*: "Caíste ao rio?! Isto é ouro! Comédia! A taberna vai chorar a rir!"
- **Lucien** *(normal)*: "Obrigado, musa. As histórias pequenas são as que ficam. As grandes, as pessoas esquecem-se dos pormenores."

⚙ +30 · desbloqueia os **minijogos de ritmo** do Lucien (tocar com ele na Taberna: `docs/ATIVIDADES.md`).

### ❤️ 6 — Café da Selva

| | |
|---|---|
| ID | `cena_lucien_6` |
| Quando | 6 ❤️ · `andar_maximo >= 21` · Taberna, 16:00–18:00 (vazia) |
| Onde | Taberna |
| Quem | herói, Lucien |
| Música | `selva_tambores` (versão de alaúde) |

- **Lucien** *(triste)*: "Perdi a voz. Bem, não perdi. Está cansada. Seis anos a cantar todas as noites. Na caravana bebíamos café da selva para a voz."
- **Lucien** *(normal)*: "O café cresce no pântano. Dez grãos chegam para um mês. Trazes-me? Pago com uma canção. E com dinheiro. Mais com canção."

⚙ Missão **R3_13 Café da Selva** (secção 9). O Lucien aceita jantar em tua casa (e toca à sobremesa).

### ❤️ 8 — A canção da terra dele

| | |
|---|---|
| ID | `cena_lucien_8` |
| Quando | 8 ❤️ · quando a Cidade Errante está num andar, à noite, depois de o Lucien voltar de a visitar |
| Onde | Taberna, depois de fechar (2:00), só os dois |
| Quem | herói, Lucien |
| Música | sem música: só o Lucien, sem rimas |

🎬 A taberna está vazia, as cadeiras em cima das mesas. O Lucien está sentado no palco sem chapéu.
- **Lucien** *(triste)*: "Fui ver os meus pais à tartaruga. O meu pai está velho. Já não consegue tocar tambor. Agora toca a minha irmã."
- **Lucien** *(triste)*: "Pediu-me para voltar. Eu disse que não. Que aqui tinha uma coisa para cantar. Ele perguntou o quê. Eu disse: alguém que sobe."
- **Lucien** *(normal)*: "Vou tocar-te a canção que ele me cantava quando eu era pequeno. Na caravana. Não rima. É na língua antiga da tartaruga."
- 🎬 Toca. É lenta, simples, bonita. Não tem graça nenhuma. Não exagera nada.
- **Lucien** *(triste)*: "Chama-se 'Para Quem Fica'. É sobre as pessoas que ficam em terra quando a caravana parte. Nunca a toquei para ninguém."

▶ **"É a mais bonita que já tocaste."**
▶ **"Vais voltar para eles?"**

- *(bonita)* **Lucien** *(feliz, a chorar)*: "É, não é? E não tem uma única rima. Que vergonha para mim." ⚙ +30
- *(voltar)* **Lucien** *(normal)*: "Um dia. Quando a tua canção estiver acabada. Não antes. Prometi a mim mesmo." ⚙ +30

⚙ 15% de desconto na Taberna. Passa a mandar **cartas** com versos (e um doce).

### ❤️ 10 — A Balada do Jogador nº 10 000

| | |
|---|---|
| ID | `cena_lucien_10` |
| Quando | 10 ❤️ · `missao(N_LUCIEN_3) == concluida` · Praça, sábado, 21:00 |
| Onde | palco da Praça, com a cidade inteira |
| Quem | herói, Lucien, os NPCs de Ascendia, os pais do Lucien (vieram da Cidade Errante) |
| Música | `tema_lucien` → **"A Balada do Jogador nº 10 000"** |

🎬 A Praça está cheia. Na primeira fila, um casal velho com roupas da caravana: os pais do Lucien.
- **Lucien** *(feliz)*: "Esta noite não exagero nada. Prometo. É a primeira canção verdadeira que escrevo. Do princípio ao fim."
- 🎬 Toca. A câmara passa pelas caras dos NPCs enquanto a canção conta, verso a verso, a aventura do herói **com os feitos reais do jogador** (os bosses vencidos, o Kai salvo ou não, a escolha da aldeia Sssar, os amigos com mais corações).
- 🎬 No último refrão, a cidade canta com ele. Até a Freya. Até o Gorvan, sem som.
- **Lucien** *(feliz)*: "Ainda não tem fim. O fim és tu que escreves. Eu só canto o que trazes."
- 🎬 Desce do palco e dá-lhe o alaúde.
- **Lucien** *(normal)*: "Leva-o lá para cima. Toca-o quando estiveres com medo. Os teus companheiros vão ouvir. E vão lutar melhor."

⚙ **Alaúde do Lucien**: tocar dá bónus a ti e aos companheiros (canções de ataque, defesa e cura). Título *Herói da Balada*.

---

## 9. Missões

### R3_13 — Café da Selva (6 ❤️, `andar_maximo >= 21`)
- **Passo**: trazer **10 Café da Selva** (região 3).
- **Entregar** — **Lucien** *(feliz)*: "O cheiro! A voz volta só de cheirar. Toma: a receita do Café Forte da minha mãe. Dá velocidade às mãos. Às minhas dá velocidade às cordas." ⚙ receita **Café Forte** · +150

### N_LUCIEN_2 — Inspiração (4 ❤️)
- **Pedir** — **Lucien**: "Estou sem ideias. Mostra-me cinco troféus de bosses. Não precisas de mos dar. Só quero ver. E tocar. E cheirar, talvez."
- **Passo**: mostrar **5 troféus de bosses** diferentes (ficam contigo).
- **Entregar** — **Lucien** *(feliz)*: "Cinco monstros, cinco versos! A canção chama-se 'A Parede do Herói'. Vou estreá-la sexta." ⚙ canção nova na Taberna (+10 amizade com todos quando tocada) · +100

### N_LUCIEN_3 — O Concerto (8 ❤️)
- **Pedir** — **Lucien** *(nervoso, raro)*: "Quero fazer um concerto na Praça. O maior da história da cidade. Preciso de ajuda. De muita ajuda."
- **Passos**:
  1. Pedir licença ao **Governador Aldric** (ele dá: "Assinado. Carimbado. Em triplicado. Não quero barulho depois da meia-noite. Quero às onze e meia.").
  2. Pedir ao **Brom** um palco de ferro (precisa de 20 Lingote de Ferro).
  3. Pedir à **Elva** um fato novo para o Lucien ("Vou fazê-lo bonito. Ele vai fazê-lo ridículo. É a natureza dele.").
  4. Convidar **5 NPCs** (qualquer um com 4+ ❤️) e mandar uma carta à Cidade Errante (Senhora Vagar) para os pais do Lucien virem.
- **Entregar** — no dia marcado, o concerto acontece: com 10 ❤️, é a **cena de 10 ❤️**; senão, uma versão mais curta da Balada. ⚙ +200

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lucien_estado_vida` | `vida_pct < 30` | surpresa | "Estás ferid{o/a}! Isso dá uma balada trágica! …Desculpa. Igreja. Agora. Depois canto." |
| `lucien_estado_sapo` | `estado(sapo)` | feliz | "Um sapo que entra na taberna! É o início de uma piada! Não, és tu. Pior. Melhor!" |
| `lucien_estado_silencio` | `estado(silencio)` | triste | "Não consegues falar? É a coisa mais triste do mundo. Toco por ti." |
| `lucien_comp_kai` | `companheiro(kai)` | feliz | "O Kai! O protagonista da minha melhor canção! Senta-te, canto-a outra vez. Não fujas!" |
| `lucien_comp_gorvan` | `companheiro(gorvan)` | feliz | "O Mestre Gorvan a subir outra vez! Vou fazer-lhe uma canção! Ele vai dizer 'Hmm'. É um sim." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `lucien_serv_rumor` | Rumor do dia | normal | "Ouvi dizer que… {rumor}. Mas eu oiço muita coisa." |
| `lucien_serv_cancao` | Pedir uma canção | feliz | "Uma canção sobre {feito}! Já! ♪ …♪ Pronto. A taberna inteira gostou. Vê as caras." |
| `lucien_serv_minijogos` | abrir minijogos (andar 30+) | feliz | "Cartas, dados ou braço de ferro? O braço de ferro é com a Freya. Escolhe bem." |
| `lucien_serv_minijogos_cedo` | antes do andar 30 | normal | "Os minijogos são para aventureiros com bolsos cheios. Volta depois do andar 30." |
| `lucien_serv_comida` | comprar comida/bebida | normal | "Fala com o taberneiro. Eu só sirvo música. Gratuita. Aceito gorjetas." |
| `lucien_serv_fechado` | antes das 16:00 | — | `[Sistema] A Taberna está fechada. O Lucien está na Praça a compor (de manhã) ou a dormir (à tarde).` |
