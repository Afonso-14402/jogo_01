# Guião das cenas

O guião de **todas as cenas da história**, fala a fala. As missões que estas cenas fazem avançar estão em
`docs/MISSOES.md` (prefixo `H_`). As conversas normais dos NPCs (fora das cenas) estão em `docs/dialogos/`.

| Ficheiro | Cenas |
|---|---|
| [`prologo.md`](prologo.md) | criação da personagem, despertar, o lobo, Ascendia, a Guilda, a primeira subida |
| [`cap01_floresta.md`](cap01_floresta.md) | capítulo 1 (andares 1–10) |
| `cap02_cavernas.md` … `cap10_abismo.md` | capítulos 2 a 10 |
| `finais.md` | a escolha final, os 4 finais e os epílogos |

---

## Como se lê uma cena

Cada cena tem uma ficha e depois as falas por ordem:

| Campo | O que é |
|---|---|
| **ID** | nome da cena no código (`cena_p02_despertar`) |
| **Quando** | o que faz a cena começar (entrar numa zona, acabar uma luta, falar com alguém…) |
| **Onde** | andar e zona |
| **Quem** | personagens em cena |
| **Música** | faixa (ver `docs/AUDIO.md`) |

Dentro da cena:

| Marca | Significa |
|---|---|
| **Nome** *(emoção)*: "fala" | um personagem fala; a emoção escolhe o retrato (normal, feliz, zangado, triste) |
| `[Sistema] …` | janela azul do Sistema |
| 🎥 | o que a câmara faz |
| 🎬 | o que os personagens fazem (animações, movimentos) |
| ▶ | **escolha** do jogador (o herói não fala fora das escolhas) |
| ⚙ | efeito no jogo (amizade, flag, item, missão) |
| ⏭ | a cena pode ser saltada a partir daqui |

O herói é **silencioso**: só "fala" através das escolhas, para o jogador se sentir ele próprio.
`{nome}` é o nome que o jogador escolheu.
