# Mestre Gorvan — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.2. Dados: `dados/dialogos/gorvan.json`.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | muito graves e lentos (ver `docs/AUDIO.md`); antes de cada "Hmm." há uma pausa de 1 s |
| Como fala | frases de 1 a 6 palavras; corta o fim das frases; nunca explica duas vezes; o humor é seco e aparece sem aviso. Depois de **H_12** fala um pouco mais; depois de **H_19** às vezes acaba as frases e chega a rir-se |
| Repete | "Hmm.", "Volta viv{o/a}.", "Não morras.", "Chega.", "Outra vez.", "Bom." |
| Tiques | coça a barba quando pensa; quando está triste toca no ombro direito vazio (animação `tocar_ombro`) |
| Nunca diz | "adeus" (diz sempre "Volta viv{o/a}."); "desisto"; os nomes da equipa **antes de H_12** |
| Chama ao herói | "Jogador" (0–3 ❤️) · `{nome}` (4+ ❤️, depois da cena 4) · "parceir{o/a}" (só com 10 ❤️, e raramente) |
| Rotina | gabinete da Guilda (8:00–17:00) · campo de treino (17:00–20:00) · muralha norte, sozinho (21:00–1:00) · casa. Antes de **H_20** o campo de treino é só para ver os novatos e arrumar bonecos; às escondidas treina sozinho (cena 2) |
| Rotina ao Domingo | a Lyra está de folga: o Gorvan fica **sozinho ao balcão** da Guilda (8:00–18:00) e faz o trabalho dela… mal |

### A equipa do andar 74 (há 20 anos)

Quem escreve diálogos usa esta tabela. **No jogo**, os nomes só aparecem depois de **H_12** (estão no diário do andar 46).

| Nome | Papel | Como era | Objeto na Sala da Equipa (andar 74) |
|---|---|---|---|
| **Edrik** | espadachim e chefe da equipa; **Jogador nº 9 961** | calado, teimoso, escolhia sempre o caminho mais difícil ("os fáceis já estão gastos"); dizia o número como quem diz o nome | a espada partida |
| **Odília** | maga (fogo) e cartógrafa; escrevia o diário | mandona, tinha sempre frio, chamava "teimoso" ao Gorvan | o caderno de mapas, queimado nas pontas |
| **Teodoro** ("Téo") | curandeiro | contava piadas péssimas; tocava flauta à fogueira; deu à equipa o nome "Os Imortais" | a flauta de madeira |
| **Ilsa** | arqueira, a mais nova (17 anos) | ria-se alto; ia sempre atrás "para ver tudo"; tinha penas amarelas na aljava | a aljava das penas amarelas |
| Gorvan | tanque (machado e escudo) | o escudo da equipa | o machado (vira o **Machado do Gorvan**, lembrança) |

- **Ordem de marcha** (é a ordem das velas do puzzle do andar 74, escrita no diário): Edrik · Gorvan · Odília · Teodoro · Ilsa.
- **O que aconteceu** (só para quem escreve): no 74, o Colosso de Ossos fechou o túnel. Os ossos prenderam o braço
  direito do Gorvan quando ele protegia a Ilsa. Os outros seguraram o túnel e gritaram-lhe que fosse avisar a Guilda.
  Ele foi. Durante 20 anos chamou a isso "fugir". Em **H_19** percebe que o mandaram ir.

---

## 2. Primeira conversa

Depois da cena P6 (prólogo), a 1.ª vez que carregas em **Conversar** (no gabinete):

- **Gorvan** *(normal)*: "Hmm."
- 🎬 Olha para a Espada de Treino à cintura do herói.
- *(se tiver a Espada de Treino equipada)* **Gorvan** *(normal)*: "Ainda tens a espada. Bom."
- *(se não)* **Gorvan** *(zangado)*: "Não usas a espada. Usa. Não é enfeite."
- **Gorvan** *(normal)*: "Missões: com a Lyra. Classe: comigo, no nível 10. Problemas: com a Lyra."
- **Gorvan** *(normal)*: "Morrer: com ninguém. Não morras."

▶ **"Mais alguma coisa?"**
▶ **"Obrigad{o/a}, Mestre."**

- *(Mais alguma coisa?)* **Gorvan** *(normal)*: "Não." 🎬 Pausa. "…Come. A Dona Marta ralha. Comigo."
- *(Obrigado)* **Gorvan** *(normal)*: "Agradece quando voltares. Antes não conta."

⚙ Abre o menu de serviços do Gorvan: **Classe · Missões (rank alto) · Perguntar sobre…** (o **Treino** só aparece depois de H_20).

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gorvan_dia_01` | `hora entre 8 e 10` | normal | "Cedo. Bom. Quem chega cedo volta cedo." |
| `gorvan_dia_02` | `hora entre 10 e 12` | normal | "Papéis. A Lyra diz que são importantes. Eu assino. Não leio." |
| `gorvan_dia_03` | `hora entre 12 e 14` | normal | "Almoço? Já comi. Ontem." |
| `gorvan_dia_04` | `hora entre 17 e 20` | normal | "Os bonecos de treino não se queixam. Não pedem missões. Gosto deles." |
| `gorvan_dia_05` | `hora entre 21 e 23` | triste | "A muralha é boa à noite. Ninguém fala." 🎬 Pausa. "Tu também não falas. Fica." |
| `gorvan_dia_06` | — | normal | "Hmm." |
| `gorvan_dia_07` | — | normal | "Subir é fácil. Voltar é que custa." |
| `gorvan_dia_08` | — | normal | "Volta viv{o/a}. É uma ordem. A única que dou duas vezes." |
| `gorvan_dia_09` | — | normal | "A Lyra arrumou o meu gabinete. Agora não encontro a cadeira." |
| `gorvan_dia_10` | — | normal | "O Tobias quis vender-me um pente. Olhei para ele. Foi-se embora. Sem o pente." |
| `gorvan_dia_11` | — | feliz | "Compro luvas aos pares. Uma fica sempre nova. Tenho uma gaveta cheia. Queres uma?" |
| `gorvan_dia_12` | `dia_semana == segunda` | zangado | "Segunda-feira. Toda a gente entrega as missões atrasadas. A Lyra grita. Eu olho." |
| `gorvan_dia_13` | `dia_semana == domingo` | normal | "Domingo. A Lyra não está. As missões estão no quadro. Lê. Eu não leio em voz alta." |
| `gorvan_dia_14` | `dia_semana == domingo && hora entre 14 e 18` | normal | "Carimbei três missões com o carimbo errado. Não digas à Lyra. Ela descobre sozinha." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gorvan_dia_20` | `estacao == primavera` | zangado | "Primavera. Flores por todo o lado. Hmm." |
| `gorvan_dia_21` | `estacao == primavera && hora entre 8 e 12` | normal | "Os novatos chegam na primavera. Olham para a torre de boca aberta. Fecha a boca. Entram moscas." |
| `gorvan_dia_22` | `estacao == verao` | normal | "Calor. A capa fica. Tirá-la dá trabalho. Com um braço, muito." |
| `gorvan_dia_23` | `estacao == verao && hora entre 18 e 20` | normal | "No verão treino mais tarde. Por causa do sol. Ou da idade. Do sol." |
| `gorvan_dia_24` | `estacao == outono` | zangado | "As folhas entram na Guilda. Eu varro. Elas entram. Um dia ganho." |
| `gorvan_dia_25` | `estacao == outono && clima == chuva` | triste | "Chuva de outono. O ombro dói. O braço que não está cá." |
| `gorvan_dia_26` | `estacao == inverno` | normal | "Frio. Bom. O frio não mente." |
| `gorvan_dia_27` | `estacao == inverno && clima == neve` | feliz | "Há um boneco de neve à porta. Tem capa. Tem um braço." 🎬 Pausa. "Ninguém lhe toca. Ordem da Guilda." |
| `gorvan_dia_28` | `clima == chuva` | normal | "Chuva. Na torre não chove igual. Lá em cima chove de lado." |
| `gorvan_dia_29` | `clima == trovoada` | normal | "Os novatos têm medo dos trovões. Eu tenho medo do silêncio depois." |
| `gorvan_dia_30` | `clima == nevoeiro` | normal | "Nevoeiro. Há andares assim o dia todo. Aprende a ouvir. Os olhos mentem." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gorvan_dia_40` | `andar_maximo < 5` | normal | "Andares 1 a 4. Aprende a fugir. Fugir também é técnica." |
| `gorvan_dia_41` | `andar_maximo >= 5 && andar_maximo < 11` | normal | "O Kai diz que é mais rápido. É. Tu és mais teimos{o/a}. No fim ganha o teimoso." |
| `gorvan_dia_42` | `andar_maximo >= 21 && missao(H_08) == inativa` | normal | "Andar 24. Há uma decisão para tomar. A Guilda ainda não a tomou. Eu ainda não a tomei." |
| `gorvan_dia_43` | `flag(sssar_defendida)` | normal | "Desobedeceste a uma ordem minha." 🎬 Pausa. "E tinhas razão. Não te habitues." |
| `gorvan_dia_44` | `flag(sssar_expulsa)` | triste | "Cumpriste a ordem. A aldeia está vazia." 🎬 Coça a barba. "As ordens pesam mais a quem as dá." |
| `gorvan_dia_45` | `andar_maximo >= 41 && missao(H_12) != concluida` | triste | "Gelo. No andar 46 há uma aldeia de caçadores. Fiquei lá três noites. Há muito tempo. …Vai." |
| `gorvan_dia_46` | `missao(H_12) == concluida && missao(H_19) != concluida` | triste | "O diário está na minha gaveta. Leio uma página por noite. Não mais. Não aguento mais." |
| `gorvan_dia_47` | `boss_derrotado(dragao_gelo)` | normal | "Metade da torre. Agora é que ela começa a contar. Conta tu também. Os passos." |
| `gorvan_dia_48` | `andar_maximo >= 53 && !flag(kai_salvo) && !boss_derrotado(kai)` | triste | "O Kai. Os que desaparecem às vezes voltam. Às vezes. Fica com o 'às vezes'." |
| `gorvan_dia_49` | `boss_derrotado(tita_magma) && missao(H_19) != concluida` | triste | "Setenta…" 🎬 Olha pela janela, para a torre. "Setenta e um, setenta e dois, setenta e três. Hmm." |
| `gorvan_dia_50` | `missao(H_19) == concluida` | feliz | "Dormi a noite toda. A primeira em vinte anos. Não contes à Lyra. Ela chora." |
| `gorvan_dia_51` | `missao(H_20) == concluida` | normal | "Às cinco, no campo. Os novatos tremem quando me veem. Bom sinal." |
| `gorvan_dia_52` | `andar_maximo >= 91` | normal | "Noventa e um. O registo da Guilda acaba aí. Escreve tu o resto." |
| `gorvan_dia_53` | `rank >= A` | normal | "Rank A. Agora as missões difíceis vêm de mim. Bate à porta. Não entres a correr." |
| `gorvan_dia_54` | `rank >= S` | feliz | "Rank S. Mais do que eu fui. Hmm. Ainda bem." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gorvan_dia_60` | `coracoes(gorvan) >= 2` | feliz | "Hmm." 🎬 Acena com a cabeça. (É um "olá" do Gorvan.) |
| `gorvan_dia_61` | `coracoes(gorvan) >= 3` | normal | "Comeste? A Dona Marta pergunta. Eu também pergunto. Por ela." |
| `gorvan_dia_62` | `coracoes(gorvan) >= 4` | normal | "{nome}." 🎬 Pausa. "Só isso. Estava a ver se me lembrava." |
| `gorvan_dia_63` | `coracoes(gorvan) >= 5` | feliz | "Guardo-te as missões boas. As más dou ao Kai. Ele nem nota." |
| `gorvan_dia_64` | `coracoes(gorvan) >= 6` | triste | "Às vezes conto os dias que estás lá em cima. Não devia. Conto." |
| `gorvan_dia_65` | `coracoes(gorvan) >= 8` | feliz | "Fiz chá. Fiz dois. Engano meu. Bebe." |
| `gorvan_dia_66` | `coracoes(gorvan) >= 10` | feliz | "O Gizmo quer fazer-me um braço de ferro. Com molas. Disse que não." 🎬 Pausa. "Disse 'talvez'." |
| `gorvan_dia_67` | `coracoes(gorvan) >= 10` | feliz | "Parceir{o/a}. Hmm. Soa bem. Não digo outra vez." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gorvan_dia_70` | `origem == jogador` | normal | "Falas de 'níveis' como quem fala do tempo. No teu mundo os mortos voltavam? Aqui não." |
| `gorvan_dia_71` | `origem == atrasado` | normal | "Chegas sempre a correr. Corre na torre. Aqui anda. Partes-me o chão." |
| `gorvan_dia_72` | `origem == ajudante` | normal | "Ajudas toda a gente. Bom. Lembra-te de te ajudar a ti. É mais difícil." |
| `gorvan_dia_73` | `origem == dormir` | triste | "Dormes bem? Eu não. Dorme por mim." |
| `gorvan_dia_74` | `skill_unica == olho_do_sistema` | normal | "Vês os números dos monstros. Eu só via os dentes. Chegava." |
| `gorvan_dia_75` | `skill_unica == segunda_vida` | zangado | "Levantas-te depois de cair. Uma vez por andar. Não é desculpa para caíres." |
| `gorvan_dia_76` | `skill_unica == lingua_universal` | normal | "Falas com monstros. Pergunta-lhes porquê. Eu nunca soube." |
| `gorvan_dia_77` | `skill_unica == coracao_de_dragao` | feliz | "Curas-te sozinh{o/a}. Hmm. Os braços também crescem?" 🎬 Pausa. "Estou a brincar. Acho." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `gorvan_curta_1` | normal | "Hmm." |
| `gorvan_curta_2` | normal | "Já falámos. Chega por hoje." |
| `gorvan_curta_3` | normal | "Mais? Não. Vai." |
| `gorvan_curta_4` | feliz | "A torre está à espera. Eu não. Vai." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Gorvan** *(normal)*: "Cem andares. Ninguém sabe quem a fez. Os que dizem que sabem estão a vender alguma coisa."
- **Gorvan** *(normal)*: "Há quem diga que ela está viva. Hmm. Os vivos cansam-se. A torre não se cansa."
- *(antes de H_19)* **Gorvan** *(triste)*: "Eu cheguei ao 74. Chega de torre."
- *(depois de H_19)* **Gorvan** *(normal)*: "Eu cheguei ao 74. Tu vais mais longe. Sobe por nós os dois."

### 4.2 O andar atual

O Gorvan fala da **região do andar mais alto** a que chegaste: conselhos curtos, de quem já lá esteve.

| Região | Fala |
|---|---|
| 1 Floresta | "Slimes, lobos, javalis. Fácil. É por ser fácil que se morre. Atenção." |
| 2 Cavernas | "Escuro. Se a tocha apagar, não corras. Para. Escuta. Depois corre." |
| 3 Pântano | "Lodo, veneno e Homens-Lagarto. Os relatórios dizem 'perigosos'. Os relatórios já se enganaram. Raramente." |
| 4 Deserto | "Água. Mais água. O sol mata mais do que os escorpiões. Os escorpiões ajudam." |
| 5 Gelo | "Frio. Não pares de te mexer. Os que param ficam lá. De pé. Vi-os." |
| 6 Oceano | "Água por cima da cabeça. Não sei nadar. Nunca precisei. Tu precisas." |
| 7 Vulcão | "Calor e lava. Não toques em nada que brilhe vermelho. Nem em ninguém." |
| 8 Reino Assombrado | *(antes de H_19)* 🎬 Toca no ombro. "…Não. Pergunta à Lyra." · *(depois)* "Mortos que andam. Leva luz. E leva-me a mim, se for preciso." |
| 9 Céu | "Ilhas no ar. Nunca lá fui. Não caias. Com um braço não apanho ninguém." |
| 10 Abismo | "Ninguém sabe. Ninguém. Escreve tudo. Depois volta e lê-mo." |

### 4.3 Rumores

O Gorvan **não conta mexericos: conta avisos**. Diz **1 por dia**. Muitos são pistas de missões e segredos.

| ID | Condição | Rumor |
|---|---|---|
| `gorvan_rumor_01` | — | "Rumores? Pergunta à Lyra. …Está bem. Um. O Brom canta quando está sozinho. Eu ouvi. Não digas." |
| `gorvan_rumor_02` | — | "O moinho do andar 1. Puxa a corda. Não perguntes como sei. Eu também fui novato." |
| `gorvan_rumor_03` | `andar_maximo >= 2` | "Andar 2, à noite. Um lobo com uma cicatriz. A Freya quer a pele dele. Vai com ela, não sozinh{o/a}." |
| `gorvan_rumor_04` | `andar_maximo >= 31` | "Há um acampamento antigo no 31. A Lyra sabe. Não sabe que eu sei que ela sabe." |
| `gorvan_rumor_05` | `andar_maximo >= 41` | "Há um mamute no gelo. Enorme. Calmo, se o deixares. Nem tudo o que é grande se tem de matar." |
| `gorvan_rumor_06` | `andar_maximo >= 44` | "O Yeti do 45 guarda brinquedos. A miúda das flores ia gostar de um. Não lhe digas que fui eu." |
| `gorvan_rumor_07` | `andar_maximo >= 45 && missao(H_12) == inativa` | "No 46 há um sino. Tocava sozinho, há vinte anos. Os caçadores diziam que era o vento. Não era." |
| `gorvan_rumor_08` | `andar_maximo >= 61` | "Acampamento das Cinzas, andar 61. Se vires o Kai, não lhe batas logo. Ouve primeiro." |
| `gorvan_rumor_09` | `andar_maximo >= 77` | "A Ordem da Luz, no 77. A Célia aprendeu lá. Leva-lhe uma carta. Ela não pede. Eu peço." |
| `gorvan_rumor_10` | `missao(N_GORVAN_3) == ativa && andar_maximo >= 81` | "Mármore Celeste. Cai das estátuas que andam, lá no céu. Andar 83, 86… Não é por nada. É por uma coisa." |
| `gorvan_rumor_11` | `rank >= C` | "O Rook vende coisas no Bairro Baixo. Eu não vi nada. Tu também não." |
| `gorvan_rumor_12` | `estacao == inverno` | "Antes do Festival da Estrela a Lyra pergunta a toda a gente do que é que eu gosto. Gosto que não perguntem. Diz-lhe." |
| `gorvan_rumor_13` | `missao(N_MIA_2) == concluida` | "A miúda das flores acerta numa maçã a vinte passos. Com uma pedra. Imagina com um arco. Eu imagino." |

### 4.4 A vida dele

| Corações | Fala |
|---|---|
| 0 | "Não." |
| 2 | "Nasci aqui. No Bairro Baixo. Cresci em cima da muralha. Fiquei grande. Fim." |
| 4 | "Vinte anos de Mestre da Guilda. Antes, quinze de aventureiro. Antes disso, um miúdo com um pau na Praça." |
| 6 | "Tinha uma equipa. Cinco. Eu era o escudo." 🎬 Toca no ombro. "O escudo devia ser o último a cair. Fui o único que não caiu." |
| 8 | *(depois de H_19)* "Não fugi. Mandaram-me ir. Há diferença. Levei vinte anos a perceber." · *(antes de H_19 repete a fala dos 6)* |
| 10 | "Volto a subir. Cinquenta e cinco anos e um braço. Os outros quatro iam rir-se. Deixa-os rir." |

---

## 5. Presentes

**Adora:** Chá Quente, armas antigas (do Arsenal do andar 79 e baús antigos), Machado do Gorvan (depois do andar 74) ·
**Gosta:** bebidas quentes, carne assada · **Detesta:** flores, doces. O resto é **neutro** (ver `docs/ITENS.md`, secção 11).
O Gorvan também detesta **"gente que desiste"**: nas escolhas de diálogo, as respostas de desistir dão **−30**.

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "Hmm." 🎬 Segura o presente muito tempo. "…Bom. Muito bom." · "Isto é bom. Não digas a ninguém que gostei. Tenho uma fama." |
| Gosta | "Obrigado. Serve." · "Hmm. Fica." |
| Neutro | "Hmm. Para que serve?" 🎬 Vira-o ao contrário. "Fica na gaveta. Com as luvas." · "Obrigado. Acho." |
| Não gosta | "Não. Mas obrigado pela intenção. A intenção conta. Pouco." |
| Detesta | "Flores. Não." 🎬 Olha para elas. "…Põe na secretária da Lyra." · "Doces. Não como doces. Dá às crianças do Bairro Baixo." |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Chá Quente | "Chá. Quente." 🎬 Pausa. "Há duas canecas na prateleira. Por acaso. Senta-te." |
| Machado do Gorvan | "O meu machado. Dei-to. Devolves-mo." 🎬 Pega nele com a mão esquerda. "Pesa o mesmo. Eu é que pesava mais. Fica na parede. É dos dois." |
| Arma antiga (qualquer) | "Ferro velho. Bom ferro. Faziam-se melhor antes. Eu também." |
| Assado de Javali | "Javali. Como de pé. Sentado demoro e a Lyra rouba-me." |
| Café da Selva | "Café. Forte. Não vou dormir. Já não dormia. Obrigado." |
| Ramo do Campo (da Mia) | "Flores. Não." 🎬 Pausa. "…Compraste à miúda da esquina? Pagaste bem? Então está bem." |
| Bolo (qualquer) | "Bolo. Não." 🎬 Pausa. "O meu bolo para a Lyra era torto. Este é direito. Fazes batota." |
| Gel de Slime | "Gel. No meu gabinete. Leva. Agora. Devagar. Não pinga." |

---

## 6. Aniversário e festivais

**Aniversário (Inverno, dia 20):**
- Sem presente: **Gorvan** *(normal)*: "Faço anos. A Lyra sabe. Vai haver um bolo torto. Eu finjo que não sei."
- Com presente que adora: **Gorvan** *(feliz)*: "Lembraste-te." 🎬 Pausa longa. "Obrigado. Não repito. Mas obrigado."
- Com outro presente: **Gorvan** *(normal)*: "Presente de anos. Hmm. Obrigado. Não faças disto um hábito."
- 🎬 Na Guilda há um bolo torto em cima do balcão, feito pela Lyra. O Gorvan come uma fatia de pé e diz: "Está torto. Está bom."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Flores. A cidade inteira cheira a flores. Vou para a muralha. Lá em cima cheira a vento." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Gorvan** *(zangado)*: "Não." 🎬 Pausa. *(surpresa)* "…Uma volta. Uma." ⚙ dança · +100 amizade (a dança dele é só rodar devagar) |
| F_02 Festival da Pesca | "Pescar. Sentado. Calado. Sem ninguém a falar." 🎬 Pausa. "Gosto. Só não digas ao Pip." |
| F_03 Noite dos Espíritos | "As crianças vêm à Guilda pedir doces. Primeiro dou-lhes medo. Depois doces. Por esta ordem." |
| F_04 Festival da Estrela | "Amigo secreto. Calhou-me a Lyra. Dei-lhe papel. Bom papel. Ela chorou. Não percebo." |
| F_04 (depois de receber o presente) | "Deram-me um cachecol. Disseram que era 'para o braço que tenho'. Uso-o no pescoço. Como toda a gente." |
| F_05 Dia da Subida | "Discursos. Hmm. Come. Bebe. Ouve o Lucien se tiveres coragem. Amanhã sobes." |
| F_06 Concurso da Casa | "Concurso de casas. Tem paredes? Tem teto? Ganhaste. Eu não sou jurado." |
| F_07 Noite das Lanternas (depois da cena 4 da Lyra) | *(antes de H_19)* "Quatro." 🎬 Põe quatro lanternas no rio, uma a uma. · *(depois)* "Quatro lanternas. Este ano estão direitas. A Ilsa ia gozar." |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`).

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `gorvan_boss_javali_rei` | "O porco grande. Hmm. Bom. Agora não comas três jantares para festejar." |
| Ent Ancião (10) | `gorvan_boss_ent_anciao` | "Andar 10. Há muitos anos que ninguém passava. Muitos. Não fiques vaidos{o/a}. Fica contente. É diferente." |
| Aranha-Mãe (15) | `gorvan_boss_aranha_mae` | "Uma aranha do tamanho de uma carroça. Odeio aranhas. Não digas a ninguém." |
| Golem de Cristal (20) | `gorvan_boss_golem_cristal` | "O Golem ajoelhou-se. Para a janela azul, não para ti. Lembra-te disso. Fica de pé." |
| Serpente do Lodo (25) | `gorvan_boss_serpente_lodo` | "Lodo nas botas. No meu gabinete. Limpa. Depois conta." |
| Hidra do Pântano (30) | `gorvan_boss_hidra_pantano` | "Cortas uma cabeça, nascem duas. Como os problemas da Guilda. Bom trabalho." |
| Escorpião Imperador (35) | `gorvan_boss_escorpiao_imperador` | "Veneno? Mostra o braço. …O teu. Está bem. Vai à Igreja na mesma." |
| Faraó Eterno (40) | `gorvan_boss_farao_eterno` | "Um Jogador feito rei. Feito múmia. A torre não devolve ninguém inteiro. Tu volta inteir{o/a}." |
| Yeti Ancião (45) | `gorvan_boss_yeti_anciao` | "Frio lá em cima. Ainda tens os dedos todos? Conta-os. Eu conto os meus. Cinco." |
| Dragão de Gelo (50) | `gorvan_boss_dragao_gelo` | "'Os outros vinham com amigos.' Contaram-me o que ele disse." 🎬 Pausa. "Não subas sozinh{o/a}. Eu subi acompanhado. Mesmo assim." |
| Capitão Esqueleto (55) | `gorvan_boss_capitao_esqueleto` | "Piratas mortos. A torre tem imaginação. Pena que seja assim." |
| Leviatã (60) | `gorvan_boss_leviata` | "Venceste o mar. O Kai não voltou. Ainda. 'Ainda' é uma palavra importante. Guarda-a." |
| Ferreiro Infernal (65) | `gorvan_boss_ferreiro_infernal` | "O Brom veio beber chá comigo. Não disse nada. Eu também não. Foi boa conversa." |
| Kai — salvo (68) | `gorvan_boss_kai_salvo` | "O rapaz voltou." 🎬 Coça a barba. "Bom. Bom. Diz-lhe que tem uma missão atrasada. De há meses." |
| Kai — vencido (68) | `gorvan_boss_kai_vencido` | "Não precisas de falar. Senta-te. Eu também perdi gente lá em cima. Senta-te só." |
| Titã de Magma (70) | `gorvan_boss_tita_magma` | "Setenta." 🎬 Olha para a torre durante muito tempo. "…Faltam quatro." |
| Lich Bibliotecário (75) | `gorvan_boss_lich_bibliotecario` | "Setenta e cinco. Mais alto do que nós. Mais alto do que eu. Continua. Por favor." |
| Rei Sem Coroa (80) | `gorvan_boss_rei_sem_coroa` | (depois da cena da história em Ascendia) "Amanhã, às cinco, no campo de treino. Não te atrases. Eu não me atraso. Já não." |
| Grifo Real (85) | `gorvan_boss_grifo_real` | "Andar 85. Não sei nada daí. É bom não saber. Conta-me tudo. Devagar." |
| Serafim Caído (90) | `gorvan_boss_serafim_caido` | "Estás calad{o/a}. Lá em cima disseram-te uma coisa pesada. Vê-se nos ombros. Não contes. Senta-te." |
| Guardião do Tempo (95) | `gorvan_boss_guardiao_tempo` | "Noventa e cinco. O Edrik ia gostar de ver isto. Ele dizia que o topo existia. Eu dizia que era teimosia." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — O campo vazio

| | |
|---|---|
| ID | `cena_gorvan_2` |
| Quando | 2 ❤️ · entrar no campo de treino entre as 19:00 e as 20:00, sem chuva |
| Onde | campo de treino da Guilda, ao pôr do sol |
| Quem | herói, Gorvan |
| Música | silêncio → `guilda` (versão lenta, só violoncelo) |

🎬 O campo está vazio. O Gorvan, sem a capa, segura um machado de treino pesado com a mão esquerda.
🎬 Ataca um boneco. Uma vez. Duas. À terceira, o peso do machado puxa-o para o lado e ele cai sobre um joelho.
🎬 Vê o herói. Levanta-se devagar. Não larga o machado.

- **Gorvan** *(zangado)*: "Há quanto tempo estás aí?"

▶ **"Acabei de chegar."**
▶ **"O tempo suficiente."**
▶ *(não dizer nada)*

- *(Acabei de chegar)* **Gorvan** *(normal)*: "Mentira. Bom. Mentes por educação."
- *(O tempo suficiente)* **Gorvan** *(normal)*: "Hmm. Honest{o/a}. É pior. Gosto mais." ⚙ +30
- *(nada)* 🎬 O Gorvan olha muito tempo e depois acena. **Gorvan** *(normal)*: "…Bom." ⚙ +30
- **Gorvan** *(normal)*: "Treino aqui quando os novatos vão jantar. Um braço. O machado ainda acha que são dois."
- 🎬 Ataca outra vez. Desta vez não luta contra o peso: deixa o machado rodar e roda com ele. Um golpe giratório limpo. O boneco parte-se ao meio.
- **Gorvan** *(feliz, quase)*: "Hmm. Esse saiu."

▶ **"Ensinas-me esse golpe?"**
▶ **"Precisas de ajuda?"**

- *(Ensinas-me)* **Gorvan** *(normal)*: "Não." 🎬 Pausa. "…Ainda não. Um dia." ⚙ +30
- *(Ajuda)* **Gorvan** *(zangado)*: "Para bater num boneco? Não." 🎬 Olha para o boneco partido. "…Para o levantar, sim. Pega aí."
- **Gorvan** *(normal)*: "Ninguém sabe que treino. Fica assim. Entre nós e os bonecos."

⚙ O **Treino** do Gorvan (quando abrir, depois de H_20) fica 5% mais barato. Flag `gorvan_treino_segredo`.

### ❤️ 4 — O braço que dói

| | |
|---|---|
| ID | `cena_gorvan_4` |
| Quando | 4 ❤️ · subir à muralha norte entre as 21:00 e as 24:00 numa noite fria (`estacao == inverno` ou `clima == chuva`) |
| Onde | muralha norte, por cima do Bairro da Guilda |
| Quem | herói, Gorvan |
| Música | `ascendia_noite` (versão só vento e violoncelo) |

🎬 O Gorvan está sentado na ameia, a olhar para a torre. Esfrega o ombro direito, devagar.

- **Gorvan** *(normal)*: "Sobe. Senta-te. Não caias. Já perdi gente suficiente."
- 🎬 Silêncio. As janelas dos primeiros andares da torre piscam ao longe, como estrelas baixas.
- **Gorvan** *(triste)*: "Com frio, dói. O braço. O que não está cá."
- **Gorvan** *(normal)*: "A Célia diz que é normal. 'O corpo lembra-se.' Hmm. O corpo devia esquecer. Eu tento."

▶ **"Como o perdeste?"**
▶ **"Dói muito?"**
▶ *(esperar)*

- *(Como)* **Gorvan** *(normal)*: "Perguntas direitas. Hmm."
- *(Dói muito?)* **Gorvan** *(triste)*: "Menos do que o resto." ⚙ +30
- *(esperar)* 🎬 Passa muito tempo. O Gorvan fala sozinho, sem olhar para o herói. ⚙ +30
- **Gorvan** *(normal)*: "Andar 74. Uma coisa feita de ossos. Pus o braço à frente."
- **Gorvan** *(normal)*: "Os ossos fecharam-se. O braço ficou lá. Eu vim cá para baixo."
- 🎬 Toca no ombro.
- **Gorvan** *(zangado, baixo)*: "Chega. Hoje não pergunto mais a mim próprio."
- 🎬 Tira do bolso da capa um cantil e uma caneca de lata amolgada. Enche-a e dá-a ao herói.
- **Gorvan** *(normal)*: "Chá. Quente. A única coisa que ajuda. Faz-se assim. Bagas de inverno, água, paciência."
- **Gorvan** *(feliz, quase)*: "Agora sabes o que me dar. Hmm. Erro meu."

⚙ Recebe a receita **Chá Quente** (se ainda não a tiveres) ou **Chá Quente** ×5.
⚙ A partir daqui, o Gorvan chama-te `{nome}`.

### ❤️ 6 — Quatro nomes num papel

| | |
|---|---|
| ID | `cena_gorvan_6` |
| Quando | 6 ❤️ · `missao(H_12) == concluida` · entrar no gabinete da Guilda de manhã (8:00–12:00) |
| Onde | gabinete do Gorvan, na Guilda |
| Quem | herói, Gorvan |
| Música | `guilda` → silêncio |

🎬 O diário da equipa (capa de couro, páginas onduladas pela neve) está aberto em cima da secretária.
🎬 Ao lado, uma folha com quatro nomes escritos em letras grandes e tortas. Escritos com a mão esquerda.

- **Gorvan** *(normal)*: "Senta-te."
- **Gorvan** *(normal)*: "Li o diário todo. Devagar. A Odília escrevia mal. Eu escrevo pior. Olha."
- 🎬 Empurra a folha para o herói. O ecrã mostra-a: *Edrik · Odília · Teodoro · Ilsa*.
- **Gorvan** *(triste)*: "Não os leio em voz alta. Ainda não. Lê tu. Por dentro."
- **Gorvan** *(normal)*: "No registo da Guilda estão. Num livro fechado. Numa gaveta. Ninguém lá passa."
- **Gorvan** *(normal)*: "Quero-os numa pedra. Na Praça. Onde as pessoas passam e tropeçam neles."
- **Gorvan** *(normal)*: "A pedra daqui gasta-se. A chuva come as letras. Lá em cima, no céu, há uma pedra que não se gasta."
- **Gorvan** *(normal)*: "Mármore Celeste. Ainda não chegaste lá. Eu sei. Esperei vinte anos. Espero mais."

▶ **"Vou trazer-ta."**
▶ **"Porque não a vais buscar tu?"**
▶ **"Isso é muito longe. Desisto já."**

- *(Vou)* **Gorvan** *(normal)*: "Hmm." 🎬 Acena. "Bom." ⚙ +30
- *(Porque não)* **Gorvan** *(zangado → triste)*: "Porque não subo." 🎬 Pausa. "…Ainda." ⚙ +30
- *(Desisto)* **Gorvan** *(zangado)*: "Não digas isso nesta sala. Nunca." ⚙ −30 → **Gorvan** *(normal)*: "Trazes quando puderes. Não há pressa."
- **Gorvan** *(normal)*: "Outra coisa. A Dona Marta diz que às vezes jantas em casa. Se houver jantar… eu levo o chá."

⚙ Missão **N_GORVAN_3 Nomes na Pedra** iniciada. O Gorvan aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — Os Imortais

| | |
|---|---|
| ID | `cena_gorvan_8` |
| Quando | 8 ❤️ · `missao(H_19) == concluida` · subir à muralha norte entre as 21:00 e as 24:00, sem chuva |
| Onde | muralha norte |
| Quem | herói, Gorvan |
| Música | `tema_gorvan` (violoncelo e tambor lento) |

🎬 O Gorvan está sentado na ameia. Ao lado, cinco canecas de lata em fila. Quatro estão cheias de chá. Uma está vazia.

- **Gorvan** *(normal)*: "Senta-te. Essa é a tua." 🎬 Enche a caneca vazia.
- **Gorvan** *(normal)*: "Lá em baixo, no 74, não lhes disse adeus. Não sei dizer. Disse 'volto'."
- **Gorvan** *(normal)*: "Hoje quero falar deles. Não do fim. Deles."
- 🎬 Toca na primeira caneca.
- **Gorvan** *(normal)*: "O Edrik. Ia sempre à frente. Era Jogador, como tu. Número nove mil novecentos e sessenta e um."
- **Gorvan** *(feliz)*: "Escolhia sempre o caminho mais difícil. 'Os fáceis já estão gastos', dizia. Irritava-me. Tinha razão."
- 🎬 Segunda caneca.
- **Gorvan** *(feliz)*: "A Odília. Maga. Fazia os mapas e mandava em todos. Chamava-me 'teimoso'. Tinha sempre frio."
- 🎬 Terceira caneca.
- **Gorvan** *(feliz)*: "O Téo. Teodoro. Curandeiro. Contava piadas tão más que os monstros fugiam. Tocava flauta à fogueira."
- 🎬 Quarta caneca. A mão fica parada em cima dela.
- **Gorvan** *(triste)*: "A Ilsa. A mais nova. Arqueira. Dezassete anos. Ia sempre atrás, 'para ver tudo'."
- **Gorvan** *(feliz)*: "Ria-se tão alto que a torre inteira sabia onde estávamos."
- **Gorvan** *(normal)*: "Chamávamo-nos 'Os Imortais'. Ideia do Téo. Votámos todos contra. Ganhou na mesma."
- 🎬 O Gorvan ri-se. A sério, com a barriga. Uma vez só.
- **Gorvan** *(normal)*: "A espada de treino que te dei no primeiro dia. Era do Edrik. A de quando ele chegou."
- **Gorvan** *(normal)*: "Guardei-a vinte anos. À espera de um Jogador que valesse a pena. Ou de um número redondo."
- **Gorvan** *(feliz, quase)*: "Calhou seres as duas coisas."
- *(se ainda tiveres a Espada de Treino)* 🎬 O herói mostra a espada. O Gorvan olha muito tempo para ela. **Gorvan** *(triste)*: "Ainda a tens. Hmm. Ele ia gostar."
- *(se já não a tiveres)* **Gorvan** *(normal)*: "Vendeste-a? Hmm. Ele também a teria vendido. Por pão."
- *(se `missao(N_MIA_2) == concluida`)* **Gorvan** *(normal)*: "E o arco pequeno que dei à miúda das flores… era o da Ilsa. O de quando aprendeu. Tinha onze anos."
  **Gorvan** *(normal)*: "Não lhe digas. Um dia digo eu."

▶ **"Obrigad{o/a} por me contares."**
▶ **"Eles iam gostar de te ver rir."**
▶ *(levantar a caneca)*

- *(Obrigado)* **Gorvan** *(normal)*: "Não agradeças. Bebe. Arrefece." ⚙ +30
- *(Rir)* **Gorvan** *(triste → feliz)*: "Iam gozar comigo. Uma semana inteira. Deixa-os." ⚙ +30
- *(caneca)* 🎬 O Gorvan levanta a dele. Os dois brindam às quatro canecas cheias. 🎥 A câmara afasta-se: duas figuras na muralha, cinco canecas, a torre ao fundo. ⚙ +30

⚙ O Treino fica 15% mais barato. O Gorvan passa a mandar **cartas** (1 por semana), sempre com a mesma frase:
*"Chá. — G."* e um presente: Chá Quente ×3, Poção de Vida G ×2 ou uma arma antiga.
⚙ A missão **N_GORVAN_3** passa a mostrar os nomes no Diário de missões.

### ❤️ 10 — Voltamos vivos

| | |
|---|---|
| ID | `cena_gorvan_10` |
| Quando | 10 ❤️ · `missao(H_20) == concluida && missao(N_GORVAN_3) == concluida` · entrar na Praça ao amanhecer (5:00–7:00) |
| Onde | Praça da Torre, junto à **Pedra dos Nomes** (ao lado da fonte) |
| Quem | herói, Gorvan, Lyra (no fim) |
| Música | `tema_gorvan` (versão completa) |

🎬 Névoa da manhã. A Praça está vazia. O Gorvan está de pé em frente à Pedra dos Nomes.
🎬 Tem vestida uma armadura velha e amolgada que ninguém via há vinte anos. Um machado ao ombro.

- **Gorvan** *(normal)*: "Cedo. Bom."
- **Gorvan** *(normal)*: "Todas as manhãs venho aqui. Digo-lhes bom dia. Não respondem. São educados."
- 🎬 Passa os dedos pela pedra, nome a nome.
- **Gorvan** *(normal)*: "Ontem perguntei-lhes uma coisa. O que fariam no meu lugar."
- **Gorvan** *(feliz)*: "O Edrik dizia 'sobe'. A Odília dizia 'sobe, teimoso'. O Téo contava uma piada. A Ilsa ria-se."
- **Gorvan** *(feliz)*: "Hmm. Maioria."
- 🎬 Vira-se para o herói.
- **Gorvan** *(normal)*: "Vou subir. Contigo. Se me quiseres."
- **Gorvan** *(normal)*: "Um braço. Cinquenta e cinco anos. Rabugento. Não sou boa companhia."
- **Gorvan** *(normal)*: "Mas sou um bom escudo. Ainda."

▶ **"Quero."**
▶ **"Tens a certeza?"**
▶ **"Só se prometeres voltar vivo."**

- *(Quero)* **Gorvan** *(feliz)*: "Hmm." 🎬 O canto da boca sobe. "Bom."
- *(Tens a certeza?)* **Gorvan** *(normal)*: "Não. Há vinte anos tinha a certeza. Prefiro assim."
- *(Prometer)* **Gorvan** *(surpresa)*: "Essa regra é minha. Roubaste-ma." 🎬 Pausa. "…Prometo."
- 🎬 O Gorvan tira de dentro da capa um machado mais pequeno e dá-o ao herói.
- **Gorvan** *(normal)*: "Este é teu. Fê-lo o Brom. Eu pedi. Tem cinco marcas no cabo."
- **Gorvan** *(normal)*: "Quatro são deles. A quinta é tua. Eu não preciso de marca. Eu vou lá estar."
- **Gorvan** *(normal)*: "E isto. Ninguém mo ensinou. Aprendi sozinho, com um braço, a cair muitas vezes."
- 🎬 Faz o golpe giratório no ar, devagar, para o herói ver. Depois mais depressa.
- **Gorvan** *(feliz)*: "Agora é teu."
- 🎬 Passos a correr. A Lyra chega de casaco por cima do pijama, com os óculos tortos.
- **Lyra** *(surpresa)*: "MESTRE! Disseram-me que… vai SUBIR? E quem é que assina os papéis?!"
- **Gorvan** *(normal)*: "Tu."
- **Lyra** *(normal)*: "…Eu, pois."
- 🎬 O Gorvan olha para a torre. Depois para o herói.
- **Gorvan** *(normal)*: "Volta viv{o/a}." 🎬 Pausa. "Não. Voltamos vivos. Os dois."

⚙ O Gorvan pode ser **companheiro** (tanque com machado; skill de companheiro **Golpe Giratório**; ver `docs/NPCS.md`, secção 4).
⚙ Aprendes a skill **Técnica do Braço Único** (golpe giratório). Recebes o **Machado da Equipa** (ver `docs/ARMAS.md`, secção 8).
⚙ Título *Um dos Imortais*. O Gorvan passa a ter as falas `gorvan_dia_66` e `gorvan_dia_67`. No epílogo, lidera expedições outra vez
(ver `docs/HISTORIA.md`, secção 7).

---

## 9. Missões

### N_GORVAN_1 — Prova de Força (0 ❤️, depois de H_03)

- **Pedir** (no campo de treino, 17:00–20:00) — **Gorvan** *(normal)*: "Três bonecos. Trinta segundos. Partes os três, ganhas uma coisa. Não partes, partes tu."
  ▶ **"Aceito."** ⚙ missão iniciada · ▶ **"Agora não."** → "Hmm. Os bonecos esperam. Eu também. Pouco."
- **Regra**: vencer **3 bonecos de treino em 30 s** (os bonecos têm HP de um Slime nível 3 e não atacam; o 3.º só aparece quando o 2.º cai).
- **Falhar** — **Gorvan** *(normal)*: "Lento. Outra vez."
  ▶ **"Outra vez."** → "Bom." · ▶ **"Desisto."** → **Gorvan** *(zangado)*: "Desistes? Aqui não. Respira. Outra vez." ⚙ −30
- **Entregar** — **Gorvan** *(normal)*: "Hmm. Vinte e tal segundos. O Kai fez em dezanove." 🎬 Pausa. "Mentira. Fez em trinta e um."
  ⚙ **Faixa de Aprendiz** (+5% ATQ) · +100 amizade

### N_GORVAN_2 — A Escolha (nível 10, e outra vez nos níveis 40 e 70)

- **Pedir** — aparece sozinha no nível 10 (`[Sistema] Atingiste o nível 10. Fala com o Mestre Gorvan para escolher uma classe.`).
  - **Gorvan** *(normal)*: "Nível 10. Hmm."
  - **Gorvan** *(normal)*: "Até hoje eras 'aventureiro'. Uma palavra que serve para tudo. Agora escolhe uma que sirva para ti."
  - **Gorvan** *(normal)*: "Escolhe."
- ⚙ Abre o ecrã das classes (4 classes base; cada uma mostra as armas preferidas e as 6 skills).
- **Confirmar** — ▶ **"Escolho esta."** → fala da classe (tabela abaixo) · ▶ **"Deixa-me pensar."** → "Pensa. A classe não foge. Tu também não."
- **Entregar** — **Gorvan** *(normal)*: "Pronto. Agora és isso. Treina. Volta no nível 40." ⚙ classe · +100 amizade (só no nível 10)
- **Evoluir (níveis 40 e 70)** — **Gorvan** *(normal)*: "Nível {nivel}. Cresceste. Dois caminhos. Um de cada vez."

| Classe | Nível | O Gorvan diz |
|---|---|---|
| Espadachim | 10 | "Espada. Rápida. Honesta. Bom começo." |
| Arqueiro | 10 | "Arco. Ficas atrás e vês tudo. Alguém tem de ver tudo." |
| Mago | 10 | "Magia. Não percebo. Não é preciso. Não te queimes." |
| Tanque | 10 | "Escudo. Ficas à frente. Levas com tudo." 🎬 Pausa. "Eu era isto. Boa escolha. Má vida." |
| Cavaleiro | 40 | "Cavaleiro. Armadura e honra. As duas pesam. Habitua-te." |
| Mestre de Lâminas | 40 | "Mais lâminas. Mais depressa. Não te cortes." |
| Atirador | 40 | "Um tiro. Certo. Não precisas de mais." |
| Ranger | 40 | "Bichos e armadilhas. O Zed vai gostar de ti. O Zed não gosta de ninguém." |
| Arquimago | 40 | "Mais fogo. Mais gelo. Mais raios. Menos sobrancelhas." |
| Necromante | 40 | "Mortos." 🎬 Pausa longa. "Trata-os bem. Já sofreram que chegue." |
| Guardião | 40 | "Guardião. Proteges os outros. Lembra-te de te proteger a ti. Eu não me lembrei." |
| Berserker | 40 | "Fúria. Serve. Até deixar de servir. Aprende a parar." |
| Paladino | 70 | "Luz. A Célia vai rezar por ti. Deixa-a. Faz-lhe bem." |
| Santo da Espada | 70 | "Santo. Hmm. Corta como quiseres. Eu não rezo a ninguém." |
| Olho de Falcão | 70 | "Vês através das paredes. Eu só via através das pessoas. Menos útil." |
| Senhor da Floresta | 70 | "Chamas um Ent. A Árvore-Mãe ia gostar. Ou não. Não perguntes." |
| Sábio dos Elementos | 70 | "Buracos negros. No meu campo de treino não. Nunca." |
| Rei dos Mortos | 70 | "Rei dos Mortos." 🎬 Toca no ombro. "Os meus deixa-os dormir." |
| Fortaleza Viva | 70 | "Fortaleza. Eu fui muralha. Tu és montanha. Hmm. Bom." |
| Senhor da Guerra | 70 | "Senhor da Guerra. Lembra-te: a guerra acaba. Tu ficas. Fica bem." |

### N_GORVAN_3 — Nomes na Pedra (6 ❤️, depois da cena de 6 ❤️)

- **Passos**:
  1. Trazer **1 Mármore Celeste** (cai dos Golems Celestes dos andares 83, 86, 89 e 90; ver `docs/regioes/r09_ceu.md`).
  2. Levar o mármore ao **Brom** para o cortar. **Brom**: "Pedra não é ferro. …Dá cá. Três dias. E não me olhes assim."
  3. Três dias depois, à noite (22:00–24:00), ir à Praça. O Gorvan está lá com um cinzel e um martelo.
  4. **Gravar os nomes**: o Gorvan não consegue segurar o cinzel e bater ao mesmo tempo.
     - **Gorvan** *(normal)*: "Seguras tu o cinzel. Eu bato. Não tremas. Eu também não."
     - ⚙ Minijogo curto de ritmo (4 batidas por nome, ver `docs/ATIVIDADES.md`, secção 4.7). Não se pode falhar: as batidas fora de tempo só deixam a letra mais torta.
- **Durante** — **Gorvan** *(normal)*: "Mármore Celeste. Lá de cima. Não há pressa." 🎬 Pausa. "Há um bocadinho de pressa."
- **Entregar** — 🎬 A pedra está no lugar, ao lado da fonte. Quatro nomes, um pouco tortos.
  - **Gorvan** *(normal)*: "Agora digo-os em voz alta. Uma vez. Para a cidade ouvir."
  - **Gorvan** *(normal)*: "Edrik. Odília. Teodoro. Ilsa."
  - 🎬 Silêncio. Um gato sobe à pedra e senta-se em cima do nome da Ilsa.
  - **Gorvan** *(feliz)*: "Hmm. Ela ia gostar disso."
  - ⚙ **Pedra dos Nomes** na Praça (fica para sempre) · +200 amizade · flag `pedra_dos_nomes`

### Missões da história (falas enquanto estão ativas)

As cenas grandes destas missões estão nos guiões dos capítulos (`docs/guiao/`). Aqui ficam só as falas do **Conversar**.

| Missão | Estado | Fala |
|---|---|---|
| H_08 Ordem da Guilda | ativa | "Andar 24. Homens-Lagarto. Os relatórios dizem que atacam caravanas. Expulsa-os." 🎬 Pausa. "Se os relatórios estiverem errados, traz provas. Não opiniões." |
| H_12 O Diário de Gorvan | pronta (tens o diário) | 🎬 O Gorvan vê o diário na mão do herói e levanta-se devagar. → começa a cena do guião (capítulo 5) |
| H_19 O Passado de Gorvan | ativa, antes de descer | "Amanhã. Seis da manhã. Cristal Mestre. Traz luz. Eu trago o resto." |
| H_19 | ativa, no andar 74 (companheiro) | frases de combate: "Atrás de mim." · "Luz! Mais luz!" · "Essa parede mexe-se. Não confies nela." · "Ainda estou de pé. Continua." |
| H_20 O Que Tentou Parar a Torre | ativa | "O rei do 80. Dizem que tentou parar a torre. Ouve o que ele tem para dizer. Depois bate-lhe." |

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gorvan_estado_vida` | `vida_pct < 30` | zangado | "Estás a sangrar. Igreja. Agora. Não discutas comigo." |
| `gorvan_estado_maldito` | `estado(amaldicoado)` | normal | "Roxo à volta da cabeça. Maldição. A Célia tira isso. Eu não toco." |
| `gorvan_estado_cansado` | `estado(cansado)` | zangado | "Olheiras. Dorme. Os cansados são os primeiros a não voltar." |
| `gorvan_estado_molhado` | `estado(encharcado)` | normal | "Pingas no meu chão. …Senta-te ao pé da lareira. Dez minutos." |
| `gorvan_estado_sapo` | `estado(sapo)` | normal | "Um sapo. Com a tua mochila." 🎬 Pausa. "Já vi pior. Já fui pior." |
| `gorvan_morreu` | 1.ª conversa depois de morrer na torre | zangado | "Morreste. A regra era uma. Uma." 🎬 Pausa. "…Ainda bem que voltaste. Não morras outra vez." |
| `gorvan_arma_nova` | arma equipada pela 1.ª vez com raridade Épica ou melhor | normal | "Arma nova. Bonita. Bonito não corta. Treina com ela." |
| `gorvan_machado` | `arma_tipo == machado` (1.ª vez) | feliz | "Machado. Hmm." 🎬 Quase sorri. "Segura mais em baixo. Assim. Bom." |
| `gorvan_animal` | `animal != nenhum` (1.ª vez) | normal | "Um bicho. Dá-lhe de comer antes de comeres tu. Ele não sabe pedir." |
| `gorvan_comp_mia` | `companheiro(mia)` | feliz | "A miúda. Arco firme." 🎬 Pausa. "Cuida dela. Ela cuida de ti. Não lhe digas que eu disse." |
| `gorvan_comp_kai` | `companheiro(kai)` | normal | "Os dois números. Não corram lá em cima. Ganha quem chega. Não quem chega primeiro." |
| `gorvan_comp_ssark` | `companheiro(ssark)` | normal | "Ssark. Hmm. Ainda bem que não cumpriste a minha ordem." |
| `gorvan_classe` | 1.ª conversa depois de escolher ou evoluir a classe | normal | "Fica-te bem. Agora usa." |
| `gorvan_nivel_10` | `nivel >= 10` e ainda sem classe | normal | "Nível 10. Vem cá. Temos de falar. Pouco." |
| `gorvan_rank` | 1.ª conversa depois de subir de rank | normal | "Rank novo. A Lyra já te deu os parabéns três vezes. Eu dou uma. Parabéns." |

### Serviço

**Classe** (níveis 10, 40 e 70: ver N_GORVAN_2) · **Missões de rank alto**: as missões fixas de rank **A, S e SS** (`G_A_01` a `G_SS_03`)
são entregues pelo Gorvan, no gabinete, e não pela Lyra · **Treino** (depois de H_20): **Aula do Mestre**, 1 por dia, das 17:00 às 20:00,
500 ouro (com os descontos das cenas 2 e 8). É um combate de treino de 60 s contra o Gorvan: cada golpe que acerta dá **5 pontos**
de *Manejo* da arma equipada, em vez de 1 (ver `docs/PROGRESSAO.md`, secção 4).

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `gorvan_serv_abrir` | abrir o menu | normal | "Hmm. Classe, missões ou treino?" (antes de H_20: "Classe ou missões?") |
| `gorvan_serv_classe_cedo` | `nivel < 10` | normal | "Nível 10. Depois falamos." |
| `gorvan_serv_classe_feito` | não há evolução nova | normal | "Já escolheste. Agora vive com isso. Até ao nível {proximo}." |
| `gorvan_serv_missoes` | `rank >= A` | normal | "Missões que a Lyra não põe no quadro. Lê com atenção. Duas vezes." |
| `gorvan_serv_missoes_nao` | `rank < A` | normal | "Rank {rank}. Estas são para rank A. Volta com mais." |
| `gorvan_serv_treino_nao` | antes de H_20 | normal | "Treino? Não treino ninguém." 🎬 Pausa. "…Ainda." |
| `gorvan_serv_treino` | começar a aula | normal | "Pega na arma. Ataca. Não pares até eu dizer." |
| `gorvan_serv_treino_fim` | fim da aula | feliz | "Hmm. Melhor. Amanhã outra vez." |
| `gorvan_serv_treino_feito` | já tiveste aula hoje | normal | "Uma aula por dia. O corpo também tem de aprender a dormir." |
| `gorvan_serv_dinheiro` | sem ouro para a aula | normal | "Sem ouro. A Guilda não vive de 'Hmm'. Volta amanhã." |
| `gorvan_serv_fechado` | na muralha, à noite | normal | "Aqui não há Guilda. Só muro. Amanhã." |
