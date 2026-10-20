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


def baixar(img, n):
    out = Image.new('RGBA', img.size, (0, 0, 0, 0))
    out.paste(img, (0, n), img)
    return out


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


# =====================================================================================================
# MONSTROS MÉDIOS (48×48)
# =====================================================================================================

CEU_ESC = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']


def passaro_trovao(t):
    """Pássaro-Trovão: águia enorme de penas azuis com riscas amarelas em raio, peito amarelo, faíscas à volta."""
    P = []
    dy = [0, -1, -2, -1][t] + 6
    flap = [0, 14, 26, 12][t]
    # asa de trás
    asa(P, 19, 18 + dy, 15, 112 + flap * 0.9, CEU_ESC, z=0.5, n=6, r=1.6, abre=70)
    # cauda em leque com as pontas amarelas
    for i, (ex, ey) in enumerate(((3, 18), (2, 22), (3, 26), (6, 29))):
        P.append(Parte(capsula(13, 22 + dy, ex, ey + dy, 1.7), CEU, z=1 + i * 0.01))
        px(P, [(ex, ey + dy), (ex + 1, ey + dy)], '#f9c22b', 1.1)
    # patas com garras
    P.append(Parte(capsula(18, 26 + dy, 17, 32 + dy, 1.3), OURO_VELHO, z=1.5))
    P.append(Parte(capsula(24, 27 + dy, 25, 33 + dy, 1.4), OURO, z=4))
    for (gx, gy, c, z) in ((15, 33, '#9babb2', 1.6), (17, 34, '#9babb2', 1.6), (23, 35, '#ffffff', 4.1), (25, 35, '#ffffff', 4.1),
                          (27, 34, '#ffffff', 4.1)):
        px(P, [(gx, gy + dy), (gx, gy + dy - 1)], c, z)
    # corpo
    corpo = elipse(20, 22 + dy, 9.5, 6.5)
    P.append(Parte(corpo, CEU, z=3))
    escamas_penas(P, corpo, '#484a77', 3.01, passo=4, cor_cla='#8fd3ff')
    peito = {p for p in elipse(26, 24 + dy, 4.5, 5) if p in corpo}
    P.append(Parte(peito, OURO, z=3.1, separar=False, luz=0.1))
    px(P, [(25, 24 + dy), (27, 26 + dy), (25, 27 + dy)], '#f79617', 3.2)
    # asa da frente com riscas em raio (atrás da cabeça)
    asa(P, 18, 18 + dy, 17, 124 + flap, CEU, z=8, n=6, r=1.7, abre=66, cob=CEU_ESC[1:] + ['#8fd3ff'])
    a = math.radians(124 + flap)
    zz = []
    for k in range(8):
        u = 0.12 + k * 0.1
        x = 18 + math.cos(a) * 17 * u
        y = 18 + dy - math.sin(a) * 17 * u
        nx, ny = math.sin(a), math.cos(a)
        o = 1.2 if k % 2 else -0.6
        zz.append((x + nx * o + 1.5 * nx, y + ny * o + 1.5 * ny))
    pts = set()
    for i in range(len(zz) - 1):
        pts |= linha(*zz[i], *zz[i + 1])
    px(P, pts, '#f9c22b', 8.5)
    # pescoço e cabeça
    P.append(Parte(capsula(25, 20 + dy, 30, 15 + dy, 3.8), CEU, z=9))
    cab = elipse(32, 13 + dy, 5.2, 4.6)
    P.append(Parte(cab, CEU, z=10, luz=0.15))
    # crista de penas amarelas (eriça-se a meio)
    e = [0, 1, 2, 1][t]
    for i, (cx_, cy_) in enumerate(((27, 5), (24, 8), (24, 12))):
        P.append(Parte(capsula(30, 11 + dy, cx_ - e, cy_ + dy - e, 1.1), OURO, z=9.8 + i * 0.01))
    # bico curvo
    bico = poligono([(35.5, 11 + dy), (40, 11.5 + dy), (42, 14 + dy), (41, 16 + dy), (39, 15 + dy), (36, 16 + dy)])
    P.append(Parte(bico, ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'], z=11))
    px(P, [(41, 16 + dy), (41, 15 + dy)], '#45293f', 11.1)
    px(P, [(37, 14 + dy), (38, 14 + dy)], '#9e4539', 11.1)
    # olho feroz
    px(P, [(33, 11 + dy), (34, 11 + dy), (33, 12 + dy), (34, 12 + dy)], '#f9c22b', 12)
    px(P, [(34, 12 + dy), (34, 11 + dy)], OUT, 12.1)
    px(P, [(33, 11 + dy)], '#ffffff', 12.2)
    px(P, [(32, 10 + dy), (33, 10 + dy), (34, 10 + dy), (35, 10 + dy)], '#323353', 12)       # sobrancelha
    # faíscas a estalar
    faiscas(P, 22, 16 + dy, 18, t, 5, n=6, z=20)
    if t in (1, 2):
        px(P, raio(6 + t * 4, 2, 3, t, passo=2), '#fbff86', 19)
    return desenhar(P, 48, 48)


def veios(P, m, cor, z, semente, dens=9, amp=2.0):
    """Veios de mármore: riscos finos e ondulados na diagonal."""
    pts = []
    for (x, y) in m - borda(m):
        u = x + y * 0.6 + amp * math.sin(y / 3.0 + semente)
        if int(u) % dens == 0 and (x * 5 + y * 3 + semente) % 4:
            pts.append((x, y))
    px(P, pts, cor, z)


def runa(P, x, y, cor, z, forma=0):
    """Uma runa pequena de 3x4."""
    formas = [[(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (2, 0)],
              [(0, 0), (1, 1), (2, 2), (1, 3), (0, 3), (2, 0)],
              [(1, 0), (1, 1), (1, 2), (1, 3), (0, 1), (2, 2)],
              [(0, 0), (2, 0), (1, 1), (1, 2), (0, 3), (2, 3)]]
    px(P, [(x + a, y + b) for a, b in formas[forma % 4]], cor, z)


def golem_celeste(t):
    """Golem Celeste: estátua de mármore branco com ouro e runas azuis que pulsam."""
    P = []
    dy = [0, 0, 1, 1][t]
    brilho = ['#4d9be6', '#8fd3ff', '#ffffff', '#8fd3ff'][t]
    # braço de trás
    P.append(Parte(capsula(16, 19 + dy, 12, 29 + dy, 3.4), MARMORE_ESC, z=1, volume='cilindro_h'))
    P.append(Parte(elipse(12, 32 + dy, 3.8, 3.4), MARMORE_ESC, z=1.1))
    P.append(Parte(retangulo(10, 26 + dy, 15, 27 + dy), OURO_VELHO, z=1.2))
    # pernas (pilares)
    P.append(Parte(capsula(19, 35, 19, 43, 3.6), MARMORE_ESC, z=2, volume='cilindro_v'))
    P.append(Parte(capsula(28, 35, 28, 43, 3.9), MARMORE, z=3, volume='cilindro_v'))
    P.append(Parte(retangulo(14, 43, 23, 46, canto=1), MARMORE_ESC, z=2.1))
    P.append(Parte(retangulo(23, 43, 33, 46, canto=1), MARMORE, z=3.1))
    P.append(Parte(retangulo(30, 43, 33, 46, canto=1), OURO, z=3.2))
    px(P, [(28, 39), (28, 40), (27, 41)], '#625565', 3.3)                     # racha
    runa(P, 27, 37, brilho, 3.4, 2)
    # cinto dourado
    P.append(Parte(retangulo(16, 31 + dy, 32, 35 + dy, canto=1), OURO, z=4, volume='cilindro_v'))
    px(P, [(24, 32 + dy), (24, 33 + dy), (23, 33 + dy), (25, 33 + dy)], brilho, 4.1)
    # tronco de mármore
    tronco = poligono([(13, 15 + dy), (35, 15 + dy), (33, 32 + dy), (16, 32 + dy)])
    P.append(Parte(tronco, MARMORE, z=5, volume='cilindro_v'))
    veios(P, tronco, '#9babb2', 5.01, 1)
    pintas(P, tronco, MARMORE, 5.02, 3)
    # runa grande do peito (círculo com uma estrela) e rachas
    anel = borda(elipse(25, 23 + dy, 4, 4))
    px(P, anel, '#4d65b4', 5.1)
    px(P, [(25, 21 + dy), (25, 22 + dy), (25, 23 + dy), (25, 24 + dy), (25, 25 + dy), (23, 23 + dy), (24, 23 + dy), (26, 23 + dy),
           (27, 23 + dy)], brilho, 5.2)
    px(P, [(17, 18 + dy), (18, 19 + dy), (18, 20 + dy), (19, 21 + dy)], '#625565', 5.15)
    runa(P, 17, 25 + dy, brilho, 5.2, 1)
    # cabeça (elmo pequeno) com coroa dourada
    cab = retangulo(21, 7 + dy, 31, 15 + dy, canto=1)
    P.append(Parte(cab, MARMORE, z=6, luz=0.25))
    P.append(Parte(retangulo(21, 6 + dy, 31, 8 + dy), OURO, z=6.1))
    px(P, [(22, 5 + dy), (25, 4 + dy), (25, 5 + dy), (28, 5 + dy), (31, 5 + dy)], '#f9c22b', 6.05)
    px(P, [(25, 4 + dy)], '#ffffff', 6.06)
    # viseira com os olhos azuis a brilhar
    px(P, [(x, y + dy) for x in range(24, 32) for y in (10, 11, 12)], '#323353', 6.2)
    px(P, [(27, 11 + dy), (28, 11 + dy), (30, 11 + dy), (31, 11 + dy)], brilho, 6.3)
    px(P, [(27, 10 + dy), (30, 10 + dy)], '#4d9be6', 6.3)
    px(P, [(29, 13 + dy), (30, 13 + dy)], '#9babb2', 6.2)                     # queixo
    # ombreiras douradas
    P.append(Parte(elipse(15, 16 + dy, 4.5, 3.4), OURO_VELHO, z=4.5))
    P.append(Parte(elipse(33, 17 + dy, 5.2, 3.8), OURO, z=7))
    px(P, [(31, 15 + dy), (32, 15 + dy)], '#ffffff', 7.1)
    # braço da frente com pulseira de ouro e punho grande
    P.append(Parte(capsula(33, 20 + dy, 36, 29 + dy, 3.6), MARMORE, z=8, volume='cilindro_h'))
    P.append(Parte(retangulo(33, 26 + dy, 39, 28 + dy), OURO, z=8.1))
    punho = elipse(37, 32 + dy, 4.2, 3.8)
    P.append(Parte(punho, MARMORE, z=8.2))
    px(P, [(38, 31 + dy), (38, 33 + dy), (39, 32 + dy)], '#9babb2', 8.3)   # dedos
    runa(P, 34, 21 + dy, brilho, 8.15, 3)
    # pozinho de luz a subir das runas
    for i, (sx, sy) in enumerate(((12, 12), (38, 8), (8, 22))):
        y = sy - (t + i) % 4
        px(P, [(sx, y)], '#8fd3ff' if (t + i) % 2 else '#ffffff', 20)
    return desenhar(P, 48, 48)


ARCO_IRIS = [VERMELHO, RAMPAS['laranja'], OURO, FOLHA, CEU, ROXO]


def asa_arco_iris(P, sx, sy, comp, ang, z, r=1.5, abre=70, sombra=False):
    """Asa de penas coloridas (uma cor por pena, do vermelho ao roxo)."""
    a = math.radians(ang)
    bx, by = math.cos(a), -math.sin(a)
    n = len(ARCO_IRIS)
    for i in range(n):
        tt = (i + 1) / n
        base = (sx + bx * comp * tt * 0.9, sy + by * comp * tt * 0.9)
        da = math.radians(ang + abre * (1 - tt) + 18 * tt)
        L = comp * (0.45 + 0.5 * tt)
        fim = (base[0] + math.cos(da) * L, base[1] - math.sin(da) * L)
        ramp = ARCO_IRIS[n - 1 - i]
        if sombra:
            ramp = [ramp[0], ramp[0], ramp[1], ramp[2], ramp[3]]
        P.append(Parte(capsula(*base, *fim, r), ramp, z=z + 0.01 * (n - i)))
    P.append(Parte(capsula(sx, sy, sx + bx * comp * 0.8, sy + by * comp * 0.8, r * 1.6),
                   MARMORE_ESC if sombra else MARMORE, z=z + 0.1))


def serpente_alada(t):
    """Serpente Alada: serpente branca-pérola com losangos verde-água, asas de penas arco-íris e crista de penas."""
    P = []
    fase = t * math.pi / 2
    flap = [0, 14, 24, 10][t]
    # o corpo: uma curva que ondula (nada no ar)
    pts = []
    for i in range(41):
        sv = i / 40
        x = 3 + 33 * sv
        onda = 6 * math.sin(2.3 * math.pi * sv - fase) * (1 - 0.55 * sv)
        y = 33 + onda
        if sv > 0.78:   # o pescoço sobe para a cabeça
            k = (sv - 0.78) / 0.22
            y = y * (1 - k) + 20 * k
        pts.append((x, y, 1.0 + 3.2 * sv ** 0.8))
    hx, hy = 39, 18 + round(math.sin(fase) * 0.6)
    # asa de trás
    asa_arco_iris(P, 31, 25, 15, 108 + flap * 0.8, z=0.5, r=1.4, sombra=True)
    # leque de penas na ponta da cauda
    tx, ty, _ = pts[0]
    for i, (dx_, dy_) in enumerate(((-3, -4), (-4, 0), (-3, 4))):
        P.append(Parte(capsula(tx + 1, ty, tx + dx_, ty + dy_, 1.2), ARCO_IRIS[i * 2], z=1 + i * 0.01))
    # segmentos do corpo (a linha entre eles faz os anéis)
    corpo = set()
    seg = 5
    for k in range(0, 40, seg):
        m = set()
        for j in range(k, min(40, k + seg) + 1):
            x, y, r = pts[j]
            m |= elipse(x, y, r, r)
        P.append(Parte(m, MARMORE, z=2 + k * 0.01, luz=0.1))
        corpo |= m
    # barriga mais clara, losangos verde-água nas costas e escamas
    escamas_penas(P, corpo, '#9babb2', 2.6, passo=4)
    for j in range(4, 38, 4):
        x, y, r = pts[j]
        ytop = y - r * 0.55
        px(P, [(x, ytop - 1), (x - 1, ytop), (x + 1, ytop), (x, ytop + 1)], '#0eaf9b', 2.7)
        px(P, [(x, ytop)], '#30e1b9', 2.71)
    # cabeça (focinho para a direita)
    cab = elipse(hx, hy, 5.2, 3.8) | capsula(hx + 2, hy + 1, hx + 7, hy + 1.5, 2.2)
    P.append(Parte(cab, MARMORE, z=6, luz=0.2))
    px(P, [(hx + 2, hy + 3), (hx + 3, hy + 3), (hx + 4, hy + 3), (hx + 5, hy + 3), (hx + 6, hy + 3)], '#7f708a', 6.1)  # boca
    px(P, [(hx + 7, hy)], '#625565', 6.1)                                        # narina
    # olho verde-água com pupila de cobra e brilho
    px(P, [(hx + 1, hy - 1), (hx + 2, hy - 1), (hx + 1, hy), (hx + 2, hy)], '#30e1b9', 6.2)
    px(P, [(hx + 2, hy - 1), (hx + 2, hy)], OUT, 6.3)
    px(P, [(hx + 1, hy - 1)], '#ffffff', 6.4)
    px(P, [(hx, hy - 2), (hx + 1, hy - 2), (hx + 2, hy - 2)], '#625565', 6.2)        # sobrolho
    # língua bifurcada (sai e entra)
    if t in (1, 2):
        px(P, [(hx + 8, hy + 3), (hx + 9, hy + 3), (hx + 10, hy + 2), (hx + 10, hy + 4)], '#e83b3b', 6.5)
    # crista de penas coloridas
    for i, (cx_, cy_) in enumerate(((hx - 7, hy - 6), (hx - 4, hy - 8), (hx - 1, hy - 8))):
        o = [0, 1, 1, 0][t]
        P.append(Parte(capsula(hx - 1, hy - 2, cx_ - o, cy_, 1.1), ARCO_IRIS[i * 2], z=5.5 + i * 0.01))
    # asa da frente
    asa_arco_iris(P, 31, 26, 16, 120 + flap, z=8, r=1.5)
    return baixar(desenhar(P, 48, 48), 3)


# =====================================================================================================
# GUARDIÕES HUMANOIDES (48×48)
# =====================================================================================================

def cavaleiro_de_luz_solida(t):
    """Cavaleiro de Luz Sólida: armadura feita de luz dourada (com riscas de luz a correr por ela), penacho de
    chama clara, escudo com o sol, espada de luz; partículas de luz a subir."""
    P = []
    dy = [0, 0, 1, 1][t]
    L = ['#f79617', '#f9c22b', '#fbff86', '#fbff86', '#ffffff']
    L2 = ['#9e4539', '#f79617', '#f9c22b', '#f9c22b', '#fbff86']
    # capa de luz (atrás)
    capa = poligono([(18, 15 + dy), (24, 15 + dy), (22, 38), (12 + [0, 1, 1, 0][t], 41), (14, 30)])
    P.append(Parte(capa, ['#9e4539', '#f79617', '#f9c22b', '#fbb954', '#fbff86'], z=0.5))
    # escudo (braço de trás) com o sol
    esc = poligono([(10, 18 + dy), (19, 18 + dy), (19, 27 + dy), (14.5, 33 + dy), (10, 27 + dy)])
    P.append(Parte(esc, L2, z=1))
    px(P, borda(elipse(14.5, 24 + dy, 2.8, 2.8)), '#f79617', 1.1)
    px(P, elipse(14.5, 24 + dy, 1.6, 1.6), '#ffffff', 1.12)
    for (a, b) in ((14, 19), (14, 29), (11, 24), (17, 24)):
        px(P, [(a + 0.5, b + dy)], '#fbff86', 1.11)
    # pernas
    P.append(Parte(capsula(21, 31, 20, 43, 2.8), L2, z=2, volume='cilindro_v'))
    P.append(Parte(capsula(27, 31, 29, 43, 3.0), L, z=3, volume='cilindro_v'))
    P.append(Parte(retangulo(16, 43, 22, 46, canto=1), L2, z=2.1))
    P.append(Parte(retangulo(26, 43, 33, 46, canto=1), L, z=3.1))
    P.append(Parte(elipse(28.5, 37, 2.5, 2), L, z=3.2))                       # joelheira
    # saia de placas
    P.append(Parte(poligono([(18, 27 + dy), (31, 27 + dy), (33, 33), (17, 33)]), L2, z=4, volume='cilindro_v'))
    px(P, [(x, 31) for x in range(19, 33, 3)], '#f79617', 4.1)
    # peitoral
    peito = poligono([(18, 15 + dy), (31, 15 + dy), (32, 22 + dy), (29, 28 + dy), (19, 28 + dy)])
    P.append(Parte(peito, L, z=5, volume='cilindro_v'))
    px(P, [(25, 18 + dy), (25, 19 + dy), (24, 19 + dy), (26, 19 + dy), (25, 20 + dy)], '#f79617', 5.1)   # estrela
    # riscas de luz a correr pela armadura (de baixo para cima)
    for (x, y) in peito | capa:
        if (y + t * 2 - x // 3) % 8 == 0 and (x + y) % 2 == 0:
            P.append(Parte({(x, y)}, None, z=5.05, separar=False, cor='#ffffff'))
    # elmo com viseira e olhos brancos
    elmo = elipse(25.5, 10 + dy, 5, 5.2)
    P.append(Parte(elmo, L, z=6))
    px(P, [(x, 9 + dy) for x in range(25, 31)] + [(x, 10 + dy) for x in range(25, 31)] + [(x, 11 + dy) for x in range(27, 31)], '#7a3045', 6.1)
    px(P, [(28, 10 + dy), (29, 10 + dy), (29, 9 + dy)], '#ffffff', 6.2)
    px(P, [(30, 10 + dy)], '#8fd3ff', 6.2)
    px(P, [(27, 13 + dy), (27, 14 + dy), (29, 13 + dy), (29, 14 + dy)], '#f79617', 6.1)   # respiradouros
    # penacho de chama clara (abana)
    o = [0, 1, 2, 1][t]
    for i, (ex, ey) in enumerate(((17 - o, 4), (16 - o, 8), (19 - o, 1))):
        P.append(Parte(capsula(25, 5 + dy, ex, ey + dy, 2.0 - i * 0.3), ['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2', '#ffffff'], z=5.5 + i * 0.01))
    # ombreira
    P.append(Parte(elipse(31, 16 + dy, 3.8, 3.0), L, z=7))
    # espada de luz (na mão da frente, a apontar para baixo e para a frente)
    hx, hy = 34, 26 + dy
    lamina = capsula(hx + 1, hy - 1, hx + 9, hy - 14, 1.2)
    P.append(Parte(lamina, ['#f9c22b', '#fbff86', '#ffffff', '#ffffff', '#ffffff'], z=8))
    px(P, linha(hx + 2, hy - 2, hx + 8, hy - 13), '#8fd3ff', 8.05)
    P.append(Parte(capsula(hx - 2, hy + 1, hx + 3, hy - 3, 0.8), L2, z=8.2))          # guarda
    P.append(Parte(capsula(31, 18 + dy, hx - 1, hy - 1, 2.0), L, z=9))                 # braço
    P.append(Parte(elipse(hx, hy, 2, 2), L2, z=9.1))                                    # mão
    # brilho na ponta da espada e partículas de luz a subir
    if t % 2 == 0:
        px(P, [(hx + 10, hy - 17), (hx + 10, hy - 15), (hx + 9, hy - 16), (hx + 11, hy - 16)], '#ffffff', 20)
    for i, (sx, sy) in enumerate(((8, 38), (38, 40), (12, 12), (40, 8))):
        y = sy - (t * 2 + i * 3) % 8
        px(P, [(sx, y)], '#fbff86' if i % 2 else '#ffffff', 20)
    return desenhar(P, 48, 48)


def jardineira_celeste(t):
    """Jardineira Celeste: autómato de jardinagem de cobre e verde, com um olho-lente, uma tesoura grande,
    um regador no outro braço e um vaso com flores nas costas."""
    P = []
    dy = [0, 0, 1, 1][t]
    VERDE_P = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
    # vaso às costas com plantas
    P.append(Parte(retangulo(10, 15 + dy, 17, 23 + dy, canto=1), ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'], z=0.5))
    for i, (lx_, ly_) in enumerate(((11, 9), (14, 6), (17, 10))):
        o = [0, 1, 0, -1][(t + i) % 4]
        P.append(Parte(capsula(13.5, 15 + dy, lx_ + o, ly_ + dy, 1.4), VERDE_P, z=0.6 + i * 0.01))
    for (fx, fy, c) in ((14, 5, '#f04f78'), (10, 8, '#fbff86'), (18, 9, '#8fd3ff')):
        o = [0, 1, 0, -1][t]
        px(P, [(fx + o, fy + dy), (fx + o - 1, fy + dy), (fx + o + 1, fy + dy), (fx + o, fy + dy - 1), (fx + o, fy + dy + 1)], c, 0.7)
        px(P, [(fx + o, fy + dy)], '#ffffff', 0.71)
    # braço de trás: regador a pingar
    P.append(Parte(capsula(18, 20 + dy, 14, 29 + dy, 1.8), FERRO, z=1))
    reg = retangulo(7, 27 + dy, 15, 34 + dy, canto=1)
    P.append(Parte(reg, VERDE_P, z=1.2, volume='cilindro_v'))
    P.append(Parte(capsula(8, 29 + dy, 2, 25 + dy, 1.1), VERDE_P, z=1.1))
    px(P, [(1, 24 + dy), (2, 24 + dy), (1, 25 + dy)], '#9babb2', 1.15)
    gy = 27 + t * 3 + dy
    px(P, [(2, gy), (2, gy + 1)], '#8fd3ff', 1.3)
    px(P, [(1, gy + 6 - (t % 2) * 12 if t % 2 else gy + 5)], '#4d9be6', 1.3)
    # pernas de metal com articulações
    for (x0, x1, z, R) in ((20, 19, 2, ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']), (27, 28, 3, FERRO)):
        P.append(Parte(capsula(x0, 33, x0, 38, 1.6), R, z=z))
        P.append(Parte(capsula(x0, 38, x1, 44, 1.6), R, z=z))
        P.append(Parte(elipse(x0, 38, 2.2, 2.2), BRONZE, z=z + 0.1))
        P.append(Parte(retangulo(x1 - 3, 44, x1 + 3, 46, canto=1), BRONZE, z=z + 0.2))
    # corpo redondo de cobre com avental verde
    corpo = elipse(24, 25 + dy, 8.5, 9)
    P.append(Parte(corpo, BRONZE, z=4))
    avental = {p for p in elipse(26, 28 + dy, 6.5, 6.5) if p in corpo and p[1] >= 23 + dy}
    P.append(Parte(avental, VERDE_P, z=4.1))
    px(P, [(25, 27 + dy), (26, 27 + dy), (27, 27 + dy), (25, 28 + dy), (27, 28 + dy)], '#165a4c', 4.2)   # bolso
    for (rx_, ry_) in ((18, 22), (19, 28), (29, 20)):
        px(P, [(rx_, ry_ + dy)], '#fbb954', 4.15)                             # rebites
    # engrenagem no peito (roda)
    gx, gy2 = 21, 20 + dy
    px(P, borda(elipse(gx, gy2, 2.4, 2.4)), '#4c3e24', 4.3)
    dentes = [(0, -3), (3, 0), (0, 3), (-3, 0)] if t % 2 == 0 else [(2, -2), (2, 2), (-2, 2), (-2, -2)]
    px(P, [(gx + a, gy2 + b) for a, b in dentes], '#4c3e24', 4.3)
    # cabeça: cúpula com um olho-lente grande
    cab = elipse(26, 11 + dy, 5.5, 5)
    P.append(Parte(cab, BRONZE, z=5))
    P.append(Parte(retangulo(21, 14 + dy, 31, 16 + dy), FERRO, z=5.1))       # pescoço/colar
    lente = elipse(28.5, 11 + dy, 2.6, 2.6)
    P.append(Parte(lente, ['#0b5e65', '#0b8a8f', '#30e1b9', '#8ff8e2', '#ffffff'], z=6))
    px(P, [(29, 11 + dy), (30, 11 + dy)], '#0b5e65', 6.1)
    px(P, [(28, 10 + dy)], '#ffffff', 6.2)
    px(P, [(22, 8 + dy), (23, 7 + dy)], '#fbb954', 5.2)
    # antena com uma folhinha
    P.append(Parte(capsula(24, 6 + dy, 23, 2 + dy, 0.6), FERRO, z=4.9, separar=False))
    px(P, [(22, 1 + dy), (23, 1 + dy), (22, 2 + dy)], '#91db69', 4.95)
    # braço da frente com a tesoura de podar (abre e fecha)
    P.append(Parte(capsula(30, 19 + dy, 33, 27 + dy, 2.0), FERRO, z=7))
    P.append(Parte(elipse(33, 27 + dy, 2.4, 2.4), BRONZE, z=7.1))
    ab = [0, 2, 3, 1][t]
    l1 = capsula(34, 27 + dy, 44, 22 + dy - ab, 1.0)
    l2 = capsula(34, 27 + dy, 44, 25 + dy + ab, 1.0)
    P.append(Parte(l2, FERRO, z=7.2))
    P.append(Parte(l1, FERRO, z=7.3))
    P.append(Parte(capsula(32, 28 + dy, 29, 33 + dy, 1.1), VERMELHO, z=7.4))   # cabos vermelhos
    px(P, [(34, 27 + dy)], '#fbb954', 7.5)
    return desenhar(P, 48, 48)


def monge_do_vento(t):
    """Monge do Vento: monge velho e careca de manto cor de laranja, sobrancelhas e barba brancas, asas cinzentas,
    contas ao pescoço e um bastão com fitas que o vento faz dançar; redemoinhos aos pés."""
    P = []
    dy = [0, -1, -1, 0][t]
    flap = [0, 8, 14, 6][t]
    LAR = ['#9e4539', '#cd683d', '#fb6b1d', '#f79617', '#fbb954']
    PELE_M = ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0']
    # asas (cinzentas)
    asa(P, 21, 18 + dy, 14, 112 + flap, NUVEM_SOMBRA, z=0.4, n=6, r=1.7, abre=66, cob=MARMORE_ESC, luz=-0.15)
    asa(P, 22, 18 + dy, 15, 132 + flap, NUVEM_SOMBRA, z=0.6, n=6, r=1.7, abre=66, cob=MARMORE_ESC)
    # manto comprido
    manto = poligono([(20, 15 + dy), (30, 15 + dy), (32, 30 + dy), (34, 43), (16, 43), (18, 30 + dy)])
    P.append(Parte(manto, LAR, z=2, volume='cilindro_v'))
    px(P, [(x, 42) for x in range(17, 34)], '#9e4539', 2.1)                     # bainha
    px(P, [(21, 33), (21, 36), (22, 39), (27, 34), (28, 38)], '#cd683d', 2.05)  # pregas
    # faixa amarela na diagonal
    faixa = {p for p in capsula(20, 17 + dy, 31, 29 + dy, 1.6) if p in manto}
    P.append(Parte(faixa, OURO, z=2.2, separar=False))
    # pés descalços (a flutuar um pouco) e redemoinhos de vento
    P.append(Parte(elipse(21, 44 + dy, 2.4, 1.4), PELE_M, z=1.5))
    P.append(Parte(elipse(28, 44 + dy, 2.6, 1.4), PELE_M, z=2.5))
    for i, (wx, wy) in enumerate(((13, 46), (30, 46), (22, 47))):
        o = (t + i) % 4
        px(P, [(wx + o, wy), (wx + o + 1, wy), (wx + o + 2, wy), (wx + o + 3, wy - 1), (wx + o + 2, wy - 2)], '#c7dcd0' if i % 2 else '#8fd3ff', 30)
    # cabeça careca com sobrancelhas compridas e barba branca
    cab = elipse(27, 10 + dy, 4.6, 5)
    P.append(Parte(cab, PELE_M, z=4, luz=0.2))
    px(P, [(29, 6 + dy), (30, 6 + dy)], '#4d9be6', 4.1)                         # marca do vento na testa
    px(P, [(24, 7 + dy), (25, 6 + dy)], '#fdcbb0', 4.2)                         # brilho da careca
    px(P, [(23, 11 + dy), (24, 11 + dy)], '#cd683d', 4.1)                       # orelha
    # olhos fechados (sereno), a não ser no quadro 2 em que espreita
    if t == 2:
        px(P, [(29, 10 + dy), (30, 10 + dy)], '#323353', 4.3)
        px(P, [(29, 10 + dy)], '#8fd3ff', 4.31)
    else:
        px(P, [(29, 10 + dy), (30, 11 + dy), (31, 10 + dy)], '#7a3045', 4.3)
    sob = [(29, 8 + dy), (30, 8 + dy), (31, 8 + dy), (32, 9 + dy), (33, 10 + dy + [0, 1, 1, 0][t])]
    px(P, sob, '#ffffff', 4.4)
    px(P, [(32, 11 + dy)], '#e6904e', 4.3)                                      # nariz
    barba = poligono([(26.5, 13 + dy), (32, 13 + dy), (31, 17 + dy), (29, 20 + dy + [0, 0, 1, 1][t]), (27, 16 + dy)])
    P.append(Parte(barba, NUVEM, z=5))
    px(P, [(29, 15 + dy), (30, 17 + dy)], '#9babb2', 5.1)
    # contas ao pescoço
    for i, (bx, by) in enumerate(((22, 15), (23, 17), (25, 18), (27, 18))):
        P.append(Parte(elipse(bx, by + dy, 1.2, 1.2), CASCA, z=5.2))
    # bastão de madeira com fitas
    sx = 36
    P.append(Parte({(sx, y) for y in range(4 + dy, 47)} | {(sx + 1, y) for y in range(4 + dy, 47)}, CASCA, z=6, volume='cilindro_h'))
    P.append(Parte(borda(elipse(36.5, 3 + dy, 2.6, 2.6)), BRONZE, z=6.1))
    for i, c in enumerate(('#8fd3ff', '#ffffff')):
        fita = []
        for k in range(9):
            fita.append((sx + 2 + k, 6 + dy + i * 2 + round(math.sin(k * 0.8 - t * 1.6 + i) * 1.2)))
        px(P, fita, c, 5.9 + i * 0.01)
    # braço (manga larga) e mão no bastão
    P.append(Parte(capsula(29, 17 + dy, 34, 24 + dy, 2.6), LAR, z=7))
    P.append(Parte(elipse(35.5, 24.5 + dy, 1.8, 1.8), PELE_M, z=7.1, luz=0.2))
    return desenhar(P, 48, 48)


def senhor_dos_trovoes(t):
    """Senhor dos Trovões: gigante de barba branca e elmo alado, de pé numa nuvem negra, com um martelo de ouro
    a faiscar; raios a estalar na nuvem."""
    P = []
    dy = [0, -1, -1, 0][t]
    # nuvem de trovoada (em baixo, à frente das pernas)
    for i, (cx, cy, r) in enumerate(((12, 41, 5), (19, 38, 6), (27, 38, 6.5), (35, 41, 5), (23, 43, 6), (15, 44, 4.5), (32, 44, 4.5))):
        P.append(Parte(elipse(cx, cy + dy, r, r * 0.8), TROVOADA_CLARA, z=10 + i * 0.01, luz=0.1))
    px(P, [(17, 34 + dy), (18, 33 + dy), (26, 33 + dy), (27, 32 + dy)], '#9babb2', 10.2)
    if t in (1, 3):   # raio por baixo da nuvem
        px(P, raio(20 + t, 45, 1, t, passo=2) + [(22, 47)], '#fbff86', 9)
    # braço de trás (punho cerrado a faiscar)
    P.append(Parte(capsula(18, 19 + dy, 13, 28 + dy, 2.8), CEU, z=1))
    P.append(Parte(elipse(12.5, 30 + dy, 2.8, 2.8), PELE, z=1.1))
    faiscas(P, 12, 30 + dy, 4, t, 9, n=3, z=20)
    # tronco largo (túnica azul) com cinto
    tronco = poligono([(17, 16 + dy), (33, 16 + dy), (34, 30 + dy), (31, 38 + dy), (19, 38 + dy), (16, 30 + dy)])
    P.append(Parte(tronco, CEU, z=2, volume='cilindro_v'))
    P.append(Parte(retangulo(17, 30 + dy, 33, 32 + dy), CASCA, z=2.1))
    P.append(Parte(retangulo(24, 29 + dy, 27, 33 + dy), OURO, z=2.2))
    px(P, [(25, 30 + dy), (26, 31 + dy), (25, 32 + dy)], '#9e4539', 2.3)        # raio na fivela
    # pele de lobo nos ombros
    pelo = elipse(20, 17 + dy, 5, 3.2) | elipse(30, 17 + dy, 5, 3.2)
    P.append(Parte(pelo, ROCHA, z=2.5))
    px(P, [(17, 18 + dy), (19, 19 + dy), (21, 18 + dy), (28, 19 + dy), (31, 19 + dy)], '#3e3546', 2.6)
    # cabeça com olhos amarelos que brilham
    cab = elipse(27, 11 + dy, 4.6, 4.8)
    P.append(Parte(cab, PELE, z=3, luz=0.2))
    px(P, [(29, 10 + dy), (30, 10 + dy), (29, 11 + dy), (30, 11 + dy)], '#f9c22b', 3.2)
    px(P, [(30, 10 + dy)], '#ffffff', 3.21)
    px(P, [(28, 9 + dy), (29, 9 + dy), (30, 9 + dy), (31, 9 + dy)], '#c7dcd0', 3.3)   # sobrancelha branca
    # barba enorme branca (abana com o vento)
    o = [0, 1, 1, 0][t]
    barba = poligono([(24, 12 + dy), (27, 13 + dy), (33, 13 + dy), (33.5, 17 + dy), (31, 25 + dy), (29 - o, 28 + dy), (26, 23 + dy), (23, 17 + dy)])
    P.append(Parte(barba, NUVEM, z=4))
    for k in range(4):
        px(P, [(25 + k * 2, 17 + dy + k % 2), (25 + k * 2, 18 + dy + k % 2)], '#9babb2', 4.1)
    px(P, [(30, 15 + dy), (31, 15 + dy)], '#6e2727', 4.2)                         # boca
    px(P, [(32, 11 + dy)], '#fca790', 4.2)                                        # nariz
    # elmo de prata com asinhas
    elmo = {p for p in elipse(27, 9 + dy, 5.2, 4.8) if p[1] <= 7 + dy}
    P.append(Parte(elmo, FERRO, z=5))
    px(P, [(x, 7 + dy) for x in range(22, 33)], '#625565', 5.1)
    for i, (ex, ey) in enumerate(((19, 2), (17, 4), (20, 0))):
        P.append(Parte(capsula(23, 6 + dy, ex - o, ey + dy, 1.1), NUVEM, z=4.9 + i * 0.01))
    # braço da frente a erguer o martelo de relâmpago
    hx, hy = 36, 20 + dy
    P.append(Parte(capsula(31, 19 + dy, hx - 1, hy + 2, 2.8), CEU, z=6))
    P.append(Parte({(hx, y) for y in range(hy - 12, hy + 6)} | {(hx + 1, y) for y in range(hy - 12, hy + 6)}, CASCA, z=6.5))
    cabeca_m = retangulo(hx - 5, hy - 19, hx + 6, hy - 11, canto=1)
    P.append(Parte(cabeca_m, OURO, z=7, volume='cilindro_h'))
    px(P, [(hx - 1, hy - 18), (hx, hy - 17), (hx - 1, hy - 16), (hx + 1, hy - 15), (hx, hy - 14), (hx + 1, hy - 13)], '#4d65b4', 7.1)
    px(P, [(hx - 4, hy - 18), (hx - 3, hy - 18)], '#ffffff', 7.1)
    P.append(Parte(elipse(hx + 0.5, hy + 2.5, 2.4, 2.4), PELE, z=7.2, luz=0.2))  # mão
    # raios a estalar à volta do martelo
    faiscas(P, hx, hy - 15, 9, t, 2, n=6, z=21)
    if t % 2 == 0:
        px(P, raio(hx + 7, hy - 22 if hy - 22 >= 0 else 0, 3, t + 4, passo=2), '#fbff86', 20)
    else:
        px(P, raio(hx - 8, hy - 21 if hy - 21 >= 0 else 0, 2, t + 7, passo=2), '#8fd3ff', 20)
    return desenhar(P, 48, 48)


# =====================================================================================================
# GUARDIÕES E BOSSES GRANDES (64×64)
# =====================================================================================================

BARRIGA = ['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2', '#8ff8e2']


def baleia_das_nuvens(t):
    """Baleia das Nuvens: baleia branca com a barriga verde-água às riscas, cracas na cabeça, esguicho de vento
    e nuvens à volta da barriga (nada nelas)."""
    P = []
    dy = [0, -1, -1, 0][t]
    cauda = [0, -3, -4, -1][t]
    # barbatana de trás
    P.append(Parte(poligono([(44, 38 + dy), (41, 38 + dy), (37, 46 + dy), (40, 46 + dy)]), NUVEM_SOMBRA, z=0.5))
    # cauda e barbatana caudal (sobe e desce)
    P.append(Parte(capsula(18, 31 + dy, 7, 29 + dy + cauda // 2, 4.2), NUVEM, z=1, volume='cilindro_h'))
    fx, fy = 6, 29 + dy + cauda // 2
    lob1 = capsula(fx + 2, fy, fx - 5, fy - 8 + cauda, 2.4) | capsula(fx + 1, fy - 1, fx - 2, fy - 9 + cauda, 1.6)
    lob2 = capsula(fx + 2, fy + 1, fx - 5, fy + 7 + cauda, 2.2) | capsula(fx + 1, fy + 1, fx - 2, fy + 8 + cauda, 1.4)
    P.append(Parte(lob2, NUVEM_SOMBRA, z=0.8))
    P.append(Parte(lob1, NUVEM, z=1.1))
    # corpo
    corpo = elipse(36, 31 + dy, 23, 12.5)
    P.append(Parte(corpo, NUVEM, z=2, luz=0.1))
    # barriga às riscas (pregas)
    barriga = {(x, y) for (x, y) in corpo if y >= 33 + dy + (x - 36) * 0.06 + max(0, 30 - x) * 0.25}
    P.append(Parte(barriga, BARRIGA, z=2.1, separar=False))
    pregas = [(x, y) for (x, y) in barriga if (y - dy) % 3 == 0 and (x, y - 1) in barriga]
    px(P, pregas, '#0b8a8f', 2.2)
    # sardas claras e cracas
    pintas(P, corpo - barriga, NUVEM, 2.3, 4)
    for (bx, by) in ((44, 21), (47, 22), (42, 22), (50, 23)):
        px(P, [(bx, by + dy), (bx + 1, by + dy)], '#7f708a', 2.4)
        px(P, [(bx, by + dy - 1), (bx + 1, by + dy - 1)], '#c7dcd0', 2.41)
    # olho, boca
    px(P, elipse(49.5, 31.5 + dy, 1.8, 1.8), '#323353', 3)
    px(P, [(49, 30 + dy)], '#ffffff', 3.1)
    px(P, [(50, 32 + dy)], '#4d65b4', 3.1)
    px(P, [(47, 29 + dy), (48, 28 + dy), (49, 28 + dy), (50, 28 + dy), (51, 29 + dy)], '#9babb2', 3)
    boca = [(58 - k, 34 + dy + (1 if k > 4 else 0) + (1 if k > 9 else 0)) for k in range(15)]
    px(P, boca, '#45293f', 3)
    # barbatana da frente (abana)
    ab = [0, 1, 2, 1][t]
    P.append(Parte(poligono([(44, 37 + dy), (37, 37 + dy), (30 - ab, 45 + dy + ab), (33 - ab, 47 + dy + ab), (39, 43 + dy)]), NUVEM, z=4))
    # esguicho de vento pelo espiráculo
    ex, ey = 42, 19 + dy
    for i in range(3):
        h = (t + i) % 4
        r = 1.5 + h * 0.5
        P.append(Parte(elipse(ex - 2 + i * 2 + h, ey - 3 - h * 2, r, r * 0.8), ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=0.3))
    # nuvens à volta da barriga (à frente)
    nuv = set()
    for i, (cx, cy, r) in enumerate(((20, 44, 4.5), (27, 44, 6), (37, 45, 5.5), (46, 45, 4.5), (13, 46, 3.5), (32, 48, 6), (52, 47, 3.2))):
        o = (t + i) % 2
        nuv |= elipse(cx + o, cy, r, r * 0.75)
    nuv = {p for p in nuv if p[1] <= 52}
    P.append(Parte(nuv, NUVEM, z=6, luz=0.35))
    px(P, [(p[0], p[1]) for p in borda(nuv) if p[1] >= 51], '#9babb2', 6.1)
    px(P, [(18 + t, 44), (19 + t, 44), (30, 43), (31, 43), (42 - t, 45)], '#ffffff', 6.2)
    return desenhar(P, 64, 64)


def carruagem_do_sol(t):
    """Carruagem do Sol: carro dourado com um disco do sol e uma roda que gira, puxado por um cavalo de fogo
    (crina e cauda de chamas)."""
    P = []
    dy = [0, 0, 1, 1][t]
    # ---- cavalo de fogo (à frente, à direita)
    CAV = FOGO
    # pernas de trás e da frente (de trás mais escuras)
    pos = [(40, 46, 39, 60), (55, 45, 56, 60)]
    for i, (x0, y0, x1, y1) in enumerate(pos):
        P.append(Parte(capsula(x0, y0 + dy, x1 - 2, y1, 1.6), ['#6e2727', '#9e4539', '#ea4f36', '#fb6b1d', '#f79617'], z=3))
    for i, (x0, y0, x1, y1) in enumerate(pos):
        P.append(Parte(capsula(x0 + 3, y0 + dy, x1 + 2, y1, 1.8), CAV, z=6))
        P.append(Parte(retangulo(x1, y1, x1 + 3, y1 + 1), OURO, z=6.1))          # cascos de ouro
    corpo = elipse(47, 41 + dy, 11, 6.5)
    P.append(Parte(corpo, CAV, z=5))
    pintas(P, corpo, CAV, 5.01, 2)
    # pescoço e cabeça
    P.append(Parte(capsula(54, 39 + dy, 58, 30 + dy, 3.6), CAV, z=7))
    cab = capsula(57, 28 + dy, 63, 32 + dy, 3.0)
    P.append(Parte(cab, CAV, z=8, luz=0.1))
    px(P, [(59, 27 + dy), (60, 27 + dy)], '#ffffff', 8.2)                      # olho a arder
    px(P, [(59, 28 + dy)], '#fbff86', 8.2)
    px(P, [(63, 32 + dy)], '#9e4539', 8.2)                                       # narina
    px(P, [(57, 25 + dy), (58, 24 + dy)], '#f9c22b', 7.9)                       # orelha
    # crina de chamas (dança)
    for i in range(6):
        bx, by = 56 - i * 1.4, 26 + i * 2.3 + dy
        h = 5 + ((i + t) % 3) * 2
        P.append(Parte(capsula(bx, by, bx - h, by - 3 - ((i + t) % 2), 1.3), CHAMA, z=6.5 + i * 0.01))
    # cauda de chamas
    for i in range(3):
        h = [0, 2, 1, 3][(t + i) % 4]
        P.append(Parte(capsula(37, 38 + dy + i, 31 - h, 34 + i * 3 + dy, 1.4), CHAMA, z=4.5 + i * 0.01))
    # arreio dourado e varal até ao carro
    px(P, linha(26, 44 + dy, 43, 41 + dy), '#f9c22b', 4.2)
    P.append(Parte(capsula(46, 36 + dy, 46, 46 + dy, 1.0), OURO, z=5.5))
    # ---- o carro dourado (atrás, à esquerda)
    carro = poligono([(4, 34 + dy), (10, 31 + dy), (28, 37 + dy), (30, 47 + dy), (6, 47 + dy)])
    P.append(Parte(carro, OURO, z=2, volume='cilindro_v'))
    px(P, [(x, 44 + dy) for x in range(7, 29)], '#9e4539', 2.1)
    px(P, [(x, 45 + dy) for x in range(7, 29, 3)], '#f9c22b', 2.11)
    # disco do sol nas costas do carro, com raios que giram
    sx, sy = 9, 24 + dy
    raios = []
    for k in range(8):
        a = k * math.pi / 4 + t * math.pi / 16
        raios.append(capsula(sx + math.cos(a) * 6, sy + math.sin(a) * 6, sx + math.cos(a) * 10, sy + math.sin(a) * 10, 1.0))
    P.append(Parte(set().union(*raios), CHAMA, z=1))
    P.append(Parte(elipse(sx, sy, 6.5, 6.5), OURO, z=1.2))
    px(P, borda(elipse(sx, sy, 4, 4)), '#f79617', 1.3)
    px(P, [(sx - 1, sy - 1), (sx + 1, sy - 1)], '#9e4539', 1.31)               # carinha do sol
    px(P, [(sx - 1, sy + 2), (sx, sy + 2), (sx + 1, sy + 2)], '#9e4539', 1.31)
    # roda grande com raios que giram
    rx, ry, R = 18, 51, 9
    P.append(Parte(borda(elipse(rx, ry, R, R)) | borda(elipse(rx, ry, R - 1, R - 1)), OURO_VELHO, z=7))
    for k in range(4):
        a = k * math.pi / 4 + t * math.pi / 8
        P.append(Parte(linha(rx - math.cos(a) * (R - 2), ry - math.sin(a) * (R - 2), rx + math.cos(a) * (R - 2), ry + math.sin(a) * (R - 2)),
                       None, z=7.1, separar=False, cor='#f79617'))
    P.append(Parte(elipse(rx, ry, 2.2, 2.2), OURO, z=7.2))
    # faúlhas a subir
    for i, (fx, fy) in enumerate(((50, 20), (34, 26), (60, 16), (22, 30))):
        y = fy - (t * 2 + i * 3) % 8
        px(P, [(fx, y)], '#fbff86' if i % 2 else '#f79617', 20)
    return desenhar(P, 64, 64)


def golem_ilha(t):
    """Golem-Ilha: uma ilha flutuante com braços e pernas de rocha; relva e uma árvore em cima, raízes penduradas,
    cristais de oricalco, uma cascatinha e uma cara esculpida com olhos azuis."""
    P = []
    dy = [0, 0, 1, 1][t]
    # braço de trás
    for i, (x, y, r) in enumerate(((13, 30, 4.5), (9, 38, 4.2), (8, 46, 4.8))):
        P.append(Parte(elipse(x, y + dy, r, r * 0.9), ROCHA, z=1 + i * 0.01, luz=-0.2))
    # pernas de rocha
    P.append(Parte(capsula(26, 50, 25, 58, 4.2), ROCHA, z=2, luz=-0.15))
    P.append(Parte(capsula(37, 50, 38, 58, 4.5), ROCHA, z=3))
    P.append(Parte(retangulo(19, 58, 30, 62, canto=1), ROCHA, z=2.1, luz=-0.15))
    P.append(Parte(retangulo(33, 58, 45, 62, canto=1), ROCHA, z=3.1))
    px(P, [(37, 53), (38, 54), (38, 55)], '#3e3546', 3.2)
    # a ilha (cone de pedra virado ao contrário) com camadas de terra
    ilha = poligono([(9, 22 + dy), (55, 22 + dy), (52, 30 + dy), (45, 42 + dy), (38, 52 + dy), (27, 52 + dy), (19, 42 + dy), (12, 30 + dy)])
    P.append(Parte(ilha, TERRA, z=4, volume='cilindro_v'))
    camadas = []
    for (x, y) in ilha:
        if (y - dy) in (27, 33, 40, 46) and (x + y) % 7 != 0 and not (31 <= x <= 48 and (y - dy) in (27, 33, 40)):
            camadas.append((x, y))
    px(P, camadas, '#45293f', 4.1)
    pintas(P, ilha, TERRA, 4.2, 5)
    # pedras embutidas e cristais de oricalco
    for (sx, sy, r) in ((16, 30, 2.4), (24, 44, 2.0), (46, 40, 1.8)):
        P.append(Parte(elipse(sx, sy + dy, r, r * 0.8), ROCHA, z=4.3))
    for (cx, cy) in ((21, 36), (38, 46), (28, 41)):
        cri = poligono([(cx, cy + dy - 3), (cx + 2, cy + dy), (cx, cy + dy + 2), (cx - 2, cy + dy)])
        P.append(Parte(cri, ['#9e4539', '#f79617', '#fbb954', '#fbff86', '#ffffff'], z=4.4))
    # raízes penduradas por baixo
    for i, (rx, ln) in enumerate(((22, 6), (29, 9), (34, 7), (41, 5))):
        o = [0, 1, 0, -1][(t + i) % 4]
        pts = [(rx + round(math.sin(k * 0.7 + i) * 1) + (o if k > ln // 2 else 0), 46 + dy + k + (rx in (29, 34)) * 5 + (rx in (22, 41)) * 1) for k in range(ln)]
        px(P, pts, '#694f62', 3.9)
    # relva por cima, com tufos
    relva = poligono([(8, 19 + dy), (56, 19 + dy), (56, 24 + dy), (8, 24 + dy)]) | elipse(32, 20 + dy, 24, 3)
    P.append(Parte(relva, FOLHA, z=5))
    for x in range(9, 56, 3):
        h = 1 + (x * 7) % 3
        px(P, [(x, 18 + dy - k + (1 if k == h else 0)) for k in range(h)], '#91db69', 5.1)
    px(P, [(x, 24 + dy) for x in range(10, 55, 2)], '#239063', 5.05)
    for (fx, c) in ((14, '#f04f78'), (46, '#fbff86'), (52, '#ffffff')):
        px(P, [(fx, 17 + dy)], c, 5.2)
    # a árvore em cima da cabeça (à esquerda)
    P.append(Parte(capsula(20, 19 + dy, 21, 9 + dy, 1.8), CASCA, z=4.8))
    P.append(Parte(capsula(21, 13 + dy, 25, 10 + dy, 0.9), CASCA, z=4.81))
    a = [0, 1, 0, -1][t]
    for i, (cx, cy, r) in enumerate(((16 + a, 7, 5), (24 + a, 5, 5.5), (20 + a, 2, 4.2), (27 + a, 9, 3.6))):
        m = elipse(cx, cy + dy, r, r * 0.85)
        P.append(Parte(m, FOLHA, z=4.85 + i * 0.01))
        pintas(P, m, FOLHA, 4.85 + i * 0.01, 3 + i, n=11)
    px(P, [(22 + a, 6 + dy), (17 + a, 8 + dy)], '#f04f78', 4.95)                # pêssegos celestes
    # cascatinha a cair pela borda direita
    for k in range(10):
        y = 22 + dy + k
        if (k + t) % 3 != 2:
            px(P, [(56 + (k > 3), y)], '#8fd3ff' if (k + t) % 2 else '#ffffff', 6)
    # cara esculpida na pedra (à direita): sobrolho, olhos azuis, boca rachada
    P.append(Parte(capsula(33, 29 + dy, 46, 28 + dy, 1.5), TERRA, z=6.5, volume='cilindro_h', luz=0.2))
    for ex in (35, 42):
        px(P, elipse(ex + 1, 32 + dy, 2.0, 1.8), '#2e222f', 7)
        px(P, [(ex + 1, 32 + dy), (ex + 2, 32 + dy), (ex + 1, 33 + dy)], '#4d9be6' if t % 2 == 0 else '#8fd3ff', 7.1)
        px(P, [(ex + 1, 31 + dy)], '#ffffff', 7.2)
    boca = [(34 + k, 37 + dy + ((k // 2) % 2)) for k in range(12)]
    px(P, boca, '#2e222f', 7)
    px(P, [(36, 38 + dy), (40, 38 + dy)], '#c7dcd0', 7.1)                     # dentes de pedra
    # braço da frente (pedras) com punho
    for i, (x, y, r) in enumerate(((51, 30, 4.6), (55, 38, 4.2), (56, 46, 5.2))):
        P.append(Parte(elipse(x, y + dy, r, r * 0.9), ROCHA, z=8 + i * 0.01))
    px(P, [(54, 44 + dy), (55, 44 + dy), (53, 36 + dy)], '#c7dcd0', 8.1)
    px(P, [(57, 48 + dy), (58, 47 + dy)], '#3e3546', 8.1)
    px(P, [(53, 41 + dy), (54, 41 + dy), (55, 42 + dy)], '#547e64', 8.2)   # musgo
    return desenhar(P, 64, 64)


def leao_alado_de_marmore(t):
    """Leão Alado de Mármore: leão de mármore branco com veios cinzentos, juba de caracóis esculpidos, asas de
    penas de pedra, coleira de ouro e olhos azuis a brilhar."""
    P = []
    dy = [0, 0, 1, 1][t]
    flap = [0, 6, 10, 4][t]
    cau = [0, 1, 2, 1][t]
    # asa de trás
    asa(P, 30, 31 + dy, 21, 112 + flap, MARMORE_ESC, z=0.5, n=6, r=2.0, abre=66)
    # pernas de trás (longe)
    P.append(Parte(capsula(22, 44 + dy, 23, 58, 2.6), MARMORE_ESC, z=1))
    P.append(Parte(capsula(40, 45 + dy, 42, 58, 2.6), MARMORE_ESC, z=1))
    for x in (23, 42):
        P.append(Parte(elipse(x + 1, 59, 3.2, 2.2), MARMORE_ESC, z=1.1))
    # cauda com tufo
    P.append(Parte(capsula(14, 39 + dy, 8, 33 + dy - cau, 1.4) | capsula(8, 33 + dy - cau, 7, 27 + dy - cau, 1.3), MARMORE, z=1.5))
    P.append(Parte(elipse(7, 25 + dy - cau, 2.6, 3), MARMORE_ESC, z=1.6))
    # corpo
    corpo = elipse(30, 40 + dy, 16, 8.5)
    P.append(Parte(corpo, MARMORE, z=2))
    veios(P, corpo, '#9babb2', 2.01, 2, dens=11)
    px(P, [(24, 37 + dy), (25, 38 + dy), (25, 39 + dy), (26, 40 + dy)], '#7f708a', 2.02)         # racha
    # pernas da frente (perto)
    P.append(Parte(elipse(18, 44 + dy, 5.5, 6), MARMORE, z=3))              # coxa
    P.append(Parte(capsula(17, 47 + dy, 17, 58, 2.9), MARMORE, z=3.1))
    P.append(Parte(capsula(44, 44 + dy, 46, 58, 3.0), MARMORE, z=3.1))
    for x in (17, 46):
        P.append(Parte(elipse(x + 1.5, 59.5, 3.6, 2.4), MARMORE, z=3.2))
        px(P, [(x + 1, 61), (x + 3, 61)], '#7f708a', 3.3)                     # dedos
    # coleira de ouro com pedra azul
    P.append(Parte(capsula(41, 34 + dy, 44, 44 + dy, 1.6), OURO, z=4.5))
    px(P, [(43, 39 + dy), (43, 40 + dy)], '#4d9be6', 4.6)
    # juba de caracóis esculpidos
    juba = elipse(46, 31 + dy, 9.5, 10.5)
    P.append(Parte(juba, MARMORE_ESC, z=4))
    caracois = []
    for (x, y) in juba - borda(juba):
        if (x + 2 * y) % 5 == 0 and (x * 3 + y) % 4 == 0:
            caracois += [(x, y), (x + 1, y)]
    px(P, [p for p in caracois if p in juba], '#625565', 4.01)
    for k in range(10):   # pontas dos caracóis à volta
        a = math.pi * 0.55 + k * 0.33
        x, y = 46 + math.cos(a) * 10, 31 + dy + math.sin(a) * 11
        P.append(Parte(elipse(x, y, 2.0, 2.0), MARMORE_ESC, z=3.9))
    # cabeça
    cab = elipse(50, 31 + dy, 6.5, 6.5)
    P.append(Parte(cab, MARMORE, z=5, luz=0.15))
    focinho = elipse(56, 34 + dy, 4, 3.2)
    P.append(Parte(focinho, MARMORE, z=5.5))
    px(P, [(59, 32 + dy), (60, 32 + dy), (60, 33 + dy)], '#625565', 5.6)    # nariz
    px(P, [(55, 36 + dy), (56, 37 + dy), (57, 37 + dy), (58, 36 + dy), (59, 36 + dy)], '#625565', 5.6)  # boca
    px(P, [(56, 38 + dy)], '#ffffff', 5.6)                                    # dente
    px(P, [(51, 28 + dy), (52, 27 + dy), (53, 27 + dy), (54, 28 + dy)], '#7f708a', 5.6)  # sobrolho
    px(P, [(52, 29 + dy), (53, 29 + dy), (52, 30 + dy), (53, 30 + dy)], '#323353', 5.7)
    px(P, [(53, 29 + dy), (53, 30 + dy)], '#8fd3ff' if t != 2 else '#ffffff', 5.8)
    px(P, [(52, 29 + dy)], '#4d9be6', 5.8)
    px(P, [(47, 24 + dy), (48, 23 + dy)], '#9babb2', 5.6)                     # orelha
    # asa da frente (penas de pedra com a ponta dourada)
    asa(P, 29, 32 + dy, 22, 124 + flap, MARMORE, z=6, n=6, r=2.1, abre=64, cob=MARMORE_ESC)
    a = math.radians(124 + flap)
    px(P, linha(29 + math.cos(a) * 4, 32 + dy - math.sin(a) * 4, 29 + math.cos(a) * 19, 32 + dy - math.sin(a) * 19), '#f9c22b', 6.2)
    return desenhar(P, 64, 64)


GRIFO = ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbb954']
GRIFO_ESC = ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#f9c22b']


def grifo_real(t):
    """Grifo Real: corpo de leão dourado, cabeça e asas de águia, crista de penas brancas, olhos de âmbar,
    patas da frente de águia (garras) e de trás de leão, cauda com tufo."""
    P = []
    dy = [0, 0, 1, 1][t]
    flap = [0, 8, 14, 6][t]
    cau = [0, 1, 2, 1][t]
    # asa de trás
    asa(P, 30, 32 + dy, 18, 108 + flap, GRIFO_ESC, z=0.5, n=6, r=1.8, abre=66)
    # pernas de longe
    P.append(Parte(capsula(22, 44 + dy, 22, 58, 2.6), GRIFO_ESC, z=1))
    P.append(Parte(capsula(42, 45 + dy, 44, 57, 1.8), ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#f9c22b'], z=1))
    P.append(Parte(elipse(23, 59, 3.2, 2.2), GRIFO_ESC, z=1.1))
    px(P, [(42, 59), (44, 59), (46, 59), (43, 58), (45, 58)], '#625565', 1.2)
    # cauda de leão com tufo
    P.append(Parte(capsula(14, 39 + dy, 8, 33 + dy - cau, 1.4) | capsula(8, 33 + dy - cau, 6, 27 + dy - cau, 1.3), GRIFO, z=1.5))
    P.append(Parte(elipse(6, 25 + dy - cau, 2.6, 3), ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e'], z=1.6))
    # corpo de leão
    corpo = elipse(30, 40 + dy, 16, 8.5)
    P.append(Parte(corpo, GRIFO, z=2))
    pintas(P, corpo, GRIFO, 2.01, 7)
    # penas do peito (a passar para águia)
    peito = {p for p in elipse(42, 39 + dy, 6, 7) if p in corpo or p[0] > 40}
    P.append(Parte(peito, ['#ab947a', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=2.5, luz=-0.1))
    escamas_penas(P, peito, '#9babb2', 2.51, passo=3)
    # pata de trás (perto)
    P.append(Parte(elipse(18, 44 + dy, 5.5, 6), GRIFO, z=3))
    P.append(Parte(capsula(17, 47 + dy, 17, 58, 2.9), GRIFO, z=3.1))
    P.append(Parte(elipse(18.5, 59.5, 3.6, 2.4), GRIFO, z=3.2))
    px(P, [(18, 61), (20, 61)], '#9e4539', 3.3)
    # pata da frente de águia (escamas amarelas e garras)
    P.append(Parte(capsula(45, 45 + dy, 46, 57, 2.0), OURO, z=3.1))
    px(P, [(45, 49 + dy), (46, 51 + dy), (45, 53 + dy), (46, 55)], '#f79617', 3.15)
    for (gx, gy) in ((43, 59), (45, 60), (48, 60), (50, 59)):
        px(P, [(gx, gy), (gx + 1, gy - 1)], '#c7dcd0', 3.2)
        px(P, [(gx, gy)], '#2e222f', 3.21)
    P.append(Parte(elipse(46.5, 58, 3, 1.6), OURO, z=3.18))
    # pescoço e cabeça de águia (dourada) com crista branca
    P.append(Parte(capsula(43, 37 + dy, 48, 29 + dy, 4.2), GRIFO, z=4))
    escamas_penas(P, capsula(43, 37 + dy, 48, 29 + dy, 3.2), '#cd683d', 4.01, passo=3)
    o = [0, 1, 1, 0][t]
    for i, (cx, cy) in enumerate(((40, 18), (38, 22), (41, 15), (38, 26))):
        P.append(Parte(capsula(48, 24 + dy, cx - o, cy + dy, 1.6 - i * 0.15), NUVEM, z=4.5 + i * 0.01))
    cab = elipse(51, 26 + dy, 5.8, 5.2)
    P.append(Parte(cab, GRIFO, z=5, luz=0.2))
    bico = poligono([(55, 23 + dy), (60, 24 + dy), (62, 27 + dy), (61, 30 + dy), (59, 28 + dy), (55, 29 + dy)])
    P.append(Parte(bico, ['#4c3e24', '#9e4539', '#cd683d', '#e6904e', '#fbb954'], z=6))
    px(P, [(61, 29 + dy), (61, 30 + dy)], '#2e222f', 6.1)
    px(P, [(57, 27 + dy), (58, 27 + dy)], '#6e2727', 6.1)
    # olho de âmbar
    px(P, [(52, 24 + dy), (53, 24 + dy), (52, 25 + dy), (53, 25 + dy)], '#f79617', 7)
    px(P, [(53, 24 + dy), (53, 25 + dy)], OUT, 7.1)
    px(P, [(52, 24 + dy)], '#ffffff', 7.2)
    px(P, [(51, 23 + dy), (52, 23 + dy), (53, 23 + dy), (54, 23 + dy)], '#ffffff', 7)   # sobrancelha branca
    # asa da frente com pontas brancas
    asa(P, 29, 33 + dy, 19, 124 + flap, GRIFO, z=8, n=6, r=1.8, abre=64, cob=GRIFO_ESC)
    a = math.radians(124 + flap)
    for i in range(6):
        tt = (i + 1) / 6
        bx, by = 29 + math.cos(a) * 19 * tt * 0.92, 33 + dy - math.sin(a) * 19 * tt * 0.92
        da = math.radians(124 + flap + 64 * (1 - tt) + 18 * tt)
        L = 19 * (0.42 + 0.5 * tt)
        px(P, [(bx + math.cos(da) * L, by - math.sin(da) * L), (bx + math.cos(da) * (L - 1), by - math.sin(da) * (L - 1))], '#ffffff', 8.2)
    # penas a voar
    for i, (fx, fy) in enumerate(((58, 8), (10, 10))):
        y = fy + (t + i * 2) % 4
        px(P, [(fx + (t % 2), y), (fx + 1 + (t % 2), y)], '#fbb954', 20)
    return desenhar(P, 64, 64)


def arcanjo_de_bronze(t):
    """Arcanjo de Bronze: autómato alado antigo de bronze com manchas de verdete, asas de penas de metal (lâminas),
    auréola de engrenagem, máscara lisa com olhos azuis e um núcleo a brilhar no peito; lança comprida."""
    P = []
    dy = [0, 0, 1, 1][t]
    flap = [0, 6, 10, 4][t]
    BR = BRONZE
    BR_ESC = ['#2e222f', '#4c3e24', '#9e4539', '#cd683d', '#e6904e']
    VERDETE = '#0eaf9b'
    nucleo = ['#30e1b9', '#8ff8e2', '#ffffff', '#8ff8e2'][t]
    # asas de metal (lâminas), a de trás mais escura
    asa(P, 26, 22 + dy, 22, 104 + flap, BR_ESC, z=0.4, n=7, r=1.6, abre=70)
    asa(P, 27, 22 + dy, 24, 124 + flap, BR, z=0.6, n=7, r=1.7, abre=66, cob=BR_ESC)
    # auréola de engrenagem atrás da cabeça
    gx, gy = 30, 9 + dy
    eng = borda(elipse(gx, gy, 7, 7)) | borda(elipse(gx, gy, 6, 6))
    for k in range(8):
        a = k * math.pi / 4 + t * math.pi / 16
        eng |= {(round(gx + math.cos(a) * 8), round(gy + math.sin(a) * 8))}
    P.append(Parte(eng, OURO_VELHO, z=0.8, separar=False))
    # pernas segmentadas
    for (x0, x1, z, R) in ((26, 25, 1, BR_ESC), (33, 35, 3, BR)):
        P.append(Parte(capsula(x0, 40, x0, 49, 2.6), R, z=z, volume='cilindro_v'))
        P.append(Parte(capsula(x0, 50, x1, 58, 2.4), R, z=z))
        P.append(Parte(elipse(x0, 49.5, 2.6, 2.4), FERRO if R is BR else ROCHA, z=z + 0.1))
        P.append(Parte(poligono([(x1 - 3, 58), (x1 + 4, 58), (x1 + 5, 62), (x1 - 3, 62)]), R, z=z + 0.2))
    px(P, [(34, 54), (35, 55)], VERDETE, 3.3)
    # saia de lâminas
    saia = poligono([(22, 34 + dy), (38, 34 + dy), (40, 43), (20, 43)])
    P.append(Parte(saia, BR, z=4, volume='cilindro_v'))
    px(P, [(x, y) for x in range(22, 40, 3) for y in range(37 + dy, 43)], '#4c3e24', 4.1)
    # tronco com o núcleo
    tronco = poligono([(21, 18 + dy), (38, 18 + dy), (37, 28 + dy), (34, 35 + dy), (25, 35 + dy), (22, 28 + dy)])
    P.append(Parte(tronco, BR, z=5, volume='cilindro_v'))
    px(P, borda(elipse(30, 25 + dy, 3.6, 3.6)), '#4c3e24', 5.1)
    px(P, elipse(30, 25 + dy, 2.4, 2.4), nucleo, 5.2)
    px(P, [(29, 24 + dy)], '#ffffff', 5.3)
    for (rx_, ry_) in ((23, 20), (36, 20), (24, 31), (35, 31)):
        px(P, [(rx_, ry_ + dy)], '#fbb954', 5.25)                           # rebites
    px(P, [(23, 25 + dy), (24, 26 + dy), (24, 27 + dy), (25, 28 + dy)], VERDETE, 5.25)
    px(P, [(23, 26 + dy)], '#0b8a8f', 5.26)
    # cabeça: máscara lisa com olhos em fenda azuis e crista
    cab = elipse(31.5, 11 + dy, 5, 5.6)
    P.append(Parte(cab, BR, z=6, luz=0.2))
    P.append(Parte(capsula(28, 6 + dy, 22, 3 + dy, 1.2), BR, z=5.9))             # crista
    px(P, [(x, 11 + dy) for x in range(31, 37)], '#2e222f', 6.1)
    px(P, [(33, 11 + dy), (34, 11 + dy), (36, 11 + dy)], nucleo, 6.2)
    px(P, [(34, 15 + dy), (35, 15 + dy)], '#4c3e24', 6.1)
    px(P, [(29, 7 + dy), (30, 7 + dy)], VERDETE, 6.15)
    px(P, [(29, 8 + dy), (28, 9 + dy)], '#fbb954', 6.15)
    # ombreira
    P.append(Parte(elipse(37, 19 + dy, 4.2, 3.4), BR, z=7))
    px(P, [(36, 18 + dy), (37, 18 + dy)], VERDETE, 7.1)
    # lança comprida de bronze (na vertical) e braço
    lx = 45
    P.append(Parte({(lx, y) for y in range(6 + dy, 63)}, None, z=8, separar=False, cor='#9e4539'))
    px(P, [(lx, y) for y in range(8 + dy, 63, 4)], '#e6904e', 8.01)
    ponta = poligono([(lx - 2.5, 7 + dy), (lx + 0.5, -2 + dy), (lx + 3.5, 7 + dy), (lx + 0.5, 9 + dy)])
    P.append(Parte(ponta, ['#4c3e24', '#9e4539', '#e6904e', '#fbb954', '#ffffff'], z=8.1))
    P.append(Parte(capsula(37, 21 + dy, lx - 2, 28 + dy, 2.2), BR, z=9))
    P.append(Parte(elipse(lx, 28.5 + dy, 2.3, 2.3), BR, z=9.1))
    px(P, [(lx - 1, 27 + dy)], '#fbb954', 9.2)
    # brilho que corre pela lâmina
    if t % 2 == 0:
        px(P, [(lx + 1, 2 + dy), (lx + 1, 0 + dy) if dy == 0 else (lx + 1, 1), (lx, 1 + dy), (lx + 2, 1 + dy)], '#ffffff', 20)
    return desenhar(P, 64, 64)


# =====================================================================================================
# GIGANTES (128×128)
# =====================================================================================================

def tempestade_viva(t):
    """Tempestade Viva: uma trovoada inteira com cara: um olho enorme no centro (âmbar, pupila em fenda), sobrolho
    de nuvem zangado, boca com dentes de relâmpago, raios a cair e chuva por baixo."""
    P = []
    dy = [0, -1, -1, 0][t]
    # chuva por baixo (atrás de tudo)
    rnd = random.Random(3)
    for i in range(26):
        x = rnd.randint(16, 112)
        y0 = 88 + ((rnd.randint(0, 40) + t * 9) % 40)
        px(P, [(x - k // 2, y0 + k) for k in range(4)], '#4d9be6' if i % 3 else '#8fd3ff', 0.1)
    # tufos de cima (mais claros) e a massa da nuvem
    cima = ((24, 44, 13), (40, 32, 15), (60, 26, 17), (80, 30, 15), (98, 38, 14), (110, 52, 10), (14, 58, 10))
    for i, (cx, cy, r) in enumerate(cima):
        m = elipse(cx, cy + dy, r, r * 0.85)
        P.append(Parte(m, TROVOADA_CLARA, z=1 + i * 0.01, luz=0.15))
        pintas(P, m, TROVOADA_CLARA, 1 + i * 0.01, i + 1, n=13)
    meio = ((22, 64, 14), (42, 66, 18), (66, 62, 22), (90, 64, 18), (108, 68, 12), (54, 78, 14), (80, 78, 14), (32, 78, 10), (98, 80, 10))
    for i, (cx, cy, r) in enumerate(meio):
        m = elipse(cx, cy + dy, r, r * 0.8)
        P.append(Parte(m, TROVOADA, z=2 + i * 0.01, luz=0.1))
        pintas(P, m, TROVOADA, 2 + i * 0.01, i + 9, n=13)
    # clarão dentro da nuvem (muda de sítio)
    fx, fy = [(36, 40), (84, 34), (60, 30), (100, 46)][t]
    px(P, [p for p in elipse(fx, fy + dy, 6, 4) if (p[0] + p[1]) % 2 == 0], '#9babb2', 1.5)
    px(P, [p for p in elipse(fx, fy + dy, 3, 2)], '#c7dcd0', 1.51)
    # o olho do centro (com pálpebras de nuvem)
    ex, ey = 68, 54 + dy
    olho_m = elipse(ex, ey, 13, 8.5)
    P.append(Parte(olho_m, ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=5))
    olhar = [0, 1, 2, 1][t]
    iris = elipse(ex + 2 + olhar, ey, 6.5, 6.5) & olho_m
    P.append(Parte(iris, ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'], z=5.1, separar=False))
    px(P, borda(elipse(ex + 2 + olhar, ey, 6.5, 6.5)) & olho_m, '#9e4539', 5.15)
    pupila = capsula(ex + 2 + olhar, ey - 4.5, ex + 2 + olhar, ey + 4.5, 1.4)
    px(P, pupila & olho_m, '#2e222f', 5.2)
    px(P, [(ex - 1 + olhar, ey - 3), (ex + olhar, ey - 3), (ex - 1 + olhar, ey - 2)], '#ffffff', 5.3)
    # veias de raio no branco do olho
    px(P, [(ex - 10, ey), (ex - 9, ey - 1), (ex - 8, ey), (ex - 7, ey + 1)], '#f9c22b', 5.05)
    # pálpebras / sobrolho zangado (tufos escuros em V)
    for i, (cx, cy, r) in enumerate(((50, 42, 7), (60, 41, 7.5), (71, 43, 7), (82, 41, 7.5), (90, 40, 6.5))):
        P.append(Parte(elipse(cx, cy + dy + (abs(cx - 70) * -0.12), r, r * 0.6), TROVOADA, z=6 + i * 0.01, luz=0.1))
    # boca com dentes de relâmpago
    boca = elipse(70, 76 + dy, 15, 4.5) - elipse(70, 72 + dy, 15, 3.5)
    P.append(Parte(boca, ['#2e222f', '#2e222f', '#2e222f', '#2e222f', '#2e222f'], z=6.5, separar=False))
    dentes = []
    for k in range(7):
        x = 58 + k * 4
        y = 75 + dy + (1 if k % 2 else 0)
        dentes += [(x, y), (x + 1, y + 1), (x, y + 2)]
    px(P, [p for p in dentes if p in boca], '#fbff86' if t % 2 == 0 else '#f9c22b', 6.6)
    # raios a cair (mudam todos os quadros)
    for k, (bx, sem) in enumerate([((30, 1), (96, 2)), ((48, 3), (104, 4)), ((26, 5), (86, 6)), ((40, 7), (100, 8))][t]):
        pts = raio(bx, 86 + dy, 9, sem, passo=4)
        px(P, [p for p in pts if p[1] < 128], '#fbff86', 8)
        px(P, [(p[0] + 1, p[1]) for p in pts if p[1] < 128 and (p[0] + p[1]) % 3 == 0], '#ffffff', 8.1)
    # faíscas à volta
    faiscas(P, 64, 56, 56, t, 11, n=10, z=9)
    return desenhar(P, 128, 128)


def serafim_caido(t):
    """Serafim Caído: anjo enorme de seis asas (três brancas em cima, três negras em baixo); metade da cara de luz
    e metade de sombra (olho dourado e olho vermelho); cabelo meio branco meio negro; auréola partida; manto de
    duas cores; uma foice de luz e sombra; penas negras a cair."""
    P = []
    dy = [0, -1, -2, -1][t]
    flap = [0, 4, 7, 3][t]
    sx, sy = 54, 50 + dy           # ombros (onde nascem as asas)
    BRANCA = NUVEM
    NEGRA = ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9']
    # seis asas: brancas para cima, negras para baixo (de trás para a frente)
    asa(P, sx, sy, 30, 72 + flap, BRANCA, z=0.3, n=8, r=2.5, abre=70, cob=MARMORE_ESC, luz=-0.15)
    asa(P, sx, sy, 34, 104 + flap, BRANCA, z=0.5, n=8, r=2.6, abre=68, cob=MARMORE_ESC, luz=-0.05)
    asa(P, sx, sy + 2, 38, 138 + flap, BRANCA, z=0.7, n=8, r=2.7, abre=66, cob=MARMORE_ESC)
    asa(P, sx, sy + 6, 38, 170 - flap, NEGRA, z=0.75, n=8, r=2.7, abre=62)
    asa(P, sx, sy + 8, 38, 202 - flap, NEGRA, z=0.6, n=8, r=2.6, abre=60)
    asa(P, sx, sy + 10, 32, 234 - flap, NEGRA, z=0.4, n=7, r=2.5, abre=56)
    # manto comprido: metade de luz (à frente) e metade de sombra (atrás), bainha esfarrapada
    manto = poligono([(50, 46 + dy), (74, 46 + dy), (78, 70 + dy), (86, 120), (40, 120), (46, 70 + dy)])
    bainha = {(x, y) for x in range(40, 87) for y in range(120, 124) if (x * 3) % 7 < 4 - (y - 120)}
    luz_m = {p for p in manto | bainha if p[0] >= 63}
    sombra_m = {p for p in manto | bainha if p[0] < 63}
    P.append(Parte(sombra_m, ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9'], z=2, volume='cilindro_v'))
    P.append(Parte(luz_m, MARMORE, z=2.1, volume='cilindro_v'))
    px(P, [(x, 118) for x in range(63, 86)], '#f9c22b', 2.2)                   # orla dourada
    px(P, [(x, 118) for x in range(41, 63, 2)], '#905ea9', 2.2)
    for (x, y0, y1) in ((70, 80, 116), (78, 84, 116), (54, 80, 116), (47, 90, 116)):
        px(P, [(x + (y - y0) // 14, y) for y in range(y0, y1, 1)], '#9babb2' if x >= 63 else '#45293f', 2.15)   # pregas
    px(P, [(63, y) for y in range(48 + dy, 120)], '#f9c22b', 2.3)               # a costura de ouro ao meio
    # cinto com uma pedra metade branca metade negra
    P.append(Parte(retangulo(47, 68 + dy, 78, 71 + dy), OURO_VELHO, z=2.4))
    px(P, [(62, 69 + dy), (62, 70 + dy)], '#ffffff', 2.5)
    px(P, [(63, 69 + dy), (63, 70 + dy)], '#6b3e75', 2.5)
    # pés descalços por baixo do manto
    P.append(Parte(elipse(72, 124, 4, 2), ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0'], z=1.9))
    # braço de trás (manga negra)
    P.append(Parte(capsula(52, 52 + dy, 44, 76 + dy, 4.2), NEGRA, z=1.5))
    P.append(Parte(elipse(43, 79 + dy, 3.4, 3.4), ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'], z=1.6))
    # cabeça: metade de luz (à frente) e metade de sombra
    hx, hy = 66, 34 + dy
    P.append(Parte(capsula(64, 40 + dy, 63, 47 + dy, 3.6), ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0'], z=3))  # pescoço
    cab = elipse(hx, hy, 8, 9)
    lado_luz = {p for p in cab if p[0] >= hx}
    lado_sombra = cab - lado_luz
    P.append(Parte(lado_luz, ['#cd683d', '#e6904e', '#fca790', '#fdcbb0', '#ffffff'], z=4, luz=0.3))
    P.append(Parte(lado_sombra, ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'], z=4, separar=False, luz=0.1))
    # cabelo comprido: branco por cima/à frente, negro atrás
    cab_b = {p for p in elipse(hx, hy - 5, 8.6, 5) if p[1] <= hy - 4 and p[0] >= hx - 1} | capsula(hx + 6, hy - 6, hx + 8, hy - 2, 1.4)
    cab_n = {p for p in elipse(hx, hy - 5, 8.6, 5) if p[1] <= hy - 4 and p[0] < hx - 1} \
        | capsula(hx - 7, hy - 3, hx - 12, hy + 16 + [0, 1, 1, 0][t], 3.0) | capsula(hx - 8, hy, hx - 16, hy + 12, 2.4)
    P.append(Parte(cab_n, ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9'], z=4.4))
    P.append(Parte(cab_b, MARMORE, z=4.5))
    px(P, [(hx - 4, hy - 9), (hx - 1, hy - 10), (hx + 2, hy - 9)], '#ffffff', 4.6)
    # olhos: dourado (luz) e vermelho (sombra)
    px(P, [(hx + 3, hy - 1), (hx + 4, hy - 1), (hx + 3, hy), (hx + 4, hy)], '#f9c22b', 5)
    px(P, [(hx + 4, hy - 1), (hx + 4, hy)], '#9e4539', 5.1)
    px(P, [(hx + 3, hy - 1)], '#ffffff', 5.2)
    px(P, [(hx - 3, hy - 1), (hx - 2, hy - 1), (hx - 3, hy), (hx - 2, hy)], '#e83b3b', 5)
    px(P, [(hx - 3, hy - 1)], '#fca790', 5.2)
    px(P, [(hx + 2, hy - 3), (hx + 3, hy - 3), (hx + 4, hy - 3), (hx + 5, hy - 2)], '#cd683d', 5)      # sobrancelha
    px(P, [(hx - 4, hy - 3), (hx - 3, hy - 3), (hx - 2, hy - 2)], '#2e222f', 5)
    px(P, [(hx + 7, hy + 2)], '#e6904e', 5)                                       # nariz
    px(P, [(hx + 2, hy + 5), (hx + 3, hy + 5), (hx + 4, hy + 5), (hx + 5, hy + 4)], '#9e4539', 5)        # boca
    px(P, [(hx - 2, hy + 4), (hx - 1, hy + 5), (hx, hy + 5)], '#2e222f', 5)
    px(P, [(hx - 4, hy + 1), (hx - 4, hy + 2), (hx - 4, hy + 3)], '#6b3e75', 5.05)   # lágrima de sombra
    # auréola partida (um pedaço falta e o outro está escurecido)
    ay = hy - 16 + [0, 0, -1, -1][t]
    anel = elipse(hx, ay, 10.5, 3.6) - elipse(hx, ay, 8, 2)
    anel_l = {p for p in anel if p[0] >= hx + 2}
    anel_s = {p for p in anel if p[0] <= hx - 3}
    P.append(Parte(anel_l, OURO, z=6))
    P.append(Parte(anel_s, ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#a884f3'], z=6))
    if t % 2 == 0:
        px(P, [(hx + 6, ay - 4), (hx + 6, ay - 6), (hx + 5, ay - 5), (hx + 7, ay - 5)], '#fbff86', 6.1)
    # a foice de luz e sombra (na mão da frente)
    fx = 96
    P.append(Parte({(fx, y) for y in range(14 + dy, 124)} | {(fx + 1, y) for y in range(14 + dy, 124)}, CASCA, z=7, volume='cilindro_h'))
    px(P, [(fx, y) for y in range(20 + dy, 124, 6)], '#f9c22b', 7.05)
    lam_luz = capsula(fx + 1, 16 + dy, fx + 12, 18 + dy, 2.6) | capsula(fx + 12, 18 + dy, fx + 21, 26 + dy, 2.2) | capsula(fx + 21, 26 + dy, fx + 25, 36 + dy, 1.6)
    lam_sombra = capsula(fx + 1, 20 + dy, fx + 11, 22 + dy, 1.6) | capsula(fx + 11, 22 + dy, fx + 18, 28 + dy, 1.3)
    P.append(Parte(lam_luz, ['#f79617', '#f9c22b', '#fbff86', '#ffffff', '#ffffff'], z=7.2))
    P.append(Parte(lam_sombra - lam_luz, ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'], z=7.3))
    P.append(Parte(elipse(fx + 0.5, 15 + dy, 3, 3), OURO_VELHO, z=7.4))
    px(P, [(fx + 0.5, 15 + dy)], '#ffffff', 7.5)
    # braço da frente (manga branca) a segurar a foice
    P.append(Parte(capsula(73, 52 + dy, 84, 66 + dy, 4.4), MARMORE, z=8))
    P.append(Parte(capsula(84, 66 + dy, fx - 2, 62 + dy, 3.4), MARMORE, z=8.1))
    P.append(Parte(elipse(fx + 0.5, 62 + dy, 3.2, 3.4), ['#cd683d', '#e6904e', '#fca790', '#fdcbb0', '#ffffff'], z=8.2))
    px(P, [(x, 62 + dy) for x in range(78, 92)], '#f9c22b', 8.15)               # punho dourado
    # penas negras a cair e brilhos de luz
    for i, (px0, py0) in enumerate(((20, 60), (34, 90), (12, 104), (108, 80))):
        y = py0 + (t * 3 + i * 5) % 12
        cor = '#45293f' if i < 3 else '#ffffff'
        px(P, [(px0 + (t + i) % 2, y), (px0 + 1 + (t + i) % 2, y + 1), (px0 + 2 + (t + i) % 2, y + 1)], cor, 20)
    for i, (gx, gy) in enumerate(((106, 54), (30, 20), (88, 96))):
        if (t + i) % 2 == 0:
            px(P, [(gx, gy), (gx - 1, gy), (gx + 1, gy), (gx, gy - 1), (gx, gy + 1)], '#fbff86', 21)
    return desenhar(P, 128, 128)


# =====================================================================================================
# GRAVAR, VERIFICAR E COMPARAR
# =====================================================================================================

CRIATURAS = [   # (id, pasta antiga)
    ('harpia', 'monstros'), ('elemental_de_ar', 'monstros'), ('nuvem_viva', 'monstros'), ('anjo_guardiao', 'monstros'),
    ('valquiria', 'monstros'), ('valquiria_sigrun', 'monstros'), ('passaro_trovao', 'monstros'),
    ('golem_celeste', 'monstros'), ('serpente_alada', 'monstros'), ('tempestade_viva', 'monstros'),
    ('cavaleiro_de_luz_solida', 'guardioes'), ('jardineira_celeste', 'guardioes'), ('monge_do_vento', 'guardioes'),
    ('senhor_dos_trovoes', 'guardioes'), ('baleia_das_nuvens', 'guardioes'), ('carruagem_do_sol', 'guardioes'),
    ('golem_ilha', 'guardioes'), ('leao_alado_de_marmore', 'guardioes'),
    ('grifo_real', 'bosses'), ('arcanjo_de_bronze', 'bosses'), ('serafim_caido', 'bosses'),
]
FUNDO = (0x26, 0x2b, 0x3a)
FONTE = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def nomes():
    d = {}
    for fn in ('monstros.json', 'bosses.json', 'masmorras.json'):
        caminho = os.path.join(RAIZ, 'dados', fn)
        if not os.path.exists(caminho):
            continue
        pilha = [json.load(open(caminho, encoding='utf-8'))]
        while pilha:   # procura em todo o ficheiro (as masmorras têm os bosses lá dentro)
            e = pilha.pop(0)
            if isinstance(e, dict):
                if 'id' in e and 'nome_pt' in e and isinstance(e['id'], str):
                    d.setdefault(e['id'], e['nome_pt'])
                pilha.extend(e.values())
            elif isinstance(e, list):
                pilha.extend(e)
    return d


def quadros_antigos(cid, pasta):
    im = Image.open(os.path.join(ANTIGA, pasta, f'{cid}_parado_lado.png')).convert('RGBA')
    n = im.height
    return [im.crop((i * n, 0, i * n + n, n)) for i in range(im.width // n)]


def verificar_paleta(img, cid):
    pal = {tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) for c in RESURRECT_64}
    for (r, g, b, a) in getattr(img, 'get_flattened_data', img.getdata)():
        if a and (r, g, b) not in pal:
            raise SystemExit(f'{cid}: cor fora da paleta {(r, g, b)}')
        if a not in (0, 255):
            raise SystemExit(f'{cid}: transparência parcial')


def escala(n):
    return 3 if n <= 32 else (2 if n <= 64 else 1)


def grelha(celulas, titulo, caminho, nfr=8, ms=160, largura_max=1200):
    """celulas: lista de (lista de animações [quadros], nome). Faz um GIF com as células em grelha."""
    fonte = ImageFont.truetype(FONTE, 12)
    margem, gap, txt_h, tit_h = 12, 16, 18, 28
    # medir as células
    medidas = []
    for anims, nome in celulas:
        n = anims[0][0].width
        k = escala(n)
        w = sum(a[0].width * k for a in anims) + 8 * (len(anims) - 1)
        tw = int(fonte.getlength(nome))
        medidas.append((max(w, tw), n * k, k))
    # distribuir por linhas
    pos, x, y, alt_linha = [], margem, margem + tit_h, 0
    for (w, h, k) in medidas:
        if x + w > largura_max - margem and x > margem:
            x, y = margem, y + alt_linha + txt_h + gap
            alt_linha = 0
        pos.append((x, y))
        x += w + gap
        alt_linha = max(alt_linha, h)
    W = largura_max if len(celulas) > 1 else medidas[0][0] + 2 * margem
    H = y + alt_linha + txt_h + margem
    # paleta fixa do GIF: Resurrect 64 + o fundo
    pal = []
    for c in RESURRECT_64:
        pal += [int(c[i:i + 2], 16) for i in (0, 2, 4)]
    pal += list(FUNDO)
    pal += [0, 0, 0] * (256 - len(pal) // 3)
    pimg = Image.new('P', (1, 1))
    pimg.putpalette(pal)
    imgs = []
    for f in range(nfr):
        im = Image.new('RGB', (W, H), FUNDO)
        d = ImageDraw.Draw(im)
        d.fontmode = '1'
        d.text((margem, margem), titulo, fill=(255, 255, 255), font=ImageFont.truetype(FONTE, 14))
        for (anims, nome), (cx, cy), (w, h, k) in zip(celulas, pos, medidas):
            xx = cx
            for a in anims:
                q = a[f % len(a)]
                q = q.resize((q.width * k, q.height * k), Image.NEAREST)
                im.paste(q, (xx, cy + (h - q.height)), q)
                xx += q.width + 8
            d.text((cx, cy + h + 3), nome, fill=(199, 220, 208), font=fonte)
        imgs.append(im.quantize(palette=pimg, dither=Image.Dither.NONE))
    imgs[0].save(caminho, save_all=True, append_images=imgs[1:], duration=ms, loop=0, disposal=1)


def main(so=None):
    os.makedirs(PASTA, exist_ok=True)
    nm = nomes()
    antes_depois, depois = [], []
    for cid, pasta in CRIATURAS:
        if so and cid not in so:
            continue
        antigos = quadros_antigos(cid, pasta)
        n = antigos[0].width
        novos = [globals()[cid](t) for t in range(4)]
        assert novos[0].size == (n, n), (cid, novos[0].size, n)
        tira = Image.new('RGBA', (n * 4, n), (0, 0, 0, 0))
        for i, q in enumerate(novos):
            verificar_paleta(q, cid)
            tira.paste(q, (i * n, 0))
        tira.save(os.path.join(PASTA, f'{cid}_parado_lado.png'))
        nome = nm.get(cid, cid)
        antes_depois.append(([antigos, novos], nome))
        depois.append(([novos], nome))
        print(f'{cid}: {n}x{n} x4 -> ok')
    if not so:
        grelha(antes_depois, 'Região 9 — Céu — antes | depois', os.path.join(PASTA, 'comparar.gif'))
        grelha(depois, 'Região 9 — Céu — proposta nova', os.path.join(PASTA, 'depois.gif'))
        print('GIFs gravados em', PASTA)


if __name__ == '__main__':
    main(sys.argv[1:] or None)
