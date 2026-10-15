# Povoações da Região 1 — diálogos e missões

As pessoas que vivem **dentro da torre** nos andares 1–10, o que dizem e as **missões da região passo a passo**.
Perfis e recompensas: `docs/regioes/r01_floresta.md` (secções 7 e 8). Formato das condições: `docs/dialogos/README.md`.
As cenas da história (C1-01, C1-05…) estão em `docs/guiao/cap01_floresta.md`.

Os NPCs das povoações têm diálogos mais curtos do que os 20 de Ascendia: **não têm corações** (a amizade com eles é
a das missões), mas mudam de fala com o progresso, a hora e as missões.

---

## 1. Tibério — mercador das Zonas Seguras (todos os andares)

| | |
|---|---|
| Quem é | o irmão gémeo do Tobias: igual a ele, mas com o bigode virado para baixo e uma mochila do tamanho de um armário |
| Voz | bips graves e rápidos; fala como um vendedor de feira, sempre a puxar pela loja |
| Repete | "Preço de viagem!", "O meu irmão?", "Compra agora, agradece depois." |
| Loja | ver `docs/LOJAS.md`, secção 3.1 |

**Primeira conversa** (andar 1, depois do prólogo)
- **Tibério** *(feliz)*: "Um cliente! Bem-vindo à loja mais alta de Ascendia! Bem, mais baixa. É o andar 1."
- **Tibério** *(normal)*: "Sou o Tibério. Vendo em todas as Zonas Seguras da torre. Como lá chego? Segredo de negócio."
- **Tibério** *(desconfiado)*: "Já conheceste o meu irmão, o Tobias? Não acredites em nada do que ele diz. Sobre mim. Sobre os preços. Sobre nada."

**Falas**

| ID | Condição | Fala |
|---|---|---|
| `tiberio_01` | — | "Compra agora, agradece depois." |
| `tiberio_02` | — | "Preço de viagem! É mais caro porque eu trouxe isto às costas. Olha para as minhas costas." |
| `tiberio_03` | — | "O meu irmão? Vende sombra no inverno." |
| `tiberio_04` | `vida_pct < 30` | "Estás com mau aspeto. Tenho poções. Também tenho espelhos, mas não te recomendo." |
| `tiberio_05` | `hora entre 20 e 5` | "À noite os monstros mudam. Os meus preços não. Sou um homem de princípios." |
| `tiberio_06` | `andar_maximo >= 11` | "Lá em baixo é escuro, não é? Tochas. Tenho tochas. Tenho sempre tochas." |
| `tiberio_07` | `andar_maximo >= 31` | "O deserto! Água a preço de ouro. Literalmente. Não, é mentira. Mas quase." |
| `tiberio_08` | `andar_maximo >= 61` | "Vi o teu amigo de casaco azul a passar. Não comprou nada. Mau sinal. Quem não compra, não planeia voltar." |
| `tiberio_09` | `andar_maximo >= 91` | "Há quarenta anos que subo esta torre a vender. Nunca passei do 91. Tu vais passar. Leva poções." |
| `tiberio_10` | `missao(N_TOBIAS_1) == ativa` | "Uma caixa do meu irmão? Para mim? …Não vou chorar. Estou a vender. Dá cá." |
| `tiberio_11` | `missao(N_TOBIAS_3) == concluida` | "O meu irmão manda cumprimentos. Escreveu-me uma carta sem insultos. Uma! Guardei-a." |
| `tiberio_curta` | já falaste hoje | "Mais alguma coisa? Leva duas, dá jeito." |

---

## 2. Acampamento dos Lenhadores (andar 2)

### 2.1 Bruno Machadão — chefe dos lenhadores

| | |
|---|---|
| Voz | bips graves e altos; ri-se muito ("AH-AH!"); fala alto mesmo quando está perto |
| Repete | "AH-AH!", "braços", "Isto sim é madeira!" |
| Loja | ver `docs/LOJAS.md`, secção 3.2 |
| Primeira conversa | cena C1-01 (as salsichas do Kai) |

| ID | Condição | Fala |
|---|---|---|
| `bruno_01` | — | "AH-AH! Mais um dia, mais um tronco! Isto sim é vida!" |
| `bruno_02` | — | "A cidade lá em baixo é feita com a nossa madeira. Cada casa tem um bocado deste andar." |
| `bruno_03` | `hora entre 6 e 9` | "Bom dia! O primeiro golpe do dia é o mais bonito. Ouviste? TOC. Música." |
| `bruno_04` | `hora entre 20 e 23` | "À noite os lobos aproximam-se do fogo. Eu aproximo-me do fogo também. Somos parecidos." |
| `bruno_05` | `clima == chuva` | "Chuva! Os troncos ficam pesados e eu fico molhado. Mas a serração anda mais depressa." |
| `bruno_06` | `estacao == inverno` | "No inverno cortamos lenha para a cidade inteira. Ninguém em Ascendia passa frio por nossa causa!" |
| `bruno_07` | `arma_tipo == machado` | "Um machado! Agora sim pareces gente! AH-AH!" |
| `bruno_08` | `flag(kai_deve_salsichas)` | "Diz ao teu amigo do casaco azul que as salsichas continuam a contar. Com juros." |
| `bruno_09` | `boss_derrotado(javali_rei)` | "Venceste o Javali-Rei?! Os meus homens já podem ir ao andar 5 buscar maçãs! AH-AH!" |
| `bruno_10` | `boss_derrotado(ent_anciao)` | "A floresta está diferente. Mais calada. Os meus machados também estão. Fazemos uma pausa por respeito." |
| `bruno_11` | `missao(R1_13) == concluida` | "A minha Tina na cidade, a fazer poções… Tenho orgulho. E saudades. Mas sobretudo orgulho. E saudades." |
| `bruno_curta` | já falaste hoje | "AH-AH! Outra vez tu! Queres um tronco? Tenho troncos." |

**Perguntar sobre…**
- *A torre*: "A torre? Eu sei da torre até ao andar 3. Daí para cima é com vocês, os da janela azul."
- *Rumores*: "O Velho Cass jura que as estátuas do andar 8 andam. O Cass também jura que já foi bonito." · "As árvores do Bosque Escuro sussurram. Se ouvires três a dizer coisas por ordem, há tesouro." · "Há um slime com coroa nos primeiros andares. COROA! Se o vires, traz-me a coroa. Para a minha Tina."

### 2.2 Tina — filha do Bruno

| | |
|---|---|
| Voz | bips médios, rápidos; usa palavras difíceis mal aplicadas ("é uma reação… exotérmica? Isso existe?") |
| Quem é | 14 anos, sonha ser alquimista; tem um caderno cheio de receitas inventadas |

**Primeira conversa**
- **Tina** *(feliz)*: "És da cidade? Conheces a alquimista? A Selene? É verdade que ela explodiu a loja três vezes?"
- **Tina** *(normal)*: "Eu quero ser alquimista. O meu pai quer que eu seja lenhadora. Os troncos não explodem. É o problema."

| ID | Condição | Fala |
|---|---|---|
| `tina_01` | — | "Hoje misturei Erva Verde com Esporo e saiu… uma pasta. Uma pasta verde. Ainda não sei para que serve." |
| `tina_02` | — | "Li que o mel azul cura a tristeza. Dei ao pai. Ele ficou contente. Mas ele já estava contente." |
| `tina_03` | `hora entre 20 e 23` | "À noite leio à luz da fogueira. Já li o único livro do acampamento onze vezes. É sobre machados." |
| `tina_04` | `missao(R1_13) == ativa` | "Os livros! Trouxeste? Não? Ah. Está bem. Não estou desesperada. Estou um bocadinho desesperada." |
| `tina_05` | `missao(R1_13) == concluida` | *(em Ascendia, na Alquimia)* "{nome}! Estou a trabalhar com a Selene! Hoje só explodiu uma coisa e não fui eu!" |

### 2.3 Velho Cass — lenhador reformado

| | |
|---|---|
| Voz | bips lentos e baixos; faz pausas longas (…); começa frases com "No meu tempo…" |
| Quem é | lenhador reformado que conta histórias; ninguém acredita em metade |

**Primeira conversa**
- **Cass** *(normal)*: "Senta-te, senta-te. Os novos nunca se sentam. Correm para a torre como se ela fosse fugir."
- **Cass** *(normal)*: "No meu tempo… subi até ao andar 8. Vi coisas. Estátuas que andam. Ninguém acredita no velho Cass."

| ID | Condição | Fala |
|---|---|---|
| `cass_01` | — | "No meu tempo, os lobos tinham educação. Mordiam só uma vez." |
| `cass_02` | — | "Esta torre já cá estava quando o meu avô era menino. E o avô dele. E o avô do avô… Perdi a conta. A torre não." |
| `cass_03` | — | "As árvores daqui sussurram. Eu falo com elas. Às vezes respondem. Às vezes sou eu a responder por elas." |
| `cass_04` | `clima == nevoeiro` | "Nevoeiro… No lago do andar 9, o nevoeiro mostra coisas. Coisas que ainda não aconteceram, dizia a minha mulher." |
| `cass_05` | `andar_maximo >= 8 && missao(R1_09) != concluida` | "Viste as estátuas? Viste? Andam! Só quando não olhas! Eu sabia! EU SABIA!" |
| `cass_06` | `missao(R1_09) == concluida` | "Resolveste as estátuas! Agora já acreditam no velho Cass. Pelo menos tu. Já é um." |
| `cass_07` | `boss_derrotado(ent_anciao)` | "A Árvore-Mãe… No meu tempo ela cantava. Ouvia-se do andar 2, quando o vento vinha do norte. Hoje está calada." |

**Perguntar sobre…**
- *A torre*: "Dizem que no topo há um jardim. Dizem também que quem lá chega não volta. Eu digo: se tem jardim, também não voltava."
- *Rumores*: "Nas noites de lua cheia anda por aí um lobo preto com uma cicatriz no olho. Foge dele. Ou não fujas. Mas eu fugia." · "Às três da manhã, no lago, os fogos-fátuos levam a uma ilha que não existe de dia. Não sei o que lá está. Nunca tive coragem."

### 2.4 Tronco — o cão do acampamento

O Tronco não fala: ladra (`[Sistema]` traduz às vezes, como piada).

| Situação | O que acontece |
|---|---|
| Falar | 🎬 abana o rabo. `[Sistema] O Tronco quer festas.` (botão: Fazer festas → +1 felicidade, coração pequeno por cima dele) |
| Dar carne | 🎬 come e salta. Conta os dias seguidos. |
| 5 dias seguidos com carne | 🎬 segue-te até à saída do andar e senta-se na escada. `[Sistema] O Tronco não pode sair do andar 2. Mas acompanhou-te até aqui.` Título *Amigo do Tronco* |
| Com o teu animal de estimação | 🎬 os dois correm à volta da fogueira (animação de 4 s) |

---

## 3. Folhalta, a Aldeia Élfica (andar 7)

Primeira chegada: cena **C1-05** (o elevador de cesto, Lothiel, Faelan e Eldrin).

### 3.1 Anciã Lothiel — chefe da aldeia

| | |
|---|---|
| Voz | bips lentos e suaves, quase música; nunca levanta a voz; chama aos outros "filhos" (mesmo aos velhos) |
| Quem é | mais de mil anos. Era menina quando a floresta caiu na torre. Lembra-se de um rapaz da janela azul que dormiu na casa mais alta |
| O que nunca diz | o nome do rapaz (não o sabe) |

| ID | Condição | Fala |
|---|---|---|
| `lothiel_01` | — | "Bem-vindo, filho da janela. A aldeia é pequena, mas o chá é grande." |
| `lothiel_02` | — | "Antes da queda, o céu era verde ao fim da tarde. Aqui o teto é azul. Os jovens acham normal. Eu nunca me habituei." |
| `lothiel_03` | `hora entre 20 e 5` | "À noite, os mais velhos contam o céu antigo às crianças. Elas não acreditam. Faz parte." |
| `lothiel_04` | `missao(R1_08) == ativa` | "A Raiz Oca… Qualquer coisa lá dentro come a floresta. Sinto-o como uma dor de dentes. Com cuidado, filho." |
| `lothiel_05` | `missao(R1_08) == concluida` | "As raízes respiram melhor. Mas a Árvore-Mãe… continua cansada. Há coisas que nem tu podes limpar." |
| `lothiel_06` | `tem_item(pagina_diario_7)` | ver **cena da página 7** abaixo |
| `lothiel_07` | `boss_derrotado(ent_anciao)` | "A Mãe partiu. Sentimos todos. Mas deu-te a semente, não deu? Então não partiu toda." |
| `lothiel_08` | `andar_maximo >= 16` | "Encontraste os Fungoides? Gente boa. Falam devagar. Gosto de gente que fala devagar." |
| `lothiel_curta` | já falaste hoje | "Volta quando quiseres, filho. As árvores lembram-se de quem as visita." |

**Cena da página 7** (`cena_lothiel_pagina7` — ao falares com ela depois de apanhares a página 7)

- **Lothiel** *(surpresa)*: "Essa letra… Mostra-me."
- 🎬 Lothiel segura a página com as duas mãos. Lê em silêncio. Sorri devagar.
- **Lothiel** *(feliz)*: "'Uma menina perguntou-me de que árvore eu vinha.' …Era eu, filho. A menina era eu."
- **Lothiel** *(normal)*: "Foi há mil anos. Um rapaz da janela azul dormiu na casa mais alta. Tinha olhos tristes e ria-se de tudo."
- **Lothiel** *(normal)*: "Disse que vinha de um 'autocarro'. Ainda hoje não sei o que é um autocarro."
▶ **"É uma carroça grande, sem cavalos."**
▶ **"Como se chamava ele?"**
- *(carroça)* **Lothiel** *(feliz)*: "Sem cavalos! Então era mesmo de outro mundo. Obrigada. Esperei mil anos por essa resposta."
- *(nome)* **Lothiel** *(triste)*: "Nunca lhe perguntei. Era pequena. Achava que ele ia voltar para me dizer. Os da janela nunca voltam."
- **Lothiel** *(normal)*: "Ele subiu. Prometeu à Árvore-Mãe que descia para lhe contar o que via lá em cima. Nunca desceu."
⚙ flag `lothiel_conhece_aren` (conta para uma fala especial dela no final secreto).

### 3.2 Faelan — arqueiro élfico

| | |
|---|---|
| Voz | bips curtos e secos; frases de 3 a 5 palavras |
| Serviço | treino de arco (ver `docs/LOJAS.md`, secção 3.2) |

| ID | Condição | Fala |
|---|---|---|
| `faelan_01` | — | "Hm. Ainda estás vivo. Bom." |
| `faelan_02` | — | "Respira. Mira. Larga. Repete." |
| `faelan_03` | `arma_tipo == arco` | "Um arco. Finalmente alguém sensato." |
| `faelan_04` | `arma_tipo == martelo` | "Um martelo. Barulhento. Humano." |
| `faelan_05` | `hora entre 5 e 7` | "Madrugada. A melhor hora. Os alvos dormem." |
| `faelan_06` | depois do 1.º treino | "Melhor. Não bom. Melhor." |
| `faelan_07` | depois do 3.º treino | "Já não te ensino nada. …Vá. Quase nada." |
| `faelan_08` | `boss_derrotado(ent_anciao)` | "Obrigado. Pela Mãe. Não volto a dizer." |

### 3.3 Mira Folha-de-Prata — comerciante

| | |
|---|---|
| Voz | bips doces; fala de cada item como de uma pessoa |
| Loja | ver `docs/LOJAS.md`, secção 3.2 |

| ID | Condição | Fala |
|---|---|---|
| `mira_01` | — | "Bem-vinda, bem-vindo! Estas sementes são tímidas, mas crescem bem com amor e água." |
| `mira_02` | — | "O linho fino é fiado pelas avós da aldeia. Cada fio tem uma história. Não as conto, são compridas." |
| `mira_03` | abrir loja | "Escolhe com calma. As coisas boas não fogem. As más também não, infelizmente." |
| `mira_04` | comprar Sementes de Árvore Dourada | "Uma Árvore Dourada! Planta-a ao sol. E fala com ela. Elas gostam de conversa." |
| `mira_05` | vender | "Obrigada! Vou arranjar-lhe um bom dono." |

### 3.4 Eldrin — irmão mais novo da Selene

| | |
|---|---|
| Voz | bips rápidos e alegres; faz perguntas atrás de perguntas |
| Quem é | elfo de ~250 anos que parece ter 18; curioso, admira a irmã; nunca saiu de Folhalta |

| ID | Condição | Fala |
|---|---|---|
| `eldrin_01` | — | "Como é Ascendia? Há muitas pessoas? As casas são de pedra? As pessoas são de pedra? Não, isso era uma piada." |
| `eldrin_02` | — | "A minha irmã partiu há cem anos. Escreve uma carta por ano. Este ano ainda não escreveu. Deve estar a explodir coisas." |
| `eldrin_03` | `missao(R1_07) == concluida` | "Ela respondeu! Disse que eu escrevo mal. É a maneira dela de dizer que tem saudades." |
| `eldrin_04` | `boss_derrotado(ent_anciao)` | "A Árvore-Mãe… A Selene vai ficar triste. Diz-lhe tu, está bem? Eu não sei escrever coisas tristes." |
| `eldrin_05` | `andar_maximo >= 11` | "Já passaste o andar 10! Eu nunca saí deste andar. Um dia vou. Um dia. Quando a Anciã deixar. Daqui a uns cem anos." |

### 3.5 Tilly — criança élfica

| | |
|---|---|
| Voz | bips agudos e saltitantes |
| Quem é | menina élfica (60 anos, "isso é pequenina, para um elfo!"); tem uma raposa que fugiu |

| ID | Condição | Fala |
|---|---|---|
| `tilly_01` | `missao(R1_06) != concluida` | "A Pimenta fugiu! É a minha raposa! É laranja e faz 'iip'! Viste-a?" |
| `tilly_02` | `missao(R1_06) == concluida && animal == raposa` | "A Pimenta gosta de ti! Ela agora é tua. Mas eu posso visitá-la. Todos os dias. Combinado?" |
| `tilly_03` | `missao(R1_06) == concluida` | "Tenho outra raposa agora! Chama-se Pimenta Dois. Não foge. É de madeira." |
| `tilly_04` | — | "Sabes subir às árvores? Eu sei. Toda a gente aqui sabe. Os bebés sabem antes de andar." |

### 3.6 Fada Lumi — Clareira Secreta das Fadas (andar 4, meia-noite)

| | |
|---|---|
| Voz | sininhos em vez de bips; ri-se a meio das frases |
| Quem é | a mais velha das fadas da clareira; manda nas outras (mais ou menos) |
| Loja | ver `docs/LOJAS.md`, secção 3.2 |

**Primeira conversa** (entrar no Anel de Fadas à meia-noite)
- 🎬 As luzes do anel sobem em espiral. O herói fica pequeno, do tamanho de uma fada. A clareira enche-se de cogumelos-casa.
- **Lumi** *(feliz)*: "Hi-hi! Um grandão pequenino! Entraste no anel à hora certa. Ninguém entra à hora certa."
- **Lumi** *(normal)*: "Aqui não há lutas. Só trocas. Tu dás, nós damos. Às vezes nós roubamos. Mas aqui não. Aqui é loja."
- **Lumi** *(triste)*: "Perdemos o nosso Pó de Fada Dourado. Cinco pitadas. Espalhadas pelo andar. Sem ele, a clareira só abre à meia-noite."
⚙ Missão **R1_04** disponível.

| ID | Condição | Fala |
|---|---|---|
| `lumi_01` | — | "Hi-hi! Não toques nas asas. Fazem cócegas. A mim, não a ti." |
| `lumi_02` | `dia_semana == sexta` | "Sexta à meia-noite é festa! As fadas lá fora hoje não roubam. Quase." |
| `lumi_03` | `missao(R1_04) == concluida` | "Agora a clareira está sempre aberta para ti. Entra pelo anel a qualquer hora. Até ao meio-dia! Que escândalo!" |
| `lumi_04` | — | "As fadas travessas são minhas primas. Desculpa por elas. Não, não desculpa. Elas divertem-se." |

---

## 4. Missões da região, passo a passo

Formato: **quem dá · quando abre · passos · falas-chave · recompensa**. Os IDs das falas são `<missao>_<nº>`.

### R1_01 — Lobos à Noite
| | |
|---|---|
| Quem dá | Bruno (andar 2) |
| Abre | depois da cena C1-01 |
| Recompensa | 200 ouro · Machado de Cobre (qualidade Boa) |

1. **Pedir** — **Bruno** *(sério, raro nele)*: "Os lobos andam a rondar o acampamento à noite. Levaram duas salsichas e um sapato. Mata-me oito, está bem? Só à noite: de dia escondem-se."
2. **Passo**: matar **8 Lobos Cinzentos** no andar 2, entre as 20:00 e as 5:00. Contador: `[Sistema] Lobos à Noite: lobos (n/8).`
3. **Durante** (de dia) — **Bruno**: "De dia não há lobos. Dorme agora, caça logo. É o que eles fazem."
4. **Entregar** — **Bruno** *(feliz)*: "OITO! Os meus homens já dormem descansados! Toma este machado, fui eu que o afiei. Dá para lobos e para árvores. AH-AH!"
5. **Extra**: se trouxeres o **sapato** (cai do 8.º lobo): "O meu sapato! Já tinha comprado outro, mas vou usar os dois. Um em cada pé!" (+50 ouro)

### R1_02 — Madeira para a Ponte
| | |
|---|---|
| Quem dá | Bruno |
| Abre | depois de R1_01 |
| Recompensa | 150 ouro · abre o projeto **Ponte do Rio** em Ascendia (Governador Aldric) |

1. **Pedir** — **Bruno**: "O Governador quer uma ponte nova em Ascendia, para o Porto. Quarenta troncos de carvalho. Eu tenho trinta e nove. Brincadeira! Tenho zero."
2. **Passo**: entregar **40 Madeira de Carvalho** ao Bruno (pode ser aos bocados).
3. **Durante** — **Bruno**: "Já vamos em {n}! A ponte vai ter o teu nome. Num bocadinho pequeno. Numa tábua."
4. **Entregar** — **Bruno**: "Quarenta! Vou mandar tudo para a cidade. Fala com o Governador: ele vai fazer um discurso. Vai demorar. Leva um banco."
5. ⚙ Projeto Ponte do Rio fica disponível na Câmara (`docs/CIDADES.md`, secção 1.4).

### R1_03 — Aprende a Pescar
Dada pelo **Pip** no andar 3. Falas e passos em `docs/dialogos/pip.md` (secção 9). Ensina o minijogo de pesca
(`tut_pesca`). Recompensa: Cana de Bambu · receita Truta Grelhada.

### R1_04 — O Anel de Fadas
| | |
|---|---|
| Quem dá | Fada Lumi (Clareira Secreta, andar 4, meia-noite) |
| Recompensa | a loja das fadas fica sempre aberta · Asas de Fada (cosmético) |

1. **Pedir** — ver a primeira conversa da Lumi (secção 3.6).
2. **Passos**: encontrar **5 Pós de Fada Dourados** no andar 4. Estão em sítios fixos (brilham e tilintam a 5 m):
   - no topo do cogumelo mais alto do Bosque Gigante (N2 no mapa);
   - dentro do Cogumelo Oco, num frasco na prateleira;
   - no meio do Pântano de Esporos (precisa de Antídoto ou Máscara de Linho);
   - com uma Fada Travessa que o roubou (aparece sempre perto do Anel de Fadas; mata-a ou… dá-lhe um Mel Azul e ela devolve);
   - debaixo de um cogumelo pequeno que só se mexe quando lhe bates 3 vezes (perto da Zona Segura).
3. **Durante** — **Lumi**: "{n} pitadas! Hi-hi! Faltam {5-n}. Não, não sei onde estão. Se soubesse, ia eu. Tenho asas."
4. **Entregar** — 🎬 as fadas atiram o pó ao ar e a clareira brilha em dourado.
   - **Lumi** *(feliz)*: "A clareira está inteira! A partir de hoje, entras quando quiseres. E toma: asas. São de enfeite. Não voam. Mas ficam lindas."

### R1_05 — Mel Azul
Dada pela **Dona Marta** (Ascendia). Falas em `docs/dialogos/marta.md` (secção 9). Trazer 5 Mel Azul do andar 6
(as abelhas atacam quem tira mel das colmeias). Recompensa: receita Panquecas de Mel Azul · ❤️ Dona Marta.

### R1_06 — A Raposa Perdida
| | |
|---|---|
| Quem dá | Tilly (Folhalta) |
| Recompensa | **Raposa da Floresta** (animal de estimação) |

1. **Pedir** — **Tilly** *(a chorar)*: "A Pimenta fugiu ontem! Foi pelo elevador e desceu ao chão da floresta! Lá em baixo há lobos! Ajudas-me? Por favor por favor por favor?"
2. **Passo 1**: descer ao chão da floresta e encontrar **pegadas de raposa** perto do elevador (brilham ao de leve).
3. **Passo 2**: seguir as pegadas (são 12, em zigue-zague; a cada 3 há uma pista: um tufo de pelo, um ovo partido, um sapato pequeno — "Isto é meu! Ela leva tudo!").
4. **Passo 3**: no fim, a raposa está encurralada por **3 Lobos Cinzentos**. Vencê-los sem que a raposa leve dano (se levar, foge e volta ao passo 2).
5. **Passo 4**: aproximar devagar (segurar o botão de interagir 3 s). `[Sistema] A raposa cheira-te a mão.`
6. **Entregar** — 🎬 a raposa salta para os braços da Tilly, depois olha para ti e salta para os teus.
   - **Tilly** *(feliz e triste)*: "Ela… gosta mais de ti. Está bem. Está bem! Fica com ela. Mas trata-a bem. E dá-lhe ovos. Ela adora ovos."
   - ⚙ **Raposa da Floresta** (animal de estimação). `[Sistema] Novo animal de estimação: Pimenta, a Raposa da Floresta.` (o nome pode mudar-se)

### R1_07 — Cartas para Selene
| | |
|---|---|
| Quem dá | Eldrin (Folhalta) |
| Recompensa | receita Poção Élfica · ❤️ Selene |

1. **Pedir** — **Eldrin** *(feliz)*: "Vais voltar à cidade? Levas uma carta à minha irmã? É importante! Bem, não é importante. É uma carta. Mas é importante para mim."
2. **Passo 1**: levar a **Carta do Eldrin** à Selene (Ascendia). A reação dela está em `docs/dialogos/selene.md` (secção 9).
3. **Passo 2**: a Selene escreve a resposta (no dia seguinte, das 9:00 às 18:00). Levar a **Resposta da Selene** ao Eldrin.
4. **Entregar** — 🎬 o Eldrin lê a carta, ri-se, e lê outra vez.
   - **Eldrin** *(feliz)*: "Diz que eu escrevo mal, que tenho de comer mais e que está orgulhosa de mim! As três coisas! Nunca diz as três!"
   - **Eldrin** *(normal)*: "Toma. A receita da Poção Élfica. A Selene sabe-a, mas nunca ta daria: ela diz que é 'demasiado fácil'."

### R1_08 — O Mal das Raízes
| | |
|---|---|
| Quem dá | Anciã Lothiel (Folhalta) |
| Abre | depois da cena C1-05 |
| Recompensa | **Arco Raiz-Viva** (arma secreta) · 800 ouro |

1. **Pedir** — **Lothiel** *(séria)*: "Há uma raiz oca no chão da floresta, antiga como a aldeia. Qualquer coisa lá dentro come as raízes da Mãe. Os nossos arqueiros não voltaram. Vais tu?"
2. **Passo 1**: encontrar os **4 Cristais de Seiva** no andar 7 (ver o mapa: `docs/mapas/r01_floresta.md`). O Poço da Lua, em noite de lua cheia, mostra onde está a Raiz Oca.
3. **Passo 2**: pôr os 4 cristais nos 4 altares → abre a **Toca das Raízes** (masmorra, `docs/regioes/r01_floresta.md`, secção 9).
4. **Passo 3**: atravessar as 3 salas e vencer a **Larva Ancestral**.
5. **Na masmorra**: na sala 2 estão os **2 arqueiros élficos** desaparecidos, presos em casulos. Libertá-los (bater nos casulos) → voltam a Folhalta (+falas: "Pensámos que era o fim. Obrigado, filho da janela.").
6. **Entregar** — **Lothiel** *(feliz)*: "As raízes respiram. Sinto-as. E trouxeste os nossos filhos de volta."
   - **Lothiel** *(normal)*: "Este arco foi feito com a madeira da primeira árvore que caiu connosco. Espera há mil anos por mãos que o mereçam."

### R1_09 — As Estátuas que Andam
| | |
|---|---|
| Quem dá | Velho Cass (andar 2) |
| Abre | `andar_maximo >= 8` |
| Recompensa | **Anel do Vigia** (+10% visão no nevoeiro e no escuro) |

1. **Pedir** — **Cass**: "Vais ao andar 8? Há uma praça com quatro estátuas e quatro pedestais vazios. No meu tempo… as estátuas estavam nos pedestais. Alguém as tirou. Ou elas saíram."
2. **Passo**: resolver o puzzle das **Estátuas** (andar 8): levar cada estátua ao seu pedestal. As estátuas só andam quando **não** estás a olhar para elas; olha para elas quando chegam ao pedestal para as "prender".
3. **Durante** — **Cass**: "Andam, não andam? Diz que andam. Preciso que alguém diga que andam."
4. **Entregar** — **Cass** *(a chorar de alegria)*: "EU SABIA! Quarenta anos a dizer! Toma o meu anel. Era do meu pai. Ele também via coisas no nevoeiro."

### R1_10 — O Rei do Lago
Dada pelo **Pip** depois de R1_03. Falas e passos em `docs/dialogos/pip.md` (secção 9). Pescar o **Rei do Lago
Nevoento** (andar 9, com nevoeiro, 5:00–7:00, Isco Dourado recomendado). Recompensa: título *Rei do Lago* · Isco Dourado ×5.

### R1_11 — Caça ao Slime Rei
| | |
|---|---|
| Quem dá | quadro da Guilda (rank E) |
| Recompensa | 500 ouro · Coroa de Gel |

1. **Quadro** — `"PROCURA-SE: Slime grande, com coroa. Visto nos andares 1 a 4. Perigoso para as plantações e para a dignidade. — Guilda"`
2. **Passo**: encontrar e vencer o **Slime Rei** (aparece com 3% ao entrar nos andares 1–4; com esta missão ativa, a hipótese sobe para **15%**).
3. **Entregar** à Lyra — **Lyra** *(surpresa)*: "Uma coroa de gel?! Tem um peixe lá dentro! Porque é que tem um peixe lá dentro?! Fica com ela. Não, a sério, fica com ela."

### R1_12 — Uivos de Cicatriz
| | |
|---|---|
| Quem dá | Capitã Freya (Quartel, Ascendia) |
| Abre | `andar_maximo >= 7` e rank E |
| Recompensa | 600 ouro · **Manto Cicatriz** |

1. **Pedir** — **Freya** *(séria)*: "Há um lobo preto nos andares da floresta. Cicatriz branca no olho. Já mandou três aventureiros para a Igreja. Trata dele. De preferência antes de ele tratar de ti."
2. **Passo**: vencer o **Lobo Cicatriz** (andares 2, 7 ou 9, só à noite; 5%, ou 20% com lua cheia; com a missão ativa, 30% na lua cheia). O Sistema avisa: `[Sistema] Um monstro com nome apareceu neste andar: Lobo Cicatriz.`
3. **Entregar** — **Freya** *(feliz, raro)*: "Bom trabalho. A sério. Bom trabalho. …Não te habitues a que eu diga isto."

### R1_13 — Livros para a Tina
| | |
|---|---|
| Quem dá | Tina (andar 2) |
| Abre | depois de falares com a Tina 3 dias diferentes |
| Recompensa | a Tina muda-se para Ascendia (ajudante da Selene: poções 10% mais baratas) |

1. **Pedir** — **Tina** *(envergonhada)*: "Posso pedir-te uma coisa? Na cidade há uma biblioteca, não há? Traz-me três livros de alquimia. Eu devolvo! Eu juro! Eu leio depressa!"
2. **Passo 1**: falar com o **Velho Fausto** (Biblioteca). **Fausto**: "Livros para uma jovem alquimista? Os livros não são para emprestar a qualquer um… mas a quem os quer ler, sim. Leva estes três. E diz-lhe que os quero de volta com dedadas de poção, como deve ser."
3. **Passo 2**: levar os **3 Livros de Alquimia** à Tina.
4. **Passo 3** (no dia seguinte): a Tina tem uma ideia. **Tina**: "Li os três! Duas vezes! Pai… eu quero ir para a cidade. Trabalhar com a Selene."
   - 🎬 o Bruno fica calado (nunca está calado). Depois ri-se, com os olhos molhados.
   - **Bruno**: "AH-AH! A minha filha, alquimista na cidade! Vai! Vai antes que eu mude de ideias!"
5. **Passo 4**: falar com a **Selene** sobre a Tina. **Selene**: "Uma ajudante? Que sabe ler? E que não tem medo de explosões? Contratada!"
6. ⚙ A Tina vive em Ascendia (Alquimia). Poções da Selene −10%.

---

## 5. Missões da Guilda (rank F) da região

As 3 primeiras do quadro (`docs/MISSOES.md`). O quadro mostra o texto; a Lyra comenta ao aceitar e ao entregar.

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_F_01 Limpeza de Slimes | "Slimes nos campos do andar 1. Precisam de ser… desslimados. 10 slimes." | "A primeira missão! Que emoção! Para mim. Para ti deve ser só slimes." | "Dez slimes! A Guilda agradece! Toma, e lava as botas antes de entrar." |
| G_F_02 Ervas para a Igreja | "A Irmã Célia precisa de 10 Erva Verde para poções. Entregar na Igreja." | "Ervas para a Igreja. Missão bonita. Ninguém se magoa. Exceto as ervas." | "A Irmã Célia mandou dizer obrigada e que és uma boa alma. Eu mandei dizer que já sabia." |
| G_F_03 Primeiro Mapa | "Explorar 80% do andar 1 para atualizar o mapa da Guilda." | "Desenha bem, está bem? O último mapa que recebi tinha um dragão no andar 1. Não há dragões no andar 1." | "Que mapa bonito! Vou pendurá-lo. Ao lado do mapa com o dragão." |
