"""PROPOSTA (ainda não aprovada): monstros, guardiões e bosses da região 10 (Abismo) e o Mímico, redesenhados.

Não mexe no jogo: grava só em arte/propostas/monstros/r10_abismo/ (uma tira "parado" de 4 quadros por criatura,
com o mesmo tamanho de quadro do desenho antigo) e as comparações comparar.gif / depois.gif.
Fichas: docs/regioes/r10_abismo.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (20 e 21).
Estilo: o do Ent Ancião (ferramentas/arte/ent_anciao.py): várias partes, textura, olhos com brilho, pormenores.

Correr (na raiz do repositório):  python3 ferramentas/arte/propostas/r10_abismo.py            (tudo)
                                  python3 ferramentas/arte/propostas/r10_abismo.py sombra mimico  (só alguns)
"""
import json
import math
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

SAIDA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r10_abismo')
OUT = '#2e222f'

# ---------- rampas (escuro -> claro), só Resurrect 64 ----------
NOITE = ['#2e222f', '#3e3546', '#45293f', '#6b3e75', '#905ea9']        # sombra, vazio
VAZIO = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']        # roxo do vazio
CEU = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']          # asas e pele estelar
AZUL = RAMPAS['azul']                                                  # azul do Sistema
VIDRO = RAMPAS['agua']
BRONZE = ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#fbb954']
LATAO = ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86']
OURO = RAMPAS['ouro']
FERRO = RAMPAS['ferro']
FERRO_ESC = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
MADEIRA = ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
MADEIRA_Q = ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e']   # madeira quente (relógio)
BRANCO = RAMPAS['branco']
MARFIM = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']
ROSA = RAMPAS['rosa']
LINGUA = ['#6e2727', '#ae2334', '#e83b3b', '#f68181', '#fca790']
PEDRA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
LAVA = ['#6e2727', '#b33831', '#ea4f36', '#f79617', '#fbff86']
GELO = ['#4d65b4', '#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff']
AREIA = ['#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fdcbb0']
CORAL = ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0']
CRISTAL = ['#6b3e75', '#905ea9', '#a884f3', '#eaaded', '#ffffff']
FOLHA = RAMPAS['verde']
PELE = RAMPAS['pele']
PELE_PALIDA = ['#966c6c', '#e6904e', '#fca790', '#fdcbb0', '#fdcbb0']
CABELO_BR = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
TECIDO_AZ = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
COURO = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#ab947a']

ESTRELAS = ['#ffffff', '#fbff86', '#8fd3ff']


# ---------- ajudas ----------

def _px(P, pts, cor, z):
    pts = {(int(round(x)), int(round(y))) for x, y in pts}
    if pts:
        P.append(Parte(pts, None, z=z, separar=False, cor=cor))


def _pt(P, x, y, cor, z):
    _px(P, [(x, y)], cor, z)


def borda(m):
    return {p for p in m if any((p[0] + dx, p[1] + dy) not in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))}


def olho(P, x, y, iris, z, grande=False, fechado=False, pupila=OUT):
    """Olho virado para a direita: íris, pupila do lado de onde olha e um ponto branco em cima à esquerda."""
    if fechado:
        _px(P, [(x, y + 1), (x + 1, y + 1)] + ([(x + 2, y + 1)] if grande else []), OUT, z)
        return
    if grande:
        _px(P, retangulo(x, y, x + 2, y + 2), iris, z)
        _px(P, [(x + 2, y + 1), (x + 2, y + 2), (x + 1, y + 2)], pupila, z + 0.01)
        _px(P, [(x, y)], '#ffffff', z + 0.02)
    else:
        _px(P, retangulo(x, y, x + 1, y + 1), iris, z)
        _px(P, [(x + 1, y + 1)], pupila, z + 0.01)
        _px(P, [(x, y)], '#ffffff', z + 0.02)


def brilho_olho(P, x, y, cor, z, fechado=False, larg=2):
    """Olho que brilha (criaturas do vazio): um traço de luz com um píxel branco."""
    if fechado:
        _px(P, [(x + i, y + 1) for i in range(larg)], OUT, z)
        return
    _px(P, [(x + i, y) for i in range(larg)] + [(x + i, y + 1) for i in range(larg)], cor, z)
    _px(P, [(x, y)], '#ffffff', z + 0.01)


def pintas(P, m, rampa, z, semente, dens=17, claras=True):
    """Textura (como a _folhagem do Ent): pintas escuras em baixo à direita e claras em cima à esquerda."""
    if not m:
        return
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    escuro, claro = [], []
    rnd = random.Random(semente)
    interior = m - borda(m)
    for (x, y) in interior:
        h = ((x * 73856093) ^ (y * 19349663) ^ (semente * 83492791)) % 9973 % dens
        lado = (x - cx) + (y - cy)
        if h == 0 or (h == 5 and lado > 2):
            escuro.append((x, y))
        elif claras and h == 9 and lado < -2 and rnd.random() < 0.8:
            claro.append((x, y))
    _px(P, escuro, rampa[0] if rampa[0] != OUT else rampa[1], z + 0.001)
    _px(P, claro, rampa[4], z + 0.002)


def estrelinhas(P, m, semente, n, t, z, cores=ESTRELAS):
    """Estrelas que piscam dentro de uma máscara (cada uma acende em quadros diferentes)."""
    rnd = random.Random(semente)
    inter = sorted(m - borda(m))
    if not inter:
        return
    for i in range(n):
        x, y = rnd.choice(inter)
        fase = rnd.randint(0, 3)
        cor = rnd.choice(cores)
        k = (t + fase) % 4
        if k == 0:     # estrela grande (cruz)
            _px(P, [(x, y)], '#ffffff', z + 0.01)
            _px(P, [p for p in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if p in m], cor, z)
        elif k in (1, 3):
            _px(P, [(x, y)], cor, z)


def cruz_estrela(P, x, y, z, grande=1, cor='#fbff86'):
    pts = [(x, y)]
    for i in range(1, grande + 1):
        pts += [(x - i, y), (x + i, y), (x, y - i), (x, y + i)]
    _px(P, pts, cor, z)
    _pt(P, x, y, '#ffffff', z + 0.01)


def corrente(pts, r):
    """Capsulas encadeadas por uma lista de pontos (tentáculos, caudas, fios)."""
    m = set()
    for (a, b) in zip(pts, pts[1:]):
        rr = r(pts.index(a)) if callable(r) else r
        m |= capsula(a[0], a[1], b[0], b[1], rr)
    return m


# =====================================================================================
# 32 px
# =====================================================================================

def sombra(t):
    """Sombra (32): silhueta curvada de fumo escuro, olhos brancos, sorriso torto e garras; sai de uma poça de sombra."""
    P = []
    y0 = [0, 0, 1, 1][t]
    onda = [0, 1, 2, 1][t]
    # poça de sombra no chão (de onde sai)
    poca = elipse(15, 29.6, 11, 2.2)
    P.append(Parte(poca, ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#45293f'], z=0, plano=True))
    _px(P, [(7 + (t * 3) % 10, 29), (19 - t, 30)], '#6b3e75', 0.1)
    # corpo: capuz curvado para a frente que alarga em baixo como fumo
    corpo = poligono([(9, 28), (7, 22), (8, 15), (12, 9 + y0), (17, 5 + y0), (22, 6 + y0), (24, 10 + y0),
                      (23, 15 + y0), (20, 19 + y0), (22, 24), (23, 28)])
    corpo |= elipse(18.5, 10.5 + y0, 5.2, 5.2)
    # fiapos de fumo a subir das costas (enrolam na ponta e ondulam)
    for i, (bx, by, sx, sy) in enumerate(((12, 9, -1.0, -1.5), (9, 16, -1.3, -1.0))):
        pts = [(bx + sx * k + 0.18 * k * k + math.sin(k * 0.9 + t * 1.6 + i * 2) * 0.7, by + sy * k + y0) for k in range(6)]
        corpo |= corrente(pts, lambda k: max(0.55, 1.9 - k * 0.3))
    corpo = {p for p in corpo if p[1] <= 28}
    P.append(Parte(corpo, NOITE, z=1))
    # bainha rasgada
    _px(P, [(10, 28), (13, 27), (13, 28), (17, 28), (20, 28), (21, 27)], '#2e222f', 1.2)
    pintas(P, corpo, NOITE, 1, 3, dens=11)
    # pó de estrelas roxo dentro do corpo
    estrelinhas(P, elipse(13, 21, 4.5, 5), 4 + t // 4, 3, t, 1.3, cores=['#a884f3', '#905ea9'])
    # braço da frente com mão de garras (o de trás quase não se vê)
    gx, gy = 23, 21 + y0 - onda // 2
    P.append(Parte(capsula(18, 18 + y0, gx, gy, 1.5), NOITE, z=3, volume='cilindro_h'))
    P.append(Parte(elipse(gx + 0.5, gy + 0.5, 2, 2), NOITE, z=3.1))
    _px(P, [(gx + 2, gy - 1), (gx + 3, gy - 1), (gx + 3, gy + 1), (gx + 4, gy + 2), (gx + 1, gy + 2), (gx + 2, gy + 3)], '#eaaded', 3.2)
    # cara: olhos brancos e um sorriso torto de dentinhos
    for ex in (19, 22):
        if t == 3:
            _px(P, [(ex, 10 + y0), (ex + 1, 10 + y0)], '#9babb2', 4)
        else:
            _px(P, [(ex, 9 + y0), (ex + 1, 9 + y0)], '#ffffff', 4)
            _px(P, [(ex, 10 + y0), (ex + 1, 10 + y0)], '#8fd3ff', 4)
    _px(P, [(19, 13 + y0), (20, 14 + y0), (21, 13 + y0), (22, 14 + y0), (23, 13 + y0)], '#c7dcd0', 4)
    return desenhar(P, 32, 32)


def olho_do_vazio(t):
    """Olho do Vazio (32): um olho enorme com pálpebra roxa, veias, íris violeta e tentáculos que ondulam."""
    P = []
    dy = [0, -1, -1, 0][t]
    cx, cy = 15.5, 12 + dy
    R = 9.5
    bola = elipse(cx, cy, R, R)
    # tentáculos finos (atrás da bola)
    for i, bx in enumerate((10, 14, 18, 21.5)):
        pts = []
        for k in range(6):
            yy = cy + 7 + k * 2.2
            lado = (bx - cx) * 0.12 * k
            xx = bx + lado + math.sin(k * 1.1 + t * 1.57 + i * 1.7) * (0.3 + k * 0.3)
            pts.append((xx, min(yy, 30)))
        ten = corrente(pts, lambda k: max(0.6, 1.5 - k * 0.22))
        P.append(Parte(ten, VAZIO if i % 2 else NOITE, z=0.5 + i * 0.01))
        _px(P, [(round(x) + 1, round(y)) for x, y in pts[2:5:2]], '#eaaded', 0.6 + i * 0.01)
    # três chifres pequenos atrás da pálpebra
    for (sx, sy, ex_, ey_) in ((10, 5, 7, 1.5), (14, 3.5, 13, -0.5), (18, 3.5, 19.5, 0)):
        P.append(Parte(capsula(sx, sy + dy, ex_, ey_ + dy + 1, 1.1), NOITE, z=0.4))
    P.append(Parte(bola, BRANCO, z=1))
    # veias que vêm da borda de trás
    veias = [(7, 12), (8, 12), (9, 13), (10, 13), (8, 16), (9, 16), (10, 17), (11, 17), (10, 15),
             (11, 20), (12, 19), (13, 19), (7, 9), (8, 9), (9, 10)]
    _px(P, [(x, y + dy) for x, y in veias if (x, y + dy) in bola], '#cf657f', 1.1)
    _px(P, [(x, y + dy) for x, y in ((7, 12), (8, 16), (11, 20), (7, 9))], '#c32454', 1.12)
    # íris e pupila (olha para a direita); a pupila encolhe e alarga
    ix, iy = cx + 4, cy + 0.5
    ir = elipse(ix, iy, 3.8, 4.4)
    P.append(Parte(ir, ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'], z=2))
    pr = [1.5, 1.2, 1.5, 1.9][t]
    _px(P, elipse(ix + 0.8, iy, pr * 0.8, pr + 0.7), OUT, 2.1)
    _px(P, [(int(ix - 2), int(iy - 2)), (int(ix - 1), int(iy - 2)), (int(ix - 2), int(iy - 1))], '#ffffff', 2.2)
    _px(P, [(int(ix + 2), int(iy + 2))], '#eaaded', 2.2)
    # pálpebra de cima, com a borda curva (desce para piscar no quadro 2)
    desce = 9.5 if t == 2 else 4.5
    ext = elipse(cx, cy, R + 0.8, R + 0.8)
    palp = {p for p in ext if p[1] + 0.5 < cy - R + desce + 0.05 * (p[0] + 0.5 - cx - 1) ** 2 * (0.4 if t == 2 else 1)}
    P.append(Parte(palp, VAZIO, z=3))
    pintas(P, palp, VAZIO, 3, 5, dens=19)
    return desenhar(P, 32, 32)


def relogio_vivo(t):
    """Relógio Vivo (32): relógio de pé de madeira com cara no mostrador (os ponteiros são o bigode),
    pêndulo a balançar atrás do vidro, luvas brancas e sapatos."""
    P = []
    dy = [0, 1, 0, 1][t]
    # pernas e sapatos
    for (lx, z) in ((12, 0.5), (19, 4)):
        P.append(Parte(capsula(lx, 25, lx, 28, 1.2), MADEIRA_Q, z=z, volume='cilindro_v'))
        P.append(Parte(elipse(lx + 1.5, 29.3, 2.6, 1.6), FERRO_ESC, z=z + 0.1))
    # braço de trás
    P.append(Parte(capsula(10, 14 + dy, 6, 19 + dy, 1.0), MADEIRA_Q, z=0.5))
    P.append(Parte(elipse(5.5, 19.5 + dy, 1.7, 1.7), MARFIM, z=0.6))
    # caixa (corpo) com veios de madeira
    caixa = retangulo(9, 12 + dy, 22, 26, canto=1)
    P.append(Parte(caixa, MADEIRA_Q, z=1, volume='cilindro_v'))
    _px(P, [(x, y) for (x, y) in caixa if x in (10, 21) and (y + x) % 4 != 0], '#7a3045', 1.05)
    _px(P, [(11, y) for y in range(14 + dy, 25, 3)], '#e6904e', 1.06)
    # base e frontão
    P.append(Parte(retangulo(8, 25, 23, 27), MADEIRA_Q, z=1.2, plano=True))
    cabeca = retangulo(8, 3 + dy, 23, 13 + dy, canto=1) | poligono([(8, 4 + dy), (15.5, -0.5 + dy), (24, 4 + dy)])
    P.append(Parte(cabeca, MADEIRA_Q, z=2, volume='cilindro_v'))
    _px(P, [(15, 0 + dy), (16, 0 + dy), (15, 1 + dy), (16, 1 + dy)], '#f9c22b', 2.1)   # pinha de latão no topo
    _pt(P, 15, 0 + dy, '#fbff86', 2.2)
    # janela do pêndulo
    jan = retangulo(13, 15 + dy, 18, 23 + dy)
    P.append(Parte(jan, ['#2e222f', '#323353', '#323353', '#484a77', '#4d65b4'], z=2.5, plano=True))
    ox = [-2, 0, 2, 0][t]
    _px(P, [(15.5 + ox * k / 6, 15 + dy + k) for k in range(6)], '#f9c22b', 2.6)
    P.append(Parte(elipse(15.5 + ox + 0.5, 21.5 + dy, 1.6, 1.6), LATAO, z=2.7))
    _px(P, [(14, 16 + dy), (14, 17 + dy)], '#8fd3ff', 2.8)                               # reflexo no vidro
    # mostrador: aro de latão, cara de marfim, olhos e ponteiros-bigode
    fx, fy = 15.5, 8 + dy
    P.append(Parte(elipse(fx, fy, 5.6, 5.6), LATAO, z=3))
    face = elipse(fx, fy, 4.4, 4.4)
    P.append(Parte(face, MARFIM, z=3.1))
    for a in (0,):                 # marca das 12
        ang = a / 12 * 2 * math.pi
        _pt(P, fx - 0.5 + math.sin(ang) * 3.6, fy - 0.5 - math.cos(ang) * 3.6, '#966c6c', 3.2)
    pisca = t == 3
    olho(P, 13, 5 + dy, '#4d65b4', 3.3, fechado=pisca)
    olho(P, 17, 5 + dy, '#4d65b4', 3.3, fechado=pisca)
    # ponteiros (o grande avança um tique por quadro)
    ang_m = math.radians(120 + t * 30)
    ang_h = math.radians(235)
    cxp, cyp = fx - 0.5, fy + 0.5
    _px(P, [(cxp + math.sin(ang_m) * k, cyp - math.cos(ang_m) * k) for k in (1, 2, 3)], OUT, 3.4)
    _px(P, [(cxp + math.sin(ang_h) * k, cyp - math.cos(ang_h) * k) for k in (1, 2)], OUT, 3.4)
    _pt(P, cxp, cyp, '#f9c22b', 3.5)
    # engrenagem pequena de lado
    eng = elipse(22.5, 11 + dy, 2.2, 2.2)
    P.append(Parte(eng, LATAO, z=3.6))
    _pt(P, 22, 10 + dy, OUT, 3.7)
    # braço da frente com luva branca
    P.append(Parte(capsula(22, 15 + dy, 26, 18 + dy - (t % 2), 1.0), MADEIRA_Q, z=5))
    P.append(Parte(elipse(26.5, 18.5 + dy - (t % 2), 1.8, 1.8), MARFIM, z=5.1))
    return desenhar(P, 32, 32)


def mimico(t):
    """Mímico (32): baú de madeira com cintas de ferro e fechadura de ouro; a tampa é uma boca cheia de dentes,
    olhos amarelos lá dentro, língua comprida, moedas e baba; patinhas de garra por baixo."""
    P = []
    ab = [9, 10, 11, 10][t]        # abre e fecha a boca (respira)
    hy = 19                        # bordo de cima da caixa
    # patinhas de garra
    for px_ in (9, 22):
        P.append(Parte(capsula(px_, 27, px_ - 1, 29, 1.3), NOITE, z=0.2))
        _px(P, [(px_ - 3, 30), (px_ - 1, 30), (px_ + 1, 30)], '#c7dcd0', 0.3)

    def lin(x):     # bordo de baixo da tampa (por onde abre)
        return hy - 1 - (x - 4) * ab / 23
    tampa = poligono([(4, hy), (28, lin(28) + 0.5), (27, lin(27) - 4), (8, lin(8) - 5), (3, hy - 4)])
    # interior da boca: a cunha entre a tampa e a caixa
    boca = poligono([(5, hy), (27, lin(27)), (27, hy + 1), (5, hy + 1)])
    P.append(Parte(boca, ['#2e222f', '#45293f', '#6e2727', '#6e2727', '#b33831'], z=0.5, plano=True))
    _px(P, [(x, y) for (x, y) in boca if y < lin(x) + 2.5], '#2e222f', 0.52)       # garganta escura em cima
    for ex in (18, 22):                  # olhos amarelos lá dentro
        ey = int(lin(ex + 1)) + 3
        _px(P, [(ex, ey), (ex + 1, ey), (ex, ey + 1), (ex + 1, ey + 1)], '#f9c22b', 0.8)
        _px(P, [(ex + 1, ey), (ex + 1, ey + 1)], OUT, 0.81)
        _pt(P, ex, ey, '#fbff86', 0.82)
    # caixa de baixo: tábuas com veios, cintas de ferro, rebites e fechadura
    caixa = retangulo(4, hy, 27, 27)
    P.append(Parte(caixa, MADEIRA, z=1, plano=True))
    _px(P, [(x, hy + 3) for x in range(5, 27)] + [(x, hy + 6) for x in range(5, 27)], '#694f62', 1.05)
    _px(P, [(12, hy + 1), (13, hy + 1), (19, hy + 5), (20, hy + 5), (6, hy + 5)], '#ab947a', 1.06)
    for bx in (7, 23):
        P.append(Parte(retangulo(bx, hy, bx + 1, 27), FERRO, z=1.1, plano=True))
        _px(P, [(bx, hy + 2), (bx + 1, hy + 5)], '#ffffff', 1.12)
    P.append(Parte(retangulo(14, hy, 17, hy + 4), OURO, z=1.3, plano=True))
    _px(P, [(15, hy + 2), (16, hy + 2), (15, hy + 3)], OUT, 1.31)
    # dentes de baixo (para cima)
    for x in range(6, 27, 3):
        _px(P, [(x, hy - 1), (x + 1, hy - 1), (x, hy - 2)], '#c7dcd0', 1.4)
        _pt(P, x, hy - 2, '#ffffff', 1.41)
    # tampa com uma cinta de ferro atrás e um friso de ouro na frente
    P.append(Parte(tampa, MADEIRA, z=2, volume='cilindro_h'))
    _px(P, [(x, int(lin(x) - 2.5)) for x in range(9, 26)], '#694f62', 2.05)
    P.append(Parte({p for p in tampa if 7 <= p[0] <= 8}, FERRO, z=2.1, plano=True))
    _px(P, [(26, int(lin(26)) - 1), (27, int(lin(27)) - 1), (26, int(lin(26)) - 4)], '#f9c22b', 2.15)   # cantos de ouro
    # dentes de cima (para baixo)
    for x in range(8, 26, 3):
        yb = int(lin(x + 1)) + 1
        _px(P, [(x, yb), (x + 1, yb), (x + 1, yb + 1)], '#c7dcd0', 2.2)
        _pt(P, x, yb, '#ffffff', 2.21)
    # língua: deitada no fundo da boca, sai pela frente e cai pelo lado
    wag = [0, 1, 2, 1][t]
    lng = corrente([(13, hy - 1), (20, hy - 2), (26, hy - 2), (29, hy + 1), (29, hy + 4 + wag)], 1.3)
    P.append(Parte(lng, LINGUA, z=1.5))
    _px(P, [(17, hy - 2), (21, hy - 2), (25, hy - 2)], '#831c5d', 1.51)
    # moedas e baba
    _px(P, [(9, hy - 2), (10, hy - 2)], '#f9c22b', 1.45)
    _pt(P, 9, hy - 2, '#fbff86', 1.46)
    _px(P, [(26, hy + k) for k in range(1 + (t % 2) * 2)], '#8ff8e2', 3.2)
    return desenhar(P, 32, 32)


def anjo_do_vazio(t):
    """Anjo do Vazio (32): anjo negro com asa cheia de estrelas, auréola partida, olhos brancos e lança estelar."""
    P = []
    dy = [0, -1, -1, 0][t]
    bate = [0, 1, 2, 1][t]
    PELE_V = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
    # asa de trás: penas compridas em leque (cada pena é uma cápsula), cheia de estrelas
    asa = elipse(10, 10 + dy, 4, 3.5)
    for i, (ex, ey, r) in enumerate(((4, 1, 2.0), (1, 6, 2.0), (1, 11, 1.9), (2, 16, 1.7), (6, 20, 1.5))):
        asa |= capsula(13, 11 + dy, ex, ey + dy + bate * (1 - i * 0.3), r)
    P.append(Parte(asa, CEU, z=0.5))
    pintas(P, asa, CEU, 0.5, 2, dens=13, claras=False)
    estrelinhas(P, asa, 7, 6, t, 0.6)
    # vestido escuro que acaba em ponta rasgada (flutua)
    veste = poligono([(13, 12 + dy), (20, 12 + dy), (22, 21 + dy), (21, 26 + dy), (19, 25 + dy), (17, 29 + dy),
                      (15, 25 + dy), (13, 27 + dy), (12, 21 + dy)])
    P.append(Parte(veste, NOITE, z=1, volume='cilindro_v'))
    _px(P, [(x, 18 + dy) for x in range(13, 22)], '#6b3e75', 1.1)          # cinto com uma estrela
    _pt(P, 18, 18 + dy, '#fbff86', 1.12)
    _px(P, [(15, 21 + dy), (15, 22 + dy), (19, 21 + dy), (19, 22 + dy)], '#2e222f', 1.11)  # pregas
    # cabeça escura com capuz atrás e olhos brancos à frente
    P.append(Parte(elipse(17.5, 8 + dy, 3.8, 3.8), PELE_V, z=2, luz=0.45))
    capuz = {p for p in elipse(16.5, 7.5 + dy, 4.6, 4.6) if p[0] < 17 or p[1] < 5 + dy}
    P.append(Parte(capuz, NOITE, z=2.1))
    if t == 3:
        _px(P, [(18, 8 + dy), (19, 8 + dy), (20, 8 + dy)], '#c7dcd0', 2.2)
    else:
        _px(P, [(18, 7 + dy), (20, 7 + dy)], '#ffffff', 2.2)
        _px(P, [(18, 8 + dy), (20, 8 + dy)], '#8fd3ff', 2.2)
    # auréola partida a pairar
    _px(P, [(15, 0 + dy), (16, 0 + dy), (17, 0 + dy), (18, 0 + dy), (19, 0 + dy), (14, 1 + dy), (20, 1 + dy),
            (15, 2 + dy), (16, 2 + dy)], '#8fd3ff', 2.3)
    _px(P, [(15, 0 + dy), (16, 0 + dy)], '#ffffff', 2.31)
    # lança estelar na diagonal
    P.append(Parte(capsula(9, 26 + dy, 26, 9 + dy, 0.7), ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'], z=3))
    cruz_estrela(P, 27, 8 + dy, 3.2, grande=1 + (t % 2), cor='#fbff86')
    # braço da frente a segurar a lança
    P.append(Parte(capsula(18, 13 + dy, 21, 14 + dy, 1.2), NOITE, z=3.5))
    P.append(Parte(elipse(21.5, 14.5 + dy, 1.4, 1.4), PELE_V, z=3.6))
    return desenhar(P, 32, 32)


# =====================================================================================
# humanoides de 48 e 64 px (proporções de adulto: cabeça pequena, ombros largos)
# =====================================================================================

def humanoide(P, cx, chao, k=1.0, dy=0, pele=PELE, tronco=FERRO, pernas=COURO, botas=FERRO_ESC, bracos=None,
              mao_f=(0, 0), mao_t=(0, 0), passo=0, cabeca=True, larg=1.0):
    """Corpo base virado para a direita. Devolve os pontos importantes (cabeça, ombros, mãos, anca)."""
    bracos = bracos or tronco
    s = lambda v: v * k  # noqa: E731
    pe_y = chao - s(1)
    anca = (cx, chao - s(17) + dy)
    ombro_f = (cx + s(3), chao - s(30) + dy)
    ombro_t = (cx - s(3.5), chao - s(30) + dy)
    cab = (cx + s(1), chao - s(36.5) + dy)
    # pernas (a de trás mais escura)
    for lado, z, rp in ((-1, 0.8, [pernas[0]] + pernas[:4]), (1, 2.2, pernas)):
        hx = cx + lado * s(2.6)
        jo = (hx + s(1) + (passo * lado), chao - s(9) + dy * 0.5)
        pe = (hx + s(0.5) + passo * lado * 1.5, pe_y - s(2))
        P.append(Parte(capsula(hx, anca[1], *jo, s(2.6) * larg), rp, z=z, volume='cilindro_v'))
        P.append(Parte(capsula(*jo, *pe, s(2.3) * larg), rp, z=z + 0.01, volume='cilindro_v'))
        bota = elipse(pe[0] + s(1.5), pe_y - s(1), s(3.6), s(2.4)) | capsula(pe[0], pe[1] - s(1), pe[0], pe_y - s(1), s(2.4))
        P.append(Parte(bota, botas if lado > 0 else [botas[0]] + botas[:4], z=z + 0.05))
    # tronco: ombros largos, cintura mais estreita
    tr = poligono([(cx - s(6) * larg, ombro_t[1] - s(1)), (cx + s(6.5) * larg, ombro_f[1] - s(1)), (cx + s(5) * larg, anca[1] + s(1)),
                   (cx - s(5) * larg, anca[1] + s(1))])
    tr |= elipse(cx + s(0.5), ombro_f[1] + s(1), s(6.5) * larg, s(3.5))
    P.append(Parte(tr, tronco, z=2.5, volume='cilindro_v'))
    if cabeca:
        P.append(Parte(capsula(cab[0], cab[1] + s(3), cab[0], ombro_f[1], s(1.8)), pele, z=2.6))   # pescoço
        P.append(Parte(elipse(cab[0], cab[1], s(4.4), s(4.6)), pele, z=3, luz=0.15))
    # braço de trás
    bt = bracos if isinstance(bracos, list) else RAMPAS[bracos]
    bt_esc = [bt[0]] + bt[:4]
    cot_t = (ombro_t[0] - s(2) + mao_t[0] * 0.4, ombro_t[1] + s(7) + mao_t[1] * 0.4)
    mt = (ombro_t[0] - s(1) + mao_t[0], ombro_t[1] + s(13) + mao_t[1])
    P.append(Parte(capsula(*ombro_t, *cot_t, s(2.2)), bt_esc, z=0.5))
    P.append(Parte(capsula(*cot_t, *mt, s(2.0)), bt_esc, z=0.51))
    P.append(Parte(elipse(mt[0], mt[1], s(2.1), s(2.1)), [pele[0]] + pele[:4], z=0.52))
    # braço da frente (as mãos e armas desenham-se depois por cima)
    cot_f = (ombro_f[0] + s(1.5) + mao_f[0] * 0.4, ombro_f[1] + s(7) + mao_f[1] * 0.4)
    mf = (ombro_f[0] + s(3) + mao_f[0], ombro_f[1] + s(12) + mao_f[1])
    P.append(Parte(capsula(*ombro_f, *cot_f, s(2.3)), bt, z=6))
    P.append(Parte(capsula(*cot_f, *mf, s(2.1)), bt, z=6.01))
    P.append(Parte(elipse(ombro_f[0] + s(0.3), ombro_f[1] + s(0.5), s(3), s(2.8)), bt, z=6.02))   # ombro
    return dict(anca=anca, ombro_f=ombro_f, ombro_t=ombro_t, cab=cab, mao_f=mf, mao_t=mt, cot_f=cot_f, s=s)


def mao(P, pt, pele, z, k=1.0):
    P.append(Parte(elipse(pt[0], pt[1], 2.2 * k, 2.2 * k), pele, z=z))


def porteiro_do_vazio(t):
    """Porteiro do Vazio (48): figura alta de capuz estrelado, cara de vazio com olhos de luz, chave enorme de ouro
    com uma pedra azul, molho de chaves pequenas ao cinto e manto rasgado em baixo."""
    P = []
    dy = [0, 0, 1, 1][t]
    cx, chao = 21, 47
    MANTO = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3']
    h = humanoide(P, cx, chao, dy=dy, pele=NOITE, tronco=MANTO, pernas=NOITE, botas=NOITE, cabeca=False,
                  mao_f=(2, -6), mao_t=(-1, 0))
    # manto comprido que tapa as pernas, com a bainha rasgada
    manto = poligono([(cx - 7, 17 + dy), (cx + 7, 17 + dy), (cx + 10, 44), (cx + 8, 46), (cx + 5, 44), (cx + 2, 46),
                      (cx - 1, 44), (cx - 4, 46), (cx - 7, 44), (cx - 10, 46), (cx - 11, 41)])
    P.append(Parte(manto, MANTO, z=3, volume='cilindro_v'))
    estrelinhas(P, manto, 11, 9, t, 3.1)
    pintas(P, manto, MANTO, 3, 2, dens=23, claras=False)
    for x0 in (cx - 4, cx + 2):   # pregas
        _px(P, [(x0 + (y - 28) // 6, y) for y in range(28, 44)], '#45293f', 3.05)
    # cinto com molho de chaves
    _px(P, [(x, 28 + dy) for x in range(cx - 7, cx + 8)], '#4c3e24', 3.2)
    _px(P, [(cx + 5, 29 + dy), (cx + 6, 30 + dy), (cx + 4, 31 + dy), (cx + 6, 32 + dy), (cx + 5, 33 + dy)], '#f9c22b', 3.3)
    _px(P, [(cx + 5, 29 + dy)], '#fbff86', 3.31)
    _pt(P, cx + 6, 31 + dy + (t % 2), '#9babb2', 3.32)
    # capuz alto e pontiagudo, com estrelas; a cara é vazio com dois olhos de luz
    cab = (cx + 1, 10 + dy)
    capuz = elipse(cab[0], cab[1] + 1, 6, 6.5) | poligono([(cab[0] - 6, cab[1]), (cab[0] - 3, cab[1] - 9), (cab[0] + 3, cab[1] - 5)])
    capuz |= poligono([(cab[0] - 7, cab[1] + 4), (cab[0] + 7, cab[1] + 4), (cab[0] + 9, cab[1] + 9), (cab[0] - 9, cab[1] + 9)])
    P.append(Parte(capuz, MANTO, z=4))
    estrelinhas(P, capuz, 3, 4, t, 4.1)
    cara = elipse(cab[0] + 2.5, cab[1] + 1.5, 3.4, 4)
    P.append(Parte(cara, ['#2e222f', '#2e222f', '#2e222f', '#3e3546', '#3e3546'], z=4.2, separar=False))
    if t == 2:
        _px(P, [(cab[0] + 1, cab[1] + 1), (cab[0] + 2, cab[1] + 1), (cab[0] + 4, cab[1] + 1), (cab[0] + 5, cab[1] + 1)], '#f9c22b', 4.3)
    else:
        for ex in (cab[0] + 1, cab[0] + 4):
            _px(P, [(ex, cab[1]), (ex + 1, cab[1]), (ex, cab[1] + 1), (ex + 1, cab[1] + 1)], '#f9c22b', 4.3)
            _pt(P, ex, cab[1], '#fbff86', 4.31)
    # a chave enorme (de pé, ao lado), segura pela mão da frente
    kx = cx + 12
    haste = retangulo(kx, 12 + dy, kx + 1, 44 + dy)
    P.append(Parte(haste, OURO, z=5, volume='cilindro_v'))
    anel = elipse(kx + 0.5, 7 + dy, 4.3, 4.3)
    P.append(Parte(anel - elipse(kx + 0.5, 7 + dy, 2, 2), OURO, z=5.1))
    P.append(Parte(elipse(kx + 0.5, 7 + dy, 1.7, 1.7), AZUL, z=5.2))
    _pt(P, kx, 6 + dy, '#ffffff', 5.3)
    for (bx, by) in ((kx + 2, 38), (kx + 2, 41)):        # dentes da chave
        P.append(Parte(retangulo(bx, by + dy, bx + 3, by + 1 + dy), OURO, z=5.1, plano=True))
    _px(P, [(kx, y + dy) for y in (16, 22, 28)], '#9e4539', 5.15)
    if t in (1, 2):
        cruz_estrela(P, kx - 3, 3 + dy + (t - 1) * 2, 5.4, cor='#8fd3ff')
    # mão da frente a agarrar a chave (manga larga)
    P.append(Parte(capsula(cx + 4, 19 + dy, kx - 1, 25 + dy, 2.6), MANTO, z=6.5))
    mao(P, (kx + 0.5, 25.5 + dy), NOITE, 6.6)
    return desenhar(P, 48, 48)


def o_desistente(t):
    """O Desistente (48): Jogador nº 7 777, cansado e curvado; elmo amolgado de viseira aberta, armadura velha com
    ferrugem, capa rasgada, um leque de armas às costas e a espada apoiada no chão."""
    P = []
    dy = [0, 0, 1, 1][t]
    cx, chao = 20, 47
    ARM = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
    CAPA = ['#45293f', '#6e2727', '#9e4539', '#cd683d', '#e6904e']
    # armas às costas (atrás de tudo): lança, arco, cabo de machado e punhos de espadas
    P.append(Parte(capsula(cx - 9, 40, cx + 2, 2 + dy, 0.7), MADEIRA, z=0.1))                       # lança
    _px(P, [(cx + 2, 1 + dy), (cx + 3, 0 + dy), (cx + 2, 0 + dy), (cx + 3, 1 + dy), (cx + 3, -1 + dy)], '#c7dcd0', 0.12)
    arco = {p for p in borda(elipse(cx - 9, 20 + dy, 5, 11)) if p[0] <= cx - 9}
    P.append(Parte(arco, ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], z=0.13, separar=False))
    _px(P, [(cx - 9, y + dy) for y in range(10, 31)], '#c7dcd0', 0.12)                               # corda
    P.append(Parte(capsula(cx - 4, 22 + dy, cx - 8, 6 + dy, 0.8), MADEIRA, z=0.14))                 # cabo do machado
    machado = poligono([(cx - 10, 3 + dy), (cx - 6, 5 + dy), (cx - 7, 9 + dy), (cx - 12, 9 + dy)])
    P.append(Parte(machado, FERRO, z=0.15))
    for (ex, ey) in ((cx - 2, 6), (cx - 5, 9)):                                                       # punhos de espada
        P.append(Parte(capsula(ex, ey + dy, ex + 1, ey + 6 + dy, 0.8), COURO, z=0.16))
        _px(P, [(ex - 1, ey + 6 + dy), (ex, ey + 6 + dy), (ex + 1, ey + 6 + dy), (ex + 2, ey + 6 + dy)], '#f9c22b', 0.17)
    # capa rasgada
    capa = poligono([(cx - 5, 16 + dy), (cx + 2, 16 + dy), (cx - 2, 40), (cx - 5, 38), (cx - 7, 42), (cx - 9, 37), (cx - 11, 40), (cx - 10, 26)])
    P.append(Parte(capa, CAPA, z=0.3, volume='cilindro_v'))
    _px(P, [(cx - 6, 28), (cx - 7, 33), (cx - 4, 35)], '#45293f', 0.31)
    h = humanoide(P, cx, chao, dy=dy, pele=PELE, tronco=ARM, pernas=COURO, botas=FERRO_ESC, bracos=ARM, mao_f=(1, 2))
    # armadura: placa do peito com ferrugem, cinto e saiote de tiras
    peito = elipse(cx + 1, 21 + dy, 5.5, 5)
    P.append(Parte(peito, ARM, z=2.7))
    _px(P, [(cx + 3, 21 + dy), (cx + 4, 22 + dy), (cx - 1, 24 + dy), (cx + 2, 18 + dy)], '#9e4539', 2.8)   # ferrugem
    _px(P, [(cx + 4, 19 + dy), (cx + 5, 20 + dy)], '#625565', 2.8)                                         # amolgadela
    _px(P, [(x, 28 + dy) for x in range(cx - 5, cx + 6)], '#694f62', 2.9)
    _pt(P, cx + 3, 28 + dy, '#f9c22b', 2.95)
    for x in (cx - 4, cx - 1, cx + 2):
        P.append(Parte(retangulo(x, 29 + dy, x + 2, 32 + dy), COURO, z=2.92, plano=True))
    # cabeça: elmo amolgado com a viseira levantada, cara cansada (olheiras, barba por fazer)
    cab = h['cab']
    elmo = {p for p in elipse(cab[0] - 0.5, cab[1] - 0.5, 5.2, 5) if p[1] < cab[1] - 1 or p[0] < cab[0] - 1}
    P.append(Parte(elmo, ARM, z=3.2))
    _px(P, [(cab[0] - 2, cab[1] - 4), (cab[0] - 1, cab[1] - 4)], '#625565', 3.25)                          # amolgadela
    _px(P, [(cab[0] - 2 + i, cab[1] - 6) for i in range(-2, 2)], '#9e4539', 3.25)                          # crista gasta
    _px(P, [(cab[0] - 4, cab[1] + 1), (cab[0] - 3, cab[1] - 1)], '#9e4539', 3.25)                          # ferrugem
    P.append(Parte(capsula(cab[0] - 2, cab[1] - 3, cab[0] + 4, cab[1] - 3, 1.1), ARM, z=3.4))               # viseira levantada
    _px(P, [(cab[0] + 1 + i, cab[1] - 3) for i in range(0, 4, 2)], '#3e3546', 3.41)                       # frestas
    olho(P, int(cab[0] + 1), int(cab[1] - 1), '#4d65b4', 3.5, fechado=(t == 3))
    _px(P, [(cab[0] + 1, cab[1] + 1), (cab[0] + 2, cab[1] + 1)], '#cd683d', 3.5)                           # olheiras
    _px(P, [(cab[0], cab[1] + 3), (cab[0] + 2, cab[1] + 3), (cab[0] + 1, cab[1] + 4), (cab[0] + 3, cab[1] + 4)], '#9e4539', 3.5)  # barba por fazer
    _px(P, [(cab[0] + 2, cab[1] + 2), (cab[0] + 3, cab[1] + 2)], '#7a3045', 3.51)                          # boca triste
    # escudo amolgado preso ao braço de trás
    mt = h['mao_t']
    esc = elipse(mt[0] - 2, mt[1] - 3, 4.5, 5.5)
    P.append(Parte(esc, ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], z=0.6))
    _px(P, borda(esc), '#7f708a', 0.61)
    _px(P, [(mt[0] - 2, mt[1] - 3 + j) for j in (-3, -1, 1, 3)], '#9e4539', 0.62)
    # espada com a ponta apoiada no chão
    mf = h['mao_f']
    P.append(Parte(capsula(mf[0] + 1, mf[1] + 2, mf[0] + 5, 45, 1.2), FERRO, z=5.5))
    _px(P, [(mf[0] - 1, mf[1] + 2), (mf[0] + 2, mf[1] + 1), (mf[0] + 3, mf[1] + 1), (mf[0], mf[1] + 2)], '#f9c22b', 5.6)
    _px(P, [(mf[0] + 2 + (y - mf[1] - 6) * 4 // (45 - mf[1] - 6), y) for y in range(int(mf[1]) + 6, 44, 5)], '#625565', 5.7)  # mossas
    mao(P, mf, PELE, 6.5)
    return desenhar(P, 48, 48)


def rainha_dos_espelhos(t):
    """Rainha dos Espelhos (48): figura de vidro verde-água com vestido em facetas, coroa a brilhar com uma pedra
    vermelha, espelho de mão e estilhaços a flutuar à volta."""
    P = []
    dy = [0, -1, -1, 0][t]
    cx, chao = 22, 47
    # estilhaços a pairar (atrás e à frente)
    for i, (sx, sy) in enumerate(((5, 14), (40, 10), (6, 32), (42, 30))):
        yy = sy + [0, -1, -2, -1][(t + i) % 4]
        cac = poligono([(sx, yy), (sx + 2, yy - 2), (sx + 3, yy + 1), (sx + 1, yy + 3)])
        P.append(Parte(cac, VIDRO, z=0.1 if i % 2 else 9))
        if (t + i) % 4 == 0:
            _pt(P, sx + 1, yy, '#ffffff', 9.1)
    h = humanoide(P, cx, chao, dy=dy, pele=['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2', '#ffffff'], tronco=VIDRO, pernas=VIDRO, botas=VIDRO, bracos=VIDRO,
                  mao_f=(2, -5), mao_t=(-1, 1), larg=0.8)
    # vestido de vidro em facetas (alarga até ao chão)
    vest = poligono([(cx - 4, 26 + dy), (cx + 5, 26 + dy), (cx + 12, 46), (cx - 12, 46)])
    P.append(Parte(vest, VIDRO, z=3, volume='cilindro_v'))
    for (x0, x1) in ((cx - 2, cx - 7), (cx + 2, cx + 6), (cx, cx - 1)):   # arestas das facetas
        _px(P, [(x0 + (x1 - x0) * (y - 27) / 19, y) for y in range(28 + dy, 46)], '#0b8a8f', 3.05)
    for k in range(3):                                                   # risco de brilho do vidro
        _px(P, [(cx - 7 + k + j, 40 - j * 2 + k * 0) for j in range(3)], '#ffffff' if k == 0 else '#8ff8e2', 3.1)
    _px(P, [(cx + 5, 33), (cx + 6, 35), (cx + 7, 36)], '#0b5e65', 3.06)                                    # racha
    # corpete com facetas
    _px(P, [(cx - 1, 18 + dy), (cx, 19 + dy), (cx + 1, 20 + dy)], '#ffffff', 3.2)
    _px(P, [(x, 26 + dy) for x in range(cx - 4, cx + 6)], '#30e1b9', 3.2)
    # cabeça de vidro com cabelo comprido em lâminas e a coroa
    cab = h['cab']
    cab_m = elipse(cab[0], cab[1], 4.4, 4.6)
    cabelo = elipse(cab[0] - 1.5, cab[1] - 0.5, 4.6, 4.8) | poligono([(cab[0] - 6, cab[1]), (cab[0] - 1, cab[1]), (cab[0] - 2, cab[1] + 12), (cab[0] - 7, cab[1] + 10)])
    cabelo = {p for p in cabelo if p[0] < cab[0] + 1 or p[1] < cab[1] - 2}
    P.append(Parte(cabelo, ['#0b5e65', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9'], z=3.6))
    _px(P, [(cab[0] - 4, cab[1] + 3 + j) for j in range(0, 7, 2)], '#8ff8e2', 3.61)
    olho(P, int(cab[0] + 1), int(cab[1]), '#c32454', 3.7, fechado=(t == 2))
    _px(P, [(cab[0] + 2, cab[1] + 3), (cab[0] + 3, cab[1] + 3)], '#0b5e65', 3.7)
    coroa = poligono([(cab[0] - 4, cab[1] - 4), (cab[0] + 4, cab[1] - 4), (cab[0] + 4.5, cab[1] - 9), (cab[0] + 2, cab[1] - 6.5),
                      (cab[0], cab[1] - 10), (cab[0] - 2, cab[1] - 6.5), (cab[0] - 4.5, cab[1] - 9)])
    P.append(Parte(coroa, OURO, z=3.8))
    _px(P, [(cab[0], cab[1] - 6)], '#e83b3b', 3.85)
    _pt(P, cab[0] - 1, cab[1] - 6, '#fca790', 3.86)
    brilho = [(cab[0] + 4, cab[1] - 11), (cab[0] - 4, cab[1] - 11), (cab[0], cab[1] - 12), (cab[0] + 4, cab[1] - 11)][t]
    cruz_estrela(P, brilho[0], brilho[1], 3.9, cor='#fbff86')
    # espelho de mão (moldura de prata, vidro azul a refletir)
    mf = h['mao_f']
    P.append(Parte(capsula(mf[0], mf[1], mf[0] + 2, mf[1] - 5, 0.8), FERRO, z=6.2))
    esp = elipse(mf[0] + 3, mf[1] - 9, 3, 4)
    P.append(Parte(esp, FERRO, z=6.3))
    P.append(Parte(elipse(mf[0] + 3, mf[1] - 9, 1.8, 2.8), AZUL, z=6.4))
    _px(P, [(mf[0] + 2, mf[1] - 11 + (t % 2)), (mf[0] + 3, mf[1] - 10 + (t % 2))], '#ffffff', 6.5)
    mao(P, mf, VIDRO, 6.6)
    return desenhar(P, 48, 48)


def indice_vivo(t):
    """Índice Vivo (48): livro gigante com capa azul e cantos de ouro, aberto como uma boca de páginas-dentes,
    olho grande na lombada, marcador como língua e páginas soltas a voar."""
    P = []
    dy = [0, -1, -2, -1][t]
    ab = [6, 7, 8, 7][t]
    CAPA = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
    PAG = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']
    cx, cy = 20, 31 + dy        # dobra (lombada) à esquerda; abre para a direita
    # páginas a voar atrás
    for i, (px_, py_) in enumerate(((4, 8), (40, 6), (42, 36))):
        yy = py_ + [0, -1, -2, -1][(t + i) % 4]
        fol = poligono([(px_, yy), (px_ + 4, yy - 1 + (t + i) % 2), (px_ + 5, yy + 3), (px_ + 1, yy + 4)])
        P.append(Parte(fol, PAG, z=0.1 if i == 0 else 8, plano=True))
        _px(P, [(px_ + 1, yy + 1), (px_ + 2, yy + 1), (px_ + 2, yy + 2), (px_ + 3, yy + 2)], '#4d9be6', 8.1 if i else 0.11)
    # capa de baixo (maxilar) e páginas de baixo
    capa_b = poligono([(cx - 13, cy), (cx + 16, cy + 1), (cx + 17, cy + 5), (cx - 12, cy + 6)])
    P.append(Parte(capa_b, CAPA, z=1, volume='cilindro_h'))
    pag_b = poligono([(cx - 11, cy - 1), (cx + 15, cy), (cx + 15, cy + 2), (cx - 11, cy + 2)])
    P.append(Parte(pag_b, PAG, z=1.5, plano=True))
    # boca: interior escuro entre as páginas
    boca = poligono([(cx - 10, cy - 1), (cx + 15, cy - ab - 2), (cx + 15, cy), (cx - 10, cy)])
    P.append(Parte(boca, ['#2e222f', '#2e222f', '#45293f', '#45293f', '#6b3e75'], z=1.2, plano=True))
    # marcador vermelho como língua
    lng = corrente([(cx - 2, cy - 1), (cx + 9, cy - 2), (cx + 16, cy + 1), (cx + 18, cy + 6 + (t % 2))], 1.2)
    P.append(Parte(lng, LINGUA, z=1.6))
    # páginas-dentes (em baixo e em cima)
    for x in range(cx - 6, cx + 15, 3):
        _px(P, [(x, cy - 2), (x + 1, cy - 2), (x, cy - 3)], '#ffffff', 1.7)
    capa_c = poligono([(cx - 13, cy - 2), (cx + 17, cy - ab - 4), (cx + 17, cy - ab - 9), (cx - 12, cy - 8)])
    pag_c = poligono([(cx - 10, cy - 2), (cx + 15, cy - ab - 3), (cx + 15, cy - ab - 5), (cx - 10, cy - 4)])
    P.append(Parte(pag_c, PAG, z=2, plano=True))
    for x in range(cx - 4, cx + 15, 3):
        yb = cy - 2 - (x - cx + 10) * (ab + 1) / 25
        _px(P, [(x, yb + 1), (x + 1, yb + 1), (x + 1, yb + 2)], '#ffffff', 2.1)
    P.append(Parte(capa_c, CAPA, z=3, volume='cilindro_h'))
    pintas(P, capa_c, CAPA, 3, 4, dens=19)
    # cantos e fecho de ouro, runas azuis do Sistema
    for (x, y) in ((cx + 15, cy - ab - 7), (cx + 15, cy + 3)):
        P.append(Parte(elipse(x, y, 1.8, 1.8), OURO, z=3.5))
    _px(P, [(cx + 1 + i * 3, cy - 6 - i * (ab + 1) // 8) for i in range(4)], '#8fd3ff', 3.2)
    # lombada com um olho grande
    lomb = elipse(cx - 12, cy - 3, 3.6, 6)
    P.append(Parte(lomb, CAPA, z=3.6, volume='cilindro_v'))
    P.append(Parte(elipse(cx - 2, cy - ab // 2 - 7, 4, 3.5), PAG, z=3.7))
    pis = t == 1
    if pis:
        _px(P, [(cx - 4 + i, cy - ab // 2 - 7) for i in range(5)], OUT, 3.8)
    else:
        P.append(Parte(elipse(cx - 1, cy - ab // 2 - 7, 2, 2.2), ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790'], z=3.8))
        _px(P, [(cx - 1, cy - ab // 2 - 7), (cx, cy - ab // 2 - 7)], OUT, 3.81)
        _pt(P, cx - 2, cy - ab // 2 - 8, '#ffffff', 3.82)
    _px(P, [(cx - 13, cy - 7), (cx - 13, cy - 4), (cx - 13, cy - 1)], '#f9c22b', 3.65)                   # nervuras de ouro
    return desenhar(P, 48, 48)


# =====================================================================================
# humanoides de 32 px (cabeça grande, como o herói)
# =====================================================================================

def pequeno(P, cx, cy_cab, dy, pele, roupa, calcas, botas, braco=None, mao_f=(0, 0), r_cab=5.0, chao=30):
    braco = braco or roupa
    # pernas
    for lado, z in ((-1, 0.8), (1, 2.2)):
        lx = cx + lado * 2
        rp = calcas if lado > 0 else [calcas[0]] + calcas[:4]
        P.append(Parte(capsula(lx, 22 + dy, lx, chao - 2, 1.5), rp, z=z, volume='cilindro_v'))
        P.append(Parte(elipse(lx + 1, chao - 1, 2.3, 1.4), botas if lado > 0 else [botas[0]] + botas[:4], z=z + 0.05))
    # braço de trás
    P.append(Parte(capsula(cx - 3, 16 + dy, cx - 4, 22 + dy, 1.4), [braco[0]] + braco[:4], z=0.5))
    P.append(Parte(elipse(cx - 4, 22.5 + dy, 1.4, 1.4), [pele[0]] + pele[:4], z=0.55))
    # tronco
    tr = retangulo(cx - 4, 15 + dy, cx + 4, 23 + dy, canto=1)
    P.append(Parte(tr, roupa, z=2.5, volume='cilindro_v'))
    # cabeça
    P.append(Parte(elipse(cx + 0.5, cy_cab + dy, r_cab, r_cab * 0.95), pele, z=3, luz=0.35))
    mf = (cx + 5 + mao_f[0], 20 + dy + mao_f[1])
    P.append(Parte(capsula(cx + 2, 16 + dy, mf[0], mf[1], 1.4), braco, z=6))
    return dict(mao_f=mf, cab=(cx + 0.5, cy_cab + dy), tronco=tr)


def administrador(t):
    """O Administrador, fase 1 (32): Aren, um homem cansado de cabelo branco despenteado e roupa simples, com olhos
    azuis que brilham como a janela do Sistema; espada simples e uma janelinha azul a pairar."""
    P = []
    dy = [0, 0, 1, 1][t]
    cx = 14
    CAMISA = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
    COLETE = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d65b4']
    CALCA = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
    h = pequeno(P, cx, 9, dy, ['#9e4539', '#e6904e', '#fca790', '#fdcbb0', '#fdcbb0'], CAMISA, CALCA, COURO, mao_f=(0, 0))
    # colete escuro aberto por cima da camisa
    _px(P, [p for p in h['tronco'] if p[0] <= cx - 1 or p[0] >= cx + 3], '#323353', 2.6)
    _px(P, [(cx + 1, 17 + dy), (cx + 1, 19 + dy), (cx + 1, 21 + dy)], '#7f708a', 2.6)          # botões
    _px(P, [(x, 22 + dy) for x in range(cx - 4, cx + 5)], '#45293f', 2.7)                       # cinto
    # cabelo branco despenteado (para trás e por cima)
    cab = h['cab']
    cabelo = {p for p in elipse(cab[0] - 0.5, cab[1] - 1.5, 5.8, 5) if p[1] < cab[1] - 2 or p[0] < cab[0] - 2}
    for (ex, ey) in ((-6, -3), (-3, -6.5), (1, -6.5), (-6.5, 1.5)):
        cabelo |= capsula(cab[0] - 1, cab[1] - 3, cab[0] + ex, cab[1] + ey, 1.3)
    P.append(Parte(cabelo, CABELO_BR, z=3.2))
    _px(P, [(cab[0] - 3, cab[1] - 4), (cab[0] - 1, cab[1] - 5), (cab[0] - 4, cab[1] - 1)], '#9babb2', 3.22)    # madeixas
    _px(P, [(cab[0] + 3, cab[1] - 2), (cab[0] + 4, cab[1] - 1)], '#c7dcd0', 3.25)              # franja
    # olhos azuis a brilhar (o de trás meio escondido), olheiras e boca cansada
    if t == 3:
        _px(P, [(cab[0] + 1, cab[1] + 1), (cab[0] + 2, cab[1] + 1)], '#9e4539', 3.4)
    else:
        _px(P, [(cab[0] + 1, cab[1]), (cab[0] + 1, cab[1] + 1)], '#4d9be6', 3.4)
        _pt(P, cab[0] + 1, cab[1], '#8fd3ff', 3.41)
        _pt(P, cab[0] + 4, cab[1] + 1, '#4d9be6', 3.4)
    _px(P, [(cab[0] + 1, cab[1] + 2), (cab[0] + 4, cab[1] + 2)], '#e6904e', 3.39)
    _px(P, [(cab[0] + 3, cab[1] + 4), (cab[0] + 4, cab[1] + 4)], '#9e4539', 3.4)
    # espada simples apontada para baixo e para a frente
    mf = h['mao_f']
    P.append(Parte(capsula(mf[0] + 1, mf[1] + 1, mf[0] + 9, mf[1] + 6, 0.8), FERRO, z=6.5))
    _px(P, [(mf[0], mf[1] - 1), (mf[0] + 1, mf[1]), (mf[0], mf[1] + 2)], '#966c6c', 6.6)
    P.append(Parte(elipse(mf[0], mf[1] + 0.5, 1.4, 1.4), PELE_PALIDA, z=6.7))
    # janelinha azul do Sistema a pairar
    wy = 4 + [0, -1, -1, 0][t]
    jan = retangulo(23, wy, 29, wy + 4)
    P.append(Parte(jan, AZUL, z=7, plano=True))
    _px(P, [(x, wy) for x in range(23, 30)], '#8fd3ff', 7.1)
    _px(P, [(24, wy + 2), (25, wy + 2), (27, wy + 2)], '#ffffff', 7.1)
    return desenhar(P, 32, 32)


def jogador_sem_numero(t):
    """O Jogador Sem Número (32): capuz escuro, máscara branca lisa com uma racha, cachecol azul a esvoaçar,
    espada torta e a janela azul por cima com "??"."""
    P = []
    dy = [0, 0, 1, 1][t]
    cx = 14
    MANTO = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
    h = pequeno(P, cx, 12, dy, MARFIM, MANTO, MANTO, FERRO_ESC, mao_f=(1, -1), r_cab=4.6)
    # cachecol azul que esvoaça para trás
    vento = [0, 1, 2, 1][t]
    cach = corrente([(cx - 1, 16 + dy), (cx - 6, 17 + dy + vento // 2), (cx - 10, 15 + dy + vento), (cx - 12, 18 + dy + vento)], 1.4)
    P.append(Parte(cach, TECIDO_AZ, z=0.4))
    P.append(Parte(capsula(cx - 3, 16 + dy, cx + 4, 16 + dy, 1.4), TECIDO_AZ, z=3.5))
    # capa curta
    capa = poligono([(cx - 4, 15 + dy), (cx - 1, 15 + dy), (cx - 2, 26), (cx - 7, 25)])
    P.append(Parte(capa, MANTO, z=0.6, volume='cilindro_v'))
    # capuz e máscara
    cab = h['cab']
    capuz = {p for p in elipse(cab[0] - 0.5, cab[1] - 0.5, 5.4, 5.4) if p[0] < cab[0] or p[1] < cab[1] - 3}
    capuz |= capsula(cab[0] - 3, cab[1] - 4, cab[0] - 6, cab[1] - 6, 1.2)
    P.append(Parte(capuz, MANTO, z=3.2))
    mask = elipse(cab[0] + 1.5, cab[1] + 0.5, 3.4, 4)
    P.append(Parte(mask, MARFIM, z=3.3, luz=0.2))
    if t == 3:
        _px(P, [(cab[0] + 1, cab[1]), (cab[0] + 2, cab[1]), (cab[0] + 4, cab[1])], OUT, 3.4)
    else:
        _px(P, [(cab[0] + 1, cab[1] - 1), (cab[0] + 1, cab[1]), (cab[0] + 4, cab[1] - 1), (cab[0] + 4, cab[1])], OUT, 3.4)
        _pt(P, cab[0] + 1, cab[1] - 1, '#8fd3ff', 3.41)
    _px(P, [(cab[0] + 2, cab[1] + 2), (cab[0] + 3, cab[1] + 3), (cab[0] + 2, cab[1] + 4)], '#7f708a', 3.42)  # racha
    # espada
    mf = h['mao_f']
    P.append(Parte(capsula(mf[0] + 1, mf[1] - 1, mf[0] + 8, mf[1] - 8, 0.8), FERRO, z=5.5))
    _px(P, [(mf[0] - 1, mf[1] - 1), (mf[0] + 1, mf[1] + 1)], '#f9c22b', 5.6)
    P.append(Parte(elipse(mf[0], mf[1], 1.4, 1.4), MANTO, z=6.7))
    # janela azul por cima com "??" (pisca)
    wx, wy = 9, 0
    if t != 2:
        jan = retangulo(wx, wy, wx + 11, wy + 6)
        P.append(Parte(jan, ['#323353', '#323353', '#4d65b4', '#4d9be6', '#4d9be6'], z=7, plano=True))
        for qx in (wx + 2, wx + 7):
            _px(P, [(qx, wy + 1), (qx + 1, wy + 1), (qx + 2, wy + 2), (qx + 1, wy + 3), (qx + 1, wy + 5)], '#ffffff', 7.1)
    else:
        _px(P, [(wx + 2, wy + 3), (wx + 4, wy + 2), (wx + 8, wy + 4)], '#4d9be6', 7)                # a janela falha
    return desenhar(P, 32, 32)


# =====================================================================================
# 64 px e maiores
# =====================================================================================

def _devorador(t, k, ancestral):
    """Corpo comum ao Devorador de Estrelas (64) e ao Devorador Ancestral (128, com chifres, cicatrizes e coroa)."""
    P = []
    S = 64 * k
    s = lambda v: v * k  # noqa: E731
    dy = [0, 1, 1, 0][t] * k
    ab = [0, 1, 2, 1][t]
    cx, cy = s(26), s(38) + dy
    rx, ry = s(22), s(15)
    # cauda com barbatana de nebulosa (atrás)
    cauda = capsula(cx - rx + s(4), cy - s(2), s(4), cy - s(8) + [0, 1, 2, 1][t] * k, s(4))
    P.append(Parte(cauda, NOITE, z=0.2))
    leque = poligono([(s(6), cy - s(8)), (s(1), cy - s(18) + ab * k), (s(4), cy - s(9)), (s(1), cy + s(1) - ab * k)])
    P.append(Parte(leque, VAZIO, z=0.3))
    pintas(P, leque, VAZIO, 0.3, 9, dens=7)
    # barbatanas de baixo (a de trás mais escura), com garras
    for (fx, z, rp) in ((cx - s(8), 0.4, NOITE), (cx + s(8), 5, NOITE)):
        fin = capsula(fx, cy + s(9), fx - s(9), cy + s(16) + [0, 1, 1, 0][t] * k, s(2.6))
        P.append(Parte(fin, rp, z=z))
        _px(P, [(fx - s(11), cy + s(18)), (fx - s(9), cy + s(19)), (fx - s(7), cy + s(19))], '#c7dcd0', z + 0.01)
    # corpo com a cabeça à frente
    corpo = elipse(cx, cy, rx, ry) | elipse(cx + s(20), cy + s(1), s(11), s(11.5))
    corpo = {p for p in corpo if p[0] < S - 1}
    # barriga roxa mais clara com sulcos
    barriga = {p for p in corpo if p[1] > cy + s(5) + (p[0] - cx) * 0.15}
    P.append(Parte(barriga, VAZIO, z=1.1, separar=False))
    _px(P, [(x, y) for (x, y) in barriga if (y - int(cy)) % (3 * k) == 0 and x % 2 == 0], '#6b3e75', 1.15)
    # pele com estrelas e nebulosas
    pele = corpo - barriga
    pintas(P, pele, NOITE, 1, 3, dens=31)
    estrelinhas(P, pele, 5, 10 * k, t, 1.2)
    # espinhos de cristal nas costas
    for i in range(5):
        bx = cx - s(14) + i * s(6)
        by = cy - math.sqrt(max(0, 1 - ((bx - cx) / rx) ** 2)) * ry + s(2)
        h = s(5 + (i % 2) * 3 + (3 if ancestral else 0))
        P.append(Parte(poligono([(bx - s(2.5), by + s(1)), (bx + s(0.5), by - h), (bx + s(2.5), by + s(1))]), CRISTAL, z=0.9))
    # boca enorme aberta à frente com o redemoinho de luz a ser sugado
    mx, my = cx + s(14), cy + s(3)
    aber = s(4 + ab)
    boca = poligono([(mx - s(2), my), (S, my - aber - s(3)), (S, my + aber + s(1)), (mx - s(2), my + s(1))])
    boca = {p for p in boca if p in corpo}
    P.append(Parte(boca, ['#2e222f', '#2e222f', '#2e222f', '#45293f', '#45293f'], z=2, separar=False, plano=True))
    for i, (r, c) in enumerate(((5.5, '#45293f'), (4, '#6b3e75'), (2.6, '#a884f3'), (1.3, '#eaaded'))):
        _px(P, {p for p in elipse(mx + s(9), my, s(r) * 0.8, s(r)) if p in boca}, c, 2.1 + i * 0.01)
    _px(P, [(mx + s(9), my)], '#ffffff', 2.2)
    # estrelas a serem sugadas (vêm de fora para a boca)
    for i in range(3 + 2 * k):
        d = ((t + i * 2) % 6) / 6
        ang = i * 1.9
        x0, y0 = mx + s(6) + math.cos(ang) * s(20) * (1 - d), my + math.sin(ang) * s(14) * (1 - d)
        _px(P, [(x0, y0)], '#fbff86' if i % 2 else '#ffffff', 9)
        _px(P, [(x0 + math.cos(ang) * s(1.5), y0 + math.sin(ang) * s(1.5))], '#8fd3ff', 8.9)
    # dentes
    for i in range(5):
        x = mx + s(2) + i * s(3.5)
        ys = my - (aber + s(3)) * (x - mx + s(2)) / (S - mx + s(2))
        P.append(Parte(poligono([(x, ys - s(0.5)), (x + s(2.4), ys - s(0.5)), (x + s(1.2), ys + s(2.5))]), MARFIM, z=2.5))
        yi = my + s(1) + (aber) * (x - mx + s(2)) / (S - mx + s(2))
        P.append(Parte(poligono([(x, yi + s(0.5)), (x + s(2.4), yi + s(0.5)), (x + s(1.2), yi - s(2.2))]), MARFIM, z=2.5))
    # olhos pequenos, amarelos e brilhantes por cima da boca
    for (ex, ey) in ((cx + s(17), cy - s(6)), (cx + s(22), cy - s(4))):
        if t == 3:
            _px(P, [(ex + i, ey + s(1)) for i in range(int(s(2)) + 1)], '#2e222f', 3)
        else:
            _px(P, elipse(ex + s(0.5), ey + s(0.5), s(1.4), s(1.4)), '#f9c22b', 3)
            _px(P, [(ex, ey)], '#ffffff', 3.1)
            _px(P, [(ex + s(1), ey + s(1))], '#9e4539', 3.1)
    if ancestral:
        # chifres curvos, cicatrizes de luz e uma coroa de estrelas presas
        for (hx, hy, ex, ey) in ((cx + 22, cy - 22, cx + 4, cy - 50), (cx + 38, cy - 16, cx + 36, cy - 46)):
            pts = [(hx + (ex - hx) * j / 6 + math.sin(j / 6 * math.pi) * 6, hy + (ey - hy) * j / 6) for j in range(7)]
            P.append(Parte(corrente(pts, lambda j: max(1.4, 5 - j * 0.6)), MARFIM, z=1.5))
            _px(P, [(int(x) + 1, int(y)) for x, y in pts[1:6]], '#966c6c', 1.55)
        for (a, b_) in (((cx - 20, cy - 4), (cx - 6, cy + 4)), ((cx + 2, cy - 18), (cx + 8, cy - 6)), ((cx - 10, cy - 20), (cx - 18, cy - 10))):
            _px(P, [(a[0] + (b_[0] - a[0]) * j / 12, a[1] + (b_[1] - a[1]) * j / 12 + (j % 3 == 0)) for j in range(13)], '#a884f3', 1.3)
            _px(P, [(a[0] + (b_[0] - a[0]) * j / 12, a[1] + (b_[1] - a[1]) * j / 12) for j in range(4, 9)], '#eaaded', 1.31)
        for i in range(5):     # estrelas apanhadas a orbitar a cabeça
            ang = i * 1.25 + t * 0.4
            cruz_estrela(P, cx + 10 + math.cos(ang) * 30, cy - 36 + math.sin(ang) * 8, 9.5, grande=1 + (i + t) % 2,
                         cor=['#fbff86', '#8fd3ff'][i % 2])
    return desenhar(P, S, S)


def devorador_de_estrelas(t):
    """Devorador de Estrelas (64): criatura enorme e escura com pele de céu estrelado, espinhos de cristal, barriga
    roxa, boca gigante onde a luz é sugada num redemoinho, olhos pequenos amarelos e garras."""
    return _devorador(t, 1, False)


def devorador_ancestral(t):
    """Devorador Ancestral (128): o mesmo devorador, gigante e velho: chifres de marfim, cicatrizes de luz e as
    estrelas do céu do andar presas à volta da cabeça."""
    return _devorador(t, 2, True)


def baleia_estelar(t):
    """Baleia Estelar (64): baleia azul feita de constelações (estrelas ligadas por linhas de luz), barriga
    rosada com sulcos, nebulosas nas costas e cauda erguida que deixa pó de estrelas."""
    P = []
    dy = [0, -1, -1, 0][t]
    fl = [0, -1, -2, -1][t]
    AZB = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
    BAR = ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0']
    cx, cy = 33, 40 + dy
    corpo = elipse(cx, cy, 23, 11) | elipse(cx + 13, cy - 1, 12, 11)
    corpo = {p for p in corpo if p[0] < 63}
    # cauda: pedúnculo e barbatana erguida (atrás)
    ped = capsula(cx - 18, cy - 1, 9, cy - 9 + fl, 5) | capsula(9, cy - 9 + fl, 6, cy - 15 + fl, 3)
    P.append(Parte(ped, AZB, z=0.5))
    fluke = poligono([(6, cy - 14 + fl), (0, cy - 24 + fl * 2), (5, cy - 19 + fl), (11, cy - 26 + fl * 2), (9, cy - 15 + fl)])
    P.append(Parte(fluke, AZB, z=0.6))
    # barbatana de trás
    P.append(Parte(capsula(cx + 2, cy + 5, cx - 6, cy + 14 - fl, 2.5), ['#2e222f'] + AZB[:4], z=0.4))
    P.append(Parte(corpo, AZB, z=1))
    # barriga com sulcos
    bar = {p for p in corpo if p[1] > cy + 3 - (p[0] - cx) * 0.08}
    P.append(Parte(bar, BAR, z=1.1, separar=False))
    _px(P, [(x, y) for (x, y) in bar if (y - int(cy)) % 2 == 0 and x > cx - 14], '#a24b6f', 1.15)
    # nebulosas e constelações nas costas
    nebu = {p for p in elipse(cx - 6, cy - 6, 9, 3.5) | elipse(cx + 12, cy - 9, 6, 3) if p in corpo and p not in bar}
    _px(P, [p for p in nebu if ((p[0] * 7) ^ (p[1] * 13)) % 3 == 0], '#484a77', 1.2)
    _px(P, [p for p in nebu if ((p[0] * 31) ^ (p[1] * 17)) % 7 == 0], '#905ea9', 1.21)
    _px(P, [p for p in nebu if ((p[0] * 11) ^ (p[1] * 29)) % 13 == 0], '#a884f3', 1.22)
    const = [((cx - 16, cy - 4), (cx - 9, cy - 8), (cx - 2, cy - 6), (cx + 4, cy - 10)),
             ((cx + 8, cy - 4), (cx + 14, cy - 7), (cx + 20, cy - 5), (cx + 16, cy - 1))]
    for i, linha in enumerate(const):
        for a, b_ in zip(linha, linha[1:]):
            n = int(max(abs(b_[0] - a[0]), abs(b_[1] - a[1])))
            _px(P, [(a[0] + (b_[0] - a[0]) * j / n, a[1] + (b_[1] - a[1]) * j / n) for j in range(n + 1)], '#4d9be6', 1.3)
        for j, (sx, sy) in enumerate(linha):
            if (j + t + i) % 4 == 0:
                cruz_estrela(P, sx, sy, 1.4, cor='#8fd3ff')
            else:
                _pt(P, sx, sy, '#ffffff', 1.4)
    # olho, boca e pregas da garganta
    ex, ey = cx + 17, cy + 1
    if t == 2:
        _px(P, [(ex, ey + 1), (ex + 1, ey + 1), (ex + 2, ey + 1)], OUT, 2)
    else:
        olho(P, ex, ey, '#323353', 2, grande=True, pupila='#2e222f')
    _px(P, [(x, cy + 4 + (x - cx - 14) // 6) for x in range(cx + 12, 62)], '#2e222f', 2.1)
    # barbatana da frente
    P.append(Parte(capsula(cx + 11, cy + 5, cx - 3, cy + 10 - fl, 2.6), AZB, z=3))
    _px(P, [(cx + 1, cy + 9 - fl), (cx + 4, cy + 8 - fl)], '#8fd3ff', 3.1)
    # pó de estrelas a sair da cauda
    for i in range(6):
        d = (t + i) % 4
        _pt(P, 4 + i * 3 - d, cy - 26 - (i % 3) * 3 + d * 2 + fl, ['#ffffff', '#fbff86', '#8fd3ff'][i % 3], 4)
    # jato de estrelas por cima da cabeça (respira)
    if t in (1, 2):
        for j in range(3):
            _pt(P, cx + 11 + j - 1, cy - 13 - j * 2 - (t - 1) * 2, ['#8fd3ff', '#ffffff', '#fbff86'][j], 4)
    return desenhar(P, 64, 64)


def fragmento_de_mundo(t):
    """Fragmento de Mundo (64): golem feito de pedaços de todos os biomas: perna de gelo, perna de areia, tronco de
    pedra com relva, braço de lava, braço de cristal, cabeça de coral; um núcleo no peito muda de elemento."""
    P = []
    dy = [0, 0, 1, 1][t]
    cx = 30
    # perna de trás: areia (com riscas de duna)
    pa = poligono([(cx - 10, 42 + dy), (cx - 2, 42 + dy), (cx - 3, 60), (cx - 12, 60)])
    P.append(Parte(pa, AREIA, z=0.5, volume='cilindro_v'))
    _px(P, [(x, 47 + (x % 4 == 0)) for x in range(cx - 10, cx - 3)] + [(x, 53 + (x % 3 == 0)) for x in range(cx - 11, cx - 3)], '#cd683d', 0.55)
    P.append(Parte(retangulo(cx - 13, 59, cx - 2, 62), AREIA, z=0.6, plano=True))
    # braço de trás: cristal roxo com pontas
    br = capsula(cx - 10, 24 + dy, cx - 16, 40 + dy, 4)
    P.append(Parte(br, CRISTAL, z=0.4))
    for (a, b_) in (((cx - 14, 30), (cx - 21, 26)), ((cx - 15, 36), (cx - 22, 37)), ((cx - 12, 26), (cx - 15, 19))):
        P.append(Parte(poligono([(a[0] - 2, a[1] + dy), (b_[0], b_[1] + dy), (a[0] + 2, a[1] + 2 + dy)]), CRISTAL, z=0.35))
    P.append(Parte(elipse(cx - 17, 42 + dy, 4.5, 4), CRISTAL, z=0.45))
    # tronco de pedra
    tr = poligono([(cx - 13, 22 + dy), (cx + 11, 20 + dy), (cx + 14, 30 + dy), (cx + 9, 45 + dy), (cx - 11, 46 + dy), (cx - 15, 33 + dy)])
    P.append(Parte(tr, PEDRA, z=2))
    pintas(P, tr, PEDRA, 2, 6, dens=11)
    for (a, b_) in (((cx - 8, 30), (cx - 3, 38)), ((cx + 6, 36), (cx + 9, 42)), ((cx - 10, 40), (cx - 5, 43))):   # rachas
        _px(P, [(a[0] + (b_[0] - a[0]) * j / 6, a[1] + dy + (b_[1] - a[1]) * j / 6 + (j % 2)) for j in range(7)], '#3e3546', 2.1)
    # costas de areia (corcunda)
    corc = {p for p in elipse(cx - 11, 28 + dy, 6, 7) if p[0] < cx - 9}
    P.append(Parte(corc, AREIA, z=2.05))
    # relva e flores nos ombros
    relva = {p for p in tr if p[1] <= 24 + dy + (1 if p[0] % 3 == 0 else 0)}
    relva |= {(x, 19 + dy - (x % 2) - (x % 5 == 0)) for x in range(cx - 10, cx + 11)}
    P.append(Parte(relva, FOLHA, z=2.2))
    _px(P, [(cx - 6, 18 + dy), (cx + 5, 17 + dy)], '#f04f78', 2.3)
    _px(P, [(cx + 1, 18 + dy)], '#fbff86', 2.3)
    # núcleo no peito: muda de elemento a cada quadro
    nuc = [LAVA, GELO, OURO, FOLHA][t]
    P.append(Parte(poligono([(cx + 2, 28 + dy), (cx + 6, 31 + dy), (cx + 2, 36 + dy), (cx - 2, 31 + dy)]), nuc, z=2.5))
    _pt(P, cx + 1, 30 + dy, '#ffffff', 2.6)
    # cabeça de coral com ramos
    cab = elipse(cx + 8, 15 + dy, 6.5, 5.5)
    for (a, b_) in (((cx + 5, 11), (cx + 2, 3)), ((cx + 9, 10), (cx + 11, 2)), ((cx + 3, 6), (cx - 1, 4)), ((cx + 10, 5), (cx + 15, 4))):
        P.append(Parte(capsula(a[0], a[1] + dy, b_[0], b_[1] + dy, 1.4), CORAL, z=2.7))
    P.append(Parte(cab, CORAL, z=3))
    pintas(P, cab, CORAL, 3, 2, dens=7)
    for ex in (cx + 9, cx + 12):
        brilho_olho(P, ex, 14 + dy, '#30e1b9', 3.1, fechado=(t == 3), larg=2)
    _px(P, [(cx + 10, 18 + dy), (cx + 11, 18 + dy), (cx + 12, 18 + dy)], '#831c5d', 3.1)
    # perna da frente: gelo (com reflexos e geada)
    pg = poligono([(cx + 1, 43 + dy), (cx + 10, 42 + dy), (cx + 11, 60), (cx + 1, 60)])
    P.append(Parte(pg, GELO, z=4, volume='cilindro_v'))
    _px(P, [(cx + 3, 46 + j) for j in range(0, 10, 2)] + [(cx + 4, 47 + j) for j in range(0, 10, 3)], '#ffffff', 4.1)
    P.append(Parte(retangulo(cx, 59, cx + 13, 62), GELO, z=4.2, plano=True))
    # braço da frente: rocha negra com fendas de lava e um punho enorme
    om = (cx + 12, 25 + dy)
    mo = (cx + 20, 44 + dy - (t % 2))
    P.append(Parte(capsula(*om, cx + 18, 34 + dy, 4.5), ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a'], z=5))
    P.append(Parte(capsula(cx + 18, 34 + dy, *mo, 4), ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a'], z=5.1))
    P.append(Parte(elipse(mo[0] + 1, mo[1] + 3, 6, 5.5), ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a'], z=5.2))
    fendas = [(cx + 14, 27), (cx + 15, 28), (cx + 16, 30), (cx + 17, 33), (cx + 18, 35), (cx + 19, 38), (cx + 18, 39),
              (cx + 19, 44), (cx + 20, 45), (cx + 22, 46), (cx + 17, 46)]
    lava_c = ['#f79617', '#fbff86', '#f79617', '#ea4f36'][t]
    _px(P, [(x, y + dy) for x, y in fendas], lava_c, 5.3)
    _px(P, [(x + 1, y + dy) for x, y in fendas[::3]], '#ea4f36', 5.29)
    if t in (1, 2):
        _pt(P, mo[0] + 4, mo[1] - 4 - t, '#f79617', 5.4)          # brasa a subir
    return desenhar(P, 64, 64)


def eco_dos_guardioes(t):
    """Eco dos Guardiões (64): espectro azul-pálido com cauda de fumo, máscara rachada e três máscaras de guardiões
    antigos a girar à volta (coroa de ouro, máscara de folhas, crânio de chifres); um contorno-eco repete-o."""
    P = []
    dy = [0, -1, -2, -1][t]
    onda = [0, 1, 2, 1][t]
    FANT = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
    cx = 30
    # corpo: capuz largo que acaba numa cauda de fumo enrolada
    corpo = elipse(cx, 24 + dy, 12, 13) | poligono([(cx - 12, 24 + dy), (cx + 12, 24 + dy), (cx + 8, 44 + dy), (cx - 6, 50 + dy)])
    corpo |= poligono([(cx - 10, 18 + dy), (cx - 12, 3 + dy + onda // 2), (cx + 2, 12 + dy)])       # ponta do capuz
    onda = [0, 1, 2, 1][t]
    cauda = corrente([(cx, 44 + dy), (cx - 6, 52 + dy), (cx - 2 + onda, 58), (cx + 6 + onda, 60), (cx + 10 + onda, 57)],
                     lambda j: max(1.2, 6 - j * 1.3))
    corpo |= cauda
    # o eco: uma cópia do contorno, deslocada, que se desfaz
    eco = {(x - 3 - (t % 2), y - 1) for (x, y) in corpo} - corpo
    _px(P, [p for p in eco if (p[0] + p[1] + t) % 2 == 0], '#484a77', 0.1)
    P.append(Parte(corpo, FANT, z=1))
    pintas(P, corpo, FANT, 1, 8, dens=53)
    for j in range(4):   # fiapos claros na cauda
        _pt(P, cx - 4 + j * 4 + onda, 52 + (j % 2) * 3 + (dy if j < 2 else 0), '#8fd3ff', 1.1)
    # interior escuro do capuz e a máscara rachada
    P.append(Parte(elipse(cx + 4, 22 + dy, 7, 8), ['#2e222f', '#2e222f', '#323353', '#323353', '#323353'], z=1.5, separar=False, plano=True))
    masc = elipse(cx + 5.5, 22 + dy, 4.6, 5.8)
    P.append(Parte(masc, BRANCO, z=2, luz=-0.1))
    for ex in (cx + 3, cx + 7):
        if t == 1:
            _px(P, [(ex, 21 + dy), (ex + 1, 21 + dy)], OUT, 2.1)
        else:
            _px(P, retangulo(ex, 19 + dy, ex + 1, 22 + dy), OUT, 2.1)
            _px(P, [(ex + 1, 20 + dy), (ex + 1, 21 + dy)], '#4d9be6', 2.2)
            _pt(P, ex + 1, 20 + dy, '#8fd3ff', 2.25)
    _px(P, [(cx + 6, 17 + dy), (cx + 7, 18 + dy), (cx + 6, 19 + dy), (cx + 7, 20 + dy)], '#7f708a', 2.15)     # racha
    _px(P, [(cx + 5, 25 + dy), (cx + 6, 26 + dy), (cx + 7, 25 + dy), (cx + 8, 26 + dy)], '#7f708a', 2.15)      # boca
    # braços finos de fumo com mãos de três dedos
    for (ox, z, lado) in ((cx - 9, 0.5, -1), (cx + 10, 3, 1)):
        m = (ox + lado * 7, 36 + dy - (t % 2) * lado)
        P.append(Parte(capsula(ox, 28 + dy, *m, 2.2), FANT, z=z))
        for f in (-2, 0, 2):
            P.append(Parte(capsula(m[0], m[1], m[0] + lado * 2 + f * 0.3, m[1] + 3 + abs(f) * 0.3, 0.8), FANT, z=z + 0.01))
    # as três máscaras dos guardiões antigos a girar
    for i in range(3):
        ang = t * math.pi / 2 + i * 2 * math.pi / 3
        mx, my = cx + 2 + math.cos(ang) * 22, 22 + dy + math.sin(ang) * 6
        z = 4 if math.sin(ang) > 0 else 0.05
        if i == 0:     # coroa de ouro
            P.append(Parte(poligono([(mx - 4, my + 2), (mx - 4, my - 3), (mx - 2, my - 1), (mx, my - 4), (mx + 2, my - 1), (mx + 4, my - 3), (mx + 4, my + 2)]), OURO, z=z))
            _pt(P, mx, my, '#e83b3b', z + 0.01)
        elif i == 1:   # máscara de folhas (o Ent)
            P.append(Parte(elipse(mx, my, 3.5, 4), FOLHA, z=z))
            _px(P, [(mx - 1, my - 1), (mx + 1, my - 1)], '#2e222f', z + 0.01)
            _px(P, [(mx - 3, my - 4), (mx + 3, my - 4)], '#91db69', z + 0.01)
        else:          # crânio de chifres
            P.append(Parte(elipse(mx, my, 3.4, 3.4), MARFIM, z=z))
            P.append(Parte(capsula(mx - 2, my - 2, mx - 5, my - 6, 1), ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'], z=z))
            P.append(Parte(capsula(mx + 2, my - 2, mx + 5, my - 6, 1), ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'], z=z))
            _px(P, [(mx - 1, my), (mx + 1, my)], '#2e222f', z + 0.01)
    return desenhar(P, 64, 64)


def gigante_invertido(t):
    """Gigante Invertido (64): um gigante de cabeça para baixo, a andar com as mãos no chão e os pés no "céu":
    roupa azul, cinto com fivela, cabelo e barba a cair para cima, pedras a cair ao contrário à volta."""
    P = []
    dy = [0, 1, 1, 0][t]
    cx = 30
    ROUPA = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
    CALCA = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
    PELE_G = ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0']
    CAB = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
    # pernas no ar (a de trás mais escura), botas no topo
    for (lx, z, rp, ab_) in ((cx - 5, 0.5, [CALCA[0]] + CALCA[:4], -3), (cx + 4, 2, CALCA, 3)):
        joelho = (lx + ab_, 13 + dy)
        P.append(Parte(capsula(lx, 26 + dy, *joelho, 4), rp, z=z, volume='cilindro_v'))
        P.append(Parte(capsula(*joelho, lx + ab_ * 1.5, 4 + dy, 3.6), rp, z=z + 0.01, volume='cilindro_v'))
        bota = elipse(lx + ab_ * 1.5 + 1.5, 3 + dy, 5, 3)
        P.append(Parte(bota, MADEIRA if z > 1 else [MADEIRA[0]] + MADEIRA[:4], z=z + 0.02))
        _px(P, [(lx + ab_ * 1.5 - 2 + i, 1 + dy) for i in range(0, 7, 2)], '#4c3e24', z + 0.03)       # sola
    # tronco de cabeça para baixo (ombros em baixo)
    tr = poligono([(cx - 9, 25 + dy), (cx + 8, 25 + dy), (cx + 11, 44), (cx - 11, 44)])
    P.append(Parte(tr, ROUPA, z=3, volume='cilindro_v'))
    _px(P, [(x, y) for (x, y) in tr if (x + y) % 9 == 0 and y > 30], '#323353', 3.05)      # remendos/pregas
    P.append(Parte(retangulo(cx - 9, 26 + dy, cx + 8, 29 + dy), COURO, z=3.1, plano=True))  # cinto
    P.append(Parte(retangulo(cx - 1, 26 + dy, cx + 2, 29 + dy), OURO, z=3.2, plano=True))
    _pt(P, cx, 27 + dy, OUT, 3.3)
    # cabeça de pernas para o ar entre os braços; cabelo e barba "caem" para cima
    hx, hy = cx + 1, 51
    cabelo = elipse(hx - 1, hy + 4, 6.5, 4)
    P.append(Parte(cabelo, CAB, z=3.5))
    P.append(Parte(elipse(hx, hy, 6, 6), PELE_G, z=3.6, luz=0.15))
    barba = poligono([(hx - 2, hy - 3), (hx + 7, hy - 3), (hx + 6, hy - 9), (hx + 3, hy - 7), (hx + 1, hy - 10)])
    P.append(Parte(barba, CAB, z=3.7))
    pintas(P, barba, CAB, 3.7, 5, dens=5)
    # cara invertida: olhos por baixo da boca (o gigante está ao contrário)
    olho(P, hx + 2, hy + 1, '#4d65b4', 3.8, fechado=(t == 2))
    _px(P, [(hx + 2, hy + 3), (hx + 3, hy + 3), (hx + 4, hy + 3)], '#9e4539', 3.75)                # sobrolho por baixo
    _px(P, [(hx + 5, hy - 1), (hx + 6, hy - 1), (hx + 6, hy)], '#cd683d', 3.8)                      # nariz
    _px(P, [(hx + 2, hy - 3), (hx + 3, hy - 3), (hx + 4, hy - 3)], '#6e2727', 3.9)                  # boca
    P.append(Parte(elipse(hx - 4, hy, 1.6, 2), PELE_G, z=3.85))                                    # orelha
    # braços: descem até ao chão, abertos, com as mãos enormes apoiadas
    for (sx, z, mx, rp) in ((cx - 9, 0.8, cx - 19, [ROUPA[0]] + ROUPA[:4]), (cx + 9, 5, cx + 20, ROUPA)):
        cot = (sx + (mx - sx) * 0.6, 51 + dy * 0.5)
        pl = PELE_G if z > 1 else [PELE_G[0]] + PELE_G[:4]
        P.append(Parte(capsula(sx, 39, *cot, 4.2), rp, z=z, volume='cilindro_v'))
        P.append(Parte(capsula(*cot, mx, 57, 3.4), pl, z=z + 0.01))
        P.append(Parte(elipse(mx, 59.5, 4.5, 3), pl, z=z + 0.02))
        for f in range(4):   # dedos abertos no chão
            P.append(Parte(capsula(mx - 3 + f * 2.2, 60, mx - 4 + f * 2.8, 62, 1.1), pl, z=z + 0.03))
    # pedras a cair para cima
    for i, (px_, py_) in enumerate(((8, 50), (52, 44), (12, 30), (56, 20))):
        yy = py_ - ((t + i) % 4) * 3
        P.append(Parte(elipse(px_, yy, 2.2, 1.8), PEDRA, z=6))
        _pt(P, px_, yy + 3, '#7f708a', 6)
    return desenhar(P, 64, 64)


def _asa(P, raiz, penas, rampa, z, semente, t, estrelas=6):
    """Asa de penas compridas (cada pena é uma cápsula da raiz até à ponta), com estrelas."""
    asa = set()
    for (ex, ey, r) in penas:
        asa |= capsula(raiz[0], raiz[1], ex, ey, r)
    P.append(Parte(asa, rampa, z=z))
    for (ex, ey, r) in penas[1:]:
        _px(P, [(raiz[0] + (ex - raiz[0]) * j / 8, raiz[1] + (ey - raiz[1]) * j / 8 + r * 0.8) for j in range(4, 8)], rampa[0], z + 0.001)
    estrelinhas(P, asa, semente, estrelas, t, z + 0.002)
    return asa


def o_guardiao_da_escada(t):
    """O Guardião da Escada (64): anjo do vazio enorme de armadura roxa-escura, quatro asas cheias de estrelas,
    elmo com fresta de luz, auréola dourada e uma espada estelar de ouro."""
    P = []
    dy = [0, -1, -1, 0][t]
    bate = [0, 1, 2, 1][t]
    ARMV = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3']
    cx, chao = 30, 63
    # quatro asas (as de trás mais escuras)
    _asa(P, (cx - 4, 20 + dy), [(cx - 26, 2 + dy - bate, 2.6), (cx - 29, 10 + dy - bate, 2.6), (cx - 28, 18 + dy - bate // 2, 2.3)],
         ['#2e222f', '#2e222f', '#323353', '#484a77', '#4d65b4'], 0.05, 3, t, 4)
    _asa(P, (cx - 4, 30 + dy), [(cx - 24, 36 + dy + bate // 2, 2.3), (cx - 22, 43 + dy + bate, 2.2), (cx - 17, 48 + dy + bate, 2)],
         ['#2e222f', '#2e222f', '#323353', '#484a77', '#4d65b4'], 0.06, 4, t, 3)
    _asa(P, (cx - 2, 21 + dy), [(cx - 20, 0 + dy - bate, 2.8), (cx - 25, 7 + dy - bate, 2.8), (cx - 24, 15 + dy - bate // 2, 2.5),
                                (cx - 20, 22 + dy, 2.3)], CEU, 0.2, 5, t, 6)
    _asa(P, (cx - 2, 31 + dy), [(cx - 19, 34 + dy + bate // 2, 2.4), (cx - 17, 41 + dy + bate, 2.2), (cx - 12, 45 + dy + bate, 2)],
         CEU, 0.25, 6, t, 4)
    h = humanoide(P, cx, chao, k=1.32, dy=dy, pele=ARMV, tronco=ARMV, pernas=ARMV, botas=FERRO_ESC, bracos=ARMV,
                  mao_f=(3, -4), cabeca=False)
    # saiote de placas e cinto com estrela
    for i, x in enumerate(range(cx - 7, cx + 7, 4)):
        P.append(Parte(poligono([(x, 40 + dy), (x + 4, 40 + dy), (x + 4.5, 48 + dy), (x - 0.5, 48 + dy)]), ARMV, z=2.9))
    P.append(Parte(retangulo(cx - 7, 38 + dy, cx + 7, 40 + dy), OURO, z=2.95, plano=True))
    cruz_estrela(P, cx + 1, 39 + dy, 2.96, grande=1, cor='#fbff86')
    # peitoral com uma constelação gravada
    _px(P, [(cx - 2, 26 + dy), (cx + 1, 28 + dy), (cx + 4, 25 + dy), (cx + 2, 31 + dy)], '#a884f3', 2.97)
    _px(P, [(cx - 1, 27 + dy), (cx + 2, 27 + dy), (cx + 3, 26 + dy), (cx + 1, 29 + dy), (cx + 1, 30 + dy)], '#6b3e75', 2.96)
    # elmo com fresta de luz e penacho
    cab = h['cab']
    elmo = elipse(cab[0], cab[1], 5.6, 6)
    P.append(Parte(elmo, ARMV, z=3.2))
    luzv = '#4d65b4' if t == 3 else '#8fd3ff'
    _px(P, [(cab[0] + i, cab[1] - 1 + j) for i in range(0, 6) for j in (0, 1)], '#2e222f', 3.29)
    _px(P, [(cab[0] + i, cab[1] - 1) for i in range(1, 6)], luzv, 3.3)
    if t != 3:
        _px(P, [(cab[0] + 3, cab[1] - 1), (cab[0] + 4, cab[1] - 1)], '#ffffff', 3.31)
    _px(P, [(cab[0] + 3, cab[1] + 1 + j) for j in range(3)], '#2e222f', 3.3)
    _px(P, [(cab[0] - 4 + j, cab[1] - 4 - (j % 2)) for j in range(0, 7)], '#f9c22b', 3.32)          # friso de ouro
    # asinhas no elmo
    P.append(Parte(poligono([(cab[0] - 3, cab[1] - 2), (cab[0] - 9, cab[1] - 9), (cab[0] - 8, cab[1] - 4), (cab[0] - 5, cab[1] + 1)]),
                   ['#4d65b4', '#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff'], z=3.35))
    # ombreiras com friso de ouro e uma pedra no peito
    om = h['ombro_f']
    _px(P, [(om[0] - 3 + j, om[1] - 3) for j in range(7)], '#f9c22b', 6.05)
    P.append(Parte(elipse(cx + 1, 30 + dy, 1.8, 2.2), AZUL, z=2.98))
    _pt(P, cx, 29 + dy, '#ffffff', 2.99)
    # auréola dourada
    aur = borda(elipse(cab[0] - 1, cab[1] - 9, 5.5, 1.8))
    _px(P, aur, '#f9c22b', 3.4)
    _px(P, [p for p in aur if p[0] < cab[0] - 2 and p[1] < cab[1] - 9], '#fbff86', 3.41)
    # espada estelar de ouro (ergue-se na diagonal)
    mf = h['mao_f']
    ponta = (mf[0] + 12, mf[1] - 30)
    lam = poligono([(mf[0] - 1, mf[1] - 2), (mf[0] + 2, mf[1] - 1), (ponta[0] + 1, ponta[1] + 2), (ponta[0], ponta[1])])
    P.append(Parte(lam, OURO, z=5.5))
    _px(P, [(mf[0] + 1 + (ponta[0] - mf[0]) * j / 12, mf[1] - 2 + (ponta[1] - mf[1] + 2) * j / 12) for j in range(1, 11)], '#ffffff', 5.55)
    P.append(Parte(capsula(mf[0] - 4, mf[1] - 2, mf[0] + 4, mf[1] + 1, 1.2), ARMV, z=5.6))         # guarda
    _pt(P, mf[0], mf[1] - 1, '#a884f3', 5.65)
    sp = [(0.3, 2), (0.6, 0), (0.85, 3), (0.45, 1)][t]
    cruz_estrela(P, mf[0] + (ponta[0] - mf[0]) * sp[0] + 3, mf[1] + (ponta[1] - mf[1]) * sp[0], 5.7, grande=1 + sp[1] % 2)
    mao(P, mf, ARMV, 6.5, 1.3)
    return desenhar(P, 64, 64)


def guardiao_do_tempo(t):
    """Guardião do Tempo (64): figura alta de bronze com um relógio no lugar da cara, quatro braços (dois ponteiros
    como espadas, uma ampulheta e um pêndulo), engrenagem a rodar no peito e túnica com rebites."""
    P = []
    dy = [0, 0, 1, 1][t]
    cx, chao = 29, 63
    # braço de trás de cima: ponteiro-espada
    P.append(Parte(capsula(cx - 5, 26 + dy, cx - 12, 18 + dy, 2.6), [BRONZE[0]] + BRONZE[:4], z=0.1))
    p2 = poligono([(cx - 12, 18 + dy), (cx - 22, 2 + dy), (cx - 23, 6 + dy), (cx - 14, 20 + dy)])
    P.append(Parte(p2, LATAO, z=0.12))
    P.append(Parte(poligono([(cx - 25, 0 + dy), (cx - 20, 1 + dy), (cx - 24, 6 + dy)]), LATAO, z=0.13))
    # braço de trás de baixo: pêndulo a balançar
    P.append(Parte(capsula(cx - 5, 32 + dy, cx - 13, 38 + dy, 2.2), [BRONZE[0]] + BRONZE[:4], z=0.15))
    ox = [-4, 0, 4, 0][t]
    _px(P, [(cx - 13 + ox * j / 12, 38 + dy + j) for j in range(12)], '#f9c22b', 0.16)
    P.append(Parte(elipse(cx - 13 + ox, 52 + dy, 3.6, 3.6), LATAO, z=0.17))
    _pt(P, cx - 14 + ox, 51 + dy, '#ffffff', 0.18)
    h = humanoide(P, cx, chao, k=1.32, dy=dy, pele=BRONZE, tronco=BRONZE, pernas=BRONZE, botas=['#45293f', '#6e2727', '#9e4539', '#cd683d', '#f79617'],
                  bracos=BRONZE, mao_f=(4, -10), cabeca=False)
    # túnica de bronze com rebites
    tun = poligono([(cx - 8, 36 + dy), (cx + 8, 36 + dy), (cx + 11, 52), (cx - 11, 52)])
    P.append(Parte(tun, BRONZE, z=2.8, volume='cilindro_v'))
    _px(P, [(x, 50) for x in range(cx - 9, cx + 10, 3)] + [(x, 38 + dy) for x in range(cx - 7, cx + 8, 3)], '#fbb954', 2.85)
    _px(P, [(cx - 3, y) for y in range(41 + dy, 51)] + [(cx + 3, y) for y in range(41 + dy, 51)], '#6e2727', 2.84)
    # engrenagem no peito (os dentes rodam)
    gx, gy = cx + 1, 28 + dy
    P.append(Parte(elipse(gx, gy, 4.3, 4.3), LATAO, z=2.9))
    for j in range(8):
        a = j * math.pi / 4 + t * math.pi / 16
        _px(P, [(gx + math.cos(a) * 5, gy + math.sin(a) * 5)], '#f79617', 2.88)
    _px(P, elipse(gx, gy, 1.5, 1.5), '#6e2727', 2.95)
    # cabeça-relógio: aro de latão, mostrador, ponteiros a andar, olhos de luz azul
    cab = h['cab']
    fx, fy = cab[0], cab[1] - 1
    P.append(Parte(elipse(fx, fy, 8, 8), LATAO, z=3.2))
    face = elipse(fx, fy, 6.3, 6.3)
    P.append(Parte(face, MARFIM, z=3.3))
    for a in range(12):
        ang = a / 12 * 2 * math.pi
        _pt(P, fx - 0.5 + math.sin(ang) * 5.3, fy - 0.5 - math.cos(ang) * 5.3, '#966c6c' if a % 3 else '#45293f', 3.35)
    for (ang, comp) in ((math.radians(t * 90 + 15), 5), (math.radians(300 + t * 8), 3)):
        _px(P, [(fx - 0.5 + math.sin(ang) * j, fy - 0.5 - math.cos(ang) * j) for j in range(1, comp)], '#2e222f', 3.4)
    _pt(P, fx - 0.5, fy - 0.5, '#f9c22b', 3.45)
    if t != 2:
        for ex in (fx - 3, fx + 2):
            _px(P, [(ex, fy - 2), (ex + 1, fy - 2)], '#4d9be6', 3.5)
            _pt(P, ex, fy - 2, '#8fd3ff', 3.51)
    _px(P, [(fx - 1, fy - 9), (fx, fy - 9), (fx - 1, fy - 10), (fx, fy - 10)], '#f9c22b', 3.25)            # coroa do relógio
    # braço da frente de baixo: ampulheta
    P.append(Parte(capsula(cx + 4, 31 + dy, cx + 11, 38 + dy, 2.2), BRONZE, z=4))
    ax, ay = cx + 14, 38 + dy
    P.append(Parte(retangulo(ax - 3, ay - 7, ax + 3, ay - 6), MADEIRA, z=4.1, plano=True))
    P.append(Parte(retangulo(ax - 3, ay + 6, ax + 3, ay + 7), MADEIRA, z=4.1, plano=True))
    vidro = poligono([(ax - 2.5, ay - 5.5), (ax + 3.5, ay - 5.5), (ax + 1, ay + 0.5), (ax + 3.5, ay + 6.5), (ax - 2.5, ay + 6.5), (ax, ay + 0.5)])
    P.append(Parte(vidro, ['#323353', '#484a77', '#4d65b4', '#8fd3ff', '#c7dcd0'], z=4.15, plano=True))
    areia = {p for p in vidro if p[1] >= ay + 6 - t} | {p for p in vidro if ay - 4 + t <= p[1] < ay}
    _px(P, areia, '#f9c22b', 4.2)
    _px(P, [(ax, ay + 1 + j) for j in range(0, 5 - t // 2, 2)], '#fbff86', 4.21)
    mao(P, (ax - 3, ay), BRONZE, 4.3)
    # braço da frente de cima: ponteiro-espada erguido
    mf = h['mao_f']
    P.append(Parte(poligono([(mf[0], mf[1]), (mf[0] + 16, mf[1] - 20), (mf[0] + 15, mf[1] - 16), (mf[0] + 2, mf[1] + 2)]), LATAO, z=5.5))
    P.append(Parte(poligono([(mf[0] + 14, mf[1] - 24), (mf[0] + 19, mf[1] - 22), (mf[0] + 14, mf[1] - 17)]), LATAO, z=5.6))
    _pt(P, mf[0] + 16, mf[1] - 22, '#ffffff', 5.7) if t in (0, 1) else None
    mao(P, mf, BRONZE, 6.5, 1.3)
    return desenhar(P, 64, 64)


def o_primeiro_erro(t):
    """O Primeiro Erro (64): um "bug" do Sistema. Fantasma roxo de capuz com olhos verde-água, o corpo cortado em
    fatias que fogem para o lado, quadrados de cor soltos, pixels em falta e, num quadro, a forma de outro boss."""
    P = []
    dy = [0, -1, 0, 1][t]
    cx = 30
    MANTO = VAZIO
    corpo = poligono([(cx - 12, 60), (cx - 14, 40), (cx - 11, 22 + dy), (cx - 5, 10 + dy), (cx + 4, 7 + dy), (cx + 12, 13 + dy),
                      (cx + 14, 26 + dy), (cx + 15, 44), (cx + 18, 60)])
    # num quadro "pisca" para a forma de outro boss: chifres e uma asa de dragão
    if t == 2:
        P.append(Parte(poligono([(cx - 10, 26), (cx - 30, 12), (cx - 27, 22), (cx - 32, 26), (cx - 24, 32), (cx - 12, 36)]), RAMPAS['vermelho'], z=0.2))
        for (a, b_) in (((cx - 2, 10), (cx - 8, 0)), ((cx + 6, 9), (cx + 10, 0))):
            P.append(Parte(capsula(a[0], a[1], b_[0], b_[1], 1.6), MARFIM, z=0.3))
    P.append(Parte(corpo, MANTO, z=1))
    pintas(P, corpo, MANTO, 1, 7, dens=37)
    # interior escuro do capuz e dois olhos verde-água grandes
    cara = elipse(cx + 5, 22 + dy, 7, 8)
    P.append(Parte(cara, ['#2e222f', '#2e222f', '#2e222f', '#45293f', '#45293f'], z=1.5, separar=False, plano=True))
    for ex in (cx + 2, cx + 8):
        if t == 1:
            _px(P, [(ex, 22 + dy), (ex + 1, 22 + dy), (ex + 2, 22 + dy)], '#30e1b9', 2)
        else:
            _px(P, retangulo(ex, 19 + dy, ex + 2, 23 + dy), '#30e1b9', 2)
            _px(P, [(ex, 19 + dy), (ex, 20 + dy)], '#8ff8e2', 2.1)
            _pt(P, ex + 2, 23 + dy, '#0b8a8f', 2.1)
    # código azul a escorrer pelo manto
    for j, x in enumerate(range(cx - 8, cx + 12, 4)):
        for k in range(3):
            y = 36 + ((j * 5 + k * 4 + t * 3) % 20)
            _px(P, [(x, y), (x + 1, y)] if k % 2 else [(x, y)], '#4d9be6', 2.2)
    # pixels em falta (buracos em xadrez) e quadrados de cor soltos
    buraco = retangulo(cx - 8 + t * 3, 44 - t * 2, cx - 4 + t * 3, 47 - t * 2)
    _px(P, [p for p in buraco if (p[0] + p[1]) % 2 == 0 and p in corpo], '#f04f78', 3)
    _px(P, [p for p in buraco if (p[0] + p[1]) % 2 == 1 and p in corpo], '#2e222f', 3)
    rnd = random.Random(t * 7 + 1)
    for i in range(6):
        x, y = rnd.randint(2, 58), rnd.randint(4, 58)
        c = ['#30e1b9', '#f04f78', '#4d9be6', '#fbff86'][i % 4]
        P.append(Parte(retangulo(x, y, x + 1 + i % 2, y + 1 + i % 2), [c] * 5, z=8, plano=True))
    img = desenhar(P, 64, 64)
    # o "glitch": fatias horizontais que fogem para o lado (muda a cada quadro)
    fatias = [((14, 18, 3), (40, 43, -4)), ((24, 27, -3), (50, 54, 3)), ((8, 12, -5), (30, 33, 5), (46, 48, -2)), ((20, 22, 4), (36, 41, -3))][t]
    out = img.copy()
    for (y1, y2, d) in fatias:
        faixa = img.crop((0, y1, 64, y2 + 1))
        out.paste((0, 0, 0, 0), (0, y1, 64, y2 + 1))
        out.paste(faixa, (d, y1))
    return out


def _janela(P, x1, y1, x2, y2, z, t, semente=0, olhos=False):
    """Uma janela azul do Sistema: moldura, barra de título com o botão X e linhas de texto que deslizam."""
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    P.append(Parte(retangulo(x1, y1, x2, y2), AZUL, z=z, plano=True))
    _px(P, retangulo(x1 + 1, y1 + 1, x2 - 1, y1 + 3), '#4d9be6', z + 0.01)                                   # barra de título
    _px(P, [(x2 - 3, y1 + 1), (x2 - 2, y1 + 2), (x2 - 3, y1 + 3), (x2 - 1, y1 + 1), (x2 - 1, y1 + 3)], '#ffffff', z + 0.02)
    _px(P, [(x1 + 2 + i, y1 + 2) for i in range(0, min(10, x2 - x1 - 8), 2)], '#8fd3ff', z + 0.02)
    dentro = retangulo(x1 + 2, y1 + 5, x2 - 2, y2 - 2)
    _px(P, dentro, '#323353', z + 0.01)
    if olhos:
        return dentro
    rnd = random.Random(semente)
    for j, y in enumerate(range(y1 + 6, y2 - 2, 3)):
        lin = (j + t) % 5
        comp = rnd.randint(3, max(4, x2 - x1 - 6)) if lin else 0
        _px(P, [(x1 + 3 + i, y) for i in range(min(comp, x2 - x1 - 6))], '#4d65b4' if lin % 2 else '#4d9be6', z + 0.02)
    return dentro


def administrador_gigante(t):
    """O Administrador, fases 3-4 (128): figura enorme feita de janelas azuis do Sistema. Cabeça-janela com olhos
    brancos, coroa de cristais verde-água, ombros-botões, braços de janelas encadeadas, uma mão-cursor e o corpo a
    desfazer-se em quadradinhos; ao lado, a janela "Desistir?"."""
    P = []
    dy = [0, -1, -2, -1][t]
    cx = 60
    # braço de trás: janelas pequenas encadeadas
    for i in range(4):
        x, y = cx - 30 - i * 6, 46 + i * 11 + dy + ((t + i) % 2)
        _janela(P, x, y, x + 12, y + 9, 0.2 + i * 0.01, t, 10 + i)
    # corpo de baixo: janelas que se desfazem em quadradinhos a cair
    rnd = random.Random(3)
    for i in range(26):
        x = cx + rnd.randint(-22, 22)
        y0 = 92 + rnd.randint(0, 30)
        y = y0 + ((t * 3 + i * 5) % 8) - 4
        tam = rnd.choice((1, 2, 2, 3))
        c = rnd.choice(['#4d65b4', '#4d9be6', '#8fd3ff', '#30e1b9'])
        P.append(Parte(retangulo(x, y, x + tam, y + tam), [c] * 5, z=0.5, plano=True))
    _janela(P, cx - 18, 82 + dy, cx + 16, 98 + dy, 0.8, t, 4)
    _janela(P, cx - 12, 96 + dy, cx + 8, 108 + dy, 0.7, t, 5)
    # tronco: janela grande, com ombros-botões verde-água
    _janela(P, cx - 26, 44 + dy, cx + 26, 86 + dy, 1, t, 1)
    _janela(P, cx - 10, 54 + dy, cx + 16, 72 + dy, 1.5, t + 2, 2)
    # coração: um núcleo azul que pulsa
    rr = [3, 4, 5, 4][t]
    P.append(Parte(elipse(cx + 3, 63 + dy, rr, rr), VIDRO, z=1.6))
    _pt(P, cx + 2, 62 + dy - rr // 2, '#ffffff', 1.7)
    for (ox, z) in ((-26, 1.8), (26, 1.8)):
        P.append(Parte(elipse(cx + ox, 46 + dy, 7, 7), VIDRO, z=z))
        _px(P, [(cx + ox - 3, 43 + dy), (cx + ox - 2, 42 + dy)], '#ffffff', z + 0.01)
    # cabeça-janela com olhos brancos e coroa de cristais
    dentro = _janela(P, cx - 14, 14 + dy, cx + 20, 40 + dy, 2, t, 0, olhos=True)
    for (ex, ey) in ((cx + 3, 24), (cx + 12, 24)):
        if t == 2:
            _px(P, retangulo(ex, ey + 3 + dy, ex + 4, ey + 4 + dy), '#ffffff', 2.1)
        else:
            _px(P, retangulo(ex, ey + dy, ex + 4, ey + 5 + dy), '#ffffff', 2.1)
            _px(P, retangulo(ex + 3, ey + 2 + dy, ex + 4, ey + 5 + dy), '#8fd3ff', 2.11)
    _px(P, [(cx + 6 + i, 34 + dy) for i in range(8)], '#4d9be6', 2.1)                                          # boca: uma linha
    for (bx, h, s_) in ((cx - 8, 10, 0), (cx + 2, 14, 1), (cx + 12, 10, 2)):
        cri = poligono([(bx - 3, 15 + dy), (bx + 1, 15 + dy - h), (bx + 4, 15 + dy)])
        P.append(Parte(cri, VIDRO, z=1.9))
        if (t + s_) % 4 == 0:
            cruz_estrela(P, bx + 1, 15 + dy - h - 2, 2.2, cor='#8ff8e2')
    # braço da frente: janelas e a mão-cursor
    for i in range(3):
        x, y = cx + 26 + i * 5, 50 + i * 11 + dy - ((t + i) % 2)
        _janela(P, x, y, x + 12, y + 9, 3 + i * 0.01, t, 20 + i)
    mx, my = cx + 40, 86 + dy
    cursor = poligono([(mx, my), (mx, my + 18), (mx + 4, my + 14), (mx + 7, my + 21), (mx + 10, my + 19), (mx + 7, my + 13), (mx + 13, my + 13)])
    P.append(Parte(cursor, ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=3.5, plano=True))
    # a janela "Desistir?" a pairar ao lado (Sim / Não)
    wy = 6 + [0, 1, 2, 1][t]
    _janela(P, 92, wy, 125, wy + 20, 4, t, 9, olhos=True)
    _px(P, [(97, wy + 8), (98, wy + 8), (99, wy + 8), (99, wy + 9), (98, wy + 10)], '#ffffff', 4.1)        # "?"
    _pt(P, 98, wy + 12, '#ffffff', 4.1)
    _px(P, retangulo(104, wy + 13, 111, wy + 16), '#1ebc73', 4.1)                                          # Sim
    _px(P, retangulo(114, wy + 13, 121, wy + 16), '#e83b3b', 4.1)                                          # Não
    return desenhar(P, 128, 128)


# =====================================================================================
# registo, gravação e comparações
# =====================================================================================

CRIATURAS = [   # (id, pasta do desenho antigo)
    ('sombra', 'arte/regioes/r10_abismo/monstros'),
    ('olho_do_vazio', 'arte/regioes/r10_abismo/monstros'),
    ('relogio_vivo', 'arte/regioes/r10_abismo/monstros'),
    ('anjo_do_vazio', 'arte/regioes/r10_abismo/monstros'),
    ('jogador_sem_numero', 'arte/regioes/r10_abismo/monstros'),
    ('devorador_de_estrelas', 'arte/regioes/r10_abismo/monstros'),
    ('fragmento_de_mundo', 'arte/regioes/r10_abismo/monstros'),
    ('devorador_ancestral', 'arte/regioes/r10_abismo/monstros'),
    ('porteiro_do_vazio', 'arte/regioes/r10_abismo/guardioes'),
    ('rainha_dos_espelhos', 'arte/regioes/r10_abismo/guardioes'),
    ('indice_vivo', 'arte/regioes/r10_abismo/guardioes'),
    ('o_desistente', 'arte/regioes/r10_abismo/guardioes'),
    ('baleia_estelar', 'arte/regioes/r10_abismo/guardioes'),
    ('eco_dos_guardioes', 'arte/regioes/r10_abismo/guardioes'),
    ('gigante_invertido', 'arte/regioes/r10_abismo/guardioes'),
    ('o_guardiao_da_escada', 'arte/regioes/r10_abismo/guardioes'),
    ('administrador', 'arte/regioes/r10_abismo/bosses'),
    ('guardiao_do_tempo', 'arte/regioes/r10_abismo/bosses'),
    ('o_primeiro_erro', 'arte/regioes/r10_abismo/bosses'),
    ('administrador_gigante', 'arte/regioes/r10_abismo/bosses'),
    ('mimico', 'arte/monstros_comuns'),
]

RESURRECT64 = """2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334 e83b3b
fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73 91db69 cddf6c
313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff 45293f 6b3e75 905ea9
a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0""".split()


def nomes_pt():
    nomes = {}
    for f in ('dados/monstros.json', 'dados/bosses.json'):
        for e in json.load(open(os.path.join(RAIZ, f), encoding='utf-8')):
            if e.get('nome_pt'):
                nomes[e['id']] = e['nome_pt']
    try:
        mas = json.load(open(os.path.join(RAIZ, 'dados/masmorras.json'), encoding='utf-8'))
        for v in (mas.values() if isinstance(mas, dict) else []):
            if isinstance(v, dict) and v.get('id') and v.get('nome_pt'):
                nomes.setdefault(v['id'], v['nome_pt'])
    except Exception:
        pass
    nomes.setdefault('administrador_gigante', 'O Administrador (gigante)')
    nomes.setdefault('o_primeiro_erro', 'O Primeiro Erro')
    return nomes


def verificar(img, nome):
    pal = {tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) for c in RESURRECT64}
    dados = img.get_flattened_data() if hasattr(img, 'get_flattened_data') else img.getdata()
    fora = {px[:3] for px in dados if px[3] and px[:3] not in pal}
    meio = {px[3] for px in dados if 0 < px[3] < 255}
    if fora or meio:
        print('  AVISO', nome, 'cores fora da paleta:', sorted(fora)[:6], 'alfa a meio:', sorted(meio)[:4])
    return not fora and not meio


def gravar(ids=None):
    os.makedirs(SAIDA, exist_ok=True)
    feitos = {}
    for cid, pasta in CRIATURAS:
        if ids and cid not in ids:
            continue
        antigo = Image.open(os.path.join(RAIZ, pasta, cid + '_parado_lado.png')).convert('RGBA')
        q = antigo.height
        quadros = [globals()[cid](t) for t in range(4)]
        assert all(f.size == (q, q) for f in quadros), (cid, quadros[0].size, q)
        tira = Image.new('RGBA', (q * 4, q), (0, 0, 0, 0))
        for i, f in enumerate(quadros):
            tira.paste(f, (i * q, 0))
        verificar(tira, cid)
        tira.save(os.path.join(SAIDA, cid + '_parado_lado.png'))
        antes = [antigo.crop((i * q, 0, i * q + q, q)) for i in range(antigo.width // q)]
        feitos[cid] = (antes, quadros)
        print('ok', cid, q)
    return feitos


def _escala(q):
    return 3 if q <= 32 else 2 if q <= 64 else 1


def gifs(feitos):
    fundo = (0x26, 0x2b, 0x3a)
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
    nomes = nomes_pt()
    larg_max, gap, txt = 1200, 12, 18

    def montar(com_antes, titulo):
        celulas = []
        for cid, _ in CRIATURAS:
            if cid not in feitos:
                continue
            antes, depois = feitos[cid]
            q = depois[0].height
            e = _escala(q)
            w = q * e * (2 if com_antes else 1) + (8 if com_antes else 0)
            celulas.append((cid, antes, depois, q, e, max(w, 90), q * e + txt))
        # arrumar em linhas
        linhas, linha, x = [], [], gap
        for c in celulas:
            if linha and x + c[5] + gap > larg_max:
                linhas.append(linha)
                linha, x = [], gap
            linha.append(c)
            x += c[5] + gap
        linhas.append(linha)
        W = min(larg_max, max(gap + sum(c[5] + gap for c in l) for l in linhas))
        H = 30 + sum(max(c[6] for c in l) + gap for l in linhas)
        pal = Image.new('P', (1, 1))
        cores = [fundo] + [tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) for c in RESURRECT64]
        flat = [v for c in cores for v in c]
        pal.putpalette(flat + flat[:3] * (256 - len(cores)))
        imgs = []
        for k in range(8):
            im = Image.new('RGBA', (W, H), fundo + (255,))
            d = ImageDraw.Draw(im)
            d.fontmode = '1'
            d.text((gap, 8), titulo, fill=(255, 255, 255), font=fonte)
            y = 30
            for l in linhas:
                x = gap
                alt = max(c[6] for c in l)
                for (cid, antes, depois, q, e, w, h) in l:
                    xx = x + (w - (q * e * (2 if com_antes else 1) + (8 if com_antes else 0))) // 2
                    yb = y + (alt - h)
                    if com_antes:
                        a = antes[k % len(antes)].resize((q * e, q * e), Image.NEAREST)
                        im.alpha_composite(a, (xx, yb))
                        xx += q * e + 8
                    n = depois[k % 4].resize((q * e, q * e), Image.NEAREST)
                    im.alpha_composite(n, (xx, yb))
                    nome = nomes.get(cid, cid)
                    tw = d.textlength(nome, font=fonte)
                    while tw > w + gap - 2 and len(nome) > 4:
                        nome = nome[:-2] + '…'
                        tw = d.textlength(nome, font=fonte)
                    d.text((x + (w - tw) / 2, yb + q * e + 3), nome, fill=(255, 255, 255), font=fonte)
                    x += w + gap
                y += alt + gap
            imgs.append(im.convert('RGB').quantize(palette=pal, dither=Image.Dither.NONE))
        return imgs

    a = montar(True, 'Região 10 — Abismo (e o Mímico) — antes | depois')
    a[0].save(os.path.join(SAIDA, 'comparar.gif'), save_all=True, append_images=a[1:], duration=160, loop=0)
    b = montar(False, 'Região 10 — Abismo (e o Mímico) — depois')
    b[0].save(os.path.join(SAIDA, 'depois.gif'), save_all=True, append_images=b[1:], duration=160, loop=0)
    print('gifs:', os.path.join(SAIDA, 'comparar.gif'), os.path.join(SAIDA, 'depois.gif'))


if __name__ == '__main__':
    ids = sys.argv[1:] or None
    feitos = gravar(ids)
    if not ids:
        gifs(feitos)
