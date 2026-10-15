# Eventos

Os **eventos** são coisas que acontecem de vez em quando, sem missão: na cidade (este ficheiro) e na torre (cada região
tem os seus, na secção 11 de `docs/regioes/rNN_*.md`). Os festivais têm data fixa e estão em `docs/ATIVIDADES.md`.

---

## 1. Como funcionam

| Regra | Valor |
|---|---|
| Sorteio | todos os dias às **6:00**, o jogo sorteia **um evento da cidade** (ou nenhum) e os eventos de cada região |
| Probabilidade | cada evento tem a sua (tabela abaixo); nunca há dois eventos da cidade no mesmo dia |
| Anúncio | o **pregão** da Praça (sino + `[Sistema] Evento: {nome}.`) e uma fala da **Lyra** ou da **Freya** ao entrar na Guilda |
| Dias proibidos | nunca há eventos da cidade nos dias de festival nem no Dia da Subida |
| Primeira vez | cada evento tem uma **primeira vez** com uma fala especial e uma recompensa a mais (marcada com ★) |

---

## 2. Invasões

Monstros que **fogem da torre pelo Cristal Mestre** e entram em Ascendia. Ninguém sabe porquê. O Doutor (andar 97)
diz que é a torre "a espreguiçar-se". Depois do final 3 já não há invasões (não há torre); no final 2, o herói pode
desligá-las nas regras.

### 2.1 Os três tamanhos

| Invasão | Quando | Duração | O que é |
|---|---|---|---|
| **Fuga** (pequena) | 10% por dia, depois do andar 5 | o dia todo | 5 monstros espalhados pela cidade (como a N_FREYA_1). Monstros da região mais alta desbloqueada −10 níveis. Se ninguém os vencer até às 20:00, a Guarda trata deles (sem recompensa) |
| **Invasão** (média) | 3% por dia, depois do andar 25 (e da N_FREYA_3) · 100% numa noite de lua cheia por estação | 22:00–2:00 | 2 vagas na Praça + um **chefe da invasão** na muralha |
| **Grande Invasão** | 1 vez por **ano** (Inverno, dia 20), depois do andar 50 | 22:00–5:00 | 3 vagas, a escolha de que bairro proteger, 2 chefes ao mesmo tempo; a cidade toda ajuda |

### 2.2 O chefe da invasão

É sempre um **monstro com nome** da região mais alta que já desbloqueaste (um dos dois, ao acaso), com −5 níveis.
Vencê-lo aqui **não conta** para a caça dele na torre (é uma "cópia" que fugiu), mas dá os drops normais.

| Região mais alta | Chefes possíveis |
|---|---|
| 1 | Slime Rei · Lobo Cicatriz |
| 2 | Rei Goblin Gruk · Toupeira Dourada |
| 3 | Mãe-Crocodilo Mandíbula *(no rio de Ascendia)* · Rei Macaco Bobo *(nos telhados)* |
| 4 | Sultão Bandido Kasim · Verme Colosso *(debaixo da Praça: a Praça treme)* |
| 5 | Presa-Branca · Mamute Ancião Tundra *(com `mamute_acalmado`, chega, olha para ti e vai-se embora sem lutar; com `mamute_morto`, é sempre a Presa-Branca)* |
| 6 | Caranguejo Rei Pinça-de-Ouro · Barba-Lodo *(chega pelo rio num barco a meio afundar)* |
| 7 | Tricéfalo · Golem Forjado Nº 7 |
| 8 | Condessa Sangria *(só de noite: é sempre de noite numa invasão)* · O Jardineiro *(corta as sebes da Igreja)* |
| 9 | Valquíria Sigrun *(não ataca: pede um duelo na Arena; se fizeste R9_11, vem só visitar a Freya)* · Tempestade Viva |
| 10 | Devorador Ancestral *(as luzes da cidade apagam-se uma a uma)* · O Jogador Sem Número *(não luta: senta-se na Praça e vai-se embora; se `ouviu_sem_numero`, deixa uma flor à porta da Dona Marta)* |

### 2.3 Quem ajuda

Na **Invasão** e na **Grande Invasão**, os NPCs de Ascendia com **6+ ❤️** aparecem a ajudar (cada um faz 1 ataque a
cada 20 s, como na fase 3 do Administrador):

| NPC | Onde aparece | O que faz | Fala ao chegar |
|---|---|---|---|
| Freya | sempre (é ela quem manda) | lança em linha | "Às portas! Tu, comigo!" |
| Gorvan | Praça | machado giratório | "Pelos cinco. E pela cidade." |
| Brom | à porta da forja | martelo que atordoa | "Ninguém toca na minha forja!" |
| Célia | Igreja | cura todos à volta 15% | "A Luz está connosco. E eu também." |
| Rook | telhados | facas de cima | "Não sou herói. Estou só a passar." |
| Kai *(`kai_salvo`)* | onde estiveres | Corte em Cruz | "Chegaste tarde! Já ia no terceiro!" |
| Mia *(10 ❤️)* | Praça | Chuva de Flechas Pequena | "Eu também sou da Guilda!" |
| Zed | Quintas | solta os animais do rancho contra os monstros | "…" (o Pimpão guincha por ele) |
| Selene | à porta da alquimia | atira poções que explodem | "Eram para vender. Agora são para isto." |
| Gizmo | Bairro dos Artesãos | uma torre de canhão que dispara sozinha 30 s | "Teste em situação real! Que sorte!" |
| Lucien | Taberna | canção que dá +10% ATQ a todos | "Uma balada de batalha! Esta escrevi agora!" |
| Dona Marta | Estalagem | atira panelas (e dá-te um guisado no fim) | "Na minha estalagem ninguém entra sem limpar os pés!" |
| Os outros (Lyra, Tobias, Fausto, Pip, Hana, Oriel, Elva, Aldric) | escondidos | não lutam: dão itens (poções, isco, sementes, cartas de sorte, um remendo na capa, um discurso) | (uma fala cada, nos ficheiros deles, condição `evento(invasao)`) |

### 2.4 A escolha do bairro (só na Grande Invasão)

A meio da noite, a Freya pergunta:
- **Capitã Freya** *(zangada)*: "Duas vagas ao mesmo tempo. Uma no Mercado, outra no Bairro Baixo. Não chego às duas. Escolhe."

▶ **"O Mercado."** · ▶ **"O Bairro Baixo."**

- O bairro que **não** escolhes fica com dano: as lojas desse bairro fecham **3 dias** para obras (o Tobias e o Bairro
  Baixo têm falas de queixa). Se tiveres a melhoria **Muralha Reforçada**, o dano é só de 1 dia.
- Se o **Rook** tiver 8+ ❤️ e escolheres o Mercado, ele defende o Bairro Baixo sozinho: não há dano. **Rook** *(no dia
  seguinte)*: "Não foi nada. Foram umas facas. Muitas facas."

### 2.5 Recompensas

| Invasão | Recompensa |
|---|---|
| Fuga | 50 ouro × região por monstro · 10 pontos de Guilda |
| Invasão | 1 500 ouro × região · drops do chefe · 50 pontos de Guilda · +20 ❤️ com cada NPC que ajudou · ★ título *Guarda Honorári{o/a}* |
| Grande Invasão | 5 000 ouro × região · drops dos 2 chefes · 150 pontos de Guilda · +50 ❤️ com cada NPC que ajudou · um **móvel único** por ano (estandarte da Guarda, sino da muralha, escudo da Freya, mapa da cidade da Grande Invasão…) · ★ título *Muralha de Ascendia* |

A missão **G_S_02 A Invasão** (rank S) é vencer uma Grande Invasão sem nenhum edifício com dano.

---

## 3. Outros eventos da cidade

| Evento | Probabilidade | Desde | O que acontece | Fala de anúncio |
|---|---|---|---|---|
| **Mercador Errante** | quando a Cidade Errante (Vagar) está no andar 1 (ver `docs/CIDADES.md`) | andar 10 | o Ambrósio monta banca na Praça com 3 itens raros | **Lyra**: "O Mercador Errante está na Praça! Leva dinheiro. Leva muito dinheiro." |
| **Chuva de Cristais** | 4% | andar 15 | caem cristalinhos do céu (do Cristal Mestre). Apanhá-los dá Fragmentos de Cristal (melhorias +1 a +5) | **Lyra**: "Está a chover cristal! Abre a boca! Não, não abras a boca." |
| **Monstro Dourado** | 3% | andar 10 | um monstro da região 1 todo dourado foge pela cidade (como o Coelho-Dourado). Não ataca: foge. Apanhá-lo dá 1 000 ouro × região | **Freya**: "Um monstro de ouro a correr pelo Mercado. Não é piada. Quem me dera que fosse." |
| **Caravana** | 5% (Primavera e Verão) | sempre | uma caravana de fora (como a do Lucien) traz 6 itens de outras regiões a preço normal e um contador de histórias | **Lucien**: "Uma caravana! Gente nova! Histórias novas! Rimas novas!" |
| **Visita dos Povos** | 5% (um povo por evento, de uma região já libertada) | depois de cada região | gente de um povo da torre visita Ascendia: elfos de Folhalta, fungoides, Ssar (só com `sssar_defendida`), Torrenses, Alados… Montam bancas com os itens deles e têm falas na Praça | **Aldric**: "Temos… visitas. De cima. Sejam bem-vindos. Não há discurso. Esqueci-me de escrever." |
| **Noite Sem Estrelas** | 2% | andar 81 | o céu de Ascendia fica preto. A Oriel não sai da tenda. À meia-noite, uma estrela cai na quinta (Estrela Cadente) | **Oriel**: "Hoje não leio cartas. As estrelas fecharam os olhos. Volta amanhã." |
| **Nevoeiro do Rio** | 4% (Outono) | andar 20 | nevoeiro no rio: o Pip diz que os peixes raros sobem à superfície (+50% de peixes raros no rio de Ascendia) | **Pip**: "Nevoeiro! Os peixes gostam. Eu gosto. Tu gostas? Devias." |
| **Dia sem Sistema** | 1% | andar 91 | a janela azul não aparece durante todo o dia em Ascendia (sem números, sem mensagens). Os NPCs reparam | **Fausto**: "Hoje a janela não te segue? Que estranho. Que bom. Que estranho." |

---

## 4. Textos do Sistema dos eventos

| ID | Mensagem |
|---|---|
| `evt_inicio` | `[Sistema] Evento: {nome}.` |
| `evt_fuga` | `[Sistema] Fuga! {n} monstros na cidade.` |
| `evt_invasao` | `[Sistema] Invasão! Defende a Praça.` |
| `evt_vaga` | `[Sistema] Vaga {n}/{total}.` |
| `evt_chefe` | `[Sistema] Chefe da invasão: {nome}.` |
| `evt_grande` | `[Sistema] GRANDE INVASÃO. Toda a cidade está em perigo.` |
| `evt_fim_bom` | `[Sistema] A cidade está a salvo.` |
| `evt_fim_dano` | `[Sistema] A cidade está a salvo. {bairro} ficou com estragos.` |
| `evt_fim` | `[Sistema] Evento terminado.` |
