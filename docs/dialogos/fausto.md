# Velho Fausto — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.10. Dados: `dados/dialogos/fausto.json`. Serviços: `docs/LOJAS.md`, secção 2.12.
Ele escreve o **Bestiário** (`docs/textos/bestiario.md`): a voz das "Notas do Fausto" é a mesma destas falas.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | baixíssimos, lentos, com pausas; os bips param a meio quando ele se distrai |
| Como fala | sussurra; corrige-se a si próprio ("o andar 13… ou 14?"); cita livros que ninguém conhece; entusiasma-se e esquece-se de sussurrar |
| Repete | "Shhh.", "Interessante…", "Onde é que eu ia?", "Tenho um livro sobre isso." |
| Tiques | sobe os óculos para a testa e procura-os (animação `procurar_oculos`) |
| Nunca diz | o nome **Aren** antes da missão R10_10 — não o sabe; chama-lhe "o autor das páginas" ou "o nosso A." |
| Chama ao herói | "jovem" (a toda a gente com menos de 70 anos); `{nome}` quando está emocionado |
| Quem é | 80 anos; neto de um copista; passou a vida a juntar o que se sabe da torre. Nunca subiu além do andar 2 ("as escadas, jovem, as escadas") |
| Rotina | Biblioteca 8:00–22:00 · banco da Praça ao sol (13:00–14:00, a ler) · ao Domingo, banco da Praça a manhã toda |

---

## 2. Primeira conversa

- **Velho Fausto** *(normal)*: "Shhh. Os livros estão a dormir. …Ah, és tu. O dez mil. Já ouvi falar. A cidade não fala de outra coisa. A cidade fala alto."
- **Velho Fausto** *(feliz)*: "Sou o Fausto. Guardo tudo o que se sabe sobre a torre. Que é pouco. Muito pouco. Uma estante. Duas, com boa vontade."
- **Velho Fausto** *(normal)*: "Se encontrares páginas antigas lá em cima, papéis, livros, inscrições… traz-mos. Eu leio. E conto-te."
- **Velho Fausto** *(normal)*: "E os monstros! Conta-me os monstros que venceres. Escrevo-os no Bestiário. Com desenhos. Os desenhos são maus. Os textos são bons."

⚙ Abre o Bestiário no Diário e o menu do Fausto: **Conversar · Perguntar sobre… · Missões · Biblioteca (serviços) · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `fausto_dia_01` | `hora entre 8 e 10` | normal | "Bom dia. Já li dois capítulos e bebi três chás. O dia está a correr bem." |
| `fausto_dia_02` | `hora entre 13 e 14` | feliz | *(no banco da Praça)* "O sol aquece as páginas. As letras ficam mais contentes. Isto não está provado. Ainda." |
| `fausto_dia_03` | `hora entre 20 e 22` | normal | "Quase a fechar. Os livros também precisam de descansar. Eu não. Eu leio na cama." |
| `fausto_dia_04` | — | normal | "Shhh. Os livros estão a dormir." |
| `fausto_dia_05` | — | normal | "Ah, o andar 13! Cristais que cantam. Ou era o 14? Tenho um livro sobre isso. Não sei onde." |
| `fausto_dia_06` | — | feliz | "Sabes quantos livros há nesta biblioteca? Três mil e doze. Sabes quantos li? Três mil e onze. O outro está em anão." |
| `fausto_dia_07` | — | normal | "O conhecimento é como uma escada. Cada degrau mostra-te que a escada é mais alta do que pensavas." |
| `fausto_dia_08` | — | normal | "A Lyra vem cá ler romances às escondidas. Escondida atrás de um livro de mapas. O livro de mapas está ao contrário." |
| `fausto_dia_09` | — | feliz | "O Brom pediu-me um livro de poesia. Disse que era 'para um amigo'. O Brom não tem amigos que leiam. Tem-se a si mesmo." |
| `fausto_dia_10` | `dia_semana == domingo` | feliz | *(no banco da Praça)* "Domingo. Leio ao sol e finjo que não ouço as crianças. As crianças fingem que não me ouvem ressonar." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `fausto_dia_20` | `estacao == primavera` | normal | "Primavera: o pólen entra pela janela e cai nos livros. Espirro em cima de séculos de história." |
| `fausto_dia_21` | `estacao == verao` | normal | "No verão o papel fica mole. Eu também. Abre a janela, jovem. Devagar. Sem vento." |
| `fausto_dia_22` | `estacao == outono` | feliz | "O outono é a estação dos livros. Chove, faz frio, e ninguém tem desculpa para não ler." |
| `fausto_dia_23` | `estacao == inverno` | normal | "Tenho três cachecóis. Um para o pescoço, outro para os joelhos, outro para o livro." |
| `fausto_dia_24` | `clima == chuva` | normal | "Não entres com o guarda-chuva aberto! Os livros têm medo de água. E eu tenho medo dos livros molhados." |
| `fausto_dia_25` | `clima == trovoada` | feliz | "Trovoada! Os antigos achavam que eram os andares de cima a mexer os móveis. Teoria absurda. E bonita." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `fausto_dia_40` | `missao(H_06) != concluida && andar_maximo >= 16` | surpresa | "Fungoides? Gente-cogumelo? Com casas? Com LÍNGUA? Conta-me tudo. Não, espera. Vou buscar papel. Agora conta." |
| `fausto_dia_41` | `missao(H_06) == concluida` | feliz | "Os povos da torre… Escrevi doze páginas numa noite. A minha mão ainda dói. A melhor dor da minha vida." |
| `fausto_dia_42` | `andar_maximo >= 31 && missao(R4_07) != concluida` | normal | "O deserto tem uma pirâmide. As pirâmides têm escritos. Os escritos têm respostas. Traz-me os escritos, jovem." |
| `fausto_dia_43` | `missao(R4_07) == concluida` | triste | "Todos os Administradores foram Jogadores. Todos. Não consigo deixar de pensar nisso. Nem tu, imagino." |
| `fausto_dia_44` | `andar_maximo >= 46 && missao(H_12) == concluida` | triste | "O diário da equipa do Gorvan… A Odília escrevia tão bem. Mapas e poemas no mesmo caderno. Ela tinha olho de bibliotecária." |
| `fausto_dia_45` | `andar_maximo >= 71` | feliz | "O Arquivo Selado do andar 75! Livros de um reino inteiro. Se morrer amanhã, morro a sonhar com essas estantes." |
| `fausto_dia_46` | `missao(H_21) == concluida` | triste | "O Administrador está cansado e procura um sucessor… Então é por isso que vocês chegam. Não é castigo. É um pedido. Isso é pior, de certa forma." |
| `fausto_dia_47` | `andar_maximo >= 91` | normal | "O teu Bestiário já tem mais monstros do que todos os livros da Guilda juntos. Um dia vou publicá-lo. Com os meus desenhos maus." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `fausto_dia_60` | `coracoes(fausto) >= 2` | feliz | "Guardei-te a cadeira boa. A que não range. Não digas aos outros: eles também querem a cadeira boa." |
| `fausto_dia_61` | `coracoes(fausto) >= 4` | normal | "Quando tinha a tua idade, quis subir. As pernas disseram que não. Os livros disseram que sim. Fiquei com os livros." |
| `fausto_dia_62` | `coracoes(fausto) >= 6` | feliz | "Escrevo as tuas aventuras numa caderneta à parte. Não, não é a Lyra que me pede. É a Lyra que me copia." |
| `fausto_dia_63` | `coracoes(fausto) >= 8` | triste | "Às vezes sonho com o topo. Não com o que lá está. Com a vista. Imagina ver tudo de uma vez. Todos os andares." |
| `fausto_dia_64` | `coracoes(fausto) >= 10` | feliz | "És o melhor livro que já li, jovem. E ainda nem acabaste." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `fausto_dia_70` | `origem == jogador` | feliz | "Jogavas jogos de subir torres? No teu mundo há livros de torres que se jogam? Fascinante. Absolutamente perturbador." |
| `fausto_dia_71` | `origem == atrasado` | normal | "Chegas sempre atrasad{o/a} e a correr. Na biblioteca não se corre. Chega atrasad{o/a} devagar." |
| `fausto_dia_72` | `skill_unica == olho_do_sistema` | surpresa | "Vês as fraquezas dos monstros?! Senta-te. Tenho quarenta perguntas. Quarenta e uma." |
| `fausto_dia_73` | `skill_unica == lingua_universal` | feliz | "Falas com monstros! Pergunta-lhes como se chamam a si mesmos. Os nomes que lhes damos são horríveis." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `fausto_curta_1` | normal | "Shhh. …Ah, és tu. Shhh na mesma." |
| `fausto_curta_2` | normal | "Onde é que eu ia? Ah. Na página 312." |
| `fausto_curta_3` | feliz | "Trouxeste mais monstros? Não? Volta quando tiveres monstros." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Velho Fausto** *(normal)*: "A torre é mais velha do que a cidade, do que os livros e do que a memória. As riscas da rocha da base contam mil anos. E param de contar."
- **Velho Fausto** *(normal)*: "Tenho três teorias. Uma: é um castelo de deuses. Duas: é um ser vivo. Três: é um livro, e nós somos as letras."
- **Velho Fausto** *(feliz)*: "A terceira não faz sentido nenhum. É a minha preferida."
- *(depois de R4_07)* **Velho Fausto** *(triste)*: "Agora tenho uma quarta teoria. Que a torre é uma cadeira. E que alguém está sentado nela há muito tempo."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "A floresta caiu do céu há mil anos, dizem os elfos. Tenho um livro élfico. Está em élfico. Ainda não percebi nada. Mas é bonito." |
| 2 Cavernas | "Os anões tinham uma forja no andar 18. Forjavam armas para quem? Ninguém sabe. Ou alguém sabe e não diz." |
| 3 Pântano | "Um povo de serpentes construiu templos no pântano. Se encontrares um ídolo de jade, NÃO O VENDAS. Traz-mo. Por favor." |
| 4 Deserto | "Uma cidade inteira engolida pela areia. Pão de pedra nas mesas. Hieróglifos na pirâmide. O paraíso, jovem." |
| 5 Gelo | "No gelo há gente congelada que ainda pestaneja, dizem. Não acredito. Mas se for verdade, quero saber o que viram." |
| 6 Oceano | "O mar dentro da torre… Dizem que há um navio de fantasmas com um diário de bordo. Os diários de bordo são os melhores livros do mundo." |
| 7 Vulcão | "Os anões do fogo guardam moldes de armas de mil anos. Mil anos! Traz-me um desenho de um molde. Só um." |
| 8 Reino Assombrado | "Há uma biblioteca no andar 75. Guardada por um lich que só quer silêncio. Somos colegas, de certa forma." |
| 9 Céu | "Os Alados dizem que o vento é a respiração dos reis antigos. É uma metáfora. Ou não é. Pergunta-lhes." |
| 10 Abismo | "Não há livros sobre o abismo. Tu és o livro, jovem. Escreve tudo na cabeça e conta-me." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `fausto_rumor_01` | — | "As páginas que trazes da torre têm todas a mesma letra. Uma letra de rapaz. Alguém subiu e escreveu. Quem?" |
| `fausto_rumor_02` | `andar_maximo >= 13` | "Há uma sala no andar 13 que só se vê com luz violeta. Vermelho e azul juntos. Os anões escreveram sobre ela." |
| `fausto_rumor_03` | `andar_maximo >= 21` | "O Ídolo de Jade do pântano vale uma fortuna. O Barão Coaxim quer comprá-lo. Eu quero lê-lo. Escolhe bem." |
| `fausto_rumor_04` | `andar_maximo >= 34` | "A Professora Íris está a escavar no deserto. É a única pessoa viva que lê hieróglifos tão mal como eu." |
| `fausto_rumor_05` | `andar_maximo >= 38` | "Na porta da pirâmide há uma lista de nomes. O último foi raspado à força. Ninguém raspa um nome sem razão." |
| `fausto_rumor_06` | `andar_maximo >= 75` | "O lich do Arquivo guardava cinco livros que ninguém pode ler. Selados. Imagino o que dizem. Imagino demais." |
| `fausto_rumor_07` | `andar_maximo >= 91` | "Há quem diga que no andar 98 há uma Arquivista. Uma bibliotecária da torre. Uma colega! Diz-lhe que lhe mando cumprimentos." |

### 4.4 A vida dele
| Corações | Fala |
|---|---|
| 0 | "Sou o Fausto. Leio. É tudo. É muito." |
| 2 | "O meu avô era copista. Copiava livros à mão para a Guilda. Ensinou-me as letras antes de me ensinar a andar." |
| 4 | "Há cinquenta anos que desenho um mapa da torre. Andar a andar, com o que os aventureiros contam. Tem buracos enormes. Tu tapas-mos." |
| 6 | "Nunca casei. Tive uma noiva, a Amélia. Gostava mais de livros do que eu. Morreu a ler. É a morte que eu quero." |
| 8 | "Sonho ver o topo. Não para governar nada. Só para ver. Um bibliotecário quer sempre ver a última página." |
| 10 | "Escrevi um livro com tudo. Toda a minha vida a juntar o que se sabe. Vou dar-to. Não, não discutas. Os livros são para quem os vai usar." |

---

## 5. Presentes

**Adora:** Página Antiga, livros raros, Ídolo de Jade · **Gosta:** chá, papel · **Detesta:** barulho — correr dentro da
biblioteca dá −10 de amizade (uma vez por dia); presentes "barulhentos" (Sino, Tambor, Concha que Canta) são "detesta".

| Reação | Falas |
|---|---|
| Adora | "Oh. Oh. Oh! Senta-te. Não, eu sento-me. Preciso de me sentar." · "Isto vai para a estante de honra. A estante de honra tem três coisas. Agora quatro." |
| Gosta | "Chá! O melhor presente depois de um livro. E dá para beber enquanto se lê um livro." |
| Neutro | "Obrigado, jovem. Vou… usar como marcador. Uso tudo como marcador." |
| Não gosta | "Hmm. Obrigado. Isto não se lê, pois não? Não. Está bem." |
| Detesta | "Isso faz BARULHO. Leva-o daqui. Devagar. Sem tocar. Shhh." |

| Item | Fala |
|---|---|
| Ídolo de Jade | "Não o vendeste. Não o vendeste! Vou chorar em cima dele. Não, vou chorar ao lado. Jade é poroso." (missão R3_15) |
| Página Antiga | "Mais uma página do nosso 'A.'. Letra apressada, tinta castanha… Vou lê-la mil vezes." |
| Livro do andar 75 | "Um livro do Arquivo Selado! Ainda cheira a pó de mil anos. É o perfume mais caro do mundo." |

---

## 6. Aniversário e festivais

**Aniversário (Outono, dia 4):**
- Sem presente: **Velho Fausto** *(normal)*: "Faço anos? Faço. Oitenta e tal. Perdi a conta no setenta e sete. Era um bom número."
- Com presente que adora: **Velho Fausto** *(feliz)*: "Um presente de anos! E é um livro! A minha festa perfeita: tu, um livro, e silêncio."
- 🎬 Neste dia a Lyra deixa-lhe um bolo à porta da biblioteca com uma vela e uma placa: "SHHH. PARABÉNS."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Prenso as flores do concurso num livro. Daqui a cem anos alguém vai abrir o livro e saber que houve uma festa." |
| F_02 Festival da Pesca | "Não pesco. Mas escrevo o tamanho de todos os peixes num caderno. O Pip mente sempre. O caderno não." |
| F_03 Noite dos Espíritos | "Os fantasmas desta noite são amigáveis. Há um que vem à biblioteca e lê por cima do meu ombro. Lê devagar. Espero por ele." |
| F_04 Festival da Estrela | "Amigo secreto: calhou-me o Kai. O que se dá a um rapaz de outro mundo? Um livro sobre o mundo dele. Não existe. Escrevi um. É curto." |
| F_05 Dia da Subida | "Mais um andar no meu mapa. Mais uma página no livro. Obrigado, jovem. É a festa de que mais gosto: a do conhecimento." |
| F_06 Concurso da Casa | "Se tiveres uma estante, ganhas o meu voto. Não sou juiz. Mas voto na mesma, de coração." |
| F_07 Noite das Lanternas | "Ponho uma lanterna pela Amélia. E escrevo num caderno os nomes de todas as outras. Alguém tem de se lembrar." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Um javali-rei! Os javalis têm reis? Têm monarquia? Que forma de governo tem uma toca? Volta e pergunta." |
| Ent Ancião (10) | "Uma árvore que falava… E disse 'o anterior'. O anterior quê? Escrevi a frase no quadro da biblioteca. Olho para ela todos os dias." |
| Aranha-Mãe (15) | "Desenhei-a pelo que me contaste. Tem nove patas. Não sei desenhar aranhas. Ninguém sabe." |
| Golem de Cristal (20) | "Ajoelhou-se para a janela azul… Os guardas da torre respeitam o Sistema como um rei. Interessante. Assustador. Interessante." |
| Serpente do Lodo (25) | "Guardava um ovo de pedra com uma janela pequenina lá dentro. Uma janela! A torre põe ovos? Não. Não pode ser. Pode?" |
| Hidra do Pântano (30) | "Quantas cabeças? A Lyra quer o número. Eu quero os nomes. Cada cabeça tinha nome? Não? Pena." |
| Escorpião Imperador (35) | "Tinha a marca da janela na carapaça. A torre marca os seus guardas. Como um dono marca o gado. Hmm." |
| Faraó Eterno (40) | "Disse 'Eu também subi'. Um Jogador antigo que ficou rei. E que nunca desceu. Fiquei a noite toda acordado." |
| Yeti Ancião (45) | "Guardava as coisas dos mortos para se lembrar deles. É um bibliotecário, jovem. Um bibliotecário peludo." |
| Dragão de Gelo (50) | "'Os outros vinham com amigos.' Que outros? Antes de vocês? Há registos? Tenho de ler tudo outra vez." |
| Capitão Esqueleto (55) | "O diário de bordo! Trouxeste-o? Os fantasmas tinham números como tu. Jogadores. Tantos." |
| Leviatã (60) | "O Leviatã tinha medo. De ti, ou da janela atrás de ti. Monstros com medo… Isso diz muito sobre quem manda." |
| Ferreiro Infernal (65) | "Uma arma com o número 10 000 forjada antes de chegares. A torre esperava-te. Isto não me deixa dormir." |
| Kai — salvo (68) | "O rapaz voltou. E a janela chamou-lhe 'inimigo'. A janela mente. Vou escrever isso a vermelho." |
| Kai — vencido (68) | "Não te pergunto nada. Mas se um dia quiseres que eu escreva o nome dele num livro, para não se perder, eu escrevo." |
| Titã de Magma (70) | "Os cultistas adoravam-no por ser forte. As pessoas adoram muitas vezes a coisa errada pela razão errada." |
| Lich Bibliotecário (75) | "Um colega. Morto, mas colega. Os livros dele estão salvos? Diz-me que estão salvos." |
| Rei Sem Coroa (80) | "Tentou parar a torre. 'Ninguém pode. Talvez tu.' Escrevi a frase por baixo da outra, a do 'anterior'. As frases estão a conversar." |
| Grifo Real (85) | "Protegia os filhos, como a Aranha-Mãe. A torre repete histórias. As boas histórias também se repetem. É como os livros." |
| Serafim Caído (90) | "O Administrador procura um sucessor… e o nome dele é o que assina as páginas. Jovem. Senta-te. Eu também me vou sentar." |
| Guardião do Tempo (95) | "Disse que te viu passar mil vezes? Mil vezes, e é sempre a primeira. Isso é a definição de ler um livro de que se gosta." |

---

## 8. Cenas de coração

### ❤️ 2 — Adormecido no livro

| | |
|---|---|
| ID | `cena_fausto_2` |
| Quando | 2 ❤️ · entrar na Biblioteca entre as 20:00 e as 22:00 |
| Onde | Biblioteca, mesa grande, uma vela quase gasta |
| Quem | herói, Velho Fausto |
| Música | `ascendia_noite` (só caixa de música) |

🎬 O Fausto dorme com a cara em cima de um livro aberto. Ressona baixinho. Os óculos estão na testa.
🎬 Ao lado, uma chávena de chá frio e um papel com uma lista: "Perguntas para o 10 000".

▶ **(Tapá-lo com o cachecol.)**
▶ **(Ler a lista.)**
▶ **(Acordá-lo.)**

- *(tapar)* 🎬 o herói põe-lhe o cachecol pelos ombros. O Fausto murmura: "…mais cinco minutos, Amélia." ⚙ +30 (no dia seguinte: "Alguém me tapou. Os livros não tapam ninguém. Obrigado.")
- *(ler)* 🎬 a lista: *"1. De que cor é o céu no mundo dele? 2. Há bibliotecas? 3. Ele tem medo? 4. Eu teria."* O Fausto acorda. **Fausto** *(envergonhado)*: "Ah. Isso. São perguntas. Não precisas de responder. A 4 não é pergunta."
- *(acordar)* **Fausto** *(surpresa)*: "Não estava a dormir! Estava a ler com os olhos fechados. É uma técnica avançada."

⚙ 5% de desconto nos serviços da Biblioteca.

### ❤️ 4 — O mapa de cinquenta anos

| | |
|---|---|
| ID | `cena_fausto_4` |
| Quando | 4 ❤️ · entrar na Biblioteca de manhã (8:00–12:00) |
| Onde | sala das traseiras da Biblioteca |
| Quem | herói, Velho Fausto |
| Música | `revelacao` (versão suave) |

🎬 Uma folha enorme pregada na parede, do chão ao teto, com um desenho da torre andar a andar. Muitos andares em branco.
🎬 Há notas pequenas coladas: "Andar 7 — elfos?", "Andar 18 — anões! (diz o Brom)", "Andar 31 — Darian ✝".

- **Velho Fausto** *(normal)*: "Cinquenta anos. Cada aventureiro que volta, eu pergunto: o que viste? E desenho. Tudo o que está aqui é memória de alguém."
- **Velho Fausto** *(triste)*: "Os andares em branco são os que ninguém voltou para contar."
- **Velho Fausto** *(feliz)*: "Mas olha." 🎬 Aponta para os andares que o herói já passou: estão todos desenhados, com letra nova. "Estes, foste tu. Num ano fizeste mais do que cinquenta."

▶ **"Vou encher o mapa todo."**
▶ **"Posso ajudar a desenhar?"**

- *(encher)* **Fausto** *(feliz)*: "Então vou precisar de mais parede. E de mais anos. Despacha-te, jovem." ⚙ +30
- *(desenhar)* **Fausto** *(feliz)*: "Desenhas melhor do que eu? Toda a gente desenha melhor do que eu. Toma. O andar 5 é teu." ⚙ +30

⚙ Recebe uma cópia pequena do mapa (**Mapa do Fausto**, decoração) e os **Mapas antigos** ficam 50% mais baratos.

### ❤️ 6 — Os Hieróglifos

| | |
|---|---|
| ID | `cena_fausto_6` |
| Quando | 6 ❤️ · `missao(R4_07) == concluida` · entrar na Biblioteca |
| Onde | Biblioteca, mesa coberta de papéis e das 6 cópias dos painéis |
| Quem | herói, Velho Fausto, Professora Íris |
| Música | `revelacao` |

> Esta cena é também a cena da história de **H_10 — Os Hieróglifos** (`docs/MISSOES.md`). Com menos de 6 ❤️ acontece
> na mesma, mas sem as últimas falas (marcadas com ★).

🎬 O Fausto e a Professora Íris estão debruçados sobre os papéis. Não dormem há dois dias.

- **Professora Íris** *(cansada)*: "Acabámos. Mais ou menos. Ele traduziu, eu discuti."
- **Velho Fausto** *(normal)*: "Os painéis contam a história de reis que governaram a torre. Chamam-lhes 'os que ficaram sentados'. Ou 'Administradores'."
- **Velho Fausto** *(triste)*: "E este painel, o sexto, diz o que eles eram antes de se sentarem. Este símbolo é a janela azul. Este é uma pessoa. Juntos querem dizer…"
- **Velho Fausto** *(triste)*: "…'Jogador'. Todos os Administradores foram Jogadores. Todos."
- `[Sistema] Página especial obtida: "Os Administradores".`
- ★ **Velho Fausto** *(sussurro)*: "Jovem. Eu sou velho e curioso. Mas se tivesse de escolher entre saber o resto e ver-te descer a salvo… escolhia ver-te descer."
- ★ **Velho Fausto** *(normal)*: "Felizmente não tenho de escolher. Vais trazer-me as duas coisas."

⚙ Missão **H_10** concluída (se ativa). Com 6 ❤️: o Fausto aceita jantar em tua casa.

### ❤️ 8 — A última página

| | |
|---|---|
| ID | `cena_fausto_8` |
| Quando | 8 ❤️ · noite limpa (sem nuvens), banco da Praça, 22:00–23:00 |
| Onde | Praça da Torre, o Fausto sentado a olhar para cima |
| Quem | herói, Velho Fausto |
| Música | `aurora` (versão calma) |

🎬 O Fausto está no banco com a cabeça inclinada para trás, a olhar para a torre que desaparece no escuro.

- **Velho Fausto** *(normal)*: "Sabes o que me custa mais? Não é não poder subir. É saber que o livro tem um fim e eu não o vou ler."
- **Velho Fausto** *(triste)*: "Um bibliotecário vive para a última página. E a minha está lá em cima, no andar 100."
- **Velho Fausto** *(feliz)*: "Mas tu vais lá. E vais voltar. E vais sentar-te neste banco e contar-me. Devagar, que eu escrevo devagar."

▶ **"Prometo."**
▶ **"E se a última página for triste?"**

- *(prometo)* **Fausto** *(feliz)*: "Não prometas. Os Jogadores prometem demasiado. Volta. Basta voltar." ⚙ +30
- *(triste)* **Fausto** *(normal)*: "Então lemos juntos e choramos juntos. As páginas tristes também têm de ser lidas. Senão o livro mente." ⚙ +30

⚙ Passa a mandar **cartas** com Páginas de lore copiadas, chá e "perguntas para o 10 000".

### ❤️ 10 — O Livro de Tudo

| | |
|---|---|
| ID | `cena_fausto_10` |
| Quando | 10 ❤️ · entrar na Biblioteca ao fim da tarde (18:00–20:00) |
| Onde | Biblioteca, mesa grande |
| Quem | herói, Velho Fausto |
| Música | `tema_fausto` (cravo + violoncelo) |

🎬 Em cima da mesa há um livro enorme, encadernado em couro gasto, com as pontas de metal. Tem um laço.

- **Velho Fausto** *(normal)*: "Cinquenta e oito anos. Tudo o que li, tudo o que me contaram, tudo o que desenhei. Está aqui."
- **Velho Fausto** *(feliz)*: "Chamei-lhe 'O Livro de Tudo'. É mentira, claro. Falta muita coisa. Mas 'O Livro de Quase Tudo' não vendia."
- **Velho Fausto** *(normal)*: "É teu. Lá em cima vai servir-te mais do que cá em baixo numa prateleira."

▶ **"É o trabalho da tua vida."**
▶ **"Escreve o resto comigo."**

- *(vida)* **Fausto** *(feliz)*: "Por isso mesmo. O trabalho de uma vida tem de ir para algum lado. Melhor ir contigo do que ficar com o pó."
- *(comigo)* **Fausto** *(surpresa)*: "Contigo? …Então tu sobes e eu escrevo. É a melhor divisão de trabalho de sempre." ⚙ +30

⚙ **O Livro de Tudo**: o Bestiário mostra as fraquezas e os drops de **todos** os monstros, mesmo os que ainda não viste.
⚙ No epílogo, o Fausto publica "A Crónica da Subida" (ou morre feliz numa cadeira, com um livro aberto: ver `docs/HISTORIA.md`, secção 7).

---

## 9. Missões

### R2_08 — A Cor Violeta (`andar_maximo >= 13`)
- **Pedir** — **Fausto**: "Os anões escreveram sobre uma 'sala da cor que não existe' na gruta de cristal. Vermelho e azul juntos, diz o texto. Vai ver?"
- **Passo**: no andar 13, bater ao mesmo tempo num cristal vermelho e num azul → luz **violeta** → aparece a **Sala Violeta** com a Ametista Grande.
- **Entregar** — **Fausto** *(feliz)*: "Violeta! Os anões tinham razão. Os anões têm quase sempre razão. Só não sabem escrever." ⚙ Ametista Grande · página de lore extra · +100

### H_06 — Povos Dentro da Torre (história; a parte do Fausto)
- **Contar ao Fausto** (depois de visitar Mycélia e a Forja Anã):
  - **Fausto** *(surpresa)*: "Gente. Gente a viver lá dentro. Com casas, com mortos, com festas. A torre não é um castelo vazio. É um país."
  - **Fausto** *(normal)*: "Vou escrever isto. Hoje. Agora. Vai-te embora, jovem, que tenho de escrever."
  - `[Sistema] Página especial obtida: "Os Povos da Torre".`

### R3_15 — O Ídolo de Jade
- **Passo**: entregar o **Ídolo de Jade** ao Fausto em vez de o vender ao Barão Coaxim (escolha).
- **Entregar** — **Fausto** *(feliz, a chorar)*: "Tem escrita na base. Um povo de serpentes. Com poesia. Serpentes com poesia, jovem!" ⚙ página extra "O Povo-Serpente" · +150

### R4_07 — Os Hieróglifos (história, com a Professora Íris)
- **Passo**: copiar os **6 painéis** do andar 39 (interagir com cada um: minijogo de decalque) e trazê-los.
- **Entregar** — ver a **cena de 6 ❤️** acima (é a mesma). ⚙ página especial "Os Administradores" · 2 000 ouro

### R8_10 — Livros Perdidos (`andar_maximo >= 75`)
- **Pedir** — **Fausto**: "O Arquivo Selado do andar 75. Cinco livros. O lich guarda-os. Se ainda estiverem inteiros… traz-mos. Por favor. Com as duas mãos."
- **Passo**: trazer os **5 Livros Selados** do Arquivo (andar 75).
- **Entregar** — **Fausto** *(feliz)*: "'O Reino Antes da Torre'. Um reino que existia antes de ser engolido. Com reis, festas e impostos. Os impostos são iguais em todo o lado." ⚙ página especial "O Reino Antes da Torre" · +200

### R10_05 — Ecos de Casa (`andar_maximo >= 94`)
- **Pedir** — **Fausto** *(normal)*: "No andar 94 há pedaços de todos os mundos. Ecos. Traz-me um eco de cada região. Dez. Quero escrever a tua história inteira."
- **Passo**: trazer **10 Fragmentos de Eco**, um de cada região.
- **Entregar** — **Fausto** *(feliz)*: "Vou escrever 'A Crónica da Subida'. A tua. Do prado ao topo." ⚙ o livro **A Crónica da Subida** aparece em tua casa (conta a tua aventura com os teus feitos) · +200

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `fausto_estado_correr` | correr dentro da Biblioteca | zangado | "NÃO SE CORRE NA BIBLIOTECA. …Shhh. Desculpa. Não se corre na biblioteca." ⚙ −10 (1 vez por dia) |
| `fausto_estado_vida` | `vida_pct < 30` | surpresa | "Estás a pingar sangue no tapete persa! Vai à Igreja! O tapete não é persa. Vai na mesma." |
| `fausto_estado_maldito` | `estado(amaldicoado)` | normal | "Uma maldição! Posso ver? Só ver. De longe. Tenho um livro sobre… não. Vai à Célia." |
| `fausto_estado_cansado` | `estado(cansado)` | normal | "Tens olheiras de quem leu a noite toda. Respeito. Mas dorme." |
| `fausto_pagina_nova` | trazer uma página do diário pela 1.ª vez esta semana | feliz | "Uma página! Deixa-me ler. …'Os cristais cantam quando lhes toco.' Ele escrevia como quem fala sozinho. Gosto dele." |
| `fausto_pagina_azul` | trazer a 1.ª página de tinta azul (53) | surpresa | "Esta tinta… é azul. Todas as outras são castanhas. E brilha. Jovem, isto não foi escrito na mesma altura." |
| `fausto_comp_kai` | `companheiro(kai)` | feliz | "O rapaz do outro mundo! Diz-me: como é uma biblioteca no teu mundo? Têm livros que falam? Que horror. Que maravilha." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `fausto_serv_abrir` | abrir serviços | normal | "Biblioteca. O que procuras? Monstros, mapas, receitas ou silêncio?" |
| `fausto_serv_bestiario` | completar uma página do Bestiário | feliz | "Pronto. Escrevi as fraquezas e o que deixa cair. Desenhei também. Não olhes para o desenho." |
| `fausto_serv_mapa` | comprar um mapa antigo | normal | "Este mapa tem setenta anos. Os segredos não mudam de sítio. As pessoas é que se esquecem deles." |
| `fausto_serv_livro` | comprar um livro de receitas | feliz | "Leva. Mas devolve com nódoas de comida. Um livro de receitas sem nódoas é um livro que ninguém usou." |
| `fausto_serv_vender_livro` | vender um livro | feliz | "Um livro novo para a coleção! Pago bem. Pago com prazer." |
| `fausto_serv_fechado` | 22:00–8:00 | — | `[Sistema] A Biblioteca está fechada. Ouve-se alguém a virar páginas lá dentro.` |
