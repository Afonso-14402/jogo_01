# Lojas

Tudo o que se pode **comprar** no jogo, a quem, a que preço e quando aparece. Os preços vêm de `docs/ITENS.md`,
`docs/ARMAS.md` e `docs/EQUIPAMENTO.md`; as regras da economia estão em `docs/SISTEMAS.md`, secção 10.
O que cada lojista **diz** está em `docs/dialogos/`.

---

## 1. Regras de todas as lojas

| Regra | Valor |
|---|---|
| Horário | cada loja abre no horário do seu dono (ver cada loja). Fora do horário a porta está fechada (`[Sistema] Está fechado. Abre às {hora}.`) |
| Stock | renova-se **todos os dias às 6:00**. Itens marcados com ∞ nunca acabam; os outros têm a quantidade indicada |
| Itens raros | os do Tobias mudam **de 3 em 3 dias**; os do Mercador Errante, cada vez que a Cidade Errante muda de andar |
| Vender | todas as lojas compram tudo a **30%** do preço (o Rook paga 40% por itens "duvidosos", ver secção 2.15) |
| Descontos de amizade | **5%** com 2 corações, **15%** com 8 corações (só com o dono da loja) |
| Preços que mudam | os preços dos itens de região baixam 20% quando vences o boss dessa região ("há mais gente a trazer isso") |
| Moedas especiais | **Lágrima de Fantasma** (Mercado Fantasma, região 8) · **cogumelos** como moeda (Mycélia, região 2) |
| Arte | cada loja abre a mesma janela de loja (ver `docs/INTERFACE.md`), com o retrato do dono e a sua frase de boas-vindas |

### Preços que se usam em várias lojas

| Coisa | Preço |
|---|---|
| Arma normal (Comum) | o preço da tabela de `docs/ARMAS.md` (≈ `150 × tier^2,2 × fator do tipo`) |
| Peça de armadura (Comum) | o preço da tabela de `docs/EQUIPAMENTO.md` (≈ 60% de uma arma do mesmo tier) |
| Ferramenta (Picareta ou Machado de lenhador) | 60% da espada do mesmo tier: **90** (Cobre) · 410 · 1 010 · 1 900 · 3 100 · 4 640 · 6 510 · 8 730 · 11 310 · **14 260** (Estelar) |
| Material básico do tier N (minério, madeira, couro, fio) | `8 × N²`: **8** (tier 1) · 32 · 72 · 128 · 200 · 288 · 392 · 512 · 648 · **800** (tier 10) |
| Lingote do tier N | `30 × N²`: 30 · 120 · 270 · 480 · 750 · 1 080 · 1 470 · 1 920 · 2 430 · 3 000 |
| Cristal da região N (para melhorias +6 a +10) | `100 × N²`: 100 · 400 · 900 · … · 10 000 (só em lojas especiais e raros) |
| Gema Lascada / Normal / Perfeita / Brilhante | 300 / 1 000 / 3 500 / 12 000 (Normal ou melhor só nos raros e no Mercador Errante) |
| Semente | 10 a 40 (básicas) · 30 + 10 × região (sementes das regiões) · árvores ×10 |

---

## 2. Lojas de Ascendia

### 2.1 Tobias — Loja Geral (Mercado)

| | |
|---|---|
| Horário | 7:00–19:00, todos os dias |
| Regatear | carrega em **Regatear** antes de comprar: hipótese de **40% + 5% por coração** de baixar 10%. Se falhar, esse item fica 5% mais caro até amanhã. **Mais de 3 vezes no mesmo dia: −30 amizade** (e ele diz que estás a "abusar da generosidade dele") |
| Compra | tudo (30%) |

**Sempre à venda (∞)**

| Item | Preço | A partir de |
|---|---|---|
| Poção de Vida P | 30 | início |
| Poção de Mana P | 40 | início |
| Antídoto | 25 | início |
| Ligadura | 20 | início |
| Colírio | 25 | início |
| Tocha | 10 | início |
| Pedra de Regresso | 50 | início |
| Isco | 5 | andar 3 |
| Poção de Vida M | 150 | região 3 |
| Poção de Vida G | 600 | região 5 |
| Farinha · Ovo · Leite · Açúcar · Sal · Arroz · Óleo | 10 · 8 · 12 · 10 · 5 · 10 · 15 | início |
| Manteiga · Queijo | 20 · 25 | início |
| Móveis básicos (cama simples, mesa, 2 cadeiras, tapete, candeeiro, estante) | 100 a 600 | casa (andar 20) |

**Do dia** (4 itens ao acaso, ×5 cada, só de regiões a que já chegaste): materiais básicos e lingotes de qualquer
região desbloqueada, Erva Verde, Flor de Mel, Cogumelo Luminoso, Pó de Fada, Cera, Mel Azul, Sal (×20), Pólvora (região 2+),
Pano Velho, Água Benta (região 8+), Poção de Luz (região 2+), Poção Purificadora (região 3+), Cantil (região 4+),
Pedra Quente (região 5+), Poção de Respirar (região 6+, mais cara do que na Selene).

**Raros** (3 itens, mudam de 3 em 3 dias; +4 com a melhoria **Mercado Coberto**):

| Grupo | Exemplos | Preço |
|---|---|---|
| Chaves | Chave de Baú de Ouro (rank D+) | 500 |
| Gemas | Rubi/Topázio/… Lascado (das regiões já visitadas) | 300 |
| Sementes raras | Árvore Dourada, Bananeira, Tamareira, Pessegueiro Celeste… | 300 a 1 500 |
| Iscos | Isco Bom (50) · Isco Dourado (200) | — |
| Arma Rara | uma arma normal do tier mais alto desbloqueado, raridade **Rara** | preço da tabela × 3 |
| Receita de cozinha | uma receita de uma povoação já visitada | 300 |
| Móvel raro | uma peça de estilo de uma região já visitada | 800 a 3 000 |
| Curiosidade do mundo real | "Telemóvel Partido", "Bola de Ténis", "Óculos de Sol" (decoração; o Kai adora recebê-las de presente) | 1 000 |

Depois de **N_TOBIAS_3** (os irmãos fazem as pazes): tudo 5% mais barato aqui e no Tibério.
Com **10 ❤️**: **Chave do Armazém** → loja secreta (secção 2.1.1).

#### 2.1.1 Armazém secreto do Tobias (10 ❤️)

| Item | Preço |
|---|---|
| 1 arma **Lendária** ao acaso do tier mais alto desbloqueado (muda a cada semana) | tabela × 8 |
| Gema Perfeita ao acaso | 3 500 |
| Elixir Estelar (depois do andar 91) | 5 000 |
| Pena de Fénix (1 por estação) | 15 000 |
| Móvel Dourado (decoração) | 20 000 |
| Mapa do Tesouro (1 por semana) | 1 000 |

### 2.2 Brom — Forja (Bairro dos Artesãos)

| | |
|---|---|
| Horário | 6:00–19:00 (fechada no dia do aniversário dele: "Hoje não se trabalha. Hoje bebe-se.") |
| Compra | armas, armaduras, minérios, lingotes, gemas |

**À venda**

| Item | Preço | A partir de |
|---|---|---|
| As 12 armas **Comuns** de cada tier já desbloqueado | tabela de `docs/ARMAS.md` | tier 1 no início; tier N quando chegas à região N |
| As 5 peças do conjunto de armadura de cada tier desbloqueado | tabela de `docs/EQUIPAMENTO.md` | idem |
| Picareta e Machado de lenhador do tier desbloqueado | ver secção 1 | idem |
| Lingotes do tier desbloqueado (×10 por dia) | `30 × N²` | idem |

**Serviços**

| Serviço | Custo |
|---|---|
| **Forjar** (com a receita e os materiais) | 20% do preço da peça em ouro |
| **Fundir** minério em lingote | 3 minérios + 1 Carvalho + 5 ouro × tier |
| **Melhorar** +1 a +10 | ver `docs/SISTEMAS.md`, secção 11.3 (10% do preço × nível + lingotes, cristais e gemas) |
| **Encantar** (encaixar gema) | 50 ouro (Lascada) · 200 (Normal) · 800 (Perfeita) · 3 000 (Brilhante) |
| **Tirar gema** (a gema não se perde) | 100 |
| **Reciclar** (desfazer) | grátis: devolve 50% dos materiais |

Com o **Pedrito** como aprendiz (R2_13): melhorias +1 a +5 20% mais baratas.

### 2.3 Selene — Alquimia (Bairro dos Artesãos)

| | |
|---|---|
| Horário | 9:00–18:00 (às vezes fecha 1 hora "por causa de uma pequena explosão": 5% por dia) |
| Compra | ervas, flores, cogumelos, pós, drops de monstros |

| Item | Preço | A partir de |
|---|---|---|
| Poção de Vida P / M / G / Máxima | 30 / 150 / 600 / 2 500 | início / região 3 / região 5 / região 10 |
| Poção de Mana P / M / G | 40 / 180 / 700 | início / região 5 / região 8 |
| Poção de Estamina | 50 | início |
| Antídoto · Ligadura · Colírio | 25 · 20 · 25 | início |
| Poção de Força · Poção de Velocidade | 90 · 80 | região 1 (depois do andar 5) |
| Poção de Luz · Poção de Visão Noturna · Poção de Defesa | 60 · 70 · 80 | região 2 |
| Poção Purificadora · Poção de Regeneração | 90 · 200 | região 3 |
| Poção Quente | 120 | região 5 |
| Poção de Respirar | 300 (mais cara do que fazê-la) | região 6 |
| Poção Fresca · Poção Ignífuga | 150 · 400 | região 7 |
| Poção das Sombras | 350 | região 8 |
| Poção de Leveza | 250 | região 9 |
| Poção do Tempo | 900 | região 10 |
| Bomba · Bomba de Gelo · Bomba de Luz · Bomba Elétrica | 60 · 120 · 150 · 150 | região 2 / 5 / 8 / 9 |
| **Receitas de alquimia** (aprende-se a fazer) | 200 a 2 000 (o preço de 10 poções) | quando a poção fica à venda |

Com a **Tina** como ajudante (R1_13): todas as poções 10% mais baratas.

### 2.4 Dona Marta — Estalagem "Ninho do Viajante" (Mercado)

| | |
|---|---|
| Horário | 5:00–23:00 (o quarto está sempre aberto) |
| Compra | ingredientes e comida |

| Coisa | Preço |
|---|---|
| **Quarto** (dormir e gravar) | grátis na 1.ª semana; depois 20 por noite (ou ajudar nas compras: missão diária "Lista da Marta"); grátis com **8 ❤️** |
| **Refeição do dia** (cura tudo, dá o bónus do prato) | 40 (pequeno-almoço 6:00–10:00) · 60 (almoço 12:00–15:00) · 80 (jantar 19:00–22:00) |
| Prato do dia para levar | 1,5 × a refeição |
| Receitas de cozinha que ela ensina | grátis com missões e corações; algumas à venda (300) |

**Ementa da semana** (o prato do jantar; o almoço é sempre Sopa de Legumes e o pequeno-almoço Panquecas):

| Segunda | Terça | Quarta | Quinta | Sexta | Sábado | Domingo |
|---|---|---|---|---|---|---|
| Espetada de Coelho | Sopa de Cogumelos | Truta Grelhada | Assado de Javali | Caldeirada do Porto (depois da região 6) ou Torta de Maçã | Prato de uma região ao acaso | **Assado de Domingo** (cura 50%, +10% a tudo 5 min) |

### 2.5 Pip — Canas e Iscos (Rio e Porto / banca no Mercado à tarde)

| | |
|---|---|
| Horário | Rio 6:00–12:00 · Mercado 13:00–18:00 (vende peixe fresco) |
| Compra | peixe (paga +10% pelo peixe) e lixo de pesca (1 ouro, "para a coleção") |

| Item | Preço | A partir de |
|---|---|---|
| Cana de Bambu | 100 (grátis na R1_03) | andar 3 |
| Cana de Mangue | 1 200 | região 3 |
| Cana de Prata | 4 000 | região 4 |
| Cana de Coral | 9 000 | região 6 |
| Isco · Isco Bom | 5 · 50 | andar 3 · região 2 |
| Isco Dourado | 200 (×3 por dia) | região 3 |
| Isco de Areia | 30 | região 4 |
| Isco Ignífugo | 150 | região 7 |
| Isco Lendário | — (só no Festival da Pesca e no Mercador Errante) | — |
| Peixe do dia (3 peixes ao acaso já pescados por ti) | preço do peixe × 1,5 | — |

### 2.6 Mia — Flores (esquina do Bairro Baixo)

| | |
|---|---|
| Horário | 9:00–17:00 (não está quando chove: "As flores não gostam de ficar molhadas. Eu também não.") |
| Compra | flores (paga 50%, mais do que os outros: "Para o meu cesto!") |

| Item | Preço |
|---|---|
| Ramo Simples (presente "gosta" para quem gosta de flores) | 30 |
| Flor da estação (Primavera: Margarida · Verão: Girassol · Outono: Crisântemo · Inverno: Campainha-de-Neve) | 20 |
| Flor de Mel | 25 (depois do andar 6) |
| Coroa de Flores (só na Festa das Flores) | 150 |

### 2.7 Hana — Sementes e quinta (Quinta / Mercado ao fim da tarde)

| | |
|---|---|
| Horário | Quinta 6:00–17:00 · Mercado 17:00–19:00 |
| Compra | legumes, frutas, flores, produtos dos animais (paga +10% pela qualidade Excelente) |

| Item | Preço | A partir de |
|---|---|---|
| Sementes básicas: Trigo · Batata · Cenoura · Cebola · Tomate · Abóbora | 10 · 15 · 15 · 15 · 25 · 40 | início (cada uma na sua estação) |
| Legumes: Batata · Cenoura · Cebola · Tomate | 8 · 8 · 8 · 10 | início |
| Sementes da região N (as plantas de `docs/ITENS.md`, secção 7) | 30 + 10 × N | depois de chegar à região N |
| Sementes de árvores (Árvore Dourada, Tamareira, Pessegueiro Celeste, Lenho-Brasa, Árvore Estelar) | 300 a 3 000 | região da árvore |
| Fertilizante | 30 | andar 10 |
| Regador de Cobre / de Ouro | 500 / 5 000 | N_HANA_1 / região 5 |
| Espantalho | 300 | andar 10 |
| Alargar o terreno (+2×2 talhões) | 1 000 × (vezes já alargado + 1), até 20×20 | andar 10 |
| Estufa | 20 000 + 50 Vidro Solar | região 4 |

### 2.8 Zed — Rancho (Quintas)

| | |
|---|---|
| Horário | sempre (às vezes ausente: "Fui buscar um animal ferido. Volto amanhã." 1 dia por semana) |
| Compra | ovos de animais, comida de animais |

| Item | Preço | A partir de |
|---|---|---|
| Galinha · Abelhas · Cabra · Ovelha · Vaca | 800 · 1 000 · 2 000 · 2 200 · 2 500 | andar 10 (precisam de galinheiro, colmeia ou estábulo) |
| Galinheiro · Estábulo · Colmeia | 1 500 · 4 000 · 600 | andar 10 |
| Comida de Animais | 20 | início |
| Escova, brinquedos (felicidade +5 por dia) | 50 a 200 | primeiro animal |
| **Chocar ovos** de animais de estimação | 200 + 1 dia | primeiro ovo |
| Montadas (ver `docs/ATIVIDADES.md`) | 5 000 a 50 000 | andar 40 |
| Sela, rédeas e enfeites | 300 a 3 000 | andar 40 |

### 2.9 Elva — Costura (Bairro dos Artesãos)

| | |
|---|---|
| Horário | 9:00–19:00 |
| Compra | fios, couros, tecidos, penas |

| Item | Preço | A partir de |
|---|---|---|
| Mochila de Couro (40) | grátis com N_ELVA_1 | andar 2 |
| Mochila de Viajante (50) | 3 000 | andar 30 |
| Mochila de Aventureiro (60) | 12 000 | andar 50 |
| Mochila Lendária (80) | 50 000 | andar 80 |
| Vestes de Aprendiz / Feiticeiro / Sábio (por peça) | preço da armadura do tier × 1,2 | andar 25 / 55 / 85 |
| **Cores do herói** (tingir roupa e cabelo) | 200 por mudança | início |
| Roupas cosméticas (aparência por cima do equipamento) | 500 a 5 000 (cada região desbloqueia 2) | andar 5 |
| Tear (usar em casa) | 4 000 | casa |

### 2.10 Gizmo — Oficina (Bairro dos Artesãos)

| | |
|---|---|
| Horário | sempre (de madrugada ele está a dormir em cima da bancada: fala a ressonar, 2:00–6:00) |
| Compra | lixo de pesca e peças (Bota Velha, Lata, Alga Seca, Engrenagens) |

| Item | Preço | A partir de |
|---|---|---|
| Lanterna de Mão (luz de 6 m, sem tempo) | 1 500 | região 2 |
| Detetor de Tesouros (apita perto de segredos) | 5 000 | região 3 |
| Bússola de Bolso (mostra a escada no minimapa) | 2 000 | região 2 |
| Bombas (iguais às da Selene, +10%) | — | região 2 |
| Mesa de joalharia (usar na oficina; em casa custa 6 000) | grátis aqui | região 2 |
| Joalharia: fazer anéis e talismãs | 10% do valor das gemas | região 2 |
| Melhorias do barco (com o Tomé, região 6) | 2 000 a 20 000 | região 6 |
| **Reciclar lixo** em peças | 3 lixos → 1 Engrenagem | sempre |

### 2.11 Irmã Célia — Igreja da Luz (Bairro Alto)

| | |
|---|---|
| Horário | 6:00–20:00 |
| Compra | nada (a Igreja não compra; aceita **donativos**: 100 ouro = +5 amizade, máx. 1 por dia) |

| Serviço | Preço |
|---|---|
| Água Benta | 60 (mais barata com a melhoria Catedral: 40) |
| Tirar uma Maldição | 100 |
| Curar todos os estados | 50 |
| **Bênção** (1 de cada vez, dura até ao próximo boss ou 1 dia): Bênção da Força (+10% ATQ) · da Proteção (+10% DEF) · da Sorte (+10% drops) · da Luz (+20% contra mortos-vivos) | 300 · 300 · 500 · 400 |
| **Redistribuir atributos** (devolve todos os pontos) | 5 000 × nível / 10 (a 1.ª vez é grátis) |
| Vela Sagrada (depois de N_CELIA_1) | 40 |

### 2.12 Velho Fausto — Biblioteca (Bairro Alto)

| | |
|---|---|
| Horário | 8:00–22:00 |
| Compra | livros e páginas encontradas (paga bem: 200 por livro novo para a coleção) |

| Serviço / item | Preço |
|---|---|
| **Bestiário** (completa a página de um monstro: fraquezas e drops) | 50 por monstro já derrotado (grátis com a skill Olho do Sistema) |
| Traduzir textos antigos (missões) | grátis |
| Mapas antigos (mostram os segredos de um andar já visitado) | 300 × região |
| Livros de receitas (1 por região: cozinha ou alquimia) | 800 |
| Cartão da Biblioteca (ler livros: pequenas histórias do mundo) | grátis |

### 2.13 Madame Oriel — Tenda da Vidente (Bairro Alto)

| | |
|---|---|
| Horário | 14:00–2:00 |
| Compra | nada |

| Serviço | Preço |
|---|---|
| **Carta da sorte do dia** (um bónus pequeno até dormir: +5% de drops, ouro, XP, crítico ou amizade, ao acaso) | 50 |
| **Profecia** (dica sobre um segredo, um puzzle ou uma página que te falta no andar mais alto) | 200 × região |
| Onde está a **Cidade Errante** | 20 |
| Onde aparece um **monstro com nome** esta semana | 500 |
| Dica sobre um **lendário** (peixe, arma ou monstro) | 1 000 (só com a melhoria Observatório) |

### 2.14 Taberna "O Primeiro Degrau" (Lucien e o taberneiro)

| | |
|---|---|
| Horário | 16:00–2:00 |
| Compra | bebidas e comida |

| Item | Preço |
|---|---|
| Sumo de Maçã · Leite Quente · Chá | 10 · 10 · 15 |
| Sopa do Dia · Pão com Queijo · Espetada | 25 · 15 · 30 |
| **Rumor do Lucien** (dica de um segredo ou missão) | 30 (1 por dia) |
| **Pedir uma canção** (sobre um feito teu: +10 amizade com todos os que estão na taberna) | 50 |
| Minijogos: cartas, dados, braço de ferro (ver `docs/ATIVIDADES.md`) | apostas de 10 a 1 000 (depois do andar 30) |

### 2.15 Rook — Mercado Negro (Bairro Baixo, telhados à noite)

| | |
|---|---|
| Horário | 22:00–4:00, só a partir do **rank C** |
| Compra | tudo a 30%; itens **"duvidosos"** a **40%** (itens de missão que já não servem, troféus repetidos, armas de guardião repetidas) |

| Item | Preço |
|---|---|
| Chave de Baú de Ouro | 400 (mais barata do que no Tobias, mas 10% de ser falsa: "Sem devoluções.") |
| Mapa do Tesouro | 800 |
| **Informação**: onde está um baú de ouro escondido no andar mais alto | 300 |
| **Informação**: a solução de um puzzle | 500 |
| Gazua (abre 1 porta trancada sem chave, nas masmorras) | 250 |
| Bomba de Fumo | 100 |
| Item roubado do dia (algo de outra loja, 30% mais barato — se a Freya souber, −amizade com ela) | — |

### 2.16 Outros sítios de Ascendia

| Quem | O quê | Preço |
|---|---|---|
| **Lyra** (Guilda) | registo, rank, missões; inscrição em eventos da Guilda | grátis / 50 |
| **Capitã Freya** (Arena) | inscrição na Arena: Bronze · Prata · Ouro · Platina | 50 · 200 · 1 000 · 5 000 |
| **Mestre Gorvan** | escolher classe (níveis 10, 40, 70) · treino (depois do andar 80) | grátis · 1 000 por sessão |
| **Governador Aldric** | melhorias da cidade (`docs/CIDADES.md`, secção 1.4) · casas maiores (secção 2.1) | ver lá |
| **Banca de mapas** (aventureiro congelado resgatado, andar 44) | mapa completo de um andar já visitado (mostra todo o terreno) | 100 × região |
| **Cristal Mestre** | teletransporte para qualquer andar já desbloqueado | grátis |

---

## 3. Lojas na torre

### 3.1 Tibério — Zonas Seguras

O irmão gémeo do Tobias. Aparece na Zona Segura de **1 em cada 3 andares** (sorteado ao entrar; sempre nos andares 1,
5, 10, 15, … e no Último Posto). Mais caro do que o irmão (+20%: "O transporte não é de graça!").

| Item | Preço |
|---|---|
| Poção de Vida (P/M/G conforme a região) | preço normal + 20% |
| Poção de Mana (conforme a região) | + 20% |
| Antídoto e o "anti-estado" da região (Poção de Luz na 2, Purificadora na 3, Cantil na 4, Pedra Quente na 5, Poção de Respirar na 6, Poção Fresca na 7, Água Benta na 8, Poção de Leveza na 9) | + 20% |
| Tocha · Pedra de Regresso | 12 · 60 |
| Comida simples (Pão com Queijo, Espetada) | 20 · 35 |
| 1 item raro do dia (como os do Tobias) | + 20% |

Depois de **N_TOBIAS_3**: −5% (os irmãos juntam as lojas) e passa a dizer "o meu irmão manda cumprimentos".

### 3.2 Região 1

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Bruno Machadão** | Acampamento dos Lenhadores (andar 2) | 6:00–20:00 | Machado de lenhador de Cobre (90) · Carvalho (8, ×30) · Espetada de Coelho (30) · Pão com Queijo (15) · Tocha (10) · Poção de Vida P (35) |
| **Mira Folha-de-Prata** | Folhalta (andar 7) | 8:00–20:00 | Arco Curto de Carvalho (tier 1, **Incomum**, 250) · Sementes de Morango Silvestre (40) · Sementes de Árvore Dourada (rara, 1 por semana, 600) · Poção Élfica (120) · Linho Fino (40) · Morangos com Natas (receita, 200) |
| **Faelan** | Folhalta (andar 7) | 8:00–18:00 | Treino de arco (+1 nível de Manejo de Arco por sessão, até 3): 300 · 600 · 1 200 · Flechas de enfeite (cosmético) 100 |
| **Fada Lumi** | Clareira Secreta das Fadas (andar 4, só à meia-noite; sempre aberta depois de R1_04) | 0:00–3:00 | Pó de Fada (20) · Pó de Fada Dourado (150) · Poção de Velocidade (70) · Asas de Fada (cosmético, R1_04) · "Folha com mel" (cura 15%, 10) · troca: 5 Mel Azul → 1 Pó de Fada Dourado |

### 3.3 Regiões 2 a 10

As lojas das povoações estão nos ficheiros das regiões (`docs/regioes/`, secção 7) e serão detalhadas como as da
região 1 quando cada região for escrita a fundo. Regra para todas:

| Tipo de loja | Vende |
|---|---|
| Loja de povoação | poções e comida da região, o material básico e o lingote do tier, 1 ou 2 itens únicos da povoação (receitas, sementes, cosméticos), o "anti-estado" da região |
| Forja de povoação (Posto Mineiro, Zahra, Bastião, Coralina, Mosteiro, Aerópolis, Último Posto) | armas e armaduras Comuns do tier da região; melhorias até +5 (as +6 a +10 só com o Brom ou nas forjas especiais) |
| Forjas especiais (Forja de Obsidiana, de Coral, de Mitril, de Oricalco, Estelar) | receitas únicas da região e melhorias até +10 com +5% de sucesso |

---

## 4. Vagar, a Cidade Errante

| Loja | Quem | À venda |
|---|---|---|
| **Itens de todo o lado** | Mercador Errante Ambrósio | 6 itens raros de **qualquer região, mesmo das que ainda não visitaste** (preço ×2): materiais, sementes, gemas Normais, Isco Lendário (1 000), receitas raras, 1 arma Épica (tabela × 6) |
| **Leilão** | Leiloeiro Gaspar | 3 itens raros por visita (troféus, móveis únicos, armas Lendárias, ovos de animais raros). Licitas contra 3 NPCs; o preço começa em metade do valor. Minijogo em `docs/ATIVIDADES.md` |
| **Trocas** | Troca-Tudo | troca 2 materiais de uma região por 1 de outra (qualquer uma já visitada) |
| **Moda** | Madame Plumas | cosméticos únicos: 4 por visita (chapéus, capas, cores raras do herói, roupa do animal de estimação), 1 000 a 10 000 |
| **Tartaruga** | a própria Vagar | 10 Alga Doce → leva-te ao andar mais alto desbloqueado |
