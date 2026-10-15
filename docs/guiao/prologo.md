# Guião — Prólogo

Missões: **H_00 Despertar**, **H_01 O Primeiro Lobo**, **H_02 Ascendia**, **H_03 A Primeira Subida**.
Duração: cerca de 20–30 minutos (com o tutorial).

---

## P1 — Antes

| | |
|---|---|
| ID | `cena_p01_antes` |
| Quando | depois de escolher a dificuldade, antes de criar a personagem |
| Onde | ecrã preto |
| Música | silêncio, depois um zumbido baixo |

🎥 Ecrã preto. Texto branco aparece letra a letra, sem caixa.

- *"Lembras-te do último dia normal?"*
- *"Do cheiro da tua casa. Do barulho da rua."*
- *"O que estavas a fazer antes de tudo ficar azul?"*

▶ **A caminho da escola, a correr porque estava atrasado.**
▶ **A jogar até tarde, só mais um nível.**
▶ **A ajudar alguém que precisava.**
▶ **A dormir. Só a dormir.**

⚙ Grava a **Origem** do herói (ver tabela). Muda um bónus pequeno e algumas falas no jogo.

| Origem | Bónus | Quem comenta |
|---|---|---|
| Atrasado | +5% velocidade de movimento | Kai ("Corres como quem perdeu o autocarro.") |
| Jogador | +5% XP das skills | Lyra ("Já sabes o que é um 'nível'? Ótimo, poupas-me o discurso.") |
| Ajudante | +10% pontos de amizade | Dona Marta ("Tens cara de quem ajuda os outros.") |
| A dormir | +10% Estamina máxima | Pip ("Também gosto de dormir. És boa gente.") |

- *"Então lembra-te disso. Vais precisar."*

🎥 O texto desaparece. Uma linha azul fina corta o ecrã ao meio, como uma janela a abrir.

- `[Sistema] A criar o registo do Jogador…`

⚙ Abre a **criação de personagem** (nome, pele, cabelo, olhos, roupa — ver `docs/INTERFACE.md`).

- `[Sistema] Registo criado. Bem-vindo, {nome}.`

---

## P2 — Despertar

| | |
|---|---|
| ID | `cena_p02_despertar` |
| Quando | depois de criar a personagem |
| Onde | andar 1, Colina do Despertar |
| Quem | herói, Sistema |
| Música | `prologo` |

🎥 Ecrã branco a desvanecer. Céu azul enorme. A câmara desce devagar até um prado de erva alta a ondular ao vento.
🎬 O herói está deitado na erva. Abre os olhos (2 frames). Senta-se. Olha à volta.

- `[Sistema] A verificar sinais vitais… ✓`
- `[Sistema] A verificar ligação ao Sistema… ✓`
- `[Sistema] Bem-vindo à Torre, Jogador nº 10 000.`

🎬 O herói levanta-se e recua um passo, assustado com a janela.

- `[Sistema] Missão principal: SOBE.`

🎥 A câmara roda e mostra, ao longe, um **círculo de pedras antigas** no cimo de uma colina, e por cima do céu…
nada. Um céu que parece um teto muito, muito alto.

⚙ Começa o **tutorial** (ver `docs/textos/tutorial.md`): mover, câmara, apanhar uma pedra.
⚙ Missão **H_00 Despertar** ativa.

### Tutorial no prado (sem cena, com mensagens)
1. `[Sistema] Usa [mover] para andar.`
2. Quando o herói chega perto de uma pedra brilhante: `[Sistema] Carrega em [interagir] para apanhar.`
   ⚙ +1 Pedra. `[Sistema] Obtiveste: Pedra ×1. É uma pedra. Parabéns.`
3. Um **Slime Verde** salta da erva alta.
   `[Sistema] Hostil detetado. Usa [atacar].`
4. Depois do 2.º golpe, o slime prepara um salto (encolhe-se).
   `[Sistema] Quando um inimigo se prepara para atacar, usa [esquivar].`
5. Slime derrotado: `[Sistema] +11 XP.` · `[Sistema] Obtiveste: Gel de Slime ×1.`
6. Mais dois slimes. Ao derrotá-los:
   `[Sistema] Subiste para o nível 2!`
   `[Sistema] Tens 5 pontos de atributo. Abre o Status com [status] quando quiseres.`

---

## P3 — O Primeiro Lobo

| | |
|---|---|
| ID | `cena_p03_lobo` |
| Quando | o herói chega ao fundo do Campo de Erva Alta |
| Onde | andar 1, Campo de Erva Alta |
| Quem | herói, Lobo Cinzento, Kai |
| Música | `floresta_perigo`, depois silêncio |

🎥 A erva mexe-se. Um rosnar. A câmara aproxima-se do herói.
🎬 Um **Lobo Cinzento** sai da erva, a mostrar os dentes.

- `[Sistema] Hostil detetado: Lobo Cinzento. Nível 3.`
- `[Sistema] Aviso: o nível do inimigo é superior ao teu.`

⚙ Luta **impossível de ganhar**: o lobo tem a vida a "???". O herói só tem de **sobreviver 20 s** (esquivar).
Se a vida do herói chegar a 10%, a cena continua mais cedo.

🎬 O lobo salta. O ecrã fica lento.
🎥 Um vulto atravessa o ecrã. Um corte azul. O lobo cai.
🎬 **Kai** aterra à frente do herói, de costas, com a espada curta na mão. Casaco azul rasgado, ténis gastos.

- **Kai** *(normal)*: "Tsc. Mais um."
- 🎬 Kai vira-se e olha o herói de cima a baixo.
- **Kai** *(normal)*: "Acordaste agora, não foi? Tens erva no cabelo."

▶ **"Quem és tu?"**
▶ **"Obrigado…"**
▶ **"Eu tinha aquilo controlado."**

- *(se "Quem és tu?")* **Kai** *(normal)*: "Kai. Jogador nº 9 999. E tu?"
- *(se "Obrigado…")* **Kai** *(feliz, só um bocadinho)*: "Não agradeças. Paga-me um jantar um dia. Número?"
- *(se "Eu tinha aquilo controlado.")* **Kai** *(feliz)*: "Ha! Claro. O lobo também achava que tinha. Número?"
  ⚙ +20 amizade com o Kai (gosta de atrevimento).

🎬 A janela azul do herói aparece sozinha: **Jogador nº 10 000**.

- **Kai** *(surpreso → feliz)*: "Dez mil? Ha. Número redondo. A torre gosta de números redondos."
- **Kai** *(sério)*: "Ouve. Isto não é um sonho e não é um jogo. Bem… é um jogo. Mas se morreres, dói."
- **Kai** *(normal)*: "Anda. Há um sítio seguro ali à frente. Depois explico… mais ou menos."

⚙ Kai segue o herói como companheiro temporário. Missão **H_01** ativa: "Segue o Kai".
*(se a Origem for "Atrasado")* **Kai**: "E corre. Corres como quem perdeu o autocarro."

---

## P4 — A Zona Segura

| | |
|---|---|
| ID | `cena_p04_zona_segura` |
| Quando | chegar à Zona Segura do andar 1 |
| Onde | andar 1, Zona Segura (fogueira e cristal) |
| Quem | herói, Kai |
| Música | `floresta_dia` (calma) |

🎬 Kai senta-se ao pé da fogueira. Um cristal azul alto brilha ao lado, a zumbir.

- **Kai** *(normal)*: "Aqui não aparecem monstros. Chama-se Zona Segura. Há uma em cada andar."
- **Kai** *(normal)*: "Aquilo é um cristal de teletransporte. Leva-te à cidade lá em baixo. E de volta."

▶ **"Que cidade?"**
▶ **"Que sítio é este?"**

- *(Que cidade?)* **Kai**: "Ascendia. Fica na base da torre. É onde vivem os que caíram aqui… como nós."
- *(Que sítio é este?)* **Kai**: "Isto? É o andar 1 de uma torre com cem andares. E nós estamos dentro dela."
- **Kai** *(pensativo)*: "Dizem que quem chega ao topo pode voltar para casa."
- 🎬 Kai olha para cima, para o céu-teto.
- **Kai** *(triste, rápido)*: "…Dizem muita coisa."
- **Kai** *(normal)*: "Toca no cristal. Vemo-nos lá em baixo."

⚙ Tutorial do cristal: `[Sistema] Toca no cristal com [interagir] para viajar.`
⚙ Desbloqueia a viagem andar 1 ↔ Ascendia.

---

## P5 — Ascendia

| | |
|---|---|
| ID | `cena_p05_ascendia` |
| Quando | primeira viagem para Ascendia |
| Onde | Praça da Torre |
| Quem | herói, Kai, aldeões |
| Música | `ascendia_dia` |

🎬 Flash azul. O herói aparece ao lado do Cristal Mestre, no centro da Praça.
🎥 **Plano grande**: a câmara sobe devagar pela torre — uma coluna de pedra gigantesca, cheia de janelas e
varandas nos primeiros andares, que se perde nas nuvens. Depois desce e mostra a cidade à volta: telhados
vermelhos, o mercado, fumo das chaminés, pessoas, um rio ao fundo.

- `[Sistema] Nova zona descoberta: Ascendia.`

🎬 Kai aparece num segundo flash azul.

- **Kai** *(feliz)*: "Bem-vindo a Ascendia. A cidade dos que caíram."
- **Kai** *(normal)*: "Vai à Guilda — o edifício grande com a bandeira azul, a norte. Pergunta pela Lyra."
- **Kai** *(normal)*: "Diz-lhe que fui eu que te mandei."
- 🎬 Kai dá dois passos e volta atrás.
- **Kai** *(envergonhado)*: "…Não, espera. Não lhe digas isso. Ela vai querer saber porque é que eu não fui lá entregar o relatório."
- 🎬 Kai foge a correr para o mercado.

⚙ Missão **H_02 Ascendia** ativa: "Vai à Guilda".
⚙ A partir daqui os aldeões da Praça têm falas de boas-vindas (ex.: "Um Jogador novo! Que a torre seja gentil contigo.").

---

## P6 — A Guilda e o Cristal de Avaliação

| | |
|---|---|
| ID | `cena_p06_guilda` |
| Quando | entrar na Guilda pela primeira vez |
| Onde | Guilda de Aventureiros, balcão |
| Quem | herói, Lyra, Mestre Gorvan |
| Música | `guilda` |

🎬 Lyra está atrás do balcão, a tentar segurar uma pilha de papéis que cai. Os óculos escorregam-lhe.

- **Lyra** *(surpresa)*: "Ah! Um momento! Um momentinho!"
- 🎬 Os papéis caem todos. Lyra suspira.
- **Lyra** *(feliz)*: "Bem-vindo à Guilda de Aventureiros de Ascendia! Eu sou a Lyra. Em que posso… espera."
- 🎬 Lyra inclina-se por cima do balcão e olha para o herói.
- **Lyra** *(feliz)*: "Erva no cabelo. Cara de assustado. És um Jogador novo! Que número?"

⚙ A janela do herói mostra: **Jogador nº 10 000**.

- **Lyra** *(muito surpresa)*: "DEZ MIL?!"
- 🎬 Toda a gente na Guilda se vira.
- **Lyra** *(envergonhada)*: "Desculpa. É que… é um número bonito. Vou escrevê-lo com a caneta boa."
*(se a Origem for "Jogador")* **Lyra**: "Já sabes o que é um 'nível'? Ótimo, poupas-me o discurso."
- **Lyra** *(normal)*: "Antes de te registar, tens de tocar no **Cristal de Avaliação**. Ele mostra o teu dom."

▶ **"Dom?"**
▶ **"Vamos a isso."**

- *(Dom?)* **Lyra**: "Todos os Jogadores trazem uma coisa especial. Uma **Skill Única**. Ninguém sabe porquê. Anda!"

🎬 Lyra leva o herói até uma sala com um cristal branco do tamanho de uma pessoa.
🎥 Aproximação lenta. O herói põe a mão no cristal. O cristal fica azul, depois brilha com a cor da skill.

- `[Sistema] A avaliar…`
- `[Sistema] Skill Única obtida: {skill_unica}.`

⚙ Sorteia a **Skill Única** (ver `docs/PROGRESSAO.md`). A Lyra reage conforme a skill:

| Skill Única | Lyra diz |
|---|---|
| Olho do Sistema | "Vês os números dos monstros? Isso é… um bocadinho assustador. E muito útil!" |
| Sorte do Herói | "Sorte! A torre dá mais coisas a quem tem sorte. Não jogues às cartas com o Lucien." |
| Mestre Artesão | "O Brom vai adorar-te. Bem, vai resmungar. É o jeito dele de adorar." |
| Coração de Dragão | "Curas-te sozinho? Ótimo. Menos Jogadores no hospital." |
| Passo Fantasma | "Esquivas duas vezes? Os monstros vão ficar tão confusos." |
| Língua Universal | "Falas com MONSTROS? Nunca vi isto. Tenho de escrever um relatório. Três relatórios!" |
| Mão de Midas | "Mais ouro! O Tobias vai querer ser teu amigo. Cuidado com o Tobias." |
| Aprendiz Rápido | "Aprendes depressa? Então ouve bem o que eu digo. Uma vez só." |
| Domador Nato | "O Zed, do rancho, vai querer conhecer-te. Ele não fala muito. O furão fala por ele." |
| Bolsa Infinita | "Uma mochila sem fundo! Leva também os meus papéis? …Estou a brincar. Mais ou menos." |
| Segunda Vida | "Levantas-te depois de cair. Isso é um dom… e uma responsabilidade, ouviste?" |
| Lâmina Espiritual | "A tua arma lança ondas de luz? Que bonito. E perigoso. Bonito e perigoso!" |

🎬 Passos pesados. **Mestre Gorvan** entra na sala: enorme, um braço só, capa de pele.

- **Gorvan** *(normal)*: "Hmm."
- **Lyra** *(nervosa)*: "Mestre Gorvan! Este é o Jogador nº 10 000. Acabou de—"
- **Gorvan** *(normal)*: "Eu ouvi. A cidade inteira ouviu."
- 🎬 Gorvan olha o herói nos olhos, em silêncio, durante 2 segundos.
- **Gorvan** *(normal)*: "Toma."
- 🎬 Atira uma espada de madeira com um núcleo de ferro. O herói apanha-a (ou não — animação engraçada se o jogador não carregar em nada).

⚙ Obtém **Espada de Treino** (ATQ 8). `[Sistema] Obtiveste: Espada de Treino.`
⚙ Tutorial de equipar: `[Sistema] Abre o Equipamento com [inventario] e equipa a espada.`

- **Gorvan** *(normal)*: "Rank F. Missões fáceis. Volta vivo."
- 🎬 Gorvan vira as costas e sai. Para à porta.
- **Gorvan** *(normal)*: "Não morras. É a única regra."
- 🎬 Sai.
- **Lyra** *(feliz)*: "Ele gostou de ti! …Acho. Com ele nunca se sabe."
- **Lyra** *(normal)*: "Vai à **Estalagem** da Dona Marta, no mercado. Ela dá um quarto aos Jogadores novos. E amanhã… sobes."

⚙ Rank **F**. Abre o quadro de missões (G_F_01–03). Recebe 100 ouro e 3 Poções de Vida P.

---

## P7 — A Estalagem

| | |
|---|---|
| ID | `cena_p07_estalagem` |
| Quando | entrar na Estalagem durante a missão H_02 |
| Onde | Estalagem "Ninho do Viajante" |
| Quem | herói, Dona Marta, (Kai ao fundo) |
| Música | `ascendia_noite` (lareira) |

🎬 A estalagem é quente: lareira, mesas de madeira, cheiro a sopa. Dona Marta limpa uma mesa.

- **Dona Marta** *(feliz)*: "Ora viva! Um Jogador novo, ouvi dizer. Dez mil, hã? Senta-te."
*(se a Origem for "Ajudante")* **Dona Marta**: "Tens cara de quem ajuda os outros. Gosto disso."
- **Dona Marta** *(normal)*: "Senta-te. Come. Depois falas."
- 🎬 Pousa uma tigela de sopa. O herói come (animação `sentar` + `beber`).
- `[Sistema] Comeste: Sopa de Legumes. HP recuperado.`
- **Dona Marta** *(normal)*: "O quarto do fundo é teu. Não pagas a primeira semana. Depois, 20 moedas. Ou ajudas-me com as compras."
- 🎥 Ao fundo, numa mesa, o Kai come sozinho e finge que não te está a ver.

▶ **Ir sentar ao pé do Kai.**
▶ **Ir dormir.**

- *(ao pé do Kai)*
  - **Kai** *(normal)*: "…Não te sentes. Pronto, senta-te."
  - **Kai** *(normal)*: "Amanhã o guardião do andar 1 vai estar à tua espera. Um coelho."
  - **Kai** *(sério)*: "Não te rias. Já mandou gente para a estalagem com o rabo em ferida."
  - ⚙ +20 amizade com o Kai.
- **Dona Marta** *(feliz, de longe)*: "Para a cama, os dois! Os heróis também dormem!"

### Primeiro sono
🎬 O herói deita-se. Ecrã escurece.
- `[Sistema] Progresso guardado.`
🎥 **Sonho**: imagem desfocada de um prado igual ao do andar 1, mas ao entardecer. Uma pessoa de costas, sozinha,
a escrever num caderno. Texto a aparecer como se fosse escrito à mão:
- *"Dia 1. Acordei num prado. Uma janela azul diz que sou o Jogador nº 1…"*
🎬 A pessoa vira a cabeça, como se tivesse ouvido alguém. Corte para branco.
- `[Sistema] Bom dia, Jogador nº 10 000.`

⚙ Dia 2 começa às 6:00. Missão **H_02** concluída. Missão **H_03 A Primeira Subida** ativa.

---

## P8 — A Primeira Subida

| | |
|---|---|
| ID | `cena_p08_primeira_subida` |
| Quando | aproximar-se do Círculo de Pedras (andar 1) com H_03 ativa |
| Onde | andar 1, Círculo de Pedras |
| Quem | herói, Coelho-Chifre Ancião, Kai (no fim) |
| Música | `guardiao` |

🎬 No meio do círculo de pedras, um coelho cinzento come erva. Parece normal… até se levantar: tem o tamanho de uma carroça,
um chifre partido e cicatrizes.

- `[Sistema] Guardião do andar 1: Coelho-Chifre Ancião.`
- `[Sistema] Derrota o guardião para desbloquear o andar 2.`

🎬 O coelho bate o pé no chão três vezes. Pedras saltam.
⚙ Luta contra o guardião (ver `docs/regioes/r01_floresta.md`). Desafio do guardião: vencê-lo sem poções.

### Depois da vitória
- `[Sistema] Guardião derrotado.`
- `[Sistema] Andar 2 desbloqueado.`
- `[Sistema] Obtiveste: Chifre Partido.` *(se cair)*
🎬 As pedras do círculo acendem-se com runas azuis. No centro abre-se uma escada de luz que sobe.
🎬 Kai está sentado numa pedra, a comer uma maçã.

- **Kai** *(feliz)*: "Nada mau, número redondo. Nada mau."
- **Kai** *(normal)*: "Faço-te uma proposta. Quem chegar primeiro ao **andar 5** paga o jantar."

▶ **"Aceito."**
▶ **"Já te devo um jantar."**

- *(Aceito)* **Kai** *(feliz)*: "Isso! Prepara a carteira."
- *(Já te devo)* **Kai** *(feliz)*: "Então pagas dois. Vamos!"
- 🎬 Kai salta para a escada de luz e desaparece a correr.

⚙ Missão **H_03** concluída. Missão **H_04 O Rei das Tocas** ativa.
⚙ `[Sistema] Capítulo 1: A Floresta.` (título grande no ecrã)
