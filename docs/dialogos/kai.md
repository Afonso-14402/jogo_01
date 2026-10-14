# Kai — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.7. Dados: `dados/dialogos/kai.json`.
As cenas da história com o Kai (P3–P8, C1-02 a C1-11…) estão em `docs/guiao/`. Aqui estão as conversas **normais**,
que mudam com a **fase da história** (fim da secção 1).

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios, rápidos e secos; quando fica envergonhado os bips cortam a meio da frase |
| Como fala | frases curtas, provocador, faz-se de duro; transforma tudo em aposta ou corrida; quando fala da irmã fica calmo e lento. Usa palavras do mundo real (telemóvel, autocarro, ténis, ramen) que ninguém em Ascendia percebe |
| Repete | "Tsc.", "Ha!", "número redondo", "Não é por ti.", "Bora.", "Aposto que…" |
| Tiques | coça a nuca quando está envergonhado (animação `cocar_nuca`); toca no bolso do casaco onde guarda o telemóvel quando pensa na Yui (`tocar_bolso`) |
| Nunca diz | "obrigado" (começa a dizer "Obrig…" e muda para "Fixe."), até ser salvo no andar 68; nunca diz que tem medo (só na cena de 2 ❤️) |
| Chama ao herói | "número redondo" (desde o prólogo); `{nome}` só nos momentos sérios e, com 8+ corações, mais vezes |
| Skill Única dele | **Passo Fantasma** (esquiva duas vezes; por isso tem o Dash no duelo) |
| Rotina | segunda a sábado: torre de dia · **Praça a treinar 19:00–23:00** (ao pé da fonte) · **domingo: Taberna 12:00–22:00** (comida "que parece do mundo real") |

### As fases do Kai

As falas do Kai mudam com a história. As secções 2 a 6 e 8 **só existem quando o Kai está na cidade**:
`missao(H_14) != concluida || flag(kai_salvo)`. Esta parte da condição **não se repete** em cada tabela.

| Fase | Condição | Onde está | Como fala |
|---|---|---|---|
| **A — Rival** | `missao(H_14) != concluida` | rotina normal (ver acima) | provocador, competitivo, saudades escondidas |
| **B — Desaparecido** | `missao(H_14) == concluida && missao(H_16) != concluida` | **ausente** (ver secção 10: quem o substitui) | — |
| **C — Frio** | `missao(H_16) == concluida && missao(H_17) != concluida` | nunca em Ascendia; às vezes ao longe nas Zonas Seguras dos andares 61–67 | curto, frio, olhos a brilhar azul |
| **D — Salvo** | `flag(kai_salvo)` | Ascendia; depois de `missao(H_22) == concluida` vive no **Último Posto** (andar 91) e só desce ao domingo | mais calmo, envergonhado; já diz "obrigado" |
| **E — Vencido** | `flag(kai_vencido)` | **ausente até ao andar 100** (aparece no final) | — |

Nas fases B, C e E **não se ganha nem se perde amizade** com o Kai (a regra de −10 por semana sem falar fica desligada).

---

## 2. Primeira conversa

Depois da cena P8 (prólogo), a 1.ª vez que carregas em **Conversar** com ele (Praça, à noite):

- **Kai** *(surpresa)*: "Tu outra vez? Não me digas que já chegaste ao andar 5. …Não chegaste. Ótimo."
- **Kai** *(normal)*: "De dia estou lá em cima. À noite treino aqui, ao pé da fonte. Ao domingo como na Taberna."
- **Kai** *(feliz)*: "Se quiseres levar uma tareia a sério, eu dou duelos de treino. Mas só depois do andar 5. Não bato em principiantes."
- **Kai** *(normal)*: "E não digas à Lyra que estou aqui. Ainda lhe devo um relatório. De há três meses."
- *(se `origem == atrasado`)* **Kai** *(feliz)*: "E pára de correr para todo o lado. O autocarro já foi."

⚙ Abre o menu do Kai: **Conversar · Perguntar sobre… · Missões · Duelo de treino** (depois de H_04) **· Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_dia_01` | `hora entre 19 e 20` | normal | "Acabei de descer da torre. Não, não te digo até onde fui. Segredo de rival." |
| `kai_dia_02` | `hora entre 19 e 20` | normal | "Mil espadadas antes de dormir. Vou na trezentas e doze. Não me distraias. …Trezentas e treze." |
| `kai_dia_03` | `hora entre 21 e 23` | normal | "A esta hora a cidade cala-se. Lá em casa havia sempre carros a passar. Aqui só há grilos." |
| `kai_dia_04` | `hora entre 21 e 23` | triste | "Às vezes olho para o céu e penso que a Yui está a olhar para o mesmo. Não está. Mas penso." |
| `kai_dia_05` | — | normal | "Ah, ainda estás viv{o/a}? Que sorte a da torre." |
| `kai_dia_06` | — | normal | "Não é por ti. Eu só… passava por aqui. Ao pé da fonte. Onde estou sempre. Pronto." |
| `kai_dia_07` | — | zangado | "O Bruno ainda fala das salsichas? Eram três. TRÊS. Pago quando chegar ao topo. Com juros." |
| `kai_dia_08` | — | normal | "A Dona Marta põe-me sempre mais batatas no prato. Eu digo que não quero. Como-as todas." |
| `kai_dia_09` | — | zangado | "A Lyra quer relatórios. Relatórios! Eu mato monstros, não escrevo redações sobre eles." |
| `kai_dia_10` | — | feliz | "Aposto que hoje subiste menos do que eu. Não me digas. Quero continuar a achar." |
| `kai_dia_11` | — | normal | "A Mia pediu-me para lhe ensinar o meu corte. Disse que não. Ensinei-lhe metade." |
| `kai_dia_12` | `dia_semana == domingo` | feliz | "Domingo é dia de comida que parece comida a sério. Senta-te. Não, não pago. Senta-te na mesma." |
| `kai_dia_13` | `dia_semana == domingo && hora entre 12 e 14` | normal | "Isto chama-se 'pão com carne'. Eu chamo-lhe quase-hambúrguer. Falta-lhe tudo. Mas sabe a casa." |
| `kai_dia_14` | `dia_semana == segunda` | zangado | "Segunda-feira. Na escola eu odiava segundas. Aqui odeio na mesma, por hábito." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_dia_20` | `estacao == primavera` | zangado | "Primavera. Tudo cheio de flores. A cidade inteira cheira a perfume de avó." |
| `kai_dia_21` | `estacao == verao` | normal | "O meu casaco é de inverno. Do meu mundo. Não o tiro. Não me perguntes porquê." |
| `kai_dia_22` | `estacao == verao && hora entre 21 e 23` | triste | "No verão a Yui e eu íamos ver o fogo de artifício à ponte. Ela tapava os ouvidos e ria-se." |
| `kai_dia_23` | `estacao == outono` | normal | "Outono. Lá em casa começavam as aulas. Nunca pensei ter saudades das aulas." |
| `kai_dia_24` | `estacao == inverno` | zangado | "A Dona Marta tricotou-me um cachecol. É cor-de-rosa. Uso-o. Cala-te." |
| `kai_dia_25` | `estacao == inverno && clima == neve` | feliz | "Neve! …Quer dizer, neve. Normal. Não vou fazer bonecos. Talvez um. Pequeno. Com espada." |
| `kai_dia_26` | `clima == chuva` | normal | "Chuva. Os ténis fazem squish. Squish, squish. Não te rias." |
| `kai_dia_27` | `clima == trovoada` | feliz | "Trovoada. Ótimo para treinar: ninguém ouve os meus gritos de ataque." |
| `kai_dia_28` | `clima == nevoeiro` | triste | "Com nevoeiro não se vê a torre. É o único dia em que me esqueço dela. Um bocadinho." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_dia_40` | `andar_maximo < 5` | feliz | "Andar 5. Jantar. Lembras-te da aposta? Eu lembro-me. Tenho fome." |
| `kai_dia_41` | `boss_derrotado(javali_rei) && andar_maximo < 11` | zangado | "O atalho do andar 5 tinha lama até aos joelhos. Os ténis ainda não secaram. Desde esse dia." |
| `kai_dia_42` | `flag(kai_sabe_do_anterior) && missao(H_14) != concluida` | triste | "'O anterior.' Ainda penso nisso. Se chegou ao topo e não desceu, é porque não quis. Tem de ser." |
| `kai_dia_43` | `andar_maximo >= 11 && andar_maximo < 21` | feliz | "Corrida até ao andar 20, lembras-te? Já tenho um plano. O plano é correr mais." |
| `kai_dia_44` | `boss_derrotado(golem_cristal) && missao(H_14) != concluida` | normal | "Tens casa. Eu durmo na estalagem há meses. Não tenho inveja. Tenho um bocadinho." |
| `kai_dia_45` | `andar_maximo >= 31 && missao(H_14) != concluida` | triste | "Sabes que dia é hoje no meu mundo? Eu também não. Perdi a conta. Isso assusta-me mais do que os monstros." |
| `kai_dia_46` | `andar_maximo >= 41 && missao(H_14) != concluida` | normal | "Lá em cima o Sistema agora diz 'Boa, Jogador.' Ha. Ficou simpático. Não gosto de quem fica simpático de repente." |
| `kai_dia_47` | `andar_maximo >= 51 && missao(H_14) != concluida` | normal | "Há um navio no 53 com um diário de Jogadores antigos. Se lá estiver escrito como se sai, quero ser o primeiro a ler." |
| `kai_dia_48` | `flag(kai_salvo)` | triste | "Toda a gente me olha como se eu fosse fugir outra vez. Não vou. Pelo menos não sem te avisar." |
| `kai_dia_49` | `flag(kai_salvo)` | normal | "A Lyra tirou o meu nome do quadro dos desaparecidos. Ficou a marca da tinta. Ainda se lê." |
| `kai_dia_50` | `flag(kai_salvo) && missao(H_22) == concluida` | feliz | "O Último Posto tem uma cama dura, um ferreiro sem um olho e vista para as estrelas. É perfeito." |
| `kai_dia_51` | `rank >= C` | feliz | "Rank C? Eu sou rank C há… duas semanas. Mas fui primeiro. Isso conta." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_dia_60` | `coracoes(kai) >= 2` | normal | "Vi um baú que não consegui abrir. Digo-te onde é. Não é por ti. É para o baú não ficar sozinho." |
| `kai_dia_61` | `coracoes(kai) >= 3` | feliz | "Treinei o teu golpe. O de esquivar e atacar logo. Não é teu. Agora é meu." |
| `kai_dia_62` | `coracoes(kai) >= 4` | feliz | "A minha irmã ia gostar de ti. Ia achar-te esquisit{o/a}." |
| `kai_dia_63` | `coracoes(kai) >= 5` | normal | "Guardei-te lugar na Taberna. Não é guardado. É só que ninguém se senta lá. Porque eu não deixo." |
| `kai_dia_64` | `coracoes(kai) >= 6` | triste | "Às vezes sonho que chego a casa e a Yui não me reconhece. Depois treino até ficar cansado demais para sonhar." |
| `kai_dia_65` | `coracoes(kai) >= 6 && andar_maximo >= 16` | normal | "O Gizmo diz que consegue carregar o meu telemóvel com uma manivela. Já partiu duas. Eu deixo-o tentar." |
| `kai_dia_66` | `coracoes(kai) >= 8` | feliz | "Já não aposto contra ti. Aposto contigo. Soa mal. Mas é verdade." |
| `kai_dia_67` | `coracoes(kai) >= 10` | feliz | "Melhor amig… rival. Melhor rival. É o que tu és. Não mudo a palavra." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_dia_70` | `origem == atrasado` | normal | "Ainda corres como quem perdeu o autocarro. Eu também estava atrasado no dia em que caí. Temos isso em comum." |
| `kai_dia_71` | `origem == jogador` | normal | "Tu jogavas jogos destes? Então diz-me como é que se ganha. …Pois. Ninguém sabe." |
| `kai_dia_72` | `origem == ajudante` | normal | "Andaste a carregar as compras da Dona Marta. Eu vi. Da próxima chama-me. Não chames. Chama." |
| `kai_dia_73` | `origem == dormir` | triste | "Estavas a dormir quando caíste? Ao menos não viste o azul a engolir a rua toda." |
| `kai_dia_74` | `skill_unica == passo_fantasma` | zangado | "Esquivas duas vezes seguidas? Esse é o MEU truque. Cópia barata." |
| `kai_dia_75` | `skill_unica == lamina_espiritual` | normal | "A tua espada lança ondas de luz. A minha só corta. Ensina-me. Não. Ensina." |
| `kai_dia_76` | `skill_unica == olho_do_sistema` | normal | "Vês os números dos monstros? Então diz-me o meu. …Não. Não quero saber." |
| `kai_dia_77` | `skill_unica == segunda_vida` | triste | "Segunda Vida não é para te armares em herói. Uma vida chega para cada um." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `kai_curta_1` | normal | "Já falámos hoje. Não te habitues." |
| `kai_curta_2` | zangado | "Que foi? Estou a treinar. Trezentas e catorze." |
| `kai_curta_3` | feliz | "Ainda aqui? Vai dormir, número redondo." |
| `kai_curta_4` | normal | "Tsc. Outra vez tu. …Olá." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Kai** *(normal)*: "Cem andares. Dizem que quem chega ao topo pode voltar para casa. É a única coisa que interessa."
- **Kai** *(normal)*: "Eu acho que isto é um jogo e que alguém está a jogar connosco. Só não sei quem é que tem o comando."
- *(se `flag(kai_sabe_do_anterior)`)* **Kai** *(triste)*: "E há o 'anterior'. Se lá em cima não houver porta… não. Há porta. Tem de haver."
- *(se `flag(kai_salvo)`)* **Kai** *(normal)*: "O Sistema queria muito que eu chegasse primeiro. Porquê eu? Porque é que lhe interessa quem chega? Não percebo. Não gosto de não perceber."

### 4.2 O andar atual

O Kai fala da **região do andar mais alto** a que chegaste. As regiões 6 a 10 só têm fala quando ele está na cidade.

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta: fácil. O coelho do andar 1 não conta. …Conta. Mandou-me duas vezes para a estalagem." |
| 2 Cavernas | "Cavernas: escuro e morcegos. Leva tochas. Eu não levei. Acho que ainda tenho um morcego no casaco." |
| 3 Pântano | "Pântano: a lama entra nos ténis. Os meus ténis eram brancos. ERAM." |
| 4 Deserto | "Deserto: quente como o meu quarto no verão. Sem ventoinha. Sem nada. Bebe água antes de teres sede." |
| 5 Gelo | "Gelo: escorregas mais do que andas. Eu escorreguei até à Zona Segura. Cheguei primeiro, isso é que interessa." |
| 6 Oceano | (só antes de H_14) "Oceano: andares inteiros de mar. E há aquele navio no 53. Vou lá antes de ti. Desta vez vou mesmo." |
| 7 Vulcão | (salvo) "Vulcão… Não me perguntes pelo vulcão. Pergunta outra coisa. …Está bem. É quente. Pronto." |
| 8 Reino Assombrado | (salvo) "Fantasmas, esqueletos e uma biblioteca que grita. Eu grito mais alto. Ganho sempre." |
| 9 Céu | (salvo) "Ilhas a voar. Se eu cair, apanhas-me? …Esquece. Não caio. Não olhes para baixo. Eu não olho." |
| 10 Abismo | (salvo) "O Último Posto é a minha casa agora. A segunda. A primeira tem a Yui." |

### 4.3 Rumores

O Kai diz **1 rumor por dia**: coisas que viu lá em cima, quase sempre pistas de segredos.

| ID | Condição | Rumor |
|---|---|---|
| `kai_rumor_01` | — | "No moinho do andar 1 há uma corda. Puxa-a. Não te digo o que acontece. Puxa." |
| `kai_rumor_02` | `andar_maximo >= 4` | "No andar 4, à meia-noite, o anel de cogumelos leva-te às fadas. Saí de lá com asas. Tirei-as logo. LOGO." |
| `kai_rumor_03` | `andar_maximo >= 5` | "No andar 5, atira uma maçã e os javalis vão comê-la. Eu atirei três. Comi a quarta." |
| `kai_rumor_04` | `andar_maximo >= 9` | "No andar 9 os troncos afundam se ficares parado. O Pip diz que pescou lá uma baleia. Eu acho que pescou um tronco." |
| `kai_rumor_05` | `andar_maximo >= 11` | "Há corridas de vagonetas no andar 11. O recorde é meu. Vai tentar. Vais perder." |
| `kai_rumor_06` | `rank >= D` | "A Arena da Capitã Freya tem ranking. Eu estou lá. Bem lá em cima. Vai ver. Lê devagar." |
| `kai_rumor_07` | `andar_maximo >= 28` | "No andar 28 há um ninho gigante com um ovo perdido. Devolve-o e dão-te uma pena com as cores todas. Eu quero uma." |
| `kai_rumor_08` | `andar_maximo >= 49` | "Há uma coroa de gelo no 49. Pus-a. Fui rei um minuto. Melhor minuto da minha vida aqui dentro." |
| `kai_rumor_09` | `andar_maximo >= 51 && missao(H_14) != concluida` | "Os fantasmas do navio do 53 têm números. Como nós. Quero ver os números deles. Quero ver se há algum perto do meu." |
| `kai_rumor_10` | `flag(kai_salvo) && andar_maximo >= 71` | "No Reino há uma biblioteca que grita se fizeres barulho. Eu espirrei. Nunca mais lá volto." |
| `kai_rumor_11` | `flag(kai_salvo) && andar_maximo >= 81` | "Dizem que no céu há um pote de ouro no fim de um arco-íris. A sério. Se for mentira, a culpa é do Lucien." |
| `kai_rumor_12` | `flag(kai_salvo) && andar_maximo >= 97` | "Na Cidade dos Perdidos há um tipo, o Rafa, que toca músicas do meu mundo. Tocou uma que eu conhecia. Tive de sair." |

### 4.4 A vida dele

| Corações | Fala |
|---|---|
| 0 | "A minha vida? Lobos, monstros, treino. E ganhar-te. É uma vida cheia." |
| 2 | "No meu mundo eu andava na escola. Era mau a matemática e bom a correr. Aqui correr serve. Matemática não." |
| 4 | "A Yui tem medo do escuro. Eu deixava a luz do corredor acesa. Quem é que a deixa acesa agora?" |
| 6 | "No dia em que caí, eu estava atrasado. Fiquei a jogar à bola. A Yui estava à porta da escola à minha espera. Eu nunca cheguei." |
| 8 | "Quando eu voltar, a primeira coisa que faço é ir buscá-la à escola. A horas. Pela primeira vez a horas." |
| 10 | "Quero voltar para casa. Mas já não é só por mim. É para lhe contar de ti. Ela não vai acreditar. Eu também não acreditava." |

---

## 5. Presentes

**Adora:** Hambúrguer de Javali, Ramen de Fungo, Pena Arco-Íris · **Gosta:** carne e pratos de carne (Carne de Javali,
Assado de Javali, Espetada de Coelho…) · **Detesta:** flores (todas), Gel de Slime. O resto é **neutro**.
"Gosta de desafios" e "detesta que te armes em herói" não são itens: são **escolhas de diálogo** (as atrevidas dão +30,
as de herói dão −30, ver `docs/SISTEMAS.md`, secção 15). Só se pode dar presentes nas fases A e D.

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "Isto… é comida a sério. Do meu mundo. Quase. Não fales comigo durante cinco minutos." · "Ha! Sabes o que eu gosto. Isso é batota. Continua." |
| Gosta | "Carne! Finalmente alguém com juízo. Fixe." · "Obrig… Fixe. É fixe. Vou comer já." |
| Neutro | "Hm. Uma coisa. Guardo. Algures." · "Para que é que serve isto? …Não digas. Eu descubro." |
| Não gosta | "Tsc. Vou fingir que não vi." |
| Detesta | "Uma flor. Para mim. Tens noção de que eu mato lobos?" · "Gel de Slime?! Está a mexer! Tira isso de ao pé de mim!" |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Hambúrguer de Javali | "Um hambúrguer. Um hambúrguer a sério. …Não estou a chorar. Tem cebola. Não tem cebola? Então tem pó." |
| Ramen de Fungo | "Ramen. Cheira à loja da esquina. A Yui dizia que eu ia virar massa. Vou virar massa hoje, com todo o gosto." |
| Pena Arco-Íris | "As cores todas… A Yui desenha tudo com arco-íris. Até a mim. Guardo-a para ela. Quando eu voltar." |
| Arroz com Ovo do Kai | "Fizeste o MEU arroz? …Está melhor do que o meu. Não digas a ninguém. Muito menos à Yui." |
| Rosa de Sangue | "É uma flor. Detesto flores. …Mas é rara. Está bem. Só esta. E não contes a ninguém." (conta como **adora**) |
| Presa do Javali-Rei | "A presa do nosso javali! Do empate! Vou pendurá-la por cima da cama. Para me lembrar que eu ia ganhar." |

---

## 6. Aniversário e festivais

**Aniversário (Verão, dia 24)** — só nas fases A e D (se ele não estiver na cidade, não há conversa):
- Sem presente: **Kai** *(normal)*: "Faço anos hoje. Não, não digo quantos. Mais do que tu, isso é que importa." · *(triste)* "A Yui fazia-me sempre um desenho. Este ano não há desenho."
- Com presente que adora: **Kai** *(feliz)*: "No dia dos meus anos. Logo isto. …Tens de parar de acertar sempre. Fico sem respostas."
- Com outro presente: **Kai** *(feliz)*: "Um presente? Para mim? Obrig… Fixe. Muito fixe." · *(se `flag(kai_salvo)`)* "Obrigado. Pronto. Disse. Aprendi isso contigo."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Uma festa inteira de flores. É o meu pesadelo com música." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Kai** *(surpresa)*: "Dançar? EU? …Uma música. Uma. E se alguém se rir, duelo." ⚙ dança · +100 amizade |
| F_02 Festival da Pesca | "Pescar o maior peixe em dez minutos? Aposto que te ganho. …Como é que se lança a linha? Não me digas. Eu descubro." |
| F_03 Noite dos Espíritos | "No meu mundo há uma noite assim, com abóboras. A Yui vestia-se de abóbora. Era uma abóbora muito zangada." |
| F_04 Festival da Estrela | "Amigo secreto. Calhou-me o Pip. O que se dá a quem dorme o dia todo? …Uma almofada. Já está." |
| F_05 Dia da Subida | "Comem todos à tua conta e o Lucien canta sobre ti. Para o ano canta sobre mim. Vais ver." |
| F_05 (depois do Titã de Magma, salvo) | "Toda a gente me olha. Eu olho para o chão. O chão é muito interessante. Tem… pedras." |
| F_06 Concurso da Casa | "Eu durmo na estalagem. A minha casa é uma cama e um prego para o casaco. Ganho em arrumação." |
| F_07 Noite das Lanternas | "Ponho uma por mim. Do lado de lá, alguém deve achar que eu não voltei. Assim fica… justo." |

> Nas fases B, C e E o Kai não está nos festivais (no Dia da Subida do Leviatã, os outros NPCs notam a falta dele).

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória. O Kai chega quase sempre **um dia depois** do herói: é a piada dele.

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `kai_boss_javali_rei` | "Empate, digam o que disserem. Eu conto o atalho da lama como dano. Ao javali e a mim." |
| Ent Ancião (10) | `kai_boss_ent_anciao` | "A cidade toda em festa e eu só penso no andar 11. Escuro. Ótimo. Bora." |
| Aranha-Mãe (15) | `kai_boss_aranha_mae` | "Uma aranha do tamanho de uma carroça. Eu ia lá amanhã. Amanhã. Ia mesmo." |
| Golem de Cristal (20) | `kai_boss_golem_cristal` | "O Golem ajoelhou-se para a janela azul? Não gosto disso. Não gosto de coisas que se ajoelham para o Sistema." |
| Serpente do Lodo (25) | `kai_boss_serpente_lodo` | "Os meus ténis foram ao pântano contigo. Ficaram lá. Descansem em paz." |
| Hidra do Pântano (30) | `kai_boss_hidra_pantano` | "Quantas cabeças cortaste? Eu cortava mais. Não tenho provas. Mas cortava." |
| Escorpião Imperador (35) | `kai_boss_escorpiao_imperador` | "Imperador de quê? Da areia? Toda a areia é dele? Que tédio de império." |
| Faraó Eterno (40) | `kai_boss_farao_eterno` | "O faraó também foi Jogador. Subiu e ficou lá dentro. Não. Eu não fico em lado nenhum. Eu volto." |
| Yeti Ancião (45) | `kai_boss_yeti_anciao` | "Um yeti! Lá em casa havia um desenho animado com um yeti. A Yui chorava no fim. Eu também. Não contes." |
| Dragão de Gelo (50) | `kai_boss_dragao_gelo` | "Metade. Cinquenta andares, número redondo. Mais cinquenta e eu vejo a Yui. Só mais cinquenta…" |
| Capitão Esqueleto (55) | — | — *(fase B: o Kai está desaparecido)* |
| Leviatã (60) | — | — *(fase B: o Kai está desaparecido)* |
| Ferreiro Infernal (65) | — | — *(fase C: o Kai não vem à cidade nem fala contigo)* |
| Kai — salvo (68) | `kai_boss_kai_salvo` | "…Não olhes para mim assim. Eu sei o que fiz." · "Obrigado. Pronto. Disse. É a primeira vez. Não te habitues." |
| Kai — vencido (68) | — | — *(fase E: o Kai desaparece até ao andar 100)* |
| Titã de Magma (70) | `kai_boss_tita_magma` | "O vulcão adormeceu. Eu quase não acordei. Tu acordaste-me. À espadeirada, mas acordaste." |
| Lich Bibliotecário (75) | `kai_boss_lich_bibliotecario` | "Uma biblioteca que grita. Eu ia gritar de volta. Tu não deixaste. Ainda bem, acho." |
| Rei Sem Coroa (80) | `kai_boss_rei_sem_coroa` | "O Gorvan chorou nas Catacumbas. Não lhe digas que eu vi. Eu chorei no 68. Ninguém diz nada a ninguém." |
| Grifo Real (85) | `kai_boss_grifo_real` | "Voei nas costas de um grifo. Tenho medo de alturas, lembras-te? Agora tenho mais." |
| Serafim Caído (90) | `kai_boss_serafim_caido` | "Estás calad{o/a} desde o anjo. Não me contes o que ele disse. Ainda não. Primeiro chegamos." |
| Guardião do Tempo (95) | `kai_boss_guardiao_tempo` | "Cinco andares. Prometemos chegar os dois. Estamos a chegar, número redondo. Estamos a chegar." |

> As falas dos bosses 70 a 95 só existem com `flag(kai_salvo)`. Depois do **Administrador** (andar 100) as falas
> dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

As cenas de 2 a 8 ❤️ acontecem nas fases A ou D. Se o Kai já vive no Último Posto, passam-se ao domingo à noite em
Ascendia. A cena de 10 ❤️ só existe **se o salvaste**.

### ❤️ 2 — Corrida até ao topo da muralha

| | |
|---|---|
| ID | `cena_kai_2` |
| Quando | 2 ❤️ · entrar na Praça entre as 20:00 e as 23:00 (não ao domingo) |
| Onde | Praça da Torre → telhados → topo da muralha norte |
| Quem | herói, Kai |
| Música | `ascendia_noite` |

🎬 O Kai está em cima da borda da fonte a esticar as pernas. Salta para o chão quando te vê.

- **Kai** *(feliz)*: "Chegaste a tempo. Corrida. Daqui até ao topo da muralha norte. Pelos telhados."
- **Kai** *(normal)*: "Quem perder diz uma coisa verdadeira. Uma coisa que nunca disse a ninguém."

▶ **"Bora!"**
▶ **"E se eu cair de um telhado?"**

- *(Bora)* **Kai** *(feliz)*: "Isso! Três, dois—" 🎬 *arranca no "dois".* ⚙ +30
- *(cair)* **Kai** *(normal)*: "Cais. Levantas-te. É assim que se sobe. Três, dois—" 🎬 *arranca no "dois".*

⚙ Minijogo de corrida pelos telhados (60 s). Há um atalho pelos barris da Forja.

- *(se ganhares)* **Kai** *(zangado → feliz)*: "…Tsc. Arrancaste antes do 'um'. Está bem. Eu também. Uma coisa verdadeira."
- *(se perderes)* **Kai** *(feliz)*: "HA! Diz lá a tua coisa verdadeira." ▶ **"Tenho saudades de casa."** / ▶ **"Gosto de ser teu rival."**
  → **Kai** *(normal)*: "…Pois. Está bem. Eu também digo uma. É justo."
- 🎥 Os dois sentados no topo da muralha. A cidade iluminada lá em baixo; a torre enorme ao fundo.
- **Kai** *(triste)*: "Tenho medo de alturas. Desde pequeno. Não consigo subir a um escadote."
- **Kai** *(normal)*: "E subo uma torre de cem andares todos os dias. A torre gosta de piadas."
- **Kai** *(feliz)*: "Se contares a alguém, digo à Lyra que foste tu que lhe roubaste a caneta boa."

⚙ Os duelos de treino com o Kai dão **+5% de XP de skills** (o Kai não tem loja).

### ❤️ 4 — A fotografia

| | |
|---|---|
| ID | `cena_kai_4` |
| Quando | 4 ❤️ · subir ao telhado da torre do relógio da Praça entre as 21:00 e as 23:00 |
| Onde | telhado da torre do relógio (o sítio do Kai, cena C1-11) |
| Quem | herói, Kai |
| Música | `amizade` (versão lenta) |

🎬 O Kai está sentado no telhado com um telemóvel na mão. O ecrã está preto.

- **Kai** *(normal)*: "Shh. Estou a poupar energia. A do telemóvel e a minha."
- **Kai** *(normal)*: "É do meu mundo. Faz chamadas, fotos, jogos… Aqui faz de pisa-papéis."
- **Kai** *(triste)*: "Tem um por cento de bateria. Há meses que tem um por cento. Ligo-o uma vez por estação. Só uma."
- 🎬 Coça a nuca.
- **Kai** *(normal)*: "Hoje… ligo-o contigo. Não é por ti. É que sozinho custa."
- 🎬 Carrega no botão. O ecrã acende-se: uma luz branca, não azul, na cara dos dois.
- 🎥 Grande plano do ecrã: uma menina de tranças sem um dente da frente, a fazer um V com os dedos, ao lado de um Kai mais novo com a mochila da escola.
- **Kai** *(feliz)*: "É a Yui. Tinha seis anos aqui. Caiu-lhe o dente nesse dia e quis uma foto 'para a história'."
- **Kai** *(triste)*: "Já deve ter dentes novos. Não sei como é a cara dela agora."

▶ **"Ela é a tua cara."**
▶ **"Vais vê-la outra vez."**
▶ *(ficar em silêncio)*

- *(tua cara)* **Kai** *(zangado → feliz)*: "Não é nada! …É um bocadinho. Os olhos." ⚙ +30
- *(vais vê-la)* **Kai** *(normal)*: "Vou. Nem que tenha de partir a torre ao meio."
- *(silêncio)* **Kai** *(normal)*: "…Ainda bem que não disseste que vai correr tudo bem. Toda a gente diz isso." ⚙ +30
- 🎬 O ecrã pisca: **0%**. Fica preto.
- **Kai** *(triste, a rir)*: "Pronto. Acabou-se o um por cento. Ainda bem que foi contigo a ver."
- **Kai** *(normal)*: "Toma. É a única coisa que sei cozinhar. Fazia-a à Yui quando a minha mãe trabalhava de noite."

⚙ Recebe a receita **Arroz com Ovo do Kai** · flag `kai_foto_yui`.

### ❤️ 6 — Duelo ao luar

| | |
|---|---|
| ID | `cena_kai_6` |
| Quando | 6 ❤️ · `clima == sol` · entrar na Praça entre as 21:00 e as 23:00 |
| Onde | campo de treino da Guilda (Bairro da Guilda), com lua |
| Quem | herói, Kai, Mestre Gorvan (ao longe, na muralha) |
| Música | silêncio → `duelo_kai` (versão lenta, só cordas) |

🎬 O Kai espera no meio do campo de treino, de espada na mão. Não é a espada de treino: é a dele.

- **Kai** *(normal)*: "Os duelos de treino são para meninos. Hoje é a sério. Sem parar aos 30%."
- **Kai** *(sério)*: "Preciso de saber se sou forte o suficiente. Para chegar ao topo. Para… o que for preciso."

▶ **"Está bem. A sério."**
▶ **"Não quero lutar contigo a sério."**

- *(a sério)* **Kai** *(feliz)*: "Isso!" ⚙ +30
- *(não quero)* **Kai** *(zangado)*: "Não é para quereres. É para lutares. Em guarda!"

⚙ Luta: o Kai tem o teu nível e usa o **Corte em Cruz**. Acaba quando um dos dois chega a 10% de vida (ninguém morre).

- *(se ganhares)* **Kai** *(triste)*: "…Outra vez. Ganhaste outra vez."
- *(se perderes)* **Kai** *(normal)*: "Ganhei. E não me sinto melhor. Estranho."
- 🎬 Os dois deitados na relva, a olhar para a lua.
- **Kai** *(sério)*: "Ouve. Se um dia eu ficar esquisito… se eu deixar de ser eu…"
- **Kai** *(sério)*: "Bate-me. Até eu voltar a ser eu. Prometes?"

▶ **"Prometo."**
▶ **"Isso não vai acontecer."**

- *(prometo)* **Kai** *(feliz)*: "Ótimo. E eu faço o mesmo por ti. Mas com mais força." ⚙ +30
- *(não vai)* **Kai** *(normal)*: "Pois. Claro que não. …Mas se acontecer, lembra-te desta noite."
- 🎥 Lá em cima, na muralha, o Gorvan esteve a ver. Vira as costas e vai-se embora devagar.

⚙ flag `kai_luar` (conta para o duelo do andar 68, missão **R7_11**). O Kai aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — Voltamos os dois

| | |
|---|---|
| ID | `cena_kai_8` |
| Quando | 8 ❤️ · entrar na Estalagem entre as 20:00 e as 23:00 |
| Onde | Estalagem "Ninho do Viajante", a mesa do canto (a mesma do jantar da aposta, C1-04) |
| Quem | herói, Kai, Dona Marta |
| Música | `amizade` (com lareira) |

🎬 O Kai está na mesa do canto com dois pratos à frente. Puxa a cadeira com o pé.

- **Kai** *(normal)*: "Senta-te. Hoje pago eu. Sem aposta. Não te habitues."
- **Dona Marta** *(feliz)*: "Pediu-me o prato mais caro. Para ti, não para ele. Anota isto, que não se repete."
- **Kai** *(zangado)*: "Dona Marta!"
- 🎬 A Dona Marta afasta-se a rir. O Kai come devagar, pela primeira vez.
- **Kai** *(normal)*: "Lembras-te do jantar do javali? Eu disse que tinha de chegar primeiro. Mais rápido do que tu."
- **Kai** *(sério)*: "Mudei de ideias. Não quero chegar primeiro. Quero chegar contigo."
- 🎬 Tira do bolso dois porta-chaves iguais: um gatinho de plástico com uma espada.
- **Kai** *(triste)*: "A Yui deu-me dois. Disse: 'Um é para o teu melhor amigo.' Eu não tinha nenhum. Fiquei com os dois."
- **Kai** *(normal)*: "…Toma. Não é nada de especial. É de plástico."
- **Kai** *(sério)*: "Voltamos os dois. Tu para a tua casa, eu para a minha. Combinado?"

▶ **"Voltamos os dois."**
▶ **"E se só um puder voltar?"**

- *(voltamos)* **Kai** *(feliz)*: "Combinado. Aperta aqui." 🎬 *aperto de mão, como no andar 5.* ⚙ +30
- *(só um)* 🎬 O Kai fica calado muito tempo. **Kai** *(triste)*: "Então vais tu. Não. Vou eu. …Não sei. Não me perguntes isso." **Kai** *(sério)*: "Voltamos os dois. Ponto."

⚙ **Porta-chaves do Gato** (acessório: +5% de velocidade; com o Kai na equipa, +5% de crítico para os dois) · flag `kai_promessa_2`.
⚙ Duelos de treino com **+15% de XP de skills**. O Kai manda **cartas** de uma linha ("Treina. — K.") com Carne de Javali,
uma Poção de Vida ou um desenho teu mal feito.

### ❤️ 10 — Treino no Último Posto

| | |
|---|---|
| ID | `cena_kai_10` |
| Quando | 10 ❤️ · `flag(kai_salvo) && missao(H_22) == concluida` · chegar ao Último Posto (andar 91) entre as 5:00 e as 7:00 |
| Onde | Último Posto, a beira da plataforma, com as estrelas por baixo |
| Quem | herói, Kai, Dorn (ao fundo, na forja) |
| Música | `tema_kai` (guitarra + piano) |

🎬 O Kai treina sozinho na beira da plataforma. Não olha para baixo.

- **Kai** *(normal)*: "Chegaste cedo. Ou eu cheguei tarde. Não dormi."
- **Kai** *(feliz)*: "Treina comigo. A sério. Os dois ao mesmo tempo, como no 68… mas do mesmo lado."

⚙ Minijogo de ritmo: o **Corte em Cruz a dois** (carregar no botão ao mesmo tempo que o Kai, 5 vezes).

- 🎬 Sentam-se. O Kai tira o telemóvel do bolso, ligado a uma manivela cheia de fios.
- **Kai** *(feliz)*: "O Gizmo conseguiu. Três por cento. É um génio. Não lhe digas."
- 🎬 Mostra o ecrã: uma foto tua, na festa do Titã, de boca cheia.
- **Kai** *(feliz)*: "Tirei-te esta na festa. Estás horrível. É a minha preferida."
- **Kai** *(sério)*: "No 68 eu ia deixar-te para trás. Por uma promessa do Sistema. Tu não me deixaste para trás. Nem quando eu te bati."
- **Kai** *(normal)*: "Lá em cima… se houver uma porta para casa, não sei o que vai acontecer. Ninguém sabe."
- **Kai** *(sério)*: "Mas sei uma coisa. Seja o que for, chegamos os dois."
- 🎬 Dá-te uma espada embrulhada no casaco azul.
- **Kai** *(normal)*: "Pedi ao Dorn. Duas espadas iguais, com um bocado da minha espada velha. A que te salvou do lobo."

▶ **"Chegamos os dois."**
▶ **"O número redondo agradece."**

- *(chegamos)* **Kai** *(feliz)*: "Ha! Isso. Agora levanta-te. Ainda não acabámos o treino."
- *(número redondo)* **Kai** *(feliz, a rir)*: "Já não és só um número. Nunca foste, {nome}."

⚙ Recebe a **Lâmina Gémea** (com o Kai na equipa, ambos fazem +20%). O Kai passa a ter a fala `kai_dia_67`.
⚙ Se o Kai foi **vencido** no andar 68, esta cena nunca acontece.

---

## 9. Missões

### N_KAI_1 — Corrida (0 ❤️, depois de H_04)

- **Pedir** — **Kai** *(feliz)*: "Corrida a sério, sem javalis pelo meio. Andar 3, da Zona Segura até à escada. Quem ganhar é o Rival oficial. Com título."
  ▶ **"Bora!"** ⚙ missão iniciada · ▶ **"Agora não."** → "Medo. Normal. Eu espero. Não muito."
- **Regras**: a corrida começa quando tocas no cristal do andar 3 com a missão ativa. O Kai vai pelas Pontes de Madeira
  e demora **2:30** (2:00 no Difícil). Tu vais por onde quiseres (as Comportas, se já as abriste, são um atalho).
  Se perderes, podes repetir no dia seguinte.
- **Durante** (o Kai grita de longe): "Lentinho!" · "Pontes são para turistas!" · (se cair na água funda) "NÃO OLHES!"
  - Se passares pelo Pip a dormir na Margem Norte: **Pip** *(a dormir)*: "…corridas… que cansaço…"
- **Ganhar** — **Kai** *(zangado → feliz)*: "…Tsc. Ganhaste. És o meu Rival. Oficial. Com R grande." ⚙ título *Rival* · +100 amizade
- **Perder** — **Kai** *(feliz)*: "HA! Amanhã outra vez? Dou-te vantagem. Dez segundos. Não, cinco."

### N_KAI_2 — Comida de Casa (3 ❤️, `boss_derrotado(javali_rei)`)

- **Pedir** (Taberna, domingo) — **Kai** *(normal)*: "Sabes o que é um hambúrguer? Pão redondo, carne, queijo, tomate. Aqui ninguém sabe. Vou inventá-lo. Bem, reinventá-lo. Ajudas?"
  ▶ **"Claro!"** ⚙ missão iniciada · ▶ **"Agora não."** → "Está bem. Vou comer pão com carne. Outra vez. Triste."
- **Passos**:
  1. Trazer **1 Carne de Javali, 1 Farinha, 1 Queijo e 1 Tomate**.
  2. Ir com o Kai à cozinha da Estalagem. **Dona Marta** *(desconfiada)*: "Carne dentro de pão? Redondo? E queijo por cima? Isso é comida ou é um chapéu?"
  3. A 1.ª tentativa corre sempre mal: **Kai** *(triste)*: "Isto é uma sandes. Uma sandes triste." A Dona Marta ensina o pão redondo e à 2.ª sai bem.
- **Entregar** — 🎬 o Kai dá uma dentada e fica parado.
  - **Kai** *(triste → feliz)*: "…É isto. É mesmo isto. Sabe a sexta à noite. Sabe a casa."
  - **Kai** *(zangado)*: "Não estou a chorar. É a cebola. Não leva cebola? Então é o queijo."
  - ⚙ receita **Hambúrguer de Javali** · +100 amizade · a Taberna passa a servir Hambúrguer de Javali aos domingos.
- **Parte 2** (`missao(N_KAI_2) == concluida && andar_maximo >= 16`) — **Kai** *(feliz)*: "Agora ramen. Dizem que em Mycélia há um fungo azul que sabe a caldo. Traz dois. E farinha. E um ovo."
  - Entregar **2 Fungo Azul, 1 Farinha e 1 Ovo** → **Kai** *(feliz)*: "A Yui dizia que eu ia virar massa. Hoje viro." ⚙ receita **Ramen de Fungo** · +100 amizade

### R7_11 — O Kai (história, andar 68)

Começa sozinha depois de H_16, na **Plataforma do Duelo**. A cena completa vai para `docs/guiao/cap07_vulcao.md`;
aqui ficam as falas do Kai. Regras da luta: `docs/BOSSES.md`, secção 14.

- **Antes** — **Kai** *(zangado, olhos azuis)*: "Não me sigas mais. O Sistema prometeu: quem chegar primeiro ao topo vai para casa. E vou ser eu."
- **Durante** — a cada 25% de vida dele há uma escolha. ✔ = resposta certa.

| Vida dele | Kai diz | Escolhas |
|---|---|---|
| 75% | *(zangado)* "Sai da frente, número redondo! Tu tens tempo! Eu não!" | ✔ ▶ **"Lembras-te do lobo? Salvaste-me."** → "…Isso foi antes. Antes de saber que só um chega primeiro." · ▶ **"Então luta a sério!"** → "É o que estou a fazer!" · ▶ **"Eu também quero voltar."** → "Então somos dois para a mesma porta!" |
| 50% | *(zangado)* "A Yui está a crescer sem mim! Tu não percebes!" | ✔ ▶ **"A Yui não ia querer isto."** → "Cala-te! Tu não a conheces! …Ela ia ter medo de mim agora, não ia?" · ▶ **"Esquece a Yui."** → "NUNCA!" · ▶ **"Desculpa, Kai."** → "Não peças desculpa! Luta!" |
| 25% | *(triste, a chorar)* "Porque é que não caís?! Porque é que não me deixas ir?!" | ✔ ▶ **"Prometemos chegar os dois."** (precisa de `kai_promessa_1` ou `kai_promessa_2`) → "…Os dois." · ✔ ▶ **"Disseste: bate-me até voltares."** (precisa de `kai_luar`) → "…Eu disse isso. Ao luar. Fui eu." · ▶ **"Isto não és tu."** → "Então quem é?!" |

- **Para salvar**: **6+ ❤️** com o Kai e as **3 respostas certas**. Com menos de 6 ❤️, as respostas certas não chegam:
  **Kai** *(zangado)*: "Palavras! Só palavras!" e a luta continua até ao fim.
- **Salvar** — 🎬 o Kai para a meio de um golpe. A espada treme. As janelas azuis à volta dele racham.
  - `[Sistema] Erro. Jogador nº 9 999: ligação perdida.`
  - **Kai** *(triste, a chorar)*: "Eu ia deixar-te para trás. Por uma porta que nem sei se existe."
  - **Kai** *(triste)*: "Desculpa. Desculpa, desculpa."
  - ▶ **"Voltamos os dois."** / ▶ **"Anda. Vamos para Ascendia."** → **Kai** *(feliz, a chorar)*: "…Pois. Os dois."
  - ⚙ flag `kai_salvo` · **Amuleto da Amizade** · o Kai passa a **companheiro** · conta para o final secreto.
- **Vencer** — 🎬 o Kai cai de joelhos. A armadura escura desfaz-se em pixels azuis.
  - **Kai** *(triste)*: "Perdi. Claro. Ganhas sempre, número redondo."
  - **Kai** *(triste)*: "Diz à Yui… não. Não lhe podes dizer nada. Ela não te conhece."
  - `[Sistema] Jogador nº 9 999: retirado do registo.` 🎬 Luz azul. Fica só a espada dele no chão.
  - ⚙ flag `kai_vencido` · **Lâmina do Kai** · o Kai só volta no andar 100.

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_estado_vida` | `vida_pct < 30` | zangado | "Estás a cair aos bocados. Vai à Igreja. Não, não te levo ao colo. …Se desmaiares, levo." |
| `kai_estado_maldito` | `estado(amaldicoado)` | normal | "Tens uma nuvem roxa na cabeça. Fica-te mal. Vai à Irmã Célia antes que pegue." |
| `kai_estado_cansado` | `estado(cansado)` | normal | "Tens cara de zombie. Vai dormir. Rival cansado não conta." |
| `kai_estado_molhado` | `estado(encharcado)` | feliz | "Estás a pingar. Squish, squish. Agora sabes como vivem os meus ténis." |
| `kai_estado_sapo` | `estado(sapo)` | feliz | "Um sapo. És um SAPO. Ha! Pena o telemóvel não ter bateria. Isto era para a história." |
| `kai_arma_nova` | arma Épica ou melhor equipada pela 1.ª vez | feliz | "Que espada é essa? Duelo. Agora. Quero ver se corta tanto como brilha." |
| `kai_animal` | `animal != nenhum` (1.ª vez) | surpresa | "Tens um bicho? …Posso fazer-lhe festas? Não digas a ninguém que perguntei." |
| `kai_comp_mia` | `companheiro(mia)` | feliz | "Mia! Guarda alta. Mais alta. Isso. Já sabes a outra metade do corte? Não fui eu." |
| `kai_comp_gorvan` | `companheiro(gorvan)` | surpresa | "O Mestre Gorvan vai subir?! Posso ir também? Não respondas. Já vou." |
| `kai_comp_nina` | `companheiro(nina)` | triste | "Nove mil. Desististe e voltaste a subir. Eu… sei como é. Mais ou menos." |
| `kai_classe` | 1.ª conversa depois de escolher classe | normal | "{classe}? Hm. Eu tinha escolhido igual. Ou melhor. Igual." |
| `kai_nivel_10` | `nivel >= 10` (1.ª vez) | feliz | "Nível 10. Vai ao Gorvan escolher classe. Eu sou Espadachim. Escolhe outra. Para não seres cópia." |

### Encontros na torre (fase A)

Até ao andar 50, ao entrar numa Zona Segura há **5%** de hipótese de o Kai lá estar.

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `kai_torre_1` | na Zona Segura | feliz | "Fogueira, cristal, um rival. Já tenho tudo o que preciso." |
| `kai_torre_2` | luta ao teu lado | normal | "Não é por ti. Este lobo olhou para mim de lado." |
| `kai_torre_3` | `vida_pct < 50` | normal | "Toma. Uma poção. Não te habitues." ⚙ +1 Poção de Vida |

### Fase B — desaparecido (H_14 a H_16)

O Kai **não está em lado nenhum**: não há conversa, presentes, cenas, missões nem duelos. Quem cobre a falta dele:

| O que era do Kai | Quem cobre |
|---|---|
| duelos de treino | a **Arena** da Capitã Freya (a partir do rank D); o lugar do Kai no ranking fica com "???" |
| treino à noite na Praça | a **Mia** treina sozinha no sítio dele (fala dela: ver `mia.md`) |
| mesa da Taberna ao domingo | fica vazia; o Lucien canta-lhe uma canção sem nome |
| o nome dele | no **quadro dos desaparecidos** da Guilda (fala `lyra_dia_46`); o **Pip** guarda-lhe um isco (fala `pip_dia_50`) |

### Fase C — o Kai frio (H_16 a H_17)

Nas Zonas Seguras dos andares 61–67 há **30%** de hipótese de veres o Kai ao longe, sentado de costas. Ao falar, diz
**uma** destas falas e desaparece num flash azul. Não dá amizade.

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kai_frio_1` | — | zangado | "Não me sigas." |
| `kai_frio_2` | — | normal | "Vai para casa, número redondo. Para a tua. Eu vou para a minha." |
| `kai_frio_3` | — | zangado | "Os meus olhos estão ótimos. Estão azuis. E daí?" |
| `kai_frio_4` | — | triste | "O Sistema prometeu. Se eu chegar primeiro… Não me olhes assim." |
| `kai_frio_5` | `flag(kai_luar)` | triste | "…Lembras-te do luar? Não. Esquece. Esquece tudo." |

### Kai na equipa (fase D)

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `kai_equipa_1` | herói com `vida_pct < 30` | zangado | "Recua! Eu seguro isto. Não te armes em herói, esse papel é meu hoje." |
| `kai_equipa_2` | entrar na arena de um boss | normal | "Os dois. Como no javali. Quem tirar mais vida paga o jantar." |
| `kai_equipa_3` | chegar a uma Zona Segura | normal | "Senta-te. Eu fico de vigia. Não durmo. Não durmo desde o 68." |

### Serviço — duelo de treino

1 duelo por dia, a partir de H_04. Luta até alguém chegar a **30% de vida** (ninguém se magoa a sério). Dá XP da skill
da arma usada, como a Arena. Nas fases B, C e E não há serviço.

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `kai_servico_abrir` | escolher **Duelo de treino** | feliz | "Duelo? Bora. Até alguém chegar aos 30%. Quem perder paga o jantar. A brincar. Mais ou menos." |
| `kai_servico_cedo` | antes de H_04 | normal | "Primeiro chega ao andar 5. Não bato em principiantes. Bato, mas não conta." |
| `kai_servico_vida` | `vida_pct < 50` | zangado | "Com essa vida? Não. Vai curar-te. Não luto com quem já está a cair." |
| `kai_servico_ganhar` | o herói ganha | zangado | "…Tsc. Sorte. Amanhã outra vez. E amanhã ganho eu." |
| `kai_servico_perder` | o Kai ganha | feliz | "HA! Mais devagar do que um slime. Levanta-te. Não, fica aí. Gosto da vista." |
| `kai_servico_repetido` | já duelaram hoje | normal | "Já levaste a tua dose hoje. Volta amanhã." |
