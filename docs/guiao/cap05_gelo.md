# Guião — Capítulo 5: Gelo (andares 41–50)

Missões: **H_12 O Diário de Gorvan** (= R5_06), **H_13 O Meio do Caminho**. Povoações e missões secundárias:
`docs/dialogos/povoacoes_r05.md`. Mapas: `docs/mapas/r05_gelo.md`.

**O que este capítulo conta**: o frio e a solidão. O herói encontra o **diário da antiga equipa do Gorvan** e, pela
primeira vez, o Gorvan conta o que aconteceu no andar 74. No meio da torre, o Dragão de Gelo diz "Os outros vinham
com amigos." O Sistema começa a ser **simpático** (`[Sistema] Boa, Jogador.`) — e o Kai desconfia. No fim, o Kai
decide ir **à frente, sozinho**: é a última vez que o vemos antes do capítulo 6.

**Flags deste capítulo**: `pena_amarela` (C5-03), `kai_aurora` (C5-06), `kai_vai_sozinho` (C5-09).

---

## C5-01 — O Frio

| | |
|---|---|
| ID | `cena_c5_01_tundra` |
| Quando | entrar pela primeira vez no andar 41 |
| Onde | andar 41, Planície Branca |
| Quem | herói |
| Música | `tundra_silencio` |

🎥 A escada de luz abre-se numa planície branca sem fim. Vento a levantar neve. Silêncio quase total: só o vento e os passos na neve.
🎬 O herói respira e sai-lhe fumo da boca. Encolhe os ombros.
- `[Sistema] Aviso: frio. Barra de Temperatura ativa.`
- `tut_temperatura`: `[Sistema] Temperatura: o frio desce a barra. Perto de fogueiras sobe. Comida quente também ajuda.`
🎬 Ao longe, através da neve, uma manada de **mamutes** passa devagar. O maior tem pássaros nas costas e musgo no pelo. Nenhum olha para o herói.
🎬 O herói dá mais uns passos e para. Abre a janela do Sistema sem querer (o gesto do frio). A janela mostra uma linha nova, diferente das outras:
- `[Sistema] Boa, Jogador. Continua.`
🎬 O herói fica a olhar para a mensagem. Ela desaparece mais devagar do que as outras.

⚙ Sem falas. É a **primeira vez** que o Sistema diz uma coisa simpática (ver `docs/HISTORIA.md`, "O Sistema muda contigo"). A partir daqui, `[Sistema] Boa, Jogador.` aparece às vezes ao vencer um guardião.

---

## C5-02 — Pinhal-do-Norte

| | |
|---|---|
| ID | `cena_c5_02_pinhal` |
| Quando | entrar pela primeira vez em Pinhal-do-Norte (andar 42) |
| Onde | andar 42, praça da aldeia → salão comunal |
| Quem | herói, Ulf Barba-Gelo, Leif, aldeões |
| Música | `pinhal_aldeia` |

🎬 Casas de troncos com telhados de relva cobertos de neve. Fumo nas chaminés. Um cheiro a pão e a resina.
🎬 Um rapaz pequeno (Leif) atira uma bola de neve. Acerta no herói. Foge a rir.
🎬 Um homem enorme de barba branca cheia de gelo sai do salão comunal, com uma caneca fumegante em cada mão.
- **Ulf** *(feliz, voz enorme)*: "Ha! Um da escada! Com cara de gelo! Toma, bebe. Não perguntes o que é. É quente. É o que interessa."
- **Ulf** *(normal)*: "Sou o Ulf. Mando nisto. Ou seja: corto lenha, resolvo discussões e como primeiro. Entra, entra. Ninguém fica à porta em Pinhal-do-Norte."
- 🎬 Dentro do salão: uma lareira do tamanho de uma casa. Dezenas de pessoas a comer, a cantar, a discutir. Ninguém olha para a janela azul do herói.
- **Ulf** *(normal)*: "Janela azul? Hm? Ah, isso. Vimos alguns com isso. Não ligamos. Aqui o que conta é se sabes cortar lenha e contar uma boa história."

▶ **"Sei contar uma boa história."**
▶ **"Sei cortar lenha."**

- *(história)* **Ulf** *(feliz)*: "Então conta-a no Solstício! À lareira! Se for má, cantamos por cima!"
- *(lenha)* **Ulf** *(feliz)*: "Ha! Amanhã de manhã. Serração. Vamos ver se é verdade."

⚙ Desbloqueia **Pinhal-do-Norte** (salão, cristal, loja, sauna). Missões R5_01 a R5_04 e R5_09 disponíveis. A **Bjorn e a Sif** (antiga equipa da Freya) vivem aqui (`docs/dialogos/povoacoes_r05.md`, secção 1.6).

---

## C5-03 — O Que Se Lembra

| | |
|---|---|
| ID | `cena_c5_03_yeti` |
| Quando | vencer o Yeti Ancião (andar 45) |
| Onde | andar 45, Gruta do Yeti |
| Quem | herói |
| Música | `yeti` → silêncio |

🎬 O Yeti cai de joelhos. Antes de cair de vez, leva a mão ao colar, como para o proteger.
🎬 Quando se desfaz em neve, o colar fica no chão. É feito de corda de pelo e cheio de **coisas penduradas**:
- um relógio de pulso digital, parado nas 7:42;
- uma chave de casa com um porta-chaves de um gato;
- um botão de casaco;
- uma **pena amarela**, de flecha;
- uma medalha de escola com um número e nenhum nome.
- um elástico de cabelo preto, muito velho, quase a desfazer-se (é do Aren: página 45; ninguém o diz).
🎬 Atrás do sítio onde o Yeti estava, um monte de coisas arrumadas com cuidado: uma boneca de pano, um sapato pequeno, um caderno sem capa.
- `[Sistema] Mini-boss derrotado: Yeti Ancião.`
- `[Sistema] Unidade de guarda 45: desativada.`
- `[Sistema] Obtiveste: Colar do Yeti.`
🎬 O herói pega na boneca. Tem um nome bordado na saia, já ilegível.

⚙ Recompensas normais: **Punhos do Yeti**, título *Coração Quente*, **Colar do Yeti** (troféu). A **boneca** é um presente que a **Mia adora** (`docs/dialogos/mia.md`). A página 45 está no monte de brinquedos.
⚙ A **pena amarela** fica no inventário como **Pena Amarela** (item especial) · flag `pena_amarela`. Se a levares ao Gorvan na cena C5-05, a cena muda (ver lá).

---

## C5-04 — O Sino

| | |
|---|---|
| ID | `cena_c5_04_sino` |
| Quando | tocar o sino da Torre do Sino 3 vezes à meia-noite (andar 46), depois de falar com a Inga |
| Onde | andar 46, Torre do Sino |
| Quem | herói, (Caçadores Congelados ao longe), Caçadora Inga |
| Música | `pinhal_aldeia` (versão triste, só um violino) → sino |

🎬 Meia-noite. Nevasca. O herói sobe a escada podre da torre e puxa a corda. O sino toca uma vez. Duas. Três.
🎬 Lá em baixo, na neve, os **Caçadores Congelados** param todos ao mesmo tempo. Alguns viram a cabeça para a torre.
- **Caçador Congelado** *(voz de gelo, ao longe)*: "…O sino… Já é hora de voltar…?"
🎬 Com o último toque, cai qualquer coisa de dentro do sino: um embrulho de pele de foca atado com corda. Bate no chão de madeira.
🎬 Dentro: um **diário** de capa de couro, com as páginas onduladas pela neve. Na primeira página, uma letra apressada:
- 📜 *"Diário de viagem. Equipa sem nome (o Téo quer chamar-nos 'Os Imortais'. Recusamos. Por enquanto.)"*
🎬 O herói folheia. Mapas desenhados à mão. Listas de comida. Piadas escritas na margem com outra letra. Na última página escrita:
- 📜 *"Andar 46. Três noites na aldeia dos caçadores. Simpáticos, falam pouco. O teimoso dormiu ao pé da lareira as três noites e diz que não tem frio. Mentiroso."*
- 📜 *"Amanhã subimos. Deixo o diário no sino, para não molhar mais. Venho buscá-lo na descida. O Téo diz que dá azar. O Téo diz que tudo dá azar. — O."*
🎬 O herói fecha o diário. Lá em baixo, a Inga está à porta da cabana, a olhar para a torre.
- **Inga** *(normal)*: "Há vinte anos passou por aqui uma equipa de cinco. Ficaram três noites. Um era enorme e calado. A minha mãe disse que tinha os olhos mais tristes que já tinha visto. E ainda não lhe tinha acontecido nada."
- **Inga** *(normal)*: "Leva isso. Não é nosso. É de quem voltou."

⚙ Recebe o **Diário da Equipa de Gorvan** (item de missão). `[Sistema] Missão: leva o diário ao Mestre Gorvan.` (H_12 / R5_06)

---

## C5-05 — A Muralha

| | |
|---|---|
| ID | `cena_c5_05_muralha` |
| Quando | entregar o diário ao Gorvan (H_12 pronta). Se for de dia, o Gorvan diz "Hoje à noite. Muralha." e a cena acontece entre as 21:00 e as 24:00 |
| Onde | muralha norte de Ascendia, à noite |
| Quem | herói, Mestre Gorvan |
| Música | silêncio → `tema_gorvan` (muito lento) |

🎬 Noite fria. A muralha norte. A torre ao fundo, com as luzes das escadas a piscar lá no alto.
🎬 O Gorvan está sentado na pedra, de costas. Ouve passos e não se vira.
- **Gorvan** *(normal)*: "Hmm. Vieste."
🎬 O herói estende-lhe o diário. O Gorvan olha para ele muito tempo antes de lhe pegar. Pega com a mão esquerda. Abre na primeira página. Fecha. Abre outra vez.
- **Gorvan** *(normal)*: "A letra dela. Escrevia mal. Sempre escreveu mal."
- **Gorvan** *(triste)*: "Ela dizia que ia buscá-lo na descida."
- 🎬 Silêncio comprido. O vento.
- **Gorvan** *(normal)*: "Há vinte anos. Andar 74. Catacumbas."
- **Gorvan** *(normal)*: "Um monstro feito de ossos. Centenas. Fechou o túnel. Atrás de nós e à frente."
- **Gorvan** *(normal)*: "Os ossos apanharam-me o braço. Este." 🎬 Toca no ombro direito, vazio. "Eu estava à frente da mais nova. Ela ia sempre atrás. Para ver tudo."
- **Gorvan** *(triste)*: "Os outros seguraram o túnel. Gritaram-me. 'Vai. Avisa a Guilda.' Eu fui."
- **Gorvan** *(triste)*: "Fugi."
- 🎬 Fecha o diário.
- **Gorvan** *(normal)*: "Vinte anos. Nunca contei a ninguém. Nem à Marta. Nem à Lyra. Agora contei-te a ti. Não sei porquê."

▶ **"Não fugiste. Mandaram-te ir."**
▶ **"Obrigad{o/a} por me contares."**
▶ *(ficar calad{o/a} e sentar ao lado dele)*

- *(mandaram)* **Gorvan** *(zangado)*: "Não sabes. Não estavas lá." 🎬 Pausa. *(triste)* "…Talvez. Não sei. Vinte anos e não sei." ⚙ +50
- *(obrigado)* **Gorvan** *(normal)*: "Hmm." 🎬 Quase um sorriso. "Não agradeças. Ouviste. É diferente." ⚙ +50
- *(calado)* 🎬 Os dois ficam sentados na muralha, sem falar. A câmara afasta-se. Muito tempo depois: **Gorvan**: "Bom. Isso foi bom." ⚙ +60

**Se tens a Pena Amarela** (`pena_amarela`):
- 🎬 O herói tira a pena do bolso e põe-na na pedra, entre os dois.
- 🎬 O Gorvan olha para ela. Fica imóvel. Pega-lhe com dois dedos, com um cuidado que não combina com a mão enorme.
- **Gorvan** *(triste)*: "Onde…?" 🎬 o herói aponta para cima. "O Yeti. Ela perdeu uma flecha no 45. Chorou meia hora. Era a preferida."
- **Gorvan** *(normal)*: "A mais nova. Tinha dezassete anos. Ria-se alto. Muito alto." 🎬 Guarda a pena dentro do diário. "Fica aqui. Com eles."
- ⚙ +50 a mais · a Pena Amarela vai para o **Gorvan** (aparece mais tarde em cima da secretária dele, dentro de um copo)

- **Gorvan** *(normal)*: "Vai dormir. Amanhã há Guilda." 🎬 Ao levantar-se, diz sem se virar: "…Volta viv{o/a}."

⚙ Missão **H_12** concluída · ❤️❤️ Gorvan (+200). O Gorvan passa a falar um pouco mais (`docs/dialogos/gorvan.md`). Abre a cena de 6 ❤️ do Gorvan.
⚙ Os nomes da equipa aparecem no Diário → Pessoas: *Edrik (Jogador nº 9 961), Odília, Teodoro, Ilsa*.

---

## C5-06 — As Almas que Desistiram

| | |
|---|---|
| ID | `cena_c5_06_aurora` |
| Quando | 1.ª noite no Mosteiro da Aurora (andar 48), depois de falar com o Mestre Kael |
| Onde | andar 48, terraço do mosteiro |
| Quem | herói, Kai, Mestre Kael (ao fundo) |
| Música | `aurora` |

🎬 Noite eterna. Uma aurora enorme, verde e roxa, a ondular no céu. No terraço do mosteiro, um monge varre a neve devagar.
🎬 O Kai está sentado no parapeito, com as pernas para o vazio, a olhar para a aurora. Tem uma caneca de chá que já não fumega.
- **Kai** *(normal)*: "Sabes o que os monges dizem? Que a aurora são as almas dos Jogadores que desistiram. Ficaram aqui. A brilhar. Bonitas e paradas."
- **Kai** *(sério)*: "Eu não vou ser uma luz bonita num céu falso. Recuso."
- 🎬 Pausa. A aurora muda de verde para azul.
- **Kai** *(normal)*: "O Sistema anda simpático contigo? 'Boa, Jogador'?"
- **Kai** *(sério)*: "Comigo também. Mas a mim diz mais coisas. Ontem disse: 'Estás à frente, Jogador nº 9 999. Continua assim e chegas primeiro.' Primeiro. Como se fosse uma corrida. Como se houvesse um prémio."
- **Kai** *(normal)*: "Não lhe respondi. Não se responde a uma janela. …Pois não?"

▶ **"Não confies nele."**
▶ **"Talvez seja só uma mensagem."**
▶ **"E se houver mesmo um prémio?"**

- *(não confies)* **Kai** *(normal)*: "Eu não confio em ninguém que fica simpático de repente. Nem no Tobias quando faz desconto." ⚙ +20 · flag `kai_aurora`
- *(só mensagem)* **Kai** *(sério)*: "As mensagens não dizem 'primeiro'. Alguém escreve isto. Alguém está a ler-me." ⚙ flag `kai_aurora`
- *(prémio)* **Kai** *(surpresa, depois sério)*: "…Pois. E se houver?" 🎬 Fica a olhar para a aurora muito tempo. "Se houver, eu quero-o. Desculpa. Quero mesmo." ⚙ flag `kai_aurora` (o Kai fica mais perto do acordo do capítulo 7; não muda o duelo)
- 🎬 O Mestre Kael passa atrás deles e para.
- **Mestre Kael** *(normal, calmo)*: "Quem corre para a frente não vê o que deixa para trás. Bebam o chá enquanto está quente. É o único conselho que vale a pena."
- 🎬 O Kai olha para a caneca fria. Ri-se baixinho.

⚙ Sem missão.

---

## C5-07 — O Meio do Caminho

| | |
|---|---|
| ID | `cena_c5_07_dragao` |
| Quando | chegar ao Ninho do Dragão (andar 50) |
| Onde | andar 50, topo da montanha |
| Quem | herói (e o companheiro, se houver), Dragão de Gelo |
| Música | vento → `dragao_gelo` |

🎬 O herói atravessa a Ponte do Vento, agarrado às cordas. No topo, um ninho enorme feito de gelo e ossos.
🎬 Do outro lado do pico, uma sombra sobe. Asas que tapam o céu. Escamas de gelo transparente. O dragão pousa e o chão estala.
- **Dragão de Gelo** *(voz grave, lenta)*: "Mais um. Até ao meio. Poucos chegam ao meio."
- *(sozinho)* **Dragão** *(normal)*: "Sozinh{o/a}? Estranho. Os outros vinham com amigos. Riam-se. Tinham medo juntos."
- *(com companheiro)* **Dragão** *(normal)*: "Trazes alguém. Bom. Os outros também traziam. Riam-se. Tinham medo juntos."
- **Dragão** *(normal)*: "Daqui para cima, o caminho fica mais curto e mais pesado. Mostra-me que aguentas o peso."
- `[Sistema] Boss: Dragão de Gelo, O Meio do Caminho.`

⚙ Luta (ver `docs/BOSSES.md`, secção 10).

## C5-08 — Metade

| | |
|---|---|
| ID | `cena_c5_08_metade` |
| Quando | vencer o Dragão de Gelo |
| Onde | andar 50, Ninho do Dragão |
| Quem | herói, Dragão de Gelo |
| Música | `vitoria` → `tundra_silencio` |

🎬 O dragão cai de lado na neve. As asas abrem-se no chão como dois lagos gelados.
- **Dragão** *(fraco)*: "Metade… Aguentas o peso. Por agora."
- **Dragão** *(normal)*: "Lá em cima… lembra-te dos amigos. Os que chegam sozinhos ao fim… ficam lá."
- 🎬 O dragão fecha os olhos. O corpo transforma-se em gelo claro e parte-se em mil cristais que o vento leva.
- `[Sistema] Boss derrotado: Dragão de Gelo.`
- `[Sistema] Obtiveste: Sopro Gélido.`
- `[Sistema] Título obtido: Matador de Dragões.`
- `[Sistema] Andar 50 de 100. Boa, Jogador. Estás a meio.`
- `[Sistema] Região 5 concluída. Andar 51 desbloqueado.`
🎬 O herói fica de pé no topo da montanha. Pela primeira vez, vê-se lá em baixo, muito pequena, a luz da escada que vem de Ascendia.

⚙ Missão **H_13** concluída. A página 50 está no ninho.

---

## C5-09 — Dia da Subida: Metade do Céu

| | |
|---|---|
| ID | `cena_c5_09_dia_subida` |
| Quando | voltar a Ascendia depois do Dragão de Gelo |
| Onde | Praça da Torre (Dia da Subida, F_05 — a **maior festa** do jogo até aqui) → fonte, à noite |
| Quem | herói, Aldric, Lucien, Gorvan, Freya, Lyra, Kai, toda a cidade |
| Música | `dia_da_subida` → `tema_kai` |

🎬 A cidade inteira na Praça. Bandeiras de todas as cores. Barracas de comida. Fogo de artifício feito pelo Gizmo (metade explode no sítio errado).
🎬 Uma estátua nova: um dragão de gelo esculpido em gelo de verdade, a derreter devagar.
- **Governador Aldric** *(no palco, emocionado)*: "Cidadãos! Metade! METADE DA TORRE! Há trezentos anos que ninguém… quer dizer, há muito tempo… Eu escrevi um discurso de seis páginas. Vou ler só… a sexta."
- 🎬 A multidão ri-se. O Aldric lê a última página: "…e por isso, obrigado." Sai do palco a chorar.
- **Lucien** *(do palco, com o alaúde)*: "Senhoras e senhores. **Metade do Céu**. Demorei três semanas. Rimei 'dragão' com 'coração' só duas vezes."
- 🎵 A canção (ver `docs/dialogos/lucien.md`, secção 7). A Praça canta o refrão: ♪ *Metade! Metade! O resto é saudade!* ♪
- 🎬 Durante a canção: o **Gorvan** está encostado a uma coluna, de braços cruzados. Quando o refrão chega, mexe a boca. Ninguém tem a certeza se está a cantar.
- 🎬 A **Freya** dá uma palmada nas costas do herói que quase o derruba. **Freya** *(feliz, raro)*: "Metade! Eu cheguei ao 62 e nunca ninguém fez uma festa assim por mim. Mereces. Hoje não treinas."
- 🎬 A **Lyra** abraça o herói de lado, rapidamente, e foge antes que ele diga alguma coisa.

### Mais tarde, à fonte
🎬 Noite. A festa ainda se ouve ao longe. O Kai está sentado na beira da fonte, com a mochila feita ao lado. Mochila grande. Corda, cantis, mapas.
- **Kai** *(normal)*: "Grande festa. Mereces. A sério."
- **Kai** *(sério)*: "Vou à frente. Amanhã de manhã. O mar, os andares 51 a 60. Sozinho."
- **Kai** *(normal)*: "Não faças essa cara. Não é por tua causa. É… há um navio no 53. Com um diário de Jogadores antigos. Se lá estiver escrito como se sai, quero ser o primeiro a ler."
- **Kai** *(triste)*: "E se não estiver, pelo menos não perdi tempo numa festa."

▶ **"Espera por mim. Vamos juntos."**
▶ **"Promete que voltas."**
▶ **"Boa sorte, Kai."**

- *(espera)* **Kai** *(triste)*: "Não posso esperar. Desculpa. Cada dia… tu sabes. A Yui." 🎬 Pausa. "Apanha-me, se conseguires. Corrida até ao 60." ⚙ +20
- *(promete)* **Kai** *(surpresa)*: "…Prometo. Volto. Com a resposta. Ou sem ela. Mas volto." ⚙ +30 · flag `kai_prometeu_voltar` (usada no capítulo 6)
- *(boa sorte)* **Kai** *(normal)*: "Sorte é para quem não treina. Mas obrigado." ⚙ +10
- 🎬 O Kai levanta-se, põe a mochila às costas e vai-se embora sem olhar para trás. Para à esquina, levanta a mão sem se virar. Desaparece.
- `[Sistema] Capítulo 6: O Oceano.` (título grande no ecrã)

⚙ Flag `kai_vai_sozinho`. O Kai continua na **fase A** até à H_14 (ver `docs/dialogos/kai.md`), mas passa os dias nos andares 51–53: na cidade só aparece à noite, cansado, e as falas dele de fase A ganham a condição extra de horário 21:00–23:00 enquanto `kai_vai_sozinho` e `missao(H_14) != concluida`.
