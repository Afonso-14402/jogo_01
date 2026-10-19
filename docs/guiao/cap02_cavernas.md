# Guião — Capítulo 2: Cavernas e Minas (andares 11–20)

Missões: **H_06 Povos Dentro da Torre**, **H_07 O Rei Sentado**. As cenas das povoações e das missões secundárias estão
em `docs/dialogos/povoacoes_r02.md`. Mapas: `docs/mapas/r02_cavernas.md`.

**O que este capítulo conta**: a torre não está vazia — há povos lá dentro (fungoides, anões, fantasmas). E os
guardas da torre respeitam a janela azul como a um rei. O jogador ouve, pela primeira vez, um nome no eco.

**O Sistema neste capítulo**: frio e burocrático, como na região 1. Uma só falha, no andar 17 (o eco).

---

## C2-01 — A Boca da Mina

| | |
|---|---|
| ID | `cena_c2_01_mina` |
| Quando | entrar pela primeira vez no andar 11 |
| Onde | andar 11, encosta rochosa → Boca da Mina |
| Quem | herói, Hilda Fundo-Rocha, mineiros |
| Música | `minas_eco` |

🎥 O herói sobe a escada de luz e sai numa encosta de pedra cinzenta. Ao fundo, a boca de uma mina com carris e lanternas.
🎬 À medida que o herói entra na mina, a luz do dia fica para trás. O ecrã escurece até sobrar só um círculo à volta dele.

- `[Sistema] Aviso: zona sem luz natural.`
- `tut_escuro`: `[Sistema] Está escuro. Usa tochas ou uma lanterna. Alguns inimigos só se veem com luz.`

🎬 Uma lanterna aparece ao fundo do túnel. Uma anã enorme, com uma trança ruiva e braços do tamanho de troncos, levanta-a.

- **Hilda** *(desconfiada)*: "Quem vem lá? Fala ou levas com a picareta!"
- **Hilda** *(normal)*: "…Uma janela azul nos olhos. Um Jogador. Entra, entra. Aqui toda a gente traz luz. Tu não trouxeste. Típico."
- 🎬 Atira-lhe três tochas.
- **Hilda** *(normal)*: "Hilda Fundo-Rocha. Mando no Posto Mineiro. Se te perderes nos túneis, morres. Se não te perderes, morres mais devagar. Bem-vind{o/a}."

▶ **"Obrigad{o/a} pelas tochas."**
▶ **"Vou precisar de mais do que três."**

- *(obrigado)* **Hilda** *(feliz)*: "Educad{o/a}! Já gosto mais de ti do que do outro."
- *(mais)* **Hilda** *(feliz)*: "Finalmente alguém com juízo! Tenho uma loja. Dez moedas cada."
- **Hilda** *(normal)*: "O outro? Um rapaz de casaco azul. Passou aqui há dois dias. Ganhou a corrida de vagonetas e foi-se. Sem pagar a tocha."

⚙ Desbloqueia o **Posto Mineiro Fundo-Rocha** (cama, cristal, loja, forja simples). Missões R2_01, R2_03, R2_09, R2_13, R2_14 disponíveis.
⚙ Missão **H_06 Povos Dentro da Torre** ativa: `[Sistema] Missão: explora os andares 11 a 20.`

---

## C2-02 — Os Que Vieram Antes

| | |
|---|---|
| ID | `cena_c2_02_mineiros` |
| Quando | entrar no Acampamento Perdido (andar 12) pela primeira vez |
| Onde | andar 12, Acampamento Perdido |
| Quem | herói (sozinho) |
| Música | `minas_eco` (mais lenta) |

🎬 Um acampamento antigo: tendas podres, uma fogueira apagada há muito, três esqueletos encostados à parede, sentados, com os capacetes postos.
🎬 Um dos esqueletos tem na mão um caderno aberto. O herói aproxima-se.

- 🎥 Grande plano do caderno: *"Dia 40. A comida acabou. Os rapazes estão a dormir. Eu também vou dormir. Se alguém encontrar isto: não temos janela azul. Viemos de Ascendia para cavar. A torre não nos queria cá em cima. Agora percebo."*
- 🎬 O herói olha para os esqueletos. Por cima de cada um não aparece nada: **nenhuma janela**, nenhum nome, nenhum nível.
- `[Sistema] Restos humanos. Sem registo.`

⚙ Sem falas. Dá a primeira pista de R2_03 (os diários têm números). A página 12 do diário do Aren está neste acampamento.

---

## C2-03 — A Mãe do Ninho

| | |
|---|---|
| ID | `cena_c2_03_aranha_antes` |
| Quando | entrar no Ninho (andar 15) |
| Onde | andar 15, O Ninho (arena) |
| Quem | herói, Aranha-Mãe, aventureiros nos casulos (se R2_04 estiver ativa) |
| Música | silêncio → `aranha_mae` |

🎬 Uma gruta redonda forrada de teias. Casulos pendurados no teto. Um deles mexe-se e geme.
- **Voz num casulo** *(abafada)*: "Socorro… alguém… está aí alguém?"
🎬 No fundo, um saco de seda enorme, cheio de ovos que pulsam. Por cima, no teto, oito olhos vermelhos abrem-se um a um.
🎥 A câmara recua. A **Aranha-Mãe** desce do teto num fio grosso, devagar, e pousa à frente do saco de ovos. As setas vermelhas das costas brilham.

- `[Sistema] Mini-boss: Aranha-Mãe, a Mãe do Ninho.`
- 🎬 A aranha levanta as patas da frente, mas **não ataca logo**: põe-se entre o herói e os ovos.

▶ **(Atacar.)**
▶ **(Recuar um passo.)**

- *(recuar)* 🎬 a aranha não se mexe. Depois, quando o herói para, ela ataca na mesma. `[Sistema] A Aranha-Mãe protege o ninho.`
- ⚙ Luta (ver `docs/BOSSES.md`, secção 3). Desafio do andar: vencer sem queimar as teias.

## C2-04 — Vitória

| | |
|---|---|
| ID | `cena_c2_04_aranha_depois` |
| Quando | vencer a Aranha-Mãe |
| Onde | andar 15, O Ninho |
| Quem | herói, aventureiros resgatados (se R2_04) |
| Música | `tristeza` (curta) |

🎬 A Aranha-Mãe cai de lado. As patas encolhem devagar. A última pata fica esticada na direção do saco de ovos.
- `[Sistema] Mini-boss derrotado: Aranha-Mãe.`
- `[Sistema] Vitória.`
🎬 A palavra "Vitória" fica no ecrã mais tempo do que o normal. Depois desaparece sem som.
🎬 (se R2_04 ativa) Os casulos rasgam-se. Três aventureiros caem ao chão, a tossir.
- **Aventureira Dália** *(feliz, fraca)*: "Estamos vivos… Estamos vivos! Quem és tu? Não interessa. Obrigada. Obrigada."

⚙ `[Sistema] Obtiveste: Presa Venenosa.` · Título *Sem Medo de Aranhas*. O casulo dourado (segredo) fica disponível.

---

## C2-05 — Mycélia

| | |
|---|---|
| ID | `cena_c2_05_mycelia` |
| Quando | entrar em Mycélia (andar 16) pela primeira vez |
| Onde | andar 16, Mycélia |
| Quem | herói, Ancião Gorro-Azul, Bolota, fungoides |
| Música | `cristal_canto` (versão de fungos: sinos e água) |

🎥 Uma caverna enorme cheia de fungos gigantes que brilham em azul e verde. Pontes feitas de lamelas. Casinhas dentro dos caules.
🎬 Dezenas de seres pequenos, com chapéus de cogumelo, param e olham. Os chapéus acendem-se em ondas de luz, um a seguir ao outro.
🎬 Um fungoide pequeno corre para o herói e fica a olhar para cima, com os olhos enormes.

- **Bolota** *(feliz)*: "És de CIMA? Não. És de BAIXO? De onde vem o SOL? Viste o SOL? Como é o SOL?"
- 🎬 Um fungoide muito velho, com um chapéu azul enorme e coberto de musgo, avança devagar. Muito devagar.
- **Ancião Gorro-Azul** *(normal, muito lento)*: "Bem… vindo… filho… da… janela…"
- `[Opção de diálogo: Acelerar a fala do Ancião]` (o jogador pode carregar em **Acelerar**: a fala passa a velocidade normal e o Ancião pisca os olhos, ofendido)
- **Ancião Gorro-Azul**: "Os nossos avós caíram aqui há muitas luas. A torre comeu o nosso mundo. Somos o que sobrou."
- **Ancião Gorro-Azul**: "A torre está viva, filho. Respira, cresce, tem fome. E come mundos."
- **Ancião Gorro-Azul** *(triste)*: "Nós somos o que ela come. Tu também. Só que a ti… ela come devagar."

▶ **"Como sabes que está viva?"**
▶ **"Há mais povos aqui dentro?"**

- *(viva)* **Ancião**: "Ponho a raiz no chão e ouço. Bate. Muito devagar. Uma vez por… muito tempo."
- *(povos)* **Ancião**: "Muitos. Em cada andar onde há luz… há alguém. Os anões, lá em cima, no 18. Mas os anões… agora são fantasmas."

⚙ Desbloqueia **Mycélia** (estalagem-cogumelo, cristal, loja). Missões R2_06, R2_07 disponíveis. H_06: `[Sistema] Mycélia visitada (1/2).`

---

## C2-06 — O Fosso dos Ecos

| | |
|---|---|
| ID | `cena_c2_06_fosso` |
| Quando | chegar à Borda Superior do andar 17 |
| Onde | andar 17, Borda Superior do Fosso dos Ecos |
| Quem | herói, Kai |
| Música | `minas_eco` (com eco forte) |

🎬 Um fosso enorme, tão fundo que não se vê o fim. Plataformas a descer pelas paredes, elevadores de corrente, correntes de ar.
🎬 Na beira, o Kai está sentado no chão, de costas para o fosso, encostado à parede. Está pálido.
- **Kai** *(zangado)*: "Não digas nada. Estou a descansar."
- **Kai** *(normal)*: "…Há quarenta minutos."
- **Kai** *(triste, baixo)*: "Tenho medo de alturas. Pronto. Disse. Desde pequeno. Não consigo subir a um escadote. E isto é um escadote do tamanho de uma cidade."
- *(se já viste a cena de 2 ❤️ do Kai, a fala de cima muda para)* **Kai** *(triste)*: "Já sabes. Alturas. E isto é a maior altura que já vi. Para baixo."

▶ **"Desço contigo."**
▶ **"A Yui ia rir-se de ti."** (só com a flag `kai_promessa_1`)
▶ **"Fica. Eu vou à frente e grito lá de baixo."**

- *(desço contigo)* **Kai** *(surpresa)*: "…Não precisas. Não é por ti. Está bem. Vai à frente. Mas devagar. MUITO devagar." ⚙ +30 amizade
- *(Yui)* **Kai** *(zangado, depois a rir)*: "Ia. Ia rir-se tanto. Ela sobe às árvores como um macaco." 🎬 levanta-se. ⚙ +30 amizade
- *(gritar)* **Kai** *(normal)*: "Grita alto. Muito alto. Quero ouvir que estás vivo."

⚙ **O Kai desce contigo** como companheiro temporário até ao Fundo do Fosso (mais lento nas plataformas; se o herói cair, o Kai grita).

### O eco

🎬 A meio da descida há um **ponto de eco** (pedra com um símbolo de boca). O tutorial dos pontos de eco aparece.
- `[Sistema] Ponto de eco. Grita (interagir) para revelar as plataformas invisíveis.`
- 🎬 O herói grita. O jogo mostra: *"{nome}!"*
- 🎬 O eco volta: *"…{nome}… {nome}…"*
- 🎬 E depois, mais baixo, uma voz diferente, quase sem som: *"…A…ren…"*
- 🎬 A janela do Sistema treme por meio segundo (falha visual: as letras ficam desfocadas).
- `[Sistema] Eco detetado.` *(as letras tremem)*
- **Kai** *(surpresa)*: "Ouviste isto? O eco disse outra coisa. Uma palavra. Não percebi."
- 🎬 O Kai grita também: *"YUI!"* O eco devolve: *"…Yui… Yui…"* — só isso.
- **Kai** *(normal)*: "O meu voltou igual. O teu voltou com… mais alguém."

▶ **"Deve ter sido o vento."**
▶ **"Era um nome."**

- *(vento)* **Kai**: "Pois. O vento. O vento das grutas fala muito." *(não acredita)*
- *(nome)* **Kai** *(sério)*: "Um nome. Pois. A torre anda a brincar connosco." ⚙ flag `eco_aren`

⚙ (A página 17 do diário, no Fundo do Fosso, diz: *"Gritei o meu nome no fosso. O eco respondeu com outro nome."*)

🎬 No fundo do fosso, o Kai senta-se no chão e respira fundo.
- **Kai** *(feliz, a tremer)*: "Desci. DESCI. Não contes a ninguém que tremi. Conta que desci."
- **Kai** *(normal)*: "Obrig… Fixe. Foi fixe. Vou à frente agora. Sozinho. Tenho de provar uma coisa a mim mesmo."

---

## C2-07 — A Forja dos Anões

| | |
|---|---|
| ID | `cena_c2_07_forja` |
| Quando | abrir o Grande Portão Anão (andar 18) |
| Onde | andar 18, Salão das Forjas |
| Quem | herói, fantasmas anões, fantasma de Grimbold (brevemente) |
| Música | `forja_ana` (começa apagada, ganha instrumentos quando se acendem as fornalhas) |

🎬 O portão de pedra tem 4 anéis com runas. Quando ficam na posição certa, as runas acendem-se a vermelho e formam um nome anão.
- `[Sistema] Inscrição: B·R·O·M.`
- 🎬 O portão abre-se com um som grave. Atrás, um salão enorme com dezenas de forjas apagadas, bigornas, martelos pendurados. Tudo coberto de pó.
🎬 O herói acende a primeira fornalha (puzzle). A luz laranja enche um canto do salão.
🎬 Na luz aparecem **fantasmas de anões**, transparentes, a martelar no vazio. Não reparam no herói.
🎬 O herói acende as três fornalhas. O salão inteiro ilumina-se. Os fantasmas param de martelar e viram-se ao mesmo tempo.

- **Fantasma Anão** *(normal, voz com eco)*: "Luz… Há cento e trinta anos que ninguém acende as forjas."
- **Fantasma Anão**: "És da janela. Os da janela vinham cá buscar armas. Antes. Muito antes."
- 🎥 Na parede, filas de **moldes de armas** pendurados. Cada um tem um número gravado: *4 112 · 5 003 · 7 680 · 9 961…*
- 🎬 O herói toca no molde 9 961. Uma espada sai do molde, enferrujada.
- **Fantasma Anão** *(triste)*: "Os anões forjavam para os que ainda não tinham chegado. A torre dizia-nos os números. Nós forjávamos. Nunca soubemos porquê."
- 🎬 Ao fundo, num corredor que vai para a Câmara do Mestre, aparece por um segundo um fantasma maior, de barba trançada, com um martelo partido. Olha para o herói.
- **Grimbold** *(muito baixo)*: "…Brom? Não… Não és o meu rapaz."
- 🎬 Desaparece.

⚙ H_06: `[Sistema] Forja Anã visitada (2/2).` · `[Sistema] Nova missão: conta ao Velho Fausto o que viste.`
⚙ Se tiveres **6 ❤️ com o Brom** (missão R2_05 ativa), o fantasma de Grimbold fica na Câmara do Mestre à tua espera (`docs/dialogos/povoacoes_r02.md`). Senão, aparece aí mais tarde, quando a missão abrir.
⚙ Os Ferreiros Fantasmas passam a vender **Lingotes Antigos**.

### C2-07b — Os Povos da Torre (Ascendia)

| | |
|---|---|
| ID | `cena_c2_07b_fausto` |
| Quando | falar com o Velho Fausto com H_06 no último passo |
| Onde | Biblioteca de Ascendia |
| Quem | herói, Velho Fausto |
| Música | `revelacao` (suave) |

🎬 O herói conta (montagem rápida, sem som: imagens de Mycélia, dos fantasmas, dos moldes com números).
- **Velho Fausto** *(surpresa)*: "Gente. Gente a viver lá dentro. Com casas, com mortos, com festas. A torre não é um castelo vazio. É um país."
- **Velho Fausto** *(normal)*: "E os moldes… armas para Jogadores que ainda não tinham chegado. Jovem, isto quer dizer que a torre sabe quem vem. Antes de chegarem."
- **Velho Fausto** *(normal)*: "Vou escrever isto. Hoje. Agora. Vai-te embora, que tenho de escrever."
- `[Sistema] Página especial obtida: "Os Povos da Torre".`

⚙ Missão **H_06** concluída. Missão **H_07 O Rei Sentado** ativa.

---

## C2-08 — O Outro Lado do Lago

| | |
|---|---|
| ID | `cena_c2_08_reflexo` |
| Quando | entrar no Lago Espelhado (andar 19) |
| Onde | andar 19, Margem de Vidro Negro |
| Quem | herói, o seu reflexo |
| Música | `cristal_canto` (lenta, desafinada) |

🎬 O chão é de cristal negro, liso como um espelho. O herói vê-se refletido por baixo dos pés.
🎬 O herói para. O reflexo continua a andar mais dois passos. Depois para também e vira-se para cima.
🎬 O reflexo **sorri**. O herói não sorriu.
- `[Sistema] …` *(janela vazia, sem texto, durante 2 segundos)*
🎬 O reflexo aponta para uma fenda na parede (é o primeiro dos 3 segredos do andar). Depois volta a imitar o herói, como se nada fosse.

⚙ Sem falas. A partir daqui, o reflexo às vezes aponta para segredos (mecânica do andar). O guardião deste andar é o **Reflexo Negro**.

---

## C2-09 — O Rei Sentado

| | |
|---|---|
| ID | `cena_c2_09_golem_antes` |
| Quando | entrar na Sala do Trono (andar 20) |
| Onde | andar 20, Sala do Trono |
| Quem | herói, Golem de Cristal |
| Música | silêncio → `golem_cristal` |

🎬 Uma escadaria enorme com degraus feitos para gigantes. No cimo, um salão com **seis colunas de cristal** azuis, roxas e verdes. Ao fundo, um trono de pedra.
🎬 No trono está sentado um **golem gigante** de rocha cinzenta, com cristais a sair dos ombros. Tem os olhos fechados. Não se mexe.
🎥 A câmara aproxima-se devagar da cara do golem. Pó cai do teto.
🎬 O núcleo de luz no peito acende-se. Os olhos abrem-se.
- `[Sistema] Boss: Golem de Cristal, o Rei Sentado.`
- 🎬 O golem não se levanta. Levanta só uma mão e aponta para o herói. As colunas brilham mais forte (o escudo).
- `[Sistema] Dica: as colunas de cristal protegem o boss.` *(só se for a 1.ª tentativa)*

⚙ Luta (ver `docs/BOSSES.md`, secção 4). O golem só se levanta do trono na fase 2.

## C2-10 — Ajoelhar

| | |
|---|---|
| ID | `cena_c2_10_golem_depois` |
| Quando | vencer o Golem de Cristal |
| Onde | andar 20, Sala do Trono |
| Quem | herói, Golem de Cristal |
| Música | `revelacao` |

🎬 O núcleo do golem racha. O golem cambaleia para trás, até ao trono.
🎬 Em vez de cair, **ajoelha-se**. Devagar. Mas não está virado para o herói.
🎥 A câmara roda: o golem está ajoelhado **virado para a janela azul do Sistema**, que flutua ao lado do herói.
- 🎬 O golem baixa a cabeça perante a janela. Depois desfaz-se em cristais.
- `[Sistema] Boss derrotado: Golem de Cristal.`
- `[Sistema] Obtiveste: Núcleo de Cristal.`
- `[Sistema] Título obtido: Quebra-Cristais.`
- `[Sistema] Região 2 concluída. Andar 21 desbloqueado.`
🎬 O herói olha para a janela azul. A janela fica parada, como sempre. Depois fecha-se sozinha.

⚙ (A página 20 do diário, aqui, diz: *"O Golem ajoelhou-se antes de cair. Não para mim. Para a janela azul."*)
⚙ Missão **H_07** concluída.

---

## C2-11 — Uma Casa

| | |
|---|---|
| ID | `cena_c2_11_dia_subida` |
| Quando | voltar a Ascendia depois do Golem |
| Onde | Praça da Torre (Dia da Subida, F_05) |
| Quem | herói, Governador Aldric, Lyra, Kai, Lucien, Brom, cidade |
| Música | `dia_da_subida` |

🎬 A Praça está em festa outra vez. Bandeirinhas de cristal (ideia do Gizmo). Uma estátua nova aparece ao lado da primeira: um golem pequeno de pedra (`Eb`).
- **Governador Aldric** *(no palco, nervoso)*: "Cidadãos! Pela segunda vez este ano… hum… *(procura a página)*… A região das minas está livre!"
- **Governador Aldric** *(feliz)*: "E conforme prometido… a cidade oferece a {nome} uma casa! Rua das Glicínias, número 7!"
- 🎬 Aplausos. O Aldric entrega uma chave grande. Depois uma pilha de formulários.
- **Governador Aldric** *(normal)*: "E os formulários. Em triplicado."
- **Lucien** *(do palco)*: "♪ Na sala das colunas, o rei de cristal / ajoelhou-se ao azul, que é coisa fatal… ♪"
- 🎬 Ao pé da fonte, o Kai come uma espetada, sozinho.

▶ **(Ir ter com o Kai.)**

- **Kai** *(normal)*: "Tens casa. Eu durmo na estalagem há meses. Não tenho inveja. Tenho um bocadinho."
- **Kai** *(sério)*: "O golem ajoelhou-se para a janela? Vi-o do Fundo do Fosso a subir. Não gosto disso. Não gosto de coisas que se ajoelham para o Sistema."
- **Kai** *(normal)*: "E aquele eco, no fosso… Ainda penso nele. Se a torre sabe nomes, sabe o meu também. E o da Yui."

▶ **"Vens jantar à minha casa nova?"**
▶ **"A torre não te vai tirar a Yui."**

- *(jantar)* **Kai** *(feliz, a disfarçar)*: "…Se tiveres comida. E cadeiras. Tens cadeiras? Compra cadeiras." ⚙ +30
- *(Yui)* **Kai** *(triste)*: "Não sabes isso. Mas… obrig… Fixe. Isso foi fixe." ⚙ +30

⚙ **A tua casa** fica disponível (Casinha, ver `docs/CIDADES.md`, secção 2). `tut_casa` (ver `docs/textos/tutorial.md`).
⚙ `[Sistema] Capítulo 3: O Pântano.` (título grande no ecrã)
