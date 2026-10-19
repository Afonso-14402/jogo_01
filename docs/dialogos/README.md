# Diálogos

As conversas **normais** das pessoas do jogo, fora das cenas da história (essas estão em `docs/guiao/`).
O perfil de cada NPC (aspeto, história, presentes, missões) está em `docs/NPCS.md`; aqui está **o que eles dizem**.

| Ficheiro | Quem |
|---|---|
| [`lyra.md`](lyra.md) | Lyra, recepcionista da Guilda |
| [`gorvan.md`](gorvan.md) | Mestre Gorvan |
| [`brom.md`](brom.md) | Brom, ferreiro |
| [`selene.md`](selene.md) | Selene, alquimista |
| [`tobias.md`](tobias.md) | Tobias, mercador |
| [`marta.md`](marta.md) | Dona Marta, Estalagem |
| [`kai.md`](kai.md) | Kai, Jogador nº 9 999 |
| [`mia.md`](mia.md) | Mia, menina das flores |
| [`pip.md`](pip.md) | Pip, pescador |
| `celia.md` … `aldric.md` | os outros 11 NPCs de Ascendia |
| `povoacoes_r01.md` … `povoacoes_r10.md` | NPCs das povoações e missões das regiões, passo a passo |
| `aldeoes.md` | aldeões sem nome de Ascendia (frases soltas) |

---

## 1. Como cada ficheiro está organizado

Todos os ficheiros de NPC têm as mesmas secções, pela mesma ordem:

| # | Secção | O que tem |
|---|---|---|
| 1 | **Ficha de voz** | como fala, a "voz" (bips), palavras que repete, o que nunca diz |
| 2 | **Primeira conversa** | o que diz quando falas com ele pela 1.ª vez (fora da cena do prólogo) |
| 3 | **Falas do dia a dia** | tabela grande com condição: estação, tempo, hora, corações, progresso… |
| 4 | **Perguntar sobre…** | a torre · o andar atual (1 por região) · rumores · a vida dele (abre com corações) |
| 5 | **Presentes** | reação a adora / gosta / neutro / não gosta / detesta, e falas de itens especiais |
| 6 | **Aniversário e festivais** | o que diz nesses dias |
| 7 | **Depois dos bosses** | 1 fala por boss (os 20 e o duelo com o Kai), dita na 1.ª conversa depois da vitória |
| 8 | **Cenas de coração** | as 5 cenas (2, 4, 6, 8 e 10 corações) escritas como no guião |
| 9 | **Missões** | as missões do NPC: pedir, durante, entregar |
| 10 | **Estados e especiais** | vida baixa, amaldiçoado, cansado, molhado, arma nova, animal, companheiros… |

---

## 2. Que fala aparece? (prioridade)

Quando carregas em **Conversar**, o jogo escolhe **uma** conversa por esta ordem (a primeira que servir ganha):

1. **Cena de coração** pendente (se estás no sítio e à hora certa, a cena começa sozinha, nem precisas de falar).
2. **Aniversário** do NPC (se ainda não lhe deste presente hoje).
3. **Festival** a decorrer.
4. **Depois de um boss** (só a 1.ª conversa depois da vitória; se venceste 2 bosses sem falar, diz só a do mais recente).
5. **Missão** do NPC ativa ou pronta a entregar.
6. **Estado** do herói (vida abaixo de 30%, amaldiçoado, cansado, molhado…), 1 vez por dia.
7. **Falas do dia a dia**: de todas as que cumprem a condição, escolhe uma ao acaso, **sem repetir** as últimas 5.
   As falas com condição mais **específica** (ex.: "chuva + noite") têm peso ×3.
8. Se já falaste hoje, diz uma das **falas curtas** (secção 3, linhas `*_curta_*`) e não dá amizade.

A 1.ª conversa do dia dá **+20 de amizade** (ver `docs/SISTEMAS.md`, secção 15).

---

## 3. Como se escrevem as condições

As condições são as do código (ver `docs/PROGRAMACAO.md`, secção 5.5). Nas tabelas usamos estas formas:

| Condição | Exemplo | Quer dizer |
|---|---|---|
| `—` | | sempre |
| `estacao` | `estacao == verao` | primavera, verao, outono, inverno |
| `dia_semana` | `dia_semana == domingo` | segunda … domingo |
| `clima` | `clima == chuva` | sol, chuva, trovoada, nevoeiro, neve |
| `hora` | `hora entre 6 e 10` | horas do jogo (0–23) |
| `coracoes` | `coracoes(lyra) >= 4` | corações com este NPC |
| `andar_maximo` | `andar_maximo >= 11` | andar mais alto a que chegaste |
| `boss_derrotado` | `boss_derrotado(ent_anciao)` | boss já vencido |
| `missao` | `missao(N_LYRA_1) == concluida` | estados: `inativa`, `ativa`, `pronta`, `concluida` |
| `flag` | `flag(kai_promessa_1)` | marca da história |
| `origem` | `origem == jogador` | atrasado, jogador, ajudante, dormir (ver o prólogo, cena P1) |
| `skill_unica` | `skill_unica == lingua_universal` | a Skill Única do herói |
| `classe` | `classe == mago` | classe atual |
| `arma_tipo` | `arma_tipo == martelo` | tipo da arma equipada (ver `docs/ARMAS.md`) |
| `vida_pct` | `vida_pct < 30` | vida em percentagem |
| `estado` | `estado(amaldicoado)` | estado ativo no herói (ver `docs/SISTEMAS.md`, secção 5) |
| `companheiro` | `companheiro(mia)` | este companheiro está na equipa |
| `animal` | `animal != nenhum` | animal de estimação equipado |
| `rank` | `rank >= C` | rank de aventureiro |
| `nivel` | `nivel >= 10` | nível do herói |
| `capitulo` | `capitulo == 1` | capítulo da história (1 a 10) |

Juntam-se com `&&` (e) e `||` (ou). Ex.: `clima == chuva && hora entre 20 e 23`.

---

## 4. Marcas usadas nos textos

| Marca | Significa |
|---|---|
| *(feliz)* | emoção do retrato: normal, feliz, zangado, triste. Extras que usam esses retratos com um efeito: *surpresa* (feliz + "!"), *nervoso/nervosa* (triste + gota de suor), *séria/sério* (normal com os olhos mais fechados) |
| ▶ | escolha do jogador |
| ⚙ | efeito no jogo (amizade, item, missão, flag) |
| 🎬 / 🎥 | o que os personagens fazem / o que a câmara faz (só nas cenas) |
| `{nome}` | nome do herói |
| `{item}`, `{andar}`, `{peixe}` | valores que o jogo preenche |
| … | pausa (a caixa espera meio segundo) |
| **negrito** | a palavra treme ou aparece maior (ênfase) |

**IDs das falas:** `<npc>_<secção>_<nº>` — ex.: `lyra_dia_07`, `lyra_presente_adora_2`, `lyra_boss_ent_anciao`.
Cada ID vira uma chave de tradução em `traducoes/dialogos.csv`.

---

## 5. Regras de escrita (para todos os NPCs)

- **Português de Portugal**, frases curtas (uma caixa de diálogo tem no máximo **3 linhas de ~40 letras**).
  Uma fala maior parte-se em várias caixas.
- Cada NPC tem **uma voz** (ver a ficha de voz). Lê a fala em voz alta: se podia ser dita por outro NPC, reescreve.
- **Ninguém em Ascendia sabe o segredo** da torre (ver `docs/HISTORIA.md`, secção 1). Podem ter teorias, nunca a verdade.
- O herói **não fala** fora das escolhas ▶. As escolhas são curtas (máx. ~35 letras) e há sempre uma "simpática".
- Não há namoros: as relações são de amizade, família, mestre e aprendiz.
- O texto tem de funcionar com **qualquer nome** do herói. Quando uma palavra muda com o género do herói, escreve-se
  `{o/a}`, `{ele/ela}`, `{ão/ã}`, `{/a}` (nada ou "a": "Defensor{/a}") — o jogo escolhe pelo **Tratamento** escolhido na criação de personagem
  (ver `docs/INTERFACE.md`, secção 6). Ex.: "Estás magr{o/a}!". Quando der, prefere frases sem género
  ("Tens cara de sono").
