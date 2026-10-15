# Povoações da Região 10 — diálogos e missões

Os NPCs que vivem nos andares 91–100 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r10_abismo.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap10_abismo.md`. O fim: `docs/guiao/finais.md`.

**A gente da Guilda** no Último Posto fala como soldados cansados e contentes: curto, prático, com piadas secas.
**Os Perdidos** são Jogadores que desistiram: falam devagar, baixinho, com frases que acabam a meio. Cada um tem o
**número** pintado na porta e diz-o como quem diz a idade. Dentro da cidade **o Sistema não aparece**.
Bips: os da Guilda, firmes; os Perdidos, lentos e graves, como um disco a rodar devagar; a Arquivista, de papel a virar.

---

## 1. Último Posto (andar 91)

Primeira chegada: cena **C10-01** (abandonado). Volta à vida com a cena **C10-02** (R10_01). Tem **cama**, **cristal**,
**Forja Estelar** (depois de R10_02) e **loja** (Tibério).

### 1.1 Sargento Bruma

| | |
|---|---|
| Voz | bips curtos, de comando; ri-se pelo nariz |
| Quem é | veterana da Guilda, cabelo grisalho curto, cicatriz no queixo, machado às costas. O avô dela era da **expedição do Capitão Orsi**, a última que chegou ao andar 91, há 60 anos, e nunca voltou. Prometeu subir se alguém abrisse o caminho |

| ID | Condição | Fala |
|---|---|---|
| `bruma_01` | antes de R10_01 | *(só aparece depois da C10-02; antes não há ninguém no posto)* |
| `bruma_02` | — | "O posto tem regras. Uma: ninguém sai da luz sozinho. Duas: quem acende a fogueira não lava a panela. Três: não há três." |
| `bruma_03` | — | "Sessenta anos à espera. Os meus colegas acham que sou sentimental. Sou. Não lhes digas." |
| `bruma_04` | `andar_maximo >= 95` | "Mandámos uma patrulha até ao 94. Voltou com um dos rapazes a jurar que viu a mãe dele num bocado de pântano. Era um Eco. Agora já não quer lá voltar. Eu também não quereria." |
| `bruma_05` | `flag(sabe_nome_aren)` | "Aren. Um rapaz de dezasseis anos. Mil anos sozinho." 🎬 pausa. "Se tiveres de lutar com ele, luta bem. Os cansados merecem um adversário a sério." |
| `bruma_orsi` | depois de ler a mensagem da expedição (segredo do 91) | "'O escuro tem chão.' Era o que o meu avô dizia quando eu tinha medo à noite. Nunca soube de onde vinha." 🎬 vira a cara. "Agora sei. Obrigada." |
| `bruma_06` | `flag(ponto_sem_retorno)` | "Vais lá acima. Ouve: o posto fica aceso até voltares. Nem que eu tenha de soprar as âncoras com a boca." |

### 1.2 Tibério

O mercador das Zonas Seguras (ver `docs/LOJAS.md`, secção 3.1). Aqui tem uma loja maior.

| ID | Condição | Fala |
|---|---|---|
| `tiberio_posto_01` | abrir loja | "A última loja antes do fim do mundo! Literalmente! Aproveita, que os preços não descem mais. Pois não. Não descem." |
| `tiberio_posto_02` | — | "Trinta anos a carregar esta mochila de andar em andar. Cheguei ao 91. A minha mãe dizia que eu não chegava ao fim da rua." |
| `tiberio_posto_03` | `flag(ponto_sem_retorno)` | "Se ele te oferecer o trono… pergunta se lá em cima precisam de um mercador. Estou a brincar. Não estou. Estou." |

### 1.3 Dorn — Forja Estelar

| | |
|---|---|
| Voz | bips graves e lentos; martela a meio das frases |
| Quem é | ferreiro itinerante, grande, cego do olho esquerdo (uma faísca de mitril, há vinte anos). Andou de forja em forja à procura de "metal que valha a pena". Respeita o **Brom** e o **Mestre Ragnar**; não respeita mais ninguém |

| ID | Condição | Fala |
|---|---|---|
| `dorn_01` | antes de R10_02 | "Forja Estelar. Precisa de fogo de estrela. Dez Fragmentos Estelares para a bigorna, três Núcleos do Vazio para o lume. Traz e eu acendo. Não trazes, não acendo." |
| `dorn_02` | `missao(R10_02) == concluida` | 🎬 o lume fica azul e branco. "Olha para isto. Trinta anos. Trinta anos à procura de um lume assim." 🎬 limpa o olho bom. "É fumo. Não é nada." |
| `dorn_03` | — | "Só vejo de um olho. Chega. As armas boas veem-se com as mãos." |
| `dorn_04` | `missao(R10_02) == concluida && missao(R10_11) != concluida` | "Armas míticas. Doze. Cada uma pede um Coração Estelar e uma Gema Prismática. E o toque final de um Martelo-Forte. O teu Brom. Eu faço o corpo; ele faz a alma. É assim que se faz." |
| `dorn_05` | `missao(R10_11) == concluida` | "Doze. Doze armas que vão ficar nos livros. O meu nome vai estar ao lado do do Brom." 🎬 pausa. "Ao lado. Não por baixo. Diz-lhe isso." |
| `dorn_06` | `tem_item(decima_milesima)` | "Essa espada com o teu número. Quem a acabou? O Brom? Hmm. Bom trabalho. Muito bom. Não lhe digas que eu disse." |

### 1.4 Kai (se `kai_salvo`)

Vive no posto quando não está na equipa. Falas da **fase D** em `docs/dialogos/kai.md`. No posto tem mais três:

| ID | Condição | Fala |
|---|---|---|
| `kai_posto_01` | — | "Treino aqui todas as manhãs. A Bruma diz que faço barulho. Eu digo que é o barulho de quem vai ganhar." |
| `kai_posto_02` | `andar_maximo >= 97` | "Estive a pensar. Se tu não me tivesses ido buscar… eu estava naquela cidade cinzenta. Numa casa com o meu número na porta. A tricotar." 🎬 faz uma careta. "Eu não sei tricotar." |
| `kai_posto_03` | `flag(sabe_nome_aren)` | "Aren. Tinha um amigo. Perdeu-o. Eu quase fui o amigo que alguém perdeu." 🎬 olha para o herói. "Obrigado por não me perderes." |

---

## 2. Cidade dos Perdidos (andar 97)

Primeira chegada: cena **C10-07**. Tem **casa vazia** (dormir), **cristal** e o **Mercado das Memórias**. O Sistema
não aparece dentro da cidade (as missões ficam escritas no Diário à mão). Antes de o relógio andar (C10-10) a cidade
é cinzenta e os Perdidos só falam à porta de casa; depois, saem à rua.

### 2.1 "Mãe Dois" (nº 2 048)

| | |
|---|---|
| Voz | bips lentos e redondos, com um tremor de avó |
| Quem é | a mais velha da cidade, pequenina, óculos grossos, casaco de malha. Chegou ao 97 há mais de sessenta anos e sentou-se. Tricota um cachecol enorme desde o primeiro dia (uma volta por dia). Trata toda a gente por "meus meninos". Dá a missão **R10_07** |

| ID | Condição | Fala |
|---|---|---|
| `mae_dois_01` | — | "Senta-te um bocadinho. Toda a gente que sobe tem pressa. Aqui não há pressa. Às vezes isso é bom. Às vezes é o problema." |
| `mae_dois_02` | — | "O meu número é dois mil e quarenta e oito. Era bom em matemática, o meu neto. Disse que era um número bonito. Nunca percebi porquê." |
| `mae_dois_03` | durante R10_07 | "Não os puxes. Ouve-os. Cada um parou por uma razão. Descobre a razão e o resto vem sozinho." |
| `mae_dois_04` | `perdidos_convencidos >= 3` | "Três dos meus meninos com mochila às costas. Não durmo de contente. Quer dizer, não durmo de qualquer maneira. Mas agora é por uma razão boa." |
| `mae_dois_05` | `flag(relogio_anda)` | "Ouves? Tique-taque. Há sessenta anos que não ouvia o tempo a passar. Pensei que tinha saudades disto. Afinal tinha medo. Agora não sei. Estou contente." |
| `mae_dois_06` | `flag(sabe_nome_aren)` | "Aren. Que nome bonito. Quando o vires, diz-lhe que a Mãe Dois lhe tricota um cachecol, se ele quiser descer." |
| `mae_dois_07` | `flag(viu_quarto)` | "Mostrou-te o teu quarto. Eu sei. Ficas com a cara assim, depois. Come qualquer coisa. Ajuda." |

### 2.2 Rafa (nº 5 150) — o músico

| | |
|---|---|
| Voz | bips com ritmo; às vezes canta a meio da fala |
| Quem é | trinta e poucos anos, barba por fazer, chapéu de lã. Tocava em bares no mundo real. Desistiu quando a guitarra se partiu no andar 94 ("sem música não consigo subir"). Tem o **ponteiro grande** do relógio. Um dos **5 Perdidos** (R10_07) e dá a **R10_14** |

| ID | Condição | Fala |
|---|---|---|
| `rafa_01` | — | "Sabes alguma música do nosso mundo? Eu sei duzentas. Já me esqueço das letras. Ficam só as melodias. Como fantasmas." |
| `rafa_02` | antes de R10_14 | "A minha guitarra partiu-se no 94. Um Eco de um Lobo saltou-lhe para cima. Um lobo! Do andar 1! Que vergonha." |
| `rafa_03` | antes de R10_14 | "Madeira do Tempo para o corpo. Fio de Luz Estelar para as cordas. Fazes-me uma guitarra e eu… eu toco. Não prometo mais nada." |
| `rafa_04` | `missao(R10_14) == concluida` | "'Casa.' Escrevi-a há dez anos e nunca a toquei a ninguém. Agora tu tens-na no gira-discos. Que estranho. Que bom." |
| `rafa_ponteiro` | durante o puzzle do relógio | "O ponteiro grande? Está aqui, a segurar a janela. Toma. A janela fica aberta sozinha agora. Já não há vento cá dentro há muito tempo." |
| `rafa_convencido` | `perdido(rafa)` | "Vou subir. Quero tocar isto lá em cima. Para ele. Mil anos sem música deve ser pior do que mil anos sem casa." |

### 2.3 "Doutor" (nº 3 001)

| | |
|---|---|
| Voz | bips rápidos, aos tropeções, como quem pensa mais depressa do que fala |
| Quem é | sessenta anos, bata branca suja, óculos na testa e outros no nariz. Era professor de física. Estuda o Sistema há trinta anos com Fragmentos de Sistema numa parede cheia de fios. Explica **o que cada final faz** (sem nomes de finais: com o que descobriu). Um dos **5 Perdidos** |

| ID | Condição | Fala |
|---|---|---|
| `doutor_01` | — | "Não sou doutor. Era professor. Os outros chamam-me Doutor porque tenho uma bata. A bata era de um pintor. Não digas a ninguém." |
| `doutor_02` | — | "O Sistema não é magia. É uma linguagem. Tem regras. Regras partem-se. Regras reescrevem-se. Ainda não percebi como." |
| `doutor_03` | antes de `perdido(doutor)` | "Traz-me Fragmentos de Sistema. Dez. Encontram-se nas falhas, nos quadradinhos coloridos. Com dez, acabo a parede. Com a parede acabada, percebo." |
| `doutor_finais_1` | `perdido(doutor)` | "Descobri três portas na parede. Primeira: quem vence o do trono pode **sair**. Abre-se uma porta para o mundo de onde veio. Só uma. Só para ele." |
| `doutor_finais_2` | `perdido(doutor)` | "Segunda: quem se **senta** no trono pode mudar as regras. Tudo. Menos uma: não pode sair. Nunca." |
| `doutor_finais_3` | `perdido(doutor)` | "Terceira: quem parte o **núcleo** desliga a torre. Os mundos voltam para onde estavam. Os andares sobem como luz. Não sei o que acontece a quem está lá dentro. Acho que fica bem. Acho." |
| `doutor_finais_4` | `perdido(doutor) && condicoes_final_secreto >= 4` | "E há uma quarta. Pequenina. Um fio que não liga a nada. Ainda. Como se esperasse que alguém o ligasse. Precisa de muita gente. Muita gente que goste de ti." |
| `doutor_convencido` | `perdido(doutor)` | "Trinta anos a estudar uma janela. Está na altura de ir ver quem está do outro lado. Vou contigo até à praça do fim. Depois decido." |

### 2.4 Nina (nº 9 000)

| | |
|---|---|
| Voz | bips baixos, curtos, a fugir; ri-se de repente e para |
| Quem é | dezoito anos, cabelo curto pintado de azul já desbotado, casaco grande demais. Chegou à torre há três anos. Subiu numa equipa da Guilda até ao 93; a equipa voltou para trás depois de um Clone Espelhado ferir dois deles; ela continuou sozinha e sentou-se no 97 "só por uma noite". Faz magia de **gelo** (gostava de neve no mundo real: nunca tinha visto). Tem o **ponteiro pequeno** do relógio. Dá a **R10_08**; pode ser **companheira** |

| ID | Condição | Fala |
|---|---|---|
| `nina_01` | — | "O meu número é redondo. Nove mil. Toda a gente acha que é sorte. Eu acho que é só redondo." |
| `nina_02` | antes de R10_08 | "Fiquei aqui uma noite. Uma. Depois mais uma. As noites aqui colam-se umas às outras como neve molhada." |
| `nina_03` | antes de R10_08 | "Não é medo de morrer. É medo de chegar lá acima e não haver nada. Ou de haver alguma coisa e eu não aguentar." |
| `nina_ponteiro` | durante o puzzle do relógio | "O ponteiro pequeno? Uso-o para mexer o chá." 🎬 tira-o da chávena. "Desculpa. Está um bocadinho doce." |
| `nina_04` | `flag(relogio_anda)` | "O relógio anda. Isso quer dizer que amanhã é outro dia. Há três anos que não havia amanhã." 🎬 pausa. "Leva-me contigo. Antes que eu mude de ideias." → **R10_08** |
| `nina_05` | `missao(R10_08) == concluida` | "Cheguei à última escada. Eu. A nº 9 000. Que só ia ficar uma noite." 🎬 ri-se e para. "Obrigada. A sério." |

### 2.5 O Desistente (nº 7 777)

O guardião do andar (cena **C10-09**). Depois de vencido fica sentado no caixote da praça e ajuda na **R10_07**.

| ID | Condição | Fala |
|---|---|---|
| `desistente_01` | `flag(desistente_ouvido)` | "Queres saber quem pode voltar a subir? Eu sei de todos. Quarenta anos a ver as cortinas mexer." |
| `desistente_pista_rafa` | R10_07 | "O Rafa? Partiu a guitarra e partiu-se com ela. Arranja-lhe música e ele levanta-se sozinho." |
| `desistente_pista_doutor` | R10_07 | "O Doutor não tem medo de subir. Tem medo de não perceber. Ajuda-o a perceber." |
| `desistente_pista_bia` | R10_07 | "A Bia viu a equipa dela ser comida pelo escuro, no 92. Não tem medo do Administrador. Tem medo do escuro. Mostra-lhe a luz." |
| `desistente_pista_ulisses` | R10_07 | "O velho Ulisses diz que é velho demais. Mentira. Tem saudades de uma coisa e acha que nunca mais a vê. Descobre o quê." |
| `desistente_pista_gemeos` | R10_07 | "Os gémeos. A Lia quer ir. O Lino não. Andam zangados há dez anos. Quando um se esconde, o outro não o procura. Procura-o tu." |
| `desistente_02` | `perdidos_convencidos == 5` | "Cinco. Eu levei quarenta anos a não convencer ninguém, nem a mim. Tu levaste uma semana." 🎬 ri-se. "Vai-te embora antes que eu chore em frente aos vizinhos." |

### 2.6 Os outros três Perdidos da R10_07

| Perdido | Quem é | ID | Fala |
|---|---|---|---|
| **Bia** (nº 6 080) | quarenta anos, enfermeira no mundo real; cabelo apanhado num lenço; dorme de luz acesa | `bia_01` | "Não apagues a luz. Por favor. Desculpa. Não apagues." |
| | | `bia_02` | "A minha equipa ia à frente. O Devorador abriu a boca e as estrelas foram todas lá para dentro. Eles também. Eu estava atrás. Fiquei." |
| | | `bia_convencida` | "Vi as âncoras acesas. Vi o caminho todo com luz. Se o escuro tem chão… então eu ponho lá o pé." |
| **Velho Ulisses** (nº 4 444) | oitenta anos, careca, bigode enorme; chegou à torre já com cinquenta | `ulisses_01` | "Sou velho demais para escadas. Tenho oitenta anos. Ou noventa. Perdi a conta no 60." |
| | | `ulisses_02` | "Sabes do que tenho saudades? Do primeiro dia. Do prado. Da erva alta. Acordei lá e pensei que estava morto e era o céu. Foi o melhor dia." |
| | | `ulisses_convencido` | 🎬 cheira a flor. "É do prado. É mesmo." 🎬 pausa. "Dizes que lá em cima há um prado igual? Então vou. Um velho tem direito a ver o céu duas vezes." |
| **Lino e Lia** (nº 8 501 e 8 502) | gémeos de vinte e poucos anos, chegaram no mesmo dia, de mãos dadas. Ela quer subir; ele não. Não se falam há dez anos e vivem em casas uma ao lado da outra | `lia_01` | "Eu ia. Ia já. Mas não vou sem ele. E ele não vai. E eu não falo com ele. Pronto." |
| | | `lino_01` | *(só de dentro de casa, sem abrir a porta)* "Diz-lhe que não estou." |
| | | `gemeos_convencidos` | **Lino**: "Encontraste-me. Ela nunca me encontrava. Escondia-me sempre no mesmo sítio para ela me encontrar." **Lia**: "…Eu sabia onde estavas. Sempre soube. Só queria que viesses tu." 🎬 abraçam-se. **Os dois**: "Vamos." |

### 2.7 Chico das Memórias (nº 2 999) — Mercado das Memórias

| | |
|---|---|
| Quem é | vendedor de bigode fino e colete de lantejoulas; vende **objetos do mundo real** que os Perdidos trouxeram nos bolsos (decoração) e troca **Fragmentos de Eco** por materiais de qualquer região. Ver `docs/LOJAS.md`, secção 3.11 |

| ID | Condição | Fala |
|---|---|---|
| `chico_01` | abrir loja | "Memórias! Memórias fresquinhas! Um porta-chaves de um país que não existe! Uma caneca com o nome de outra pessoa! Um telemóvel sem bateria desde mil novecentos e… não sei!" |
| `chico_02` | — | "Os ecos? Dá-me dez e dou-te pedra de qualquer andar. Os ecos lembram-se de onde vieram. Eu só os ajudo a voltar." |
| `chico_03` | `flag(viu_quarto)` | "Tenho uma coisa que talvez queiras." 🎬 mostra um despertador igual ao do quarto. "Não. Não é o teu. É de alguém que também teve um. Todos temos um." |

### 2.8 Ssark (só com `sssar_expulsa`)

| | |
|---|---|
| Quem é | o Chefe Ssark, mais velho, magro, as escamas baças. Depois de expulsos, os Ssar espalharam-se pelos andares; ele subiu sozinho "até onde a dor deixasse" e parou no 97. **Não é Jogador**: a cidade aceita qualquer um que tenha desistido. Vive numa casa sem número, ao pé do portão |

**Cena: O Chefe Sem Aldeia** (falar com ele pela primeira vez)
🎬 Uma figura de escamas sentada à porta de uma casa, a talhar uma lança pequena de madeira que nunca acaba.
- **Ssark** *(normal, sem levantar os olhos)*: "O da janela. Lembro-me de ti. Tu também te lembras de mim. Do 24."
- **Ssark** *(triste)*: "Os meus foram para o 22, para o 25, para lado nenhum. A Ilssa ficou a tratar dos velhos num charco sem nome. O Kesh foi com os Renegados, como o irmão. Para ter onde dormir."
- **Ssark** *(normal)*: "Não estou zangado. Fizeste o que a Guilda mandou. Eu também fiz o que a minha aldeia precisava. Perdemos os dois."

▶ **"Desculpa."**
▶ **"Vem comigo. Para cima."** *(só com `perdidos_convencidos >= 3`)*
▶ *(ficar calad{o/a})*

- *(desculpa)* **Ssark** *(normal)*: "Ssss. Aceito. Não muda nada. Mas aceito." ⚙ fala `ssark_97_desculpa`.
- *(vem)* **Ssark** *(surpreendido)*: "Para cima? Um lagarto velho, no fim do mundo?" 🎬 olha para a lança pequena. Parte-a ao meio. "…Os meus filhos eram a aldeia toda. Iam gostar de saber que o chefe deles subiu até ao fim. Vou. Não por ti. Por eles."
  - ⚙ flag `ssark_97_sobe`. O Ssark aparece no fim do jogo (ver `finais.md`). **Não conta** para os 5 Perdidos.
- *(calado)* **Ssark** *(normal)*: "Fazes bem. Não há nada para dizer." ⚙ sem efeito.

### 2.9 Os Perdidos genéricos (rua, depois de C10-10)

| ID | Fala |
|---|---|
| `perdido_01` | "Ouviste o relógio? Ouviste? Pensava que estava a sonhar." |
| `perdido_02` | "Tenho o número 6 312. Já não me lembro do meu nome. O número ficou. É engraçado o que fica." |
| `perdido_03` | "Às vezes subo ao telhado e olho para cima. Só olho. Já é alguma coisa." |
| `perdido_04` | "Dizem que tu saíste da casa sem número. Eu fiquei lá dois anos. Era a casa da minha avó. Ainda cheira a bolachas, quando chove." |
| `perdido_05` | "Se lá chegares… diz-lhe que nem todos os que desistiram estão tristes. Alguns só estão cansados. É diferente." |

---

## 3. A Arquivista (andar 98)

| | |
|---|---|
| Voz | bips de papel a virar, sempre baixinhos |
| Quem é | mulher sem idade, óculos redondos, vestido feito de páginas de livro (as páginas mudam: às vezes leem-se frases). Guarda a **Biblioteca do Mundo**: um livro de cada mundo engolido. Conheceu o Aren quando ele subiu; guardou-lhe o nome. Dá a **R10_10** (cenas **C10-11** e **C10-12**) e o puzzle do **Catálogo** |

| ID | Condição | Fala |
|---|---|---|
| `arquivista_01` | — | "Cada corredor é um mundo. Lê um livro de cada e vais saber mais da torre do que ela sabe de si mesma." |
| `arquivista_02` | — | "Silêncio, por favor. Não por mim. Pelos livros. Alguns estão a dormir há mil anos." |
| `arquivista_catalogo` | antes do puzzle | "Três livros. Procura-mos: *O Mar Que Subiu*, *Receitas de Uma Avó Anã* e *Como Se Faz Uma Estrela*. Usa o catálogo. Ordem alfabética, e depois por mundo. Não é difícil. É só comprido." |
| `arquivista_catalogo_ok` | puzzle feito | "Trouxeste os três. Sabes porque os pedi? São os três livros que o rapaz leu quando passou aqui. Um sobre o mar, um sobre uma avó, um sobre estrelas. Diz-me muito sobre ele." |
| `arquivista_03` | menos de 90 páginas | "{paginas} páginas. Faltam {90-paginas}, pelo menos. Procura nos sítios altos e nos sítios tristes. Ele gostava dos dois." |
| `arquivista_04` | `flag(sabe_nome_aren)` | "Agora que sabes, diz o nome dele em voz alta, quando lá chegares. Ninguém o diz há mil anos. Os nomes estragam-se quando ninguém os diz." |
| `arquivista_05` | `flag(ouviu_sem_numero)` | "O Simão falou contigo? Então ainda há esperança para toda a gente." |
| `arquivista_mundo` | ler um livro de um corredor | *(cada corredor tem uma história de 3 linhas do seu mundo: os 10 mundos das regiões, mais o mundo do herói, que tem as páginas em branco)* |
| `arquivista_06` | ler o livro do mundo do herói | "Esse? Está em branco. É o teu mundo. Ainda não foi comido. É por isso que está em branco. É uma coisa boa." |

---

## 4. Missões da região, passo a passo

### R10_01 — Reativar o Último Posto
| | |
|---|---|
| Quem dá | (sozinha: cena C10-01) · = parte da **H_22** |
| Recompensa | posto ativo (cama, cristal, loja do Tibério, Forja Estelar depois de R10_02) |

1. **Passo 1**: acender as **5 âncoras de luz** do andar 91 **pela ordem em que as estrelas piscam** (cada âncora tem uma estrela por cima; piscam uma a uma, de 10 em 10 s). A ordem errada apaga as que estavam acesas.
2. **Passo 2**: entre âncoras, o caminho é escuro: Sombras saem da tua sombra. A luz de cada âncora acesa faz uma zona segura.
3. **Fim** — cena **C10-02**.

### R10_02 — A Forja Estelar
Dorn. **10 Fragmento Estelar + 3 Núcleo do Vazio** → **Forja Estelar** (armas e armaduras Estelares, melhorias até +10, armas míticas). `dorn_02`.

### R10_03 — Constelações do Mar
(andar 92). Tocar nas estrelas de cada constelação pela ordem (como desenhos de "ligar os pontos": a primeira estrela é a maior). Cinco constelações: **o Lobo, a Bigorna, a Serpente, a Baleia e a Janela** (as quatro primeiras lembram bosses; a última é um quadrado). Cada uma faz um bocado do caminho até ao Planeta Pequeno → baú de ouro.

### R10_04 — O Espelho Partido
(andar 93). Os **7 estilhaços** estão espalhados no labirinto (um em cada zona e três na Galeria). Cada estilhaço que apanhas mostra-te, por um segundo, um bocadinho do teu mundo (uma rua, uma paragem de autocarro, uma cozinha). Juntá-los no Espelho Partido → **Espelho Mágico** para a casa (mostra o teu reflexo do mundo real: à noite, com pijama).

### R10_05 — Ecos de Casa
Dada pelo **Velho Fausto** (`andar_maximo >= 94`). Falas em `docs/dialogos/fausto.md`. **10 Fragmentos de Eco, um de cada região** (cada Eco deixa o fragmento da região de onde veio; o da região 10 vem de um Eco de Sombra) → **"A Crónica da Subida"** (livro na casa) · ❤️❤️ Fausto.

### R10_06 — O Tempo Perdido
(andar 95). As 4 **Árvores do Tempo** mudam de estação quando lhes tocas (Primavera → Verão → Outono → Inverno). Pô-las **as quatro em estações diferentes ao mesmo tempo** — mas as bolhas de tempo fazem algumas mudarem sozinhas: usa as bolhas lentas para as segurar → **Flor do Tempo** (acessório: imune a Parado; semente para a quinta).

### R10_07 — Os Perdidos (história) = **H_23**
| | |
|---|---|
| Quem dá | "Mãe Dois" (cena C10-07) |
| Recompensa | conta para os **finais** (cada Perdido convencido aparece no fim) · com os 5: título *Esperança dos Perdidos* e o **Cachecol da Mãe Dois** (cena C10-10) |

Cada Perdido convence-se **resolvendo a razão por que parou** (o Desistente dá as pistas, depois da C10-09). A ordem não importa.

| Perdido | O que fazer | Fala final |
|---|---|---|
| **Rafa** (5 150) | fazer a **R10_14** (a guitarra e a música) | `rafa_convencido` |
| **Doutor** (3 001) | dar-lhe **10 Fragmentos de Sistema** e ouvir as 3 portas (`doutor_finais_1` a `_3`) | `doutor_convencido` |
| **Bia** (6 080) | ter o **Último Posto aceso** (R10_01) e levá-la ao andar 92 pelo Caminho de Estrelas **sem deixar nenhum Devorador apagar a luz** (escolta: ela segue-te; se a luz apagar, ela foge para o cristal e recomeça) | `bia_convencida` |
| **Velho Ulisses** (4 444) | trazer-lhe uma **Flor do Prado** do pedaço da Floresta do andar 94 (o pedaço da região 1; a flor só existe lá) | `ulisses_convencido` |
| **Lino e Lia** (8 501 e 8 502) | jogar às escondidas: o Lino esconde-se num de 12 sítios do Bairro dos Números (muda cada vez); encontrá-lo **3 vezes** e levar a Lia ao último esconderijo | `gemeos_convencidos` |

⚙ Cada Perdido convencido soma 1 a `perdidos_convencidos` e muda-se para o **Último Posto** (dormem nas tendas; falas novas curtas: "Isto tem luz. Gosto disto.").

### R10_08 — A Nina
| | |
|---|---|
| Quem dá | Nina (`nina_04`, depois da C10-10) |
| Recompensa | **Nina** como companheira (maga de gelo; skill Nevão Pequeno) · ❤️ |

1. **Pedir** — `nina_04`. A Nina entra na equipa (conta como companheiro: se já tiveres 2, ela segue-te como terceira só nesta missão).
2. **Passo**: subir com ela os andares 98 e 99. **Em cada patamar da Escada Final** (C10-14) ela para e fala; tens de responder. Se responderes mal duas vezes seguidas, ela senta-se e volta ao 97 (recomeça a partir do último patamar onde falou).

| Patamar | Nina diz | Resposta certa | Resposta errada |
|---|---|---|---|
| 1.º | "E se lá em cima não houver nada?" | ▶ "Há o fim. Já é alguma coisa." | ▶ "Há de haver tudo." *(ela não acredita)* |
| 2.º | "Tenho frio. Não é do andar. É de dentro." | ▶ *(dar-lhe o casaco / a capa)* | ▶ "Não penses nisso." |
| 3.º | "Se eu desistir outra vez, vais ficar zangad{o/a}?" | ▶ "Não. Mas vou ficar à tua espera." | ▶ "Vou." |
| 4.º | "Nunca vi neve. No meu mundo. Sabias? Faço gelo e nunca vi neve." | ▶ "Quando isto acabar, vemos juntos." | ▶ "No andar 41 há muita." *(ela ri-se, mas não conta)* |

3. **Fim** — no Ponto Sem Retorno: `nina_05`.

### R10_09 — O Desistente
Ver a cena **C10-09**. Vencer **O Desistente** e ouvi-lo até ao fim → **Arco do Desistente** · ele dá as pistas da R10_07.

### R10_10 — O Diário de A. = **H_24**
Ver as cenas **C10-11** e **C10-12**. Ter **90 ou mais** páginas e entregá-las à Arquivista → o nome **Aren** · flag `sabe_nome_aren` · conta para o **final secreto**.

### R10_11 — Armas Míticas (12 partes)
Dorn + Brom. Cada mítica: **10 Lingote Estelar + 1 Coração Estelar + 1 Gema Prismática** (ver `docs/ARMAS.md`, secção 9). O Dorn faz o corpo na Forja Estelar; o **Brom** dá o toque final em Ascendia (`brom_serv_mitica`). As 12 → título *Lenda Forjada*.

### R10_12 — O Nome Raspado
Dada pela **Capitã Freya** (rank SS; = `G_SS_02`) ou ao encontrar o Jogador Sem Número. Ver a cena **C10-13**. Ouvi-lo até ao fim da luta → **Máscara Sem Número** · página especial **"O Nome Raspado"** · flag `ouviu_sem_numero`.

### R10_13 — O Devorador Ancestral
Dada pela **Capitã Freya** (rank SS; = `G_SS_01`). Falas em `docs/dialogos/freya.md`. O **Devorador Ancestral** (andares 92 e 99; 3%; 30% com a missão) come as estrelas do céu do andar: o andar escurece; apanhar **fragmentos de luz** do chão e atirar-lhos à boca quando a abre → **Coração Estelar** · 15 000 ouro · título *Guardião das Estrelas*.

### R10_14 — A Última Música
| | |
|---|---|
| Quem dá | Rafa |
| Recompensa | música **"Casa"** para o gira-discos da casa · o Rafa fica convencido (R10_07) |

1. **Pedir** — `rafa_03`.
2. **Passo 1**: **3 Madeira do Tempo + 2 Fio de Luz Estelar** para a guitarra (o Dorn ou o Gizmo fazem-na: 1 dia).
3. **Passo 2**: tocar com ele na praça: **minijogo de ritmo** (como o do Lucien, mas a 2 vozes: tu fazes as notas de baixo). Precisa de 80% de acertos.
4. **Entregar** — 🎬 a praça enche-se de Perdidos a ouvir. Ninguém aplaude. Depois a Mãe Dois aplaude sozinha, devagar, e a praça inteira segue-a. `rafa_04`.

### R10_15 — A Mini-Estrela
Dada pelo **Zed**. Falas em `docs/dialogos/zed.md`. No Planeta Pequeno (andar 92), dar **uma volta completa a andar sem parar** abre um alçapão: lá dentro, uma estrela bebé do tamanho de uma maçã, a chorar luz → **Mini-Estrela** (animal de estimação).

---

## 5. Missões da Guilda (rank SS) da região

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_SS_01 O Devorador Ancestral (R10_13) | "Avistado nos andares 92 e 99: criatura que come estrelas. Tamanho: o andar inteiro. Recompensa: a maior de sempre." | "Rank SS. Nunca carimbei um SS. Olha, a mão está a tremer. Não é medo. É… é medo." | "Comeste… quer dizer, venceste uma coisa que come estrelas. Vou escrever isto devagar para não me enganar nas letras." |
| G_SS_02 O Nome Raspado (R10_12) | "Procura-se: Jogador sem número, de máscara branca. Visto raramente nos andares 93, 97 e 99. Não atacar primeiro. Ouvir." | "'Ouvir.' A Capitã escreveu 'ouvir' num cartaz de caça. Nunca a vi fazer isso. Isto deve ser importante." | "Simão. Tinha nome. Toda a gente tem nome. Vou escrevê-lo no registo, no sítio onde estava o ponto de interrogação." |
| G_SS_03 20 Monstros com Nome | "Vencer os 20 monstros com nome da torre. Todos. Sim, todos." | "Vinte! Tenho uma lista. Fiz uma lista. Fiz duas listas, uma com desenhos. Toma a dos desenhos." | "Os vinte. Vou ter de arranjar uma parede nova para os cartazes. Ou uma sala. Ou uma Guilda nova." |
