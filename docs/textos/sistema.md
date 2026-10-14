# Mensagens do Sistema

Lista das mensagens da janela azul. `{x}` são valores que o jogo preenche. As mensagens da história (que mudam ao longo
do jogo) estão no guião (`docs/guiao/`). O estilo das janelas está em `docs/INTERFACE.md`.

## Itens e ouro
| ID | Mensagem |
|---|---|
| `sis_obteve` | `[Sistema] Obtiveste: {item} ×{qtd}.` |
| `sis_ouro` | `[Sistema] +{ouro} ouro.` |
| `sis_mochila_cheia` | `[Sistema] Mochila cheia. Deixa alguma coisa ou volta à cidade.` |
| `sis_peso` | `[Sistema] Estás a carregar demasiado peso. Andas mais devagar e não podes esquivar.` |
| `sis_raro` | `[Sistema] Item {raridade}! {item}.` (com som especial para Épico ou melhor) |
| `sis_roubado` | `[Sistema] Roubaram-te: {item}! Apanha o ladrão!` |
| `sis_sem_ouro` | `[Sistema] Ouro insuficiente.` |
| `sis_sem_materiais` | `[Sistema] Faltam materiais: {lista}.` |

## Combate
| ID | Mensagem |
|---|---|
| `sis_hostil` | `[Sistema] Hostil detetado: {monstro}. Nível {nivel}.` |
| `sis_nivel_alto` | `[Sistema] Aviso: o nível do inimigo é muito superior ao teu.` |
| `sis_elite` | `[Sistema] Elite: {monstro}.` |
| `sis_nome` | `[Sistema] Um monstro com nome apareceu neste andar: {monstro}.` |
| `sis_guardiao` | `[Sistema] Guardião do andar {andar}: {guardiao}.` |
| `sis_boss` | `[Sistema] Boss: {boss}, {titulo}.` |
| `sis_fase` | `[Sistema] {boss} mudou de fase.` |
| `sis_furia` | `[Sistema] {boss} está furioso!` |
| `sis_vitoria` | `[Sistema] {boss} derrotado.` |
| `sis_estado` | `[Sistema] Estás {estado}.` |
| `sis_imune` | `[Sistema] Imune.` (número cinzento no alvo) |
| `sis_fraco` | `[Sistema] Golpe eficaz!` (só nas primeiras vezes) |
| `sis_morte` | `[Sistema] Os teus pontos de vida chegaram a zero.` |
| `sis_perdeu` | `[Sistema] Perdeste: {lista}.` |
| `sis_segunda_vida` | `[Sistema] Segunda Vida ativada.` |

## Progresso
| ID | Mensagem |
|---|---|
| `sis_xp` | `[Sistema] +{xp} XP.` |
| `sis_nivel` | `[Sistema] Subiste para o nível {nivel}!` |
| `sis_pontos` | `[Sistema] Tens {n} pontos de atributo por distribuir.` |
| `sis_skill_sobe` | `[Sistema] {skill} subiu para Nv {nivel}.` |
| `sis_skill_nova` | `[Sistema] Novo ataque: {ataque}.` |
| `sis_classe` | `[Sistema] Classe obtida: {classe}.` |
| `sis_titulo` | `[Sistema] Título obtido: {titulo}.` |
| `sis_conquista` | `[Sistema] Conquista: {conquista}.` |
| `sis_rank` | `[Sistema] Rank de aventureiro: {rank}.` |
| `sis_andar` | `[Sistema] Andar {andar} desbloqueado.` |
| `sis_regiao` | `[Sistema] Região {n} concluída.` |
| `sis_capitulo` | `[Sistema] Capítulo {n}: {nome}.` |
| `sis_explorado` | `[Sistema] Andar {andar} explorado a 100%!` |
| `sis_desafio` | `[Sistema] Desafio cumprido: {desafio}.` |
| `sis_segredo` | `[Sistema] Segredo descoberto! ({n}/{total})` |
| `sis_lore` | `[Sistema] Página do diário encontrada ({n}/100).` |
| `sis_receita` | `[Sistema] Receita aprendida: {receita}.` |
| `sis_bestiario` | `[Sistema] Nova entrada no Bestiário: {monstro}.` |

## Missões e amizade
| ID | Mensagem |
|---|---|
| `sis_missao_nova` | `[Sistema] Missão nova: {missao}.` |
| `sis_missao_passo` | `[Sistema] {missao}: {passo} ({n}/{total}).` |
| `sis_missao_feita` | `[Sistema] Missão concluída: {missao}.` |
| `sis_missao_falhou` | `[Sistema] Missão falhada: {missao}.` |
| `sis_coracao` | `[Sistema] ❤️ {npc} gosta mais de ti.` |
| `sis_coracao_menos` | `[Sistema] 💔 {npc} não gostou.` |
| `sis_aniversario` | `[Sistema] Hoje é o aniversário de {npc}!` |
| `sis_carta` | `[Sistema] Tens uma carta nova na caixa do correio.` |
| `sis_companheiro` | `[Sistema] {npc} juntou-se à equipa.` |
| `sis_companheiro_caiu` | `[Sistema] {npc} caiu. Levanta-se em 30 s.` |

## Mundo
| ID | Mensagem |
|---|---|
| `sis_zona` | `[Sistema] Nova zona descoberta: {zona}.` |
| `sis_zona_segura` | `[Sistema] Zona Segura.` |
| `sis_guardado` | `[Sistema] Progresso guardado.` |
| `sis_bom_dia` | `[Sistema] Bom dia. Dia {dia} de {estacao}.` |
| `sis_cansado` | `[Sistema] Estás cansado. Vai dormir.` |
| `sis_clima` | `[Sistema] O tempo mudou: {clima}.` |
| `sis_evento` | `[Sistema] Evento: {evento}.` |
| `sis_ferramenta` | `[Sistema] É preciso uma {ferramenta} de {material} ou melhor.` |
| `sis_fechado` | `[Sistema] Está trancado.` |
| `sis_mercador` | `[Sistema] O Mercador Errante está neste andar.` |
| `sis_vagar` | `[Sistema] A Cidade Errante apareceu no andar {andar}.` |
| `sis_temperatura` | `[Sistema] Estás a congelar!` / `[Sistema] Estás a ferver!` |
| `sis_ar` | `[Sistema] Ar a acabar!` |

## Falhas (região 10)
Mensagens normais com erros de propósito: letras trocadas (`[Sisetma]`), números errados, texto riscado,
janelas a abrir duas vezes, e às vezes mensagens que não fazem sentido: `[Sistema] Lembras-te da cor da tua casa?`
