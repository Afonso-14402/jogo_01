# Tutorial

O tutorial **não é um bloco de texto no início**: cada coisa é ensinada **na primeira vez que aparece**, com uma mensagem
do Sistema. Cada mensagem aparece **uma só vez** (fica marcada como vista) e pode ser revista no Diário → "Ajuda".

- `[botão]` é substituído pelo ícone do botão certo (teclado, comando ou toque) — autoload `Entrada`.
- **Bloqueia?** = o jogo espera que o jogador faça a ação antes de continuar (só no prólogo).
- No telemóvel, quando há um botão novo, ele **pisca** durante a dica.

---

## 1. Prólogo (andar 1)

| ID | Quando | Mensagem | Acaba quando | Bloqueia? |
|---|---|---|---|---|
| `tut_mover` | começo do jogo | `[Sistema] Usa [mover] para andar.` | andar 3 m | sim |
| `tut_camara` | depois de andar | `[Sistema] Usa [zoom] para aproximar ou afastar a câmara.` | usar o zoom ou 5 s | não |
| `tut_interagir` | perto da pedra brilhante | `[Sistema] Carrega em [interagir] para apanhar.` | apanhar | sim |
| `tut_atacar` | aparece o 1.º slime | `[Sistema] Hostil detetado. Usa [atacar].` | acertar 1 vez | sim |
| `tut_combo` | 2.º golpe | `[Sistema] Ataca várias vezes seguidas para fazer um combo. O último golpe é mais forte.` | 3 golpes seguidos | não |
| `tut_esquivar` | o slime prepara um salto | `[Sistema] Quando um inimigo se prepara para atacar, usa [esquivar]. Durante a esquiva és invencível.` | esquivar | sim (o jogo abranda até esquivares) |
| `tut_estamina` | 1.ª esquiva | `[Sistema] Esquivar gasta Estamina (barra amarela). Ela recupera sozinha.` | 5 s | não |
| `tut_xp` | 1.º monstro morto | `[Sistema] Monstros dão XP. Com XP suficiente, sobes de nível.` | 5 s | não |
| `tut_drop` | 1.º item no chão | `[Sistema] Os monstros deixam cair coisas. Passa por cima para apanhar.` | apanhar | não |
| `tut_nivel` | subir ao nível 2 | `[Sistema] Subiste de nível! Tens 5 pontos de atributo. Abre o Status com [status] para os distribuir.` | abrir o Status | não |
| `tut_atributos` | abrir o Status | `[Sistema] FOR: dano · AGI: velocidade · DES: arco e críticos · INT: magia · VIT: vida e defesa · SOR: sorte. Escolhe à vontade: podes mudar mais tarde na Igreja.` | fechar | não |
| `tut_erva` | entrar na erva alta | `[Sistema] A erva alta esconde coisas. Corta-a com [atacar].` | cortar 5 tufos | não |
| `tut_aviso` | 1.º ataque com marca vermelha no chão | `[Sistema] As marcas vermelhas no chão mostram onde um ataque vai cair. Sai de cima delas!` | 5 s | não |
| `tut_vida` | vida abaixo de 50% | `[Sistema] Bebe uma poção com [pocao]. Fora de combate, a vida também recupera devagar.` | beber ou 10 s | não |
| `tut_zona_segura` | entrar na Zona Segura | `[Sistema] Zona Segura: aqui não aparecem monstros. A fogueira grava o jogo.` | 5 s | não |
| `tut_cristal` | perto do cristal | `[Sistema] Toca no cristal com [interagir] para viajar entre a cidade e os andares.` | usar | sim |

## 2. Primeiro dia em Ascendia

| ID | Quando | Mensagem | Acaba quando |
|---|---|---|---|
| `tut_falar` | perto do 1.º NPC | `[Sistema] Carrega em [interagir] para falar.` | falar |
| `tut_dialogo` | 1.º diálogo | `[Sistema] Carrega em [aceitar] para continuar. Algumas respostas mudam o que as pessoas pensam de ti.` | — |
| `tut_equipar` | receber a Espada de Treino | `[Sistema] Abre o Equipamento com [inventario] e equipa a espada.` | equipar |
| `tut_missoes` | aceitar a 1.ª missão | `[Sistema] As missões ficam no Diário ([diario]). A missão seguida aparece no ecrã.` | abrir o Diário |
| `tut_mapa` | sair da Guilda | `[Sistema] Abre o mapa com [mapa]. Os ícones mostram lojas, pessoas e missões.` | abrir o mapa |
| `tut_dormir` | entrar no quarto | `[Sistema] Dormir numa cama passa para o dia seguinte e grava o jogo.` | dormir |
| `tut_hora` | 1.ª manhã | `[Sistema] O tempo passa: 1 dia são 20 minutos. As lojas abrem e fecham, e as pessoas mudam de sítio.` | 5 s |

## 3. Primeiros andares

| ID | Quando | Mensagem |
|---|---|---|
| `tut_guardiao` | ver o 1.º guardião | `[Sistema] Cada andar tem um guardião junto à escada. Vence-o para desbloquear o andar seguinte.` |
| `tut_bau` | 1.º baú | `[Sistema] Baús! Madeira: materiais. Prata: equipamento. Ouro: precisa de chave.` |
| `tut_mimico` | 1.º mímico | `[Sistema] Nem tudo o que parece um baú é um baú.` |
| `tut_recolher` | 1.º nó de minério ou árvore | `[Sistema] Bate com uma ferramenta (ou uma arma de martelo ou machado) para recolher materiais.` |
| `tut_ferramenta` | nó de tier superior | `[Sistema] Precisas de uma ferramenta melhor. O Brom faz picaretas.` |
| `tut_elite` | 1.º Elite | `[Sistema] Monstro Elite: mais forte, mas com melhores recompensas.` |
| `tut_nome` | 1.º monstro com nome | `[Sistema] Um monstro com nome! Raro, forte e com recompensas únicas.` |
| `tut_segredo` | 1.º segredo descoberto | `[Sistema] Segredo descoberto! Cada andar tem 1 a 3. O mapa mostra quantos encontraste.` |
| `tut_puzzle` | 1.º puzzle | `[Sistema] Os puzzles abrem caminhos e tesouros. Se estiveres preso, os sussurros, os NPCs e a Madame Oriel dão dicas.` |
| `tut_desafio` | entrar no andar 1 depois do prólogo | `[Sistema] Cada andar tem 2 desafios. Vê-os no mapa. Cumpri-los dá medalhas e recompensas.` |
| `tut_lore` | 1.ª página de lore | `[Sistema] Encontraste uma página de um diário antigo. Lê-a no Diário → Páginas.` |
| `tut_morte` | 1.ª morte | `[Sistema] Morrer não é o fim: acordas na estalagem, mas perdes parte dos materiais do andar.` |
| `tut_estados` | 1.º estado alterado | `[Sistema] Estás {estado}. Os ícones por baixo da vida mostram os estados e quanto tempo duram.` |
| `tut_fraqueza` | 1.º golpe "fraco a" | `[Sistema] Golpe eficaz! Os monstros têm fraquezas a elementos. O Bestiário mostra-as.` |

## 4. Sistemas da cidade

| ID | Quando | Mensagem |
|---|---|---|
| `tut_forja` | 1.ª vez na forja | `[Sistema] Forja: faz armas e ferramentas com materiais. Melhorar dá +5% de dano por nível.` |
| `tut_melhorar_falha` | 1.ª melhoria falhada | `[Sistema] A melhoria falhou, mas a arma está inteira. A próxima tentativa tem mais hipóteses.` |
| `tut_alquimia` | 1.ª vez na alquimia | `[Sistema] Alquimia: faz poções e bombas com ervas e materiais.` |
| `tut_cozinha` | 1.º fogão | `[Sistema] Cozinhar dá pratos que curam e dão bónus. Só um bónus de comida de cada vez.` |
| `tut_receitas` | descobrir uma receita | `[Sistema] Receita nova! As receitas aprendem-se com pessoas, livros ou a experimentar.` |
| `tut_presentes` | 2.º dia a falar com o mesmo NPC | `[Sistema] Podes dar presentes às pessoas. Cada uma gosta de coisas diferentes. Um por dia.` |
| `tut_coracoes` | 1.º coração | `[Sistema] A amizade sobe com conversas, presentes e missões. Com mais corações, há cenas e recompensas.` |
| `tut_skills_uso` | Manejo de Espada nv 2 | `[Sistema] As skills sobem com o uso: quanto mais usas uma arma, melhor ficas com ela.` |
| `tut_skill_arma` | Manejo nv 3 | `[Sistema] Novo ataque especial! Põe-no na barra de skills ([skills]).` |
| `tut_classe` | nível 10 | `[Sistema] Atingiste o nível 10. Fala com o Mestre Gorvan para escolher uma classe.` |
| `tut_rank` | 1.º rank novo | `[Sistema] O teu rank subiu! Ranks mais altos abrem missões e lojas novas.` |

## 5. Mais tarde

| ID | Quando | Mensagem |
|---|---|---|
| `tut_pesca` | missão R1_03 | `[Sistema] Lança com [atacar] (segura para ir mais longe). Quando a boia afundar, carrega logo. Depois mantém o peixe dentro da zona verde.` |
| `tut_quinta` | abrir a quinta | `[Sistema] Planta sementes, rega-as todos os dias e colhe quando estiverem prontas. Cada planta tem as suas estações.` |
| `tut_companheiro` | 1.º companheiro | `[Sistema] Companheiro na equipa! Dá ordens com [ordens]: Atacar, Defender, Ficar, Seguir.` |
| `tut_animal` | 1.º animal de estimação | `[Sistema] O teu animal ganha XP contigo. Dá-lhe comida e carinho para ficar mais feliz e mais forte.` |
| `tut_casa` | receber a casa (andar 20) | `[Sistema] Tens casa! Cama, fogão e baús. Decora-a com móveis e expõe os teus troféus.` |
| `tut_montada` | 1.ª montada | `[Sistema] Chama a montada com [montada] fora de combate. Se levares dano, cais.` |
| `tut_gancho` | receber o Gancho | `[Sistema] Aponta para um ponto de gancho (anel brilhante) e carrega em [skill_unica] para te puxares.` |
| `tut_escuro` | região 2 | `[Sistema] Está escuro. Usa tochas ou uma lanterna. Alguns inimigos só se veem com luz.` |
| `tut_calor_pantano` | andar 21 | `[Sistema] Calor: a Estamina recupera mais devagar. Bebe água ou Água de Coco para o aguentar (5 min).` |
| `tut_temperatura` | região 5 | `[Sistema] Temperatura: o frio desce a barra. Perto de fogueiras sobe. Comida quente também ajuda.` |
| `tut_ar` | região 6 | `[Sistema] Debaixo de água tens uma barra de Ar. Sem ar, perdes vida. Procura bolhas.` |
| `tut_calor` | região 7 | `[Sistema] Calor: perto da lava a barra sobe. Bebe água ou Poção Fresca.` |
| `tut_luz_sagrada` | região 8 | `[Sistema] A névoa roxa amaldiçoa. As zonas de luz curam e os mortos-vivos não entram.` |
| `tut_planar` | Capa Planadora | `[Sistema] No ar, segura [esquivar] para planar.` |
| `tut_falhas` | região 10 | `[Sistema] D̷e̷t̷e̷t̷a̷d̷a̷ ̷u̷m̷a̷ ̷f̷a̷l̷h̷a̷. Não confies em tudo o que vês.` |
