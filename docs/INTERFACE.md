# Interface (UI)

Todos os ecrãs, menus e janelas do jogo, para PC (teclado e rato, comando) e telemóvel.
Os controlos estão em `docs/PROGRAMACAO.md`, secção 8.

---

## 1. Estilo

| | |
|---|---|
| Ideia | A interface **é o "Sistema"**: janelas azuis translúcidas com moldura fina e brilhante, como nos animes isekai |
| Cores | fundo `#323353` a 85% de opacidade · moldura `#4d9be6` · brilho `#8fd3ff` · texto `#ffffff` · destaque `#f9c22b` (ouro) · perigo `#e83b3b` · cura `#91db69` |
| Letra | fonte pixel (ex.: *Tiny5* ou *Pixelify Sans*, licença livre) para títulos e números; fonte pixel mais legível para textos longos |
| Animação | as janelas **abrem como um ecrã a ligar** (linha horizontal que se abre) e fecham ao contrário; som "blip" |
| Tamanhos | pensada para 1280×720; escala inteira (×2, ×3) para manter os píxeis nítidos |
| Ícones | 16×16 (itens), 24×24 (skills), desenhados à mão (ver `docs/ARTE.md`) |

---

## 2. HUD (no jogo)

### PC / comando
```
┌───────────────────────────────────────────────────────────────────────┐
│ [retrato] Nome  Nv 23   ▓▓▓▓▓▓▓░░ HP        [Andar 15 · Ninho] 12:40 ☀ │
│           ▓▓▓▓░░░░ MP   ▓▓▓▓▓▓ Est.                      ┌─────────┐   │
│                                                          │ mini-   │   │
│                                                          │  mapa   │   │
│   [Sistema] Obtiveste: Seda de Aranha ×2                 └─────────┘   │
│                                                                       │
│                        (mundo do jogo)                                 │
│                                                                       │
│  ⓘ Missão: O Martelo do Pai — falar com o Brom                        │
│                                                                       │
│ [1][2][3][4][5][6] skills      [Q] poção ×5   [R] arma 2    🐾 Slime │
└───────────────────────────────────────────────────────────────────────┘
```
- **Topo esquerdo**: retrato, nome, nível, barras de HP (vermelho), MP (azul), Estamina (amarelo, só aparece quando se gasta).
  Ícones de **estados** por baixo (veneno, frio…) com tempo.
- **Topo direito**: andar e zona, **hora** e **tempo**, **minimapa** (redondo; mostra NPCs, baús vistos, saída, missão).
- **Barras de região**: Temperatura (região 5), Ar (região 6), Calor (região 7) aparecem por baixo das barras normais.
- **Esquerda**: mensagens `[Sistema]` (empilham e desaparecem em 4 s).
- **Centro em baixo**: missão seguida.
- **Fundo**: barra de **6 skills** com recarga (círculo a encher), poção rápida, arma secundária, animal de estimação.
- **Bosses**: barra de vida grande no cimo com nome e título; marcas nas barras indicam as fases.
- **Companheiros**: retratos pequenos com barra de vida à esquerda.

### Telemóvel
```
┌──────────────────────────────────────────────────────────┐
│[⏸] [retrato] HP ▓▓▓▓░  MP ▓▓░                 [mapa] ◯   │
│                                                          │
│                                                          │
│                     (mundo)                              │
│                                                          │
│   ◯                                         [S1][S2]     │
│ joystick                              [S3]  (ATACAR)     │
│                                       [S4]   [esquiva]   │
│ [mochila]                   [poção] [usar]               │
└──────────────────────────────────────────────────────────┘
```
- Joystick à esquerda (onde tocares), botão de **ataque grande** à direita, **esquiva**, 4 skills (deslizar para mudar de página),
  poção, "Usar" (só aparece quando há algo para interagir).
- **Opções**: tamanho e transparência dos botões, **modo canhoto** (inverte), vibração.
- O jogo respeita o *notch* e as bordas curvas.

### Números e avisos no mundo
- **Números de dano** saltam (branco, amarelo crítico, azul magia, verde cura, roxo veneno, cinzento "IMUNE").
- Ícone **"!"** por cima de inimigos que te viram; **"?"** quando perdem a tua pista.
- **Marcas vermelhas** no chão nos ataques dos inimigos (aviso).
- NPCs com missão: **"!"** amarelo; missão para entregar: **"?"** amarelo; aniversário: 🎂.

---

## 3. Janelas do Sistema (mensagens)

| Tipo | Exemplo | Como aparece |
|---|---|---|
| Notificação | `[Sistema] Obtiveste: Gel de Slime ×2` | canto, 4 s |
| Nível | `[Sistema] Subiste para o nível 12!` | centro, grande, com som e brilho |
| Skill | `[Sistema] Manejo de Espada subiu para Nv 3. Novo ataque: Corte Duplo` | centro, médio |
| Monstro com nome | `[Sistema] Um monstro com nome apareceu neste andar: Slime Rei.` | topo, a piscar |
| Missão | `[Sistema] Missão concluída: Lobos à Noite` | centro |
| Aviso | `[Sistema] É preciso uma Picareta de Prata ou melhor.` | perto do objeto |
| História | janelas grandes com texto que muda ao longo do jogo (ver `docs/HISTORIA.md`) | centro, o jogo pausa |
| Falhas (região 10) | janelas com letras trocadas, cores erradas, a tremer | qualquer sítio |

---

## 4. Menu principal do jogo (pausa)

Abre com `Esc` / Start / botão ⏸. Separadores (troca com Q/E ou LB/RB):

| Separador | O que tem |
|---|---|
| **Mochila** | grelha de itens com filtros (tudo, equipamento, consumíveis, materiais, missão); ordenar; ver detalhes; usar, equipar, deitar fora; peso atual |
| **Equipamento** | o herói ao centro (a arma aparece na mão) com os espaços à volta (ver `docs/EQUIPAMENTO.md`); comparar stats (setas verdes/vermelhas) |
| **Status** | a janela azul do Sistema: nível, XP, atributos (botões "+" para distribuir pontos), HP/MP/Estamina, ATQ/DEF/RES, crítico, resistências, Skill Única, classe, título, rank |
| **Skills** | árvore da classe (base → avançada → lendária), skills de armas (níveis 1–10), skills de vida (1–50); arrastar skills para a barra |
| **Diário** | missões (história ⭐, ativas, concluídas), **páginas de lore** (o diário de Aren, ler), **Bestiário** (com o Fausto), coleções, títulos, conquistas, calendário (aniversários e festivais) |
| **Mapa** | mapa do andar atual (zonas, baús abertos/não, segredos encontrados, % explorado) e **mapa da torre** (100 andares em coluna, com regiões, bosses vencidos, povoações, onde está a Cidade Errante) |
| **Amizades** | os NPCs com corações, presentes que já sabes que gostam, próxima cena de coração |
| **Grupo** | companheiros (equipar, ordens) e animal de estimação (felicidade, nível) |
| **Opções** | secção 7 |
| **Gravar / Sair** | gravar (só em camas e cristais), sair para o menu |

---

## 5. Outras janelas

| Janela | Como é |
|---|---|
| **Diálogo** | caixa em baixo com retrato à esquerda (emoção), nome, texto letra a letra, escolhas em lista; botão "registo" para reler |
| **Loja** | lista de itens com preço e quantidade; separadores Comprar / Vender / Recomprar; comparação com o equipamento |
| **Crafting** | lista de receitas conhecidas (filtrar por "posso fazer"), ingredientes com ✓/✗, qualidade possível, botão Fazer (barra de progresso); receitas desconhecidas aparecem como "???" |
| **Melhorar** | arma ao centro, +N atual, hipótese de sucesso em %, materiais; animação de martelo; resultado ✓ ou ✗ |
| **Cristal de teletransporte** | lista de andares por região com as Zonas Seguras visitadas; Ascendia no topo |
| **Quadro da Guilda** | papéis pregados num quadro (cada missão é um papel); rank no canto |
| **Pesca** | barra vertical do minijogo à direita do herói (ver `docs/ATIVIDADES.md`) |
| **Casa (decorar)** | modo de construção: grelha no chão, catálogo de móveis à direita, rodar e mover |
| **Morte** | ecrã escurece; `[Sistema] Os teus pontos de vida chegaram a zero.`; lista do que perdeste; "Acordar" |
| **Carregamento** | arte de um andar com uma **dica** ou uma frase do diário de Aren; barra de progresso |
| **Cena** | barras pretas em cima e em baixo; botão para saltar (segurar 1 s) |

---

## 6. Menu inicial e criação de personagem

**Menu inicial**: a torre à noite com nuvens a passar; logótipo; **Continuar · Novo Jogo · Carregar · Opções · Créditos**;
idioma (PT, EN) no canto; versão do jogo.

**Novo jogo**:
1. Escolher o **espaço de gravação** (1–3).
2. **Dificuldade** (História, Normal, Difícil, Hardcore).
3. **Criar personagem**: nome; tom de pele (6), cor do cabelo (10), penteado (8), cor dos olhos (6), roupa do mundo real (4 conjuntos)
   — tudo feito com **trocas de cor** e poucas variações de sprite (ver `docs/ARTE.md`).
   **Tratamento** (como as pessoas falam contigo): *ele* · *ela* — muda as palavras com género nos diálogos (`{o/a}`, ver `docs/dialogos/README.md`).
4. Começa o prólogo (H_00).

---

## 7. Opções

| Grupo | Opções |
|---|---|
| **Gráficos** | qualidade (Alta, Normal, Leve), modo retro (pixel grande), sombras, partículas, limite de FPS (30/60/sem limite), ecrã inteiro, escala da interface |
| **Som** | volume geral, música, efeitos, vozes (bips), ambiente |
| **Controlos** | mudar teclas, sensibilidade, vibração, inverter eixos, tamanho e transparência dos botões (telemóvel), modo canhoto |
| **Jogo** | velocidade do texto, idioma, mostrar números de dano, mostrar dicas, gravação automática |
| **Acessibilidade** | tamanho do texto, **modo daltónico** (as marcas de aviso ganham padrões além da cor), **desligar o tremor do ecrã**, **desligar flashes**, legendas para sons importantes, mira assistida, abrandar o jogo (80%) |

---

## 8. Navegação

- Tudo funciona com **teclado**, **rato**, **comando** e **toque**.
- Com comando: foco visível (moldura dourada) em todos os botões; `A` aceita, `B` volta.
- Os ícones dos botões mudam sozinhos conforme o que estás a usar (teclado ↔ comando ↔ toque) — autoload `Entrada`.
