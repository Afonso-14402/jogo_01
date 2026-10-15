# Bestiário

O livro dos monstros, no **Diário → Bestiário**. Quem o escreve (dentro do jogo) é o **Velho Fausto**, com o que tu
lhe contas. Os números (vida, ataques, drops) vêm dos ficheiros das regiões; aqui estão os **textos**.

---

## 1. Como funciona

| Nível da página | Como se abre | O que mostra |
|---|---|---|
| (silhueta) | ver o monstro pela 1.ª vez | silhueta preta, nome "???", andar onde o viste |
| ★ | vencê-lo 1 vez | nome, **imagem animada** (a animação "parado"), tipo, andares, **Descrição** |
| ★★ | vencê-lo **10 vezes** (guardiões, monstros com nome e bosses: 1 vez) | comportamento, ataques e os seus **avisos**, fraco a / resiste a |
| ★★★ | vencê-lo **30 vezes** (guardiões e monstros com nome: 3 vezes; bosses: 1 vez) **ou** pagar ao Fausto (50 ouro) | drops com percentagens, a versão **Elite**, a **Nota do Fausto** e uma **carta** para o jogo de cartas da Taberna |

- Com a Skill Única **Olho do Sistema**, o ★★ e o ★★★ (menos a Nota do Fausto) abrem logo à 1.ª vitória.
- `[Sistema] Nova entrada no Bestiário: {monstro}.` aparece ao abrir o ★.
- Completar o Bestiário dá o título *Enciclopédia Viva* (ver `docs/ATIVIDADES.md`).
- A **Descrição** tem no máximo ~200 letras; a **Nota do Fausto** ~250. Tom: um velho sábio, curioso e com humor.

**IDs**: `best_<monstro>_desc` e `best_<monstro>_nota` (ex.: `best_slime_verde_desc`).

---

## 2. Região 1 — Floresta

### 2.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Slime Verde** | Uma gota de gel com vontade própria. Salta para cima de quem passa, mais por curiosidade do que por maldade. Derrete com fogo. | "Guardei um num frasco durante uma semana. Comeu a rolha, metade do frasco e uma meia minha. Libertei-o. Ainda me sinto vigiado." |
| **Coelho-Chifre** | Pasta em paz até te ver. Depois decide, numa fração de segundo, se te ataca ou foge. Ninguém sabe como escolhe. | "Os caçadores dizem que o chifre dá sorte. Tenho três numa gaveta. Esta semana perdi os óculos duas vezes. Os caçadores mentem." |
| **Lobo Cinzento** | Caça em alcateia e rodeia a presa. O líder é maior e uiva quando perde um irmão. Os olhos brilham quando a janela azul aparece. | "Um lobo sozinho é cauteloso. Três lobos são uma estratégia. Uma das páginas antigas que me trouxeste diz que os olhos deles 'conhecem a janela'. Interessante." |
| **Javali** | Ignora-te até te achar perto demais. Depois carrega em linha reta, com toda a força e nenhum juízo. Se bater numa árvore, fica tonto. | "A melhor arma contra um javali é uma árvore. A segunda melhor é uma maçã. A pior é ficar parado a pensar qual é a melhor." |
| **Cogumelo Andante** | Finge ser um cogumelo normal até passares ao lado. Quando acorda, incha e solta uma nuvem de esporos venenosos. | "Não se come. Eu sei porque o Brom comeu. Passou dois dias a falar com uma bota. Diz ele que a bota começou." |
| **Fada Travessa** | Pequena, rápida e risonha. Teletransporta-se quando te aproximas e rouba o que tiveres à mão. Mata-a e recuperas o que levou. | "Não são más. São aborrecidas. Uma fada sem nada para fazer é uma fada a fazer alguma coisa a alguém." |
| **Abelha-Gigante** | Só ataca quem se aproxima da colmeia. Quando uma pica, o enxame inteiro vem atrás. O mel delas é azul. | "O mel azul cura a tosse, a tristeza e as segundas-feiras. Sobre as picadas, não há livro que ajude. Corre." |
| **Treant Jovem** | Uma árvore nova que acordou zangada. Disfarça-se entre as outras e só se mexe quando já é tarde. Queima depressa. | "Os elfos dizem que os Treants são as árvores que sonham demais. Bater numa árvore com um machado nesta floresta é sempre uma aposta." |

### 2.2 Versões Elite (aparecem na página ★★★)

| Elite | Texto |
|---|---|
| Slime Esmeralda | "Quando morre, divide-se em dois. Quando os dois morrem… pronto, aí morre mesmo." |
| Coelho Lunar | "Só aparece à noite, branco como a lua. Investe duas vezes. Os poetas acham-no bonito. Os poetas nunca levaram com ele." |
| Lobo de Sombra | "Fica invisível antes de atacar. Ouve-se a respiração. Se ouvires respiração e não vires lobo, esquiva." |
| Javali Ferro-Pelo | "Pelo duro como arame. Carga tripla. As árvores desta zona têm todas um buraco à altura do focinho." |
| Cogumelo Real | "Vermelho e orgulhoso. A nuvem dele também prende os pés." |
| Fada Rainha Pequena | "Chama as amigas. As amigas chamam as amigas. Leva antídoto e paciência." |
| Abelha Soldado | "Maior, com carapaça. Protege a rainha. Não tem sentido de humor." |
| Treant de Musgo | "Em cima do musgo cura-se sozinho. Tira-o de lá. Com jeito. Ou com fogo." |

### 2.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Slime Rei** | Um slime enorme com uma coroa de ouro e, ninguém sabe porquê, um peixe lá dentro. Aos 50% de vida divide-se em quatro. | "A coroa é verdadeira. O peixe também. Está vivo. Tenho muitas perguntas e nenhuma coragem para as fazer ao slime." |
| **Lobo Cicatriz** | Lobo negro com uma cicatriz branca no olho. Caça nas noites de lua cheia e o uivo dele dá força à alcateia. | "Os lenhadores dizem que ganhou a cicatriz a lutar contra um Jogador. Nenhum deles sabe dizer qual. Só sabem que o lobo ganhou." |

### 2.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Coelho-Chifre Ancião** | 1 | Um coelho cinzento do tamanho de uma carroça, com um chifre partido. Guarda o Círculo de Pedras há mais tempo do que alguém se lembra. | "Já mandou muitos aventureiros para a estalagem. A Dona Marta chama-lhe 'o meu melhor cliente'." |
| **Coruja Sombria** | 2 | Coruja negra de olhos amarelos. Ataca do alto e o pio dela cega por momentos. | "Vê no escuro, ouve um rato a cem metros e roda a cabeça para trás. Eu, na idade dela, já nem roda o pescoço." |
| **Lagostim Couraçado** | 3 | Lagostim azul-escuro com pinças grandes. Fecha-se na carapaça quando está em perigo. Raio abre-lhe a casca. | "Cozido fica cor de laranja. Não digas isto perto dele." |
| **Rainha dos Esporos** | 4 | Um cogumelo gigante de "vestido" e coroa de esporos. Chama os súbditos e enche o ar de veneno. | "Governa o andar 4 com mão de ferro. Ou de chapéu. Os cogumelos não têm mãos." |
| **Abelha-Rainha Melífera** | 6 | Abelha enorme dourada e azul. Chama o enxame e faz chover mel que prende os pés. | "A rainha não faz mel. Manda fazer. Há quem diga que é uma boa líder. Há quem tenha levado uma ferroada." |
| **Guardião de Musgo** | 7 | Um golem de raízes e pedra coberto de musgo. Abraça quem se aproxima e cura-se em cima do musgo. | "Os elfos de Folhalta dizem que foi feito para proteger a floresta deles. Agora protege um andar. Ninguém lhe explicou a diferença." |
| **Cavaleiro de Pedra Musgosa** | 8 | Uma estátua de cavaleiro que ganhou vida. Defende-se de frente com o escudo; ataca-o pelas costas. | "Nas ruínas há quatro estátuas iguais a ele que se mexem quando não olhas. Ele é o único que se mexe quando olhas. É o corajoso." |
| **Serpente da Névoa** | 9 | Serpente branca de água que entra e sai do lago. No nevoeiro só se vê a ondulação. | "Os pescadores juram que é ela que guarda o Rei do Lago. O Pip jura que já a pescou. O Pip jura muitas coisas." |

### 2.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Javali-Rei** (andar 5) | O Rei das Tocas: um javali gigante com coroa de raízes e presas rachadas. Carrega como uma avalanche, mas também bate nas árvores. | "Os javalis do andar 5 trazem-lhe maçãs. Ele nunca as come. Guarda-as. Ninguém sabe para quem." |
| **Ent Ancião** (andar 10) | O Guardião da Floresta: árvore gigante com cara de velho, metade seca. Protegia a Árvore-Mãe de tudo, até de quem a vinha ajudar. | "Era o filho mais velho da Árvore-Mãe. Confundiu-te com outro. Escrevo isto com tristeza: às vezes os guardas mais fiéis são os que menos ouvem." |
| **Larva Ancestral** (masmorra Toca das Raízes) | Verme gigante de madeira podre que escava debaixo da floresta. Era ela que comia as raízes por dentro. | "A doença da floresta tinha boca e dentes. Mas a Árvore-Mãe continuou a secar depois de ela morrer. Há doenças que vêm de mais acima." |

---

## 3. Região 2 — Cavernas e Minas

### 3.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Morcego** | Dorme pendurado no teto e acorda com luz ou barulho. Ataca em bando, aos ziguezagues. | "Os morcegos veem com os ouvidos. Eu ouço com os olhos fechados. Às vezes adormeço. É diferente." |
| **Goblin Mineiro** | Pica a rocha em grupo; um deles leva a lanterna. Se a lanterna cair, os outros ficam às escuras. | "Roubam minério, vendem-no aos kobolds, que o vendem aos mineiros. A Hilda chama-lhe 'economia'. Eu chamo-lhe 'círculo'." |
| **Golem de Pedra** | Parece um pedregulho até chegares perto. Lento e duro; um martelo faz-lhe mais estragos do que uma espada. | "Os anões diziam que os golens são pedras que sonharam ser gente. Acordaram a meio do sonho e ficaram zangados." |
| **Toupeira Gigante** | Anda debaixo do chão; só se vê a terra a mexer. Sai por baixo de ti para atacar. | "Se o chão tremer debaixo dos teus pés, não é medo. Bem, também é medo. Mas é sobretudo uma toupeira." |
| **Aranha da Caverna** | Desce do teto num fio quando passas por baixo. Morde com veneno e foge. | "Olha para cima nas grutas. Sempre. Tenho um pescoço torto de tanto olhar para cima nos livros de aranhas." |
| **Kobold** | Pequeno homem-lagarto com lança e lanterna. Põe armadilhas e tenta apagar-te a tocha com um sopro. | "Os kobolds têm medo do escuro, por isso andam com lanternas. E apagam as dos outros. A lógica dos kobolds é profunda." |
| **Lagarta de Cristal** | Lagarta enorme com cristais nas costas que iluminam e devolvem a magia. Enrola-se e rola. | "Os cristais dela cantam a mesma nota que a janela azul. Toda a gruta canta essa nota. Porque será?" |
| **Fantasma Mineiro** | Mineiro morto que vagueia no escuro. Só pode ser atingido quando está iluminado. | "Não sabem que morreram. Continuam a cavar. Se lhes falares com calma e luz, alguns lembram-se de onde puseram as coisas." |

### 3.2 Versões Elite

| Elite | Texto |
|---|---|
| Morcego Vampiro | "Bebe um bocadinho do que te tira. Não é educado." |
| Goblin Capataz | "Tem chicote e os outros goblins trabalham mais depressa perto dele. Odeio chefes assim." |
| Golem de Ferro | "Mais duro, mas o raio corre-lhe pelo corpo como água num cano." |
| Toupeira Blindada | "Placas de pedra nas costas. Bate-lhe na barriga. É o único conselho que dou sobre barrigas." |
| Aranha Saltadora | "Salta oito metros. Oito! Eu levo oito minutos a subir as escadas da biblioteca." |
| Kobold Xamã | "Cura os outros. Mata-o primeiro. É feio dizer isto num livro, mas é verdade." |
| Lagarta Prismática | "Muda de cor e de elemento. Espera pela cor que te convém. A paciência é uma arma." |
| Capataz Fantasma | "Ainda dá ordens. Os fantasmas ainda obedecem. A morte não acaba com os hábitos." |

### 3.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Rei Goblin Gruk** | Goblin gordo com coroa de latão e um martelo de vagoneta. Chama os súbditos e atira bombas grandes. | "Proclamou-se rei de 'tudo o que brilha'. Infelizmente, brilha pouca coisa nas minas. Por isso é rei de pouco." |
| **Toupeira Dourada** | Uma toupeira pequena de pelo dourado que não ataca: só foge. Valiosíssima. | "Ninguém sabe porque é dourada. Talvez coma ouro. O Tobias quer criá-las. Imagina um Tobias com toupeiras de ouro. Não imagines." |

### 3.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Vagoneta Assombrada** | 11 | Uma vagoneta de ferro com olhos de brasa e dentes de carril. Anda nos carris a toda a velocidade. | "Muda as agulhas e ela descarrila. É a única maneira de vencer uma coisa que só sabe ir em frente." |
| **Touro das Galerias** | 12 | Homem-touro mineiro com capacete e uma picareta gigante. Investe pelos túneis e bate nas paredes. | "Os mineiros juram que ele era um deles. Que se perdeu tanto tempo nos túneis que se esqueceu de ser gente." |
| **Prisma Vivo** | 13 | Um cristal flutuante cujo núcleo muda de cor. A cor diz que elemento lhe faz mais dano. | "Muda de cor a cada dez segundos. Como as minhas opiniões sobre a torre." |
| **Barqueiro Afogado** | 14 | Esqueleto de capa num barco com uma lanterna verde. Puxa quem passa para dentro de água. | "Leva as pessoas do rio para lado nenhum. Um barqueiro sem margem do outro lado. Que trabalho triste." |
| **Água-Viva Fúngica** | 16 | Um fungo que flutua como uma medusa, com tentáculos de luz. Chove esporos que cegam. | "Os fungoides chamam-lhe 'a Avó do Céu'. Têm-lhe respeito. E medo. É o que as avós costumam ter." |
| **Morcego-Rei dos Ecos** | 17 | Morcego gigante de orelhas enormes. Repete contra ti o último ataque que fizeste. | "Um eco com asas. O fosso devolve tudo o que lhe dás. Até os nomes, dizem." |
| **Sentinela Anã** | 18 | Autómato de bronze com uma fornalha no peito. Quando sobreaquece, bate mais e aguenta menos. | "Os anões faziam guardas que nunca dormiam. Cento e trinta anos depois, ainda não dormiu. Coitado." |
| **Reflexo Negro** | 19 | Uma silhueta negra de ti mesmo. Copia a tua arma e as tuas skills, e troca de lugar contigo. | "Lutar contra o próprio reflexo. Os filósofos escrevem sobre isto há séculos. Tu fizeste-o num lago." |

### 3.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Aranha-Mãe** (andar 15) | A Mãe do Ninho: aranha enorme com setas vermelhas nas costas. Protege o saco de ovos até ao fim. | "A última pata ficou esticada para os ovos. Não escrevo mais nada sobre isto. Não consigo." |
| **Golem de Cristal** (andar 20) | O Rei Sentado: golem gigante de rocha e cristal. Escuda-se com as colunas; só se levanta quando o obrigam. | "Ajoelhou-se perante a janela azul antes de cair. Os guardas da torre têm um rei. E não somos nós." |
| **Rei Anão Esquecido** (masmorra Mina do Rei Anão) | Fantasma de um rei anão com machado de duas mãos. Fica invisível sem luz e chama os seus mortos. | "Acordou há cento e trinta anos e expulsou o seu próprio povo. Os reis esquecidos são os mais perigosos: querem ser lembrados à força." |

---

## 4. Região 3 — Pântano e Selva

### 4.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Sapo Venenoso** | Salta entre nenúfares e prefere atacar de longe: puxa-te com a língua e cospe veneno que fica no chão. | "Não lambas um sapo destes. Escrevo isto porque alguém me perguntou. Foi o Pip. Claro que foi o Pip." |
| **Homem-Lagarto Renegado** | Exilado da Aldeia Sssar, pintado de vermelho. Luta em formação: um com escudo, um com lança, um com arco atrás. | "Não são o povo de Sssar. São os que o povo de Sssar não quis. Repara nas pinturas: vermelho é renegado, azul é vizinho." |
| **Flor Carnívora** | Enraizada e paciente. Morde quem chega perto e cospe sementes a quem fica longe. Fechada, parece uma flor qualquer. | "Na Primavera dormem de dia. Não lhes faças cócegas. Sei de um botânico que fez. Agora é um botânico com nove dedos." |
| **Mosquito Gigante** | Zumbe à tua volta, pica e afasta-se. Cada picada rouba um pouco de vida. O zumbido chama os outros. | "Do tamanho de um gato. O fumo das fogueiras afasta-os. Eu recomendo também afastar-me a mim do pântano." |
| **Crocodilo** | Fica debaixo de água com os olhos de fora e espera que passes na margem. Agarra e roda. | "Se vires dois olhos a boiar, não são dois sapos. Nunca são dois sapos. Afasta-te da margem." |
| **Macaco Ladrão** | Desce das árvores, rouba-te ouro e foge para as copas a rir-se. Atira cocos de cima. | "Mata-o e recuperas o ouro, com juros. É o único ladrão do mundo que devolve mais do que levou." |
| **Sanguessuga Gigante** | Escondida na água, salta e agarra-se a ti. Enquanto estiver agarrada, bebe. Sacode-a! | "Sal. Sal mata-as de uma vez. Leva sempre um saquinho de sal ao pântano. E outro para a sopa." |
| **Bruxa do Pântano** | Fica longe, a mexer o caldeirão. Quando chegas perto, afunda-se na lama e aparece noutro sítio. | "Não são todas más. Algumas só querem que as deixem mexer o caldeirão em paz. Compreendo-as. Eu sou assim com os meus livros." |

### 4.2 Versões Elite

| Elite | Texto |
|---|---|
| Sapo Dourado | "A pele vale oitocentas moedas. O veneno vale um funeral. Faz as contas antes de lhe tocar." |
| Campeão Renegado | "Escudo, lança e um grito que te gela as pernas. Ataca-o de lado: o escudo só olha para a frente." |
| Flor Gigante | "Puxa-te com vinhas até à boca. Corta as vinhas. Corta sempre as vinhas." |
| Mosquito Rainha | "Chama quatro filhas. Mata a mãe e as filhas perdem o rumo. Triste, mas eficaz." |
| Crocodilo Albino | "Branco como leite e rápido como um boato. Raro. O Barão Coaxim quer um empalhado. Eu não." |
| Macaco Prateado | "Bate no peito e luta em vez de fugir. É o único macaco honesto do pântano." |
| Sanguessuga Rainha | "Cresce enquanto bebe. Não a deixes beber. Isto também vale para o Brom, mas por outras razões." |
| Bruxa Anciã | "Transforma-te em sapo três segundos. Aproveita: é a única altura em que podes saltar tão alto." |

### 4.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Mãe-Crocodilo Mandíbula** | Crocodilo velhíssimo coberto de algas e conchas. Afunda e aparece noutro sítio, e chama as crias. | "Quarenta anos a afundar barcos. O Chefe Ssark tem a cicatriz no focinho por causa dela. Ela tinha um dente a menos por causa dele." |
| **Rei Macaco Bobo** | Macaco de coroa de cascas de banana e capa de folhas. Rouba toda a gente e foge pelos ramos. | "Juntou duas mil moedas roubadas e não comprou nada. Não sabe o que é comprar. Só sabe o que é brilhar. Há reis piores." |

### 4.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Garça-Lança** | 21 | Garça cinzenta gigante com um bico comprido como uma lança. Bica em linha e mergulha do céu. | "Fica imóvel horas a fio, numa perna só. Depois, num segundo, acerta. A paciência é a arma mais afiada do pântano." |
| **Lodo Tóxico** | 22 | Slime gigante verde-fluorescente com ossos a boiar lá dentro. Divide-se e volta a comer os pedaços. | "Os ossos que tem lá dentro não são dele. Não perguntes de quem são. Eu perguntei. Não dormi." |
| **Pantera de Jade** | 23 | Felino verde-escuro com manchas que brilham. Desaparece na vegetação e salta de onde não esperas. | "As manchas brilham quando caça. Se vires luzinhas verdes no mato, não são pirilampos. Bem, às vezes são." |
| **Totem Vivo de Sssar** | 24 | Totem de madeira com três cabeças esculpidas, acordado pelos renegados. Dispara raios em três direções. | "Os Ssar dizem que cada cabeça é um avô. Os renegados acordaram os avós à força. Os avós não gostaram." |
| **Caranguejo-Violinista Gigante** | 26 | Caranguejo laranja com uma pinça enorme. Esconde-se no buraco e só sai na maré baixa. | "A pinça grande serve para lutar e para namorar. Ele usou-a para as duas coisas contigo. Não respondas." |
| **Ninfa da Cascata** | 27 | Espírito de água com cabelo que é uma cascata. Ataca com jatos e cura-se no nevoeiro. | "Não é má. É água. A água não é boa nem má: ocupa o sítio que lhe deixam. Ela só não queria deixar-te o sítio dela." |
| **Grande Bugio** | 28 | Macaco gigante de cara vermelha. Salta entre ramos, atira troncos e faz as pontes abanar. | "O grito ouve-se a quatro andares de distância. Dizem os exploradores. Eu ouço-o daqui, mas pode ser o Brom a espirrar." |
| **Dríade Corrompida** | 29 | Mulher-planta com uma flor carnívora no lugar do cabelo. Prende com vinhas e cega com pólen. | "Era a guardiã do jardim. O jardim ficou com fome e ela ficou com ele. Corrompida é uma palavra triste para 'com fome'." |

### 4.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Serpente do Lodo** (andar 25) | A Guardiã do Ovo de Pedra: serpente gigante coberta de lodo, com uma coroa de pedra antiga. Mais rápida quando a água sobe. | "Guardava um ovo de pedra com uma luz azul lá dentro. O ovo desfez-se. A serpente guardou-o até ao fim, sem saber o que era. Como tantos de nós." |
| **Hidra do Pântano** (andar 30) | A Que Não Morre: três cabeças (verde, roxa e amarela) que voltam a crescer quando as cortas. Só o fogo fecha os pescoços. | "Os Ssar chamavam-lhe 'a Que Come os Reis'. Cortar uma cabeça faz nascer duas. Há problemas assim. Queima-os pela raiz." |
| **Jaguar de Pedra Solar** (masmorra Santuário do Jaguar) | Estátua de jaguar dourado que corre pelas paredes. Os raios de sol que entram pelo teto queimam onde batem. | "O povo-serpente adorava o sol. Pintava-o nas paredes, esculpia-o em pedra e punha-o a guardar os seus tesouros. Ele ainda guarda. Ninguém o mandou parar." |

---

## 5. Região 4 — Deserto

### 5.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Escorpião** | Enterrado na areia, só com a cauda de fora. Sai quando passas perto e ferra com veneno. | "Se vires uma cauda a sair da areia, o resto também está lá. É a primeira lei do deserto. A segunda é: não te sentes." |
| **Múmia** | Anda devagar de braços esticados, embrulhada em ligaduras velhas. Não sente dor. Arde muito bem. | "Alguém as embrulhou com tanto cuidado. Alguém chorou por elas. E agora andam por aí a gemer. Não há descanso na torre." |
| **Verme da Areia** | Vive debaixo da areia e sente os passos. Quem corre, chama-o. Sai por baixo de ti de boca aberta. | "Anda devagar no deserto. Não por educação: porque o chão tem ouvidos. E dentes." |
| **Esqueleto Guerreiro** | Luta com cimitarra e escudo. Se não lhe partires o crânio, volta a montar-se em cinco segundos. | "Teimoso até depois de morto. Conheço pessoas assim. Uma delas tem uma forja." |
| **Chacal** | Caça em alcateia e tenta sempre morder pelas costas. À noite são mais. | "Os nómadas dizem que os chacais guiam as almas perdidas. Para onde, não dizem. Não sigas os chacais." |
| **Espírito da Areia** | Um redemoinho com uma cara. Puxa, cega e desaparece nas tempestades. Com água, vira lama. | "Água num espírito de areia: fica lama, fica lento, fica envergonhado. A ciência é bonita." |
| **Bandido do Deserto** | Emboscam caravanas em bandos: um com espada, um com arco, um com bombas de fumo. Fogem se o chefe cair. | "Gente como nós, mas com piores escolhas. Às vezes trazem mapas do tesouro. Nunca são deles." |
| **Escaravelho de Fogo** | Corre em enxame e rola em chamas. Ao morrer, explode. | "Pequenos, brilhantes e mal-dispostos. Os sacerdotes antigos achavam-nos sagrados. Os sacerdotes antigos não andavam descalços." |

### 5.2 Versões Elite

| Elite | Texto |
|---|---|
| Escorpião Negro | "O veneno dele também te deixa lento. Dois problemas pelo preço de um ferrão." |
| Múmia Real | "Tem coroa. Até as múmias têm classes sociais. Chama escaravelhos para a servir." |
| Verme Cristal | "O corpo é de vidro solar. Um raio e estilhaça-se. É bonito de ver. De longe." |
| Esqueleto Capitão | "Chama dois soldados. Os esqueletos ainda obedecem a patentes. Que disciplina." |
| Chacal de Anúbis | "Negro, de olhos dourados, aparece e desaparece. Os nómadas não lhe dizem o nome em voz alta. Eu escrevo-o, que é diferente." |
| Djinn Menor | "Um primo pequeno do Djinn da tempestade. Atira raios. Os primos pequenos são sempre os mais irritantes." |
| Chefe de Bando | "Grita e o bando corre mais. Cala-o primeiro. Com respeito. Com força." |
| Escaravelho Real | "Dourado e com uma explosão maior. O Barão Coaxim quer um. Vivo. Boa sorte, Barão." |

### 5.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Sultão Bandido Kasim** | Bandido de turbante dourado e duas cimitarras. Chama o bando, atira fumo e foge quando perde. | "Chama-se 'Sultão' a si próprio. A Sultana de Zahra chama-lhe outras coisas. Não as escrevo num livro de família." |
| **Verme Colosso** | Um verme do tamanho de uma rua. Só aparece nas tempestades de areia. Os redemoinhos dizem onde vai sair. | "Engole caravanas inteiras. Encontraram-se camelos vivos lá dentro, uma vez. Muito confusos." |

### 5.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Lagarto-Duna Gigante** | 31 | Lagarto cheio de espinhos cor de areia. Enrola-se e rola pelas dunas abaixo. | "Parece uma duna até rolar para ti. No deserto, até as dunas têm pressa de te apanhar." |
| **A Miragem** | 32 | Uma figura de água e luz a tremer. Faz cópias de si: só a verdadeira tem sombra. | "Procura a sombra. É uma boa regra para a Miragem e para a vida: o que é verdadeiro tem peso." |
| **Abutre Rei** | 33 | Abutre enorme e careca, com uma coroa de penas. Agarra-te e larga-te do alto. | "Come o que os outros deixam. Não é nobre, mas é eficaz. A torre tem muitos abutres. Alguns usam coroa." |
| **Golem de Arenito** | 34 | Golem feito de blocos de templo com hieróglifos. Afunda e levanta-se da areia. | "Os hieróglifos do corpo dele são orações. Ao contrário. Alguém o construiu a rezar e alguém o acordou a praguejar." |
| **Djinn da Tempestade** | 36 | Espírito azul de turbante, com uma cauda de fumo. Atira raios de areia e tornados. | "Diz-se que um rei de cima o prendeu numa lâmpada. Se a lâmpada aparecer, devolve-lha. Um Djinn agradecido vale mais do que um Djinn zangado." |
| **Cavaleiro de Ossos Montado** | 37 | Esqueleto de armadura num camelo-esqueleto. Carrega com a lança e, depois, luta a pé. | "Um cavaleiro sem cavalo, num camelo sem carne. A torre tem sentido de humor. Um humor muito seco." |
| **Esfinge Menor** | 38 | Leão de pedra com cara de pessoa. Faz uma pergunta antes de lutar. Acertar dói-lhe mais do que uma espada. | "Responde bem e ela perde vida. Há poucos monstros que se vencem a pensar. Gosto muito desta." |
| **Sacerdote-Chacal** | 39 | Homem com cabeça de chacal e uma balança dourada. Pesa a tua alma contra a dele. | "Quem tiver mais vida perde. Uma balança justa? Uma balança cruel? Uma balança, só. As balanças não têm opinião." |

### 5.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Escorpião Imperador** (andar 35) | Imperador das Areias: escorpião negro e dourado com a marca azul da janela na carapaça. | "A marca apagou-se quando caiu. O Sistema chamou-lhe 'unidade de guarda'. Unidade. Como uma peça de uma máquina. Fiquei a pensar nisto uma semana." |
| **Faraó Eterno** (andar 40) | O Que Também Subiu: múmia real com máscara de ouro e olhos azuis. Enche a sala de areia quando perde. | "Era um de vocês. Um Jogador. Um dos reis da roda. A torre pô-lo num caixão a guardar a porta. Que espécie de reino é este, que trata assim os seus reis?" |
| **Esqueleto de Dragão Jovem** (masmorra Túmulo do Dragão Antigo) | Esqueleto de um dragão que nunca chegou a voar. Asas de osso, fogo azul. Voa mal e cai sobre ti. | "Morreu jovem, quando o céu dele foi engolido. Nunca voou a sério. A morte deu-lhe asas de osso. Coitado. Voa mal." |

---

## 6. Região 5 — Gelo

### 6.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Lobo de Gelo** | Caça em alcateia na neve. O pelo branco esconde-o até estar perto. O sopro gela. | "Primos dos lobos da floresta, mas com mais paciência. O frio ensina a esperar." |
| **Urso Polar** | Enorme, sozinho e com fome. Levanta-se nas patas de trás antes de atacar. | "Se ele se levantar, já é tarde para fugires. Se se sentar, é pior: está a pensar." |
| **Golem de Gelo** | Um bloco de gelo eterno que anda. Atira estacas que congelam. Derrete-se com fogo, mas devagar. | "Gelo que nunca derrete, a andar. Os anões queriam forjar com ele. Os golens não concordaram." |
| **Espírito da Neve** | Uma nuvem de neve com olhos. Traz o nevão consigo e desaparece nele. | "Os do norte dizem que é a neve a lembrar-se de que já foi chuva. Fica triste e zangada." |
| **Harpia Gélida** | Meio mulher, meio ave, de penas de gelo. Mergulha do céu e grita. | "As balistas do castelo foram feitas para elas. Usa-as. Os antigos não as construíram para decoração." |
| **Caçador Congelado** | Um caçador morto que continua a caçar. Atira flechas e põe armadilhas. Fogo e luz dão-lhe descanso. | "Eram homens e mulheres da aldeia do 46. Têm nomes. A Inga sabe-os todos. Não os chames de monstros à frente dela." |
| **Pinguim Guerreiro** | Pinguins em bando, de lança de gelo. Deslizam de barriga contra ti. | "Ridículos e perigosos ao mesmo tempo. Como os gansos da praça, mas com lanças." |
| **Mamute Jovem** | Manadas pacíficas. Só atacam se as provocares. Com a tesoura certa, dão lã sem luta. | "Não lhes batas. Eles lembram-se. Os mamutes lembram-se de tudo, por isso andam sempre devagar: estão a pensar no passado." |

### 6.2 Versões Elite

| Elite | Texto |
|---|---|
| Lobo Aurora | "O pelo muda de cor com a aurora. Teletransporta-se. Bonito demais para ser justo." |
| Urso de Gelo Azul | "Uma carapaça de gelo nas costas. O fogo derrete-a. Depois é só um urso. Só." |
| Golem de Gelo Negro | "As estacas dele congelam à primeira. Não fiques no caminho delas. Nem perto." |
| Espírito do Nevão | "O nevão segue-o. Ou ele segue o nevão. Ninguém sabe quem manda." |
| Harpia Rainha | "Penas de gelo em espiral. As outras harpias calam-se quando ela grita. Eu também me calava." |
| Caçador-Chefe Congelado | "Chama dois lobos. Era o chefe da caçada. Ainda é." |
| Pinguim Imperador | "Tem coroa e organiza o bando em formação. Ninguém lhe deu a coroa. Encontrou-a." |
| Mamute Ferido | "Ferido, furioso, ataca à vista. Alguém lhe fez mal. Não foste tu. Ele não sabe." |

### 6.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Presa-Branca** | Lobo branco enorme, com cicatrizes azuis que brilham. Só aparece nas noites de nevão. | "Dizem que é o pai de todos os lobos de gelo. Teve uma cria. Se a encontrares, trata-a bem: ela vai lembrar-se de quem o venceu." |
| **Mamute Ancião Tundra** | Um mamute do tamanho de uma casa, com musgo e pássaros nas costas. Pacífico. | "Os pássaros vivem nas costas dele. Os musgos vivem nas costas dele. Talvez uma aldeia inteira viva nas costas dele. Não lhe batas." |

### 6.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Morsa Gigante** | 41 | Morsa enorme com presas compridas. Desliza de barriga e parte o gelo com as presas. | "Parece preguiçosa. É preguiçosa. Mas quando acorda, acorda toda de uma vez." |
| **Alce Fantasma** | 42 | Alce branco meio transparente, com chifres de gelo. Desaparece entre os pinheiros. | "Os do norte deixam-lhe sal no caminho para ele não atacar. Ele ataca na mesma. Mas come o sal." |
| **Kraken do Gelo** | 43 | Só se veem os tentáculos a sair dos buracos do gelo. Abre buracos novos para te apanhar. | "Roubou três redes e um primo ao Ulf. O primo voltou. Isso diz muito sobre o primo." |
| **Coração de Cristal Azul** | 44 | Uma figura de gelo a flutuar, com estilhaços em órbita. Congela áreas inteiras. | "O coração da gruta. Quando parar de bater, as paredes vão derreter um bocadinho. Coisas presas vão acordar." |
| **Wendigo** | 46 | Criatura magra e altíssima, com crânio de alce. Invisível no nevão. O grito dá medo. | "Os caçadores do 46 saíram para o caçar e voltaram congelados. Não leias isto à noite. Eu escrevi-o de dia." |
| **Tartaruga-Glaciar** | 47 | Tartaruga gigante com um glaciar como carapaça. Esconde-se; ataca-lhe as patas quando as põe de fora. | "Tem mil anos? Dois mil? Ninguém lhe pergunta. Seria falta de educação." |
| **Raposa Aurora** | 48 | Raposa branca de várias caudas, que brilham como a aurora. Faz ilusões e fogos-fátuos. | "Os monges dizem que ela guarda as almas da aurora. Que as conta, todas as noites. Que a conta nunca acaba." |
| **Cavaleiro de Gelo** | 49 | Armadura de gelo vazia, com espada grande. Reflete projéteis e chama soldados. | "Uma armadura vazia que ainda guarda o rei. O rei não vem. Ele guarda na mesma. Lealdade é isto." |

### 6.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Yeti Ancião** (andar 45) | O Que Se Lembra: yeti enorme com um colar cheio de objetos de Jogadores antigos. Faz cair estalactites. | "Não comia os Jogadores. Guardava as coisas deles. Um relógio, uma chave, uma pena. Era um museu com braços. Eu entendo-o melhor do que gostava." |
| **Dragão de Gelo** (andar 50) | O Meio do Caminho: dragão branco e azul de escamas transparentes. Voa, sopra gelo e cria estacas. | "'Os outros vinham com amigos.' Cinquenta andares e um dragão sabe mais de amizade do que muitos livros meus." |
| **Rei do Inverno Esquecido** (masmorra Cripta do Rei do Inverno) | Rei-esqueleto de gelo, com coroa. Chama nevões e guerreiros e congela metade da sala de cada vez. | "Dormiu tanto tempo à espera de alguém que o esqueceram. Até o nome. Acordaste-o. Ele não estava à tua espera. Ficou zangado." |
