# Armas

Todas as armas do jogo, com os números para programar. Os números seguem as fórmulas de `docs/SISTEMAS.md`
(dano, raridade, melhorias) e afinam-se depois a jogar.

## Resumo

| Grupo | Quantidade | Onde se arranjam |
|---|---|---|
| Armas normais (12 tipos × 10 materiais) | 120 | forja (receitas), lojas, baús, drops |
| Armas únicas dos bosses | 20 | 1.ª vitória contra cada mini-boss e boss |
| Armas de guardião | 79 | guardiões dos andares (30%; 100% na 1.ª vitória com o desafio feito) |
| Armas secretas | 10 | bosses das masmorras escondidas (1 por região) |
| Armas raras (monstros com nome, missões) | 12 | ver secção 7 |
| Armas de amizade | 5 | 10 corações com certos NPCs |
| Armas míticas | 12 | Forja Estelar, no fim do jogo |
| **Total** | **~258** | |

As **raridades** (Comum → Mítico) mudam os stats e o **brilho** da arma; o brilho é feito pelo jogo, **não é preciso
desenhar a arma outra vez** para cada raridade. Cada arma tem **um sprite** (32×32 ou 48×48) e **um ícone** (16×16)
(ver `docs/ARTE.md`, secção 4).

---

## 1. Os 12 tipos de armas

| Tipo | Atributo | Combo | Ataque carregado (segurar 0,8 s) | Especial do tipo | Animação do herói | Sprite |
|---|---|---|---|---|---|---|
| **Espada** | FOR | 3 golpes: corte, corte, estocada | Corte Giratório (360°) | equilibrada | Corte | 32×32 |
| **Espada Grande** | FOR | 2 golpes largos (180°) | Golpe da Terra (onda em linha) | acerta à volta; lenta | Pesado | 48×48 |
| **Adaga** | DES / AGI | 4 golpes muito rápidos | Estocada Dupla | **×2 pelas costas**; crítico alto | Corte | 32×32 |
| **Katana** | AGI | 3 cortes | **Iai**: corte rápido em linha (×2,5 em vez de ×2,2) | rápida e precisa | Corte | 48×48 |
| **Machado** | FOR | 2 golpes pesados | Arremesso (o machado volta) | 10% Sangrar; **corta árvores** como um machado de ferramenta do mesmo tier | Pesado | 32×32 |
| **Martelo** | FOR | 2 golpes pesados | Tremor (área 3 m) | 15% Atordoado; **parte rochas** como uma picareta de um tier abaixo | Pesado | 48×48 |
| **Lança** | FOR / AGI | 3 estocadas | Investida (6 m) | alcance longo; atravessa 2 inimigos | Estocada | 48×48 |
| **Foice** | AGI | 2 golpes em arco largo (240°) | Ceifar (círculo completo) | 3% de roubo de vida | Corte | 48×48 |
| **Arco** | DES | tiro a tiro | Tiro Carregado (×2, atravessa) | longo alcance; **flechas infinitas** | Disparo | 32×32 |
| **Besta** | DES | tiro, recarga 0,7 s | Virote Pesado (empurra) | atravessa escudos; crítico alto | Disparo | 32×32 |
| **Cajado** | INT | projéteis mágicos (0 MP) | Projétil Grande (×2,2, 10 MP) | o elemento vem da **gema** encaixada; sem gema é "Arcano" (neutro) | Magia | 48×48 |
| **Manoplas** | FOR / AGI | 6 socos muito rápidos | Uppercut (atira o inimigo ao ar) | o último golpe do combo empurra | Soco | 32×32 |

Cada tipo tem **"Manejo de …"** (nível 1 a 10) que sobe com o uso e dá ataques especiais (ver `docs/PROGRESSAO.md`).

---

## 2. Raridades

| Raridade | Hipótese num baú/drop | Stats | Brilho (feito pelo jogo) |
|---|---|---|---|
| Comum | 60% | ×1,00 | nenhum |
| Incomum | 25% | ×1,10 | brilho fraco verde |
| Raro | 10% | ×1,25 | brilho azul + faíscas |
| Épico | 4% | ×1,45 | brilho roxo forte + partículas |
| Lendário | 0,9% | ×1,70 | aura laranja + rasto nos golpes |
| Mítico | 0,1% (só andares 91+) e as 12 míticas | ×2,00 | aura arco-íris animada + rasto + som |

- Armas **feitas na forja** saem **Comuns** (com qualidade Normal / Boa / Excelente). Armas Raras ou melhores vêm de baús, drops e lojas especiais.
- **Únicas, secretas, de guardião e míticas** têm raridade **fixa** (ver cada secção).
- **Melhorias +1 a +10**: +5% de ATQ cada (ver `docs/SISTEMAS.md`, secção 11.3).
- **Encantamento**: encaixar uma **gema** dá o elemento à arma (ver `docs/EQUIPAMENTO.md`).

---

## 3. As 120 armas normais

**ATQ** = ATQ base do tier × multiplicador do tipo (Espada 1,0 · Espada Grande 1,8 · Adaga 0,6 · Katana 1,1 ·
Machado 1,4 · Martelo 1,7 · Lança 1,15 · Foice 1,3 · Arco 0,9 · Besta 1,4 · Cajado 1,0 (mágico) · Manoplas 0,55).
**ATQ base** por tier: 12 · 24 · 40 · 60 · 85 · 115 · 150 · 190 · 235 · 290.
**Preço** = 150 × tier^2,2 × fator do tipo. A forja pede também **20% do preço em ouro**.

### Tier 1 — Cobre (Região 1, nível mínimo 1)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_cobre` | Espada de Cobre | 12 | 1,6 | 1,8 m | 5% | 2,0 kg | 150 | 3 Lingote de Cobre + 1 Couro de Javali |
| `espada_grande_cobre` | Espada Grande de Cobre | 22 | 0,8 | 2,4 m | 5% | 6,0 kg | 200 | 5 Lingote de Cobre + 1 Madeira de Carvalho + 1 Couro de Javali |
| `adaga_cobre` | Adaga de Cobre | 7 | 2,6 | 1,2 m | 15% | 1,0 kg | 120 | 2 Lingote de Cobre + 1 Couro de Javali |
| `katana_cobre` | Katana de Cobre | 13 | 1,5 | 2,0 m | 10% | 2,5 kg | 180 | 4 Lingote de Cobre + 1 Couro de Javali + 1 Linho Bravo |
| `machado_cobre` | Machado de Cobre | 17 | 1,1 | 1,8 m | 8% | 4,0 kg | 150 | 3 Lingote de Cobre + 2 Madeira de Carvalho |
| `martelo_cobre` | Martelo de Cobre | 20 | 0,85 | 1,8 m | 5% | 7,0 kg | 160 | 5 Lingote de Cobre + 2 Madeira de Carvalho |
| `lanca_cobre` | Lança de Cobre | 14 | 1,3 | 3,0 m | 7% | 3,5 kg | 150 | 2 Lingote de Cobre + 3 Madeira de Carvalho |
| `foice_cobre` | Foice de Cobre | 16 | 1,1 | 2,6 m | 10% | 4,0 kg | 160 | 3 Lingote de Cobre + 2 Madeira de Carvalho + 1 Linho Bravo |
| `arco_cobre` | Arco de Cobre | 11 | 1,2 | 18 m | 10% | 1,5 kg | 150 | 1 Lingote de Cobre + 4 Madeira de Carvalho + 2 Linho Bravo |
| `besta_cobre` | Besta de Cobre | 17 | 0,7 | 20 m | 12% | 4,5 kg | 180 | 2 Lingote de Cobre + 3 Madeira de Carvalho + 2 Linho Bravo |
| `cajado_cobre` | Cajado de Cobre | 12 mág. | 1,0 | 12 m | 5% | 2,0 kg | 180 | 1 Lingote de Cobre + 4 Madeira de Carvalho + 1 Seiva Cristalizada |
| `manoplas_cobre` | Manoplas de Cobre | 7 | 3,0 | 1,0 m | 8% | 2,5 kg | 140 | 3 Lingote de Cobre + 2 Couro de Javali |

### Tier 2 — Ferro (Região 2, nível mínimo 11)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_ferro` | Espada de Ferro | 24 | 1,6 | 1,8 m | 5% | 2,0 kg | 690 | 3 Lingote de Ferro + 1 Couro de Toupeira |
| `espada_grande_ferro` | Espada Grande de Ferro | 43 | 0,8 | 2,4 m | 5% | 6,0 kg | 900 | 5 Lingote de Ferro + 1 Escora Velha + 1 Couro de Toupeira |
| `adaga_ferro` | Adaga de Ferro | 14 | 2,6 | 1,2 m | 15% | 1,0 kg | 550 | 2 Lingote de Ferro + 1 Couro de Toupeira |
| `katana_ferro` | Katana de Ferro | 26 | 1,5 | 2,0 m | 10% | 2,5 kg | 830 | 4 Lingote de Ferro + 1 Couro de Toupeira + 1 Seda de Aranha |
| `machado_ferro` | Machado de Ferro | 34 | 1,1 | 1,8 m | 8% | 4,0 kg | 690 | 3 Lingote de Ferro + 2 Escora Velha |
| `martelo_ferro` | Martelo de Ferro | 41 | 0,85 | 1,8 m | 5% | 7,0 kg | 760 | 5 Lingote de Ferro + 2 Escora Velha |
| `lanca_ferro` | Lança de Ferro | 28 | 1,3 | 3,0 m | 7% | 3,5 kg | 690 | 2 Lingote de Ferro + 3 Escora Velha |
| `foice_ferro` | Foice de Ferro | 31 | 1,1 | 2,6 m | 10% | 4,0 kg | 760 | 3 Lingote de Ferro + 2 Escora Velha + 1 Seda de Aranha |
| `arco_ferro` | Arco de Ferro | 22 | 1,2 | 18 m | 10% | 1,5 kg | 690 | 1 Lingote de Ferro + 4 Escora Velha + 2 Seda de Aranha |
| `besta_ferro` | Besta de Ferro | 34 | 0,7 | 20 m | 12% | 4,5 kg | 830 | 2 Lingote de Ferro + 3 Escora Velha + 2 Seda de Aranha |
| `cajado_ferro` | Cajado de Ferro | 24 mág. | 1,0 | 12 m | 5% | 2,0 kg | 830 | 1 Lingote de Ferro + 4 Escora Velha + 1 Cristal de Gruta |
| `manoplas_ferro` | Manoplas de Ferro | 13 | 3,0 | 1,0 m | 8% | 2,5 kg | 620 | 3 Lingote de Ferro + 2 Couro de Toupeira |

### Tier 3 — Aço (Região 3, nível mínimo 21)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_aco` | Espada de Aço | 40 | 1,6 | 1,8 m | 5% | 2,0 kg | 1 680 | 3 Lingote de Aço + 1 Pele de Crocodilo |
| `espada_grande_aco` | Espada Grande de Aço | 72 | 0,8 | 2,4 m | 5% | 6,0 kg | 2 190 | 5 Lingote de Aço + 1 Madeira de Mangue + 1 Pele de Crocodilo |
| `adaga_aco` | Adaga de Aço | 24 | 2,6 | 1,2 m | 15% | 1,0 kg | 1 350 | 2 Lingote de Aço + 1 Pele de Crocodilo |
| `katana_aco` | Katana de Aço | 44 | 1,5 | 2,0 m | 10% | 2,5 kg | 2 020 | 4 Lingote de Aço + 1 Pele de Crocodilo + 1 Fibra de Liana |
| `machado_aco` | Machado de Aço | 56 | 1,1 | 1,8 m | 8% | 4,0 kg | 1 680 | 3 Lingote de Aço + 2 Madeira de Mangue |
| `martelo_aco` | Martelo de Aço | 68 | 0,85 | 1,8 m | 5% | 7,0 kg | 1 850 | 5 Lingote de Aço + 2 Madeira de Mangue |
| `lanca_aco` | Lança de Aço | 46 | 1,3 | 3,0 m | 7% | 3,5 kg | 1 680 | 2 Lingote de Aço + 3 Madeira de Mangue |
| `foice_aco` | Foice de Aço | 52 | 1,1 | 2,6 m | 10% | 4,0 kg | 1 850 | 3 Lingote de Aço + 2 Madeira de Mangue + 1 Fibra de Liana |
| `arco_aco` | Arco de Aço | 36 | 1,2 | 18 m | 10% | 1,5 kg | 1 680 | 1 Lingote de Aço + 4 Madeira de Mangue + 2 Fibra de Liana |
| `besta_aco` | Besta de Aço | 56 | 0,7 | 20 m | 12% | 4,5 kg | 2 020 | 2 Lingote de Aço + 3 Madeira de Mangue + 2 Fibra de Liana |
| `cajado_aco` | Cajado de Aço | 40 mág. | 1,0 | 12 m | 5% | 2,0 kg | 2 020 | 1 Lingote de Aço + 4 Madeira de Mangue + 1 Âmbar do Pântano |
| `manoplas_aco` | Manoplas de Aço | 22 | 3,0 | 1,0 m | 8% | 2,5 kg | 1 510 | 3 Lingote de Aço + 2 Pele de Crocodilo |

### Tier 4 — Prata (Região 4, nível mínimo 31)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_prata` | Espada de Prata | 60 | 1,6 | 1,8 m | 5% | 2,0 kg | 3 170 | 3 Lingote de Prata + 1 Couro de Chacal |
| `espada_grande_prata` | Espada Grande de Prata | 108 | 0,8 | 2,4 m | 5% | 6,0 kg | 4 120 | 5 Lingote de Prata + 1 Madeira de Acácia + 1 Couro de Chacal |
| `adaga_prata` | Adaga de Prata | 36 | 2,6 | 1,2 m | 15% | 1,0 kg | 2 530 | 2 Lingote de Prata + 1 Couro de Chacal |
| `katana_prata` | Katana de Prata | 66 | 1,5 | 2,0 m | 10% | 2,5 kg | 3 800 | 4 Lingote de Prata + 1 Couro de Chacal + 1 Ligadura Antiga |
| `machado_prata` | Machado de Prata | 84 | 1,1 | 1,8 m | 8% | 4,0 kg | 3 170 | 3 Lingote de Prata + 2 Madeira de Acácia |
| `martelo_prata` | Martelo de Prata | 102 | 0,85 | 1,8 m | 5% | 7,0 kg | 3 480 | 5 Lingote de Prata + 2 Madeira de Acácia |
| `lanca_prata` | Lança de Prata | 69 | 1,3 | 3,0 m | 7% | 3,5 kg | 3 170 | 2 Lingote de Prata + 3 Madeira de Acácia |
| `foice_prata` | Foice de Prata | 78 | 1,1 | 2,6 m | 10% | 4,0 kg | 3 480 | 3 Lingote de Prata + 2 Madeira de Acácia + 1 Ligadura Antiga |
| `arco_prata` | Arco de Prata | 54 | 1,2 | 18 m | 10% | 1,5 kg | 3 170 | 1 Lingote de Prata + 4 Madeira de Acácia + 2 Ligadura Antiga |
| `besta_prata` | Besta de Prata | 84 | 0,7 | 20 m | 12% | 4,5 kg | 3 800 | 2 Lingote de Prata + 3 Madeira de Acácia + 2 Ligadura Antiga |
| `cajado_prata` | Cajado de Prata | 60 mág. | 1,0 | 12 m | 5% | 2,0 kg | 3 800 | 1 Lingote de Prata + 4 Madeira de Acácia + 1 Vidro Solar |
| `manoplas_prata` | Manoplas de Prata | 33 | 3,0 | 1,0 m | 8% | 2,5 kg | 2 850 | 3 Lingote de Prata + 2 Couro de Chacal |

### Tier 5 — Gelo Eterno (Região 5, nível mínimo 41)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_gelo_eterno` | Espada de Gelo Eterno | 85 | 1,6 | 1,8 m | 5% | 2,0 kg | 5 170 | 3 Barra de Gelo Eterno + 1 Pele de Urso Polar |
| `espada_grande_gelo_eterno` | Espada Grande de Gelo Eterno | 153 | 0,8 | 2,4 m | 5% | 6,0 kg | 6 730 | 5 Barra de Gelo Eterno + 1 Pinheiro Nevado + 1 Pele de Urso Polar |
| `adaga_gelo_eterno` | Adaga de Gelo Eterno | 51 | 2,6 | 1,2 m | 15% | 1,0 kg | 4 140 | 2 Barra de Gelo Eterno + 1 Pele de Urso Polar |
| `katana_gelo_eterno` | Katana de Gelo Eterno | 94 | 1,5 | 2,0 m | 10% | 2,5 kg | 6 210 | 4 Barra de Gelo Eterno + 1 Pele de Urso Polar + 1 Lã de Mamute |
| `machado_gelo_eterno` | Machado de Gelo Eterno | 119 | 1,1 | 1,8 m | 8% | 4,0 kg | 5 170 | 3 Barra de Gelo Eterno + 2 Pinheiro Nevado |
| `martelo_gelo_eterno` | Martelo de Gelo Eterno | 144 | 0,85 | 1,8 m | 5% | 7,0 kg | 5 690 | 5 Barra de Gelo Eterno + 2 Pinheiro Nevado |
| `lanca_gelo_eterno` | Lança de Gelo Eterno | 98 | 1,3 | 3,0 m | 7% | 3,5 kg | 5 170 | 2 Barra de Gelo Eterno + 3 Pinheiro Nevado |
| `foice_gelo_eterno` | Foice de Gelo Eterno | 110 | 1,1 | 2,6 m | 10% | 4,0 kg | 5 690 | 3 Barra de Gelo Eterno + 2 Pinheiro Nevado + 1 Lã de Mamute |
| `arco_gelo_eterno` | Arco de Gelo Eterno | 76 | 1,2 | 18 m | 10% | 1,5 kg | 5 170 | 1 Barra de Gelo Eterno + 4 Pinheiro Nevado + 2 Lã de Mamute |
| `besta_gelo_eterno` | Besta de Gelo Eterno | 119 | 0,7 | 20 m | 12% | 4,5 kg | 6 210 | 2 Barra de Gelo Eterno + 3 Pinheiro Nevado + 2 Lã de Mamute |
| `cajado_gelo_eterno` | Cajado de Gelo Eterno | 85 mág. | 1,0 | 12 m | 5% | 2,0 kg | 6 210 | 1 Barra de Gelo Eterno + 4 Pinheiro Nevado + 1 Lágrima de Aurora |
| `manoplas_gelo_eterno` | Manoplas de Gelo Eterno | 47 | 3,0 | 1,0 m | 8% | 2,5 kg | 4 660 | 3 Barra de Gelo Eterno + 2 Pele de Urso Polar |

### Tier 6 — Coral Abissal (Região 6, nível mínimo 51)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_coral_abissal` | Espada de Coral Abissal | 115 | 1,6 | 1,8 m | 5% | 2,0 kg | 7 730 | 3 Barra de Coral Abissal + 1 Pele de Tubarão |
| `espada_grande_coral_abissal` | Espada Grande de Coral Abissal | 207 | 0,8 | 2,4 m | 5% | 6,0 kg | 10 050 | 5 Barra de Coral Abissal + 1 Madeira de Naufrágio + 1 Pele de Tubarão |
| `adaga_coral_abissal` | Adaga de Coral Abissal | 69 | 2,6 | 1,2 m | 15% | 1,0 kg | 6 180 | 2 Barra de Coral Abissal + 1 Pele de Tubarão |
| `katana_coral_abissal` | Katana de Coral Abissal | 127 | 1,5 | 2,0 m | 10% | 2,5 kg | 9 270 | 4 Barra de Coral Abissal + 1 Pele de Tubarão + 1 Fio de Alga-Prata |
| `machado_coral_abissal` | Machado de Coral Abissal | 161 | 1,1 | 1,8 m | 8% | 4,0 kg | 7 730 | 3 Barra de Coral Abissal + 2 Madeira de Naufrágio |
| `martelo_coral_abissal` | Martelo de Coral Abissal | 196 | 0,85 | 1,8 m | 5% | 7,0 kg | 8 500 | 5 Barra de Coral Abissal + 2 Madeira de Naufrágio |
| `lanca_coral_abissal` | Lança de Coral Abissal | 132 | 1,3 | 3,0 m | 7% | 3,5 kg | 7 730 | 2 Barra de Coral Abissal + 3 Madeira de Naufrágio |
| `foice_coral_abissal` | Foice de Coral Abissal | 150 | 1,1 | 2,6 m | 10% | 4,0 kg | 8 500 | 3 Barra de Coral Abissal + 2 Madeira de Naufrágio + 1 Fio de Alga-Prata |
| `arco_coral_abissal` | Arco de Coral Abissal | 104 | 1,2 | 18 m | 10% | 1,5 kg | 7 730 | 1 Barra de Coral Abissal + 4 Madeira de Naufrágio + 2 Fio de Alga-Prata |
| `besta_coral_abissal` | Besta de Coral Abissal | 161 | 0,7 | 20 m | 12% | 4,5 kg | 9 270 | 2 Barra de Coral Abissal + 3 Madeira de Naufrágio + 2 Fio de Alga-Prata |
| `cajado_coral_abissal` | Cajado de Coral Abissal | 115 mág. | 1,0 | 12 m | 5% | 2,0 kg | 9 270 | 1 Barra de Coral Abissal + 4 Madeira de Naufrágio + 1 Pérola |
| `manoplas_coral_abissal` | Manoplas de Coral Abissal | 63 | 3,0 | 1,0 m | 8% | 2,5 kg | 6 950 | 3 Barra de Coral Abissal + 2 Pele de Tubarão |

### Tier 7 — Obsidiana (Região 7, nível mínimo 61)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_obsidiana` | Espada de Obsidiana | 150 | 1,6 | 1,8 m | 5% | 2,0 kg | 10 850 | 3 Barra de Obsidiana + 1 Couro de Salamandra |
| `espada_grande_obsidiana` | Espada Grande de Obsidiana | 270 | 0,8 | 2,4 m | 5% | 6,0 kg | 14 100 | 5 Barra de Obsidiana + 1 Lenho-Brasa + 1 Couro de Salamandra |
| `adaga_obsidiana` | Adaga de Obsidiana | 90 | 2,6 | 1,2 m | 15% | 1,0 kg | 8 680 | 2 Barra de Obsidiana + 1 Couro de Salamandra |
| `katana_obsidiana` | Katana de Obsidiana | 165 | 1,5 | 2,0 m | 10% | 2,5 kg | 13 020 | 4 Barra de Obsidiana + 1 Couro de Salamandra + 1 Seda Ignífuga |
| `machado_obsidiana` | Machado de Obsidiana | 210 | 1,1 | 1,8 m | 8% | 4,0 kg | 10 850 | 3 Barra de Obsidiana + 2 Lenho-Brasa |
| `martelo_obsidiana` | Martelo de Obsidiana | 255 | 0,85 | 1,8 m | 5% | 7,0 kg | 11 930 | 5 Barra de Obsidiana + 2 Lenho-Brasa |
| `lanca_obsidiana` | Lança de Obsidiana | 172 | 1,3 | 3,0 m | 7% | 3,5 kg | 10 850 | 2 Barra de Obsidiana + 3 Lenho-Brasa |
| `foice_obsidiana` | Foice de Obsidiana | 195 | 1,1 | 2,6 m | 10% | 4,0 kg | 11 930 | 3 Barra de Obsidiana + 2 Lenho-Brasa + 1 Seda Ignífuga |
| `arco_obsidiana` | Arco de Obsidiana | 135 | 1,2 | 18 m | 10% | 1,5 kg | 10 850 | 1 Barra de Obsidiana + 4 Lenho-Brasa + 2 Seda Ignífuga |
| `besta_obsidiana` | Besta de Obsidiana | 210 | 0,7 | 20 m | 12% | 4,5 kg | 13 020 | 2 Barra de Obsidiana + 3 Lenho-Brasa + 2 Seda Ignífuga |
| `cajado_obsidiana` | Cajado de Obsidiana | 150 mág. | 1,0 | 12 m | 5% | 2,0 kg | 13 020 | 1 Barra de Obsidiana + 4 Lenho-Brasa + 1 Cristal de Magma |
| `manoplas_obsidiana` | Manoplas de Obsidiana | 82 | 3,0 | 1,0 m | 8% | 2,5 kg | 9 760 | 3 Barra de Obsidiana + 2 Couro de Salamandra |

### Tier 8 — Mitril (Região 8, nível mínimo 71)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_mitril` | Espada de Mitril | 190 | 1,6 | 1,8 m | 5% | 2,0 kg | 14 550 | 3 Lingote de Mitril + 1 Asa de Gárgula |
| `espada_grande_mitril` | Espada Grande de Mitril | 342 | 0,8 | 2,4 m | 5% | 6,0 kg | 18 920 | 5 Lingote de Mitril + 1 Ébano Morto + 1 Asa de Gárgula |
| `adaga_mitril` | Adaga de Mitril | 114 | 2,6 | 1,2 m | 15% | 1,0 kg | 11 640 | 2 Lingote de Mitril + 1 Asa de Gárgula |
| `katana_mitril` | Katana de Mitril | 209 | 1,5 | 2,0 m | 10% | 2,5 kg | 17 460 | 4 Lingote de Mitril + 1 Asa de Gárgula + 1 Fio Espectral |
| `machado_mitril` | Machado de Mitril | 266 | 1,1 | 1,8 m | 8% | 4,0 kg | 14 550 | 3 Lingote de Mitril + 2 Ébano Morto |
| `martelo_mitril` | Martelo de Mitril | 323 | 0,85 | 1,8 m | 5% | 7,0 kg | 16 010 | 5 Lingote de Mitril + 2 Ébano Morto |
| `lanca_mitril` | Lança de Mitril | 218 | 1,3 | 3,0 m | 7% | 3,5 kg | 14 550 | 2 Lingote de Mitril + 3 Ébano Morto |
| `foice_mitril` | Foice de Mitril | 247 | 1,1 | 2,6 m | 10% | 4,0 kg | 16 010 | 3 Lingote de Mitril + 2 Ébano Morto + 1 Fio Espectral |
| `arco_mitril` | Arco de Mitril | 171 | 1,2 | 18 m | 10% | 1,5 kg | 14 550 | 1 Lingote de Mitril + 4 Ébano Morto + 2 Fio Espectral |
| `besta_mitril` | Besta de Mitril | 266 | 0,7 | 20 m | 12% | 4,5 kg | 17 460 | 2 Lingote de Mitril + 3 Ébano Morto + 2 Fio Espectral |
| `cajado_mitril` | Cajado de Mitril | 190 mág. | 1,0 | 12 m | 5% | 2,0 kg | 17 460 | 1 Lingote de Mitril + 4 Ébano Morto + 1 Lágrima de Fantasma |
| `manoplas_mitril` | Manoplas de Mitril | 105 | 3,0 | 1,0 m | 8% | 2,5 kg | 13 100 | 3 Lingote de Mitril + 2 Asa de Gárgula |

### Tier 9 — Oricalco (Região 9, nível mínimo 81)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_oricalco` | Espada de Oricalco | 235 | 1,6 | 1,8 m | 5% | 2,0 kg | 18 850 | 3 Lingote de Oricalco + 1 Pele de Pássaro-Trovão |
| `espada_grande_oricalco` | Espada Grande de Oricalco | 423 | 0,8 | 2,4 m | 5% | 6,0 kg | 24 510 | 5 Lingote de Oricalco + 1 Madeira-Nuvem + 1 Pele de Pássaro-Trovão |
| `adaga_oricalco` | Adaga de Oricalco | 141 | 2,6 | 1,2 m | 15% | 1,0 kg | 15 080 | 2 Lingote de Oricalco + 1 Pele de Pássaro-Trovão |
| `katana_oricalco` | Katana de Oricalco | 258 | 1,5 | 2,0 m | 10% | 2,5 kg | 22 630 | 4 Lingote de Oricalco + 1 Pele de Pássaro-Trovão + 1 Fio de Nuvem |
| `machado_oricalco` | Machado de Oricalco | 329 | 1,1 | 1,8 m | 8% | 4,0 kg | 18 850 | 3 Lingote de Oricalco + 2 Madeira-Nuvem |
| `martelo_oricalco` | Martelo de Oricalco | 400 | 0,85 | 1,8 m | 5% | 7,0 kg | 20 740 | 5 Lingote de Oricalco + 2 Madeira-Nuvem |
| `lanca_oricalco` | Lança de Oricalco | 270 | 1,3 | 3,0 m | 7% | 3,5 kg | 18 850 | 2 Lingote de Oricalco + 3 Madeira-Nuvem |
| `foice_oricalco` | Foice de Oricalco | 306 | 1,1 | 2,6 m | 10% | 4,0 kg | 20 740 | 3 Lingote de Oricalco + 2 Madeira-Nuvem + 1 Fio de Nuvem |
| `arco_oricalco` | Arco de Oricalco | 212 | 1,2 | 18 m | 10% | 1,5 kg | 18 850 | 1 Lingote de Oricalco + 4 Madeira-Nuvem + 2 Fio de Nuvem |
| `besta_oricalco` | Besta de Oricalco | 329 | 0,7 | 20 m | 12% | 4,5 kg | 22 630 | 2 Lingote de Oricalco + 3 Madeira-Nuvem + 2 Fio de Nuvem |
| `cajado_oricalco` | Cajado de Oricalco | 235 mág. | 1,0 | 12 m | 5% | 2,0 kg | 22 630 | 1 Lingote de Oricalco + 4 Madeira-Nuvem + 1 Cristal Celeste |
| `manoplas_oricalco` | Manoplas de Oricalco | 129 | 3,0 | 1,0 m | 8% | 2,5 kg | 16 970 | 3 Lingote de Oricalco + 2 Pele de Pássaro-Trovão |

### Tier 10 — Estelar (Região 10, nível mínimo 91)

| ID | Arma | ATQ | Vel. | Alcance | Crít. | Peso | Preço | Receita (+ 20% do preço em ouro) |
|---|---|---|---|---|---|---|---|---|
| `espada_estelar` | Espada Estelar | 290 | 1,6 | 1,8 m | 5% | 2,0 kg | 23 770 | 3 Lingote Estelar + 1 Pele do Vazio |
| `espada_grande_estelar` | Espada Grande Estelar | 522 | 0,8 | 2,4 m | 5% | 6,0 kg | 30 910 | 5 Lingote Estelar + 1 Madeira do Tempo + 1 Pele do Vazio |
| `adaga_estelar` | Adaga Estelar | 174 | 2,6 | 1,2 m | 15% | 1,0 kg | 19 020 | 2 Lingote Estelar + 1 Pele do Vazio |
| `katana_estelar` | Katana Estelar | 319 | 1,5 | 2,0 m | 10% | 2,5 kg | 28 530 | 4 Lingote Estelar + 1 Pele do Vazio + 1 Fio de Luz Estelar |
| `machado_estelar` | Machado Estelar | 406 | 1,1 | 1,8 m | 8% | 4,0 kg | 23 770 | 3 Lingote Estelar + 2 Madeira do Tempo |
| `martelo_estelar` | Martelo Estelar | 493 | 0,85 | 1,8 m | 5% | 7,0 kg | 26 150 | 5 Lingote Estelar + 2 Madeira do Tempo |
| `lanca_estelar` | Lança Estelar | 334 | 1,3 | 3,0 m | 7% | 3,5 kg | 23 770 | 2 Lingote Estelar + 3 Madeira do Tempo |
| `foice_estelar` | Foice Estelar | 377 | 1,1 | 2,6 m | 10% | 4,0 kg | 26 150 | 3 Lingote Estelar + 2 Madeira do Tempo + 1 Fio de Luz Estelar |
| `arco_estelar` | Arco Estelar | 261 | 1,2 | 18 m | 10% | 1,5 kg | 23 770 | 1 Lingote Estelar + 4 Madeira do Tempo + 2 Fio de Luz Estelar |
| `besta_estelar` | Besta Estelar | 406 | 0,7 | 20 m | 12% | 4,5 kg | 28 530 | 2 Lingote Estelar + 3 Madeira do Tempo + 2 Fio de Luz Estelar |
| `cajado_estelar` | Cajado Estelar | 290 mág. | 1,0 | 12 m | 5% | 2,0 kg | 28 530 | 1 Lingote Estelar + 4 Madeira do Tempo + 1 Núcleo do Vazio |
| `manoplas_estelar` | Manoplas Estelar | 160 | 3,0 | 1,0 m | 8% | 2,5 kg | 21 400 | 3 Lingote Estelar + 2 Pele do Vazio |

---

## 4. Armas únicas dos bosses (20)

Raridade **Lendária** fixa. ATQ base = arma normal do mesmo tier × 1,2 (antes da raridade).

| Andar | Boss | Arma | Tipo | Tier | ATQ base | Efeito |
|---|---|---|---|---|---|---|
| 5 | Javali-Rei | **Presa do Javali-Rei** | Machado | 1 | 20 | Investida que derruba inimigos (ataque carregado) |
| 10 | Ent Ancião | **Raiz Ancestral** | Cajado | 1 | 14 mág. | Raízes prendem os inimigos 2 s (25%) |
| 15 | Aranha-Mãe | **Presa Venenosa** | Adaga | 2 | 17 | Veneno em 30% dos golpes |
| 20 | Golem de Cristal | **Núcleo de Cristal** | Martelo | 2 | 49 | Ondas de choque de cristal no ataque carregado |
| 25 | Serpente do Lodo | **Língua de Serpente** | Lança | 3 | 55 | Estocada dupla (cada estocada acerta 2 vezes) |
| 30 | Hidra do Pântano | **Arco da Hidra** | Arco | 3 | 43 | Dispara 3 flechas de uma vez |
| 35 | Escorpião Imperador | **Ferrão Imperial** | Besta | 4 | 101 | Virotes que envenenam e causam Lentidão |
| 40 | Faraó Eterno | **Khopesh do Faraó** | Espada | 4 | 72 | Matar um inimigo invoca 3 escaravelhos aliados (8 s) |
| 45 | Yeti Ancião | **Punhos do Yeti** | Manoplas | 5 | 56 | Cada golpe dá Frio |
| 50 | Dragão de Gelo | **Sopro Gélido** | Katana | 5 | 112 | O ataque carregado congela tudo numa linha de 6 m |
| 55 | Capitão Esqueleto | **Sabre do Afogado** | Espada | 6 | 138 | Cura 2% do dano feito |
| 60 | Leviatã | **Tridente do Leviatã** | Lança | 6 | 159 | Estocadas lançam uma onda de água (Encharcado) |
| 65 | Ferreiro Infernal | **Martelo da Forja** | Martelo | 7 | 306 | Golpes em chamas (Queimadura 30%) |
| 70 | Titã de Magma | **Coração de Magma** | Espada Grande | 7 | 324 | Ataque carregado faz uma explosão de lava (área 4 m) |
| 75 | Lich Bibliotecário | **Grimório Proibido** | Cajado | 8 | 228 mág. | Invoca 2 esqueletos aliados a cada 20 s |
| 80 | Rei Sem Coroa | **Lâmina do Rei Caído** | Espada Grande | 8 | 410 | Ignora a DEF dos inimigos |
| 85 | Grifo Real | **Pena de Grifo** | Arco | 9 | 254 | Flechas que perseguem o inimigo |
| 90 | Serafim Caído | **Foice do Serafim** | Foice | 9 | 367 | Golpes alternam Luz e Sombra; +30% contra o elemento oposto |
| 95 | Guardião do Tempo | **Segundo Parado** | Adaga | 10 | 209 | Inimigos perto de ti ficam 30% mais lentos |
| 100 | O Administrador | **Chave do Sistema** | Espada | 10 | 348 | Abre os Andares do Eco; +5% ATQ a cada 10 andares do Eco |

---

## 5. Armas de guardião (79)

Raridade **Épica** fixa. ATQ base = arma normal do tier da região × 1,1. Caem do **guardião** de cada andar
(descritos nos ficheiros das regiões). No andar 68 o "guardião" é o **Kai** (ver secção 7).

| Andar | Guardião | Arma | Tipo | Efeito |
|---|---|---|---|---|
| 1 | Coelho-Chifre Ancião | Chifre Partido | adaga | +10% velocidade de movimento |
| 2 | Coruja Sombria | Pena-Noturna | arco | +30% dano em inimigos que ainda não te viram |
| 3 | Lagostim Couraçado | Martelo Pinça | martelo | +30% dano a inimigos do tipo Tanque |
| 4 | Rainha dos Esporos | Esporo-Luz | cajado | os projéteis deixam esporos venenosos no chão |
| 6 | Abelha-Rainha Melífera | Ferrão-de-Mel | lança | 15% Veneno; matar um inimigo cura 2% HP |
| 7 | Guardião de Musgo | Tronco-Velho | espada grande | +15% HP máximo enquanto equipada |
| 8 | Cavaleiro de Pedra Musgosa | Lâmina do Cavaleiro Esquecido | espada | combo de 4 golpes em vez de 3 |
| 9 | Serpente da Névoa | Foice Bruma | foice | cada golpe tem 10% de te tornar invisível 1 s (os inimigos perdem-te) |
| 11 | Vagoneta Assombrada | Martelo Carril | martelo | o ataque carregado faz uma onda de choque em linha |
| 12 | Touro das Galerias | Chifre-Picareta | machado | também minera como uma picareta de tier 3 |
| 13 | Prisma Vivo | Cajado Prisma | cajado | cada projétil tem elemento ao acaso (Fogo, Gelo ou Raio) |
| 14 | Barqueiro Afogado | Remo do Barqueiro | lança | empurra muito; +20% dano em inimigos na água |
| 16 | Água-Viva Fúngica | Foice Micélio | foice | os golpes deixam esporos no chão que te curam 1% por segundo |
| 17 | Morcego-Rei dos Ecos | Besta Ressonante | besta | os virotes ressaltam para mais 1 inimigo |
| 18 | Sentinela Anã | Manoplas da Fornalha | manoplas | o 6.º golpe do combo causa Queimadura |
| 19 | Reflexo Negro | Lâmina Reflexo | katana | 15% de hipótese de o golpe se repetir (eco) |
| 21 | Garça-Lança | Bico da Garça | lança | +15% crítico |
| 22 | Lodo Tóxico | Cajado Lodoso | cajado | os projéteis deixam uma poça de veneno |
| 23 | Pantera de Jade | Garras de Jade | manoplas | ataques pelas costas fazem ×2 |
| 24 | Totem Vivo de Sssar | Machado Totémico | machado | matar um inimigo dá +5% ATQ por 10 s (acumula 3 vezes) |
| 26 | Caranguejo-Violinista Gigante | Pinça Maior | espada grande | +20% DEF enquanto carregas o ataque |
| 27 | Ninfa da Cascata | Arco Cascata | arco | as flechas deixam o alvo Encharcado |
| 28 | Grande Bugio | Martelo Bugio | martelo | os ataques carregados atordoam sempre |
| 29 | Dríade Corrompida | Foice de Espinhos | foice | 20% de causar Sangrar |
| 31 | Lagarto-Duna Gigante | Espinho da Duna | adaga | 10% de causar Sangrar |
| 32 | A Miragem | Cajado Miragem | cajado | 20% de criar uma cópia tua que distrai os inimigos 3 s |
| 33 | Abutre Rei | Arco do Abutre | arco | +25% dano em inimigos com menos de 30% de vida |
| 34 | Golem de Arenito | Martelo de Arenito | martelo | os golpes levantam areia que Cega 1 s |
| 36 | Djinn da Tempestade | Cimitarra do Vento | espada | os golpes lançam uma lâmina de vento (projétil de 4 m) |
| 37 | Cavaleiro de Ossos Montado | Lança do Cavaleiro de Ossos | lança | ataque carregado faz uma carga de 6 m |
| 38 | Esfinge Menor | Garras da Esfinge | manoplas | os críticos dão +10% de velocidade de ataque 3 s |
| 39 | Sacerdote-Chacal | Foice de Ouro do Sacerdote | foice | roubo de vida 5% |
| 41 | Morsa Gigante | Presas de Morsa | adaga | +20% dano em inimigos com Frio ou Congelados |
| 42 | Alce Fantasma | Arco de Chifre | arco | as flechas atravessam 1 inimigo |
| 43 | Kraken do Gelo | Lança Tentáculo | lança | as estocadas puxam o alvo para ti |
| 44 | Coração de Cristal Azul | Cajado Gélido | cajado | 25% de causar Frio |
| 46 | Wendigo | Foice do Wendigo | foice | 10% de causar Medo |
| 47 | Tartaruga-Glaciar | Martelo Glaciar | martelo | os golpes gelam o chão e os inimigos escorregam |
| 48 | Raposa Aurora | Katana Aurora | katana | os críticos libertam uma pequena explosão de Luz |
| 49 | Cavaleiro de Gelo | Lâmina do Cavaleiro Gélido | espada grande | +10% DEF e imune a Frio |
| 51 | Tartaruga-Marinha Anciã | Martelo Casco de Tartaruga | martelo | +15% DEF |
| 52 | Gaivota Gigante Ladra | Arco Gaivota | arco | flechas 30% mais rápidas e +10% velocidade de movimento |
| 53 | O Imediato Fantasma | Âncora do Imediato | martelo | o ataque carregado puxa os inimigos à volta para ti |
| 54 | Peixe-Leão Rei | Adaga Peixe-Leão | adaga | 25% de causar Veneno |
| 56 | Dragão-Marinho Folhado | Lança de Alga | lança | as estocadas deixam o alvo Encharcado |
| 57 | Golem de Coral | Manoplas de Coral | manoplas | cada golpe cura 1% do HP |
| 58 | Tamboril Abissal | Cajado Lanterna Abissal | cajado | ilumina 8 m e +15% dano no escuro |
| 59 | Guardião das Marés | Foice das Marés | foice | os golpes empurram uma onda à frente (área ×1,2) |
| 61 | Fénix de Cinza | Arco Fénix | arco | uma vez por dia, se morreres, renasces com 20% de vida |
| 62 | Serpente de Lava | Lança de Magma | lança | as estocadas deixam um rasto de fogo no chão |
| 63 | Ent Carbonizado | Machado Brasa-Viva | machado | 20% de causar Queimadura |
| 64 | Escavadora Anã Possuída | Martelo-Broca | martelo | minera como picareta de tier 8 e ignora 20% da DEF |
| 66 | Sapo-Vulcão | Manoplas Géiser | manoplas | o último golpe do combo atira o inimigo ao ar (atordoado) |
| 67 | Golem Portão de Obsidiana | Espada Grande Portão | espada grande | +20% DEF enquanto carregas o ataque |
| 69 | Sumo-Sacerdote das Chamas | Cajado do Sumo-Sacerdote | cajado | a Bola de Fogo tem +30% de área |
| 71 | Sentinela da Muralha | Arco da Sentinela | arco | as flechas ignoram 30% da DEF |
| 72 | O Pregoeiro Fantasma | Martelo-Sino | martelo | 10% de atordoar todos os inimigos à volta |
| 73 | Coveiro Ghoul | Pá-Machado do Coveiro | machado | também escava pontos de tesouro |
| 74 | Colosso de Ossos | Espada Grande de Ossos | espada grande | o ataque carregado lança 3 crânios que perseguem inimigos |
| 76 | Rainha das Rosas Negras | Adaga Rosa Negra | adaga | os críticos causam Maldição |
| 77 | Anjo Caído de Vitral | Katana Vitral | katana | cada golpe muda de elemento (Fogo → Gelo → Raio → Luz) |
| 78 | Carcereiro | Manoplas do Carcereiro | manoplas | o 6.º golpe prende o inimigo 1 s com uma corrente |
| 79 | Comandante dos Cavaleiros Caídos | Lança do Comandante | lança | +10% ATQ aos teus companheiros |
| 81 | Baleia das Nuvens | Arpão da Baleia | lança | ao acertar, puxa-te até ao alvo |
| 82 | Golem-Ilha | Martelo-Ilha | martelo | o ataque carregado lança uma rocha |
| 83 | Cavaleiro de Luz Sólida | Espada de Luz Sólida | espada | +15% velocidade de ataque |
| 84 | Jardineira Celeste | Foice da Jardineira | foice | cada inimigo que matas faz crescer uma flor que cura 5% |
| 86 | Leão Alado de Mármore | Manoplas do Leão | manoplas | +20% dano nos 3 primeiros golpes contra um alvo novo |
| 87 | Senhor dos Trovões | Katana Relâmpago | katana | o ataque carregado lança um raio em linha |
| 88 | Monge do Vento | Cajado do Vento | cajado | os projéteis empurram os inimigos |
| 89 | Carruagem do Sol | Arco do Sol | arco | de dia, +20% dano e Queimadura |
| 91 | Porteiro do Vazio | Chave-Espada do Porteiro | espada | 10% de abrir um portal que faz ×2 de dano |
| 92 | Baleia Estelar | Arpão Cometa | lança | o ataque carregado lança um cometa |
| 93 | Rainha dos Espelhos | Adaga Espelho | adaga | 15% de criar uma cópia tua que ataca 3 s |
| 94 | Eco dos Guardiões | Lâmina dos Ecos | katana | cada golpe usa um elemento ao acaso |
| 96 | Gigante Invertido | Martelo da Gravidade | martelo | o ataque carregado puxa os inimigos à volta para o centro |
| 97 | O Desistente | Arco do Desistente | arco | +30% dano quando tens menos de 50% de vida |
| 98 | Índice Vivo | Cajado do Índice | cajado | cada 5.º projétil é um feitiço de um boss ao acaso |
| 99 | O Guardião da Escada | Espada Grande da Escada Final | espada grande | +2% de dano por cada boss diferente que já venceste (máx. +40%) |

---

## 6. Armas secretas das masmorras escondidas (10)

Raridade **Lendária** fixa. ATQ base = arma normal do tier × 1,3.

| Região | Masmorra | Arma | Tipo | ATQ base | Efeito |
|---|---|---|---|---|---|
| 1 | Toca das Raízes (andar 7) | **Arco Raiz-Viva** | Arco | 14 | Flechas prendem com raízes (Lentidão 2 s, 20%) |
| 2 | Mina do Rei Anão (andar 18) | **Machado do Rei Sob a Montanha** | Machado | 44 | +25% dano a golems; minera como picareta de tier 5 |
| 3 | Santuário do Jaguar (andar 23) | **Katana Garra-do-Sol** | Katana | 57 | Ataque carregado solta uma onda de Luz (×1,5 contra mortos-vivos) |
| 4 | Túmulo do Dragão Antigo (andar 37) | **Espada Grande Osso-de-Dragão** | Espada Grande | 140 | +20% dano contra bosses |
| 5 | Cripta do Rei do Inverno (andar 47) | **Lança do Inverno Eterno** | Lança | 127 | Congela com 2 acumulações de Frio (em vez de 3) |
| 6 | Cofre do Almirante Afogado (andar 56) | **Besta Arpão do Almirante** | Besta | 209 | Virotes puxam os inimigos; sem perda debaixo de água |
| 7 | Forja Primordial (andar 64) | **Martelo Primordial** | Martelo | 332 | Ataque carregado cria uma erupção (área de fogo 4 m) |
| 8 | Cripta da Rainha (andar 73) | **Foice da Rainha Viúva** | Foice | 321 | Cada inimigo morto liberta um fantasma aliado (10 s) |
| 9 | Santuário das Asas Perdidas (andar 84) | **Lança Arcanjo** | Lança | 351 | Estocada de queda ×3 enquanto planas |
| 10 | O Andar Zero (andar 98) | **Katana do Erro** | Katana | 415 | 1% de cada golpe fazer 9 999 de dano |

---

## 7. Armas raras (monstros com nome e missões)

Raridade **Rara** (ou a indicada). ATQ base = arma normal do tier × 1,05.

| Arma | Tipo | Tier | ATQ base | Onde | Efeito |
|---|---|---|---|---|---|
| **Martelo de Vagoneta** | Martelo | 2 | 43 | Rei Goblin Gruk (monstro com nome) | Ondas de choque pequenas |
| **Lança Tribal de Aço** | Lança | 3 | 48 | Homem-Lagarto Renegado (5%) | +10% dano na água |
| **Lança de Ssark** | Lança | 3 | 48 | missão R3_03 | +15% DEF |
| **Arco Tribal de Aço** | Arco | 3 | 38 | missão R3_05 | +10% crítico |
| **Cimitarra do Sultão** | Espada | 4 | 63 | Sultão Bandido Kasim (monstro com nome) | Combo de 4 golpes |
| **Cimitarra Velha de Prata** | Espada | 4 | 63 | Esqueleto Guerreiro (3%) | +15% dano a mortos-vivos |
| **Arco de Gelo Eterno** | Arco | 5 | 80 | missão R5_05 (Épico) | Flechas dão Frio |
| **Besta Pesada de Gelo Eterno** | Besta | 5 | 125 | missão R5_14 (Épico) | Virotes atravessam 2 inimigos |
| **Foice-Tesoura** | Foice | 8 | 259 | O Jardineiro (monstro com nome) | Cortes duplos |
| **Besta de Mitril Abençoada** | Besta | 8 | 279 | missão R8_07 (Épico) | Elemento Luz |
| **Lança Relâmpago** | Lança | 9 | 284 | Valquíria Sigrun (monstro com nome) | Estocadas com Choque |
| **Lâmina do Kai** | Espada | 7 | 158 | vencer o Kai até ao fim (andar 68) | +20% velocidade de ataque |

---

## 8. Armas de amizade (5)

Dadas por NPCs com **10 corações** (ver `docs/NPCS.md`). **Crescem contigo**: o ATQ acompanha o teu nível.

| Arma | Tipo | De quem | Como é |
|---|---|---|---|
| **A Décima Milésima** | Espada | Brom (10 ❤️) | ATQ igual ao de uma espada do teu nível × 1,3; ganha um efeito novo a cada 10 níveis |
| **Arco da Mia** | Arco | Mia (10 ❤️) | ATQ igual ao de um arco do teu nível × 1,2; a Mia faz +20% de dano |
| **Lâmina Gémea** | Espada | Kai (10 ❤️, só se o salvaste) | Com o Kai na equipa, ambos fazem +20% |
| **Machado da Equipa** | Machado | Gorvan (10 ❤️) | +5% de dano por cada companheiro contigo |
| **Lança da Capitã** | Lança | Freya (10 ❤️) | +10% DEF; a investida atordoa |

---

## 9. Armas míticas (12)

Raridade **Mítica** fixa. ATQ base = arma Estelar × 1,5. Fazem-se na **Forja Estelar** (Dorn, andar 91) e o
**Brom** dá o toque final (missão R10_11).

**Receita de cada mítica**: 10 Lingote Estelar + 1 **Coração Estelar** (Devorador Ancestral) + 1 **Gema Prismática**
(andar 94) + 5 **Fragmento de Sistema** + o **troféu** de um boss do mesmo tipo de arma + 50 000 ouro.

| Arma | Tipo | ATQ base | Poder |
|---|---|---|---|
| **Aurora do Primeiro Dia** | Espada | 435 | Golpes libertam luz; as skills de espada recarregam 30% mais depressa |
| **Fim dos Mundos** | Espada Grande | 783 | O ataque carregado parte o chão numa área enorme com todos os elementos |
| **Sussurro do Vazio** | Adaga | 261 | Os críticos teletransportam-te para trás do inimigo seguinte |
| **Lua de Mil Anos** | Katana | 478 | O ataque carregado para o tempo 1 s à tua volta |
| **Raiz do Mundo** | Machado | 609 | Cada golpe cura 2%; corta qualquer árvore ou rocha de um golpe |
| **Coração da Torre** | Martelo | 740 | Os golpes fazem tremer o andar: 20% de atordoar tudo a 8 m |
| **Agulha do Céu** | Lança | 500 | A estocada carregada atravessa tudo numa linha de 15 m |
| **Ceifeira de Estrelas** | Foice | 566 | Cada inimigo morto dá +2% ATQ até saíres do andar (máx. +40%) |
| **Arco-Íris Eterno** | Arco | 392 | Cada flecha tem um elemento diferente e ressalta 2 vezes |
| **Cometa Final** | Besta | 609 | O virote carregado cai como um cometa (área de 6 m) |
| **Voz do Sistema** | Cajado | 435 mág. | Projéteis em leque de 3; depois de um crítico, feitiços sem custo durante 5 s |
| **Punhos de Aren** | Manoplas | 239 | O combo nunca acaba; cada 10.º golpe faz ×3 |

---

## 10. Ferramentas

Não são armas: servem para recolher. Têm **tier** (uma Picareta de Cobre não parte minério de Prata).

| Ferramenta | Tiers | Para quê | Onde |
|---|---|---|---|
| Picareta | Cobre → Estelar (10) | minério, cristais, gemas | Brom (receita: 3 lingotes + 1 madeira) |
| Machado de lenhador | Cobre → Estelar (10) | madeira | Brom (3 lingotes + 2 madeira) |
| Cana de pesca | Bambu · Mangue · Prata · Coral · Cana do Pip | pescar (melhor cana = minijogo mais fácil) | Pip, missões |
| Cana Ignífuga | 1 | pescar na lava | Mestre Ragnar (andar 64) |
| Arpão | 1 | peixes grandes (Narval Real) | missão R5_09 |
| Pá | Pá · Pá de Prata · Pá Dourada | escavar portas soterradas e pontos de tesouro | Beto (andar 34), missões |
| Regador | Lata · Cobre · Ouro (3×3) | regar a quinta | Hana |
| Faca de Mergulho | 1 | abrir ostras | Ama Kaia (andar 54) |
| Gancho | 1 | atravessar buracos e chegar a sítios altos | missão R2_02 |
| Capa Planadora | 1 | planar | missão R9_01 |
