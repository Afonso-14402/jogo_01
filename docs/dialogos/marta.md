# Dona Marta — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.6. Dados: `dados/dialogos/marta.json`. Serviços e ementa: `docs/LOJAS.md`, secção 2.4.
A primeira cena dela é a **P7 — A Estalagem** (`docs/guiao/prologo.md`).

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | médios e redondos, devagar; sobem quando ralha |
| Como fala | como uma avó: dá ordens com carinho, faz perguntas sem esperar resposta, responde a tudo com comida |
| Repete | "Senta-te. Come. Depois falas.", "filh{o/a}", "Ai, Senhor.", "Come mais um bocadinho." |
| Tiques | limpa as mãos ao avental quando está nervosa (animação `limpar_avental`); dá palmadinhas na bochecha do herói com 6+ corações |
| Nunca diz | que está cansada; o nome do filho antes dos 4 corações |
| Chama ao herói | "querid{o/a}" ao início; "filh{o/a}" a partir dos 6 corações |
| O filho | **Tomás**. Subiu a torre aos 20 anos, há 28 anos, numa equipa da Guilda. Nunca voltou. O quarto dele, no andar de cima da estalagem, está igual |
| Rotina ao Domingo | não abre a cozinha de manhã: vai ao mercado da madrugada (5:00–7:00) e faz o **Assado de Domingo** |

---

## 2. Primeira conversa

A primeira conversa é a cena P7 (quarto, jantar, o Kai). A 1.ª vez que carregas em **Conversar** depois disso:

- **Dona Marta** *(feliz)*: "Dormiste bem? Não dormiste. Tens a cara amarrotada. Senta-te."
- **Dona Marta** *(normal)*: "Regras da casa: o pequeno-almoço é às seis, o almoço ao meio-dia e o jantar às sete. Quem não come, não sobe."
- **Dona Marta** *(normal)*: "A primeira semana é por conta da casa. Depois são vinte moedas. Ou ajudas-me com as compras: tenho sempre uma lista."
- **Dona Marta** *(feliz)*: "E se te magoares lá em cima, vens cá. Eu não curo feridas. Mas faço sopa."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Quarto · Refeição · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `marta_dia_01` | `hora entre 5 e 8` | feliz | "Bom dia! O pão ainda está quente. Não, não é para levar. É para comer aqui, sentad{o/a}." |
| `marta_dia_02` | `hora entre 5 e 8` | normal | "Acordei às quatro. Não por necessidade. É o costume. O corpo já não sabe dormir até tarde." |
| `marta_dia_03` | `hora entre 11 e 14` | normal | "Almoço! Hoje há sopa. Amanhã também há sopa. Sopa nunca fez mal a ninguém." |
| `marta_dia_04` | `hora entre 15 e 18` | normal | "A estalagem fica calma a esta hora. Aproveito para descascar batatas. Queres ajudar? Não queres. Ninguém quer." |
| `marta_dia_05` | `hora entre 19 e 22` | feliz | "Jantar! Senta-te. Come. Depois falas." |
| `marta_dia_06` | `hora entre 22 e 23` | normal | "Já é tarde. Os heróis também dormem. Os heróis dormem até mais do que os outros." |
| `marta_dia_07` | — | normal | "Estás magr{o/a}! A torre não te dá de comer?" |
| `marta_dia_08` | — | feliz | "O Tobias diz que a minha sopa é a melhor da cidade. O Tobias diz isso para não pagar. Mas é verdade." |
| `marta_dia_09` | — | normal | "Ontem um aventureiro pediu 'só água'. Dei-lhe água. E sopa. E pão. Saiu de cá a rebolar." |
| `marta_dia_10` | — | normal | "Quarenta anos de estalagem. Já vi passar aventureiros de todas as cores. Os que voltam têm todos a mesma cara: fome." |
| `marta_dia_11` | — | feliz | "O Brom vem cá jantar todas as noites e diz sempre 'está mais ou menos'. Raspa o prato com o pão. 'Mais ou menos'." |
| `marta_dia_12` | — | normal | "Põe o casaco. Não me interessa que lá em cima esteja calor. Cá em baixo está frio." |
| `marta_dia_13` | `dia_semana == domingo` | feliz | "Domingo é dia de assado! Fui ao mercado às cinco. O Tobias ainda estava a bocejar." |
| `marta_dia_14` | `dia_semana == segunda` | normal | "Segunda-feira. Lençóis. Todos os lençóis. Os aventureiros sujam lençóis como ninguém." |
| `marta_dia_15` | `dia_semana == sexta` | normal | "Sexta há música na taberna. O Lucien canta, eu fecho as janelas. Gosto muito do Lucien. Das janelas fechadas." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `marta_dia_20` | `estacao == primavera` | feliz | "Primavera: ervilhas, cenouras novas, morangos. A cozinha cheira a jardim." |
| `marta_dia_21` | `estacao == verao` | normal | "Com este calor, faço sopa fria. Sim, existe. Sim, é boa. Não, não discutas." |
| `marta_dia_22` | `estacao == outono` | feliz | "Abóboras! No outono faço doce de abóbora para o ano inteiro. Guardo um frasco para ti." |
| `marta_dia_23` | `estacao == inverno` | normal | "No inverno a estalagem enche. Os aventureiros sobem menos e comem mais. Não me queixo." |
| `marta_dia_24` | `clima == chuva` | zangado | "Molhad{o/a}! Até aos ossos! Tira as botas à porta. À PORTA." |
| `marta_dia_25` | `clima == trovoada` | triste | "Não gosto de trovoada. Não por mim. Penso sempre em quem está lá em cima sem telhado." |
| `marta_dia_26` | `clima == neve` | feliz | "Neve! Fiz chocolate quente. Bem, fiz leite quente com açúcar. O chocolate é caro. Mas imagina que é chocolate." |
| `marta_dia_27` | `clima == nevoeiro` | normal | "Com este nevoeiro, nem vejo a torre. Faz-me bem, às vezes. Não ver a torre." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `marta_dia_40` | `andar_maximo < 5` | normal | "Andar quanto? Três? Ai, Senhor. Já é alto. Eu enjoo no segundo degrau do escadote." |
| `marta_dia_41` | `boss_derrotado(ent_anciao)` | feliz | "A cidade fez festa por ti! E tu comeste? Na festa? Uma espetada não é comer." |
| `marta_dia_42` | `andar_maximo >= 11 && andar_maximo < 21` | normal | "Lá em baixo, nas minas, é escuro. Leva pão. O pão não se apaga como as tochas." |
| `marta_dia_43` | `boss_derrotado(golem_cristal)` | triste | "Tens casa própria agora. Ainda bem. …Mas vens jantar, não vens? A tua casa não tem a minha sopa." |
| `marta_dia_44` | `andar_maximo >= 31` | normal | "Deserto! Bebe água. Muita. Põe um lenço na cabeça. Não, um lenço não chega. Dois lenços." |
| `marta_dia_45` | `andar_maximo >= 41` | normal | "Tricotei-te umas meias para o gelo. Estão tortas. Aquecem na mesma. As meias tortas aquecem igual." |
| `marta_dia_46` | `andar_maximo >= 51` | triste | "O mar… O meu Tomás gostava tanto do mar. Nunca o viu. Só nos livros." |
| `marta_dia_47` | `missao(H_14) == concluida && missao(H_16) != concluida` | triste | "O prato do Kai está na mesa. Todas as noites. Se ele voltar com fome, a comida está pronta." |
| `marta_dia_48` | `flag(kai_salvo)` | feliz | "O Kai voltou e comeu três pratos. Três! E pediu desculpa por ter desaparecido. Com a boca cheia. Perdoei-lhe." |
| `marta_dia_49` | `flag(kai_vencido)` | triste | "Ainda ponho o prato do Kai na mesa. Não me digas que é tolice. Eu sei que é tolice." |
| `marta_dia_50` | `andar_maximo >= 71` | normal | "O Mestre Gorvan veio cá jantar. Há vinte anos que não vinha. Não disse nada. Comeu tudo. Foi o suficiente." |
| `marta_dia_51` | `andar_maximo >= 91` | triste | "Estás tão alto, filh{o/a}. Mais alto do que o meu Tomás alguma vez chegou. Volta. É só isso. Volta." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `marta_dia_60` | `coracoes(marta) >= 2` | feliz | "Guardei-te a fatia do meio do bolo. A do meio é a melhor. Não contes a ninguém." |
| `marta_dia_61` | `coracoes(marta) >= 3` | normal | "Já sei o que gostas de comer. Gostas de tudo. Isso é bom. Os esquisitos não chegam longe." |
| `marta_dia_62` | `coracoes(marta) >= 4` | triste | "O meu Tomás também chegava a casa com essa cara. Cansado e contente. Era a cara de que eu mais gostava." |
| `marta_dia_63` | `coracoes(marta) >= 5` | feliz | "Remendei-te o casaco enquanto dormias. Não perguntes como entrei no quarto. É a minha estalagem." |
| `marta_dia_64` | `coracoes(marta) >= 6` | feliz | "Filh{o/a}. …Deixa-me chamar-te assim. Na minha idade já não peço licença, mas peço-te a ti." |
| `marta_dia_65` | `coracoes(marta) >= 8` | normal | "O quarto é teu. Não é 'o quarto do fundo'. É o teu quarto. Pus-lhe uma cortina nova." |
| `marta_dia_66` | `coracoes(marta) >= 10` | feliz | "Quando subires lá acima, lembra-te: tens uma casa cá em baixo. Com sopa. Sempre com sopa." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `marta_dia_70` | `origem == ajudante` | feliz | "Carregaste-me as compras outra vez sem eu pedir. No teu mundo devias ter uma mãe muito orgulhosa." |
| `marta_dia_71` | `origem == atrasado` | normal | "Comes a correr. Engoles sem mastigar. Tu no teu mundo estavas sempre atrasad{o/a}, não estavas?" |
| `marta_dia_72` | `origem == dormir` | feliz | "Dormiste doze horas! Doze! Isso é que é dormir. Bate-se à porta e nada. Gosto de quem dorme bem." |
| `marta_dia_73` | `origem == jogador` | normal | "O Kai diz que no vosso mundo há 'jogos' onde se sobe torres. E que as pessoas fazem isso por gosto. Ai, Senhor." |
| `marta_dia_74` | `skill_unica == coracao_de_dragao` | surpresa | "Curas-te sozinh{o/a}? Então porque é que chegas sempre a sangrar? Coração de dragão e cabeça de vento." |
| `marta_dia_75` | `skill_unica == bolsa_infinita` | feliz | "Uma mochila sem fundo! Leva-me lá acima um tacho. Um grande. Para fazeres sopa como deve ser." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `marta_curta_1` | normal | "Comeste? Come." |
| `marta_curta_2` | feliz | "Outra vez por aqui? Ainda há sopa." |
| `marta_curta_3` | normal | "Vai descansar. Eu fico aqui. Fico sempre aqui." |
| `marta_curta_4` | feliz | "Hmm? Estava a provar o molho. Falta sal. Falta sempre sal." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Dona Marta** *(normal)*: "A torre? Eu não percebo nada da torre. Percebo de quem volta dela."
- **Dona Marta** *(triste)*: "Uns voltam com fome, outros com feridas, outros com medo. Alguns não voltam. Para todos há um prato."
- **Dona Marta** *(feliz)*: "Por isso tu vais voltar. Tens um prato à espera. Ninguém deixa um prato a arrefecer."

### 4.2 O andar atual

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta! Traz-me cogumelos. Dos que não andam." |
| 2 Cavernas | "Debaixo da terra… Os mineiros comem pouco e mal. Leva-lhes sopa. Não, leva-os a eles para cá." |
| 3 Pântano | "Pântano? Lava-te antes de entrar. Ainda me lembro do cheiro do último que veio do pântano. Três dias." |
| 4 Deserto | "Deserto. Água. Já disse água? Água." |
| 5 Gelo | "Gelo! Tens as meias? As tortas? Calça-as. Duas de cada lado." |
| 6 Oceano | "O mar dentro da torre… O meu Tomás havia de gostar de ver. Traz-me uma concha. Uma pequena. Para mim." |
| 7 Vulcão | "Lava?! Ai, Senhor. Não te chegues perto. Nem para aquecer as mãos." |
| 8 Reino Assombrado | "Fantasmas… Se vires algum com fome, diz-lhe que a estalagem é aqui." |
| 9 Céu | "No céu? Por cima das nuvens? Então já passaste o sítio onde os pássaros desistem." |
| 10 Abismo | "Não sei o que há lá em cima. Não quero saber. Quero que voltes e me contes. Ao jantar." |

### 4.3 Rumores

| ID | Condição | Rumor |
|---|---|---|
| `marta_rumor_01` | — | "O Tobias dá pão aos pobres do Bairro Baixo às escondidas. Pensa que ninguém sabe. Sou eu que lhe vendo o pão." |
| `marta_rumor_02` | — | "A Mia não come o suficiente. Leva-lhe uma torta. Diz que é de ti. Não digas que é minha: ela não aceita esmolas." |
| `marta_rumor_03` | — | "O Brom chora com histórias tristes. Diz que é fumo. Na minha cozinha não há fumo. Há cebolas." |
| `marta_rumor_04` | `andar_maximo >= 2` | "O Bruno do acampamento vinha cá comer quando era rapaz. Comia por três. Agora tem uma filha que lê livros. O mundo dá voltas." |
| `marta_rumor_05` | `andar_maximo >= 6` | "Dizem que no andar 6 há mel azul. Azul! Se me trouxeres, faço-te uma coisa que nunca comeste." |
| `marta_rumor_06` | — | "O Gorvan não come desde que… Bem. Come pouco. Se o vires, leva-o a jantar. Ele diz que não. Leva-o na mesma." |
| `marta_rumor_07` | `andar_maximo >= 16` | "Um fungoide veio cá pedir sopa de cogumelos. Fiquei sem saber se era canibalismo. Dei-lhe sopa de batata." |
| `marta_rumor_08` | `estacao == outono` | "Na Noite dos Espíritos, ponho uma lanterna à janela do quarto de cima. Ninguém pergunta porquê. Ainda bem." |
| `marta_rumor_09` | `andar_maximo >= 51` | "Os aventureiros que voltam do mar contam de um navio cheio de fantasmas. Dizem que não sabem que morreram. Coitados. Ninguém lhes disse." |

### 4.4 A vida dela

| Corações | Fala |
|---|---|
| 0 | "Eu? Sou a Marta da estalagem. Faço comida, lavo lençóis, ralho. É uma vida boa." |
| 2 | "Abri esta estalagem há quarenta anos com o meu marido, o Abel. Ele morreu de uma tosse num inverno muito frio. Fiquei eu e o fogão." |
| 4 | "Tive um filho. O **Tomás**. Subiu a torre aos vinte anos. Há vinte e oito anos. Não voltou." |
| 6 | "Abri a estalagem a todos os aventureiros por causa dele. Se algum aventureiro lá em cima tiver fome, que alguém lhe dê de comer. Como eu dou aqui aos filhos dos outros." |
| 8 | "O quarto dele está igual. A cama feita. Os livros sobre o mar. Limpo-o todas as segundas. Já não choro quando entro. Quase nunca." |
| 10 | "Já não espero que ele volte. Espero só que, onde estiver, alguém lhe tenha dado sopa. E tu trouxeste-me isso. A certeza." |

---

## 5. Presentes

**Adora:** ingredientes de qualidade **Excelente**, Flor de Mel, Mel Azul · **Gosta:** flores, legumes, qualquer
prato de qualidade Boa · **Detesta:** partes de monstros, Gel de Slime, lixo de pesca. O resto é **neutro**.
**Regra especial:** se o herói **dormir 3 noites seguidas sem comer**, a Dona Marta ralha (fala `marta_estado_fome`) e
não aceita presentes nesse dia.

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "Ai, que coisa tão boa! Isto merece uma receita nova. Vou pensar numa. Vou pensar a noite toda." · "Excelente! Vê-se logo. Tens bom olho, filh{o/a}. Tens olho de cozinheir{o/a}." |
| Gosta | "Que bonito! Vai já para a mesa." · "Obrigada, querid{o/a}. Logo à noite há disto no jantar." |
| Neutro | "Obrigada! Hei de lhe dar uso. Tudo tem uso numa cozinha." |
| Não gosta | "Ah… Obrigada pela intenção. A intenção também se come. Pouco." |
| Detesta | "Isso está a pingar no meu chão LIMPO. Lá para fora. Já." · "Gel de slime? Numa cozinha? Ai, Senhor, Senhor." |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Mel Azul | "Mel azul! Tal e qual como o Tomás descrevia num livro. Pensei que era invenção. Afinal existe." |
| Flor de Mel | "Cheira à minha mãe. Ela punha destas na janela. Obrigada, filh{o/a}." |
| Concha (qualquer) | "Uma concha do mar. Vou pô-la no quarto do Tomás. Na prateleira dos livros do mar." |
| Sopa de Legumes feita pelo herói | "A minha receita! Prova-se… Está boa. Está quase tão boa como a minha. Não digas a ninguém que eu disse 'quase'." |
| Guisado da Mãe feito pelo herói | 🎬 a Dona Marta prova e fica calada. "…Está igual. Está igual ao meu. Já não preciso de estar cá para isto existir." |
| Pão (qualquer) | "Pão? Dás-me pão? A mim? …Vou provar só por curiosidade. Está bom. Grrr. Está bom." |

---

## 6. Aniversário e festivais

**Aniversário (Outono, dia 12):**
- Sem presente: **Dona Marta** *(normal)*: "Hoje? Nada de especial. Mais um ano. A sopa não sabe que dia é."
- Com presente que adora: **Dona Marta** *(feliz)*: "Lembraste-te! Ninguém se lembra da velha da estalagem. Senta-te. Hoje sou eu que te sirvo o dobro."
- Com outro presente: **Dona Marta** *(feliz)*: "Um presente para mim? Ai, filh{o/a}. Não era preciso. Mas era bom. Era muito bom."
- 🎬 Neste dia a estalagem tem bolo de abóbora de graça para todos (e todos os NPCs que lá vão jantar dizem "parabéns").

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Concurso de flores! Eu não concorro. Ponho as flores nas mesas. As mesas também merecem." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Dona Marta** *(feliz)*: "Eu?! Com estas pernas? …Uma só. Devagar. E se te piso, a culpa é tua." ⚙ dança · +100 |
| F_02 Festival da Pesca | "Tragam-me os peixes que não ganharem! Faço caldeirada para a cidade inteira." |
| F_03 Noite dos Espíritos | "Esta noite ponho uma lanterna à janela do quarto de cima. É para quem anda perdido encontrar o caminho." |
| F_04 Festival da Estrela | "Amigo secreto! Calhou-me o Brom. Vou dar-lhe meias. Ele vai dizer que são 'mais ou menos'. Vai usá-las todos os dias." |
| F_05 Dia da Subida | "Fiz comida para a praça inteira! Tu primeiro. Herói come primeiro. É a regra. Inventei-a agora." |
| F_06 Concurso da Casa | "Não sou jurada. Mas vou ver as cozinhas de toda a gente. Para aprender. E para julgar. Em silêncio." |
| F_07 Noite das Lanternas | "Ponho sempre uma lanterna pelo Tomás. Este ano… podes pô-la tu? As minhas mãos já tremem." (com 4+ ❤️ ⚙ +30) |

---

## 7. Depois dos bosses

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `marta_boss_javali_rei` | "Um javali enorme? Trouxeste carne? Não? Então para que é que serviu a luta?" |
| Ent Ancião (10) | `marta_boss_ent_anciao` | "A cidade está em festa e tu estás com cara de quem chorou. Come. Depois conta. Ou não contes." |
| Aranha-Mãe (15) | `marta_boss_aranha_mae` | "Uma aranha?! Sacode a roupa lá fora. Toda. A roupa toda." |
| Golem de Cristal (20) | `marta_boss_golem_cristal` | "Casa nova! Toma: um tacho, uma colher de pau e um avental. Uma casa sem tacho não é casa." |
| Serpente do Lodo (25) | `marta_boss_serpente_lodo` | "Cheiras a pântano. Banho. Depois jantar. A ordem é essa." |
| Hidra do Pântano (30) | `marta_boss_hidra_pantano` | "Cortaste cabeças e nasciam mais? Isso é como os pratos para lavar." |
| Escorpião Imperador (35) | `marta_boss_escorpiao_imperador` | "Estás queimad{o/a} do sol! Põe manteiga. Não, a manteiga é para comer. Põe a pomada da Selene." |
| Faraó Eterno (40) | `marta_boss_farao_eterno` | "Um rei morto há mil anos? E ainda lutava? Isso é que é teimosia. Gosto de gente teimosa. De mortos, menos." |
| Yeti Ancião (45) | `marta_boss_yeti_anciao` | "Calçaste as meias tortas? Calçaste! Vês? Venceste por causa das meias." |
| Dragão de Gelo (50) | `marta_boss_dragao_gelo` | "Metade da torre! Fiz um bolo com cinquenta velas. Não cabiam. Pus cinco. Imagina as outras." |
| Capitão Esqueleto (55) | `marta_boss_capitao_esqueleto` | "Piratas mortos… Diz-me: no navio deles havia algum rapaz de olhos castanhos? …Não. Esquece. Come." |
| Leviatã (60) | `marta_boss_leviata` | "Venceste o mar. Mas o Kai… O prato dele continua na mesa." |
| Ferreiro Infernal (65) | `marta_boss_ferreiro_infernal` | "O Brom passou cá. Comeu calado. Depois disse 'está bom'. Não 'mais ou menos'. 'Bom.' Fiquei preocupada." |
| Kai — salvo (68) | `marta_boss_kai_salvo` | "Trouxeste-mo de volta. Senta-te. Os dois. Não, primeiro abraço. Depois sopa." |
| Kai — vencido (68) | `marta_boss_kai_vencido` | "Não digas nada. Eu sei. Eu sei como é. Senta-te aqui ao pé de mim." |
| Titã de Magma (70) | `marta_boss_tita_magma` | "Tens as sobrancelhas chamuscadas. Crescem. Come que crescem mais depressa." |
| Lich Bibliotecário (75) | `marta_boss_lich_bibliotecario` | "O Fausto anda a ler à mesa outra vez. Disse que foste tu que lhe trouxeste livros. Agora não come. Obrigadinha." |
| Rei Sem Coroa (80) | `marta_boss_rei_sem_coroa` | "O Gorvan voltou a jantar cá todas as noites. Ri-se. O Gorvan ri-se! Que fizeste tu a esse homem?" |
| Grifo Real (85) | `marta_boss_grifo_real` | "Voaste num pássaro gigante? Ai, Senhor. Não me contes. Conta. Não me contes!" |
| Serafim Caído (90) | `marta_boss_serafim_caido` | "Vens com os olhos de quem ouviu uma coisa que não queria. Não precisas de dizer. Hoje dormes cá. No quarto de cima." |
| Guardião do Tempo (95) | `marta_boss_guardiao_tempo` | "Dizes que o tempo parou lá em cima? Cá em baixo não. A sopa arrefeceu. Senta-te que eu aqueço." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — A primeira sopa

| | |
|---|---|
| ID | `cena_marta_2` |
| Quando | 2 ❤️ · entrar na Estalagem entre as 15:00 e as 18:00 |
| Onde | cozinha da Estalagem |
| Quem | herói, Dona Marta |
| Música | `ascendia_dia` (versão calma) |

🎬 A cozinha está cheia de tachos. A Dona Marta tem uma faca na mão e um monte de cenouras à frente.

- **Dona Marta** *(feliz)*: "Ah, chegaste na hora certa! Lava as mãos. Vais aprender a fazer sopa."
- **Dona Marta** *(normal)*: "Toda a gente devia saber fazer uma sopa. Quem sabe fazer sopa nunca passa fome. Nem fica sozinho."
- 🎬 Minijogo curto: cortar 3 legumes (carregar no botão no ritmo) e mexer o tacho.
- *(se cortar bem)* **Dona Marta** *(surpresa)*: "Olha! Tens jeito! Quem te ensinou?"
- *(se cortar mal)* **Dona Marta** *(feliz)*: "Ai, as cenouras! Parecem pedras de rio. Não faz mal. A sopa não vê a forma."

▶ **"A minha família cozinhava assim."**
▶ **"Nunca fiz uma sopa."**

- *(família)* **Dona Marta** *(feliz)*: "Então tens uma família que gosta de ti. Vê-se. Quem cozinha para os outros gosta deles." ⚙ +30
- *(nunca)* **Dona Marta** *(normal)*: "Nunca?! Então hoje é um dia importante. A primeira sopa a gente não esquece."
- **Dona Marta** *(feliz)*: "Pronto. Agora sabes. Leva a receita. E se alguma vez estiveres triste lá em cima, faz sopa. Funciona sempre."

⚙ Receita **Sopa de Legumes** (se ainda não a tiveres) e **Torta de Maçã Selvagem**. 5% de desconto nas refeições.

### ❤️ 4 — O nome do filho

| | |
|---|---|
| ID | `cena_marta_4` |
| Quando | 4 ❤️ · entrar na Estalagem entre as 22:00 e as 23:00 |
| Onde | sala da Estalagem, vazia; só uma vela acesa |
| Quem | herói, Dona Marta |
| Música | `tristeza` (versão curta) |

🎬 A Dona Marta está sentada sozinha, a dobrar guardanapos que já estão dobrados.

- **Dona Marta** *(surpresa)*: "Ainda acordad{o/a}? Senta-te. Eu também não tenho sono."
- **Dona Marta** *(normal)*: "Sabes porque é que guardo sempre o quarto do fundo para os Jogadores novos?"
- **Dona Marta** *(triste)*: "Porque o quarto de cima é do Tomás. O meu filho."
- **Dona Marta** *(triste)*: "Tinha vinte anos. Queria ver o mar. Lia livros sobre o mar. Dizia que lá em cima, algures, havia um mar inteiro."
- **Dona Marta** *(triste)*: "Foi com uma equipa da Guilda. Há vinte e oito anos. Despediu-se da porta. Disse: 'Guarda-me sopa.'"
- 🎬 Ela endireita um guardanapo. Outra vez.
- **Dona Marta** *(normal)*: "Ainda guardo. Todas as noites há uma tigela a mais. Acabo por a dar a alguém. Hoje é tua."

▶ **"Vou procurá-lo lá em cima."**
▶ **(Comer a sopa em silêncio.)**

- *(procurar)* **Dona Marta** *(triste)*: "Não, filh{o/a}. Não sobes por ele. Sobes por ti. Se encontrares alguma coisa… então, sim, traz. Mas não sobes por ele." ⚙ +30
- *(silêncio)* 🎬 o herói come. A Dona Marta sorri. **Dona Marta** *(feliz)*: "Comes como ele. Com a colher cheia demais." ⚙ +30

⚙ A Dona Marta ensina **receitas da estalagem**: abre 3 receitas na loja dela.

### ❤️ 6 — O guisado secreto

| | |
|---|---|
| ID | `cena_marta_6` |
| Quando | 6 ❤️ · Domingo, entre as 12:00 e as 14:00 |
| Onde | cozinha da Estalagem |
| Quem | herói, Dona Marta (e o Brom, a espreitar à porta) |
| Música | `taberna` (versão lenta) |

🎬 Há um tacho enorme ao lume. Cheira a coisas boas. O Brom está à porta da cozinha a espreitar.

- **Dona Marta** *(feliz)*: "Prova isto. Não, não perguntes o que é. Prova."
- 🎬 O herói prova.
- **Dona Marta** *(normal)*: "É o meu guisado. O verdadeiro. Ainda não está pronto: falta-lhe uma coisa e eu já não sei qual é."
- **Dona Marta** *(triste)*: "A minha mãe fazia-o. Morreu antes de me dizer o último ingrediente. Há quarenta anos que tento."
- **Brom** *(da porta, zangado)*: "Falta-lhe alho!"
- **Dona Marta** *(zangado)*: "Não falta alho, Brom! Vai para a tua forja!"

▶ **"Falta-lhe mel."**
▶ **"Falta-lhe sal."**
▶ **"Está perfeito assim."**

- *(mel)* **Dona Marta** *(surpresa)*: "Mel? Num guisado? …A minha mãe tinha colmeias. Ai, Senhor. Tinha colmeias." ⚙ +30 · flag `marta_pista_mel`
- *(sal)* **Dona Marta** *(feliz)*: "Falta sempre sal! Mas não é isso. Bem tentado."
- *(perfeito)* **Dona Marta** *(feliz)*: "Mentiroso. Mas és um mentiroso simpático."
- **Dona Marta** *(normal)*: "Vou continuar a tentar. E tu, se encontrares alguma coisa lá em cima… Uma carta, uma pista, qualquer coisa do meu Tomás…"
- **Dona Marta** *(triste)*: "Não. Esquece. Não te peço isso."

⚙ Missão **N_MARTA_3 O Quarto Vazio** fica disponível (secção 9). A Dona Marta aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — O quarto é teu

| | |
|---|---|
| ID | `cena_marta_8` |
| Quando | 8 ❤️ · voltar à cidade depois de morrer na torre **ou** entrar na Estalagem entre as 20:00 e as 22:00 |
| Onde | corredor da Estalagem, à porta do quarto do fundo |
| Quem | herói, Dona Marta |
| Música | `amizade` |

🎬 A porta do quarto do fundo tem um papel pregado com o nome do herói, escrito com letra bonita.

- **Dona Marta** *(nervosa)*: "Não é nada! É só um papel. Para saberem que o quarto tem dono."
- **Dona Marta** *(normal)*: "A partir de hoje não pagas. Não, não discutas. Já discuti eu sozinha a noite toda e ganhei eu."
- **Dona Marta** *(feliz)*: "O quarto é teu, filh{o/a}. Não 'o quarto dos Jogadores novos'. O teu."
- 🎬 Abre a porta. Cortinas novas, uma manta de retalhos na cama, um vaso com uma flor.
- **Dona Marta** *(triste)*: "A manta fui eu que a fiz. Tem bocados de roupa velha da estalagem. Este azul era do Tomás."

▶ **"Obrigad{o/a}, mãe."**
▶ **"Obrigad{o/a}, Dona Marta."**

- *(mãe)* 🎬 A Dona Marta fica parada. Põe a mão na boca. **Dona Marta** *(feliz, a chorar)*: "…Ai, Senhor. Ai, Senhor. Vai dormir. Vai, antes que eu faça figuras." ⚙ +30
- *(Dona Marta)* **Dona Marta** *(feliz)*: "Dona Marta, Dona Marta. Tão educad{o/a}. Vai dormir."

⚙ Dormir na Estalagem fica **grátis para sempre**. 15% de desconto nas refeições. Passa a mandar **cartas** (1 por semana) com comida: um prato do dia, uma torta ou um frasco de doce de abóbora.

### ❤️ 10 — O Guisado da Mãe

| | |
|---|---|
| ID | `cena_marta_10` |
| Quando | 10 ❤️ · `missao(N_MARTA_3) == concluida` · Domingo à noite (19:00–22:00) |
| Onde | cozinha da Estalagem, só com uma vela e o fogão aceso |
| Quem | herói, Dona Marta |
| Música | `tema_marta` (guitarra, embalar) |

🎬 A Dona Marta tem a carta do Tomás aberta em cima da mesa, presa com uma colher para não fugir.

- **Dona Marta** *(feliz)*: "Lembras-te do guisado? Do ingrediente que faltava?"
- **Dona Marta** *(normal)*: "Li a carta do Tomás outra vez. Pela centésima vez. E no fim ele escreveu: 'Diz à avó que o guisado dela tinha mel. Eu via-a pôr às escondidas.'"
- **Dona Marta** *(surpresa)*: "Ele sabia! O meu menino sabia o segredo da minha mãe e nunca mo disse. Porque eu nunca lhe perguntei!"
- 🎬 Ela ri-se e chora. Põe uma colher de mel no tacho. Mexe devagar.
- **Dona Marta** *(feliz)*: "Prova."
- 🎬 O herói prova. A cozinha fica dourada por um segundo (efeito suave).
- **Dona Marta** *(feliz)*: "É este. É este o sabor. Quarenta anos."
- **Dona Marta** *(normal)*: "Agora ouve bem, que só digo uma vez. Vou ensinar-te tudo. Cada passo. Cada colher."
- **Dona Marta** *(triste)*: "Assim, quando eu já cá não estiver, alguém continua a fazê-lo. E quem o comer vai sentir-se em casa."

▶ **"Vou fazê-lo para toda a gente."**
▶ **"Vou fazê-lo para ti."**

- *(toda a gente)* **Dona Marta** *(feliz)*: "Isso. É para isso que serve uma receita. Para se dar."
- *(para ti)* **Dona Marta** *(feliz)*: "Para mim? Ai, filh{o/a}. Então volta todos os domingos. Para eu provar e dizer que falta sal."

⚙ Receita **Guisado da Mãe** (cura tudo e +10% a tudo durante 1 dia). Título *Família da Estalagem*.
⚙ No epílogo, a Dona Marta põe a tua fotografia ao lado da do Tomás (ver `docs/HISTORIA.md`, secção 7).

---

## 9. Missões

### N_MARTA_1 — Ingredientes Frescos (0 ❤️, depois de a quinta abrir, andar 10)

- **Pedir** — **Dona Marta** *(normal)*: "Tens uma quinta? Uma quinta tua? Então traz-me cinco legumes que tenhas sido tu a plantar. Dos teus. Quero ver se tens mão para a terra."
- **Passo**: entregar **5 legumes** colhidos na tua quinta (qualquer legume; qualidade Boa ou melhor dá +50 amizade extra).
- **Durante** — **Dona Marta**: "Ainda não colheste? As cenouras não se apressam. Tu também não te apresses. Rega-as."
- **Entregar** — **Dona Marta** *(feliz)*: "Olha que bonitos! Tortinhos, mas bonitos. Toma a receita da minha Sopa de Legumes. A verdadeira. Com o truque da cebola."
  - ⚙ Receita **Sopa de Legumes** (se já a tiveres da cena de 2 ❤️, dá a **Sopa de Abóbora**) · +100 amizade

### R1_05 — Mel Azul (0 ❤️, `andar_maximo >= 6`)

- **Pedir** — **Dona Marta** *(feliz)*: "Dizem que no andar 6 há abelhas que fazem mel azul. AZUL. Traz-me cinco frascos e faço-te uma coisa que nunca comeste."
- **Passo**: apanhar **5 Mel Azul** nas Colmeias Gigantes do andar 6 (as abelhas atacam quem tira mel; ver `docs/regioes/r01_floresta.md`).
- **Durante** — **Dona Marta**: "As abelhas picaram-te? Põe vinagre. Não tens vinagre? Toma vinagre."
- **Entregar** — 🎬 a Dona Marta abre um frasco e cheira.
  - **Dona Marta** *(feliz)*: "Azul. É mesmo azul. O Tomás tinha um livro com uma abelha azul na capa. Pensei que era invenção."
  - **Dona Marta** *(feliz)*: "Senta-te. Panquecas de mel azul. Estas sim, nunca comeste. Toma a receita, mas prova primeiro as minhas."
  - ⚙ Receita **Panquecas de Mel Azul** · +150 amizade

### Lista da Marta (diária, opcional)

- Substitui o pagamento do quarto (20 ouro) depois da 1.ª semana.
- **Dona Marta**: "Hoje a lista é: {qtd} {item}, {qtd} {item}. Vai ao mercado ou à tua quinta, como quiseres."
- Itens: 2 a 3 ingredientes básicos ao acaso (ver `docs/ITENS.md`, secção 5).
- **Entregar**: "Obrigada, querid{o/a}. O quarto está pago. E leva este pãozinho, que estás com cara de fome." (+1 Pão com Queijo)

### N_MARTA_3 — O Quarto Vazio (6 ❤️, depois da cena de 6 ❤️, `andar_maximo >= 58`)

- **Abre** — sem pedido: quando chegas ao andar 58, `[Sistema] Missão nova: O Quarto Vazio.` (a Dona Marta não a pede; o herói decide procurar).
- **Passos**:
  1. Na **Fossa Abissal** (andar 58), no **Fundo Escuro**, encontrar o destroço do barco **"Gaivota"** (o barco da equipa do Tomás; precisa de luz e do Capacete de Escafandro).
  2. Dentro do destroço, abrir a caixa de lata (puzzle simples: rodar o fecho com 3 números — os números estão riscados na parede do barco: 2-8-0, os dias que a equipa contou).
  3. Apanhar a **Carta do Tomás** (item de missão; está seca dentro da caixa).
  4. Levar a carta à Dona Marta.
- **No destroço** — `[Sistema] Encontraste: o barco "Gaivota".` Na parede: "Tomás · Rui · Belmira · Sancho — 280 dias".
- **Entregar** (Estalagem, qualquer hora):
  - 🎬 O herói pousa a carta na mesa. A Dona Marta reconhece a letra antes de pegar nela.
  - **Dona Marta** *(triste)*: "…É a letra dele. Escrevia os 'a' como se fossem 'o'. Eu ralhava."
  - 🎬 Lê em silêncio. A câmara não mostra a carta: só a cara dela, que muda devagar.
  - **Dona Marta** *(triste)*: "Ele viu o mar. Viu o mar, filh{o/a}. Diz que era 'maior do que todos os livros juntos'."
  - **Dona Marta** *(triste)*: "Diz que tinha fome, mas que se lembrava da minha sopa e que isso chegava."
  - **Dona Marta** *(feliz, a chorar)*: "E diz: 'Mãe, não fiques à minha espera. Dá a minha sopa a outro.'"
  - 🎬 Ela olha para o herói durante muito tempo.
  - **Dona Marta** *(feliz)*: "Já dei. Já a dei a outro. Ele ia gostar de ti."
  - ⚙ +300 amizade (❤️❤️❤️) · flag `marta_carta_tomas` · a Carta do Tomás passa a estar no quarto de cima da estalagem (decoração que se pode ler)

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `marta_estado_vida` | `vida_pct < 30` | zangado | "Estás a sangrar! Senta-te. NÃO. Na cadeira não, que está limpa. No banco. Já vou buscar panos." |
| `marta_estado_maldito` | `estado(amaldicoado)` | triste | "Estás com uma cor esquisita. Vai à Irmã Célia. Depois vem cá. Sopa quente também tira maldições. Acho eu." |
| `marta_estado_cansado` | `estado(cansado)` | zangado | "Olheiras até ao chão! Cama. Já. E amanhã ao pequeno-almoço quero ver essa cara diferente." |
| `marta_estado_molhado` | `estado(encharcado)` | zangado | "Molhad{o/a} outra vez! Tira as botas. À porta. Já disse que à porta." |
| `marta_estado_fome` | dormiu 3 noites seguidas sem comer | zangado | "Três dias sem comer?! Pensas que eu não sei? Eu sei tudo. Senta-te. Hoje não sais daqui sem jantar." ⚙ não aceita presentes hoje |
| `marta_estado_sapo` | `estado(sapo)` | surpresa | "Um sapo na minha cozinha! Fora! …Espera. Esse sapo tem o teu chapéu. Ai, Senhor." |
| `marta_morte` | 1.ª vez que voltas à estalagem depois de morrer | triste | "Trouxeram-te em braços. Não me faças isso outra vez. Ouviste? Não me faças isso." |
| `marta_animal` | `animal != nenhum` (1.ª vez) | feliz | "Um bicho! Come? Come o quê? Vou fazer-lhe uma tigela. Uma pequena. Com o nome dele." |
| `marta_comp_kai` | `companheiro(kai)` | feliz | "Kai! Estás mais magro! Os dois, para a mesa." |
| `marta_comp_mia` | `companheiro(mia)` | feliz | "Mia! Com um arco de verdade! Senta-te. As heroínas pequenas comem o dobro." |
| `marta_comp_gorvan` | `companheiro(gorvan)` | surpresa | "O Gorvan na torre outra vez… Leva-lhe isto. É a sopa preferida dele. Ele diz que não tem preferidas. Tem esta." |
| `marta_casa` | 1.ª vez depois de receber a casa (andar 20) | triste | "Vais dormir na tua casa agora. Está certo. Está muito certo. …Mas o quarto fica aqui. Sempre." |

### Serviço

| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `marta_serv_quarto` | **Quarto** (1.ª semana) | feliz | "A cama está feita. Esta semana é por conta da casa." |
| `marta_serv_quarto_pago` | **Quarto** (depois da 1.ª semana, sem 8 ❤️) | normal | "Vinte moedas, querid{o/a}. Ou a lista das compras. Escolhe." |
| `marta_serv_quarto_gratis` | **Quarto** com 8+ ❤️ | feliz | "O teu quarto está pronto. Como sempre." |
| `marta_serv_sem_ouro` | sem ouro para o quarto | normal | "Sem dinheiro? Então dormes na mesma. Pagas amanhã. Ou depois. Eu aponto num caderno que depois perco." |
| `marta_serv_dormir` | dormir | normal | "Boa noite. Amanhã há pão quente às seis." |
| `marta_serv_refeicao` | **Refeição** | feliz | "Hoje há {prato}. Senta-te. Come. Depois falas." |
| `marta_serv_refeicao_domingo` | refeição ao domingo | feliz | "Assado de Domingo! Come devagar. É o melhor prato da semana e eu levei três horas a fazê-lo." |
| `marta_serv_cozinha_fechada` | refeição fora de horas | normal | "A cozinha está fechada, querid{o/a}. Mas há pão na cesta. Tira um. Não, tira dois." |
| `marta_serv_receita` | comprar uma receita | feliz | "Esta receita é boa. Era da minha mãe. Agora é tua. Usa-a bem." |
| `marta_serv_fechado` | fora de horas (23:00–5:00) | — | `[Sistema] A Dona Marta está a dormir. O teu quarto está aberto.` |
