# Regras da arte

Segue estas regras para tudo o que desenhares ou modelares entrar no jogo **sem ter de ser refeito**.

---

## 1. Regras gerais

- **Paleta**: só as cores da **Resurrect 64** (Lospec). Importa-a no Pixelorama / Aseprite.
- **Formato**: `.png` com fundo **transparente**.
- **Nunca** desfocar, suavizar ou redimensionar com filtro: só pixel art "dura".
- **Nomes dos ficheiros**: tudo em **minúsculas**, **sem espaços** e **sem acentos**, com `_` a separar.
  - ✅ `lobo_cinzento_andar_lado.png` · ❌ `Lobo Cinzento (andar).PNG`
- Guarda **também o ficheiro de trabalho** (`.pxo` do Pixelorama ou `.aseprite`) ao lado do `.png`.

---

## 2. Herói

- **Tamanho**: 32×32 px por frame. O herói ocupa cerca de 16 px de largura e 26 px de altura,
  com os **pés no fundo do quadro** (centro em baixo).
- **Direções**: `baixo`, `cima`, `lado`. O lado é virado para a **direita**; a esquerda é espelhada no jogo.
- **O herói desenha-se SEM arma.** A arma é um sprite separado (ver secção 4).

| Animação | Frames | Notas |
|---|---|---|
| `parado` | 4 | respirar |
| `andar` | 6 | |
| `esquiva` | 4 | rolar / dash |
| `dano` | 2 | |
| `morrer` | 5 | |
| `recolher` | 4 | minar / cortar / apanhar |
| `ataque_corte` | 4 | espada, adaga, katana, foice |
| `ataque_pesado` | 5 | espada grande, machado, martelo |
| `ataque_estocada` | 4 | lança |
| `ataque_disparo` | 4 | arco, besta |
| `ataque_magia` | 4 | cajado |
| `ataque_soco` | 4 | manoplas |

Total: cerca de **50 frames × 3 direções ≈ 150 frames**.

**Exportar**: uma tira horizontal por animação e direção, ex.: `heroi_andar_baixo.png` (6 frames de 32×32 = 192×32 px).

---

## 3. Monstros e NPCs

| Tipo | Tamanho | Direções |
|---|---|---|
| NPCs da cidade | 32×32 | `baixo`, `cima`, `lado` (só `parado` e `andar`) |
| Monstros normais | 32×32 ou 48×48 | só `lado` (espelhado) |
| Mini-bosses | 64×64 | `lado` |
| Bosses | até 128×128 | `lado` (+ `baixo` se der) |

| Animação | Frames |
|---|---|
| `parado` | 2–4 |
| `mover` | 4 |
| `atacar` | 4 |
| `dano` | 1 |
| `morrer` | 4 |
| Bosses: `especial_1`, `especial_2`, `especial_3` | 4–8 cada |

**Exportar**: `lobo_cinzento_mover_lado.png`, `ent_anciao_especial_1_lado.png`, etc.

---

## 4. Armas

- **Uma imagem por arma** (sem animação). O jogo roda e mexe a arma durante o ataque.
- **Posição**: arma **na vertical, a apontar para cima**, com o **punho no centro em baixo** do quadro.
  (Arco e besta: na vertical, com o meio da arma no centro do quadro.)
- **Tamanhos**: 32×32 ou 48×48 conforme o tipo (ver `docs/ARMAS.md`).
- **Ícone do inventário**: 16×16, arma **na diagonal** (punho em baixo à esquerda).
- **Raridade**: **não** desenhes versões diferentes; o brilho é feito pelo jogo.

**Nomes**: `espada_cobre.png` + `espada_cobre_icone.png`, `arco_hidra.png` + `arco_hidra_icone.png`.

Por região: **12 armas normais + 2 únicas = 14 armas** (e 14 ícones).

Também são precisos: **flecha** e **virote** (projéteis), e um efeito de magia por elemento.

---

## 5. Ícones e interface

- **Ícones de itens** (materiais, poções, armaduras, comida): 16×16.
- **Janela de Status / inventário**: estilo "Sistema" isekai (azul translúcido). ❓ desenhar mais tarde, o Claude faz uma versão provisória.

---

## 6. Mundo 3D (Blender)

### Regras
- **Escala**: 1 unidade = 1 metro. O herói tem ~1,6 m. Uma porta tem ~2,2 m.
- **Grelha**: as peças do kit encaixam numa **grelha de 2×2 m** (chão 2×2, parede 2 m de largura).
- **Origem** de cada peça **no centro em baixo**. Antes de exportar: *Apply → All Transforms*.
- **Low-poly**: o mínimo de polígonos que fique bem.
- **Texturas**: pixel art de 32×32 px (ou 64×64 para coisas grandes), no Blender com interpolação **Closest**.
- **Exportar**: `File → Export → glTF 2.0 (.glb)`, uma peça por ficheiro.
- Guarda **também o `.blend`**.

### Kit de peças de cada região (~25 peças)

| Grupo | Peças |
|---|---|
| Chão | 3 variações + 1 caminho + 1 borda |
| Paredes / falésias | parede, canto, rampa, escada |
| Passagens | ponte, porta / arco, escada para o andar seguinte |
| Natureza | 3 árvores (ou equivalente do bioma), 3 rochas, 2 arbustos / plantas |
| Recolha | ponto de minério, árvore que se corta, erva |
| Objetos | baú, fogueira da Zona Segura, cristal de teletransporte |
| Decoração | 3–5 peças do tema (ex.: cogumelo gigante, vagoneta, coral) |

E por cada **andar**: 3–5 peças especiais só desse andar (ver `docs/TORRE.md`).

**Nomes**: `r01_chao_1.glb`, `r01_arvore_2.glb`, `a04_cogumelo_gigante.glb` (a04 = andar 4).

### Cidade
Guilda, Ferreiro, Alquimista, Mercado, Estalagem, casas genéricas (3), base da torre, fonte, bancas, candeeiros.

---

## 7. Pastas

```
arte/
  heroi/                     heroi_andar_baixo.png, ...
  npcs/                      ferreiro_parado_baixo.png, ...
  armas/                     espada_cobre.png, espada_cobre_icone.png, ...
  icones/                    minerio_cobre.png, pocao_vida.png, ...
  ui/
  cidade/                    guilda.blend, guilda.glb, ...
  regioes/
    r01_floresta/
      monstros/              slime_verde_mover_lado.png, ...
      kit/                   r01_chao_1.blend, r01_chao_1.glb, ...
      andares/               a04_cogumelo_gigante.glb, ...
    r02_cavernas/
    ...
    r10_abismo/
  sons/
  musica/
```

---

## 8. Ordem de trabalho (Fase A)

Faz por esta ordem e **mostra-me cada parte** quando acabares, para eu a pôr no protótipo:

1. **Herói**: só `parado` e `andar` (3 direções). → testar no jogo
2. **1 peça de chão + 1 árvore + 1 rocha** da Região 1. → testar no jogo (escala, cores, câmara)
3. Resto das animações do herói
4. **Espada de Cobre** + ícone. → testar na mão do herói
5. Resto do **kit da Região 1**
6. **6 monstros** da Região 1
7. **12 armas de cobre** + **2 únicas** + ícones
8. **Javali-Rei** e **Ent Ancião**
9. Peças especiais dos andares 1–10
10. **Cidade**

> Os passos 1, 2 e 4 são os mais importantes: se o tamanho ou o estilo não ficar bem no jogo,
> corrige-se logo, **antes** de haver centenas de desenhos feitos.

---

## 9. Checklist por região

Copia esta lista para cada região:

- [ ] Kit de peças (~25)
- [ ] Peças especiais dos 10 andares
- [ ] 6 monstros (todas as animações)
- [ ] Mini-boss
- [ ] Boss
- [ ] 12 armas + ícones
- [ ] 2 armas únicas + ícones
- [ ] Ícones dos materiais da região (minério, madeira/planta, drops dos monstros)
- [ ] Música da região (opcional)
