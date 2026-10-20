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
        a0, a1 = cam[max(0, i - 1)], cam[min(n - 1, i + 1)]
        nx, ny = a1[0] - a0[0], a1[1] - a0[1]
        ln = math.hypot(nx, ny) or 1
        ox, oy = ny / ln, -nx / ln          # normal para fora do arco (em cima / à esquerda)
        if ox + oy > 0:
            ox, oy = -ox, -oy
        anel = elipse(x, y, r, r)
        P.append(Parte(anel, CORPO, z=1 + i * 0.1))
        # barriga clara (lado de dentro do arco) e uma risca de sombra entre a barriga e as costas
        listras(P, anel, '#fbb954', 1 + i * 0.1 + 0.01,
                lambda xx, yy, x=x, y=y, r=r, ox=ox, oy=oy: -((xx + .5 - x) * ox + (yy + .5 - y) * oy) > r * 0.45)
        listras(P, anel, '#9e4539', 1 + i * 0.1 + 0.012,
                lambda xx, yy, x=x, y=y, r=r, ox=ox, oy=oy: 0.2 * r < -((xx + .5 - x) * ox + (yy + .5 - y) * oy) <= r * 0.45)
        # espinho nas costas
        if 0 < i < n - 1 and (i % 2 == 1 or colosso):
            bx, by = x + ox * r * 0.7, y + oy * r * 0.7
            tx, ty = x + ox * (r + S(4.5)) - oy * S(1.5), y + oy * (r + S(4.5)) + ox * S(1.5)
            esp = poligono([(bx - oy * S(2), by + ox * S(2)), (tx, ty), (bx + oy * S(2), by - ox * S(2))])
            P.append(Parte(esp, PLACA, z=0.5 + i * 0.1, plano=True))
        if colosso and 0 < i < n - 1:
            # placa de armadura nas costas de cada anel
            pl = {p for p in elipse(x, y, r * 0.95, r * 0.95) if (p[0] - x) + (p[1] - y) < -r * 0.35}
            P.append(Parte(pl, PLACA, z=1 + i * 0.1 + 0.03))
            escamas(P, pl, '#2e222f', 1 + i * 0.1 + 0.04, passo=5, claro='#ab947a')
    # cabeça: a ponta do arco, com a boca virada para a direita
    hx, hy = cam[-1]
    hr = rs[-1] * (1.2 if not colosso else 1.35)
    cab = elipse(hx + S(1), hy, hr, hr)
    P.append(Parte(cab, CORPO, z=3))
    textura(P, cab, '#9e4539', '#fbb954', 3.01, 5, 0.05, 0.04)
    if colosso:
        pl = {p for p in cab if (p[0] - hx) * 0.3 + (p[1] - hy) < -hr * 0.3 and p[0] < hx + hr * 0.5}
        P.append(Parte(pl, PLACA, z=3.02))
        escamas(P, pl, '#2e222f', 3.03, passo=5, claro='#ab947a')
    # boca redonda de lampreia virada para a frente: lábio rosa, garganta escura e dentes em anel
    mx, my = hx + hr * 0.8 + S(1), hy + S(0.5)
    ry = S(4.0) + boca * S(0.5)
    rx = ry * 0.55
    labio = elipse(mx, my, rx, ry)
    P.append(Parte(labio, ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'], z=3.2))
    gar = elipse(mx + S(0.4), my, max(1.0, rx - S(1.0)), max(1.0, ry - S(1.1)))
    px(P, gar, '#45293f', 3.25)
    px(P, elipse(mx + S(0.6), my, max(0.8, rx - S(2.0)), max(0.8, ry - S(2.4))), '#2e222f', 3.26)
    nd = 8 if not colosso else 12
    dentes = set()
    gx1, gy1, gx2, gy2 = lados(gar)
    for j in range(nd):
        an = j * 2 * math.pi / nd
        da = math.pi / nd * 0.6
        rxi, ryi = max(1.0, rx - S(1.0)), max(1.0, ry - S(1.1))
        def pt(a_, f):
            return (mx + S(0.4) + math.cos(a_) * rxi * f, my + math.sin(a_) * ryi * f)
        if colosso:
            dentes |= poligono([pt(an - da, 1.05), pt(an, 0.45), pt(an + da, 1.05)])
        else:
            x_, y_ = pt(an, 0.85)
            dentes.add((int(x_), int(y_)))
    dentes &= gar
    P.append(Parte(dentes, ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=3.3, separar=False, plano=True))
    # olhinhos por cima da boca
    ojos = ((hx + S(1), hy - hr * 0.6), (hx + S(4), hy - hr * 0.62)) if not colosso else \
        ((hx - S(0.5), hy - hr * 0.12), (hx + S(2.5), hy - hr * 0.2))
    for j, (ex, ey) in enumerate(ojos):
        q = max(1, int(round(S(1.2))))
        px(P, [(ex + a, ey + b) for a in range(q + 1) for b in range(q + 1)], '#2e222f', 3.4)
        if colosso:
            px(P, [(ex + a, ey + b) for a in range(q) for b in range(q)], '#f9c22b', 3.405)
        px(P, [(ex, ey)], '#ffffff', 3.41)
    if colosso:
        # cicatrizes e pedras cravadas
        for (a, b, c, d) in ((-6, -3, 2, 3), (-3, 4, 4, 1)):
            px(P, [(hx + S(a) + i, hy + S(b) + (i * (S(d) - S(b))) / max(1, S(c))) for i in range(int(S(c)))], '#fca790', 3.5)
        for i in (3, 6, 8):
            x, y = cam[i]
            P.append(Parte(elipse(x + rs[i] * 0.2, y + rs[i] * 0.1, S(1.4), S(1.1)), ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'], z=1 + i * 0.1 + 0.05))
    # monte de areia (por cima da base)
    mm = {p for p in elipse(base[0] + S(3), S(49), S(16), S(8)) if p[1] <= N - 2}
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


# =====================================================================================
# GUARDIÕES
# =====================================================================================

def _espinho(P, bx, by, ang, comp, larg, rampa, z, ponta=None):
    """Espinho triangular: base em (bx, by), aponta no ângulo ang (graus; 0 = direita, -90 = cima)."""
    a = math.radians(ang)
    dx, dy = math.cos(a), math.sin(a)
    pts = [(bx - dy * larg, by + dx * larg), (bx + dx * comp, by + dy * comp), (bx + dy * larg, by - dx * larg)]
    P.append(Parte(poligono(pts), rampa, z=z, plano=True))
    if ponta:
        px(P, [(bx + dx * (comp - 1), by + dy * (comp - 1))], ponta, z + 0.01)


def lagarto(t):
    """Lagarto-Duna Gigante (64): lagarto cor de areia, baixo e comprido, cheio de espinhos (costas, cauda e
    uma coroa de chifres na nuca), faixas cor de tijolo, escamas, barriga clara, olho amarelo de pupila em
    fenda, garras brancas. Parado: respira, a garganta incha, a língua bifurcada sai, a cauda mexe."""
    P = []
    dy = (0, 0, 1, 1)[t]
    cd = (0, 1, 2, 1)[t]
    PL = ['#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fdcbb0']
    PLE = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
    ESP = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
    # patas do lado de lá
    P.append(Parte(capsula(21, 46 + dy, 16, 52, 2.8) | capsula(16, 52, 15, 60, 2.2), PLE, z=0))
    P.append(Parte(capsula(39, 46 + dy, 45, 51, 2.8) | capsula(45, 51, 46, 60, 2.2), PLE, z=0))
    # cauda (afina para a esquerda)
    cam = curva((20, 44 + dy), (7, 45), (1, 51 - cd), 9)
    cau = cadeia(cam, [6.5 - i * 0.65 for i in range(9)])
    P.append(Parte(cau, PL, z=1, volume='cilindro_h'))
    listras(P, cau, '#cd683d', 1.01, lambda x, y: (x // 4) % 2 == 0)
    for i in (1, 3, 5):
        x, y = cam[i]
        _espinho(P, x, y - (6.5 - i * 0.65) * 0.7, -105, 6 - i * 0.6, 1.8, ESP, 0.9, ponta='#c7dcd0')
    # corpo
    corpo = elipse(30, 43 + dy, 15, 9)
    P.append(Parte(corpo, PL, z=2, volume='cilindro_h'))
    listras(P, corpo, '#cd683d', 2.01, lambda x, y: (x // 5) % 2 == 0 and y < 44 + dy)        # faixas
    listras(P, corpo, '#fdcbb0', 2.02, lambda x, y: y >= 49 + dy and 20 < x < 42)              # barriga clara
    escamas(P, corpo, '#9e4539', 2.03, passo=5, claro='#fdcbb0')
    # espinhos das costas (alternam tamanho)
    for i, x in enumerate(range(18, 44, 4)):
        top = 43 + dy - math.sqrt(max(0, 1 - ((x - 30) / 15) ** 2)) * 9
        _espinho(P, x, top + 2, -95 + (x - 30) * 1.2, 11 if i % 2 else 8, 2.4, ESP, 1.5, ponta='#c7dcd0')
    # cabeça: crânio + focinho comprido
    hy = 37 + dy
    gar = elipse(47, hy + 7, 5.5, 3.6 + (t in (1, 2)) * 0.9)                                     # garganta
    P.append(Parte(gar, PL, z=3))
    listras(P, gar, '#e6904e', 3.01, lambda x, y: y % 2 == 0)
    cab = elipse(49, hy + 2, 7.5, 6) | capsula(51, hy + 3, 60, hy + 4, 3.5)
    P.append(Parte(cab, PL, z=4))
    escamas(P, cab, '#cd683d', 4.01, passo=3)
    px(P, [(x, hy + 6) for x in range(52, 61)], '#7a3045', 4.02)                                 # boca
    px(P, [(53, hy + 7), (56, hy + 7)], '#cd683d', 4.021)
    px(P, [(60, hy + 2)], '#45293f', 4.03)                                                       # narina
    # coroa de chifres na nuca
    for (bx, by, ang, c) in ((43, hy - 1, -160, 9), (45, hy - 3, -135, 10), (48, hy - 4, -110, 8)):
        _espinho(P, bx, by, ang, c, 2.0, ESP, 3.9, ponta='#c7dcd0')
    # olho amarelo de pupila em fenda e crista de sobrolho
    ex, ey = 51, hy
    px(P, [(ex + i, ey + j) for i in range(-1, 3) for j in range(-1, 3)], '#2e222f', 4.1)
    if t != 3:
        px(P, [(ex, ey), (ex + 1, ey), (ex, ey + 1)], '#f9c22b', 4.2)
        px(P, [(ex + 1, ey + 1)], '#2e222f', 4.21)
        px(P, [(ex, ey)], '#fbff86', 4.22)
    else:
        px(P, [(ex, ey + 1), (ex + 1, ey + 1)], '#9e4539', 4.2)
    P.append(Parte(capsula(48, ey - 2, 55, ey - 2, 1.3), PL, z=4.3))
    # língua bifurcada
    if t in (1, 2):
        L = 1 if t == 1 else 2
        px(P, [(61 + i, hy + 5) for i in range(L)] + [(61 + L, hy + 4), (61 + L, hy + 6)], '#f04f78', 4.4)
    # patas do lado de cá (cotovelo para fora) com garras
    for (o, j, pe) in (((24, 48), (19, 53), (19, 60)), ((38, 48), (43, 53), (43, 60))):
        P.append(Parte(capsula(*o, *j, 3.4) | capsula(*j, *pe, 2.5), PL, z=5))
        px(P, [(pe[0] - 2, 62), (pe[0] + 1, 62), (pe[0] + 3, 62)], '#c7dcd0', 5.1)
    return desenhar(P, 64, 64)



def _riscas_h(P, m, cores, z, alt=2, desvio=0):
    """Riscas horizontais alternadas (ex.: o lenço nemes azul e dourado)."""
    for (x, y) in m:
        i = ((y + desvio) // alt) % len(cores)
        if cores[i]:
            px(P, [(x, y)], cores[i], z)


def esfinge(t):
    """Esfinge Menor (64): leão de arenito com cara de pessoa, lenço nemes às riscas azuis e douradas com
    uma cobra de ouro na testa, barba entrançada, olhos pintados que brilham, asas de pedra dobradas nas
    costas, rachas e uma cauda com borla. Parado: respira, a cauda abana, as asas mexem, os olhos brilham."""
    P = []
    dy = (0, 0, 1, 1)[t]
    PED = ['#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fdcbb0']
    PED_E = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
    CARA = ['#cd683d', '#e6904e', '#fbb954', '#fdcbb0', '#ffffff']
    # patas do lado de lá
    P.append(Parte(capsula(16, 46, 13, 60, 3), PED_E, z=0))
    P.append(Parte(capsula(39, 46, 41, 60, 3), PED_E, z=0))
    # cauda com borla
    w = (0, 1, 2, 1)[t]
    cam = curva((12, 42 + dy), (3, 44), (5 + w, 31), 6)
    P.append(Parte(cadeia(cam, [1.5] * 6), PED, z=0.5))
    P.append(Parte(elipse(cam[-1][0], cam[-1][1] - 1, 2.6, 3), ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], z=0.6))
    # corpo de leão
    corpo = elipse(27, 44 + dy, 16, 8.5)
    P.append(Parte(corpo, PED, z=2, volume='cilindro_h'))
    anca = elipse(16, 46 + dy, 7, 8)
    P.append(Parte(anca, PED, z=2.1))
    listras(P, corpo, '#fdcbb0', 2.2, lambda x, y: y >= 49 + dy and 22 < x < 38)
    # rachas na pedra
    px(P, [(22, 41 + dy), (23, 42 + dy), (23, 43 + dy), (24, 44 + dy), (31, 47 + dy), (32, 48 + dy), (32, 49 + dy)], '#7a3045', 2.3)
    px(P, [(15, 43 + dy), (14, 44 + dy), (14, 45 + dy)], '#7a3045', 2.3)
    textura(P, corpo, '#cd683d', '#fdcbb0', 2.25, 9, 0.05, 0.03)
    # asa de pedra dobrada (penas em camadas)
    lv = (0, 1, 1, 0)[t]
    asa = poligono([(34, 36 + dy), (24, 31 + dy - lv), (12, 30 + dy - lv * 2), (8, 33 + dy - lv), (16, 38 + dy), (30, 41 + dy)])
    P.append(Parte(asa, PED, z=3))
    for i, (x0, y0) in enumerate(((12, 33), (17, 35), (22, 37))):
        px(P, [(x0 + j, y0 + dy + (j // 3)) for j in range(10 - i * 2)], '#9e4539', 3.1)
    px(P, [(x, 31 + dy - lv) for x in range(14, 26, 2)], '#fdcbb0', 3.1)
    # patas do lado de cá (patas grandes com dedos)
    for (x0, x1) in ((19, 18), (42, 44)):
        P.append(Parte(capsula(x0, 47 + dy, x1, 59, 3.4), PED, z=4, volume='cilindro_v'))
        pe = elipse(x1 + 1.5, 59.5, 4, 2.2)
        P.append(Parte(pe, PED, z=4.1))
        px(P, [(x1 + 1, 60), (x1 + 3, 60)], '#9e4539', 4.2)
    # peito e cabeça
    P.append(Parte(elipse(42, 41 + dy, 6, 7), PED, z=4.5))
    hx, hy = 45, 28 + dy
    # nemes: toucado às riscas (tampa o alto da cabeça e cai atrás, até aos ombros)
    nem = poligono([(hx - 5, hy - 9), (hx + 6, hy - 11), (hx + 11, hy - 6), (hx + 10, hy - 4), (hx + 2, hy - 3),
                    (hx + 1, hy + 2), (hx, hy + 13), (hx - 9, hy + 13), (hx - 9, hy - 3)])
    P.append(Parte(nem, TECIDO_AZ, z=5))
    _riscas_h(P, nem, ['#4d65b4', '#f9c22b'], 5.01, alt=2)
    px(P, [(x, y) for (x, y) in nem if not dentro(nem, (x, y)) and y < hy - 2], '#f79617', 5.02)
    # cara humana de pedra (grande, à frente do toucado)
    fx = hx + 7
    cara = elipse(fx, hy + 1, 5.6, 6.6)
    P.append(Parte(cara, CARA, z=6))
    px(P, [(fx + 5, hy), (fx + 6, hy + 1), (fx + 6, hy + 2), (fx + 5, hy + 3)], '#cd683d', 6.1)        # nariz
    px(P, [(fx + 2, hy + 5), (fx + 3, hy + 5), (fx + 4, hy + 5)], '#9e4539', 6.1)                       # boca
    px(P, [(fx - 3, hy + 2), (fx - 4, hy + 3)], '#cd683d', 6.1)                                         # orelha
    # olho pintado (risco preto para trás) com íris que brilha
    gl = ('#4d9be6', '#8fd3ff', '#8fd3ff', '#4d9be6')[t]
    ox = fx + 1
    px(P, [(ox - 1, hy - 1), (ox, hy - 1), (ox + 1, hy - 1), (ox + 2, hy - 1), (ox + 3, hy - 1), (ox - 2, hy), (ox - 3, hy),
           (ox + 3, hy), (ox, hy + 2), (ox + 1, hy + 2), (ox + 2, hy + 2)], '#2e222f', 6.2)
    px(P, [(ox, hy), (ox + 1, hy), (ox + 2, hy), (ox, hy + 1), (ox + 1, hy + 1), (ox + 2, hy + 1)], '#ffffff', 6.25)
    px(P, [(ox + 1, hy), (ox + 2, hy), (ox + 1, hy + 1), (ox + 2, hy + 1)], gl, 6.3)
    px(P, [(ox + 2, hy + 1)], '#323353', 6.305)
    px(P, [(ox + 1, hy)], '#ffffff', 6.31)
    px(P, [(ox - 1, hy - 3), (ox, hy - 3), (ox + 1, hy - 3), (ox + 2, hy - 3), (ox + 3, hy - 3)], '#9e4539', 6.2)  # sobrolho
    # faixa da testa e cobra de ouro (uraeus)
    P.append(Parte(capsula(hx + 1, hy - 4, fx + 4, hy - 4, 1.0), OURO, z=6.5))
    P.append(Parte(capsula(fx + 4, hy - 4, fx + 5, hy - 9, 1.0), OURO, z=6.6))
    px(P, [(fx + 6, hy - 9)], '#e83b3b', 6.7)
    # barba entrançada
    bar = capsula(fx + 3, hy + 7, fx + 4, hy + 13, 1.3)
    P.append(Parte(bar, TECIDO_AZ, z=6.4))
    _riscas_h(P, bar, ['#4d65b4', '#f9c22b'], 6.41, alt=1)
    img = desenhar(P, 64, 64)
    if t == 1:
        solto(img, [(fx + 4, hy - 2, '#ffffff')])
    return img


def golem(t):
    """Golem de Arenito (64): blocos de templo empilhados num corpo de ombros enormes, com juntas, cantos
    lascados, rachas e hieróglifos cavados (ankh, pássaro, ondas). A cabeça é um bloco metido entre os
    ombros, com uma fresta de olhos turquesa; o olho de Hórus do peito brilha. Corre areia das juntas e tem
    um tufo de erva seca no ombro. Parado: respira (os blocos sobem e descem), o brilho pulsa."""
    P = []
    dy = (0, 0, 1, 1)[t]
    G = ARENITO
    GE = ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e']
    brilho = ('#0eaf9b', '#30e1b9', '#8ff8e2', '#30e1b9')[t]

    def bloco(pts, rampa, z, vol='esfera'):
        m = poligono(pts) if len(pts) > 2 else retangulo(*pts[0], *pts[1], canto=1)
        P.append(Parte(m, rampa, z=z, volume=vol, brilho=False))
        return m

    def glifo(pts, x0, y0, z=2.5, cor='#7a3045'):
        px(P, [(x0 + a, y0 + b + dy) for a, b in pts], cor, z)
        px(P, [(x0 + a + 1, y0 + b + 1 + dy) for a, b in pts if (a + 1, b + 1) not in pts], '#fbb954', z - 0.01)

    # braço de trás (escuro) e perna de trás
    bloco([(7, 19 + dy), (17, 30 + dy)], GE, 0)
    bloco([(7, 31 + dy), (14, 40 + dy)], GE, 0, 'cilindro_v')
    bloco([(4, 41 + dy), (15, 52 + dy)], GE, 0)
    bloco([(20, 45), (28, 61)], GE, 0.2, 'cilindro_v')
    # tronco: peito largo em trapézio + cintura
    peito = bloco([(13, 20 + dy), (47, 17 + dy), (44, 35 + dy), (18, 36 + dy)], G, 2)
    cint = bloco([(20, 36 + dy), (40, 46 + dy)], G, 2.1, 'cilindro_v')
    px(P, [(x, 27 + dy) for x in range(16, 45) if (x, 27 + dy) in peito and x % 9 != 0], '#9e4539', 2.2)   # junta
    px(P, [(30, y + dy) for y in range(18, 27)], '#9e4539', 2.2)
    px(P, [(x, 41 + dy) for x in range(21, 40)], '#9e4539', 2.2)
    glifo([(1, 0), (0, 1), (2, 1), (1, 2), (0, 3), (1, 3), (2, 3), (1, 4), (1, 5)], 18, 20)           # ankh
    glifo([(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (2, 2), (3, 2), (2, 3), (4, 3)], 19, 29)            # pássaro
    glifo([(0, 1), (1, 0), (2, 1), (3, 0), (4, 1), (0, 3), (1, 2), (2, 3), (3, 2), (4, 3)], 33, 29)   # ondas
    glifo([(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (1, 2), (1, 3)], 28, 37)
    # olho de Hórus no peito (brilha)
    glifo([(0, 1), (1, 0), (2, 0), (3, 0), (4, 1), (1, 2), (2, 2), (3, 2), (2, 3), (1, 4), (4, 3), (5, 4)], 33, 20)
    px(P, [(35, 21 + dy), (35, 22 + dy), (36, 21 + dy)], brilho, 2.6)
    # rachas
    px(P, [(41, 18 + dy), (40, 19 + dy), (40, 20 + dy), (39, 21 + dy), (39, 22 + dy)], '#7a3045', 2.5)
    px(P, [(24, 37 + dy), (25, 38 + dy), (25, 39 + dy)], '#7a3045', 2.5)
    # cabeça: bloco metido entre os ombros, com a fresta dos olhos
    bloco([(32, 7 + dy), (44, 18 + dy)], G, 3)
    px(P, [(x, 12 + dy) for x in range(35, 45)], '#2e222f', 3.1)
    px(P, [(x, 13 + dy) for x in range(36, 45)], '#2e222f', 3.1)
    px(P, [(39, 12 + dy), (40, 12 + dy), (43, 12 + dy), (44, 12 + dy)], brilho, 3.2)
    px(P, [(39, 12 + dy), (43, 12 + dy)], '#ffffff', 3.21)
    px(P, [(34, 16 + dy), (35, 17 + dy), (42, 16 + dy)], '#7a3045', 3.15)
    # tufo de erva seca no ombro
    for i, a in enumerate((16, 18, 20, 22)):
        h = (3, 5, 4, 2)[i] + (t + i) % 2
        px(P, [(a, 19 + dy - j) for j in range(h)], '#a2a947' if i % 2 else '#676633', 1.9)
    # perna da frente
    bloco([(31, 46), (40, 61)], G, 4, 'cilindro_v')
    px(P, [(x, 54) for x in range(32, 40)], '#9e4539', 4.1)
    # braço da frente: ombro, antebraço, punho enorme
    bloco([(41, 17 + dy), (53, 29 + dy)], G, 5)
    bloco([(45, 30 + dy), (52, 40 + dy)], G, 5.1, 'cilindro_v')
    punho = bloco([(42, 41 + dy), (56, 53 + dy)], G, 5.2)
    px(P, [(x, 47 + dy) for x in range(44, 56) if x % 4 != 3], '#9e4539', 5.3)                       # dedos
    px(P, [(x, 44 + dy) for x in range(53, 56)], '#7a3045', 5.3)
    glifo([(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)], 44, 22, z=5.5)
    img = desenhar(P, 64, 64)
    # areia a escorrer das juntas
    sol = []
    for i, (x, y) in enumerate(((47, 30), (22, 46), (48, 41), (10, 41))):
        for j in range(2):
            sol.append((x + j * 2, y + dy + (t + j * 2 + i) % 4 + 1, '#fbb954' if j else '#e6904e'))
    return solto(img, sol)



def cavaleiro(t):
    """Cavaleiro de Ossos Montado (64): esqueleto de armadura enferrujada (elmo com crista vermelha, olho azul
    a brilhar, capa rasgada) montado num camelo-esqueleto (costelas a ver-se, bossa de vértebras, pescoço
    curvo, crânio comprido com olho azul, manta vermelha com franja dourada), lança comprida com bandeirola.
    Parado: o camelo respira e mexe o pescoço, a capa e a bandeirola esvoaçam, os olhos piscam."""
    P = []
    dy = (0, 0, 1, 1)[t]
    nk = (0, 1, 1, 0)[t]
    w = (0, 1, 2, 1)[t]
    OB = OSSO
    OBE = OSSO_ESC
    olho = ('#4d9be6', '#8fd3ff', '#8fd3ff', '#4d9be6')[t]
    # pernas do lado de lá
    for (x0, x1) in ((19, 16), (37, 40)):
        P.append(Parte(capsula(x0, 40 + dy, x1, 50, 1.3) | capsula(x1, 50, x1 + 1, 61, 1.1), OBE, z=0))
    # capa do cavaleiro (atrás, rasgada)
    capa = poligono([(25, 16 + dy), (13 - w, 30 + dy), (10 - w, 37 + dy), (14, 35 + dy), (16, 38 + dy), (19, 34 + dy), (27, 26 + dy)])
    P.append(Parte(capa, ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=0.5))
    # cauda de vértebras
    P.append(Parte(cadeia(curva((13, 36 + dy), (8, 38), (9, 45), 4), [1.2, 1.1, 1.0, 0.9]), OBE, z=1))
    # costelas (com buracos entre elas) e coluna com bossa
    for i, x in enumerate(range(16, 38, 3)):
        top = 33 + dy
        P.append(Parte(capsula(x, top, x + 1, top + 9 - abs(x - 27) * 0.25, 0.9), OB, z=2 + i * 0.01))
    P.append(Parte(capsula(14, 33 + dy, 40, 33 + dy, 1.6), OB, z=2.2, volume='cilindro_h'))
    for i, x in enumerate(range(18, 33, 3)):
        h = 4 - abs(x - 25) * 0.25
        P.append(Parte(capsula(x, 32 + dy, x, 32 + dy - h, 0.9), OB, z=2.1))
    P.append(Parte(elipse(16, 36 + dy, 4, 3.5), OB, z=2.3))                                    # bacia
    # manta vermelha com franja dourada por baixo da sela
    manta = poligono([(21, 30 + dy), (31, 30 + dy), (32, 36 + dy), (20, 36 + dy)])
    P.append(Parte(manta, VERMELHO, z=3))
    listras(P, manta, '#f9c22b', 3.01, lambda x, y: y == 36 + dy and x % 2 == 0, borda=True)
    listras(P, manta, '#6e2727', 3.01, lambda x, y: x == 26)
    # pescoço curvo de vértebras e crânio de camelo
    pesc = curva((39, 34 + dy), (45, 30 + dy), (47 + nk, 21 + dy), 6)
    for i, (x, y) in enumerate(pesc):
        P.append(Parte(elipse(x, y, 1.9, 1.9), OB, z=3.5 + i * 0.01))
    cx_, cy_ = pesc[-1]
    cra = elipse(cx_ + 3, cy_ - 1, 4, 3) | capsula(cx_ + 4, cy_, cx_ + 11, cy_ + 2, 2)
    P.append(Parte(cra, OB, z=4))
    px(P, [(cx_ + 3, cy_ - 2), (cx_ + 4, cy_ - 2), (cx_ + 3, cy_ - 1), (cx_ + 4, cy_ - 1)], '#2e222f', 4.1)
    px(P, [(cx_ + 4, cy_ - 1)], olho, 4.2)
    px(P, [(cx_ + 10, cy_ + 1)], '#2e222f', 4.1)
    px(P, [(cx_ + x, cy_ + 3) for x in range(6, 11, 2)], '#3e3546', 4.1)                         # dentes
    # cavaleiro: perna, tronco de armadura enferrujada, elmo
    P.append(Parte(capsula(27, 28 + dy, 31, 34 + dy, 1.6) | capsula(31, 34 + dy, 30, 40 + dy, 1.3), FERRO, z=5))
    tronco = poligono([(22, 16 + dy), (30, 16 + dy), (31, 28 + dy), (23, 29 + dy)])
    P.append(Parte(tronco, FERRO, z=5.1, volume='cilindro_v'))
    textura(P, tronco, '#9e4539', None, 5.11, 4, 0.18)                                            # ferrugem
    listras(P, tronco, '#3e3546', 5.12, lambda x, y: y in (21 + dy, 25 + dy))
    P.append(Parte(capsula(22, 18 + dy, 25, 18 + dy, 2.2), FERRO, z=5.2))                         # ombreira
    # crânio dentro do elmo
    hx, hy = 27, 10 + dy
    elmo = elipse(hx, hy, 4.6, 4.6) | retangulo(hx - 4, hy, hx + 1, hy + 4)
    P.append(Parte(elmo, FERRO, z=6))
    textura(P, elmo, '#9e4539', None, 6.01, 8, 0.12)
    cara = retangulo(hx + 1, hy - 1, hx + 4, hy + 4)
    P.append(Parte(cara, OB, z=6.1))
    px(P, [(hx + 2, hy), (hx + 3, hy)], '#2e222f', 6.2)
    px(P, [(hx + 3, hy)], olho, 6.3)
    px(P, [(hx + 2, hy + 3), (hx + 4, hy + 3)], '#3e3546', 6.2)
    px(P, [(x, hy - 2) for x in range(hx - 2, hx + 5)], '#625565', 6.2)                           # viseira
    # crista vermelha no elmo
    for i in range(5):
        P.append(Parte(capsula(hx - 2 + i, hy - 5, hx - 4 + i - w // 2, hy - 8 + abs(i - 2) * 0.5, 0.8), VERMELHO, z=5.9))
    # braço com a lança comprida (para a frente e para cima) e bandeirola
    P.append(Parte(capsula(27, 19 + dy, 32, 23 + dy, 1.3), FERRO, z=7))
    P.append(Parte(capsula(20, 29 + dy, 62, 6 + dy, 0.7), MAD, z=7.1))
    px(P, [(62, 5 + dy), (63, 4 + dy), (61, 5 + dy)], '#c7dcd0', 7.2)
    band = poligono([(51, 12 + dy), (57, 8.5 + dy), (49 - w, 19 + dy + (w % 2)), (51, 15 + dy)])
    P.append(Parte(band, VERMELHO, z=7.05))
    # pernas do lado de cá (joelho de camelo)
    for (x0, x1) in ((22, 20), (35, 37)):
        P.append(Parte(capsula(x0, 40 + dy, x1, 50, 1.4) | capsula(x1, 50, x1 + 1, 61, 1.2), OB, z=8))
        px(P, [(x1, 50), (x1 + 1, 50)], '#ffffff', 8.1)
        px(P, [(x1 - 1, 62), (x1, 62), (x1 + 2, 62)], '#7f708a', 8.1)
    return desenhar(P, 64, 64)



def djinn(t):
    """Djinn da Tempestade (48): espírito azul e musculado de braços cruzados, turbante branco com joia
    vermelha e pena, orelha bicuda, pera preta, olhos amarelos a brilhar, pulseiras de ouro, faixa vermelha
    e, em vez de pernas, uma cauda de fumo de tempestade que se enrola. Parado: flutua, o fumo gira,
    faíscas de raio à volta."""
    P = []
    dy = (0, 1, 1, 0)[t]
    FUMO = ['#484a77', '#905ea9', '#a884f3', '#eaaded', '#ffffff']
    # cauda de fumo (enrola para baixo e para trás)
    sw = (0, 1, 0, -1)[t]
    cam = curva((23, 31 + dy), (30 + sw, 40), (14 - sw, 45), 8)
    for i, (x, y) in enumerate(cam):
        r = max(1.2, 6.5 - i * 0.75)
        P.append(Parte(elipse(x, y, r, r * 0.9), FUMO, z=1 - i * 0.01))
    caud = set().union(*[elipse(x, y, max(1.2, 6.5 - i * 0.75), max(1.2, 6.5 - i * 0.75) * 0.9) for i, (x, y) in enumerate(cam)])
    listras(P, caud, '#eaaded', 1.05, lambda x, y: (x + 2 * y + t * 2) % 7 == 0)
    listras(P, caud, '#6b3e75', 1.05, lambda x, y: (x - 2 * y - t * 2) % 9 == 0 and y > 36)
    # faixa vermelha na cintura
    P.append(Parte(elipse(23, 30 + dy, 6.5, 2.4), VERMELHO, z=2))
    P.append(Parte(poligono([(18, 30 + dy), (14 - sw, 35 + dy), (17, 36 + dy), (20, 32 + dy)]), VERMELHO, z=1.9))
    # tronco musculado
    tr = elipse(23, 22 + dy, 7.5, 7.5)
    P.append(Parte(tr, AZUL, z=3))
    px(P, [(24, 19 + dy), (24, 20 + dy), (25, 21 + dy), (21, 25 + dy), (22, 26 + dy), (24, 26 + dy)], '#484a77', 3.1)  # músculos
    # cabeça
    hx, hy = 26, 11 + dy
    P.append(Parte(poligono([(hx - 3, hy), (hx - 8, hy - 3), (hx - 3, hy + 3)]), AZUL, z=3.9))   # orelha bicuda
    cab = elipse(hx, hy + 1, 5.2, 5.6)
    P.append(Parte(cab, AZUL, z=4, luz=0.1))
    # olhos que brilham e sobrolho zangado
    px(P, [(hx + 1, hy), (hx + 2, hy), (hx + 3, hy), (hx + 1, hy + 1), (hx + 2, hy + 1), (hx + 3, hy + 1)], '#2e222f', 4.15)
    px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 2, hy + 1)], '#f9c22b', 4.2)
    px(P, [(hx + 2, hy)], '#ffffff', 4.21)
    px(P, [(hx, hy - 1), (hx + 1, hy - 1), (hx + 2, hy - 1), (hx + 3, hy - 2), (hx + 4, hy - 2)], '#2e222f', 4.2)
    px(P, [(hx + 5, hy + 1), (hx + 5, hy + 2), (hx + 6, hy + 2)], '#4d65b4', 4.15)               # nariz
    px(P, [(hx + 2, hy + 4), (hx + 3, hy + 4), (hx + 4, hy + 4), (hx + 5, hy + 3)], '#323353', 4.2)  # sorriso
    P.append(Parte(capsula(hx + 3, hy + 6, hx + 4, hy + 9, 1.0), NEGRO, z=4.3))                   # pera
    # turbante branco com joia e pena
    tur = {p for p in elipse(hx - 0.5, hy - 4, 6, 3.8) if p[1] <= hy - 2}
    P.append(Parte(tur, PANO, z=5))
    listras(P, tur, '#9babb2', 5.01, lambda x, y: (y + x // 3) % 3 == 0)
    px(P, [(hx + 3, hy - 4), (hx + 4, hy - 4), (hx + 3, hy - 3), (hx + 4, hy - 3)], '#e83b3b', 5.1)
    px(P, [(hx + 3, hy - 4)], '#fca790', 5.11)
    P.append(Parte(capsula(hx + 2, hy - 6, hx - (t % 2), hy - 12, 1.0), ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'], z=4.9))
    # peito: músculos marcados
    px(P, [(23, 17 + dy), (24, 18 + dy), (25, 18 + dy), (26, 18 + dy)], '#4d65b4', 3.1)
    # braço da frente dobrado à frente do peito (punho fechado), pulseira de ouro
    P.append(Parte(capsula(28, 16 + dy, 31, 22 + dy, 2.4), AZUL, z=6))
    P.append(Parte(capsula(31, 23 + dy, 21, 24 + dy, 2.2), AZUL, z=6.1, volume='cilindro_h'))
    P.append(Parte(elipse(20, 24 + dy, 2.4, 2.4), AZUL, z=6.2))
    px(P, [(27, 22 + dy), (27, 23 + dy), (27, 24 + dy), (27, 25 + dy)], '#f9c22b', 6.3)
    px(P, [(27, 22 + dy)], '#fbff86', 6.31)
    # ombro de trás
    P.append(Parte(elipse(17, 18 + dy, 3, 3), AZUL_ESC, z=2.9))
    img = desenhar(P, 48, 48)
    # faíscas de raio
    fa = [((5, 10), (6, 11), (5, 12), (6, 13)), ((40, 6), (41, 7), (40, 8)), ((40, 30), (41, 31), (40, 32), (41, 33))]
    for i, f in enumerate(fa):
        if (t + i) % 3 == 0:
            solto(img, [(x, y, '#fbff86') for x, y in f])
    return img


def sacerdote(t):
    """Sacerdote-Chacal (48): homem de pele bronzeada com cabeça de chacal preta (orelhas altas, olhos de ouro),
    toucado azul e dourado, colar largo de ouro e lápis-lazúli, saiote branco com cinto de ouro e uma balança
    dourada na mão: num prato uma pena, no outro um coração. Parado: a balança oscila, os olhos brilham."""
    P = []
    dy = (0, 0, 1, 1)[t]
    PB = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fca790']
    PBE = ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e']
    # pernas e braço de trás
    P.append(Parte(capsula(21, 33, 20, 45, 1.7), PBE, z=0, volume='cilindro_v'))
    P.append(Parte(capsula(19, 19 + dy, 16, 28 + dy, 1.6), PBE, z=0.5))
    # toucado (atrás da cabeça, cai até aos ombros)
    hx, hy = 25, 10 + dy
    nem = poligono([(hx - 5, hy - 3), (hx + 1, hy - 4), (hx + 1, hy + 9), (hx - 6, hy + 9)])
    P.append(Parte(nem, TECIDO_AZ, z=1))
    _riscas_h(P, nem, ['#4d65b4', '#f9c22b'], 1.01, alt=2)
    # tronco
    tr = elipse(23, 24 + dy, 5.5, 6.5)
    P.append(Parte(tr, PB, z=2))
    P.append(Parte(capsula(25, 33, 26, 45, 1.8), PB, z=3, volume='cilindro_v'))
    px(P, [(19, 46), (20, 46), (21, 46), (25, 46), (26, 46), (27, 46)], '#f79617', 3.1)            # sandálias
    # saiote branco com cinto de ouro
    sai = poligono([(18, 29 + dy), (29, 29 + dy), (31, 38), (17, 38)])
    P.append(Parte(sai, PANO, z=4))
    listras(P, sai, '#9babb2', 4.01, lambda x, y: x % 3 == 0 and y > 31)
    P.append(Parte(retangulo(18, 29 + dy, 29, 30 + dy), OURO, z=4.1, plano=True))
    P.append(Parte(poligono([(24, 31 + dy), (27, 31 + dy), (26, 37), (25, 37)]), OURO, z=4.2, plano=True))
    # colar largo (ouro e azul)
    col = {p for p in elipse(24, 17 + dy, 6.5, 4.5) if p[1] >= 17 + dy}
    P.append(Parte(col, OURO, z=5))
    _riscas_h(P, col, ['#f9c22b', '#4d65b4'], 5.01, alt=1)
    # cabeça de chacal preta
    P.append(Parte(poligono([(hx - 3, hy - 1), (hx - 2, hy - 10), (hx + 1, hy - 2)]), NEGRO, z=5.5))  # orelha de trás
    cab = elipse(hx + 1, hy + 1, 4.5, 4)
    foc = capsula(hx + 3, hy + 2, hx + 10, hy + 4, 1.8)
    P.append(Parte(cab | foc, NEGRO, z=6))
    P.append(Parte(poligono([(hx, hy - 1), (hx + 2, hy - 11), (hx + 4, hy - 2)]), NEGRO, z=6.1))   # orelha
    px(P, [(hx + 2, hy - 7), (hx + 2, hy - 6), (hx + 2, hy - 5)], '#f9c22b', 6.2)                  # orelha com ouro
    px(P, [(hx + 10, hy + 3)], '#2e222f', 6.2)
    px(P, [(x, hy + 5) for x in range(hx + 5, hx + 10)], '#2e222f', 6.2)                           # boca
    # olho de ouro pintado
    gl = ('#f9c22b', '#fbff86', '#fbff86', '#f9c22b')[t]
    px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 4, hy), (hx + 1, hy + 1)], '#f79617', 6.25)
    px(P, [(hx + 3, hy), (hx + 4, hy)], gl, 6.3)
    px(P, [(hx + 3, hy)], '#ffffff', 6.31)
    # braço da frente com a balança dourada
    P.append(Parte(capsula(26, 19 + dy, 30, 25 + dy, 1.6), PB, z=7))
    P.append(Parte(capsula(30, 25 + dy, 34, 23 + dy, 1.4), PB, z=7.1))
    px(P, [(29, 24 + dy), (30, 24 + dy)], '#f9c22b', 7.2)                                           # pulseira
    bx = 35
    P.append(Parte(capsula(bx, 25 + dy, bx, 14 + dy, 0.7), OURO, z=7.3))
    inc = (0, 1, 0, -1)[t]
    P.append(Parte(capsula(bx - 6, 15 + dy + inc, bx + 6, 15 + dy - inc, 0.7), OURO, z=7.35))
    px(P, [(bx, 13 + dy)], '#fbff86', 7.4)
    for sx, sgn in ((-6, 1), (6, -1)):
        yy = 15 + dy + inc * sgn
        px(P, [(bx + sx, yy + j) for j in range(1, 6)], '#f79617', 7.3)
        prato = {p for p in elipse(bx + sx, yy + 6, 3.2, 1.6) if p[1] >= yy + 6}
        P.append(Parte(prato, OURO, z=7.4))
    # pena (prato da esquerda) e coração (prato da direita)
    yy = 15 + dy + inc
    px(P, [(bx - 6, yy + 3), (bx - 6, yy + 4), (bx - 5, yy + 2), (bx - 7, yy + 4)], '#ffffff', 7.45)
    yy = 15 + dy - inc
    px(P, [(bx + 5, yy + 4), (bx + 7, yy + 4), (bx + 5, yy + 5), (bx + 6, yy + 5), (bx + 7, yy + 5), (bx + 6, yy + 6)], '#e83b3b', 7.45)
    return desenhar(P, 48, 48)


def miragem(t):
    """A Miragem (48): figura feita de água e de luz, sem pernas (o corpo cai como uma cascata e abre-se numa
    poça), olhos brancos sem pupila, uma coroa de luz e orbes brancos à volta. Tudo treme como o ar quente:
    cada linha do desenho foge um píxel para o lado, a ondular."""
    P = []
    dy = (0, 1, 1, 0)[t]
    # orbe de trás
    ang = t * math.pi / 2
    # corpo em cascata
    corpo = poligono([(19, 16 + dy), (29, 16 + dy), (31, 30), (34, 41), (38, 45), (10, 45), (14, 41), (17, 30)])
    P.append(Parte(corpo, AGUA, z=2, volume='cilindro_v'))
    listras(P, corpo, '#8ff8e2', 2.01, lambda x, y: (x * 3 + y + t * 4) % 11 == 0)
    listras(P, corpo, '#0b8a8f', 2.02, lambda x, y: (x * 3 - y + t * 2) % 13 == 0 and y > 24)
    poca = elipse(24, 45, 15, 2.2)
    P.append(Parte(poca, AGUA, z=2.5))
    px(P, [(x, 45) for x in range(12, 37, 3)], '#8ff8e2', 2.6)
    # braços abertos (gotas a cair das mãos)
    P.append(Parte(capsula(19, 18 + dy, 12, 26 + dy, 1.6), AGUA, z=1.5))
    P.append(Parte(capsula(29, 18 + dy, 36, 25 + dy, 1.7), AGUA, z=3))
    # cabeça
    hx, hy = 25, 10 + dy
    cab = elipse(hx, hy, 4.8, 5.3)
    P.append(Parte(cab, AGUA, z=4, luz=0.15))
    # cabelo de água a escorrer para trás
    P.append(Parte(poligono([(hx - 4, hy - 4), (hx + 2, hy - 6), (hx - 2, hy - 2), (hx - 6, hy + 8), (hx - 8, hy + 6)]), AGUA, z=3.9))
    # olhos brancos a brilhar
    px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 2, hy + 1), (hx + 3, hy + 1)], '#ffffff', 4.2)
    px(P, [(hx + 1, hy - 1), (hx + 4, hy + 1)], '#0b5e65', 4.15)
    px(P, [(hx + 3, hy + 4), (hx + 4, hy + 4)], '#0b8a8f', 4.2)
    # coroa de luz (três pontas)
    for i, (a, b) in enumerate(((-2, -9), (1, -11), (4, -9))):
        P.append(Parte(capsula(hx + a * 0.6, hy - 5, hx + a, hy + b - (t + i) % 2, 0.8), ['#f79617', '#f9c22b', '#fbff86', '#ffffff', '#ffffff'], z=4.5))
    img = desenhar(P, 48, 48)
    # tremer como o ar quente: cada linha desliza um píxel
    out = Image.new('RGBA', img.size, (0, 0, 0, 0))
    for y in range(img.height):
        d = int(round(math.sin(y * 0.7 + t * math.pi / 2) * 0.9))
        out.paste(img.crop((0, y, img.width, y + 1)), (d, y))
    # orbes de luz à volta e gotas
    sol = []
    for k in range(3):
        a = ang + k * 2.09
        x, y = 24 + math.cos(a) * 15, 20 + math.sin(a) * 5
        sol += [(x, y, '#ffffff'), (x + 1, y, '#8ff8e2'), (x, y + 1, '#8ff8e2'), (x - 1, y, '#30e1b9'), (x, y - 1, '#30e1b9')]
    sol += [(12, 29 + t * 2, '#8ff8e2'), (36, 28 + ((t + 2) % 4) * 2, '#8ff8e2')]
    return solto(out, sol)


def abutre(t):
    """Abutre Rei (48): abutre enorme a pairar e a bater as asas (cima, meio, baixo, meio): penas castanho-
    escuras em escamas com as pontas abertas como dedos, gola de penugem branca, pescoço e cabeça carecas
    cor-de-rosa, bico curvo cor de marfim, olho vermelho, uma coroa de penas douradas e garras amarelas."""
    P = []
    fase = (0, 1, 2, 1)[t]
    dy = (0, 1, 2, 1)[t] - 1
    PEN = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
    PEN_E = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
    CAREC = ['#7a3045', '#c32454', '#f04f78', '#f68181', '#fdcbb0']
    MARF = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']

    def asa(ox, oy, fase, rampa, z, k=1.0):
        # fase: 0 = levantada, 1 = aberta para trás, 2 = em baixo
        tx, ty = ((-12, -17), (-19, -4), (-13, 11))[fase]
        tx, ty = ox + tx * k, oy + ty * k
        tr = ((4, 7), (5, 4), (6, -2))[fase]
        base = poligono([(ox + 2, oy - 3), (tx, ty), (tx + tr[0], ty + tr[1]), (ox + 1, oy + 7)])
        P.append(Parte(base, rampa, z=z))
        escamas(P, base, rampa[1], z + 0.01, passo=3, claro=rampa[4])
        # orla clara das penas de cobertura
        px(P, [p for p in base if dentro(base, p) and abs((p[0] - ox) * (ty - oy) - (p[1] - oy) * (tx - ox)) < 12 * k], rampa[3], z + 0.02)
        # penas primárias abertas como dedos (saem da ponta para fora)
        ang = math.atan2(ty - oy, tx - ox)
        for i in range(4):
            aa = ang + math.radians(-12 + i * 12)
            fx, fy = tx + tr[0] * i / 4, ty + tr[1] * i / 4
            P.append(Parte(capsula(fx, fy, fx + math.cos(aa) * 6 * k, fy + math.sin(aa) * 6 * k, 1.0), rampa, z=z - 0.1 - i * 0.01))
    # asa de lá
    asa(24, 18 + dy, fase, PEN_E, 0.5, 0.85)
    # cauda em leque
    for i in range(3):
        P.append(Parte(capsula(17, 30 + dy, 9 + i * 2, 36 + dy + i, 1.6), PEN, z=1))
    # garras amarelas penduradas
    for x in (20, 24):
        P.append(Parte(capsula(x, 33 + dy, x, 38 + dy, 0.9), OURO_ESC, z=1.5))
        px(P, [(x - 1, 39 + dy), (x + 1, 39 + dy), (x, 39 + dy)], '#2e222f', 1.6)
    # corpo de penas
    corpo = elipse(22, 26 + dy, 7, 8)
    P.append(Parte(corpo, ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a'], z=2))
    escamas(P, corpo, '#2e222f', 2.01, passo=3, claro='#966c6c')
    # gola de penugem branca (recortada)
    gola = elipse(27, 19 + dy, 5.5, 3.6)
    gola -= {(x, y) for (x, y) in gola if y >= 21 + dy and x % 2 == 0}
    P.append(Parte(gola, PANO_AREIA, z=3))
    # pescoço e cabeça carecas
    P.append(Parte(capsula(28, 18 + dy, 31, 12 + dy, 1.6), CAREC, z=3.5))
    hx, hy = 32, 10 + dy
    cab = elipse(hx, hy, 3.4, 3)
    P.append(Parte(cab, CAREC, z=4))
    px(P, [(hx - 2, hy + 1), (hx - 1, hy + 2)], '#c32454', 4.05)                                  # rugas
    bico = poligono([(hx + 2, hy - 2), (hx + 6, hy - 1), (hx + 7, hy + 2), (hx + 6, hy + 3), (hx + 2, hy + 1)])
    P.append(Parte(bico, MARF, z=4.2))
    px(P, [(hx + 6, hy + 3), (hx + 7, hy + 2)], '#45293f', 4.3)                                   # ponta curva
    px(P, [(hx, hy - 1), (hx + 1, hy - 1)], '#e83b3b', 4.3)                                       # olho
    px(P, [(hx + 1, hy - 1)], '#2e222f', 4.31)
    px(P, [(hx, hy - 1)], '#fca790', 4.32)
    # coroa de penas douradas
    for i, ang in enumerate((-150, -125, -100, -78)):
        a = math.radians(ang)
        bx, by = hx - 1 + i * 0.8, hy - 2
        P.append(Parte(capsula(bx, by, bx + math.cos(a) * 6, by + math.sin(a) * 6, 1.0), OURO, z=3.9))
        px(P, [(bx + math.cos(a) * 6, by + math.sin(a) * 6)], '#ffffff', 3.95)
    # asa da frente
    asa(22, 20 + dy, fase, PEN, 5, 1.0)
    return desenhar(P, 48, 48)



# =====================================================================================
# BOSSES
# =====================================================================================

def imperador(t):
    """Escorpião Imperador (64): escorpião negro com as placas debruadas a ouro, a marca azul do Sistema a
    brilhar na carapaça, uma coroa de picos dourados, pinças enormes de pontas douradas, olhos turquesa e uma
    cauda de anéis negros e dourados com um ferrão de ouro a pingar veneno. Parado: a cauda balança, as
    pinças abrem e fecham, a marca pulsa."""
    P = []
    dy = (0, 0, 1, 1)[t]
    sw = (0, 1, 2, 1)[t]
    pin = (0, 1, 2, 1)[t]
    N = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
    NE = ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565']
    marca = ('#4d65b4', '#4d9be6', '#8fd3ff', '#4d9be6')[t]
    # pernas do lado de lá
    for x, pe in ((16, 9), (23, 18), (30, 28), (37, 39)):
        P.append(Parte(capsula(x, 46 + dy, x - 4, 40 + dy, 1.3) | capsula(x - 4, 40 + dy, pe - 2, 60, 1.1), NE, z=0))
    # cauda: anéis que sobem pelas costas, com aros de ouro
    cam = curva((15, 41 + dy), (-2 + sw, 8), (27 + sw, 8 + dy), 8)
    for i, (x, y) in enumerate(cam):
        r = 4.4 - i * 0.28
        anel = elipse(x, y, r, r)
        P.append(Parte(anel, N, z=1 + i * 0.01))
        px(P, [p for p in anel if not dentro(anel, p) and (p[0] - x) + (p[1] - y) < -r * 0.6], '#f9c22b', 1 + i * 0.01 + 0.005)
    fx, fy = cam[-1]
    P.append(Parte(elipse(fx + 4, fy + 3, 3.5, 3), OURO, z=1.2))                                  # bolbo de ouro
    P.append(Parte(capsula(fx + 6, fy + 4, fx + 9, fy + 9, 1.0), OURO_ESC, z=1.25))               # ferrão
    # abdómen em placas debruadas a ouro
    abd = elipse(26, 45 + dy, 14, 7.5)
    P.append(Parte(abd, N, z=2))
    for x in (17, 23, 29, 35):
        px(P, [(x, y) for y in range(38 + dy, 47 + dy) if (x, y) in abd and dentro(abd, (x, y))], '#f79617', 2.1)
        px(P, [(x + 1, y) for y in range(38 + dy, 46 + dy) if (x + 1, y) in abd and dentro(abd, (x + 1, y))], '#2e222f', 2.1)
    textura(P, abd, None, '#7f708a', 2.15, 3, 0, 0.05)
    # marca azul do Sistema (losango com olho) na carapaça
    mx, my = 26, 41 + dy
    los = poligono([(mx - 5, my), (mx, my - 3.5), (mx + 5, my), (mx, my + 3.5)])
    px(P, [p for p in los if not dentro(los, p)], marca, 2.3)
    px(P, [(mx - 1, my), (mx, my), (mx + 1, my), (mx, my - 1), (mx, my + 1)], marca, 2.3)
    px(P, [(mx, my)], '#ffffff', 2.31)
    # cabeça (cefalotórax) com coroa
    cab = elipse(43, 45 + dy, 8, 6.5)
    P.append(Parte(cab, N, z=3))
    px(P, [p for p in cab if not dentro(cab, p) and p[1] < 42 + dy], '#f9c22b', 3.05)
    for i, x in enumerate((39, 42, 45)):
        _espinho(P, x, 39.5 + dy, -90 + (i - 1) * 12, 4 + (i == 1), 1.3, OURO, 2.9)
    px(P, [(41, 39 + dy)], '#e83b3b', 3.0)
    # olhos turquesa com brilho
    for (ex, ey) in ((45, 42), (48, 43)):
        px(P, [(ex, ey + dy), (ex + 1, ey + dy), (ex, ey + 1 + dy), (ex + 1, ey + 1 + dy)], '#30e1b9', 3.2)
        px(P, [(ex, ey + dy)], '#ffffff', 3.21)
    px(P, [(x, 49 + dy) for x in range(46, 51)], '#2e222f', 3.2)
    # pernas do lado de cá
    for x, pe in ((19, 15), (26, 24), (33, 33), (40, 43)):
        P.append(Parte(capsula(x, 49 + dy, x - 3, 47 + dy, 1.3) | capsula(x - 3, 47 + dy, pe, 61, 1.2), N, z=4))
        px(P, [(pe, 61), (pe + 1, 61)], '#f79617', 4.1)
    # braço e pinça enorme
    P.append(Parte(capsula(48, 47 + dy, 52, 42 + dy, 2.4), N, z=5))
    garra = elipse(55, 39 + dy, 5.2, 4.3)
    P.append(Parte(garra, N, z=6))
    px(P, [p for p in garra if not dentro(garra, p) and p[1] < 37 + dy], '#f9c22b', 6.05)
    P.append(Parte(capsula(57, 36 + dy, 62, 31 + dy - pin, 1.8), N, z=6.1))
    P.append(Parte(capsula(58, 42 + dy, 62, 41 + dy, 1.6), N, z=6.1))
    px(P, [(62, 31 + dy - pin), (61, 32 + dy - pin), (62, 41 + dy), (63, 41 + dy)], '#f9c22b', 6.2)
    px(P, [(53, 37 + dy), (54, 36 + dy)], '#7f708a', 6.2)
    img = desenhar(P, 64, 64)
    gx, gy = fx + 9, fy + 10
    if t in (1, 2, 3):
        solto(img, [(gx, gy + (t - 1) * 2, '#91db69'), (gx, gy + (t - 1) * 2 + 1, '#1ebc73')])
    return img


def dragao(t):
    """Esqueleto de Dragão Jovem (64): esqueleto de dragão de quatro patas, crânio com chifres e órbitas de
    fogo azul, costelas com um coração de fogo azul lá dentro, pescoço de vértebras, asas de osso com restos
    de membrana rasgada e cauda de vértebras com espinhos. Parado: o fogo azul tremeluz, as asas abrem um
    pouco, fumo azul sai da boca."""
    P = []
    dy = (0, 0, 1, 1)[t]
    ab = (0, 1, 2, 1)[t]
    OB = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']
    OBE = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
    MEMB = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
    fogo = ('#4d9be6', '#8fd3ff', '#4d9be6', '#8fd3ff')[t]
    # asa de lá (só os ossos)
    om = (30, 33 + dy)
    pu = (22 - ab, 10 + dy - ab)
    P.append(Parte(capsula(*om, *pu, 1.4), OBE, z=0))
    for (fx_, fy_) in ((6, 18), (11, 24), (17, 28)):
        P.append(Parte(capsula(*pu, fx_ - ab, fy_ + dy, 0.9), OBE, z=0))
    # pernas de lá
    P.append(Parte(capsula(17, 41 + dy, 14, 50, 1.6) | capsula(14, 50, 16, 60, 1.3), OBE, z=0.5))
    P.append(Parte(capsula(36, 41 + dy, 39, 50, 1.6) | capsula(39, 50, 38, 60, 1.3), OBE, z=0.5))
    # cauda de vértebras com espinhos
    cam = curva((15, 39 + dy), (4, 40), (2, 52 - ab), 8)
    for i, (x, y) in enumerate(cam):
        P.append(Parte(elipse(x, y, 2.1 - i * 0.15, 2.1 - i * 0.15), OB, z=1 + i * 0.01))
        if i % 2 == 0 and i < 7:
            _espinho(P, x, y - 1.5, -110, 3, 0.9, OB, 0.95)
    # coração de fogo azul dentro das costelas
    P.append(Parte(elipse(26, 38 + dy, 5, 4), ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'], z=1.5))
    px(P, [(25, 37 + dy), (26, 37 + dy), (25, 38 + dy)], fogo, 1.6)
    # costelas (com espaço entre elas) e coluna
    for i, x in enumerate(range(17, 36, 3)):
        h = 9 - abs(x - 26) * 0.35
        P.append(Parte(capsula(x, 33 + dy, x + 1.5, 33 + dy + h, 0.8), OB, z=2 + i * 0.01))
    P.append(Parte(capsula(14, 33 + dy, 38, 32 + dy, 1.7), OB, z=2.2, volume='cilindro_h'))
    for x in range(16, 38, 3):
        _espinho(P, x, 31.5 + dy, -95, 3, 0.9, OB, 2.15)
    P.append(Parte(elipse(15, 36 + dy, 4, 3.4), OB, z=2.3))                                      # bacia
    # pescoço curvo e crânio
    pesc = curva((38, 33 + dy), (46, 31 + dy), (47, 20 + dy), 6)
    for i, (x, y) in enumerate(pesc):
        P.append(Parte(elipse(x, y, 2.2, 2.2), OB, z=3 + i * 0.01))
    hx, hy = pesc[-1]
    cra = elipse(hx + 3, hy - 1, 5, 4) | capsula(hx + 5, hy, hx + 13, hy + 1, 2.4)
    P.append(Parte(cra, OB, z=4))
    maxi = capsula(hx + 4, hy + 4, hx + 12, hy + 4 + ab * 0.5, 1.4)                              # mandíbula
    P.append(Parte(maxi, OB, z=3.9))
    px(P, [(hx + 6 + i * 2, hy + 3) for i in range(4)], '#ffffff', 4.1)                          # dentes
    for (a, b, c) in ((-2, -4, -150), (0, -4, -130)):
        _espinho(P, hx + a, hy + b, c, 7, 1.4, OB, 3.95, ponta='#ffffff')                          # chifres
    # órbita com chama azul
    px(P, [(hx + 3, hy - 2), (hx + 4, hy - 2), (hx + 5, hy - 2), (hx + 3, hy - 1), (hx + 4, hy - 1), (hx + 5, hy - 1), (hx + 4, hy)], '#2e222f', 4.2)
    px(P, [(hx + 4, hy - 2), (hx + 4, hy - 1)], fogo, 4.3)
    px(P, [(hx + 4, hy - 2)], '#ffffff', 4.31)
    px(P, [(hx + 11, hy - 1), (hx + 12, hy - 1)], '#2e222f', 4.2)                                # narina
    # patas de cá com garras
    for (o, j, pe) in (((19, 41 + dy), (17, 50), (19, 60)), ((34, 41 + dy), (38, 50), (37, 60))):
        P.append(Parte(capsula(*o, *j, 1.8) | capsula(*j, *pe, 1.5), OB, z=5))
        px(P, [(j[0], j[1]), (j[0] + 1, j[1])], '#ffffff', 5.1)
        for d in (-1, 1, 3):
            px(P, [(pe[0] + d, 61)], '#c7dcd0', 5.1)
    # asa de cá: braço de osso, dedos e membrana rasgada entre eles
    om = (29, 32 + dy)
    pu = (24 - ab, 6 + dy - ab)
    dedos = ((5 - ab, 15 + dy), (10 - ab, 22 + dy), (16, 27 + dy))
    memb = poligono([pu, dedos[0], (8, 18 + dy), dedos[1], (14, 25 + dy), dedos[2], om])
    memb = {p for p in memb if (p[0] * 3 + p[1] * 5) % 11 not in (0, 1) or p[1] < 14 + dy}
    P.append(Parte(memb, MEMB, z=5.5, separar=False))
    P.append(Parte(capsula(*om, *pu, 1.6), OB, z=6))
    for d in dedos:
        P.append(Parte(capsula(*pu, *d, 1.0), OB, z=6.1))
    P.append(Parte(elipse(pu[0], pu[1], 1.8, 1.8), OB, z=6.2))
    _espinho(P, pu[0], pu[1] - 1, -80, 4, 1.0, OB, 6.15, ponta='#ffffff')
    img = desenhar(P, 64, 64)
    # fumo azul da boca e faíscas do coração
    sol = []
    for i in range(3):
        sol.append((hx + 14 + i + (t % 2), hy + 2 - i * 2 - t % 2, ('#8fd3ff', '#4d9be6', '#484a77')[i]))
    sol.append((24 + (t % 2) * 3, 30 + dy - t, '#8fd3ff'))
    return solto(img, sol)


def farao(t):
    """Faraó Eterno (96): múmia real alta (proporções de adulto), ligaduras com faixas douradas, máscara de
    ouro com olhos que brilham azul (um antigo Jogador), nemes azul e dourado com a cobra na testa, barba
    entrançada, colar largo, escaravelho azul ao peito, saiote dourado, capa azul-escura e o cetro-serpente
    (uma cobra de ouro de olhos vermelhos) na mão. Parado: respira, a capa e as pontas soltas das ligaduras
    abanam, os olhos e o cetro brilham, sobe pó azul."""
    P = []
    dy = (0, 0, 1, 1)[t]
    w = (0, 1, 2, 1)[t]
    gl = ('#4d9be6', '#8fd3ff', '#8fd3ff', '#4d9be6')[t]
    LIG = ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff']
    LIGE = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
    CAPA = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
    cx = 44
    # capa azul-escura atrás (esvoaça para a esquerda)
    capa = poligono([(cx - 9, 33 + dy), (cx + 4, 33 + dy), (cx + 2, 60), (cx - 2, 92), (cx - 20 - w, 92), (cx - 24 - w, 86),
                     (cx - 17, 60)])
    P.append(Parte(capa, CAPA, z=0))
    listras(P, capa, '#323353', 0.01, lambda x, y: (x + y // 3) % 7 == 0 and y > 50)
    px(P, [(x, 92) for x in range(cx - 22 - w, cx - 1) if x % 3 == 0], '#f9c22b', 0.02)
    # perna de trás e braço de trás (ligaduras)
    P.append(Parte(capsula(cx - 4, 66, cx - 6, 91, 3.4), LIGE, z=1, volume='cilindro_v'))
    P.append(Parte(capsula(cx - 9, 37 + dy, cx - 12, 52 + dy, 3.0) | capsula(cx - 12, 52 + dy, cx - 10, 63 + dy, 2.6), LIGE, z=1.2))
    # ponta de ligadura solta do braço de trás
    P.append(Parte(capsula(cx - 11, 60 + dy, cx - 15 - w, 68 + dy, 1.0), LIGE, z=1.1))
    # tronco de ligaduras com faixas douradas
    tr = poligono([(cx - 10, 34 + dy), (cx + 9, 34 + dy), (cx + 7, 60 + dy), (cx - 8, 60 + dy)])
    P.append(Parte(tr, LIG, z=2, volume='cilindro_v'))
    listras(P, tr, '#966c6c', 2.01, lambda x, y: (y - (x // 5)) % 4 == 0)
    listras(P, tr, '#f9c22b', 2.02, lambda x, y: (y - (x // 5)) % 12 == 6)
    # saiote dourado com painel azul
    sai = poligono([(cx - 9, 59 + dy), (cx + 8, 59 + dy), (cx + 11, 72), (cx - 11, 72)])
    P.append(Parte(sai, OURO, z=3))
    listras(P, sai, '#f79617', 3.01, lambda x, y: x % 3 == 0 and y > 62)
    pan = poligono([(cx + 1, 61 + dy), (cx + 6, 61 + dy), (cx + 7, 72), (cx + 1, 72)])
    P.append(Parte(pan, TECIDO_AZ, z=3.1))
    _riscas_h(P, pan, ['#4d65b4', '#f9c22b'], 3.11, alt=2)
    P.append(Parte(retangulo(cx - 9, 58 + dy, cx + 8, 60 + dy), OURO, z=3.2, plano=True))
    # perna da frente
    P.append(Parte(capsula(cx + 4, 70, cx + 6, 91, 3.6), LIG, z=4, volume='cilindro_v'))
    pf = capsula(cx + 4, 70, cx + 6, 91, 3.6)
    listras(P, pf, '#966c6c', 4.01, lambda x, y: (y + x // 3) % 4 == 0)
    P.append(Parte(capsula(cx + 3, 93, cx + 10, 93, 1.6), OURO, z=4.1))                          # sandália
    P.append(Parte(capsula(cx - 8, 93, cx - 2, 93, 1.5), OURO_ESC, z=1.1))
    # colar largo (usekh) e escaravelho azul
    col = {p for p in elipse(cx, 34 + dy, 12, 7) if p[1] >= 33 + dy}
    P.append(Parte(col, OURO, z=5))
    _riscas_h(P, col, ['#f9c22b', '#4d65b4', '#f9c22b', '#30e1b9'], 5.01, alt=1)
    esc = elipse(cx + 1, 45 + dy, 3, 2.6)
    P.append(Parte(esc, AZUL, z=5.5))
    px(P, [(cx + 1, 43 + dy), (cx + 1, 44 + dy), (cx + 1, 45 + dy), (cx + 1, 46 + dy)], '#323353', 5.6)
    px(P, [(cx - 3, 45 + dy), (cx - 4, 44 + dy), (cx + 5, 45 + dy), (cx + 6, 44 + dy)], '#f9c22b', 5.45)  # asas do escaravelho
    # cabeça: nemes (atrás e por cima), máscara de ouro, cobra e barba
    hx, hy = cx + 2, 20 + dy
    nem = poligono([(hx - 8, hy - 9), (hx + 4, hy - 12), (hx + 10, hy - 7), (hx + 9, hy - 4), (hx + 1, hy - 4), (hx - 1, hy + 2),
                    (hx - 2, hy + 15), (hx - 13, hy + 15), (hx - 12, hy - 2)])
    P.append(Parte(nem, TECIDO_AZ, z=6))
    _riscas_h(P, nem, ['#4d65b4', '#4d65b4', '#f9c22b', '#f9c22b'], 6.01, alt=1)
    px(P, [p for p in nem if not dentro(nem, p) and p[1] < hy - 3], '#f79617', 6.02)
    masc = elipse(hx + 5, hy + 1, 6.4, 7.6)
    P.append(Parte(masc, OURO, z=7))
    # olhos que brilham azul, com o risco pintado
    ex, ey = hx + 6, hy
    px(P, [(ex - 3, ey), (ex - 2, ey - 1), (ex - 1, ey - 1), (ex, ey - 1), (ex + 1, ey - 1), (ex + 2, ey - 1), (ex + 3, ey),
           (ex - 1, ey + 2), (ex, ey + 2), (ex + 1, ey + 2), (ex + 2, ey + 2)], '#323353', 7.1)
    px(P, [(ex - 1, ey), (ex, ey), (ex + 1, ey), (ex + 2, ey), (ex - 1, ey + 1), (ex, ey + 1), (ex + 1, ey + 1), (ex + 2, ey + 1)], '#2e222f', 7.15)
    px(P, [(ex, ey), (ex + 1, ey), (ex, ey + 1), (ex + 1, ey + 1)], gl, 7.2)
    px(P, [(ex, ey)], '#ffffff', 7.21)
    px(P, [(ex - 2, ey - 3), (ex - 1, ey - 3), (ex, ey - 3), (ex + 1, ey - 3), (ex + 2, ey - 3)], '#9e4539', 7.1)   # sobrolho
    px(P, [(hx + 11, hy + 2), (hx + 11, hy + 3), (hx + 10, hy + 4)], '#f79617', 7.1)               # nariz
    px(P, [(hx + 7, hy + 6), (hx + 8, hy + 6), (hx + 9, hy + 6)], '#9e4539', 7.1)                  # boca
    P.append(Parte(capsula(hx - 1, hy - 5, hx + 9, hy - 5, 1.2), OURO, z=7.3))                     # faixa da testa
    P.append(Parte(capsula(hx + 9, hy - 5, hx + 10, hy - 11, 1.3), OURO, z=7.4))                   # cobra (uraeus)
    P.append(Parte(elipse(hx + 11, hy - 11, 1.8, 1.6), OURO, z=7.45))
    px(P, [(hx + 12, hy - 12)], '#e83b3b', 7.5)
    bar = capsula(hx + 7, hy + 8, hx + 8, hy + 15, 1.6)
    P.append(Parte(bar, TECIDO_AZ, z=7.2))
    _riscas_h(P, bar, ['#4d65b4', '#f9c22b'], 7.21, alt=1)
    # braço da frente segura o cetro-serpente
    P.append(Parte(capsula(cx + 7, 37 + dy, cx + 12, 49 + dy, 3.0), LIG, z=8))
    P.append(Parte(capsula(cx + 12, 49 + dy, cx + 18, 52 + dy, 2.6), LIG, z=8.1))
    px(P, [(cx + 10, 44 + dy), (cx + 11, 45 + dy), (cx + 12, 46 + dy)], '#f9c22b', 8.2)          # bracelete
    sx = cx + 20
    cet = capsula(sx, 26 + dy, sx, 92, 1.3)
    P.append(Parte(cet, OURO, z=7.9, volume='cilindro_v'))
    listras(P, cet, '#4d65b4', 7.91, lambda x, y: y % 6 == 0, borda=True)
    # a cobra no topo do cetro (capuz aberto, olho vermelho, língua)
    cob = curva((sx, 27 + dy), (sx - 4, 20 + dy), (sx + 1, 13 + dy), 5)
    P.append(Parte(cadeia(cob, [1.6, 1.6, 1.7, 1.8, 1.9]), OURO, z=8.3))
    capuz = elipse(sx, 16 + dy, 3.6, 4.6)
    P.append(Parte(capuz, OURO, z=8.35))
    px(P, [(sx - 1, 15 + dy), (sx - 1, 17 + dy), (sx, 19 + dy)], '#4d65b4', 8.36)
    cab_c = elipse(sx + 3, 13 + dy, 2.6, 2) | capsula(sx + 3, 13 + dy, sx + 6, 14 + dy, 1.4)
    P.append(Parte(cab_c, OURO, z=8.4))
    px(P, [(sx + 3, 12 + dy)], '#e83b3b', 8.5)
    if t in (1, 2):
        px(P, [(sx + 8, 15 + dy), (sx + 9, 14 + dy), (sx + 9, 16 + dy)], '#f04f78', 8.5)
    P.append(Parte(elipse(sx + 1, 51 + dy, 2.6, 2.6), LIG, z=8.6))                               # mão
    img = desenhar(P, 96, 96)
    # pó azul a subir dos olhos e do cetro
    sol = []
    for i in range(3):
        sol.append((ex + 4 + i * 2, ey - 2 - ((t + i) % 4) * 2, '#8fd3ff' if i % 2 else '#4d9be6'))
    sol += [(sx + 4, 8 + dy - t, '#fbff86'), (sx - 4, 22 + dy - (t + 2) % 4, '#f9c22b')]
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
    'lagarto_duna_gigante': ('guardioes', 64, lagarto),
    'esfinge_menor': ('guardioes', 64, esfinge),
    'golem_de_arenito': ('guardioes', 64, golem),
    'cavaleiro_de_ossos_montado': ('guardioes', 64, cavaleiro),
    'djinn_da_tempestade': ('guardioes', 48, djinn),
    'sacerdote_chacal': ('guardioes', 48, sacerdote),
    'a_miragem': ('guardioes', 48, miragem),
    'abutre_rei': ('guardioes', 48, abutre),
    'escorpiao_imperador': ('bosses', 64, imperador),
    'esqueleto_de_dragao_jovem': ('bosses', 64, dragao),
    'farao_eterno': ('bosses', 96, farao),
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
