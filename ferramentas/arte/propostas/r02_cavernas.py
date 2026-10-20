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
    """Um número 'ao acaso' mas sempre igual para o mesmo píxel (a textura não tremeluz entre quadros)."""
    return random.Random((x + 1000) * 100003 + (y + 1000) * 1009 + s * 7919).random()


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
        S, E, T = (16, 14), (10, 17), (3, 21)
        borda = [(5, 24), (8, 22), (11, 24), (14, 20)]
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
    pelo_cab = pelo if dourada else ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
    cab = parte(P, elipse(X(25), 22 + dy * 0.5 + (1 - k) * 3, 4.8 * k, 4.4 * k), pelo_cab, 4)
    textura(P, cab, pelo_cab, 4, s=12, escuro=0.1, claro=0.06, traco=1)
    barriga = {p for p in corpo if p[1] >= max(q[1] for q in corpo) - 1 and X(8) < p[0] < X(21)}
    px(P, barriga, '#966c6c' if not dourada else '#fbff86', 2.01)
    fy = 23.5 + (1 - k) * 3 + dy * 0.5
    parte(P, capsula(X(27), fy, X(30) + fz, fy + 0.5 - fz * 0.5, 1.6 * k), 'rosa', 5)
    px(P, [(X(30) + fz + 1, fy - fz * 0.5)], '#831c5d', 5.1)
    if t == 3:
        px(P, [(X(26), fy - 2), (X(27), fy - 2)], OUT, 6)
    else:
        px(P, [(X(26), fy - 3), (X(27), fy - 3), (X(26), fy - 2), (X(27), fy - 2)], OUT, 6)
        px(P, [(X(26), fy - 3)], BRANCO, 6.1)
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
    # corpo/cabeça
    corpo = parte(P, elipse(17.5, 14.5 + dy, 6.8, 6.5), 'fantasma', 4)
    px(P, [(13, 12 + dy), (14, 11 + dy), (13, 13 + dy)], '#8ff8e2', 4.1)
    mao = [0, 1, 1, 0][t]
    parte(P, capsula(21, 20 + dy, 26, 21 + dy - mao, 1.3), 'fantasma', 5)                 # braço a estender
    px(P, [(27, 20 + dy - mao), (28, 21 + dy - mao), (27, 22 + dy - mao)], '#30e1b9', 5.1)   # dedos
    # cara: olhos fundos a brilhar e boca triste
    for ex in (17, 21):
        px(P, [(ex, 13 + dy), (ex + 1, 13 + dy), (ex, 14 + dy), (ex + 1, 14 + dy), (ex, 15 + dy), (ex + 1, 15 + dy)], OUT, 6)
        px(P, [(ex + 1, 14 + dy)], '#8ff8e2' if t != 2 else BRANCO, 6.1)
    px(P, [(16, 12 + dy), (22, 12 + dy)], '#0b5e65', 6)   # sobrancelhas tristes
    px(P, [(19, 17 + dy), (20, 17 + dy), (19, 18 + dy), (20, 18 + dy)] + ([(19, 19 + dy), (20, 19 + dy)] if t % 2 else []), OUT, 6)
    # capacete amolgado com vela
    cap = {p for p in elipse(17, 10 + dy, 6, 5.5) if p[1] <= 9 + dy}
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
        textura(P, m, 'pedra_cl', 3 + i, s=40 + i, escuro=0.08, claro=0.05)
    racha(P, [(12, 18 + dy), (15, 21 + dy), (14, 25 + dy)], 4.5)
    racha(P, [(28, 29 + dy), (25, 31 + dy), (26, 34 + dy)], 4.6)
    # veio de ferro (ferrugem) e um cristalzinho a sair da bossa
    px(P, [(20, 25 + dy), (21, 26 + dy), (22, 26 + dy)], '#cd683d', 4.7)
    px(P, [(21, 25 + dy)], '#f57d4a', 4.71)
    cristal(P, 13, 16 + dy, math.radians(-115), 10, 2.4, 'cristal_t', 3.2, brilho=t in (0, 1))
    cristal(P, 17, 14 + dy, math.radians(-80), 6, 1.8, 'cristal_a', 3.21, brilho=t == 2)
    # musgo em cima da bossa e dos ombros
    musgo = {p for p in elipse(17, 14 + dy, 7, 3) if p in bossa and p[1] <= 15 + dy}
    parte(P, musgo, 'verde_esc', 3.3, separar=False)
    px(P, [(14, 12 + dy), (17, 12 + dy), (20, 13 + dy)], '#b2ba90', 3.31)
    # cabeça pequena e afundada
    cab = parte(P, elipse(36, 15 + dy, 6, 5.2), pedra, 6.5)
    parte(P, capsula(32, 11.5 + dy, 41, 12 + dy, 1.4), pedra, 6.55, volume='cilindro_h')   # sobrolho
    brasa = ['#f79617', '#f9c22b', '#fbff86', '#f9c22b'][t]
    for ex in (36, 40):
        px(P, [(ex - 1, 14 + dy), (ex, 14 + dy), (ex + 1, 14 + dy), (ex - 1, 15 + dy), (ex, 15 + dy), (ex + 1, 15 + dy)], OUT, 6.6)
        px(P, [(ex, 14 + dy), (ex, 15 + dy), (ex - 1, 15 + dy)], brasa, 6.7)
        px(P, [(ex, 14 + dy)], BRANCO, 6.8)
    px(P, [(35, 18 + dy), (36, 19 + dy), (37, 18 + dy), (38, 19 + dy), (39, 18 + dy), (40, 19 + dy)], OUT, 6.6)   # boca rachada
    px(P, [(32, 10 + dy), (33, 9 + dy), (35, 9 + dy), (36, 9 + dy)], '#547e64', 6.9)        # musgo na cabeça
    px(P, [(34, 9 + dy)], '#92a984', 6.91)
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
        comp = 9 + (i % 3) * 3 - (1 if i == 0 else 0)
        ang = math.radians(-100 - (5 - i) * 4)
        cristal(P, x, y - r + 2, ang, comp, 2.6 + (i % 2) * 0.5, cores[i], 1.5 + i * 0.1, brilho=(i + t) % 3 == 0)
        if i % 2 == 0:
            cristal(P, x + 3, y - r + 3, math.radians(-65), comp * 0.6, 1.8, cores[(i + 1) % 3], 1.55 + i * 0.1, brilho=False)
    # brilhos dos cristais a piscar
    pts = [(int(gomos[i][0] - 2), int(gomos[i][1] - gomos[i][2] - 9 - (i % 3) * 3)) for i in (1, 2, 4)]
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
    pele = capsula(19, 21 + dy, 31, 22 + dy, 2.2)
    parte(P, pele, 'branco', 5)
    px(P, [(21, 22 + dy), (25, 21 + dy), (29, 22 + dy)], OUT, 5.1)
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


# =====================================================================================
#  GUARDIÕES
# =====================================================================================

def vagoneta_assombrada(t):
    """Vagoneta Assombrada (48): caixa de ferro com tiras e rebites, ferrugem, carvão em brasa por cima, olhos de
    fogo zangados à frente, boca de dentes de carril, rodas com raios e fumo fantasma roxo a sair."""
    P = []
    dy = [0, 1, 0, 1][t]
    # fumo fantasma (atrás)
    for i, (x, y) in enumerate(((10, 12), (7, 6), (12, 2))):
        yy = y - t + (i * 2) % 3
        parte(P, elipse(x + (t % 2), yy + 3, 2.6 - i * 0.5, 2.2 - i * 0.4), ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'], 0.2 + i * 0.01)
    # rodas
    for (wx, z) in ((14, 1), (35, 1.1)):
        r = parte(P, elipse(wx, 41, 4.6, 4.6), 'ferro_esc', z)
        px(P, [(wx, 41), (wx - 1, 41)], '#9babb2', z + 0.01)
        ang = t * math.pi / 4
        for k in range(2):
            a = ang + k * math.pi / 2
            px(P, [(wx + math.cos(a) * d, 41 + math.sin(a) * d) for d in (-3, -2, 2, 3)], '#3e3546', z + 0.02)
    # carvão em brasa por cima
    for i, (x, r) in enumerate(((12, 4), (19, 4.5), (26, 4.2), (33, 4), (39, 3.4))):
        parte(P, elipse(x, 21 + dy - (i % 2), r, 3.2), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#7f708a'], 2 + i * 0.01)
    brasas = [(13, 19), (20, 18), (27, 19), (34, 19), (17, 20), (31, 18)]
    for i, (x, y) in enumerate(brasas):
        c = ['#ea4f36', '#f79617', '#f9c22b', '#fb6b1d'][(i + t) % 4]
        px(P, [(x, y + dy), (x + 1, y + dy)], c, 2.2)
        if (i + t) % 3 == 0:
            px(P, [(x, y + dy - 1)], '#fbff86', 2.21)
    # caixa
    caixa = poligono([(5, 23 + dy), (44, 23 + dy), (41, 39 + dy), (8, 39 + dy)])
    parte(P, caixa, 'ferro_esc', 3, volume='cilindro_h')
    textura(P, caixa, 'ferro_esc', 3, s=61, escuro=0.06, claro=0.04)
    # ferrugem
    for (x, y) in ((10, 33), (11, 34), (12, 35), (16, 36), (39, 36), (38, 37)):
        px(P, [(x, y + dy)], '#9e4539', 3.01)
    px(P, [(11, 35 + dy), (39, 37 + dy)], '#cd683d', 3.02)
    # aro de cima e tiras com rebites
    parte(P, retangulo(4, 22 + dy, 45, 24 + dy), 'ferro', 3.5, plano=True)
    for x in (13, 22):
        parte(P, retangulo(x, 25 + dy, x + 1, 38 + dy), 'ferro', 3.6, plano=True)
        for y in (27, 31, 35):
            px(P, [(x, y + dy)], BRANCO, 3.61)
    for x in (7, 16, 26, 36, 42):
        px(P, [(x, 23 + dy)], BRANCO, 3.62)
    # cara à frente: olhos de brasa zangados
    for ex in (28, 36):
        px(P, elipse(ex + 1, 29 + dy, 2.6, 2.2), OUT, 4)
        px(P, elipse(ex + 1, 29.5 + dy, 1.6, 1.3), '#f79617' if t != 2 else '#f9c22b', 4.1)
        px(P, [(ex + 1, 29 + dy), (ex, 29 + dy)], '#fbff86', 4.2)
        px(P, [(ex, 28 + dy)], BRANCO, 4.3)
    px(P, [(26, 26 + dy), (27, 26 + dy), (28, 27 + dy), (29, 27 + dy), (35, 27 + dy), (36, 27 + dy), (37, 26 + dy), (38, 26 + dy)], OUT, 4.4)
    # boca de dentes de carril
    boca = retangulo(26, 33 + dy, 40, 36 + dy)
    px(P, boca, OUT, 4.5)
    px(P, [(x, 33 + dy) for x in range(27, 40, 2)] + [(x, 36 + dy) for x in range(28, 40, 2)], '#c7dcd0', 4.6)
    px(P, [(x, 34 + dy) for x in range(27, 40, 4)], '#9babb2', 4.6)
    px(P, [(x, 35 + dy) for x in range(30, 40, 4)], '#ea4f36', 4.6)
    return desenhar(P, 48, 48)


def touro_das_galerias(t):
    """Touro das Galerias (64): homem-touro mineiro com pelo ruivo às riscas, cornos grandes, argola de latão no
    focinho, capacete com lanterna, picareta gigante ao ombro, cinto e saiote, cascos; bufa vapor pelo nariz."""
    P = []
    dy = RESP[t]
    pelo = 'pelo_touro'
    pelo_esc = ['#2e222f', '#45293f', '#7a3045', '#9e4539', '#cd683d']
    # picareta gigante ao ombro (atrás)
    parte(P, capsula(44, 38 + dy, 17, 9 + dy, 1.3), 'madeira', 0.5)
    pic = poligono([(7, 19 + dy), (11, 11 + dy), (17, 6 + dy), (25, 3 + dy), (27, 5 + dy), (19, 9 + dy), (14, 13 + dy), (9, 20 + dy)])
    parte(P, pic, 'ferro', 0.6, plano=True)
    px(P, [(12, 12 + dy), (16, 8 + dy), (20, 6 + dy)], BRANCO, 0.61)
    px(P, [(8, 19 + dy), (26, 4 + dy)], '#c7dcd0', 0.61)
    # pernas (de trás e da frente) com cascos
    parte(P, capsula(28, 46, 27, 54, 4.2), pelo_esc, 1)
    parte(P, capsula(27, 54, 28, 59, 3), pelo_esc, 1.1)
    parte(P, retangulo(24, 59, 31, 62, canto=1), 'pedra', 1.2, plano=True)
    parte(P, capsula(38, 46, 40, 54, 4.5), pelo, 3)
    parte(P, capsula(40, 54, 40, 59, 3.2), pelo, 3.1)
    parte(P, retangulo(36, 59, 44, 62, canto=1), 'pedra', 3.2, plano=True)
    px(P, [(40, 60), (40, 61)], OUT, 3.3)                                           # casco fendido
    # braço de trás
    parte(P, capsula(25, 28 + dy, 21, 42 + dy, 4), pelo_esc, 2)
    parte(P, elipse(21, 44 + dy, 3.6, 3.4), pelo_esc, 2.1)
    # tronco
    tronco = parte(P, elipse(33, 33 + dy, 12, 12), pelo, 4)
    textura(P, tronco, pelo, 4, s=71, escuro=0.12, claro=0.05, traco=1)
    peito = {p for p in elipse(37, 31 + dy, 6, 6)}
    px(P, interior(peito) & tronco, '#cd683d', 4.01)
    racha(P, [(30, 26 + dy), (34, 30 + dy)], 4.05, cor='#7a3045', luz='#e6904e')       # cicatriz
    # saiote e cinto
    sai = poligono([(22, 40 + dy), (45, 40 + dy), (46, 49), (21, 49)])
    parte(P, sai, 'pano', 4.5, plano=True)
    px(P, [(27, 42 + dy), (27, 48), (33, 42 + dy), (33, 48), (39, 42 + dy), (39, 48)], '#45293f', 4.51)
    parte(P, retangulo(21, 39 + dy, 46, 41 + dy), 'terra', 4.6, plano=True)
    parte(P, retangulo(36, 38 + dy, 40, 42 + dy), 'ouro', 4.7, plano=True)
    px(P, [(38, 40 + dy)], '#9e4539', 4.71)
    # cabeça de touro
    cab = parte(P, elipse(45, 18 + dy, 7.5, 6.5), pelo, 6)
    textura(P, cab, pelo, 6, s=72, escuro=0.1, claro=0.05, traco=1)
    foc = parte(P, elipse(52, 23 + dy, 5.2, 4.2), ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fca790'], 6.5)
    px(P, [(54, 22 + dy), (56, 22 + dy)], OUT, 6.6)                                  # narinas
    parte(P, elipse(55, 26 + dy, 2.4, 2.2) - elipse(55, 26 + dy, 1, 1), 'ouro', 6.7)   # argola
    px(P, [(49, 26 + dy), (50, 26 + dy), (51, 26 + dy)], '#45293f', 6.6)             # boca
    # olho vermelho zangado
    if t == 3:
        px(P, [(47, 16 + dy), (48, 16 + dy), (49, 16 + dy)], OUT, 6.8)
    else:
        olho(P, 47, 15 + dy, '#e83b3b', 6.8)
        px(P, [(49, 16 + dy)], '#e83b3b', 6.8)
    px(P, [(46, 13 + dy), (47, 13 + dy), (48, 14 + dy), (49, 14 + dy), (50, 14 + dy)], '#45293f', 6.9)
    # orelha
    parte(P, poligono([(39, 16 + dy), (34, 18 + dy), (39, 20 + dy)]), pelo, 5.5, plano=True)
    # cornos
    for (pts, z) in (([(40, 12), (36, 9), (34, 4), (36, 3), (38, 7), (43, 10)], 5.8),
                     ([(47, 11), (52, 8), (55, 2), (57, 3), (55, 10), (49, 14)], 7.5)):
        parte(P, poligono([(x, y + dy) for x, y in pts]), 'osso', z, plano=True)
        px(P, [(pts[2][0] + 1, pts[2][1] + dy + 1)], '#9babb2', z + 0.01)
    # capacete com lanterna
    capa = {p for p in elipse(44, 12 + dy, 6.5, 4.5) if p[1] <= 12 + dy}
    parte(P, capa, 'ouro', 7)
    parte(P, retangulo(37, 12 + dy, 51, 12 + dy), ['#4c3e24', '#4c3e24', '#9e4539', '#cd683d', '#cd683d'], 7.1, plano=True)
    parte(P, elipse(49.5, 9.5 + dy, 2, 2), 'ferro', 7.2)
    px(P, [(50, 9 + dy), (51, 9 + dy)] + ([(51, 10 + dy)] if t % 2 else []), '#fbff86', 7.3)
    px(P, [(50, 9 + dy)], BRANCO, 7.31)
    # braço da frente (segura a picareta)
    parte(P, elipse(39, 29 + dy, 6, 5.5), pelo, 8)
    parte(P, capsula(41, 32 + dy, 44, 38 + dy, 3.6), pelo, 8.1)
    parte(P, elipse(45, 39 + dy, 3.6, 3.4), pelo, 8.2)
    parte(P, retangulo(40, 34 + dy, 45, 35 + dy), 'terra', 8.3, plano=True)          # braçadeira
    # vapor a sair do nariz
    if t in (1, 2):
        k = t - 1
        px(P, [(58 + k, 21 + dy - k), (59 + k, 21 + dy - k), (60 + k * 2, 20 + dy - k)], '#c7dcd0', 9)
        px(P, [(61 + k, 19 + dy - k)], '#9babb2', 9)
    return desenhar(P, 64, 64)


def prisma_vivo(t):
    """Prisma Vivo (48): cristal flutuante facetado (água à esquerda, rosa à direita) com arestas claras, um núcleo
    vivo a pulsar com um olho, lascas que giram à volta e brilhos."""
    P = []
    dy = BOB[t]
    cx, cy = 24, 22 + dy
    top, dir_, baixo, esq = (cx, 3 + dy), (cx + 11, cy), (cx, 42 + dy), (cx - 11, cy)
    meio_t, meio_b = (cx + 1, cy - 2), (cx + 1, cy + 2)
    # lascas que giram (as de trás primeiro)
    for k in range(3):
        a = t * math.pi / 2 + k * 2 * math.pi / 3
        x, y = cx + math.cos(a) * 17, cy + math.sin(a) * 9
        z = 5 if math.sin(a) > 0 else 0.5
        cristal(P, x, y + 2, math.radians(-90), 5, 1.5, ['cristal_t', 'cristal_p', 'cristal_a'][k], z, brilho=False)
    tudo = poligono([top, dir_, baixo, esq])
    parte(P, tudo, 'cristal_t', 2)
    px(P, poligono([top, meio_t, esq]) & tudo, '#8ff8e2', 2.01)
    px(P, poligono([esq, meio_b, baixo]) & tudo, '#0eaf9b', 2.01)
    px(P, poligono([top, dir_, meio_t]) & tudo, '#f68181', 2.01)
    px(P, poligono([dir_, baixo, meio_b]) & tudo, '#c32454', 2.01)
    px(P, poligono([esq, meio_t, dir_, meio_b]) & tudo, '#30e1b9', 2.005)
    # arestas claras
    px(P, linha(top[0] - 1, top[1] + 2, esq[0] + 2, esq[1] - 1), '#ffffff', 2.02)
    px(P, linha(top[0], top[1] + 1, meio_t[0], meio_t[1] - 3), '#fdcbb0', 2.02)
    px(P, linha(esq[0] + 2, esq[1], dir_[0] - 2, dir_[1]), '#8ff8e2', 2.015)
    # riscos internos (veios do cristal)
    px(P, [(cx - 5, cy + 6), (cx - 4, cy + 7), (cx - 3, cy + 9), (cx + 5, cy - 7), (cx + 6, cy - 6)], '#0b8a8f', 2.03)
    # núcleo com olho
    r = [3.4, 3.8, 4.2, 3.8][t]
    px(P, elipse(cx + 1, cy, r + 1, r + 1), '#831c5d', 3)
    px(P, elipse(cx + 1, cy, r, r), '#eaaded', 3.1)
    px(P, elipse(cx + 1, cy, r - 1.3, r - 1.3), '#ffffff', 3.2)
    px(P, [(cx + 1, cy - 1), (cx + 2, cy - 1), (cx + 1, cy), (cx + 2, cy), (cx + 1, cy + 1), (cx + 2, cy + 1)], '#6b3e75', 3.3)
    px(P, [(cx + 2, cy), (cx + 2, cy - 1)], OUT, 3.4)
    px(P, [(cx + 1, cy - 1)], '#ffffff', 3.5)
    brilhos(P, [(cx - 7, 9 + dy), (cx + 9, cy + 12), (cx - 13, cy + 9)], 6, t)
    return desenhar(P, 48, 48)


def reflexo_negro(t):
    """Reflexo Negro (32): a tua silhueta feita de sombra, com cabelo espetado, contorno de luz roxa, olhos roxos a
    brilhar, uma katana negra de fio roxo e fumo de sombra a sair dos pés e da cabeça."""
    P = []
    dy = RESP[t]
    S = ['#2e222f', '#3e3546', '#45293f', '#6b3e75', '#905ea9']
    # fumo de sombra (atrás)
    for i, (x, y) in enumerate(((9, 28), (24, 29), (12, 5), (18, 3))):
        yy = y - (t + i) % 3
        px(P, [(x + (t + i) % 2, yy), (x + 1 + (t + i) % 2, yy)], '#45293f', 0.2)
    # katana (atrás do braço)
    parte(P, capsula(21, 22 + dy, 29, 9 + dy, 0.6), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#625565'], 1)
    px(P, linha(22, 20 + dy, 29, 9 + dy), '#a884f3', 1.1)
    px(P, [(29, 9 + dy)], BRANCO, 1.2)
    parte(P, retangulo(19, 22 + dy, 22, 23 + dy), S, 1.3, plano=True)          # guarda
    # pernas
    parte(P, capsula(14, 23, 13, 29, 1.8), S, 2)
    parte(P, capsula(18, 23, 19, 29, 1.9), S, 2.5)
    # tronco e capa curta
    parte(P, poligono([(10, 16 + dy), (14, 15 + dy), (9, 26 + dy), (6, 25 + dy)]), ['#2e222f', '#2e222f', '#2e222f', '#45293f', '#45293f'], 2.6, plano=True)
    parte(P, elipse(16, 19.5 + dy, 4.6, 5), S, 3)
    px(P, [(13, 17 + dy), (14, 16 + dy)], '#905ea9', 3.01)
    # braço da frente
    parte(P, capsula(17, 18 + dy, 21, 22 + dy, 1.4), S, 5)
    # cabeça e cabelo espetado
    parte(P, elipse(17, 10.5 + dy, 5, 4.8), S, 4)
    cab = poligono([(11, 10 + dy), (11, 3 + dy), (14, 6 + dy), (15, 1 + dy), (17, 5 + dy), (20, 2 + dy), (20, 6 + dy),
                    (24, 5 + dy), (22, 9 + dy), (16, 9 + dy), (13, 13 + dy)])
    parte(P, cab, ['#2e222f', '#2e222f', '#2e222f', '#6b3e75', '#6b3e75'], 4.5, plano=True)
    px(P, [(11, 4 + dy), (15, 2 + dy), (20, 3 + dy)], '#a884f3', 4.51)
    # olhos roxos a brilhar
    if t == 3:
        px(P, [(18, 11 + dy), (19, 11 + dy), (21, 11 + dy)], '#6b3e75', 6)
    else:
        for ex in (18, 21):
            px(P, [(ex, 10 + dy), (ex, 11 + dy)], '#a884f3', 6)
            px(P, [(ex, 10 + dy)], '#eaaded', 6.1)
        px(P, [(17, 12 + dy), (22, 12 + dy)], '#6b3e75', 6)
    return desenhar(P, 32, 32)


def sentinela_ana(t):
    """Sentinela Anã (48): autómato anão de bronze com rebites e runas que brilham, fornalha no peito com grelha e
    fogo a tremer, elmo com viseira de olhos em brasa, barba de placas de ferro, chaminé que deita fumo e martelo."""
    P = []
    dy = RESP[t]
    br_esc = ['#45293f', '#6e2727', '#9e4539', '#cd683d', '#e6904e']
    # fumo da chaminé
    for i in range(3):
        y = 6 - i * 3 - t
        parte(P, elipse(12 - i + (t % 2), y + 1, 2.2 + i * 0.4, 1.8 + i * 0.3), ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'], 0.1 + i * 0.01)
    parte(P, retangulo(11, 8 + dy, 14, 18 + dy), 'ferro_esc', 0.5, volume='cilindro_v')   # chaminé
    parte(P, retangulo(10, 7 + dy, 15, 8 + dy), 'ferro', 0.6, plano=True)
    # pernas e botas
    parte(P, capsula(19, 38, 19, 42, 3.4), br_esc, 1, volume='cilindro_v')
    parte(P, capsula(29, 38, 30, 42, 3.6), 'bronze', 2, volume='cilindro_v')
    parte(P, retangulo(14, 43, 23, 46, canto=1), 'ferro_esc', 1.1, plano=True)
    parte(P, retangulo(25, 43, 35, 46, canto=1), 'ferro_esc', 2.1, plano=True)
    px(P, [(30, 39), (19, 39)], '#fbb954', 2.2)
    # braço de trás
    parte(P, capsula(16, 23 + dy, 13, 33 + dy, 3), br_esc, 2.5)
    parte(P, elipse(13, 35 + dy, 3, 2.8), br_esc, 2.6)
    # corpo-barril
    corpo = parte(P, elipse(24, 29 + dy, 10.5, 10), 'bronze', 3, volume='cilindro_v')
    for y in (21, 37):
        px(P, [(x, y + dy) for x in range(15, 34) if (x, y + dy) in corpo], '#6e2727', 3.01)
    for (x, y) in ((16, 25), (16, 33), (32, 23), (33, 35)):
        px(P, [(x, y + dy)], '#fbb954', 3.02)                                         # rebites
    # runas a brilhar
    runa = '#30e1b9' if t % 2 == 0 else '#8ff8e2'
    px(P, [(18, 27 + dy), (18, 28 + dy), (19, 27 + dy), (18, 30 + dy), (19, 31 + dy), (18, 32 + dy)], runa, 3.03)
    # fornalha no peito
    forn = retangulo(23, 25 + dy, 31, 33 + dy, canto=1)
    parte(P, forn, 'ferro_esc', 4, plano=True)
    fogo = retangulo(24, 26 + dy, 30, 32 + dy)
    cores = ['#b33831', '#ea4f36', '#f79617', '#f9c22b', '#fbff86']
    for (x, y) in fogo:
        k = (31 + dy - y) + ((x * 3 + t * 2) % 4) * 0.7
        px(P, [(x, y)], cores[max(0, min(4, int(4 - k * 0.6)))], 4.01)
    px(P, [(x, y) for x in (25, 27, 29) for y in range(26 + dy, 33 + dy)], '#3e3546', 4.02)   # grelha
    # cabeça: elmo com viseira e barba de placas
    parte(P, elipse(27, 15 + dy, 6.5, 6), 'bronze', 5)
    px(P, retangulo(25, 14 + dy, 34, 16 + dy), OUT, 5.1)
    brasa = ['#f79617', '#f9c22b', '#fbff86', '#f9c22b'][t]
    px(P, [(28, 15 + dy), (29, 15 + dy), (32, 15 + dy), (33, 15 + dy)], brasa, 5.2)
    px(P, [(28, 15 + dy), (32, 15 + dy)], BRANCO, 5.3)
    parte(P, capsula(27, 9 + dy, 27, 7 + dy, 1.5), 'ferro', 5.4)                     # crista do elmo
    barba = poligono([(23, 18 + dy), (34, 18 + dy), (33, 24 + dy), (29, 28 + dy), (25, 24 + dy)])
    parte(P, barba, 'ferro', 5.5, plano=True)
    for y in (20, 23, 26):
        px(P, [(x, y + dy) for x in range(23, 35) if (x, y + dy) in barba], '#625565', 5.51)
    px(P, [(29, 27 + dy), (29, 28 + dy)], '#f9c22b', 5.52)                               # anel na barba
    # braço da frente com martelo
    parte(P, elipse(33, 22 + dy, 4.2, 4), 'bronze', 6)
    parte(P, capsula(35, 25 + dy, 38, 31 + dy, 2.6), 'bronze', 6.1)
    parte(P, capsula(39, 37, 41, 14 + dy, 0.9), 'madeira', 6.2)
    mart = retangulo(36, 8 + dy, 45, 15 + dy, canto=1)
    parte(P, mart, 'ferro', 6.3, plano=True)
    px(P, [(38, 11 + dy), (39, 12 + dy), (40, 11 + dy), (42, 12 + dy)], runa, 6.31)
    parte(P, elipse(39, 32 + dy, 2.8, 2.6), 'bronze', 6.4)
    return desenhar(P, 48, 48)


def barqueiro_afogado(t):
    """Barqueiro Afogado (48): esqueleto de capuz verde-musgo esfarrapado e a pingar, caveira com olhos verdes a
    brilhar, costelas à mostra, algas penduradas, o remo comprido com a lanterna de fogo-fátuo pendurada."""
    P = []
    dy = RESP[t]
    capa_r = ['#2e222f', '#313638', '#374e4a', '#547e64', '#92a984']
    # remo (atrás da mão) com a pá em baixo e a lanterna em cima
    parte(P, capsula(36, 44, 38, 6 + dy, 0.9), 'madeira', 0.5)
    parte(P, elipse(35.5, 43, 2.2, 3.4), 'madeira', 0.6)
    parte(P, capsula(38, 6 + dy, 42, 8 + dy, 0.6), 'ferro_esc', 0.7)                     # gancho
    lx, ly = 43, 12 + dy + [0, 1, 0, -1][t] * 0.5
    px(P, linha(42, 8 + dy, lx, ly - 3), '#625565', 0.8)
    lan = retangulo(lx - 2, int(ly - 2), lx + 2, int(ly + 3), canto=1)
    parte(P, lan, 'ferro_esc', 0.9, plano=True)
    chama = ['#1ebc73', '#91db69', '#cddf6c', '#91db69'][t]
    px(P, [(lx - 1, int(ly)), (lx, int(ly)), (lx + 1, int(ly)), (lx, int(ly) - 1), (lx - 1, int(ly) + 1), (lx, int(ly) + 1), (lx + 1, int(ly) + 1)], chama, 0.91)
    px(P, [(lx, int(ly))], BRANCO, 0.92)
    # capa (corpo), com a bainha esfarrapada que ondula
    w = [0, 1, 0, -1][t]
    bainha = [(29, 46), (27, 44), (25, 46), (22, 44), (20, 46 + (w > 0)), (17, 44), (14, 46)]
    capa = poligono([(18, 13 + dy), (28, 13 + dy), (31, 26 + dy), (31, 40), (30, 46)] + bainha + [(13 + w, 40), (14, 26 + dy)])
    parte(P, capa, capa_r, 2, volume='cilindro_v')
    textura(P, capa, capa_r, 2, s=81, escuro=0.08, claro=0.05, traco=1)
    # costelas à mostra num rasgão
    ras = elipse(26, 27 + dy, 3, 4)
    px(P, ras, OUT, 2.1)
    for y in (25, 27, 29):
        px(P, [(25, y + dy), (26, y + dy), (27, y + dy)], '#c7dcd0', 2.2)
    # algas penduradas e pingos
    for (x, y, n) in ((16, 30, 5), (19, 36, 4), (29, 33, 4)):
        px(P, [(x + (i % 2), y + i + dy) for i in range(n)], '#239063', 2.3)
        px(P, [(x, y + dy)], '#1ebc73', 2.31)
    gy = 40 + t * 2
    px(P, [(15, gy)], '#4d9be6', 2.4)
    px(P, [(31, 43 - t)], '#8fd3ff', 2.4)
    # capuz e caveira
    capuz = parte(P, elipse(23, 12 + dy, 7.5, 7.5), capa_r, 3)
    caveira = parte(P, elipse(25.5, 13 + dy, 4.3, 4.6), 'osso_esc', 4)
    px(P, elipse(24.5, 11 + dy, 7, 3.2) & capuz - caveira, '#313638', 3.01)
    sombra = {p for p in caveira if p[1] <= 10 + dy}
    px(P, sombra, '#7f708a', 4.01)                                              # sombra do capuz na testa
    for ex in (25, 28):
        px(P, [(ex, 12 + dy), (ex + 1, 12 + dy), (ex, 13 + dy), (ex + 1, 13 + dy)], OUT, 4.1)
        px(P, [(ex + 1, 12 + dy)], '#91db69' if t != 2 else '#cddf6c', 4.2)
    px(P, [(28, 15 + dy)], OUT, 4.1)                                                 # nariz
    px(P, [(25, 17 + dy), (26, 17 + dy), (27, 17 + dy), (28, 17 + dy)], '#7f708a', 4.1)
    px(P, [(26, 17 + dy), (28, 17 + dy)], OUT, 4.11)                                # dentes
    # braço ossudo da frente a segurar o remo
    parte(P, capsula(28, 21 + dy, 33, 25 + dy, 2.3), capa_r, 5)
    parte(P, capsula(33, 25 + dy, 36, 23 + dy, 0.8), 'osso', 5.1)
    parte(P, elipse(37, 22.5 + dy, 1.6, 1.8), 'osso', 5.2)
    # pés ossudos a espreitar
    px(P, [(18, 46), (19, 46), (24, 46), (25, 46)], '#c7dcd0', 2.5)
    return desenhar(P, 48, 48)


def agua_viva_fungica(t):
    """Água-Viva Fúngica (64): chapéu de cogumelo rosa com pintas que brilham e borda recortada, lamelas por baixo,
    dois olhinhos azul-água, tentáculos de fungo que ondulam (uns rosa com franjas, outros finos e luminosos com
    a ponta a brilhar) e esporos a subir."""
    P = []
    dy = BOB[t]
    sq = [0, 0.4, 0.8, 0.4][t]
    cx, cy = 32, 26 + dy
    # tentáculos (atrás do chapéu)
    for i, x0 in enumerate((20, 25, 30, 35, 40, 44)):
        fino = i % 2 == 1
        pts = []
        comp = 22 + (i * 5) % 9
        for k in range(comp):
            y = cy + 6 + k
            x = x0 + math.sin(k * 0.35 + t * math.pi / 2 + i) * (1.6 if fino else 1.2)
            pts.append((x, y))
        m = set()
        for (x, y) in pts:
            m |= capsula(x, y, x, y, 0.8 if fino else 1.6 - y * 0.004)
        if fino:
            parte(P, m, 'agua', 1 + i * 0.01, plano=True)
            px(P, [pts[-1], (pts[-1][0], pts[-1][1] - 1)], '#8ff8e2', 1.1)
            px(P, [pts[-1]], BRANCO, 1.11)
            px(P, pts[4::5], '#30e1b9', 1.05)
        else:
            parte(P, m, 'fungo', 1 + i * 0.01, plano=True)
            px(P, [(x - 2, y) for (x, y) in pts[3::4]], '#f04f78', 1.05)        # franjas
            px(P, [(x, y) for (x, y) in pts[2::4]], '#831c5d', 1.06)
    # lamelas
    lam = retangulo(18, int(cy + 2), 46, int(cy + 8), canto=1)
    parte(P, lam, ['#45293f', '#753c54', '#a24b6f', '#cf657f', '#ed8099'], 2, plano=True)
    px(P, [(x, y) for x in range(19, 46, 2) for y in range(int(cy + 3), int(cy + 7)) if (x, y) in lam], '#753c54', 2.01)
    # olhinhos nas lamelas
    for ex in (34, 40):
        if t == 3:
            px(P, [(ex, int(cy + 6)), (ex + 1, int(cy + 6))], OUT, 3.5)
        else:
            olho(P, ex, int(cy + 5), '#30e1b9', 3.5, tam=1, pupila='#0b5e65')
    # chapéu
    chapeu = {p for p in elipse(cx, cy + 3, 16, 14 - sq) if p[1] <= cy + 3}
    borda = [(x, int(cy + 3) + (1 if (x // 3) % 2 else 0)) for x in range(17, 48)]
    chapeu |= {p for p in borda}
    parte(P, chapeu, 'fungo', 3)
    # pintas que brilham
    for (x, y, r) in ((24, -6, 2.2), (33, -9, 2.6), (41, -4, 2), (28, 0, 1.6), (37, 0, 1.4), (20, 0, 1.2)):
        m = elipse(x, cy + y, r, r * 0.85) & chapeu
        px(P, m, '#30e1b9', 3.1)
        px(P, [min(m)] if m else [], '#8ff8e2', 3.2)
    px(P, [(22, cy - 8), (23, cy - 9), (25, cy - 10)], '#fdcbb0', 3.05)                  # brilho do chapéu
    # esporos a subir
    rnd = random.Random(5)
    for i in range(7):
        x = rnd.randint(12, 52)
        y = (rnd.randint(4, 60) - t * 3) % 60 + 2
        px(P, [(x, y)], '#8ff8e2' if i % 2 else '#30e1b9', 9)
    return desenhar(P, 64, 64)


def morcego_rei_dos_ecos(t):
    """Morcego-Rei dos Ecos (64): morcego gigante roxo com orelhas enormes (rosa por dentro, com pregas), coroa de
    latão pequena, juba de pelo claro ao pescoço, nariz em folha, presas, olhos vermelhos, asas grandes com dedos
    e veias, e ondas de som a sair das orelhas."""
    P = []
    dy = [0, -1, 0, 1][t]
    # asa de trás
    tras = [[(28, 26), (22, 12), (14, 6), (17, 14), (20, 18), (24, 22)],
            [(28, 26), (20, 18), (10, 17), (15, 22), (20, 24), (24, 26)],
            [(28, 28), (20, 30), (12, 34), (17, 34), (21, 33), (25, 32)],
            [(28, 26), (20, 18), (10, 17), (15, 22), (20, 24), (24, 26)]][t]
    parte(P, poligono([(x, y + dy) for x, y in tras]), ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9'], 1, plano=True)
    # asa da frente
    S = (31, 27)
    if t == 0:
        E, T, borda = (20, 12), (4, 6), [(8, 17), (14, 17), (18, 23), (24, 24), (27, 30)]
    elif t == 2:
        E, T, borda = (18, 36), (6, 48), [(10, 54), (15, 50), (20, 53), (25, 46), (29, 40)]
    else:
        E, T, borda = (18, 24), (2, 25), [(5, 32), (11, 30), (16, 34), (22, 32), (27, 34)]
    asa = poligono([(x, y + dy) for x, y in [S, E, T] + borda])
    parte(P, asa, ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'], 8, plano=True)
    for b in borda[:4]:
        px(P, [p for p in linha(E[0], E[1] + dy, b[0], b[1] + dy) if (int(round(p[0])), int(round(p[1]))) in asa], '#905ea9', 8.1)
    px(P, linha(S[0], S[1] + dy, E[0], E[1] + dy) + linha(E[0], E[1] + dy, T[0], T[1] + dy), '#a884f3', 8.2)
    px(P, [(E[0], E[1] + dy), (E[0] - 1, E[1] + dy - 1)], '#eaaded', 8.3)          # garra da asa
    # corpo peludo
    corpo = parte(P, elipse(31, 32 + dy, 9, 9.5), 'roxo', 5)
    textura(P, corpo, 'roxo_esc', 5, s=91, escuro=0.16, claro=0.06, traco=1)
    # patas com garras
    for x in (28, 33):
        parte(P, capsula(x, 40 + dy, x, 44 + dy, 1.2), 'roxo_esc', 4.5)
        px(P, [(x - 1, 46 + dy), (x + 1, 46 + dy), (x, 46 + dy)], '#c7dcd0', 4.6)
    # orelhas enormes
    for (pts, z) in (([(34, 20), (30, 3), (38, 16)], 4.2), ([(39, 19), (44, 1), (48, 18)], 6.5)):
        m = poligono([(x, y + dy) for x, y in pts])
        parte(P, m, 'roxo', z, plano=True)
        dentro = interior(m, 2)
        px(P, dentro, '#c32454', z + 0.01)
        px(P, [p for p in dentro if p[1] % 3 == 0], '#831c5d', z + 0.02)              # pregas
    # juba clara ao pescoço
    juba = poligono([(33, 24 + dy), (36, 26 + dy), (35, 29 + dy), (38, 30 + dy), (36, 33 + dy), (40, 33 + dy), (41, 36 + dy),
                     (43, 32 + dy), (45, 29 + dy), (41, 26 + dy)])
    parte(P, juba, ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'], 6.6, plano=True)
    px(P, [(37, 30 + dy), (39, 33 + dy), (41, 31 + dy)], '#6b3e75', 6.61)
    # cabeça
    cab = parte(P, elipse(42, 23 + dy, 6.5, 5.5), 'roxo', 7)
    parte(P, elipse(48, 25 + dy, 3, 2.5), 'lilas', 7.1)                                 # focinho
    parte(P, poligono([(48, 20 + dy), (51, 22 + dy), (49, 24 + dy)]), 'rosa', 7.2, plano=True)   # nariz em folha
    if t == 3:
        px(P, [(43, 22 + dy), (44, 22 + dy), (45, 22 + dy)], OUT, 7.3)
    else:
        olho(P, 43, 21 + dy, '#e83b3b', 7.3, pupila='#6e2727')
        px(P, [(45, 22 + dy)], '#e83b3b', 7.3)
    px(P, [(42, 19 + dy), (43, 19 + dy), (44, 20 + dy), (45, 20 + dy)], '#45293f', 7.35)
    px(P, [(45, 27 + dy), (46, 27 + dy), (47, 27 + dy), (48, 27 + dy)], OUT, 7.4)
    px(P, [(46, 28 + dy), (48, 28 + dy), (46, 29 + dy)], BRANCO, 7.5)                     # presas
    # coroa pequena entre as orelhas
    coroa = retangulo(37, 16 + dy, 43, 17 + dy) | poligono([(37, 16 + dy), (37.5, 13 + dy), (39, 16 + dy)]) \
        | poligono([(39.5, 16 + dy), (40.5, 12 + dy), (41.5, 16 + dy)]) | poligono([(42, 16 + dy), (43.5, 13 + dy), (44, 16 + dy)])
    parte(P, coroa, 'ouro', 7.6)
    px(P, [(40, 16 + dy)], '#e83b3b', 7.61)
    # ondas de som (arcos que crescem)
    for k in range(2):
        r = 4 + ((t + k * 2) % 4) * 3
        arco = [(52 + r * math.cos(a), 12 + dy + r * math.sin(a)) for a in [i * 0.15 - 0.75 for i in range(11)]]
        px(P, arco, '#a884f3' if k == 0 else '#eaaded', 9)
    return desenhar(P, 64, 64)


# =====================================================================================
#  BOSSES
# =====================================================================================

def aranha_mae(t):
    """Aranha-Mãe (64), na linha da referência: abdómen enorme roxo-escuro com pelos e setas vermelhas que
    pulsam, marca de ampulheta, saco de ovos de seda (com os ovos a ver-se) preso por fios, cabeça com cacho de
    olhos vermelhos, presas brancas a pingar veneno verde e 8 patas compridas com juntas vermelhas e pelos."""
    P = []
    dy = RESP[t]
    sh = [0, 1, 0, -1][t]
    roxo = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3']
    perna = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#905ea9']
    perna_esc = ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#6b3e75']
    # patas: (anca, joelho, pé)
    patas = [((46, 32), (55, 16), (63, 62)), ((44, 33), (48, 13), (55, 62)),
             ((41, 33), (35, 24), (27, 62)), ((39, 33), (24, 28), (9, 62))]
    for i, (h, j, p) in enumerate(patas):         # as do lado de lá
        o = sh if i % 2 else -sh
        h2, j2, p2 = (h[0] - 2, h[1] + dy), (j[0] - 5, j[1] + 3 + dy + o), (p[0] - 6, p[1] - 2)
        parte(P, capsula(*h2, *j2, 0.9), perna_esc, 1, plano=True)
        parte(P, capsula(*j2, *p2, 0.8), perna_esc, 1.1, plano=True)
        px(P, [j2], '#b33831', 1.2)
    for i, (h, j, p) in enumerate(patas):         # as do lado de cá (atrás do corpo, para não o taparem)
        o = -sh if i % 2 else sh
        h2, j2, p2 = (h[0], h[1] + dy), (j[0], j[1] + dy + o), p
        parte(P, capsula(*h2, *j2, 1.1), perna, 2, plano=True)
        parte(P, capsula(*j2, *p2, 0.9), perna, 2.1, plano=True)
        px(P, [j2, (j2[0], j2[1] + 1)], '#e83b3b', 2.2)
        mid = (j2[0] + (p2[0] - j2[0]) * 0.55, j2[1] + (p2[1] - j2[1]) * 0.55)
        px(P, [mid], '#c32454', 2.2)
        for k in (0.25, 0.75):                     # pelinhos
            q = (j2[0] + (p2[0] - j2[0]) * k, j2[1] + (p2[1] - j2[1]) * k)
            px(P, [(q[0] + 1, q[1])], '#6b3e75', 2.15)
    # saco de ovos e fios de seda
    px(P, linha(9, 22 + dy, 14, 18 + dy) + linha(9, 30 + dy, 15, 27 + dy), '#c7dcd0', 2.9)
    saco = parte(P, elipse(6.5, 27 + dy, 6, 6.5 + sh * 0.2), ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], 3)
    for (x, y) in ((4, 25), (7, 28), (3, 30), (8, 24), (6, 32)):
        px(P, [(x, y + dy), (x + 1, y + dy)], '#9babb2', 3.01)
        px(P, [(x, y + dy - 1)], '#ffffff', 3.02)
    # abdómen
    ab = parte(P, elipse(24, 17 + dy, 15, 12.5), roxo, 4)
    textura(P, ab, roxo, 4, s=101, escuro=0.08, claro=0.05, traco=1)
    for (x, y) in ((11, 9), (14, 6), (30, 5), (37, 9), (12, 25), (36, 25)):      # pelos na borda
        px(P, [(x, y + dy)], '#905ea9', 4.01)
    # setas vermelhas que pulsam
    seta = ['#b33831', '#e83b3b', '#f68181', '#e83b3b'][t]
    for x0 in (16, 22, 28):
        px(P, [(x0, 13 + dy), (x0 + 1, 14 + dy), (x0 + 2, 15 + dy), (x0 + 1, 16 + dy), (x0, 17 + dy),
               (x0 + 1, 13 + dy), (x0 + 2, 14 + dy), (x0 + 3, 15 + dy), (x0 + 2, 16 + dy), (x0 + 1, 17 + dy)], seta, 4.1)
    px(P, [(x, 26 + dy) for x in (31, 32, 33)] + [(32, 27 + dy)] + [(x, 28 + dy) for x in (31, 32, 33)], '#e83b3b', 4.1)   # ampulheta
    # cefalotórax e cabeça
    ce = parte(P, elipse(42, 31 + dy, 6.5, 4.8), roxo, 5)
    px(P, [(39, 29 + dy), (40, 28 + dy)], '#a884f3', 5.01)
    cab = parte(P, elipse(52, 31 + dy, 6.8, 6), roxo, 6)
    textura(P, cab, roxo, 6, s=102, escuro=0.08, claro=0.04)
    # cacho de olhos vermelhos
    for (x, y, g) in ((53, 27, 1), (57, 28, 1), (50, 28, 0), (55, 31, 0), (58, 31, 0)):
        if g:
            px(P, [(x, y + dy), (x + 1, y + dy), (x, y + 1 + dy), (x + 1, y + 1 + dy)], '#e83b3b', 6.1)
            px(P, [(x + 1, y + 1 + dy)], '#6e2727', 6.11)
            px(P, [(x, y + dy)], '#fca790' if t != 2 else BRANCO, 6.12)
        else:
            px(P, [(x, y + dy)], '#f57d4a', 6.1)
    # presas com veneno
    for (x, z) in ((54, 6.5), (58, 7)):
        parte(P, capsula(x, 35 + dy, x + 1, 39 + dy, 1.1), 'osso', z)
        px(P, [(x + 1, 40 + dy)], '#c7dcd0', z + 0.01)
    gy = 41 + dy + t
    px(P, [(59, gy), (59, gy + 1)], '#91db69', 7.1)
    px(P, [(59, gy + 1)], '#1ebc73', 7.11)
    # palpos
    parte(P, capsula(57, 34 + dy, 61, 37 + dy, 0.9), perna, 6.8)
    return desenhar(P, 64, 64)


def golem_de_cristal(t):
    """Golem de Cristal (128): golem gigante de rocha cinzenta feito de blocos com rachas, musgo e veios de cristal;
    cristais azuis, roxos e verdes a sair dos ombros, das costas, do peito e do antebraço; um núcleo de luz no
    peito que pulsa e deita raios; cabeça pequena com sobrolho de pedra e olhos azuis; punhos enormes."""
    P = []
    dy = RESP[t]
    pedra = 'pedra_cl'
    esc = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
    # pernas
    parte(P, capsula(50, 98, 48, 116, 9), esc, 1, volume='cilindro_v')
    parte(P, elipse(46, 120, 13, 6.5), esc, 1.1)
    parte(P, capsula(74, 98, 76, 116, 10), pedra, 2, volume='cilindro_v')
    parte(P, elipse(78, 120, 14, 6.5), pedra, 2.1)
    px(P, [(84, 119), (88, 120), (91, 118)], '#3e3546', 2.2)
    # braço de trás
    parte(P, capsula(42, 50 + dy, 30, 76 + dy, 8), esc, 2.5)
    parte(P, capsula(30, 76 + dy, 30, 92 + dy, 7), esc, 2.6)
    parte(P, elipse(30, 98 + dy, 10, 9), esc, 2.7)
    cristal(P, 26, 70 + dy, math.radians(-150), 10, 3, 'cristal_r', 2.65, brilho=False)
    # bacia e barriga
    parte(P, elipse(62, 94 + dy, 20, 10), esc, 3)
    barriga = parte(P, elipse(62, 82 + dy, 19, 12), pedra, 3.5)
    # costas/bossa e peito
    bossa = parte(P, elipse(46, 52 + dy, 18, 16), pedra, 4)
    peito = parte(P, elipse(64, 62 + dy, 23, 19), pedra, 5)
    for i, m in enumerate((barriga, bossa, peito)):
        textura(P, m, pedra, 3.5 + i * 0.5 + (0.5 if i == 2 else 0), s=110 + i, escuro=0.06, claro=0.04)
    racha(P, [(48, 70 + dy), (54, 76 + dy), (52, 82 + dy), (56, 88 + dy)], 5.2)
    racha(P, [(78, 74 + dy), (74, 80 + dy)], 5.2)
    racha(P, [(36, 44 + dy), (42, 50 + dy), (40, 56 + dy)], 4.2)
    # veios de cristal na pedra
    px(P, linha(70, 84 + dy, 78, 88 + dy), '#4d9be6', 5.3)
    px(P, linha(44, 60 + dy, 38, 66 + dy), '#a884f3', 4.3)
    # musgo em cima da bossa
    musgo = {p for p in elipse(44, 40 + dy, 14, 5) if p in bossa and p[1] <= 41 + dy}
    parte(P, musgo, 'verde_esc', 4.4, separar=False)
    px(P, [(36, 38 + dy), (40, 37 + dy), (46, 37 + dy), (50, 38 + dy)], '#b2ba90', 4.41)
    # cristais das costas (azul, roxo, verde)
    for (x, y, a, c, r, w, z) in ((34, 44, -130, 'cristal_a', 18, 4.5, 3.8), (42, 40, -105, 'cristal_r', 24, 5, 3.81),
                                  (52, 40, -80, 'cristal_v', 16, 4, 3.82), (30, 54, -160, 'cristal_a', 12, 3.5, 3.83),
                                  (47, 41, -95, 'cristal_a', 12, 3, 3.84)):
        cristal(P, x, y + dy, math.radians(a), r, w, c, z, brilho=(t + int(x)) % 3 == 0)
    # núcleo no peito
    nx, ny = 70, 62 + dy
    px(P, elipse(nx, ny, 10, 10), '#3e3546', 5.5)
    px(P, elipse(nx, ny, 9, 9) - elipse(nx, ny, 7.5, 7.5), '#625565', 5.51)
    rr = [6, 6.6, 7.2, 6.6][t]
    px(P, elipse(nx, ny, rr, rr), '#4d9be6', 5.6)
    px(P, elipse(nx - 0.5, ny - 0.5, rr - 1.6, rr - 1.6), '#8fd3ff', 5.61)
    px(P, elipse(nx - 1, ny - 1, rr - 3.4, rr - 3.4), '#ffffff', 5.62)
    for k in range(8):                                   # raios
        a = k * math.pi / 4 + t * math.pi / 8
        r1, r2 = 11, 13 + (k + t) % 2 * 2
        px(P, [(nx + math.cos(a) * r, ny + math.sin(a) * r) for r in range(r1, r2)], '#8fd3ff', 5.7)
    # cristais do peito
    cristal(P, 56, 56 + dy, math.radians(-125), 10, 3, 'cristal_t', 5.8, brilho=t == 1)
    cristal(P, 82, 76 + dy, math.radians(-30), 8, 2.5, 'cristal_r', 5.81, brilho=t == 3)
    # cabeça pequena entre os ombros
    cab = parte(P, elipse(84, 41 + dy, 11, 9.5), pedra, 7.5)
    textura(P, cab, pedra, 7.5, s=120, escuro=0.06, claro=0.04)
    parte(P, capsula(76, 36 + dy, 95, 37 + dy, 2.8), pedra, 7.6, volume='cilindro_h')       # sobrolho
    olho_c = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    for ex in (86, 92):
        px(P, retangulo(ex - 2, 40 + dy, ex + 2, 42 + dy), OUT, 7.7)
        px(P, retangulo(ex - 1, 40 + dy, ex + 1, 41 + dy), olho_c, 7.71)
        px(P, [(ex - 1, 40 + dy)], BRANCO, 7.72)
    px(P, [(x, 47 + dy + (x // 2) % 2) for x in range(84, 94)], OUT, 7.7)                 # boca
    cristal(P, 79, 34 + dy, math.radians(-105), 9, 2.6, 'cristal_a', 7.55, brilho=t == 0)
    # ombro da frente com cristais e braço da frente
    cristal(P, 94, 52 + dy, math.radians(-35), 18, 4.5, 'cristal_r', 6.9, brilho=t == 2)
    cristal(P, 97, 58 + dy, math.radians(-5), 12, 3.5, 'cristal_a', 6.91, brilho=t == 0)
    cristal(P, 76, 50 + dy, math.radians(-150), 11, 3, 'cristal_v', 6.92, brilho=t == 1)
    omb = parte(P, elipse(86, 58 + dy, 12, 11), pedra, 7)
    textura(P, omb, pedra, 7, s=121, escuro=0.06, claro=0.05)
    parte(P, capsula(90, 66 + dy, 96, 88 + dy, 8.5), pedra, 7.1)
    cristal(P, 100, 78 + dy, math.radians(-20), 10, 3, 'cristal_v', 7.15, brilho=t == 3)
    punho = parte(P, elipse(98, 98 + dy, 12, 11), pedra, 7.2)
    textura(P, punho, pedra, 7.2, s=122, escuro=0.06, claro=0.05)
    for y in (94, 99, 104):                                # nós dos dedos
        px(P, linha(104, y + dy, 109, y + 1 + dy), '#3e3546', 7.3)
    racha(P, [(86, 54 + dy), (90, 60 + dy)], 7.3)
    # pó a cair
    if t in (1, 2):
        px(P, [(108 + t, 70 + t * 6), (111, 80 + t * 4)], '#9babb2', 9)
    return desenhar(P, 128, 128)


def rei_anao_esquecido(t):
    """Rei Anão Esquecido (64): fantasma de um rei anão em armadura, translúcido azul-água, coroa de ouro, barba
    branca enorme entrançada com anéis de ouro, olhos ocos a brilhar, capa esfarrapada, machado de duas mãos com
    runas, e as pernas a desfazerem-se em névoa."""
    P = []
    dy = BOB[t]
    F = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
    F_esc = ['#2e222f', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9']
    # capa esfarrapada (atrás)
    w = [0, 1, 0, -1][t]
    capa = poligono([(24, 22 + dy), (32, 20 + dy), (28, 40 + dy), (26, 52), (22, 54 + w), (19, 51), (17, 55 - w), (16, 48), (18, 34)])
    parte(P, capa, F_esc, 0.5, plano=True)
    # machado de duas mãos (atrás da mão da frente)
    parte(P, capsula(50, 58, 53, 8 + dy, 1.1), 'madeira', 1)
    lam_d = poligono([(53, 9 + dy), (61, 3 + dy), (63, 12 + dy), (61, 21 + dy), (53, 16 + dy)])
    lam_e = poligono([(52, 9 + dy), (46, 5 + dy), (44, 12 + dy), (46, 19 + dy), (52, 16 + dy)])
    parte(P, lam_e, F_esc, 1.1, plano=True)
    parte(P, lam_d, F, 1.2, plano=True)
    runa = '#8ff8e2' if t % 2 == 0 else BRANCO
    px(P, [(57, 9 + dy), (58, 10 + dy), (57, 11 + dy), (58, 12 + dy), (57, 13 + dy)], runa, 1.3)
    px(P, [(62, 5 + dy), (63, 8 + dy), (63, 15 + dy)], BRANCO, 1.31)
    # pernas que se desfazem em névoa
    for (x, z, r) in ((26, 2, F_esc), (36, 2.5, F)):
        parte(P, capsula(x, 44 + dy, x, 54, 4.5), r, z, volume='cilindro_v')
    nevoa = set()
    for i, x in enumerate(range(20, 44, 4)):
        nevoa |= elipse(x + (t + i) % 2, 57 + (i % 2) * 2, 2.4 - (i % 2) * 0.6, 2)
    parte(P, nevoa, F, 2.6, plano=True)
    px(P, [(20 + (t * 3) % 8, 62), (34 - t, 63), (41, 61 - t % 2)], '#0eaf9b', 2.7)
    # braço de trás
    parte(P, capsula(24, 28 + dy, 22, 40 + dy, 3.3), F_esc, 2.8)
    # tronco de armadura
    tronco = parte(P, poligono([(23, 26 + dy), (40, 25 + dy), (42, 45 + dy), (22, 45 + dy)]), F, 3, volume='cilindro_v')
    px(P, [(x, 34 + dy) for x in range(24, 41)], '#0b8a8f', 3.02)                    # placas da armadura
    px(P, [(x, 39 + dy) for x in range(23, 42)], '#0b8a8f', 3.02)
    px(P, [(x, 44 + dy) for x in range(21, 42)], '#0b5e65', 3.01)                  # cinto
    parte(P, retangulo(30, 43 + dy, 34, 46 + dy), 'ouro', 3.1, plano=True)
    px(P, [(32, 44 + dy)], '#9e4539', 3.11)
    for (x, y) in ((24, 33), (24, 39), (38, 32)):
        px(P, [(x, y + dy)], '#8ff8e2', 3.05)                                       # rebites
    # ombreira
    parte(P, elipse(36, 27 + dy, 6.5, 4.5), F, 4)
    px(P, [(33, 25 + dy), (34, 24 + dy), (36, 24 + dy)], '#ffffff', 4.01)
    # cabeça
    cab = parte(P, elipse(36, 17 + dy, 7, 6.5), ['#0b5e65', '#0b8a8f', '#30e1b9', '#8ff8e2', '#ffffff'], 5)
    parte(P, capsula(42, 17 + dy, 45, 20 + dy, 2), F, 6.5)                                    # nariz grande
    for ex in (36, 40):
        px(P, [(ex, 15 + dy), (ex + 1, 15 + dy), (ex, 16 + dy), (ex + 1, 16 + dy), (ex, 17 + dy), (ex + 1, 17 + dy)], OUT, 5.3)
        px(P, [(ex + 1, 16 + dy), (ex, 16 + dy)], '#8ff8e2', 5.31)
        px(P, [(ex + 1, 16 + dy)], '#ffffff' if t != 2 else '#30e1b9', 5.32)
    px(P, [(35, 14 + dy), (36, 13 + dy), (37, 13 + dy), (39, 13 + dy), (40, 13 + dy), (41, 14 + dy)], '#ffffff', 7.5)  # sobrancelhas
    # barba enorme entrançada
    bw = [0, 0, 1, 1][t]
    barba = poligono([(31, 20 + dy), (45, 20 + dy), (44, 30 + dy), (41, 40 + dy + bw), (38, 46 + dy + bw), (35, 40 + dy), (32, 31 + dy)])
    parte(P, barba, 'branco', 6)
    for y in range(23, 44, 3):
        px(P, [(x, y + dy + (x % 2)) for x in range(33, 44) if (x, y + dy + (x % 2)) in barba], '#9babb2', 6.01)
    for (x, y) in ((40, 32), (38, 41)):
        px(P, [(x, y + dy + bw), (x + 1, y + dy + bw)], '#f9c22b', 6.02)                       # anéis de ouro
    px(P, [(38, 23 + dy), (39, 23 + dy), (40, 23 + dy), (41, 22 + dy)], '#0b5e65', 6.03)        # boca no bigode
    # coroa
    coroa = retangulo(29, 9 + dy, 42, 11 + dy) | poligono([(29, 9 + dy), (30, 4 + dy), (32, 9 + dy)]) \
        | poligono([(33, 9 + dy), (35.5, 2 + dy), (38, 9 + dy)]) | poligono([(39, 9 + dy), (41, 4 + dy), (42, 9 + dy)])
    parte(P, coroa, 'ouro', 7)
    px(P, [(35, 10 + dy), (36, 10 + dy)], '#4d9be6', 7.1)
    px(P, [(30, 4 + dy), (35, 2 + dy), (41, 4 + dy)], '#ffffff', 7.11)
    # braço da frente agarrado ao machado
    parte(P, capsula(38, 30 + dy, 46, 34 + dy, 3.2), F, 8)
    parte(P, elipse(50, 33 + dy, 3.2, 3), F, 8.1)
    px(P, [(41, 31 + dy), (42, 31 + dy)], '#8ff8e2', 8.2)
    # pontinhos de alma a subir
    for i, (x, y) in enumerate(((12, 30), (56, 40), (18, 14))):
        px(P, [(x + (t + i) % 2, y - (t * 2 + i * 3) % 8)], '#8ff8e2', 9)
    return desenhar(P, 64, 64)


# =====================================================================================
#  Gravar a proposta e as comparações
# =====================================================================================

CRIATURAS = [   # (id, pasta antiga, função)
    ('morcego', 'monstros', morcego),
    ('goblin_mineiro', 'monstros', goblin_mineiro),
    ('golem_de_pedra', 'monstros', golem_de_pedra),
    ('toupeira_gigante', 'monstros', toupeira),
    ('aranha_da_caverna', 'monstros', aranha_da_caverna),
    ('kobold', 'monstros', kobold),
    ('lagarta_de_cristal', 'monstros', lagarta_de_cristal),
    ('fantasma_mineiro', 'monstros', fantasma_mineiro),
    ('rei_goblin_gruk', 'monstros', rei_goblin_gruk),
    ('toupeira_dourada', 'monstros', lambda t: toupeira(t, dourada=True)),
    ('vagoneta_assombrada', 'guardioes', vagoneta_assombrada),
    ('touro_das_galerias', 'guardioes', touro_das_galerias),
    ('prisma_vivo', 'guardioes', prisma_vivo),
    ('barqueiro_afogado', 'guardioes', barqueiro_afogado),
    ('agua_viva_fungica', 'guardioes', agua_viva_fungica),
    ('morcego_rei_dos_ecos', 'guardioes', morcego_rei_dos_ecos),
    ('sentinela_ana', 'guardioes', sentinela_ana),
    ('reflexo_negro', 'guardioes', reflexo_negro),
    ('aranha_mae', 'bosses', aranha_mae),
    ('golem_de_cristal', 'bosses', golem_de_cristal),
    ('rei_anao_esquecido', 'bosses', rei_anao_esquecido),
]

PALETA = set("""2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334
e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73
91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff
45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0""".split())
FUNDO = (0x26, 0x2b, 0x3a)
FONTE = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def nomes_pt():
    n = {}
    for f in ('monstros.json', 'bosses.json', 'masmorras.json'):
        try:
            d = json.load(open(os.path.join(RAIZ, 'dados', f), encoding='utf-8'))
        except OSError:
            continue
        listas = [d] if isinstance(d, list) else [v if isinstance(v, list) else list(v.values()) for v in d.values() if isinstance(v, (list, dict))]
        for lst in listas:
            for e in lst:
                if isinstance(e, dict) and 'id' in e and e.get('nome_pt'):
                    n.setdefault(e['id'], e['nome_pt'])
    return n


def quadros(tira_img):
    h = tira_img.height
    return [tira_img.crop((i * h, 0, i * h + h, h)) for i in range(tira_img.width // h)]


def fora_da_paleta(img):
    cores = {'%02x%02x%02x' % c[:3] for c in img.getdata() if c[3]}
    return sorted(cores - PALETA)


def escala(lado):
    return 3 if lado <= 32 else (2 if lado <= 64 else 1)


def grelha(itens, titulo, caminho, com_antes=True, n=8, ms=160, largura_max=1200):
    """itens: (nome, quadros_antes, quadros_depois). Faz um GIF animado em grelha."""
    fonte = ImageFont.truetype(FONTE, 12)
    fonte_t = ImageFont.truetype(FONTE, 16)
    gap = 12
    celulas = []
    for nome, antes, depois in itens:
        lado = depois[0].width
        k = escala(lado)
        w = lado * k * (2 if com_antes else 1) + (6 if com_antes else 0)
        celulas.append((nome, antes, depois, k, w, lado * k + 18))
    # arrumar em linhas (largura máxima)
    linhas, atual, larg = [], [], gap
    for c in celulas:
        if atual and larg + c[4] + gap > largura_max:
            linhas.append(atual)
            atual, larg = [], gap
        atual.append(c)
        larg += c[4] + gap
    linhas.append(atual)
    W = max(gap + sum(c[4] + gap for c in l) for l in linhas)
    H = 34 + sum(max(c[5] for c in l) + gap for l in linhas)
    frames = []
    for f in range(n):
        im = Image.new('RGB', (W, H), FUNDO)
        d = ImageDraw.Draw(im)
        d.text((gap, 8), titulo, fill=(230, 230, 230), font=fonte_t)
        y = 34
        for l in linhas:
            x = gap
            hl = max(c[5] for c in l)
            for nome, antes, depois, k, w, h in l:
                lado = depois[0].width
                topo = y + (hl - h)
                pares = [antes, depois] if com_antes else [depois]
                for j, q in enumerate(pares):
                    fr = q[f % len(q)].resize((lado * k, lado * k), Image.NEAREST)
                    im.paste(fr, (x + j * (lado * k + 6), topo), fr)
                tw = d.textlength(nome, font=fonte)
                d.text((x + (w - tw) / 2, topo + lado * k + 3), nome, fill=(220, 220, 220), font=fonte)
                x += w + gap
            y += hl + gap
        frames.append(im)
    frames[0].save(caminho, save_all=True, append_images=frames[1:], duration=ms, loop=0, disposal=2)


def main():
    os.makedirs(SAIDA, exist_ok=True)
    nomes = nomes_pt()
    itens = []
    for cid, pasta, f in CRIATURAS:
        antigo = Image.open(os.path.join(ANTIGO, pasta, f'{cid}_parado_lado.png')).convert('RGBA')
        lado = antigo.height
        novos = [f(t) for t in range(4)]
        assert all(q.size == (lado, lado) for q in novos), (cid, novos[0].size, lado)
        tira = Image.new('RGBA', (lado * 4, lado), (0, 0, 0, 0))
        for i, q in enumerate(novos):
            tira.paste(q, (i * lado, 0))
        tira.save(os.path.join(SAIDA, f'{cid}_parado_lado.png'))
        mal = fora_da_paleta(tira)
        print(f'{cid:22s} {lado:3d}px  {"OK" if not mal else "FORA DA PALETA: " + " ".join(mal)}')
        itens.append((nomes.get(cid, cid), quadros(antigo), novos))
    grelha(itens, 'Região 2 — Cavernas e Minas — antes | depois', os.path.join(SAIDA, 'comparar.gif'))
    grelha(itens, 'Região 2 — Cavernas e Minas — proposta nova', os.path.join(SAIDA, 'depois.gif'), com_antes=False)
    print('gravado em', SAIDA)


if __name__ == '__main__':
    main()
