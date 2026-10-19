"""Os móveis básicos em pixel art para a vista 2D (docs/ARTE.md, secção 6.3; docs/PROGRAMACAO.md, 4A).

As peças 3D dos móveis (arte/moveis/movel_bNN.glb) são formas simples; fotografadas para o 2D pareciam caixas.
Aqui cada móvel é feito de caixinhas (pernas, tampo, colchão, almofada, livros...) e manchas (folhas), desenhadas
com a mesma projeção do 2D: 1 m = 16 px, vê-se o topo e a frente (o alto sobe 0,8 m no ecrã por cada metro).
Luz de cima à esquerda, contorno escuro (#2e222f) e só cores da paleta Resurrect 64.

Cada móvel tem as 4 rotações (0°, 90°, 180°, 270° à volta do eixo vertical, como no Godot): as caixas rodam e o
desenho faz-se outra vez (uma cadeira de lado mostra o encosto ao lado). A vela e a lareira têm 4 quadros (a chama
mexe-se).

Saída: arte/moveis2d/<id>_r<rotação>.png (os animados: uma tira de quadros lado a lado) e dados/moveis2d.json
       {"moveis": {id: {"r0": [png, âncora x, âncora y, quadros], ...}}, "regional": {id regional: id básico}}
Uso:   python3 ferramentas/arte/moveis2d.py [--previa pasta]
"""
import json
import math
import os
import random
import sys

from PIL import Image

PX = 16.0
SOBE = 0.8
M = 1   # margem (para o contorno)
SAIDA = os.path.join('arte', 'moveis2d')


def hx(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


OUT = hx('#2e222f')
R = {
    'madeira':  ['#4c3e24', '#7a3045', '#9e4539', '#cd683d', '#e6904e'],
    'madeira_c': ['#4c3e24', '#9e4539', '#cd683d', '#e6904e', '#fbb954'],
    'pedra':    ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'branco':   ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'vermelho': ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790'],
    'azul':     ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'verde':    ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'ouro':     ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
    'ferro':    ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff'],
    'barro':    ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'],
    'creme':    ['#966c6c', '#ab947a', '#fbb954', '#fbff86', '#ffffff'],
    'escuro':   ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565'],
    'livro_r':  ['#6e2727', '#6e2727', '#b33831', '#ea4f36', '#ea4f36'],
    'livro_a':  ['#323353', '#323353', '#4d65b4', '#4d9be6', '#4d9be6'],
    'livro_v':  ['#165a4c', '#165a4c', '#239063', '#1ebc73', '#1ebc73'],
    'livro_o':  ['#9e4539', '#9e4539', '#f79617', '#f9c22b', '#f9c22b'],
    'livro_l':  ['#45293f', '#45293f', '#6b3e75', '#905ea9', '#905ea9'],
}


class Caixa:
    def __init__(self, x0, x1, y0, y1, z0, z1, rampa, veio=False, borda=True, padrao=None, cor_frente=None):
        self.x0, self.x1, self.y0, self.y1, self.z0, self.z1 = x0, x1, y0, y1, z0, z1
        self.r = [hx(c) for c in R[rampa]] if isinstance(rampa, str) else rampa
        self.veio = veio          # veios da madeira
        self.borda = borda        # linha escura à volta de cada face
        self.padrao = padrao      # função (u, v) -> cor ou None, por cima do topo (tapetes)
        self.cor_frente = cor_frente   # função (u, v, w, h) -> cor ou None, por cima da frente (gavetas, fogo, quadro)

    def rodar(self, r):
        x0, x1, z0, z1 = self.x0, self.x1, self.z0, self.z1
        for _ in range(r % 4):   # +90° no Godot: (x, z) -> (z, -x)
            x0, x1, z0, z1 = z0, z1, -x1, -x0
        c = Caixa(x0, x1, self.y0, self.y1, z0, z1, self.r, self.veio, self.borda, self.padrao, self.cor_frente)
        c.rot = r % 4
        return c


class Mancha:
    """Uma mancha redonda (folha, flor, chama) no sítio (x, y, z) com raio em metros; desenha-se no ecrã."""
    def __init__(self, x, y, z, rx, ry, rampa):
        self.x, self.y, self.z, self.rx, self.ry = x, y, z, rx, ry
        self.r = [hx(c) for c in R[rampa]] if isinstance(rampa, str) else rampa

    def rodar(self, r):
        x, z = self.x, self.z
        for _ in range(r % 4):
            x, z = z, -x
        return Mancha(x, self.y, z, self.rx, self.ry, self.r)


def desenhar(pecas):
    """Desenha a lista de caixas e manchas (já rodadas). Devolve (imagem, âncora x, âncora y)."""
    xs, ss = [], []
    for p in pecas:
        if isinstance(p, Caixa):
            xs += [p.x0, p.x1]
            ss += [p.z0 - SOBE * p.y1, p.z1 - SOBE * p.y0]
        else:
            xs += [p.x - p.rx, p.x + p.rx]
            ss += [p.z - SOBE * p.y - p.ry, p.z - SOBE * p.y + p.ry]
    X0, S0 = min(xs), min(ss)
    w = int(math.ceil((max(xs) - X0) * PX)) + 2 * M
    h = int(math.ceil((max(ss) - S0) * PX)) + 2 * M
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    px = img.load()

    def ex(x):
        return int(round((x - X0) * PX)) + M

    def ey(z, y):
        return int(round((z - SOBE * y - S0) * PX)) + M

    fundo = {}   # profundidade de cada píxel: y + 0,8·z (maior = mais perto de quem vê, de cima e de sul)

    def pinta(x, y, c, d=0.0):
        if 0 <= x < w and 0 <= y < h and d >= fundo.get((x, y), -1e9) - 1e-6:
            fundo[(x, y)] = d
            px[x, y] = c + (255,)

    def s_de(y):   # a linha do ecrã em metros
        return (y + 0.5 - M) / PX + S0

    ordem = sorted(pecas, key=lambda p: (round(p.z1, 3), p.y0) if isinstance(p, Caixa) else (round(p.z + p.rx * 0.5, 3), p.y))
    for p in ordem:
        if isinstance(p, Mancha):
            cx, cy = (p.x - X0) * PX + M, (p.z - SOBE * p.y - S0) * PX + M
            rx, ry = max(0.6, p.rx * PX), max(0.6, p.ry * PX)
            for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
                for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
                    u, v = (x + 0.5 - cx) / rx, (y + 0.5 - cy) / ry
                    d = u * u + v * v
                    if d <= 1.0:
                        k = 4 if (u + v < -0.9 and d > 0.15) else (3 if u + v < 0.2 else (2 if d < 0.85 else 1))
                        pinta(x, y, p.r[k], p.y + SOBE * p.z + p.rx * (1.0 - d))
            continue
        a, b = ex(p.x0), ex(p.x1)
        t0, t1 = ey(p.z0, p.y1), ey(p.z1, p.y1)     # o topo
        f1 = ey(p.z1, p.y0)                          # o fundo da frente
        if b <= a:
            b = a + 1
        # topo
        for y in range(t0, max(t1, t0 + (1 if p.y1 - p.y0 < 0.05 else 0))):
            for x in range(a, b):
                u, v = (x - a) / max(1, b - a), (y - t0) / max(1, t1 - t0)
                c = p.r[3]
                if p.veio and (y - t0) % 3 == 2 and (x * 7 + y * 3) % 11 > 2:
                    c = p.r[2]
                if p.padrao:
                    c2 = p.padrao(u, v, x - a, y - t0, b - a, t1 - t0)
                    if c2 == 'x':
                        continue   # (transparente: tapete redondo)
                    if c2:
                        c = c2
                if p.borda and b - a > 3 and t1 - t0 > 2 and (y == t0 or x == a or x == b - 1):
                    c = p.r[1] if y == t0 else p.r[2]
                pinta(x, y, c, (1 + SOBE * SOBE) * p.y1 + SOBE * s_de(y))
        if t1 > t0 and p.borda and b - a > 2:   # aresta clara entre o topo e a frente
            for x in range(a, b):
                pinta(x, t1 - 1, p.r[4], (1 + SOBE * SOBE) * p.y1 + SOBE * s_de(t1 - 1) + 1e-4)
        # frente
        for y in range(t1, f1):
            for x in range(a, b):
                c = p.r[2]
                if p.veio and (y - t1) % 4 == 3 and (x * 5 + y) % 9 > 1:
                    c = p.r[1]
                if p.cor_frente:
                    c2 = p.cor_frente((x - a) / max(1, b - a), (y - t1) / max(1, f1 - t1), x - a, y - t1, b - a, f1 - t1)
                    if c2:
                        c = c2
                if p.borda and (y == f1 - 1 or x == b - 1) and b - a > 2:
                    c = p.r[1]
                if p.borda and x == a and b - a > 3:
                    c = p.r[3] if y > t1 else c
                pinta(x, y, c, (p.z1 - s_de(y)) / SOBE + SOBE * p.z1)
    # contorno escuro por fora
    cheio = {(x, y) for y in range(h) for x in range(w) if px[x, y][3]}
    for (x, y) in cheio:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (x + dx, y + dy)
            if v not in cheio and 0 <= v[0] < w and 0 <= v[1] < h:
                px[v] = OUT + (255,)
    ax = (0 - X0) * PX + M
    ay = (0 - S0) * PX + M
    return img, ax, ay


# ------------------------------------------------------------ os móveis (em metros; a frente é +z, o sul)

def pernas(x0, x1, z0, z1, alt, g=0.07, rampa='madeira'):
    return [Caixa(x, x + g, 0, alt, z, z + g, rampa, borda=False) for x in (x0, x1 - g) for z in (z0, z1 - g)]


def cama(cor='vermelho'):
    return [Caixa(-0.5, 0.5, 0, 0.9, -1.02, -0.92, 'madeira', veio=True),           # cabeceira
            Caixa(-0.5, 0.5, 0, 0.4, -0.92, 0.96, 'madeira', veio=True),            # estrado
            Caixa(-0.46, 0.46, 0.4, 0.55, -0.9, 0.92, 'branco'),                     # colchão
            Caixa(-0.33, 0.33, 0.55, 0.66, -0.88, -0.6, 'branco'),                   # almofada
            Caixa(-0.48, 0.48, 0.55, 0.6, -0.5, 0.94, cor,
                  padrao=lambda u, v, x, y, w, h: hx(R[cor][4]) if y == 1 or (x % 6 == 2 and y > 2) else None),   # manta
            Caixa(-0.5, 0.5, 0, 0.62, 0.92, 1.0, 'madeira', veio=True)]               # pés da cama


def mesa(itens=True, toalha=None):
    p = pernas(-0.78, 0.78, -0.43, 0.43, 0.78) + [Caixa(-0.8, 0.8, 0.78, 0.85, -0.45, 0.45, 'madeira_c', veio=True)]
    if toalha:
        p.append(Caixa(-0.5, 0.5, 0.85, 0.86, -0.45, 0.45, toalha, borda=False,
                       padrao=lambda u, v, x, y, w, h: hx(R[toalha][4]) if (x + y) % 4 == 0 else None))
    if itens:
        p += [Caixa(-0.45, -0.2, 0.85, 0.87, -0.15, 0.08, 'branco', borda=False),   # prato
              Mancha(-0.33, 0.9, -0.04, 0.07, 0.05, 'barro'),                       # pão
              Caixa(0.25, 0.37, 0.85, 1.0, -0.2, -0.08, 'azul'),                     # caneca
              Caixa(0.45, 0.6, 0.85, 0.88, 0.05, 0.25, 'creme', borda=False)]        # papel
    return p


def cabeceira():
    gaveta = lambda u, v, x, y, w, h: hx('#4c3e24') if y == h // 2 or (x == w // 2 and abs(y - h // 4) <= 0) else None
    return [Caixa(-0.26, 0.26, 0, 0.55, -0.2, 0.2, 'madeira', veio=True, cor_frente=gaveta),
            Caixa(-0.05, 0.05, 0.55, 0.7, -0.05, 0.05, 'branco'), Mancha(0.0, 0.76, 0.0, 0.03, 0.05, 'ouro')]


def cadeira():
    return (pernas(-0.21, 0.21, -0.21, 0.21, 0.44, g=0.06) +
            [Caixa(-0.23, 0.23, 0.42, 0.49, -0.23, 0.23, 'madeira_c', veio=True),
             Caixa(-0.23, -0.16, 0.49, 1.05, -0.23, -0.17, 'madeira', borda=False),
             Caixa(0.16, 0.23, 0.49, 1.05, -0.23, -0.17, 'madeira', borda=False),
             Caixa(-0.23, 0.23, 0.82, 1.05, -0.23, -0.17, 'madeira'),
             Caixa(-0.23, 0.23, 0.6, 0.66, -0.23, -0.17, 'madeira', borda=False)])


def banco():
    return (pernas(-0.18, 0.18, -0.18, 0.18, 0.4, g=0.06) +
            [Caixa(-0.21, 0.21, 0.4, 0.47, -0.21, 0.21, 'madeira_c', veio=True)])


def banco_igreja():
    """Banco comprido da igreja, com encosto do lado de quem está sentado (vê-se por trás, virado para o altar)."""
    return (pernas(-0.82, 0.82, -0.2, 0.2, 0.42, g=0.07) +
            [Caixa(-0.85, 0.85, 0.42, 0.49, -0.22, 0.22, 'madeira_c', veio=True),
             Caixa(-0.85, 0.85, 0.49, 1.0, 0.16, 0.23, 'madeira', veio=True),
             Caixa(-0.88, -0.8, 0.0, 1.05, 0.14, 0.25, 'madeira'),
             Caixa(0.8, 0.88, 0.0, 1.05, 0.14, 0.25, 'madeira')])


def tapete(redondo=False, cor='vermelho', cor2='ouro'):
    c1, c2, c3 = hx(R[cor][2]), hx(R[cor2][2]), hx(R[cor][1])

    def pad(u, v, x, y, w, h):
        du, dv = u - 0.5, v - 0.5
        if redondo:
            d = math.sqrt((du / 0.5) ** 2 + (dv / 0.5) ** 2)
            if d > 1.0:
                return 'x'
            if d > 0.86:
                return c3
            return c2 if 0.62 < d < 0.72 or d < 0.16 else c1
        if x < 2 or y < 1 or x >= w - 2 or y >= h - 1:
            return c3
        if x in (3, w - 4) or y in (2, h - 3):
            return c2
        if abs(du) < 0.15 and abs(dv) < 0.2 and (x + y) % 2 == 0:
            return c2
        return c1

    t = Caixa(-0.8, 0.8, 0, 0.02, -0.55, 0.55, cor, borda=False, padrao=pad)
    return [t]


def candeeiro():
    return [Caixa(-0.15, 0.15, 0, 0.05, -0.15, 0.15, 'ferro'),
            Caixa(-0.03, 0.03, 0.05, 1.18, -0.03, 0.03, 'ferro', borda=False),
            Caixa(-0.2, 0.2, 1.15, 1.45, -0.2, 0.2, 'creme',
                  cor_frente=lambda u, v, x, y, w, h: hx('#fbff86') if y >= h - 2 else None)]


def chama(q, x, y, z, k=1.0):
    """Uma chama que se mexe (q = quadro 0–3): 3 manchas, a de cima a abanar."""
    o = [0.0, 0.015, 0.0, -0.015][q] * k
    alt = [1.0, 1.15, 0.95, 1.1][q]
    return [Mancha(x, y + 0.03 * k, z, 0.045 * k, 0.05 * k, 'vermelho'),
            Mancha(x + o * 0.5, y + 0.07 * k * alt, z, 0.035 * k, 0.05 * k * alt, 'ouro'),
            Mancha(x + o, y + 0.12 * k * alt, z, 0.02 * k, 0.03 * k * alt, 'ouro')]


def vela(q=0):
    return [Caixa(-0.13, 0.13, 0, 0.04, -0.13, 0.13, 'ouro'),
            Caixa(-0.025, 0.025, 0.04, 0.8, -0.025, 0.025, 'ouro', borda=False),
            Caixa(-0.1, 0.1, 0.78, 0.82, -0.1, 0.1, 'ouro'),
            Caixa(-0.04, 0.04, 0.82, 1.0, -0.04, 0.04, 'branco')] + chama(q, 0.0, 1.0, 0.0)


def estante(alta=True, seed=1):
    rnd = random.Random(seed)
    topo = 2.2 if alta else 1.3
    n = 4 if alta else 2
    p = [Caixa(-0.8, 0.8, 0, topo, -0.26, -0.2, 'madeira', borda=False),          # fundo
         Caixa(-0.8, -0.73, 0, topo, -0.26, 0.26, 'madeira', veio=True),
         Caixa(0.73, 0.8, 0, topo, -0.26, 0.26, 'madeira', veio=True)]
    alt = topo / n
    for i in range(n + 1):
        y = i * alt
        p.append(Caixa(-0.8, 0.8, max(0, y - 0.04), y + 0.04, -0.26, 0.26, 'madeira_c', veio=True))
        if i == n:
            break
        x = -0.71
        while x < 0.68:
            if rnd.random() < 0.12:
                x += 0.12
                continue
            lw = rnd.choice([0.07, 0.08, 0.1, 0.12])
            lh = alt * rnd.uniform(0.55, 0.85)
            cor = rnd.choice(['livro_r', 'livro_a', 'livro_v', 'livro_o', 'livro_l'])
            if rnd.random() < 0.08 and x < 0.4:   # um livro deitado / um jarro
                p.append(Caixa(x, x + 0.25, y + 0.04, y + 0.11, -0.2, 0.22, cor, borda=False))
                x += 0.27
                continue
            p.append(Caixa(x, min(0.72, x + lw), y + 0.04, y + 0.04 + lh, -0.2, 0.24, cor, borda=False))
            x += lw + 0.01
    return p


def secretaria():
    gav = lambda u, v, x, y, w, h: hx('#4c3e24') if (y in (h // 3, 2 * h // 3)) or (x == w // 2 and y in (h // 6, h // 2, 5 * h // 6)) else None
    return (pernas(-0.78, -0.2, -0.43, 0.43, 0.78) +
            [Caixa(0.25, 0.78, 0, 0.78, -0.43, 0.43, 'madeira', veio=True, cor_frente=gav),
             Caixa(-0.8, 0.8, 0.78, 0.85, -0.45, 0.45, 'madeira_c', veio=True),
             Caixa(-0.55, -0.2, 0.85, 0.87, -0.2, 0.1, 'creme', borda=False),
             Caixa(-0.5, -0.25, 0.87, 0.88, -0.15, 0.05, 'branco', borda=False),
             Caixa(0.1, 0.18, 0.85, 0.95, -0.25, -0.17, 'escuro'),
             Caixa(0.3, 0.6, 0.85, 0.92, -0.15, 0.1, 'livro_v')])


def quadro():
    def pintura(u, v, x, y, w, h):
        if x < 1 or y < 1 or x >= w - 1 or y >= h - 1:
            return hx('#f9c22b') if (x + y) % 3 else hx('#f79617')
        if v < 0.45:
            return hx('#8fd3ff') if not (abs(u - 0.75) < 0.1 and abs(v - 0.2) < 0.12) else hx('#fbff86')
        colina = 0.55 + 0.15 * math.sin(u * 6.0)
        return hx('#1ebc73') if v < colina + 0.2 else hx('#239063')
    return [Caixa(-0.45, 0.45, 1.2, 1.9, -0.05, 0.05, 'ouro', borda=False, cor_frente=pintura)]


def vaso(flores=True):
    p = [Caixa(-0.15, 0.15, 0, 0.32, -0.15, 0.15, 'barro', cor_frente=lambda u, v, x, y, w, h: hx('#e6904e') if y == 1 else None)]
    if flores:
        p += [Caixa(-0.01, 0.01, 0.32, 0.55, -0.01, 0.01, 'verde', borda=False),
              Mancha(-0.1, 0.42, 0.02, 0.07, 0.05, 'verde'), Mancha(0.1, 0.45, 0.0, 0.07, 0.05, 'verde'),
              Mancha(-0.07, 0.62, 0.0, 0.06, 0.05, 'vermelho'), Mancha(0.08, 0.66, 0.0, 0.06, 0.05, 'ouro'),
              Mancha(0.0, 0.7, -0.02, 0.06, 0.05, 'azul')]
    return p


def planta():
    p = [Caixa(-0.2, 0.2, 0, 0.38, -0.2, 0.2, 'barro', cor_frente=lambda u, v, x, y, w, h: hx('#e6904e') if y == 1 else None),
         Caixa(-0.03, 0.03, 0.38, 0.8, -0.03, 0.03, 'madeira', borda=False)]
    for (x, y, z, r) in [(-0.2, 0.62, 0.05, 0.16), (0.2, 0.66, 0.03, 0.16), (0.0, 0.62, 0.12, 0.15), (-0.14, 0.92, -0.02, 0.17),
                         (0.16, 0.95, 0.0, 0.16), (0.0, 1.15, 0.0, 0.18), (0.0, 0.85, 0.1, 0.15)]:
        p.append(Mancha(x, y, z, r, r * 0.85, 'verde'))
    return p


def lareira(q=0):
    def tijolo(u, v, x, y, w, h):
        if 0.25 < u < 0.75 and v > 0.4:
            return None   # a boca (desenhada à parte)
        linha = y // 3
        if y % 3 == 0 or (x + (linha % 2) * 3) % 6 == 0:
            return hx('#625565')
        return None
    p = [Caixa(-0.9, 0.9, 0, 1.3, -0.35, 0.18, 'pedra', cor_frente=tijolo),
         Caixa(-0.95, 0.95, 1.08, 1.16, -0.38, 0.3, 'madeira_c', veio=True),            # a prateleira
         Caixa(-0.45, 0.45, 0.04, 0.72, 0.17, 0.19, 'escuro', borda=False),               # a boca
         Caixa(-0.9, 0.9, 0, 0.05, 0.18, 0.5, 'pedra'),                                   # a pedra do chão
         Caixa(-0.3, 0.3, 0.05, 0.13, 0.12, 0.2, 'madeira'),                               # lenha
         Caixa(-0.62, -0.5, 1.16, 1.3, -0.25, -0.13, 'ouro'), Caixa(0.4, 0.58, 1.16, 1.26, -0.25, -0.12, 'azul')]
    for i, x in enumerate((-0.18, 0.0, 0.18)):
        p += chama((q + i) % 4, x, 0.13, 0.21, k=2.6 if i == 1 else 2.0)
    return p


def armario():
    porta = lambda u, v, x, y, w, h: hx('#4c3e24') if x == w // 2 or y in (0,) or (abs(x - w // 2) == 2 and y == h // 2) else None
    p = [Caixa(-0.55, 0.55, 0, 0.9, -0.28, 0.3, 'madeira', veio=True, cor_frente=porta),
         Caixa(-0.57, 0.57, 0.9, 0.95, -0.3, 0.32, 'madeira_c', veio=True),
         Caixa(-0.55, 0.55, 0.95, 1.8, -0.28, -0.18, 'madeira', borda=False),
         Caixa(-0.55, -0.5, 0.95, 1.8, -0.28, 0.0, 'madeira'), Caixa(0.5, 0.55, 0.95, 1.8, -0.28, 0.0, 'madeira'),
         Caixa(-0.57, 0.57, 1.36, 1.4, -0.28, 0.0, 'madeira_c'), Caixa(-0.57, 0.57, 1.76, 1.82, -0.3, 0.02, 'madeira_c')]
    for i, x in enumerate((-0.4, -0.2, 0.0, 0.2)):   # pratos ao alto e frascos
        p.append(Mancha(x + 0.08, 1.12, -0.12, 0.08, 0.1, 'branco'))
    for x, c in ((-0.38, 'verde'), (-0.12, 'vermelho'), (0.14, 'ouro'), (0.36, 'azul')):
        p.append(Caixa(x - 0.06, x + 0.06, 1.4, 1.58, -0.16, -0.06, c))
    return p


def bau():
    bandas = lambda u, v, x, y, w, h: hx('#9babb2') if x in (2, w - 3) else (hx('#f9c22b') if abs(x - w // 2) <= 1 and 1 <= y <= 3 else None)
    return [Caixa(-0.46, 0.46, 0, 0.5, -0.3, 0.32, 'madeira', veio=True, cor_frente=bandas),
            Caixa(-0.48, 0.48, 0.5, 0.72, -0.32, 0.34, 'madeira_c', veio=True,
                  padrao=lambda u, v, x, y, w, h: hx('#9babb2') if x in (2, w - 3) else None, cor_frente=bandas)]


MOVEIS = {
    'movel_b01': lambda q: cama(),
    'movel_b03': lambda q: mesa(),
    'movel_b04': lambda q: cabeceira(),
    'movel_b05': lambda q: cadeira(),
    'movel_b06': lambda q: banco(),
    'movel_b09': lambda q: tapete(True),
    'movel_b10': lambda q: tapete(False, 'azul', 'ouro'),
    'movel_b11': lambda q: candeeiro(),
    'movel_b12': vela,
    'movel_b13': lambda q: estante(False, 2),
    'movel_b14': lambda q: estante(True, 1),
    'movel_b15': lambda q: secretaria(),
    'movel_b19': lambda q: quadro(),
    'movel_b20': lambda q: vaso(),
    'movel_b21': lambda q: planta(),
    'movel_b22': lareira,
    'movel_b24': lambda q: armario(),
    'movel_b25': lambda q: bau(),
}
ANIMADOS = {'movel_b12': 4, 'movel_b22': 4}
# os básicos que têm versão de cada região (ver ferramentas/dados/interiores.py, REGIONAL): no 2D usam o básico
REGIONAL = {'01': 'movel_b05', '02': 'movel_b03', '03': 'movel_b01', '04': 'movel_b09', '05': 'movel_b11', '06': 'movel_b14'}


def main():
    os.makedirs(SAIDA, exist_ok=True)
    indice = {'moveis': {}, 'regional': {}}
    previa = []
    for mid, fazer in MOVEIS.items():
        nq = ANIMADOS.get(mid, 1)
        e = {}
        for r in range(4):
            quadros = []
            for q in range(nq):
                img, ax, ay = desenhar([p.rodar(r) for p in fazer(q)])
                quadros.append(img)
            w = max(i.width for i in quadros)
            h = max(i.height for i in quadros)
            tira = Image.new('RGBA', (w * nq, h), (0, 0, 0, 0))
            for q, i in enumerate(quadros):
                tira.paste(i, (q * w, 0))
            nome = f'{mid}_r{r}.png'
            tira.save(os.path.join(SAIDA, nome))
            e[f'r{r}'] = [f'res://arte/moveis2d/{nome}', round(ax * 2) / 2, round(ay * 2) / 2, nq]
            previa.append((mid, r, quadros))
        indice['moveis'][mid] = e
    for reg in range(1, 11):
        for n, base in REGIONAL.items():
            indice['regional'][f'movel_r{reg:02d}_{n}'] = base
    # móveis só em 2D (sem peça .glb): o interior usa a imagem diretamente (interior.gd, ids "res://...png")
    for nome, pecas in (('banco_igreja', banco_igreja()),):
        img, ax, ay = desenhar(pecas)
        img.save(os.path.join(SAIDA, nome + '.png'))
    with open(os.path.join('dados', 'moveis2d.json'), 'w', encoding='utf-8') as f:
        json.dump(indice, f, ensure_ascii=False, indent=1)
    if '--previa' in sys.argv:
        pasta = sys.argv[sys.argv.index('--previa') + 1]
        fazer_previa(previa, pasta)
    print('moveis2d: %d móveis' % len(MOVEIS))


def fazer_previa(previa, pasta):
    """Uma folha com todos (4 rotações) e um GIF com os animados."""
    linhas = {}
    for mid, r, quadros in previa:
        linhas.setdefault(mid, []).append(quadros)
    W = 4 + sum(max(q[0].width for q in v) + 6 for v in [linhas[k] for k in linhas][:1]) * 0 + 4 * 70
    altura = sum(max(q[0].height for q in v) + 6 for v in linhas.values()) + 4
    frames = []
    for f in range(4):
        im = Image.new('RGBA', (W, altura), hx('#966c6c') + (255,))
        y = 4
        for mid, v in linhas.items():
            hh = max(q[0].height for q in v)
            x = 4
            for quadros in v:
                q = quadros[f % len(quadros)]
                im.alpha_composite(q, (x, y + hh - q.height))
                x += 70
            y += hh + 6
        frames.append(im.resize((W * 3, altura * 3), Image.NEAREST))
    frames[0].save(os.path.join(pasta, 'moveis2d.gif'), save_all=True, append_images=frames[1:], duration=160, loop=0)
    frames[0].save(os.path.join(pasta, 'moveis2d.png'))


if __name__ == '__main__':
    main()
