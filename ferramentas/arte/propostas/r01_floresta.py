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
ASA = ['#0b8a8f', '#30e1b9', '#8ff8e2', '#ffffff', '#ffffff']
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
# lista e saída
# =====================================================================================

CRIATURAS = [
    # (id, pasta de origem, tamanho, função)
    ('slime_verde', 'monstros', 32, slime_verde),
    ('coelho_chifre', 'monstros', 32, coelho_chifre),
    ('lobo_cinzento', 'monstros', 32, lobo_cinzento),
    ('slime_rei', 'monstros', 64, slime_rei),
    ('lobo_cicatriz', 'monstros', 48, lobo_cicatriz),
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
    return feitos


if __name__ == '__main__':
    feitos = gerar()
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
