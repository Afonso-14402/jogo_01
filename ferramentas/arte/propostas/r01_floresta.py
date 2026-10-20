"""PROPOSTA (ainda não está no jogo): os monstros, guardiões e bosses da Região 1 (Floresta) redesenhados,
no estilo do Ent Ancião novo (ferramentas/arte/ent_anciao.py): formas orgânicas feitas de várias partes,
textura (pelo, escamas, veios, pintas), olhos com brilho e pormenores próprios de cada criatura.

Só desenha a animação "parado" (4 quadros) de cada um, com o MESMO tamanho de quadro do desenho atual.
NÃO mexe na arte do jogo: grava tudo em arte/propostas/monstros/r01_floresta/ (e o Ent Ancião, já aprovado,
é só copiado). Se o utilizador aprovar, o próximo passo é passar estes desenhos para os scripts do jogo
(monstros_r01.py e guardioes_r01.py) e fazer as outras animações com o mesmo corpo.

Uso (a partir da raiz do repositório):
    python3 ferramentas/arte/propostas/r01_floresta.py            -> PNG + comparar.gif + depois.gif
    python3 ferramentas/arte/propostas/r01_floresta.py rever DIR  -> também imagens antes|depois ampliadas em DIR
"""
import math
import os
import random
import shutil
import sys

from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402

ORIGEM = os.path.join(RAIZ, 'arte', 'regioes', 'r01_floresta')
DESTINO = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r01_floresta')

OUT = '#2e222f'
BR = '#ffffff'

# A paleta Resurrect 64 inteira (para verificar que nenhum desenho sai dela).
RESURRECT64 = {'#' + c.lower() for c in """
2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334 e83b3b
fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73
91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6
8fd3ff 45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0
""".split()}

# ---------------- rampas próprias (só cores da Resurrect 64, escuro -> claro)
GEL = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
FOLHA = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
FOLHA_ESC = ['#165a4c', '#165a4c', '#239063', '#1ebc73', '#91db69']
MUSGO = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']
MUSGO_VIVO = ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#fbff86']
CASCA = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
CASCA_ESC = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
OUTONO = ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#fbb954']
OURO = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
MARFIM = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']
PELO_COELHO = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
PELO_COELHO_ESC = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
CREME = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']
CAULE = ['#625565', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
CINZA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
CINZA_ESC = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
NEGRO = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
JAVALI = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
JAVALI_ESC = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
FOCINHO = ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0']
VERMELHO = ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790']
LARANJA = ['#9e4539', '#cd683d', '#fb6b1d', '#f79617', '#fbb954']
AZUL = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
AZUL_ESC = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
AGUA = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
ROXO = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']
ROXO_ESC = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3']
ROSA = ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0']
LILAS = ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0']
ASA = ['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2', '#ffffff']
ASA_ABELHA = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
PEDRA = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
PEDRA_CLARA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
TERRA = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
BRANCO_ESC = ['#484a77', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']
BRANCO = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
FERRO = ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
COBRE = ['#6e2727', '#9e4539', '#cd683d', '#f57d4a', '#fca790']
ACIDO = ['#165a4c', '#239063', '#91db69', '#cddf6c', '#fbff86']


# =====================================================================================
# utilidades de desenho
# =====================================================================================

def px(P, pts, cor, z):
    """Píxeis de uma cor só (olhos, marcas, textura), sem contorno."""
    s = {(int(math.floor(x)), int(math.floor(y))) for x, y in pts}
    if s:
        P.append(Parte(s, None, z=z, separar=False, cor=cor))


def _h(x, y, s=0):
    v = (x * 73856093) ^ (y * 19349663) ^ (s * 83492791)
    v = (v ^ (v >> 13)) * 1274126177
    return (v ^ (v >> 16)) & 0xffff


def _caixa(m):
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    return min(xs), min(ys), max(xs), max(ys)


def pelo(P, m, rampa, z, sem=0, dens=7, claro=True, escuro=True, ancora=None, passo=(-1, 1)):
    """Textura de pelo: risquinhos escuros (sombra entre os pelos) do lado da sombra e risquinhos claros do lado
    da luz (cima-esquerda). Os riscos seguem o sentido do pelo (passo)."""
    if not m:
        return
    x1, y1, x2, y2 = _caixa(m)
    ax, ay = ancora if ancora else (x1, y1)
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    rx, ry = max(1, (x2 - x1) / 2), max(1, (y2 - y1) / 2)
    esc, cla = [], []
    for (x, y) in m:
        h = _h(x - ax, y - ay, sem) % dens
        lado = (x - cx) / rx + (y - cy) / ry
        if escuro and h == 0 and lado > -0.3:
            esc += [(x, y), (x + passo[0], y + passo[1])]
        elif claro and h == 1 and lado < -0.5:
            cla += [(x, y)]
    px(P, [p for p in esc if p in m], rampa[1] if rampa[1] != rampa[0] else rampa[0], z + 0.001)
    px(P, [p for p in cla if p in m], rampa[3], z + 0.002)


def pintas(P, m, cor, z, sem=0, dens=9, ancora=None, so=None):
    """Pintas de uma cor espalhadas dentro de m (so: função (x,y)->bool para escolher a zona)."""
    if not m:
        return
    x1, y1, _, _ = _caixa(m)
    ax, ay = ancora if ancora else (x1, y1)
    pts = [(x, y) for (x, y) in m if _h(x - ax, y - ay, sem) % dens == 0 and (so is None or so(x, y))]
    px(P, pts, cor, z)


def borda_pelo(m, sem=0, lado='cima', prob=0.45):
    """Recorta a borda (tufos de pelo/folhas a sair) no lado pedido."""
    rnd = random.Random(sem)
    m = set(m)
    x1, y1, x2, y2 = _caixa(m)
    cy = (y1 + y2) / 2
    novos = set()
    for (x, y) in sorted(m):
        if lado == 'cima' and (x, y - 1) not in m and y < cy:
            if rnd.random() < prob:
                novos.add((x, y - 1))
        if lado == 'baixo' and (x, y + 1) not in m and y > cy:
            if rnd.random() < prob:
                novos.add((x, y + 1))
    return m | novos


def olho(P, x, y, iris, z=40, tam=2, fechado=False, brilho=BR, olhar=1):
    """Olho com brilho, a olhar para a direita.
    tam 2: 2×2 (brilho + íris à esquerda, pupila à direita); tam 3: 3×3; tam 4: 4×4."""
    x, y = int(x), int(y)
    if fechado:
        px(P, [(x + i, y + tam // 2) for i in range(tam)], OUT, z)
        return
    if tam == 1:
        px(P, [(x, y)], iris, z)
        return
    if tam == 2:
        px(P, [(x + 1, y), (x + 1, y + 1)], OUT, z)
        px(P, [(x, y + 1)], iris, z)
        px(P, [(x, y)], brilho, z + 0.01)
        return
    if tam == 3:
        px(P, [(x + i, y + j) for i in range(3) for j in range(3)], iris, z)
        px(P, [(x + 2, y + 1), (x + 1, y + 1), (x + 2, y + 2)], OUT, z + 0.01)
        px(P, [(x, y)], brilho, z + 0.02)
        return
    # tam 4
    px(P, [(x + i, y + j) for i in range(4) for j in range(4) if (i, j) not in ((0, 0), (3, 0), (0, 3), (3, 3))], iris, z)
    px(P, [(x + 2, y + 1), (x + 2, y + 2), (x + 1, y + 2), (x + 3, y + 1), (x + 3, y + 2)], OUT, z + 0.01)
    px(P, [(x + 1, y), (x, y + 1)], brilho, z + 0.02)


def elipse_rot(x1, y1, x2, y2, r):
    """Elipse esticada de (x1,y1) a (x2,y2) (o comprimento) com meia-largura r: asas, folhas, penas."""
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    L = max(1.0, math.hypot(x2 - x1, y2 - y1) / 2)
    ux, uy = (x2 - x1) / (2 * L), (y2 - y1) / (2 * L)
    m = set()
    for y in range(int(min(y1, y2) - L - r) - 1, int(max(y1, y2) + L + r) + 2):
        for x in range(int(min(x1, x2) - L - r) - 1, int(max(x1, x2) + L + r) + 2):
            dx, dy = x + .5 - cx, y + .5 - cy
            a = dx * ux + dy * uy
            b = -dx * uy + dy * ux
            if (a / L) ** 2 + (b / r) ** 2 <= 1.0:
                m.add((x, y))
    return m


def brilhinho(P, x, y, cor, z, grande=False):
    """Uma estrelinha (cruz) para brilhos e faíscas."""
    x, y = int(x), int(y)
    px(P, [(x, y)], BR if grande else cor, z + 0.01)
    if grande:
        px(P, [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], cor, z)


def tufo(cx, cy, r, sem, ry=None):
    """Tufo de folhas/musgo: círculo com a borda recortada (folhinhas a sair) — como no Ent Ancião."""
    rnd = random.Random(sem)
    m = elipse(cx, cy, r, ry if ry else r * 0.86)
    borda = [p for p in m if any((p[0] + dx, p[1] + dy) not in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
    for (x, y) in sorted(borda):
        k = rnd.random()
        if k < 0.25:
            m.discard((x, y))
        elif k < 0.45:
            dx, dy = (x - cx), (y - cy)
            n = math.hypot(dx, dy) or 1
            m.add((int(x + dx / n * 1.5), int(y + dy / n * 1.5)))
    return m


def folhagem(P, m, rampa, z, sem, dens=13):
    """Textura de folhas dentro de um tufo: pintas escuras (sombra entre folhas) e folhinhas claras em cima."""
    if not m:
        return
    x1, y1, x2, y2 = _caixa(m)
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    esc, cla = [], []
    for (x, y) in m:
        h = _h(x - x1, y - y1, sem) % dens
        lado = (x - cx) + (y - cy)
        if h == 0 or (h == 5 and lado > 1):
            esc.append((x, y))
        elif h == 9 and lado < -2:
            cla += [(x, y), (x + 1, y)]
    px(P, esc, rampa[0], z + 0.001)
    px(P, [p for p in cla if p in m], rampa[4], z + 0.002)


def cogumelinho(P, x, y, z, cor=VERMELHO, esq=False):
    """Um cogumelo vermelho pequenino de pintas brancas (pé em (x, y))."""
    P.append(Parte(capsula(x, y - 2, x, y, 0.8), ['#c7dcd0'] * 5, z=z))
    chap = {p for p in elipse(x + 0.5, y - 2.5, 2.4, 1.8) if p[1] <= y - 2}
    P.append(Parte(chap, cor, z=z + 0.01))
    px(P, [(x - 1, y - 3)], BR, z + 0.02)


def gota(P, x, y, rampa, z, comp=2):
    """Uma gota (mel, baba, água) a pingar: um fio e uma bolinha."""
    P.append(Parte(capsula(x, y, x, y + comp, 0.7) | elipse(x + 0.5, y + comp + 0.8, 1.2, 1.3), rampa, z=z))


# =====================================================================================
# 1. Slime Verde (32)
# =====================================================================================

def slime_verde(t):
    P = []
    rx, ry = [(10.0, 8.6), (10.4, 8.3), (10.9, 7.9), (10.4, 8.3)][t]
    cx, base = 16, 30
    corpo, cy = _gel(cx, base, rx, ry)
    P.append(Parte(corpo, GEL, z=1))
    x1, y1, x2, y2 = _caixa(corpo)
    # luz que atravessa o gel e sai em baixo
    px(P, [(x, base - 1) for x in range(cx - 3, cx + 4)], '#1ebc73', 1.1)
    # bolhas a subir (mexem de quadro para quadro)
    for (bx, by, f) in ((cx - 4, base - 2, 0), (cx + 1, base - 3, 2)):
        yy = by - ((t + f) % 4)
        if (bx, yy) in corpo and (bx, yy - 1) in corpo:
            px(P, [(bx, yy)], '#91db69', 1.2)
    # brilho forte do gel (em cima à esquerda)
    px(P, [(x1 + 3, y1 + 4), (x1 + 3, y1 + 3), (x1 + 4, y1 + 2), (x1 + 5, y1 + 2)], BR, 2)
    px(P, [(x1 + 2, y1 + 5), (x1 + 6, y1 + 1)], '#cddf6c', 2)
    # rebento de duas folhas no cocuruto (abanam)
    tx, ty = cx - 1, y1
    P.append(Parte(capsula(tx, ty, tx, ty - 2, 0.6), ['#4c3e24', '#676633', '#676633', '#a2a947', '#a2a947'], z=0.5))
    f = [0, 1, 1, 0][t]
    P.append(Parte(capsula(tx, ty - 2, tx - 3, ty - 3 - f, 1.0), MUSGO_VIVO, z=0.6))
    P.append(Parte(capsula(tx + 1, ty - 2, tx + 3, ty - 4 + f, 1.0), MUSGO_VIVO, z=0.7))
    # cara (virada para a direita)
    ey = int(cy) - 1
    pisca = t == 2
    olho(P, cx + 2, ey, '#165a4c', z=3, fechado=pisca)
    olho(P, cx + 6, ey, '#165a4c', z=3, fechado=pisca)
    px(P, [(cx + 4, ey + 3), (cx + 5, ey + 3)], OUT, 3)
    px(P, [(cx + 8, ey + 2), (cx + 1, ey + 2)], '#f68181', 3)
    return desenhar(P, 32, 32)


# =====================================================================================
# 2. Slime Rei (64): coroa de ouro e um peixe lá dentro
# =====================================================================================

def slime_rei(t):
    P = []
    rx, ry = [(21.5, 19.0), (22.0, 18.5), (22.6, 17.8), (22.0, 18.5)][t]
    cx, base = 32, 62
    corpo, cy = _gel(cx, base, rx, ry, k=2)
    corpo |= capsula(cx + rx * 0.7, base - 3, cx + rx * 0.72, base, 1.5)
    P.append(Parte(corpo, GEL, z=1))
    x1, y1, x2, y2 = _caixa(corpo)
    # luz que atravessa o gel (em baixo)
    px(P, [(x, base - 1) for x in range(cx - 9, cx + 10)] + [(x, base - 2) for x in range(cx - 5, cx + 6)], '#1ebc73', 1.05)
    # o peixe lá dentro (nada para a frente e para trás)
    fx, fy = cx - 8 + [0, 1, 2, 1][t], int(cy) + 6
    cauda = [0, 1, 0, -1][t]
    peixe = elipse(fx, fy, 6.0, 3.6) | poligono([(fx - 5, fy), (fx - 10, fy - 4 - cauda), (fx - 9, fy), (fx - 10, fy + 4 - cauda)])
    P.append(Parte(peixe, LARANJA, z=1.3, separar=False))
    px(P, [p for p in peixe if any((p[0] + a, p[1] + b) not in peixe for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))], '#165a4c', 1.35)
    px(P, [(fx + 3, fy - 1), (fx + 3, fy)], OUT, 1.4)
    px(P, [(fx + 2, fy - 1)], BR, 1.41)
    px(P, [(fx, fy - 2), (fx - 1, fy - 1), (fx - 1, fy), (fx, fy + 1)], '#cd683d', 1.4)          # guelra
    px(P, [(fx - 3, fy - 4), (fx - 2, fy - 4), (fx - 1, fy - 5), (fx, fy - 5)], '#fbb954', 1.4)    # barbatana
    px(P, [(fx + 5, fy + 1)], OUT, 1.4)                                                            # boca do peixe
    # moedas e um osso de quem tentou roubar a coroa (no fundo do gel)
    for (mx, my) in ((cx + 9, base - 5), (cx + 12, base - 4), (cx + 10, base - 3)):
        P.append(Parte(elipse(mx, my, 1.8, 1.4), OURO, z=1.3))
    osso = capsula(cx - 2, base - 5, cx + 4, base - 6, 0.8) | elipse(cx - 2, base - 5, 1.4, 1.4) | elipse(cx + 4, base - 6, 1.4, 1.4)
    P.append(Parte(osso, BRANCO, z=1.25))
    # bolhas a subir
    for (bx, by, f) in ((cx - 15, base - 8, 0), (cx + 15, base - 12, 1), (cx - 4, base - 10, 2), (cx + 3, int(cy) - 1, 3)):
        yy = by - ((t + f) % 4) * 2
        anel = [(bx - 1, yy), (bx + 1, yy), (bx, yy - 1), (bx, yy + 1)]
        if all(p in corpo for p in anel):
            px(P, anel, '#91db69', 1.5)
            px(P, [(bx - 1, yy - 1)], BR, 1.5)
    # brilho grande do gel: um arco branco junto à borda de cima-esquerda
    arco = [(cx + rx * 0.74 * math.cos(math.radians(a)), cy + ry * 0.74 * math.sin(math.radians(a))) for a in range(196, 246, 4)]
    px(P, arco, BR, 2)
    px(P, [(x + 1, y + 1) for (x, y) in arco[2:-2]], '#cddf6c', 1.9)
    px(P, [(cx + rx * 0.74 * math.cos(math.radians(a)), cy + ry * 0.74 * math.sin(math.radians(a))) for a in (180, 184)], BR, 2)
    # cara: olhos grandes, sobrancelhas de quem manda, sorriso convencido
    ey = int(cy) - 6
    pisca = t == 2
    for ex in (cx + 3, cx + 12):
        if pisca:
            px(P, [(ex, ey + 2), (ex + 1, ey + 3), (ex + 2, ey + 3), (ex + 3, ey + 2)], OUT, 3)
        else:
            olho(P, ex, ey, '#165a4c', z=3, tam=4)
        px(P, [(ex - 1, ey - 3), (ex, ey - 3), (ex + 1, ey - 2), (ex + 2, ey - 2), (ex + 3, ey - 2)], '#165a4c', 3)
    my = ey + 8
    px(P, [(cx + 5, my), (cx + 6, my + 1), (cx + 7, my + 1), (cx + 8, my + 1), (cx + 9, my + 1), (cx + 10, my + 1), (cx + 11, my), (cx + 12, my - 1)], OUT, 3)
    px(P, [(cx + 8, my + 2), (cx + 9, my + 2)], '#e83b3b', 3)
    px(P, [(cx + 16, my - 2), (cx + 17, my - 2), (cx + 1, my - 2)], '#f68181', 3)
    # coroa de ouro (assenta no cocuruto e abana com o gel)
    top = int(y1) + 1
    k = [0, 0, 1, 0][t]
    c = cx + 3
    coroa = poligono([(c - 9, top + 2 + k), (c - 10, top - 6 + k), (c - 6, top - 2 + k), (c - 2.5, top - 8 + k), (c + 1, top - 2 + k),
                      (c + 4.5, top - 8 + k), (c + 7, top - 2 + k), (c + 10, top - 5 + k), (c + 9.5, top + 2 + k)])
    P.append(Parte(coroa, OURO, z=5, volume='cilindro_v'))
    P.append(Parte(retangulo(int(c - 9), top + k, int(c + 9), top + 2 + k), ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86'], z=5.1, volume='cilindro_v'))
    for (gx2, cor) in ((-6, '#e83b3b'), (0, '#4d9be6'), (5, '#e83b3b')):
        px(P, [(c + gx2, top + 1 + k), (c + gx2 + 1, top + 1 + k)], cor, 5.2)
        px(P, [(c + gx2, top + k)], BR, 5.3)
    for (gx2, gy2) in ((-10, -6), (-2.5, -8), (4.5, -8), (10, -5)):
        P.append(Parte(elipse(c + gx2 + 0.5, top + gy2 + k, 1.3, 1.3), ['#831c5d', '#c32454', '#e83b3b', '#f68181', BR], z=5.4))
    if t == 1:
        brilhinho(P, c - 6, top - 4, '#fbff86', 6, grande=True)
    if t == 3:
        brilhinho(P, c + 9, top - 3, '#fbff86', 6, grande=True)
    return desenhar(P, 64, 64)


# =====================================================================================
# 3. Coelho-Chifre (32)
# =====================================================================================

def coelho_chifre(t):
    P = []
    dy = [0, 0, 1, 0][t]
    orelha = [0, -1, 0, 1][t]
    hx, hy = 21, 17 + dy
    # orelha de trás (mais escura)
    P.append(Parte(capsula(hx - 2, hy - 2, hx - 5 + orelha, hy - 11, 1.3), PELO_COELHO_ESC, z=1))
    # pata de trás (a do lado de lá)
    P.append(Parte(capsula(9, 29.5, 15, 29.5, 1.3), PELO_COELHO_ESC, z=1.2))
    P.append(Parte(capsula(19.5, 26, 20.5, 29.5, 1.1), PELO_COELHO_ESC, z=1.2))
    # cauda de algodão
    P.append(Parte(borda_pelo(elipse(6.5, 22 + dy, 2.4, 2.3), 3, 'cima', 0.6), BRANCO, z=1.5))
    # corpo: anca grande + peito
    corpo = elipse(12.5, 24 + dy, 6.3, 5.2) | elipse(17.5, 23.5 + dy, 4.2, 4.6)
    corpo = borda_pelo(corpo, 5, 'cima', 0.3)
    P.append(Parte(corpo, PELO_COELHO, z=2))
    pelo(P, corpo, PELO_COELHO, 2, sem=1, dens=8, claro=False, passo=(-1, 0))
    # barriga clara
    barriga = {p for p in elipse(17, 27 + dy, 3.6, 2.2) if p in corpo}
    px(P, barriga, '#ab947a', 2.2)
    # coxa (pata de trás grande) e o pé comprido
    P.append(Parte(elipse(11, 25.5 + dy, 3.8, 3.4), PELO_COELHO, z=2.5))
    P.append(Parte(capsula(9, 29.5, 15.5, 29.5, 1.4), PELO_COELHO, z=2.6))
    # pata da frente
    P.append(Parte(capsula(18, 26 + dy, 18.5, 29.5, 1.2), PELO_COELHO, z=2.8))
    # cabeça (com focinho)
    cab = elipse(hx, hy, 4.3, 3.8) | elipse(hx + 2.8, hy + 1.2, 2.8, 2.4)
    P.append(Parte(cab, PELO_COELHO, z=4))
    px(P, [(hx + 2, hy + 3), (hx + 3, hy + 3)], '#c7dcd0', 4.1)        # bochecha clara
    # orelha da frente com o interior cor-de-rosa
    ox = hx - 1 + orelha
    P.append(Parte(capsula(hx - 1, hy - 3, ox - 1, hy - 12, 1.6), PELO_COELHO, z=5))
    for i in range(2, 8):
        px(P, [(round(hx - 1 + (ox - hx) * i / 9.0), hy - 3 - i)], '#cf657f', 5.1)
    # chifre de marfim a sair da testa (com anéis)
    chifre = poligono([(hx + 0.5, hy - 2), (hx + 3.5, hy - 3.5), (hx + 6, hy - 11)])
    P.append(Parte(chifre, MARFIM, z=6))
    px(P, [(hx + 3, hy - 5), (hx + 4, hy - 8)], '#966c6c', 6.1)
    # cara
    olho(P, hx + 1, hy - 1, '#9e4539', z=8, fechado=(t == 3))
    px(P, [(hx + 5, hy + 1)], '#f04f78', 8)                       # nariz
    if t == 1:
        px(P, [(hx + 5, hy)], '#f68181', 8)                       # o nariz a mexer
    px(P, [(hx + 4, hy + 3)], OUT, 8)                             # boca
    px(P, [(hx + 6, hy + 2), (hx + 7, hy + 2)], '#c7dcd0', 8)      # bigodes
    return desenhar(P, 32, 32)


# =====================================================================================
# 4. Lobo Cinzento (32) e Lobo Cicatriz (48)
# =====================================================================================

def _lobo(t, k, W, rampa, rampa_esc, ventre, olho_cor, cicatriz=False):
    """Lobo de lado (virado para a direita). Coordenadas pensadas para 32 px; k = escala (1,5 para 48 px)."""
    P = []
    base = W - 2

    def X(v):
        return v * k

    def Y(v, mexe=0):
        return base - (30 - v) * k + mexe

    def R(v):
        return v * k

    dy = [0, 0, 1, 0][t]          # respirar (o peito sobe e desce)
    cauda = [0, 1, 2, 1][t]       # a cauda abana
    orelha = [0, 0, 0, 1][t]      # a orelha mexe
    # ---- patas do lado de lá (mais escuras)
    P.append(Parte(capsula(X(11), Y(22), X(9.5), Y(26.5), R(1.3)) | capsula(X(9.5), Y(26.5), X(10.5), Y(30), R(1.1)), rampa_esc, z=0))
    P.append(Parte(capsula(X(17.5), Y(22), X(17), Y(30), R(1.2)), rampa_esc, z=0))
    # ---- cauda farfalhuda
    c1, c2, c3 = (X(7), Y(16, dy)), (X(3.5), Y(18) + cauda), (X(2.5), Y(22.5) + cauda)
    caudam = borda_pelo(capsula(*c1, *c2, R(2.1)) | capsula(*c2, *c3, R(1.9)), 9, 'cima', 0.5)
    P.append(Parte(caudam, rampa, z=0.5))
    P.append(Parte({p for p in elipse(c3[0], c3[1] + R(0.6), R(1.7), R(1.7)) if p in caudam or p[1] > c3[1]}, ventre, z=0.6, separar=False))
    # ---- tronco: dorso + peito fundo
    corpo = capsula(X(7.5), Y(18, dy), X(18), Y(17.5, dy), R(4.0)) | elipse(X(18.5), Y(19, dy), R(4.2), R(4.6))
    corpo = borda_pelo(corpo, 11, 'cima', 0.5)
    P.append(Parte(corpo, rampa, z=2, volume='cilindro_h'))
    pelo(P, corpo, rampa, 2, sem=2, dens=9 if k < 1.4 else 7, claro=False, passo=(-1, 0))
    # sela mais escura no dorso
    sela = [(x, y) for (x, y) in corpo if y <= Y(15, dy) + (1 if (x // 2) % 2 else 0) and X(8) < x < X(17)]
    px(P, sela, rampa_esc[2], 2.05)
    # ---- pescoço com a crina clara do peito
    P.append(Parte(capsula(X(18.5), Y(16.5, dy), X(22), Y(13.5, dy), R(3.0)), rampa, z=2.4))
    juba = borda_pelo({p for p in elipse(X(21.2), Y(18, dy), R(1.9), R(3.0))}, 4, 'baixo', 0.8)
    P.append(Parte(juba, ventre, z=2.45, separar=False))
    pelo(P, juba, ventre, 2.45, sem=3, dens=5, claro=False, passo=(0, 1))
    # ---- patas do lado de cá: coxa + perna com jarrete; perna da frente
    P.append(Parte(elipse(X(10), Y(20.5, dy), R(3.3), R(3.8)), rampa, z=2.6))
    P.append(Parte(capsula(X(9.5), Y(23), X(8), Y(26.5), R(1.4)) | capsula(X(8), Y(26.5), X(9), Y(30), R(1.2)), rampa, z=2.7))
    P.append(Parte(capsula(X(19.5), Y(22, dy), X(20), Y(30), R(1.35)), rampa, z=2.7))
    for pxx in (X(9), X(20)):
        px(P, [(pxx + 1, Y(30)), (pxx + 2, Y(30))], rampa[3], 2.8)           # dedos
    # ---- cabeça: crânio + focinho comprido + queixo
    hx, hy = X(24), Y(12, dy)
    P.append(Parte(poligono([(hx - R(2.8), hy - R(1)), (hx - R(2) - orelha * k, hy - R(6.5)), (hx - R(0.2), hy - R(2))]), rampa_esc, z=3.9))
    cab = elipse(hx, hy, R(3.6), R(3.1)) | capsula(hx + R(1), hy + R(0.8), hx + R(5.8), hy + R(1.6), R(1.7))
    cab = borda_pelo(cab | elipse(hx - R(0.8), hy + R(2), R(2.6), R(2.4)), 13, 'baixo', 0.6)
    P.append(Parte(cab, rampa, z=4))
    px(P, [(x, y) for (x, y) in cab if y >= hy + R(1.9) and x >= hx + R(0.5)], ventre[2], 4.1)     # focinho/queixo claro
    ore = poligono([(hx - R(1), hy - R(1.8)), (hx + R(0.2) - orelha * k, hy - R(7)), (hx + R(2), hy - R(2.2))])
    P.append(Parte(ore, rampa, z=4.5))
    px(P, [(hx + R(0.1) - orelha * k * 0.5, hy - R(4.2)), (hx + R(0.2) - orelha * k * 0.5, hy - R(3.2))], rampa_esc[1], 4.6)
    # ---- olho, nariz, boca, dente
    ex, ey = hx + R(1.3), hy - R(1.0)
    olho(P, ex, ey, olho_cor, z=8, tam=2 if k < 1.4 else 3, fechado=(t == 2))
    nx = hx + R(6.4)
    px(P, [(nx, hy + R(0.3)), (nx, hy + R(0.3) + 1)] if k > 1.4 else [(nx, hy + R(0.6))], OUT, 8)
    my = hy + R(2.4)
    px(P, [(x, my) for x in range(int(hx + R(2)), int(nx))], OUT, 8)
    px(P, [(nx - R(1.5), my + 1)], BR, 8.1)
    if cicatriz:
        # cicatriz branca de cima a baixo pelo olho, orelha rasgada, marcas no flanco e pelo eriçado vermelho
        px(P, [(ex, ey - 4), (ex + 1, ey - 3), (ex + 1, ey - 2), (ex + 2, ey + 3), (ex + 2, ey + 4), (ex + 3, ey + 5)], '#c7dcd0', 9)
        px(P, [(ex - 1, ey - 5), (ex + 3, ey + 6)], '#9babb2', 9)
        for (sx, sy) in ((X(12), Y(16.5, dy)), (X(14.2), Y(16, dy)), (X(16.4), Y(16.5, dy))):
            px(P, [(sx, sy), (sx + 1, sy + 1), (sx + 1, sy + 2), (sx + 2, sy + 3)], '#7f708a', 2.3)
        px(P, [(hx + R(0.3) - orelha * k, hy - R(5.6)), (hx + R(0.8) - orelha * k, hy - R(5.0))], OUT, 4.7)
        for i, x in enumerate(range(int(X(9)), int(X(18)), 3)):
            px(P, [(x, Y(14, dy) - 1 - (i % 2)), (x + 1, Y(14, dy) - 2 + (i % 2))], '#6e2727', 2.06)
    return P


def lobo_cinzento(t):
    P = _lobo(t, 1.0, 32, CINZA, CINZA_ESC, ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0'], '#f9c22b')
    return desenhar(P, 32, 32)


def lobo_cicatriz(t):
    P = _lobo(t, 1.5, 48, NEGRO, ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565'],
              ['#3e3546', '#45293f', '#625565', '#7f708a', '#9babb2'], '#e83b3b', cicatriz=True)
    return desenhar(P, 48, 48)


def _gel(cx, base, rx, ry, pinga=True, k=1.0):
    """Corpo de slime: uma elipse cortada em baixo (assenta no chão), com um pingo a escorrer atrás."""
    cy = base + 0.5 - ry * 0.8
    corpo = {p for p in elipse(cx, cy, rx, ry) if p[1] <= base}
    if pinga:
        corpo |= capsula(cx - rx * 0.78, base - 2 * k, cx - rx * 0.85 - k, base, 1.0 * k)
    return corpo, cy


# =====================================================================================
# 5. Javali (48) e Javali-Rei (64)
def _javali(t, k, W, ox=0, rei=False):
    """Javali de lado, virado para a direita (coordenadas pensadas para 48 px; k = escala)."""
    P = []
    base = W - 2

    def X(v):
        return ox + v * k

    def Y(v, m=0):
        return base - (46 - v) * k + m

    def R(v):
        return v * k

    dy = [0, 0, 1, 0][t]
    orelha = [0, 0, 0, 1][t]
    cauda = [0, 1, 0, -1][t]
    pelo_r = JAVALI if not rei else ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
    pelo_e = JAVALI_ESC
    # ---- patas do lado de lá
    P.append(Parte(capsula(X(16), Y(38), X(15.5), Y(44.5), R(2.0)), pelo_e, z=0))
    P.append(Parte(capsula(X(33), Y(39), X(33.5), Y(44.5), R(1.9)), pelo_e, z=0))
    for hx in (X(15.5), X(33.5)):
        P.append(Parte(elipse(hx + R(0.5), Y(45.3), R(2.0), R(1.0)), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#625565'], z=0.1))
    # ---- cauda fininha com tufo
    P.append(Parte(capsula(X(7), Y(29, dy), X(4.5 + cauda * 0.5), Y(34, dy), R(0.8)), pelo_r, z=0.5))
    P.append(Parte(elipse(X(4.3 + cauda * 0.5), Y(35, dy), R(1.3), R(1.6)), pelo_e, z=0.6))
    # ---- corpo: barril + bossa dos ombros
    corpo = elipse(X(19), Y(33, dy), R(12.5), R(8.6)) | elipse(X(27), Y(30, dy), R(8.5), R(9.5))
    P.append(Parte(corpo, pelo_r, z=2))
    pelo(P, corpo, pelo_r, 2, sem=4, dens=7, passo=(-1, 1))
    # crina eriçada ao longo do dorso
    crina = set()
    for i in range(14):
        x = X(10 + i * 2)
        topo = min([y for (xx, y) in corpo if xx == int(x)] or [Y(25, dy)])
        alt = R(2.5 + (i % 3) * 1.2 + (2 if 5 < i < 11 else 0))
        crina |= poligono([(x - R(1.6), topo + R(2)), (x - R(0.6), topo - alt), (x + R(1.4), topo + R(2))])
    P.append(Parte(crina, ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c'], z=2.2))
    # barriga um pouco mais clara
    # ---- patas do lado de cá: presunto + pata curta, pata da frente
    P.append(Parte(elipse(X(13), Y(35, dy), R(5.2), R(5.5)), pelo_r, z=2.5))
    P.append(Parte(capsula(X(13), Y(39), X(12.5), Y(44.5), R(2.2)), pelo_r, z=2.6))
    P.append(Parte(capsula(X(30), Y(37, dy), X(31), Y(44.5), R(2.1)), pelo_r, z=2.6))
    for hx in (X(12.5), X(31)):
        P.append(Parte(elipse(hx + R(0.6), Y(45.3), R(2.2), R(1.0)), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#7f708a'], z=2.7))
        px(P, [(hx + R(0.6), Y(45))], '#2e222f', 2.8)                              # o casco fendido
    # lama nas patas
    for (lx, ly) in ((X(12), Y(43)), (X(14), Y(42)), (X(30), Y(43)), (X(32), Y(42.5))):
        px(P, [(lx, ly), (lx + 1, ly)], '#4c3e24', 2.9)
    # ---- cabeça: cara comprida e baixa, focinho, presa, orelha
    hx, hy = X(37), Y(34, dy)
    cab = elipse(hx, hy, R(6.2), R(5.6)) | capsula(hx + R(2), hy + R(1.5), hx + R(8.5), hy + R(3), R(3.0))
    P.append(Parte(cab, pelo_r, z=4))
    pelo(P, cab, pelo_r, 4, sem=8, dens=7, claro=False, passo=(-1, 0))
    P.append(Parte(elipse(hx + R(9.3), hy + R(3), R(1.5), R(2.6)), FOCINHO, z=4.5))         # o disco do focinho
    px(P, [(hx + R(9.6), hy + R(2.2)), (hx + R(9.6), hy + R(3.6))], '#753c54', 4.6)        # narinas
    # presa de marfim curva para cima
    presa = capsula(hx + R(5.5), hy + R(5), hx + R(7.5), hy + R(3.6), R(1.0)) | capsula(hx + R(7.5), hy + R(3.6), hx + R(8), hy + R(0.5), R(0.8))
    P.append(Parte(presa, MARFIM, z=5))
    if rei:
        px(P, [(hx + R(7.6), hy + R(2.2)), (hx + R(7.2), hy + R(2.9))], '#966c6c', 5.1)    # presa rachada
    # orelha
    ore = poligono([(hx - R(3.5), hy - R(3)), (hx - R(5.5) - orelha * k, hy - R(9)), (hx - R(0.5), hy - R(4.5))])
    P.append(Parte(ore, pelo_r, z=4.6))
    px(P, [(hx - R(4) - orelha * k * 0.5, hy - R(6)), (hx - R(3.5), hy - R(5))], FOCINHO[1], 4.7)
    # olho
    olho(P, hx + R(1.5), hy - R(1.8), '#91db69' if rei else '#9e4539', z=8, tam=2 if k < 1.2 else 3, fechado=(t == 2))
    px(P, [(hx + R(0.5), hy - R(3)), (hx + R(1.5), hy - R(3.2)), (hx + R(2.5), hy - R(3))], OUT, 8)   # sobrolho
    # bufar: vapor a sair do focinho
    if t in (2, 3):
        vx, vy = hx + R(11.5) + (t - 2) * R(1.5), hy + R(4) - (t - 2) * R(1)
        P.append(Parte(elipse(vx, vy, R(1.2) + (t - 2), R(1.0) + (t - 2) * 0.5), ['#9babb2', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=9))
    if rei:
        # coroa de raízes com folhinhas na cabeça
        rx_, ry_ = hx + R(0.5), hy - R(5.2)
        for (a, b) in ((-3.5, -3.5), (-1, -5.5), (1.5, -5), (3.5, -3)):
            P.append(Parte(capsula(rx_ + R(a * 0.5), ry_, rx_ + R(a), ry_ + R(b), R(0.7)), ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], z=6))
            px(P, [(rx_ + R(a), ry_ + R(b) - 1)], '#91db69', 6.1)
            px(P, [(rx_ + R(a) + 1, ry_ + R(b) - 1)], '#1ebc73', 6.1)
        P.append(Parte(capsula(rx_ - R(3), ry_ + R(0.3), rx_ + R(3), ry_, R(0.9)), ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], z=6.2, volume='cilindro_h'))
        px(P, [(rx_, ry_)], '#f9c22b', 6.3)       # uma pedrinha de âmbar
        # flechas antigas espetadas no lombo (com penas)
        for (fx, fy, ang) in ((X(17), Y(27, dy), 0.75), (X(22), Y(25, dy), 0.35)):
            cx2, cy2 = fx + R(9) * math.cos(ang + math.pi), fy + R(9) * math.sin(ang + math.pi)
            P.append(Parte(capsula(fx, fy, cx2, cy2, 0.6), ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#c7dcd0'], z=6))
            px(P, [(cx2 - 1, cy2), (cx2 - 2, cy2 + 1), (cx2, cy2 - 1), (cx2 - 1, cy2 - 2)], '#e83b3b', 6.1)
            px(P, [(cx2 - 2, cy2 - 1), (cx2 - 3, cy2)], '#ffffff', 6.1)
        # cicatrizes de garras no flanco
        for (sx, sy) in ((X(20), Y(31, dy)), (X(22.5), Y(30.5, dy))):
            px(P, [(sx, sy), (sx + 1, sy + 1), (sx + 1, sy + 2), (sx + 2, sy + 3), (sx + 2, sy + 4)], '#cf657f', 2.3)
    return P


def javali(t):
    return desenhar(_javali(t, 1.0, 48), 48, 48)


def javali_rei(t):
    return desenhar(_javali(t, 1.27, 64, ox=1, rei=True), 64, 64)


# =====================================================================================
# 6. Cogumelo Andante (32)
def cogumelo_andante(t):
    P = []
    dy = [0, 0, 1, 0][t]
    # pés
    for x in (13, 19):
        P.append(Parte(elipse(x, 29.5, 2.4, 1.6), CAULE, z=0.5))
    # corpo (o pé do cogumelo) com cara
    corpo = elipse(16, 24 + dy * 0.5, 5.6, 5.8)
    P.append(Parte(corpo, CAULE, z=1))
    px(P, [(12, 26 + dy), (13, 27 + dy), (12, 23 + dy)], '#9babb2', 1.05)     # marcas do pé do cogumelo
    # bracinhos
    P.append(Parte(capsula(11, 23 + dy, 9.5, 26, 1.1), CAULE, z=0.8))
    P.append(Parte(capsula(21, 23 + dy, 23, 25.5 - (t == 3), 1.1), CAULE, z=1.5))
    # chapéu vermelho de pintas brancas
    cy = 12 + dy
    chap = {p for p in elipse(15.5, cy + 3, 11.5, 9) if p[1] <= cy + 3} | elipse(15.5, cy + 3, 11.8, 1.6)
    P.append(Parte(chap, VERMELHO, z=3))
    # lamelas por baixo do chapéu
    lam = {p for p in elipse(15.5, cy + 4.3, 10, 1.6) if p[1] >= cy + 4}
    P.append(Parte(lam, ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#c7dcd0'], z=2.9))
    px(P, [(x, cy + 5) for x in range(8, 24, 2)], '#966c6c', 2.95)
    for (sx, sy, r) in ((10, cy - 1, 1.8), (16, cy - 4, 2.0), (21.5, cy, 1.6), (13, cy + 2, 1.2), (24, cy + 3, 1.0), (7, cy + 2.5, 1.0)):
        P.append(Parte(elipse(sx, sy, r, r * 0.85), BRANCO, z=3.2, separar=False))
    px(P, [(9, cy - 3), (10, cy - 4), (11, cy - 5)], '#fca790', 3.3)            # brilho do chapéu
    # cara no corpo, virada para a direita
    ey = 21 + dy
    olho(P, 15, ey, '#45293f', z=5, fechado=(t == 2))
    olho(P, 18, ey, '#45293f', z=5, fechado=(t == 2))
    px(P, [(16, ey + 3), (17, ey + 3)], OUT, 5)
    px(P, [(14, ey + 2), (20, ey + 2)], '#f68181', 5)
    # esporos a subir (brilham)
    for i, (sx, sy) in enumerate(((5, 10), (27, 8), (24, 15))):
        yy = sy - ((t + i) % 4) * 2
        px(P, [(sx + (i % 2), yy)], ['#cddf6c', '#fbff86', '#d5e04b'][i], 6)
    # erva aos pés
    px(P, [(9, 30), (10, 29), (24, 30), (23, 29), (25, 29)], '#239063', 0.4)
    return desenhar(P, 32, 32)


# =====================================================================================
# 7. Fada Travessa (32)
def fada_travessa(t):
    P = []
    dy = [0, -1, -1, 0][t]
    asa = [0, 1, 2, 1][t]             # 0 = asas em cima, 2 = asas em baixo
    cx, cy = 16, 14 + dy
    # asas (duas de cada lado: a de trás mais escura), translúcidas com veios
    pontas_c = [(-8, -8), (-9, -5), (-9, -2)][asa]
    pontas_b = [(-6, 3), (-7, 4), (-6, 5)][asa]
    for (dx2, dy2, rampa, z, r) in ((pontas_c[0] + 2, pontas_c[1] - 1, ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'], 0.5, 2.4),
                                    (pontas_c[0], pontas_c[1], ASA, 1, 2.8), (pontas_b[0], pontas_b[1], ASA, 1.1, 2.0)):
        a = capsula(cx - 1, cy + 1, cx - 1 + dx2, cy + dy2, r)
        P.append(Parte(a, rampa, z=z))
        px(P, [(cx - 1 + dx2 * i / 6.0, cy + 1 + dy2 * i / 6.0) for i in range(2, 6)], '#0b8a8f', z + 0.01)
    # pernas
    P.append(Parte(capsula(cx, cy + 6, cx - 1, cy + 9, 0.8), RAMPAS['pele'], z=2))
    P.append(Parte(capsula(cx + 2, cy + 6, cx + 3, cy + 8.5, 0.8), RAMPAS['pele'], z=2.1))
    # vestido de folha
    vest = poligono([(cx - 1.5, cy + 1), (cx + 3.5, cy + 1), (cx + 5, cy + 7), (cx + 1, cy + 6), (cx - 3, cy + 7)])
    P.append(Parte(vest, FOLHA, z=3))
    px(P, [(cx + 1, cy + 2), (cx + 1, cy + 3), (cx + 1, cy + 4)], '#165a4c', 3.1)
    # braço com a varinha (estrela na ponta)
    P.append(Parte(capsula(cx + 3, cy + 2, cx + 6, cy + 1, 0.8), RAMPAS['pele'], z=4))
    px(P, [(cx + 7, cy), (cx + 8, cy - 1)], '#966c6c', 4.1)
    brilhinho(P, cx + 9, cy - 2, '#f9c22b', 4.2, grande=True)
    # cabeça, orelha bicuda e cabelo amarelo com carrapito
    P.append(Parte(elipse(cx + 1.5, cy - 2, 3.0, 2.8), RAMPAS['pele'], z=5))
    cab = {p for p in elipse(cx + 1, cy - 3.2, 3.4, 2.6) if p[0] <= cx + 3 or p[1] <= cy - 4} | elipse(cx - 1.5, cy - 6, 1.5, 1.4)
    cab |= capsula(cx - 1, cy - 2, cx - 2.5, cy + 1, 0.9)
    P.append(Parte(cab, OURO, z=5.5))
    px(P, [(cx - 1, cy - 1)], '#e6904e', 5.6)                                    # orelha bicuda
    px(P, [(cx - 2, cy - 2)], '#fca790', 5.6)
    # cara travessa: olho a brilhar e sorriso de lado
    olho(P, cx + 2, cy - 2, '#1ebc73', z=8, fechado=(t == 3))
    px(P, [(cx + 3, cy + 0), (cx + 4, cy - 1)], OUT, 8)
    px(P, [(cx + 4, cy - 0)], '#f68181', 8)
    # pó de fada a cair e brilhos à volta
    for i, (sx, sy) in enumerate(((cx - 6, cy + 9), (cx + 6, cy + 6), (cx - 2, cy + 12), (cx + 9, cy - 6), (cx - 9, cy - 4))):
        fase = (t + i) % 4
        if fase == 0:
            brilhinho(P, sx, sy, '#fbff86', 9, grande=True)
        elif fase in (1, 3):
            px(P, [(sx, sy + 1)], '#8ff8e2' if i % 2 else '#fbff86', 9)
    return desenhar(P, 32, 32)


# =====================================================================================
# 8. Abelha-Gigante (32) e Abelha-Rainha Melífera (48)
def _abelha(t, k, W, oy=0, rainha=False):
    P = []

    def X(v):
        return v * k

    def Y(v):
        return oy + v * k + bob

    def R(v):
        return v * k

    bob = [0, -1, 0, 1][t]
    asa = [0, 1, 2, 1][t]
    escuro = ['#2e222f', '#2e222f', '#3e3546', '#625565', '#7f708a']
    listra = AZUL_ESC if rainha else escuro
    cabeca_r = AZUL if rainha else escuro
    # asa de trás
    tips = [(-3, -7), (0, -7.5), (2, -5)]
    tx, ty = tips[asa]
    P.append(Parte(elipse_rot(X(16), Y(14), X(16 + tx - 2), Y(13 + ty + 1), R(2.2)), ['#7f708a', '#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0'], z=0.2))
    # patinhas a pender
    for (a, b, c2) in ((15.5, 19, -1.5), (18, 19.5, 0), (20.5, 19, 1.5)):
        P.append(Parte(capsula(X(a), Y(b), X(a + c2), Y(b + 3.5), R(0.6)), escuro, z=0.5))
    # abdómen às riscas, com ferrão
    ab = elipse(X(10), Y(17.5), R(6.3), R(5.0))
    P.append(Parte(poligono([(X(4.5), Y(16.5)), (X(1), Y(19)), (X(4.5), Y(20))]), escuro, z=0.9))
    P.append(Parte(ab, OURO, z=1))
    for (a, b) in ((6.5, 8.3), (10.5, 12.3)):
        P.append(Parte({p for p in ab if X(a) <= p[0] <= X(b)}, listra, z=1.1, separar=False))
    pelo(P, ab, OURO, 1.2, sem=2, dens=9, claro=False, passo=(0, 1))
    # tórax peludo
    tor = borda_pelo(elipse(X(17), Y(15.5), R(3.9), R(3.8)), 5, 'cima', 0.7)
    P.append(Parte(tor, LARANJA if not rainha else OURO, z=2))
    pelo(P, tor, LARANJA, 2.1, sem=3, dens=5, claro=True, passo=(0, 1))
    if rainha:
        # gola real de pelo branco
        gola = borda_pelo(elipse(X(19.5), Y(18.3), R(1.8), R(2.0)), 7, 'baixo', 0.9)
        P.append(Parte(gola, BRANCO, z=2.5))
    # cabeça com olho composto grande, antenas e mandíbulas
    hx, hy = X(22.5), Y(15.5)
    for (a, b) in ((0.5, -2.5), (2, -2.0)):
        ant = capsula(hx + R(a - 1), hy + R(b), hx + R(a + 1), hy + R(b - 4), R(0.5)) | capsula(hx + R(a + 1), hy + R(b - 4), hx + R(a + 3), hy + R(b - 4.5), R(0.5))
        P.append(Parte(ant, escuro, z=2.8 + a * 0.01))
    P.append(Parte(elipse(hx, hy, R(3.3), R(3.1)), cabeca_r, z=3))
    P.append(Parte(elipse(hx + R(0.8), hy - R(0.6), R(1.8), R(2.0)), ['#2e222f', '#323353', '#484a77', '#4d65b4', '#8fd3ff'] if not rainha else ['#2e222f', '#2e222f', '#323353', '#484a77', '#8fd3ff'], z=3.1))
    px(P, [(hx + R(0.2), hy - R(1.6))], BR, 3.2)
    P.append(Parte(capsula(hx + R(2.6), hy + R(1.6), hx + R(3.4), hy + R(2.6), R(0.6)), escuro, z=3.3))
    # asa da frente (por cima), com veios
    tips = [(-5, -7.5), (-1, -8.5), (2.5, -6)]
    tx, ty = tips[asa]
    asa_m = elipse_rot(X(17.5), Y(13.5), X(17.5 + tx), Y(12.5 + ty), R(2.7))
    P.append(Parte(asa_m, ASA_ABELHA, z=4))
    px(P, [(X(17.5) + tx * k * i / 5.0, Y(12.5) + ty * k * i / 5.0) for i in range(1, 5)], '#9babb2', 4.1)
    if rainha:
        # coroa de cera com pingos de mel
        cx2, cy2 = hx - R(0.5), hy - R(3.3)
        coroa = poligono([(cx2 - R(3), cy2 + R(0.8)), (cx2 - R(3.2), cy2 - R(2.5)), (cx2 - R(1.5), cy2 - R(1)), (cx2, cy2 - R(3.2)),
                          (cx2 + R(1.5), cy2 - R(1)), (cx2 + R(3.2), cy2 - R(2.5)), (cx2 + R(3), cy2 + R(0.8))])
        P.append(Parte(coroa, ['#9e4539', '#e6904e', '#fbb954', '#fbff86', '#ffffff'], z=5))
        px(P, [(cx2 - R(0.5), cy2 + R(1)), (cx2 + R(1.5), cy2 + R(1.2))], '#f79617', 5.1)
        # pingo de mel no ferrão
        g = [0, 1, 2, 3][t]
        gota(P, X(1.5), Y(20), OURO, z=5, comp=1 + g)
    return P


def abelha_gigante(t):
    return desenhar(_abelha(t, 1.0, 32, oy=1), 32, 32)


def abelha_rainha_melifera(t):
    return desenhar(_abelha(t, 1.5, 48, oy=-1, rainha=True), 48, 48)


# =====================================================================================
# 9. Treant Jovem (48)
def treant_jovem(t):
    P = []
    cx = 22
    dy = [0, 0, 1, 0][t]
    a = [0, 1, 0, -1][t]          # a copa abana
    # pernas de raízes (a de trás escura)
    P.append(Parte(capsula(cx - 4, 37, cx - 7, 44, 3.0), CASCA_ESC, z=0))
    for (tx, r) in ((-5, 1.6), (-1, 1.4)):
        P.append(Parte(capsula(cx - 7, 44, cx - 7 + tx, 46, r), CASCA_ESC, z=0.1))
    P.append(Parte(capsula(cx + 4, 37, cx + 6, 44, 3.2), CASCA, z=3, volume='cilindro_v'))
    for (tx, r) in ((-3, 1.5), (1, 1.6), (5, 1.4)):
        P.append(Parte(capsula(cx + 6, 44, cx + 6 + tx, 46, r), CASCA, z=3.1))
    # braço de trás (galho) com folhas
    P.append(Parte(capsula(cx - 6, 27 + dy, cx - 13, 31 + dy, 2.0) | capsula(cx - 13, 31 + dy, cx - 17, 28 + dy, 1.4), CASCA_ESC, z=0.5))
    P.append(Parte(tufo(cx - 18, 26 + dy, 3.4, 41), FOLHA_ESC, z=0.6))
    # tronco
    contorno = [(cx - 9, 40), (cx - 7, 32), (cx - 8, 24), (cx - 5, 16), (cx + 5, 16), (cx + 8, 24), (cx + 7, 32), (cx + 10, 40)]
    tronco = poligono([(x, y + dy) for x, y in contorno])
    P.append(Parte(tronco, CASCA, z=2, volume='cilindro_v'))
    veio, luz = [], []
    for (x, y) in tronco:
        u = x + 1.6 * math.sin((y - dy) / 5.0 + x * 0.4)
        if int(u) % 5 == 0 and (y * 3 + x) % 7 != 0:
            veio.append((x, y))
        elif int(u) % 5 == 1 and x < cx and (x + y) % 3 == 0:
            luz.append((x, y))
    px(P, veio, '#45293f', 2.1)
    px(P, luz, '#ab947a', 2.1)
    # nó, musgo e um cogumelo
    px(P, elipse(cx - 3, 35 + dy, 1.6, 2.0), '#2e222f', 2.2)
    P.append(Parte({p for p in elipse(cx - 6, 39 + dy, 3, 1.5) if p in tronco}, MUSGO, z=2.3, separar=False))
    cogumelinho(P, cx - 9, 34 + dy, 2.4)
    # copa: tufos de folhas, com uma bolota pendurada e uma flor
    for (tx, ty, r, sem, rampa) in ((-9, 13, 8, 1, FOLHA_ESC), (8, 12, 8, 2, FOLHA_ESC), (-2, 8, 10, 3, FOLHA), (7, 6, 7, 4, FOLHA),
                                    (-10, 7, 6, 5, FOLHA), (1, 14, 6, 6, FOLHA)):
        m = tufo(cx + tx + a, ty + dy, r, sem)
        P.append(Parte(m, rampa, z=2.6 + sem * 0.01))
        folhagem(P, m, rampa, 2.6 + sem * 0.01, sem)
    for (fx, fy) in ((cx - 12 + a, 4), (cx + 4 + a, 1), (cx + 12 + a, 10)):
        px(P, [(fx, fy + dy), (fx + 1, fy + dy)], '#cddf6c', 2.8)
    # folhas de outono (amarelas) a espreitar
    px(P, [(cx - 14 + a, 11 + dy), (cx - 13 + a, 12 + dy), (cx + 13 + a, 15 + dy)], '#f9c22b', 2.8)
    P.append(Parte(capsula(cx + 10 + a, 18 + dy, cx + 10 + a, 20 + dy, 0.5), CASCA, z=2.9))
    P.append(Parte(elipse(cx + 10.5 + a, 22 + dy, 1.7, 2.0), ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], z=2.95))
    P.append(Parte({p for p in elipse(cx + 10.5 + a, 20.6 + dy, 2.0, 1.2) if p[1] <= 21 + dy}, ['#4c3e24', '#4c3e24', '#676633', '#a2a947', '#a2a947'], z=2.96))
    # cara entalhada no tronco (virada para a direita)
    fx, fy = cx - 4, 27 + dy
    for ex in (fx, fx + 5):
        if t == 2:
            px(P, [(ex, fy + 1), (ex + 1, fy + 1), (ex + 2, fy + 1)], OUT, 5)
        else:
            px(P, elipse(ex + 1.5, fy + 1, 2.0, 1.8), OUT, 5)
            px(P, [(ex + 1, fy + 1), (ex + 2, fy + 1)], '#cddf6c', 5.1)
            px(P, [(ex + 1, fy)], BR, 5.2)
    P.append(Parte(capsula(fx - 1, fy - 2.5, fx + 3, fy - 2, 0.9), CASCA, z=5.3, volume='cilindro_h'))
    P.append(Parte(capsula(fx + 5, fy - 2, fx + 8, fy - 2.5, 0.9), CASCA, z=5.3, volume='cilindro_h'))
    P.append(Parte(capsula(fx + 3.5, fy + 2, fx + 5.5, fy + 4, 1.1), CASCA, z=5.4))         # nariz de nó
    px(P, [(x, fy + 6 + (x % 2)) for x in range(fx + 1, fx + 7)], OUT, 5)                     # boca
    # braço da frente (galho com dedos de raminho) e um tufo de folhas
    om = (cx + 7, 27 + dy)
    mao = (cx + 15, 31 + dy + a)
    P.append(Parte(capsula(*om, cx + 11, 30 + dy, 2.2) | capsula(cx + 11, 30 + dy, *mao, 1.8), CASCA, z=6, volume='cilindro_h'))
    for (dx2, dy2) in ((3, -1), (3, 2), (1, 3)):
        P.append(Parte(capsula(*mao, mao[0] + dx2, mao[1] + dy2, 0.8), CASCA, z=6.1))
    m = tufo(cx + 12, 26 + dy + a, 3.0, 51)
    P.append(Parte(m, FOLHA, z=6.2))
    return desenhar(P, 48, 48)


# =====================================================================================
# 10. Coelho-Chifre Ancião (48): enorme, cinzento, um chifre partido e cicatrizes
def coelho_chifre_anciao(t):
    P = []
    dy = [0, 0, 1, 0][t]
    orelha = [0, -1, 0, 1][t]
    rp = CINZA
    re = CINZA_ESC
    hx, hy = 31, 22 + dy
    # orelha de trás (com um rasgão)
    P.append(Parte(capsula(hx - 3, hy - 3, hx - 9 + orelha, hy - 16, 2.0), re, z=1))
    # patas do lado de lá
    P.append(Parte(capsula(13, 44.5, 22, 44.5, 2.0), re, z=1.2))
    P.append(Parte(capsula(29, 37 + dy, 30.5, 44.5, 1.7), re, z=1.2))
    # cauda
    P.append(Parte(borda_pelo(elipse(9, 31 + dy, 3.4, 3.2), 3, 'cima', 0.6), BRANCO, z=1.5))
    # corpo grande e musculado
    corpo = borda_pelo(elipse(18.5, 34 + dy, 10, 8.4) | elipse(26, 33 + dy, 6.6, 7.4), 5, 'cima', 0.45)
    P.append(Parte(corpo, rp, z=2))
    pelo(P, corpo, rp, 2, sem=1, dens=6, passo=(-1, 0))
    px(P, [p for p in elipse(26, 39 + dy, 5, 3.2) if p in corpo], '#9babb2', 2.1)
    # cicatrizes no flanco
    for (sx, sy) in ((17, 30 + dy), (20, 29 + dy), (23, 30 + dy)):
        px(P, [(sx, sy), (sx + 1, sy + 1), (sx + 1, sy + 2), (sx + 2, sy + 3), (sx + 2, sy + 4)], '#cf657f', 2.3)
        px(P, [(sx - 1, sy)], '#ed8099', 2.3)
    # coxa enorme e pé comprido
    P.append(Parte(elipse(16, 36.5 + dy, 6, 5.6), rp, z=2.5))
    pelo(P, elipse(16, 36.5 + dy, 6, 5.6), rp, 2.5, sem=7, dens=7, claro=False, passo=(-1, 0))
    P.append(Parte(capsula(12, 44.5, 23, 44.5, 2.1), rp, z=2.6))
    px(P, [(23, 45), (24, 45), (24, 44)], '#c7dcd0', 2.7)
    # pata da frente
    P.append(Parte(capsula(27, 37 + dy, 27.5, 44.5, 1.8), rp, z=2.8))
    px(P, [(28, 45), (29, 45)], '#c7dcd0', 2.9)
    # cabeça com bochechas fofas e "barba" de pelo
    cab = elipse(hx, hy, 6.4, 5.6) | elipse(hx + 4, hy + 2, 4.0, 3.4)
    cab = borda_pelo(cab, 9, 'baixo', 0.7)
    P.append(Parte(cab, rp, z=4))
    pelo(P, cab, rp, 4, sem=3, dens=8, claro=False, passo=(-1, 0))
    barba = borda_pelo({p for p in elipse(hx + 1, hy + 5, 4, 2.2)}, 2, 'baixo', 0.9)
    P.append(Parte(barba, BRANCO, z=4.2, separar=False))
    # orelha da frente (rasgada na ponta), interior cor-de-rosa
    ox = hx - 2 + orelha
    ore = capsula(hx - 2, hy - 4, ox - 2, hy - 18, 2.4)
    ore -= {(int(ox - 1), int(hy - 18)), (int(ox - 1), int(hy - 17)), (int(ox - 1), int(hy - 19)), (int(ox), int(hy - 17))}
    P.append(Parte(ore, rp, z=5))
    for i in range(3, 12):
        px(P, [(round(hx - 2 + (ox - hx) * i / 14.0), hy - 4 - i)], '#cf657f', 5.1)
    # chifre partido (a ponta foi-se: base grossa, corte em bisel)
    ch = poligono([(hx, hy - 4), (hx + 5, hy - 5.5), (hx + 6.5, hy - 11), (hx + 4, hy - 12)])
    P.append(Parte(ch, MARFIM, z=6))
    px(P, [(hx + 3, hy - 7), (hx + 4, hy - 7), (hx + 4, hy - 9), (hx + 5, hy - 9)], '#966c6c', 6.1)
    px(P, [(hx + 5, hy - 11), (hx + 4, hy - 11)], '#c7dcd0', 6.1)
    # olho zangado com cicatriz por cima
    olho(P, hx + 2, hy - 2, '#e83b3b', z=8, tam=3, fechado=(t == 3))
    px(P, [(hx + 1, hy - 4), (hx + 2, hy - 3), (hx + 3, hy - 3), (hx + 4, hy - 3), (hx + 5, hy - 4)], OUT, 8)     # sobrolho
    px(P, [(hx + 1, hy - 6), (hx + 2, hy - 5), (hx + 2, hy + 1), (hx + 3, hy + 2)], '#ed8099', 8)               # cicatriz
    px(P, [(hx + 8, hy + 1), (hx + 8, hy + 2)], '#f04f78', 8)                                                   # nariz
    if t == 1:
        px(P, [(hx + 8, hy)], '#f68181', 8)
    px(P, [(hx + 6, hy + 4), (hx + 7, hy + 4)], OUT, 8)
    px(P, [(hx + 7, hy + 5)], BR, 8)                                                                            # dentão
    px(P, [(hx + 9, hy + 3), (hx + 10, hy + 3), (hx + 11, hy + 4), (hx + 9, hy + 5), (hx + 10, hy + 6)], '#c7dcd0', 8)  # bigodes
    return desenhar(P, 48, 48)


# =====================================================================================
# 11. Coruja Sombria (48): coruja negra de olhos amarelos, a voar
def coruja_sombria(t):
    P = []
    bob = [0, -1, 0, 1][t]
    asa = [0, 1, 2, 1][t]          # 0 = asas em cima, 2 = em baixo
    pen = ROXO_ESC
    cx, cy = 24, 25 + bob
    # asa de trás (esquerda, mais escura): penas em leque
    pontas = [[(-20, -14), (-21, -9), (-19, -4), (-15, 0)], [(-21, -8), (-21, -3), (-18, 2), (-14, 5)], [(-19, 0), (-18, 5), (-15, 9), (-11, 11)]][asa]
    for i, (dx, dy) in enumerate(pontas):
        P.append(Parte(elipse_rot(cx - 5, cy - 3, cx + dx, cy + dy, 2.4), ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9'], z=0.2 + i * 0.01))
    # cauda
    P.append(Parte(poligono([(cx - 5, cy + 6), (cx - 11, cy + 13), (cx - 6, cy + 14), (cx - 1, cy + 8)]), ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9'], z=0.5))
    # garras alaranjadas a pender
    for (gx, gl) in ((cx - 2, 0), (cx + 2, 1)):
        P.append(Parte(capsula(gx, cy + 9, gx + gl, cy + 13, 1.1), LARANJA, z=0.8))
        px(P, [(gx - 1 + gl, cy + 14), (gx + gl, cy + 14), (gx + 1 + gl, cy + 14)], OUT, 0.9)
    # corpo com peito de penas em escamas
    corpo = elipse(cx, cy + 1, 8, 10)
    P.append(Parte(corpo, pen, z=1))
    peito = {p for p in elipse(cx + 2, cy + 4, 5, 6.5) if p in corpo}
    P.append(Parte(peito, ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'], z=1.1, separar=False))
    for j, yy in enumerate(range(int(cy) + 0, int(cy) + 10, 3)):
        for xx in range(int(cx) - 2 + (j % 2), int(cx) + 7, 3):
            if (xx, yy) in peito:
                px(P, [(xx, yy), (xx - 1, yy - 1), (xx + 1, yy - 1)], '#45293f', 1.2)
    # cabeça redonda com orelhas de penas
    hx, hy = cx + 2, cy - 10
    for (ax, ay, bx) in ((-6, -3, -8), (4, -3, 6)):
        P.append(Parte(poligono([(hx + ax, hy + ay + 1), (hx + bx, hy + ay - 6), (hx + ax + 3.5, hy + ay - 1)]), pen, z=1.9))
    P.append(Parte(elipse(hx, hy, 8, 7), pen, z=2))
    # disco facial (mais claro) e olhos amarelos enormes
    disco = elipse(hx - 3, hy + 0.5, 3.6, 3.6) | elipse(hx + 3.5, hy + 0.5, 3.6, 3.6)
    P.append(Parte(disco, ['#45293f', '#6b3e75', '#6b3e75', '#905ea9', '#a884f3'], z=2.1, separar=False))
    for ex in (hx - 5, hx + 1.5):
        if t == 3:
            px(P, [(ex + i, hy + 1) for i in range(4)], OUT, 3)
            px(P, [(ex + i, hy) for i in range(4)], '#f9c22b', 3)
        else:
            P.append(Parte(elipse(ex + 2, hy + 0.5, 2.4, 2.4), ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'], z=3))
            px(P, [(ex + 2, hy), (ex + 3, hy), (ex + 2, hy + 1), (ex + 3, hy + 1)], OUT, 3.1)
            px(P, [(ex + 1, hy - 1)], BR, 3.2)
    # sobrancelhas zangadas (penas em V)
    px(P, [(hx - 6, hy - 4), (hx - 5, hy - 4), (hx - 4, hy - 3), (hx - 3, hy - 3), (hx - 2, hy - 2)], '#a884f3', 3.3)
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 3), (hx + 3, hy - 3), (hx + 4, hy - 4), (hx + 5, hy - 4)], '#a884f3', 3.3)
    # bico
    P.append(Parte(poligono([(hx - 1, hy + 2), (hx + 1.5, hy + 2), (hx + 0.5, hy + 5.5)]), ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86'], z=3.4))
    # asa da frente (direita): por cima do corpo
    pontas = [[(17, -16), (20, -11), (21, -6), (19, -1)], [(19, -9), (21, -4), (20, 1), (17, 5)], [(17, 0), (17, 5), (14, 9), (10, 11)]][asa]
    for i, (dx, dy) in enumerate(pontas):
        P.append(Parte(elipse_rot(cx + 5, cy - 2, cx + dx, cy + dy, 2.6), pen, z=4 + i * 0.01))
        px(P, [(cx + dx - (1 if dx > 0 else -1) * 1, cy + dy)], '#a884f3', 4.2)
    # brilhinhos de sombra (fumo roxo) que a seguem
    for i, (sx, sy) in enumerate(((cx - 14, cy + 12), (cx + 14, cy + 10), (cx - 10, cy - 15))):
        if (t + i) % 4 in (0, 1):
            px(P, [(sx, sy - (t + i) % 4), (sx + 1, sy - (t + i) % 4)], '#6b3e75', 5)
    return desenhar(P, 48, 48)


# =====================================================================================
# 12. Lagostim Couraçado (48): azul-escuro, pinças grandes
def lagostim_couracado(t):
    P = []
    dy = [0, 0, 1, 0][t]
    pinca = [0, 1, 2, 1][t]        # as pinças abrem e fecham
    ant = [0, 1, 0, -1][t]
    base = 46
    # patas finas
    for i, x in enumerate((18, 21, 24, 27)):
        P.append(Parte(capsula(x, 37 + dy, x - 2, 41, 0.9) | capsula(x - 2, 41, x - 1, base - 0.5, 0.7), AZUL_ESC, z=0.2))
    # pinça de trás (mais pequena e escura, levantada)
    P.append(Parte(capsula(28, 33 + dy, 32, 27 + dy, 1.5), AZUL_ESC, z=0.4))
    P.append(Parte(elipse_rot(31, 26 + dy, 36, 22 + dy, 2.3), AZUL_ESC, z=0.5))
    P.append(Parte(elipse_rot(35, 21 + dy, 39, 18 + dy - pinca * 0.5, 1.0), AZUL_ESC, z=0.45))
    P.append(Parte(elipse_rot(36, 23 + dy, 40, 21 + dy, 1.0), AZUL_ESC, z=0.45))
    # cauda em segmentos e leque
    segs = [(17, 35, 4.6, 4.2), (12.5, 36.5, 4.0, 3.8), (8.5, 38.5, 3.5, 3.4), (5.5, 40.5, 3.0, 2.9)]
    for i, (sx, sy, rx, ry) in enumerate(segs):
        m = elipse(sx, sy + dy, rx, ry)
        P.append(Parte(m, AZUL, z=1 + (len(segs) - i) * 0.01))
    for (lx, ly) in ((-6, -3), (-6.5, 0.5), (-4, 3)):
        P.append(Parte(elipse_rot(4, 41 + dy, 4 + lx, 41 + dy + ly, 1.4), AZUL, z=0.9))
    # carapaça com três espinhos, cabeça e rostro
    car = elipse(25, 33 + dy, 8, 5.8)
    for (sx, h) in ((22, 2.5), (25.5, 3), (29, 2.5)):
        car |= poligono([(sx - 1.3, 28.5 + dy), (sx, 28.5 + dy - h), (sx + 1.3, 28.5 + dy)])
    P.append(Parte(car, AZUL, z=2))
    cabeca = elipse(32.5, 33 + dy, 4, 3.6) | poligono([(33, 30.5 + dy), (39, 31.5 + dy), (34, 33 + dy)])
    P.append(Parte(cabeca, AZUL, z=2.1))
    px(P, [(x, 35 + dy) for x in range(19, 31) if x % 3 != 0], '#323353', 2.05)          # costura da carapaça
    px(P, [(21, 31 + dy), (24, 30 + dy), (27, 31 + dy)], '#8fd3ff', 2.06)
    # cracas e uma alga agarradas
    px(P, [(19, 31 + dy), (20, 31 + dy)], '#c7dcd0', 2.1)
    px(P, [(19, 30 + dy)], '#9babb2', 2.1)
    P.append(Parte(capsula(16, 32 + dy, 14, 28 + dy - (t % 2), 0.7), ['#165a4c', '#239063', '#1ebc73', '#91db69', '#91db69'], z=2.15))
    # olho no pedúnculo
    P.append(Parte(capsula(32, 31 + dy, 32, 29 + dy, 0.7), AZUL_ESC, z=2.2))
    P.append(Parte(elipse(32.5, 28.5 + dy, 1.3, 1.3), ['#2e222f', '#2e222f', '#2e222f', '#3e3546', '#3e3546'], z=2.3))
    px(P, [(32, 28 + dy)], BR, 2.4)
    # antenas compridas (abanam)
    for (comp, alt, cor) in ((13, -12, '#4d65b4'), (10, -8, '#484a77')):
        px(P, [(37 + i * 0.8, 30 + dy + alt * (i / comp) + ant * (i / comp) ** 2 * 2) for i in range(comp)], cor, 2.5)
    # pinça da frente: braço, pulso, palma grande e dois dedos (com dentes e ponta vermelha)
    P.append(Parte(capsula(30, 37 + dy, 34, 33 + dy, 2.0), AZUL, z=3, volume='cilindro_h'))
    P.append(Parte(elipse(35, 31.5 + dy, 2.3, 2.1), AZUL, z=3.1))
    palma = elipse_rot(35, 30 + dy, 42, 28 + dy, 3.8)
    sup = elipse_rot(40, 25.5 + dy, 47, 24 + dy - pinca, 1.5)
    inf = elipse_rot(41, 30.5 + dy, 47, 31 + dy, 1.4)
    P.append(Parte(inf, AZUL, z=3.2))
    P.append(Parte(palma, AZUL, z=3.3))
    P.append(Parte(sup, AZUL, z=3.4))
    px(P, [(46, 23 + dy - pinca), (47, 23 + dy - pinca), (46, 31 + dy), (47, 31 + dy)], '#ea4f36', 3.5)
    px(P, [(43, 26 + dy - pinca // 2), (45, 26 + dy - pinca // 2), (44, 30 + dy)], '#c7dcd0', 3.5)
    px(P, [(36, 28 + dy), (37, 27 + dy), (38, 27 + dy)], '#8fd3ff', 3.5)
    # bolhas a subir
    for i, (bx, by) in enumerate(((38, 22), (35, 17))):
        yy = by - (t + i * 2) % 4
        px(P, [(bx, yy), (bx + 1, yy - 1), (bx - 1, yy - 1), (bx, yy - 2)], '#8fd3ff', 5)
    return desenhar(P, 48, 48)


# =====================================================================================
# 13. Rainha dos Esporos (64): cogumelo gigante com vestido de lamelas e coroa de esporos
def rainha_dos_esporos(t):
    P = []
    dy = [0, 0, 1, 0][t]
    cx = 31
    # vestido de lamelas (pregas verticais), assenta no chão
    vest = poligono([(cx - 6, 36 + dy), (cx + 6, 36 + dy), (cx + 14, 61), (cx - 14, 61)])
    bainha = set()
    for i in range(-14, 15, 4):
        bainha |= elipse(cx + i + 2, 61, 2.2, 1.6)
    vest |= {p for p in bainha if p[1] <= 62}
    P.append(Parte(vest, LILAS, z=1, volume='cilindro_v'))
    for (x, y) in vest:
        rel = (x - cx) / max(1.0, 6 + (y - 34 - dy) * 8 / 27.0)
        if abs(round(rel * 4) - rel * 4) < 0.12 and y > 37 + dy:
            px(P, [(x, y)], '#753c54', 1.1)
        elif abs(round(rel * 4) - rel * 4 - 0.28) < 0.1 and y > 38 + dy and x < cx:
            px(P, [(x, y)], '#ed8099', 1.1)
    px(P, [(x, 60) for x in range(cx - 13, cx + 14) if x % 4 == 1], '#fdcbb0', 1.2)
    # esporos-pérola a enfeitar o vestido
    for (ex2, ey2) in ((cx - 4, 44), (cx + 3, 48), (cx - 7, 53), (cx + 8, 55), (cx, 56)):
        px(P, [(ex2, ey2 + dy)], '#fbff86', 1.3)
    # braço de trás e o ceptro-cogumelo na mão da frente
    P.append(Parte(capsula(cx - 4, 37 + dy, cx - 9, 45 + dy, 1.5), CAULE, z=0.8))
    sx = cx + 13
    P.append(Parte(capsula(sx, 34 + dy, sx + 1, 60, 1.0), ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], z=1.5))
    P.append(Parte({p for p in elipse(sx + 0.5, 34 + dy, 3.6, 2.8) if p[1] <= 34 + dy}, ROSA, z=1.6))
    px(P, [(sx - 1, 32 + dy), (sx + 1, 33 + dy)], BR, 1.7)
    brilho_c = (t % 2 == 0)
    if brilho_c:
        brilhinho(P, sx + 0.5, 28 + dy, '#d5e04b', 1.8, grande=True)
    # pescoço e cabeça (branca, de rainha)
    P.append(Parte(capsula(cx, 32 + dy, cx, 37 + dy, 2.2), CAULE, z=2))
    cab = elipse(cx + 2, 30 + dy, 6.2, 5.4)
    P.append(Parte(cab, CAULE, z=2.2))
    # braço da frente a segurar o ceptro
    P.append(Parte(capsula(cx + 3, 36 + dy, cx + 9, 40 + dy, 1.4) | capsula(cx + 9, 40 + dy, sx, 37 + dy, 1.2), CAULE, z=2.5))
    # gola de lamelas
    gola = set()
    for i in range(-6, 7, 3):
        gola |= elipse(cx + i, 36 + dy, 2, 1.6)
    P.append(Parte(gola, ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'], z=2.4))
    # chapéu enorme roxo com pintas que brilham
    chy = 19 + dy
    chap = {p for p in elipse(cx, chy + 4, 21, 11) if p[1] <= chy + 4} | elipse(cx, chy + 4, 21.5, 2.2)
    P.append(Parte(chap, ROXO, z=3))
    lam = {p for p in elipse(cx, chy + 5.4, 18, 2.4) if p[1] >= chy + 5}
    P.append(Parte(lam, ['#45293f', '#753c54', '#a24b6f', '#cf657f', '#cf657f'], z=2.9))
    px(P, [(x, chy + 6) for x in range(cx - 16, cx + 17, 2)], '#45293f', 2.95)
    pulso = [0, 1, 2, 1][t]
    for i, (px_, py_, r) in enumerate(((cx - 12, chy - 1, 2.6), (cx - 3, chy - 6, 3.0), (cx + 8, chy - 3, 2.6), (cx + 15, chy + 2, 1.8),
                                       (cx - 17, chy + 3, 1.6), (cx + 2, chy + 1, 1.8), (cx - 8, chy + 3, 1.4))):
        P.append(Parte(elipse(px_, py_, r, r * 0.8), ROSA, z=3.1 + i * 0.01, separar=False))
        if (i + pulso) % 3 == 0:
            px(P, [(px_ - 1, py_ - 1)], BR, 3.2)
        else:
            px(P, [(px_ - 1, py_ - 1)], '#fdcbb0', 3.2)
    px(P, [(cx - 14, chy - 5), (cx - 13, chy - 6), (cx - 12, chy - 7), (cx - 11, chy - 7)], '#eaaded', 3.3)
    # coroa de esporos: hastes com bolas de luz que pulsam
    for i, (hx2, alt) in enumerate(((-9, 3), (-3, 5), (3, 5.5), (9, 3.5))):
        topo = min(y for (x, y) in chap if x == cx + hx2)
        P.append(Parte(capsula(cx + hx2, topo + 1, cx + hx2 + 0.5, topo - alt, 0.7), ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#d5e04b'], z=3.4))
        r = 1.8 + (0.6 if (i + t) % 4 == 0 else 0)
        P.append(Parte(elipse(cx + hx2 + 0.5, topo - alt - 1, r, r), MUSGO_VIVO, z=3.5))
        px(P, [(cx + hx2, topo - alt - 2)], BR, 3.6)
    # cara: olhos de pestanas compridas, boca pequena e bochechas
    fy = 29 + dy
    for ex in (cx + 1, cx + 5):
        if t == 3:
            px(P, [(ex, fy + 1), (ex + 1, fy + 1), (ex + 2, fy + 1)], OUT, 5)
        else:
            olho(P, ex, fy, '#6b3e75', z=5, tam=3)
        px(P, [(ex + 2, fy - 1), (ex + 3, fy - 2)], OUT, 5.1)
    px(P, [(cx + 4, fy + 4), (cx + 5, fy + 4)], '#c32454', 5)
    px(P, [(cx - 1, fy + 3), (cx + 8, fy + 3)], '#f68181', 5)
    # esporos a flutuar à volta (sobem e brilham)
    for i, (sx2, sy2) in enumerate(((cx - 20, 30), (cx + 20, 26), (cx - 16, 44), (cx + 19, 47), (cx - 22, 18), (cx + 23, 12))):
        yy = sy2 - ((t + i) % 4) * 2
        cor = ['#d5e04b', '#fbff86', '#eaaded'][i % 3]
        if (t + i) % 4 == 1:
            brilhinho(P, sx2, yy, cor, 6, grande=True)
        else:
            px(P, [(sx2, yy)], cor, 6)
    return desenhar(P, 64, 64)


# =====================================================================================
# 14. Guardião de Musgo (64): golem de raízes e pedra coberto de musgo, olhos verdes
def guardiao_de_musgo(t):
    P = []
    dy = [0, 0, 1, 0][t]
    fio = [0, 1, 0, -1][t]
    cx = 31
    # pernas de raízes (a de trás escura)
    P.append(Parte(capsula(cx - 7, 46 + dy, cx - 10, 58, 4.0), CASCA_ESC, z=0))
    for (tx, r) in ((-5, 2.0), (0, 1.8), (4, 1.6)):
        P.append(Parte(capsula(cx - 10, 58, cx - 10 + tx, 62, r), CASCA_ESC, z=0.1))
    # braço de trás (raízes) com punho de pedra
    P.append(Parte(capsula(cx - 12, 32 + dy, cx - 18, 42 + dy, 3.4) | capsula(cx - 18, 42 + dy, cx - 19, 49 + dy, 3.0), CASCA_ESC, z=0.3))
    P.append(Parte(elipse(cx - 19, 52 + dy, 4.5, 4.0), PEDRA, z=0.4))
    # tronco: um pedregulho
    tronco = elipse(cx, 37 + dy, 16, 13.5)
    P.append(Parte(tronco, PEDRA_CLARA, z=1))
    # rachas na pedra e pintas
    for (a, b) in (((cx - 10, 36), (cx - 6, 40)), ((cx - 6, 40), (cx - 7, 45)), ((cx + 6, 42), (cx + 10, 46))):
        n = int(max(abs(b[0] - a[0]), abs(b[1] - a[1])))
        px(P, [(a[0] + (b[0] - a[0]) * i / n, a[1] + dy + (b[1] - a[1]) * i / n) for i in range(n + 1)], '#3e3546', 1.1)
    pintas(P, tronco, '#625565', 1.05, sem=9, dens=13)
    # runas verdes a brilhar no peito
    brilha = '#91db69' if t in (0, 3) else '#cddf6c'
    for (rx2, ry2) in ((cx + 2, 40), (cx + 6, 38)):
        px(P, [(rx2, ry2 + dy), (rx2, ry2 + 1 + dy), (rx2 + 1, ry2 + 2 + dy), (rx2 - 1, ry2 + 2 + dy), (rx2, ry2 + 3 + dy)], brilha, 1.2)
    # raízes a envolver a pedra
    for (a, b, c) in (((cx - 14, 30), (cx - 4, 36), (cx + 3, 49)), ((cx + 13, 31), (cx + 9, 41), (cx + 12, 49))):
        P.append(Parte(capsula(a[0], a[1] + dy, b[0], b[1] + dy, 1.4) | capsula(b[0], b[1] + dy, c[0], c[1] + dy, 1.2), CASCA, z=1.3))
    # perna da frente
    P.append(Parte(capsula(cx + 7, 47 + dy, cx + 9, 58, 4.2), CASCA, z=2, volume='cilindro_v'))
    for (tx, r) in ((-4, 1.8), (1, 2.0), (6, 1.7)):
        P.append(Parte(capsula(cx + 9, 58, cx + 9 + tx, 62, r), CASCA, z=2.1))
    # manto de musgo nos ombros e no cocuruto (com flores e um cogumelo)
    for (tx, ty, r, sem) in ((-9, 27, 9, 1), (2, 23, 10, 2), (12, 27, 8, 3)):
        m = tufo(cx + tx, ty + dy, r, sem, ry=r * 0.6)
        P.append(Parte(m, FOLHA, z=3 + sem * 0.01))
        folhagem(P, m, FOLHA, 3 + sem * 0.01, sem)
    # fios de musgo pendurados (abanam)
    for i, x in enumerate(range(cx - 14, cx + 6, 3)):
        comp = 2 + (i * 5) % 5
        topo = max([y for (xx, y) in P[-1].m if xx == x] or [29 + dy])
        fio_px = [(x + (fio if j > comp // 2 and i % 2 else 0), topo + 1 + j) for j in range(comp)]
        px(P, fio_px, '#239063', 3.05)
        px(P, fio_px[-1:], '#1ebc73', 3.06)
    for (fx2, fy2, cor) in ((cx - 10, 22, '#ffffff'), (cx + 6, 19, '#f9c22b'), (cx + 15, 24, '#ffffff'), (cx - 3, 18, '#f68181')):
        px(P, [(fx2 - 1, fy2 + dy), (fx2 + 1, fy2 + dy), (fx2, fy2 - 1 + dy), (fx2, fy2 + 1 + dy)], cor, 3.2)
        px(P, [(fx2, fy2 + dy)], '#f9c22b' if cor != '#f9c22b' else '#cd683d', 3.21)
    cogumelinho(P, cx - 15, 25 + dy, 3.3)
    # cabeça de pedra encaixada à frente, com olhos verdes que brilham
    hx, hy = cx + 12, 26 + dy
    cabeca = elipse(hx, hy, 7, 6)
    P.append(Parte(cabeca, PEDRA_CLARA, z=4))
    P.append(Parte(capsula(hx - 6, hy - 4, hx + 6, hy - 5, 2.0), PEDRA, z=4.1, volume='cilindro_h'))            # testa (sobrolho)
    m = tufo(hx - 2, hy - 7, 5, 9, ry=2.8)
    P.append(Parte(m, FOLHA, z=4.2))
    folhagem(P, m, FOLHA, 4.2, 9)
    olho_c = '#91db69' if t != 2 else '#cddf6c'
    for ex in (hx - 3, hx + 2):
        px(P, [(ex + i, hy - 2 + j) for i in range(4) for j in range(3)], OUT, 5)
        px(P, [(ex + 1, hy - 1), (ex + 2, hy - 1), (ex + 3, hy - 1), (ex + 1, hy), (ex + 2, hy)], olho_c, 5.1)
        px(P, [(ex + 1, hy - 1)], BR, 5.2)
    px(P, [(x, hy + 3 + (x % 2)) for x in range(hx - 1, hx + 5)], OUT, 5)          # boca de racha
    # braço da frente: raízes grossas e um punho de pedra com dedos de raiz
    om = (cx + 14, 36 + dy)
    co = (cx + 20, 42 + dy)
    P.append(Parte(capsula(*om, *co, 3.6) | capsula(*co, cx + 22, 50 + dy, 3.0), CASCA, z=6, volume='cilindro_h'))
    P.append(Parte(elipse(cx + 22, 53 + dy, 5, 4.4), PEDRA_CLARA, z=6.1))
    px(P, [(cx + 20, 52 + dy), (cx + 21, 51 + dy), (cx + 24, 52 + dy)], '#3e3546', 6.2)
    for (dx2, dy2) in ((-3, 5), (1, 6), (4, 5)):
        P.append(Parte(capsula(cx + 22 + dx2, 55 + dy, cx + 22 + dx2 * 1.3, 55 + dy2 + dy, 0.9), CASCA, z=6.3))
    m = tufo(cx + 15, 36 + dy, 4.0, 12, ry=2.4)
    P.append(Parte(m, FOLHA, z=6.4))
    folhagem(P, m, FOLHA, 6.4, 12)
    return desenhar(P, 64, 64)


# =====================================================================================
# 15. Cavaleiro de Pedra Musgosa (48): estátua de cavaleiro viva, espada partida, escudo
def cavaleiro_de_pedra_musgosa(t):
    P = []
    dy = [0, 0, 1, 0][t]
    cx = 23
    # perna de trás e perna da frente (grevas de pedra) com hera
    P.append(Parte(capsula(cx - 3, 34 + dy, cx - 4, 44, 2.6), PEDRA, z=0))
    P.append(Parte(elipse(cx - 3.5, 45, 3.2, 1.6), PEDRA, z=0.1))
    P.append(Parte(capsula(cx + 3, 34 + dy, cx + 4, 44, 2.8), PEDRA_CLARA, z=2.5, volume='cilindro_v'))
    P.append(Parte(elipse(cx + 5, 45, 3.6, 1.7), PEDRA_CLARA, z=2.6))
    px(P, [(cx + 4, 37 + dy), (cx + 3, 38 + dy), (cx + 3, 39 + dy), (cx + 4, 40 + dy), (cx + 5, 41 + dy), (cx + 4, 42 + dy)], '#239063', 2.7)
    px(P, [(cx + 5, 38 + dy), (cx + 2, 41 + dy)], '#91db69', 2.71)
    # escudo no braço de trás (terracota, com uma folha gravada e musgo)
    esc = poligono([(cx - 15, 20 + dy), (cx - 5, 20 + dy), (cx - 5, 30 + dy), (cx - 10, 37 + dy), (cx - 15, 30 + dy)])
    P.append(Parte(esc, COBRE, z=1, volume='cilindro_v'))
    borda = {p for p in esc if any((p[0] + a, p[1] + b) not in esc for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))}
    px(P, borda, '#9e4539', 1.05)
    px(P, [(cx - 10, y) for y in range(23 + dy, 33 + dy)], '#6e2727', 1.1)                                   # a nervura da folha
    px(P, [(cx - 11, 25 + dy), (cx - 12, 24 + dy), (cx - 9, 26 + dy), (cx - 8, 25 + dy), (cx - 11, 28 + dy), (cx - 12, 27 + dy),
           (cx - 9, 29 + dy), (cx - 8, 28 + dy)], '#6e2727', 1.1)
    px(P, [(cx - 14, 31 + dy), (cx - 13, 33 + dy), (cx - 12, 34 + dy)], '#3e3546', 1.1)                     # racha
    m = tufo(cx - 13, 21 + dy, 3.0, 4, ry=1.8)
    P.append(Parte(m, FOLHA, z=1.2))
    # tronco: peitoral de pedra, cinto e saiote
    P.append(Parte(poligono([(cx - 6, 30 + dy), (cx + 6, 30 + dy), (cx + 7, 36 + dy), (cx - 7, 36 + dy)]), PEDRA, z=1.8))
    peito = elipse(cx, 25 + dy, 7, 7)
    P.append(Parte(peito, PEDRA_CLARA, z=2))
    px(P, [(cx + 1, 21 + dy), (cx + 2, 22 + dy), (cx + 2, 23 + dy), (cx + 3, 24 + dy)], '#3e3546', 2.1)     # racha
    P.append(Parte(capsula(cx - 6, 31 + dy, cx + 6, 31 + dy, 1.2), ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], z=2.2, volume='cilindro_h'))
    px(P, [(cx + 1, 31 + dy)], '#c7dcd0', 2.3)
    # cabeça: elmo com viseira de onde sai luz verde, pluma partida
    hx, hy = cx + 1, 13 + dy
    P.append(Parte(capsula(hx - 2, hy - 6, hx - 4, hy - 9, 1.2), PEDRA, z=2.9))
    elmo = elipse(hx, hy, 5.6, 6.2)
    P.append(Parte(elmo, PEDRA_CLARA, z=3))
    P.append(Parte(capsula(hx - 5, hy - 1, hx + 6, hy - 1, 1.0), PEDRA, z=3.1, volume='cilindro_h'))       # aba da viseira
    luz = '#91db69' if t != 1 else '#cddf6c'
    px(P, [(x, hy + 1) for x in range(hx - 1, hx + 6)], OUT, 3.2)
    if t != 3:
        px(P, [(hx + 1, hy + 1), (hx + 2, hy + 1), (hx + 4, hy + 1), (hx + 5, hy + 1)], luz, 3.3)
        px(P, [(hx + 2, hy + 1)], BR, 3.4)
    px(P, [(hx + 3, y) for y in range(hy + 3, hy + 6)], '#3e3546', 3.2)                                        # respiros
    px(P, [(hx + 5, hy + 3), (hx + 5, hy + 5)], '#3e3546', 3.2)
    m = tufo(hx - 2, hy - 5, 3.6, 7, ry=2.0)
    P.append(Parte(m, FOLHA, z=3.5))
    folhagem(P, m, FOLHA, 3.5, 7, dens=7)
    # ombreira com musgo e braço da frente com a espada partida
    P.append(Parte(elipse(cx + 6, 20 + dy, 4.0, 3.4), PEDRA_CLARA, z=4))
    m = tufo(cx + 5, 18 + dy, 3.2, 3, ry=1.8)
    P.append(Parte(m, FOLHA, z=4.1))
    mao = (cx + 11, 28 + dy)
    P.append(Parte(capsula(cx + 7, 22 + dy, cx + 9, 26 + dy, 2.0) | capsula(cx + 9, 26 + dy, *mao, 1.8), PEDRA_CLARA, z=4.2))
    # espada: punho, guarda e lâmina partida (ponta irregular)
    P.append(Parte(capsula(mao[0] - 2, mao[1] + 2, mao[0] + 1, mao[1] - 1, 0.8), ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], z=4.3))
    P.append(Parte(capsula(mao[0] - 1, mao[1] - 3, mao[0] + 3, mao[1] + 1, 0.9), OURO, z=4.4))
    lam = poligono([(mao[0] + 1, mao[1] - 2), (mao[0] + 3, mao[1]), (mao[0] + 10, mao[1] - 7), (mao[0] + 9, mao[1] - 10), (mao[0] + 7.5, mao[1] - 8.5)])
    P.append(Parte(lam, FERRO, z=4.5))
    px(P, [(mao[0] + 3 + i, mao[1] - 2 - i) for i in range(5)], '#ffffff', 4.6)
    px(P, [(mao[0] + 6, mao[1] - 3), (mao[0] + 7, mao[1] - 4)], '#625565', 4.6)                                # mossa
    P.append(Parte(elipse(mao[0], mao[1], 1.8, 1.8), PEDRA_CLARA, z=4.7))
    # pedrinha/pó a cair (é uma estátua velha)
    yy = 30 + t * 4
    px(P, [(cx - 6, yy), (cx - 5, yy)], '#9babb2', 5)
    return desenhar(P, 48, 48)


# =====================================================================================
# 16. Serpente da Névoa (64): serpente branca de água que sai do lago
def serpente_da_nevoa(t):
    P = []
    onda = t % 2
    cab_dx = [0, 1, 1, 0][t]
    cab_dy = [0, 0, 1, 1][t]
    # água: um anel de ondulação à volta de onde sai
    agua = elipse(24, 58, 20, 4.2)
    P.append(Parte(agua, AGUA, z=0, plano=True))
    for i, x in enumerate(range(7, 42, 4)):
        px(P, [(x + onda * 2, 57 + (i % 2)), (x + 1 + onda * 2, 57 + (i % 2))], '#8ff8e2', 0.1)
    px(P, [(x, 59) for x in range(14, 34) if (x + onda) % 3 == 0], '#0b5e65', 0.1)
    # corpo em S: uma corrente de círculos que encolhem até ao pescoço
    pts = []
    for i in range(22):
        f = i / 21.0
        x = 20 + 14 * math.sin(f * 2.6 - 0.4) * (1 - f * 0.3) + f * 8 + cab_dx * f * f
        y = 58 - f * 36 + cab_dy * f * f
        r = 5.6 - f * 2.0
        pts.append((x, y, r))
    corpo = set()
    for (x, y, r) in pts:
        corpo |= elipse(x, y, r, r)
    corpo = {p for p in corpo if p[1] <= 57}
    P.append(Parte(corpo, BRANCO_ESC, z=1, volume='cilindro_h'))
    # barriga de placas (do lado da frente) e escamas
    for (x, y, r) in pts[1:]:
        for k2 in range(int(r) - 1, int(r) + 1):
            p = (int(x + r - 1.5), int(y))
            if p in corpo:
                px(P, [p, (p[0] - 1, p[1])], '#8ff8e2' if int(y) % 3 else '#30e1b9', 1.1)
    esc = [(x, y) for (x, y) in corpo if (x * 2 + y * 3) % 7 == 0 and (x + y) % 2 == 0]
    px(P, esc, '#9babb2', 1.05)
    # barbatanas translúcidas ao longo das costas
    for i in range(4, 20, 4):
        x, y, r = pts[i]
        fin = poligono([(x - r + 0.5, y - 2), (x - r - 4, y - 3), (x - r + 0.5, y + 2)])
        P.append(Parte(fin, ASA, z=0.8))
    # cabeça comprida com crista, olho azul que brilha, presas e língua
    hx, hy, _ = pts[-1]
    hx, hy = hx + 2, hy - 2
    crista = poligono([(hx - 4, hy - 2), (hx - 9, hy - 9), (hx - 2, hy - 5), (hx - 3, hy - 11), (hx + 1, hy - 4)])
    P.append(Parte(crista, ASA, z=1.9))
    cab = elipse(hx, hy, 5.2, 4.4) | capsula(hx + 2, hy + 1, hx + 9, hy + 2, 2.6)
    P.append(Parte(cab, BRANCO_ESC, z=2))
    px(P, [(x, hy + 3) for x in range(int(hx) + 2, int(hx) + 11)], '#8ff8e2', 2.1)
    olho(P, hx + 1, hy - 2, '#30e1b9', z=3, tam=3, fechado=(t == 3))
    px(P, [(hx, hy - 3), (hx + 1, hy - 4), (hx + 2, hy - 4), (hx + 3, hy - 4)], '#484a77', 3.1)               # sobrolho
    px(P, [(hx + 9, hy + 1)], OUT, 3)                                                                         # narina
    px(P, [(x, hy + 4) for x in range(int(hx) + 3, int(hx) + 11)], OUT, 3)
    px(P, [(hx + 9, hy + 5), (hx + 6, hy + 5)], BR, 3.1)                                                       # presas
    if t == 1:
        px(P, [(hx + 11, hy + 4), (hx + 12, hy + 4), (hx + 13, hy + 3), (hx + 13, hy + 5)], '#e83b3b', 3.2)   # língua
    # bigodes de dragão (fios ciano a pender)
    for (bx, by, comp) in ((hx + 4, hy + 5, 6), (hx + 7, hy + 5, 4)):
        px(P, [(bx - j * 0.4 + (onda if j > 2 else 0), by + j) for j in range(comp)], '#30e1b9', 3.2)
    # névoa à volta (anda devagar)
    for i, (nx, ny) in enumerate(((6, 48), (40, 46), (10, 36), (44, 30), (4, 24), (36, 52))):
        x = nx + ((t + i) % 4) - 1
        px(P, [(x, ny), (x + 1, ny), (x + 2, ny), (x + 1, ny - 1)], '#c7dcd0' if i % 2 else '#8ff8e2', 4)
    # salpicos onde sai da água
    px(P, [(12 + onda, 54), (35 - onda, 53), (33, 55 - onda)], '#8ff8e2', 4)
    return desenhar(P, 64, 64)


# =====================================================================================
# 17. Larva Ancestral (64): verme gigante de madeira podre que sai do chão
def larva_ancestral(t):
    P = []
    sx = [0, 1, 1, 0][t]
    sy = [0, 0, 1, 1][t]
    # monte de terra com o buraco
    monte = elipse(28, 59, 22, 5)
    P.append(Parte(monte, TERRA, z=0))
    px(P, [p for p in monte if _h(*p, 4) % 9 == 0], '#4c3e24', 0.05)
    P.append(Parte(elipse(26, 58, 12, 2.6), ['#2e222f'] * 5, z=0.1, separar=False))
    for (rx2, ry2, r) in ((8, 60, 2.2), (47, 59, 2.6), (40, 62, 1.6)):
        P.append(Parte(elipse(rx2, ry2, r, r * 0.8), PEDRA_CLARA, z=0.2))
    # o corpo: segmentos de madeira podre do buraco até à cabeça
    segs = [(24, 54, 9), (26, 46, 8.6), (29, 39, 8.2), (33, 33, 7.8), (38, 28, 7.4)]
    for i, (x, y, r) in enumerate(segs):
        f = i / 4.0
        m = elipse(x + sx * f, y + sy * f, r, r * 0.85)
        if i == 0:
            m = {p for p in m if p[1] <= 58}
        P.append(Parte(m, CASCA, z=1 + i * 0.1, volume='cilindro_h'))
        # veios da madeira e musgo por cima
        veio = [(xx, yy) for (xx, yy) in m if int(yy + 1.8 * math.sin(xx * 0.5)) % 4 == 0 and (xx * 3 + yy) % 5 != 0]
        px(P, veio, '#45293f', 1.01 + i * 0.1)
        px(P, [(xx, yy) for (xx, yy) in m if (xx + yy) % 5 == 0 and xx < x + sx * f - 2 and yy < y + sy * f - 2], '#ab947a', 1.02 + i * 0.1)
        mm = {p for p in m if p[1] < y + sy * f - r * 0.45 and _h(*p, i) % 3 != 0}
        P.append(Parte(mm, MUSGO, z=1.03 + i * 0.1, separar=False))
    # cogumelos e uma racha com luz de ácido
    cogumelinho(P, int(22 + sx * 0.25), 39, 1.5)
    cogumelinho(P, int(19), 47, 1.2)
    px(P, [(30, 45), (31, 46), (31, 47), (32, 48)], '#91db69', 1.45)
    # cabeça: boca redonda com anéis de dentes, mandíbulas e olhos verdes
    hx, hy = 42 + sx, 25 + sy
    P.append(Parte(elipse(hx, hy, 8.4, 8), CASCA, z=2))
    pintas(P, elipse(hx, hy, 8.4, 8), '#45293f', 2.01, sem=3, dens=7)
    boca = elipse(hx + 4, hy + 1, 4.2, 5)
    P.append(Parte(boca, ['#2e222f'] * 5, z=2.2, separar=False))
    P.append(Parte(elipse(hx + 4.5, hy + 1.5, 2.2, 2.8), ACIDO, z=2.3, separar=False))
    for (dx2, dy2) in ((1, -3), (3, -4), (5, -4), (7, -2), (7, 2), (6, 5), (3, 5), (1, 3)):
        px(P, [(hx + dx2, hy + 1 + dy2 * 0.8)], '#c7dcd0', 2.4)
    for s2 in (-1, 1):
        mand = capsula(hx + 6, hy + 1 + s2 * 5, hx + 10, hy + 1 + s2 * 3.5, 1.1) | capsula(hx + 10, hy + 1 + s2 * 3.5, hx + 11, hy + 1 + s2 * 1, 0.8)
        P.append(Parte(mand, MARFIM, z=2.5))
    for (ex, ey) in ((hx - 3, hy - 5), (hx, hy - 6), (hx - 4, hy - 2)):
        P.append(Parte(elipse(ex, ey, 1.3, 1.3), ACIDO, z=2.6))
        px(P, [(ex - 1, ey - 1)], BR, 2.7)
    # baba ácida a pingar
    g = [0, 1, 2, 3][t]
    gota(P, hx + 5, hy + 6, ACIDO, z=3, comp=1 + g)
    if t == 3:
        px(P, [(hx + 5, 56), (hx + 4, 57), (hx + 6, 57)], '#91db69', 3)
    # terra a cair dos segmentos
    yy = 40 + t * 4
    px(P, [(16, yy), (17, yy + 1)], '#694f62', 3)
    return desenhar(P, 64, 64)


# =====================================================================================
# lista e saída
# =====================================================================================

CRIATURAS = [
    # (id, pasta de origem, tamanho, função)
    ('slime_verde', 'monstros', 32, slime_verde),
    ('coelho_chifre', 'monstros', 32, coelho_chifre),
    ('lobo_cinzento', 'monstros', 32, lobo_cinzento),
    ('slime_rei', 'monstros', 64, slime_rei),
    ('lobo_cicatriz', 'monstros', 48, lobo_cicatriz),
    ('javali', 'monstros', 48, javali),
    ('cogumelo_andante', 'monstros', 32, cogumelo_andante),
    ('fada_travessa', 'monstros', 32, fada_travessa),
    ('abelha_gigante', 'monstros', 32, abelha_gigante),
    ('treant_jovem', 'monstros', 48, treant_jovem),
    ('coelho_chifre_anciao', 'guardioes', 48, coelho_chifre_anciao),
    ('coruja_sombria', 'guardioes', 48, coruja_sombria),
    ('lagostim_couracado', 'guardioes', 48, lagostim_couracado),
    ('rainha_dos_esporos', 'guardioes', 64, rainha_dos_esporos),
    ('abelha_rainha_melifera', 'guardioes', 48, abelha_rainha_melifera),
    ('guardiao_de_musgo', 'guardioes', 64, guardiao_de_musgo),
    ('cavaleiro_de_pedra_musgosa', 'guardioes', 48, cavaleiro_de_pedra_musgosa),
    ('serpente_da_nevoa', 'guardioes', 64, serpente_da_nevoa),
    ('larva_ancestral', 'bosses', 64, larva_ancestral),
    ('javali_rei', 'bosses', 64, javali_rei),
]


def verificar_paleta(img, nome):
    fora = set()
    for (r, g, b, a) in list(img.convert('RGBA').tobytes() and zip(*[iter(img.tobytes())] * 4)):
        if a and '#%02x%02x%02x' % (r, g, b) not in RESURRECT64:
            fora.add('#%02x%02x%02x' % (r, g, b))
    if fora:
        print('  !! cores fora da paleta em', nome, sorted(fora))
    return not fora


def tira(frames):
    w, h = frames[0].size
    img = Image.new('RGBA', (w * len(frames), h), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        img.paste(f, (i * w, 0))
    return img


def quadros(caminho):
    im = Image.open(caminho).convert('RGBA')
    h = im.height
    return [im.crop((i * h, 0, i * h + h, h)) for i in range(im.width // h)]


def gerar():
    os.makedirs(DESTINO, exist_ok=True)
    feitos = {}
    for (cid, pasta, W, f) in CRIATURAS:
        frames = [f(t) for t in range(4)]
        for fr in frames:
            assert fr.size == (W, W)
        img = tira(frames)
        verificar_paleta(img, cid)
        img.save(os.path.join(DESTINO, f'{cid}_parado_lado.png'))
        feitos[cid] = (pasta, W)
    # o Ent Ancião já foi redesenhado e aprovado: só se copia
    shutil.copyfile(os.path.join(ORIGEM, 'bosses', 'ent_anciao_parado_lado.png'), os.path.join(DESTINO, 'ent_anciao_parado_lado.png'))
    feitos['ent_anciao'] = ('bosses', 128)
    return feitos


FONTE = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FUNDO = (0x26, 0x2b, 0x3a)
ORDEM = ['monstros', 'guardioes', 'bosses']


def nomes_pt():
    import json
    nomes = {}
    for f in ('monstros.json', 'bosses.json'):
        for x in json.load(open(os.path.join(RAIZ, 'dados', f), encoding='utf-8')):
            if isinstance(x, dict) and 'id' in x and 'nome_pt' in x:
                nomes[x['id']] = x['nome_pt']
    try:   # a Larva Ancestral é o boss da masmorra escondida (dados/masmorras.json)
        m = json.load(open(os.path.join(RAIZ, 'dados', 'masmorras.json'), encoding='utf-8'))
        for k, v in m.get('bosses', {}).items():
            nomes.setdefault(k, v.get('nome_pt', k))
    except (OSError, ValueError, AttributeError):
        pass
    return nomes


def _paleta_exata(im):
    """Passa a imagem a 'P' sem mudar nenhuma cor (as cores da arte têm de ficar iguais às da paleta)."""
    cores = im.getcolors(256)
    if cores is None:   # mais de 256 cores (só o texto pode causar isto): reduz sem pontilhado
        return im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    lista = [c for _, c in cores]
    idx = {c: i for i, c in enumerate(lista)}
    out = Image.new('P', im.size)
    out.putpalette([v for c in lista for v in c] + [0] * (768 - 3 * len(lista)))
    out.putdata([idx[p] for p in im.getdata()])
    return out


def gifs(feitos):
    """comparar.gif (antes à esquerda, depois à direita) e depois.gif (só os novos), 8 quadros de 160 ms."""
    nomes = nomes_pt()
    fonte = ImageFont.truetype(FONTE, 12)
    titulo_f = ImageFont.truetype(FONTE, 16)
    lista = sorted(feitos.items(), key=lambda kv: (ORDEM.index(kv[1][0]), kv[1][1]))
    for modo in ('comparar', 'depois'):
        celulas = []
        for cid, (pasta, W) in lista:
            e = {32: 3, 48: 2, 64: 2}.get(W, 1)
            D = W * e
            depois = quadros(os.path.join(DESTINO, f'{cid}_parado_lado.png'))
            antes = quadros(os.path.join(ORIGEM, pasta, f'{cid}_parado_lado.png')) if modo == 'comparar' else None
            larg = (2 * D + 10 if antes else D) + 24
            larg = max(larg, int(fonte.getlength(nomes.get(cid, cid))) + 16)
            celulas.append((cid, W, e, D, antes, depois, larg, D + 26))
        # arrumar em linhas (largura máxima 1200)
        linhas, linha, x = [], [], 0
        for c in celulas:
            if linha and x + c[6] > 1200:
                linhas.append(linha)
                linha, x = [], 0
            linha.append(c)
            x += c[6]
        linhas.append(linha)
        larg_total = min(1200, max(sum(c[6] for c in l) for l in linhas))
        topo = 34
        alt_total = topo + sum(max(c[7] for c in l) + 10 for l in linhas)
        titulo = 'Região 1 (Floresta) — antes | depois' if modo == 'comparar' else 'Região 1 (Floresta) — depois'
        imgs = []
        for q in range(8):
            im = Image.new('RGB', (larg_total, alt_total), FUNDO)
            d = ImageDraw.Draw(im)
            d.fontmode = '1'   # texto sem suavizar: o GIF fica só com as cores da arte + fundo + texto
            d.text((12, 8), titulo, font=titulo_f, fill=(255, 255, 255))
            y = topo
            for l in linhas:
                h = max(c[7] for c in l)
                x = (larg_total - sum(c[6] for c in l)) // 2
                for (cid, W, e, D, antes, depois, lg, hc) in l:
                    xx = x + (lg - ((2 * D + 10) if antes else D)) // 2
                    yy = y + (h - 26 - D)
                    if antes:
                        a = antes[q % len(antes)].resize((D, D), Image.NEAREST)
                        im.paste(a, (xx, yy), a)
                        d.line([(xx + D + 4, yy + 4), (xx + D + 4, yy + D - 4)], fill=(70, 76, 98))
                        xx += D + 10
                    b = depois[q % len(depois)].resize((D, D), Image.NEAREST)
                    im.paste(b, (xx, yy), b)
                    nome = nomes.get(cid, cid)
                    d.text((x + (lg - fonte.getlength(nome)) / 2, y + h - 20), nome, font=fonte, fill=(220, 224, 236))
                    x += lg
                y += h + 10
            imgs.append(_paleta_exata(im))
        imgs[0].save(os.path.join(DESTINO, f'{modo}.gif'), save_all=True, append_images=imgs[1:], duration=160, loop=0)


if __name__ == '__main__':
    feitos = gerar()
    gifs(feitos)
    if len(sys.argv) > 2 and sys.argv[1] == 'rever':
        d = sys.argv[2]
        os.makedirs(d, exist_ok=True)
        for cid, (pasta, W) in feitos.items():
            antes = quadros(os.path.join(ORIGEM, pasta, f'{cid}_parado_lado.png'))
            depois = quadros(os.path.join(DESTINO, f'{cid}_parado_lado.png'))
            e = {32: 6, 48: 4, 64: 3, 96: 2, 128: 2}[W]
            n = 4
            im = Image.new('RGB', (W * e * (n + 1) + 20 + W * e, W * e * 2 + 10), (38, 43, 58))
            for i in range(n):
                a = antes[i % len(antes)].resize((W * e, W * e), Image.NEAREST)
                b = depois[i].resize((W * e, W * e), Image.NEAREST)
                im.paste(a, (i * W * e, 0), a)
                im.paste(b, (i * W * e, W * e + 10), b)
            # e o 1.º quadro do novo em tamanho real (1×) e ×2 ao lado
            b1 = depois[0]
            im.paste(b1, (n * W * e + 10, 0), b1)
            b2 = depois[0].resize((W * 2, W * 2), Image.NEAREST)
            im.paste(b2, (n * W * e + 10, W + 10), b2)
            im.save(os.path.join(d, f'rever_{cid}.png'))
