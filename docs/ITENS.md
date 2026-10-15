# Itens

Poções, bombas, comida, ingredientes, materiais, plantas, animais da quinta, móveis e presentes.
Os materiais e peixes de cada região estão também nos ficheiros das regiões (secções 2 e 10).

---

## 1. Categorias

| Categoria | Empilha | Exemplos |
|---|---|---|
| Consumível de combate | 99 | poções, bombas, elixires |
| Comida | 99 | pratos com bónus |
| Ingrediente | 99 | farinha, ovos, legumes, peixe |
| Material | 99 (ou ilimitado na Bolsa de Materiais) | minérios, lingotes, madeiras, couros, fios, cristais, drops |
| Gema | 99 | rubi, safira… (ver `docs/EQUIPAMENTO.md`) |
| Semente | 99 | sementes de todas as regiões |
| Utilidade | 99 | tochas, Pedra de Regresso, iscos, chaves |
| Equipamento | 1 | armas, armaduras, acessórios |
| Móvel / Decoração | 1 | para a casa |
| Item de missão | — (vai para o Diário) | cartas, diários, objetos |

---

## 2. Poções e elixires (alquimia)

A **duração** dos bónus é de 3 minutos, salvo indicação. Só pode estar ativo **um bónus de cada tipo** (o novo substitui o antigo).

| Poção | Efeito | Receita (mesa de alquimia) | Preço | Disponível |
|---|---|---|---|---|
| Poção de Vida P | cura 30% do HP | 2 Erva Verde + 1 Água Limpa | 30 | início |
| Poção de Vida M | cura 50% | 2 Musgo Medicinal + 1 Poção de Vida P | 150 | região 3 |
| Poção de Vida G | cura 75% | 2 Flor-de-Neve + 1 Poção de Vida M | 600 | região 5 |
| Poção de Vida Máxima | cura 100% e tira todos os estados | 1 Lótus Estelar + 1 Poção de Vida G | 2 500 | região 10 |
| Poção de Mana P / M / G | 30% / 50% / 75% do MP | Cogumelo Luminoso · Lírio da Lua · Lágrima de Aurora (+ a anterior) | 40 / 180 / 700 | regiões 1 / 8 / 5 |
| Poção de Estamina | enche a Estamina e +30% regeneração | 2 Flor de Mel + 1 Água Limpa | 50 | região 1 |
| Poção Élfica | cura 20% de HP e 20% de MP | Folhalta (missão R1_07) | 120 | região 1 |
| Antídoto | tira Veneno | 1 Erva Verde + 1 Esporo | 25 | início |
| Ligadura | tira Sangrar | 2 Linho Bravo | 20 | início |
| Colírio | tira Cegueira | 2 Água Limpa + 1 Flor de Mel | 25 | início |
| Água Benta | tira Maldição; consagra sepulturas | 1 Sálvia Sagrada + 1 Água Limpa (ou Igreja) | 60 | Igreja / região 8 |
| Poção Purificadora | imune ao veneno do ambiente | 2 Lírio do Pântano + 1 Água Limpa | 90 | região 3 |
| Poção de Respirar | o Ar dura o triplo durante 5 min | 1 Anémona + 1 Alga Doce (ou Selene, caro) | 200 | Selene / região 6 |
| Poção de Visão Noturna | vês no escuro durante 5 min | 2 Musgo Luminoso | 70 | região 2 |
| Poção de Luz | ilumina 6 m durante 5 min | 1 Cogumelo Luminoso + 1 Cristal de Gruta | 60 | região 2 |
| Poção de Defesa | +20% DEF | 2 Raiz-Pedra + 1 Água Limpa | 80 | região 2 |
| Poção de Escamas | +30% DEF | 3 Escama de Lagarto + 1 Lírio do Pântano | 160 | região 3 (R3_04) |
| Poção de Força | +20% ATQ | 1 Presa de Lobo + 1 Erva Verde + 1 Flor de Mel | 90 | região 1 |
| Poção de Velocidade | +20% velocidade | 2 Pó de Fada | 80 | região 1 |
| Poção Quente | +40 Temperatura e imune a Frio | 1 Flor-de-Neve + 1 Bagas de Inverno | 120 | região 5 |
| Poção Fresca | −40 Calor e imune a Queimadura | 1 Flor de Cinza + 1 Cacto-Água | 150 | região 7 |
| Poção Ignífuga | podes pisar lava 5 s | 1 Escama Ardente + 1 Flor de Cinza + 1 Seda Ignífuga | 400 | região 7 |
| Poção de Leveza | saltas mais alto e cais devagar | 2 Flor-do-Vento | 250 | região 9 |
| Poção das Sombras | invisível 10 s (fora de combate) | 2 Rosa Negra + 1 Ectoplasma | 350 | região 8 |
| Poção de Regeneração | cura 2% por segundo durante 20 s | 1 Sanguessuga + 2 Musgo Medicinal | 200 | região 3 |
| Poção de Encolher | ficas pequeno 30 s (passas por buracos) | missão N_SELENE_3 | — | região 1 |
| Poção do Tempo | és imune a Parado e um pouco mais rápido | 2 Areia do Tempo + 1 Flor do Tempo | 900 | região 10 |
| Poção Surpresa | efeito ao acaso (bom ou mau!) | Doutor Girino (Vila Coaxa) | 100 | região 3 |
| Poção Arco-Íris | todos os bónus pequenos ao mesmo tempo (+10%) | missão R3_08 | 1 200 | região 3 |
| Elixir Estelar | cura tudo e +10% a tudo durante 5 min | 1 Lótus Estelar + 1 Pó de Estrela + 1 Poção de Vida G | 5 000 | região 10 |
| Pena de Fénix | revive-te com 50% quando morres (gasta-se) | não se faz: ninho de fénix (andar 66), baús de ouro raros | — | região 7 |

## 3. Bombas (alquimia)

| Bomba | Efeito | Receita |
|---|---|---|
| Bomba | dano de Fogo em área (3 m) | 1 Pólvora (Enxofre + Carvão) + 1 Pano Velho |
| Bomba de Gelo | Frio ×2 em área | 1 Essência de Neve + 1 Pólvora |
| Bomba de Pólen | Lentidão e Cegueira em área | 2 Pétala Carnívora |
| Bomba de Fumo | Cegueira em área; os inimigos perdem-te | 2 Areia Mágica |
| Bomba de Luz | dano de Luz em área (×1,5 a mortos-vivos) | 1 Água Benta + 1 Pólvora |
| Bomba Elétrica | Choque em área | 2 Gel Elétrico + 1 Pólvora |
| Saquinho de Sal | mata sanguessugas de um golpe; afasta fantasmas 5 s | 3 Sal |

---

## 4. Utilidades

| Item | Para quê | Onde | Preço |
|---|---|---|---|
| Pedra de Regresso | volta à cidade (3 s a canalizar, fora de combate) | lojas | 50 |
| Tocha | luz de 5 m durante 3 min; acende fogueiras e queima teias | lojas, Hilda | 10 |
| Frasco de Vaga-lumes | luz de 4 m durante 3 min | apanhar vaga-lumes (andar 2) | — |
| Lanterna Sagrada | zona de luz (Região 8) que levas contigo 5 min | Ordem da Luz | 120 |
| Giz de Mineiro | marca setas nas paredes (aparecem no mapa) | Hilda | 15 |
| Chave de Baú de Ouro | abre 1 baú de ouro | Elites (5%), guardiões (30%), Rook | 500 |
| Mapa do Tesouro | mostra um ponto para escavar | bandidos, piratas (3%) | — |
| Pedra Quente | a Temperatura não desce durante 5 min | receita R5_12 | 150 |
| Cantil | 3 bebidas de água (anula o sol e baixa o Calor) | Faisal | 100 |
| Cantil Infinito | água sem fim | missão R4_02 | — |
| Água Limpa | ingrediente | poços e fontes (grátis) | — |
| Iscos | Isco (normal), Isco Bom, Isco Dourado, Isco Lendário, Isco de Areia (pesca na areia), Isco Ignífugo (lava) | Pip, lojas de pesca | 5 – 500 |
| Fertilizante | +1 qualidade nas colheitas | Guano (drop) ou Hana | 30 |
| Comida de Animais | felicidade dos animais (+10) | Zed | 20 |

---

## 5. Comida (cozinha)

- Cozinha-se no **fogão** (Estalagem, tua casa, povoações com cozinha) ou **na fogueira** (só pratos simples, marcados com 🔥).
- Cada prato **cura** um pouco e dá **um bónus de comida** (5 min). Só um bónus de comida de cada vez.
- A **qualidade** dos ingredientes melhora o prato (Boa ×1,1, Excelente ×1,2).

### Ingredientes básicos (Mercado e Hana)
Farinha (do Trigo), Ovo, Leite, Manteiga (do Leite), Queijo (do Leite), Açúcar, Sal, Arroz, Óleo, Batata, Cenoura, Cebola, Tomate, Água Limpa.

### Receitas
| Prato | Ingredientes | Cura | Bónus | Onde se aprende |
|---|---|---|---|---|
| Truta Grelhada 🔥 | 1 Truta do Ribeiro + 1 Sal | 20% | +5% DEF | R1_03 |
| Espetada de Coelho 🔥 | 2 Carne de Coelho | 20% | +5% ATQ | início |
| Sopa de Legumes | 3 legumes + 1 Água Limpa | 25% | +10% regeneração de HP | N_MARTA_1 |
| Sopa de Cogumelos | 3 Cogumelo Luminoso + 1 Leite | 20% | +20% regeneração de MP | Livro de Receitas: Sopas (andar 4) |
| Panquecas de Mel Azul | 1 Farinha + 1 Ovo + 2 Mel Azul | 30% | +10% velocidade | R1_05 |
| Torta de Maçã Selvagem | 3 Maçã Selvagem + 1 Farinha + 1 Manteiga | 30% | +10% Estamina máx. | Dona Marta (2 ❤️) |
| Morangos com Natas | 3 Morango Silvestre + 1 Leite | 15% | +5% crítico | Folhalta |
| Assado de Javali | 2 Carne de Javali + 1 Cebola + 1 Batata | 40% | +10% ATQ | Brom (4 ❤️) |
| Sopa de Mineiro | 5 Carne + 5 Raiz-Pedra + 1 Cogumelo Luminoso | 35% | +20% DEF | R2_14 |
| Ramen de Fungo | 1 Farinha + 2 Fungo Azul + 1 Ovo | 30% | +10% ATQ e +10% MP | Kai (N_KAI_2) |
| Hambúrguer de Javali | 1 Carne de Javali + 1 Farinha + 1 Queijo + 1 Tomate | 40% | +10% ATQ e +5% velocidade | Kai (N_KAI_2) |
| Batatas Roxas Assadas 🔥 | 3 Batata Roxa da Gruta | 25% | luz de 3 m | Hilda |
| Pão de Fungo | 1 Farinha + 2 Fungo Azul | 20% | +10% RES | Mestre Lamela |
| Café Forte | 2 Café da Selva + 1 Açúcar | 10% | +10% velocidade de ataque | R3_13 |
| Chocolate Quente | 2 Cacau + 1 Leite + 1 Açúcar | 20% | +20 Temperatura; +10% regeneração | R3_14 |
| Banana Frita 🔥 | 2 Banana + 1 Óleo | 15% | +20% regeneração de Estamina | Refúgio das Copas |
| Caril da Selva | 1 Carne + 2 Pimenta da Selva + 1 Arroz | 35% | +15% ATQ | Zith |
| Espetada de Crocodilo 🔥 | 2 Carne de Crocodilo | 30% | +10% DEF | Kesh |
| Moscas Fritas | (só se compra na Vila Coaxa) | 5% | +5% velocidade | loja da Vila Coaxa |
| Tâmaras com Mel | 3 Tâmaras + 1 Mel | 15% | +20% Estamina | Zahra |
| Cuscuz do Oásis | 1 Farinha + 1 Carne + 1 legume + 1 Açafrão | 35% | +15% regeneração de HP | Zahra |
| Sumo de Cacto | 2 Cacto-Água | 10% | imune ao sol do deserto 5 min | início da região 4 |
| Pão de Açafrão | 1 Farinha + 1 Açafrão + 1 Ovo | 25% | +5% drops raros | Nómadas do Vento |
| Chá Quente | 2 Bagas de Inverno + 1 Água Limpa | 10% | +40 Temperatura; +10% regeneração | R5_13 |
| Sopa de Couve do Norte | 2 Couve do Norte + 1 Batata + 1 Carne | 35% | +15% HP máx. | Pinhal-do-Norte |
| Bacalhau no Forno | 1 Bacalhau Ártico + 2 Batata + 1 Óleo | 40% | +15% DEF | Ulf |
| Bolo de Bagas | 3 Bagas de Inverno + 1 Farinha + 1 Ovo + 1 Açúcar | 25% | +15% MP máx. | Astrid |
| Sushi do Recife | 1 peixe do mar + 1 Arroz + 1 Alga Doce | 25% | +30% de Ar | Vila das Pérolas |
| Caldeirada do Porto | 3 peixes do mar + 1 Tomate + 1 Batata | 50% | +10% RES | Rosa (Porto) |
| Arroz de Marisco | 1 Carne de Caranguejo + 1 Arroz + 1 Tomate | 40% | +10% ATQ e +10% DEF | Coralina |
| Ananás Grelhado 🔥 | 1 Ananás da Ilha | 15% | +10% velocidade | Rosa |
| Ovos de Géiser | 3 ovos de Sapo-Vulcão | 20% | o Calor sobe metade | R7_08 |
| Pimentos Picantes Recheados | 2 Pimenta-Lava + 1 Carne + 1 Arroz | 35% | +20% ATQ (e a boca arde) | Fumarola |
| Batata Vulcânica Assada 🔥 | 2 Batata Vulcânica | 25% | +20 Temperatura / −20 Calor (equilibra) | Fumarola |
| Pão Fantasma | 5 Farinha + 3 Ectoplasma | 15% | atravessas paredes finas 10 s | R8_04 |
| Sopa de Abóbora | 1 Abóbora + 1 Leite + 1 Cebola | 35% | +15% RES | Noite dos Espíritos |
| Tarte Celeste | 3 Pêssego Celeste + 1 Farinha + 1 Manteiga | 40% | **+5% XP durante 1 dia** | R9_09 |
| Sumo de Uva Celeste | 3 Uva Celeste | 15% | +20% regeneração de MP | Brisa (Aerópolis) |
| Guisado das Estrelas | 1 Lótus Estelar + 2 Carne + 2 legumes | 50% | +5% a tudo | Dorn |
| **Guisado da Mãe** | receita secreta | 100% | +10% a tudo durante 1 dia | Dona Marta (10 ❤️) |

Há mais receitas para descobrir: cozinhar **qualquer combinação nova** de 2–4 ingredientes tem 30% de hipótese
de inventar um prato simples (cura 15% e um bónus pequeno ao acaso).

---

## 6. Materiais (resumo por região)

| Região | Lingote / barra | Madeira | Couro | Fio | Cristal | Gema | Ervas e outros |
|---|---|---|---|---|---|---|---|
| 1 Floresta | Lingote de Cobre | Carvalho | Couro de Javali | Linho Bravo | Seiva Cristalizada | Rubi pequeno | Erva Verde, Flor de Mel, Cogumelo Luminoso, Mel Azul, Pó de Fada |
| 2 Cavernas | Lingote de Ferro (+ Carvão) | Escora Velha, Fungo-Lenho | Couro de Toupeira | Seda de Aranha | Cristal de Gruta | Topázio, Rubi, Ametista | Musgo Luminoso, Raiz-Pedra, Engrenagem, Guano |
| 3 Pântano | Lingote de Aço | Mangue | Pele de Crocodilo | Fibra de Liana | Âmbar do Pântano | Esmeralda | Lírio do Pântano, Musgo Medicinal, Banana, Cacau, Café, Coco |
| 4 Deserto | Lingote de Prata | Acácia | Couro de Chacal | Ligadura Antiga | Vidro Solar | — | Sal, Cacto-Água, Flor do Deserto, Tâmaras, Açafrão, Pérola do Deserto |
| 5 Gelo | Barra de Gelo Eterno | Pinheiro Nevado | Pele de Urso Polar | Lã de Mamute | Lágrima de Aurora | Safira | Flor-de-Neve, Musgo Ártico, Bagas de Inverno, Marfim |
| 6 Oceano | Barra de Coral Abissal | Madeira de Naufrágio | Pele de Tubarão | Fio de Alga-Prata | Pérola | Pérola Negra | Sal Marinho, Alga Doce, Anémona, Concha Rara, Gel Elétrico |
| 7 Vulcão | Barra de Obsidiana (+ Brasa de Lava) | Lenho-Brasa | Couro de Salamandra | Seda Ignífuga | Cristal de Magma | Rubi | Pimenta-Lava, Flor de Cinza, Enxofre, Núcleo de Magma |
| 8 Reino | Lingote de Mitril (+ Água Benta) | Ébano Morto | Asa de Gárgula | Fio Espectral | Lágrima de Fantasma | Ónix, Diamante | Rosa Negra, Sálvia Sagrada, Lírio da Lua, Ectoplasma, Página Antiga |
| 9 Céu | Lingote de Oricalco (+ Pedra-Sol) | Madeira-Nuvem | Pele de Pássaro-Trovão | Fio de Nuvem | Cristal Celeste | Topázio, Diamante | Pêssego Celeste, Flor-do-Vento, Pena Celeste, Estrela Cadente |
| 10 Abismo | Lingote Estelar (+ Núcleo do Vazio) | Madeira do Tempo | Pele do Vazio | Fio de Luz Estelar | Núcleo do Vazio | Gema Prismática | Lótus Estelar, Areia do Tempo, Fragmento de Sistema, Fragmento de Eco |

**Lingotes**: 3 minérios + 1 combustível na forja (Carvalho na região 1, Carvão nas regiões 2–6, Brasa de Lava na 7,
Água Benta purifica o Mitril na 8, Pedra-Sol na 9, Núcleo do Vazio na 10).

Os **drops dos monstros** (Gel de Slime, Presa de Lobo, Ferrão de Escorpião…) estão em cada monstro, nas regiões.
Servem para receitas, missões, presentes e para vender.

---

## 7. Plantas (todas)

| Planta | Região | Dias | Estação | Dá sempre? | Usos |
|---|---|---|---|---|---|
| Trigo | básica (Hana) | 4 | Primavera, Verão, Outono | não | Farinha |
| Nabo Bravo | 1 | 4 | Primavera | não | cozinha |
| Batata | básica | 6 | Primavera, Outono | não | cozinha |
| Cenoura | básica | 5 | Primavera, Outono | não | cozinha |
| Tomate | básica | 7 | Verão | sim | cozinha |
| Cebola | básica | 5 | todas menos Inverno | não | cozinha |
| Morango Silvestre | 1 | 6 | Primavera, Verão | sim | cozinha, presentes |
| Batata da Pradaria | 1 | 6 | Primavera, Outono | não | cozinha |
| Flor de Mel | 1 | 5 | Primavera, Verão | não | doces, poções |
| Árvore Dourada | 1 | 28 | todas | sim (1/semana) | Maçã Dourada |
| Fungo Azul | 2 | 3 | todas (à sombra) | sim | cozinha, luz |
| Raiz-Pedra | 2 | 7 | Outono, Inverno | não | Poção de Defesa |
| Batata Roxa da Gruta | 2 | 5 | todas (à sombra) | não | cozinha |
| Cacau | 3 | 10 | Verão, Outono | sim | chocolate |
| Café da Selva | 3 | 8 | Verão | sim | café |
| Bananeira | 3 | 14 | Verão | sim | cozinha |
| Pimenta da Selva | 3 | 6 | Verão | não | picante |
| Lírio do Pântano | 3 | 5 (junto à água) | Primavera, Verão | não | poções |
| Semente Carnívora | 3 | 10 | todas | — | guarda da quinta |
| Tamareira | 4 | 21 | Verão | sim | doces |
| Cacto-Água | 4 | 6 | todas | sim | bebida |
| Melão do Deserto | 4 | 8 | Verão | não | cozinha |
| Açafrão | 4 | 10 | Outono | não | especiaria cara |
| Flor do Deserto | 4 | 7 | Verão | não | presentes |
| Bagas de Inverno | 5 | 8 | Outono, Inverno | sim | chá |
| Couve do Norte | 5 | 6 | Inverno | não | sopas |
| Flor-de-Neve | 5 | 7 | Inverno | não | poções |
| Musgo Ártico | 5 | 5 | Inverno (sombra) | não | poções |
| Alga Doce | 6 | 4 (lago) | todas | sim | cozinha |
| Ananás da Ilha | 6 | 12 | Verão | não | cozinha |
| Batata-Doce da Ilha | 6 | 6 | Verão, Outono | não | cozinha |
| Pimenta-Lava | 7 | 7 | Verão | não | cozinha |
| Flor de Cinza | 7 | 6 | todas | não | poções |
| Lenho-Brasa | 7 | 21 | todas | sim | madeira |
| Batata Vulcânica | 7 | 6 | Verão, Outono | não | cozinha |
| Rosa Negra | 8 | 8 | Outono | não | presentes, poções |
| Sálvia Sagrada | 8 | 6 | Primavera, Verão | sim | Água Benta |
| Abóbora | básica | 10 | Outono | não | cozinha, lanternas |
| Lírio da Lua | 8 | 7 | todas | não | poções de MP |
| Pessegueiro Celeste | 9 | 21 | Primavera, Verão | sim | tarte |
| Algodão-Nuvem | 9 | 8 | Verão | não | Fio de Nuvem |
| Flor-do-Vento | 9 | 6 | Primavera | não | Poção de Leveza |
| Uva Celeste | 9 | 10 | Outono | sim | sumo |
| Lótus Estelar | 10 | 10 (lago) | todas | não | elixir |
| Flor do Tempo | 10 | 4 | todas | não | presentes, poções |
| Semente do Mundo | 10 | 7 | todas | não | colheita ao acaso |
| Árvore Estelar | 10 | 28 | todas | sim (1/semana) | Fragmento Estelar |

---

## 8. Animais da quinta (Zed)

| Animal | Preço | Dá | Precisa |
|---|---|---|---|
| Galinha | 800 | 1 Ovo por dia | galinheiro, comida |
| Vaca | 2 500 | 1 Leite por dia (Leite → Queijo, Manteiga na cozinha) | estábulo |
| Cabra | 2 000 | 1 Leite de Cabra a cada 2 dias | estábulo |
| Ovelha | 2 200 | Lã a cada 3 dias (fio comum) | estábulo |
| Abelhas | 1 000 | Mel a cada 4 dias (Mel Azul se houver Flores de Mel perto) | colmeia (carpintaria) |

Animais felizes (carinho e comida todos os dias) dão produtos de melhor qualidade.

---

## 9. Peixes

**60 peixes** (6 por região, incluindo 1 lendário por região) — estão na secção 10 de cada ficheiro de região.
Também se pesca **lixo**: Bota Velha, Lata, Alga Seca (dá para reciclar no Gizmo em peças).
O minijogo de pesca está em `docs/ATIVIDADES.md`.

---

## 10. Móveis e decoração

Cerca de **200 peças** para a casa:

| Grupo | Quantidade | Como |
|---|---|---|
| Básicos (cama, mesa, cadeiras, tapetes, candeeiros, estantes) | ~30 | Tobias, Mercado |
| **Estilo de cada região** (10 por região: ex. cadeira de cogumelo, tapete do deserto, lareira de gelo, cama de coral, candeeiro de lava, órgão pequeno, nuvem-sofá, relógio estelar) | 100 | carpintaria (madeira e materiais da região) |
| Troféus dos bosses e dos monstros com nome | 40 | 1.ª vitória |
| Decorações de missões (Remo Dourado, Pinturas de Cinza, Esculturas de Nuvem, Espelho Mágico, Telescópio…) | ~25 | missões |
| Festivais (lanternas, coroas de flores, fogo de artifício de parede) | ~20 | festivais |
| Coleções (parede de armas, aquário, museu) | — | automáticos |

---

## 11. Presentes

Cada NPC tem a sua lista (ver `docs/NPCS.md`). Há também presentes **universais**:

| Tipo | Itens |
|---|---|
| Todos **adoram** | Pérola Azul (andar 16), Rosa de Sangue, Estrela Cadente, Maçã Dourada |
| Todos **gostam** | qualquer prato de qualidade Excelente, flores de festival |
| Todos **detestam** | lixo de pesca (Bota Velha, Lata), Gel de Slime (quase todos), Ectoplasma |
