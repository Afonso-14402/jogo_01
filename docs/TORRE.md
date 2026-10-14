# A Torre — 100 andares

Visão geral da torre. **Os detalhes de cada andar** (bioma, zonas, mecânica, monstros, guardião, segredo, puzzle,
página de lore, desafios e peças de arte) estão nos ficheiros das regiões:

| Região | Andares | Ficheiro |
|---|---|---|
| 1 · Floresta | 1–10 | [`regioes/r01_floresta.md`](regioes/r01_floresta.md) |
| 2 · Cavernas e Minas | 11–20 | [`regioes/r02_cavernas.md`](regioes/r02_cavernas.md) |
| 3 · Pântano e Selva | 21–30 | [`regioes/r03_pantano.md`](regioes/r03_pantano.md) |
| 4 · Deserto | 31–40 | [`regioes/r04_deserto.md`](regioes/r04_deserto.md) |
| 5 · Gelo | 41–50 | [`regioes/r05_gelo.md`](regioes/r05_gelo.md) |
| 6 · Oceano | 51–60 | [`regioes/r06_oceano.md`](regioes/r06_oceano.md) |
| 7 · Vulcão | 61–70 | [`regioes/r07_vulcao.md`](regioes/r07_vulcao.md) |
| 8 · Reino Assombrado | 71–80 | [`regioes/r08_reino_assombrado.md`](regioes/r08_reino_assombrado.md) |
| 9 · Céu | 81–90 | [`regioes/r09_ceu.md`](regioes/r09_ceu.md) |
| 10 · Abismo / Coração da Torre | 91–100 | [`regioes/r10_abismo.md`](regioes/r10_abismo.md) |

Os 20 bosses estão em [`BOSSES.md`](BOSSES.md) e as povoações em [`CIDADES.md`](CIDADES.md).

---

## 1. Números da torre

| | Quantidade |
|---|---|
| Andares | 100 (+ infinitos no pós-jogo) |
| Regiões | 10 |
| Monstros normais | 80 (8 por região) + versões Elite |
| Monstros com nome | 20 |
| Guardiões dos andares | 79 (+ o duelo com o Kai) |
| Mini-bosses / bosses | 10 / 10 |
| Masmorras escondidas (com boss) | 10 |
| Povoações | 26 |
| Páginas de lore | 100 (+ 10 extra) |
| Puzzles principais | 100 (um por andar) |
| Desafios | 200 (dois por andar) |

---

## 2. Como é um andar

Todos os andares seguem a mesma estrutura (assim o código é igual para todos e só mudam os dados):

1. **Chegada** pela escada do andar anterior (ou pelo cristal).
2. **Zona Segura** perto da entrada: fogueira, cristal de teletransporte, às vezes o Tibério (loja). Aqui não aparecem monstros.
3. **3 a 5 zonas** com nomes, cada uma com a sua lista de monstros e recursos.
4. **Mecânica especial** do andar (ex.: erva alta, água tóxica, gravidade invertida).
5. **Segredos** (1 a 3) e **puzzle principal** (1).
6. **Página de lore** escondida (1).
7. **Guardião** junto à escada para o andar seguinte (ou o mini-boss / boss nos andares 5 e 10 de cada região).
8. **Escada** para o andar seguinte, que só abre depois de vencer o guardião (na 1.ª vez).

| Regra | Valor |
|---|---|
| Tamanho | 150×150 m a 300×300 m (andares verticais: até 400 m de altura) |
| Tempo para explorar | 10 a 20 minutos |
| Nível dos monstros | igual ao número do andar (ver `SISTEMAS.md`, secção 6.3) |
| Voltar a entrar | monstros, materiais e baús voltam a ser sorteados (os segredos e o puzzle ficam resolvidos) |
| Clima | o clima da região (ver cada região) |
| Desafios | 2 por andar; cada um dá uma medalha e uma recompensa |

### Como fazer 100 andares diferentes sem enlouquecer
1. Cada região tem **um kit de peças** no Blender (≈ 25–30 peças).
2. Cada **andar** usa o kit da região + **3 a 5 peças especiais só dele**.
3. Cada andar tem **luz, céu, nevoeiro e partículas próprios** (feitos no Godot, sem arte nova).
4. O andar 94 reaproveita os kits de todas as regiões e o 100 reaproveita o da região 1.
5. Os **Andares do Eco** (pós-jogo) são montados **ao acaso** com os kits de todas as regiões.

---

## 3. Os 100 andares

💀 = mini-boss · 👑 = boss

| Andar | Nome | Região | Guardião / boss | Povoação |
|---|---|---|---|---|
| 1 | Prado do Despertar | 1 · Floresta | Coelho-Chifre Ancião |  |
| 2 | Bosque dos Sussurros | 1 · Floresta | Coruja Sombria | Acampamento dos Lenhadores |
| 3 | Ribeiro Cristalino | 1 · Floresta | Lagostim Couraçado |  |
| 4 | Clareira dos Cogumelos | 1 · Floresta | Rainha dos Esporos |  |
| 5 | Toca do Javali-Rei | 1 · Floresta | 💀 Javali-Rei |  |
| 6 | Colinas Floridas | 1 · Floresta | Abelha-Rainha Melífera |  |
| 7 | Floresta Antiga | 1 · Floresta | Guardião de Musgo | Folhalta |
| 8 | Ruínas Cobertas de Musgo | 1 · Floresta | Cavaleiro de Pedra Musgosa |  |
| 9 | Lago da Névoa | 1 · Floresta | Serpente da Névoa |  |
| 10 | Coração da Floresta | 1 · Floresta | 👑 Ent Ancião |  |
| 11 | Entrada da Mina | 2 · Cavernas | Vagoneta Assombrada | Posto Mineiro Fundo-Rocha |
| 12 | Túneis dos Mineiros Perdidos | 2 · Cavernas | Touro das Galerias |  |
| 13 | Gruta de Cristal | 2 · Cavernas | Prisma Vivo |  |
| 14 | Rio Subterrâneo | 2 · Cavernas | Barqueiro Afogado |  |
| 15 | Ninho das Aranhas | 2 · Cavernas | 💀 Aranha-Mãe |  |
| 16 | Cavernas Fúngicas | 2 · Cavernas | Água-Viva Fúngica | Mycélia, Cidade dos Fungoides |
| 17 | Fosso dos Ecos | 2 · Cavernas | Morcego-Rei dos Ecos |  |
| 18 | Forja Anã Abandonada | 2 · Cavernas | Sentinela Anã |  |
| 19 | Lago de Cristal Negro | 2 · Cavernas | Reflexo Negro |  |
| 20 | Trono do Golem | 2 · Cavernas | 👑 Golem de Cristal |  |
| 21 | Margem do Pântano | 3 · Pântano | Garça-Lança |  |
| 22 | Charco Venenoso | 3 · Pântano | Lodo Tóxico |  |
| 23 | Selva Profunda | 3 · Pântano | Pantera de Jade |  |
| 24 | Aldeia dos Homens-Lagarto | 3 · Pântano | Totem Vivo de Sssar | Aldeia Sssar |
| 25 | Templo Afundado | 3 · Pântano | 💀 Serpente do Lodo |  |
| 26 | Mangue das Raízes | 3 · Pântano | Caranguejo-Violinista Gigante | Vila Coaxa |
| 27 | Cascata Esmeralda | 3 · Pântano | Ninfa da Cascata |  |
| 28 | Copas das Árvores | 3 · Pântano | Grande Bugio | Refúgio das Copas |
| 29 | Ninho das Flores Carnívoras | 3 · Pântano | Dríade Corrompida |  |
| 30 | Altar da Hidra | 3 · Pântano | 👑 Hidra do Pântano |  |
| 31 | Dunas Douradas | 4 · Deserto | Lagarto-Duna Gigante |  |
| 32 | Oásis Escondido | 4 · Deserto | A Miragem | Oásis de Zahra |
| 33 | Desfiladeiro Vermelho | 4 · Deserto | Abutre Rei |  |
| 34 | Cidade Enterrada | 4 · Deserto | Golem de Arenito | Acampamento dos Escavadores |
| 35 | Ninho dos Escorpiões | 4 · Deserto | 💀 Escorpião Imperador |  |
| 36 | Tempestade de Areia | 4 · Deserto | Djinn da Tempestade |  |
| 37 | Cemitério de Ossos Gigantes | 4 · Deserto | Cavaleiro de Ossos Montado | Nómadas do Vento |
| 38 | Pirâmide: Entrada | 4 · Deserto | Esfinge Menor |  |
| 39 | Pirâmide: Câmaras | 4 · Deserto | Sacerdote-Chacal |  |
| 40 | Sala do Faraó Eterno | 4 · Deserto | 👑 Faraó Eterno |  |
| 41 | Tundra Gelada | 5 · Gelo | Morsa Gigante |  |
| 42 | Pinhal Nevado | 5 · Gelo | Alce Fantasma | Pinhal-do-Norte |
| 43 | Lago Congelado | 5 · Gelo | Kraken do Gelo |  |
| 44 | Grutas de Gelo Azul | 5 · Gelo | Coração de Cristal Azul |  |
| 45 | Covil do Yeti | 5 · Gelo | 💀 Yeti Ancião |  |
| 46 | Aldeia dos Caçadores | 5 · Gelo | Wendigo | Aldeia dos Caçadores |
| 47 | Glaciar Rachado | 5 · Gelo | Tartaruga-Glaciar |  |
| 48 | Campos da Aurora | 5 · Gelo | Raposa Aurora | Mosteiro da Aurora |
| 49 | Fortaleza de Gelo | 5 · Gelo | Cavaleiro de Gelo |  |
| 50 | Trono do Inverno | 5 · Gelo | 👑 Dragão de Gelo |  |
| 51 | Praia das Conchas | 6 · Oceano | Tartaruga-Marinha Anciã |  |
| 52 | Arquipélago | 6 · Oceano | Gaivota Gigante Ladra | Porto Arquipélago |
| 53 | Navio Fantasma | 6 · Oceano | O Imediato Fantasma |  |
| 54 | Recife de Coral | 6 · Oceano | Peixe-Leão Rei | Vila das Pérolas |
| 55 | Gruta dos Piratas | 6 · Oceano | 💀 Capitão Esqueleto |  |
| 56 | Floresta de Algas | 6 · Oceano | Dragão-Marinho Folhado |  |
| 57 | Cidade Submersa | 6 · Oceano | Golem de Coral | Coralina |
| 58 | Fossa Abissal | 6 · Oceano | Tamboril Abissal |  |
| 59 | Templo do Mar | 6 · Oceano | Guardião das Marés |  |
| 60 | Trono do Leviatã | 6 · Oceano | 👑 Leviatã |  |
| 61 | Planícies de Cinza | 7 · Vulcão | Fénix de Cinza | Acampamento das Cinzas |
| 62 | Rios de Lava | 7 · Vulcão | Serpente de Lava |  |
| 63 | Floresta Queimada | 7 · Vulcão | Ent Carbonizado |  |
| 64 | Minas de Obsidiana | 7 · Vulcão | Escavadora Anã Possuída | Bastião de Obsidiana |
| 65 | Forja Infernal | 7 · Vulcão | 💀 Ferreiro Infernal |  |
| 66 | Campos de Géiseres | 7 · Vulcão | Sapo-Vulcão | Termas dos Géiseres |
| 67 | Ponte sobre o Magma | 7 · Vulcão | Golem Portão de Obsidiana |  |
| 68 | Cratera Interior | 7 · Vulcão | Kai, Jogador nº 9 999 |  |
| 69 | Templo do Fogo | 7 · Vulcão | Sumo-Sacerdote das Chamas |  |
| 70 | Coração do Vulcão | 7 · Vulcão | 👑 Titã de Magma |  |
| 71 | Muralhas em Ruínas | 8 · Reino Assombrado | Sentinela da Muralha |  |
| 72 | Cidade Fantasma | 8 · Reino Assombrado | O Pregoeiro Fantasma | Mercado Fantasma |
| 73 | Cemitério Real | 8 · Reino Assombrado | Coveiro Ghoul |  |
| 74 | Catacumbas | 8 · Reino Assombrado | Colosso de Ossos |  |
| 75 | Biblioteca Proibida | 8 · Reino Assombrado | 💀 Lich Bibliotecário |  |
| 76 | Jardins Mortos | 8 · Reino Assombrado | Rainha das Rosas Negras |  |
| 77 | Catedral Partida | 8 · Reino Assombrado | Anjo Caído de Vitral | Mosteiro da Ordem da Luz |
| 78 | Masmorras do Castelo | 8 · Reino Assombrado | Carcereiro |  |
| 79 | Salão dos Cavaleiros Caídos | 8 · Reino Assombrado | Comandante dos Cavaleiros Caídos |  |
| 80 | Sala do Trono | 8 · Reino Assombrado | 👑 Rei Sem Coroa |  |
| 81 | Mar de Nuvens | 9 · Céu | Baleia das Nuvens |  |
| 82 | Ilhas Flutuantes | 9 · Céu | Golem-Ilha | Aerópolis |
| 83 | Pontes de Luz | 9 · Céu | Cavaleiro de Luz Sólida |  |
| 84 | Jardim Suspenso | 9 · Céu | Jardineira Celeste |  |
| 85 | Ninho dos Grifos | 9 · Céu | 💀 Grifo Real |  |
| 86 | Ruínas Celestes | 9 · Céu | Leão Alado de Mármore | Observatório Celeste |
| 87 | Tempestade Eterna | 9 · Céu | Senhor dos Trovões |  |
| 88 | Templo dos Ventos | 9 · Céu | Monge do Vento |  |
| 89 | Escadaria do Sol | 9 · Céu | Carruagem do Sol |  |
| 90 | Palácio Celeste | 9 · Céu | 👑 Serafim Caído |  |
| 91 | Porta do Vazio | 10 · Abismo | Porteiro do Vazio | Último Posto |
| 92 | Mar de Estrelas | 10 · Abismo | Baleia Estelar |  |
| 93 | Labirinto de Espelhos | 10 · Abismo | Rainha dos Espelhos |  |
| 94 | Ecos dos Andares | 10 · Abismo | Eco dos Guardiões |  |
| 95 | Jardim do Tempo | 10 · Abismo | 💀 Guardião do Tempo |  |
| 96 | Planície Invertida | 10 · Abismo | Gigante Invertido |  |
| 97 | Cidade dos Perdidos | 10 · Abismo | O Desistente | Cidade dos Perdidos |
| 98 | Biblioteca do Mundo | 10 · Abismo | Índice Vivo |  |
| 99 | Escada Final | 10 · Abismo | O Guardião da Escada |  |
| 100 | Topo da Torre | 10 · Abismo | 👑 O Administrador |  |

---

## 4. Andares do Eco (101+, pós-jogo)

- Abrem com a **Chave do Sistema** (arma do Administrador) no Topo da Torre.
- São **gerados ao acaso**: pedaços de kits de várias regiões ligados por pontes de luz, com Ecos de monstros de todas as regiões.
- Nível dos monstros = número do andar. A cada **10 andares** há um **Boss Desperto** (um dos 20 bosses mais forte).
- Recompensas: armas Míticas ao acaso, materiais Estelares, títulos (andar 150, 200…).
