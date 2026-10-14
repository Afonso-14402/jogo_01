# Som e música

## 1. Ferramentas e formatos

| Coisa | Ferramenta | Formato |
|---|---|---|
| Música | **BeepBox** (no browser) ou **LMMS** | `.ogg` (em ciclo, com ponto de repetição) |
| Efeitos sonoros | **jsfxr** / **ChipTone** | `.wav` curtos |
| Editar e cortar | **Audacity** | — |
| Vozes dos NPCs | bips gerados (um tom e velocidade por NPC) | gerado no jogo |

- Estilo: **chiptune com instrumentos "reais" por cima** (flauta, cordas, piano) — retro mas emotivo, combina com o HD-2D.
- Volume: músicas mais baixas do que os efeitos; tudo normalizado.
- Pastas: `musica/` e `sons/` (ver `docs/PROGRAMACAO.md`).

### Música dinâmica
Cada região tem uma faixa **de exploração** e uma camada **de combate** que entra suavemente quando há inimigos
a perseguir-te e sai 5 s depois de acabar a luta. À noite, as faixas tocam uma versão mais calma.

---

## 2. Músicas (lista)

### Menus e cidade
| Faixa | Onde | Sensação |
|---|---|---|
| `tema_principal` | menu inicial e créditos | épico, saudade |
| `prologo` | andar 1, prólogo | misterioso, a acordar |
| `ascendia_dia` / `ascendia_noite` | cidade | acolhedora, viva / calma |
| `taberna` | Taberna | alegre, alaúde |
| `guilda` | Guilda | trabalho, aventura |
| `casa` | a tua casa | calma; versão final "Casa" (R10_14) |
| `festival` (4 variações) | festivais | festa de cada estação |
| `dia_da_subida` | depois dos bosses | triunfo |
| `cidade_errante` (`vagar`) | Vagar | acordeão e tambores |

### Regiões (exploração + combate + noite)
| Região | Faixas |
|---|---|
| 1 Floresta | `floresta_dia`, `floresta_noite`, `floresta_perigo` |
| 2 Cavernas | `minas_eco`, `cristal_canto`, `forja_ana` |
| 3 Pântano | `pantano_lodo`, `selva_tambores`, `aldeia_sssar` |
| 4 Deserto | `dunas`, `bazar_zahra`, `piramide` |
| 5 Gelo | `tundra_silencio`, `pinhal_aldeia`, `aurora` |
| 6 Oceano | `praia`, `porto_piratas`, `debaixo_de_agua`, `abismo` |
| 7 Vulcão | `cinzas`, `rios_de_lava`, `bastiao_brasa` |
| 8 Reino | `muralhas`, `cidade_fantasma` (caixa de música), `catacumbas`, `catedral` |
| 9 Céu | `mar_de_nuvens`, `aeropolis`, `pontes_de_luz` (ritmo das pontes), `tempestade_eterna` |
| 10 Abismo | `vazio`, `mar_de_estrelas`, `ecos` (mistura de todas as regiões), `cidade_dos_perdidos` |

### Bosses
`guardiao` (genérica para os guardiões, 3 variações) · `javali_rei` · `ent_anciao` · `aranha_mae` · `golem_cristal` ·
`serpente_lodo` · `hidra` · `escorpiao_imperador` · `farao_eterno` · `yeti` · `dragao_gelo` · `capitao_esqueleto` ·
`leviata` · `ferreiro_infernal` · `duelo_kai` · `tita_magma` · `lich` · `rei_sem_coroa` · `grifo_real` · `serafim_caido` ·
`guardiao_do_tempo` · `administrador` (4 partes, uma por fase; a última quase em silêncio)

### Momentos
`tristeza` (cenas tristes) · `revelacao` (verdades da história) · `amizade` (cenas de coração) · `finais` (uma por final) ·
`morte` (curta) · `vitoria` (fanfarra curta) · `subir_de_nivel` (jingle)

**Total**: cerca de **75 faixas** (muitas curtas).

---

## 3. Efeitos sonoros

| Grupo | Sons |
|---|---|
| **Herói** | passos (relva, pedra, areia, neve, água, madeira, metal, nuvem), esquiva, saltar, cair, levar dano, morrer, subir de nível, beber poção, comer, planar, nadar |
| **Armas** (por tipo) | espada (corte, corte pesado), espada grande, adaga, katana (Iai), machado, martelo (impacto), lança, foice, arco (esticar, disparar), besta (recarregar, disparar), cajado (feitiço por elemento), manoplas (socos) |
| **Impactos** | acerto normal, crítico, bloqueado, imune, inimigo morre, hitstop |
| **Elementos** | fogo, gelo, raio, veneno, luz, sombra (cada um: lançar e acertar) |
| **Estados** | envenenado, a arder, congelar/descongelar, atordoado, amaldiçoado |
| **Monstros** | 1–3 sons por monstro (80): grito ao ver-te, ataque, morte |
| **Bosses** | rugidos, mudança de fase, ataques especiais |
| **Mundo** | baú a abrir (madeira, prata, ouro), mímico, porta, alavanca, placa de pressão, cristal de teletransporte, recolher (minério, madeira, erva), cascata, lava, vento, sinos, órgão |
| **Interface** | abrir janela do Sistema, fechar, mover cursor, aceitar, recusar, sem dinheiro, comprar, vender, equipar, melhoria com sucesso, melhoria falhada, notificação, missão concluída, monstro com nome |
| **Pesca** | lançar, boia, mordida, puxar, apanhado, fugiu |
| **Quinta** | plantar, regar, colher, animais (galinha, vaca, cabra, ovelha) |
| **Ambiente** (ciclos) | floresta (pássaros, vento), gruta (pingos, eco), pântano (rãs, insetos), deserto (vento, areia), gelo (vento, gelo a ranger), mar (ondas, gaivotas), vulcão (borbulhar, ronco), reino (corvos, sinos), céu (vento alto), vazio (zumbido grave), cidade (pessoas, mercado), chuva, trovoada |

**Total**: cerca de **300 sons** (muitos são variações do mesmo som).

---

## 4. Vozes dos NPCs

Não há vozes gravadas: cada NPC tem um **"bip"** próprio que soa a cada letra do diálogo.

| NPC | Bip |
|---|---|
| Brom | grave e curto |
| Lyra | agudo e rápido |
| Gorvan | muito grave e lento |
| Selene | médio, com eco "mágico" |
| Kai | médio e decidido |
| Fantasmas | bips com eco e tremido |
| Fungoides | bips lentíssimos e suaves |
| O Sistema | bip eletrónico "limpo" |
| O Administrador | o bip do Sistema que vai ficando humano |
