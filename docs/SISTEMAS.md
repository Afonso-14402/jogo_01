# Sistemas do jogo — regras e fórmulas

Este documento diz **exatamente como cada sistema funciona**, com números. Quando for a hora de
programar, é seguir isto. Todos os números ficam num ficheiro de dados
(`dados/constantes.json`, ver `docs/PROGRAMACAO.md`) para se poderem **afinar** depois de testar,
sem mexer no código.

> Os números são **valores iniciais**. O equilíbrio final faz-se a jogar e com testes automáticos.

---

## 1. Convenções

| Coisa | Unidade |
|---|---|
| Distâncias | metros (1 unidade do Godot = 1 m) |
| Tempo | segundos |
| Velocidade | metros por segundo |
| Percentagens | escritas como `0,15` = 15% nos dados |
| Jogo a correr | 60 imagens por segundo (física a 60 Hz) |
| Arredondamentos | dano e HP arredondam para baixo; mínimo de dano = 1 |

---

## 2. O jogador

### 2.1 Atributos
Começam todos em **5**. A cada nível ganhas **5 pontos** para distribuir (nível 100 = 495 pontos).
Máximo de cada atributo: **300**.

| Atributo | Efeitos |
|---|---|
| **FOR** | +1,5 ATQ físico (armas corpo a corpo e manoplas); +2 kg de carga |
| **AGI** | +0,4% velocidade de ataque; +0,2% velocidade de movimento; +1 Estamina máx. |
| **DES** | +1,5 ATQ físico (arco e besta); +0,10% crítico; +0,5 ATQ (adaga e katana) |
| **INT** | +2 ATQ mágico; +6 MP; +0,5% regeneração de MP |
| **VIT** | +12 HP; +0,6 DEF; +0,3 RES (resistência mágica) |
| **SOR** | +0,15% crítico; +0,3% hipótese de drop raro; +0,5% ouro |

### 2.2 Valores derivados

| Valor | Fórmula |
|---|---|
| HP máx. | `100 + VIT × 12 + nível × 8 + bónus do equipamento` |
| MP máx. | `30 + INT × 6 + nível × 2` |
| Estamina máx. | `100 + AGI × 1` (máx. 250) |
| Regeneração de HP | 1% do HP máx. a cada 5 s, **só fora de combate** (5 s sem levar nem dar dano) |
| Regeneração de MP | 2% do MP máx. por segundo |
| Regeneração de Estamina | 30 por segundo (para 0,6 s depois de a gastar) |
| Velocidade a andar | 4,5 m/s × (1 + AGI × 0,002), máx. 6,5 m/s |
| Crítico (hipótese) | `5% + DES × 0,10% + SOR × 0,15% + arma`, máx. 75% |
| Dano crítico | `150% + bónus da arma` |
| DEF | soma das armaduras + `VIT × 0,6` |
| RES | soma das armaduras + `VIT × 0,3 + INT × 0,3` |

### 2.3 Ações e custos

| Ação | Custo | Detalhes |
|---|---|---|
| Ataque normal | 0 | Combo de 3 golpes (varia por arma, ver `docs/ARMAS.md`) |
| Ataque carregado | 15 Estamina | Segurar o botão 0,8 s → dano ×2,2 |
| Esquiva (dash) | 25 Estamina | 3 m em 0,25 s; **invencível durante 0,25 s** |
| Correr | 8 Estamina/s | velocidade ×1,5 (só fora de combate) |
| Skill de arma | MP ou Estamina | ver `docs/PROGRESSAO.md` |
| Beber poção | — | 0,6 s a beber (podes ser interrompido), recarga de 2 s |
| Interagir | — | tecla de interagir a menos de 1,5 m |

### 2.4 Carga
Peso máximo = `40 kg + FOR × 2`. Acima de 100% andas 30% mais devagar e não podes esquivar.
Os materiais pesam pouco (0,1–0,5 kg); armas 1–8 kg; armaduras 1–10 kg.

### 2.5 Nadar (água funda)

- Na **água funda** (`~~`, `ww` nos mapas) **nada-se**, menos no vulcão (região 7), onde é lava. A nadar: velocidade
  **×0,6**, não se ataca, não se esquiva nem se usam skills (as poções sim); os monstros de terra não entram na água.
- **Oceano (região 6)**: nada-se **debaixo de água** — barra de **Ar de 30 s** (aparece por baixo das barras); sem Ar
  perdes **5% do HP por segundo**; fora de água (ou na água rasa) o Ar enche-se em 3 s; a nadar ficas **Encharcado**.
- Números em `dados/constantes.json` → `nadar`. Os companheiros também nadam (e não têm Ar: são do mundo da torre).
- **Barco** (`JJ` nos mapas do oceano): **E** ao pé dele para entrar; no barco andas **×1,3** na água funda, sem gastar
  Ar nem ficar Encharcado, e não atacas; não sai da água funda. **E** junto à margem para sair (o barco fica ali).
- **Correntes** (`ww` no oceano: redemoinhos, correntes): levam-te (a nadar ou de barco) a **3 m/s** para a ilha mais
  perto com o boss, o guardião ou a escada (ex.: andar 60, o redemoinho puxa o barco até à ilha). Com o nadar, os passadiços do caminho garantido
  (`docs/mapas/README.md`, ponto 7) só são precisos por cima da lava, do vazio e da rocha.

---

## 3. Níveis e XP

- **XP para passar do nível L para L+1:** `50 × L^1,6 + 50` (arredondado)
- **XP de um monstro de nível L:** `8 + 3 × L^1,3` × multiplicador do tipo (secção 6)
- Missões dão XP próprio (ver `docs/MISSOES.md`).
- Matar monstros **5 ou mais níveis abaixo** de ti dá só 20% da XP.
- Nível máximo: **100**.

| Nível | XP para o seguinte | XP total acumulada | XP de um monstro deste nível | Monstros para subir |
|---|---|---|---|---|
| 1 | 100 | 0 | 11 | 9 |
| 2 | 202 | 100 | 15 | 13 |
| 5 | 707 | 1 151 | 32 | 22 |
| 10 | 2 041 | 7 137 | 68 | 30 |
| 20 | 6 084 | 44 390 | 155 | 39 |
| 30 | 11 594 | 128 931 | 258 | 45 |
| 40 | 18 342 | 274 282 | 371 | 49 |
| 50 | 26 191 | 492 159 | 493 | 53 |
| 60 | 35 045 | 793 117 | 623 | 56 |
| 70 | 44 834 | 1 186 875 | 759 | 59 |
| 80 | 55 502 | 1 682 516 | 902 | 62 |
| 90 | 67 001 | 2 288 611 | 1 049 | 64 |
| 99 | 78 031 | 2 935 270 | 1 187 | 66 |

Ao subir de nível: HP e MP enchem, aparece `[Sistema] Subiste para o nível X!` e ganhas 5 pontos.

---

## 4. Combate

### 4.1 Dano físico
```
ATQ = ATQ_arma × (1 + melhoria × 0,05) × raridade
      + FOR × 1,5   (corpo a corpo)   ou   DES × 1,5   (arco e besta)
dano = ATQ × multiplicador_do_golpe × 100 / (100 + DEF_alvo)
       × elemento × crítico × variação(0,95 a 1,05)
```

### 4.2 Dano mágico
```
ATQ_mágico = ATQ_mágico_arma × (1 + melhoria × 0,05) × raridade + INT × 2
dano = ATQ_mágico × multiplicador_da_skill × 100 / (100 + RES_alvo)
       × elemento × crítico × variação
```

### 4.3 Multiplicadores

| Situação | Multiplicador |
|---|---|
| Golpe 1 / 2 / 3 do combo | ×1,0 / ×1,1 / ×1,4 |
| Ataque carregado | ×2,2 |
| Ataque pelas costas (adaga) | ×2,0 |
| Crítico | ×1,5 (+ bónus da arma) |
| Elemento a que o alvo é **fraco** | ×1,5 |
| Elemento a que o alvo **resiste** | ×0,5 |
| Alvo **imune** | ×0 (aparece "IMUNE") |
| Alvo atordoado | ×1,2 |

### 4.4 Ao acertar
- **Hitstop**: o jogo "congela" 0,05 s (0,1 s num crítico) para o golpe ter peso.
- **Piscar a branco**: o alvo fica branco 0,1 s.
- **Empurrão**: 0,5 m (armas pesadas 1,2 m). Bosses não são empurrados.
- **Números de dano** a saltar: branco normal, amarelo crítico, azul magia, verde cura, roxo veneno.
- **Invencibilidade do jogador** depois de levar dano: 0,6 s (pisca).

### 4.5 Elementos
6 elementos: **Fogo, Gelo, Raio, Veneno, Luz, Sombra** + **Físico** (sem elemento).
Cada monstro tem uma lista de fraquezas, resistências e imunidades (ver os ficheiros das regiões).
A arma ganha um elemento quando é **encantada** com uma gema (ver `docs/EQUIPAMENTO.md`).

---

## 5. Estados alterados

| Estado | Como se apanha | Efeito | Dura | Cura |
|---|---|---|---|---|
| **Veneno** | ataques venenosos, armas de veneno | perde 2% do HP máx. por segundo (não desce abaixo de 1 HP) | 6 s | Antídoto, Irmã Célia |
| **Queimadura** | fogo | perde 3% do HP por segundo; DEF −10% | 4 s | rolar no chão (esquivar 2×), água |
| **Frio** | gelo | movimento e ataque −30%. **3 acumulações = Congelado** | 4 s | Poção Quente, fogo |
| **Congelado** | 3× Frio | não te mexes; o próximo golpe faz ×1,5 e parte o gelo | 1,5 s | carregar nos botões depressa |
| **Choque** | raio | interrompe a ação; salta para 2 inimigos a menos de 3 m (50% do dano) | instantâneo | — |
| **Atordoado** | martelo, golpes pesados | não age | 1 s (bosses 0,3 s) | — |
| **Sangrar** | machado, garras | perde 1% do HP por cada metro que andas | 5 s | Ligadura |
| **Lentidão** | teias, lama | movimento −50% | 3 s | — |
| **Cegueira** | areia, tinta, luz forte | o ecrã escurece à volta; inimigos atacam com 30% menos precisão | 4 s | Colírio |
| **Medo** | gritos de bosses | não podes atacar, só fugir | 1,5 s | Amuleto da Coragem dá imunidade |
| **Maldição** | mortos-vivos, Região 8 | cura recebida −50% | 10 s | Água Benta |
| **Encharcado** | água | raio faz ×1,5; fogo faz ×0,5 | 6 s | — |

### 5.1 Estados especiais (de certas regiões e bosses)

| Estado | De onde | Efeito | Dura |
|---|---|---|---|
| **Agarrado** | Crocodilo, Polvo, Urso Polar, bosses | não te mexes; carrega nos botões depressa para soltar | até soltar (máx. 3 s) |
| **Preso** | raízes, teias, armadilhas | não andas, mas podes atacar | 1–3 s |
| **Puxado** | canto da Sereia, Hipnose do Vampiro, Olho do Vazio | és arrastado devagar para o inimigo | 2 s |
| **Partida** | Diabrete | troca a tua arma pela secundária | instantâneo |
| **Controlos trocados** | pólen tonto (andar 29) | esquerda ↔ direita, cima ↔ baixo | 3 s |
| **Transformado em sapo** | Bruxa Anciã | só podes saltar | 3 s |
| **Parado** | Relógio Vivo, Guardião do Tempo | o tempo para para ti: não te mexes | 1–1,5 s |
| **Silêncio** | Anjo do Vazio, Lich | não podes usar skills | 3 s |
| **Encolhido** | Poção de Encolher | passas por buracos pequenos; fazes metade do dano | 30 s |

Os monstros também apanham estes estados. **Bosses** têm resistência: cada estado dura 50% e depois de
o apanharem ficam 10 s imunes a esse estado.

---

## 6. Monstros

### 6.1 Valores por nível (nível L)

| Valor | Fórmula |
|---|---|
| HP | `25 + 22 × L + 0,35 × L²` |
| ATQ | `6 + 2,2 × L + 0,01 × L²` (o termo ao quadrado aperta os andares altos: +20% no nível 50, +40% no 95) |
| DEF | `L` |
| RES | `L × 0,8` |
| XP | `8 + 3 × L^1,3` |
| Ouro | aleatório entre `2 × L` e `3 × L` |

| Nível | HP | ATQ | DEF |
|---|---|---|---|
| 1 | 47 | 8 | 1 |
| 10 | 280 | 28 | 10 |
| 20 | 605 | 50 | 20 |
| 30 | 1 000 | 72 | 30 |
| 50 | 2 000 | 116 | 50 |
| 70 | 3 280 | 160 | 70 |
| 100 | 5 725 | 226 | 100 |

### 6.2 Tipos de monstro (multiplicam os valores acima)

| Tipo | HP | ATQ | DEF | Velocidade | XP | Notas |
|---|---|---|---|---|---|---|
| Fraco | ×0,6 | ×0,8 | ×0,5 | ×1,0 | ×0,6 | aparece em grupos |
| Normal | ×1 | ×1 | ×1 | ×1 | ×1 | |
| Rápido | ×0,7 | ×0,9 | ×0,7 | ×1,4 | ×1 | |
| Tanque | ×2,2 | ×1,1 | ×1,8 | ×0,7 | ×1,6 | |
| Atirador | ×0,8 | ×1,0 | ×0,8 | ×0,9 | ×1,1 | ataca de longe, foge se estás perto |
| Mago | ×0,7 | ×1,3 | ×0,6 | ×0,9 | ×1,2 | dano mágico |
| Voador | ×0,8 | ×1,0 | ×0,7 | ×1,2 | ×1,1 | ignora buracos e água |
| **Elite** | ×2,5 | ×1,3 | ×1,3 | ×1,1 | ×3 | 5% de hipótese; brilha; drop melhor garantido |
| **Monstro com nome** | ×5 | ×1,4 | ×1,5 | ×1,1 | ×8 | único, aparece com aviso do Sistema |
| **Guardião do andar** | ×6 | ×1,5 | ×1,5 | — | ×10 | 1 por andar, guarda a escada |
| **Mini-boss** | ×15 | ×1,7 | ×1,8 | — | ×25 | andares 5, 15, 25… |
| **Boss** | ×24 | ×1,6 | ×2,0 | — | ×50 | andares 10, 20, 30… (afinado com o robô: era ×30 / ×2,0, ver secção 23) |

### 6.3 Nível dos monstros em cada andar
- Monstros normais do andar **N**: nível **N** (alguns N−1 ou N+1).
- Guardião do andar: **N + 1**. Mini-boss: **N + 2**. Boss: **N + 3**.
- Monstro com nome: **N + 2**.

### 6.4 Inteligência artificial (máquina de estados)

```
DESCANSO ──(jogador a menos de "visão")──► ALERTA (0,5 s, "!" por cima)
    ▲                                          │
    │                                          ▼
REGRESSO ◄──(longe do ponto inicial > 25 m)── PERSEGUIR ──(no alcance)──► ATACAR
    │                                          ▲                            │
    └──(chegou ao ponto) → DESCANSO            └──────(recarga)─────────────┘
FUGIR: se HP < 20% e o monstro for "cobarde"
MORTO: animação morrer → drops → desaparece em 2 s
```

| Parâmetro | Valor normal |
|---|---|
| Visão | 8 m (à noite 6 m, monstros noturnos 10 m) |
| Ouvir | 4 m (mesmo atrás) |
| Distância máxima do ponto inicial | 25 m (depois volta e recupera HP) |
| Antes de cada ataque | **aviso** (*telegraph*): a pose de preparação dura 0,3–0,8 s |
| Ataques ao mesmo tempo | no máximo 3 monstros atacam o jogador ao mesmo tempo; os outros rodeiam |

### 6.5 Aparecimento (spawn)
- Cada andar tem **zonas de monstros** com uma lista de quem aparece e quantos.
- Os monstros mortos **voltam a aparecer** passados 3 minutos, longe da vista do jogador.
- Ao sair do andar e voltar, tudo é sorteado de novo (posições de monstros, baús e materiais).
- **Guardiões e bosses** só voltam passado **1 dia de jogo** (dão menos recompensas da 2.ª vez em diante).

---

## 7. Bosses

- **Arena fechada**: ao entrar, a porta fecha. Sair só morrendo ou ganhando.
- **Barra de vida grande** no cimo do ecrã com o nome e o título.
- **Fases**: a cada limiar de HP (normalmente 70% e 35%) o boss muda de fase: ataques novos,
  mais rápido, e uma pequena cena (1–2 s, o boss fica invencível).
- **Fúria**: se a luta passar de 5 minutos, o boss fica 30% mais rápido.
- **Aviso** de todos os ataques: pose de preparação + marca no chão (vermelho = área de dano).
- **Pausa** entre ataques: depois de cada ataque o boss (e o mini-boss) fica **1,8 s** sem atacar
  (`boss_pausa_ataques`) — é a janela para lhe bater. Sem ela o boss atacava sem parar.
- **Recompensas da 1.ª vez**: arma única garantida (bosses e mini-bosses), troféu para a casa,
  muita XP, ouro e materiais raros, e desbloqueio do próximo andar.
- Detalhes de cada boss em `docs/BOSSES.md`; guardiões nos ficheiros das regiões.

---

## 8. Morrer

- Ecrã: `[Sistema] Os teus pontos de vida chegaram a zero.` e acordas na **Estalagem** (ou no último
  acampamento com cama, se tiveres dormido lá).
- Perdes **30% dos materiais** apanhados **nesse andar** desde a última Zona Segura (escolhidos ao acaso).
- **Não perdes**: ouro, armas, armaduras, XP, itens de missão.
- O dia avança para as 6:00 do dia seguinte.
- Em **Hardcore**: o jogo acaba (o ficheiro fica como "memorial").

---

## 9. Drops e raridade

### 9.1 Como funciona um drop
Cada monstro tem uma **tabela de drops**: cada linha tem um item e uma hipótese. Rola-se cada linha.

```
hipótese_final = hipótese × (1 + SOR × 0,003) × bónus (Elite ×2, Skill "Sorte do Herói" ×1,3)
```

### 9.2 Raridade de armas e armaduras que caem ou saem de baús

| Raridade | Hipótese base | Multiplicador de stats |
|---|---|---|
| Comum | 60% | ×1,00 |
| Incomum | 25% | ×1,10 |
| Raro | 10% | ×1,25 |
| Épico | 4% | ×1,45 |
| Lendário | 0,9% | ×1,70 |
| Mítico | 0,1% (só a partir do andar 91) | ×2,00 |

- A Sorte desloca as hipóteses: cada 50 de SOR passa 1% de Comum para as raridades acima.
- **Proteção contra azar**: se abrires 30 baús de prata ou ouro sem um Épico, o próximo é Épico garantido.

### 9.3 Baús

| Baú | Onde | Conteúdo |
|---|---|---|
| Madeira | 6–10 por andar | 2–4 materiais, ouro, às vezes poção |
| Prata | 1–3 por andar, em sítios difíceis | 1 arma ou armadura (Incomum ou mais), materiais raros |
| Ouro | 0–1 por andar, **precisa de chave** | 1 item Raro ou mais + gema + muito ouro |
| Mímico | 10% dos baús de madeira a partir do andar 6 | é um monstro (Tanque, nível N+2) com drop de baú de prata |
| Baú do guardião | ao derrotar o guardião | arma de guardião (30%), troféu, materiais |

---

## 10. Economia

| Coisa | Regra |
|---|---|
| Ouro inicial | 100 |
| Vender ao NPC | 30% do preço de compra (Rook paga 40% por itens "duvidosos") |
| Preço de arma normal | `150 × tier^2,2` (tier = 1 a 10, ver `docs/ARMAS.md`) |
| Preço de armadura (peça) | 60% do preço de uma arma do mesmo tier |
| Poção de Vida pequena / média / grande / máxima | 30 / 150 / 600 / 2 500 |
| Dormir na estalagem | grátis na 1.ª semana; depois 20 ouro. Grátis com 8 corações da Dona Marta ("o quarto é teu") ou com casa própria |
| Teletransporte para um andar | grátis (só para quem está registado na Guilda: quem não está vai sempre parar ao andar 1 — `[Sistema] Passageiro não registado.`) |
| Lojas | o stock muda todos os dias às 6:00; itens raros do Tobias mudam a cada 3 dias |
| Descontos de amizade | 2 corações 5%, 8 corações 15% (só NPCs com loja) |

---

## 11. Crafting

### 11.1 Regras
- Cada receita tem: **ingredientes**, **ouro**, **estação** (forja, mesa de alquimia, fogão, tear,
  bancada do Gizmo, mesa de joalharia) e **skill de vida mínima**.
- Fazer um item demora 1–3 s (barra) e dá XP à skill de vida.
- **Receitas** aprendem-se: com NPCs (amizade, missões), livros encontrados na torre, ou ao apanhar
  todos os ingredientes uma vez ("Descobriste uma receita!").

### 11.2 Qualidade
Itens feitos por ti têm **qualidade**: Normal (×1), Boa (×1,1), Excelente (×1,2).
`hipótese de Boa = 10% + skill × 0,8%` · `hipótese de Excelente = 2% + skill × 0,3%`
(com **Mestre Artesão** ×2).

### 11.3 Melhorar armas e armaduras (+1 a +10)

| Melhoria | Sucesso | Custo (materiais do tier da arma) | Ouro |
|---|---|---|---|
| +1 a +5 | 100% | 1 a 5 lingotes | 10% do preço × nível |
| +6 | 90% | 6 lingotes + 1 cristal | 10% × 6 |
| +7 | 75% | 7 lingotes + 1 cristal | 10% × 7 |
| +8 | 60% | 8 lingotes + 2 cristais | 10% × 8 |
| +9 | 45% | 9 lingotes + 2 cristais + 1 gema | 10% × 9 |
| +10 | 30% | 10 lingotes + 3 cristais + 1 gema | 10% × 10 |

- Falhar gasta os materiais, mas **a arma nunca se parte nem desce**.
- Cada falhanço seguido dá +5% de sucesso à tentativa seguinte (reinicia ao acertar).
- Cada +1 dá **+5% de ATQ** (+10 = +50%). Skill Ferraria: +0,2% de sucesso por nível.

### 11.4 Reciclar
O Brom desfaz uma arma ou armadura em 50% dos materiais usados para a fazer.

---

## 12. Recolha

| Nó | Ferramenta | Dá | Volta a aparecer |
|---|---|---|---|
| Minério | Picareta (ou Martelo como arma) | minério do tier da região, às vezes gema | ao sair e voltar ao andar |
| Árvore | Machado (ferramenta ou arma) | madeira, às vezes seiva ou ninho | idem |
| Erva / flor | à mão | ervas | idem |
| Cristal | Picareta de tier igual ou maior | cristais | 1 dia |
| Ponto de pesca | Cana | peixe (minijogo) | sempre |
| Carcaça / ninho | à mão | pele, ossos, ovos | idem |

- Cada nó dá 1–3 itens; a skill de vida dá +1% por nível de hipótese de item extra.
- **Ferramentas têm tier**: uma picareta de Cobre não parte minério de Prata
  (aparece `[Sistema] É preciso uma Picareta de Prata ou melhor.`).

---

## 13. Inventário e armazém

| Espaço | Tamanho | Como aumentar |
|---|---|---|
| Mochila | 30 espaços | Elva faz mochilas: 40 / 50 / 60 / 80 |
| Itens empilháveis | até 99 por espaço | — |
| Barra rápida | 6 espaços (poções, comida, bombas) | — |
| Baú da estalagem | 100 espaços | — |
| Baús da casa | 50 por baú, até 8 baús | construir mais baús |
| Bolsa de materiais | ilimitada para materiais de crafting | desbloqueia com 6 corações da Lyra |

Itens de missão não ocupam espaço (ficam no Diário).

---

## 14. Tempo

| Coisa | Valor |
|---|---|
| 1 hora de jogo | 50 segundos reais (1 dia = 20 minutos) |
| Começo do dia | 6:00 |
| Dia | 6:00–18:00 · Entardecer 18:00–20:00 · Noite 20:00–5:00 · Madrugada 5:00–6:00 |
| Calendário | 4 estações de 28 dias (Primavera, Verão, Outono, Inverno) |
| Semana | 7 dias: Segunda, Terça, Quarta, Quinta, Sexta, Sábado, Domingo. Cada estação tem 4 semanas e começa numa Segunda. Ao Domingo algumas pessoas mudam de rotina (ver `docs/dialogos/`) |
| Dormir | salta para as 6:00 do dia seguinte e grava o jogo |
| Às 2:00 sem dormir | ficas "cansado": −20% em tudo até dormires |
| Dentro da torre | o tempo passa igual; em andares "fechados" (grutas, edifícios) a hora só muda a luz da entrada |

### 14.1 Tempo atmosférico (cidade e andares ao ar livre)

| Estação | Sol | Chuva | Trovoada | Nevoeiro | Neve |
|---|---|---|---|---|---|
| Primavera | 55% | 30% | 5% | 10% | 0% |
| Verão | 75% | 10% | 10% | 5% | 0% |
| Outono | 45% | 30% | 5% | 20% | 0% |
| Inverno | 40% | 10% | 0% | 15% | 35% |

Os andares têm o seu próprio clima (ver os ficheiros das regiões): por exemplo, o Gelo tem sempre neve e o
Deserto tem tempestades de areia. Chuva deixa tudo **Encharcado**; à noite há monstros diferentes.

---

## 15. Amizade

- Cada NPC principal tem **0 a 1000 pontos**; **1 coração = 100 pontos**.

| Ação | Pontos |
|---|---|
| Falar pela 1.ª vez no dia | +20 |
| Presente "adora" | +80 (no aniversário ×8) |
| Presente "gosta" | +45 |
| Presente "neutro" | +20 |
| Presente "não gosta" | −20 |
| Presente "detesta" | −40 |
| Acabar uma missão do NPC | +100 a +200 |
| Escolha de diálogo que agrada / desagrada | +30 / −30 |
| Ir ao festival com ele | +100 |
| Uma semana sem falar (a partir de 6 corações) | −10 |

- 1 presente por dia e 2 por semana por NPC (no aniversário não conta).
- As **cenas de coração** acontecem quando chegas a 2, 4, 6, 8 e 10 corações e cumpres a condição
  (sítio e hora, ver `docs/NPCS.md`).

---

## 16. Missões e rank

| Rank | Pontos de Guilda precisos | Abre |
|---|---|---|
| F | 0 | missões F, andares 1–10 |
| E | 100 | missões E |
| D | 400 | missões D, Arena (bronze) |
| C | 1 200 | missões C, mercado negro do Rook |
| B | 3 000 | missões B, Arena (prata) |
| A | 7 000 | missões A |
| S | 15 000 | missões S, Arena (ouro) |
| SS | 30 000 | missões SS |
| SSS | 60 000 + andar 100 | título "Lenda de Ascendia" |

Missão de rank R dá: F 10, E 20, D 40, C 80, B 150, A 300, S 600, SS 1 200 pontos.
Estados de uma missão: **Disponível → Aceite → Concluída (entregar) → Entregue**. Máximo de 10 missões aceites.

---

## 17. Viagens

- **Cristal de teletransporte** em cada Zona Segura: vai para a cidade ou para qualquer Zona Segura já visitada.
- **Pedra de Regresso** (item, 50 ouro): volta à cidade de qualquer sítio fora de combate (3 s a canalizar).
- Na cidade: a entrada da torre tem o **Cristal Mestre** com a lista de todos os andares desbloqueados.
- Andar desbloqueia ao **derrotar o guardião** do andar anterior (ou o mini-boss / boss).

---

## 18. Gravar o jogo

- **3 ficheiros** de jogo.
- Grava automaticamente ao: dormir, entrar numa Zona Segura, derrotar um guardião ou boss, entrar na cidade.
- Pode-se gravar à mão em qualquer cama ou cristal de Zona Segura.
- O que se grava: ver `docs/PROGRAMACAO.md`, secção "Formato do ficheiro de gravação".

---

## 19. Dificuldade

| Modo | Dano recebido | Dano feito | Perda ao morrer | Notas |
|---|---|---|---|---|
| História | ×0,5 | ×1,3 | nada | para quem só quer ver a história |
| Normal | ×1 | ×1 | 30% dos materiais do andar | |
| Difícil | ×1,5 | ×0,9 | 50% dos materiais do andar | monstros com mais ataques; drops ×1,2 |
| Hardcore | ×1,5 | ×0,9 | o jogo acaba | só se escolhe ao criar o jogo |

**Novo Jogo+** (depois de um final): manténs nível, armas, armaduras, receitas, coleções e casa;
os monstros ficam com nível +100 em relação ao normal e aparecem drops "Despertos".

---

## 20. Companheiros

- Até **3 companheiros** na equipa, controlados pelo jogo (quem são e como se arranjam: `docs/NPCS.md`, secção 4).
  Os dados ficam em `dados/companheiros.json` (26: 6 da história, 12 da Guilda, 8 escondidos).
- **Onde se arranjam**: os da história (falar com eles → *Convidar para o grupo*, quando a condição estiver feita), os
  **aventureiros da Guilda**, que se contratam à Lyra (preço pago uma vez; 4 no início e mais à medida que sobes) e os
  **escondidos**, num sítio afastado do andar deles (falar com eles e cumprir o que pedem).
- **Habilidade especial** (só os escondidos): uma passiva que mais ninguém tem (cura do grupo, +30% ouro, íman de 8 m,
  metade do dano, inimigos lentos à volta, renascer uma vez por andar, invisível para os monstros, +15% ATQ/DEF ao grupo).
  Os escondidos têm **×1,1** em HP e ATQ.
- **Nível**: igual ao teu −2 (mínimo 1). **Atributos**: 5 em cada + 5 pontos por nível, repartidos pelo estilo
  (ex.: tanque VIT 2 · FOR 2 · AGI 1). HP, DEF e ATQ saem das mesmas fórmulas do herói (secções 2 e 4) com a arma e a
  armadura que lhes deres. Os aventureiros da Guilda têm **×0,85** em HP e ATQ (são menos experientes).
- **Equipamento** (janela *Grupo*): 1 arma dos tipos que sabem usar + peças de armadura (cabeça, corpo, mãos, pés),
  dadas da tua mochila; ao tirá-las voltam para a mochila. Sem nada dado, usam o **equipamento próprio**: a arma do tier
  do nível deles, gasta (ATQ ×0,9), e uma armadura leve (por cada espaço vazio, 50% da DEF/RES da peça do tier). A arma
  e as peças que lhes deres (com melhorias, raridade e qualidade) substituem as deles.
- **Mochila do companheiro**: até **5 poções de vida** que lhes dás; bebem uma abaixo de **35% HP** (recarga 8 s).
- **Habilidades**: a **skill própria** (recarga 15 s) + **1 skill ensinada**: escolhes uma das tuas skills ativas do
  tipo da arma deles (para os de cajado, as skills de cajado); usam-na com a recarga +50%.
- **IA**: seguem-te a 2–4 m, atacam o alvo que tu atacas (ou o inimigo mais perto de ti), saem das áreas vermelhas
  (avisos), usam a skill quando há inimigos perto.
- **Ordens** (tecla **T** roda as ordens; também na janela *Grupo*): **Atacar** (vão a qualquer inimigo até 10 m),
  **Defender-me** (ficam a 2 m e só atacam o que estiver a 3 m de ti), **Ficar** (param onde estão e lutam ali),
  **Seguir** (não lutam, só te seguem).
- **Cair**: com 0 HP ficam caídos; levantam-se passados **30 s** com 50% HP, ou logo se lhes deres uma poção tua
  (tecla **E** ao pé deles).
- Os monstros atacam o mais perto (tu ou um companheiro); os bosses e guardiões continuam a escolher-te a ti.
- O XP, o ouro e os drops dos monstros que eles matam são teus.
- Ganham amizade contigo ao lutarem juntos (**+5 por andar completado**). Só sobem a torre contigo (na cidade estão
  nos sítios deles).
- Números em `dados/constantes.json` → `companheiros` (máximo 3, nível −2, ×0,85 Guilda, ×1,1 escondidos, poções 5 a 35%, recargas 15 s e
  ×1,5, levantar 30 s com 50%, +5 amizade, seguir 2–4 m, raio de ataque 10 m, de defesa 3 m).

---

## 21. Animais de estimação e montadas

| | Regra |
|---|---|
| Animal de estimação | nível 1–20; sobe com XP partilhada (10% da tua); 1 habilidade passiva + 1 ativa (recarga 20 s) |
| Felicidade | 0–100; sobe com comida e carinho (interagir); com 100 a habilidade fica 50% mais forte |
| Montada | chamar com um botão (2 s, fora de combate); velocidade 9–12 m/s; sair ao levar dano |
| Montadas especiais | Salamandra Gigante anda por cima de lava; Cavalo-marinho só na água; Grifo salta buracos até 8 m |

---

## 22. Constantes (para o ficheiro de dados)

Todos estes valores ficam em `dados/constantes.json`, por exemplo:

```json
{
  "atributo_inicial": 5,
  "pontos_por_nivel": 5,
  "nivel_maximo": 100,
  "xp_base": 50, "xp_expoente": 1.6,
  "esquiva_custo": 25, "esquiva_distancia": 3.0, "esquiva_invencivel": 0.25,
  "critico_base": 0.05, "critico_dano": 1.5,
  "hora_em_segundos": 50,
  "perda_materiais_morte": 0.3,
  "elite_hipotese": 0.05
}
```

---

## 23. Equilíbrio: o jogador esperado e os robôs

Para medir a dificuldade sem jogar à mão há duas ferramentas (ver `docs/PROGRAMACAO.md`, secção 10):

- `ferramentas/equilibrio.py` — **só contas**: para cada andar 1–100, golpes para matar cada monstro, golpes que o
  herói aguenta e a duração da luta com o guardião / boss. Escreve também `testes/jogador_esperado.json`.
- `testes/robo_jogar.tscn` (+ `ferramentas/robo_jogar.py`) — um **robô que joga** o andar a sério (anda, ataca em
  combo, esquiva-se de metade dos avisos, bebe poções abaixo de 35% de HP, vai ao guardião) e conta tudo; também
  passeia por Ascendia (edifícios, janelas, lojas), atravessa as pontes e verifica os mapas.

**O jogador esperado no andar N** (o que um jogador normal tem ao chegar lá):

| | Regra |
|---|---|
| Nível | N (no andar 1, nível 1) |
| Atributos | os pontos ganhos repartidos FOR 40% · VIT 30% · AGI 20% · DES 10% |
| Arma | Espada do tier da região a partir do 3.º andar da região (+0 a +3); nos 2 primeiros, a da região anterior +4 |
| Armadura | nenhuma nos andares 1–2; corpo e cabeça nos 3–5; o conjunto todo depois (tier e melhoria da arma) |
| Poções | 5 do tamanho da região (P até ao andar 20, M até 40, G até 90, Máxima depois) |
| Classe | Espadachim no nível 10, Mestre de Lâminas no 40, Santo da Espada no 70 |
| Manejo de Espada | 200 golpes por andar subido |

**Alvos** (secção 10 de `PROGRAMACAO.md`): monstro normal 4–8 golpes (na Demo pode ser menos); guardião 30–50 golpes;
boss 2–4 minutos. **O que o robô mediu** (outubro, depois das correções; esquiva 50%):

| Andares | Golpes para matar (normal / tanque) | Golpes que aguenta | Mortes em 2 min | Chefe |
|---|---|---|---|---|
| 1–4 (Demo) | 2–4 | 18–20 | 0 | guardiões 15–21 s |
| 5–10 (Demo) | 4–9 (tanques 8–12) | 14–19 | 0–1 | Javali-Rei ~65 s sem morrer; Ent Ancião: ~metade do HP por vida (2 tentativas; com 80% de esquiva quase à 1.ª) |
| 15–35 | 5–8 (tanques 12–14) | 18–19 | 0–1 | Aranha-Mãe ~65 s; Golem de Cristal ~2/3 do HP por vida |
| 50–95 | 6–14 (tanques até 30) | 31–39 | 0 | Dragão de Gelo 170 s, Administrador 265 s, sem morrer |

**Afinações feitas com o robô**: Boss HP ×30 → **×24** e ATQ ×2,0 → **×1,6**, mais a **pausa de 1,8 s** entre ataques
(antes o Ent Ancião matava o jogador esperado 12 vezes seguidas e a luta passava dos 5 minutos).

**Decidido:** a partir do andar ~40 o herói aguentava 30–40 golpes de um monstro normal; o ATQ dos monstros ganhou um termo ao quadrado (`6 + 2,2 × L + 0,01 × L²`: +20% no nível 50, +40% no 95; quase nada na Demo).

