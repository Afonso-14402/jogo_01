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

---

## 7. Região 6 — Oceano

### 7.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Caranguejo Gigante** | Anda de lado nas praias e nas rochas. A carapaça aguenta tudo menos martelos e raios. | "Os caranguejos andam de lado porque a vida lhes ensinou que a direito não vale a pena. Filosofia de praia." |
| **Sereia Sombria** | Canta nas rochas à noite. O canto puxa-te para a água. Não é a mesma coisa que as sereias de Coralina. | "As de Coralina não gostam que as confundam com estas. Eu confundi uma vez. Não voltei a ser convidado." |
| **Homem-Tubarão** | Nada em círculos à tua volta antes de atacar. Fora de água é desajeitado; dentro, não. | "Se vires uma barbatana a fazer círculos, sai da água. Se não puderes, faz círculos também. Confunde-o." |
| **Pirata Esqueleto** | Piratas que nunca deixaram de o ser, nem depois de mortos. Lutam com sabres e roubam moedas. | "A Rosa do porto diz que cozinhou para muitos deles em vida. Diz que eram melhores clientes mortos: não comiam." |
| **Polvo** | Esconde-se nas rochas e agarra com os tentáculos. Solta tinta e foge. | "Oito braços, três corações e mais esperteza do que muita gente que conheço. Não te aproximes das rochas escuras." |
| **Alforreca Elétrica** | Flutua, brilha e dá choques. Em grupo, iluminam o mar à noite. | "Bonitas. Inúteis. Dolorosas. A tríade perfeita do mar. Não lhes toques. Nem para ver se são moles. São." |
| **Peixe-Lanterna** | Vive na escuridão do fundo. A luz na cabeça atrai presas. A presa és tu. | "Quem leva uma lanterna na testa no escuro está a pedir para ser visto. Ou está a fazer de isco. Ele faz as duas coisas." |
| **Serpente Marinha Jovem** | Uma serpente do mar ainda pequena (para uma serpente do mar). Ataca barcos e nadadores. | "Jovem. A mãe deve andar por perto. Ou não. As serpentes do mar foram ficando poucas. Esta talvez seja das últimas." |

### 7.2 Versões Elite

| Elite | Texto |
|---|---|
| Caranguejo Ermitão | "Usa um crânio gigante como casa. De quem é o crânio? Não queiras saber. Eu quis. Não durmo." |
| Sereia Abissal | "O canto dela também dá medo. Tapa os ouvidos. Com as mãos, não com coragem. A coragem não chega." |
| Tubarão-Martelo | "A cabeça é um martelo. A investida atordoa. A natureza tem sentido de humor." |
| Pirata Contramestre | "Dá ordens e os outros atacam mais depressa. Os piratas mortos ainda respeitam a hierarquia." |
| Polvo Gigante | "Dois agarrões de uma vez. Corta os tentáculos. Ele tem mais. Corta esses também." |
| Alforreca Rainha | "Choque em área grande. Estás molhado? Estás. Então dói o dobro." |
| Peixe-Lanterna Rei | "A luz dele cega. É a primeira vez que uma lanterna me parece agressiva." |
| Serpente das Tempestades | "Aparece nas tempestades e atrai raios. Tu estás encharcado. Ela também. Os raios não escolhem." |

### 7.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Caranguejo Rei Pinça-de-Ouro** | Caranguejo dourado com coroa e uma pinça de ouro maciço. Esconde-se na areia. | "O Barão Coaxim quer a pinça. O Tobias quer a pinça. O caranguejo também quer a pinça. Só um deles tem razão." |
| **Barba-Lodo** | Pirata fantasma com barba de algas, num pequeno navio fantasma. Só aparece nas noites de nevoeiro. | "Traiu a tripulação, roubou a capitã e ficou com o mar. O mar ficou com ele. A justiça do mar é lenta e molhada." |

### 7.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Tartaruga-Marinha Anciã** | 51 | Tartaruga enorme com uma ilha de palmeiras nas costas. Faz ondas e chama caranguejos. | "Há quem viva na ilha dela sem saber que a ilha nada. Dizem que, de cem em cem anos, ela muda de praia." |
| **Gaivota Gigante Ladra** | 52 | Gaivota enorme com um lenço de pirata. Rouba-te poções em pleno voo. | "É uma gaivota. Rouba. Não há mais nada a dizer sobre gaivotas." |
| **O Imediato Fantasma** | 53 | Fantasma de pirata gigante com uma âncora. Prende os Jogadores mortos ao navio. | "O braço direito do capitão do navio. Continua a mandar, depois de todos terem desistido de obedecer." |
| **Peixe-Leão Rei** | 54 | Peixe-leão listrado com barbatanas de espinhos venenosos. Camufla-se no coral. | "Lindo de morrer. Literalmente. Os espinhos têm veneno. Admira-o de longe." |
| **Dragão-Marinho Folhado** | 56 | Cavalo-marinho-dragão coberto de "folhas". Desaparece entre as algas. | "Parece alga. Comporta-se como alga. Morde como dragão. Os nomes da natureza são sempre honestos no fim." |
| **Golem de Coral** | 57 | Golem de coral rosa e branco. Era a defesa de Coralina e enlouqueceu. Regenera-se. | "Construído para proteger a cidade. Agora protege-a de toda a gente, até dos donos. Há guardas assim." |
| **Tamboril Abissal** | 58 | Peixe-diabo enorme com uma luz na antena. No escuro, só se vê a luz. | "Se no escuro do fundo vires uma luz bonita, nada para o outro lado. As luzes bonitas do fundo têm dentes." |
| **Guardião das Marés** | 59 | Estátua de tritão feita de pérola, com tridente. Enche a sala de água. | "Guardava um templo de um deus que já não existe. Guarda na mesma. A torre está cheia de guardas sem patrão." |

### 7.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Capitão Esqueleto** (andar 55) | O Contador de Ouro: esqueleto de capitão pirata, com sabre, gancho e um papagaio-esqueleto que avisa os ataques. | "Contava ouro que não podia gastar. O papagaio contava com ele. Os dois, para sempre, numa gruta. Há castigos piores. Não muitos." |
| **Leviatã** (andar 60) | O Último do Mar: serpente marinha colossal de olhos tristes. Luta no mar e à volta de uma ilha. | "Não queria lutar. Fugiu. E depois os olhos ficaram azuis. Escrevo isto e a mão treme. Quem é que manda nos monstros da torre?" |
| **Almirante Afogado** (masmorra Cofre do Almirante Afogado) | Fantasma de almirante com dois sabres e uma mão de caranguejo. Chama marés e afoga a sala aos bocados. | "Morreu a guardar um cofre. O cofre não tinha nada que valesse a vida dele. Os cofres nunca têm." |

---

## 8. Região 7 — Vulcão

### 8.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Salamandra** | Lagarto de fogo que anda à vontade perto da lava. Cospe brasas. | "Os alquimistas antigos achavam que nasciam do fogo. Nascem de ovos. Muito quentes, mas ovos." |
| **Elemental de Fogo** | Uma chama viva com braços. Arde mais quando está zangado. Apaga-se com gelo. | "Não é um bicho. É o fogo a querer ser alguém. Quase consegue." |
| **Diabrete** | Pequeno demónio vermelho que ri, rouba e troca as tuas armas. Chama os amigos. | "Os diabretes não são maus. São irritantes. Há uma diferença. Pequena." |
| **Golem de Magma** | Rocha negra com lava por dentro. Lento, pesado, a escorrer fogo pelas fendas. | "Bate-lhe nas fendas. Não com as mãos. Já sabias. Escrevo para quem não sabia." |
| **Cão Infernal** | Cão negro de olhos de brasa. Sopra fogo e caça em matilha. | "Os refugiados das Cinzas juram que eram os cães da cidade deles, antes do fogo. Não escrevo se acredito." |
| **Morcego de Cinza** | Morcego cinzento que se esconde na cinza que cai. Ataca em bandos e cega. | "Primo dos morcegos das minas, mas com pior feitio. A cinza não faz bem a ninguém." |
| **Escorpião de Lava** | Escorpião de rocha com um ferrão que pinga lava. Nada debaixo da cinza. | "Os do deserto picavam. Estes queimam. A torre gosta de melhorar os seus monstros." |
| **Cultista do Fogo** | Encapuzados que adoram o Titã. Fazem rituais que chamam elementais. | "Adoram o que os pode matar porque é forte. Há quem faça o mesmo com reis. Não é só no vulcão." |

### 8.2 Versões Elite

| Elite | Texto |
|---|---|
| Salamandra Negra | "O cuspe deixa uma poça de lava. Não pises. Nem que te paguem." |
| Elemental Azul | "Fogo azul é mais quente do que o vermelho. As crianças acham bonito. As crianças não deviam estar no vulcão." |
| Diabrete Chefe | "Chama mais três. O único diabrete pior do que um diabrete são quatro diabretes." |
| Golem de Magma Branco | "Tão quente que o chão derrete à volta dele. Usa gelo. Muito gelo." |
| Cão Infernal Alfa | "O sopro deixa o chão a arder. Os outros cães seguem-no. Corta a cabeça à matilha. Figurativamente." |
| Morcego de Brasa | "O rasto queima. Os morcegos de cinza respeitam-no. Eu também." |
| Escorpião de Obsidiana | "Carapaça de vidro negro. O martelo parte-a. Como parte o vidro. Clássico." |
| Sumo-Cultista | "O ritual dele chama dois elementais. Interrompe-o. É falta de educação, mas salva vidas." |

### 8.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Tricéfalo** | Cão infernal de três cabeças: uma de fogo, uma de fumo, uma de lava. Cada uma ataca à sua maneira. | "Três cabeças e um só estômago. Imagina as discussões à hora do jantar." |
| **Golem Forjado Nº 7** | Golem de obsidiana polida com um 7 gravado no peito. O ponto fraco é o núcleo nas costas. | "O Gizmo diz que assinou o projeto. O Gizmo diz muitas coisas. Desta vez acredito: o golem também explode quando não devia." |

### 8.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Fénix de Cinza** | 61 | Pássaro de cinza e brasas. Quando morre, renasce com um terço da vida, a não ser que lhe congeles as cinzas. | "Renasce sempre. Mas renasce menos de cada vez. Até as fénix se cansam." |
| **Serpente de Lava** | 62 | Serpente de rocha e lava que nada no magma e salta para fora. | "Nada em lava. Gosto pouco de cobras. Gosto ainda menos de cobras que nadam em lava." |
| **Ent Carbonizado** | 63 | Ent queimado, em brasa, primo da Árvore-Mãe. Ataca com galhos em fogo e raízes. | "Ardeu e continuou de pé. Os refugiados dizem que falou, uma vez, a alguém que passou: 'Cuidado com o que te prometerem.' Bom conselho. Vindo de uma árvore a arder, ainda melhor." |
| **Escavadora Anã Possuída** | 64 | Máquina de minas dos anões com uma broca enorme, possuída pelos cultistas. | "Os anões construíram-na para escavar rocha. Os cultistas puseram-na a escavar pessoas. A culpa não é da máquina." |
| **Sapo-Vulcão** | 66 | Sapo enorme com um géiser nas costas. Atira-te ao ar e salta-te em cima. | "Primo dos sapos do pântano, mas com um vulcão às costas. A família dos sapos é muito variada." |
| **Golem Portão de Obsidiana** | 67 | Um portão vivo de obsidiana com runas. Fecha-se e fica invencível até lhe partires as quatro runas. | "Um portão que luta. Os anões nunca fazem nada que só sirva para uma coisa." |
| **Kai** | 68 | Jogador nº 9 999. O teu rival. Com os olhos azuis da janela e uma armadura que o Sistema lhe deu. | "Não escrevo sobre ele. Não é um monstro. Nunca foi. Esta página fica em branco de propósito." |
| **Sumo-Sacerdote das Chamas** | 69 | O chefe dos cultistas, de máscara dourada. Chama elementais e faz muralhas de fogo. | "Adorava o Titã. Quando o Titã adormeceu, ficou sem deus. Não sei o que é pior: adorar um vulcão ou perdê-lo." |

### 8.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Ferreiro Infernal** (andar 65) | O Que Forjou o Teu Número: demónio ferreiro com uma fornalha no peito e um martelo enorme. | "Forjava armas para quem ainda não tinha chegado. Uma com o teu número. Alguém lhe dizia os números antes de vocês caírem do céu. Quem?" |
| **Titã de Magma** (andar 70) | O Coração do Vulcão: gigante de rocha negra com fendas de lava e uma coroa de chamas. | "Não morreu. Adormeceu. A região inteira respira melhor. Às vezes vencer é deixar alguém descansar." |
| **Autómato da Forja Primordial** (masmorra Forja Primordial) | Autómato anão antiquíssimo, com um martelo no lugar de um braço e uma fornalha no peito. | "Forjava as armas dos primeiros Jogadores, os sem número. Continua a forjar. Para ninguém. Há trabalhos que não sabem acabar." |

---

## 9. Região 8 — Reino Assombrado

### 9.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Fantasma** | Uma figura transparente que atravessa paredes e possui objetos. Só lhe acertas com luz ou magia. | "Nem todos os fantasmas do reino são maus. Estes são. Os do mercado não. A diferença é se ainda se lembram de quem eram." |
| **Zombie** | Anda devagar, morde, não desiste. Volta a levantar-se nas sepulturas que não estão consagradas. | "Água benta nas sepulturas. Ou paciência infinita. Eu escolhia a água benta." |
| **Cavaleiro Esqueleto** | Cavaleiro de armadura velha, com espada e escudo. Ainda faz a ronda pelo reino. | "Fazem a ronda há séculos. Não sabem que o rei já não precisa deles. Ninguém lhes disse." |
| **Gárgula** | Parece uma estátua até passares. Depois mergulha do alto com garras de pedra. | "Se uma estátua tiver a cabeça virada para ti, desconfia. As estátuas normais não têm curiosidade." |
| **Vampiro** | Elegante, pálido e rápido. De noite, hipnotiza e bebe. De dia, dorme num caixão. | "O Caçador Van diz que se lhes conta os passos pelo bater do coração. Eles não têm. Por isso são silenciosos." |
| **Livro Possuído** | Um livro que voa e ataca com feitiços. Acorda com barulho. Na biblioteca há centenas. | "Livros que mordem. Sempre achei que os livros tinham opinião. Estes têm dentes." |
| **Banshee** | Uma mulher fantasma que grita. O grito atordoa e parte vidros. | "Grita por quem morreu. Não grita para te fazer mal. Grita porque não sabe fazer outra coisa." |
| **Armadura Viva** | Uma armadura vazia com um fantasma dentro. Parece decoração até se mexer. A luz mostra quais são. | "Na Galeria das Armaduras, ilumina-as todas antes de passar. A decoração mais perigosa da torre." |

### 9.2 Versões Elite

| Elite | Texto |
|---|---|
| Fantasma Nobre | "Possui dois objetos ao mesmo tempo. Os nobres sempre quiseram mais do que um de tudo." |
| Zombie Inchado | "Explode numa nuvem de veneno quando morre. Mata-o de longe. Muito de longe." |
| Cavaleiro Negro | "A espada dele deixa maldição. Era o melhor da guarda. Ainda é." |
| Gárgula Ancestral | "Cospe ácido. As gárgulas eram canos de chuva. Esta lembra-se disso de forma desagradável." |
| Vampiro Ancião | "Chama dois vampiros. É o avô de alguém. Os avós vampiros são os piores: têm tempo." |
| Grimório | "Um livro que chama mais livros. Uma biblioteca inteira com mau feitio." |
| Banshee Rainha | "O grito parte paredes finas. Às vezes abre caminhos. Às vezes abre-te a ti." |
| Armadura Real | "Dourada, com um fantasma nobre lá dentro. Era o rei de alguma coisa. Agora é o rei de um corredor." |

### 9.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Condessa Sangria** | Vampira de vestido vermelho e leque preto. Vira nuvem de morcegos e "dança" à tua volta. | "O Caçador Van perseguiu-a trinta anos. Diz que dança bem. Diz isso com raiva e com admiração. As duas coisas." |
| **O Jardineiro** | Zombie gigante com chapéu de palha e uma tesoura de poda enorme. Persegue quem entra no labirinto. | "Plantava rosas brancas para a rainha. Agora só nascem negras. Corta as sebes e ri-se. Acho que ri para não chorar." |

### 9.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Sentinela da Muralha** | 71 | Fantasma de arqueiro gigante nas ameias. Dispara chuvas de flechas e grita alerta. | "Ainda vigia o fosso. O inimigo era a torre. A torre entrou por baixo. Não havia ameias para isso." |
| **O Pregoeiro Fantasma** | 72 | Fantasma gordo com um sino gigante. O sino atordoa; a proclamação vira os cidadãos contra ti. | "Anunciava as notícias da cidade. A última notícia foi o fim da cidade. Ele ainda a anuncia. Todas as noites." |
| **Coveiro Ghoul** | 73 | Ghoul curvado com uma pá. Cava, desaparece e levanta mortos. | "Enterrou toda a gente do reino. Depois não havia ninguém para o enterrar a ele. Ficou assim." |
| **Colosso de Ossos** | 74 | Gigante feito de centenas de ossos. Desfaz-se num enxame e volta a montar-se. | "Fechou o túnel há vinte anos a uma equipa de cinco. O Gorvan voltou lá contigo. Escrevo isto e tenho de parar um bocadinho." |
| **Rainha das Rosas Negras** | 76 | Espírito de rainha feito de rosas e espinhos. Faz sangrar e amaldiçoa. | "Não é a rainha. É o que ficou da tristeza dela, no jardim. A tristeza também ganha forma, aqui." |
| **Anjo Caído de Vitral** | 77 | Anjo de vidro de vitral partido e colorido. Cada raio é de um elemento diferente. | "Feito dos vitrais que a torre partiu. Bonito como uma catedral e zangado como um vidro partido." |
| **Carcereiro** | 78 | Brutamontes de capuz com chaves e uma bola com corrente. Prende-te numa cela. | "Guardava os da janela que não queriam subir. Por ordem do rei. Para os proteger. Os carcereiros nunca sabem se são guardas ou prisioneiros." |
| **Comandante dos Cavaleiros Caídos** | 79 | Cavaleiro negro com um estandarte rasgado. Dá força às armaduras vivas. | "Jurou defender o rei até ao fim. O fim chegou e ele não reparou. Fazer o brinde com eles ajuda-os a reparar." |

### 9.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Lich Bibliotecário** (andar 75) | O Que Leu Demais: esqueleto de túnica roxa, óculos partidos e uma coroa de velas. Lê feitiços dos livros que o rodeiam. | "Leu tudo. Todos os livros. Até os que não devia. E no fim só lhe restou guardar os livros dos outros. Tenho medo de acabar assim. Um bocadinho." |
| **Rei Sem Coroa** (andar 80) | O Que Tentou Parar a Torre: rei-cavaleiro de armadura negra e dourada. Luta para alcançar a coroa que flutua. | "Fechou o reino para que ninguém subisse. Achou que a roda parava. A torre engoliu-o. Mas antes de cair disse 'talvez tu'. Os reis cansados dizem coisas verdadeiras." |
| **Rainha Sem Rei** (masmorra Cripta da Rainha) | Fantasma triste da rainha. Ataca com lágrimas e espelhos; numa fase não ataca, só chora. | "Não se vence. Ouve-se. Fala com ela quando chorar. A luta acaba. Há lutas assim." |

## 10. Região 9 — Céu

### 10.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Harpia** | Meio mulher, meio pássaro. Voa à volta das ilhas, agarra-te e larga-te no vazio. | "Não te matam. Só te largam. As nuvens apanham-te. Acho que é uma brincadeira para elas. Uma brincadeira má." |
| **Elemental de Ar** | Um redemoinho com olhos. Não ataca para magoar: ataca para te empurrar para fora da ilha. | "Bater-lhe com uma espada é como bater no vento. Porque é vento. Usa sombra. A sombra pesa." |
| **Pássaro-Trovão** | Águia enorme de penas azuis e amarelas que faíscam. Eriça as penas antes do raio. | "Quando as penas se levantarem, sai de perto. Eu sei que é bonito. Sai de perto na mesma." |
| **Golem Celeste** | Estátua de mármore e ouro com runas azuis. As runas acendem antes do laser. | "Guarda escadas que já não vão dar a lado nenhum. Os golens não perguntam para quê. É a vantagem de ser pedra." |
| **Anjo Guardião** | Guerreiro alado com lança de luz. Cura os outros monstros e torna-os invencíveis um bocadinho. | "Mata-o primeiro. Custa, porque parece um anjo. Mas cura quem te quer matar. Os anjos de verdade não faziam isso. Acho eu." |
| **Valquíria** | Guerreira alada de armadura prateada. Sobe e cai do céu em cima de ti. Andam aos pares. | "Lutam com honra. Se lutares com honra, respeitam-te. Continuam a tentar matar-te, mas com respeito." |
| **Nuvem Viva** | Nuvem fofa com olhos. Parece simpática. As cinzentas trovejam. | "Fofas. Molham-te. Cegam-te. Trovejam. Continuam fofas. O mundo é injusto." |
| **Serpente Alada** | Serpente com asas de penas coloridas que nada no ar em curvas. | "Uma cobra com asas. Achei que já tinha visto tudo. A torre acha sempre que não." |

### 10.2 Versões Elite

| Elite | Texto |
|---|---|
| Harpia Rainha do Vento | "Chama o vento para te levar à borda. Rainha de quê? De quem cai." |
| Elemental do Furacão | "Dois tornados. Um não chegava. Um nunca chega, para os furacões." |
| Pássaro-Trovão Ancião | "O raio salta de um para outro. Quatro de cada vez. Não fiques ao pé dos teus amigos." |
| Golem Dourado | "O laser roda à volta dele. Salta. Salta outra vez. Continua a saltar." |
| Anjo Comandante | "Cura toda a gente à volta. Toda. Mesmo. Começa por ele, ou não acabas nunca." |
| Valquíria de Elite | "Quando cai do céu, o chão treme. Literalmente. Há uma onda. Salta-a." |
| Nuvem de Trovoada | "Grande, escura e zangada. Já não é fofa. Pelo menos é honesta." |
| Serpente Emplumada | "As penas mudam de cor e o elemento muda com elas. Olha para as penas antes de escolher a arma." |

### 10.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Valquíria Sigrun** | Valquíria líder de asas douradas e lança-relâmpago. Pede um duelo justo. | "Conheceu a Capitã Freya no andar 62, há muitos anos. Não sei o que aconteceu entre elas. A Freya também não me diz. Mas a Freya sorriu. Escrevi a data." |
| **Tempestade Viva** | Uma tempestade inteira com uma cara, do tamanho do andar. Só se lhe acerta no olho do centro. | "Os Alados dizem que é a torre zangada. Eu acho que é só uma tempestade que se esqueceu de acabar. Há coisas assim. Há pessoas assim." |

### 10.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Baleia das Nuvens** | 81 | Baleia branca que nada nas nuvens. Esguicha vento e canta para te atordoar. | "Uma baleia que canta no céu. Se não fosse guardiã, eu ia lá só para a ouvir." |
| **Golem-Ilha** | 82 | Um golem que é uma ilha, com uma árvore na cabeça. Inclina-se para te fazer escorregar. | "A árvore da cabeça dá pêssegos. Ele não sabe. Ninguém lhe diz, para ele não ficar vaidoso." |
| **Cavaleiro de Luz Sólida** | 83 | Cavaleiro translúcido feito de luz. Liga e desliga as pontes e faz clones de si mesmo. | "Feito da mesma luz das pontes. Quando morre, a música do andar fica um bocadinho mais triste." |
| **Jardineira Celeste** | 84 | Autómato de jardinagem com regadores e tesouras. Molha-te e depois chama o raio. | "Cuida do jardim para alguém que nunca veio. Ainda corta as flores secas todas as manhãs. Não sei quem programou isto. Sei que gostava de alguém." |
| **Leão Alado de Mármore** | 86 | Leão de mármore com asas. Ruge luz e cai do céu em cima de ti. | "Guardava o Observatório. A Vega dá-lhe os bons-dias, quando passa. Ele não responde. É mármore." |
| **Senhor dos Trovões** | 87 | Gigante pequeno numa nuvem com um martelo de relâmpago. | "'Gigante pequeno'. Escrevi isto e reli três vezes. É isso mesmo: um gigante pequeno. Grande para homem, pequeno para gigante. Zangado com as duas coisas." |
| **Monge do Vento** | 88 | Monge alado muito rápido com um bastão. Desaparece no vento e aparece atrás de ti. | "Os outros monges dizem que ele foi o primeiro a ouvir a respiração no vento. Depois deixou de conseguir parar de a ouvir." |
| **Carruagem do Sol** | 89 | Carruagem dourada puxada por cavalos de fogo. Desce a escadaria a toda a velocidade. | "Leva o sol para cima todas as manhãs. Leva-te a ti para baixo, se estiveres no caminho. Sai do caminho." |

### 10.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Grifo Real** (andar 85) | O Pai dos Ninhos: grifo dourado de crista branca e olhos de âmbar. Fica furioso se te meteres entre ele e o ninho. | "Defende os filhos como a Aranha-Mãe do andar 10. Se te lembrares dela, vais ter vontade de pedir desculpa. Pede. Ele não percebe, mas tu ficas melhor." |
| **Serafim Caído** (andar 90) | O Que Serviu o Administrador: anjo de seis asas, metade luz, metade sombra. Muda de forma conforme o lado da varanda. | "Serviu quem está lá em cima. Diz que o viu chorar. Escrevo isto com a mão a tremer. Se o Administrador chora, então é gente. E se é gente, pode-se falar com ele." |
| **Arcanjo de Bronze** (masmorra Santuário das Asas Perdidas) | Autómato alado antigo de bronze. Lança penas de metal; na 2.ª fase perde as asas e luta no chão. | "Alguém fez anjos de metal para guardar um santuário de asas perdidas. Quem perdeu asas? Quem as fez? A página da masmorra diz. Não te conto. Lê." |

## 11. Região 10 — Abismo

### 11.1 Monstros

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Sombra** | Silhueta escura de olhos brancos. Entra na tua sombra e sai atrás de ti. No escuro quase não sente os golpes. | "Leva luz. Leva mais luz. Quando achares que levas luz que chegue, leva mais." |
| **Olho do Vazio** | Um olho gigante com tentáculos que flutua. Vê-te de muito longe. A pupila encolhe antes do laser. | "Não gosto de ser olhado. Por isto, ainda menos. Ele não pisca para descansar: pisca para aparecer noutro sítio." |
| **Clone Espelhado** | Uma cópia tua de vidro. Usa a tua arma e repete o que fazes, meio segundo depois. | "Para venceres a tua cópia, faz uma coisa que nunca fazes. Ela não sabe o que tu não sabes. É a única vantagem de seres imprevisível." |
| **Devorador de Estrelas** | Criatura enorme e escura que come a luz: apaga as âncoras, as lanternas e a tua luz. | "Abre a boca e as estrelas vão lá para dentro. Ouvi dizer que é por isso que no vazio há tão poucas. Não acredito. Acredito um bocadinho." |
| **Relógio Vivo** | Um relógio de pé com braços e pernas. Para o tempo, acelera e rebobina. | "Quando o tique-taque ficar mais alto, mexe-te. Depois não te mexes, mesmo que queiras. É desagradável. Falo por experiência dos livros." |
| **Eco** | Versões escuras dos monstros das regiões de baixo. Fazem os ataques do original e às vezes repetem-nos. | "A torre lembra-se de tudo o que comeu. Os Ecos são as memórias dela a andar sozinhas. Tristes. Roxas. E com dentes." |
| **Anjo do Vazio** | Anjo negro de asas cheias de estrelas. Servo do Administrador. Faz buracos negros pequenos e cala as tuas skills. | "Os servos dele. Não são maus. Obedecem. Já vi gente boa fazer coisas más só por obedecer. Eu próprio, uma vez, deitei fora um livro." |
| **Fragmento de Mundo** | Golem feito de bocados de todos os biomas. Muda de elemento a cada golpe: a cor diz qual. | "Uma perna de gelo, um braço de lava, uma cabeça de coral. É o mundo inteiro a andar aos tropeções. Bate-lhe com o contrário da cor." |

### 11.2 Versões Elite

| Elite | Texto |
|---|---|
| Sombra Maior | "Duas a sair da tua sombra ao mesmo tempo. Começo a ter medo da minha. Não é bom para um velho." |
| Olho Ancião | "Três lasers. Um olho com três olhares. A matemática da torre é estranha." |
| Clone Perfeito | "Tão forte como tu. Quer dizer que és forte. Parabéns. Agora foge." |
| Devorador de Galáxias | "Puxa-te para a boca com mais força. Corre para longe. Correr para longe é uma estratégia. Está nos livros." |
| Relógio de Ouro | "Para o tempo dois segundos. Em dois segundos lê-se uma frase inteira. Ou leva-se um golpe inteiro." |
| Eco Brilhante | "Repete tudo. Tudo. É como uma criança que aprendeu uma palavra nova." |
| Anjo do Vazio Superior | "Dois buracos negros. Não fiques entre eles. Escrevo isto como se fosse óbvio. É óbvio. Mas escrevo." |
| Fragmento de Continente | "Muda de elemento a cada dois segundos. Leva uma arma de cada. Ou uma mítica. Ou desiste e vai lanchar." |

### 11.3 Monstros com nome

| Monstro | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Devorador Ancestral** | Um devorador do tamanho do andar, que come as estrelas do céu. O andar vai escurecendo. Luta-se com fragmentos de luz atirados à boca. | "A Capitã Freya diz que é a maior coisa que já viu num relatório. A Freya não exagera. Nunca. Fiquei a olhar para o relatório uma hora." |
| **O Jogador Sem Número** | Figura de capa cinzenta e máscara branca. A janela por cima dele diz "????". Fala contigo enquanto luta. | "O nome raspado da pirâmide. Recusou a coroa há trezentos anos. Chama-se Simão. Escrevo o nome em letra grande. Os nomes precisam de ser escritos em letra grande, às vezes." |

### 11.4 Guardiões

| Guardião | Andar | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|---|
| **Porteiro do Vazio** | 91 | Figura alta de capuz estrelado, com uma chave enorme. Abre portais e prende-te numa dimensão pequenina. | "Guarda a porta para dentro da torre. Não é a porta de entrada. É a porta para o sítio onde a torre se lembra de ser torre." |
| **Baleia Estelar** | 92 | Baleia feita de constelações. Canta, chama cometas e engole as estrelas do caminho. | "Primo da Baleia das Nuvens? Não sei. Mas canta melhor. Quer dizer, mais longe." |
| **Rainha dos Espelhos** | 93 | Figura de vidro com coroa. Aparece em todos os espelhos; só a verdadeira tem a coroa a brilhar. | "Troca de lugar contigo. Pensa nisso: há um segundo em que és tu a rainha. Aproveita para bater." |
| **Eco dos Guardiões** | 94 | Muda de forma a cada 20% de vida: é um guardião antigo diferente de cada vez. | "Todos os guardiões que venceste a voltar ao mesmo tempo. A torre é rancorosa. Ou saudosa. Não sei distinguir." |
| **Gigante Invertido** | 96 | Gigante de cabeça para baixo que anda no "céu". Inverte a gravidade e atira pedras para cima. | "Para ele, quem está de pernas para o ar és tu. Tem razão, de um certo ponto de vista. Do dele." |
| **O Desistente** | 97 | Jogador nº 7 777, de armadura velha e muitas armas às costas. Troca de arma a cada fase e fala contigo. | "Quarenta anos sentado num caixote. Depois de vencido, ajuda os outros a levantarem-se. Às vezes é preciso perder para se ter coragem." |
| **Índice Vivo** | 98 | Livro gigante com olhos e páginas a voar. Lê ataques de bosses antigos e fecha-se como um escudo. | "Um livro que lê os outros livros e os atira à cabeça. Se eu fosse um livro, era este. Não digas à Arquivista." |
| **O Guardião da Escada** | 99 | Anjo do vazio enorme de quatro asas e espada estelar. Dá vida às estátuas dos bosses por um momento. | "Desobedeceu ao Administrador para te pôr à prova. Os bons guardas desobedecem quando é preciso. Já não se fazem assim." |

### 11.5 Mini-boss, boss e masmorra

| Boss | Descrição (★) | Nota do Fausto (★★★) |
|---|---|---|
| **Guardião do Tempo** (andar 95) | O Que Te Viu Mil Vezes: figura de bronze com um relógio no lugar da cara e quatro braços. Faz bolhas de tempo e rebobina. | "Diz que viu passar mil Jogadores. Para ele somos todos o mesmo. Não sei se isso é triste ou bonito. Escrevi as duas palavras. Risquei as duas." |
| **O Administrador** (andar 100) | Aren, Jogador nº 1: primeiro um homem cansado de cabelo branco; depois uma figura enorme feita de janelas azuis. | "Tinha dezasseis anos. Um cão chamado Farol. Desenhava mapas. Esteve mil anos sozinho a carregar no 'Não'. Esta nota não é de bestiário. Não sei onde mais a pôr." |
| **O Primeiro Erro** (masmorra O Andar Zero) | Um *bug* do Sistema: muda de forma para outros bosses durante um instante, teletransporta-se, os ataques vêm de sítios errados. | "Um erro com vida. O primeiro de todos. Se o Sistema tem erros, então foi feito por alguém. E quem faz pode desfazer." |
