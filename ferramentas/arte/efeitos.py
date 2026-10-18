"""Efeitos: projéteis, explosões por elemento, cortes das armas, ícones de estados e partículas.
Regras: docs/ARTE.md (secções 4 e 11). Tudo animado em tiras horizontais. Saída: arte/efeitos/.
Os efeitos de luz não levam contorno (brilham); os objetos (flecha, virote, ícones) levam.

Uso: python3 ferramentas/arte/efeitos.py
"""
import math
import os
import random
from PIL import Image

OUT = '#2e222f'
PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'efeitos')

# rampas dos elementos (escuro -> claro), só cores da Resurrect 64
EL = {
    'fogo':   ['#6e2727', '#b33831', '#ea4f36', '#f79617', '#f9c22b', '#fbff86'],
    'gelo':   ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff'],
    'raio':   ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff', '#ffffff'],
    'veneno': ['#45293f', '#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'luz':    ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff', '#ffffff'],
    'sombra': ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'],
    'fisico': ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
}


def _rgba(c, a=255):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (a,)


class Q:
    """Quadro de píxeis com contorno opcional."""

    def __init__(self, W, H=None):
        self.W, self.H = W, H or W
        self.p = {}

    def put(self, x, y, c):
        x, y = int(math.floor(x)), int(math.floor(y))
        if 0 <= x < self.W and 0 <= y < self.H:
            self.p[(x, y)] = c

    def disco(self, cx, cy, r, rampa, i0=0, buraco=0.0, pontilhado=False):
        """Disco brilhante: mais claro no centro (luz própria)."""
        for y in range(int(cy - r) - 1, int(cy + r) + 2):
            for x in range(int(cx - r) - 1, int(cx + r) + 2):
                d = math.hypot(x + .5 - cx, y + .5 - cy) / max(r, 0.01)
                if d <= 1 and d >= buraco and (not pontilhado or (x + y) % 2 == 0 or d < 0.7):
                    k = min(len(rampa) - 1, max(0, int((1 - d) * (len(rampa) - i0)) + i0))
                    self.put(x, y, rampa[k])

    def imagem(self, contorno=False):
        im = Image.new('RGBA', (self.W, self.H))
        if contorno:
            for (x, y) in {(x + a, y + b) for (x, y) in self.p for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))} - set(self.p):
                if 0 <= x < self.W and 0 <= y < self.H:
                    im.putpixel((x, y), _rgba(OUT))
        for (x, y), c in self.p.items():
            im.putpixel((x, y), _rgba(c))
        return im


def tira(frames):
    W, H = frames[0].size
    im = Image.new('RGBA', (W * len(frames), H))
    for i, f in enumerate(frames):
        im.paste(f, (i * W, 0))
    return im


# ---------------- projéteis (16×16, a voar para a direita) ----------------

def orbe(el, f):
    q = Q(16)
    r = EL[el]
    rnd = random.Random(f * 13 + len(el))
    for i in range(5):   # rasto
        x = 9 - i * 2 - rnd.random() * 1.5
        y = 8 + rnd.uniform(-2.2, 2.2)
        q.disco(x, y, 1.6 - i * 0.25, r[: 4 - i // 2])
    q.disco(10, 8, 3.6 + (f % 2) * 0.4, r, i0=1)
    q.put(9, 6, r[-1])
    return q.imagem()


def estilhaco_gelo(f):
    q = Q(16)
    r = EL['gelo']
    for x in range(3, 14):
        meia = 2.5 - abs(x - 9) * 0.45 if x >= 6 else 1.2 - (6 - x) * 0.4
        for y in range(int(8 - meia), int(8 + meia) + 1):
            q.put(x, y, r[5] if y < 8 and x > 8 else r[3] if y < 8 else r[2])
    for i in range(3):   # cristais soltos a brilhar
        q.put(2 + i * 2 + f % 2, 5 + (i * 3 + f) % 7, r[4])
    return q.imagem(contorno=True)


def raio(f):
    q = Q(16)
    r = EL['raio']
    rnd = random.Random(f * 31 + 7)
    y = 8
    for x in range(1, 15):
        y = max(3, min(12, y + rnd.choice((-1, 0, 1))))
        q.put(x, y, r[4])
        q.put(x, y - 1, r[2])
        q.put(x, y + 1, r[2])
    q.disco(13, y, 2.4, r, i0=2)
    return q.imagem()


def cuspe(el, f):
    q = Q(16)
    r = EL[el]
    q.disco(10, 8, 3.2, r[1:], i0=1)
    q.put(9, 6, r[-1])
    for i in range(3):
        q.disco(5 - i * 2, 8 + ((i + f) % 3) - 1, 1.3, r[1:4])
    return q.imagem(contorno=True)


def flecha():
    q = Q(16)
    for x in range(2, 12):
        q.put(x, 8, '#966c6c')
    for x, y in ((12, 8), (13, 8), (12, 7), (12, 9), (14, 8)):
        q.put(x, y, '#c7dcd0' if y == 7 or x == 14 else '#9babb2')
    for x, y in ((1, 6), (2, 7), (1, 10), (2, 9), (3, 7), (3, 9)):
        q.put(x, y, '#ffffff' if y < 8 else '#c7dcd0')
    return q.imagem(contorno=True)


def virote():
    q = Q(16)
    for x in range(3, 12):
        q.put(x, 8, '#694f62')
        q.put(x, 7, '#966c6c')
    for x, y in ((12, 7), (12, 8), (13, 7), (13, 8), (14, 8), (14, 7)):
        q.put(x, y, '#c7dcd0' if y == 7 else '#9babb2')
    for x, y in ((2, 6), (3, 6), (2, 9), (3, 9)):
        q.put(x, y, '#e83b3b')
    return q.imagem(contorno=True)


def pedra(f):
    q = Q(16)
    r = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
    ang = f * math.pi / 2
    for y in range(16):
        for x in range(16):
            u, v = x + .5 - 8, y + .5 - 8
            a = math.atan2(v, u) + ang
            if math.hypot(u, v) <= 4 + 0.8 * math.cos(3 * a):
                i = 3 if (u < 0 and v < 0) else 2 if u + v < 2 else 1
                q.put(x, y, r[i])
    return q.imagem(contorno=True)


# ---------------- explosões (32×32, 6 frames) ----------------

def explosao(el, f):
    q = Q(32)
    r = EL[el]
    rnd = random.Random(len(el) * 97)
    raio_ = [4, 8, 11, 13, 14, 15][f]
    if f < 3:
        q.disco(16, 16, raio_, r, i0=f)
    else:
        # o anel desvanece: claro por fora, cada vez com menos tons
        q.disco(16, 16, raio_, list(reversed(r[2:9 - f])), buraco=0.55 + 0.1 * (f - 3), pontilhado=f == 5)
    for i in range(10):   # faíscas a fugir
        a = rnd.uniform(0, 2 * math.pi)
        d = raio_ + 1 + rnd.uniform(0, 3) * (f / 2 + 0.5)
        if f > 0 and f < 5:
            q.put(16 + math.cos(a) * d, 16 + math.sin(a) * d, r[5 - f // 2])
    if el == 'raio' and f < 4:
        for k in range(4):
            a = k * math.pi / 2 + 0.4
            for s in range(raio_, raio_ + 5):
                q.put(16 + math.cos(a) * s + (s % 2), 16 + math.sin(a) * s, r[4])
    if el == 'gelo' and f >= 2:
        for k in range(6):
            a = k * math.pi / 3
            for s in range(3, raio_ - 1):
                q.put(16 + math.cos(a) * s, 16 + math.sin(a) * s, r[5 if f < 5 else 3])
    return q.imagem()


# ---------------- cortes e impactos das armas (32×32) ----------------

def corte(f, grande=False, n=4):
    """Rasto do golpe (virado para a direita): uma meia-lua grossa que varre de cima para baixo — aparece em
    ponta, fica cheia (branco no meio, azul-claro e cinza nas beiras) e desfaz-se aos píxeis."""
    q = Q(56 if grande else 40)
    c = q.W / 2
    R = q.W * 0.46
    esp = (9 if grande else 6.5)          # grossura no meio da meia-lua
    fim = [0.45, 1.0, 1.0, 1.0, 1.0][min(f, 4)]   # o primeiro quadro só tem a ponta de cima
    for y in range(q.H):
        for x in range(q.W):
            dx, dy = x + .5 - c, y + .5 - c
            ang = math.atan2(dy, dx)          # -pi/2 em cima, +pi/2 em baixo
            if ang < -1.75 or ang > 1.75:
                continue
            t = (ang + 1.75) / 3.5            # 0 em cima, 1 em baixo
            if t > fim:
                continue
            d = math.hypot(dx, dy)
            e = esp * math.sin(math.pi * min(1.0, t / max(fim, 0.01)) * 0.98 + 0.02)   # mais grossa a meio
            dentro = R - d
            if dentro < 0 or dentro > e:
                continue
            k = dentro / max(e, 0.5)
            col = '#ffffff' if k < 0.35 else ('#c7dcd0' if k < 0.65 else ('#8fd3ff' if k < 0.85 else '#4d9be6'))
            if f >= n - 2:                    # a desfazer-se: tira píxeis em xadrez, cada vez mais
                if (x + y + f) % (2 if f == n - 1 else 3) == 0 or (f == n - 1 and k > 0.4):
                    continue
                col = '#c7dcd0' if col == '#ffffff' else col
            q.put(x, y, col)
    return q.imagem()


def estocada(f):
    q = Q(32)
    comp = [8, 18, 24, 20][f]
    for x in range(4, 4 + comp):
        q.put(x, 16, '#ffffff')
        if x > 6 + f:
            q.put(x, 15, '#c7dcd0')
            q.put(x, 17, '#9babb2')
    for i in range(3):
        y = 12 + i * 4
        for x in range(2 + f * 3, 2 + f * 3 + 5):
            q.put(x, y, '#c7dcd0')
    return q.imagem()


def impacto(f):
    q = Q(32)
    r = EL['fisico']
    raio_ = [3, 6, 9, 11][f]
    for k in range(8):
        a = k * math.pi / 4 + 0.2
        for s in range(max(0, raio_ - 4), raio_):
            q.put(16 + math.cos(a) * s, 16 + math.sin(a) * s, r[5 - (f > 1)])
    if f < 2:
        q.disco(16, 16, 3 - f, ['#f9c22b', '#fbff86', '#ffffff'])
    return q.imagem()


def critico(f):
    q = Q(32)
    t = [5, 9, 12, 10][f]
    cores = ['#f79617', '#f9c22b', '#fbff86', '#ffffff']
    for k in range(4):
        a = k * math.pi / 2 + math.pi / 4 * (f % 2)
        for s in range(t):
            q.put(16 + math.cos(a) * s, 16 + math.sin(a) * s, cores[min(3, 3 - s * 4 // t)])
    q.disco(16, 16, 2.5, cores)
    return q.imagem()


# ---------------- ícones dos estados (9×9, por cima da cabeça) ----------------

ESTADOS = {
    'veneno': ("""
...oo....
..oVVo...
..oVVo...
.oVVVVo..
oVvVVVVo.
oVvVVVVo.
oVVVVVvo.
.oVVVvo..
..oooo...
""", {'V': '#1ebc73', 'v': '#91db69'}),
    'queimadura': ("""
....o....
...oFo...
..oFfo...
..oFfFo..
.oFfYfFo.
.oFYYYFo.
.oFfYfFo.
..oFFFo..
...ooo...
""", {'F': '#ea4f36', 'f': '#f79617', 'Y': '#fbff86'}),
    'frio': ("""
....o....
.o.oBo.o.
..oBBBo..
.oBBWBBo.
oBBWWWBBo
.oBBWBBo.
..oBBBo..
.o.oBo.o.
....o....
""", {'B': '#4d9be6', 'W': '#ffffff'}),
    'congelado': ("""
.ooooooo.
oWBBBBBBo
oBWBBBBBo
oBBWBBBBo
oBBBBBBBo
oBBBBWBBo
oBBBBBWBo
oBBBBBBWo
.ooooooo.
""", {'B': '#8fd3ff', 'W': '#ffffff'}),
    'choque': ("""
....ooo..
...oYYo..
..oYYo...
.oYYYYo..
.ooYYYo..
...oYo...
..oYo....
..oo.....
.........
""", {'Y': '#f9c22b'}),
    'atordoado': ("""
....o....
...oYo...
oooYYYooo
oYYYWYYYo
.oYYYYYo.
.oYYoYYo.
oYYo.oYYo
ooo...ooo
.........
""", {'Y': '#f9c22b', 'W': '#ffffff'}),
    'sangrar': ("""
....o....
...oRo...
..oRRo...
..oRRRo..
.oRrRRRo.
.oRrRRRo.
.oRRRRRo.
..oRRRo..
...ooo...
""", {'R': '#e83b3b', 'r': '#f68181'}),
    'lentidao': ("""
.........
..ooooo..
.oCCCCCo.
oCcoooCCo
oCoCCoCCo
oCcCCoCCo
.oCooCCo.
..oCCCo..
...ooo...
""", {'C': '#cd683d', 'c': '#e6904e'}),
    'cegueira': ("""
.........
..ooooo..
.oWWWWWo.
oWWoooWWo
oWoxxxoWo
oWWoooWWo
.oWWWWWo.
..ooooo..
.........
""", {'W': '#c7dcd0', 'x': '#3e3546'}),
    'medo': ("""
.ooooooo.
oPPPPPPPo
oPoPPPoPo
oPoPPPoPo
oPPPPPPPo
oPPoooPPo
oPoPPPoPo
oPPPPPPPo
.ooooooo.
""", {'P': '#a884f3'}),
    'maldicao': ("""
..ooooo..
.oSSSSSo.
oSSoSoSSo
oSSSSSSSo
.oSoooSo.
..oSSSo..
..oSoSo..
..ooooo..
.........
""", {'S': '#905ea9'}),
    'encharcado': ("""
....o....
...oAo...
...oAo...
..oAAAo..
.oAaAAAo.
.oAaAAAo.
.oAAAAAo.
..oAAAo..
...ooo...
""", {'A': '#4d9be6', 'a': '#8fd3ff'}),
}

# estados especiais (docs/SISTEMAS.md, 5.1)
ESTADOS.update({
    'agarrado': ("""
..o.o.o..
.oSoSoSo.
.oSoSoSo.
.oSSSSSoo
.oSSSSSoS
.oSSSSSSo
..oSSSSo.
...oSSo..
....oo...
""", {'S': '#fca790'}),
    'preso': ("""
.o.....o.
oRo...oRo
.oRo.oRo.
..oRoRo..
...oRo...
..oRoRo..
.oRo.oRo.
oRo...oRo
.o.....o.
""", {'R': '#7a4841'}),
    'puxado': ("""
..ooooo..
.oMMMMMo.
oMMoooMMo
oMo...oMo
oMo...oMo
oWo...oWo
oWo...oWo
ooo...ooo
.........
""", {'M': '#e83b3b', 'W': '#ffffff'}),
    'partida': ("""
...o.....
..oYo....
.oYYYYYo.
..oYo..o.
...o.o...
.o..oYo..
.oYYYYYo.
....oYo..
.....o...
""", {'Y': '#f5a097'}),
    'trocado': ("""
.o.....o.
oGo...oGo
.oGo.oGo.
..oGoGo..
...oGo...
..oGoGo..
.oGo.oGo.
oGGo.oGGo
.oo...oo.
""", {'G': '#b2ba90'}),
    'sapo': ("""
.oo...oo.
oWbo.oWbo
oGGoooGGo
oGGGGGGGo
oGgggggGo
oGGGGGGGo
.oGGGGGo.
..ooooo..
.........
""", {'G': '#5ac54f', 'g': '#1ebc73', 'W': '#ffffff', 'b': '#2e222f'}),
    'parado': ("""
..ooooo..
.oWWWWWo.
oWWWoWWWo
oWWWoWWWo
oWWWooWWo
oWWWWWWWo
.oWWWWWo.
..ooooo..
.........
""", {'W': '#e3c896'}),
    'silencio': ("""
..ooooo..
.oWWWWWo.
oWoWWWoWo
oWWoWoWWo
oWWWoWWWo
oWWoWoWWo
.ooWWWoo.
..ooooo..
.........
""", {'W': '#9babb2'}),
    'encolhido': ("""
...ooo...
...oYo...
...oYo...
.ooYYYoo.
..oYYYo..
...oYo...
....o....
.ooooooo.
.........
""", {'Y': '#e3c896'}),
})



def icone_estado(nome, f):
    g, cores = ESTADOS[nome]
    cores = dict(cores, o=OUT)
    im = Image.new('RGBA', (9, 11))
    dy = [0, -1, -1, 0][f]   # sobe e desce
    for y, l in enumerate(g.strip('\n').split('\n')):
        for x, ch in enumerate(l):
            if ch != '.':
                im.putpixel((x, y + 1 + dy), _rgba(cores[ch]))
    return im


# ---------------- partículas (8×8) ----------------

PARTICULAS = {
    'folha': (['.....o..', '...ooGo.', '..oGGgo.', '.oGgGo..', '.oGGo...', 'ooo.....'], {'G': '#239063', 'g': '#91db69'}),
    'neve': (['........', '...w....', '.w.w.w..', '..www...', 'wwwWwww.', '..www...', '.w.w.w..', '...w....'],
             {'w': '#c7dcd0', 'W': '#ffffff'}),
    'cinza': (['........', '...oo...', '..oCco..', '..occo..', '...oo...', '........', '........', '........'],
              {'C': '#7f708a', 'c': '#625565'}),
    'bolha': (['........', '..oooo..', '.oWaaao.', '.oaaaao.', '.oaaaao.', '..oooo..', '........', '........'],
              {'W': '#ffffff', 'a': '#8fd3ff'}),
    'faisca': (['........', '...Y....', '...Y....', '.YYWYY..', '...Y....', '...Y....', '........', '........'],
               {'Y': '#f9c22b', 'W': '#ffffff'}),
    'esporo': (['........', '..vvv...', '.vVWVv..', '.vVVVv..', '..vvv...', '........', '........', '........'],
               {'V': '#cddf6c', 'v': '#91db69', 'W': '#ffffff'}),
    'pena': (['......o.', '....ooWo', '...oWwo.', '..oWwo..', '.oWwo...', 'oooo....', 'o.......', '........'],
             {'W': '#ffffff', 'w': '#c7dcd0'}),
    'gota': (['...o....', '..oAo...', '..oAo...', '.oAaAo..', '.oAAAo..', '..ooo...', '........', '........'],
             {'A': '#4d9be6', 'a': '#ffffff'}),
    'brasa': (['........', '...o....', '..oFo...', '.oFYFo..', '..oFo...', '...o....', '........', '........'],
              {'F': '#ea4f36', 'Y': '#fbff86'}),
    'petala': (['........', '..ooo...', '.oRRRo..', 'oRrRRo..', '.oRRo...', '..oo....', '........', '........'],
               {'R': '#f04f78', 'r': '#fdcbb0'}),
}


def particula(nome):
    g, cores = PARTICULAS[nome]
    cores = dict(cores, o=OUT)
    im = Image.new('RGBA', (8, 8))
    for y, l in enumerate(g):
        for x, ch in enumerate(l):
            if ch != '.':
                im.putpixel((x, y), _rgba(cores[ch]))
    return im


# ---------------- efeitos do jogo ----------------

def poeira(f):
    q = Q(16)
    r = ['#625565', '#7f708a', '#9babb2', '#c7dcd0']
    for i, (x, y) in enumerate(((5, 12), (10, 12), (7, 10))):
        q.disco(x + f * (1 if i else -1) * 0.7, y - f * 0.8, [2.6, 3.2, 3.0, 2.0][f] - i * 0.3, r[: 4 - f // 2],
                pontilhado=f == 3)
    return q.imagem()


def fumo_morte(f):
    """32×32: o monstro desfaz-se numa nuvem de fumo que cresce e se desfaz, com estrelinhas a saltar."""
    q = Q(32)
    r = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']
    bolas = ((16, 20, 0), (10, 22, 1), (22, 22, 2), (13, 15, 3), (19, 14, 4))
    for i, (x, y, k) in enumerate(bolas):
        if f < 1 and i > 2:
            continue
        cresce = [3.5, 5.0, 5.8, 6.0, 5.2, 3.8][f] - k * 0.4
        sobe = f * 1.3 + k * 0.3
        q.disco(x + (x - 16) * f * 0.25, y - sobe, cresce, r[: 5 - f // 2], pontilhado=f >= 4)
    if 1 <= f <= 4:
        for i, (dx, dy) in enumerate(((-11, -6), (11, -8), (-7, -12), (8, -13))):
            x, y = 16 + dx * (0.6 + f * 0.15), 16 + dy * (0.6 + f * 0.15)
            c = '#fbff86' if (i + f) % 2 else '#ffffff'
            for d in (-1, 0, 1):
                q.put(x + d, y, c)
                q.put(x, y + d, c)
    return q.imagem()


def cura(f):
    q = Q(16, 32)
    cores = ['#1ebc73', '#91db69', '#ffffff']
    for i, (x, y0) in enumerate(((4, 28), (11, 24), (7, 18), (12, 30))):
        y = y0 - f * 4
        if 0 < y < 31:
            c = cores[(i + f) % 3]
            for d in (-1, 0, 1):
                q.put(x + d, y, c)
                q.put(x, y + d, c)
    return q.imagem()


def subir_nivel(f):
    q = Q(32, 48)
    r = EL['luz']
    larg = [2, 5, 7, 7, 5, 2][f]
    for y in range(48 - [10, 30, 48, 48, 48, 48][f], 48):
        for x in range(16 - larg, 16 + larg + 1):
            d = abs(x - 16) / max(1, larg)
            if f < 4 or (x + y) % 2 == 0:
                q.put(x, y, r[5 - int(d * 3) - (1 if y < 20 else 0)])
    rnd = random.Random(f)
    for _ in range(8):
        q.put(rnd.randrange(4, 28), rnd.randrange(4, 44), r[5])
    return q.imagem()


def brilho_item(f):
    q = Q(16)
    t = [1, 3, 5, 3][f]
    for s in range(-t, t + 1):
        q.put(8 + s, 8, '#ffffff' if abs(s) < 2 else '#fbff86')
        q.put(8, 8 + s, '#ffffff' if abs(s) < 2 else '#fbff86')
    if f == 2:
        for d in (-2, 2):
            q.put(8 + d, 8 + d, '#fbff86')
            q.put(8 + d, 8 - d, '#fbff86')
    return q.imagem()


def portal(f):
    """Aparecer/desaparecer: anel que gira e fecha."""
    q = Q(32)
    r = EL['sombra']
    R = [4, 9, 12, 13, 12, 9][f]
    for k in range(48):
        a = k * 2 * math.pi / 48 + f * 0.5
        rr = R * (0.85 + 0.15 * math.sin(a * 3))
        q.put(16 + math.cos(a) * rr, 16 + math.sin(a) * rr * 0.5 + 8, r[4 - (k % 3)])
    for i in range(6):
        a = i + f
        q.put(16 + math.cos(a) * R * 0.5, 22 - (f * 2 + i * 3) % 20, r[5])
    return q.imagem()


def gerar():
    os.makedirs(PASTA, exist_ok=True)
    g = lambda nome, frames: tira(frames).save(os.path.join(PASTA, f'{nome}.png'))
    n = 0
    for el in ('fogo', 'luz', 'sombra'):
        g(f'projetil_{el}', [orbe(el, f) for f in range(4)]); n += 1
    g('projetil_gelo', [estilhaco_gelo(f) for f in range(4)])
    g('projetil_raio', [raio(f) for f in range(4)])
    g('projetil_veneno', [cuspe('veneno', f) for f in range(4)])
    g('projetil_pedra', [pedra(f) for f in range(4)])
    g('flecha', [flecha()])
    g('virote', [virote()])
    n += 6
    for el in EL:
        g(f'explosao_{el}', [explosao(el, f) for f in range(6)]); n += 1
    g('corte', [corte(f) for f in range(4)])
    g('corte_pesado', [corte(f, grande=True, n=5) for f in range(5)])
    g('estocada', [estocada(f) for f in range(4)])
    g('impacto', [impacto(f) for f in range(4)])
    g('critico', [critico(f) for f in range(4)])
    n += 5
    for nome in ESTADOS:
        g(f'estado_{nome}', [icone_estado(nome, f) for f in range(4)]); n += 1
    for nome in PARTICULAS:
        g(f'particula_{nome}', [particula(nome)]); n += 1
    g('poeira', [poeira(f) for f in range(4)])
    g('fumo_morte', [fumo_morte(f) for f in range(6)])
    g('cura', [cura(f) for f in range(6)])
    g('subir_nivel', [subir_nivel(f) for f in range(6)])
    g('brilho_item', [brilho_item(f) for f in range(4)])
    g('portal', [portal(f) for f in range(6)])
    n += 5
    print('ok', n, 'efeitos')


if __name__ == '__main__':
    gerar()
