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
| Almofada (o Pip adora como presente) | 80 | início |

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
| **Voltar a sortear a Skill Única** (uma única vez, depois do andar 20) | 10 000 |

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

### 3.3 Região 2

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Hilda Fundo-Rocha** | Posto Mineiro (andar 11) | 5:00–21:00 | Tocha (10, ∞) · Giz de Mineiro (15) · Carvão (10, ×30) · Picareta de Ferro (410) · Lingote de Ferro (120, ×10) · Batata Roxa da Gruta (sementes, 50) · Poção de Luz (70) · forja simples: fundir minério (grátis com o teu carvão) |
| **Dona Graça** | Cantina do Posto (andar 11) | 6:00–20:00 | Sopa de Mineiro (60) · Pão com Queijo (15) · Batatas Roxas Assadas (30) |
| **Senhor Ruivo** | Posto Mineiro (andar 11) | 8:00–18:00 | Mapa dos Túneis (300, ou de graça com R2_03) · mapas dos andares 11–14 (100 cada) |
| **Pila** | Mycélia (andar 16) | sempre (os fungoides não dormem: descansam) | paga-se em **Cogumelos Luminosos** (1 = 5 ouro) ou ouro: Esporos de Fungo Azul (8 cogumelos) · Poção de Visão Noturna (14 cog.) · Poção de Luz (12 cog.) · Pão de Fungo (6 cog.) · Truta Fúngica (16 cog.) |
| **Mestre Lamela** | Mycélia (andar 16) | sempre | receitas com cogumelos: Pão de Fungo (40 cog.), Sopa de Cogumelos (30 cog.), Poção de Visão Noturna (60 cog.) |
| **Ferreiros Fantasmas** | Forja Anã (andar 18), só com as fornalhas acesas | sempre | Lingote Antigo (qualidade Boa, 180, ×5 por dia) · melhorias até +5 com +5% de sucesso · Rubi Lascado (300, 1 por semana) |

### 3.4 Região 3

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Zith** (só com `sssar_defendida`) | Aldeia Sssar (andar 24) | 6:00–20:00 | Água de Coco (25, ∞) · Pimenta da Selva (20) · Sementes de Café e de Pimenta (60) · Escama de Lagarto (72, ×10) · Lança Tribal de Aço (2 020) · Espetada de Crocodilo (45) · Caril da Selva (55) · na **Festa na Aldeia**: Escama do Primeiro Rei de imitação (cosmético, 800) e Totem Pequeno (móvel, 1 200) |
| **Xamã Ilssa** (só com `sssar_defendida`) | Aldeia Sssar (andar 24) | 7:00–19:00 | curar estados (50) · Antídoto (25) · Poção Purificadora (90) · Poção de Escamas (160, depois de R3_04) |
| **Barão Coaxim** | Vila Coaxa (andar 26) | 10:00–22:00 | **compra** tesouros a 100% do preço (não a 30%): Pele Dourada (800) · Dente de Mandíbula (1 500) · Âmbar com Mosquito (1 200) · Esmeralda Grande (2 000) · Ídolo de Jade (3 000, R3_07) · Pinça de Ouro (6 000, R6_12). Depois de R3_07, **itens raros** (mudam de 3 em 3 dias, 2 de cada vez): Gema Normal (1 000) · Mapa do Tesouro (500) · Ovo de Sapinho dourado (cosmético do Sapinho, 2 500) · Leque do Barão (acessório: +5% velocidade com calor, 3 000) |
| **Doutor Girino** | Vila Coaxa (andar 26) | 9:00–21:00 (fecha 1 dia depois de cada explosão: ver o letreiro) | Poção Surpresa (100, ∞) · Poção de Regeneração (200) · Poção Arco-Íris (1 200, depois de R3_08) · Bomba de Pólen (80) |
| **Loja da Vila** (Dona Bolha) | Vila Coaxa (andar 26) | 6:00–22:00 | estalagem-nenúfar (30 por noite) · Poção de Vida M (150) · Água de Coco (25) · Banana (15) · Moscas Fritas (comida dos sapos: +5% velocidade, 10) · Lingote de Aço (270, ×10) · Madeira de Mangue (72, ×20) |
| **Velho Remo** | cais da Vila Coaxa (andar 26) | 5:00–21:00 | aluguer de barco (50 por dia) · Cana de Mangue (300, se não a encontraste no andar 21) · Isco Bom (20, ∞) |
| **Rã-Rã** | cais da Vila Coaxa (andar 26) | 5:00–9:00 e 16:00–19:00 | Pirarucu (300) e Peixe-Arco-Íris (350), 1 de cada por dia · inscrição no concurso (grátis) |
| **Vera Liana** | Refúgio das Copas (andar 28) | 8:00–20:00 | mapas dos andares 21–30 (150 cada; mostram as zonas e as Zonas Seguras) · **paga** 5 ouro por cada 1% novo de exploração (uma vez por andar) |
| **Irmã Nara** | Refúgio das Copas (andar 28) | 7:00–21:00 | curar estados (30) · Poção de Vida M (150) · Poção Purificadora (90) · Antídoto (25) · Poção de Vida P (50) |
| **Tom Tirolesa** | Refúgio das Copas (andar 28) | 7:00–19:00 | Fibra de Liana (72, ×20) · Muda de Bananeira (600) · Banana Frita (35) |

### 3.5 Região 4

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Yusuf** (banca, depois de R4_02) | bazar de Zahra (andar 32) | 7:00–19:00 | **loja de viagem**: Cacto-Água (20, ∞) · Sumo de Cacto (35) · Lenço do Deserto (900) · Tâmaras (15) · Corda · Tocha (10) · Poção de Vida M (150) |
| **Faisal** | bazar de Zahra | 9:00–21:00 | Tapete de Zahra (móvel, 1 500) · tapetes pequenos (400) · Açafrão (120) · Perfume (300) · especiarias (Pimenta, Canela: 30) · Lâmpada Velha (500, R4_11) · 10% de desconto depois de R4_01 |
| **Ferreira Nadia** (forja) | bazar de Zahra | 7:00–19:00 | armas e armaduras de Prata (Comuns, preço da tabela) · Lingote de Prata (480, ×10) · Picareta e Machado de Prata (1 900) · melhorias até +5 · receitas de cimitarras (aspeto de espada, 800) |
| **Layla** | bazar de Zahra (palco) | 16:00–22:00 | lenços e véus (cosméticos, 200–600) · Vestes de Dança (1 200, depois de R4_10) · no **Festival do Oásis**: Lanterna de Papel (móvel, 150) e Cuscuz do Oásis (40) |
| **Hakim** (depois do segredo do andar 36) | bazar de Zahra | 18:00–2:00 | lâmpadas (móveis de luz, 300–2 000) · Óleo de Lâmpada (10) · Lanterna do Deserto (1 400) |
| **Estalagem de Zahra** | ao pé da lagoa | sempre | quarto (40 por noite) · Tâmaras com Mel (30) · Cuscuz do Oásis (40) · Chá de Hortelã (+10% regeneração de Estamina, 15) |
| **Banhos de Zahra** (depois de R4_14) | atrás do palácio | 8:00–22:00 | banho (50): +10% regeneração de HP durante um dia |
| **Mestre Rahim** | estábulos de Zahra | 6:00–18:00 | Tâmaras para a montada (15) · Sela simples (500) · tratar a montada (cura-a, 30) |
| **Beto** | Acampamento dos Escavadores (andar 34) | 6:00–20:00 (dorme das 12:00 às 14:00) | Pá (300) · Corda (20) · Tocha (10) · Mapa do Tesouro usado (só mostra baús de madeira, 100) · tenda-cama (20 por noite) |
| **Mina** | Nómadas do Vento (andar 37; muda de sítio) | 7:00–19:00 | Lenço do Deserto (900) · Turbante de Pano (como o Lenço, mais bonito: 1 100) · tapetes (móveis, 400–1 200) · Sementes de Melão (70) · Bolbo de Açafrão (70) · Pão de Açafrão (40) |
| **Tarik** | Nómadas do Vento | 7:00–19:00 | Tâmaras (15) · Ferradura de Lagarto (+5% velocidade da montada, 800) · aposta nas corridas (100 a 1 000; paga o dobro) |

### 3.6 Região 5

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Velha Astrid** | Pinhal-do-Norte (andar 42) | 8:00–20:00 | Raquetes de Neve (1 800) · gorros, luvas e cachecóis (cosméticos, 200–500) · Casaco de Lã (2 500, depois de R5_01) · Sementes de Couve do Norte (80) · Bolo de Bagas (45) |
| **Loja do Salão** (Ulf) | Pinhal-do-Norte | 6:00–22:00 | salão (dormir, 30) · Sopa de Couve do Norte (45) · Chá Quente (25, depois de R5_13) · Poção Quente (120) · Pinheiro Nevado (200, ×20) · Barra de Gelo Eterno (750, ×10) · Picareta e Machado de Gelo Eterno (3 100) · Isco Bom (20) |
| **Sigrid** (sauna) | Pinhal-do-Norte | 7:00–23:00 | sauna (30): a temperatura não desce durante 1 dia |
| **Erik Trenó** | Pinhal-do-Norte | 6:00–20:00 | viagem de trenó entre Zonas Seguras da região (20, depois de R5_04) |
| **Sven** (Armazém) | Aldeia dos Caçadores (andar 46) | 7:00–19:00 | Pele de Urso Polar (200, ×10) · flechas e virotes · Carne Seca (+10 Temperatura, 20) · armadilhas (para a quinta: afastam corvos, 300) |
| **Ferreiro Gunnar** | Aldeia dos Caçadores | 7:00–19:00 | armas e armaduras de Gelo Eterno (Comuns, preço da tabela) · melhorias até +5 · Barra de Gelo Eterno (750) |
| **Curandeira Helka** | Aldeia dos Caçadores | 8:00–20:00 | curar estados (60) · Poção de Vida M (150) · Poção Quente (120) · Pedra Quente (150, depois de R5_12) |
| **Mosteiro da Aurora** (Irmã Noor) | andar 48 | sempre (noite eterna) | celas (dormir, grátis) · Chá Quente (grátis, 1 por dia) · chás especiais: Chá de Aurora (+20% MP 10 min, 80) · livros de receitas de chá (300 cada) |
| **Benedito** (depois de R5_12) | Praça de Ascendia | 9:00–17:00 | Pedra Quente (180) · Lata (10) · conversa sobre os doze anos no gelo (grátis, comprida) |

### 3.7 Região 6

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Rosa** (taberna e estalagem) | Porto Arquipélago (andar 52) | 7:00–2:00 | quarto (40 por noite) · Caldeirada do Porto (60) · Ananás Grelhado (35) · Sardinhas Assadas (20) · Sementes de Ananás (90) · rumores (30) |
| **Tomé** (estaleiro) | Porto Arquipélago | 7:00–19:00 | melhorias do barco (R6_03) · reparar o barco (100) · Madeira de Naufrágio (288, ×20) · Pólvora (40, ×20) |
| **Loja do Porto** (Capitã Marisa) | Porto Arquipélago | 8:00–20:00 | Poção de Respirar (200) · Faca de Mergulho (600) · Isco Bom (20) · Isco Dourado (150) · Barra de Coral Abissal (1 080, ×10) · Picareta e Machado de Coral Abissal (4 640) |
| **Navio Mercante** (evento semanal) | cais do andar 52 | 1 dia por semana | 6 itens de regiões diferentes, ao acaso (como o Mercador Errante) |
| **Ourives Pérola** | Vila das Pérolas (andar 54) | 9:00–18:00 | joalharia com pérolas (anéis e colares: ver `docs/EQUIPAMENTO.md`, secção 8) · Pérola (500) · compra Pérolas Negras (2 000) |
| **Cabana da Kaia** | Vila das Pérolas | 6:00–18:00 | cabana (20 por noite) · Máscara de Mergulho (depois de R6_06: 1 500) · Batata-Doce Assada (25) · Sementes de Batata-Doce (90) |
| **Nerissa** (forja abissal) | Coralina (andar 57) | 8:00–20:00 | armas e armaduras de Coral Abissal (Comuns, preço da tabela) · melhorias até +5 · receitas de tridentes (aspeto de lança, 1 200) |
| **Loja de Coralina** | Coralina | 9:00–21:00 | Arroz de Marisco (60) · Sushi do Recife (45) · Esporos de Alga Doce (90) · Anémona (100) · Poção de Respirar (200) · Lágrima de Sereia (só com 4 ❤️ da Rainha: 3 000) |
| **Rainha Coralina** (trocas) | Palácio de Pérola | 10:00–18:00 | troca **pérolas** por raros: 10 Pérolas → Gema Normal · 3 Pérolas Negras → Gema Perfeita · 20 Pérolas → Escama Real (decoração) |

### 3.8 Região 7

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Loja do Acampamento** (Mãe Brasa) | Acampamento das Cinzas (andar 61) | 6:00–20:00 | tenda (20 por noite) · Água (5, ∞) · Pão das Cinzas (15, depois de R7_01) · Sementes de Pimenta-Lava (100) · Semente de Lenho-Brasa (1 000, depois de R7_01) |
| **Fuligem** | Acampamento das Cinzas | 9:00–18:00 | mapas "verdadeiros" (10; levam a sítios ao acaso: 1 em 10 dá um baú) |
| **Curandeiro Carvão** | Acampamento das Cinzas | 7:00–21:00 | curar estados (70) · Poção Fresca (90) · Poção Ignífuga (400) · Poção de Vida G (600) |
| **Loja do Bastião** | Bastião de Obsidiana (andar 64) | 6:00–22:00 | estalagem (50 por noite) · Barra de Obsidiana (1 470, ×10) · Brasa de Lava (392, ×20) · Picareta e Machado de Obsidiana (6 510) · armas e armaduras de Obsidiana (Comuns) |
| **Mestre Ragnar** (Forja de Obsidiana) | Bastião | 6:00–20:00 | melhorias até +10 com +5% de sucesso (depois de R7_03) · **Cana Ignífuga** (2 500) · receitas de armas anãs (machados e martelos com runas, 2 000) |
| **Ruby Brasa** | Bastião | 9:00–19:00 | encantamentos de Fogo (gema de Rubi na arma: +10% de dano de Fogo, 1 500) · Rubi (1 000, 1 por semana) · joalharia com rubis |
| **Senhor Vapor** (termas) | Termas dos Géiseres (andar 66) | 6:00–24:00 | termas (50: Calor a 0 e cura tudo durante 1 dia, depois de R7_06) · estalagem (60 por noite) · toalha de lembrança (cosmético, 100) |
| **Massagista Lava** | Termas | 10:00–20:00 | massagem (100): +10% Estamina máx. durante 1 dia |
| **Cozinheira Fumarola** | Termas | 7:00–22:00 | Ovos de Géiser (40) · Batata Vulcânica Assada (30) · Sementes de Batata Vulcânica (100) |
| **Gil** (depois de R7_07) | Termas | 10:00–18:00 | fotografias dos andares (decoração, 200 cada; uma por região) · molduras (50) |

### 3.9 Região 8

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Mortimer** (Mercado Fantasma) | Praça do Mercado (andar 72) | 21:00–4:00 (e de dia depois de R8_02) | paga-se em ouro ou **Lágrimas de Fantasma** (1 = 40 ouro): caixas de música (móveis, 8 Lágrimas) · candelabros (6) · espelhos antigos (10) · Página Antiga (3) · um item raro antigo por noite (ao acaso) |
| **Hugo** (padaria) | Mercado Fantasma | 21:00–4:00 | Pão Fantasma (2 Lágrimas, depois de R8_04) · bolos que não acabam (+10% regeneração de HP 10 min, 1 Lágrima) |
| **Hotel Fantasma** | Mercado Fantasma | sempre (só se entra à noite) | quarto (2 Lágrimas ou 80 ouro): dormir dá um **sonho** com lore (`docs/dialogos/povoacoes_r08.md`, secção 1.6) |
| **Banca de Flores Fantasma** | Mercado Fantasma | 21:00–4:00 | Lírio da Lua (2 Lágrimas) · Rosa Negra (3) · Sementes de Abóbora (só no Outono, 110 ouro) |
| **Loja do Mosteiro** | Mosteiro da Ordem da Luz (andar 77) | 6:00–22:00 | celas (dormir, grátis para quem ajuda a Ordem) · Água Benta (80, ∞) · Lanterna Sagrada (120) · Sálvia Sagrada (60) · Poção de Vida G (600) · curar estados (80) · Sementes de Sálvia (110) |
| **Irmão Bento** (forja de Mitril) | Mosteiro | 7:00–19:00 | purificar Mitril (grátis depois de R8_12; antes, 100 por lingote) · armas e armaduras de Mitril (Comuns) · Lingote de Mitril (1 920, ×10) · Picareta e Machado de Mitril (8 730) · encantamentos de Luz (Diamante na arma: +10% dano de Luz, 2 500) |
| **Caçador Van** | Mosteiro (à porta, ao entardecer) | 17:00–21:00 | virotes de prata (200 por 20) · Poção das Sombras (300) · conselhos sobre vampiros (grátis; longos) |
| **Irmã Clara** | Mosteiro (oficina de vitrais) | 9:00–17:00 | Vidro Colorido (1 500) · vitrais para a casa (móveis de luz, 3 000) |

### 3.10 Região 9

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Loja de Aerópolis** (Brisa) | Aerópolis (andar 82) | 7:00–19:00 | Pêssego Celeste (60) · Sumo de Uva Celeste (90) · Poção de Leveza (250) · Pena Celeste (648, ×5) · Fio de Nuvem (648, ×10) · Madeira-Nuvem (648, ×10) · Sementes de Algodão-Nuvem, Flor-do-Vento e Uva Celeste (120) · Semente de Pessegueiro Celeste (1 200) · Poção de Vida G (600) · curar estados (90) |
| **Estalagem das Cúpulas** | Aerópolis | sempre | quarto (60 por noite; a janela dá para o mar de nuvens) · Tarte Celeste (só depois de R9_09, 120) |
| **Ferreira Ícara** (Forja de Oricalco) | Aerópolis | 6:00–20:00 | armas e armaduras de Oricalco e Penas do Trovão (Comuns) · Lingote de Oricalco (2 430, ×10) · Pedra-Sol (200, ×20) · Picareta e Machado de Oricalco (11 310) · melhorias até +10 com +5% de sucesso · encantamentos de Raio (Topázio na arma: +10% de dano de Raio, 3 000) |
| **Nimbo** (porto de balões) | Aerópolis | 6:00–21:00 | viagem de balão entre as ilhas (grátis) e para os andares 81–89 (50 por viagem; depois de R9_02) |
| **Cúmulo** | Aerópolis (ateliê) | 10:00–18:00 | esculturas de nuvem para a casa (depois de R9_13: 2 500 cada, 6 formas) |
| **Loja do Observatório** (Orion) | Observatório Celeste (andar 86) | 18:00–6:00 (é de noite que se trabalha) | cama (grátis para quem ajuda a Vega) · lentes (cosmético: óculos, 500) · mapas das constelações (decoração, 800) · Cristal Celeste (8 100, 1 por semana) · Poção de Leveza (250) |
| **Velho Altair** | Observatório (varanda) | 20:00–4:00 | Pó de Estrela (5 000, 1 por semana, depois de R9_15) · ouvir as estrelas (grátis: diz que tempo vai fazer amanhã na região) |
| **Monges do Vento** | Templo dos Ventos (andar 88) | 5:00–21:00 | esteira (dormir, grátis) · chá de Flor-do-Vento (20: +10% Estamina durante 10 min) · bandeiras de oração (decoração, 150) · Sino de Vento (só depois de R9_14, 1 000) |

### 3.11 Região 10

| Loja | Onde | Horário | À venda |
|---|---|---|---|
| **Tibério** (loja grande) | Último Posto (andar 91, depois de R10_01) | 6:00–22:00 | o stock normal dele (secção 3.1) e mais: Poção de Vida Máxima (3 000) · Lanterna-Âncora (500) · Pele do Vazio e Fio de Luz Estelar (800, ×10) · Pedra de Regresso (60, ∞) · "anti-estado" da região: Poção do Tempo (1 080) |
| **Tendas da Guilda** (Sargento Bruma) | Último Posto | sempre | tenda (grátis para aventureiros) · Guisado das Estrelas (só depois de R10_02, 200) · Chá de Campanha (15: cura 10%) |
| **Dorn** (Forja Estelar) | Último Posto (depois de R10_02) | 6:00–20:00 | armas e armaduras Estelares (Comuns) · Lingote Estelar (3 000, ×10) · Núcleo do Vazio (10 000, 1 por semana) · Picareta e Machado Estelares (14 260) · melhorias até +10 com +5% de sucesso · **armas míticas** (R10_11: só o trabalho, 50 000 cada; os materiais trazes tu) · Armadura de Aren (5 Lingote Estelar + 1 Coração Estelar por peça; trabalho 20 000) · Semente de Árvore Estelar (1 300) |
| **Mercado das Memórias** (Chico) | Cidade dos Perdidos (andar 97) | sempre (o tempo não passava; depois de C10-10, 8:00–20:00) | **troca**: 10 Fragmento de Eco = 5 materiais básicos de qualquer região já visitada, ou 1 lingote, ou 1 Semente do Mundo · objetos do mundo real (decoração: 6 por semana, 500 a 3 000 cada) · Semente do Mundo (130, ou 10 Fragmentos de Eco) |
| **Casa da Mãe Dois** | Cidade dos Perdidos | sempre | Chá da Mãe Dois (grátis, 1 por dia) · ela tricota-te uma peça de roupa (cosmético) se lhe deres 5 Fio de Luz Estelar (demora 3 dias) |
| **O Desistente** | Praça do Desistir (depois de C10-09) | sempre | vende as armas velhas dele (5 armas de tier 9, Raras, preço normal) · "conselhos para desistir" (grátis; são péssimos de propósito) |
| **A Arquivista** | Biblioteca do Mundo (andar 98) | sempre | não vende. Empresta livros dos mundos (decoração para a casa, devolvem-se sozinhos ao fim de 7 dias) · Página Antiga (300) · Tinta Mágica (500) |

---

## 4. Vagar, a Cidade Errante

| Loja | Quem | À venda |
|---|---|---|
| **Itens de todo o lado** | Mercador Errante Ambrósio | 6 itens raros de **qualquer região, mesmo das que ainda não visitaste** (preço ×2): materiais, sementes, gemas Normais, Isco Lendário (1 000), receitas raras, 1 arma Épica (tabela × 6) |
| **Leilão** | Leiloeiro Gaspar | 3 itens raros por visita (troféus, móveis únicos, armas Lendárias, ovos de animais raros). Licitas contra 3 NPCs; o preço começa em metade do valor. Minijogo em `docs/ATIVIDADES.md` |
| **Trocas** | Troca-Tudo | troca 2 materiais de uma região por 1 de outra (qualquer uma já visitada) |
| **Moda** | Madame Plumas | cosméticos únicos: 4 por visita (chapéus, capas, cores raras do herói, roupa do animal de estimação), 1 000 a 10 000 |
| **Tartaruga** | a própria Vagar | 10 Alga Doce → leva-te ao andar mais alto desbloqueado |
