# Mapas

Mapas **vistos de cima** de cada andar e de Ascendia, para construir os níveis no Blender e no Godot.
O que há em cada andar (monstros, recursos, segredos) está em `docs/regioes/`; aqui está **onde** fica.

| Ficheiro | Mapas |
|---|---|
| [`ascendia.md`](ascendia.md) | a cidade |
| [`r01_floresta.md`](r01_floresta.md) | andares 1–10 |
| [`r02_cavernas.md`](r02_cavernas.md) | andares 11–20 |
| [`r03_pantano.md`](r03_pantano.md) | andares 21–30 |
| [`r04_deserto.md`](r04_deserto.md) | andares 31–40 |
| [`r05_gelo.md`](r05_gelo.md) | andares 41–50 |
| [`r06_oceano.md`](r06_oceano.md) | andares 51–60 |
| [`r07_vulcao.md`](r07_vulcao.md) | andares 61–70 |
| `r08_reino_assombrado.md` … `r10_abismo.md` | andares 71–100 (um ficheiro por região) |

---

## Como se lê um mapa

- Cada **célula** do mapa tem **10×10 m** e aparece com **2 letras** (para ficar quadrada no ecrã).
- As colunas têm letras (A, B, C…) e as linhas números: **F8** é a coluna F, linha 8.
- **Norte em cima.** A câmara do jogo olha de sul para norte, por isso o mapa está como o jogador o vê.
- Debaixo de cada mapa há uma tabela com os **pontos importantes** (com a célula), as **zonas**, o **caminho principal**
  e **notas para construir**.

## Legenda dos andares

| Marca | O que é | Passa-se? |
|---|---|---|
| `TT` | floresta densa, rocha ou parede: **limite** do andar | não |
| `tt` | árvores soltas, arbustos | sim (devagar entre os troncos) |
| `▒▒` | floresta escura (sem luz) | sim |
| `..` | chão aberto (erva baixa, terra, pedra) | sim |
| `""` | erva alta ou juncos (escondem coisas) | sim |
| `^^` | colina, terreno mais alto (2 a 6 m) | sim (rampa) |
| `##` | rocha, muro, ruína, falésia | não |
| `~~` | água funda (nada-se ou arrasta) | depende do andar |
| `,,` | água rasa | sim (devagar) |
| `==` | ponte, passadiço, raiz-ponte | sim |
| `::` | caminho ou trilho | sim |
| `%%` | lama (Lentidão) | sim |
| `xx` | zona venenosa (esporos) | sim (envenena) |
| `**` | flores | sim |
| `ww` | rio especial do andar (ex.: mel) ou cascata | ver o andar |
| `mm` | mato denso **cortável** (abre-se com armas de corte; volta a crescer) | só depois de cortar |
| `nn` | nevoeiro ou nuvem (tóxica, de pólen…: ver o andar) | sim (com o efeito do andar) |
| `()` | cogumelo gigante ou tronco gigante | não (alguns sobem-se) |
| `CC` | construção: casa, tenda, moinho, templo, colmeia | não (algumas têm porta) |
| `EE` | **chegada** (escada do andar de baixo) | — |
| `SS` | **Zona Segura** (fogueira + cristal; sem monstros) | — |
| `GG` | **guardião** do andar | — |
| `>>` | **escada** para o andar seguinte (abre depois do guardião) | — |
| `BB` | arena de mini-boss ou boss | — |
| `$$` | baú especial (prata ou ouro) | — |
| `??` | segredo | — |
| `PP` | página do diário de Aren | — |
| `!!` | puzzle (ou peça de um puzzle) | — |
| `@@` | NPC ou povoação | — |
| `AA` | sítio especial da história (ex.: onde acordas) | — |
| `rr` | rocha de minério | — |
| `ii` | objeto a apanhar (cristal, chave, lanterna…) | — |
| `JJ` | objeto que se usa: trampolim, elevador, barco | — |
| `HH` | toca, buraco, entrada de masmorra | — |
| `FF` | planta especial (macieira, flor de pólen…) | — |
| `MM` | estátua | — |
| `[]` | porta (de madeira, de pedra, portão) | depende |
| `<>` | elevador, poço, passagem entre pisos | — |
| `vv` | objeto grande especial do andar (ver tabela) | — |

Os baús normais (madeira) e os nós de recursos comuns **não estão nos mapas**: são sorteados ao entrar no andar
(ver `docs/SISTEMAS.md`). Os monstros aparecem nas zonas indicadas na tabela de cada andar.

## Do mapa para o Godot

1. **Escala**: 1 célula = 10 m = **5 células do GridMap** (que tem 2 m, ver `docs/PROGRAMACAO.md`).
2. Começa por fazer o **chão** e os **limites** (`TT`, `##`) com as peças do kit da região no GridMap.
3. Põe a **chegada**, a **Zona Segura**, o **guardião** e a **escada** nos sítios do mapa. Já dá para jogar.
4. Depois as **zonas** (água, lama, erva alta) e por fim os pontos (segredos, puzzle, página, NPCs).
5. Os pontos são **nós `Marker3D`** com nome (`Pagina`, `Segredo1`, `Puzzle`…) para o código os encontrar.
6. O mapa é um **guia**, não uma regra: se no jogo ficar melhor de outra maneira, muda e atualiza o desenho aqui.
