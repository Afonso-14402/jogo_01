# Progressão: status, classes, skills e rank

As fórmulas (HP, dano, XP) estão em `docs/SISTEMAS.md`. Aqui está **o que se ganha** ao subir: atributos,
Skill Única, **20 classes com 120 skills**, 36 skills de armas, 12 skills de vida e o rank.

---

## 1. Status

| Atributo | O que faz |
|---|---|
| **FOR** (Força) | dano corpo a corpo, carga |
| **AGI** (Agilidade) | velocidade de ataque e de movimento, Estamina |
| **DES** (Destreza) | dano com arco e besta, críticos, adaga e katana |
| **INT** (Inteligência) | dano mágico, MP |
| **VIT** (Vitalidade) | HP, DEF, RES |
| **SOR** (Sorte) | drops raros, ouro, críticos |

- Começam em 5; **5 pontos por nível**; nível máximo **100**; máximo de 300 por atributo.
- **Redistribuir pontos**: a Irmã Célia faz um ritual que devolve todos os pontos (5 000 ouro × nível / 10; grátis uma vez).

---

## 2. Skill Única (Cristal de Avaliação)

Sorteada pelo Cristal no início do jogo (missão H_02). Podes **voltar a sortear uma única vez**
na Madame Oriel (depois do andar 20, por 10 000 ouro).

| Skill Única | Efeito exato |
|---|---|
| **Olho do Sistema** | vês o nível, HP, fraquezas e drops dos inimigos; baús escondidos brilham a 10 m |
| **Sorte do Herói** | hipóteses de drop raro ×1,3; baús de prata 10% mais frequentes |
| **Mestre Artesão** | hipóteses de qualidade Boa e Excelente ×2; melhorias +5% de sucesso |
| **Coração de Dragão** | regeneras 1% do HP por segundo, também em combate |
| **Passo Fantasma** | podes esquivar **2 vezes seguidas** sem esperar; a 2.ª é grátis |
| **Língua Universal** | falas com alguns monstros (diálogos especiais, lojas de monstros, monstros que te deixam passar) |
| **Mão de Midas** | ouro de monstros e baús ×1,5 |
| **Aprendiz Rápido** | +20% XP e skills (armas e vida) sobem 50% mais depressa |
| **Domador Nato** | o animal de estimação tem +50% de stats e sobe de nível 2× mais depressa |
| **Bolsa Infinita** | mochila com 99 espaços desde o início; sem limite de peso para materiais |
| **Segunda Vida** | uma vez por andar, quando morres, levantas-te com 30% de vida |
| **Lâmina Espiritual** | a cada 4.º golpe sai uma onda de energia (×0,8) que atravessa inimigos |

---

## 3. Classes

Até ao **nível 10** és "Aventureiro" (sem classe). No nível 10 o **Mestre Gorvan** deixa-te escolher a classe;
nos níveis **40** e **70** evoluis. Podes usar **qualquer arma** com qualquer classe, mas cada classe tem armas
**preferidas** (+10% de dano com elas).

```
Espadachim ─┬─ Cavaleiro ────────── Paladino
            └─ Mestre de Lâminas ─── Santo da Espada
Arqueiro ───┬─ Atirador ─────────── Olho de Falcão
            └─ Ranger ───────────── Senhor da Floresta
Mago ───────┬─ Arquimago ────────── Sábio dos Elementos
            └─ Necromante ───────── Rei dos Mortos
Tanque ─────┬─ Guardião ─────────── Fortaleza Viva
            └─ Berserker ────────── Senhor da Guerra
```

**20 classes**, cada uma com **6 skills** = **120 skills**. Ao evoluir manténs as skills das classes anteriores
(no fim tens 18 skills de classe). Na barra cabem **6 skills** de cada vez (2 páginas no telemóvel).

| Classe base | Armas preferidas | Bónus da classe |
|---|---|---|
| Espadachim | espada, espada grande, katana, adaga | +10% ATQ corpo a corpo |
| Arqueiro | arco, besta | +10% alcance e dano à distância |
| Mago | cajado | +15% MP, +10% dano mágico |
| Tanque | martelo, machado, lança, manoplas | +15% HP, +10% DEF |

### 3.1 Espadachim (níveis 10–35)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 10 | Corte Rápido | ativa | 10 Est. | 4 s | avança 3 m com um corte ×1,5 |
| 15 | Postura de Guarda | ativa | 15 Est. | 12 s | durante 1 s bloqueia o próximo golpe à frente e contra-ataca ×2 |
| 20 | Maestria de Lâmina | passiva | — | — | +10% dano com espada, espada grande, katana e adaga |
| 25 | Lâmina de Vento | ativa | 20 MP | 8 s | onda de corte em linha de 6 m ×1,8 |
| 30 | Combo Fluido | passiva | — | — | +15% velocidade de ataque no 2.º e 3.º golpes do combo |
| 35 | Golpe Decisivo | ativa | 30 Est. | 20 s | golpe ×3,5; crítico garantido contra alvos com menos de 30% de vida |

### 3.2 Cavaleiro (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Investida do Cavaleiro | ativa | 25 Est. | 10 s | carga de 8 m que atordoa 1 s |
| 45 | Armadura de Honra | passiva | — | — | +15% DEF e +10% HP |
| 50 | Provocação | ativa | 10 MP | 15 s | os inimigos à volta atacam-te; +30% DEF durante 5 s |
| 55 | Lança-Lâmina | ativa | 30 MP | 12 s | estocada de energia em linha de 8 m ×2,5 |
| 60 | Juramento | passiva | — | — | quando um companheiro cai, +30% ATQ durante 10 s |
| 65 | Muralha de Aço | ativa | 40 MP | 30 s | 4 s invencível (parado); quem te bate leva 50% do dano |

### 3.3 Paladino (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Golpe Sagrado | ativa | 30 MP | 8 s | golpe ×3 de Luz |
| 75 | Aura de Cura | ativa | 50 MP | 30 s | tu e os companheiros curam 3% por segundo durante 10 s |
| 80 | Fé Inabalável | passiva | — | — | imune a Medo e Maldição |
| 85 | Julgamento | ativa | 60 MP | 20 s | coluna de luz em área (4 m) ×4 de Luz |
| 90 | Escudo Divino | ativa | 80 MP | 60 s | tu e os companheiros ficam invencíveis 3 s |
| 95 | Avatar da Luz | ativa | 100 MP | 120 s | 15 s: +50% ATQ, todos os golpes são de Luz e curas 1% por segundo |

### 3.4 Mestre de Lâminas (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Dança das Lâminas | ativa | 30 Est. | 10 s | 6 cortes rápidos à tua volta ×0,8 cada |
| 45 | Olho Afiado | passiva | — | — | +10% crítico e +20% dano crítico |
| 50 | Contra-Golpe | ativa | 15 Est. | 6 s | se fores atingido nos 0,5 s seguintes, esquivas e contra-atacas ×2,5 |
| 55 | Mil Cortes | ativa | 40 MP | 15 s | 1,5 s de cortes num alvo (12 golpes ×0,5) |
| 60 | Fluxo | passiva | — | — | cada crítico tira 1 s às recargas |
| 65 | Lâmina Fantasma | ativa | 50 MP | 25 s | uma cópia tua repete os teus ataques durante 8 s |

### 3.5 Santo da Espada (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Corte do Horizonte | ativa | 40 MP | 10 s | corte em linha de 15 m ×3 |
| 75 | Mente Vazia | passiva | — | — | esquiva perfeita (no último instante) abranda o tempo 2 s |
| 80 | Lâmina Celestial | ativa | 60 MP | 15 s | 8 espadas de luz caem numa área ×1 cada |
| 85 | Passo do Vento | passiva | — | — | +20% velocidade; 1 em cada 3 esquivas não gasta Estamina |
| 90 | Corte que Separa Mundos | ativa | 80 MP | 40 s | ×6 num alvo e ignora a DEF |
| 95 | Mestre de Todas as Lâminas | ativa | 100 MP | 120 s | 15 s: o combo tem 6 golpes e +50% de velocidade de ataque |

### 3.6 Arqueiro (níveis 10–35)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 10 | Tiro Duplo | ativa | 10 Est. | 4 s | 2 flechas seguidas |
| 15 | Rolar e Disparar | ativa | 15 Est. | 8 s | esquiva para trás e dispara ×1,5 |
| 20 | Olho de Águia | passiva | — | — | +20% alcance; +10% dano a mais de 8 m |
| 25 | Flecha Perfurante | ativa | 20 MP | 8 s | atravessa tudo em linha ×2 |
| 30 | Aljava Leve | passiva | — | — | +15% velocidade de tiro |
| 35 | Armadilha | ativa | 25 MP | 15 s | armadilha no chão que prende 3 s |

### 3.7 Atirador (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Tiro Certeiro | ativa | 30 Est. | 12 s | carrega 1,5 s e dispara ×4 com crítico garantido |
| 45 | Ponto Fraco | passiva | — | — | +25% dano crítico; uma marca mostra o ponto fraco dos bosses |
| 50 | Rajada | ativa | 30 MP | 12 s | 5 flechas em leque |
| 55 | Flecha Explosiva | ativa | 40 MP | 10 s | explosão de Fogo em área (3 m) ×2,5 |
| 60 | Concentração | passiva | — | — | parado durante 1 s: +20% dano |
| 65 | Chuva de Flechas | ativa | 50 MP | 20 s | área de 5 m durante 3 s (×0,6 por tique) |

### 3.8 Olho de Falcão (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Tiro do Falcão | ativa | 50 MP | 15 s | flecha que persegue e ressalta 4 vezes |
| 75 | Visão de Falcão | passiva | — | — | vês inimigos e baús através das paredes a 15 m |
| 80 | Flecha do Horizonte | ativa | 60 MP | 20 s | ×5 numa linha que atravessa o andar |
| 85 | Sem Falhar | passiva | — | — | os tiros carregados nunca falham e atravessam escudos |
| 90 | Céu de Flechas | ativa | 80 MP | 40 s | área enorme (10 m) durante 5 s |
| 95 | Flecha Estelar Perfeita | ativa | 100 MP | 90 s | ×10 num alvo; se o matar, recuperas todo o MP |

### 3.9 Ranger (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Companheiro Selvagem | passiva | — | — | o teu animal de estimação tem +50% de dano e de vida |
| 45 | Armadilha de Espinhos | ativa | 20 MP | 10 s | área com Sangrar |
| 50 | Camuflagem | ativa | 30 MP | 25 s | invisível 5 s; o próximo tiro faz ×3 |
| 55 | Flecha de Raízes | ativa | 30 MP | 10 s | prende os inimigos numa área 2 s |
| 60 | Instinto | passiva | — | — | +15% velocidade e esquiva quando os inimigos não te veem |
| 65 | Chamar a Matilha | ativa | 60 MP | 45 s | 3 lobos espirituais lutam contigo 15 s |

### 3.10 Senhor da Floresta (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Fúria da Natureza | ativa | 50 MP | 20 s | raízes e espinhos numa área de 6 m |
| 75 | Coração Verde | passiva | — | — | ao ar livre regeneras 1% do HP por segundo |
| 80 | Chamar o Ent | ativa | 80 MP | 60 s | um Ent aliado luta contigo 20 s |
| 85 | Mestre das Armadilhas | passiva | — | — | até 3 armadilhas ao mesmo tempo, +50% dano |
| 90 | Tempestade de Folhas | ativa | 70 MP | 30 s | tornado de folhas cortantes que persegue os inimigos |
| 95 | Espírito da Floresta | ativa | 100 MP | 120 s | 15 s: o teu animal fica gigante e todos os tiros prendem com raízes |

### 3.11 Mago (níveis 10–35)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 10 | Bola de Fogo | ativa | 10 MP | 3 s | ×1,8 de Fogo numa área pequena |
| 15 | Lança de Gelo | ativa | 12 MP | 4 s | ×1,6 de Gelo e Frio |
| 20 | Raio | ativa | 14 MP | 5 s | ×1,5 de Raio que salta para mais 2 inimigos |
| 25 | Barreira Mágica | ativa | 20 MP | 15 s | escudo que absorve 20% do teu HP máximo |
| 30 | Mente Clara | passiva | — | — | +20% MP e +20% regeneração de MP |
| 35 | Teletransporte | ativa | 15 MP | 6 s | a esquiva passa a ser um teletransporte de 5 m |

### 3.12 Arquimago (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Meteoro | ativa | 40 MP | 15 s | área de 4 m ×4 de Fogo (aviso 1 s) |
| 45 | Afinidade Elemental | passiva | — | — | +20% de dano contra fraquezas |
| 50 | Nevão | ativa | 40 MP | 15 s | área de 6 m com Frio durante 5 s |
| 55 | Tempestade | ativa | 50 MP | 20 s | raios numa área durante 5 s |
| 60 | Canalização | passiva | — | — | feitiços carregados custam −30% de MP |
| 65 | Feitiço Duplo | ativa | 30 MP | 30 s | os próximos 3 feitiços saem 2 vezes |

### 3.13 Sábio dos Elementos (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Fúria dos Elementos | ativa | 60 MP | 15 s | Fogo, Gelo e Raio ao mesmo tempo numa área |
| 75 | Equilíbrio | passiva | — | — | cada elemento diferente usado seguido dá +10% (máx. +30%) |
| 80 | Buraco Negro | ativa | 80 MP | 30 s | puxa e esmaga tudo num raio de 6 m |
| 85 | Mana Infinita | passiva | — | — | 10% de hipótese de um feitiço não gastar MP |
| 90 | Chuva de Estrelas | ativa | 100 MP | 45 s | 20 estrelas caem numa área enorme (×1,5 cada) |
| 95 | Magia Proibida | ativa | todo o MP | 180 s | dano igual a 5× o MP gasto, numa área enorme |

### 3.14 Necromante (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Levantar Esqueleto | ativa | 30 MP | 20 s | 1 esqueleto aliado (máx. 3) |
| 45 | Toque Sombrio | passiva | — | — | os feitiços têm 15% de Maldição e passam a ser de Sombra |
| 50 | Drenar Vida | ativa | 30 MP | 8 s | raio que rouba 50% do dano |
| 55 | Explosão de Ossos | ativa | 40 MP | 15 s | os teus esqueletos explodem (área) |
| 60 | Pacto | passiva | — | — | cada inimigo morto devolve 5% do MP |
| 65 | Nuvem de Peste | ativa | 50 MP | 20 s | Veneno e Maldição numa área durante 5 s |

### 3.15 Rei dos Mortos (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Exército dos Mortos | ativa | 70 MP | 45 s | 6 esqueletos durante 15 s |
| 75 | Coroa de Ossos | passiva | — | — | os teus esqueletos têm +50% de stats e duram mais |
| 80 | Ceifar Almas | ativa | 60 MP | 15 s | inimigos com menos de 20% de vida morrem logo (bosses não) |
| 85 | Imortal | passiva | — | — | 1 vez por andar, ao morrer, ficas 5 s com 1 HP e invencível |
| 90 | Dragão de Ossos | ativa | 100 MP | 90 s | um dragão de ossos aliado durante 20 s |
| 95 | Reino das Sombras | ativa | 120 MP | 180 s | 15 s: inimigos −30% ATQ e roubas 10% de vida |

### 3.16 Tanque (níveis 10–35)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 10 | Grito de Provocação | ativa | 10 Est. | 10 s | os inimigos à volta atacam-te |
| 15 | Pele Dura | passiva | — | — | +15% DEF |
| 20 | Empurrão | ativa | 15 Est. | 6 s | empurra tudo à frente 4 m |
| 25 | Aguentar | ativa | 20 Est. | 15 s | 3 s com −50% de dano recebido |
| 30 | Corpo de Ferro | passiva | — | — | +20% HP; não és empurrado |
| 35 | Terramoto | ativa | 30 Est. | 15 s | área de 4 m que atordoa 1 s |

### 3.17 Guardião (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Muralha | ativa | 30 MP | 20 s | bloqueias tudo à frente durante 4 s |
| 45 | Proteger | passiva | — | — | companheiros perto de ti levam −20% de dano |
| 50 | Contra-Ataque | passiva | — | — | 20% de devolver 50% do dano corpo a corpo |
| 55 | Cúpula | ativa | 50 MP | 30 s | cúpula de 4 m: −50% de dano para quem está dentro, 5 s |
| 60 | Inabalável | passiva | — | — | imune a Atordoado e Medo |
| 65 | Último Bastião | ativa | 60 MP | 60 s | 6 s sem conseguir descer de 1 HP |

### 3.18 Fortaleza Viva (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Pele de Pedra | ativa | 50 MP | 30 s | DEF ×2 durante 8 s |
| 75 | Gigante | passiva | — | — | +30% HP e um pouco maior (mais alcance) |
| 80 | Terramoto Maior | ativa | 70 MP | 20 s | área de 8 m que atordoa 2 s |
| 85 | Regeneração de Pedra | passiva | — | — | parado, regeneras 2% do HP por segundo |
| 90 | Fortaleza | ativa | 90 MP | 60 s | 8 s: tu e os companheiros com −70% de dano |
| 95 | Montanha | ativa | 120 MP | 180 s | 15 s: invencível, tamanho ×2, golpes ×2 |

### 3.19 Berserker (níveis 40–65)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 40 | Fúria | ativa | 10% do HP | 20 s | +40% ATQ e −20% DEF durante 10 s |
| 45 | Sede de Sangue | passiva | — | — | roubo de vida 5% |
| 50 | Golpe Selvagem | ativa | 30 Est. | 8 s | ×3, e mais dano quanto menos vida tiveres |
| 55 | Grito de Guerra | ativa | 30 MP | 25 s | Medo em área e +20% ATQ |
| 60 | Raiva | passiva | — | — | +1% ATQ por cada 2% de vida que te falta |
| 65 | Tornado de Aço | ativa | 50 Est. | 20 s | giras 3 s a acertar em tudo à volta |

### 3.20 Senhor da Guerra (níveis 70–95)
| Nível | Skill | Tipo | Custo | Recarga | Efeito |
|---|---|---|---|---|---|
| 70 | Lâmina Sangrenta | ativa | 10% do HP | 10 s | ×4 e Sangrar |
| 75 | Sem Dor | passiva | — | — | os 3 primeiros golpes que levas em cada luta fazem metade |
| 80 | Massacre | ativa | 60 Est. | 25 s | 6 golpes giratórios em área |
| 85 | Imparável | passiva | — | — | durante a Fúria és imune a estados |
| 90 | Grito do Senhor da Guerra | ativa | 60 MP | 60 s | companheiros +30% ATQ 15 s e Medo nos inimigos |
| 95 | Fúria Eterna | ativa | 25% do HP | 180 s | 20 s: +100% ATQ, roubo de vida 15% e não podes morrer |

---

## 4. Skills de armas (sobem com o uso)

Cada tipo de arma tem **"Manejo de …" do nível 1 ao 10**. Cada golpe que acerta dá 1 ponto; o nível N precisa de
`50 × N²` pontos (nível 10 ≈ 14 000 golpes no total). Cada nível dá **+2% de dano** com esse tipo e, nos níveis
3, 6 e 10, um **ataque especial** (usa-se com o botão de skill de arma):

| Arma | Nível 3 | Nível 6 | Nível 10 |
|---|---|---|---|
| Espada | **Corte Duplo** (15 Est., 5 s): 2 cortes ×1,3 | **Lâmina Giratória** (25 Est., 10 s): giro 360° ×2 | **Corte Celestial** (40 MP, 25 s): corte de luz em linha ×4 |
| Espada Grande | **Golpe da Terra** (20 Est., 8 s): onda em linha ×2 | **Furacão de Aço** (30 Est., 12 s): 3 giros | **Juízo Final** (50 MP, 30 s): salto e golpe em área ×5 |
| Adaga | **Passo Sombrio** (15 Est., 6 s): teletransporte para trás do alvo | **Mil Cortes** (25 Est., 10 s): 8 cortes rápidos | **Assassinato** (40 MP, 30 s): ×6 pelas costas |
| Katana | **Iai** (15 Est., 6 s): corte instantâneo ×2 | **Lua Crescente** (25 Est., 10 s): onda em arco | **Corte do Vazio** (40 MP, 25 s): ×5 que atravessa tudo |
| Machado | **Arremesso** (15 Est., 6 s): o machado vai e volta | **Fúria** (25 Est., 12 s): 4 golpes pesados | **Decapitar** (40 MP, 25 s): ×4; ×8 se o alvo tiver menos de 20% |
| Martelo | **Tremor** (20 Est., 8 s): área 3 m, atordoa | **Martelo Trovão** (30 MP, 12 s): raio + golpe | **Impacto Sísmico** (50 MP, 30 s): área 8 m ×4 |
| Lança | **Investida** (15 Est., 6 s): 6 m ×1,8 | **Chuva de Lanças** (30 MP, 12 s): lanças caem em linha | **Lança do Dragão** (50 MP, 30 s): salto e queda ×5 |
| Foice | **Ceifar** (20 Est., 8 s): círculo ×1,8 | **Dança da Morte** (30 Est., 12 s): 3 ceifadas, rouba vida | **Lua de Sangue** (50 MP, 30 s): área 6 m ×4, rouba 20% |
| Arco | **Tiro Duplo** (10 Est., 4 s) | **Chuva de Flechas** (30 MP, 12 s) | **Flecha Estelar** (50 MP, 30 s): ×6 em linha |
| Besta | **Virote Explosivo** (20 Est., 8 s): área ×2 | **Rajada** (30 Est., 12 s): 5 virotes | **Canhão** (50 MP, 30 s): virote gigante ×6 |
| Cajado | **Bola de Fogo / Lança de Gelo / Raio** (conforme a gema) | **Meteoro / Nevão / Tempestade** | **Magia Proibida** (feitiço enorme do elemento) |
| Manoplas | **Combo** (15 Est., 5 s): 8 socos | **Punho Ardente** (25 Est., 10 s): soco de fogo ×3 | **Mil Punhos** (40 MP, 25 s): 2 s de socos ×0,6 |

**36 skills de armas** no total.

---

## 5. Skills de vida (sobem com o uso, nível 1 a 50)

O nível N precisa de `20 × N^1,8` ações. Cada 10 níveis dá uma vantagem:

| Skill | Sobe ao… | Nv 10 | Nv 20 | Nv 30 | Nv 40 | Nv 50 |
|---|---|---|---|---|---|---|
| Mineração | partir minério | +1 minério 10% | gemas 2× | partir em 1 golpe | veios raros | minério ×2 sempre |
| Lenhador | cortar árvores | +1 madeira 10% | seiva/ninhos 2× | cortar em 1 golpe | madeiras raras | madeira ×2 sempre |
| Herbalismo | apanhar ervas | +1 erva 10% | ervas raras 2× | vês ervas a 20 m | plantas lendárias | ervas ×2 |
| Pesca | pescar | barra +10% | peixes raros 2× | lixo nunca | lendários 2× | barra +50% |
| Cozinha | cozinhar | Boa +10% | bónus +20% | duração ×1,5 | 2 pratos por receita | Excelente +20% |
| Ferraria | forjar e melhorar | melhorias +2% | Boa +10% | receitas secretas | melhorias +5% | Excelente +15% |
| Alquimia | fazer poções | +1 poção 10% | poções +20% | bombas ×2 | elixires | poções ×2 |
| Agricultura | colher | +1 colheita 10% | Boa +20% | cresce 1 dia mais depressa | sementes raras | colheita ×2 |
| Domar | cuidar de animais | felicidade +20% | animais +10% | animal sobe 2× | 2.º animal (quinta) | animais +30% |
| Joalharia | fazer joias | gemas: sair 2 10% | joias +10% | lapidar Brilhante | joias com 2 gemas | joias +30% |
| Engenharia | fazer engenhocas | engenhocas +10% | Gancho mais longo | bombas mecânicas | robô ajudante pequeno | engenhocas ×2 |
| Costura | fazer roupa e armaduras | +10% DEF | cosméticos novos | mochilas mais baratas | vestes +20% | capa própria |

---

## 6. Rank de aventureiro

**F → E → D → C → B → A → S → SS → SSS** (pontos e o que abre: `docs/SISTEMAS.md`, secção 16).
O rank aparece por baixo do teu nome e os NPCs comentam-no ("Rank A? Já és alguém!").
