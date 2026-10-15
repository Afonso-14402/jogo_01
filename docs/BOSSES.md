# Bosses

Os **20 bosses** da torre (10 mini-bosses nos andares 5, 15, 25… e 10 bosses nos andares 10, 20, 30…),
mais o **duelo com o Kai** (andar 68). Os guardiões dos outros andares e os bosses das masmorras escondidas
estão nos ficheiros de cada região (`docs/regioes/`).

### Regras comuns (ver `docs/SISTEMAS.md`, secção 7)
- **Arena fechada**, barra de vida grande com nome e título, música própria.
- **Fases** por limiares de vida; ao mudar de fase há uma pequena cena (1–2 s) e o boss fica invencível nesse tempo.
- **Fúria** aos 5 minutos: +30% de velocidade.
- **Todos os ataques têm aviso** (pose + marca vermelha no chão). Na tabela, "aviso" é o tempo entre o aviso e o golpe.
- **Mini-boss**: nível do andar +2, HP ×15. **Boss**: nível do andar +3, HP ×30.
- **Recompensa da 1.ª vitória**: arma única garantida, **troféu** para a casa, título, muita XP e ouro, materiais raros.
  Vitórias seguintes (o boss volta passado 1 dia): materiais e 25% de hipótese da arma única.
- **Tamanho dos sprites**: mini-bosses 64×64; bosses 96×96 a 128×128.
- **Animações mínimas**: parado, mover, cada ataque, mudança de fase, dano (1), morrer (6–8).

---

## 1. Javali-Rei — andar 5 (mini-boss)

| | |
|---|---|
| Título | *O Rei das Tocas* |
| Nível / Tamanho | 7 · 64×64 |
| Aspeto | javali enorme de pelo castanho-escuro, presas de marfim rachadas, coroa de raízes e cicatrizes de flechas antigas |
| Arena | **Grande Toca**: cratera de terra com árvores à volta e lama no centro |
| Fraco a | Fogo · resiste a Físico de frente (−20%) |
| Mecânica especial | Tal como os javalis normais, **se bater numa árvore fica atordoado 3 s** (o momento de atacar). Na fase 2 as árvores partem-se ao 2.º choque |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–60% | **Carga Real**: corre em linha reta (aviso 1 s: raspa a pata, bufa vapor) · **Cabeçada** (aviso 0,5 s) · **Chamar Javalis**: 2 javalis normais (uma vez) |
| 2 | 60–0% | **Carga Tripla**: três cargas seguidas, a mudar de direção · **Terramoto**: salta e cai, onda de choque em anel (aviso 0,8 s: salta) · a lama do centro espalha-se (Lentidão) |

| Recompensas | |
|---|---|
| Arma única | **Presa do Javali-Rei** (machado) — investida que derruba inimigos |
| Troféu | Cabeça do Javali-Rei (para pendurar na parede) |
| Título | *Caçador de Reis* |
| Outros | Couro de Javali ×10 · Presa Real |

---

## 2. Ent Ancião — andar 10 (boss)

| | |
|---|---|
| Título | *Guardião da Floresta* |
| Nível / Tamanho | 13 · 128×128 |
| Aspeto | árvore gigante com cara de velho, barba de musgo, olhos de luz verde, galhos como braços, raízes como pernas; metade do corpo está seca |
| Arena | **Raízes da Árvore-Mãe**: clareira circular rodeada de raízes, com a Árvore-Mãe ao fundo |
| Fraco a | Fogo (queimadura dura o dobro) · resiste a Água e Físico (−10%) |
| Mecânica especial | As **8 lanternas** do Caminho das Lanternas, se as acendeste, dão +10% de dano. Na fase 2, **pontos de seiva** brilhantes aparecem no tronco: acertar neles faz ×2 |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–70% | **Varrer com o Braço** (área à frente, aviso 0,9 s) · **Raízes em Linha**: 3 linhas de raízes saem do chão (aviso 1 s: o chão racha) · **Chuva de Bolotas** (projéteis em área) |
| 2 | 70–35% | Chama **2 Treants Jovens** · **Prisão de Raízes**: raízes rodeiam-te (esquivar para fora antes de fechar, 1,2 s) · **Folhas Cortantes**: tornado de folhas que anda pela arena |
| 3 | 35–0% | **Fúria da Floresta**: a arena enche-se de raízes (só ficam caminhos) · **Pisão Gigante** (área grande, aviso 1,2 s: levanta a raiz-perna) · **Grito da Árvore**: Medo 1 s (aviso 1,5 s) |

| Recompensas | |
|---|---|
| Arma única | **Raiz Ancestral** (cajado) — raízes prendem os inimigos |
| Troféu | Ramo do Ent (decoração que dá flores na primavera) |
| Título | *Amigo da Floresta* |
| Cena | A Árvore-Mãe fala contigo antes de morrer: "Não sejas como o anterior." |

---

## 3. Aranha-Mãe — andar 15 (mini-boss)

| | |
|---|---|
| Título | *A Mãe do Ninho* |
| Nível / Tamanho | 17 · 64×64 — **sprite de referência**: `arte/referencia/aranha_mae/` |
| Aspeto | aranha roxa-escura com setas vermelhas nas costas que brilham, olhos vermelhos, presas brancas com veneno verde, um saco de ovos de seda atrás |
| Arena | **O Ninho**: gruta redonda forrada de teias; casulos pendurados |
| Fraco a | Fogo, Raio · resiste a Veneno |
| Mecânica especial | **Teias no chão** (Lentidão). Podes **queimá-las** (tocha, fogo) — mas o desafio do andar pede para não o fazer. O **saco de ovos** pode ser atacado: destruí-lo antes da fase 2 impede o "Chamar as Crias" |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–55% | **Mordida Venenosa** (aviso 0,6 s: encolhe-se e levanta as patas da frente) · **Cuspe de Teia**: projétil, Lentidão (aviso 0,5 s) · **Descer do Teto**: sobe por um fio e cai em cima de ti (aviso: sombra no chão 1 s) |
| 2 | 55–0% | **Chamar as Crias**: o saco de ovos incha (fica rosa, 1,5 s) e rebenta — saem 4 aranhas bebés · **Chuva de Veneno**: gotas verdes caem do teto em zonas marcadas · **Investida em Leque**: 3 saltos seguidos |

| Recompensas | |
|---|---|
| Arma única | **Presa Venenosa** (adaga) — envenena |
| Troféu | Teia Dourada (decoração) |
| Título | *Sem Medo de Aranhas* |
| Outros | Seda de Aranha ×15 · Glândula de Veneno ×5 |

---

## 4. Golem de Cristal — andar 20 (boss)

| | |
|---|---|
| Título | *O Rei Sentado* |
| Nível / Tamanho | 23 · 128×128 |
| Aspeto | golem gigante de rocha cinzenta com cristais azuis, roxos e verdes a sair dos ombros e do peito; um núcleo de luz no peito |
| Arena | **Sala do Trono**: salão com **6 colunas de cristal** e um trono de pedra |
| Fraco a | Raio, Martelo (×1,5) · imune a Veneno |
| Mecânica especial | Enquanto houver **colunas de cristal** de pé, o golem tem um **escudo** (dano −70%). Partir as colunas (bater-lhes 5 vezes, ou fazer o golem bater nelas com o laser) tira o escudo |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–65% | **Murro de Cristal** (aviso 0,9 s) · **Laser do Núcleo**: raio em linha que roda devagar (aviso 1,2 s: o núcleo acende) · **Estalagmites**: saem do chão onde estás (aviso 0,8 s) |
| 2 | 65–30% | Levanta-se do trono · **Chuva de Cristais** (área) · **Pisão em Anel** · **Refazer Coluna**: tenta fazer crescer uma coluna nova (interrompe-o atacando o núcleo) |
| 3 | 30–0% | O núcleo fica exposto e **sobreaquece** · **Laser Duplo** (dois raios em X) · **Explosão de Cristal** ao chegar a 10% (corre para longe: aviso 2 s) |

| Recompensas | |
|---|---|
| Arma única | **Núcleo de Cristal** (martelo) — ondas de choque de cristal |
| Troféu | Fragmento do Núcleo (luz para a casa) |
| Título | *Quebra-Cristais* |
| Depois | O Governador Aldric oferece-te uma **casa** em Ascendia |

---

## 5. Serpente do Lodo — andar 25 (mini-boss)

| | |
|---|---|
| Título | *A Guardiã do Ovo de Pedra* |
| Nível / Tamanho | 27 · 64×64 (o corpo sai e entra na água) |
| Aspeto | serpente gigante verde-acastanhada coberta de lodo e algas, olhos amarelos, coroa de pedra antiga na cabeça |
| Arena | **Altar Inundado**: sala do templo com água pelos joelhos e plataformas de pedra; alavancas nas paredes |
| Fraco a | Fogo · resiste a Água |
| Mecânica especial | **Alavancas de água**: subir a água ajuda-a (fica mais rápida); **baixar** a água deixa-a encalhada 4 s (vulnerável ×1,5). Ela volta a subir a água ao fim de 15 s |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Mordida** a sair da água (aviso: bolhas no sítio 0,8 s) · **Cuspe de Lodo**: Lentidão · **Cauda** (varre as plataformas) |
| 2 | 50–0% | **Constrição**: enrola-se numa coluna e faz cair pedras · **Tsunami de Lodo**: onda que atravessa a sala (saltar para uma plataforma alta) · **Olhar Hipnótico**: Lentidão forte 2 s |

| Recompensas | |
|---|---|
| Arma única | **Língua de Serpente** (lança) — estocada dupla |
| Troféu | Coroa de Pedra da Serpente |
| Título | *Encantador de Serpentes* |

---

## 6. Hidra do Pântano — andar 30 (boss)

| | |
|---|---|
| Título | *A Que Não Morre* |
| Nível / Tamanho | 33 · 128×128 |
| Aspeto | corpo enorme de lagarto do pântano dentro do lago ritual, com **3 cabeças** de serpente (verde, roxa, amarela); escamas cobertas de musgo |
| Arena | **O Altar**: lago ritual com ilhas de pedra e **6 braseiros** à volta |
| Fraco a | Fogo · resiste a Veneno |
| Mecânica especial | **Cabeças**: cada cabeça tem vida própria. Cortar uma cabeça → passados 8 s **nascem duas** no lugar, **a não ser que queimes o pescoço** (fogo, ou empurrá-la contra um braseiro aceso). O corpo só leva dano quando não tem cabeças (ou cada cabeça cortada tira 15% ao corpo). Máximo de 5 cabeças |

| Cabeça | Ataque |
|---|---|
| Verde | **Veneno**: cuspe que deixa poça venenosa |
| Roxa | **Maldição**: raio que causa Maldição |
| Amarela | **Ácido**: cone que tira DEF −20% durante 10 s |

| Fase | Vida do corpo | Ataques do corpo |
|---|---|---|
| 1 | 100–50% | **Pisão no Lago** (ondas) · as cabeças atacam uma de cada vez |
| 2 | 50–0% | As cabeças atacam **juntas** (combinações) · **Rugido Triplo**: Medo · **Mergulho**: o corpo afunda e volta a sair noutro lado da arena |

| Recompensas | |
|---|---|
| Arma única | **Arco da Hidra** (arco) — dispara 3 flechas de uma vez |
| Troféu | Três Dentes da Hidra |
| Título | *Corta-Cabeças* |
| Depois | Abre a Arena (prata) e os minijogos da Taberna |

---

## 7. Escorpião Imperador — andar 35 (mini-boss)

| | |
|---|---|
| Título | *Imperador das Areias* |
| Nível / Tamanho | 37 · 64×64 |
| Aspeto | escorpião negro e dourado com a **marca azul do Sistema** na carapaça, pinças enormes e uma cauda com ferrão de ouro |
| Arena | **Cratera do Ninho**: areia escura com buracos e carapaças |
| Fraco a | Gelo · resiste a Fogo e Veneno |
| Mecânica especial | **Enterra-se** na areia e aparece noutro sítio (aviso: a areia mexe-se em linha). O **ferrão** pode ser partido (o desafio de não ser envenenado fica mais fácil): acertar 10 vezes na cauda quando ele a crava no chão |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Pinças em Tesoura** (área à frente) · **Ferrão** (aviso 0,8 s: a cauda treme): Veneno forte · **Enterrar-se** |
| 2 | 50–0% | **Chuva de Ferrões**: dispara ferrões para o ar que caem em zonas marcadas · **Tempestade de Areia** na arena (Cegueira) · chama **Escaravelhos de Fogo** |

| Recompensas | |
|---|---|
| Arma única | **Ferrão Imperial** (besta) — virotes que envenenam |
| Troféu | Carapaça Imperial |
| Título | *Destronador* |

---

## 8. Faraó Eterno — andar 40 (boss)

| | |
|---|---|
| Título | *O Que Também Subiu* |
| Nível / Tamanho | 43 · 96×96 |
| Aspeto | múmia real de ligaduras douradas, máscara de ouro, cetro em forma de serpente; os olhos brilham azul (é um antigo Jogador) |
| Arena | **Sala do Sarcófago**: câmara enorme com estátuas de deuses-animais e um sarcófago de ouro ao centro |
| Fraco a | Fogo (as ligaduras ardem), Gelo, Luz · imune a Veneno |
| Mecânica especial | **Areia a encher**: na fase 3 a sala enche-se de areia aos poucos (fica mais apertado). **Estátuas**: na fase 2 o Faraó dá vida a 2 estátuas (destruí-las cura-te 10%) |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–65% | **Cetro-Serpente**: golpe e raio em linha (aviso 0,9 s) · **Ligaduras**: atira ligaduras que prendem (aviso 0,7 s) · **Maldição do Faraó** (aviso 1 s) |
| 2 | 65–30% | **Despertar das Estátuas**: 2 estátuas de deuses-animais lutam com ele · **Praga de Escaravelhos**: enxame que corre pelo chão · **Teletransporte** para o sarcófago |
| 3 | 30–0% | A areia começa a encher · **Tempestade do Deserto** · **Julgamento**: uma balança aparece; se estiveres com mais vida do que ele em %, levas dano grande (baixa a vida dele antes!) |

| Recompensas | |
|---|---|
| Arma única | **Khopesh do Faraó** (espada) — invoca escaravelhos |
| Troféu | Máscara do Faraó |
| Título | *Quebra-Maldições* |
| Cena | "Eu também subi. Eu também quis voltar." Depois vira pó |

---

## 9. Yeti Ancião — andar 45 (mini-boss)

| | |
|---|---|
| Título | *O Que Se Lembra* |
| Nível / Tamanho | 47 · 64×64 |
| Aspeto | yeti enorme de pelo branco e sujo, cara azulada, braços muito compridos, um colar com objetos de Jogadores mortos |
| Arena | **Gruta do Yeti**: gruta de gelo com estalactites e montes de neve |
| Fraco a | Fogo · resiste a Gelo |
| Mecânica especial | **Estalactites**: o Yeti faz cair estalactites; se caírem em cima dele, fica atordoado 3 s. **Bolas de neve**: podes **devolver** as bolas de neve dele com um golpe no momento certo |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Murro Duplo** · **Bola de Neve Gigante** (rola pela gruta; aviso 1 s) · **Rugido**: estalactites caem (sombras no chão) |
| 2 | 50–0% | **Fúria Gelada**: fica azul e mais rápido · **Avalanche**: neve cai de um lado da gruta (fugir para o outro) · **Agarrar e Atirar** (aviso 0,8 s) |

| Recompensas | |
|---|---|
| Arma única | **Punhos do Yeti** (manoplas) — socos que congelam |
| Troféu | Colar do Yeti (lore: objetos de Jogadores antigos) |
| Título | *Coração Quente* |

---

## 10. Dragão de Gelo — andar 50 (boss)

| | |
|---|---|
| Título | *O Meio do Caminho* |
| Nível / Tamanho | 53 · 128×128 |
| Aspeto | dragão branco e azul com escamas de gelo transparente, asas enormes, chifres de cristal, sopro azul |
| Arena | **Ninho do Dragão**: topo plano de uma montanha com estacas de gelo e vento forte |
| Fraco a | Fogo · imune a Gelo |
| Mecânica especial | **Voo**: o dragão voa e ataca de cima; enquanto voa só se lhe acerta com arco, besta, cajado ou quando mergulha. **Estacas de gelo** que ele cria servem de **abrigo** contra o sopro |

| Fase | Vida | Ataques |
|---|---|---|
| 1 (no chão) | 100–70% | **Mordida** · **Garras** · **Cauda** (atrás) · **Sopro Gélido** em cone (aviso 1,2 s: inspira e o peito brilha) |
| 2 (no ar) | 70–35% | **Mergulho** em linha · **Chuva de Estacas** (marcas no chão) · **Sopro do Alto** (varre a arena: esconder atrás de estacas) |
| 3 (furioso) | 35–0% | Volta ao chão · **Tempestade de Gelo** (Frio constante: ficar perto das fogueiras da arena) · **Prisão de Gelo**: congela uma zona; quem lá estiver fica Congelado |

| Recompensas | |
|---|---|
| Arma única | **Sopro Gélido** (katana) — corte que congela em linha |
| Troféu | Escama de Dragão de Gelo (escudo de parede) |
| Título | *Matador de Dragões* |
| Cena | "Os outros vinham com amigos." Festa enorme em Ascendia (andar 50) |

---

## 11. Capitão Esqueleto — andar 55 (mini-boss)

| | |
|---|---|
| Título | *O Contador de Ouro* |
| Nível / Tamanho | 57 · 64×64 |
| Aspeto | esqueleto de capitão pirata com chapéu de penas, casaco vermelho rasgado, sabre e um gancho, um papagaio-esqueleto no ombro |
| Arena | **Cais do Capitão**: o convés de um navio atracado dentro da gruta, com canhões |
| Fraco a | Luz, Raio, Martelo · imune a Veneno |
| Mecânica especial | **Canhões**: podes usar os canhões do convés contra ele (carregar com pólvora: 3 s). **O papagaio** avisa os ataques dele ("Lá vai!") — se o papagaio for derrubado, os avisos ficam mais curtos mas ele fica mais lento |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Esgrima**: combo de 4 golpes · **Gancho**: puxa-te · **Pistola** (aviso 1,2 s) |
| 2 | 50–0% | **Tripulação**: chama 4 Piratas Esqueleto · **Bombardeio**: os canhões do navio inimigo disparam em linhas · **Remontar**: aos 10% desfaz-se e volta a montar-se uma vez (parte o crânio!) |

| Recompensas | |
|---|---|
| Arma única | **Sabre do Afogado** (espada) — cura ao acertar |
| Troféu | Chapéu do Capitão |
| Título | *Terror dos Mares* |
| Outros | **Chave do Almirante** (masmorra escondida do andar 56) |

---

## 12. Leviatã — andar 60 (boss)

| | |
|---|---|
| Título | *O Último do Mar* |
| Nível / Tamanho | 63 · 128×128 (só se vê uma parte de cada vez) |
| Aspeto | serpente marinha colossal de escamas azul-escuras, barbatanas como velas, olhos tristes e luminosos |
| Arena | **Mar Aberto** (fase 1, no teu barco) e **O Trono** (fases 2 e 3, ilha de rocha no centro do redemoinho) |
| Fraco a | Raio · resiste a Água |
| Mecânica especial | **Fase no barco**: usar os **canhões** do barco e o leme para fugir. O barco tem vida própria (se afundar, vais parar à ilha com −30% de vida). **Na ilha**: o Leviatã enrola-se à volta dela |

| Fase | Vida | Ataques |
|---|---|---|
| 1 (barco) | 100–70% | **Investida** contra o barco · **Onda Gigante** · **Redemoinho** que puxa o barco |
| 2 (ilha) | 70–35% | **Mordida** a sair da água · **Jato de Água** em linha · **Chuva** (Encharcado: cuidado com os teus próprios raios!) |
| 3 (ilha) | 35–0% | **Enrolar a Ilha**: a ilha encolhe (o corpo ocupa as bordas) · **Grito do Abismo** (Medo) · **Tsunami** (saltar para cima de rochas) |

| Recompensas | |
|---|---|
| Arma única | **Tridente do Leviatã** (lança) — ondas de água |
| Troféu | Escama do Leviatã |
| Título | *Senhor dos Mares* |
| Cena | O Leviatã tinha medo — "da janela azul atrás de ti" |

---

## 13. Ferreiro Infernal — andar 65 (mini-boss)

| | |
|---|---|
| Título | *O Que Forjou o Teu Número* |
| Nível / Tamanho | 67 · 64×64 |
| Aspeto | demónio grande de pele vermelha-escura, avental de couro queimado, um martelo enorme, uma fornalha no peito, chifres partidos |
| Arena | **Arena-Forja**: forja gigante com bigornas, canais de metal fundido e martelos mecânicos |
| Fraco a | Gelo · imune a Fogo |
| Mecânica especial | **Canais de metal fundido**: alavancas desviam o metal — podes desviá-lo **contra ele** (3 vezes = desafio). **Martelos mecânicos** batem em ritmo e acertam em quem lá estiver (ele também) |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Martelada** (onda de choque em linha) · **Atirar Metal Fundido** (poças) · **Forjar**: bate na bigorna e faz uma arma de fogo que atira contra ti |
| 2 | 50–0% | **Fornalha Aberta**: o peito abre e lança fogo em cone (aviso 1 s) · **Tempestade de Faúlhas** · **Martelos Loucos**: os martelos mecânicos aceleram |

| Recompensas | |
|---|---|
| Arma única | **Martelo da Forja** (martelo) — golpes em chamas |
| Troféu | Bigorna Infernal (forja pequena para a casa) |
| Título | *Mais Forte que o Ferro* |
| Outros | A **arma inacabada nº 10 000** (o Brom acaba-a: ver `docs/NPCS.md`) |

---

## 14. Kai — andar 68 (duelo da história)

| | |
|---|---|
| Título | *Jogador nº 9 999* |
| Nível / Tamanho | o teu nível · 32×32 (como o herói) |
| Aspeto | o Kai de sempre, mas com os olhos a brilhar azul e uma armadura escura que o Sistema lhe deu |
| Arena | **Plataforma do Duelo**: plataforma redonda no meio do lago de magma da cratera |
| Mecânica especial | **Salvar ou vencer.** Durante a luta aparecem **3 escolhas de diálogo**, aos 75%, 50% e 25% da vida dele. Para o salvar: **6+ corações com o Kai** e as **3 respostas certas** (lembrar-lhe as promessas que fizeram). A 3.ª resposta certa só aparece se tiveres a flag `kai_promessa_1` ou `kai_promessa_2` (cenas do jantar e de 8 ❤️) ou `kai_luar` (cena de 6 ❤️). Se conseguires, ele **para de lutar**: o Sistema perde o controlo dele. Senão, a luta vai até ao fim (ver `docs/dialogos/kai.md`, missão R7_11) |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–75% | Espada rápida: combos de 3 · **Dash** (como a tua esquiva) |
| 2 | 75–50% | **Corte em Cruz** (onda em X) · **Imagens**: 2 cópias dele |
| 3 | 50–25% | **Poder do Sistema**: janelas azuis à volta dele disparam raios |
| 4 | 25–0% | **Desespero**: ataques fortes e lentos, ele fica a chorar entre ataques |

| Resultado | Recompensa |
|---|---|
| **Salvaste o Kai** | **Amuleto da Amizade** · o Kai volta a Ascendia e depois vai para o Último Posto · conta para o **final secreto** |
| **Venceste o Kai** | **Lâmina do Kai** (espada) · o Kai desaparece (só volta no andar 100, como parte do final) |

---

## 15. Titã de Magma — andar 70 (boss)

| | |
|---|---|
| Título | *O Coração do Vulcão* |
| Nível / Tamanho | 73 · 128×128 (sai do magma da cintura para cima) |
| Aspeto | gigante de rocha negra com fendas de lava por todo o corpo, uma coroa de chamas e olhos brancos |
| Arena | **O Coração**: ilhas de rocha a flutuar num poço de magma |
| Fraco a | Gelo, Água · imune a Fogo |
| Mecânica especial | **Ilhas**: o Titã afunda ilhas (tens de saltar entre elas). Os **punhos** dele ficam no chão depois de um murro: são o momento de subir pelo braço e atacar o **núcleo** no peito (×2) |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–65% | **Murro na Ilha** (aviso 1,2 s: o punho sobe) · **Chuva de Lava** · **Onda de Magma** |
| 2 | 65–30% | **Afundar Ilhas** · **Chamar Elementais de Fogo** · **Sopro Vulcânico** em cone |
| 3 | 30–0% | **Erupção**: a arena toda treme, rochas caem · **Abraço do Titã**: tenta apanhar-te com as duas mãos (esquivar para dentro, entre as mãos) |

| Recompensas | |
|---|---|
| Arma única | **Coração de Magma** (espada grande) — explosão de lava |
| Troféu | Pedra-Coração do Titã (aquece a casa toda) |
| Título | *Mais Quente que a Lava* |
| Depois | O vulcão adormece; o Calor da região sobe metade |

---

## 16. Lich Bibliotecário — andar 75 (mini-boss)

| | |
|---|---|
| Título | *O Que Leu Demais* |
| Nível / Tamanho | 77 · 64×64 |
| Aspeto | esqueleto alto de túnica roxa com óculos redondos partidos, uma coroa de velas e livros a orbitar à volta |
| Arena | **Sala do Lich**: sala redonda de estantes altíssimas, com escadas de rodas |
| Fraco a | Luz, Fogo (os livros) · resiste a Sombra |
| Mecânica especial | **Livros em órbita**: cada livro é um feitiço. O Lich **lê** um livro antes de o usar (aviso: o livro abre-se à frente dele e brilha). Se ler **3 feitiços seguidos** sem ser interrompido, faz o **Feitiço Proibido**. Bater-lhe enquanto lê interrompe. Destruir os livros em órbita tira-lhe feitiços |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Livro de Fogo** (bolas de fogo) · **Livro de Gelo** (estacas) · **Livro de Raio** (raio em cadeia) · **Silêncio na Biblioteca**: ficas em Silêncio 3 s |
| 2 | 50–0% | **Chamar Esqueletos** (4) · **Estantes a Cair**: empurra estantes (aviso: inclinam) · **Feitiço Proibido**: um círculo enorme que tira 50% da vida (só se ele ler 3 seguidos) |

| Recompensas | |
|---|---|
| Arma única | **Grimório Proibido** (cajado) — invoca esqueletos |
| Troféu | Óculos do Lich |
| Título | *Leitor Proibido* |

---

## 17. Rei Sem Coroa — andar 80 (boss)

| | |
|---|---|
| Título | *O Que Tentou Parar a Torre* |
| Nível / Tamanho | 83 · 96×96 |
| Aspeto | rei-cavaleiro morto-vivo de armadura negra e dourada, capa real rasgada, espada grande, sem coroa (a coroa flutua no ar acima do trono) |
| Arena | **Sala do Trono**: salão real enorme com vitrais roxos e um trono partido |
| Fraco a | Luz · resiste a Sombra |
| Mecânica especial | **A coroa flutuante**: o Rei tenta alcançá-la. Se a coroa tocar no trono, ele **recupera 10% de vida** e fica mais forte. Os teus ataques à coroa **empurram-na** para longe do trono |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–65% | **Golpe Real** (área em arco) · **Investida com Escudo** · **Ordem**: chama 2 Cavaleiros Esqueleto |
| 2 | 65–30% | **Espada Amaldiçoada**: os golpes deixam Maldição · **Grito do Rei** (Medo em toda a sala) · **Chuva de Espadas** fantasmas |
| 3 | 30–0% | **Último Juramento**: os fantasmas dos cavaleiros (andar 79) aparecem e lutam **ao teu lado** se fizeste a missão do banquete · **Corte do Fim do Reino** (aviso 2 s: linha enorme no chão) |

| Recompensas | |
|---|---|
| Arma única | **Lâmina do Rei Caído** (espada grande) — os ataques ignoram a defesa |
| Troféu | A Coroa do Reino |
| Título | *Coroado* |
| Cena | "Tentei parar a torre. Ninguém pode. Talvez tu." O Gorvan fala contigo em Ascendia |

---

## 18. Grifo Real — andar 85 (mini-boss)

| | |
|---|---|
| Título | *O Pai dos Ninhos* |
| Nível / Tamanho | 87 · 64×64 |
| Aspeto | grifo dourado (corpo de leão, cabeça e asas de águia) com uma crista de penas brancas e olhos de âmbar |
| Arena | **Pico do Grifo Real**: topo de penhasco com o ninho dele e vento forte |
| Fraco a | Sombra · resiste a Ar |
| Mecânica especial | **Vento**: rajadas empurram-te para a borda (cair = voltar à plataforma com −10%). **O ninho**: se te puseres entre ele e o ninho, ele fica furioso (mais forte, mas descuidado: mais aberturas) |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Garras** · **Bicada** · **Rajada das Asas** (empurra) · **Mergulho** (aviso: grito) |
| 2 | 50–0% | **Voo Alto**: ataca só a mergulhar (atinge-o com arco/besta ou esquiva no momento certo e ataca quando aterra) · **Tornado de Penas** · **Grito** que chama 2 Harpias |

| Recompensas | |
|---|---|
| Arma única | **Pena de Grifo** (arco) — flechas que perseguem |
| Troféu | Pena Real do Grifo |
| Título | *Senhor dos Céus* |

---

## 19. Serafim Caído — andar 90 (boss)

| | |
|---|---|
| Título | *O Que Serviu o Administrador* |
| Nível / Tamanho | 93 · 128×128 |
| Aspeto | anjo enorme de seis asas: três brancas e três negras; um lado da cara é de luz e o outro de sombra; uma foice de duas cores |
| Arena | **Varanda do Fim**: varanda aberta para o céu; o chão está dividido em **metade luz** e **metade sombra** |
| Fraco a | Sombra (quando está do lado da luz) e Luz (quando está do lado da sombra) |
| Mecânica especial | **Luz e sombra**: o Serafim muda de forma conforme o lado da arena onde está. No lado da **sombra** tu perdes 2% de vida por segundo (não fiques lá mais de 10 s — desafio) |

| Fase | Vida | Ataques |
|---|---|---|
| 1 (luz) | 100–65% | **Lança de Luz** · **Chuva de Penas Brancas** · **Juízo**: raios de luz caem em colunas |
| 2 (sombra) | 65–30% | **Foice das Sombras** (área enorme) · **Asas Negras**: escurece a arena · **Clones de Sombra** |
| 3 (ambos) | 30–0% | Muda de lado a cada 10 s · **Eclipse**: toda a arena fica de sombra durante 5 s (aviso 2 s) · **Queda do Anjo**: voa e cai no centro |

| Recompensas | |
|---|---|
| Arma única | **Foice do Serafim** (foice) — golpes de luz e sombra |
| Troféu | Asa do Serafim |
| Título | *Além do Céu* |
| Cena | **A verdade**: o Administrador está cansado e procura um sucessor (ver `docs/HISTORIA.md`) |

---

## 20. Guardião do Tempo — andar 95 (mini-boss)

| | |
|---|---|
| Título | *O Que Te Viu Mil Vezes* |
| Nível / Tamanho | 97 · 64×64 |
| Aspeto | figura alta de bronze com um relógio no lugar da cara, quatro braços (dois ponteiros como espadas, uma ampulheta, um pêndulo) |
| Arena | **Arena das Engrenagens**: chão de engrenagens gigantes que rodam |
| Fraco a | Martelo, Raio · resiste a Luz e Sombra |
| Mecânica especial | **Bolhas de tempo**: ele cria bolhas lentas (dentro, tudo lento) e rápidas. Atrair os ataques dele para uma bolha lenta torna-os fáceis de esquivar. **Rebobinar**: uma vez por fase, volta à vida que tinha 10 s antes — mas se lhe partires a ampulheta (bater-lhe 10 vezes na mão da ampulheta) já não o pode fazer |

| Fase | Vida | Ataques |
|---|---|---|
| 1 | 100–50% | **Ponteiros** (golpes em cruz) · **Parar o Tempo**: ficas Parado 1,5 s (aviso: TIQUE… TAQUE… muito alto) · **Engrenagens** que rodam e empurram |
| 2 | 50–0% | **Acelerar**: fica 2× mais rápido 5 s · **Eco do Passado**: aparece uma cópia de ti que repete o que fizeste há 5 s (e ataca-te) · **Fim do Tempo**: a arena escurece e só os ponteiros brilham |

| Recompensas | |
|---|---|
| Arma única | **Segundo Parado** (adaga) — abranda o tempo à volta |
| Troféu | Relógio Parado |
| Título | *Senhor do Tempo* |

---

## 21. O Administrador — andar 100 (boss final)

| | |
|---|---|
| Título | *Aren, Jogador nº 1* |
| Nível / Tamanho | 103 · 32×32 na fase 1 (uma pessoa normal) → 128×128 nas fases 3 e 4 |
| Aspeto | **fase 1**: um homem cansado de cabelo branco e roupa simples, com olhos azuis como a janela do Sistema; **fases 3–4**: uma figura enorme feita de janelas azuis do Sistema |
| Arena | **O Trono do Administrador**: uma sala com janelas azuis a flutuar, que muda a cada fase |
| Fraco a | nada fixo: em cada fase a **janela do Sistema** dele diz a fraqueza (e às vezes mente — na fase 4) |
| Mecânica especial | **O Sistema falha**: a interface vai desaparecendo, os números de dano mentem, o chão vira janelas azuis. **Antes da luta** o Administrador **oferece-te o lugar dele** — se aceitares logo, vais para o final "O novo Administrador" sem lutar |

| Fase | Vida | Como é |
|---|---|---|
| 1 — **O Jogador nº 1** | 100–75% | Luta como um Jogador: espada simples, esquivas, skills. Fala contigo ("Também tive medo") |
| 2 — **As Memórias** | 75–50% | Chama **Ecos dos teus bosses** (um de cada região, 1 ataque cada) usando a tua própria história contra ti |
| 3 — **O Sistema** | 50–25% | Torna-se a figura de janelas azuis. **Janelas** que disparam, **Menus** que te prendem ("Tens a certeza? Sim/Não"), **barra de vida falsa**. Os **companheiros** e os NPCs com 10 corações aparecem em janelas a **ajudar-te** (cada um faz 1 ataque) |
| 4 — **O Fim** | 25–0% | A interface desaparece toda. Só tu, ele e o som. O ataque final dele é uma janela gigante: **"Desistir?"** — tens de a **partir** (atacar), não carregar em "Sim" |

| Depois | |
|---|---|
| Escolha final | Ver os **4 finais** em `docs/HISTORIA.md` |
| Arma única | **Chave do Sistema** (espada) — no pós-jogo: abre os **Andares do Eco** (101+) e a arma fica mais forte a cada 10 andares do Eco |
| Troféu | A Primeira Janela (uma janela azul pequena para a casa, que mostra as tuas estatísticas) |
| Título | *Conquistador da Torre* |
