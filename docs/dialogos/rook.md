# Rook — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.11. Dados: `dados/dialogos/rook.json`. Mercado negro: `docs/LOJAS.md`, secção 2.15.
**Escolhas que contam**: N_ROOK_1 (abrir o embrulho ou não) e N_ROOK_3 (falar com a Freya ou ajudá-lo a fugir) mudam a
amizade com o Rook e com a Freya e decidem o **epílogo** dele (`docs/HISTORIA.md`, secção 7).

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios e baixos, arrastados, como quem fala ao canto da boca |
| Como fala | sarcástico, responde a perguntas com perguntas, nunca diz uma coisa boa sobre si próprio; quando fala das crianças do bairro, a voz muda |
| Repete | "Eu? Roubar?", "Não contes à Freya.", "Sem perguntas.", "Pago bem. Às vezes." |
| Tiques | atira uma faca pequena ao ar e apanha-a (animação `faca_ar`); afasta o cabelo do olho quando está a falar a sério |
| Nunca diz | "obrigado" (diz "estamos quites"); que ajuda o bairro |
| Chama ao herói | "Dez Mil" ou "herói", em tom de gozo; `{nome}` só a partir dos 6 corações |
| Quem é | **Torrense**: nasceu em **Zahra** (andar 32), dentro da torre. Aos 8 anos desceu 32 andares sozinho, a fugir de uma coisa que não conta. Cresceu no Bairro Baixo a roubar para comer |
| Rotina | dorme de dia (8:00–15:00, ninguém sabe onde) · Bairro Baixo à tarde · **telhados à noite** (22:00–4:00, mercado negro). Ao Domingo à tarde joga à bola com as crianças do bairro (finge que é para as "treinar a fugir") |

---

## 2. Primeira conversa

Só depois do **rank D** o Rook fala contigo a sério; antes disso, se o encontrares no Bairro Baixo, foge pelos telhados ("Não falo com principiantes. Dá azar.").
A 1.ª conversa (telhados, à noite, rank D+):

- 🎬 O Rook está sentado na beira de um telhado. Não se vira.
- **Rook** *(normal)*: "Dez Mil. Sobes muito para quem vem de baixo. Sentes-te importante? Não te sintas. A torre adora gente que se sente importante."
- **Rook** *(feliz)*: "Sou o Rook. Vendo coisas. Sei coisas. Às vezes vendo as coisas que sei."
- **Rook** *(normal)*: "Quando fores rank C, volta. Aí abro a loja. Antes disso, és só mais um que não sabe guardar segredos."

⚙ Com rank C abre o **Mercado Negro**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `rook_dia_01` | `hora entre 15 e 19` | normal | *(Bairro Baixo)* "De dia não trabalho. Trabalhar de dia é para gente honesta. E cansada." |
| `rook_dia_02` | `hora entre 22 e 4` | feliz | "Bem-vind{o/a} aos telhados. A melhor vista da cidade. E ninguém sobe cá a cobrar impostos." |
| `rook_dia_03` | — | normal | "Eu? Roubar? Só peço emprestado para sempre." |
| `rook_dia_04` | — | normal | "Não contes à Freya que me viste. Nem que não me viste. Não contes nada à Freya." |
| `rook_dia_05` | — | feliz | "O Tobias tem um cofre atrás do quadro do bigode. Não roubo. Só gosto de saber onde estão as coisas." |
| `rook_dia_06` | — | normal | "A torre é o maior ladrão de todos. Rouba mundos. E toda a gente lhe chama 'maravilha'. Eu roubo um pão e chamam-me 'Rook'." |
| `rook_dia_07` | — | normal | "O Governador tem goteiras na Câmara. Deixei-lhe um bilhete. É o meu serviço público." |
| `rook_dia_08` | — | feliz | "A Mia quer ser aventureira. Ensinei-lhe a cair sem se magoar. A Célia ensinou-a a rezar. Veremos qual serve mais." |
| `rook_dia_09` | `dia_semana == domingo && hora entre 14 e 18` | feliz | *(no largo, com crianças)* "Não estou a jogar. Estou a treiná-los a fugir com uma bola. É muito diferente." |
| `rook_dia_10` | `clima == chuva && hora entre 22 e 4` | zangado | "Telhados molhados. Escorregam. Se eu cair, diz que foi de propósito. Para impressionar." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `rook_dia_20` | `estacao == inverno` | triste | "No inverno o bairro passa frio. A lenha do Bruno é cara. Às vezes aparece lenha à porta das casas. Mistério." |
| `rook_dia_21` | `estacao == verao` | feliz | "No verão dorme-se nos telhados. É o único hotel de luxo do Bairro Baixo." |
| `rook_dia_22` | `estacao == outono` | normal | "Outono: os ricos compram casacos novos e deitam fora os velhos. O bairro veste-se bem no outono." |
| `rook_dia_23` | `clima == nevoeiro` | feliz | "Nevoeiro. O meu tempo preferido. Ninguém vê ninguém. Toda a gente é inocente." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `rook_dia_40` | `andar_maximo >= 21` | normal | "No pântano há um macaco que rouba ouro. Um colega. Mas um colega ganancioso. Tenho um trabalho para ti." |
| `rook_dia_41` | `andar_maximo >= 32` | triste | "Foste a Zahra. …Não, não me perguntes. Disse que não falava disso. Ainda não." |
| `rook_dia_42` | `missao(H_08) == concluida && flag(sssar_defendida)` | feliz | "Desobedeceste à Guilda pelos lagartos. Gosto de ti, Dez Mil. Não digas a ninguém que disse isto." |
| `rook_dia_43` | `missao(H_08) == concluida && flag(sssar_expulsa)` | normal | "Fizeste o que a Guilda mandou. Toda a gente faz. Eu também fazia, se a Guilda me pagasse." |
| `rook_dia_44` | `missao(H_14) == concluida && missao(H_16) != concluida` | triste | "O rapaz do casaco azul. Vi-o a subir no último dia. Não olhou para trás. Quem não olha para trás está a fugir de alguma coisa." |
| `rook_dia_45` | `andar_maximo >= 97` | normal | "Há uma cidade lá em cima para quem desistiu. Imagino que tenha bons telhados. Os desistentes nunca olham para cima." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `rook_dia_60` | `coracoes(rook) >= 2` | normal | "Guardei-te uma coisa boa no mercado. Não por simpatia. Por negócio. A simpatia não paga." |
| `rook_dia_61` | `coracoes(rook) >= 4` | feliz | "Já me viste a dar pão às crianças. Se contares a alguém, digo que és tu que dás. Ninguém acredita." |
| `rook_dia_62` | `coracoes(rook) >= 6` | normal | "{nome}. Pronto. Disse o teu nome. Não faças essa cara." |
| `rook_dia_63` | `coracoes(rook) >= 8` | triste | "Às vezes penso em subir outra vez. Até Zahra. Só para ver se ainda lá está alguém. Depois não vou." |
| `rook_dia_64` | `coracoes(rook) >= 10` | feliz | "Estamos quites, Dez Mil. Para sempre. É o maior elogio que eu sei dar." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `rook_dia_70` | `origem == atrasado` | feliz | "Sabes correr. Corres como quem foge do autocarro. Eu corro como quem foge da Guarda. Somos da mesma escola." |
| `rook_dia_71` | `origem == ajudante` | normal | "Ajudavas pessoas no teu mundo. Aqui ajudas pessoas. Não te cansas? …Pergunto por um amigo." |
| `rook_dia_72` | `skill_unica == mao_de_midas` | feliz | "Mão de Midas! Já pensaste em mudar de profissão? Tenho uma vaga. Paga bem. Em ouro, claro." |
| `rook_dia_73` | `skill_unica == passo_fantasma` | normal | "Esquivas duas vezes seguidas. Isso nos telhados é ouro. Fica longe dos telhados. São meus." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `rook_curta_1` | normal | "Ainda aqui? Os telhados não são praça pública." |
| `rook_curta_2` | feliz | "Se não compras, não falas. Regra da casa. A casa é o telhado." |
| `rook_curta_3` | normal | "Hmm? Estava a contar as janelas abertas. Por hobby." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Rook** *(normal)*: "Nasci lá dentro, Dez Mil. Os Torrenses acham que o céu de Zahra é o único céu. Eu achava. Depois desci e vi este."
- **Rook** *(triste)*: "O céu cá de baixo também não é verdadeiro. É só o teto da torre de fora. Ninguém aqui viu um céu verdadeiro. Só vocês, os da janela."
- **Rook** *(normal)*: "Por isso não me perguntes o que é a torre. Pergunta-me o que vale. Isso eu sei."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "Na floresta as fadas roubam. Respeito. Mas roubam mal: só itens pequenos." |
| 2 Cavernas | "Nas minas há goblins com um rei. Um rei de lata. Os reis de lata são os piores: precisam de provar que são de ouro." |
| 3 Pântano | "Há um macaco rei que rouba ouro aos exploradores. Quero o ouro. Para o bairro. Não, para mim. Para o bairro." |
| 4 Deserto | "Zahra é bonita. O bazar tem cinco lojas. Três vendem coisas roubadas. Adivinha quais." |
| 5 Gelo | "No gelo há gente congelada com bolsos cheios. Não, não te estou a sugerir nada. Estou só a informar." |
| 6 Oceano | "Piratas reformados! Os meus heróis de infância. Diz-lhes que o Rook manda cumprimentos. Não me conhecem. Mas diz." |
| 7 Vulcão | "Lá em cima os cultistas guardam ouro nos altares. Ouro de altar é o mais fácil de roubar. Ninguém fica a guardar um altar." |
| 8 Reino Assombrado | "Um mercado de fantasmas que aceita lágrimas como moeda. Finalmente uma moeda que eu tenho." |
| 9 Céu | "Os Alados não têm fechaduras. Não precisam: quem é que lá chega? Tu. Pois." |
| 10 Abismo | "Não há nada para roubar no fim do mundo. Só respostas. E essas não se vendem." |

### 4.3 Rumores (vendidos no mercado negro, ou dados de graça com 6+ ❤️)
| ID | Condição | Rumor |
|---|---|---|
| `rook_rumor_01` | — | "Há um baú de ouro escondido no moinho do andar 1. Puxa a corda. Toda a gente olha para as pás, ninguém puxa a corda." |
| `rook_rumor_02` | `andar_maximo >= 12` | "Os diários dos mineiros perdidos têm números. Junta-os. É o código de um cofre." |
| `rook_rumor_03` | `andar_maximo >= 21` | "O Barão Coaxim quer comprar o Ídolo de Jade. Paga 3 000. O Fausto paga em lágrimas de alegria. Escolhe a moeda." |
| `rook_rumor_04` | `andar_maximo >= 31` | "Os bandidos do deserto escondem mapas do tesouro nos bolsos. Três em cada cem. Faz as contas e bate em cem." |
| `rook_rumor_05` | `andar_maximo >= 52` | "No Porto Arquipélago há um ex-pirata que vende mapas falsos. Os falsos levam a sítios verdadeiros. Os verdadeiros não." |
| `rook_rumor_06` | — | "A Freya sabe onde eu durmo. Sabe há anos. Nunca lá foi. Pensa nisso." |

### 4.4 A vida dele
| Corações | Fala |
|---|---|
| 0 | "A minha vida? Não está à venda." |
| 2 | "Cresci no Bairro Baixo. Comia o que caía das bancas. Às vezes as coisas caíam porque eu as empurrava." |
| 4 | "Não sou daqui. Nasci lá dentro. Num oásis com nome bonito. Não te digo qual. Ainda." |
| 6 | "Zahra. Andar 32. Os Torrenses nunca saem. Eu saí. Com oito anos e uns sapatos roubados." |
| 8 | ver a **cena de 8 ❤️** |
| 10 | "Agora sabes tudo. Ninguém sabe tudo. Nem a Freya. Sobretudo a Freya." |

---

## 5. Presentes

**Adora:** segredos (Mapa do Tesouro), Pérola Negra, Coroa de Casca · **Gosta:** itens roubados (os que tiram as fadas e os macacos, e os do "item roubado do dia"), doces ·
**Detesta:** a Guarda (qualquer item da Freya ou do Quartel), flores.

| Reação | Falas |
|---|---|
| Adora | "Um mapa do tesouro? Para mim? Estás a tentar comprar-me. Está a resultar." · "Pérola negra. Bonita. Escura. Como o meu futuro. Obrigado. Estamos quites. Não, não estamos. Estou a dever-te." |
| Gosta | "Doces! Para as crianças. Não, para mim. Para as crianças." |
| Neutro | "Hmm. Isto vende-se. Obrigado." |
| Não gosta | "Que é que eu faço com isto? Não respondas." |
| Detesta | "Flores? A sério? Pareço um vaso?" · "Isto tem o selo da Guarda. Tira isso de ao pé de mim. Já." |

| Item | Fala |
|---|---|
| Coroa de Casca (R3_12) | "A coroa do Rei Bobo. Vou usá-la nos telhados. O Rei dos Telhados. Soa bem. Soa a problemas." |
| Areia de Zahra (decoração do andar 32) | 🎬 fica calado muito tempo. "…Cheira igual. Não sabia que me lembrava do cheiro." ⚙ +80 (conta como adora) |

---

## 6. Aniversário e festivais

**Aniversário (Outono, dia 21):**
- Sem presente: "Não faço anos. Os ladrões não fazem anos. Desaparecem um dia e aparecem mais velhos."
- Com presente que adora: "Como é que sabes o dia? Ninguém sabe o dia. …A Mia. Claro. A Mia sabe tudo e conta tudo."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Festa das flores. Detesto flores. Venho pelo bolo. E pelos bolsos distraídos. É mentira. Venho pelo bolo." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Dançar? Em público? À frente da Freya? …Uma. E se eu pisar, pisei de propósito." ⚙ +100 |
| F_02 Festival da Pesca | "Aposto contra o Pip todos os anos. Ele é o juiz. Perco sempre. Tenho de investigar." |
| F_03 Noite dos Espíritos | "Esta noite visto-me de fantasma e as crianças do bairro dão-me doces. Inverto o sistema. Sou um génio." |
| F_04 Festival da Estrela | "Amigo secreto. Calhou-me a Freya. Dou-lhe uma coisa que lhe roubei há cinco anos. Ela vai ficar furiosa. E contente." |
| F_05 Dia da Subida | "Comida grátis na praça! A melhor festa. Ninguém olha para os bolsos. Brincadeira. Estou a comer. Só a comer." |
| F_06 Concurso da Casa | "Vou visitar as casas todas. Para ver a decoração. Só para ver. Com os olhos." |
| F_07 Noite das Lanternas | "Não ponho lanterna. Os meus não subiram: ficaram lá em cima, em Zahra. Ponho uma vela no telhado. Para eles verem, se olharem para baixo." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Um rei derrubado. Gosto de reis derrubados. São todos iguais de perto." |
| Ent Ancião (10) | "A cidade fez festa. Eu fiz festa no telhado. Vista melhor e sem discursos." |
| Aranha-Mãe (15) | "Aranhas. Ainda bem que não fui eu. Eu subo paredes, mas não com oito patas." |
| Golem de Cristal (20) | "Uma casa, hein? Que fechadura tem? Pergunto por segurança. A tua." |
| Serpente do Lodo (25) | "Cheiras a lodo. Cheiras a dinheiro também? O lodo do pântano tem moedas antigas." |
| Hidra do Pântano (30) | "Corta uma cabeça, nascem duas. É como os impostos do Governador." |
| Escorpião Imperador (35) | "Estiveste perto de Zahra. Viste… não. Não perguntes. Eu também não pergunto." |
| Faraó Eterno (40) | "Um Jogador que ficou rei e acabou em pó. A torre trata bem os reis. Até à hora de os comer." |
| Yeti Ancião (45) | "O yeti guardava coisas dos mortos. Um colecionador. Um colega, quase." |
| Dragão de Gelo (50) | "Metade da torre. A cidade está bêbeda de festa. Bons bolsos esta noite. É piada. Quase." |
| Capitão Esqueleto (55) | "O capitão tinha ouro que não podia gastar. Eu tenho o contrário. Trocávamos bem." |
| Leviatã (60) | "O teu amigo continua desaparecido. Ponho-me a ver os telhados à noite. Nunca se sabe por onde se volta." |
| Ferreiro Infernal (65) | "O anão rabugento passou a noite na forja a martelar. Ouvia-se do bairro. Não me queixei. Era um som triste." |
| Kai — salvo (68) | "Trouxeste-o. Bem feito, Dez Mil. Há quem desça sozinho. Ainda bem que ele não teve de descer sozinho." |
| Kai — vencido (68) | "Sobe ao telhado. Vem. Daqui não se vê a torre por causa do fumo das chaminés. Às vezes é bom não a ver." |
| Titã de Magma (70) | "Os cultistas vão chorar. Os altares deles ficam sem guarda. Isto não é uma sugestão." |
| Lich Bibliotecário (75) | "Um morto a guardar livros. O Fausto vai querer ir lá viver." |
| Rei Sem Coroa (80) | "Um rei que pediu desculpa. Pela primeira vez gosto de um rei." |
| Grifo Real (85) | "Penas de grifo vendem-se a peso de ouro. Não, guarda-as. São tuas. Estou a ficar mole." |
| Serafim Caído (90) | "Vens com cara de quem soube quem manda. Não me digas. Eu sempre soube que alguém mandava. Só não sabia que estava cansado." |
| Guardião do Tempo (95) | "Cinco andares. Se não voltares, fico com as tuas coisas. …Volta. Não quero as tuas coisas." |

---

## 8. Cenas de coração

### ❤️ 2 — O pão do bairro

| | |
|---|---|
| ID | `cena_rook_2` |
| Quando | 2 ❤️ · entrar no Bairro Baixo entre as 5:00 e as 6:00 |
| Onde | beco do Bairro Baixo |
| Quem | herói, Rook, 4 crianças |
| Música | sem música; só o vento |

🎬 Madrugada. O Rook passa pelas portas das casas pobres e deixa um pão à frente de cada uma. Quatro crianças seguem-no em fila, em silêncio, a ajudar.
🎬 Uma criança vê o herói e puxa a manga do Rook. Ele vira-se. Fica parado com um pão na mão.

- **Rook** *(zangado)*: "Não viste nada."
- **Rook** *(normal)*: "Os pães caíram de uma carroça. Uma carroça desastrada. Toda a semana. À mesma hora."

▶ **"Não vi nada."**
▶ **"Posso ajudar?"**

- *(não vi)* **Rook** *(feliz)*: "Bem. Estamos quites. Por hoje." ⚙ +30
- *(ajudar)* **Rook** *(surpresa)*: "…Leva a cesta. As casas com a porta azul. Não batas. Pousa e vai." ⚙ +30 · o herói entrega 5 pães (minijogo curto de silêncio: não correr)

⚙ 5% de desconto no mercado negro.

### ❤️ 4 — A corrida pelos telhados

| | |
|---|---|
| ID | `cena_rook_4` |
| Quando | 4 ❤️ · telhados, à noite (22:00–2:00) |
| Onde | telhados de Ascendia, do Bairro Baixo à Praça |
| Quem | herói, Rook |
| Música | `taberna` (versão rápida) |

- **Rook** *(feliz)*: "Sabes correr nos telhados? Não sabes. Vamos ver. Até à torre do relógio da Câmara. Quem perder paga o pequeno-almoço."
- 🎬 **Minijogo**: corrida pelos telhados (saltos entre casas, passar por cima de chaminés, não cair à rua). 90 s.
- *(ganhar)* **Rook** *(surpresa)*: "Ganhaste. Ganhaste?! Fiz batota e ganhaste na mesma. Isto não volta a acontecer." ⚙ +30
- *(perder)* **Rook** *(feliz)*: "Pagas o pequeno-almoço. Pão com queijo da Dona Marta. Dois. Um é para a Mia."
- 🎬 Os dois sentam-se no telhado da Câmara. A cidade inteira por baixo.
- **Rook** *(normal)*: "Daqui vejo tudo. Quem entra, quem sai, quem chora à janela. É o meu bairro inteiro. A cidade toda é o meu bairro."

⚙ Recebe a receita **Pão com Queijo à Rook** (cura pouco, +10% velocidade 5 min) e desbloqueia o **atalho dos telhados** (um caminho rápido entre o Bairro Baixo e a Praça).

### ❤️ 6 — O Rei Bobo

| | |
|---|---|
| ID | `cena_rook_6` |
| Quando | 6 ❤️ · `andar_maximo >= 21` · telhados à noite |
| Onde | telhados |
| Quem | herói, Rook |
| Música | `ascendia_noite` |

- **Rook** *(normal)*: "Tenho um trabalho. Honesto. Quase. No pântano há um macaco que se acha rei. Rouba ouro aos exploradores e senta-se em cima."
- **Rook** *(normal)*: "Tu tiras-lhe o ouro. Metade é tua. Metade é para… uma coisa. Não perguntes."
- **Rook** *(triste)*: "Pronto. É para o bairro. Este inverno vai ser frio. Satisfeit{o/a}?"

⚙ Missão **R3_12 O Rei Bobo** (secção 9). O Rook aceita jantar em tua casa (entra pela janela).

### ❤️ 8 — Como desceu

| | |
|---|---|
| ID | `cena_rook_8` |
| Quando | 8 ❤️ · noite de nevoeiro, telhados |
| Onde | telhado mais alto do Bairro Baixo, de frente para a torre |
| Quem | herói, Rook |
| Música | `bazar_zahra` (versão lenta, só uma flauta) |

🎬 O Rook está sentado com os joelhos encostados ao peito. Tira o capuz. Afasta o cabelo do olho: tem uma cicatriz pequena por baixo, em forma de estrela.

- **Rook** *(triste)*: "Em Zahra, quando uma criança nasce com esta marca, dizem que vai ser 'da torre'. Que um dia a torre a chama. Que fica a servi-la."
- **Rook** *(triste)*: "A minha mãe não queria isso para mim. Quando fiz oito anos, deu-me uns sapatos, pão para dez dias e disse: 'Desce. Desce sempre. Não pares.'"
- **Rook** *(normal)*: "Desci trinta e dois andares. Sozinho. Aprendi a roubar no andar 20 e a esconder-me no 11. Cheguei cá em baixo com os sapatos rotos."
- **Rook** *(triste)*: "Nunca voltei. Não sei se ela ainda está viva. Tenho medo de saber."

▶ **"Vou procurá-la em Zahra."**
▶ **"Ela queria que fosses livre. És."**

- *(procurar)* **Rook** *(zangado, depois triste)*: "Não! …Não. Ainda não. Se algum dia eu pedir, então sim. Não antes." ⚙ +30 · flag `rook_mae_zahra`
- *(livre)* **Rook** *(feliz, raro)*: "Livre. A roubar pão num bairro pobre. …Sim. Sou. É a melhor coisa que tenho." ⚙ +30

⚙ 15% de desconto no mercado negro. Passa a mandar **cartas** (sem remetente; com doces ou uma informação de um segredo).
⚙ Com a flag `rook_mae_zahra`, aparece em Zahra (andar 32) uma velha Torrense chamada **Samira** que pergunta por "um rapaz com uma estrela no olho". Contar-lhe é opcional (dá uma fala especial ao Rook e muda o epílogo dele: ver secção 9, N_ROOK_3).

### ❤️ 10 — A Gazua Mestra

| | |
|---|---|
| ID | `cena_rook_10` |
| Quando | 10 ❤️ · `missao(N_ROOK_3) == concluida` · telhados à noite |
| Onde | telhado da Câmara |
| Quem | herói, Rook (e, se o ajudaste a ser solto pela Freya, a Freya ao longe a fingir que não vê) |
| Música | `tema_rook` (guitarra espanhola, assobio) |

🎬 O Rook atira uma coisa pequena ao herói. É uma gazua de prata, fina, gasta de tanto uso.

- **Rook** *(normal)*: "É a minha gazua. A primeira. Fi-la no andar 20 com o arame de uma vagoneta. Abriu todas as portas que me interessaram."
- **Rook** *(feliz)*: "Agora tu precisas mais dela do que eu. Eu só abro portas cá em baixo. Tu vais abrir as de cima."
- **Rook** *(triste)*: "E quando chegares à última porta… abre-a. Mesmo que te digam para não abrir. Alguém tem de abrir."

▶ **"Estamos quites."**
▶ **"Obrigad{o/a}, Rook."**

- *(quites)* **Rook** *(feliz)*: "Não. Agora sou eu que te devo. Que horror."
- *(obrigado)* **Rook** *(surpresa)*: "…Ninguém me diz obrigado. Dizem 'apanhem-no'." 🎬 sorri. "Obrigado também. Pronto. Disse."

⚙ **Gazua Mestra**: abre 1 baú de ouro por dia sem chave. Título *Amig{o/a} dos Telhados*.

---

## 9. Missões

### N_ROOK_1 — Um Favor Pequeno (rank C)
- **Pedir** — **Rook** *(normal)*: "Leva este embrulho ao Tibério, na Zona Segura do andar 10. Sem perguntas. Sem espreitar. Pago bem."
- **Escolha** (durante a viagem, abrir o inventário mostra a opção **Abrir o embrulho**):
  - **Não abrir** → o Tibério recebe-o: "Do Rook? Remédios para o bairro, comprados mais baratos cá em cima. Não lhe digas que te disse." ⚙ Rook +100 · 300 ouro
  - **Abrir** → são **frascos de remédio** com um bilhete: *"Para a tosse do bairro. Não é roubado. Desta vez."* O Rook sabe (o embrulho estava atado com um nó especial): "Abriste. Claro que abriste. Pelo menos agora sabes. Não contes à Célia." ⚙ Rook +30 · 150 ouro

### R3_12 — O Rei Bobo (6 ❤️, `andar_maximo >= 21`)
- **Passos**: no pântano, encontrar o **Rei Macaco Bobo** (região 3, ver `docs/regioes/r03_pantano.md`), vencê-lo e recuperar o **ouro do Rei** (2 000) e a **Coroa de Casca**.
- **Escolha** ao entregar:
  - **Dar metade ao Rook** → **Rook** *(feliz)*: "Metade. Exatamente metade. Contaste? Contaste. És estranh{o/a}, Dez Mil. Obrigado. Estamos quites." ⚙ +200 (❤️❤️) · 1 000 ouro · no inverno seguinte, o Bairro Baixo tem lenha (fala dos aldeões)
  - **Ficar com tudo** → **Rook** *(normal)*: "Ficas com tudo. Justo. Foste tu que lutaste. Eu arranjo-me. Arranjo-me sempre." ⚙ −30 · 2 000 ouro

### N_ROOK_3 — A Prisão (8 ❤️)
- **Começa** — a Freya prende o Rook a sair da Câmara pela janela, com um saco de documentos. `[Sistema] O Rook foi preso.` Ele fica na **cela do Quartel**.
- **Na cela** — **Rook** *(normal)*: "Não roubei nada. Fui devolver as escrituras das casas do bairro que o antigo governador vendeu às escondidas. Ninguém acredita. A Freya não acredita."
- **Escolha**:
  - **A) Falar com a Freya** — levar-lhe as provas (as escrituras originais estão na Biblioteca: o Fausto tem cópias). **Freya** *(zangada, depois justa)*: "Ele tem razão. Detesto quando ele tem razão." 🎬 a Freya solta-o e o Aldric anula as vendas. ⚙ Rook +100 · Freya +100 · flag `rook_ajudado_lei` → **epílogo bom**: o Rook abre um orfanato no Bairro Baixo.
  - **B) Ajudá-lo a fugir** — à noite, distrair o guarda e abrir a cela (gazua emprestada ou chave roubada da mesa da Freya). 🎬 o Rook foge pelos telhados. ⚙ Rook +150 · **Freya −200** · flag `rook_fugiu` → o Rook passa a ser procurado: só aparece nos telhados à 1:00–3:00; **epílogo**: foge para a Cidade Errante (a não ser que, mais tarde, a escolha A ainda seja feita: levar as provas à Freya depois da fuga dá a versão "perdoado" e o epílogo bom).
- **Entregar** (qualquer escolha) — **Rook** *(normal)*: "Estamos quites. Não. Desta vez não estamos. Desta vez devo-te. Que coisa horrível."

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `rook_estado_vida` | `vida_pct < 30` | normal | "Estás a deixar um rasto de sangue até ao meu telhado. Isso é mau para o negócio. Vai à Célia." |
| `rook_estado_maldito` | `estado(amaldicoado)` | feliz | "Uma maldição! Se fosse contagiosa, vendia-a à Freya." |
| `rook_freya_perto` | a Freya está a menos de 20 m | surpresa | "Shh! É a Freya. Não estou aqui." 🎬 desaparece |
| `rook_roubado` | uma fada ou macaco roubou-te um item hoje | feliz | "Roubaram-te? A ti? Que vergonha. Para eles. Roubar a um herói não tem desafio nenhum." |
| `rook_comp_mia` | `companheiro(mia)` | normal | "Mia. Cuidado com ela, Dez Mil. Se ela voltar com um arranhão, roubo-te as botas. Todas." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `rook_serv_abrir` | abrir o mercado negro | normal | "Hoje há {n} coisas. Não perguntes de onde vêm. Vêm de algum lado." |
| `rook_serv_sem_rank` | rank abaixo de C | normal | "Rank C, Dez Mil. Antes disso, nem me vês." |
| `rook_serv_chave` | comprar Chave de Baú de Ouro | feliz | "Chave boa. Quase sempre. Sem devoluções." |
| `rook_serv_chave_falsa` | a chave era falsa (10%) | — | `[Sistema] A chave partiu-se na fechadura.` (no dia seguinte, o Rook: "Ah. Essa. Pois. Leva outra a metade do preço. Não digas a ninguém.") |
| `rook_serv_info` | comprar informação | normal | "No andar {andar}, {pista}. Esqueci-me do que disse. Tu também." |
| `rook_serv_duvidoso` | vender um item duvidoso | feliz | "Isto é duvidoso. Gosto de coisas duvidosas. Pago mais." |
| `rook_serv_sem_ouro` | sem ouro | normal | "Sem ouro, sem negócio. Mas posso fiar. A juros de ladrão." |
| `rook_serv_fechado` | de dia | — | `[Sistema] Não há ninguém nos telhados. Só uma faca espetada numa chaminé, com um papel: "Volta à noite."` |
