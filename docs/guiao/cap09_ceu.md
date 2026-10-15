# Guião — Capítulo 9: Céu (andares 81–90)

Missões: **H_21 A Verdade do Serafim** (= R9_07). Povoações e missões secundárias: `docs/dialogos/povoacoes_r09.md`.
Mapas: `docs/mapas/r09_ceu.md`.

**O que este capítulo conta**: o fim está perto e o Sistema fica cada vez mais "humano" (`[Sistema] Estás quase. Não
pares.`). No anfiteatro das ruínas celestes, fantasmas de atores representam a história do **Primeiro Jogador** (sem
dizer o nome). No Palácio Celeste, o **Serafim Caído**, que serviu o Administrador, conta a verdade: o Administrador
foi um Jogador, está **cansado** e **procura um sucessor**. É por isso que traz Jogadores. E assina com a mesma letra do
diário: **"A."**

**Flags deste capítulo**: `viu_peca` (C9-03), `sabe_sucessor` (C9-07).

---

## C9-01 — Acima das Nuvens

| | |
|---|---|
| ID | `cena_c9_01_nuvens` |
| Quando | entrar pela primeira vez no andar 81 |
| Onde | andar 81, Ilhéu de Chegada |
| Quem | herói (e o companheiro) |
| Música | `mar_de_nuvens` |

🎥 A escada de luz abre-se num ilhéu de rocha pequeno, a flutuar. À volta, um mar de nuvens brancas até ao horizonte. Um arco-íris enorme liga o ilhéu a outro, lá longe. O sol é forte e limpo.
🎬 O herói dá um passo para fora do ilhéu e cai. As nuvens apanham-no como um colchão e atiram-no de volta para a rocha.
- `[Sistema] Cair: as nuvens apanham-te, mas perdes vida.`
- `tut_nuvens`: `[Sistema] Nuvens brancas aguentam-te. As cinzentas desfazem-se 2 s depois de as pisares.`
- *(com o Kai)* **Kai** *(feliz)*: "Isto é o céu? O céu a sério? …Não. Olha lá para cima. Mais nuvens. A torre nunca deixa ver o fim."
🎬 O herói olha para cima. Por cima das nuvens, mais nuvens. Por cima dessas, um brilho dourado.

⚙ Sem missão.

---

## C9-02 — Chão É o Que Cai

| | |
|---|---|
| ID | `cena_c9_02_aeropolis` |
| Quando | entrar pela primeira vez em Aerópolis (andar 82) |
| Onde | andar 82, porto de balões → palácio |
| Quem | herói, Imperatriz Celestia, Zéfiro, Pena, Alados |
| Música | `aeropolis` |

🎬 Ilhas a flutuar presas umas às outras por correntes grossas. Casas brancas de cúpulas azuis. Balões coloridos. E gente com **asas**, a voar de ilha em ilha como quem atravessa a rua.
🎬 Uma criança alada (Pena) corre pela ponte ao lado do herói, a abanar as asas com força. Não sai do chão. Tropeça. Levanta-se. Continua a correr.
🎬 No palácio, uma mulher de asas brancas enormes está sentada num trono feito de nuvem sólida.
- **Imperatriz Celestia** *(normal)*: "Um sem asas. Que coragem. Ou que distração."
- **Imperatriz Celestia** *(normal)*: "Nós, os Alados, nascemos aqui. Nunca pisámos chão a sério. Os nossos avós diziam: 'Chão é o que cai.'"
- **Imperatriz Celestia** *(séria)*: "Os da janela passam por aqui a caminho do fim. Poucos voltam a passar. Alguns ficam em Aerópolis e aprendem a planar. São mais felizes do que os que sobem. Não digo isto para te convencer. Digo porque é verdade."
- 🎬 Um Alado velho de bigode branco (Zéfiro) aparece à porta.
- **Zéfiro** *(feliz)*: "Sem asas, mas com pernas! Pernas chegam. Vem ao campo dos aros. Ensino-te a cair devagar. É o que planar é: cair devagar e com estilo."

⚙ Desbloqueia **Aerópolis** (estalagem, cristal, forja de Oricalco, loja, porto de balões). Missões R9_01, R9_02, R9_03, R9_12, R9_13 disponíveis.

---

## C9-03 — A Peça do Primeiro

| | |
|---|---|
| ID | `cena_c9_03_peca` |
| Quando | à noite (21:00–1:00), entrar no Anfiteatro do andar 86 e sentar-se ([interagir] num degrau) |
| Onde | andar 86, Anfiteatro |
| Quem | herói, fantasmas de atores |
| Música | só uma flauta e um tambor, devagar |

🎬 O anfiteatro de pedra branca, vazio. O herói senta-se num degrau. As tochas do palco acendem-se sozinhas.
🎬 Figuras transparentes sobem ao palco: atores fantasmas, de máscaras. Um deles faz de **Narrador**. A peça tem 5 atos curtos. Ninguém diz nomes.
- **Narrador**: "A peça do Primeiro. Contada como nos contaram. Mal, mas com amor."

**Ato 1** — 🎬 um ator pequeno, de máscara de rapaz, acorda num prado de pano verde. Por cima dele, um quadrado azul de papel numa vara.
- **Narrador**: "Caiu do céu um rapaz com uma janela. Era o primeiro com número. Não havia mais ninguém."

**Ato 2** — 🎬 o rapaz sobe uma escada de cartão. Os monstros (atores com cabeças de papel) curvam-se ao quadrado azul, não a ele.
- **Narrador**: "Subiu sozinho. Os guardas da torre curvavam-se à janela. Ele não sabia porquê."

**Ato 3** — 🎬 aparece outro ator: o **Amigo**, com uma máscara de rapaz que ri. Os dois andam de mãos dadas. Depois um pano vermelho (fogo) sobe entre eles. O Amigo fica do outro lado. Quando o pano desce, o Amigo já não está.
- **Narrador**: "Encontrou um amigo no fundo do mar. Perdeu-o no fogo. A janela disse que era um inimigo. A janela mentia."

**Ato 4** — 🎬 o rapaz chega ao topo da escada. Uma figura alta e cansada põe-lhe uma coroa. O rapaz aceita.
- **Narrador**: "No topo, ofereceram-lhe a coroa. Ele aceitou. Queria descobrir como mandar toda a gente para casa."

**Ato 5** — 🎬 o rapaz, agora sozinho no topo da escada, de coroa, senta-se. Fica muito tempo parado. Depois olha para a plateia. Para o herói.
- **Narrador**: "Não descobriu. Ficou. E espera." 🎬 pausa. "Espera o próximo."
🎬 Os atores fazem uma vénia. Apagam-se, um a um. O último a desaparecer é o rapaz de coroa, que ainda está a olhar para o herói.
- `[Sistema] …`

⚙ Flag `viu_peca`. Recebe a **página de lore extra "A Peça do Primeiro"** (o texto do Narrador). Desafio do andar cumprido.
⚙ Se o herói tiver **50+ páginas** do diário, aparece uma linha no Diário: *"O rapaz da peça tem o cabelo enorme. Como o das páginas."* (só isto).

---

## C9-04 — O Telescópio Grande

| | |
|---|---|
| ID | `cena_c9_04_observatorio` |
| Quando | entrar pela primeira vez no Observatório Celeste (andar 86) |
| Onde | andar 86, cúpula do Observatório |
| Quem | herói, Astrónoma Vega, Orion |
| Música | `pontes_de_luz` (versão calma) |

🎬 Uma cúpula dourada aberta para as estrelas. Um telescópio enorme de latão no meio. Uma mulher de cabelo grisalho apanhado com dois lápis (Vega) está a olhar por ele.
- **Vega** *(sem tirar o olho do telescópio)*: "Não toques em nada. Se tocares, toca com cuidado. Se partires, paga."
- **Vega** *(normal)*: "Vens de baixo. Conheces uma velha de lenço que lê cartas? Que fala de mais e dorme de dia?"
- **Vega** *(triste, depressa)*: "Não respondas. Já sei que sim. Ela desceu há trinta anos. Por causa de uma coisa que viu aqui. Neste telescópio."
- 🎬 Vega afasta-se do telescópio e faz sinal ao herói para olhar.
🎥 Pelo telescópio: as estrelas não são pontos. São **janelinhas**. Cada uma mostra um mundo pequenino: uma floresta, um deserto, uma cidade com carros, um mar… a girar devagar.
- **Vega** *(normal)*: "Cada estrela é um mundo. Um mundo que a torre ainda não comeu. Estão todos à espera."
- **Vega** *(séria)*: "Há trinta anos, uma estrela apagou-se e, no sítio dela, apareceu um número. Dez mil. A Oriel viu-o. Eu também vi. Ela desceu para te esperar. Eu fiquei, com medo."

⚙ Desbloqueia o **Observatório Celeste** (cama, cristal, loja). Missões R9_06, R9_08 (com a Carta da Oriel), R9_10, R9_15 disponíveis.

---

## C9-05 — Vem

| | |
|---|---|
| ID | `cena_c9_05_escadaria` |
| Quando | entrar pela primeira vez no andar 89 |
| Onde | andar 89, Base da Escadaria do Sol |
| Quem | herói (e o companheiro) |
| Música | `pontes_de_luz` → silêncio |

🎥 Uma escadaria dourada gigante a subir até um sol enorme. Estátuas de anjos nos patamares. A luz é tão forte que a câmara faz "brilho".
🎬 O herói põe o pé no primeiro degrau. A janela do Sistema abre-se sozinha.
- `[Sistema] Estás quase. Não pares.`
🎬 O herói fica parado a olhar para a mensagem. Não é uma notificação. Parece… uma pessoa a falar.
- *(com o Kai)* **Kai** *(sério)*: "'Não pares.' A mim dizia 'continua'. É diferente. 'Não pares' é o que se diz a quem se quer muito que chegue."
- *(com o Gorvan)* **Gorvan** *(normal)*: "Hmm. Fala como gente. Não gosto."

⚙ A partir daqui, a mensagem `[Sistema] Estás quase. Não pares.` aparece ao vencer cada guardião (em vez de "Boa, Jogador").

---

## C9-06 — O Que Serviu o Administrador

| | |
|---|---|
| ID | `cena_c9_06_serafim_antes` |
| Quando | entrar na Varanda do Fim (andar 90) |
| Onde | andar 90, Varanda do Fim |
| Quem | herói (e o companheiro), Serafim Caído |
| Música | silêncio → `serafim_caido` |

🎬 Uma varanda aberta para o céu infinito, branca e dourada. Metade do chão está iluminada; a outra metade está numa sombra que não vem de lado nenhum.
🎬 Do céu desce uma figura enorme de seis asas: três brancas, três negras. Metade da cara é luz, metade é sombra. Na mão, uma foice de duas cores.
- **Serafim Caído** *(normal, duas vozes ao mesmo tempo)*: "Mais um com o número. O último deles, pelo número. Dez mil."
- **Serafim Caído** *(normal)*: "Servi o que está lá em cima desde antes de vocês terem números. Abri-lhe as portas. Guardei-lhe a varanda. Vi-o chorar."
- **Serafim Caído** *(zangado)*: "Ele mandou-me deixar-te passar. Eu não deixo ninguém passar sem saber se aguenta o que está do outro lado."
- `[Sistema] Boss: Serafim Caído, O Que Serviu o Administrador.`

⚙ Luta (ver `docs/BOSSES.md`, secção 19).

## C9-07 — A Verdade

| | |
|---|---|
| ID | `cena_c9_07_verdade` |
| Quando | vencer o Serafim Caído |
| Onde | andar 90, Varanda do Fim |
| Quem | herói (e o companheiro), Serafim Caído |
| Música | `vitoria` (só os primeiros acordes) → vento → `tema_principal` (piano, muito lento) |

🎬 O Serafim cai de joelhos na linha entre a luz e a sombra. As asas negras desfazem-se em penas. Ficam as brancas.
- **Serafim** *(normal, já só uma voz)*: "Aguentas. Bom. Então ouve. Alguém tem de te dizer, antes de lá chegares."
- **Serafim** *(normal)*: "O que está lá em cima. O Administrador. Já foi como tu. Caiu do céu com uma janela. Subiu sozinho."
- **Serafim** *(triste)*: "Perdeu um amigo no fogo. Chegou ao topo. Aceitou a coroa para descobrir como mandar toda a gente para casa."
- **Serafim** *(triste)*: "Não descobriu. Quem governa a torre não pode sair. E quem não governa não pode mandar ninguém embora."
- **Serafim** *(normal)*: "Está cansado. Mil anos de cansaço. É por isso que vos traz. Os números, as janelas, os 'continua'. Está à procura de alguém que fique no lugar dele."
- **Serafim** *(normal)*: "Um sucessor. Para ele poder, finalmente, descansar."

▶ **"E se eu não quiser ficar?"**
▶ **"Quem é ele?"**
▶ *(ficar calad{o/a})*

- *(não quiser)* **Serafim** *(normal)*: "Um recusou, há trezentos anos. A torre raspou-lhe o nome. Ainda anda lá em baixo, no abismo, à procura de quem o ouça."
- *(quem é)* **Serafim** *(normal)*: "Perdeu o nome há muito tempo. Já nem o diz. Assina com uma letra só." 🎬 olha para o bolso do herói, onde estão as páginas. "A mesma das páginas que trazes contigo."
- *(calado)* **Serafim** *(normal)*: "Fazes bem. Há coisas que se ouvem melhor caladas."
- **Serafim** *(normal)*: "Quando chegares, ele vai oferecer-te o lugar. Vai pedir-te com muito cuidado. Vai parecer a coisa certa."
- **Serafim** *(feliz, pela primeira vez)*: "Pensa bem. E depois faz o que quiseres. É a única coisa que nenhum de vocês pôde fazer até agora."
- 🎬 O Serafim desfaz-se em penas brancas que o vento leva para cima, para a luz dourada.
- `[Sistema] Boss derrotado: Serafim Caído.`
- `[Sistema] Obtiveste: Foice do Serafim.`
- `[Sistema] Título obtido: Além do Céu.`
- `[Sistema] Região 9 concluída. Andar 91 desbloqueado.`
- `[Sistema] …`
- `[Sistema] Desculpa.` 🎬 *(aparece e desaparece em meio segundo)*

**Falas do companheiro** (se houver):
- *(Kai)* **Kai** *(zangado, depois triste)*: "Então o acordo… o 'quem chegar primeiro vai para casa'… era isto? Chegar primeiro para ficar no lugar dele? Para ficar PRESO?" 🎬 dá um pontapé numa pena. "Eu ia aceitar. Eu ia aceitar e nem sabia."
- *(Gorvan)* **Gorvan** *(normal)*: "Hmm." 🎬 pausa comprida. "Um rapaz sozinho, mil anos, num sítio alto. Conheço o género." 🎬 olha para o herói. "Não fiques. Ouviste? Não fiques."

⚙ Missão **H_21** concluída. Flag `sabe_sucessor`. A página 90 (**tinta azul**) aparece na varanda, presa entre duas penas brancas.

---

## C9-08 — Dia da Subida: O Dia Calado

| | |
|---|---|
| ID | `cena_c9_08_dia_subida` |
| Quando | voltar a Ascendia depois do Serafim |
| Onde | Praça da Torre (Dia da Subida, o mais silencioso) → Biblioteca → Estalagem |
| Quem | herói, Aldric, Lucien, Lyra, Gorvan, Fausto, Dona Marta, Mia, (Kai se `kai_salvo`) |
| Música | `dia_da_subida` (só piano) |

🎬 A Praça tem bandeiras, mas ninguém dança. As notícias correram: o Fausto contou ao Lucien, o Lucien contou à cidade. Lá em cima há um rei cansado à procura de quem fique no lugar dele.
🎬 A estátua nova é uma pena branca de pedra, sem mais nada.
- **Governador Aldric** *(no palco, sem papel)*: "Cidadãos. Hoje não li o discurso. Não sei o que dizer." 🎬 pausa. "Noventa andares. Faltam dez. E temos medo de que, quando lá chegar, não volte."
- **Governador Aldric** *(normal)*: "Por isso hoje não é uma festa. É um… obrigado. E um 'volta'. Só isso."
- 🎬 Ninguém aplaude. Depois a Mia grita, lá do fundo: "VOLTA!" e a Praça inteira repete.
- **Lucien** *(do palco, a afinar o alaúde e a desistir)*: "Hoje não há canção nova. Há uma velha. A primeira que escrevi quando chegaste." 🎵 *(o tema do prólogo, devagar, em alaúde)*

### Na Biblioteca
- **Fausto** *(normal, sem levantar os olhos dos livros)*: "A roda. Os hieróglifos tinham razão. Um sobe, recebe a coroa, cansa-se, chama outro."
- **Fausto** *(triste)*: "Passei a vida a querer saber tudo. Hoje queria não saber isto."
- **Fausto** *(normal)*: "Leva as páginas que tens. Todas. Lá em cima, alguém as vai querer ler contigo. Tenho a certeza."

### Na Estalagem, à noite
- 🎬 A Dona Marta põe dois pratos de guisado na mesa. Senta-se à frente do herói. Não come.
- **Dona Marta** *(normal)*: "O meu Tomás foi e não voltou. Tu vais e voltas. Já decidi. Não discutas com uma velha."
- *(se `kai_salvo`)* 🎬 O Kai entra, senta-se ao lado, rouba uma batata do prato do herói.
  - **Kai** *(sério)*: "Prometemos chegar os dois. Vamos chegar os dois. E depois vamos descer os dois. Se ele te oferecer o lugar, dizes que não. Se ele insistir, eu digo que não por ti. Bem alto."

⚙ `[Sistema] Capítulo 10: O Abismo.` (título grande no ecrã)
