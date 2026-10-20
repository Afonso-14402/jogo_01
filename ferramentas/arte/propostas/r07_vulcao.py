"""PROPOSTA (por aprovar): os monstros, guardiões e bosses da região 7 — Vulcão — redesenhados.

Não mexe no jogo: só grava em arte/propostas/monstros/r07_vulcao/
  - <id>_parado_lado.png  (4 quadros "parado", o mesmo tamanho de quadro que o desenho antigo)
  - comparar.gif          (antes | depois, a mexer)
  - depois.gif            (só os novos)

Desenhado com o motor (ferramentas/arte/motor.py), no estilo do Ent Ancião (ent_anciao.py): várias partes,
textura (fendas de lava, pintas, escamas, penas), olhos com brilho, pormenores próprios e luz de cima à esquerda.
Fichas: docs/regioes/r07_vulcao.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (secções 13, 14 e 15).

Correr (na raiz do repositório):  python3 ferramentas/arte/propostas/r07_vulcao.py  [--ver PASTA]
  --ver PASTA  grava também, em PASTA, uma imagem antes|depois ampliada de cada criatura (para verificar).
"""
import math
import os
import random
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

REGIAO = 'r07_vulcao'
ANTIGO = os.path.join(RAIZ, 'arte', 'regioes', REGIAO)
DESTINO = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', REGIAO)

OUT = '#2e222f'
BRANCO = '#ffffff'

# A paleta Resurrect 64 (para verificar que não fugimos dela).
PALETA = {'#' + c.lower() for c in """
2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334 e83b3b
fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73
91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6
8fd3ff 45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0
""".split()}

# ---------------- rampas desta região (escuro -> claro, só Resurrect 64)
ROCHA = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']        # basalto
ROCHA_ESC = ['#2e222f', '#2e222f', '#3e3546', '#625565', '#7f708a']
OBSID = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3']         # obsidiana (vidro negro-roxo)
OBSID_ESC = ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9']
LAVA = ['#9e4539', '#fb6b1d', '#f79617', '#f9c22b', '#fbff86']
BRASA = ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790']
DEMONIO = ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a']
DEMONIO_ESC = ['#2e222f', '#45293f', '#6e2727', '#b33831', '#ea4f36']
LARANJA = ['#9e4539', '#cd683d', '#fb6b1d', '#f79617', '#fbb954']
CINZA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
CINZA_ESC = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
CARVAO = ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565']
COURO = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
COURO_Q = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#966c6c']     # couro queimado
FERRO = ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
FERRO_ESC = ['#2e222f', '#3e3546', '#625565', '#9babb2', '#c7dcd0']
OURO = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
BRONZE = ['#4c3e24', '#9e4539', '#cd683d', '#e6904e', '#fbb954']
PELE = RAMPAS['pele']
CABELO_PRETO = ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565']
AZUL = RAMPAS['azul']
SISTEMA = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']       # a armadura escura do Sistema
VERMELHO = RAMPAS['vermelho']
ROXO = RAMPAS['roxo']
BRANCO_R = RAMPAS['branco']
MADEIRA = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']

FOGO_CORES = ['#ea4f36', '#fb6b1d', '#f9c22b', '#fbff86']               # fora -> dentro
FOGO_AZUL = ['#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff']


# ======================================================================================================
# ferramentas de desenho
# ======================================================================================================

def px(P, pts, cor, z):
    """Píxeis soltos de uma cor (marcas, brilhos, olhos)."""
    P.append(Parte({(int(x), int(y)) for x, y in pts}, None, z=z, separar=False, cor=cor))


def pintas(P, m, cor, z, semente, prob=0.08, filtro=None):
    """Pintas de uma cor espalhadas por dentro de uma máscara (sombras, escamas, cinza)."""
    rnd = random.Random(semente)
    pts = [p for p in sorted(m) if rnd.random() < prob and (filtro is None or filtro(*p))]
    px(P, pts, cor, z)
    return pts


def borda_de(m):
    return {p for p in m if any((p[0] + dx, p[1] + dy) not in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))}


def miolo(m, n=1):
    """A máscara sem as n camadas da borda."""
    for _ in range(n):
        m = m - borda_de(m)
    return m


def fendas(P, m, semente, z, n=3, comp=8, t=0, grossa=False):
    """Fendas de lava a correr dentro de uma máscara (rocha com lava por dentro).
    O meio da fenda brilha (amarelo) e pulsa com t; as pontas são laranja-escuras."""
    rnd = random.Random(semente)
    dentro = miolo(m, 1)
    if not dentro:
        return
    pontos = sorted(dentro)
    escuro, medio, claro = [], [], []
    for k in range(n):
        x, y = rnd.choice(pontos)
        dx, dy = rnd.choice(((1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1), (1, -1)))
        for i in range(comp):
            if (x, y) not in dentro:
                break
            q = i / max(1, comp - 1)
            if q < 0.15 or q > 0.8:
                escuro.append((x, y))
            elif (i + t) % 3 == 0:
                claro.append((x, y))
            else:
                medio.append((x, y))
            if grossa and (x + 1, y) in dentro and 0.2 < q < 0.7:
                medio.append((x + 1, y))
            r = rnd.random()
            if r < 0.35:   # a fenda vira
                dx, dy = rnd.choice(((1, 0), (0, 1), (-1, 0), (0, 1), (1, 1), (-1, 1)))
            x, y = x + dx, y + dy
    px(P, escuro, '#9e4539', z)
    px(P, medio, '#fb6b1d' if t % 2 == 0 else '#f79617', z + 0.001)
    px(P, claro, '#f9c22b' if t % 2 == 0 else '#fbff86', z + 0.002)


def lingua_fogo(cx, base, larg, alt, fase, torcer=1.0):
    """Máscara de uma língua de fogo em gota: fundo redondo e bico em cima, que ondula com a fase."""
    R = max(0.8, larg / 2)
    cy = base - R
    m = set()
    for y in range(int(base - alt) - 2, int(base) + 2):
        yc = y + .5
        if yc >= cy:
            d = R * R - (yc - cy) ** 2
            if d < 0:
                continue
            half, sx = math.sqrt(d), 0.0
        else:
            q = (cy - yc) / max(0.5, alt - R)
            if q > 1:
                continue
            half = R * (1 - q) ** 1.15
            sx = math.sin(q * 2.6 + fase) * q * 1.8 * torcer
        linha = [x for x in range(int(cx - R) - 4, int(cx + R) + 5) if abs(x + .5 - (cx + sx)) <= half]
        if not linha and half > 0.12:
            linha = [int(math.floor(cx + sx))]
        for x in linha:
            m.add((x, y))
    return m


def fogo(P, cx, base, larg, alt, t, z, semente=0, cores=FOGO_CORES, linguas=3, separar=True):
    """Uma chama em camadas (vermelho-laranja por fora, amarelo e quase branco por dentro), que tremula com t."""
    rnd = random.Random(semente)
    fase = t * math.pi / 2 + semente
    fora = lingua_fogo(cx, base, larg, alt * (1 + 0.08 * math.sin(fase)), fase)
    for i in range(linguas - 1):
        lado = -1 if i % 2 == 0 else 1
        ox = lado * larg * (0.26 + rnd.random() * 0.1)
        h = alt * (0.5 + 0.22 * math.sin(fase * 1.0 + i * 1.7 + 1))
        fora |= lingua_fogo(cx + ox, base - larg * 0.1, larg * 0.5, h, fase + i * 2.1 + 1, 1.3 * lado)
    P.append(Parte(fora, None, z=z, separar=separar, cor=cores[0]))
    camadas = ((0.74, 0.7), (0.5, 0.46), (0.28, 0.24))
    for k, (fl, fa) in enumerate(camadas):
        if k >= len(cores) - 1 or larg * fl < 1.2:
            break
        m = lingua_fogo(cx, base - 0.6 - k * 0.4, larg * fl, alt * fa, fase + 0.3 * (k + 1))
        P.append(Parte(m & fora, None, z=z + 0.01 * (k + 1), separar=False, cor=cores[k + 1]))
    return fora


def faiscas(P, x1, y1, x2, y2, t, z, n=4, semente=0, cores=('#f9c22b', '#fb6b1d', '#fbff86')):
    """Faúlhas a subir (cada quadro sobem 2 píxeis; no fim voltam a baixo)."""
    rnd = random.Random(semente)
    alt = max(1, y2 - y1)
    for i in range(n):
        x = rnd.randint(x1, x2)
        y0 = rnd.randint(0, alt)
        y = y2 - ((y2 - y1 - y0 + t * 2 + i) % alt)
        x += int(round(math.sin(t * 1.6 + i) * 1))
        px(P, [(x, y)], cores[(i + t) % len(cores)], z)


def cinzas(P, x1, y1, x2, y2, t, z, n=4, semente=0):
    """Flocos de cinza a cair devagar."""
    rnd = random.Random(semente)
    alt = max(1, y2 - y1)
    for i in range(n):
        x = rnd.randint(x1, x2) + (1 if (t + i) % 4 < 2 else 0)
        y = y1 + ((rnd.randint(0, alt) + t) % alt)
        px(P, [(x, y)], rnd.choice(('#9babb2', '#7f708a', '#c7dcd0')), z)


def olho(P, x, y, z, cor='#f9c22b', tam=1, pupila=None, fechado=False, contorno=True):
    """Olho de lado com brilho. tam 1 = 2×2, tam 2 = 3×3, tam 3 = 4×4. pupila: cor da pupila (fenda vertical)."""
    x, y = int(x), int(y)
    if fechado:
        px(P, [(x + i, y + tam) for i in range(tam + 1)], OUT, z + 0.02)
        return
    s = tam + 1
    caixa = [(x + i, y + j) for i in range(s) for j in range(s)]
    if contorno and tam >= 2:
        anel = [(x + i, y + j) for i in range(-1, s + 1) for j in range(-1, s + 1) if (x + i, y + j) not in caixa]
        anel = [p for p in anel if not (p[0] in (x - 1, x + s) and p[1] in (y - 1, y + s))]
        px(P, anel, OUT, z)
    if tam >= 2:
        caixa = [p for p in caixa if not ((p[0] in (x, x + s - 1)) and (p[1] in (y, y + s - 1)))] if tam >= 3 else caixa
    px(P, caixa, cor, z + 0.01)
    if pupila:
        cxp = x + s // 2
        px(P, [(cxp, y + j) for j in range(s)] if s >= 3 else [(x + 1, y + 1)], pupila, z + 0.015)
    px(P, [(x, y)] if tam < 3 else [(x + 1, y + 1)], BRANCO, z + 0.02)


def dentes(P, x1, x2, y, z, para_baixo=True, passo=2, cor='#c7dcd0'):
    pts = []
    for x in range(x1, x2 + 1, passo):
        pts.append((x, y))
        pts.append((x, y + (1 if para_baixo else -1)))
    px(P, pts, cor, z)


def escamas(P, m, z, cor_esc, cor_cla, semente=0, passo=3):
    """Escamas em meia-lua: um píxel escuro por baixo e um claro por cima, numa grelha desencontrada."""
    esc, cla = [], []
    for (x, y) in m:
        if y % passo == 0 and (x + (y // passo) * 2 + semente) % (passo + 1) == 0:
            if (x, y + 1) in m:
                esc.append((x, y + 1))
            cla.append((x, y))
    px(P, esc, cor_esc, z)
    px(P, cla, cor_cla, z + 0.001)


def veios(P, m, z, cor, freq=7, onda=2.0, sentido='v', luz=None, cx=None):
    """Riscos ondulados (casca, músculo, pedra estratificada)."""
    a, b = [], []
    for (x, y) in m:
        u = (x + onda * math.sin(y / 5.0 + x * 0.3)) if sentido == 'v' else (y + onda * math.sin(x / 5.0 + y * 0.3))
        if int(u) % freq == 0 and (x * 3 + y) % 9 != 0:
            a.append((x, y))
        elif luz and int(u) % freq == 1 and (cx is None or x < cx) and (x + y) % 3 == 0:
            b.append((x, y))
    px(P, a, cor, z)
    if luz:
        px(P, b, luz, z + 0.001)


def runa(P, x, y, z, cor, forma=0):
    formas = [
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (2, 0), (2, 2)],
        [(1, 0), (0, 1), (2, 1), (1, 2), (1, 3)],
        [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2), (1, 3)],
        [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (0, 3), (2, 3)],
    ]
    px(P, [(x + a, y + b) for a, b in formas[forma % len(formas)]], cor, z)


# ======================================================================================================
# 32 × 32 — monstros
# ======================================================================================================

def salamandra(t):
    """Lagarto de fogo: corpo laranja com pintas escuras, barriga amarela, crista de espinhos em brasa,
    cauda enrolada com a ponta a arder, olho de réptil (fenda), garras claras."""
    P = []
    resp = (0, 0, 1, 0)[t]
    sw = (0, 1, 0, -1)[t]
    BARRIGA = ['#9e4539', '#f79617', '#f9c22b', '#fbb954', '#fbff86']
    # patas do lado de lá
    P.append(Parte(capsula(10, 26, 8, 29, 1.3), DEMONIO_ESC, z=0))
    P.append(Parte(capsula(20, 26, 22, 29, 1.3), DEMONIO_ESC, z=0))
    # cauda enrolada para cima, com a ponta a arder
    P.append(Parte(capsula(10, 24, 5, 24, 2.5), LARANJA, z=1, volume='cilindro_h'))
    P.append(Parte(capsula(5, 24, 3, 20, 1.8), LARANJA, z=1.1))
    P.append(Parte(capsula(3, 20, 4 + sw, 16, 1.2), LARANJA, z=1.2))
    fogo(P, 4 + sw, 16, 4, 7, t, z=1.3, semente=3, linguas=2)
    px(P, [(6, 23), (4, 21)], '#9e4539', 1.25)
    # crista de espinhos em brasa (atrás do corpo)
    for i, x in enumerate((11, 14, 17, 20)):
        h = 4 + ((i + t) % 2)
        P.append(Parte(poligono([(x - 1.6, 22), (x + 1.6, 22), (x + 0.5, 21 - h)]), BRASA, z=1.5, plano=True))
        px(P, [(x, 22 - h)], '#f9c22b', 1.55)
    # corpo
    corpo = elipse(16, 24.5 - resp * 0.5, 8, 3.8 + resp * 0.3)
    P.append(Parte(corpo, LARANJA, z=2, volume='cilindro_h'))
    barriga = {p for p in corpo if p[1] >= 26}
    P.append(Parte(barriga, BARRIGA, z=2.1, separar=False, plano=True))
    px(P, [(10, 22), (11, 22), (11, 23), (14, 22), (15, 22), (18, 22), (19, 23), (19, 22), (13, 24), (17, 24)], '#9e4539', 2.2)
    px(P, [(12, 22), (16, 22), (20, 22)], '#fbb954', 2.25)
    # cabeça
    hy = 21 - resp * 0.5
    cab = elipse(24.5, hy, 3.8, 3.2) | capsula(25, hy + 1, 28.5, hy + 1.5, 1.8)
    P.append(Parte(cab, LARANJA, z=4, luz=0.1))
    queixo = {p for p in cab if p[1] >= int(hy) + 3}
    P.append(Parte(queixo, BARRIGA, z=4.1, separar=False, plano=True))
    y = int(hy)
    if t == 3:
        px(P, [(24, y), (25, y), (26, y)], OUT, 5)
    else:
        px(P, [(24, y - 1), (25, y - 1), (24, y), (25, y)], '#f9c22b', 5)
        px(P, [(25, y - 1), (25, y)], OUT, 5.1)
        px(P, [(24, y - 1)], BRANCO, 5.2)
    px(P, [(23, y - 2), (24, y - 2), (25, y - 2), (26, y - 2)], '#9e4539', 5)   # sobrolho
    px(P, [(29, y)], OUT, 5)                                                   # narina
    px(P, [(x, y + 2) for x in range(24, 30)], '#9e4539', 5)                   # boca
    if t == 2:
        px(P, [(30, y + 2), (31, y + 2), (31, y + 3)], '#e83b3b', 5)        # língua
    # patas do lado de cá, com garras
    P.append(Parte(elipse(12, 26, 2.4, 2), LARANJA, z=6))
    P.append(Parte(capsula(12, 27, 11, 29, 1.3), LARANJA, z=6.1))
    P.append(Parte(capsula(21, 26, 23, 29, 1.3), LARANJA, z=6))
    for x in (11, 23):
        px(P, [(x - 1, 30), (x + 1, 30), (x + 2, 30)], '#c7dcd0', 6.2)
    return desenhar(P, 32, 32)


def elemental_de_fogo(t):
    """Uma chama viva com cara: corpo em gota a arder, olhos de carvão com brilho, boca aberta,
    mãos de chama a flutuar, duas pedras de carvão a girar à volta e faúlhas a subir."""
    P = []
    dy = (0, -1, -1, 0)[t]
    ang = t * math.pi / 2
    pedras = []
    for i in range(2):
        a = ang + i * math.pi
        x = 16 + math.cos(a) * 12
        y = 22 + dy + math.sin(a) * 3
        pedras.append((x, y, math.sin(a) > 0))
    for (x, y, frente) in pedras:
        if not frente:
            P.append(Parte(elipse(x, y, 1.8, 1.5), CARVAO, z=0.2))
            px(P, [(int(x), int(y))], '#fb6b1d', 0.25)
    # o corpo
    fogo(P, 16, 29 + dy, 16, 26, t, z=1, semente=1, linguas=3,
         cores=['#ea4f36', '#fb6b1d', '#f79617', '#f9c22b'])
    # o coração (mais claro, no meio do peito)
    px(P, elipse(16, 24 + dy, 3.6, 3), '#fbff86', 1.5)
    # a cara
    ey = 15 + dy
    for ex in (15, 20):
        if t == 3:
            px(P, [(ex - 1, ey + 2), (ex, ey + 2), (ex + 1, ey + 2)], OUT, 3)
        else:
            px(P, [(ex, ey), (ex + 1, ey), (ex - 1, ey + 1), (ex, ey + 1), (ex + 1, ey + 1),
                   (ex - 1, ey + 2), (ex, ey + 2), (ex + 1, ey + 2), (ex, ey + 3)], OUT, 3)
            px(P, [(ex, ey + 1)], BRANCO, 3.1)
            px(P, [(ex + 1, ey + 2)], '#9e4539', 3.1)
    px(P, [(13, ey - 1), (14, ey - 2)], '#9e4539', 3)     # sobrancelhas zangadas
    px(P, [(22, ey - 1), (21, ey - 2)], '#9e4539', 3)
    boca = elipse(18, ey + 7, 2.6, 1.4 + (t % 2) * 0.6)
    px(P, boca, OUT, 3)
    px(P, [(17, ey + 7), (18, ey + 7), (19, ey + 8)], '#9e4539', 3.05)
    px(P, [(16, ey + 6), (20, ey + 6)], '#fbff86', 3.1)    # dentinhos de chama
    # mãos de chama a flutuar
    fogo(P, 4, 22 + dy, 5, 7, t + 1, z=4, semente=11, linguas=2)
    fogo(P, 28, 22 - dy, 5, 7, t + 3, z=4, semente=12, linguas=2)
    for (x, y, frente) in pedras:
        if frente:
            P.append(Parte(elipse(x, y, 1.8, 1.5), CARVAO, z=5))
            px(P, [(int(x), int(y))], '#fb6b1d', 5.1)
    faiscas(P, 9, 0, 23, 8, t, z=6, n=4, semente=2)
    return desenhar(P, 32, 32)


def diabrete(t):
    """Demoniozinho vermelho (≈18 px): chifres de osso, orelha bicuda, asas de morcego, sorriso de dentes,
    olhos amarelos, barriguinha, cauda de seta e um tridente maior do que ele."""
    P = []
    bob = (0, 0, -1, -1)[t]
    asa = (0, 1, 2, 1)[t]
    ASA = ['#2e222f', '#45293f', '#7a3045', '#a24b6f', '#cf657f']
    OSSO = ['#4c3e24', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff']
    y0 = bob
    # asa (atrás de tudo)
    sx, sy = 13, 18 + y0
    w = (7, 11 + asa * 2)
    pts = [(sx, sy), (w[0], w[1] + y0 - 6), (2, 9 + asa * 2 + y0), (4, 13 + asa + y0), (3, 17 + asa + y0),
           (6, 17 + asa + y0), (7, 21 + y0), (11, 21 + y0)]
    m = poligono(pts)
    P.append(Parte(m, ASA, z=0, plano=True))
    px(P, [(sx - i, sy - int(i * (sy - (w[1] + y0 - 6)) / (sx - w[0]))) for i in range(1, sx - w[0])], '#45293f', 0.1)
    # cauda com ponta de seta
    P.append(Parte(capsula(13, 25 + y0, 8, 27 + y0, 1.0), DEMONIO, z=0.5))
    P.append(Parte(capsula(8, 27 + y0, 5, 24 + y0 - (t % 2), 0.9), DEMONIO, z=0.5))
    ax, ay = 4, 22 + y0 - (t % 2)
    P.append(Parte({(ax, ay), (ax - 1, ay + 1), (ax, ay + 1), (ax + 1, ay + 1), (ax - 1, ay), (ax + 1, ay), (ax, ay - 1)},
                   DEMONIO, z=0.6, plano=True))
    # perna de trás e braço de trás
    P.append(Parte(capsula(14, 24, 13, 29, 1.2), DEMONIO_ESC, z=1))
    px(P, [(12, 30), (13, 30), (14, 30)], OUT, 1.1)
    P.append(Parte(capsula(14, 19 + y0, 12, 23 + y0, 1.0), DEMONIO_ESC, z=1))
    # corpo
    corpo = elipse(16, 21.5 + y0 * 0.5, 3.6, 4)
    P.append(Parte(corpo, DEMONIO, z=2))
    px(P, [(17, 21 + y0), (18, 22 + y0), (17, 23 + y0), (18, 23 + y0)], '#ea4f36', 2.1)
    # perna da frente
    P.append(Parte(capsula(17, 24, 18, 29, 1.3), DEMONIO, z=3))
    px(P, [(17, 30), (18, 30), (19, 30), (20, 30)], OUT, 3.1)
    # cabeça
    hx, hy = 17, 12 + y0
    # orelha bicuda (para trás)
    P.append(Parte(poligono([(hx - 4, hy - 1), (hx - 10, hy - 3), (hx - 4, hy + 2)]), DEMONIO, z=3.8))
    px(P, [(hx - 6, hy - 1), (hx - 5, hy - 1)], '#6e2727', 3.85)
    # chifres
    P.append(Parte(capsula(hx - 3, hy - 3, hx - 5, hy - 7, 1.2) | capsula(hx - 5, hy - 7, hx - 4, hy - 10, 0.8), OSSO, z=3.9))
    P.append(Parte(capsula(hx + 1, hy - 4, hx + 1, hy - 8, 1.2) | capsula(hx + 1, hy - 8, hx + 3, hy - 10, 0.8), OSSO, z=4.2))
    cab = elipse(hx, hy, 5.3, 4.8)
    P.append(Parte(cab, DEMONIO, z=4, luz=0.12))
    # olhos (dois, porque está de três quartos) com pupila e brilho
    for (ex, s) in ((hx, 0), (hx + 3, 1)):
        if t == 3:
            px(P, [(ex, hy), (ex + 1, hy)], OUT, 5)
            continue
        px(P, [(ex, hy - 2), (ex + 1, hy - 2), (ex, hy - 1), (ex + 1, hy - 1), (ex, hy), (ex + 1, hy)], '#f9c22b', 5)
        px(P, [(ex + 1, hy - 1), (ex + 1, hy)], OUT, 5.1)
        px(P, [(ex, hy - 2)], BRANCO, 5.2)
    px(P, [(hx - 1, hy - 3), (hx, hy - 4), (hx + 1, hy - 4), (hx + 3, hy - 4), (hx + 4, hy - 4)], '#6e2727', 5)
    # sorriso malandro com dentes
    px(P, [(hx - 1, hy + 2), (hx, hy + 3), (hx + 1, hy + 3), (hx + 2, hy + 3), (hx + 3, hy + 3), (hx + 4, hy + 2)], OUT, 5)
    px(P, [(hx, hy + 2), (hx + 2, hy + 2), (hx + 3, hy + 2)], BRANCO, 5.1)
    px(P, [(hx + 5, hy - 1)], '#6e2727', 5)                    # narina
    # braço da frente e tridente
    tx = 23
    P.append(Parte(capsula(tx, 4 + y0, tx, 29 + y0, 0.6), ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#ab947a'], z=6))
    dentes_t = {(tx, 1 + y0), (tx, 2 + y0), (tx, 3 + y0), (tx - 2, 2 + y0), (tx - 2, 3 + y0), (tx - 2, 4 + y0),
                (tx + 2, 2 + y0), (tx + 2, 3 + y0), (tx + 2, 4 + y0), (tx - 1, 5 + y0), (tx + 1, 5 + y0), (tx, 5 + y0),
                (tx - 2, 5 + y0), (tx + 2, 5 + y0)}
    P.append(Parte(dentes_t, FERRO, z=6.1, plano=True))
    if t in (0, 1):
        px(P, [(tx, 1 + y0 + t)], BRANCO, 6.2)
    P.append(Parte(capsula(18, 19 + y0, tx - 1, 20 + y0, 1.1), DEMONIO, z=6.3))
    P.append(Parte(elipse(tx, 20 + y0, 1.5, 1.5), DEMONIO, z=6.4))
    return desenhar(P, 32, 32)


def cao_infernal(t):
    """Cão de basalto com fendas de lava: crina e ponta da cauda em chamas, olho a arder, boca entreaberta
    a brilhar, presas, orelha em bico, patas com garras."""
    P = []
    resp = (0, 0, 1, 0)[t]
    y0 = resp
    # patas do lado de lá
    P.append(Parte(capsula(11, 22, 10, 26, 1.8) | capsula(10, 26, 11, 29, 1.3), ROCHA_ESC, z=0))
    P.append(Parte(capsula(23, 22, 24, 29, 1.4), ROCHA_ESC, z=0))
    # cauda com a ponta a arder
    P.append(Parte(capsula(7, 18 + y0, 4, 15 + y0, 1.4) | capsula(4, 15 + y0, 4, 12 + y0, 1.1), ROCHA, z=0.5))
    fogo(P, 4, 12 + y0, 4, 7, t, z=0.6, semente=5, linguas=2)
    # crina de chamas no pescoço (atrás da cabeça)
    for i, (x, b, h) in enumerate(((15, 17, 6), (18, 16, 8), (21, 15, 7))):
        fogo(P, x, b + y0 * 0.5, 5, h, t + i, z=1.5, semente=i + 11, linguas=1)
    # corpo
    corpo = elipse(14, 20.5 + y0 * 0.4, 8, 4.2) | elipse(20, 19.5, 4.5, 5)
    P.append(Parte(corpo, ROCHA, z=2))
    px(P, [(11, 21), (11, 22), (13, 21), (13, 22), (15, 21), (15, 22)], '#3e3546', 2.1)   # costelas
    fendas(P, corpo, 4, 2.2, n=2, comp=6, t=t)
    # cabeça
    hx, hy = 24, int(14 + y0 * 0.5)
    P.append(Parte(poligono([(hx - 3, hy - 2), (hx - 3, hy - 8), (hx + 1, hy - 3)]), ROCHA, z=3.9))   # orelha
    px(P, [(hx - 2, hy - 5), (hx - 2, hy - 4)], '#b33831', 3.95)
    cab = elipse(hx, hy, 4.2, 3.6) | capsula(hx + 1, hy + 1, hx + 5, hy + 1, 2.0)
    P.append(Parte(cab, ROCHA, z=4, luz=0.05))
    mand = capsula(hx, hy + 4, hx + 4, hy + 5, 1.1)
    P.append(Parte(mand, ROCHA_ESC, z=3.95))
    px(P, [(x, hy + 3) for x in range(hx + 1, hx + 6)], '#fb6b1d' if t % 2 == 0 else '#f79617', 4.5)   # boca a brilhar
    px(P, [(hx + 2, hy + 3)], '#f9c22b', 4.55)
    px(P, [(hx + 3, hy + 3), (hx + 5, hy + 3), (hx + 4, hy + 4)], BRANCO, 4.6)    # presas
    px(P, [(hx + 6, hy)], OUT, 4.5)                                              # nariz
    if t == 3:
        px(P, [(hx, hy - 1), (hx + 1, hy - 1), (hx + 2, hy - 1)], OUT, 5)
    else:
        px(P, [(hx, hy - 1), (hx + 1, hy - 1), (hx + 2, hy - 1)], '#f9c22b', 5)
        px(P, [(hx + 1, hy - 1)], BRANCO, 5.1)
        px(P, [(hx + 2, hy - 1)], '#fb6b1d', 5.1)
    px(P, [(hx - 1, hy - 3), (hx, hy - 2), (hx + 1, hy - 2), (hx + 2, hy - 2)], '#2e222f', 5)   # sobrolho
    fendas(P, cab, 9, 4.3, n=1, comp=3, t=t)
    # patas do lado de cá (a de trás dobrada)
    P.append(Parte(elipse(9, 21, 3.4, 3.6), ROCHA, z=5.5))
    P.append(Parte(capsula(8, 23, 7, 26, 1.6) | capsula(7, 26, 8, 29, 1.3), ROCHA, z=5.6))
    P.append(Parte(capsula(21, 22, 21, 29, 1.6), ROCHA, z=6))
    for x in (8, 21):
        px(P, [(x + 1, 30), (x + 2, 30)], '#c7dcd0', 6.1)
    px(P, [(21, 25), (7, 25)], '#fb6b1d', 6.1)
    return desenhar(P, 32, 32)


def morcego_de_cinza(t):
    """Morcego de cinza: orelhas grandes, olho de brasa, presas, asas com dedos de osso e as pontas a arder,
    a largar um rasto de cinza."""
    P = []
    voo = (0, 1, 2, 1)[t]
    cx, cy = 16, 16 + voo

    def asa(lado, z, rampa, osso):
        sh = (cx + lado * 2, cy)
        if t == 0:     # asas em cima
            pulso = (cx + lado * 7, cy - 8)
            dedos = [(cx + lado * 14, cy - 9), (cx + lado * 13, cy - 3), (cx + lado * 9, cy + 1)]
        elif t == 2:   # asas em baixo
            pulso = (cx + lado * 7, cy + 2)
            dedos = [(cx + lado * 13, cy + 8), (cx + lado * 9, cy + 9), (cx + lado * 5, cy + 7)]
        else:          # a meio
            pulso = (cx + lado * 8, cy - 4)
            dedos = [(cx + lado * 15, cy - 2), (cx + lado * 13, cy + 3), (cx + lado * 8, cy + 4)]
        pts = [sh, pulso, dedos[0]]
        for a, b in zip(dedos, dedos[1:]):
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            pts.append((mx + (sh[0] - mx) * 0.25, my + (sh[1] - my) * 0.25))   # recorte entre dedos
            pts.append(b)
        pts.append((cx, cy + 3))
        m = poligono(pts)
        P.append(Parte(m, rampa, z=z, plano=True))
        ossos = []
        for (a, b) in [(sh, pulso)] + [(pulso, d) for d in dedos]:
            n = int(max(abs(b[0] - a[0]), abs(b[1] - a[1]))) + 1
            for s in range(n):
                q = s / max(1, n - 1)
                ossos.append((int(a[0] + (b[0] - a[0]) * q), int(a[1] + (b[1] - a[1]) * q)))
        px(P, [p for p in ossos if p in m], osso, z + 0.01)
        px(P, [(int(pulso[0]), int(pulso[1]) - 1)], osso, z + 0.01)   # a garrinha do pulso
        px(P, [d for d in dedos[:1]], '#fb6b1d', z + 0.02)          # a ponta a arder
        return m
    # rasto de cinza (atrás)
    for i in range(6):
        x = 1 + i * 2 + ((t + i) % 2)
        y = cy + 4 + ((i * 2 + t) % 3) - 1
        px(P, [(x, y)], ('#625565', '#7f708a', '#9babb2')[(i + t) % 3], 0)
    asa(-1, 0.5, ['#2e222f', '#3e3546', '#3e3546', '#625565', '#7f708a'], '#7f708a')
    # corpo peludo
    corpo = elipse(cx, cy + 1, 3.8, 4.4)
    P.append(Parte(corpo, CINZA, z=2))
    pintas(P, corpo, '#625565', 2.1, 3, 0.18)
    px(P, [(cx - 1, cy + 6), (cx + 1, cy + 6), (cx - 1, cy + 7), (cx + 2, cy + 7)], '#3e3546', 1.9)   # pés
    # cabeça e orelhas
    hx, hy = cx + 2, cy - 4
    P.append(Parte(poligono([(hx - 3, hy - 1), (hx - 4, hy - 8), (hx, hy - 2)]), CINZA_ESC, z=2.9))
    P.append(Parte(poligono([(hx - 1, hy - 2), (hx + 2, hy - 9), (hx + 3, hy - 1)]), CINZA, z=3.1))
    px(P, [(hx + 1, hy - 5), (hx + 1, hy - 4)], '#cf657f', 3.2)
    cab = elipse(hx, hy, 3.6, 3.2) | capsula(hx, hy + 1, hx + 4, hy + 1, 1.5)
    P.append(Parte(cab, CINZA, z=3, luz=0.1))
    px(P, [(hx + 1, hy - 1), (hx + 2, hy - 1), (hx + 1, hy), (hx + 2, hy)], '#fb6b1d', 4)
    px(P, [(hx + 2, hy)], '#f9c22b', 4.05)
    px(P, [(hx + 1, hy - 1)], BRANCO, 4.1)
    px(P, [(hx + 5, hy + 1)], OUT, 4)
    px(P, [(hx + 2, hy + 3), (hx + 4, hy + 3)], BRANCO, 4.1)   # presas
    asa(1, 5, ['#2e222f', '#625565', '#625565', '#7f708a', '#9babb2'], '#c7dcd0')
    cinzas(P, 2, 2, 30, 30, t, z=6, n=3, semente=8)
    return desenhar(P, 32, 32)


def escorpiao_de_lava(t):
    """Escorpião com carapaça de rocha às placas, lava a brilhar entre as placas, cauda curvada por cima
    das costas com o ferrão incandescente, duas pinças de rocha e patas finas com joelho."""
    P = []
    cs = (0, 1, 1, 0)[t]
    pin = (0, 0, 1, 1)[t]
    lava = '#fb6b1d' if t % 2 == 0 else '#f79617'
    # patas do lado de lá
    for x in (10, 14, 18):
        P.append(Parte(capsula(x, 25, x + 1, 26, 0.7) | capsula(x + 1, 26, x - 1, 29, 0.7), ROCHA_ESC, z=0))
    # pinça do lado de lá
    P.append(Parte(capsula(21, 23, 23, 20, 1.1), ROCHA_ESC, z=0.3))
    P.append(Parte(elipse(25, 19, 2.2, 1.8) | capsula(25, 18, 28, 17 - pin, 0.9) | capsula(25, 20, 28, 20, 0.8), ROCHA_ESC, z=0.4))
    # cauda: segmentos em arco por cima das costas
    seg = [(8, 24), (5, 21), (4, 16), (6, 12 + cs), (10, 10 + cs), (14, 10 + cs)]
    for i in range(len(seg) - 1):
        r = 2.5 - i * 0.25
        P.append(Parte(capsula(*seg[i], *seg[i + 1], r), ROCHA, z=1 + i * 0.1))
        px(P, [(int(seg[i + 1][0]), int(seg[i + 1][1]))], lava, 1.05 + i * 0.1)
    # ferrão incandescente a apontar para a frente e para baixo
    fx, fy = seg[-1]
    bulbo = elipse(fx + 2, fy + 1, 2.2, 2)
    P.append(Parte(bulbo, LAVA, z=2))
    P.append(Parte(capsula(fx + 3, fy + 2, fx + 5, fy + 5, 0.7), ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86'], z=2.1))
    px(P, [(fx + 5, fy + 6)], '#fbff86' if t % 2 == 0 else '#f9c22b', 2.2)
    # corpo em placas
    corpo = elipse(14, 25, 7.5, 3.4)
    P.append(Parte(corpo, ROCHA, z=3, volume='cilindro_h'))
    for x in (9, 12, 15, 18):
        px(P, [(x, y) for y in range(22, 28) if (x, y) in corpo and y < 26], lava, 3.1)
    pintas(P, corpo, '#7f708a', 3.05, 6, 0.12, filtro=lambda x, y: y < 24)
    # cabeça
    hx, hy = 21, 25
    cab = elipse(hx, hy - 0.5, 3.4, 3)
    P.append(Parte(cab, ROCHA, z=4, luz=0.2))
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2)], '#e83b3b', 4.1)
    px(P, [(hx + 2, hy - 2)], '#fca790', 4.15)
    px(P, [(hx + 3, hy + 1), (hx + 3, hy + 2)], '#9e4539', 4.1)
    # pinça do lado de cá (grande)
    P.append(Parte(capsula(hx + 1, hy + 1, hx + 5, hy - 1, 1.3), ROCHA, z=6))
    garra = elipse(hx + 6.5, hy - 2, 2.8, 2.3)
    dedo1 = capsula(hx + 7, hy - 3, hx + 10, hy - 5 - pin, 1.1)
    dedo2 = capsula(hx + 7, hy - 1, hx + 10, hy, 1.0)
    P.append(Parte(garra | dedo1 | dedo2, ROCHA, z=6.1, luz=0.2))
    px(P, [(hx + 9, hy - 2 - pin // 2), (hx + 10, hy - 2)], '#fb6b1d', 6.12)
    px(P, [(hx + 10, hy - 4 - pin), (hx + 10, hy)], '#f79617', 6.2)
    fendas(P, garra, 2, 6.15, n=1, comp=3, t=t)
    # patas do lado de cá
    for x in (11, 15, 19):
        P.append(Parte(capsula(x, 26, x + 2, 27, 0.8) | capsula(x + 2, 27, x + 1, 30, 0.7), ROCHA, z=5))
    return desenhar(P, 32, 32)


def cultista_do_fogo(t):
    """Cultista de túnica vermelha com capuz bicudo e orla dourada, cara na sombra com olhos de brasa,
    cinto de corda, símbolo da chama no peito, bainha bordada e uma chama a flutuar entre as mãos."""
    P = []
    resp = (0, 0, 1, 0)[t]
    TUN = ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a']
    cx = 13
    sw = (0, 1, 0, -1)[t]
    # túnica
    tun = poligono([(cx - 4, 12 + resp), (cx + 4, 12 + resp), (cx + 7 + sw, 30), (cx - 7 + sw, 30)])
    P.append(Parte(tun, TUN, z=1, volume='cilindro_v'))
    px(P, [(x, 26 + (x % 3 == 0)) for x in range(cx - 5, cx + 6) if (x - cx) % 3 == 0], '#6e2727', 1.1)   # pregas
    px(P, [(x, 29) for x in range(cx - 6 + sw, cx + 7 + sw)], '#f9c22b', 1.2)        # bainha bordada
    px(P, [(x, 28) for x in range(cx - 6 + sw, cx + 7 + sw, 2)], '#f79617', 1.2)
    # cinto de corda com o nó
    px(P, [(x, 20 + resp) for x in range(cx - 5, cx + 6)], '#966c6c', 1.3)
    px(P, [(cx - 3, 21 + resp), (cx - 3, 22 + resp), (cx - 4, 23 + resp), (cx - 2, 23 + resp)], '#ab947a', 1.3)
    # símbolo da chama no peito
    px(P, [(cx + 1, 14 + resp), (cx, 15 + resp), (cx + 1, 15 + resp), (cx, 16 + resp), (cx + 1, 16 + resp), (cx + 2, 16 + resp),
           (cx + 1, 17 + resp)], '#f9c22b', 1.4)
    px(P, [(cx + 1, 16 + resp)], '#fb6b1d', 1.45)
    # capuz bicudo
    hx, hy = cx + 1, 8 + resp
    capuz = elipse(hx, hy, 5, 4.8) | poligono([(hx - 4, hy - 1), (hx - 7, hy - 8), (hx + 1, hy - 4)])
    P.append(Parte(capuz, TUN, z=3))
    cara = elipse(hx + 2.5, hy + 1, 2.6, 2.8)
    P.append(Parte(cara, None, z=3.1, separar=False, cor='#2e222f'))
    px(P, [(hx, hy - 3), (hx + 1, hy - 4), (hx + 2, hy - 4), (hx + 3, hy - 4), (hx + 4, hy - 3), (hx + 5, hy - 2)], '#f9c22b', 3.2)
    if t == 3:
        px(P, [(hx + 2, hy + 1), (hx + 4, hy + 1)], '#9e4539', 3.3)
    else:
        px(P, [(hx + 2, hy), (hx + 2, hy + 1), (hx + 4, hy), (hx + 4, hy + 1)], '#f9c22b', 3.3)
        px(P, [(hx + 2, hy), (hx + 4, hy)], BRANCO, 3.4)
    # manga e mão à frente; a chama a pairar
    P.append(Parte(capsula(cx, 15 + resp, cx + 5, 20 + resp, 2.0), TUN, z=4))
    px(P, [(cx + 6, 20 + resp), (cx + 7, 20 + resp), (cx + 7, 19 + resp)], '#cd683d', 4.1)
    px(P, [(cx + 5, 22 + resp), (cx + 6, 22 + resp)], '#cd683d', 4.1)
    fogo(P, cx + 10, 22 + resp - (t % 2), 6, 10, t, z=5, semente=4)
    faiscas(P, cx + 7, 3, cx + 14, 12, t, z=6, n=3, semente=1)
    return desenhar(P, 32, 32)


def _kai(t, boss):
    """Kai, Jogador nº 9 999: rapaz de cabelo preto espetado, casaco azul rasgado, espada curta, ténis gastos;
    no duelo tem os olhos a brilhar azul e a armadura escura que o Sistema lhe deu (mais armadura no boss)."""
    P = []
    resp = (0, 0, 1, 0)[t]
    cx = 14
    CALCA = ['#2e222f', '#323353', '#3e3546', '#484a77', '#484a77']
    # pernas e ténis gastos
    P.append(Parte(capsula(cx - 2, 22, cx - 3, 28, 1.5), CALCA, z=0))
    P.append(Parte(capsula(cx + 2, 22, cx + 2, 28, 1.6), CALCA, z=2))
    for (x, z) in ((cx - 4, 0.1), (cx + 1, 2.1)):
        P.append(Parte(retangulo(x, 29, x + 3, 30), ['#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0', '#c7dcd0'], z=z, plano=True))
        px(P, [(x + 1, 29), (x + 3, 30)], '#e83b3b', z + 0.01)
        px(P, [(x, 30)], '#7f708a', z + 0.01)
    # braço de trás
    P.append(Parte(capsula(cx - 2, 15 + resp, cx - 4, 21 + resp, 1.4), AZUL, z=0.5))
    # casaco azul (aberto, rasgado em baixo)
    tronco = retangulo(cx - 4, 13 + resp, cx + 4, 23, canto=1)
    P.append(Parte(tronco, AZUL, z=1, volume='cilindro_v'))
    px(P, [(cx - 4, 23), (cx - 2, 23), (cx - 3, 22), (cx + 4, 23)], OUT, 1.05)        # rasgões
    px(P, [(cx - 4, 17 + resp), (cx - 3, 18 + resp)], '#323353', 1.05)
    # peitoral escuro do Sistema
    peito = retangulo(cx - 1, 14 + resp, cx + 3, 21, canto=1)
    P.append(Parte(peito, SISTEMA, z=1.2, volume='cilindro_v'))
    px(P, [(cx + 1, 15 + resp), (cx + 1, 16 + resp), (cx, 17 + resp), (cx + 2, 17 + resp), (cx + 1, 18 + resp)],
       '#8fd3ff' if t % 2 == 0 else '#4d9be6', 1.3)
    if boss:
        P.append(Parte(elipse(cx - 1, 14 + resp, 3.4, 2.4), SISTEMA, z=1.4))   # ombreira
        px(P, [(cx - 2, 13 + resp), (cx - 1, 13 + resp)], '#8fd3ff', 1.45)
        P.append(Parte(retangulo(cx - 4, 21, cx + 4, 22), SISTEMA, z=1.3, plano=True))   # cinto de placas
        px(P, [(cx, 21), (cx + 1, 21)], '#8fd3ff', 1.35)
    # cabeça: cara à direita, cabelo preto espetado em cima e atrás
    hx, hy = cx + 1, 8 + resp
    cab = elipse(hx, hy, 4.8, 4.6)
    P.append(Parte(cab, ['#cd683d', '#e6904e', '#fca790', '#fdcbb0', '#fdcbb0'], z=3, plano=True))
    px(P, [(hx + 5, hy + 1)], '#e6904e', 3.05)          # nariz
    cabelo = {p for p in elipse(hx - 0.5, hy - 1.5, 5.1, 3.8) if p[1] <= hy - 2 or p[0] <= hx - 2}
    cabelo |= {p for p in elipse(hx - 2, hy + 0.5, 3.2, 4.2) if p[0] <= hx - 1}
    for (a, b) in ((-5, -7), (-1, -8), (3, -7), (-7, -3), (-6, 2)):
        cabelo |= poligono([(hx - 1.5, hy - 2.5), (hx + a, hy + b), (hx + 1.5, hy - 3.5)])
    cabelo |= poligono([(hx + 1, hy - 4), (hx + 6, hy - 3), (hx + 4, hy - 1.5), (hx + 3, hy - 2.5), (hx + 2, hy - 0.5)])   # franja
    P.append(Parte(cabelo, CABELO_PRETO, z=3.5))
    px(P, [(hx - 3, hy - 4), (hx - 2, hy - 5), (hx, hy - 5), (hx + 1, hy - 6)], '#625565', 3.55)   # brilho do cabelo
    px(P, [(hx - 1, hy + 1), (hx - 1, hy + 2)], '#e6904e', 3.6)       # orelha
    ex, ey = hx + 2, hy
    if t == 3:
        px(P, [(ex, ey + 1), (ex + 1, ey + 1)], OUT, 4)
    else:
        px(P, [(ex, ey), (ex + 1, ey), (ex, ey + 1), (ex + 1, ey + 1)], '#4d9be6', 4)
        px(P, [(ex + 1, ey + 1)], '#8fd3ff', 4.05)
        px(P, [(ex, ey)], BRANCO, 4.1)
        if boss:
            px(P, [(ex + 2, ey)], '#8fd3ff', 4.1)   # o brilho do Sistema a escapar do olho
    px(P, [(ex - 1, ey - 1), (ex, ey - 1), (ex + 1, ey - 2)], OUT, 4)   # sobrolho franzido
    px(P, [(hx + 2, hy + 3), (hx + 3, hy + 3)], '#9e4539', 4)         # boca cerrada
    # braço da frente com a espada curta
    mx, my = cx + 5, 19 + resp
    P.append(Parte(capsula(cx + 2, 15 + resp, mx, my, 1.5), AZUL, z=5))
    lam = capsula(mx + 1, my - 1, mx + 8, my - 6, 0.9)
    P.append(Parte(lam, FERRO, z=5.5))
    px(P, [(mx + 2 + t * 2, my - 2 - int(t * 1.4))], BRANCO, 5.6)
    P.append(Parte(capsula(mx - 1, my - 2, mx + 2, my + 1, 0.7), OURO, z=5.6))
    P.append(Parte(elipse(mx, my, 1.4, 1.4), PELE, z=5.7))
    if boss:
        # janelinha azul do Sistema a pairar atrás dele
        wy = 2 + (t % 2)
        P.append(Parte(retangulo(2, wy, 7, wy + 4), ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'], z=7, plano=True))
        px(P, [(3, wy + 1), (4, wy + 1), (5, wy + 1), (3, wy + 3), (4, wy + 3)], '#8fd3ff', 7.1)
        px(P, [(6, wy + 1)], '#e83b3b', 7.1)
    return desenhar(P, 32, 32)


def kai(t):
    return _kai(t, True)


def kai_duelo_da_historia(t):
    return _kai(t, False)


def golem_de_magma(t):
    """Golem de rocha negra com lava a correr por dentro: corcunda de pedra, cabeça enterrada nos ombros,
    olhos e boca de lava, núcleo a pulsar no peito, punhos enormes a pingar lava, chamas nos ombros."""
    P = []
    resp = (0, 0, 1, 1)[t]
    y0 = resp
    # perna do lado de lá e braço do lado de lá
    P.append(Parte(capsula(17, 36, 16, 43, 3.6), ROCHA_ESC, z=0))
    P.append(Parte(elipse(16, 44.5, 4.5, 2), ROCHA_ESC, z=0.1))
    P.append(Parte(capsula(13, 21 + y0, 8, 30 + y0, 3.6) | capsula(8, 30 + y0, 9, 36 + y0, 3.2), ROCHA_ESC, z=0.5))
    P.append(Parte(elipse(9, 38 + y0, 4, 3.6), ROCHA_ESC, z=0.6))
    px(P, [(7, 39 + y0), (9, 40 + y0), (11, 39 + y0)], '#fb6b1d', 0.7)
    # chamas nos ombros/costas (atrás)
    fogo(P, 14, 15 + y0, 6, 9, t, z=0.8, semente=2, linguas=2)
    fogo(P, 22, 12 + y0, 5, 8, t + 1, z=0.8, semente=5, linguas=2)
    # tronco com corcunda
    tronco = elipse(22, 28 + y0, 12, 10) | elipse(18, 19 + y0, 9, 6.5)
    P.append(Parte(tronco, ROCHA, z=2))
    # placas de rocha: fendas de lava entre elas
    fendas(P, tronco, 3, 2.2, n=6, comp=9, t=t, grossa=True)
    pintas(P, tronco, '#7f708a', 2.1, 5, 0.06, filtro=lambda x, y: x < 22 and y < 26 + y0)
    pintas(P, tronco, '#3e3546', 2.1, 9, 0.06)
    # núcleo a pulsar no peito
    nr = 3.4 + (t % 2) * 0.5
    P.append(Parte(elipse(28, 28 + y0, nr + 1.2, nr + 1.2), ROCHA_ESC, z=2.4))
    P.append(Parte(elipse(28, 28 + y0, nr, nr), LAVA, z=2.5))
    px(P, [(27, 27 + y0)], BRANCO, 2.6)
    # perna do lado de cá
    P.append(Parte(capsula(27, 36, 28, 43, 4), ROCHA, z=3))
    P.append(Parte(elipse(29, 44.5, 5.5, 2), ROCHA, z=3.1))
    fendas(P, capsula(27, 36, 28, 43, 4), 8, 3.2, n=1, comp=6, t=t)
    # cabeça enterrada entre os ombros
    hx, hy = 31, 14 + y0
    cab = elipse(hx, hy, 5.5, 4.8)
    P.append(Parte(elipse(hx - 1, hy + 2, 6.5, 5), ROCHA_ESC, z=3.9))
    P.append(Parte(cab, ROCHA, z=6, luz=0.15))
    px(P, [(hx - 1, hy - 2), (hx, hy - 2), (hx + 1, hy - 2), (hx + 2, hy - 2), (hx + 3, hy - 2), (hx + 4, hy - 2)], OUT, 6.1)   # testa
    for ex in (hx, hx + 3):
        if t == 3:
            px(P, [(ex, hy), (ex + 1, hy)], '#fb6b1d', 6.2)
        else:
            px(P, [(ex, hy - 1), (ex + 1, hy - 1), (ex, hy), (ex + 1, hy), (ex + 2, hy)], '#f9c22b', 6.2)
            px(P, [(ex, hy - 1)], BRANCO, 6.3)
    boca = [(x, hy + 3) for x in range(hx - 1, hx + 5)] + [(hx, hy + 4), (hx + 2, hy + 4), (hx + 4, hy + 4)]
    px(P, boca, '#fb6b1d', 6.2)
    px(P, [(hx + 1, hy + 3), (hx + 3, hy + 3)], '#f9c22b', 6.25)
    # braço do lado de cá com punho enorme
    om, co = (31, 24 + y0), (37, 31 + y0)
    P.append(Parte(capsula(*om, *co, 4), ROCHA, z=5))
    P.append(Parte(capsula(co[0], co[1], 38, 35 + y0, 3.6), ROCHA, z=5.1))
    punho = elipse(39, 38 + y0, 5.5, 5)
    P.append(Parte(punho, ROCHA, z=5.2, luz=0.08))
    px(P, [(41, 35 + y0), (42, 37 + y0), (42, 39 + y0), (41, 41 + y0)], '#3e3546', 5.3)   # dedos
    px(P, [(43, 36 + y0), (43, 38 + y0), (43, 40 + y0)], '#fb6b1d', 5.3)
    fendas(P, capsula(*om, *co, 4), 12, 5.15, n=1, comp=6, t=t)
    # gota de lava a pingar do punho
    gy = 43 + y0 + t
    if gy < 47:
        px(P, [(38, gy), (38, gy - 1)], '#f79617', 5.4)
        px(P, [(38, gy)], '#f9c22b', 5.45)
    faiscas(P, 10, 2, 28, 12, t, z=6, n=4, semente=3)
    return desenhar(P, 48, 48)


def fenix_de_cinza(t):
    """Pássaro de cinza e brasas: asas abertas para cima com penas de cinza a acabar em brasa,
    crista de chamas, bico dourado, olho em fogo, cauda longa com as pontas a arder; caem cinzas."""
    P = []
    asa = (0, 1, 2, 1)[t]
    y0 = (0, 0, 1, 1)[t]
    PENA = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
    PENA_C = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']

    def asa_m(ox, oy, z, rampa, borda):
        sh = (23 + ox, 27 + oy + y0)
        tips = [(4 + ox, 6 + oy + asa * 2), (3 + ox, 13 + oy + asa * 2), (5 + ox, 20 + oy + asa), (9 + ox, 26 + oy), (14 + ox, 30 + oy)]
        for i, tp in enumerate(tips):
            r = 2.2 - i * 0.15
            pena = capsula(sh[0] - 2 - i, sh[1] - 2, tp[0], tp[1], r)
            P.append(Parte(pena, rampa, z=z + i * 0.01))
            bx, by = sh[0] - 2 - i, sh[1] - 2
            ponta = capsula(bx + (tp[0] - bx) * 0.72, by + (tp[1] - by) * 0.72, tp[0], tp[1], r)
            P.append(Parte(ponta & pena, BRASA if z > 1 else DEMONIO, z=z + i * 0.01 + 0.005, separar=False))
            px(P, [(int(tp[0]), int(tp[1]))], borda[i % 2], z + 0.05)
        cob = poligono([(sh[0] + 1, sh[1] - 3), (14 + ox, 11 + oy + asa * 2), (10 + ox, 15 + oy + asa), (15 + ox, 24 + oy), (sh[0] - 1, sh[1] + 2)])
        P.append(Parte(cob, rampa, z=z + 0.1, plano=True))
        escamas(P, cob, z + 0.11, rampa[1], rampa[4], semente=1, passo=3)
        return cob
    # asa de lá
    asa_m(7, -4, 0, PENA, ('#ea4f36', '#fb6b1d'))
    # cauda: penas longas com as pontas a arder
    for i, (tx, ty) in enumerate(((3, 40), (6, 45), (2, 34))):
        sw = int(math.sin(t * math.pi / 2 + i) * 1.5)
        P.append(Parte(capsula(20, 35 + y0, tx, ty + sw, 1.6 - i * 0.2), PENA, z=0.5 + i * 0.01))
        fogo(P, tx + 1, ty + sw + 1, 3, 4, t + i, z=0.6, semente=20 + i, linguas=1)
    # patas com garras
    for (x, z) in ((24, 1), (28, 3)):
        P.append(Parte(capsula(x, 36, x - 1, 44, 1.0), ['#2e222f', '#45293f', '#694f62', '#966c6c', '#966c6c'], z=z))
        px(P, [(x - 3, 45), (x - 2, 45), (x, 45), (x + 1, 45), (x - 3, 46), (x + 1, 46)], '#f79617', z + 0.1)
    # corpo
    corpo = elipse(26, 31 + y0, 7, 7.5)
    P.append(Parte(corpo, PENA_C, z=2))
    peito = {p for p in corpo if p[0] >= 27}
    escamas(P, peito, 2.1, '#625565', '#c7dcd0', semente=2, passo=2)
    px(P, [(29, 34 + y0), (31, 32 + y0), (30, 36 + y0)], '#fb6b1d', 2.15)   # brasas no peito
    # pescoço e cabeça
    P.append(Parte(capsula(28, 27 + y0, 32, 20 + y0, 3.2), PENA_C, z=5.5))
    hx, hy = 33, 17 + y0
    # crista de chamas
    for i, (cx_, h) in enumerate(((28, 8), (30, 10), (32, 7))):
        fogo(P, cx_, hy - 1, 4, h, t + i, z=2.8, semente=30 + i, linguas=1)
    cab = elipse(hx, hy, 4.6, 4.2)
    P.append(Parte(cab, PENA_C, z=6, luz=0.15))
    bico = poligono([(hx + 3, hy - 1), (hx + 9, hy + 1), (hx + 6, hy + 2), (hx + 3, hy + 3)])
    P.append(Parte(bico, OURO, z=6.5, plano=True))
    px(P, [(hx + 4, hy + 2), (hx + 5, hy + 2)], '#9e4539', 6.6)
    if t == 3:
        px(P, [(hx, hy), (hx + 1, hy), (hx + 2, hy)], OUT, 7)
    else:
        olho(P, hx, hy - 1, 7, cor='#fb6b1d', tam=2)
        px(P, [(hx + 2, hy), (hx + 2, hy + 1)], '#f9c22b', 7.015)
    px(P, [(hx - 1, hy - 3), (hx, hy - 3), (hx + 1, hy - 3), (hx + 3, hy - 2)], '#ea4f36', 7.05)   # sobrancelha de brasa
    # asa de cá
    asa_m(0, 0, 5, PENA_C, ('#fb6b1d', '#f9c22b'))
    cinzas(P, 2, 2, 46, 46, t, z=7, n=6, semente=4)
    faiscas(P, 4, 2, 20, 16, t, z=7, n=4, semente=6)
    return desenhar(P, 48, 48)


def sapo_vulcao(t):
    """Sapo enorme de pele em brasa com verrugas, um vulcãozinho de rocha nas costas a fumegar e a pingar lava,
    olhos amarelos de pupila deitada, papo a inchar, patas com dedos largos."""
    P = []
    papo = (0, 1, 2, 1)[t]
    PELE_S = ['#45293f', '#6e2727', '#9e4539', '#cd683d', '#e6904e']
    PELE_E = ['#2e222f', '#45293f', '#6e2727', '#9e4539', '#cd683d']
    BARR = ['#9e4539', '#e6904e', '#fbb954', '#f9c22b', '#fbff86']
    # patas do lado de lá
    P.append(Parte(capsula(30, 38, 32, 44, 1.8), PELE_E, z=0))
    for dx in (-1, 2, 4):
        P.append(Parte(capsula(32, 44, 32 + dx, 46, 0.9), PELE_E, z=0.1))
    # fumo do vulcão (atrás)
    for i in range(3):
        k = (t + i) % 4
        r = 2 + k * 0.7
        P.append(Parte(elipse(17 + k + (i % 2), 9 - k * 2 - i, r, r * 0.8), ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'], z=0.2 + i * 0.01))
    # vulcão nas costas
    vul = poligono([(9, 29), (25, 29), (21, 13), (14, 13)])
    P.append(Parte(vul, ROCHA, z=1, volume='cilindro_v'))
    veios(P, vul, 1.05, '#3e3546', freq=4, onda=0.8, sentido='h')
    P.append(Parte(elipse(17.5, 13, 4, 1.6), LAVA, z=1.2))
    for (x, y1, y2) in ((15, 14, 18 + t % 2), (19, 14, 21 + (t + 1) % 3), (21, 15, 17)):
        px(P, [(x, y) for y in range(y1, y2)], '#fb6b1d', 1.3)
        px(P, [(x, y2)], '#f9c22b', 1.31)
    fogo(P, 17.5, 13, 5, 4 + t % 2, t, z=1.25, semente=7, linguas=2)
    # corpo
    corpo = elipse(22, 35, 14, 9.5)
    P.append(Parte(corpo, PELE_S, z=2, luz=-0.1))
    barriga = {p for p in corpo if p[1] >= 40}
    P.append(Parte(barriga, BARR, z=2.05, separar=False, plano=True))
    rnd = random.Random(3)
    for _ in range(9):   # verrugas
        x, y = rnd.randint(10, 30), rnd.randint(28, 38)
        if (x, y) in corpo:
            px(P, [(x, y), (x + 1, y)], '#e6904e', 2.1)
            px(P, [(x, y + 1), (x + 1, y + 1)], '#45293f', 2.1)
            if (x + y) % 3 == 0:
                px(P, [(x, y)], '#f79617', 2.11)
    fendas(P, {p for p in corpo if p[1] < 38}, 2, 2.15, n=2, comp=6, t=t)
    # pata de trás dobrada
    coxa = elipse(14, 39, 7, 5.5)
    P.append(Parte(coxa, PELE_S, z=3))
    pintas(P, coxa, '#6e2727', 3.05, 4, 0.1)
    pintas(P, coxa, '#e6904e', 3.06, 7, 0.05)
    P.append(Parte(capsula(10, 44, 20, 45, 1.6), PELE_S, z=3.1))
    for dx in (0, 3, 6):
        px(P, [(20 + dx // 2, 46), (21 + dx // 2, 46)], '#e6904e', 3.2)
    # cabeça
    cab = elipse(35, 31, 9, 6.8)
    P.append(Parte(cab, PELE_S, z=4, luz=0.08))
    # papo a inchar
    P.append(Parte(elipse(34, 37, 4.5 + papo * 0.6, 2.5 + papo * 0.5), BARR, z=4.1))
    # boca larga
    px(P, [(x, 34 - (1 if x > 40 else 0)) for x in range(28, 44)], '#6e2727', 4.5)
    px(P, [(27, 33)], '#6e2727', 4.5)
    px(P, [(42, 29), (43, 29)], OUT, 4.5)   # narina
    # olhos em cima da cabeça
    for (ex, ey, r) in ((33, 25, 3.6), (38.5, 25, 3.2)):
        P.append(Parte(elipse(ex, ey, r, r), PELE_S, z=4.6))
        px(P, elipse(ex + 0.3, ey + 0.3, r - 1.1, r - 1.1), '#f9c22b', 4.7)
        if t == 3:
            px(P, [(int(ex) - 2 + i, int(ey)) for i in range(5)], '#9e4539', 4.8)
        else:
            px(P, [(int(ex), int(ey)), (int(ex) + 1, int(ey)), (int(ex), int(ey) + 1), (int(ex) + 1, int(ey) + 1)], OUT, 4.8)
            px(P, [(int(ex) - 1, int(ey) - 1)], BRANCO, 4.85)
            px(P, [(int(ex) - 2, int(ey) + 1)], '#fbff86', 4.85)
    # pata da frente
    P.append(Parte(capsula(40, 36, 42, 44, 2.0), PELE_S, z=5))
    for dx in (-2, 1, 4):
        P.append(Parte(capsula(42, 44, 42 + dx, 46, 1.0), PELE_S, z=5.1))
    faiscas(P, 13, 0, 22, 8, t, z=6, n=3, semente=9)
    return desenhar(P, 48, 48)


def sumo_sacerdote_das_chamas(t):
    """O cultista principal: túnica carmesim comprida, capa escura, estola dourada com chamas bordadas,
    máscara dourada com rasgos de olhos a brilhar, coroa de pontas de ouro e um cajado com um braseiro a arder."""
    P = []
    resp = (0, 0, 1, 1)[t]
    sw = (0, 1, 0, -1)[t]
    TUN = ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a']
    CAPA = ['#2e222f', '#45293f', '#7a3045', '#9e4539', '#b33831']
    cx = 21
    y0 = resp
    # capa atrás
    capa = poligono([(cx - 5, 15 + y0), (cx + 4, 15 + y0), (cx - 1 + sw, 46), (cx - 13 + sw, 46)])
    P.append(Parte(capa, CAPA, z=0, volume='cilindro_v'))
    veios(P, capa, 0.05, '#45293f', freq=4, onda=0.6)
    # braço de trás
    P.append(Parte(capsula(cx - 3, 18 + y0, cx - 7, 28 + y0, 2.4), TUN, z=0.5))
    # túnica
    tun = poligono([(cx - 6, 16 + y0), (cx + 6, 16 + y0), (cx + 10 + sw, 46), (cx - 9 + sw, 46)])
    P.append(Parte(tun, TUN, z=1, volume='cilindro_v'))
    px(P, [(x, 45) for x in range(cx - 8 + sw, cx + 10 + sw)], '#f9c22b', 1.1)
    px(P, [(x, 44) for x in range(cx - 8 + sw, cx + 10 + sw, 2)], '#f79617', 1.1)
    px(P, [(x, 43) for x in range(cx - 7 + sw, cx + 9 + sw, 4)], '#f79617', 1.1)
    # estola dourada com chamas bordadas
    est = poligono([(cx + 1, 17 + y0), (cx + 5, 17 + y0), (cx + 6 + sw, 43), (cx + 2 + sw, 43)])
    P.append(Parte(est, OURO, z=1.2, plano=True))
    for k, yy in enumerate((22, 29, 36)):
        x = cx + 3 + (sw if yy > 30 else 0)
        px(P, [(x, yy + y0), (x, yy + 1 + y0), (x + 1, yy + 1 + y0), (x - 1, yy + 2 + y0), (x, yy + 2 + y0), (x + 1, yy + 2 + y0)], '#ea4f36', 1.3)
    # cinto
    P.append(Parte(retangulo(cx - 6, 26 + y0, cx + 7, 27 + y0), BRONZE, z=1.4, plano=True))
    P.append(Parte(elipse(cx + 3, 26.5 + y0, 1.8, 1.8), OURO, z=1.5))
    px(P, [(cx + 3, 26 + y0)], '#e83b3b', 1.55)
    # ombros
    P.append(Parte(capsula(cx - 2, 16 + y0, cx + 5, 16 + y0, 1.6), OURO, z=2.6))
    px(P, [(cx + 1, 17 + y0)], '#e83b3b', 2.65)
    # cabeça: capuz escuro, máscara dourada, coroa de pontas
    hx, hy = cx + 1, 11 + y0
    P.append(Parte(elipse(hx - 1, hy, 4.6, 4.8), CAPA, z=2))
    coroa = retangulo(hx - 4, hy - 5, hx + 3, hy - 4)
    for i, x in enumerate(range(hx - 4, hx + 4, 2)):
        h = 4 if i % 2 else 6
        coroa |= poligono([(x - 0.2, hy - 4), (x + 1.8, hy - 4), (x + 0.8, hy - 4 - h)])
    P.append(Parte(coroa, OURO, z=2.2, plano=True))
    px(P, [(hx - 1, hy - 5), (hx + 2, hy - 5)], '#e83b3b', 2.25)   # rubis
    mascara = elipse(hx + 1.5, hy + 0.5, 3.2, 3.8)
    P.append(Parte(mascara, ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'], z=2.4, plano=True))
    if t == 3:
        px(P, [(hx + 1, hy), (hx + 2, hy), (hx + 4, hy)], '#9e4539', 2.5)
    else:
        px(P, [(hx + 1, hy - 1), (hx + 2, hy), (hx + 1, hy), (hx + 4, hy - 1), (hx + 4, hy)], OUT, 2.5)
        px(P, [(hx + 2, hy), (hx + 4, hy)], '#fb6b1d', 2.55)
        px(P, [(hx + 1, hy - 1)], '#fbff86', 2.56)
    px(P, [(hx + 2, hy + 3), (hx + 3, hy + 3)], '#9e4539', 2.5)   # boca da máscara
    px(P, [(hx + 2, hy + 1), (hx + 2, hy + 2)], '#f79617', 2.5)   # nariz
    # braço da frente e cajado com braseiro
    sx = 34
    P.append(Parte(capsula(sx, 9 + y0, sx, 46, 0.8), MADEIRA, z=3))
    P.append(Parte(capsula(cx + 3, 18 + y0, cx + 8, 25 + y0, 2.6), TUN, z=3.5))
    P.append(Parte(capsula(cx + 8, 25 + y0, sx - 1, 23 + y0, 2.2), TUN, z=3.6))
    px(P, [(cx + 9, 26 + y0), (cx + 10, 26 + y0), (cx + 11, 25 + y0)], '#f9c22b', 3.65)   # punho bordado
    P.append(Parte(elipse(sx, 23 + y0, 1.8, 1.8), ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0'], z=3.7))
    bras = poligono([(sx - 4, 7 + y0), (sx + 4, 7 + y0), (sx + 2, 11 + y0), (sx - 2, 11 + y0)])
    P.append(Parte(bras, OURO, z=3.8, volume='cilindro_h'))
    px(P, [(sx - 2, 9 + y0), (sx, 9 + y0), (sx + 2, 9 + y0)], '#9e4539', 3.85)
    fogo(P, sx, 7 + y0, 7, 10, t, z=3.7, semente=4)
    faiscas(P, sx - 6, 0, sx + 6, 6, t, z=6, n=4, semente=5)
    return desenhar(P, 48, 48)


def golem_forjado_n7(t):
    """Golem de obsidiana polida: reflexos de vidro em diagonal, um "7" gravado no peito a brilhar de magma,
    visor com olho de luz, ombreiras, antebraços-foguete com bocais, e o núcleo de magma a espreitar nas costas."""
    P = []
    resp = (0, 0, 1, 1)[t]
    y0 = resp
    BOCAL = ['#2e222f', '#3e3546', '#625565', '#9babb2', '#c7dcd0']
    # núcleo de magma nas costas (o ponto fraco)
    P.append(Parte(elipse(17, 31 + y0, 4.5, 6), OBSID_ESC, z=0))
    P.append(Parte(elipse(16, 31 + y0, 3, 4.5), LAVA, z=0.1))
    px(P, [(15, 29 + y0)], BRANCO, 0.15)
    faiscas(P, 10, 18, 18, 30, t, z=0.2, n=3, semente=7)
    # perna e braço do lado de lá
    P.append(Parte(capsula(26, 44, 25, 56, 5), OBSID_ESC, z=0.5, volume='cilindro_v'))
    P.append(Parte(retangulo(19, 56, 31, 61, canto=1), OBSID_ESC, z=0.6, plano=True))
    P.append(Parte(capsula(19, 24 + y0, 14, 34 + y0, 4), OBSID_ESC, z=0.7))
    P.append(Parte(capsula(14, 34 + y0, 13, 44 + y0, 5), OBSID_ESC, z=0.8, volume='cilindro_v'))
    P.append(Parte(retangulo(9, 44 + y0, 17, 50 + y0, canto=1), OBSID_ESC, z=0.9, plano=True))
    # tronco
    tronco = poligono([(18, 20 + y0), (46, 20 + y0), (42, 45), (22, 45)])
    P.append(Parte(tronco, OBSID, z=2, volume='cilindro_v'))
    # reflexos de vidro em diagonal
    for k, x0 in enumerate((22, 27)):
        px(P, [(x0 + i, 23 + y0 + i) for i in range(8 - k * 3) if (x0 + i, 23 + y0 + i) in tronco], '#eaaded' if k == 0 else '#a884f3', 2.2)
    # juntas das placas
    px(P, [(x, 33 + y0) for x in range(20, 45) if (x, 33 + y0) in tronco and x % 5 != 0], '#2e222f', 2.1)
    px(P, [(32, y) for y in range(21 + y0, 33 + y0)], '#45293f', 2.1)
    # o "7" gravado no peito, a brilhar
    sete = [(34 + i, 24 + y0) for i in range(7)] + [(34 + i, 25 + y0) for i in range(7)]
    sete += [(40 - i // 3, 26 + y0 + i) for i in range(9)] + [(39 - i // 3, 26 + y0 + i) for i in range(9)]
    sete = sorted(set(sete))
    px(P, [(x, y + 1) for (x, y) in sete], '#2e222f', 2.3)
    px(P, sete, '#fb6b1d' if t % 2 == 0 else '#f79617', 2.31)
    px(P, sete[::3], '#f9c22b', 2.32)
    # cinto de placas
    P.append(Parte(retangulo(22, 40, 42, 44), OBSID_ESC, z=2.4, plano=True))
    for x in (25, 30, 35, 40):
        px(P, [(x, 41), (x, 42)], '#905ea9', 2.45)
    # perna do lado de cá
    P.append(Parte(capsula(37, 44, 38, 56, 5.5), OBSID, z=3, volume='cilindro_v'))
    P.append(Parte(retangulo(32, 56, 46, 61, canto=1), OBSID, z=3.1, plano=True))
    px(P, [(34, 58), (37, 58), (40, 58), (43, 58)], '#a884f3', 3.2)
    px(P, [(36 + i, 47 + i) for i in range(4)], '#a884f3', 3.15)
    # cabeça com visor
    cab = retangulo(29, 8 + y0, 41, 19 + y0, canto=1)
    P.append(Parte(cab, OBSID, z=4, volume='cilindro_v', luz=0.1))
    P.append(Parte(retangulo(30, 13 + y0, 41, 15 + y0), None, z=4.1, separar=False, cor=OUT))
    if t == 3:
        px(P, [(x, 14 + y0) for x in range(33, 41)], '#0b8a8f', 4.2)
    else:
        px(P, [(x, 14 + y0) for x in range(32, 41)], '#30e1b9', 4.2)
        px(P, [(37, 14 + y0), (38, 14 + y0), (39, 14 + y0)], '#8ff8e2', 4.25)
        px(P, [(38, 13 + y0)], BRANCO, 4.3)
    px(P, [(31, 10 + y0), (32, 10 + y0), (33, 10 + y0), (31, 11 + y0)], '#eaaded', 4.3)
    px(P, [(35, 6 + y0), (35, 7 + y0), (36, 7 + y0)], '#905ea9', 3.9)   # antena
    P.append(Parte(retangulo(34, 7 + y0, 36, 8 + y0), OBSID_ESC, z=3.9, plano=True))
    # ombreira e braço-foguete do lado de cá
    P.append(Parte(elipse(46, 23 + y0, 6, 5), OBSID, z=5, luz=0.1))
    px(P, [(43, 21 + y0), (44, 20 + y0), (45, 20 + y0)], '#eaaded', 5.1)
    P.append(Parte(capsula(47, 26 + y0, 50, 34 + y0, 3.6), OBSID, z=5.2))
    ante = capsula(50, 34 + y0, 51, 44 + y0, 5)
    P.append(Parte(ante, OBSID, z=5.3, volume='cilindro_v'))
    for y in (37, 41):
        P.append(Parte(retangulo(46, y + y0, 56, y + 1 + y0), BRONZE, z=5.35, plano=True))
    # bocais do foguete (atrás do cotovelo) com chama pequenina
    P.append(Parte(retangulo(44, 34 + y0, 46, 37 + y0), BOCAL, z=5.25, plano=True))
    fogo(P, 43, 37 + y0, 3, 4 + t % 2, t, z=5.1, semente=3, linguas=1, cores=FOGO_AZUL)
    punho = retangulo(46, 45 + y0, 56, 52 + y0, canto=1)
    P.append(Parte(punho, OBSID, z=5.4, plano=True))
    px(P, [(x, 48 + y0) for x in range(47, 56, 3)], '#2e222f', 5.45)
    return desenhar(P, 64, 64)


def golem_portao_de_obsidiana(t):
    """Um portão de castelo vivo, de obsidiana: ameias em cima, pedra-chave com cara e olhos de magma,
    blocos de alvenaria, portas de ferro com uma fresta de lava, quatro runas a pulsar e punhos de pedra."""
    P = []
    resp = (0, 0, 1, 1)[t]
    y0 = resp
    # braço de lá (atrás)
    P.append(Parte(capsula(14, 26 + y0, 8, 38 + y0, 4.2), OBSID_ESC, z=0))
    P.append(Parte(retangulo(3, 38 + y0, 13, 47 + y0, canto=1), OBSID_ESC, z=0.1, plano=True))
    # pés-pilar
    P.append(Parte(retangulo(13, 54, 25, 61, canto=1), OBSID_ESC, z=0.5, plano=True))
    P.append(Parte(retangulo(39, 54, 51, 61, canto=1), OBSID, z=0.6, plano=True))
    # o corpo-portão com ameias
    corpo = retangulo(12, 14 + y0, 52, 56)
    for x in range(12, 53, 8):
        corpo |= retangulo(x, 9 + y0, x + 4, 14 + y0)
    P.append(Parte(corpo, OBSID, z=1, volume='cilindro_v'))
    # alvenaria: fiadas e juntas desencontradas, reflexos
    jun = []
    for y in range(20 + y0, 56, 6):
        jun += [(x, y) for x in range(13, 52)]
        off = 0 if ((y - y0) // 6) % 2 else 5
        for x in range(13 + off, 52, 10):
            jun += [(x, yy) for yy in range(y + 1, min(y + 6, 56))]
    px(P, [p for p in jun if p in corpo], '#2e222f', 1.1)
    px(P, [(x, y) for (x, y) in corpo if (x - 13) % 10 == 1 and (y - y0) % 6 == 3 and x < 32], '#a884f3', 1.15)
    # arco da porta
    arco = retangulo(24, 34 + y0, 40, 56) | elipse(32, 34 + y0, 8, 6)
    P.append(Parte(arco, None, z=2, cor='#2e222f'))
    portas = retangulo(25, 35 + y0, 39, 56) | elipse(32, 35 + y0, 7, 5)
    portas = {p for p in portas if p in arco}
    P.append(Parte(portas, MADEIRA, z=2.1, plano=True, separar=False))
    veios(P, portas, 2.15, '#4c3e24', freq=3, onda=0.3)
    for y in (39, 46, 52):
        px(P, [(x, y + (y0 if y < 50 else 0)) for x in range(25, 40)], '#625565', 2.2)
        px(P, [(x, y + (y0 if y < 50 else 0)) for x in range(25, 40, 3)], '#9babb2', 2.21)
    # a fresta de lava entre as portas
    lava = '#f9c22b' if t % 2 == 0 else '#fb6b1d'
    px(P, [(32, y) for y in range(31 + y0, 56)], lava, 2.3)
    px(P, [(31, y) for y in range(34 + y0, 56, 2)], '#fb6b1d', 2.29)
    # argola
    px(P, [(34, 44 + y0), (35, 45 + y0), (35, 46 + y0), (34, 47 + y0), (33, 46 + y0)], '#c7dcd0', 2.3)
    # pedra-chave com a cara
    chave = poligono([(26, 17 + y0), (38, 17 + y0), (36, 30 + y0), (28, 30 + y0)])
    P.append(Parte(chave, OBSID, z=3, luz=0.12))
    px(P, [(27, 20 + y0), (28, 20 + y0), (29, 21 + y0), (35, 21 + y0), (36, 20 + y0), (37, 20 + y0)], OUT, 3.1)   # sobrolho
    for ex in (29, 34):
        if t == 3:
            px(P, [(ex, 23 + y0), (ex + 1, 23 + y0), (ex + 2, 23 + y0)], '#fb6b1d', 3.2)
        else:
            px(P, [(ex, 22 + y0), (ex + 1, 22 + y0), (ex, 23 + y0), (ex + 1, 23 + y0), (ex + 2, 23 + y0)], '#f9c22b', 3.2)
            px(P, [(ex, 22 + y0)], BRANCO, 3.25)
    px(P, [(x, 27 + y0) for x in range(30, 35)], OUT, 3.1)
    px(P, [(31, 27 + y0), (33, 27 + y0)], '#fb6b1d', 3.15)
    # as 4 runas (a pulsar, uma de cada vez mais forte)
    for i, (rx, ry) in enumerate(((16, 24), (45, 24), (16, 44), (45, 44))):
        forte = (i == t)
        runa(P, rx, ry + y0, 3.5, '#fbff86' if forte else '#fb6b1d', forma=i)
        if forte:
            px(P, [(rx - 1, ry + y0 - 1), (rx + 3, ry + y0 + 4)], '#f9c22b', 3.55)
    # braço de cá
    P.append(Parte(elipse(53, 24 + y0, 5, 5), OBSID, z=4, luz=0.1))
    P.append(Parte(capsula(54, 27 + y0, 57, 38 + y0, 4.2), OBSID, z=4.1))
    punho = retangulo(51, 38 + y0, 62, 48 + y0, canto=1)
    P.append(Parte(punho, OBSID, z=4.2, plano=True))
    px(P, [(x, 43 + y0) for x in range(52, 62)], '#2e222f', 4.25)
    runa(P, 55, 39 + y0, 4.3, '#fb6b1d', forma=3)
    return desenhar(P, 64, 64)


def escavadora_ana_possuida(t):
    """Máquina de minas dos anões, possuída: caldeira com chaminé a fumegar, chassis de bronze com rebites
    e runas anãs, rodas de carril com raios a girar, cara de ferro com olhos de cultista e uma broca enorme
    em espiral a rodar."""
    P = []
    vib = (0, 1, 0, 1)[t]
    y0 = vib
    # fumo da chaminé
    for i in range(3):
        k = (t + i) % 4
        r = 2.2 + k * 0.8
        P.append(Parte(elipse(15 - k * 2 + i, 6 - k * 1.5 - i, r, r * 0.8), ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'], z=0 + i * 0.01))
    # caldeira e chaminé
    P.append(Parte(capsula(17, 8 + y0, 17, 20 + y0, 2.6), FERRO_ESC, z=1, volume='cilindro_v'))
    P.append(Parte(retangulo(14, 7 + y0, 20, 9 + y0), BRONZE, z=1.1, plano=True))
    cald = capsula(10, 27 + y0, 30, 27 + y0, 8)
    P.append(Parte(cald, FERRO_ESC, z=2, volume='cilindro_h'))
    for x in (14, 22):
        P.append(Parte(retangulo(x, 19 + y0, x + 1, 35 + y0), BRONZE, z=2.1, plano=True))
    px(P, [(x, 22 + y0) for x in range(6, 32, 3) if (x, 22 + y0) in cald], '#c7dcd0', 2.15)   # rebites
    # janelinha da fornalha
    P.append(Parte(elipse(26, 27 + y0, 3, 3), BRONZE, z=2.2))
    px(P, elipse(26, 27 + y0, 1.8, 1.8), '#fb6b1d' if t % 2 else '#f9c22b', 2.3)
    # chassis
    ch = retangulo(5, 34 + y0, 46, 51 + y0, canto=1)
    P.append(Parte(ch, BRONZE, z=3, volume='cilindro_v'))
    px(P, [(x, 40 + y0) for x in range(6, 46)], '#4c3e24', 3.1)
    for x in range(8, 46, 5):
        px(P, [(x, 36 + y0), (x, 49 + y0)], '#fbb954', 3.15)
    for i, x in enumerate((10, 19, 28)):
        runa(P, x, 43 + y0, 3.2, '#f79617' if (i + t) % 3 else '#fbff86', forma=i)
    # rodas de carril com raios a girar
    for (wx, z) in ((13, 4), (27, 4), (41, 4)):
        roda = elipse(wx, 55, 5.5, 5.5)
        P.append(Parte(roda, FERRO_ESC, z=z))
        P.append(Parte(elipse(wx, 55, 2, 2), BRONZE, z=z + 0.1))
        a = t * math.pi / 4
        for k in range(2):
            aa = a + k * math.pi / 2
            px(P, [(int(wx + math.cos(aa) * r), int(55 + math.sin(aa) * r)) for r in (-4, -3, 3, 4)], '#3e3546', z + 0.05)
    # carril
    P.append(Parte(retangulo(0, 61, 63, 62), FERRO_ESC, z=0.5, plano=True))
    # cabeça de ferro (frente) com olhos de cultista
    cab = retangulo(36, 20 + y0, 50, 41 + y0, canto=1)
    P.append(Parte(cab, FERRO_ESC, z=5, volume='cilindro_v', luz=0.1))
    P.append(Parte(retangulo(37, 23 + y0, 44, 31 + y0), None, z=5.1, separar=False, cor='#2e222f'))   # o capuz/visor escuro
    for ex in (38, 41):
        if t == 3:
            px(P, [(ex, 28 + y0), (ex + 1, 28 + y0)], '#9e4539', 5.2)
        else:
            px(P, [(ex, 26 + y0), (ex + 1, 26 + y0), (ex, 27 + y0), (ex + 1, 27 + y0), (ex + 1, 28 + y0)], '#f9c22b', 5.2)
            px(P, [(ex, 26 + y0)], BRANCO, 5.25)
    px(P, [(37, 24 + y0), (38, 25 + y0), (43, 24 + y0), (42, 25 + y0)], '#b33831', 5.2)   # o fogo da possessão
    px(P, [(x, 35 + y0) for x in range(38, 49, 2)], '#3e3546', 5.15)   # grelha
    px(P, [(x, 37 + y0) for x in range(38, 49, 2)], '#3e3546', 5.15)
    # a broca: cone em espiral a rodar
    broca = poligono([(46, 21 + y0), (46, 53 + y0), (63.5, 37 + y0)])
    P.append(Parte(broca, FERRO, z=6, volume='cilindro_h'))
    esp = []
    for (x, y) in broca:
        if (x + 2 * (y - y0) + t * 2) % 6 in (0, 1):
            esp.append((x, y))
    px(P, esp, '#625565', 6.1)
    px(P, [(x, y) for (x, y) in esp if (x + y) % 2 == 0 and y < 34 + y0], '#c7dcd0', 6.15)
    P.append(Parte(retangulo(44, 20 + y0, 47, 54 + y0, canto=1), BRONZE, z=6.2, plano=True))
    px(P, [(45, y + y0) for y in range(22, 53, 4)], '#fbb954', 6.25)
    faiscas(P, 56, 30, 63, 46, t, z=7, n=3, semente=4)
    return desenhar(P, 64, 64)


def automato_da_forja_primordial(t):
    """Autómato anão antiquíssimo: corpo de bronze em barril com placas, rebites e manchas de verdete,
    elmo com visor a brilhar, barba de ferro entrançada com contas, fornalha aberta no peito com grelha,
    engrenagem no ombro a rodar, um martelo enorme no lugar do braço direito e vapor a sair do cano."""
    P = []
    resp = (0, 0, 1, 1)[t]
    y0 = resp
    VERDETE = '#547e64'
    # vapor do cano das costas
    for i in range(3):
        k = (t + i) % 4
        r = 2 + k * 0.7
        P.append(Parte(elipse(12 - k * 2, 14 - k * 2 - i, r, r * 0.8), ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=0 + i * 0.01))
    P.append(Parte(capsula(16, 26 + y0, 14, 17 + y0, 1.8), FERRO_ESC, z=0.3))
    # braço de lá (mão mecânica)
    P.append(Parte(capsula(20, 28 + y0, 15, 38 + y0, 3.4), BRONZE, z=0.5))
    P.append(Parte(capsula(15, 38 + y0, 16, 45 + y0, 3), BRONZE, z=0.6))
    P.append(Parte(elipse(16, 47 + y0, 3.4, 3), FERRO_ESC, z=0.7))
    # pernas curtas e botas
    P.append(Parte(capsula(25, 46, 24, 56, 5), BRONZE, z=1, volume='cilindro_v'))
    P.append(Parte(retangulo(18, 56, 30, 61, canto=1), FERRO_ESC, z=1.1, plano=True))
    P.append(Parte(capsula(36, 46, 37, 56, 5.2), BRONZE, z=1.2, volume='cilindro_v'))
    P.append(Parte(retangulo(31, 56, 44, 61, canto=1), FERRO_ESC, z=1.3, plano=True))
    px(P, [(x, 57) for x in range(33, 43, 3)] + [(x, 57) for x in range(20, 29, 3)], '#c7dcd0', 1.4)
    # tronco em barril
    tronco = elipse(30, 36 + y0, 14, 12)
    P.append(Parte(tronco, BRONZE, z=2, volume='cilindro_v'))
    for y in (29, 43):
        px(P, [(x, y + y0) for x in range(16, 45) if (x, y + y0) in tronco], '#4c3e24', 2.1)
        px(P, [(x, y + y0 - 1) for x in range(17, 44, 3) if (x, y + y0 - 1) in tronco], '#fbb954', 2.12)
    pintas(P, tronco, VERDETE, 2.15, 11, 0.05)
    pintas(P, tronco, '#92a984', 2.16, 12, 0.02)
    # runas antigas nas placas
    runa(P, 20, 32 + y0, 2.2, '#4c3e24', forma=0)
    runa(P, 20, 38 + y0, 2.2, '#4c3e24', forma=2)
    # fornalha no peito: boca em arco com grelha e fogo
    forn = retangulo(29, 33 + y0, 40, 42 + y0) | elipse(34.5, 33 + y0, 5.5, 3)
    P.append(Parte(forn, FERRO_ESC, z=2.3))
    dentro = retangulo(31, 34 + y0, 38, 41 + y0) | elipse(34.5, 34 + y0, 3.5, 2)
    P.append(Parte(dentro, None, z=2.4, separar=False, cor='#9e4539'))
    fogo(P, 34.5, 41 + y0, 7, 8, t, z=2.5, semente=2, linguas=2, separar=False)
    for x in (32, 35, 37):
        px(P, [(x, y) for y in range(33 + y0, 42 + y0)], '#2e222f', 2.6)
    # cabeça: elmo com visor e barba de ferro entrançada
    hx, hy = 34, 17 + y0
    elmo = elipse(hx, hy, 6, 5.5)
    P.append(Parte(elmo, BRONZE, z=3, luz=0.1))
    P.append(Parte(retangulo(hx - 6, hy + 2, hx + 6, hy + 3), FERRO_ESC, z=3.1, plano=True))   # aba do elmo
    P.append(Parte(capsula(hx - 4, hy - 5, hx - 7, hy - 9, 1.2), FERRO, z=2.9))    # cristas de ferro
    P.append(Parte(capsula(hx + 2, hy - 5, hx + 4, hy - 9, 1.2), FERRO, z=2.9))
    P.append(Parte(retangulo(hx - 1, hy - 1, hx + 6, hy + 1), None, z=3.2, separar=False, cor=OUT))   # visor
    if t == 3:
        px(P, [(x, hy) for x in range(hx + 1, hx + 6)], '#9e4539', 3.3)
    else:
        px(P, [(x, hy) for x in range(hx + 1, hx + 6)], '#30e1b9', 3.3)
        px(P, [(hx + 3, hy), (hx + 4, hy)], '#8ff8e2', 3.35)
        px(P, [(hx + 4, hy - 1)], BRANCO, 3.4)
    barba = poligono([(hx - 5, hy + 4), (hx + 7, hy + 4), (hx + 5, hy + 15), (hx + 1, hy + 18), (hx - 3, hy + 14)])
    P.append(Parte(barba, FERRO, z=3.5, volume='cilindro_v'))
    for x in (hx - 2, hx + 1, hx + 4):   # tranças
        px(P, [(x + (y % 2), y) for y in range(hy + 5, hy + 16) if (x, y) in barba], '#625565', 3.55)
    px(P, [(hx - 2, hy + 12), (hx + 1, hy + 15), (hx + 4, hy + 12)], '#f9c22b', 3.6)    # contas de ouro
    # engrenagem no ombro de cá, a rodar
    gx, gy = 44, 27 + y0
    eng = elipse(gx, gy, 4.5, 4.5)
    a0 = t * math.pi / 8
    for k in range(8):
        a = a0 + k * math.pi / 4
        eng |= elipse(gx + math.cos(a) * 5.2, gy + math.sin(a) * 5.2, 1.2, 1.2)
    P.append(Parte(eng, BRONZE, z=4))
    P.append(Parte(elipse(gx, gy, 1.6, 1.6), FERRO_ESC, z=4.1))
    # o braço-martelo
    P.append(Parte(capsula(gx + 1, gy + 3, 48, 39 + y0, 3.6), BRONZE, z=4.2))
    P.append(Parte(capsula(48, 39 + y0, 50, 56, 1.4), MADEIRA, z=4.3))   # cabo
    cab_m = retangulo(41, 42 + y0, 62, 56 + y0, canto=1)
    P.append(Parte(cab_m, FERRO_ESC, z=4.5, volume='cilindro_h'))
    P.append(Parte(retangulo(41, 42 + y0, 43, 56 + y0), BRONZE, z=4.6, plano=True))
    P.append(Parte(retangulo(60, 42 + y0, 62, 56 + y0), BRONZE, z=4.6, plano=True))
    runa(P, 49, 46 + y0, 4.7, '#fb6b1d' if t % 2 else '#f9c22b', forma=1)
    runa(P, 54, 46 + y0, 4.7, '#f9c22b' if t % 2 else '#fb6b1d', forma=3)
    px(P, [(46, 45 + y0), (47, 45 + y0), (48, 45 + y0)], '#c7dcd0', 4.7)
    faiscas(P, 30, 26, 40, 34, t, z=6, n=3, semente=8)
    return desenhar(P, 64, 64)


# ======================================================================================================
# @@CRIATURAS_GRANDES@@
# ======================================================================================================

# id -> (pasta antiga, função, lado do quadro)
CRIATURAS = [
    ('salamandra', 'monstros', salamandra, 32),
    ('elemental_de_fogo', 'monstros', elemental_de_fogo, 32),
    ('diabrete', 'monstros', diabrete, 32),
    ('cao_infernal', 'monstros', cao_infernal, 32),
    ('morcego_de_cinza', 'monstros', morcego_de_cinza, 32),
    ('escorpiao_de_lava', 'monstros', escorpiao_de_lava, 32),
    ('cultista_do_fogo', 'monstros', cultista_do_fogo, 32),
    ('kai_duelo_da_historia', 'monstros', kai_duelo_da_historia, 32),
    ('kai', 'bosses', kai, 32),
    ('golem_de_magma', 'monstros', golem_de_magma, 48),
    ('fenix_de_cinza', 'guardioes', fenix_de_cinza, 48),
    ('sapo_vulcao', 'guardioes', sapo_vulcao, 48),
    ('sumo_sacerdote_das_chamas', 'guardioes', sumo_sacerdote_das_chamas, 48),
    ('golem_forjado_n7', 'monstros', golem_forjado_n7, 64),
    ('golem_portao_de_obsidiana', 'guardioes', golem_portao_de_obsidiana, 64),
    ('escavadora_ana_possuida', 'guardioes', escavadora_ana_possuida, 64),
    ('automato_da_forja_primordial', 'bosses', automato_da_forja_primordial, 64),
]


def _nomes():
    import json
    d = {}

    def andar(o):
        if isinstance(o, dict):
            if 'id' in o and 'nome_pt' in o and isinstance(o['id'], str):
                d.setdefault(o['id'], o['nome_pt'])
            for v in o.values():
                andar(v)
        elif isinstance(o, list):
            for v in o:
                andar(v)
    for f in ('monstros.json', 'bosses.json', 'masmorras.json'):
        try:
            with open(os.path.join(RAIZ, 'dados', f), encoding='utf-8') as fh:
                andar(json.load(fh))
        except (OSError, ValueError):
            pass
    return d


def _quadros(img):
    h = img.height
    return [img.crop((i * h, 0, (i + 1) * h, h)) for i in range(img.width // h)]


def _escala(lado):
    return {32: 3, 48: 2, 64: 2}.get(lado, 1)


def _fora_da_paleta(img):
    maus = set()
    dados = img.get_flattened_data() if hasattr(img, 'get_flattened_data') else img.getdata()
    for (r, g, b, a) in dados:
        if a and '#%02x%02x%02x' % (r, g, b) not in PALETA:
            maus.add('#%02x%02x%02x' % (r, g, b))
    return maus


def _grelha(blocos, titulo, caminho, fundo=(38, 43, 58)):
    """blocos: lista de (lista de listas de quadros lado a lado, escala, nome). Grava um GIF de 8 quadros, 160 ms."""
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
    fonte_t = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    MAXL, GAP, TXT = 1200, 12, 18
    tam = []
    for (anims, k, nome) in blocos:
        w = sum(a[0].width * k for a in anims) + GAP * (len(anims) - 1)
        h = max(a[0].height * k for a in anims)
        w = max(w, int(fonte.getlength(nome)) + 4)
        tam.append((w, h))
    # arrumar em linhas
    pos, x, y, alt_linha = [], GAP, 30, 0
    for (w, h) in tam:
        if x + w + GAP > MAXL and x > GAP:
            x, y = GAP, y + alt_linha + TXT + GAP
            alt_linha = 0
        pos.append((x, y))
        x += w + GAP * 2
        alt_linha = max(alt_linha, h)
    W = MAXL if len(blocos) > 1 else max(tam[0][0] + 2 * GAP, 300)
    H = y + alt_linha + TXT + GAP
    imgs = []
    for f in range(8):
        im = Image.new('RGB', (W, H), fundo)
        d = ImageDraw.Draw(im)
        d.text((GAP, 6), titulo, fill=(230, 230, 230), font=fonte_t)
        for (anims, k, nome), (bx, by), (w, h) in zip(blocos, pos, tam):
            xx = bx
            for a in anims:
                q = a[f % len(a)].resize((a[0].width * k, a[0].height * k), Image.NEAREST)
                im.paste(q, (xx, by + h - q.height), q)
                xx += q.width + GAP
            d.text((bx, by + h + 3), nome, fill=(220, 220, 220), font=fonte)
        imgs.append(im)
    pal = [i.convert('P', palette=Image.ADAPTIVE, colors=255) for i in imgs]
    pal[0].save(caminho, save_all=True, append_images=pal[1:], duration=160, loop=0, disposal=1)


def main():
    ver = None
    so = None
    if '--ver' in sys.argv:
        ver = sys.argv[sys.argv.index('--ver') + 1]
        os.makedirs(ver, exist_ok=True)
    if '--so' in sys.argv:
        so = set(sys.argv[sys.argv.index('--so') + 1].split(','))
    os.makedirs(DESTINO, exist_ok=True)
    nomes = _nomes()
    comp, novos = [], []
    for (cid, pasta, func, lado) in CRIATURAS:
        if so and cid not in so:
            continue
        frames = [func(t) for t in range(4)]
        for f in frames:
            assert f.size == (lado, lado), (cid, f.size)
        tira = Image.new('RGBA', (lado * 4, lado), (0, 0, 0, 0))
        for i, f in enumerate(frames):
            tira.paste(f, (i * lado, 0))
        maus = _fora_da_paleta(tira)
        if maus:
            print('!! cores fora da paleta em', cid, sorted(maus))
        tira.save(os.path.join(DESTINO, f'{cid}_parado_lado.png'))
        antigo = Image.open(os.path.join(ANTIGO, pasta, f'{cid}_parado_lado.png')).convert('RGBA')
        velhos = _quadros(antigo)
        k = _escala(lado)
        nome = nomes.get(cid, cid)
        comp.append(([velhos, frames], k, nome))
        novos.append(([frames], k, nome))
        if ver:
            kk = max(2, 384 // lado)
            folha = Image.new("RGBA", (lado * kk * 4 + 30, lado * kk * 2 + 20), (38, 43, 58, 255))
            for i, q in enumerate(velhos[:4]):
                g = q.resize((lado * kk, lado * kk), Image.NEAREST)
                folha.paste(g, (i * lado * kk + i * 10, 0), g)
            for i, q in enumerate(frames):
                g = q.resize((lado * kk, lado * kk), Image.NEAREST)
                folha.paste(g, (i * lado * kk + i * 10, lado * kk + 10), g)
            folha.save(os.path.join(ver, f'ver_{cid}.png'))
        print('ok', cid, lado)
    if not so:
        _grelha(comp, 'Região 7 — Vulcão — antes | depois', os.path.join(DESTINO, 'comparar.gif'))
        _grelha(novos, 'Região 7 — Vulcão — depois', os.path.join(DESTINO, 'depois.gif'))
        print('gifs gravados em', DESTINO)


if __name__ == '__main__':
    main()
