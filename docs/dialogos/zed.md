# Zed — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.15. Dados: `dados/dialogos/zed.json`. Rancho: `docs/LOJAS.md`, secção 2.8.
Animais de estimação e montadas: `docs/ATIVIDADES.md`, secção 5.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | baixos, raros, com pausas compridas; o furão faz guinchos agudos por cima |
| Como fala | muito pouco com pessoas: frases de 2 a 6 palavras, muitas vezes "…"; com animais fala muito e com carinho. O furão **Pimpão** "traduz" (guincha e o Zed explica) |
| Repete | "…", "Ele diz olá.", "Animais não mentem.", "Shhh. Está a dormir." |
| Tiques | coça a cabeça do Pimpão quando está nervoso (animação `cocar_furao`); fareja o ar quando alguém chega |
| Nunca diz | o próprio nome verdadeiro (não se lembra); uma frase longa a uma pessoa antes dos 6 corações |
| Chama ao herói | não chama; com 4+ corações, "amig{o/a}"; com 8+ diz `{nome}`, devagar, como quem aprende a palavra |
| Quem é | 40 anos. Ninguém sabe de onde veio. Foi encontrado em criança no **andar 2**, entre uma alcateia de lobos de um mundo engolido que já não existe (cena de 8 ❤️). Os lenhadores trouxeram-no para Ascendia |
| Rotina | Rancho sempre; **1 dia por semana** (ao acaso, nunca ao Domingo) está fora "a buscar um animal ferido" e o Rancho fica com o Pimpão e um bilhete. Ao Domingo à tarde leva os animais a passear pela Praça |

---

## 2. Primeira conversa

- 🎬 O Zed está a escovar uma vaca. Não se vira. O Pimpão sobe-lhe ao ombro e olha para o herói.
- **Zed** *(normal)*: "…"
- 🎬 O Pimpão guincha.
- **Zed** *(normal)*: "Ele diz olá."
- **Zed** *(normal)*: "Zed. Animais. Ovos. …Comida."
- 🎬 O Pimpão guincha mais tempo.
- **Zed** *(feliz, raro)*: "Ele diz que és boa gente. Ele nunca se engana."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Rancho (loja) · Chocar ovos · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `zed_dia_01` | `hora entre 5 e 8` | normal | "…Vacas acordadas. Galinhas também. Eu também. Mais ou menos." |
| `zed_dia_02` | `hora entre 12 e 14` | normal | "Almoço dos animais. Depois o meu. Eles primeiro. Sempre." |
| `zed_dia_03` | `hora entre 20 e 23` | triste | "Os lobos uivam no andar 2. Daqui ouve-se. …Às vezes respondo." |
| `zed_dia_04` | — | normal | "…" *(o Pimpão guincha)* "Ele diz olá." |
| `zed_dia_05` | — | normal | "Animais não mentem. Pessoas sim." |
| `zed_dia_06` | — | feliz | "A vaca Rosinha deu mais leite. Cantei-lhe. Desafinado. Ela não liga." |
| `zed_dia_07` | — | normal | "O Pimpão roubou um ovo. Outra vez. Não é ladrão. É… furão." |
| `zed_dia_08` | — | normal | "Pessoas falam muito. Animais dizem tudo com o rabo." |
| `zed_dia_09` | `dia_semana == domingo && hora entre 14 e 18` | feliz | *(na Praça, com cabras e o furão)* "Passeio. Eles gostam de ver gente. Gente gosta de ver eles. …Eu fico calado." |
| `zed_fora` | dia em que o Zed está fora | — | *(o Pimpão, sozinho, ao balcão, com um bilhete)* `"Fui buscar animal ferido. Volto amanhã. — Z. (O Pimpão vende. Não deixem que ele faça descontos.)"` |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `zed_dia_20` | `estacao == primavera` | feliz | "Primavera. Nascimentos. Três cabritos esta semana. …Bonitos." |
| `zed_dia_21` | `estacao == verao` | normal | "Calor. Água fresca para todos. Sombra para todos. Eu fico ao sol. Não faz mal." |
| `zed_dia_22` | `estacao == outono` | normal | "Outono. Os animais engordam. Sabem que vem o frio. Eu também sei. Não engordo." |
| `zed_dia_23` | `estacao == inverno` | triste | "Inverno. Durmo no estábulo. Mais quente. Mais companhia." |
| `zed_dia_24` | `clima == trovoada` | nervoso | "Trovoada. Os cavalos têm medo. Fico com eles. …Eu também tenho. Um bocadinho." |
| `zed_dia_25` | `clima == chuva` | normal | "Chuva. Os patos estão felizes. São os únicos." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `zed_dia_40` | `boss_derrotado(lobo_cicatriz)` | triste | "O lobo da cicatriz. …Era velho. Era chefe. Os lobos vão chorar uma noite. Depois escolhem outro." |
| `zed_dia_41` | `andar_maximo >= 40` | feliz | "Andar 40. Já podes montar. Montadas. Tenho. Tens dinheiro? Tens coragem? Precisas das duas." |
| `zed_dia_42` | `missao(R5_11) == concluida && flag(mamute_acalmado)` | feliz | "Acalmaste o mamute. Não o mataste. …Obrigado. Ele é velho. Merece acabar a dormir." |
| `zed_dia_43` | `missao(R5_11) == concluida && flag(mamute_morto)` | triste | "Mataste o mamute. …Às vezes é preciso. Às vezes. Não muitas." |
| `zed_dia_44` | `andar_maximo >= 85` | feliz | "Grifos. No céu. Se vires um ovo caído… traz. Com cuidado. Muito cuidado." |
| `zed_dia_45` | `andar_maximo >= 92` | normal | "Lá em cima há uma estrela pequena. Viva. Não sei se é animal. Traz na mesma. Eu descubro." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `zed_dia_60` | `coracoes(zed) >= 2` | normal | "O Pimpão guardou-te uma noz. Está no bolso dele. Não peças. Ele dá quando quiser." |
| `zed_dia_61` | `coracoes(zed) >= 4` | feliz | "Amig{o/a}. …Pronto. Disse. Não foi difícil. Foi um bocadinho." |
| `zed_dia_62` | `coracoes(zed) >= 6` | normal | "Contigo falo mais. Não sei porquê. Talvez porque não falas muito. Também." |
| `zed_dia_63` | `coracoes(zed) >= 8` | triste | "{nome}. …É assim? {nome}. Gosto. É um bom nome. Para pessoa." |
| `zed_dia_64` | `coracoes(zed) >= 10` | feliz | "Tens dois animais agora. Eles gostam um do outro. Eu sabia. Eu disse ao Pimpão. Ele não acreditou." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `zed_dia_70` | `skill_unica == domador_nato` | feliz | "…Os animais olham para ti como olham para mim. És como eu. Quase. Tu falas com pessoas." |
| `zed_dia_71` | `skill_unica == lingua_universal` | surpresa | "Falas com monstros?! …Pergunta ao Pimpão o que pensa de mim. Não. Não perguntes. Não quero saber." |
| `zed_dia_72` | `origem == dormir` | normal | "Dormes muito. Como os gatos. Os gatos são sábios." |
| `zed_dia_73` | `origem == ajudante` | feliz | "Ajudas. Os animais sabem quem ajuda. O Pimpão sabia. No primeiro dia." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `zed_curta_1` | normal | "…" |
| `zed_curta_2` | normal | "Shhh. Está a dormir." *(aponta para uma galinha)* |
| `zed_curta_3` | feliz | *(o Pimpão guincha)* "Ele diz que voltaste. Sim. Já sabia." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Zed** *(normal)*: "A torre? …É uma toca. Grande. Muitos bichos. Muitos mundos de bichos."
- **Zed** *(triste)*: "Os animais da torre não escolheram estar lá. Como eu. Como tu."
- **Zed** *(normal)*: "Por isso trato deles. Alguém tem de tratar."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "Raposas, coelhos, lobos. Bons animais. Não lhes faças mal sem razão." |
| 2 Cavernas | "Morcegos. Ovo de morcego no fosso do 17. Bichinho bom. Faz luz. Traz." |
| 3 Pântano | "Sapos. Sapo pequeno venenoso. Bom amigo. Não lambas." |
| 4 Deserto | "Escaravelho dourado ao pôr do sol. E lagartos para montar. Paciência. Muita." |
| 5 Gelo | "Mamutes. Lobos de gelo. A cria do lobo branco… se a encontrares, traz quente. Muito quente." |
| 6 Oceano | "Cavalos-marinhos. Um está ferido no 56. Leva alga doce. Três dias. Ele vai lembrar-se." |
| 7 Vulcão | "Salamandras. Gostam de calor. E de pimenta. Pimenta da lava. Quem diria." |
| 8 Reino Assombrado | "Gatos fantasmas. …Também são animais. Também precisam de festas. Atravessam a mão. Mas gostam." |
| 9 Céu | "Grifos. Orgulhosos. Respeito primeiro. Carne depois. Montar só no fim." |
| 10 Abismo | "Uma estrela pequena. Perdida. Traz. Ninguém devia estar perdido sozinho." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `zed_rumor_01` | — | "O Slime Rei tem um ovo lá dentro. Slime bebé. Apanha os itens do chão. Útil. E fofo. Mole." |
| `zed_rumor_02` | `andar_maximo >= 5` | "Há um ovo de ouro numa toca pequena do andar 5. Só passa quem for pequeno. Muito pequeno." |
| `zed_rumor_03` | `andar_maximo >= 15` | "No ninho das aranhas há um casulo dourado. Ovo de aranha. Faz seda. Traz. Eu choco." |
| `zed_rumor_04` | `andar_maximo >= 43` | "Pinguins no gelo. Um está sempre sozinho. Fala com ele. Os pinguins sozinhos querem companhia." |
| `zed_rumor_05` | `andar_maximo >= 56` | "Ovo de polvo no 56. Tubarões querem comer. Protege até à bolha. Polvo bebé respira por ti." |
| `zed_rumor_06` | — | "Os lobos da floresta não atacam quem cheira a lobo. Eu cheiro a lobo. Tu não. Ainda." |

### 4.4 A vida dele
| Corações | Fala |
|---|---|
| 0 | "…Zed. Rancho. Animais. Pronto." |
| 2 | "O Pimpão encontrei no andar 3. Preso numa rede. Há seis anos. Ficou. Não o prendi. Ele ficou." |
| 4 | "Não sei de onde vim. Lembro-me de pelos. De calor. De dormir encostado a lobos." |
| 6 | "Os lenhadores do andar 2 encontraram-me. Tinha seis anos. Mordi o Bruno. O pai do Bruno. Ele riu-se. Trouxe-me na mesma." |
| 8 | ver a **cena de 8 ❤️** |
| 10 | "Agora tenho rancho. Animais. Pimpão. E amig{o/a}. …Chega. É muito. É bom." |

---

## 5. Presentes

**Adora:** ovos raros (qualquer ovo de animal de estimação), comida de animais de qualidade Excelente, Ovo de Ouro do Javali ·
**Gosta:** carne, peixe · **Detesta:** quem maltrata animais — **atacar um animal pacífico** (vaca, galinha, Tronco, raposa) perto dele dá −50; e presentes feitos de animais que ele trata (peles de animais da quinta).

| Reação | Falas |
|---|---|
| Adora | 🎬 os olhos do Zed brilham. "…Um ovo. Para mim. …Vou chocar. Vai ser teu. Sempre foi teu." · "Ovo de ouro! O Pimpão vai enlouquecer. Vou escondê-lo. Do Pimpão." |
| Gosta | "Carne. Boa. Para mim e para os gatos. Mais para os gatos." |
| Neutro | "…Obrigado." |
| Não gosta | "…Hmm." *(o Pimpão guincha)* "Ele diz que não gostou. Eu não disse nada." |
| Detesta | "Isto é pele de… não. Leva. Não quero." |

---

## 6. Aniversário e festivais

**Aniversário (Outono, dia 27 — é o dia em que os lenhadores o encontraram; ninguém sabe o verdadeiro):**
- Sem presente: "…Hoje faz anos que me encontraram. Não sei quando nasci. Escolhi este."
- Com presente que adora: "…Lembraste-te. O Pimpão lembrou-se também. Deu-me uma noz. Tu deste-me isto. Bom dia."

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "As abelhas gostam. As cabras comem as flores do concurso. Todos os anos. Peço desculpa. Todos os anos." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "…Não sei dançar. Os lobos não dançam. …Uivam. Posso tentar." ⚙ +100 (o Zed dança muito mal e com muito cuidado) |
| F_02 Festival da Pesca | "Os peixes pequenos devolvo ao rio. O Pip ralha. Eu não ralho de volta." |
| F_03 Noite dos Espíritos | "Os gatos fantasmas vêm ao rancho. Dou-lhes leite. Não bebem. Agradecem na mesma." |
| F_04 Festival da Estrela | "Amigo secreto. …Dou um ovo de galinha decorado. Sempre. A Lyra chora sempre. Não sei porquê." |
| F_05 Dia da Subida | "Muita gente. Muito barulho. Fico ao pé da fonte com os animais. Eles gostam de festas. De longe." |
| F_06 Concurso da Casa | "Se tiveres um animal em casa, ganhas. Para mim. Não sou juiz." |
| F_07 Noite das Lanternas | "Ponho uma lanterna pelos animais que não consegui salvar. É grande. Tem muitos nomes." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "…O rei dos javalis. Velho. Forte. Os javalis vão escolher outro. Sem coroa, espero." |
| Ent Ancião (10) | "A árvore grande morreu. Os pássaros do 10 vão precisar de casa. …Quinta tem árvores. Que venham." |
| Aranha-Mãe (15) | "Ela protegia os ovos. …Trouxeste algum? O dourado? Eu choco. Ela ia querer." |
| Golem de Cristal (20) | "Pedra. Não é animal. …Bem feito." |
| Serpente do Lodo (25) | "Serpente. Guardava um ovo. …De pedra. Não se choca. Pena." |
| Hidra do Pântano (30) | "Sete cabeças. Sete fomes. Coitada. Ninguém dá de comer a sete cabeças." |
| Escorpião Imperador (35) | "Escorpiões. Tocas. Ovos. …Não. Escorpiões não. O Pimpão não deixa." |
| Faraó Eterno (40) | "Montadas a partir de agora. Vem ao rancho. O lagarto da areia está à tua espera. Não muito paciente." |
| Yeti Ancião (45) | "O yeti guardava coisas. Como o Pimpão. …Não lhe digas que os comparei." |
| Dragão de Gelo (50) | "Um dragão. …Dragões têm ovos? Se tiver… traz. Não. Não traz. Sim. Traz." |
| Capitão Esqueleto (55) | "Piratas. Tinham papagaios? Os papagaios dos piratas mortos… onde estão? Vou perguntar." |
| Leviatã (60) | "O Leviatã tinha um ovo. No 58. Não lhe toques. Um dia vai nascer. O mar precisa de um." |
| Ferreiro Infernal (65) | "Salamandras na forja dele. Eram prisioneiras. …Ainda bem." |
| Kai — salvo (68) | "O rapaz voltou. O Pimpão dormiu no colo dele. O Pimpão nunca dorme no colo de ninguém." |
| Kai — vencido (68) | "…Senta-te. Os animais sabem quando alguém está triste. Deixa-os vir. Não digas nada." |
| Titã de Magma (70) | "O vulcão calmo. As salamandras vão dormir. Bem." |
| Lich Bibliotecário (75) | "Livros. Não são animais. …O Fausto ficou contente. Isso conta." |
| Rei Sem Coroa (80) | "O Gorvan veio ao rancho. Fez festas a um cavalo. Uma hora. Não falou. Eu também não. Foi bom." |
| Grifo Real (85) | "A mãe grifo. Protegia os filhos. …Se houver ovo caído, traz. Por favor. Por favor." |
| Serafim Caído (90) | "Asas partidas. Trato muitas. …As tuas não estão partidas. Estão cansadas. Descansa." |
| Guardião do Tempo (95) | "O Pimpão está nervoso. Os animais sabem quando as coisas acabam. Volta. Ele espera." |

---

## 8. Cenas de coração

### ❤️ 2 — O furão que responde

| | |
|---|---|
| ID | `cena_zed_2` |
| Quando | 2 ❤️ · entrar no Rancho entre as 6:00 e as 9:00 |
| Onde | Rancho, cerca das galinhas |
| Quem | herói, Zed, Pimpão |
| Música | `ascendia_dia` (com sons de quinta) |

🎬 O Zed está sentado num balde virado, a falar com o Pimpão. Fala normalmente, frases inteiras.
- **Zed** *(normal)*: "…e a vaca nova não gosta da palha do sul. Prefere a do norte. Achas que é o cheiro? Também acho."
- 🎬 O Pimpão guincha uma vez.
- **Zed** *(feliz)*: "Exato. Foi o que eu disse."
- 🎬 O Zed vê o herói. Fica calado de repente.

▶ **"Ele percebe-te mesmo?"**
▶ **"Continua. Eu não ouvi."**

- *(percebe)* **Zed** *(normal)*: "…Percebe. Mais do que pessoas." 🎬 o Pimpão salta para o ombro do herói. "…Ele percebe-te também. Raro." ⚙ +30
- *(continua)* 🎬 o Zed hesita, depois continua a falar com o Pimpão, mais baixinho. No fim olha para o herói. "…Obrigado." ⚙ +30

⚙ 5% de desconto no Rancho. O Pimpão passa a aparecer às vezes em tua casa (decoração viva, rouba 1 noz por semana).

### ❤️ 4 — O parto da vaca

| | |
|---|---|
| ID | `cena_zed_4` |
| Quando | 4 ❤️ · noite (22:00–2:00), primavera ou verão · entrar no Rancho |
| Onde | estábulo, só com uma lanterna |
| Quem | herói, Zed, a vaca Rosinha |
| Música | sem música; só sons do estábulo |

🎬 O Zed está ajoelhado ao pé da vaca Rosinha, que está deitada e a respirar depressa.
- **Zed** *(nervoso)*: "Vem. Ajuda. Segura a lanterna. Não, mais perto. Não, menos perto."
- 🎬 **Minijogo curto**: segurar a lanterna estável (manter um círculo dentro de outro) enquanto o Zed ajuda o vitelo a nascer.
- 🎬 Nasce um vitelo, todo molhado, que tenta pôr-se de pé e cai três vezes.
- **Zed** *(feliz, raro)*: "…Está bem. Os dois estão bem."
- **Zed** *(normal)*: "Dás um nome? Tu ajudaste. Tu dás."
- ▶ (o jogador escreve um nome para o vitelo) — **Zed**: "…{nome_vitelo}. Bom nome. Ele gosta."

⚙ O vitelo fica no Rancho com o nome escolhido. Recebe a receita de **Comida de Animais Excelente** (felicidade +25).

### ❤️ 6 — O hospital dos animais

| | |
|---|---|
| ID | `cena_zed_6` |
| Quando | 6 ❤️ · no dia seguinte a um dia em que o Zed esteve fora |
| Onde | celeiro de trás do Rancho (só abre nesta cena) |
| Quem | herói, Zed |
| Música | `amizade` |

🎬 O celeiro de trás está cheio de animais da torre com ligaduras: um morcego com a asa partida, uma raposa coxa, um pinguim com o bico remendado, um lagarto sem cauda (a crescer).
- **Zed** *(normal)*: "Ninguém sabe. Os animais da torre que se magoam… trago para aqui. Trato. Depois devolvo."
- **Zed** *(triste)*: "Alguns não voltam. Ficam. Não conseguem. …Esses ficam aqui. Comigo."
- **Zed** *(normal)*: "Agora sabes. Podes ajudar. Se quiseres. Animal ferido na torre: traz. Com cuidado."

⚙ Abre a atividade **Animais Feridos**: às vezes, na torre, aparece um animal ferido (ícone de pata). Trazê-lo ao Zed dá +50 amizade e uma recompensa pequena. Todas as missões de animais (secção 9) passam a dar +50 extra.
⚙ O Zed aceita jantar em tua casa (traz o Pimpão; o Pimpão rouba um talher).

### ❤️ 8 — Os lobos

| | |
|---|---|
| ID | `cena_zed_8` |
| Quando | 8 ❤️ · lua cheia, andar 2, Bosque Escuro, 22:00–2:00 (o Zed vai lá nessas noites) |
| Onde | andar 2, clareira escondida no Bosque Escuro |
| Quem | herói, Zed, uma alcateia de lobos cinzentos |
| Música | `floresta_noite` → `tema_zed` |

🎬 Uma alcateia de lobos à volta do Zed, sentado no chão. Os lobos não atacam. Um lobo velho encosta a cabeça ao ombro dele.
🎬 Os lobos veem o herói e rosnam. O Zed faz um som baixo, de lobo. Os lobos calam-se.
- **Zed** *(normal)*: "Senta. Devagar. Eles cheiram. Depois aceitam."
- **Zed** *(triste)*: "Os meus lobos eram de outro mundo. Pelos cinzentos com riscas azuis. A torre engoliu o mundo deles. Eles vieram parar aqui. Comigo pequeno."
- **Zed** *(triste)*: "Morreram todos. Os lobos daqui não são eles. Mas… são parecidos. Venho cá. Na lua cheia. Para não me esquecer de uivar."
- **Zed** *(normal)*: "Nunca contei a ninguém. …Tu és o primeiro. O segundo foi o Pimpão."
- 🎬 O Zed uiva. Os lobos uivam com ele.

▶ **(Uivar também.)**
▶ **(Ficar em silêncio.)**

- *(uivar)* 🎬 o herói uiva (mal). Os lobos olham. Depois uivam por cima. **Zed** *(a rir, pela primeira vez)*: "Mal. Muito mal. …Outra vez." ⚙ +30 · título *Irm{ão/ã} dos Lobos*
- *(silêncio)* **Zed** *(feliz)*: "Ouvir também é bom. Os lobos também ouvem." ⚙ +30

⚙ 15% de desconto no Rancho. Os **Lobos Cinzentos** dos andares 2–9 deixam de te atacar primeiro (só atacam se lhes bateres). Passa a mandar **cartas** (com uma pena, uma noz do Pimpão ou um desenho de um animal).

### ❤️ 10 — O Apito do Zed

| | |
|---|---|
| ID | `cena_zed_10` |
| Quando | 10 ❤️ · Rancho, ao pôr do sol (18:00–20:00) |
| Onde | colina atrás do Rancho, com todos os animais à volta |
| Quem | herói, Zed, Pimpão, os teus animais de estimação |
| Música | `tema_zed` (flauta de osso e cordas) |

- **Zed** *(normal)*: "Fiz uma coisa. Para ti."
- 🎬 Dá-lhe um apito pequeno de osso, com riscas azuis gravadas.
- **Zed** *(normal)*: "Osso de lobo. Dos meus. Do mundo deles. O último bocado que tenho."
- **Zed** *(feliz)*: "Com o apito, dois animais vêm contigo. Ao mesmo tempo. Eles vão gostar. Não ficam sozinhos em casa."
- 🎬 O herói sopra. Os animais de estimação aparecem os dois, a correr, e brincam um com o outro.
- **Zed** *(feliz)*: "…Vês? Família. Animais fazem família depressa. Pessoas demoram. Nós demorámos. Mas fizemos."

⚙ **Apito do Zed**: podes ter **2 animais de estimação** ao mesmo tempo. Título *Amig{o/a} dos Animais*.

---

## 9. Missões

Fala ao **dar** · fala ao **entregar** (as missões dão-se no Rancho, a partir da região indicada):

| Missão | Dar | Entregar |
|---|---|---|
| R1_06 A Raposa Perdida | (dada pela Tilly; o Zed comenta) "Raposa perdida. Segue as pegadas. Raposas andam em zigue-zague. Para enganar. Não enganam." | "Raposa bonita. Dá-lhe ovos. E deixa-a dormir no teu sapato. Elas gostam de sapatos." |
| R4_13 O Escaravelho Dourado | "Escaravelho dourado. Palmeiral. Ao pôr do sol. Só ao pôr do sol. Devagar. Ele foge da sombra." | "Brilha. Traz sorte. Traz ouro. …Traz também barulho à noite." |
| R5_07 A Cria de Presa-Branca | "A cria do lobo branco ficou sozinha. Leva-a. Quente. Fogueiras pelo caminho. Não a deixes arrefecer." | 🎬 a cria lambe a cara do Zed. "…Vai crescer. Vai ser grande. Vais montá-la. Ela vai deixar. Porque és tu." |
| R6_14 O Cavalo-marinho Ferido | "Cavalo-marinho no 56. Ferido. Alga doce. Três dias seguidos. Não falhes um." | "Ele lembra-se de ti. Vai levar-te pelo mar. Sem ar acabar." |
| R6_15 O Ovo de Polvo | (dada pelo Velho Nalu; o Zed comenta) "Ovo de polvo. Tubarões. Protege. Até à bolha. Eu choco aqui." | "Polvo bebé. Oito braços. Oito abraços. O Pimpão tem ciúmes." |
| R7_09 A Salamandrazinha | "Salamandra bebé numa ilha a afundar. No 62. Rápido. Muito rápido." | "Quentinha. Não lhe toques sem luvas. Ela gosta de ti. Ainda queima." |
| R7_10 Montar na Lava | "Salamandra gigante no 66. Pimenta-lava para acalmar. Não mostres medo. Ela sente." | "Montaste. Na lava. …Os lobos do meu mundo iam rir-se. De orgulho." |
| R9_04 O Ovo Abandonado | "Ovo de grifo caído no 85. A mãe não o encontra. Traz. Protege. É frágil. Muito." | 🎬 o ovo abre-se no Rancho: um grifo bebé espirra penas. "…Pensa que és a mãe. Não lhe digas que não." |
| R9_05 Domar o Grifo | "Grifo selvagem. Carne e pêssegos. Respeito primeiro. Três voltas sem cair." | "Voaste. …Eu nunca voei. Conta-me como é. Devagar." |
| R10_15 A Mini-Estrela | "Uma estrela pequena perdida no 92. Não sei se é animal. Não importa. Está sozinha." | 🎬 a Mini-Estrela brilha na mão do Zed. Ele não diz nada durante muito tempo. "…Está bem. Já não está sozinha." |

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `zed_estado_vida` | `vida_pct < 30` | nervoso | "Ferid{o/a}. …Igreja. Os animais trato eu. Pessoas não sei." |
| `zed_estado_cansado` | `estado(cansado)` | normal | "Cansad{o/a}. Feno ali. Dorme. Ninguém acorda. As vacas não contam." |
| `zed_mau_animal` | atacaste um animal pacífico perto dele | zangado | "…Porquê? Ele não te fez nada. …Vai embora. Hoje não." ⚙ −50 |
| `zed_animal_feliz` | o teu animal de estimação com felicidade máxima | feliz | "O teu animal está feliz. Vê-se no rabo. Tratas bem. Bom." |
| `zed_animal_triste` | o teu animal de estimação com felicidade baixa | triste | "O teu animal está triste. Comida. Festas. Passeio. Hoje." |
| `zed_comp_mia` | `companheiro(mia)` | feliz | "A pequena. Gosta dos cabritos. Os cabritos gostam dela. Deixa-a ficar um bocado." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `zed_serv_abrir` | abrir o Rancho | normal | "Animais. Comida. Montadas. …Escolhe." |
| `zed_serv_comprar_animal` | comprar animal da quinta | feliz | "Trata bem. Todos os dias. Eles lembram-se de quem esquece." |
| `zed_serv_sem_casa` | sem galinheiro ou estábulo | normal | "Precisa de casa. O animal. Primeiro casa, depois animal." |
| `zed_serv_chocar` | chocar um ovo | feliz | "Ovo. Amanhã nasce. Dorme descansad{o/a}. Eu não durmo. Fico a ver." |
| `zed_serv_ovo_nasceu` | ovo chocado | feliz | "Nasceu. Olhou para mim. Depois procurou-te. É teu." |
| `zed_serv_montada` | comprar uma montada | normal | "Montada. Não puxes as rédeas com força. Ela sabe o caminho. Às vezes melhor do que tu." |
| `zed_serv_montada_cedo` | antes do andar 40 | normal | "Montadas depois do 40. Antes, perna. Perna é bom." |
| `zed_serv_sem_ouro` | sem ouro | normal | "…Sem ouro. Volta. Ou traz comida. Para eles. Aceito comida." |
| `zed_serv_fora` | dia em que o Zed está fora | — | `[Sistema] O Zed foi buscar um animal ferido. O Pimpão está ao balcão. (Os preços estão iguais. O Pimpão tentou mudá-los.)` |
