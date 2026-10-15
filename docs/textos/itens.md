# Descrições dos itens

O texto que aparece na **caixa de informação** de cada item (inventário, lojas, baús). Os números (ATQ, preço,
efeitos) são mostrados pelo jogo a partir dos dados; aqui está só a **descrição**.

## Regras
- **1 ou 2 frases**, no máximo **~120 letras**. Primeiro o que é ou para que serve; depois, se couber, um toque de humor ou de mundo.
- Não repetir os números que o jogo já mostra (não escrever "cura 30%": isso aparece por baixo, em verde).
- Itens de missão dizem **para quem são** ou **o que fazer com eles**.
- **ID** igual ao dos dados (`dados/itens.json`, `dados/armas.json`); a chave de tradução é `item_<id>_desc`.

A caixa de informação mostra, por esta ordem: **nome** (cor da raridade) · tipo · números · **descrição** · preço de venda.

---

## Região 1 — Floresta

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `minerio_cobre` | Minério de Cobre | Pedra com veios cor de laranja. Na forja vira lingote. |
| `lingote_cobre` | Lingote de Cobre | Cobre fundido e limpo. A base de quase tudo o que se forja na floresta. |
| `carvalho` | Madeira de Carvalho | Madeira forte e honesta. Serve para cabos, arcos, móveis e para alimentar a forja. |
| `seiva_cristalizada` | Seiva Cristalizada | Seiva antiga que endureceu como vidro. O cristal da floresta: precisa-se dela para melhorias a sério. |
| `couro_javali` | Couro de Javali | Grosso e áspero. Dá boas manoplas e armaduras que cheiram ligeiramente a javali. |
| `linho_bravo` | Linho Bravo | Fibras de uma planta alta. Torcidas, viram fio para arcos e roupa. |
| `erva_verde` | Erva Verde | Cresce em todo o lado. O primeiro ingrediente de qualquer Poção de Vida. |
| `flor_de_mel` | Flor de Mel | Flor amarela que cheira a doce. As abelhas adoram-na. A Lyra também. |
| `cogumelo_luminoso` | Cogumelo Luminoso | Brilha no escuro. Bom para poções de MP e para não tropeçar à noite. |
| `mel_azul` | Mel Azul | Mel das colmeias do andar 6. Azul, doce, e ninguém sabe bem porquê. |
| `po_de_fada` | Pó de Fada | Brilha entre os dedos e faz cócegas. Usa-se em poções rápidas e encantamentos fracos. |
| `po_de_fada_dourado` | Pó de Fada Dourado | Pó de fada raro, cor de ouro. As fadas do andar 4 querem-no de volta. |
| `bolota_dourada` | Bolota Dourada | Uma bolota que brilha. Plantada, dá uma Árvore Dourada. |
| `rubi_pequeno` | Rubi Pequeno | Uma lasca de rubi encontrada no cobre. Pouco brilho, mas quente ao toque: tem Fogo dentro. |
| `gel_slime` | Gel de Slime | Verde, mole, ligeiramente vivo. Quase ninguém o quer como presente. |
| `gel_real` | Gel Real | Gel do Slime Rei. Mais firme, dourado, e com cheiro a peixe. |
| `chifre_pequeno` | Chifre Pequeno | Chifre de Coelho-Chifre. Dizem que dá sorte. Não dá. |
| `pelo_macio` | Pelo Macio | Pelo de coelho, macio como uma nuvem. Bom para forrar capas. |
| `pele_lobo` | Pele de Lobo | Pele cinzenta e quente. Os lenhadores pagam bem por ela no inverno. |
| `presa_lobo` | Presa de Lobo | Uma presa afiada. Ingrediente da Poção de Força. |
| `presa_negra` | Presa Negra | Presa do Lobo Cicatriz. Escura como a noite em que caiu. |
| `presa_javali` | Presa de Javali | Curva e dura. Os ferreiros usam-na em punhos de armas. |
| `presa_real` | Presa Real | Presa do Javali-Rei, rachada de mil cargas. Um troféu e um material raro. |
| `carne` | Carne | Carne crua. Melhor cozinhada. Muito melhor cozinhada. |
| `carne_coelho` | Carne de Coelho | Carne magra. Numa espetada, à fogueira, é o jantar de qualquer aventureiro. |
| `carne_javali` | Carne de Javali | Muita carne, muito sabor. O Brom diz que é a melhor comida do mundo. |
| `esporo` | Esporo | Pó dos Cogumelos Andantes. Venenoso para respirar, útil para Antídotos. |
| `chapeu_cogumelo` | Chapéu de Cogumelo | O chapéu de um Cogumelo Andante. Dá para cozinhar. Dá para usar. Não recomendamos usar. |
| `asa_de_fada` | Asa de Fada | Fina como papel de seda. Brilha com as cores do arco-íris. |
| `mel` | Mel | Mel normal, dourado. Doce para cozinhar. |
| `ferrao` | Ferrão | Ferrão de Abelha-Gigante. Ainda pica. Cuidado ao meter a mão na mochila. |
| `cera` | Cera | Cera de abelha. Faz velas, móveis brilhantes e Velas Sagradas. |
| `madeira_viva` | Madeira Viva | Madeira de Treant. Ainda tem folhas pequenas a crescer. Ótima para cajados. |
| `madeira_fulminada` | Madeira Fulminada | Madeira atingida por um raio. Ainda faz faíscas. Rara e cobiçada pelo Gizmo. |
| `folha_dourada` | Folha Dourada | Folha do Coração da Floresta. Não murcha. |
| `hera` | Hera | Trepadeira das ruínas. Decorativa e boa para cordas. |
| `pedra_trabalhada` | Pedra Trabalhada | Pedra cortada por mãos antigas. Serve para construir. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_treino` | Espada de Treino | A espada que o Gorvan dá a todos os Jogadores novos. Rombuda, honesta e com o teu nome riscado no cabo. |
| `espada_cobre` | Espada de Cobre | A primeira espada a sério. Equilibrada, simples, fiável. |
| `espada_grande_cobre` | Espada Grande de Cobre | Pesada e larga. Cada golpe varre tudo à frente. |
| `adaga_cobre` | Adaga de Cobre | Pequena e rápida. Faz o dobro pelas costas. |
| `katana_cobre` | Katana de Cobre | Lâmina curva e fina. O Kai diz que no mundo dele isto era "muito fixe". |
| `machado_cobre` | Machado de Cobre | Corta inimigos e árvores. Às vezes as duas coisas são a mesma. |
| `martelo_cobre` | Martelo de Cobre | Lento, pesado e convincente. Também parte rochas. |
| `lanca_cobre` | Lança de Cobre | Mantém os inimigos longe. E atravessa dois de uma vez. |
| `foice_cobre` | Foice de Cobre | Ceifa em arco largo. Rouba um bocadinho de vida a cada golpe. |
| `arco_cobre` | Arco de Cobre | Flechas infinitas. Ninguém sabe de onde vêm. Ninguém pergunta. |
| `besta_cobre` | Besta de Cobre | Lenta a recarregar, mas o virote atravessa escudos. |
| `cajado_cobre` | Cajado de Cobre | Dispara energia mágica. Encaixa uma gema e muda o elemento. |
| `manoplas_cobre` | Manoplas de Cobre | Seis socos num piscar de olhos. Para quem gosta de estar perto. |
| `arco_curto_carvalho` | Arco Curto de Carvalho | Feito pelos elfos de Folhalta. Leve, bonito e certeiro. |
| `chifre_partido` | Chifre Partido | O chifre do Coelho-Chifre Ancião, afiado como adaga. Dá pernas rápidas a quem o leva. |
| `pena_noturna` | Pena-Noturna | Arco da Coruja Sombria. Faz mais dano a quem ainda não te viu. |
| `martelo_pinca` | Martelo Pinça | A pinça do Lagostim Couraçado num cabo. Parte cascas e couraças. |
| `esporo_luz` | Esporo-Luz | Cajado da Rainha dos Esporos. Os projéteis deixam esporos venenosos no chão. |
| `ferrao_de_mel` | Ferrão-de-Mel | Lança da Abelha-Rainha. Envenena e cura um pouco a cada inimigo vencido. |
| `tronco_velho` | Tronco-Velho | Espada grande feita do Guardião de Musgo. Enquanto a seguras, sentes-te mais forte. |
| `lamina_cavaleiro_esquecido` | Lâmina do Cavaleiro Esquecido | A espada partida do cavaleiro de pedra. Ainda se lembra de um quarto golpe. |
| `foice_bruma` | Foice Bruma | Foice da Serpente da Névoa. Às vezes desapareces no meio do golpe. |
| `presa_javali_rei` | Presa do Javali-Rei | Machado feito da presa do Rei das Tocas. O ataque carregado derruba como uma carga de javali. |
| `raiz_ancestral` | Raiz Ancestral | Cajado do Ent Ancião. As raízes ainda se lembram de proteger: prendem os inimigos. |
| `arco_raiz_viva` | Arco Raiz-Viva | Arco secreto da Toca das Raízes. Cada flecha tem uma semente; algumas prendem o alvo. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `couro_javali_cabeca` | Capuz de Couro de Javali | Protege a cabeça e cheira a floresta. |
| `couro_javali_corpo` | Gibão de Couro de Javali | Grosso e confortável. A primeira armadura de muitos aventureiros. |
| `couro_javali_maos` | Luvas de Couro de Javali | Para segurar a arma sem bolhas. |
| `couro_javali_pes` | Botas de Couro de Javali | Boas para lama, erva alta e fugir de javalis. |
| `couro_javali_capa` | Capa de Linho Bravo | Leve. Esvoaça bem quando corres. |
| `coroa_de_gel` | Coroa de Gel | A coroa do Slime Rei. Ainda abana quando andas. |
| `manto_cicatriz` | Manto Cicatriz | Feito da pele do Lobo Cicatriz. À noite, corres como ele. |
| `anel_sussurro` | Anel do Sussurro | Encontrado numa árvore oca. Às vezes ouves um sussurro perto de segredos. |
| `anel_vigia` | Anel do Vigia | Dado pelo Velho Cass. Os teus olhos veem mais longe no nevoeiro e no escuro. |
| `amuleto_nevoa` | Amuleto da Névoa | Do Altar do Reflexo. Frio ao toque. No nevoeiro, os inimigos falham mais. |
| `faixa_aprendiz` | Faixa de Aprendiz | O Gorvan dá-a a quem passa a Prova de Força. Ele nunca diz "parabéns". Isto é o "parabéns". |
| `bussola_darian` | Bússola de Darian | Era do pai da Lyra. A agulha aponta sempre para a Zona Segura mais próxima. Para casa. |
| `bolsa_viagem` | Bolsa de Viagem | +5 espaços na mochila. Presente da Lyra pela Entrega Rápida. |
| `bolsa_materiais` | Bolsa de Materiais | Da Guilda, para aventureiros de confiança. Os materiais não ocupam espaço. |
| `mochila_couro` | Mochila de Couro | Feita pela Elva. Mais espaço, costuras fortes. |

### Ferramentas

| ID | Nome | Descrição |
|---|---|---|
| `picareta_cobre` | Picareta de Cobre | Parte minério de cobre e pedras do rio. Não te atrevas com prata. |
| `machado_lenhador_cobre` | Machado de Lenhador de Cobre | Corta carvalhos. O Bruno diz que se ouve a árvore a pedir desculpa. |
| `cana_bambu` | Cana de Bambu | A primeira cana. Leve e flexível. O Pip deu-ta com uma sesta pelo meio. |

### Consumíveis

| ID | Nome | Descrição |
|---|---|---|
| `pocao_vida_p` | Poção de Vida P | Vermelha e com sabor a morango falso. Fecha feridas pequenas. |
| `pocao_mana_p` | Poção de Mana P | Azul e fresca. Devolve um pouco de magia. |
| `pocao_estamina` | Poção de Estamina | Amarela, com mel. Para correr e esquivar mais. |
| `pocao_elfica` | Poção Élfica | Receita de Folhalta. Cura o corpo e a magia ao mesmo tempo. |
| `antidoto` | Antídoto | Tira o veneno. Sabe a erva e a arrependimento. |
| `ligadura` | Ligadura | Linho limpo para parar o sangue. |
| `colirio` | Colírio | Duas gotas e voltas a ver. |
| `pocao_forca` | Poção de Força | Com presa de lobo. Durante uns minutos, bates como um javali. |
| `pocao_velocidade` | Poção de Velocidade | Pó de fada dissolvido. Faz cócegas nos pés. |
| `pocao_encolher` | Poção de Encolher | A "poção impossível" da Selene. Ficas pequeno uns segundos. Não bebas perto de gatos. |
| `tocha` | Tocha | Luz e fogo. Acende fogueiras e queima teias. Apaga-se com o tempo. |
| `pedra_regresso` | Pedra de Regresso | Aperta-a, espera três segundos e acordas em Ascendia. Não funciona a meio de uma luta. |
| `frasco_vagalumes` | Frasco de Vaga-lumes | Vaga-lumes do Bosque Escuro num frasco. Luz por uns minutos. Solta-os depois. |
| `isco` | Isco | Uma minhoca com ambições. |
| `isco_dourado` | Isco Dourado | Os peixes grandes não lhe resistem. O Pip guarda-os numa caixa só para eles. |

### Comida

| ID | Nome | Descrição |
|---|---|---|
| `truta_grelhada` | Truta Grelhada | Truta do ribeiro com sal, feita na fogueira. Simples e perfeita. |
| `espetada_coelho` | Espetada de Coelho | O jantar clássico do aventureiro. Quente, rápido, sem pratos para lavar. |
| `sopa_legumes` | Sopa de Legumes | A sopa da Dona Marta. Dizem que cura tudo. Pelo menos cura a fome. |
| `sopa_cogumelos` | Sopa de Cogumelos | Cremosa e brilhante. Usa cogumelos luminosos: a tigela brilha no escuro. |
| `panquecas_mel_azul` | Panquecas de Mel Azul | Fofas, douradas e com mel azul a escorrer. A comida preferida da Lyra. |
| `torta_maca` | Torta de Maçã Selvagem | Maçãs do pomar dos javalis. Os javalis não foram consultados. |
| `morangos_natas` | Morangos com Natas | Morangos de Folhalta com natas frescas. Sabem a verão. |
| `assado_javali` | Assado de Javali | Carne, cebola e batata no forno. O Brom fica de bom humor só de cheirar. |
| `maca_selvagem` | Maçã Selvagem | Vermelha e ácida. Os javalis adoram-na: atira-a e eles esquecem-se de ti. |
| `maca_dourada` | Maçã Dourada | Da Árvore Dourada. A primeira que comes deixa-te mais forte para sempre. Todos a adoram como presente. |
| `folha_com_mel` | Folha com Mel | Comida das fadas: uma folha com uma gota de mel. Pouca, mas encantada. |

### Peixes

| ID | Nome | Descrição |
|---|---|---|
| `truta_ribeiro` | Truta do Ribeiro | Pintalgada e rápida. Gosta de água fria e corrente. |
| `perca_prateada` | Perca Prateada | Brilha como uma moeda. Morde quase sempre. |
| `peixe_folha` | Peixe-Folha | Parece uma folha a boiar. Só aparece com chuva. |
| `carpa_dourada` | Carpa Dourada | Dourada e preguiçosa. Só acorda de manhã cedo. |
| `enguia_musgo` | Enguia do Musgo | Verde, escorregadia e noturna. Vive nas fontes das ruínas. |
| `rei_lago_nevoento` | Rei do Lago Nevoento | **Lendário.** Um peixe enorme e velho, de escamas brancas. Só nada na névoa do amanhecer. |
| `bota_velha` | Bota Velha | Não é um peixe. O Gizmo transforma-a em peças. |
| `lata` | Lata | Não é um peixe. De onde vêm as latas, dentro de uma torre? |
| `alga_seca` | Alga Seca | Não é um peixe. Nem é bonita. |

### Sementes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `semente_nabo_bravo` | Sementes de Nabo Bravo | Crescem na primavera. O nabo mais teimoso do mundo. |
| `semente_morango` | Sementes de Morango Silvestre | De Folhalta. Primavera e verão. Dão mais de uma vez. |
| `semente_batata_pradaria` | Sementes de Batata da Pradaria | Encontradas na erva alta do andar 1. Primavera e outono. |
| `semente_flor_mel` | Sementes de Flor de Mel | Plantar perto das colmeias dá Mel Azul. |
| `nabo_bravo` | Nabo Bravo | Rijo e picante. Bom em sopas. |
| `morango_silvestre` | Morango Silvestre | Pequeno, vermelho e muito doce. |
| `batata_pradaria` | Batata da Pradaria | Batata pequena com sabor a terra boa. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `pedra_inicial` | Pedra | É uma pedra. Parabéns. (A primeira coisa que apanhaste neste mundo. Não a deites fora. Ou deita.) |
| `formulario_guilda` | Formulário da Guilda | Um formulário de inscrição que o vento levou. A Lyra quer os cinco de volta. |
| `carta_lyra` | Carta da Lyra | Carta urgente da Guilda. Tem de ser entregue hoje. HOJE. |
| `carta_eldrin` | Carta do Eldrin | Carta do irmão da Selene. A letra é apressada e alegre. |
| `resposta_selene` | Resposta da Selene | A resposta da Selene ao irmão. Tem uma mancha de poção no canto. |
| `caixa_tobias` | Caixa para o Tibério | Pesada e fechada. O Tobias diz que não é para abrir. Abana como se tivesse moedas. |
| `cristal_seiva` | Cristal de Seiva | Um dos 4 cristais que abrem a Raiz Oca. Brilha mais perto dos altares. |
| `chave_ruinas` | Chave das Ruínas | Chave de pedra verde. Abre o baú de ouro do Templo Enterrado. |
| `chave_bau_ouro_ilhota` | Chave Molhada | Estava num ninho na Ilhota. Abre o baú atrás da cascata. |
| `ovo_ouro_javali` | Ovo de Ouro do Javali | Ninguém sabe como um javali pôs um ovo de ouro. Os animais de estimação adoram-no. |
| `ovo_slime_bebe` | Ovo de Slime | Um ovo verde e mole que salta sozinho. O Zed pode chocá-lo. |
| `semente_arvore_mae` | Semente da Árvore-Mãe | A última semente da Árvore-Mãe. "Planta-a num sítio onde haja gente." |
| `trofeu_javali_rei` | Cabeça do Javali-Rei | Troféu para pendurar na parede de casa. Os olhos parecem seguir-te. |
| `trofeu_ramo_ent` | Ramo do Ent | Troféu. Na primavera dá flores. |
| `lanterna_papel` | Lanterna de Papel | Para pôr no rio na Noite das Lanternas, por alguém de quem tens saudades. |
| `pagina_diario` | Página Antiga | Uma página de um diário antigo, com letra de rapaz. Lê-a no Diário. |

---

## Região 2 — Cavernas e Minas

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `minerio_ferro` | Minério de Ferro | Pedra cinzenta e pesada. Com carvão, vira lingote. |
| `lingote_ferro` | Lingote de Ferro | Ferro fundido. Mais duro do que o cobre e muito menos bonito. |
| `carvao` | Carvão | Pedra preta que arde. Daqui para cima, as forjas comem carvão. |
| `escora_velha` | Escora Velha | Viga de madeira das minas, seca há anos. Boa para cabos e bestas. |
| `fungo_lenho` | Fungo-Lenho | O caule de um fungo gigante. Duro como madeira e leve como cortiça. |
| `couro_toupeira` | Couro de Toupeira | Macio por fora, resistente por dentro. Cheira a terra. |
| `seda_aranha` | Seda de Aranha | O fio mais forte e mais leve que existe. A Elva quer tudo. |
| `cristal_gruta` | Cristal de Gruta | Brilha sozinho e canta quando lhe tocas. Usa-se em melhorias e cajados. |
| `topazio` | Topázio | Gema amarela com um raio preso lá dentro. |
| `rubi` | Rubi | Gema vermelha, quente ao toque. Fogo em pedra. |
| `ametista` | Ametista | Gema violeta. Os anões diziam que traz sonhos sem pesadelos. |
| `musgo_luminoso` | Musgo Luminoso | Musgo que brilha nas paredes. Com ele vês no escuro. |
| `raiz_pedra` | Raiz-Pedra | Raiz tão dura que parece pedra. Dá Poções de Defesa. |
| `engrenagem` | Engrenagem | Roda dentada de uma engenhoca goblin. O Gizmo dá tudo por elas. |
| `guano` | Guano | Cocó de morcego. Nojento. O melhor fertilizante da quinta. |
| `asa_morcego` | Asa de Morcego | Fina como papel. Cheira mal. |
| `pano_velho` | Pano Velho | Trapo dos goblins. Serve para bombas. Para mais nada. |
| `pedra` | Pedra | Uma pedra. Para construir. Ou para atirar. |
| `nucleo_golem` | Núcleo de Golem | Uma pedra redonda que ainda aquece. Dizem que é o coração do golem. |
| `garra_toupeira` | Garra de Toupeira | Curva e afiada. Faz bons ganchos. |
| `glandula_veneno` | Glândula de Veneno | Cuidado: pinga. Usa-se em poções e armas envenenadas. |
| `olho_aranha` | Olho de Aranha | Um dos oito. Ainda parece estar a olhar. |
| `lanterna_partida` | Lanterna Partida | Lanterna de kobold. O Gizmo arranja. |
| `escama_cristal` | Escama de Cristal | Escama da Lagarta de Cristal. Devolve a luz. |
| `ectoplasma` | Ectoplasma | Gosma de fantasma. Fria, brilhante, detestada por quase todos. |
| `lingote_antigo` | Lingote Antigo | Ferro dos anões fantasmas. Sempre de qualidade Boa. |
| `garra_dourada` | Garra Dourada | Da Toupeira Dourada. Vale uma fortuna e dá sorte a quem cava. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_ferro` | Espada de Ferro | Sem enfeites. Corta, aguenta, não reclama. |
| `espada_grande_ferro` | Espada Grande de Ferro | Uma barra de ferro com fio. Precisa das duas mãos e de alguma fé. |
| `adaga_ferro` | Adaga de Ferro | Rápida e escondida. Ótima no escuro. |
| `katana_ferro` | Katana de Ferro | Curva e afiada. O ferro escuro não brilha: ninguém a vê chegar. |
| `machado_ferro` | Machado de Ferro | Abre crânios e escoras. |
| `martelo_ferro` | Martelo de Ferro | O melhor amigo de quem luta contra golens. |
| `lanca_ferro` | Lança de Ferro | Longa o suficiente para não teres de ver a cara da aranha. |
| `foice_ferro` | Foice de Ferro | Ceifa em arco. Nos túneis estreitos, cuidado com as paredes. |
| `arco_ferro` | Arco de Ferro | Arco reforçado com ferro. Aguenta a humidade das grutas. |
| `besta_ferro` | Besta de Ferro | Pesada e precisa. Os virotes atravessam carapaças. |
| `cajado_ferro` | Cajado de Ferro | Cajado com ponta de ferro. Não é elegante. Funciona. |
| `manoplas_ferro` | Manoplas de Ferro | Para socos que se ouvem do outro lado da mina. |
| `martelo_carril` | Martelo Carril | Feito de um carril da Vagoneta Assombrada. O ataque carregado corre em linha como um comboio. |
| `chifre_picareta` | Chifre-Picareta | Machado do Touro das Galerias. Também mina, como uma picareta boa. |
| `cajado_prisma` | Cajado Prisma | Cada disparo sai com uma cor e um elemento diferentes. Nunca sabes qual. |
| `remo_barqueiro` | Remo do Barqueiro | Uma lança que era um remo. Empurra muito e adora inimigos molhados. |
| `foice_micelio` | Foice Micélio | Os golpes deixam esporos que te curam. Cheira a cogumelo. |
| `besta_ressonante` | Besta Ressonante | Os virotes fazem eco e ressaltam para outro inimigo. |
| `manoplas_fornalha` | Manoplas da Fornalha | Ainda quentes. O último golpe do combo queima. |
| `lamina_reflexo` | Lâmina Reflexo | Katana do Reflexo Negro. Às vezes o golpe acontece duas vezes. |
| `presa_venenosa` | Presa Venenosa | Adaga feita da presa da Aranha-Mãe. Envenena. |
| `nucleo_cristal` | Núcleo de Cristal | Martelo com o coração do Golem. O ataque carregado faz ondas de cristal. |
| `martelo_vagoneta` | Martelo de Vagoneta | O martelo do Rei Gruk. Faz ondas de choque pequenas. E barulho grande. |
| `machado_rei_montanha` | Machado do Rei Sob a Montanha | Arma secreta da Mina do Rei Anão. Odeia golens e mina como uma picareta muito boa. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `ferro_cabeca` | Elmo de Ferro | Pesado. Bate-se com a cabeça nas vigas e é a viga que se queixa. |
| `ferro_corpo` | Couraça de Ferro | Ferro e couro de toupeira. Com o conjunto completo, brilha um pouco no escuro. |
| `ferro_maos` | Luvas de Ferro | Para segurar picaretas e martelos sem bolhas. |
| `ferro_pes` | Botas de Ferro | Fazem barulho nos túneis. Os goblins ouvem-te chegar. Fogem. |
| `ferro_capa` | Capa de Seda de Aranha | Leve e forte. Não rasga nas pedras. |
| `coroa_latao` | Coroa de Latão | A coroa do Rei Gruk. Não é de ouro. Dá ouro na mesma. |
| `capacete_mineiro` | Capacete de Mineiro | Com uma lanterna em cima. Nunca mais ficas às escuras. |
| `amuleto_espelho` | Amuleto do Espelho | Um pequeno espelho negro. Devolve parte da magia que te atiram. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_ferro` | Picareta de Ferro | Parte ferro e cristal. A partir daqui, a mina é tua. |
| `machado_lenhador_ferro` | Machado de Lenhador de Ferro | Corta escoras e caules de fungos gigantes. |
| `gancho` | Gancho | Engenhoca do Gizmo. Aponta a um anel brilhante e voa até lá. Às vezes contra a parede. |
| `giz_mineiro` | Giz de Mineiro | Desenha setas nas paredes. Aparecem no mapa. Nunca te percas. |
| `pa_dourada` | Pá Dourada | Da Toupeira Dourada. Escava os pontos de tesouro. |
| `mapa_tuneis` | Mapa dos Túneis | Desenhado de memória pelo Senhor Ruivo. Mostra o labirinto do andar 12. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `pocao_luz` | Poção de Luz | Bebe e brilhas. Não é bonito, mas vês. |
| `pocao_visao_noturna` | Poção de Visão Noturna | Os olhos ficam como os de um gato por uns minutos. |
| `pocao_defesa` | Poção de Defesa | Sabe a pedra. A pele fica como pedra. |
| `bomba` | Bomba | Pólvora num pano. Acende, atira, foge. Por esta ordem. |
| `batatas_roxas_assadas` | Batatas Roxas Assadas | Batatas da gruta assadas na brasa. Brilham um bocadinho. |
| `pao_fungo` | Pão de Fungo | Receita dos fungoides. Azul por dentro. Melhor do que parece. |
| `sopa_mineiro` | Sopa de Mineiro | Grossa, quente e com raiz-pedra. Para quem trabalha debaixo da terra. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `peixe_cego` | Peixe-Cego | Branco e sem olhos. Não precisa deles: nunca viu luz. |
| `caranguejo_gruta` | Caranguejo de Gruta | Pequeno e mal-humorado. Belisca. |
| `carpa_cristal` | Carpa de Cristal | As escamas parecem vidro. Vê-se a espinha. |
| `truta_fungica` | Truta Fúngica | Tem musgo nas barbatanas. Os fungoides dizem que é parente deles. |
| `enguia_eletrica` | Enguia Elétrica | Dá choque mesmo depois de pescada. Pega com luvas. |
| `peixe_vidro` | Peixe de Vidro | **Lendário.** Transparente como água. Só aparece de madrugada nos buracos do lago negro. |
| `semente_fungo_azul` | Esporos de Fungo Azul | Plantam-se à sombra. Dão fungos azuis o ano todo. |
| `fungo_azul` | Fungo Azul | Brilha um pouco. Bom em pão e em poções de luz. |
| `batata_roxa` | Batata Roxa da Gruta | Cresce no escuro. Roxa por dentro e por fora. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `diario_mineiro` | Diário de Mineiro | O diário de um dos mineiros perdidos do andar 12. A última página tem um número. |
| `martelo_forte_rocha` | Martelo Forte-Rocha | O martelo do pai do Brom. O cabo tem a marca dos dedos dele. Leva-o ao Brom. |
| `livro_runas_anas` | Livro de Runas Anãs | Receitas de armas de ferro melhores. E a chave da mina do rei esquecido. |
| `ametista_grande` | Ametista Grande | Da Sala Violeta. Do tamanho de um punho. O Fausto quer vê-la. |
| `remo_dourado` | Remo Dourado | Decoração. Estava escondido atrás de uma cascata escura. Ninguém sabe de quem era. |
| `ovo_morceguinho` | Ovo de Morceguinho | Um ovo pequeno e quente, pendurado de cabeça para baixo. O Zed sabe chocá-lo. |
| `ovo_aranha_dourado` | Ovo de Aranha Dourado | Do casulo dourado do ninho. Nasce uma aranha que tece seda em tua casa. |
| `trofeu_teia_dourada` | Teia Dourada | Troféu da Aranha-Mãe. Brilha à luz das velas. |
| `trofeu_fragmento_nucleo` | Fragmento do Núcleo | Troféu do Golem de Cristal. Ilumina uma sala inteira. |
| `chave_casa` | Chave da Casa | Rua das Glicínias, número 7. A tua casa. |

---

## Região 3 — Pântano e Selva

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `minerio_ferro_negro` | Minério de Ferro Negro | Ferro escuro que nasce no lodo. Com carvão, dá aço. |
| `lingote_aco` | Lingote de Aço | Três de ferro negro e um de carvão. Mais duro, mais leve, mais caro. |
| `madeira_mangue` | Madeira de Mangue | Vive com os pés na água e não apodrece. Boa para barcos e arcos. |
| `junco` | Junco | Talo comprido e oco. Os sapos fazem pontes com ele. |
| `pele_crocodilo` | Pele de Crocodilo | Grossa e cheia de escamas. Aguenta dentadas. De outros crocodilos, até. |
| `fibra_liana` | Fibra de Liana | Corda que cresce nas árvores. A selva já te dá o fio feito. |
| `ambar_pantano` | Âmbar do Pântano | Resina antiga, dourada e transparente. Às vezes tem lá dentro coisas que já não existem. |
| `ambar_mosquito` | Âmbar com Mosquito | Um mosquito preso no âmbar há milhares de anos. O Barão Coaxim paga uma fortuna. Ninguém sabe porquê. |
| `esmeralda` | Esmeralda | Gema verde das grutas da cascata. Guarda veneno lá dentro. |
| `esmeralda_grande` | Esmeralda Grande | Do tamanho de um ovo. Os sapos acham que dá sorte. Dá, se a venderes ao Barão. |
| `lirio_pantano` | Lírio do Pântano | Flor branca que limpa a água à volta. Boa para poções e para presentes. |
| `musgo_medicinal` | Musgo Medicinal | Musgo macio e húmido. Põe-se nas feridas. Arde um bocadinho. |
| `banana` | Banana | Amarela, doce e cheia de energia. Os macacos não partilham. |
| `cacau` | Cacau | Grão amargo de uma vagem amarela. Com leite e açúcar, deixa de ser amargo. |
| `cafe_selva` | Café da Selva | Grão vermelho que acorda os mortos. Bem, os cansados. |
| `coco` | Coco | Duro por fora, água fresca por dentro. Abre-se com uma pedra. Ou com a cabeça de alguém. |
| `pimenta_selva` | Pimenta da Selva | Vermelha e pequena. Pequena demais para tanto fogo. |
| `pele_sapo` | Pele de Sapo | Fina e escorregadia. Usa-se em luvas que nunca deixam cair nada. |
| `muco_sapo` | Muco de Sapo | Nojento e útil. Cola tudo. Até os dedos. |
| `pele_dourada` | Pele Dourada | A pele do Sapo Dourado. Brilha como ouro e vale quase o mesmo. Tesouro. |
| `escama_lagarto` | Escama de Lagarto | Escama verde e dura. Com ela fazem-se armaduras leves e a Poção de Escamas. |
| `dente_lagarto` | Dente de Lagarto | Afiado como uma faca pequena. As crianças de Sssar usam-nos em colares. |
| `petala_carnivora` | Pétala Carnívora | Vermelha e pegajosa. Ainda tenta morder-te o dedo. |
| `nectar` | Néctar | Doce e dourado. As flores carnívoras usam-no para atrair comida. Tu és a comida. |
| `semente_carnivora` | Semente Carnívora | Planta-se na quinta. Cresce uma flor que come pragas. E corvos. E carteiros, se não tiveres cuidado. |
| `proboscide` | Probóscide | O ferrão do Mosquito Gigante. Oco como uma palhinha. Faz agulhas. |
| `asa_mosquito` | Asa de Mosquito | Transparente e com veias. Faz flechas mais leves. |
| `dente_crocodilo` | Dente de Crocodilo | Comprido e curvo. Faz pontas de lança. |
| `carne_crocodilo` | Carne de Crocodilo | Sabe a frango. Diz toda a gente. Não sabe a frango. |
| `pelo_macaco` | Pelo de Macaco | Castanho e macio. Faz forros quentes. Cheira a banana. |
| `sanguessuga` | Sanguessuga | Ainda mexe. A Selene usa-a na Poção de Regeneração. Não perguntes como. |
| `ingredientes_bruxa` | Ingredientes de Bruxa | Um saquinho com olhos de sapo, raízes e uma coisa que não sabes o que é. Alquimia. |
| `dente_mandibula` | Dente de Mandíbula | Do tamanho de um braço. A Mãe-Crocodilo não precisa mais dele. Tesouro. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_aco` | Espada de Aço | Lâmina de aço com punho de couro de crocodilo. Corta lianas e o resto. |
| `espada_grande_aco` | Espada Grande de Aço | Abre caminho na selva como se fosse uma porta. |
| `adaga_aco` | Adaga de Aço | Leve como uma pena de garça e duas vezes mais afiada. |
| `katana_aco` | Katana de Aço | O aço dobrado brilha como água parada. Corta vinhas de um só golpe. |
| `machado_aco` | Machado de Aço | Cabo de mangue, cabeça de aço. Árvore ou crocodilo, tanto faz. |
| `martelo_aco` | Martelo de Aço | Pesado de mais para o pântano. Leve de menos para o que te espera. |
| `lanca_aco` | Lança de Aço | A arma favorita dos Homens-Lagarto. Agora percebes porquê. |
| `foice_aco` | Foice de Aço | Ceifa juncos e mosquitos ao mesmo tempo. |
| `arco_aco` | Arco de Aço | Mangue e aço. Não empena com a humidade. |
| `besta_aco` | Besta de Aço | Os virotes de aço atravessam escamas. |
| `cajado_aco` | Cajado de Aço | Com um âmbar na ponta. A luz que sai é dourada. |
| `manoplas_aco` | Manoplas de Aço | Forradas a pele de crocodilo. Bater com elas é quase um abraço. Quase. |
| `bico_garca` | Bico da Garça | Lança feita do bico da Garça-Lança. Quando acerta, acerta onde dói. |
| `cajado_lodoso` | Cajado Lodoso | Pinga sempre. Os projéteis deixam poças de veneno. Não o guardes na mochila. |
| `garras_jade` | Garras de Jade | Manoplas da Pantera. Pelas costas, fazem o dobro. Não é bonito. É eficaz. |
| `machado_totemico` | Machado Totémico | Tem três caras esculpidas. Ficam mais contentes cada vez que vences alguém. |
| `pinca_maior` | Pinça Maior | Espada grande feita da pinça do Caranguejo-Violinista. Enquanto carregas, ficas mais duro. |
| `arco_cascata` | Arco Cascata | As flechas saem molhadas. Os inimigos também ficam. |
| `martelo_bugio` | Martelo Bugio | O ataque carregado atordoa sempre. Cheira a macaco. Sempre também. |
| `foice_espinhos` | Foice de Espinhos | A lâmina é um espinho enorme da Dríade. Faz sangrar. |
| `lingua_serpente` | Língua de Serpente | Lança de ponta dupla, como a língua da Serpente do Lodo. Cada estocada acerta duas vezes. |
| `arco_hidra` | Arco da Hidra | Três cabeças, três flechas. Dispara as três de uma vez. |
| `lanca_tribal_aco` | Lança Tribal de Aço | Lança dos renegados, com penas vermelhas. Mais forte quando lutas na água. |
| `lanca_ssark` | Lança de Ssark | Era do pai do Ssark. Agora é de quem defendeu os filhos dele. |
| `arco_tribal_aco` | Arco Tribal de Aço | O arco do Rakk. O Kesh nunca o pôde usar. Acerta mais vezes onde dói. |
| `katana_garra_sol` | Katana Garra-do-Sol | Arma secreta do Santuário do Jaguar. O ataque carregado solta uma onda de Luz. Os mortos-vivos detestam. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `crocodilo_cabeca` | Elmo de Crocodilo | Um elmo de aço forrado com pele de crocodilo. Parece que tens a cabeça dentro de uma boca. |
| `crocodilo_corpo` | Couraça de Crocodilo | Escamas por cima, aço por baixo. A água escorre sem entrar. |
| `crocodilo_maos` | Luvas de Crocodilo | Agarram tudo, mesmo molhadas. |
| `crocodilo_pes` | Botas de Crocodilo | Para andar no lodo sem o lodo andar dentro de ti. |
| `crocodilo_capa` | Capa de Liana | Tecida com fibra de liana. Leve, fresca e cheia de folhas. Ninguém te vê no mato. |
| `anel_serpente` | Anel da Serpente | Uma serpente de pedra que morde a própria cauda. Os teus golpes ficam mais rápidos. |
| `escama_primeiro_rei` | Escama do Primeiro Rei | Do fundo da Lagoa Sagrada. O rei dos Ssar escondeu-a lá. Quem a usa não teme veneno. |
| `bolsa_couro_real` | Bolsa de Couro Real | Feita com a pele da Mãe-Crocodilo. Cabe tudo. Mais dez coisas. |
| `chapeu_bruxa` | Chapéu de Bruxa | Bicudo, torto e com uma mosca a voar à volta. Cosmético. A mosca não sai. |
| `coroa_casca` | Coroa de Casca | A coroa do Rei Macaco Bobo: cascas de banana secas. Cosmético. Cheira ainda. |
| `pena_arco_iris` | Pena Arco-Íris | Um chapéu com a pena do pássaro gigante. Brilha com todas as cores. Cosmético. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_aco` | Picareta de Aço | Parte ferro negro, âmbar e esmeraldas. |
| `machado_lenhador_aco` | Machado de Lenhador de Aço | Corta mangue como se fosse manteiga. Manteiga molhada. |
| `cana_mangue` | Cana de Mangue | Estava no alçapão da cabana do pescador. Flexível e forte. O peixe luta menos. |
| `bussola_explorador` | Bússola de Explorador | Era da Vera Liana. A agulha treme quando há um segredo a menos de 20 metros. |
| `ocarina` | Ocarina | Presente do Coro dos Sapos. Toca-a ao pé da água e os peixes raros vêm ouvir. |
| `barco_alugado` | Barco Alugado | Do Velho Remo. 50 moedas por dia. Devolve-o com o fundo para baixo. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `pocao_vida_m` | Poção de Vida M | Vermelha e com musgo a boiar. Cura metade. |
| `pocao_purificadora` | Poção Purificadora | Cheira a lírio. A água venenosa deixa de te fazer mal. |
| `pocao_escamas` | Poção de Escamas | Receita da Xamã Ilssa. Sabe mal. Nascem-te escamas por um bocadinho. Saram. |
| `pocao_regeneracao` | Poção de Regeneração | Não perguntes o que tem dentro. Cura devagar e sem parar. |
| `pocao_surpresa` | Poção Surpresa | Do Doutor Girino. Pode dar força. Pode dar soluços. Pode transformar-te em sapo. Para a ciência! |
| `pocao_arco_iris` | Poção Arco-Íris | Todas as cores, todos os bónus pequenos. Catorze explosões para a inventar. |
| `bomba_polen` | Bomba de Pólen | Pétalas carnívoras numa bolsa. Rebenta numa nuvem dourada que cega e abranda. |
| `agua_coco` | Água de Coco | Fresca, doce, direta do coco. O calor do pântano deixa de te cansar. |
| `cafe_forte` | Café Forte | Receita do Lucien. Preto como a noite. Atacas mais depressa. Dormes mais devagar. |
| `chocolate_quente` | Chocolate Quente | Receita da Hana. Aquece por dentro e cura um bocadinho. Sabe a domingo. |
| `banana_frita` | Banana Frita | Crocante por fora, mole por dentro. A Estamina volta mais depressa. |
| `caril_selva` | Caril da Selva | Receita da Zith. Se não chorares, não está pronto. Dá força. |
| `espetada_crocodilo` | Espetada de Crocodilo | Receita do Kesh. Assada na fogueira. Não sabe a frango. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `bagre_lodo` | Bagre do Lodo | Bigodes compridos e cara de quem acabou de acordar. Só sai à noite. |
| `enguia_lama` | Enguia de Lama | Escorrega das mãos e da cana. E do prato, se não tiveres cuidado. |
| `piranha` | Piranha | Pequena e cheia de dentes. Não metas o dedo. Nem a cana toda. |
| `pirarucu` | Pirarucu | Um dos maiores peixes de rio. Só na maré alta. Pesa como uma criança. |
| `peixe_arco_iris` | Peixe-Arco-Íris | Só aparece com sol, ao meio-dia, quando há arco-íris. As escamas têm todas as cores. |
| `velho_bigodes` | O Velho Bigodes | **Lendário.** Um bagre do tamanho de um barco. Maré alta, noite, chuva. A Rã-Rã nunca o apanhou. |
| `semente_cacau` | Sementes de Cacau | Plantam-se e crescem numa árvore pequena que dá cacau para sempre. |
| `semente_cafe` | Sementes de Café | Arbusto teimoso. Dá café sem parar no Verão. |
| `muda_bananeira` | Muda de Bananeira | Uma bananeira bebé. Daqui a catorze dias, bananas. |
| `semente_pimenta` | Sementes de Pimenta | Pequenas e picantes. Até as sementes. |
| `bolbo_lirio` | Bolbo de Lírio | Planta-o junto ao rio da quinta. Precisa de água para florir. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `ordem_expulsao` | Ordem de Expulsão | Papel com o selo da Guilda. Manda expulsar os Homens-Lagarto do andar 24. Pesa mais do que parece. |
| `insignia_vermelha` | Insígnia Vermelha | A insígnia do Krass, chefe dos renegados. A prova de quem atacou os exploradores. |
| `saco_roubos` | Saco de Coisas Roubadas | Bússolas e cantis com o símbolo da Guilda. Roubados aos exploradores atacados no andar 23. |
| `idolo_jade` | Ídolo de Jade | Uma serpente de jade com olhos de esmeralda. O Barão quer vendê-lo. O Fausto quer lê-lo. |
| `diario_pescador` | Diário do Pescador | Um peixe por dia, durante anos. O último dia diz só: "Hoje não." |
| `ovo_passaro_gigante` | Ovo de Pássaro Gigante | Do tamanho de um barril. Quente. Algures há um ninho à espera dele. |
| `canoa_sssar` | Canoa Sssar | Móvel. Uma canoa pintada de azul, prémio da corrida na Festa na Aldeia. Não flutua na sala. |
| `totem_pequeno` | Totem Pequeno | Móvel. Três caras de madeira. Os Ssar dizem que protege a casa. Olha para ti à noite. |
| `trofeu_coroa_serpente` | Coroa de Pedra da Serpente | Troféu da Serpente do Lodo. Pedra antiga, com desenhos que ninguém sabe ler. |
| `trofeu_dentes_hidra` | Três Dentes da Hidra | Troféu da Hidra do Pântano. Um verde, um roxo, um amarelo. Não voltam a crescer. Espero. |
