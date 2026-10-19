# Povoações da Região 5 — diálogos e missões

Os NPCs que vivem nos andares 41–50 e as **missões da região passo a passo**. Perfis e recompensas:
`docs/regioes/r05_gelo.md` (secções 7 e 8). Cenas da história: `docs/guiao/cap05_gelo.md`.

**Gente do norte**: Torrenses do frio. Falam alto, riem-se alto, abraçam com força e dizem tudo à frente. Não ligam
à janela azul ("aqui o que conta é a lenha"). Bips: graves e quentes. Os monges da aurora falam baixo e devagar.

---

## 1. Pinhal-do-Norte (andar 42)

Primeira chegada: cena **C5-02**. Tem **salão comunal** (dormir), **cristal**, **loja** e **sauna** (depois de R5_02).

### 1.1 Ulf Barba-Gelo — chefe da aldeia

| | |
|---|---|
| Voz | bips muito graves e altos; ri-se como um trovão ("HA!") |
| Quem é | 60 anos, enorme, barba branca sempre com pedacinhos de gelo. Chefe porque "ninguém mais quis". Corta lenha todas as manhãs. Detesta o Kraken do lago ("roubou-me três redes e um primo") |
| Repete | "HA!", "Ninguém fica à porta em Pinhal-do-Norte.", "Isso resolve-se com lenha." |

| ID | Condição | Fala |
|---|---|---|
| `ulf_01` | — | "Bom dia! Já cortaste lenha hoje? Não? Então ainda não é bom dia. HA!" |
| `ulf_02` | — | "Discussão entre vizinhos? Resolve-se com lenha. Cada um corta um monte. Quem acabar primeiro tem razão. Funciona sempre." |
| `ulf_03` | `clima == nevao` | "Nevão! Toda a gente para dentro! Até tu! Até os cães! Os cães já estão dentro. São mais espertos do que tu." |
| `ulf_04` | antes de R5_09 | "O Kraken do lago 43. Roubou-me três redes e um primo. O primo voltou. As redes não. Quero as redes." |
| `ulf_05` | `missao(R5_09) == concluida` | "O Kraken caiu e o gelo do farol ficou inteiro! Toma, o arpão do meu avô. Ele dizia que só se usa para o peixe mais teimoso do mar. Ainda não o encontrei. Talvez tu." |
| `ulf_06` | Festa do Solstício | "SOLSTÍCIO! A noite mais comprida! Mais tempo para comer! HA!" |
| `ulf_curta` | já falaste hoje | "Lenha. Depois falamos." |

### 1.2 Sigrid — dona da sauna

| ID | Condição | Fala |
|---|---|---|
| `sigrid_01` | antes de R5_02 | "A sauna caiu com o peso da neve. A aldeia sem sauna é como… como um pinheiro sem neve. Feio e triste." |
| `sigrid_02` | `missao(R5_02) == concluida` | "Entra, sua, sai, salta para a neve, grita. É a tradição. O grito é obrigatório." |
| `sigrid_03` | depois da sauna | "Agora o frio não te apanha o dia todo. E tens a pele de um bebé. Um bebé muito cansado." |

### 1.3 Erik Trenó — condutor de trenós

| | |
|---|---|
| Quem é | 35 anos, sempre com seis cães à volta (Fumo, Brasa, Neve, Pinha, Bolota e o Senhor Gordo). Perdeu quatro cães num nevão |

| ID | Condição | Fala |
|---|---|---|
| `erik_01` | antes de R5_04 | "Tinha dez cães. Um nevão levou quatro. Estão vivos, sinto-o. Os cães do norte não morrem de frio. Morrem de saudade." |
| `erik_02` | `missao(R5_04) == concluida` | "Os dez! Sobe para o trenó! Segura-te! Os cães não travam! Ninguém lhes ensinou!" |
| `erik_03` | ao usar o trenó | "Para onde? Diz depressa, que eles já estão a correr." |

### 1.4 Velha Astrid — tricota tudo

| ID | Condição | Fala |
|---|---|---|
| `astrid_01` | abrir loja | "Casacos, luvas, gorros, meias. Tudo de lã. Tudo quente. Tudo meu. Bem, agora teu, se pagares." |
| `astrid_02` | — | "Estás magr{o/a}. E com frio. As duas coisas resolvem-se com sopa e lã. Eu tenho as duas." |
| `astrid_03` | `missao(R5_01) == concluida` | "O casaco fica-te bem. Fica bem a toda a gente. É o casaco que é bonito, não és tu. Mas também." |

### 1.5 Leif — rapaz de 9 anos

| ID | Condição | Fala |
|---|---|---|
| `leif_01` | antes de R5_03 | "Queres ver uma coisa? *(atira uma bola de neve)* Isso. Era isso." |
| `leif_02` | antes de R5_03 | "Eu quero um pinguim. A mãe diz que os pinguins vivem no lago. O lago é longe. Tu és crescido. Tu podes ir." |
| `leif_03` | `missao(R5_03) == concluida` | "O meu pinguim chama-se Senhor Fato. Porque tem fato. O teu chama-se como? Não pode ser Senhor Fato. Já está ocupado." |

### 1.6 Bjorn e Sif — a antiga equipa da Freya

| | |
|---|---|
| Quem são | casal na casa dos 40, ex-aventureiros de rank S de Ascendia. Com a Freya chegaram ao andar 62. Depois do que lá aconteceu, casaram e ficaram em Pinhal-do-Norte. Ele faz barcos de pesca; ela ensina as crianças a usar o arco. Escrevem à Freya todos os meses; ela não responde (até ter 10 ❤️) |
| Onde | casa azul ao pé do lago (dia) · salão comunal (noite) |

| ID | Condição | Fala |
|---|---|---|
| `bjorn_01` | — | "És de Ascendia? Conheces a Capitã Freya? …Ela está bem? Come? Dorme? Ainda grita com os recrutas?" |
| `sif_01` | — | "Escrevemos-lhe todos os meses. Há oito anos. Nunca respondeu. Não faz mal. Escrevemos na mesma. Os amigos são para isso." |
| `bjorn_02` | `coracoes(freya) >= 6` | "Diz-lhe… diz-lhe que o barco novo tem o nome dela. Não lhe digas. Ela zanga-se. Diz." |
| `sif_02` | `coracoes(freya) >= 10` | *(com uma carta na mão, a chorar)* "Ela respondeu! Três páginas! A Freya! Três PÁGINAS! Bjorn, senta-te, senão cais!" |
| `sif_03` | `andar_maximo >= 61` | "Já passaste o 60? Cuidado no 62. Não te digo porquê. A Freya é que tem de contar." |

### 1.7 Aldeões de Pinhal-do-Norte (sem nome)

| ID | Quem | Fala |
|---|---|---|
| `pinhal_lenhador_01` | lenhador | "Cada pinheiro que corto, planto dois. Por isso o pinhal nunca acaba. Por isso eu nunca acabo de trabalhar." |
| `pinhal_crianca_01` | criança | "Fizemos um boneco de neve igual ao Ulf! Tem barba de verdade! Arrancámos ao Ulf! Não lhe digas!" |
| `pinhal_velho_01` | velho à lareira | "No meu tempo os invernos eram mais frios. E mais compridos. E as histórias também. Senta-te." |

---

## 2. Aldeia dos Caçadores (andar 46) — reconstrução

Começa **abandonada**: só vive lá a **Caçadora Inga**. Cada parte da R5_05 traz pessoas e serviços.
O **sino** da torre é a cena **C5-04** (diário da equipa de Gorvan).

### 2.1 Caçadora Inga

| | |
|---|---|
| Voz | bips curtos e secos; quase nunca usa frases com mais de dez palavras |
| Quem é | 28 anos, caçadora, cabelo rapado de um lado, cicatriz de garra no braço. A última da aldeia: há 15 anos uma nevasca trouxe o **Wendigo** e os caçadores que saíram para o caçar voltaram **congelados** e mortos-vivos. A mãe dela era a curandeira |
| Repete | "Hm.", "A neve não perdoa. Eu também não." |
| Companheira | depois da R5_05: companheira de caça (arqueira), só nos andares 41–50 |

| ID | Condição | Fala |
|---|---|---|
| `inga_01` | 1.ª vez | "Não há ninguém aqui. Só eu. E eles." *(aponta para a floresta)* "Não são gente. Já foram." |
| `inga_02` | — | "Os caçadores congelados eram os meus vizinhos. O da barba ruiva era o meu tio. Não lhes batas na cara. Por favor." |
| `inga_03` | antes de R5_05 | "Queria a aldeia viva outra vez. Sozinha não consigo. Contigo, talvez." |
| `inga_04` | depois de cada parte da R5_05 | "Mais um. A aldeia respira." |
| `inga_05` | `missao(R5_05) == concluida` | "Cinco casas. Gente outra vez. Barulho outra vez. Não sabia que tinha saudades do barulho." |
| `inga_06` | `missao(R5_15) == concluida` | "Descansaram. O meu tio também. Enterrei-o ao pé da minha mãe. Obrigada. É a primeira vez que digo isto em quinze anos." |

### 2.2 Os que voltam (R5_05)

| NPC | Quando aparece | Fala |
|---|---|---|
| **Ferreiro Gunnar** | Forja do Caçador | "Gelo Eterno não derrete, mas dobra-se. Com paciência e um martelo muito quente. Eu tenho os dois." |
| **Curandeira Helka** | Casa da Curandeira | "Era aprendiz da mãe da Inga. Agora sou a curandeira. Ainda tenho medo de agulhas. Não digas a ninguém." |
| **Comerciante Sven** | Armazém | "Peles, carne seca, flechas, cordas. Tudo o que um caçador precisa. Menos coragem. Essa traz-se de casa." |
| **Sineiro Olaf** | Torre do Sino | "Toco o sino à meia-noite. Os congelados param e ouvem. Às vezes um deles chora. Gelo a escorrer. Toco mais devagar." |

---

## 3. Mosteiro da Aurora (andar 48)

**Noite eterna.** Os monges falam baixo. No mosteiro há **celas** (dormir), **cristal** e **chá quente** de graça.
Primeira noite: cena **C5-06** (o Kai no terraço).

### 3.1 Mestre Kael — abade

| | |
|---|---|
| Voz | bips muito lentos e calmos; nunca muda de tom |
| Quem é | 80 anos, careca, olhos semicerrados, manto cinzento. Estuda a aurora há 60 anos. Acredita que a aurora são as almas dos Jogadores que desistiram ("não se perderam: pararam") |

| ID | Condição | Fala |
|---|---|---|
| `kael_01` | — | "Senta-te. Não faças nada. É mais difícil do que parece." |
| `kael_02` | — | "Vês a aurora? Cada luz é alguém que parou de subir. Não é triste. Pararam. Descansam. A luz é o que fica de quem descansa." |
| `kael_03` | antes de R5_08 | "Há quatro pedras que cantam, cada uma com a sua cor. Toca-lhes na cor certa e aprendes a parar. Quem sabe parar, recupera depressa." |
| `kael_04` | `missao(R5_08) == concluida` | "Agora sabes parar. Não te esqueças: parar não é desistir. Desistir é parar para sempre." |
| `kael_05` | `missao(H_12) == concluida` | "O homem grande de um braço. Passou aqui há vinte anos, a descer. Sozinho. Não parou. Nem para beber chá. Tenho pena dele até hoje." |

### 3.2 Monge Tenzin

| ID | Condição | Fala |
|---|---|---|
| `tenzin_01` | — | "Equilíbrio! *(fica num pé só e cai)* …Estou a aprender." |
| `tenzin_02` | antes de R5_10 | "Atravessas o gelo fino do 43 em sessenta segundos? Eu consegui em cinquenta e nove. Depois caí na água. Conta na mesma." |
| `tenzin_03` | `missao(R5_10) == concluida` | "Não caíste! Nem uma vez! O Mestre diz que é sorte. Eu digo que és um monge e ainda não sabes." |

### 3.3 Irmã Noor — biblioteca

| ID | Condição | Fala |
|---|---|---|
| `noor_01` | — | "Livros sobre a aurora, sobre chá e sobre neve. Os três assuntos importantes. Os outros são opiniões." |
| `noor_02` | — | "Há um livro antigo que diz que a aurora tem uma quinta cor. Dourada. Aparece quando alguém lá em cima se lembra de nós. Bonito. Provavelmente mentira." |
| `noor_03` | `missao(H_10) == concluida` | "Administradores? Temos um livro sobre reis de cima. Chama-se 'Os Que Não Desceram'. Não tem fim. As últimas páginas estão em branco." |

---

## 4. Outras pessoas da região

### 4.1 Benedito, o congelado (andar 44)
Na Sala dos Congelados há um aventureiro de Ascendia preso no gelo **vivo** (pestaneja). Derretê-lo com fogo (5 golpes de
fogo ou uma Bomba) começa uma pequena missão de escolta.
- **Benedito** *(a tremer)*: "Q-que ano é? …Doze anos? Doze anos dentro de um cubo de gelo? A minha mulher deve estar furiosa."
- **Escolta**: levá-lo até ao cristal do andar 44 sem a temperatura dele (barra por cima da cabeça) chegar a 0: passar pelas fogueiras.
- **Em Ascendia**: vive no Bairro Baixo. Fala com a Dona Marta todos os dias: "Doze anos e a sopa ainda é a mesma. Que alívio."
- ⚙ Recompensa: 1 000 ouro · título *Descongelador* · o Benedito vende **Pedras Quentes** na Praça (depois da R5_12).

### 4.2 O Mamute Ancião Tundra
Ver a missão **R5_11** (secção 5). Não fala, mas se o acalmares, às vezes aparece ao longe nos andares 41 e 47 e
**baixa a cabeça** quando passas.

---

## 5. Missões da região, passo a passo

### R5_01 — Casaco Quente
| | |
|---|---|
| Quem dá | Velha Astrid (Pinhal-do-Norte) |
| Recompensa | **Casaco de Lã** (a temperatura desce metade) |

1. **Pedir** — **Astrid**: "Tens os lábios azuis. Dá-me lã de mamute e pele de lobo e faço-te um casaco. Dez e cinco. Não discutas com uma velha."
2. **Passo**: entregar **10 Lã de Mamute** (Mamute Jovem; **não** é preciso matá-los: tosquiar com uma lâmina quando estão a dormir, de noite, também dá 1) + **5 Pele de Lobo de Gelo**.
3. **Entregar** — 🎬 corte rápido: a Astrid a tricotar à lareira, depressíssimo. **Astrid**: "Pronto. Veste. Não tires até à primavera."

### R5_02 — A Sauna da Sigrid
| | |
|---|---|
| Quem dá | Sigrid |
| Recompensa | **Sauna aberta**: a temperatura não desce durante 1 dia depois de uma sauna (30 ouro) |

1. **Pedir** — **Sigrid**: "Vinte pinheiros e dez pedras. Eu sei construir. Não sei carregar. As costas já não deixam."
2. **Passo**: entregar **20 Pinheiro Nevado + 10 Pedra**.
3. **Entregar** — 🎬 a sauna de pé, a fumegar. A aldeia toda faz fila. O Ulf entra primeiro e grita ao sair para a neve.

### R5_03 — Um Pinguim para o Leif
| | |
|---|---|
| Quem dá | Leif |
| Recompensa | **Pinguim** (animal de estimação) — o Leif fica com o outro |

1. **Pedir** — **Leif**: "Dois ovos! Um para mim, um para ti! Mas os ovos não podem arrefecer, senão não nascem. A mãe disse."
2. **Passo 1**: no andar 43, no **ninho de pinguins** atrás do farol, apanhar **2 ovos** (os Pinguins Guerreiros defendem o ninho; se lutares, vêm todos — podes esperar que mergulhem para pescar, de 2 em 2 minutos).
3. **Passo 2**: levar os ovos até Pinhal-do-Norte. Os ovos têm uma **barra de calor** (desce como a temperatura): passar por fogueiras recupera-a. Se chegar a 0, o ovo "adormece" e tens de ir buscar outro.
4. **Entregar** — 🎬 os ovos chocam ao pé da lareira do salão. Dois pinguins pequenos a abanar as asas. O Leif chora de alegria.
   - **Leif** *(feliz)*: "Senhor Fato! E o teu! Como se chama o teu?" ⚙ escolher o nome do pinguim. `tut_animal`.

### R5_04 — Os Cães do Erik
| | |
|---|---|
| Quem dá | Erik Trenó |
| Recompensa | **Trenó** (viagem rápida entre as Zonas Seguras da região, 20 ouro) |

1. **Pedir** — **Erik**: "Quatro cães. Lobo-Cinzento, Mancha, Pimenta e o Tímido. O Tímido não vem se o chamares. Vem se te sentares."
2. **Passos**: encontrar os **4 cães** nos andares 41 e 42 (seguir as pegadas pequenas na neve; latem quando estás a 20 m):
   - **Lobo-Cinzento** — a lutar com 2 Lobos de Gelo (ajudá-lo);
   - **Mancha** — preso num banco de neve (escavar com a Pá ou bater 5 vezes);
   - **Pimenta** — numa ilhota de gelo do rio do 42 (empurrar troncos para fazer ponte);
   - **O Tímido** — escondido numa toca. Sentar ao lado dele ([interagir] → *sentar*) e esperar 10 s.
3. **Entregar** — os cães correm para o Erik e derrubam-no na neve. **Erik** *(a rir)*: "Dez! Dez outra vez! Sobe! Vamos dar uma volta! Agora!"

### R5_05 — Reconstruir a Aldeia (5 partes)
| | |
|---|---|
| Quem dá | Caçadora Inga (andar 46) |
| Recompensa | cada parte: um edifício e um NPC (ver secção 2.2) · no fim: **festa** na aldeia e o **Arco de Gelo Eterno** (Épico) |

1. **Pedir** — **Inga**: "Cinco casas. Uma de cada vez. Eu digo o que falta. Tu trazes."
2. **Partes** (pela ordem que quiseres; os materiais estão em `docs/regioes/r05_gelo.md`, secção 7.2):
   - **Cabana Comum** → cama e cristal · **Inga**: "Uma cama. Primeira vez em quinze anos que não durmo sozinha numa aldeia."
   - **Forja do Caçador** → Gunnar · **Casa da Curandeira** → Helka · **Armazém** → Sven · **Torre do Sino** → Olaf.
3. **Entregar** — 🎬 festa à noite: fogueiras, carne no espeto, o Olaf toca o sino de alegria (e os congelados param e ouvem). A Inga dança, mal, uma vez.
   - **Inga** *(feliz, rara)*: "Toma. O arco da minha mãe. Gelo Eterno. Não parte. Como ela."

### R5_06 — O Diário de Gorvan (história)
= **H_12**. Ver as cenas **C5-04 e C5-05** em `docs/guiao/cap05_gelo.md`.

### R5_07 — A Cria de Presa-Branca
Dada pelo **Zed** (depois de vencer o Presa-Branca, que deixa cair a cria na 1.ª vez). Falas em `docs/dialogos/zed.md`.
- **Passo**: levar a cria do andar onde venceste o Presa-Branca até ao cristal e depois ao Rancho do Zed. A cria tem uma **barra de calor** (como os ovos da R5_03).
- **Recompensa**: **Montada Lobo de Gelo**.

### R5_08 — Meditação
| | |
|---|---|
| Quem dá | Mestre Kael (Mosteiro da Aurora) |
| Recompensa | skill passiva **Meditação** (parado 2 s: o MP regenera ×3) |

1. **Pedir** — **Kael**: "Quatro pedras. Verde, azul, roxa e a que canta quando ninguém olha. Toca-lhes quando a aurora tiver a cor delas. Pela ordem que o céu quiser."
2. **Passo**: no andar 48, as 4 **Pedras Cantantes** (a aurora muda de cor de 2 em 2 minutos):
   - pedra **verde** (aurora verde) · pedra **azul** (aurora azul) · pedra **roxa** (aurora roxa);
   - a 4.ª pedra é **branca**: toca-se com a aurora em **qualquer cor**, mas só se ficares **parado ao lado dela 30 s sem tocar em nada** (a pedra canta sozinha).
3. **Entregar** — **Kael**: "Ouviste a quarta? Não se toca. Espera-se. Agora sabes."

### R5_09 — O Kraken do Lago
| | |
|---|---|
| Quem dá | Ulf Barba-Gelo |
| Recompensa | **Arpão** (pesca de peixes grandes, como o Narval Real) |

1. **Pedir** — **Ulf**: "O Kraken do 43. Vence-o. Mas não partas o gelo à volta do farol! O farol é o caminho seguro! Sem o gelo, o farol fica numa ilha e ninguém o acende!"
2. **Passo**: vencer o **Kraken do Gelo** (guardião do andar 43) sem que nenhum buraco novo se abra no círculo à volta do farol (marcado no chão a branco). O Kraken parte o gelo com o ataque **Partir o gelo**: interrompe-o (bater no tentáculo que se levanta) quando ele aponta para o farol.
3. **Entregar** — `ulf_05`.

### R5_10 — Gelo Fino
| | |
|---|---|
| Quem dá | Monge Tenzin |
| Recompensa | **Botas de Pico** (não escorregas no gelo) |

1. **Pedir** — `tenzin_02`.
2. **Passo**: atravessar o **Gelo Fino** do andar 43 de uma ponta à outra em **60 s**. O gelo racha se ficares parado 1 s. Com o farol aceso (puzzle do andar), o caminho seguro aparece; sem ele, é às cegas.
3. **Entregar** — `tenzin_03`.

### R5_11 — O Gigante Gentil
Dada pela **Capitã Freya** (rank B; = `G_B_02`). Falas em `docs/dialogos/freya.md`.
- **Escolha**:
  - **vencer** o Mamute Ancião → Marfim Ancestral · flag `mamute_morto`;
  - **acalmá-lo**: dar-lhe **20 Bagas de Inverno** sem o atacar (aproximar devagar: se correres, foge; ele come 5 de cada vez, 4 vezes) → Lã Ancestral ×5, título *Amigo dos Gigantes* · flag `mamute_acalmado`.
- O **Zed** reage às duas (`docs/dialogos/zed.md`). Conta para uma pequena cena no final ("Amigo dos Gigantes").

### R5_12 — Fogueira Eterna
| | |
|---|---|
| Quem dá | Velho Fausto |
| Recompensa | receita **Pedra Quente** (a temperatura não desce durante 5 min) |

1. **Pedir** — **Fausto**: "Há um iglu no 41 com uma fogueira que nunca se apaga. Uma fogueira eterna! Traz-me uma brasa. Numa lata. Não na mão. Na mão já tentaram."
2. **Passo**: encontrar o **iglu escondido** (Pedras de Vento, andar 41) e apanhar uma **Brasa Eterna** com uma **Lata** (Tobias, 10 ouro).
3. **Entregar** — 🎬 o Fausto põe a brasa num frasco e fica a olhar para ela. **Fausto** *(feliz)*: "Não queima o vidro. Não gasta nada. Arde e não come. Isto contraria três livros meus. Esplêndido. Toma, uma receita, para te aqueceres enquanto eu reescrevo os livros."

### R5_13 — Chá de Bagas
Dada pela **Dona Marta**. Falas em `docs/dialogos/marta.md`. Entregar **10 Bagas de Inverno** → receita **Chá Quente**.

### R5_14 — Balistas
Dada pela **Capitã Freya**. Falas em `docs/dialogos/freya.md`. No andar 49, usar as **balistas** das torres ([interagir] para montar; [atacar] para disparar) para derrubar **10 Harpias Gélidas**.

### R5_15 — Descanso para os Caçadores
| | |
|---|---|
| Quem dá | Caçadora Inga (depois da R5_05) |
| Recompensa | **Amuleto do Caçador** (+15% de dano a monstros que não te viram) |

1. **Pedir** — **Inga**: "Os congelados. Dez. Com fogo ou luz, descansam a sério. Os diários deles, enterra-os ao pé da torre. Cinco. Para terem nome."
2. **Passos**: vencer **10 Caçadores Congelados** com dano de **Fogo** ou **Luz** (o último golpe) · apanhar **5 Diários de Caçador** (drop 10%) e enterrá-los no **cemitério** atrás da torre do sino ([interagir] em cada campa).
   - Ao enterrar cada diário: `[Sistema] {nome do caçador} descansa.` (nomes: Halvar, Ragna, Torvi, Eskil, Brynja)
3. **Entregar** — `inga_06`. 🎬 o Olaf toca o sino uma vez, devagar.

---

## 6. Missões da Guilda (rank B) da região

A G_B_01 e a G_B_03 são da região 4 (`docs/dialogos/povoacoes_r04.md`).

| Missão | Texto do quadro | Lyra ao aceitar | Lyra ao entregar |
|---|---|---|---|
| G_B_02 O Gigante Gentil (R5_11) | "Um mamute gigante anda pelos andares 41 e 47. Os exploradores têm medo. Resolver. (A Guilda não diz como.)" | "A Guilda não diz como! Isso quer dizer que posso escolher? Escolhe bem. Os mamutes têm memória comprida." | *(acalmado)* "Acalmaste-o! O Zed chorou quando lhe contei. Disse que era pó. Era choro." · *(morto)* "Pronto. Está resolvido. …Está. O registo diz 'resolvido'." |
