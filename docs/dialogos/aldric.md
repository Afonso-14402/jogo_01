# Governador Aldric — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.20. Dados: `dados/dialogos/aldric.json`.
Melhorias da cidade e casas: `docs/CIDADES.md`, secções 1.4 e 2. Primeiro discurso: cena C1-11 (`docs/guiao/cap01_floresta.md`).

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios, rápidos e aos solavancos; param quando ele procura um papel |
| Como fala | nervoso, educado, cheio de palavras de repartição ("conforme", "em anexo", "despacho"); quando se emociona, esquece-se e fala como gente |
| Repete | "Carimbo.", "Em triplicado.", "A cidade agradece.", "Conforme o regulamento… que eu escrevi." |
| Tiques | carimba coisas quando está nervoso, mesmo que não sejam papéis (animação `carimbar`) |
| Nunca diz | "não sei" (diz "vou averiguar"); mal da cidade |
| Chama ao herói | "Jogador nº 10 000" (com o título por extenso) ao início; `{nome}` a partir dos 4 corações |
| Quem é | 50 anos. Era escrivão da Câmara. Foi eleito governador há 10 anos "porque mais ninguém quis". Sabe o nome de todos os habitantes |
| Rotina | Câmara 8:00–18:00 · inaugurações na Praça (quando uma melhoria acaba, às 10:00) · ao Domingo passeia pela cidade com um caderno, a apontar buracos na calçada |

---

## 2. Primeira conversa

- **Governador Aldric** *(nervoso)*: "Ah! O Jogador nº 10 000! Em pessoa! Um momento." 🎬 Carimba um papel. "Pronto. Está registad{o/a} como cidad{ão/ã} provisóri{o/a}. Bem-vind{o/a}."
- **Governador Aldric** *(normal)*: "Sou o Governador Aldric. A minha função é… tudo. Pontes, fontes, impostos, gatos presos em telhados."
- **Governador Aldric** *(feliz)*: "Se trouxer materiais da torre, a cidade cresce. Faço uma lista. Faço sempre uma lista. Tenho uma lista das listas."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Projetos da cidade · Missões · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `aldric_dia_01` | `hora entre 8 e 10` | normal | "Bom dia. Tenho quarenta e dois papéis para assinar antes do almoço. Já assinei um. Era o errado." |
| `aldric_dia_02` | `hora entre 12 e 14` | normal | "Hora de almoço. Como na secretária. A sopa da Dona Marta tem manchas em metade dos documentos da cidade." |
| `aldric_dia_03` | `hora entre 16 e 18` | triste | "Fim do dia e a pilha está maior do que de manhã. Os papéis reproduzem-se. Tenho a certeza." |
| `aldric_dia_04` | — | normal | "Carimbo. Carimbo. Isto não se carimba. Porque é que isto não se carimba?" |
| `aldric_dia_05` | — | feliz | "A cidade agradece. Eu também. Em triplicado." |
| `aldric_dia_06` | — | normal | "Recebi uma queixa: 'o Brom canta alto'. Recebi outra: 'o Brom não canta'. Arquivei as duas." |
| `aldric_dia_07` | — | normal | "O Rook voltou a entrar na Câmara pela janela. Não roubou nada. Deixou um bilhete: 'o telhado tem goteiras'. Tem." |
| `aldric_dia_08` | — | feliz | "Fiz as contas: a cidade tem 2 412 habitantes. 2 413 contigo. Gosto de números que sobem." |
| `aldric_dia_09` | `dia_semana == domingo` | normal | *(na rua)* "Domingo de inspeção. Buraco na calçada número 37. Já é o meu preferido." |
| `aldric_dia_10` | `dia_semana == segunda` | triste | "Segunda-feira. Reunião com os comerciantes. O Tobias vai pedir descontos nos impostos. Vai trazer bolos. Vou aceitar os bolos." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `aldric_dia_20` | `estacao == primavera` | feliz | "Primavera: obras! O tempo bom é para obras. E para formulários de obras." |
| `aldric_dia_21` | `estacao == verao` | normal | "No verão o rio baixa e aparecem coisas no fundo. Três carroças, uma estátua e as chaves que perdi há dois anos." |
| `aldric_dia_22` | `estacao == outono` | normal | "Outono. Varrer folhas da praça custa doze moedas por dia. Estou a pensar em multar as árvores." |
| `aldric_dia_23` | `estacao == inverno` | triste | "No inverno as obras param e os papéis não. Os papéis não têm frio." |
| `aldric_dia_24` | `clima == chuva` | zangado | "Lama! Na Câmara! Limpe os pés. Os dois. Há um tapete. Usamo-lo para isso." |
| `aldric_dia_25` | `clima == neve` | feliz | "Neve! Fechei a Câmara uma hora para fazer um boneco de neve. Não diga a ninguém. Já toda a gente viu." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `aldric_dia_40` | `andar_maximo < 10` | normal | "Andar baixo, ainda. Mas cada andar conta. Literalmente: tenho uma folha para contar." |
| `aldric_dia_41` | `missao(R1_02) == concluida` | feliz | "A Ponte do Rio está nos planos! Quarenta troncos! Só falta o ouro. E o resto. Mas os troncos já cá estão." |
| `aldric_dia_42` | `boss_derrotado(golem_cristal)` | feliz | "Já tem casa! Fui eu que escolhi a rua. É sossegada. Bem, é sossegada até o Gizmo testar coisas." |
| `aldric_dia_43` | `missao(H_08) == concluida && flag(sssar_defendida)` | nervoso | "A Guilda fez uma queixa formal contra si. Tenho-a aqui. Vou… perdê-la. Perdi. Que pena." |
| `aldric_dia_44` | `andar_maximo >= 50` | feliz | "Metade da torre! Vou mandar fazer uma placa. Com o seu nome. Em letras de latão. Ou de cobre. O orçamento decide." |
| `aldric_dia_45` | `missao(H_14) == concluida && missao(H_16) != concluida` | triste | "O nome do Kai está no registo dos desaparecidos. Eu escrevo esse registo. Nunca me custou tanto escrever um nome." |
| `aldric_dia_46` | `andar_maximo >= 90` | normal | "O Monumento à Subida pode começar. Precisa de um troféu de cada região. Já tem quase todos. Eu contei. Duas vezes." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `aldric_dia_60` | `coracoes(aldric) >= 2` | feliz | "Pus o seu processo em cima da pilha. É o único privilégio que um governador pode dar sem ser preso." |
| `aldric_dia_61` | `coracoes(aldric) >= 4` | normal | "Pode tratar-me por Aldric. Só Aldric. Fora do horário de expediente. E dentro também, vá." |
| `aldric_dia_62` | `coracoes(aldric) >= 6` | feliz | "Quando passa pela praça e as pessoas acenam, eu fico à janela a ver. É a melhor parte do meu dia." |
| `aldric_dia_63` | `coracoes(aldric) >= 8` | triste | "Às vezes acordo de noite e penso: e se a cidade estivesse melhor com outra pessoa? Depois lembro-me de que ninguém quer o lugar. Volto a dormir." |
| `aldric_dia_64` | `coracoes(aldric) >= 10` | feliz | "Cidad{ão/ã} de Honra. Escrevi o decreto à mão. Com a caneta boa. A Lyra emprestou-ma." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `aldric_dia_70` | `origem == atrasado` | normal | "Chegou atrasad{o/a} à cerimónia. Outra vez. Já pus na ata: 'o herói chegou com dez minutos de heroísmo'." |
| `aldric_dia_71` | `origem == ajudante` | feliz | "Recebi três cartas de habitantes a agradecer-lhe coisas. Três! Normalmente recebo cartas a reclamar." |
| `aldric_dia_72` | `skill_unica == mao_de_midas` | feliz | "Mão de Midas. Já pensou em doar um bocadinho à cidade? Tenho um formulário. Já preenchido. Só falta assinar." |
| `aldric_dia_73` | `skill_unica == bolsa_infinita` | normal | "Uma mochila sem fundo. Pode guardar-me lá os arquivos de 1 200? Estão a ocupar uma sala inteira." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `aldric_curta_1` | normal | "Mais alguma coisa? Tenho um carimbo à espera." |
| `aldric_curta_2` | feliz | "A cidade agradece. Outra vez. Em duplicado, hoje." |
| `aldric_curta_3` | normal | "Já falámos hoje. Pus na ata." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Governador Aldric** *(normal)*: "Oficialmente, a torre é 'património natural de Ascendia'. Fui eu que escrevi. Não sabia o que pôr."
- **Governador Aldric** *(nervoso)*: "Extraoficialmente… tenho medo dela. A cidade vive dela, come dela, sonha com ela. E não sabemos o que é."
- **Governador Aldric** *(feliz)*: "Mas tem uma coisa boa: traz pessoas como você. Isso eu sei arquivar."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "A madeira da cidade vem do andar 2. Se vir os lenhadores, diga-lhes que o pagamento está atrasado. Não diga. Eu digo." |
| 2 Cavernas | "Os mineiros do andar 11 pedem tochas há meses. Tenho o pedido em cima da mesa. Tenho a mesa em cima do pedido." |
| 3 Pântano | "A Guilda quer que a cidade declare os Homens-Lagarto 'perigosos'. Eu nunca vi um. Não assino o que não vi." |
| 4 Deserto | "Zahra! Uma cidade dentro da torre com banhos públicos. Banhos públicos! Ascendia não tem. Tome notas." |
| 5 Gelo | "Ouvi dizer que no gelo há uma aldeia que se reconstrói. Pergunte-lhes como fazem a papelada." |
| 6 Oceano | "Um porto de piratas reformados! Será que pagam impostos? Não pergunte. Não quero saber." |
| 7 Vulcão | "Os anões do fogo fazem obras com lava. Lava! E eu a lutar com tijolos." |
| 8 Reino Assombrado | "Um reino inteiro com rei e tudo. O rei ainda governa? Morto? Eu estou vivo e mal consigo." |
| 9 Céu | "Os Alados têm um porto de balões. Se trouxer madeira-nuvem, fazemos um. Balões para Ascendia! Sonhe comigo." |
| 10 Abismo | "Lá em cima não há câmaras, nem governadores, nem papéis. Parece o paraíso. Tenha cuidado na mesma." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `aldric_rumor_01` | — | "Há anos que tento recensear o Bairro Baixo. O Rook muda as placas das ruas todas as semanas." |
| `aldric_rumor_02` | — | "A Hana pediu um jardim público. Precisamos de sementes de muitos sítios. Vinte tipos. Ela tem dezanove." |
| `aldric_rumor_03` | — | "O Gizmo quer um 'para-raios gigante' na Praça. A última invenção dele explodiu a fonte. Disse que não." |
| `aldric_rumor_04` | `andar_maximo >= 25` | "A muralha precisa de reforço. Os monstros escapam pela torre e entram na cidade. A Capitã Freya tem uma lista. Eu tenho o orçamento. Não combinam." |
| `aldric_rumor_05` | `andar_maximo >= 40` | "O Lucien quer um teatro. Para fazer peças sobre si. Já li o guião. Você salva a cidade de uma galinha gigante. Não sei de onde ele tirou isso." |
| `aldric_rumor_06` | `andar_maximo >= 85` | "Os Alados mandaram uma carta a dizer que, se fizermos um porto de balões, nos visitam. Uma visita oficial do céu! Tenho de comprar um chapéu." |

### 4.4 A vida dele
| Corações | Fala |
|---|---|
| 0 | "Sou o governador. Nasci em Ascendia, estudei em Ascendia, governo Ascendia. Não sou muito viajado." |
| 2 | "Fui escrivão da Câmara vinte anos. Quando o governador anterior morreu, ninguém se candidatou. Candidatei-me eu para não ficar vazio. Ganhei por um voto. O meu." |
| 4 | "Sei o nome de todos os habitantes. Todos. Não é talento. É que fui eu que os escrevi no registo." |
| 6 | "Nunca subi à torre. Nem ao andar 1. Tenho vertigens no segundo andar da Câmara. Governo uma cidade que vive de subir." |
| 8 | "Tenho medo de falhar à cidade. Todos os dias. Por isso trabalho muito. Ou porque não sei fazer outra coisa." |
| 10 | "Já não tenho tanto medo. Vejo a cidade a crescer e sei que não fui só eu. Foste tu também. E toda a gente. Uma cidade é um trabalho de equipa. Com carimbos." |

---

## 5. Presentes

**Adora:** projetos acabados (cada melhoria inaugurada dá +80 como um presente "adora"), Selo Dourado, Coroa do Reino ·
**Gosta:** papel, chá · **Detesta:** atrasos (falhar o dia de uma inauguração em que prometeste estar), lama (e itens sujos: Gel de Slime, Lodo).

| Reação | Falas |
|---|---|
| Adora | "Um… um selo dourado. Para mim. Vou carimbar a minha própria mão. Não, não vou. Vou." · "A Coroa do Reino! Vai para o museu da cidade. O museu da cidade é uma vitrina na Câmara. Agora tem uma coisa." |
| Gosta | "Papel! Papel bom! Grosso! A cidade agradece. Eu agradeço mais." |
| Neutro | "Obrigado. Vou registá-lo como 'oferta à governação'. É a lei. Inventei-a há pouco." |
| Não gosta | "Ah. Obrigado. Vou… arquivar." |
| Detesta | "Isso está a pingar lama no chão da Câmara. No chão da Câmara! Leve isso daqui, por favor. Por favor em triplicado." |

| Item | Fala |
|---|---|
| Carimbo (decoração) | "Um carimbo novo! Este diz 'APROVADO' com mais força do que o meu. Vou aprovar tudo hoje." |
| Planta de cidade (mapa do Fausto) | "Um mapa! Da cidade! Com os buracos da calçada marcados? Não. Vou marcá-los eu. Obrigado!" |

---

## 6. Aniversário e festivais

**Aniversário (Inverno, dia 14):**
- Sem presente: "Faço anos? Faço. Está na minha agenda. Entre 'reunião sobre esgotos' e 'reunião sobre esgotos, parte 2'."
- Com presente que adora: "Um presente! No meu aniversário! Ninguém me dá presentes! Só formulários! Vou chorar em papel timbrado."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Sou o júri do concurso de flores. Todas as flores são bonitas. Tenho de escolher uma. É o pior dia do ano." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Dançar? Em público? O governador? …Uma dança protocolar. Curta. Com dignidade." ⚙ +100 |
| F_02 Festival da Pesca | "Entrego os prémios. O Pip é o juiz. É a única pessoa que eu vi pescar uma bota e chamar-lhe 'troféu'." |
| F_03 Noite dos Espíritos | "Os fantasmas desta noite estão autorizados. Assinei a licença. Os outros, não." |
| F_04 Festival da Estrela | "O fogo de artifício custou trezentas moedas. Vale cada moeda. Não diga ao Tobias que eu disse isto." |
| F_05 Dia da Subida | *(no palco, discurso)* "Cidadãos de Ascendia. Hoje… hum… *(procura a página)* … hoje é um dia histórico. Outra vez. Graças a {nome}. Viva!" |
| F_06 Concurso da Casa | "Sou jurado com o Lucien. Eu vejo os acabamentos. Ele vê o 'drama'. Discutimos muito." |
| F_07 Noite das Lanternas | "Registo todas as lanternas. Não por obrigação. Para que os nomes fiquem escritos em algum sítio oficial." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "O Javali-Rei derrotado! Os lenhadores vão poder colher maçãs no andar 5. A cidade vai ter tartes. Tartes são economia." |
| Ent Ancião (10) | "O primeiro Dia da Subida em anos! O discurso correu… correu. Perdi a página três. Ninguém notou. Notaram." |
| Aranha-Mãe (15) | "Os aventureiros resgatados vão viver para cá. Já lhes arranjei casa. Bem, um quarto. Bem, uma promessa de quarto." |
| Golem de Cristal (20) | "Conforme prometido, a cidade oferece-lhe uma casa! Rua das Glicínias, número 7. Tome a chave. E os formulários." |
| Serpente do Lodo (25) | "Mais um andar, mais uma página no Registo da Subida. Estou a ficar sem papel. Bom problema." |
| Hidra do Pântano (30) | "A Arena de prata pode abrir! A Capitã Freya está contente. Quando ela está contente, ninguém nota. Mas eu sei." |
| Escorpião Imperador (35) | "Do deserto vem vidro solar. Com vidro solar fazemos banhos públicos. Com banhos públicos a cidade cheira melhor. Política é isto." |
| Faraó Eterno (40) | "Um rei que governou a torre… e acabou em pó. Fiquei a pensar no meu cargo. Não quero acabar em pó. Quero acabar reformado." |
| Yeti Ancião (45) | "Pelo de yeti! Para os casacos de inverno da cidade! Não? É um troféu? Pronto. Não está cá quem falou." |
| Dragão de Gelo (50) | "Metade da torre! Grande festa! Encomendei quinhentos pastéis. A Dona Marta vai matar-me." |
| Capitão Esqueleto (55) | "O ouro dos piratas mortos… não é da cidade, pois não? Não. Claro que não. Era só para saber." |
| Leviatã (60) | "O Dia da Subida vai ser mais pequeno. Por causa do Kai. Ninguém mo pediu. Eu decidi. Às vezes decido." |
| Ferreiro Infernal (65) | "O Brom pediu-me uma licença para 'forjar uma coisa importante'. Dei-lha sem perguntar. Às vezes não se pergunta." |
| Kai — salvo (68) | "Vou tirar o nome do Kai do registo dos desaparecidos. Com a borracha boa. Não, vou riscar e escrever por cima 'VOLTOU'." |
| Kai — vencido (68) | "Não há formulário para isto. Desculpe. Não sei o que dizer quando não há formulário." |
| Titã de Magma (70) | "A Torre de Vigia pode ser construída! Obsidiana! Lá de cima vamos ver os andares todos. Bem, mais ou menos." |
| Lich Bibliotecário (75) | "O Fausto pediu um aumento de estantes. Pela primeira vez em trinta anos, disse que sim antes de ele acabar a frase." |
| Rei Sem Coroa (80) | "Um rei que pediu desculpa. Vou pôr a frase na parede da Câmara: 'Os reis também pedem desculpa.' Para os próximos governadores." |
| Grifo Real (85) | "O Porto de Balões! Os Alados vêm visitar! Comprei o chapéu. É alto. Tenho vertigens no chapéu." |
| Serafim Caído (90) | "O Dia da Subida foi em silêncio. Por sua causa. Por respeito. A cidade sentiu que alguma coisa mudou. Eu também." |
| Guardião do Tempo (95) | "Cinco andares. A cidade inteira está à espera. Eu tenho um discurso pronto para o fim. Tenho dois. Um para cada… não. Tenho um." |

---

## 8. Cenas de coração

### ❤️ 2 — Adormecido nos papéis

| | |
|---|---|
| ID | `cena_aldric_2` |
| Quando | 2 ❤️ · entrar na Câmara entre as 17:00 e as 18:00 |
| Onde | gabinete do governador |
| Quem | herói, Aldric |
| Música | `ascendia_dia` (calma) |

🎬 Pilhas de papéis por todo o lado. O Aldric dorme sentado, com a cara em cima de um formulário e o carimbo na mão.
🎬 Ressona. A cada ressonar, o carimbo bate no papel: *APROVADO. APROVADO.*

▶ **(Tirar-lhe o carimbo da mão.)**
▶ **(Acordá-lo.)**

- *(carimbo)* 🎬 o Aldric acorda de repente. **Aldric** *(surpresa)*: "Não aprovei nada! Aprovei? Aprovei a construção de quê? …De 'um lago de sopa'? Quem escreveu isto?! Ah. Fui eu. A sonhar." ⚙ +30
- *(acordar)* **Aldric** *(envergonhado)*: "Não estava a dormir. Estava a… rever com os olhos fechados. É um método."
- **Aldric** *(normal)*: "Obrigado. A sério. Às vezes fico aqui até de manhã. A cidade não pode parar porque eu estou cansado."

⚙ +30 extra se trouxeres um chá ao gabinete nessa cena (opção aparece se tiveres Chá no inventário).

### ❤️ 4 — A maqueta

| | |
|---|---|
| ID | `cena_aldric_4` |
| Quando | 4 ❤️ · entrar na Câmara de manhã (8:00–12:00) |
| Onde | sala das traseiras da Câmara |
| Quem | herói, Aldric |
| Música | `guilda` (versão de caixa de música) |

🎬 Uma mesa enorme com uma **maqueta de Ascendia** feita de madeira e papel: casinhas, a torre de cartão, o rio de vidro azul.
🎬 Há peças por pintar: uma ponte, uma fonte, um teatro, um porto de balões.

- **Aldric** *(feliz)*: "Ninguém conhece esta sala. É a minha maqueta. Faço-a há dez anos. Uma casinha por cada casa da cidade."
- **Aldric** *(normal)*: "As peças por pintar são os projetos que ainda não fizemos. Quando um acaba, pinto-o. É a minha maneira de festejar."
- 🎬 Aponta para a ponte pintada de fresco. "Esta foi a sua. A Ponte do Rio. Pintei-a ontem à noite."

▶ **"Vamos pintar a maqueta toda."**
▶ **"Põe também a minha casa."**

- *(toda)* **Aldric** *(feliz)*: "Toda! Não há tinta que chegue. Vou encomendar. Em triplicado." ⚙ +30
- *(casa)* **Aldric** *(feliz)*: "Já está. Olhe." 🎬 uma casinha com uma bandeira pequena. "Pus-lhe uma bandeira. É ilegal pôr bandeiras nas casas. Abri uma exceção." ⚙ +30

⚙ Os projetos da cidade ficam **10% mais baratos** em ouro. Recebe uma **Casinha da Maqueta** (decoração).

### ❤️ 6 — O Censo

| | |
|---|---|
| ID | `cena_aldric_6` |
| Quando | 6 ❤️ · falar com ele na Câmara |
| Onde | gabinete |
| Quem | herói, Aldric |
| Música | `guilda` |

- **Aldric** *(nervoso)*: "Tenho um problema. O registo da cidade diz 2 412 habitantes. Mas eu acho que há mais. Ou menos. Ou outros."
- **Aldric** *(normal)*: "Preciso de um censo. Falar com toda a gente num dia. Os vinte de sempre e… os outros. Os que vieram viver para cá por sua causa."
- **Aldric** *(feliz)*: "Faria isso por mim? Dou-lhe uma prancheta. É uma prancheta oficial."

⚙ Missão **N_ALDRIC_3 O Censo** (secção 9). O Aldric aceita jantar em tua casa (traz sobremesa e um formulário de satisfação).

### ❤️ 8 — O medo de falhar

| | |
|---|---|
| ID | `cena_aldric_8` |
| Quando | 8 ❤️ · noite de invasão à cidade (N_FREYA_3) ou de trovoada · na muralha, 21:00–23:00 |
| Onde | cimo da muralha sul |
| Quem | herói, Aldric |
| Música | `tristeza` (versão curta) |

🎬 O Aldric está encostado ao muro, sem casaca, a olhar para a cidade às escuras.

- **Aldric** *(triste)*: "Sabe o que faço quando há perigo? Nada. Assino papéis. A Freya luta, a Célia cura, você sobe. Eu assino."
- **Aldric** *(triste)*: "Tenho medo de que um dia a cidade precise de mim e eu só tenha um carimbo para lhe dar."

▶ **"Os teus papéis construíram a ponte."**
▶ **"A cidade confia em ti."**
▶ **(Ficar calad{o/a} ao lado dele.)**

- *(ponte)* **Aldric** *(surpresa)*: "…É verdade. Sem papéis não há ponte. Sem ponte não há atalho. Sem atalho, o Pip chegava atrasado. Mais atrasado." ⚙ +30
- *(confia)* **Aldric** *(triste)*: "Confia porque não tem alternativa." 🎬 pausa. "…Mas confia. Obrigado."
- *(calado)* 🎬 Os dois ficam a olhar para a cidade. As luzes acendem-se uma a uma. **Aldric**: "Olhe. Cada luz é uma casa que está bem. Conto-as todas as noites." ⚙ +30

⚙ 15% de desconto nos projetos da cidade (acumula com o da maqueta). Passa a mandar **cartas** (com chá, papel bom e "decretos" engraçados).

### ❤️ 10 — A Chave da Cidade

| | |
|---|---|
| ID | `cena_aldric_10` |
| Quando | 10 ❤️ · pelo menos **8 melhorias da cidade** acabadas · Praça, 10:00 |
| Onde | Praça da Torre, com um palco e toda a cidade |
| Quem | herói, Aldric, os NPCs de Ascendia, aldeões |
| Música | `tema_aldric` (fanfarra pequena, depois cordas) |

🎬 A Praça está cheia. O Aldric está no palco com uma caixa de veludo. Treme. Tem o discurso numa pilha de 14 folhas.
🎬 Olha para a pilha. Olha para a cidade. Põe a pilha de lado.

- **Aldric** *(nervoso)*: "Cidadãos. Eu tinha um discurso. Catorze páginas. Vou… não o ler."
- 🎬 A Lyra, na plateia, deixa cair a caneta de surpresa.
- **Aldric** *(normal)*: "Há dez anos que trabalho para que Ascendia seja um sítio bom para viver. Sozinho, não consegui. Com {nome}, conseguimos."
- **Aldric** *(feliz)*: "Ponte, fonte, luzes, jardim… Não fui eu. Foi quem subiu e quem ficou cá em baixo à espera."
- 🎬 Abre a caixa: uma chave grande de bronze, com a torre gravada.
- **Aldric** *(feliz)*: "A Chave da Cidade. Abre todas as portas de Ascendia. Bem, nenhuma porta. É simbólica. Mas os comerciantes respeitam-na."
- **Tobias** *(da plateia)*: "Dez por cento! Respeitamos dez por cento!"
- 🎬 Aplausos. O Aldric, no meio do barulho, carimba a mão do herói: *CIDAD{ÃO/Ã} DE HONRA*.

⚙ **Chave da Cidade**: tudo em Ascendia 10% mais barato. Título *Cidad{ão/ã} de Honra*.

---

## 9. Missões

### R1_02 — Madeira para a Ponte (a parte do Aldric)
- Depois de entregares os 40 Carvalho ao Bruno (`docs/dialogos/povoacoes_r01.md`), o projeto **Ponte do Rio** aparece na Câmara.
- **Aldric** *(feliz)*: "Quarenta troncos! O Bruno mandou-os com um bilhete que diz 'AH-AH'. Arquivei. Agora só faltam quinhentas moedas. A cidade tem trezentas. Pode ajudar? Não precisa. Mas pode."
- **Inauguração** (3 dias depois, 10:00) — *(no palco)* "Declaro a Ponte do Rio… aberta! Ao trânsito, aos peões e ao Pip, que chega sempre atrasado." ⚙ a ponte aparece no mapa (`docs/mapas/ascendia.md`) · +80

### Melhorias da cidade (todas)
- **Pedir** (menu Projetos) — "Projeto: {nome}. Custo: {materiais} e {ouro}. Efeito: {efeito}. Quer contribuir?"
- **Ao entregar** — "Recebido! A obra começa amanhã e demora três dias. Os operários pedem silêncio. Não vão ter."
- **Inauguração** — o Aldric faz um discurso curto na Praça às 10:00 do dia em que a obra acaba; se estiveres lá, +80 amizade (conta como presente "adora"); se não estiveres e tinhas dito que ias, −20 ("atraso").
- Falas de inauguração de cada projeto: *"Declaro {projeto} aberto! {frase}"* — Fonte Nova: "Não atirem moedas. Bem, atirem: revertem para a cidade." · Escola de Aventureiros: "Aprendam a fugir. É a primeira lição." · Teatro: "O Lucien prometeu peças curtas. Prometeu." · Hospital: "Espero que nunca precisem dele. Precisam. Mas espero." · Monumento à Subida: "A estátua é maior do que a pessoa. As estátuas são sempre."

### N_ALDRIC_3 — O Censo (6 ❤️)
- **Passos**: num só dia (6:00–2:00), **falar com os 20 NPCs de Ascendia** e com **todas as pessoas que se mudaram para a cidade** (ver `docs/CIDADES.md`, secção 1.5: Tina, Bolota, Pedrito…). A prancheta marca quem falta.
- O Rook só aparece à noite nos telhados; o Zed às vezes está fora (não conta se estiver fora); a Mia esconde-se (tem de se encontrar na Igreja ou no rio).
- **Durante** — **Aldric**: "Já vai em {n}? Ótimo. O Rook conta como um. Embora diga que são três."
- **Entregar** — **Aldric** *(feliz)*: "2 431! Mais dezanove do que o registo! Gente que veio por sua causa. A cidade cresceu e eu não tinha papelada para isso. Agora tenho." ⚙ +200 (❤️❤️) · título *Recenseador*

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `aldric_estado_vida` | `vida_pct < 30` | surpresa | "Está ferid{o/a}! Tenho um formulário de baixa médica! Não, vá à Igreja. Preencho depois." |
| `aldric_estado_lama` | `estado(encharcado)` ou vindo do pântano | zangado | "Lama! No chão! Da Câmara!" |
| `aldric_estado_cansado` | `estado(cansado)` | normal | "Também está cansad{o/a}? Somos dois. Vá dormir. Pelo menos um de nós." |
| `aldric_casa` | 1.ª vez depois de receber a casa | feliz | "Gosta da casa? Se precisar de obras, há um formulário. Se precisar de vizinhos simpáticos, a rua é sossegada." |
| `aldric_comp_kai` | `companheiro(kai)` | feliz | "Kai! Tenho de lhe dar o registo de cidadão. Está em atraso há oito meses. Assine aqui. E aqui. E aqui." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `aldric_serv_projetos` | abrir Projetos | normal | "Projetos da cidade. Os que pode ajudar estão a verde. Os outros ainda dependem da torre." |
| `aldric_serv_doar` | contribuir para um projeto | feliz | "Registado. A cidade agradece. Em triplicado." |
| `aldric_serv_falta` | faltam materiais | normal | "Faltam {lista}. A lista também está anexada. Em duas vias." |
| `aldric_serv_casa` | comprar uma casa maior | feliz | "Uma casa maior! Assine aqui. A escritura está pronta em três dias. E a mudança, quando quiser." |
| `aldric_serv_fechado` | 18:00–8:00 | — | `[Sistema] A Câmara está fechada. Há luz no gabinete do governador.` |
