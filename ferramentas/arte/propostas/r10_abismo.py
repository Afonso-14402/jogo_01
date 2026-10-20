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
        h = (x * 7 + y * 13 + semente * 5) % dens
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
