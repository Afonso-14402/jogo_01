# Capitã Freya — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.12. Dados: `dados/dialogos/freya.json`. Arena: `docs/LOJAS.md`, secção 2.16 e `docs/ATIVIDADES.md`.
A amizade com a Freya **muda com as escolhas do Rook** (N_ROOK_3: `docs/dialogos/rook.md`).

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | graves, secos, curtos; como ordens |
| Como fala | direta, frases de soldado; elogia pouco e a sério; humor seco que ninguém percebe que é humor |
| Repete | "Mostra-me.", "Bom trabalho. Não te habitues.", "Se vires o Rook, diz-me." |
| Tiques | bate com a ponta da lança no chão quando acaba uma conversa (animação `bater_lanca`) |
| Nunca diz | que tem medo; que sente falta da torre (até aos 8 corações) |
| Chama ao herói | "recruta" até ao rank C; "aventureir{o/a}" até ao rank A; `{nome}` com rank A ou 6+ corações |
| Quem é | 35 anos. Ex-aventureira **rank S** (chegou ao andar 62). Há 8 anos deixou de subir para defender a cidade dos monstros que fogem pela torre |
| Rotina | Quartel 7:00–18:00 · patrulha 18:00–21:00 (anda pelas ruas, aparece em sítios diferentes) · sábado e domingo: Arena 10:00–18:00 |

---

## 2. Primeira conversa

- **Capitã Freya** *(normal)*: "Recruta. O número dez mil. Ouvi falar. Mostra-me o que sabes."
- **Capitã Freya** *(normal)*: "Não, a sério. Mostra." 🎬 Atira-lhe um boneco de treino. "Três golpes. Agora."
- 🎬 O herói bate no boneco (3 golpes).
- **Capitã Freya** *(normal)*: "Hm. Postura má. Força razoável. Coragem a mais. Vais viver. Talvez."
- **Capitã Freya** *(normal)*: "Eu caço monstros que fogem da torre para a cidade. E os que têm nome, lá em cima. Quando tiveres rank, há trabalho."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Caças · Arena · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `freya_dia_01` | `hora entre 7 e 9` | normal | "Treinei duas horas antes de abrires os olhos. Não é uma crítica. É um facto." |
| `freya_dia_02` | `hora entre 18 e 21` | normal | *(patrulha)* "Patrulha. Ruas limpas, portas fechadas, Rook escondido. A ordem natural das coisas." |
| `freya_dia_03` | — | normal | "Mostra-me o que sabes. Não, a sério. Mostra." |
| `freya_dia_04` | — | normal | "Se vires o Rook, diz-me. Se não vires, também diz." |
| `freya_dia_05` | — | feliz | "O Lucien cantou uma canção sobre mim. Rimou 'Freya' com 'cadeia'. Prendi-o uma hora. Por rima ilegal." |
| `freya_dia_06` | — | normal | "Ontem entrou um slime na padaria. Um slime. Na padaria. Tenho dezassete guardas e foi a Mia que o tirou com uma vassoura." |
| `freya_dia_07` | — | normal | "A diferença entre um aventureiro e um guarda? O aventureiro sobe. O guarda fica. Alguém tem de ficar." |
| `freya_dia_08` | — | normal | "Não confio em gente que sorri muito. Tu sorris pouco. Bom." |
| `freya_dia_09` | `dia_semana == sabado \|\| dia_semana == domingo` | feliz | *(na Arena)* "Fim de semana. Arena. O único sítio onde se pode bater em alguém e no fim apertar-lhe a mão." |
| `freya_dia_10` | `dia_semana == segunda` | normal | "Segunda-feira. Relatórios. Odeio relatórios. A Lyra adora relatórios. Faço-os para a ver contente." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `freya_dia_20` | `estacao == primavera` | normal | "Primavera: os monstros acasalam e fogem mais. Duplo turno." |
| `freya_dia_21` | `estacao == verao` | feliz | "Verão. Treino no rio. A armadura aquece tanto que se podia fritar um ovo. Já fritei." |
| `freya_dia_22` | `estacao == inverno` | normal | "No inverno os monstros de gelo descem. Gosto do inverno. Os inimigos de gelo partem-se com mais facilidade." |
| `freya_dia_23` | `clima == chuva` | normal | "Chuva. A lança escorrega. Treina com chuva. No dia em que precisares, vai chover." |
| `freya_dia_24` | `clima == trovoada` | feliz | "Trovoada. O meu tempo preferido. A Lança Relâmpago… um dia. Um dia." |
| `freya_dia_25` | `clima == nevoeiro` | zangado | "Nevoeiro. O Rook adora nevoeiro. Eu detesto nevoeiro. Não é coincidência." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `freya_dia_40` | `rank < D` | normal | "Rank F e E não caçam comigo. Sobe de rank. Depois falamos de monstros com nome." |
| `freya_dia_41` | `rank >= D` | normal | "Rank D. Já podes ir à Arena de bronze. Se perderes, não chores. Se ganhares, não te gabes." |
| `freya_dia_42` | `missao(H_08) == concluida && flag(sssar_defendida)` | normal | "Desobedeceste à Guilda. Eu não te prendo por isso. Desobedecer pela coisa certa não é crime. É raro." |
| `freya_dia_43` | `andar_maximo >= 62` | triste | "Passaste o 62. O meu recorde. Há oito anos que olho para esse número. Agora é teu. Ainda bem." |
| `freya_dia_44` | `rank >= S` | feliz | "Rank S. Como eu. Não. Melhor do que eu: eu parei. Tu não." |
| `freya_dia_45` | `missao(H_14) == concluida && missao(H_16) != concluida` | normal | "O Kai desapareceu. Mandei patrulhas às Zonas Seguras até ao 60. Nada. Continuo a mandar." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `freya_dia_60` | `coracoes(freya) >= 2` | normal | "Tens a postura melhor. Não é um elogio. É uma observação. …Está bem, é um elogio." |
| `freya_dia_61` | `coracoes(freya) >= 4` | feliz | "Os meus guardas perguntam se és meu aprendiz. Eu digo que não. Que és meu colega. Ficam assustados." |
| `freya_dia_62` | `coracoes(freya) >= 6` | normal | "{nome}. Quando subires, pensa em quem fica. Eu penso em quem sobe. É o acordo." |
| `freya_dia_63` | `coracoes(freya) >= 8` | triste | "Às vezes subo à muralha e olho para a torre. Quinze minutos. Depois volto ao trabalho. Ninguém sabe. Agora tu." |
| `freya_dia_64` | `coracoes(freya) >= 10` | feliz | "Lutámos lado a lado. Nunca tinha confiado as minhas costas a ninguém desde a minha equipa. Obrigada." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `freya_dia_70` | `origem == atrasado` | zangado | "Chegaste atrasad{o/a} à Arena. Na torre, quem chega atrasado não chega." |
| `freya_dia_71` | `origem == dormir` | normal | "Dormes bem. Bom. Soldado cansado é soldado morto. Dorme. É uma ordem." |
| `freya_dia_72` | `skill_unica == passo_fantasma` | feliz | "Duas esquivas seguidas. Na Arena isso é batota. Contra monstros é inteligência. Usa." |
| `freya_dia_73` | `skill_unica == lamina_espiritual` | normal | "A tua lâmina dispara energia. Bonito. Mas a primeira coisa que te tiram é a arma. Treina com as mãos." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `freya_curta_1` | normal | "Dispensad{o/a}." |
| `freya_curta_2` | normal | "Já falámos. Vai treinar." |
| `freya_curta_3` | feliz | "Outra vez? Então treinamos. Não? Então vai." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Capitã Freya** *(normal)*: "A torre é um campo de batalha que não acaba. Subi até ao 62. Lá em cima as coisas não querem matar-te: querem que desistas."
- **Capitã Freya** *(normal)*: "Os monstros que fogem pela torre e chegam à cidade são poucos. Mas basta um. Por isso fico."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "Lobos em alcateia. Mantém-nos à frente. Nunca de costas para três." |
| 2 Cavernas | "Escuro. Nunca entres numa sala sem saber como sais. Marca as paredes." |
| 3 Pântano | "Crocodilos. Quando a água fica quieta demais, é porque alguma coisa está à espera." |
| 4 Deserto | "Vermes debaixo da areia. Sentem passos. Anda devagar. Corre só quando já sabes para onde." |
| 5 Gelo | "Mamutes. Não os ataques. Se tiveres de os atacar, que seja por uma boa razão. Não há boas razões." |
| 6 Oceano | "Debaixo de água a lança é melhor do que a espada. Pensa nisso." |
| 7 Vulcão | "O 62 foi onde parei. Calor, cultistas, e um silêncio que pesa. Bebe água. E não pares de andar." |
| 8 Reino Assombrado | "Mortos-vivos. Luz e golpes pesados. Não deixes que a névoa te toque." |
| 9 Céu | "Harpias e uma valquíria que só luta a sério com quem merece. Ela vai querer lutar contigo." |
| 10 Abismo | "Não sei. Ninguém sabe. Se tiveres medo, ótimo. O medo mantém-te vivo." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `freya_rumor_01` | — | "Há um lobo com uma cicatriz no olho nos andares da floresta. Já mandou três aventureiros para a Igreja. Está na minha lista." |
| `freya_rumor_02` | `andar_maximo >= 11` | "Um goblin com uma coroa de latão anda a assaltar os mineiros. Rei Gruk. Quando tiveres rank D, é teu." |
| `freya_rumor_03` | `andar_maximo >= 15` | "Três aventureiros estão presos em casulos no ninho das aranhas. Preciso de alguém que os vá buscar." |
| `freya_rumor_04` | `andar_maximo >= 41` | "O Mamute Ancião anda zangado no gelo. Pode ser vencido. Pode ser acalmado. A escolha diz quem tu és." |
| `freya_rumor_05` | `andar_maximo >= 81` | "Há uma valquíria nas nuvens que desafia guerreiros. Sigrun. Vence duelos há cem anos. Quero que a venças. Num duelo justo." |
| `freya_rumor_06` | — | "Os monstros fogem mais pela torre nas noites de lua cheia. Nessas noites durmo de armadura." |

### 4.4 A vida dela
| Corações | Fala |
|---|---|
| 0 | "Capitã da Guarda. Ex-aventureira. Fim." |
| 2 | "Nasci no Quartel. O meu pai era guarda, a minha mãe aventureira. Escolhi a profissão da minha mãe. Acabei na do meu pai." |
| 4 | "Tive uma equipa: eu, o Bjorn e a Sif. Chegámos ao 62. Rank S. Éramos os melhores da cidade." |
| 6 | "O Bjorn e a Sif estão vivos. Casaram e foram viver para Pinhal-do-Norte, no andar 42. Escrevem-me. Eu não respondo. Não sei porquê." |
| 8 | ver a **cena de 8 ❤️** |
| 10 | "Já respondi às cartas do Bjorn e da Sif. Três páginas. Eles vão desmaiar." |

---

## 5. Presentes

**Adora:** armas de qualidade **Excelente**, Lança Relâmpago · **Gosta:** treino (convidá-la para a Arena conta como presente "gosta", 1 por semana), carne ·
**Detesta:** ladrões (itens roubados, presentes do Rook), doces.

| Reação | Falas |
|---|---|
| Adora | "Excelente. A qualidade vê-se no fio. Quem fez isto sabe o que faz. Vou usá-la amanhã." · "A Lança Relâmpago… Sabes há quanto tempo quero uma destas? Não digas nada. Não digas nada." |
| Gosta | "Carne. Boa. Os soldados comem carne. Os bardos comem bolos. Não sejas bardo." |
| Neutro | "Obrigada. Vai para o armazém do Quartel. Tudo tem uso." |
| Não gosta | "Hm. Não. Mas obrigada pela intenção." |
| Detesta | "Doces? Pareço o Lucien?" · "Isto é roubado. Sei pelo cheiro. Cheira a telhado." |

---

## 6. Aniversário e festivais

**Aniversário (Verão, dia 15):**
- Sem presente: "Faço anos. Faço mais flexões do que no ano passado. É assim que se festeja."
- Com presente que adora: "Lembraste-te. Os guardas lembram-se porque têm medo. Tu lembraste-te porque sim. Obrigada."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Sou a segurança da festa. Ninguém rouba as flores do concurso. Este ano não. Rook." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Dançar é como lutar sem acertar. Consigo. Acho. Não me pises. Eu piso de volta." ⚙ +100 |
| F_02 Festival da Pesca | "Não pesco. Faço guarda ao rio. Os peixes são os únicos que fogem de mim sem razão." |
| F_03 Noite dos Espíritos | "Esta noite os fantasmas são amigáveis. Os outros, não. Fico de guarda à Igreja com a Célia." |
| F_04 Festival da Estrela | "Amigo secreto. Calhou-me o Rook. Outra vez. Acho que alguém faz batota. Acho que sei quem." |
| F_05 Dia da Subida | "Bom trabalho, aventureir{o/a}. Disse-o em público. Não me faças repetir." |
| F_06 Concurso da Casa | "Revisto as casas: portas, janelas, fechaduras. Segurança é decoração." |
| F_07 Noite das Lanternas | "Ponho lanternas pelos guardas que perdi. Quatro em oito anos. Sei os nomes. Digo-os baixinho." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Bateu nas árvores? Usaste o terreno. Bom. É a primeira lição que ninguém ensina." |
| Ent Ancião (10) | "Região 1 limpa. A cidade fez festa. Eu fiz uma patrulha extra. Festa é quando os monstros atacam." |
| Aranha-Mãe (15) | "Trouxeste os três dos casulos? Então és dos que voltam por outros. Esses são os melhores." |
| Golem de Cristal (20) | "Partiste as colunas primeiro. Táctica. Gosto de táctica." |
| Serpente do Lodo (25) | "Veneno e lodo. Sujo. Bom trabalho na mesma." |
| Hidra do Pântano (30) | "A Arena de prata abre. Inscreve-te. Vou estar a ver. Não te sintas pressionad{o/a}. Sente-te." |
| Escorpião Imperador (35) | "Carapaça dura e veneno. Atacaste as juntas? Atacaste as juntas. Bom." |
| Faraó Eterno (40) | "Um rei que subiu e ficou. Eu também quis ficar lá em cima, uma vez. Ainda bem que não fiquei." |
| Yeti Ancião (45) | "O Bjorn e a Sif vivem perto dali. Se os vires, diz… não digas nada. Diz que estou bem." |
| Dragão de Gelo (50) | "Metade. Lembro-me do dia em que passei o 50. Bebi três canecas. Tu bebe uma. És mais nov{o/a}." |
| Capitão Esqueleto (55) | "Piratas mortos. Duas vezes mortos agora. Bom trabalho." |
| Leviatã (60) | "Venceste o mar. E o Kai continua lá em cima. As patrulhas continuam." |
| Ferreiro Infernal (65) | "Passaste o meu recorde há três andares e não disseste nada. Bom. Gabar-se é para bardos." |
| Kai — salvo (68) | "Trouxeste-o. Abraça-o tu. Eu dou-lhe um relatório para preencher. Cada um mostra o carinho como sabe." |
| Kai — vencido (68) | "Às vezes a missão não acaba como queremos. Isso não quer dizer que falhaste. Quer dizer que era difícil." |
| Titã de Magma (70) | "Cultistas interrompidos, titã a dormir. Uma vitória limpa. As melhores são assim." |
| Lich Bibliotecário (75) | "Lutaste em silêncio numa biblioteca. Essa nem eu conseguia." |
| Rei Sem Coroa (80) | "O Gorvan voltou a treinar. Ontem treinámos juntos. Não perdi. Não ganhei. Foi bom." |
| Grifo Real (85) | "A Sigrun anda por lá. Se a vires, não lutes com raiva. Ela só respeita quem luta limpo." |
| Serafim Caído (90) | "Não perguntei o que ouviste. A Lyra perguntou-me se eu sabia. Disse que não. Era verdade." |
| Guardião do Tempo (95) | "Cinco andares. Vou estar na muralha. Toda a noite. Todas as noites até voltares." |

---

## 8. Cenas de coração

### ❤️ 2 — Braço de ferro

| | |
|---|---|
| ID | `cena_freya_2` |
| Quando | 2 ❤️ · Taberna, sexta à noite (20:00–23:00) |
| Onde | Taberna "O Primeiro Degrau" |
| Quem | herói, Freya, Lucien, clientes |
| Música | `taberna` |

🎬 A Freya está sentada a uma mesa com o braço apoiado. Três guardas sentados no chão a esfregar o braço.
- **Capitã Freya** *(feliz)*: "Aventureir{o/a}. Senta-te. Braço de ferro. Quem perder paga a rodada."
- 🎬 **Minijogo**: braço de ferro (ver `docs/ATIVIDADES.md`), versão fácil.
- *(ganhar)* **Freya** *(surpresa)*: "Ganhaste. Ninguém ganha. Fiz batota? Não. Ganhaste. Bom." ⚙ +30 · o Lucien começa a compor uma canção sobre isso
- *(perder)* **Freya** *(feliz)*: "Pagas a rodada. Não fiques triste. O Gorvan perdeu comigo uma vez. Com um braço só, mas perdeu."

⚙ 5% de desconto nas inscrições da Arena.

### ❤️ 4 — Treino a sério

| | |
|---|---|
| ID | `cena_freya_4` |
| Quando | 4 ❤️ · campo de treino, 6:00–8:00 |
| Onde | campo de treino da Guilda |
| Quem | herói, Freya |
| Música | `guilda` (versão rápida) |

- **Capitã Freya** *(normal)*: "Hoje treino a sério. Sem bonecos. Comigo. Se te magoar, a Célia trata. Se me magoares, não contes a ninguém."
- 🎬 **Duelo curto** contra a Freya (nível do herói +5, lança; acaba aos 50% de vida de um dos dois).
- **Freya** *(normal, depois)*: "Esquivas para trás. Toda a gente esquiva para trás. Esquiva para dentro. Para o lado da lança. Onde o inimigo não quer que estejas."
- `[Sistema] Dica nova: esquivar para dentro dos ataques grandes.`
- **Freya** *(feliz)*: "Amanhã à mesma hora. E depois de amanhã. Até deixares de esquivar para trás."

⚙ Skill de arma **Contra-Ataque** (depois de uma esquiva perfeita, o próximo golpe faz +50%) e +1 nível de Manejo de Lança.

### ❤️ 6 — A Invasão

| | |
|---|---|
| ID | `cena_freya_6` |
| Quando | 6 ❤️ · `andar_maximo >= 25` · uma noite de lua cheia |
| Onde | muralha e Praça de Ascendia |
| Quem | herói, Freya, guardas, NPCs |
| Música | `invasao` (ver `docs/AUDIO.md`; usa `floresta_perigo` se ainda não existir) |

🎬 Sinos a tocar. A Freya corre pela Praça a dar ordens.
- **Capitã Freya** *(zangada)*: "Invasão! Monstros a sair pelo Cristal Mestre! {nome}, comigo, na Praça! Guardas, às portas!"
⚙ Missão **N_FREYA_3 A Invasão** (evento grande: ver `docs/textos/eventos.md`, secção Invasões, e secção 9 abaixo).

### ❤️ 8 — Porque deixou de subir

| | |
|---|---|
| ID | `cena_freya_8` |
| Quando | 8 ❤️ · muralha sul, 21:00–23:00 |
| Onde | cimo da muralha, a torre ao fundo |
| Quem | herói, Freya |
| Música | `tristeza` (versão com trompa) |

🎬 A Freya está sem armadura, só com uma camisola, encostada às ameias a olhar para a torre.
- **Capitã Freya** *(triste)*: "Há oito anos estávamos no 62. Eu, o Bjorn e a Sif. A dois passos do Bastião dos anões. A melhor equipa da cidade."
- **Capitã Freya** *(triste)*: "Nessa noite, os monstros fugiram pela torre como nunca. Uma vaga. Cá em baixo só havia seis guardas."
- **Capitã Freya** *(normal)*: "Senti. Não sei explicar. Senti que a cidade estava a arder. Desci sozinha, quarenta andares numa noite, pelo cristal."
- **Capitã Freya** *(normal)*: "Cheguei a tempo. Por pouco. A Praça estava cheia de lobos de sombra. Lutei até de manhã."
- **Capitã Freya** *(triste)*: "Depois disso, não consegui voltar a subir. Não por medo. Porque sabia que, se subisse, ninguém estaria cá em baixo da próxima vez."

▶ **"Salvaste a cidade."**
▶ **"Ainda queres subir?"**

- *(salvaste)* **Freya** *(normal)*: "Salvei. E perdi a torre. Não me arrependo. Quase nunca." ⚙ +30
- *(subir)* **Freya** *(triste)*: "Todos os dias. Quinze minutos por dia, nesta muralha. Depois volto ao trabalho." ⚙ +30 · flag `freya_quer_subir` (com 10 ❤️ ela pede para lutar contigo na Arena; no epílogo bom, volta a subir com o Bjorn e a Sif)

⚙ 15% de desconto nas inscrições da Arena. Passa a mandar **cartas** (curtas: "Treina. — F.") com carne seca ou pedras de afiar.

### ❤️ 10 — Lado a lado na Arena

| | |
|---|---|
| ID | `cena_freya_10` |
| Quando | 10 ❤️ · Arena, sábado, 10:00–18:00 |
| Onde | Arena de Ascendia, cheia |
| Quem | herói, Freya, público, Lucien a narrar |
| Música | `tema_freya` (tambores e trompas) |

- **Capitã Freya** *(feliz)*: "Hoje inscrevi-nos aos dois. Torneio de duplas. Platina. Contra os campeões da Cidade Errante."
- **Capitã Freya** *(normal)*: "As minhas costas são tuas. As tuas são minhas. Não falhes. Eu não falho."
- 🎬 **Luta em dupla** (a Freya é companheira temporária) contra 3 rondas de equipas da Arena Errante.
- 🎬 No fim, a Freya levanta o braço do herói. O público grita. O Lucien canta desafinado.
- **Capitã Freya** *(feliz)*: "Há oito anos que não lutava ao lado de alguém. Tinha-me esquecido de como é bom."
- 🎬 Entrega-lhe a lança dela e a insígnia do peito.
- **Capitã Freya** *(normal)*: "A minha lança. A que levei ao 62. Leva-a mais alto do que eu levei. E a insígnia: na cidade, quem a usa fala com a minha voz."

⚙ **Lança da Capitã** (lança lendária) e **Insígnia da Capitã** (+10% DEF). Título *Braço Direito da Guarda*.

---

## 9. Missões

### N_FREYA_1 — Patrulha (0 ❤️, rank E)
- **Pedir** — **Freya**: "Cinco monstros passaram pelo cristal esta noite. Andam pela cidade. Encontra-os. Antes que a padaria tenha outro slime."
- **Passo**: encontrar e vencer **5 monstros** na cidade (sítios ao acaso: telhado da forja, cais, jardim da Igreja, mercado, quinta da Hana). Monstros da região mais alta desbloqueada −10 níveis.
- **Entregar** — **Freya** *(normal)*: "Cinco. E nenhum aldeão ferido. Bom trabalho. Não te habitues." ⚙ 200 ouro · 20 pontos de Guilda · +100

### Caças de monstros com nome (todas)
A Freya dá as caças quando chegas ao rank pedido. Fala ao **dar** · fala ao **entregar**:

| Missão | Rank | Dar | Entregar |
|---|---|---|---|
| R1_12 Uivos de Cicatriz | E | "Lobo preto, cicatriz no olho. Já mandou três para a Igreja. Trata dele." | "Bom trabalho. A sério. Não te habitues." |
| R2_10 O Rei Goblin | D | "Um goblin com coroa de latão a assaltar mineiros. Reis de lata são os piores." | "A coroa é de latão. O rei era de lata. A missão era de ouro." |
| R3_11 Mandíbula | C | "Uma mãe-crocodilo enorme no pântano. Quando a água fica quieta, ela está lá." | "Voltaste com os dez dedos. Conta-os. Pronto." |
| R4_12 O Colosso | B | "Um verme do tamanho de uma rua debaixo da areia. Anda devagar. Ele sente os passos." | "Um colosso. Já não há muitos aventureiros que possam dizer isso." |
| R5_11 O Gigante Gentil | B | "O Mamute Ancião anda zangado. Vence-o ou acalma-o. A escolha é tua." | *(acalmar)* "Acalmaste um mamute. Isso é mais difícil do que vencer." *(vencer)* "Venceste. Às vezes é o que é preciso." |
| R5_14 Balistas | B | "Harpias a atacar o andar 49. Há balistas velhas lá em cima. Usa-as." | "Dez harpias com balistas. Engenharia e pontaria. Bom." |
| R7_13 Três Cabeças | A | "Um cão de três cabeças no vulcão. Três cabeças: três vezes mais cuidado." | "Uma cabeça para cada um dos meus guardas que não voltaram do 66. Obrigada." |
| R8_08 A Condessa | A | (dada pelo Caçador Van; a Freya só comenta) "A Condessa Sangria. Vai com luz e alho. O alho é piada. A luz não." | "Uma vampira a menos. A noite fica mais curta." |
| R9_11 O Duelo de Sigrun | S | "A valquíria Sigrun. Um duelo justo. Sem poções, sem companheiros. Ela respeita isso." | 🎬 olha para a Lança Relâmpago. "Ganhaste-a num duelo justo. É tua. …Posso segurá-la um bocadinho?" |
| R10_13 O Devorador Ancestral | SS | "Rank SS. A primeira em cinquenta anos. A última caça. A maior coisa que já vi num relatório." | "Já não tenho mais caças para te dar. És maior do que a minha lista." |

### N_FREYA_3 — A Invasão (6 ❤️)
- **Passos** (evento de 1 noite, 22:00–5:00):
  1. Defender a **Praça** de 3 vagas de monstros que saem do Cristal Mestre (monstros da região mais alta desbloqueada).
  2. Escolher entre proteger o **Mercado** ou a **Igreja** (a outra fica com dano: o edifício fecha 3 dias para obras).
  3. Vencer o **chefe da invasão** (um monstro com nome da região mais alta) na muralha.
- A Freya, os guardas e os NPCs com 6+ ❤️ ajudam (aparecem na luta: o Brom com um martelo, a Célia com a maça, o Rook nos telhados com facas…).
- **Entregar** — **Freya** *(feliz)*: "A cidade está de pé. Feridos, nenhum. Mortos, nenhum. Nunca tinha escrito um relatório assim." ⚙ +200 · título *Defensor{/a} de Ascendia* · a melhoria **Muralha Reforçada** fica 50% mais barata.
- As invasões seguintes (eventos) estão em `docs/textos/eventos.md`.

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `freya_estado_vida` | `vida_pct < 30` | zangado | "Ferid{o/a}? Igreja. Agora. É uma ordem." |
| `freya_estado_cansado` | `estado(cansado)` | normal | "Soldado cansado é soldado morto. Cama." |
| `freya_rook_fugiu` | `flag(rook_fugiu)` (1.ª vez) | zangado | "Ajudaste o Rook a fugir. Sei que foste tu. Não te prendo. Mas não te vou esquecer." |
| `freya_rook_lei` | `flag(rook_ajudado_lei)` (1.ª vez) | normal | "Tinhas razão sobre o Rook. Eu estava errada. Não digas a ninguém. Sobretudo a ele." |
| `freya_arma_excelente` | arma equipada de qualidade Excelente | feliz | "Essa arma foi bem feita. Respeita-a." |
| `freya_comp_kai` | `companheiro(kai)` | normal | "Kai. Relatório em atraso: oito meses. Mas bem-vindo." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `freya_serv_arena` | abrir a Arena | normal | "Bronze, prata, ouro, platina. Escolhe o teu nível. Ou um acima. Eu escolhia um acima." |
| `freya_serv_inscricao` | pagar a inscrição | normal | "Inscrit{o/a}. Lembra-te: no fim aperta-se a mão." |
| `freya_serv_sem_rank` | rank insuficiente | normal | "Ainda não. Sobe de rank primeiro." |
| `freya_serv_cacas` | ver as caças | normal | "Estas são as caças para o teu rank. As outras ainda não são para ti." |
| `freya_serv_fechado` | Quartel fechado | — | `[Sistema] O Quartel está fechado. A Capitã está de patrulha.` |
