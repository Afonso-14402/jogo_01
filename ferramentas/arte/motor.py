"""Motor de desenho de pixel art (estilo da referência Aranha-Mãe).

Um boneco é uma lista de PARTES (formas simples: elipses, cápsulas, retângulos, polígonos). Cada parte tem:
  - uma RAMPA de cores da paleta Resurrect 64 (do mais escuro para o mais claro);
  - um volume (esfera ou cilindro) que decide a luz: vem sempre de CIMA À ESQUERDA, com brilho forte;
  - uma ordem (z): as partes da frente ficam por cima e ganham um contorno escuro que as separa das de trás.
No fim, todo o boneco leva o contorno de fora (#2e222f).

Os bonecos (herói, monstros, NPCs) estão noutros ficheiros desta pasta e usam este motor.
"""
import math
from PIL import Image

OUT = '#2e222f'

# Rampas (escuro -> claro), só com cores da Resurrect 64.
RAMPAS = {
    'roxo':      ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'],
    'pele':      ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0'],
    'cabelo':    ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e'],
    'azul':      ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'vermelho':  ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790'],
    'cinza':     ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'couro':     ['#45293f', '#694f62', '#966c6c', '#ab947a', '#ab947a'],
    'castanho':  ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'ouro':      ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
    'cobre':     ['#6e2727', '#9e4539', '#cd683d', '#f57d4a', '#fca790'],
    'ferro':     ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff'],
    'madeira':   ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'verde':     ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'verde_esc': ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90'],
    'musgo':     ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#fbff86'],
    'agua':      ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'],
    'rosa':      ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
    'branco':    ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'lilas':     ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0'],
    'laranja':   ['#9e4539', '#cd683d', '#fb6b1d', '#f79617', '#fbb954'],
    'amarelo':   ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
    'preto':     ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a'],
}

LUZ = (-0.55, -0.65, 0.52)
_n = math.sqrt(sum(c * c for c in LUZ))
LUZ = tuple(c / _n for c in LUZ)


def hexrgb(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


# ---------- formas (devolvem um conjunto de píxeis) ----------

def elipse(cx, cy, rx, ry):
    m = set()
    for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            if ((x + .5 - cx) / rx) ** 2 + ((y + .5 - cy) / ry) ** 2 <= 1.0:
                m.add((x, y))
    return m


def retangulo(x1, y1, x2, y2, canto=0):
    m = {(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)}
    if canto:
        for cx, cy in ((x1, y1), (x2, y1), (x1, y2), (x2, y2)):
            m.discard((cx, cy))
    return m


def capsula(x1, y1, x2, y2, r):
    """Um "salsicha" de (x1,y1) a (x2,y2) com raio r: braços, pernas, patas, caudas."""
    m = set()
    dx, dy = x2 - x1, y2 - y1
    L2 = dx * dx + dy * dy or 1e-9
    for y in range(int(min(y1, y2) - r) - 1, int(max(y1, y2) + r) + 2):
        for x in range(int(min(x1, x2) - r) - 1, int(max(x1, x2) + r) + 2):
            px, py = x + .5, y + .5
            t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / L2))
            qx, qy = x1 + t * dx, y1 + t * dy
            if (px - qx) ** 2 + (py - qy) ** 2 <= r * r:
                m.add((x, y))
    return m


def poligono(pts):
    m = set()
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    for y in range(int(min(ys)), int(max(ys)) + 1):
        for x in range(int(min(xs)), int(max(xs)) + 1):
            px, py = x + .5, y + .5
            dentro = False
            j = len(pts) - 1
            for i in range(len(pts)):
                xi, yi = pts[i]
                xj, yj = pts[j]
                if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                    dentro = not dentro
                j = i
            if dentro:
                m.add((x, y))
    return m


def desenho_a_mao(linhas, x0, y0, mapa, z=0, separar=False, espelho=False):
    """Uma parte desenhada à mão, píxel a píxel: cada letra das linhas é uma cor do mapa ('.' = vazio)."""
    pix = {}
    larg = max(len(l) for l in linhas)
    for y, l in enumerate(linhas):
        for x, ch in enumerate(l):
            if ch == '.' or ch == ' ':
                continue
            xx = larg - 1 - x if espelho else x
            pix[(x0 + xx, y0 + y)] = mapa[ch]
    p = Parte(set(pix), None, z=z, separar=separar)
    p.pixels = pix
    return p


def mover(m, dx=0, dy=0):
    return {(x + dx, y + dy) for x, y in m}


def espelhar(m, eixo):
    return {(2 * eixo - x - 1, y) for x, y in m}


# ---------- o boneco ----------

class Parte:
    def __init__(self, mascara, rampa, z=0, volume='esfera', brilho=True, separar=True, plano=False, cor=None, luz=0.0):
        self.m = set(mascara)
        self.rampa = RAMPAS[rampa] if isinstance(rampa, str) else rampa
        self.z = z
        self.volume = volume
        self.brilho = brilho
        self.separar = separar
        self.plano = plano      # sem volume: só claro em cima-esquerda, escuro em baixo-direita
        self.cor = cor          # cor única (olhos, marcas): ignora a rampa
        self.luz = luz          # + mais claro / - mais escuro (ex.: caras um pouco mais claras)
        self.pixels = None      # desenho feito à mão (ver desenho_a_mao)


def _tom(parte, x, y, bbox):
    if parte.cor:
        return parte.cor
    if parte.pixels:
        return parte.pixels[(x, y)]
    r = parte.rampa
    x1, y1, x2, y2 = bbox
    cx, cy = (x1 + x2 + 1) / 2, (y1 + y2 + 1) / 2
    rx, ry = max(1, (x2 - x1 + 1) / 2), max(1, (y2 - y1 + 1) / 2)
    if parte.plano:
        m = parte.m
        if (x - 1, y) not in m or (x, y - 1) not in m:
            return r[3]
        if (x + 1, y) not in m or (x, y + 1) not in m:
            return r[1]
        return r[2]
    nx = (x + .5 - cx) / rx
    ny = (y + .5 - cy) / ry
    if parte.volume == 'cilindro_v':
        ny = ny * 0.25
    elif parte.volume == 'cilindro_h':
        nx = nx * 0.25
    d = nx * nx + ny * ny
    nz = math.sqrt(max(0.0, 1 - min(1.0, d)))
    i = nx * LUZ[0] + ny * LUZ[1] + nz * LUZ[2] + parte.luz
    if parte.brilho and i > 0.93:
        return r[4]
    if i > 0.62:
        return r[3]
    if i > 0.25:
        return r[2]
    if i > -0.25:
        return r[1]
    return r[0]


def desenhar(partes, largura, altura, contorno_fora=True):
    """Desenha as partes por ordem de z e devolve uma imagem RGBA."""
    px = {}
    dono = {}
    for parte in sorted(partes, key=lambda p: p.z):
        if not parte.m:
            continue
        xs = [p[0] for p in parte.m]
        ys = [p[1] for p in parte.m]
        bbox = (min(xs), min(ys), max(xs), max(ys))
        if parte.separar:
            for x, y in parte.m:
                for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    v = (x + vx, y + vy)
                    if v not in parte.m and v in px:
                        px[v] = OUT
        for x, y in parte.m:
            px[(x, y)] = _tom(parte, x, y, bbox)
            dono[(x, y)] = parte
    if contorno_fora:
        borda = set()
        for (x, y) in px:
            for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                v = (x + vx, y + vy)
                if v not in px:
                    borda.add(v)
        for v in borda:
            px[v] = OUT
    img = Image.new('RGBA', (largura, altura), (0, 0, 0, 0))
    for (x, y), c in px.items():
        if 0 <= x < largura and 0 <= y < altura:
            img.putpixel((x, y), hexrgb(c) + (255,))
    return img


def tira(frames):
    w, h = frames[0].size
    img = Image.new('RGBA', (w * len(frames), h), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        img.paste(f, (i * w, 0))
    return img


def previa_gif(linhas, caminho, escala=6, fundo=(50, 51, 83), ms=110):
    """linhas: lista de listas de animações (cada animação = lista de frames). Faz um GIF a mexer."""
    import math as _m
    w, h = linhas[0][0][0].size
    ncol = max(len(l) for l in linhas)
    ticks = 1
    for l in linhas:
        for a in l:
            ticks = ticks * len(a) // _m.gcd(ticks, len(a))
    ticks = min(ticks, 60)
    imgs = []
    for t in range(ticks):
        im = Image.new('RGB', (ncol * w * escala, len(linhas) * h * escala), fundo)
        for j, l in enumerate(linhas):
            for i, a in enumerate(l):
                f = a[t % len(a)].resize((w * escala, h * escala), Image.NEAREST)
                im.paste(f, (i * w * escala, j * h * escala), f)
        imgs.append(im.convert('P', palette=Image.ADAPTIVE))
    imgs[0].save(caminho, save_all=True, append_images=imgs[1:], duration=ms, loop=0)
