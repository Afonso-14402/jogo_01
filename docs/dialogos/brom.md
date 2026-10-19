# Brom — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.3. Dados: `dados/dialogos/brom.json`.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | graves e curtos, descem no fim das frases (ver `docs/AUDIO.md`) |
| Como fala | frases curtas, resmunga, começa quase tudo com "Hmpf."; fala do metal como se fosse gente; quando se emociona fala ainda menos e muda logo de assunto |
| Repete | "Hmpf.", "O ferro não tem pressa.", "Não é choro. É fumo da forja.", "Pelas barbas do meu pai!" |
| Tiques | limpa as mãos ao avental (animação `limpar_maos`) quando está nervoso; bate com o martelo na bigorna para acabar uma frase |
| Nunca diz | "obrigado" às claras antes dos 6 ❤️ (diz "Hmpf. …Está bem."); nunca admite que canta; nunca diz mal de uma arma bem feita, nem que seja do inimigo |
| Chama ao herói | "miúd{o/a}" até aos 4 ❤️, depois `{nome}`; com 8+ ❤️ às vezes "aprendiz" (é um elogio) |
| Rotina ao Domingo | a Forja está fechada; de manhã está no Rio com o Pip (não pesca, fica sentado); à tarde, em casa, faz brinquedos de ferro para as crianças do Bairro Baixo (não conta a ninguém) |

---

## 2. Primeira conversa

Depois da cena P6 (prólogo), a 1.ª vez que carregas em **Conversar**:

- **Brom** *(zangado)*: "Hmpf. Outro Jogador. Mostra-me essa espada."
- **Brom** *(zangado)*: "Espada de Treino. Madeira com um prego dentro. O Gorvan dá isto a toda a gente."
- **Brom** *(normal)*: "E toda a gente volta cá a precisar de mim. Eu sou o Brom. Forjo, melhoro, encanto e reciclo."
- **Brom** *(normal)*: "Tu trazes os materiais. Eu trago o talento. Cobre, para começar. O cobre é mole, mas é honesto."
- **Brom** *(normal)*: "…Dez mil, hã? A Lyra gritou tão alto que a bigorna tremeu. Número redondo."
- **Brom** *(zangado)*: "Vê se não morres antes de eu te fazer uma arma decente. Detesto trabalho desperdiçado."

⚙ Abre o menu de serviços do Brom: **Forja · Perguntar sobre… · Missões · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_dia_01` | `hora entre 6 e 8` | feliz | "Cedo. Bom. A forja está quente e a cidade ainda está calada. É a melhor hora do dia." |
| `brom_dia_02` | `hora entre 6 e 8` | normal | "Já de pé? Isso é coisa de anão. Hmpf. Começo a gostar de ti. Um bocadinho." |
| `brom_dia_03` | `hora entre 12 e 14` | normal | "Almoço? Como em cima da bigorna. A bigorna não se queixa das migalhas." |
| `brom_dia_04` | `hora entre 17 e 19` | zangado | "Quase a fechar. Se queres uma arma, depressa. Se queres conversa, vai à taberna." |
| `brom_dia_05` | `hora entre 19 e 23` | normal | "Na taberna não se fala de trabalho. …Mostra lá a arma." |
| `brom_dia_06` | `hora entre 20 e 23` | feliz | "Uma caneca, uma cadeira e ninguém a pedir +10. Isto é que é vida." |
| `brom_dia_07` | — | normal | "Volta amanhã. O ferro não tem pressa." |
| `brom_dia_08` | — | zangado | "Hmpf. Mostra-me essa arma. …Quem te ensinou a afiar? Um javali?" |
| `brom_dia_09` | — | normal | "Uma arma boa não é a que corta mais. É a que volta para casa contigo." |
| `brom_dia_10` | — | zangado | "Se ouvires alguém a cantar na forja, é o fole. O fole assobia. Não sou eu." |
| `brom_dia_11` | — | zangado | "A Lyra anda a dizer que eu canto. A Lyra também diz que os patos olham para ela." |
| `brom_dia_12` | — | normal | "O Tobias revendeu uma faca minha como 'faca de anão autêntica'. É autêntica. É isso que me irrita." |
| `brom_dia_13` | `dia_semana == segunda` | zangado | "Segunda-feira. Toda a gente quer a arma pronta para ontem. O ontem já passou." |
| `brom_dia_14` | `dia_semana == sexta` | feliz | "Sexta é braço de ferro na taberna. Ninguém me ganha. A Capitã quase. Quase." |
| `brom_dia_15` | `dia_semana == domingo` | normal | "Domingo. A forja descansa. Eu finjo que descanso. O Pip finge que pesca." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_dia_20` | `estacao == primavera` | zangado | "Primavera. Pólen por todo o lado. Espirrei em cima de uma lâmina quente. Fez fumo verde." |
| `brom_dia_21` | `estacao == primavera && hora entre 6 e 12` | zangado | "A Hana deixou flores à porta da forja, 'para alegrar'. Agora a forja cheira a jardim." |
| `brom_dia_22` | `estacao == verao` | normal | "No verão a forja é um forno e eu sou o pão. Bebe água. Eu bebo cerveja. Não faças como eu." |
| `brom_dia_23` | `estacao == verao && hora entre 17 e 19` | feliz | "Ao fim do dia abro a porta das traseiras e entra ar fresco. É o melhor momento do verão. O único." |
| `brom_dia_24` | `estacao == outono` | normal | "Outono. Toda a gente volta com as armas cheias de lama e folhas. Toda a gente precisa de mim." |
| `brom_dia_25` | `estacao == outono && clima == chuva` | zangado | "Chuva de outono. As lâminas enferrujam só de olhar pela janela. Oleia tudo. TUDO." |
| `brom_dia_26` | `estacao == inverno` | feliz | "Inverno, a melhor estação. A forja é o sítio mais quente da cidade. Vem cá toda a gente. Para aquecer as mãos." |
| `brom_dia_27` | `estacao == inverno && clima == neve` | normal | "Os miúdos do Bairro Baixo vêm cá aquecer-se quando neva. Deixo-os. Não digas a ninguém." |
| `brom_dia_28` | `clima == chuva` | zangado | "Fecha a porta! Água fria em ferro quente faz um barulho que me arrepia a barba." |
| `brom_dia_29` | `clima == trovoada` | normal | "Trovões. O meu pai dizia que eram gigantes a forjar lá em cima. Têm mau ritmo." |
| `brom_dia_30` | `clima == nevoeiro` | normal | "Nevoeiro. Bom dia para trabalhar sem ninguém a espreitar. …Tu estás a espreitar." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_dia_40` | `andar_maximo < 5` | zangado | "Ainda andas com a Espada de Treino? Traz-me cobre e eu faço-te uma a sério." |
| `brom_dia_41` | `boss_derrotado(ent_anciao) && andar_maximo < 15` | feliz | "Do 11 para cima há ferro. FERRO! Agora sim, vamos fazer armas." |
| `brom_dia_42` | `flag(andar_18_visitado) && missao(R2_05) != concluida` | triste | "Já passaste o 18. …Hmpf. Não. Não digas nada. Ainda não." |
| `brom_dia_43` | `missao(R2_05) == concluida` | feliz | "O martelo do meu pai está na parede. Bato-lhe de manhã, para dizer bom dia. É parvo. Faço na mesma." |
| `brom_dia_44` | `andar_maximo >= 31` | normal | "Já me trazes prata. Lembro-me de quando trazias cobre torto. Bons tempos. Maus tempos. Os dois." |
| `brom_dia_45` | `andar_maximo >= 50` | feliz | "Metade da torre. As tuas armas passaram por esta bigorna. Metade da vitória é minha. Um quarto. Um bocadinho." |
| `brom_dia_46` | `andar_maximo >= 53 && andar_maximo < 68` | triste | "Fiz uma lâmina para o rapaz do casaco azul. Está ali, à espera dele. Ninguém lhe toca." |
| `brom_dia_47` | `flag(kai_salvo)` | feliz | "O rapaz veio buscar a lâmina. Disse 'obrigado'. Duas vezes. Acho que está doente." |
| `brom_dia_48` | `missao(R7_03) == concluida` | feliz | "O meu tio manda-me cartas pelo cristal. Escreve mal e só fala de rubis. É mesmo da família." |
| `brom_dia_49` | `andar_maximo >= 81` | normal | "Oricalco. Metal do céu. Se o meu pai me visse a forjar isto…" |
| `brom_dia_50` | `andar_maximo >= 91` | triste | "Metal das estrelas. As minhas mãos tremem quando lhe toco. É do calor. É do calor." |
| `brom_dia_51` | `rank >= C` | normal | "Rank C. Já não és nenhum aprendiz. As tuas armas têm de estar à altura. As minhas estão." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_dia_60` | `coracoes(brom) >= 2` | normal | "Guardei-te o melhor lingote da semana. Não é favor. É que tu não os estragas. Muito." |
| `brom_dia_61` | `coracoes(brom) >= 3` | normal | "Já sei de cor como seguras a arma. Mal. Mas sempre igual. Assim consigo afinar." |
| `brom_dia_62` | `coracoes(brom) >= 4` | triste | "Senta-te no banco. Não, esse não. Esse é do meu pai. …Era. Senta-te no outro." |
| `brom_dia_63` | `coracoes(brom) >= 5` | normal | "Quando demoras a voltar, a forja fica calada demais. Não gosto de silêncio. Faz eco." |
| `brom_dia_64` | `coracoes(brom) >= 6` | feliz | "Ensinei-te a ver o fio de uma lâmina. Agora vês. Isso não se desaprende. É como andar de vagoneta." |
| `brom_dia_65` | `coracoes(brom) >= 8` | feliz | "Aprendiz. …Não te habitues. Só te chamo isso quando fazes as coisas bem. Hoje fizeste." |
| `brom_dia_66` | `coracoes(brom) >= 10` | triste | "Tu és família, {nome}. Não me olhes assim. É fumo. Tudo é fumo." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_dia_70` | `origem == jogador` | zangado | "Falas em 'melhorar' armas como quem carrega num botão. No teu mundo era assim? Que mundo triste." |
| `brom_dia_71` | `origem == atrasado` | normal | "Chegas sempre a correr. Ao ferro não se chega a correr. Respira. O ferro espera." |
| `brom_dia_72` | `origem == ajudante` | normal | "Dizem que ajudas toda a gente. Então carrega este saco de carvão. …Era um teste. Passaste." |
| `brom_dia_73` | `origem == dormir` | zangado | "Tens cara de sono. Aqui o martelo começa às seis. O martelo não pergunta se dormiste bem." |
| `brom_dia_74` | `skill_unica == mestre_artesao` | surpresa | "Mestre Artesão? Tu? Pega no martelo. …Hmm. Hmmmm. Está bem. Tens mãos. Não te gabes." |
| `brom_dia_75` | `skill_unica == mao_de_midas` | zangado | "Mão de Midas? Tudo o que tocas vira ouro? Então não me toques nas ferramentas." |
| `brom_dia_76` | `skill_unica == lingua_universal` | normal | "Se falas com monstros, pergunta aos golens quem os fez. Por motivos profissionais." |
| `brom_dia_77` | `skill_unica == passo_fantasma` | zangado | "Esquivas duas vezes seguidas? Deixa a armadura levar um golpe de vez em quando. Fi-la para isso." |
| `brom_dia_78` | `skill_unica == olho_do_sistema` | triste | "Vês quanto vale tudo? Então não me digas quanto vale esta espada. Para mim vale mais." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `brom_curta_1` | zangado | "Outra vez? Estou a trabalhar." |
| `brom_curta_2` | normal | "Hmpf." |
| `brom_curta_3` | normal | "A arma não fica pronta mais depressa por me olhares." |
| `brom_curta_4` | feliz | "Ainda aqui? Pega numa vassoura, então." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Brom** *(normal)*: "A torre? É pedra. Pedra trabalhada por alguém que sabia o que fazia. E que não assinou. Detesto quem não assina."
- **Brom** *(normal)*: "O meu povo forjava armas lá dentro, no andar 18. Para Jogadores. Os anões sempre souberam que vocês vinham."
- **Brom** *(triste)*: "Dizem que no topo há uma porta para casa. A minha casa era o 18. Fica mais perto. E custa mais."

### 4.2 O andar atual

O Brom fala da **região do andar mais alto** a que chegaste, sempre pelo lado do metal.

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta: cobre. É mole, mas é honesto. Aprende a forjar com cobre; o resto logo se vê." |
| 2 Cavernas | "Cavernas: ferro, carvão e escuro. Leva tochas. E se passares pelo 18… não me contes. Ou conta. Não sei." |
| 3 Pântano | "Pântano: aço. E humidade, que é inimiga do aço. Oleia a lâmina todas as noites. Todas!" |
| 4 Deserto | "Deserto: prata. Brilha e os mortos detestam-na. São as duas qualidades da prata. Não tem mais." |
| 5 Gelo | "Gelo Eterno: não derrete na forja. Tenho de o trabalhar a frio. Traz muito. Vou partir muitos martelos." |
| 6 Oceano | "Coral abissal: metal que cresceu no fundo do mar. Não devia existir. Adoro-o." |
| 7 Vulcão | "Vulcão: obsidiana. E anões do fogo, os Brasa. Família da minha mãe. Diz-lhes… diz-lhes olá. Só olá." |
| 8 Reino Assombrado | "Mitril. MITRIL. O metal mais bonito que há. Traz-mo e eu faço-te chorar de alegria. A ti, não a mim." |
| 9 Céu | "Oricalco: leve como uma pena. Um anão não confia em nada que seja leve. Mas forja-o." |
| 10 Abismo | "Metal das estrelas. Nunca toquei em nenhum. Tenho medo de lhe tocar. …Traz-mo na mesma." |

### 4.3 Rumores

O Brom diz **1 rumor por dia** (os rumores dele são quase sempre sobre metal, armas e anões).

| ID | Condição | Rumor |
|---|---|---|
| `brom_rumor_01` | — | "O Tobias vende 'pedras de amolar mágicas'. São pedras do rio. Sei porque fui eu que lhas vendi." |
| `brom_rumor_02` | — | "O Gizmo pediu-me uma mola. Uma MOLA. Eu sou ferreiro. …Fiz-lha. É a melhor mola de Ascendia." |
| `brom_rumor_03` | `andar_maximo >= 3` | "Ao pé da cascata do andar 3 há cobre aos montes. Os aventureiros passam por ele a olhar para as trutas." |
| `brom_rumor_04` | `andar_maximo >= 8` | "No andar 8 há estátuas de cavaleiros com espadas partidas. Ninguém as conserta. Dá-me nervos." |
| `brom_rumor_05` | `andar_maximo >= 11` | "A Hilda do posto mineiro manda-me minério com bilhetes: 'para o anão da cidade'. Eu respondo: 'obrigado, anã da mina'." |
| `brom_rumor_06` | `andar_maximo >= 11` | "Dizem que o Rei Goblin das minas tem um martelo feito de uma vagoneta. Quero ver isso. Para me rir." |
| `brom_rumor_07` | `andar_maximo >= 11 && missao(R2_13) != concluida` | "Há um rapaz no posto mineiro, o Pedrito, que quer aprender comigo. Mãos de manteiga. Mas tem vontade." |
| `brom_rumor_08` | `andar_maximo >= 18` | "Debaixo das forjas do 18 há uma mina com o ouro de um rei anão. Os anões não deixam ouro sem guarda. Leva luz." |
| `brom_rumor_09` | `andar_maximo >= 20` | "Um núcleo de golem metido numa arma faz a arma cantar. Eu não canto. A arma é que canta." |
| `brom_rumor_10` | `andar_maximo >= 24` | "Os Homens-Lagarto fazem lanças que não partem. Não sei como. Não durmo bem por causa disso." |
| `brom_rumor_11` | `andar_maximo >= 31` | "Há areia no deserto que corta como vidro. A Selene compra-a aos sacos. Eu fujo dela." |
| `brom_rumor_12` | `andar_maximo >= 41` | "Fiz uma colher de Gelo Eterno. A sopa fica sempre fria. A Dona Marta quer-me matar." |
| `brom_rumor_13` | `andar_maximo >= 61` | "Os Brasa, no 64, guardam os moldes das armas dos primeiros Jogadores. Moldes de mil anos. MIL." |
| `brom_rumor_14` | `andar_maximo >= 71` | "O mitril só obedece depois de lavado com Água Benta. Até o metal tem medo dos mortos." |
| `brom_rumor_15` | `andar_maximo >= 91` | "Um tal Dorn tem uma forja de estrelas no 91. Cego de um olho. Quero conhecê-lo. Para discutir." |
| `brom_rumor_16` | `estacao == inverno` | "No Festival da Estrela há amigo secreto. Se te calhar eu: lingotes. Não flores. Lingotes." |
| `brom_rumor_17` | `missao(R8_11) == concluida` | "O ferreiro que trouxeste do Reino trabalha bem. Calado. Martela como quem pede desculpa. Gosto dele." |

### 4.4 A vida dele

| Corações | Fala |
|---|---|
| 0 | "A minha vida? Ferro, fogo, martelo. E gente a fazer perguntas. Mostra a arma ou vai-te." |
| 2 | "Nasci numa forja. A minha primeira palavra foi 'quente'. A segunda foi 'ai'." |
| 4 | "O meu pai era o **Grimbold Martelo-Forte**, mestre da Forja Anã, no andar 18. Fugi de lá com dez anos. Nunca voltei." |
| 6 | "A minha mãe era **Sigrid Brasa**, dos anões do fogo. Como chegou ao 18, nunca me contou. Dizia só: 'Subi a descer.'" |
| 8 | "Há cento e trinta anos que forjo para Jogadores. O meu pai também forjava. Às vezes acho que estou a acabar o trabalho dele." |
| 10 | "Já não tenho medo do 18. Tenho um martelo, um tio, uma forja e {um amigo/uma amiga} teimos{o/a}. Um anão não precisa de mais." |

---

## 5. Presentes

**Adora:** Minério de Mitril, Assado de Javali, Rubi · **Gosta:** lingotes, carne ·
**Detesta:** flores, Gel de Slime, armas partidas. O resto é **neutro** (ver `docs/ITENS.md`, secção dos presentes).

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "Isto… isto é para mim? Hmpf. Pousa aí. Devagar! …Não é choro. É fumo da forja." · "Pelas barbas do meu pai! Sabes o que me trouxeste? SABES? Sabes, sim. Por isso é que trouxeste." |
| Gosta | "Hmpf. Serve. Serve bem. …Está bem. Obrigado. Pronto, já disse." · "Isto é coisa que se aproveita. Gosto de coisas que se aproveitam. E de quem as traz." |
| Neutro | "Hmm. Uma coisa. Obrigado pela coisa." · "Vou pôr ali, ao pé das outras coisas que não sei para que servem." |
| Não gosta | "…Porquê? Não, a sério. Porquê?" |
| Detesta | "Flores. Na minha forja. Vão arder em dois segundos. Um. Dois. Pronto." · "Gel de Slime! Tira isso da bigorna! Vai entrar nas juntas do martelo!" |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Minério de Mitril | "Mitril. Em bruto. Nas minhas mãos. Vou fazer uma coisa tão bonita que vais ter de usar óculos de sol." |
| Assado de Javali | "Assado de javali! O meu pai fazia isto nos dias de festa. Este está quase tão bom. Quase. Come metade comigo." |
| Rubi | "Um rubi. A minha mãe tinha um assim, numa conta da barba. Os Brasa usam-nos todos. …Fica comigo. Obrigado." |
| Lingote Antigo | "Isto é do 18. Tem a marca da forja. Um martelo e uma montanha. …Vou guardá-lo. Não o vou derreter. Nunca." |
| Chifre Partido (ou outra arma com "Partid{o/a}" no nome) | "Uma arma com 'partido' no nome. Como presente. Para um ferreiro. …Hmpf. Dá-me lingotes. Lingotes inteiros." |
| Pedra | "Uma pedra. Obrigado. Tenho uma montanha delas. Agora tenho uma montanha e uma." |
| Cerveja de Mel (se existir na Taberna) | "Cerveja! Isto não é presente, é bom senso. Senta-te. Bebemos à saúde do ferro." |

---

## 6. Aniversário e festivais

**Aniversário (Inverno, dia 9):**
- Sem presente: **Brom** *(zangado)*: "Hoje faço anos. Não perguntes quantos. Mais do que tu e menos do que a Selene."
- Com presente que adora: **Brom** *(feliz)*: "Lembraste-te. Ninguém se lembra dos anos do ferreiro. Toda a gente se lembra da arma. …É fumo. Vai-te."
- Com outro presente: **Brom** *(normal)*: "Um presente de anos. Hmpf. Está bem. Hoje não resmungo. Até às seis da tarde."
- Na Taberna há bolo com uma vela em forma de martelo: 🎬 o Lucien canta-lhe uma canção; o Brom finge que não ouve e bate o pé no ritmo.

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Flores. A cidade inteira cheira a flores. Vou passar o dia dentro da forja com a porta fechada." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Brom** *(surpresa)*: "Os anões não dançam. Os anões… marcam o ritmo com os pés. …Uma vez. UMA." ⚙ dança · +100 amizade |
| F_02 Festival da Pesca | "O Pip arrastou-me para o concurso. Eu trouxe uma rede de ferro. Não é batota se fores tu a fazer a rede." |
| F_03 Noite dos Espíritos | "Pus uma abóbora à porta da forja. A abóbora é feia. O fogo lá dentro é bonito." (depois de R2_05: "Este ano a lanterna é para o meu pai. Para saber onde estou.") |
| F_04 Festival da Estrela | "Amigo secreto. Calhou-me a Selene. O que se dá a uma elfa que explode coisas? Um avental de ferro. Pesa doze quilos." |
| F_05 Dia da Subida | "A cidade bebe à tua saúde. Eu também. Duas vezes. Uma por ti, outra pela tua arma." |
| F_06 Concurso da Casa | "Põe uma parede de armas na sala. Os juízes não percebem nada, mas eu dava-te dez pontos. Não sou juiz." |
| F_07 Noite das Lanternas | *(triste)* "Ponho uma lanterna por cada Jogador que levou uma arma minha e não voltou. São muitas. Não falo disto." |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`). O Brom repara sempre na **arma única** que o boss deixou.

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `brom_boss_javali_rei` | "Fizeram um machado com a presa do Javali-Rei? Quem, a torre? Hmpf. O fio está torto. Dá cá." |
| Ent Ancião (10) | `brom_boss_ent_anciao` | "A Lyra contou-me da árvore grande que morreu. A que falava. …É fumo. Vai-te embora. Volta amanhã." |
| Aranha-Mãe (15) | `brom_boss_aranha_mae` | "Aranhas. Detesto aranhas. Fazem ninho na chaminé. Fizeste muito bem." |
| Golem de Cristal (20) | `brom_boss_golem_cristal` | "Pedra que anda. Quem o fez sabia trabalhar pedra. E tu partiste-o todo. E ganhaste uma casa! Põe uma parede para armas." |
| Serpente do Lodo (25) | `brom_boss_serpente_lodo` | "Lodo na lâmina, lodo nas botas, lodo no meu chão. O lodo come o aço. Deixa a arma. Limpo-a de graça. Desta vez." |
| Hidra do Pântano (30) | `brom_boss_hidra_pantano` | "Cabeças que voltam a crescer quando lhes bates. Há ferro assim. Teimoso. Tu também és assim." |
| Escorpião Imperador (35) | `brom_boss_escorpiao_imperador` | "A carapaça daquele bicho é melhor do que muitas armaduras que vi. Traz um bocado. Para estudar. Não para gostar." |
| Faraó Eterno (40) | `brom_boss_farao_eterno` | "O Fausto não se cala com o rei que também foi Jogador. Eu só quero saber da espada curva. Bonita. Detesto admitir." |
| Yeti Ancião (45) | `brom_boss_yeti_anciao` | "Manoplas feitas dos punhos de um yeti. A torre tem um gosto muito estranho para armas." |
| Dragão de Gelo (50) | `brom_boss_dragao_gelo` | "Metade da torre. Fiz um brinde na taberna. Um só. Bem, três. Pela metade, pela outra metade e por ti." |
| Capitão Esqueleto (55) | `brom_boss_capitao_esqueleto` | "Piratas mortos com sabres velhos. Sal e ferrugem. Odeio sal. Odeio ferrugem. Fizeste muito bem." |
| Leviatã (60) | `brom_boss_leviata` | "O mar acabou. E o rapaz do casaco azul não voltou. …Fiz-lhe uma lâmina nova. Fica ali. À espera." |
| Ferreiro Infernal (65) | `brom_boss_ferreiro_infernal` | (conversa mais longa: ver abaixo) |
| Kai — salvo (68) | `brom_boss_kai_salvo` | "O rapaz voltou. Diz-lhe que tenho uma lâmina à espera dele desde o mar. E que não a parta." |
| Kai — vencido (68) | `brom_boss_kai_vencido` | "…Senta-te. Não digas nada. Eu tenho trabalho e tu tens um banco ao pé da forja. Fica o tempo que quiseres." |
| Titã de Magma (70) | `brom_boss_tita_magma` | "O coração do vulcão. Os Brasa vivem ao lado daquilo. Vão fazer festa uma semana. Com fogo. Claro." |
| Lich Bibliotecário (75) | `brom_boss_lich_bibliotecario` | "Livros que lançam fogo. O Fausto está encantado. Eu prefiro livros que fiquem quietos. E fechados." |
| Rei Sem Coroa (80) | `brom_boss_rei_sem_coroa` | "Os cavaleiros do Reino usavam mitril. Mitril! Se trouxeste um bocadinho… Não, nada. Parabéns. E traz mitril." |
| Grifo Real (85) | `brom_boss_grifo_real` | "Aquilo voa e tu acertaste-lhe. Com quê? Mostra. …Hmpf. Com uma arma minha. Claro." |
| Serafim Caído (90) | `brom_boss_serafim_caido` | "Estás calad{o/a}. Os anões dizem: quando o ferro fica calado, ainda está quente. Fica ao pé da forja até arrefeceres." |
| Guardião do Tempo (95) | `brom_boss_guardiao_tempo` | "Andar 95. Tenho cento e quarenta anos e nunca vi ninguém chegar tão alto. Nem o meu pai sonhava com isto." |

**Ferreiro Infernal** (`brom_boss_ferreiro_infernal`): o herói traz a **Arma Inacabada Nº 10 000** (ver `docs/BOSSES.md`, secção 13).
- **Brom** *(normal)*: "Um demónio que forjava para Jogadores que ainda não tinham chegado. Isso não é forjar. É esperar."
- 🎬 O Brom passa o polegar pelo número gravado na lâmina.
- **Brom** *(surpresa)*: "Dez mil. Gravado à mão. Esta coisa estava à tua espera antes de tu chegares."
- **Brom** *(triste)*: "Ficou a meio. Quem a começou parou… como quem ainda não sabe para quem é."
- **Brom** *(zangado)*: "Deixa-ma cá. Um dia acabo-a. …E não é choro. É fumo. Lá de cima. Do 65."
- ⚙ A arma fica pendurada na forja até à cena de 10 ❤️.

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — A canção do martelo

| | |
|---|---|
| ID | `cena_brom_2` |
| Quando | 2 ❤️ · entrar na Forja entre as 6:00 e as 7:00 (acabou de abrir e pensa que está sozinho) |
| Onde | Forja do Brom |
| Quem | herói, Brom |
| Música | silêncio → só o martelo e a voz do Brom |

🎬 A forja ainda está meio escura. O Brom está de costas, a bater numa lâmina ao ritmo do martelo. E canta, baixinho, com uma voz grave e afinada.

- **Brom** *(a cantar)*: "♪ Bate o ferro, bate o fogo, quem não bate não é anão… ♪"
- **Brom** *(a cantar)*: "♪ Bate o ferro, bate o fogo, que a montanha é o nosso chão… ♪"
- 🎬 Vira-se para pegar nas tenazes. Vê o herói. Fica parado com as tenazes no ar.
- **Brom** *(surpresa)*: "…"
- **Brom** *(zangado)*: "Há quanto tempo estás aí?"

▶ **"Cantas bem!"**
▶ **"Não ouvi nada."**
▶ *(bater palmas)*

- *(Cantas bem)* **Brom** *(zangado)*: "Eu NÃO canto. Eu marco o ritmo do martelo. Com a boca. É diferente." ⚙ +30
- *(Não ouvi nada)* **Brom** *(normal)*: "…Ótimo. Não ouviste. E se a Lyra perguntar, também não ouviste." ⚙ +30
- *(palmas)* 🎬 O Brom fica vermelho até às orelhas. **Brom** *(zangado)*: "Para com isso! As palmas estragam a têmpera!"
- 🎬 Silêncio. Limpa as mãos ao avental.
- **Brom** *(triste)*: "Era a canção do meu pai. Cantava-a a forjar. Dizia que o ferro gosta de música. Que fica mais direito."
- **Brom** *(normal)*: "Pronto. Já sabes. Não contes a ninguém. A ninguém, miúd{o/a}."

⚙ 5% de desconto na forja.

### ❤️ 4 — O martelo pequeno

| | |
|---|---|
| ID | `cena_brom_4` |
| Quando | 4 ❤️ · entrar na Taberna "O Primeiro Degrau" entre as 20:00 e as 23:00 |
| Onde | Taberna, mesa do canto ao pé da lareira |
| Quem | herói, Brom, (Lucien ao fundo) |
| Música | `taberna` (versão calma, com alaúde) |

🎬 O Brom está sozinho com uma caneca. Em cima da mesa há um martelo pequeno e gasto, com o cabo enrolado em couro velho.

- **Brom** *(normal)*: "Senta-te. Não, não te vou pedir minério. Senta-te só."
- 🎬 Empurra o martelo pequeno na direção do herói.
- **Brom** *(normal)*: "É o martelo velho do meu pai. O pequeno, dos acabamentos. Ele usava o grande para bater e este para acertar."
- **Brom** *(triste)*: "Trouxe-o quando fugi do 18. Era a única coisa que me cabia na mão. Tinha dez anos."

▶ **"Porque é que fugiste?"**
▶ **"O teu pai também fugiu?"**

- **Brom** *(triste)*: "Uma noite as fornalhas apagaram-se todas ao mesmo tempo. E das minas fundas começaram a subir… coisas."
- **Brom** *(triste)*: "O meu pai pôs-me nas mãos de um Jogador que estava de passagem e disse: 'Corre.' Eu corri. Ele ficou."
- **Brom** *(normal)*: "Nunca soube o que lhe aconteceu. Nunca lá voltei. Tenho medo do que vou encontrar. Ou de não encontrar nada."
- 🎬 O Lucien, ao fundo, começa uma canção triste. O Brom esfrega os olhos.
- **Brom** *(zangado)*: "Não é choro. É fumo da lareira. …Lucien! Toca outra coisa!"
- **Brom** *(normal)*: "Toma. Não é o martelo, esse não sai daqui. É a receita do assado do meu pai. Fazia-o nos dias de festa."
- **Brom** *(feliz)*: "A Dona Marta faz melhor. Não lhe digas que eu disse isto. Nem o contrário."

⚙ Recebe a receita **Assado de Javali** (ver `docs/ITENS.md`). +30 amizade se escolheste a 1.ª pergunta (ele gosta de quem pergunta direito).

### ❤️ 6 — A marca do martelo

| | |
|---|---|
| ID | `cena_brom_6` |
| Quando | 6 ❤️ · `flag(andar_18_visitado)` · entrar na Forja entre as 8:00 e as 17:00 |
| Onde | Forja do Brom |
| Quem | herói, Brom |
| Música | `forja` → `forja_ana` (versão lenta) |

> Esta é a conversa de exemplo de `docs/NPCS.md`, secção 5, escrita por inteiro.

🎬 O Brom está à bigorna. Nem levanta os olhos.

- **Brom** *(zangado)*: "Hmpf. Outra vez tu? Mostra-me essa espada."

▶ **"Está como nova!"**
▶ **"Acho que lhe parti a ponta…"**
▶ **"Queres ver o que encontrei no andar 18?"**

- *(como nova)* **Brom** *(zangado)*: "Como nova. Dizes sempre isso. Nunca está." → volta às escolhas (a 3.ª fica a brilhar).
- *(parti a ponta)* **Brom** *(zangado)*: "PARTISTE? …Não partiste. Está só torta. Não me pregues sustos." → volta às escolhas.
- *(andar 18)* 🎬 O martelo para no ar.
- **Brom** *(triste)*: "O andar 18? A forja dos anões?… Mostra. MOSTRA!"
- 🎬 O herói tira da mochila um **Lingote Antigo**. O Brom pega nele com as duas mãos e vira-o devagar. Tem uma marca: um martelo em cima de uma montanha.
- **Brom** *(triste)*: "A marca do mestre da forja. Todos os lingotes levavam esta marca. Era a marca do meu pai."
- **Brom** *(normal)*: "Viste o Grande Portão? Com quatro anéis de pedra cheios de runas? Estava fechado?"
- **Brom** *(normal)*: "O meu pai fechava tudo com o meu nome. A arca das ferramentas. A porta de casa. Dizia que era o nome mais forte que conhecia."
- **Brom** *(triste)*: "Se o portão está fechado… experimenta B-R-O-M. Se abrir, é porque foi ele que o fechou."
- 🎬 Silêncio. Limpa as mãos ao avental três vezes seguidas.
- **Brom** *(triste)*: "Eu não consigo lá ir, {nome}. Já tentei. Chego ao cristal e as pernas não andam."
- **Brom** *(normal)*: "Vai tu. Por favor. …Pronto, disse 'por favor'. Não contes à Lyra."

▶ **"Eu vou."**
▶ **"Vamos descobrir o que aconteceu."**

- *(Eu vou)* **Brom** *(normal)*: "Leva luz. Muita luz. Os anões gostavam de escuro, mas os fantasmas gostam mais." ⚙ +30
- *(Vamos descobrir)* **Brom** *(triste)*: "'Vamos.' Hmpf. Gosto dessa palavra. Há cento e trinta anos que ninguém a diz comigo." ⚙ +30

⚙ `[Sistema] Missão iniciada: O Martelo do Pai.` Missão **R2_05** ativa. O Brom aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — A adaga a quatro mãos

| | |
|---|---|
| ID | `cena_brom_8` |
| Quando | 8 ❤️ · Domingo, das 14:00 às 18:00 · entrar na Forja (fechada ao público) |
| Onde | Forja do Brom, com a porta trancada por dentro |
| Quem | herói, Brom |
| Música | `forja` (versão com voz grave a cantarolar) |

- (no Sábado, na Forja) **Brom** *(normal)*: "Amanhã. Domingo. Duas da tarde. Aqui. A forja está fechada, mas bates três vezes. Não te atrases."

🎬 A porta abre-se ao 3.º toque. A forja está acesa só para os dois. Há dois aventais pendurados: um enorme e queimado, outro novo, mais pequeno.

- **Brom** *(normal)*: "Veste o avental. É teu. Fi-lo esta semana. Não é presente, é equipamento de segurança."
- **Brom** *(normal)*: "Hoje vais forjar uma adaga. Tu. Eu só seguro e grito."
- **Brom** *(feliz)*: "Primeira regra: o ferro não tem pressa. Segunda regra: tu também não. Terceira: não toques no martelo grande."

⚙ **Minijogo de forja**: bater no ritmo do Brom (uma barra anda de um lado para o outro, como no braço de ferro). 3 rondas.

- 🎬 Na 2.ª ronda, o Brom começa a cantar sem dar por isso: "♪ Bate o ferro, bate o fogo… ♪"

▶ *(cantar com ele)*
▶ *(marcar o ritmo em silêncio)*

- *(cantar)* 🎬 O Brom para um segundo, surpreendido. Depois canta mais alto. **Brom** *(feliz)*: "♪ …que a montanha é o nosso chão! ♪ Desafinad{o/a}. Mas no ritmo. Isso é que conta." ⚙ +30
- *(silêncio)* **Brom** *(feliz)*: "Bom ritmo. Tens o martelo no braço. Agora só falta tê-lo na cabeça." ⚙ +30
- 🎬 A adaga sai da água a fumegar. O Brom pega nela e olha-a contra a luz da fornalha durante muito tempo.
- **Brom** *(surpresa)*: "…Hmpf."
- **Brom** *(normal)*: "Está direita. A lâmina está direita. Na primeira vez a minha saiu em forma de colher."
- 🎬 Grava qualquer coisa no cabo com um punção: o nome do herói e, por baixo, pequenino, "BROM".
- **Brom** *(feliz)*: "Quatro mãos, dois nomes. É assim que os anões marcam a primeira arma de um aprendiz."
- **Brom** *(normal)*: "Aprendiz. Sim, ouviste bem. Não te habitues. Só te chamo isso aos domingos."

⚙ Recebe a **Adaga a Quatro Mãos** (adaga do tier da região mais alta a que chegaste, qualidade Excelente garantida, com os dois nomes gravados).
⚙ 15% de desconto na forja. O Brom passa a mandar **cartas** (1 por semana) com presentes: um lingote do teu tier, Assado de Javali ou uma pedra de amolar (decoração).

### ❤️ 10 — A Décima Milésima

| | |
|---|---|
| ID | `cena_brom_10` |
| Quando | 10 ❤️ · `boss_derrotado(ferreiro_infernal)` · a Arma Inacabada Nº 10 000 está na parede da forja · entrar na Forja entre as 18:00 e as 20:00 |
| Onde | Forja do Brom, depois de fechar (fica acesa toda a noite) |
| Quem | herói, Brom, Mestre Ragnar (só se `missao(R7_03) == concluida`) |
| Música | `tema_brom` (martelos em ritmo + coro grave de anões) |

🎬 A forja está mais quente do que nunca. O Martelo Forte-Rocha já não está na parede: está na bigorna, ao lado da arma inacabada. (Se fizeste R7_03: o **Ragnar** está ao fole, com a barba cheia de contas de rubi.)

- **Brom** *(normal)*: "Chegaste. Bom. Fecha a porta. Hoje não há clientes."
- *(com o Ragnar)* **Ragnar** *(feliz)*: "AH! O pequeno dos Martelo-Forte tem amigos! Subi sessenta e quatro andares para ver isto!"
- *(com o Ragnar)* **Brom** *(zangado)*: "Desceste, tio. Desceste sessenta e quatro andares. Pelo cristal. Sentado."
- 🎬 O Brom pega na arma inacabada. Passa o polegar pelo número: **10 000**.
- **Brom** *(normal)*: "Lembras-te? Quem a começou parou a meio, sem saber para quem era. Custou-me perceber o que lhe faltava."
- **Brom** *(feliz)*: "Faltava isto: começou-a um demónio para alguém que ainda não tinha chegado. Acaba-a um anão para alguém que chegou."
- **Brom** *(normal)*: "Pega no martelo pequeno do meu pai. O dos acabamentos. Eu bato com o grande. Tu acertas."

⚙ Minijogo de forja (curto, impossível de falhar: se errares o ritmo, o Brom acerta por ti).

- 🎬 Os dois martelos batem à vez. O Brom começa a cantar. *(com o Ragnar: o Ragnar canta com ele, uma voz ainda mais grave.)*
- **Brom** *(a cantar)*: "♪ Bate o ferro, bate o fogo, quem não bate não é anão… ♪"
- 🎥 A câmara afasta-se devagar: a forja acesa na noite de Ascendia, faíscas a sair pela chaminé como estrelas.
- 🎬 Corte para a madrugada. A espada está pronta: lâmina clara com um veio vermelho, e no cabo o número **10 000** e, por baixo, os nomes de quem a fez.
- **Brom** *(normal)*: "A Décima Milésima. Não tem fim. Cresce contigo. Tu sobes, ela sobe. Fi-la assim de propósito."
- **Brom** *(normal)*: "Assim nunca vais precisar de outra arma. E nunca vais ter desculpa para não voltar cá para a afinar."
- 🎬 Esfrega os olhos com as costas da mão, todo sujo de fuligem.
- **Brom** *(triste)*: "Não é choro. É fumo da forja."

▶ **"Eu sei."**
▶ *(abraçá-lo)*

- *(Eu sei)* **Brom** *(feliz)*: "…Pois. Tu sabes. Tu sabes sempre."
- *(abraçar)* 🎬 O Brom fica muito quieto. Depois dá-te três palmadas nas costas, fortes demais. **Brom** *(feliz)*: "Pronto. Pronto. Chega. A forja está a ver."
- *(com o Ragnar)* **Ragnar** *(feliz, a chorar)*: "Os Brasa também têm fumo, pequeno. Muito fumo. É de família!"

⚙ Recebe **A Décima Milésima** (espada Lendária, ver `docs/ARMAS.md`, secção 8). Título *Sangue de Forja*.
⚙ A partir daqui o Brom tem a fala `brom_dia_66` e, no epílogo, aparece a forjar ao lado do tio Ragnar (ver `docs/HISTORIA.md`, secção 7).

---

## 9. Missões

### N_BROM_1 — Minério para Começar (0 ❤️, rank F, `andar_maximo >= 2`)

- **Pedir** — **Brom** *(zangado)*: "Queres uma arma a sério? Traz-me dez Minério de Cobre. Há rochas com veios cor de laranja nos andares 1, 3, 5 e 8."
  - **Brom** *(normal)*: "Picareta? Não tens picareta. Claro que não tens. Toma a minha velha. EMPRESTADA. Se a partes, partes-me o coração."
  - ▶ **"Combinado!"** ⚙ missão iniciada · recebe a **Picareta Velha** (tier 1, emprestada) · ▶ **"Agora não."** → "Hmpf. O cobre também não tem pressa."
- **Durante** — **Brom**: "Quantos trazes? {n}? Faltam {10-n}. O andar 3 tem uma cascata cheia deles. Os aventureiros olham para as trutas."
- **Entregar** — **Brom** *(normal)*: "Dez. Bom cobre. Pouca pedra agarrada. Afinal sabes bater numa rocha."
  - 🎬 O Brom atira a picareta velha para um canto e pousa uma nova na bigorna, a brilhar.
  - **Brom** *(feliz)*: "Picareta de Cobre. Tua. Não emprestada. Agora já não tens desculpa para me trazeres pouco minério."
  - ⚙ **Picareta de Cobre** · 150 ouro · +120 amizade · flag `brom_confia` (a Picareta Velha volta para o Brom)

### R2_05 — O Martelo do Pai (6 ❤️, começa na cena de 6 ❤️)

- **Passos**:
  1. Ir ao andar 18 e abrir o **Grande Portão Anão**: rodar os 4 anéis de runas até formarem **B-R-O-M**.
  2. Reacender as **3 fornalhas** do Salão das Forjas (os fantasmas só se veem com luz).
  3. Falar com o **fantasma de Grimbold** na Câmara do Mestre (a conversa dele está em `docs/dialogos/povoacoes_r02.md`).
  4. Apanhar o **Martelo Forte-Rocha** na bigorna da Câmara do Mestre.
  5. Voltar à Forja do Brom.
- **O que o fantasma conta** (resumo, para o Brom reagir certo): o Grimbold ficou a segurar o portão para os outros fugirem e fechou-o com o nome do filho, para que só o Brom (ou alguém mandado por ele) o abrisse. Deixa um recado: *"Diz ao meu rapaz que o portão aguentou. E que eu ouvia-o cantar."*
- **Durante** — **Brom** *(triste)*: "Ainda não foste? Não faz mal. Esperei cento e trinta anos. Espero mais uns dias. …Mas vai."
- **Entregar** — 🎬 o herói pousa o Martelo Forte-Rocha na bigorna. O Brom não lhe toca durante três segundos.
  - **Brom** *(triste)*: "É ele. O cabo tem a marca dos dedos dele. Olha. Gastou a madeira com tanto trabalho."
  - ▶ **"Ficou a segurar o portão."** → **Brom** *(triste)*: "Ficou. Claro que ficou. Os Martelo-Forte não largam o que seguram."
  - ▶ **"Disse: 'o portão aguentou'."** → **Brom** *(triste)*: "Aguentou. Cento e trinta anos. Com o meu nome. Pelas barbas do meu pai…"
  - 🎬 (depois de qualquer escolha) o herói ainda tem uma escolha: ▶ **"E que te ouvia cantar."**
  - **Brom** *(surpresa)*: "…Ouvia?"
  - 🎬 O Brom esfrega os olhos. **Brom** *(zangado)*: "Não é choro. É fumo da forja."
  - 🎬 A câmara mostra a fornalha: está apagada. O Brom olha para ela. Olha para o herói.
  - **Brom** *(triste)*: "…Pois. Desta vez é choro."
  - **Brom** *(normal)*: "O cabo está rachado. Ponho-lhe aros de ferro novos, mas a madeira fica. A madeira tem as mãos dele."
  - **Brom** *(normal)*: "Depois penduro-o ali, por cima da bigorna. Para ele ver o trabalho."
  - **Brom** *(normal)*: "O meu pai tinha um truque. Três batidas antes de cada melhoria. Uma pelo ferro, uma pelo fogo, uma por quem a vai usar."
  - **Brom** *(feliz)*: "Nunca o ensinei a ninguém. Agora ensino. A ti."
  - ⚙ A forja ganha a **Forja Anã** (+10% de sucesso nas melhorias) · +200 amizade · flag `brom_pai_encontrado`

### R7_03 — O Tio Ragnar (`andar_maximo >= 64`)

- **Pedir** — **Brom** *(surpresa)*: "Foste ao 64? Ao Bastião dos Brasa? Há lá um Ragnar? Barba com contas de rubi?"
  - **Brom** *(triste)*: "É o irmão da minha mãe. Nunca o vi. Ela dizia que ele ria tão alto que caíam pedras do teto."
  - **Brom** *(normal)*: "Leva-lhe isto. É uma carta. NÃO a leias. Escrevi-a nove vezes e continua mal escrita."
  - ▶ **"Levo já."** ⚙ missão iniciada · recebe a **Carta do Brom** (item de missão) · ▶ **"Depois."** → "Depois. Sim. Também andei a dizer 'depois' cento e trinta anos."
- **Passos**: levar a carta ao **Mestre Ragnar Brasa** (Bastião de Obsidiana, andar 64) · ele lê e escreve a resposta (falas dele em `docs/dialogos/povoacoes_r07.md`) · trazer a **Resposta do Ragnar** e uma **conta de rubi** da barba dele.
- **Durante** — **Brom** *(normal)*: "Já lha deste? O 64 é longe, eu sei. Mas a carta pesa-me. E é só papel."
- **Entregar** — 🎬 o Brom lê a carta duas vezes. Ri-se uma vez, alto. Depois fica calado.
  - **Brom** *(feliz)*: "Escreve mal. Pior do que eu. Diz que tenho a barba da minha mãe. Como é que ele sabe? Nunca me viu."
  - 🎬 Mostra-lhe a conta de rubi. O Brom entrança-a na barba, devagar, ao lado dos anéis de ferro.
  - **Brom** *(triste)*: "Os Brasa dão uma conta destas a quem é da família. A minha mãe tinha uma. Perdi-a quando fugi."
  - **Brom** *(normal)*: "Ele manda-te um segredo da Forja de Obsidiana. Para a minha forja. Diz que é 'para o sobrinho deixar de fazer armas moles'."
  - ⚙ A forja ganha a **Forja de Obsidiana** (+5% de sucesso nas melhorias) · +200 amizade · flag `brom_ragnar` · o retrato e o sprite do Brom passam a ter **uma conta de rubi** na barba

### N_MIA_1 — Primeira Espada (missão da Mia: a parte do Brom)

- **Pedir** (com a missão da Mia ativa) — ▶ **"Fazes uma espada para a Mia?"**
  - **Brom** *(zangado)*: "Uma espada? Para a miúda das flores? Tem onze anos!"
  - **Brom** *(triste)*: "…Eu tinha dez quando peguei no primeiro martelo."
  - **Brom** *(normal)*: "Uma espada pequena. Sem fio. De treino. Volta amanhã. E não lhe digas que fui eu. Diz que foi a torre."
- **Entregar** (no dia seguinte) — **Brom** *(normal)*: "Toma. O cabo está à medida da mão dela. Já a vi a segurar o pau. Segura bem. Melhor do que tu."
  - ⚙ **Espada Pequena da Mia** (item de missão, para levar à Mia) · +30 amizade com o Brom

### R2_13 — Aprendiz do Brom (missão do Pedrito: a parte do Brom)

- 🎬 O herói entra na forja com o Pedrito, que segura o boné com as duas mãos.
- **Brom** *(zangado)*: "Um aprendiz? Não preciso de aprendiz. Preciso de silêncio. E de carvão. Ele é carvão? Não é carvão."
- ▶ **"Ele lembra-me alguém."** → **Brom** *(triste)*: "Lembra quem? …Hmpf. Eu sei quem. Não digas." ⚙ aceita · +30
- ▶ **"O teu pai também te ensinou."** → **Brom** *(triste)*: "…Ensinou. Com paciência. Eu não tenho paciência. Mas posso fingir. Ele também fingia." ⚙ aceita · +30
- ▶ **"Ele trabalha de graça."** → **Brom** *(zangado)*: "De graça ninguém trabalha bem. Volta amanhã com uma razão melhor." ⚙ tenta outra vez no dia seguinte
- (se aceitar) **Brom** *(normal)*: "Pedrito. Pega naquela vassoura. Toda a gente começa pela vassoura. Eu comecei pela vassoura."
- ⚙ O Pedrito passa a trabalhar na forja: melhorias **+1 a +5** ficam 20% mais baratas (ver `docs/CIDADES.md`, secção 1.5).

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_estado_vida` | `vida_pct < 30` | zangado | "Estás a sangrar no meu chão! Vai à Igreja. Agora. E não te deites na bigorna, não é cama!" |
| `brom_estado_maldito` | `estado(amaldicoado)` | surpresa | "Tens uma nuvem roxa à volta da cabeça. Isso não sai com martelo. Vai à Irmã Célia." |
| `brom_estado_cansado` | `estado(cansado)` | normal | "Tens olheiras até à barba. Que não tens. Vai dormir. Com sono, a mão treme e o ferro sabe." |
| `brom_estado_molhado` | `estado(encharcado)` | zangado | "Estás a pingar! Tira essa arma molhada de ao pé do ferro quente! Ferrugem! FERRUGEM!" |
| `brom_estado_sapo` | `estado(sapo)` | surpresa | "Um sapo na minha forja. Com a tua mochila. …{nome}? Hmpf. Ao menos os sapos não pedem +10." |
| `brom_estado_frio` | `estado(frio)` | feliz | "Gelad{o/a}! Chega-te à fornalha. Não tanto. Aí. A forja é o melhor sítio da cidade para isso." |
| `brom_arma_nova` | arma equipada pela 1.ª vez com raridade Épica ou melhor | surpresa | "Que arma é ESSA? Dá cá. …Hmm. Quem a fez sabia. Quase tão bem como eu. Quase." |
| `brom_arma_sua` | arma equipada feita pelo herói na forja, qualidade Excelente | feliz | "Essa arma saiu desta bigorna. Reconheço o meu trabalho. E o teu. Mais o meu." |
| `brom_animal` | `animal != nenhum` (1.ª vez) | normal | "Um animal. Não o deixes lamber a bigorna. Da última vez um cão ficou com a língua colada." |
| `brom_comp_mia` | `companheiro(mia)` | feliz | "A miúda das flores, de arco na mão. Hmpf. Segura bem. Melhor do que tu seguravas." |
| `brom_comp_kai` | `companheiro(kai)` | normal | "Rapaz. A lâmina está boa? Não a partiste? Mostra. …Hmpf. Está boa." |
| `brom_comp_gorvan` | `companheiro(gorvan)` | surpresa | "Gorvan. A subir outra vez. Há vinte anos que não me pedes uma arma. …Deixa ver esse machado." |
| `brom_classe` | 1.ª conversa depois de escolher classe | normal | "{classe}, hã? Então as tuas armas vão mudar. Volta cá. As armas mudam e eu mudo-as." |
| `brom_treino_10` | `nivel >= 10` e a arma equipada ainda é a Espada de Treino | zangado | "Nível 10 com a Espada de Treino? Isso não é coragem. É teimosia. Traz cobre!" |

### A arma que trazes

Quando vens falar com o Brom com uma arma de **tipo diferente** da última vez que ele a viu, a 1.ª conversa do dia
é sobre ela (conta como fala de estado: 1 vez por dia). A condição é `arma_tipo == <tipo>` (ver `docs/ARMAS.md`, secção 1).

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `brom_arma_espada` | `arma_tipo == espada` | normal | "Espada. A arma de quem ainda não sabe o que quer. Bom. É a que ensina mais." |
| `brom_arma_espada_grande` | `arma_tipo == espada_grande` | feliz | "Espada grande! Isso pesa mais do que tu. Gosto. Bate devagar e com o corpo todo." |
| `brom_arma_adaga` | `arma_tipo == adaga` | zangado | "Adaga. Faca com ambições. Ataca pelas costas, que é para isso que serve. Não te gabes." |
| `brom_arma_katana` | `arma_tipo == katana` | surpresa | "Katana. Lâmina de um só fio, curva e fina. Difícil de forjar. Se a partires, choro. É fumo." |
| `brom_arma_machado` | `arma_tipo == machado` | feliz | "Um machado! Arma de anão. Corta inimigos e lenha. Duas utilidades. Respeito." |
| `brom_arma_martelo` | `arma_tipo == martelo` | feliz | "Um martelo. Pelas barbas do meu pai, finalmente uma arma a sério. Parte rochas e cabeças." |
| `brom_arma_lanca` | `arma_tipo == lanca` | normal | "Lança. Manténs o perigo longe. É sensato. Os sensatos vivem mais. Os anões nunca usam." |
| `brom_arma_foice` | `arma_tipo == foice` | zangado | "Uma foice? Para a guerra? O Zed usa uma igual para cortar erva aos bichos. Hmpf. Afia-se bem." |
| `brom_arma_arco` | `arma_tipo == arco` | zangado | "Arco. Madeira e fio. Quase nada de metal. Vens à forja porquê? …Para as pontas. Está bem." |
| `brom_arma_besta` | `arma_tipo == besta` | normal | "Besta. Isso sim, um arco com engenharia. Tem molas. As molas dão-me razão." |
| `brom_arma_cajado` | `arma_tipo == cajado` | normal | "Cajado. Um pau com uma pedra. Mas a pedra fui eu que encaixei. Por isso é um pau bom." |
| `brom_arma_manoplas` | `arma_tipo == manoplas` | feliz | "Manoplas! Bater com as mãos, como os antigos. Mostra os nós dos dedos. Hmpf. Ainda estão inteiros." |

### Serviço (a forja)

Falas da **Forja** (menu de serviço). O que cada serviço faz e quanto custa está em `docs/SISTEMAS.md`, secção 11,
e `docs/EQUIPAMENTO.md`, secção 8.

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `brom_serv_abrir` | abrir a forja | zangado | "Forjar, melhorar, encantar, reciclar. Escolhe. E não toques no martelo grande." |
| `brom_serv_abrir_2` | abrir a forja, 4+ ❤️ | normal | "Ah, és tu. Pousa a arma na bigorna. Devagar. Ela não te fez mal." |
| `brom_serv_forjar` | forjar com sucesso (qualidade Normal) | normal | "Feita. Lâmina direita, cabo firme. Não a uses para abrir latas." |
| `brom_serv_boa` | sai qualidade **Boa** | normal | "Boa. Saiu boa. Não te habitues." |
| `brom_serv_excelente` | sai qualidade **Excelente** | surpresa | "Excelente. …Olha para isto. OLHA. Hmpf. Não é choro. É orgulho. Que também faz fumo." |
| `brom_serv_ferramenta` | fazer uma picareta ou um machado de lenhador | normal | "Ferramenta nova. Não é arma. Não lhe batas com monstros. É melhor do que muitas armas, mas não é." |
| `brom_serv_melhoria_baixa` | melhoria **+1 a +5** | normal | "+{n}. Fácil. O ferro ainda não discute nesta altura." |
| `brom_serv_melhoria_alta` | melhoria **+6 a +9** com sucesso | feliz | "+{n}! Entrou. O ferro resmungou e eu resmunguei mais alto. Ganhei." |
| `brom_serv_falhou` | melhoria falhada | zangado | "Falhou. A arma está inteira, os lingotes é que foram. O ferro hoje não quis." |
| `brom_serv_falhou_2` | 2.ª falha seguida ou mais (+5% na próxima) | normal | "Outra vez não. Mas o ferro já está cansado de me dizer que não. Na próxima entra. Sinto-o na barba." |
| `brom_serv_mais10` | melhoria **+10** com sucesso | surpresa | "+10. MAIS DEZ. Faz silêncio. Ouve como soa. Em cento e quarenta anos fiz poucas destas." |
| `brom_serv_mais10_2` | (continua) | triste | "…Não é choro. É fumo da forja. Muito fumo. Vai-te embora antes que o fumo piore." |
| `brom_serv_encantar` | encaixar uma gema | normal | "{gema} na arma. Agora ela tem feitio. Cada pedra tem o seu. Como as pessoas." |
| `brom_serv_rubi` | encaixar um **Rubi** | feliz | "Rubi. Fogo. A pedra dos Brasa. Esta arma vai aquecer-te as mãos no inverno." |
| `brom_serv_tirar_gema` | tirar uma gema (100 ouro) | zangado | "Tirar a gema? Cem moedas. A gema sai inteira. A minha paciência, não." |
| `brom_serv_reciclar` | reciclar uma arma ou armadura | triste | "Desfazer uma arma dói-me sempre. Toma, metade do que tinha. A outra metade foi para o céu das armas." |
| `brom_serv_objeto` | entregar-lhe um **objeto partido de uma missão** (só nas missões que o pedem; as armas nunca se partem) | normal | "Isto não é uma arma. É uma história partida. Dá cá. Com cuidado. As histórias também se soldam." |
| `brom_serv_sem_materiais` | faltam materiais | zangado | "Sem lingotes não há arma. Sou ferreiro, não sou mágico. Mágica é a Selene. E nem ela." |
| `brom_serv_sem_ouro` | falta ouro | zangado | "Não tens ouro que chegue. O carvão não é de graça. O meu tempo também não." |
| `brom_serv_fechado` | falar com ele na Taberna (19:00–23:00) | normal | "A forja está fechada. Eu estou na taberna. Vês a diferença? Eu vejo. Amanhã às seis." |
| `brom_serv_fechado_domingo` | Domingo | zangado | "Domingo. A forja dorme. A tua arma que espere. O ferro não tem pressa." |
| `brom_serv_desconto` | 1.ª compra depois da cena de 2 ❤️ | normal | "Faço-te desconto. Não é por gostar de ti. É porque não me estragas as armas. Muito." |
| `brom_serv_pedrito` | melhoria +1 a +5 com o Pedrito na forja (R2_13) | feliz | "O Pedrito faz as pequenas, até +5. Eu fico a ver e a resmungar. Agora é esse o meu trabalho." |
| `brom_serv_forja_ana` | 1.ª melhoria depois de R2_05 | triste | "Três batidas. Uma pelo ferro, uma pelo fogo, uma por ti. …Pronto. Agora sim." |
| `brom_serv_mitica` | toque final numa arma mítica (R10_11) | surpresa | "O toque final? Pousa. …Esta arma é maior do que eu. Mas vai sair daqui com o meu martelo nela." |
| `brom_serv_adeus` | sair da forja | normal | "Vai. E volta com ela inteira." |
