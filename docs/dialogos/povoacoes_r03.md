# Povoações da Região 3 — diálogos e missões

Os NPCs que vivem nos andares 21–30 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r03_pantano.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap03_pantano.md`.

---

## 1. Aldeia Sssar (andar 24) — dos Homens-Lagarto

Primeira chegada: cena **C3-03**. A escolha da Ordem da Guilda (cenas C3-04 e C3-05) decide o que acontece à aldeia:

| Estado | Como fica a aldeia |
|---|---|
| **Antes da escolha** (H_08 ativa) | os NPCs estão todos lá, desconfiados; só falam as falas marcadas `antes` · a loja da Zith está **fechada** ("Primeiro decide. Depois compra.") · a cabana de hóspedes está aberta |
| **`sssar_defendida`** (B) | aldeia **amiga**: loja, cabana, cristal, Festa na Aldeia, missões R3_03, R3_04, R3_05 e R4_15 |
| **`sssar_expulsa`** (A) | a aldeia fica com **Renegados** (inimigos, pinturas vermelhas). Ilssa, Kesh e Zith partem com o Ssark. As missões R3_03, R3_04, R3_05 e R4_15 **perdem-se**. O cristal continua a funcionar, mas há sempre 4–6 Renegados à volta |

**Como falam**: os Homens-Lagarto **sibilam**, esticam os "s" ("Sssim", "issso"). No texto, escreve-se só um ou dois
"s" a mais, para ler bem. Chamam aos humanos **"os da janela"**. Bips: graves e com um silvo no fim.

### 1.1 Chefe Ssark

| | |
|---|---|
| Voz | bips muito graves e lentos; um silvo comprido no fim de cada frase |
| Quem é | o mais velho guerreiro de Sssar, enorme, escamas verde-escuras quase pretas, uma **cicatriz no focinho** (de uma luta com a Mãe-Crocodilo Mandíbula, há 40 anos: "ela ficou com um dente meu, eu fiquei com um dela"). Honrado, paciente, seco. Tem um colar com um dente de crocodilo |
| Repete | "Os Ssar não pedem. Só esperam.", "Assim sseja.", "Um da janela." |
| Família | a mulher morreu de febre há muitos anos; os filhos são "toda a aldeia" |
| Companheiro | depois de R3_03 (tanque com lança e escudo; skill **Muralha de Escamas**). Ver secção 1.6 |

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `ssark_antes_01` | `antes` | normal | "Olhas para os nossos totens como quem conta lanças. São só totens. Contam histórias, não lanças." |
| `ssark_antes_02` | `antes` | triste | "Os nossos filhos perguntam porque é que os da janela nos odeiam. Digo-lhes que não odeiam. Que só têm medo. É quase o mesmo." |
| `ssark_01` | — | normal | "Bom dia, Jogador{/a}. A lagoa está calma. Isso é bom. Ou é mau. Nunca se sabe com a lagoa." |
| `ssark_02` | — | normal | "Os novos querem lutar. Os velhos querem dormir. Eu quero as duas coisass. Por essa ordem." |
| `ssark_03` | — | feliz | "O Kessh caçou um crocodilo sozinho ontem. Pequeno. Mas sozinho. Não lhe digas que eu disse. Fica vaidoso." |
| `ssark_04` | `hora entre 5 e 7` | normal | "Ao nascer do ssol, os Ssar molham a cabeça na Lagoa Sagrada. Para lembrar que viemos da água. E que lá voltamos." |
| `ssark_05` | `hora entre 20 e 23` | normal | "À noite, a velha Ssilsa canta. É a canção do Primeiro Rei. Não percebes as palavras. Ninguém percebe. É muito velha." |
| `ssark_06` | `clima == chuva` | feliz | "Chuva! Boa para as escamass. Os da janela fogem dela. Nunca percebi porquê." |
| `ssark_07` | `boss_derrotado(serpente_lodo)` | surpresa | "Mataste a Ssserpente do templo. Os nossos avós rezavam-lhe. Os nossos pais tinham medo dela. Nós… não sabemos o que sentir." |
| `ssark_08` | `boss_derrotado(hidra)` | feliz | "A Que Come os Reis morreu. Hoje à noite, toda a aldeia come peixe em tua honra. Tu também. É obrigatório." |
| `ssark_09` | `missao(R3_11) == concluida` | feliz | "A Mandíbula. Morta. Quarenta anos e ainda me doía o focinho quando chovia. Hoje não dói. Obrigado." |
| `ssark_10` | `companheiro(ssark)` no andar 24 | normal | "Em casa. Os pequenos vão querer tocar no teu… no que trazes às costas. Deixa-os. Tocam em tudo." |
| `ssark_curta` | já falaste hoje | normal | "Sssim?" |

**Perguntar sobre…**
- *A aldeia*: "Sssar quer dizer 'os que ficam'. Os nossos avós vieram de baixo, de um mar que não conhecemos. Pararam aqui. Ficaram."
- *Os Renegados*: "O chefe deles chama-sse Krass. Queria levar a aldeia a assaltar os da janela. Por ouro. Eu disse não. Ele levou trinta dos nossos jovens. Ainda dói."
- *Os da janela*: "Passam muitos. Sobem, sobem. Poucos voltam a passar a descer. Um deles, há muitos anos, ensinou-nos a fazer canoas mais leves. Não disse o nome. Os da janela nunca dizem o nome. Dizem números."
- *A torre*: "Os avós diziam: a torre é uma árvore e nós somos os bichos que vivem nos ramos. Ninguém pergunta à árvore porque cresce."

### 1.2 Xamã Ilssa — curandeira

| | |
|---|---|
| Voz | bips suaves e roucos, a sibilar baixinho, como quem conta um segredo |
| Quem é | velha Homem-Lagarto de escamas cinzentas, coberta de colares de ossinhos e conchas. Cura com ervas e cantigas. Tem medo de sal ("o sal seca as escamas e a alma") mas usa-o contra as sanguessugas |
| Serviços | cura estados (50 ouro) · ensina a **Poção de Escamas** (R3_04) |
| Amizade | **corações simples** (só para R4_15): +20 por conversa, +45 por presente de Lírio do Pântano ou Musgo Medicinal |

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `ilssa_antes_01` | `antes` | normal | "Ssenta-te. Tens cara de quem não dorme. Ninguém dorme bem com um papel daqueles na mochila." |
| `ilssa_01` | — | normal | "As ervas falam. Esta diz 'come-me'. Esta diz 'não me comas'. Aprende a ouvi-las e nunca adoeces." |
| `ilssa_02` | — | feliz | "Os teus pés estão molhados há três dias. Vê-se. Ssecam-se ao fogo, não com esperança." |
| `ilssa_03` | `estado(veneno)` | normal | "Envenenad{o/a}. Sapo, pelo cheiro. Bebe isto. Sabe a lodo. É lodo. Funciona." |
| `ilssa_04` | `estado(amaldicoado)` | séria | "Uma bruxa tocou-te. Tira as botas. Não, não é para a cura. É porque cheiras mal. A cura é depois." |
| `ilssa_05` | `missao(R4_15) == concluida` | feliz | "O teu sal! Agora as sanguessugas fogem dos nossos pequenos. Mandei fazer saquinhos para toda a gente." |
| `ilssa_curta` | já falaste hoje | normal | "Dói alguma coisa? Não? Então volta quando doer." |

**Perguntar sobre…**
- *A Escama do Primeiro Rei*: "Está no fundo da Lagoa Sagrada. Quem a encontra não teme veneno. Mas tem de respirar debaixo de água. Os da janela não sabem. Há uma poção para isso."

### 1.3 Kesh — jovem caçador

| | |
|---|---|
| Voz | bips rápidos e agudos para um lagarto; sibila mais quando se irrita |
| Quem é | 17 anos (em idade de lagarto: "quase adulto"), escamas verde-claras, arco às costas. Orgulhoso, competitivo, desconfiado dos humanos. O irmão mais velho, **Rakk**, foi com os Renegados — por isso odeia o Krass e tem medo de ser comparado com o irmão |
| Repete | "Aposto que não consegues.", "Eu sabia!" |
| Arena | depois de R3_05 aparece no ranking da Arena de Ascendia (Prata), só com `sssar_defendida` |

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `kesh_antes_01` | `antes` | zangado | "Estou a ver-te. Estou SEMPRE a ver-te. Até quando durmo. Durmo com um olho aberto. Os lagartos conseguem." |
| `kesh_01` | — | normal | "Aposto que não consegues acertar naquele sapo daqui. …Eu também não. Mas aposto que tu falhas por mais." |
| `kesh_02` | — | normal | "O chefe diz que os da janela não são todos iguais. Estou a decidir se tu és diferente. Ainda não decidi." |
| `kesh_03` | `missao(R3_05) == concluida` | feliz | "Ganhaste-me. UMA vez. A próxima ganho eu. Ou a seguir. Um dia." |
| `kesh_04` | `missao(R3_03) == concluida` | triste | "No acampamento… vi o meu irmão. O Rakk. Fugiu antes de lutarmos. Ainda bem. Não sei o que fazia se lutasse com ele." |
| `kesh_05` | `boss_derrotado(hidra)` | surpresa | "A Hidra?! Sozinh{o/a}?! …Ensinas-me? Não. Esquece. Não disse nada." |
| `kesh_curta` | já falaste hoje | normal | "Ainda aqui? Os da janela não têm torre para subir?" |

**Perguntar sobre…**
- *O irmão*: "O Rakk era o melhor caçador da aldeia. Melhor do que eu. O Krass disse-lhe que lá fora havia ouro para quem fosse forte. O Rakk era forte. Não era esperto."

### 1.4 Zith — mercadora

| | |
|---|---|
| Voz | bips médios, saltitantes, sibila nas palavras de dinheiro ("ouuuro", "dessconto") |
| Quem é | Homem-Lagarto de escamas vermelhas e amarelas, muito faladora, troca com os sapos da Vila Coaxa de canoa. Conhece os preços de tudo, de todos os andares de 21 a 30 |
| Loja | escamas, armas tribais de aço, Pimenta da Selva, sementes de Café e Pimenta, **Água de Coco** (ver `docs/LOJAS.md`, secção 3.4) · ensina o **Caril da Selva** com 2 corações simples (+20 por compra, +45 por presente de Banana) |

| ID | Condição | Fala |
|---|---|---|
| `zith_antes` | `antes`, abrir loja | "Fechado. Primeiro decide. Depois compra. Os mortos não compram e os expulsos não voltam." |
| `zith_01` | abrir loja | "Ouuuro! Quer dizer… bem-vind{o/a}! Tudo fresco! Exceto o que é seco. Isso é seco." |
| `zith_02` | comprar | "Bom negócio! Para os dois! Mais para mim, mas não faz mal." |
| `zith_03` | vender escamas | "Escamas de renegado? Não pergunto de onde vêm. Sei de onde vêm. Pago na mesma." |
| `zith_04` | `clima == sol` e `hora entre 12 e 16` | "Calor! Água de Coco! Dois por um! …Mentira, é um por um. Mas é muito boa." |
| `zith_05` | ensinar receita | "Caril da Selva. Pimenta, carne, arroz. E mais pimenta. Se não chorares, não está pronto." |

### 1.5 Aldeões Sssar (sem nome)

| ID | Quem | Fala |
|---|---|---|
| `sssar_crianca_01` | criança-lagarto | "És mesmo da janela? Mostra a janela! …Não tens? Que aldrabice." |
| `sssar_crianca_02` | criança-lagarto | "Eu nado mais depressa do que tu. E sou pequeno. Imagina quando for grande." |
| `sssar_guerreiro_01` | guerreiro | "Sssim, Jogador{/a}. Passa. Não toques nas canoas. Nem nos totens. Nem em mim." |
| `sssar_velha_ssilsa` | velha Ssilsa (à noite, a cantar) | *(canta numa língua antiga; legenda)* "♪ …o Rei desceu da água… pôs a coroa no fundo… para que ninguém a levasse… ♪" |
| `sssar_pescador_01` | pescador | "Os sapos de Coaxa pescam com a língua. Nós com lança. Os da janela com um pau e um fio. Todos se riem uns dos outros." |

### 1.6 Ssark como companheiro

| Momento | Fala |
|---|---|
| entrar na equipa | "Vou contigo. A aldeia fica com o Kessh. Que os avós a protejam. E ao Kessh." |
| começar uma luta | "Atrás do escudo!" · "Os Ssar não recuam." · "Este é meu. Aquele também." |
| usar **Muralha de Escamas** | "Muralha!" |
| herói com pouca vida | "Para trás, Jogador{/a}! Eu aguento!" |
| matar um Renegado | "Era dos nossos. Já não era." |
| ver um crocodilo | "Ssss. Esses lembram-se de mim." |
| chuva | "Ahh. Chuva." |
| frio (região 5) | "Frio… os lagartos… dormem… no frio… acorda-me… se for importante…" (fica 10% mais lento) |
| andar novo | "Nunca tinha subido tanto. Os avós não acreditavam. Eu também não." |
| sair da equipa | "Volto para a aldeia. Chama-me pelo cristal. Os Ssar vêm sempre." |

### 1.7 Festa na Aldeia (só com `sssar_defendida`)

| | |
|---|---|
| Quando | dia 14 de cada estação, 10:00–22:00 |
| O que há | **corrida de canoas** (desafio do andar 24), espetadas de peixe e crocodilo, danças à volta das fogueiras, e a **loja especial** da Zith (1 Escama do Primeiro Rei de imitação: cosmético; Totem Pequeno: móvel) |
| Corrida de canoas | minijogo: 3 voltas à Lagoa Sagrada contra o Kesh e 2 guerreiros. Remar = carregar em [atacar] ao ritmo do tambor (verde = certo). Bater nas estacas atrasa 1 s. Prémio: 500 ouro e, na 1.ª vitória, a **Canoa Sssar** (móvel de decoração) |

- **Ssark** *(ao começar)*: "Remem como se a Hidra viesse atrás. E se a Hidra vier atrás… remem mais."
- **Kesh** *(se ganhares)*: "Batota! Não sei como, mas foi batota!" · *(se ele ganhar)*: "EU SABIA!"

---

## 2. Vila Coaxa (andar 26) — dos Homens-Sapo

Primeira chegada: cena **C3-07**. Os Homens-Sapo são **comerciantes e cómicos**: falam alto, riem-se muito, coaxam no
fim das frases quando estão contentes ("croac!"). Bips: borbulhantes. À noite (21:00–23:00) o **Coro dos Sapos** canta no
palco de nenúfar (com o tenor, depois de R3_06).

### 2.1 Barão Coaxim

| | |
|---|---|
| Voz | bips gordos e lentos, com um "croac" grave no fim de cada frase |
| Quem é | o sapo mais rico do pântano: colete dourado, monóculo, leque de folha de palmeira. Compra tesouros raros e coleciona-os na sua "Galeria" (um nenúfar só para ele). **Fala sempre em rimas**. Quando fica sem rima, entra em pânico |
| Repete | "Ora viva, ora viva!", "…e quem não rima, desafina!" |
| Loja | compra **tesouros** (Pele Dourada, Dente de Mandíbula, Âmbar com Mosquito, e mais tarde a Pinça de Ouro, R6_12) por mais do que ninguém · depois de R3_07 vende **itens raros** (ver `docs/LOJAS.md`, secção 3.4) |

| ID | Condição | Fala |
|---|---|---|
| `coaxim_01` | — | "Bom dia, bom dia, que dia tão belo! Traz-me um tesouro e dou-te um castelo! …Um castelo não. Mas dou-te dinheiro. Croac!" |
| `coaxim_02` | — | "O ouro é amarelo, o sapo é verde, quem guarda o seu ouro nunca o perde!" |
| `coaxim_03` | — | "A minha Galeria é a mais bela do pântano inteiro: tem pedras, tem peles, e um sapo de ouro… que sou eu, no espelho. Croac!" |
| `coaxim_04` | `clima == chuva` | "Chove na vila, chove no lago, chove no Barão… e o Barão fica pago! …Não fica pago. Fica molhado. Rimei mal. Ai." |
| `coaxim_05` | `hora entre 21 e 23` | "Ouve o meu coro, que bela cantoria! …Sem o tenor é uma gritaria." *(antes de R3_06)* |
| `coaxim_06` | `missao(R3_06) == concluida` | "Com o tenor de volta, o coro é divino! Até eu choro, e eu sou… sapino? Sapuno? Sapeiro? …Croac." |
| `coaxim_07` | `missao(R3_07) == concluida` | "Na Galeria, o meu Ídolo brilha! Ou os tesouros! Brilha a família! …A família não. Ai, a rima." |
| `coaxim_08` | `missao(R3_15) == concluida` | "Deste o Ídolo ao velho dos livros?! Um ídolo lido não vale um tostão! …Mas está bem. Ele chorou? Então valeu, então." |
| `coaxim_09` | `boss_derrotado(hidra)` | "A Hidra caiu, a Hidra morreu, e o pântano inteiro já te agradeceu! Um brinde, um brinde, croac e mais croac!" |
| `coaxim_curta` | já falaste hoje | "Outra vez por cá? Que alegria, que bom! Tens tesouro? Não? Então… adeus, bom tom." |
| `coaxim_sem_rima` | 1 em 20 conversas | "Hoje o tempo está… está… laranja? Não. Está… *(entra em pânico)* CROAC! Volta amanhã!" |

**Perguntar sobre…**
- *Tesouros*: "Pele de sapo dourado, dente de crocodilo velho, âmbar com bicho dentro… Traz-me isso e dou-te um conselho. E ouro. Mais ouro do que conselho."
- *O Ídolo de Jade*: "Nas ruínas da selva, um ídolo verde, quem o encontrar com o Barão não perde! Três mil moedas, palavra de sapo!"
- *A torre*: "A torre é alta, a torre é escura, e cá em baixo há sapos com muita cultura!"

### 2.2 Rã-Rã — pescadora

| | |
|---|---|
| Voz | bips curtos e secos; fala pouco; ri-se só quando apanha peixe |
| Quem é | rã magrinha e calada, de chapéu de palha furado. **Pesca com a língua** (é muito rápida: 0,2 s). Campeã do Concurso de Pesca de Coaxa há 11 anos. Treina o Sapinho, que é "o sobrinho da sobrinha da sobrinha" dela |
| Organiza | **Concurso de Pesca de Coaxa** (R3_16), todos os dias às 7:00 e às 17:00 |

| ID | Condição | Fala |
|---|---|---|
| `raraa_01` | — | "Shh. Os peixes ouvem." |
| `raraa_02` | — | *(apanha um peixe com a língua, sem olhar)* "…Doze." |
| `raraa_03` | estás a pescar ao pé dela | "Cana. Hmm. Língua é melhor. Mas não tens língua para isso. Ninguém tem." |
| `raraa_04` | depois de pescares um raro no andar 26 | "…Bom peixe." *(é o maior elogio que ela faz)* |
| `raraa_05` | `missao(R3_16) == concluida` | "Ganhaste. Onze anos. Acabou." *(pausa)* "…Amanhã outra vez?" |
| `raraa_06` | `hora entre 21 e 23` e `clima == chuva` | "Hoje o Velho Bigodes sobe. Maré alta, noite, chuva. Eu nunca o apanhei. Ninguém apanhou." |

### 2.3 Doutor Girino — inventor de poções

| | |
|---|---|
| Voz | bips agudos, aos saltos, com pausas estranhas no meio das frases |
| Quem é | sapo pequenino que ainda tem um bocadinho de **cauda de girino** (tem vergonha: usa uma bata comprida para a esconder). Óculos de garrafa. Inventa poções misturando tudo o que encontra. Já explodiu o laboratório 14 vezes |
| Loja | **Poções Surpresa** (100 ouro, efeito ao acaso, secção 4: R3_08) · depois de R3_08, Poção Arco-Íris (1 200) |

| ID | Condição | Fala |
|---|---|---|
| `girino_01` | — | "Ciência! É quando misturas coisas e… vês. O que acontece. Às vezes acontece fogo." |
| `girino_02` | — | "Esta poção faz-te… voar? Ou faz-te… sapo. Uma das duas. Ou as duas! Seria um sapo voador! Para a ciência!" |
| `girino_03` | — | *(se olhares muito para ele)* "Não estou a olhar para a minha cauda. Tu é que estás. Não tenho cauda. É a bata." |
| `girino_04` | `estado(sapo)` | "UM SAPO! Bem-vind{o/a} à família! …Ah, és tu. Dura três segundos. Aproveita." |
| `girino_05` | `missao(R3_08) == concluida` | "Sobreviveste a cinco! Recorde! O último ficou às bolinhas uma semana. Bolinhas roxas. Era bonito." |
| `girino_06` | `clima == trovoada` | "Trovoada! Bom tempo para experiências! O raio dá… energia! E cabelo! Eu não tenho cabelo! Ainda!" |

### 2.4 Coro dos Sapos

| | |
|---|---|
| Quem são | **Croque** (baixo, gordo e solene), **Ribito** (barítono, sempre a afinar) e **Dona Lili** (soprano, dramática). O tenor, **Bufo**, perdeu-se há um mês: foi apanhar flores "para inspirar a voz" e não voltou |
| Onde | palco de nenúfar (canta das 21:00 às 23:00) |

| ID | Condição | Fala |
|---|---|---|
| `coro_01` | antes de R3_06 | **Dona Lili** *(dramática)*: "Sem o Bufo, o nosso dó de peito é um dó de… pé. Um dó de pé!" |
| `coro_02` | antes de R3_06 | **Croque**: "Croooac." *(quer dizer "tenho saudades dele"; o Ribito traduz)* |
| `coro_03` | depois de R3_06 | **Bufo**: "Desculpem o atraso! Fui buscar inspiração! Fiquei preso dentro de uma flor um mês! Muito inspirador!" |
| `coro_04` | depois de R3_06, à noite | 🎵 o coro canta `coaxa_coro` (4 vozes). Ver a canção na secção 4, R3_06 |

### 2.5 Outros Homens-Sapo

| ID | Quem | Fala |
|---|---|---|
| `remo_01` | **Velho Remo** (barqueiro, aluguer de barcos) | "Barco: 50 moedas por dia. Devolve-o com o fundo para baixo. O último devolveu-mo com o fundo para cima." |
| `remo_02` | Velho Remo, maré baixa | "Maré baixa. Barco não serve. Anda na lama. Cuidado com os buracos. Têm caranguejos." |
| `bolha_01` | **Dona Bolha** (estalagem-nenúfar) | "Quarto-nenúfar: 30 moedas. A cama mexe-se um bocadinho. É a água. Habituas-te. Ou enjoas." |
| `coaxa_vendedor_01` | sapo vendedor | "Moscas fritas! Moscas cozidas! Moscas cruas para os puristas! …Não comes moscas? Coitad{o/a}." |
| `coaxa_vendedor_02` | sapo vendedor | "Croac! Leque de folha! Para o calor! Para o Barão! Para ti!" |
| `coaxa_girinos` | 3 girinos a nadar | "Olha, um da janela! Ele não tem guelras! Não tem guelras!" *(riem-se e mergulham)* |

---

## 3. Refúgio das Copas (andar 28)

Posto de exploradores de Ascendia a 30 m de altura. Primeira chegada: sobe-se pelas lianas do Chão da Selva e
o primeiro a falar contigo é o Tom. Plataformas, redes, um telescópio virado para cima.

### 3.1 Vera Liana — cartógrafa

| | |
|---|---|
| Voz | bips rápidos e precisos; fala por números |
| Quem é | 40 anos, de Ascendia, cabelo apanhado com um lápis, mapas enrolados às costas. Andou com a Freya há anos; ficou cá em cima porque "aqui vê-se tudo". Paga a exploração: cada **1% novo** de um andar explorado vale **5 ouro** (uma vez por andar; 100% = 500 ouro) |
| Serviço | vende mapas dos andares 21–30 (mostram as zonas) · paga a exploração · missão R3_09 |

| ID | Condição | Fala |
|---|---|---|
| `vera_01` | — | "Andar 28: 240 por 240 metros, 30 de altura, 14 pontes, 6 tirolesas. Três delas não funcionam. Ainda." |
| `vera_02` | — | "Mapas! Trazes-me o que vês, eu desenho. Tu ganhas ouro, eu ganho papel. O papel vale mais. Mas não te digo." |
| `vera_03` | — | "Olha pelo telescópio. Para cima. O que é aquilo?" *(o herói olha)* "Exato. Não é céu. São raízes. Do andar 29. O nosso céu é o chão de alguém." |
| `vera_04` | `andar_maximo >= 31` | "Deserto? Areia que se mexe? Como é que se faz um mapa de uma coisa que se mexe? …Com muito lápis." |
| `vera_05` | `missao(R3_09) == concluida` | "Cem por cento dos dois! O meu mapa da selva está completo. Primeira vez em vinte anos. Vou emoldurá-lo. E chorar um bocadinho." |
| `vera_curta` | já falaste hoje | "Trouxeste mapa? Não? Então trouxeste-me o quê? Conversa? Não paga." |

**Perguntar sobre…**
- *A Freya*: "Fizemos o pântano juntas, há quinze anos. Ela lutava, eu desenhava. Diz-lhe que ainda tenho o mapa onde ela escreveu 'Aqui caí na lama'."
- *Mapas antigos*: "No Refúgio havia um mapa velhíssimo quando cheguei. Ia até ao andar 40. Tinha um desenho de uma janela no canto. Perdi-o num temporal. Ainda me dói."

### 3.2 Tom Tirolesa — construtor

| | |
|---|---|
| Voz | bips alegres e altos, com um "IUUUPI" sempre que desce numa corda |
| Quem é | 25 anos, de Ascendia, magro, com cordas à cintura e capacete de casca de coco. Construiu metade das pontes do Refúgio. Quer ligar a selva toda com tirolesas |

| ID | Condição | Fala |
|---|---|---|
| `tom_01` | 1.ª vez | "Ei! Subiste pelas lianas? À mão? És doid{o/a}! Gosto! Bem-vind{o/a} ao Refúgio!" |
| `tom_02` | — | "Andar a pé é para quem não tem corda. Eu tenho muitas cordas." |
| `tom_03` | — | "Caí doze vezes este ano. Cá para baixo. Lá em baixo há flores que comem pessoas. Elas não gostam de mim. Sou muito ossudo." |
| `tom_04` | `missao(R3_10) == concluida` | "IUUUPI! Seis tirolesas! A selva inteira de corda! Experimenta a grande! É a mais rápida! É a mais assustadora!" |
| `tom_05` | `clima == trovoada` | "Hoje não há tirolesas. Corda molhada mais raio é igual a Tom frito." |

### 3.3 Irmã Nara — enfermeira

| | |
|---|---|
| Voz | bips calmos e doces, com um suspiro de vez em quando |
| Quem é | 30 anos, irmã da Igreja de Ascendia, mandada pela **Irmã Célia** para tratar os exploradores. Tem medo de alturas (ri-se disso). Escreve todas as semanas à Célia |
| Serviço | vende poções (Vida, Purificadora, Antídoto) e cura estados (30 ouro) |

| ID | Condição | Fala |
|---|---|---|
| `nara_01` | — | "A Irmã Célia mandou-me para cá porque 'és a que tem mais paciência'. Não me disse que era a 30 metros. Ela sabia." |
| `nara_02` | — | "Não olhes para baixo. Eu não olho para baixo há dois anos. Já não sei como é o chão." |
| `nara_03` | `vida_pct < 30` | "Senta-te. Não, aí não, que é a beira. Aqui. Bebe. Respira. Não olhes para baixo." |
| `nara_04` | `estado(veneno)` | "Sapo? Flor? Bruxa? Não digas. O antídoto serve para os três. Menos para a bruxa. Para a bruxa é rezar." |
| `nara_05` | `coracoes(celia) >= 6` | "A Irmã Célia fala de ti nas cartas. Diz que és boa pessoa. Diz isso de pouca gente. Diz isso de mim às vezes." |

---

## 4. Missões da região, passo a passo

### R3_01 — Repara os Passadiços
| | |
|---|---|
| Quem dá | quadro da Guilda (rank C; = `G_C_03`) |
| Recompensa | 300 ouro · 80 pontos · **atalho** no andar 21 (passadiço novo da entrada até à escada) |

1. **Quadro** — `"Os passadiços do andar 21 estão podres. A Guilda precisa de 20 Madeira de Mangue para os reparar. Mangue não apodrece."`
2. **Passo**: entregar **20 Madeira de Mangue** (andares 21 e 26, com machado) na Guilda.
3. **Entregar** — **Lyra**: "Vinte! Os carpinteiros sobem amanhã. Pediram-te para não caíres mais nos buracos antigos. Ficam tristes."
4. ⚙ Ao voltar ao andar 21: um passadiço novo, de mangue escuro, liga a entrada à escada. `[Sistema] Atalho aberto.`

### R3_02 — Ordem da Guilda (história)
Ver as cenas **C3-02 a C3-05** em `docs/guiao/cap03_pantano.md`.

### R3_03 — Os Renegados
| | |
|---|---|
| Quem dá | Chefe Ssark (só na escolha **B** da R3_02) |
| Recompensa | **Ssark** como companheiro · **Lança de Ssark** (rara) · prova para a Guilda (insígnia vermelha) |

1. **Pedir** — cena C3-05B: o herói rasga a ordem. **Ssark**: "Rassgaste um papel da Guilda. Vamos dar-lhes uma razão para ficarem contentess."
2. **Passo 1 — O caminho**: atravessar a lagoa até ao **Acampamento Renegado** com o Ssark e o Kesh (companheiros temporários). Puzzle das **canoas** (levar 3 canoas até à margem certa para fazer uma ponte).
   - **Kesh** *(a remar)*: "Se o meu irmão lá estiver… não lhe batas na cabeça. É a única coisa que ele tem boa."
3. **Passo 2 — O acampamento**: paliçada com 3 grupos de Renegados (pinturas vermelhas). No meio, o **Totem Vivo de Sssar**, roubado e pintado de vermelho, acorda (luta de guardião).
   - **Ssark** *(zangado)*: "O nosso totem! Pintaram-no de ssangue! Os avós devem estar a morder as caudas!"
4. **Passo 3 — O Campeão**: o próprio **Krass**, o **Campeão Renegado** (Elite), desafia o herói para um duelo. Ganhar o duelo cumpre também o desafio do andar.
   - **Krass** *(zangado)*: "Ssark, velho! Trouxeste um da janela para lutar por ti? Os Ssar já não têm dentes?"
   - **Ssark** *(normal)*: "Os Ssar têm amigos. Tu tens pinturas."
   - 🎬 Durante a luta, um Renegado jovem (o **Rakk**) foge pelo mangue. O Kesh vê-o e não dispara.
5. **Entregar** — o Krass cai de joelhos. O Ssark arranca-lhe a **insígnia vermelha**; ao lado, um saco com bússolas e cantis da Guilda.
   - **Ssark** *(normal)*: "Vai, Krass. Para cima. Para longe. Se voltares, não falo eu. Fala a lança."
   - 🎬 O Krass foge pelo mangue com os últimos Renegados. Continua na cena C3-05B (Gorvan).
6. ⚙ Depois da cena na Guilda, o Ssark dá a **Lança de Ssark**: "Era do meu pai. Agora é de quem defendeu os filhos dele." e oferece-se como **companheiro**.

> Na escolha **A**, o Krass e os Renegados ficam com a aldeia. Os Renegados que ainda aparecem nos andares 21–25 (com B) são os que fugiram com ele.

### R3_04 — Escamas Fortes
| | |
|---|---|
| Quem dá | Xamã Ilssa |
| Recompensa | receita **Poção de Escamas** (+DEF) |

1. **Pedir** — **Ilssa**: "Os da janela têm a pele fina como folha. Faço-te uma poção que dá escamas por um bocadinho. Preciso de escamas. E de lírios, para não cheirar a lagarto."
2. **Passo**: entregar **10 Escama de Lagarto** (Homem-Lagarto Renegado, 50%) **+ 5 Lírio do Pântano** (andares 21 e 22).
3. **Entregar** — 🎬 a Ilssa mexe um caldeirão a cantar. Sai fumo verde. Ela prova e faz uma careta. **Ilssa** *(feliz)*: "Perfeito. Sabe mal. As boas sabem sempre mal. Toma, aprende."

### R3_05 — Caçada com o Kesh
| | |
|---|---|
| Quem dá | Kesh |
| Recompensa | **Arco Tribal de Aço** (raro) · o Kesh entra no ranking da Arena |

1. **Pedir** — **Kesh**: "Aposto que caço dez sapos antes de ti. Andar 22. Os venenosos. Se ganhares, dou-te o meu arco. Não vais ganhar."
2. **Passo**: corrida no **andar 22**: matar **10 Sapos Venenosos** antes do Kesh. O contador dele aparece no ecrã (1 sapo a cada 25 s; total ≈ 4 min). O Kesh caça na mesma zona e às vezes "rouba" um sapo que estavas a atacar (se não lhe deres o último golpe, conta para ele).
   - *(Kesh vai à frente)* **Kesh**: "Seis! Estás a dormir?"
   - *(estás à frente)* **Kesh**: "Isso não conta! Esse estava doente!"
3. **Entregar**
   - *(ganhas)* **Kesh** *(zangado, depois sorri)*: "…Toma. O arco. Era do Rakk. Ele nunca mo deixou usar. Agora não o uso eu. Usa-o tu. Bem."
   - *(perdes)* **Kesh** *(feliz)*: "EU SABIA! Amanhã outra vez? Gosto de ganhar." ⚙ pode repetir-se no dia seguinte

### R3_06 — O Quarto Cantor
| | |
|---|---|
| Quem dá | Coro dos Sapos (Vila Coaxa, à noite) |
| Recompensa | concerto à noite · **Ocarina** (tocar ao pé da água atrai peixes raros: +20% de raros durante 3 min, 1 vez por dia) |

1. **Pedir** — **Dona Lili** *(dramática)*: "O nosso Bufo foi buscar flores há um mês! Para a voz! Nunca mais voltou! Encontra-o, Jogador{/a}! Antes que o nosso coro morra de… desafinação!"
2. **Passo 1**: procurar no **andar 29**. Pistas: no Jardim Devorador, de 30 em 30 m, ouve-se um "dó" abafado (o som fica mais alto perto da **Estufa Natural**).
3. **Passo 2**: na Estufa, uma **flor carnívora gigante fechada** canta. Bater-lhe 3 vezes com fogo (ou uma Bomba de Fogo) para ela abrir sem morder.
   - **Bufo** *(de dentro da flor)*: "♪ Dóóó… ♪ Oh! Uma pessoa! Uma pessoa a sério! Tira-me daqui! Mas devagar! Estou a meio de uma nota!"
4. **Passo 3**: escoltar o Bufo até ao cristal do andar 29 (ele salta devagar; se ficar com Lentidão do pólen, para e canta até passar).
5. **Entregar** — 🎬 nessa noite, o concerto: as 4 vozes juntas pela primeira vez num mês. Os sapos da vila saem das casas. O Barão chora atrás do leque.
   - **Coro** *(a cantar, legenda)*: "♪ Croac no lodo, croac no rio, quatro vozes contra o frio… e quem voltou da flor gigante, cantou mais alto, mais bonito, mais… avante! ♪"
   - **Ribito**: "'Avante' não rima com 'gigante'." · **Dona Lili**: "Rima com sentimento!"
   - ⚙ **Ocarina**. A música `coaxa_coro` passa a tocar na vila à noite.

### R3_07 — A Riqueza do Barão
| | |
|---|---|
| Quem dá | Barão Coaxim |
| Recompensa | 3 000 ouro · abre a **loja de itens raros** do Barão |

1. **Pedir** — **Barão**: "Na selva há ruínas, nas ruínas há pedra, na pedra há um ídolo que brilha e que medra! Traz-mo, traz-mo, que pago a valer: três mil moedas para ti receber!"
   - ▶ **"E se eu não o encontrar?"** → **Barão**: "Então três tesouros, que sejam bem raros: dourados, antigos, bonitos e caros!"
2. **Passo** — uma de duas:
   - **A)** entregar o **Ídolo de Jade** (andar 23, Ruínas de Pedra Verde, depois do puzzle das pedras dos animais). Se o fizeres, a **R3_15** (Fausto) falha.
   - **B)** entregar **3 tesouros raros** à escolha: Pele Dourada (Sapo Dourado), Dente de Mandíbula (R3_11), Âmbar com Mosquito (2% em nós de Âmbar), Esmeralda Grande (1% em nós de Esmeralda).
3. **Entregar** — **Barão** *(feliz)*: "Ora viva, ora viva, que belo tesouro! Toma as moedas, toma o meu ouro! E a minha loja, com coisas tão raras, abre-se agora para as tuas… taras? Caras! Coisas caras! Croac!"

> O Fausto e o Barão querem os dois o Ídolo (`fausto_rumor_03`, `rook_rumor_03`). Dar-lho ao Fausto **não** fecha a R3_07: o Barão aceita os 3 tesouros.

### R3_08 — Poções Surpresa
| | |
|---|---|
| Quem dá | Doutor Girino |
| Recompensa | título *Cobaia* · receita **Poção Arco-Íris** |

1. **Pedir** — **Girino**: "Preciso de alguém para… testar. Cinco poções. Uma de cada vez. Se morreres… não morres. Acho. Noventa por cento. Oitenta."
2. **Passo**: beber **5 Poções Surpresa** (ele dá-as; ficam na mochila) e **sobreviver** a cada efeito (1 minuto cada; se morreres durante o efeito, recomeça).
   - Efeitos possíveis (ao acaso, 10% cada):

     | Efeito | O que faz | Girino diz |
     |---|---|---|
     | Força | +30% ATQ, 1 min | "Músculos! Para a ciência!" |
     | Pena | saltas o dobro | "Leve como uma… pena! Ou um girino!" |
     | Sapo | `estado(sapo)` 3 s | "UM SAPO!" |
     | Gigante | ficas 1,5× maior (+20% vida, mais lento) | "Grande! GRANDE! Não pises o laboratório!" |
     | Pequeno | ficas 0,5× menor (+30% esquiva) | "Onde estás? Ah. Aí." |
     | Bolinhas | ficas às bolinhas roxas (só visual, 1 dia) | "Bonito!" |
     | Ao contrário | os controlos trocam (como o pólen do andar 29) | "Isso foi… inesperado." |
     | Fogo no rabo | rastro de fogo atrás de ti (queima inimigos) | "Ups. Corre. Corre para os inimigos." |
     | Soluços | a cada 5 s um soluço atira-te 1 m para cima | "Hic! Contagioso? Hic!" |
     | Nada | nada | "Nada? NADA? Isso é o pior resultado! Para a ciência!" |
3. **Entregar** — **Girino** *(feliz)*: "Cinco! E estás inteir{o/a}! Mais ou menos inteir{o/a}! Toma. A Arco-Íris. Tem tudo o que é bom e nada do que é mau. Demorei… catorze explosões."

### R3_09 — Mapa da Selva
| | |
|---|---|
| Quem dá | Vera Liana |
| Recompensa | **Bússola de Explorador** (mostra os segredos a 20 m no mapa) · 1 500 ouro |

1. **Pedir** — **Vera**: "O andar 23 e o 28. Os mais difíceis de desenhar: um é só folhas, o outro é só ar. Traz-mos a cem por cento. Os dois."
2. **Passo**: explorar **100%** do andar 23 (incluindo as Ruínas e o Rio Lento) e do andar 28 (incluindo o **Chão da Selva**, lá em baixo). O mapa mostra a % no canto.
   - Dica da Vera (se estiveres a 90% há muito tempo): "Os cantos. Ninguém vai aos cantos. Os cantos é que fazem os cem."
3. **Entregar** — **Vera** *(feliz)*: "Cem e cem! Toma esta bússola. Era minha. Já não preciso dela: agora tenho o mapa. Tu ainda precisas dos dois."

### R3_10 — Tirolesas
| | |
|---|---|
| Quem dá | Tom Tirolesa |
| Recompensa | as **6 tirolesas** do andar 28 ficam ativas |

1. **Pedir** — **Tom**: "Tenho seis tirolesas pensadas. Faltam-me cordas e ganchos. Cordas de liana, ganchos de aço. Trinta cordas, dez lingotes."
2. **Passo**: entregar **30 Fibra de Liana + 10 Lingote de Aço** (3 Ferro Negro + 1 Carvão na forja).
3. **Entregar** — 🎬 o Tom prende a última corda. Desce a primeira tirolesa aos gritos. **Tom**: "IUUUUUUPI!" *(de longe)* "FUNCIONA! VEM!"
   - ⚙ Tirolesas: interagir no ponto de partida (anel de corda); o herói desliza sozinho (pode atacar mosquitos pelo caminho).

### R3_11 — Mandíbula
Dada pela **Capitã Freya** (rank C; = `G_C_01`). Falas em `docs/dialogos/freya.md`. O Ssark tem uma fala especial (`ssark_09`).

### R3_12 — O Rei Bobo
Dada pelo **Rook**. Falas em `docs/dialogos/rook.md`.

### R3_13 — Café da Selva
Dada pelo **Lucien**. Falas em `docs/dialogos/lucien.md`.

### R3_14 — Chocolate!
Dada pela **Hana**. Falas em `docs/dialogos/hana.md`.

### R3_15 — O Ídolo de Jade
Dada pelo **Velho Fausto**. Falas em `docs/dialogos/fausto.md`. Escolha com a R3_07 (secção acima).

### R3_16 — Concurso de Pesca de Coaxa
| | |
|---|---|
| Quem dá | Rã-Rã |
| Recompensa | **Sapinho** (animal de estimação) · título *Mais Rápido que a Língua* |

1. **Pedir** — **Rã-Rã**: "Concurso. Cinco minutos. Maior peixe ganha. Eu ganho sempre." *(pausa)* "Inscreves-te?"
2. **Passo**: às **7:00** ou às **17:00**, nos Canais da Vila Coaxa. 5 minutos. Ganha o **peixe mais pesado**.
   - Concorrentes: Rã-Rã (o maior peixe dela é sempre **8 kg**), 3 sapos (2–5 kg) e, se o **Pip** estiver na equipa, o Pip (`pip_torre_26`).
   - Pesos: Bagre do Lodo 1–4 kg, Enguia de Lama 1–3 kg, Pirarucu 6–20 kg (só na **maré alta**), Velho Bigodes 40 kg (lendário; não aparece no concurso).
   - Ou seja: para ganhar, é preciso um **Pirarucu com mais de 8 kg**, o que obriga a ir na maré alta (ou com sorte e a Ocarina).
3. **Entregar**
   - *(ganhas)* 🎬 a Rã-Rã olha para o teu peixe. Muito tempo. Tira o chapéu. **Rã-Rã**: "…Onze anos." *(pausa)* "Toma. O Sapinho. Ele gosta de quem ganha." 🎬 o Sapinho salta-te para a cabeça.
   - *(perdes)* **Rã-Rã**: "Doze anos." ⚙ pode repetir-se no próximo concurso

---

## 5. Missões da Guilda (rank C) da região

Os objetivos e recompensas estão em `docs/MISSOES.md` (secção 3).

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_C_01 Mandíbula (R3_11) | "PROCURA-SE: Mãe-Crocodilo Mandíbula. Velha, enorme, com algas. Afundou 3 barcos no andar 26." | "Ela tem quarenta anos e nunca perdeu. Tu tens… menos. Mas és mais teimos{o/a}." | "O dente dela! É do tamanho do meu braço! Vou… não vou pô-lo na vitrine. Mete medo." |
| G_C_02 As Bruxas do Charco | "Cinco Bruxas do Pântano amaldiçoam quem passa no andar 22. Cuidado: afundam-se na lama." | "Bruxas! Se te transformarem em sapo, não venhas cá. O Gorvan tem alergia a sapos. Mentira. Mas vem pela porta de trás." | "Cinco! E não és um sapo! Tens a certeza? Diz 'croac'. …Pronto, estás bem." |
| G_C_03 Repara os Passadiços (R3_01) | ver a missão R3_01 (secção 4) | "Mangue! É a madeira que não apodrece. Quem me dera ser de mangue." | "Os carpinteiros agradecem. Dizem que é a primeira vez que alguém traz madeira sem cair na água. Caíste? Não lhes digo." |
