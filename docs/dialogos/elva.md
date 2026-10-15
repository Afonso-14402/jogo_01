# Elva — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.19. Dados: `dados/dialogos/elva.json`. Costura: `docs/LOJAS.md`, secção 2.9.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios, precisos, sem pressa; um "tic" de tesoura de vez em quando |
| Como fala | elegante, frases bem acabadas, honestidade sem filtro sobre roupa; ri-se pouco e baixinho |
| Repete | "A elegância também é uma arma.", "Isso é armadura ou um saco de batatas?", "Fica quiet{o/a}." |
| Tiques | mede tudo com a fita métrica (animação `medir`), até pessoas a passar; tem alfinetes na boca quando trabalha |
| Nunca diz | que uma roupa feia é bonita (nem por educação); o nome da rainha antes dos 8 corações |
| Chama ao herói | "cliente" ao início; "manequim" a partir dos 2 corações (carinhoso); `{nome}` a partir dos 6 |
| Quem é | 32 anos. Foi costureira da rainha **Isolda** no **Reino de Alvorada**, um reino pequeno de tecelões que a torre engoliu há 12 anos. Ela estava fora do palácio a comprar tecidos e ficou do lado de cá. Nunca soube onde o reino foi parar dentro da torre |
| Rotina | Costura 9:00–19:00 · Mercado de tecidos (sábado de manhã) · **uma vez por estação** vai à Cidade Errante comprar tecidos (2 dias fora; a Costura fica fechada com um bilhete bordado) |

---

## 2. Primeira conversa

- 🎬 A Elva olha o herói de cima a baixo. Tira a fita métrica do pescoço.
- **Elva** *(normal)*: "Isso que trazes vestido… é armadura ou um saco de batatas?"
- **Elva** *(normal)*: "Não respondas. Era retórico. É um saco de batatas."
- **Elva** *(feliz, um bocadinho)*: "Sou a Elva. Faço armaduras de tecido, mochilas e roupa para quem quer subir com dignidade. A elegância também é uma arma."
- **Elva** *(normal)*: "Volta quando quiseres mudar de cor. Ou de vida. Começa-se sempre pela cor."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Costura (loja) · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `elva_dia_01` | `hora entre 9 e 11` | normal | "Bom dia. Já cortei três capas e um mal-entendido. A capa ficou melhor." |
| `elva_dia_02` | `hora entre 13 e 15` | normal | "Hora de almoço. Como em pé, ao balcão. Sentar amarrota o vestido." |
| `elva_dia_03` | `hora entre 17 e 19` | feliz | "Fim do dia. A melhor luz para ver as cores verdadeiras. As cores mentem de manhã." |
| `elva_dia_04` | — | normal | "A elegância também é uma arma." |
| `elva_dia_05` | — | normal | "O Brom veio pedir um avental novo. Disse-lhe que o velho tem cento e vinte anos e uma alma. Ele disse 'exato'. Fiz-lhe um igual." |
| `elva_dia_06` | — | feliz | "O Lucien quer um fato para o concerto. Com penas. Muitas penas. Estou a tentar convencê-lo a ter só algumas penas." |
| `elva_dia_07` | — | normal | "A Freya usa a mesma armadura há oito anos. Brilha. Mas a capa está um horror. Não lho digo. Tenho amor à vida." |
| `elva_dia_08` | — | normal | "Uma costura direita é um pequeno milagre. Faço vinte por dia." |
| `elva_dia_09` | `dia_semana == sabado && hora entre 8 e 12` | feliz | *(no Mercado de tecidos)* "Sábado de tecidos. Toco em tudo. Compro pouco. Os comerciantes odeiam-me e respeitam-me." |
| `elva_fora` | dias em que está na Cidade Errante | — | *(bilhete bordado na porta)* `"Fui buscar tecidos à Cidade Errante. Volto em dois dias. Não entrem na loja com lama. — E."` |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `elva_dia_20` | `estacao == primavera` | feliz | "Primavera: linho e cores claras. Tudo o que é pesado vai para o baú." |
| `elva_dia_21` | `estacao == verao` | normal | "Verão: as armaduras de couro cheiram mal. Não é opinião. É ciência." |
| `elva_dia_22` | `estacao == outono` | feliz | "Outono: lã, cor de vinho, cor de folha. A minha estação." |
| `elva_dia_23` | `estacao == inverno` | normal | "Inverno: toda a gente quer casacos. Ninguém quer casacos bonitos. Eu faço-os bonitos na mesma." |
| `elva_dia_24` | `clima == chuva` | zangado | "Chuva. Não entres molhad{o/a}. A seda tem memória e nunca perdoa." |
| `elva_dia_25` | `clima == nevoeiro` | normal | "Nevoeiro. As cores ficam todas cinzentas. Odeio. Fico a costurar à luz da vela." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `elva_dia_40` | `andar_maximo >= 15` | feliz | "Seda de aranha! Do ninho do 15! Traz-me. É o tecido mais forte e mais leve do mundo. As aranhas são as melhores costureiras." |
| `elva_dia_41` | `andar_maximo >= 25` | normal | "Já posso fazer-te vestes de aprendiz. Se usas cajado. Se usas martelo, faço-te outra coisa. Com menos dignidade." |
| `elva_dia_42` | `andar_maximo >= 30` | feliz | "Mochila de Viajante pronta. Cinquenta espaços. Costuras duplas. Aguenta um javali. Não testei. Mas aguenta." |
| `elva_dia_43` | `andar_maximo >= 71` | triste | "Um reino engolido com rei e tudo, lá em cima… Não é o meu. O meu era mais pequeno. Mas vou perguntar-te uma coisa um dia." |
| `elva_dia_44` | `andar_maximo >= 72` | feliz | "Ectoplasma! Dos fantasmas! Dá um fio que brilha no escuro. Fio Espectral. Imagina uma capa feita de luz de fantasma." |
| `elva_dia_45` | `andar_maximo >= 91` | normal | "Fio de luz estelar. Se trouxeres, faço-te a melhor coisa que alguma vez fiz. Já tenho o desenho. Há doze anos." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `elva_dia_60` | `coracoes(elva) >= 2` | feliz | "Manequim! Fica aí. Não te mexas. Estou a imaginar-te de azul." |
| `elva_dia_61` | `coracoes(elva) >= 4` | normal | "Já sei as tuas medidas de cor. Se cresceres, vou saber. Se emagreceres, a Dona Marta vai saber primeiro." |
| `elva_dia_62` | `coracoes(elva) >= 6` | feliz | "{nome}. Tens bom gosto agora. Não tinhas. Eu ensinei. Estou orgulhosa." |
| `elva_dia_63` | `coracoes(elva) >= 8` | triste | "Às vezes cozo um ponto que a rainha me ensinou e paro. Fico com a agulha no ar. Depois continuo." |
| `elva_dia_64` | `coracoes(elva) >= 10` | feliz | "A capa fica-te bem. Fica-te mesmo bem. É a primeira vez que digo isto a alguém sem acrescentar 'mas'." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `elva_dia_70` | `origem == atrasado` | normal | "Chegaste com a camisa por dentro de um lado e por fora do outro. No teu mundo saías de casa sempre a correr, não era?" |
| `elva_dia_71` | `origem == dormir` | feliz | "Vieste para cá a dormir? De pijama? Diz-me que vieste de pijama. Tenho de ver o padrão." |
| `elva_dia_72` | `origem == jogador` | normal | "No teu mundo havia jogos onde se mudava a roupa da personagem? E toda a gente ficava igual? Que tragédia." |
| `elva_dia_73` | `skill_unica == bolsa_infinita` | surpresa | "Uma mochila infinita. Sem costuras. Sem forro. Isso não é magia: é um insulto à profissão." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `elva_curta_1` | normal | "Fica quiet{o/a}. Estou a medir uma coisa." |
| `elva_curta_2` | normal | "Já falámos. As agulhas não esperam." |
| `elva_curta_3` | feliz | "Essa cor fica-te bem hoje. Amanhã logo se vê." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Elva** *(normal)*: "A torre é uma colcha de retalhos. Cada andar é um pano de um mundo diferente. Cosidos à pressa. As costuras vêem-se."
- **Elva** *(triste)*: "Algures nessa colcha está o meu reino. Um retalho pequeno. Bordado a fio de ouro."
- **Elva** *(normal)*: "Não sei em que andar. Não quero saber. Ou quero muito. Depende do dia."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "Linho bravo! Fibras finas, cor de palha. Traz-me molhos. Faço-te uma capa leve." |
| 2 Cavernas | "Seda de aranha no ninho. Teias como cortinas. Não tenhas medo das aranhas: tem medo de não as aproveitar." |
| 3 Pântano | "Pele de crocodilo: dura, verde, impermeável. Para botas. Só para botas. Não me peças um casaco de crocodilo." |
| 4 Deserto | "Os tecidos do bazar de Zahra são os melhores da torre. Cores que não existem cá em baixo. Traz-me um laranja. Qualquer laranja." |
| 5 Gelo | "Lã de mamute. Pele de urso. Quente, pesada, feia. Eu faço-a bonita. É o meu talento." |
| 6 Oceano | "Seda de alga e escamas de sereia. Tecidos que brilham como água. Traz-me um retalho. Um pequeno. Pago o que quiseres." |
| 7 Vulcão | "Seda ignífuga dos bichos do fogo. Não arde. Uma capa que não arde! O sonho de qualquer costureira com velas." |
| 8 Reino Assombrado | "Ectoplasma para fio espectral. E… nada. Vai. Traz o ectoplasma. Não, espera. Viste algum estandarte com um sol a nascer? Não? Pronto." |
| 9 Céu | "Algodão-nuvem: o tecido mais leve que existe. Uma capa de nuvem. Cai como chuva. Imagina." |
| 10 Abismo | "Fio de luz estelar. Dizem que se tece com as mãos geladas. Eu tenho mãos geladas. Traz." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `elva_rumor_01` | — | "A Madame Plumas, da Cidade Errante, vende cores que eu não consigo fazer. Somos rivais. Ela ganha. Por agora." |
| `elva_rumor_02` | — | "O Rook rasga a capa todas as semanas nos telhados. Coso-a todas as semanas. Ele paga com doces. Roubados, espero eu que não." |
| `elva_rumor_03` | `andar_maximo >= 15` | "Há um casulo dourado no ninho das aranhas. Se nascer uma aranha de seda, ela tece em tua casa. Eu ia viver para tua casa." |
| `elva_rumor_04` | `andar_maximo >= 32` | "No bazar de Zahra há uma tecelã velha que faz tapetes voadores. Não voam. Mas são tão bonitos que parece que voam." |
| `elva_rumor_05` | `andar_maximo >= 57` | "A Rainha das sereias tem um vestido feito de pérolas cosidas. Mil e duzentas. Contei pelo desenho de um aventureiro." |
| `elva_rumor_06` | `andar_maximo >= 66` | "Há um ninho de fénix no vulcão. As penas de fénix… nem quero pensar. Não penso. Penso. Traz uma." |

### 4.4 A vida dela
| Corações | Fala |
|---|---|
| 0 | "Sou costureira. Coso. É isso." |
| 2 | "Aprendi a coser antes de aprender a ler. A minha mãe era costureira. A avó também. Todas as mulheres da família tinham calos no mesmo dedo." |
| 4 | "Trabalhei num palácio. Fazia os vestidos de uma rainha. Ela dizia que eu cosia 'como quem escreve uma carta'." |
| 6 | "O meu reino chamava-se Alvorada. Um reino pequeno de tecelões. O estandarte era um sol a nascer, bordado a ouro." |
| 8 | ver a **cena de 8 ❤️** |
| 10 | "Já não procuro o meu reino em todos os andares. Faço vestidos. Os vestidos levam um bocadinho de Alvorada para onde forem." |

---

## 5. Presentes

**Adora:** Seda de Aranha, Fio de Luz Estelar, Pena Arco-Íris · **Gosta:** tecidos (Linho Fino, Lã, Seda de Alga), penas ·
**Detesta:** roupa rasgada e coisas sujas (lixo de pesca, Gel de Slime, Lodo). **Especial:** se o teu equipamento for todo de raridade Comum, ela comenta (`elva_estado_comum`).

| Reação | Falas |
|---|---|
| Adora | "Seda de aranha. Pura. Sem nós. Vou fazer-te uma coisa com isto. Vou fazer-me uma coisa com isto. Vamos ver quem ganha." · "Uma pena arco-íris! As cores! Todas! Não sei se a uso ou se a emolduro." |
| Gosta | "Linho fino. Bom. Bom mesmo. Tens olho." |
| Neutro | "Obrigada. Vai para a caixa dos 'talvez'." |
| Não gosta | "Hmm. Isto é… uma escolha. Tua." |
| Detesta | "Isso está a pingar. Na minha loja. Em cima da seda. Sai. Com isso. Agora." |

| Item | Fala |
|---|---|
| Estandarte de Alvorada (ver N_ELVA_3, opcional) | 🎬 a Elva fica muito quieta. "…O sol a nascer. Fui eu que bordei estes raios. Este. E este." (conta como "adora" ×3) |

---

## 6. Aniversário e festivais

**Aniversário (Outono, dia 8):**
- Sem presente: "Faço anos. Fiz um vestido novo para mim. É o único presente que sei que vai servir."
- Com presente que adora: "Um presente… e do tecido certo. Escolheste bem. Isto é raro. Tu és rar{o/a}. Obrigada."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "O desfile de vestidos! Este ano vou mostrar o meu melhor. Se me ajudares, vai ser o melhor de sempre." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Só se trocares de casaco. …Brincadeira. Estás aceitável. Vamos." ⚙ +100 |
| F_02 Festival da Pesca | "Os pescadores vestem-se horrivelmente. É uma tradição. Respeito as tradições. De longe." |
| F_03 Noite dos Espíritos | "Faço as fantasias das crianças do bairro. De graça. Este ano a Mia quer ser 'um javali-rei com espada'. Estou a pensar." |
| F_04 Festival da Estrela | "Faço os laços dos presentes da cidade. Todos os anos. Uma noite inteira de laços. Odeio. Adoro." |
| F_05 Dia da Subida | "Fizeste-me ficar com um fato de gala parado no armário. Agora uso-o em todos os Dias da Subida. Não me faças parar." |
| F_06 Concurso da Casa | "Cortinas. É tudo o que olho. As cortinas dizem tudo de uma casa." |
| F_07 Noite das Lanternas | "Faço as lanternas de pano para quem não sabe dobrar papel. Uma é sempre minha: tem um sol bordado." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Couro de javali rei! Grosso, castanho. Para botas. Daquelas que duram uma vida." |
| Ent Ancião (10) | "Folhas douradas do coração da floresta. Prensadas e cosidas dão um bordado que não murcha. Trouxeste?" |
| Aranha-Mãe (15) | "A melhor costureira da torre morreu. Respeito. E… trouxeste a seda dela? Respeito com seda." |
| Golem de Cristal (20) | "Cristais do Golem. Botões! Os botões mais bonitos de Ascendia! A tua capa nova vai ter botões de golem." |
| Serpente do Lodo (25) | "Lodo. Nas botas. No chão. Sai." |
| Hidra do Pântano (30) | "Pele de hidra: escamas verdes que mudam com a luz. Uma capa de hidra… não. Sim. Talvez." |
| Escorpião Imperador (35) | "Carapaça de escorpião: dura demais para coser. Vou lixá-la. Botões outra vez." |
| Faraó Eterno (40) | "Ligaduras de faraó. Linho de mil anos. Perfeito. Assustador. Perfeito." |
| Yeti Ancião (45) | "Pelo de yeti. Branco. Quentíssimo. Um gorro. Vou fazer-te um gorro. Não discutas." |
| Dragão de Gelo (50) | "Escamas de dragão de gelo. Azuis. Brilham. Uma capa de dragão para a metade da torre. Merecida." |
| Capitão Esqueleto (55) | "O chapéu do capitão! É feio! É lindo de tão feio! Vou restaurá-lo." |
| Leviatã (60) | "Venceste o mar. A cidade está triste por causa do Kai. Fiz-lhe um casaco azul novo. Para quando voltar. Igual ao dele." |
| Ferreiro Infernal (65) | "Seda ignífuga dos bichos de fogo do Ferreiro. Uma capa que não arde! Já a estou a desenhar." |
| Kai — salvo (68) | "Dei-lhe o casaco azul novo. Ele disse que preferia o velho, rasgado. Depois vestiu o novo. Por cima do velho." |
| Kai — vencido (68) | "O casaco azul está no armário. Não o vendo. Não o desfaço. Fica." |
| Titã de Magma (70) | "Cinza vulcânica dá um cinzento que eu nunca consegui. Traz um saco. Tinta nova!" |
| Lich Bibliotecário (75) | "Capas de livros de mil anos. O Fausto deixou-me ver. Couro, ouro, bordados… Chorei. Discretamente." |
| Rei Sem Coroa (80) | "Viste os estandartes do reino? Algum tinha um sol? …Não. Pois. Era outro reino. Era sempre outro reino." |
| Grifo Real (85) | "Penas de grifo! Douradas! Uma pluma no chapéu! Um chapéu com pluma de grifo! Toda a cidade vai ter inveja!" |
| Serafim Caído (90) | "Penas de anjo… brancas. Não quero. Parecem tristes. Guarda-as tu." |
| Guardião do Tempo (95) | "Cinco andares. A tua roupa está em farrapos. Vem cá antes. Arranjo-a. Ninguém sobe ao topo em farrapos." |

---

## 8. Cenas de coração

### ❤️ 2 — As medidas à força

| | |
|---|---|
| ID | `cena_elva_2` |
| Quando | 2 ❤️ · entrar na Costura de manhã (9:00–12:00) |
| Onde | Costura |
| Quem | herói, Elva |
| Música | `ascendia_dia` (cravo) |

🎬 A Elva fecha a porta da loja à chave assim que o herói entra.
- **Elva** *(normal)*: "Fica quiet{o/a}. Braços abertos. Não, mais. Não respires."
- 🎬 **Minijogo curto**: ficar parado enquanto ela mede (não carregar em nada durante 5 s; se te mexeres, ela recomeça e suspira).
- **Elva** *(feliz)*: "Pronto. Agora sei as tuas medidas. Não as conto a ninguém. São um segredo profissional."
- **Elva** *(normal)*: "Porquê? Porque estava farta de te ver passar com um saco de batatas. Vou fazer-te uma coisa. Não precisas de pagar. Desta vez."

⚙ Recebe uma **roupa cosmética** à escolha (3 opções) e 5% de desconto na Costura.

### ❤️ 4 — O vestido da rainha

| | |
|---|---|
| ID | `cena_elva_4` |
| Quando | 4 ❤️ · entrar na Costura ao fim da tarde (17:00–19:00) |
| Onde | sala de trás da Costura |
| Quem | herói, Elva |
| Música | `revelacao` (suave, com harpa) |

🎬 Um manequim tapado com um pano. A Elva tira o pano devagar.
🎬 Um vestido inacabado, azul-escuro com um sol dourado bordado no peito. Faltam as mangas e a barra.
- **Elva** *(normal)*: "Era para a rainha. Para o aniversário dela. Faltavam doze dias quando o reino… foi."
- **Elva** *(triste)*: "Eu estava fora, a comprar fio de ouro. Quando voltei para casa, não havia casa. Só uma planície e a torre ao fundo."
- **Elva** *(normal)*: "Nunca o acabei. Não consigo. Cada vez que pego na agulha, as mãos não querem."

▶ **"Um dia vais acabá-lo."**
▶ **"É lindo assim."**

- *(acabar)* **Elva** *(triste)*: "Talvez. Quando souber para quem é. Ela já não está aqui para o vestir." ⚙ +30
- *(lindo)* **Elva** *(surpresa)*: "Inacabado? …Talvez seja. Nunca pensei nisso. Coisas inacabadas também são bonitas. Às vezes." ⚙ +30

⚙ Receita de costura **Linho Fino** (tear) e as **Vestes** ficam 10% mais baratas.

### ❤️ 6 — O desfile

| | |
|---|---|
| ID | `cena_elva_6` |
| Quando | 6 ❤️ · Inverno ou início da Primavera (antes da Festa das Flores) · Costura |
| Onde | Costura |
| Quem | herói, Elva |
| Música | `festival` (versão de primavera) |

- **Elva** *(nervosa)*: "Este ano quero fazer uma coisa no desfile da Festa das Flores. Uma coisa grande. Vou acabar o vestido da rainha."
- **Elva** *(normal)*: "Mas preciso de tecidos de seis regiões. Fio de ouro já não chega. Quero que o vestido tenha a torre inteira dentro. Ajudas-me?"

⚙ Missão **N_ELVA_3 O Vestido da Rainha** (secção 9). A Elva aceita jantar em tua casa (comenta as tuas cortinas).

### ❤️ 8 — O reino de Alvorada

| | |
|---|---|
| ID | `cena_elva_8` |
| Quando | 8 ❤️ · noite de lua cheia, telhado da Costura (21:00–23:00) |
| Onde | telhado da Costura, com tecidos a secar ao luar |
| Quem | herói, Elva |
| Música | `tema_elva` (versão curta: harpa e flauta) |

🎬 Lençóis coloridos a secar, a ondular. A Elva sentada no meio, a bordar à luz da lua.
- **Elva** *(triste)*: "A rainha chamava-se Isolda. Era mais nova do que eu. Sabia coser melhor do que eu. Nunca o admiti."
- **Elva** *(feliz)*: "Ensinou-me um ponto. O 'ponto de alvorada': a linha entra e sai como um sol a nascer. Ninguém fora do reino o sabe fazer."
- **Elva** *(triste)*: "Às vezes vejo esse ponto em tecidos que os aventureiros trazem lá de cima. Uma vez numa bandeira rasgada. Outra num lenço."
- **Elva** *(normal)*: "Quer dizer que Alvorada está algures lá dentro. E que alguém ainda cose como ela me ensinou."

▶ **"Vou procurar Alvorada."**
▶ **"Ensina-me o ponto."**

- *(procurar)* **Elva** *(triste)*: "Não. Por favor. Se encontrares… diz-me. Mas não procures. Não quero que subas por mim. Já perdi um reino. Não quero perder um cliente." ⚙ +30 · flag `elva_alvorada` (abre o segredo opcional da secção 9)
- *(ensinar)* **Elva** *(feliz)*: "Dá-me a mão. Assim. Entra, sai, sobe. Como o sol." 🎬 bordam juntos. ⚙ +30 · receita **Ponto de Alvorada** (cosméticos com +2% de esquiva)

⚙ 15% de desconto. Passa a mandar **cartas** com retalhos, botões e, às vezes, um cosmético.

### ❤️ 10 — A capa

| | |
|---|---|
| ID | `cena_elva_10` |
| Quando | 10 ❤️ · `missao(N_ELVA_3) == concluida` · Costura, de manhã |
| Onde | Costura, com o vestido da rainha acabado num manequim ao fundo |
| Quem | herói, Elva |
| Música | `tema_elva` |

🎬 O vestido da rainha está acabado e é lindo. Mas a Elva não está a olhar para ele. Tem uma capa dobrada nos braços.
- **Elva** *(normal)*: "O vestido acabou. Ficou para a cidade: está na Câmara, numa vitrina. O Aldric chorou. Carimbou a vitrina."
- **Elva** *(feliz)*: "Mas os retalhos que sobraram… os retalhos das seis regiões… fiz isto. Para ti."
- 🎬 Abre a capa. Muda de cor devagar: azul, dourado, verde, vermelho.
- **Elva** *(normal)*: "Muda de cor com o teu humor. Não perguntes como. Pus-lhe um fio de fantasma, um fio de estrela e um ponto de alvorada."
- **Elva** *(feliz)*: "Se estiveres triste, fica azul. Se estiveres furios{o/a}, vermelha. Se estiveres feliz… dourada. Quero vê-la dourada."
- 🎬 O herói veste a capa. Fica dourada.
- **Elva** *(feliz, sem "mas")*: "Fica-te bem. Fica-te mesmo bem."

⚙ **Capa Lendária da Elva**: +10% de esquiva (a invencibilidade da esquiva dura mais) e muda de cor com o humor. Título *Bem Vestid{o/a}*.

---

## 9. Missões

### N_ELVA_1 — Mochila Nova (0 ❤️, `andar_maximo >= 2`)
- **Pedir** — **Elva**: "A tua mochila é um saco com alças. Traz-me dez couros e cinco molhos de linho. Faço-te uma a sério."
- **Passo**: entregar **10 Couro** (qualquer couro) + **5 Linho Bravo**.
- **Entregar** — **Elva** *(feliz)*: "Costuras duplas, fundo reforçado, um bolso secreto para o que não queres que a Freya veja. Quarenta espaços." ⚙ **Mochila de Couro** (40) · +100

### N_ELVA_2 — Fio de Fantasma (4 ❤️, `andar_maximo >= 71`)
- **Pedir** — **Elva**: "Ectoplasma. Dez frascos. Dos fantasmas do reino lá em cima. Quero aprender a fiá-lo. E ensinar-te."
- **Passo**: entregar **10 Ectoplasma**.
- **Entregar** — 🎬 a Elva fia o ectoplasma num fio que brilha no escuro. **Elva** *(surpresa)*: "Funciona! Brilha! Fio Espectral! Agora tu também sabes fazer. No tear. Com paciência." ⚙ aprende a tecer **Fio Espectral** · +150

### N_ELVA_3 — O Vestido da Rainha (6 ❤️)
- **Passos**: trazer tecidos de **6 regiões** diferentes, uma peça de cada: Linho Fino (1), Seda de Aranha (2), Pele de Crocodilo (3), Seda do Bazar (4), Lã de Mamute (5), Seda de Alga (6). (Outras regiões podem substituir: Seda Ignífuga (7), Fio Espectral (8), Algodão-Nuvem (9), Fio de Luz Estelar (10).)
- Ter tudo **antes da Festa das Flores** (Primavera, dia 13). Se passar, a missão espera pela do ano seguinte.
- **No festival** — 🎬 desfile na Praça: a Elva apresenta o vestido num manequim. A cidade fica calada. Depois aplaude de pé.
  - **Elva** *(feliz, a chorar)*: "Para a rainha Isolda. Onde quer que esteja. E para Ascendia, que me deixou ficar."
- **Entregar** — ⚙ 1.º lugar no desfile · +200 · o vestido fica na Câmara (decoração da cidade).
- **Segredo opcional** (com a flag `elva_alvorada`): no **andar 76** (jardins do palácio), um estandarte rasgado com um sol a nascer, bordado com o ponto de alvorada, está preso numa sebe. Trazê-lo à Elva dá a fala do "Estandarte de Alvorada" (secção 5) e uma linha especial no epílogo dela: *"Bordou o estandarte de Alvorada de novo e pendurou-o à porta da Costura."* (O reino da Elva **não** é o Reino Assombrado: o estandarte foi lá parar levado por um aventureiro, e ninguém sabe de onde veio.)

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `elva_estado_comum` | todo o equipamento é de raridade Comum | normal | "Tudo Comum. Tudo cinzento. Tudo triste. Tens dinheiro? Gasta-o em ti. Por favor." |
| `elva_estado_encharcado` | `estado(encharcado)` | zangado | "Molhad{o/a}! Nem um passo! Toalha! Ali! Seca-te ali!" |
| `elva_estado_vida` | `vida_pct < 30` | surpresa | "Estás a sangrar na seda! …Primeiro a Igreja. Depois volto a ralhar." |
| `elva_cosmetico_novo` | 1.ª conversa depois de mudar a cor do herói | feliz | "Essa cor! Quem ta escolheu? Fui eu? Fui eu. Tenho bom gosto." |
| `elva_capa_cor` | com a Capa Lendária equipada | feliz | "A capa está {cor}. Então estás {humor}. Eu sei sempre. É o meu segredo agora." |
| `elva_comp_lucien` | o Lucien na Taberna com o fato do concerto | feliz | "Viste o fato do Lucien? Só tem doze penas. Ganhei a discussão. Ele chorou. Ficou lindo." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `elva_serv_abrir` | abrir a Costura | normal | "Mochilas, vestes, cores. E opiniões, de graça." |
| `elva_serv_mochila` | comprar mochila | feliz | "Mais espaço. Menos desculpas para deixares coisas na torre." |
| `elva_serv_vestes` | comprar vestes | normal | "Vestes para quem usa cajado. Leves, bonitas, e a magia passa melhor pelo tecido. Juro." |
| `elva_serv_cores` | mudar a cor do herói | feliz | "Fica quiet{o/a}. …Pronto. Muito melhor. Muito." |
| `elva_serv_cosmetico` | comprar roupa cosmética | feliz | "Por cima da armadura. Ninguém vê a armadura feia. Toda a gente vê a roupa bonita." |
| `elva_serv_vender` | vender tecidos | normal | "Hmm. Este sim. Este não. Este talvez. Pago pelos 'sim'." |
| `elva_serv_sem_ouro` | sem ouro | normal | "Sem ouro? A elegância espera. Mas não muito." |
| `elva_serv_fechado` | fora de horas ou na Cidade Errante | — | `[Sistema] A Costura está fechada. Há um bilhete bordado na porta.` |
