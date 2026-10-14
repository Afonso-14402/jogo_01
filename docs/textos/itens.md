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
