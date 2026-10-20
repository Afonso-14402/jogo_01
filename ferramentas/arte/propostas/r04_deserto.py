"""PROPOSTA de redesenho dos monstros, guardiões e bosses da Região 4 — Deserto (andares 31–40).

Só proposta (o utilizador ainda tem de aprovar): NÃO grava nada em arte/regioes/. Grava em
arte/propostas/monstros/r04_deserto/:
  - <id>_parado_lado.png  (4 quadros "parado", o mesmo tamanho de quadro do desenho antigo)
  - comparar.gif          (antes | depois, a mexer)
  - depois.gif            (só os novos)

Fichas: docs/regioes/r04_deserto.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (secções 7 e 8).
Estilo: docs/ARTE.md secção 0 e o exemplo ferramentas/arte/ent_anciao.py (partes com volume, textura,
olhos com brilho, pormenores). Só cores da Resurrect 64; luz de cima à esquerda; virados para a DIREITA.

Correr na raiz do repositório:  python3 ferramentas/arte/propostas/r04_deserto.py  [id ...]
"""
import json
import math
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
sys.path.insert(0, 'ferramentas/arte')

from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS, hexrgb  # noqa: E402,F401

OUT = '#2e222f'
RESURRECT_64 = '''2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334
e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73
91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff
45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0'''.split()
SAIDA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r04_deserto')
ANTIGO = os.path.join(RAIZ, 'arte', 'regioes', 'r04_deserto')

# ---------------- rampas desta região (escuro -> claro, só Resurrect 64) ----------------
AREIA = ['#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fdcbb0']
AREIA_ESC = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
ARENITO = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
CARAP = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
CARAP_ESC = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
NEGRO = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
OSSO = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']
OSSO_ESC = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
LIGA = ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff']
LIGA_ESC = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
OURO = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
OURO_ESC = ['#7a3045', '#9e4539', '#f79617', '#f9c22b', '#fbff86']
FERRO = ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
PELE = ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0']
PELE_ESC = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fca790']
LARANJA = ['#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fdcbb0']
VERMELHO = ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790']
VERM_ESC = ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a']
AZUL = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
AZUL_ESC = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
AGUA = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
TECIDO_AZ = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
ROXO = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']
COURO = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
COURO_ESC = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
PANO = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
PANO_AREIA = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']
CARNE = ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0']
MAD = ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']


# ---------------- ajudas ----------------

def px(P, pts, cor, z):
    """Píxeis soltos de uma só cor (marcas, olhos, brilhos)."""
    m = {(int(round(x)), int(round(y))) for x, y in pts}
    if m:
        P.append(Parte(m, None, z=z, separar=False, cor=cor))


def dentro(m, p):
    x, y = p
    return all((x + dx, y + dy) in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))


def lados(m):
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    return min(xs), min(ys), max(xs), max(ys)


def textura(P, m, escuro, claro, z, semente, d_esc=0.10, d_claro=0.06):
    """Pintas: escuras na metade de baixo/direita, claras em cima à esquerda (só no interior da forma)."""
    if not m:
        return
    rnd = random.Random(semente)
    x1, y1, x2, y2 = lados(m)
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    w, h = max(1, x2 - x1), max(1, y2 - y1)
    e, c = [], []
    for p in sorted(m):
        if not dentro(m, p):
            continue
        lado = (p[0] - cx) / w + (p[1] - cy) / h
        r = rnd.random()
        if escuro and lado > -0.15 and r < d_esc:
            e.append(p)
        elif claro and lado < -0.2 and r < d_claro:
            c.append(p)
    px(P, e, escuro, z)
    px(P, c, claro, z + 0.001)


def escamas(P, m, cor, z, passo=4, desvio=0, claro=None):
    """Escamas em 'u' (arco de 3 píxeis) numa grelha desfasada; um píxel claro por cima de algumas."""
    e, c = [], []
    for (x, y) in m:
        if y % passo != 0:
            continue
        xx = x + desvio + (passo // 2 if (y // passo) % 2 else 0)
        if xx % passo == 0:
            for q in ((x - 1, y), (x, y + 1), (x + 1, y)):
                if q in m and dentro(m, q):
                    e.append(q)
            if claro and (x, y - 1) in m and dentro(m, (x, y - 1)) and (x + y) % 3 == 0:
                c.append((x, y - 1))
    px(P, e, cor, z)
    if claro:
        px(P, c, claro, z + 0.001)


def listras(P, m, cor, z, f, borda=False):
    """Pinta os píxeis da forma m em que f(x, y) é verdadeiro (riscas, ligaduras, segmentos)."""
    px(P, [p for p in m if f(*p) and (borda or dentro(m, p))], cor, z)


def olho(P, x, y, iris, z, w=2, h=2, pupila=OUT, brilho='#ffffff'):
    """Olho com brilho: íris de cor, pupila escura à frente (direita) e um ponto branco em cima à esquerda."""
    pts = [(x + i, y + j) for i in range(w) for j in range(h)]
    px(P, pts, iris, z)
    if pupila and w >= 2:
        px(P, [(x + w - 1, y + h - 1)] if h > 1 else [(x + w - 1, y)], pupila, z + 0.01)
    if brilho:
        px(P, [(x, y)], brilho, z + 0.02)


def solto(img, pts):
    """Pinta píxeis por cima do desenho já feito, SEM contorno (poeira, faíscas, brilhos no ar)."""
    for (x, y, cor) in pts:
        x, y = int(round(x)), int(round(y))
        if 0 <= x < img.width and 0 <= y < img.height:
            img.putpixel((x, y), hexrgb(cor) + (255,))
    return img


def cadeia(pontos, raios):
    """Uma 'corrente' de elipses ao longo de pontos (caudas, vermes, pescoços)."""
    m = set()
    for (x, y), r in zip(pontos, raios):
        m |= elipse(x, y, r, r)
    return m


def curva(p0, p1, p2, n):
    """n pontos numa curva de Bézier quadrática."""
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        a, b, c = (1 - t) ** 2, 2 * (1 - t) * t, t * t
        out.append((a * p0[0] + b * p1[0] + c * p2[0], a * p0[1] + b * p1[1] + c * p2[1]))
    return out


# =====================================================================================
# MONSTROS (32×32, verme 48, colosso 128)
# =====================================================================================

def escorpiao(t):
    """Escorpião (32): carapaça castanho-arroxeada em placas, cauda de contas curvada sobre as costas, ferrão
    vermelho com uma gota de veneno verde, pinças grandes, olhos vermelhos. Parado: a cauda balança, as pinças
    abrem e fecham, respira."""
    P = []
    sw = (0, 1, 1, 0)[t]
    dy = (0, 0, 1, 1)[t]
    pin = (0, 1, 1, 0)[t]
    C = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
    CE = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
    # pernas de trás (escuras, finas)
    for x, pe in ((9, 5), (17, 15)):
        P.append(Parte(capsula(x, 23 + dy, x - 3, 22 + dy, 0.6) | capsula(x - 3, 22 + dy, pe, 29, 0.6), CE, z=0, separar=False))
    # abdómen em placas
    abd = elipse(12.5, 22 + dy, 7.0, 4.0)
    P.append(Parte(abd, C, z=2))
    for x in (9, 12, 15):
        px(P, [(x, y) for y in range(18 + dy, 22 + dy) if (x, y) in abd and dentro(abd, (x, y))], '#694f62', 2.1)
        px(P, [(x + 1, 19 + dy)], '#c7dcd0', 2.2)
    px(P, [(10, 24 + dy), (14, 24 + dy), (11, 20 + dy)], '#694f62', 2.2)               # pintas de sombra
    # cabeça
    cab = elipse(20.5, 22 + dy, 3.8, 3.3)
    P.append(Parte(cab, C, z=3))
    px(P, [(21, 20 + dy)], '#ea4f36', 3.2)
    px(P, [(22, 20 + dy)], '#fca790', 3.3)
    # pernas da frente
    for x, (kx, pe) in ((8, (6, 8)), (12, (11, 12)), (16, (17, 17)), (19, (21, 22))):
        P.append(Parte(capsula(x, 25 + dy, kx, 26 + dy, 0.6) | capsula(kx, 26 + dy, pe, 30, 0.6), CE, z=4, separar=False))
    # braço e pinça grande
    P.append(Parte(capsula(22, 23 + dy, 24, 22 + dy, 1.2), C, z=5))
    garra = elipse(26, 21.5 + dy, 2.8, 2.4)
    P.append(Parte(garra, C, z=6))
    P.append(Parte(capsula(27, 20 + dy, 30, 18 + dy - pin, 1.0), C, z=6.1))
    P.append(Parte(capsula(27, 23 + dy, 30, 22 + dy, 0.9), C, z=6.1))
    px(P, [(29, 18 + dy - pin)], '#c7dcd0', 6.2)
    # cauda: contas que sobem pelas costas
    cam = curva((7, 20 + dy), (0 + sw, 5), (12 + sw, 5 + dy), 6)
    for i, ((x, y), r) in enumerate(zip(cam, (2.4, 2.3, 2.2, 2.1, 2.0, 1.8))):
        P.append(Parte(elipse(x, y, r, r), C, z=1 + i * 0.01))
    # ferrão (bolbo vermelho + ponta) e gota de veneno
    fx, fy = cam[-1]
    P.append(Parte(elipse(fx + 2, fy + 1.5, 1.8, 1.6), VERMELHO, z=1.2))
    px(P, [(fx + 4, fy + 3)], '#2e222f', 1.3)
    img = desenhar(P, 32, 32)
    if t in (1, 2):
        solto(img, [(fx + 4, fy + 5 + (t - 1), '#91db69')])
    return img


def mumia(t):
    """Múmia (32): ligaduras bege enroladas na diagonal, um olho a brilhar amarelo numa fresta, braços esticados
    para a frente, uma ponta de ligadura solta a abanar atrás e pó a cair."""
    P = []
    dy = (0, 0, 1, 1)[t]
    ab = (0, 1, 1, 0)[t]
    # pernas
    P.append(Parte(capsula(13, 23, 12, 29, 1.7), LIGA_ESC, z=0, volume='cilindro_v'))
    P.append(Parte(capsula(17, 23, 18, 29, 1.8), LIGA, z=3, volume='cilindro_v'))
    # braço de trás (esticado)
    br2 = capsula(14, 17 + dy, 24, 16 + dy + ab, 1.5)
    P.append(Parte(br2, LIGA_ESC, z=1, volume='cilindro_h'))
    # tronco
    tr = poligono([(10, 15 + dy), (20, 15 + dy), (20.5, 24), (10, 24)])
    P.append(Parte(tr, LIGA, z=2, volume='cilindro_v'))
    listras(P, tr, '#966c6c', 2.1, lambda x, y: (y - (x // 4)) % 3 == 0)
    # cabeça
    hy = 9 + dy
    cab = elipse(15.5, hy, 6.4, 6.0)
    P.append(Parte(cab, LIGA, z=4))
    listras(P, cab, '#966c6c', 4.1, lambda x, y: (y + (x // 5)) % 3 == 0)
    # fresta escura com o olho
    px(P, [(x, hy) for x in range(15, 22)], '#45293f', 4.2)
    px(P, [(x, hy + 1) for x in range(16, 21)], '#45293f', 4.2)
    px(P, [(19, hy), (20, hy)], '#f9c22b', 4.3)
    px(P, [(19, hy)], '#fbff86', 4.4)
    px(P, [(20, hy + 1)], '#f79617', 4.3)
    px(P, [(18, hy + 4), (19, hy + 4), (20, hy + 4)], '#694f62', 4.2)      # boca
    # ponta da ligadura solta (atrás da cabeça, abana)
    w = (0, 1, 2, 1)[t]
    P.append(Parte(capsula(11, hy + 4, 7, hy + 6 + w, 1.1), LIGA, z=3.5))
    P.append(Parte(capsula(7, hy + 6 + w, 6 - w // 2, hy + 10, 1.0), LIGA, z=3.5))
    # braço da frente (esticado) com a ponta de ligadura a pender
    br = capsula(17, 18 + dy, 26, 17 + dy + ab, 1.6)
    P.append(Parte(br, LIGA, z=6, volume='cilindro_h'))
    listras(P, br, '#966c6c', 6.1, lambda x, y: x % 3 == 0)
    P.append(Parte(capsula(22, 19 + dy + ab, 22, 21 + dy + ab + (t % 2), 0.6), LIGA_ESC, z=5.9, separar=False))
    # escaravelho azul no peito (amuleto)
    px(P, [(15, 19 + dy), (16, 19 + dy)], '#4d9be6', 6.5)
    px(P, [(15, 18 + dy)], '#8fd3ff', 6.6)
    img = desenhar(P, 32, 32)
    # pó a cair
    for i, (x, y) in enumerate(((11, 25), (21, 27), (8, 20))):
        yy = y + (t + i) % 4
        solto(img, [(x, yy, '#ab947a')])
    return img


def chacal(t):
    """Chacal (32): magro, orelhas enormes, dorso escuro em sela, peito e focinho claros, olho âmbar,
    ponta da cauda negra. Parado: respira, a cauda abana, uma orelha mexe, língua de fora."""
    P = []
    dy = (0, 0, 1, 1)[t]
    cd = (0, 1, 2, 1)[t]
    PEL = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
    PEL_E = ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e']
    # pernas de trás (longe)
    P.append(Parte(capsula(9, 21 + dy, 8, 29, 1.0), PEL_E, z=0))
    P.append(Parte(capsula(20, 21 + dy, 20, 29, 1.0), PEL_E, z=0))
    # cauda
    cam = curva((6, 17 + dy), (2, 19), (2 + cd * 0.3, 25 - cd), 5)
    cau = cadeia(cam, (1.6, 1.8, 1.9, 1.8, 1.4))
    P.append(Parte(cau, PEL, z=1))
    px(P, [p for p in cau if p[1] >= cam[3][1]], '#45293f', 1.1)
    # corpo
    corpo = elipse(13.5, 18.5 + dy, 8.2, 4.4)
    P.append(Parte(corpo, PEL, z=2, volume='cilindro_h'))
    listras(P, corpo, '#694f62', 2.1, lambda x, y: y <= 16 + dy and 8 <= x <= 19)          # sela escura
    listras(P, corpo, '#45293f', 2.11, lambda x, y: y == 15 + dy and 10 <= x <= 17 and x % 2 == 0)
    listras(P, corpo, '#fbb954', 2.12, lambda x, y: y >= 21 + dy and x >= 15)                 # barriga clara
    # pescoço + cabeça
    P.append(Parte(capsula(19, 18 + dy, 22, 13 + dy, 2.6), PEL, z=3))
    cab = elipse(23, 12 + dy, 3.6, 3.0)
    P.append(Parte(cab, PEL, z=4))
    foc = capsula(24, 13 + dy, 29, 14 + dy, 1.5)
    P.append(Parte(foc, PEL, z=4.1))
    px(P, [(29, 13 + dy), (30, 13 + dy)], '#2e222f', 4.3)                                     # nariz
    px(P, [(x, 15 + dy) for x in range(24, 29)], '#fdcbb0', 4.2)                              # queixo claro
    px(P, [(26, 15 + dy), (27, 15 + dy)], '#2e222f', 4.25)                                    # boca
    if t in (1, 2):
        px(P, [(27, 16 + dy)], '#f04f78', 4.3)                                                # língua
    # orelhas (a de trás mexe)
    o2 = (0, 0, -1, 0)[t]
    P.append(Parte(poligono([(20, 11 + dy), (21 + o2, 3 + dy), (23, 10 + dy)]), PEL_E, z=3.5))
    P.append(Parte(poligono([(22, 11 + dy), (24, 3 + dy), (26, 10 + dy)]), PEL, z=4.5))
    px(P, [(24, 7 + dy), (24, 8 + dy), (23, 9 + dy)], '#f68181', 4.6)
    # olho âmbar com pupila e brilho
    px(P, [(24, 11 + dy), (25, 11 + dy)], '#f9c22b', 4.7)
    px(P, [(25, 11 + dy)], '#2e222f', 4.71)
    px(P, [(24, 10 + dy)], '#2e222f', 4.7)
    px(P, [(25, 10 + dy)], '#2e222f', 4.7)
    # pernas da frente
    P.append(Parte(capsula(11, 21 + dy, 11, 29, 1.1), PEL, z=5))
    P.append(Parte(capsula(18, 21 + dy, 19, 29, 1.1), PEL, z=5))
    px(P, [(10, 29), (11, 29), (18, 29), (19, 29)], '#45293f', 5.1)
    return desenhar(P, 32, 32)


def escaravelho(t):
    """Escaravelho de Fogo (~16 px num quadro de 32): carapaça vermelha com brasas, chifre, seis patas e
    chamas a dançar em cima das costas."""
    P = []
    dy = (0, 0, 1, 0)[t]
    ESC = ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a']
    # patas de trás
    for x0, x1 in ((10, 8), (14, 13), (18, 18)):
        P.append(Parte(capsula(x0, 25 + dy, x1 - 1, 27, 0.7) | capsula(x1 - 1, 27, x1 - 2, 29, 0.6), NEGRO, z=0, separar=False))
    # corpo: élitros (concha) + cabeça + chifre
    con = elipse(14, 22 + dy, 7.5, 5.2)
    con = {p for p in con if p[1] <= 26 + dy}
    P.append(Parte(con, ESC, z=2))
    listras(P, con, '#45293f', 2.1, lambda x, y: x == 14 and y > 18 + dy)               # risca entre élitros
    px(P, [(11, 21 + dy), (16, 23 + dy), (12, 24 + dy), (18, 20 + dy)], '#f79617', 2.2)  # brasas
    px(P, [(11, 20 + dy), (16, 22 + dy)], '#f9c22b', 2.3)
    cab = elipse(22, 24 + dy, 2.6, 2.3)
    P.append(Parte(cab, NEGRO, z=3))
    P.append(Parte(capsula(23, 23 + dy, 26, 19 + dy, 0.9), NEGRO, z=3.1))                # chifre
    px(P, [(23, 23 + dy)], '#f9c22b', 3.2)                                                # olho
    px(P, [(22, 23 + dy)], '#fbff86', 3.25)
    # patas da frente
    for x0, x1 in ((11, 9), (15, 15), (19, 21)):
        P.append(Parte(capsula(x0, 26 + dy, x1, 28, 0.7) | capsula(x1, 28, x1 + 1, 30, 0.6), NEGRO, z=4, separar=False))
    # chamas nas costas (mudam de forma)
    alt = ((4, 6, 3), (6, 3, 5), (3, 5, 6), (5, 4, 4))[t]
    for i, (x, h) in enumerate(zip((10, 14, 18), alt)):
        base = 18 + dy - (1 if i == 1 else 0)
        fl = poligono([(x - 2, base), (x + (t + i) % 2 - 0.5, base - h - 1), (x + 2, base)])
        P.append(Parte(fl, ['#b33831', '#ea4f36', '#f79617', '#f9c22b', '#fbff86'], z=1.5 + i * 0.01, separar=False))
    img = desenhar(P, 32, 32)
    sp = [(8, 9), (19, 7), (13, 6), (21, 11)]
    x, y = sp[t]
    solto(img, [(x, y, '#fbff86')])
    x, y = sp[(t + 2) % 4]
    solto(img, [(x, y + 2, '#f79617')])
    return img


def _espada_curva(P, x, y, comp, z, sobe=1.0, cor=None):
    """Cimitarra: punho em (x, y), lâmina curva para a frente e para cima, guarda dourada."""
    pts = curva((x + 1, y), (x + comp * 0.7, y - comp * 0.15 * sobe), (x + comp, y - comp * 0.75 * sobe), 6)
    lam = set()
    for i, (a, b) in enumerate(pts):
        lam |= elipse(a, b, 1.1 if i < 4 else 0.8, 1.1 if i < 4 else 0.8)
    P.append(Parte(lam, cor or FERRO, z=z, volume='cilindro_h'))
    px(P, [(int(a), int(b) - 1) for (a, b) in pts[1:4]], '#ffffff', z + 0.01)
    px(P, [(x, y - 1), (x, y), (x, y + 1)], '#f9c22b', z + 0.02)
    px(P, [(x - 1, y)], '#694f62', z + 0.02)


def esqueleto(t):
    """Esqueleto Guerreiro (32): crânio grande rachado com um brilho azul no olho, costelas, lenço vermelho
    rasgado ao pescoço, escudo redondo de bronze amolgado atrás e cimitarra à frente. Parado: a mandíbula
    bate, o brilho do olho pisca, o lenço abana."""
    P = []
    dy = (0, 0, 1, 1)[t]
    jaw = 1 if t == 2 else 0
    # pernas e braço de trás
    P.append(Parte(capsula(14, 23, 13, 29, 0.9), OSSO_ESC, z=0))
    P.append(Parte(capsula(14, 17 + dy, 11, 21 + dy, 0.9), OSSO_ESC, z=0))
    # escudo redondo (atrás, no braço de trás)
    esc = elipse(9.5, 20 + dy, 4.2, 4.8)
    P.append(Parte(esc, ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#fbb954'], z=1))
    anel = esc - elipse(9.5, 20 + dy, 3.0, 3.6)
    px(P, [p for p in anel if p[0] > 9], '#9e4539', 1.1)
    px(P, [(9, 19 + dy), (10, 19 + dy), (9, 20 + dy), (10, 20 + dy)], '#f9c22b', 1.2)         # umbo
    px(P, [(9, 19 + dy)], '#ffffff', 1.25)
    px(P, [(7, 17 + dy), (8, 18 + dy), (11, 23 + dy)], '#6e2727', 1.2)                        # amolgadelas
    # coluna, bacia, costelas
    P.append(Parte(capsula(15, 16 + dy, 15, 22, 0.8), OSSO, z=2))
    P.append(Parte(elipse(15.5, 22.5, 2.6, 1.6), OSSO, z=2.1))
    cost = elipse(16, 18 + dy, 3.4, 2.8)
    P.append(Parte(cost, OSSO, z=2.2))
    listras(P, cost, '#3e3546', 2.3, lambda x, y: (y - dy) % 2 == 1 and x != 15, borda=False)
    P.append(Parte(capsula(17, 23, 18, 29, 1.0), OSSO, z=3))
    px(P, [(17, 26), (18, 26)], '#c7dcd0', 3.1)                                                # joelho
    # crânio
    hy = 9 + dy
    cr = elipse(16, hy, 6.2, 5.6)
    P.append(Parte(cr, OSSO, z=5))
    queixo = retangulo(16, hy + 4 + jaw, 21, hy + 6 + jaw, canto=1)
    P.append(Parte(queixo, OSSO, z=4.9))
    px(P, [(x, hy + 4 + jaw) for x in range(17, 22) if x % 2 == 0], '#3e3546', 5.1)          # dentes de baixo
    px(P, [(x, hy + 4) for x in range(17, 22)], '#3e3546', 5.05)
    px(P, [(x, hy + 3) for x in range(17, 22) if x % 2 == 1], '#c7dcd0', 5.06)               # dentes de cima
    # órbita e brilho
    px(P, [(18, hy - 1), (19, hy - 1), (20, hy - 1), (18, hy), (19, hy), (20, hy), (19, hy + 1)], '#2e222f', 5.2)
    px(P, [(19, hy)], '#8fd3ff' if t != 3 else '#4d9be6', 5.3)
    px(P, [(21, hy + 2)], '#2e222f', 5.2)                                                      # nariz
    px(P, [(13, hy - 4), (14, hy - 3), (14, hy - 2), (13, hy - 1)], '#625565', 5.2)            # racha
    # lenço vermelho ao pescoço (ponta abana para trás)
    w = (0, 1, 1, 0)[t]
    P.append(Parte(capsula(13, 15 + dy, 18, 15 + dy, 1.2), VERMELHO, z=6))
    P.append(Parte(poligono([(13, 14 + dy), (9 - w, 16 + dy + w), (10, 18 + dy), (14, 16 + dy)]), VERMELHO, z=5.9))
    # braço da frente e cimitarra
    P.append(Parte(capsula(17, 17 + dy, 20, 20 + dy, 0.9), OSSO, z=7))
    P.append(Parte(capsula(20, 20 + dy, 22, 19 + dy, 0.9), OSSO, z=7))
    _espada_curva(P, 22, 19 + dy, 8, 8)
    return desenhar(P, 32, 32)


def _humano(P, dy, pele, roupa, calca, cinto, olho_y=0):
    """Corpo pequeno (estilo herói) virado para a direita: pernas, tronco, cabeça. Devolve (hx, hy)."""
    P.append(Parte(capsula(14, 23, 13, 28, 1.5), [calca[0]] + calca[:4], z=0, volume='cilindro_v'))
    P.append(Parte(capsula(18, 23, 19, 28, 1.6), calca, z=3, volume='cilindro_v'))
    px(P, [(12, 29), (13, 29), (14, 29)], '#45293f', 0.1)
    px(P, [(18, 29), (19, 29), (20, 29)], '#694f62', 3.1)
    tr = poligono([(11, 15 + dy), (20, 15 + dy), (21, 24), (11, 24)])
    P.append(Parte(tr, roupa, z=2, volume='cilindro_v'))
    P.append(Parte(retangulo(11, 21, 21, 22), cinto, z=2.2, plano=True))
    hx, hy = 16, 9 + dy
    P.append(Parte(elipse(hx, hy, 5.8, 5.4), pele, z=4, luz=0.15))
    return hx, hy


def bandido(t):
    """Bandido do Deserto (32): lenço cor de areia a tapar a cabeça e um pano vermelho na cara (só se veem os
    olhos), colete de couro, faixa vermelha, calças índigo e cimitarra. A ponta do lenço abana."""
    P = []
    dy = (0, 0, 1, 1)[t]
    w = (0, 1, 2, 1)[t]
    P.append(Parte(capsula(13, 17 + dy, 12, 21 + dy, 1.1), PELE_ESC, z=1))                     # braço de trás
    hx, hy = _humano(P, dy, PELE, ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], AZUL, VERMELHO)
    # camisa clara por baixo do colete
    px(P, [(x, y) for x in range(17, 20) for y in range(16 + dy, 21)], '#c7dcd0', 2.1)
    px(P, [(18, y) for y in range(17 + dy, 21)], '#9babb2', 2.11)
    # lenço na cabeça (turbante de pano) e cauda a abanar
    tur = {p for p in elipse(hx - 0.5, hy - 1, 6.6, 5.6) if p[1] <= hy - 2 or p[0] < hx - 1}
    P.append(Parte(tur, PANO_AREIA, z=5, separar=False))
    listras(P, tur, '#ab947a', 5.1, lambda x, y: (x + y) % 4 == 0)
    P.append(Parte(poligono([(hx - 5, hy), (hx - 10 - w, hy + 3 + w), (hx - 9 - w, hy + 6), (hx - 4, hy + 3)]), PANO_AREIA, z=4.5))
    # pano vermelho na cara
    masc = {p for p in elipse(hx + 1, hy + 3.5, 5.2, 3.0) if p[1] >= hy + 3}
    P.append(Parte(masc, VERMELHO, z=5.2, separar=False))
    px(P, [(hx + 4, hy + 5), (hx + 2, hy + 6)], '#6e2727', 5.3)
    # olho e sobrolho (a cara fica entre o lenço e o pano)
    if t != 3:
        px(P, [(hx + 3, hy), (hx + 3, hy + 1)], '#ffffff', 5.4)
        px(P, [(hx + 4, hy), (hx + 4, hy + 1)], '#2e222f', 5.5)
    else:
        px(P, [(hx + 3, hy + 1), (hx + 4, hy + 1)], '#2e222f', 5.5)
    # braço da frente e cimitarra
    P.append(Parte(capsula(18, 17 + dy, 21, 20 + dy, 1.2), PELE, z=7))
    _espada_curva(P, 22, 20 + dy, 8, 8)
    return desenhar(P, 32, 32)


def sultao(t):
    """Sultão Bandido Kasim (32): turbante dourado com joia vermelha e pena, bigode preto enorme, colete roxo,
    faixa dourada, capa vermelha a esvoaçar e DUAS cimitarras (uma em cada mão)."""
    P = []
    dy = (0, 0, 1, 1)[t]
    w = (0, 1, 2, 1)[t]
    # capa vermelha atrás
    P.append(Parte(poligono([(12, 14 + dy), (7 - w, 27), (11, 28), (14, 20)]), VERM_ESC, z=-1))
    # braço de trás com a segunda cimitarra (levantada atrás)
    P.append(Parte(capsula(13, 17 + dy, 10, 15 + dy, 1.1), PELE_ESC, z=0.5))
    pts = curva((9, 15 + dy), (5, 12 + dy), (5, 5 + dy), 5)
    lam = set()
    for a, b in pts:
        lam |= elipse(a, b, 0.9, 0.9)
    P.append(Parte(lam, ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'], z=0.4))
    px(P, [(9, 14 + dy), (10, 15 + dy)], '#f9c22b', 0.6)
    hx, hy = _humano(P, dy, PELE, ROXO, ['#45293f', '#753c54', '#a24b6f', '#cf657f', '#ed8099'], OURO)
    px(P, [(x, y) for x in range(17, 20) for y in range(16 + dy, 21)], '#f9c22b', 2.1)       # colete com bordo
    px(P, [(18, y) for y in range(16 + dy, 21)], '#fbff86', 2.11)
    # turbante dourado (mais alto) com joia e pena
    tur = elipse(hx - 0.5, hy - 3.5, 6.8, 4.6)
    tur = {p for p in tur if p[1] <= hy - 2}
    P.append(Parte(tur, OURO, z=5, separar=False))
    listras(P, tur, '#f79617', 5.1, lambda x, y: (y + x // 4) % 3 == 0)
    px(P, [(hx + 3, hy - 4), (hx + 4, hy - 4), (hx + 3, hy - 3), (hx + 4, hy - 3)], '#e83b3b', 5.2)
    px(P, [(hx + 3, hy - 4)], '#fca790', 5.3)
    P.append(Parte(capsula(hx + 3, hy - 6, hx + 1 - w // 2, hy - 11, 0.9), ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790'], z=4.8))
    # olho, sobrolho e bigode
    px(P, [(hx + 3, hy), (hx + 3, hy + 1)], '#ffffff', 5.4)
    px(P, [(hx + 4, hy), (hx + 4, hy + 1)], '#2e222f', 5.5)
    big = {(hx + 2, hy + 3), (hx + 3, hy + 3), (hx + 4, hy + 3), (hx + 5, hy + 3), (hx + 6, hy + 2),
           (hx + 1, hy + 4), (hx + 1, hy + 3)}
    px(P, big, '#2e222f', 5.6)
    px(P, [(hx + 3, hy + 3), (hx + 4, hy + 3)], '#45293f', 5.61)
    px(P, [(hx + 4, hy + 5), (hx + 3, hy + 5)], '#9e4539', 5.5)                                 # boca
    # braço da frente e cimitarra
    P.append(Parte(capsula(18, 17 + dy, 21, 20 + dy, 1.2), PELE, z=7))
    _espada_curva(P, 22, 20 + dy, 8, 8, cor=['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff'])
    img = desenhar(P, 32, 32)
    if t == 1:
        solto(img, [(hx + 2, hy - 7, '#ffffff')])
    return img


def espirito(t):
    """Espírito da Areia (32): redemoinho de areia a flutuar (largo em cima, fino em baixo), riscas que
    giram, uma cara zangada com olhos que brilham e pedrinhas a voar à volta."""
    P = []
    m = set()
    for i in range(8):
        cy = 5 + i * 2.9
        cx = 16 + math.sin(i * 0.9 + t * math.pi / 2) * 1.4
        rx = max(1.2, 9.5 - i * 1.15)
        m |= elipse(cx, cy, rx, 2.4)
    P.append(Parte(m, AREIA, z=1))
    listras(P, m, '#cd683d', 1.1, lambda x, y: (x + y * 2 + t * 3) % 9 in (0, 1) and y > 7)
    listras(P, m, '#fdcbb0', 1.11, lambda x, y: (x + y * 2 + t * 3) % 9 == 4 and x < 16)
    # cara (virada para a direita): sombra funda à volta dos olhos e da boca
    px(P, elipse(20.5, 10, 6, 3.2), '#cd683d', 1.9)
    pisca = t == 3
    for ex in (17, 22):
        px(P, [(ex - 1, 8), (ex, 8), (ex + 1, 8), (ex - 1, 9), (ex, 9), (ex + 1, 9), (ex - 1, 10), (ex, 10), (ex + 1, 10)], '#45293f', 2)
        if not pisca:
            px(P, [(ex, 9), (ex + 1, 9)], '#fbff86', 2.1)
            px(P, [(ex, 9)], '#ffffff', 2.2)
        else:
            px(P, [(ex - 1, 9), (ex, 9), (ex + 1, 9)], '#f9c22b', 2.1)
    px(P, [(15, 7), (16, 7), (17, 7)], '#7a3045', 2.05)                                        # sobrolhos zangados
    px(P, [(22, 7), (23, 7), (24, 6)], '#7a3045', 2.05)
    boca = elipse(20.5, 14.5, 2.6, 1.5 + (t % 2) * 0.6)
    px(P, boca, '#45293f', 2)
    px(P, [(19, 14), (21, 14)], '#fdcbb0', 2.1)                                               # dentinhos de pedra
    img = desenhar(P, 32, 32)
    # pedrinhas e grãos a girar à volta
    ang = t * math.pi / 2
    for k in range(3):
        a = ang + k * 2.1
        x = 16 + math.cos(a) * 12
        y = 13 + math.sin(a) * 4
        solto(img, [(x, y, '#ab947a' if math.sin(a) < 0 else '#fbb954')])
    for k in range(2):
        a = -ang * 1.3 + k * 3
        solto(img, [(16 + math.cos(a) * 7, 25 + math.sin(a) * 2, '#e6904e')])
    return img


def verme(t, N=48, colosso=False):
    """Verme da Areia (48) / Verme Colosso (128): sai de um monte de areia num arco, anéis de carne cor de
    laranja com espinhos escuros nas costas e barriga clara, boca redonda cheia de dentes virada para a frente
    e olhinhos pretos com brilho. O Colosso tem placas de armadura, cicatrizes e pedras cravadas.
    Parado: o corpo balança, a boca abre e fecha, cai areia do corpo."""
    P = []
    k = N / 48.0
    S = lambda v: v * k   # noqa: E731
    sw = (0, 1, 2, 1)[t] * k * 0.8
    boca = (0, 1, 2, 1)[t]
    CORPO = ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
    PLACA = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
    MONTE = ['#9e4539', '#e6904e', '#fbb954', '#fdcbb0', '#fdcbb0']
    # monte de areia à frente da base
    base = (S(15), S(45))
    n = 9 if not colosso else 11
    cam = curva(base, (S(4) + sw * 0.5, S(10)), (S(31) + sw, S(14)), n)
    rs = [S(7.2) - i * S(0.25) for i in range(n)]
    # anéis (do fundo para a cabeça)
    for i, ((x, y), r) in enumerate(zip(cam, rs)):
        anel = elipse(x, y, r, r)
        P.append(Parte(anel, CORPO, z=1 + i * 0.1))
        # barriga clara (lado de dentro do arco, em baixo à direita)
        listras(P, anel, '#fbb954', 1 + i * 0.1 + 0.01,
                lambda xx, yy, x=x, y=y, r=r: (xx - x) * 0.6 + (yy - y) > r * 0.45 and (xx - x) > -r * 0.2)
        # espinho nas costas (fora do arco: em cima à esquerda)
        if 0 < i < n - 1 and (i % 2 == 0 or colosso):
            nx, ny = cam[i + 1][0] - cam[i - 1][0], cam[i + 1][1] - cam[i - 1][1]
            ln = math.hypot(nx, ny) or 1
            ox, oy = ny / ln, -nx / ln          # normal para fora do arco
            if ox > 0:
                ox, oy = -ox, -oy
            bx, by = x + ox * r * 0.8, y + oy * r * 0.8
            tx, ty = x + ox * (r + S(3.4)), y + oy * (r + S(3.4))
            esp = poligono([(bx - oy * S(1.6), by + ox * S(1.6)), (tx, ty), (bx + oy * S(1.6), by - ox * S(1.6))])
            P.append(Parte(esp, PLACA, z=0.5 + i * 0.1, plano=True))
        if colosso and 0 < i < n - 1:
            # placa de armadura nas costas de cada anel
            pl = {p for p in elipse(x, y, r * 0.95, r * 0.95) if (p[0] - x) + (p[1] - y) < -r * 0.35}
            P.append(Parte(pl, PLACA, z=1 + i * 0.1 + 0.03))
            escamas(P, pl, '#2e222f', 1 + i * 0.1 + 0.04, passo=5, claro='#ab947a')
    # cabeça: a ponta do arco, com a boca virada para a direita
    hx, hy = cam[-1]
    hr = rs[-1] * 1.05
    cab = elipse(hx + S(1), hy, hr, hr)
    P.append(Parte(cab, CORPO, z=3))
    textura(P, cab, '#9e4539', '#fbb954', 3.01, 5, 0.08, 0.08)
    mx, my = hx + hr * 0.75 + S(1), hy + S(1)
    ab = S(3.2) + boca * S(0.7)
    gula = elipse(mx, my, S(2.6), ab)
    P.append(Parte(gula, ['#45293f', '#831c5d', '#c32454', '#f04f78', '#f68181'], z=3.2))
    px(P, elipse(mx + S(0.6), my, S(1.3), max(1, ab - S(1.4))), '#2e222f', 3.25)
    # anel de dentes à volta da boca
    nd = 7 if not colosso else 11
    dentes = []
    for j in range(nd):
        a = -math.pi / 2 + j * math.pi / (nd - 1)
        x0 = mx - S(0.3) + math.cos(a) * S(2.4)
        y0 = my + math.sin(a) * (ab - S(0.2))
        x1 = mx - S(0.3) + math.cos(a) * S(1.0)
        y1 = my + math.sin(a) * (ab - S(1.6))
        dentes.append(capsula(x0, y0, x1, y1, max(0.6, S(0.45))))
    P.append(Parte(set().union(*dentes), ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=3.3, separar=False))
    # olhinhos por cima da boca
    for j, (ex, ey) in enumerate(((hx + S(1.5), hy - hr * 0.55), (hx + S(4.2), hy - hr * 0.4))):
        q = max(1, int(round(S(1))))
        px(P, [(ex + a, ey + b) for a in range(q + 1) for b in range(q + 1)], '#2e222f', 3.4)
        px(P, [(ex, ey)], '#ffffff', 3.41)
    if colosso:
        # cicatrizes e pedras cravadas
        for (a, b, c, d) in ((-6, -3, 2, 3), (-3, 4, 4, 1)):
            px(P, [(hx + S(a) + i, hy + S(b) + (i * (S(d) - S(b))) / max(1, S(c))) for i in range(int(S(c)))], '#fca790', 3.5)
        for i in (3, 6, 8):
            x, y = cam[i]
            P.append(Parte(elipse(x + rs[i] * 0.2, y + rs[i] * 0.1, S(1.4), S(1.1)), ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'], z=1 + i * 0.1 + 0.05))
    # monte de areia (por cima da base)
    mm = {p for p in elipse(base[0] + S(4), S(48.5), S(17), S(6)) if p[1] <= N - 2}
    P.append(Parte(mm, MONTE, z=5))
    textura(P, mm, '#e6904e', '#ffffff', 5.01, 3, 0.12, 0.04)
    for (a, b) in ((S(6), S(45)), (S(27), S(46))):
        P.append(Parte(elipse(a, b, S(1.3), S(1)), ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff'], z=5.1))
    img = desenhar(P, N, N)
    # areia a escorrer do corpo
    sol = []
    for i, (x, y) in enumerate(cam[2:-1:2]):
        yy = y + rs[0] + ((t + i) % 4) * S(1.5)
        sol.append((x + S(2), yy, '#fbb954' if i % 2 else '#fdcbb0'))
    return solto(img, sol)


CRIATURAS = {
    'escorpiao': ('monstros', 32, escorpiao),
    'mumia': ('monstros', 32, mumia),
    'chacal': ('monstros', 32, chacal),
    'escaravelho_de_fogo': ('monstros', 32, escaravelho),
    'esqueleto_guerreiro': ('monstros', 32, esqueleto),
    'bandido_do_deserto': ('monstros', 32, bandido),
    'sultao_bandido_kasim': ('monstros', 32, sultao),
    'espirito_da_areia': ('monstros', 32, espirito),
    'verme_da_areia': ('monstros', 48, verme),
    'verme_colosso': ('monstros', 128, lambda t: verme(t, 128, True)),
}


# =====================================================================================
# gravar, comparar e GIFs
# =====================================================================================

def quadros(cid):
    _, n, f = CRIATURAS[cid]
    fr = [f(t) for t in range(4)]
    for q in fr:
        assert q.size == (n, n)
    return fr


def antigo(cid):
    pasta, n, _ = CRIATURAS[cid]
    im = Image.open(os.path.join(ANTIGO, pasta, f'{cid}_parado_lado.png')).convert('RGBA')
    h = im.height
    return [im.crop((i * h, 0, i * h + h, h)) for i in range(im.width // h)]


def escala(n):
    return 3 if n <= 32 else 2 if n <= 64 else 1


def nomes():
    d = {}

    def andar(x):
        if isinstance(x, dict):
            if 'id' in x and 'nome_pt' in x and x['id'] not in d:
                d[x['id']] = x['nome_pt']
            for v in x.values():
                andar(v)
        elif isinstance(x, list):
            for v in x:
                andar(v)
    for f in ('monstros.json', 'bosses.json', 'masmorras.json'):
        try:
            andar(json.load(open(os.path.join(RAIZ, 'dados', f), encoding='utf-8')))
        except (OSError, ValueError):
            pass
    return d


def ver(cid, caminho, k=None):
    """Imagem de verificação: antes (em cima) e depois (em baixo), os 4 quadros, ampliados."""
    a, d = antigo(cid), quadros(cid)
    n = d[0].width
    k = k or max(1, 256 // n)
    W = n * k * 4 + 5 * 8
    im = Image.new('RGB', (W, 2 * n * k + 24), (38, 43, 58))
    for j, fr in enumerate((a[:4], d)):
        for i, q in enumerate(fr):
            g = q.resize((n * k, n * k), Image.NEAREST)
            im.paste(g, (8 + i * (n * k + 8), 8 + j * (n * k + 8)), g)
    im.save(caminho)


def grelha(cids, com_antes, titulo, caminho):
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
    ft = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    nm = nomes()
    cel = []
    for c in cids:
        d = quadros(c)
        n = d[0].width
        k = escala(n)
        w = n * k * (2 if com_antes else 1) + (6 if com_antes else 0)
        cel.append((c, d, antigo(c), n, k, w, n * k))
    MAXW, M = 1200, 10
    linhas, lin, x = [], [], M
    for c in cel:
        if lin and x + c[5] + M > MAXW:
            linhas.append(lin)
            lin, x = [], M
        lin.append(c)
        x += c[5] + M
    if lin:
        linhas.append(lin)
    W = min(MAXW, max(sum(c[5] + M for c in l) + M for l in linhas))
    H = 34 + sum(max(c[6] for c in l) + 22 + M for l in linhas)
    imgs = []
    for f in range(8):
        im = Image.new('RGBA', (W, H), (0x26, 0x2b, 0x3a, 255))
        dr = ImageDraw.Draw(im)
        dr.text((M, 8), titulo, font=ft, fill=(232, 232, 232))
        y = 34
        for l in linhas:
            hl = max(c[6] for c in l)
            x = M
            for (cid, d, a, n, k, w, h) in l:
                yy = y + hl - h
                partes = ([a[f % len(a)], d[f % 4]] if com_antes else [d[f % 4]])
                for i, q in enumerate(partes):
                    g = q.resize((n * k, n * k), Image.NEAREST)
                    im.alpha_composite(g, (x + i * (n * k + 6), yy))
                if com_antes:
                    dr.line([(x + n * k + 2, yy + 2), (x + n * k + 2, yy + h - 2)], fill=(70, 76, 96), width=1)
                nome = nm.get(cid, cid)
                tw = dr.textlength(nome, font=fonte)
                dr.text((x + (w - tw) / 2, y + hl + 4), nome, font=fonte, fill=(220, 220, 220))
                x += w + M
            y += hl + 22 + M
        imgs.append(im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255))
    imgs[0].save(caminho, save_all=True, append_images=imgs[1:], duration=160, loop=0, disposal=1)


def paleta_ok(img):
    pal = {hexrgb('#' + c) for c in RESURRECT_64}
    fora = {c[:3] for _, c in img.getcolors(1 << 20) if c[3] and c[:3] not in pal}
    return fora


def main(ids):
    os.makedirs(SAIDA, exist_ok=True)
    todos = list(CRIATURAS)
    ids = ids or todos
    for cid in ids:
        fr = quadros(cid)
        w = fr[0].width
        tira = Image.new('RGBA', (w * 4, w), (0, 0, 0, 0))
        for i, q in enumerate(fr):
            tira.paste(q, (i * w, 0))
        fora = paleta_ok(tira)
        if fora:
            print('CORES FORA DA PALETA em', cid, fora)
        tira.save(os.path.join(SAIDA, f'{cid}_parado_lado.png'))
        print('ok', cid, tira.size)
    if set(ids) == set(todos):
        grelha(todos, True, 'Região 4 — Deserto — antes | depois', os.path.join(SAIDA, 'comparar.gif'))
        grelha(todos, False, 'Região 4 — Deserto — depois', os.path.join(SAIDA, 'depois.gif'))
        print('GIFs gravados em', SAIDA)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--ver':
        ver(sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1:])
