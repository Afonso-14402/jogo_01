# Gizmo — diálogos

Perfil completo: `docs/NPCS.md`, secção 3.18. Dados: `dados/dialogos/gizmo.json`. Oficina: `docs/LOJAS.md`, secção 2.10.

---

## 1. Ficha de voz

| | |
|---|---|
| Voz (bips) | agudíssimos e muito rápidos, com estalidos metálicos; às vezes um "ding!" quando tem uma ideia |
| Como fala | a mil à hora, começa três frases e acaba uma; usa palavras inventadas de engenharia; grita as palavras importantes |
| Repete | "ENGENHARIA!", "Não é magia!", "Isso vai explodir? Provavelmente.", "Ding!" |
| Tiques | o braço mecânico das costas mexe-se sozinho e mexe nas coisas (animação `braco_extra`); limpa os óculos de soldar com a língua (nojo) |
| Nunca diz | "magia" sem acrescentar "é ciência que ainda não percebemos" |
| Chama ao herói | "Dez Mil", "assistente" (a partir dos 2 corações), "colega" (a partir dos 6) |
| Quem é | gnomo de 60 anos, inventor de **Engrenópolis**, um mundo de máquinas que a torre engoliu (uma parte está no andar 66). Primo do **Senhor Vapor** (Termas, andar 66). Chegou a Ascendia há 40 anos, a fugir de uma explosão "que não foi culpa dele" |
| Rotina | Oficina sempre (dorme em cima da bancada, 2:00–6:00, a ressonar como um motor) · Praça ao meio-dia quando testa invenções (às quartas, 50% de explodir) |

---

## 2. Primeira conversa

- 🎬 Uma explosão pequena. Sai fumo pela porta da oficina. O Gizmo sai a tossir, com o cabelo em pé.
- **Gizmo** *(feliz)*: "FUNCIONOU! Bem, explodiu. Mas explodiu como devia explodir! Isso é funcionar!"
- **Gizmo** *(surpresa)*: "Um cliente! Um JOGADOR! Tu vens de um mundo com máquinas, não vens? Diz-me que vens de um mundo com máquinas."
- **Gizmo** *(normal)*: "Sou o Gizmo. Faço engenhocas. Ganchos, lanternas, coisas que voam, coisas que não deviam voar. Tudo ENGENHARIA. Nada de magia."

⚙ Abre o menu: **Conversar · Perguntar sobre… · Missões · Oficina · Dar presente**.

---

## 3. Falas do dia a dia

### 3.1 Gerais e de hora

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gizmo_dia_01` | `hora entre 6 e 9` | normal | "Acordei com uma ideia. Esqueci-a ao lavar a cara. Por isso não lavo a cara." |
| `gizmo_dia_02` | `hora entre 12 e 13 && dia_semana == quarta` | feliz | *(na Praça)* "Teste público! Afastem-se! Mais! Mais! …Pronto, agora estão longe demais para ver." |
| `gizmo_dia_03` | `hora entre 0 e 2` | feliz | "Meia-noite! A melhor hora para inventar. O cérebro está cansado e deixa passar as ideias más. As melhores!" |
| `gizmo_dia_04` | — | feliz | "Não é magia, é ENGENHARIA com BRILHOS!" |
| `gizmo_dia_05` | — | normal | "Isso vai explodir? Provavelmente. Mas vai explodir BEM." |
| `gizmo_dia_06` | — | feliz | "Inventei uma torradeira que anda. Chama-se Torrada. Não faz torradas. Anda." |
| `gizmo_dia_07` | — | normal | "O Governador proibiu-me de fazer um para-raios gigante na Praça. Fiz um pequeno. No telhado dele. Não perguntou." |
| `gizmo_dia_08` | — | normal | "O Brom diz que as minhas engrenagens são 'brinquedos'. Os brinquedos dele pesam cinquenta quilos. Quem é que brinca?" |
| `gizmo_dia_09` | — | feliz | "Ding! Uma colher que mexe sozinha! …Já existe? Chama-se 'braço'? Ah." |
| `gizmo_dia_10` | `dia_semana == domingo` | normal | "Domingo é dia de arrumar a oficina. Começo às seis. Às sete já estou a inventar outra vez. Arrumar é aborrecido." |

### 3.2 Estação e tempo

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gizmo_dia_20` | `estacao == verao` | normal | "No verão as engrenagens dilatam. Tudo encrava. Eu também." |
| `gizmo_dia_21` | `estacao == inverno` | feliz | "Inverno! O vapor sobe melhor. As máquinas ficam contentes. Eu fico com o nariz vermelho." |
| `gizmo_dia_22` | `clima == trovoada` | feliz | "TROVOADA! Energia de graça a cair do céu! Onde está o meu frasco? O GRANDE?" |
| `gizmo_dia_23` | `clima == chuva` | zangado | "Chuva! Ferrugem! A inimiga natural de todos os inventores! Fecha a porta!" |
| `gizmo_dia_24` | `clima == neve` | normal | "Neve. Estou a fazer um aparelho que derrete neve. Derreteu a mesa. A neve ficou." |

### 3.3 Progresso

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gizmo_dia_40` | `andar_maximo >= 11 && missao(R2_02) != concluida` | feliz | "Minas! Precipícios! Buracos! Precisas de um GANCHO! Eu faço-te um gancho. Traz-me peças." |
| `gizmo_dia_41` | `missao(R2_02) == concluida` | feliz | "Já usaste o gancho? Funciona? Funciona! Às vezes desconfio das minhas coisas quando funcionam." |
| `gizmo_dia_42` | `andar_maximo >= 51` | normal | "Andares debaixo de água! Precisas de respirar! Tenho uma ideia: um capacete com ar dentro. Ding!" |
| `gizmo_dia_43` | `andar_maximo >= 66` | triste | "Foste ao 66? Viste as termas? Viste o meu primo? Está velho? Está mais velho do que eu? Diz que sim." |
| `gizmo_dia_44` | `andar_maximo >= 66` | normal | "Lá em cima há um bocado do meu mundo. Engrenópolis. As fábricas, os canos, as chaminés. Engolidas. Ainda a trabalhar, dizem." |
| `gizmo_dia_45` | `andar_maximo >= 91` | normal | "As 'falhas do Sistema' lá em cima… quadrados coloridos, coisas que se copiam… Isso não é magia. É um PROGRAMA. Avariado. Interessante!" |

### 3.4 Corações

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gizmo_dia_60` | `coracoes(gizmo) >= 2` | feliz | "Assistente! Segura isto. Não, não por aí. Por aí explode. Por AQUI." |
| `gizmo_dia_61` | `coracoes(gizmo) >= 4` | feliz | "A Torrada gosta de ti. Anda atrás de ti quando entras. Não a deixes sair. Ela não sabe atravessar a rua." |
| `gizmo_dia_62` | `coracoes(gizmo) >= 6` | normal | "Colega. És a primeira pessoa em quarenta anos que não fugiu quando uma coisa minha começou a apitar." |
| `gizmo_dia_63` | `coracoes(gizmo) >= 8` | triste | "Às vezes faço coisas que funcionam e não sei porquê. Isso assusta-me mais do que as explosões." |
| `gizmo_dia_64` | `coracoes(gizmo) >= 10` | feliz | "Saltas duas vezes no ar! Com as MINHAS botas! A gravidade está furiosa comigo. Ótimo." |

### 3.5 Origem e Skill Única

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gizmo_dia_70` | `origem == jogador` | feliz | "Jogavas JOGOS em ECRÃS? Com BOTÕES? Explica-me tudo! Como é que o ecrã sabe que carregaste? Desenha! DESENHA!" |
| `gizmo_dia_71` | `origem == atrasado` | normal | "No teu mundo havia 'autocarros'? Carroças que andam sozinhas com MOTOR? Ding! Vou fazer um. Pequeno. Para a Torrada." |
| `gizmo_dia_72` | `skill_unica == mestre_artesao` | feliz | "Mestre Artesão! Tens mãos de inventor! Larga a espada, vem trabalhar comigo! …Não? Está bem. Pelo menos às quartas." |
| `gizmo_dia_73` | `skill_unica == bolsa_infinita` | surpresa | "Uma mochila com mais espaço dentro do que fora?! Isso viola… tudo! Empresta-ma uma semana. Só uma. Prometo devolver. Talvez em pedaços." |

### 3.6 Falas curtas

| ID | Emoção | Fala |
|---|---|---|
| `gizmo_curta_1` | feliz | "Ding! Não, nada. Foi um ding pequeno." |
| `gizmo_curta_2` | normal | "Estou ocupado. Estou sempre ocupado. Fala na mesma." |
| `gizmo_curta_3` | normal | "Cuidado onde pisas. Não, aí. Isso era um protótipo." |

---

## 4. Perguntar sobre…

### 4.1 A torre
- **Gizmo** *(feliz)*: "A torre é uma MÁQUINA. Ninguém acredita em mim. Tem engrenagens: os andares rodam, as escadas abrem, os monstros voltam a aparecer todos os dias. Isso é uma FÁBRICA!"
- **Gizmo** *(normal)*: "E a janela azul é o painel de controlo. Alguém está a carregar nos botões. Ou alguém carregou há muito tempo e esqueceu-se de desligar."
- *(com rank A)* **Gizmo** *(triste)*: "E se a máquina estiver cansada? As máquinas também se cansam. Gastam-se. Rangem. Pedem óleo."

### 4.2 O andar atual
| Região | Fala |
|---|---|
| 1 Floresta | "Árvores! Natureza! Aborrecido. Traz-me madeira fulminada por raios. Isso tem energia." |
| 2 Cavernas | "Minas com vagonetas! CARRIS! Alguém lá em baixo percebia de engenharia. Os anões. Respeito os anões. Não lhes digo." |
| 3 Pântano | "Gel elétrico das enguias do pântano! Uma pilha natural! Traz-me tudo o que encontrares." |
| 4 Deserto | "Vidro solar! Concentra a luz do sol! Com isto faço um raio de calor. Não para fazer mal. Para torradas." |
| 5 Gelo | "Gelo eterno: nunca derrete. Um frigorífico perfeito. Imagina: comida fresca para sempre. A Dona Marta ia chorar." |
| 6 Oceano | "Pressão! Profundidade! Precisas de um escafandro. Eu faço. Já fiz um. Para a Torrada. Não resultou. Ela não respira." |
| 7 Vulcão | "Engrenópolis. A minha cidade. Está lá em cima, engolida. Há um golem lá, o Nº 7. Fui eu que o desenhei. Há quarenta anos. Não quero falar disso. Quero falar disso." |
| 8 Reino Assombrado | "Fantasmas! Energia sem corpo! Se conseguisse ligar um fantasma a uma lâmpada… Não. Não é ético. Talvez um fantasma voluntário." |
| 9 Céu | "Os Alados têm balões! E pontes de LUZ! Sólida! Isto é a melhor engenharia da torre! Desenha-me tudo!" |
| 10 Abismo | "Falhas, erros, quadrados coloridos… É o código da torre a aparecer. Se tiveres uma chave de fendas grande, aperta alguma coisa." |

### 4.3 Rumores
| ID | Condição | Rumor |
|---|---|---|
| `gizmo_rumor_01` | — | "A Madeira Fulminada só aparece quando um raio cai numa árvore da floresta. Nas trovoadas. Se a vires a fumegar, apanha-a. Com luvas." |
| `gizmo_rumor_02` | `andar_maximo >= 11` | "Os goblins das minas fazem engenhocas com lixo. Pouco seguras. Muito inventivas. Traz-me uma." |
| `gizmo_rumor_03` | `andar_maximo >= 21` | "As enguias elétricas do pântano dão Gel Elétrico. É o meu presente preferido. Só para saberes. Sem pressão." |
| `gizmo_rumor_04` | `andar_maximo >= 51` | "Há uma Lanterna Abissal no fundo do mar. Luz que não precisa de fogo. Com ela, faço-te uma coisa que respira debaixo de água." |
| `gizmo_rumor_05` | `andar_maximo >= 61` | "O Golem Forjado Nº 7 anda pelo vulcão. Tem um núcleo de obsidiana. Preciso dele. Por razões… pessoais." |
| `gizmo_rumor_06` | `andar_maximo >= 94` | "Dizem que há uma Engrenagem do Tempo no andar 95. Uma engrenagem que gira para trás. Para TRÁS! Vendia a oficina por ela." |

### 4.4 A vida dele
| Corações | Fala |
|---|---|
| 0 | "A minha vida é inventar. O resto é intervalo entre invenções." |
| 2 | "Venho de Engrenópolis. Uma cidade de máquinas, fumo e gnomos. Tudo tinha engrenagens. Até as camas. Sobretudo as camas." |
| 4 | "A torre engoliu Engrenópolis há quarenta anos. Eu estava a testar um foguete. Fui atirado para fora. Caí aqui, em Ascendia. Com o foguete." |
| 6 | "O meu primo Vapor ficou lá em cima, no que sobrou. Abriu umas termas. Escrevemo-nos. Ele diz que eu explodi a cidade. Não explodi. Quase não." |
| 8 | "Às vezes as minhas máquinas funcionam sem razão. Uma lâmpada sem fio. Uma mola que salta mais alto do que devia. Os outros chamam a isso magia. Eu chamo… não sei. É isso que me assusta." |
| 10 | "Já não tenho tanto medo da magia. Se é ciência que ainda não percebemos, então tenho muito para perceber. Isso é bom. É o melhor." |

---

## 5. Presentes

**Adora:** Engrenagem do Tempo, Núcleo de Magma, Gel Elétrico · **Gosta:** engrenagens, peças (Engrenagem, Mola, Lata, Bota Velha "para peças") ·
**Detesta:** magia — dar-lhe **Pó de Fada** dá −40 ("detesta"), e Pó de Fada Dourado ainda pior (−60).

| Reação | Falas |
|---|---|
| Adora | "GEL ELÉTRICO! Isto é energia em frasco! Vou fazer… vou fazer… DING! Vou fazer tudo!" · "Um núcleo de magma! Ainda está quente! Vou pô-lo num forno. Vou pô-lo num forno que anda!" |
| Gosta | "Uma engrenagem! Dente perfeito! Encaixa em… espera… encaixa na Torrada! A Torrada vai ter um joelho novo." |
| Neutro | "Obrigado! Vou desmontar isto e ver o que tem por dentro." |
| Não gosta | "Isto não tem peças. Nem fios. Nem nada. É… inteiro. Que desperdício." |
| Detesta | "PÓ DE FADA?! Isso é MAGIA! Tira isso da minha oficina! Faz espirrar as máquinas!" |

| Item | Fala |
|---|---|
| Lixo de pesca (Bota Velha, Lata) | "Uma bota! Uma bota velha! Toda a gente deita fora. Eu vejo uma sola, um atacador, três ilhós e um futuro." (conta como "gosta") |
| Placa Nº 7 (região 7) | 🎬 o Gizmo fica calado, a olhar. "…É minha. Esta placa. Fui eu que a gravei." (conta como "adora") |

---

## 6. Aniversário e festivais

**Aniversário (Primavera, dia 23):**
- Sem presente: "Faço anos? Faço! Inventei um bolo que se acende sozinho. Pegou fogo à cozinha. Foi o melhor aniversário."
- Com presente que adora: "Um presente! Com peças dentro! Ding ding ding! Três dings! Nunca dei três dings!"

| Festival | Fala |
|---|---|
| F_01 Festa das Flores | "Inventei uma flor mecânica para o concurso. Abre-se ao sol. E fecha-se com força. Cuidado com os dedos." |
| F_01 (dança, 4+ ❤️) | ▶ **"Danças comigo?"** → "Dançar é engenharia de movimento! Contei os passos: oito por compasso. Vamos! Não me pises o braço extra." ⚙ +100 |
| F_02 Festival da Pesca | "Fiz uma cana que lança sozinha! Lançou o Pip ao rio. Desclassificaram-me. Valeu a pena." |
| F_03 Noite dos Espíritos | "Fiz uma abóbora com uma lâmpada lá dentro em vez de uma vela! Mais segura. Explodiu. Menos segura." |
| F_04 Festival da Estrela | "O fogo de artifício sou eu que faço! Este ano tem formas: uma torre, um javali e um herói. O herói pode sair com três braços." |
| F_05 Dia da Subida | "Fiz uma máquina que atira confettis! Atirou confettis, um balde e o Governador. Ele não se magoou. Muito." |
| F_06 Concurso da Casa | "A minha casa ganha sempre o prémio 'Mais Original'. É o prémio que inventaram para mim. Para eu parar de explodir as casas dos outros." |
| F_07 Noite das Lanternas | "Fiz lanternas que flutuam no ar em vez de no rio. A Lyra disse que era bonito mas que não era a tradição. Pus uma no rio. Pela minha cidade." |

---

## 7. Depois dos bosses

| Boss | Fala |
|---|---|
| Javali-Rei (5) | "Um javali que corre em linha reta e bate em árvores? É um aríete mal calibrado. Bem feito." |
| Ent Ancião (10) | "Uma árvore que fala… Sem cordas vocais. Sem pulmões. Ciência que ainda não percebemos. Vou perceber. Um dia." |
| Aranha-Mãe (15) | "Seda de aranha! Mais forte do que aço! Traz-me! Vou fazer um cabo! Um cabo para quê? Ainda não sei! Mas forte!" |
| Golem de Cristal (20) | "Um golem a cristal! Um motor de luz no peito! Trouxeste o núcleo? Trouxeste?! Posso ver? Só ver. Com as mãos." |
| Serpente do Lodo (25) | "Lodo. Sem peças. Passa à frente." |
| Hidra do Pântano (30) | "Cabeças que voltam a crescer: regeneração! Se eu pusesse isso numa máquina… máquinas que se arranjam sozinhas! Ding!" |
| Escorpião Imperador (35) | "A carapaça! Articulações perfeitas! A natureza é a melhor engenheira. Mas não lhe digas." |
| Faraó Eterno (40) | "Um rei a funcionar há mil anos sem manutenção! Que máquina! Que múmia!" |
| Yeti Ancião (45) | "Pelo de yeti: isolamento térmico perfeito. Vou forrar a Torrada. Ela tem frio. Acho." |
| Dragão de Gelo (50) | "Metade da torre! Fiz um contador mecânico para os andares! Está a 50! Daqui a nada encrava! Já encravou." |
| Capitão Esqueleto (55) | "Canhões no navio! Pólvora velha! Traz-me um canhão. Pequeno. Médio. O que couber na mochila." |
| Leviatã (60) | "Venceste o mar. Agora o fogo. O meu fogo. A minha cidade. Cuidado lá em cima, colega." |
| Ferreiro Infernal (65) | "O Ferreiro tinha uma forja que fazia armas para quem ainda não tinha chegado. Uma FÁBRICA de futuros. Isto não me sai da cabeça." |
| Kai — salvo (68) | "O Kai voltou! O telemóvel dele! Posso ver o telemóvel dele? Outra vez? Só mais uma vez?" |
| Kai — vencido (68) | "Fiz uma coisa para o Kai. Um carregador. Para o telemóvel dele. Guardo-o na gaveta. Para quando ele voltar." |
| Titã de Magma (70) | "O titã era o coração do vulcão. Engrenópolis bebia o calor dele. Agora dorme. A minha cidade vai arrefecer. Talvez seja melhor assim." |
| Lich Bibliotecário (75) | "Um morto-vivo a guardar livros. Eu queria guardar engrenagens assim. Para sempre." |
| Rei Sem Coroa (80) | "O rei tentou parar a torre. 'Ninguém pode.' Ninguém com espadas. Com uma chave de fendas? Ninguém experimentou." |
| Grifo Real (85) | "Penas de grifo: aerodinâmica perfeita. Vou fazer asas! Para a Torrada! Ela vai VOAR!" |
| Serafim Caído (90) | "Um anjo-máquina que serviu o Administrador. Engrenagens de luz. Diz-me como era por dentro. Não? Está bem. Diz-me como estavas tu." |
| Guardião do Tempo (95) | "Um guardião do TEMPO! Uma máquina que mexe no tempo! Trouxeste a Engrenagem? Trouxeste?! Ding! DING!" |

---

## 8. Cenas de coração

### ❤️ 2 — A invenção que voou

| | |
|---|---|
| ID | `cena_gizmo_2` |
| Quando | 2 ❤️ · passar à porta da Oficina entre as 12:00 e as 15:00 |
| Onde | rua do Bairro dos Artesãos |
| Quem | herói, Gizmo, uma engenhoca voadora |
| Música | `ascendia_dia` (rápida) |

🎬 Uma janela da oficina rebenta. Uma engenhoca com hélice sai a voar, aos zigue-zagues, a apitar.
- **Gizmo** *(da janela)*: "APANHA-A! APANHA-A! É o Pombo Nº 3! Tem o meu almoço!"
- 🎬 **Minijogo curto**: perseguir o Pombo Nº 3 pelos telhados baixos e apanhá-lo (com o Gancho, se o tiveres, é mais fácil).
- **Gizmo** *(feliz)*: "Apanhaste-o! E o almoço está inteiro! Bem, o pão. O queijo voou para o rio."

▶ **"Porque é que tem o teu almoço?"**
▶ **"Posso ficar com ele?"**

- *(almoço)* **Gizmo** *(normal)*: "Era um teste: um pombo que leva comida aos mineiros do andar 11. Ainda não sabe o caminho. Sabe o caminho do rio." ⚙ +30
- *(ficar)* **Gizmo** *(feliz)*: "Queres? É teu! Precisa de corda todos os dias. E foge às vezes. Como os gatos!" ⚙ +30 · **Pombo Nº 3** (decoração viva para a casa)

⚙ 5% de desconto na Oficina.

### ❤️ 4 — O robô

| | |
|---|---|
| ID | `cena_gizmo_4` |
| Quando | 4 ❤️ · entrar na Oficina à noite (20:00–2:00) |
| Onde | Oficina |
| Quem | herói, Gizmo, Torrada |
| Música | `taberna` (caixa de música) |

🎬 Uma torradeira de lata com duas pernas de mola anda pela oficina a bater nas coisas. Faz "tic, tic, tic".
- **Gizmo** *(feliz)*: "Apresento-te… a TORRADA! O meu robô! O primeiro robô de Ascendia!"
- **Gizmo** *(normal)*: "Não faz nada. Anda. Às vezes para. Às vezes vem ter comigo quando estou triste. Isso não programei."
- 🎬 A Torrada vai ter com o herói e encosta-se à perna dele.
- **Gizmo** *(surpresa)*: "Ela… gosta de ti. Isso também não programei."

▶ **"Talvez tenha vontade própria."**
▶ **"É só uma máquina."**

- *(vontade)* **Gizmo** *(nervoso)*: "Vontade própria? Uma máquina? Isso seria… magia. Não. Não pode ser. Pode?" ⚙ +30
- *(máquina)* **Gizmo** *(feliz)*: "Exato! Só uma máquina! …Uma máquina simpática." ⚙ +10

⚙ Receita de joalharia **Anel de Engrenagem** (+5% velocidade de ataque) e a **Torrada** passa a visitar a tua casa às quartas.

### ❤️ 6 — O Número 7

| | |
|---|---|
| ID | `cena_gizmo_6` |
| Quando | 6 ❤️ · `andar_maximo >= 61` · Oficina |
| Onde | Oficina, parede do fundo com desenhos antigos |
| Quem | herói, Gizmo |
| Música | `bastiao_brasa` (versão lenta) |

🎬 O Gizmo tira um desenho amarelado da parede: um golem de ferro enorme, com um "7" no peito.
- **Gizmo** *(triste)*: "Golem Forjado Nº 7. Fui eu que o desenhei. Em Engrenópolis. Era para trabalhar nas fábricas. Para os gnomos descansarem."
- **Gizmo** *(triste)*: "Quando a torre engoliu a cidade, ele ficou lá. Sem ninguém para lhe dar ordens. Agora anda pelo vulcão a destruir tudo. A trabalhar sem saber para quem."
- **Gizmo** *(normal)*: "Traz-me o núcleo dele. Não quero que o destruas por ódio. Quero que ele descanse. E… quero ver se ainda tem a minha assinatura lá dentro."

⚙ Missão **R7_14 O Número 7** (secção 9). O Gizmo aceita jantar em tua casa (leva a Torrada).

### ❤️ 8 — A magia sem querer

| | |
|---|---|
| ID | `cena_gizmo_8` |
| Quando | 8 ❤️ · trovoada, Oficina, à noite |
| Onde | Oficina |
| Quem | herói, Gizmo |
| Música | `revelacao` (suave) |

🎬 A Oficina está às escuras. Só uma lâmpada pequena brilha, em cima da mesa, **sem estar ligada a nada**.
- **Gizmo** *(triste)*: "Vês aquilo? Não tem fio. Não tem pilha. Não tem nada. Brilha há três dias."
- **Gizmo** *(triste)*: "Às vezes acontece. As minhas coisas funcionam sem razão. Em Engrenópolis chamavam-me 'o gnomo com sorte'. Eu sabia que não era sorte."
- **Gizmo** *(nervoso)*: "Acho que… acho que eu faço magia. Sem querer. Quando quero muito que uma coisa funcione. E eu não ACREDITO em magia, colega!"

▶ **"Talvez a magia seja ciência que ainda não percebes."**
▶ **"Não importa como. Funciona."**

- *(ciência)* **Gizmo** *(surpresa, depois a rir)*: "Usaste a minha frase contra mim! …É justo. É muito justo. Então vou estudar-me a mim próprio. Sou o meu melhor projeto." ⚙ +30
- *(funciona)* **Gizmo** *(feliz)*: "Funciona. Pois. Sessenta anos a inventar e o mais importante é isso. Funciona." ⚙ +30

⚙ 15% de desconto na Oficina. Passa a mandar **cartas** com peças e desenhos de invenções.
⚙ Com esta cena feita, o Gizmo faz o **carregador de manivela** para o telemóvel do Kai (dá 3% de bateria; ver `docs/dialogos/kai.md`).

### ❤️ 10 — As Botas-Mola

| | |
|---|---|
| ID | `cena_gizmo_10` |
| Quando | 10 ❤️ · `missao(R7_14) == concluida` · Praça, quarta-feira, 12:00 (dia de teste) |
| Onde | Praça da Torre |
| Quem | herói, Gizmo, Torrada, aldeões |
| Música | `tema_gizmo` (marimba e apitos) |

- **Gizmo** *(feliz)*: "Teste público! O melhor de sempre! Cala-te, Torrada! Senhoras e senhores… as BOTAS-MOLA!"
- 🎬 Mostra umas botas com molas de cobre e uma engrenagem azul no calcanhar. A engrenagem brilha sozinha.
- **Gizmo** *(normal)*: "Fi-las para ti. Com uma peça do Nº 7. E com… um bocadinho de mim. Não sei explicar. Não quero explicar."
- 🎬 O herói calça as botas. **Minijogo**: saltar duas vezes no ar para apanhar um balão em cima da fonte.
- 🎬 Os aldeões aplaudem. A Torrada salta também (cai).
- **Gizmo** *(feliz)*: "FUNCIONOU! E não explodiu! Isto nunca me aconteceu num teste público! Colega, é o melhor dia da minha vida!"

⚙ **Botas-Mola**: **salto duplo**. Título *Assistente de Inventor*.

---

## 9. Missões

### R2_02 — O Gancho (`andar_maximo >= 11`)
- **Pedir** — **Gizmo**: "Traz-me cinco engrenagens dos goblins e dez lingotes de ferro. Faço-te um gancho que te puxa até ao teto. Ou até à parede. Ou contra a parede. Ainda estou a afinar."
- **Passo**: entregar **5 Engrenagens** (drop dos goblins, região 2) e **10 Lingotes de Ferro**.
- **Entregar** — 🎬 testa o gancho na oficina: o gancho prende-se ao teto e puxa o Gizmo. Ele fica pendurado.
  - **Gizmo** *(pendurado, feliz)*: "FUNCIONA! Agora tira-me daqui. Devagar." ⚙ **Gancho** (`tut_gancho`) · +100

### R6_11 — Escafandro (`andar_maximo >= 54`)
- **Pedir** — **Gizmo**: "Para ires ao fundo do mar sem seres esmagad{o/a}, precisas de um capacete com ar e com força. Traz-me gel elétrico, coral abissal e uma lanterna das profundezas."
- **Passo**: entregar **10 Gel Elétrico + 5 Barra de Coral Abissal + 1 Lanterna Abissal**.
- **Entregar** — **Gizmo** *(feliz)*: "Capacete de Escafandro! Ar infinito! Aguenta a pressão! Testei com a Torrada no rio. Ela não precisava de ar, mas gostou." ⚙ **Capacete de Escafandro** · +150

### R7_14 — O Número 7 (6 ❤️, `andar_maximo >= 61`)
- **Passos**: encontrar o **Golem Forjado Nº 7** no vulcão (região 7), vencê-lo e trazer o **Núcleo de Obsidiana** (e, se apanhares, as **3 Placas Nº 7** — o Brom faz com elas o Peitoral Nº 7).
- **Entregar** — 🎬 o Gizmo abre o núcleo com uma chave pequena. Lá dentro, gravado: *"G. — para que os outros descansem."*
  - **Gizmo** *(triste)*: "A minha assinatura. Ainda lá está. E ele trabalhou quarenta anos sem ninguém para descansar."
  - **Gizmo** *(normal)*: "Vou pôr o núcleo noutra máquina. Uma pequena. Que trabalhe na terra. Que regue plantas. Que descanse quando quiser."
  - ⚙ **Autómato de Quinta** (rega a quinta sozinho todos os dias) · +200

---

## 10. Estados e especiais

| ID | Condição | Emoção | Fala |
|---|---|---|---|
| `gizmo_estado_vida` | `vida_pct < 30` | surpresa | "Estás a perder óleo! Quer dizer, sangue! Vai à Igreja! Eu não sei consertar gente. Só torradeiras." |
| `gizmo_estado_choque` | `estado(choque)` | feliz | "Estás eletrizad{o/a}! Encosta-te a esta lâmpada! …Funciona! És uma pilha!" |
| `gizmo_estado_maldito` | `estado(amaldicoado)` | nervoso | "Isso é magia má. Não chegues perto das máquinas. Ficam com soluços." |
| `gizmo_arma_rara` | arma de raridade Épica ou melhor | feliz | "Essa arma tem um brilho! O brilho é calor? É luz? É… vou estudar. Empresta-ma uma noite." |
| `gizmo_comp_kai` | `companheiro(kai)` | feliz | "O Kai! O telemóvel! A bateria! Senta-te, vou ligar a manivela! Gira! GIRA!" |
| `gizmo_falhas` | `andar_maximo >= 91` (1.ª vez) | normal | "As falhas lá em cima… Se for um programa avariado, então alguém o escreveu. E se alguém o escreveu, alguém o pode reparar." |

### Serviço
| ID | Situação | Emoção | Fala |
|---|---|---|---|
| `gizmo_serv_abrir` | abrir a Oficina | feliz | "Bem-vind{o/a} à Oficina! Não toques em nada que apite. Nem em nada que não apite. Toca no balcão." |
| `gizmo_serv_comprar` | comprar engenhoca | feliz | "Excelente escolha! Garantia de três dias. Ou até explodir. O que vier primeiro." |
| `gizmo_serv_joalharia` | usar a mesa de joalharia | normal | "Pedras brilhantes num anel. Não é engenharia. Mas pagam bem. Usa à vontade." |
| `gizmo_serv_reciclar` | reciclar lixo | feliz | "Três botas velhas, uma engrenagem! A alquimia dos pobres! Não é alquimia. É reciclagem. Ding!" |
| `gizmo_serv_barco` | melhorias do barco | normal | "O Tomé faz a madeira, eu faço os motores. Não há motores. Ainda." |
| `gizmo_serv_sem_ouro` | sem ouro | normal | "Sem ouro? Paga em peças. Aceito peças. Prefiro peças." |
| `gizmo_serv_dormir` | 2:00–6:00 | — | `[Sistema] O Gizmo dorme em cima da bancada. Ressona como um motor. A loja continua aberta (paga no balcão).` |
