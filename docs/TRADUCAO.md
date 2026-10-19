# Tradução (português → inglês)

O jogo é escrito em **português de Portugal** e traduzido para **inglês** (PT e EN no menu: `docs/INTERFACE.md`).
Como funciona no código: `docs/PROGRAMACAO.md` (ficheiros CSV `traducoes/*.csv` com as colunas `chave, pt, en`).

A tradução faz-se **quando os textos passarem para os ficheiros de dados** (fase B), região a região, com a Demo
primeiro. Este documento diz **como** se traduz, para ficar sempre igual: as regras e o glossário dos nomes.

---

## 1. Regras

| Regra | Como |
|---|---|
| Tom | o mesmo do português: frases curtas, simples, com humor. Inglês "neutro" (nem muito britânico nem muito americano); ortografia **americana** (color, armor) |
| Tamanho | uma caixa de diálogo tem no máximo 3 linhas de ~40 letras. O inglês costuma ser mais curto; se ficar maior, corta-se, não se encolhe a letra |
| Nomes de pessoas | **não se traduzem** (Lyra, Gorvan, Dona Marta → "Dona Marta", Mãe Dois → ver glossário) |
| Nomes de sítios e coisas | traduzem-se quando têm significado (Prado do Despertar → Meadow of Waking); ficam quando são nomes próprios (Ascendia, Zahra, Coralina) |
| Género do herói | o inglês quase não tem: `{o/a}` vira a mesma palavra; "Jogador{/a}" → "Player". Os pronomes do herói (they/he/she) vêm do **Tratamento** escolhido na criação (`docs/INTERFACE.md`, secção 6) e usam `{they/he/she}` |
| `[Sistema]` | → `[System]`. As **falhas** da região 10 traduzem-se com o mesmo tipo de erro (`[Sytsem]`, números trocados) |
| Sotaques | os Ssar arrastam o "s" ("Ssss", "assim") → em inglês também ("Yess", "thiss"). Os anões e os Torrenses não têm sotaque escrito |
| Rimas e canções | traduz-se o sentido e faz-se uma rima nova; não se traduz palavra a palavra |
| Piadas | se a piada não funcionar em inglês, escreve-se outra parecida no mesmo sítio |
| Datas e números | 10 000 → 10,000 · 1,5 → 1.5 · horas em 24 h ficam iguais |

---

## 2. Glossário

### 2.1 Mundo e história

| Português | Inglês |
|---|---|
| a Torre | the Tower |
| Ascendia | Ascendia |
| Jogador / Jogador nº 10 000 | Player / Player No. 10,000 |
| o Sistema · a janela azul | the System · the blue window |
| Administrador | Administrator |
| Skill Única | Unique Skill |
| Cristal de Avaliação · Cristal Mestre | Appraisal Crystal · Master Crystal |
| Zona Segura | Safe Zone |
| guardião (de andar) | floor guardian |
| monstro com nome | named monster |
| Dia da Subida | Ascension Day |
| Guilda de Aventureiros | Adventurers' Guild |
| rank (F a SSS) | rank (F to SSS) |
| Prado do Despertar | Meadow of Waking |
| os Perdidos · Cidade dos Perdidos | the Lost · City of the Lost |
| Último Posto | Last Outpost |
| Biblioteca do Mundo · a Arquivista | Library of Worlds · the Archivist |
| Andares do Eco | Echo Floors |
| Bosses Despertos | Awakened Bosses |
| página de lore · Diário de A. | lore page · The Diary of A. |
| Ponto Sem Retorno | Point of No Return |
| Cidade Errante (Vagar) | the Wandering City (Vagar) |
| Ponte para as Estrelas | Bridge to the Stars |

### 2.2 Os finais

| Português | Inglês |
|---|---|
| Voltar a Casa | Going Home |
| O Novo Administrador | The New Administrator |
| Libertar os Mundos | Set the Worlds Free |
| A Ponte | The Bridge |

### 2.3 Personagens com nome que se traduz

| Português | Inglês |
|---|---|
| Mestre Gorvan | Guildmaster Gorvan |
| Capitã Freya | Captain Freya |
| Irmã Célia | Sister Célia |
| Velho Fausto | Old Fausto |
| Madame Oriel | Madame Oriel |
| Dona Marta | Dona Marta (é um título português: fica) |
| Governador Aldric | Governor Aldric |
| "Mãe Dois" | "Mother Two" |
| "Doutor" | "Doc" |
| O Desistente | The Quitter |
| O Jogador Sem Número | The Numberless Player |
| Sargento Bruma | Sergeant Bruma |
| Chico das Memórias | Chico of Memories |
| Os Imortais (a equipa do Gorvan) | the Immortals |

### 2.4 Bosses (títulos)

| Boss | Título PT | Título EN |
|---|---|---|
| Javali-Rei | O Rei das Tocas | King of the Burrows |
| Ent Ancião | Guardião da Floresta | Guardian of the Forest |
| Aranha-Mãe | A Mãe do Ninho | Mother of the Nest |
| Golem de Cristal | O Rei Sentado | The Seated King |
| Serpente do Lodo | A Guardiã do Ovo de Pedra | Keeper of the Stone Egg |
| Hidra do Pântano | A Que Não Morre | The One Who Won't Die |
| Escorpião Imperador | Imperador das Areias | Emperor of the Sands |
| Faraó Eterno | O Que Também Subiu | The One Who Also Climbed |
| Yeti Ancião | O Que Se Lembra | The One Who Remembers |
| Dragão de Gelo | O Meio do Caminho | The Halfway Point |
| Capitão Esqueleto | O Contador de Ouro | The Gold Counter |
| Leviatã | O Último do Mar | The Last of the Sea |
| Ferreiro Infernal | O Que Forjou o Teu Número | The One Who Forged Your Number |
| Titã de Magma | O Coração do Vulcão | Heart of the Volcano |
| Lich Bibliotecário | O Que Leu Demais | The One Who Read Too Much |
| Rei Sem Coroa | O Que Tentou Parar a Torre | The One Who Tried to Stop the Tower |
| Grifo Real | O Pai dos Ninhos | Father of Nests |
| Serafim Caído | O Que Serviu o Administrador | The One Who Served the Administrator |
| Guardião do Tempo | O Que Te Viu Mil Vezes | The One Who Saw You a Thousand Times |
| O Administrador | Aren, Jogador nº 1 | Aren, Player No. 1 |

### 2.5 Materiais (tiers)

| Tier | PT | EN |
|---|---|---|
| 1 | Cobre | Copper |
| 2 | Ferro | Iron |
| 3 | Aço | Steel |
| 4 | Prata | Silver |
| 5 | Gelo Eterno | Everice |
| 6 | Coral Abissal | Abyssal Coral |
| 7 | Obsidiana | Obsidian |
| 8 | Mitril | Mithril |
| 9 | Oricalco | Orichalcum |
| 10 | Estelar | Stellar |

### 2.6 Estados

| PT | EN |
|---|---|
| Veneno · Queimadura · Frio · Congelado · Choque | Poison · Burn · Chill · Frozen · Shock |
| Atordoado · Sangrar · Lentidão · Cegueira · Medo | Stunned · Bleed · Slow · Blind · Fear |
| Maldição · Encharcado · Parado · Silêncio | Curse · Soaked · Stopped · Silenced |
| Agarrado · Preso · Puxado · Partida · Controlos trocados | Grabbed · Rooted · Pulled · Trick · Reversed Controls |

---|---|
| Veneno · Queimadura · Congelado · Choque | Poison · Burn · Frozen · Shock |
| Lentidão · Atordoado · Cegueira · Medo | Slow · Stunned · Blind · Fear |
| Encharcado · Amaldiçoado · Parado · Silêncio | Soaked · Cursed · Stopped · Silenced |
| Cansado · Calor · Frio | Tired · Heat · Cold |

---

## 3. Frases que têm de ficar iguais (pistas da história)

Estas frases **repetem-se** de propósito em sítios diferentes. Têm de ser traduzidas **sempre da mesma maneira**:

| PT | EN | Onde |
|---|---|---|
| "Não sejas como o anterior." | "Don't be like the one before." | Árvore-Mãe (andar 10) e mais tarde |
| "Estás quase. Não pares." | "You're almost there. Don't stop." | Sistema (andar 89+) e página 90 ("Não pares") |
| "Vem." | "Come." | Sistema (andar 99), página 89 |
| "Desculpa." | "I'm sorry." | Sistema (andares 90 e 99) |
| "— A." | "— A." | assinatura do diário |
| "Talvez tu." | "Maybe you." | Rei Sem Coroa |
| "O escuro tem chão." | "The dark has a floor." | expedição do Orsi (andar 91) |
| "Desistir?" | "Give up?" | a última janela do Administrador |
| "Obrigado. — A." | "Thank you. — A." | final 1 (telemóvel) |
