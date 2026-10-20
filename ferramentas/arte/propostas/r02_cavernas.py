"""PROPOSTA: monstros, guardiões e bosses da região 2 (Cavernas e Minas) redesenhados (só o "parado", 4 quadros).

NÃO mexe no jogo: grava só em arte/propostas/monstros/r02_cavernas/ (PNG de cada criatura + comparar.gif + depois.gif).
Para correr (na raiz do repositório):  python3 ferramentas/arte/propostas/r02_cavernas.py

Fichas: docs/regioes/r02_cavernas.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (Aranha-Mãe, Golem de Cristal).
Estilo: docs/ARTE.md secção 0 e o exemplo ferramentas/arte/ent_anciao.py (partes com volume, textura, olhos com brilho).
Só cores da paleta Resurrect 64; luz de cima à esquerda; contorno #2e222f; virados para a DIREITA, pés no fundo.
"""
import glob
import json
import math
import os
import random
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

REGIAO = 'r02_cavernas'
ANTIGO = os.path.join(RAIZ, 'arte', 'regioes', REGIAO)
SAIDA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', REGIAO)

OUT = '#2e222f'
BRANCO = '#ffffff'

# ---------------- rampas extra (só Resurrect 64, escuro -> claro) ----------------
R = dict(RAMPAS)
R.update({
    'pedra':     ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'],
    'pedra_cl':  ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'terra':     ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'],
    'roxo_esc':  ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'],
    'goblin':    ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'pano':      ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'],
    'pano_az':   ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6'],
    'pano_vm':   ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'],
    'escama_lj': ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#fbb954'],
    'cristal_t': ['#0b5e65', '#0b8a8f', '#30e1b9', '#8ff8e2', '#ffffff'],
    'cristal_r': ['#45293f', '#6b3e75', '#a884f3', '#eaaded', '#ffffff'],
    'cristal_a': ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff'],
    'cristal_v': ['#165a4c', '#239063', '#91db69', '#cddf6c', '#ffffff'],
    'cristal_p': ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
    'fantasma':  ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'],
    'osso':      ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'osso_esc':  ['#3e3546', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff'],
    'bronze':    ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'],
    'ferro_esc': ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'],
    'pelo_tou':  ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'],
    'pelo_touro': ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e'],
    'fungo':     ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
    'sombra':    ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565'],
    'madeira_e': ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'],
    'verde_fan': ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90'],
})


def rp(nome):
    return R[nome] if isinstance(nome, str) else nome


# ---------------- pequenas ferramentas de desenho ----------------

def px(P, pts, cor, z):
    """Píxeis de uma só cor (pormenores: olhos, riscos, pintas)."""
    P.append(Parte({(int(round(x)), int(round(y))) for x, y in pts}, None, z=z, separar=False, cor=cor))


def parte(P, m, rampa, z, **kw):
    p = Parte(m, rp(rampa), z=z, **kw)
    P.append(p)
    return m


def _h(x, y, s):
    v = (x * 374761393 + y * 668265263 + s * 2147483647) & 0xffffffff
    v = (v ^ (v >> 13)) * 1274126177 & 0xffffffff
    return (v ^ (v >> 16)) / 0xffffffff


def interior(m, d=1):
    """Os píxeis da máscara que não estão na borda (para a textura não estragar a silhueta)."""
    r = set(m)
    for _ in range(d):
        r = {(x, y) for (x, y) in r if all((x + a, y + b) in r for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))}
    return r


def centro(m):
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    return (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2


def textura(P, m, rampa, z, s=1, escuro=0.08, claro=0.05, traco=0):
    """Pintas de sombra (mais do lado escuro) e reflexos claros (só em cima à esquerda). traco>0 faz riscos (pelo)."""
    r = rp(rampa)
    cx, cy = centro(m)
    dentro = interior(m)
    e, c = [], []
    for (x, y) in dentro:
        lado = (x - cx) + (y - cy)
        k = _h(x, y, s)
        if k < escuro * (1.6 if lado > 0 else 0.7):
            e.append((x, y))
            if traco and (x + traco, y + 1) in dentro:
                e.append((x + traco, y + 1))
        elif k > 1 - claro and lado < -1:
            c.append((x, y))
            if traco and (x + traco, y + 1) in dentro:
                c.append((x + traco, y + 1))
    px(P, e, r[1] if len(r) > 1 else r[0], z + 0.001)
    px(P, c, r[3], z + 0.002)


def olho(P, x, y, iris, z, tam=1, pupila=OUT, brilho=BRANCO, fechado=False, cor_palpebra=None):
    """Olho com pupila e ponto de brilho. tam 1: 2x2; tam 2: 3x3; tam 0: 1 píxel + brilho."""
    if fechado:
        px(P, [(x + i, y + (tam // 2)) for i in range(tam + 1)], cor_palpebra or OUT, z)
        return
    if tam == 0:
        px(P, [(x, y)], iris, z)
        px(P, [(x, y - 1)], brilho, z + 0.01)
        return
    n = tam + 1
    px(P, [(x + i, y + j) for i in range(n) for j in range(n)], iris, z)
    px(P, [(x + n - 1, y + n - 1)] + ([(x + n - 2, y + n - 1)] if tam > 1 else []), pupila, z + 0.01)
    px(P, [(x, y)], brilho, z + 0.02)


def cristal(P, bx, by, ang, comp, larg, rampa, z, brilho=True):
    """Um cristal facetado: metade esquerda clara, metade direita escura, aresta clara e um brilho na ponta."""
    r = rp(rampa)
    dx, dy = math.cos(ang), math.sin(ang)
    nx, ny = -dy, dx
    tx, ty = bx + dx * comp, by + dy * comp
    a = (bx + nx * larg, by + ny * larg)
    b = (bx - nx * larg, by - ny * larg)
    m = (bx + dx * comp * 0.15, by + dy * comp * 0.15)
    toda = poligono([a, (tx, ty), b, (bx - dx, by - dy)])
    P.append(Parte(toda, r, z=z, cor=r[2]))
    # que lado é o iluminado? (luz vem de cima à esquerda)
    lado_a = (a[0] - bx) * -0.6 + (a[1] - by) * -0.8
    clara, escura = (a, b) if lado_a > 0 else (b, a)
    px(P, poligono([clara, (tx, ty), m]) & toda, r[3], z + 0.001)
    px(P, poligono([escura, (tx, ty), m]) & toda, r[1], z + 0.001)
    aresta = [(bx + dx * comp * t + (clara[0] - bx) * 0.25 * (1 - t), by + dy * comp * t + (clara[1] - by) * 0.25 * (1 - t))
              for t in [i / max(1, comp) for i in range(int(comp * 0.3), int(comp))]]
    px(P, [p for p in aresta if (int(round(p[0])), int(round(p[1]))) in toda], r[4], z + 0.002)
    if brilho:
        px(P, [(tx - dx * 1.2, ty - dy * 1.2)], BRANCO, z + 0.003)
    return toda


def brilhos(P, pts, z, fase, cor=BRANCO, cor2='#fbff86'):
    """Estrelinhas a piscar (cruz de 5 px numa fase, ponto na outra)."""
    for i, (x, y) in enumerate(pts):
        k = (fase + i) % 4
        if k == 0:
            px(P, [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], cor2, z)
            px(P, [(x, y)], cor, z + 0.01)
        elif k == 1:
            px(P, [(x, y)], cor, z)


def linha(x1, y1, x2, y2):
    n = int(max(abs(x2 - x1), abs(y2 - y1))) + 1
    return [(x1 + (x2 - x1) * i / max(1, n - 1), y1 + (y2 - y1) * i / max(1, n - 1)) for i in range(n)]


RESP = [0, 0, 1, 1]       # respirar: desce 1 px a meio
BOB = [0, -1, 0, 1]       # flutuar


# =====================================================================================
#  MONSTROS (32×32 e 48×48)
# =====================================================================================

def morcego(t):
    """Morcego (32): corpo peludo roxo, orelhas grandes rosadas por dentro, asas de membrana com dedos, olho vermelho
    com brilho, um dente branco e garrinhas. As asas batem (cima, meio, baixo, meio)."""
    P = []
    dy = [0, -1, 0, 1][t]
    # asa de trás (mais escura, sobe por trás do corpo)
    tras = [[(14, 12), (10, 3), (6, 1), (8, 6), (10, 8), (12, 10)],
            [(14, 12), (9, 6), (4, 6), (7, 9), (10, 10), (12, 12)],
            [(14, 13), (9, 12), (4, 15), (7, 15), (10, 15), (13, 15)],
            [(14, 12), (9, 6), (4, 6), (7, 9), (10, 10), (12, 12)]][t]
    parte(P, poligono([(x, y + dy) for x, y in tras]), ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9'], 1, plano=True)
    # asa da frente (membrana com recortes e os "dedos" mais claros)
    if t == 0:
        S, E, T = (16, 13), (11, 5), (3, 3)
        borda = [(5, 9), (8, 9), (10, 12), (13, 13)]
    elif t == 2:
        S, E, T = (16, 14), (11, 18), (5, 24)
        borda = [(8, 22), (10, 20), (12, 21), (14, 18)]
    else:
        S, E, T = (16, 13), (10, 11), (2, 11)
        borda = [(4, 15), (7, 14), (10, 17), (13, 16)]
    asa = poligono([(x, y + dy) for x, y in [S, E, T] + borda])
    parte(P, asa, ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'], 8, plano=True)
    for b in borda[1:3]:
        px(P, [p for p in linha(E[0], E[1] + dy, b[0], b[1] + dy) if (int(round(p[0])), int(round(p[1]))) in asa], '#905ea9', 8.1)
    px(P, linha(S[0], S[1] + dy, E[0], E[1] + dy) + linha(E[0], E[1] + dy, T[0], T[1] + dy), '#a884f3', 8.2)
    px(P, [(E[0], E[1] + dy)], '#eaaded', 8.3)
    # corpo peludo
    corpo = parte(P, elipse(16.5, 15 + dy, 4.6, 4.8), 'roxo', 5)
    textura(P, corpo, 'roxo_esc', 5, s=3, escuro=0.18, claro=0.06, traco=1)
    px(P, [(18, 17 + dy), (19, 16 + dy), (18, 18 + dy)], '#a884f3', 5.1)          # peito mais claro
    # garrinhas
    px(P, [(15, 20 + dy), (15, 21 + dy), (18, 20 + dy), (18, 21 + dy)], '#c7dcd0', 4)
    # orelhas (a de trás e a da frente, rosa por dentro)
    parte(P, poligono([(16, 11 + dy), (15, 3 + dy), (19, 9 + dy)]), 'roxo', 4.5)
    o2 = parte(P, poligono([(19, 10 + dy), (21, 2 + dy), (23, 9 + dy)]), 'roxo', 6.5)
    px(P, [(21, 5 + dy), (21, 6 + dy), (21, 7 + dy), (22, 7 + dy)], '#f04f78', 6.6)
    # cabeça e focinho
    parte(P, elipse(21, 12 + dy, 3.8, 3.3), 'roxo', 6)
    parte(P, elipse(24.2, 13 + dy, 1.8, 1.5), 'lilas', 6.2)
    px(P, [(25, 12 + dy)], '#831c5d', 6.3)                                     # nariz
    olho(P, 21, 10 + dy, '#e83b3b', 7, tam=0) if t != 3 else px(P, [(21, 11 + dy), (22, 11 + dy)], OUT, 7)
    if t != 3:
        px(P, [(22, 11 + dy)], '#e83b3b', 7)
    px(P, [(23, 15 + dy)], BRANCO, 7)                                           # dente
    return desenhar(P, 32, 32)


def goblin_mineiro(t):
    """Goblin Mineiro (32): cabeça verde grande com orelha pontiaguda e verrugas, nariz comprido, olho amarelo,
    capacete de mineiro com lanterna acesa, túnica remendada com cinto, picareta a arrastar atrás."""
    P = []
    dy = RESP[t]
    # picareta (atrás, na mão de trás)
    parte(P, capsula(12, 21 + dy, 6, 27, 0.8), 'madeira', 0.5)
    cab = poligono([(2, 25), (5, 25), (9, 27), (9, 28), (5, 28), (2, 27)])
    parte(P, cab | {(1, 26), (10, 29)}, 'ferro', 0.6, plano=True)
    px(P, [(3, 26), (4, 26)], BRANCO, 0.61)
    # pernas e botas
    parte(P, capsula(13, 24, 13, 28, 1.4), 'pano_az', 1, volume='cilindro_v')
    parte(P, capsula(17, 24, 18, 28, 1.5), 'pano_az', 3, volume='cilindro_v')
    parte(P, elipse(13.5, 29.3, 2.4, 1.5), 'terra', 1.5)
    parte(P, elipse(19, 29.3, 2.6, 1.5), 'terra', 3.5)
    # braço de trás
    parte(P, capsula(13, 19 + dy, 11.5, 22 + dy, 1.4), ['#165a4c', '#165a4c', '#239063', '#1ebc73', '#91db69'], 1.8)
    # túnica
    tun = parte(P, elipse(15.5, 21 + dy, 5, 4.8), 'pano', 2)
    textura(P, tun, 'pano', 2, s=5, escuro=0.12)
    px(P, [(x, 23 + dy) for x in range(11, 21)], '#45293f', 2.1)                 # cinto
    px(P, [(17, 23 + dy)], '#f9c22b', 2.2)                                      # fivela
    px(P, [(12, 19 + dy), (13, 19 + dy), (12, 20 + dy), (13, 20 + dy)], '#676633', 2.15)   # remendo
    px(P, [(14, 19 + dy), (14, 20 + dy)], '#ab947a', 2.16)                     # ponto do remendo
    # braço da frente
    parte(P, capsula(17, 19 + dy, 20.5, 22 + dy, 1.4), 'goblin', 6)
    parte(P, elipse(21, 22.5 + dy, 1.6, 1.5), 'goblin', 6.1)
    # orelha (para trás) e cabeça
    orelha = poligono([(12, 10 + dy), (4, 8 + dy), (6, 12 + dy), (12, 15 + dy)])
    parte(P, orelha, 'goblin', 4, plano=True)
    px(P, [(8, 10 + dy), (9, 11 + dy), (10, 11 + dy), (11, 12 + dy)], '#239063', 4.1)
    cab = parte(P, elipse(17, 13 + dy, 6, 5), 'goblin', 5)
    px(P, [(13, 15 + dy), (15, 16 + dy)], '#239063', 5.1)                     # verrugas
    px(P, [(14, 13 + dy)], '#91db69', 5.1)
    parte(P, capsula(21.5, 13 + dy, 25, 15.5 + dy, 1.6), 'goblin', 5.5)          # nariz
    px(P, [(25, 16 + dy)], '#239063', 5.6)
    if t == 3:
        px(P, [(19, 12 + dy), (20, 12 + dy)], OUT, 6)
    else:
        olho(P, 19, 11 + dy, '#f9c22b', 6)
    px(P, [(18, 10 + dy), (19, 9 + dy), (20, 9 + dy), (21, 10 + dy)], '#165a4c', 6.1)   # sobrolho
    px(P, [(19, 17 + dy), (20, 17 + dy), (21, 17 + dy), (22, 16 + dy)], OUT, 6)     # boca
    px(P, [(20, 18 + dy)], BRANCO, 6.1)                                         # dente
    # capacete de mineiro com lanterna
    cap = {p for p in elipse(16.5, 9.5 + dy, 5.8, 4.4) if p[1] <= 9 + dy}
    parte(P, cap, 'ouro', 7)
    parte(P, retangulo(10, 9 + dy, 23, 9 + dy), ['#4c3e24', '#4c3e24', '#9e4539', '#cd683d', '#cd683d'], 7.2, plano=True)
    px(P, [(15, 6 + dy), (16, 6 + dy), (15, 7 + dy)], '#fbff86', 7.3)
    lamp = elipse(21.5, 7 + dy, 1.8, 1.8)
    parte(P, lamp, 'ferro', 7.5)
    px(P, [(22, 7 + dy), (22, 6 + dy)] + ([(23, 7 + dy)] if t % 2 == 0 else []), '#fbff86', 7.6)
    px(P, [(22, 6 + dy)], BRANCO, 7.7)
    return desenhar(P, 32, 32)


def toupeira(t, dourada=False):
    """Toupeira (32): de quatro patas, pelo espesso com riscos, focinho comprido cor-de-rosa que fareja, olhinho
    pequeno, garras grandes de escavar e bigodes. A Dourada é mais pequena, de pelo dourado e a brilhar."""
    P = []
    dy = RESP[t]
    pelo = 'ouro' if dourada else 'pelo_tou'
    pelo_esc = ['#9e4539', '#9e4539', '#f79617', '#f9c22b', '#fbff86'] if dourada else ['#2e222f', '#2e222f', '#4c3e24', '#694f62', '#966c6c']
    k = 0.85 if dourada else 1.0
    ox = 2 if dourada else 0
    fz = [0, 1, 0, 0][t]     # o focinho fareja
    def X(x):
        return ox + 16 + (x - 16) * k
    # patas de trás (longe)
    parte(P, capsula(X(9), 26, X(8), 29, 1.6 * k), pelo_esc, 1)
    parte(P, capsula(X(22), 26, X(23), 29, 1.6 * k), pelo_esc, 1)
    # corpo
    corpo = parte(P, elipse(X(15), 23 + dy * 0.5 + (1 - k) * 4, 10 * k, 6.5 * k), pelo, 2)
    textura(P, corpo, pelo, 2, s=11, escuro=0.2, claro=0.1, traco=1)
    # cauda curta
    parte(P, capsula(X(5), 22, X(3), 21, 1), 'rosa' if not dourada else 'ouro', 1.5)
    # cabeça e focinho
    cab = parte(P, elipse(X(25), 22 + dy * 0.5 + (1 - k) * 3, 4.6 * k, 4.2 * k), pelo, 4)
    textura(P, cab, pelo, 4, s=12, escuro=0.15, claro=0.08, traco=1)
    fy = 23.5 + (1 - k) * 3 + dy * 0.5
    parte(P, capsula(X(27), fy, X(30) + fz, fy + 0.5 - fz * 0.5, 1.6 * k), 'rosa', 5)
    px(P, [(X(30) + fz + 1, fy - fz * 0.5)], '#831c5d', 5.1)
    olho(P, X(26), fy - 3, '#2e222f', 6, tam=0, brilho='#c7dcd0')
    # bigodes
    px(P, [(X(29) + fz, fy - 2), (X(30) + fz, fy - 3), (X(29) + fz, fy + 2), (X(30) + fz, fy + 3)], '#c7dcd0', 6)
    # patas da frente com garras grandes
    for (bx, z) in ((X(22), 7), (X(11), 6.5)):
        parte(P, capsula(bx, 25, bx + 1, 28.5, 1.8 * k), pelo, z)
        for i in range(3):
            px(P, [(bx + 2 + i, 29 - i % 2), (bx + 3 + i, 30 - i % 2)], '#c7dcd0', z + 0.1)
        px(P, [(bx + 2, 28)], BRANCO, z + 0.2)
    if dourada:
        brilhos(P, [(X(12), 15), (X(24), 17), (X(6), 20)], 20, t)
    return desenhar(P, 32, 32)


def aranha_da_caverna(t):
    """Aranha da Caverna (32): abdómen grande cinzento-acastanhado com chevrons claros e pelos, cefalotórax,
    cachos de olhos laranja com brilho, quelíceras vermelhas com pontas brancas, 8 patas finas com joelhos altos."""
    P = []
    dy = RESP[t]
    sh = [0, 1, 0, -1][t]
    # (anca, joelho, pé) das 4 patas do lado de cá; as do lado de lá são iguais, 2 px atrás e mais escuras
    patas = [((21, 20), (27, 11), (31, 30)), ((20, 20), (23, 8), (26, 30)),
             ((19, 20), (15, 7), (15, 30)), ((18, 20), (8, 7), (3, 30))]
    for i, (h, j, p) in enumerate(patas):
        o = sh if i % 2 else -sh
        h2, j2, p2 = (h[0] - 1, h[1] + dy), (j[0] - 2, j[1] + 2 + dy + o), (p[0] - 2, p[1] - 1)
        parte(P, capsula(*h2, *j2, 0.55), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#625565'], 1, plano=True)
        parte(P, capsula(*j2, *p2, 0.5), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#625565'], 1, plano=True)
    # abdómen
    ab = parte(P, elipse(9, 18.5 + dy, 7.5 - (t % 2) * 0.3, 6), ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a'], 3)
    textura(P, ab, ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a'], 3, s=21, escuro=0.15, claro=0.05, traco=1)
    for i, x in enumerate((5, 8, 11)):            # chevrons vermelhos (marca da aranha)
        px(P, [(x - 1, 15 + dy), (x, 16 + dy), (x - 1, 17 + dy)], '#c7dcd0' if i == 1 else '#ab947a', 3.1)
    px(P, [(2, 19 + dy), (1, 20 + dy), (3, 22 + dy), (6, 22 + dy)], '#3e3546', 3.1)            # pelinhos
    # cefalotórax e cabeça
    parte(P, elipse(18.5, 21 + dy, 4.2, 3.4), 'pelo_tou', 4)
    parte(P, elipse(23.5, 21 + dy, 3.5, 3.2), 'pelo_tou', 5)
    for (x, y, c) in ((23, 19, '#fb6b1d'), (25, 20, '#f79617')):
        px(P, [(x, y + dy), (x + 1, y + dy)], c, 6)
        px(P, [(x, y + dy)], '#fbb954' if t != 2 else BRANCO, 6.1)
    px(P, [(22, 18 + dy), (24, 18 + dy)], '#f79617', 6)
    # quelíceras
    for (x, z) in ((24, 6.5), (26, 7)):
        parte(P, capsula(x, 23 + dy, x + 0.5, 25 + dy, 1), 'vermelho', z)
        px(P, [(x + 1, 26 + dy)], BRANCO, z + 0.1)
    # patas do lado de cá (finas, com joelho claro)
    for i, (h, j, p) in enumerate(patas):
        o = -sh if i % 2 else sh
        h2, j2, p2 = (h[0], h[1] + dy), (j[0], j[1] + dy + o), p
        perna = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#7f708a']
        parte(P, capsula(*h2, *j2, 0.6), perna, 2, plano=True)
        parte(P, capsula(*j2, *p2, 0.55), perna, 2.1, plano=True)
        px(P, [j2, (j2[0] + (1 if i < 2 else -1), j2[1] + 1)], '#ab947a', 2.2)
        px(P, [(p2[0] - (p2[0] - j2[0]) * 0.3, p2[1] - (p2[1] - j2[1]) * 0.3)], '#9e4539', 2.2)
    return desenhar(P, 32, 32)


def kobold(t):
    """Kobold (32): homenzinho-lagarto laranja com focinho comprido, cornos, olho amarelo de pupila em fenda,
    colete de couro, lança com um pano vermelho, lanterna pequena no cinto e cauda que abana."""
    P = []
    dy = RESP[t]
    cauda_y = [0, 1, 2, 1][t]
    # cauda (sai de trás e abana)
    parte(P, capsula(12, 24, 8, 26 + cauda_y * 0.5, 2), 'escama_lj', 0.5)
    parte(P, capsula(8, 26 + cauda_y * 0.5, 3, 27 + cauda_y, 1.1), 'escama_lj', 0.6)
    # pernas (de lagarto, para trás)
    parte(P, capsula(14, 24, 13, 28, 1.5), ['#6e2727', '#6e2727', '#9e4539', '#cd683d', '#f79617'], 1)
    parte(P, capsula(18, 24, 19, 28, 1.6), 'escama_lj', 3)
    for (x, z) in ((13, 1.2), (19, 3.2)):
        parte(P, elipse(x + 0.5, 29.3, 2.2, 1.3), 'escama_lj', z)
        px(P, [(x + 2, 30), (x + 3, 30)], '#c7dcd0', z + 0.1)
    # lança (atrás do braço da frente)
    parte(P, capsula(26, 30, 28.5, 7, 0.6), 'madeira', 2.5)
    parte(P, poligono([(27, 7), (29, 1), (30.5, 7)]), 'ferro', 2.6, plano=True)
    parte(P, poligono([(27, 8), (30, 8), (30, 12), (28, 11)]), 'pano_vm', 2.7, plano=True)
    # corpo e colete
    parte(P, elipse(16, 21 + dy, 4.6, 4.8), 'escama_lj', 4)
    col = parte(P, {p for p in elipse(15.5, 21 + dy, 4.6, 4.8) if p[0] <= 16}, 'couro', 4.2)
    px(P, [(x, 24 + dy) for x in range(12, 21)], '#45293f', 4.3)
    px(P, [(17, 19 + dy), (18, 20 + dy), (18, 22 + dy)], '#fbb954', 4.3)        # barriga às riscas
    px(P, [(14, 19 + dy), (13, 21 + dy)], '#ab947a', 4.25)
    # lanterna no cinto
    parte(P, retangulo(10, 24 + dy, 12, 27 + dy), 'ferro_esc', 4.4, plano=True)
    px(P, [(11, 25 + dy), (11, 26 + dy)], '#f9c22b' if t % 2 == 0 else '#fbff86', 4.5)
    # cabeça, focinho e cornos
    parte(P, poligono([(15, 9 + dy), (11, 6 + dy), (12, 9 + dy), (14, 11 + dy)]), 'osso_esc', 5, plano=True)
    cab = parte(P, elipse(17, 12.5 + dy, 4.6, 4.2), 'escama_lj', 6)
    fo = parte(P, capsula(19, 13.5 + dy, 24, 14.5 + dy, 2.3), 'escama_lj', 6.5)
    textura(P, cab | fo, 'escama_lj', 6.5, s=31, escuro=0.18, claro=0.06)
    px(P, [(24, 13 + dy)], OUT, 6.6)                                           # narina
    px(P, [(x, 16 + dy) for x in range(20, 25)], '#6e2727', 6.6)               # boca
    px(P, [(22, 17 + dy), (24, 17 + dy)], BRANCO, 6.7)                          # dentinhos
    if t == 2:
        px(P, [(26, 16 + dy), (27, 16 + dy), (28, 17 + dy)], '#f04f78', 6.7)    # língua
    if t == 3:
        px(P, [(17, 11 + dy), (18, 11 + dy), (19, 11 + dy)], OUT, 7)
    else:
        px(P, [(17, 10 + dy), (18, 10 + dy), (19, 10 + dy), (17, 11 + dy), (18, 11 + dy), (19, 11 + dy)], '#f9c22b', 7)
        px(P, [(18, 10 + dy), (18, 11 + dy)], OUT, 7.1)
        px(P, [(17, 10 + dy)], BRANCO, 7.2)
    px(P, [(16, 9 + dy), (17, 8 + dy), (18, 8 + dy), (19, 9 + dy)], '#9e4539', 7)  # crista
    # braço da frente (segura a lança)
    parte(P, capsula(16, 19 + dy, 24, 20 + dy, 1.3), 'escama_lj', 8)
    parte(P, elipse(26, 19.5 + dy, 1.7, 1.7), 'escama_lj', 8.1)
    return desenhar(P, 32, 32)


def fantasma_mineiro(t):
    """Fantasma Mineiro (32): fantasma azul-esverdeado com capacete de mineiro amolgado e vela, olhos fundos a
    brilhar, boca triste aberta, cauda de fumo ondulante e uma picareta fantasma na mão."""
    P = []
    dy = BOB[t]
    w = [0, 1, 0, -1][t]
    # cauda de fumo (ondula)
    cauda = poligono([(12, 15 + dy), (23, 15 + dy), (22, 20 + dy), (18, 23 + dy), (14 + w, 25 + dy),
                      (10 + w, 27 + dy), (8 + w, 26 + dy), (10, 22 + dy), (11, 19 + dy)])
    parte(P, cauda, 'fantasma', 2, plano=True)
    px(P, [(12 + w, 23 + dy), (11 + w, 24 + dy), (14, 20 + dy), (13, 21 + dy)], '#30e1b9', 2.1)
    px(P, [(18, 21 + dy), (16, 22 + dy)], '#0b5e65', 2.1)
    # pedacinhos de fumo soltos
    px(P, [(7 - w, 29 + dy), (6, 24 - dy)], '#0eaf9b', 2)
    # braço e picareta fantasma
    parte(P, capsula(26, 22 + dy, 28, 11 + dy, 0.6), ['#0b5e65', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9'], 3)
    parte(P, poligono([(24, 12 + dy), (27, 9 + dy), (30, 10 + dy), (31, 13 + dy), (28, 11 + dy)]),
          ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'], 3.1, plano=True)
    # corpo/cabeça
    corpo = parte(P, elipse(17.5, 14 + dy, 6.5, 6.5), 'fantasma', 4)
    px(P, [(13, 12 + dy), (14, 11 + dy), (13, 13 + dy)], '#8ff8e2', 4.1)
    parte(P, capsula(21, 18 + dy, 25.5, 20 + dy, 1.4), 'fantasma', 5)                 # braço
    # cara: olhos fundos e boca triste
    for ex in (18, 22):
        px(P, elipse(ex + 0.5, 13.5 + dy, 1.5, 2), OUT, 6)
        px(P, [(ex, 13 + dy + (t == 2))], '#8ff8e2', 6.1)
    px(P, [(17, 11 + dy), (18, 10 + dy), (22, 10 + dy), (23, 11 + dy)], '#0b5e65', 6)   # sobrancelhas tristes
    px(P, elipse(21, 18 + dy, 1.3, 1.6 + (t % 2) * 0.4), OUT, 6)
    # capacete amolgado com vela
    cap = {p for p in elipse(17, 9.5 + dy, 6.6, 4.6) if p[1] <= 9 + dy}
    parte(P, cap, ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#fbff86'], 7)
    parte(P, retangulo(10, 9 + dy, 24, 10 + dy), ['#4c3e24', '#4c3e24', '#676633', '#a2a947', '#a2a947'], 7.2, plano=True)
    px(P, [(14, 7 + dy)], '#4c3e24', 7.3)                                         # amolgadela
    parte(P, retangulo(18, 4 + dy, 19, 6 + dy), 'branco', 7.4, plano=True)       # vela
    chama = [(18, 3 + dy), (19, 2 + dy), (18, 2 + dy)] if t % 2 == 0 else [(18, 3 + dy), (18, 2 + dy), (18, 1 + dy)]
    px(P, chama, '#30e1b9', 7.5)
    px(P, [(18, 3 + dy)], '#8ff8e2', 7.6)
    return desenhar(P, 32, 32)


def racha(P, pts, z, cor=OUT, luz='#9babb2'):
    """Uma racha na pedra: linha escura com um fio claro por baixo/à direita."""
    linha_px = []
    for a, b in zip(pts, pts[1:]):
        linha_px += linha(a[0], a[1], b[0], b[1])
    px(P, linha_px, cor, z)
    if luz:
        px(P, [(x + 1, y + 1) for x, y in linha_px[::2]], luz, z - 0.0005)


def golem_de_pedra(t):
    """Golem de Pedra (48): corpo de pedregulhos encaixados (bossa nas costas, peito, barriga), cabeça pequena
    enterrada nos ombros com olhos de brasa, braços enormes até ao chão, rachas, musgo, veios de ferro e um
    cristalzinho. Respira devagar e solta uma pedrinha."""
    P = []
    dy = RESP[t]
    pedra, esc = 'pedra_cl', ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
    # pernas
    parte(P, elipse(18, 41, 4.5, 5), esc, 1)
    parte(P, retangulo(13, 43, 23, 46, canto=1), esc, 1.1, plano=True)
    parte(P, elipse(28, 41, 5, 5), pedra, 2)
    parte(P, retangulo(23, 43, 34, 46, canto=1), pedra, 2.1, plano=True)
    # braço de trás
    parte(P, capsula(15, 22 + dy, 11, 34 + dy, 4), esc, 2.5)
    parte(P, elipse(11, 38 + dy * 0.5, 4.5, 4), esc, 2.6)
    # corpo: bossa, peito e barriga
    bossa = parte(P, elipse(17, 21 + dy, 9, 9), pedra, 3)
    barriga = parte(P, elipse(24, 34 + dy, 9, 6.5), esc, 3.5)
    peito = parte(P, elipse(26, 25 + dy, 9, 8), pedra, 4)
    for i, m in enumerate((bossa, peito)):
        textura(P, m, 'pedra', 3 + i, s=40 + i, escuro=0.1, claro=0.05)
    racha(P, [(12, 18 + dy), (15, 21 + dy), (14, 25 + dy)], 4.5)
    racha(P, [(28, 29 + dy), (25, 31 + dy), (26, 34 + dy)], 4.6)
    # veio de ferro (ferrugem) e um cristalzinho a sair da bossa
    px(P, [(20, 25 + dy), (21, 26 + dy), (22, 26 + dy)], '#cd683d', 4.7)
    px(P, [(21, 25 + dy)], '#f57d4a', 4.71)
    cristal(P, 12, 15 + dy, math.radians(-120), 6, 1.6, 'cristal_t', 3.2)
    # musgo em cima da bossa e dos ombros
    musgo = {p for p in elipse(17, 14 + dy, 7, 3) if p in bossa and p[1] <= 15 + dy}
    parte(P, musgo, 'verde_esc', 3.3, separar=False)
    px(P, [(14, 12 + dy), (17, 12 + dy), (20, 13 + dy)], '#b2ba90', 3.31)
    # cabeça pequena e afundada
    cab = parte(P, elipse(33, 17 + dy, 5.5, 4.8), pedra, 5)
    parte(P, capsula(29, 14 + dy, 38, 14.5 + dy, 1.6), esc, 5.5, volume='cilindro_h')     # sobrolho
    brasa = ['#f79617', '#f9c22b', '#fbff86', '#f9c22b'][t]
    px(P, [(33, 16 + dy), (34, 16 + dy), (35, 16 + dy)], OUT, 5.6)
    px(P, [(34, 16 + dy), (35, 16 + dy)], brasa, 5.7)
    px(P, [(35, 16 + dy)], BRANCO, 5.8)
    px(P, [(33, 20 + dy), (34, 20 + dy), (35, 19 + dy), (37, 20 + dy)], OUT, 5.6)          # boca rachada
    # braço da frente (ombro de pedregulho, antebraço e punho grande)
    parte(P, elipse(30, 24 + dy, 5.5, 5), pedra, 6)
    parte(P, capsula(32, 27 + dy, 35, 35 + dy, 3.6), pedra, 6.1)
    punho = parte(P, elipse(36, 39 + dy * 0.5, 5, 4.6), pedra, 6.2)
    px(P, [(38, 37 + dy), (39, 39 + dy), (38, 41 + dy)], '#625565', 6.3)                 # nós dos dedos
    px(P, [(27, 22 + dy), (28, 21 + dy), (29, 21 + dy)], '#547e64', 6.3)                 # musgo no ombro
    racha(P, [(33, 30 + dy), (35, 32 + dy)], 6.4)
    # pedrinha a cair
    if t in (1, 2, 3):
        y = [0, 30, 36, 42][t]
        px(P, [(41, y), (42, y)], '#7f708a', 7)
    return desenhar(P, 48, 48)


def lagarta_de_cristal(t):
    """Lagarta de Cristal (48): corpo verde em gomos que ondulam, barriga clara, pintas, patinhas, cristais
    (água, roxo, azul) nas costas que brilham à vez, cabeça com olho grande, mandíbulas e antenas de cristal."""
    P = []
    n = 6
    cores = ['cristal_t', 'cristal_r', 'cristal_a', 'cristal_t', 'cristal_r', 'cristal_a']
    gomos = []
    for i in range(n):
        x = 6 + i * 6.2
        y = 38 + math.sin(i * 1.1 - t * math.pi / 2) * 1.2
        r = 5.2 + i * 0.25
        gomos.append((x, y, r))
    # patinhas
    for i, (x, y, r) in enumerate(gomos):
        parte(P, capsula(x, y + r - 1, x + 1, 45.5, 0.9), 'verde_esc', 0.5 + i * 0.01)
    for i, (x, y, r) in enumerate(gomos):
        g = parte(P, elipse(x, y, r, r * 0.95), 'verde', 2 + i * 0.1)
        barriga = {p for p in g if p[1] >= y + r * 0.45}
        px(P, barriga, '#cddf6c', 2 + i * 0.1 + 0.001)
        px(P, [(int(x) + 1, int(y) - 1), (int(x) - 2, int(y) + 1)], '#165a4c', 2 + i * 0.1 + 0.002)   # pintas
        px(P, [(int(x) - 2, int(y - r * 0.6))], '#cddf6c', 2 + i * 0.1 + 0.002)
    # cristais nas costas (atrás do gomo seguinte, à frente do próprio)
    for i, (x, y, r) in enumerate(gomos[:-1]):
        comp = 6 + (i % 3) * 2.5
        ang = math.radians(-100 - (5 - i) * 4)
        cristal(P, x, y - r + 2, ang, comp, 1.8 + (i % 2) * 0.5, cores[i], 1.5 + i * 0.1, brilho=(i + t) % 3 == 0)
        if i % 2 == 0:
            cristal(P, x + 2.5, y - r + 2.5, math.radians(-70), comp * 0.6, 1.3, cores[(i + 1) % 3], 1.55 + i * 0.1, brilho=False)
    # brilhos dos cristais a piscar
    pts = [(int(gomos[i][0] + 1), int(gomos[i][1] - gomos[i][2] - 6 - (i % 3) * 2)) for i in (0, 2, 4)]
    brilhos(P, pts, 9, t, cor2='#8ff8e2')
    # cabeça
    hx, hy, _ = gomos[-1]
    hx += 4
    cab = parte(P, elipse(hx, hy - 1, 6, 5.8), 'verde', 4)
    px(P, [(int(hx) + 4 + i, int(hy) + 2) for i in range(3)], OUT, 4.1)               # boca
    parte(P, capsula(hx + 5, hy + 3, hx + 7, hy + 5, 1), 'osso', 4.2)                    # mandíbula
    olho(P, int(hx) + 1, int(hy) - 4, '#323353', 4.3, tam=2, pupila='#2e222f')
    px(P, [(int(hx) + 1, int(hy) - 4), (int(hx) + 2, int(hy) - 4)], '#8fd3ff', 4.31)
    px(P, [(int(hx) + 1, int(hy) - 4)], BRANCO, 4.32)
    # antenas com uma pontinha de cristal
    a = [0, 1, 0, -1][t]
    for (dx, z) in ((-1, 3.5), (2, 4.4)):
        parte(P, capsula(hx + dx, hy - 6, hx + dx + 3 + a, hy - 12, 0.6), 'verde_esc', z)
        px(P, [(hx + dx + 3 + a, hy - 13), (hx + dx + 4 + a, hy - 13)], '#30e1b9', z + 0.01)
        px(P, [(hx + dx + 3 + a, hy - 13)], BRANCO, z + 0.02)
    return desenhar(P, 48, 48)


def rei_goblin_gruk(t):
    """Rei Goblin Gruk (48): goblin gordo de barriga à mostra, colete vermelho, capa com pele de arminho, coroa de
    latão com uma pedra vermelha, presas, sobrolho zangado e o Martelo de Vagoneta pousado no chão."""
    P = []
    dy = RESP[t]
    gob_esc = ['#165a4c', '#165a4c', '#239063', '#1ebc73', '#91db69']
    # capa (atrás)
    capa = poligono([(16, 18 + dy), (24, 18 + dy), (21, 44), (15, 45), (9, 44), (11, 30)])
    parte(P, capa, 'pano_vm', 0.5, volume='cilindro_v')
    px(P, [(12, 34), (13, 38), (11, 41)], '#6e2727', 0.51)
    # pernas e botas
    parte(P, capsula(20, 38, 19, 43, 2.5), 'pano', 1)
    parte(P, capsula(28, 38, 29, 43, 2.6), 'pano', 3)
    parte(P, elipse(19, 45, 3.6, 1.8), 'terra', 1.2)
    parte(P, elipse(30.5, 45, 4, 1.8), 'terra', 3.2)
    # braço de trás (mão na anca)
    parte(P, capsula(17, 25 + dy, 14, 32 + dy, 2.2), gob_esc, 2)
    # barriga e colete
    bar = parte(P, elipse(25, 32 + dy, 10, 8.5), 'goblin', 4)
    px(P, [(29, 34 + dy), (30, 33 + dy)], '#239063', 4.01)                            # umbigo
    textura(P, bar, 'goblin', 4, s=51, escuro=0.05, claro=0.04)
    colete = {p for p in elipse(24, 30 + dy, 10.5, 9) if p[0] <= 25 - (p[1] - 22 - dy) * 0.3}
    parte(P, colete, 'pano_vm', 4.5)
    px(P, [(x, 37 + dy) for x in range(16, 33)], '#4c3e24', 4.6)                     # cinto
    parte(P, retangulo(27, 36 + dy, 30, 38 + dy), 'ouro', 4.7, plano=True)
    px(P, [(28, 37 + dy)], '#9e4539', 4.8)
    # pele de arminho nos ombros
    pele = capsula(15, 21 + dy, 27, 21 + dy, 2.6)
    parte(P, pele, 'branco', 5)
    px(P, [(17, 21 + dy), (21, 22 + dy), (25, 21 + dy)], OUT, 5.1)
    # martelo de vagoneta pousado no chão
    parte(P, capsula(35, 30 + dy, 39, 38, 1), 'madeira', 5.5)
    cab = retangulo(33, 38, 46, 45, canto=1)
    parte(P, cab, 'ferro_esc', 5.6, plano=True)
    parte(P, retangulo(33, 38, 46, 39), 'cobre', 5.65, plano=True)
    px(P, [(35, 42), (40, 42), (44, 42)], '#9babb2', 5.7)                           # rebites
    px(P, [(36, 41)], BRANCO, 5.71)
    # cabeça
    parte(P, poligono([(23, 13 + dy), (13, 9 + dy), (16, 13 + dy), (23, 17 + dy)]), 'goblin', 6, plano=True)   # orelha
    px(P, [(16, 11 + dy), (18, 12 + dy), (20, 13 + dy)], '#239063', 6.01)
    cab = parte(P, elipse(28, 16 + dy, 7, 6), 'goblin', 6.5)
    textura(P, cab, 'goblin', 6.5, s=52, escuro=0.08, claro=0.04)
    parte(P, capsula(33, 16 + dy, 37, 18 + dy, 2), 'goblin', 7)                        # nariz
    px(P, [(37, 19 + dy)], '#239063', 7.01)
    # boca com presas
    px(P, [(x, 21 + dy) for x in range(28, 35)], OUT, 7.1)
    px(P, [(29, 20 + dy), (29, 19 + dy), (34, 20 + dy)], BRANCO, 7.2)
    # olho zangado
    if t == 3:
        px(P, [(30, 15 + dy), (31, 15 + dy), (32, 15 + dy)], OUT, 7.3)
    else:
        olho(P, 30, 14 + dy, '#f9c22b', 7.3)
        px(P, [(29, 15 + dy)], '#f9c22b', 7.3)
    px(P, [(28, 12 + dy), (29, 12 + dy), (30, 13 + dy), (31, 13 + dy), (32, 13 + dy)], '#165a4c', 7.4)
    # coroa de latão
    coroa = retangulo(22, 8 + dy, 32, 10 + dy) | poligono([(22, 8 + dy), (23, 3 + dy), (25, 8 + dy)]) \
        | poligono([(26, 8 + dy), (27.5, 2 + dy), (29, 8 + dy)]) | poligono([(30, 8 + dy), (32, 4 + dy), (33, 8 + dy)])
    parte(P, coroa, 'ouro', 8)
    px(P, [(27, 9 + dy), (28, 9 + dy)], '#e83b3b', 8.1)
    px(P, [(27, 9 + dy)], '#fca790', 8.2)
    px(P, [(23, 3 + dy), (27, 2 + dy), (32, 4 + dy)], '#fbff86', 8.2)
    # braço da frente (segura o martelo)
    parte(P, capsula(29, 24 + dy, 34, 29 + dy, 2.4), 'goblin', 9)
    parte(P, elipse(35, 30 + dy, 2.3, 2.2), 'goblin', 9.1)
    return desenhar(P, 48, 48)
