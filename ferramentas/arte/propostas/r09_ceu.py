"""PROPOSTA (ainda não aprovada): os monstros, guardiões e bosses da Região 9 — Céu, desenhados de novo.

Só grava em arte/propostas/monstros/r09_ceu/ (não mexe na arte do jogo). Para cada criatura faz a tira
<id>_parado_lado.png (4 quadros "parado", o mesmo tamanho de quadro do desenho antigo) e, no fim,
comparar.gif (antes | depois) e depois.gif (só os novos).

Fichas: docs/regioes/r09_ceu.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (Grifo Real e Serafim Caído).
Estilo: o Ent Ancião (ferramentas/arte/ent_anciao.py): partes com volume, contorno escuro, luz de cima à
esquerda, textura (penas, escamas, veios do mármore, fiapos de nuvem) e olhos com brilho.

Correr a partir da raiz do repositório:  python3 ferramentas/arte/propostas/r09_ceu.py [id ...]
"""
import json
import math
import os
import random
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

OUT = '#2e222f'
PASTA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r09_ceu')
ANTIGA = os.path.join(RAIZ, 'arte', 'regioes', 'r09_ceu')

RESURRECT_64 = """2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334
e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73
91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff
45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0""".split()

# ---------------- rampas desta região (escuro -> claro), só Resurrect 64
NUVEM = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
NUVEM_SOMBRA = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']
TROVOADA = ['#2e222f', '#323353', '#484a77', '#625565', '#7f708a']
TROVOADA_CLARA = ['#323353', '#484a77', '#625565', '#7f708a', '#9babb2']
CEU = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
CEU_CLARO = ['#4d65b4', '#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff']
OURO = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
OURO_VELHO = ['#7a3045', '#9e4539', '#f79617', '#f9c22b', '#fbff86']
BRONZE = ['#4c3e24', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
MARMORE = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
MARMORE_ESC = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']
PELE = ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0']
PENA_CAST = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
PENA_ESC = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
FOGO = ['#9e4539', '#ea4f36', '#fb6b1d', '#f79617', '#f9c22b']
CHAMA = ['#b33831', '#fb6b1d', '#f79617', '#f9c22b', '#fbff86']
FOLHA = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
ROCHA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
TERRA = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
CASCA = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
FERRO = ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
AGUA = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
SOMBRA = ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9']
PRETO = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
ROXO = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']
LUZ_SOLIDA = ['#f79617', '#f9c22b', '#fbff86', '#ffffff', '#ffffff']
CABELO_OURO = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86']
VERMELHO = ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790']


# ---------------- ajudas de desenho

def px(P, pts, cor, z):
    """Píxeis soltos de uma só cor (marcas, brilhos, riscos)."""
    P.append(Parte({(int(round(x)), int(round(y))) for x, y in pts}, None, z=z, separar=False, cor=cor))


def linha(x1, y1, x2, y2):
    n = int(max(abs(x2 - x1), abs(y2 - y1))) + 1
    return {(int(round(x1 + (x2 - x1) * i / max(1, n - 1))), int(round(y1 + (y2 - y1) * i / max(1, n - 1)))) for i in range(n)}


def borda(m):
    return {p for p in m if any((p[0] + dx, p[1] + dy) not in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))}


def pintas(P, m, rampa, z, semente, escuro=0.0, claro=0.0, n=17):
    """Textura: pintas escuras em baixo à direita (sombra) e pintas claras em cima à esquerda (luz)."""
    if not m:
        return
    rnd = random.Random(semente)
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    esc, cla = [], []
    dentro = m - borda(m)
    for (x, y) in dentro:
        h = (x * 7 + y * 13 + semente * 5) % n
        lado = (x - cx) + (y - cy)
        if h == 0 and lado > -1 and rnd.random() < 0.6 + escuro:
            esc.append((x, y))
        elif h == 9 and lado < 1 and rnd.random() < 0.5 + claro:
            cla.append((x, y))
    px(P, esc, rampa[0] if len(rampa) > 1 else rampa, z + 0.001)
    px(P, cla, rampa[4] if len(rampa) > 1 else rampa, z + 0.002)


def escamas_penas(P, m, cor_esc, z, passo=3, fase=0, cor_cla=None):
    """Penas em escama (pequenos 'v' em fiadas desencontradas) por dentro de uma máscara."""
    esc, cla = [], []
    dentro = m - borda(m)
    for (x, y) in dentro:
        lin = (y + fase) // 2
        if (y + fase) % 2 == 0 and (x + (lin % 2) * (passo // 2 + 1)) % passo == 0:
            esc.append((x, y))
            if cor_cla and (x - 1, y - 1) in dentro:
                cla.append((x - 1, y - 1))
    px(P, esc, cor_esc, z)
    if cor_cla:
        px(P, cla, cor_cla, z + 0.0005)


def asa(P, sx, sy, comp, ang, rampa, z, n=5, r=1.6, abre=70, curva=1.0, cob=None, separar=True, luz=0.0):
    """Uma asa de penas vista de lado: um 'osso' que sai do ombro (sx, sy) com o ângulo ang (graus, 90 = para cima,
    180 = para trás) e as penas penduradas por trás dele, mais compridas na ponta. abre: o leque das penas."""
    a = math.radians(ang)
    bx, by = math.cos(a), -math.sin(a)
    tip = (sx + bx * comp, sy + by * comp)
    partes = []
    for i in range(n):
        t = (i + 1) / n
        base = (sx + bx * comp * t * 0.92, sy + by * comp * t * 0.92)
        da = math.radians(ang + abre * (1 - t) + 18 * t * curva)
        L = comp * (0.42 + 0.5 * t)
        fim = (base[0] + math.cos(da) * L, base[1] - math.sin(da) * L)
        partes.append(Parte(capsula(base[0], base[1], fim[0], fim[1], r), rampa, z=z + 0.01 * (n - i), separar=separar, luz=luz))
    P.extend(partes)
    # as penas pequenas de cima (cobertura), por cima das outras
    c = cob or rampa
    P.append(Parte(capsula(sx, sy, sx + bx * comp * 0.85, sy + by * comp * 0.85, r * 1.7), c, z=z + 0.1, separar=separar, luz=luz + 0.15))
    return tip


def olho(P, x, y, iris, z, grande=False, pupila=OUT, brilho='#ffffff'):
    """Olho com brilho: pequeno (2 píxeis) ou grande (3x3 com pupila e ponto branco)."""
    if grande:
        px(P, elipse(x + .5, y + .5, 1.9, 1.9), iris, z)
        px(P, [(x + 1, y), (x + 1, y + 1)], pupila, z + 0.001)
        px(P, [(x - 1, y - 1)], brilho, z + 0.002)
    else:
        px(P, [(x, y)], iris, z)
        px(P, [(x, y - 1)], brilho, z + 0.001)


def nuvem_massa(P, puffs, rampa, z, separar=True, luz=0.0):
    """Uma nuvem feita de bolas (cx, cy, r): cada bola tem volume e a linha entre elas é o tom mais escuro."""
    m_total = set()
    for i, (cx, cy, r) in enumerate(puffs):
        m = elipse(cx, cy, r, r * 0.9)
        P.append(Parte(m, rampa, z=z + 0.001 * i, separar=separar, luz=luz))
        m_total |= m
    return m_total


def raio(x, y, comp, semente, passo=3):
    """Um raio em zigue-zague para baixo."""
    rnd = random.Random(semente)
    pts = []
    cx, cy = x, y
    for _ in range(comp):
        nx = cx + rnd.choice((-1, 1)) * rnd.randint(1, 2)
        ny = cy + passo
        pts += list(linha(cx, cy, nx, ny))
        cx, cy = nx, ny
    return pts


def faiscas(P, cx, cy, raio_, t, semente, cores=('#fbff86', '#ffffff'), n=4, z=80):
    rnd = random.Random(semente)
    for i in range(n):
        ang = rnd.uniform(0, 6.28) + t * 0.9
        d = rnd.uniform(raio_ * 0.6, raio_)
        x, y = cx + math.cos(ang) * d, cy + math.sin(ang) * d
        if (i + t) % 3 == 2:
            continue
        cor = cores[(i + t) % len(cores)]
        if (i + t) % 2:
            px(P, [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], cor, z)
        else:
            px(P, [(x, y)], cor, z)


BOB = [0, -1, -1, 0]        # respirar / pairar
BOB2 = [0, 0, 1, 1]


# =====================================================================================================
# MONSTROS PEQUENOS (32×32)
# =====================================================================================================

def harpia(t):
    """Harpia: mulher-pássaro de penas castanhas, cabelo ruivo desgrenhado, olhos amarelos, garras amarelas."""
    P = []
    dy = [0, -1, -1, 0][t]
    flap = [0, 18, 34, 16][t]
    # asa de trás (mais escura)
    asa(P, 12, 14 + dy, 10, 112 + flap, PENA_ESC, z=0.5, n=4, r=1.1, abre=70)
    # cauda de penas
    for i, (ex, ey) in enumerate(((3, 17), (4, 20), (6, 22))):
        P.append(Parte(capsula(10, 17 + dy, ex, ey + dy, 1.1), PENA_CAST, z=1 + i * 0.01))
    px(P, [(4, 17 + dy), (5, 20 + dy), (7, 22 + dy)], '#c7dcd0', 1.1)
    # pernas e garras amarelas
    P.append(Parte(capsula(12, 20 + dy, 11, 25 + dy, 1.0), OURO_VELHO, z=1.5))
    P.append(Parte(capsula(16, 20 + dy, 17, 25 + dy, 1.0), OURO, z=4))
    px(P, [(10, 26 + dy), (12, 26 + dy)], '#9babb2', 1.6)
    px(P, [(16, 26 + dy), (18, 26 + dy), (19, 25 + dy)], '#ffffff', 4.1)
    # corpo de penas
    corpo = elipse(14, 16 + dy, 5, 4.5)
    P.append(Parte(corpo, PENA_CAST, z=3))
    escamas_penas(P, corpo, '#694f62', 3.01, passo=3)
    peito = {p for p in elipse(17.5, 17 + dy, 2.4, 3.2) if p in corpo}
    P.append(Parte(peito, ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#c7dcd0'], z=3.1, separar=False))
    # asa da frente: sai do ombro para cima e para trás (não tapa a cara)
    asa(P, 13, 14 + dy, 11, 122 + flap, PENA_CAST, z=5, n=5, r=1.1, abre=68, cob=PENA_ESC)
    # cabeça (cara de mulher) e cabelo ruivo selvagem
    PELE_H = ['#cd683d', '#e6904e', '#fca790', '#fdcbb0', '#fdcbb0']
    CAB_H = ['#2e222f', '#45293f', '#7a3045', '#9e4539', '#cd683d']
    cab = elipse(22.5, 9.5 + dy, 4.2, 4.2)
    P.append(Parte(cab, PELE_H, z=6, luz=0.35))
    P.append(Parte(capsula(20, 12 + dy, 18, 14 + dy, 1.2), PELE_H, z=5.9))   # pescoço
    v = [0, 1, 1, 0][t]
    capuz = {(x, y) for (x, y) in cab if y <= 6 + dy or x <= 19 or (y == 7 + dy and x <= 24) or (y == 8 + dy and x <= 21)}
    cabelo = capuz | elipse(21.5, 6.8 + dy, 3.6, 1.6) | capsula(19, 8 + dy, 13, 6 + dy - v, 1.6) \
        | capsula(19, 10 + dy, 13, 10 + dy, 1.5) | capsula(19, 12 + dy, 15, 14 + dy + v, 1.2)
    P.append(Parte(cabelo - (cab - capuz), CAB_H, z=7, separar=False))
    px(P, [(16, 6 + dy - v), (19, 6 + dy), (21, 6 + dy)], '#cd683d', 7.1)
    px(P, [(24, 7 + dy)], '#7a3045', 7.2)                     # franja a cair na testa
    # olho amarelo com pupila, nariz e boca
    px(P, [(23, 9 + dy), (23, 10 + dy)], '#f9c22b', 8)
    px(P, [(24, 9 + dy), (24, 10 + dy)], OUT, 8)
    px(P, [(24, 9 + dy)], '#ffffff', 8.1)
    px(P, [(22, 8 + dy), (23, 8 + dy), (24, 8 + dy)], '#7a3045', 8)          # sobrancelha zangada
    px(P, [(26, 10 + dy)], '#fca790', 8)                                     # nariz
    px(P, [(24, 12 + dy), (25, 12 + dy)], '#7a3045', 8)                      # boca
    return desenhar(P, 32, 32)


def elemental_de_ar(t):
    """Elemental de Ar: um redemoinho branco-azulado com olhos, a rodar; uma folha e uma pedrinha apanhadas pelo vento."""
    P = []
    dy = [0, -1, -1, 0][t]
    VENTO = ['#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff']
    topo, fundo = 6, 27
    faixas = []
    for y in range(topo + 2, fundo + 1, 4):
        k = (fundo - y) / (fundo - topo)
        w = 2.0 + 10.0 * k ** 0.8
        cx = 15 + 1.8 * math.sin(y * 0.3 + t * math.pi / 2)
        faixas.append((cx, y + dy, w))
    corpo = set()
    for i, (cx, y, w) in enumerate(faixas):
        m = elipse(cx, y, w, 3.0)
        P.append(Parte(m, VENTO, z=10 - i * 0.1, volume='cilindro_h', luz=0.15))
        corpo |= m
    # riscas do vento em espiral (uma por faixa, andam com o tempo)
    for i, (cx, y, w) in enumerate(faixas):
        L = max(2, int(w * 0.8))
        x0 = cx - w + 1 + ((t * 3 + i * 4) % max(1, int(2 * w - L)))
        risco = [(x0 + k, y + (1 if k > L * 0.6 else 0)) for k in range(L)]
        px(P, [p for p in risco if p in corpo], '#4d9be6', 11)
        px(P, [(x0 - 1, y - 1)] if (x0 - 1, y - 1) in corpo else [], '#ffffff', 11)
    # olhos: ovais escuros com brilho, na faixa de cima, do lado direito
    cx0, y0, _ = faixas[1]
    y0 -= 2
    for ex in (int(cx0) + 2, int(cx0) + 6):
        px(P, [(ex, y0), (ex + 1, y0), (ex, y0 + 1), (ex + 1, y0 + 1), (ex, y0 + 2), (ex + 1, y0 + 2)], '#323353', 20)
        px(P, [(ex, y0)], '#ffffff', 20.1)
    px(P, [(int(cx0) + 4, y0 + 4), (int(cx0) + 5, y0 + 4)], '#484a77', 20)       # boquinha a soprar
    # fiapos de vento soltos à volta
    for (ax, ay, ln) in ((2, 10, 4), (26, 15, 4), (3, 21, 3)):
        o = (t * 2 + ax) % 3 - 1
        px(P, [(ax + o + i, ay + dy) for i in range(ln)] + [(ax + o + ln, ay + dy - 1)], '#c7dcd0', 30)
    # uma folha verde e uma pedrinha a rodar à volta do funil
    ang = t * math.pi / 2 + 0.6
    lx, ly = 15 + math.cos(ang) * 12, 13 + math.sin(ang) * 3 + dy
    zf = 25 if math.sin(ang) > 0 else 1
    px(P, [(lx, ly), (lx + 1, ly), (lx + 1, ly - 1)], '#91db69', zf)
    px(P, [(lx + 1, ly)], '#239063', zf + 0.1)
    sx, sy = 15 - math.cos(ang) * 8, 22 - math.sin(ang) * 2 + dy
    zp = 25 if math.sin(ang) < 0 else 1
    px(P, [(sx, sy), (sx + 1, sy)], '#7f708a', zp)
    px(P, [(sx, sy)], '#9babb2', zp + 0.1)
    return desenhar(P, 32, 32)


def nuvem_viva(t):
    """Nuvem Viva: nuvem fofa e simpática (bochechas cor-de-rosa), mas com uma pinga de chuva sempre pronta."""
    P = []
    dy = [0, -1, -1, 0][t]
    b = [0, 0.4, 0.6, 0.2][t]   # respira: incha um bocadinho
    # tufos de cima (atrás) e a barriga (à frente, uma peça só: a cara fica limpa)
    for i, (cx, cy, r) in enumerate(((10, 15, 4.0), (15, 10.5, 5.0), (21, 10.5, 4.4), (25, 14.5, 3.6))):
        P.append(Parte(elipse(cx, cy + dy, r + b, (r + b) * 0.9), NUVEM_SOMBRA, z=1 + i * 0.01, luz=0.25))
    barriga = elipse(17, 17 + dy, 11 + b, 5.5 + b / 2)
    P.append(Parte(barriga, NUVEM_SOMBRA, z=2, luz=0.25))
    fundo = {(x, y) for (x, y) in barriga if y >= 21 + dy}
    P.append(Parte(fundo, ['#625565', '#7f708a', '#9babb2', '#9babb2', '#9babb2'], z=2.1, separar=False, plano=True))
    # fiapos claros por cima
    px(P, [(12, 8 + dy), (13, 8 + dy), (14, 7 + dy), (19, 7 + dy), (20, 7 + dy)], '#ffffff', 3)
    px(P, [(7, 13 + dy), (8, 12 + dy)], '#ffffff', 3)
    # olhos grandes (piscam no último quadro), virados para a direita
    for ex in (18, 23):
        if t == 3:
            px(P, [(ex, 16 + dy), (ex + 1, 16 + dy), (ex - 1, 15 + dy), (ex + 2, 15 + dy)], '#323353', 5)
        else:
            px(P, [(ex, 14 + dy), (ex + 1, 14 + dy), (ex, 15 + dy), (ex + 1, 15 + dy), (ex, 16 + dy), (ex + 1, 16 + dy)], '#323353', 5)
            px(P, [(ex, 14 + dy)], '#ffffff', 5.1)
            px(P, [(ex + 1, 16 + dy)], '#4d65b4', 5.1)
    # bochechas e boquinha
    px(P, [(16, 18 + dy), (17, 18 + dy)], '#f68181', 5)
    px(P, [(25, 18 + dy), (26, 18 + dy)], '#f68181', 5)
    px(P, [(20, 18 + dy), (21, 19 + dy), (22, 18 + dy)], '#484a77', 5)
    # uma pinga de chuva a cair por baixo
    gy = 24 + [0, 2, 4, 6][t] + dy
    if t < 3:
        px(P, [(11, gy), (11, gy + 1)], '#8fd3ff', 6)
        px(P, [(11, gy + 1)], '#4d9be6', 6.1)
    return desenhar(P, 32, 32)


def _alado32(t, tipo):
    """Guerreiros alados pequenos (Anjo Guardião, Valquíria, Valquíria Sigrun): cabeça grande, asa, lança."""
    P = []
    dy = [0, -1, -1, 0][t]
    flap = [0, 8, 14, 6][t]
    anjo, sig = tipo == 'anjo', tipo == 'sigrun'
    ASA = OURO if sig else NUVEM
    ARM = OURO if anjo else FERRO
    # asa (atrás de tudo)
    asa(P, 12, 15 + dy, 11, 118 + flap, ASA, z=0.5, n=5, r=1.3, abre=72, cob=(OURO_VELHO if sig else MARMORE_ESC))
    if sig:
        px(P, [(4, 6 + dy), (3, 8 + dy)], '#ffffff', 0.9)
    # escudo redondo às costas (valquírias)
    if not anjo:
        esc = elipse(10.5, 19 + dy, 3.6, 4.2)
        P.append(Parte(esc, ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'] if not sig else BRONZE, z=1))
        px(P, [(10, 18 + dy), (11, 18 + dy), (10, 19 + dy), (11, 19 + dy)], '#c7dcd0' if not sig else '#fbff86', 1.1)
        px(P, [(9, 16 + dy), (8, 19 + dy), (9, 22 + dy)], '#9babb2', 1.05)
    # pernas e botas
    P.append(Parte(capsula(13, 24, 13, 29, 1.3), ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'], z=2))
    P.append(Parte(capsula(17, 24, 17, 29, 1.3), ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'] if anjo else FERRO, z=3))
    P.append(Parte(retangulo(12, 29, 14, 30), CASCA if not anjo else OURO_VELHO, z=2.1))
    P.append(Parte(retangulo(16, 29, 19, 30), CASCA if not anjo else OURO, z=3.1))
    # saia / túnica
    if anjo:
        saia = poligono([(10.5, 21 + dy), (19.5, 21 + dy), (21, 27), (9, 27)])
        P.append(Parte(saia, NUVEM, z=4, volume='cilindro_v'))
        px(P, [(11, 26), (14, 26), (17, 26), (20, 26)], '#9babb2', 4.1)            # pregas
    else:
        saia = poligono([(10.5, 21 + dy), (19.5, 21 + dy), (20.5, 26), (9.5, 26)])
        P.append(Parte(saia, CEU if not sig else VERMELHO, z=4, volume='cilindro_v'))
        px(P, [(x, 25) for x in range(10, 21, 2)], '#c7dcd0' if not sig else '#fbb954', 4.1)
    # tronco (peitoral)
    tronco = elipse(15, 18.5 + dy, 4.2, 4.0)
    P.append(Parte(tronco, ARM if not anjo else NUVEM, z=5))
    if anjo:
        px(P, [(x, 21 + dy) for x in range(12, 19)], '#f9c22b', 5.1)              # cinto dourado
        px(P, [(15, 21 + dy)], '#ffffff', 5.2)
    else:
        px(P, [(13, 17 + dy), (14, 16 + dy)], '#ffffff', 5.1)
        px(P, [(x, 21 + dy) for x in range(12, 19)], '#694f62' if not sig else '#9e4539', 5.1)
        px(P, [(15, 21 + dy)], '#f9c22b', 5.2)
    # cabeça
    cab = elipse(17.5, 10.5 + dy, 4.4, 4.4)
    PELE_C = ['#cd683d', '#e6904e', '#fca790', '#fdcbb0', '#fdcbb0']
    P.append(Parte(cab, PELE_C, z=6, luz=0.35))
    CAB = CABELO_OURO
    capuz = {(x, y) for (x, y) in cab if y <= 7 + dy or x <= 15 or (y == 8 + dy and x <= 19)}
    v = [0, 1, 1, 0][t]
    if anjo:   # caracóis dourados
        cabelo = capuz | elipse(14.5, 12 + dy, 2.4, 3.6) | elipse(17, 6.5 + dy, 4, 2)
        P.append(Parte(cabelo, CAB, z=6.5, separar=False))
        px(P, [(13, 9 + dy), (15, 7 + dy), (12, 13 + dy), (18, 6 + dy)], '#fbff86', 6.6)
        px(P, [(14, 11 + dy), (13, 14 + dy), (16, 8 + dy)], '#f79617', 6.6)
    else:      # capacete com asinhas e trança loura
        tranca = capsula(13, 12 + dy, 11, 18 + dy + v, 1.2)
        P.append(Parte(tranca, CAB, z=5.5))
        px(P, [(11, 14 + dy + v), (12, 16 + dy + v)], '#9e4539', 5.6)
        cabelo = capuz | elipse(14.5, 11 + dy, 2.0, 2.4)
        P.append(Parte(cabelo, CAB, z=6.5, separar=False))
        elmo = {(x, y) for (x, y) in elipse(17.5, 8.5 + dy, 4.8, 3.6) if y <= 8 + dy}
        P.append(Parte(elmo, ARM, z=7))
        px(P, [(x, 8 + dy) for x in range(13, 23)], '#625565' if not sig else '#9e4539', 7.1)   # aba do elmo
        asinha = [(14, 6), (13, 5), (12, 4), (11, 3), (13, 6), (12, 5), (11, 4), (10, 3), (12, 6), (11, 5), (14, 5)]
        P.append(Parte({(x, y + dy - v) for x, y in asinha}, NUVEM if not sig else ['#9e4539', '#f79617', '#fbff86', '#ffffff', '#ffffff'], z=7.2))
        px(P, [(17, 5 + dy), (16, 5 + dy)], '#ffffff', 7.3)
    # olho (azul) com brilho, boca
    px(P, [(19, 10 + dy), (19, 11 + dy)], '#323353', 8)
    px(P, [(20, 10 + dy), (20, 11 + dy)], '#4d9be6' if not sig else '#f9c22b', 8)
    px(P, [(19, 10 + dy)], '#ffffff', 8.1)
    px(P, [(21, 13 + dy)], '#cd683d', 8)
    # auréola (anjo): um anel dourado que flutua e brilha
    if anjo:
        hy = 3 + [0, 0, -1, -1][t] + dy
        anel = borda(elipse(16.5, hy + 0.5, 3.8, 1.6))
        P.append(Parte(anel, OURO, z=9, plano=True))
        px(P, [(14, hy - 1)], '#ffffff', 9.1)
    # lança direita, à frente do corpo
    lx = 23
    topo = 5 + dy
    P.append(Parte({(lx, y) for y in range(topo + 2, 31)}, None, z=10, separar=False, cor='#f9c22b' if anjo else '#966c6c'))
    px(P, [(lx, y) for y in range(topo + 3, 31, 3)], '#9e4539' if anjo else '#694f62', 10.01)
    if sig:   # lança-relâmpago: ponta em zigue-zague amarela e faíscas
        zz = {(lx, topo + 1), (lx + 1, topo), (lx, topo - 1), (lx - 1, topo - 2), (lx, topo - 3), (lx + 1, topo - 4),
              (lx - 1, topo), (lx + 1, topo + 1)}
        P.append(Parte(zz, OURO, z=10.5))
        faiscas(P, lx, topo - 2, 4, t, 3, n=4, z=12)
    elif anjo:  # lança de luz: ponta em losango que brilha
        pm = {(lx, topo - 3), (lx - 1, topo - 2), (lx, topo - 2), (lx + 1, topo - 2), (lx - 1, topo - 1), (lx, topo - 1),
              (lx + 1, topo - 1), (lx - 1, topo), (lx, topo), (lx + 1, topo), (lx, topo + 1)}
        P.append(Parte(pm, LUZ_SOLIDA, z=10.5))
        if t % 2 == 0:
            px(P, [(lx + 3, topo - 4), (lx + 3, topo - 6), (lx + 2, topo - 5), (lx + 4, topo - 5)], '#fbff86', 12)
        else:
            px(P, [(lx - 3, topo + 1)], '#ffffff', 12)
    else:
        pm = {(lx, topo - 3), (lx, topo - 2), (lx - 1, topo - 1), (lx, topo - 1), (lx + 1, topo - 1), (lx - 1, topo),
              (lx, topo), (lx + 1, topo), (lx, topo + 1)}
        P.append(Parte(pm, ['#3e3546', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=10.5))
        px(P, [(lx + 1, topo + 3), (lx + 2, topo + 4 + [0, 1, 1, 0][t])], '#b33831', 10.6)     # fita vermelha
    # braço da frente a segurar a lança
    P.append(Parte(capsula(16, 16 + dy, lx - 1, 19 + dy, 1.2), ARM if not anjo else NUVEM, z=11))
    P.append(Parte(elipse(lx + 0.5, 19.5 + dy, 1.4, 1.5), PELE_C, z=11.1, luz=0.3))
    return desenhar(P, 32, 32)


def anjo_guardiao(t):
    return _alado32(t, 'anjo')


def valquiria(t):
    return _alado32(t, 'valquiria')


def valquiria_sigrun(t):
    return _alado32(t, 'sigrun')
