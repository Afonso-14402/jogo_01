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
    'barriga_lev': ['#484a77', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff'],
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


def escamas(passo=4, alt=3, dy=0, arco=False):
    """Escamas em fiadas desencontradas: uma risca escura em baixo de cada escama e um brilho em cima.
    arco=True: escamas maiores em "U" (a borda de baixo curva), para os bichos grandes."""
    def fn(x, y):
        yy = y - dy
        lin = yy // alt
        u = (x + (lin % 2) * (passo // 2)) % passo
        v = yy % alt
        if arco:
            if (v == alt - 1 and 1 <= u <= passo - 2) or (v == alt - 2 and u in (0, passo - 1)):
                return -1
            if v == 0 and u in (1, 2):
                return 1
            return 0
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


def render(P, S, texturas=(), desloc=(0, 0)):
    img = desenhar(P, S, S)
    for (m, rampa, fn) in texturas:
        textura(img, m, rampa, fn)
    if desloc != (0, 0):
        out = Image.new('RGBA', img.size, (0, 0, 0, 0))
        out.paste(img, desloc, img)
        img = out
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
    """Esqueleto pirata (cabeça grande, como os outros bonecos de 32): chapéu de bicos com caveirinha e galão de ouro,
    órbita funda com um olho vermelho a brilhar, dentes que batem, brinco de ouro, colete vermelho aberto (vê-se as
    costelas), cinto com fivela, perna de pau e sabre curvo que reluz."""
    P, T = [], []
    d = RESP[t]
    # pernas: a de trás em osso, a de cá de pau
    parte(P, capsula(13.5, 23, 13, 25.5, 1.6), 'casaco_vt', 0.5)
    parte(P, capsula(13, 25.5, 12.5, 30, 0.8), 'osso_t', 0.4)
    parte(P, capsula(12.5, 30, 14.5, 30, 0.8), 'osso_t', 0.41)
    parte(P, capsula(17.5, 23, 17.5, 25.5, 1.9), 'casaco_v', 3)
    parte(P, capsula(17.5, 25.5, 17.5, 30, 1.1), 'madeira', 2.9, volume='cilindro_v')
    px(P, [(17, 28), (18, 28)], '#4c3e24', 2.95)
    # braço de trás (osso)
    parte(P, capsula(13, 17 + d, 11, 21 + d, 0.8), 'osso_t', 0.6)
    # tronco: colete vermelho às riscas, aberto à frente com as costelas à mostra
    tronco = parte(P, elipse(15.5, 19.5 + d, 4.0, 4.0), 'casaco_v', 2)
    T.append((tronco, 'casaco_v', riscas(3, 1, 0.6)))
    parte(P, elipse(17.3, 19.3 + d, 1.7, 2.6), 'osso', 2.1, plano=True)
    for y in (18, 20):
        px(P, [(16, y + d), (17, y + d), (18, y + d)], '#7f708a', 2.15)
    parte(P, retangulo(11, 22 + d, 19, 23 + d), 'couro', 2.4, plano=True)
    px(P, [(17, 22 + d), (18, 22 + d), (17, 23 + d), (18, 23 + d)], '#f9c22b', 2.45)
    # caveira grande
    cab = parte(P, elipse(16.5, 9.8 + d, 5.3, 4.9), 'osso', 4, luz=0.18)
    queixo = 1 if t in (1, 3) else 0
    parte(P, retangulo(16, 13 + d + queixo, 20, 14 + d + queixo), 'osso', 3.9, plano=True)
    px(P, [(x, 13 + d) for x in range(16, 21)] if queixo else [], OUT, 3.95)
    px(P, [(x, 12 + d) for x in range(16, 21)], OUT, 4.1)                           # linha dos dentes
    px(P, [(17, 12 + d), (19, 12 + d)], '#9babb2', 4.12)
    px(P, [(x, 14 + d + queixo) for x in (17, 19)], '#9babb2', 4.12)
    px(P, [(18 + i, 7 + j + d) for i in range(3) for j in range(3)], OUT, 4.2)    # órbita funda
    px(P, [(19, 8 + d)], ('#e83b3b', '#f57d4a', '#e83b3b', '#ea4f36')[t], 4.3)
    px(P, [(18, 9 + d)], '#6e2727', 4.3)
    px(P, [(21, 10 + d), (21, 11 + d)], OUT, 4.2)                                   # nariz
    px(P, [(13, 9 + d), (14, 11 + d)], '#9babb2', 4.2)                              # racha no crânio
    px(P, [(13, 13 + d), (13, 14 + d)], '#f9c22b', 4.3)                             # brinco
    # chapéu de bicos (só em cima da cabeça)
    parte(P, poligono([(11.5, 6 + d), (12.5, 1 + d), (16.5, 0 + d), (20.5, 1 + d), (21.5, 6 + d)]), 'chapeu', 5)
    parte(P, capsula(9.5, 5.6 + d, 22, 5.2 + d, 1.1), 'chapeu', 5.1)
    parte(P, capsula(21.5, 5.2 + d, 23.5, 3 + d, 0.9), 'chapeu', 5.2)
    px(P, [(x, 4 + d) for x in range(12, 21)], '#f9c22b', 5.3)                       # galão dourado
    px(P, [(16, 2 + d), (17, 2 + d)], '#c7dcd0', 5.3)
    px(P, [(16, 3 + d)], '#9babb2', 5.3)
    # braço da frente com o sabre
    parte(P, capsula(18, 17 + d, 20, 20 + d, 1.4), 'casaco_v', 6)
    parte(P, capsula(20, 20 + d, 22.5, 21 + d, 0.8), 'osso', 6.1)
    lam = [(23.5, 19.5 + d), (25.5, 17 + d), (27, 14 + d), (27.5, 11 + d)]
    parte(P, corrente(lam, 0.9, 0.6), 'ferro', 5.9, plano=True)
    px(P, [lam[t]], BRANCO, 5.95)
    parte(P, retangulo(22, 19 + d, 23, 22 + d), 'ouro', 6.2, plano=True)
    return render(P, 32, T)


# ================================================================ HOMEM-TUBARÃO (32)
def homem_tubarao(t):
    """Tubarão de pé (cabeça grande): focinho comprido, boca cheia de dentes, guelras que mexem, barbatana dorsal,
    barriga branca, cauda de tubarão, tanga de couro com corda, colar de dentes e uma cicatriz."""
    P, T = [], []
    d = RESP[t]
    ca = (0, 1, 0, -1)[t]
    parte(P, capsula(12, 23 + d, 7, 25 + d, 1.6), 'tubarao_t', 0.3)
    parte(P, poligono([(8, 25 + d), (3, 20 + d + ca), (5, 25 + d), (3, 30 - ca), (8, 26 + d)]), 'tubarao_t', 0.31)
    parte(P, capsula(13, 24, 12.5, 29, 1.7), 'tubarao_t', 0.5)
    parte(P, capsula(12, 30, 14, 30, 1.0), 'tubarao_t', 0.51)
    parte(P, capsula(17.5, 24, 18, 29, 1.9), 'tubarao', 3)
    parte(P, capsula(18, 30, 21, 30, 1.0), 'tubarao', 3.1)
    px(P, [(22, 30)], '#c7dcd0', 3.2)
    parte(P, capsula(13, 16 + d, 11, 21 + d, 1.3), 'tubarao_t', 0.6)
    px(P, [(10, 22 + d), (12, 22 + d)], '#c7dcd0', 0.65)
    tr = parte(P, elipse(15.5, 18.5 + d, 4.4, 4.6), 'tubarao', 2)
    T.append((tr, 'tubarao', pintas(2, 0.06, 0.0, d)))
    parte(P, elipse(17.8, 19.3 + d, 2.0, 3.6), 'branco', 2.1)
    parte(P, poligono([(10.5, 16 + d), (9, 9 + d), (14.5, 13 + d)]), 'tubarao', 1.9)       # barbatana dorsal
    parte(P, poligono([(11, 21.5 + d), (20, 21.5 + d), (20, 24 + d), (18, 25 + d), (16, 23.5 + d), (14, 26 + d), (11, 24 + d)]), 'couro', 2.5)
    px(P, [(x, 21 + d) for x in range(11, 21)], '#ab947a', 2.55)
    # cabeça grande de tubarão
    cab = elipse(16, 9 + d, 5.4, 4.8) | poligono([(17, 4.5 + d), (26.5, 8.5 + d), (25.5, 11 + d), (17, 12.5 + d)])
    parte(P, cab, 'tubarao', 4)
    T.append((cab, 'tubarao', pintas(6, 0.05, 0.0, d)))
    parte(P, poligono([(15, 11 + d), (25, 11 + d), (23.5, 13.4 + d), (15, 13.8 + d)]), 'branco', 4.1)
    px(P, [(x, 11 + d) for x in range(18, 26)], OUT, 4.2)                           # boca
    px(P, [(19, 12 + d), (21, 12 + d), (23, 12 + d)], BRANCO, 4.25)
    px(P, [(20, 10 + d), (22, 10 + d), (24, 10 + d)], BRANCO, 4.25)
    if t == 2:
        px(P, [(19, 7 + d), (20, 7 + d)], OUT, 4.3)
    else:
        px(P, [(19, 6 + d), (20, 6 + d), (19, 7 + d), (20, 7 + d)], OUT, 4.3)
        px(P, [(19, 6 + d)], BRANCO, 4.31)
    px(P, [(22, 7 + d), (23, 8 + d)], '#8fd3ff', 4.25)                             # cicatriz
    gu = (0, 1, 0, 1)[t]
    for x in (13, 14.5, 16):
        px(P, [(x, 10 + d + gu), (x, 11 + d + gu)], '#323353', 4.3)                 # guelras
    px(P, [(15, 15 + d), (17, 16 + d), (19, 16 + d)], BRANCO, 4.4)                 # colar de dentes
    px(P, [(16, 15 + d), (18, 16 + d)], '#966c6c', 4.4)
    parte(P, capsula(18, 16 + d, 20, 19 + d, 1.4), 'tubarao', 6)
    parte(P, capsula(20, 19 + d, 22, 21 + d, 1.3), 'tubarao', 6.1)
    parte(P, poligono([(19, 18 + d), (17, 21 + d), (20, 20 + d)]), 'tubarao_t', 5.9)
    px(P, [(23, 22 + d), (22, 23 + d), (24, 21 + d)], '#c7dcd0', 6.2)
    return render(P, 32, T)


# ================================================================ BARBA-LODO (32)
def barba_lodo(t):
    """Pirata fantasma (cabeça grande): cara verde-água, olho a brilhar e sobrolho carregado, chapéu de bicos com
    cracas e pena de alga, barba de algas em fios que abanam e pingam lodo, casaco de lodo com botões de ouro e
    uma lanterna fantasma que tremeluz."""
    P, T = [], []
    d = RESP[t]
    parte(P, capsula(13, 23, 12.5, 28, 1.6), 'lodo', 0.5)
    parte(P, retangulo(11, 28, 14, 30), 'chapeu', 0.55)
    parte(P, capsula(17, 23, 17.5, 28, 1.8), 'lodo', 3)
    parte(P, retangulo(16, 28, 20, 30), 'chapeu', 3.1)
    px(P, [(16, 28), (17, 28)], '#625565', 3.15)
    parte(P, capsula(13, 16 + d, 11, 21 + d, 1.3), 'lodo', 0.6)
    parte(P, elipse(11, 22 + d, 1.3, 1.2), 'fantasma_t', 0.61)
    cas = parte(P, poligono([(10.5, 15 + d), (19.5, 15 + d), (20.5, 25 + d), (17.5, 24 + d), (15, 26 + d), (10, 25 + d)]), 'lodo', 2)
    T.append((cas, 'lodo', pintas(3, 0.09, 0.03, d)))
    parte(P, retangulo(10, 21 + d, 20, 22 + d), 'couro', 2.2, plano=True)
    px(P, [(18, 21 + d), (18, 22 + d)], '#f9c22b', 2.25)
    # cabeça fantasma grande
    cab = parte(P, elipse(16.5, 9.8 + d, 5.2, 4.8), 'fantasma', 4)
    T.append((cab, 'fantasma', pintas(7, 0.05, 0.0, d)))
    cor = ('#cddf6c', '#fbff86', '#cddf6c', '#91db69')[t]
    px(P, [(18, 8 + d), (19, 8 + d), (18, 9 + d), (19, 9 + d)], OUT, 4.2)
    px(P, [(18, 8 + d), (19, 9 + d)], cor, 4.3)
    px(P, [(18, 8 + d)], BRANCO, 4.31) if t != 1 else None
    px(P, [(17, 7 + d), (18, 6 + d), (19, 6 + d), (20, 7 + d)], '#0b5e65', 4.25)    # sobrolho
    px(P, [(21, 10 + d), (21, 11 + d)], '#0b8a8f', 4.25)                             # nariz
    # barba de algas em fios (abanam) e bigode
    for i, x in enumerate(range(15, 22)):
        comp = 5 + (i * 3) % 5
        ox = round(math.sin(i * 1.3 + t * 1.57) * 1.0)
        fio = capsula(x, 12.5 + d, x + ox, 12.5 + comp + d, 0.7 if i % 2 else 0.9)
        parte(P, fio, 'alga_t' if i % 2 else 'alga', 4.5 + i * 0.01)
    parte(P, capsula(17, 12 + d, 22, 11.5 + d, 0.9), 'alga', 4.6)
    gy = 19 + t * 3
    px(P, [(19, gy + d), (19, gy + 1 + d)], '#91db69', 4.7)
    # chapéu de bicos com cracas e pena de alga
    parte(P, poligono([(11.5, 6 + d), (12.5, 1 + d), (16.5, 0 + d), (20.5, 1 + d), (21.5, 6 + d)]), 'chapeu', 5)
    parte(P, capsula(9.5, 5.6 + d, 22, 5.2 + d, 1.1), 'chapeu', 5.1)
    px(P, [(13, 2 + d), (14, 2 + d), (19, 2 + d)], '#c7dcd0', 5.2)
    px(P, [(13, 3 + d), (19, 3 + d)], '#625565', 5.2)
    pena = curva(12, 2 + d, -160, 7, 14, 5, 0.12, t * 1.6)
    parte(P, corrente(pena, 1.0, 0.6), 'alga', 5.3)
    # braço da frente com a lanterna fantasma
    parte(P, capsula(18, 16 + d, 20.5, 19 + d, 1.4), 'lodo', 6)
    parte(P, elipse(21.5, 19.5 + d, 1.3, 1.2), 'fantasma', 6.1)
    lx, ly = 22, 23 + d + (0, 0, 1, 0)[t]
    px(P, [(22, 20 + d), (22, 21 + d)], '#625565', 6.15)
    parte(P, retangulo(lx - 1, ly - 1, lx + 2, ly + 3), 'ferro_t', 6.2, plano=True)
    px(P, [(lx, ly), (lx + 1, ly), (lx, ly + 1), (lx + 1, ly + 1), (lx, ly + 2), (lx + 1, ly + 2)], '#91db69', 6.3)
    px(P, [(lx, ly + 1 - (t % 2)), (lx + 1, ly + 2 - (t % 2))], '#fbff86', 6.35)
    for i, (gx, gy) in enumerate(((-2, 5), (4, 1), (3, -2), (4, 5))):
        if (t + i) % 2 == 0:
            px(P, [(lx + gx, ly + gy)], '#cddf6c', 6.4)
    return render(P, 32, T)


# ================================================================ SEREIA SOMBRIA (32)
def sereia_sombria(t):
    """Sentada numa rocha da maré (cabeça grande): cabelo comprido roxo-escuro que ondula pelas costas, olho
    turquesa a brilhar, flor de coral no cabelo, top de concha, cauda de escamas verde-azuladas enrolada na rocha
    com a barbatana a abanar; de vez em quando sai uma nota do canto dela."""
    P, T = [], []
    d = RESP[t]
    roc = parte(P, elipse(15, 29.5, 10, 3.2) | elipse(11, 28, 5.5, 2.8), 'rocha', 0.2)
    T.append((roc, 'rocha', pintas(4, 0.1, 0.06)))
    px(P, [(7, 28), (7, 29), (8, 30), (22, 29), (23, 30)], '#239063', 0.3)
    px(P, [(6, 27), (23, 28)], '#1ebc73', 0.3)
    px(P, [(19, 28), (20, 28)], '#f68181', 0.3)
    fl = (0, -1, 0, 1)[t]
    cauda = corrente([(16, 22 + d), (14, 25.5), (10, 27), (6, 26), (4, 23 + fl * 0.5)], 3.0, 1.3)
    parte(P, cauda, 'cauda_ser', 1)
    T.append((cauda, 'cauda_ser', escamas(3, 2)))
    bar = poligono([(4.5, 23.5 + fl * 0.5), (1, 17 + fl), (3.5, 19 + fl), (5.5, 21)]) | poligono([(4, 23 + fl * 0.5), (7, 17 + fl), (7, 20 + fl), (5, 22)])
    parte(P, bar, 'barbatana', 1.1)
    px(P, [(2, 18 + fl), (6, 18 + fl)], BRANCO, 1.15)
    # cabelo de trás comprido
    on = (0, 1, 1, 0)[t]
    cab_t = corrente([(14, 7 + d), (11.5, 11 + d), (11 + on, 15 + d), (11.5, 19 + d), (10 + on, 22 + d)], 3.6, 1.6)
    parte(P, cab_t, 'cabelo_ser', 0.8)
    T.append((cab_t, 'cabelo_ser', riscas(3, 1, -0.4)))
    parte(P, capsula(15, 15 + d, 13, 20 + d, 1.0), 'pele_ser', 0.9)
    parte(P, capsula(16.5, 15 + d, 16, 21 + d, 2.7), 'pele_ser', 2, volume='cilindro_v')
    parte(P, elipse(18, 16.5 + d, 1.6, 1.2), 'roxo', 2.1)
    px(P, [(18, 16 + d)], '#eaaded', 2.15)
    px(P, [(14, 21 + d), (15, 22 + d), (17, 22 + d), (18, 21 + d)], '#0eaf9b', 2.2)
    # cabeça grande e cara à vista
    cab = parte(P, elipse(17, 9.5 + d, 4.8, 4.7), 'pele_ser', 4, luz=0.12)
    if t == 3:
        px(P, [(18, 10 + d), (19, 10 + d), (20, 10 + d)], OUT, 4.3)
    else:
        px(P, [(18 + i, 8 + j + d) for i in range(3) for j in range(2)], '#30e1b9', 4.3)
        px(P, [(20, 9 + d), (19, 9 + d)], '#0b5e65', 4.31)
        px(P, [(18, 8 + d)], BRANCO, 4.32)
        px(P, [(18, 7 + d), (19, 7 + d), (20, 7 + d)], OUT, 4.3)                    # pestanas
    px(P, [(20, 12 + d), (21, 12 + d)], '#831c5d', 4.3)                              # boca escura
    px(P, [(17, 11 + d)], '#f68181', 4.3)                                            # bochecha
    # cabelo da frente: calote por cima e madeixa atrás da orelha (a cara fica livre)
    calote = {p for p in elipse(16.5, 8.3 + d, 5.6, 4.6) if p[1] <= 6 + d or p[0] <= 15}
    parte(P, calote, 'cabelo_ser', 4.5)
    T.append((calote, 'cabelo_ser', riscas(3, 1, -0.5)))
    parte(P, corrente([(20, 5 + d), (22.5, 5.5 + d), (22.5 + on * 0.5, 8 + d)], 1.2, 0.8), 'cabelo_ser', 4.55)
    px(P, [(15, 4 + d), (16, 4 + d)], '#a884f3', 4.6)
    px(P, [(13, 7 + d), (14, 6 + d)], '#f68181', 4.62)
    px(P, [(13, 6 + d)], '#fdcbb0', 4.63)
    # braço da frente apoiado na rocha, com pulseira
    parte(P, capsula(18, 15.5 + d, 20.5, 21 + d, 1.1), 'pele_ser', 6)
    parte(P, capsula(20.5, 21 + d, 21.5, 25, 1.0), 'pele_ser', 6.1)
    px(P, [(20, 20 + d), (21, 20 + d)], '#30e1b9', 6.2)
    if t in (1, 2):
        nx, ny = 25 + t, 7 - t * 2
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
    ant = curva(14, 6 + f, -95, 13, 26, 7)
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
    for i, (x, y, ang, cur) in enumerate(((16, 30, 160, 12), (20, 32, 125, 16), (29, 32, 60, -16), (33, 30, 25, -12))):
        pts = curva(x, y + d, ang, 14, cur, 8, 0.09, fa + i)
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
    for (ex, ey, zz) in ((26, 21, 2.3), (31, 22, 2.4)):
        parte(P, elipse(ex, ey + d, 3.8, 3.6), 'polvo', zz)
    for (ex, ey, zz) in ((24, 20, 2.31), (30, 21, 2.41)):
        if t == 3:
            px(P, [(ex + i, ey + 1 + d) for i in range(4)], OUT, zz + 0.05)
        else:
            px(P, [(ex + i, ey + j + d) for i in range(4) for j in range(3)], '#f9c22b', zz + 0.05)
            px(P, [(ex + i, ey + 1 + d) for i in range(4)], OUT, zz + 0.06)
            px(P, [(ex + i, ey + 2 + d) for i in range(4)], '#f79617', zz + 0.055)
            px(P, [(ex, ey + d)], BRANCO, zz + 0.07)
        px(P, [(ex + i, ey - 1 + d) for i in range(4)], '#45293f', zz + 0.05)      # pálpebra
    # tentáculos da frente (com ventosas)
    for i, (x, y, ang, cur, comp) in enumerate(((19, 32, 125, 17, 17), (23, 33, 100, 22, 14), (28, 33, 80, -22, 14), (32, 31, 55, -17, 17))):
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
    return render(P, 48, T, desloc=(0, 10))


# ================================================================ SERPENTES (Serpente Marinha Jovem 64, Leviatã 128)
def _normal(pts, i):
    a = pts[max(0, i - 1)]
    b = pts[min(len(pts) - 1, i + 1)]
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy) or 1
    return dy / n, -dx / n


def _linha(x1, y1, x2, y2):
    n = int(max(abs(x2 - x1), abs(y2 - y1))) + 1
    return [(x1 + (x2 - x1) * i / n, y1 + (y2 - y1) * i / n) for i in range(n + 1)]


def crista(P, pts, comp, z, rampa='barbatana', raio='#0b5e65', lado=1, ondula=0.0, fase=0.0, de=0, ate=None):
    """Barbatana em crista ao longo de um corpo: espinhos (raios escuros) com membrana recortada entre eles."""
    ate = len(pts) if ate is None else ate
    tips = []
    for i in range(de, ate):
        nx, ny = _normal(pts, i)
        L = comp(i) if callable(comp) else comp
        L *= 1 + ondula * math.sin(fase + i * 1.3)
        tips.append((pts[i], (pts[i][0] + nx * L * lado, pts[i][1] + ny * L * lado), L))
    mem = set()
    for j in range(len(tips) - 1):
        (p0, t0, L0), (p1, t1, L1) = tips[j], tips[j + 1]
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        nx, ny = (t0[0] + t1[0]) / 2 - mx, (t0[1] + t1[1]) / 2 - my
        meio = (mx + nx * 0.72, my + ny * 0.72)
        mem |= poligono([p0, t0, meio, t1, p1])
    parte(P, mem, rampa, z)
    for (p0, t0, L0) in tips:
        px(P, _linha(p0[0], p0[1], t0[0], t0[1])[1:], raio, z + 0.01)
    return mem


def serpente_marinha_jovem(t):
    """Serpente azul a sair da água: um arco do corpo atrás e o pescoço a subir, escamas, barriga creme às
    riscas, crista de barbatana turquesa com espinhos, leques nas bochechas, olho amarelo de pupila em fenda,
    dentes, e anéis de água à volta. O pescoço baloiça, a crista ondula e pisca o olho."""
    P, T = [], []
    S = 64
    mar = 58
    hx, hy = (0, 1, 1, 0)[t], (0, 0, 1, 1)[t]
    # anéis de água (atrás e à frente de cada sítio onde o corpo entra na água)
    def anel(x, larg, z, fase):
        r = larg + (fase % 2)
        m = elipse(x, mar + 1, r, 2.2) - elipse(x, mar + 1, r - 1.5, 1.2)
        parte(P, m, 'agua', z, plano=True)
        px(P, [(x - r + 1, mar), (x + r - 2, mar + 2)], BRANCO, z + 0.01)
    # arco de trás (o fim do corpo)
    arco = [(5, mar + 2), (7, 50), (12, 44), (18, 44), (23, 49), (25, mar + 2)]
    m = parte(P, corrente(arco, 4.2, 4.0), 'serpente_t', 1)
    T.append((m, 'serpente_t', escamas(4, 3)))
    crista(P, arco, 8.5, 0.9, rampa='agua', ondula=0.15, fase=t * 1.57, de=1, ate=5)
    anel(6, 6, 0.5, t)
    anel(24, 6, 0.5, t + 1)
    # pescoço a subir (baloiça)
    base = [(35, mar + 3), (35.5, 51), (38.5, 44), (39.5, 37), (42, 30), (46, 25), (49, 22)]
    pesc = [(x + hx * i / 6, y + hy * i / 6) for i, (x, y) in enumerate(base)]
    crista(P, pesc, lambda i: 6.0 - i * 0.27 + 5.0, 1.8, ondula=0.2, fase=t * 1.57, de=1)
    corpo = corrente(pesc, 6.0, 4.4)
    parte(P, corpo, 'serpente', 2)
    T.append((corpo, 'serpente', escamas(4, 3)))
    # barriga creme (do lado da frente)
    bar = corrente([(x + 3.6 - i * 0.25, y + 1.2) for i, (x, y) in enumerate(pesc[:-1])], 2.0, 1.5)
    parte(P, bar, 'creme', 2.1)
    T.append((bar, 'creme', riscas(3, 1, 1.4)))
    anel(37, 8, 3, t)
    # cabeça
    cx, cy = 49 + hx, 18 + hy
    leque = poligono([(cx - 3, cy - 1), (cx - 9, cy - 8), (cx - 6, cy - 2), (cx - 10, cy - 2), (cx - 6, cy + 1), (cx - 9, cy + 5), (cx - 3, cy + 3)])
    parte(P, leque, 'barbatana', 2.5)
    px(P, _linha(cx - 3, cy, cx - 8, cy - 7) + _linha(cx - 3, cy + 1, cx - 9, cy - 2) + _linha(cx - 3, cy + 2, cx - 8, cy + 4), '#0b5e65', 2.51)
    cab = elipse(cx, cy, 7.0, 5.4) | poligono([(cx + 2, cy - 4.5), (cx + 13, cy - 1.5), (cx + 13.5, cy + 2), (cx + 2, cy + 3)])
    parte(P, cab, 'serpente', 3)
    T.append((cab, 'serpente', pintas(5, 0.05, 0.03)))
    maxi = poligono([(cx - 1, cy + 2), (cx + 12, cy + 2.5), (cx + 11, cy + 5), (cx, cy + 7)])
    parte(P, maxi, 'creme', 2.9)
    px(P, [(x, cy + 2) for x in range(cx + 1, cx + 13)], OUT, 3.1)                 # boca
    px(P, [(cx + 4, cy + 3), (cx + 7, cy + 3), (cx + 10, cy + 3), (cx + 6, cy + 1), (cx + 9, cy + 1)], BRANCO, 3.2)  # dentes
    px(P, [(cx + 12, cy - 1)], OUT, 3.1)                                           # narina
    # olho amarelo de fenda + sobrolho
    if t == 3:
        px(P, [(cx + 1 + i, cy - 1) for i in range(3)], OUT, 3.3)
    else:
        px(P, [(cx + 1 + i, cy - 2 + j) for i in range(3) for j in range(2)], '#f9c22b', 3.3)
        px(P, [(cx + 2, cy - 2), (cx + 2, cy - 1)], OUT, 3.31)
        px(P, [(cx + 1, cy - 2)], BRANCO, 3.32)
    parte(P, capsula(cx - 1, cy - 4, cx + 4, cy - 3.5, 1.1), 'serpente', 3.4)
    # chifrinhos para trás
    parte(P, poligono([(cx - 3, cy - 3), (cx - 7, cy - 7), (cx - 2, cy - 5)]), 'creme', 2.8)
    # gotas a cair do queixo
    px(P, [(cx + 6, cy + 7 + t * 2)], '#8ff8e2', 3.5)
    return render(P, S, T)


def leviata(t):
    """Leviatã: serpente colossal de escamas azul-escuras a sair do mar em dois arcos e um pescoço enorme,
    barbatanas como velas (turquesa, com raios), chifres para trás, leques nas bochechas, bigodes compridos que
    ondulam, olhos tristes que brilham azul-claro (com uma lágrima de luz), barriga creme, cracas e cicatrizes,
    espuma e anéis de água. O pescoço baloiça devagar, as velas ondulam e o olho pulsa."""
    P, T = [], []
    S = 128
    mar = 116
    hx, hy = (0, 1, 2, 1)[t], (0, 1, 1, 0)[t]

    def anel(x, larg, z, fase):
        r = larg + (fase % 2) * 2
        m = elipse(x, mar + 2, r, 4) - elipse(x, mar + 2, r - 2.5, 2.2)
        parte(P, m, 'agua', z, plano=True)
        px(P, [(x - r + 2, mar), (x - r + 3, mar), (x + r - 3, mar + 4), (x + 2, mar - 1)], BRANCO, z + 0.01)

    # arcos do corpo (o mais longe primeiro)
    arco1 = [(4, mar + 4), (6, 100), (13, 90), (23, 88), (31, 94), (34, mar + 4)]
    arco2 = [(36, mar + 4), (39, 94), (48, 82), (60, 80), (69, 88), (71, mar + 4)]
    for j, (arco, r, z) in enumerate(((arco1, 6.5, 0.6), (arco2, 8.5, 1.0))):
        crista(P, arco, r + 9, z - 0.1, rampa='barbatana', ondula=0.2, fase=t * 1.57 + j, de=1, ate=5)
        m = parte(P, corrente(arco, r, r), 'leviata_t', z)
        T.append((m, 'leviata_t', escamas(6, 4, arco=True)))
        anel(arco[0][0] + 2, r + 3, z - 0.05, t + j)
        anel(arco[-1][0] - 1, r + 3, z + 0.05, t + j + 1)
    # pescoço enorme
    base = [(80, mar + 6), (78, 104), (80, 92), (86, 80), (88, 69), (86, 59), (86, 50)]
    pesc = [(x + hx * i / 6, y + hy * i / 6) for i, (x, y) in enumerate(base)]
    crista(P, pesc, lambda i: 23 - i * 1.2, 1.8, rampa='barbatana', ondula=0.18, fase=t * 1.57 + 2, de=1)
    corpo = corrente(pesc, 12, 9.5)
    parte(P, corpo, 'leviata', 2)
    T.append((corpo, 'leviata', escamas(6, 4, arco=True)))
    bar = corrente([(x + 8 - i * 0.5, y + 2) for i, (x, y) in enumerate(pesc[:-1])], 4.0, 3.2)
    parte(P, bar, 'barriga_lev', 2.1)
    T.append((bar, 'barriga_lev', riscas(4, 1, 1.4)))
    # cracas e cicatrizes no pescoço
    for (bx, by) in ((76, 96), (79, 82), (74, 102)):
        parte(P, elipse(bx + hx * 0.3, by, 1.8, 1.5), 'osso_t', 2.2)
        px(P, [(bx + hx * 0.3, by - 0.5)], OUT, 2.25)
    px(P, _linha(83, 70, 87, 64), '#8fd3ff', 2.2)
    px(P, _linha(84, 72, 88, 66), '#323353', 2.2)
    anel(80, 16, 3, t)
    # cabeça grande
    cx, cy = 93 + hx, 36 + hy
    # leques das bochechas (com raios)
    for (a, b, c, d2) in (((cx - 8, cy - 4), (cx - 26, cy - 18), (cx - 20, cy - 6), (cx - 30, cy - 4)),
                          ((cx - 8, cy + 4), (cx - 30, cy + 4), (cx - 22, cy + 10), (cx - 26, cy + 20))):
        leq = poligono([a, b, c, d2, (a[0], a[1] + 6)])
        parte(P, leq, 'barbatana', 2.5)
        for q in (b, c, d2):
            px(P, _linha(a[0], a[1] + 2, q[0], q[1]), '#0b5e65', 2.51)
    # chifres compridos para trás
    for (dx, dy2, z, rr) in ((0, 2, 2.6, 'osso_t'), (5, 0, 3.6, 'barriga_lev')):
        pts = curva(cx - 4 + dx, cy - 8 + dy2, -150, 26, 6, 6)
        parte(P, corrente(pts, 3.0, 0.8), rr, z)
    cab = elipse(cx, cy, 16, 12) | poligono([(cx + 4, cy - 11), (cx + 30, cy - 4), (cx + 31, cy + 3), (cx + 4, cy + 8)])
    parte(P, cab, 'leviata', 3)
    T.append((cab, 'leviata', escamas(6, 4, arco=True)))
    maxi = poligono([(cx - 4, cy + 5), (cx + 29, cy + 4), (cx + 26, cy + 10), (cx + 2, cy + 16)])
    parte(P, maxi, 'barriga_lev', 2.9)
    T.append((maxi, 'barriga_lev', riscas(4, 1, -0.5)))
    px(P, [(x, cy + 4 + (1 if x < cx + 8 else 0)) for x in range(cx + 0, cx + 30)], OUT, 3.1)
    px(P, [(x, cy + 6 - (1 if x < cx + 8 else 0)) for x in range(cx + 7, cx + 28, 4)] + [(x, cy + 3) for x in range(cx + 9, cx + 28, 4)], BRANCO, 3.2)
    px(P, [(cx + 27, cy - 3), (cx + 28, cy - 3)], OUT, 3.1)                          # narina
    # placas na testa
    for i in range(3):
        parte(P, elipse(cx - 6 + i * 7, cy - 9 + i * 1.5, 3.8, 2.4), 'leviata', 3.3 + i * 0.01)
    # olho triste e luminoso (amêndoa, com o canto de fora a descer)
    ex, ey = cx + 6, cy - 3
    pul = ('#8fd3ff', '#ffffff', '#8fd3ff', '#4d9be6')[t]
    forma = [(0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 1), (6, 2)]
    contorno = set()
    for (i, j0) in forma:
        for j in range(j0, 4):
            contorno |= {(ex + i + a2, ey + j + b2) for a2 in (-1, 0, 1) for b2 in (-1, 0, 1)}
    px(P, contorno, OUT, 3.4)
    olhop = [(ex + i, ey + j) for (i, j0) in forma for j in range(j0, 4)]
    px(P, olhop, '#4d9be6', 3.41)
    px(P, [(x, y) for (x, y) in olhop if ex + 1 <= x <= ex + 4 and y >= ey + 1], pul, 3.42)
    px(P, [(ex + 2, ey + 2), (ex + 3, ey + 2)], '#323353', 3.425)
    px(P, [(ex + 1, ey + 1)], BRANCO, 3.43)
    parte(P, capsula(ex - 4, ey - 6, ex + 8, ey - 2, 1.8), 'leviata', 3.5)          # sobrolho caído (triste)
    px(P, [(ex + 5, ey + 5 + t % 2), (ex + 5, ey + 6 + t % 2)], '#8fd3ff', 3.45)   # lágrima de luz
    if t < 3:
        px(P, [(ex + 5, ey + 9 + t * 2)], '#30e1b9', 3.45)
    # bigodes compridos a ondular
    for j, (sx, sy) in enumerate(((cx + 24, cy + 1), (cx + 16, cy + 12))):
        pts = [(sx, sy)] + [(sx + 2 + i * 1.5 + math.sin(t * 1.57 + i * 0.8 + j) * 1.8, sy + i * 4.5) for i in range(1, 9)]
        parte(P, corrente(pts, 1.6, 0.7), 'barbatana', 3.6 + j * 0.01)
    # espuma a saltar
    for i, (fx, fy) in enumerate(((60, 110), (96, 112), (104, 109), (20, 111), (50, 113))):
        if (i + t) % 2:
            px(P, [(fx, fy), (fx + 1, fy - 1)], BRANCO, 4)
        else:
            px(P, [(fx, fy - 2)], '#8ff8e2', 4)
    return render(P, S, T)


# ================================================================ TARTARUGA-MARINHA ANCIÃ (64)
def _palmeira(P, x, y, alt, inclina, t, z, semente):
    """Palmeira: tronco curvo aos gomos e uma copa de folhas que caem e abanam, com cocos."""
    pts = [(x + inclina * (i / 6) ** 1.6, y - alt * i / 6) for i in range(7)]
    tr = corrente(pts, 1.8, 1.3)
    parte(P, tr, 'tronco', z, volume='cilindro_v')
    for i in range(1, 6):
        px(P, [(pts[i][0] - 1, pts[i][1]), (pts[i][0], pts[i][1])], '#4c3e24', z + 0.01)
    tx, ty = pts[-1]
    a = math.sin(t * 1.57 + semente) * 0.12
    for j, ang in enumerate((-170, -135, -100, -60, -20, 15)):
        fol = curva(tx, ty, ang, 11 if j in (1, 4) else 9, 18 if ang > -90 else -18, 6, a, 0)
        m = corrente(fol, 1.7, 0.6)
        parte(P, m, 'alga' if j % 2 else 'alga_t', z + 0.1 + j * 0.01)
        for q in fol[2::2]:
            px(P, [(q[0], q[1] + 2)], '#165a4c', z + 0.09)          # folíolos a pender
    parte(P, elipse(tx + 1, ty + 2, 1.5, 1.5), 'tronco', z + 0.2)
    parte(P, elipse(tx - 2, ty + 2.5, 1.4, 1.4), 'tronco', z + 0.19)


def tartaruga_marinha_ancia(t):
    """Tartaruga enorme e velha com uma ilhota nas costas: carapaça com placas, cracas e algas penduradas,
    monte de areia com duas palmeiras, uma concha e uma pedra; cabeça de pálpebras pesadas, bico, rugas e
    escamas; barbatanas grandes. As palmeiras abanam, as algas baloiçam, a cabeça sobe e desce e pisca."""
    P, T = [], []
    d = RESP[t]
    # barbatanas do lado de lá
    parte(P, capsula(16, 54, 7, 61, 3), 'tartaruga_t', 0.2)
    parte(P, capsula(44, 54, 51, 61, 3.4), 'tartaruga_t', 0.2)
    # carapaça
    casco = {p for p in elipse(30, 47, 21, 12) if p[1] <= 53}
    parte(P, casco, 'casco', 2)
    T.append((casco, 'casco', pintas(21, 0.05, 0.03)))
    # placas (linhas escuras) e borda
    for x0 in (21, 30, 39):
        px(P, [(x0 + (y - 44) * (x0 - 30) * 0.04, y) for y in range(37, 51)], '#313638', 2.05)
    px(P, [(x, 44 + abs(x - 30) * 0.05) for x in range(12, 49)], '#313638', 2.05)
    borda = {p for p in elipse(30, 51, 21.5, 4) if p[1] >= 51}
    parte(P, borda, 'casco', 2.1)
    px(P, [(x, y) for (x, y) in borda if x % 4 == 0], '#313638', 2.12)
    parte(P, elipse(30, 55, 18, 2.5), 'creme', 1.9)                                 # plastrão
    # cracas
    for (bx, by) in ((15, 47), (19, 50), (42, 48)):
        parte(P, elipse(bx, by, 1.6, 1.3), 'osso_t', 2.2)
        px(P, [(bx, by - 0.5)], OUT, 2.25)
    # algas penduradas da borda (baloiçam)
    for i, x in enumerate((12, 17, 24, 36, 45)):
        pts = [(x, 52)] + [(x + math.sin(t * 1.57 + i + j) * 0.8, 52 + j * 2) for j in range(1, 3 + i % 2)]
        parte(P, corrente(pts, 0.8, 0.6), 'alga', 2.3 + i * 0.01)
    # a ilhota: monte de areia, pedra, concha e palmeiras
    ilha = {p for p in elipse(29, 37, 15, 5) if p[1] <= 39}
    parte(P, ilha, 'areia', 3)
    T.append((ilha, 'areia', pintas(22, 0.06, 0.04)))
    parte(P, elipse(38, 35, 3, 2.2), 'rocha', 3.1)
    parte(P, elipse(20, 36.5, 2, 1.4), 'coral', 3.1)
    px(P, [(19, 36), (21, 36)], '#fdcbb0', 3.15)
    _palmeira(P, 26, 35, 22, -8, t, 3.3, 0)
    _palmeira(P, 33, 35, 14, 7, t, 3.5, 2)
    # pescoço e cabeça
    hy = d
    parte(P, capsula(46, 49, 54, 45 + hy, 4.2), 'tartaruga', 4, volume='cilindro_h')
    cab = parte(P, elipse(57, 42 + hy, 6, 4.6), 'tartaruga', 4.5)
    T.append((cab, 'tartaruga', escamas(3, 2)))
    parte(P, poligono([(59, 42 + hy), (64, 42 + hy), (63, 45 + hy), (59, 47 + hy)]), 'creme', 4.4)   # bico
    px(P, [(60, 44 + hy), (61, 44 + hy), (62, 44 + hy), (63, 43 + hy)], OUT, 4.6)
    if t == 3:
        px(P, [(57, 40 + hy), (58, 40 + hy), (59, 40 + hy)], OUT, 4.7)
    else:
        px(P, [(57, 40 + hy), (58, 40 + hy), (57, 41 + hy), (58, 41 + hy)], OUT, 4.7)
        px(P, [(57, 40 + hy)], BRANCO, 4.71)
    px(P, [(56, 39 + hy), (57, 39 + hy), (58, 39 + hy), (59, 39 + hy)], '#165a4c', 4.72)   # pálpebra pesada
    px(P, [(55, 43 + hy), (56, 44 + hy), (54, 45 + hy)], '#165a4c', 4.72)                 # rugas
    px(P, [(50, 45 + hy), (51, 47 + hy), (49, 48 + hy)], '#91db69', 4.1)
    # barbatana da frente (grande)
    bf = corrente([(43, 52), (49, 57), (56, 60), (60, 61)], 3.6, 1.8)
    parte(P, bf, 'tartaruga', 5)
    T.append((bf, 'tartaruga', escamas(3, 2)))
    return render(P, 64, T)


# ================================================================ GAIVOTA GIGANTE LADRA (48)
def gaivota_gigante_ladra(t):
    """Gaivota enorme a pairar: lenço de pirata vermelho às bolinhas com o nó a esvoaçar, olho amarelo mau com
    sobrolho, bico amarelo com a mancha vermelha, asas cinzentas de pontas pretas com pintas brancas (batem nos
    4 quadros) e uma poção roubada agarrada nas patas."""
    P, T = [], []
    pontas = ((-4, -21), (-18, -11), (-13, 9), (-18, -11))
    dy = (1, 0, -1, 0)[t]
    cx, cy = 22, 21 + dy

    def asa(z, rampa, dx, esc):
        sx, sy = cx - 1 + dx, cy - 3
        tx, ty = sx + pontas[t][0] * esc, sy + pontas[t][1] * esc
        vx, vy = tx - sx, ty - sy
        n = math.hypot(vx, vy) or 1
        nx, ny = -vy / n, vx / n
        if nx < 0:
            nx, ny = -nx, -ny
        lead = (sx + vx * 0.5 + nx * 4, sy + vy * 0.5 + ny * 4)
        trail = (sx + vx * 0.65 - nx * 5, sy + vy * 0.65 - ny * 5)
        m = poligono([(sx + 5, sy), lead, (tx, ty), trail, (sx - 5, sy + 2)])
        parte(P, m, rampa, z)
        T.append((m, rampa, riscas(3, 1, -0.8, dy)))
        pp = {p for p in m if math.hypot(p[0] - tx, p[1] - ty) < 6}
        px(P, pp, '#2e222f' if z > 3 else '#3e3546', z + 0.01)
        px(P, [(tx + vx / n * -3 + nx, ty + vy / n * -3 + ny)], BRANCO, z + 0.02)
        return m
    asa(0.5, 'asa_t', 3, 0.85)
    # cauda
    parte(P, poligono([(cx - 7, cy), (cx - 16, cy - 1), (cx - 15, cy + 4), (cx - 7, cy + 4)]), 'gaivota', 1)
    px(P, [(cx - 15, cy), (cx - 15, cy + 1), (cx - 15, cy + 2), (cx - 14, cy + 3)], '#3e3546', 1.1)
    # patas com a poção roubada
    parte(P, capsula(cx + 1, cy + 5, cx + 1, cy + 10, 0.8), 'pata', 1.2)
    parte(P, capsula(cx + 4, cy + 5, cx + 4, cy + 10, 0.8), 'pata', 1.2)
    bx, by = cx + 2.5, cy + 13
    parte(P, elipse(bx, by, 3, 3), ['#6e2727', '#b33831', '#e83b3b', '#f68181', '#ffffff'], 1.5)
    parte(P, retangulo(int(bx) - 1, int(by) - 5, int(bx), int(by) - 3), 'madeira', 1.6, plano=True)
    px(P, [(bx - 1, by - 1)], BRANCO, 1.7)
    px(P, [(cx, cy + 10), (cx + 2, cy + 10), (cx + 3, cy + 10), (cx + 5, cy + 10)], '#cd683d', 1.8)
    # corpo
    corpo = parte(P, elipse(cx, cy, 9.5, 6.2), 'gaivota', 2)
    parte(P, {p for p in elipse(cx - 1, cy - 2, 8, 4) if p[1] < cy - 2}, 'asa', 2.1)  # dorso cinzento
    # cabeça
    hx, hy = cx + 9, cy - 7
    parte(P, elipse(hx, hy, 5.2, 4.8), 'gaivota', 3)
    bico = poligono([(hx + 3.5, hy - 0.5), (hx + 11, hy + 0.5), (hx + 11, hy + 2.5), (hx + 9.5, hy + 3.5), (hx + 3.5, hy + 3)])
    parte(P, bico, 'bico', 3.1)
    px(P, [(hx + 4, hy + 1.5), (hx + 5, hy + 1.5), (hx + 6, hy + 1.5), (hx + 7, hy + 1.5), (hx + 8, hy + 1.5)], '#9e4539', 3.15)
    px(P, [(hx + 9, hy + 2.5)], '#e83b3b', 3.2)
    px(P, [(hx + 10, hy + 1.5)], '#9e4539', 3.2)
    if t == 2:
        px(P, [(hx + 1, hy), (hx + 2, hy)], OUT, 3.3)
    else:
        px(P, [(hx + 1, hy - 1), (hx + 2, hy - 1), (hx + 1, hy), (hx + 2, hy)], '#f9c22b', 3.3)
        px(P, [(hx + 2, hy), (hx + 2, hy - 1)], OUT, 3.31)
        px(P, [(hx + 1, hy - 1)], BRANCO, 3.32)
    px(P, [(hx, hy - 3), (hx + 1, hy - 2), (hx + 2, hy - 2), (hx + 3, hy - 1)], OUT, 3.4)   # sobrolho mau
    # lenço de pirata
    lenco = {p for p in elipse(hx - 0.5, hy - 0.5, 5.8, 5.4) if p[1] <= hy - 3 or (p[0] <= hx - 3 and p[1] <= hy)}
    parte(P, lenco, 'lenco', 3.5)
    px(P, [(hx - 3, hy - 4), (hx + 1, hy - 5), (hx - 1, hy - 2), (hx + 3, hy - 4)], BRANCO, 3.55)
    fl = (0, 1, 2, 1)[t]
    for (a, b) in (((hx - 6, hy - 2), (hx - 11, hy - 4 + fl)), ((hx - 6, hy - 1), (hx - 10, hy + 2 + fl))):
        parte(P, capsula(a[0], a[1], b[0], b[1], 1.0), 'lenco', 3.45)
    parte(P, elipse(hx - 6, hy - 1.5, 1.5, 1.5), 'lenco', 3.6)
    # asa da frente
    asa(4, 'asa', 0, 1.0)
    return render(P, 48, T)


# ================================================================ PEIXE-LEÃO REI (48)
def peixe_leao_rei(t):
    """Peixe-leão: corpo às riscas vermelho-acastanhadas e creme, uma juba de espinhos compridos às riscas na
    dorsal, barbatanas do peito em leque (raios às riscas), cauda transparente com pintas, olho vermelho com a
    risca a passar, tentáculos por cima do olho, lábios grossos e uma coroinha. Os espinhos e os leques ondulam."""
    P, T = [], []
    f = FLUT[t]
    cx, cy = 22, 21 + f
    on = t * 1.57
    # espinhos da dorsal (juba): raio às riscas + membrana
    mem = set()
    raios = []
    for i in range(9):
        bx = cx - 10 + i * 2.3
        by = cy - 6.5 + abs(i - 4) * 0.4
        ang = math.radians(-120 + i * 7 + math.sin(on + i * 0.7) * 4)
        L = 14 - abs(i - 3) * 1.0
        tx, ty = bx + math.cos(ang) * L, by + math.sin(ang) * L
        raios.append(((bx, by), (tx, ty)))
        if i:
            (pb, pt) = raios[i - 1]
            mem |= poligono([pb, (pt[0] * 0.55 + pb[0] * 0.45, pt[1] * 0.55 + pb[1] * 0.45), (tx * 0.55 + bx * 0.45, ty * 0.55 + by * 0.45), (bx, by)])
    parte(P, mem, 'membrana', 0.5, plano=True)
    for (b, e) in raios:
        lin = _linha(b[0], b[1], e[0], e[1])
        for j, q in enumerate(lin):
            px(P, [q], '#fdcbb0' if (j // 2) % 2 else '#b33831', 0.6)
        px(P, [lin[-1]], BRANCO, 0.61)
    # cauda transparente com pintas
    ca = (0, 1, 0, -1)[t]
    cauda = poligono([(cx - 11, cy), (cx - 20, cy - 7 + ca), (cx - 22, cy + ca), (cx - 20, cy + 7 + ca)])
    parte(P, cauda, ['#9e4539', '#cd683d', '#f57d4a', '#fca790', '#fdcbb0'], 0.7, plano=True)
    px(P, [(cx - 17, cy - 3 + ca), (cx - 18, cy + 1 + ca), (cx - 16, cy + 4 + ca), (cx - 14, cy - 1)], '#6e2727', 0.75)
    # corpo às riscas
    corpo = elipse(cx, cy, 12.5, 8)
    parte(P, corpo, 'leao', 2, luz=0.12)
    listras = {(x, y) for (x, y) in corpo if (x + y * 0.25) % 6 < 2 and x < cx + 6}
    parte(P, listras, ['#966c6c', '#e6904e', '#fca790', '#fdcbb0', '#ffffff'], 2.01, separar=False)
    # cabeça: lábios, olho, tentáculos, coroa
    parte(P, poligono([(cx + 10, cy + 1), (cx + 15.5, cy + 1.5), (cx + 15, cy + 4.5), (cx + 10, cy + 4.5)]), 'leao', 2.2)
    px(P, [(cx + 11, cy + 3), (cx + 12, cy + 3), (cx + 13, cy + 3), (cx + 14, cy + 3)], OUT, 2.25)
    ex, ey = cx + 6, cy - 4
    px(P, [(ex - 1 + i, ey - 1 + j) for i in range(6) for j in range(6) if (i, j) not in ((0, 0), (5, 0), (0, 5), (5, 5))], '#fdcbb0', 2.3)
    px(P, [(ex + 1, ey + 5), (ex + 2, ey + 6), (ex + 2, ey + 7)], '#6e2727', 2.3)   # risca a sair do olho
    if t == 3:
        px(P, [(ex + i, ey + 2) for i in range(4)], OUT, 2.4)
    else:
        px(P, [(ex + i, ey + j) for i in range(4) for j in range(4)], '#e83b3b', 2.4)
        px(P, [(ex + 1, ey + 1), (ex + 2, ey + 1), (ex + 1, ey + 2), (ex + 2, ey + 2), (ex + 3, ey + 2), (ex + 2, ey + 3)], OUT, 2.41)
        px(P, [(ex, ey), (ex + 1, ey)], BRANCO, 2.42)
    parte(P, capsula(ex + 1, ey - 1, ex + 3, ey - 5, 0.7), 'membrana', 2.45)
    parte(P, poligono([(cx + 5, cy - 7), (cx + 5, cy - 11), (cx + 7, cy - 9), (cx + 8, cy - 12), (cx + 9, cy - 9), (cx + 11, cy - 11), (cx + 11, cy - 6)]), 'ouro', 2.5, plano=True)
    px(P, [(cx + 8, cy - 9)], '#4d9be6', 2.55)
    # barbatanas do peito em leque (raios às riscas que ondulam)
    lq = set()
    pontas = []
    for i in range(6):
        ang = math.radians(100 + i * 13 + math.sin(on + i) * 4)
        L = 16 - i * 0.6
        pontas.append((cx - 1 + math.cos(ang) * L, cy + 4 + math.sin(ang) * L))
    lq = poligono([(cx, cy + 3)] + pontas + [(cx - 1, cy + 5)])
    parte(P, lq, ['#6e2727', '#9e4539', '#cd683d', '#f57d4a', '#fca790'], 1.5, plano=True)
    for q in pontas:
        lin = _linha(cx - 1, cy + 4, q[0], q[1])
        for j, r in enumerate(lin):
            px(P, [r], '#fdcbb0' if (j // 3) % 2 else '#7a3045', 1.51)
    brilhos(P, [(cx + 12, cy - 13), (cx + 3, cy - 10)], t, 4)
    return render(P, 48, T)


# ================================================================ TAMBORIL ABISSAL (64)
def tamboril_abissal(t):
    """Peixe-diabo enorme do abismo: bocarra aberta com duas filas de dentes de agulha que se cruzam, olho
    pequeno e pálido, antena comprida com a isca turquesa a pulsar (halo), verrugas, franjas de pele por baixo
    do queixo, barbatanas esfarrapadas e pintas luminosas."""
    P, T = [], []
    f = FLUT[t]
    cx, cy = 26, 25 + f
    ca = (0, 1, 0, -1)[t]
    # cauda e dorsal esfarrapadas
    parte(P, poligono([(cx - 17, cy), (cx - 25, cy - 9 + ca), (cx - 23, cy - 3), (cx - 26, cy + 1), (cx - 23, cy + 4), (cx - 25, cy + 10 - ca)]), 'abissal_t', 0.5)
    parte(P, poligono([(cx - 10, cy - 12), (cx - 8, cy - 18), (cx - 5, cy - 14), (cx - 2, cy - 19), (cx + 1, cy - 14), (cx + 3, cy - 13)]), 'abissal_t', 0.6)
    # corpo
    corpo = elipse(cx, cy, 20, 15)
    parte(P, corpo, 'abissal', 2)
    T.append((corpo, 'abissal', pintas(31, 0.06, 0.04, f)))
    # bocarra
    boca = poligono([(cx + 4, cy + 2), (cx + 22, cy - 6), (cx + 25, cy + 10), (cx + 8, cy + 8)])
    px(P, boca, '#45293f', 2.4)
    px(P, elipse(cx + 14, cy + 4, 5, 3), '#6e2727', 2.45)
    maxila = poligono([(cx + 6, cy + 7), (cx + 26, cy + 9), (cx + 24, cy + 14), (cx + 10, cy + 15)])
    parte(P, maxila, 'abissal', 2.6)
    # dentes de agulha (de cima para baixo e de baixo para cima)
    for i, x in enumerate(range(cx + 9, cx + 24, 3)):
        yt = cy - 3.5 - (x - cx - 9) * 0.25 + 4
        px(P, [(x, yt + j) for j in range(3 + i % 2)], '#c7dcd0', 2.7)
        px(P, [(x, yt)], BRANCO, 2.71)
        xb = x + 1
        px(P, [(xb, cy + 8 - j) for j in range(3 + (i + 1) % 2)], '#c7dcd0', 2.7)
    # franjas de pele por baixo
    for i, x in enumerate(range(cx - 4, cx + 22, 4)):
        L = 3 + (i % 2) * 2
        pts = [(x, cy + 13 - abs(x - cx - 8) * 0.15), (x + math.sin(t * 1.57 + i) * 0.8, cy + 13 + L)]
        parte(P, corrente(pts, 0.9, 0.6), 'abissal_t', 2.8)
    # olho pequeno e pálido
    ex, ey = cx + 9, cy - 9
    parte(P, elipse(ex + 1, ey + 1, 3, 2.6), 'abissal', 2.9)
    if t == 3:
        px(P, [(ex, ey + 1), (ex + 1, ey + 1), (ex + 2, ey + 1)], OUT, 3)
    else:
        olho(P, ex, ey, '#8ff8e2', 3, tam=1, pupila=OUT)
    # verrugas
    for (wx, wy) in ((-12, -6), (-6, -10), (-14, 4), (-2, -4), (4, -13)):
        px(P, [(cx + wx, cy + wy)], '#7f708a', 3.1)
        px(P, [(cx + wx, cy + wy + 1)], '#323353', 3.1)
    # barbatana do peito
    parte(P, poligono([(cx - 6, cy + 6), (cx - 13, cy + 14 + ca), (cx - 9, cy + 13), (cx - 7, cy + 16 + ca), (cx - 2, cy + 9)]), 'abissal_t', 3.2)
    # pintas luminosas
    for i, (x, y) in enumerate(((-15, 2), (-11, 5), (-7, 7), (-3, 9))):
        px(P, [(cx + x, cy + y)], '#30e1b9' if (i + t) % 2 else '#8ff8e2', 3.3)
    # antena e isca
    ant = curva(cx + 4, cy - 14, -100, 22, 22, 9)
    parte(P, corrente(ant, 1.0, 0.6), 'rocha', 1.5)
    lx, ly = int(ant[-1][0]), int(ant[-1][1]) + 2
    pul = (0, 1, 2, 1)[t]
    halo = elipse(lx + 0.5, ly + 0.5, 3.5 + pul, 3.5 + pul) - elipse(lx + 0.5, ly + 0.5, 2.6 + pul, 2.6 + pul)
    px(P, [p for i, p in enumerate(sorted(halo)) if (i + t) % 3 == 0], '#30e1b9', 3.9)
    parte(P, elipse(lx + 0.5, ly + 0.5, 2.8, 2.8), 'barbatana', 4)
    px(P, [(lx - 1, ly - 1), (lx, ly - 1)], BRANCO, 4.1)
    return render(P, 64, T)
