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
