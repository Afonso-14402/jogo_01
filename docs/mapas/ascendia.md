# Mapa de Ascendia

A cidade na base da torre (descrição e bairros em `docs/CIDADES.md`). Tamanho: **300×220 m** · 30×22 células de
10 m · norte em cima. As células da cidade usam **abreviaturas de 2 letras** (legenda abaixo).

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d 
  1  tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
  2  tttttttttttt######################################tttttttttt
  3  tttttttttttt##cacaTCcaca::GuGuGuGuGu::QuQuArArAr##tttttttttt
  4  tttttttttttt##caca..caca::GuGuGuGuGu::QuQuArArAr##tttttttttt
  5  tttttttttttt##..........::TrTr..TrTr::....ArArAr##tttttttttt
  6  tttttttttttt##::::::::::::::::::::::::::::::::::##tttttttttt
  7  tttttttttttt##FoFo..AlAl::....Eb....Eb::MeMeMeMe##tttttttttt
  8  cbcbcbcbcb..##FoFo..AlAl::..▓▓▓▓▓▓▓▓..::MeMeMeMe##HaHaHa....
  9  cbRocbcb::::][..........::Fn▓▓▓▓▓▓▓▓Pa::TaTaEsEs][::::HaHaHa
 10  cbcbcbMicb..##GiGi..CoCo::..▓▓Cr▓▓▓▓..::TaTaEsEs##ZeZe..QtQt
 11  cbcbcbcbcb..##GiGi..CoCo::....Qa......::........##ZeZe..QtQt
 12  ttcbcbcbtt..##::::::::::::::::::::::::::::::::::##tt::tttttt
 13  tttttttttttt##tttt^^^^GoGoGo^^^^IgIgIg^^^^^^tttt##tt::tttttt
 14  tttttttttttt##tt^^^^^^GoGoGo^^::IgIgIg^^BiBi^^tt##tt::tttttt
 15  tttttttttttt##tt^^Vi^^^^^^^^^^::^^^^^^^^BiBi^^tt##tt::tttttt
 16  tttttttttttt##tttt^^^^^^^^^^^^::^^^^^^^^^^^^tttt##tt::tttttt
 17  tttttttttttt##tttttt..........::..........tttttt##tt::tttttt
 18  tttttttttttt##################][##################tt::tttttt
 19  tttttttttt....................::....................::tttttt
 20  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~==~~~~~~~~~~~~~~~~~~~~::tttttt
 21  tttttttt............PiCaCaCaCa......................::tttttt
 22  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

## Legenda da cidade

| Marca | O que é | Marca | O que é |
|---|---|---|---|
| `##` | muralha | `][` | porta da muralha |
| `::` | rua | `..` | praça, largo ou chão de terra |
| `tt` | árvores, jardins | `^^` | colina do Bairro Alto (sobe até 8 m) |
| `~~` | rio | `==` | Ponte do Rio (só depois do projeto R1_02) |
| `▓▓` | **a Torre** | `Cr` | **Cristal Mestre** (entrada da torre) |
| `Fn` | fonte | `Pa` | palco dos festivais |
| `Qa` | quadro de avisos | `Eb` | estátuas dos bosses (aparece uma por cada boss vencido, à volta da praça) |
| `Gu` | Guilda de Aventureiros | `Tr` | campo de treino (bonecos) |
| `Qu` | Quartel da Guarda | `Ar` | Arena |
| `ca` | casas dos NPCs | `TC` | **a tua casa** (depois do andar 20) |
| `Fo` | Forja do Brom | `Al` | Alquimia da Selene |
| `Gi` | Oficina do Gizmo | `Co` | Costura da Elva |
| `Me` | Mercado (Tobias) | `Ta` | Taberna "O Primeiro Degrau" |
| `Es` | Estalagem "Ninho do Viajante" | `Go` | Câmara do Governador |
| `Ig` | Igreja da Luz | `Bi` | Biblioteca |
| `Vi` | Tenda da Vidente | `cb` | casas pobres do Bairro Baixo |
| `Ro` | esconderijo do Rook | `Mi` | esquina da Mia (vende flores) |
| `Ha` | Quinta da Hana | `Ze` | Rancho do Zed |
| `Qt` | **a tua quinta** (abre no andar 10) | `Pi` | sítio do Pip no cais |
| `Ca` | cais e barcos de pesca | | |

## Bairros

| Bairro | Células | Quem está lá |
|---|---|---|
| Praça da Torre | N7–S11 | Kai (a treinar à noite), crianças, aldeões; festivais no palco |
| Bairro da Guilda | N3–X5 | Lyra, Mestre Gorvan (Guilda), Capitã Freya (Quartel) |
| Zona Residencial | H3–L5 | casas dos NPCs e a tua (`TC`, J3) |
| Bairro dos Artesãos | H7–L11 | Brom, Selene, Gizmo, Elva |
| Mercado | U7–X11 | Tobias, Lucien (Taberna), Dona Marta (Estalagem) |
| Bairro Alto | H13–W17 | Governador Aldric, Irmã Célia, Velho Fausto, Madame Oriel |
| Bairro Baixo (fora da muralha) | A8–F12 | Rook, Mia; entra-se pela porta oeste (G9) |
| Quintas (fora da muralha) | Z8–d11 | Hana, Zed, a tua quinta; entra-se pela porta este (Y9) |
| Rio e Porto (fora da muralha) | A19–d21 | Pip, barcos de pesca |

## Caminhos

- **Cruz de ruas**: duas ruas norte–sul (colunas M e T) e duas este–oeste (linhas 6 e 12) à volta da Praça.
- **Porta sul** (P18) → rua → rio. **Antes da Ponte do Rio** (R1_02) não há passagem direta para o Porto: vai-se pela
  margem até ao caminho da coluna **a**, à volta do braço do rio, e volta-se para oeste pela linha 21.
  **Depois da ponte** (P20) desce-se a direito: é o "atalho para o Porto" do projeto.
- **Porta oeste** (G9) → Bairro Baixo. **Porta este** (Y9) → Quintas e caminho para o Porto.
- A muralha não tem porta a norte: a norte da cidade só há floresta e montanhas.

## O que muda no mapa com o tempo

| Quando | Muda |
|---|---|
| andar 10 | abre a tua quinta (c10–d11) |
| projeto Ponte do Rio | aparece a ponte em P20 |
| cada boss vencido | aparece uma estátua `Eb` à volta da praça (há lugar para 20: 2 desenhadas, as outras nas células `..` da praça) |
| andar 20 | a tua casa (`TC`) fica com a porta aberta |
| melhorias da cidade (`docs/CIDADES.md`, secção 1.4) | cada uma tem um sítio: Fonte Nova em N9, Mercado Coberto por cima de U7–X8, Escola de Aventureiros no lugar do campo de treino, Jardim Público em K17–O17, Banhos Públicos ao pé da Estalagem, Teatro ao pé da Taberna, Hospital ao pé da Igreja, Aquário e Farol no Porto, Torre de Vigia na muralha (Y2), Catedral no lugar da Igreja, Porto de Balões no cimo da colina (ao lado de P15), Observatório ao pé da Vidente, Monumento à Subida no centro da praça, Ponte para as Estrelas no topo da torre |

## Notas para construir

- A Praça é plana; o Bairro Alto sobe em degraus largos até 8 m (vê-se a cidade toda lá de cima).
- A Torre ocupa 4×3 células (40×30 m) mas sobe até fora do ecrã: o modelo é só a base com 60 m e o resto é
  um "skybox" pintado que se vê de qualquer sítio da cidade.
- Os interiores (Guilda, Forja, Estalagem…) são **cenas separadas**: entrar numa porta muda de cena.
