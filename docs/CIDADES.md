# Cidades e povoações

- **Ascendia**: a cidade na base da torre, a tua base.
- **A tua casa** em Ascendia.
- **22 povoações** dentro da torre (lista na secção 4; os detalhes estão nos ficheiros das regiões).
- **Vagar, a Cidade Errante**: uma cidade que **aparece num andar ao acaso** todas as semanas.

---

## 1. Ascendia

Cidade de pedra clara e telhados vermelhos construída em círculo à volta da base da torre, por pessoas que
ficaram presas ao longo de séculos (Jogadores que desistiram, Torrenses que desceram, gente de mundos engolidos).
A torre vê-se de todo o lado: é uma coluna gigante que desaparece nas nuvens.

### 1.1 Mapa (de cima)

```
                         N
          ┌──────────── Muralha ────────────┐
          │  Zona          Bairro da         │
          │  Residencial   Guilda   Quartel  │
          │  (a tua casa)  (Guilda) + Arena  │
          │                                  │      Quintas
 Bairro   │  Bairro dos    ┌──────┐  Mercado │      (Hana, Zed,
 Baixo ───│  Artesãos      │TORRE │  Taberna │────  a tua quinta)
 (Rook)   │  (Brom, Selene,│Praça │  Estalagem│
          │  Elva, Gizmo)  └──────┘          │
          │        Bairro Alto (colina):     │
          │   Governador · Igreja · Biblioteca · Vidente
          └──────── Rio e Porto (Pip) ───────┘
                         S
```

### 1.2 Bairros e edifícios

| Bairro | Edifícios | NPCs |
|---|---|---|
| **Praça da Torre** (centro) | Entrada da torre com o **Cristal Mestre**, fonte, **quadro de avisos**, palco dos festivais, **estátuas dos bosses** que venceste (aparece uma por cada boss) | Kai (a treinar à noite), crianças, aldeões |
| **Bairro da Guilda** (norte) | **Guilda de Aventureiros** (Cristal de Avaliação, quadro de missões), **Quartel da Guarda** e **Arena**, campo de treino com bonecos | Lyra, Mestre Gorvan, Capitã Freya |
| **Mercado** (leste) | **Mercado** com bancas, **Taberna "O Primeiro Degrau"**, **Estalagem "Ninho do Viajante"** | Tobias, Lucien, Dona Marta |
| **Bairro dos Artesãos** (oeste) | **Forja do Brom**, **Alquimia da Selene**, **Costura da Elva**, **Oficina do Gizmo** (com a mesa de joalharia) | Brom, Selene, Elva, Gizmo |
| **Bairro Alto** (colina a sul) | **Câmara do Governador**, **Igreja da Luz**, **Biblioteca**, **Tenda da Vidente** | Aldric, Irmã Célia, Velho Fausto, Madame Oriel |
| **Bairro Baixo** (sudoeste) | casas pobres, becos, o **esconderijo do Rook** (mercado negro a partir do rank C) | Rook, Mia (vende flores na esquina) |
| **Rio e Porto** (sul) | cais, barcos de pesca, ponte (projeto "Ponte do Rio") | Pip |
| **Quintas** (fora da muralha, a leste) | **Quinta da Hana**, **Rancho do Zed**, **a tua quinta** | Hana, Zed |
| **Zona Residencial** (noroeste) | casas dos NPCs, **a tua casa** (depois do andar 20) | — |

### 1.3 O que abre à medida que sobes

| Quando | O que abre em Ascendia |
|---|---|
| Início | Guilda, Mercado, Estalagem, Forja, Alquimia, Igreja, Biblioteca, Taberna (rumores), Rio (pesca a partir do andar 3) |
| Andar 10 (Ent Ancião) | Quinta (Hana), Câmara do Governador (**melhorias da cidade**), Bênçãos (Igreja), 1.º **Dia da Subida** |
| Andar 15 | Rancho do Zed (animais de estimação) |
| Andar 16+ | Oficina do Gizmo (engenhocas e joalharia), Costura da Elva |
| Rank C | Mercado negro do Rook |
| Andar 20 (Golem de Cristal) | **A tua casa**, Tenda da Vidente (profecias) |
| Andar 30 (Hidra) | Arena (Prata), minijogos da Taberna |
| Andar 40 (Faraó) | Montadas no Rancho do Zed |
| Andar 50 (Dragão) | Grande festa; a Praça ganha um palco maior e o Lucien a "Balada do Andar 50" |
| Andar 60 | Doca do teu barco no Porto (o barco do andar 52 pode ser trazido) |
| Andar 80 | O Gorvan volta a treinar no campo da Guilda (aulas de combate) |
| Andar 100 | A Praça muda conforme o **final** (ver `docs/HISTORIA.md`) |

### 1.4 Melhorias da cidade (Governador Aldric)

Doas materiais e ouro na Câmara; a obra demora 3 dias e muda a cidade (vê-se no mapa).

| Projeto | Custo | Efeito | Abre |
|---|---|---|---|
| Ponte do Rio | 40 Carvalho + 500 ouro (missão R1_02) | atalho para o Porto | andar 10 |
| Iluminação das Ruas | 20 Lingote de Cobre + 20 Cristal de Gruta | a cidade fica iluminada à noite; NPCs ficam na rua até mais tarde | andar 15 |
| Fonte Nova | 30 Pedra + 10 Lingote de Ferro | +1 ponto de amizade extra por dia com quem passa na praça | andar 15 |
| Mercado Coberto | 40 Escora Velha + 1 000 ouro | o Tobias tem mais 4 itens raros | andar 20 |
| Muralha Reforçada | 50 Pedra + 20 Lingote de Aço | eventos de invasão de monstros à cidade ficam mais fáceis | andar 25 |
| Escola de Aventureiros | 30 Mangue + 2 000 ouro | os aventureiros resgatados dão aulas: +10% XP das skills de armas | andar 30 |
| Jardim Público | 20 sementes diferentes | festivais da Primavera com mais flores; Hana vende sementes raras | andar 30 |
| Banhos Públicos | 20 Lingote de Prata + 10 Vidro Solar | banho: +10% regeneração 1 dia | andar 40 |
| Teatro | 30 Acácia + 3 000 ouro | o Lucien faz peças sobre os teus feitos (cenas engraçadas) | andar 40 |
| Hospital | 20 Barra de Gelo Eterno + 20 Flor-de-Neve | morrer custa menos (perdes 15% dos materiais em vez de 30%) | andar 45 |
| Aquário Municipal | 1 de cada peixe das regiões 1–5 | os peixes da tua coleção ficam em exposição; bónus de pesca +5% | andar 50 |
| Farol do Porto | 20 Barra de Coral + 10 Pérola | pesca noturna no rio de Ascendia; peixes raros | andar 55 |
| Torre de Vigia | 20 Barra de Obsidiana + 5 000 ouro | o mapa mostra os eventos dos andares (Mercador Errante, monstros com nome) | andar 65 |
| Catedral de Ascendia | 20 Lingote de Mitril + 10 Diamante | a Igreja vende Água Benta mais barata; bênçãos mais fortes | andar 75 |
| Porto de Balões | 20 Madeira-Nuvem + 10 Fio de Nuvem | viagem de balão de Ascendia para qualquer Zona Segura | andar 85 |
| Observatório de Ascendia | 10 Cristal Celeste + 5 Estrela Cadente | a Madame Oriel dá dicas sobre os lendários | andar 88 |
| Monumento à Subida | 1 troféu de cada região | estátua gigante teu na praça; título *Herói de Ascendia* | andar 90 |
| Ponte para as Estrelas | 20 Lingote Estelar + 10 Fragmento de Sistema | só no final "A Ponte" (ver história) | final |

### 1.5 Pessoas que vão viver para Ascendia

Ao longo do jogo, pessoas que **salvas ou ajudas** mudam-se para a cidade e passam a fazer coisas:

| Quem | De onde (missão) | O que faz em Ascendia |
|---|---|---|
| Tina | R1_13 | ajudante da Selene: poções 10% mais baratas |
| Bolota (fungoide) | R2_06 | vive na quinta da Hana; vende Fungo Azul |
| Pedrito | R2_13 | aprendiz do Brom: melhorias +1 a +5 20% mais baratas |
| 3 aventureiros do Ninho | R2_04 | dão aulas na Escola de Aventureiros (com a melhoria) |
| Aventureiro congelado (andar 44) | resgate | abre uma banca de mapas (vende mapas dos andares) |
| Príncipe Maré (visitas) | R6_09 | aparece no Porto no Verão, com presentes do mar |
| 4 prisioneiros do Reino | R8_11 | um é cozinheiro (5 receitas novas na Estalagem), outro ferreiro (ajuda o Brom), outro jardineiro, outro músico (toca com o Lucien) |
| Kai | se o salvaste | treina na praça; companheiro |
| Ssark | se defendeste a aldeia | visita a cidade nos festivais |
| Perdidos convencidos | R10_07 | no final, a Praça enche-se deles |

---

## 2. A tua casa

O Governador oferece-te uma casa depois do **andar 20**. É a tua base: dormir, guardar, cozinhar, expor
o que conquistaste.

### 2.1 Tamanhos

| Tamanho | Como | Espaço |
|---|---|---|
| Casinha | grátis (andar 20) | 1 divisão + cama + cozinha pequena |
| Casa | 10 000 ouro + 50 madeira | 3 divisões + **sala de troféus** |
| Casarão | 50 000 ouro + 100 madeira + 50 lingotes | 6 divisões + cave + jardim grande |
| Mansão da Torre | 200 000 ouro + materiais de todas as regiões | 10 divisões + torre de vigia + lago |

### 2.2 O que se pode ter em casa

| Coisa | Para quê |
|---|---|
| **Cama** | dormir e gravar (grátis) |
| **Fogão** | cozinhar |
| **Mesa de alquimia, forja pequena, tear** | crafting em casa |
| **Baús** | 50 espaços cada, até 8 |
| **Parede de armas** | expor as armas que tens (há espaço para **todas as armas do jogo**; completar a parede dá o título *Colecionador*) |
| **Sala de troféus** | os troféus dos 20 bosses e dos monstros com nome |
| **Aquário** | os peixes que pescaste nadam lá |
| **Estufa escura** | plantar fungos e plantas de sombra |
| **Lago** | plantar Alga Doce, Lírio, Lótus |
| **Gira-discos** | ouvir as músicas que já ouviste no jogo (e a música "Casa") |
| **Telescópio** | (missão R9_06) |
| **Espelho Mágico** | (missão R10_04) |
| **Museu da Subida** | (andar 94) |
| **Móveis e decoração** | ~200 peças: compradas, feitas na carpintaria (forja + madeira) ou ganhas em missões |
| **Animais** | o teu animal de estimação dorme em casa; a Aranha de Seda vive no canto |

- **Convidar NPCs**: com 6+ corações, um NPC aceita vir jantar a tua casa (cena + amizade).
- **Concurso da Casa Mais Bonita**: festival do Outono (o Lucien e o Governador são os juízes).

---

## 3. A quinta

O terreno fica fora da muralha, ao lado da quinta da Hana. Abre no **andar 10**.

| Coisa | Como funciona |
|---|---|
| Terreno | começa com 6×6 talhões; a Hana alarga-o (até 20×20) |
| Plantar | sementes das regiões (cada região tem as suas, ver os ficheiros das regiões e `docs/ITENS.md`) |
| Regar | todos os dias (ou com o **Autómato de Quinta**, missão R7_14); a chuva rega sozinha |
| Estações | cada planta só cresce em certas estações (a estufa permite todas) |
| Qualidade | Normal / Boa / Excelente; o Guano melhora a qualidade |
| Árvores | plantadas uma vez, dão sempre |
| Animais da quinta | galinhas, vacas, cabras e ovelhas (Zed vende): ovos, leite, queijo, lã |
| Espantalho | sem espantalho, os corvos comem 1 planta por dia |
| Planta de guarda | a **Semente Carnívora** (região 3) come as pragas |

---

## 4. Povoações dentro da torre

| Andar | Povoação | Povo | Serviços | Detalhes |
|---|---|---|---|---|
| 2 | Acampamento dos Lenhadores | humanos de Ascendia | cama, cristal, loja | `regioes/r01_floresta.md` |
| 7 | **Folhalta** | elfos da floresta | estalagem, cristal, loja élfica, treino de arco | `regioes/r01_floresta.md` |
| 11 | Posto Mineiro Fundo-Rocha | mineiros (humanos e anões) | cama, cristal, loja, forja simples | `regioes/r02_cavernas.md` |
| 16 | **Mycélia** | Fungoides | estalagem, cristal, loja (aceita cogumelos) | `regioes/r02_cavernas.md` |
| 18 | Fantasmas da Forja Anã | fantasmas de anões | loja de lingotes antigos | `regioes/r02_cavernas.md` |
| 24 | **Aldeia Sssar** | Homens-Lagarto | cabana, cristal, loja tribal (só se a aldeia for amiga) | `regioes/r03_pantano.md` |
| 26 | **Vila Coaxa** | Homens-Sapo | estalagem, cristal, loja, barcos | `regioes/r03_pantano.md` |
| 28 | Refúgio das Copas | exploradores | cama, cristal, loja | `regioes/r03_pantano.md` |
| 32 | **Oásis de Zahra** | Torrenses do deserto | estalagem, cristal, bazar (5 lojas), forja, banhos | `regioes/r04_deserto.md` |
| 34 | Acampamento dos Escavadores | arqueólogos | tenda, cristal, loja | `regioes/r04_deserto.md` |
| 37 | Nómadas do Vento | nómadas (mudam de sítio) | tenda, loja | `regioes/r04_deserto.md` |
| 42 | **Pinhal-do-Norte** | gente do norte | salão, cristal, loja, sauna, trenó | `regioes/r05_gelo.md` |
| 46 | Aldeia dos Caçadores | caçadores (reconstrução) | depende da reconstrução | `regioes/r05_gelo.md` |
| 48 | Mosteiro da Aurora | monges | celas, cristal, chá | `regioes/r05_gelo.md` |
| 52 | **Porto Arquipélago** | ex-piratas | estalagem, cristal, estaleiro, loja | `regioes/r06_oceano.md` |
| 54 | Vila das Pérolas | mergulhadores | cabana, cristal, loja | `regioes/r06_oceano.md` |
| 57 | **Coralina** | sereias e tritões | estalagem, cristal, forja de coral, loja | `regioes/r06_oceano.md` |
| 61 | Acampamento das Cinzas | refugiados | tenda, cristal, loja básica | `regioes/r07_vulcao.md` |
| 64 | **Bastião de Obsidiana** | anões do fogo (Clã Brasa) | estalagem, cristal, loja, Forja de Obsidiana | `regioes/r07_vulcao.md` |
| 66 | Termas dos Géiseres | gnomo e turistas | estalagem, cristal, loja, termas | `regioes/r07_vulcao.md` |
| 72 | **Mercado Fantasma** | fantasmas (só à noite) | hotel fantasma, lojas | `regioes/r08_reino_assombrado.md` |
| 77 | Mosteiro da Ordem da Luz | monges caçadores | celas, cristal, loja, forja de Mitril | `regioes/r08_reino_assombrado.md` |
| 82 | **Aerópolis** | Alados | estalagem, cristal, forja, loja, balões | `regioes/r09_ceu.md` |
| 86 | Observatório Celeste | astrónomos | cama, cristal, loja | `regioes/r09_ceu.md` |
| 91 | Último Posto | Guilda | cama, cristal, loja, Forja Estelar | `regioes/r10_abismo.md` |
| 97 | **Cidade dos Perdidos** | Jogadores que desistiram | casa, cristal, Mercado das Memórias | `regioes/r10_abismo.md` |

(As povoações a **negrito** são cidades grandes; as outras são pequenas.)

---

## 5. Vagar, a Cidade Errante

Uma cidade de mercadores construída nas costas de uma **tartaruga gigante** que viaja entre andares por portais.
**Aparece num andar ao acaso** (dos que já desbloqueaste) e fica lá **2 dias**. Depois desaparece e volta passados
**5 dias** noutro andar. O quadro de avisos de Ascendia e a Madame Oriel dizem onde está.

| | |
|---|---|
| Tamanho | 128×128 (a tartaruga) + uma pequena cidade em cima (escadas de corda para subir) |
| Música | `vagar` (acordeão e tambores) |
| Desbloqueia | depois do andar 20 |

| NPC | Quem é | O que faz |
|---|---|---|
| **Senhora Vagar** | velha capitã da tartaruga, cachimbo de bolhas | Conta histórias de todos os andares; dá missões de entrega entre povoações |
| **Mercador Errante Ambrósio** | o mercador dos eventos | Vende itens raros **de qualquer região**, incluindo de regiões a que ainda não chegaste (caro!) |
| **Leiloeiro Gaspar** | leilão semanal | **Leilão**: 3 itens raros por visita; licitas contra NPCs |
| **Troca-Tudo** | gnomo das trocas | Troca materiais de uma região por materiais de outra (2 por 1) |
| **Madame Plumas** | estilista | Cosméticos únicos: cores do herói, chapéus, capas |
| **Tartaruga Vagar** | a própria tartaruga | Se lhe deres 10 Alga Doce, ela leva-te ao andar mais alto que tens desbloqueado |

**Atividades em Vagar**: a **Arena Errante** (desafios com regras malucas: só manoplas, sem esquiva, de olhos vendados…),
**jogo das conchas**, **pesca na tartaruga** (peixes de todas as regiões) e a **Coleção Vagar** (selos de cada andar
onde a encontraste: 50 selos = título *Viajante Errante* e uma tartaruguinha como animal de estimação extra).
