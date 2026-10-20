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
LA = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']            # lã de mamute
LA_T = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
MORSA = ['#45293f', '#753c54', '#966c6c', '#e6904e', '#fca790']
MORSA_T = ['#2e222f', '#45293f', '#753c54', '#966c6c', '#e6904e']
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
    P.append(Parte(cara, GELO_CL, z=3.5))
    px(P, [(18, 8 + b), (19, 8 + b)], OUT, 3.6)
    px(P, [(20, 8 + b), (21, 8 + b)], '#30e1b9' if t != 2 else '#8ff8e2', 3.6)               # olho a brilhar
    px(P, [(21, 8 + b)], BR, 3.7)
    px(P, [(19, 11 + b), (20, 11 + b), (21, 11 + b)], '#323353', 3.6)                         # boca
    px(P, [(19, 12 + b), (21, 12 + b), (21, 13 + b)], '#8fd3ff', 3.7)                         # pingentes (barba)
    # braço da frente com o arco
    P.append(Parte(capsula(17, 14 + b, 22, 17 + b, 1.3), COURO, z=4))
    arco = {(23, y) for y in range(10 + b, 25 + b)} | {(24, y) for y in range(12 + b, 23 + b)} | {(25, y) for y in range(14 + b, 21 + b)}
    arco -= {(23, y) for y in range(12 + b, 23 + b)} | {(24, y) for y in range(14 + b, 21 + b)}
    P.append(Parte(arco, None, z=4.5, separar=False, cor='#966c6c'))
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
    # lança de gelo (atrás da asa)
    px(P, [(25, y) for y in range(13, 31)], '#966c6c', 1)
    P.append(Parte(poligono([(23.5, 13), (25.5, 6), (27.5, 13)]), GELO_CL, z=1.1))
    px(P, [(24, 13), (26, 13), (25, 14)], '#ab947a', 1.2)
    # pés
    P.append(Parte(elipse(16, 30, 2.2, 1.2), LARANJA, z=0.5))
    P.append(Parte(elipse(21, 30, 2.4, 1.2), LARANJA, z=2.5))
    # corpo
    corpo = elipse(18.5 + lean * 0.5, 23.5, 5.5, 6.5)
    P.append(Parte(corpo, COSTAS, z=2))
    P.append(Parte(elipse(20.5 + lean * 0.5, 24.5, 3.2, 5) & corpo, NEVE, z=2.1, separar=False))
    # cabeça
    hx = 19 + lean
    P.append(Parte(elipse(hx, 16.5, 4, 3.6), COSTAS, z=3))
    P.append(Parte(elipse(hx + 2, 17.5, 1.8, 1.8), NEVE, z=3.1, separar=False))               # bochecha branca
    px(P, [(hx + 1, 16), (hx + 2, 16)], OUT, 3.2)
    px(P, [(hx + 1, 16)], BR, 3.3)                                                                  # olho
    P.append(Parte(poligono([(hx + 3, 16.5), (hx + 7, 17.6), (hx + 3, 19)]), LARANJA, z=3.4))    # bico
    # capacete de concha (com estrias)
    concha = {p for p in elipse(hx - 0.5, 14.5, 4.6, 3.2) if p[1] <= 14}
    P.append(Parte(concha, ['#966c6c', '#e6904e', '#fca790', '#fdcbb0', '#ffffff'], z=3.5))
    for i in (-3, -1, 1, 3):
        px(P, [(hx - 0.5 + i, 13), (hx - 0.5 + i + (1 if i > 0 else 0), 12)], '#cd683d', 3.51)
    # asa da frente a segurar a lança
    P.append(Parte(capsula(18 + lean * 0.5, 21, 24, 22, 1.4), COSTAS, z=4))
    px(P, [(25, 21), (25, 22)], '#ab947a', 4.1)
    ex = []
    if t == 0:
        ex += estrela_brilho([(25, 8)], BR)
    if t == 2:
        ex += estrela_brilho([(24, 10)], BR)
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
    pelo(P, corpo, '#45293f', '#ab947a', 2, s=1, dens=7, comp=int(2 + k))
    # musgo, neve e pássaros nas costas (o Ancião)
    if anciao:
        rnd = random.Random(4)
        for (mx, my, rx, ry) in ((20, 29, 7, 3), (33, 25.5, 6, 2.6), (12, 33, 4, 2.4)):
            mm = {(x, y + b) for (x, y) in elipse(*S(mx, my), rx * k, ry * k)}
            mm = {p for p in felpudo(mm, 2, baixo=2, cima=2) if rnd.random() < 0.92}
            P.append(Parte(mm, MUSGO, z=2.5))
            pintas(P, mm, '#d5e04b', 2.51, s=int(mx), dens=7)
        P.append(Parte(felpudo({(x, y + b) for (x, y) in elipse(*S(38, 24.5), 5 * k, 1.6 * k)}, 0, baixo=2, cima=0), NEVE, z=2.6))
        # cogumelinhos / flores de neve no musgo
        for (fx, fy) in ((17, 26.5), (24, 26.5)):
            X, Y = S(fx, fy)
            px(P, [(X, Y + b), (X + 1, Y + b - 1), (X - 1, Y + b - 1), (X, Y + b - 2)], BR, 2.62)
            px(P, [(X, Y + b - 1)], '#f9c22b', 2.63)
        # dois pássaros (pisco-de-peito-ruivo) a saltitar nas costas
        for i, (bx, by) in enumerate(((22, 25), (30, 22))):
            X, Y = S(bx, by)
            hop = 2 if (t + i) % 4 == 1 else 0
            Y = Y + b - hop
            P.append(Parte(elipse(X, Y, 3, 2.4), PEDRA, z=2.8))
            P.append(Parte(elipse(X + 1.5, Y + 0.8, 1.6, 1.4), LARANJA, z=2.81, separar=False))
            P.append(Parte(elipse(X + 2.5, Y - 2, 1.8, 1.7), PEDRA, z=2.82))
            px(P, [(X + 3, Y - 2.5)], OUT, 2.83)
            px(P, [(X + 4.5, Y - 2), (X + 5.5, Y - 2)], '#f79617', 2.83)
            px(P, [(X - 3, Y - 1), (X - 4, Y - 1), (X - 4, Y)], '#3e3546', 2.79)
    # pernas da frente (perto) com unhas claras
    for x in (18, 44):
        perna = capsula(*S(x, 44 + b / k), *S(x + 0.5, 57.5), 4.4 * k)
        P.append(Parte(perna, LA, z=3, volume='cilindro_v', separar=False))
        pelo(P, perna, '#45293f', None, 3, s=x, dens=6, comp=2)
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
    pelo(P, cab, '#45293f', '#ab947a', 4, s=3, dens=8, comp=int(1 + k))
    # orelha pequena
    P.append(Parte({(x, y + b) for x, y in elipse(*S(43, 32), 2.6 * k, 3.6 * k)}, LA_T, z=4.1))
    # olho com brilho e pestanas
    X, Y = S(51, 31)
    olho(P, X, Y + b, OUT, z=4.5, tam=1 if k == 1 else 2, fechado=(t == 3))
    if t != 3:
        px(P, [(X + 1, Y + b)] if k == 1 else [(X + 1, Y + b + 1), (X + 2, Y + b + 1)], '#966c6c', 4.51)
        px(P, [(X, Y + b)], BR, 4.52)
    # tromba (curva para a frente e enrola no fim, a abanar)
    tw = w * 0.8
    tromba = capsula(*S(53, 37 + b / k), *S(56 + tw * 0.5, 47), 3 * k) | capsula(*S(56 + tw * 0.5, 47), *S(56 + tw, 55), 2.2 * k) \
        | capsula(*S(56 + tw, 55), *S(59 + tw, 56.5), 1.7 * k)
    # presas de marfim (curvas)
    if anciao:
        presa = capsula(*S(52, 42 + b / k), *S(58, 50), 2 * k) | capsula(*S(58, 50), *S(63, 47), 1.6 * k) | capsula(*S(63, 47), *S(63.5, 41), 1.2 * k)
    else:
        presa = capsula(*S(52, 43 + b / k), *S(57, 47), 1.5 * k) | capsula(*S(57, 47), *S(59.5, 45.5), 1.2 * k)
    P.append(Parte(presa, MARFIM, z=4.6 if not anciao else 5.2, volume='cilindro_h'))
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
