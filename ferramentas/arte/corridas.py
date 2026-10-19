"""Corridas (docs/ATIVIDADES.md 4.5): os veículos, os obstáculos e o que se apanha, vistos de cima (um pouco
inclinados, como o resto do jogo), para o minijogo de corrida que desce pelo ecrã.

  - vagoneta (andar 11): a vagoneta de ferro com o herói lá dentro (andar: faíscas nas rodas; baixar: só se vê o
    capacete), a viga por cima dos carris e o cristal que brilha;
  - canoa (andar 24): remar à esquerda e à direita (2 quadros cada), a pedra no rio e o tronco a boiar;
  - lagarto (andar 37): o lagarto de corrida a correr (4 quadros) e a saltar, a pedra e o cacto;
  - trenó (andar 42): o trenó a deslizar, o pinheiro com neve e a bandeira.

Cada coisa é feita com as formas do motor (luz de cima à esquerda, contorno #2e222f), como os bonecos.
Saída: arte/minijogos/corrida_<nome>.png (tira horizontal de quadros)
Uso:   python3 ferramentas/arte/corridas.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, tira, previa_gif

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
PASTA = os.path.join(RAIZ, 'arte', 'minijogos')
PREVIA = '/tmp/claude-0/-home-user-jogo-01/1927e887-160f-5d34-9e8c-45231f72ddcb/scratchpad/corridas_previa.gif'

SPRITES = {}


def ponto(x, y, cor, z=60):
    return Parte({(x, y)}, None, z=z, cor=cor, separar=False)


def pontos(lista, cor, z=60):
    return Parte(set(lista), None, z=z, cor=cor, separar=False)


def cabeca_heroi(cx, cy, z, capacete=True, baixo=False):
    """O herói visto de cima e de trás: cabelo castanho e o capacete de mineiro (com a lanterna)."""
    P = []
    r = 3 if baixo else 4
    P.append(Parte(elipse(cx, cy, r + 0.5, r), 'cabelo', z=z))
    if capacete:
        P.append(Parte(elipse(cx, cy - 1, r + 0.5, r - 0.5), 'amarelo', z=z + 1))
        P.append(ponto(int(cx), int(cy - r), '#fbff86', z + 2))
    if not baixo:   # ombros e braços a agarrar a beira
        P.append(Parte(capsula(cx - 4, cy + 4, cx + 4, cy + 4, 2), 'vermelho', z=z - 1))
    return P


def vagoneta(fase, baixar=False):
    P = []
    # a caixa de ferro (mais larga em cima: está inclinada para nós)
    P.append(Parte(poligono([(6, 9), (26, 9), (25, 29), (7, 29)]), 'ferro', z=1, volume='cilindro_v'))
    P.append(Parte(retangulo(9, 11, 23, 21), 'preto', z=2, plano=True))
    P.append(Parte(retangulo(6, 22, 26, 23), 'cinza', z=3, plano=True))   # a faixa de rebites
    for x in (8, 12, 16, 20, 24):
        P.append(ponto(x, 22, '#c7dcd0', 4))
    # rodas e faíscas
    for x in (7, 23):
        P.append(Parte(retangulo(x, 26, x + 2, 30), 'preto', z=0, plano=True))
    if fase % 2 == 0:
        P.append(pontos([(5, 30), (4, 31), (28, 29)], '#f9c22b'))
    else:
        P.append(pontos([(27, 31), (28, 30), (4, 29)], '#fbff86'))
    P += cabeca_heroi(16, 13 if baixar else 12, 10, baixo=baixar)
    return desenhar(P, 32, 32)


def viga():
    P = [Parte(retangulo(0, 3, 95, 10), 'madeira', z=1, volume='cilindro_h')]
    for x in (8, 47, 87):
        P.append(Parte(retangulo(x - 1, 4, x + 1, 9), 'ferro', z=2, plano=True))
    P.append(Parte(retangulo(0, 11, 95, 12), 'preto', z=0, plano=True))   # a sombra
    return desenhar(P, 96, 16, contorno_fora=True)


def cristal(fase):
    P = [Parte(poligono([(8, 1), (12, 6), (8, 15), (4, 6)]), 'roxo', z=1)]
    P.append(Parte(poligono([(8, 3), (10, 6), (8, 11)]), 'lilas', z=2, plano=True))
    brilho = [(6, 4), (11, 9), (5, 10), (9, 3)][fase % 4]
    P.append(pontos([brilho, (brilho[0] + 1, brilho[1]), (brilho[0], brilho[1] + 1)], '#ffffff'))
    return desenhar(P, 16, 16)


def canoa(lado, fase, cor='madeira'):
    """lado: -1 rema à esquerda, 1 à direita; fase 0 = remo à frente, 1 = remo atrás (a puxar a água)."""
    P = [Parte(elipse(16, 17, 6, 14), cor, z=1, volume='cilindro_v')]
    P.append(Parte(elipse(16, 18, 4, 10), 'preto', z=2, plano=True))
    P += cabeca_heroi(16, 18, 10, capacete=False)
    y1, y2 = (10, 22) if fase == 0 else (16, 28)
    x = 16 + lado * 9
    P.append(Parte(capsula(16 + lado * 3, 20, x, (y1 + y2) // 2, 0.6), 'castanho', z=12))
    P.append(Parte(elipse(x, y2 - 2, 1.6, 3), 'castanho', z=12))
    if fase == 1:   # salpicos
        P.append(pontos([(x - 2, y2 + 1), (x + 2, y2 + 2), (x, y2 + 3)], '#8ff8e2'))
    return desenhar(P, 32, 32)


def pedra_rio(fase):
    P = [Parte(elipse(12, 10, 9, 6), 'cinza', z=1)]
    espuma = [(3, 13), (5, 15), (19, 14), (21, 12)] if fase == 0 else [(4, 14), (7, 16), (18, 15), (20, 13)]
    P.append(pontos(espuma, '#8ff8e2'))
    return desenhar(P, 24, 18)


def pedra():
    P = [Parte(elipse(12, 11, 9, 6), 'cinza', z=1)]
    P.append(Parte(elipse(16, 9, 4, 3), 'cinza', z=2))
    P.append(Parte(retangulo(3, 15, 21, 16), 'preto', z=0, plano=True))   # a sombra
    return desenhar(P, 24, 18)


def tronco(fase):
    P = [Parte(capsula(4, 8, 27, 8, 3.5), 'madeira', z=1, volume='cilindro_h')]
    P.append(Parte(elipse(27, 8, 2.5, 3), 'castanho', z=2, plano=True))
    P.append(pontos([(2 + fase, 12), (29 - fase, 12)], '#8ff8e2'))
    return desenhar(P, 32, 16)


def lagarto(fase, salto=False):
    P = []
    dy = -3 if salto else 0
    # cauda a abanar
    cx = [12, 16, 20, 16][fase % 4] if not salto else 16
    P.append(Parte(capsula(16, 23 + dy, cx, 32 + dy, 1.5), 'laranja', z=1))
    P.append(Parte(elipse(16, 17 + dy, 6, 8), 'laranja', z=2))
    P.append(Parte(capsula(16, 10 + dy, 16, 6 + dy, 2), 'laranja', z=3))   # o pescoço
    P.append(Parte(elipse(16, 4 + dy, 3.5, 3.5), 'laranja', z=4))
    P.append(pontos([(14, 3 + dy), (18, 3 + dy)], '#2e222f', 7))
    # patas abertas para os lados (alternadas)
    for k, (px, py) in enumerate([(8, 12), (24, 12), (8, 22), (24, 22)]):
        frente = (k + fase) % 2 == 0
        y = py + dy + (-2 if frente else 1)
        P.append(Parte(capsula(16 + (px - 16) // 3, py + dy, px, y, 1.2), 'laranja', z=1))
        P.append(pontos([(px - 1, y - 1), (px + 1, y - 1)], '#9e4539', 2))
    P.append(Parte(retangulo(11, 18 + dy, 21, 21 + dy), 'vermelho', z=8, plano=True))   # a sela
    P += cabeca_heroi(16, 16 + dy, 10, capacete=False)
    img = desenhar(P, 32, 34)
    return img


def cacto():
    P = [Parte(capsula(12, 4, 12, 22, 3), 'verde', z=1, volume='cilindro_v')]
    P.append(Parte(capsula(6, 9, 6, 15, 2), 'verde', z=0, volume='cilindro_v'))
    P.append(Parte(capsula(18, 7, 18, 13, 2), 'verde', z=0, volume='cilindro_v'))
    P.append(pontos([(11, 7), (13, 12), (11, 17), (6, 11), (18, 9)], '#cddf6c'))
    return desenhar(P, 24, 26)


def treno(fase):
    P = []
    for x in (9, 23):   # os patins
        P.append(Parte(capsula(x, 6, x, 30, 1), 'ferro', z=0, volume='cilindro_v'))
    P.append(Parte(retangulo(8, 9, 24, 27, 2), 'vermelho', z=1, volume='cilindro_v'))
    P += cabeca_heroi(16, 16, 10, capacete=False)
    P.append(Parte(retangulo(11, 19, 21, 21), 'azul', z=11, plano=True))   # o cachecol
    neve = [(6, 31), (26, 30), (5, 29)] if fase == 0 else [(27, 31), (6, 30), (25, 29)]
    P.append(pontos(neve, '#ffffff'))
    return desenhar(P, 32, 32)


def pinheiro_neve():
    P = []
    for k, (y, r) in enumerate([(24, 12), (17, 10), (10, 7)]):
        P.append(Parte(elipse(16, y, r, r * 0.6), 'verde_esc', z=k))
        P.append(Parte(elipse(14, y - 2, r * 0.7, r * 0.3), 'branco', z=k + 0.5, plano=True))
    P.append(Parte(retangulo(15, 28, 17, 31), 'madeira', z=-1, plano=True))
    return desenhar(P, 32, 32)


def bandeira(fase):
    P = [Parte(retangulo(4, 2, 5, 15), 'madeira', z=0, plano=True)]
    pano = [(6, 2), (14, 4 + fase), (6, 8)]
    P.append(Parte(poligono(pano), 'azul', z=1, plano=True))
    return desenhar(P, 16, 16)


def tudo():
    SPRITES['corrida_vagoneta'] = [vagoneta(f) for f in range(2)]
    SPRITES['corrida_vagoneta_baixar'] = [vagoneta(f, True) for f in range(2)]
    SPRITES['corrida_viga'] = [viga()]
    SPRITES['corrida_cristal'] = [cristal(f) for f in range(4)]
    SPRITES['corrida_canoa'] = [canoa(-1, 0), canoa(-1, 1), canoa(1, 0), canoa(1, 1)]
    SPRITES['corrida_canoa_rival'] = [canoa(-1, 0, 'verde'), canoa(-1, 1, 'verde'), canoa(1, 0, 'verde'), canoa(1, 1, 'verde')]
    SPRITES['corrida_pedra_rio'] = [pedra_rio(f) for f in range(2)]
    SPRITES['corrida_pedra'] = [pedra()]
    SPRITES['corrida_tronco'] = [tronco(f) for f in range(2)]
    SPRITES['corrida_lagarto'] = [lagarto(f) for f in range(4)]
    SPRITES['corrida_lagarto_salto'] = [lagarto(0, True)]
    SPRITES['corrida_cacto'] = [cacto()]
    SPRITES['corrida_treno'] = [treno(f) for f in range(2)]
    SPRITES['corrida_pinheiro'] = [pinheiro_neve()]
    SPRITES['corrida_bandeira'] = [bandeira(f) for f in range(2)]


def gravar():
    os.makedirs(PASTA, exist_ok=True)
    for nome, frames in SPRITES.items():
        tira(frames).save(os.path.join(PASTA, nome + '.png'))


def previas():
    linhas = [[SPRITES['corrida_vagoneta'], SPRITES['corrida_vagoneta_baixar'], SPRITES['corrida_canoa'],
               SPRITES['corrida_canoa_rival'], SPRITES['corrida_lagarto'], SPRITES['corrida_treno']]]
    previa_gif(linhas, PREVIA, escala=6, fundo=(62, 53, 70), ms=160)
    peq = [[SPRITES['corrida_cristal'], SPRITES['corrida_bandeira']]]
    previa_gif(peq, PREVIA.replace('.gif', '_coisas.gif'), escala=8, fundo=(62, 53, 70), ms=160)


if __name__ == '__main__':
    tudo()
    gravar()
    previas()
    print('ok', len(SPRITES), 'sprites em', os.path.normpath(PASTA))
