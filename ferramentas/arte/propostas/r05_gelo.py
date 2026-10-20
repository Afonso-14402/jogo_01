"""PROPOSTA: os monstros, guardiões e bosses da Região 5 (Gelo) desenhados de novo, mais bonitos.

Só proposta para o utilizador aprovar: NÃO mexe no jogo. Escreve apenas em arte/propostas/monstros/r05_gelo/:
  - <id>_parado_lado.png  (4 quadros "parado", o mesmo tamanho de quadro do desenho antigo)
  - comparar.gif          (antes | depois, a mexer)
  - depois.gif            (só os novos)

Fichas: docs/regioes/r05_gelo.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (Yeti Ancião, Dragão de Gelo).
Estilo: docs/ARTE.md secção 0 e o exemplo ferramentas/arte/ent_anciao.py (partes, textura, olhos com brilho).

Uso (na raiz do repositório):  python3 ferramentas/arte/propostas/r05_gelo.py [id ...]
"""
import math
import os
import random
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402,F401

SAIDA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r05_gelo')
ANTIGO = os.path.join(RAIZ, 'arte', 'regioes', 'r05_gelo')

OUT = '#2e222f'
BR = '#ffffff'
# ---- rampas (escuro -> claro), só Resurrect 64 ----
NEVE = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']          # pelo branco
NEVE_T = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0']        # pelo branco do lado de trás (mais escuro)
GELO = ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff']          # gelo azul
GELO_T = ['#323353', '#323353', '#484a77', '#4d65b4', '#4d9be6']
GELO_CL = ['#4d65b4', '#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff']       # gelo claro / transparente
CRISTAL = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']       # turquesa (gelo eterno)
CRISTAL_T = ['#0b5e65', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9']
AURORA_V = ['#0b5e65', '#0eaf9b', '#30e1b9', '#8ff8e2', '#ffffff']
AURORA_R = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']
AURORA_P = ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0']
LA = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#ab947a']            # lã de mamute
LA_T = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
MORSA = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#fdcbb0']
MORSA_T = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
MARFIM = ['#966c6c', '#ab947a', '#fdcbb0', '#ffffff', '#ffffff']
OSSO = ['#625565', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
PEDRA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
PELE_V = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']        # pele verde-acinzentada (tartaruga)
PELE_VT = ['#2e222f', '#313638', '#374e4a', '#547e64', '#92a984']
COURO = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
COURO_T = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
PRETO = ['#2e222f', '#2e222f', '#3e3546', '#625565', '#7f708a']
OURO = RAMPAS['ouro']
LARANJA = ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86']
VERM = ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790']
ROXO = RAMPAS['roxo']
AZUL_R = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']       # capa / tecidos azuis
MUSGO = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']


# ======================================================================
# utilidades
# ======================================================================

def px(P, pts, cor, z):
    """Píxeis de uma só cor (marcas, olhos, veios). Não fazem contorno próprio."""
    P.append(Parte({(int(x), int(y)) for x, y in pts}, None, z=z, separar=False, cor=cor))


def borda(m):
    return {p for p in m if any((p[0] + dx, p[1] + dy) not in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))}


def felpudo(m, s=0, baixo=3, cima=4, lados=0):
    """Pelo a sair da silhueta: tufos pendurados em baixo e pontas em cima (a borda deixa de ser lisa)."""
    m = set(m)
    b = borda(m)
    for (x, y) in sorted(b):
        if (x, y + 1) not in m and baixo and (x + s) % baixo == 0:
            m.add((x, y + 1))
            if (x + s) % (baixo * 2) == 0:
                m.add((x - 1, y + 1))
        if (x, y - 1) not in m and cima and (x + s) % cima == 0:
            m.add((x, y - 1))
        if lados and (x - 1, y) not in m and (y + s) % lados == 0:
            m.add((x - 1, y))
    return m


def pelo(P, m, escuro, claro, z, s=0, dens=9, comp=2, so_interior=True):
    """Textura de pelo: risquinhos na diagonal (escuros em baixo à direita, claros em cima à esquerda)."""
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    if not xs:
        return
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    rx, ry = max(1, (max(xs) - min(xs)) / 2), max(1, (max(ys) - min(ys)) / 2)
    dentro = m - borda(m) if so_interior else m
    esc, cla = [], []
    for (x, y) in dentro:
        h = (x * 5 + y * 11 + s * 7) % dens
        lado = (x - cx) / rx + (y - cy) / ry
        risco = [(x - i, y + i) for i in range(comp)]
        if h == 0 and lado > -0.4:
            esc += risco
        elif h == dens // 2 and lado < 0.1 and claro:
            cla += risco
    px(P, [p for p in esc if p in dentro], escuro, z + 0.001)
    if claro:
        px(P, [p for p in cla if p in dentro], claro, z + 0.002)


def la(P, m, escuro, claro, z, s=0, n=0.06, comp=(2, 4)):
    """Textura de lã/pelo comprido: fios verticais irregulares (escuros por todo o lado, claros só em cima à esquerda)."""
    rnd = random.Random(s)
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    rx, ry = max(1, (max(xs) - min(xs)) / 2), max(1, (max(ys) - min(ys)) / 2)
    dentro = m - borda(m)
    esc, cla = [], []
    for (x, y) in sorted(dentro):
        if rnd.random() < n:
            lado = (x - cx) / rx + (y - cy) / ry
            L = rnd.randint(*comp)
            fio = [(x + (1 if i >= L * 0.6 and rnd.random() < 0.3 else 0), y + i) for i in range(L)]
            if lado < -0.5 and rnd.random() < 0.6 and claro:
                cla += fio
            else:
                esc += fio
    px(P, [p for p in esc if p in dentro], escuro, z + 0.001)
    if claro:
        px(P, [p for p in cla if p in dentro], claro, z + 0.002)


def pintas(P, m, cor, z, s=0, dens=13, lado_min=None):
    """Pintas soltas (gelo baço, sujidade, escamas)."""
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    d = m - borda(m)
    pts = []
    for (x, y) in d:
        if (x * 7 + y * 3 + s * 11) % dens == 0:
            if lado_min is None or (x - cx) + (y - cy) > lado_min:
                pts.append((x, y))
    px(P, pts, cor, z)


def racha(P, x, y, passos, cor, z, s=0, dx=1, dy=1, dentro=None):
    """Uma racha de gelo em zig-zague."""
    rnd = random.Random(s)
    pts = []
    for _ in range(passos):
        pts.append((x, y))
        if rnd.random() < 0.5:
            x += dx
        else:
            y += dy
        if rnd.random() < 0.2:
            x -= dx
    if dentro is not None:
        pts = [p for p in pts if p in dentro]
    px(P, pts, cor, z)


def olho(P, x, y, iris, z=60, tam=1, fundo=OUT, fechado=False):
    """Olho de lado com brilho: tam 1 = 2×2 (íris + ponto branco); tam 2 = 3×3 com pupila; tam 3 = 4×3."""
    x, y = int(x), int(y)
    if fechado:
        px(P, [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)][:tam + 1], fundo, z)
        return
    if tam == 1:
        px(P, [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)], iris, z)
        px(P, [(x, y)], BR, z + 0.01)
    elif tam == 2:
        px(P, [(x + i, y + j) for i in range(3) for j in range(3)], iris, z)
        px(P, [(x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2), (x + 2, y + 2)], fundo, z + 0.01)
        px(P, [(x, y)], BR, z + 0.02)
    else:
        px(P, [(x + i, y + j) for i in range(4) for j in range(3)], iris, z)
        px(P, [(x + 2, y + 1), (x + 3, y + 1), (x + 2, y + 2), (x + 3, y + 2)], fundo, z + 0.01)
        px(P, [(x, y), (x + 1, y)], BR, z + 0.02)


def olho_brilho(P, x, y, cor, z=60, tam=1):
    """Olho que brilha (sem pupila): cor viva + ponto branco, num buraco escuro."""
    x, y = int(x), int(y)
    if tam == 1:
        px(P, [(x, y), (x + 1, y)], cor, z)
        px(P, [(x + 1, y)], BR, z + 0.01)
    else:
        px(P, [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 2, y - 1), (x - 1, y), (x + 2, y), (x - 1, y + 1),
               (x, y + 1), (x + 1, y + 1), (x + 2, y + 1)], OUT, z - 0.01)
        px(P, [(x, y), (x + 1, y)], cor, z)
        px(P, [(x + 1, y)], BR, z + 0.01)


def faceta(P, pts, rampa, z, separar=True):
    """Um bloco de gelo com faces: polígono pintado plano (claro em cima à esquerda) e uma aresta de brilho."""
    m = poligono(pts)
    P.append(Parte(m, rampa, z=z, plano=True, separar=separar))
    return m


def cristal(cx, base, alt, larg, incl=0.0):
    """Um cristal/estaca: losango comprido de pé (incl > 0 inclina para a direita)."""
    return [(cx - larg, base), (cx - larg * 0.7 + incl * alt * 0.6, base - alt * 0.7), (cx + incl * alt, base - alt),
            (cx + larg * 0.7 + incl * alt * 0.6, base - alt * 0.7), (cx + larg, base)]


def estrela_brilho(pontos, cor=BR, grande=False):
    """Brilho em cruz (por cima do desenho, sem contorno)."""
    r = []
    for x, y in pontos:
        r.append(((x, y), cor))
        if grande:
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r.append(((x + d[0], y + d[1]), '#8fd3ff' if cor == BR else cor))
    return r


def acabar(P, W, extras=(), H=None):
    """Desenha as partes e põe por cima os píxeis soltos (brilhos, flocos) sem contorno."""
    img = desenhar(P, W, H or W)
    for (x, y), c in extras:
        if 0 <= x < W and 0 <= y < (H or W):
            img.putpixel((int(x), int(y)), tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,))
    return img


def flocos(W, H, t, n, s, zona=None):
    """Flocos de neve a cair devagar (4 posições por ciclo)."""
    rnd = random.Random(s)
    r = []
    x0, y0, x1, y1 = zona or (0, 0, W - 1, H - 1)
    for i in range(n):
        x = rnd.randint(x0, x1)
        y = rnd.randint(y0, y1)
        yy = y0 + (y - y0 + t * 2 + i) % (y1 - y0 + 1)
        xx = x + (1 if (t + i) % 4 < 2 else 0)
        r.append(((xx, yy), BR if i % 3 else '#8fd3ff'))
    return r


RESP = [0, 0, 1, 1]        # respirar (sobe-desce) nos 4 quadros
ABANA = [0, 1, 0, -1]      # abanar (cauda, asas, tentáculos)


# ======================================================================
# MONSTROS
# ======================================================================

def lobo_de_gelo(t):
    """32×32: lobo branco esguio, crista de gelo no pescoço e dorso, focinho comprido, olho turquesa, bafo gelado."""
    P = []
    b = RESP[t]
    w = ABANA[t]
    # cauda farfalhuda (atrás, a abanar)
    cauda = capsula(7, 17 + b, 3, 14 + w, 2.2) | capsula(3, 14 + w, 2, 11 + w, 1.6)
    cauda = felpudo(cauda, 1, baixo=2, cima=2)
    P.append(Parte(cauda, NEVE, z=1))
    px(P, [(2, 10 + w), (1, 11 + w), (2, 11 + w)], '#8fd3ff', 1.1)          # ponta gelada
    # pernas do lado de trás (mais escuras)
    P.append(Parte(capsula(9, 21 + b, 7, 29, 1.3), NEVE_T, z=0.5, volume='cilindro_v'))
    P.append(Parte(capsula(21, 21 + b, 20, 29, 1.3), NEVE_T, z=0.5, volume='cilindro_v'))
    # corpo: peito fundo, barriga recolhida, anca; pernas da frente coladas (sem contorno no meio)
    corpo = poligono([(5, 17 + b), (10, 14.5 + b), (19, 14 + b), (24, 15 + b), (25, 21 + b), (21, 23.5 + b),
                      (15, 21.5 + b), (11, 22.5 + b), (6, 21 + b)])
    corpo |= elipse(9, 18.5 + b, 4, 4)
    corpo = felpudo(corpo, 2, baixo=3, cima=0)
    P.append(Parte(corpo, NEVE, z=2))
    for (x1, x2) in ((10, 11), (23, 23)):          # pernas da frente: coladas ao corpo, sem contorno
        perna = capsula(x1, 20 + b, x2, 29, 1.5) | elipse(x2 + 1, 29.6, 1.9, 1.1)
        P.append(Parte(perna, NEVE, z=2.05, volume='cilindro_v', separar=False))
    pelo(P, {p for p in corpo if 17 + b < p[1] < 23}, '#9babb2', None, 2, s=3, dens=6)
    px(P, [(13, 30), (25, 30)], '#4d65b4', 2.1)                           # unhas
    # crista de gelo (do pescoço para trás, a diminuir)
    for (cx_, cy_, al) in ((22, 14.5, 5), (19, 14.5, 4), (16, 14.5, 3), (13, 14.8, 2)):
        faceta(P, cristal(cx_, cy_ + b, al, 1.5, -0.45), GELO, 2.5)
    # cabeça com focinho comprido
    cab = elipse(25, 13 + b, 3.4, 3.3) | poligono([(25, 11.5 + b), (31.5, 14 + b), (31.5, 15.6 + b), (26, 16.6 + b)])
    P.append(Parte(cab, NEVE, z=4, luz=0.1))
    # orelhas altas e bicudas
    for ox in (23, 26):
        P.append(Parte(poligono([(ox - 1.3, 11 + b), (ox + 0.2, 5 + b), (ox + 1.8, 11 + b)]), NEVE, z=3.9 + (ox - 23) * 0.01))
    px(P, [(23, 9 + b), (23, 10 + b)], '#4d65b4', 3.95)
    # nariz, boca, presa
    px(P, [(31, 14 + b), (32, 14 + b), (31, 15 + b)], OUT, 4.2)
    px(P, [(x, 16 + b) for x in range(27, 31)], '#7f708a', 4.2)
    px(P, [(29, 17 + b)], BR, 4.3)
    # olho turquesa com brilho
    olho(P, 26, 12 + b, '#30e1b9', z=4.4, fechado=(t == 3))
    # pingentes de gelo no peito
    px(P, [(24, 22 + b), (24, 23 + b), (22, 23 + b)], '#8fd3ff', 4.5)
    ex = []
    if t in (1, 2):   # bafo gelado
        ex += [((31, 12 + b - t), BR), ((30, 11 + b - t), '#c7dcd0')]
    ex += estrela_brilho([(21, 10 + b + (t % 2))], BR) if t < 2 else []
    return acabar(P, 32, ex)


def urso_polar(t):
    """48×48: urso enorme e pesado, pelo em risquinhos, focinho escuro, garras, bafo; pinga gelo do queixo."""
    P = []
    b = RESP[t]
    # pernas do lado de trás
    P.append(Parte(capsula(12, 33, 11, 43, 3.2), NEVE_T, z=0.5, volume='cilindro_v'))
    P.append(Parte(capsula(31, 33, 32, 43, 3.2), NEVE_T, z=0.5, volume='cilindro_v'))
    # corpo: ancas, dorso alto (bossa do ombro), barriga
    corpo = elipse(18, 29 + b * 0.5, 13, 9.5) | elipse(28, 27 + b, 9, 9) | elipse(10, 30, 7, 8)
    corpo = felpudo(corpo, 1, baixo=2, cima=5)
    P.append(Parte(corpo, NEVE, z=2))
    pelo(P, {p for p in corpo if p[1] > 24}, '#9babb2', None, 2, s=1, dens=10, comp=3)
    # rabinho
    P.append(Parte(elipse(5, 25, 2, 2), NEVE, z=1.9))
    # pernas da frente (perto) com coxa
    P.append(Parte(capsula(12, 33, 14, 43, 3.6), NEVE, z=3.1, volume='cilindro_v', separar=False))
    P.append(Parte(capsula(34, 31 + b, 35, 43, 3.8), NEVE, z=3.1, volume='cilindro_v', separar=False))
    for x in (14, 35):
        pata = elipse(x + 1, 44, 4.2, 2.2)
        P.append(Parte(pata, NEVE, z=3.2, separar=False))
        px(P, [(x + 3, 45), (x + 5, 45), (x + 4, 44)][:2] + [(x + 1, 45)], '#3e3546', 3.3)   # garras
    px(P, [(15, 37), (16, 39), (36, 36 + b), (37, 38)], '#9babb2', 3.15)
    # cabeça (para a frente e um pouco abaixo do dorso)
    hy = 25 + b
    cab = elipse(38, hy, 6.2, 5.6) | capsula(40, hy + 2, 45, hy + 3, 3)
    P.append(Parte(cab, NEVE, z=4, luz=0.05))
    pelo(P, elipse(37, hy, 5, 4.6), '#9babb2', None, 4, s=6, dens=7)
    # orelha redonda
    P.append(Parte(elipse(35, hy - 5.5, 2.2, 2), NEVE, z=3.9))
    px(P, [(35, hy - 5)], '#7f708a', 3.95)
    # focinho: nariz preto brilhante, boca
    P.append(Parte(elipse(45.5, hy + 1.6, 1.8, 1.4), PRETO, z=4.3))
    px(P, [(45, hy + 1)], '#7f708a', 4.4)
    px(P, [(41, hy + 5), (42, hy + 5), (43, hy + 5), (44, hy + 4)], '#7f708a', 4.3)
    # olho pequeno escuro com brilho
    olho(P, 39, hy - 2, OUT, z=4.4, fechado=(t == 3))
    if t != 3:
        px(P, [(40, hy - 2), (40, hy - 1)], '#4d65b4', 4.41)
        px(P, [(39, hy - 2)], BR, 4.42)
    # gelo no pelo (pingentes no queixo e na barriga)
    px(P, [(38, hy + 6), (38, hy + 7), (40, hy + 6)], '#8fd3ff', 4.5)
    px(P, [(20, 39), (20, 40), (25, 39), (16, 38)], '#8fd3ff', 2.5)
    ex = []
    if t in (1, 2):
        ex += [((47, hy + 1 - t), BR), ((46, hy - t), '#c7dcd0'), ((47, hy - 1 - t), '#8fd3ff')]
    return acabar(P, 48, ex)


def golem_de_gelo(t):
    """48×48: blocos de gelo eterno (turquesa) facetados, núcleo azul que pulsa no peito, neve nos ombros,
    cristais a crescer das costas, punho enorme."""
    P = []
    b = RESP[t]
    nucleo = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    # perna e braço do lado de trás
    faceta(P, [(14, 32 + b), (21, 32 + b), (21, 45), (13, 45)], CRISTAL_T, 0.5)
    faceta(P, [(9, 17 + b), (15, 16 + b), (14, 29 + b), (8, 29 + b)], CRISTAL_T, 0.4)
    faceta(P, [(6, 28 + b), (14, 28 + b), (15, 35 + b), (7, 36 + b)], CRISTAL_T, 0.45)          # punho de trás
    # cristais grandes a sair das costas
    for (cx_, by, al, inc) in ((13, 15, 9, -0.35), (17, 12, 11, -0.15), (10, 20, 6, -0.6)):
        faceta(P, cristal(cx_, by + b, al, 2.2, inc), GELO_CL, 1)
    # tronco: bloco grande irregular
    tronco = [(12, 15 + b), (19, 9 + b), (31, 10 + b), (36, 16 + b), (34, 31 + b), (26, 35 + b), (15, 33 + b)]
    mt = faceta(P, tronco, CRISTAL, 2)
    # faces do bloco: tampo claro e lado direito escuro
    px(P, poligono([(19, 10 + b), (30, 11 + b), (28, 14 + b), (17, 14 + b)]), '#30e1b9', 2.1)
    px(P, poligono([(31, 11 + b), (35, 16 + b), (33, 30 + b), (30, 27 + b), (29, 14 + b)]), '#0b8a8f', 2.1)
    # rachas e bolhas presas no gelo
    racha(P, 15, 18 + b, 9, '#0b5e65', 2.2, s=3, dx=1, dy=1, dentro=mt)
    racha(P, 30, 25 + b, 6, '#0b5e65', 2.2, s=8, dx=-1, dy=1, dentro=mt)
    px(P, [(18, 27 + b), (21, 30 + b), (31, 18 + b), (17, 22 + b)], '#8ff8e2', 2.25)
    # núcleo azul (com moldura escura) no peito
    P.append(Parte(elipse(24.5, 21.5 + b, 4.4, 4.4), GELO, z=2.4))
    px(P, poligono([(24.5, 17.5 + b), (27.5, 21.5 + b), (24.5, 25.5 + b), (21.5, 21.5 + b)]), nucleo, 2.5)
    px(P, [(23, 20 + b)], BR, 2.6)
    # neve em cima dos ombros
    neve = felpudo(elipse(24, 9.5 + b, 8, 2.2) | elipse(14, 14.5 + b, 3.5, 1.8), 1, baixo=2, cima=0)
    P.append(Parte(neve, NEVE, z=2.7))
    # cabeça: bloco pequeno metido entre os ombros, olhos azuis numa racha escura
    faceta(P, [(26, 1 + b), (35, 2 + b), (38, 10 + b), (29, 12 + b), (25, 7 + b)], CRISTAL, 4.5)
    px(P, [(27, 2 + b), (28, 2 + b), (29, 2 + b), (30, 3 + b)], '#8ff8e2', 4.55)
    px(P, [(x, y + b) for x in range(29, 38) for y in (6, 7)], OUT, 4.6)
    if t != 3:
        px(P, [(31, 6 + b), (32, 6 + b), (31, 7 + b), (32, 7 + b), (35, 6 + b), (36, 6 + b), (35, 7 + b), (36, 7 + b)], '#8fd3ff', 4.7)
        px(P, [(31, 6 + b), (35, 6 + b)], BR, 4.8)
    px(P, [(x, 10 + b) for x in range(31, 36)], '#0b5e65', 4.6)       # boca
    # perna da frente com pé largo
    faceta(P, [(24, 32 + b), (32, 31 + b), (33, 42), (23, 42)], CRISTAL, 3.5)
    faceta(P, [(21, 41), (35, 41), (36, 46), (20, 46)], CRISTAL, 3.6)
    px(P, [(22, 42), (23, 42), (24, 42)], '#8ff8e2', 3.65)
    racha(P, 27, 34 + b, 5, '#0b5e65', 3.55, s=5, dx=1, dy=1)
    # braço da frente: ombro, antebraço e punho enorme até perto do chão
    faceta(P, [(31, 12 + b), (39, 11 + b), (41, 19 + b), (34, 21 + b)], CRISTAL, 4)
    faceta(P, [(35, 20 + b), (41, 19 + b), (42, 28 + b), (36, 29 + b)], CRISTAL, 4.1)
    faceta(P, [(33, 28 + b), (42, 27 + b), (45, 33 + b), (43, 39 + b), (34, 39 + b), (32, 34 + b)], CRISTAL, 4.2)
    px(P, [(x, y + b) for x in (37, 40) for y in (34, 35, 36, 37)], '#0b5e65', 4.25)   # dedos
    px(P, [(34, 29 + b), (35, 29 + b), (36, 29 + b)], '#8ff8e2', 4.25)
    for (cx_, al, inc) in ((39, 4, 0.1), (41, 6, 0.3)):   # cristais no ombro
        faceta(P, cristal(cx_, 13 + b, al, 1.4, inc), GELO_CL, 4.3)
    ex = estrela_brilho([(16 + t, 4 + b), (44, 30 + b - t % 2)], BR)
    if t == 2:
        ex += estrela_brilho([(24, 21 + b)], BR, grande=True)
    return acabar(P, 48, ex)


def espirito_da_neve(t):
    """32×32: fantasminha de neve a flutuar, cauda em espiral, olhos grandes, coroa de flocos a rodar."""
    P = []
    dy = [0, -1, -2, -1][t]
    # cauda em fumo de neve (vai fininha para trás e abana)
    w = ABANA[t]
    cauda = capsula(12, 18 + dy, 7, 22 + dy + w, 3) | capsula(7, 22 + dy + w, 3, 20 + dy + w * 2, 1.8) | elipse(3, 19 + dy + w * 2, 1.4, 1.4)
    P.append(Parte(cauda, GELO_CL, z=1))
    # corpo (gota grande)
    corpo = elipse(17, 15 + dy, 7.5, 7) | capsula(14, 18 + dy, 11, 21 + dy, 4)
    P.append(Parte(corpo, NEVE, z=2, luz=0.05))
    pintas(P, corpo, '#c7dcd0', 2.01, s=1, dens=9)
    # braços pequenos
    P.append(Parte(capsula(22, 19 + dy, 25, 20 + dy + w, 1.3), NEVE, z=2.02, separar=False))
    pelo(P, corpo, '#9babb2', None, 2.01, s=4, dens=11)
    # bochechas e cara
    olho(P, 18, 13 + dy, '#4d9be6', z=4, tam=2, fechado=(t == 3))
    olho(P, 22, 13 + dy, '#4d9be6', z=4, tam=2, fechado=(t == 3))
    px(P, [(17, 17 + dy), (23, 17 + dy)], '#eaaded', 4)
    px(P, [(20, 18 + dy), (21, 18 + dy)], '#4d65b4', 4)
    # coroa de flocos a rodar à volta
    ex = []
    for i in range(5):
        a = (t / 4 + i / 5) * 2 * math.pi
        x = 17 + math.cos(a) * 11
        y = 14 + dy + math.sin(a) * 4
        if math.sin(a) < -0.2:
            continue                       # atrás do corpo: não se vê
        ex += estrela_brilho([(int(x), int(y))], BR, grande=(i % 2 == 0))
    ex += flocos(32, 32, t, 3, 5, (2, 24, 29, 30))
    return acabar(P, 32, ex)


def harpia_gelida(t):
    """32×32: mulher-pássaro a planar, asas turquesa de penas de gelo, cara pálida de cabelo branco, garras amarelas."""
    P = []
    dy = [0, -1, 0, 1][t] + 5
    asa = [0, -2, -1, 1][t]
    # asa de trás (mais escura, levantada atrás)
    a2 = poligono([(15, 13 + dy), (12, 6 + dy + asa), (7, 1 + dy + asa), (4, 2 + dy + asa), (6, 7 + dy + asa // 2), (10, 14 + dy)])
    P.append(Parte(a2, CRISTAL_T, z=0.5))
    # cauda de penas
    for i, (ex_, ey_) in enumerate(((5, 17), (4, 20), (6, 22))):
        P.append(Parte(capsula(11, 16 + dy, ex_, ey_ + dy, 1.3), CRISTAL if i != 1 else GELO, z=1))
    # corpo de penas (peito claro)
    corpo = elipse(15, 15 + dy, 5, 4.2)
    P.append(Parte(corpo, CRISTAL, z=2))
    pelo(P, corpo, '#0b8a8f', '#8ff8e2', 2, s=2, dens=5)
    P.append(Parte(elipse(18, 16 + dy, 2.5, 3), GELO_CL, z=2.1, separar=False))
    # pernas com garras amarelas
    for x0 in (14, 17):
        px(P, [(x0, 19 + dy), (x0, 20 + dy), (x0, 21 + dy)], '#f79617', 1.5)
        px(P, [(x0 - 1, 22 + dy), (x0 + 1, 22 + dy), (x0, 22 + dy)], '#f9c22b', 1.6)
    # asa da frente (levantada para trás e para cima, sem tapar a cara)
    a1 = poligono([(17, 12 + dy), (14, 5 + dy + asa), (10, -0.5 + dy + asa), (6, -1 + dy + asa), (8, 4 + dy + asa // 2),
                   (10, 10 + dy), (13, 15 + dy)])
    P.append(Parte(a1, CRISTAL, z=3))
    for i in range(3):                          # penas (riscos escuros e pontas claras)
        x, y = 9 + i * 2, 2 + dy + asa + i
        px(P, [(x, y), (x + 1, y + 1), (x + 1, y + 2)], '#0b5e65', 3.01)
    px(P, [(6, -1 + dy + asa + 1), (7, 0 + dy + asa), (8, 0 + dy + asa)], BR, 3.02)
    # cabeça: cara pálida, cabelo branco a esvoaçar para trás
    cabelo = elipse(21, 7.8 + dy, 3.4, 2.4) | capsula(20, 7 + dy, 14, 7 + dy - ABANA[t], 1.2) | capsula(20, 8 + dy, 15, 11 + dy - ABANA[t], 1.2) | capsula(19, 9 + dy, 17, 14 + dy, 1.1)
    P.append(Parte(cabelo, NEVE, z=4))
    cara = elipse(22, 10.5 + dy, 3, 3) - elipse(21, 7.8 + dy, 3.6, 2.6)
    P.append(Parte(cara, ['#9babb2', '#c7dcd0', '#fdcbb0', '#fdcbb0', '#ffffff'], z=4.5))
    olho(P, 22, 10 + dy, '#30e1b9', z=5, fechado=(t == 2))
    px(P, [(25, 11 + dy), (25, 12 + dy), (26, 12 + dy)], '#f9c22b', 5)   # bico pequeno
    ex = estrela_brilho([(7, 0 + dy + asa)], BR) if t in (0, 1) else []
    ex += flocos(32, 32, t, 2, 9, (2, 24, 29, 30))
    return acabar(P, 32, ex)


def cacador_congelado(t):
    """32×32: caçador morto no gelo: capuz de pele com geada, cara azul congelada com um olho a brilhar,
    casaco rasgado com pingentes, aljava às costas e arco na mão."""
    P = []
    b = RESP[t]
    # aljava com flechas (atrás)
    P.append(Parte(capsula(11, 13 + b, 9, 21 + b, 1.6), COURO, z=0.2))
    px(P, [(10, 10 + b), (11, 9 + b), (12, 10 + b)], BR, 0.3)
    px(P, [(11, 11 + b), (11, 12 + b)], '#966c6c', 0.25)
    # perna e braço de trás
    P.append(Parte(capsula(14, 22, 13, 28, 1.5), COURO_T, z=0.5, volume='cilindro_v'))
    P.append(Parte(elipse(13.5, 29.5, 2.2, 1.2), PRETO, z=0.6))
    P.append(Parte(capsula(13, 14 + b, 12, 20 + b, 1.2), COURO_T, z=0.7))
    # casaco comprido rasgado, com orla de pele
    casaco = poligono([(12, 12 + b), (19, 12 + b), (21, 24), (10, 24)])
    casaco -= {(11, 24), (14, 24), (15, 23), (19, 24), (20, 24)}
    P.append(Parte(casaco, COURO, z=2, volume='cilindro_v'))
    pelo(P, casaco, '#45293f', None, 2, s=2, dens=6)
    P.append(Parte(felpudo(capsula(12, 22.5, 19, 22.5, 0.9), 1, baixo=2, cima=0), NEVE_T, z=2.2, separar=False))
    P.append(Parte(capsula(14, 18 + b, 19, 18 + b, 0.6), PRETO, z=2.3, separar=False))       # cinto
    px(P, [(17, 18 + b)], '#9babb2', 2.35)                                                      # fivela
    # perna da frente com bota
    P.append(Parte(capsula(18, 23, 19, 28, 1.6), COURO, z=2.5, volume='cilindro_v'))
    P.append(Parte(elipse(20, 29.5, 2.4, 1.3), PRETO, z=2.6))
    # capuz de pele (com geada) e cara congelada
    capuz = felpudo(elipse(17, 8 + b, 4.6, 4.6), 0, baixo=0, cima=2, lados=2)
    P.append(Parte(capuz, NEVE, z=3))
    pintas(P, capuz, '#8fd3ff', 3.01, s=3, dens=5)
    cara = elipse(19.5, 9 + b, 2.6, 3)
    P.append(Parte(cara, CRISTAL, z=3.5, luz=0.15))
    px(P, [(18, 8 + b), (19, 8 + b)], OUT, 3.6)
    px(P, [(20, 8 + b), (21, 8 + b)], '#30e1b9' if t != 2 else '#8ff8e2', 3.6)               # olho a brilhar
    px(P, [(21, 8 + b)], BR, 3.7)
    px(P, [(19, 11 + b), (20, 11 + b), (21, 11 + b)], '#323353', 3.6)                         # boca
    px(P, [(19, 12 + b), (21, 12 + b), (21, 13 + b)], '#8fd3ff', 3.7)                         # pingentes (barba)
    # braço da frente com o arco
    P.append(Parte(capsula(17, 14 + b, 22, 17 + b, 1.3), COURO, z=4))
    arco = {(23, y) for y in range(10 + b, 25 + b)} | {(24, y) for y in range(12 + b, 23 + b)} | {(25, y) for y in range(14 + b, 21 + b)}
    arco -= {(23, y) for y in range(12 + b, 23 + b)} | {(24, y) for y in range(14 + b, 21 + b)}
    P.append(Parte(arco, ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], z=4.5, plano=True))
    px(P, [(23, 10 + b), (23, 24 + b)], '#ab947a', 4.6)
    px(P, [(22, y) for y in range(11 + b, 24 + b)], '#c7dcd0', 4.4)                          # corda
    P.append(Parte(elipse(22.5, 17 + b, 1.4, 1.4), GELO_CL, z=4.7))                          # mão congelada
    # geada nos ombros e pingentes no casaco
    px(P, [(13, 12 + b), (14, 12 + b), (18, 12 + b)], '#c7dcd0', 3.2)
    ex = [((12, 25 + (t % 2)), '#8fd3ff'), ((16, 24 + ((t + 1) % 3)), '#8fd3ff')]
    if t in (1, 2):
        ex += [((23, 10 + b - t), '#c7dcd0')]                                                     # bafo frio
    return acabar(P, 32, ex)


def pinguim_guerreiro(t):
    """32×32 (pequeno): pinguim de capacete de concha e lança de gelo, bamboleia de um lado para o outro."""
    P = []
    lean = [0, 1, 0, -1][t]
    COSTAS = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#8fd3ff']
    # lança de gelo (atrás do corpo, na asa da frente)
    px(P, [(25, y) for y in range(12, 31)], '#966c6c', 1)
    P.append(Parte(poligono([(23.5, 12), (25.5, 5), (27.5, 12)]), GELO_CL, z=1.1))
    px(P, [(24, 12), (26, 12), (25, 13)], '#ab947a', 1.2)
    # pés
    P.append(Parte(elipse(16, 30, 2.2, 1.2), LARANJA, z=0.5))
    # corpo inteiro (cabeça + corpo, sem pescoço), a bambolear
    corpo = elipse(18 + lean * 0.5, 23.5, 5.6, 6.6) | elipse(19 + lean, 17, 4.2, 4)
    P.append(Parte(corpo, COSTAS, z=2))
    barriga = (elipse(20.5 + lean * 0.6, 24, 3.4, 5.6) | elipse(21 + lean, 18.5, 2.4, 2.2)) & corpo
    P.append(Parte(barriga, NEVE, z=2.1, separar=False))
    P.append(Parte(elipse(21, 30, 2.4, 1.2), LARANJA, z=2.5))
    hx = 19 + lean
    # olho com anel branco e brilho
    px(P, [(hx + 1, 15), (hx + 2, 15), (hx + 1, 16), (hx + 2, 16)], BR, 3.2)
    px(P, [(hx + 2, 16)], OUT, 3.3)
    px(P, [(hx + 2, 15)], '#4d65b4', 3.3)
    P.append(Parte(poligono([(hx + 3.5, 16), (hx + 7.5, 17.4), (hx + 3.5, 18.6)]), LARANJA, z=3.4))    # bico
    # capacete de concha (com estrias)
    concha = {p for p in elipse(hx - 0.3, 14.2, 4.8, 3.4) if p[1] <= 13}
    P.append(Parte(concha, ['#966c6c', '#e6904e', '#fca790', '#fdcbb0', '#ffffff'], z=3.5))
    for i in (-3, -1, 1, 3):
        px(P, [(hx + i, 13), (hx + i + (1 if i > 0 else -1), 12)], '#cd683d', 3.51)
    # asa da frente a segurar a lança
    P.append(Parte(capsula(17 + lean * 0.5, 20, 24, 22, 1.3), COSTAS, z=4))
    px(P, [(25, 21), (25, 22)], '#ab947a', 4.1)
    ex = []
    if t == 0:
        ex += estrela_brilho([(25, 7)], BR)
    if t == 2:
        ex += estrela_brilho([(24, 9)], BR)
    return acabar(P, 32, ex)


def _mamute(t, W, anciao=False):
    """Mamute de lã castanha, de lado (64 = jovem; 128 = Ancião com musgo, pássaros e presas enormes).
    Desenhado numa grelha de 64 e escalado por k nas coordenadas (não nos píxeis)."""
    k = W / 64
    P = []
    b = RESP[t] * (1 if W == 64 else 2)
    w = ABANA[t]

    def S(x, y):
        return x * k, y * k
    # pernas do lado de trás
    for x in (14, 41):
        P.append(Parte(capsula(*S(x, 44), *S(x - 0.5, 57), 4.2 * k), LA_T, z=0.5, volume='cilindro_v'))
    # cauda com tufo
    P.append(Parte(capsula(*S(8, 37), *S(5, 45 + w), 1.0 * k), LA, z=0.6))
    P.append(Parte(felpudo(elipse(*S(5, 46 + w), 1.6 * k, 2 * k), 1), LA_T, z=0.7))
    # corpo: dorso alto à frente (bossa), ancas mais baixas
    corpo = elipse(*S(25, 39), 17 * k, 10.5 * k) | elipse(*S(37, 34), 11 * k, 10 * k) | elipse(*S(12, 40), 6 * k, 8 * k)
    corpo = {(x, y + b) for x, y in corpo}
    # franja de lã comprida pendurada da barriga
    franja = set()
    for i, x in enumerate(range(int(10 * k), int(48 * k), max(1, int(2 * k)))):
        topo = max(y for (xx, y) in corpo if xx == x) if any(xx == x for xx, _ in corpo) else int(46 * k)
        franja |= capsula(x, topo - 2 * k, x - 0.6 * k, topo + (2 + (i * 5) % 4) * k, 0.9 * k)
    corpo |= franja
    corpo = felpudo(corpo, 1, baixo=2, cima=3)
    P.append(Parte(corpo, LA, z=2))
    la(P, corpo, '#694f62', '#ab947a', 2, s=1, n=0.07, comp=(2, int(3 * k + 1)))
    la(P, corpo, '#45293f', None, 2.0005, s=9, n=0.025, comp=(2, int(3 * k)))
    # musgo, neve e pássaros nas costas (o Ancião)
    if anciao:
        rnd = random.Random(4)
        for (mx, my, rx, ry) in ((21, 30.5, 7, 2.6), (32, 26.5, 6, 2.2), (12, 34, 4, 2.2)):
            mm = {(x, y + b) for (x, y) in elipse(*S(mx, my), rx * k, ry * k)}
            mm = {p for p in felpudo(mm, 2, baixo=2, cima=2) if rnd.random() < 0.92}
            P.append(Parte(mm, MUSGO, z=2.5))
            pintas(P, mm, '#d5e04b', 2.51, s=int(mx), dens=7)
        P.append(Parte(felpudo({(x, y + b) for (x, y) in elipse(*S(40, 25.5), 4.5 * k, 1.3 * k)}, 0, baixo=2, cima=0), NEVE, z=2.6))
        # cogumelinhos / flores de neve no musgo
        for (fx, fy) in ((17, 26.5), (24, 26.5)):
            X, Y = S(fx, fy)
            px(P, [(X, Y + b), (X + 1, Y + b - 1), (X - 1, Y + b - 1), (X, Y + b - 2)], BR, 2.62)
            px(P, [(X, Y + b - 1)], '#f9c22b', 2.63)
        # dois pássaros (pisco-de-peito-ruivo) a saltitar nas costas
        for i, (bx, by) in enumerate(((20, 26.5), (31, 22.5))):
            X, Y = S(bx, by)
            hop = 2 if (t + i) % 4 == 1 else 0
            Y = Y + b - hop
            P.append(Parte(capsula(X - 5, Y - 1, X - 8, Y + 1, 1.3), PEDRA, z=2.79))       # cauda
            P.append(Parte(elipse(X, Y, 4.2, 3.4), PEDRA, z=2.8))
            P.append(Parte(elipse(X + 2, Y + 1, 2.4, 2.2), LARANJA, z=2.81, separar=False))  # peito ruivo
            P.append(Parte(elipse(X + 3, Y - 3.5, 2.8, 2.6), PEDRA, z=2.82))
            px(P, [(X + 4, Y - 4)], OUT, 2.83)
            px(P, [(X + 4, Y - 5)], BR, 2.84)
            px(P, [(X + 6, Y - 3), (X + 7, Y - 3)], '#f79617', 2.83)
            px(P, [(X - 2, Y - 1), (X - 1, Y), (X - 3, Y)], '#3e3546', 2.83)            # asa
            px(P, [(X, Y + 3), (X, Y + 4), (X + 2, Y + 3), (X + 2, Y + 4)], '#f79617', 2.78)  # patas
    # pernas da frente (perto) com unhas claras
    for x in (18, 44):
        perna = capsula(*S(x, 44 + b / k), *S(x + 0.5, 57.5), 4.4 * k)
        P.append(Parte(perna, LA, z=3, volume='cilindro_v', separar=False))
        la(P, perna, '#694f62', None, 3, s=x, n=0.08, comp=(2, 3))
        pe = elipse(*S(x + 0.8, 58.5), 4.8 * k, 2 * k)
        P.append(Parte(pe, LA_T, z=3.1))
        X, Y = S(x + 0.8, 59.5)
        for d in (-2.5, 0, 2.5):
            px(P, [(X + d * k + i, Y) for i in range(int(k))] + ([(X + d * k, Y - 1)] if k > 1 else []), '#c7dcd0', 3.2)
    # cabeça em cúpula, testa alta
    hx, hy = 48, 33
    cab = elipse(*S(hx, hy), 8.5 * k, 9.5 * k) | elipse(*S(hx - 2, hy - 7), 5.5 * k, 4 * k)
    cab = {(x, y + b) for x, y in cab}
    cab = felpudo(cab, 2, baixo=0, cima=2)
    P.append(Parte(cab, LA, z=4, luz=0.05))
    la(P, cab, '#694f62', '#ab947a', 4, s=3, n=0.06, comp=(2, int(2 * k + 1)))
    # orelha pequena
    P.append(Parte({(x, y + b) for x, y in elipse(*S(42.5, 33), 2 * k, 3 * k)}, LA, z=4.1))
    X, Y = S(48, 28.5)
    px(P, [(X + i, Y + b) for i in range(int(4 * k))], '#45293f', 4.4)                  # sobrolho
    # olho com brilho e pestanas
    X, Y = S(51, 31)
    olho(P, X, Y + b, OUT, z=4.5, tam=1 if k == 1 else 3, fechado=(t == 3))
    if t != 3:
        px(P, [(X + 1, Y + b)] if k == 1 else [(X + 2, Y + b + 1), (X + 3, Y + b + 1), (X + 2, Y + b + 2)], '#2e222f', 4.51)
        px(P, [(X, Y + b)] if k == 1 else [(X + 2, Y + b + 1)], BR, 4.52)
    # tromba (curva para a frente e enrola no fim, a abanar)
    tw = w * 0.8
    tromba = capsula(*S(53, 37 + b / k), *S(56 + tw * 0.5, 47), 3 * k) | capsula(*S(56 + tw * 0.5, 47), *S(56 + tw, 55), 2.2 * k) \
        | capsula(*S(56 + tw, 55), *S(59 + tw, 56.5), 1.7 * k)
    # presas de marfim (curvas)
    if anciao:
        presa = capsula(*S(52, 42 + b / k), *S(57, 50), 2 * k) | capsula(*S(57, 50), *S(61, 48.5), 1.6 * k) | capsula(*S(61, 48.5), *S(62, 43), 1.2 * k)
    else:
        presa = capsula(*S(52, 43 + b / k), *S(57, 48), 1.6 * k) | capsula(*S(57, 48), *S(61, 46), 1.3 * k)
    P.append(Parte(presa, MARFIM, z=5.2, volume='cilindro_h'))
    P.append(Parte(tromba, LA, z=5, volume='cilindro_v'))
    for i in range(5):                          # rugas da tromba
        X, Y = S(55 + i * 0.3 + tw * i * 0.15, 42 + i * 3)
        px(P, [(X - 1, Y), (X, Y), (X + 1 * k, Y)], '#694f62', 5.01)
    ex = []
    if t in (1, 2):
        X, Y = S(60, 54)
        ex += [((X + w, Y - t * k), '#c7dcd0')]
    return acabar(P, W, ex)


def mamute_jovem(t):
    """64×64: mamute jovem de lã castanha, presas pequenas, tromba a abanar, franja de lã."""
    return _mamute(t, 64)


def mamute_anciao_tundra(t):
    """128×128: mamute gigante e pacífico, presas enormes enroladas, musgo e flores nas costas, dois pássaros."""
    return _mamute(t, 128, anciao=True)


def presa_branca(t):
    """64×64: lobo branco enorme, juba farfalhuda, cicatrizes azuis que brilham (no flanco e sobre o olho),
    presas de fora, bafo gelado."""
    P = []
    b = RESP[t]
    w = ABANA[t]
    cic = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    # cauda grande e farfalhuda
    cauda = capsula(12, 36 + b, 6, 30 + w, 4) | capsula(6, 30 + w, 5, 22 + w * 2, 3.2) | elipse(5, 21 + w * 2, 2.4, 2.4)
    cauda = felpudo(cauda, 1, baixo=2, cima=2, lados=2)
    P.append(Parte(cauda, NEVE, z=1))
    la(P, cauda, '#9babb2', None, 1, s=2, n=0.08)
    px(P, [(5, 19 + w * 2), (4, 20 + w * 2), (6, 20 + w * 2)], '#8fd3ff', 1.1)
    # pernas do lado de trás
    P.append(Parte(capsula(17, 44 + b, 14, 52, 2.6) | capsula(14, 52, 16, 58, 2.2), NEVE_T, z=0.5, volume='cilindro_v'))
    P.append(Parte(capsula(43, 44 + b, 42, 58, 2.6), NEVE_T, z=0.5, volume='cilindro_v'))
    for x in (17, 43):
        P.append(Parte(elipse(x, 59, 3.2, 1.8), NEVE_T, z=0.6))
    # corpo
    corpo = poligono([(11, 35 + b), (21, 28 + b), (40, 27 + b), (49, 30 + b), (50, 42 + b), (43, 47 + b), (32, 43 + b),
                      (22, 45 + b), (12, 42 + b)])
    corpo |= elipse(19, 38 + b, 8, 7.5)
    corpo = felpudo(corpo, 2, baixo=2, cima=4)
    P.append(Parte(corpo, NEVE, z=2))
    la(P, corpo, '#9babb2', None, 2, s=5, n=0.06, comp=(2, 3))
    # cicatrizes do flanco (três garras) a brilhar
    for i in range(3):
        x0, y0 = 26 + i * 4, 31 + b
        risco = [(x0 + j // 2, y0 + j) for j in range(10)]
        px(P, risco + [(x + 1, y) for x, y in risco], '#4d65b4', 2.2)
        px(P, risco[1:-1], cic, 2.21)
    # pernas da frente (perto): a de trás com jarrete, a da frente direita
    P.append(Parte(capsula(20, 44 + b, 17, 51, 3) | capsula(17, 51, 20, 58, 2.5), NEVE, z=2.05, volume='cilindro_v', separar=False))
    P.append(Parte(capsula(46, 42 + b, 47, 58, 3.2), NEVE, z=2.05, volume='cilindro_v', separar=False))
    for x in (21, 48):
        P.append(Parte(elipse(x, 59, 3.6, 2), NEVE, z=2.1))
        px(P, [(x + 2, 60), (x + 4, 60), (x, 60)], '#3e3546', 2.15)              # garras
    px(P, [(45, 50), (45, 52), (19, 53)], '#9babb2', 2.06)
    # juba à volta do pescoço
    juba = felpudo(elipse(44, 31 + b, 8.5, 10), 3, baixo=2, cima=2, lados=2)
    P.append(Parte(juba, NEVE, z=3))
    la(P, juba, '#9babb2', BR, 3, s=7, n=0.1, comp=(2, 4))
    px(P, [(44, 41 + b), (44, 42 + b), (47, 41 + b), (40, 40 + b), (40, 41 + b)], '#8fd3ff', 3.1)   # pingentes
    # cabeça e focinho
    cab = elipse(50, 25 + b, 7, 6.5) | poligono([(50, 20.5 + b), (62.5, 27 + b), (62.5, 30 + b), (52, 32.5 + b)])
    P.append(Parte(cab, NEVE, z=4, luz=0.08))
    # orelhas
    P.append(Parte(poligono([(45, 21 + b), (47, 10 + b), (51, 20 + b)]), NEVE, z=3.9))
    P.append(Parte(poligono([(50, 20 + b), (53, 11 + b), (55.5, 20.5 + b)]), NEVE, z=3.95))
    px(P, [(48, 15 + b), (48, 16 + b), (48, 17 + b), (49, 18 + b)], '#4d65b4', 3.96)
    # nariz, boca com presas
    P.append(Parte(elipse(62, 27.5 + b, 1.6, 1.4), PRETO, z=4.2))
    px(P, [(x, 31 + b - (1 if x > 59 else 0)) for x in range(53, 62)], '#625565', 4.2)
    px(P, [(56, 32 + b), (56, 33 + b), (59, 31 + b), (59, 32 + b)], BR, 4.3)
    # olho azul a brilhar e cicatriz por cima do olho
    olho(P, 53, 23 + b, '#4d9be6', z=4.4, tam=2, fechado=(t == 3))
    px(P, [(52, 22 + b), (53, 22 + b), (54, 22 + b), (55, 21 + b)], '#7f708a', 4.35)   # sobrolho
    px(P, [(51, 19 + b), (52, 20 + b), (53, 21 + b)] + [(55, 27 + b), (56, 28 + b)], '#4d65b4', 4.45)
    px(P, [(52, 20 + b), (55, 27 + b)], cic, 4.46)
    ex = []
    if t in (1, 2):
        ex += [((63, 25 + b - t), BR), ((62, 24 + b - t), '#c7dcd0'), ((63, 23 + b - t), '#8fd3ff')]
    ex += estrela_brilho([(30 + t * 2, 33 + b + t)], BR) if t % 2 == 0 else []
    return acabar(P, 64, ex)


# ======================================================================
# GUARDIÕES
# ======================================================================

FANT = ['#484a77', '#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff']           # branco fantasma (sombra azulada)
FANT_T = ['#323353', '#4d65b4', '#8fd3ff', '#c7dcd0', '#c7dcd0']


def esbater(img, y0, y1, forca=0.85):
    """Meio transparente: tira píxeis com um padrão regular, cada vez mais para baixo (de y0 a y1)."""
    from motor import _BAYER
    out = img.copy()
    p = out.load()
    w, h = out.size
    for y in range(max(0, y0), min(h, y1 + 1)):
        f = (y - y0) / max(1, (y1 - y0)) * forca
        for x in range(w):
            if p[x, y][3] and _BAYER[y % 4][x % 4] < f * 16:
                p[x, y] = (0, 0, 0, 0)
    return out


def alce_fantasma(t):
    """48×48: alce branco meio transparente (as patas desfazem-se em névoa), chifres largos de gelo, olho turquesa."""
    P = []
    b = [0, -1, -1, 0][t]
    # pernas do lado de trás
    for (x1, x2) in ((14, 13), (32, 33)):
        P.append(Parte(capsula(x1, 30 + b, x2, 45, 1.7), FANT_T, z=0.5, volume='cilindro_v'))
    # cauda curta
    P.append(Parte(elipse(8, 24 + b, 2, 2.4), FANT, z=0.7))
    # corpo: dorso com bossa no ombro
    corpo = elipse(20, 27 + b, 12, 6.5) | elipse(30, 24 + b, 7.5, 7.5)
    corpo = felpudo(corpo, 1, baixo=3, cima=0)
    P.append(Parte(corpo, FANT, z=2))
    la(P, corpo, '#8fd3ff', None, 2, s=3, n=0.05)
    # pernas da frente
    for (x1, x2) in ((17, 16), (35, 36)):
        P.append(Parte(capsula(x1, 30 + b, x2, 45, 1.9), FANT, z=2.05, volume='cilindro_v', separar=False))
        px(P, [(x2, 37), (x2, 38)], '#8fd3ff', 2.06)                                    # joelho
    # pescoço e cabeça comprida com focinho caído
    P.append(Parte(capsula(33, 23 + b, 39, 21 + b, 4), FANT, z=3, separar=False))
    cab = capsula(37, 19 + b, 44, 24 + b, 3.2) | elipse(44.5, 25 + b, 3.2, 3)
    P.append(Parte(cab, FANT, z=3.5, luz=0.08))
    P.append(Parte(capsula(38, 27 + b, 38, 31 + b, 1.3), FANT, z=3.4))               # barbela
    px(P, [(46, 25 + b), (47, 25 + b)], '#4d65b4', 3.6)                                 # narina
    px(P, [(43, 28 + b), (44, 28 + b), (45, 28 + b)], '#8fd3ff', 3.6)                   # boca
    # orelha
    P.append(Parte(poligono([(36, 18 + b), (33, 15 + b), (34, 19 + b)]), FANT, z=3.3))
    # olho turquesa
    olho_brilho(P, 40, 20 + b, '#30e1b9' if t != 2 else '#8ff8e2', z=3.8)
    # chifres largos (palmas de gelo com pontas de cristal)
    palma2 = poligono([(38, 16 + b), (41, 10 + b), (42, 6 + b), (44, 8 + b), (45, 4 + b), (46, 9 + b), (43, 15 + b)])
    P.append(Parte(palma2, GELO, z=1.5, plano=True))                                        # o chifre do outro lado
    palma = poligono([(37, 16 + b), (31, 13 + b), (25, 11 + b), (21, 7 + b), (24, 7.5 + b), (24, 3 + b), (27, 7 + b),
                      (28, 2 + b), (30, 7 + b), (32, 2 + b), (33, 8 + b), (35, 4 + b), (36, 10 + b), (39, 16 + b)])
    P.append(Parte(palma, GELO_CL, z=3.2, plano=True))
    px(P, [(26, 10 + b), (28, 10 + b), (30, 11 + b), (32, 12 + b), (34, 13 + b)], '#4d65b4', 3.21)
    px(P, [(21, 7 + b), (24, 3 + b), (28, 2 + b), (32, 2 + b), (35, 4 + b)], BR, 3.22)
    img = acabar(P, 48, [])
    img = esbater(img, 36, 47, 0.8)                     # as patas desfazem-se em névoa
    # fiapos de névoa a sair (por cima, sem contorno)
    ex = []
    for i, (x, y) in enumerate(((10, 30), (24, 35), (6, 22), (42, 33))):
        yy = y + b - (t + i) % 4
        ex += [((x + (t + i) % 2, yy), '#c7dcd0'), ((x, yy - 1), '#8fd3ff')]
    ex += estrela_brilho([(29 + t, 3 + b)], BR) if t % 2 == 0 else []
    for (x, y), c in ex:
        img.putpixel((x, y), tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,))
    return img


def _tentaculo(cx, base, alt, lado, fase, r0, r1):
    """Um tentáculo a sair do buraco: sobe, abre para o lado (lado = -1 esquerda, 1 direita), abana com a fase
    e enrola na ponta para dentro."""
    pts = []
    n = 12
    for i in range(n + 1):
        u = i / n
        x = cx + lado * (u ** 1.4) * 9 + math.sin(u * 3 + fase) * 1.6 * u
        y = base - u * alt
        pts.append((x, y))
    ex, ey = pts[-1]
    for j in range(1, 5):                      # caracol na ponta
        a = j * 0.85
        pts.append((ex - lado * (1 - math.cos(a)) * 2.6, ey - math.sin(a) * 2.6))
    m = set()
    for i in range(len(pts) - 1):
        r = r0 + (r1 - r0) * (i / (len(pts) - 1))
        m |= capsula(*pts[i], *pts[i + 1], r)
    return m, pts


def kraken_do_gelo(t):
    """64×64: kraken a sair de um buraco no gelo: cabeça turquesa com geada, olho amarelo enorme, tentáculos
    com ventosas a abrir para os lados e a abanar."""
    P = []
    f = t * math.pi / 2
    agua_y = 55
    rb = RESP[t]
    # gelo à volta do buraco e a água escura
    P.append(Parte(elipse(32, 56, 30, 7.5), GELO_CL, z=0, plano=True))
    P.append(Parte(elipse(32, 56, 24, 4.8), None, z=0.1, separar=False, cor='#323353'))
    px(P, [(x, 55) for x in range(14, 50, 5)], '#0b5e65', 0.2)
    # tentáculos de trás (mais escuros, altos)
    for (cx, alt, lado, fs) in ((19, 40, -1, 0), (45, 42, 1, 1.5)):
        m, _ = _tentaculo(cx, agua_y, alt, lado, f + fs, 3.4, 1.0)
        P.append(Parte(m, CRISTAL_T, z=0.5))
    # cabeça (manto) a sair da água
    cab = {p for p in elipse(32, 33 + rb, 13, 15) if p[1] <= agua_y} | elipse(31, 22 + rb, 11.5, 11)
    P.append(Parte(cab, CRISTAL, z=1))
    pintas(P, cab, '#0b8a8f', 1.01, s=2, dens=9)
    # geada e pingentes no topo
    gea = felpudo({p for p in elipse(29, 14 + rb, 9, 3.6) if p in cab}, 1, baixo=2, cima=0)
    P.append(Parte(gea, NEVE, z=1.5, separar=False))
    px(P, [(23, 17 + rb), (23, 18 + rb), (34, 18 + rb), (37, 17 + rb), (37, 18 + rb)], '#8fd3ff', 1.6)
    # olho grande do lado de cá e outro a espreitar
    y = 32 + rb
    px(P, elipse(40.5, y, 5, 3.8), OUT, 2)
    if t != 3:
        px(P, elipse(40.5, y, 4, 2.8), '#f9c22b', 2.1)
        px(P, [p for p in elipse(40.5, y, 4, 2.8) if p[1] >= y + 1], '#f79617', 2.15)
        px(P, [(x, y) for x in range(39, 44)], OUT, 2.2)        # pupila em risca
        px(P, [(38, y - 2), (39, y - 2)], BR, 2.3)
    else:
        px(P, [(x, y) for x in range(37, 45)], '#f79617', 2.1)
    px(P, [(x, y - 4 - (1 if x < 40 else 0)) for x in range(35, 45)], '#0b5e65', 2.05)  # sobrolho
    px(P, [(27, y - 1), (28, y - 1), (27, y), (28, y)], '#f9c22b', 2.1)
    px(P, [(28, y)], OUT, 2.2)
    # tentáculos da frente com ventosas (para os lados, sem tapar a cara)
    for i, (cx, alt, lado, fs) in enumerate(((14, 30, -1, 0.8), (50, 32, 1, 2.4), (24, 14, -1, 3.6))):
        m, pts = _tentaculo(cx, agua_y + 1, alt, lado, f + fs, 3.8, 1.2)
        P.append(Parte(m, CRISTAL, z=3 + i * 0.1))
        vs = [(x + lado * 2.4, yy) for (x, yy) in pts[1:-5:2]]
        px(P, [p for p in {(int(a), int(b)) for a, b in vs} if p in m], '#8ff8e2', 3.05 + i * 0.1)
    # gelo da frente (borda do buraco tapa a base dos tentáculos)
    anel = elipse(32, 56, 30, 7.5)
    frente = {p for p in anel if p[1] >= 59 or (p[1] >= 56 and (p[0] < 9 or p[0] > 55))}
    P.append(Parte(frente, GELO_CL, z=5, plano=True))
    px(P, [(x, 61) for x in range(8, 56, 7)], '#4d9be6', 5.1)
    ex = [((14 + t * 9, 54 + (t % 2)), '#8fd3ff'), ((47 - t * 5, 55), BR)]
    return acabar(P, 64, ex)


def coracao_de_cristal_azul(t):
    """48×48: figura de gelo a flutuar: cabeça de cristal com olhos a brilhar, peito de cristal turquesa com um
    coração azul que bate, cauda de lascas e estilhaços a rodar à volta."""
    P = []
    dy = [0, -1, -1, 0][t]
    bate = t in (1, 2)
    # estilhaços em órbita (atrás e à frente)
    orb = []
    for i in range(6):
        a = (t / 4 + i / 6) * 2 * math.pi
        x = 24 + math.cos(a) * 20
        y = 23 + dy + math.sin(a) * 5
        orb.append((x, y, math.sin(a) > 0))
    for (x, y, frente) in orb:
        if not frente:
            P.append(Parte(poligono([(x - 1.5, y), (x, y - 3), (x + 1.5, y), (x, y + 2)]), CRISTAL_T, z=0.2, plano=True))
    # cauda de lascas
    for (x1, y1, x2, y2, r) in ((24, 32, 24, 41, 2.6), (22, 33, 19, 39, 1.6), (26, 33, 29, 38, 1.6)):
        P.append(Parte(poligono([(x1 - r, y1 + dy), (x1 + r, y1 + dy), (x2, y2 + dy)]), CRISTAL, z=1, plano=True))
    # braços de lascas a flutuar
    for s in (-1, 1):
        x0 = 24 + s * 11
        P.append(Parte(poligono([(x0 - 2, 15 + dy), (x0 + 2, 15 + dy), (x0 + s * 2, 26 + dy - t % 2), (x0 - s * 1, 24 + dy)]),
                       CRISTAL if s > 0 else CRISTAL_T, z=1.5 if s < 0 else 4, plano=True))
    # peito de cristal facetado
    peito = [(15, 15 + dy), (24, 11 + dy), (33, 15 + dy), (31, 27 + dy), (24, 34 + dy), (17, 27 + dy)]
    P.append(Parte(poligono(peito), CRISTAL, z=2, plano=True))
    px(P, poligono([(15, 15 + dy), (24, 11 + dy), (24, 16 + dy), (18, 17 + dy)]), '#30e1b9', 2.1)
    px(P, poligono([(31, 17 + dy), (33, 15 + dy), (31, 27 + dy), (28, 27 + dy)]), '#0b8a8f', 2.1)
    px(P, [(18, 17 + dy), (19, 20 + dy), (20, 24 + dy), (21, 28 + dy)], '#8ff8e2', 2.15)
    # o coração azul (bate: cresce um píxel)
    r = 5 if bate else 4
    cor = elipse(24 - r * 0.45, 21 + dy, r * 0.62, r * 0.6) | elipse(24 + r * 0.45, 21 + dy, r * 0.62, r * 0.6) | \
        poligono([(24 - r * 1.05, 21.5 + dy), (24 + r * 1.05, 21.5 + dy), (24, 21 + dy + r * 1.3)])
    P.append(Parte(cor, GELO, z=2.5))
    px(P, [(22, 20 + dy), (21, 20 + dy)], BR, 2.6)
    # cabeça de cristal com olhos
    cab = [(19, 8 + dy), (24, 1 + dy), (30, 6 + dy), (29, 11 + dy), (21, 12 + dy)]
    P.append(Parte(poligono(cab), GELO_CL, z=3, plano=True))
    px(P, [(x, 7 + dy) for x in range(23, 30)], OUT, 3.1)
    px(P, [(24, 7 + dy), (25, 7 + dy), (27, 7 + dy), (28, 7 + dy)], '#4d9be6' if t != 3 else '#4d65b4', 3.2)
    px(P, [(25, 7 + dy), (28, 7 + dy)], BR, 3.3)
    for (x, y, frente) in orb:
        if frente:
            P.append(Parte(poligono([(x - 2, y), (x, y - 4), (x + 2, y), (x, y + 2)]), GELO_CL, z=6, plano=True))
    ex = estrela_brilho([(24, 22 + dy)], BR, grande=True) if bate else []
    ex += estrela_brilho([(24 + int(math.cos(t) * 3), 1 + dy)], BR)
    return acabar(P, 48, ex)


def morsa_gigante(t):
    """64×64: morsa castanha enorme deitada no gelo, pregas no pescoço, bigode com cerdas, presas compridas."""
    P = []
    b = RESP[t]
    # barbatana de trás (longe) e cauda
    P.append(Parte(poligono([(10, 52), (2, 56), (3, 60), (12, 58)]), MORSA_T, z=0.4))
    # corpo
    corpo = elipse(28, 47 - b * 0.5, 20, 12.5 + b * 0.5) | elipse(13, 52, 10, 7) | elipse(42, 42, 10, 10)
    P.append(Parte(corpo, MORSA, z=2))
    pelo(P, corpo, '#753c54', None, 2, s=2, dens=11)
    la(P, corpo, '#694f62', None, 2.005, s=3, n=0.03, comp=(2, 3))
    # pregas da pele no pescoço
    for i in range(3):
        px(P, [(37 + i * 3 + int(math.sin(j / 2.5) * 1.2), 38 + j) for j in range(7)], '#694f62', 2.1)
    # neve no dorso
    P.append(Parte(felpudo(elipse(24, 35.5 - b * 0.5, 9, 1.8) | elipse(30, 35 - b * 0.5, 3, 1.6), 1, baixo=2, cima=3), NEVE, z=2.2))
    # barbatana da frente
    P.append(Parte(poligono([(36, 52), (46, 54), (50, 60), (38, 60)]), MORSA, z=3))
    px(P, [(41, 59), (44, 59), (47, 59)], '#45293f', 3.1)
    # cabeça levantada
    cab = elipse(49, 35 + b, 9, 8.5)
    P.append(Parte(cab, MORSA, z=4, luz=0.05))
    # bigode (focinho largo) com cerdas
    foc = elipse(54.5, 40.5 + b, 5.5, 4)
    P.append(Parte(foc, MORSA, z=4.5, luz=0.15))
    px(P, [(x, y + b) for (x, y) in ((52, 39), (54, 39), (56, 39), (53, 41), (55, 41), (57, 41), (58, 39), (51, 41))], '#45293f', 4.6)
    px(P, [(59 + (t % 2), 42 + b), (60, 40 + b), (59, 43 + b)], '#fdcbb0', 4.6)       # cerdas
    # presas compridas (para baixo)
    for (x0, z) in ((51, 4.4), (55, 4.7)):
        P.append(Parte(capsula(x0, 44 + b, x0 + 1.5, 58, 1.4), MARFIM, z=z, volume='cilindro_v'))
    # olho pequeno com brilho e sobrolho
    olho(P, 51, 31 + b, OUT, z=4.8, fechado=(t == 3))
    if t != 3:
        px(P, [(52, 32 + b), (52, 31 + b)], '#45293f', 4.81)
        px(P, [(51, 31 + b)], BR, 4.82)
    px(P, [(50, 29 + b), (51, 29 + b), (52, 29 + b), (53, 30 + b)], '#45293f', 4.8)
    # cicatriz de luta
    px(P, [(30, 41), (31, 42), (32, 43), (33, 44)], '#45293f', 2.3)
    ex = []
    if t in (1, 2):
        ex += [((61, 38 + b - t), '#c7dcd0'), ((62, 37 + b - t), BR)]
    return acabar(P, 64, ex)


def raposa_aurora(t):
    """48×48: raposa branca esguia com três caudas compridas que brilham com as cores da aurora e abanam."""
    P = []
    b = RESP[t]
    # três caudas compridas em pluma (atrás): brancas na base e com a cor da aurora na ponta
    caudas = (((17, 30), (12, 24), (12, 14), (17, 5), AURORA_V, 0.0),
              ((17, 31), (8, 30), (3, 22), (3, 11), AURORA_R, 1.4),
              ((17, 32), (9, 37), (3, 37), (1, 30), AURORA_P, 2.8))
    for i, (p0, p1, p2, p3, rampa, fs) in enumerate(caudas):
        w = math.sin(t * math.pi / 2 + fs) * 1.5
        ctrl = [p0, (p1[0], p1[1] + w * 0.3), (p2[0] + w * 0.5, p2[1] + w * 0.6), (p3[0] + w, p3[1] + w)]
        pts = []
        for k in range(13):
            u = k / 12
            x = (1 - u) ** 3 * ctrl[0][0] + 3 * (1 - u) ** 2 * u * ctrl[1][0] + 3 * (1 - u) * u ** 2 * ctrl[2][0] + u ** 3 * ctrl[3][0]
            y = (1 - u) ** 3 * ctrl[0][1] + 3 * (1 - u) ** 2 * u * ctrl[1][1] + 3 * (1 - u) * u ** 2 * ctrl[2][1] + u ** 3 * ctrl[3][1]
            pts.append((x, y, u))
        base, ponta = set(), set()
        for k in range(12):
            x1, y1, u = pts[k]
            x2, y2, _ = pts[k + 1]
            r = 1.3 + 1.8 * math.sin(min(1, u * 1.15) * math.pi) ** 0.7
            (base if u < 0.5 else ponta).update(capsula(x1, y1, x2, y2, max(0.8, r)))
        ponta -= base
        P.append(Parte(felpudo(base, i, baixo=3, cima=3), NEVE, z=0.5 + i * 0.1))
        P.append(Parte(felpudo(ponta, i + 1, baixo=3, cima=3), rampa, z=0.5 + i * 0.1, separar=False))
    # pernas do lado de trás
    for (x1, x2) in ((20, 19), (31, 32)):
        P.append(Parte(capsula(x1, 33 + b, x2, 45, 1.3), NEVE_T, z=0.8, volume='cilindro_v'))
    # corpo
    corpo = elipse(25, 32 + b, 9.5, 5) | elipse(32, 30 + b, 5, 6)
    corpo = felpudo(corpo, 2, baixo=3, cima=0)
    P.append(Parte(corpo, NEVE, z=2))
    pelo(P, corpo, '#9babb2', None, 2, s=1, dens=7)
    # pernas da frente com "meias" escuras
    for (x1, x2) in ((22, 21), (34, 35)):
        P.append(Parte(capsula(x1, 33 + b, x2, 45, 1.5), NEVE, z=2.05, volume='cilindro_v', separar=False))
        px(P, [(x2, y) for y in range(42, 46)] + [(x2 + 1, 45), (x2 - 1, 45)], '#484a77', 2.06)
    # peito felpudo
    P.append(Parte(felpudo(elipse(35, 31 + b, 3, 4), 1, baixo=2, cima=0), NEVE, z=2.5, separar=False))
    # cabeça com focinho bicudo
    cab = elipse(37, 23 + b, 4.5, 4) | poligono([(37, 21 + b), (46.5, 25.5 + b), (46, 27 + b), (38, 27.5 + b)])
    P.append(Parte(cab, NEVE, z=4, luz=0.1))
    # orelhas grandes com interior lilás
    for (ox, z) in ((34, 3.9), (38, 3.95)):
        P.append(Parte(poligono([(ox - 2, 21 + b), (ox, 12 + b), (ox + 2.5, 20 + b)]), NEVE, z=z))
    px(P, [(34, 16 + b), (34, 17 + b), (34, 18 + b), (35, 19 + b)], '#a884f3', 3.96)
    px(P, [(38, 15 + b), (38, 16 + b), (38, 17 + b)], '#a884f3', 4.01)
    px(P, [(46, 25 + b), (47, 25 + b), (46, 26 + b)], OUT, 4.2)                        # nariz
    px(P, [(41, 27 + b), (42, 27 + b), (43, 27 + b)], '#7f708a', 4.2)
    # olho a brilhar (turquesa) com risco da aurora
    olho(P, 39, 22 + b, '#30e1b9', z=4.4, fechado=(t == 3))
    px(P, [(38, 21 + b), (37, 21 + b)], '#a884f3', 4.3)
    px(P, [(36, 25 + b), (37, 26 + b)], '#ed8099', 4.3)                                  # marca na cara
    # brilhos da aurora a cair das caudas
    ex = []
    cores = ['#30e1b9', '#a884f3', '#ed8099', '#8ff8e2']
    for i in range(4):
        x = 4 + i * 4 + (t % 2)
        y = 10 + ((t + i * 3) * 5) % 26
        ex.append(((x, y), cores[(i + t) % 4]))
    return acabar(P, 48, ex)


def tartaruga_glaciar(t):
    """64×64: tartaruga gigante com um glaciar por carapaça (blocos de gelo, neve no cimo, estacas de cristal,
    pingentes), pele verde-acinzentada com escamas, bico e garras."""
    P = []
    b = RESP[t]
    hb = [0, 0, 1, 1][t]
    # patas do lado de trás
    P.append(Parte(capsula(20, 48, 19, 58, 4), PELE_VT, z=0.3, volume='cilindro_v'))
    P.append(Parte(capsula(44, 48, 45, 58, 4), PELE_VT, z=0.3, volume='cilindro_v'))
    # cauda
    P.append(Parte(poligono([(10, 49), (3, 54), (11, 53)]), PELE_V, z=0.5))
    # pescoço e cabeça (à frente, a espreitar)
    P.append(Parte(capsula(46, 46, 53, 41 + hb, 4.4), PELE_V, z=1, volume='cilindro_h'))
    pintas(P, capsula(46, 46, 53, 41 + hb, 4.4), '#374e4a', 1.01, s=1, dens=5)
    cab = elipse(55, 39 + hb, 6.4, 5) | poligono([(57, 36 + hb), (63, 40 + hb), (60, 44 + hb), (55, 43 + hb)])
    P.append(Parte(cab, PELE_V, z=1.5, luz=0.08))
    px(P, [(x, 42 + hb) for x in range(56, 62)], '#313638', 1.6)                       # bico
    px(P, [(61, 39 + hb), (62, 40 + hb)], '#b2ba90', 1.6)
    olho(P, 56, 37 + hb, OUT, z=1.7, fechado=(t == 3))
    if t != 3:
        px(P, [(57, 38 + hb)], '#f9c22b', 1.71)
        px(P, [(56, 37 + hb)], BR, 1.72)
    px(P, [(55, 35 + hb), (56, 35 + hb), (57, 35 + hb), (58, 36 + hb)], '#374e4a', 1.65)
    # carapaça = glaciar: base escura (borda) e blocos de gelo por cima
    borda_c = poligono([(6, 50), (10, 44), (52, 44), (56, 50), (50, 53), (12, 53)])
    P.append(Parte(borda_c, GELO_T, z=2, plano=True))
    px(P, [(x, 51) for x in range(12, 52, 4)], '#4d65b4', 2.05)
    blocos = [
        [(8, 46 + b), (14, 34 + b), (22, 32 + b), (24, 46 + b)],
        [(20, 46 + b), (22, 28 + b), (32, 24 + b), (36, 46 + b)],
        [(33, 46 + b), (35, 28 + b), (44, 30 + b), (50, 46 + b)],
        [(16, 46 + b), (18, 38 + b), (28, 36 + b), (30, 46 + b)],
        [(30, 46 + b), (32, 37 + b), (42, 38 + b), (44, 46 + b)],
    ]
    for i, q in enumerate(blocos):
        P.append(Parte(poligono(q), GELO_CL if i % 2 else GELO, z=2.2 + i * 0.05, plano=True))
    for (x, y, n, s) in ((14, 38, 5, 1), (25, 30, 7, 2), (38, 33, 6, 3), (34, 40, 4, 4)):
        racha(P, x, y + b, n, '#323353', 2.5, s=s, dx=1, dy=1)
    # neve no cimo
    neve = felpudo(elipse(28, 26 + b, 10, 3) | elipse(16, 33 + b, 5, 2) | elipse(40, 29 + b, 5, 2), 1, baixo=2, cima=0)
    P.append(Parte(neve, NEVE, z=2.6))
    # estacas de cristal a sair do glaciar
    for (cx, by, al, inc) in ((22, 27, 10, -0.2), (27, 25, 14, 0.0), (33, 25, 9, 0.25), (14, 32, 6, -0.4), (43, 29, 6, 0.4)):
        P.append(Parte(poligono(cristal(cx, by + b, al, 2, inc)), CRISTAL, z=2.7, plano=True))
    # pingentes na borda
    for x in (13, 19, 27, 36, 44):
        px(P, [(x, 54), (x, 55)] + ([(x, 56)] if x % 2 else []), '#8fd3ff', 2.8)
    # patas da frente (grossas, com garras)
    for x in (16, 40):
        P.append(Parte(capsula(x, 50, x - 1, 58, 4.4), PELE_V, z=3, volume='cilindro_v'))
        pintas(P, capsula(x, 50, x - 1, 58, 4.4), '#374e4a', 3.01, s=x, dens=5)
        px(P, [(x - 3, 61), (x - 1, 61), (x + 1, 61), (x + 3, 61)], '#c7dcd0', 3.1)
    ex = estrela_brilho([(27, 11 + b + (t % 2))], BR, grande=(t == 0)) + estrela_brilho([(44, 24 + b)], BR) * (t % 2)
    return acabar(P, 64, ex)


def wendigo(t):
    """48×48: criatura alta e magríssima de gelo, crânio de alce com hastes, costelas à mostra, braços compridos
    com garras até aos joelhos, olhos a brilhar no fundo do crânio."""
    P = []
    b = RESP[t]
    sw = ABANA[t]
    PELE = ['#484a77', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
    PELE_T = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
    # perna e braço do lado de trás
    P.append(Parte(capsula(20, 30, 18, 38, 1.5) | capsula(18, 38, 20, 46, 1.3), PELE_T, z=0.5))
    P.append(Parte(capsula(20, 15 + b, 16, 26 + b, 1.4) | capsula(16, 26 + b, 17, 36 + b + sw, 1.2), PELE_T, z=0.6))
    for i in range(3):
        px(P, [(16 + i, 37 + b + sw), (16 + i, 38 + b + sw), (15 + i * 1, 39 + b + sw)], '#3e3546', 0.7)
    # tronco magro, curvado para a frente
    tronco = poligono([(18, 15 + b), (26, 13 + b), (28, 20 + b), (25, 30), (20, 31), (19, 23 + b)])
    P.append(Parte(tronco, PELE, z=2))
    for i in range(4):                                        # costelas
        y = 17 + b + i * 3
        px(P, [(20 + j, y + (j // 3)) for j in range(6)], '#323353', 2.1)
        px(P, [(20 + j, y - 1 + (j // 3)) for j in range(0, 5, 2)], '#c7dcd0', 2.11)
    # anca e perna da frente (dobrada, pé de garras)
    P.append(Parte(capsula(24, 30, 27, 38, 1.7) | capsula(27, 38, 25, 46, 1.4), PELE, z=2.5))
    px(P, [(26, 47), (28, 47), (24, 47)], '#3e3546', 2.6)
    # trapos de pele velha à cintura
    P.append(Parte(poligono([(18, 27), (27, 26), (28, 32), (25, 31), (23, 34), (21, 31), (18, 33)]), COURO, z=2.7))
    # crânio de alce com hastes
    hx, hy = 29, 12 + b
    P.append(Parte(capsula(25, 15 + b, hx - 1, hy, 1.6), PELE, z=3.4))                      # pescoço
    hastes = capsula(hx - 2, hy - 3, hx - 7, hy - 9, 1) | capsula(hx - 7, hy - 9, hx - 6, hy - 14, 0.8) | \
        capsula(hx - 5, hy - 7, hx - 2, hy - 11, 0.8) | capsula(hx - 7, hy - 9, hx - 11, hy - 11, 0.8) | \
        capsula(hx + 1, hy - 3, hx + 2, hy - 10, 0.9) | capsula(hx + 2, hy - 10, hx + 5, hy - 13, 0.7) | capsula(hx + 2, hy - 7, hx + 5, hy - 8, 0.7)
    P.append(Parte(hastes, OSSO, z=3))
    px(P, [(hx - 6, hy - 14), (hx + 5, hy - 13), (hx - 11, hy - 11)], '#8fd3ff', 3.05)       # pontas geladas
    cranio = elipse(hx, hy - 1, 4, 3.6) | poligono([(hx, hy - 3), (hx + 9, hy + 1), (hx + 8, hy + 4), (hx + 1, hy + 3)])
    P.append(Parte(cranio, OSSO, z=3.5, luz=0.1))
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2), (hx + 1, hy - 1), (hx + 2, hy - 1), (hx + 3, hy - 1)], OUT, 3.6)   # órbita
    if t != 2:
        px(P, [(hx + 2, hy - 1)], '#30e1b9', 3.7)
        px(P, [(hx + 2, hy - 2)], '#8ff8e2', 3.71)
    px(P, [(hx + 8, hy + 1), (hx + 8, hy + 2)], OUT, 3.6)                                   # narina
    px(P, [(hx + 3, hy + 3), (hx + 5, hy + 3), (hx + 7, hy + 3)], OUT, 3.6)                 # dentes
    px(P, [(hx + 4, hy + 3), (hx + 6, hy + 3)], BR, 3.61)
    # braço da frente comprido, garras compridas
    P.append(Parte(capsula(25, 15 + b, 31, 24 + b, 1.5) | capsula(31, 24 + b, 33, 34 + b + sw, 1.3), PELE, z=4))
    for i in range(3):
        px(P, [(32 + i, 35 + b + sw), (32 + i, 36 + b + sw), (33 + i, 37 + b + sw), (33 + i, 38 + b + sw)], '#2e222f', 4.1)
        px(P, [(33 + i, 38 + b + sw)], '#8fd3ff', 4.11)
    ex = []
    if t in (0, 1):
        ex += [((hx + 10, hy - t), '#c7dcd0')]
    ex += flocos(48, 48, t, 4, 12, (2, 2, 45, 45))
    return acabar(P, 48, ex)


def cavaleiro_de_gelo(t):
    """48×48: armadura de gelo vazia (só uma luz azul lá dentro), elmo com crista de cristal, capa rasgada,
    mãos no punho de uma espada grande espetada no chão."""
    P = []
    b = RESP[t]
    vento = ABANA[t]
    ARM = CRISTAL
    ARM_T = CRISTAL_T
    luz = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    # capa rasgada atrás
    capa = poligono([(17, 12 + b), (25, 12 + b), (22 + vento * 0.5, 40), (9 + vento, 42), (12, 26)])
    capa -= {(x, y) for x in range(0, 48) for y in range(39, 44) if (x // 2) % 2 == 0 and y > 40}
    P.append(Parte(capa, AZUL_R, z=0.2))
    px(P, [(14 + vento, 34), (15 + vento, 37), (12 + vento, 39)], '#323353', 0.25)
    # perna de trás
    P.append(Parte(capsula(20, 31, 19, 43, 2.2), ARM_T, z=0.5, volume='cilindro_v'))
    P.append(Parte(elipse(20, 45, 3, 1.7), ARM_T, z=0.6))
    # espada (lâmina espetada no chão, à frente)
    lamina = poligono([(36, 25 + b), (39, 25 + b), (38.5, 44), (37.5, 46), (36.5, 44)])
    P.append(Parte(lamina, GELO_CL, z=1, volume='cilindro_v'))
    px(P, [(37, y) for y in range(27 + b, 43)], '#8fd3ff', 1.05)
    # tronco (peitoral com faces)
    peito = poligono([(17, 13 + b), (29, 13 + b), (30, 24 + b), (27, 30 + b), (19, 30 + b), (16, 22 + b)])
    P.append(Parte(peito, ARM, z=2, plano=True))
    px(P, [(23, y) for y in range(15 + b, 29 + b)], '#0b5e65', 2.05)
    px(P, [(18, 15 + b), (19, 15 + b), (20, 16 + b), (18, 16 + b)], '#8ff8e2', 2.06)
    # a luz de dentro, a ver-se pelas frestas
    px(P, [(22, 20 + b), (24, 24 + b)], luz, 2.07)
    # cinto e saiote de placas
    P.append(Parte(retangulo(17, 30 + b, 29, 31 + b), PRETO, z=2.2, plano=True))
    px(P, [(23, 30 + b), (24, 30 + b)], '#8fd3ff', 2.25)
    for i, x in enumerate(range(17, 29, 4)):
        P.append(Parte(poligono([(x, 32 + b), (x + 4, 32 + b), (x + 3.5, 36 + b), (x + 0.5, 36 + b)]), ARM, z=2.3 + i * 0.01, plano=True))
    # perna da frente
    P.append(Parte(capsula(26, 34, 27, 43, 2.4), ARM, z=2.5, volume='cilindro_v'))
    P.append(Parte(elipse(28, 45, 3.6, 1.8), ARM, z=2.6))
    px(P, [(26, 38), (27, 38)], '#8ff8e2', 2.55)                                           # joelheira
    # elmo com viseira em T e crista de cristal
    elmo = elipse(24, 8 + b, 5, 5.2) | retangulo(20, 8 + b, 29, 12 + b)
    P.append(Parte(elmo, ARM, z=3))
    px(P, [(x, 8 + b) for x in range(24, 30)] + [(27, 9 + b), (27, 10 + b), (27, 11 + b)], OUT, 3.1)
    px(P, [(25, 8 + b), (26, 8 + b), (28, 8 + b), (29, 8 + b)], luz, 3.2)
    for (cx, al, inc) in ((20, 5, -0.4), (23, 7, -0.2), (26, 5, 0.0)):
        P.append(Parte(poligono(cristal(cx, 5 + b, al, 1.4, inc)), GELO_CL, z=2.9, plano=True))
    # ombreira de cristal
    P.append(Parte(elipse(27, 15 + b, 4.4, 3.2), ARM, z=3.5))
    for (cx, al) in ((25, 4), (28, 5)):
        P.append(Parte(poligono(cristal(cx, 14 + b, al, 1.3, 0.2)), GELO_CL, z=3.55, plano=True))
    # braço da frente e mãos no punho da espada
    P.append(Parte(capsula(28, 17 + b, 32, 22 + b, 2.2) | capsula(32, 22 + b, 35, 23 + b, 2), ARM, z=4))
    P.append(Parte(retangulo(33, 23 + b, 42, 24 + b), PRETO, z=4.2, plano=True))        # guarda
    px(P, [(33, 23 + b), (42, 23 + b)], '#8fd3ff', 4.25)
    P.append(Parte(retangulo(37, 17 + b, 38, 22 + b), COURO, z=4.1, plano=True))         # punho
    P.append(Parte(elipse(37.5, 16 + b, 1.6, 1.6), GELO, z=4.15))                         # pomo
    P.append(Parte(elipse(37.5, 20 + b, 2.6, 2.2), ARM, z=4.3))                           # manopla
    ex = estrela_brilho([(38, 30 + (t * 3) % 12)], BR) if t != 3 else []
    return acabar(P, 48, ex)


# ======================================================================
# BOSSES
# ======================================================================

def yeti_anciao(t):
    """64×64: yeti enorme e curvado, pelo branco sujo e comprido, cara azulada com presas, braços compridíssimos
    (os nós dos dedos no chão) e um colar com coisas de Jogadores mortos (elmo, espada partida, moeda, anel)."""
    P = []
    b = RESP[t]
    SUJO = ['#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0', '#ffffff']
    SUJO_T = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#9babb2']
    CARA = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
    # braço de trás (comprido, até ao chão)
    P.append(Parte(capsula(22, 26 + b, 15, 42 + b * 0.5, 4) | capsula(15, 42 + b * 0.5, 13, 56, 3.4), SUJO_T, z=0.4))
    P.append(Parte(elipse(13, 58, 4.4, 3.4), CARA, z=0.45))
    # perna de trás
    P.append(Parte(capsula(24, 46, 22, 58, 4.6), SUJO_T, z=0.5, volume='cilindro_v'))
    P.append(Parte(elipse(23, 60, 5, 2.4), CARA, z=0.55))
    # corpo curvado (costas altas)
    corpo = elipse(30, 33 + b, 15, 14) | elipse(26, 44, 11, 8) | elipse(36, 25 + b, 11, 9)
    corpo = felpudo(corpo, 1, baixo=2, cima=2, lados=3)
    P.append(Parte(corpo, SUJO, z=2))
    la(P, corpo, '#9babb2', BR, 2, s=2, n=0.07, comp=(2, 5))
    pintas(P, corpo, '#ab947a', 2.003, s=4, dens=37)                        # sujidade
    pintas(P, corpo, '#966c6c', 2.004, s=7, dens=53)
    # perna da frente
    P.append(Parte(felpudo(capsula(35, 46, 36, 57, 5), 2, baixo=2, cima=0), SUJO, z=2.5, volume='cilindro_v'))
    P.append(Parte(elipse(38, 60, 5.6, 2.4), CARA, z=2.6))
    px(P, [(41, 61), (43, 60), (39, 61)], '#c7dcd0', 2.65)                       # unhas
    # cabeça metida à frente dos ombros: pelo à volta, cara azul
    cab = felpudo(elipse(46, 20 + b, 9.5, 9), 3, baixo=2, cima=2, lados=2)
    P.append(Parte(cab, SUJO, z=3))
    la(P, cab, '#9babb2', BR, 3, s=6, n=0.08, comp=(2, 4))
    cara = elipse(50, 23 + b, 6, 6.2)
    P.append(Parte(cara, CARA, z=3.5, luz=0.1))
    # sobrolho pesado, olhos a brilhar, nariz achatado, boca com presas
    px(P, [(46, 19 + b), (47, 19 + b), (48, 19 + b), (49, 20 + b), (50, 20 + b), (51, 19 + b), (52, 19 + b)], '#323353', 3.6)
    if t != 3:
        px(P, [(48, 21 + b), (49, 21 + b), (51, 21 + b), (52, 21 + b)], '#8fd3ff', 3.7)
        px(P, [(49, 21 + b), (52, 21 + b)], BR, 3.71)
    else:
        px(P, [(48, 21 + b), (49, 21 + b), (51, 21 + b), (52, 21 + b)], '#323353', 3.7)
    px(P, [(53, 23 + b), (54, 23 + b), (53, 24 + b)], '#323353', 3.7)
    px(P, [(x, 26 + b) for x in range(48, 54)], OUT, 3.7)
    px(P, [(49, 25 + b), (52, 25 + b), (50, 27 + b)], BR, 3.75)
    # colar com coisas de Jogadores
    fio = [(36 + i, 30 + b + int(3 * math.sin(i / 14 * math.pi))) for i in range(15)]
    px(P, fio, '#694f62', 4.6)
    P.append(Parte(elipse(39, 33 + b, 2.4, 2) - {(x, 34 + b) for x in range(36, 43)}, PEDRA, z=4.7))       # elmo
    px(P, [(38, 34 + b), (39, 34 + b), (40, 34 + b)], '#3e3546', 4.75)
    P.append(Parte(capsula(44, 33 + b, 45, 37 + b, 0.8), PEDRA, z=4.7))                                 # espada partida
    px(P, [(43, 33 + b), (44, 32 + b), (45, 32 + b), (46, 33 + b)], '#966c6c', 4.75)
    P.append(Parte(elipse(48.5, 32.5 + b, 1.4, 1.4), OURO, z=4.7))                                      # moeda
    px(P, [(41, 35 + b), (41, 36 + b)], '#fdcbb0', 4.7)                                                  # dente
    # braço da frente, muito comprido, mão no chão
    braco = capsula(44, 28 + b, 52, 40 + b * 0.5, 4.4) | capsula(52, 40 + b * 0.5, 53, 54, 3.8)
    braco = felpudo(braco, 1, baixo=2, cima=0, lados=2)
    P.append(Parte(braco, SUJO, z=4))
    la(P, braco, '#9babb2', None, 4, s=9, n=0.08, comp=(2, 4))
    P.append(Parte(elipse(54, 57.5, 5, 3.6), CARA, z=4.5))
    for i in range(3):
        px(P, [(52 + i * 2, 59), (52 + i * 2, 60)], '#323353', 4.55)
    px(P, [(58, 60), (58, 61)], '#c7dcd0', 4.56)
    # pingentes no pelo
    px(P, [(20, 46), (20, 47), (28, 51), (28, 52), (31, 50)], '#8fd3ff', 2.6)
    ex = []
    if t in (1, 2):
        ex += [((57, 23 + b - t), '#c7dcd0'), ((58, 22 + b - t), BR), ((59, 24 + b - t), '#c7dcd0')]
    return acabar(P, 64, ex)


def rei_do_inverno_esquecido(t):
    """64×64: rei-esqueleto de gelo: coroa de cristal e ouro velho, órbitas a arder em azul, barba de pingentes,
    costelas geladas, capa real rasgada a abanar, espada longa de gelo na mão."""
    P = []
    b = RESP[t]
    vento = ABANA[t]
    luz = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    # capa real (atrás), rasgada em baixo
    capa = poligono([(22, 15 + b), (34, 15 + b), (30 + vento * 0.5, 57), (12 + vento, 60), (14, 36)])
    capa -= {(x, y) for x in range(64) for y in range(55, 62) if (x // 3) % 2 == 0 and y >= 57}
    P.append(Parte(capa, AZUL_R, z=0.2))
    la(P, capa, '#323353', None, 0.2, s=3, n=0.04, comp=(3, 6))
    px(P, [(x, 58 - (x % 3)) for x in range(14 + vento, 28)], '#8fd3ff', 0.25)              # geada na bainha
    # perna de trás (ossos)
    P.append(Parte(capsula(27, 40, 26, 49, 1.4) | capsula(26, 49, 26, 58, 1.2), OSSO, z=0.5))
    P.append(Parte(elipse(27, 59.5, 3, 1.6), GELO, z=0.6))
    # braço de trás
    P.append(Parte(capsula(25, 20 + b, 21, 30 + b, 1.2) | capsula(21, 30 + b, 22, 38 + b, 1.1), OSSO, z=0.7))
    # coluna e costelas
    P.append(Parte(capsula(29, 18 + b, 28, 38, 1.2), OSSO, z=2))
    for i in range(4):
        y = 21 + b + i * 3
        cost = capsula(25 - i * 0.3, y, 33 - i * 0.5, y + 1, 0.8)
        P.append(Parte(cost, OSSO, z=2.1 + i * 0.01))
    px(P, [(30, 24 + b), (27, 27 + b), (31, 30 + b)], '#8fd3ff', 2.2)                     # gelo entre as costelas
    px(P, [(28, 25 + b), (29, 25 + b)], luz, 2.15)                                           # o coração frio
    # cinto e saiote de placas velhas
    P.append(Parte(retangulo(23, 36, 34, 38), ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff'], z=2.4, plano=True))
    P.append(Parte(elipse(28.5, 37, 1.6, 1.6), OURO, z=2.45))
    for i, x in enumerate(range(23, 34, 4)):
        P.append(Parte(poligono([(x, 39), (x + 4, 39), (x + 3.5, 44), (x + 0.5, 44)]), AZUL_R, z=2.5 + i * 0.01, plano=True))
    # perna da frente (ossos com joelho)
    P.append(Parte(capsula(31, 42, 33, 50, 1.5) | capsula(33, 50, 32, 58, 1.3), OSSO, z=2.6))
    P.append(Parte(elipse(33, 50, 1.8, 1.8), OSSO, z=2.65))
    P.append(Parte(elipse(34, 59.5, 3.4, 1.6), GELO, z=2.7))
    # ombreira de gelo
    P.append(Parte(elipse(31, 18 + b, 5, 3.4), GELO, z=3))
    for (cx, al) in ((28, 4), (31, 5), (34, 4)):
        P.append(Parte(poligono(cristal(cx, 17 + b, al, 1.2, 0.1)), GELO_CL, z=3.05, plano=True))
    # crânio com barba de pingentes
    cr = elipse(33, 10 + b, 5.4, 5) | retangulo(32, 12 + b, 38, 15 + b)
    P.append(Parte(cr, OSSO, z=4, luz=0.1))
    px(P, [(34, 9 + b), (35, 9 + b), (36, 9 + b), (34, 10 + b), (35, 10 + b), (36, 10 + b)], OUT, 4.1)   # órbita
    px(P, [(35, 9 + b), (36, 9 + b)], luz, 4.2)
    px(P, [(36, 9 + b)], BR, 4.21)
    px(P, [(38, 11 + b), (38, 12 + b)], OUT, 4.1)                                            # nariz
    px(P, [(33, 14 + b), (35, 14 + b), (37, 14 + b)], OUT, 4.1)                              # dentes
    for i, x in enumerate(range(32, 39, 2)):                                                  # barba de pingentes
        px(P, [(x, 16 + b + j) for j in range(2 + (i * 3) % 4)], '#8fd3ff', 4.15)
        px(P, [(x, 16 + b)], BR, 4.16)
    # coroa: aro de ouro velho com pontas de cristal
    P.append(Parte(retangulo(28, 5 + b, 38, 6 + b), OURO, z=4.3, plano=True))
    for (cx, al, c) in ((29, 4, CRISTAL), (32, 6, GELO_CL), (35, 7, CRISTAL), (38, 5, GELO_CL)):
        P.append(Parte(poligono(cristal(cx, 5 + b, al, 1.3, 0.0)), c, z=4.25, plano=True))
    px(P, [(33, 5 + b)], '#e83b3b', 4.35)                                                     # pedra vermelha
    # braço da frente com a espada de gelo (em guarda, ponta para cima e para a frente)
    P.append(Parte(capsula(32, 21 + b, 36, 29 + b, 1.3) | capsula(36, 29 + b, 41, 30 + b, 1.2), OSSO, z=5))
    lamina = poligono([(42, 28 + b), (44, 30 + b), (59, 7 + b), (60, 4 + b), (57, 6 + b)])
    P.append(Parte(lamina, GELO_CL, z=4.8, plano=True))
    px(P, [(44 + i, 27 + b - int(i * 1.45)) for i in range(13)], '#ffffff', 4.85)
    P.append(Parte(capsula(39, 33 + b, 46, 26 + b, 0.9), PRETO, z=5.1))                     # guarda
    px(P, [(39, 33 + b), (46, 26 + b)], '#8fd3ff', 5.15)
    P.append(Parte(capsula(41, 31 + b, 39, 34 + b, 0.9), COURO, z=5.05))                    # punho
    P.append(Parte(elipse(42, 30 + b, 1.8, 1.6), OSSO, z=5.2))                               # mão
    ex = estrela_brilho([(59 - t * 3, 6 + b + int(t * 4.4))], BR, grande=(t % 2 == 0))
    ex += flocos(64, 64, t, 5, 21, (2, 2, 61, 60))
    return acabar(P, 64, ex)


def dragao_de_gelo(t):
    """128×128: dragão branco e azul com escamas de gelo, asas enormes de membrana turquesa transparente,
    chifres de cristal, crista de estacas, o peito a brilhar (o sopro a crescer lá dentro) e bafo gelado."""
    P = []
    b = RESP[t] * 2
    asa = [0, -2, -3, -1][t]
    peito = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    ESC = ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff']          # escamas azuis
    ESC_T = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
    BARRIGA = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
    MEMB = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
    MEMB_T = ['#0b5e65', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9']

    def asa_m(ox, oy, k, dy):
        """Os ossos e a membrana de uma asa a partir do ombro (ox, oy)."""
        cot = (ox - 14 * k, oy - 26 * k + dy)
        pul = (ox - 34 * k, oy - 44 * k + dy * 1.5)
        dedos = [(pul[0] - 26 * k, pul[1] + 18 * k), (pul[0] - 16 * k, pul[1] + 36 * k), (pul[0] - 2 * k, pul[1] + 46 * k)]
        def cava(a, c, f=0.35):   # a borda da membrana curva para dentro entre dois dedos
            mx, my = (a[0] + c[0]) / 2, (a[1] + c[1]) / 2
            return (mx + (pul[0] - mx) * f, my + (pul[1] - my) * f)
        fim = (ox - 4 * k, oy + 6 * k)
        memb = poligono([(ox, oy), cot, pul, dedos[0], cava(dedos[0], dedos[1]), dedos[1], cava(dedos[1], dedos[2]),
                         dedos[2], cava(dedos[2], fim, 0.25), fim])
        ossos = capsula(ox, oy, *cot, 3 * k) | capsula(*cot, *pul, 2.4 * k)
        for d in dedos:
            ossos |= capsula(*pul, *d, 1.2 * k)
        return memb, ossos, pul, dedos
    # asa do lado de lá (mais escura, atrás de tudo)
    memb, ossos, pul, _ = asa_m(70, 58 + b, 0.85, asa * 0.7)
    memb = {(x + 10, y - 4) for x, y in memb}
    ossos = {(x + 10, y - 4) for x, y in ossos}
    P.append(Parte(memb, MEMB_T, z=0.1, plano=True))
    P.append(Parte(ossos, ESC_T, z=0.15))
    # cauda comprida com espinhos
    cauda = [(40, 84 + b), (26, 92), (14, 102), (8, 112), (14, 118), (24, 116)]
    for i in range(len(cauda) - 1):
        r = 7 - i * 1.2
        P.append(Parte(capsula(*cauda[i], *cauda[i + 1], max(1.6, r)), ESC, z=0.3 + i * 0.01))
    P.append(Parte(poligono([(24, 116), (32, 110), (30, 120)]), GELO_CL, z=0.35, plano=True))  # ponta em lâmina
    for (x, y) in ((30, 86), (20, 94), (12, 104)):
        P.append(Parte(poligono(cristal(x, y + 1, 6, 2, -0.5)), GELO_CL, z=0.29, plano=True))
    # patas do lado de lá
    P.append(Parte(capsula(44, 92, 38, 108, 5) | capsula(38, 108, 42, 117, 3.6), ESC_T, z=0.5))
    P.append(Parte(capsula(84, 88, 88, 104, 4.4) | capsula(88, 104, 86, 117, 3.4), ESC_T, z=0.5))
    for x in (42, 86):
        P.append(Parte(elipse(x + 2, 118.5, 5, 2.4), ESC_T, z=0.55))
    # corpo
    corpo = elipse(60, 80 + b, 28, 16) | elipse(84, 74 + b, 14, 16) | elipse(40, 84 + b, 14, 12)
    P.append(Parte(corpo, ESC, z=2))
    # escamas: arcos pequenos em fila
    esc = []
    for (x, y) in corpo:
        if (y // 4) % 2 == 0:
            if (x + (y // 4) * 4) % 9 == 0 and (x, y + 1) in corpo:
                esc += [(x, y), (x + 1, y + 1), (x - 1, y + 1)]
    esc = [p for p in esc if p in corpo - borda(corpo)]
    px(P, [p for p in esc if p[1] > 72 + b or p[0] > 70], '#4d65b4', 2.01)
    px(P, [p for p in esc if p[1] <= 72 + b and p[0] <= 70], '#8fd3ff', 2.01)
    # barriga com placas brancas
    barr = (elipse(66, 90 + b, 24, 7) | elipse(88, 82 + b, 8, 12)) & corpo
    P.append(Parte(barr, BARRIGA, z=2.1, separar=False))
    for y in range(76, 98, 4):
        px(P, [(x, y + b) for x in range(40, 100) if (x, y + b) in barr], '#9babb2', 2.11)
    # o peito a brilhar (sopro)
    P.append(Parte(elipse(91, 72 + b, 4, 5), None, z=3.6, separar=False, cor=peito))
    px(P, elipse(91, 72 + b, 2, 2.6), BR if t in (1, 2) else '#8fd3ff', 3.61)
    # crista de estacas de gelo pelas costas
    for i, (x, y, al) in enumerate(((44, 70, 6), (52, 66, 8), (60, 64, 9), (68, 63, 9), (76, 60, 8))):
        P.append(Parte(poligono(cristal(x, y + b + 2, al, 2.2, -0.35)), GELO_CL, z=1.9, plano=True))
    # pata de trás (perto): coxa grande
    P.append(Parte(elipse(46, 88 + b, 11, 12), ESC, z=3))
    P.append(Parte(capsula(46, 96, 42, 110, 4.6) | capsula(42, 110, 47, 117, 3.6), ESC, z=3.1))
    P.append(Parte(elipse(50, 118.5, 6, 2.6), ESC, z=3.2))
    for i in range(3):
        px(P, [(52 + i * 3, 120), (53 + i * 3, 120), (54 + i * 3, 119)], '#c7dcd0', 3.3)
    # pescoço em S (escamas da frente claras)
    pesc = capsula(86, 70 + b, 96, 54 + b, 8) | capsula(96, 54 + b, 102, 44 + b, 6.5)
    P.append(Parte(pesc, ESC, z=3.5))
    px(P, [p for p in capsula(91, 72 + b, 101, 54 + b, 3) if p in pesc], '#c7dcd0', 3.51)
    for (x, y) in ((88, 60), (93, 50), (98, 42)):                                      # espinhos do pescoço
        P.append(Parte(poligono(cristal(x, y + b + 2, 6, 1.8, -0.5)), GELO_CL, z=3.45, plano=True))
    # cabeça: crânio, focinho comprido, maxilar
    hy = 40 + b
    cab = elipse(104, hy, 10, 8) | poligono([(104, hy - 6), (124, hy + 2), (125, hy + 6), (106, hy + 8)])
    P.append(Parte(cab, ESC, z=4, luz=0.08))
    maxi = poligono([(100, hy + 5), (122, hy + 7), (121, hy + 10), (102, hy + 10)])
    P.append(Parte(maxi, BARRIGA, z=3.9))
    px(P, [(x, hy + 7) for x in range(106, 121)], OUT, 4.05)                           # boca
    for x in (109, 113, 117):
        px(P, [(x, hy + 8)], BR, 4.06)                                                  # dentes
    px(P, [(122, hy + 1), (123, hy + 2)], OUT, 4.05)                                    # narina
    # chifres de cristal (para trás)
    for (x1, y1, x2, y2, r) in ((100, hy - 6, 84, hy - 18, 3), (104, hy - 6, 94, hy - 22, 2.6)):
        P.append(Parte(capsula(x1, y1, x2, y2, r) | poligono([(x2 - r, y2 + 1), (x2 - 5, y2 - 5), (x2 + r, y2 - 1)]), CRISTAL, z=3.8))
    # olho de gelo a brilhar com sobrolho
    px(P, [(104, hy - 4), (105, hy - 4), (106, hy - 4), (107, hy - 4), (108, hy - 4), (109, hy - 3), (110, hy - 3)], OUT, 4.1)
    px(P, elipse(107, hy - 1, 3.2, 2.4), OUT, 4.15)
    if t != 3:
        px(P, elipse(107, hy - 1, 2.2, 1.5), '#8fd3ff', 4.2)
        px(P, [(108, hy - 2), (108, hy - 1)], '#323353', 4.21)
        px(P, [(106, hy - 2)], BR, 4.22)
    else:
        px(P, [(106, hy - 1), (107, hy - 1), (108, hy - 1)], OUT, 4.2)
    # asa do lado de cá (grande, à frente das costas)
    memb, ossos, pul, dedos = asa_m(66, 66 + b, 1.0, asa)
    P.append(Parte(memb, MEMB, z=5, plano=True))
    # veios da membrana
    for d in dedos:
        for k in range(1, 6):
            u = k / 6
            x = pul[0] + (d[0] - pul[0]) * u + (66 - pul[0]) * u * 0.25
            y = pul[1] + (d[1] - pul[1]) * u + (66 + b - pul[1]) * u * 0.25
            px(P, [(x, y)], '#0b8a8f', 5.01)
    P.append(Parte(ossos, ESC, z=5.1))
    P.append(Parte(poligono(cristal(pul[0], pul[1] - 1, 7, 2, -0.3)), GELO_CL, z=5.15, plano=True))  # garra da asa
    # pata da frente (perto)
    P.append(Parte(capsula(92, 86 + b, 96, 102, 5) | capsula(96, 102, 94, 116, 4), ESC, z=6))
    P.append(Parte(elipse(98, 118.5, 6.4, 2.6), ESC, z=6.1))
    for i in range(3):
        px(P, [(99 + i * 3, 120), (100 + i * 3, 120), (101 + i * 3, 119)], '#c7dcd0', 6.2)
    ex = []
    for i in range(3):                                                                  # bafo gelado
        if (t + i) % 4 < 3:
            ex += [((124 - i * 2 + t, hy + 4 - (t + i) % 4), BR if i % 2 else '#8fd3ff')]
    ex += estrela_brilho([(62 + t * 4, 63 + b - t)], BR, grande=(t % 2 == 0))
    ex += flocos(128, 128, t, 8, 33, (2, 2, 125, 125))
    return acabar(P, 128, ex)
