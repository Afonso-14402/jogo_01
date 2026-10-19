# Mapas — Região 1: Floresta (andares 1–10)

Mapas vistos de cima, para construir os andares no Blender e no Godot. A legenda e as regras estão em
[`README.md`](README.md). Monstros, recursos, segredos e puzzles vêm de `docs/regioes/r01_floresta.md`;
aqui está **onde** fica cada coisa.

---

## Andar 1 — Prado do Despertar

Tamanho: **150×150 m** · 15×15 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O 
  1  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
  2  TTTTTTTTtt^^##^^##^^ttTTTTTTTT
  3  TTTTTTtt^^##^^GG^^##^^ttTTTTTT
  4  TTTTtt""^^^^##^^##^^^^""ttTTTT
  5  TTtt""""""^^^^::^^^^""""rrttTT
  6  TT""""""""""""::""""""CCCCttTT
  7  TTtt""""""""""::""""""CC??..TT
  8  TT""""""""rr""""::""""""""ttTT
  9  TTtt^^^^!!""""""""::""""""ttTT
 10  TT^^^^^^^^""""""""::""""rrttTT
 11  TT^^ttPP^^""""""""""SS..ttttTT
 12  TT^^AA^^^^..""""""""....ttTTTT
 13  TTTT^^^^..""""""""..ttTTTTTTTT
 14  TTTTTTtt....""""""..TTTTTTTTTT
 15  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `AA` | C12 | Onde o herói acorda no prólogo (cena P2). A pedra brilhante do tutorial está 1 célula a norte |
| `SS` | K11 | Zona Segura: fogueira, cristal, Tibério (depois do prólogo). Aqui o Kai leva o herói na cena P4 |
| `GG` | H3 | Coelho-Chifre Ancião, no centro do Círculo de Pedras. Depois de vencido, abre-se aqui a **escada de luz** para o andar 2 |
| `??` | M7 | Moinho Abandonado: a corda das pás está aqui. Puxar → as pás rodam → alçapão com **baú de prata** |
| `PP` | D11 | Página 1 do diário, debaixo de uma pedra lisa ao pé da árvore (só a partir de H_03) |
| `!!` | E9 | Puzzle tutorial: empurrar a pedra para dentro do buraco e passar da colina para o campo |
| `rr` | M5 | Rocha de Minério de Cobre |
| `rr` | F8 | Rocha de Minério de Cobre |
| `rr` | M10 | Rocha de Minério de Cobre |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Colina do Despertar | B9–E13 | Slime Verde (poucos) | Erva Verde, Linho Bravo |
| Campo de Erva Alta | B4–L14 | Slime Verde, Coelho-Chifre (escondidos na erva) | Erva Verde (muita), sementes |
| Moinho Abandonado | L6–N8 | Coelho-Chifre | Carvalho (poucos) |
| Círculo de Pedras | E2–K5 | — (só o guardião) | — |

**Caminho principal:** Prólogo: A → descer a colina (puzzle `!!`) → erva alta (slimes; o lobo da cena P3 aparece em G12) → Zona Segura `SS`. Depois do prólogo: `SS` → trilho `::` para norte → Círculo de Pedras `GG`.

**Notas para construir:** O Círculo de Pedras fica 4 m acima do campo (colina `^^`). O moinho é a peça especial: as pás rodam sempre devagar e mais depressa depois do segredo. A erva alta `""` é um MultiMesh com shader de vento.

---

## Andar 2 — Bosque dos Sussurros

Tamanho: **200×200 m** · 20×20 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T 
  1  TTTTTTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTT
  2  TTTTTTTTTTTTTTTTTT..GG..TTTTTTTTTTTTTTTT
  3  TTTTTTTTTTTTTTtt..........ttTTTTTTTTTTTT
  4  TTTT..........ttTTtt::ttTTTTTTTTTTTTTTTT
  5  TT......!!......tttt::ttttTTTTTTTTTTTTTT
  6  TT..$$........tttttt::ttttttttTTTTTTTTTT
  7  TTTT........tttttttt::ttCCCC..CCttTTTTTT
  8  TT▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒tt::::..@@....,,ttTTTT
  9  TT▒▒▒▒▒▒??▒▒▒▒▒▒▒▒tttt::CC..CC..,,ttTTTT
 10  TT▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒tt::......CC,,,,ttTT
 11  TT▒▒▒▒PP▒▒▒▒▒▒▒▒▒▒▒▒tt::tttttttt,,,,ttTT
 12  TT▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒tt::tttttttt,,ttttTT
 13  TTTT▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒tt::tttttt,,,,ttttTT
 14  TTTTTT▒▒▒▒▒▒▒▒▒▒tttt..::tttttt,,ttttttTT
 15  TTTTTTTT▒▒▒▒tttt......::....tt,,,,ttttTT
 16  TTTTTTTTTTtttt........::......,,ttTTTTTT
 17  TTTTTTTTTTTTtt........::........,,TTTTTT
 18  TTTTTTTTTTTTTTtt......::..SS....,,TTTTTT
 19  TTTTTTTTTTTTTTTTtt....EE..ttTTTT,,TTTTTT
 20  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT,,TTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | L19 | Chegada (escada do andar 1) |
| `SS` | N18 | Zona Segura |
| `GG` | K2 | Coruja Sombria (guardião), numa clareira redonda |
| `>>` | K1 | Escada para o andar 3 |
| `$$` | C6 | Baú de prata do puzzle dos 3 Sussurros |
| `??` | E9 | Árvore oca com o **Anel do Sussurro** |
| `PP` | D11 | Página 2, presa num ramo baixo de uma árvore que sussurra ("Ele também passou por aqui…") |
| `!!` | E5 | Puzzle **Os 3 Sussurros**: as 3 árvores com cara à volta da clareira dizem a ordem; as 3 pedras estão em C4, E6 e G4 |
| `@@` | N8 | Acampamento dos Lenhadores: fogueira grande e Bruno Machadão (cena C1-01). Tendas `CC` à volta; cama e cristal na tenda de M9 |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Trilho dos Lenhadores | K3–L19 | Coelho-Chifre, Slime Verde | Carvalho |
| Acampamento dos Lenhadores | M7–Q11 | — (povoação) | loja do Bruno |
| Bosque Escuro | B8–J15 | Lobo Cinzento (alcateias de 3), Cogumelo Andante | Cogumelo Luminoso, vaga-lumes (frasco de luz) |
| Clareira dos Sussurros | B4–G7 | Cogumelo Andante | Erva Verde, Linho Bravo |

**Caminho principal:** `EE` → Trilho para norte (passa pelo Acampamento) → Clareira da Coruja `GG` → `>>`. O Bosque Escuro e a Clareira dos Sussurros são opcionais.

**Notas para construir:** O Bosque Escuro `▒▒` tem luz muito baixa (só a lanterna do herói e os vaga-lumes). O ribeiro `,,` que passa pela serração (P10) é só decorativo: água rasa. As árvores que sussurram usam a peça "árvore com cara".

---

## Andar 3 — Ribeiro Cristalino

Tamanho: **220×180 m** · 22×18 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V 
  1  TTTTTTTTTTTTTTTTTTTTTT####~~####TTTTTTTTTTTT
  2  TTTT>>....ttttTTTTTTTT##??~~rr##TTTTTTTTTTTT
  3  TTTT..GG........tttttttt##~~~~rr##ttTTTTTTTT
  4  TTtt..................tttt..~~~~....ttTTTTTT
  5  TTtt..................,,!!~~~~~~,,......ttTT
  6  TTtt............@@,,,,======,,,,........ttTT
  7  TTtt..............,,~~~~~~~~,,,,........ttTT
  8  TTTT............,,~~~~~~~~~~~~~~,,......ttTT
  9  TTTT..........,,~~~~~~......~~~~~~,,....ttTT
 10  TT............!!~~~~~~..??..~~~~~~!!....ttTT
 11  TTTT..........,,~~~~~~~~~~~~~~~~,,......ttTT
 12  TTTT............,,~~~~~~~~~~~~,,........ttTT
 13  TTtt..............,,~~~~~~~~,,..........ttTT
 14  TTtt..............,,==PP====,,........rr..TT
 15  TTTT..............,,~~~~~~,,............ttTT
 16  TTTTTT..........,,~~~~~~,,........SS....TTTT
 17  TTTTTTTT......,,======,,............EE..TTTT
 18  TTTTTTTTTTTT,,~~~~~~,,TTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | S17 | Chegada (escada do andar 2) |
| `SS` | R16 | Zona Segura |
| `GG` | D3 | Lagostim Couraçado (guardião), na Margem Norte |
| `>>` | C2 | Escada para o andar 4 |
| `??` | M2 | Gruta atrás da Cascata Alta com o **baú de ouro** (entra-se pelo lado direito da cascata) |
| `??` | M10 | Ninho na Ilhota com a **chave** do baú de ouro |
| `PP` | L14 | Página 3, entalada entre duas tábuas da ponte do meio (vê-se a brilhar por baixo) |
| `!!` | M5 | Roda das comportas nº 1 |
| `!!` | H10 | Roda das comportas nº 2 |
| `!!` | R10 | Roda das comportas nº 3. Ordem certa: 2 → 3 → 1 (dica numa placa ao lado da roda nº 1). A água baixa e aparece um caminho de pedras até à Ilhota |
| `@@` | I6 | Pip a pescar (cena de apresentação e missão R1_03) |
| `rr` | O2 | Minério de Cobre (zona rica) |
| `rr` | P3 | Minério de Cobre (zona rica) |
| `rr` | T14 | Minério de Cobre |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Cascata Alta | K1–Q4 | Slime Verde | Minério de Cobre (muito) |
| Margem Norte | B2–K8 | Lobo Cinzento, Javali | Erva Verde, Juncos |
| Pontes de Madeira | H5–P7 e I13–O17 | Coelho-Chifre | pedras de rio |
| Bacia Funda | H8–R12 | — (água funda: leva-te rio abaixo) | peixes (pesca) |
| Ilhota | L9–N10 | — | ninho com a chave |

**Caminho principal:** `EE` → atravessar uma das 3 pontes (norte L6–N6, meio K14–N14, sul I17–K17) para a margem oeste → subir para norte → `GG` → `>>`.

**Notas para construir:** A água funda `~~` arrasta o herói rio abaixo (corrente para sul) e larga-o na margem sul. As tábuas das pontes rangem. A cascata é a peça especial (shader de água a cair + partículas de salpicos).

---

## Andar 4 — Clareira dos Cogumelos

Tamanho: **200×200 m** · 20×20 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T 
  1  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
  2  TTTTTT>>TTTTTTTTTT()()TTTT()()TTTTTTTTTT
  3  TTTT..GG....tttt()()..JJ....()()()..TTTT
  4  TTTT........tt()..$$!!....JJ....()()..TT
  5  TTtt..........()..()..()..()....JJ....TT
  6  TTtt............JJ..........()....()..TT
  7  TTtt..()()()()..................ttttTTTT
  8  TTtt..()??..()......()()()......ttttttTT
  9  TTtt..()()()()....()??CC()........ttttTT
 10  TTtt..............()CCPP()....xxxx%%ttTT
 11  TTtt..........()....()()....xxxx%%%%xxTT
 12  TTtt()()..............::......xx%%%%xxTT
 13  TTtt()................::....xxxx%%xxxxTT
 14  TTTT()................::......xxxxxxttTT
 15  TTtt..()..............::..........ttttTT
 16  TTtt()..........()....::........ttttttTT
 17  TTTTtt................::....ttttTTTTTTTT
 18  TTTTTTtt..........SS..::....ttTTTTTTTTTT
 19  TTTTTTTTtttt..........EE....TTTTTTTTTTTT
 20  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | L19 | Chegada (escada do andar 3) |
| `SS` | J18 | Zona Segura |
| `GG` | D3 | Rainha dos Esporos (guardião) |
| `>>` | D2 | Escada para o andar 5 |
| `$$` | J4 | Baú de prata do puzzle das luzes |
| `??` | E8 | Centro do **Anel de Fadas**: entrar à meia-noite leva à Clareira Secreta das Fadas (loja, missão R1_04) |
| `??` | K9 | Sala escondida do Cogumelo Oco com o **Livro de Receitas: Sopas** |
| `PP` | L10 | Página 4, em cima da mesa redonda do Cogumelo Oco |
| `!!` | K4 | Puzzle **Luzes dos cogumelos**: os 5 cogumelos-lanterna estão em I3, J5, L5, N5 e O6; bater-lhes pela ordem do arco-íris (vermelho, laranja, amarelo, verde, azul) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Anel de Fadas | C7–G9 | Fada Travessa | Erva Verde |
| Bosque Gigante | G2–S6 | Cogumelo Andante, Fada Travessa | Cogumelo Luminoso (no topo dos cogumelos) |
| Cogumelo Oco | J8–M11 | — | — |
| Pântano de Esporos | O10–S14 | Cogumelo Andante (muitos), Slime Verde | Esporo (muito) |

**Caminho principal:** `EE` → norte pelo trilho até L12 → campo aberto → `GG` (noroeste) → `>>`. O Bosque Gigante sobe-se com os cogumelos-trampolim `JJ` (desafio: chegar ao cimo do mais alto, em N2).

**Notas para construir:** Os cogumelos gigantes `()` têm 3 alturas (4, 7 e 10 m) e o topo é plataforma. Os trampolins `JJ` atiram o herói 6 m para cima. O Pântano de Esporos `xx` envenena (área com partículas roxas); `%%` é lama.

---

## Andar 5 — Toca do Javali-Rei 💀

Tamanho: **180×180 m** · 18×18 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R 
  1  TTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTT
  2  TTTTTTTTTTTT^^BBBBBB^^TTTTTTTTTTTTTT
  3  TTTTTTTTTT^^BBBBBBBBBB^^TTTTTTTTTTTT
  4  TTTTTTTT^^^^BBBBBBBBBB^^^^TTTTTTTTTT
  5  TTTTTTtt^^^^^^BBBBBB^^^^^^ttTTTTTTTT
  6  TTTTtt^^HH^^^^^^::^^^^HH^^^^ttTTTTTT
  7  TTtt^^^^^^^^HH^^::^^^^^^^^HH^^ttTTTT
  8  TT^^^^HH^^^^^^^^::^^^^HH^^^^^^^^ttTT
  9  TT^^^^^^^^%%%%%%::%%%%^^^^^^^^^^ttTT
 10  TTtt^^??^^%%%%%%%%%%%%%%^^HH^^FFttTT
 11  TTtt^^^^%%%%%%%%::%%%%%%%%^^FFFFFFTT
 12  TTttHH^^^^%%%%%%::%%%%^^^^FFFFPPFFTT
 13  TTtt^^^^^^^^^^..::....^^^^FFFFFFFFTT
 14  TTTTtt^^HH^^....::........FFFFFFttTT
 15  TTTTTTtt^^^^....::....SS....ttttTTTT
 16  TTTTTTTTtt......::........ttTTTTTTTT
 17  TTTTTTTTTTTTtt..EE....ttTTTTTTTTTTTT
 18  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | I17 | Chegada (escada do andar 4) |
| `SS` | L15 | Zona Segura (aqui o Tibério espera pela caixa do Tobias, missão N_TOBIAS_1) |
| `>>` | I1 | Escada para o andar 6 (abre depois do Javali-Rei) |
| `BB` | H2, I2, J2, G3, H3, I3, J3, K3, G4, H4, I4, J4, K4, H5, I5, J5 | Grande Toca: arena do mini-boss **Javali-Rei** (cenas C1-02 e C1-03). Cratera de terra com lama no centro |
| `??` | D10 | Toca pequena: só se passa a rastejar depois da **Poção de Encolher** → **Ovo de Ouro do Javali** |
| `PP` | P12 | Página 5, pregada na macieira mais velha do Pomar (a que tem marcas de presas) |
| `FF` | P10, O11, P11, Q11, N12, O12, Q12, N13, O13, P13, Q13, N14, O14, P14 | Macieira (maçãs para atirar aos javalis) |
| `HH` | E6, L6, G7, N7, D8, L8, N10, C12, E14 | Toca (sai um javali quando passas perto) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Colinas das Tocas | B5–P9 | Javali (muitos), Coelho-Chifre | Minério de Cobre |
| Lamaçal | E8–M12 | Javali, Lobo Cinzento | — |
| Pomar Selvagem | M9–Q14 | Javali (a comer) | Maçã Selvagem, Carvalho |
| Grande Toca | F1–M5 | Javali-Rei | — |

**Caminho principal:** `EE` → trilho para norte → atravessar o Lamaçal (Lentidão; ou contornar pelo Pomar) → subir as colinas → Grande Toca `BB` → `>>`.

**Notas para construir:** O andar é todo em colinas (`^^` = 2 a 6 m de altura, suaves). As tocas `HH` são buracos na encosta. A arena tem uma cerca de troncos que se fecha quando a luta começa.

---

## Andar 6 — Colinas Floridas

Tamanho: **220×220 m** · 22×22 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V 
  1  TTTTTTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTTTTTT
  2  TTTTTTTT**MM**TTTT..GG..TTTTCCCCCCCCTTTTTTTT
  3  TTTT**MM**??**MM**......ttCCCC!!CCCCttTTTTTT
  4  TT$$****MM******MM**..****..ttCCCCCCCCttTTTT
  5  TT**********..******::****..**ttttCCCCttTTTT
  6  TT****FF********....::**FF****..ttttttTTTTTT
  7  TTtt**********FF**..::********FF****ttttTTTT
  8  TTtt****FF**********::****FF********ttTTTTTT
  9  TT**********........::........**********ttTT
 10  TTwwwwwwwwwwwwwwwwww==wwwwwwwwwwwwwwwwwwwwTT
 11  TTwwwwwwwwwwwwwwwwww==wwwwwwwwwwwwwwwwwwwwTT
 12  TT**FF************..::..******FF********ttTT
 13  TT**************....::....******CCPP****ttTT
 14  TTtt****FF********..::..**************ttttTT
 15  TTtt**************..::....****FF******ttTTTT
 16  TTTT************....::....**********ttTTTTTT
 17  TTTTtt********SS....::......******ttttTTTTTT
 18  TTTTTTtt****........EE......****ttTTTTTTTTTT
 19  TTTTTTTTTTtttt................ttttTTTTTTTTTT
 20  TTTTTTTTTTTTTTttttttttttttttttTTTTTTTTTTTTTT
 21  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
 22  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | K18 | Chegada (escada do andar 5) |
| `SS` | H17 | Zona Segura |
| `GG` | K2 | Abelha-Rainha Melífera (guardião) |
| `>>` | K1 | Escada para o andar 7 |
| `$$` | B4 | Passagem secreta com **baú de ouro** (abre quando pões a Flor de Mel no vaso) |
| `??` | F3 | Estátua com o **vaso vazio** (pôr uma Flor de Mel) |
| `PP` | R13 | Página 6, colada com mel à entrada da colmeia mais pequena |
| `!!` | P3 | Entrada da colmeia maior: puzzle **Colmeia labirinto** (empurrar favos até ao Mel Real) |
| `FF` | D6 | Flor de pólen vermelha (+10% ATQ, 30 s) |
| `FF` | M6 | Flor de pólen azul (+MP) |
| `FF` | H7 | Flor de pólen amarela (+velocidade) |
| `FF` | P7 | Flor de pólen vermelha |
| `FF` | E8 | Flor de pólen azul |
| `FF` | N8 | Flor de pólen amarela |
| `FF` | C12 | Flor de pólen vermelha |
| `FF` | P12 | Flor de pólen azul |
| `FF` | E14 | Flor de pólen amarela |
| `FF` | P15 | Flor de pólen vermelha |
| `MM` | F2, D3, H3, E4, I4 | Estátua de jardim |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Jardim das Estátuas | B2–J5 | Fada Travessa | Flor de Mel |
| Colmeias Gigantes | N2–S6 e Q13 | Abelha-Gigante (muitas) | Mel Azul, Cera |
| Campos de Flores | B4–T19 (menos o rio) | Coelho-Chifre, Javali, Abelha-Gigante | Flor de Mel, Linho Bravo |
| Rio de Mel | B10–U11 | — (Lentidão forte) | — |

**Caminho principal:** `EE` → trilho para norte → **ponte** sobre o Rio de Mel (K10–K11) → `GG` → `>>`.

**Notas para construir:** As flores `**` mudam de cor com a estação (4 variações da mesma textura). O Rio de Mel `ww` é dourado, espesso, com bolhas lentas; quem entra fica com Lentidão forte. As colmeias são a peça especial.

---

## Andar 7 — Floresta Antiga

Tamanho: **260×260 m** · 26×26 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
  1  TTTTTTTTTTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTTTTTTTTTT
  2  TTTTTTTTTTTTTTTTTTTTtt..GG..ttTTTTTTTTTTTTTTTTTTTTTT
  3  TTTTTTTT()()TTTTTTtt..........ttTTTT()()TTTTTTTTTTTT
  4  TTTTTT()()()()..ii......::....()()()()()....()TTTTTT
  5  TTTT()()==()()..........::......()()@@@@()()..ttTTTT
  6  TTtt()()==()()....tt....::....()()@@@@@@@@()()..ttTT
  7  TTtt..====......tttt....::....()@@@@PP@@@@@@()....TT
  8  TTtt..==..........tt....::......()@@JJ@@@@()......TT
  9  TTttii==....()()........::........()()JJ()()....ttTT
 10  TTtt..==....()()........::......................ttTT
 11  TT()..========..........==========............()()TT
 12  TT()()..??..()()........::....()()()........()()()TT
 13  TT()()......()()....ii..::....()()()..........()()TT
 14  TTtt....................::......................ttTT
 15  TTtt....()()()..........::..........()()()......ttTT
 16  TTtt..()()!!()()........::........()()..ii....ttttTT
 17  TTtt..()!!HH!!()........::..........()()........ttTT
 18  TTtt..()()!!()()........::....................ttTTTT
 19  TTtt....................::..........()()()......ttTT
 20  TTtt....()()()..........::....................ttTTTT
 21  TTtttt..()()()........SS::......()()()..........ttTT
 22  TTTTtttt................EE............ttttttttTTTTTT
 23  TTTTTTTTTTtttt......................ttttTTTTTTTTTTTT
 24  TTTTTTTTTTTTTTttttttttttttttttttttTTTTTTTTTTTTTTTTTT
 25  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
 26  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | M22 | Chegada (escada do andar 6) |
| `SS` | L21 | Zona Segura |
| `GG` | M2 | Guardião de Musgo (guardião), numa clareira com musgo (tira-o do musgo!) |
| `>>` | M1 | Escada para o andar 8 |
| `??` | E12 | Poço da Lua: numa noite de lua cheia, a luz aponta para a Raiz Oca |
| `PP` | S7 | Página 7, na casa vazia mais alta de Folhalta |
| `!!` | F16 | Altar da Seiva (norte) |
| `!!` | E17 | Altar da Seiva (oeste) |
| `!!` | G17 | Altar da Seiva (este) |
| `!!` | F18 | Altar da Seiva (sul) — os 4 Cristais de Seiva abrem a Raiz Oca |
| `@@` | S5, T5, R6, S6, T6, U6, Q7, R7, T7, U7, V7, R8, T8, U8 | Folhalta: casas élficas nas árvores (estalagem, cristal, loja da Mira, Anciã Lothiel, Eldrin, Tilly, Faelan). Cena C1-05 no elevador de cesto |
| `ii` | I4 | Cristal de Seiva nº 1 |
| `ii` | C9 | Cristal de Seiva nº 2 (no fim da raiz-ponte) |
| `ii` | K13 | Cristal de Seiva nº 3 |
| `ii` | U16 | Cristal de Seiva nº 4 |
| `HH` | F17 | Raiz Oca: entrada da masmorra **Toca das Raízes** (fechada até pores os 4 cristais) |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Raízes Gigantes | B3–K12 | Treant Jovem, Lobo Cinzento | Carvalho, Madeira Viva |
| Folhalta | P4–W9 (no alto, a 20 m) | — (povoação) | loja élfica |
| Poço da Lua | B11–H13 | Fada Travessa (de noite) | Seiva Cristalizada |
| Raiz Oca | B14–H19 | Cogumelo Andante, Treant Jovem | Cogumelo Luminoso |

**Caminho principal:** `EE` → trilho para norte → raiz-ponte grande (M11–Q11) → clareira → `GG` → `>>`. Folhalta fica a este, lá em cima (elevadores `JJ`).

**Notas para construir:** Andar com **dois níveis**: o chão (0 m) e os caminhos em altura (raízes-ponte `==` e plataformas, a 8–20 m). Os troncos gigantes `()` têm 20 m de largura (aqui 1 célula = o tronco visto de cima, mas o modelo real ocupa 2×2 células). Desafio: atravessar o andar sem tocar no chão (há sempre um caminho por cima).

---

## Andar 8 — Ruínas Cobertas de Musgo

Tamanho: **220×220 m** · 22×22 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V 
  1  TTTTTTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTTTTTT
  2  TTTTTTTTTTTTTTTT##..GG..##TTTTTTTTTTTTTTTTTT
  3  TTTTTTTTTTtt######......######ttTTTTTTTTTTTT
  4  TTTTTTtt..CC..##....::....##..CCCC..ttTTTTTT
  5  TTTTtt....CCCC......::........CCii....ttTTTT
  6  TTtt..####..........::..............ttTTTTTT
  7  TTtt..CCCC....MM........MM..........ttttTTTT
  8  TTtt..CC??..........::..........CCCCCCCCttTT
  9  TTtt..............::!!::..........CC$$CCttTT
 10  TTtt................::..........CCPPCCCCttTT
 11  TTtt....MM..........::......MM....CCCCCCttTT
 12  TTtt....####........::........####..ttTTTTTT
 13  TTTTtt..............::..............ttTTTTTT
 14  TTTTtt..CCCC........::........CCCC..ttTTTTTT
 15  TTTTtt..CC..rr......::......rr..CC....ttTTTT
 16  TTTTTTtt............::..............ttTTTTTT
 17  TTTTTTtt....SS......::............ttTTTTTTTT
 18  TTTTTTTT####......##EE##......####TTTTTTTTTT
 19  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
 20  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
 21  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
 22  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | K18 | Chegada, no **Portão Partido** (escada do andar 7) |
| `SS` | G17 | Zona Segura |
| `GG` | K2 | Cavaleiro de Pedra Musgosa (guardião), entre dois muros |
| `>>` | K1 | Escada para o andar 9 |
| `$$` | S9 | Baú de ouro do Templo Enterrado (precisa da Chave das Ruínas) |
| `??` | E8 | Cimo da **Torre de Vigia**: de dia vê-se o brilho da chave num telhado |
| `PP` | R10 | Página 8, debaixo do altar partido do Templo Enterrado |
| `!!` | K9 | Centro da Praça: puzzle **Estátuas** (os 4 pedestais estão nos cantos da praça, à volta deste ponto) |
| `rr` | G15 | Minério de Cobre |
| `rr` | O15 | Minério de Cobre |
| `ii` | Q5 | **Chave das Ruínas**, num telhado (sobe-se por uma parede caída) |
| `MM` | H7 | Estátua de cavaleiro que anda nº 1 |
| `MM` | M7 | Estátua nº 2 |
| `MM` | E11 | Estátua nº 3 |
| `MM` | O11 | Estátua nº 4 |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Portão Partido | E16–Q18 | Slime Verde, Lobo Cinzento | pedra trabalhada |
| Praça das Estátuas | D6–O12 | — (as estátuas) | Hera |
| Templo Enterrado | Q7–T11 | Treant Jovem | — |
| Torre de Vigia | C6–E8 | Abelha-Gigante | — |
| Aldeia em ruínas | C3–Q5 e C13–Q15 | Treant Jovem, Abelha-Gigante | Minério de Cobre, Carvalho |

**Caminho principal:** `EE` → rua principal para norte → Praça das Estátuas (cena C1-06, os símbolos do Sistema) → `GG` → `>>`.

**Notas para construir:** As 4 estátuas `MM` só se mexem quando estão **fora do ecrã** (o código vê se a câmara as vê). Os símbolos azuis do Sistema estão nas paredes do Templo e da Praça (decalques que brilham).

---

## Andar 9 — Lago da Névoa

Tamanho: **240×240 m** · 24×24 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R S T U V W X 
  1  TTTTTTTTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTTTTTTTT
  2  TTTTTTTTTTTTTTTTTTtt..GG..ttTTTTTTTTTTTTTTTTTTTT
  3  TTTTTTTTTTTTtt,,,,,,,,,,,,,,,,,,ttTTTTTTTTTTTTTT
  4  TTTTTTTTtt,,,,~~~~~~~~~~~~~~~~~~,,,,ttTTTTTTTTTT
  5  TTTTtt,,,,~~~~~~~~~~~~~~~~~~~~~~~~~~,,,,ttTTTTTT
  6  TTtt,,~~~~~~~~tt..!!~~~~~~~~~~~~~~~~~~~~,,ttTTTT
  7  TT,,~~~~~~~~~~tttt~~~~~~~~~~~~~~~~tt..~~~~,,ttTT
  8  TT,,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~tt..~~~~~~,,TT
  9  TT,,~~~~~~~~~~~~~~~~CCCCCC~~~~~~~~~~~~~~~~~~,,TT
 10  TT,,~~~~~~~~~~~~~~..CCPPCC..~~~~~~~~~~~~~~~~,,TT
 11  TT,,~~~~~~~~~~~~~~..........~~~~~~~~~~~~~~~~,,TT
 12  TT,,~~~~~~??~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,,TT
 13  TT,,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~tt..~~~~~~,,TT
 14  TT,,~~~~tt!!~~~~~~~~~~~~~~~~~~~~~~..!!~~~~~~,,TT
 15  TT,,~~~~tttt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,,ttTT
 16  TTtt,,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,,ttTT
 17  TTTT,,,,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,,,,TTTT
 18  TTTTtt,,,,,,~~~~~~~~~~~~~~~~~~~~~~~~,,,,,,ttTTTT
 19  TTTTtt"""",,,,==JJ~~~~~~~~~~~~~~,,,,"""",,ttTTTT
 20  TTTTtt"""""",,,,,,,,,,,,,,,,,,,,""""""""ttTTTTTT
 21  TTTTTTtt""""""""........::........""""ttttTTTTTT
 22  TTTTTTTTtt""""""....SS..::........""""ttTTTTTTTT
 23  TTTTTTTTTTtttt..........EE..........ttttTTTTTTTT
 24  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | M23 | Chegada (escada do andar 8) |
| `SS` | K22 | Zona Segura |
| `GG` | L2 | Serpente da Névoa (guardião): sai do lago nesta margem |
| `>>` | L1 | Escada para o andar 10 |
| `??` | F12 | Ilha que **só aparece às 3:00** (seguir os fogos-fátuos): **Altar do Reflexo** |
| `PP` | L10 | Página 9, no templo da Ilha Central, em cima do banco virado para o lago |
| `!!` | J6 | Sino de barco nº 1 |
| `!!` | F14 | Sino de barco nº 2 |
| `!!` | S14 | Sino de barco nº 3 — tocar os 3 no mesmo minuto abre o templo da Ilha Central |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Margem dos Juncos | C18–T22 | Slime Verde, Cogumelo Andante, Lobo Cinzento (noite) | Juncos, Erva Verde |
| Cais Velho | G19–I19 | — | pesca |
| Ilhas dos Salgueiros | H6–J7, R7–S8, R13–S14, E14–F15 | Fada Travessa | Salgueiro (madeira) |
| Ilha Central | J9–N11 | — | — |
| Margem Norte | H2–O3 | — | — |

**Caminho principal:** `EE` → Cais Velho → **barco** até à Margem Norte (ou a pé pela água rasa `,,` à volta do lago, mais lento) → `GG` → `>>`. Cena C1-07 (o reflexo) acontece na Margem dos Juncos.

**Notas para construir:** Nevoeiro denso: só se vê a 6 m (o resto do lago fica branco). A água rasa `,,` à volta deixa andar devagar. Troncos a boiar no lago afundam se ficares parado 2 s em cima deles. O barco é a peça especial (controlo de remar com o analógico).

---

## Andar 10 — Coração da Floresta 👑

Tamanho: **180×180 m** · 18×18 células de 10 m · norte em cima

```
     A B C D E F G H I J K L M N O P Q R 
  1  TTTTTTTTTTTTTTTT>>TTTTTTTTTTTTTTTTTT
  2  TTTTTTTTTTTT()()()()()TTTTTTTTTTTTTT
  3  TTTTTTTT^^^^()()()()()()^^^^TTTTTTTT
  4  TTTTTT^^BBBBBBBBPPBBBBBBBBBB^^TTTTTT
  5  TTTT^^BBBBBBBBBBBBBBBBBBBBBBBB^^TTTT
  6  TTTT^^BBBBBBBBBBBBBBBBBBBBBBBB^^TTTT
  7  TTTTTT^^BBBBBBBBBBBBBBBBBBBB^^TTTTTT
  8  TTTTTTtttt^^^^^^::^^^^^^^^ttttTTTTTT
  9  TTTTtttt..ii....::....ii..ttttTTTTTT
 10  TTtttttt........::........ttttttTTTT
 11  TTtttt....ii....::....ii....ttttTTTT
 12  TTtttt..........::..........ttttTTTT
 13  TTTTtttt..ii....::....ii..ttttTTTTTT
 14  TTTTtttttt......::......ttttttTTTTTT
 15  TTTTTTtttt..ii..::..ii..ttttTTTTTTTT
 16  TTTTTTTTtt......::..SS..ttTTTTTTTTTT
 17  TTTTTTTTTTtt....EE....ttTTTTTTTTTTTT
 18  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
```

**Pontos importantes**

| Marca | Onde | O que é |
|---|---|---|
| `EE` | I17 | Chegada (escada do andar 9) |
| `SS` | K16 | Zona Segura (a última da região) |
| `>>` | I1 | Escada para o andar 11 (aparece atrás da Árvore-Mãe depois da cena C1-10) |
| `BB` | E4, F4, G4, H4, J4, K4, L4, M4, N4, D5, E5, F5, G5, H5, I5, J5, K5, L5, M5, N5, O5, D6, E6, F6, G6, H6, I6, J6, K6, L6, M6, N6, O6, E7, F7, G7, H7, I7, J7, K7, L7, M7, N7 | Raízes da Árvore-Mãe: arena do boss **Ent Ancião** (cenas C1-09 e C1-10). A Árvore-Mãe `()` fica ao fundo |
| `PP` | I4 | Página 10: cai de um ramo da Árvore-Mãe no fim da cena C1-10 |
| `ii` | F9 | Lanterna de pedra nº 1 |
| `ii` | L9 | nº 2 |
| `ii` | F11 | nº 3 |
| `ii` | L11 | nº 4 |
| `ii` | F13 | nº 5 |
| `ii` | L13 | nº 6 |
| `ii` | G15 | nº 7 |
| `ii` | K15 | nº 8 — acender as 8 (com fogo) dá +10% de dano contra o boss |

**Zonas**

| Zona | Células | Monstros | Recursos |
|---|---|---|---|
| Caminho das Lanternas | E8–L16 | Treant Jovem, Fada Travessa | Folha Dourada |
| Bosque Sagrado | B7–P16 (dos lados do caminho) | Lobo Cinzento, Treant Jovem | Seiva Cristalizada, Madeira Viva |
| Raízes da Árvore-Mãe | C2–O7 | Ent Ancião | — |

**Caminho principal:** `EE` → Caminho das Lanternas (cena C1-08, a voz) → arena `BB` → boss → cena da Árvore-Mãe → `>>`.

**Notas para construir:** Andar pequeno e direito: é o "corredor" para o boss. Árvores brancas `tt`, folhas douradas a cair (partículas). A Árvore-Mãe é a maior peça da região (cerca de 40 m de altura); depois da cena fica cinzenta (troca de material).
