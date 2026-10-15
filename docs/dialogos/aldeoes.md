# Aldeões de Ascendia — frases soltas

A gente **sem nome** de Ascendia: andam pelas ruas, param, dizem **uma** frase e seguem. Não dão amizade, não têm
presentes nem missões. Servem para a cidade parecer viva e para mostrar **como a cidade muda** à medida que sobes.
Regras gerais dos diálogos: `docs/dialogos/README.md` (as condições escrevem-se da mesma maneira).

---

## 1. Como funcionam

| Regra | Valor |
|---|---|
| Quantos | **8 tipos** (secção 2), cada um com 2–3 aspetos (cores e cabelos trocados). Na cidade andam 20–40 ao mesmo tempo (mais nos festivais) |
| Onde | cada tipo tem os seus bairros e horários (rotina simples: casa → trabalho → Praça → casa) |
| Falar | [interagir] mostra **uma frase** num balão por cima da cabeça (sem caixa de diálogo, sem retrato). Ao passar perto, às vezes dizem uma frase sozinhos (10%) |
| Que frase | a mais **específica** que cumprir a condição (festival → invasão → depois de boss → capítulo → clima/hora → geral); ao acaso entre as do mesmo nível; não repete as últimas 3 |
| Nome no balão | o tipo: "Guarda", "Vendedeira", "Criança"… |
| IDs | `aldeao_<tipo>_<nº>` e `aldeao_<situação>_<nº>` |

---

## 2. Os tipos

| Tipo | Quem é | Onde anda | Bip |
|---|---|---|---|
| **Guarda** | soldado da Freya, de capacete e lança | muralha, portões, Praça | firme, curto |
| **Vendedeira** | vende fruta, peixe ou pão no Mercado | Mercado, 7:00–18:00 | rápido, alto |
| **Criança** | brinca aos aventureiros com paus | Praça, Bairro Baixo, rio | agudo, aos saltos |
| **Velho** | sentado nos bancos, a ver a torre | Praça, Bairro Alto, Taberna | lento, rouco |
| **Aventureiro** | da Guilda, rank E a B, mochila às costas | Guilda, Praça, Estalagem | animado |
| **Pescador** | do porto, de botas de borracha | Rio e Porto | preguiçoso |
| **Artesã** | aprendiz de algum mestre (avental sujo) | Bairro dos Artesãos | prático |
| **Lavadeira** | lava roupa no rio e sabe tudo de todos | rio, Bairro Baixo | conversador |

---

## 3. Frases gerais (por tipo)

| ID | Tipo | Condição | Frase |
|---|---|---|---|
| `aldeao_guarda_01` | Guarda | — | "Circula. Quer dizer, por favor. A Capitã diz para dizer 'por favor'." |
| `aldeao_guarda_02` | Guarda | `hora entre 22 e 5` | "Ronda da noite. Os monstros não dormem. Eu também não. Grande vida." |
| `aldeao_guarda_03` | Guarda | `rank >= B` | "É {o/a} da janela que já vai alto? Posso… posso apertar-te a mão? Não digas à Capitã." |
| `aldeao_vend_01` | Vendedeira | — | "Maçãs! Fresquinhas! Do andar 2! Não, não mordem. Essas são as do andar 3." |
| `aldeao_vend_02` | Vendedeira | `estacao == inverno` | "No inverno o peixe dura mais. Os clientes é que duram menos. Ninguém sai de casa." |
| `aldeao_vend_03` | Vendedeira | `hora entre 16 e 18` | "Ao fim do dia é metade do preço. Não digas ao Tobias que eu disse." |
| `aldeao_crianca_01` | Criança | — | "Eu sou {o/a} da janela e tu és o Ent! Cai! CAI!" |
| `aldeao_crianca_02` | Criança | — | "A minha mãe diz que um dia também vou à torre. Depois diz que é brincadeira. Depois chora." |
| `aldeao_crianca_03` | Criança | `animal != nenhum` | "Posso fazer festinhas? POSSO? Obrigad{o/a}!!! …Ele mordeu-me. Foi fixe." |
| `aldeao_crianca_04` | Criança | `arma_tipo == martelo` | "Isso é um martelo? É maior do que eu! Dá para partir a torre?" |
| `aldeao_velho_01` | Velho | — | "Quando eu era novo, a torre já estava ali. Quando eu for velho… já sou velho. Continua ali." |
| `aldeao_velho_02` | Velho | — | "Nunca subi. Nem ao andar 1. Sabes porquê? Também não sei. Sempre achei que amanhã." |
| `aldeao_velho_03` | Velho | `clima == chuva` | "Chove. A torre não se molha. Já reparaste? A chuva passa-lhe ao lado." |
| `aldeao_aventureiro_01` | Aventureiro | — | "Rank D! Há três anos! Estou quase no C. Quase. Desde há três anos." |
| `aldeao_aventureiro_02` | Aventureiro | `andar_maximo >= 30` | "Andar trinta? Eu cheguei ao doze. Uma vez. Com muita sorte e pouca dignidade." |
| `aldeao_aventureiro_03` | Aventureiro | `estado(cansado)` | "Estás com a cara que eu faço depois do andar 6. Vai dormir. A sério." |
| `aldeao_pescador_01` | Pescador | — | "Hoje não pica nada. Ontem também não. Amanhã vai picar. Tenho a certeza. Há vinte anos." |
| `aldeao_pescador_02` | Pescador | `clima == nevoeiro` | "Com nevoeiro, o Pip pesca peixes que não existem. Eu vi. Não acreditei. Ainda não acredito." |
| `aldeao_artesa_01` | Artesã | — | "O mestre diz que tenho mãos de manteiga. Eu digo que a manteiga também tem os seus talentos." |
| `aldeao_artesa_02` | Artesã | `missao(R10_11) == concluida` | "Doze armas míticas. O Brom não fala de outra coisa. Bem, fala. Mas pouco. Resmunga mais." |
| `aldeao_lav_01` | Lavadeira | — | "Sabes quem anda a namorar quem? Não? Ainda bem. Não se namora em Ascendia. É uma regra. Não sei de quem." |
| `aldeao_lav_02` | Lavadeira | — | "A Dona Marta põe mel no guisado. Às escondidas. Toda a gente sabe. Ninguém lhe diz." |
| `aldeao_lav_03` | Lavadeira | `hora entre 6 e 9` | "De manhã a água do rio é fria como a cara do Gorvan. Tu não digas que eu disse." |

---

## 4. Como a cidade fala de ti (por capítulo)

Valem para **todos os tipos** (a frase é a mesma; o balão mostra o tipo de quem a diz).

| ID | Condição | Frase |
|---|---|---|
| `aldeao_cap1_01` | `capitulo == 1` | "Outr{o/a} da janela. Já são dez mil. Dizem que é número redondo. Dá sorte?" |
| `aldeao_cap1_02` | `capitulo == 1` | "O rapaz de cabelo espetado, o 9 999, salvou-te? Ele salva toda a gente e depois finge que não." |
| `aldeao_cap2_01` | `capitulo == 2` | "Venceste a Árvore? Quer dizer, o Ent. O Ent da árvore. Bom. Parabéns. Pela árvore." |
| `aldeao_cap2_02` | `capitulo == 2` | "Diz que lá em baixo há gente a viver. Dentro da torre. Cogumelos que falam. Isso não pode ser verdade." |
| `aldeao_cap3_01` | `capitulo == 3` | "Os lagartos do pântano… a Guilda quer que os expulsem. Eu não sei. Nunca me fizeram mal. Também nunca os vi." |
| `aldeao_cap4_01` | `capitulo == 4 && flag(sssar_defendida)` | "Defendeste os lagartos? Contra a Guilda? Coragem. Ou loucura. Às vezes são primos." |
| `aldeao_cap4_02` | `capitulo == 4 && flag(sssar_expulsa)` | "A aldeia dos lagartos ficou vazia, dizem. Fizeste o que te mandaram. Não te julgo. Também não te aplaudo." |
| `aldeao_cap5_01` | `capitulo == 5` | "O Fausto anda a dizer que a torre teve reis. Reis! Que eram dos da janela. O homem bebe chá a mais." |
| `aldeao_cap6_01` | `capitulo == 6` | "Um dragão! No andar cinquenta! E tu venceste-o! O meu filho fez-te um desenho. Não te dou. É meu." |
| `aldeao_cap7_01` | `capitulo == 7 && flag(kai_desaparecido)` | "O 9 999 desapareceu? Aquele rapaz… sempre a correr. Há de aparecer. Os rápidos aparecem sempre." |
| `aldeao_cap8_01` | `capitulo == 8 && flag(kai_salvo)` | "O 9 999 voltou! Anda envergonhado. Dá para ver: come de cabeça baixa na Estalagem." |
| `aldeao_cap8_02` | `capitulo == 8 && flag(kai_vencido)` | "Não se fala do 9 999. A Lyra pediu. Ninguém fala." |
| `aldeao_cap9_01` | `capitulo == 9` | "O Gorvan foi ao andar 74 contigo? O Gorvan? O nosso Gorvan? Que está sempre na muralha? Não acredito." |
| `aldeao_cap10_01` | `capitulo == 10` | "Dizem que lá em cima há um rei cansado. Que quer alguém para o lugar dele. Não vás. Quer dizer… vai. Mas volta." |
| `aldeao_cap10_02` | `capitulo == 10` | "Toda a cidade fala de ti. Eu também. Agora estou a falar contigo. É diferente. Estou nervos{o/a}." |
| `aldeao_cap10_03` | `andar_maximo >= 97` | "Há quem diga que há uma cidade lá em cima para os que desistem. Eu nunca subi e já desisti. Moro aqui." |

---

## 5. Depois de cada boss de região (a 1.ª vez, durante 3 dias)

| ID | Condição | Frase |
|---|---|---|
| `aldeao_boss_ent` | `boss_derrotado(ent_anciao)` | "A primeira festa em anos! Por tua causa! Dança comigo! Não? Está bem. Danço eu." |
| `aldeao_boss_golem` | `boss_derrotado(golem_cristal)` | "Um golem de cristal. A minha avó tinha um copo de cristal. Partiu-se também. Pensei nisso." |
| `aldeao_boss_hidra` | `boss_derrotado(hidra)` | "Quantas cabeças? Sete? Nove? Cada um diz um número. Tu é que sabes. Não digas. É mais bonito assim." |
| `aldeao_boss_farao` | `boss_derrotado(farao_eterno)` | "Um faraó! Com múmias e tudo! O meu neto anda enrolado em ligaduras pela casa desde ontem." |
| `aldeao_boss_dragao` | `boss_derrotado(dragao_gelo)` | "METADE! Estás a meio da torre! Vou contar a toda a gente! Já contei. Vou contar outra vez." |
| `aldeao_boss_leviata` | `boss_derrotado(leviata)` | "O Pip diz que ajudou a vencer o Leviatã. Com uma cana. Não ajudou, pois não?" |
| `aldeao_boss_tita` | `boss_derrotado(tita_magma)` | "Venceste o coração de um vulcão. Eu ontem queimei uma torrada. Cada um tem a sua luta." |
| `aldeao_boss_rei` | `boss_derrotado(rei_sem_coroa)` | "Um rei que tentou parar a torre… Pobre homem. Dizem que te pediu desculpa. Os reis não pedem desculpa." |
| `aldeao_boss_serafim` | `boss_derrotado(serafim_caido)` | "…Hoje não há festa. Mas obrigado. A sério. Por teres ido. Por teres voltado." |

---

## 6. Clima, hora e estações

| ID | Condição | Frase |
|---|---|---|
| `aldeao_chuva_01` | `clima == chuva` | "Chuva! Os caracóis do andar 1 devem estar contentes." |
| `aldeao_trovoada_01` | `clima == trovoada` | "Com trovoada, o Cristal Mestre brilha mais. Ninguém sabe porquê. Eu não gosto." |
| `aldeao_neve_01` | `clima == neve` | "Neve! Bonecos de neve na Praça! O Governador proibiu. Ninguém liga." |
| `aldeao_noite_01` | `hora entre 22 e 4` | "À noite a torre parece mais alta. Juro. Já medi. Com os olhos." |
| `aldeao_manha_01` | `hora entre 5 e 7` | "Levantas-te cedo como os pescadores. Ou como os ladrões. Ou como os da janela." |
| `aldeao_primavera_01` | `estacao == primavera` | "Primavera. As flores da Mia estão todas abertas. Compra-lhe uma. Ela finge que não precisa." |
| `aldeao_verao_01` | `estacao == verao` | "Calor. Até a torre parece cansada." |
| `aldeao_outono_01` | `estacao == outono` | "As folhas caem e a torre fica. Isto parece um poema. Não é. É só outono." |
| `aldeao_inverno_01` | `estacao == inverno` | "Inverno. A Estalagem enche. O guisado da Dona Marta salva mais gente do que a Igreja." |

---

## 7. Festivais e eventos

| ID | Condição | Frase |
|---|---|---|
| `aldeao_f01` | festival F_01 | "Festa das Flores! Põe uma flor no cabelo! Ou na espada! Eu não te digo onde!" |
| `aldeao_f02` | festival F_02 | "Festival da Pesca! O Pip ganha sempre. Este ano ganhas tu. Aposto dois peixes." |
| `aldeao_f03` | festival F_03 | "Noite dos Espíritos! Puseste a lanterna à porta? Os espíritos ficam ofendidos." |
| `aldeao_f04` | festival F_04 | "Festival da Estrela! Quem te calhou no amigo secreto? Não digas! Diz! Não digas!" |
| `aldeao_f05` | festival F_05 (Dia da Subida) | "Hoje a cidade é tua! Quer dizer, é do Governador. Mas hoje é um bocadinho tua." |
| `aldeao_f07` | festival F_07 | "Vou pôr uma lanterna no rio por quem subiu e não voltou. Toda a gente tem alguém." |
| `aldeao_invasao_01` | `evento(invasao)` | "MONSTROS! Para dentro! Para dentro! Tu não! Tu para fora! Vai!" |
| `aldeao_invasao_02` | dia a seguir a uma invasão | "Obrigad{o/a} pela noite. A minha casa ainda tem telhado. A do vizinho não, mas ele ressona." |
| `aldeao_mercador_01` | `evento(mercador_errante)` | "O Mercador Errante está na Praça! Vende coisas que não sei para que servem. Comprei duas." |

---

## 8. Depois do fim (pós-jogo)

| ID | Condição | Frase |
|---|---|---|
| `aldeao_final1_01` | `flag(final_1)` | "Dizem que voltaste a casa e que isto é um sonho. Se é um sonho, sonha comigo a comprar maçãs." |
| `aldeao_final2_01` | `flag(final_2)` | "Ponho uma flor na tua estátua todas as manhãs. Tu vês? Lá de cima? Se vês, pisca uma estrela." |
| `aldeao_final2_02` | `flag(final_2)` | "Desde que estás lá em cima, ninguém novo cai no prado. Às vezes tenho saudades dos novos. Eram tão confusos." |
| `aldeao_final3_01` | `flag(final_3)` | "Um céu sem torre. Ainda olho para cima à procura dela. Os meus olhos não se habituam." |
| `aldeao_final3_02` | `flag(final_3)` | "Ascendia-ao-Sol. O Governador gaguejou o nome novo três vezes. Ficou." |
| `aldeao_final4_01` | `flag(final_4)` | "Ontem atravessei a ponte. Fui a um mundo de elfos e voltei para o jantar. Ainda não acredito." |
| `aldeao_final4_02` | `flag(final_4)` | "O senhor de cabelo branco que come guisado na Taberna… dizem que era o rei lá de cima. Parece tão simpático." |
