# Bíblia do jogo — índice

Tudo o que é preciso para fazer o jogo está escrito nestes documentos. Quando for a hora de programar ou de desenhar,
é **seguir o que aqui está**. Se alguma coisa mudar, muda-se primeiro no documento.

## Ordem de leitura

1. [`../OBJETIVO.md`](../OBJETIVO.md) — **o plano**: a ideia, as decisões, as ferramentas e as etapas.
2. [`HISTORIA.md`](HISTORIA.md) — a história, os segredos e os 4 finais.
3. [`TORRE.md`](TORRE.md) — os 100 andares num relance.
4. [`regioes/`](regioes/) — as 10 regiões, andar a andar.
5. Depois, o que precisares.

## Todos os documentos

| Documento | Para quê | Quem usa mais |
|---|---|---|
| [`../OBJETIVO.md`](../OBJETIVO.md) | plano oficial, decisões, etapas | os dois |
| [`HISTORIA.md`](HISTORIA.md) | história completa, escolhas, finais, epílogos | os dois |
| [`TORRE.md`](TORRE.md) | tabela dos 100 andares e estrutura de um andar | os dois |
| [`regioes/r01_floresta.md`](regioes/r01_floresta.md) … [`r10_abismo.md`](regioes/r10_abismo.md) | cada região: identidade, materiais, 8 monstros, monstros com nome, 10 andares, guardiões, povoações, missões, masmorra, peixes, plantas, eventos, **lista de arte** | os dois |
| [`BOSSES.md`](BOSSES.md) | 20 bosses + o duelo do Kai: fases, ataques, recompensas | os dois |
| [`CIDADES.md`](CIDADES.md) | Ascendia, casa, quinta, 26 povoações, Cidade Errante | os dois |
| [`NPCS.md`](NPCS.md) | diálogo, amizade, 20 NPCs com perfil completo, companheiros | os dois |
| [`MISSOES.md`](MISSOES.md) | história principal, Guilda, festivais | código |
| [`ARMAS.md`](ARMAS.md) | ~258 armas com números | código e arte |
| [`EQUIPAMENTO.md`](EQUIPAMENTO.md) | armaduras, acessórios, gemas | código e arte |
| [`ITENS.md`](ITENS.md) | poções, comida, materiais, plantas, móveis, presentes | código e arte |
| [`PROGRESSAO.md`](PROGRESSAO.md) | status, classes, skills, rank | código |
| [`ATIVIDADES.md`](ATIVIDADES.md) | minijogos, coleções, títulos, conquistas, pós-jogo | código |
| [`SISTEMAS.md`](SISTEMAS.md) | **todas as regras e fórmulas** | código |
| [`PROGRAMACAO.md`](PROGRAMACAO.md) | **guia técnico do Godot** e ordem de implementação | código |
| [`INTERFACE.md`](INTERFACE.md) | ecrãs, menus, HUD, opções | código e arte |
| [`AUDIO.md`](AUDIO.md) | músicas, sons, vozes | som |
| [`ARTE.md`](ARTE.md) | **regras da arte** (padrão, tamanhos, animações, Blender, pastas) e **lista total** | arte |
| [`LOJAS.md`](LOJAS.md) | todas as lojas: o que vendem, preços, horários, serviços | código |
| [`guiao/`](guiao/) | **guião** das cenas da história, fala a fala (prólogo, capítulos, finais) | os dois |
| [`dialogos/`](dialogos/) | **diálogos** dos NPCs (dia a dia, presentes, festivais, cenas de coração, missões), das povoações e dos aldeões | código |
| [`textos/`](textos/) | tutorial, mensagens do Sistema, dicas de carregamento, Bestiário, descrições dos itens, **eventos** (invasões) e **móveis** | código |
| [`lore/diario_aren.md`](lore/diario_aren.md) | as **100 páginas** do diário de Aren | os dois |
| [`mapas/`](mapas/) | **mapas** vistos de cima de Ascendia e de cada andar | os dois |
| [`TRADUCAO.md`](TRADUCAO.md) | regras e glossário da tradução para inglês | código |
| [`PUBLICACAO.md`](PUBLICACAO.md) | textos da página do itch.io, créditos, lista antes de lançar | os dois |
| [`PROPOSTAS.md`](PROPOSTAS.md) | **decisões que faltam tomar** (o nome do jogo, a origem da torre) | tu |

## Ferramentas

- [`../ferramentas/visualizador.html`](../ferramentas/visualizador.html) — ver as tuas tiras de frames animadas e verificar as regras da arte
  (também online: https://claude.ai/artifact/BBE65E9dT8pp4xc81Q9zE8).
- [`../arte/referencia/aranha_mae/`](../arte/referencia/aranha_mae/) — o sprite de referência do estilo.

## Números do jogo (resumo)

| | |
|---|---|
| Andares | 100 (+ infinitos no pós-jogo) em 10 regiões |
| Monstros | 80 normais + 20 com nome + 79 guardiões + 20 bosses + 10 bosses de masmorra |
| Povoações | 26 + Ascendia + a Cidade Errante |
| NPCs | 20 principais em Ascendia + ~90 nas povoações |
| Armas | ~258 |
| Classes / skills | 20 classes · 120 skills de classe · 36 de armas · 12 Skills Únicas · 12 skills de vida |
| Missões | ~270 + infinitas da Guilda |
| Finais | 4 (um secreto) |
