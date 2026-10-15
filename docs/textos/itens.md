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
| `leque_barao` | Leque do Barão | Folha de palmeira com cabo de ouro. Abana sozinho quando está calor. O Barão tem dez. |
| `ovo_sapinho_dourado` | Ovo de Sapinho Dourado | Cosmético para o Sapinho: fica dourado. Ele acha que é rei. Não é. Mas deixa-o pensar. |
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
| `moscas_fritas` | Moscas Fritas | Comida de sapo. Estaladiça. Os sapos dizem que é como batata frita. Os sapos mentem. |
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

---

## Região 4 — Deserto

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `minerio_prata` | Minério de Prata | Pedra branca com veios que brilham. Os mortos-vivos não gostam dela. |
| `lingote_prata` | Lingote de Prata | Prata fundida. Brilha mesmo no escuro. As múmias desviam os olhos. |
| `madeira_acacia` | Madeira de Acácia | Dura, seca e cheia de nós. Cresce onde nada cresce. |
| `couro_chacal` | Couro de Chacal | Leve e fresco. Bom para quem anda ao sol. |
| `ligadura_antiga` | Ligadura Antiga | Linho de múmia, velho de séculos. Forte como corda. Cheira a pó e a resina. |
| `vidro_solar` | Vidro Solar | Areia que um raio derreteu. Guarda o calor e a luz lá dentro. |
| `sal` | Sal | Das salinas do 33. Para a sopa, para o peixe e para as sanguessugas. |
| `cacto_agua` | Cacto-Água | Corta-se e bebe-se. Sabe a pepino triste. Salva vidas. |
| `flor_deserto` | Flor do Deserto | Só abre ao amanhecer. Cheira a mel e a chuva que nunca vem. |
| `tamaras` | Tâmaras | Doces e pegajosas. Os camelos venderiam a alma por uma. |
| `acafrao` | Açafrão | A especiaria mais cara do deserto. Três fios dão cor a uma panela inteira. |
| `perola_deserto` | Pérola do Deserto | Nasce dentro do Verme da Areia. Amarela e quente. Rara. |
| `perola_deserto_grande` | Pérola do Deserto Grande | Do Verme Colosso. Do tamanho de uma laranja. Tesouro. |
| `carapaca_escorpiao` | Carapaça de Escorpião | Dura e leve. Armaduras de quem não quer pesar. |
| `ferrao_escorpiao` | Ferrão de Escorpião | Ainda pinga. Virotes envenenados e poções. |
| `po_mumia` | Pó de Múmia | Os alquimistas antigos juravam que curava tudo. Não cura. Mas faz boas maldições. |
| `escama_verme` | Escama de Verme | Lisa e cor de areia. Escorrega até a água. |
| `dente_verme` | Dente de Verme | Um dente em forma de anel. Os vermes têm muitos. Agora têm menos um. |
| `osso` | Osso | Um osso. De quem, não perguntes. |
| `cranio` | Crânio | Os esqueletos remontam-se sem ele. Ou melhor: não se remontam. |
| `dente_chacal` | Dente de Chacal | Pequeno e afiado. Os nómadas fazem colares contra o azar. |
| `areia_magica` | Areia Mágica | Areia que se mexe sozinha na palma da mão. Para cajados e ampulhetas. |
| `carapaca_escaravelho` | Carapaça de Escaravelho | Brilha como metal. Os de Zahra fazem botões com ela. |
| `po_fogo` | Pó de Fogo | Arde ao contacto com o ar. Guarda bem fechado. |
| `osso_gigante` | Osso Gigante | Um osso de dragão do tamanho de uma viga. Constrói-se com ele. |
| `ouro_antigo` | Ouro Antigo | Moedas e pedaços de ouro da pirâmide. Vende-se bem. Não se gasta: os lojistas não as aceitam como moeda. |
| `escama_colosso` | Escama de Colosso | Do tamanho de um escudo. O Brom faz escudos com ela. Diz "Hmpf". |
| `amuleto_escaravelho_drop` | Amuleto Escaravelho | Pequeno escaravelho de pedra azul. Vende-se aos colecionadores de Zahra. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_prata` | Espada de Prata | Brilha ao sol e à lua. Corta o vivo e o morto. |
| `espada_grande_prata` | Espada Grande de Prata | Uma barra de luz com fio. Os esqueletos fogem dela. Os que podem. |
| `adaga_prata` | Adaga de Prata | Pequena, fria e certeira. A preferida dos bandidos com bom gosto. |
| `katana_prata` | Katana de Prata | Curva como uma duna e afiada como o vento do 36. |
| `machado_prata` | Machado de Prata | Parte crânios de esqueleto com uma pancada. Às vezes duas. |
| `martelo_prata` | Martelo de Prata | O pesadelo das múmias e dos golens de arenito. |
| `lanca_prata` | Lança de Prata | Longa e brilhante. Os chacais não chegam às tuas costas. |
| `foice_prata` | Foice de Prata | Ceifa em arco, como a lua. Os mortos-vivos detestam-na. |
| `arco_prata` | Arco de Prata | Acácia e prata. Atira longe por cima das dunas. |
| `besta_prata` | Besta de Prata | Pesada. Os virotes de prata atravessam ligaduras. |
| `cajado_prata` | Cajado de Prata | Com vidro solar na ponta. Aquece nas mãos. |
| `manoplas_prata` | Manoplas de Prata | Para socos que se ouvem do outro lado da duna. |
| `espinho_duna` | Espinho da Duna | Adaga feita de um espinho do Lagarto-Duna. Faz sangrar. |
| `cajado_miragem` | Cajado Miragem | Às vezes cria uma cópia tua que distrai os inimigos. Não fala. Ainda bem. |
| `arco_abutre` | Arco do Abutre | Faz mais dano a quem já está quase a cair. Como um abutre. |
| `martelo_arenito` | Martelo de Arenito | Os golpes levantam areia que cega. Pesa como um templo. |
| `cimitarra_vento` | Cimitarra do Vento | Do Djinn da tempestade. Cada golpe lança uma lâmina de vento. |
| `lanca_cavaleiro_ossos` | Lança do Cavaleiro de Ossos | O ataque carregado faz uma carga de seis metros. Sem camelo. |
| `garras_esfinge` | Garras da Esfinge | Cada crítico deixa-te mais rápido. A Esfinge pensava depressa. |
| `foice_ouro_sacerdote` | Foice de Ouro do Sacerdote | Rouba um bocadinho de vida a cada golpe. Pesa almas. |
| `ferrao_imperial` | Ferrão Imperial | Besta feita da cauda do Escorpião Imperador. Os virotes envenenam. |
| `khopesh_farao` | Khopesh do Faraó | A espada curva do Faraó Eterno. Chama escaravelhos para lutar contigo. |
| `cimitarra_sultao` | Cimitarra do Sultão | Uma das duas do Kasim. Combos de quatro golpes. A outra ficou com ele, na jaula. |
| `cimitarra_velha_prata` | Cimitarra Velha de Prata | De um esqueleto guerreiro. Velha e com mossas. Faz mais dano a mortos-vivos. |
| `espada_grande_osso_dragao` | Espada Grande Osso-de-Dragão | Arma secreta do Túmulo do Dragão Antigo. Feita do osso de um dragão que nunca voou. Odeia bosses. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `deserto_cabeca` | Capuz do Deserto | Couro de chacal e um véu de ligadura para a areia não entrar no nariz. |
| `deserto_corpo` | Colete do Deserto | Leve, fresco e com placas de prata. Para quem luta ao sol. |
| `deserto_maos` | Luvas do Deserto | Agarram a cimitarra mesmo com as mãos a suar. |
| `deserto_pes` | Botas do Deserto | Não se enterram na areia. Quase nunca. |
| `deserto_capa` | Capa de Ligaduras | Faixas de linho antigo. Dizem que protege de maldições. Não protege. Mas é bonita. |
| `turbante_sultao` | Turbante do Sultão | O turbante dourado do Kasim. O sol do deserto não te toca. Ainda cheira a perfume caro. |
| `lenco_deserto` | Lenço do Deserto | Um lenço comprido para a cabeça. O sol deixa de fazer mal. Os bandidos usam-nos. Tu também podes. |
| `olho_solar` | Olho Solar | Um olho de ouro com um rubi. Durante o dia, bates mais. |
| `amuleto_escaravelho` | Amuleto do Escaravelho | Da avó do Guarda Sami. As maldições não te pegam. |
| `bussola_darian` | Bússola de Darian | Do pai da Lyra. Tem um "D" gravado. Aponta sempre para a Zona Segura mais próxima. Para casa. |
| `vestes_danca` | Vestes de Dança | Cosmético. Lenços de todas as cores que voam quando rodas. A Layla diz que ficas bem. A Layla diz isso a toda a gente. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_prata` | Picareta de Prata | Parte prata e vidro solar. |
| `machado_lenhador_prata` | Machado de Lenhador de Prata | Corta acácia, que é a madeira mais teimosa do deserto. |
| `pa` | Pá | Do Beto. Para escavar portas soterradas e pontos de tesouro. |
| `pa_prata` | Pá de Prata | Da Professora Íris. Escava o dobro e abre as portas de prata. |
| `cantil_infinito` | Cantil Infinito | Era do pai do Yusuf. Nunca seca. O sol do deserto deixa de te fazer mal. |
| `mapa_tesouro` | Mapa do Tesouro | Um X num desenho mal feito. Leva uma pá. |
| `mapa_estrelas` | Mapa das Estrelas | Da Anciã Sahra. As estrelas pregadas do céu de Zahra mostram onde estão os baús de ouro. |
| `sela_corrida` | Sela de Corrida | Do Tarik. A montada corre mais 15%. Ele chorou ao dar-ta. |
| `lanterna_deserto` | Lanterna do Deserto | Do Hakim. Luz de 6 metros. O vento não a apaga. |
| `laco` | Laço | Do Mestre Rahim. Para apanhar Lagartos da Areia. Não para mais nada. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `sumo_cacto` | Sumo de Cacto | Verde e fresco. Durante cinco minutos, o sol esquece-se de ti. |
| `tamaras_mel` | Tâmaras com Mel | Doce em cima de doce. Dá energia para correr dunas acima. |
| `cuscuz_oasis` | Cuscuz do Oásis | Receita de Zahra, com açafrão. Cura devagar e enche a barriga. |
| `pao_acafrao` | Pão de Açafrão | Amarelo e perfumado. Os nómadas dizem que traz sorte. Traz: os drops raros caem mais. |
| `perfume` | Perfume | Flor do Deserto num frasco. Presente que quase toda a gente adora. |
| `oleo_lampada` | Óleo de Lâmpada | Para as lâmpadas do Hakim. Não se bebe. Alguém perguntou. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `tilapia_azul` | Tilápia Azul | O peixe da lagoa de Zahra. Azul como a água. Saboroso como nada no deserto. |
| `peixe_areia` | Peixe-Areia | Nada na areia como os outros na água. Pesca-se nas dunas com isco especial. |
| `siluro_salgado` | Siluro Salgado | Vive no lago das salinas. Já vem temperado. |
| `peixe_escaravelho` | Peixe-Escaravelho | Do Poço Real da pirâmide. Tem uma carapaça como um escaravelho. Estranho e raro. |
| `peixe_oasis` | Peixe do Oásis Verdadeiro | Só no oásis que não é miragem. Brilha. |
| `farao_aguas` | O Faraó das Águas | **Lendário.** Um peixe dourado com uma "máscara" nas escamas. Lua cheia, meia-noite, lagoa de Zahra. |
| `muda_tamareira` | Muda de Tamareira | Daqui a 21 dias, tâmaras para sempre. Paciência de deserto. |
| `semente_cacto` | Sementes de Cacto-Água | Plantam-se e esquecem-se. Não precisam de água. Dão água. |
| `semente_melao` | Sementes de Melão do Deserto | Da Mina. Rega pouco. Os melões do deserto não gostam de mimos. |
| `bolbo_acafrao` | Bolbo de Açafrão | Flor roxa, fios vermelhos, preço de ouro. |
| `semente_flor_deserto` | Sementes de Flor do Deserto | Flores que abrem ao amanhecer. Na quinta, também. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `caderno_arroz` | Caderno de Papel de Arroz | Da Professora Íris. Para copiar os hieróglifos com carvão. "Até as manchas." |
| `copias_hieroglifos` | Cópias dos Hieróglifos | Seis folhas cheias de símbolos azuis em carvão. Leva-as ao Velho Fausto. |
| `lampada_velha` | Lâmpada Velha | Uma lâmpada de óleo amolgada. Dizem que tem um Djinn preso. Não a esfregues. |
| `lenco_samira` | Lenço de Samira | Um lenço com uma estrela bordada no canto. Para o Rook. |
| `coroa_cidade_enterrada` | Coroa da Cidade Enterrada | Decoração. A coroa do rei de Qasr-al-Ma. A cidade era da água. A coroa ainda tem uma gota. |
| `escudo_carapaca` | Escudo de Carapaça | Troféu e decoração. Uma carapaça gigante de escorpião, pendurada na parede. |
| `trofeu_carapaca_imperial` | Carapaça Imperial | Troféu do Escorpião Imperador. A marca azul já não brilha. |
| `trofeu_mascara_farao` | Máscara do Faraó | Troféu do Faraó Eterno. Partida ao meio, colada com resina. Por trás, não há cara. |
| `tapete_zahra` | Tapete de Zahra | Móvel. Dura cem anos. Diz o Faisal. |

---

## Região 5 — Gelo

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `fragmento_gelo_eterno` | Fragmento de Gelo Eterno | Gelo azul que nunca derrete, nem ao fogo. Frio ao toque, sempre. |
| `barra_gelo_eterno` | Barra de Gelo Eterno | Três fragmentos fundidos num molde quente. Mais duro do que a prata. |
| `pinheiro_nevado` | Pinheiro Nevado | Madeira do norte, cheia de resina. Arde bem e cheira melhor. |
| `pele_urso_polar` | Pele de Urso Polar | Grossa, branca e quentíssima. Faz casacos que aguentam tudo. |
| `la_mamute` | Lã de Mamute | Lã comprida e áspera. Fia-se em fio que não parte. |
| `la_ancestral` | Lã Ancestral | Do Mamute Ancião, dada de boa vontade. Mais macia do que qualquer outra. |
| `lagrima_aurora` | Lágrima de Aurora | Cristal que só aparece com a aurora. Muda de cor como ela. |
| `safira` | Safira | Gema azul das grutas de gelo. Guarda o frio lá dentro. |
| `flor_neve` | Flor-de-Neve | Flor branca que só abre no frio. Faz Poção Quente e alegra quem a recebe. |
| `musgo_artico` | Musgo Ártico | Verde-acinzentado e fofo. Cresce à sombra e cura feridas de frio. |
| `bagas_inverno` | Bagas de Inverno | Vermelhas e azedas. Fazem chá. E os mamutes adoram-nas. |
| `marfim` | Marfim | De presa de mamute ou de morsa. Branco e liso. Para joias e decoração. |
| `marfim_ancestral` | Marfim Ancestral | Do Mamute Ancião. Pesado de mais para o que custou. |
| `pena_gelida` | Pena Gélida | Pena de harpia, com gelo nas pontas. Flechas que congelam e chapéus que não. |
| `brasa_eterna` | Brasa Eterna | Do iglu do 41. Arde e não gasta. O Fausto ainda não acredita. |
| `pele_lobo_gelo` | Pele de Lobo de Gelo | Branca com pontas azuis. Bonita e quente. |
| `presa_gelada` | Presa Gelada | Dente de lobo de gelo. Faz pontas de flecha que gelam. |
| `garra_urso` | Garra de Urso | Do tamanho da tua mão. Faz manoplas assustadoras. |
| `nucleo_gelado` | Núcleo Gelado | O centro de um golem de gelo. Ainda bate, como um coração. |
| `essencia_neve` | Essência de Neve | Um floco que não derrete, num frasco. Para cajados e poções frias. |
| `garra_harpia` | Garra de Harpia | Curva e fina como um anzol. |
| `pele_velha` | Pele Velha | Dos casacos dos caçadores congelados. Ainda serve. Lava-a primeiro. |
| `diario_cacador` | Diário de Caçador | O diário de um caçador do 46. Tem um nome na capa. Enterra-o ao pé da torre (R5_15). |
| `pena_pinguim` | Pena de Pinguim | Preta e branca, impermeável. Para capas que não molham. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_gelo_eterno` | Espada de Gelo Eterno | Azul e transparente. Vês o inimigo através da lâmina. |
| `espada_grande_gelo_eterno` | Espada Grande de Gelo Eterno | Pesada e fria. Deixa uma neblina no ar a cada golpe. |
| `adaga_gelo_eterno` | Adaga de Gelo Eterno | Pequena como um caramelo de gelo. Mais afiada do que parece. |
| `katana_gelo_eterno` | Katana de Gelo Eterno | Curva como uma estalactite. Corta em silêncio, como a neve a cair. |
| `machado_gelo_eterno` | Machado de Gelo Eterno | Corta pinheiros e ursos. Prefere pinheiros. |
| `martelo_gelo_eterno` | Martelo de Gelo Eterno | Cada pancada deixa uma estrela de gelo no chão. |
| `lanca_gelo_eterno` | Lança de Gelo Eterno | Comprida e fina como um pingente. |
| `foice_gelo_eterno` | Foice de Gelo Eterno | Ceifa neve e inimigos. Fica bonita nas fotografias. Não há fotografias. |
| `arco_gelo_eterno` | Arco de Gelo Eterno | Não empena com o frio. As flechas assobiam. |
| `besta_gelo_eterno` | Besta de Gelo Eterno | Pesada. Os virotes deixam um rasto de geada. |
| `cajado_gelo_eterno` | Cajado de Gelo Eterno | Com uma safira na ponta. Brilha azul no escuro. |
| `manoplas_gelo_eterno` | Manoplas de Gelo Eterno | Socos frios. Muito frios. Os inimigos ficam a tremer. Literalmente. |
| `presas_morsa` | Presas de Morsa | Adaga feita da presa da Morsa Gigante. Faz mais dano a quem já tem frio. |
| `arco_chifre` | Arco de Chifre | Do Alce Fantasma. As flechas atravessam um inimigo e continuam. |
| `lanca_tentaculo` | Lança Tentáculo | Do Kraken do Gelo. As estocadas puxam o alvo para ti. Nojenta e útil. |
| `cajado_gelido` | Cajado Gélido | Do Coração de Cristal Azul. Os feitiços às vezes dão Frio. |
| `foice_wendigo` | Foice do Wendigo | Feita do crânio de alce do Wendigo. Às vezes mete medo a quem leva com ela. |
| `martelo_glaciar` | Martelo Glaciar | Da Tartaruga-Glaciar. O chão gela e os inimigos escorregam. |
| `katana_aurora` | Katana Aurora | Da Raposa Aurora. Os críticos rebentam em luz colorida. |
| `lamina_cavaleiro_gelido` | Lâmina do Cavaleiro Gélido | Espada grande do Cavaleiro de Gelo. Com ela, o frio não te toca. |
| `punhos_yeti` | Punhos do Yeti | Manoplas de pelo branco com gelo nos nós dos dedos. Os socos congelam. |
| `sopro_gelido` | Sopro Gélido | Katana do Dragão de Gelo. O corte congela tudo numa linha. |
| `arco_gelo_eterno_inga` | Arco da Mãe da Inga | Arco de Gelo Eterno (Épico). Não parte. Como ela. |
| `besta_pesada_gelo_eterno` | Besta Pesada de Gelo Eterno | Épica. Os virotes atravessam dois inimigos. A Freya disse "Hm. Serve." |
| `lanca_inverno_eterno` | Lança do Inverno Eterno | Arma secreta da Cripta do Rei do Inverno. Congela com duas acumulações de Frio em vez de três. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `urso_cabeca` | Gorro de Urso | Com orelhas. Sim, orelhas. É quente. Não discutas. |
| `urso_corpo` | Casaco de Urso Polar | Pele de urso por fora, gelo eterno por dentro. Ninguém tem frio dentro dele. |
| `urso_maos` | Luvas de Urso | Grandes como patas. Dá para pegar na espada. Mais ou menos. |
| `urso_pes` | Botas de Urso | Peludas e pesadas. A neve funda já não te come os pés. |
| `urso_capa` | Capa de Lã de Mamute | Comprida até aos tornozelos. Os mamutes não ficaram contentes. |
| `casaco_la` | Casaco de Lã | Da Velha Astrid. A temperatura desce metade. "Não tires até à primavera." |
| `capa_presa_branca` | Capa de Presa-Branca | Pele do grande lobo branco. A temperatura desce metade. As cicatrizes azuis ainda brilham. |
| `botas_pico` | Botas de Pico | Com picos de ferro na sola. Não escorregas no gelo. Fazem barulho no chão de madeira. |
| `raquetes_neve` | Raquetes de Neve | Parecem raquetes de ténis nos pés. Andas na neve funda sem afundar. |
| `amuleto_cacador` | Amuleto do Caçador | Da Inga. Bates mais em quem não te viu. |
| `porta_chaves_gato` | Porta-chaves do Gato | Do Kai. Um gato de plástico com a tinta gasta. Velocidade +5%. Com o Kai ao lado, críticos +5% para os dois. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_gelo_eterno` | Picareta de Gelo Eterno | Parte gelo eterno e lágrimas de aurora. |
| `machado_lenhador_gelo_eterno` | Machado de Lenhador de Gelo Eterno | Corta pinheiros nevados de um golpe. A neve cai-te na cabeça na mesma. |
| `arpao` | Arpão | Do avô do Ulf. Para o peixe mais teimoso do mar. E do lago. |
| `lata` | Lata | Do Tobias. Para guardar brasas. E outras coisas que não se agarram com a mão. |
| `bilhete_treno` | Bilhete de Trenó | Do Erik. Viagem rápida entre as Zonas Seguras da região. Os cães não travam. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `pocao_quente` | Poção Quente | Vermelha e a fumegar. +40 de temperatura e o Frio não te pega. |
| `pedra_quente` | Pedra Quente | Uma pedra lisa aquecida com uma Brasa Eterna. Cinco minutos sem frio. |
| `cha_quente` | Chá Quente | Receita da Dona Marta. Bagas de inverno e água. Aquece as mãos e o resto. |
| `sopa_couve_norte` | Sopa de Couve do Norte | Receita de Pinhal-do-Norte. Grossa, verde, deliciosa. Dá vida. |
| `bacalhau_forno` | Bacalhau no Forno | Receita do Ulf. Peixe, batata e azeite. O melhor jantar do norte. |
| `bolo_bagas` | Bolo de Bagas | Receita da Velha Astrid. Rosa por dentro. Dá energia mágica. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `caranguejo_neve` | Caranguejo-Neve | Branco como a costa onde vive. Belisca devagar: está com frio. |
| `bacalhau_artico` | Bacalhau Ártico | Grande e prateado. Pesca-se nos buracos do gelo. O Ulf adora. |
| `salmao_gelo` | Salmão do Gelo | Rosa por dentro, azul por fora. Sobe o rio no Outono. |
| `peixe_lanterna_gelado` | Peixe-Lanterna Gelado | Tem uma luz azul na testa. Vive nas poças escuras das grutas de gelo. |
| `truta_aurora` | Truta Aurora | As escamas mudam de cor como o céu. Só com aurora verde. |
| `narval_real` | Narval Real | **Lendário.** Um narval com um chifre de cristal. Só com o Arpão, de madrugada, num nevão. |
| `semente_bagas_inverno` | Sementes de Bagas de Inverno | Arbusto que dá bagas no frio. Os mamutes agradecem. |
| `semente_couve_norte` | Sementes de Couve do Norte | Da Astrid. Couve grande como uma cabeça. |
| `semente_flor_neve` | Sementes de Flor-de-Neve | Só florescem no Inverno. Valem a espera. |
| `esporos_musgo_artico` | Esporos de Musgo Ártico | Plantam-se à sombra. Crescem devagar e sem fazer barulho. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `diario_equipa_gorvan` | Diário da Equipa de Gorvan | Capa de couro, páginas onduladas pela neve. Mapas, listas de comida, piadas na margem. Leva-o ao Gorvan. |
| `pena_amarela` | Pena Amarela | De uma flecha. Estava no colar do Yeti. Era de alguém que se ria alto. |
| `boneca_pano` | Boneca de Pano | Do monte de brinquedos do Yeti. Tem um nome bordado, ilegível. A Mia vai gostar. |
| `ovo_pinguim` | Ovo de Pinguim | Quente. Tem de continuar quente. Passa pelas fogueiras. |
| `cria_presa_branca` | Cria de Presa-Branca | Um lobinho branco que tem frio. Estranho para um lobo de gelo. Leva-o ao Zed. |
| `coroa_gelo` | Coroa de Gelo | Do trono vazio do 49. Põe-na e vês a corte a dançar. Um minuto. |
| `trofeu_colar_yeti` | Colar do Yeti | Troféu. Um relógio parado às 7:42, uma chave, um botão, uma medalha… e um elástico de cabelo muito velho. |
| `trofeu_escama_dragao_gelo` | Escama de Dragão de Gelo | Troféu e escudo de parede. Transparente. Vê-se a parede através dela. |
| `escultura_gelo` | Escultura de Gelo | Móvel do concurso do Solstício. Não derrete. É gelo eterno. Ou é magia. |

---

## Região 6 — Oceano

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `coral_abissal` | Coral Abissal | Coral escuro dos recifes fundos. Duro como pedra e leve como osso. |
| `barra_coral_abissal` | Barra de Coral Abissal | Coral polido com sal na forja. Brilha como o fundo do mar ao sol. |
| `madeira_naufragio` | Madeira de Naufrágio | Madeira de barcos afundados, salgada e dura. Volta a ser barco com gosto. |
| `pele_tubarao` | Pele de Tubarão | Áspera como uma lixa. Faz armaduras que escorregam na água. |
| `fio_alga_prata` | Fio de Alga-Prata | Alga brilhante que se fia como seda. Não apodrece. |
| `perola` | Pérola | Branca e redonda. Nasce dentro das ostras. Abre-se com a Faca de Mergulho. |
| `perola_negra` | Pérola Negra | Rara e escura como o fundo da fossa. Joias de luxo e presentes que fazem chorar. |
| `sal_marinho` | Sal Marinho | Das rochas da maré. Para a cozinha e para polir coral. |
| `alga_doce` | Alga Doce | Verde e doce. Os cavalos-marinhos adoram. Tu também, se tiveres fome. |
| `anemona` | Anémona | Flor do mar que pica. Faz Poção de Respirar. |
| `concha_rara` | Concha Rara | Espiralada e cheia de cores. Para colecionar, decorar e oferecer. |
| `gel_eletrico` | Gel Elétrico | Da Alforreca Elétrica. Ainda dá choque. O Gizmo usa-o como bateria. |
| `moeda_antiga` | Moeda Antiga | Moeda pirata de ouro velho. Vale 50 ouro. Ou mais, se a colecionares. |
| `carapaca_caranguejo` | Carapaça de Caranguejo | Dura e vermelha. Escudos pequenos e armaduras de praia. |
| `carne_caranguejo` | Carne de Caranguejo | Doce e branca. Fica melhor com arroz. |
| `pinca` | Pinça | De caranguejo gigante. Serve de tenaz. Ou de arma, se fores criativ{o/a}. |
| `escama_sereia` | Escama de Sereia | Furta-cores. As sereias de Coralina não gostam de a ver à venda. |
| `lagrima_sereia` | Lágrima de Sereia | Uma gota dura como vidro. Diz-se que cura a tristeza. Não cura. Mas é bonita. |
| `dente_tubarao` | Dente de Tubarão | Triangular e serrilhado. Os piratas faziam colares com eles. |
| `tentaculo` | Tentáculo | Ainda se mexe. Cozinha-se ou faz-se em cordas. |
| `tinta_polvo` | Tinta de Polvo | Preta como a noite. Escreve-se com ela e faz-se Bomba de Tinta. |
| `tentaculo_fino` | Tentáculo Fino | De alforreca. Transparente e com choque. |
| `lanterna_abissal` | Lanterna Abissal | A luz do Peixe-Lanterna, num frasco. Ilumina 6 metros no escuro do fundo. |
| `dente_abissal` | Dente Abissal | Comprido e fino como uma agulha. |
| `escama_serpente_marinha` | Escama de Serpente Marinha | Azul-escura, grande como um prato. |
| `barbatana` | Barbatana | De serpente marinha. Faz barbatanas de nadar. A sério. |
| `polvora` | Pólvora | Dos piratas. Para canhões e bombas. Mantém-na seca. No mar. Boa sorte. |
| `pinca_ouro` | Pinça de Ouro | Do Caranguejo Rei. Ouro maciço. O Barão paga 6 000. Ou fica na tua parede. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_coral_abissal` | Espada de Coral Abissal | Lâmina escura com reflexos verdes. Não enferruja na água. |
| `espada_grande_coral_abissal` | Espada Grande de Coral Abissal | Pesada como uma âncora. Mais ou menos com a mesma utilidade contra tubarões. |
| `adaga_coral_abissal` | Adaga de Coral Abissal | Afiada como um dente de tubarão. Aliás, é parecida. |
| `katana_coral_abissal` | Katana de Coral Abissal | Curva como uma onda. Corta a água sem fazer espuma. |
| `machado_coral_abissal` | Machado de Coral Abissal | Para madeira de naufrágio e carapaças de caranguejo. |
| `martelo_coral_abissal` | Martelo de Coral Abissal | Parte carapaças, cascos e crânios de piratas. |
| `lanca_coral_abissal` | Lança de Coral Abissal | Comprida e fina, como um arpão. A arma preferida dos tritões. |
| `foice_coral_abissal` | Foice de Coral Abissal | Ceifa algas e alforrecas. Cuidado com o choque. |
| `arco_coral_abissal` | Arco de Coral Abissal | Madeira de naufrágio e coral. Atira longe por cima das ondas. |
| `besta_coral_abissal` | Besta de Coral Abissal | Os virotes não perdem força na chuva. Nem no mar. Quase. |
| `cajado_coral_abissal` | Cajado de Coral Abissal | Com uma pérola na ponta. Brilha como a lua na água. |
| `manoplas_coral_abissal` | Manoplas de Coral Abissal | Socos que se ouvem debaixo de água. Os peixes fogem. |
| `martelo_casco_tartaruga` | Martelo Casco de Tartaruga | Da Tartaruga-Marinha Anciã. Com ele, aguentas mais. |
| `arco_gaivota` | Arco Gaivota | Da Gaivota Ladra. Flechas rápidas e pés leves. Não rouba. Ainda. |
| `ancora_imediato` | Âncora do Imediato | Martelo-âncora do Imediato Fantasma. O ataque carregado puxa os inimigos para ti. |
| `adaga_peixe_leao` | Adaga Peixe-Leão | Um espinho venenoso com cabo. Envenena às vezes. |
| `lanca_alga` | Lança de Alga | Do Dragão-Marinho Folhado. As estocadas deixam o alvo encharcado. |
| `manoplas_coral` | Manoplas de Coral | Do Golem de Coral. Cada golpe cura-te um bocadinho. O coral cresce. |
| `cajado_lanterna_abissal` | Cajado Lanterna Abissal | Do Tamboril. Ilumina 8 metros e bate mais no escuro. |
| `foice_mares` | Foice das Marés | Do Guardião das Marés. Os golpes empurram uma onda à frente. |
| `sabre_afogado` | Sabre do Afogado | O sabre do Capitão Esqueleto. Cura-te um bocadinho a cada golpe. Ainda cheira a rum. |
| `tridente_leviata` | Tridente do Leviatã | Feito de uma barbatana do Leviatã. As estocadas lançam ondas. Pesa mais do que devia. |
| `besta_arpao_almirante` | Besta Arpão do Almirante | Arma secreta do Cofre do Almirante. Os virotes puxam os inimigos e não perdem força debaixo de água. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `tubarao_cabeca` | Elmo de Tubarão | Tem a forma da cabeça de um tubarão. Os peixes pequenos fogem. |
| `tubarao_corpo` | Couraça de Tubarão | Pele de tubarão e coral. A água escorre. Os dentes também. |
| `tubarao_maos` | Luvas de Tubarão | Ásperas: nada escorrega das mãos. Nem a espada molhada. |
| `tubarao_pes` | Botas de Tubarão | Com barbatanas pequenas nos calcanhares. Nadas um bocadinho mais depressa. |
| `tubarao_capa` | Capa de Alga-Prata | Brilha à luz do mar. Seca depressa. |
| `mascara_mergulho` | Máscara de Mergulho | Da filha da Ama Kaia. Mais 50% de Ar. |
| `capacete_escafandro` | Capacete de Escafandro | Do Gizmo. Ar infinito e a pressão do fundo não te esmaga. Pesa como uma bigorna. |
| `colar_perolas` | Colar de Pérolas | Da Ourives Pérola. +15% de MP. Fica bem a toda a gente. |
| `chapeu_barba_lodo` | Chapéu de Barba-Lodo | Tricórnio com algas. Mais 5% de dano no mar. Ainda pinga. |
| `coroa_conchas` | Coroa de Conchas | Cosmético. Do Príncipe Maré. Tilinta quando corres. |
| `coroa_pinca` | Coroa de Pinça | Cosmético. A coroa do Caranguejo Rei. Pequena demais para a tua cabeça. Usa-se de lado. |
| `chapeu_pirata` | Chapéu de Pirata | Cosmético. Um tricórnio com uma caveira. Não te torna pirata. Só pareces. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_coral_abissal` | Picareta de Coral Abissal | Parte coral abissal e pérolas presas na rocha. |
| `machado_lenhador_coral_abissal` | Machado de Lenhador de Coral Abissal | Corta madeira de naufrágio, mesmo molhada. |
| `faca_mergulho` | Faca de Mergulho | Da Ama Kaia. Para abrir ostras. Não para lutar. A sério. |
| `barco` | O teu Barco | Reparado no estaleiro do Tomé. Tem o nome que lhe deste. Leva-te entre ilhas. |
| `carta_nautica` | Carta Náutica | Do Joaquim. O mapa do mar mostra as correntes. Segue as setas azuis. |
| `oculo_pirata` | Óculo de Pirata | Do Capitão Vasco. Vês mais longe no mar. |
| `bussola_amaldicoada` | Bússola Amaldiçoada | Do Barba-Lodo. Aponta para os tesouros enterrados da região. Às vezes treme sozinha. |
| `concha_mar` | Concha do Mar | Da Lirael. Toca-a e o mar escuta. Tem quatro canções. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `pocao_respirar` | Poção de Respirar | Sabe a mar. O Ar dura o triplo durante 5 minutos. |
| `sushi_recife` | Sushi do Recife | Peixe cru, arroz e alga doce. Mais Ar. Mais estilo. |
| `caldeirada_porto` | Caldeirada do Porto | Receita da Rosa. Peixe de três sítios. Dá resistência. |
| `arroz_marisco` | Arroz de Marisco | Receita de Coralina. Caranguejo, arroz e tomate. Força e defesa. |
| `ananas_grelhado` | Ananás Grelhado | Receita da Rosa. Doce e quente. Ficas mais rápid{o/a}. |
| `bomba_tinta` | Bomba de Tinta | Tinta de polvo num saco. Cega quem a apanhar. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `sardinha` | Sardinha | Pequena, prateada e deliciosa grelhada. Toda a gente concorda. |
| `robalo` | Robalo | Peixe de mar aberto. Os pescadores do porto juram que é o mais esperto. |
| `peixe_palhaco` | Peixe-Palhaço | Laranja e branco. Vive nas anémonas. Não tem graça nenhuma. |
| `atum_azul` | Atum Azul | Enorme e rápido. Só se apanha do barco, de manhã. |
| `peixe_lua` | Peixe-Lua | Redondo e achatado como uma lua. Só aparece com sol forte. |
| `celacanto_anciao` | Celacanto Ancião | **Lendário.** Um peixe mais velho do que as sereias. Vive nas fontes quentes da fossa. |
| `semente_alga_doce` | Esporos de Alga Doce | Plantam-se no lago da quinta. Dão alga sempre. |
| `semente_ananas` | Sementes de Ananás da Ilha | Da Rosa. Um ananás demora doze dias. Vale a pena. |
| `semente_batata_doce` | Sementes de Batata-Doce | Da Vila das Pérolas. Laranja por dentro. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `garrafa_mensagem` | Garrafa com Mensagem | Um mapa do tesouro dentro de uma garrafa. Clássico. |
| `carta_1450` | Carta da Jogadora nº 1 450 | Para a Inês. Nunca foi mandada. Lê-a em voz alta. |
| `cancao_312` | Fim da Canção | O último verso da canção do nº 312, riscado numa porta. |
| `caderno_duarte` | Caderno do Duarte | Um caderno da escola com um nome na capa. O nº 3 377 tinha um nome. |
| `diario_bordo` | Diário de Bordo | Novecentos anos de "amanhã". A última página é do Kai. |
| `carta_tomas` | Carta do Tomás | Do barco "Gaivota", no fundo da fossa. Os "a" parecem "o". Leva-a à Dona Marta. |
| `ovo_polvo` | Ovo de Polvo | Transparente. Vê-se um polvo pequenino a mexer lá dentro. Não o deixes partir. |
| `chave_almirante` | Chave do Almirante | Do cofre do Capitão Esqueleto. Abre a porta do Naufrágio Antigo. |
| `trofeu_chapeu_capitao` | Chapéu do Capitão | Troféu do Capitão Esqueleto. O papagaio ainda está agarrado à pena. Também é troféu. |
| `trofeu_escama_leviata` | Escama do Leviatã | Troféu. Do tamanho de uma porta. Ainda tem um reflexo verde, triste. |

---

## Região 7 — Vulcão

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `obsidiana` | Obsidiana | Vidro negro que nasce da lava. Corta como uma navalha. |
| `barra_obsidiana` | Barra de Obsidiana | Obsidiana fundida com brasa de lava. Negra e espelhada. |
| `brasa_lava` | Brasa de Lava | Pedra que nunca arrefece. O carvão desta região. |
| `lenho_brasa` | Lenho-Brasa | Madeira negra que não arde. A árvore que sobreviveu ao fogo. |
| `couro_salamandra` | Couro de Salamandra | Vermelho e escamoso. Quem o veste sente menos o calor. |
| `seda_ignifuga` | Seda Ignífuga | Dos casulos da floresta queimada. O fogo não lhe pega. |
| `cristal_magma` | Cristal de Magma | Lava que arrefeceu depressa e ficou a brilhar por dentro. |
| `rubi` | Rubi | Gema vermelha dos veios do Bastião. Fogo em pedra. Os anões adoram-nos. |
| `pimenta_lava` | Pimenta-Lava | A pimenta mais picante da torre. As salamandras acalmam-se com ela. Tu não. |
| `flor_cinza` | Flor de Cinza | Cinzenta e bonita. Cresce na cinza. Faz Poção Fresca. |
| `enxofre` | Enxofre | Amarelo e malcheiroso. Pólvora e bombas. |
| `nucleo_magma` | Núcleo de Magma | O coração de um golem de magma. Ainda quente. |
| `cinza` | Cinza | Do mundo que ardeu. Cobre tudo. Serve para pintar. |
| `cinza_magica` | Cinza Mágica | Cinza de elemental. Brilha um bocadinho. A Lena pinta com ela. |
| `escama_ardente` | Escama Ardente | De salamandra. Quente ao toque, sempre. |
| `essencia_fogo` | Essência de Fogo | Um bocadinho de elemental num frasco. Não abras ao pé de nada que arda. |
| `chifre_diabrete` | Chifre de Diabrete | Pequeno e torto. Os diabretes não sentem falta. Têm outro. |
| `pele_cao_infernal` | Pele de Cão Infernal | Negra e quente. Faz capas para quem tem frio. Ninguém tem frio aqui. |
| `presa_ardente` | Presa Ardente | Dente de cão infernal. Pontas de flecha que queimam. |
| `asa_cinza` | Asa de Cinza | De morcego. Desfaz-se se apertares. |
| `carapaca_rocha` | Carapaça de Rocha | De escorpião de lava. Pesada e quente. |
| `ferrao_lava` | Ferrão de Lava | Pinga fogo. Guarda-o num frasco de pedra. |
| `pergaminho_fogo` | Pergaminho de Fogo | Orações ao Titã. Não as leias em voz alta. |
| `placa_n7` | Placa Nº 7 | Do Golem Forjado Nº 7. Material lendário para armaduras. Tem a assinatura do Gizmo num canto. Pequenina. |
| `nucleo_obsidiana` | Núcleo de Obsidiana | O coração do Nº 7. O Gizmo quer-no para uma coisa que não explode. Diz ele. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_obsidiana` | Espada de Obsidiana | Negra e espelhada. Vês a tua cara na lâmina. E a do inimigo, assustada. |
| `espada_grande_obsidiana` | Espada Grande de Obsidiana | Um muro de vidro negro com punho. |
| `adaga_obsidiana` | Adaga de Obsidiana | Mais afiada do que qualquer metal. Também mais frágil. Cuidado com ela. |
| `katana_obsidiana` | Katana de Obsidiana | Os anões fizeram-na sem saber o que era uma katana. Saiu bem na mesma. |
| `machado_obsidiana` | Machado de Obsidiana | Corta lenho-brasa e golens. Os golens queixam-se. |
| `martelo_obsidiana` | Martelo de Obsidiana | O martelo preferido do Clã Brasa. Pesa como uma promessa. |
| `lanca_obsidiana` | Lança de Obsidiana | Ponta de vidro negro e cabo de lenho-brasa. Não arde nem parte. |
| `foice_obsidiana` | Foice de Obsidiana | Ceifa em arco. Deixa um risco escuro no ar. |
| `arco_obsidiana` | Arco de Obsidiana | Lenho-brasa e seda ignífuga. Flechas com ponta de vidro negro. |
| `besta_obsidiana` | Besta de Obsidiana | Os virotes partem-se dentro dos inimigos. É nojento. Funciona. |
| `cajado_obsidiana` | Cajado de Obsidiana | Com um rubi na ponta. Os feitiços de fogo saem maiores. |
| `manoplas_obsidiana` | Manoplas de Obsidiana | Socos que fazem faíscas. |
| `arco_fenix` | Arco Fénix | Da Fénix de Cinza. Uma vez por dia, se morreres, renasces com um bocadinho de vida. |
| `lanca_magma` | Lança de Magma | Da Serpente de Lava. As estocadas deixam um rasto de fogo. |
| `machado_brasa_viva` | Machado Brasa-Viva | Do Ent Carbonizado. Ainda arde. Às vezes queima quem leva com ele. |
| `martelo_broca` | Martelo-Broca | Da Escavadora. Minera como uma picareta muito boa e ignora parte da defesa. |
| `manoplas_geiser` | Manoplas Géiser | Do Sapo-Vulcão. O último golpe do combo atira o inimigo ao ar. |
| `espada_grande_portao` | Espada Grande Portão | Do Golem Portão. Enquanto carregas, és uma porta fechada. |
| `cajado_sumo_sacerdote` | Cajado do Sumo-Sacerdote | As bolas de fogo saem maiores. A máscara dourada vinha junto. Não a uses. |
| `martelo_forja` | Martelo da Forja | Do Ferreiro Infernal. Os golpes ardem. Ainda cheira a metal fundido. |
| `coracao_magma` | Coração de Magma | Espada grande do Titã. O ataque carregado rebenta em lava. Está sempre morna. |
| `lamina_kai` | Lâmina do Kai | A espada que o Sistema mandou acabar para o Kai. Rápida. Fria. Pesa mais do que devia. |
| `arma_inacabada_10000` | Arma Inacabada nº 10 000 | Uma lâmina sem fio e sem punho, com o teu número no cabo. Leva-a ao Brom. |
| `martelo_primordial` | Martelo Primordial | Arma secreta da Forja Primordial. O ataque carregado faz uma erupção. Foi feito para os primeiros. Agora é teu. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `salamandra_cabeca` | Elmo de Salamandra | Couro vermelho e obsidiana. O calor sobe metade. |
| `salamandra_corpo` | Couraça de Salamandra | Escamas que não aquecem. Por dentro, fresco. Por fora, fogo. |
| `salamandra_maos` | Luvas de Salamandra | Pegas em brasas sem te queimar. Não experimentes. Funciona, mas não experimentes. |
| `salamandra_pes` | Botas de Salamandra | Andam na cinza quente sem fazer bolhas. |
| `salamandra_capa` | Capa de Seda Ignífuga | Leve como fumo. O fogo escorrega por ela. |
| `anel_rubi_rainha` | Anel de Rubi da Rainha | Da Rainha Hildur. Mais 15% de dano de Fogo. |
| `amuleto_amizade` | Amuleto da Amizade | Do Kai, no 68. Melhor em tudo quando tens alguém ao teu lado. Ele diz que não foi presente. Foi. |
| `coleira_tricefalo` | Coleira de Tricéfalo | Do tamanho de um pneu. Mais 10% de dano elemental. Ainda cheira a fumo. |
| `tunica_cultista` | Túnica de Cultista | Cosmético. Vermelha, com capuz. Os cultistas não reparam em ti. Os outros sim. |
| `pena_fenix` | Pena de Fénix | Revive-te uma vez com metade da vida. Depois desfaz-se em cinza. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_obsidiana` | Picareta de Obsidiana | Parte obsidiana, rubis e cristal de magma. |
| `machado_lenhador_obsidiana` | Machado de Lenhador de Obsidiana | Corta lenho-brasa, a madeira que não arde. |
| `cana_ignifuga` | Cana Ignífuga | Do Mestre Ragnar. Para pescar na lava. O isco é que derrete. |
| `camara_gil` | Câmara do Gil | Velha e pesada. Abre o **Modo Foto**. |
| `automato_quinta` | Autómato de Quinta | Do Gizmo, com o núcleo do Nº 7. Rega a quinta todos os dias. Às vezes rega-te a ti. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `pocao_fresca` | Poção Fresca | Sabe a hortelã e a arrependimento. Baixa o Calor. |
| `pocao_ignifuga` | Poção Ignífuga | Durante uns minutos, a lava não te queima. Não abuses. |
| `ovos_geiser` | Ovos de Géiser | Receita da Fumarola. Cozidos no géiser. O calor sobe metade durante 5 minutos. |
| `batata_vulcanica_assada` | Batata Vulcânica Assada | Quente por dentro durante horas. Literalmente. |
| `pao_cinzas` | Pão das Cinzas | Receita da Mãe Brasa. Saiu queimado da primeira vez. Agora sai bem. Sabe a recomeço. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `caranguejo_basalto` | Caranguejo de Basalto | Preto como a rocha das margens. Belisca quente. |
| `peixe_geiseres` | Peixe dos Géiseres | Vive na água quente dos lagos azuis. Já vem meio cozido. |
| `carpa_negra` | Carpa Negra | Do Lago Negro. Só sai à noite. Tem olhos de brasa. |
| `peixe_brasa` | Peixe-Brasa | Nada na lava. Brilha como uma brasa. Pesca-se com a Cana Ignífuga. |
| `enguia_magma` | Enguia de Magma | Só aparece nas erupções. Comprida, a escorrer fogo. |
| `fenix_profundezas` | Fénix das Profundezas | **Lendário.** Um peixe de fogo com barbatanas como asas. Do poço do 70, ao meio-dia. |
| `semente_pimenta_lava` | Sementes de Pimenta-Lava | Para quem gosta de chorar a comer. |
| `semente_flor_cinza` | Sementes de Flor de Cinza | Florescem em qualquer estação. Cinzentas e bonitas. |
| `semente_lenho_brasa` | Semente de Lenho-Brasa | Da Mãe Brasa. Uma árvore que não arde. Demora 21 dias. Vale a pena. |
| `semente_batata_vulcanica` | Sementes de Batata Vulcânica | Da Fumarola. Batatas que aquecem as mãos. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `carta_brom` | Carta do Brom | Para o tio Ragnar. Três linhas. A letra é péssima. A última linha diz "tenho saudades" e está riscada. Ainda se lê. |
| `peca_mestra` | Peça Mestra | O motor da Escavadora. Dentro tinha uma pedra com o símbolo dos cultistas. |
| `runa_forja_primordial` | Runa da Forja Primordial | Do Ragnar e da Rainha. Abre a porta dos Veios Profundos. |
| `broto_verde` | Broto Verde | O último broto verde do mundo queimado. Rega-o. |
| `trofeu_bigorna_infernal` | Bigorna Infernal | Troféu do Ferreiro. Uma forja pequena para a casa. Melhora armas até +3. |
| `trofeu_pedra_coracao` | Pedra-Coração do Titã | Troféu do Titã de Magma. Aquece a casa toda. No Inverno é a coisa mais útil da torre. |
| `quadro_cinza` | Quadro de Cinza | Móvel. Da Lena. Cinzento, com cem cores se olhares bem. |

---

## Região 8 — Reino Assombrado

### Materiais e drops

| ID | Nome | Descrição |
|---|---|---|
| `minerio_mitril` | Minério de Mitril (amaldiçoado) | Prateado, com um brilho roxo. Tem de ser purificado com água benta. |
| `lingote_mitril` | Lingote de Mitril | Mitril purificado. Leve como uma pena e mais forte do que o aço. |
| `ebano_morto` | Ébano Morto | Madeira negra de árvores que morreram de pé. Dura e silenciosa. |
| `asa_gargula` | Asa de Gárgula | Couro de pedra que dobra. O couro da região. |
| `fio_espectral` | Fio Espectral | Ectoplasma tecido no tear. Quase não se vê. Não rasga. |
| `lagrima_fantasma` | Lágrima de Fantasma | Uma gota fria que brilha. No Mercado Fantasma serve de moeda. |
| `onix` | Ónix | Gema negra das catacumbas. Guarda sombras. |
| `diamante` | Diamante | Dos vitrais partidos da catedral. Guarda a luz. |
| `rosa_negra` | Rosa Negra | Negra e perfumada. Tocar dá maldição. Oferecer dá… depende de quem. |
| `salvia_sagrada` | Sálvia Sagrada | Do claustro do mosteiro. Com água limpa, faz água benta. |
| `lirio_lua` | Lírio da Lua | Só abre à noite. Faz poções de magia. |
| `pagina_antiga` | Página Antiga | De um livro possuído. Tem receitas, feitiços ou listas de compras de há mil anos. |
| `tinta_magica` | Tinta Mágica | Escreve sozinha se a deixares aberta. Não a deixes aberta. |
| `trapo` | Trapo | De zombie. Não. Não toques. Pronto, já tocaste. |
| `dente` | Dente | De zombie. Ninguém sabe de quem era antes. |
| `armadura_velha` | Armadura Velha | De cavaleiro esqueleto. Funde-se em ferro e às vezes tem mitril. |
| `fragmento_mitril` | Fragmento de Mitril | Um pedaço de mitril já purificado. Raro e precioso. |
| `pedra_esculpida` | Pedra Esculpida | De gárgula. Tem uma cara pequena. A cara olha para ti. |
| `presa_vampiro` | Presa de Vampiro | Afiada e branca. O Caçador Van coleciona-as num frasco. |
| `sangue_antigo` | Sangue Antigo | Escuro e espesso num frasco de vidro. Para alquimia que é melhor não perguntar. |
| `veu_banshee` | Véu de Banshee | Transparente como fumo. Ouve-se um suspiro quando lhe tocas. |
| `placa_mitril` | Placa de Mitril | De armadura viva. Já purificada pelo fantasma de dentro. Ninguém sabe como. |
| `elmo_vazio` | Elmo Vazio | Decoração. Às vezes ouve-se um suspiro lá dentro. |
| `osso_gigante_74` | Osso do Colosso | Um osso do Colosso de Ossos. Pesado de mais para o que vale. Pesado de mais para o que lembra. |

### Armas

| ID | Nome | Descrição |
|---|---|---|
| `espada_mitril` | Espada de Mitril | Prateada e leve como uma pena. Os mortos-vivos tremem quando a veem. |
| `espada_grande_mitril` | Espada Grande de Mitril | Enorme e leve. Parece impossível. É mitril. |
| `adaga_mitril` | Adaga de Mitril | Brilha no escuro como um bocadinho de lua. |
| `katana_mitril` | Katana de Mitril | O fio nunca se gasta. Os monges da Ordem usam-nas. |
| `machado_mitril` | Machado de Mitril | Corta ébano morto e cavaleiros esqueleto com o mesmo som. |
| `martelo_mitril` | Martelo de Mitril | Parte crânios e maldições. |
| `lanca_mitril` | Lança de Mitril | A preferida dos caçadores de vampiros. Longa e brilhante. |
| `foice_mitril` | Foice de Mitril | A arma dos ceifeiros que caçam a morte. Irónico. |
| `arco_mitril` | Arco de Mitril | Ébano morto e mitril. As flechas cantam baixinho. |
| `besta_mitril` | Besta de Mitril | Virotes de prata que atravessam fantasmas. |
| `cajado_mitril` | Cajado de Mitril | Com um diamante na ponta. A luz cura quem está perto. |
| `manoplas_mitril` | Manoplas de Mitril | Socos que brilham. Os zombies voltam a cair e já não se levantam. |
| `arco_sentinela` | Arco da Sentinela | Da Sentinela da Muralha. As flechas ignoram parte da defesa. |
| `martelo_sino` | Martelo-Sino | Do Pregoeiro. Às vezes atordoa tudo à volta. Toca quando bates. |
| `pa_machado_coveiro` | Pá-Machado do Coveiro | Do Coveiro Ghoul. Um machado que também escava tesouros. |
| `espada_grande_ossos` | Espada Grande de Ossos | Do Colosso. O ataque carregado lança três crânios que perseguem os inimigos. |
| `adaga_rosa_negra` | Adaga Rosa Negra | Da Rainha das Rosas. Os críticos amaldiçoam. Tem espinhos no cabo. Usa luvas. |
| `katana_vitral` | Katana Vitral | Do Anjo de Vitral. Cada golpe muda de cor e de elemento. |
| `manoplas_carcereiro` | Manoplas do Carcereiro | O sexto golpe prende o inimigo com uma corrente. |
| `lanca_comandante` | Lança do Comandante | Do Comandante dos Cavaleiros. Os teus companheiros ficam mais fortes. |
| `grimorio_proibido` | Grimório Proibido | Cajado-livro do Lich. Chama esqueletos que lutam por ti. Às vezes lê-se sozinho à noite. |
| `lamina_rei_caido` | Lâmina do Rei Caído | A espada do Rei Sem Coroa. Ignora a defesa. Pesa como uma desculpa. |
| `foice_tesoura` | Foice-Tesoura | A tesoura de poda do Jardineiro, feita foice. Cortes duplos. |
| `besta_mitril_abencoada` | Besta de Mitril Abençoada | A segunda besta do Caçador Van (a primeira chama-se Clementina). Dispara Luz. |
| `foice_rainha_viuva` | Foice da Rainha Viúva | Arma secreta da Cripta da Rainha. Cada inimigo que matas liberta um fantasma que luta por ti. |

### Armaduras e acessórios

| ID | Nome | Descrição |
|---|---|---|
| `mitril_cabeca` | Elmo de Mitril Abençoado | Brilha um bocadinho no escuro. Os fantasmas desviam o olhar. |
| `mitril_corpo` | Couraça de Mitril Abençoado | Leve como pano, forte como pedra. Abençoada pelo Irmão Bento. |
| `mitril_maos` | Luvas de Mitril | Seguram água benta sem a entornar. É mais importante do que parece. |
| `mitril_pes` | Botas de Mitril | Silenciosas. Os livros da biblioteca não acordam. |
| `mitril_capa` | Capa de Fio Espectral | Quase invisível. Atravessa o vento. |
| `anel_mitril` | Anel de Mitril | Do Irmão Bento. Mais 10% de RES. Não pesa nada. |
| `leque_condessa` | Leque da Condessa | Preto, com rendas. Cada golpe rouba um bocadinho de vida. Abana-te com ele no calor. |
| `chapeu_palha_jardineiro` | Chapéu de Palha do Jardineiro | Mais uma colheita na quinta. Cheira a terra e a rosas. |
| `capa_vampiro` | Capa de Vampiro | Cosmético. Vermelha por dentro, preta por fora. Os morcegos seguem-te um bocadinho. |
| `bencao_luz` | Bênção da Luz | Não é um objeto: é uma marca na tua ficha. Mais 10% de dano de Luz para sempre. |

### Ferramentas e utilidades

| ID | Nome | Descrição |
|---|---|---|
| `picareta_mitril` | Picareta de Mitril | Parte mitril, ónix e diamantes. |
| `machado_lenhador_mitril` | Machado de Lenhador de Mitril | Corta ébano morto sem fazer barulho. |
| `lanterna_sagrada` | Lanterna Sagrada | Da Ordem da Luz. Levas uma zona de luz contigo durante 5 minutos. |
| `chave_mestra` | Chave Mestra das Masmorras | Três partes juntas. Abre todas as celas do andar 78. |

### Consumíveis e comida

| ID | Nome | Descrição |
|---|---|---|
| `agua_benta` | Água Benta | Sálvia e água limpa, abençoadas. Tira maldições e consagra sepulturas. Não se bebe. |
| `pocao_sombras` | Poção das Sombras | Feita com rosa negra. Ficas invisível às criaturas da sombra durante um bocadinho. |
| `pao_fantasma` | Pão Fantasma | Receita do Hugo. Durante 10 segundos, atravessas paredes finas. Sabe a pão. Estranhamente. |
| `sopa_abobora` | Sopa de Abóbora | Laranja e quente. A preferida da Noite dos Espíritos. |
| `receitas_teresa` | Receitas da Teresa | Cinco receitas novas na Estalagem. Nenhuma tem ratos. Ela promete. |

### Peixes e plantas

| ID | Nome | Descrição |
|---|---|---|
| `lucio_assombrado` | Lúcio Assombrado | Do fosso das muralhas. Tem os olhos brancos. Morde depois de pescado. |
| `peixe_fantasma` | Peixe-Fantasma | Transparente. Nada nos canais da Cidade Fantasma à noite. |
| `enguia_cripta` | Enguia da Cripta | Vive na água escura das catacumbas. Pálida e comprida. |
| `peixe_vitral` | Peixe-Vitral | As escamas parecem vitrais coloridos. Só com sol, no lago do mosteiro. |
| `truta_prata_negra` | Truta de Prata Negra | Do rio do poço das masmorras. Brilha como mitril. |
| `peixe_lua_negra` | Peixe da Lua Negra | **Lendário.** Só na lua nova, à meia-noite, quando a Fonte Seca se enche de água negra. |
| `semente_rosa_negra` | Sementes de Rosa Negra | Do Jardineiro. Na quinta crescem negras. Talvez um dia nasçam brancas. |
| `semente_salvia` | Sementes de Sálvia Sagrada | Do Irmão Bento. Para fazer água benta em casa. |
| `semente_abobora` | Sementes de Abóbora | Da Hana. Lanternas para a Noite dos Espíritos. |
| `bolbo_lirio_lua` | Bolbo de Lírio da Lua | Só floresce à noite. Na quinta também. |

### Itens de missão e especiais

| ID | Nome | Descrição |
|---|---|---|
| `boneca_matilde` | A Matilde | A boneca da Elise. De pano, com um olho de botão a menos. |
| `carta_rosalinda` | Carta da Rosalinda | Para o cavaleiro Gaspar. Perfumada a rosas brancas. |
| `carta_gaspar` | Carta do Gaspar | Para a menina Rosalinda. A letra treme. |
| `anel_noivado_fantasma` | Anel de Noivado Fantasma | Ficou na borda da fonte. Presente que quase toda a gente adora. |
| `carta_celia` | Carta da Célia | Para a Abadessa Lumina. Começa com "Desculpe a demora". Vinte anos de demora. |
| `resposta_abadessa` | Resposta da Abadessa | Curta. A Célia vai chorar. |
| `caderno_odilia` | Caderno de Mapas da Odília | Queimado nas pontas. A última página é para o Gorvan. Ele ficou com ele. |
| `machado_gorvan` | Machado do Gorvan | Decoração. O machado que o Gorvan deixou no 74 há vinte anos. Deu-to. |
| `estandarte_alvorada` | Estandarte de Alvorada | Um sol a nascer bordado a ouro. Rasgado. Leva-o à Elva. |
| `livros_fausto` | Livros Perdidos | Cinco livros do Arquivo Selado. O Fausto vai chorar. Vai fingir que é pó. |
| `trofeu_coroa_reino` | Coroa do Reino | Troféu do Rei Sem Coroa. Leve. Bonita. Ninguém a quer pôr. |
| `calice_prata` | Cálice de Prata | Decoração. Do banquete dos cavaleiros. Está sempre cheio de nada. |
| `espada_benta` | Espada Benta | Decoração. Da cripta debaixo do altar da catedral. Brilha nas noites de lua cheia. |
