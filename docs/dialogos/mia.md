# Mia — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.8. Dados: `dados/dialogos/mia.json`.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | agudos, curtos e saltitantes; sobem muito quando está entusiasmada |
| Como fala | depressa e aos solavancos; exagera tudo e dá nomes grandiosos às coisas ("navio de guerra", "Golpe do Dragão Furioso"); faz perguntas atrás de perguntas; ofende-se num segundo e esquece no seguinte |
| Repete | "Um dia…", "Não sou pequena!", "A sério a sério?", "Eu sei!", "Os aventureiros não desistem!" |
| Tiques | aponta o pau (ou o arco) como se fosse uma espada (animação `apontar_pau`); enche as bochechas quando está zangada |
| Nunca diz | "não consigo"; "tenho medo" (até aos 8 ❤️); nunca chora à frente de ninguém (vira-se de costas) |
| Chama ao herói | `{nome}` · depois de N_MIA_2: "{Mestre/Mestra}" (a brincar, mas a sério) · com 10 ❤️: "colega" |
| **Regra de ouro** | **Escolhas que a tratam como criança: −30 de amizade. Escolhas que a tratam como igual: +30.** Muitas falas desta página têm escolhas ▶ (ver `docs/SISTEMAS.md`, secção 15) |
| Rotina | esquina do Bairro Baixo a vender flores (7:00–13:00) · Praça a "treinar" (14:00–18:00) · Igreja da Luz (19:00: janta e dorme lá; a Irmã Célia cuida dela) |
| Rotina ao Domingo | de manhã põe flores no altar da Igreja; à tarde (14:00–18:00) está no rio a lançar barquinhos de papel |

---

## 2. Primeira conversa

Depois da cena P6 (prólogo), a 1.ª vez que carregas em **Conversar**:

- **Mia** *(surpresa)*: "És tu! O Jogador nº 10 000! A cidade inteira ouviu a Lyra gritar 'DEZ MIL'!"
- 🎬 Aponta o pau ao herói, como se fosse uma espada.
- **Mia** *(feliz)*: "Eu sou a Mia. Aventureira. Bem… quase. Falta-me o registo. E uma espada. E o resto."
- **Mia** *(normal)*: "Também vendo flores. Mas é só até ficar rica com tesouros."

▶ **"Quantos anos tens?"**
▶ **"Prazer, colega."**
▶ **"Vendes-me uma flor?"**

- *(anos)* **Mia** *(zangado)*: "Onze. E três quartos. A idade não interessa! O Kai tem dezassete e ontem caiu num buraco!" ⚙ −30
- *(colega)* **Mia** *(surpresa → feliz)*: "COLEGA! Ouviste isto, Bairro Baixo? Colega!" ⚙ +30
- *(flor)* **Mia** *(feliz)*: "Sim! Quer dizer… a loja é muito profissional. Escolhe com calma. Mas depressa."
- **Mia** *(normal)*: "Um dia vou subir mais alto do que tu. Aviso já, para não ficares triste depois."

⚙ Abre o menu da Mia: **Flores (loja) · Perguntar sobre… · Dar presente**

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `mia_dia_01` | `hora entre 7 e 10` | feliz | "Flores fresquinhas! Apanhei-as antes do sol. O sol é preguiçoso." |
| `mia_dia_02` | `hora entre 10 e 13` | normal | "Hoje vendi três flores. Uma foi ao Pip. Adormeceu a meio de pagar." |
| `mia_dia_03` | `hora entre 12 e 14` | normal | "Almoço? Tenho meia maçã. A outra metade foi para treinar pontaria." |
| `mia_dia_04` | `hora entre 14 e 18` | feliz | "Estou a treinar! Não me distraias! …Pronto, distrai-me um bocadinho." |
| `mia_dia_05` | `hora entre 14 e 18` | feliz | "Viste o meu golpe? O Golpe do Dragão Furioso!" ▶ **"Que fofo!"** ⚙ −30 → *(zangado)* "FOFO?! Os dragões não são fofos!" · ▶ **"Roda mais a anca."** ⚙ +30 → "A anca! Claro! …Onde é a anca?" |
| `mia_dia_06` | `hora entre 18 e 20` | triste | "A Irmã Célia já me chamou para jantar. Os aventureiros a sério jantam quando querem." |
| `mia_dia_07` | `hora entre 20 e 23` | normal | "Devia estar a dormir. Estou a fingir. Sou muito boa a fingir que durmo." |
| `mia_dia_08` | — | feliz | "Um dia vou subir mais alto do que tu!" |
| `mia_dia_09` | — | zangado | "Não sou pequena. Sou… compacta." |
| `mia_dia_10` | — | normal | "Sabias que a Praça tem trezentos e doze passos? Dos meus. Dos teus tem menos. Batoteir{o/a}." |
| `mia_dia_11` | — | feliz | "Ontem lutei com um gato. Empatámos. Ele ficou com o meu pão. Eu fiquei com a dignidade." |
| `mia_dia_12` | — | normal | "Achas que eu já podia ir à torre?" ▶ **"És muito nova."** ⚙ −30 → *(zangado)* "Toda a gente diz isso. Toda a gente é chata." · ▶ **"Ainda não. Falta treino."** ⚙ +30 → *(feliz)* "Falta TREINO. Não falta idade. Ouviste? Treino!" |
| `mia_dia_13` | — | zangado | "O Rook diz que as crianças não podem andar nos telhados. Ele anda nos telhados! Todas as noites!" |
| `mia_dia_14` | `dia_semana == domingo` | feliz | "Pus flores no altar. A Irmã Célia diz que a luz gosta de flores. Acho que é ela que gosta." |
| `mia_dia_15` | `dia_semana == domingo && hora entre 14 e 18` | feliz | "Estou a lançar barcos no rio! Este é o Destemido. O que se afundou era o Destemido Dois." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `mia_dia_20` | `estacao == primavera` | feliz | "Primavera! As flores crescem sozinhas e eu fico rica. Quase rica. Menos pobre." |
| `mia_dia_21` | `estacao == primavera && hora entre 7 e 13` | normal | "Os aventureiros novos compram flores para a Lyra. Ela tem a secretária cheia. Eu tenho o bolso cheio." |
| `mia_dia_22` | `estacao == verao` | normal | "Com este calor as flores murcham. Eu não murcho. Os aventureiros não murcham." |
| `mia_dia_23` | `estacao == verao && hora entre 18 e 20` | feliz | "Ao fim do dia a torre fica cor-de-laranja. Parece que tem uma vela acesa lá em cima." |
| `mia_dia_24` | `estacao == outono` | normal | "No outono há poucas flores. Vendo folhas bonitas. Ninguém compra folhas. O Tobias diz que é 'má estratégia'." |
| `mia_dia_25` | `estacao == outono && clima == nevoeiro` | feliz | "Nevoeiro! Ótimo para treinar emboscadas. Já emboscei três pombos." |
| `mia_dia_26` | `estacao == inverno` | normal | "No inverno não há flores. Faço-as de papel. A Lyra dá-me os formulários velhos. Não digas ao Mestre Gorvan." |
| `mia_dia_27` | `estacao == inverno && clima == neve` | feliz | "Fiz um boneco de neve aventureiro! Tem um pau e uma fita. É igual a mim, mas mais alto. Por enquanto." |
| `mia_dia_28` | `clima == chuva` | zangado | "As flores ficam pesadas e eu fico molhada. Os heróis não se queixam. Eu estou a queixar-me um bocadinho." |
| `mia_dia_29` | `clima == trovoada` | normal | "Os trovões não me metem medo. Só me escondo debaixo da mesa para… treinar esconderijos." |
| `mia_dia_30` | `clima == nevoeiro` | normal | "Com nevoeiro ninguém me vê treinar. Assim ninguém se ri. Não que se riam. Riem-se." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `mia_dia_40` | `andar_maximo < 5` | feliz | "Já foste ao andar 1? Há coelhos? Coelhos grandes? Do tamanho de quê? De mim?" |
| `mia_dia_41` | `missao(N_LYRA_1) == concluida` | zangado | "Ainda estou chateada por ter devolvido o meu navio de guerra. Era o melhor barco da frota. Era o único." |
| `mia_dia_42` | `boss_derrotado(javali_rei) && andar_maximo < 11` | feliz | "Venceste um javali REI! Eu venci um pombo rei. Era o mais gordo." |
| `mia_dia_43` | `boss_derrotado(ent_anciao)` | normal | "Viste a Árvore-Mãe? O que é que ela disse?" ▶ **"É uma história triste."** ⚙ +30 → "Eu aguento histórias tristes. Sou aventureira." · ▶ **"Não é para crianças."** ⚙ −30 → *(zangado)* "Então porque é que TU a ouviste?" |
| `mia_dia_44` | `flag(sssar_defendida)` | feliz | "Defendeste os homens-lagarto! A Lyra diz que são verdes e simpáticos. Eu quero um amigo verde." |
| `mia_dia_45` | `andar_maximo >= 44` | normal | "Dizem que o Yeti guarda brinquedos. Brinquedos não me interessam." 🎬 Pausa. "Que tipo de brinquedos?" |
| `mia_dia_46` | `boss_derrotado(dragao_gelo)` | feliz | "Eu disse a toda a gente que tu ias vencer um dragão! Ganhei duas maçãs em apostas." |
| `mia_dia_47` | `andar_maximo >= 53 && !flag(kai_salvo) && !boss_derrotado(kai)` | triste | "O Kai deixou de passar na Praça. Às vezes ensinava-me golpes. Golpes maus. Mas golpes." |
| `mia_dia_48` | `flag(kai_salvo) && flag(mia_arqueira)` | feliz | "O Kai disse que eu tenho pose de espadachim. Eu disse-lhe que agora sou arqueira. Ficou confuso." |
| `mia_dia_49` | `missao(H_19) == concluida` | feliz | "O Mestre Gorvan sorriu para mim hoje! Acho. Pode ter sido o vento. Mas acho que sorriu." |
| `mia_dia_50` | `andar_maximo >= 81` | feliz | "Estás nas nuvens! Se me trouxeres uma nuvem, guardo-a num frasco. Prometo que lhe dou água." |
| `mia_dia_51` | `andar_maximo >= 91` | normal | "Quando chegares ao topo, acenas cá para baixo? Eu fico na Praça a olhar. Com os olhos todos." |
| `mia_dia_52` | `rank >= C` | feliz | "Rank C! Quando eu for rank C compro um chapéu. Os rank C têm todos chapéu? Deviam." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `mia_dia_60` | `coracoes(mia) >= 2` | feliz | "{nome}! Guardei-te a flor mais bonita. Não é de graça. É com desconto de amig{o/a}." |
| `mia_dia_61` | `coracoes(mia) >= 3` | feliz | "Contas-me uma história da torre? Assustadora!" ▶ **"Vais ter pesadelos."** ⚙ −30 → "Os pesadelos é que têm medo de mim." · ▶ **(contar a do Javali-Rei)** ⚙ +30 → "E depois?! E DEPOIS?!" |
| `mia_dia_62` | `coracoes(mia) >= 4` | normal | "Hoje dei uma flor de graça à Dona Marta. Os aventureiros também fazem coisas sem ganhar nada. Às vezes." |
| `mia_dia_63` | `coracoes(mia) >= 5` | feliz | "Escrevi o teu nome no meu caderno de heróis. Estás em segundo. Eu estou em primeiro. O caderno é meu." |
| `mia_dia_64` | `coracoes(mia) >= 6` | triste | "Quando sobes, fico a olhar para a torre até a Irmã Célia me chamar. Não é medo. É… vigilância." |
| `mia_dia_65` | `coracoes(mia) >= 8` | feliz | "Sabes o que vou ser quando for grande? Tu. Mas com fita." |
| `mia_dia_66` | `coracoes(mia) >= 10` | feliz | "Colega de equipa! Já desenhei o nosso estandarte. Num guardanapo. Está um bocadinho sujo de sopa." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `mia_dia_70` | `origem == jogador` | feliz | "No teu mundo havia jogos de aventureiros? E tu eras bom? …Eras bom, não eras?" |
| `mia_dia_71` | `origem == atrasado` | feliz | "Chegas sempre a correr! Estás a treinar velocidade? Ensina-me!" |
| `mia_dia_72` | `origem == ajudante` | normal | "A Dona Marta diz que ajudas toda a gente. Ajudas-me a crescer? …Era uma piada. Meia piada." |
| `mia_dia_73` | `origem == dormir` | normal | "No teu mundo dormias muito? Eu aqui durmo pouco. Há muito para fazer. E a Irmã Célia ressona." |
| `mia_dia_74` | `skill_unica == lingua_universal` | feliz | "Falas com monstros?! Pergunta a um coelho-chifre se tem medo de mim. Diz que sim, está bem?" |
| `mia_dia_75` | `skill_unica == sorte_do_heroi` | feliz | "Tens sorte? Toca no meu cesto. Para vender mais. …Não resultou. Toca outra vez." |
| `mia_dia_76` | `skill_unica == domador_nato` | normal | "Os animais gostam de ti? Os gatos do Bairro Baixo arranham-me. Ensinas-me a ser tu?" |
| `mia_dia_77` | `skill_unica == passo_fantasma` | zangado | "Esquivas duas vezes seguidas? Isso é batota! Eu também quero batota!" |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `mia_curta_1` | feliz | "Estou a treinar! Volta depois!" |
| `mia_curta_2` | normal | "Já compraste flores hoje? Compra mais. Para amanhã." |
| `mia_curta_3` | feliz | "Olá outra vez! Ainda sou a Mia. Ainda sou aventureira." |
| `mia_curta_4` | zangado | "Shh! Estou numa missão secreta. …Ver se o pombo volta." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Mia** *(feliz)*: "A torre? É o sítio mais bonito do mundo. E o mais perigoso. As duas coisas ao mesmo tempo. Como o Mestre Gorvan."
- **Mia** *(normal)*: "Os miúdos do Bairro Baixo dizem que no topo há um dragão a dormir em cima de ouro. Eu acho que há uma janela."
- **Mia** *(normal)*: "Uma janela de onde se vê tudo. Toda a gente. Até as pessoas que eu não conheço."

### 4.2 O andar atual

A Mia nunca lá foi: fala da **região do andar mais alto** a que chegaste com perguntas e sonhos.

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta! Há coelhos com chifres? Quero um. Para montar. Não? Para ser meu amigo, então." |
| 2 Cavernas | "Cavernas escuras… Eu não tenho medo do escuro. Durmo de vela acesa por causa da… leitura." |
| 3 Pântano | "Há sapos gigantes? Se lhes deres um beijo viram príncipes? O Lucien diz que sim. O Lucien diz muita coisa." |
| 4 Deserto | "Areia por todo o lado! Faz-me um castelo lá em cima. Um a sério. Com múmias." |
| 5 Gelo | "Neve que nunca acaba? Eu fazia o maior boneco de neve do mundo. E depois um exército de bonecos." |
| 6 Oceano | "Andares debaixo de água! Viste sereias? São bonitas? Mais bonitas do que eu? Não respondas." |
| 7 Vulcão | "Lava! É como sopa de fogo? Trazes-me uma pedra de lava? Fria. Fria é melhor." |
| 8 Reino Assombrado | "Fantasmas! Não tenho medo de fantasmas. A Irmã Célia diz que são só pessoas tristes." |
| 9 Céu | "Ilhas no céu! Se eu saltar de lá, voo? Nem um bocadinho? Que torre tão mal feita." |
| 10 Abismo | "O fundo lá de cima? Isso nem faz sentido. Escreve-me tudo. Eu leio devagar. Já leio quase tudo." |

### 4.3 Rumores

"Os miúdos do Bairro Baixo veem tudo. Ninguém olha para os miúdos." A Mia diz **1 rumor por dia**.

| ID | Condição | Rumor |
|---|---|---|
| `mia_rumor_01` | — | "O Rook deixa pão à porta da Igreja todas as noites. Diz que não é ele. É ele. Tem migalhas no capuz." |
| `mia_rumor_02` | — | "O Mestre Gorvan diz que detesta doces. Mas compra um saco na Noite dos Espíritos. São para nós." |
| `mia_rumor_03` | — | "O Brom canta na forja quando acha que está sozinho. Canta sobre uma montanha. Desafinado. Bonito." |
| `mia_rumor_04` | — | "Há um gato preto que dorme na pedra mais alta da muralha. Chama-se Sargento. Fui eu que lhe dei o nome." |
| `mia_rumor_05` | `andar_maximo >= 1` | "O Tibério, na Zona Segura do andar 1, vende doces mais baratos do que o Tobias. Não digas ao Tobias." |
| `mia_rumor_06` | `andar_maximo >= 2` | "No andar 2 há uma rapariga que quer ser alquimista. A Tina. Podíamos ser equipa. Ela explode coisas, eu corto-as." |
| `mia_rumor_07` | — | "O Gizmo tem uma torradeira com pernas. Ela foge. Já a apanhei duas vezes. Deu-me um parafuso de recompensa." |
| `mia_rumor_08` | `missao(R2_13) == concluida` | "O Pedrito é aprendiz do Brom! Tem um avental! Eu também quero um avental. Mas de aventureira." |
| `mia_rumor_09` | `andar_maximo >= 45` | "Um aventureiro disse que o Yeti do 45 tinha uma boneca. Uma boneca que esteve numa gruta de YETI. Isso é um tesouro." |
| `mia_rumor_10` | `estacao == primavera` | "Vem aí a Festa das Flores! Tenho uma flor secreta para o concurso. Está tão escondida que nem eu a encontro." |
| `mia_rumor_11` | `missao(N_LYRA_1) == concluida` | "Agora faço barcos com os formulários velhos da Lyra. Ela é que mos dá. Diz que assim 'pelo menos navegam'." |
| `mia_rumor_12` | `missao(N_MIA_2) == concluida` | "O Mestre Gorvan às vezes fica a ver-me treinar. Finge que está a ver os pombos. Os pombos estão do outro lado." |

### 4.4 A vida dela

| Corações | Fala |
|---|---|
| 0 | "Eu? Sou a Mia. Vendo flores e vou ser aventureira. É só isso. Por enquanto." |
| 2 | "Durmo na Igreja. A Irmã Célia deixa-me ter a cama ao pé da janela. Para ver a torre antes de adormecer." |
| 4 | "Não conheço os meus pais. A Irmã Célia encontrou-me à porta da Igreja, num cesto de flores. Por isso vendo flores." 🎬 Pausa. "Mentira. Vendo flores porque dá dinheiro. Mas o cesto é verdade." |
| 6 | "Às vezes invento os meus pais. Hoje são aventureiros rank S. Ontem eram piratas. Amanhã ainda não decidi." |
| 8 | "Vou contar-te uma coisa. Só a ti. Tenho medo da torre. Muito." 🎬 Pausa. "Mas vou na mesma. O medo é uma coisa que se sente. Não é uma coisa que se é." |
| 10 | "Quando for rank S, escrevo o meu nome no quadro grande da Guilda. Se os meus pais o virem, sabem que sou eu. Se não virem… eu sei que sou eu." |

---

## 5. Presentes

**Adora:** armas pequenas (adagas, arcos curtos), coisas da torre com história (troféus de bosses e de monstros com nome),
**Boneca do Yeti** (andar 45) · **Gosta:** doces, flores · **Detesta:** brinquedos de bebé (dar-lhos é tratá-la como criança),
lixo de pesca, Ectoplasma. **Exceção:** o Gel de Slime, que quase todos detestam, para a Mia é **neutro**.
O resto é **neutro** (ver `docs/ITENS.md`, secção 11).

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "ISTO É PARA MIM?! A sério a sério? Vou dormir com isto debaixo da almofada. Com a mão em cima." · "É a melhor coisa que alguém me deu. Desde sempre. E sempre é muito tempo." |
| Gosta | "Obrigada! Vou comer devagar. Não, vou comer já. Devagar é para velhos." · "Que bonito! Vou pôr no cesto. Não é para vender! É para mostrar." |
| Neutro | "Hmm. Obrigada. Serve para quê? …Vou descobrir." · "Está bem! Fica na minha caixa das coisas. É uma caixa importante." |
| Não gosta | "Ah… obrigada. Vou dar à Irmã Célia. Ela gosta de coisas… destas." |
| Detesta | "Um brinquedo de bebé. Obrigadinha." 🎬 Enche as bochechas. · "Isso cheira a rio podre! Tira isso de ao pé das flores!" |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Boneca do Yeti | "Uma boneca que esteve na gruta do YETI?! Isto não é um brinquedo. É um tesouro de guerra. Vai dormir comigo. Para eu a proteger." |
| Adaga (qualquer) | "Uma adaga a sério! A Irmã Célia vai tirar-ma. Vou escondê-la muito bem. …Na tua casa." |
| Troféu (qualquer) | "Isto é… {item}? A SÉRIO? Conta-me tudo. Desde o início. Não saltes partes." |
| Pato de Madeira | "Um pato de madeira. Para bebés. Obrigadinha." 🎬 Pausa. "…Vou dá-lo à Lyra. Ela tem medo de patos. Vai ser ótimo." |
| Gel de Slime | "Gel de slime! Toda a gente detesta. Eu não. Vou pô-lo na cama do Rook." |
| Flor de Mel | "Uma Flor de Mel! Esta não a vendo. Esta é para mim. Às vezes também mereço flores." |
| Ramo do Campo (comprado a ela) | "Estás a dar-me uma flor que me compraste a mim? Então ganhei duas vezes. Isto é genial." |
| Doce (qualquer) | "Doce! Obrigada! Não contes à Irmã Célia. Ela conta-me os dentes." |
| Coroa de Flores | "Uma coroa! Agora sou rainha das flores. Rainha aventureira. Isso existe? Agora existe." |

---

## 6. Aniversário e festivais

**Aniversário (Primavera, dia 27):**
- Sem presente: **Mia** *(feliz)*: "Hoje faço anos! Sou oficialmente mais velha do que ontem. Muito mais. Um dia inteiro."
- Com presente que adora: **Mia** *(surpresa)*: "Lembraste-te dos meus anos?! Ninguém se lembra, só a Irmã Célia! E agora tu! São DOIS!"
- Com outro presente: **Mia** *(feliz)*: "Um presente de anos! Vou abri-lo devagar. …Não consegui. Já abri."
- 🎬 Com 6+ ❤️, a Mia convida-te: "Vens à Igreja às sete? A Irmã Célia faz um bolo. É pequeno. Corta-se em fatias muito finas."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "O meu dia! Vendi o cesto todo antes das dez! Agora vou ganhar o concurso. Ou ficar em segundo. Atrás da Hana." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Mia** *(surpresa)*: "Eu? Não sei dançar. Sei lutar. É parecido?" ⚙ dança · +100 amizade (a Mia dança como quem luta) |
| F_02 Festival da Pesca | "O Pip emprestou-me uma cana. Pesquei uma bota. A bota era do Pip." |
| F_03 Noite dos Espíritos | "Vou mascarada de Mestre Gorvan! Um braço dentro da camisola e digo 'Hmm.' a toda a gente." |
| F_04 Festival da Estrela | "Amigo secreto! Calhou-me o Brom. Fiz-lhe uma flor de ferro. De papel pintado de cinzento. Ele vai chorar. Fumo." |
| F_05 Dia da Subida | "Quando subires mais, vais ter uma estátua? Posso pôr uma flor na tua estátua? Todos os dias?" |
| F_06 Concurso da Casa | "Se a tua casa ganhar, é porque eu dei ideias. Põe flores. Muitas. Compradas a mim." |
| F_07 Noite das Lanternas (depois da cena 4 da Lyra) | "Ponho uma lanterna pelos meus pais. Não sei se subiram. Mas, se subiram, já está." (com 6+ ❤️: "Pões a tua ao pé da minha?" ⚙ +30) |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`).

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `mia_boss_javali_rei` | "Um javali REI! Tinha coroa? De raízes? Isso conta como coroa! Trazes-me um bocadinho?" |
| Ent Ancião (10) | `mia_boss_ent_anciao` | "Venceste uma árvore que anda! Eu ontem venci uma árvore que não anda. Subi-a toda." |
| Aranha-Mãe (15) | `mia_boss_aranha_mae` | "Uma aranha do tamanho de uma carroça! Eu não tinha medo. Tinha… respeito. Muito respeito." |
| Golem de Cristal (20) | `mia_boss_golem_cristal` | "Um gigante de cristal! Ficou em bocadinhos? Trouxeste um? Pequenino? Muito pequenino?" |
| Serpente do Lodo (25) | `mia_boss_serpente_lodo` | "Uma cobra de lama! Cheiras mesmo a pântano. Não faz mal. Os heróis cheiram a aventura." |
| Hidra do Pântano (30) | `mia_boss_hidra_pantano` | "Quantas cabeças? Cortaste todas? Elas cresceram outra vez? Isso é batota de monstro!" |
| Escorpião Imperador (35) | `mia_boss_escorpiao_imperador` | "Um escorpião imperador. Tinha capa? Os imperadores têm capa. Sem capa era só um escorpião grande." |
| Faraó Eterno (40) | `mia_boss_farao_eterno` | "Uma múmia! Andava assim?" 🎬 Anda de braços esticados. "Eu sabia!" |
| Yeti Ancião (45) | `mia_boss_yeti_anciao` | "Venceste o Yeti! E os brinquedos dele? Ficaram lá sozinhos? Coitados dos brinquedos." |
| Dragão de Gelo (50) | `mia_boss_dragao_gelo` | "UM DRAGÃO. Eu disse. Eu DISSE. Ninguém acreditou! Agora devem-me maçãs. Muitas maçãs." |
| Capitão Esqueleto (55) | `mia_boss_capitao_esqueleto` | "Piratas esqueletos! Tinham papagaios esqueletos? Diz que sim. Por favor." |
| Leviatã (60) | `mia_boss_leviata` | "Venceste o monstro do mar… mas o Kai ainda não voltou. Quando voltar, vence-o também. Por ter fugido." |
| Ferreiro Infernal (65) | `mia_boss_ferreiro_infernal` | "O Brom estava a chorar na forja. Disse que era fumo. Dei-lhe uma flor. Chorou mais. Era muito fumo." |
| Kai — salvo (68) | `mia_boss_kai_salvo` | "O Kai voltou! Fez-me uma festa na cabeça. Detesto festas na cabeça. Desta vez deixei." |
| Kai — vencido (68) | `mia_boss_kai_vencido` | "A Lyra disse para não te fazer perguntas. Não faço. Toma. É uma flor. É de graça. Só hoje." |
| Titã de Magma (70) | `mia_boss_tita_magma` | "Um gigante de lava! Trouxeste-me a pedra de lava? Fria? Não faz mal. Para a próxima." |
| Lich Bibliotecário (75) | `mia_boss_lich_bibliotecario` | "Um esqueleto que lia livros! O Velho Fausto ficou com inveja. Disse que não. Mas ficou." |
| Rei Sem Coroa (80) | `mia_boss_rei_sem_coroa` | "O Mestre Gorvan está a treinar no campo! À frente de toda a gente! Fui ver. Ele disse 'Hmm.' Com orgulho." |
| Grifo Real (85) | `mia_boss_grifo_real` | "Meio leão, meio águia! Posso ter um? Meio grifo? Um bocadinho de grifo?" |
| Serafim Caído (90) | `mia_boss_serafim_caido` | "Estás triste. Não precisas de dizer porquê. Os aventureiros também ficam tristes. Eu sei. Vi-te." |
| Guardião do Tempo (95) | `mia_boss_guardiao_tempo` | "Andar 95! Já não há ninguém para te passar à frente. Só eu. Daqui a uns anos. Espera por mim." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — O Golpe do Dragão Furioso

| | |
|---|---|
| ID | `cena_mia_2` |
| Quando | 2 ❤️ · passar pela Praça entre as 14:00 e as 18:00, sem chuva |
| Onde | Praça da Torre, ao pé da fonte |
| Quem | herói, Mia, duas crianças do Bairro Baixo |
| Música | `ascendia_dia` |

🎬 A Mia "luta" contra um saco de palha pendurado num candeeiro. Duas crianças estão a ver, a rir.

- **Mia** *(zangado)*: "GOLPE DO DRAGÃO FURIOSO!"
- 🎬 Roda o pau, roda o corpo, roda demais e cai sentada. As crianças riem-se.
- **Criança**: "A Mia caiu outra vez! A aventureira caiu!"
- **Mia** *(zangado)*: "Foi de propósito! É uma técnica! Chama-se… Queda do Dragão!"
- 🎬 As crianças fogem a rir. A Mia vê o herói e fica vermelha até às orelhas.
- **Mia** *(surpresa)*: "Viste isso? Não viste. Ninguém viu."

▶ **"Que golpe tão giro!"**
▶ **"Os pés estão mal. Abre-os mais."**
▶ **"Não devias brincar com paus."**

- *(giro)* **Mia** *(zangado)*: "GIRO?! Não é giro. É MORTAL. Os dragões não são giros!" ⚙ −30
- *(pés)* **Mia** *(surpresa)*: "Os pés? …Assim?" 🎬 Abre os pés e roda outra vez. Não cai. "ASSIM! Porque é que ninguém me disse isto antes?" ⚙ +30
- *(paus)* **Mia** *(zangado)*: "Não é brincar! É treinar! Os adultos dizem sempre isso!" ⚙ −30
- **Mia** *(normal)*: "Treino todos os dias. Desde os sete anos. Com este pau. Chama-se Relâmpago."
- **Mia** *(triste)*: "Toda a gente se ri. Mas um dia vão ver."
- 🎬 Um pombo pousa em cima do saco de palha. Sem olhar, a Mia apanha uma pedra e atira-a. Acerta no nó da corda. O saco cai. O pombo foge.
- **Mia** *(normal)*: "Isso? Isso não conta. Pedras não são armas de aventureiros."

▶ **"Pois eu acho que conta."**
▶ *(não dizer nada)*

- *(conta)* **Mia** *(surpresa)*: "…Achas? Hmm. Vou pensar nisso. Mas não muito." ⚙ +30
- *(nada)* **Mia** *(normal)*: "Amanhã há mais treino. Se quiseres ver, vê. Mas não te rias."

⚙ As flores da Mia ficam 5% mais baratas. Missão **N_MIA_1 Primeira Espada** disponível.

### ❤️ 4 — Ensina-me

| | |
|---|---|
| ID | `cena_mia_4` |
| Quando | 4 ❤️ · `missao(N_MIA_1) == concluida` · passar pela esquina do Bairro Baixo entre as 7:00 e as 13:00 |
| Onde | esquina do Bairro Baixo |
| Quem | herói, Mia, Irmã Célia (no fim) |
| Música | `amizade` |

🎬 O cesto das flores está fechado. Em cima dele, a Espada Pequena embrulhada num pano, como um tesouro. A Mia estava à espera.

- **Mia** *(normal)*: "Fechei a loja mais cedo. Isto é importante. Mais importante do que dinheiro. Quase."
- **Mia** *(normal)*: "Tenho espada. Tenho vontade. Tenho um pau de reserva. Falta-me uma coisa."
- 🎬 Endireita-se toda e faz uma vénia muito séria, como os cavaleiros dos livros.
- **Mia** *(normal)*: "{nome}. Ensinas-me a lutar? A sério. Não a brincar. Não 'para eu me calar'."

▶ **"Ensino. Mas a sério."**
▶ **"És muito nova para isso."**
▶ **"Porque é que queres tanto subir?"**

- *(a sério)* **Mia** *(feliz)*: "A SÉRIO! Prometo treinar todos os dias! E não me queixar! Quase nada!" ⚙ +30
- *(nova)* **Mia** *(zangado)*: "O Kai subiu com dezassete. Eu tenho onze. São só seis anos!" ⚙ −30
  **Mia** *(triste)*: "Se não me ensinares, aprendo sozinha. E aprendo mal. É pior." → ▶ **"Está bem. Ensino."**
- *(porquê)* **Mia** *(normal)*: "Porque lá em cima ninguém sabe que eu sou pequena. Só sabem se és forte." 🎬 Pausa. "E porque alguém tem de ver o topo. Pode ser eu." ⚙ +30
- 🎬 A Irmã Célia aparece ao fundo da rua, de braços cruzados.
- **Irmã Célia** *(normal)*: "Mia. Treinos na Praça, à vista de todos. E à hora do jantar estás em casa."
- **Mia** *(feliz)*: "Ela disse que sim! Aquilo foi um sim!"
- 🎬 A Mia tira a fita amarela do cabelo. Tenta cortá-la com a Espada Pequena. A espada não tem fio. Corta-a com os dentes.
- **Mia** *(feliz)*: "Toma. Metade da minha fita. Agora somos da mesma equipa. A equipa ainda não tem nome. Vou pensar."

⚙ Missão **N_MIA_2 Treino** iniciada. Recebe a **Fita Amarela** (acessório cosmético: usa-se no pulso ou atada à arma).

### ❤️ 6 — Passageira não registada

| | |
|---|---|
| ID | `cena_mia_6` |
| Quando | 6 ❤️ · `missao(N_MIA_2) == concluida` · tocar no Cristal Mestre entre as 6:00 e as 18:00 |
| Onde | Praça da Torre → andar 1, Zona Segura |
| Quem | herói, Mia, Tibério |
| Música | `ascendia_dia` → `floresta_perigo` |

🎬 O herói toca no Cristal Mestre. Antes do flash, uma mão pequena agarra-se à alça da mochila.
🎥 Flash azul. A imagem treme (efeito de falha, 1 s).

- `[Sistema] Passageiro não registado detetado.`
- `[Sistema] A redirecionar para o andar 1.`

🎬 O herói e a Mia caem na erva da Zona Segura do andar 1. A Mia levanta-se primeiro, com o arco pequeno às costas.

- **Mia** *(feliz)*: "RESULTOU! Bem… mais ou menos. Eu queria ir ao andar onde tu ias. Mas este também serve!"
- **Mia** *(normal)*: "Não te zangues. Fiz os cinco treinos. Tu disseste que eu estava quase pronta."

▶ **"Eu disse 'quase'."**
▶ **"Volta já para o cristal!"**

- *(quase)* **Mia** *(feliz)*: "'Quase' é quase 'sim'!"
- *(volta)* **Mia** *(zangado)*: "Não! Os aventureiros não voltam para trás no primeiro passo!"
- 🎬 Ouve-se um uivo ao longe. A Mia olha para o herói, depois para a erva alta.
- **Mia** *(feliz, nervosa)*: "Vou só ver o que é! Um minuto! Uma aventureira tem de ver as coisas!"
- 🎬 Corre para a erva alta antes que o herói a apanhe. A fita amarela desaparece entre as ervas.
- **Tibério** *(normal, da banca)*: "Era tua irmã? Corre como o meu irmão quando há contas para pagar."
- `[Sistema] Uma alcateia de Lobos Cinzentos desceu do andar 2. Encontra a Mia antes deles.`

⚙ Missão **N_MIA_3 A Fuga** começa logo. A partir daqui a Mia aceita jantar em tua casa (a Irmã Célia deixa, "até às oito").

### ❤️ 8 — Testemunha

| | |
|---|---|
| ID | `cena_mia_8` |
| Quando | 8 ❤️ · `missao(N_MIA_3) == concluida` · falar com a Mia na Praça (14:00–18:00); a cena continua no dia seguinte no andar 1, entre as 9:00 e as 12:00 |
| Onde | andar 1, Círculo de Pedras |
| Quem | herói, Mia, Coelho-Chifre Ancião, Mestre Gorvan (de longe) |
| Música | `guardiao` → `tema_mia` |

- *(na Praça)* **Mia** *(normal)*: "Amanhã. Andar 1. Círculo de Pedras. Vou lutar com o guardião. Sozinha."
- *(na Praça)* **Mia** *(normal)*: "A Irmã Célia disse 'só se fores com {nome}'. Levas-me? Mas não ajudas! Só vês. És a testemunha."

🎬 No dia seguinte. O Coelho-Chifre Ancião come erva no meio do círculo. A Mia aperta o arco. As pernas tremem-lhe.

- **Mia** *(normal)*: "Ele é maior do que eu me lembrava. Ou eu sou mais pequena. Não. Ele é maior."
- 🎬 O coelho levanta-se e bate o pé três vezes. Pedras saltam.

▶ **"Eu ajudo!"**
▶ *(cruzar os braços e ver)*
▶ **"Lembra-te: ele salta, tu rolas."**

- *(ajudo)* **Mia** *(zangado)*: "NÃO! Prometeste! Sozinha!" ⚙ −30 🎬 O herói fica onde está.
- *(ver)* 🎬 O herói encosta-se a uma pedra, de braços cruzados. A Mia vê isso e respira fundo. ⚙ +30
- *(lembra-te)* **Mia** *(feliz)*: "Ele salta, eu rolo. Eu sei! Foste tu que me ensinaste!" ⚙ +30

🎬 A luta (30 s, o jogador só vê): o coelho salta; a Mia rola para o lado como no treino. Quando ele cai, ela dispara.
O coelho carrega; ela rola outra vez. Três flechas. Quatro. A quinta acerta no chifre partido.
🎬 O coelho cai de lado, a arfar. Levanta-se, olha muito tempo para a Mia… e vai-se embora aos saltos, devagar, para a erva alta.

- **Mia** *(surpresa)*: "…Ganhei?"
- **Mia** *(feliz)*: "GANHEI! Viste? Tu viste! Testemunha! TESTEMUNHA!"
- 🎬 Corre para o herói. A meio do caminho, o abraço vira um aperto de mão muito sério.
- **Mia** *(normal)*: "Obrigada pelo treino, {Mestre/Mestra}. …Isto foi um aperto de mão de aventureira. Não foi um abraço."
- 🎥 Ao longe, em cima de uma das pedras do círculo, está o Mestre Gorvan. Acena uma vez com a cabeça e vai-se embora.
- **Mia** *(surpresa)*: "Aquele era o Mestre Gorvan? Ele veio ver? Ele VEIO VER?"

▶ **"Ele veio ver."**
▶ **"Mas foste tu que ganhaste."**

- *(veio ver)* **Mia** *(feliz)*: "Vou lembrar-me disto até ser velha. Velha tipo trinta anos."
- *(ganhaste)* **Mia** *(feliz)*: "Pois fui! Fui eu! Mas ele veio ver!"

⚙ As flores ficam 15% mais baratas. A Mia passa a mandar **cartas** (1 por semana), com a letra muito grande e um desenho,
e um presente: Ramo do Campo, um doce ou uma **Pedra da Sorte** (pedra com uma cara pintada; decoração).

### ❤️ 10 — Rank F

| | |
|---|---|
| ID | `cena_mia_10` |
| Quando | 10 ❤️ · cena de 8 ❤️ vista · entrar na Guilda de manhã (8:00–12:00) |
| Onde | Guilda, sala do Cristal de Avaliação |
| Quem | herói, Mia, Lyra, Mestre Gorvan, Irmã Célia |
| Música | `guilda` → `tema_mia` (flauta e guizos) |

🎬 Estão todos na sala do Cristal. A Mia tem o vestido acabado de coser (a Irmã Célia passou a noite nisso) e uma fita amarela nova.

- **Lyra** *(feliz)*: "{nome}! Chegaste! A Mia não deixava começar sem ti. Ameaçou-me com um pau."
- **Mia** *(normal)*: "Não ameacei. Informei."
- **Lyra** *(normal)*: "Pronto. Mia, põe a mão no Cristal de Avaliação. É só para o registo."
- 🎬 A Mia põe a mão no cristal. O cristal fica branco. Só branco. Não acontece mais nada.
- **Lyra** *(triste)*: "Ah… Não tens Skill Única. Pois. Só os Jogadores têm."
- 🎬 Silêncio. A Mia olha para a mão.

▶ **"Não precisas de dom."**
▶ *(pôr-lhe a mão no ombro)*

- **Mia** *(normal)*: "…Eu sei. Não preciso de dom. Tenho treino."
- **Gorvan** *(normal)*: "Hmm. A maior parte dos aventureiros não tem dom." 🎬 Pausa. "Eu não tenho."
- **Mia** *(surpresa)*: "…O senhor não tem?"
- **Gorvan** *(normal)*: "Tenho teimosia. Serve."
- 🎬 O Gorvan escreve num cartão de registo, devagar, com a mão esquerda. Dá-o à Mia.
- **Gorvan** *(normal)*: "Mia. Rank F. Missões fáceis. Volta viva."
- 🎬 Vira-se para sair. Para à porta.
- **Gorvan** *(normal)*: "Não morras. É a única regra."
- 🎬 Sai. A Mia fica a olhar para o cartão, com as duas mãos.
- **Mia** *(feliz)*: "Ele disse-me a regra. A mesma que te disse a ti. A Lyra contou-me."
- **Lyra** *(feliz, a chorar)*: "Eu não estou a chorar. É poeira. A Guilda tem muita poeira."
- **Irmã Célia** *(feliz)*: "…Pois. Muita poeira."
- 🎬 A Mia vira-se de costas um segundo. Depois tira de trás do balcão um embrulho comprido.
- **Mia** *(normal)*: "Isto é para ti. Juntei o dinheiro das flores. Muito tempo. Não digo quanto, senão ficas triste."
- 🎬 Um arco de madeira clara, com uma fita amarela atada no punho.
- **Mia** *(feliz)*: "Foi o Brom que o fez. Eu escolhi a madeira. Ele diz que é um arco que cresce contigo. Como eu."
- **Mia** *(feliz)*: "Mandei fazer dois. O meu é mais pequeno. Por enquanto."
- **Mia** *(normal)*: "Agora já posso subir contigo. Não à frente. Atrás. Para ver tudo."
- 🎥 À porta, o Gorvan (que voltou sem ninguém dar por isso) ouve isto e fica muito quieto. Toca no ombro. Vai-se embora.

▶ **"Bem-vinda à equipa, colega."**
▶ **"Atrás de mim. Por agora."**

- *(colega)* **Mia** *(feliz)*: "COLEGA. Rank F. Equipa. Hoje é o melhor dia de sempre. E sempre é muito tempo."
- *(por agora)* **Mia** *(feliz)*: "Por agora! Daqui a uns anos, à frente! Avisei no primeiro dia!"

⚙ A Mia fica **rank F**: o Cristal Mestre já a leva a qualquer andar.
⚙ A Mia pode ser **companheira** (arqueira; skill **Chuva de Flechas Pequena**; ver `docs/NPCS.md`, secção 4).
⚙ Recebes o **Arco da Mia** (ver `docs/ARMAS.md`, secção 8). A Mia passa a ter a fala `mia_dia_66` e continua a vender flores
quando não está contigo ("os aventureiros também precisam de dinheiro"). No epílogo é rank B aos 14 anos (ver `docs/HISTORIA.md`, secção 7).

---

## 9. Missões

### N_MIA_1 — Primeira Espada (2 ❤️, depois da cena de 2 ❤️)

- **Pedir** — **Mia** *(normal)*: "Pedes ao Brom uma espada para mim? Pequena. A mim ele diz 'sai da forja, miúda'. A ti ouve. Às vezes."
  ▶ **"Vou falar com ele."** ⚙ missão iniciada · ▶ **"Uma espada é perigosa."** → *(zangado)* "Os paus também! Já parti três!" ⚙ −30 (a missão fica disponível)
- **Passos**:
  1. Falar com o **Brom**. **Brom**: "Uma espada? Para a miúda das flores? NÃO. Espadas não são brinquedos."
     ▶ **"Ela treina todos os dias."** → **Brom**: "…Todos os dias? Hmpf. Eu também comecei com um pau." ·
     ▶ **"Faz uma sem fio."** → **Brom**: "Sem fio, sem ponta, leve. Hmpf. Isso é uma colher comprida."
  2. Levar ao Brom **2 Lingote de Cobre + 1 Carvalho**.
  3. Voltar no dia seguinte. **Brom**: "Toma. Sem fio. Sem ponta. Bem equilibrada. A melhor colher que já fiz."
- **Durante** — **Mia**: "O Brom já disse que sim? Já? E agora? E agora? E AGORA?"
- **Entregar** — **Mia** *(surpresa → feliz)*: "UMA ESPADA. Uma espada a sério!" 🎬 Examina-a. "…Não tem fio. Não faz mal! Tem ponta! …Também não tem ponta. NÃO FAZ MAL!"
  **Mia** *(feliz)*: "Vai chamar-se Relâmpago Dois. O pau reforma-se." ⚙ **Espada Pequena** (da Mia) · +100 amizade

### N_MIA_2 — Treino (4 ❤️, depois da cena de 4 ❤️)

- **Regra**: **5 sessões**, 1 por dia, na Praça (14:00–18:00). Cada sessão é o **minijogo de ritmo** (ver `docs/ATIVIDADES.md`,
  secção 4.7): tu fazes o movimento, a Mia repete. Acertar 70% das setas faz a sessão contar.

| Sessão | O que se treina | Antes | Depois |
|---|---|---|---|
| 1 | Postura | "Pés abertos! Eu sei! Lembro-me! Começa!" | "Não caí uma única vez! Isto é um recorde mundial!" |
| 2 | Golpe | "Hoje é a sério. Golpes a sério. Golpes de verdade." | "Dói-me o braço. É bom sinal, não é? Diz que é." |
| 3 | Esquiva | "Ele salta, eu rolo. Ele salta, eu rolo." | "Rolei tanto que fiquei tonta. Os monstros também ficam tontos?" |
| 4 | Pontaria (com pedras) | "Pedras? Hoje é com pedras? …Está bem. Mas não conta." | 🎬 Acerta em todos os alvos. "…Isto conta?" 🎬 O Gorvan está ao fundo, encostado ao muro, a ver. |
| 5 | Prova final | "Hoje é a prova! Se passar, sou… sou o quê? Sou mais." | (ver **Entregar**) |

- **Falhar uma sessão** — **Mia** *(zangado)*: "Outra vez! Os aventureiros não desistem!"
  ▶ **"Hoje chega, estás cansada."** ⚙ −30 → "Sou eu que digo quando chega!" · ▶ **"Outra vez."** ⚙ +30 → "Isso!"
- **Entregar** (depois da 5.ª sessão):
  - 🎬 A Mia ataca o boneco com a Espada Pequena. Falha. Falha outra vez. Zanga-se e atira a espada. A espada acerta no centro do alvo pintado.
  - **Mia** *(surpresa)*: "…Era para fazer isso. Mais ou menos."
  - 🎬 O Mestre Gorvan atravessa a Praça. As pessoas afastam-se. Para em frente à Mia, enorme.
  - **Gorvan** *(normal)*: "Espada não."
  - **Mia** *(zangado)*: "Porquê?!"
  - **Gorvan** *(normal)*: "Arco." 🎬 Tira de dentro da capa um arco pequeno e velho, com a madeira escura de tanto uso.
  - **Gorvan** *(normal)*: "Estava na arrecadação da Guilda. Era de uma arqueira. Já não precisa dele."
  - 🎬 Dá-o à Mia e vai-se embora. Não espera pelo obrigado.
  - **Mia** *(feliz)*: "O Mestre Gorvan deu-me um arco. A MIM. E nem disse 'Hmm'! Disse 'Arco'!"
  - **Mia** *(normal)*: "Vou chamar-lhe… Pica-Pau. Não, isso é ridículo. Vou chamar-lhe Pica-Pau."
  - ⚙ +150 amizade · título *{Mestre/Mestra} da Mia* · a Mia passa a ser arqueira (treina com o Pica-Pau) · flag `mia_arqueira`

### N_MIA_3 — A Fuga (6 ❤️, começa na cena de 6 ❤️)

- **Passos**:
  1. Seguir as pistas pelo Campo de Erva Alta (brilham a 5 m): a fita amarela presa num arbusto, pétalas no chão,
     a Espada Pequena caída, pegadas pequenas até ao **Moinho Abandonado**.
  2. Tens **3 minutos** (o tempo aparece no ecrã): a alcateia (3 Lobos Cinzentos e o líder) também anda à procura.
  3. A Mia está no sótão do moinho, com o arco apontado à porta. Lutar contra os lobos.
  4. Voltar com a Mia ao cristal da Zona Segura (`[Sistema] Passageiro acompanhado. Destino: Ascendia.`).
- **Se o tempo acabar** — os lobos chegam primeiro: a Mia sobe às pás do moinho e a luta tem 5 lobos em vez de 3. **A missão não falha.**
- **Durante a luta** — **Mia**: "Acertei num! Juro! Ele é que não quis cair!" · "Atrás de ti! Não, do outro lado! O outro atrás!"
- **Entregar** (na Zona Segura, logo a seguir):
  - 🎬 A Mia senta-se na erva, abraçada ao arco, a tremer. Tem um arranhão no joelho.
  - **Mia** *(triste)*: "Eu só queria ver. Um bocadinho. Pensei que conseguia."

  ▶ **"Podias ter morrido! És uma criança!"**
  ▶ **"Foste corajosa. E tonta. As duas."**
  ▶ **"Da próxima vez, subimos juntos."**

  - *(criança)* **Mia** *(zangado → triste)*: "Eu sei! Não precisas de gritar! …Não sou criança. Sou uma aventureira que se enganou." ⚙ −30
  - *(corajosa e tonta)* **Mia** *(surpresa → feliz)*: "As duas? …É justo. Os heróis dos livros também são as duas." ⚙ +30
  - *(juntos)* **Mia** *(feliz)*: "Juntos? Prometes? Promessa de aventureiro?" ⚙ +30
  - 🎬 Em Ascendia, a Irmã Célia está à porta da Igreja. Não grita. Abraça a Mia durante muito tempo.
  - **Irmã Célia** *(normal)*: "Obrigada, {nome}. Ela fica de castigo uma semana. Sem treinos."
  - **Mia** *(zangado)*: "UMA SEMANA?!" · **Irmã Célia**: "Duas." · **Mia** *(normal)*: "…Uma está ótimo."
  - ⚙ +200 amizade · flag `mia_fuga` · durante 7 dias a Mia não treina na Praça: vende flores até às 18:00
    ("Estou de castigo. Mas os castigos acabam. Os aventureiros não.")

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `mia_estado_vida` | `vida_pct < 30` | surpresa | "Estás a sangrar! Isso é sangue a sério?! Vai à Irmã Célia! Eu levo-te as coisas!" |
| `mia_estado_maldito` | `estado(amaldicoado)` | feliz | "Tens uma nuvem roxa na cabeça! Que fixe! …Não é fixe? A Irmã Célia tira isso. Ela tira tudo." |
| `mia_estado_cansado` | `estado(cansado)` | normal | "Tens cara de quem não dorme. Eu também faço essa cara. A Irmã Célia manda-me logo para a cama." |
| `mia_estado_molhado` | `estado(encharcado)` | surpresa | "Estás encharcad{o/a}! Caíste num rio? Num lago? Num monstro de água?" |
| `mia_estado_sapo` | `estado(sapo)` | surpresa | "Um sapo com a mochila de {nome}! …És tu? Fica quiet{o/a}. Eu espero que passe. Não dou beijos a sapos." |
| `mia_arma_nova` | arma equipada pela 1.ª vez com raridade Épica ou melhor | feliz | "Isso brilha! Posso tocar? Só com um dedo? Com meio dedo?" |
| `mia_arco` | `arma_tipo == arco && flag(mia_arqueira)` (1.ª vez) | feliz | "Tens um arco! Como eu! Agora somos arqueiros. Eu sou a melhor. Tu és {o segundo/a segunda}." |
| `mia_fita` | tens a Fita Amarela equipada (1.ª vez) | feliz | "Estás a usar a fita! A nossa fita! Agora toda a gente sabe que somos uma equipa." |
| `mia_animal` | `animal != nenhum` (1.ª vez) | feliz | "Um animal! Como se chama? Posso dar-lhe um segundo nome? Um nome de aventureiro?" |
| `mia_comp_gorvan` | `companheiro(gorvan)` | surpresa | "O Mestre Gorvan vai contigo?! Mestre, posso ir também?" 🎬 Pausa. "Ele disse 'Hmm'. Isso é sim?" |
| `mia_comp_kai` | `companheiro(kai)` | zangado | "Kai, ensina-me o Corte em Cruz! …Disse 'quando fores mais alta'. Detesto o Kai." |
| `mia_comp_mia` | `companheiro(mia)` (falar com ela em Ascendia) | normal | "Estou de serviço! Não posso conversar. Bem, posso. Mas com voz de aventureira." |
| `mia_classe` | 1.ª conversa depois de escolher ou evoluir a classe | feliz | "Agora és {classe}! Quando eu crescer também vou ser {classe}. Ou arqueira. Arqueira." |
| `mia_rank` | 1.ª conversa depois de subir de rank | feliz | "Rank novo! Eu ainda sou rank 'quase'. Mas estou a subir." (com 10 ❤️: "Eu continuo F. Mas um F muito forte.") |

### Serviço

**Flores da Mia** (esquina do Bairro Baixo, 7:00–13:00; durante o castigo de N_MIA_3, até às 18:00). Descontos: 5% (2 ❤️) e 15% (8 ❤️).
As flores contam como **flores** para os presentes (gostam: Lyra, Dona Marta, Hana, Irmã Célia, Lucien…; detestam: Gorvan, Brom, Kai, Rook).

| Estação | O que vende | Preço |
|---|---|---|
| Primavera, Verão | **Ramo do Campo** · **Flor de Mel** | 20 · 30 ouro |
| Outono | **Ramo do Campo** · **Ramo de Folhas** (ninguém compra; é neutro para todos) | 20 · 5 ouro |
| Inverno | **Flor de Papel** (feita com formulários velhos da Guilda) | 15 ouro |

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `mia_serv_abrir` | abrir a loja | feliz | "Flores fresquinhas! Bem, frescas de manhã. Escolhe!" (no inverno: "Flores de papel! Não murcham! Nunca! É a vantagem do papel.") |
| `mia_serv_comprar` | comprar | feliz | "Obrigada! Este dinheiro vai para o fundo de aventureira. É um frasco. Debaixo da cama." |
| `mia_serv_comprar_muito` | comprar 5 ou mais de uma vez | surpresa | "CINCO?! Vais dar flores à cidade inteira? Boa ideia. Compra seis." |
| `mia_serv_folhas` | comprar um Ramo de Folhas | surpresa | "Compraste FOLHAS? Alguém comprou folhas! Vou contar ao Tobias. Estratégia!" |
| `mia_serv_sem_dinheiro` | sem ouro | normal | "Não tens dinheiro? Eu às vezes também não. Volta quando tiveres. A flor espera." |
| `mia_serv_fechado` | fora de horas | normal | "A loja está fechada! Agora estou a treinar. Os aventureiros têm horário. Volta de manhã!" |
