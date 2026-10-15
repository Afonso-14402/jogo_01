# Guião — Capítulo 10: Abismo (andares 91–100)

Missões: **H_22 O Último Posto**, **H_23 Os Perdidos**, **H_24 O Diário de A.**, **H_25 A Escada Final**,
**H_26 O Administrador**. Povoações e missões secundárias: `docs/dialogos/povoacoes_r10.md`. Mapas:
`docs/mapas/r10_abismo.md`. A escolha final, os 4 finais e os epílogos: `docs/guiao/finais.md`.

**O que este capítulo conta**: acaba a torre que se vê e começa a torre **por dentro**. O Sistema falha cada vez
mais e fala cada vez mais como uma pessoa. Na **Cidade dos Perdidos** vivem os Jogadores que desistiram; a torre
mostra ao herói o **quarto dele** do mundo real, para o convencer a ficar. Na **Biblioteca do Mundo**, a Arquivista
junta o diário e diz o nome: **Aren**. No topo há um jardim igual ao Prado do Despertar, e um homem cansado sentado
na relva.

**Flags deste capítulo**: `posto_ativo` (C10-02), `viu_quarto` (C10-08), `desistente_ouvido` (C10-09),
`relogio_anda` (C10-10), `sabe_nome_aren` (C10-12), `ouviu_sem_numero` (C10-13), `ponto_sem_retorno` (C10-14).
Contador: `perdidos_convencidos` (0 a 5, missão R10_07).

**O Sistema neste capítulo**: as mensagens normais aparecem com **falhas** (`docs/textos/sistema.md`, secção
"Falhas"): `[Sisetma]`, números errados, janelas que abrem duas vezes. As mensagens que contam a história aparecem
**sem falhas nenhumas**, limpas: é assim que o jogador atento percebe que é outra pessoa a escrever.

---

## C10-01 — A Torre Por Dentro

| | |
|---|---|
| ID | `cena_c10_01_vazio` |
| Quando | entrar pela primeira vez no andar 91 |
| Onde | andar 91, ilha de chegada → Último Posto (abandonado) |
| Quem | herói (e o companheiro) |
| Música | silêncio → `vazio` |

🎥 A escada de luz acaba numa ilha de pedra a flutuar no escuro total. Não há céu, não há chão: só pontos de luz muito longe, como estrelas, e um frio sem vento.
🎬 O herói dá um passo e a luz da escada apaga-se atrás dele. Só se vê um círculo de 3 m à volta dos pés.
- `[Sisetma] Bem-vindo ao andar 19.`
🎬 A janela pisca e corrige-se sozinha.
- `[Sistema] Bem-vindo ao andar 91.`
- `tut_vazio`: `[Sistema] Fora da luz não se vê nada. Acende as âncoras para tornar o caminho seguro.`
🎬 Ao fundo, tendas rasgadas, uma fogueira apagada há muito tempo, uma bandeira da Guilda desbotada.
- *(com o Kai)* **Kai** *(baixinho)*: "Isto é um acampamento da Guilda. Olha a bandeira." 🎬 toca na tenda; desfaz-se em pó. "Há quanto tempo é que ninguém chega aqui?"
- *(com o Gorvan)* **Gorvan** *(normal)*: "O Último Posto. Ouvi falar dele quando era novo. A expedição do Capitão Orsi. Sessenta anos. Ninguém voltou." 🎬 pausa. "Ninguém subiu tanto, depois. Nem eu."
🎬 Num poste, uma âncora de luz apagada: um globo de vidro com uma estrela pequenina lá dentro, a dormir.

⚙ Missão **H_22** ativa. `[Sistema] Missão: acende as âncoras de luz (0/5).` (= R10_01)

---

## C10-02 — O Último Posto

| | |
|---|---|
| ID | `cena_c10_02_posto` |
| Quando | acender a 5.ª âncora do andar 91 (R10_01) |
| Onde | andar 91, Último Posto |
| Quem | herói (e o companheiro), Sargento Bruma, Dorn, Tibério, aventureiros da Guilda; Kai (se `kai_salvo` e não estiver na equipa) |
| Música | `vazio` → `ascendia` (versão pequena, só flauta) |

🎬 A última âncora acende-se. As cinco ficam ligadas por fios de luz e o escuro recua: o Último Posto aparece inteiro, com tendas, uma forja de pedra e um cristal partido.
🎬 Ouve-se um "plim" do cristal. Ele brilha e reconstrói-se. Do cristal saem, um a um, aventureiros da Guilda com mochilas enormes.
🎬 À frente vem uma mulher de cabelo grisalho curto e cicatriz no queixo, com um machado às costas.
- **Sargento Bruma** *(séria)*: "Jogador{/a} nº 10 000. Sargento Bruma, da Guilda. A Capitã Freya mandou-nos assim que o cristal piscou lá em baixo."
- **Sargento Bruma** *(normal)*: "Sessenta anos à espera que alguém acendesse isto. O meu avô era da expedição do Orsi. Eu prometi que subia se alguém abrisse o caminho."
- **Sargento Bruma** *(feliz, só um bocadinho)*: "Abriste. Agora é a nossa vez. Montamos o posto. Tu descansas."
🎬 Atrás dela, o Tibério aparece com a mochila de sempre, sem fôlego.
- **Tibério** *(feliz)*: "Cheguei! Cheguei antes da loja do andar 90 fechar? Não interessa. Cheguei. Loja aberta!"
🎬 Um homem grande, cego de um olho, pousa uma bigorna no chão como quem pousa um saco de batatas.
- **Dorn** *(normal)*: "Dorn. Ferreiro. Ando de forja em forja há trinta anos à espera de metal que valha a pena. Diz-me que lá para cima há estrelas para martelar."
- *(se `kai_salvo` e o Kai não estiver na equipa)* 🎬 O Kai sai do cristal a correr, com a espada já na mão.
  - **Kai** *(feliz)*: "Não me deixaste para trás! Quer dizer, deixaste. Mas eu vim. Vou ficar aqui. Treino contigo sempre que quiseres."

⚙ Missão **H_22** concluída. Flag `posto_ativo`. Desbloqueia o **Último Posto** (cama, cristal, loja do Tibério). Missões R10_02 e R10_05 disponíveis.
⚙ Ao encontrar a **ilha invisível** do fim da Ponte para o Nada (segredo), lê-se a **mensagem da expedição**: *"Dia 41. O Orsi saltou para o escuro para ver se havia chão. Havia. Voltou a rir. Amanhã subimos. Se alguém ler isto: o escuro tem chão. Só é preciso coragem para o pisar."* (A Bruma tem uma fala nova: `bruma_orsi`.)

---

## C10-03 — Um Planeta Azul

| | |
|---|---|
| ID | `cena_c10_03_planeta` |
| Quando | chegar pela primeira vez a uma borda do Caminho de Estrelas (andar 92) |
| Onde | andar 92, Caminho de Estrelas |
| Quem | herói (e o companheiro) |
| Música | `mar_de_estrelas` |

🎥 O herói anda por cima de um caminho de estrelas. Por baixo dos pés não há nada: só espaço, nebulosas cor-de-rosa e roxas, cometas a passar devagar.
🎥 Lá em baixo, muito longe, um **planeta azul** com nuvens brancas. A câmara aproxima-se devagar. Mares, continentes. Parece…
🎬 O herói ajoelha-se na borda do caminho e fica a olhar.
🎥 A câmara aproxima-se mais. Os continentes têm as formas erradas. Não é. É parecido, mas não é.
- `[Sistema] …`
- *(com o Kai)* **Kai** *(triste)*: "Por um segundo achei que era. Juro que achei." 🎬 senta-se ao lado do herói. "A Yui adorava planetas. Tinha um candeeiro com o sistema solar no teto."
- *(com o Gorvan)* **Gorvan** *(normal)*: "É o teu?" 🎬 o herói abana a cabeça. "Hmm. Então ainda está à tua espera noutro sítio. É melhor assim. Os que estão à espera estão inteiros."
- *(com a Nina)* **Nina** *(normal)*: "Não é o nosso. Eu já vim aqui chorar uma vez. Não vale a pena. Anda."

⚙ Sem missão. O planeta azul fica no fundo do andar 92 para sempre (e muda, depois do final 4: ver `finais.md`).

---

## C10-04 — Os Espelhos

| | |
|---|---|
| ID | `cena_c10_04_espelhos` |
| Quando | entrar na **Sala dos Mil Reflexos** (andar 93) |
| Onde | andar 93, Sala dos Mil Reflexos |
| Quem | herói (e o companheiro) |
| Música | `vazio` (com um eco a mais) |

🎬 Uma sala redonda, toda de espelhos de molduras douradas. Em todos, o herói. Mas não iguais.
🎥 A câmara passa de espelho em espelho:
- num, o herói mais velho, de cabelo branco, sentado num trono simples, com uma coroa de luz azul. Olha para baixo, cansado;
- noutro, o herói no **quarto dele**, a dormir, com o despertador a tocar;
- noutro, o herói em Ascendia, à mesa da Estalagem, com a Dona Marta a pôr-lhe mais um prato;
- noutro, o herói a lutar contra o Kai, no andar 68, e a perder;
- num espelho partido, só escuro.
🎬 O herói para à frente do espelho do quarto. Estende a mão. O vidro está frio.
▶ **Tocar no espelho do quarto**
▶ **Tocar no espelho do trono**
▶ **Não olhar mais** *(virar as costas)*

- *(quarto)* 🎬 O reflexo acorda, olha para o herói e diz qualquer coisa sem som. Depois o espelho escurece. `[Sistema] Lembras-te da cor da tua casa?`
- *(trono)* 🎬 O reflexo de cabelo branco levanta os olhos e sorri, muito cansado. Depois o espelho escurece. `[Sistema] Ainda não.`
- *(não olhar)* 🎬 O herói vira as costas. Todos os espelhos escurecem ao mesmo tempo. `[Sistema] …` *(sem falhas)*
- *(com o Kai)* **Kai** *(sério)*: "Eu vi um em que eu ganhava. No 68. Não gostei de mim nesse." 🎬 pausa. "Vamos sair daqui."

⚙ Sem missão. A escolha não muda o final; muda uma fala do Administrador (C10-15: `espelho_quarto`, `espelho_trono` ou `espelho_nenhum`).

---

## C10-05 — A Torre Lembra-se

| | |
|---|---|
| ID | `cena_c10_05_ecos` |
| Quando | entrar pela primeira vez no andar 94 |
| Onde | andar 94, chegada (à vista dos 10 Pedaços) |
| Quem | herói (e o companheiro) |
| Música | `ecos` (um bocadinho de cada música das regiões, todas juntas e fora de tempo) |

🎥 No escuro, dez pedaços de mundo a flutuar: um bocado da floresta do andar 1 com a Árvore-Mãe pequenina; um pedaço de gruta com cristais; o pântano; uma duna com a ponta da pirâmide; um bloco de gelo com o castelo; uma bolha de mar; uma ilha de lava; uma torre do reino; uma nuvem com uma cúpula azul. E um décimo pedaço, apagado.
🎬 O herói vê, no pedaço da floresta, um **Slime** igualzinho ao primeiro que matou. Mas roxo-escuro. Ele salta. Para. Volta a saltar duas vezes no mesmo sítio, como um disco riscado.
- *(com o Kai)* **Kai** *(normal)*: "É tudo o que passámos. Em pedacinhos. Como um álbum de fotografias estragado."
- *(com o Gorvan)* **Gorvan** *(triste)*: 🎬 olha para o pedaço do reino assombrado durante muito tempo. "Não vou lá. Já lá fui. Chega."
- *(sem companheiro)* `[Sistema] A torre lembra-se de tudo o que comeu.` *(sem falhas)*

⚙ Sem missão. O décimo pedaço (apagado) é o **Centro**: acende-se com o puzzle da ordem da subida.

---

## C10-06 — O Que Te Viu Mil Vezes

| | |
|---|---|
| ID | `cena_c10_06_tempo` |
| Quando | entrar na Arena das Engrenagens (andar 95) e, depois, vencer o Guardião do Tempo |
| Onde | andar 95, Arena das Engrenagens |
| Quem | herói (e o companheiro), Guardião do Tempo |
| Música | tique-taque → `guardiao_do_tempo` |

**Antes da luta**
🎬 Engrenagens gigantes rodam no chão. No meio, uma figura alta de bronze com um relógio no lugar da cara. Quatro braços: dois ponteiros como espadas, uma ampulheta, um pêndulo.
- **Guardião do Tempo** *(normal, cada palavra a cair com um tique)*: "Ah. Tu. Outra vez."
- **Guardião do Tempo** *(normal)*: "Já te vi passar aqui mil vezes. Mil caras, mil números, a mesma vontade: ir para casa. Para mim és sempre o mesmo. Para ti é sempre a primeira vez."
- **Guardião do Tempo** *(normal)*: "Houve um, há muito, que se sentou aqui no chão e chorou uma tarde inteira. Depois levantou-se e subiu. Eu deixei. Ele voltou a passar mil vezes, sempre a subir, nos olhos dos outros."
- `[Sistema] Mini-boss: Guardião do Tempo, O Que Te Viu Mil Vezes.`

**Depois da luta**
🎬 O Guardião ajoelha-se. Os ponteiros da cara param às doze.
- **Guardião do Tempo** *(normal)*: "Interessante. Desta vez parti-me eu."
- **Guardião do Tempo** *(normal)*: "Vai. E quando chegares lá acima, diz-lhe que o tempo ainda anda. Ele acha que parou. Não parou. Só anda devagar para quem está sozinho."
- 🎬 Desfaz-se em areia dourada, que cai **para cima** e fica a flutuar.
- `[Sistema] Mini-boss derrotado: Guardião do Tempo.`
- `[Sistema] Unidade de guarda 95: desativada.`
- `[Sistema] Obtiveste: Segundo Parado.`

⚙ Sem missão de história. A **Flor do Tempo** (R10_06) fica disponível.

---

## C10-07 — A Cidade dos Perdidos

| | |
|---|---|
| ID | `cena_c10_07_perdidos` |
| Quando | entrar pela primeira vez no andar 97 |
| Onde | andar 97, Portão dos Perdidos → Praça do Desistir |
| Quem | herói (e o companheiro), "Mãe Dois", Perdidos |
| Música | `cidade_dos_perdidos` |

🎥 Uma cidade cinzenta. Casas todas iguais, de porta azul-desbotada, cada uma com um **número** pintado: 3 412, 6 080, 1 777… As janelas têm cortinas. As ruas estão limpas e vazias.
🎬 Algumas cortinas mexem-se. Caras espreitam e escondem-se.
🎬 Na praça, um relógio grande **sem ponteiros**. Por baixo dele, sentada numa cadeira de baloiço, uma velha pequenina de casaco de malha e óculos grossos, a tricotar uma coisa muito comprida.
- **"Mãe Dois"** *(feliz)*: "Ora, uma cara nova. Senta-te, senta-te. Chamam-me Mãe Dois. Sou a nº 2 048. A mais velha da cidade."
- **"Mãe Dois"** *(normal)*: "Isto é a cidade de quem parou. Ninguém te vai obrigar a nada aqui. É a única regra. A janela azul cala-se cá dentro."
- 🎬 O herói olha para cima. A janela do Sistema, que andou sempre por perto, não está lá.
- **"Mãe Dois"** *(normal)*: "Vês? Silêncio. É por isso que ficam. Uns chegaram ao 97 e sentaram-se. Outros vieram pelos atalhos que a torre lhes abriu quando choraram muito. A torre é boa a abrir atalhos para quem chora."
- **"Mãe Dois"** *(triste)*: "Eu cheguei há… perdi a conta. Tricoto um cachecol desde o primeiro dia. Uma volta por dia. Já dá a volta à praça três vezes."
- **"Mãe Dois"** *(normal)*: "Não te vou pedir para ficares. Vou pedir-te outra coisa: há aqui gente que não ficou por gosto. Ficou por medo. Se conseguires falar com eles… talvez alguns voltem a subir contigo."

▶ **"Vou tentar."**
▶ **"E tu? Não queres voltar a subir?"**

- *(tentar)* **"Mãe Dois"** *(feliz)*: "Boa. Não os puxes. Ouve-os. Os puxados voltam a sentar-se."
- *(e tu)* **"Mãe Dois"** *(normal)*: "Eu? Tenho noventa e tal anos, filh{o/a}. As minhas pernas desistiram antes de mim. Mas vou contigo até à praça, no dia. Para ver."
- *(com o Kai)* **Kai** *(baixinho)*: "Se tu não me tivesses ido buscar ao 68… era aqui que eu estava. Numa casa com o 9 999 na porta."

⚙ Missão **H_23** ativa (= R10_07). `[Sistema]` não aparece: a missão é anotada no Diário à mão, com a letra do herói.
⚙ Desbloqueia a **Cidade dos Perdidos** (casa vazia para dormir, cristal, Mercado das Memórias).

---

## C10-08 — O Quarto

| | |
|---|---|
| ID | `cena_c10_08_quarto` |
| Quando | abrir a porta da **casa sem número** (Bairro dos Números, andar 97) |
| Onde | andar 97, casa sem número |
| Quem | herói (sozinho: os companheiros ficam à porta) |
| Música | silêncio; depois o som de chuva numa janela e um carro a passar ao longe |

🎬 A porta não tem número. Abre-se sozinha. O companheiro tenta entrar e não consegue: o ar da porta é sólido para ele.
🎥 Lá dentro, o **quarto do herói**. O do mundo real. A cama por fazer, a secretária com cadernos da escola, um carregador de telemóvel pendurado da tomada, um poster meio descolado, roupa em cima da cadeira. A luz é de fim de tarde. Lá fora, pela janela, chove numa rua normal.
🎬 O herói anda devagar. Toca na cama. É macia. Abre a gaveta da secretária: há um desenho velho, de criança, de uma torre.
🎬 Em cima da almofada, um despertador. Está parado às **7:00**.
🎥 Close no despertador. Os ponteiros tremem, como se quisessem andar.
- `[Sistema] Podes ficar aqui. É igual. Ninguém te vai obrigar a subir.` *(sem falhas, letra limpa)*
- `[Sistema] Ficas?`

▶ **Deitar na cama** *(ficar)*
▶ **Sair do quarto**

- *(deitar)* 🎬 O herói deita-se. O quarto é quentinho. A chuva lá fora é bonita. A câmara afasta-se… e a imagem **falha**: quadrados coloridos, a parede mostra pedra cinzenta por baixo do papel. O despertador começa a tocar sozinho, muito alto. O herói acorda, sobressaltad{o/a}, na casa cinzenta, sem móveis, deitad{o/a} no chão de pedra.
  - `[Sistema] …`
  - `[Sistema] Desculpa. Isto não fui eu.` *(sem falhas; desaparece logo)*
- *(sair)* 🎬 O herói olha uma última vez e sai. A porta fecha-se. Por dentro, ouve-se o despertador começar a tocar.
- 🎬 Cá fora, o companheiro está à porta, preocupado. A "Mãe Dois" está ao fundo da rua, encostada à bengala.
- **"Mãe Dois"** *(triste)*: "Mostrou-te o teu quarto, não foi? Mostra a toda a gente. A mim mostrou a cozinha da minha mãe, com bolo no forno."
- **"Mãe Dois"** *(normal)*: "A torre lê-nos as memórias. Faz casas com elas. Para ficarmos. Metade desta cidade entrou numa casa sem número e nunca mais saiu de casa."
- **"Mãe Dois"** *(normal)*: "Tu saíste. Isso diz muito."

⚙ Flag `viu_quarto`. No Diário (nota do herói): *"Havia um quarto igual ao meu. Era mentira. Mas era bonito."* Fala nova do Administrador (C10-15).

---

## C10-09 — O Desistente

| | |
|---|---|
| ID | `cena_c10_09_desistente` |
| Quando | entrar no Portão dos Perdidos pelo lado de dentro (saída da cidade) e, depois, vencer O Desistente |
| Onde | andar 97, Portão dos Perdidos |
| Quem | herói (e o companheiro), O Desistente (Jogador nº 7 777) |
| Música | `cidade_dos_perdidos` → `boss` (versão cansada, mais lenta) |

**Antes da luta**
🎬 À saída da cidade, sentado num caixote à frente do portão, um homem de armadura velha e amolgada. Às costas, muitas armas: uma espada, um arco, uma lança, um martelo, uma adaga. Nenhuma está limpa.
- **O Desistente** *(normal, sem se levantar)*: "Nº 7 777. Dizem que é um número com sorte." 🎬 ri-se sem vontade. "Cheguei aqui há quarenta anos. Sentei-me para descansar cinco minutos."
- **O Desistente** *(normal)*: "Agora guardo o portão. Ninguém mandou. Fui eu que decidi. Quem quer sair da cidade, passa por mim. Para eu ver se vale a pena."
- **O Desistente** *(zangado, a levantar-se)*: "Para quê subir? Diz-me tu. Lá em cima está um homem cansado à espera de outro para ficar tão cansado como ele. É isso que queres?"
- `[Sistema] Guardião: O Desistente, Jogador nº 7 777.`

**Durante a luta** (uma fala por fase, quando troca de arma)
- *(espada)* "Eu era bom com esta. O melhor da minha Guilda."
- *(arco)* "Havia uma rapariga que me ensinou. Ficou no 60. Eu continuei. Para quê?"
- *(martelo)* "Bate mais forte! Se vais subir, sobe com vontade!"
- *(adaga, já sem força)* "Para. Para, por favor. Eu… eu já não quero."

**Depois da luta**
🎬 O Desistente larga as armas todas no chão. Senta-se outra vez no caixote. Tira o elmo. É um homem de meia-idade com cara de quem não dorme.
- **O Desistente** *(triste)*: "Quarenta anos. Sabes o que é pior? Não é o cansaço. É saber que, se me tivesse levantado no dia seguinte, tinha chegado ao topo antes de ti."
- **O Desistente** *(normal)*: "Não vou subir. Já é tarde para mim. Mas…" 🎬 olha para a cidade. "Há gente aqui que ainda vai a tempo. Eu conheço-os a todos. Sei o que os prende. Deixa-me ajudar-te a falar com eles."

▶ **"Anda connosco."**
▶ **"Obrigad{o/a}."**

- *(anda)* **O Desistente** *(feliz, pela primeira vez)*: "Ha. Não. Mas obrigado por perguntares. Há quarenta anos que ninguém pergunta."
- *(obrigado)* **O Desistente** *(normal)*: "Não agradeças. Ainda não fiz nada. É o costume."
- `[Sistema] Guardião derrotado: O Desistente.` *(o Sistema escreve isto com uma falha: `Guardião derortado`)*
- `[Sistema] Obtiveste: Arco do Desistente.`

⚙ Missão **R10_09** concluída. Flag `desistente_ouvido`. O Desistente passa a viver na praça e dá **pistas** para cada Perdido da R10_07 (`docs/dialogos/povoacoes_r10.md`). A escada para o andar 98 abre.

---

## C10-10 — A Cidade Ganha Cor

| | |
|---|---|
| ID | `cena_c10_10_relogio` |
| Quando | pôr os dois ponteiros no relógio da praça (puzzle do andar 97) |
| Onde | andar 97, Praça do Desistir |
| Quem | herói, "Mãe Dois", Rafa, Nina, os Perdidos (os convencidos à frente) |
| Música | tique-taque → `cidade_dos_perdidos` com cor (entra uma guitarra) |

🎬 O herói sobe ao relógio com os dois ponteiros: o grande (do Rafa) e o pequeno (da Nina). Encaixa-os. Nada.
🎬 Depois, um **tique**. E outro. Os ponteiros começam a andar.
🎥 A cor espalha-se a partir do relógio como tinta em água: as portas ficam azuis a sério, as flores das janelas ficam vermelhas e amarelas, as casas deixam de ser todas iguais.
🎬 As portas abrem-se. Os Perdidos saem para a rua e olham para cima, para o relógio, como se nunca o tivessem visto.
- **"Mãe Dois"** *(a chorar e a rir)*: "Está a andar. Olha, está a andar!" 🎬 larga as agulhas do tricô. "O tempo! Ai, o tempo!"
- **Rafa** *(feliz)*: "Isto pede música." 🎬 começa a tocar (com a guitarra nova, se R10_14 já está feita; senão, com uma guitarra de duas cordas).
- *(se `perdidos_convencidos` ≥ 1)* 🎬 Os Perdidos convencidos estão à frente, com mochilas. Acenam ao herói.
- *(se `perdidos_convencidos` = 5)* **"Mãe Dois"** *(normal)*: "Cinco. Cinco dos meus meninos vão subir. Nunca pensei ver isto." 🎬 tira o cachecol enorme do colo e enrola-o três vezes à volta do pescoço do herói. "Leva. Lá em cima faz frio. Faz sempre frio aos que estão sozinhos."

⚙ Flag `relogio_anda`. Desafio do andar cumprido. Com 5 Perdidos: item **Cachecol da Mãe Dois** (acessório: imune a Frio e Congelamento; +1 coração a todos os NPCs no próximo presente).

---

## C10-11 — A Arquivista

| | |
|---|---|
| ID | `cena_c10_11_arquivista` |
| Quando | chegar à **Sala do Diário** (andar 98) pela primeira vez (depois de sair das escadas em ciclo) |
| Onde | andar 98, Sala do Diário |
| Quem | herói (e o companheiro), A Arquivista |
| Música | `vazio` com uma caixa de música muito baixinho |

🎥 Estantes que sobem e descem para sempre. Livros com luz azul nas lombadas. Escadas em espiral que voltam ao mesmo sítio.
🎬 O herói sai das escadas em ciclo seguindo a luz das páginas que traz no bolso: elas brilham quando ele vai pelo caminho certo.
🎬 Uma sala redonda, pequena, com uma mesa e uma cadeira. Na mesa, cem molduras vazias, em fila, como para fotografias.
🎬 Uma mulher sem idade, de óculos redondos e um vestido feito de páginas de livro, está a limpar o pó a uma moldura.
- **A Arquivista** *(normal)*: "Ah. As páginas. Ouvi-as chegar. Fazem barulho, sabes? Papel velho a querer voltar para casa."
- **A Arquivista** *(normal)*: "Sou a Arquivista. Guardo um livro de cada mundo que a torre comeu. Milhares. Lidos por mim. Só por mim. Até hoje."
- **A Arquivista** *(normal)*: 🎬 aponta para as molduras. "Estas são para um livro só. O de um rapaz. Esperei por ele muito tempo. Ele escreveu-o às pedaços e espalhou-o pela torre."
- *(se tiver menos de 90 páginas)* **A Arquivista** *(normal)*: "Trazes {paginas}. Não chega. Não consigo ler um livro com buracos tão grandes. Volta quando tiveres pelo menos noventa. Eu espero. É o que faço melhor."
  - ⚙ A missão **H_24** fica **opcional**. `[Sistema] Missão: O Diário de A. ({paginas}/90).`
- *(se tiver 90 ou mais páginas)* → segue logo para a cena **C10-12**.

---

## C10-12 — O Diário de A.

| | |
|---|---|
| ID | `cena_c10_12_diario` |
| Quando | falar com a Arquivista com **90 ou mais** páginas do diário (R10_10) |
| Onde | andar 98, Sala do Diário |
| Quem | herói (e o companheiro), A Arquivista |
| Música | caixa de música → `tema_principal` (piano e violoncelo, muito lento) |

🎬 A Arquivista estende as mãos. O herói tira as páginas do bolso. Elas voam sozinhas para as molduras, uma a uma, cada uma com um som de papel. As que faltam ficam vazias, com um "?" a lápis.
🎥 A câmara passa pelas molduras. As páginas castanhas. A página 68, a lápis, cinzenta. E, aqui e ali, as **azuis**, a brilhar um bocadinho.
- **A Arquivista** *(normal)*: "Reparaste nas páginas azuis? A tinta azul só existe num sítio da torre. No topo."
- **A Arquivista** *(normal)*: "Ele escreveu as castanhas a subir. Com medo, com fome, sozinho. As azuis escreveu-as depois. Lá de cima. Para ti."
- **A Arquivista** *(triste)*: "A da página 68 é a lápis. Um lápis amarelo que guardava para os dias importantes. Foi o dia em que perdeu o amigo. Não quis gastar tinta nesse dia. Quis que se pudesse apagar."
- 🎬 A Arquivista tira os óculos e limpa-os.
- **A Arquivista** *(normal)*: "Nunca disse o nome em cem páginas. Assina 'A.'. Uma vez, há muito tempo, quando ainda subia, passou por aqui e disse-mo. Pediu-me que o guardasse até alguém juntar o livro."
- **A Arquivista** *(normal)*: "Chama-se **Aren**. Tinha dezasseis anos. Vivia numa vila ao pé do mar, com a mãe e um cão velho chamado Farol. Gostava de desenhar mapas de sítios que não existiam."
- **A Arquivista** *(normal)*: "Foi o Jogador nº 1. É o Administrador. Está lá em cima há mil anos."
- 🎬 Silêncio. Na última moldura vazia, a 100, aparece por um instante um brilho azul. Depois apaga.
- **A Arquivista** *(feliz, só um bocadinho)*: "A última, ele ainda não escreveu. Acho que está à tua espera para a escrever."
- *(com o Kai)* **Kai** *(sério)*: "Dezasseis. Era da nossa idade." 🎬 pausa. "Perdeu o amigo no fogo. Como eu quase te perdi a ti. Como tu quase me perdeste a mim."
- *(com o Gorvan)* **Gorvan** *(normal)*: "Hmm. Um rapaz com um cão." 🎬 desvia o olhar. "Eu tive um cão. Pronto. Não digo mais nada."
- `[Sistema] …` *(sem falhas)*
- `[Sistema] Obrigado por as teres guardado.` *(aparece e desaparece num instante; sem falhas)*

⚙ Missão **H_24** (= R10_10) concluída. Flag `sabe_nome_aren`. O Diário do herói passa a ter o título **"O Diário de Aren"**. As páginas que faltam continuam a poder ser apanhadas (aparecem nas molduras). Conta para o **final secreto**.
⚙ Desbloqueia a **porta-livro** da Sala do Diário (masmorra **O Andar Zero**).

---

## C10-13 — O Nome Raspado

| | |
|---|---|
| ID | `cena_c10_13_sem_numero` |
| Quando | encontrar **O Jogador Sem Número** (andares 93, 97 ou 99; 2%; 30% com a missão R10_12 da Freya, ou depois de ler a nota do Fausto) |
| Onde | onde aparecer |
| Quem | herói (e o companheiro), O Jogador Sem Número |
| Música | silêncio → `boss` sem melodia (só percussão) |

🎬 Uma figura alta, de capa cinzenta e **máscara branca lisa**, sem olhos pintados. Por cima da cabeça, uma janela azul com **"????"** onde devia estar o número.
- **Sem Número** *(normal, voz rouca de quem não fala há muito)*: "Mais um com número. O último. Ele deve estar contente."
- **Sem Número** *(normal)*: "Eu também subi. Há trezentos anos. Ele ofereceu-me o lugar. Disse que não."
- **Sem Número** *(zangado)*: "A torre raspou-me o nome da porta da pirâmide. Apagou-me o número. Fiquei sem nada. Mas fiquei eu."
- `[Sistema] ????: Jogador Sem Número.`

**Durante a luta** (uma fala por fase, cada fase com uma arma diferente)
- *(fase 1, lança)* "Não precisas de lhe obedecer. A janela não manda. Pede. Há trezentos anos que ninguém percebe a diferença."
- *(fase 2, duas adagas)* "Diz-lhe que não. Ele aguenta. Já aguentou mil anos. Mais cem não o matam."
- *(fase 3, espada grande)* "Ou… diz-lhe que sim. E depois faz melhor do que ele. Eu não tive coragem para nenhuma das duas. Só para fugir."

**Depois da luta**
🎬 A máscara estala e cai. Por baixo, a cara de um homem normal, de barba, com olhos castanhos. Nada de azul.
- **Sem Número** *(normal)*: "O meu nome era **Teodoro**. Não o digo há trezentos anos. Soube-me bem."
- **Sem Número** *(normal)*: "Quando chegares lá acima, não lhe digas que me viste. Ele pensa que eu o odeio. Não odeio. Tenho pena dele. Tenho pena de nós os dois."
- **Sem Número** *(normal)*: "Fizeste-me falar. É o que se faz com os que ficam sozinhos. Faz-lhe o mesmo a ele."
- 🎬 Vai-se embora, devagar, para o escuro. Deixa a máscara.
- `[Sistema] Registo 0: restaurado.` *(sem falhas)*

⚙ Missão **R10_12** concluída. Flag `ouviu_sem_numero`. **Máscara Sem Número** · página especial **"O Nome Raspado"** (as palavras dele). No andar 38, a Porta dos Nomes passa a mostrar **"Teodoro"** no lugar do nome raspado.

---

## C10-14 — A Escada Final

| | |
|---|---|
| ID | `cena_c10_14_escada` |
| Quando | subir o andar 99 (uma parte por patamar) |
| Onde | andar 99, Base → Patamares das Estátuas → Ponto Sem Retorno → Porta do Topo |
| Quem | herói (e o companheiro), o Sistema, O Guardião da Escada; Nina (R10_08) se estiver na equipa |
| Música | `vazio` → o `tema_principal`, a cada patamar com mais um instrumento |

🎥 Uma escadaria de luz azul que sobe no vazio. Em cada patamar, **estátuas cinzentas** dos bosses que o herói venceu: a Aranha-Mãe, o Golem, a Hidra, o Faraó, o Dragão, o Leviatã, o Rei Sem Coroa, o Serafim… Cada estátua tem uma placa.
🎬 A cada patamar, o Sistema escreve. **Nenhuma destas mensagens tem falhas.**

| Patamar | Mensagem |
|---|---|
| Base | `[Sistema] Bem-vind{o/a} à última escada, {nome}.` *(é a primeira vez que o Sistema diz o nome do herói em vez do número)* |
| 1.º (Aranha-Mãe, Rei Musgo) | `[Sistema] Lembras-te do primeiro dia? Eu lembro-me do meu.` |
| 2.º (Faraó, Golem) | `[Sistema] O Faraó pediu-te para me dizeres uma coisa. Não precisas. Eu ouvi.` *(só se venceste o Faraó; senão, `[Sistema] Subiste muito.`)* |
| 3.º (Dragão, Leviatã) | `[Sistema] Tens amigos. Eu também tive um.` |
| 4.º (Rei Sem Coroa, Serafim) | `[Sistema] Desculpa por tudo o que te obriguei a fazer.` |
| Ponto Sem Retorno | `[Sistema] Vem.` |

- *(no 3.º patamar, com o Kai)* **Kai** *(sério)*: "'Eu também tive um.' Um amigo." 🎬 aperta o punho da espada. "O do fogo. É ele. Está a falar connosco, não está?"
- *(no 4.º patamar, com o Gorvan)* **Gorvan** *(normal)*: "Pede desculpa com a mesma letra com que mandava. Hmm. Os chefes cansados são todos iguais." 🎬 pausa. "Eu também pedi."
- *(com a Nina, em cada patamar: ver R10_08 em `povoacoes_r10.md`)*

**O Guardião da Escada** (antes do Ponto Sem Retorno)
🎬 Do vazio desce um anjo negro enorme, de quatro asas cheias de estrelas e uma espada estelar.
- **Guardião da Escada** *(normal)*: "Ele mandou-me não te fazer mal. Não lhe obedeço nisso. Ninguém sobe a última escada sem provar que a merece."
- `[Sistema] Guardião: O Guardião da Escada.`
- *(depois da luta)* **Guardião da Escada** *(normal)*: "Mereces." 🎬 ajoelha-se e as estrelas das asas apagam-se uma a uma. "Diz-lhe que fiz o meu trabalho até ao fim."
- `[Sistema] Guardião derrotado: O Guardião da Escada.`

**Ponto Sem Retorno**
🎬 Um patamar pequeno com um cristal e uma fogueira azul. Para cima, uma porta pequena de madeira, igual à porta de uma casa normal.
- `[Sistema] Ponto Sem Retorno. Podes gravar e voltar a Ascendia. Depois daquela porta, não há volta até ao fim.`
- `[Sistema] Vem.`
🎬 Se o herói ficar parado muito tempo (30 s) à frente da porta:
- `[Sistema] Desculpa. Não te quero apressar. Demora o tempo que precisares.`

⚙ Missão **H_25** concluída ao chegar ao Ponto Sem Retorno. Flag `ponto_sem_retorno`. **Gravação obrigatória** antes da porta (o jogo grava sozinho também). Desafio "Ler as 20 placas" dá o título *Memória da Torre*.

---

## C10-15 — O Jardim do Topo

| | |
|---|---|
| ID | `cena_c10_15_topo` |
| Quando | abrir a porta pequena do Ponto Sem Retorno |
| Onde | andar 100, Jardim do Topo |
| Quem | herói (e os companheiros), Aren; Kai (sempre: a forma depende de `kai_salvo` / `kai_vencido`) |
| Música | silêncio → vento na erva → `casa` (piano sozinho, a melodia do prólogo) |

🎥 A porta abre para… **o Prado do Despertar**. A mesma erva alta, as mesmas flores, a mesma árvore pequena. Mas ao **entardecer**, com o céu cor de laranja e uma brisa morna. Igual ao sonho do prólogo.
🎬 Ao fundo, sentado na erva, de costas, um homem de cabelo branco e roupa simples. Está a desenhar num caderno.
🎬 O herói aproxima-se. O homem não se vira.
- **Aren** *(normal, sem se virar)*: "Desculpa o jardim. Foi o primeiro sítio da torre onde me senti bem. Fiz uma cópia, cá em cima. Não sou muito original."
🎬 Vira-se. É um homem de idade incerta, de cabelo completamente branco e olhos **azuis como a janela do Sistema**. Tem cara de rapaz e de velho ao mesmo tempo. Sorri.
- **Aren** *(feliz, nervoso)*: "Olá. Ensaiei isto mil anos e agora não sei o que dizer."

**Se `sabe_nome_aren`**
- **Aren** *(surpreendido)*: "Tu sabes quem eu sou. Vejo-o na tua cara. A Arquivista contou-te." 🎬 ri-se baixinho. "Ela guarda tudo. Até o que eu lhe pedi para esquecer."
- **Aren** *(normal)*: "Então posso dizer-te como deve ser." 🎬 levanta-se, limpa a erva das calças. "Chamo-me Aren. Fui o Jogador nº 1. Olá, Jogador{/a} nº 10 000. Olá, {nome}."

**Se não `sabe_nome_aren`**
- **Aren** *(normal)*: "Não sabes quem eu sou. Está bem. É justo. Eu também já quase não sei."
- **Aren** *(normal)*: "Fui o primeiro com número. O nº 1. As páginas que encontraste pela torre fui eu que as escrevi. O meu nome…" 🎬 pausa comprida. "Chamo-me Aren. Há muito tempo que não o digo em voz alta. Soa estranho."

⚙ A página **100** (tinta azul) aparece no caderno dele. Ele arranca-a e dá-a ao herói. `[Sistema] Página do diário encontrada (100/100).` *(só se tiver as outras 99; senão, o número certo)*

**A conversa**
- **Aren** *(normal)*: "Sabes o que te vou pedir. O Serafim contou-te. Eu pedi-lhe que contasse. Não tive coragem de ser eu."
- **Aren** *(triste)*: "Subi como tu. Perdi um amigo como tu quase perdeste. Cheguei aqui. Aceitei, para descobrir como mandar toda a gente para casa. E fiquei preso."
- **Aren** *(normal)*: "Quem governa a torre não pode sair. Quem não governa não pode mandar ninguém embora. Tentei tudo. Mil anos. Comecei a trazer Jogadores. Com números, para os poder contar. À procura de alguém que ficasse."
- **Aren** *(triste)*: "Trouxe-os à força. Isso não tem desculpa. Pedi desculpa na mesma. Viste."

*(falas que mudam conforme o que o herói fez — aparecem as que se aplicam, por esta ordem)*
- *(espelho do quarto, C10-04)* **Aren**: "Tocaste no espelho do quarto. Eu também tocava. Todos os dias, nos primeiros cem anos."
- *(espelho do trono)* **Aren**: "Tocaste no espelho do trono. Curioso. Ninguém toca nesse."
- *(`viu_quarto`)* **Aren** *(zangado consigo)*: "A casa sem número… não fui eu. É a torre. Ela quer que fiquem. Eu só quero que alguém queira."
- *(venceu o Faraó)* **Aren** *(triste)*: "O Faraó. Foi um dos que se sentaram aqui antes de mim. A torre guardou-o lá em baixo, numa caixa de ouro, a contar areia. É o que faz aos que se cansam." 🎬 pausa. "Eu tinha medo de acabar assim. Por isso é que te chamei."
- *(`ouviu_sem_numero`)* 🎬 Aren olha para a Máscara Sem Número no inventário do herói. "O Teodoro. Ele… está bem?" ▶ *"Tem pena de ti."* / *"Não te odeia."* → **Aren** *(com os olhos a brilhar)*: "Trezentos anos a pensar o contrário."
- *(`gorvan_paz` e Gorvan na equipa)* **Gorvan** *(normal)*: "Fizeste-me ler o caderno da Odília até ao fim. A página 74. Tinta azul. Eras tu." **Aren** *(normal)*: "Era. Desculpa ter espreitado. Os teus cinco eram muito bons."
- *(R3: `sssar_defendida` e Ssark na equipa)* **Ssark** *(normal)*: "Ssss. O que ssse sssenta no trono não é rei. É guarda de uma prisão. Conheço o género." **Aren**: "É exatamente isso. Obrigado, chefe."

**O Kai**
- *(se `kai_salvo`)* **Kai** *(zangado, a dar um passo em frente)*: "Prometeste-me que ia para casa se chegasse primeiro. Era mentira." **Aren** *(triste)*: "Era meia mentira. Ias para casa. E ficavas no meu lugar. Desculpa, Kai. A tua irmã… a Yui, não é? Está bem. Eu vejo-a às vezes, pelas janelas. Faz desenhos de espadas."
  - 🎬 O Kai fica calado. Depois baixa a espada.
- *(se `kai_vencido`)* 🎬 Aren faz um gesto. Uma janela azul abre-se no ar: lá dentro, o **Kai**, a dormir, encolhido, como numa bolha. **Aren** *(normal)*: "Está aqui. Desde o 68. Não o deixei cair. Já deixei cair um amigo uma vez." 🎬 olha para o herói. "Ele não sabe que perdeu. Está a sonhar que ganhou. Quando isto acabar, decide tu o que lhe acontece."

**A oferta**
🎬 Aren estende a mão aberta. Por cima dela, uma janela azul pequenina com uma coroa desenhada.
- **Aren** *(normal)*: "Fica com isto. Com o trono, com as janelas, com a torre. Podes fazer melhor do que eu. Podes deixar de trazer pessoas à força. Podes mudar as regras."
- **Aren** *(triste)*: "E eu posso, finalmente, descansar."
- `[Sistema] Aceitar o lugar de Administrador?` *(a janela tem dois botões: Sim · Não)*

▶ **"Sim."** → final **"O Novo Administrador"** (`finais.md`, secção 3), sem luta.
▶ **"Não."**
▶ **"Há outra maneira."** *(só aparece se as 5 condições do final secreto estiverem cumpridas)*

- *(não)* **Aren** *(normal)*: "Eu sabia. Eu também disse que não, na primeira vez. Durante uma hora." 🎬 fecha a mão; a janela da coroa apaga-se. "Então tens de me vencer. É a regra. Não fui eu que a fiz. Foi a torre. Só sai daqui quem vence quem está no trono."
- *(outra maneira)* **Aren** *(surpreendido)*: "Outra… maneira?" 🎬 olha para o herói muito tempo. "Ninguém nunca disse isso." 🎬 sorri devagar. "Mostra-me. Mas a torre não deixa sem luta. Vamos ter de lutar na mesma. Só que talvez… lutar ao contrário."
- **Aren** *(normal)*: 🎬 deixa cair o caderno na erva. O jardim desfaz-se em janelas azuis que voam para cima. "Desculpa. Isto vai doer um bocadinho aos dois."

⚙ Missão **H_26** ativa. Transição para a arena **O Trono do Administrador** e para a cena C10-16.

---

## C10-16 — O Administrador

| | |
|---|---|
| ID | `cena_c10_16_luta` |
| Quando | começa logo a seguir à C10-15 (se o herói disse "Não" ou "Há outra maneira") |
| Onde | andar 100, O Trono do Administrador |
| Quem | herói (e os companheiros), Aren; na fase 3, os amigos nas janelas |
| Música | `administrador` (fases 1–2) → `administrador` com coro (fase 3) → só o coração a bater (fase 4) |

🎬 Uma sala enorme cheia de janelas azuis a flutuar, como um céu de ecrãs. Ao fundo, um trono simples de pedra, sem almofada.
- `[Sistema] Boss: O Administrador, Aren, Jogador nº 1.`

**Fase 1 — O Jogador nº 1** (100–75%)
🎬 Aren luta com uma espada simples de ferro, como a primeira do herói. Esquiva-se bem. Ri-se quando falha.
- *(início)* **Aren**: "Há mil anos que não pego numa espada. Desculpa se for mau."
- *(a meio)* **Aren** *(feliz)*: "És bom. Melhor do que eu era. Eu fugia dos lobos do andar 1."
- *(fim da fase)* **Aren** *(normal)*: "Também tive medo. Tive sempre. Até agora."

**Fase 2 — As Memórias** (75–50%)
🎬 Aren levanta as mãos. Das janelas saem **Ecos** dos bosses que o herói venceu, um de cada região, um de cada vez.
- *(início)* **Aren** *(triste)*: "Desculpa. A torre usa o que tens dentro. Também me fez isto a mim."
- *(Eco da Aranha-Mãe)* **Aren**: "A primeira mãe. Eu também a matei. Também não sabia."
- *(Eco do Rei Sem Coroa)* **Aren**: "Ele tentou parar a torre. Eu deixei-o tentar. Queria que alguém conseguisse."
- *(fim da fase)* **Aren** *(normal)*: "Ainda estás de pé. Ainda bem. Ainda bem."

**Fase 3 — O Sistema** (50–25%)
🎬 Aren desfaz-se e torna-se uma **figura enorme feita de janelas azuis**. A interface do herói começa a falhar: a barra de vida mostra números errados, o mapa mente.
- `[Sistema] Tens a certeza? Sim / Não` *(menus que prendem: carregar em "Não" para sair)*
- **Aren** *(voz de muitas janelas)*: "Isto sou eu há mil anos. Já nem sei onde acabo e onde começa o Sistema."
🎬 Depois de 10 s, **as janelas do herói mudam**: em vez de números, aparecem **caras**. Os companheiros e os NPCs de Ascendia com 10 corações, cada um na sua janela, a fazer **um ataque** (ver `docs/BOSSES.md`, secção 21). Cada um diz uma frase curta:
  - **Brom**: "Martelo-Forte! Para a frente!"
  - **Dona Marta**: "Come primeiro! Depois bate!" *(cura)*
  - **Mia**: "Eu também sou aventureira! Rank… F! Mas conta!"
  - **Lyra**: "Registo de missão: GANHAR!"
  - **Gorvan** *(se não estiver na equipa)*: "Pelos cinco!"
  - **Kai** *(se `kai_salvo` e não estiver na equipa)*: "Juntos, lembras-te? JUNTOS!"
  - **Fausto**: "Está tudo escrito. Até isto. Eu escrevo o resto!"
  - *(os outros NPCs: uma frase cada, nos ficheiros de diálogo deles, condição `final_janela`)*
- **Aren** *(a voz a falhar)*: "Tantos… Tens tantos. Eu nunca tive tantos."
- *(se "Há outra maneira")* 🎬 As janelas dos amigos não atacam o Aren: **seguram-no**. **Aren** *(baixinho)*: "Estão a… segurar-me? Porquê?" → a luta muda para o **final secreto** (`finais.md`, secção 5). A fase 4 não acontece.

**Fase 4 — O Fim** (25–0%)
🎬 A interface desaparece toda. Não há barra de vida, não há números, não há mapa. Só o herói, a figura de janelas e o som de um coração.
🎬 A figura encolhe até voltar a ser Aren, de joelhos, cansado.
🎬 Uma **janela gigante** aparece entre os dois:
- `[Sistema] Desistir?` *(botões: Sim · Não)*
🎬 Os botões não funcionam: carregar em "Não" não faz nada, carregar em "Sim" mostra `[Sistema] Tens a certeza?` uma e outra vez. A única maneira é **atacar a janela** até ela partir.
🎬 A janela parte-se em mil quadradinhos azuis que caem como neve.
- **Aren** *(a sorrir, deitado na relva do jardim, que voltou)*: "Partiste-a. Eu nunca a parti. Carreguei sempre no 'Não'. Mil anos a carregar no 'Não'."
- `[Sistema] Boss derrotado: O Administrador.` *(sem falhas)*
- `[Sistema] Obtiveste: Chave do Sistema.`
- `[Sistema] Título obtido: Conquistador da Torre.`

⚙ Missão **H_26**: passo da luta cumprido. Segue para **a escolha final** (`docs/guiao/finais.md`, secção 1).
