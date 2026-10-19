# Selene — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.4. Dados: `dados/dialogos/selene.json`.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios, com eco "mágico" (ver `docs/AUDIO.md`); nas falas marcadas *(depressa)* o texto aparece ao dobro da velocidade |
| Como fala | depressa e aos saltos; pensa em voz alta ("Hipótese: … Conclusão: …"); faz perguntas e responde ela própria; esquece-se do que estava a dizer a meio |
| Repete | "Fascinante!", "Hipótese:", "Não toques nisso!", "Era para fazer bum? Era para fazer bum.", "Pelas raízes!" |
| Tiques | baixa os óculos de proteção da testa para os olhos antes de uma explosão (animação `oculos_baixo`); tira o lápis do cabelo para escrever e o cabelo cai-lhe todo |
| Nunca diz | "impossível" (diz "ainda não"); nada de mau sobre Folhalta ou a Anciã Lothiel; não tem ódio à torre, só curiosidade |
| Chama ao herói | "jovem" (tem 300 anos) ou `{nome}`; com 4+ ❤️ às vezes "a minha cobaia favorita" (em alquimia é um elogio) |
| Rotina ao Domingo | a Alquimia está fechada; de manhã anda pelas Quintas e pela margem do Rio a apanhar ervas; à tarde está na Biblioteca até o Velho Fausto a pôr na rua |

---

## 2. Primeira conversa

Depois da cena P6 (prólogo), a 1.ª vez que carregas em **Conversar**:

- **Selene** *(surpresa)*: "Não toques nisso! …Ah. Não tocaste. Desculpa, é o que digo a toda a gente que entra."
- **Selene** *(feliz)*: "Um Jogador novo! O dez mil, não é? Ouvi a Lyra gritar daqui. Os frascos tremeram todos."
- **Selene** *(normal)*: "Sou a Selene. Faço poções, antídotos, bombas e, às vezes, buracos na parede. Os buracos não estão à venda."
- **Selene** *(normal)*: "Poção de Vida para a vida. Antídoto para o veneno. Ligadura para o sangue. Decora isto e vives mais."
- **Selene** *(feliz, depressa)*: "E se encontrares ervas esquisitas lá em cima, traz-mas! Quanto mais esquisitas, melhor! Pago bem! Às vezes em ouro!"

⚙ Abre o menu de serviços da Selene: **Loja · Receitas · Perguntar sobre… · Missões · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `selene_dia_01` | `hora entre 9 e 11` | feliz | "Bom dia! Já explodi duas coisas e ainda nem tomei o pequeno-almoço. Dia produtivo!" |
| `selene_dia_02` | `hora entre 9 e 11` | normal | "Cheguei às nove. A porta estava no sítio? Ótimo. Ontem não estava." |
| `selene_dia_03` | `hora entre 12 e 14` | surpresa | "Almoço? Ah. Almoço! Sabia que me estava a esquecer de alguma coisa. Há três dias." |
| `selene_dia_04` | `hora entre 15 e 18` | normal | "A esta hora o caldeirão está no ponto. Não sei de quê. Ainda estou a descobrir." |
| `selene_dia_05` | `hora entre 18 e 20` | normal | "Shhh! Estamos na biblioteca. …Shhh! Fui eu. Desculpa. Estou a falar comigo." |
| `selene_dia_06` | `hora entre 20 e 23` | normal | "À noite as poções brilham mais. Ou sou eu que tenho sono. Hipótese a testar." |
| `selene_dia_07` | — | surpresa | "Não toques nisso! …Ou toca, para ver o que acontece. Não, não toques." |
| `selene_dia_08` | — | feliz | "BUM! Ah. Era para fazer bum? Era para fazer bum." |
| `selene_dia_09` | — | normal | "Porque é que as Poções de Vida são vermelhas? Há cem anos que pergunto. Ninguém sabe. Nem elas." |
| `selene_dia_10` | — | feliz | "O Gizmo diz que a alquimia é 'química com chapéu'. Eu digo que as engenhocas dele são magia com parafusos. Somos muito amigos." |
| `selene_dia_11` | — | normal | "Hipótese: Erva Verde mais Erva Verde dá duas Ervas Verdes. Conclusão: preciso de dormir." |
| `selene_dia_12` | — | feliz | "O Brom diz que um dia rebento com a rua toda. Exagerado. Só metade da rua." |
| `selene_dia_13` | `dia_semana == segunda` | surpresa | "Segunda é dia de arrumar o laboratório. Encontrei uma poção de há quarenta anos. Está a olhar para mim." |
| `selene_dia_14` | `dia_semana == sexta` | normal | "À sexta o Fausto fecha a biblioteca mais cedo para ouvir o Lucien. Diz que é 'para estudar a rima'." |
| `selene_dia_15` | `dia_semana == domingo` | feliz | "Domingo! Sem loja! Só ervas, rio e silêncio. E uma explosão pequenina. Pequenina!" |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `selene_dia_20` | `estacao == primavera` | surpresa | "Primavera! Está a crescer uma flor dentro do caldeirão. Não sei como. Não lhe toco. Ela que decida." |
| `selene_dia_21` | `estacao == primavera && hora entre 9 e 12` | normal | "O pólen muda a cor das poções. Hoje as Poções de Vida estão cor-de-rosa. Funcionam na mesma. Acho." |
| `selene_dia_22` | `estacao == verao` | normal | "Com este calor as poções fervem sozinhas. Poupo lenha. Perco sobrancelhas." |
| `selene_dia_23` | `estacao == verao && hora entre 20 e 23` | triste | "Os vaga-lumes do verão… Em Folhalta também os há. Apanho um para a janela. Depois solto-o." |
| `selene_dia_24` | `estacao == outono` | feliz | "Outono: época de cogumelos! Os bons, os maus e os que falam. Todos!" |
| `selene_dia_25` | `estacao == outono && clima == nevoeiro` | normal | "Nevoeiro é o melhor tempo para Cogumelos Luminosos. Brilham mais quando ninguém os vê." |
| `selene_dia_26` | `estacao == inverno` | normal | "No inverno as ervas dormem. Eu não. Estudo. E bebo chá. E estudo o chá." |
| `selene_dia_27` | `estacao == inverno && clima == neve` | feliz | "Cada floco de neve tem seis pontas. Contei. Contei muitos. Tenho os dedos gelados e uma teoria nova." |
| `selene_dia_28` | `clima == chuva` | feliz | "Água Limpa grátis a cair do céu! Pus os frascos todos lá fora. Agora não tenho frascos cá dentro." |
| `selene_dia_29` | `clima == trovoada` | surpresa | "Um raio a sério! Se o apanhasse num frasco… Não. Não vou subir ao telhado. Outra vez." |
| `selene_dia_30` | `clima == nevoeiro` | normal | "Este nevoeiro cheira a erva-doce. Interessante. Ou é o meu laboratório. Deve ser o meu laboratório." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `selene_dia_40` | `andar_maximo < 5` | normal | "Primeiros andares? Leva Antídotos. Os cogumelos do andar 4 cospem coisas. Coisas verdes." |
| `selene_dia_41` | `andar_maximo >= 5 && andar_maximo < 7` | triste | "No andar 7 há árvores enormes. Se lá chegares, cumprimenta-as por mim. As árvores. Ou… ninguém. Esquece." |
| `selene_dia_42` | `andar_maximo >= 7` | surpresa | "Viste Folhalta! As pontes de corda ainda balançam? Não, não me contes. …Conta. Devagar." |
| `selene_dia_43` | `boss_derrotado(ent_anciao)` | triste | "A Árvore-Mãe morreu. Lá em cima contavam histórias dela. Hipótese: a torre bebe-a. Não gosto desta hipótese." |
| `selene_dia_44` | `andar_maximo >= 16` | feliz | "Os Fungoides dizem que a torre é viva! Digo isso há cem anos! Finalmente alguém concorda. São cogumelos, mas concordam." |
| `selene_dia_45` | `andar_maximo >= 21` | normal | "Pântano: o paraíso dos ingredientes. E dos mosquitos. Traz-me lírios. Não me tragas mosquitos." |
| `selene_dia_46` | `andar_maximo >= 41` | surpresa | "Lá em cima há auroras? Luzes no céu? Dentro da torre? Conta-me tudo. As cores. A ordem das cores." |
| `selene_dia_47` | `andar_maximo >= 61` | normal | "Vulcão: leva Poções Frescas. Muitas. Eu levava-as todas, mas tu tens mais mochila. E mais coragem." |
| `selene_dia_48` | `andar_maximo >= 81` | triste | "Ilhas no céu… Mas é céu a sério? Ou é teto pintado, como em Folhalta? Repara bem. Por mim." |
| `selene_dia_49` | `andar_maximo >= 91` | surpresa | "Lótus Estelar, Areia do Tempo… coisas que nem estão nos livros. Escreve tudo. Desenha. Cheira. Não comas." |
| `selene_dia_50` | `andar_maximo >= 2 && missao(R1_13) != concluida` | feliz | "Há uma menina no acampamento dos lenhadores que quer ser alquimista? Com catorze anos? Eu comecei aos duzentos!" |
| `selene_dia_51` | `missao(R1_13) == concluida` | surpresa | "A Tina lê as instruções ANTES de começar. Antes! Nada explode. É assustador." |
| `selene_dia_52` | `missao(R1_13) == concluida` | feliz | "A Tina pôs etiquetas em todos os frascos. Agora sei o que tenho. Tenho coisas muito perigosas." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `selene_dia_60` | `coracoes(selene) >= 2` | feliz | "Guardei-te um frasco da poção nova. Não sei o que faz. Por isso é que é para ti." |
| `selene_dia_61` | `coracoes(selene) >= 3` | normal | "Já não me assusto quando entras. Antes assustava-me e explodia qualquer coisa. Progresso!" |
| `selene_dia_62` | `coracoes(selene) >= 4` | feliz | "A minha cobaia favorita! Em alquimia, isto é o maior elogio que há. Juro." |
| `selene_dia_63` | `coracoes(selene) >= 5` | normal | "Escrevi o teu nome no caderno, na coluna 'coisas que correram bem'. Estás sozinh{o/a} nessa coluna." |
| `selene_dia_64` | `coracoes(selene) >= 6` | triste | "Conto-te coisas que nunca contei ao Eldrin. Ele é o meu irmão. Tu és… a minha testemunha." |
| `selene_dia_65` | `coracoes(selene) >= 8` | feliz | "Cem anos em Ascendia e nunca tive ninguém para ver as estrelas comigo. Agora tenho. Isso não se mede. Tentei." |
| `selene_dia_66` | `coracoes(selene) >= 10` | feliz | "Trezentos anos a estudar o mundo e a melhor descoberta foi uma pessoa. Não escrevas isso. Está bem, escreve." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `selene_dia_70` | `origem == jogador` | surpresa | "No teu mundo havia jogos onde se fazem poções? E explodiam? Não? Que jogos tão aborrecidos." |
| `selene_dia_71` | `origem == atrasado` | normal | "Chegas sempre a correr. As poções também não gostam de pressa. Espera… essa gosta. Bebe." |
| `selene_dia_72` | `origem == ajudante` | feliz | "Tens cara de quem segura frascos sem os deixar cair. Muito raro. Quase um ingrediente." |
| `selene_dia_73` | `origem == dormir` | normal | "Tens cara de sono. Tenho uma poção para isso. Ainda não a testei. Queres testar?" |
| `selene_dia_74` | `skill_unica == aprendiz_rapido` | feliz | "Aprendes depressa? Então decora: 'Não toques nisso.' Pronto. Já sabes o mais importante." |
| `selene_dia_75` | `skill_unica == coracao_de_dragao` | surpresa | "Curas-te sozinh{o/a}? Dás-me uma gota de sangue? Uma gotinha, para a ciência. Não? Está bem." |
| `selene_dia_76` | `skill_unica == lingua_universal` | feliz | "Falas com monstros! Pergunta aos slimes de que são feitos por dentro. Tentei abrir um e ele ofendeu-se." |
| `selene_dia_77` | `skill_unica == olho_do_sistema` | normal | "Vês os números de tudo? Quanto cura esta poção? …Era o que eu tinha calculado! Ou não. Não me digas." |
| `selene_dia_78` | `skill_unica == sorte_do_heroi` | normal | "A alquimia não acredita em sorte. Mas fica ao pé do caldeirão enquanto eu mexo. Por via das dúvidas." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `selene_curta_1` | surpresa | "Não toques nisso! Ah, és tu. Toca. Não, não toques." |
| `selene_curta_2` | normal | "Hmm? Estava a contar gotas. Perdi a conta. Começo outra vez." |
| `selene_curta_3` | feliz | "Voltaste! Ainda não explodiu nada desde que saíste. Estou orgulhosa." |
| `selene_curta_4` | normal | "Agora não, que está a ferver. Tudo. Está tudo a ferver." |

---

## 4. Perguntar sobre…

### 4.1 A torre

A Selene tem **teorias**, nunca a verdade (ver `docs/HISTORIA.md`, secção 1).

- **Selene** *(feliz, depressa)*: "A torre? A minha teoria é que é viva! Respira! Medi: as paredes do andar 1 aquecem de manhã e arrefecem à noite. Como uma barriga!"
- **Selene** *(normal)*: "Engole mundos e cresce. Cada andar é um anel, como nos troncos das árvores. Hipótese: é uma árvore gigante feita de pedra."
- **Selene** *(normal)*: "O Fausto diz que é uma construção. O Gizmo diz que é uma máquina. Eu digo que é alguém. Espero que não seja o Gizmo a ter razão."
- **Selene** *(triste)*: "Se é alguém… o que é que quer? Ninguém come mundos por gosto. Nem a torre. Acho eu."

### 4.2 O andar atual

A Selene fala da **região do andar mais alto** a que chegaste: que poções levar e que ingredientes trazer.

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta: Erva Verde, Flor de Mel, Cogumelos Luminosos… E Folhalta, no 7. É bonita. Leva Antídotos para o 4." |
| 2 Cavernas | "Cavernas: fungos que brilham! Traz-me Musgo Luminoso e faço-te Visão Noturna. Vais precisar. Muito." |
| 3 Pântano | "Pântano: veneno no ar, na água, nas plantas. Bebe a Poção Purificadora antes de entrar. Não depois de cair." |
| 4 Deserto | "Deserto: sol que queima e areia que cega. Colírio, muito Colírio. E água. A água não sou eu que faço, mas recomendo." |
| 5 Gelo | "Gelo: Poção Quente de manhã, à tarde e à noite. E se vires uma aurora, apanha uma Lágrima. Para mim. Por favor." |
| 6 Oceano | "Oceano: Poção de Respirar! Sem ela, os andares de água são muito curtos. Muito curtos e muito finais." |
| 7 Vulcão | "Vulcão: Poção Fresca, Poção Ignífuga. Se encontrares uma Pena de Fénix, não a gastes. Traz-ma. Está bem, gasta. Depois traz." |
| 8 Reino Assombrado | "Reino Assombrado: Água Benta e Bombas de Luz. Os mortos não gostam de luz. Nem de alquimistas." |
| 9 Céu | "Céu: Poção de Leveza para as quedas. E repara no céu. É céu de verdade? Diz-me. É importante." |
| 10 Abismo | "Abismo: ingredientes que mais ninguém viu. Tu és os meus olhos lá em cima. E o meu nariz." |

### 4.3 Rumores

A Selene diz **1 rumor por dia**. Os dela são sobre ingredientes raros, receitas e segredos da torre.

| ID | Condição | Rumor |
|---|---|---|
| `selene_rumor_01` | — | "Dizem que o Fausto tem um livro que se lê sozinho à noite. Fui ver. Era o Fausto a ressonar com o livro na cara." |
| `selene_rumor_02` | — | "O Brom canta na forja. Toda a gente sabe. Eu medi: canta em ré. Desafinado em ré." |
| `selene_rumor_03` | `andar_maximo >= 4` | "No andar 4 há um círculo de cogumelos onde as fadas dançam. O pó delas é dourado. DOURADO. Para a ciência, traz." |
| `selene_rumor_04` | `andar_maximo >= 5` | "No andar 5 há uma toca onde só cabe um coelho pequeno. O que há lá dentro? Ninguém sabe. Ainda. Ainda!" |
| `selene_rumor_05` | `andar_maximo >= 7` | "Em Folhalta há um Poço da Lua. Em noite de lua cheia mostra caminhos escondidos. A Lothiel diz que os poços sabem coisas." |
| `selene_rumor_06` | `andar_maximo >= 7` | "A Mira, da loja de Folhalta, vende Linho Fino. Diz-lhe que vais da minha parte. Ela vai fazer uma cara. Faz parte." |
| `selene_rumor_07` | `andar_maximo >= 16` | "O Mestre Lamela, em Mycélia, sabe receitas de cogumelos que eu nunca vi. Nunca! Diz-lhe que tenho inveja. Saudável." |
| `selene_rumor_08` | `andar_maximo >= 16` | "Os Fungoides pagam com Cogumelos Luminosos. Dinheiro que brilha no escuro! Nunca mais perdes as moedas." |
| `selene_rumor_09` | `andar_maximo >= 26` | "Na Vila Coaxa há um sapo, o Doutor Girino, que faz Poções Surpresa. Bebi uma. Falei ao contrário dois dias. Recomendo!" |
| `selene_rumor_10` | `andar_maximo >= 31` | "Areia Mágica: mexe-se sozinha dentro do frasco. Dei-lhe um nome: Areia. É uma areia muito tímida." |
| `selene_rumor_11` | `andar_maximo >= 41` | "Lágrimas de Aurora só aparecem quando há aurora. Dizem que são o céu a chorar. Eu acho que é condensação. Bonita." |
| `selene_rumor_12` | `andar_maximo >= 61` | "Dizem que no andar 66 há um ninho de fénix no cimo de uma rocha. Com uma pena que te traz de volta da morte. Uma PENA!" |
| `selene_rumor_13` | `andar_maximo >= 71` | "No Reino fazem Água Benta com Sálvia Sagrada. Eu tentei com salsa. Não é a mesma coisa. Não é." |
| `selene_rumor_14` | `andar_maximo >= 81` | "No céu cresce a Flor-do-Vento. Quem a cheira fica mais leve. Se tens medo de alturas, não a cheires." |
| `selene_rumor_15` | `andar_maximo >= 91` | "Dizem que no Abismo há flores feitas de estrelas. Se uma Lótus Estelar não é um ingrediente, nada é." |
| `selene_rumor_16` | `estacao == primavera` | "Na Festa das Flores ganha sempre uma flor da Hana. Este ano concorro com uma flor que eu fiz. Tem dentes. Conta?" |
| `selene_rumor_17` | `missao(R1_13) == concluida` | "A Tina escreve ao pai todas as semanas. O Bruno responde com desenhos de machados. Ela chora a ler. É o pólen." |
| `selene_rumor_18` | `missao(R1_07) == concluida` | "O Eldrin escreve-me que o Faelan sorriu. Uma vez. A aldeia inteira parou para ver. Durou um segundo." |

### 4.4 A vida dela

| Corações | Fala |
|---|---|
| 0 | "Eu? Sou alquimista. Explodo coisas. Às vezes de propósito. Mais nada. Bem, há mais. Mas depois." |
| 2 | "Nasci em **Folhalta**, no andar 7. Dentro da torre. A floresta dos elfos caiu lá dentro há mil anos. Eu nasci muito depois." |
| 4 | "Desci para Ascendia há cem anos, para estudar alquimia com os humanos. Os anciãos não queriam. Elfos não descem. Eu desci." |
| 6 | "Tenho um irmão mais novo, o **Eldrin**. Ficou lá. Quando eu desci, ele correu atrás do cesto a gritar o meu nome." |
| 8 | "Nunca vi um céu verdadeiro. Em Folhalta o céu é um teto. Aqui há céu, mas a torre está sempre a meio dele." |
| 10 | "Trezentos anos e ainda não sei o que é a torre. Mas já sei o que eu sou: alguém que fica. Por agora. Até ver o céu." |

---

## 5. Presentes

**Adora:** Cogumelo Luminoso, ervas raras, Lágrima de Aurora · **Gosta:** cogumelos, flores estranhas ·
**Detesta:** coisas "normais" (pão, pedra). O resto é **neutro** (ver `docs/ITENS.md`, secção dos presentes).

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "PARA MIM?! Isto é… Pelas raízes! Sabes o que isto faz? Eu também não! Vou descobrir! Obrigada, obrigada!" · "Fascinante. Fascinante! Vou pôr num frasco. Não, em dois frascos. Não, vou olhar para isto o dia todo." |
| Gosta | "Oh, que estranho! Gosto de coisas estranhas. Obrigada, {nome}." · "Isto vai para a prateleira das coisas interessantes. Está quase cheia. De coisas tuas." |
| Neutro | "Obrigada! Vou… descobrir para que serve." · "Hmm. Não explode? Não muda de cor? Está bem. Obrigada na mesma." |
| Não gosta | "Ah. Isto é muito… quieto. Obrigada pela intenção." |
| Detesta | "Pão. Pão normal. Feito de farinha. Que tristeza tão grande." · "Uma pedra. Uma pedra normal. Nem brilha. Porque é que ela não brilha?" |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Cogumelo Luminoso | "Um Cogumelo Luminoso! Em Folhalta usávamo-los como candeeiros. Aqui uso-os como tudo. Obrigada!" |
| Lágrima de Aurora | "Uma Lágrima de Aurora… Isto veio de um céu com luzes. Está fria. É o céu, não é? Um bocadinho de céu." |
| Morango Silvestre | "Morangos de Folhalta! Sabem a casa. A casa e a terra. Mais a casa." |
| Pó de Fada | "Pó de Fada! Não o dês ao Gizmo, ele desmaia. A mim podes dar quanto quiseres." |
| Pão Fantasma | "Pão que atravessa paredes? Isto não é pão normal. Isto é pão EXTRAORDINÁRIO. Retiro tudo o que disse sobre pão." |
| Folha Dourada | "Uma folha da árvore nova da Praça… da semente da Árvore-Mãe. Vou guardá-la no livro das coisas que não se usam." |
| Pena de Fénix | "Uma Pena de Fénix. Para mim. Uma coisa que traz gente de volta. …Guardo-a. Mas se precisares, vens buscá-la. Promete." |

---

## 6. Aniversário e festivais

**Aniversário (Primavera, dia 18):**
- Sem presente: **Selene** *(feliz)*: "Hoje faço trezentos e… Não. Perdi a conta aos cento e cinquenta. Faço anos. Isso é certo."
- Com presente que adora: **Selene** *(feliz, depressa)*: "Lembraste-te! Em Folhalta faziam-me uma coroa de folhas. Tu trouxeste-me isto. É melhor. Não digas ao Eldrin."
- Com outro presente: **Selene** *(feliz)*: "Um presente de anos! Vou abrir com cuidado. Às vezes os meus presentes explodem. Os teus nunca."
- Na Alquimia há um bolo com velas a mais: 🎬 se falares com a Tina nesse dia (depois de R1_13), ela diz "Contei as velas. São sessenta. Ela disse que chegava."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Concurso de flores! Este ano levo uma flor que fiz eu. Tem dentes. O júri vai ficar de boca aberta. Espero que não demasiado perto." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Selene** *(surpresa)*: "Os elfos dançam em círculo à volta das árvores. Aqui há uma fonte. Serve!" ⚙ dança · +100 amizade |
| F_02 Festival da Pesca | "Não pesco. Mas estudo as escamas de todos os peixes do concurso. O Pip chama-me 'a senhora das escamas'." |
| F_03 Noite dos Espíritos | "Os fantasmas amigáveis aparecem esta noite! Pergunto-lhes sempre de que são feitos. Nenhum sabe. Nem eles." |
| F_04 Festival da Estrela | "Amigo secreto! Calhou-me o Brom. Vou dar-lhe uma flor. De ferro. Fiz com o Gizmo. Não explodiu. Quase." |
| F_05 Dia da Subida | "Fiz o fogo de artifício para a festa! O verde não era para ser verde. Mas ficou bonito, não ficou?" |
| F_06 Concurso da Casa | "Põe um caldeirão na sala. Dá ambiente. E cheiro. Sobretudo cheiro." |
| F_07 Noite das Lanternas | *(triste)* "Ponho uma lanterna pelo Eldrin. Ele não morreu! Mas está longe. A Lyra diz que também serve." |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`).

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `selene_boss_javali_rei` | "Tinha mesmo uma pedra brilhante na barriga? Não? A Lyra mentiu-me. Ou o Bruno. Ou o javali." |
| Ent Ancião (10) | `selene_boss_ent_anciao` | "O Ent… e a Árvore-Mãe. Em Folhalta contavam histórias dela. Desculpa. Vou mexer o caldeirão. Não tem nada ao lume." |
| Aranha-Mãe (15) | `selene_boss_aranha_mae` | "Veneno de aranha-mãe! Seda de aranha-mãe! Trouxeste algum? Não? Bom. Também é bom estares viv{o/a}." |
| Golem de Cristal (20) | `selene_boss_golem_cristal` | "Um golem que se ajoelhou antes de cair? Os golens não se ajoelham. Alguém lhes ensinou. Quem? Não gosto de não saber." |
| Serpente do Lodo (25) | `selene_boss_serpente_lodo` | "Lodo de serpente: ótimo para unguentos. Péssimo para o cabelo. O teu. Vai lavar-te." |
| Hidra do Pântano (30) | `selene_boss_hidra_pantano` | "Cabeças que voltam a crescer! Tens sangue de hidra nas botas? Posso raspar? Para uma Poção de Regeneração Real!" |
| Escorpião Imperador (35) | `selene_boss_escorpiao_imperador` | "Uma gota de veneno de escorpião imperador mata um camelo. Duas fazem um antídoto. A alquimia é muito estranha." |
| Faraó Eterno (40) | `selene_boss_farao_eterno` | "Um faraó que viveu séculos. Que poção bebia? Quero a receita. Quero muito a receita. Não a encontraste? Procura melhor." |
| Yeti Ancião (45) | `selene_boss_yeti_anciao` | "Pelo de yeti não arde. Testei com fogo normal: não ardeu. Testei o meu cabelo: ardeu." |
| Dragão de Gelo (50) | `selene_boss_dragao_gelo` | "Metade da torre! Fiz uma poção para festejar. Tem bolhas. As bolhas cantam. Não era suposto." |
| Capitão Esqueleto (55) | `selene_boss_capitao_esqueleto` | "Os ossos dos piratas têm sal de um mar de outro mundo. Fascinante! Assustador. Fascinante!" |
| Leviatã (60) | `selene_boss_leviata` | "Venceste o mar inteiro… E o Kai? Nada? Fiz uma Poção de Respirar a mais. Para ele. Fica guardada." |
| Ferreiro Infernal (65) | `selene_boss_ferreiro_infernal` | "O Brom veio cá dizer 'nada'. Três vezes. Depois foi-se embora. Vai lá ter com ele, sim?" |
| Kai — salvo (68) | `selene_boss_kai_salvo` | "O Kai voltou! Dei-lhe uma poção de boas-vindas. Ele ficou verde. A poção não. Já passa." |
| Kai — vencido (68) | `selene_boss_kai_vencido` | "Senta-te. Faço-te um chá. Não é poção, é só chá. Às vezes o chá é a melhor alquimia que há." |
| Titã de Magma (70) | `selene_boss_tita_magma` | "Núcleo de Magma: o ingrediente mais quente que existe! Se trouxeres um, usa luvas. As minhas. Toma." |
| Lich Bibliotecário (75) | `selene_boss_lich_bibliotecario` | "Uma biblioteca de feitiços proibidos! Proibidos por quem? Só quero ler um. Os proibidos são os melhores." |
| Rei Sem Coroa (80) | `selene_boss_rei_sem_coroa` | "Um rei que tentou parar a torre. Se a torre é viva, ele tentou parar um coração. Coragem ou tristeza? As duas, acho." |
| Grifo Real (85) | `selene_boss_grifo_real` | "Penas de grifo flutuam sozinhas! Numa poção… Poção de Leveza Real. Já tem nome. Só falta existir." |
| Serafim Caído (90) | `selene_boss_serafim_caido` | "Tens os olhos cansados. Tenho poções para os olhos. Para isso não tenho. Fica aqui um bocadinho." |
| Guardião do Tempo (95) | `selene_boss_guardiao_tempo` | "O tempo parava lá em cima? Então lá não se envelhece? Eu já levo trezentos anos de avanço. Não faz mal." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — Cabelo em pé

| | |
|---|---|
| ID | `cena_selene_2` |
| Quando | 2 ❤️ · entrar na Alquimia entre as 9:00 e as 18:00 |
| Onde | Alquimia da Selene |
| Quem | herói, Selene |
| Música | `alquimia` → silêncio → `alquimia` |

🎬 Ao abrires a porta, ouve-se um **BUM** abafado. Fumo roxo sai pela porta. Quando o fumo passa, a Selene está de pé no meio da sala, com a cara preta de fuligem e o cabelo prateado todo em pé, como um ouriço.

- **Selene** *(surpresa)*: "…"
- 🎬 Pisca os olhos duas vezes. Cai-lhe o lápis do cabelo. O cabelo continua em pé.

▶ **"Estás bem?!"**
▶ *(rir)*
▶ **"Era para fazer bum?"**

- *(Estás bem)* **Selene** *(feliz)*: "Estou ótima! As sobrancelhas é que ainda não sei. Ainda as tenho? Não me digas." ⚙ +30
- *(rir)* 🎬 A Selene olha-se num frasco espelhado e desata a rir também, tão alto que outro frasco cai. **Selene** *(feliz)*: "Pareço um cogumelo assustado!" ⚙ +30
- *(Era para fazer bum?)* **Selene** *(normal)*: "Era para fazer bum? …Era para fazer bum. Era! Escrevi 'fazer bum' no caderno. Sucesso!" ⚙ +30
- **Selene** *(feliz, depressa)*: "Sabes o que isto quer dizer? Que a raiz de ontem reage com a seiva! Hipótese confirmada! Com estilo!"
- 🎬 Tenta alisar o cabelo. Volta a pôr-se em pé.
- **Selene** *(normal)*: "Vou ficar assim uns dias. Se alguém perguntar, é moda élfica."

⚙ 5% de desconto na Alquimia.

### ❤️ 4 — A poção do humor

| | |
|---|---|
| ID | `cena_selene_4` |
| Quando | 4 ❤️ · entrar na Alquimia entre as 15:00 e as 18:00 |
| Onde | Alquimia, mesa do fundo |
| Quem | herói, Selene |
| Música | `alquimia` (versão calma, com sinos) |

🎬 A Selene está sentada a olhar para um frasco redondo. O líquido lá dentro muda devagar de cor: azul, verde, amarelo.

- **Selene** *(feliz)*: "Senta-te. Mas não toques. Bem, toca. É para tocar. Segura nele."
- 🎬 O herói segura no frasco. O líquido fica cor de laranja.
- **Selene** *(surpresa)*: "Laranja! Laranja é 'curioso'. Esta poção muda de cor com o humor de quem a segura. Levei onze anos a fazê-la."
- **Selene** *(normal)*: "Não serve para nada. Não cura, não protege, não explode. Os humanos perguntam sempre 'para que serve?'"

▶ **"É bonita. Chega."**
▶ **"Que cor fica contigo?"**
▶ **"Serve para saber como estás."**

- *(bonita)* **Selene** *(feliz)*: "É bonita, chega! Vou escrever isso na porta da loja." ⚙ +30
- *(contigo)* 🎬 A Selene pega no frasco. Fica azul-escuro, quase cinzento. Depois, devagar, amarelo. **Selene** *(triste → feliz)*: "Azul é saudade. Amarelo é… companhia. Fica amarelo quando estás aqui. Não sei porquê. Sei." ⚙ +30
- *(saber como estás)* **Selene** *(surpresa)*: "…Ninguém tinha pensado nisso. Nem eu. Afinal serve para alguma coisa." ⚙ +30
- **Selene** *(normal)*: "Fica com ela. Põe-na em casa. Assim, quando chegares cansad{o/a}, ela diz-te. E tu dizes-me."

⚙ Recebe o **Frasco do Humor** (decoração para a casa: muda de cor com o teu estado — vida, cansaço, amizades).

### ❤️ 6 — A carta do Eldrin

| | |
|---|---|
| ID | `cena_selene_6` |
| Quando | 6 ❤️ · `missao(R1_07) == ativa` (já entregaste a carta do Eldrin) · entrar na Biblioteca entre as 18:00 e as 20:00 |
| Onde | Biblioteca, mesa do canto, à luz de um Cogumelo Luminoso |
| Quem | herói, Selene, (Velho Fausto ao fundo) |
| Música | `biblioteca` → `tema_selene` (harpa) |

🎬 A Selene está com a carta do Eldrin à frente, ainda fechada. Já a tirou da gaveta. Não a abriu.

- **Selene** *(triste)*: "{nome}. Senta-te. Preciso de alguém aqui quando abrir isto. Alguém que não seja o Fausto. Ele ressona."
- **Selene** *(triste)*: "Tenho medo do que diz. Que diga 'volta'. Ou pior: que não diga."
- 🎬 Abre a carta. A letra é grande e torta, com desenhos de folhas nas margens.
- **Selene** *(a ler)*: "'Querida Selene. A Lothiel diz que não te devo escrever. Escrevo na mesma. Aprendi contigo.'"
- **Selene** *(a ler)*: "'O Poço da Lua voltou a brilhar. O Faelan continua sem sorrir. A Tilly perdeu a raposa outra vez.'"
- **Selene** *(a ler)*: "'A Lothiel diz o teu nome quando pensa que ninguém ouve. Baixinho. Como quem guarda uma coisa.'"
- 🎬 A Selene para. Tapa a boca com a mão.
- **Selene** *(a ler)*: "'Não estou zangado por teres ido. Nunca estive. Só cresci. Já chego ao cesto sem saltar.'"
- **Selene** *(a ler)*: "'Escreve-me. Nem que seja só: não explodi.'"
- 🎬 Silêncio. O Fausto, ao fundo, finge que lê muito atentamente.

▶ **"Escreve-lhe tudo."**
▶ **"Porque é que nunca voltaste?"**
▶ *(esperar em silêncio)*

- *(tudo)* **Selene** *(feliz, a chorar)*: "Tudo? São cem anos. Vou precisar de muito papel. Fausto! Papel!" ⚙ +30
- *(nunca voltaste)* **Selene** *(triste)*: "Porque saí de noite, contra a vontade dos anciãos. Tive medo de voltar e já não ter lugar. Cem anos de medo." ⚙ +30
- *(silêncio)* 🎬 A Selene encosta a cabeça ao teu ombro durante um segundo. **Selene** *(normal)*: "Obrigada. O silêncio também é um ingrediente." ⚙ +30
- 🎬 Escreve muito depressa. Enche três folhas. Dobra-as. Escreve por fora, em letra pequena: *"Não explodi. Quase."*
- **Selene** *(feliz)*: "Levas-lha? Eu… ainda não consigo subir. Mas a carta consegue. É um começo."

⚙ Missão **R1_07** avança: levar a **Resposta da Selene** ao Eldrin (andar 7). A Selene aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — Um céu inteiro

| | |
|---|---|
| ID | `cena_selene_8` |
| Quando | 8 ❤️ · noite, 21:00–23:00 · `clima == sol` (céu limpo) · entrar no Bairro dos Artesãos |
| Onde | telhado da Alquimia (sobe-se pela escada das traseiras) |
| Quem | herói, Selene |
| Música | `aurora` (versão só harpa) |

🎬 Uma escada encostada à parede das traseiras. Lá em cima, a Selene está deitada nas telhas, de óculos de proteção na testa, a olhar para as estrelas. Ao lado dela há um caderno aberto cheio de pontos e linhas.

- **Selene** *(feliz)*: "Sobe! Cuidado com a terceira telha. E a quinta. E a sétima. As ímpares estão todas soltas."
- 🎬 O herói deita-se ao lado dela.
- **Selene** *(normal)*: "Em Folhalta o céu é um teto. Tem cor de céu, tem nuvens, até chove. Mas do cimo da árvore mais alta… quase lhe tocas."
- **Selene** *(normal)*: "A Lothiel tinha seis anos quando a floresta caiu. Lembra-se de pouco. Mas lembra-se do céu."
- **Selene** *(feliz)*: "Contava-me que o céu de antes tinha duas luas. Uma grande e branca, e uma pequenina, verde, que corria atrás da outra."
- **Selene** *(feliz)*: "Que o vento vinha de muito longe e trazia cheiros de sítios que ninguém conhecia. E que se atirasses uma pedra para cima, ela nunca batia em nada."
- **Selene** *(triste)*: "Quando desci para Ascendia, chorei a primeira vez que vi este céu. É tão grande. Mas olha."
- 🎥 A câmara roda devagar: o céu cheio de estrelas e, a meio, a torre, negra, a cortá-lo de cima a baixo.
- **Selene** *(triste)*: "A torre está sempre a meio. Como um dedo a apontar. Nunca é um céu inteiro."
- **Selene** *(normal)*: "O meu sonho é ver um céu verdadeiro. Sem teto e sem torre. Um céu onde uma pedra atirada para cima nunca bate em nada."

▶ **"Um dia vemo-lo juntos."**
▶ *(atirar uma pedra para cima)*
▶ **"No meu mundo há um assim."**

- *(juntos)* **Selene** *(feliz)*: "Os elfos levam as promessas muito a sério. Vais ter de viver muito tempo. Tenho uma poção para isso. Não, não tenho. Ainda." ⚙ +30
- *(pedra)* 🎬 A pedra sobe… e cai no telhado da Forja do Brom, ao lado. Ouve-se ao longe: "QUEM FOI?!" A Selene ri-se tanto que quase escorrega. **Selene** *(feliz)*: "Bateu em alguma coisa! Bateu no Brom! Não conta!" ⚙ +30
- *(meu mundo)* **Selene** *(surpresa)*: "No teu mundo o céu não tem torre? Então tu já viste um céu inteiro! Conta-me. Devagar. Quero desenhar." ⚙ +30
- 🎬 Ficam os dois calados a olhar para cima. Uma estrela cadente atravessa o céu, do lado onde não está a torre.
- **Selene** *(normal)*: "Viste? Do lado certo. Isso é um sinal. Não acredito em sinais. Mas este conta."

⚙ 15% de desconto na Alquimia. A Selene passa a mandar **cartas** (1 por semana) com presentes: Cogumelo Luminoso, uma poção da tua região ou uma página do caderno das estrelas dela (decoração emoldurada).

### ❤️ 10 — Trezentos anos

| | |
|---|---|
| ID | `cena_selene_10` |
| Quando | 10 ❤️ · `missao(N_SELENE_3) == concluida` · entrar na Alquimia entre as 18:00 e as 20:00 (nesse dia ela não vai à Biblioteca) |
| Onde | Alquimia, porta fechada, todas as velas acesas |
| Quem | herói, Selene |
| Música | `tema_selene` (harpa + coro baixo) |

🎬 A sala está arrumada. Arrumada! Nenhum frasco fora do sítio. No meio da mesa, uma caixinha de madeira de Folhalta.

- **Selene** *(normal)*: "Não estranhes a arrumação. Foi a Tina. Eu só não desarrumei. Está a custar-me imenso."
- **Selene** *(normal)*: "Quando eu era pequena, em Folhalta, misturava seiva com orvalho e dizia que ia fazer uma pedra mágica."
- **Selene** *(feliz)*: "Uma pedra que transformasse as coisas. Os livros dos humanos dizem 'chumbo em ouro'. Eu queria outra coisa."
- **Selene** *(triste)*: "Queria transformar o teto de Folhalta num céu verdadeiro. Trezentos anos a tentar. Não consegui."
- 🎬 Abre a caixinha. Lá dentro há uma pedra pequena, vermelha, que pulsa devagar como um coração.
- **Selene** *(feliz)*: "Mas a pedra aprendeu outra coisa. Faz as coisas valerem o dobro. Uma poção cura o dobro. Um remédio, o dobro."
- **Selene** *(normal)*: "É a Pedra Filosofal. É tudo o que eu sei, metido numa coisa do tamanho de um morango."
- **Selene** *(normal)*: "E é tua. Não, não digas que não. Tu é que sobes. Eu fico cá em baixo a explodir coisas."

▶ **"É o teu trabalho de uma vida."**
▶ **"Vens comigo ver o céu, um dia."**

- *(trabalho de uma vida)* **Selene** *(feliz)*: "Exatamente. E uma vida inteira fechada numa caixa não serve para nada. Leva-a lá para cima. Deixa-a trabalhar."
- *(ver o céu)* **Selene** *(feliz, a chorar)*: "Prometido. Os elfos cumprem sempre as promessas. Demoram é muito."
- **Selene** *(normal)*: "Dizem que quem chega ao topo pode voltar para casa. Se chegares… olha para o céu lá de cima. Por mim."
- **Selene** *(feliz)*: "E depois desce e conta-me. Com pormenores. Cores, cheiros, quantas luas."
- 🎬 Pega no Frasco do Humor que tens na mochila (se o trouxeres) e segura-o: fica amarelo, muito amarelo.

⚙ Recebe a **Pedra Filosofal** (acessório: as poções curam o dobro). Título *A Melhor Experiência*.
⚙ A partir daqui a Selene tem a fala `selene_dia_66`.

---

## 9. Missões

### N_SELENE_1 — Ervas Verdes (0 ❤️, rank F, depois de H_03)

- **Pedir** — **Selene** *(feliz, depressa)*: "Preciso de dez Ervas Verdes! Dez! Para uma experiência. Não, não vai explodir. Provavelmente. Trazes?"
  ▶ **"Claro!"** ⚙ missão iniciada · ▶ **"Agora não."** → "Está bem. Eu espero. Os elfos são ótimos a esperar. Eu sou péssima, mas sou elfa."
- **Durante** — **Selene**: "Já tens {n}? Faltam {10-n}. A Erva Verde está em todo o lado. Literalmente. Tenho uma no sapato."
- **Entregar** — 🎬 a Selene atira as ervas para o caldeirão. **BUM.** Fumo verde.
  - **Selene** *(surpresa)*: "Era para fazer bum? …Não era. Não era nada."
  - **Selene** *(feliz)*: "Mas olha o que sobrou no fundo: Poção de Vida. Perfeita. Por acaso. A melhor alquimia é sempre por acaso."
  - **Selene** *(normal)*: "Toma a receita. Duas Ervas Verdes e uma Água Limpa. Sem explosões. Com estas mãos, até tu consegues."
  - ⚙ receita **Poção de Vida P** · 80 ouro · +100 amizade

### R1_07 — Cartas para Selene (dada pelo Eldrin, andar 7)

A missão começa em Folhalta (falas do Eldrin em `docs/dialogos/povoacoes_r01.md`) e acaba na cena de 6 ❤️.

- **Entregar a carta** (qualquer número de corações) — 🎬 a Selene vê a letra no envelope e fica muito quieta.
  - **Selene** *(surpresa)*: "É a letra do Eldrin. As folhas desenhadas na margem. Ele faz sempre as folhas."
  - **Selene** *(triste)*: "Obrigada. Vou ler. Depois. Logo. Amanhã."
  - 🎬 Guarda a carta numa gaveta e fecha-a à chave.
  - ⚙ +50 amizade · Diário: *"A Selene guardou a carta do Eldrin sem a abrir. Talvez um dia confie em ti o suficiente para a ler. (6 ❤️)"*
- **Durante** (antes dos 6 ❤️) — **Selene** *(normal)*: "A carta? Está segura. Na gaveta. Fechada. Muito, muito segura."
- **Cena de 6 ❤️** — a Selene lê a carta contigo e escreve a resposta (ver secção 8).
- **Levar a resposta** ao Eldrin (andar 7). A reação dele está em `povoacoes_r01.md`; ele manda de volta um **raminho de Folhalta** atado com fio.
- **Entregar** — **Selene** *(feliz, depressa)*: "Ele leu? O que disse? Riu-se? Chorou? Os dois? Os dois é bom!"
  - 🎬 Cheira o raminho e fecha os olhos.
  - **Selene** *(feliz)*: "Cheira a casa. Toma: a receita da Poção Élfica. A da minha mãe. Lá em cima, todos a sabem. Cá em baixo, só tu."
  - ⚙ receita **Poção Élfica** · +150 amizade · flag `selene_eldrin_cartas` (o Eldrin e a Selene passam a trocar cartas; há uma fala nova do Eldrin em Folhalta em cada estação)

### N_SELENE_3 — A Poção Impossível (`coracoes(selene) >= 5 && andar_maximo >= 41`)

- **Pedir** — **Selene** *(feliz, depressa)*: "Os livros dizem que a Poção de Encolher é impossível! IMPOSSÍVEL! Eu não acredito em impossível. Acredito em 'ainda não'."
  - **Selene** *(normal)*: "Preciso de uma coisa pequena de cada mundo. Hipótese: as coisas pequenas sabem como se é pequeno."
  - **Selene** *(normal)*: "Pó de Fada, do andar 4. Esporos de Fungo Azul, de Mycélia. Um Lírio do Pântano. Areia Mágica do deserto."
  - **Selene** *(feliz)*: "E uma Lágrima de Aurora. Não é para comer. É para a poção. …Está bem, não é para comer."
  - ▶ **"Vou buscar tudo."** ⚙ missão iniciada · ▶ **"É muita coisa."** → "É. Por isso é que é impossível. Ainda."
- **Ingredientes**: 1 Pó de Fada (região 1) · 1 Esporos de Fungo Azul (região 2) · 1 Lírio do Pântano (região 3) · 1 Areia Mágica (região 4) · 1 Lágrima de Aurora (região 5).
- **Durante** — **Selene**: "Já tens {n} dos 5? A Lágrima de Aurora é a mais difícil. Só aparece quando há aurora. Paciência. Tu tens. Eu não."
- **Entregar** — 🎬 a Selene põe os cinco ingredientes no caldeirão, um de cada vez, e baixa os óculos de proteção.
  - **Selene** *(normal)*: "Pronto. Se isto explodir, diz à Tina que os frascos azuis são dela."
  - 🎬 Nada explode. O caldeirão faz *plim*. Sai uma poção minúscula, do tamanho de um dedal.
  - **Selene** *(surpresa)*: "Não explodiu. Porque é que não explodiu? Tenho de testar."
  - 🎬 Bebe-a antes que a possas impedir. **Puf.** A Selene fica do tamanho de um frasco, em cima da mesa.
  - **Selene** *(feliz, voz fininha)*: "FUNCIONA! Funciona! Sou do tamanho de uma colher! …Como é que se desfaz? Não pensei nisso."
  - 🎬 30 segundos depois, **puf**, volta ao tamanho normal. Senta-se no chão a rir.
  - **Selene** *(feliz)*: "Trinta segundos. Chega para passar por um buraco pequeno. Como a toca do andar 5, onde só cabe um coelho…"
  - ⚙ receita **Poção de Encolher** · Poção de Encolher ×3 · +200 amizade

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `selene_estado_vida` | `vida_pct < 30` | surpresa | "Estás pálid{o/a}! Bebe isto. Não, isso é tinta. ISTO. E depois vai à Igreja. A correr. Devagar. A correr devagar." |
| `selene_estado_maldito` | `estado(amaldicoado)` | surpresa | "Uma maldição! Posso estudar? Não! Primeiro vais à Irmã Célia. Depois contas-me tudo." |
| `selene_estado_cansado` | `estado(cansado)` | normal | "Olheiras! Tenho uma poção para o sono, mas não sei se faz dormir ou acordar. Vai dormir. É mais seguro." |
| `selene_estado_molhado` | `estado(encharcado)` | surpresa | "Não te aproximes dos frascos de pó! Alguns não gostam de água. Explodem de desgosto." |
| `selene_estado_veneno` | `estado(veneno)` | normal | "Verde à volta dos olhos: veneno. Toma um Antídoto. Este é por conta da casa. O próximo não." |
| `selene_estado_sapo` | `estado(sapo)` | surpresa | "UM SAPO! Fica quieto, só quero medir… {nome}?! Desculpa! Mas não te mexas na mesma." |
| `selene_estado_encolhido` | `estado(encolhido)` | feliz | "Funciona fora do laboratório! Estás do tamanho de uma chávena! Não te mexas, vou buscar o caderno!" |
| `selene_arma_nova` | arma equipada pela 1.ª vez com raridade Épica ou melhor | surpresa | "Essa arma brilha! Pó de estrela? Não… outra coisa. Posso raspar um bocadinho? Um bocadinho só." |
| `selene_animal` | `animal != nenhum` (1.ª vez) | feliz | "Um animal! Posso ver-lhe os dentes? Para a ciência. Não para morder. Ele é que decide." |
| `selene_comp_mia` | `companheiro(mia)` | feliz | "Mia! Queres ver uma explosão pequenina? …Não me olhes assim, {nome}. É educativo." |
| `selene_comp_kai` | `companheiro(kai)` | feliz | "Kai! Fiz uma poção que sabe à 'cola' do teu mundo. Acho eu. Nunca bebi cola. Prova." |
| `selene_comp_gorvan` | `companheiro(gorvan)` | surpresa | "Mestre Gorvan! Uma Poção de Força? Não precisa? Pois não. Leve na mesma. Por mim." |
| `selene_classe` | 1.ª conversa depois de escolher classe | feliz | "{classe}! Então vais precisar de poções. Todas as classes precisam de poções. Vês como sou imparcial?" |
| `selene_tina_chegou` | 1.ª conversa depois de `missao(R1_13) == concluida` | surpresa | "Trouxeste-me uma aprendiz! A Tina! Ela lê as instruções ANTES de começar. Nunca vi tal coisa. Vou aprender muito." |
| `selene_titulo_cobaia` | 1.ª conversa depois de ganhar o título *Cobaia* (R3_08) | feliz | "Bebeste cinco Poções Surpresa e sobreviveste? Cobaia oficial! Estou tão orgulhosa. E um bocadinho com inveja." |

### Serviço (a Alquimia)

Falas da **Loja** e das **Receitas**. Os preços e as receitas estão em `docs/ITENS.md`, secções 2 e 3.

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `selene_serv_abrir` | abrir a loja | feliz | "Poções, antídotos, bombas, elixires! Tudo testado. Em mim. Quase tudo." |
| `selene_serv_abrir_2` | abrir a loja, 4+ ❤️ | feliz | "A minha cobaia favorita! O que precisas hoje? Não, espera. Deixa-me adivinhar pela tua cara. …Poções de Vida." |
| `selene_serv_vida` | comprar Poções de Vida | normal | "Poções de Vida. Bebe quando doer, não quando já não doer nada. Isso é tarde." |
| `selene_serv_antidoto` | comprar Antídoto, Ligadura ou Colírio | normal | "Antídotos! A coisa mais aborrecida que faço. E a que salva mais gente. A vida é assim." |
| `selene_serv_bomba` | comprar bombas | feliz | "Bombas! Atira para longe. LONGE. Mais longe do que estás a pensar." |
| `selene_serv_elixir` | comprar um elixir ou poção rara | surpresa | "Esse é caro porque levei semanas a fazê-lo. E porque explodiu duas vezes. As explosões também se pagam." |
| `selene_serv_receita` | comprar uma receita | feliz | "Uma receita nova! Lê tudo antes de começar. Eu nunca leio. Por isso é que tenho o cabelo assim." |
| `selene_serv_mesa` | usar a mesa de alquimia dela | normal | "A mesa é tua. Os frascos da esquerda são inofensivos. Os da direita… usa os da esquerda." |
| `selene_serv_excelente` | fazer uma poção de qualidade **Excelente** | surpresa | "Excelente?! Na primeira? Deixa-me ver a cor. …Perfeita. Estou orgulhosa e ofendida ao mesmo tempo." |
| `selene_serv_descoberta` | descobrir uma receita nova sozinh{o/a} | feliz | "Descobriste uma receita sozinh{o/a}! Fascinante! Escreve-a já, antes que te esqueças. Eu esqueço sempre." |
| `selene_serv_vender` | vender-lhe ervas raras ou ingredientes estranhos | feliz | "Isto é raro! Compro! Compro tudo! …Pago o preço justo. Quase justo. Sou alquimista, não sou santa." |
| `selene_serv_sem_ingredientes` | faltam ingredientes | normal | "Faltam ingredientes. A alquimia é como a cozinha: sem ovos não há bolo. Com ovos a mais há explosão." |
| `selene_serv_sem_ouro` | falta ouro | triste | "Não chega o ouro. Desculpa. Eu dava-te, mas a Tina faz as contas e ela é implacável." |
| `selene_serv_fechado` | falar com ela na Biblioteca (18:00–20:00) | normal | "Shhh! A loja está fechada. Estou a estudar. Amanhã às nove. Ou às nove e meia. Às nove." |
| `selene_serv_fechado_domingo` | Domingo | feliz | "Domingo! A loja dorme. Eu ando a apanhar ervas. Ajudas? Não pago, mas ensino." |
| `selene_serv_tina` | comprar com a Tina ao balcão (depois de R1_13: poções 10% mais baratas) | feliz | "A Tina faz o preço. Ela é mais barata e mais organizada do que eu. Vou fingir que não me importo." |
| `selene_serv_desconto` | 1.ª compra depois da cena de 2 ❤️ | feliz | "Desconto para quem me viu com o cabelo em pé e não fugiu. É uma categoria muito pequena." |
| `selene_serv_muitas` | comprar 20 ou mais poções de uma vez | surpresa | "Vinte poções?! Vais subir ou vais abrir uma loja? Não abras uma loja. A Tina ficava com ciúmes." |
| `selene_serv_adeus` | sair da loja | normal | "Volta inteir{o/a}! E se encontrares uma erva que não conheço, traz. Mesmo que morda." |
