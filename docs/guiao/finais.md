# Guião — A Escolha Final, os 4 Finais e os Epílogos

Vem depois da cena **C10-16** (`docs/guiao/cap10_abismo.md`). Regras dos finais: `docs/HISTORIA.md`, secção 6.
A luta: `docs/BOSSES.md`, secção 21.

| Final | Como se chega | Secção |
|---|---|---|
| 1 · **Voltar a Casa** | vencer o Aren e escolher **partir** | 2 |
| 2 · **O Novo Administrador** | aceitar a oferta **antes** da luta (C10-15) ou **depois** de vencer | 3 |
| 3 · **Libertar os Mundos** | vencer o Aren e escolher **partir o núcleo** | 4 |
| 4 · **A Ponte** (secreto) | as 5 condições + "Há outra maneira" na C10-15 | 5 |

**As 5 condições do final secreto**: `kai_salvo` · `sssar_defendida` · 8+ NPCs de Ascendia com 10 ❤️ ·
`perdidos_convencidos == 5` · `sabe_nome_aren` (90+ páginas). O contador `condicoes_final_secreto` (0–5) é usado pelo
Doutor (`doutor_finais_4`) e pelo menu "Diário → Pistas" depois do jogo (diz quantas faltaram, não quais).

**Quem aparece no fim** (em todas as cenas desta página, quando a cena diz "os teus"):
- os **companheiros** da equipa;
- o **Kai** (salvo: acordado; vencido: dentro da janela, a dormir, até à escolha);
- os **Perdidos convencidos** (0 a 5), que subiram atrás do herói e esperam no Ponto Sem Retorno;
- o **Ssark** se `ssark_97_sobe` (expulsos) ou se é companheiro (defendidos);
- a **Nina**, se R10_08 está feita.

---

## 1. A Escolha

| | |
|---|---|
| ID | `cena_fim_01_escolha` |
| Quando | depois da fase 4 do Administrador (não acontece no final 4) |
| Onde | andar 100, Jardim do Topo (volta a aparecer quando a janela "Desistir?" se parte) |
| Quem | herói, Aren, e os teus |
| Música | vento na erva → `casa` (piano) |

🎬 Aren está deitado de costas na erva, a olhar para o céu de fim de tarde. Já não tem olhos azuis: são castanhos. Respira devagar, como quem acabou de correr muito.
🎬 Os companheiros e os Perdidos convencidos entram pela porta pequena e ficam ao longe, calados.
- **Aren** *(normal, sem se levantar)*: "Então é isto, perder. Esqueci-me de como era. Não é tão mau."
- **Aren** *(normal)*: "Agora é a regra da torre, não a minha. Quem vence quem está no trono escolhe. Há três portas. Não te vou dizer qual é a certa. Não sei."
🎬 Aren levanta a mão. No ar aparecem **três janelas azuis**, lado a lado, cada uma com uma imagem pequenina a mexer.
🎥 Janela 1: um quarto com a chuva a bater na janela e um despertador. Janela 2: o trono simples de pedra, vazio. Janela 3: uma esfera azul que pulsa, como um coração.
- **Aren** *(normal)*: "A primeira abre uma porta para o teu mundo. Só para ti. Voltas a casa como se tivesses adormecido no autocarro."
- **Aren** *(normal)*: "A segunda é o trono. Ficas com ele. Mudas o que quiseres. Nunca sais."
- **Aren** *(triste)*: "A terceira é o núcleo. Partes o coração da torre. Os mundos voltam para onde estavam. Não sei o que acontece a mim. Nem a ti. Ninguém nunca a escolheu."
- *(com `flag(doutor_convencido)`)* 🎬 O Doutor, ao fundo, sussurra: "As três portas. Eu tinha razão. Eu tinha razão!" e depois fica muito envergonhado.

▶ **Partir** *(janela 1)* → secção 2
▶ **Ficar** *(janela 2)* → secção 3 (versão B)
▶ **Partir o núcleo** *(janela 3)* → secção 4

🎬 Antes de confirmar, aparece `[Sistema] Tens a certeza? Sim / Não` — **sem falhas**. Desta vez "Não" funciona e volta às três janelas. Pode-se pensar o tempo que se quiser. Aren espera, a arrancar ervas.

---

## 2. Final 1 — "Voltar a Casa"

### F1-01 — As despedidas

| | |
|---|---|
| ID | `cena_f1_01_despedidas` |
| Onde | andar 100, Jardim do Topo |
| Música | `casa` |

🎬 Aren levanta-se. Toca no ar e abre uma **porta azul**, de madeira, igual à porta do quarto do herói. Por baixo dela sai luz de fim de tarde e cheiro a chuva.
- **Aren** *(normal)*: "Vai. Mas despede-te. Eu não me despedi de ninguém. Arrependo-me todos os dias."
🎬 O herói vai de um em um.
- *(Kai, `kai_salvo`)* **Kai** *(a tentar sorrir)*: "Vais primeiro. Estava escrito. O 9 999 chega sempre a seguir." 🎬 Aren toca-lhe no ombro. **Aren**: "Abro-te uma segunda porta. Gasto o que me resta. A tua irmã está à tua espera." **Kai** *(sem palavras, depois)*: "…Obrigado. Velho." 🎬 o Kai abraça o herói com força. "Vemo-nos do outro lado. Eu encontro-te. Sou muito bom a encontrar pessoas."
- *(Kai, `kai_vencido`)* 🎬 Aren abre a janela onde o Kai dorme. **Aren**: "Mando-o para casa. Mas não leva memórias da torre. É mais simples, assim. Para ele." 🎬 O Kai, a dormir, sorri, e desaparece em luz. O herói fica a olhar para o sítio vazio.
- *(Gorvan)* **Gorvan** *(normal)*: "Hmm." 🎬 pausa comprida. "Vai. Não olhes para trás. Quem olha para trás fica." 🎬 vira-se ele primeiro.
- *(Mia, companheira)* **Mia** *(a chorar e zangada)*: "Prometeste que me levavas ao rank A! Ainda sou B!" 🎬 abraça-se à perna do herói. "Vai. Mas não me esqueças."
- *(Ssark)* **Ssark**: "Ssss. Boa caça, da janela. No teu mundo, não haja guildas."
- *(Inga)* **Inga** *(normal)*: "No meu mundo, quem parte leva uma pena de coruja. Toma. Não perguntes porquê."
- *(Nina)* **Nina** *(baixinho)*: "No teu mundo há neve?" ▶ *"Há."* **Nina**: "Então vê-a por mim."
- *(Perdidos)* 🎬 Os Perdidos convencidos acenam. A Bia chora. O Ulisses tira o chapéu. Os gémeos dão as mãos.
- **Aren** *(no fim)*: "E eu fico. Não te preocupes. Ganhaste, mas não te sentaste. Por isso eu continuo." 🎬 sorri. "Mas não trago mais ninguém. Prometo. Vou esperar sozinho, como devia ter feito desde o princípio. Ou… vou descer à Cidade dos Perdidos. Dizem que lá há uma senhora que tricota cachecóis."

▶ **Abraçar o Aren**
▶ **"Obrigad{o/a}."**
▶ *(acenar e ir)*

- *(abraçar)* 🎬 Aren fica rígido. Depois abraça de volta, desajeitado, como quem não abraça há mil anos. "Isto. Também me tinha esquecido disto."
- *(obrigado)* **Aren**: "Não. Obrigado eu. Leste até ao fim."
- *(acenar)* **Aren** *(a acenar também)*: "Assim é que é. Sem fazer cerimónias."
🎬 O herói passa a porta azul. A luz enche o ecrã.

### F1-02 — O Despertador

| | |
|---|---|
| ID | `cena_f1_02_quarto` |
| Onde | o quarto do herói, no mundo real |
| Música | silêncio → chuva → o despertador |

🎥 Escuro. Um som: **o despertador**. 7:00.
🎬 O herói abre os olhos. É o quarto dele: a cama por fazer, a secretária com os cadernos, o carregador pendurado da tomada. O mesmo quarto da casa sem número, mas agora com o cheiro certo, a luz certa e uma voz lá em baixo a chamar para o pequeno-almoço.
🎬 O herói senta-se na cama. Olha para as mãos. Não há janela azul.
🎬 O telemóvel vibra na mesinha. Uma mensagem de um número desconhecido:
- 📱 *"Obrigado. — A."*
🎬 O herói fica a olhar para a mensagem. Depois sorri.
- *(se `kai_salvo`)* 🎬 O telemóvel vibra outra vez. Uma fotografia: uma menina pequenina (a Yui) a segurar um desenho de uma espada enorme, e ao lado, a fazer uma careta para a câmara, o Kai. Por baixo: *"Encontrei-te. Disse que era bom nisto. Sábado?"*
🎬 Lá em baixo, a voz chama outra vez. O herói levanta-se e abre a janela do quarto. Chove numa rua normal. Ao fundo, nas nuvens, por um segundo, parece haver uma torre. Não há.
🎬 Fim. Créditos (secção 6).

> **Depois**: ao carregar o jogo, o herói está de volta à torre "num sonho" (o Sistema diz `[Sistema] Bem-vind{o/a} de volta. Isto é um sonho. Aproveita.`) para o pós-jogo, com tudo como estava.

---

## 3. Final 2 — "O Novo Administrador"

### Versão A — aceitar logo (C10-15, "Sim")

| | |
|---|---|
| ID | `cena_f2_a_aceitar` |
| Onde | andar 100, Jardim do Topo → Sala do Sistema |
| Música | `casa` → `administrador` (só cordas, devagar) |

🎬 O herói carrega em "Sim" antes de lutar. Aren fica muito quieto.
- **Aren** *(surpreendido)*: "Assim? Sem lutar?" 🎬 os olhos azuis enchem-se de lágrimas. "Eu também disse que sim depressa. Pensei que era o mais corajoso. Era só o mais cansado."
- **Aren** *(normal)*: "Tens a certeza? Não precisas de responder. Já carregaste no botão. A torre não tem 'voltar atrás'. Foi a primeira coisa que me ensinou."
- *(Kai, `kai_salvo`, se presente)* **Kai** *(a gritar)*: "NÃO! Disseste que dizias que não! Prometemos descer os dois!" 🎬 o herói olha para ele. O Kai para. "…Fazes isto para eu poder ir para casa. Não fazes?" 🎬 pausa. "És estúpid{o/a}. És {o/a} mais estúpid{o/a} que eu conheço." 🎬 abraça o herói. "Obrigado."
→ segue para **"A Coroa"** (abaixo).

### Versão B — escolher ficar depois de vencer (secção 1, "Ficar")

| | |
|---|---|
| ID | `cena_f2_b_ficar` |
| Onde | andar 100, Jardim do Topo → Sala do Sistema |

- **Aren** *(triste)*: "Venceste-me e escolhes o trono. Porquê?"

▶ **"Para ninguém mais ser trazido à força."**
▶ **"Para tu poderes descansar."**
▶ **"Porque alguém tem de ficar."**

- *(à força)* **Aren**: "Era o que eu queria fazer e nunca fiz. Vais fazer melhor. Já fazes."
- *(descansar)* **Aren** *(a chorar sem esconder)*: "Ninguém nunca escolheu nada por mim. Em mil anos."
- *(alguém)* **Aren**: "Não tem. Mas obrigado por pensares que sim."
→ segue para **"A Coroa"**.

### A Coroa

🎬 Aren leva o herói pela mão até ao trono simples de pedra, na Sala do Sistema. As janelas azuis começam a rodar devagar à volta deles, como pássaros.
- **Aren** *(normal)*: "Senta-te. Vai doer um bocadinho na cabeça. Depois vês tudo. A torre inteira. Cada andar, cada pessoa. É bonito e é demasiado. Habituas-te."
🎬 O herói senta-se. As janelas param. Todas se viram para ele. Os olhos do herói ficam **azuis**.
- `[Sistema] Novo Administrador: {nome}.`
- `[Sistema] Primeira regra. Escreve.`
🎬 Uma janela aparece à frente do herói, com um cursor a piscar. O jogador **não escreve**: o herói escreve sozinho, letra a letra:
- `[Sistema] Já não serão trazidos Jogadores à força.`
- *(se `kai_vencido`)* `[Sistema] O Jogador nº 9 999 vai para casa. Com as memórias.` 🎬 a janela onde o Kai dorme abre-se. Ele acorda, olha para o herói com os olhos azuis, e percebe. "…Não. Não, não, não. Tu não." Desaparece em luz antes de acabar a frase.
🎬 Aren vê a regra escrita. Sorri. O cabelo branco começa a ficar castanho, e depois **luz**.
- **Aren** *(feliz, pela primeira vez sem tristeza nenhuma)*: "Finalmente. Obrigado, {nome}. Desculpa. Obrigado."
- **Aren** *(a desaparecer)*: "Se encontrares o Nereu… não. Não procures. Deixa-o estar onde estiver. Se ele estiver bem, chega."
🎬 Aren desfaz-se em luz que sobe pela torre, andar a andar, e sai pelo topo. Fica o caderno dele na erva.
- `[Sistema] …` *(desta vez é o herói a escrever: o jogador vê o cursor parar)*

### F2-02 — A Estátua no Topo

🎥 Ascendia, uma semana depois. Na Praça da Torre, uma estátua nova: **o herói**, de pé no topo de uma torre pequena de pedra, a olhar para cima.
- **Governador Aldric** *(a ler um papel, a gaguejar)*: "Cidadãos… hoje… hoje inauguramos… Não. Não consigo." 🎬 dobra o papel. "Subiu. Ficou. Para que os outros pudessem ficar ou ir. Mais nada."
🎬 A Dona Marta põe um prato de guisado aos pés da estátua. Todos os dias, até ao fim da vida.
🎬 Lá em cima, no topo, o herói está sentado no trono. Uma janela pequenina mostra a Praça. Ele toca na janela. A Mia, lá em baixo, sente uma brisa quente na cara e olha para cima.
🎬 Fim. Créditos (secção 6).

> **Depois**: pós-jogo como **Administrador**: no Topo, a Sala do Sistema deixa **mudar regras** (clima de cada região, a música, a dificuldade, os monstros de cada andar, as estações). O herói anda pela torre como sempre, mas **não pode descer abaixo do andar 1** (Ascendia só se vê pelas janelas; os NPCs vêm visitar ao andar 1, ao Prado). Ver `docs/ATIVIDADES.md`.

---

## 4. Final 3 — "Libertar os Mundos"

### F3-01 — O Núcleo

| | |
|---|---|
| ID | `cena_f3_01_nucleo` |
| Onde | andar 100, Sala do Sistema → o núcleo (por baixo do trono) |
| Música | `administrador` (só o baixo, a bater como um coração) → silêncio |

🎬 Aren abre o chão por baixo do trono. Lá dentro, uma **esfera azul** do tamanho de uma casa, a pulsar.
- **Aren** *(normal)*: "Nunca lhe toquei. Tive medo de ser a única coisa que me segurava cá."
- **Aren** *(normal)*: "Se a partires, a torre deixa de comer. Os andares voltam para os mundos de onde vieram. Os que vivem lá dentro vão com eles. Para casa."
- **Aren** *(triste)*: "E os Jogadores… os vossos mundos nunca foram comidos. Não há andar que volte para lá. Ficam onde estiverem quando a torre acabar."
- **Aren** *(normal)*: "Ou seja: libertas toda a gente menos tu."

▶ **Partir o núcleo**
▶ **Voltar atrás** *(volta à escolha, secção 1)*

🎬 O herói levanta a arma. O núcleo bate mais depressa, como um coração com medo. Um golpe. Uma racha. Dois. Três.
- *(com o Kai, `kai_salvo`)* 🎬 o Kai põe a mão por cima da do herói no último golpe. "Juntos. Lembras-te?"
🎬 O núcleo parte-se. Silêncio. Depois, um som enorme, como um sino do tamanho do céu.

### F3-02 — A Torre Desfaz-se

🎥 A torre vista de fora, de Ascendia. Uma racha de luz desce do topo até à base.
🎥 Andar a andar, a torre **desfaz-se em luzes** que sobem ao céu, cada uma de uma cor: verde (a Floresta), azul-escuro (as Cavernas), dourada (o Deserto)…
🎬 Em cada andar, os povos despedem-se, a subir na luz:
- Em **Folhalta**, a Anciã Lothiel ergue o bastão. O **Eldrin** acena para baixo, para Ascendia, para a irmã. Na loja de alquimia, a **Selene** larga um frasco e corre para a rua, a chorar e a rir.
- Em **Mycélia**, os fungoides dançam.
- Na aldeia **Sssar** (se `sssar_defendida`), a aldeia inteira sobe, a cantar. O Ssark fica para trás um segundo, a acenar ao herói, e depois sobe também.
- Em **Coralina**, a Rainha e o Príncipe Maré sobem numa bolha de mar. O Maré grita: "VOU VER O CÉU!"
- Na Forja de Obsidiana, o **tio Ragnar** bate três vezes na bigorna, como despedida. Em Ascendia, o **Brom** ouve e bate três vezes na dele.
- Em **Aerópolis**, os Alados voam na própria luz, a fazer acrobacias. A Pena à frente de todos.
- E num andar que ninguém sabia qual era, um reino pequeno de tecelões, com um estandarte de sol a nascer, sobe também. Em Ascendia, a **Elva** vê-o passar no céu e deixa cair a tesoura: "Alvorada."
🎬 No topo, Aren está ao lado do herói, a ver tudo. Uma luz azul-mar, a de Coralina, passa ao lado deles.
- **Aren** *(baixinho)*: "O mar. O mundo do Nereu." 🎬 olha para o herói. "Posso?"

▶ **"Vai."**
▶ *(acenar)*

- **Aren** *(a sorrir como um rapaz)*: "Talvez ele esteja lá. Talvez não. Vou ver. Tenho tempo." 🎬 Aren entra na luz azul-mar e sobe com ela. O cabelo dele, a subir, já não é branco.

### F3-03 — Ascendia ao Sol

🎥 De manhã. **Não há torre.** No sítio dela, uma planície de erva enorme, com flores do andar 1 e uma colina pequena.
🎬 Ascendia está no meio de um mundo novo, verde e vazio, ao sol. O céu é o primeiro céu verdadeiro que a cidade tem.
🎬 O herói está na Praça, onde estava a escada da torre. À volta, os teus.
- **Fausto** *(a olhar para cima)*: "Um céu. Sem nada por cima. Tenho de começar um livro novo. Tenho de começar uma vida nova. Tenho oitenta anos. Que maravilha."
- *(Kai, `kai_salvo`)* **Kai** *(sentado no chão)*: "Não há luz para o meu mundo. Pois não?" 🎬 pausa. "Está bem. A Yui tem a minha mãe. E eu tenho… isto. Vou construir uma casa. E vou escrever-lhe cartas. Um dia alguém inventa um correio entre mundos. Vais ver."
- *(Kai, `kai_vencido`)* 🎬 o Kai acorda deitado na erva, no sítio da torre, sem saber como ali chegou. Olha para o herói. Não diz nada. Depois estende a mão para o herói o ajudar a levantar-se.
- **Governador Aldric**: "Bem. Bem, bem, bem. Uma cidade sem torre. Vamos precisar de… de… de tudo. De um nome novo, para começar."
- **Mia** *(a correr pela planície)*: "Posso ser aventureira na mesma? Há sítios novos? Há monstros novos? Há?"
🎬 A câmara sobe. Ascendia, pequenina, no meio de um mundo enorme por explorar.
🎬 Fim. Créditos (secção 6).

> **Depois**: pós-jogo na **"torre-memória"** (os **Andares do Eco**): no sítio da torre há uma pedra com uma janela azul pequenina. Tocar-lhe abre um sonho com a torre como era, para quem quiser continuar a subir.

---

## 5. Final 4 (secreto) — "A Ponte"

### F4-01 — Lutar ao Contrário

| | |
|---|---|
| ID | `cena_f4_01_segurar` |
| Quando | fase 3 do Administrador, depois de "Há outra maneira" (C10-15): as janelas dos amigos **seguram** o Aren em vez de o atacar |
| Onde | andar 100, O Trono do Administrador |
| Música | `administrador` com coro → o coro canta sozinho o tema de Ascendia |

🎬 A figura de janelas azuis treme. As janelas dos amigos (todos os NPCs com 10 ❤️, os companheiros, os Perdidos, a Mãe Dois a tricotar, o Desistente) não disparam. **Agarram** nas janelas do Aren, uma a uma, como quem segura a mão de alguém.
- **Aren** *(a voz de muitas janelas, confusa)*: "Porquê? Porque é que não me atacam?"
- **Dona Marta** *(da janela dela)*: "Porque estás cansado, filho. Os cansados não se batem. Põe-se-lhes um prato à frente."
- **Gorvan**: "Pousa isso. Pousa o peso. Também me custou."
- **Kai**: "Eu sei o que é aceitar um acordo mau por saudades. Larga."
- **"Mãe Dois"**: "Meu menino. Mil anos. Anda cá."
🎬 A figura encolhe. As janelas desprendem-se dele uma a uma e ficam a flutuar, livres. No meio, fica o Aren, de joelhos, de cabelo branco, a chorar.
- **Aren**: "Não sei como se desliga isto. Se eu largar, a torre fica sem ninguém."
🎬 O herói estende a mão. As janelas soltas vêm todas para ele. **Mas o herói não se senta.** Fica de pé, com o poder do Sistema nas mãos, e olha para o Aren.
- `[Sistema] Administrador: ????. O que queres fazer?`

▶ **Ligar os mundos** *(é a única opção; aparece escrita à mão, na letra do herói)*

### F4-02 — A Ponte

🎬 O herói junta as janelas como quem faz uma corda. A corda de luz sai pelo topo da torre.
🎥 De fora: do topo da torre sai **uma ponte de luz** que se divide em muitas, como os ramos de uma árvore. Cada ramo vai até uma estrela. Cada estrela é um mundo.
🎥 Os mundos engolidos aparecem nas pontas dos ramos: a floresta dos elfos, o mar de Coralina, um reino de tecelões, um céu cheio de dragões… **e um planeta azul**, aquele do andar 92 — e outro, muito parecido, que **é** o do herói.
- `[Sistema] Regra nova: quem quiser, pode ir. Quem quiser, pode voltar.`
- `[Sistema] Os andares ficam. As portas ficam abertas.`
🎬 O Aren olha para a ponte. Levanta-se devagar. O cabelo continua branco. Os olhos ficam castanhos.
- **Aren** *(baixinho)*: "Eu nunca pensei nisto. Mil anos e nunca pensei. Ou entrava ou saía. Nunca pensei em abrir."
- **Aren** *(a rir e a chorar)*: "Que parvo. Que parvo que eu fui."
🎬 O herói senta-se na erva do Jardim, ao lado dele. Sem trono. Os dois a olhar para a ponte.
- `[Sistema] Administrador: ninguém. Guardiões da Ponte: {nome} e Aren.`

### F4-03 — Quem Vem

🎬 Na ponte que vai dar ao mar de Coralina, uma figura a andar na direção da torre. Um rapaz. Cabelo escuro e molhado, a pingar. Pára a meio da ponte. Acena.
🎬 O Aren levanta-se de repente. Dá um passo. Mais um. Para.
- **Aren** *(sem voz)*: "…"
🎥 A câmara não se aproxima. Não se vê a cara do rapaz. O Aren começa a correr pela ponte.
🎬 (O jogo nunca diz quem é.)

### F4-04 — A Festa Final

| | |
|---|---|
| ID | `cena_f4_04_festa` |
| Onde | Ascendia, Praça da Torre, um mês depois |
| Música | `dia_da_subida` com todos os instrumentos de todas as regiões |

🎬 A maior festa que Ascendia já teve. Na Praça, a escada da torre tem agora uma **ponte de luz** a sair do topo, visível de toda a cidade, como um arco-íris de noite.
🎬 Gente de todos os andares na Praça: elfos de Folhalta, fungoides, os Ssar, Torrenses de Zahra, caçadores do Gelo, sereias numa fonte gigante, anões, fantasmas do Mercado (de dia, pela primeira vez), Alados a voar por cima das bandeiras, os Perdidos todos (não só os cinco), a Arquivista com um livro debaixo do braço.
- **Kai**, de mão dada com uma menina pequenina de mochila às costas: **Yui**. **Kai** *(feliz)*: "Ela atravessou a ponte sozinha. Sozinha! Tem nove anos!" **Yui** *(a olhar para o herói)*: "Tu é que és {o/a} 10 000? O meu irmão fala de ti o tempo todo. É chato."
- **Gorvan**, de braço de ferro com cinco nomes gravados, a dançar (mal) com a Freya.
- **Selene** e **Eldrin**, juntos, a ver o céu verdadeiro do mundo dos elfos pela ponte.
- **Elva**, com um vestido com o ponto de alvorada, ao lado de uma rainha jovem: **Isolda**.
- **Hana**, a plantar a "semente do mundo" da mãe no meio da Praça. Cresce uma árvore de trigo dourado.
- **Zed**, a olhar para a ponte que vai dar a um mundo de lobos cinzentos com riscas azuis. O Pimpão no ombro. Não diz nada. Sorri.
- **"Mãe Dois"**, sentada numa cadeira de baloiço no meio da Praça, a tricotar. O cachecol já dá a volta à Praça inteira.
- **Rafa**, no palco, com o Lucien: tocam a "Casa" a duas guitarras e um alaúde.
- **Aren**, sentado nos degraus da Taberna, de cabelo branco, com um rapaz de cabelo escuro ao lado a rir-se de qualquer coisa. Os dois a comer guisado da Dona Marta.
🎬 O herói está no meio da Praça. Toda a gente olha para ele. A Mia sobe a uma cadeira e grita: "DISCURSO!"
🎬 O herói é silencioso. Não diz nada. Sorri.
🎬 A Praça inteira ri-se. A festa continua.
🎬 Fim. Créditos (secção 6).

> **Depois**: pós-jogo com **viagens entre mundos**: a **Ponte para as Estrelas** em Ascendia (pela ponte de luz) leva ao **quarto do herói** (uma pequena área do mundo real: o quarto, a rua, a paragem de autocarro) e aos mundos engolidos (visitas curtas). Os Andares do Eco também abrem.

---

## 6. Créditos e epílogos

Os créditos passam por cima de **imagens** (uma por NPC, desenhadas como as páginas do diário: papel e lápis de cor).
Cada imagem tem **uma frase**. A versão depende do **final** e da **amizade** (**muita** = 8+ ❤️; **pouca** = menos).
Os finais 1 e 3 usam as colunas "muita"/"pouca"; o 2 e o 4 trocam algumas (coluna "No final 2 / 4").

### 6.1 Os 20 de Ascendia

| NPC | Muita amizade | Pouca amizade | No final 2 / 4 |
|---|---|---|---|
| **Kai** | (salvo) volta para a irmã; visita a torre aos fins de semana (final 4) ou escreve-te todas as semanas (final 1) | (vencido) o Sistema leva-o para casa sem memórias. Às vezes sonha com uma torre e acorda a chorar sem saber porquê | **2**: em casa, desenha todos os dias uma pessoa sentada num trono, para não se esquecer da cara |
| **Gorvan** | volta a liderar expedições, com os nomes da equipa gravados no braço de ferro | continua na Guilda, sozinho, a olhar para a torre da muralha | **4**: leva expedições pela ponte; "Os Imortais II", diz a bandeira |
| **Brom** | forja a "Décima Milésima" ao lado do tio Ragnar; ensina um aprendiz anão | continua a resmungar na forja, mas pendura a tua primeira espada na parede | **3**: o Ragnar sobe na luz; o Brom fica com a bigorna dele |
| **Mia** | rank B aos 14 anos; ensina outras crianças a usar o arco | continua a vender flores, mas a sonhar com mapas | **2**: deixa uma flor por dia aos pés da tua estátua |
| **Lyra** | escreve um livro com as tuas aventuras: *Registo de Missão: Tudo* | continua na Guilda, a carimbar | **3**: vai procurar o sítio onde o pai ficou (o andar 31 voltou para um deserto qualquer). Encontra uma lápide com o nome dele |
| **Dona Marta** | põe a tua fotografia ao lado da do Tomás, por cima do balcão | cozinha para o próximo Jogador | **2**: leva-te um prato de guisado todos os dias, ao andar 1 |
| **Rook** | (ajudado) abre um orfanato no Bairro Baixo; com `samira_sabe`, visita Zahra todos os anos, e a Samira passa os invernos em Ascendia | (fugiu) vive na Cidade Errante, a roubar aos ricos de outros andares | **3**: com `samira_sabe`, sobe na luz do deserto com a mãe, e despede-se dos miúdos do orfanato |
| **Velho Fausto** | publica *A Crónica da Subida*; o primeiro exemplar fica na tua casa | morre feliz numa cadeira da biblioteca, com um livro aberto | **4**: a Arquivista e ele trocam livros todas as semanas pela ponte. Discutem por carta |
| **Selene** | vê um céu verdadeiro, com o Eldrin | continua a fazer poções e a olhar pela janela | **3**: sobe na luz de Folhalta; deixa a loja à aprendiz |
| **Tobias** | ele e o Tibério juntam as lojas: "Tobias & Tibério, de Baixo a Cima" | continua a discutir com o irmão por cartas | **4**: abre uma filial do outro lado da ponte |
| **Irmã Célia** | a Abadessa Lumina desce a Ascendia e as duas fazem chá todas as semanas | reza pela torre, sozinha, à noite | **3**: o mosteiro sobe na luz; a Lumina fica em Ascendia com ela |
| **Capitã Freya** | reforma-se e treina a nova guarda; com R9_11 feita, recebe cartas da Sigrun | continua a patrulhar a muralha, sem monstros para caçar | **4**: atravessa a ponte para o céu das valquírias; volta todos os invernos |
| **Pip** | pesca finalmente a baleia (desta vez há testemunhas) | continua a contar a história da baleia; ninguém acredita | **3**: os rios da torre desaparecem; ele descobre um rio novo, na planície |
| **Hana** | a "semente do mundo" da mãe dá uma árvore de trigo dourado no meio da quinta | alimenta a cidade, sozinha, sem tempo para mais nada | **4**: visita o mundo dos campos de trigo pela ponte. Volta com os bolsos cheios de sementes |
| **Zed** | encontra uma alcateia de lobos cinzentos com riscas azuis; não diz nada; o Pimpão chora por ele | continua no rancho, a falar com os animais | **4**: atravessa a ponte e fica uma semana com os lobos. Volta com um nome |
| **Madame Oriel** | volta ao Observatório e faz as pazes com a Vega; olham as estrelas juntas | continua a ler cartas, e acerta mais do que diz | **2**: sabe sempre onde estás. Põe uma carta virada para cima à porta da tenda todas as manhãs: a Estrela |
| **Lucien** | escreve a canção do teu nome, que toda a cidade sabe de cor | continua a tocar na Taberna as mesmas canções | **4**: toca a "Casa" com o Rafa todos os sábados |
| **Gizmo** | faz uma máquina que fala com o Senhor Vapor por cima dos andares (com o final 4, atravessa a ponte e encontra o mundo das máquinas) | continua a inventar coisas que explodem | **3**: o primo sobe na luz; o Gizmo fica a construir um balão |
| **Elva** | encontra Alvorada (finais 3 e 4: o reino reaparece; ela abraça a rainha Isolda) | faz vestidos com um bocadinho de Alvorada em cada um | **2**: tu encontras Alvorada nas janelas e mandas-lhe o caminho; ela chora uma semana inteira |
| **Governador Aldric** | reeleito por unanimidade; faz um discurso de duas horas; ninguém se importa | continua a governar uma cidade que já não precisa tanto dele | **3**: muda o nome da cidade para "Ascendia-ao-Sol". Gagueja no discurso |

### 6.2 Os outros

| Quem | Condição | Frase |
|---|---|---|
| **Ssark** | `sssar_defendida` | a aldeia Sssar faz uma festa todos os anos no dia em que a defendeste. A tua estátua tem escamas pintadas |
| **Ssark** | `sssar_expulsa` e `ssark_97_sobe` | volta ao pântano e começa a juntar os seus, um a um. Demora anos. Consegue |
| **Ssark** | `sssar_expulsa` sem subir | fica na Cidade dos Perdidos, a talhar lanças pequenas que nunca acaba |
| **Kesh e Rakk** | `sssar_defendida` | os dois irmãos caçam juntos outra vez (o Rakk volta com o fim dos Renegados) |
| **Nina** | R10_08 feita | vê neve pela primeira vez. Faz um boneco de neve com duas pedras azuis no lugar dos olhos |
| **Os Perdidos convencidos** | um por um, os que convenceste | **Rafa**: grava um disco · **Doutor**: dá aulas na Biblioteca do Fausto ("O Sistema, Explicado Devagar") · **Bia**: abre uma enfermaria no Último Posto · **Ulisses**: deita-se na erva do Prado do Despertar todas as tardes · **Lino e Lia**: escondem-se um do outro por toda a Ascendia, e encontram-se sempre |
| **"Mãe Dois"** | `relogio_anda` | o cachecol fica pronto. Mede três quilómetros. Ela dá-o ao Aren |
| **O Desistente** | `desistente_ouvido` | levanta-se do caixote, numa manhã qualquer, e sobe até ao 98, sozinho, para ver a biblioteca |
| **Simão** (o Sem Número) | `ouviu_sem_numero` | volta à pirâmide do andar 38 e grava o próprio nome, com cuidado, por baixo do do Aren |
| **O Mamute Ancião** | `mamute_acalmado` | dorme ao sol, no andar 47. Tem crias. A imagem diz "Amigo dos Gigantes" |
| **O Mamute Ancião** | `mamute_morto` | o Zed pendura um bocado de marfim na porta do rancho, sem dizer nada |
| **Os fantasmas do navio** | `fantasmas_livres` | cinco luzes num mar calmo. O 3 377 (Duarte) acena |
| **A Pena** (Aerópolis) | R9_03 feita | ensina outras crianças aladas a voar. Diz que aprendeu "com uma pessoa sem asas" |
| **Aren** | finais 1, 2, 3, 4 | **1**: desce à Cidade dos Perdidos e senta-se ao lado da Mãe Dois · **2**: um rapaz de cabelo castanho num prado ao pé do mar, com um cão velho · **3**: uma luz azul-mar a mergulhar num oceano · **4**: dois rapazes a desenhar mapas nos degraus da Taberna |

### 6.3 A última imagem

Depois de todos, uma página do diário em branco. Uma mão (a do herói) escreve, com a letra do herói:
- *(final 1)* *"Dia 1. Acordei no meu quarto."*
- *(final 2)* *"Dia 1. Sentei-me no trono. Já não trago ninguém."*
- *(final 3)* *"Dia 1. Não há torre. Há céu."*
- *(final 4)* *"Dia 1. Abri a porta. Quem quiser, entra."*

E por baixo, pequenino, a assinatura: **"— {nome}, nº 10 000"**.

---

## 7. Flags e o que fica gravado

| Flag | Onde muda | Para quê |
|---|---|---|
| `final_1` / `final_2` / `final_3` / `final_4` | aqui | pós-jogo, conquistas, a imagem de título do jogo muda (quarto · trono · planície · ponte) |
| `final_janela` | fase 3 da C10-16 | os NPCs com 10 ❤️ têm uma frase cada (nos ficheiros de diálogo deles) |
| `ssark_97_sobe`, `perdidos_convencidos`, `sabe_nome_aren`, `kai_salvo`/`kai_vencido`, `samira_sabe`, `mamute_*`, `fantasmas_livres`, `relogio_anda`, `desistente_ouvido`, `ouviu_sem_numero` | capítulos anteriores | epílogos (secção 6) |

> **Novo Jogo+**: depois de qualquer final, pode-se começar de novo com o nível, as armas e as receitas. O Sistema diz,
> no primeiro ecrã: `[Sistema] Bem-vind{o/a}, Jogador{/a} nº 10 000. …Outra vez?` (sem falhas). O diário guarda as
> páginas já lidas (aparecem em cinzento até as voltares a encontrar).
