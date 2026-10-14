# Lyra — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.1. Dados: `dados/dialogos/lyra.json`.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | agudos e rápidos, sobem no fim das frases |
| Como fala | depressa, com muitos pontos de exclamação; muda de assunto a meio; ao balcão é profissional ("A Guilda agradece!"), fora dele é desastrada |
| Repete | "MESMO", "ouviste?", "Um momentinho!", "A Guilda agradece!" |
| Tiques | empurra os óculos para cima (animação `ajeitar_oculos`) quando está nervosa ou a pensar |
| Nunca diz | palavrões; nada de mau sobre aventureiros que morreram |
| Chama ao herói | `{nome}`; com 6+ corações às vezes "Dez Mil" (alcunha carinhosa) |
| Rotina ao Domingo | a Guilda tem só o Gorvan; a Lyra está no Mercado de manhã e no rio à tarde (a escrever no diário dela) |

---

## 2. Primeira conversa

Depois da cena P6 (prólogo), a 1.ª vez que carregas em **Conversar**:

- **Lyra** *(feliz)*: "Voltaste! Ótimo, ótimo. Deixa-me explicar como isto funciona, que o Mestre Gorvan explica tudo com três palavras."
- **Lyra** *(normal)*: "O **quadro** tem missões. Escolhes uma, fazes, voltas, eu pago. Simples!"
- **Lyra** *(normal)*: "As missões dão **pontos de Guilda**. Com pontos, sobes de rank. Com rank, há missões melhores. E mais ouro!"
- **Lyra** *(feliz)*: "E se precisares de alguma coisa, de QUALQUER coisa, pergunta. Eu sei tudo o que se passa nesta cidade."
- **Lyra** *(normal)*: "…Quase tudo. Ainda não sei porque é que o Brom canta quando ninguém está a ver."

⚙ Abre o menu de serviços da Lyra: **Missões · Rank · Perguntar sobre…**

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lyra_dia_01` | `hora entre 8 e 10` | feliz | "Bom dia! Hoje há três missões novas e uma é MESMO estranha." |
| `lyra_dia_02` | `hora entre 8 e 10` | normal | "Cheguei cedo. A tinta ainda está fresca. Cheira a trabalho!" |
| `lyra_dia_03` | `hora entre 12 e 14` | normal | "Hora de almoço… e eu aqui com um pão no bolso. Não contes ao Mestre." |
| `lyra_dia_04` | `hora entre 16 e 18` | normal | "Quase a fechar! Se tens alguma coisa para entregar, é agora ou amanhã." |
| `lyra_dia_05` | `hora entre 18 e 20` | feliz | "Fora do balcão sou só a Lyra. Olá, só-a-Lyra! …Isto soou melhor na minha cabeça." |
| `lyra_dia_06` | `hora entre 20 e 23` | triste | "Ainda acordad{o/a}? Eu também. Às vezes a cidade fica tão calada…" |
| `lyra_dia_07` | — | normal | "Sabias que o Brom canta quando ninguém está a ver? É verdade. Tenho testemunhas. Eu." |
| `lyra_dia_08` | — | feliz | "Volta inteir{o/a}, ouviste? É uma ordem da Guilda!" |
| `lyra_dia_09` | — | normal | "Já arrumei os registos por andar, por data e por cor. Agora não encontro nada." |
| `lyra_dia_10` | — | normal | "Partiram-se-me os óculos duas vezes esta semana. Uma foi a porta. A outra também foi a porta." |
| `lyra_dia_11` | — | feliz | "O Tobias tentou vender-me um 'pente para carecas'. Para o Mestre Gorvan. Quase comprei." |
| `lyra_dia_12` | — | normal | "Um conselho de quem lê todos os relatórios: os aventureiros que voltam são os que fogem a tempo." |
| `lyra_dia_13` | `dia_semana == segunda` | zangado | "Segunda-feira. Toda a gente se lembra de entregar as missões à segunda-feira." |
| `lyra_dia_14` | `dia_semana == sexta` | feliz | "Sexta! O Lucien estreia canção nova na taberna. Às vezes rima." |
| `lyra_dia_15` | `dia_semana == domingo` | feliz | "Domingo não há balcão! Hoje sou só uma pessoa normal a comer pão doce." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lyra_dia_20` | `estacao == primavera` | feliz | "Primavera! O quadro enche-se de missões de ervas. E de alergias." |
| `lyra_dia_21` | `estacao == primavera && hora entre 8 e 12` | normal | "Abri a janela da Guilda e entrou uma abelha. Ela agora trabalha cá. Chama-se Formulário." |
| `lyra_dia_22` | `estacao == verao` | normal | "Com este calor, as cartas colam-se umas às outras. E eu colo-me à cadeira." |
| `lyra_dia_23` | `estacao == verao && hora entre 18 e 20` | feliz | "No verão o pôr do sol fica cor-de-laranja em cima da torre. Gosto de pensar que é ela a corar." |
| `lyra_dia_24` | `estacao == outono` | normal | "As folhas entram pela porta e o Mestre Gorvan olha para elas como se fossem inimigos." |
| `lyra_dia_25` | `estacao == outono` | triste | "No outono há sempre mais missões de busca. Gente que não volta antes do frio." |
| `lyra_dia_26` | `estacao == inverno` | normal | "Tenho três camisolas vestidas. Pareço uma cebola com óculos." |
| `lyra_dia_27` | `estacao == inverno && clima == neve` | feliz | "Neve! Fiz um boneco de neve à porta. Tem uma capa e um braço só. Não digas a ninguém quem é." |
| `lyra_dia_28` | `clima == chuva` | normal | "Chuva! Se fores à torre, seca-te antes de entrar. Da última vez inundaram-me os relatórios." |
| `lyra_dia_29` | `clima == trovoada` | triste | "Não gosto de trovões. O meu pai dizia que eram os andares de cima a mudar os móveis." |
| `lyra_dia_30` | `clima == nevoeiro` | normal | "Com este nevoeiro, nem vejo o quadro de missões. E está a dois passos." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lyra_dia_40` | `andar_maximo < 5` | normal | "Os andares 1 a 4 são bons para aprender. Não fiques muito tempo, mas também não corras." |
| `lyra_dia_41` | `andar_maximo >= 5 && andar_maximo < 11` | feliz | "O Kai passou por cá a dizer que é mais rápido do que tu. Eu disse-lhe que sim, sim. Para ele se calar." |
| `lyra_dia_42` | `boss_derrotado(ent_anciao) && andar_maximo < 15` | normal | "Andar 11 para cima é escuro. MESMO escuro. Compra tochas. Compra mais tochas." |
| `lyra_dia_43` | `andar_maximo >= 20` | feliz | "A tua página no registo da Guilda já vai na terceira folha. Tive de colar mais papel!" |
| `lyra_dia_44` | `andar_maximo >= 31 && missao(N_LYRA_3) != concluida` | triste | "Já passaste o andar 31… Não, nada. Esquece. Boa sorte lá em cima." |
| `lyra_dia_45` | `andar_maximo >= 50` | feliz | "Metade da torre! Sabes quantos aventureiros chegaram ao 50 nos últimos dez anos? Contigo, três." |
| `lyra_dia_46` | `andar_maximo >= 61 && !flag(kai_salvo)` | triste | "O nome do Kai continua no quadro dos desaparecidos. Eu não o tiro. Não o tiro." |
| `lyra_dia_47` | `flag(kai_salvo)` | feliz | "O Kai veio cá entregar uma missão e disse 'obrigado'. Escrevi a data. É histórico." |
| `lyra_dia_48` | `andar_maximo >= 81` | normal | "Andar 81… Para lá disto, a Guilda nem tem mapas. Tu é que os vais fazer." |
| `lyra_dia_49` | `andar_maximo >= 91` | triste | "Tenho medo de abrir o registo e ver que paraste de escrever. Volta sempre, está bem?" |
| `lyra_dia_50` | `rank >= C` | feliz | "Rank C! Agora podes aceitar as missões com carimbo vermelho. Eu adoro o carimbo vermelho." |
| `lyra_dia_51` | `rank >= A` | feliz | "Rank A… Há aventureiros que trabalham uma vida inteira para isto. Tu nem tens rugas!" |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lyra_dia_60` | `coracoes(lyra) >= 2` | feliz | "Guardei-te a missão mais fácil do quadro. Não digas que fui eu." |
| `lyra_dia_61` | `coracoes(lyra) >= 3` | normal | "Ontem sonhei que eu também subia a torre. Caí no andar 1. Num slime. Acordei."  |
| `lyra_dia_62` | `coracoes(lyra) >= 4` | feliz | "Dez Mil! …Desculpa. Saiu. É que na minha cabeça já te chamo assim." |
| `lyra_dia_63` | `coracoes(lyra) >= 5` | normal | "Quando voltas, eu faço um risquinho no calendário. Já tenho muitos risquinhos." |
| `lyra_dia_64` | `coracoes(lyra) >= 6` | triste | "Às vezes tenho medo de que deixes de voltar. Depois apareces e eu finjo que não tive medo." |
| `lyra_dia_65` | `coracoes(lyra) >= 8` | feliz | "O meu diário de aventuras já tem mais páginas tuas do que minhas. Isso é estranho? Isso é estranho." |
| `lyra_dia_66` | `coracoes(lyra) >= 10` | feliz | "Melhor amig{o/a} da recepcionista da Guilda. É um título oficial. Eu inventei-o. Tem carimbo." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lyra_dia_70` | `origem == jogador` | feliz | "Tu falas de 'pontos de vida' como se fosse normal. No teu mundo havia mesmo jogos assim?" |
| `lyra_dia_71` | `origem == atrasado` | normal | "Chegas sempre a correr. No teu mundo também estavas sempre atrasad{o/a}?" |
| `lyra_dia_72` | `origem == ajudante` | feliz | "A Dona Marta diz que ajudaste a carregar as compras. Ela fala de ti como se fosses net{o/a} dela." |
| `lyra_dia_73` | `origem == dormir` | normal | "Tens cara de quem dormia bem no teu mundo. Aqui ninguém dorme bem. Menos o Pip." |
| `lyra_dia_74` | `skill_unica == olho_do_sistema` | normal | "Com esse olho vês os níveis dos monstros? Podias trabalhar aqui! Era só ler os relatórios… e ver se mentem." |
| `lyra_dia_75` | `skill_unica == mao_de_midas` | feliz | "Mão de Midas… Toca no meu ordenado, por favor." |
| `lyra_dia_76` | `skill_unica == lingua_universal` | normal | "Se falas com monstros, pergunta-lhes porque é que roubam sempre as meias dos aventureiros." |
| `lyra_dia_77` | `skill_unica == segunda_vida` | triste | "Segunda Vida não é desculpa para gastares a primeira, ouviste?" |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `lyra_curta_1` | feliz | "Mais alguma coisa? Estou aqui!" |
| `lyra_curta_2` | normal | "O quadro não muda até amanhã, prometo." |
| `lyra_curta_3` | feliz | "Olá outra vez! Ainda estou a trabalhar. Infelizmente." |
| `lyra_curta_4` | normal | "Hmm? Ah! Estava a contar formulários. Perdi a conta. Obrigada." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Lyra** *(normal)*: "A torre? Ninguém sabe quem a fez. Está aí desde sempre. A cidade cresceu à volta dela, como musgo numa pedra."
- **Lyra** *(normal)*: "São cem andares. Ninguém chega ao topo há trezentos anos. O registo mais alto da Guilda é o andar 91."
- **Lyra** *(feliz)*: "Mas tu és o Jogador nº 10 000. Isso tem de querer dizer alguma coisa. Os números bonitos querem sempre dizer alguma coisa!"

### 4.2 O andar atual

A Lyra fala da **região do andar mais alto** a que chegaste, com informação "da Guilda".

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta: slimes, lobos, javalis. No andar 5 há um javali enorme que os aventureiros chamam 'Rei'. Eu chamo-lhe 'não'." |
| 2 Cavernas | "Cavernas: escuro, morcegos, mineiros com medo. 4 em cada 10 missões falhadas aqui são por causa de tochas apagadas. 4 em cada 10!" |
| 3 Pântano | "Pântano: lodo, sanguessugas e Homens-Lagarto. A Guilda diz que são perigosos. Eu… não sei. Os relatórios contradizem-se." |
| 4 Deserto | "Deserto: calor, areia, esqueletos. O meu pai foi lá. Leva água. Leva o dobro da água." |
| 5 Gelo | "Gelo: o frio mata mais do que os monstros. Os relatórios dizem 'morreu de frio' mais vezes do que 'morreu de yeti'." |
| 6 Oceano | "Oceano: andares debaixo de água! A Guilda tem um relatório só sobre 'não respirar'. É curto." |
| 7 Vulcão | "Vulcão: lava, cultistas, e… o último sítio onde viram o Kai. Tem cuidado. Por favor." |
| 8 Reino Assombrado | "Reino Assombrado: mortos que andam e uma biblioteca que grita se fizeres barulho. Não acredito em fantasmas. Acredito em relatórios." |
| 9 Céu | "Céu: ilhas a flutuar! Se caíres… as nuvens apanham-te. Quase sempre. Os relatórios dizem 'quase sempre'." |
| 10 Abismo | "Abismo: a Guilda não tem relatórios daí. Os poucos que voltaram não conseguiam explicar o que viram. Escreve tudo, está bem?" |

### 4.3 Rumores

A Lyra diz **1 rumor por dia**, escolhido dos que cumprem a condição. Muitos dão pistas de missões e segredos.

| ID | Condição | Rumor |
|---|---|---|
| `lyra_rumor_01` | — | "Dizem que o Tobias tem um irmão gémeo que vende nas Zonas Seguras. E que se odeiam. Por cartas. Com selo." |
| `lyra_rumor_02` | `andar_maximo >= 2` | "O Velho Cass, no andar 2, jura que as estátuas do andar 8 se mexem. Ninguém acredita nele. Eu acredito um bocadinho." |
| `lyra_rumor_03` | `andar_maximo >= 3` | "Um aventureiro jura que viu uma luz a dançar no andar 4, perto de um círculo de cogumelos. Fadas? Febre?" |
| `lyra_rumor_04` | `andar_maximo >= 5` | "Há um javali com uma pedra brilhante na barriga… Ou foi o que o Bruno disse. O Bruno diz muitas coisas." |
| `lyra_rumor_05` | `andar_maximo >= 7` | "A Selene tem um irmão em Folhalta, no andar 7. Ela nunca fala dele. Isso quer dizer que pensa nele sempre." |
| `lyra_rumor_06` | `andar_maximo >= 9` | "O Pip diz que no lago do andar 9 há um peixe do tamanho de uma casa. O Pip também diz que pescou uma baleia." |
| `lyra_rumor_07` | — | "Viram o Rook a sair da Câmara do Governador à noite. Pela janela. Do segundo andar." |
| `lyra_rumor_08` | — | "A Madame Oriel previu que eu ia encontrar um grande amor. Encontrei um gato. É um bom gato." |
| `lyra_rumor_09` | `andar_maximo >= 11` | "Há uma toupeira dourada nas minas. Vale uma fortuna. O Tobias já mandou fazer uma gaiola de ouro. Para uma toupeira!" |
| `lyra_rumor_10` | `andar_maximo >= 18` | "Dizem que há uma forja de anões no andar 18. O Brom faz de conta que não ouviu quando se fala nisso." |
| `lyra_rumor_11` | `andar_maximo >= 21` | "Os mineiros juram que há uma aldeia de Homens-Lagarto amigos. A Guilda diz que 'amigo' é muito forte." |
| `lyra_rumor_12` | `andar_maximo >= 31` | "Há um acampamento antigo da Guilda algures no andar 31. Ninguém sabe exatamente onde. Eu… gostava de saber." |
| `lyra_rumor_13` | `andar_maximo >= 41` | "Uma aldeia de caçadores no gelo tem um sino que toca sozinho. Dizem que dentro dele há um diário." |
| `lyra_rumor_14` | `andar_maximo >= 51` | "Há um navio que aparece no mar dos andares 51 a 60 e desaparece no nevoeiro. Os marinheiros chamam-lhe 'o navio dos que não chegaram'." |
| `lyra_rumor_15` | `andar_maximo >= 71` | "O Velho Fausto anda a pedir livros do andar 75. Livros de uma biblioteca que grita. O Velho Fausto é corajoso ou doido." |
| `lyra_rumor_16` | `andar_maximo >= 91` | "Dizem que no topo da torre há um jardim. Igual ao primeiro andar. Porque é que alguém faria isso?" |
| `lyra_rumor_17` | `estacao == inverno` | "Este ano o Festival da Estrela tem amigo secreto outra vez. Se te calhar eu… gosto de flores. Só estou a dizer." |
| `lyra_rumor_18` | `missao(N_TOBIAS_3) == concluida` | "O Tobias e o Tibério juntaram as lojas! Vi-os abraçados. Depois discutiram sobre quem pagou o abraço." |

### 4.4 A vida dela

| Corações | Fala |
|---|---|
| 0 | "Eu? Não há nada para contar. Nasci aqui, trabalho aqui, como pão doce aqui. Fim!" |
| 2 | "O meu pai era aventureiro. Chamava-se **Darian**. Saiu para o andar 31 quando eu tinha oito anos e não voltou." |
| 4 | "Trabalho na Guilda porque assim sei de todos os que sobem. Se alguém não voltar… pelo menos alguém se lembra do nome." |
| 6 | "A minha mãe vende tecidos no mercado da manhã. Ela não fala do meu pai. Eu falo por nós as duas." |
| 8 | "Tenho medo de subir. Tenho medo de altura, de escuro, de aranhas e de patos. Os patos olham para mim de uma maneira…" |
| 10 | "Já não preciso de saber o que aconteceu ao meu pai para estar bem. Graças a ti. Mas continuo com medo de patos." |

---

## 5. Presentes

**Adora:** Flor de Mel, Panquecas de Mel Azul, Concha Rara · **Gosta:** flores, doces ·
**Detesta:** partes de monstros, Gel de Slime. O resto é **neutro** (ver `docs/ITENS.md`, secção dos presentes).

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "PARA MIM?! Isto é… isto é MESMO para mim? Vou pôr no sítio mais bonito da Guilda. Que é a minha secretária." · "Não acredito que te lembraste! Estou a guardar isto para sempre. Ou até ao almoço, se for comida." |
| Gosta | "Que bonito! Obrigada, {nome}. A Guilda agradece. Eu também, mas mais." · "Ah, gosto disto! Vou usar já. Ou comer já. Ou as duas coisas." |
| Neutro | "Oh, obrigada! Vou… arranjar-lhe um sítio." · "Hmm! Que… prático. Obrigada!" |
| Não gosta | "Ah. Isto é… muito… teu. Obrigada pela intenção!" |
| Detesta | "Isso está a MEXER?! Tira isso do meu balcão, por favor, por favor, por favor." · "Gel de Slime. Na Guilda. Em cima dos formulários. Obrigadíssima." |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Flor de Mel | "Flor de Mel! O meu pai trazia-me uma sempre que voltava da torre. …Desculpa, entrou-me poeira no olho." |
| Panquecas de Mel Azul | "Panquecas da Dona Marta?! Não, fizeste-as tu? Vou casar com estas panquecas." |
| Concha Rara | "Uma concha do mar de dentro da torre… Se a encostar ao ouvido, ouço os andares de cima?" |
| Óculos (qualquer) | "Óculos novos! Os meus agradecem. Os velhos vão para a gaveta dos óculos velhos. Que já tem nove." |
| Pato de Madeira (brinquedo) | "Porquê?! Porque é que farias isto?! …Está bem, é giro. Mas olha para mim de lado." |
| Presa do Javali-Rei | "Uma presa?! Do REI das tocas? Isto vai para o museu da Guilda. Não para a minha secretária. Por favor." |

---

## 6. Aniversário e festivais

**Aniversário (Primavera, dia 5):**
- Sem presente: **Lyra** *(feliz)*: "Hoje faço anos! …Não, não estou a dizer isto para ganhar presentes. Estou a dizer por dizer. Por dizer."
- Com presente que adora: **Lyra** *(feliz)*: "Lembraste-te dos meus anos! Ninguém se lembra dos anos da recepcionista! Vou chorar. Não vou. Já estou."
- Com outro presente: **Lyra** *(feliz)*: "Um presente de anos! Obrigada, obrigada! Este ano está a ser o melhor."
- Na Guilda há um bolo torto em cima do balcão: 🎬 se falares com o Gorvan nesse dia, ele diz "Fui eu que o fiz. Não digas."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Concurso de flores! Eu concorro todos os anos. Fico sempre em último. A minha flor é sempre a mais… original." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Lyra** *(surpresa)*: "EU? Sim! Não. Sim! Mas aviso já que piso pés." ⚙ dança · +100 amizade |
| F_02 Festival da Pesca | "Eu não pesco. Os peixes olham para mim. Mas faço as fichas de inscrição! Queres uma? Tem um desenho de um peixe. Fui eu." |
| F_03 Noite dos Espíritos | "Esta noite ponho uma lanterna à janela. Para o meu pai encontrar o caminho. É tonto, eu sei." (com 6+ ❤️: "Pões uma comigo?" ⚙ +30) |
| F_04 Festival da Estrela | "Amigo secreto! Calhou-me o Mestre Gorvan. O que se dá a quem não gosta de nada? …Um cachecol. Para o braço que tem." |
| F_05 Dia da Subida | "Tive de escrever o teu nome no quadro grande da Guilda! Com a caneta boa! Toda a gente parou para ler!" |
| F_06 Concurso da Casa | "Vou ser jurada este ano! Não, não posso dar-te pontos extra. …Que cor são as cortinas?" |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`).

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `lyra_boss_javali_rei` | "O Javali-Rei! Tenho de mudar o estado no registo de 'perigo' para 'derrotado por {nome}'. Adoro mudar estados!" |
| Ent Ancião (10) | `lyra_boss_ent_anciao` | "A floresta está livre! Há gente na praça a cantar. Desafinados, mas a cantar!" |
| Aranha-Mãe (15) | `lyra_boss_aranha_mae` | "Uma aranha do tamanho de uma carroça. Não me contes os detalhes. Não. Conta. Não!" |
| Golem de Cristal (20) | `lyra_boss_golem_cristal` | "O Governador quer dar-te uma casa! Fui eu que preenchi os papéis. Escolhi a que tem a janela maior." |
| Serpente do Lodo (25) | `lyra_boss_serpente_lodo` | "Os relatórios do pântano estavam tão cheios de lodo que tive de os ler com pinças." |
| Hidra do Pântano (30) | `lyra_boss_hidra_pantano` | "Uma hidra! Quantas cabeças? Não, quantas cabeças MESMO? Preciso do número para o registo." |
| Escorpião Imperador (35) | `lyra_boss_escorpiao_imperador` | "O deserto é onde o meu pai foi. Obrigada por ires lá e… voltares." |
| Faraó Eterno (40) | `lyra_boss_farao_eterno` | "Um faraó que também foi Jogador? O Velho Fausto não se cala com isso. Nem dorme. Nem come." |
| Yeti Ancião (45) | `lyra_boss_yeti_anciao` | "Trouxeste neve nas botas para a Guilda! …Pode ficar. É neve de herói." |
| Dragão de Gelo (50) | `lyra_boss_dragao_gelo` | "Metade da torre. METADE. Vou ter de comprar um livro de registo novo só para ti." |
| Capitão Esqueleto (55) | `lyra_boss_capitao_esqueleto` | "Piratas mortos. Claro. Porque não? Já nada me surpreende. Mentira, surpreende tudo." |
| Leviatã (60) | `lyra_boss_leviata` | "Venceste o mar… e o Kai continua sem voltar. Desculpa. Eu devia estar feliz. Estou. Um bocadinho." |
| Ferreiro Infernal (65) | `lyra_boss_ferreiro_infernal` | "O Brom passou aqui de olhos vermelhos e disse que era fumo. Na Guilda não há fumo, Brom." |
| Kai — salvo (68) | `lyra_boss_kai_salvo` | "Ele voltou! O Kai voltou! Vou tirar o nome dele do quadro dos desaparecidos com as minhas próprias mãos!" |
| Kai — vencido (68) | `lyra_boss_kai_vencido` | "Não perguntei nada. Não precisas de contar. Senta-te um bocado aqui, ao pé do balcão, está bem?" |
| Titã de Magma (70) | `lyra_boss_tita_magma` | "Chegaste mais alto do que quase todos os registos da Guilda. Quase. Ainda faltam vinte e um andares para bateres o recorde." |
| Lich Bibliotecário (75) | `lyra_boss_lich_bibliotecario` | "O Velho Fausto chorou quando soube que a biblioteca do 75 está livre. Depois pediu-te uma lista de livros. Longa." |
| Rei Sem Coroa (80) | `lyra_boss_rei_sem_coroa` | "O Mestre Gorvan voltou ao campo de treino. Está a treinar outra vez. Não sei o que fizeste, mas obrigada." |
| Grifo Real (85) | `lyra_boss_grifo_real` | "Uma pena de grifo?! Posso usá-la como caneta? É a caneta mais bonita da história da Guilda." |
| Serafim Caído (90) | `lyra_boss_serafim_caido` | "Estás calad{o/a}. Não faz mal. Se quiseres contar, eu escrevo. Se não quiseres, eu fico aqui." |
| Guardião do Tempo (95) | `lyra_boss_guardiao_tempo` | "Andar 95. Passaste o registo mais alto da Guilda. Já não há ninguém para comparar. Só tu." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — Papéis à noite

| | |
|---|---|
| ID | `cena_lyra_2` |
| Quando | 2 ❤️ · entrar na Guilda entre as 20:00 e as 23:00 |
| Onde | Guilda, balcão (só a luz de uma vela) |
| Quem | herói, Lyra |
| Música | `ascendia_noite` (versão só piano) |

🎬 A Guilda está escura. A Lyra está ao balcão com pilhas de papéis à volta e uma vela quase no fim.

- **Lyra** *(surpresa)*: "Ah! {nome}! Assustaste-me. Pensei que era… ninguém. Ninguém, era isso que eu pensava."
- **Lyra** *(normal)*: "Estou a arrumar os registos antigos. De há dez anos, vinte anos… Há nomes aqui que mais ninguém lê."
- 🎬 Ajeita os óculos. Passa o dedo por uma linha.
- **Lyra** *(triste)*: "Este é o do meu pai. 'Darian. Rank B. Andar 31. Estado: não voltou.'"
- **Lyra** *(triste)*: "'Não voltou.' Não diz 'morreu'. Eu sei que é a mesma coisa. Mas a Guilda escreve 'não voltou'."

▶ **"Lamento muito."**
▶ **"Talvez ainda haja pistas."**
▶ *(ficar em silêncio)*

- *(Lamento)* **Lyra** *(triste)*: "Obrigada. Já foi há muito tempo. Eu tinha oito anos. Lembro-me mais do cheiro do casaco dele do que da cara."
- *(Pistas)* **Lyra** *(normal)*: "…Já pensei nisso. Mil vezes. Mas a Guilda não manda ninguém ao 31 por causa de uma pessoa só." ⚙ +30
- *(silêncio)* 🎬 A Lyra sorri devagar. **Lyra** *(normal)*: "Obrigada por não dizeres nada. As pessoas dizem sempre qualquer coisa." ⚙ +30
- **Lyra** *(feliz)*: "Pronto! Chega de coisas tristes. Ajudas-me a arrumar a letra D? Ninguém gosta da letra D."

⚙ 5% de desconto nos serviços da Guilda (não há loja: as taxas de inscrição em eventos da Arena ficam mais baratas).

### ❤️ 4 — As lanternas do rio

| | |
|---|---|
| ID | `cena_lyra_4` |
| Quando | 4 ❤️ · falar com a Lyra no **dia 28 de qualquer estação** (Noite das Lanternas) |
| Onde | Rio e Porto, às 20:00 |
| Quem | herói, Lyra, aldeões |
| Música | `lanternas_rio` |

> **Noite das Lanternas**: no último dia de cada estação, Ascendia põe lanternas de papel no rio, uma por cada aventureiro
> que não voltou. É uma tradição pequena (não é um festival: não há loja nem jogos).

- (de dia, na Guilda) **Lyra** *(nervosa)*: "Hoje à noite… vens comigo ao rio? Às oito. Há uma coisa que quero mostrar. Não é nada de mal! É bonito."

🎬 Às 20:00, no cais. Dezenas de lanternas de papel a flutuar no rio, amarelas e laranja, a refletir na água.
🎥 A câmara sobe devagar até mostrar o rio inteiro cheio de luzes, com a torre ao fundo.

- **Lyra** *(feliz)*: "Cada lanterna é uma pessoa que subiu e não voltou. Este ano há quarenta e duas."
- **Lyra** *(normal)*: "A minha é aquela torta. Faço-a sempre eu. Fica sempre torta."
- 🎬 A Lyra dá-te uma lanterna por acender.
- **Lyra** *(normal)*: "Esta é para tu pores… quando quiseres. Não precisa de ser por alguém que morreu. Pode ser por alguém de quem tens saudades."

▶ **"Ponho pela minha família, lá do meu mundo."**
▶ **"Ponho pelo teu pai."**
▶ **"Guardo-a para mais tarde."**

- *(família)* **Lyra** *(triste)*: "Eles também devem pôr uma por ti. Do lado de lá. Tenho a certeza." ⚙ +30
- *(teu pai)* **Lyra** *(feliz, a chorar)*: "…Agora ele tem duas. Nunca teve duas." ⚙ +30
- *(guardar)* **Lyra** *(normal)*: "Está bem. A lanterna espera. As lanternas são boas a esperar."

⚙ Recebe a receita **Panquecas de Mel Azul** (se ainda não a tiveres) ou **Lanterna de Papel** (decoração) ×3.
⚙ A partir daqui, todas as Noites das Lanternas podes pôr uma lanterna no rio (+10 amizade com todos os NPCs presentes).

### ❤️ 6 — O nome no registo

| | |
|---|---|
| ID | `cena_lyra_6` |
| Quando | 6 ❤️ · `andar_maximo >= 31` · entrar na Guilda de manhã (8:00–12:00) |
| Onde | Guilda, arquivo das traseiras |
| Quem | herói, Lyra |
| Música | `guilda` → silêncio |

🎬 A Lyra está no arquivo, sentada no chão, rodeada de caixas abertas. Tem um papel amarelado na mão.

- **Lyra** *(surpresa)*: "{nome}! Vem cá, vem cá! Olha para isto!"
- **Lyra** *(normal)*: "É o último relatório da equipa do meu pai. Estava numa caixa errada. Na letra D! Ninguém arruma a letra D!"
- **Lyra** *(normal)*: "'Acampamento montado no andar 31, perto das três rochas em forma de dente. Água para 6 dias. Darian vai à frente.'"
- **Lyra** *(triste)*: "Ele estava num acampamento. Com um sítio. Com rochas. Há um SÍTIO, {nome}."
- 🎬 Ajeita os óculos três vezes seguidas.
- **Lyra** *(nervosa)*: "Eu sei que é pedir muito. Eu sei que é perigoso. Eu nunca pedi nada a nenhum aventureiro. Nunca."
- **Lyra** *(triste)*: "Mas tu já passaste o 31. E… se alguém tem de ir lá, eu queria que fosses tu."

▶ **"Eu vou."**
▶ **"Vou, mas prometes não te preocupar demasiado."**

- *(Eu vou)* **Lyra** *(feliz, a chorar)*: "Obrigada. Obrigada. Volta inteir{o/a}, ouviste? Isto já não é uma ordem da Guilda. É um pedido meu."
- *(Prometes)* **Lyra** *(feliz)*: "Não prometo nada! Vou preocupar-me imenso! Mas vou fingir muito bem."

- **Lyra** *(normal)*: "Ah! E… toma. É uma **Bolsa de Materiais** da Guilda. Só a damos aos aventureiros de confiança."
- **Lyra** *(feliz)*: "Quem decide quem é de confiança sou eu. Decidi agora."

⚙ Recebe a **Bolsa de Materiais** (materiais ilimitados, ver `docs/EQUIPAMENTO.md`, secção 9).
⚙ Missão **N_LYRA_3 O Pai da Lyra** iniciada. A Lyra aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — O diário das tuas aventuras

| | |
|---|---|
| ID | `cena_lyra_8` |
| Quando | 8 ❤️ · Domingo, das 14:00 às 18:00 |
| Onde | margem do rio, debaixo do salgueiro |
| Quem | herói, Lyra |
| Música | `ascendia_dia` (versão calma) |

🎬 A Lyra está sentada na relva a escrever num caderno grosso. Fecha-o de repente quando te vê.

- **Lyra** *(surpresa)*: "Nada! Não estava a fazer nada. Este caderno não existe."
- **Lyra** *(normal)*: "…Está bem. Existe. Senta-te."
- **Lyra** *(nervosa)*: "Desde o dia em que tocaste no Cristal, eu escrevo tudo o que fazes. Os relatórios da Guilda são tão secos… 'Andar 5. Javali. Concluído.'"
- **Lyra** *(feliz)*: "Mas tu não fizeste só 'concluído'. Tu… tropeçaste numa raiz e caíste em cima do javali. O Kai contou-me."
- 🎬 Abre o caderno. Há desenhos teus, mal feitos, com setas e notas.
- **Lyra** *(feliz)*: "Olha. Aqui és tu com o Ent. Aqui és tu com o Brom a gritar contigo. Aqui és tu a dormir na taberna."

▶ **"Desenhas bem!"**
▶ **"Posso escrever uma página?"**
▶ **"Porque é que escreves isto?"**

- *(Desenhas bem)* **Lyra** *(feliz)*: "Mentira. Mas obrigada. O Ent parece uma couve."
- *(Escrever)* **Lyra** *(surpresa)*: "A sério? Toma! Escreve o que quiseres. Não leio até chegares a casa. …Talvez leia." ⚙ +30
- *(Porquê)* **Lyra** *(triste)*: "Porque ninguém escreveu as aventuras do meu pai. Só 'não voltou'. Contigo, não vai ser assim. Vai haver um livro inteiro." ⚙ +30

⚙ 15% de desconto. A Lyra passa a mandar **cartas** (1 por semana) com presentes: Flor de Mel, Poção de Vida, ou uma página do caderno dela (decoração emoldurada).

### ❤️ 10 — A carta do pai

| | |
|---|---|
| ID | `cena_lyra_10` |
| Quando | 10 ❤️ · `missao(N_LYRA_3) == concluida` · entrar na Guilda ao entardecer (18:00–20:00) |
| Onde | Guilda, depois de fechar |
| Quem | herói, Lyra |
| Música | `tema_lyra` (piano + violino) |

🎬 A Lyra está sentada no balcão (em cima do balcão, não atrás). Tem a bússola do pai aberta ao contrário.

- **Lyra** *(normal)*: "A tampa de trás da bússola estava presa. Hoje abriu. Sozinha. Juro."
- 🎬 Mostra um papel dobrado muitas vezes, pequeno, quase transparente.
- **Lyra** *(triste)*: "Tem escrito por fora: 'Para o próximo aventureiro que passar por aqui.'"
- **Lyra** *(normal)*: "Não é para mim. É para ti. Foste tu que passaste por lá. Mas… posso ser eu a ler?"

▶ **"Lê tu."**

🎬 A Lyra desdobra o papel. Respira fundo. Ajeita os óculos.

- **Lyra** *(a ler)*: "'Se encontraste isto, chegaste mais longe do que eu. Parabéns. A sério.'"
- **Lyra** *(a ler)*: "'Eu tenho uma filha em Ascendia. Chama-se Lyra. Tem oito anos e medo de patos.'"
- 🎬 Para. Ri-se e chora ao mesmo tempo.
- **Lyra** *(a ler)*: "'Se voltares lá abaixo, diz-lhe que o pai não ficou aqui por ser fraco. Ficou porque o caminho de volta era mais comprido do que a água.'"
- **Lyra** *(a ler)*: "'E diz-lhe que não precisa de subir para ser corajosa. Ficar também é corajoso.'"
- 🎬 Silêncio. A vela tremeluz.
- **Lyra** *(triste)*: "Ele sabia que eu tinha medo de patos."
- **Lyra** *(feliz)*: "{nome}. Obrigada. Por teres ido. Por teres voltado. Por me teres deixado ler."
- 🎬 Abre uma gaveta e tira um cartão dourado com o teu nome gravado.
- **Lyra** *(feliz)*: "Isto estava pronto há semanas. Estava à espera do momento certo. Acho que o momento certo é agora."

⚙ Recebe o **Cartão de Ouro da Guilda** (as missões dão +25% de recompensa). Título *Amig{o/a} da Guilda*.
⚙ A Lyra passa a ter a fala `lyra_dia_66` e, no epílogo, aparece a escrever um livro (ver `docs/HISTORIA.md`, secção 7).

---

## 9. Missões

### N_LYRA_1 — Papéis Perdidos (0 ❤️, rank F, depois de H_03)

- **Pedir** — **Lyra** *(nervosa)*: "{nome}! Desastre! Abri a janela e o vento levou cinco formulários de inscrição! Se o Mestre Gorvan sabe… Ajudas-me a encontrá-los? Estão espalhados pela cidade!"
  ▶ **"Claro!"** ⚙ missão iniciada · ▶ **"Agora não."** → "Está bem… Vou fingir que é arte moderna."
- **Onde estão os 5 papéis** (brilham quando estás a 5 m):
  1. na fonte da Praça (a flutuar);
  2. na banca do Tobias (ele está a usá-lo para embrulhar peixe: "É meu! Encontrei! Achado não é roubado!" → ▶ "É da Guilda." → ele devolve);
  3. no telhado da Forja (sobe pelos barris);
  4. com a Mia, que fez um barquinho de papel ("É um navio de guerra. …Está bem, toma.");
  5. no Rio, preso numa cana do Pip (ele está a dormir; tira-o devagar ou ele acorda e conta uma história de pesca).
- **Durante** — **Lyra**: "Já encontraste quantos? {n}? Ai, faltam {5-n}. Não, eu estou calma. Estou MESMO calma."
- **Entregar** — **Lyra** *(feliz)*: "Todos! E só um cheira a peixe! Toma, é pouco, mas é do meu bolso. Não contes ao Mestre." ⚙ 100 ouro · +100 amizade

### N_LYRA_2 — Entrega Rápida (2 ❤️, `andar_maximo >= 11`)

- **Pedir** — **Lyra** *(normal)*: "Tenho três cartas urgentes: o Bruno no andar 2, a Anciã Lothiel no andar 7 e o Posto Mineiro no andar 11. Têm de chegar hoje. HOJE. Consegues?"
- **Regra**: as 3 entregas no mesmo dia (das 6:00 às 2:00). O cristal pode ser usado. Se falhar, volta a tentar no dia seguinte.
- **Ao entregar cada carta**: Bruno — "Uma carta da Lyra! Diz que me devo lavar mais. Ela tem razão." · Lothiel — "A pequena Lyra. Escreve como o pai dela falava: depressa." · Capataz do Posto — "Até que enfim! Pedimos tochas há uma semana."
- **Falhar** — **Lyra** *(triste)*: "Não faz mal! Amanhã há mais 'hoje'. Eu escrevo as cartas outra vez. Já tenho prática."
- **Entregar** — **Lyra** *(feliz)*: "Três andares num dia! Merecias uma medalha. Não temos medalhas. Tens esta bolsa." ⚙ **Bolsa de Viagem** (+5 espaços) · +150 amizade

### N_LYRA_3 — O Pai da Lyra (6 ❤️, depois da cena de 6 ❤️)

- **Passos**:
  1. Ir ao andar 31 e encontrar as **três rochas em forma de dente** (atrás do **Rochedo do Vigia**; o sítio só aparece no mapa depois desta missão).
  2. Seguir as estacas meio enterradas até ao **acampamento** (tenda rasgada, fogueira com pedras, mochila velha).
  3. Ler o diário do acampamento (é uma página de lore normal, não do Aren).
  4. Apanhar a **bússola do pai** (dentro da mochila).
  5. Voltar à Guilda.
- **No acampamento**: `[Sistema] Encontraste: Acampamento de Darian.` A última linha do diário: *"Água para 2 dias. Volto amanhã ao amanhecer. Hoje o céu está bonito."*
- **Entregar** — 🎬 a Lyra pega na bússola com as duas mãos.
  - **Lyra** *(triste)*: "Era dele. Tem as iniciais. 'D.' A agulha… aponta para onde?"
  - `[Sistema] A Bússola de Darian aponta sempre para a Zona Segura mais próxima.`
  - **Lyra** *(feliz, a chorar)*: "Para casa. Claro. Ele queria sempre voltar para casa."
  - **Lyra** *(normal)*: "Fica com ela. Não, a sério. Ela quer subir. Eu… eu quero ficar. Está bem assim."
  - ⚙ **Bússola de Darian** (acessório) · +200 amizade · flag `lyra_pai_encontrado`

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `lyra_estado_vida` | `vida_pct < 30` | zangado | "Estás a SANGRAR em cima do balcão! Vai à Igreja! Agora! Eu limpo isto. Vai!" |
| `lyra_estado_maldito` | `estado(amaldicoado)` | surpresa | "Tens uma nuvem roxa à volta da cabeça. Não é moda, pois não? A Irmã Célia tira isso." |
| `lyra_estado_cansado` | `estado(cansado)` | normal | "Tens olheiras até ao queixo. Vai dormir! A torre não foge." |
| `lyra_estado_molhado` | `estado(encharcado)` | zangado | "Estás a pingar nos formulários! Fica aí. Não. Aí. Mais para trás. Obrigada." |
| `lyra_estado_sapo` | `estado(sapo)` | surpresa | "Um sapo! Na Guilda! …Espera. Esse sapo tem a tua mochila. {nome}?!" |
| `lyra_arma_nova` | arma equipada pela 1.ª vez com raridade Épica ou melhor | feliz | "Que arma é ESSA? Brilha! Posso pôr no registo como 'arma muito brilhante'?" |
| `lyra_animal` | `animal != nenhum` (1.ª vez) | feliz | "Tens um animal! Posso fazer-lhe festas? Ele pode registar-se na Guilda? Não pode. Mas eu faço-lhe um cartão na mesma." |
| `lyra_comp_mia` | `companheiro(mia)` | feliz | "Mia! Tens um ar tão profissional! …Tira o pau do bolso, já tens um arco." |
| `lyra_comp_kai` | `companheiro(kai)` | feliz | "Os dois juntos! Os números 9 999 e 10 000! Parece o início de uma canção do Lucien." |
| `lyra_comp_gorvan` | `companheiro(gorvan)` | surpresa | "O Mestre vai SUBIR? Contigo? Quem é que fica a assinar os papéis?! …Eu, pois." |
| `lyra_classe` | 1.ª conversa depois de escolher classe | feliz | "{classe}! Tenho de mudar a tua ficha. Adoro mudar fichas. Já disse que adoro mudar coisas?" |
| `lyra_nivel_10` | `nivel >= 10` (1.ª vez) | normal | "Nível 10? Fala com o Mestre Gorvan. Ele escolhe a tua classe contigo. Ou seja, diz 'Hmm' e tu escolhes." |
