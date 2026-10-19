# Guião — Capítulo 7: Vulcão (andares 61–70)

Missões: **H_16 O Regresso do Kai**, **H_17 🔀 O Duelo** (= R7_11), **H_18 O Coração do Vulcão**. Povoações e missões
secundárias: `docs/dialogos/povoacoes_r07.md`. Mapas: `docs/mapas/r07_vulcao.md`.

**O que este capítulo conta**: o Kai **volta**, mas com os olhos azuis. Aceitou um acordo com o Sistema: "quem
chegar primeiro ao topo vai para casa". O Sistema obriga os dois a lutar no andar 68. Se o herói for amigo do Kai (6+ ❤️)
e se lembrar das promessas certas, **salva-o**; senão, **vence-o** e o Kai desaparece até ao fim. É a segunda grande
escolha do jogo. Na Forja Infernal, o herói encontra uma arma **com o seu número**.

**Flags deste capítulo**: `kai_voltou` (C7-02), `arma_10000` (C7-04), `kai_salvo` **ou** `kai_vencido` (C7-06).
O duelo usa as flags `kai_promessa_1`, `kai_promessa_2`, `kai_luar` e `kai_sem_ti` (ver `docs/dialogos/kai.md`).

---

## C7-01 — As Cinzas

| | |
|---|---|
| ID | `cena_c7_01_cinzas` |
| Quando | entrar pela primeira vez no andar 61 |
| Onde | andar 61, Mar de Cinza → Acampamento das Cinzas |
| Quem | herói, Mãe Brasa, crianças refugiadas |
| Música | `cinzas` |

🎥 A escada de luz abre-se numa planície cinzenta. Cai cinza do céu, devagar, como neve escura. Ao fundo, um vulcão enorme a fumegar.
🎬 O herói tosse. Limpa a cara. Fica com a mão preta.
- `[Sistema] Aviso: calor. Barra de Calor ativa.`
- `tut_calor`: `[Sistema] Calor: perto da lava a barra sobe. Bebe água ou Poção Fresca.`
🎬 Ao longe, uma fogueira grande e tendas cinzentas. Crianças a fazer "bonecos de cinza" como se fosse neve.
🎬 Uma mulher larga, de lenço na cabeça e mãos negras de carvão, vem ao encontro do herói com um cantil.
- **Mãe Brasa** *(normal)*: "Bebe. Aqui a primeira regra é beber. A segunda é não perguntar pelo que ardeu."
- **Mãe Brasa** *(triste)*: "A nossa cidade era ali, onde agora está o vulcão. Uma manhã, a torre engoliu-nos. A terra abriu-se. O fogo subiu. Os que correram mais depressa estão aqui."
- **Mãe Brasa** *(normal)*: "Somos poucos. Mas ainda há sementes. Ainda há crianças. Ainda há fogueira para aquecer, que é a coisa mais estúpida de se dizer num vulcão."

⚙ Desbloqueia o **Acampamento das Cinzas** (tenda, cristal, loja básica). Missões R7_01, R7_02, R7_15 disponíveis.

---

## C7-02 — Olhos Azuis

| | |
|---|---|
| ID | `cena_c7_02_regresso` |
| Quando | 1.ª noite no Acampamento das Cinzas (andar 61), depois da C7-01 |
| Onde | andar 61, beira do acampamento, à noite |
| Quem | herói, Kai, Mãe Brasa (ao longe) |
| Música | `cinzas` (versão noturna) → `duelo_kai` (só a introdução) |

🎬 Noite. A fogueira do acampamento ao fundo. Na escuridão da planície, uma figura sentada numa rocha, de costas, de casaco azul coberto de cinza.
🎬 O herói aproxima-se. A figura não se vira.
- **Kai** *(normal)*: "Sabia que vinhas. O Sistema diz-me sempre onde estás. É útil. É horrível."
- 🎬 Vira-se. Os olhos do Kai **brilham azul**, da cor exata da janela do Sistema. Tem uma armadura escura nova, sem riscos, sem nada.
- **Kai** *(normal)*: "Não faças essa cara. Estou bem. Nunca estive tão bem. Não durmo, não tenho fome, não tenho frio."
- **Kai** *(sério)*: "No navio, o Sistema falou comigo. Ofereceu-me um acordo. **Quem chegar primeiro ao topo vai para casa.** Eu aceitei."
- **Kai** *(sério)*: "Deu-me isto. A armadura. A velocidade. Os olhos. Diz que é para eu não perder tempo."

▶ **"Isso é uma armadilha, Kai."**
▶ **"E eu? Fico cá?"**
▶ **"A Yui ia ter medo de ti agora."** (só com `kai_promessa_1`)

- *(armadilha)* **Kai** *(zangado)*: "Toda a gente diz isso! A Lyra diria isso! O Fausto escreveria um livro sobre isso! E se não for?! E se for verdade e eu não aceitei?!"
- *(e eu)* **Kai** *(triste)*: 🎬 os olhos piscam, por um segundo castanhos. "…Tu chegas depois. Tu tens tempo. Tu não tens ninguém à espera." 🎬 os olhos voltam a azul. "Desculpa. Isso foi mau. É verdade, mas foi mau."
- *(Yui)* **Kai** *(zangado)*: "NÃO." 🎬 levanta-se de repente. Treme. "Não digas o nome dela com essa voz." ⚙ conta como uma lembrança para o duelo (não muda nada agora)
- **Kai** *(normal)*: "Não me sigas. A sério. Vou à frente. Se me apanhares… o Sistema diz que só um passa."
- 🎬 Um flash azul. O Kai desaparece. Fica a marca dos pés dele na cinza, e depois nem isso.
- `[Sistema] Jogador nº 9 999: localização confidencial.`

⚙ Missão **H_16 O Regresso do Kai** ativa. `[Sistema] Missão: segue o Kai.` Flag `kai_voltou`. O Kai entra na **fase C** (`docs/dialogos/kai.md`: aparece ao longe nas Zonas Seguras dos andares 61–67).
⚙ Na Guilda, a **Lyra** risca "em missão" e escreve "voltou". Depois apaga. Fala `lyra_kai_voltou`: "Voltou mas não voltou. Como é que se escreve isso num registo?"

---

## C7-03 — O Clã Brasa

| | |
|---|---|
| ID | `cena_c7_03_bastiao` |
| Quando | entrar pela primeira vez no Bastião de Obsidiana (andar 64) |
| Onde | andar 64, portão do Bastião → salão do clã |
| Quem | herói, Rainha-Forja Hildur, Mestre Ragnar |
| Música | `bastiao_brasa` |

🎬 Um portão de vidro negro escavado na montanha. Lá dentro, salões de obsidiana a brilhar à luz da lava canalizada. Anões de barbas trançadas a martelar.
🎬 Um anão enorme, de barba ruiva trançada com contas de rubi, para de martelar. Olha para o herói. Cheira-o.
- **Mestre Ragnar** *(desconfiado)*: "Hmpf. Cheiras a forja. A forja de baixo. A Martelo-Forte." 🎬 *(feliz)* "AH! Conheces o meu sobrinho! O pequeno Brom!"
- **Mestre Ragnar** *(feliz)*: "Ele ainda faz aquela cara? Esta?" 🎬 faz uma careta exatamente igual à do Brom. "Ha! Faz! Claro que faz!"
- 🎬 Uma anã de coroa de obsidiana levanta-se do trono de pedra.
- **Rainha-Forja Hildur** *(normal)*: "Ragnar. Senta-te." 🎬 ele senta-se logo. "Descid{o/a}. O Clã Brasa forja aqui desde que a torre nos engoliu. Forjávamos para os primeiros Jogadores. Agora forjamos para quem paga e para quem merece."
- **Hildur** *(séria)*: "Passou por aqui um rapaz de olhos azuis há três dias. Não parou. Não comprou nada. Os nossos fornos apagaram-se quando ele passou. Todos ao mesmo tempo."

⚙ Desbloqueia o **Bastião de Obsidiana** (estalagem, cristal, loja, Forja de Obsidiana). Missões R7_03 (com a carta do Brom), R7_04, R7_05 disponíveis.

---

## C7-04 — O Que Forjou o Teu Número

| | |
|---|---|
| ID | `cena_c7_04_arma` |
| Quando | vencer o Ferreiro Infernal (andar 65) |
| Onde | andar 65, Arena-Forja |
| Quem | herói, Kai (no fim) |
| Música | `ferreiro_infernal` → silêncio → martelos mecânicos a parar um a um |

🎬 O Ferreiro cai sobre a própria bigorna. A fornalha do peito apaga-se. Os martelos mecânicos param, um a um.
- `[Sistema] Mini-boss derrotado: Ferreiro Infernal.`
- `[Sistema] Unidade de guarda 65: desativada.`
🎬 Atrás da bigorna maior, uma prateleira comprida cheia de armas por acabar. Cada uma com um número gravado no cabo. 9 962. 9 980. 9 997. 9 998.
🎬 O espaço do **9 999** está vazio: só o pó com a forma de uma espada.
🎬 Ao lado, a última: uma lâmina sem fio, sem punho, ainda negra da forja. No cabo: **10 000**.
- `[Sistema] Obtiveste: Arma Inacabada nº 10 000.`
🎬 Passos atrás do herói. O Kai está à entrada da arena, encostado à parede, com uma espada nova à cintura.
- **Kai** *(normal)*: "A minha já estava pronta. O Sistema mandou-a acabar mais depressa. Corta bem." 🎬 bate no cabo. "A tua não. Ainda bem. Não sei se ias gostar do que ela se ia tornar."
- **Kai** *(sério)*: "No 68 há uma plataforma no meio da cratera. O Sistema diz que é lá que decidimos. Só um passa para o 69."
- **Kai** *(triste)*: "Eu não queria que fosse assim. Juro que não queria. Mas quero mais ir para casa do que não querer isto."
- 🎬 Flash azul. Desaparece.

⚙ Missão **H_16** concluída. Flag `arma_10000`. A **Arma Inacabada nº 10 000** vai para o **Brom** acabar (`docs/dialogos/brom.md`).
⚙ Recompensas normais: **Martelo da Forja**, título *Mais Forte que o Ferro*, Bigorna Infernal.

---

## C7-05 — A Plataforma

| | |
|---|---|
| ID | `cena_c7_05_antes_duelo` |
| Quando | chegar à Plataforma do Duelo (andar 68) |
| Onde | andar 68, Cratera Interior |
| Quem | herói, Kai |
| Música | o magma a borbulhar → `duelo_kai` |

🎥 Dentro da cratera. Paredes de rocha a perder de vista. Um lago de magma que sobe e desce como uma respiração. No meio, uma plataforma redonda de pedra negra, ligada à margem por uma ponte estreita.
🎬 O Kai está no centro da plataforma, de costas, de espada na mão. A ponte atrás do herói **desfaz-se** quando ele pisa a plataforma.
- `[Sistema] Duelo obrigatório: Jogador nº 9 999 contra Jogador nº 10 000.`
- `[Sistema] Só um avança.`
- **Kai** *(zangado, olhos azuis)*: "Não me sigas mais. O Sistema prometeu: quem chegar primeiro ao topo vai para casa. E vou ser eu."
- **Kai** *(normal)*: "Não te contenhas. Eu não me vou conter. Se te contiveres, perdes. E eu não quero ganhar a alguém que não lutou."
- `[Sistema] Boss: Kai, Jogador nº 9 999.`

⚙ Luta (ver `docs/BOSSES.md`, secção 14). As **3 escolhas** aos 75%, 50% e 25% da vida dele estão em `docs/dialogos/kai.md` (R7_11).
- Durante a fase 4 (25–0%), entre ataques, o Kai **para e chora** 2 s. Não é uma abertura: é ele.
- *(se o herói morrer)* `[Sistema] Jogador nº 10 000: derrotado.` 🎬 O Kai olha para o herói no chão e grita: "Levanta-te! LEVANTA-TE! Não é assim! Não quero assim!" → o herói acorda na Zona Segura do 68 e a luta recomeça. (O Kai não avança sem a vitória.)

---

## C7-06A — Salvo

| | |
|---|---|
| ID | `cena_c7_06a_salvo` |
| Quando | duelo: 6+ ❤️ com o Kai e as 3 respostas certas |
| Onde | andar 68, Plataforma do Duelo |
| Quem | herói, Kai |
| Música | `duelo_kai` corta → silêncio → `tema_kai` (piano) |

🎬 Aos 25%, depois da terceira resposta certa, o Kai para a meio de um golpe. A espada treme. As janelas azuis à volta dele **racham** como vidro.
- `[Sistema] Erro.`
- `[Sistema] Jogador nº 9 999: ligação perdida.`
🎬 A armadura escura desfaz-se em pixels azuis que sobem como faúlhas. Os olhos do Kai voltam a ser castanhos. Ele cai de joelhos.
- **Kai** *(triste, a chorar)*: "Eu ia deixar-te para trás. Por uma porta que nem sei se existe."
- **Kai** *(triste)*: "Desculpa. Desculpa, desculpa."
- 🎬 O herói estende-lhe a mão.

▶ **"Voltamos os dois."**
▶ **"Anda. Vamos para Ascendia."**

- **Kai** *(feliz, a chorar)*: "…Pois. Os dois."
- 🎬 O Kai agarra a mão e levanta-se. Fica a olhar para a mão do herói.
- **Kai** *(normal)*: "Tens a mão quente. Há semanas que eu não sentia nada. Nem calor. Isto é… bom. Isto dói. É bom."
- 🎬 Do magma, à volta da plataforma, levanta-se uma ponte de rocha nova. O caminho para o 69 abre-se.
- **Kai** *(normal, a limpar a cara com a manga)*: "Não contes a ninguém que chorei. …Conta só à Mia. Ela vai gozar comigo. Mereço."
- `[Sistema] …`
- `[Sistema] Duelo terminado. Ambos avançam.` 🎬 *(a mensagem pisca, como se o Sistema não tivesse a certeza)*

⚙ Flag `kai_salvo` · **Amuleto da Amizade** · o Kai passa a **companheiro** · conta para o **final secreto**. Missão **H_17** concluída. O Kai entra na **fase D**.

## C7-06B — Vencido

| | |
|---|---|
| ID | `cena_c7_06b_vencido` |
| Quando | duelo: o Kai chega a 0% (sem as condições para o salvar) |
| Onde | andar 68, Plataforma do Duelo |
| Quem | herói, Kai |
| Música | `duelo_kai` acaba → só o magma |

🎬 O Kai cai de joelhos. A armadura escura desfaz-se em pixels azuis.
- **Kai** *(triste)*: "Perdi. Claro. Ganhas sempre, número redondo."
- **Kai** *(triste)*: "Diz à Yui… não. Não lhe podes dizer nada. Ela não te conhece."
- **Kai** *(normal, a sorrir um bocadinho)*: "Sobe. Já que ganhaste… ao menos chega lá acima. Pergunta-lhe porquê. Por mim."
- `[Sistema] Jogador nº 9 999: retirado do registo.`
- 🎬 Luz azul. O Kai desaparece. Fica só a espada dele no chão da plataforma.
- `[Sistema] Duelo terminado. Jogador nº 10 000 avança.`
- 🎬 Uma ponte de rocha nova sobe do magma. O herói fica muito tempo parado antes de pegar na espada.

⚙ Flag `kai_vencido` · **Lâmina do Kai** · o Kai só volta no **andar 100** (como parte do final). Missão **H_17** concluída. O Kai entra na **fase E**.

---

## C7-07 — A Parede dos Nomes

| | |
|---|---|
| ID | `cena_c7_07_nomes` |
| Quando | entrar nas Câmaras dos Votos (andar 69) |
| Onde | andar 69, Câmaras dos Votos |
| Quem | herói (e o Kai, se `kai_salvo` e estiver na equipa) |
| Música | `cinzas` (versão de templo) |

🎬 Uma câmara alta. Uma parede inteira coberta de **nomes** riscados na rocha, com letras de muitos tamanhos. Não estão na escrita azul da pirâmide: estão em letras normais, de gente.
🎬 Alguns nomes têm números ao lado. "Edrik 9 961." "Odília." "Teo." "Ilsa ☆". *(a equipa do Gorvan passou aqui)*
🎬 O último nome da parede é recente. Riscado com uma espada: **"KAI 9 999 — PRIMEIRO."**
- *(com o Kai salvo, na equipa)* **Kai** *(envergonhado)*: "Escrevi isso há duas semanas. Parece outra pessoa. Era outra pessoa." 🎬 Pega na espada e risca o "PRIMEIRO". Escreve por baixo: "E O 10 000. OS DOIS." ⚙ +50 Kai
- *(sem o Kai)* 🎬 O herói fica a olhar para o nome. Pode escrever o seu ao lado ([interagir] → *escrever o nome*). Se escrever: aparece **"{nome} 10 000"** riscado ao lado do do Kai.

⚙ Sem missão. Se viste os nomes da equipa do Gorvan (`missao(H_12) == concluida`), o Diário → Pessoas acrescenta: *"Passaram pelo andar 69."*

---

## C7-08 — O Coração do Vulcão

| | |
|---|---|
| ID | `cena_c7_08_tita` |
| Quando | entrar n'O Coração (andar 70) / vencer o Titã |
| Onde | andar 70, poço de magma |
| Quem | herói (e o Kai, se estiver na equipa), Titã de Magma |
| Música | `tita_magma` → silêncio → um suspiro enorme |

**Antes**
🎬 Um poço de magma gigante. Ilhas de rocha a flutuar. O magma sobe em bolhas. Depois sobe uma cabeça de pedra negra com uma coroa de chamas e olhos brancos.
- `[Sistema] Boss: Titã de Magma, O Coração do Vulcão.`
- *(com o Kai)* **Kai** *(normal)*: "Grande. Muito grande. Eu fico com o braço esquerdo. Tu com o direito. Quem chegar primeiro à cabeça paga o jantar." 🎬 pausa. "…Desculpa. 'Primeiro.' Hábito."

**Depois**
🎬 O Titã afunda-se devagar no magma. Não morre: fecha os olhos. As fendas de lava do corpo dele apagam-se uma a uma. O magma do poço baixa e escurece. Toda a montanha **suspira**: um som enorme, comprido, como alguém a adormecer.
- `[Sistema] Boss derrotado: Titã de Magma.`
- `[Sistema] Obtiveste: Coração de Magma.`
- `[Sistema] Título obtido: Mais Quente que a Lava.`
- `[Sistema] Região 7 concluída. Andar 71 desbloqueado.`
- `[Sistema] O vulcão adormeceu.`

⚙ Missão **H_18** concluída. O Calor dos andares 61–69 passa a subir metade. A página 70 está na ilha onde o Titã afundou.

---

## C7-09 — Dia da Subida: O Nome da Canção

| | |
|---|---|
| ID | `cena_c7_09_dia_subida` |
| Quando | voltar a Ascendia depois do Titã |
| Onde | Praça da Torre (Dia da Subida, F_05) |
| Quem | herói, Aldric, Lucien, Lyra, Mia, Dona Marta, Gorvan, (Kai se `kai_salvo`) |
| Música | `dia_da_subida` |

### Se `kai_salvo`
🎬 A Praça cheia. A estátua nova é um titã de pedra com uma coroa de papel vermelho.
🎬 O Kai está ao lado do herói, com o capuz posto, a tentar ser invisível. Não resulta.
- **Mia** *(a correr, aos gritos)*: "KAI! KAI VOLTOU! O KAI CHOROU, EU SEI QUE CHOROU, TEM A CARA TODA INCHADA!" 🎬 atira-se a ele. O Kai cai.
- **Kai** *(envergonhado)*: "…Olá, Mia. Também tive saudades. Sai de cima de mim."
- 🎬 A Lyra chega com o registo da Guilda debaixo do braço. Abre-o à frente de toda a gente. Risca "desaparecido". Escreve "**voltou**" em letras enormes.
- **Lyra** *(feliz, a chorar)*: "Pronto. Agora é verdade."
- 🎬 A Dona Marta não diz nada. Dá-lhe uma palmada na cabeça e depois um abraço que dura muito tempo.
- **Dona Marta** *(feliz)*: "O teu quarto está feito. Com a janela aberta. Vai fechá-la."
- 🎬 O Gorvan passa, para, olha para o Kai de cima a baixo.
- **Gorvan** *(normal)*: "Hmm. Voltaste." 🎬 pausa. "Bem." 🎬 continua a andar.
- **Lucien** *(do palco)*: "A canção que não tinha nome… agora tem. Chama-se **'O Regresso'**. É a mesma música. Mas agora tem letra."
- 🎵 ♪ *Partiu de noite e voltou de dia, com os olhos de quem chorou… e a cidade, que não dormia, fez-lhe a cama e se calou…* ♪
- **Kai** *(baixinho, para o herói)*: "Se contares a alguém que esta canção me fez chorar outra vez, nego tudo."

### Se `kai_vencido`
🎬 A Praça tem festa, mas o lugar ao pé da fonte está vazio. A Lyra pendura a espada do Kai num prego na parede da Guilda.
- **Lyra** *(triste)*: "Não escrevo 'morto'. Não morreu, pois não? Desapareceu. A luz levou-o. Escrevo 'à espera'."
- **Mia** *(zangada, a chorar)*: "Tu é que ganhaste! Porque é que não o trouxeste?!" 🎬 foge. (No dia seguinte pede desculpa à maneira dela: fala `mia_boss_kai_vencido`, com uma flor.)
- **Lucien** *(do palco)*: "A canção sem nome continua sem nome. Fica assim até ele voltar."
- **Gorvan** *(normal, ao herói, sem olhar)*: "Fizeste o que tinhas de fazer. Isso não quer dizer que esteja bem. Quer dizer que está feito."

⚙ `[Sistema] Capítulo 8: O Reino Assombrado.` (título grande no ecrã)
