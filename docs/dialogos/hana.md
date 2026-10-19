# Hana — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.14. Dados: `dados/dialogos/hana.json`. Loja: `docs/LOJAS.md`, secção 2.7. Quinta: `docs/CIDADES.md`, secção 3.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios, alegres, saltitantes; com uma risadinha no fim |
| Como fala | entusiasmada, fala das plantas como de pessoas (com nome), conta piadas más às couves, nunca se queixa de trabalho |
| Repete | "Bom dia!" (a qualquer hora), "Ela está a crescer!", "As plantas crescem melhor quando lhes contas piadas." |
| Tiques | limpa as mãos às calças e deixa marcas de terra (animação `limpar_maos`); cheira tudo o que lhe dão |
| Nunca diz | que está cansada (às 4 da manhã já está a regar) |
| Chama ao herói | "vizinh{o/a}" (desde que tens quinta); `{nome}` com 4+ corações |
| Quem é | 24 anos. A família tinha uma quinta num mundo de **campos de trigo dourado** que a torre engoliu quando ela tinha 9 anos. Desceu com os pais e um bolso cheio de sementes. Os pais já morreram; a quinta alimenta meia cidade |
| Rotina | Quinta 4:00–17:00 · banca no Mercado 17:00–19:00 · ao Domingo, Praça de manhã a cuidar dos canteiros públicos |
| Na quinta dela vive | o **Bolota** (fungoide, depois de R2_06) e um espantalho chamado **Senhor Palha** com quem ela fala |

---

## 2. Primeira conversa

Só acontece quando a **tua quinta abre** (andar 10). Antes disso ela vende no Mercado e diz só falas curtas.

- **Hana** *(feliz)*: "Bom dia! É boa tarde? Bom dia na mesma! És o meu vizinho novo! Ou vizinha! A quinta ao lado da minha é tua!"
- **Hana** *(normal)*: "Aquilo agora é só pedras e ervas daninhas. Mas a terra é boa. Cheira. Não, cheira mesmo. Ajoelha-te e cheira."
- **Hana** *(feliz)*: "Planta, rega todos os dias, e conversa com elas. Eu sei que parece tolice. Mas as minhas couves são as maiores da cidade por alguma razão."

⚙ Abre a quinta (`tut_quinta`) e o menu: **Conversar · Perguntar sobre… · Missões · Loja e quinta · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `hana_dia_01` | `hora entre 4 e 6` | feliz | "Bom dia! Já reguei, já colhi, já… são seis da manhã? Ah." |
| `hana_dia_02` | `hora entre 6 e 10` | feliz | "As couves acordaram bem-dispostas. Contei-lhes uma piada sobre uma batata. Riram-se. Por dentro." |
| `hana_dia_03` | `hora entre 12 e 15` | normal | "O sol do meio-dia é para as abóboras. As alfaces preferem sombra. São mais tímidas." |
| `hana_dia_04` | `hora entre 17 e 19` | feliz | *(no Mercado)* "Legumes frescos! Colhidos hoje! Bem, alguns ontem. Mas com carinho!" |
| `hana_dia_05` | — | normal | "As plantas crescem melhor quando lhes contas piadas." |
| `hana_dia_06` | — | feliz | "Esta cenoura chama-se Gustavo. Vai ser a maior da estação. Não lhe digas, fica convencida." |
| `hana_dia_07` | — | normal | "O Senhor Palha assusta os corvos. Os corvos não têm medo dele. Mas fingem, por educação." |
| `hana_dia_08` | — | feliz | "A Dona Marta compra-me legumes todas as manhãs. Escolhe-os um a um. Eu finjo que não vejo que ela fala com eles também." |
| `hana_dia_09` | — | normal | "Uma quinta não é trabalho. É conversa lenta com a terra. A terra responde em meses." |
| `hana_dia_10` | `dia_semana == domingo && hora entre 7 e 12` | feliz | *(na Praça)* "Domingo trato dos canteiros da cidade! Ninguém me pediu. As flores pediram." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `hana_dia_20` | `estacao == primavera` | feliz | "PRIMAVERA! Tudo a nascer! Planta nabos, morangos, cenouras! Planta tudo! Não, planta com calma." |
| `hana_dia_21` | `estacao == verao` | normal | "Verão: rega duas vezes se não chover. Os tomates bebem como o Brom." |
| `hana_dia_22` | `estacao == outono` | feliz | "Outono é colheita! E abóboras! Já escolhi a minha abóbora para a Noite dos Espíritos. Chama-se Bernardo." |
| `hana_dia_23` | `estacao == inverno` | triste | "No inverno quase nada cresce cá fora. Faço uma estufa no coração. E nos vasos da cozinha." |
| `hana_dia_24` | `clima == chuva` | feliz | "Chuva! Rega de borla! As plantas estão a beber e eu estou a descansar o braço." |
| `hana_dia_25` | `clima == trovoada` | triste | "Trovoada. Fico com medo pelos milhos. Os milhos são altos e orgulhosos. Os raios gostam de orgulhosos." |
| `hana_dia_26` | `clima == neve` | normal | "Neve. A terra está a dormir debaixo de um cobertor branco. Não a acordes." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `hana_dia_40` | `missao(R2_06) == concluida` | feliz | "O Bolota vive comigo agora! Planta fungos à sombra do celeiro e chora ao ver o sol. De alegria. Acho." |
| `hana_dia_41` | `andar_maximo >= 21` | feliz | "Sementes do pântano? Cacau? Café? Bananas?! Traz-me tudo! Vou ter uma selva ao pé do celeiro!" |
| `hana_dia_42` | `andar_maximo >= 31` | normal | "No deserto há plantas que vivem sem água. Traz-me um cacto. Quero perguntar-lhe como faz." |
| `hana_dia_43` | `andar_maximo >= 41` | normal | "Flor-de-neve: só cresce no frio. Se a estufa estiver pronta, consigo ter inverno num canto e verão no outro." |
| `hana_dia_44` | `andar_maximo >= 76` | triste | "Um jardim de rosas negras com um jardineiro que não deixa ninguém entrar… Jardins tristes deixam-me triste." |
| `hana_dia_45` | `andar_maximo >= 92` | feliz | "Lá em cima há uma Semente do Mundo? Que dá uma coisa diferente cada vez? É o sonho de qualquer agricultora." |
| `hana_dia_46` | `flag(arvore_praca)` | feliz | "A árvore da Praça cresceu dez centímetros esta semana! Medi! Pus-lhe uma fita! Os pombos acham que é para eles." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `hana_dia_60` | `coracoes(hana) >= 2` | feliz | "Os teus nabos estão lindos! Contaste-lhes piadas? Contaste! Nota-se!" |
| `hana_dia_61` | `coracoes(hana) >= 4` | normal | "Quando sobes, rego a tua quinta também. Não digas que não. Já está regada." |
| `hana_dia_62` | `coracoes(hana) >= 6` | feliz | "Dei o teu nome a uma couve. Não te ofendas. É a couve mais bonita." |
| `hana_dia_63` | `coracoes(hana) >= 8` | triste | "Às vezes sonho com os campos de trigo da minha terra. Dourados até ao horizonte. Acordo com cheiro a pão." |
| `hana_dia_64` | `coracoes(hana) >= 10` | feliz | "A nossa árvore está a dar sombra! Na Praça! Os velhos sentam-se lá a jogar às cartas. Fizemos isso. Nós." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `hana_dia_70` | `origem == dormir` | feliz | "Dormes até às sete?! É uma vida de luxo! Às sete eu já almocei." |
| `hana_dia_71` | `origem == ajudante` | feliz | "Ajudaste-me a apanhar as maçãs sem eu pedir! No teu mundo devias ter uma quinta. Ou uma avó com uma quinta." |
| `hana_dia_72` | `skill_unica == domador_nato` | normal | "Os animais seguem-te como se fosses o Zed. Tens jeito. Ajuda-me com as galinhas. Elas não me respeitam." |
| `hana_dia_73` | `skill_unica == mestre_artesao` | feliz | "As tuas colheitas saem sempre boas? Isso é talento! Ou é a Skill. É a Skill. Mas também é talento." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `hana_curta_1` | feliz | "Bom dia! Outra vez!" |
| `hana_curta_2` | normal | "Estou a sachar. Fala enquanto sacho. Elas ouvem também." |
| `hana_curta_3` | feliz | "Rega a tua quinta! Já regaste? Rega outra vez. Não. Não regues outra vez." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Hana** *(normal)*: "A torre é como uma árvore enorme. Os andares são ramos. E nós somos… as formigas? Não, somos os passarinhos."
- **Hana** *(triste)*: "Engoliu a minha terra. Mas deixou-me as sementes. Às vezes penso que a torre não sabe o que faz. Como uma tempestade."
- **Hana** *(feliz)*: "E das tempestades nascem coisas. Depois da chuva, a terra fica ótima."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "A floresta tem morangos selvagens e flores de mel! Traz sementes! E Bolotas Douradas! Dão árvores douradas!" |
| 2 Cavernas | "Debaixo da terra crescem fungos e batatas roxas. Planta-os à sombra do celeiro. Ficam felizes no escuro." |
| 3 Pântano | "Cacau! Café! Bananas! A selva é a melhor despensa da torre." |
| 4 Deserto | "Tâmaras, açafrão e cactos que guardam água. Plantas espertas. Respeito-as." |
| 5 Gelo | "Bagas de inverno e couves do norte. Plantas teimosas que crescem na neve. Como eu." |
| 6 Oceano | "Algas doces e ananases! Preciso de um lago para as algas. Vamos fazer um lago? Vamos fazer um lago!" |
| 7 Vulcão | "Pimenta-lava! Batatas vulcânicas! Uma árvore que arde e não se queima! Que maravilha. Que perigo." |
| 8 Reino Assombrado | "Há um jardineiro lá em cima que guarda sementes de rosas negras. Ninguém devia guardar sementes. Sementes são para plantar." |
| 9 Céu | "Pessegueiros celestes e algodão-nuvem! Plantas que crescem no ar! Traz-me UMA. Por favor. Uma." |
| 10 Abismo | "A Semente do Mundo… Diz-se que dá uma coisa diferente cada vez. Como se lembrasse de todos os mundos." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `hana_rumor_01` | — | "A primeira Maçã Dourada que comes deixa-te mais forte para sempre. É verdade. Comi uma. Agora carrego dois sacos de batatas de cada vez." |
| `hana_rumor_02` | — | "O Zed diz que os corvos são inteligentes. Eu sei. Roubam-me as couves pela ordem do tamanho." |
| `hana_rumor_03` | `andar_maximo >= 6` | "No andar 6 as flores dão força quando passas por elas. Tentei plantá-las cá. Dão força às minhas galinhas. Agora fogem mais depressa." |
| `hana_rumor_04` | `andar_maximo >= 16` | "Os fungoides de Mycélia pagam em cogumelos. Uma vez paguei-lhes em couves. Ainda não perceberam o que fazer com elas." |
| `hana_rumor_05` | `andar_maximo >= 24` | "Há uma Semente Carnívora no pântano que come pragas. Uma planta-guarda! O Senhor Palha vai ficar com ciúmes." |
| `hana_rumor_06` | `andar_maximo >= 76` | "Dizem que o jardineiro dos jardins negros era um jardineiro de verdade, antes. Que plantou as rosas para uma rainha. Que ainda espera por ela." |

### 4.4 A vida dela
| Corações | Fala |
|---|---|
| 0 | "Sou a Hana. Planto coisas. Coisas crescem. A cidade come. É uma vida boa!" |
| 2 | "Nasci numa quinta enorme, num mundo de campos de trigo. Dourados. Quando o vento passava, pareciam o mar." |
| 4 | "A torre engoliu o meu mundo quando eu tinha nove anos. A minha mãe pôs-me um saquinho de sementes no bolso e disse: 'Isto é a nossa casa.'" |
| 6 | "Os meus pais trabalharam esta terra vinte anos. Morreram há três invernos, um logo atrás do outro. Ela não aguentou ficar sem ele." |
| 8 | ver a **cena de 8 ❤️** |
| 10 | "Já não tenho saudades de casa como antes. Agora tenho casa aqui. E uma árvore na Praça. Plantada contigo." |

---

## 5. Presentes

**Adora:** sementes raras (qualquer semente de região 3+ ou de árvore), Guano, Semente do Mundo · **Gosta:** legumes, flores ·
**Detesta:** pragas (Gafanhoto, Lagarta), Pétala Carnívora.

| Reação | Falas |
|---|---|
| Adora | "Sementes novas! Nunca vi estas! Vou plantá-las hoje! Agora! Já!" · "Guano! O ouro dos agricultores! Isto é melhor do que flores. Isto faz FLORES." |
| Gosta | "Uma cenoura linda! Fizeste-a tu? Que orgulho. Vou pô-la na sopa. Com respeito." |
| Neutro | "Obrigada! Vou arranjar-lhe um sítio. Talvez ao pé do Senhor Palha." |
| Não gosta | "Hmm. Isto não se planta. Nem se come. Para que serve? Não respondas." |
| Detesta | "Uma pétala carnívora?! Ela come as minhas abelhas! Leva-a para longe!" · "Lagartas! Na minha quinta! Tira! TIRA!" |

| Item | Fala |
|---|---|
| Semente da Árvore-Mãe | não se pode oferecer: a Hana diz "Essa não é um presente. Essa é uma promessa. Guarda-a. Um dia plantamo-la juntos." |
| Maçã Dourada | "Uma maçã dourada! Não a como. Vou plantar as sementes. Uma árvore dourada dá mais do que uma maçã." |

---

## 6. Aniversário e festivais

**Aniversário (Primavera, dia 11):**
- Sem presente: "Faço anos na primavera! Como as flores! Toda a gente se esquece porque estão ocupados a plantar. Eu também me esqueço."
- Com presente que adora: "Lembraste-te! E trouxeste sementes! O melhor presente: um presente que dá mais presentes!"

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "O MEU festival! Concorro com uma flor que treinei o ano todo. Chama-se Margarida. É uma rosa. É confuso, eu sei." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "SIM! Danço como quem planta: dois passos, um buraco, outro passo. Vamos!" ⚙ +100 |
| F_02 Festival da Pesca | "Não pesco. Ponho as tripas dos peixes na terra. Fertilizante. A pesca alimenta as minhas couves." |
| F_03 Noite dos Espíritos | "Esculpo as abóboras para a cidade toda! Este ano fiz uma com a cara do Gorvan. Ele disse 'Hmm'. Gostou." |
| F_04 Festival da Estrela | "Amigo secreto! Vou dar uma planta em vaso. Dou sempre uma planta. Assim quem recebe tem de cuidar de alguma coisa." |
| F_05 Dia da Subida | "Comida grátis na Praça! Os legumes são meus! Come os legumes! Não comas só a carne!" |
| F_06 Concurso da Casa | "Vejo os jardins das casas. Se tiveres flores à porta, voto em ti. Não sou jurada. Voto na mesma." |
| F_07 Noite das Lanternas | "Ponho duas lanternas: pelos meus pais. E planto uma flor na margem, ao pé de onde as soltei. Todos os anos a mesma flor." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Os javalis estragam campos! Um rei dos javalis estraga reinos! Obrigada!" |
| Ent Ancião (10) | "A Árvore-Mãe morreu… mas deixou-te uma semente, não deixou? Não a percas. Uma semente é uma árvore à espera." |
| Aranha-Mãe (15) | "As aranhas comem pragas. Não te vou agradecer por matares uma aranha. Mas aquela era grande demais." |
| Golem de Cristal (20) | "Uma casa! Com jardim? Tem jardim? Eu faço-te o jardim! De graça! Bem, pagas as sementes." |
| Serpente do Lodo (25) | "Lodo do pântano é ótimo para a terra. Trouxeste? Não? Para a próxima traz um balde." |
| Hidra do Pântano (30) | "Cabeças que voltam a crescer. Como as ervas daninhas! Tens de arrancar pela raiz. Sempre pela raiz." |
| Escorpião Imperador (35) | "O deserto é seco, mas tem sementes valentes. Trouxeste-me alguma? Uma? Meia?" |
| Faraó Eterno (40) | "Um rei de areia. A areia é a terra que desistiu. Mas até na areia cresce o cacto." |
| Yeti Ancião (45) | "Lá em cima está frio. Comeste a sopa da Dona Marta antes de ir? Comeste? Muito bem." |
| Dragão de Gelo (50) | "Metade da torre! Plantei cinquenta sementes de girassol para festejar. Vão nascer todas viradas para ti." |
| Capitão Esqueleto (55) | "Piratas com ouro e sem sementes. Que vida tão triste. Ouro não se come." |
| Leviatã (60) | "O mar está calmo. Que bom. A Lyra está triste por causa do Kai. Levei-lhe flores. Ela sorriu um bocadinho." |
| Ferreiro Infernal (65) | "O Brom pediu-me uma flor para pôr na forja. O Brom! Uma flor! Dei-lhe um cardo. Combina com ele." |
| Kai — salvo (68) | "O Kai voltou! Vou fazer-lhe a sopa de legumes. Não, a Dona Marta faz. Eu dou os legumes. Muitos legumes." |
| Kai — vencido (68) | "Plantei uma árvore pequena pelo Kai. Ao pé da tua quinta. Para quando ele voltar, haver sombra." |
| Titã de Magma (70) | "O vulcão dorme. Terra de vulcão é a mais fértil de todas. Traz-me um saco. Por favor." |
| Lich Bibliotecário (75) | "O Fausto encontrou um livro sobre plantas antigas no meio dos livros que trouxeste! Está a lê-lo para mim. Devagar. Muito devagar." |
| Rei Sem Coroa (80) | "O reino tinha jardins. Os jardins ficaram negros quando o rei se perdeu. Talvez agora voltem a ter cor." |
| Grifo Real (85) | "Um grifo! Os grifos comem pêssegos? Tenho pêssegos! Celestes!" |
| Serafim Caído (90) | "Vens triste. Anda à quinta. Ajuda-me a apanhar morangos. Morangos não curam nada. Mas ajudam." |
| Guardião do Tempo (95) | "Cinco andares. A tua quinta fica comigo. Rego-a todos os dias. Até voltares. E depois também." |

---

## 8. Cenas de coração

### ❤️ 2 — A conversa com as couves

| | |
|---|---|
| ID | `cena_hana_2` |
| Quando | 2 ❤️ · entrar na Quinta da Hana entre as 5:00 e as 7:00 |
| Onde | horta da Hana, nevoeiro da manhã |
| Quem | herói, Hana |
| Música | `ascendia_dia` (versão calma, com pássaros) |

🎬 A Hana está ajoelhada entre as couves, a falar baixinho com elas. Não vê o herói.
- **Hana** *(feliz)*: "…e então a batata disse ao nabo: 'Sabes porque é que nunca te convidam para festas? Porque és muito RAIZ.' Hihihi."
- 🎬 Vira-se. Vê o herói. Fica vermelha.
- **Hana** *(surpresa)*: "Ah! Há quanto tempo estás aí? Ouviste a piada? Não ouviste. Diz que não ouviste."

▶ **"A piada era boa."**
▶ **"As couves riram-se?"**

- *(boa)* **Hana** *(feliz)*: "Era horrível! Mas obrigada. As couves preferem as horríveis." ⚙ +30
- *(riram)* **Hana** *(normal, a sério)*: "Riem-se por dentro. Ficam mais verdes. Repara amanhã." ⚙ +30 · no dia seguinte, as couves da Hana estão mesmo mais verdes (troca de cor)

⚙ 5% de desconto nas sementes e +1 talhão grátis na tua quinta.

### ❤️ 4 — A tempestade

| | |
|---|---|
| ID | `cena_hana_4` |
| Quando | 4 ❤️ · primeira trovoada depois de chegares aos 4 corações · entrar nas Quintas |
| Onde | Quinta da Hana, de noite, chuva forte |
| Quem | herói, Hana, Bolota (se já vive lá) |
| Música | `tempestade` (curta) → `amizade` |

🎬 Chuva e vento. A Hana corre de um lado para o outro a tapar as plantas com panos. Um pano voa.
- **Hana** *(nervosa)*: "{nome}! Ajuda-me! O vento vai arrancar as estufas pequenas! Segura as cordas!"
- 🎬 **Minijogo curto**: segurar 3 cordas de lona contra o vento (carregar no botão no ritmo das rajadas) e tapar 5 canteiros.
- 🎬 Acaba a tempestade. Os dois sentados no celeiro, encharcados. O Bolota faz luz.
- **Hana** *(feliz)*: "Salvámos quase tudo! Perdemos três tomates. Vou fazer-lhes um funeral. É uma piada. Vou fazer molho."
- **Hana** *(normal)*: "Na minha terra, quando havia tempestade, a minha mãe dizia: 'A terra está a respirar fundo.' E ficava tudo bem."

⚙ Receita **Sopa de Tomate da Hana** (cura 30%, +10% regeneração) e o **Regador de Cobre** (se ainda não o tiveres).

### ❤️ 6 — Chocolate!

| | |
|---|---|
| ID | `cena_hana_6` |
| Quando | 6 ❤️ · `andar_maximo >= 21` · Quinta, de manhã |
| Onde | Quinta da Hana |
| Quem | herói, Hana |
| Música | `selva_tambores` (versão alegre) |

- **Hana** *(feliz)*: "Sabes o que eu nunca comi? CHOCOLATE. Nunca. Nem no meu mundo. O Kai fala dele como se fosse magia."
- **Hana** *(normal)*: "Dizem que vem de uma fruta do pântano. Cacau. Traz-me cinco frutos. Eu planto as sementes. E um dia, a cidade tem chocolate."

⚙ Missão **R3_14 Chocolate!** (secção 9). A Hana aceita jantar em tua casa (traz salada; muita salada).

### ❤️ 8 — A semente da casa

| | |
|---|---|
| ID | `cena_hana_8` |
| Quando | 8 ❤️ · pôr do sol (18:00–20:00), campo de trigo da Hana |
| Onde | o pequeno campo de trigo atrás do celeiro da Hana |
| Quem | herói, Hana |
| Música | `tema_hana` (versão curta, violino e guitarra) |

🎬 Um campo pequeno de trigo dourado. O vento passa e o trigo ondula. A Hana está sentada no meio.
- **Hana** *(triste)*: "Este trigo é da minha terra. As últimas sementes que a minha mãe me deu. Planto-as todos os anos. Guardo sempre um punhado para o ano seguinte."
- **Hana** *(feliz)*: "Olha o vento. Parece o mar. Era assim, lá. Mas até ao horizonte."
- 🎬 Tira do bolso um saquinho de pano velho. Dentro, uma semente grande e escura que brilha um bocadinho.
- **Hana** *(normal)*: "E esta. A minha mãe chamava-lhe 'a semente do mundo'. Disse que, se a plantasse no sítio certo, crescia uma coisa que lembrava a nossa casa. Nunca encontrei o sítio certo."

▶ **"Vamos encontrar o sítio certo juntos."**
▶ **"Talvez o sítio certo seja aqui."**

- *(juntos)* **Hana** *(feliz)*: "Juntos. Está bem. Quando o encontrarmos, plantamos as duas: a tua e a minha." ⚙ +30 · flag `hana_semente`
- *(aqui)* **Hana** *(surpresa)*: "Aqui? Em Ascendia? …Talvez. Uma cidade inteira de gente que veio de outros sítios. Talvez seja o sítio certo para lembrar casas." ⚙ +30 · flag `hana_semente`

⚙ 15% de desconto. Passa a mandar **cartas** com legumes da estação e sementes.

### ❤️ 10 — A árvore da Praça

| | |
|---|---|
| ID | `cena_hana_10` |
| Quando | 10 ❤️ · Domingo, Praça, 7:00–9:00 · tens a **Semente da Árvore-Mãe** (se já a plantaste na quinta, usa-se uma estaca dela) |
| Onde | Praça da Torre, um canteiro novo ao pé da fonte |
| Quem | herói, Hana, alguns NPCs a assistir (Lyra, Célia, Aldric com um papel) |
| Música | `tema_hana` |

🎬 A Hana cavou um buraco redondo no canteiro novo. Tem a semente dela na mão.
- **Hana** *(feliz)*: "Encontrei o sítio certo. É aqui. No meio da cidade. Onde toda a gente passa."
- **Hana** *(normal)*: "A tua semente e a minha. A da Árvore-Mãe e a do meu mundo. Juntas."
- 🎬 Os dois põem as sementes no buraco. A Hana tapa com terra. O herói rega.
- **Governador Aldric** *(da plateia)*: "Isto tem licença? …Tem. Acabei de a assinar."
- 🎬 Um rebento verde e dourado aparece logo, pequenino. A Hana chora e ri.
- **Hana** *(feliz)*: "Daqui a uns anos vai dar sombra à Praça inteira. E quem se sentar debaixo dela vai lembrar-se de casa. De qualquer casa."
- 🎬 Dá-lhe o regador dourado dela.
- **Hana** *(feliz)*: "O meu regador. Rega nove de uma vez. E a estufa: já está montada na tua quinta. Fui eu, de madrugada. Não acordaste."

⚙ **Regador de Ouro** (rega 3×3) e **estufa grátis**. A **Árvore da Praça** cresce durante 28 dias: depois dá Folhas Douradas e **+5% de amizade ganha com toda a gente de Ascendia** (ver cena C1-10). Flag `arvore_praca`. Título *Jardineir{o/a} de Ascendia*.

---

## 9. Missões

### N_HANA_1 — A Primeira Colheita (0 ❤️, quinta aberta)
- **Pedir** — **Hana**: "A primeira colheita é a mais importante! Planta cinco nabos, rega-os todos os dias e traz-mos. Quero ver se tens mão para isto."
- **Passo**: plantar, regar e colher **5 Nabos Bravos** (Primavera; noutra estação a Hana dá sementes de Cebola em vez de nabo).
- **Entregar** — **Hana** *(feliz)*: "Olha estes nabos! Tortos, mas teus! Toma o meu regador velho. É melhor do que a tua lata." ⚙ **Regador de Cobre** · +100

### R2_06 — Bolota Quer Ver o Sol (a parte da Hana)
- Ao trazeres o **Bolota** (fungoide) de Mycélia a Ascendia, ele não aguenta o sol direto. A Hana resolve:
- **Hana** *(feliz)*: "Um cogumelo que fala! Pode viver à sombra do meu celeiro! Tenho um canto escuro e húmido. Perfeito para ele. Péssimo para mim."
- ⚙ O Bolota vive na quinta da Hana e vende Fungo Azul. +50

### R3_14 — Chocolate! (6 ❤️)
- **Passo**: trazer **5 Cacau** (região 3).
- **Entregar** — 🎬 a Hana parte um fruto, cheira, prova um grão cru. Faz uma careta enorme.
  - **Hana** *(surpresa)*: "É AMARGO! O Kai mentiu-me!"
  - **Hana** *(normal)*: "…Espera. A Dona Marta diz que se torra e se junta leite e açúcar. Vamos experimentar."
  - 🎬 Corte: as duas (a Hana e a Dona Marta) com chávenas. O herói também.
  - **Hana** *(feliz)*: "Chocolate quente! Agora percebo o Kai. Agora percebo TUDO."
  - ⚙ **Sementes de Cacau** · receita **Chocolate Quente** · +150

### R8_09 — O Jardineiro (`andar_maximo >= 76`)
- **Pedir** — **Hana** *(séria)*: "Há um jardineiro nos jardins negros do andar 76 que guarda sementes de rosas há séculos. As sementes estão a morrer na mão dele. Traz-mas. Eu dou-lhes vida."
- **Passo**: vencer **O Jardineiro** (monstro com nome, região 8) e trazer as sementes que ele guardava.
- **Entregar** — **Hana** *(triste)*: "Rosas negras. Estão tristes. Vou plantá-las ao sol. Talvez fiquem vermelhas outra vez. Talvez não. Mas vão crescer." ⚙ **Sementes de Rosa Negra** · **Chapéu de Palha do Jardineiro** · +150

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `hana_estado_vida` | `vida_pct < 30` | nervoso | "Estás ferid{o/a}! Tenho ervas para… não, vai à Igreja! As minhas ervas são para sopa!" |
| `hana_estado_veneno` | `estado(veneno)` | normal | "Veneno? Mastiga isto. É erva verde. Não cura. Mas é saudável." |
| `hana_estado_cansado` | `estado(cansado)` | feliz | "Cansad{o/a}? Deita-te no feno. É o colchão mais macio da cidade. As galinhas não se importam." |
| `hana_quinta_seca` | 3 dias sem regar a tua quinta | triste | "As tuas plantas estão com sede. Reguei-as eu, mas estão tristes. Elas gostam de ti, não de mim." |
| `hana_quinta_linda` | quinta com 20+ plantas de qualidade Excelente | feliz | "A tua quinta está mais bonita do que a minha! Estou com ciúmes! Estou orgulhosa! Estou as duas coisas!" |
| `hana_animal` | `animal != nenhum` (1.ª vez) | feliz | "Um animalzinho! Pode vir à quinta brincar! Desde que não coma as alfaces. Come as alfaces? Vai comer as alfaces." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `hana_serv_abrir` | abrir a loja | feliz | "Sementes da estação! E legumes frescos! E conselhos de graça!" |
| `hana_serv_semente` | comprar sementes | feliz | "Planta em terra solta. Rega todos os dias. E conta-lhes uma piada. Tem de ser má." |
| `hana_serv_fora_estacao` | semente fora da estação | normal | "Esta não cresce agora. Guarda-a para a {estacao}. Ou faz uma estufa!" |
| `hana_serv_alargar` | alargar o terreno | feliz | "Mais terra! Amanhã de manhã já está lavrada. Fui eu. Às quatro." |
| `hana_serv_vender` | vender legumes | feliz | "Que bonitos! Pago bem. Os Excelentes pago melhor." |
| `hana_serv_fechado` | 19:00–4:00 | — | `[Sistema] A Hana está a dormir. A quinta dorme também.` |
