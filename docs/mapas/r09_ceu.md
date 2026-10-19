# Mapas — Região 9: Céu (andares 81–90)

Mapas vistos de cima. Legenda e regras: [`README.md`](README.md). O que há em cada andar: `docs/regioes/r09_ceu.md`.
No Céu quase não há chão: o **espaço em branco** é **céu aberto** (quem cai é apanhado pelas nuvens e volta à última
plataforma com −10% de HP). `nn` são **nuvens sólidas** (ou negras, no 87), `cc` são **nuvens fracas** (desfazem-se
2 s depois de as pisares), `↑↑` são **correntes de ar** ou túneis de vento, e `==` são pontes de luz, correntes grossas
ou pontes de corda (ver cada andar). Planar com a **Capa Planadora** (R9_01, andar 82) leva-te por cima do vazio.

---

## Andar 81 — Mar de Nuvens

Tamanho: **300×300 m** · 30×30 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d 
  1                                                              
  2                              nnnnnn                          
  3        nnnnnnnnnnnnnn      nn..>>..nn      nnnnnnnnnnnnnn    
  4        nnnnnnnnnnnnnn    nn....GG....nn    nnnnnnnnnnnnnn    
  5        nnnnnnnnnnnnnn    nn..........nn    nnnnnnnnnnnnnn    
  6        nnnnnnnnnnnnnn    nn..........nn    nnnnnnnnnnnnnn    
  7        nnnnnnnnnnnnnn      nn......nn      nnnnnnnnnnnnnn    
  8        nnnnnnnnnnnnnn        nnnnnn                          
  9                                nn                            
 10                              ..nn..                          
 11                            ..........                  ..    
 12              ..nnnnnnnnnnnnnnrr....==================..??..  
 13            ..rr..          ..........                  ..    
 14              ..nn    cc      ......                          
 15                nn    cc        cc                            
 16              ↑↑nn    cc        cc                            
 17              ↑↑nn    cccccccccccc                            
 18              ↑↑nn              cc                            
 19            ....nn              cccccccccccccccc              
 20          ..........            !!                            
 21          ..rr......            nn                            
 22          ..........            nn                            
 23            ......              nn                            
 24                                nn                            
 25                              ......                          
 26                            ......SS..                        
 27                            ..........                        
 28                            ....EE..PP                        
 29                              ......                          
 30                                                              
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | P28 | Chegada (escada do andar 80), no Ilhéu de Chegada (cena C9-01) |
| `SS` | Q26 | Zona Segura (braseiro dourado e cristal) |
| `GG` | P4 | Baleia das Nuvens (guardião): nada à volta do ilhéu final |
| `>>` | P3 | Escada para o andar 82 |
| `??` | b12 | **Fim do arco-íris**: o pote de ouro (10 000 ouro, uma vez) só aparece no evento Arco-Íris Duplo |
| `PP` | R28 | Página 81, debaixo de uma pedra na ponta do ilhéu, virada para o vazio |
| `!!` | P20 | Início do puzzle das **nuvens fracas** (as que piscam primeiro desfazem-se primeiro) |
| `rr` | O12, G13, F21 | Flor-do-Vento e Fio de Nuvem (à noite, às vezes, uma Estrela Cadente) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Ilhéu de Chegada | à volta de P27 | Nuvem Viva | Flor-do-Vento |
| Caminho de Nuvens Sólidas | coluna P, linhas 8–24 | Harpia | — |
| Nuvens Fracas (puzzle) | P15–P19, K14–P17, P19–W19 | Harpia | — |
| Ponte Arco-Íris | R12–Z12 | Elemental de Ar | — |
| Nuvens de Tempestade | D3–J8 e V3–b7 | Elemental de Ar, Nuvem Viva (cinzentas) | Fio de Nuvem |

**Caminho principal:** `EE` → nuvens sólidas `nn` → puzzle das nuvens fracas `cc` (os ramos para leste, P19–W19, e para oeste, até K14, desfazem-se no vazio: são os caminhos errados) → ilhéu do meio → `nn` → ilhéu final → `GG` → `>>`.

**Notas para construir:** Este é o primeiro andar sem chão à volta: o espaço vazio (`  `) é **céu aberto** — quem cai é apanhado pelas nuvens e volta à última plataforma com −10% de HP. `nn` são **nuvens sólidas** (brancas, pisam-se), `cc` são **nuvens fracas** (cinzentas, desfazem-se 2 s depois de as pisares, voltam 5 s depois), `↑↑` é uma **corrente de ar** (com a Capa Planadora leva-te para cima; antes dela, empurra-te só um bocadinho). A Ponte Arco-Íris é sólida e escorregadia.

---

## Andar 82 — Ilhas Flutuantes

Tamanho: **300×300 m** · 30×30 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d 
  1                                                              
  2                            ......                            
  3                          ....>>....                          
  4                          ..........            ......        
  5          ......          ....GG....          ..........      
  6        ..........          ......          ....rr........    
  7      ....FF........          ==            ==............    
  8      ............==          ==            ==......rr....    
  9      ........FF..==          ==            ==..........      
 10        ..........==        ..==..          ==  ......        
 11          ......  ==    ......CC......      ==                
 12                  ==  ..CC..........CC..    ==                
 13                  ==  ........@@........======                
 14                  ====............@@....!!                    
 15                    ......@@..........JJPP                    
 16                  ====................@@!!                    
 17                  ==  ......@@..@@......!!                    
 18                  ==  ..CC..........CC..                      
 19          ......  ==    ......@@......                        
 20        ..........==        ......                            
 21      ........FF..==          ==                ......        
 22      ....FF......==          ==              ..........      
 23      ..............          ==              ..........      
 24        ..........            ==              ..........      
 25          ......            ..==..              ......nnnnnn  
 26                          ..........                nnnnnnnn  
 27                          ......SS..                nnnn??nn  
 28                          ....EE....                nnnnnnnn  
 29                            ......                    nnnnnn  
 30                                                              
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | O28 | Chegada (escada do andar 81), na ilha de chegada |
| `SS` | P27 | Zona Segura |
| `GG` | O5 | Golem-Ilha (guardião) |
| `>>` | O3 | Escada para o andar 83 |
| `??` | b27 | **Ilha escondida dentro de uma nuvem** (só se chega a planar): casa abandonada de um Jogador, o diário dele e um baú de ouro |
| `PP` | T15 | Página 82, enrolada na corda de um balão velho no porto |
| `!!` | T14, T16, T17 | Os 3 guinchos (puzzle: puxar a ilha solta Y23 até à ponte) |
| `@@` | O13 | Imperatriz Celestia (palácio) |
| `@@` | Q14 | Brisa (loja) |
| `@@` | M15 | Ferreira Ícara (Forja de Oricalco) |
| `@@` | S16 | Cúmulo (ateliê) |
| `@@` | N17 | Pena (à beira da praça, a olhar para cima) |
| `@@` | P17 | Zéfiro (campo dos aros, R9_01) |
| `@@` | O19 | Estalagem das Cúpulas |
| `rr` | X6, Z8 | Minério de Oricalco |
| `FF` | E7, G9, G21, E22 | Pessegueiros (Pêssego Celeste) e árvores-nuvem (Madeira-Nuvem) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Aerópolis | à volta de O15 | — (povoação) | lojas |
| Ilhas de Pomares | à volta de F8 e F22 | Nuvem Viva | Pêssego Celeste, Madeira-Nuvem |
| Ilhas de Pedra | à volta de Y7 | Pássaro-Trovão | Minério de Oricalco |
| Correntes | as `==` | Harpia | — |

**Caminho principal:** `EE` → corrente `==` → Aerópolis → corrente para norte (O7–O10) → `GG` → `>>`.

**Notas para construir:** As `==` deste andar são **correntes grossas**: anda-se por cima delas e o vento abana (equilíbrio). Os balões do Nimbo ligam todas as ilhas depois de R9_02. A ilha solta (Y23) fica a flutuar longe até se rodarem os 3 guinchos `!!`; depois encosta à corrente e dá um atalho para as Ilhas de Pedra.

---

## Andar 83 — Pontes de Luz

Tamanho: **240×240 m** · 24×24 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X 
  1                                                  
  2                        >>                  ..    
  3                      ......              ..??..  
  4                        GG                  ..    
  5          ..            ==            ..    ==    
  6        ..!!..          ==          ..!!======    
  7          ==            ==            ==          
  8        ==========      ==  ============          
  9        ======  ==      ==  ==                    
 10        ==  ==  ======......==                    
 11        ==  ==        ....rr==                    
 12                    ==..PP....==                  
 13                    ==rr......==                  
 14          ============..!!..  ==========          
 15          ==            ==            ==          
 16          ==            ==            ==          
 17          ==            ==            ==          
 18        ..!!..          ==          ..!!..        
 19          ==            ==            ==          
 20          ==            ==            ==          
 21          ==            ==            ==          
 22          ============SS================          
 23                        EE                        
 24                                                  
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | L23 | Chegada (escada do andar 82), no primeiro pilar |
| `SS` | K22 | Zona Segura |
| `GG` | L4 | Cavaleiro de Luz Sólida (guardião) |
| `>>` | L2 | Escada para o andar 84 |
| `??` | V3 | Pilar escondido: a ponte (T6–V4) **só aparece no escuro** (à noite, com a música parada) e leva a um baú de ouro |
| `PP` | L12 | Página 83, encostada ao último refletor da Plataforma Central (aparece quando a luz chega lá) |
| `!!` | E6 | Refletor de cristal 1 |
| `!!` | S6 | Refletor 2 |
| `!!` | L14 | Refletor 3 |
| `!!` | E18 | Refletor 4 |
| `!!` | S18 | Refletor 5 (o último: leva a luz até à Plataforma Central) |
| `rr` | M11, K13 | Cristal Celeste e Minério de Oricalco |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Pilares de Cristal | os seis pilares | Golem Celeste | Cristal Celeste |
| Pontes de Luz | as `==` | Elemental de Ar | — |
| Labirinto de Luz | D8–J11 | Nuvem Viva | — |
| Plataforma Central | à volta de L12 | Golem Celeste | Minério de Oricalco |

**Caminho principal:** `EE` → ponte L21–L15 (em ritmo) → Plataforma Central → refletores → ponte N11–S7 até ao refletor 4 → ponte L9–L4 → `GG` → `>>`.

**Notas para construir:** As `==` deste andar são **pontes de luz**: ligam-se e desligam-se ao ritmo da música (4 tempos ligadas, 2 desligadas). A ponte L9–L4 só se acende quando os 5 refletores levam a luz à Plataforma Central. O Labirinto de Luz troca de forma a cada compasso: no mapa está a forma da primeira batida.

---

## Andar 84 — Jardim Suspenso

Tamanho: **260×260 m** · 26×26 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
  1                nn                                    
  2        nn      nn                                    
  3      nnHHnn    ww                                    
  4        nn      ww                                    
  5                    ......>>........  CCCCCC          
  6                    ....FF....FF....  CCPPCC          
  7                    ........GG......==CCCCCC          
  8                    ................  CCCCCC          
  9                    ................                  
 10            ww......!!............!!......ww          
 11            ww............******..........ww          
 12            ww..FF........******....FF....ww          
 13            ww............******..........ww          
 14            ww............................ww          
 15          wwww............................wwww        
 16          ....!!........................!!....        
 17          ....................................        
 18          ......FF....**********......FF......        
 19          ..rr........**********..........rr..        
 20          ............**********..............        
 21          ....FF......**********........FF....        
 22          ..................SS................        
 23          ................EE..................        
 24                                                      
 25                                                      
 26                                                      
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | M23 | Chegada (escada do andar 83), no terraço de baixo |
| `SS` | N22 | Zona Segura |
| `GG` | N7 | Jardineira Celeste (guardiã) |
| `>>` | M5 | Escada para o andar 85 |
| `PP` | T6 | Página 84, dentro de um vaso vazio na Estufa |
| `!!` | J10 | Comporta 1 |
| `!!` | Q10 | Comporta 2 |
| `!!` | G16 | Comporta 3 |
| `!!` | T16 | Comporta 4 (puzzle: desviar as cascatas para regar as 4 árvores secas, que dão frutos dourados) |
| `rr` | F19, U19 | Algodão-Nuvem e Uva Celeste |
| `FF` | L6 | Árvore seca 1 (puzzle da rega) |
| `FF` | O6 | Árvore seca 2 |
| `FF` | H12 | Pessegueiro |
| `FF` | R12 | Pessegueiro |
| `FF` | H18 | Árvore seca 3 |
| `FF` | S18 | Árvore seca 4 |
| `FF` | G21 | Pessegueiro |
| `FF` | T21 | Pessegueiro |
| `HH` | D3 | **Santuário das Asas Perdidas** (masmorra escondida): ilha escondida nas nuvens; só se chega planando a partir do topo da cascata mais alta (H2) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Terraços | E16–V23, G10–T15, J5–Q9 | Valquíria, Nuvem Viva | Flor-do-Vento |
| Cascatas para o Vazio | as `ww` | Serpente Alada | Truta Celeste |
| Pomar Celeste | os pessegueiros | Nuvem Viva | Pêssego Celeste |
| Estufa das Estrelas | S5–U8 | — | — |

**Caminho principal:** `EE` → terraço de baixo → rampa para o 2.º terraço → 3.º terraço → `GG` → `>>`.

**Notas para construir:** Os três terraços estão a alturas diferentes (cada um 6 m acima do outro), ligados por escadas de pedra nas pontas. As `ww` são **cascatas que caem para o vazio**: atravessá-las empurra-te para a borda. A cascata mais alta (H2–H4) nasce numa nuvem: do topo dela, a planar para oeste, chega-se à ilha do Santuário.

---

## Andar 85 — Ninho dos Grifos

Tamanho: **200×200 m** · 20×20 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T 
  1                                          
  2                                          
  3                                          
  4                ########>>########        
  5                ####..BBBBBB..####        
  6                ####..BBBBBB..####        
  7                ####..........####        
  8                ############==####        
  9                            ==            
 10      ######################::########    
 11      ##########vv##########::####vv##    
 12      ######::::::::::::::::::::::####    
 13      ######::rr################::####    
 14      ##vv##::################rr::####    
 15      ##::PP::::::::::##########vv####    
 16      ##ii##########::################    
 17      ##############::SS##############    
 18      ##############EE################    
 19                                          
 20                                          
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | J18 | Chegada (escada do andar 84), no fundo dos penhascos |
| `SS` | K17 | Zona Segura (numa gruta pequena) |
| `>>` | L4 | Escada para o andar 86 (abre depois do mini-boss) |
| `BB` | K5, L5, M5, K6, L6, M6 | Pico do Grifo Real: **Grifo Real** (mini-boss), com o ninho dele |
| `PP` | E15 | Página 85, num ninho vazio, por baixo de uma casca de ovo partida |
| `rr` | G13, O14 | Minério de Oricalco e Pena de Grifo |
| `ii` | D16 | **Ovo abandonado** caído fora do ninho (missão R9_04 → Grifo Bebé) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Penhascos | C10–R18 | Harpia, Pássaro-Trovão | Minério de Oricalco |
| Ninhos | os `vv` | Harpia | Pena de Grifo |
| Pico do Grifo Real | H4–P8 | — | — |

**Caminho principal:** `EE` → trilho `::` em ziguezague pelos penhascos (sem tocar nos ninhos) → ponte de corda N8–N9 → `BB` → `>>`.

**Notas para construir:** Os `##` são **rocha de penhasco** (sobe-se só pelo trilho). O vento forte empurra para oeste nas partes abertas do trilho e na ponte de corda. O ovo abandonado (D16) está num desvio do trilho, perto de um ninho: para o levar sem passar ao pé de outro ninho, volta-se pelo mesmo caminho.

---

## Andar 86 — Ruínas Celestes

Tamanho: **260×260 m** · 26×26 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
  1                                                      
  2                                                      
  3                    ##############                    
  4                  ..##....@@....##..                  
  5              ......##..@@PP@@..##......              
  6            ........##....[]....##........            
  7          ..##............::............##..          
  8          ######..........::..........######          
  9        rr..##....MM......::......MM....##....        
 10        ..................::..................        
 11      ..##########........::....................      
 12      ..##..>>..##........::......MM............      
 13      ..##..GG............::....................      
 14      ..##......##........::......""""""""""""rr      
 15      ..##########........::......""::::::::""..      
 16        ..................::......""::::::::""        
 17        ....##....MM......::......""::AA::::""        
 18          ######..........::......""::::::::""        
 19          ..##............::......""::::::::""        
 20            ..............::......""""""""""""        
 21              ............::............              
 22                  ........::SS......                  
 23                      ....EE....                      
 24                                                      
 25                                                      
 26                                                      
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `AA` | S17 | **Anfiteatro**: à noite, a peça dos fantasmas sobre o primeiro Jogador (cena C9-03, página especial "A Peça do Primeiro") |
| `EE` | M23 | Chegada (escada do andar 85), na ponta sul da ilha |
| `SS` | N22 | Zona Segura |
| `GG` | F13 | Leão Alado de Mármore (guardião), no Templo Partido |
| `>>` | F12 | Escada para o andar 87 |
| `PP` | M5 | Página 86, entalada no telescópio grande |
| `@@` | M4 | Astrónoma Vega (o telescópio grande, cena C9-04) |
| `@@` | L5 | Velho Altair (varanda) |
| `@@` | N5 | Orion (loja) |
| `rr` | D9, W14 | Mármore Celeste, Cristal Celeste, Minério de Oricalco |
| `MM` | I9, Q9, Q12, I17 | As 5 estátuas que apontam para as constelações (puzzle e missão R9_06) |
| `[]` | M6 | Porta do Observatório Celeste |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Colunatas Brancas | à volta de F8, F18, T8, T18 | Golem Celeste, Serpente Alada | Mármore Celeste |
| Observatório Celeste | J3–P6 | — (povoação) | loja |
| Anfiteatro | Q14–V20 | Anjo Guardião (de dia) | — |
| Templo Partido | D11–H15 | Anjo Guardião | Cristal Celeste |

**Caminho principal:** `EE` → caminho `::` para norte → Observatório (à direita, o Anfiteatro) → oeste → Templo Partido → `GG` → `>>`.

**Notas para construir:** **Gravidade baixa** em todo o andar: saltas o dobro e cais devagar. Os `##` das colunatas são colunas partidas a flutuar (saltar de coluna em coluna até ao templo é um desafio). No Anfiteatro, os `""` são os degraus de pedra onde te sentas.

---

## Andar 87 — Tempestade Eterna

Tamanho: **260×260 m** · 26×26 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
  1                                                      
  2    nnnnnnnnnnnnnnnnnn....>>....nnnnnnnnnnnnnnnnnnnn  
  3    nnnnnnnnnnnnnnnnnn....GG....nnnnnnnnnnnnnnnnnnnn  
  4    nnnnnnnnnnnnnnnnnn..........nnnnnnnnnnnnnnnnnnnn  
  5    nnnnnn......nnnnnnnn..::..nnnnnnnn......nnnnnnnn  
  6    nnnn......rr..nnnnnnnn::nnnnnnnn..........nnnnnn  
  7    nnnn..........nnnnnnnn[]nnnnnnnn..........nnnnnn  
  8    nnnn..vv......nnnnnnnn::nnnnnnnn......vv..nnnnnn  
  9    nnnnnn..::..nnnnnnnnnn::nnnnnnnnnn..::..nnnnnnnn  
 10    nnnnnnnn::nnnnnnnnnn......nnnnnnnnnn::nnnnnnnnnn  
 11    nnnnnnnn::::::::::..........::::::::::nnnnnnnnnn  
 12    nnnnnnnnnnnnnnnn..............nnnnnnnnnnnnnnnnnn  
 13    nnnnnnnnnnnnnnnn......??PP....nnnnnnnnnnnnnnnnnn  
 14    nnnnnnnnnnnnnnnn..............nnnnnnnnnnnnnnnnnn  
 15    nnnnnnnn::::::::::..........::::::::::nnnnnnnnnn  
 16    nnnnnnnn::nnnnnnnnnn......nnnnnnnnnn::nnnnnnnnnn  
 17    nnnnnnnn::nnnnnnnnnnnn::nnnnnnnnnnnn::nnnnnnnnnn  
 18    nnnnnn..::..nnnnnnnnnn::nnnnnnnnnn..::..nnnnnnnn  
 19    nnnn..vv......nnnnnnnn::nnnnnnnn......vv..nnnnnn  
 20    nnnn..........nnnnnnnn::nnnnnnnn..........nnnnnn  
 21    nnnn..........nnnnnnnn::nnnnnnnn..rr......nnnnnn  
 22    nnnnnn......nnnnnnnnnn::nnnnnnnnnn......nnnnnnnn  
 23    nnnnnnnnnnnnnnnnnnnnnn::SSnnnnnnnnnnnnnnnnnnnnnn  
 24    nnnnnnnnnnnnnnnnnnnn..EE..nnnnnnnnnnnnnnnnnnnnnn  
 25    nnnnnnnnnnnnnnnnnnnnnn..nnnnnnnnnnnnnnnnnnnnnnnn  
 26                                                      
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | M24 | Chegada (escada do andar 86) |
| `SS` | N23 | Zona Segura (debaixo de um para-raios pequeno) |
| `GG` | M3 | Senhor dos Trovões (guardião) |
| `>>` | M2 | Escada para o andar 88 |
| `??` | M13 | **Olho da Tempestade**: calmo, sem chuva; o **sino de vento** acalma a tempestade 10 minutos |
| `PP` | N13 | Página 87, pendurada no sino de vento do Olho da Tempestade (o papel está seco: ali não chove) |
| `rr` | G6, S21 | Topázio e Pena Elétrica |
| `[]` | M7 | Porta elétrica (abre com os raios encaminhados pelas torres) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Nuvens Negras | todo o `nn` | Nuvem Viva (cinzentas), Pássaro-Trovão | Gota de Chuva Celeste |
| Ilhas Eletrificadas | as 4 ilhas dos cantos | Elemental de Ar, Serpente Alada | Topázio |
| Para-raios | as `vv` | — | — |
| Olho da Tempestade | à volta de M13 | — | — |

**Caminho principal:** `EE` → trilho para norte → Olho da Tempestade → puzzle das torres → porta elétrica `[]` → `GG` → `>>`.

**Notas para construir:** Aqui as `nn` são **nuvens negras** (sólidas, mas com chuva constante: estás sempre Encharcado). Os raios caem com uma marca no chão 1 s antes; perto de um `vv` (5 m) estás protegido. No Olho da Tempestade não chove nem cai nenhum raio.

---

## Andar 88 — Templo dos Ventos

Tamanho: **240×240 m** · 24×24 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X 
  1                                                  
  2                                                  
  3      ########################################    
  4      ##↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑##    
  5      ##↑↑################################↑↑##    
  6      ##↑↑########......CC........########↑↑##    
  7      ##↑↑##....##......GG>>......########↑↑##    
  8      ##↑↑##??....................########↑↑##    
  9      ##↑↑##..PP##................rr######↑↑##    
 10      ##↑↑##....##................########↑↑##    
 11      ##↑↑##############↑↑################↑↑##    
 12      ##↑↑##############↑↑################↑↑##    
 13      ##↑↑##############↑↑################↑↑##    
 14      ##↑↑................................↑↑##    
 15      ####..!!......!!........!!......!!..####    
 16      ####rr..............................####    
 17      ####............@@....@@............####    
 18      ####................................####    
 19      ####..!!........................!!..####    
 20      ####................SS..............####    
 21      ##################EE####################    
 22                                                  
 23                                                  
 24                                                  
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | L21 | Chegada (escada do andar 87), à porta do templo |
| `SS` | M20 | Zona Segura |
| `GG` | L7 | Monge do Vento (guardião), no Campanário |
| `>>` | M7 | Escada para o andar 89 |
| `??` | F8 | **Sala do Silêncio**: o gongo faz parar os moinhos e mostra uma passagem |
| `PP` | G9 | Página 88, por baixo do gongo da Sala do Silêncio |
| `!!` | F15 | Moinho 1 (bandeira branca) |
| `!!` | J15 | Moinho 2 (azul) |
| `!!` | O15 | Moinho 3 (verde) |
| `!!` | S15 | Moinho 4 (amarela) |
| `!!` | F19 | Moinho 5 (vermelha) |
| `!!` | S19 | Moinho 6 (negra) — puzzle e R9_14 |
| `@@` | K17, N17 | Monges do Vento (esteiras, chá; dão R9_14) |
| `rr` | Q9, E16 | Flor-do-Vento, Essência de Ar e Minério de Oricalco |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Pátio dos Moinhos | E14–T20 | Harpia, Valquíria | Flor-do-Vento |
| Túneis de Vento | os `↑↑` | Elemental de Ar | Essência de Ar |
| Campanário | I6–P10 | Anjo Guardião | — |
| Sala do Silêncio | F7–H10 | — | — |

**Caminho principal:** `EE` → Pátio → rodar os moinhos pela ordem das bandeiras → túnel de vento (D14 → D4 → U4) ou o do meio (L13–L8) → Campanário → `GG` → `>>`.

**Notas para construir:** Os `##` são o **templo de pedra clara** (por dentro, corredores estreitos). Os `↑↑` são **túneis de vento**: entras e o vento leva-te como um tubo, na direção que os moinhos mandam. Com os moinhos errados, o túnel do meio atira-te de volta para o pátio.

---

## Andar 89 — Escadaria do Sol

Tamanho: **200 m de largura · 300 m de subida** · 20×30 células de 10 m · norte em cima = o topo da escadaria

```
     A B C D E F G H I J K L M N O P Q R S T 
  1                                          
  2              ........>>......            
  3              ......GG........            
  4              ................            
  5                  ^^^^^^^^                
  6                  ^^^^^^^^                
  7                  [][][][]                
  8                  ^^^^^^^^                
  9          ..!!................!!..        
 10          ..........!!............        
 11                  ^^^^^^^^                
 12                  ^^^^^^^^                
 13                  ^^^^^^^^                
 14      ....MM....................MM        
 15      ..PP??......................        
 16      ....        ^^^^rr^^                
 17                  ^^^^^^^^                
 18                  ^^^^^^^^                
 19          MM....................MM        
 20          ........................        
 21                  ^^^^^^^^                
 22                  ^^^^^^^^                
 23                  ^^^^^^^^                
 24          ..rr....................        
 25          ....................rr..        
 26                  ^^^^^^^^                
 27                  ^^^^^^^^                
 28              ................            
 29              ......EESS......            
 30                                          
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | J29 | Chegada (escada do andar 88), na Base (cena C9-05: "Estás quase. Não pares.") |
| `SS` | K29 | Zona Segura |
| `GG` | J3 | Carruagem do Sol (guardião): desce a escadaria de tempos a tempos |
| `>>` | K2 | Escada para o andar 90 |
| `??` | E15 | Pôr uma Pena Celeste na estátua sem asa abre uma sala lateral com um baú de ouro |
| `PP` | D15 | Página 89, na sala secreta da estátua sem asa |
| `!!` | F9 | Relógio de sol 1 |
| `!!` | O9 | Relógio de sol 2 |
| `!!` | J10 | Relógio de sol 3 (puzzle: pôr as sombras na hora certa com espelhos) |
| `rr` | K16, F24, O25 | Pedra-Sol, Diamante e Minério de Oricalco |
| `MM` | E14, P14, E19, P19 | Estátuas de anjos nos patamares (a de E14, no 3.º patamar, **não tem uma asa**) |
| `[]` | I7, J7, K7, L7 | **Portões Dourados** (abrem com os 3 relógios) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Base | G28–N29 | — | — |
| Patamares | linhas 9–10, 14–15, 19–20, 24–25 | Anjo Guardião, Valquíria | Diamante |
| Escadaria | I4–L28 | Golem Celeste, Serpente Alada | Pedra-Sol |
| Portões Dourados | I7–L7 | — | — |
| Topo | G2–N4 | — | — |

**Caminho principal:** `EE` → subir a escadaria `^^` de patamar em patamar (fugir para os lados quando a Carruagem desce) → relógios de sol → Portões Dourados → Topo → `GG` → `>>`.

**Notas para construir:** Os `^^` são **degraus dourados** (cada linha do mapa sobe 10 m). Os **patamares** são largos: as pontas (colunas E–F e O–P) são os **refúgios** onde a Carruagem do Sol não passa. Há 5 patamares no jogo: o 1.º é a Base. O sol gigante está no fundo, a norte, e não aquece.

---

## Andar 90 — Palácio Celeste

Tamanho: **220×220 m** · 22×22 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V 
  1                                              
  2            nnnnnnnnnnnnBBBBPP......          
  3            nnnnnnnnnnnnBBBB........          
  4            ........................          
  5            ############..##########          
  6            ##....vv..vv..vv..vv..##          
  7            ##....................##          
  8            ##....................##          
  9            ##....................##          
 10            ############[]##########          
 11        ................................      
 12        ..rr............::..........rr..      
 13        ................::..............      
 14        ..********......::....********..      
 15        ..********......::....********..      
 16        ..********......::....********..      
 17        ..********......::....********..      
 18        ..********......::....********..      
 19        ................::SS............      
 20        ................EE..............      
 21                                              
 22                                              
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | L20 | Chegada (escada do andar 89), nos Jardins do Palácio |
| `SS` | M19 | Zona Segura (a última antes do boss) |
| `BB` | L2, M2, L3, M3 | Varanda do Fim: **Serafim Caído** (boss) (cenas C9-06 e C9-07) |
| `PP` | N2 | Página 90 (**tinta azul**), presa entre duas penas brancas (aparece depois da cena C9-07) |
| `rr` | E12, R12 | Diamante e Cristal Celeste |
| `[]` | L10 | Porta do Salão dos Tronos Vazios |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Jardins do Palácio | D11–S20 | Anjo Guardião, Valquíria | Diamante |
| Salão dos Tronos Vazios | F5–Q10 | Golem Celeste | — |
| Varanda do Fim | F2–Q4 | — | — |

**Caminho principal:** `EE` → caminho dos jardins → Salão dos Tronos Vazios → Varanda do Fim → `BB`. A escada para o andar 91 aparece no fim da cena C9-07, onde estava o Serafim.

**Notas para construir:** Na Varanda, metade do chão é de **luz** (colunas L–Q) e metade de **sombra** (F–K): no mapa, a metade de sombra está marcada com `nn` (não é nuvem: é sombra que não vem de lado nenhum; tira 2% de vida por segundo). Não há `>>` desenhado: a escada aparece depois da cena.
