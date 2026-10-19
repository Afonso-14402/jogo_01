# Missões

Tipos de missões e onde estão escritas:

| Tipo | Prefixo | Onde estão |
|---|---|---|
| **História principal** | `H_` | **aqui** (secção 2) |
| **Guilda** (fixas por rank e geradas) | `G_` | **aqui** (secções 3 e 4) |
| **Festivais** | `F_` | **aqui** (secção 5) |
| NPCs de Ascendia | `N_` | `docs/NPCS.md` (em cada NPC) |
| Regiões (povoações e NPCs da torre) | `R1_`…`R10_` | `docs/regioes/rXX_*.md` (secção 8 de cada região) |

Regras gerais (estados, máximo de missões, pontos de Guilda): `docs/SISTEMAS.md`, secção 16.
Formato dos dados: `docs/PROGRAMACAO.md`, secção 5.6.

---

## 1. Contagem

| Tipo | Quantidade |
|---|---|
| História principal | 27 |
| NPCs de Ascendia | ~45 (mais as das regiões que eles dão) |
| Regiões | 148 (R1 13 · R2 14 · R3 16 · R4 15 · R5 15 · R6 15 · R7 15 · R8 15 · R9 15 · R10 15) |
| Guilda fixas | 27 |
| Guilda geradas | **infinitas** (3 novas por dia) |
| Festivais | 6 (repetem-se todos os anos) |
| **Total escrito** | **~270** |

---

## 2. História principal

As missões da história aparecem no Diário com uma estrela ⭐ e **não podem ser abandonadas**.
A ordem é fixa; algumas têm **escolhas** que mudam o resto do jogo (marcadas com 🔀).

### Prólogo
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_00 | Despertar | Acordas no Prado do Despertar (andar 1). Janela azul: `[Sistema] Bem-vindo, Jogador nº 10 000.` Escolhes o teu nome e aspeto | Tutorial: andar, olhar à volta, apanhar uma pedra, atacar um slime, esquivar | — |
| H_01 | O Primeiro Lobo | Um Lobo Cinzento ataca; o **Kai** salva-te | Sobreviver 20 s · seguir o Kai até à Zona Segura · usar o cristal | Kai apresenta-se |
| H_02 | Ascendia | Chegas à cidade | Falar com a **Lyra** na Guilda · tocar no **Cristal de Avaliação** (Skill Única) · registar-te (rank F) · o Gorvan dá-te uma **Espada de Treino** · a Dona Marta dá-te um quarto | Espada de Treino · 100 ouro · 3 Poções de Vida |
| H_03 | A Primeira Subida | Voltas ao andar 1 sozinho | Vencer o **Coelho-Chifre Ancião** | Andar 2 desbloqueado |

### Capítulo 1 — Floresta
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_04 | O Rei das Tocas | O Kai desafia-te a chegar primeiro ao andar 5 | Chegar ao andar 5 · vencer o **Javali-Rei** | o Kai fica impressionado (❤️) |
| H_05 | A Árvore-Mãe | A torre está "doente" na floresta | Chegar ao andar 10 · vencer o **Ent Ancião** · ouvir a Árvore-Mãe | **Dia da Subida** (festa em Ascendia); abrem a quinta e as melhorias da cidade |

### Capítulo 2 — Cavernas
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_06 | Povos Dentro da Torre | Descobres que há gente a viver dentro da torre | Visitar **Mycélia** (16) · visitar a **Forja Anã** (18) · contar ao Velho Fausto | Página especial "Os Povos da Torre" |
| H_07 | O Rei Sentado | | Vencer o **Golem de Cristal** (20) | **Dia da Subida**; o Governador dá-te a **casa** |

### Capítulo 3 — Pântano
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_08 | 🔀 Ordem da Guilda | O Gorvan manda expulsar os Homens-Lagarto do andar 24 (a Guilda acha que são perigosos). O Chefe Ssark pede-te ajuda contra os renegados | **Escolha**: **A)** cumprir a ordem (lutar contra a aldeia) **ou** **B)** defender a aldeia e provar à Guilda que os renegados são os culpados | **A**: a aldeia fica vazia, +pontos de Guilda, o Ssark aparece no andar 97 · **B**: a aldeia fica amiga, o Ssark pode ser companheiro, o Gorvan respeita-te (❤️) — conta para o final secreto |
| H_09 | A Que Não Morre | | Vencer a **Hidra do Pântano** (30) | **Dia da Subida**; abre a Arena (prata) |

### Capítulo 4 — Deserto
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_10 | Os Hieróglifos | A Professora Íris encontra escritos na pirâmide | Copiar os 6 painéis (andar 39) · levá-los ao Velho Fausto · cena: **a torre já teve vários Administradores, e todos foram Jogadores** | Página especial "Os Administradores" |
| H_11 | O Que Também Subiu | | Vencer o **Faraó Eterno** (40) | **Dia da Subida**; montadas no Rancho do Zed |

### Capítulo 5 — Gelo
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_12 | O Diário de Gorvan | No sino da Aldeia dos Caçadores está o diário da antiga equipa do Gorvan | Encontrar o diário (andar 46) · levá-lo ao Gorvan · cena: o Gorvan conta (pela primeira vez) o que viu no andar 74 | ❤️❤️ Gorvan |
| H_13 | O Meio do Caminho | | Vencer o **Dragão de Gelo** (50) | **Grande festa** do andar 50 |

### Capítulo 6 — Oceano
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_14 | Fantasmas do Navio | No Navio Fantasma há Jogadores antigos presos | Libertar os 5 fantasmas (andar 53) · ler o diário de bordo · **o Kai desaparece** (o último registo é dele) | Página especial |
| H_15 | O Último do Mar | | Vencer o **Leviatã** (60) | **Dia da Subida** (mais triste: o Kai continua desaparecido) |

### Capítulo 7 — Vulcão
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_16 | O Regresso do Kai | Encontras o Kai no Acampamento das Cinzas (61). Diz que **aceitou um acordo com o Sistema**: se chegar ao topo primeiro, vai para casa | Falar com o Kai · segui-lo até ao andar 65 (ele foge) | — |
| H_17 | 🔀 O Duelo | O Sistema obriga-vos a lutar na Cratera Interior | **Duelo** (ver `docs/BOSSES.md`). **Salvar** (6+ ❤️ e as respostas certas) **ou vencer** | **Salvar**: o Kai volta (companheiro, conta para o final secreto) · **Vencer**: o Kai desaparece até ao andar 100 |
| H_18 | O Coração do Vulcão | | Vencer o **Titã de Magma** (70) | **Dia da Subida** |

### Capítulo 8 — Reino Assombrado
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_19 | O Passado de Gorvan | O Gorvan decide voltar ao andar 74 contigo | Descer às Catacumbas com o Gorvan · vencer o Colosso de Ossos · encontrar a Sala da Equipa · cena de despedida | o Gorvan reconcilia-se com o passado |
| H_20 | O Que Tentou Parar a Torre | | Vencer o **Rei Sem Coroa** (80) · ouvir o Rei | **Dia da Subida**; o Gorvan volta a treinar |

### Capítulo 9 — Céu
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_21 | A Verdade do Serafim | | Vencer o **Serafim Caído** (90) · ouvir a verdade: **o Administrador está cansado e procura um sucessor; é por isso que traz Jogadores** | Cena · o Dia da Subida é silencioso |

### Capítulo 10 — Abismo
| ID | Nome | O que acontece | Passos | Recompensa |
|---|---|---|---|---|
| H_22 | O Último Posto | | Chegar ao andar 91 · reativar o posto (R10_01) | o posto passa a ser a tua base avançada |
| H_23 | 🔀 Os Perdidos | Na Cidade dos Perdidos vivem Jogadores que desistiram | Falar com a "Mãe Dois" · **convencer Perdidos** a voltar a subir (R10_07: 0 a 5) | quantos convenceres conta para o final |
| H_24 | O Diário de A. (opcional mas recomendada) | A Arquivista junta as páginas | Ter 90+ páginas de lore · falar com a Arquivista | revela o nome **Aren** antes do fim |
| H_25 | A Escada Final | | Subir o andar 99 · vencer o Guardião da Escada · **Ponto Sem Retorno** (última gravação) | — |
| H_26 | 🔀 O Administrador | | Ouvir a oferta (aceitar já = final "O novo Administrador") · ou lutar e vencer · **escolha final** | **Um dos 4 finais** (ver `docs/HISTORIA.md`) |

### Pós-jogo
| ID | Nome | Passos | Recompensa |
|---|---|---|---|
| H_27 | Os Andares do Eco | Usar a **Chave do Sistema** no Topo da Torre | Abrem os andares 101+ (infinitos) e os **Bosses Despertos** |

---

## 3. Guilda — missões fixas por rank

Estão sempre no quadro até as fazeres. Algumas são as mesmas missões das regiões (o ID da região está entre parênteses).

| Rank | ID | Nome | Objetivo | Recompensa |
|---|---|---|---|---|
| F | G_F_01 | Limpeza de Slimes | Matar 10 Slimes Verdes | 50 ouro · 10 pontos |
| F | G_F_02 | Ervas para a Igreja | 10 Erva Verde para a Irmã Célia | 2 Poções de Vida · 10 pontos |
| F | G_F_03 | Primeiro Mapa | Explorar 80% do andar 1 | Bússola simples · 10 pontos |
| E | G_E_01 | Lobos no Bosque | Matar 8 Lobos Cinzentos (andar 2) | 150 ouro · 20 pontos |
| E | G_E_02 | Caça ao Slime Rei (R1_11) | Vencer o Slime Rei | 500 ouro · Coroa de Gel · 20 pontos |
| E | G_E_03 | Luz para a Cidade | 20 Cogumelo Luminoso | 200 ouro · 20 pontos |
| D | G_D_01 | Goblins na Mina | Matar 15 Goblins Mineiros | 400 ouro · 40 pontos |
| D | G_D_02 | O Rei Goblin (R2_10) | Vencer o Rei Goblin Gruk | 900 ouro · 40 pontos |
| D | G_D_03 | Seda para a Elva | 15 Seda de Aranha | mochila +5 · 40 pontos |
| C | G_C_01 | Mandíbula (R3_11) | Vencer a Mãe-Crocodilo Mandíbula | 1 200 ouro · 80 pontos |
| C | G_C_02 | As Bruxas do Charco | Vencer 5 Bruxas do Pântano | 900 ouro · 80 pontos |
| C | G_C_03 | Repara os Passadiços (R3_01) | 20 Mangue | 300 ouro · 80 pontos |
| B | G_B_01 | O Colosso (R4_12) | Vencer o Verme Colosso | 2 500 ouro · 150 pontos |
| B | G_B_02 | O Gigante Gentil (R5_11) | Vencer ou acalmar o Mamute Ancião | 150 pontos |
| B | G_B_03 | Caravana em Perigo | Defender uma caravana no andar 31 (evento) | 2 000 ouro · 150 pontos |
| A | G_A_01 | Três Cabeças (R7_13) | Vencer o Tricéfalo | 4 000 ouro · 300 pontos |
| A | G_A_02 | A Condessa (R8_08) | Vencer a Condessa Sangria | 300 pontos |
| A | G_A_03 | Barba-Lodo (R6_13) | Vencer o Barba-Lodo | 300 pontos |
| S | G_S_01 | O Duelo de Sigrun (R9_11) | Vencer a Valquíria Sigrun | 600 pontos |
| S | G_S_02 | A Invasão (N_FREYA_3) | Defender Ascendia da grande invasão | 10 000 ouro · 600 pontos |
| S | G_S_03 | Todos os Nomes | Vencer 10 monstros com nome diferentes | título *Caçador de Nomes* · 600 pontos |
| SS | G_SS_01 | O Devorador Ancestral (R10_13) | Vencer o Devorador Ancestral | 1 200 pontos |
| SS | G_SS_02 | O Nome Raspado (R10_12) | Encontrar o Jogador Sem Número | 1 200 pontos |
| SS | G_SS_03 | 20 Monstros com Nome | Vencer os 20 monstros com nome | título *Lenda dos Nomes* · 1 200 pontos |
| SSS | G_SSS_01 | Os Bosses Despertos | (pós-jogo) Vencer os 20 Bosses Despertos | título *Lenda de Ascendia* |
| SSS | G_SSS_02 | O Andar 150 | (pós-jogo) Chegar ao andar 150 do Eco | Asas do Eco (cosmético) |
| SSS | G_SSS_03 | Tudo | 100% das coleções | título *O Completo* |

---

## 4. Guilda — missões geradas (quadro diário)

Todos os dias às 6:00 aparecem **3 missões novas** no quadro da Guilda, criadas a partir destes modelos com os
monstros, materiais e andares que já desbloqueaste. O rank da missão é igual ao teu ou um abaixo.

| Modelo | Exemplo | Recompensa (ouro) |
|---|---|---|
| **Caça** | "Matar 12 Escorpiões no andar 33" | 30 × nível do andar |
| **Recolha** | "Trazer 15 Seda de Aranha" | preço dos materiais × 1,5 |
| **Entrega** | "Levar um pacote ao Oásis de Zahra (andar 32) até às 18:00" | 25 × nível do andar |
| **Resgate** | "Um aventureiro perdeu-se no andar 27; encontra-o" (aparece um NPC num sítio ao acaso) | 40 × nível do andar |
| **Exploração** | "Explorar 90% do andar 44" | 35 × nível do andar |
| **Escolta** | "Acompanhar um mercador da Zona Segura até à escada do andar 12" | 40 × nível do andar |
| **Investigação** | "Encontrar a origem dos uivos no andar 41" (pistas no andar levam a um monstro Elite) | 45 × nível do andar |
| **Defesa** | "Defender o Posto Mineiro de 3 ondas de goblins" | 50 × nível do andar |

Pontos de Guilda: ver a tabela da secção 16 de `docs/SISTEMAS.md`. Há também **missões diárias da Guilda**
(fazer 3 missões do quadro num dia dá um baú de prata).

---

## 5. Festivais

| ID | Festival | Quando | Missão | Recompensa |
|---|---|---|---|---|
| F_01 | **Festa das Flores** | Primavera, dia 13 | Trazer a flor mais bonita (qualidade Excelente) para o concurso; dançar com um NPC (o NPC aceita com 4+ ❤️) | 1.º lugar: Coroa de Flores · +100 amizade com o par de dança |
| F_02 | **Festival da Pesca** | Verão, dia 20 | Pescar o maior peixe em 10 minutos no rio de Ascendia | 1.º lugar: Isco Lendário ×3 · título *Rei da Pesca* |
| F_03 | **Noite dos Espíritos** | Outono, dia 26 | Pôr uma lanterna de abóbora à porta · recolher 10 doces dos fantasmas amigáveis · encontrar o fantasma do Pregoeiro (piada) | Máscara de Abóbora · doces |
| F_04 | **Festival da Estrela** | Inverno, dia 25 | **Amigo secreto**: dar um presente ao NPC que te calhar (ele diz-te o que gosta numa pista) · ver o fogo de artifício | presente do teu amigo secreto · +amizade com todos |
| F_05 | **Dia da Subida** | sempre que vences um boss de região | Falar com toda a gente na Praça · ouvir o discurso do Governador · a nova canção do Lucien | comida grátis · +20 amizade com todos |
| F_06 | **Concurso da Casa Mais Bonita** | Outono, dia 15 (depois da casa) | Decorar a casa; os juízes visitam | 1.º lugar: Móvel Dourado · título *Decorador* |
| F_07 | **Noite das Lanternas** | dia 28 de cada estação, 20:00 | Tradição pequena (sem loja nem jogos): pôr no rio uma lanterna de papel por cada aventureiro que não voltou. Abre com a cena de 4 ❤️ da Lyra | +10 amizade com cada NPC presente |

Há também festivais **nas povoações da torre** (Festa na Aldeia Sssar, Festival do Oásis, Festa do Solstício
em Pinhal-do-Norte, Festival da Forja no Bastião, Festival das Lanternas Celestes em Aerópolis): ver as regiões.
