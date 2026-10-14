# NPCs e diálogo

Este documento tem: como se fala com NPCs (secção 1), a amizade (2), os **20 NPCs principais de Ascendia
com perfil completo** (3), os companheiros (4) e um exemplo de conversa (5).
Os NPCs das povoações da torre estão nos ficheiros de cada região; os números da amizade estão em `docs/SISTEMAS.md`.

---

## 1. Como funciona falar com NPCs

- Aproximas-te e carregas em **Falar** (tecla **E** ou tocar no NPC no telemóvel).
- Abre uma **caixa de diálogo** com o **retrato** do NPC (4 emoções: normal, feliz, zangado, triste), o **nome**
  e o texto a aparecer **letra a letra**, com um som de "voz" próprio de cada NPC (bips de tons diferentes).
- Carregar no botão acaba a frase de uma vez; carregar outra vez passa à seguinte.
- Muitas conversas têm **escolhas** (até 4 respostas). Algumas mudam a amizade, as missões ou o final.
- Menu de cada NPC: **Conversar** · **Perguntar sobre…** (a torre, o andar atual, rumores, a vida dele) ·
  **Missões** · **Loja / Serviço** · **Dar presente**.
- Os diálogos ficam em ficheiros de dados (`dados/dialogos/<npc>.json`, ver `docs/PROGRAMACAO.md`), em Português e Inglês.

### O que muda o que os NPCs dizem
- hora do dia, estação e tempo · andar mais alto e bosses derrotados ("Venceste o Ent Ancião!") ·
  a tua amizade com ele · a arma que trazes · o teu estado (pouca vida, amaldiçoado, cansado) ·
  escolhas da história · festivais · o teu animal de estimação e companheiros.

---

## 2. Amizade ❤️

- Cada NPC principal tem **0 a 10 corações** (100 pontos cada, ver `docs/SISTEMAS.md`, secção 15).
- **1 presente por dia** e **2 por semana** por NPC (no aniversário não conta e vale ×8).
- **Cenas de coração** aos 2, 4, 6, 8 e 10 corações: acontecem quando entras no sítio indicado à hora indicada.

| Corações | Recompensa geral |
|---|---|
| 2 | cena 1 · 5% de desconto (se tiver loja) |
| 4 | cena 2 · receita ou item exclusivo |
| 6 | cena 3 · missão pessoal · aceita vir jantar a tua casa |
| 8 | cena 4 · 15% de desconto · manda-te cartas com presentes |
| 10 | cena final · **recompensa única** (ver cada NPC) |

> O jogo é de **amizade**: não há namoros. Os NPCs tornam-se melhores amigos, mentores, família.

---

## 3. Os 20 NPCs de Ascendia

### 3.1 Lyra — recepcionista da Guilda
| | |
|---|---|
| Aspeto | rapariga de 19 anos, cabelo ruivo em rabo-de-cavalo, uniforme azul da Guilda, sardas, óculos que lhe escorregam |
| Personalidade | faladora, alegre, sabe todos os mexericos da cidade; organizada no trabalho, desastrada fora dele |
| História | nasceu em Ascendia; o pai foi aventureiro e nunca voltou do andar 31. Por isso trabalha na Guilda: quer saber de todos os que sobem |
| Onde está | Guilda (8:00–18:00) · Mercado (18:00–20:00) · casa |
| Aniversário | Primavera, dia 5 |
| Serviços | missões da Guilda, rank, **Cristal de Avaliação** (no início) |
| Adora | Flor de Mel, Panquecas de Mel Azul, Concha Rara · **Gosta** de flores, doces · **Detesta** partes de monstros, Gel de Slime |
| Cenas de coração | 2: arruma papéis à noite e fala do pai · 4: pede-te para ires com ela ao rio ver as lanternas · 6: encontra o nome do pai num registo antigo (missão N_LYRA_3) · 8: mostra-te o diário onde escreve as tuas aventuras · 10: o pai deixou uma carta para "o próximo aventureiro"; ela lê-ta |
| Missões | **N_LYRA_1** *Papéis Perdidos*: encontrar 5 formulários que o vento levou pela cidade → 100 ouro, ❤️ · **N_LYRA_2** *Entrega Rápida*: levar 3 cartas a povoações dos andares 2, 7 e 11 num só dia → Bolsa de Viagem (+5 espaços) · **N_LYRA_3** *O Pai da Lyra*: encontrar o acampamento do pai no andar 31 → ❤️❤️ e a bússola do pai (aponta para a Zona Segura) |
| Recompensa (10 ❤️) | **Cartão de Ouro da Guilda**: as missões dão +25% de recompensa |
| Falas | "Bom dia! Hoje há três missões novas e uma é MESMO estranha." · "Sabias que o Brom canta quando ninguém está a ver?" · "Volta inteiro, ouviste? É uma ordem da Guilda!" |

### 3.2 Mestre Gorvan — Mestre da Guilda
| | |
|---|---|
| Aspeto | homem de 55 anos, enorme, careca com barba cinzenta, **só um braço** (o esquerdo), cicatriz no olho, capa de pele |
| Personalidade | sério, poucas palavras, duro mas justo; esconde uma grande tristeza |
| História | chegou ao andar 74 há 20 anos com a sua equipa de 5. Só ele voltou, sem um braço. Nunca mais subiu e nunca fala disso |
| Onde está | gabinete da Guilda · campo de treino ao fim da tarde · sozinho na muralha à noite |
| Aniversário | Inverno, dia 20 |
| Serviços | escolher a **classe** (nível 10, 40, 70), missões de rank alto, **treino** (depois do andar 80) |
| Adora | Chá Quente, armas antigas, Machado do Gorvan (depois do andar 74) · **Gosta** de bebidas quentes, carne assada · **Detesta** flores, doces, "gente que desiste" |
| Cenas de coração | 2: treina sozinho com um braço; deixa-te ver · 4: conta como perdeu o braço (sem os detalhes) · 6: missão N_GORVAN_3 · 8: fala da equipa pelo nome · 10: volta a subir à torre contigo (depois do andar 80) |
| Missões | **N_GORVAN_1** *Prova de Força*: vencer 3 bonecos de treino em 30 s → Faixa de Aprendiz (+5% ATQ) · **N_GORVAN_2** *A Escolha*: escolher a classe (nível 10) · **N_GORVAN_3** *Nomes na Pedra*: gravar os nomes da equipa dele numa pedra na Praça (precisa de Mármore Celeste) → ❤️❤️ |
| História principal | diário da equipa (andar 46), Catacumbas (andar 74), cena depois do Rei Sem Coroa (andar 80) |
| Recompensa (10 ❤️) | **Gorvan como companheiro** (tanque com machado) e a skill **Técnica do Braço Único** (golpe giratório) |
| Falas | "Hmm." · "Subir é fácil. Voltar é que custa." · "Não morras. É a única regra." |

### 3.3 Brom — ferreiro
| | |
|---|---|
| Aspeto | anão de 140 anos, barba ruiva com tranças e anéis de ferro, avental de couro queimado, braços enormes, sobrancelhas grossas |
| Personalidade | rabugento, resmungão, perfeccionista; tem um coração de ouro e chora com histórias tristes (diz que é fumo) |
| História | filho de **Grimbold Martelo-Forte**, ferreiro da Forja Anã do andar 18. Fugiu da torre em pequeno e nunca soube o que aconteceu ao pai. O **tio Ragnar** vive no andar 64 |
| Onde está | Forja (6:00–19:00) · Taberna (19:00–23:00) · casa |
| Aniversário | Inverno, dia 9 |
| Serviços | forjar, **melhorar +1 a +10**, encantar com gemas, reciclar, reparar |
| Adora | Minério de Mitril, Assado de Javali, Rubi · **Gosta** de lingotes, carne · **Detesta** flores, Gel de Slime, armas partidas |
| Cenas de coração | 2: canta a forjar (apanhas-o) · 4: mostra o martelo velho do pai · 6: missão R2_05 *O Martelo do Pai* · 8: ensina-te a forjar uma adaga contigo · 10: acaba a **arma inacabada nº 10 000** do andar 65 |
| Missões | **N_BROM_1** *Minério para Começar*: 10 Minério de Cobre → Picareta de Cobre · **R2_05** *O Martelo do Pai* · **R7_03** *O Tio Ragnar* |
| Recompensa (10 ❤️) | **A Décima Milésima** (espada lendária feita para ti): o ATQ cresce com o teu nível |
| Falas | "Hmpf. Mostra-me essa espada. …Quem te ensinou a afiar? Um javali?" · "Volta amanhã. O ferro não tem pressa." · "Não é choro. É fumo da forja." |

### 3.4 Selene — alquimista
| | |
|---|---|
| Aspeto | elfa de 300 anos que parece ter 25, cabelo prateado preso com lápis, óculos de proteção na testa, bata cheia de manchas coloridas |
| Personalidade | distraída, curiosa, as experiências explodem; fala depressa quando está entusiasmada |
| História | nasceu em **Folhalta** (andar 7), dentro da torre (a floresta dos elfos foi engolida há mil anos). Desceu para Ascendia há cem anos para estudar alquimia com os humanos, contra a vontade dos anciãos. O irmão mais novo **Eldrin** ficou lá. Nunca viu um céu verdadeiro e quer muito ver um |
| Onde está | Alquimia (9:00–18:00) · Biblioteca (18:00–20:00) · casa (às vezes explode qualquer coisa) |
| Aniversário | Primavera, dia 18 |
| Serviços | poções, elixires, bombas, antídotos; receitas de alquimia |
| Adora | Cogumelo Luminoso, Ervas raras, Lágrima de Aurora · **Gosta** de cogumelos, flores estranhas · **Detesta** coisas "normais" (pão, pedra) |
| Cenas de coração | 2: uma explosão deixa-a com o cabelo em pé (ri-se) · 4: mostra-te uma poção que muda de cor com o humor · 6: carta do Eldrin (R1_07) · 8: conta as histórias da floresta antes de cair (as que a Lothiel lhe contava) e o sonho de ver um céu verdadeiro · 10: dá-te o resultado de 300 anos de estudo |
| Missões | **N_SELENE_1** *Ervas Verdes*: 10 Erva Verde → receita Poção de Vida · **R1_07** *Cartas para Selene* · **N_SELENE_3** *A Poção Impossível*: ingredientes de 5 regiões → Poção de Encolher (usada no andar 5) |
| Recompensa (10 ❤️) | **Pedra Filosofal** (acessório): as poções curam o dobro |
| Falas | "Não toques nisso! …Ou toca, para ver o que acontece. Não, não toques." · "BUM! Ah. Era para fazer bum? Era para fazer bum." |

### 3.5 Tobias — mercador
| | |
|---|---|
| Aspeto | homem baixo e redondo de 45 anos, bigode enrolado, colete com bolsos cheios, chapéu com pena |
| Personalidade | ganancioso mas divertido, regateia tudo, adora contar dinheiro; no fundo é generoso com quem precisa |
| História | irmão gémeo do **Tibério** (o mercador das Zonas Seguras); os dois discutem por cartas sobre quem vende mais |
| Onde está | Mercado (7:00–19:00) · Taberna · casa |
| Aniversário | Verão, dia 3 |
| Serviços | loja geral (muda todos os dias) e **itens raros** (mudam de 3 em 3 dias) |
| Adora | Pinça de Ouro, Pérola Negra, Ouro antigo · **Gosta** de gemas, moedas antigas · **Detesta** regatear demasiado (−amizade se regateares mais de 3 vezes no dia) |
| Cenas de coração | 2: conta moedas a cantar · 4: revela que dá comida aos pobres às escondidas · 6: zanga com o Tibério (missão N_TOBIAS_3) · 8: mostra o armazém secreto · 10: dá-te a chave |
| Missões | **N_TOBIAS_1** *Entrega ao Tibério*: levar uma caixa à Zona Segura do andar 5 → 200 ouro · **R2_11** *A Toupeira Dourada* · **N_TOBIAS_3** *Irmãos*: fazer as pazes entre o Tobias e o Tibério (escolhas de diálogo) → os dois juntam as lojas: preços −5% em todo o lado |
| Recompensa (10 ❤️) | **Chave do Armazém**: loja secreta com itens lendários |
| Falas | "Preço especial! Só para ti! …É o mesmo preço para toda a gente, mas tu és especial." · "O meu irmão? Vende areia a quem tem sede." |

### 3.6 Dona Marta — dona da Estalagem
| | |
|---|---|
| Aspeto | senhora de 60 anos, gordinha, avental florido, cabelo branco num carrapito, faces coradas |
| Personalidade | a "mãe" de toda a gente; preocupa-se, dá de comer a todos, ralha com carinho |
| História | perdeu o filho para a torre há muitos anos; abriu a estalagem para que nenhum aventureiro dormisse com fome |
| Onde está | Estalagem (5:00–23:00) · mercado de manhã cedo |
| Aniversário | Outono, dia 12 |
| Serviços | dormir e gravar, **cozinha** (ensina receitas), refeições quentes |
| Adora | ingredientes frescos de qualidade Excelente, Flor de Mel, Mel Azul · **Gosta** de flores, legumes · **Detesta** que saltes refeições (se dormires 3 dias sem comer, ralha) |
| Cenas de coração | 2: ensina-te a cozinhar uma sopa · 4: fala do filho · 6: pede-te para provares o guisado secreto · 8: guarda o quarto dela para ti ("é teu, filho") · 10: ensina o **Guisado da Mãe** |
| Missões | **N_MARTA_1** *Ingredientes Frescos*: 5 legumes da quinta → receita Sopa de Legumes · **R1_05** *Mel Azul* · **N_MARTA_3** *O Quarto Vazio*: encontrar uma carta do filho dela (andar 58, num destroço) → ❤️❤️❤️ |
| Recompensa (10 ❤️) | **Guisado da Mãe** (cura tudo e +10% a tudo durante 1 dia) e quarto grátis para sempre |
| Falas | "Senta-te. Come. Depois falas." · "Estás magro! A torre não te dá de comer?" |

### 3.7 Kai — Jogador nº 9 999
| | |
|---|---|
| Aspeto | rapaz de 17 anos, cabelo preto espetado, casaco azul do mundo real (rasgado), espada curta, ténis gastos |
| Personalidade | orgulhoso, competitivo, faz-se de duro; leal até ao fim; tem muitas saudades de casa (irmã pequena) |
| História | chegou meses antes de ti. Salva-te no prólogo. Quer voltar para a irmã a todo o custo — é por isso que aceita o acordo do Sistema (andar 61–68) |
| Onde está | na torre de dia · Praça a treinar à noite · Taberna aos domingos (comida "que parece do mundo real") |
| Aniversário | Verão, dia 24 |
| Serviços | **duelos de treino** (a Arena dá XP de skills) · aparece nos andares para ajudar (eventos) |
| Adora | comida do mundo real (Hambúrguer de Javali, Ramen de Fungo), Pena Arco-Íris · **Gosta** de desafios, carne · **Detesta** que te armes em herói, flores |
| Cenas de coração | 2: corrida até ao topo da muralha · 4: mostra-te a foto da irmã (o telemóvel sem bateria) · 6: duelo a sério ao luar · 8: promessa: "voltamos os dois" · 10: (se salvo) treinam juntos no Último Posto |
| Missões | **N_KAI_1** *Corrida*: chegar antes dele ao fim do andar 3 → título *Rival* · **N_KAI_2** *Comida de Casa*: inventar uma receita "do mundo real" (hambúrguer) → receita · **R7_11** *O Kai* (o duelo) |
| Recompensa (10 ❤️) | **Lâmina Gémea** (espada): com o Kai na equipa, ambos fazem +20% |
| Falas | "Ah, ainda estás vivo? Que sorte a da torre." · "Não é por ti. Eu só… passava por aqui." · "A minha irmã ia gostar de ti. Ia achar-te esquisito." |

### 3.8 Mia — menina das flores
| | |
|---|---|
| Aspeto | menina de 11 anos, cabelo castanho com uma fita amarela, vestido remendado, cesto de flores, um pau como "espada" |
| Personalidade | sonhadora, teimosa, corajosa; odeia que a tratem como criança |
| História | órfã do Bairro Baixo. Quer ser aventureira como tu |
| Onde está | esquina do Bairro Baixo a vender flores · Praça a "treinar" · Igreja (dorme lá) |
| Aniversário | Primavera, dia 27 |
| Serviços | vende flores (presentes baratos) |
| Adora | armas pequenas, histórias da torre, a boneca do Yeti (andar 45) · **Gosta** de doces, flores · **Detesta** que a trates como criança (opções de diálogo!) |
| Cenas de coração | 2: mostra-te o "treino" com o pau · 4: pede-te para a ensinares (começa o treino) · 6: segue-te às escondidas até ao andar 1 (missão) · 8: vence o Coelho-Chifre Ancião sozinha · 10: torna-se aventureira (rank F) e **companheira** |
| Missões | **N_MIA_1** *Primeira Espada*: pedir ao Brom uma espada pequena → ❤️ · **N_MIA_2** *Treino*: 5 sessões de treino (minijogo de ritmo) · **N_MIA_3** *A Fuga*: encontrar a Mia no andar 1 antes dos lobos |
| Recompensa (10 ❤️) | **Mia como companheira** (arqueira) e o **Arco da Mia** (arco que cresce contigo) |
| Falas | "Um dia vou subir mais alto do que tu!" · "Não sou pequena. Sou… compacta." |

### 3.9 Irmã Célia — sacerdotisa
| | |
|---|---|
| Aspeto | mulher de 40 anos, túnica branca e azul, cabelo castanho num lenço, um colar com um cristal de luz |
| Personalidade | calma, sábia, gentil; firme com quem faz mal |
| História | aprendeu com a **Abadessa Lumina** na Ordem da Luz (andar 77); desceu para cuidar de Ascendia |
| Onde está | Igreja (6:00–20:00) · visita doentes à tarde |
| Aniversário | Inverno, dia 2 |
| Serviços | **bênçãos** (bónus antes de bosses), tirar Maldições, cura de estados, Água Benta |
| Adora | Velas, Cristais de Luz, Sálvia Sagrada · **Gosta** de flores brancas, chá · **Detesta** itens amaldiçoados |
| Cenas de coração | 2: canta na igreja vazia · 4: fala da Ordem da Luz · 6: missão R7_12 · 8: conta que já foi caçadora de mortos-vivos · 10: abençoa-te para sempre |
| Missões | **N_CELIA_1** *Velas*: 10 Cera → receita Vela Sagrada · **R7_12** *Rituais Interrompidos* · **N_CELIA_3** *Carta à Mestra*: levar uma carta à Abadessa Lumina (andar 77) → ❤️❤️ |
| Recompensa (10 ❤️) | **Bênção Eterna**: +10% de HP máximo para sempre |
| Falas | "A luz não vence a escuridão. Só a faz recuar. Isso chega." · "Deixa-me ver essa ferida." |

### 3.10 Velho Fausto — bibliotecário
| | |
|---|---|
| Aspeto | velho de 80 anos, barba branca até à cintura, óculos grossos, cachecol, sempre com um livro |
| Personalidade | esquecido, apaixonado por história, fala muito baixo e detesta barulho |
| História | passou a vida a juntar tudo o que se sabe sobre a torre. Traduz os hieróglifos (andar 39) |
| Onde está | Biblioteca (8:00–22:00) · banco da Praça ao sol |
| Aniversário | Outono, dia 4 |
| Serviços | **Bestiário**, tradução de livros e páginas de lore, mapas antigos |
| Adora | Página Antiga, livros raros, Ídolo de Jade · **Gosta** de chá, papel · **Detesta** barulho (correr dentro da biblioteca dá −amizade) |
| Cenas de coração | 2: adormece em cima de um livro · 4: mostra o mapa da torre que desenha há 50 anos · 6: os hieróglifos (R4_07) · 8: fala do sonho de ver o topo · 10: dá-te o livro de uma vida |
| Missões | **R2_08** *A Cor Violeta* · **R3_15** *O Ídolo de Jade* · **R4_07** *Os Hieróglifos* · **R8_10** *Livros Perdidos* · **R10_05** *Ecos de Casa* |
| Recompensa (10 ❤️) | **O Livro de Tudo**: o Bestiário mostra as fraquezas e os drops de todos os monstros, mesmo os que ainda não viste |
| Falas | "Shhh. Os livros estão a dormir." · "Ah, o andar 13! Cristais que cantam. Ou era o 14?" |

### 3.11 Rook — ladrão do Bairro Baixo
| | |
|---|---|
| Aspeto | jovem de 22 anos, capuz escuro, cabelo comprido a tapar um olho, sorriso torto, muitas facas pequenas |
| Personalidade | sarcástico, esperto, ninguém sabe de que lado está; protege as crianças do Bairro Baixo |
| História | Torrense que desceu sozinho de criança. Rouba aos ricos e dá ao bairro (diz que não) |
| Onde está | dorme de dia · Bairro Baixo à tarde · **telhados à noite** (só aparece aí) |
| Aniversário | Outono, dia 21 |
| Serviços | **mercado negro** (rank C): itens raros, informações sobre segredos, missões duvidosas; compra itens "duvidosos" a 40% |
| Adora | segredos (Mapas do Tesouro), Pérola Negra, Coroa de Casca · **Gosta** de itens roubados, doces · **Detesta** a Guarda, flores |
| Cenas de coração | 2: apanhas-o a dar comida às crianças · 4: corrida pelos telhados · 6: missão R3_12 · 8: conta como chegou à cidade · 10: dá-te a gazua dele |
| Missões | **N_ROOK_1** *Um Favor Pequeno*: entregar um embrulho sem perguntas (escolha: abrir ou não) · **R3_12** *O Rei Bobo* · **N_ROOK_3** *A Prisão*: tirar o Rook da cela da Guarda (escolha: falar com a Freya ou ajudá-lo a fugir — muda a amizade dos dois) |
| Recompensa (10 ❤️) | **Gazua Mestra**: abre 1 baú de ouro por dia sem chave |
| Falas | "Eu? Roubar? Só peço emprestado para sempre." · "Não contes à Freya que me viste." |

### 3.12 Capitã Freya — Capitã da Guarda
| | |
|---|---|
| Aspeto | mulher de 35 anos, alta e musculada, cabelo loiro curto, armadura de aço polida, lança, cicatriz no queixo |
| Personalidade | dura, justa, sem paciência para mentiras; adora um bom combate |
| História | ex-aventureira rank S. Ficou na cidade para a proteger dos monstros que fogem da torre |
| Onde está | Quartel (7:00–18:00) · patrulha pela cidade · Arena aos fins de semana |
| Aniversário | Verão, dia 15 |
| Serviços | **caças** a monstros com nome e monstros que fogem para a cidade, **Arena** |
| Adora | armas de qualidade Excelente, Lança Relâmpago · **Gosta** de treino, carne · **Detesta** ladrões, doces |
| Cenas de coração | 2: luta-se de braço de ferro na Taberna · 4: treino a sério · 6: missão N_FREYA_3 · 8: conta porque deixou de subir (salvou a cidade de uma invasão) · 10: luta a teu lado na Arena (dupla) |
| Missões | **N_FREYA_1** *Patrulha*: limpar 5 monstros que entraram na cidade · todas as caças de monstros com nome (R1_12, R2_10, R3_11, R4_12, R5_11, R5_14, R7_13, R8_08, R9_11, R10_13) · **N_FREYA_3** *A Invasão*: defender a cidade de uma invasão (evento grande) |
| Recompensa (10 ❤️) | **Lança da Capitã** (lança lendária) e **Insígnia da Capitã** (+10% DEF) |
| Falas | "Mostra-me o que sabes. Não, a sério. Mostra." · "Se vires o Rook, diz-me. Se não vires, também diz." |

### 3.13 Pip — pescador
| | |
|---|---|
| Aspeto | homem de 30 anos, magrinho, chapéu de palha, cana às costas, sempre com sono |
| Personalidade | preguiçoso, simpático, conta histórias de pesca exageradíssimas |
| História | pesca em todos os rios e lagos que a torre tem; diz que um dia pescou uma baleia (mentira… ou não?) |
| Onde está | Rio de Ascendia de manhã · Mercado à tarde (vende peixe) · Taberna à noite · às vezes nos andares (3, 9, 26) |
| Aniversário | Verão, dia 9 |
| Serviços | ensina **pesca**, vende canas e iscos, **Festival da Pesca** |
| Adora | peixes lendários, Isco Dourado · **Gosta** de peixes raros, sestas (dar-lhe uma almofada!) · **Detesta** pressas |
| Cenas de coração | 2: adormece com a cana na mão · 4: pescam juntos ao pôr do sol · 6: R1_10 *O Rei do Lago* · 8: confessa que a baleia era um tronco · 10: dá-te a cana dele |
| Missões | **R1_03** *Aprende a Pescar* · **R1_10** *O Rei do Lago* · **N_PIP_3** *Todos os Peixes*: pescar 30 espécies diferentes → título *Mestre Pescador* |
| Recompensa (10 ❤️) | **Cana do Pip**: o minijogo de pesca fica mais fácil e os lendários aparecem mais |
| Falas | "Shh… estão a morder. Não. Era o vento." · "Uma vez pesquei um peixe TÃO grande que o rio ficou vazio." |

### 3.14 Hana — agricultora
| | |
|---|---|
| Aspeto | rapariga de 24 anos, chapéu de palha com flores, macacão de ganga, botas de borracha, sempre com terra nas mãos |
| Personalidade | alegre, acorda às 4 da manhã, fala com as plantas |
| História | a família tinha uma quinta num mundo engolido; trouxe sementes no bolso. Hoje alimenta meia cidade |
| Onde está | Quinta (4:00–17:00) · Mercado (17:00–19:00) · casa |
| Aniversário | Primavera, dia 11 |
| Serviços | **quinta** (alargar o terreno, sementes, animais da quinta com o Zed), estufa |
| Adora | sementes raras, Guano, Semente do Mundo · **Gosta** de legumes, flores · **Detesta** pragas, Pétala Carnívora |
| Cenas de coração | 2: fala com as couves · 4: pede ajuda numa tempestade · 6: R3_14 *Chocolate!* · 8: mostra a semente do mundo dela · 10: plantam juntas uma árvore na Praça |
| Missões | **N_HANA_1** *A Primeira Colheita*: plantar e colher 5 Nabos → regador melhor · **R3_14** *Chocolate!* · **R8_09** *O Jardineiro* |
| Recompensa (10 ❤️) | **Regador de Ouro** (rega 3×3 de uma vez) e **estufa grátis** |
| Falas | "Bom dia! Já reguei, já colhi, já… são 6 da manhã? Ah." · "As plantas crescem melhor quando lhes contas piadas." |

### 3.15 Zed — domador de bestas
| | |
|---|---|
| Aspeto | homem de 40 anos, barba desgrenhada com penas, roupa de peles, um furão no ombro, cheira a estábulo |
| Personalidade | tímido com pessoas, fala muito mais com animais (e os animais entendem-no) |
| História | ninguém sabe de onde veio; dizem que foi criado por lobos de um mundo engolido |
| Onde está | Rancho (sempre); vai às vezes aos andares buscar animais feridos |
| Aniversário | Outono, dia 27 |
| Serviços | **animais de estimação** (choca ovos), **montadas** (depois do andar 40), animais da quinta, comida para animais |
| Adora | ovos raros, comida de animais de qualidade Excelente, Ovo de Ouro do Javali · **Gosta** de carne, peixe · **Detesta** quem maltrata animais (atacar um animal pacífico perto dele = −amizade) |
| Cenas de coração | 2: fala com o furão (e o furão responde?) · 4: um parto de uma vaca à noite · 6: mostra-te os animais feridos que trata · 8: conta a história dos lobos · 10: dá-te o apito |
| Missões | todas as missões de animais (R1_06, R4_13, R5_07, R6_14, R6_15, R7_09, R7_10, R9_04, R9_05, R10_15) |
| Recompensa (10 ❤️) | **Apito do Zed**: podes ter **2 animais de estimação** ao mesmo tempo |
| Falas | "…" (o furão guincha) "Ele diz olá." · "Animais não mentem. Pessoas sim." |

### 3.16 Madame Oriel — vidente
| | |
|---|---|
| Aspeto | mulher de idade indefinida, lenço roxo com estrelas, muitas pulseiras, olhos pintados de azul, um baralho de cartas brilhantes |
| Personalidade | misteriosa, fala por enigmas, tem um humor seco escondido |
| História | era astrónoma no **Observatório Celeste** (andar 86); desceu depois de ver uma coisa nas estrelas que não quer dizer |
| Onde está | Tenda da Vidente (14:00–2:00) |
| Aniversário | Inverno, dia 28 |
| Serviços | **profecias** (dicas pagas sobre segredos, monstros com nome e lendários), cartas da sorte (bónus do dia), onde está a **Cidade Errante** |
| Adora | Estrela Cadente, Cristal Celeste, cartas antigas · **Gosta** de cristais, chá · **Detesta** céticos (escolha de diálogo "Isso é tudo mentira" = −amizade) |
| Cenas de coração | 2: acerta numa previsão sobre ti · 4: lê-te as cartas a sério · 6: R9_08 *A Carta da Oriel* · 8: conta o que viu nas estrelas (o teu número) · 10: dá-te a bola de cristal |
| Missões | **R2_12** *O Outro Eu* · **R9_08** *A Carta da Oriel* · **N_ORIEL_3** *A Carta Que Falta*: encontrar a 22.ª carta do baralho dela (Cidade Errante) |
| Recompensa (10 ❤️) | **Bola de Cristal**: 1 vez por dia mostra no mapa todos os segredos do andar onde estás |
| Falas | "Vejo… um baú. Ou uma caixa. Ou um caixão. As cartas não são precisas." · "O teu número tem quatro zeros. Isso diz-me tudo." |

### 3.17 Lucien — bardo da Taberna
| | |
|---|---|
| Aspeto | homem de 28 anos, cabelo comprido loiro, chapéu com pena enorme, roupas coloridas, alaúde sempre na mão |
| Personalidade | dramático, exagera tudo, romântico com as palavras, um pouco vaidoso |
| História | chegou a Ascendia com uma caravana; ficou porque "aqui há heróis para cantar" |
| Onde está | Taberna (16:00–2:00) · Praça de manhã (a compor) |
| Aniversário | Verão, dia 19 |
| Serviços | **rumores** (dicas), **canções** sobre os teus feitos, **minijogos** da Taberna (cartas, dados, braço de ferro — depois do andar 30) |
| Adora | Café da Selva, histórias de bosses, instrumentos (Ocarina, Concha do Mar) · **Gosta** de doces, flores · **Detesta** silêncio |
| Cenas de coração | 2: canta uma canção sobre ti (muito exagerada) · 4: pede-te uma história para cantar · 6: R3_13 *Café da Selva* · 8: canta só para ti uma canção triste (da terra dele) · 10: compõe "A Balada do Jogador nº 10 000" |
| Missões | **R3_13** *Café da Selva* · **N_LUCIEN_2** *Inspiração*: levar-lhe 5 troféus de bosses para ver → canção nova · **N_LUCIEN_3** *O Concerto*: ajudar a organizar um concerto na Praça |
| Recompensa (10 ❤️) | **Alaúde do Lucien**: tocar dá bónus a ti e aos companheiros (canções de ataque, defesa e cura) |
| Falas | "Ó herói que sobe aos céus, com a espada e… e os pés!" · "A rima vem depois. Primeiro vem a emoção." |

### 3.18 Gizmo — inventor
| | |
|---|---|
| Aspeto | gnomo de 60 anos, óculos de soldar, cabelo branco espetado, fato-macaco com mil bolsos, braço mecânico extra nas costas |
| Personalidade | hiperativo, fala depressa, não acredita em magia ("é ciência que ainda não percebemos!") |
| História | inventor de um mundo de máquinas engolido; primo do **Senhor Vapor** (andar 66) |
| Onde está | Oficina (sempre, até de madrugada) · Praça quando testa invenções (explodem) |
| Aniversário | Primavera, dia 23 |
| Serviços | **engenhocas** (Gancho, Lanterna, bombas, detetor de tesouros, Capacete de Escafandro), **joalharia**, melhorias do barco (com o Tomé) |
| Adora | Engrenagem do Tempo, Núcleo de Magma, Gel Elétrico · **Gosta** de engrenagens, peças · **Detesta** magia (dar-lhe Pó de Fada = −amizade) |
| Cenas de coração | 2: uma invenção voa pela janela · 4: mostra-te o "robô" dele (uma torradeira com pernas) · 6: R7_14 *O Número 7* · 8: admite que às vezes usa magia sem querer · 10: dá-te as botas-mola |
| Missões | **R2_02** *O Gancho* · **R6_11** *Escafandro* · **R7_14** *O Número 7* |
| Recompensa (10 ❤️) | **Botas-Mola**: **salto duplo** |
| Falas | "Não é magia, é ENGENHARIA com BRILHOS!" · "Isso vai explodir? Provavelmente. Mas vai explodir BEM." |

### 3.19 Elva — costureira
| | |
|---|---|
| Aspeto | mulher de 32 anos, elegante, cabelo preto num coque com alfinetes, fita métrica ao pescoço, vestido feito por ela |
| Personalidade | perfeccionista, elegante, honesta (diz-te se a tua roupa é feia) |
| História | era costureira de uma rainha num reino engolido; desce todas as estações à Cidade Errante para comprar tecidos |
| Onde está | Costura (9:00–19:00) · Mercado de tecidos |
| Aniversário | Outono, dia 8 |
| Serviços | **armaduras de tecido**, **roupas e cores do herói** (cosméticos), **mochilas maiores**, tear (Fio Espectral) |
| Adora | Seda de Aranha, Fio de Luz Estelar, Pena Arco-Íris · **Gosta** de tecidos, penas · **Detesta** roupa rasgada (se o teu equipamento for comum, ela comenta…) |
| Cenas de coração | 2: tira-te as medidas à força · 4: mostra um vestido da rainha · 6: missão N_ELVA_3 · 8: conta do reino dela · 10: faz-te a capa |
| Missões | **N_ELVA_1** *Mochila Nova*: 10 Couro + 5 Linho → mochila de 40 · **N_ELVA_2** *Fio de Fantasma*: 10 Ectoplasma → ensina a tecer Fio Espectral · **N_ELVA_3** *O Vestido da Rainha*: materiais de 6 regiões para um desfile no Festival das Flores |
| Recompensa (10 ❤️) | **Capa Lendária da Elva**: +10% de esquiva (invencibilidade da esquiva dura mais) e muda de cor com o teu humor |
| Falas | "Isso que trazes vestido… é armadura ou um saco de batatas?" · "A elegância também é uma arma." |

### 3.20 Governador Aldric — governa Ascendia
| | |
|---|---|
| Aspeto | homem de 50 anos, magro, óculos pequenos, casaca formal com medalhas, sempre com papéis e um carimbo |
| Personalidade | burocrata, ansioso, quer o melhor para a cidade mas afoga-se em papelada |
| História | eleito há 10 anos porque "mais ninguém quis"; dedicou a vida a tornar Ascendia num sítio bom para viver |
| Onde está | Câmara (8:00–18:00) · Praça (inaugura coisas) · casa |
| Aniversário | Inverno, dia 14 |
| Serviços | **melhorias da cidade** (ver `docs/CIDADES.md`), a tua **casa** (andar 20) |
| Adora | projetos acabados (cada melhoria = +amizade), Selo Dourado, Coroa do Reino · **Gosta** de papel, chá · **Detesta** atrasos, lama |
| Cenas de coração | 2: adormece em cima dos papéis · 4: mostra a maqueta da cidade · 6: missão N_ALDRIC_3 · 8: confessa que tem medo de falhar à cidade · 10: dá-te a chave da cidade |
| Missões | **R1_02** *Madeira para a Ponte* · todas as melhorias da cidade · **N_ALDRIC_3** *O Censo*: falar com todos os habitantes de Ascendia num dia |
| Recompensa (10 ❤️) | **Chave da Cidade**: tudo em Ascendia 10% mais barato e título *Cidadão de Honra* |
| Falas | "Carimbo. Carimbo. Isto não se carimba. Porque é que isto não se carimba?" · "A cidade agradece. Eu também. Em triplicado." |

---

## 4. Companheiros

Até **2 companheiros** sobem a torre contigo (regras em `docs/SISTEMAS.md`, secção 20).

| Companheiro | Como se consegue | Estilo | Skill |
|---|---|---|---|
| **Kai** | salvá-lo no andar 68 | espadachim rápido | Corte em Cruz |
| **Mia** | 10 ❤️ com a Mia | arqueira | Chuva de Flechas Pequena |
| **Mestre Gorvan** | 10 ❤️ com o Gorvan (depois do andar 80) | tanque com machado | Golpe Giratório |
| **Chefe Ssark** | missão R3_03 (aldeia amiga) | tanque com lança e escudo | Muralha de Escamas |
| **Caçadora Inga** | reconstruir a Aldeia dos Caçadores (R5_05) | arqueira com armadilhas | Armadilha de Urso |
| **Nina** | missão R10_08 | maga (gelo) | Nevão Pequeno |

---

## 5. Exemplo de conversa

```
┌─────────┐  BROM
│ retrato │  "Hmpf. Outra vez tu? Mostra-me essa espada."
│ zangado │
└─────────┘
  ▶ "Está como nova!"
    "Acho que lhe parti a ponta…"
    "Queres ver o que encontrei no andar 18?"   ← só aparece se já foste ao andar 18

(escolhes a 3.ª)

┌─────────┐  BROM
│ retrato │  "O andar 18? A forja dos anões?… Mostra. MOSTRA!"
│ triste  │
└─────────┘
  [Sistema] Missão iniciada: O Martelo do Pai. ❤️ +1
```
