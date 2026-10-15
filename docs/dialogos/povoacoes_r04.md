# Povoações da Região 4 — diálogos e missões

Os NPCs que vivem nos andares 31–40 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r04_deserto.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap04_deserto.md`.

**Torrenses**: a gente de Zahra e dos Nómadas nasceu **dentro da torre** e nunca viu o céu de Ascendia. Chamam aos
Jogadores **"descidos"** (os que descem pela escada de luz) e acham o céu de baixo "estranho, sem teto". Falam com
calma, com muitos provérbios de areia ("A areia não tem pressa."). Bips: médios, com um eco quente.

---

## 1. Caravaneiro Yusuf (andar 31)

| | |
|---|---|
| Voz | bips rápidos e aflitos; ri-se de nervos |
| Quem é | mercador de Zahra, 50 anos, barriga redonda, turbante amarelo desfeito. A caravana dele foi atacada pelos bandidos do Kasim. Os camelos fugiram. Ficou à sombra de uma roda "a pensar na vida e a perder água" |
| Depois de R4_02 | volta para Zahra e monta uma banca no bazar (vende o mesmo que a Loja de Viagem: ver `docs/LOJAS.md`, secção 3.5) |

| ID | Condição | Fala |
|---|---|---|
| `yusuf_01` | antes de R4_02 | "Os meus camelos! Três! A Bela, o Teimoso e o Senhor Bigodes! Fugiram com os bandidos atrás! Sem eles não volto a Zahra. Bem… volto. Mas a pé. E triste." |
| `yusuf_02` | antes de R4_02 | "Não és uma miragem, pois não? As miragens não suam. Tu suas. Ótimo." |
| `yusuf_03` | `missao(R4_01) == ativa` | "Cacto-Água! Da parte do Faisal? Esse avarento mandou-me água? Vou chorar. Não, que perco água." |
| `yusuf_04` | `missao(R4_02) == concluida` | *(no bazar de Zahra)* "O Senhor Bigodes cuspiu-me hoje de manhã. Sinal de que está feliz. Os camelos são assim." |
| `yusuf_05` | evento Caravana Atacada | "Outra vez! Outra vez! Porque é que é sempre a MINHA caravana? Eu pinto-a de outra cor, juro!" |

---

## 2. Oásis de Zahra (andar 32)

Primeira chegada: cena **C4-02**. O bazar tem **5 lojas** (Faisal, Nadia, Layla, a banca do Yusuf depois de R4_02 e a
loja de lâmpadas do Hakim depois do segredo do andar 36). O palácio só abre depois de R4_04.

### 2.1 Sultana Amira

| | |
|---|---|
| Voz | bips calmos e graves para uma mulher; nunca levanta a voz |
| Quem é | 35 anos, governante de Zahra desde os 20, véu dourado, olhos muito atentos. Justa, curiosa, cansada dos bandidos. Faz muitas perguntas sobre Ascendia ("Têm Sultana? Não? E quem manda? Um Governador? Ele é sábio?" — "…Ele tenta.") |
| Repete | "A areia não tem pressa. Eu tenho.", "Conta-me mais." |

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `amira_01` | — | normal | "Conta-me mais de Ascendia. As vossas casas têm telhado? Para quê, se o céu não tem fim? Chove? Chove muito? Que estranho." |
| `amira_02` | — | normal | "Zahra tem quatrocentas famílias. Eu conheço o nome de todas. Os avós dos avós conheciam os nomes dos avós dos avós delas. É assim que se governa." |
| `amira_03` | antes de R4_04 | zangada | "O Kasim chama-se 'Sultão'. Sultão de quê? De três grutas e cem ladrões? Eu é que tenho de dizer às mães porque é que os filhos não voltam das caravanas." |
| `amira_04` | `missao(R4_04) == concluida` | feliz | "Desde que o Kasim caiu, as caravanas chegam inteiras. Os mercadores já se queixam de outras coisas. É bom sinal: quando se queixam de pouco, é porque vivem bem." |
| `amira_05` | `boss_derrotado(farao)` | séria | "O Faraó da pirâmide era um descido? O Omar tinha razão. Odeio quando o Omar tem razão: fica insuportável durante uma estação inteira." |
| `amira_06` | `missao(R4_14) == concluida` | feliz | "Os banhos! Os banhos voltaram! Tomei três hoje. Uma Sultana limpa é uma Sultana justa. Não é provérbio. Acabei de o inventar." |
| `amira_curta` | já falaste hoje | normal | "Volta amanhã. Guarda as histórias para amanhã." |

**Perguntar sobre…**
- *Zahra*: "Os primeiros de Zahra caíram aqui com o oásis. Uma cidade inteira de outro mundo, engolida com a água e tudo. Não sabemos de que mundo. Sabemos que tínhamos sede."
- *Os descidos*: "Passam poucos. Uns ficam uma noite. Outros ficam uma vida. Nenhum desce outra vez pela escada. Só tu e os teus, que têm o cristal."

### 2.2 Mestre Rahim — domador de lagartos

| | |
|---|---|
| Voz | bips graves e lentos; assobia aos lagartos a meio das frases |
| Quem é | 70 anos, bigode branco enorme que lhe chega às orelhas. Doma Lagartos da Areia desde criança. Fala com eles mais do que com as pessoas ("os lagartos não mentem; as pessoas às vezes") |

| ID | Condição | Fala |
|---|---|---|
| `rahim_01` | `andar_maximo < 35` | "Um lagarto? Para ti? Ainda cheiras a pântano. Os lagartos não gostam de pântano. Volta quando tiveres passado o ninho dos escorpiões." |
| `rahim_02` | `andar_maximo >= 35`, R4_03 inativa | "Já cheiras a deserto. Bom. Vamos apanhar-te um lagarto. Não, não te vendo um. Os lagartos não se vendem. Apanham-se. Ou eles apanham-te." |
| `rahim_03` | — | *(assobia)* "Este chama-se Relâmpago. É o mais lento. Os nomes são para dar coragem." |
| `rahim_04` | `missao(R4_03) == concluida` | "O teu lagarto está gordo? Dá-lhe menos tâmaras. Está magro? Mais tâmaras. É toda a ciência." |
| `rahim_05` | `missao(R4_08) == concluida` | "Ganhaste ao Tarik três vezes! O rapaz chorou no estábulo. Eu também chorei. A rir." |

### 2.3 Faisal — mercador de luxo

| | |
|---|---|
| Voz | bips doces e espertos; fala depressa quando sente lucro |
| Quem é | 45 anos, anéis em todos os dedos, tapetes, especiarias e lâmpadas. Avarento mas honesto ("nunca enganei ninguém; só os deixei pagar muito") |
| Loja | tapetes (móveis), especiarias, Açafrão, Perfume, Lâmpada Velha (missão R4_11) · 10% de desconto depois de R4_01 |

| ID | Condição | Fala |
|---|---|---|
| `faisal_01` | abrir loja | "Bem-vind{o/a}! Tudo é caro, mas tudo vale o preço. Quase tudo. Aquilo não. Aquilo é caro e mau. Não compres aquilo." |
| `faisal_02` | — | "Um tapete de Zahra dura cem anos. O dono dura menos. Por isso compra dois: um para ti, um para os teus netos." |
| `faisal_03` | `missao(R4_01) == concluida` | "Salvaste a caravana do Yusuf. Ele deve-me dinheiro. Agora pode pagar-me. Obrigado duas vezes." |
| `faisal_04` | `missao(R4_11) == concluida` | "Um desejo! E pediste ISSO? Eu teria pedido uma loja maior. Ou duas lojas. Cada um é como é." |

### 2.4 Layla — dançarina

| | |
|---|---|
| Voz | bips alegres e musicais, sobe e desce como uma canção |
| Quem é | 22 anos, dança no bazar ao pôr do sol com lenços de todas as cores. Quer fazer o **Festival do Oásis**, que não se faz há 10 anos (desde que os bandidos atacaram o último) |
| Loja | cosméticos: lenços, véus, Vestes de Dança (depois de R4_10) |

| ID | Condição | Fala |
|---|---|---|
| `layla_01` | — | "Dança comigo! Não? Então bate palmas. Toda a gente sabe bater palmas. …Quase toda a gente." |
| `layla_02` | `hora entre 18 e 20` | *(a dançar)* "O sol põe-se e o bazar fica cor de laranja. É a hora mais bonita de Zahra. Fica a ver." |
| `layla_03` | antes de R4_10 | "Há dez anos que não há festival. Os mais novos nunca viram um. Eu vi um. Tinha doze anos. Nunca mais parei de dançar." |
| `layla_04` | `missao(R4_10) == concluida` | "O Festival voltou! E dançaste! Mal! Mas dançaste! É isso que conta!" |

### 2.5 Velho Omar — contador de histórias

| | |
|---|---|
| Voz | bips muito lentos e roucos; faz pausas compridas para criar suspense |
| Quem é | 88 anos, cego de um olho, senta-se sempre no mesmo banco do bazar. Sabe mil histórias e jura que todas são verdade. Conhece as lendas dos **reis de cima** (os Administradores, sem saber o nome) |
| Serviço | conta **uma lenda por dia** (lore; cada lenda nova dá +1 entrada no Diário → Lendas) |

| ID | Condição | Fala |
|---|---|---|
| `omar_01` | — | "Senta-te. Há uma história para cada grão de areia. Hoje conto-te uma. Amanhã, outra. Quando acabarem, morro. Por isso vem devagar." |
| `omar_02` | `missao(H_10) == concluida` | "Administradores, dizem os teus sábios. Nós dizíamos 'os reis de cima'. Nomes diferentes para a mesma coroa." |
| `omar_03` | `boss_derrotado(farao)` | "O Faraó caiu. A minha avó dizia que ele chorava à noite, lá dentro. Ninguém acreditava. Agora já não chora. Isso é bom ou mau? Depende de quem chorava." |

**Lendas do Omar** (uma por dia, pela ordem; `omar_lenda_<n>`)

| Nº | Lenda |
|---|---|
| 1 | "O Primeiro Rei de Cima: no princípio, um descido subiu a escada toda. No topo, a torre pôs-lhe uma coroa. Ele reinou até ficar cansado. Depois chamou outro." |
| 2 | "As Estrelas Pregadas: o céu de Zahra foi pintado por um rei que tinha saudades do céu dele. Pintou as estrelas que se lembrava. Esqueceu-se de algumas. Por isso há buracos escuros." |
| 3 | "A Criança da Estrela: as crianças que nascem com uma estrela no olho são chamadas pela torre. Um dia ouvem uma voz e sobem. Não voltam. Por isso as mães, quando as têm, mandam-nas descer." |
| 4 | "O Oásis que Não Desaparece: entre as miragens há uma verdadeira. Só ela tem sombra ao meio-dia. Quem bebe dela nunca mais tem sede." |
| 5 | "Os Dragões Caídos: houve um céu cheio de dragões. A torre engoliu-o. Os dragões caíram no 37 e ficaram lá, em ossos, a olhar para cima." |
| 6 | "O Nome Raspado: na porta da pirâmide há um nome que ninguém pode ler. O dono recusou uma coroa. A torre nunca lhe perdoou." |
| 7 | "A Lâmpada e o Djinn: o Djinn da tempestade foi preso numa lâmpada por um rei de cima. Quem lha devolver tem direito a um desejo. Um. Não peças mais. Ele zanga-se." |

> A lenda 3 é a do Rook (`docs/dialogos/rook.md`, 8 ❤️). A 6 é o Jogador Sem Número (região 10). Ninguém em Zahra sabe
> que são verdade.

### 2.6 Ferreira Nadia

| | |
|---|---|
| Voz | bips firmes e curtos; martela enquanto fala |
| Quem é | 40 anos, braços queimados da forja, lenço vermelho na cabeça. Única forja de prata da região. Tem uma rivalidade amigável com o Brom por carta ("Diz ao velho anão que as minhas cimitarras cortam melhor do que as espadas dele." — o Brom responde: "Hmpf.") |
| Loja | armas e armaduras de Prata (Comuns), melhorias até +5, receitas de cimitarras (aspeto de espada) |

| ID | Condição | Fala |
|---|---|---|
| `nadia_01` | abrir loja | "Prata! Corta, brilha e assusta mortos-vivos. Escolhe." |
| `nadia_02` | — | "O Brom ainda está vivo? Diz-lhe que a prata não se martela como o ferro. Ele sabe. Mas gosta que lho digam." |
| `nadia_03` | arma de Brom +6 ou mais equipada | "Isso é trabalho do Brom. …Está bom. Não lhe digas que eu disse." |

### 2.7 Encarregado Bilal — banhos

| | |
|---|---|
| Voz | bips lentos e tristes; suspira muito |
| Quem é | 55 anos, careca, toalha ao ombro. Os banhos de Zahra estão fechados há 3 anos: o aqueduto partiu-se numa tempestade e não há prata para os canos |

| ID | Condição | Fala |
|---|---|---|
| `bilal_01` | antes de R4_14 | "Os banhos estão fechados. Há três anos. As pessoas lavam-se na lagoa. Os peixes queixam-se." |
| `bilal_02` | `missao(R4_14) == concluida` | "Banho! Quente! Com sais! Entra! Sai mais leve, mais limpo e mais feliz. Garantido. Ou devolvo a toalha." |

### 2.8 Hakim — mercador de lâmpadas (depois do segredo do andar 36)

| | |
|---|---|
| Quem é | velho magríssimo, preso **7 anos** na Caravana Perdida do andar 36 (sobreviveu a comer tâmaras secas e a beber da cisterna da caravana). Quando o salvas, volta a Zahra e abre uma loja de lâmpadas |
| Loja | lâmpadas (móveis de luz para a casa), Óleo de Lâmpada, Lanterna do Deserto (luz de 6 m, não se apaga com vento) |

| ID | Condição | Fala |
|---|---|---|
| `hakim_salvar` | na Caravana Perdida (andar 36) | "Uma pessoa… uma pessoa a sério… Não és mais uma miragem? Já falei com tantas. Uma até me vendeu um camelo." |
| `hakim_01` | em Zahra | "Sete anos na tempestade. Agora vendo luz. Nunca mais quero estar às escuras. Compra uma. Por favor. Por mim." |

### 2.9 Samira (só com `rook_mae_zahra`)

| | |
|---|---|
| Quem é | Torrense de 70 anos, costureira. Senta-se à porta de casa, ao pé do poço, a olhar para a escada de luz. É a mãe do Rook |
| Onde | rua dos poços, 8:00–18:00 |

**Conversa** (`cena_samira`, 1.ª vez)
- **Samira** *(normal)*: "Desculpa, descid{o/a}. Pergunto a todos os que descem. Viste lá em baixo um rapaz com uma estrela no olho? Uma cicatriz pequena. Aqui."
- **Samira** *(triste)*: "Mandei-o descer quando tinha oito anos. Para a torre não o levar. Já deve ser um homem. Se estiver vivo."

▶ **"Vi. Está vivo. Chama-se Rook."**
▶ **"Não sei. Desculpe."**

- *(está vivo)* **Samira** *(surpresa, depois a chorar)*: "Rook… Não era esse o nome que lhe dei. Mas se é o que ele escolheu, é o nome certo."
  - **Samira** *(feliz)*: "Não lhe digas para subir. Não. Diz-lhe só… diz-lhe que a mãe come bem, que o poço ainda tem água e que ele fez bem em descer."
  - ⚙ flag `samira_sabe`. Recebe **Lenço de Samira** (item de missão: entregar ao Rook). O Rook tem a fala `rook_samira` (abaixo) e o **epílogo** dele muda (visita Zahra: ver `docs/textos/finais.md`).
- *(não sei)* **Samira** *(normal)*: "Pois. Ninguém sabe. Obrigada na mesma. Se o vires… não lhe digas nada. Melhor assim." ⚙ podes voltar a falar com ela e mudar de resposta

**Entregar o lenço ao Rook** (`rook_samira`, nos telhados de Ascendia, à noite)
- 🎬 O Rook pega no lenço. Cheira-o. Fica de costas muito tempo.
- **Rook** *(triste)*: "…Ela borda sempre uma estrela no canto. Sempre fez. Até nos meus sapatos."
- **Rook** *(normal)*: "O poço ainda tem água? …Ainda bem. Ainda bem, Dez Mil."
- ⚙ +100 amizade com o Rook.

### 2.10 Aldeões de Zahra (sem nome)

| ID | Quem | Fala |
|---|---|---|
| `zahra_crianca_01` | criança | "És descid{o/a}? Desce outra vez! Quero ver! …Não podes? Que aldrabice." |
| `zahra_velho_01` | velho no banco | "A areia não tem pressa. Eu também não. Senta-te." |
| `zahra_vendedor_01` | vendedor de tâmaras | "Tâmaras! Doces como o primeiro beijo e duras como o segundo!" |
| `zahra_guarda_01` | guarda | "Não corras no bazar. Não toques nos tapetes. Não olhes para a Sultana durante muito tempo. Bem-vind{o/a}." |
| `zahra_mae_01` | mãe com um bebé | "Ele nasceu ontem. Contei-lhe os dedos e olhei-lhe para os olhos. Sem estrela. Graças à areia." |

---

## 3. Acampamento dos Escavadores (andar 34)

Primeira chegada: cena **C4-04**.

### 3.1 Professora Íris Pá-Velha

| | |
|---|---|
| Voz | bips agudos e rápidos; ri-se com um "ha!" seco |
| Quem é | 62 anos, arqueóloga de Ascendia, óculos enormes, chapéu de abas largas, pincel sempre na boca. Amiga e rival do Velho Fausto há 40 anos (estudaram juntos; ela foi para o campo, ele ficou nos livros). Fala de tudo como se fosse uma descoberta |
| Repete | "Esplêndido!", "As manchas também dizem coisas." |

| ID | Condição | Fala |
|---|---|---|
| `iris_01` | — | "Esplêndido! Um caco! …Não. É uma pedra. Mas é uma pedra antiga. Todas são. Ha!" |
| `iris_02` | — | "O Fausto acha que se aprende tudo nos livros. Eu acho que se aprende tudo a cavar. Os dois temos razão. Ele um bocadinho menos." |
| `iris_03` | antes de R4_05 | "Debaixo da areia há uma cidade inteira. Ruas, casas, pão nas mesas. Pão de pedra. A areia muda todos os dias. Preciso de alguém com pá e paciência." |
| `iris_04` | `missao(R4_05) == concluida` | "As cinco portas! A cidade chamava-se **Qasr-al-Ma**, 'o palácio da água'. Engolida com o rio. O rio é que não veio." |
| `iris_05` | `missao(H_10) == concluida` | "Uma roda. Não consigo deixar de pensar nisso. Escavo há quarenta anos e nunca encontrei uma coisa que me desse tanto medo. Nem uma múmia." |
| `iris_curta` | já falaste hoje | "Estou ocupada! Estou sempre ocupada! Fala. Rápido. Esplêndido." |

### 3.2 Beto — escavador

| ID | Condição | Fala |
|---|---|---|
| `beto_01` | — | "Pás! Cordas! Tochas! Tudo o que um escavador precisa. Menos costas novas. Isso não vendo." |
| `beto_02` | a dormir (12:00–14:00) | *(dentro de um buraco, com o chapéu na cara)* "…Zzz… mais um caco… zzz…" |
| `beto_03` | `missao(R4_05) == concluida` | "Cinco portas num dia! A Professora deu-me folga. A primeira em seis anos. Não sei o que se faz numa folga." |

### 3.3 Guarda Sami

| | |
|---|---|
| Quem é | 30 anos, ex-aventureiro de rank D, guarda o acampamento sozinho. Tem medo de múmias ("são pessoas embrulhadas; não é natural") mas fica na mesma |

| ID | Condição | Fala |
|---|---|---|
| `sami_01` | dia | "De dia é calmo. De noite, a areia mexe-se. E das covas saem coisas embrulhadas." |
| `sami_02` | noite | "Shhh. Estás a ouvir? Não? Ainda bem. Eu estou sempre a ouvir." |
| `sami_03` | `missao(R4_06) == concluida` | "Dormi. Uma noite inteira. Sem uma múmia. Obrigado. Sonhei com o mar. Nunca vi o mar." |

---

## 4. Nómadas do Vento (andar 37)

Mudam de sítio no andar **todos os dias às 6:00** (5 sítios possíveis, ver o mapa). À noite acendem uma fogueira
grande: vê-se de longe. Sem cristal: o teletransporte leva-te à Zona Segura do andar.

### 4.1 Anciã Sahra

| | |
|---|---|
| Voz | bips muito baixos e lentos, como um vento; nunca pisca os olhos |
| Quem é | idade desconhecida ("contei até cem e depois parei"), olhos brancos, mãos pintadas de azul. Lê as estrelas pregadas do céu da torre. Guarda o **Poço dos Ossos** (a masmorra). Fala por enigmas, mesmo quando pede o almoço |

| ID | Condição | Fala |
|---|---|---|
| `sahra_01` | — | "Tens a janela atrás dos olhos. Vejo-a. É azul e não pisca. Tu piscas. Ainda bem." |
| `sahra_02` | — | "O que tem cem degraus e nenhum corrimão? A torre. O que tem um corrimão e nenhum degrau? O teu coração. Pensa nisso. Eu também não percebi." |
| `sahra_03` | antes de R4_09 | "Escondi cinco pedras na areia, uma em cada sítio onde o vento canta. Cada uma tem uma pergunta. Responde às cinco e abro-te o poço." |
| `sahra_04` | `missao(R4_09) == concluida` | "Cinco respostas. O poço abre-se. Lá em baixo dorme um dragão que nunca voou. Acorda-o com respeito. Ou não o acordes." |
| `sahra_05` | `missao(H_10) == concluida` | "Agora sabes da roda. Eu sempre soube. As estrelas são pregadas pelos que rodam. Um dia alguém vai parar a roda. Ou vai rodar com ela." |

### 4.2 Tarik — corredor de lagartos

| ID | Condição | Fala |
|---|---|---|
| `tarik_01` | — | "Corres? Tens lagarto? Não tens? Então anda a pé atrás de mim. Ha! Brincadeira. Arranja um lagarto e vem." |
| `tarik_02` | com montada, antes de R4_08 | "Um Lagarto da Areia! Do Rahim! Vamos ver se ele te ensinou a segurar as rédeas. Três corridas. Se ganhares as três, dou-te a minha sela." |
| `tarik_03` | `missao(R4_08) == concluida` | "Perdi três vezes. Para um descido. A minha avó não me fala. O meu lagarto também não." |

### 4.3 Mina — tecelã

| ID | Condição | Fala |
|---|---|---|
| `mina_01` | abrir loja | "Lenços contra o sol. Turbantes contra a areia. Tapetes contra o chão frio. Tudo contra alguma coisa." |
| `mina_02` | — | "Teço o caminho dos nómadas num tapete. Cada dia, uma linha. Este já tem trinta anos. Quando eu morrer, alguém continua." |
| `mina_03` | — | "Sementes de melão? Toma. Planta no calor. E rega pouco. Os melões do deserto não gostam de mimos." |

---

## 5. Missões da região, passo a passo

### R4_01 — Água para a Caravana
| | |
|---|---|
| Quem dá | Faisal (Zahra) |
| Recompensa | 400 ouro · 10% de desconto no bazar |

1. **Pedir** — **Faisal**: "O Yusuf deve-me dinheiro e está preso no 31 sem água. Se morrer, não me paga. Leva-lhe dez Cacto-Água. É generosidade. Com juros."
2. **Passo**: apanhar **10 Cacto-Água** (cactos dos andares 31, 33 e 36, com lâmina) e entregá-los ao **Yusuf** (andar 31).
   - **Yusuf**: "Água! Do Faisal?! Vou ter de lhe pagar, não vou? …Bebo na mesma."
3. **Entregar** — **Faisal** *(feliz)*: "Vivo e com sede de pagar! Esplêndido. Toma, e a partir de hoje tens desconto. Pequeno. Não te habitues."

### R4_02 — Os Camelos Perdidos
| | |
|---|---|
| Quem dá | Caravaneiro Yusuf (andar 31) |
| Recompensa | **Cantil Infinito** (anula o sol do deserto) |

1. **Pedir** — **Yusuf**: "Três camelos. A Bela tem um laço vermelho. O Teimoso não se mexe. O Senhor Bigodes cospe. Encontra-os e traz-mos."
2. **Passos** (puzzle do andar 31):
   - **A Bela** — no Mar de Dunas, rodeada de Chacais (vencer os chacais; ela segue-te);
   - **O Teimoso** — enterrado até à barriga numa **areia movediça** (puxá-lo: carregar em [interagir] 10 vezes depressa sem cair também);
   - **O Senhor Bigodes** — no topo do Rochedo do Vigia (só desce se lhe deres uma **Tâmara**; cospe-te na cara na mesma).
   - Os camelos seguem-te até à caravana; se te afastares mais de 15 m, param e sentam-se.
3. **Entregar** — 🎬 o Yusuf abraça os três camelos ao mesmo tempo. O Senhor Bigodes cospe-lhe.
   - **Yusuf** *(a chorar de alegria)*: "Toma! O meu cantil. Era do meu pai. Nunca seca. Ninguém sabe porquê. Eu acho que é magia. O meu pai achava que era sorte."

### R4_03 — Lagarto da Areia
| | |
|---|---|
| Quem dá | Mestre Rahim (Zahra), com `andar_maximo >= 35` |
| Recompensa | **Montada Lagarto da Areia** |

1. **Pedir** — **Rahim**: "No 31, nas dunas grandes, andam lagartos selvagens. Leva este laço. Atira-o, segura-te e não largues. Quando ele parar de correr, é teu."
2. **Passo — o minijogo do laço**:
   - encontrar um **Lagarto da Areia selvagem** (andar 31, Mar de Dunas, 3 a 5 de cada vez; fogem se correres para eles: aproxima-te a andar);
   - atirar o laço com [atacar] (a 6 m);
   - **segurar**: o lagarto puxa para os lados; mantém o ponteiro no meio da barra (como a pesca) durante **15 s**. Se a barra chegar ao fim, cais e ele foge.
3. **Entregar** — 🎬 voltas a Zahra montad{o/a} no lagarto. O Rahim assobia; o lagarto deita-se.
   - **Rahim** *(feliz)*: "Ele escolheu-te. Os lagartos não escolhem qualquer um. Dá-lhe um nome. Bonito. Os nomes dão coragem."
   - ⚙ Escolher o nome da montada. `tut_montada`.

### R4_04 — O Esconderijo de Kasim
| | |
|---|---|
| Quem dá | Sultana Amira |
| Recompensa | 3 000 ouro · **Turbante do Sultão** (do Kasim) · o **palácio** de Zahra abre (biblioteca de lendas e a varanda) |

1. **Pedir** — **Amira**: "O Kasim esconde-se no Desfiladeiro, no 33. Ninguém sabe onde. Dizem que atrás de uma cascata. Mas no deserto não há cascatas."
2. **Passo 1**: no andar 33, encontrar a **cascata de areia** (areia a cair de uma fenda na parede, nas Salinas). Atravessá-la.
3. **Passo 2**: o esconderijo: 3 salas com o bando (Bandidos do Deserto e um Chefe de Bando). Na 3.ª sala, o **Sultão Bandido Kasim**.
   - **Kasim** *(feliz, a afiar as cimitarras)*: "Uma visita! Sem convite! Que falta de educação. Eu, pelo menos, quando roubo uma caravana, digo bom dia."
4. **Passo 3**: aos 20% de vida, o Kasim **foge** pelos túneis (atira bombas de fumo). Persegue-o (30 s) até à saída da gruta, onde fica encurralado.
   - **Kasim** *(nervoso)*: "Pronto! Pronto! Rendo-me! Diz à Sultana que eu… que eu ia devolver tudo. Amanhã. Ou depois."
5. **Entregar** — o Kasim vai preso para Zahra (aparece numa jaula no palácio, a queixar-se).
   - **Amira** *(feliz)*: "O 'Sultão' na minha jaula. Vou deixá-lo lá uma semana a ouvir a Layla ensaiar. É o castigo mais cruel que conheço."
   - **Kasim** *(da jaula, depois)*: "Ela canta mal! Canta MESMO mal! Alguém me salve!"

### R4_05 — A Cidade Debaixo da Areia
| | |
|---|---|
| Quem dá | Professora Íris (andar 34) |
| Recompensa | 1 500 ouro · **Pá de Prata** (escava mais depressa e abre portas soterradas de prata) |

1. **Pedir** — **Íris**: "Encontrei um mapa da cidade num vaso partido. Cinco portas, numeradas. Se as abrirmos pela ordem, chegamos ao arquivo. Pela ordem, ouviste? A cidade era muito arrumada."
2. **Passos**: escavar as **5 portas soterradas** do andar 34 pela ordem do mapa da Íris (I, II, III, IV, V). A areia muda todos os dias: o mapa mostra onde estão **hoje**.
   - Abrir fora de ordem: a porta abre, mas a sala está vazia e a areia volta a tapar as abertas (recomeça).
   - Cada porta tem uma sala: casa com pão de pedra (I), escola (II), padaria (III), fonte seca (IV), **arquivo** com tábuas de barro (V).
3. **Entregar** — **Íris** *(feliz)*: "Qasr-al-Ma! O nome da cidade! E tábuas de barro com a lista do pão de cada dia! Esplêndido! Um dia inteiro de uma cidade, em tábuas. Toma a minha pá de prata. A sério. Eu compro outra. Ha!"

### R4_06 — Noite no Acampamento
| | |
|---|---|
| Quem dá | Guarda Sami (andar 34) |
| Recompensa | **Amuleto do Escaravelho** (imune a Maldição) |

1. **Pedir** — **Sami**: "Esta noite é lua nova. Nas noites de lua nova saem mais múmias. Fica comigo. Por favor. Pago-te. Com um amuleto. E com gratidão. A gratidão não serve para nada, mas é sincera."
2. **Passo**: das **21:00 às 3:00**, defender o acampamento de **3 ondas**:
   - onda 1 (22:00): 6 Múmias;
   - onda 2 (0:00): 4 Múmias + 3 Esqueletos Guerreiros;
   - onda 3 (2:00): 1 **Múmia Real** (Elite) + escaravelhos.
   - Se as múmias chegarem às tendas (3 vezes), a missão falha (repete-se na próxima lua nova).
3. **Entregar** — 🎬 nasce o sol. O Sami adormece de pé, encostado à lança. Acorda com um susto.
   - **Sami** *(feliz)*: "Já é de dia? Ganhámos? Ganhámos! Toma. O amuleto. Era da minha avó. Ela dizia que as múmias têm medo de escaravelhos. Eu tenho medo dos dois."

### R4_07 — Os Hieróglifos (história)
= **H_10**. Ver as cenas **C4-04, C4-08 e C4-11** em `docs/guiao/cap04_deserto.md`.

### R4_08 — Corrida de Lagartos
| | |
|---|---|
| Quem dá | Tarik (Nómadas, andar 37) — precisa de montada |
| Recompensa | **Sela de Corrida** (+15% velocidade da montada) |

1. **Pedir** — **Tarik**: "Três corridas. Três pistas. Se ganhares as três, a sela é tua. Se perderes uma, recomeças. É a regra dos nómadas. Acabei de a inventar."
2. **Passos** — 3 corridas no andar 37, contra o Tarik (o lagarto dele corre 10% mais do que o teu sem sela):
   - **Pista das Costelas**: por baixo dos arcos de ossos (curvas apertadas);
   - **Pista das Caveiras**: saltar por cima de 5 caveiras pequenas (carregar em [esquivar] no sítio certo);
   - **Pista do Vento**: com tempestade de areia (vento lateral; visão curta).
   - Atalhos: cada pista tem um atalho escondido (há uma Tâmara pendurada que mostra onde).
3. **Entregar** — **Tarik** *(zangado, depois ri-se)*: "Três! TRÊS! Toma a sela. Não, espera. Deixa-me despedir dela. …Pronto. Toma."

### R4_09 — Os Enigmas da Sahra
| | |
|---|---|
| Quem dá | Anciã Sahra (Nómadas, andar 37) |
| Recompensa | **Mapa das Estrelas** (mostra os baús de ouro da região) · abre a masmorra **Túmulo do Dragão Antigo** |

1. **Pedir** — **Sahra**: "Cinco pedras. Cinco perguntas. As pedras estão onde o vento canta. Responde em voz alta. As pedras ouvem."
2. **As 5 pedras-enigma** (cada uma tem uma pergunta gravada; a resposta escolhe-se de 4 opções):

| Pedra | Onde | Enigma | Resposta |
|---|---|---|---|
| 1 | andar 31, no topo do Rochedo do Vigia | "Corro sem pernas, canto sem boca, apago pegadas e acendo fogueiras." | **O vento** |
| 2 | andar 33, debaixo da ponte de pedra mais alta | "Sou branco, venho do mar que não está aqui, e as sanguessugas morrem por minha causa." | **O sal** |
| 3 | andar 34, num telhado da Cidade Enterrada | "Fui pão e agora sou pedra. Fui casa e agora sou duna. O que me engoliu?" | **A torre** |
| 4 | andar 36, no farol do Olho da Tempestade | "Quanto mais escuro está, mais se vê de mim." | **As estrelas** |
| 5 | andar 39, à saída do Poço Real | "Todos me atravessam a subir. Ninguém me atravessa a descer. Tenho cem portas e nenhuma casa." | **A escada** |

   - Resposta errada: a pedra fica muda até ao dia seguinte.
3. **Entregar** — 🎬 a Sahra leva o herói ao **Poço dos Ossos** e toca na pedra da boca com as mãos azuis. O poço abre-se com um suspiro de pó.
   - **Sahra** *(normal)*: "Cinco respostas. Cinco certas. O vento gosta de ti. Lá em baixo, o dragão também vai gostar. Ou vai comer-te. O vento não sabe tudo."

### R4_10 — A Dança do Oásis
| | |
|---|---|
| Quem dá | Layla (Zahra) |
| Recompensa | **Vestes de Dança** (cosmético) · começa o **Festival do Oásis** (1 vez por estação, dia 7) |

1. **Pedir** — **Layla**: "Para o festival preciso de flores e de seda. Flores do Deserto para a coroa da dança. Seda para os lenços. Cinco e três. E preciso de um par para dançar. Tu."
2. **Passo**: entregar **5 Flor do Deserto** (andares 32 e 37, só ao amanhecer) + **3 Seda de Aranha**.
3. **Entregar** — 🎬 na mesma noite, o primeiro Festival do Oásis em 10 anos. Lanternas na lagoa, música, toda a cidade na rua.
   - **Minijogo da dança**: carregar nos botões que aparecem à volta da Layla ao ritmo da música (como o jogo de ritmo da Taberna). Qualquer pontuação conta.
   - **Layla** *(feliz)*: "Pisaste-me duas vezes! Ninguém reparou! Toda a gente reparou! Foi perfeito!"

### R4_11 — A Lâmpada
| | |
|---|---|
| Quem dá | Faisal (Zahra) |
| Recompensa | **um desejo** (escolhe 1): +3 pontos de atributo **ou** 5 000 ouro **ou** uma arma **Épica** de Prata (à escolha do tipo) |

1. **Pedir** — **Faisal**: "Tenho uma lâmpada velha que ninguém compra. Diz a lenda que é a prisão do Djinn da tempestade. Se for verdade, devolve-lha. Se não for, vende-a lá em cima. Ganho de qualquer maneira."
   - ⚙ Recebe a **Lâmpada Velha**.
2. **Passo**: levar a lâmpada ao **Djinn da Tempestade** (andar 36, Olho da Tempestade). Se a tiveres, ele não luta (ver C4-06).
   - 🎬 O Djinn vê a lâmpada e fica quieto.
   - **Djinn** *(surpresa)*: "A minha lâmpada. A minha prisão. Cem anos… não. Muitos mais, lá dentro. Um rei de cima prendeu-me nela por eu soprar onde não devia."
   - **Djinn** *(feliz)*: "Trouxeste-ma. Não a esfregaste. Não me mandaste nada. És o primeiro. Por isso: um desejo. Um. Escolhe bem."
3. **O desejo** (escolha):
   - ▶ **"Quero ficar mais forte."** → +3 pontos de atributo. **Djinn**: "Força. Clássico. Os reis de cima pediam sempre o mesmo."
   - ▶ **"Quero ouro."** → 5 000 ouro. **Djinn**: "Ouro! Toma. É da areia. Não digas a ninguém."
   - ▶ **"Quero uma arma."** → arma Épica de Prata (escolhe o tipo). **Djinn**: "Uma arma do vento. Corta como uma tempestade. Cuida dela."
   - ▶ **"Quero ir para casa."** → **Djinn** *(triste)*: "Esse não. Esse não posso. Ninguém pode, aqui em baixo. Só o de cima. Escolhe outro." *(volta às opções; não gasta o desejo)*
4. 🎬 O Djinn parte a lâmpada na mão e voa para cima, dentro da tempestade, a rir. A tempestade do andar fica 20% mais fraca para sempre.
   - O guardião do andar 36 passa a ser o **Djinn Menor** (Elite) em vez do Djinn; a **Cimitarra do Vento** continua a cair dele.

### R4_12 — O Colosso
Dada pela **Capitã Freya** (rank B; = `G_B_01`). Falas em `docs/dialogos/freya.md`. O Verme Colosso só aparece em **tempestades de areia** nos andares 36 e 37 (10%; 50% com a missão ativa).

### R4_13 — O Escaravelho Dourado
Dada pelo **Zed**. Falas em `docs/dialogos/zed.md`. O escaravelho aparece no **Palmeiral** do andar 32 ao pôr do sol (18:00–19:00), só com tempo limpo; foge se correres.

### R4_14 — Os Banhos de Zahra
| | |
|---|---|
| Quem dá | Encarregado Bilal (Zahra) |
| Recompensa | **Banhos abertos**: tomar banho (50 ouro) dá +10% de regeneração de HP durante um dia |

1. **Pedir** — **Bilal**: "O aqueduto. Canos de prata e pedra nova. Dez lingotes, vinte pedras. E alguém que não se importe de se molhar."
2. **Passo 1**: entregar **10 Lingote de Prata + 20 Pedra**.
3. **Passo 2**: ir ao aqueduto (atrás do palácio, por cima da lagoa) e **rodar 3 comportas** pela ordem (a água tem de chegar à primeira antes de abrires a segunda; vê-se pelo barulho).
4. **Entregar** — 🎬 a água chega aos banhos a fumegar. O Bilal mete os pés. Suspira de felicidade (pela primeira vez, um suspiro feliz).
   - **Bilal** *(feliz)*: "Três anos. Três anos a lavar-me na lagoa com os peixes a olhar. Obrigado. O primeiro banho é teu. De graça. Os outros não."

### R4_15 — Sal para o Pântano
Dada pela **Xamã Ilssa** (andar 24, só com `sssar_defendida`). Levar-lhe **20 Sal** (Salinas do andar 33). Falas em `docs/dialogos/povoacoes_r03.md` (`ilssa_05`).

---

## 6. Missões da Guilda (rank B) da região

Os objetivos e recompensas estão em `docs/MISSOES.md` (secção 3). A G_B_02 (Mamute Ancião) é da região 5.

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_B_01 O Colosso (R4_12) | "PROCURA-SE: Verme Colosso. Aparece nas tempestades de areia dos andares 36 e 37. Engole caravanas inteiras." | "Engole caravanas! Inteiras! Com os camelos e tudo! Não te deixes engolir. Não tenho formulário para isso." | "Escamas de Colosso! Do tamanho de escudos! O Brom vai fazer um escudo. Disse que ia. Disse 'Hmpf'. Vai." |
| G_B_03 Caravana em Perigo | "Uma caravana de Zahra vai atravessar o andar 31. Bandidos à espreita. Escoltar até ao fim." | "Caravanas! Camelos! Ai, gostava tanto de ver um camelo. Traz um desenho. Não, traz um camelo. Não, um desenho." | "Chegou inteira! E o caravaneiro mandou-me isto: um lenço de Zahra! Para mim! Vou usá-lo todos os dias. Até no verão." |
