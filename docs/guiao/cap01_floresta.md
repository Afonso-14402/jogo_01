# Guião — Capítulo 1: A Floresta (andares 1–10)

Missões: **H_04 O Rei das Tocas**, **H_05 A Árvore-Mãe**. As cenas das povoações e das missões secundárias
estão em `docs/dialogos/povoacoes_r01.md`.

---

## C1-01 — Um Casaco Azul Passou por Aqui

| | |
|---|---|
| ID | `cena_c1_01_acampamento` |
| Quando | entrar pela primeira vez no Acampamento dos Lenhadores (andar 2) |
| Onde | andar 2, Acampamento dos Lenhadores |
| Quem | herói, Bruno Machadão |
| Música | `floresta_dia` |

🎬 Bruno parte um tronco com um só golpe de machado e ri-se alto. Vê o herói.

- **Bruno** *(feliz)*: "AH-AH! Mais um Jogador! Este ano está a chover Jogadores!"
- **Bruno** *(normal)*: "Ainda agora passou um rapaz de casaco azul a correr. Nem disse bom dia! Comeu-me três salsichas da grelha a correr."
- **Bruno** *(feliz)*: "Se é teu amigo, diz-lhe que me deve três salsichas."

▶ **"É meu rival."**
▶ **"É meu amigo."**

- *(rival)* **Bruno**: "Rivais! Bonito! Então corre também, que ele vai à frente!"
- *(amigo)* **Bruno**: "Então pagas tu as salsichas! AH-AH! Estou a brincar. Um bocadinho."
- **Bruno** *(normal)*: "Aqui tens cama e uma fogueira. E se precisares de trabalho, eu preciso de braços."

⚙ Desbloqueia o Acampamento (cama, cristal, loja). Missões R1_01 e R1_02 disponíveis.

---

## C1-02 — O Rei das Tocas

| | |
|---|---|
| ID | `cena_c1_02_javali_antes` |
| Quando | entrar na Grande Toca (andar 5) |
| Onde | andar 5, Grande Toca |
| Quem | herói, Kai, Javali-Rei |
| Música | silêncio → `javali_rei` |

🎬 O herói entra na arena. Do outro lado, ao mesmo tempo, entra o Kai, sem fôlego.

- **Kai** *(zangado)*: "O QUÊ? Tu?! Eu vim pelo atalho!"
- **Kai** *(zangado)*: "…Que atalho tinha lama até aos joelhos."

🎬 O chão treme. Raízes rebentam no centro. O **Javali-Rei** sai da terra, enorme, com a coroa de raízes.
🎬 Bufa vapor pelo focinho e raspa a pata.

- `[Sistema] Mini-boss: Javali-Rei, o Rei das Tocas.`
- **Kai** *(feliz)*: "Muda a aposta. Quem lhe tirar mais vida paga o jantar."

▶ **"Aceito."**
▶ **"Primeiro sobrevivemos, depois apostamos."**

- *(Aceito)* **Kai**: "Isso!"
- *(Primeiro sobrevivemos)* **Kai** *(sério)*: "…Está bem. Tens razão. Mas depois apostamos."

⚙ **O Kai luta a teu lado** nesta luta (companheiro temporário, nível igual ao teu).
⚙ No fim, o jogo conta quanto dano fez cada um.

## C1-03 — Empate

| | |
|---|---|
| ID | `cena_c1_03_javali_depois` |
| Quando | vencer o Javali-Rei |
| Onde | andar 5, Grande Toca |
| Quem | herói, Kai |

🎬 O Javali-Rei cai de lado. A coroa de raízes desfaz-se. Os javalis pequenos fogem.

- `[Sistema] Mini-boss derrotado: Javali-Rei.`
- `[Sistema] Obtiveste: Presa do Javali-Rei.`
- `[Sistema] Título obtido: Caçador de Reis.`

🎬 O Kai senta-se no chão a arfar e olha para a janela azul dele.

- *(se tiveres feito mais dano)* **Kai** *(zangado → feliz)*: "…Tiraste mais do que eu. Tsc. Sorte." 🎬 *estende a mão para um aperto de mão.* "Pago eu. Desta vez."
- *(se o Kai tiver feito mais)* **Kai** *(feliz)*: "HA! Pagas tu! E eu vou pedir o prato mais caro."
- **Kai** *(sério)*: "Ei. Não és mau nisto, número redondo."

⚙ +50 amizade com o Kai. Missão **H_04** concluída. Cena de jantar disponível na Estalagem esta noite.

---

## C1-04 — O Jantar da Aposta

| | |
|---|---|
| ID | `cena_c1_04_jantar` |
| Quando | entrar na Estalagem à noite depois do Javali-Rei |
| Onde | Estalagem |
| Quem | herói, Kai, Dona Marta |
| Música | `amizade` |

🎬 Kai e o herói numa mesa ao canto. Dona Marta traz dois pratos de Assado de Javali.

- **Dona Marta** *(feliz)*: "Javali-rei assado! Bem… javali normal. Mas assado com amor."
- 🎬 Kai come muito depressa.
- **Kai** *(normal, de boca cheia)*: "Sabes o que eu tinha de comer em casa? Ramen da loja da esquina. Todos os dias."
- **Kai** *(normal)*: "A minha irmã dizia que eu ia virar massa."
- 🎬 Kai pára de comer.

▶ **"Tens uma irmã?"**
▶ **"Tens saudades de casa?"**

- **Kai** *(triste)*: "A Yui. Tem sete anos. Quando eu caí aqui, ela estava à minha espera à porta da escola."
- **Kai** *(triste)*: "…Já passaram oito meses. Ela deve achar que eu fugi."
- 🎬 Silêncio. A lareira estala.
- **Kai** *(normal, a forçar um sorriso)*: "Por isso tenho de chegar ao topo. Rápido. Mais rápido do que tu, de preferência."

▶ **"Vamos chegar os dois."**
▶ **"Vou chegar primeiro."**

- *(os dois)* **Kai** *(surpreso → feliz)*: "…Pois. Os dois." ⚙ +80 amizade com o Kai · flag `kai_promessa_1`
- *(primeiro)* **Kai** *(feliz)*: "Ha! Vamos ver." ⚙ +40 amizade com o Kai

---

## C1-05 — A Floresta Que Caiu do Céu

| | |
|---|---|
| ID | `cena_c1_05_folhalta` |
| Quando | subir a Folhalta pela primeira vez (andar 7) |
| Onde | andar 7, Folhalta |
| Quem | herói, Anciã Lothiel, Faelan, Eldrin |
| Música | `floresta_dia` com harpa |

🎬 O elevador de cesto chega ao topo das árvores. Dois arqueiros élficos apontam flechas ao herói.

- **Faelan** *(zangado)*: "Alto. Mais um da janela azul."
- 🎬 Uma voz calma atrás deles.
- **Anciã Lothiel** *(normal)*: "Baixem os arcos, filhos. Os da janela azul não escolheram vir. Tal como nós."
- 🎬 Os arcos baixam. Lothiel aproxima-se: cabelo branco até aos pés, olhos verdes muito velhos.
- **Lothiel** *(normal)*: "Há sete luas, a nossa floresta caiu do céu. Num momento estávamos em casa. No seguinte, aqui."
- **Lothiel** *(triste)*: "A torre engole mundos, Jogador. Árvore a árvore. Povo a povo."

▶ **"A torre engoliu a vossa casa?"**
▶ **"Também me engoliu a mim."**

- **Lothiel** *(normal)*: "Sim. E agora vivemos dentro dela, como pássaros numa gaiola muito grande."
- 🎬 Um elfo jovem e alegre aparece a correr.
- **Eldrin** *(feliz)*: "É um Jogador? Lá de baixo? Da cidade? Conheces uma elfa chamada Selene? Faz explosões?"
- **Lothiel** *(feliz, leve)*: "Eldrin. Deixa-o respirar."

⚙ Desbloqueia Folhalta. Missões R1_06, R1_07 e R1_08 disponíveis.
⚙ `[Sistema] Nova informação: os andares da torre são pedaços de outros mundos.`

---

## C1-06 — Símbolos Conhecidos

| | |
|---|---|
| ID | `cena_c1_06_simbolos` |
| Quando | entrar na Praça das Estátuas (andar 8) |
| Onde | andar 8, Ruínas Cobertas de Musgo |
| Quem | herói, Sistema |
| Música | `floresta_noite` |

🎥 A câmara mostra uma parede coberta de musgo. Por baixo, gravados na pedra: **os mesmos símbolos azuis da janela do Sistema**.
🎬 O herói aproxima-se. A janela azul abre-se sozinha e **treme** (efeito de falha de imagem, 1 s).

- `[Sistema] A ler… ▒▒▒▒ … erro.`
- `[Sistema] Ignora.`

🎬 A janela fecha-se de repente.

⚙ `[Sistema] Nova entrada no Diário: "Símbolos do Sistema nas ruínas".`

---

## C1-07 — O Reflexo

| | |
|---|---|
| ID | `cena_c1_07_reflexo` |
| Quando | chegar à margem do Lago da Névoa com nevoeiro (andar 9) |
| Onde | andar 9, Margem dos Juncos |
| Quem | herói |
| Música | `aurora` (versão calma) |

🎥 O nevoeiro abre-se um pouco. A água fica lisa como um espelho.
🎥 No reflexo **não** aparece o herói: aparece uma cidade com prédios altos, carros e semáforos — a cidade do mundo real.
🎬 Uma gota cai na água. O reflexo desfaz-se. Volta o nevoeiro.

- *(sem falas; só um som de cidade muito longe: buzinas, um sino de escola)*

⚙ Página de lore 9 mais fácil de encontrar (um fogo-fátuo aparece perto).

---

## C1-08 — A Voz no Caminho das Lanternas

| | |
|---|---|
| ID | `cena_c1_08_voz` |
| Quando | entrar no andar 10 |
| Onde | andar 10, Caminho das Lanternas |
| Quem | herói, voz da Árvore-Mãe |
| Música | `floresta_noite` (lenta) |

🎬 Folhas douradas caem. As lanternas de pedra estão apagadas.
- **Voz** *(sussurro, sem retrato)*: "…Jogador…"
- **Voz**: "…acende a luz… e vem…"
- `[Sistema] Acende as 8 lanternas para enfraquecer o guardião.` *(dica, só se ainda não as acendeste)*

---

## C1-09 — O Ent Ancião

| | |
|---|---|
| ID | `cena_c1_09_ent_antes` |
| Quando | entrar nas Raízes da Árvore-Mãe |
| Onde | andar 10, arena |
| Quem | herói, Ent Ancião, Árvore-Mãe (ao fundo) |
| Música | silêncio → `ent_anciao` |

🎥 Plano grande: a **Árvore-Mãe** ao fundo, gigantesca, meio seca. À frente dela, raízes enormes começam a mexer-se.
🎬 O **Ent Ancião** levanta-se do chão. Musgo cai-lhe da barba. Os olhos acendem-se a verde.

- **Ent Ancião** *(zangado, voz grave e lenta)*: "Mais… um… da… janela."
- **Ent Ancião**: "Vêm… sobem… e a torre… cresce."
- **Ent Ancião** *(zangado)*: "Não… deixarei… que a leves… também."

▶ **"Não quero levar nada!"**
▶ **(Preparar a arma.)**

- *(Não quero levar nada)* **Ent Ancião**: "Todos… dizem… isso."
- `[Sistema] Boss: Ent Ancião, Guardião da Floresta.`

⚙ Luta (ver `docs/BOSSES.md`).

## C1-10 — A Árvore-Mãe

| | |
|---|---|
| ID | `cena_c1_10_arvore_mae` |
| Quando | vencer o Ent Ancião |
| Onde | andar 10, arena |
| Quem | herói, Árvore-Mãe |
| Música | `tristeza` |

🎬 O Ent cai devagar e fica quieto, como uma árvore normal. Folhas douradas caem por todo o lado.
🎬 A Árvore-Mãe abre os olhos: uma cara antiga e gentil desenhada na casca.

- **Árvore-Mãe** *(triste, gentil)*: "Ele protegia-me. Era o meu filho mais velho."
- **Árvore-Mãe**: "Não te culpo. Ele confundiu-te… com o outro."

▶ **"Que outro?"**
▶ **"Desculpa."**

- **Árvore-Mãe**: "O primeiro. Há muito tempo, subiu por aqui um Jogador como tu. Era gentil. Falava comigo."
- **Árvore-Mãe**: "Depois chegou ao topo… e nunca mais desceu. E a torre começou a crescer."
- 🎬 A casca racha. A luz nos olhos dela fica mais fraca.
- **Árvore-Mãe** *(triste)*: "Estou a secar, pequeno. A torre bebe-me por dentro."
- 🎬 Uma semente dourada cai nas mãos do herói.
- **Árvore-Mãe**: "Leva-a. Planta-a num sítio onde haja gente."
- **Árvore-Mãe** *(muito baixo)*: "E… não sejas como o anterior."
- 🎬 Os olhos fecham-se. A árvore fica cinzenta. Uma última folha dourada cai.

- `[Sistema] Boss derrotado: Ent Ancião.`
- `[Sistema] Obtiveste: Raiz Ancestral.`
- `[Sistema] Obtiveste: Semente da Árvore-Mãe.`
- `[Sistema] Título obtido: Amigo da Floresta.`
- `[Sistema] Região 1 concluída. Andar 11 desbloqueado.`

⚙ A **Semente da Árvore-Mãe** pode ser plantada na **Praça de Ascendia** (com a Hana, cena de 10 ❤️ da Hana) ou na tua quinta.
Quando cresce (28 dias), dá Folhas Douradas e +5% de amizade ganha com toda a gente de Ascendia.
⚙ Missão **H_05** concluída.

---

## C1-11 — O Dia da Subida

| | |
|---|---|
| ID | `cena_c1_11_dia_da_subida` |
| Quando | voltar a Ascendia depois do Ent Ancião |
| Onde | Praça da Torre (enfeitada), de noite |
| Quem | herói, Governador Aldric, Lucien, Lyra, Kai, Hana, aldeões |
| Música | `dia_da_subida` |

🎥 A Praça está cheia de bandeiras, lanternas e bancas de comida. Pessoas a dançar.
🎬 Ao chegar, toda a gente aplaude.

- **Lyra** *(feliz)*: "Chegou o herói! Há anos que ninguém passava do andar 10! Anos!"
- 🎬 O Governador sobe ao palco com papéis a mais.
- **Aldric** *(nervoso)*: "Cidadãos de Ascendia. Hoje… hum… *(procura a página)* … hoje é um dia histórico."
- **Aldric** *(feliz)*: "Declaro aberto o **Dia da Subida**! E a partir de amanhã a Câmara aceita **pedidos de melhorias da cidade**!"
- 🎬 Ninguém aplaude a parte das melhorias. O Lucien salta para o palco.
- **Lucien** *(feliz)*: "Ó herói que sobe aos céus, com a espada e… e os pés! Venceu a árvore que andava — e ela nem sequer falava! Bem, falava. Mas pouco!"
- 🎬 Toda a gente ri. Música e fogo de artifício.
- **Hana** *(feliz)*: "Olá! Sou a Hana, da quinta. Ouvi dizer que trazes uma semente mágica. Passa lá amanhã! Tenho um terreno à tua espera."

⚙ Abre a **Quinta**, as **melhorias da cidade** e as **bênçãos**. +20 amizade com todos os NPCs presentes.

### No telhado
🎬 Se o herói subir as escadas da torre do relógio da Praça, encontra o Kai sentado no telhado a olhar para a torre.

- **Kai** *(normal)*: "Barulho demais lá em baixo."
- **Kai** *(sério)*: "A árvore disse-te alguma coisa, não disse? Vi na tua cara."

▶ **Contar o que a Árvore-Mãe disse.**
▶ **"Não foi nada."**

- *(contar)* **Kai** *(sério)*: "'O anterior'… Um Jogador que chegou ao topo e não desceu."
  **Kai** *(triste)*: "Se lá em cima não há saída… então para que é que estamos a subir?"
  🎬 Silêncio. Depois o Kai levanta-se.
  **Kai** *(decidido)*: "Não. Há saída. Tem de haver. A Yui está à espera."
  ⚙ flag `kai_sabe_do_anterior` · +40 amizade com o Kai
- *(não foi nada)* **Kai** *(normal)*: "Hm. Está bem. Guarda os teus segredos, número redondo."
- **Kai** *(feliz)*: "Corrida até ao andar 20?"
- 🎬 Fogo de artifício por trás deles. Fim do capítulo.

- `[Sistema] Capítulo 2: As Cavernas.`
