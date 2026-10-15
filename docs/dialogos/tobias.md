# Tobias — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.5. Dados: `dados/dialogos/tobias.json`.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios e saltitantes, com um "tlim" de moeda no fim das frases felizes |
| Como fala | como um pregão de feira: alto, exagerado, cheio de exclamações; diz os preços a cantar; promete descontos que não existem; quando fala do irmão fica vermelho e repete as palavras |
| Repete | "Preço especial!", "Só para ti!", "Negócio é negócio!", "Ai, o meu coração de mercador!", "Tlim-tlim!" |
| Tiques | torce o bigode (animação `torcer_bigode`) quando pensa num preço; morde as moedas para ver se são verdadeiras (`morder_moeda`) |
| Nunca diz | o preço verdadeiro à primeira; que é generoso (até à cena de 4 ❤️); que tem saudades do irmão (até à missão N_TOBIAS_3); mal de quem não tem dinheiro |
| Chama ao herói | `{freguês/freguesa}`; com 6+ corações "sóci{o/a}" |
| Rotina ao Domingo | Mercado das 7:00 às 12:00 · Taberna ao almoço (12:00–17:00) · Bairro Baixo das 18:00 às 20:00, de capuz, com um carrinho de pão (é o segredo da cena de 4 ❤️; antes dela, só se vê um vulto que foge) |

---

## 2. Primeira conversa

Depois da cena P5 (prólogo), a 1.ª vez que carregas em **Conversar** com o Tobias:

- **Tobias** *(feliz)*: "Um Jogador novo! Bem-vind{o/a}, bem-vind{o/a}! Tobias, mercador, ao teu dispor. E ao dispor do teu ouro."
- **Tobias** *(normal)*: "Aqui há de tudo: poções, tochas, comida, móveis… e coisas que ainda não sabes que precisas. A banca muda todos os dias às seis."
- **Tobias** *(normal)*: "De três em três dias, coisas RARAS. Estão debaixo deste pano. Não se tocam. Olham-se. E compram-se."
- **Tobias** *(feliz)*: "Regatear? Podes tentar! Regatear é uma arte. Mas é uma arte cansativa: três vezes por dia, no máximo. Ou o Tobias fica rabugento."
- **Tobias** *(zangado)*: "Ah, e se vires um mercador igual a mim numa Zona Segura, é o meu irmão. Não lhe compres nada. Os preços dele são uma vergonha."
- *(se a Skill Única for Mão de Midas)* **Tobias** *(surpresa)*: "Espera… Mão de Midas?! Tu e eu vamos ser grandes amigos. Enormes."

⚙ Abre o menu do Tobias: **Loja · Itens raros · Missões · Perguntar sobre…**

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `tobias_dia_01` | `hora entre 7 e 9` | feliz | "Bom dia! Abri há cinco minutos e já vendi duas coisas. Uma foi a mim próprio, mas conta." |
| `tobias_dia_02` | `hora entre 7 e 9` | normal | "Mercadoria nova! Chegou hoje. Ou ontem. Está fresca, é o que interessa." |
| `tobias_dia_03` | `hora entre 12 e 14` | normal | "Hora de almoço. Eu almoço a vender. Vender alimenta mais." |
| `tobias_dia_04` | `hora entre 17 e 19` | normal | "Quase a fechar! Os preços do fim do dia são os melhores. São os mesmos, mas ditos com mais pena." |
| `tobias_dia_05` | `hora entre 19 e 23` | feliz | "Fora de horas não vendo nada. A não ser que queiras comprar. Queres comprar?" |
| `tobias_dia_06` | — | feliz | "Preço especial! Só para ti! …É o mesmo preço para toda a gente, mas tu és especial." |
| `tobias_dia_07` | — | zangado | "O meu irmão? Vende areia a quem tem sede." |
| `tobias_dia_08` | — | normal | "Uma moeda bem contada vale duas. Uma moeda mal contada vale zero e uma dor de cabeça." |
| `tobias_dia_09` | — | normal | "Tentei vender à Lyra um pente para o Mestre Gorvan. O Mestre passou e olhou para mim. Só olhou. Ainda estou a tremer." |
| `tobias_dia_10` | — | feliz | "Este colete tem vinte e três bolsos. Sei o que está em vinte e dois. O vigésimo terceiro é um mistério." |
| `tobias_dia_11` | — | normal | "Achado não é roubado! …A Lyra diz que um papel da Guilda é da Guilda. A Lyra é muito rígida." |
| `tobias_dia_12` | — | feliz | "Se vires uma coisa que brilha, apanha-a. Se não brilhar, apanha-a na mesma. Eu compro." |
| `tobias_dia_13` | `missao(H_14) != concluida` | feliz | "O Kai tentou regatear comigo e ganhou-me uma maçã. Uma! Estou orgulhoso e furioso ao mesmo tempo." |
| `tobias_dia_14` | `dia_semana == segunda` | zangado | "Segunda-feira: chega a carta do meu irmão. Já estou zangado e ainda nem a abri." |
| `tobias_dia_15` | `dia_semana == sexta` | feliz | "Sexta! O Lucien canta na taberna e eu vendo amendoins à porta. Ele diz que é falta de respeito. Eu digo que é parceria." |
| `tobias_dia_16` | `dia_semana == domingo` | normal | "Ao domingo fecho ao meio-dia. Porquê? …Descanso. Os mercadores também descansam. Às vezes." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `tobias_dia_20` | `estacao == primavera` | feliz | "Primavera! Toda a gente quer sementes, flores e sapatos novos. E eu quero que toda a gente queira." |
| `tobias_dia_21` | `estacao == primavera && hora entre 7 e 12` | normal | "Vendi um chapéu de palha à Hana. Ela já tinha um. Agora tem dois. Isso é que é felicidade." |
| `tobias_dia_22` | `estacao == verao` | normal | "Calor! Leques, chapéus, água fresca. A água é do poço, mas o copo é meu. E o copo paga-se." |
| `tobias_dia_23` | `estacao == verao && hora entre 12 e 16` | normal | "Com este sol, as moedas aquecem nos bolsos. Ando a tilintar quente." |
| `tobias_dia_24` | `estacao == outono` | normal | "Outono: as pessoas compram casacos e fazem contas ao inverno. Eu faço contas o ano inteiro." |
| `tobias_dia_25` | `estacao == outono && clima == chuva` | feliz | "Chuva de outono! Guarda-chuvas a metade do preço. Metade de um preço muito alto, mas metade." |
| `tobias_dia_26` | `estacao == inverno` | triste | "Inverno. Ninguém compra gelados. Vendi um ao Brom. Comeu-o a resmungar. Foi o meu melhor cliente do mês." |
| `tobias_dia_27` | `estacao == inverno && clima == neve` | feliz | "Neve! Vou pôr uma placa: 'Neve fresca, uma moeda o balde.' Alguém compra. Alguém compra sempre." |
| `tobias_dia_28` | `clima == chuva` | normal | "A chuva espanta os fregueses. Fico a contar moedas. As moedas não fogem da chuva." |
| `tobias_dia_29` | `clima == trovoada` | triste | "Trovoada! Escondi o ouro debaixo do balcão. Os raios gostam de metal. Eu também, mas não assim." |
| `tobias_dia_30` | `clima == nevoeiro` | normal | "Com este nevoeiro não vejo quem compra. Paga primeiro, depois vemos se és tu." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `tobias_dia_40` | `andar_maximo < 5` | normal | "Andares de baixo? Compra poções. Muitas. A mim. Isto é um conselho e uma venda ao mesmo tempo." |
| `tobias_dia_41` | `andar_maximo >= 5 && andar_maximo < 11` | zangado | "Viste numa Zona Segura um senhor com o meu bigode, mas mal penteado? É o meu irmão. Não lhe compres nada." |
| `tobias_dia_42` | `boss_derrotado(ent_anciao) && andar_maximo < 15` | triste | "Agora que há quinta, toda a gente me quer VENDER legumes. Eu queria que me comprassem. A vida é ao contrário." |
| `tobias_dia_43` | `andar_maximo >= 11 && missao(R2_11) != concluida` | feliz | "Nas minas há uma toupeira de ouro. De OURO. Eu tenho uma gaiola. Tu tens pernas. Estás a ver onde quero chegar?" |
| `tobias_dia_44` | `boss_derrotado(golem_cristal)` | feliz | "Tens casa! Uma casa precisa de mesas, cadeiras, tapetes, candeeiros… Senta-te. Vamos falar de mobília." |
| `tobias_dia_45` | `andar_maximo >= 31` | normal | "Lá em cima pagam fortunas por uma tocha. Leva tochas. Vende-as. Traz-me metade. É só uma ideia." |
| `tobias_dia_46` | `andar_maximo >= 50` | feliz | "Metade da torre! Se fosses mercadoria, valias o dobro. É um elogio. O maior que eu sei fazer." |
| `tobias_dia_47` | `missao(H_14) == concluida && missao(H_17) != concluida` | triste | "O Kai devia-me dez moedas. Já não as quero. Quero que ele volte para me dever mais." |
| `tobias_dia_48` | `flag(kai_salvo)` | feliz | "O Kai voltou e pagou-me as dez moedas. Disse que eram 'para dar sorte'. Guardei-as numa caixa à parte." |
| `tobias_dia_49` | `missao(H_17) == concluida && !flag(kai_salvo)` | triste | "As dez moedas do Kai continuam no caderno. Não as risco. Ele ainda me deve. Ainda vai pagar." |
| `tobias_dia_50` | `missao(H_22) == concluida` | normal | "O meu irmão vende no andar 91. NOVENTA E UM. Eu nem sabia que ele era tão doido. Nem tão corajoso." |
| `tobias_dia_51` | `rank >= C` | normal | "Rank C! O Rook já te deixa entrar na loja dele, não é? Lá tudo é mais barato porque não é de ninguém." |
| `tobias_dia_52` | `rank >= A` | feliz | "Rank A! Quando passas na rua, as pessoas compram coisas parecidas com as tuas. Ganho muito contigo." |
| `tobias_dia_53` | `missao(N_TOBIAS_3) == concluida` | feliz | "Placa nova: 'Tobias & Tibério'. Ele queria 'Tibério & Tobias'. Tirámos à sorte. Ganhei. Ele diz que a moeda era minha." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `tobias_dia_60` | `coracoes(tobias) >= 2` | feliz | "Guardei-te uma coisa boa debaixo do balcão. Não, não é de graça. Mas está guardada. Isso já é muito." |
| `tobias_dia_61` | `coracoes(tobias) >= 3` | normal | "Sabes porque é que regateio? O meu pai regateava. E o pai dele. Somos uma família de gente teimosa." |
| `tobias_dia_62` | `coracoes(tobias) >= 4` | normal | "Domingo à tarde estou ocupado. Já sabes com quê. Shhh. Fala mais baixo. Eu nem disse nada." |
| `tobias_dia_63` | `coracoes(tobias) >= 5` | feliz | "Fiz as contas: és quem mais vem à minha banca. Não te dou desconto por isso. Dou um sorriso. Grátis." |
| `tobias_dia_64` | `coracoes(tobias) >= 6` | feliz | "Sóci{o/a}! Posso chamar-te sóci{o/a}? Não tens parte nos lucros. É só um nome bonito." |
| `tobias_dia_65` | `coracoes(tobias) >= 8` | triste | "Às vezes conto as moedas e penso em ti. Não por seres rico. És rico? Não. Penso em ti na mesma." |
| `tobias_dia_66` | `coracoes(tobias) >= 10` | feliz | "Se um dia eu tiver uma loja do tamanho da torre, a primeira chave é tua. A segunda do meu irmão. A terceira minha." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `tobias_dia_70` | `origem == jogador` | feliz | "No teu mundo, os jogos tinham mercadores que compravam tudo? Até botas velhas? Que mundo maravilhoso." |
| `tobias_dia_71` | `origem == atrasado` | feliz | "Chegas sempre a correr. Ótimo! Quem tem pressa não regateia." |
| `tobias_dia_72` | `origem == ajudante` | normal | "A Dona Marta diz que ajudas toda a gente. Cuidado: quem ajuda toda a gente fica sem tempo para fazer compras." |
| `tobias_dia_73` | `origem == dormir` | normal | "Tens cara de quem dorme bem. Vendo almofadas. Ah, já dormes bem? Então vendo-te mais almofadas." |
| `tobias_dia_74` | `skill_unica == mao_de_midas` | feliz | "Mão de Midas! Toca nesta moeda. Mais uma vez. Nada? Tem de ser com mais força? Toca outra vez." |
| `tobias_dia_75` | `skill_unica == bolsa_infinita` | feliz | "Uma mochila sem fundo! És o melhor cliente que a torre alguma vez fez. Tu e esse saco." |
| `tobias_dia_76` | `skill_unica == olho_do_sistema` | normal | "Vês os números dos monstros? Então quanto vale este anel? …Não vês números de anéis? Que olho tão pouco prático." |
| `tobias_dia_77` | `skill_unica == mestre_artesao` | feliz | "Mestre Artesão? Tu fazes, eu vendo. Metade-metade. Bem… sessenta-quarenta. Para mim." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `tobias_curta_1` | feliz | "Voltaste! Esqueceste-te de comprar alguma coisa? Tenho a certeza que sim." |
| `tobias_curta_2` | normal | "Os preços não mudaram desde a última vez. Juro pelo meu bigode." |
| `tobias_curta_3` | feliz | "Tlim-tlim! É o som de quem volta à banca do Tobias." |
| `tobias_curta_4` | normal | "Estou a contar. Trinta e… pronto, perdi-me. Diz." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Tobias** *(normal)*: "A torre? É o maior cliente do mundo. Engole mundos inteiros e nunca pagou nada a ninguém."
- **Tobias** *(normal)*: "Mas também é a maior loja do mundo. Tudo o que vendo vem de lá: couro, minério, pérolas, ouro antigo…"
- **Tobias** *(feliz)*: "A minha teoria? Lá no topo alguém faz as contas a tudo. Andares, Jogadores, moedas. Eu gostava de ver esse caderno."
- **Tobias** *(triste)*: "Só não gosto de uma coisa nela: há muita gente que sobe e eu fico com as coisas que deixaram. À espera."

### 4.2 O andar atual

O Tobias fala da **região do andar mais alto** a que chegaste, com informação de mercador.

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta: couro de javali, cogumelos, Flor de Mel. E Mel Azul, no andar 6! Traz-mo. Compro barato, mas compro." |
| 2 Cavernas | "Cavernas: tochas, tochas, tochas. Vendo-as a 10. No andar 11 o meu irmão vende-as a 15. Ladrão de bigode." |
| 3 Pântano | "Pântano: Sal para as sanguessugas e Antídotos para tudo. E não compres nada a sapos. Os sapos fazem descontos falsos." |
| 4 Deserto | "Deserto: há ouro antigo pelo chão das pirâmides, no 38 e no 39. Se te sobrar algum… eu adoro ouro antigo. Para estudar." |
| 5 Gelo | "Gelo: no frio, uma sopa quente vale o dobro. Diz isso à Dona Marta. Não. Não digas. Ela bate-me com a colher." |
| 6 Oceano | "Oceano: pérolas! Pérolas Negras! Caranguejos com pinças de ouro maciço! Eu devia ter sido pirata." |
| 7 Vulcão | "Vulcão: os anões do Bastião regateiam melhor do que eu. Isso não devia ser possível. Vai lá e aprende. Depois ensina-me." |
| 8 Reino Assombrado | "Reino Assombrado: há um mercado de fantasmas que só abre à noite. Pagam com moedas que já não existem. Eu aceitava." |
| 9 Céu | "Céu: em Aerópolis vendem balões. Ar dentro de um saco! Quem é que compra isso? …Eu comprava. Que ideia brilhante." |
| 10 Abismo | "Abismo: não sei nada. Só sei que o meu irmão vende lá em cima. Se o vires, diz-lhe… diz-lhe que os preços dele são altos." |

### 4.3 Rumores

O Tobias diz **1 rumor por dia**, escolhido dos que cumprem a condição. São rumores de mercado: preços, coisas raras, quem compra o quê.

| ID | Condição | Rumor |
|---|---|---|
| `tobias_rumor_01` | — | "O meu irmão diz que vende nas Zonas Seguras porque 'ali ninguém compete'. Ali ninguém compete porque ninguém é doido." |
| `tobias_rumor_02` | — | "A Dona Marta compra duas mãos-cheias de cenouras a mais todas as manhãs. Há anos. Nunca perguntei para quem." |
| `tobias_rumor_03` | — | "O Brom deve-me três lingotes desde o inverno. Ou sou eu que lhe devo. Ninguém se lembra. Estamos quites." |
| `tobias_rumor_04` | — | "O Rook paga 40% por coisas 'duvidosas'. Eu pago 30% por coisas honestas. A honestidade sai cara." |
| `tobias_rumor_05` | `andar_maximo >= 5` | "No andar 5 há uma toca pequena demais para gente. Dizem que lá dentro há um ovo de ouro. Para animais! Que desperdício." |
| `tobias_rumor_06` | `andar_maximo >= 11` | "A Toupeira Dourada aparece uma vez em cada cinquenta túneis. Eu já mandei fazer a gaiola. Por precaução." |
| `tobias_rumor_07` | `andar_maximo >= 11` | "No andar 2 os lenhadores pagam bem por machados. No 11 pagam bem por tochas. Lá em cima pagam bem por tudo." |
| `tobias_rumor_08` | `boss_derrotado(golem_cristal)` | "A Cidade Errante anda por aí. O Ambrósio vende lá tudo pelo dobro. Eu vendo pelo dobro e meio, mas com simpatia." |
| `tobias_rumor_09` | `boss_derrotado(golem_cristal)` | "Fui ao leilão do Gaspar, em Vagar. Licitei por uma colher. Ganhei. Paguei trezentas moedas. Era uma colher." |
| `tobias_rumor_10` | `boss_derrotado(golem_cristal)` | "Se o Mercado tivesse telhado, eu tinha mais quatro coisas raras para vender. Fala com o Governador. Não digas que fui eu." |
| `tobias_rumor_11` | `andar_maximo >= 32` | "No Oásis de Zahra há um bazar com cinco lojas. Cinco! E nenhuma tem um bigode como o meu." |
| `tobias_rumor_12` | `andar_maximo >= 38` | "Na pirâmide do 38 há ouro antigo e armadilhas. O ouro vale as armadilhas? O ouro vale sempre as armadilhas." |
| `tobias_rumor_13` | `andar_maximo >= 51` | "Anda nas praias do mar um caranguejo com uma pinça de ouro maciço. Se o Barão Coaxim te oferecer 6 000, eu dou 6 001." |
| `tobias_rumor_14` | `andar_maximo >= 54` | "As ostras gigantes do andar 54 têm Pérolas Negras. Dizem que só abrem com música. Eu canto. Mal, mas canto." |
| `tobias_rumor_15` | `andar_maximo >= 55` | "Há um cofre num navio afundado no andar 56. Quem guarda dinheiro debaixo de água? …Na verdade é boa ideia." |
| `tobias_rumor_16` | `andar_maximo >= 71` | "No andar 72 há um mercado de fantasmas. Pagam com Moedas Antigas. Eu ADORO Moedas Antigas. Era capaz de lá ir. De dia não." |
| `tobias_rumor_17` | `andar_maximo >= 91` | "Dizem que no andar 97 há um mercado onde se trocam memórias. Que negócio horrível. Genial. Mas horrível." |
| `tobias_rumor_18` | `estacao == inverno` | "Festival da Estrela: toda a gente compra os presentes à última hora. É a minha época preferida. A seguir às outras três." |
| `tobias_rumor_19` | `missao(N_TOBIAS_3) == concluida` | "O Tibério está a ensinar-me a vender no escuro. Eu estou a ensiná-lo a sorrir. Estamos os dois a falhar." |

### 4.4 A vida dele

| Corações | Fala |
|---|---|
| 0 | "A minha vida? Comprar barato, vender caro, dormir pouco. É uma vida simples. Rica, mas simples." |
| 2 | "O meu pai, o velho **Teodoro**, tinha esta banca. Eu e o Tibério crescemos debaixo dela. A brincar entre os caixotes." |
| 4 | "Ao domingo à tarde já sabes onde estou. Às vezes acho que o Senhor Ninguém é o melhor de mim. E ele nem tem nome." |
| 6 | "Não vejo o Tibério há vinte anos. Só cartas. Às vezes leio-as com a voz dele. Imito-a mal. Já não me lembro bem da voz." |
| 8 | "Tenho medo de ficar velho a contar moedas sozinho. Pronto. Disse. Agora compra qualquer coisa, para disfarçarmos." |
| 10 | "Antes contava as moedas para saber quanto tinha. Agora conto para saber quanto posso dar. A conta é igual. Sabe melhor." |

---

## 5. Presentes

**Adora:** Pinça de Ouro, Pérola Negra, Ouro antigo · **Gosta:** gemas, Moeda Antiga ·
**Detesta:** lixo de pesca (Bota Velha, Lata), Gel de Slime, Ectoplasma. O resto é **neutro** (ver `docs/ITENS.md`, secção 11).
O que ele detesta mesmo é que regateies mais de 3 vezes no mesmo dia (ver o Serviço, na secção 10).

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "Para MIM?! Isto vale… não, não vou dizer quanto vale. Vale muito. Vale mais porque foste tu." · "Ai, o meu coração de mercador! Isto não vai para a banca. Isto vai para o Armazém. Para sempre." |
| Gosta | "Que bonito! Já estou a pensar no preço. Não vou vender. Mas é bom saber o preço." · "Obrigado, {freguês/freguesa}! A partir de hoje és {freguês/freguesa} preferid{o/a}. Os preços são iguais, mas o carinho não." |
| Neutro | "Oh. Obrigado. Vou… arranjar-lhe um cliente." · "Hmm! Um presente. Grátis. A palavra mais bonita do mundo, a seguir a 'lucro'." |
| Não gosta | "Ah. Isto é… difícil de vender. Muito difícil. Mas obrigado pela intenção. A intenção não se vende." |
| Detesta | "Uma lata. Vale zero. Já vendi coisas que valiam zero, mas eram MINHAS." · "Gel de Slime na mercadoria?! Tira isso! Os tecidos colam-se! Os fregueses colam-se!" |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Pinça de Ouro | "Ouro MACIÇO! De um caranguejo! Recusaste 6 000 ao Barão para ma dares a mim? …Vou chorar. Vou chorar ouro." |
| Pérola Negra | "Uma Pérola Negra… do fundo do mar. Sabes quantas vi na vida? Esta. Só esta. Vou dormir com ela debaixo da almofada." |
| Ouro antigo | "Ouro antigo! Olha para isto: tem mil anos e ainda brilha. Eu tenho quarenta e cinco e já não brilho tanto." |
| Moeda Antiga | 🎬 morde a moeda. "Verdadeira! De piratas! Vai para a minha coleção. Tenho trinta e uma. Agora trinta e duas." |
| Garra Dourada | "Uma garra da Toupeira Dourada! Então ela está bem e continua a cavar. …Fico contente. Não digas que fico contente." |
| Pá Dourada (a que ele te deu) | "A minha pá! Estás a devolver um presente? …Aceito. Revendo-a. Não, guardo-a. Não. Revendo. Guardo." |

---

## 6. Aniversário e festivais

**Aniversário (Verão, dia 3)** — é também o aniversário do **Tibério** (são gémeos):
- Sem presente: **Tobias** *(feliz)*: "Faço anos! E o meu irmão também, infelizmente. Ele diz que nasceu primeiro. Mentira. Ninguém sabe."
- Com presente que adora: **Tobias** *(feliz)*: "Um presente de anos que vale ouro! Literalmente! Este é o melhor aniversário dos últimos vinte. E tive muitos."
- Com outro presente: **Tobias** *(feliz)*: "Um presente! De graça! No meu dia! Hoje não regateio contigo. Bem… só um bocadinho."
- 🎬 Nesse dia chega sempre uma carta do Tibério. O Tobias lê-a em voz alta, sem querer:
  **Tobias** *(a ler)*: "'Parabéns a mim. E a ti, já agora. — T.'" · **Tobias** *(triste)*: "'Já agora.' Vinte anos de 'já agora'."
- Depois da missão N_TOBIAS_3: o Tibério desce a Ascendia nesse dia. Há um bolo na banca, cortado em fatias exatamente iguais (com régua).

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Flores! Vendo flores para o concurso. E flores para consolar quem perdeu o concurso. Vendo mais dessas." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Tobias** *(surpresa)*: "Eu? Dançar? Hoje não cobro. Mas aviso: danço como conto moedas. Depressa e mal." ⚙ dança · +100 amizade |
| F_02 Festival da Pesca | "Pescar? Eu não pesco. Compro peixe a quem pesca e vendo a quem não pesca. É a mesma coisa, mas sem minhocas." |
| F_03 Noite dos Espíritos | "Máscaras de abóbora, cinco moedas! Doces, uma moeda! Os fantasmas não pagam. Já tentei cobrar." |
| F_04 Festival da Estrela | "Amigo secreto! Calhou-me a Dona Marta. O que se dá a quem dá tudo? …Uma panela nova. Comprada a mim. Com desconto." |
| F_05 Dia da Subida | "Dia da Subida! Vendi trezentas bandeirinhas com a tua cara. Bem… com uma cara. Parecida. De longe." |
| F_06 Concurso da Casa | "Concurso da casa? Se ganhares, diz que os móveis são do Tobias. Se perderes, não digas nada." |
| F_07 Noite das Lanternas | "Eu não ponho lanternas. Eu vendo-as. …Hoje são de graça. Não digas a ninguém. Estragas-me a fama." |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`).

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `tobias_boss_javali_rei` | "O Javali-Rei! Ficaste com a presa? Não a vendas a outro. A outro não. A mim. Pago bem. Pago… razoável." |
| Ent Ancião (10) | `tobias_boss_ent_anciao` | "Dia da Subida! Bandeirinhas, fitas, apitos! Vendi tudo! Obrigado por teres vencido uma árvore." |
| Aranha-Mãe (15) | `tobias_boss_aranha_mae` | "Seda de aranha! A Elva paga, eu pago, toda a gente paga. A aranha é que não paga. Coitada." |
| Golem de Cristal (20) | `tobias_boss_golem_cristal` | "Casa nova! Cama, mesa, cadeiras, tapetes, estantes. Tenho tudo. Que coincidência maravilhosa." |
| Serpente do Lodo (25) | `tobias_boss_serpente_lodo` | "Cheiras a lodo. Não faz mal: o dinheiro não cheira. Mas lava as mãos antes de tocares na mercadoria." |
| Hidra do Pântano (30) | `tobias_boss_hidra_pantano` | "Uma hidra com várias cabeças! Se lhe vendesses chapéus, vendias logo uns cinco. Isso é que é um cliente!" |
| Escorpião Imperador (35) | `tobias_boss_escorpiao_imperador` | "Um escorpião com ferrão de OURO? E não o trouxeste? Partiste o ferrão e o meu coração." |
| Faraó Eterno (40) | `tobias_boss_farao_eterno` | "Um faraó com ouro até nas ligaduras! Diz-me que guardaste as ligaduras. Diz-me." |
| Yeti Ancião (45) | `tobias_boss_yeti_anciao` | "O Yeti tinha um colar com coisas de Jogadores mortos… Não, isso não compro. Há coisas que não se vendem." |
| Dragão de Gelo (50) | `tobias_boss_dragao_gelo` | "Metade da torre! Para festejar, vendo-te uma coisa a meio preço. Uma. Pequena. Esta colher." |
| Capitão Esqueleto (55) | `tobias_boss_capitao_esqueleto` | "Um capitão que contava ouro que não podia gastar… Isso dá que pensar. Não muito. Mas dá." |
| Leviatã (60) | `tobias_boss_leviata` | "Venceste o mar. A cidade está contente. Mas a cadeira do Kai na taberna continua vazia. Isso não se compra." |
| Ferreiro Infernal (65) | `tobias_boss_ferreiro_infernal` | "O Brom veio cá comprar um lenço. 'Para o fumo', disse ele. Dei-lho de graça. Não contes a ninguém." |
| Kai — salvo (68) | `tobias_boss_kai_salvo` | "O Kai voltou! Vou fazer uma promoção: 'Compre um, leve o Kai.' Ele não aceitou. Vou fazê-la na mesma." |
| Kai — vencido (68) | `tobias_boss_kai_vencido` | "Hoje não precisas de comprar nada. Fica aqui um bocado à sombra da banca. A banca é grande. Cabe toda a gente." |
| Titã de Magma (70) | `tobias_boss_tita_magma` | "Um titã de lava! Trouxeste Núcleo de Magma? O Gizmo paga o dobro. Eu pago o dobro do Gizmo menos metade." |
| Lich Bibliotecário (75) | `tobias_boss_lich_bibliotecario` | "Livros! O Velho Fausto vai querer todos. Eu compro-tos e vendo-lhos. Toda a gente fica feliz. Eu mais." |
| Rei Sem Coroa (80) | `tobias_boss_rei_sem_coroa` | "A Coroa do Reino! Não a quero comprar. Só quero segurar. Um bocadinho. Para sentir o peso." |
| Grifo Real (85) | `tobias_boss_grifo_real` | "Uma pena de grifo! Quanto vale? Não sei. Ninguém nunca vendeu uma. Seria o primeiro! Que emoção!" |
| Serafim Caído (90) | `tobias_boss_serafim_caido` | "Estás com cara de quem viu uma coisa muito grande. Hoje não te vendo nada. Toma uma maçã. Esta é grátis." |
| Guardião do Tempo (95) | `tobias_boss_guardiao_tempo` | "O meu irmão escreveu: 'Diz-lhe que tenho poções no 91, se precisar.' Ele não escreve 'diz-lhe' a ninguém. Gosta de ti." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — A canção das moedas

| | |
|---|---|
| ID | `cena_tobias_2` |
| Quando | 2 ❤️ · passar pelo Mercado entre as 19:00 e as 21:00 (depois de fechar) |
| Onde | Mercado, banca do Tobias (só uma lanterna acesa) |
| Quem | herói, Tobias |
| Música | `ascendia_noite` (versão com caixinha de música) |

🎬 O Mercado está vazio. Na banca do Tobias há uma lanterna e pilhas de moedas. Ele conta-as e canta baixinho, a abanar a cabeça.

- **Tobias** *(feliz, a cantar)*: "♪ Uma moeda, duas moedas, três moedas a dançar… quatro no bolso, cinco no colete, seis para a mãe guardar… ♪"
- 🎬 Vê-te. Uma moeda cai e rola até aos teus pés.
- **Tobias** *(surpresa)*: "Há quanto tempo estás aí? Não, não respondas. Eu não estava a cantar. Estava a contar alto. Com música."
- **Tobias** *(normal)*: "É a canção das moedas. O meu pai ensinou-a a mim e ao meu irmão, para aprendermos a contar."
- **Tobias** *(feliz)*: "O Tibério aprendeu a contar. Eu aprendi a cantar. Por isso é que ele tem jeito para os números. Diz ele."
- 🎬 Torce o bigode.
- **Tobias** *(normal)*: "Agora conto todas as noites. Se não cantar, engano-me. Se cantar, as moedas parecem mais."

▶ **"Canta outra vez!"**
▶ **"Posso ajudar a contar?"**
▶ **Apanhar a moeda e devolvê-la.**

- *(Canta)* **Tobias** *(feliz)*: "Só se cantares comigo. …Não? Então canto eu. A versão curta. A longa tem quarenta moedas." ⚙ +30
- *(Ajudar)* **Tobias** *(surpresa)*: "Ajudar a contar? Normalmente querem ajudar a GASTAR. Senta-te. Tu contas as de cobre, eu as de ouro. A confiança tem limites." ⚙ +30
- *(Devolver)* 🎬 O Tobias morde a moeda. **Tobias** *(normal)*: "Verdadeira. E tu também. Muita gente ficava com ela. Fica com ela. Não. Fica. …Fica." ⚙ +1 ouro
- **Tobias** *(feliz)*: "Pronto. Agora sabes um segredo meu. Um pequeno. Os grandes custam mais."

⚙ 5% de desconto na loja do Tobias.

### ❤️ 4 — O Senhor Ninguém

| | |
|---|---|
| ID | `cena_tobias_4` |
| Quando | 4 ❤️ · Domingo, entrar no Bairro Baixo entre as 18:00 e as 20:00 |
| Onde | Bairro Baixo, beco do poço velho |
| Quem | herói, Tobias, Mia, crianças do bairro |
| Música | `amizade` |

🎬 Um vulto de capuz empurra um carrinho de mão cheio de pães, maçãs e um queijo. Pára no beco e bate três vezes numa porta velha. Crianças saem a correr.

- **Mia** *(feliz)*: "É o Senhor Ninguém! Trouxe pão! E maçãs! E isto é… é QUEIJO!"
- 🎬 O vulto põe um dedo nos lábios. O capuz escorrega. Por baixo aparece um bigode enrolado.
- 🎥 A câmara aproxima-se devagar do bigode.
- **Tobias** *(surpresa)*: "…Não sou eu."
- **Tobias** *(normal)*: "Sou outro senhor de bigode. Há muitos. Está na moda."
- **Mia** *(normal)*: "É o senhor Tobias. Toda a gente sabe. Só fingimos que não, porque ele fica contente."
- 🎬 A Mia leva duas maçãs e foge. As crianças vão atrás dela.
- **Tobias** *(triste)*: "'Toda a gente sabe.' Anos de capuz para nada."
- **Tobias** *(normal)*: "É o que não vendi durante a semana. Coisas que se iam estragar. …Está bem, comprei metade hoje de manhã."
- **Tobias** *(normal)*: "O meu pai dizia: 'Um mercador que não dá nada nunca é rico.' Demorei muito a perceber o que ele queria dizer."

▶ **"O teu segredo está guardado."**
▶ **"Porque é que escondes isto?"**
▶ **"Posso ajudar no domingo que vem?"**

- *(Segredo)* **Tobias** *(feliz)*: "Ótimo. Se contares a alguém, digo que és doid{o/a}. E aumento-te os preços. As duas coisas." ⚙ +30
- *(Porquê)* **Tobias** *(normal)*: "Porque se souberem que dou, toda a gente me pede desconto. E a fama de forreta, {freguês/freguesa}, dá muito trabalho a manter."
- *(Ajudar)* **Tobias** *(surpresa → feliz)*: "De graça? …Está bem. Mas trazes capuz. Dois capuzes num beco é mais discreto. Acho eu." ⚙ +30
- 🎬 O Tobias tira do colete uma moeda de latão, gasta, com um furo no meio.
- **Tobias** *(normal)*: "Toma. É a moeda da sorte do meu pai. Ele deu uma a mim e outra ao Tibério."
- **Tobias** *(feliz)*: "É falsa. É de latão. Mas dá sorte na mesma. Dá mais sorte do que as verdadeiras."

⚙ Recebe a **Moeda da Sorte** (acessório: +5% de ouro dos monstros e baús; não se pode vender).
⚙ A partir daqui, ao Domingo das 18:00 às 20:00, podes ajudar o Tobias a distribuir o pão no Bairro Baixo (+20 amizade, 1 vez por semana).

### ❤️ 6 — A balança do pai

| | |
|---|---|
| ID | `cena_tobias_6` |
| Quando | 6 ❤️ · `missao(N_TOBIAS_1) == concluida` · segunda-feira, passar pelo Mercado entre as 7:00 e as 10:00 |
| Onde | Mercado, banca do Tobias |
| Quem | herói, Tobias, aldeões (a olhar) |
| Música | `ascendia_dia` → `tristeza` |

🎬 O Tobias está vermelho como um tomate, com uma carta na mão. Os aldeões à volta afastam-se devagar.

- **Tobias** *(zangado)*: "ELE VAI VENDER A BALANÇA! A balança do pai! A quem der mais! Ouve isto. OUVE!"
- **Tobias** *(a ler)*: "'Irmão mais novo: vou pôr a balança do pai no leilão do Gaspar, em Vagar. Tu não terias dinheiro para ela. — T.'"
- **Tobias** *(zangado)*: "Mais novo! MAIS NOVO! Nascemos no mesmo dia! A nossa mãe dizia que nascemos de mãos dadas!"
- 🎬 Senta-se num caixote. O caixote range.
- **Tobias** *(triste)*: "O nosso pai, o Teodoro, tinha esta banca. Quando morreu, deixou um papel: 'A banca fica para o meu filho mais velho.'"
- **Tobias** *(triste)*: "Mas ninguém sabia qual de nós era o mais velho. A parteira já tinha morrido. A mãe dizia sempre: 'os dois'."
- **Tobias** *(normal)*: "Eu acordei mais cedo e abri a banca. Ele chegou dez minutos depois. Discutimos. Puxámos o papel. Rasgou-se ao meio."
- **Tobias** *(normal)*: "Ele pôs a mochila às costas e disse: 'Fica com a banca. Eu vou vender onde ninguém vende.' Foi para a torre."
- **Tobias** *(triste)*: "Isso foi há vinte anos. Desde aí, só cartas. Todas as semanas. Todas a dizer que vende mais do que eu."
- **Tobias** *(normal)*: "A balança ficou com ele. Era a única coisa do pai que eu queria. Mais do que a banca. …Não lhe digas isto."

▶ **"Escreve-lhe a dizer isso."**
▶ **"Eu vou falar com ele."**
▶ **"Talvez ele também tenha saudades."**

- *(Escreve)* **Tobias** *(zangado)*: "Escrever ao Tibério que tenho saudades? Prefiro vender tudo a metade do preço!" 🎬 Pausa. "…Quase prefiro."
- *(Eu vou)* **Tobias** *(surpresa)*: "Tu? Falar com aquela mula de bigode liso? …Farias isso? Por mim?" ⚙ +30
- *(Saudades)* **Tobias** *(triste)*: "Ele? …Escreve-me todas as semanas há vinte anos. Ninguém escreve tanto a quem não tem saudades." ⚙ +30
- **Tobias** *(normal)*: "Está bem. Vai. Leva-lhe esta carta. Está muito zangada. Mas leva-a."

⚙ Missão **N_TOBIAS_3 Irmãos** iniciada. O Tobias aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — O Armazém

| | |
|---|---|
| ID | `cena_tobias_8` |
| Quando | 8 ❤️ · passar pelo Mercado entre as 19:00 e as 21:00 |
| Onde | Mercado → cave por baixo da banca (alçapão) |
| Quem | herói, Tobias |
| Música | `ascendia_noite` → `amizade` |

🎬 O Tobias olha para os dois lados, afasta um tapete atrás da banca e abre um alçapão.

- **Tobias** *(normal)*: "Desce. Cuidado com o terceiro degrau. Morde. É uma maneira de falar. Mas range muito."
- 🎥 A câmara desce com o herói: uma cave enorme, muito maior do que a banca. Prateleiras até ao teto, baús, armaduras antigas, um barco pequeno pendurado, um lustre de cristal, uma estátua de javali.
- **Tobias** *(feliz)*: "O Armazém! Vinte e cinco anos de compras. Tudo o que achei bonito, raro ou estranho demais para vender."
- **Tobias** *(normal)*: "Esta espada é de um Jogador que voltou para casa… sem a espada. Esta é uma bota de gigante. Só uma. Nunca encontrei a outra."
- 🎬 Pega num relógio de bolso parado.
- **Tobias** *(normal)*: "Isto é de uma senhora que me vendeu tudo para pagar a viagem lá para cima. Prometi guardá-lo até ela voltar."
- **Tobias** *(triste)*: "Muita coisa aqui é assim. Coisas de gente que subiu. Não as vendo. Fico à espera."
- **Tobias** *(normal)*: "O meu irmão diz que compro tudo porque sou ganancioso. Talvez. Ou talvez não goste que as coisas se percam."
- 🎬 Ao fundo há uma porta de ferro com três fechaduras.

▶ **"O que há atrás daquela porta?"**
▶ **"Isto é um museu, Tobias."**
▶ **"Obrigad{o/a} por me mostrares."**

- *(Porta)* **Tobias** *(normal)*: "Ah. Isso. As coisas MESMO raras. Lendárias. Um dia mostro. Hoje já te mostrei o coração. Chega por um dia." ⚙ +30
- *(Museu)* **Tobias** *(feliz)*: "Um museu onde tudo tem preço! O melhor tipo de museu que há." ⚙ +30
- *(Obrigado)* **Tobias** *(triste → feliz)*: "Não agradeças. Ninguém desce aqui. Nem o meu irmão desceu. …Está bem, agradece. Sabe bem."

⚙ 15% de desconto. O Tobias passa a mandar **cartas** (1 por semana) com presentes: uma gema ao acaso, Moeda Antiga ×3 ou um móvel do Armazém.

### ❤️ 10 — A Chave do Armazém

| | |
|---|---|
| ID | `cena_tobias_10` |
| Quando | 10 ❤️ · `missao(N_TOBIAS_3) == concluida` · Domingo, passar pelo Mercado entre as 8:00 e as 12:00 |
| Onde | Mercado, banca "Tobias & Tibério" → Armazém |
| Quem | herói, Tobias, Tibério |
| Música | `amizade` |

🎬 Os gémeos estão lado a lado atrás da banca: um de bigode enrolado, o outro de bigode liso. Discutem baixinho.

- **Tibério** *(normal)*: "Dizes tu."
- **Tobias** *(normal)*: "Não, dizes tu. Hoje és tu o mais velho."
- **Tibério** *(normal)*: "Eu sou o mais velho à segunda, quarta e sexta. Hoje é domingo."
- **Tobias** *(zangado)*: "E ao domingo é quem?"
- **Tibério** *(feliz)*: "Ao domingo é quem tiver o bigode mais bonito. És tu. Fala."
- 🎬 O Tobias torce o bigode, todo orgulhoso. Vira-se para ti.
- **Tobias** *(feliz)*: "{nome}! Anda cá. Desce connosco."

🎬 Descem ao Armazém e vão até à porta de ferro das três fechaduras.

- **Tobias** *(normal)*: "Três fechaduras. Uma chave minha, uma chave do Tibério…"
- **Tibério** *(normal)*: "…e uma terceira, que mandámos fazer esta semana. Foi cara. Ele quis regatear com o serralheiro. Não deixei."
- 🎬 O Tobias tira do colete uma chave dourada.
- **Tobias** *(feliz)*: "É tua. A Chave do Armazém."
- **Tobias** *(normal)*: "Lá dentro estão as coisas lendárias. Não as vendo a ninguém. Vendo-as a ti. Não de graça, que eu continuo a ser o Tobias."
- **Tibério** *(feliz)*: "Mas a preço de família. Que é igual ao preço normal, mas dito com carinho."
- **Tobias** *(surpresa)*: "Essa frase é minha!"
- **Tibério** *(feliz)*: "Agora é das duas lojas. Lemos o testamento, lembras-te? Metade de tudo."
- 🎬 Os dois riem-se ao mesmo tempo, da mesma maneira, com a barriga a tremer.
- **Tobias** *(triste → feliz)*: "Sem ti, {nome}, eu ainda estava a escrever cartas zangadas. E ele a lê-las a rir. …Ele ria-se, sabias?"
- **Tibério** *(normal)*: "Todas as semanas. Guardei-as todas. Tenho uma mochila só para elas."

▶ **"Agora são uma família outra vez."**
▶ **"Isto tem desconto?"**

- *(Família)* **Tobias** *(feliz)*: "Três. Uma família de três. És péssim{o/a} a regatear, mas contas."
- *(Desconto)* **Tobias e Tibério** *(feliz, ao mesmo tempo)*: "NÃO." 🎬 Riem-se outra vez.

⚙ Recebe a **Chave do Armazém**: abre a loja secreta de itens lendários (ver o Serviço, secção 10). Título *Sóci{o/a} de Honra*.
⚙ O Tobias passa a ter a fala `tobias_dia_66`.

---

## 9. Missões

### N_TOBIAS_1 — Entrega ao Tibério (0 ❤️, `andar_maximo >= 5`)

- **Pedir** — **Tobias** *(feliz)*: "{freguês/freguesa}! Negócio! Esta caixa tem de chegar à Zona Segura do andar 5. Ao meu irmão. Pago duzentas moedas. Duzentas! Estou doido."
  ▶ **"Combinado!"** ⚙ missão iniciada ·
  ▶ **"O que tem a caixa?"** → "Mercadoria. Mercadoria séria. Não abras. Não cheires. Não abanes." ⚙ missão iniciada ·
  ▶ **"Agora não."** → "Está bem. A caixa espera. A caixa é paciente. Eu não sou."
- **Durante** — **Tobias**: "Ainda não entregaste? Isso tem mercadoria que se estraga. Não muito. Mas estraga-se."
- **No andar 5 (Zona Segura)** — 🎬 ao pé da fogueira está um homem igual ao Tobias, mas de bigode liso, virado para baixo, e com uma mochila do tamanho de um armário.
  - **Tibério** *(normal)*: "Deixa-me adivinhar. O meu irmão mandou-te com uma caixa e disse 'mercadoria'."
  - 🎬 Abre a caixa. Está cheia de bolachas.
  - **Tibério** *(normal)*: "Bolachas de canela. A receita da nossa mãe. Ele manda-mas todas as estações e diz que são para eu vender."
  - **Tibério** *(normal)*: "Nunca vendi nenhuma." 🎬 Come uma. "Diz-lhe que estavam moles."
  - **Tibério** *(feliz, de boca cheia)*: "…Não estavam. Mas diz-lhe."
  - **Tibério** *(normal)*: "Leva-lhe a resposta. Está zangada. As minhas cartas estão sempre zangadas. É tradição."
  - ⚙ Recebe a **Carta do Tibério** (item de missão).
- **Entregar** — 🎬 o Tobias abre a carta e lê em voz alta.
  - **Tobias** *(a ler)*: "'Bolachas moles. Preços altos. Bigode feio. — T.'"
  - **Tobias** *(zangado → feliz)*: "MOLES?! …Comeu-as todas, não comeu? Comeu. Ele come sempre todas."
  - **Tobias** *(feliz)*: "Toma: duzentas. Contadas duas vezes e cantadas uma." ⚙ 200 ouro · +100 amizade
  - ⚙ A partir daqui chegam as **Cartas do Tibério** à segunda-feira (secção 10).

### R2_11 — A Toupeira Dourada (`andar_maximo >= 11`)

- **Pedir** — **Tobias** *(feliz)*: "Já ouviste falar da Toupeira Dourada? Pelo de OURO! Nas minas! Quero-a na banca, numa gaiola de ouro. Os fregueses vão vir de todo o lado!"
  - **Tobias** *(normal)*: "Viva, ouviste? VIVA. Tonta, mas viva. A gaiola já está feita. Custou uma fortuna. Bem… metade de uma fortuna."
  ▶ **"Vou apanhá-la."** ⚙ missão iniciada ·
  ▶ **"Coitada da toupeira…"** → "Coitada? Vai viver numa gaiola de OURO! Vai ser a toupeira mais rica da torre!" ⚙ missão iniciada
- **Onde** — qualquer andar da região 2 (aparece pouco). Foge para debaixo do chão e tens 30 s: atordoa-a e ela fica apanhada (ver `docs/regioes/r02_cavernas.md`, monstros com nome).
- **Durante** — **Tobias**: "Já a viste? Procura nos túneis mais escuros. O ouro gosta do escuro. Eu também, quando conto."
- **Entregar** — 🎬 a toupeira, tonta, numa gaiola dourada em cima da banca. Uma multidão à volta.
  - **Tobias** *(feliz)*: "Olha para isto! Três clientes em cinco minutos! Ela é um génio do comércio!"
  - **Tobias** *(normal)*: "Toma. Mandei fazer uma pá dourada para combinar com a gaiola. Fica-te melhor a ti. E as mil moedas. Contadas e cantadas."
  - ⚙ **Pá Dourada** · 1 000 ouro · +100 amizade
- **No dia seguinte** — ver `tobias_toupeira_fugiu` (secção 10).

### N_TOBIAS_3 — Irmãos (6 ❤️, depois da cena de 6 ❤️)

**Passos:**
1. Levar a **carta zangada** ao Tibério (o mapa mostra a Zona Segura onde ele está nesse dia; ao princípio é a do andar 5).
2. Ouvir a versão do Tibério.
3. Ir à **Câmara** buscar a cópia do **testamento do Teodoro** (o Governador Aldric guarda os papéis da cidade).
4. Convencer o Tobias a ir à **Zona Segura do andar 1** (o Tibério não desce à cidade e o Tobias tem medo da torre: o andar 1 é o meio-termo).
5. A conversa à fogueira (cena com escolhas).

**Passo 1–2 — O Tibério**
- **Tibério** *(normal)*: "Uma carta dele fora da segunda-feira? Deve estar furioso." 🎬 Lê. "Chamou-me 'mula' três vezes. Está a melhorar. O ano passado eram sete."
- **Tibério** *(normal)*: "A balança? Nunca a vendia. Escrevi aquilo para ver se ele subia cá acima para a buscar. Vinte anos. Nunca subiu."
- **Tibério** *(triste)*: "No dia da banca, eu cheguei dez minutos atrasado porque fui buscar pão quente. Para os dois. Para o pequeno-almoço."
- **Tibério** *(triste)*: "Quando cheguei, ele estava a gritar 'É MINHA!'. Fiquei ali com o pão na mão. Comi-o todo no caminho para a torre."

▶ **"Ele tem saudades da balança."**
▶ **"Ele tem saudades tuas."**

- *(Balança)* **Tibério** *(normal)*: "A balança. Claro. Sempre a balança."
- *(Tuas)* **Tibério** *(surpresa)*: "…Ele disse isso? Não por palavras, pois não? Eu sei ler um bigode."
- **Tibério** *(normal)*: "O papel rasgou-se ao meio nesse dia. Eu fiquei com a metade de baixo e perdia-a na torre. Nunca soube o que dizia."

**Passo 3 — A Câmara**
- **Aldric** *(nervoso)*: "Testamentos… T… T… Teodoro! Aqui está. Carimbado em triplicado. Ninguém o veio buscar em vinte anos!"
- **Aldric** *(feliz)*: "Leve uma cópia. Leve duas. Leve três, que é para isso que existe o triplicado."
- ⚙ Recebe o **Testamento do Teodoro** (item de missão). O herói não o lê: está fechado com o selo da Câmara.

**Passo 4 — Convencer o Tobias**
- **Tobias** *(surpresa)*: "Na torre? EU? …Só se fores comigo. E se eu levar três poções. E o colete. O colete dá sorte."

**Passo 5 — A fogueira**

🎬 Zona Segura do andar 1, ao fim da tarde. A fogueira estala. O Tobias de um lado, agarrado a três poções. O Tibério do outro, com a mochila. Não se olham.

- **Tobias** *(zangado)*: "Bigode liso."
- **Tibério** *(normal)*: "Bigode de saca-rolhas."
- **Tobias** *(zangado)*: "Ladrão de balanças!"
- **Tibério** *(zangado)*: "Ladrão de bancas!"

▶ **"Parem os dois!"**
▶ **Mostrar a Moeda da Sorte.** *(certa)*
▶ **"O Tobias tem razão."** *(errada)*
▶ **"O Tibério tem razão."** *(errada)*

- *(Parem)* **Tobias e Tibério** *(ao mesmo tempo)*: "Ele é que começou!" 🎬 Olham um para o outro, irritados por terem falado ao mesmo tempo.
- *(Moeda)* 🎬 O Tibério fica quieto. **Tibério** *(surpresa)*: "…Deste-lhe a moeda do pai?" · **Tobias** *(normal)*: "Dei. E tu? Ainda tens a tua?"
  🎬 O Tibério tira do bolso uma moeda igual, gasta de tanto ser apertada. **Tibério** *(triste)*: "Nunca a larguei."
- *(Razão a um)* O outro *(zangado)*: "Claro! Até tu estás do lado dele!"

🎬 Dás o testamento.

▶ **"Leiam os dois. Ao mesmo tempo."** *(certa)*
▶ **Dar o testamento ao Tobias.** *(errada)*
▶ **Dar o testamento ao Tibério.** *(errada)*

- *(Dar a um)* Quem o recebe lê só a primeira linha: "'A banca fica para o meu filho mais velho.' VÊS?!" · o outro: "Isso prova que é MINHA!" 🎬 Tens de lhes tirar o papel e pô-lo entre os dois.
- 🎬 Os dois inclinam-se sobre o papel, testa com testa.
- **Tobias e Tibério** *(a ler, ao mesmo tempo)*: "'Deixo a minha banca ao meu filho mais velho.'"
- **Tobias e Tibério** *(a ler)*: "'Como nunca soube qual dos dois é, o mais velho será o primeiro que pedir desculpa ao outro.'"
- **Tobias e Tibério** *(a ler)*: "'E a balança fica para pesar desculpas, não moedas. — Teodoro.'"
- 🎬 Silêncio. A fogueira estala.

▶ **"Então? Quem é o mais velho?"** *(certa)*
▶ **"Façam as pazes, por favor."** *(certa)*
▶ **"Dividam: metade para cada um."** *(errada)*

- *(Metade)* **Tobias** *(zangado)*: "Metade da balança? Serra-se?!" · **Tibério** *(triste)*: "Metade de um pai não existe."
- 🎬 Os dois abrem a boca ao mesmo tempo.
- **Tobias e Tibério** *(ao mesmo tempo)*: "Desculpa!"
- **Tobias** *(zangado)*: "Eu disse primeiro!"
- **Tibério** *(zangado)*: "Disseste ao mesmo tempo!"
- 🎬 Pausa. Começam a rir. Os dois da mesma maneira.
- **Tibério** *(feliz)*: "Então somos os dois o mais velho."
- **Tobias** *(feliz, a chorar)*: "Como a mãe dizia. De mãos dadas."
- 🎬 Abraçam-se. As poções do Tobias caem. Uma parte-se.
- **Tobias** *(normal)*: "…Quem paga a poção?"
- **Tibério** *(normal)*: "Tu. Foste tu que a trouxeste."
- 🎬 Discutem. Mas a sorrir.

> **Regra**: se escolheres **2 ou mais respostas erradas**, os dois vão-se embora zangados antes do fim:
> `[Sistema] Os irmãos foram embora. Tenta outra vez amanhã.` O passo 5 repete-se no dia seguinte.

- **Entregar** (no dia seguinte, no Mercado) — 🎬 a banca tem uma placa nova: **"TOBIAS & TIBÉRIO — Desde sempre"**. A balança do pai está no meio do balcão.
  - **Tobias** *(feliz)*: "{nome}! Olha a placa! Ele vem ao domingo de manhã. O resto da semana anda lá em cima. Juntámos tudo: lojas, contas, fregueses."
  - **Tobias** *(triste → feliz)*: "E baixámos os preços. Cinco por cento! Em todo o lado! Estou a sofrer. Mas é um sofrimento bom."
  - ⚙ +200 amizade · preços **−5% em todo o lado** · flag `irmaos_juntos` · as Cartas do Tibério passam a ser as "depois das pazes"

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `tobias_estado_vida` | `vida_pct < 30` | zangado | "Com essa vida não te vendo nada. Vendo-te uma Poção de Vida. Bebe-a aqui. Agora. Pagas depois. Mas pagas." |
| `tobias_estado_maldito` | `estado(amaldicoado)` | surpresa | "Essa nuvem roxa espanta-me os fregueses. A Irmã Célia tira isso. Eu só vendo Água Benta. A sessenta." |
| `tobias_estado_cansado` | `estado(cansado)` | normal | "Tens olheiras de quem contou moedas a noite inteira. Eu conheço essa cara. Vai dormir." |
| `tobias_estado_molhado` | `estado(encharcado)` | zangado | "Não toques nos tecidos! Molhad{o/a} assim, só te posso vender guarda-chuvas. Queres um? Hoje estão caros." |
| `tobias_estado_sapo` | `estado(sapo)` | surpresa | "Um sapo quer comprar? Já vendi a sapos, na Vila Coaxa. Regateiam como ninguém. …Espera. Essa mochila é d{o/a} {nome}?" |
| `tobias_arma_nova` | arma equipada pela 1.ª vez com raridade Épica ou melhor | feliz | "Que arma! Quanto queres por ela? Não vendes? Toda a gente vende. Um dia vendes. E eu estou cá." |
| `tobias_animal` | `animal != nenhum` (1.ª vez) | feliz | "Um animal! Come muito? A partir de hoje vendo coleiras. Coleiras de luxo. Para esse aí, a primeira é quase grátis." |
| `tobias_comp_mia` | `companheiro(mia)` | feliz | "Mia! Aventureira a sério! Toma, uma maçã para o caminho. Não é do Senhor Ninguém. É minha. Quer dizer… pronto." |
| `tobias_comp_kai` | `companheiro(kai)` | feliz | "O Kai e {nome}! Dois clientes pelo preço de dois. Não há promoção. Mas fica bonito dizer." |
| `tobias_comp_gorvan` | `companheiro(gorvan)` | surpresa | "Mestre Gorvan, a subir outra vez? Leve o pente. De graça. …É uma piada. Não me olhe assim." |
| `tobias_classe` | 1.ª conversa depois de escolher classe | feliz | "{classe}! Tenho exatamente o que um {classe} precisa. Não tenho. Mas amanhã tenho." |
| `tobias_toupeira_fugiu` | dia seguinte a entregar R2_11 (1 vez) | zangado | ver abaixo |

**`tobias_toupeira_fugiu`** — 🎬 a gaiola dourada está vazia; há um buraco no chão, mesmo por baixo da banca.
- **Tobias** *(zangado)*: "FUGIU! Cavou pelo fundo da gaiola!"
- **Tobias** *(normal)*: "…A gaiola não tinha fundo. Um fundo de ouro custava o dobro. Pensei: 'Para que é que uma toupeira quer chão?'"
- **Tobias** *(triste → feliz)*: "Pensando bem, ela parecia triste ali dentro. Ainda bem que fugiu. NÃO digas a ninguém que eu disse isto."

### Cartas do Tibério

Depois da missão N_TOBIAS_1, à **segunda-feira de manhã** (7:00–12:00) a 1.ª conversa com o Tobias é a carta da semana
(entra na prioridade como "Estado", passo 6 do `README.md`). O Tobias lê-a em voz alta, quer queiras quer não.
As cartas saem por ordem; quando acabam, voltam ao princípio. Depois de N_TOBIAS_3 só saem as cartas 07 a 09.

| ID | Condição | Carta (o Tobias a ler) | Reação do Tobias |
|---|---|---|---|
| `tobias_carta_01` | — | "'Irmão mais novo: vendi quarenta tochas no andar 11. No escuro, pagam o que for. Tu vendes tochas ao sol. — T.'" | *(zangado)* "Mais novo! MAIS NOVO! …E eu não vendo tochas ao sol. Vendo-as ao fim da tarde. É diferente." |
| `tobias_carta_02` | — | "'Tobias: um freguês perguntou-me se eu era o irmão bonito. Disse que sim. Não menti. — T.'" | *(zangado)* "Somos IGUAIS! Somos gémeos! …Bigode liso não é bigode. É uma sobrancelha que caiu." |
| `tobias_carta_03` | — | "'Soube que tentaste vender um pente para carecas. Eu vendi um guarda-chuva num andar onde não chove. Empate. — T.'" | *(surpresa)* "Um guarda-chuva sem chuva é uma sombra portátil. Isso é genial. …Odeio quando ele é genial." |
| `tobias_carta_04` | `andar_maximo >= 5` | "'Irmão: o Jogador nº 10 000 passou por cá e comprou-me três poções. Pagou sem regatear. Estás a ensiná-lo mal. — T.'" | *(zangado)* "Não regateaste com ELE?! Comigo regateias e a ele pagas tudo? {Traidor/Traidora}!" |
| `tobias_carta_05` | `estacao == inverno` | "'Faz frio nas Zonas Seguras. A fogueira é de graça, por isso ninguém lhe dá valor. Como a ti. — T.'" | *(triste)* "…Ele está com frio. Vou mandar-lhe um cachecol. Não. Sim. Diz que é do Mercado. Não é meu." |
| `tobias_carta_06` | `coracoes(tobias) >= 4` | "'Tobias: hoje dei a última poção a um rapaz que chorava. Não lhe cobrei. Não contes a ninguém. — T.'" | *(surpresa → feliz)* "Ele também?! Ele TAMBÉM dá coisas às escondidas? …Somos mesmo gémeos. Que desgraça." |
| `tobias_carta_07` | `flag(irmaos_juntos) && missao(H_22) == concluida` | "'Mano: vendi tudo no andar 91. Lá em cima pagam o triplo. Manda poções. E bolachas. Sobretudo bolachas. — T.'" | *(feliz)* "'Mano'! Escreveu 'mano'! Vinte anos de 'irmão mais novo' e agora 'mano'!" |
| `tobias_carta_08` | `flag(irmaos_juntos)` | "'Tobias: hoje um freguês disse que eu me pareço contigo. Não me zanguei. Devo estar a ficar velho. — T.'" | *(feliz)* "Velho! Se ele está velho, eu também estou. …Ninguém sabe quem é o mais velho. Que bom." |
| `tobias_carta_09` | `flag(irmaos_juntos)` | "'Irmão: perguntaram-me quem é o melhor mercador da torre. Disse o teu nome. Não acreditaram. Eu também não. — T.'" | *(surpresa → feliz)* "Disse o MEU nome? Antes do dele?" 🎬 Assoa-se ao lenço. "É pó. Há muito pó no Mercado." |

### Serviço — Loja

O que a loja vende e a que preço está em `docs/LOJAS.md`, secção 2.1. A loja geral muda todos os dias às 6:00; os **itens raros** mudam de 3 em 3 dias.
Com a melhoria **Mercado Coberto** (ver `docs/CIDADES.md`, secção 1.4) há mais 4 itens raros.

**Regatear** (botão no ecrã da loja, antes de comprar; regras em `docs/LOJAS.md`, secção 2.1): 40% + 5% por coração de baixar 10%.
Se falhar, esse item fica 5% mais caro até amanhã. **Mais de 3 vezes no mesmo dia: −30 de amizade** cada vez.

| ID | Quando | Emoção | Fala | ⚙ |
|---|---|---|---|---|
| `tobias_serv_abrir_1` | abrir a loja de manhã (7:00–12:00) | feliz | "Banca aberta! Mercadoria fresca de hoje! O que vai ser, {freguês/freguesa}?" | abre a loja |
| `tobias_serv_abrir_2` | abrir a loja à tarde (12:00–19:00) | normal | "Ainda há coisas boas. As melhores já foram, mas as segundas melhores são ótimas." | abre a loja |
| `tobias_serv_raros` | abrir a loja num dia em que os raros mudaram | feliz | "Dia de raros! Tirei o pano há bocado. Olha. Não toques. Olha. Agora podes tocar, se fores pagar." | separador **Raros** com "!" |
| `tobias_serv_raros_coberto` | 1.ª vez depois da melhoria Mercado Coberto | feliz | "Com telhado novo cabem mais quatro raridades! O Governador fez uma coisa útil. Escreve a data." | +4 itens raros |
| `tobias_serv_comprar_1` | comprar | feliz | "Excelente escolha! Toda a gente diz isto, mas eu digo com o coração." | — |
| `tobias_serv_comprar_2` | comprar 1 000 ouro ou mais de uma vez | feliz | "Tlim-tlim-tlim! Volta sempre. Volta amanhã. Volta já, se quiseres." | — |
| `tobias_serv_comprar_movel` | comprar um móvel | normal | "Uma cadeira! Uma casa sem cadeiras é um sítio onde se está de pé." | — |
| `tobias_serv_vender_1` | vender | normal | "Trinta por cento. É o preço justo. Justo para mim, mas justo." | recebe 30% do preço |
| `tobias_serv_vender_2` | vender um item raro ou melhor | surpresa | "Isto… isto vale muito. Não te digo quanto. Mas pago-te bem. Razoavelmente bem." | recebe 30% do preço |
| `tobias_serv_vender_3` | vender lixo de pesca | normal | "Uma bota velha. Compro. Não sei porquê. Alguém há de ter um pé só." | — |
| `tobias_serv_vender_missao` | tentar vender um item de missão | normal | "Isso é de uma missão. Cheira a promessa. As promessas não se compram. Pelo menos estas." | não deixa vender |
| `tobias_serv_recomprar` | abrir o separador Recomprar | normal | "Arrependeste-te? Toda a gente se arrepende. Por isso guardo tudo até amanhã." | — |
| `tobias_serv_regatear_ok` | regatear e conseguir | feliz | "Ai, o meu coração de mercador! Está bem. Está BEM. Leva. Mas não contes a ninguém." | desconto nesse item |
| `tobias_serv_regatear_nao` | regatear e falhar | normal | "Hmm… não. Esse é o preço. E agora, por teimosia, fica um bocadinho mais caro. Até amanhã." | esse item +5% até amanhã |
| `tobias_serv_regatear_3` | 3.ª vez no dia | zangado | "Terceira vez hoje. O bigode já me está a tremer. Cuidado." | aviso (ainda sem perda) |
| `tobias_serv_regatear_4` | 4.ª vez ou mais no dia | zangado | "Chega! Estás a abusar da minha generosidade! Regatear é uma arte, não é uma tortura. Volta amanhã." | −30 amizade (cada vez) |
| `tobias_serv_sem_ouro` | comprar sem ouro suficiente | normal | "Sem ouro? Então hoje és visita. As visitas olham. Olha à vontade. Olhar é grátis. Por enquanto." | `sis_sem_ouro` |
| `tobias_serv_mochila` | comprar com a mochila cheia | surpresa | "A mochila não fecha! Vende-me qualquer coisa primeiro. Assim ficamos os dois contentes." | `sis_mochila_cheia` |
| `tobias_serv_fechado` | falar com ele fora das 7:00–19:00 (na Taberna ou em casa) | normal | "Fechado! A banca dorme. Eu não, mas a banca sim. Volta às sete." | não abre a loja |
| `tobias_serv_domingo` | Domingo depois das 12:00 | normal | "Domingo à tarde a banca está fechada. Porquê? …Assuntos. Coisas. Volta amanhã." | não abre a loja |
| `tobias_serv_midas` | `skill_unica == mao_de_midas` (1.ª compra do dia) | feliz | "Toca no meu ouro antes de pagares. Para ver se cresce. …Não cresceu. Paga na mesma." | — |
| `tobias_serv_irmaos` | `flag(irmaos_juntos)`, Domingo de manhã | feliz | "Hoje somos dois a atender! Se o preço do Tibério for mais alto, compra-me a mim. Se for mais baixo… compra-lhe a ele. É tudo da casa." | — |
| `tobias_serv_armazem` | abrir o Armazém (10 ❤️) | normal | "O Armazém. Desce com cuidado. Terceiro degrau. Lembras-te." | abre a loja secreta |
| `tobias_serv_armazem_comprar` | comprar no Armazém | feliz | "Isso é lendário. Custa uma lenda. Pagas em ouro, que lendas não aceito." | — |

> **Armazém** (Chave do Armazém, 10 ❤️): abre no horário do Mercado. O que vende está em `docs/LOJAS.md`, secção 2.1.1
> (1 arma Lendária por semana, Gema Perfeita, Elixir Estelar, Pena de Fénix, Móvel Dourado, Mapa do Tesouro).
