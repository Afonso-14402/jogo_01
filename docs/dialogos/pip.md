# Pip — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.13. Dados: `dados/dialogos/pip.json`.
O minijogo de pesca está em `docs/ATIVIDADES.md` (secção 4.1) e os peixes na secção 10 de cada região.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | graves e lentos, com pausas; às vezes um bocejo a meio da frase (som `bocejo`) |
| Como fala | devagar, frases que acabam em "…"; exagera tudo o que mede (tamanhos, dias, quilos); leva todas as conversas para o rio e os peixes; nunca tem pressa |
| Repete | "Calma…", "Juro pela minha cana.", "Era deste tamanho.", "Os peixes não têm pressa.", "Shh… estão a morder." |
| Tiques | boceja (animação `bocejar`); abre os braços para mostrar o tamanho dos peixes (`deste_tamanho`), cada vez mais abertos |
| Nunca diz | "depressa"; nunca se zanga a sério (o retrato zangado só aparece com trovoada, pressas e lixo no rio) |
| Chama ao herói | `{nome}`; com 4+ corações, "colega" (de pesca) |
| Rotina | cais do Rio 6:00–12:00 · **sesta** no cais 12:00–13:00 · banca de peixe no Mercado 13:00–18:00 · Taberna 19:00–23:00 · **quarta**: andar 3 (Margem Norte, 7:00–17:00) · **sábado**: andar 9 (Cais Velho) ou, com `andar_maximo >= 26`, sábado sim sábado não, Vila Coaxa (andar 26) · **domingo**: dorme de manhã, rio das 14:00 às 20:00 |

Quando o Pip está **a dormir** (sesta, ou antes de o conheceres) não abre o menu: diz uma fala `pip_sono_*` (secção 10).

---

## 2. Primeira conversa

Antes de o conheceres, o Pip está sempre a dormir no cais de Ascendia. A 1.ª conversa é no **andar 3** (Margem Norte):
está encostado a uma pedra, de chapéu na cara, e a boia mexe-se sozinha.

- `[Sistema] O Pip está a dormir.` *(carregar outra vez acorda-o)*
- **Pip** *(surpresa)*: "Hã? Peixe? …Ah. Pessoa. Olá, pessoa."
- **Pip** *(normal)*: "Sou o Pip. Pesco. Estava a pescar de olhos fechados. É uma técnica. Muito avançada."
- **Pip** *(feliz)*: "És Jogador, não és? Tens cara de quem nunca pescou. Não faz mal. Ninguém nasce a pescar. Eu nasci a dormir."
- *(se `origem == dormir`)* **Pip** *(feliz)*: "Também gosto de dormir. És boa gente."
- **Pip** *(normal)*: "Queres aprender? Eu ensino. Devagar. É a única velocidade que eu tenho."

⚙ Oferece a missão **R1_03** (ver secção 9). Abre o menu do Pip: **Conversar · Perguntar sobre… · Missões · Loja · Dar presente**.
⚙ A partir daqui o Pip segue a rotina normal (rio de Ascendia, mercado, taberna).

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `pip_dia_01` | `hora entre 6 e 9` | normal | "Bom dia… ou boa madrugada. Os peixes acordam cedo. Eu acordo com eles. Depois volto a dormir com eles." |
| `pip_dia_02` | `hora entre 6 e 12` | normal | "Shh… estão a morder. …Não. Era o vento." |
| `pip_dia_03` | `hora entre 9 e 12` | feliz | "Ainda nada. Mas o isco está feliz. Já é alguma coisa." |
| `pip_dia_04` | `hora entre 13 e 18` | feliz | "Peixe fresco! Fresquíssimo! Pescado hoje. Ou ontem muito tarde, que é quase hoje." |
| `pip_dia_05` | `hora entre 13 e 18` | normal | "O Tobias diz que eu vendo pouco. Eu digo que ele fala muito. Ficamos quites." |
| `pip_dia_06` | `hora entre 19 e 23` | feliz | "À noite conto histórias na taberna. O Lucien canta-as. Ficam maiores. Gosto quando ficam maiores." |
| `pip_dia_07` | `hora entre 19 e 23` | normal | "Leite morno. É o que eu bebo. O Lucien diz que não é bebida de taberna. Eu digo que é bebida de sono." |
| `pip_dia_08` | — | feliz | "Uma vez pesquei um peixe TÃO grande que o rio ficou vazio." |
| `pip_dia_09` | — | normal | "Os peixes não têm pressa. Eu também não. Por isso nos damos bem." |
| `pip_dia_10` | `coracoes(pip) < 8` | feliz | "Pesquei uma baleia, sabias? No lago do andar 9. Era deste tamanho." 🎬 *abre os braços* |
| `pip_dia_11` | — | normal | "Sabes qual é o segredo da pesca? Esperar. E ter sono. Esperar com sono é mais fácil." |
| `pip_dia_12` | `missao(H_14) != concluida \|\| flag(kai_salvo)` | normal | "O Kai veio pescar uma vez. Esteve três minutos. Disse que os peixes eram lentos. Os peixes disseram o mesmo dele." |
| `pip_dia_13` | `missao(N_LYRA_1) == concluida` | normal | "A Lyra tirou-me um papel da cana enquanto eu dormia. Pensa que não dei por isso. Não dei." |
| `pip_dia_14` | — | feliz | "A Mia quer pescar com o pau dela. Eu disse que um pau é meia cana. Ficou contentíssima." |
| `pip_dia_15` | `dia_semana == domingo` | feliz | "Domingo. Não há banca. Fico aqui ao rio a tarde toda. Também não há pressa. Nunca há." |
| `pip_dia_16` | `dia_semana == segunda` | triste | "Segunda-feira. Os peixes também não gostam. Mordem menos. É ciência." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `pip_dia_20` | `estacao == primavera` | feliz | "Primavera. Os peixes têm bebés. Eu só pesco os grandes. Os pequenos vão para casa crescer." |
| `pip_dia_21` | `estacao == verao` | feliz | "Verão! Época de sestas compridas e do festival. A minha época." |
| `pip_dia_22` | `estacao == verao && hora entre 13 e 16` | normal | "Com este calor até a boia adormece. E eu com ela." |
| `pip_dia_23` | `estacao == outono` | normal | "As folhas caem no rio e os peixes julgam que é comida. Coitados. Eu também já julguei." |
| `pip_dia_24` | `estacao == inverno` | normal | "Inverno. O rio fica lento. Eu também. Somos parecidos." |
| `pip_dia_25` | `estacao == inverno && clima == neve` | feliz | "A margem gelou. Faço um buraco e pesco como no gelo lá de cima. Só que mais perto da cama." |
| `pip_dia_26` | `clima == chuva` | feliz | "Chuva! O melhor tempo para pescar. Os peixes sobem. Eu fico debaixo do chapéu. Chapéu é tudo." |
| `pip_dia_27` | `clima == chuva && andar_maximo >= 2` | normal | "Com chuva, o Peixe-Folha sai no riacho do andar 2. Disfarça-se de folha. Eu disfarço-me de pedra." |
| `pip_dia_28` | `clima == trovoada` | zangado | "Trovoada não. Cana e raios não são amigos. Fico em casa. A dormir. Por segurança." |
| `pip_dia_29` | `clima == nevoeiro && andar_maximo >= 9` | normal | "Nevoeiro… No lago do andar 9, o Rei adora nevoeiro. Entre as cinco e as sete. Não digas a ninguém." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `pip_dia_40` | `missao(R1_03) == concluida && andar_maximo < 11` | feliz | "Já pescas sozinh{o/a}! Daqui a nada pescas melhor do que eu. Daqui a muito. Não tenhas pressa." |
| `pip_dia_41` | `boss_derrotado(ent_anciao)` | feliz | "Vão fazer uma ponte no rio. Os peixes vão ter sombra. Gosto de obras que dão sombra." |
| `pip_dia_42` | `andar_maximo >= 11 && andar_maximo < 21` | normal | "Nas cavernas há peixes sem olhos. Eu às vezes também pesco de olhos fechados. Somos parecidos." |
| `pip_dia_43` | `andar_maximo >= 26` | feliz | "Foste à Vila Coaxa? A Rã-Rã pesca com a língua. É batota. É genial. É batota." |
| `pip_dia_44` | `andar_maximo >= 50 && !flag(melhoria_aquario)` | normal | "Fala-se de um Aquário na cidade. Um peixe de cada região. Imagina: peixes a olhar para nós, para variar." |
| `pip_dia_45` | `flag(melhoria_aquario)` | feliz | "Fui ao Aquário. Fiquei três horas a olhar para a Carpa Dourada. Ela também. Empatámos." |
| `pip_dia_46` | `flag(melhoria_farol)` | normal | "Com o Farol já se pesca de noite no rio. Eu não pesco. Durmo. Mas é bom saber que podia." |
| `pip_dia_47` | `andar_maximo >= 60` | feliz | "Tens um barco no Porto! Posso dormir nele? Só a sesta. Prometo não o afundar. Prometo pouco." |
| `pip_dia_48` | `missao(N_PIP_3) == ativa` | normal | "Já pescaste {n} espécies. Faltam {30-n}. Devagar. Os peixes não fogem. Fogem, mas voltam." |
| `pip_dia_49` | `rank >= C` | feliz | "Rank C! Eu tenho rank de sesta. S. Ou SS. Ninguém me avaliou, mas eu sei." |
| `pip_dia_50` | `missao(H_14) == concluida && !flag(kai_salvo)` | triste | "Guardei um isco para o Kai. Está aqui, numa latinha. Fica cá até ele voltar." |
| `pip_dia_51` | `flag(kai_salvo)` | feliz | "Dei o isco ao Kai. Deitou-o fora. Depois foi buscá-lo. Está tudo bem outra vez." |
| `pip_dia_52` | `andar_maximo >= 91` | normal | "Tão alto… Lá em cima há peixes? Se houver, conta-me. Devagar. Com pormenores." |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `pip_dia_60` | `coracoes(pip) >= 2` | feliz | "Guardei-te o lugar bom da margem. O que tem sombra e uma pedra lisa para as costas." |
| `pip_dia_61` | `coracoes(pip) >= 3` | normal | "Vi-te pescar ontem. Puxas cedo demais. Conta até três. Até quatro. Até adormecer, se der." |
| `pip_dia_62` | `coracoes(pip) >= 4` | feliz | "Colega! …Posso chamar-te colega? Colega de pesca. Já chamei. Agora é tarde." |
| `pip_dia_63` | `coracoes(pip) >= 5` | feliz | "Sonhei contigo. Estavas a pescar e pescaste-me a mim. Foi um sonho bom. Molhado, mas bom." |
| `pip_dia_64` | `coracoes(pip) >= 6` | normal | "Nunca contei a ninguém onde é o meu sítio secreto no rio. Ainda não te conto. Mas já penso em contar." |
| `pip_dia_65` | `coracoes(pip) >= 8` | triste | "Desde que te contei a verdade, as minhas histórias ficaram mais pequenas. Mas mais bonitas, acho." |
| `pip_dia_66` | `coracoes(pip) >= 10` | feliz | "Colega de pesca para sempre. É o maior título que eu sei dar. Maior do que Rei do Lago." |

### 3.5 Origem e Skill Única (raras, 1 vez cada)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `pip_dia_70` | `origem == atrasado` | normal | "Correr? Para quê? O rio não sai do sítio. Senta-te. Respira. Pronto, chegaste." |
| `pip_dia_71` | `origem == jogador` | feliz | "No teu mundo havia jogos de pesca? Pescavas a fingir? Isso é triste. E muito bonito." |
| `pip_dia_72` | `origem == ajudante` | normal | "Ajudas toda a gente. Ajuda-me a mim: senta-te aqui e não faças nada. É difícil, vais ver." |
| `pip_dia_73` | `origem == dormir` | feliz | "Dormir é a melhor coisa do teu mundo e do meu. Pelo menos nisso, os mundos concordam." |
| `pip_dia_74` | `skill_unica == lingua_universal` | feliz | "Falas com monstros? Pergunta aos peixes onde está o Velho Bigodes. E diz-lhes que eu sou boa pessoa." |
| `pip_dia_75` | `skill_unica == sorte_do_heroi` | normal | "Sorte do Herói? Pesca ao pé de mim. Pode ser que pegue." |
| `pip_dia_76` | `skill_unica == domador_nato` | feliz | "Se domas animais, doma um peixe. Ensina-o a vir ter comigo. Era um sonho." |
| `pip_dia_77` | `skill_unica == mao_de_midas` | normal | "Mão de Midas. Toca no meu isco. Se ficar dourado, poupo dinheiro." |

### 3.6 Falas curtas (já falaste hoje)

| ID | Emoção | Fala |
|---|---|---|
| `pip_curta_1` | normal | "Hmm… ainda aqui? Eu também." |
| `pip_curta_2` | normal | "Shh. Peixe. …Não. Folha." |
| `pip_curta_3` | feliz | "Olá outra vez. Já disse olá? Digo outra vez. Não custa." |
| `pip_curta_4` | normal | "Volta amanhã. Ou depois. Não há pressa." |

---

## 4. Perguntar sobre…

### 4.1 A torre

- **Pip** *(normal)*: "A torre? É alta. Muito alta. Cansa só de olhar. Por isso olho para o rio."
- **Pip** *(normal)*: "Os velhos dizem que este rio nasce debaixo da torre e que a água vem de todos os andares. Por isso pesco peixes de todo o lado. Ou por isso digo que pesco."
- **Pip** *(feliz)*: "Se um dia chegares lá acima, vê se há um lago. Se houver, guarda-me um lugar. Com sombra."

### 4.2 O andar atual

O Pip fala da **pesca** na região do andar mais alto a que chegaste.

| Região | Fala |
|---|---|
| 1 Floresta | "Floresta: os peixes são simpáticos. Mordem devagar, para tu aprenderes. Começa pelo ribeiro do andar 3." |
| 2 Cavernas | "Cavernas: peixes sem olhos. Não vêem o isco, cheiram-no. Põe isco que cheire bem. Ou mal. Depende do peixe." |
| 3 Pântano | "Pântano: água castanha, peixes com dentes e sapos que pescam melhor do que eu. Eu vou lá aos sábados, ao 26." |
| 4 Deserto | "Deserto: pesca-se na AREIA. Precisas de Isco de Areia. E de um chapéu. Eu tenho chapéu." |
| 5 Gelo | "Gelo: fazes um buraco, sentas-te, esperas. É como aqui, mas com o rabo gelado. E há um narval que só sai com arpão." |
| 6 Oceano | "Oceano: o mar é um rio sem margem do outro lado. Leva barco. E paciência. Mais paciência do que barco." |
| 7 Vulcão | "Vulcão: pesca na lava. Precisas da Cana Ignífuga do anão Ragnar. A minha cana ardeu só de eu pensar nisso." |
| 8 Reino Assombrado | "Reino Assombrado: os peixes de lá são fantasmas. Pescá-los é fácil. Segurá-los é que é difícil." |
| 9 Céu | "Céu: pesca-se nas nuvens. Lanças para baixo e o peixe vem de cima. Ou ao contrário. Não sei, adormeci." |
| 10 Abismo | "Abismo: dizem que lá em cima se pesca para o teto. Eu fico com o meu rio. Mas conta-me tudo. Devagar." |

### 4.3 Rumores

O Pip diz **1 rumor ou 1 história de pesca por dia** (escolhida ao acaso das que cumprem a condição).

| ID | Condição | Rumor |
|---|---|---|
| `pip_rumor_01` | — | "Atrás da Cascata Alta, no andar 3, há uma gruta. A chave está num ninho na Ilhota. Os pássaros não a usam. Eu também não. Preguiça." |
| `pip_rumor_02` | `andar_maximo >= 9` | "Às três da manhã, no andar 9, os fogos-fátuos levam a uma ilha que só existe de noite. Segui-os uma vez. Adormeci no barco." |
| `pip_rumor_03` | `andar_maximo >= 21` | "No andar 21 há uma cabana de pescador abandonada. Tem um alçapão. Dizem que há lá uma cana boa. E um diário triste." |
| `pip_rumor_04` | `andar_maximo >= 26` | "Na Vila Coaxa, a Rã-Rã faz um concurso de pesca. Quem ganha leva um sapinho. Eu fiquei em segundo. Contra sapos." |
| `pip_rumor_05` | `andar_maximo >= 26` | "O Velho Bigodes só morde com maré alta, à noite e com chuva. Tudo junto. É um peixe muito exigente." |
| `pip_rumor_06` | `andar_maximo >= 29` | "O Coro dos Sapos perdeu um cantor. Se o encontrares, dão-te uma ocarina. Tocar ocarina atrai peixes raros. E sapos." |
| `pip_rumor_07` | `andar_maximo >= 31` | "No deserto pesca-se na areia, com Isco de Areia. Eu vendo-o. Não é publicidade. É um bocadinho." |
| `pip_rumor_08` | `andar_maximo >= 62` | "O anão Ragnar faz canas que não ardem. Para pescar na LAVA. Gente corajosa ou gente sem sono." |
| `pip_rumor_09` | `andar_maximo >= 76` | "No Reino Assombrado há uma fonte seca que só se enche na lua nova. À meia-noite há lá um peixe preto como o céu." |

**Histórias de pesca** — uma por cada peixe da torre (6 por região). Ninguém sabe quais são verdade.
Das regiões 7 a 10 o Pip só "ouviu dizer" ou "sonhou".

| ID | Peixe | Condição | História |
|---|---|---|---|
| `pip_historia_01` | Truta do Ribeiro | — | "Pesquei uma truta tão rápida que chegou à frigideira antes de mim. Ainda me esperou." |
| `pip_historia_02` | Perca Prateada | — | "A Perca Prateada brilha tanto que uma vez me penteei nela. Ela não gostou. Eu fiquei bem penteado." |
| `pip_historia_03` | Peixe-Folha | `andar_maximo >= 2` | "Uma vez pesquei uma folha durante uma hora. Achava que era um Peixe-Folha. Era mesmo uma folha. Boa luta, na mesma." |
| `pip_historia_04` | Carpa Dourada | `andar_maximo >= 9` | "Uma Carpa Dourada pagou-me o jantar. Pronto, vendi-a. Mas gosto de dizer que ela pagou." |
| `pip_historia_05` | Enguia do Musgo | `andar_maximo >= 8` | "Uma Enguia do Musgo enrolou-se à minha perna e levou-me a passear pelas ruínas. Bom passeio. Pouco seco." |
| `pip_historia_06` | Rei do Lago Nevoento | `andar_maximo >= 9` | "O Rei do Lago tem bigodes de névoa. Puxei-o três dias. Ao terceiro foi ele que me puxou a mim. Ganhou ele." |
| `pip_historia_07` | Peixe-Cego | `andar_maximo >= 14` | "O Peixe-Cego não me vê e eu não o vejo. Somos amigos assim, às escuras. Dá muito jeito para dormir." |
| `pip_historia_08` | Caranguejo de Gruta | `andar_maximo >= 14` | "Um Caranguejo de Gruta roubou-me o isco, a linha e uma bota. Ainda anda por lá com a bota. Fica-lhe bem." |
| `pip_historia_09` | Carpa de Cristal | `andar_maximo >= 13` | "A Carpa de Cristal canta quando a tiras da água. Desafinada. Igual ao Lucien. Não digas ao Lucien." |
| `pip_historia_10` | Truta Fúngica | `andar_maximo >= 16` | "A Truta Fúngica tem cogumelos nas costas. Os fungoides de Mycélia acham que é prima deles. Pedem-ma de volta." |
| `pip_historia_11` | Enguia Elétrica | `andar_maximo >= 14` | "Uma Enguia Elétrica deu-me um choque e fiquei com o cabelo em pé uma semana. Ninguém viu. Tenho chapéu." |
| `pip_historia_12` | Peixe de Vidro | `andar_maximo >= 19` | "Pesquei um Peixe de Vidro e só dei por ele em casa, no balde, a olhar para mim. Transparente e ofendido." |
| `pip_historia_13` | Bagre do Lodo | `andar_maximo >= 21` | "O Bagre do Lodo tem bigodes maiores do que os do Tobias. Não digas ao Tobias. O bagre já sabe." |
| `pip_historia_14` | Enguia de Lama | `andar_maximo >= 22` | "Pesquei a mesma Enguia de Lama quatro vezes no mesmo minuto. Ela escorrega. Eu também, de cansaço." |
| `pip_historia_15` | Piranha | `andar_maximo >= 23` | "Uma Piranha comeu-me o isco, a linha e meia cana. A outra metade guardei. Para ela não ficar com tudo." |
| `pip_historia_16` | Pirarucu | `andar_maximo >= 26` | "Um Pirarucu puxou o meu barco de um canal ao outro. Poupei nos remos. Agradeci-lhe." |
| `pip_historia_17` | Peixe-Arco-Íris | `andar_maximo >= 27` | "O Peixe-Arco-Íris tem as cores todas. Menos uma. Há anos que tento descobrir qual." |
| `pip_historia_18` | O Velho Bigodes | `andar_maximo >= 26` | "O Velho Bigodes partiu-me três canas. À quarta, parti-a eu, de raiva. Ele riu-se. Eu ouvi." |
| `pip_historia_19` | Tilápia Azul | `andar_maximo >= 32` | "Na lagoa de Zahra as Tilápias Azuis fazem fila para morder o isco. Peixes muito bem-educados." |
| `pip_historia_20` | Peixe-Areia | `andar_maximo >= 31` | "Lancei a linha numa duna e saiu um peixe. E um escaravelho. E uma sandália que perdi há um ano noutro andar." |
| `pip_historia_21` | Siluro Salgado | `andar_maximo >= 33` | "O Siluro Salgado já vem temperado. Só é preciso assar. É o peixe mais simpático do mundo." |
| `pip_historia_22` | Peixe-Escaravelho | `andar_maximo >= 39` | "O Peixe-Escaravelho bate no anzol antes de morder. Toc, toc. Gosto de peixes educados." |
| `pip_historia_23` | Peixe do Oásis Verdadeiro | `andar_maximo >= 32` | "O Peixe do Oásis Verdadeiro só morde ao meio-dia. Ao meio-dia e um já está a dormir. Somos iguais." |
| `pip_historia_24` | O Faraó das Águas | `andar_maximo >= 32` | "Quando pescas o Faraó das Águas tens de fazer uma vénia. Senão volta para a água, ofendido. Eu fiz duas." |
| `pip_historia_25` | Caranguejo-Neve | `andar_maximo >= 41` | "Um Caranguejo-Neve fez-me um boneco de neve com as pinças. O nariz ficou torto. Não lhe disse." |
| `pip_historia_26` | Bacalhau Ártico | `andar_maximo >= 43` | "Pesquei um Bacalhau Ártico tão grande que tive de alargar o buraco no gelo. Agora é um lago. Chama-se Pip." |
| `pip_historia_27` | Salmão do Gelo | `andar_maximo >= 42` | "Os Salmões do Gelo sobem o rio aos saltos. Um saltou para a minha mochila. Poupou-me o trabalho todo." |
| `pip_historia_28` | Peixe-Lanterna Gelado | `andar_maximo >= 44` | "Li um livro inteiro à luz de um Peixe-Lanterna Gelado. Ele também leu. Gostou mais do fim do que eu." |
| `pip_historia_29` | Truta Aurora | `andar_maximo >= 48` | "A Truta Aurora muda de cor com o céu. Ficou verde, roxa e laranja. Eu fiquei de boca aberta. E com frio." |
| `pip_historia_30` | Narval Real | `andar_maximo >= 43` | "Um Narval Real furou-me o barco com o chifre. Depois tapou o buraco com o chifre. Ficámos ali os dois. Muito tempo." |
| `pip_historia_31` | Sardinha | `andar_maximo >= 51` | "Pesquei mil Sardinhas de uma vez. Ou foi uma Sardinha mil vezes. Eram todas iguais." |
| `pip_historia_32` | Robalo | `andar_maximo >= 52` | "Um Robalo saltou para o meu barco e pôs-se ao leme. Levou-me ao cais. Bom robalo. Mau a estacionar." |
| `pip_historia_33` | Peixe-Palhaço | `andar_maximo >= 54` | "O Peixe-Palhaço conta piadas. São más. Ri-me por educação. Ele percebeu. Ficou triste." |
| `pip_historia_34` | Atum Azul | `andar_maximo >= 52` | "Um Atum Azul puxou o meu barco até ao horizonte. Lá não havia nada. Voltámos. Foi simpático da parte dele." |
| `pip_historia_35` | Peixe-Lua | `andar_maximo >= 56` | "O Peixe-Lua é redondo e preguiçoso. Ficámos os dois a boiar uma tarde inteira. O melhor dia do verão." |
| `pip_historia_36` | Celacanto Ancião | `andar_maximo >= 58` | "O Celacanto Ancião é mais velho do que a torre. Disse-mo com os olhos. Os olhos dele falam muito devagar." |
| `pip_historia_37` | Caranguejo de Basalto | `andar_maximo >= 62` | "Um anão do Clã Brasa usa um Caranguejo de Basalto como martelo. O Brom quis comprá-lo. Ao caranguejo." |
| `pip_historia_38` | Peixe dos Géiseres | `andar_maximo >= 66` | "Dizem que nas termas do 66 os peixes saem do géiser já cozidos. Só falta o sal. Acredito em tudo o que vem cozido." |
| `pip_historia_39` | Carpa Negra | `andar_maximo >= 63` | "A Carpa Negra é tão escura que de noite só se lhe vê o sorriso. Peixes não sorriem. Esta, dizem, sorri." |
| `pip_historia_40` | Peixe-Brasa | `andar_maximo >= 62` | "Um Peixe-Brasa aqueceu a lareira da taberna uma semana inteira. Pelo menos foi o que o Lucien cantou." |
| `pip_historia_41` | Enguia de Magma | `andar_maximo >= 67` | "Uma Enguia de Magma derreteu a linha, o anzol e as sobrancelhas de um pescador. As sobrancelhas voltaram. A linha não." |
| `pip_historia_42` | Fénix das Profundezas | `andar_maximo >= 70` | "A Fénix das Profundezas arde e volta ao magma. Pescas outra vez, arde outra vez. Dizem que dá para um dia inteiro." |
| `pip_historia_43` | Lúcio Assombrado | `andar_maximo >= 71` | "Dizem que o Lúcio Assombrado assusta os outros peixes. Comigo não resultava. Eu bocejava e ele fugia." |
| `pip_historia_44` | Peixe-Fantasma | `andar_maximo >= 72` | "Sonhei que punha um Peixe-Fantasma no balde. O balde ficava vazio, mas pesava o mesmo. Foi um sonho muito preciso." |
| `pip_historia_45` | Enguia da Cripta | `andar_maximo >= 74` | "Dizem que a Enguia da Cripta é a mais calada de todas. A companhia de pesca perfeita. Depois de ti." |
| `pip_historia_46` | Peixe-Vitral | `andar_maximo >= 77` | "O Peixe-Vitral tem escamas de vidro colorido. Com sol, desenha no chão. Uma vez desenhou um peixe. Ele próprio." |
| `pip_historia_47` | Truta de Prata Negra | `andar_maximo >= 78` | "Uma Truta de Prata Negra vale tanto que o Tobias se ajoelhou quando a viu. À truta. Não a mim." |
| `pip_historia_48` | Peixe da Lua Negra | `andar_maximo >= 76` | "O Peixe da Lua Negra só aparece sem lua. Pescá-lo de olhos fechados é a minha especialidade. Em teoria." |
| `pip_historia_49` | Peixe-Nuvem | `andar_maximo >= 81` | "Sonhei que pescava nas nuvens. Apanhei um Peixe-Nuvem e ele choveu-me em cima. Era um peixe muito emotivo." |
| `pip_historia_50` | Peixe-Voador | `andar_maximo >= 82` | "Um Peixe-Voador bate-te na cara e foge. Conta como pescado? Eu conto. Tu também podes contar, eu deixo." |
| `pip_historia_51` | Truta Celeste | `andar_maximo >= 84` | "A Truta Celeste sobe as cascatas ao contrário. Eu tentei, num sonho. Não dá. Nem a sonhar." |
| `pip_historia_52` | Peixe-Estrela | `andar_maximo >= 86` | "Dizem que o Peixe-Estrela concede um desejo. Se o pescares, pede uma sesta para mim. Comprida." |
| `pip_historia_53` | Enguia Relâmpago | `andar_maximo >= 87` | "Uma Enguia Relâmpago caiu do céu numa cana. Ou a cana caiu na enguia. Foi tão rápido que ninguém sabe." |
| `pip_historia_54` | O Peixe-Sol | `andar_maximo >= 89` | "O Peixe-Sol é tão quente que se pesca com luvas de forno e óculos escuros. E chapéu. Chapéu é sempre preciso." |
| `pip_historia_55` | Peixe-Cometa | `andar_maximo >= 92` | "Ouvi dizer que os Peixes-Cometa deixam um rasto de luz num mar de estrelas. Se seguires um, leva-te a casa. Qual casa, não sei." |
| `pip_historia_56` | Peixe-Espelho | `andar_maximo >= 93` | "Sonhei que pescava um Peixe-Espelho e me via a mim a pescar. Acenei. Eu acenei de volta. Fui simpático." |
| `pip_historia_57` | Carpa do Tempo | `andar_maximo >= 95` | "A Carpa do Tempo nada para trás. Se a pescares amanhã, já a pescaste ontem. Dói-me a cabeça só de pensar." |
| `pip_historia_58` | Peixe Invertido | `andar_maximo >= 96` | "Há um lago no teto onde se pesca para cima. O sangue vai à cabeça e o peixe à barriga. Ou ao contrário." |
| `pip_historia_59` | Peixe-Memória | `andar_maximo >= 97` | "O Peixe-Memória faz-te lembrar coisas. Se o pescares, devolve-o. As memórias são dele. Só as empresta." |
| `pip_historia_60` | O Peixe do Princípio | `boss_derrotado(administrador)` | "Dizem que no topo há um peixe que estava lá antes da torre. Pescaste-o? Não me contes. Quero continuar a sonhar com ele." |

### 4.4 A vida dele

| Corações | Fala |
|---|---|
| 0 | "Eu? Pesco. Durmo. Pesco a dormir. É uma vida boa. Recomendo." |
| 2 | "A minha avó Nita ensinou-me a pescar neste rio. Dizia: 'Quem espera, pesca.' Eu esperei tanto que adormeci. Ela riu-se." |
| 4 | "Já tentei ser aventureiro. Durou um dia. Adormeci numa escolta. O mercador chegou sozinho. Ainda bem que chegou." |
| 6 | "Vivo num barco velho virado ao contrário, ao pé do cais. Chove lá dentro só um bocadinho. Ouve-se o rio a noite toda." |
| 8 | "Nunca pesquei uma baleia. Pronto. Já sabes. Mas uma vez pesquei um tronco do tamanho de uma baleia. Isso conta um bocadinho." |
| 10 | "Metade das minhas histórias são verdade. A outra metade devia ser. Contigo, quero que sejam todas verdade." |

---

## 5. Presentes

**Adora:** peixes lendários, Isco Dourado · **Gosta:** peixes raros, Almofada (e tudo o que sirva para uma sesta) ·
**Detesta:** lixo de pesca (Bota Velha, Lata), Gel de Slime. O resto é **neutro**.
"Detesta pressas" não é um item: as **escolhas de diálogo** apressadas dão −30 (ver `docs/SISTEMAS.md`, secção 15).

| Reação | Falas (escolhe uma) |
|---|---|
| Adora | "Para mim?! …Preciso de me sentar. Já estou sentado. Preciso de me deitar." · "Isto é… deste tamanho. De felicidade." 🎬 *abre os braços até ao fim* |
| Gosta | "Que bonito. Obrigado, {nome}. Vou pô-lo debaixo do chapéu, que é onde guardo as coisas boas." · "Um peixe raro! Vou dizer a toda a gente que foste tu que o pescaste. Com exagero." |
| Neutro | "Ah… obrigado. Vou pensar no que fazer com isto. Amanhã. Ou depois." · "Hmm. Não é peixe. Mas é simpático." |
| Não gosta | "Ah. Isto… não flutua, pois não? Pronto. Obrigado na mesma." |
| Detesta | "Uma bota. Eu tiro botas do rio todos os dias. Não preciso de mais uma. A sério." · "Gel de Slime. Os peixes fogem disto. Eu também." |

**Itens com fala própria:**

| Item | Fala |
|---|---|
| Rei do Lago Nevoento | "O Rei! Não posso aceitar. …Posso? Vamos devolvê-lo ao lago. Os dois. Amanhã de manhã, com nevoeiro." |
| O Velho Bigodes | "O Velho Bigodes! O que me partiu quatro canas! Olá, velho. Afinal és mais pequeno ao perto." |
| Isco Dourado | "Isco Dourado. Brilha como o sol às sete da manhã. A minha hora preferida para não estar acordado." |
| Almofada | "Uma almofada! Tu percebes-me. Vou testá-la. Agora. …Zzz." 🎬 *adormece em cima dela* |
| Truta Grelhada | "A receita que te ensinei! Está melhor do que a minha. Tem sal a mais. Não, está bem assim." |
| Peixe-Memória | "Um Peixe-Memória… Lembrei-me da minha avó. A sorrir, no cais. Obrigado. Vou devolvê-lo ao rio. Ele merece." |

---

## 6. Aniversário e festivais

**Aniversário (Verão, dia 9):**
- Sem presente: **Pip** *(feliz)*: "Faço anos hoje. Vou comemorar com uma sesta extra. Duas, se for um bom ano."
- Com presente que adora: **Pip** *(feliz)*: "No dia dos meus anos! Vou guardá-lo. Não, vou usá-lo. Não, guardá-lo. …Amanhã decido."
- Com outro presente: **Pip** *(feliz)*: "Um presente! Vou abri-lo devagar. Muito devagar. Volta daqui a uma hora."
- 🎬 Nesse dia o Pip não vende peixe: está o dia todo no cais, e quem passa deixa-lhe uma almofada (há uma pilha delas).

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "As flores não precisam de festa, só de sol. Eu também. Vou deitar-me no meio delas." |
| F_01 (convite para dançar, 4+ ❤️) | ▶ **"Danças comigo?"** → **Pip** *(surpresa)*: "Dançar? Eu? Devagarinho, está bem? Uma dança de sesta." ⚙ dança · +100 amizade |
| F_02 Festival da Pesca | "Eu sou o juiz. Ganhei sete anos seguidos e proibiram-me de concorrer. Ainda bem. Cansava." |
| F_02 (4+ ❤️) | "O juiz não dá dicas. Mas se o juiz lançasse, lançava para a sombra do cais. Não ouviste nada." |
| F_02 (ganhaste) | "Rei da Pesca! O meu título de antigamente. Trata-o bem. Dá-lhe sestas." |
| F_03 Noite dos Espíritos | "Dizem que nesta noite os peixes-fantasma sobem o rio. Eu nunca vi. Adormeço sempre antes da meia-noite." |
| F_04 Festival da Estrela | "Amigo secreto. Se te calhar eu… uma almofada. Só estou a dizer. Uma almofada muda vidas." |
| F_05 Dia da Subida | "Dia da Subida! Comida grátis. A minha festa preferida, logo a seguir à sesta." |
| F_06 Concurso da Casa | "A minha casa é um barco virado ao contrário. O júri diz que não conta. O júri não sabe o que perde." |
| F_07 Noite das Lanternas | *(triste)* "Fico na curva do rio, com a cana. Quando uma lanterna fica presa nos juncos, solto-a. Todas têm de chegar ao fim." |

---

## 7. Depois dos bosses

1.ª conversa depois de cada vitória (ver a prioridade no `README.md`).

| Boss | ID | Fala |
|---|---|---|
| Javali-Rei (5) | `pip_boss_javali_rei` | "Venceste o javali grande! Eu uma vez pesquei um javali. Caiu ao rio e eu puxei. Conta como pesca." |
| Ent Ancião (10) | `pip_boss_ent_anciao` | "A floresta está livre. Os ribeiros lá de cima vão correr mais limpos. Os peixes agradecem. Eu também." |
| Aranha-Mãe (15) | `pip_boss_aranha_mae` | "Uma aranha gigante. Com aquelas teias fazia-se uma rede de pesca do tamanho de uma praça." |
| Golem de Cristal (20) | `pip_boss_golem_cristal` | "Um golem de cristal. Brilhava? Os peixes adoram coisas que brilham. Guardaste um bocadinho? Para isco." |
| Serpente do Lodo (25) | `pip_boss_serpente_lodo` | "Uma serpente do lodo é quase uma enguia. Uma enguia muito grande e muito zangada. Parabéns." |
| Hidra do Pântano (30) | `pip_boss_hidra_pantano` | "Uma hidra! Muitas cabeças. Eu tenho uma e já me cansa. Imagina sete." |
| Escorpião Imperador (35) | `pip_boss_escorpiao_imperador` | "Um escorpião no deserto. E lá pesca-se na areia, sabias? Era isso que eu queria perguntar." |
| Faraó Eterno (40) | `pip_boss_farao_eterno` | "Um faraó amaldiçoado. Aqui no rio também há maldições. Chama-se segunda-feira." |
| Yeti Ancião (45) | `pip_boss_yeti_anciao` | "Um yeti! Tinha frio? Eu fazia-lhe um buraco no gelo para pescar. Era um bom yeti, aposto." |
| Dragão de Gelo (50) | `pip_boss_dragao_gelo` | "Metade da torre! Vou fazer uma sesta em tua honra. Uma comprida. A mais comprida do ano." |
| Capitão Esqueleto (55) | `pip_boss_capitao_esqueleto` | "Um capitão pirata. Tinha papagaio? Os papagaios comem peixe? Pergunto por perguntar." |
| Leviatã (60) | `pip_boss_leviata` | *(triste)* "Venceste o maior peixe da torre. Não era peixe? Era quase. E o Kai… ainda não voltou." |
| Ferreiro Infernal (65) | `pip_boss_ferreiro_infernal` | "Um ferreiro do inferno. O Brom diz que não é colega dele. Diz muito alto. Muitas vezes." |
| Kai — salvo (68) | `pip_boss_kai_salvo` | "O Kai voltou! Vou dar-lhe o isco que guardei. Ele vai deitá-lo fora. Depois vai buscá-lo. Conheço-o." |
| Kai — vencido (68) | `pip_boss_kai_vencido` | *(triste)* "Não digo nada. Senta-te aqui no cais. A água não faz perguntas. Eu também não." |
| Titã de Magma (70) | `pip_boss_tita_magma` | "Um titã de lava. Há peixes na lava, sabias? O Ragnar diz que sim. Eu digo que sim também, para não discutir." |
| Lich Bibliotecário (75) | `pip_boss_lich_bibliotecario` | "O Velho Fausto chorou de alegria. Eu chorei de sono. Choramos todos, cada um à sua maneira." |
| Rei Sem Coroa (80) | `pip_boss_rei_sem_coroa` | "O Mestre Gorvan passou pelo rio. Sentou-se onde se sentava antigamente. Desta vez sorriu." |
| Grifo Real (85) | `pip_boss_grifo_real` | "Penas de grifo dão boas boias. Eu digo isto de tudo. Mas desta vez é verdade." |
| Serafim Caído (90) | `pip_boss_serafim_caido` | *(triste)* "Estás calad{o/a}. Senta-te. Pesca comigo um bocado. Não precisas de dizer nada. Os peixes também não dizem." |
| Guardião do Tempo (95) | `pip_boss_guardiao_tempo` | "Um guardião do tempo. Pede-lhe mais tempo para mim. Para sestas. Ou não. Vence-o na mesma." |

> Depois do **Administrador** (andar 100) as falas dependem do final: ver `docs/guiao/finais.md`.

---

## 8. Cenas de coração

### ❤️ 2 — A cana que puxa

| | |
|---|---|
| ID | `cena_pip_2` |
| Quando | 2 ❤️ · de segunda a sábado · `clima == sol` · ir ao cais do Rio entre as 9:00 e as 12:00 |
| Onde | Rio e Porto, ponta do cais |
| Quem | herói, Pip |
| Música | `ascendia_dia` (versão calma) |

🎬 O Pip dorme sentado na ponta do cais, de cana na mão. A cana dobra-se toda. O Pip escorrega devagar para a água, a dormir.

▶ **Acordar o Pip.**
▶ **Segurar a cana por ele.**
▶ **Segurar o Pip pelo cinto.**

- *(acordar)* **Pip** *(surpresa)*: "Hã? …PEIXE! Calma. Calma, Pip. Calma, peixe. Ajuda-me, {nome}!"
- *(cana)* 🎬 O Pip continua a dormir. **Pip** *(a dormir)*: "…mais para a esquerda… era deste tamanho…" ⚙ +30
- *(cinto)* 🎬 Seguras o Pip enquanto ele, a dormir, puxa a cana. **Pip** *(a dormir)*: "…obrigado, avó…" ⚙ +30

⚙ Minijogo de pesca (não se pode perder). Sai uma **Perca Prateada** enorme.

- **Pip** *(feliz)*: "Uma perca deste tamanho." 🎬 *abre os braços* "…E desta vez é mesmo deste tamanho. Pela primeira vez."
- **Pip** *(normal)*: "Pescaste-a com a minha cana. Ou eu pesquei-a com as tuas mãos. É nossa. Fica tu com ela."

⚙ **Perca Prateada** (qualidade Excelente) · 5% de desconto na loja do Pip.

### ❤️ 4 — Pôr do sol no rio

| | |
|---|---|
| ID | `cena_pip_4` |
| Quando | 4 ❤️ · domingo · ir à margem do Rio entre as 18:00 e as 20:00 |
| Onde | margem do Rio de Ascendia, à sombra do cais (ou debaixo da Ponte do Rio, se já existir) |
| Quem | herói, Pip |
| Música | `amizade` |

🎬 O Pip tem duas canas espetadas na margem. Dá-te uma sem dizer nada.

- **Pip** *(normal)*: "Trouxe duas. Uma é para ti. Não é presente, é empréstimo. Até ao pôr do sol."

⚙ Minijogo de pesca a dois (o Pip pesca ao teu lado; ninguém perde).

- **Pip** *(normal)*: "A minha avó Nita pescava aqui. Dizia: 'Quem espera, pesca.'"
- **Pip** *(normal)*: "Toda a gente em Ascendia corre. Para a torre, para a Guilda, para o mercado."
- **Pip** *(feliz)*: "Alguém tem de ficar parado a ver o rio. Senão, quem é que vê o rio?"

▶ **"Eu fico a ver contigo."**
▶ **"Não te aborreces?"**
▶ *(bocejar)*

- *(ficar)* **Pip** *(feliz)*: "…Obrigado, colega. Posso chamar-te colega? Já chamei." ⚙ +30
- *(aborreces)* **Pip** *(normal)*: "O rio nunca é igual. Hoje, por exemplo, tem mais uma pessoa a olhar para ele."
- *(bocejar)* **Pip** *(surpresa)*: "Bocejaste! Estás a aprender. É o primeiro passo." ⚙ +30
- 🎥 O sol desce atrás da muralha. Duas sombras no rio cor de laranja, a torre ao fundo.
- 🎬 O Pip tira do chapéu um caderno húmido, cheio de desenhos de peixes.
- **Pip** *(normal)*: "É o meu caderno de pesca. Tem todos os peixes que sei. E alguns que inventei. Não te digo quais."

⚙ Recebe o **Caderno de Pesca do Pip** (no Diário, mostra onde e quando aparece cada peixe que ainda não pescaste).
⚙ Abre a missão **N_PIP_3 Todos os Peixes**.

### ❤️ 6 — O Rei do Lago

| | |
|---|---|
| ID | `cena_pip_6` |
| Quando | 6 ❤️ · `andar_maximo >= 9` · entrar na Taberna entre as 20:00 e as 23:00 |
| Onde | Taberna "O Primeiro Degrau", mesa ao pé da lareira |
| Quem | herói, Pip, Lucien (ao fundo) |
| Música | `taberna` (versão calma) |

🎬 O Pip tem um copo de leite morno nas mãos. Está acordado. Muito acordado, para o Pip.

- **Lucien** *(feliz, de longe)*: "Pip! Conta a da baleia! A da baleia!"
- **Pip** *(normal)*: "Hoje não, Lucien. Hoje conto uma verdadeira."
- **Pip** *(normal)*: "No lago do andar 9 vive o Rei do Lago Nevoento. Bigodes de névoa. Olhos de lua."
- **Pip** *(normal)*: "A minha avó viu-o uma vez. Eu vejo-o todos os anos, nos dias de nevoeiro, entre as cinco e as sete."
- **Pip** *(triste)*: "Nunca o apanhei. Parti seis canas. Ele olha para mim antes de fugir. Acho que se ri."
- **Pip** *(triste)*: "Toda a gente acha que é mais uma história minha. Às vezes até eu acho."
- **Pip** *(normal)*: "Pesca-o tu. Não é para mim. É para eu saber que é verdade."

▶ **"Eu pesco-o."**
▶ **"Vamos os dois."**

- *(pesco)* **Pip** *(feliz)*: "Leva isco bom. E paciência. Mais paciência do que isco."
- *(os dois)* **Pip** *(surpresa)*: "Os dois? …Está bem. Mas quem puxa és tu. Eu seguro o chapéu." ⚙ +30

⚙ Missão **R1_10 O Rei do Lago** iniciada. O Pip aceita jantar em tua casa (se tiveres casa).

### ❤️ 8 — A baleia

| | |
|---|---|
| ID | `cena_pip_8` |
| Quando | 8 ❤️ · sábado · chegar ao Cais Velho do andar 9 entre as 8:00 e as 12:00 |
| Onde | andar 9, Lago da Névoa, de barco a remos |
| Quem | herói, Pip |
| Música | `aurora` (versão calma) |

🎬 O Pip espera sentado no barco a remos. Faz-te sinal para entrares.

- **Pip** *(normal)*: "Senta-te. Quero mostrar-te uma coisa. Rema tu. Eu já remei o ano passado."
- 🎥 O barco entra no nevoeiro. Do branco sai uma sombra enorme: um tronco gigante a boiar, com dois nós que parecem olhos.
- **Pip** *(feliz)*: "Apresento-te a baleia."
- **Pip** *(normal)*: "Eu tinha dezassete anos. Nevoeiro. Senti uma coisa ENORME na linha. Puxei três horas."
- **Pip** *(normal)*: "Quando o nevoeiro abriu, era isto. Um tronco. Com dois nós que pareciam olhos."
- **Pip** *(triste)*: "Voltei a Ascendia e toda a gente perguntou: 'Então, Pip?' Eu disse: 'Pesquei uma baleia.' E riram-se. Tão contentes…"
- **Pip** *(triste)*: "Nunca mais desdisse. Era a melhor coisa que eu tinha para dar às pessoas: uma história grande."

▶ **"É a melhor história de pesca."**
▶ **"Porque me contas agora?"**
▶ **"A baleia está a afundar."**

- *(melhor)* **Pip** *(feliz)*: "Pois é! E ainda por cima é verdade. Quer dizer… é verdade que é mentira." ⚙ +30
- *(porquê)* **Pip** *(normal)*: "Porque a ti não preciso de dar histórias grandes. Basta estares aqui." ⚙ +30
- *(afundar)* 🎬 O tronco afunda devagar (ficaram parados mais de 2 s). **Pip** *(surpresa)*: "Ah. Sim. Ela faz isso. Rema, colega. REMA."

⚙ 15% de desconto na loja. A fala `pip_dia_10` (a baleia) deixa de aparecer.
⚙ O Pip passa a mandar **cartas** (1 por semana): um isco, um peixe do dia ou um desenho de um peixe "deste tamanho" (cada vez maior).

### ❤️ 10 — A cana do Pip

| | |
|---|---|
| ID | `cena_pip_10` |
| Quando | 10 ❤️ · `missao(R1_10) == concluida` · ir ao cais do Rio entre as 5:00 e as 6:00 |
| Onde | Rio e Porto, ponta do cais, de madrugada |
| Quem | herói, Pip |
| Música | `tema_pip` (flauta + acordeão) |

🎬 O Pip está de pé, acordado, ao nascer do sol. Tem nas mãos uma cana velha com o cabo gasto e um peixinho de madeira atado na ponta.

- **Pip** *(normal)*: "Acordei cedo. Não digas a ninguém. Estragas-me a fama."
- **Pip** *(normal)*: "Esta cana era da minha avó Nita. Depois foi minha. Pesquei com ela em todos os sítios onde a torre me deixou ir."
- **Pip** *(feliz)*: "Ela gosta de quem sobe. Eu gosto de quem fica. Por isso… fica com ela. Assim estamos os dois bem servidos."
- **Pip** *(normal)*: "Eu fico com a de bambu. É mais leve. Para adormecer."

▶ **"Vou cuidar bem dela."**
▶ **"Pescamos juntos com ela?"**

- *(cuidar)* **Pip** *(feliz)*: "Eu sei. Não tenhas pressa com ela. Ela também não tem."
- *(juntos)* **Pip** *(feliz)*: "Todos os domingos à tarde. Eu trago a sesta, tu trazes a cana."
- 🎬 Os primeiros raios de sol chegam ao rio. O Pip boceja, deita-se no cais e adormece.
- **Pip** *(a dormir)*: "…era deste tamanho… a amizade… zzz…"

⚙ Recebe a **Cana do Pip** (o minijogo fica mais fácil e os lendários aparecem mais). O Pip passa a ter a fala `pip_dia_66`.

---

## 9. Missões

### R1_03 — Aprende a Pescar (0 ❤️, andar 3, 1.ª conversa)

- **Pedir** — **Pip** *(feliz)*: "Toma, usa esta. É de bambu. É velha. É tua, se pescares três peixes aqui no ribeiro."
  ▶ **"Ensina-me!"** ⚙ missão iniciada · ▶ **"Agora não."** → "Está bem. Eu espero. Sou ótimo a esperar."
- **A lição** (tutorial da pesca, ver `docs/ATIVIDADES.md`, secção 4.1):
  - **Pip**: "Primeiro lanças. Seguras o botão: quanto mais seguras, mais longe vai. Longe há peixes maiores. E mais teimosos."
  - **Pip**: "Depois esperas. Esta é a parte boa. Quando a boia afundar, puxa logo. Logo. É a única vez que eu digo 'logo'."
  - **Pip**: "Depois aparece uma barra. Seguras para a zona verde subir, largas para descer. Mantém o peixe lá dentro. Como quem embala um bebé."
- **Durante** — **Pip**: "Já vais em {n}? Faltam {3-n}. Calma. O ribeiro tem peixes para toda a gente."
- **Falhar um peixe** — **Pip**: "Fugiu? Os peixes também têm de ir para casa. Lança outra vez."
- **Entregar** — **Pip** *(feliz)*: "Três! Já és {pescador/pescadora}. Pequen{o/a}, mas és." ⚙ **Cana de Bambu** · receita **Truta Grelhada** · +100 amizade

### R1_10 — O Rei do Lago (6 ❤️, depois da cena de 6 ❤️)

- **Onde e quando**: andar 9, **com nevoeiro, entre as 5:00 e as 7:00** (lendário: muito rápido; o Isco Bom ajuda).
  Nos dias de nevoeiro o Pip espera no **Cais Velho** das 4:00 às 8:00.
- **Durante** (no Cais Velho) — **Pip**: "Shh. Ele está lá. Sinto-o nos bigodes. Eu não tenho bigodes. Sinto na mesma."
- **Se ele fugir** — **Pip** *(normal)*: "Fugiu? Ele faz isso. Ri-se e foge. Amanhã há mais nevoeiro. Ou depois. Ou para a semana."
- **Se já o tinhas pescado antes** — **Pip** *(surpresa)*: "Já o pescaste?! E não me disseste? …Mostra. MOSTRA." (tens de o ter na mochila ou no Aquário)
- **Entregar** — 🎬 o Pip pega no peixe com as duas mãos.
  - **Pip** *(surpresa → feliz, a chorar)*: "É ele. Os bigodes. Os olhos de lua. É mesmo ele."
  - **Pip** *(feliz)*: "Então era verdade. Uma das minhas histórias era verdade."
  - **Pip** *(normal)*: "Não tens de o devolver ao lago. É teu. Mas eu devolvia."
  - ▶ **"Devolver ao lago."** → "Obrigado. Ele volta para o ano. E eu também." ⚙ +30 (o peixe fica na coleção)
  - ▶ **"Fico com ele."** → "Está bem. Faz-lhe uma casa bonita. Com nevoeiro."
  - ⚙ Título *Rei do Lago* · **Isco Dourado ×5** · +150 amizade

### N_PIP_3 — Todos os Peixes (depois da cena de 4 ❤️)

- **Pedir** — **Pip** *(normal)*: "O meu caderno tem trinta peixes que eu juro que existem. Pesca-os todos. Trinta espécies. Não há pressa. Mesmo nenhuma."
  ▶ **"Aceito."** ⚙ missão iniciada · ▶ **"Trinta?!"** → "Trinta. Um por dia, é um mês. Um por semana, é um ano. Eu espero."
- **Regra**: contam todos os peixes da coleção, também os que pescaste antes da missão.
- **Durante** — **Pip**: "{n} espécies! Faltam {30-n}. O caderno está a ficar contente."
- **Entregar** — **Pip** *(feliz)*: "Trinta! Agora conta-me como foi cada um. Do princípio."
  🎬 À terceira história o Pip adormece. **Pip** *(a dormir)*: "…Mestre… Pescador…"
  ⚙ Título *Mestre Pescador* · +150 amizade

---

## 10. Estados e especiais (1 vez por dia)

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `pip_estado_vida` | `vida_pct < 30` | triste | "Estás a sangrar para o rio. Os peixes ficam nervosos. Vai à Irmã Célia. Devagar. Mas vai." |
| `pip_estado_maldito` | `estado(amaldicoado)` | normal | "Tens uma nuvem roxa. Os peixes não mordem a quem tem nuvens. Vai à Igreja." |
| `pip_estado_cansado` | `estado(cansado)` | feliz | "Cansad{o/a}? Disso percebo eu. Deita-te aqui no cais. Eu vigio. Bem, eu também durmo. Mas perto." |
| `pip_estado_molhado` | `estado(encharcado)` | feliz | "Molhad{o/a}! Caíste ao rio? Bem-vind{o/a} ao clube. O clube sou eu." |
| `pip_estado_sapo` | `estado(sapo)` | surpresa | "Um sapo! A Rã-Rã ia gostar de ti. Pesca com a língua, experimenta. …Não experimentes." |
| `pip_arma_nova` | arma Épica ou melhor equipada pela 1.ª vez | normal | "Arma nova? Brilha. Os peixes gostam de coisas que brilham. Não a uses como isco. Eu já tentei com uma colher." |
| `pip_lendario` | 1.ª conversa depois de pescares um lendário | surpresa | "Um lendário! Era deste tamanho? …Era. Desta vez sou eu que fico de boca aberta." |
| `pip_animal` | `animal != nenhum` (1.ª vez) | feliz | "Esse bicho come peixe? Se come, somos amigos. Se não come, somos amigos na mesma." |
| `pip_animal_polvo` | `animal == polvo_bebe` | surpresa | "Um polvo! Oito braços. Podia pescar com oito canas. Ensina-me a ter oito braços." |
| `pip_comp_kai` | `companheiro(kai)` | feliz | "Kai! Queres pescar? …Não? Nunca queres. Guardo-te o lugar na mesma." |
| `pip_comp_mia` | `companheiro(mia)` | feliz | "Mia! Já tens um arco a sério. O pau agora pode ser meia cana. Falta a outra meia." |
| `pip_comp_gorvan` | `companheiro(gorvan)` | triste | "Mestre Gorvan. Quando eu era pequeno, sentava-se aqui ao rio sem dizer nada. Eu emprestava-lhe a minha cana. Lembra-se?" |
| `pip_classe` | 1.ª conversa depois de escolher classe | normal | "{classe}? Bonito. Há alguma classe de pescador? Não? Devia haver." |
| `pip_nivel_10` | `nivel >= 10` (1.ª vez) | normal | "Nível 10! O meu nível de pesca é… não sei. Nunca contei. Contar cansa." |

### A dormir

Na sesta (12:00–13:00) e antes de o conheceres: `[Sistema] O Pip está a dormir.` e uma destas falas. Não dá amizade nem abre a loja.

| ID | Condição | Fala |
|---|---|---|
| `pip_sono_1` | — | "Zzz… era deste tamanho… não… maior…" |
| `pip_sono_2` | `coracoes(pip) < 8` | "Zzz… baleia… tronco… baleia…" |
| `pip_sono_3` | — | "…calma, peixinho… calma… zzz…" |
| `pip_sono_4` | `missao(R1_10) == concluida` | "…avó… pesquei o rei… quer dizer… pescaram… zzz…" |

### Na torre

| ID | Onde | Emoção | Fala |
|---|---|---|---|
| `pip_torre_3` | andar 3 (quarta) | feliz | "Quarta-feira é dia de ribeiro. A água aqui canta. Ou é a minha barriga." |
| `pip_torre_9` | andar 9 (sábado) | normal | "O nevoeiro hoje está bom. Pode ser que ele apareça. Pode ser que eu adormeça. Uma das duas." |
| `pip_torre_26` | andar 26 (Vila Coaxa) | normal | "A Rã-Rã já pescou doze. Eu pesquei uma ideia. Ela diz que não conta." |
| `pip_torre_26b` | andar 26, à noite | triste | "O Velho Bigodes está lá em baixo. Hoje não chove. Hoje não é dia. Hoje é dia de sesta." |

### Serviço — loja e banca de peixe

**Loja** (no rio, na banca e na torre): Isco · Isco Bom (depois de R1_03) · Isco Dourado (depois de R1_10) · Isco de Areia
(`andar_maximo >= 31`) · Isco Ignífugo (`andar_maximo >= 62`) · Cana de Bambu · Cana de Prata (`andar_maximo >= 31`) ·
Cana de Coral (`andar_maximo >= 51`). Preços em `dados/`. **Banca** (Mercado, 13:00–18:00): compra-te peixe.

| ID | Quando | Emoção | Fala |
|---|---|---|---|
| `pip_loja_abrir` | abrir a loja | feliz | "Canas e iscos. Escolhe com calma. Eu espero. Sou ótimo a esperar." |
| `pip_loja_comprar` | comprar | feliz | "Boa escolha. Os peixes vão gostar. Ou não. Depende do peixe." |
| `pip_loja_sem_dinheiro` | sem ouro | normal | "Não chega? Não faz mal. O isco espera por ti. Eu também." |
| `pip_loja_vender` | vender peixe na banca | normal | "Peixe fresco? Compro. Pago justo. Devagar, mas justo." |
| `pip_loja_vender_lendario` | vender um lendário | triste | "Vais vender um LENDÁRIO? …Está bem. É teu. Mas eu vou chorar para dentro." |
| `pip_loja_vender_lixo` | vender Bota Velha ou Lata | zangado | "Lixo não compro. Leva ao Gizmo, ele faz coisas com botas. E não o deites ao rio." |
| `pip_loja_ensinar` | **Ensinar a pescar** (repete a lição) | feliz | "Outra vez? Segura, larga, segura. É como respirar. Mas com peixe." |
| `pip_loja_fechado` | a dormir ou fora de horas | — | `[Sistema] A loja do Pip está fechada.` *(o Pip ressona)* |
