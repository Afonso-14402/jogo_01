# Irmã Célia — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.9. Dados: `dados/dialogos/celia.json`. Serviços: `docs/LOJAS.md`, secção 2.11.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | baixos e suaves, sem pressa; nunca sobem |
| Como fala | frases calmas e curtas; faz perguntas que obrigam a pensar; quando é firme, fala ainda mais baixo |
| Repete | "Que a luz te acompanhe.", "Deixa-me ver essa ferida.", "Respira." |
| Tiques | toca no cristal do colar quando reza ou pensa (animação `tocar_colar`) |
| Nunca diz | mal de ninguém pelas costas; que sabe o que há no topo |
| Chama ao herói | `{nome}`; "pequen{o/a}" quando está preocupada |
| Quem é | nasceu no **Mosteiro da Ordem da Luz** (andar 77), aluna da Abadessa Lumina. Foi caçadora de mortos-vivos. Há 20 anos **desceu 77 andares a pé** (descer não precisa de Jogador) para cuidar de Ascendia |
| Com a Mia | a Mia dorme na Igreja; a Célia trata dela como de uma sobrinha teimosa (ver `docs/dialogos/mia.md`) |
| Rotina ao Domingo | missa curta às 9:00 (os NPCs que vão aparecem sentados nos bancos); à tarde visita o Bairro Baixo |

---

## 2. Primeira conversa

- **Irmã Célia** *(normal)*: "Bem-vind{o/a} à Igreja da Luz. Não precisas de rezar. Podes só descansar. Os bancos são para isso também."
- **Irmã Célia** *(normal)*: "Se vieres ferid{o/a}, eu trato. Se vieres amaldiçoad{o/a}, eu tiro. Se vieres triste… também há lugar."
- **Irmã Célia** *(feliz)*: "E se vires uma menina com um pau na mão a fingir que é espada, é a Mia. Diz-lhe que o jantar é às sete."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Serviços (bênçãos, curas, Água Benta) · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `celia_dia_01` | `hora entre 6 e 9` | normal | "Acendo as velas todas as manhãs. Uma por cada pessoa que está lá em cima. Hoje acendi mais uma: a tua." |
| `celia_dia_02` | `hora entre 12 e 14` | normal | "Vou visitar os doentes do Bairro Baixo à tarde. Se tiveres poções a mais, eles agradecem." |
| `celia_dia_03` | `hora entre 18 e 20` | normal | "Ao fim do dia a igreja fica cor de laranja. É a minha hora preferida. Senta-te, se quiseres." |
| `celia_dia_04` | — | normal | "A luz não vence a escuridão. Só a faz recuar. Isso chega." |
| `celia_dia_05` | — | normal | "Respira. Toda a gente que entra aqui vem a correr. Ninguém sai a correr. É bom sinal." |
| `celia_dia_06` | — | feliz | "A Mia escondeu-me o lenço outra vez. Diz que foi um 'ladrão de lenços'. O ladrão tem tranças." |
| `celia_dia_07` | — | normal | "Coragem não é não ter medo. É ter medo e voltar à mesma. Tu voltas sempre." |
| `celia_dia_08` | — | normal | "Já perdi a conta às maldições que tirei. Mas lembro-me de todas as pessoas." |
| `celia_dia_09` | `dia_semana == domingo && hora entre 8 e 10` | feliz | "Fica para a missa? É curta. O Brom vem e adormece. O Tobias vem e conta as moedas da caixa." |
| `celia_dia_10` | `dia_semana == sabado` | normal | "Ao sábado lavo os bancos. A Mia ajuda. Bem, a Mia molha-se e eu lavo os bancos." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `celia_dia_20` | `estacao == primavera` | feliz | "Na primavera a sálvia cresce no jardim de trás. É com ela que faço a Água Benta." |
| `celia_dia_21` | `estacao == verao` | normal | "No verão há mais insolações do que maldições. Bebe água. É uma bênção barata." |
| `celia_dia_22` | `estacao == outono` | triste | "No outono os aventureiros sobem mais antes do frio. E nem todos descem. Rezo mais no outono." |
| `celia_dia_23` | `estacao == inverno` | normal | "No inverno a igreja abre de noite para quem não tem lareira. Às vezes enche. Ninguém se queixa do aperto." |
| `celia_dia_24` | `clima == chuva` | normal | "Entra, entra. A chuva lá fora é para as plantas, não para ti." |
| `celia_dia_25` | `clima == trovoada` | feliz | "A Mia tem medo de trovoada. Diz que não. Vem dormir para o banco ao pé de mim. Diz que é para me proteger." |
| `celia_dia_26` | `clima == nevoeiro` | normal | "No mosteiro onde nasci havia sempre névoa. Aqui faz-me sentir em casa. Um bocadinho." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `celia_dia_40` | `andar_maximo < 10` | normal | "A floresta é bonita. Não deixes que a beleza te distraia. Os lobos também são bonitos." |
| `celia_dia_41` | `andar_maximo >= 21` | normal | "O pântano tem venenos que as minhas orações não tiram. Leva antídotos. Deus ajuda quem leva antídotos." |
| `celia_dia_42` | `missao(H_08) == concluida && flag(sssar_defendida)` | feliz | "Defendeste os Homens-Lagarto. A Guilda não gostou. Eu gostei. Às vezes a coisa certa não é a ordem certa." |
| `celia_dia_43` | `missao(H_08) == concluida && flag(sssar_expulsa)` | triste | "Fizeste o que a Guilda mandou. Não te julgo. Mas reza por eles comigo, está bem? Também eram alguém." |
| `celia_dia_44` | `andar_maximo >= 41` | normal | "O frio lá em cima faz esquecer. Repete o nome das pessoas de quem gostas. Em voz alta. Ajuda." |
| `celia_dia_45` | `andar_maximo >= 71` | triste | "Chegaste ao reino dos mortos. Foi lá que nasci. Dá cumprimentos à Abadessa. E não toques na névoa roxa." |
| `celia_dia_46` | `andar_maximo >= 91` | normal | "Ninguém sabe o que há no topo. Eu também não. Mas sei que sobes com mais gente do que pensas. Cá em baixo rezamos todos." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `celia_dia_60` | `coracoes(celia) >= 2` | feliz | "Guardei-te um banco. O terceiro da esquerda. Tem melhor luz." |
| `celia_dia_61` | `coracoes(celia) >= 4` | normal | "Acendo-te sempre duas velas agora. Uma para a subida. Outra para a descida." |
| `celia_dia_62` | `coracoes(celia) >= 6` | feliz | "Falas comigo como se eu fosse só uma pessoa. Não a Irmã. É raro. Obrigada." |
| `celia_dia_63` | `coracoes(celia) >= 8` | normal | "Se um dia precisares de fugir de tudo, a porta das traseiras da igreja nunca está fechada à chave." |
| `celia_dia_64` | `coracoes(celia) >= 10` | feliz | "A luz vai contigo. Não é uma frase bonita. É uma bênção. Está mesmo contigo." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `celia_dia_70` | `origem == ajudante` | feliz | "Estavas a ajudar alguém quando a torre te trouxe. Pergunto-me se essa pessoa ficou bem. Rezo por ela também." |
| `celia_dia_71` | `origem == dormir` | normal | "Foste trazid{o/a} a dormir. Sem despedidas. Isso é uma ferida também. Mesmo que não sangre." |
| `celia_dia_72` | `skill_unica == segunda_vida` | normal | "Segunda Vida. A torre deu-te uma segunda oportunidade. Nem todos a têm. Não a gastes à toa." |
| `celia_dia_73` | `skill_unica == coracao_de_dragao` | feliz | "Curas-te sozinh{o/a}! Vou ficar sem trabalho. Não, não vou. Trazes sempre feridas que nem um dragão curava." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `celia_curta_1` | normal | "Que a luz te acompanhe." |
| `celia_curta_2` | normal | "Precisas de alguma coisa? Estou aqui." |
| `celia_curta_3` | feliz | "Outra vez? A igreja não se cansa de ti. Eu também não." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Irmã Célia** *(normal)*: "A Ordem onde cresci diz que a torre é uma prova. Que os mundos que ela engole são postos à prova."
- **Irmã Célia** *(normal)*: "Eu não sei se é verdade. Sei que as pessoas que vivem lá dentro rezam, comem, discutem e fazem as pazes. Como cá em baixo."
- **Irmã Célia** *(triste)*: "Se é uma prova, então o que se prova é isso. Que continuamos a ser gente."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "A floresta está doente. Sinto-o quando os lenhadores vêm cá. Têm as mãos tristes." |
| 2 Cavernas | "Debaixo da terra há fantasmas que não sabem que morreram. Fala-lhes com calma. Eles ouvem." |
| 3 Pântano | "Leva antídotos. E não julgues os Homens-Lagarto pela cara. Ninguém escolhe a cara." |
| 4 Deserto | "No deserto há múmias. São mortos-vivos antigos. A luz assusta-os. Leva Água Benta." |
| 5 Gelo | "Lá em cima o frio faz esquecer. Escreve os nomes de quem gostas num papel e leva-o contigo." |
| 6 Oceano | "No mar há um navio de fantasmas. Se conseguires, ajuda-os a seguir em frente. É uma boa ação, mesmo para mortos." |
| 7 Vulcão | "Há cultistas que rezam ao fogo. Rezar não é o problema. O problema é o que pedem." |
| 8 Reino Assombrado | "O meu reino. O Mosteiro fica no andar 77. Se vires a Abadessa Lumina, diz-lhe que a Célia está bem. E que come." |
| 9 Céu | "Lá em cima o céu está perto. Mas cuidado: o que cai do céu não é sempre um anjo." |
| 10 Abismo | "Não sei o que há aí. Ninguém sabe. Leva luz. Toda a luz que conseguires." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `celia_rumor_01` | — | "O Rook deixa moedas na caixa das esmolas à noite. Pensa que não sei. A caixa conta-me tudo." |
| `celia_rumor_02` | — | "A Mia quer ser aventureira. Eu não a proíbo. Só lhe digo que espere até ser maior. Ela responde que já é 'compacta'." |
| `celia_rumor_03` | — | "O Mestre Gorvan vem à igreja quando está vazia. Não reza. Senta-se no último banco. Eu deixo-o em paz." |
| `celia_rumor_04` | `andar_maximo >= 15` | "Há aventureiros presos em casulos no ninho das aranhas. A Capitã Freya anda a juntar gente para os ir buscar." |
| `celia_rumor_05` | `andar_maximo >= 38` | "Na porta da pirâmide há um nome raspado. O Fausto diz que é o de alguém que disse 'não' à torre. Que coragem." |
| `celia_rumor_06` | `andar_maximo >= 61` | "No vulcão há cultistas a fazer rituais. Se os acabarem, coisas más acordam. Preciso de ajuda com isso." |
| `celia_rumor_07` | `estacao == inverno` | "No Festival da Estrela a igreja fica cheia de velas. Vem ver. Mesmo que não acredites em nada. As velas não perguntam." |

### 4.4 A vida dela
| Corações | Fala |
|---|---|
| 0 | "Sou a Irmã Célia. Trato de quem chega. Não há muito mais para contar." |
| 2 | "Nasci dentro da torre, num mosteiro no andar 77. Nunca vi o céu de verdade até descer para Ascendia." |
| 4 | "A minha mestra é a Abadessa Lumina. Ensinou-me a rezar, a curar e a lutar. Por essa ordem. Eu aprendi ao contrário." |
| 6 | "Desci setenta e sete andares a pé. Descer não precisa de Jogador: só de pernas e de teimosia. Demorei um ano." |
| 8 | "Antes de ser irmã, fui caçadora de mortos-vivos. Era boa. Boa demais. Um dia percebi que já não via pessoas, só alvos. Desci para aprender a curar." |
| 10 | "Ainda tenho a minha maça de caçadora debaixo do altar. Não lhe toco há vinte anos. Mas sei exatamente onde está." |

---

## 5. Presentes

**Adora:** Velas (qualquer), Cristais de Luz, Sálvia Sagrada · **Gosta:** flores brancas, chá ·
**Detesta:** itens amaldiçoados (Ectoplasma, Rosa Negra, Ossos). O resto é neutro.

| Reação | Falas |
|---|---|
| Adora | "Que presente bonito. Vai ficar no altar. Assim todos o veem, e eu também." · "Obrigada, {nome}. A luz agradece. Eu também." |
| Gosta | "Que gentileza. Vou pô-la numa jarra, ao pé da janela." |
| Neutro | "Obrigada. Tudo tem uso nesta casa." |
| Não gosta | "Agradeço a intenção. A intenção é o que conta, dizem. Neste caso, conta mais." |
| Detesta | "Isto tem uma sombra. Não o tragas para dentro da igreja, por favor. Eu trato dele. Lá fora." |

| Item | Fala |
|---|---|
| Vela Sagrada feita pelo herói | "Fizeste-a tu? A chama é direita. Isso quer dizer que tens a mão calma. Ou que tiveste sorte." |
| Água Benta | "Água Benta para a Irmã! É como levar areia à praia. Mas fico com ela. Nunca sobra." |
| Rosa Negra | "Uma rosa negra. É bonita, eu sei. Mas carrega tristeza de outro alguém. Vou enterrá-la no jardim, com uma oração." |

---

## 6. Aniversário e festivais

**Aniversário (Inverno, dia 2):**
- Sem presente: **Irmã Célia** *(normal)*: "No mosteiro não se festejam anos. Festeja-se o dia. Hoje é um bom dia."
- Com presente que adora: **Irmã Célia** *(feliz)*: "Lembraste-te. Não conto a ninguém o meu dia, e tu lembraste-te. A Mia disse-te, foi? Claro que foi."
- Com outro presente: **Irmã Célia** *(feliz)*: "Obrigada. Hoje vou acender uma vela por ti, além das outras."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Faço as coroas de flores para as crianças. Este ano a Mia quer uma 'com espinhos, para meter medo'." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Uma irmã a dançar… Que diria a Abadessa? Diria 'já não era sem tempo'. Vamos." ⚙ +100 |
| F_02 Festival da Pesca | "Abençoo os barcos de manhã. Os peixes não sei se ficam contentes." |
| F_03 Noite dos Espíritos | "Esta noite os mortos ficam perto. Os bons visitam. Os maus, eu trato deles. Vai à festa descansad{o/a}." |
| F_04 Festival da Estrela | "A igreja enche-se de velas. É a noite de que mais gosto. Ninguém está sozinho no Festival da Estrela." |
| F_05 Dia da Subida | "Rezei por ti a noite toda. Não por te faltar força. Por te sobrar coragem." |
| F_06 Concurso da Casa | "Não julgo casas. Mas se tiveres uma vela à janela, é a minha preferida." |
| F_07 Noite das Lanternas | "Abençoo as lanternas antes de irem para o rio. Uma por uma. Demoro. Sei os nomes de quase todos." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Voltaste inteir{o/a}. Senta-te. Deixa-me ver essa ferida. Pois. Isto foi uma presa." |
| Ent Ancião (10) | "A Árvore-Mãe partiu. Rezei por ela. As árvores também têm alma. As velhas, pelo menos." |
| Aranha-Mãe (15) | "Trouxeste os aventureiros dos casulos? Estão cá, a recuperar. Um deles pergunta por ti de hora a hora." |
| Golem de Cristal (20) | "Uma casa! Vou benzê-la, se deixares. É uma tradição. A água não estraga o chão. Muito." |
| Serpente do Lodo (25) | "O veneno do pântano entranha. Bebe isto. Não perguntes o que é. É amargo porque funciona." |
| Hidra do Pântano (30) | "Cortaste cabeças que voltavam a crescer. Há males assim. Corta-se a raiz, não a cabeça." |
| Escorpião Imperador (35) | "Veneno outra vez. Já guardo o teu antídoto numa prateleira só tua." |
| Faraó Eterno (40) | "Um rei que também foi Jogador… E que nunca descansou. Que a luz lhe dê agora o descanso que a torre não deu." |
| Yeti Ancião (45) | "O Yeti guardava as coisas dos mortos para se lembrar deles. Há mais santidade num monstro do que em muita gente." |
| Dragão de Gelo (50) | "Metade da torre. Acendi cinquenta velas. A Mia apagou duas com o sopro. Diz que era um vento mágico." |
| Capitão Esqueleto (55) | "Os fantasmas do navio seguiram em frente? Então fizeste mais do que vencer. Fizeste-lhes um funeral." |
| Leviatã (60) | "Venceste o mar. O Kai… Acendo uma vela por ele todas as noites. Não digo a ninguém. Digo-te a ti." |
| Ferreiro Infernal (65) | "O Brom veio cá. Sentou-se no último banco. Não disse nada. Fiquei ao lado dele. Chegou." |
| Kai — salvo (68) | "Trouxeste-o de volta. A torre quis quebrar uma amizade e não conseguiu. Isso é um milagre. Dos pequenos." |
| Kai — vencido (68) | "Senta-te aqui. Não precisas de rezar. Eu rezo pelos dois." |
| Titã de Magma (70) | "Interrompeste os rituais? Então o titã dormiu sem ninguém a chamá-lo de volta. Obrigada." |
| Lich Bibliotecário (75) | "Um morto que só queria silêncio para ler. Compreendo-o mais do que gostaria." |
| Rei Sem Coroa (80) | "O rei pediu desculpa? Os reis quase nunca pedem. Os mortos, às vezes. Ainda bem que ouviste." |
| Grifo Real (85) | "A Mia quer uma pena de grifo. Já lhe disse que não. Ela já sabe que vais trazer uma." |
| Serafim Caído (90) | "Um anjo caído disse-te uma verdade pesada. Não a carregues sozinh{o/a}. Pousa um bocado aqui." |
| Guardião do Tempo (95) | "Cinco andares. Só cinco. Vou rezar a cada hora. Não para pedir. Para te fazer companhia." |

> Depois do **Administrador**: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — A canção na igreja vazia

| | |
|---|---|
| ID | `cena_celia_2` |
| Quando | 2 ❤️ · entrar na Igreja entre as 19:00 e as 20:00 |
| Onde | Igreja, vazia, só com as velas |
| Quem | herói, Irmã Célia |
| Música | sem música: só a voz dela (canção `canto_mosteiro`, a capella) |

🎬 A Irmã Célia está sozinha ao pé do altar, de costas, a cantar baixinho numa língua antiga. A luz das velas treme.
🎥 A câmara fica na porta, longe. O herói fica parado.
🎬 Ela acaba. Vira-se. Não se assusta.

- **Irmã Célia** *(normal)*: "Ouviste? Não faz mal. É uma canção do mosteiro onde nasci. Canta-se ao fim do dia para os mortos saberem que é hora de descansar."
- **Irmã Célia** *(triste)*: "Cá em baixo os mortos já descansam sozinhos. Mas eu canto na mesma. É o meu costume. É a minha casa."

▶ **"Canta outra vez?"**
▶ **"Tens saudades de casa?"**

- *(canta)* **Irmã Célia** *(feliz)*: "Uma vez só. Senta-te." 🎬 Canta outra vez; o herói senta-se no banco. ⚙ +30
- *(saudades)* **Irmã Célia** *(normal)*: "Todos os dias. Mas as saudades não são uma ferida. São uma ponte. Lembram-te de onde vens." ⚙ +30

⚙ 5% de desconto nos serviços da Igreja.

### ❤️ 4 — A Ordem da Luz

| | |
|---|---|
| ID | `cena_celia_4` |
| Quando | 4 ❤️ · entrar no jardim de trás da Igreja de manhã (7:00–10:00) |
| Onde | jardim da Igreja, com sálvia e um poço |
| Quem | herói, Irmã Célia |
| Música | `ascendia_dia` (calma) |

🎬 A Célia corta sálvia com uma faca pequena. Cheira-a antes de a pôr no cesto.

- **Irmã Célia** *(normal)*: "No andar 77 há um mosteiro em cima de uma montanha de pedra negra. A Ordem da Luz. Monges que caçam o que não devia estar vivo."
- **Irmã Célia** *(normal)*: "A Abadessa Lumina encontrou-me num cesto à porta. Como eu encontrei a Mia. A torre repete as histórias."
- **Irmã Célia** *(feliz)*: "Ensinou-me a fazer Água Benta. Sálvia, água limpa e uma oração. A oração é o que custa: tem de ser sincera."

▶ **"Ensinas-me?"**
▶ **"Porque é que desceste?"**

- *(ensinas)* **Irmã Célia** *(feliz)*: "Ensino. A oração não ensino: essa é tua." ⚙ receita **Água Benta** (se ainda não a tiveres)
- *(desceste)* **Irmã Célia** *(normal)*: "Porque cá em baixo ninguém sabia curar maldições. E porque lá em cima eu já não sabia parar de lutar. Fica para outro dia." ⚙ +30 e a receita na mesma

⚙ Receita **Água Benta** · receita **Vela Sagrada** (se a missão N_CELIA_1 já estiver feita, recebe 5 Velas Sagradas).

### ❤️ 6 — Rituais Interrompidos

| | |
|---|---|
| ID | `cena_celia_6` |
| Quando | 6 ❤️ · `andar_maximo >= 61` · falar com ela na Igreja |
| Onde | Igreja |
| Quem | herói, Irmã Célia |
| Música | `revelacao` (curta) |

🎬 A Célia está diante de um mapa da torre pregado na parede, com três pregos vermelhos no andar 69.

- **Irmã Célia** *(séria)*: "Os cultistas do vulcão estão a fazer três rituais no andar 69. Se os acabarem, o Titã acorda mais forte. E com ele, outras coisas."
- **Irmã Célia** *(normal)*: "Eu não posso subir lá. Já não tenho a idade, nem a vontade, de lutar. Mas posso dar-te tudo o que sei."
- 🎬 Põe-lhe nas mãos um saco com dez frascos de Água Benta e um terço de contas de cristal.
- **Irmã Célia** *(normal)*: "A água para os círculos. O terço para ti. Quando tiveres medo, conta as contas. São trinta e três. Ao chegar ao fim, já passou."

⚙ Missão **R7_12 Rituais Interrompidos** (secção 9). A Célia aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — A caçadora

| | |
|---|---|
| ID | `cena_celia_8` |
| Quando | 8 ❤️ · `estado(amaldicoado)` **ou** Noite dos Espíritos, à meia-noite, na Praça |
| Onde | Praça da Torre, à noite |
| Quem | herói, Irmã Célia, um Espectro que entrou na cidade |
| Música | `catedral` → silêncio |

🎬 Um **Espectro** (morto-vivo do andar 72) passou pelo cristal e está na Praça. Os aldeões fogem.
🎬 Antes de o herói atacar, a Célia passa por ele a andar. Tem uma maça de ferro na mão, velha, com runas.
🎬 Um golpe. Um só. O espectro desfaz-se em luz.
🎬 A Célia fica parada a olhar para a maça. Depois baixa-a devagar.

- **Irmã Célia** *(triste)*: "Vinte anos sem lhe tocar. E as mãos ainda sabem o caminho."
- **Irmã Célia** *(normal)*: "Fui caçadora, {nome}. A melhor da Ordem. Caçava mortos-vivos noite após noite. Um dia matei um que ainda dizia o nome da filha. E não parei para ouvir."
- **Irmã Célia** *(triste)*: "Foi aí que desci. Para aprender a ouvir antes de bater."

▶ **"Hoje ouviste?"**
▶ **"Salvaste a praça."**

- *(ouviste)* **Irmã Célia** *(feliz)*: "Ouvi. Este já não dizia nada. Só estava perdido. Agora não está." ⚙ +30
- *(salvaste)* **Irmã Célia** *(normal)*: "A praça salvava-se sozinha. Tu estavas aqui. Mas obrigada por me deixares ser eu a fazê-lo."

⚙ 15% de desconto nos serviços. Passa a mandar **cartas** com Água Benta ou Velas Sagradas.

### ❤️ 10 — A Bênção Eterna

| | |
|---|---|
| ID | `cena_celia_10` |
| Quando | 10 ❤️ · `missao(N_CELIA_3) == concluida` · entrar na Igreja ao amanhecer (6:00–7:00) |
| Onde | Igreja, com a luz da manhã a entrar pelos vitrais |
| Quem | herói, Irmã Célia, Mia (a espreitar atrás de um banco) |
| Música | `tema_celia` (órgão suave + voz) |

🎬 A Célia está no altar com a carta da Abadessa aberta. Sorri como nunca sorriu.

- **Irmã Célia** *(feliz)*: "A Abadessa respondeu. Diz que tem orgulho em mim. Vinte anos à espera de ler isto. E foste tu que a trouxeste."
- **Irmã Célia** *(normal)*: "No mosteiro há uma bênção que só se dá uma vez na vida. A uma só pessoa. A Abadessa deu-ma a mim."
- **Irmã Célia** *(normal)*: "Quero dá-la a ti. Ajoelha-te. Não por mim. Pela luz. Ela gosta de cerimónias."
- 🎬 O herói ajoelha-se. A Célia põe-lhe as mãos na cabeça. Os vitrais acendem-se um a um.
- **Irmã Célia** *(sussurro)*: "Que onde fores haja luz. E quando não houver, que sejas tu a levá-la."
- 🎬 Uma luz suave desce sobre o herói (efeito dourado).
- **Mia** *(atrás do banco)*: "Também quero uma!"
- **Irmã Célia** *(feliz)*: "Quando fores maior. E compacta."

⚙ **Bênção Eterna**: +10% de HP máximo para sempre. Título *Abençoad{o/a} pela Luz*.

---

## 9. Missões

### N_CELIA_1 — Velas (0 ❤️)
- **Pedir** — **Irmã Célia**: "As velas estão a acabar. Se me trouxeres dez pedaços de cera, faço velas novas e ensino-te a fazer as sagradas."
- **Passo**: entregar **10 Cera** (Abelha-Gigante, andar 6, ou colmeias da quinta).
- **Entregar** — **Irmã Célia** *(feliz)*: "Cheira a mel. As velas vão cheirar a mel. As pessoas vão rezar com fome." ⚙ receita **Vela Sagrada** · +100

### R7_12 — Rituais Interrompidos (6 ❤️, `andar_maximo >= 61`)
- **Passos**: no andar 69, encontrar os **3 círculos de ritual** (marcados no mapa depois da cena) e interrompê-los: vencer os cultistas que rezam (cada círculo tem 4) e **apagar o círculo com Água Benta** antes de a barra do ritual encher (2 min por círculo).
- **Durante** — **Irmã Célia**: "Conta as contas quando tiveres medo. Trinta e três."
- **Entregar** — **Irmã Célia** *(feliz)*: "Os três? Então o titã vai dormir sozinho. Toma: mais água. Nunca chega." ⚙ Água Benta ×10 · +150

### N_CELIA_3 — Carta à Mestra (8 ❤️, `andar_maximo >= 77`)
- **Pedir** — **Irmã Célia** *(nervosa, raro nela)*: "Escrevi uma carta à Abadessa Lumina. Há vinte anos que não lhe escrevo. Desci sem a avisar. Levas-lha?"
- **Passos**: levar a **Carta da Célia** à Abadessa Lumina (Mosteiro da Ordem da Luz, andar 77; as falas dela estão em `docs/dialogos/povoacoes_r08.md`) · trazer a **Resposta da Abadessa**.
- **Entregar** — 🎬 a Célia lê, sentada no degrau do altar. Põe a carta ao peito.
  - **Irmã Célia** *(feliz, a chorar)*: "Ela diz que sabia. Que soube no dia em que desci. E que esperou que eu lhe escrevesse primeiro. Teimosa. Tão teimosa como eu." ⚙ +200 (❤️❤️)

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `celia_estado_vida` | `vida_pct < 30` | triste | "Deixa-me ver essa ferida. Não, não te mexas. Respira. Pronto. Agora sim." ⚙ cura 20% de graça, 1 vez por dia |
| `celia_estado_maldito` | `estado(amaldicoado)` | normal | "Uma maldição. Senta-te. Isto vai arder um bocadinho. Mais por dentro do que por fora." |
| `celia_estado_cansado` | `estado(cansado)` | normal | "O cansaço também é uma maldição. Esta tira-se com cama." |
| `celia_estado_medo` | `estado(medo)` | normal | "Respira. Conta comigo: um, dois, três. Já está a passar." |
| `celia_morte` | 1.ª vez depois de morrer | triste | "Trouxeram-te para aqui. Acordaste. Isso é tudo o que importa hoje." |
| `celia_comp_mia` | `companheiro(mia)` | triste | "Leva-a e traz-ma. Não te peço mais nada. Traz-ma." |
| `celia_comp_kai` | `companheiro(kai)` | normal | "Kai. Ainda bem que voltaste. Senta-te um minuto. A igreja não morde." |
| `celia_animal` | `animal != nenhum` (1.ª vez) | feliz | "Os animais também podem entrar. Na Ordem havia um gato que assistia à missa. Mais atento do que os monges." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `celia_serv_abrir` | abrir serviços | normal | "Do que precisas? Bênção, cura, água. Não há pressa." |
| `celia_serv_bencao` | comprar uma bênção | normal | "Que a luz caminhe à tua frente. E atrás de ti, para o caso de olhares para trás." |
| `celia_serv_maldicao` | tirar maldição | normal | "Pronto. Saiu. Não pegues em coisas que sussurram." |
| `celia_serv_curar` | curar estados | normal | "Feito. Agora come qualquer coisa. A Dona Marta trata do resto." |
| `celia_serv_redistribuir` | redistribuir atributos | normal | "O ritual devolve-te ao início. Não é recomeçar. É escolher outra vez, sabendo mais." |
| `celia_serv_redistribuir_1` | 1.ª vez (grátis) | feliz | "A primeira vez é de graça. Toda a gente merece uma segunda escolha." |
| `celia_serv_doacao` | donativo de 100 ouro | feliz | "Obrigada. Amanhã há sopa no Bairro Baixo por tua causa." |
| `celia_serv_sem_ouro` | sem ouro | normal | "Não tens? Não faz mal. A cura não te recuso. As bênçãos… essas custam velas. Volta depois." |
| `celia_serv_fechado` | 20:00–6:00 | — | `[Sistema] A Igreja está fechada. A porta das traseiras está entreaberta.` (com 8+ ❤️: a Célia atende na mesma) |
