"""PROPOSTA (por aprovar): os monstros, guardiões e bosses da região 6 — Oceano, redesenhados.

Só desenha a animação "parado" (4 quadros) de cada criatura, com o mesmo tamanho de quadro do desenho antigo, e
grava em arte/propostas/monstros/r06_oceano/. NÃO mexe na arte do jogo (arte/regioes/...).
Fichas: docs/regioes/r06_oceano.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (secções 11 e 12).

Correr a partir da raiz do repositório:
    python3 ferramentas/arte/propostas/r06_oceano.py            (todas)
    python3 ferramentas/arte/propostas/r06_oceano.py polvo ...  (só algumas, sem refazer os GIF)
"""
import math
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
sys.path.insert(0, 'ferramentas/arte')
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

OUT = '#2e222f'
BRANCO = '#ffffff'
PASTA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r06_oceano')
ANTIGOS = os.path.join(RAIZ, 'arte', 'regioes', 'r06_oceano')

# ---------------------------------------------------------------- rampas (escuro -> claro), só Resurrect 64
R = dict(RAMPAS)
R.update({
    'carapaca':  ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790'],
    'carapaca_t': ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'],
    'barriga':   ['#9e4539', '#e6904e', '#fca790', '#fdcbb0', '#fdcbb0'],
    'ouro_corpo': ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86'],
    'ouro_t':    ['#7a3045', '#9e4539', '#cd683d', '#f79617', '#f9c22b'],
    'ouro':      ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
    'areia':     ['#966c6c', '#e6904e', '#fca790', '#fdcbb0', '#ffffff'],
    'rocha':     ['#313638', '#3e3546', '#625565', '#7f708a', '#9babb2'],
    'abissal':   ['#323353', '#3e3546', '#484a77', '#625565', '#7f708a'],
    'abissal_t': ['#2e222f', '#323353', '#3e3546', '#484a77', '#625565'],
    'cauda_ser': ['#165a4c', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9'],
    'cabelo_ser': ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'],
    'pele_ser':  ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0'],
    'agua':      ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'],
    'barbatana': ['#0b5e65', '#0eaf9b', '#30e1b9', '#8ff8e2', '#ffffff'],
    'tubarao':   ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'tubarao_t': ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6'],
    'osso':      ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'osso_t':    ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0'],
    'chapeu':    ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a'],
    'casaco_v':  ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790'],
    'casaco_vt': ['#45293f', '#6e2727', '#ae2334', '#e83b3b', '#f57d4a'],
    'casaco_a':  ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'casaco_at': ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6'],
    'fantasma':  ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'],
    'fantasma_t': ['#165a4c', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9'],
    'lodo':      ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90'],
    'alga':      ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'alga_t':    ['#313638', '#165a4c', '#239063', '#1ebc73', '#91db69'],
    'couro':     ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'madeira':   ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'ferro':     ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff'],
    'ferro_t':   ['#2e222f', '#3e3546', '#625565', '#9babb2', '#c7dcd0'],
    'polvo':     ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'],
    'polvo_t':   ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'],
    'ventosa':   ['#753c54', '#cf657f', '#ed8099', '#fdcbb0', '#fdcbb0'],
    'gaivota':   ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'asa':       ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'asa_t':     ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'],
    'bico':      ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'],
    'pata':      ['#9e4539', '#cd683d', '#f79617', '#fbb954', '#fbb954'],
    'lenco':     ['#6e2727', '#ae2334', '#e83b3b', '#f68181', '#fca790'],
    'leao':      ['#6e2727', '#9e4539', '#cd683d', '#f57d4a', '#fbb954'],
    'leao_t':    ['#45293f', '#6e2727', '#9e4539', '#cd683d', '#f57d4a'],
    'espinho':   ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'],
    'membrana':  ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790'],
    'folhado':   ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86'],
    'folha':     ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#fbff86'],
    'folha_v':   ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'coral':     ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
    'coral_t':   ['#45293f', '#831c5d', '#c32454', '#f04f78', '#f68181'],
    'coral_b':   ['#9babb2', '#c7dcd0', '#fdcbb0', '#ffffff', '#ffffff'],
    'perola':    ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'perola_t':  ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff'],
    'tartaruga': ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'tartaruga_t': ['#313638', '#165a4c', '#239063', '#1ebc73', '#91db69'],
    'casco':     ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90'],
    'tronco':    ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'leviata':   ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'leviata_t': ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6'],
    'escuro_az': ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6'],
    'pele_alm':  ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'],
    'serpente':  ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'serpente_t': ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6'],
    'creme':     ['#ab947a', '#e6904e', '#fbb954', '#fdcbb0', '#fdcbb0'],
})

PALETA = set(('2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 '
              'ea4f36 f57d4a ae2334 e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 '
              'd5e04b fbff86 165a4c 239063 1ebc73 91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b '
              '30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff 45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f '
              'ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0').split())


# ---------------------------------------------------------------- ajudas
def rp(nome):
    return R[nome] if isinstance(nome, str) else nome


def px(P, pts, cor, z):
    """Píxeis de uma cor só (olhos, brilhos, marcas), sem contorno."""
    P.append(Parte({(int(round(x)), int(round(y))) for x, y in pts}, None, z=z, separar=False, cor=cor))


def parte(P, m, rampa, z, **kw):
    p = Parte(m, rp(rampa), z=z, **kw)
    P.append(p)
    return m


def corrente(pts, r0, r1):
    """Uma "corrente" de cápsulas ao longo de pontos, com o raio a ir de r0 a r1 (caudas, tentáculos, pescoços)."""
    m = set()
    n = len(pts) - 1
    for i in range(n):
        r = r0 + (r1 - r0) * (i + 0.5) / max(1, n)
        m |= capsula(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], r)
    return m


def curva(x, y, ang, comp, curvar, passos=8, onda=0.0, fase=0.0):
    """Pontos de uma linha que vai encaracolando (ângulo em graus; curvar = graus por passo)."""
    pts = [(x, y)]
    a = math.radians(ang)
    d = comp / passos
    for i in range(passos):
        a += math.radians(curvar) + onda * math.sin(fase + i * 0.9)
        x += math.cos(a) * d
        y += math.sin(a) * d
        pts.append((x, y))
    return pts


def olho(P, x, y, iris, z, tam=1, fechado=False, pupila=OUT, brilho=BRANCO):
    """Olho de lado: tam 1 = 2×2 (íris + pupila + brilho); tam 2 = 3×3; fechado = risco."""
    x, y = int(x), int(y)
    if fechado:
        px(P, [(x + i, y + tam - 1) for i in range(tam + 1)], OUT, z)
        return
    if tam == 0:
        px(P, [(x, y)], iris, z)
        return
    n = tam + 1
    px(P, [(x + i, y + j) for i in range(n) for j in range(n)], iris, z)
    px(P, [(x + n - 1, y + n - 1)] + ([(x + n - 2, y + n - 1), (x + n - 1, y + n - 2)] if tam >= 2 else []), pupila, z + 0.01)
    px(P, [(x, y)], brilho, z + 0.02)


def brilhos(P, pts, fase, z, cores=('#ffffff', '#fbff86')):
    """Estrelinhas a piscar: cada ponto acende num quadro diferente."""
    for i, (x, y) in enumerate(pts):
        f = (fase + i) % 4
        if f == 0:
            px(P, [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], cores[0], z)
        elif f == 1:
            px(P, [(x, y)], cores[1], z)


def bolha(P, x, y, r, z):
    x, y = int(x), int(y)
    if r < 1.0:
        px(P, [(x, y)], '#8ff8e2', z)
        return
    if r < 1.8:
        px(P, [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)], '#8ff8e2', z)
        px(P, [(x - 1, y - 1)], BRANCO, z)
        return
    anel = elipse(x, y, r, r) - elipse(x, y, r - 1, r - 1)
    px(P, anel, '#8ff8e2', z)
    px(P, [(int(x - r / 2), int(y - r / 2))], BRANCO, z + 0.01)


# ---------------------------------------------------------------- texturas (depois de desenhar: mudam o tom na rampa)
def textura(img, mascara, rampa, fn):
    """Para cada píxel da máscara que ainda é da rampa, fn(x, y) diz -1 (mais escuro), +1 (mais claro) ou 0."""
    rampa = rp(rampa)
    ix = {}
    for i, c in enumerate(rampa):
        ix.setdefault(c, i)
    pix = img.load()
    w, h = img.size
    for (x, y) in mascara:
        if not (0 <= x < w and 0 <= y < h):
            continue
        r, g, b, a = pix[x, y]
        if not a:
            continue
        c = '#%02x%02x%02x' % (r, g, b)
        if c not in ix:
            continue
        d = fn(x, y)
        if not d:
            continue
        i = max(0, min(4, ix[c] + d))
        if d < 0 and i == ix[c]:
            continue
        n = rampa[i]
        pix[x, y] = tuple(int(n[k:k + 2], 16) for k in (1, 3, 5)) + (255,)


def escamas(passo=4, alt=3, dy=0):
    """Escamas em fiadas desencontradas: uma risca escura em baixo de cada escama e um brilho em cima."""
    def fn(x, y):
        yy = y - dy
        lin = yy // alt
        u = (x + (lin % 2) * (passo // 2)) % passo
        v = yy % alt
        if v == alt - 1 and u != 0:
            return -1
        if v == 0 and u == 1:
            return 1
        return 0
    return fn


def pintas(semente, dens=0.08, claro=0.0, dy=0):
    def fn(x, y):
        h = ((x * 73856093) ^ ((y - dy) * 19349663) ^ (semente * 83492791)) & 1023
        if h < dens * 1024:
            return -1
        if h > 1024 - claro * 1024:
            return 1
        return 0
    return fn


def riscas(periodo, larg, inclina=0.0, dy=0):
    def fn(x, y):
        u = x + (y - dy) * inclina
        return -2 if (u % periodo) < larg else 0
    return fn


def render(P, S, texturas=()):
    img = desenhar(P, S, S)
    for (m, rampa, fn) in texturas:
        textura(img, m, rampa, fn)
    return img


RESP = (0, 0, 1, 1)   # respirar: o corpo desce 1 píxel nos quadros 2 e 3
FLUT = (0, -1, -1, 0)  # flutuar


# ================================================================ CARANGUEJOS
def caranguejo(t, S=48, rei=False):
    """Caranguejo Gigante (48) e Caranguejo Rei Pinça-de-Ouro (64, dourado, coroa e pinça de ouro maciço).
    Carapaça larga com espinhos na borda e bossas, olhos pretos em pedúnculos, patas com articulações e pontas
    escuras, a pinça da frente (grande, com dentes) abre e fecha devagar e sai uma bolha da boca."""
    k = S / 48.0
    P, T = [], []
    dy = RESP[t]
    corpo = 'ouro_corpo' if rei else 'carapaca'
    corpo_t = 'ouro_t' if rei else 'carapaca_t'
    pata = 'laranja' if rei else 'carapaca'
    chao = S - 2
    cx, cy, rx, ry = 20 * k, 30 * k + dy, 13.5 * k, 7.6 * k

    def perna(rx_, ry_, kx, ky, tx, rampa, z):
        r0 = 1.45 * k
        parte(P, capsula(rx_ * k, ry_ * k + dy, kx * k, ky * k + dy, r0), rampa, z, volume='cilindro_h')
        parte(P, capsula(kx * k, ky * k + dy, tx * k, chao, r0 * 0.75), rampa, z + 0.01, volume='cilindro_v')
        px(P, [(tx * k, chao), (tx * k, chao - 1)], '#3e3546', z + 0.02)                 # ponta escura
        px(P, [(kx * k, ky * k + dy - 1)], rp(rampa)[4], z + 0.02)                        # brilho no joelho
    # ---- patas de trás (lado de lá: escuras, atrás de tudo)
    for i, (a, b, c, d, e) in enumerate(((11, 32, 4, 24, 0.5), (15, 34, 9, 26, 6), (25, 34, 32, 26, 37), (28, 33, 38, 26, 43))):
        perna(a, b, c, d, e, corpo_t, 0.2 + i * 0.02)
    # ---- pinça de trás (pequena, escura)
    parte(P, capsula(28 * k, 31 * k + dy, 33 * k, 25 * k + dy, 2.0 * k), corpo_t, 0.5)
    parte(P, elipse(34 * k, 21 * k + dy, 3.4 * k, 3.0 * k), corpo_t, 0.6)
    parte(P, poligono([(35 * k, 18.5 * k + dy), (40 * k, 16.5 * k + dy), (38.5 * k, 19.5 * k + dy), (36 * k, 21 * k + dy)]), corpo_t, 0.61)
    # ---- barriga (por baixo da carapaça, às riscas)
    barr = parte(P, elipse(cx + 1 * k, cy + 6 * k, 10.5 * k, 3.2 * k), 'barriga', 1.5, volume='cilindro_h')
    T.append((barr, 'barriga', riscas(3, 1)))
    # ---- patas do lado de cá (por baixo da carapaça, mais claras)
    for i, (a, b, c, d, e) in enumerate(((12, 35, 5, 29, 2), (17, 37, 11, 31, 8.5), (24, 37, 30, 31, 33))):
        perna(a, b, c, d, e, pata, 1.7 + i * 0.02)
    # ---- carapaça: elipse larga + espinhos na borda da frente e de trás
    cara = elipse(cx, cy, rx, ry)
    for ang in (-160, -140, -120, -60, -40, -20, 0):
        a = math.radians(ang)
        ex, ey = cx + math.cos(a) * rx * 0.97, cy + math.sin(a) * ry * 0.97
        ox, oy = math.cos(a), math.sin(a)
        L = 2.4 * k
        cara |= poligono([(ex - oy * 1.4 * k, ey + ox * 1.4 * k), (ex + ox * L, ey + oy * L), (ex + oy * 1.4 * k, ey - ox * 1.4 * k)])
    parte(P, cara, corpo, 2)
    T.append((cara, corpo, pintas(5 if rei else 3, 0.025 if rei else 0.035, 0.02, dy)))
    # sulco em "H" no meio da carapaça (como nos caranguejos de verdade)
    for i in range(int(7 * k)):
        x = cx - 3 * k + i
        px(P, [(x, cy - 1 * k + 0.08 * (i - 3.5 * k) ** 2 / k)], R[corpo][1], 2.05)
    # bossas: um ponto claro com sombra por baixo
    for (bx, by) in ((-7, -4), (-2, -5.5), (4, -4.5), (-10, -0.5), (8, -1)):
        x, y = cx + bx * k, cy + by * k
        px(P, [(x, y)], R[corpo][4], 2.1)
        px(P, [(x, y + 1)], R[corpo][1], 2.1)
    if not rei:
        # um raminho de alga e uma craca presos na carapaça
        px(P, [(cx - 6 * k, cy - ry - 1), (cx - 6 * k, cy - ry), (cx - 7 * k, cy - ry - 2)], '#1ebc73', 2.3)
        px(P, [(cx - 6 * k + (t % 2), cy - ry - 3)], '#91db69', 2.3)
        parte(P, retangulo(int(cx - 1 * k), int(cy - ry), int(cx - 1 * k) + 2, int(cy - ry) + 1), 'osso_t', 2.2, plano=True)
        px(P, [(int(cx - 1 * k) + 1, int(cy - ry))], OUT, 2.25)
    # ---- olhos em pedúnculos (o de trás escuro)
    for (sx, sy, ex, ey, zz) in ((25, 24, 26, 18, 1.0), (28.5, 24, 30, 17, 2.5)):
        parte(P, capsula(sx * k, sy * k + dy, ex * k, ey * k + dy, 1.0 * k), corpo if zz > 2 else corpo_t, zz, volume='cilindro_v')
        e = elipse(ex * k + 0.5, (ey - 1.2) * k + dy, 1.6 * k, 1.6 * k)
        parte(P, e, ['#2e222f', '#2e222f', '#3e3546', '#625565', '#9babb2'], zz + 0.05)
        if t == 3 and zz > 2:      # pestaneja
            parte(P, e, corpo, zz + 0.06)
            px(P, [(ex * k - 1, (ey - 1) * k + dy), (ex * k, (ey - 1) * k + dy), (ex * k + 1, (ey - 1) * k + dy)], OUT, zz + 0.07)
        else:
            px(P, [(ex * k, (ey - 1.8) * k + dy)], BRANCO, zz + 0.1)
    # boca: palpos peludos à frente
    for i in range(int(2 * k)):
        px(P, [(cx + rx - 1 + i * 0.6, cy + 2 * k + i), (cx + rx + i * 0.6, cy + 2 * k + i)], R['barriga'][2 + (i % 2)], 2.4)
    # ---- coroa (Rei)
    if rei:
        bx, by = cx - 2 * k, cy - ry
        coroa = poligono([(bx - 5 * k, by + 1 * k), (bx - 5.5 * k, by - 4 * k), (bx - 3 * k, by - 1.5 * k), (bx - 0.5 * k, by - 5.5 * k),
                          (bx + 2 * k, by - 1.5 * k), (bx + 4.5 * k, by - 4 * k), (bx + 4.5 * k, by + 1 * k)])
        parte(P, coroa, 'ouro', 4, plano=True)
        px(P, [(bx - 1 * k, by - 1 * k)], '#e83b3b', 4.1)
        px(P, [(bx - 4 * k, by - 0.5 * k), (bx + 3 * k, by - 0.5 * k)], '#4d9be6', 4.1)
    # ---- pinça da frente (grande) — abre e fecha
    ab = (0, 1, 2, 1)[t]
    br = 'ouro' if rei else corpo
    kk = 1.32 if rei else 1.0
    om, co = (29 * k, 33 * k + dy), (35 * k, 36 * k + dy)
    hx, hy = (37.5 if rei else 38.5) * k, (27 if rei else 28) * k + dy
    parte(P, capsula(*om, *co, 2.2 * k), corpo, 5, volume='cilindro_h')
    parte(P, capsula(*co, hx - 1 * k, hy + 3 * k, 2.4 * k), corpo, 5.1)
    px(P, [(co[0] - 1, co[1] - 2 * k), (co[0], co[1] - 2 * k)], R[corpo][4], 5.15)
    palma = elipse(hx, hy, 4.6 * k * kk, 4.0 * k * kk)
    parte(P, palma, br, 6)
    a = -ab * 1.3 * k
    dedo_b = poligono([(hx + 1 * k, hy + 0.5 * k), (hx + 8.5 * k * kk, hy + 0 * k), (hx + 7.5 * k * kk, hy + 2.2 * k), (hx + 1 * k, hy + 3.6 * k * kk)])
    dedo_c = poligono([(hx + 0 * k, hy - 3.6 * k * kk), (hx + 5 * k * kk, hy - 5 * k * kk + a), (hx + 9.2 * k * kk, hy - 2.5 * k + a * 1.1),
                       (hx + 6 * k * kk, hy - 1.4 * k + a * 0.6), (hx + 1 * k, hy - 0.8 * k)])
    parte(P, dedo_b, br, 6.1)
    parte(P, dedo_c, br, 6.2)
    # pontas escuras e dentinhos claros por dentro
    px(P, [(hx + 8.5 * k * kk - 1, hy + 0.3 * k)], R[br][0], 6.3)
    px(P, [(hx + 9.2 * k * kk - 1, hy - 2.5 * k + a * 1.1)], R[br][0], 6.3)
    px(P, [(hx + 4 * k, hy - 0.2 * k), (hx + 6 * k, hy - 0.2 * k)], R['barriga'][4], 6.3)
    px(P, [(hx + 5 * k, hy - 1.6 * k + a * 0.6)], R['barriga'][4], 6.3)
    T.append((palma | dedo_b | dedo_c, br, pintas(9, 0.05, 0, dy)))
    if rei:
        brilhos(P, [(int(hx - 1 * k), int(hy - 2 * k)), (int(hx + 6 * k), int(hy - 4 * k)), (int(hx + 2 * k), int(hy + 2 * k)),
                    (int(cx - 2 * k), int(cy - ry - 6 * k))], t, 7)
    # bolha a subir da boca
    by = (21, 17, 13, 9)[t] * k + dy
    bolha(P, 45 * k + (t % 2), by, (0.6, 1.2, 1.2, 2.0)[t] * k, 8)
    return render(P, S, T)


def caranguejo_rei(t):
    return caranguejo(t, 64, rei=True)


# ================================================================ PIRATA ESQUELETO (32)
def pirata_esqueleto(t):
    """Esqueleto pirata: chapéu de bicos com caveira, colete vermelho aberto (vê-se as costelas), perna de pau,
    brinco de ouro, olho vermelho a brilhar na órbita, sabre curvo. Os dentes batem e o sabre reluz."""
    P, T = [], []
    d = RESP[t]
    # perna de trás (osso) e de cá (perna de pau)
    parte(P, capsula(13, 21, 12.5, 25, 1.7), 'casaco_vt', 0.5)
    parte(P, capsula(12.5, 25, 12.5, 30, 0.8), 'osso_t', 0.4)
    parte(P, capsula(12.5, 30, 14.5, 30, 0.8), 'osso_t', 0.41)
    parte(P, capsula(17, 21, 17, 25, 2.0), 'casaco_v', 3)
    parte(P, capsula(17, 25, 17, 30, 1.1), 'madeira', 2.9, volume='cilindro_v')
    px(P, [(16, 27), (17, 27), (18, 27)], '#4c3e24', 2.95)
    # braço de trás (osso, atrás do corpo)
    parte(P, capsula(13, 14 + d, 11, 18 + d, 0.8), 'osso_t', 0.6)
    parte(P, capsula(11, 18 + d, 11, 20 + d, 0.9), 'osso_t', 0.61)
    # tronco: colete vermelho com as costelas à mostra
    tronco = parte(P, elipse(15.2, 16.6 + d, 3.9, 4.2), 'casaco_v', 2)
    T.append((tronco, 'casaco_v', riscas(4, 1, 0.5)))
    cost = elipse(16.8, 16.4 + d, 1.9, 3.0)
    parte(P, cost, 'osso', 2.1, plano=True)
    for y in (15, 17, 19):
        px(P, [(16, y + d), (17, y + d), (18, y + d)], '#7f708a', 2.15)
    px(P, [(14, 13 + d), (14, 14 + d), (14, 15 + d)], '#f9c22b', 2.2)   # botões
    # cinto com fivela
    parte(P, retangulo(11, 20 + d, 19, 21 + d), 'couro', 2.4, plano=True)
    px(P, [(17, 20 + d), (18, 20 + d), (17, 21 + d), (18, 21 + d)], '#f9c22b', 2.45)
    # caveira
    cab = parte(P, elipse(16, 8.6 + d, 4.3, 4.1), 'osso', 4)
    queixo = 1 if t in (1, 3) else 0
    parte(P, retangulo(16, 12 + d + queixo, 19, 13 + d + queixo), 'osso', 3.9, plano=True)
    for x in (16, 18):
        px(P, [(x, 12 + d + queixo)], '#7f708a', 3.95)
    px(P, [(x, 12 + d) for x in range(16, 20)] if queixo else [], OUT, 3.96)
    px(P, [(17, 11 + d), (18, 11 + d), (19, 11 + d)], OUT, 4.1)                    # dentes de cima
    px(P, [(17, 11 + d), (19, 11 + d)], '#c7dcd0', 4.12)
    px(P, [(17, 8 + d), (18, 8 + d), (17, 9 + d), (18, 9 + d), (19, 9 + d)], OUT, 4.2)  # órbita
    px(P, [(18, 9 + d)], ('#e83b3b', '#f57d4a', '#e83b3b', '#ea4f36')[t], 4.3)
    px(P, [(20, 10 + d)], OUT, 4.2)                                                 # nariz
    px(P, [(14, 11 + d)], '#f9c22b', 4.3)                                           # brinco
    # chapéu de bicos (com aba virada à frente e uma caveirinha)
    parte(P, poligono([(11, 7.5 + d), (12, 3 + d), (15, 1.5 + d), (19, 2.5 + d), (20.5, 7 + d)]), 'chapeu', 5)
    parte(P, capsula(9, 7 + d, 21, 6.5 + d, 1.2), 'chapeu', 5.1)
    parte(P, capsula(20, 6.5 + d, 23, 4 + d, 1.0), 'chapeu', 5.2)
    px(P, [(x, 6 + d) for x in range(11, 21)], '#f9c22b', 5.3)                       # galão dourado
    px(P, [(15, 3 + d), (16, 3 + d), (15, 4 + d)], '#c7dcd0', 5.3)
    # braço da frente com o sabre
    parte(P, capsula(17, 14 + d, 19, 17 + d, 1.4), 'casaco_v', 6)
    parte(P, capsula(19, 17 + d, 22, 18 + d, 0.8), 'osso', 6.1)
    lam = [(23, 17 + d), (25, 15 + d), (27, 12 + d), (28, 9 + d)]
    parte(P, corrente(lam, 0.9, 0.6), 'ferro', 5.9, plano=True)
    px(P, [lam[min(3, t)]], BRANCO, 5.95)
    parte(P, retangulo(21, 16 + d, 23, 19 + d), 'ouro', 6.2, plano=True)
    return render(P, 32, T)


# ================================================================ HOMEM-TUBARÃO (32)
def homem_tubarao(t):
    """Tubarão de pé: cabeça comprida com focinho, boca cheia de dentes, guelras, barbatana dorsal, barriga
    branca, cauda de tubarão, tanga de corda, colar de dentes e uma cicatriz. As guelras e a cauda mexem."""
    P, T = [], []
    d = RESP[t]
    ca = (0, 1, 0, -1)[t]
    # cauda de tubarão
    parte(P, capsula(12, 21 + d, 7, 23 + d + ca * 0.5, 1.6), 'tubarao_t', 0.3)
    parte(P, poligono([(8, 23 + d), (3, 18 + d + ca), (5, 23 + d), (3, 28 + d - ca), (8, 24 + d)]), 'tubarao_t', 0.31)
    # pernas
    parte(P, capsula(13, 22, 12, 29, 1.7), 'tubarao_t', 0.5)
    parte(P, capsula(12, 30, 14, 30, 1.0), 'tubarao_t', 0.51)
    parte(P, capsula(17, 22, 18, 29, 1.9), 'tubarao', 3)
    parte(P, capsula(18, 30, 21, 30, 1.0), 'tubarao', 3.1)
    px(P, [(22, 30)], '#c7dcd0', 3.2)
    # braço de trás
    parte(P, capsula(13, 13 + d, 11, 19 + d, 1.3), 'tubarao_t', 0.6)
    px(P, [(10, 20 + d), (12, 20 + d)], '#c7dcd0', 0.65)
    # tronco + barriga branca
    tr = parte(P, elipse(15.5, 15.8 + d, 4.6, 5.2), 'tubarao', 2)
    T.append((tr, 'tubarao', pintas(2, 0.06, 0.0, d)))
    parte(P, elipse(18, 16.8 + d, 2.2, 4.0), 'branco', 2.1)
    # barbatana dorsal (nas costas)
    parte(P, poligono([(10.5, 14 + d), (9.5, 6 + d), (14.5, 11.5 + d)]), 'tubarao', 1.9)
    # tanga de corda
    parte(P, poligono([(11, 19 + d), (20, 19 + d), (20, 22 + d), (18, 23 + d), (16, 21.5 + d), (14, 24 + d), (11, 22 + d)]), 'couro', 2.5)
    px(P, [(x, 19 + d) for x in range(11, 21)], '#ab947a', 2.55)
    # cabeça de tubarão
    cab = elipse(16.5, 8.2 + d, 4.6, 3.8) | poligono([(17, 4.6 + d), (25.5, 8 + d), (24.5, 10.2 + d), (17, 11.5 + d)])
    parte(P, cab, 'tubarao', 4)
    T.append((cab, 'tubarao', pintas(6, 0.05, 0.0, d)))
    queixo = poligono([(16, 10 + d), (24, 10 + d), (22.5, 12.2 + d), (16, 12.6 + d)])
    parte(P, queixo, 'branco', 4.1)
    px(P, [(x, 10 + d) for x in range(18, 25)], OUT, 4.2)                           # boca
    px(P, [(19, 11 + d), (21, 11 + d), (23, 11 + d)], BRANCO, 4.25)               # dentes de baixo
    px(P, [(20, 9 + d), (22, 9 + d)], BRANCO, 4.25)                               # dentes de cima
    olho(P, 19, 6 + d, '#2e222f', 4.3, tam=1, pupila=OUT, brilho=BRANCO) if t != 2 else olho(P, 19, 6 + d, '', 4.3, fechado=True)
    px(P, [(21, 7 + d), (22, 8 + d)], '#8fd3ff', 4.25)                             # cicatriz
    gu = (0, 1, 0, 1)[t]
    for x in (14, 15.5, 17):
        px(P, [(x, 10 + d + gu), (x, 11 + d + gu)], '#323353', 4.3)                 # guelras
    # colar de dentes
    px(P, [(15, 13 + d), (17, 14 + d), (19, 14 + d)], BRANCO, 4.4)
    px(P, [(16, 13 + d), (18, 14 + d)], '#966c6c', 4.4)
    # braço da frente com barbatana no antebraço e garras
    parte(P, capsula(18, 13 + d, 20, 17 + d, 1.4), 'tubarao', 6)
    parte(P, capsula(20, 17 + d, 22, 19 + d, 1.3), 'tubarao', 6.1)
    parte(P, poligono([(19, 16 + d), (17, 19 + d), (20, 18 + d)]), 'tubarao_t', 5.9)
    px(P, [(23, 20 + d), (22, 21 + d), (24, 19 + d)], '#c7dcd0', 6.2)
    return render(P, 32, T)


# ================================================================ BARBA-LODO (32)
def barba_lodo(t):
    """Pirata fantasma: cara verde-água transparente, olhos a brilhar, chapéu de bicos com cracas e uma pena,
    barba comprida de algas (abana e pinga lodo), casaco de lodo com botões de ouro e uma lanterna fantasma."""
    P, T = [], []
    d = RESP[t]
    # pernas (calças de lodo e botas)
    parte(P, capsula(13, 21, 12.5, 28, 1.7), 'lodo', 0.5)
    parte(P, retangulo(11, 28, 14, 30), 'chapeu', 0.55)
    parte(P, capsula(17, 21, 17.5, 28, 1.9), 'lodo', 3)
    parte(P, retangulo(16, 28, 20, 30), 'chapeu', 3.1)
    px(P, [(16, 28), (17, 28)], '#625565', 3.15)
    # braço de trás
    parte(P, capsula(13, 13 + d, 11, 19 + d, 1.3), 'lodo', 0.6)
    parte(P, elipse(11, 20 + d, 1.3, 1.2), 'fantasma_t', 0.61)
    # casaco comprido
    cas = parte(P, poligono([(10.5, 12 + d), (19.5, 12 + d), (20.5, 23 + d), (17.5, 22 + d), (15, 24 + d), (10, 23 + d)]), 'lodo', 2)
    T.append((cas, 'lodo', pintas(3, 0.09, 0.03, d)))
    px(P, [(18, 14 + d), (18, 17 + d), (18, 20 + d)], '#f9c22b', 2.1)
    parte(P, retangulo(10, 18 + d, 20, 19 + d), 'couro', 2.2, plano=True)
    # cabeça fantasma
    cab = parte(P, elipse(16, 8.6 + d, 4.0, 3.9), 'fantasma', 4)
    for i in range(2):
        cor = ('#cddf6c', '#fbff86', '#cddf6c', '#91db69')[t]
        px(P, [(17 + i * 2, 8 + d), (18 + i * 2, 8 + d)], OUT, 4.2)
        px(P, [(17 + i * 2, 8 + d)], cor, 4.3)
    px(P, [(18, 7 + d), (19, 6 + d), (20, 7 + d)], '#165a4c', 4.25)                # sobrolho
    # barba de algas em fios (abanam)
    for i, x in enumerate(range(14, 21)):
        comp = 6 + (i * 5) % 5
        ox = round(math.sin(i * 1.3 + t * 1.57) * 1.2)
        fio = capsula(x, 11 + d, x + ox, 11 + comp + d, 0.7 if i % 2 else 0.9)
        parte(P, fio, 'alga_t' if i % 2 else 'alga', 4.5 + i * 0.01)
    gota = (16 + 2 * d, 17 + t * 3)
    if gota[1] < 30:
        px(P, [(18, 17 + t * 3 + d), (18, 18 + t * 3 + d)], '#91db69', 4.6)
    # chapéu de bicos com pena e cracas
    parte(P, poligono([(11, 7 + d), (12, 3 + d), (15, 1.5 + d), (19, 2.5 + d), (20.5, 6.5 + d)]), 'chapeu', 5)
    parte(P, capsula(9, 6.5 + d, 21.5, 6 + d, 1.2), 'chapeu', 5.1)
    px(P, [(13, 3 + d), (14, 3 + d)], '#c7dcd0', 5.2)
    px(P, [(18, 3 + d)], '#c7dcd0', 5.2)
    px(P, [(13, 4 + d), (18, 4 + d)], '#625565', 5.2)
    pena = curva(12, 3 + d, -150, 7, 12, 5, 0.12, t * 1.6)
    parte(P, corrente(pena, 1.0, 0.6), 'alga', 5.3)
    # braço da frente com a lanterna fantasma
    parte(P, capsula(17, 13 + d, 20, 17 + d, 1.4), 'lodo', 6)
    parte(P, elipse(21, 17.5 + d, 1.3, 1.2), 'fantasma', 6.1)
    lx, ly = 22, 21 + d + (0, 0, 1, 0)[t]
    px(P, [(22, 18 + d), (22, 19 + d)], '#625565', 6.15)
    parte(P, retangulo(lx - 1, ly - 1, lx + 2, ly + 3), 'ferro_t', 6.2, plano=True)
    px(P, [(lx, ly), (lx + 1, ly), (lx, ly + 1), (lx + 1, ly + 1), (lx, ly + 2), (lx + 1, ly + 2)], '#91db69', 6.3)
    px(P, [(lx, ly + 1 - (t % 2)), (lx + 1, ly + 2 - (t % 2))], '#fbff86', 6.35)
    for i, (gx, gy) in enumerate(((-3, 0), (4, 1), (1, -3), (2, 5))):
        if (t + i) % 2 == 0:
            px(P, [(lx + gx, ly + gy)], '#cddf6c', 6.4)
    return render(P, 32, T)


# ================================================================ SEREIA SOMBRIA (32)
def sereia_sombria(t):
    """Sentada numa rocha da maré: cabelo comprido roxo-escuro que ondula, olho a brilhar, conchas, cauda de
    escamas verde-azuladas enrolada na rocha e a barbatana a abanar. Uma nota de canto sobe de vez em quando."""
    P, T = [], []
    d = RESP[t]
    # rocha com algas
    roc = parte(P, elipse(15, 29.5, 10, 3.5) | elipse(11, 27.5, 5.5, 3), 'rocha', 0.2)
    T.append((roc, 'rocha', pintas(4, 0.1, 0.06)))
    px(P, [(7, 28), (7, 29), (8, 30), (22, 29), (23, 30)], '#239063', 0.3)
    px(P, [(6, 27), (23, 28)], '#1ebc73', 0.3)
    px(P, [(19, 27), (20, 27)], '#f68181', 0.3)                                    # concha
    # cauda enrolada e barbatana
    fl = (0, -1, 0, 1)[t]
    cauda = corrente([(16, 21 + d), (14, 24.5), (10, 26), (6, 25), (4, 22 + fl * 0.5)], 3.0, 1.3)
    parte(P, cauda, 'cauda_ser', 1)
    T.append((cauda, 'cauda_ser', escamas(3, 2)))
    bar = poligono([(4.5, 22.5 + fl * 0.5), (1, 16 + fl), (3.5, 18 + fl), (5.5, 20)]) | poligono([(4, 22 + fl * 0.5), (7, 16 + fl), (7, 19 + fl), (5, 21)])
    parte(P, bar, 'barbatana', 1.1)
    px(P, [(2, 17 + fl), (6, 17 + fl)], BRANCO, 1.15)
    parte(P, poligono([(13, 25), (11, 28), (15, 26)]), 'barbatana', 1.05)          # barbatana da anca
    # cabelo de trás (comprido, a ondular)
    on = (0, 1, 1, 0)[t]
    cab_t = corrente([(15, 6 + d), (12.5, 10 + d), (12 + on, 14 + d), (12.5, 18 + d), (11 + on, 21 + d)], 3.2, 1.6)
    parte(P, cab_t, 'cabelo_ser', 0.8)
    T.append((cab_t, 'cabelo_ser', riscas(3, 1, -0.4)))
    # braço de trás
    parte(P, capsula(15, 13 + d, 13, 19 + d, 1.0), 'pele_ser', 0.9, luz=-0.2)
    # tronco
    parte(P, capsula(16.5, 13 + d, 16, 19.5 + d, 2.8), 'pele_ser', 2, volume='cilindro_v')
    parte(P, elipse(18, 14.5 + d, 1.6, 1.2), 'roxo', 2.1)                          # top de concha
    px(P, [(18, 14 + d)], '#eaaded', 2.15)
    px(P, [(14, 19 + d), (15, 20 + d), (17, 20 + d), (18, 19 + d)], '#0eaf9b', 2.2)   # escamas na anca
    # cabeça
    cab = parte(P, elipse(17.5, 8.5 + d, 3.6, 3.8), 'pele_ser', 4, luz=0.1)
    if t == 3:
        px(P, [(19, 8 + d), (20, 8 + d)], OUT, 4.3)
    else:
        px(P, [(19, 7 + d), (20, 7 + d), (19, 8 + d), (20, 8 + d)], '#30e1b9', 4.3)
        px(P, [(20, 8 + d)], '#0b5e65', 4.31)
        px(P, [(19, 7 + d)], BRANCO, 4.32)
    px(P, [(20, 11 + d), (21, 10 + d)], '#831c5d', 4.3)                            # boca escura
    # cabelo da frente (franja e madeixa por cima do ombro)
    franja = elipse(16.5, 6 + d, 4.2, 2.8) | capsula(14, 6 + d, 14.5, 11 + d, 1.8)
    parte(P, franja, 'cabelo_ser', 4.5)
    madeixa = corrente([(18.5, 6 + d), (21, 5 + d), (21.5, 7.5 + d)], 1.2, 0.8)
    parte(P, madeixa, 'cabelo_ser', 4.55)
    px(P, [(16, 4 + d), (17, 4 + d)], '#a884f3', 4.6)
    px(P, [(14, 6 + d)], '#f68181', 4.6)                                           # flor de coral no cabelo
    # braço da frente apoiado na rocha
    parte(P, capsula(18, 13.5 + d, 20.5, 19 + d, 1.1), 'pele_ser', 6)
    parte(P, capsula(20.5, 19 + d, 21.5, 23, 1.0), 'pele_ser', 6.1)
    px(P, [(18, 13 + d + 3)], '#30e1b9', 6.2)                                       # pulseira
    # nota de canto
    if t in (1, 2):
        nx, ny = 24 + t, 6 - t * 2
        px(P, [(nx, ny), (nx, ny + 1), (nx, ny + 2), (nx - 1, ny + 2), (nx + 1, ny)], '#a884f3', 7)
    return render(P, 32, T)


# ================================================================ ALFORRECA ELÉTRICA (32)
def alforreca_eletrica(t):
    """Medusa amarela a flutuar: chapéu de gelatina com a borda franzida e anéis por dentro, dois olhinhos,
    braços orais franzidos, tentáculos finos a ondular e faíscas azuis a saltar."""
    P, T = [], []
    f = FLUT[t]
    cy = 12 + f
    sino = {p for p in elipse(16, cy + 1, 8.5, 7.2) if p[1] <= cy + 3}
    for x in range(8, 25, 3):
        sino |= elipse(x + 0.5, cy + 3.5, 1.7, 1.3)
    # tentáculos finos (atrás)
    for i, x in enumerate((9, 12, 20, 23)):
        pts = [(x + 0.5, cy + 4)]
        for j in range(1, 7):
            pts.append((x + 0.5 + math.sin(j * 0.9 + t * 1.57 + i) * 1.3, cy + 4 + j * 2.4))
        parte(P, corrente(pts, 0.55, 0.5), 'ouro' if i % 2 else 'laranja', 0.5 + i * 0.01, plano=True)
    # braços orais (franzidos, ao meio)
    for i, x in enumerate((14, 18)):
        pts = [(x, cy + 3)] + [(x + math.sin(j * 1.1 + t * 1.57 + i * 2) * 1.0, cy + 3 + j * 2.2) for j in range(1, 6)]
        m = corrente(pts, 1.5, 0.8)
        parte(P, m, 'laranja', 0.8 + i * 0.01)
        T.append((m, 'laranja', riscas(2, 1, 0.0, f)))
    # o chapéu
    parte(P, sino, 'ouro', 2)
    # anéis por dentro e pintas
    for (ax, ay) in ((12, 0), (16, -2), (20, 0)):
        anel = elipse(ax, cy + ay, 2.2, 1.6) - elipse(ax, cy + ay, 1.2, 0.7)
        px(P, anel, '#f79617', 2.1)
    px(P, [(x, cy + 3) for x in range(9, 24)], '#f79617', 2.05)
    px(P, [(11, cy - 4), (12, cy - 5)], BRANCO, 2.2)
    # olhinhos
    for ex in (14, 19):
        if t == 2:
            px(P, [(ex, cy + 1), (ex + 1, cy + 1)], OUT, 2.3)
        else:
            px(P, [(ex, cy), (ex + 1, cy), (ex, cy + 1), (ex + 1, cy + 1)], OUT, 2.3)
            px(P, [(ex, cy)], BRANCO, 2.31)
    # faíscas
    zig = [[(4, 9), (5, 10), (4, 11), (5, 12)], [(27, 7), (26, 8), (27, 9), (26, 10)], [(6, 19), (5, 20), (6, 21)],
           [(26, 17), (27, 18), (26, 19), (27, 20)]]
    for i, z in enumerate(zig):
        if (i + t) % 2 == 0:
            px(P, [(x, y + f) for x, y in z], '#8fd3ff' if i % 2 else '#4d9be6', 3)
            px(P, [(z[0][0], z[0][1] + f)], BRANCO, 3.01)
    return render(P, 32, T)


# ================================================================ PEIXE-LANTERNA (32)
def peixe_lanterna(t):
    """Peixe do abismo, escuro: boca enorme cheia de dentes de agulha, olho pálido, antena com a isca a
    brilhar (pulsa), pintas azuis luminosas no flanco, barbatanas esfarrapadas."""
    P, T = [], []
    f = FLUT[t]
    # barbatana da cauda e dorsal
    ca = (0, 1, 0, -1)[t]
    parte(P, poligono([(5, 12 + f), (0, 6 + f + ca), (2, 12 + f), (0, 19 + f - ca)]), 'abissal_t', 0.5)
    px(P, [(2, 8 + f + ca), (1, 17 + f - ca)], '#625565', 0.55)
    parte(P, poligono([(8, 7 + f), (10, 3 + f), (12, 5.5 + f), (14, 3.5 + f), (15, 6 + f)]), 'abissal_t', 0.6)
    # corpo
    corpo = elipse(13, 13 + f, 10, 7.5)
    parte(P, corpo, 'abissal', 2)
    T.append((corpo, 'abissal', pintas(8, 0.07, 0.03, f)))
    # boca aberta (cunha escura) e mandíbula de baixo saliente
    boca = poligono([(16, 13.5 + f), (25, 10 + f), (25, 16.5 + f)])
    px(P, boca, '#6e2727', 2.5)
    px(P, [(19, 14 + f), (20, 14 + f), (21, 14 + f)], '#b33831', 2.55)
    parte(P, poligono([(15, 16 + f), (26, 16 + f), (25, 19 + f), (16, 20.5 + f)]), 'abissal', 2.6)
    # dentes de agulha
    for x in (18, 20, 22, 24):
        px(P, [(x, 11.5 + f - (x - 18) * 0.35), (x, 12.5 + f - (x - 18) * 0.35)], BRANCO, 2.7)
        px(P, [(x + 1, 15 + f), (x + 1, 14 + f)], '#c7dcd0', 2.7)
    # olho pálido
    olho(P, 17, 7 + f, '#fbff86', 3, tam=1) if t != 3 else olho(P, 17, 7 + f, '', 3, fechado=True)
    # barbatana do peito
    parte(P, poligono([(11, 15 + f), (7, 20 + f + ca), (10, 20 + f), (13, 17 + f)]), 'abissal_t', 3.2)
    # pintas luminosas
    for i, (x, y) in enumerate(((7, 13), (10, 15), (13, 16.5))):
        px(P, [(x, y + f)], '#30e1b9' if (i + t) % 2 else '#8ff8e2', 3.3)
    # antena e isca
    ant = curva(15, 6 + f, -80, 8, 22, 6)
    parte(P, corrente(ant, 0.6, 0.5), 'rocha', 1.5, plano=True)
    lx, ly = int(ant[-1][0]), int(ant[-1][1]) + 1
    pul = (0, 1, 2, 1)[t]
    if pul:
        halo = elipse(lx + 0.5, ly + 0.5, 2 + pul * 0.7, 2 + pul * 0.7) - elipse(lx + 0.5, ly + 0.5, 1.6 + pul * 0.6, 1.6 + pul * 0.6)
        px(P, [p for i, p in enumerate(sorted(halo)) if i % 2 == 0], '#f79617', 3.9)
    parte(P, elipse(lx + 0.5, ly + 0.5, 1.8, 1.8), 'ouro', 4)
    px(P, [(lx, ly)], BRANCO, 4.1)
    return render(P, 32, T)


# ================================================================ POLVO (48)
def polvo(t):
    """Polvo roxo: manto grande inclinado para trás com pintas e verrugas, olhos amarelos de pupila deitada em
    cima de bossas, sifão, oito tentáculos a encaracolar e a ondular, com ventosas cor-de-rosa."""
    P, T = [], []
    d = RESP[t]
    fa = t * math.pi / 2
    # tentáculos de trás
    for i, (x, y, ang, cur) in enumerate(((16, 32, 160, -14), (20, 34, 120, -16), (30, 34, 50, 16), (34, 32, 20, 16))):
        pts = curva(x, y + d, ang, 15, cur, 8, 0.09, fa + i)
        parte(P, corrente(pts, 2.3, 0.7), 'polvo_t', 0.5 + i * 0.01)
    # manto
    manto = elipse(18, 15 + d, 10.5, 11) | elipse(24, 24 + d, 9, 7)
    parte(P, manto, 'polvo', 2)
    T.append((manto, 'polvo', pintas(12, 0.07, 0.03, d)))
    for (wx, wy) in ((12, 10), (16, 6), (20, 12), (11, 17)):
        px(P, [(wx, wy + d)], '#eaaded', 2.1)
        px(P, [(wx, wy + 1 + d)], '#6b3e75', 2.1)
    # sifão
    parte(P, capsula(17, 27 + d, 14, 28 + d, 1.4), 'polvo_t', 2.2)
    # bossas dos olhos
    for (ex, ey, zz) in ((27, 21, 2.3), (31, 22, 2.4)):
        parte(P, elipse(ex, ey + d, 3.2, 3.0), 'polvo', zz)
    for (ex, ey, zz) in ((26, 20, 2.31), (30, 21, 2.41)):
        if t == 3:
            px(P, [(ex, ey + 1 + d), (ex + 1, ey + 1 + d), (ex + 2, ey + 1 + d)], OUT, zz + 0.05)
        else:
            px(P, [(ex + i, ey + j + d) for i in range(3) for j in range(2)], '#f9c22b', zz + 0.05)
            px(P, [(ex, ey + 1 + d), (ex + 1, ey + 1 + d), (ex + 2, ey + 1 + d)], OUT, zz + 0.06)
            px(P, [(ex, ey + d)], BRANCO, zz + 0.07)
    # tentáculos da frente (com ventosas)
    for i, (x, y, ang, cur, comp) in enumerate(((18, 31, 150, -18, 16), (23, 32, 105, -22, 14), (28, 32, 75, 20, 14), (33, 30, 35, 18, 15))):
        pts = curva(x, y + d, ang, comp, cur, 9, 0.1, fa * 1.0 + i * 1.7)
        m = corrente(pts, 2.6, 0.8)
        parte(P, m, 'polvo', 3 + i * 0.01)
        for j in range(2, len(pts) - 1, 2):
            (x1, y1), (x2, y2) = pts[j], pts[j + 1]
            nx, ny = -(y2 - y1), (x2 - x1)
            n = math.hypot(nx, ny) or 1
            sx, sy = x1 + nx / n * 1.4, y1 + ny / n * 1.4
            if sy > y1:   # só do lado de baixo
                px(P, [(sx, sy)], '#ed8099', 3.05 + i * 0.01)
            else:
                sx, sy = x1 - nx / n * 1.4, y1 - ny / n * 1.4
                px(P, [(sx, sy)], '#ed8099', 3.05 + i * 0.01)
    return render(P, 48, T)
