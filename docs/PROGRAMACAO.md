# Guia de programação (Godot 4)

Como o jogo vai ser construído: pastas, cenas, scripts, formatos dos ficheiros de dados e a ordem
de implementação. Com este documento e o `docs/SISTEMAS.md`, programar é seguir os passos.

---

## 1. Decisões técnicas

| Tema | Decisão |
|---|---|
| Motor | **Godot 4** (última versão estável quando começarmos) |
| Linguagem | **GDScript com tipos** (`var vida: int = 100`) |
| Nomes no nosso código | **português sem acentos**, minúsculas com `_` (`vida_maxima`, `func receber_dano()`); classes em `PascalCase` (`Monstro`, `ArmaDados`) |
| Renderizador | **Forward+** no PC; **Mobile** no Android; **Compatibility** na Web (gráficos mais simples) |
| Resolução base | 1280×720, a escalar; interface pensada também para 16:9 e telemóvel 20:9 |
| Física | Jolt (se disponível) ou física 3D normal do Godot; 60 Hz |
| Dados do jogo | ficheiros **JSON** em `dados/` (fáceis de editar e de traduzir) |
| Traduções | ficheiros **CSV** do Godot (`traducoes/textos.csv`) com colunas `chave, pt, en` |
| Testes | addon **GUT** (Godot Unit Test) para fórmulas e regras |
| Builds | **GitHub Actions** com Godot sem ecrã (*headless*) → Windows, Linux, Web, Android |

---

## 2. Estrutura de pastas do projeto

O projeto Godot fica na **raiz do repositório** (`project.godot` na raiz).

```
/
├─ project.godot
├─ arte/                     ← a tua arte (ver docs/ARTE.md)
├─ dados/                    ← tudo o que é "conteúdo" em JSON
│   ├─ constantes.json
│   ├─ armas.json            armaduras.json   acessorios.json
│   ├─ itens.json            receitas.json    lojas.json
│   ├─ monstros.json         bosses.json      guardioes.json
│   ├─ andares/a001.json … a100.json
│   ├─ regioes.json          povoacoes.json
│   ├─ npcs.json             presentes.json
│   ├─ dialogos/<npc>.json
│   ├─ missoes.json          conquistas.json  titulos.json
│   ├─ skills.json           classes.json     skills_unicas.json
│   └─ peixes.json           plantas.json     animais.json
├─ traducoes/textos.csv
├─ cenas/
│   ├─ principal.tscn        (arranque → menu)
│   ├─ menu/                 menu_inicial, criar_personagem, opcoes, carregar
│   ├─ mundo/                cidade.tscn, andar.tscn, arena_boss.tscn, casa.tscn
│   ├─ personagens/          jogador.tscn, npc.tscn, companheiro.tscn, animal.tscn, montada.tscn
│   ├─ monstros/             monstro_base.tscn + 1 cena por monstro que herda da base
│   ├─ bosses/               boss_base.tscn + 1 cena por boss
│   ├─ objetos/              bau.tscn, no_recolha.tscn, cristal.tscn, porta.tscn, alavanca.tscn,
│   │                        placa_pressao.tscn, item_chao.tscn, projetil.tscn, ponto_pesca.tscn
│   ├─ efeitos/              numero_dano.tscn, particulas/…, flash.tscn
│   └─ ui/                   hud, dialogo, inventario, status, crafting, loja, mapa, diario,
│                            bestiario, pausa, mensagem_sistema, minijogo_pesca, cartas, …
├─ scripts/
│   ├─ autoload/             (ver secção 3)
│   ├─ combate/              dano.gd, estados.gd, hitbox.gd, hurtbox.gd
│   ├─ ia/                   maquina_estados.gd, estados/*.gd
│   ├─ sistemas/             inventario.gd, crafting.gd, melhorias.gd, recolha.gd, loot.gd,
│   │                        amizade.gd, missoes.gd, pesca.gd, quinta.gd
│   └─ util/
├─ sons/   musica/
├─ addons/gut/
├─ testes/                   testes GUT
└─ .github/workflows/builds.yml
```

---

## 3. Autoloads (scripts globais)

Ficam sempre carregados (Projeto → Definições → Autoload).

| Nome | Para quê |
|---|---|
| `Dados` | Lê todos os JSON de `dados/` no arranque e dá acesso: `Dados.arma("espada_cobre")` |
| `Jogo` | O estado do jogo: jogador (nível, atributos, HP…), inventário, ouro, andares desbloqueados, flags da história, amizades, missões |
| `Tempo` | Relógio, dia/noite, estação, clima; emite sinais `nova_hora`, `novo_dia`, `nova_estacao` |
| `Eventos` | "Central de sinais": `monstro_morto(id)`, `item_apanhado(id, qtd)`, `boss_derrotado(id)`, `missao_mudou(id)`… Os sistemas (missões, conquistas, bestiário) ouvem daqui |
| `Sistema` | Mostra as mensagens azuis `[Sistema] …` e as janelas do Sistema |
| `Gravar` | Gravar e carregar (secção 7) |
| `Cenas` | Troca de cena com ecrã de carregamento e transição |
| `Audio` | Música (com mistura suave entre faixas) e efeitos sonoros |
| `Entrada` | Sabe se o jogador está a usar teclado, comando ou toque, e muda os ícones dos botões |

---

## 4A. Como se faz o 2D no Godot (Fase D do `OBJETIVO.md`)

O jogo passa a ser **desenhado em 2D** (decidido pelo utilizador). Para não perder nada do que já funciona, as contas
do jogo (física, combate, IA dos monstros, puzzles, povoações, masmorras, cidade, interiores) continuam a fazer-se no
plano (x, z), em metros, nos mesmos scripts. A **vista 2D** (`scripts/mundo2d/vista2d.gd`) desenha tudo em 2D por
cima: a câmara 3D continua a existir para as contas, mas não desenha nada (`cull_mask = 0`, `disable_3d`). A **vista
3D antiga foi tirada** (sem opção; só os robôs de teste desligam a vista 2D, para irem mais depressa): a secção 4
abaixo fica a explicar a "maquete" 3D invisível que faz as contas por baixo.

- **Projeção**: 1 m = 16 px. O ponto (x, y, z) fica no ecrã em (x, z − 0,8·y) × 16: o alto sobe e o lado de frente
  vê-se (vista de cima, um pouco de frente). A ordem de desenho é pelo z (**y-sort**): o que está mais a sul
  desenha-se por cima, por isso o herói passa por trás das árvores, das casas e das paredes.
- **Chão** (`scripts/mundo2d/chao2d.gd`): os mesmos blocos de 2 m, alturas e texturas da versão 3D. O chão plano
  fica numa camada por baixo de tudo; os blocos altos (colinas, paredes de rocha) têm o lado de frente à vista e
  entram no y-sort pela beira de trás de cada fila. Água, lava, margens e bordas como no 3D.
- **Espelhos 2D** de cada coisa do mundo 3D: `AnimatedSprite3D`/`Sprite3D` → `AnimatedSprite2D`/`Sprite2D` (as
  mesmas folhas de animação), `Label3D` → `Label`, plantas (MultiMesh) → um `Sprite2D` por planta (abanam ao vento),
  caixas/planos/cilindros (paredes das masmorras, avisos de ataque, tapetes) → o topo e os lados virados para sul,
  `OmniLight3D` → `PointLight2D`, partículas 3D → `CPUParticles2D` (chuva, neve, pirilampos), a luz do sol e do céu →
  a cor de tudo (`CanvasModulate`). As coisas novas (monstros, golpes, números de dano) entram sozinhas.
- **Peças 3D (.glb)** → desenhadas em pixel art (`arte/sprites2d/`, `dados/sprites2d.json`) por
  `ferramentas/arte/glb2d.py`: lê os triângulos de cada .glb (`glb_ler.py`) e pinta-os na mesma projeção, com
  padrões pelo nome do material (telhas, tijolos, tábuas, troncos, folhagem, neve, cristal...), luz de cima à
  esquerda, aresta clara no cimo das paredes e contorno #2e222f (4 rotações; as do kit, 1; as pontes, 4).
  Sempre que se muda um `.glb`, corre-se outra vez para essa peça: `python3 ferramentas/arte/glb2d.py <peça.glb>`.
  (As antigas "fotografias" de `glb_sprites.gd` ficam só como ferramenta de comparação.)
- **Móveis**: os básicos têm desenho próprio em pixel art (`arte/moveis2d/`, `dados/moveis2d.json`, feitos por
  `ferramentas/arte/moveis2d.py`, com profundidade por píxel para as coisas em cima dos móveis ficarem certas); os
  outros usam a fotografia. Dentro de casa, à noite, a luz baixa e acendem-se as velas, os candeeiros e a lareira.
  Os bocados de dentro de uma peça .glb não têm espelho próprio (a peça já tem a imagem inteira).
- **Pontes ("==")**: debaixo é água (no 3D e no 2D); anda-se nas tábuas (a colisão da ponte, com paredes invisíveis
  dos lados) e no 2D as pontes, passadiços e cais ficam numa camada por baixo de quem passa. Não nascem monstros nelas.
- **Tapar o herói**: árvores, casas e paredes de rocha à frente dele abrem uma janela redonda (borda aos quadradinhos).
- **Falésias e paredes**: cantos de fora redondos, contorno escuro de 1 píxel atrás e dos lados, aresta clara em cima
  e na frente, linha escura na base (tudo no shader do chão).
- **Píxeis certos**: plantas e peças escalam só em múltiplos de 1/3 (com o zoom 3 os píxeis ficam todos iguais).
- **Sombras**: elipse no chão debaixo das árvores, arbustos, rochas e peças (um pouco para a direita e para baixo).
- **Luz das grutas**: a cor fica escura e as coisas que brilham (LuzesGruta) e o herói têm luz em 4 degraus.
- **Câmara 2D**: segue o herói (zoom 2×/3×/4× pela roda, como a distância da câmara 3D) e treme como a 3D.

## 4. A maquete 3D por baixo (era a vista 2.5D antiga; hoje não se vê, só faz as contas)

### 4.1 Bonecos (sprites 2D no mundo 3D)
- Cada personagem tem um **`Sprite3D`** com:
  - `billboard = Y` (vira-se sempre para a câmara mas fica de pé)
  - `texture_filter = Nearest` (pixel art nítida)
  - `pixel_size = 0.0625` → **16 píxeis = 1 metro** (o herói, com 26 px de altura, fica com ~1,6 m)
  - `shaded = true` (as luzes do mundo iluminam o boneco) e `alpha_cut = Discard` (para fazer sombra)
- **Herói e armas**: o corpo e a arma são desenhados num **`SubViewport` 2D** pequeno
  (`AnimatedSprite2D` do corpo + `Sprite2D` da arma que roda com um `AnimationPlayer`). A imagem desse
  SubViewport vai para o `Sprite3D` (*ViewportTexture*). Assim a arma roda em 2D por cima do boneco.
- **Espelhar** para a esquerda: `flip_h` no `Sprite3D`.
- **Piscar a branco**: shader simples no material do sprite com um parâmetro `flash` (0 a 1).
- **Sombra no chão**: um `Decal` redondo escuro debaixo de cada personagem (fica melhor do que a sombra real do sprite).

### 4.2 Câmara
- `Camera3D` em perspetiva, **FOV 30°**, inclinada **−35°**, a ~16 m do jogador.
- Segue o jogador com suavização (`lerp` 8 por segundo), um pouco à frente da direção em que anda.
- Zoom com a roda do rato / pinça: 10 m a 24 m.
- Tremer: função `tremer(força, duração)` no script da câmara.
- **Modo retro** (opção): o mundo é desenhado num `SubViewport` de 640×360 e ampliado com *nearest*.

### 4.3 Mundo
- Peças do kit (Blender `.glb`) → cena com as peças → **MeshLibrary** → **`GridMap`** com células de **2×2×2 m**.
- Colisões: no Blender, dar às peças de colisão o sufixo `-colonly` (o Godot cria a colisão sozinho).
- Peças especiais e decoração solta: cenas normais colocadas à mão por cima do GridMap.
- **`NavigationRegion3D`** em cada andar para os monstros encontrarem caminho.
- **`WorldEnvironment`** por andar: cor do céu, nevoeiro, *glow*, luz ambiente (os valores vêm de `dados/andares/aXXX.json`).
- **`DirectionalLight3D`** (sol/lua) que roda com a hora do dia (nunca abaixo de 40°, para as sombras não ficarem
  enormes de manhã), com sombras a 62% (de cor, não pretas); luzes pontuais em tochas, cristais, lava.
- Cor final: saturação 0,9 e contraste 1,06 (`Environment.adjustment`), para a paleta não "gritar" ao sol.
- **Botões**: todos os botões do jogo usam `arte/ui/botao_*.png` ao dobro (tema em `scripts/ui/tema.gd`).
- Partículas com `GPUParticles3D` (folhas, neve, cinza, bolhas, faíscas).

### 4.4 Colisões e combate
- Camadas de física: 1 Mundo · 2 Jogador · 3 Monstros · 4 NPCs · 5 Projéteis · 6 Itens · 7 Interação · 8 Água/Lava.
- **Hitbox** (`Area3D` que causa dano, ligada só durante os frames do golpe) e
  **Hurtbox** (`Area3D` que recebe dano). O cálculo está em `scripts/combate/dano.gd` e segue o `SISTEMAS.md`.
- Os frames em que a hitbox está ativa são marcados no `AnimationPlayer` (pistas de método `ligar_hitbox()` / `desligar_hitbox()`).

---

## 5. Formatos dos ficheiros de dados

### 5.1 Arma (`dados/armas.json`)
```json
{
  "id": "espada_cobre",
  "nome": "ARMA_ESPADA_COBRE",          // chave de tradução
  "tipo": "espada",
  "tier": 1,
  "atq": 12, "atq_magico": 0,
  "velocidade": 1.6, "alcance": 1.8, "critico": 0.05,
  "elemento": null,
  "efeitos": [],
  "nivel_minimo": 1,
  "preco": 150,
  "peso": 2.0,
  "sprite": "res://arte/armas/espada_cobre.png",
  "icone": "res://arte/armas/espada_cobre_icone.png",
  "unica": false
}
```
`efeitos` usa uma lista de efeitos com nomes fixos, por exemplo
`{"tipo": "veneno", "hipotese": 0.25}`, `{"tipo": "roubo_vida", "valor": 0.03}`,
`{"tipo": "projeteis_extra", "valor": 2}`.

### 5.2 Monstro (`dados/monstros.json`)
```json
{
  "id": "lobo_cinzento",
  "nome": "MONSTRO_LOBO_CINZENTO",
  "regiao": 1,
  "tipo": "rapido",
  "fraquezas": ["fogo"], "resistencias": [], "imunidades": [],
  "visao": 9, "cobarde": false, "noturno": false, "grupo": [2, 4],
  "ataques": [
    {"id": "mordida", "mult": 1.0, "alcance": 1.5, "aviso": 0.35, "recarga": 1.2},
    {"id": "investida", "mult": 1.4, "alcance": 6.0, "aviso": 0.6, "recarga": 5.0}
  ],
  "drops": [
    {"item": "pele_lobo", "hipotese": 0.6, "qtd": [1, 2]},
    {"item": "presa_lobo", "hipotese": 0.25, "qtd": [1, 1]}
  ],
  "sprite": "res://arte/regioes/r01_floresta/monstros/lobo_cinzento",
  "tamanho_px": 32
}
```
O nível, HP e ATQ **não** estão aqui: calculam-se com o nível do andar (ver `SISTEMAS.md`, secção 6).

### 5.3 Andar (`dados/andares/a004.json`)
```json
{
  "numero": 4,
  "nome": "ANDAR_4_NOME",
  "regiao": 1,
  "cena": "res://cenas/mundo/andares/a004.tscn",
  "tamanho": [200, 200],
  "ambiente": {"ceu": "#7fa0c8", "nevoeiro": "#c8e0d0", "densidade_nevoeiro": 0.02,
               "luz_ambiente": 0.6, "particulas": "esporos_luminosos", "musica": "floresta_2"},
  "clima": {"sol": 0.5, "chuva": 0.3, "nevoeiro": 0.2},
  "zonas": [
    {"id": "entrada", "monstros": [["slime_verde", 4], ["cogumelo_andante", 3]]},
    {"id": "clareira_grande", "monstros": [["cogumelo_andante", 6], ["fada_travessa", 2]]}
  ],
  "recolha": {"minerio_cobre": 6, "carvalho": 8, "cogumelo_luminoso": 12},
  "baus": {"madeira": [6, 9], "prata": [1, 2], "ouro": [0, 1]},
  "guardiao": "rainha_dos_esporos",
  "povoacao": null,
  "pagina_lore": 4,
  "segredos": ["cogumelo_oco"],
  "desafios": ["sem_dano", "matar_30_em_3min"]
}
```

### 5.4 NPC (`dados/npcs.json`) e presentes
```json
{
  "id": "brom",
  "nome": "Brom",
  "aniversario": {"estacao": "inverno", "dia": 9},
  "loja": "ferreiro",
  "rotina": {
    "normal": [["06:00", "forja"], ["19:00", "taberna"], ["23:00", "casa_brom"]],
    "chuva":  [["06:00", "forja"], ["21:00", "casa_brom"]],
    "festival": [["10:00", "praca"]]
  },
  "presentes": {"adora": ["minerio_mitril", "assado_javali"], "gosta": ["lingote_*"],
                "detesta": ["flor_*", "gel_slime"]},
  "cenas_coracao": [2, 4, 6, 8, 10],
  "companheiro": false
}
```

### 5.5 Diálogo (`dados/dialogos/brom.json`)
Cada conversa é uma lista de **nós**. Um nó tem quem fala, a emoção do retrato, o texto (chave de
tradução), e pode ter **escolhas**, **condições** e **efeitos**.
```json
{
  "id": "brom_espada_partida",
  "condicao": "missao('M_BROM_01') == 'entregue' && coracoes('brom') >= 1",
  "nos": [
    {"id": "1", "fala": "brom", "emocao": "zangado", "texto": "BROM_ESPADA_1",
     "escolhas": [
       {"texto": "BROM_ESPADA_R1", "ir": "2a"},
       {"texto": "BROM_ESPADA_R2", "ir": "2b", "efeitos": ["amizade(brom, 30)"]},
       {"texto": "BROM_ESPADA_R3", "ir": "2c", "condicao": "flag('andar_18_visitado')"}
     ]},
    {"id": "2b", "fala": "brom", "emocao": "zangado", "texto": "BROM_ESPADA_2B",
     "efeitos": ["sistema('SISTEMA_BROM_REPARA')"], "fim": true}
  ]
}
```
**Condições** disponíveis: `flag(nome)`, `coracoes(npc) >= n`, `andar_maximo >= n`, `hora entre a e b`,
`estacao == x`, `clima == x`, `tem_item(id, qtd)`, `missao(id) == estado`, `boss_derrotado(id)`.
**Efeitos** disponíveis: `amizade(npc, n)`, `dar_item(id, qtd)`, `tirar_item(id, qtd)`, `ouro(n)`,
`flag(nome)`, `missao_iniciar(id)`, `missao_avancar(id)`, `abrir_loja(id)`, `sistema(texto)`, `cena(id)`.

### 5.6 Missão (`dados/missoes.json`)
```json
{
  "id": "M_BROM_01",
  "nome": "MISSAO_BROM_01_NOME",
  "dada_por": "brom",
  "tipo": "recolha",
  "rank": "F",
  "requisitos": {"coracoes": {"brom": 0}, "andar_maximo": 2},
  "passos": [
    {"tipo": "apanhar", "item": "minerio_cobre", "qtd": 10},
    {"tipo": "falar", "npc": "brom"}
  ],
  "recompensas": {"xp": 120, "ouro": 150, "itens": [["picareta_cobre", 1]], "amizade": {"brom": 120},
                  "pontos_guilda": 10, "flags": ["brom_confia"]},
  "repetivel": false
}
```
Tipos de passo: `matar`, `apanhar`, `entregar`, `falar`, `ir_a`, `escoltar`, `derrotar_boss`,
`pescar`, `cozinhar`, `fazer_item`, `explorar_andar(%)`, `esperar_ate(hora)`.

### 5.7 Item, receita e loja
```json
{"id": "pocao_vida_p", "nome": "ITEM_POCAO_VIDA_P", "categoria": "consumivel",
 "efeito": {"curar_hp_percent": 0.30}, "preco": 30, "peso": 0.2, "empilha": 99,
 "icone": "res://arte/icones/pocao_vida_p.png"}

{"id": "R_POCAO_VIDA_P", "estacao": "alquimia", "resultado": ["pocao_vida_p", 2],
 "ingredientes": [["erva_verde", 2], ["agua_limpa", 1]], "ouro": 0, "skill": ["alquimia", 1],
 "aprende": "inicio"}

{"id": "loja_selene", "itens": [["pocao_vida_p", 99], ["antidoto", 10]],
 "itens_por_andar": {"20": [["pocao_vida_m", 20]]}}
```

---

## 6. Monstros e bosses no código

- `monstro_base.gd` tem: estado da IA, HP, receber dano, estados alterados, drops, morrer.
- Cada ataque é um **recurso** (`AtaqueDados`) com: animação, multiplicador, alcance, aviso,
  recarga, hitbox (forma e tamanho), projétil (opcional), efeito (opcional).
- Cada monstro só escolhe ataques que estão **fora de recarga** e **no alcance**, com pesos
  (ex.: mordida 70%, investida 30%).
- `boss_base.gd` herda de `monstro_base.gd` e acrescenta: **fases** (lista de limiares de HP e
  ataques de cada fase), cena de mudança de fase, fúria, barra de vida grande, arena.
- Padrões de bosses descritos como **sequências** nos dados, por exemplo:
  `"fase_2": [["investida", 1], ["chamar_crias", 1], ["mordida", 2]]` em ciclo, com algum acaso.

---

## 7. Formato do ficheiro de gravação

Ficheiro `user://jogo_1.json` (um por espaço de gravação):
```json
{
  "versao": 1,
  "criado": "2026-10-14T15:00:00",
  "tempo_jogado": 12345,
  "jogador": {"nome": "Afonso", "nivel": 12, "xp": 830, "atributos": {"for": 20, "agi": 12, "des": 8, "int": 5, "vit": 15, "sor": 5},
              "pontos_livres": 0, "hp": 300, "mp": 60, "classe": null, "skill_unica": "olho_do_sistema", "origem": "dormir", "tratamento": "ele",
              "titulo": "matador_de_slimes", "skins": {"cor_cabelo": 3}},
  "equipamento": {"arma": "inst_0007", "arma_2": null, "cabeca": "inst_0012"},
  "inventario": [{"inst": "inst_0007", "id": "espada_cobre", "melhoria": 3, "raridade": "raro", "qualidade": "boa", "gema": null},
                 {"id": "minerio_cobre", "qtd": 34}],
  "ouro": 2210,
  "tempo": {"dia": 5, "estacao": "primavera", "ano": 1, "hora": 13.5},
  "andares": {"desbloqueados": 12, "visitados": [1, 2, 3], "explorado": {"1": 1.0, "2": 0.74}},
  "flags": ["prologo_feito", "brom_confia"],
  "missoes": {"M_BROM_01": "entregue", "M_LYRA_02": {"estado": "aceite", "passo": 1, "progresso": 4}},
  "amizade": {"brom": 230, "lyra": 410},
  "skills": {"manejo_espada": [4, 120], "mineracao": [7, 40]},
  "receitas": ["R_POCAO_VIDA_P"],
  "colecoes": {"bestiario": {"slime_verde": 52}, "peixes": {"truta_ribeiro": 3}, "lore": [1, 2, 4]},
  "casa": {"comprada": false},
  "cidade": {"projetos": ["ponte_rio"]},
  "animais": [], "companheiros": [],
  "dificuldade": "normal"
}
```
- Gravar em JSON torna fácil corrigir e ler. Ao carregar, se `versao` for antiga, corre-se uma
  "migração" para a nova.
- Ao gravar, escreve-se primeiro para `jogo_1.tmp` e só depois se troca o nome (para não estragar o ficheiro se o jogo fechar a meio).

---

## 8. Controlos (mapa de entrada)

| Ação (`InputMap`) | Teclado e rato | Comando | Telemóvel |
|---|---|---|---|
| `mover` | WASD / setas | stick esquerdo | joystick à esquerda |
| `apontar` | rato | stick direito (ou direção do movimento) | automático (inimigo mais perto) |
| `atacar` | clique esquerdo | X / □ | botão grande |
| `ataque_forte` (segurar = carregar) | clique direito | Y / △ | segurar o botão grande |
| `esquivar` | Espaço | B / ○ | botão de esquiva |
| `interagir` | E | A / ✕ | botão "Usar" (aparece só quando há algo) |
| `skill_1` … `skill_6` | 1–6 | LB/RB + botões | 4 botões de skill + deslizar para mudar de página |
| `pocao` | Q | ↓ na cruz | botão de poção |
| `trocar_arma` | R | ↑ na cruz | botão pequeno |
| `skill_unica` | F | RT | botão especial |
| `correr` | Shift | carregar no stick esquerdo | duplo toque no joystick |
| `mapa` | M / Tab | View/Select | botão de mapa |
| `inventario` | I | Menu → Inventário | botão de mochila |
| `status` | C | Menu → Status | — (no menu) |
| `diario` | J | Menu → Diário | — (no menu) |
| `pausa` | Esc / P | Start | botão ⏸ |
| `montada` | Z | carregar no stick direito | botão de montada |
| `grupo` (janela do grupo) | G | ← na cruz | — (no menu) |
| `ordem_grupo` (roda as ordens) | T | → na cruz | botão pequeno ao lado da poção |

Todas as teclas podem ser mudadas nas **Opções**.

---

## 9. Ordem de implementação (Fase B do `OBJETIVO.md`)

Cada passo acaba com algo que se pode **jogar e testar**.

1. **Projeto e base**: projeto Godot, pastas, autoloads vazios, `constantes.json`, cena de teste com chão.
2. **Jogador**: sprite 3D billboard com o herói provisório, mover, câmara, esquiva, estamina.
3. **Combate**: hitbox/hurtbox, combo de espada, números de dano, flash, hitstop, um monstro com IA simples.
4. **Dados**: `Dados` a ler armas e monstros do JSON; trocar de arma; 12 tipos de arma com a arma a rodar.
5. **Estados e elementos**: veneno, fogo, gelo…; fraquezas.
6. **Sistema isekai**: XP, níveis, atributos, janela de Status, mensagens `[Sistema]`, skills que sobem com o uso.
7. **Inventário e drops**: apanhar itens, mochila, barra rápida, poções.
8. **Recolha e crafting**: nós de recolha, ferramentas, forja, alquimia, cozinha, melhorias +1…+10.
9. **Andar a partir de dados**: GridMap com o kit, zonas de monstros, baús, Zona Segura, cristal, escada, guardião.
10. **Tempo**: dia/noite, clima, calendário.
11. **NPCs e diálogo**: caixa de diálogo com retrato e escolhas, condições, efeitos, amizade, presentes, rotinas.
12. **Missões e Guilda**: diário, quadro de missões, rank.
13. **Cidade**: cena de Ascendia com os edifícios da Demo, lojas.
14. **Bosses**: `boss_base`, arena, fases; Javali-Rei e Ent Ancião.
15. **Gravar e carregar**, menu inicial, opções.
16. **Pesca**, bestiário, páginas de lore, conquistas, títulos.
17. **Telemóvel**: controlos de toque, interface adaptada, desempenho.
18. **Builds automáticas** e **Demo**.

---

## 10. Testes

- Testes automáticos (GUT) para tudo o que é **fórmula**: dano, XP, drops, melhorias, amizade, tempo.
- **Simulador de equilíbrio**: um script que simula um jogador "médio" a subir os andares (nível, arma do tier,
  pontos em FOR/VIT) e escreve quantos golpes leva a matar cada monstro e boss, e quantos golpes aguenta.
  Objetivo: monstro normal 4–8 golpes; guardião 30–50; boss 2–4 minutos de luta.
- **Teste de cada andar**: um "robô" que entra no andar, verifica que a escada é alcançável a partir da
  Zona Segura (navegação), e que todos os baús e nós de recolha estão em sítios alcançáveis.
- **Feito** (ver `docs/SISTEMAS.md`, secção 23):
  - `python3 ferramentas/equilibrio.py [andares]` — o simulador de equilíbrio (só contas) e o `testes/jogador_esperado.json`.
  - `python3 ferramentas/robo_jogar.py --godot <godot> --sem2d [andares]` — o robô `testes/robo_jogar.tscn` joga cada
    andar 120 s (`--modo boss` vai logo ao chefe e conta uma vida; `--modo pontes` atravessa todas as pontes;
    `--cidade` entra nos edifícios de Ascendia, abre as janelas e as lojas e fala com as pessoas) e junta os erros do
    Godot (SCRIPT ERROR, ERROR, Invalid…) num resumo. Sem `--sem2d` corre também a vista 2D (3× mais lento).
  - `python3 ferramentas/robo_jogar.py --mapas` — sem Godot: a partir da chegada chega-se a pé ao guardião, à
    escada e à Zona Segura?

---

## 11. Builds automáticas (GitHub Actions)

Ficheiro `.github/workflows/builds.yml`:
- Corre em cada *push* para `main` e quando se cria uma *tag* `v*`.
- Usa a imagem Docker com o Godot sem ecrã e os *export templates* da mesma versão.
- Exporta **Windows** (`.exe` em zip), **Linux**, **Web** (para o itch.io) e **Android** (`.apk` de teste;
  o `.aab` para a Play Store com a chave guardada nos *secrets* do GitHub).
- Os ficheiros ficam como *artifacts* da execução; nas tags ficam numa *Release*.
