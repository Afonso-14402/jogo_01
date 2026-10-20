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
    """Máscara de uma língua de fogo: larga em baixo, bico em cima, a ondular com a fase."""
    m = set()
    for r in range(int(alt) + 1):
        q = r / max(1, alt)
        meia = larg / 2 * (1 - q) ** 0.75 * (1 + 0.15 * math.sin(q * 6 + fase))
        sway = math.sin(q * 3.2 + fase) * q * 2.0 * torcer
        y = int(round(base - r))
        x1 = int(round(cx + sway - meia))
        x2 = int(round(cx + sway + meia))
        for x in range(x1, max(x1, x2 - 1) + 1):
            m.add((x, y))
    return m


def fogo(P, cx, base, larg, alt, t, z, semente=0, cores=FOGO_CORES, linguas=3, separar=True):
    """Uma chama em camadas (vermelho-laranja por fora, amarelo e quase branco por dentro), que tremula com t."""
    rnd = random.Random(semente)
    fase = t * math.pi / 2
    fora = lingua_fogo(cx, base, larg, alt, fase + semente)
    for i in range(linguas - 1):
        lado = -1 if i % 2 == 0 else 1
        ox = lado * larg * (0.28 + rnd.random() * 0.12)
        h = alt * (0.45 + 0.3 * abs(math.sin(fase + i + semente)))
        fora |= lingua_fogo(cx + ox, base, larg * 0.55, h, fase * 1.3 + i * 2 + semente, 1.4)
    P.append(Parte(fora, None, z=z, separar=separar, cor=cores[0]))
    meio = lingua_fogo(cx, base - 1, larg * 0.7, alt * 0.72, fase + semente + 0.4)
    P.append(Parte(meio & fora, None, z=z + 0.01, separar=False, cor=cores[1]))
    dentro = lingua_fogo(cx, base - 1, larg * 0.42, alt * 0.45, fase + semente + 0.8)
    P.append(Parte(dentro & fora, None, z=z + 0.02, separar=False, cor=cores[2]))
    if alt >= 6:
        nucleo = lingua_fogo(cx, base - 1, max(1.5, larg * 0.2), alt * 0.22, fase + semente)
        P.append(Parte(nucleo & fora, None, z=z + 0.03, separar=False, cor=cores[3]))
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
    """Lagarto de fogo: corpo laranja com pintas escuras, barriga amarela, crista de chamas nas costas,
    cauda com ponta a arder, olho de réptil (fenda), garras."""
    P = []
    resp = (0, 0, 1, 0)[t]
    cauda = (0, 1, 2, 1)[t]
    # patas de trás (longe)
    for (x0, x1) in ((10, 8), (20, 22)):
        P.append(Parte(capsula(x0, 25, x1, 29, 1.4), DEMONIO_ESC, z=0))
        px(P, [(x1 + 1, 30), (x1 - 1, 30)], '#c7dcd0', 0.1)
    # cauda: três segmentos a afinar, ponta a abanar
    c1 = (8, 24)
    c2 = (3, 22 - cauda // 2)
    c3 = (1, 17 - cauda)
    P.append(Parte(capsula(*c1, *c2, 2.6), LARANJA, z=1, volume='cilindro_h'))
    P.append(Parte(capsula(*c2, *c3, 1.6), LARANJA, z=1.1))
    fogo(P, c3[0] + 1, c3[1], 4, 6, t, z=1.2, semente=3, linguas=2)
    # corpo
    corpo = elipse(15, 24 - resp * 0.5, 8.5, 4.5 + resp * 0.3)
    P.append(Parte(corpo, LARANJA, z=2, volume='cilindro_h'))
    barriga = {p for p in elipse(15, 26.5, 7.5, 2.6) if p[1] >= 26} & corpo
    P.append(Parte(barriga, ['#9e4539', '#f79617', '#f9c22b', '#fbb954', '#fbff86'], z=2.1, separar=False, plano=True))
    # pintas escuras e escamas claras nas costas
    px(P, [(10, 22), (11, 22), (14, 21), (15, 21), (18, 22), (19, 22), (12, 24), (17, 24)], '#9e4539', 2.2)
    px(P, [(9, 21), (13, 20), (16, 20)], '#fbb954', 2.25)
    # crista de chamas nas costas
    for i, x in enumerate((9, 13, 17)):
        fogo(P, x, 20 - resp, 3.2, 3 + (i + t) % 3, t + i, z=1.5, semente=i + 7, linguas=1, separar=False)
    # cabeça
    cab = elipse(24.5, 21.5 - resp * 0.5, 5, 3.6) | capsula(24, 22 - resp * 0.5, 29.5, 23 - resp * 0.5, 2.0)
    P.append(Parte(cab, LARANJA, z=4, luz=0.08))
    queixo = {p for p in cab if p[1] >= 24 - resp * 0.5}
    P.append(Parte(queixo, ['#9e4539', '#f79617', '#f9c22b', '#fbb954', '#fbff86'], z=4.1, separar=False, plano=True))
    y = int(20 - resp * 0.5)
    olho(P, 24, y - 1, 5, cor='#f9c22b', tam=1)
    px(P, [(25, y), (25, y - 1)], OUT, 5.1)               # pupila em fenda
    px(P, [(23, y - 2), (24, y - 2), (25, y - 2), (26, y - 2)], '#9e4539', 5)   # sobrolho
    px(P, [(29, y + 1)], OUT, 5)                           # narina
    px(P, [(x, y + 3) for x in range(25, 30)], '#9e4539', 5)   # boca
    if t == 2:
        px(P, [(30, y + 3), (31, y + 3), (31, y + 4)], '#e83b3b', 5)   # língua
    # patas da frente (perto)
    for (x0, x1) in ((12, 11), (21, 23)):
        P.append(Parte(capsula(x0, 25, x1, 29, 1.5), LARANJA, z=6))
        px(P, [(x1 + 1, 30), (x1 - 1, 30), (x1 + 2, 30)], '#c7dcd0', 6.1)
    return desenhar(P, 32, 32)


def elemental_de_fogo(t):
    """Uma chama viva com cara: corpo em gota a arder, pedaços de carvão a girar à volta, mãos de chama,
    olhos brancos-amarelos e boca aberta; faúlhas a subir."""
    P = []
    dy = (0, -1, -1, 0)[t]
    base = 27 + dy
    # cauda de fumo/fogo em baixo (flutua)
    fogo(P, 16, 30 + dy, 5, 6, t + 2, z=0.5, semente=9, linguas=1)
    # corpo
    corpo = fogo(P, 16, base, 15, 22, t, z=1, semente=1, linguas=3)
    # cara: órbitas escuras, olhos, boca
    ey = 15 + dy
    for ex in (16, 21):
        px(P, elipse(ex + 0.5, ey + 1, 2, 2.2), '#9e4539', 3)
        if t == 3:
            px(P, [(ex - 1, ey + 1), (ex, ey + 1), (ex + 1, ey + 1)], OUT, 3.1)
        else:
            px(P, [(ex, ey), (ex + 1, ey), (ex, ey + 1), (ex + 1, ey + 1), (ex, ey + 2), (ex + 1, ey + 2)], '#fbff86', 3.1)
            px(P, [(ex, ey)], BRANCO, 3.2)
    boca = elipse(19.5, ey + 6, 2.2, 1.6 + (t % 2) * 0.5)
    px(P, boca, '#9e4539', 3)
    px(P, [(19, ey + 6), (20, ey + 6)], '#6e2727', 3.05)
    # mãos de chama a flutuar
    for (hx, hy, s) in ((6, 19, 11), (26, 20, 12)):
        hy += (dy if s == 11 else -dy)
        fogo(P, hx, hy + 2, 4, 5, t + s, z=4, semente=s, linguas=2)
    # carvões a girar à volta (núcleo)
    ang = t * math.pi / 2
    for i in range(3):
        a = ang + i * 2 * math.pi / 3
        x = 16 + math.cos(a) * 11
        y = 18 + dy + math.sin(a) * 4
        z = 5 if math.sin(a) > 0 else 0.4
        P.append(Parte(elipse(x, y, 1.6, 1.4), CARVAO, z=z))
        px(P, [(int(x), int(y))], '#fb6b1d', z + 0.01)
    faiscas(P, 8, 0, 24, 10, t, z=6, n=4, semente=2)
    return desenhar(P, 32, 32)


def diabrete(t):
    """Demoniozinho vermelho (≈18 px): chifres, orelhas bicudas, asas de morcego, sorriso de dentes,
    olhos amarelos, cauda de seta e um tridente."""
    P = []
    voo = (0, -1, -2, -1)[t]
    asa = (0, 1, 2, 1)[t]
    cx = 14
    by = 23 + voo
    # asa de trás
    a2 = poligono([(cx - 2, by - 9), (cx - 9, by - 15 + asa * 2), (cx - 12, by - 9 + asa), (cx - 9, by - 7 + asa), (cx - 6, by - 5)])
    P.append(Parte(a2, ['#2e222f', '#45293f', '#7a3045', '#9e4539', '#cd683d'], z=0, plano=True))
    # cauda com ponta de seta
    P.append(Parte(capsula(cx - 3, by - 1, cx - 7, by + 3, 1.0), DEMONIO, z=0.5))
    P.append(Parte(capsula(cx - 7, by + 3, cx - 9, by + 1 - (t % 2), 0.8), DEMONIO, z=0.5))
    sx, sy = cx - 10, by - (t % 2)
    px(P, [(sx, sy), (sx - 1, sy), (sx, sy - 1), (sx + 1, sy - 1), (sx - 1, sy - 1), (sx, sy - 2)], '#b33831', 0.6)
    # pernas
    P.append(Parte(capsula(cx - 2, by, cx - 3, by + 5, 1.2), DEMONIO_ESC, z=1))
    P.append(Parte(capsula(cx + 1, by, cx + 2, by + 5, 1.3), DEMONIO, z=3))
    px(P, [(cx + 3, by + 6), (cx + 4, by + 6), (cx - 2, by + 6), (cx - 1, by + 6)], OUT, 3.1)
    # corpo (barriguinha)
    corpo = elipse(cx, by - 3, 3.6, 4.2)
    P.append(Parte(corpo, DEMONIO, z=2))
    px(P, [(cx + 1, by - 2), (cx + 2, by - 1), (cx + 1, by)], '#ea4f36', 2.1)
    # cabeça grande
    hx, hy = cx + 1, by - 10
    cab = elipse(hx, hy, 5.4, 4.8)
    P.append(Parte(cab, DEMONIO, z=4, luz=0.1))
    # orelha bicuda
    P.append(Parte(poligono([(hx - 3, hy - 1), (hx - 9, hy - 3), (hx - 3, hy + 2)]), DEMONIO, z=3.9))
    # chifres
    for (bx, curva) in ((hx - 2, -1), (hx + 2, 1)):
        ch = capsula(bx, hy - 4, bx + curva, hy - 7, 1.1) | capsula(bx + curva, hy - 7, bx + curva * 2 + 1, hy - 9, 0.7)
        P.append(Parte(ch, ['#4c3e24', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff'], z=4.2))
    # olhos grandes e sorriso
    olho(P, hx + 1, hy - 2, 5, cor='#f9c22b', tam=1)
    px(P, [(hx + 2, hy - 1)], OUT, 5.1)
    olho(P, hx + 4, hy - 2, 5, cor='#f9c22b', tam=1)
    px(P, [(hx + 5, hy - 1)], OUT, 5.1)
    px(P, [(hx + 0, hy - 3), (hx + 1, hy - 4), (hx + 2, hy - 4)], '#6e2727', 5)   # sobrolho malandro
    sorr = [(hx + 1, hy + 2), (hx + 2, hy + 3), (hx + 3, hy + 3), (hx + 4, hy + 3), (hx + 5, hy + 2)]
    px(P, sorr, OUT, 5)
    px(P, [(hx + 2, hy + 2), (hx + 4, hy + 2)], BRANCO, 5.1)
    # asa da frente
    a1 = poligono([(cx + 0, by - 8), (cx - 5, by - 16 + asa * 2), (cx - 8, by - 11 + asa), (cx - 6, by - 8 + asa), (cx - 3, by - 5)])
    P.append(Parte(a1, ['#2e222f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=4.5, plano=True))
    px(P, [(cx - 1, by - 8), (cx - 2, by - 10 + asa), (cx - 3, by - 12 + asa), (cx - 4, by - 14 + asa)], '#6e2727', 4.6)   # osso da asa
    # tridente (na mão da frente)
    mx, my = cx + 6, by - 3
    P.append(Parte(capsula(mx, my - 10, mx, my + 8, 0.6), ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#ab947a'], z=6))
    tri = [(mx - 2, my - 11), (mx - 2, my - 12), (mx - 2, my - 13), (mx, my - 12), (mx, my - 13), (mx, my - 14),
           (mx + 2, my - 11), (mx + 2, my - 12), (mx + 2, my - 13), (mx - 1, my - 11), (mx + 1, my - 11), (mx, my - 11)]
    P.append(Parte(set(tri), FERRO, z=6.1, plano=True))
    braco = capsula(cx + 2, by - 5, mx, my, 1.1)
    P.append(Parte(braco, DEMONIO, z=6.2))
    px(P, [(mx, my - 1), (mx + 1, my)], '#ea4f36', 6.3)
    if t == 0:
        px(P, [(mx, my - 14)], BRANCO, 6.4)
    return desenhar(P, 32, 32)


def cao_infernal(t):
    """Cão de basalto com fendas de lava: crina e ponta da cauda em chamas, olhos a arder, boca a brilhar,
    dentes, orelhas em bico, garras."""
    P = []
    resp = (0, 0, 1, 0)[t]
    y0 = resp
    # pernas de trás (longe)
    P.append(Parte(capsula(9, 21, 8, 29, 1.6), ROCHA_ESC, z=0))
    P.append(Parte(capsula(21, 21, 22, 29, 1.6), ROCHA_ESC, z=0))
    # cauda
    P.append(Parte(capsula(6, 19 + y0, 2, 14 + y0, 1.4), ROCHA, z=0.5))
    fogo(P, 2, 14 + y0, 4, 6, t, z=0.6, semente=5, linguas=2)
    # corpo
    corpo = elipse(14, 20 + y0 * 0.5, 8.5, 5) | elipse(20, 19, 5, 5.5)
    P.append(Parte(corpo, ROCHA, z=2))
    # costelas e fendas de lava
    px(P, [(12, 20), (12, 21), (14, 20), (14, 21), (16, 20), (16, 21)], '#3e3546', 2.1)
    fendas(P, corpo, 4, 2.2, n=2, comp=6, t=t)
    # crina de chamas no pescoço
    for i, (x, h) in enumerate(((17, 6), (20, 7), (23, 5))):
        fogo(P, x, 16 + y0 * 0.5, 4, h, t + i, z=2.5, semente=i + 11, linguas=1)
    # cabeça
    hx, hy = 25, 15 + y0 * 0.5
    cab = elipse(hx, hy, 4.2, 3.8) | capsula(hx, hy + 1, hx + 5, hy + 2, 2.2)
    P.append(Parte(cab, ROCHA, z=4, luz=0.08))
    # orelha
    P.append(Parte(poligono([(hx - 3, hy - 2), (hx - 3, hy - 8), (hx + 1, hy - 3)]), ROCHA, z=3.9))
    px(P, [(hx - 2, hy - 5), (hx - 2, hy - 4)], '#b33831', 3.95)
    # boca aberta a brilhar e dentes
    by = int(hy + 3)
    px(P, [(x, by) for x in range(hx + 1, hx + 7)], OUT, 5)
    px(P, [(x, by + 1) for x in range(hx + 1, hx + 5)], '#fb6b1d', 5)
    px(P, [(hx + 2, by + 1)], '#f9c22b', 5.1)
    px(P, [(hx + 3, by), (hx + 5, by), (hx + 6, by + 1)], BRANCO, 5.2)
    px(P, [(hx + 6, int(hy) + 1)], OUT, 5)   # nariz
    # olho a arder
    if t == 3:
        px(P, [(hx, int(hy) - 1), (hx + 1, int(hy) - 1), (hx + 2, int(hy) - 1)], OUT, 5)
    else:
        px(P, [(hx, int(hy) - 1), (hx + 1, int(hy) - 1), (hx + 2, int(hy) - 1), (hx + 1, int(hy) - 2)], '#f9c22b', 5)
        px(P, [(hx + 1, int(hy) - 1)], BRANCO, 5.1)
    px(P, [(hx - 1, int(hy) - 3), (hx, int(hy) - 3), (hx + 1, int(hy) - 2)], '#3e3546', 5)   # sobrolho
    # pernas da frente (perto)
    P.append(Parte(capsula(11, 22, 11, 29, 1.8), ROCHA, z=6))
    P.append(Parte(capsula(23, 20, 24, 29, 1.8), ROCHA, z=6))
    for x in (11, 24):
        px(P, [(x + 1, 30), (x + 2, 30)], '#c7dcd0', 6.1)
        px(P, [(x - 1, 26)], '#fb6b1d', 6.1)
    return desenhar(P, 32, 32)


def morcego_de_cinza(t):
    """Morcego cinzento de cinza: orelhas grandes, olhos de brasa, presas, asas com dedos e brasas,
    a largar um rasto de cinza."""
    P = []
    asa = (0, 1, 2, 1)[t]       # 0 = em cima, 2 = em baixo
    voo = (0, 1, 2, 1)[t]
    cx, cy = 16, 17 + voo
    # rasto de cinza (atrás, à esquerda)
    for i in range(5):
        x = 3 + i * 2 - (t % 2)
        y = cy + 3 + ((i + t) % 3) - 1
        px(P, [(x, y)], ('#7f708a', '#9babb2', '#625565')[(i + t) % 3], 0)
    # asas: forma muda com o bater
    def asa_m(lado, z, rampa):
        sx = cx + (-2 if lado < 0 else 2)
        if asa == 0:
            pts = [(sx, cy - 1), (sx + lado * 5, cy - 9), (sx + lado * 11, cy - 7), (sx + lado * 13, cy - 2),
                   (sx + lado * 10, cy - 3), (sx + lado * 8, cy), (sx + lado * 5, cy - 1), (sx + lado * 2, cy + 2)]
        elif asa == 1:
            pts = [(sx, cy - 1), (sx + lado * 6, cy - 4), (sx + lado * 12, cy - 3), (sx + lado * 14, cy + 1),
                   (sx + lado * 11, cy + 1), (sx + lado * 8, cy + 3), (sx + lado * 5, cy + 2), (sx + lado * 2, cy + 3)]
        else:
            pts = [(sx, cy - 1), (sx + lado * 6, cy + 1), (sx + lado * 11, cy + 4), (sx + lado * 12, cy + 9),
                   (sx + lado * 9, cy + 7), (sx + lado * 6, cy + 8), (sx + lado * 4, cy + 5), (sx + lado * 1, cy + 3)]
        m = poligono(pts)
        P.append(Parte(m, rampa, z=z, plano=True))
        # dedos da asa
        ossos = []
        for k in (2, 3, 5):
            x2, y2 = pts[k]
            for s in range(1, 6):
                q = s / 6
                ossos.append((int(sx + (x2 - sx) * q), int(cy - 1 + (y2 - cy + 1) * q)))
        px(P, [p for p in ossos if p in m], rampa[0] if rampa[0] != OUT else '#3e3546', z + 0.01)
        return m
    asa_m(-1, 0.5, ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'])
    # corpo
    corpo = elipse(cx, cy + 1, 3.8, 4.2)
    P.append(Parte(corpo, CINZA, z=2))
    pintas(P, corpo, '#625565', 2.1, 3, 0.12)
    # pés
    px(P, [(cx - 1, cy + 6), (cx + 1, cy + 6), (cx - 1, cy + 7), (cx + 2, cy + 7)], '#3e3546', 1.9)
    # cabeça e orelhas
    hx, hy = cx + 2, cy - 4
    P.append(Parte(poligono([(hx - 3, hy - 1), (hx - 4, hy - 8), (hx, hy - 2)]), CINZA, z=2.9))
    P.append(Parte(poligono([(hx + 0, hy - 2), (hx + 2, hy - 8), (hx + 3, hy - 1)]), CINZA, z=3.1))
    px(P, [(hx + 2, hy - 5), (hx + 2, hy - 4)], '#cf657f', 3.2)
    cab = elipse(hx, hy, 3.6, 3.2) | capsula(hx, hy + 1, hx + 4, hy + 1, 1.5)
    P.append(Parte(cab, CINZA, z=3, luz=0.1))
    olho(P, hx + 1, hy - 1, 4, cor='#fb6b1d', tam=1)
    px(P, [(hx + 2, hy)], '#f9c22b', 4.05)
    px(P, [(hx + 5, hy + 1)], OUT, 4)
    px(P, [(hx + 2, hy + 3), (hx + 4, hy + 3)], BRANCO, 4.1)   # presas
    asa_m(1, 5, ['#2e222f', '#625565', '#7f708a', '#9babb2', '#c7dcd0'])
    # brasas na asa da frente
    px(P, [(cx + 7, cy - 1 + asa * 2), (cx + 10, cy + asa * 2)], '#fb6b1d', 5.2)
    cinzas(P, 2, 2, 30, 30, t, z=6, n=3, semente=8)
    return desenhar(P, 32, 32)


def escorpiao_de_lava(t):
    """Escorpião com carapaça de rocha às placas, lava a brilhar entre as placas, cauda curvada sobre as costas
    com ferrão incandescente, pinças de rocha e seis patas finas."""
    P = []
    cs = (0, 1, 1, 0)[t]
    pin = (0, 0, 1, 1)[t]
    # patas (as de trás primeiro)
    for i, x in enumerate((9, 13, 17)):
        P.append(Parte(capsula(x, 25, x - 3, 29, 0.8) | capsula(x - 3, 29, x - 4, 30, 0.6), ROCHA_ESC, z=0))
    # cauda: segmentos em arco por cima das costas
    seg = [(7, 24), (4, 20), (4, 15), (7, 11 + cs), (11, 9 + cs), (15, 10 + cs)]
    for i in range(len(seg) - 1):
        r = 2.6 - i * 0.25
        P.append(Parte(capsula(*seg[i], *seg[i + 1], r), ROCHA, z=1 + i * 0.1))
        px(P, [seg[i + 1]], '#fb6b1d' if (i + t) % 2 else '#f79617', 1.05 + i * 0.1)
    # ferrão incandescente
    fx, fy = seg[-1]
    fer = capsula(fx, fy, fx + 3, fy + 3, 1.6) | capsula(fx + 3, fy + 3, fx + 4, fy + 6, 0.7)
    P.append(Parte(fer, LAVA, z=2))
    px(P, [(fx + 4, fy + 6)], '#fbff86' if t % 2 == 0 else '#f9c22b', 2.1)
    # corpo em placas
    corpo = elipse(14, 25, 8, 3.6)
    P.append(Parte(corpo, ROCHA, z=3, volume='cilindro_h'))
    for x in (9, 13, 17):
        px(P, [(x, y) for y in range(22, 28) if (x, y) in corpo], '#fb6b1d' if (x + t) % 2 else '#f79617', 3.1)
    pintas(P, corpo, '#7f708a', 3.05, 6, 0.1, filtro=lambda x, y: y < 24)
    # cabeça
    hx, hy = 22, 25
    cab = elipse(hx, hy, 3.4, 2.8)
    P.append(Parte(cab, ROCHA, z=4, luz=0.08))
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2)], '#e83b3b', 4.1)
    px(P, [(hx + 1, hy - 2)], '#fca790', 4.15)
    # pinças: braço + garra em C
    for (z, dx, dyy, rampa) in ((3.5, -1, -1, ROCHA_ESC), (6, 0, 0, ROCHA)):
        ax, ay = hx + 2 + dx, hy + 1 + dyy
        mx, my = hx + 6 + dx, hy - 1 + dyy
        P.append(Parte(capsula(ax, ay, mx, my, 1.2), rampa, z=z))
        g = elipse(mx + 2, my - 1, 2.4, 1.9)
        cima = capsula(mx + 2, my - 2, mx + 5, my - 3 - pin, 1.0)
        baixo = capsula(mx + 2, my, mx + 5, my + 1, 0.9)
        P.append(Parte(g | cima | baixo, rampa, z=z + 0.1))
        px(P, [(mx + 5, my - 3 - pin)], '#f79617', z + 0.2)
    # patas da frente
    for x in (11, 15, 19):
        P.append(Parte(capsula(x, 26, x + 2, 29, 0.8) | capsula(x + 2, 29, x + 3, 30, 0.6), ROCHA, z=5))
    return desenhar(P, 32, 32)


def cultista_do_fogo(t):
    """Cultista de túnica vermelha com capuz bicudo, cara na sombra com olhos de brasa, cinto de corda,
    bordados dourados e uma chama a flutuar nas mãos."""
    P = []
    resp = (0, 0, 1, 0)[t]
    cx = 14
    # bainha da túnica (abana)
    sw = (0, 1, 0, -1)[t]
    tun = poligono([(cx - 4, 12 + resp), (cx + 4, 12 + resp), (cx + 7 + sw, 30), (cx - 7 + sw, 30)])
    P.append(Parte(tun, ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=1, volume='cilindro_v'))
    veios(P, tun, 1.1, '#6e2727', freq=4, onda=0.6)
    px(P, [(x, 29) for x in range(cx - 6 + sw, cx + 7 + sw)], '#f9c22b', 1.2)        # bordado da bainha
    px(P, [(x, 28) for x in range(cx - 6 + sw, cx + 7 + sw, 2)], '#f79617', 1.2)
    # cinto de corda
    px(P, [(x, 20 + resp) for x in range(cx - 5, cx + 6)], '#966c6c', 1.3)
    px(P, [(cx + 2, 21 + resp), (cx + 2, 22 + resp), (cx + 3, 23 + resp), (cx + 1, 23 + resp)], '#ab947a', 1.3)
    # símbolo da chama no peito
    px(P, [(cx, 15 + resp), (cx - 1, 16 + resp), (cx + 1, 16 + resp), (cx, 17 + resp), (cx, 16 + resp)], '#f9c22b', 1.4)
    # capuz
    hx, hy = cx + 1, 8 + resp
    capuz = elipse(hx, hy, 5.2, 5) | poligono([(hx - 5, hy - 1), (hx - 7, hy - 8), (hx + 1, hy - 4)])
    P.append(Parte(capuz, ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=3))
    # cara na sombra
    cara = elipse(hx + 2, hy + 1, 3, 3.2)
    P.append(Parte(cara, None, z=3.1, separar=False, cor='#2e222f'))
    if t == 3:
        px(P, [(hx + 2, hy + 1), (hx + 4, hy + 1)], '#9e4539', 3.2)
    else:
        px(P, [(hx + 2, hy), (hx + 2, hy + 1), (hx + 4, hy), (hx + 4, hy + 1)], '#f9c22b', 3.2)
        px(P, [(hx + 2, hy), (hx + 4, hy)], BRANCO, 3.3)
    px(P, [(hx + 3, hy - 3), (hx + 4, hy - 3), (hx + 5, hy - 2)], '#f9c22b', 3.25)   # orla dourada do capuz
    # mangas e mãos à frente, com a chama
    P.append(Parte(capsula(cx, 15 + resp, cx + 5, 19 + resp, 2.0), ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=4))
    px(P, [(cx + 6, 18 + resp), (cx + 6, 19 + resp), (cx + 7, 19 + resp)], '#cd683d', 4.1)
    fogo(P, cx + 8, 17 + resp - (t % 2), 5, 8, t, z=5, semente=4)
    faiscas(P, cx + 5, 2, cx + 11, 10, t, z=6, n=3, semente=1)
    return desenhar(P, 32, 32)


def _kai(t, boss):
    """Kai, Jogador nº 9 999: rapaz de cabelo preto espetado, casaco azul rasgado, espada curta, ténis gastos;
    no duelo tem os olhos a brilhar azul e uma armadura escura do Sistema (mais armadura no boss)."""
    P = []
    resp = (0, 0, 1, 0)[t]
    cx = 14
    # pernas e ténis
    P.append(Parte(capsula(cx - 2, 22, cx - 3, 28, 1.6), ['#2e222f', '#323353', '#484a77', '#484a77', '#4d65b4'], z=0))
    P.append(Parte(capsula(cx + 2, 22, cx + 2, 28, 1.7), ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d65b4'], z=2))
    for (x, z) in ((cx - 3, 0.1), (cx + 2, 2.1)):
        P.append(Parte(retangulo(x - 1, 29, x + 3, 30), ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=z, plano=True))
        px(P, [(x + 2, 29), (x + 3, 30)], '#e83b3b', z + 0.01)
    # braço de trás
    P.append(Parte(capsula(cx - 2, 15 + resp, cx - 4, 21 + resp, 1.5), AZUL, z=0.5))
    # tronco: casaco azul aberto + armadura escura
    tronco = retangulo(cx - 4, 13 + resp, cx + 4, 23, canto=1)
    P.append(Parte(tronco, AZUL, z=1, volume='cilindro_v'))
    px(P, [(cx - 4, 22), (cx - 2, 23), (cx + 3, 23), (cx - 3, 21)], OUT, 1.05)       # rasgões
    peito = retangulo(cx - 1, 14 + resp, cx + 3, 21, canto=1)
    P.append(Parte(peito, SISTEMA, z=1.2, volume='cilindro_v'))
    px(P, [(cx + 1, 16 + resp), (cx + 1, 17 + resp), (cx, 18 + resp), (cx + 2, 18 + resp)], '#8fd3ff', 1.3)   # linha do Sistema
    if boss:
        P.append(Parte(elipse(cx + 1, 14 + resp, 3.2, 2.2), SISTEMA, z=1.4))   # ombreira
        px(P, [(cx, 13 + resp)], '#8fd3ff', 1.45)
        px(P, [(x, 22) for x in range(cx - 3, cx + 4)], '#4d65b4', 1.3)
    # cabeça: cara, cabelo espetado
    hx, hy = cx + 1, 8 + resp
    cab = elipse(hx, hy, 5, 4.8)
    P.append(Parte(cab, PELE, z=3, luz=0.05))
    cabelo = elipse(hx - 1, hy - 2, 5.4, 3.6) | poligono([(hx - 6, hy + 2), (hx - 5, hy - 2), (hx - 2, hy + 3)])
    for (a, b) in ((-6, -6), (-3, -8), (0, -8), (3, -6), (-8, -2), (5, -4)):
        cabelo |= poligono([(hx - 2, hy - 2), (hx + a, hy + b), (hx + 2, hy - 3)])
    franja = poligono([(hx + 1, hy - 4), (hx + 5, hy - 3), (hx + 4, hy - 1), (hx + 3, hy - 2), (hx + 2, hy)])
    P.append(Parte(cabelo | franja, CABELO_PRETO, z=3.5))
    px(P, [(hx - 2, hy - 5), (hx - 1, hy - 5), (hx + 1, hy - 6)], '#625565', 3.55)   # brilho do cabelo
    ex, ey = hx + 2, hy
    if t == 3:
        px(P, [(ex, ey + 1), (ex + 1, ey + 1)], OUT, 4)
    else:
        px(P, [(ex, ey), (ex + 1, ey), (ex, ey + 1), (ex + 1, ey + 1)], '#4d9be6', 4)
        px(P, [(ex + 1, ey)], '#8fd3ff', 4.05)
        px(P, [(ex, ey)], BRANCO, 4.1)
        px(P, [(ex + 2, ey + 2)], '#8fd3ff', 4.1)   # o brilho do Sistema a escorrer
    px(P, [(ex - 1, ey - 1), (ex, ey - 2), (ex + 1, ey - 2)], OUT, 4)   # sobrolho franzido
    px(P, [(hx + 3, hy + 3), (hx + 4, hy + 3)], '#9e4539', 4)         # boca cerrada
    # cachecol/gola
    P.append(Parte(capsula(cx - 3, 12 + resp, cx + 3, 13 + resp, 1.4), ['#2e222f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=3.6))
    P.append(Parte(capsula(cx - 4, 13 + resp, cx - 6 - (t % 2), 16 + resp, 1.0), ['#2e222f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a'], z=0.4))
    # braço da frente com a espada curta (lâmina com brilho azul)
    mx, my = cx + 5, 19 + resp
    P.append(Parte(capsula(cx + 2, 15 + resp, mx, my, 1.6), AZUL, z=5))
    lam = capsula(mx + 1, my - 1, mx + 9, my - 6, 0.9)
    P.append(Parte(lam, FERRO, z=5.5))
    px(P, [(mx + 3 + (t % 4) * 2, my - 2 - (t % 4))], BRANCO, 5.6)
    P.append(Parte(capsula(mx - 1, my - 2, mx + 2, my + 1, 0.8), OURO, z=5.6))
    P.append(Parte(elipse(mx, my, 1.4, 1.4), PELE, z=5.7))
    if boss:
        # janelinha azul do Sistema a pairar
        wy = 4 + (t % 2)
        P.append(Parte(retangulo(cx - 12, wy, cx - 7, wy + 3), ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'], z=7, plano=True))
        px(P, [(cx - 11, wy + 1), (cx - 10, wy + 1), (cx - 9, wy + 2)], '#8fd3ff', 7.1)
    return desenhar(P, 32, 32)


def kai(t):
    return _kai(t, True)


def kai_duelo_da_historia(t):
    return _kai(t, False)


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
