"""PROPOSTA (ainda não aprovada): os monstros, guardiões e bosses da Região 8 — Reino Assombrado, redesenhados.

Só a animação "parado" (4 quadros), para o utilizador comparar com os antigos e aprovar. NÃO mexe no jogo:
grava apenas em arte/propostas/monstros/r08_reino_assombrado/ (PNG de cada criatura + comparar.gif + depois.gif).

Desenhado por código com o motor do projeto (ferramentas/arte/motor.py), no estilo da Aranha-Mãe e do Ent
Ancião (ferramentas/arte/ent_anciao.py): várias partes com volume, luz de cima à esquerda, contorno #2e222f,
textura (pintas, veios, rachas), olhos com brilho e pormenores próprios em cada criatura.
Todos de lado, virados para a direita, os pés (ou a cauda) no fundo do quadro.

Correr na raiz do repositório:  python3 ferramentas/arte/propostas/r08_reino_assombrado.py
"""
import json
import math
import os
import random
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS  # noqa: E402,F401

OUT = '#2e222f'
REGIAO = 'r08_reino_assombrado'
ORIGEM = os.path.join(RAIZ, 'arte', 'regioes', REGIAO)
DESTINO = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', REGIAO)

# ---------------------------------------------------------------- paleta Resurrect 64 (para verificar)
RESURRECT64 = """2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a
ae2334 e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c
239063 1ebc73 91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77
4d65b4 4d9be6 8fd3ff 45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181
fca790 fdcbb0""".split()

# ---------------------------------------------------------------- rampas (escuro -> claro), só Resurrect 64
ESPECTRO = ['#4d65b4', '#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff']      # fantasmas brancos com sombra azul
VERDE_F = ['#0b5e65', '#0b8a8f', '#30e1b9', '#8ff8e2', '#8ff8e2']       # verde fantasma (#8ff8e2)
VERDE_F2 = ['#0b5e65', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9']
OSSO = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
OSSO_ESC = ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0']
FERRO = ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
FERRO_ESC = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
NEGRO = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
NEGRO_ESC = ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565']
ROXO = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']
ROXO_ESC = ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3']
SANGUE = ['#45293f', '#6e2727', '#ae2334', '#e83b3b', '#f68181']
SANGUE_ESC = ['#2e222f', '#45293f', '#6e2727', '#ae2334', '#e83b3b']
ROSA_N = ['#2e222f', '#45293f', '#831c5d', '#c32454', '#f04f78']        # rosas negras
LILAS = ['#753c54', '#a24b6f', '#cf657f', '#ed8099', '#fdcbb0']
LILAS_CL = ['#a24b6f', '#cf657f', '#ed8099', '#fdcbb0', '#ffffff']
ZOMBI = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']
ZOMBI_ESC = ['#2e222f', '#313638', '#374e4a', '#547e64', '#92a984']
PALIDO = ['#7f708a', '#9babb2', '#c7dcd0', '#fdcbb0', '#ffffff']        # pele de vampiro
TRAPO = ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#ab947a']
TRAPO_ESC = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
COURO = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
MADEIRA = ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
OURO = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
PEDRA = ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0']
PEDRA_ESC = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
CINZA_AZ = ['#323353', '#484a77', '#7f708a', '#9babb2', '#c7dcd0']     # pele de ghoul
CINZA_AZ_ESC = ['#2e222f', '#323353', '#484a77', '#7f708a', '#9babb2']
PALHA = ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86']
CAULE = ['#2e222f', '#165a4c', '#239063', '#1ebc73', '#91db69']
AZUL = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']


def esc(r):
    """A mesma rampa um tom mais escura (membros do lado de lá)."""
    return [r[0], r[0], r[1], r[2], r[3]]


# ---------------------------------------------------------------- ajudas de desenho

def px(P, pts, cor, z):
    P.append(Parte({(int(round(x)), int(round(y))) for x, y in pts}, None, z=z, separar=False, cor=cor))


def _h(x, y, s):
    v = (x * 73856093) ^ (y * 19349663) ^ (s * 83492791)
    v = (v ^ (v >> 13)) * 1274126177
    return (v ^ (v >> 16)) & 0xffff


def miolo(m):
    """Os píxeis de dentro de uma máscara (sem a borda), para a textura não estragar o contorno."""
    return {(x, y) for (x, y) in m if all((x + a, y + b) in m for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))}


def pintas(P, m, cor, z, semente, dens=8, o=0, so_miolo=True):
    """Pintas (sombra, manchas, podre, ferrugem) espalhadas numa máscara. `o` = quanto a parte subiu/desceu."""
    alvo = miolo(m) if so_miolo else m
    pts = [(x, y) for (x, y) in alvo if _h(x, y - o, semente) % 100 < dens]
    px(P, pts, cor, z)


def brilhos_pele(P, m, cor, z, semente, dens=6, o=0):
    """Pintas claras só na metade de cima-esquerda (a luz vem de lá)."""
    if not m:
        return
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    pts = [(x, y) for (x, y) in miolo(m) if (x - cx) + (y - cy) < -1 and _h(x, y - o, semente) % 100 < dens]
    px(P, pts, cor, z)


def olho(P, x, y, cor, z, tam=1):
    """Olho que brilha: tam=1 -> 2×1 com ponto branco; tam=2 -> 2×2 com ponto branco; tam=3 -> 3×2."""
    x, y = int(x), int(y)
    if tam == 1:
        px(P, [(x, y)], cor, z)
        px(P, [(x + 1, y)], '#ffffff', z + 0.01)
    elif tam == 2:
        px(P, [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)], cor, z)
        px(P, [(x + 1, y)], '#ffffff', z + 0.01)
    else:
        px(P, [(x + i, y + j) for i in range(3) for j in range(2)], cor, z)
        px(P, [(x + 2, y)], '#ffffff', z + 0.01)


def olho_fechado(P, x, y, z, larg=2, cor=OUT):
    px(P, [(int(x) + i, int(y) + 1) for i in range(larg)], cor, z)


def corda(pts_xy, r=0.6):
    """Linha fina entre vários pontos (cordas, correntes, hastes finas)."""
    m = set()
    for (a, b) in zip(pts_xy, pts_xy[1:]):
        m |= capsula(a[0], a[1], b[0], b[1], r)
    return m


def linha(x1, y1, x2, y2):
    """Linha de 1 píxel (Bresenham)."""
    pts = []
    x1, y1, x2, y2 = int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2))
    dx, dy = abs(x2 - x1), -abs(y2 - y1)
    sx, sy = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
    e = dx + dy
    while True:
        pts.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * e
        if e2 >= dy:
            e += dy
            x1 += sx
        if e2 <= dx:
            e += dx
            y1 += sy
    return pts


def fita(x0, y0, comp, larg, curva, fase, amp=1.2, ondas=1.0, fim=0.25):
    """Uma "fita" orgânica (cauda de fantasma, cabelo ao vento, capa rasgada): bolas cada vez mais pequenas
    ao longo de uma curva que desce (comp) e se dobra para trás (curva < 0 = para a esquerda), a ondular."""
    m = set()
    n = max(6, int(comp * 1.5))
    for i in range(n + 1):
        t = i / n
        x = x0 + curva * t * t + math.sin(t * math.pi * 2 * ondas + fase) * amp * t
        y = y0 + comp * t
        r = larg * (1 - t * (1 - fim))
        m |= elipse(x, y, max(0.6, r), max(0.6, r))
    return m


def rasgar(m, semente, prof=2, so_baixo=True, dens=40):
    """Rasga a borda de baixo (trapos, capas rasgadas, véus): tira pedaços com alturas ao acaso."""
    m = set(m)
    if not m:
        return m
    cols = {}
    for (x, y) in m:
        cols[x] = max(cols.get(x, -999), y)
    for x, yb in cols.items():
        k = _h(x // 2, 7, semente) % 100
        if k < dens:
            corte = 1 + _h(x, 3, semente) % prof
            for d in range(corte):
                m.discard((x, yb - d))
    return m


def mosaico(m, celula, semente):
    """Divide uma máscara em pedaços de vidro (Voronoi) e devolve (pedaços, linhas de chumbo)."""
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    rnd = random.Random(semente)
    sem = []
    for gy in range(min(ys), max(ys) + 1, celula):
        for gx in range(min(xs), max(xs) + 1, celula):
            sem.append((gx + rnd.uniform(0, celula), gy + rnd.uniform(0, celula)))
    dono = {}
    for (x, y) in m:
        d = sorted(((x - a) ** 2 + (y - b) ** 2, i) for i, (a, b) in enumerate(sem))
        dono[(x, y)] = d[0][1]
    pedacos = {}
    chumbo = set()
    for (x, y), i in dono.items():
        if any(dono.get((x + a, y + b), i) != i for a, b in ((1, 0), (0, 1))):
            chumbo.add((x, y))
        else:
            pedacos.setdefault(i, set()).add((x, y))
    return list(pedacos.values()), chumbo


def particulas(P, cx, cy, raio, f, cores, n, semente, z=80, subir=True):
    """Pontinhos de luz/névoa à volta (sobem e piscam com o quadro)."""
    rnd = random.Random(semente)
    for i in range(n):
        x = cx + rnd.uniform(-raio, raio)
        y0 = cy + rnd.uniform(-raio * 0.6, raio * 0.6)
        vel = rnd.choice((1, 1, 2))
        y = y0 - (f * vel if subir else 0)
        if (i + f) % 4 == 3:
            continue
        px(P, [(x, y)], cores[(i + f) % len(cores)], z)


def dentes(P, x1, x2, y, z, cor='#ffffff', passo=2, para_baixo=True):
    pts = [(x, y) for x in range(int(x1), int(x2) + 1, passo)]
    px(P, pts, cor, z)


# ================================================================ MONSTROS 32×32

def fantasma(f):
    """Lençol branco a flutuar, cauda a ondular para trás, bracinhos gelados, boca em "o", corrente partida."""
    P = []
    o = [0, -1, -2, -1][f]
    fase = f * math.pi / 2
    cab = elipse(17, 11 + o, 7.5, 7.5)
    corpo = poligono([(9.5, 12 + o), (24.5, 12 + o), (24, 19 + o), (21, 23 + o), (14, 25 + o), (10, 21 + o)])
    cauda = fita(14, 20 + o, 8, 4.2, -9, fase, amp=1.3, ondas=1.2, fim=0.15)
    m = cab | corpo | cauda
    P.append(Parte(m, ESPECTRO, z=2))
    # véu: pregas mais escuras e fios claros
    for i, x in enumerate((12, 15, 19)):
        px(P, [(x + int(math.sin(y * 0.6 + fase + i)), y + o) for y in range(17, 23 - i)], '#8fd3ff', 2.1)
    brilhos_pele(P, cab, '#ffffff', 2.05, 3, 10, o)
    # pontas da cauda (fiapos que se soltam)
    px(P, [(5 + int(math.sin(fase) * 1.5), 29 + o), (7 + int(math.cos(fase)), 30 + o)], '#8fd3ff', 2.2)
    # braço de trás e da frente (bracinhos que tocam gelado)
    P.append(Parte(capsula(10, 17 + o, 6, 20 + o + (f % 2), 1.6), esc(ESPECTRO), z=1))
    mb = capsula(21, 18 + o, 26.5, 20 + o - (f % 2), 1.6)
    P.append(Parte(mb, ESPECTRO, z=6))
    # corrente partida no pulso de trás
    px(P, [(5, 22 + o), (5, 24 + o), (4, 26 + o)], '#7f708a', 0.5)
    px(P, [(5, 23 + o), (4, 25 + o)], '#c7dcd0', 0.5)
    # cara: dois olhos fundos com brilho verde fantasma, boca em "o"
    for ex in (19, 22):
        px(P, [(ex, 8 + o), (ex + 1, 8 + o), (ex, 9 + o), (ex + 1, 9 + o), (ex, 10 + o), (ex + 1, 10 + o)], OUT, 8)
        if f == 3:
            px(P, [(ex, 8 + o), (ex + 1, 8 + o), (ex, 10 + o), (ex + 1, 10 + o)], '#c7dcd0', 8.2)
        else:
            px(P, [(ex + 1, 9 + o)], '#8ff8e2', 8.1)
            px(P, [(ex + 1, 8 + o)], '#ffffff', 8.1)
    px(P, elipse(21.5, 13.5 + o, 1.5, 1.6 + (f % 2) * 0.5), OUT, 8)
    px(P, [(21, 14 + o)], '#484a77', 8.1)
    # pontinhos de névoa fria
    particulas(P, 16, 18, 12, f, ['#8ff8e2', '#8fd3ff', '#ffffff'], 6, 11)
    return desenhar(P, 32, 32)


def zombie(f):
    """Morto-vivo curvado: um braço esticado, camisa rasgada com costelas à vista, pontos na testa, um olho a brilhar."""
    P = []
    b = [0, 0, 1, 1][f]
    sw = [0, 1, 1, 0][f]
    # pernas (calças rasgadas) e pés descalços
    P.append(Parte(capsula(13, 22, 12, 28, 1.8), TRAPO_ESC, z=0, volume='cilindro_v'))
    P.append(Parte(capsula(12, 28.5, 9.5, 29.5, 1.2), ZOMBI_ESC, z=0.1))
    P.append(Parte(capsula(17, 22, 18, 27, 1.9), esc(TRAPO), z=3, volume='cilindro_v'))
    P.append(Parte(capsula(18, 27, 18.5, 29, 1.3), ZOMBI, z=3.05))
    P.append(Parte(capsula(18.5, 29, 21.5, 29.5, 1.1), ZOMBI, z=3.1))
    px(P, [(16, 26), (18, 25)], '#2e222f', 3.2)     # rasgões
    # braço de trás pendurado
    P.append(Parte(capsula(12, 14 + b, 10.5, 21 + b, 1.4), ZOMBI_ESC, z=0.5))
    P.append(Parte(capsula(10.5, 21 + b, 10, 23 + b, 0.7), ZOMBI_ESC, z=0.6))
    # tronco curvado (camisa rasgada, azul desbotado)
    tronco = poligono([(9.5, 14 + b), (16, 11 + b), (21, 13.5 + b), (20, 23), (10.5, 23)])
    tronco = rasgar(tronco, 5, prof=2, dens=55)
    camisa = ['#2e222f', '#323353', '#484a77', '#7f708a', '#9babb2']
    P.append(Parte(tronco, camisa, z=2, volume='cilindro_v'))
    pintas(P, tronco, '#4c3e24', 2.1, 9, 9, b)      # nódoas de terra
    # rasgão com costelas à vista
    px(P, [(15, 16 + b), (16, 16 + b), (17, 16 + b), (18, 16 + b), (15, 18 + b), (16, 18 + b), (17, 18 + b)], ZOMBI[2], 2.2)
    px(P, [(15, 17 + b), (16, 17 + b), (17, 17 + b), (18, 17 + b), (16, 19 + b)], '#c7dcd0', 2.25)
    # suspensório e cinto de corda
    px(P, linha(13, 12 + b, 14, 21), '#966c6c', 2.3)
    px(P, [(x, 21) for x in range(11, 20)], '#966c6c', 2.3)
    px(P, [(x, 21) for x in range(12, 20, 3)], '#4c3e24', 2.31)
    # cabeça (para a frente e para baixo)
    hx, hy = 20, 9 + b
    cab = elipse(hx, hy, 4.6, 4.4) | elipse(hx + 2.5, hy + 2.5, 2.4, 1.8)   # + queixo caído
    P.append(Parte(cab, ZOMBI, z=4, luz=0.1))
    pintas(P, cab, '#374e4a', 4.1, 21, 10, b)
    # cabelo ralo despenteado (só atrás e em cima)
    cabelo = {p for p in elipse(hx - 1, hy - 1.8, 4.6, 3.4) if p[0] <= hx + 1 and p[1] <= hy - 3}
    cabelo |= {p for p in elipse(hx - 3.6, hy, 1.4, 2.4)}
    cabelo |= {(int(hx) - 5, int(hy) - 4), (int(hx) - 1, int(hy) - 6), (int(hx) - 3, int(hy) - 6)}
    P.append(Parte(cabelo, NEGRO, z=4.2, separar=False))
    # pontos na testa
    px(P, [(hx + 1, hy - 3), (hx + 2, hy - 2), (hx + 3, hy - 3)], OUT, 4.3)
    # olho: brilha amarelo (pisca no último quadro)
    if f == 3:
        olho_fechado(P, hx + 2, hy - 1, 4.4)
    else:
        px(P, [(hx + 2, hy - 1), (hx + 3, hy - 1), (hx + 2, hy)], OUT, 4.4)
        px(P, [(hx + 3, hy)], '#d5e04b', 4.45)
        px(P, [(hx + 3, hy - 1)], '#fbff86', 4.46)
    # nariz podre e boca aberta com dentes tortos
    px(P, [(hx + 5, hy + 1)], ZOMBI[1], 4.4)
    px(P, [(hx + 2, hy + 3), (hx + 3, hy + 3), (hx + 4, hy + 3), (hx + 3, hy + 4)], OUT, 4.4)
    px(P, [(hx + 2, hy + 2), (hx + 4, hy + 2)], '#c7dcd0', 4.5)
    # orelha meio comida
    px(P, [(hx - 2, hy + 1), (hx - 2, hy + 2)], ZOMBI[1], 4.5)
    # braço da frente esticado, mão em garra
    om = (18, 14 + b)
    mao = (26.5, 15 + b + sw)
    P.append(Parte(capsula(*om, *mao, 1.5), ZOMBI, z=6, volume='cilindro_h'))
    P.append(Parte(capsula(om[0] - 0.5, om[1], om[0] + 3, om[1] + 0.5, 2.0), camisa, z=6.1))   # manga rasgada
    px(P, [(om[0] + 4, om[1] + 1)], camisa[2], 6.12)
    for (dx, dy) in ((2, -1), (2.5, 0.5), (1.5, 2)):
        P.append(Parte(capsula(mao[0], mao[1], mao[0] + dx, mao[1] + dy, 0.6), ZOMBI, z=6.2))
    px(P, [(23, 15 + b + (1 if sw else 0))], ZOMBI[1], 6.3)
    # moscas
    for i in range(2):
        a = f * 1.6 + i * 3
        px(P, [(9 + math.cos(a) * 3 + i * 3, 4 + math.sin(a) * 2)], OUT, 9)
    return desenhar(P, 32, 32)


def cavaleiro_esqueleto(f):
    """Esqueleto de armadura velha: meio elmo com pluma, crânio com olho vermelho, escudo, espada, costelas à vista."""
    P = []
    b = [0, 0, 1, 1][f]
    ARM = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
    # escudo às costas (atrás de tudo)
    esc_m = poligono([(5.5, 13 + b), (12.5, 13 + b), (12.5, 19 + b), (9, 24 + b), (5.5, 19 + b)])
    P.append(Parte(esc_m, ROXO, z=0, plano=True))
    px(P, [(9, y + b) for y in range(14, 22)], '#f9c22b', 0.1)
    px(P, [(7, 16 + b), (8, 16 + b), (10, 16 + b), (11, 16 + b)], '#f9c22b', 0.1)
    px(P, [(6, 14 + b), (11, 20 + b)], '#45293f', 0.12)       # amolgadelas
    # pernas: ossos com caneleiras de ferro
    for (xh, xf, z) in ((13, 12, 1), (16.5, 17, 3)):
        P.append(Parte(capsula(xh, 22, xh, 25, 0.9), OSSO if z > 2 else OSSO_ESC, z=z))
        P.append(Parte(capsula(xh, 25.5, xf, 28.5, 1.5), ARM if z > 2 else esc(ARM), z=z + 0.1, volume='cilindro_v'))
        P.append(Parte(capsula(xf, 29, xf + 3, 29.5, 1.1), ARM if z > 2 else esc(ARM), z=z + 0.2))
    # braço de trás (osso)
    P.append(Parte(capsula(12, 14 + b, 11, 20 + b, 0.9), OSSO_ESC, z=1.5))
    # bacia, coluna e costelas (à vista por baixo do peitoral)
    P.append(Parte(elipse(14.5, 21.5, 3, 1.6), OSSO, z=2))
    P.append(Parte(capsula(14, 17 + b, 14, 21, 0.7), OSSO, z=2.1))
    for y in (17, 19):
        P.append(Parte(capsula(12, y + b, 17, y + 1 + b, 0.6), OSSO, z=2.2))
    # tabardo roxo rasgado por trás
    tab = rasgar(poligono([(10.5, 13 + b), (13, 13 + b), (13, 24), (10.5, 24)]), 3, prof=2, dens=60)
    P.append(Parte(tab, ROXO_ESC, z=1.8))
    # peitoral (só em cima) com ferrugem e rebites
    peito = poligono([(10.5, 11.5 + b), (17, 11.5 + b), (18.5, 13.5 + b), (17, 16 + b), (11, 16 + b)])
    P.append(Parte(peito, ARM, z=3))
    pintas(P, peito, '#9e4539', 3.1, 4, 14, b)
    px(P, [(12, 13 + b), (15, 15 + b)], '#c7dcd0', 3.1)
    # crânio
    hx, hy = 17, 7.5 + b
    P.append(Parte(elipse(hx, hy, 3.6, 3.4), OSSO, z=4))
    P.append(Parte(retangulo(int(hx), int(hy) + 2, int(hx) + 3, int(hy) + 4), OSSO, z=4.1, plano=True))   # maxilar
    px(P, [(int(hx) + 1, int(hy) + 3), (int(hx) + 3, int(hy) + 3)], OUT, 4.2)                        # dentes
    px(P, [(int(hx) + 3, int(hy) + 1)], OUT, 4.2)                                                    # nariz
    px(P, [(int(hx) + 1, int(hy) - 1), (int(hx) + 2, int(hy) - 1), (int(hx) + 1, int(hy)), (int(hx) + 2, int(hy))], OUT, 4.3)
    if f != 3:
        px(P, [(int(hx) + 2, int(hy))], '#e83b3b', 4.4)
        px(P, [(int(hx) + 2, int(hy) - 1)], '#f68181', 4.4)
    px(P, [(int(hx) - 1, int(hy) + 1), (int(hx) - 2, int(hy) + 2)], '#7f708a', 4.3)                 # racha
    # meio elmo (calote) e pluma vermelha
    calote = {p for p in elipse(hx - 0.6, hy - 0.4, 4.3, 4.0) if p[1] <= hy - 2.5 or (p[0] <= hx - 3 and p[1] <= hy + 1)}
    P.append(Parte(calote, ARM, z=5))
    px(P, [(int(hx) - 2, int(hy) - 3)], '#c7dcd0', 5.1)
    pl = capsula(hx - 1, hy - 4.5, hx - 6, hy - 3 + (f % 2), 1.4) | capsula(hx - 6, hy - 3 + (f % 2), hx - 8, hy + (f % 2), 1.0)
    P.append(Parte(pl, SANGUE, z=4.5))
    # ombreira
    P.append(Parte(elipse(15.5, 12.5 + b, 2.6, 2), ARM, z=5.5))
    px(P, [(15, 12 + b)], '#c7dcd0', 5.6)
    # braço da frente (osso) com espada levantada
    P.append(Parte(capsula(16, 13.5 + b, 18, 17.5 + b, 0.9), OSSO, z=6))
    P.append(Parte(capsula(18, 17.5 + b, 21, 16.5 + b, 0.9), OSSO, z=6.1))
    lam = capsula(22.5, 14 + b, 26.5, 4 + b, 1.2)
    P.append(Parte(lam, FERRO, z=6.3, volume='cilindro_h'))
    px(P, linha(22, 13 + b, 25, 6 + b), '#ffffff', 6.31)
    P.append(Parte(capsula(19.5, 14.5 + b, 24, 16.5 + b, 0.8), OURO, z=6.4))         # guarda
    P.append(Parte(elipse(21.5, 17 + b, 1.4, 1.2), OSSO, z=6.5))                      # mão
    px(P, [(21, 18 + b), (20, 19 + b)], '#966c6c', 6.6)                               # punho
    if f == 1:
        px(P, [(26, 5 + b)], '#ffffff', 7)
        px(P, [(25, 5 + b), (27, 5 + b), (26, 4 + b), (26, 6 + b)], '#c7dcd0', 7)
    return desenhar(P, 32, 32)


def condessa_sangria(f):
    """Vampira de vestido vermelho armado e renda preta, gola alta, coque com rosa, leque preto aberto."""
    P = []
    b = [0, 0, 1, 1][f]
    lq = [0, 1, 0, -1][f]
    # gola alta de vampira (atrás da cabeça)
    gola = poligono([(10, 5 + b), (13, 9 + b), (14, 13 + b), (11, 13 + b), (9, 9 + b)])
    P.append(Parte(gola, NEGRO, z=0.5))
    px(P, [(11, 8 + b), (12, 10 + b), (12, 11 + b)], '#ae2334', 0.6)
    # saia em sino com renda preta em baixo
    saia = poligono([(12, 17 + b), (19, 17 + b), (24.5, 29.5), (7.5, 29.5)])
    P.append(Parte(saia, SANGUE, z=1, volume='cilindro_v'))
    for i, x in enumerate(range(10, 23, 4)):           # pregas
        px(P, linha(15 + (x - 15) * 0.3, 19 + b, x, 28), '#6e2727', 1.1)
    renda = {(x, y) for x in range(8, 25) for y in (28, 29) if (x + y) % 2 == 0 or y == 29}
    renda &= saia | {(x, 29) for x in range(8, 25)}
    px(P, renda, '#2e222f', 1.2)
    px(P, [(x, 30) for x in range(8, 25) if x % 3 == 0], '#2e222f', 1.2)
    # corpete com atilhos
    corp = poligono([(12.5, 11 + b), (18, 11 + b), (19, 17.5 + b), (12, 17.5 + b)])
    P.append(Parte(corp, SANGUE, z=2))
    px(P, [(16, 12 + b), (17, 13 + b), (16, 14 + b), (17, 15 + b), (16, 16 + b)], OUT, 2.1)
    px(P, [(x, 17 + b) for x in range(12, 20)], OUT, 2.2)                 # cinta preta
    px(P, [(18, 17 + b)], '#f9c22b', 2.3)
    # braço de trás
    P.append(Parte(capsula(13, 12 + b, 12, 18 + b, 1.2), esc(SANGUE), z=1.5))
    # cabeça pálida, coque preto com rosa
    hx, hy = 18, 7 + b
    P.append(Parte(elipse(hx, hy, 4.0, 4.1), PALIDO, z=4, luz=0.15))
    cab = {p for p in elipse(hx - 0.6, hy - 1, 4.5, 3.9) if p[1] <= hy - 3 or p[0] <= hx - 2.5}
    cab |= elipse(hx - 4.5, hy - 3.5, 2.6, 2.4)
    P.append(Parte(cab, NEGRO, z=4.5, separar=False))
    px(P, [(hx - 4, hy - 5), (hx - 5, hy - 4), (hx - 1, hy - 4)], '#625565', 4.6)
    px(P, [(hx - 7, hy - 2), (hx - 6, hy - 2), (hx - 7, hy - 1)], '#e83b3b', 4.7)               # rosa no coque
    px(P, [(hx - 6, hy - 1)], '#6e2727', 4.7)
    # cara
    if f == 3:
        olho_fechado(P, hx + 1, hy - 1, 4.8)
    else:
        px(P, [(hx + 1, hy - 1), (hx + 1, hy)], OUT, 4.8)
        px(P, [(hx + 2, hy)], '#e83b3b', 4.8)
        px(P, [(hx + 2, hy - 1)], '#f68181', 4.81)
    px(P, [(hx + 3, hy + 2)], '#ae2334', 4.8)                                  # lábios
    px(P, [(hx + 3, hy + 3)], '#ffffff', 4.8)                                  # presa
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2)], OUT, 4.8)                      # sobrancelha
    # colar de rubi
    px(P, [(15, 11 + b), (16, 12 + b), (17, 12 + b)], '#f9c22b', 4.9)
    px(P, [(18, 12 + b)], '#e83b3b', 4.95)
    # braço da frente com o leque aberto à frente do peito
    P.append(Parte(capsula(16, 12 + b, 18, 16 + b, 1.2), SANGUE, z=6))
    P.append(Parte(capsula(18, 16 + b, 21, 15 + b, 1.0), PALIDO, z=6.1))
    lcx, lcy = 21.5, 17 + b
    leque = set()
    for k in range(-4, 5):
        ang = -math.pi / 2 + 0.55 + k * 0.17 + lq * 0.06
        leque |= set(linha(lcx, lcy, lcx + math.cos(ang) * 6.5, lcy + math.sin(ang) * 6.5))
    P.append(Parte(leque, NEGRO, z=7, plano=True))
    for k in range(-4, 5, 2):
        ang = -math.pi / 2 + 0.55 + k * 0.17 + lq * 0.06
        px(P, linha(lcx, lcy, lcx + math.cos(ang) * 5, lcy + math.sin(ang) * 5), '#6b3e75', 7.1)
    for k in (-4, 0, 4):
        ang = -math.pi / 2 + 0.55 + k * 0.17 + lq * 0.06
        px(P, [(lcx + math.cos(ang) * 6, lcy + math.sin(ang) * 6)], '#e83b3b', 7.2)
    P.append(Parte(elipse(21, 16.5 + b, 1.2, 1.1), PALIDO, z=7.3))   # dedos a segurar
    return desenhar(P, 32, 32)


def livro_possuido(f):
    """Grimório que voa a bater as capas: capas roxas com cantos de ouro, páginas com dentes, olho e fita-língua."""
    P = []
    o = [0, -1, -1, 0][f]
    ab = [5, 7, 8, 6][f]                        # abertura da "boca"
    hx, hy = 8, 17 + o                          # a lombada (atrás, à esquerda)
    cima = poligono([(hx, hy - 1), (hx + 2, hy - 3), (25, hy - 3 - ab), (26.5, hy - 1 - ab), (hx + 2, hy + 0.5)])
    baixo = poligono([(hx, hy + 1), (hx + 2, hy + 3), (25, hy + 4 + ab * 0.5), (25, hy + 6 + ab * 0.5), (hx + 2, hy + 4.5)])
    # páginas: leque branco entre as capas, com dentes na ponta
    pag = poligono([(hx + 2, hy), (24, hy - 2 - ab + 1), (24, hy + 3 + ab * 0.5)])
    P.append(Parte(pag, ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=1, plano=True))
    for k in range(1, 4):                       # linhas das folhas
        t = k / 4
        px(P, linha(hx + 3, hy, 23, hy - 2 - ab + 1 + (ab * 1.5 + 4) * t), '#9babb2', 1.1)
    # boca escura dentro das páginas
    boca = poligono([(hx + 9, hy + 0.5), (24, hy - ab + 1), (24, hy + 2 + ab * 0.4)])
    P.append(Parte(boca, ['#2e222f', '#45293f', '#45293f', '#6b3e75', '#6b3e75'], z=1.5, plano=True))
    for i in range(3):                          # dentes de papel
        x = 21 - i * 3
        yt = hy - ab + 1 + i * (ab / 6)
        px(P, [(x, yt + 1), (x + 1, yt + 1), (x, yt + 2)], '#ffffff', 1.6)
        yb = hy + 2 + ab * 0.4 - i * (ab / 10)
        px(P, [(x, yb - 1), (x + 1, yb - 1), (x + 1, yb - 2)], '#ffffff', 1.6)
    # fita marcadora a fazer de língua
    lng = fita(hx + 12, hy + 1, 7, 0.9, 3, f * 1.4, amp=1.0, fim=0.8)
    P.append(Parte(lng, SANGUE, z=1.7))
    # capas
    P.append(Parte(baixo, ROXO_ESC, z=2, plano=True))
    P.append(Parte(cima, ROXO, z=3, plano=True))
    # cantoneiras de ouro e fecho
    px(P, [(24, hy - 2 - ab), (25, hy - 2 - ab), (25, hy - 1 - ab)], '#f9c22b', 3.1)
    px(P, [(24, hy + 5 + int(ab * 0.5)), (24, hy + 4 + int(ab * 0.5))], '#f79617', 2.1)
    # símbolo na capa: um olho que pisca
    ex, ey = 17, hy - 2 - int(ab * 0.55)
    if f == 2:
        px(P, [(ex - 1, ey), (ex, ey), (ex + 1, ey)], OUT, 3.2)
    else:
        px(P, [(ex - 1, ey), (ex, ey), (ex + 1, ey), (ex, ey - 1), (ex, ey + 1)], '#f9c22b', 3.2)
        px(P, [(ex, ey)], OUT, 3.3)
        px(P, [(ex + 1, ey - 1)], '#ffffff', 3.3)
    # lombada com nervuras
    lomb = capsula(hx, hy - 1, hx, hy + 2, 1.6)
    P.append(Parte(lomb, ROXO_ESC, z=3.5))
    px(P, [(hx - 1, hy), (hx - 1, hy + 2)], '#f79617', 3.6)
    # página solta a voar e faíscas mágicas
    pgx, pgy = 4 + f, 8 - f + o
    px(P, [(pgx, pgy), (pgx + 1, pgy), (pgx, pgy + 1), (pgx + 1, pgy + 1)], '#c7dcd0', 4)
    px(P, [(pgx + 1, pgy)], '#ffffff', 4.1)
    particulas(P, 18, 16, 10, f, ['#a884f3', '#eaaded', '#f9c22b'], 5, 4)
    return desenhar(P, 32, 32)


def vampiro(f):
    """Vampiro elegante: capa preta forrada a vermelho com gola alta, cabelo em bico, presas, colete vermelho."""
    P = []
    b = [0, 0, 1, 1][f]
    w = [0, 1, 2, 1][f]
    # capa (atrás), a abanar, com o forro vermelho à vista
    capa = poligono([(9, 9 + b), (15, 10 + b), (15, 27), (12, 29.5), (3 - w * 0.6, 29.5), (6, 19)])
    capa = rasgar(capa, 8, prof=2, dens=45)
    P.append(Parte(capa, NEGRO, z=0))
    forro = poligono([(10, 12 + b), (14, 12 + b), (14.5, 27), (11, 29.5), (8 - w * 0.3, 29.5)]) & capa
    P.append(Parte(forro, SANGUE_ESC, z=0.05))
    px(P, linha(11, 14 + b, 10 - w * 0.3, 27), '#45293f', 0.06)
    # gola alta (forro vermelho)
    gola = poligono([(10, 2 + b), (14, 7 + b), (14, 11 + b), (11, 11 + b), (8.5, 6 + b)])
    P.append(Parte(gola, SANGUE, z=0.5))
    px(P, linha(10, 3 + b, 12, 10 + b), '#45293f', 0.6)
    # pernas finas de calça preta e botas
    P.append(Parte(capsula(14, 20, 13, 28.5, 1.4), NEGRO_ESC, z=1, volume='cilindro_v'))
    P.append(Parte(capsula(13, 29, 15.5, 29.5, 1.0), NEGRO_ESC, z=1.1))
    P.append(Parte(capsula(16.5, 20, 17.5, 28.5, 1.5), NEGRO, z=3, volume='cilindro_v'))
    P.append(Parte(capsula(17.5, 29, 20.5, 29.5, 1.0), NEGRO, z=3.1))
    px(P, [(20, 29)], '#9babb2', 3.2)
    # casaca preta com colete vermelho e lenço branco
    tronco = poligono([(12, 10 + b), (18, 10 + b), (19, 19 + b), (18.5, 22), (12.5, 22)])
    P.append(Parte(tronco, NEGRO, z=2))
    P.append(Parte(poligono([(16, 11 + b), (18.5, 11 + b), (19, 18 + b), (16.5, 18 + b)]), SANGUE, z=2.1, plano=True))
    px(P, [(18, 11 + b), (18, 12 + b), (17, 12 + b)], '#ffffff', 2.2)        # lenço
    px(P, [(17, 15 + b), (17, 17 + b)], '#f9c22b', 2.3)                        # botões
    px(P, [(x, 22) for x in range(13, 19, 2)], '#3e3546', 2.2)                 # abas da casaca
    # braço de trás
    P.append(Parte(capsula(13, 12 + b, 12, 18 + b, 1.2), NEGRO_ESC, z=1.5))
    # cabeça pálida, cabelo preto puxado para trás em bico
    hx, hy = 17, 6.5 + b
    P.append(Parte(elipse(hx, hy, 3.9, 4.0), PALIDO, z=4, luz=0.15))
    cab = {p for p in elipse(hx - 0.8, hy - 1.2, 4.3, 3.6) if p[1] <= hy - 3 or p[0] <= hx - 2.5}
    cab |= {(int(hx) + 1, int(hy) - 3), (int(hx), int(hy) - 3)}     # o bico na testa
    cab |= capsula(hx - 4, hy - 1, hx - 4.5, hy + 2.5, 1.1)
    P.append(Parte(cab, NEGRO, z=4.5, separar=False))
    px(P, [(hx - 2, hy - 4), (hx - 3, hy - 3), (hx, hy - 5)], '#625565', 4.6)
    px(P, [(hx - 1, hy), (hx - 1, hy + 1), (hx - 2, hy - 1)], '#9babb2', 4.55)    # orelha pontiaguda
    if f == 3:
        olho_fechado(P, hx + 1, hy - 1, 4.8)
    else:
        px(P, [(hx + 1, hy - 1), (hx + 1, hy)], OUT, 4.8)
        px(P, [(hx + 2, hy)], '#e83b3b', 4.8)
        px(P, [(hx + 2, hy - 1)], '#f68181', 4.81)
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2), (hx + 3, hy - 1)], OUT, 4.8)     # sobrolho zangado
    px(P, [(hx + 2, hy + 2), (hx + 3, hy + 2)], '#6e2727', 4.8)                 # boca
    px(P, [(hx + 3, hy + 3)], '#ffffff', 4.85)                                  # presa
    # braço da frente dobrado, mão em garra
    P.append(Parte(capsula(17, 12 + b, 20, 16 + b, 1.3), NEGRO, z=6))
    P.append(Parte(capsula(20, 16 + b, 23, 14 + b, 1.1), NEGRO, z=6.1))
    for (dx, dy) in ((2, -1), (2, 1), (1, 2)):
        P.append(Parte(capsula(23.5, 14 + b, 23.5 + dx, 14 + b + dy, 0.5), PALIDO, z=6.2))
    px(P, [(23, 13 + b)], '#e83b3b', 6.3)                                      # anel de rubi
    # morcego pequenino a voar
    mx, my = 26 - f, 5 + (f % 2)
    asa = [(mx - 1, my - 1), (mx + 1, my - 1)] if f % 2 else [(mx - 1, my + 1), (mx + 1, my + 1)]
    px(P, [(mx, my), (mx - 2, my), (mx + 2, my)] + asa, '#2e222f', 9)
    px(P, [(mx, my)], '#45293f', 9.1)
    return desenhar(P, 32, 32)


def banshee(f):
    """Espírito de mulher: cabelo comprido a esvoaçar, véu cor-de-rosa que acaba em fiapos, mãos na cara, lágrimas."""
    P = []
    o = [0, -1, -2, -1][f]
    fase = f * math.pi / 2
    CAB = ['#753c54', '#a24b6f', '#eaaded', '#ffffff', '#ffffff']
    # cabelo comprido para trás (uma massa a ondular e uma madeixa escura por trás)
    m2 = fita(13, 7 + o, 15, 2.6, -8, fase + 1.5, amp=1.8, ondas=1.0, fim=0.3)
    P.append(Parte(m2, ['#45293f', '#753c54', '#a24b6f', '#cf657f', '#cf657f'], z=0))
    m1 = fita(15, 5 + o, 13, 3.4, -11, fase, amp=1.6, ondas=0.9, fim=0.25)
    P.append(Parte(m1, CAB, z=0.5))
    for k in range(3):   # fios do cabelo
        px(P, [(15 - k - t * 0.6 + math.sin(t * 0.5 + fase) * 1.2, 6 + o + t) for t in range(2, 11, 2)], '#cf657f', 0.6)
    # véu/corpo em fiapos
    corpo = poligono([(13.5, 10 + o), (20, 10 + o), (22, 17 + o), (19, 23 + o), (13, 23 + o), (12, 16 + o)])
    corpo |= fita(16, 20 + o, 8, 3.6, -5, fase + 1, amp=1.5, ondas=1.3, fim=0.15)
    corpo |= fita(19.5, 20 + o, 7, 2.0, -2, fase + 2.5, amp=1.2, ondas=1.0, fim=0.2)
    P.append(Parte(corpo, LILAS_CL, z=2))
    for k in range(3):
        px(P, [(14 + k * 2 + int(math.sin(y * 0.5 + fase + k)), y + o) for y in range(15, 22)], '#cf657f', 2.1)
    # cabeça
    hx, hy = 18, 6.5 + o
    PELE = ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff']
    P.append(Parte(elipse(hx, hy, 3.6, 3.8), PELE, z=4))
    P.append(Parte({p for p in elipse(hx - 0.8, hy - 1, 4.1, 3.4) if p[1] <= hy - 3 or p[0] <= hx - 2},
                   CAB, z=4.5, separar=False))
    # cara: olho fundo, lágrimas, boca a chorar
    px(P, [(hx + 1, hy - 1), (hx + 2, hy - 1), (hx + 1, hy), (hx + 2, hy)], OUT, 5)
    px(P, [(hx + 2, hy)], '#8ff8e2', 5.1)
    px(P, [(hx + 1, hy - 2), (hx + 2, hy - 3)], '#7f708a', 5)                 # sobrancelha triste
    px(P, elipse(hx + 2.2, hy + 2.6, 0.9, 1.1 + (f % 2) * 0.4), OUT, 5)
    for i in range(2):
        ty = hy + 1 + ((f + i * 2) % 4) * 2
        px(P, [(hx + 3, ty)], '#8ff8e2' if i == 0 else '#8fd3ff', 5.2)
    # mãos juntas ao peito
    P.append(Parte(capsula(15.5, 12 + o, 19.5, 14 + o, 1.2), LILAS_CL, z=6))
    P.append(Parte(elipse(20, 13.5 + o, 1.3, 1.3), PELE, z=6.1))
    # diadema de luto
    px(P, [(hx - 2, hy - 4), (hx - 1, hy - 4), (hx, hy - 5), (hx + 1, hy - 4)], '#45293f', 5.5)
    px(P, [(hx, hy - 5)], '#8ff8e2', 5.6)
    particulas(P, 16, 16, 12, f, ['#eaaded', '#8ff8e2'], 5, 21)
    return desenhar(P, 32, 32)


# ================================================================ MONSTROS E GUARDIÕES 48×48

VIDRO = {
    'vermelho': ['#6e2727', '#ae2334', '#e83b3b', '#f68181', '#ffffff'],
    'azul': ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff'],
    'ouro': ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
    'verde': ['#165a4c', '#239063', '#1ebc73', '#91db69', '#ffffff'],
    'roxo': ['#45293f', '#6b3e75', '#a884f3', '#eaaded', '#ffffff'],
    'agua': ['#0b5e65', '#0b8a8f', '#30e1b9', '#8ff8e2', '#ffffff'],
}


def rachas(P, m, cor, z, semente, n=3, comp=5, o=0):
    """Rachas (pedra, osso, vidro): pequenos caminhos aos ziguezagues dentro da máscara."""
    rnd = random.Random(semente)
    dentro = sorted(miolo(m))
    if not dentro:
        return
    pts = []
    for _ in range(n):
        x, y = rnd.choice(dentro)
        for _ in range(comp):
            pts.append((x, y))
            x += rnd.choice((-1, 0, 1))
            y += 1
            if (x, y) not in m:
                break
    px(P, [(x, y + o) for (x, y) in pts if (x, y) in m], cor, z)


def armadura_viva(f):
    """Armadura vazia com um fantasma dentro: elmo fechado com o olhar verde na viseira, alabarda, tabardo roxo,
    ferrugem e amolgadelas, e fumo fantasma a sair pelas frestas."""
    P = []
    b = [0, 0, 1, 1][f]
    A, AE = FERRO, FERRO_ESC
    # perna de trás
    P.append(Parte(capsula(20, 31, 19, 38, 3), AE, z=0, volume='cilindro_v'))
    P.append(Parte(capsula(19, 38, 18.5, 43, 2.6), AE, z=0.1, volume='cilindro_v'))
    P.append(Parte(capsula(18, 44.5, 22.5, 45, 2), AE, z=0.2))
    # braço de trás
    P.append(Parte(capsula(18, 18 + b, 15, 26 + b, 2.4), AE, z=0.5, volume='cilindro_h'))
    P.append(Parte(elipse(15, 27.5 + b, 2.4, 2.2), AE, z=0.6))
    # perna da frente
    P.append(Parte(capsula(26, 31, 27, 38, 3.2), A, z=2, volume='cilindro_v'))
    P.append(Parte(capsula(27, 38, 27, 43, 2.8), A, z=2.1, volume='cilindro_v'))
    P.append(Parte(elipse(27, 37.5, 2.8, 2.3), A, z=2.2))
    P.append(Parte(capsula(26, 44.5, 32, 45, 2), A, z=2.3))
    px(P, [(29, 44), (31, 44)], '#3e3546', 2.4)
    # saiote de lâminas
    for i, y in enumerate((27, 30)):
        P.append(Parte(poligono([(16.5 - i, y + b), (29.5 + i, y + b), (30 + i, y + 3.5 + b), (16 - i, y + 3.5 + b)]), A, z=3 + i * 0.1, volume='cilindro_v'))
    # tronco (couraça) com lâminas e aresta ao meio
    peito = poligono([(16, 15 + b), (28, 14 + b), (31, 19 + b), (30, 27 + b), (17, 28 + b)])
    P.append(Parte(peito, A, z=4, volume='cilindro_v'))
    px(P, linha(25, 16 + b, 27, 26 + b), '#ffffff', 4.1)
    px(P, [(x, 23 + b) for x in range(18, 30)], '#3e3546', 4.1)
    pintas(P, peito, '#9e4539', 4.15, 12, 6, b)            # ferrugem
    px(P, [(20, 18 + b), (21, 19 + b), (19, 25 + b)], '#3e3546', 4.2)   # amolgadelas
    # tabardo roxo rasgado (da cintura para baixo)
    tab = rasgar(poligono([(20, 24 + b), (28, 24 + b), (28.5, 38), (19.5, 38)]), 4, prof=3, dens=55)
    P.append(Parte(tab, ROXO, z=5, volume='cilindro_v'))
    px(P, [(24, 27 + b), (23, 28 + b), (24, 28 + b), (25, 28 + b), (24, 29 + b), (24, 30 + b)], '#f9c22b', 5.1)
    # elmo fechado (grande elmo) com crista roxa
    crista = fita(23, 4 + b, 2, 2.0, -9, f * 0.9, amp=0.8, fim=0.4) | capsula(23, 4 + b, 15, 8 + b + (f % 2), 1.8)
    P.append(Parte(crista, ROXO, z=5.4))
    elmo = poligono([(19.5, 5 + b), (27, 4 + b), (30.5, 7 + b), (31, 14 + b), (28, 16 + b), (20, 16 + b)])
    P.append(Parte(elmo, A, z=6, volume='cilindro_v'))
    px(P, linha(22, 6 + b, 22, 15 + b), '#9babb2', 6.05)
    px(P, [(x, 10 + b) for x in range(25, 32)], OUT, 6.1)          # viseira
    brilho = ['#8ff8e2', '#30e1b9', '#8ff8e2', '#ffffff'][f]
    px(P, [(28, 10 + b), (29, 10 + b)], brilho, 6.2)
    px(P, [(30, 10 + b)], '#30e1b9', 6.2)
    for (x, y) in ((27, 13), (29, 13), (28, 14), (30, 12)):          # furos de respirar
        px(P, [(x, y + b)], '#3e3546', 6.15)
    px(P, [(26, 5 + b)], '#ffffff', 6.2)
    # ombreira com rebites
    omb = elipse(21.5, 17 + b, 5, 4) - {p for p in elipse(21.5, 17 + b, 5, 4) if p[1] > 19 + b}
    P.append(Parte(omb, A, z=7))
    px(P, [(x, 19 + b) for x in range(17, 27)], AE[1], 7.05)
    px(P, [(18, 17 + b), (21, 15 + b), (24, 16 + b)], '#3e3546', 7.1)
    # braço da frente
    P.append(Parte(capsula(23, 20 + b, 28, 25 + b, 2.3), A, z=7.5, volume='cilindro_h'))
    P.append(Parte(capsula(28, 25 + b, 33, 24 + b, 2.1), A, z=7.6, volume='cilindro_h'))
    # alabarda (haste, lâmina, ponta e gancho)
    P.append(Parte(capsula(35, 2 + b, 35, 46, 1.0), MADEIRA, z=7.7, volume='cilindro_h'))
    px(P, [(35, y) for y in range(12 + b, 46, 5)], '#4c3e24', 7.75)
    lam = poligono([(36, 5 + b), (42, 2 + b), (44, 8 + b), (42, 14 + b), (36, 11 + b)])
    P.append(Parte(lam, A, z=7.8, plano=True))
    px(P, linha(43, 4 + b, 44, 9 + b), '#ffffff', 7.85)
    px(P, [(40, 9 + b), (39, 7 + b)], '#9e4539', 7.86)
    P.append(Parte(capsula(35, 4 + b, 35, -1 + b, 0.8), A, z=7.8))
    P.append(Parte(capsula(34, 8 + b, 31, 10 + b, 0.8) | capsula(31, 10 + b, 31, 12 + b, 0.6), A, z=7.8))
    P.append(Parte(elipse(35, 24.5 + b, 2.4, 2.2), A, z=8))          # manopla
    px(P, [(36, 23 + b)], '#ffffff', 8.1)
    # fumo fantasma a sair pelas frestas (pescoço, cintura, joelho)
    for (x0, y0) in ((24, 16 + b), (29, 28 + b), (19, 30 + b)):
        for k in range(3):
            y = y0 - ((f + k) % 4)
            x = x0 + int(math.sin(f + k * 2) * 1.2)
            px(P, [(x, y)], ['#8ff8e2', '#30e1b9', '#0eaf9b'][k], 9)
    return desenhar(P, 48, 48)


def gargula(f):
    """Gárgula de pedra agachada: asas de morcego, chifres, cauda de ponta em lança, garras, olhos vermelhos,
    rachas e musgo na pedra."""
    P = []
    b = [0, 0, 1, 1][f]
    w = [0, 1, 2, 1][f]
    # asa de trás (mais escura) e asa da frente, meio abertas: braço da asa, dedos e membrana recortada
    MEMB = ['#2e222f', '#45293f', '#625565', '#7f708a', '#9babb2']
    for (dx, rp, z) in ((-4, esc(MEMB), 0), (2, MEMB, 1)):
        oy = -w if z else -(w // 2)
        ombro = (21 + dx, 21 + b)
        pulso = (14 + dx, 4 + oy)
        pontas = [(3 + dx, 5 + oy), (0 + dx, 15 + oy), (4 + dx, 25 + oy), (12 + dx, 29)]
        memb = poligono([ombro, pulso] + pontas + [(19 + dx, 27)])
        cadeia = [pulso] + pontas
        for i in range(len(cadeia) - 1):     # recortes entre os dedos
            (x1, y1), (x2, y2) = cadeia[i], cadeia[i + 1]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            vx, vy = ombro[0] - mx, ombro[1] - my
            n = math.hypot(vx, vy) or 1
            memb -= elipse(mx - vx / n * 1.2, my - vy / n * 1.2, 2.6, 2.6)
        P.append(Parte(memb, rp, z=z, plano=True))
        osso = PEDRA if z else PEDRA_ESC
        P.append(Parte(capsula(*ombro, *pulso, 1.4), osso, z=z + 0.1))
        for d in pontas[:3]:
            P.append(Parte(capsula(*pulso, *d, 0.7), osso, z=z + 0.12))
        px(P, [(pulso[0], pulso[1] - 1), (pulso[0] + 1, pulso[1] - 2)], '#c7dcd0', z + 0.2)    # garra da asa
    # cauda em S com ponta de lança
    cauda = corda([(15, 38 + b), (8, 43), (3, 40), (3, 34)], 1.5)
    P.append(Parte(cauda, PEDRA, z=1.5))
    P.append(Parte(poligono([(3, 29), (6, 33), (3, 35.5), (0.5, 33)]), PEDRA, z=1.6, plano=True))
    # braço de trás (apoiado no chão)
    P.append(Parte(capsula(25, 25 + b, 27, 36, 2.2), PEDRA_ESC, z=2))
    P.append(Parte(capsula(27, 36, 28, 44, 1.8), PEDRA_ESC, z=2.1))
    # anca e pé de trás
    anca = elipse(18, 35, 6.5, 6.5)
    P.append(Parte(anca, PEDRA, z=3))
    P.append(Parte(capsula(19, 39, 22, 44, 2.2), PEDRA, z=3.1))
    for dx in (0, 2.5, 5):
        P.append(Parte(capsula(21 + dx * 0.4, 44.5, 23 + dx, 45.5, 0.8), PEDRA, z=3.2))
    # tronco curvado
    tronco = elipse(24, 29 + b, 8.5, 8.5) | elipse(29, 25 + b, 6.5, 6.5)
    P.append(Parte(tronco, PEDRA, z=4))
    px(P, [(31, 27 + b), (32, 29 + b), (31, 31 + b), (30, 25 + b)], '#625565', 4.1)   # costelas na barriga
    rachas(P, tronco | anca, '#3e3546', 4.2, 5, n=4, comp=6)
    pintas(P, tronco, '#9babb2', 4.15, 3, 6, b)
    # cabeça: focinho, chifres, orelha, sobrolho
    hx, hy = 34, 16 + b
    cab = elipse(hx, hy, 5.2, 4.8) | capsula(hx + 2, hy + 1, hx + 7.5, hy + 2.5, 2.6)
    P.append(Parte(cab, PEDRA, z=6))
    P.append(Parte(capsula(hx + 1, hy + 4, hx + 7, hy + 5, 1.3), PEDRA_ESC, z=5.9))   # maxilar
    px(P, [(hx + 3, hy + 4), (hx + 5, hy + 4), (hx + 7, hy + 4)], '#ffffff', 6.1)    # dentes
    px(P, [(hx + 8, hy + 3)], '#ffffff', 6.1)
    px(P, [(hx + 8, hy + 1)], OUT, 6.1)                                               # narina
    for (ax, ay, bx_, by_, cx_, cy_) in ((-1, -4, -5, -9, -9, -9), (2, -4, 0, -10, -3, -12)):
        P.append(Parte(corda([(hx + ax, hy + ay), (hx + bx_, hy + by_), (hx + cx_, hy + cy_)], 1.2), OSSO_ESC, z=6.2))
    P.append(Parte(poligono([(hx - 3, hy - 2), (hx - 9, hy - 5), (hx - 4, hy + 1)]), PEDRA_ESC, z=5.8, plano=True))   # orelha
    P.append(Parte(capsula(hx, hy - 2, hx + 5, hy - 1, 1.1), PEDRA, z=6.3))           # sobrolho
    if f == 3:
        px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 4, hy)], OUT, 6.4)
    else:
        px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 4, hy), (hx + 2, hy + 1), (hx + 3, hy + 1)], '#e83b3b', 6.4)
        px(P, [(hx + 3, hy)], '#ffffff', 6.5)
        px(P, [(hx + 4, hy + 1)], '#ae2334', 6.45)
    pintas(P, cab, '#625565', 6.15, 8, 8, b)
    # musgo em cima da cabeça e dos ombros
    musgo = [p for p in (cab | tronco) if _h(p[0], p[1] - b, 77) % 100 < 45 and
             (p[0], p[1] - 1) not in (cab | tronco) and p[0] < hx + 3]
    px(P, musgo, '#547e64', 6.6)
    px(P, [(x, y + 1) for (x, y) in musgo if _h(x, y, 5) % 3 == 0], '#374e4a', 6.6)
    # braço da frente com garras no chão
    P.append(Parte(capsula(30, 24 + b, 34, 33, 2.6), PEDRA, z=7, volume='cilindro_h'))
    P.append(Parte(capsula(34, 33, 35, 42, 2.2), PEDRA, z=7.1))
    for dx in (-1, 1.5, 4):
        P.append(Parte(capsula(35, 43, 35 + dx, 45.5, 0.8), PEDRA, z=7.2))
        px(P, [(35 + dx, 46)], '#c7dcd0', 7.3)
    px(P, [(33, 36), (34, 38)], '#3e3546', 7.25)
    return desenhar(P, 48, 48)


def o_jardineiro(f):
    """Zombie gigante de chapéu de palha e jardineiras remendadas, sorriso de dentes, tesoura de poda enorme."""
    P = []
    b = [0, 0, 1, 1][f]
    snip = [0, 1, 2, 1][f]
    JARD = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
    JARD_E = esc(JARD)
    # perna de trás, perna da frente, botas
    P.append(Parte(capsula(19, 33, 17, 43, 3.2), JARD_E, z=0, volume='cilindro_v'))
    P.append(Parte(capsula(16, 44.5, 21, 45, 2.0), NEGRO, z=0.1))
    P.append(Parte(capsula(26, 33, 28, 43, 3.4), JARD, z=2, volume='cilindro_v'))
    P.append(Parte(capsula(27, 44.5, 33, 45, 2.1), NEGRO, z=2.1))
    px(P, [(25, 39), (26, 39), (27, 40)], ZOMBI[2], 2.2)                 # joelho podre pelo rasgão
    px(P, [(25, 38), (28, 39)], OUT, 2.2)
    # braço de trás pendurado
    P.append(Parte(capsula(16, 20 + b, 13, 31 + b, 2.6), ZOMBI_ESC, z=0.5))
    for dx in (-1, 1):
        P.append(Parte(capsula(13, 32 + b, 13 + dx, 35 + b, 0.8), ZOMBI_ESC, z=0.6))
    # tronco: camisa rasgada e jardineiras com remendo
    tronco = poligono([(13, 19 + b), (29, 16 + b), (33, 23 + b), (31, 35), (14, 35)])
    P.append(Parte(tronco, TRAPO, z=1, volume='cilindro_v'))
    pintas(P, tronco, '#4c3e24', 1.1, 3, 10, b)
    peito = poligono([(17, 23 + b), (30, 22 + b), (32, 35), (15, 35.5)])
    P.append(Parte(peito, JARD, z=1.5, volume='cilindro_v'))
    px(P, linha(19, 17 + b, 18, 23 + b), JARD[2], 1.6)                    # alças
    px(P, linha(27, 16 + b, 28, 22 + b), JARD[2], 1.6)
    px(P, [(18, 23 + b), (28, 22 + b)], '#f9c22b', 1.7)                   # botões
    remendo = retangulo(20, 27 + b, 24, 31 + b)
    P.append(Parte(remendo, ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#e6904e'], z=1.8, plano=True))
    px(P, [(19, 28 + b), (19, 30 + b), (25, 28 + b), (25, 30 + b), (21, 26 + b), (23, 26 + b)], '#c7dcd0', 1.9)   # costuras
    px(P, [(x, 33) for x in range(16, 31, 2)], JARD[1], 1.75)
    # cabeça (para a frente), verde, sorriso de dentes
    hx, hy = 31, 16 + b
    cab = elipse(hx, hy, 5.6, 5.2) | elipse(hx + 3, hy + 3, 3.4, 2.6)
    P.append(Parte(cab, ZOMBI, z=3, luz=0.25))
    pintas(P, cab, '#374e4a', 3.1, 6, 12, b)
    px(P, [(x, hy + 3) for x in range(hx + 1, hx + 7)], OUT, 3.2)        # boca rasgada
    px(P, [(x, hy + 3) for x in range(hx + 1, hx + 7, 2)], '#c7dcd0', 3.25)
    px(P, [(hx + 6, hy + 2), (hx + 7, hy + 2)], OUT, 3.2)
    px(P, [(hx - 1, hy + 2), (hx, hy + 3), (hx - 1, hy + 4)], OUT, 3.2)  # cicatriz cosida
    px(P, [(hx + 6, hy)], ZOMBI[1], 3.2)                                   # nariz
    if f == 3:
        olho_fechado(P, hx + 2, hy - 1, 3.3, 3)
    else:
        px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2), (hx + 3, hy - 2), (hx + 4, hy - 2), (hx + 1, hy - 1), (hx + 1, hy)], OUT, 3.3)
        px(P, [(hx + 2, hy - 1), (hx + 3, hy - 1), (hx + 2, hy), (hx + 3, hy)], '#d5e04b', 3.35)
        px(P, [(hx + 3, hy - 1)], '#fbff86', 3.36)
    # chapéu de palha: copa, fita vermelha, aba larga, palhinhas soltas
    copa = {p for p in elipse(hx - 1, hy - 7, 5.6, 4.6) if p[1] <= hy - 6}
    P.append(Parte(copa, PALHA, z=4))
    px(P, [(x, hy - 7) for x in range(hx - 6, hx + 5)], '#ae2334', 4.1)
    px(P, [(x, hy - 7) for x in range(hx - 6, hx + 5, 3)], '#6e2727', 4.11)
    aba = elipse(hx, hy - 5, 11, 2.2)
    P.append(Parte(aba, PALHA, z=4.2, volume='cilindro_h'))
    palha = [p for p in (copa | aba) if (p[0] + p[1] * 2) % 5 == 0 and p in miolo(copa | aba)]
    px(P, palha, '#cd683d', 4.25)
    px(P, [(hx - 9, hy - 5), (hx + 6, hy - 6), (hx - 3, hy - 11)], '#2e222f', 4.3)   # buracos na palha
    px(P, [(hx + 11, hy - 5), (hx + 12, hy - 4), (hx - 11, hy - 6)], '#f9c22b', 4.3)
    px(P, [(hx - 6, hy - 8), (hx - 5, hy - 9)], '#e83b3b', 4.35)           # rosa espetada na fita
    px(P, [(hx - 6, hy - 9)], '#239063', 4.35)
    # braço da frente e a tesoura de poda
    P.append(Parte(capsula(27, 21 + b, 30, 28 + b, 2.6), ZOMBI, z=5, volume='cilindro_h'))
    P.append(Parte(capsula(26, 20 + b, 30, 22 + b, 2.8), TRAPO, z=5.05))  # manga
    P.append(Parte(capsula(30, 28 + b, 35, 30 + b, 2.3), ZOMBI, z=5.1))
    piv = (38, 27 + b)
    for k, (tx, ty) in enumerate(((46, 5 + b - snip), (47.5, 11 + b + snip))):
        dx, dy = tx - piv[0], ty - piv[1]
        n = math.hypot(dx, dy)
        nx, ny = -dy / n, dx / n
        lam = poligono([(piv[0] - nx * 1.6, piv[1] - ny * 1.6), (piv[0] + nx * 1.6, piv[1] + ny * 1.6),
                        (tx + nx * 0.3, ty + ny * 0.3), (tx - nx * 1.2, ty - ny * 1.2)])
        P.append(Parte(lam, FERRO, z=5.2 + k * 0.1, plano=True))
        px(P, linha(piv[0] + nx * 0.8, piv[1] + ny * 0.8, tx - nx * 0.2, ty - ny * 0.2), '#ffffff', 5.25 + k * 0.1)
    px(P, [(piv[0], piv[1])], '#f9c22b', 5.4)
    for k, (hx2, hy2) in enumerate(((32, 35 + b), (35.5, 37 + b))):
        P.append(Parte(capsula(piv[0], piv[1], piv[0] + (hx2 - piv[0]) * 0.4, piv[1] + (hy2 - piv[1]) * 0.4, 1.1), MADEIRA, z=5.15 + k * 0.1))
        P.append(Parte(capsula(piv[0] + (hx2 - piv[0]) * 0.4, piv[1] + (hy2 - piv[1]) * 0.4, hx2, hy2, 1.6), SANGUE, z=5.16 + k * 0.1))
    P.append(Parte(elipse(35.5, 30 + b, 2.6, 2.4), ZOMBI, z=5.5))       # mão
    px(P, [(36, 29 + b), (37, 30 + b)], ZOMBI[1], 5.55)
    # folhas de sebe presas na tesoura
    px(P, [(43, 15 + b), (44, 14 + b), (42, 16 + b)], '#239063', 5.6)
    return desenhar(P, 48, 48)


def anjo_caido_de_vitral(f):
    """Anjo de vitral partido: corpo e asas de pedaços de vidro colorido com chumbo escuro, cara de vidro rachada,
    auréola partida e estilhaços a flutuar."""
    P = []
    o = [2, 1, 0, 1][f]
    cores = ['azul', 'vermelho', 'ouro', 'roxo', 'verde', 'azul', 'agua', 'vermelho']

    def vitral(m, z, semente, chave, buracos=0, paleta=None):
        """Pedaços de vidro com chumbo: `chave(x, y)` diz a que pedaço pertence cada píxel."""
        paleta = paleta or cores
        dono = {p: chave(*p) for p in m}
        pedacos = {}
        chumbo = set()
        for (x, y), k in dono.items():
            if any(dono.get((x + a, y + c), k) != k for a, c in ((1, 0), (0, 1))):
                chumbo.add((x, y))
            else:
                pedacos.setdefault(k, set()).add((x, y))
        for k in sorted(pedacos):
            pd = pedacos[k]
            hsh = _h(k[0] + 50, k[1] + 50, semente)
            if hsh % 100 < buracos:
                continue
            nome = paleta[hsh % len(paleta)]
            P.append(Parte(pd, VIDRO[nome], z=z, plano=True, separar=False))
            if (hsh + f) % 6 == 0:     # um pedaço brilha a cada quadro
                mx = min(pd, key=lambda p: (p[0] + p[1]))
                px(P, [mx], '#ffffff', z + 0.02)
        px(P, chumbo, '#2e222f', z + 0.01)

    # asas (de trás e da frente), feitas de penas de vidro (raios a partir do ombro e anéis)
    for (dx, z, sm) in ((-2, 0, 3), (3, 1, 5)):
        ox, oy = 22 + dx, 16 + o
        asa = poligono([(ox, oy - 1), (12 + dx, 5 + o), (4 + dx, 4 + o), (1 + dx, 10 + o), (3 + dx, 17 + o),
                        (6 + dx, 25 + o), (11 + dx, 32 + o), (16 + dx, 31 + o), (21 + dx, 24 + o)])
        for k in range(4):     # recortes das penas em baixo
            asa -= elipse(6 + dx + k * 4, 30 + o - k * 0.8, 1.6, 2.6)

        def chave(x, y, ox=ox, oy=oy):
            ang = math.atan2(y - oy, x - ox)
            dist = math.hypot(x - ox, y - oy)
            return (int((ang + math.pi) / 0.42), int((dist + 2) / 8))
        P.append(Parte(asa, ['#2e222f'] * 5, z=z - 0.05))
        vitral(asa, z, sm, chave, buracos=8 if z else 14,
               paleta=['azul', 'agua', 'azul', 'roxo', 'agua', 'ouro', 'azul'])
    # túnica em ponta (não tem pés: flutua), em losangos de vidro
    corpo = poligono([(23, 15 + o), (31, 15 + o), (34, 27 + o), (33, 37 + o), (28, 44 + o), (22, 37 + o), (21, 27 + o)])
    P.append(Parte(corpo, ['#2e222f'] * 5, z=1.95))
    vitral(corpo, 2, 11, lambda x, y: ((x + y - o) // 7, (x - y + o) // 7),
           paleta=['vermelho', 'ouro', 'roxo', 'vermelho', 'ouro'])
    # cabeça de vidro claro rachada, cabelo de vidro dourado
    hx, hy = 29, 10 + o
    P.append(Parte(capsula(hx - 1, hy + 3, hx - 1, hy + 6, 1.5), ['#4d65b4', '#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff'], z=2.5))
    P.append(Parte(elipse(hx, hy, 4.4, 4.5), ['#4d65b4', '#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff'], z=3, luz=0.1))
    cabelo = {p for p in elipse(hx - 1.2, hy - 1, 4.8, 4.2) if p[1] <= hy - 3 or p[0] <= hx - 2.5}
    cabelo |= capsula(hx - 4, hy, hx - 6, hy + 6, 1.6)
    P.append(Parte(cabelo, VIDRO['ouro'], z=3.5, separar=False))
    px(P, [(hx - 4, hy - 2), (hx - 3, hy + 1), (hx - 5, hy + 4)], '#9e4539', 3.55)
    px(P, linha(hx - 1, hy - 2, hx + 2, hy + 3), '#4d65b4', 3.6)          # racha na cara
    px(P, [(hx + 2, hy - 1), (hx + 3, hy - 1)], OUT, 3.7)                 # olho fechado triste
    px(P, [(hx + 2, hy), (hx + 3, hy + 1)], '#8fd3ff', 3.7)               # lágrima de luz
    px(P, [(hx + 3, hy + 3)], '#4d65b4', 3.7)
    # auréola partida (inclinada, com um bocado a cair)
    aur = elipse(hx - 1, hy - 7, 5, 1.8) - elipse(hx - 1, hy - 7, 3.2, 0.8)
    aur -= {p for p in aur if p[0] >= hx + 1 and p[1] <= hy - 7}
    P.append(Parte(aur, OURO, z=4))
    px(P, [(hx + 4, hy - 9 + (f % 2)), (hx + 5, hy - 9 + (f % 2))], '#f9c22b', 4.1)
    # braço da frente estendido a segurar um estilhaço em forma de lâmina
    P.append(Parte(capsula(29, 18 + o, 34, 24 + o, 1.7), VIDRO['azul'], z=5))
    P.append(Parte(capsula(34, 24 + o, 38, 22 + o, 1.5), ['#4d65b4', '#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff'], z=5.1))
    lam = poligono([(37, 24 + o), (40, 20 + o), (46.5, 7 + o), (44, 18 + o), (40, 24 + o)])
    P.append(Parte(lam, VIDRO['agua'], z=5.2, plano=True))
    px(P, linha(40, 20 + o, 45, 11 + o), '#ffffff', 5.25)
    # estilhaços a flutuar à volta
    rnd = random.Random(9)
    for i in range(6):
        ang = i * 1.05 + f * 0.4
        x = 24 + math.cos(ang) * (17 + (i % 2) * 3)
        y = 26 + math.sin(ang) * 14 + o
        c = VIDRO[cores[i % len(cores)]]
        tri = [(x, y), (x + 1, y), (x, y + 1)] if i % 2 else [(x, y), (x, y + 1), (x + 1, y + 1), (x, y + 2)]
        px(P, tri, c[2], 9)
        px(P, [tri[0]], c[3], 9.1)
    return desenhar(P, 48, 48)


def carcereiro(f):
    """Brutamontes de capuz com olhos amarelos, braços enormes com ligaduras, avental de couro, molho de chaves
    no cinto e uma bola de ferro com espigões presa a uma corrente."""
    P = []
    b = [0, 0, 1, 1][f]
    sw = [0, 1, 0, -1][f]
    PELE = ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fca790']
    PELE_E = esc(PELE)
    CAPUZ = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
    # pernas e botas
    P.append(Parte(capsula(19, 33, 18, 43, 3.6), TRAPO_ESC, z=0, volume='cilindro_v'))
    P.append(Parte(capsula(17, 44.5, 22.5, 45, 2.2), NEGRO, z=0.1))
    P.append(Parte(capsula(26, 33, 27, 43, 3.8), esc(TRAPO), z=2, volume='cilindro_v'))
    P.append(Parte(capsula(26, 44.5, 32.5, 45, 2.3), NEGRO, z=2.1))
    px(P, [(29, 43), (31, 43)], '#625565', 2.2)
    # braço de trás (enorme)
    P.append(Parte(capsula(17, 19 + b, 14, 29 + b, 3.4), PELE_E, z=0.5))
    P.append(Parte(elipse(14, 31 + b, 3, 2.8), PELE_E, z=0.6))
    # tronco largo: camisa suja e colete de couro
    tronco = poligono([(13, 17 + b), (30, 15 + b), (34, 22 + b), (33, 34), (15, 34)])
    P.append(Parte(tronco, COURO, z=1, volume='cilindro_v'))
    pintas(P, tronco, '#2e222f', 1.1, 4, 6, b)
    px(P, [(18, 21 + b), (18, 25 + b), (18, 29 + b)], '#ab947a', 1.15)   # costuras
    # avental de couro com nódoas
    av = poligono([(23, 23 + b), (33, 22 + b), (34, 40), (25, 40)])
    P.append(Parte(av, ['#2e222f', '#45293f', '#694f62', '#966c6c', '#966c6c'], z=1.5, volume='cilindro_v'))
    pintas(P, av, '#6e2727', 1.55, 8, 9, b)
    # cinto com o molho de chaves
    px(P, [(x, 31) for x in range(14, 34)], '#2e222f', 1.6)
    px(P, [(x, 32) for x in range(14, 34)], '#45293f', 1.6)
    px(P, [(24, 31), (24, 32)], '#f9c22b', 1.7)
    anel = elipse(19, 34.5, 1.8, 1.8) - {(19, 34)}
    px(P, [p for p in anel if p not in elipse(19, 34.5, 0.9, 0.9)], '#9babb2', 1.8)
    for k, (dx, ln) in enumerate(((-2, 4), (0, 6), (2, 4))):
        kx = 19 + dx + (sw if k == 1 else 0)
        haste = linha(19 + dx * 0.4, 36, kx, 36 + ln)
        px(P, haste, '#c7dcd0' if k == 1 else '#9babb2', 1.85)
        px(P, [(kx + 1, 36 + ln), (kx + 1, 35 + ln)], '#7f708a', 1.9)        # dentes da chave
        px(P, [haste[0]], '#ffffff', 1.9)
    # capuz com ponta caída para trás e capa curta nos ombros
    hx, hy = 29, 11 + b
    capuz = elipse(hx, hy, 6, 6) | capsula(hx - 3, hy - 3, hx - 9, hy + 2, 2.2)
    capuz |= poligono([(hx - 9, hy + 3), (hx + 5, hy + 3), (hx + 7, hy + 9), (hx - 11, hy + 10)])
    capuz = rasgar(capuz, 12, prof=2, dens=50)
    P.append(Parte(capuz, CAPUZ, z=3))
    pintas(P, capuz, '#694f62', 3.05, 9, 5, b)
    buraco = elipse(hx + 2.5, hy + 0.5, 3.2, 3.6)
    px(P, buraco, '#2e222f', 3.1)
    if f == 3:
        px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 4, hy)], '#9e4539', 3.2)
    else:
        px(P, [(hx + 2, hy - 1), (hx + 3, hy - 1), (hx + 2, hy)], '#f9c22b', 3.2)
        px(P, [(hx + 3, hy - 1)], '#fbff86', 3.25)
        px(P, [(hx + 5, hy - 1)], '#f79617', 3.2)
    px(P, [(hx + 3, hy + 3), (hx + 4, hy + 3)], '#cd683d', 3.2)          # queixo a espreitar
    # braço da frente com ligaduras e a corrente
    P.append(Parte(capsula(28, 19 + b, 31, 27 + b, 3.4), PELE, z=4, volume='cilindro_h'))
    P.append(Parte(capsula(31, 27 + b, 36, 30 + b, 3.0), PELE, z=4.1, volume='cilindro_h'))
    px(P, [(29, 22 + b), (30, 23 + b), (31, 23 + b)], '#7a3045', 4.15)    # cicatriz
    for x in (33, 35):
        px(P, [(x, 28 + b + k) for k in range(4)], '#c7dcd0', 4.2)          # ligaduras
    P.append(Parte(elipse(37.5, 30.5 + b, 3, 2.8), PELE, z=4.3))          # punho
    # corrente e bola com espigões a abanar
    bx, by = 40 + sw, 40
    elos = []
    for i in range(6):
        t = (i + 0.5) / 6
        elos.append((37.5 + (bx - 37.5) * t, 32 + b + (by - 4 - 32 - b) * t))
    for i, (x, y) in enumerate(elos):
        px(P, [(x, y), (x + (1 if i % 2 else 0), y + (0 if i % 2 else 1))], '#9babb2' if i % 2 else '#625565', 4.4)
    for ang in range(0, 360, 60):
        a = math.radians(ang + 15)
        P.append(Parte(capsula(bx, by, bx + math.cos(a) * 5.6, by + math.sin(a) * 5.6, 0.7), FERRO, z=4.45))
    P.append(Parte(elipse(bx, by, 4, 4), FERRO_ESC, z=4.5))
    px(P, [(bx - 2, by - 2), (bx - 1, by - 2)], '#c7dcd0', 4.55)
    return desenhar(P, 48, 48)


def comandante_dos_cavaleiros_caidos(f):
    """Cavaleiro negro de elmo com chifres e viseira vermelha, capa rasgada e uma lança com o estandarte rasgado."""
    P = []
    b = [0, 0, 1, 1][f]
    w = [0, 1, 2, 1][f]
    A = ['#2e222f', '#2e222f', '#3e3546', '#625565', '#9babb2']
    AE = esc(A)
    # capa rasgada atrás
    capa = poligono([(17, 15 + b), (23, 15 + b), (22, 40), (16, 46), (6 - w, 45), (9, 30)])
    capa = rasgar(capa, 21, prof=4, dens=55)
    P.append(Parte(capa, SANGUE_ESC, z=0))
    px(P, linha(15, 20 + b, 11 - w * 0.5, 42), '#2e222f', 0.05)
    px(P, [(12, 36), (14, 40)], '#2e222f', 0.06)                          # buracos
    # pernas de placas negras com joelheiras douradas
    P.append(Parte(capsula(20, 31, 19, 43, 3), AE, z=0.5, volume='cilindro_v'))
    P.append(Parte(capsula(18.5, 44.5, 23, 45, 2), AE, z=0.6))
    P.append(Parte(capsula(26, 31, 27, 43, 3.2), A, z=2, volume='cilindro_v'))
    P.append(Parte(capsula(26, 44.5, 32, 45, 2.1), A, z=2.1))
    P.append(Parte(elipse(27, 37, 2.0, 1.6), A, z=2.2))
    px(P, [(26, 36), (27, 36)], '#f9c22b', 2.25)
    # braço de trás
    P.append(Parte(capsula(18, 18 + b, 16, 27 + b, 2.4), AE, z=1))
    # saiote e couraça
    P.append(Parte(poligono([(16.5, 27 + b), (29.5, 27 + b), (31, 33 + b), (15, 33 + b)]), A, z=3, volume='cilindro_v'))
    px(P, [(x, 30 + b) for x in range(16, 31)], '#45293f', 3.05)
    peito = poligono([(16, 14 + b), (28, 13 + b), (31, 19 + b), (30, 27 + b), (17, 28 + b)])
    P.append(Parte(peito, A, z=4, volume='cilindro_v'))
    px(P, linha(17, 15 + b, 28, 14 + b), '#f9c22b', 4.05)                 # debruado dourado
    px(P, linha(30, 20 + b, 29, 27 + b), '#f79617', 4.05)
    px(P, [(23, 19 + b), (22, 20 + b), (24, 20 + b), (23, 21 + b)], '#ae2334', 4.1)   # brasão (uma rosa vermelha)
    px(P, [(x, 26 + b) for x in range(17, 30)], '#ae2334', 4.1)           # faixa
    # elmo com chifres e viseira vermelha
    hx, hy = 25, 9 + b
    for (ax, ay, mx, my, ex, ey) in ((-2, -4, -6, -8, -5, -12), (1, -4, 0, -9, 3, -12)):
        P.append(Parte(corda([(hx + ax, hy + ay), (hx + mx, hy + my), (hx + ex, hy + ey)], 1.3), OSSO_ESC, z=4.9))
    elmo = poligono([(hx - 5, hy - 4), (hx + 3, hy - 5), (hx + 6, hy - 2), (hx + 6, hy + 4), (hx + 3, hy + 6), (hx - 5, hy + 5)])
    P.append(Parte(elmo, A, z=5, volume='cilindro_v'))
    px(P, [(x, hy) for x in range(hx + 1, hx + 7)], OUT, 5.1)
    brilho = ['#e83b3b', '#f57d4a', '#e83b3b', '#ae2334'][f]
    px(P, [(hx + 3, hy), (hx + 4, hy), (hx + 5, hy)], brilho, 5.2)
    px(P, [(hx + 4, hy)], '#fca790', 5.25)
    px(P, [(hx + 6, hy - 1 - k) for k in range(2)] + [(hx + 7, hy - 3)], '#ae2334', 5.3)   # rasto de luz
    px(P, linha(hx - 5, hy + 5, hx + 3, hy + 6), '#f79617', 5.1)
    px(P, [(hx - 2, hy - 3)], '#9babb2', 5.15)
    # ombreira com espigões
    omb = {p for p in elipse(21, 16 + b, 5, 3.6) if p[1] <= 18 + b}
    P.append(Parte(omb, A, z=6))
    for k in range(3):
        P.append(Parte(capsula(18 + k * 3, 13 + b, 17 + k * 3, 10 + b, 0.6), OSSO_ESC, z=5.9))
    px(P, [(x, 18 + b) for x in range(17, 26)], '#f79617', 6.05)
    # braço da frente a segurar a lança com o estandarte
    P.append(Parte(capsula(23, 19 + b, 28, 25 + b, 2.3), A, z=7))
    P.append(Parte(capsula(28, 25 + b, 33, 24 + b, 2.1), A, z=7.1))
    P.append(Parte(capsula(35, 3 + b, 35, 46, 1.0), MADEIRA, z=6.9, volume='cilindro_h'))
    P.append(Parte(poligono([(35, -1 + b), (37, 4 + b), (35, 6 + b), (33, 4 + b)]), FERRO, z=7, plano=True))
    est = poligono([(36, 6 + b), (46, 6 + b + w * 0.5), (45, 18 + b), (42, 15 + b + w * 0.5), (39, 19 + b), (36, 17 + b)])
    est -= elipse(43, 10 + b, 0.8, 0.8)
    P.append(Parte(est, SANGUE, z=6.95, plano=True))
    px(P, [(40, 9 + b), (39, 10 + b), (41, 10 + b), (40, 11 + b), (40, 12 + b)], '#f9c22b', 7.0)   # coroa bordada
    px(P, [(39, 9 + b), (41, 9 + b)], '#f79617', 7.0)
    px(P, [(x, 7 + b) for x in range(37, 45, 2)], '#f9c22b', 7.0)
    P.append(Parte(elipse(35, 24.5 + b, 2.3, 2.1), A, z=7.5))
    px(P, [(36, 24 + b)], '#9babb2', 7.55)
    # brasas vermelhas a subir
    particulas(P, 22, 30, 12, f, ['#e83b3b', '#ae2334'], 4, 8)
    return desenhar(P, 48, 48)


def coveiro_ghoul(f):
    """Ghoul curvado de pele cinzenta-azulada, orelhas bicudas, dentes afiados, sobretudo remendado, uma pá e
    uma lanterna pendurada no cinto."""
    P = []
    b = [0, 0, 1, 1][f]
    luz = ['#fbb954', '#f79617', '#fbb954', '#fbff86'][f]
    # pernas finas dobradas e pés com garras
    for (q, j, p, rp, z) in (((18, 37), (14, 41), (16, 45), CINZA_AZ_ESC, 0), ((25, 37), (29, 41), (27, 45), CINZA_AZ, 2)):
        P.append(Parte(capsula(*q, *j, 1.8), rp, z=z))
        P.append(Parte(capsula(*j, *p, 1.6), rp, z=z + 0.1))
        for dx in (0, 2, 4):
            P.append(Parte(capsula(p[0], p[1], p[0] + dx, 45.5, 0.7), rp, z=z + 0.2))
    # lanterna pendurada atrás
    P.append(Parte(capsula(13, 32 + b, 13, 34 + b, 0.5), FERRO_ESC, z=0.4))
    lant = retangulo(11, 35 + b, 15, 39 + b, canto=1)
    P.append(Parte(lant, FERRO_ESC, z=0.5, plano=True))
    px(P, retangulo(12, 36 + b, 14, 38 + b), luz, 0.6)
    px(P, [(13, 37 + b)], '#ffffff', 0.61)
    # braço de trás pendurado
    P.append(Parte(capsula(19, 20 + b, 16, 28 + b, 1.8), CINZA_AZ_ESC, z=0.8))
    P.append(Parte(capsula(16, 28 + b, 17, 34 + b, 1.6), CINZA_AZ_ESC, z=0.85))
    # sobretudo remendado com abas rasgadas
    casaco = poligono([(12, 20 + b), (24, 14 + b), (30, 19 + b), (29, 33 + b), (25, 39), (13, 39), (11, 30)])
    casaco = rasgar(casaco, 31, prof=3, dens=60)
    P.append(Parte(casaco, TRAPO, z=1.5))
    pintas(P, casaco, '#4c3e24', 1.55, 2, 8, b)
    rem = retangulo(15, 27 + b, 18, 30 + b)
    P.append(Parte(rem, ['#4c3e24', '#676633', '#a2a947', '#a2a947', '#a2a947'], z=1.6, plano=True))
    px(P, [(14, 28 + b), (19, 29 + b), (16, 26 + b)], '#c7dcd0', 1.65)
    px(P, [(x, 32 + b) for x in range(13, 29)], '#2e222f', 1.7)          # cinto de corda
    px(P, [(x, 32 + b) for x in range(14, 29, 3)], '#966c6c', 1.71)
    # gola levantada
    P.append(Parte(poligono([(21, 13 + b), (27, 15 + b), (26, 20 + b), (21, 19 + b)]), esc(TRAPO), z=1.8))
    # cabeça para a frente, careca, orelha bicuda para trás
    hx, hy = 31, 18 + b
    P.append(Parte(poligono([(hx - 3, hy - 2), (hx - 11, hy - 6), (hx - 4, hy + 1)]), CINZA_AZ, z=2.9, plano=True))
    px(P, [(hx - 6, hy - 3), (hx - 7, hy - 4)], '#cf657f', 2.95)
    cab = elipse(hx, hy, 5.6, 5) | capsula(hx + 2, hy + 2, hx + 7, hy + 3, 2.4)
    P.append(Parte(cab, CINZA_AZ, z=3, luz=0.15))
    pintas(P, cab, '#484a77', 3.05, 5, 8, b)
    px(P, [(hx - 2, hy - 5), (hx, hy - 6), (hx - 4, hy - 4)], OUT, 3.06)    # cabelinhos
    if f == 3:
        olho_fechado(P, hx + 2, hy - 2, 3.2, 3)
    else:
        px(P, [(hx + 1, hy - 2), (hx + 2, hy - 2), (hx + 3, hy - 2), (hx + 1, hy - 1)], OUT, 3.2)
        px(P, [(hx + 2, hy - 1), (hx + 3, hy - 1)], '#f9c22b', 3.25)
        px(P, [(hx + 3, hy - 1)], '#fbff86', 3.26)
    # boca grande de dentes afiados
    px(P, [(x, hy + 3) for x in range(hx + 1, hx + 9)], OUT, 3.3)
    px(P, [(hx + 2, hy + 2), (hx + 4, hy + 2), (hx + 6, hy + 2), (hx + 8, hy + 2)], '#ffffff', 3.35)
    px(P, [(hx + 3, hy + 4), (hx + 7, hy + 4)], '#c7dcd0', 3.35)
    px(P, [(hx + 8, hy + 1)], OUT, 3.3)                                   # narina
    # pá à frente (cabo comprido com pega em T, lâmina com terra)
    P.append(Parte(capsula(40, 10 + b, 40, 37, 1.0), MADEIRA, z=3.8, volume='cilindro_h'))
    P.append(Parte(capsula(38, 9 + b, 42, 9 + b, 0.9), MADEIRA, z=3.85))
    lamina = poligono([(37, 36), (43, 36), (43.5, 43), (40, 46.5), (36.5, 43)])
    P.append(Parte(lamina, FERRO, z=3.9, plano=True))
    px(P, [(38, 43), (39, 44), (40, 45), (41, 44), (39, 42), (42, 42)], '#4c3e24', 3.95)
    px(P, [(42, 38), (42, 39)], '#9e4539', 3.95)
    # braço da frente comprido, a agarrar o cabo
    P.append(Parte(capsula(25, 20 + b, 31, 28 + b, 1.9), CINZA_AZ, z=4))
    P.append(Parte(capsula(31, 28 + b, 38, 26 + b, 1.7), CINZA_AZ, z=4.1))
    P.append(Parte(capsula(24, 19 + b, 28, 23 + b, 2.3), TRAPO, z=4.05))   # manga
    P.append(Parte(elipse(40, 26 + b, 1.9, 2.1), CINZA_AZ, z=4.2))
    for dy in (-1, 1):
        px(P, [(42, 26 + b + dy)], '#ffffff', 4.25)                        # unhas
    # luz da lanterna e pirilampos
    particulas(P, 13, 34, 5, f, [luz, '#fbb954'], 3, 2)
    return desenhar(P, 48, 48)


def o_pregoeiro_fantasma(f):
    """Fantasma gordo a apregoar: tricórnio com pena, bigode farto, boca aberta, barriga com botões de ouro,
    um pergaminho e um sino enorme a tocar (ondas de som)."""
    P = []
    o = [0, -1, -1, 0][f]
    fase = f * math.pi / 2
    toque = [0, 1, 2, 1][f]
    # cauda
    cauda = fita(21, 33 + o, 11, 7, -12, fase, amp=1.6, ondas=1.0, fim=0.12)
    P.append(Parte(cauda, VERDE_F2, z=0))
    # braço de trás com pergaminho
    P.append(Parte(capsula(17, 23 + o, 12, 28 + o, 2.2), VERDE_F2, z=0.5))
    perg = capsula(9, 26 + o, 12, 33 + o, 1.6)
    P.append(Parte(perg, ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff'], z=0.6))
    P.append(Parte(capsula(9, 26 + o, 7, 31 + o, 1.2), ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff'], z=0.7))
    px(P, [(10, 29 + o), (11, 31 + o)], '#694f62', 0.8)
    # barriga enorme com casaca e botões
    barriga = elipse(24, 27 + o, 11, 10.5)
    P.append(Parte(barriga, VERDE_F, z=1))
    casaca = {p for p in barriga if p[0] <= 21 or p[1] >= 34 + o}
    P.append(Parte(casaca, VERDE_F2, z=1.1, separar=False))
    for y in (21, 25, 29):
        px(P, [(30 + (1 if y == 25 else 0), y + o)], '#f9c22b', 1.2)
        px(P, [(30 + (1 if y == 25 else 0), y + 1 + o)], '#f79617', 1.2)
    px(P, [(x, 33 + o) for x in range(17, 33)], '#0b5e65', 1.15)         # cinto
    px(P, [(27, 33 + o), (28, 33 + o)], '#f9c22b', 1.2)
    # cabeça (enfiada nos ombros) com papada
    hx, hy = 30, 13 + o
    P.append(Parte(elipse(hx, hy, 5.6, 5.2) | elipse(hx + 1, hy + 5, 4.6, 2.6), VERDE_F, z=2, luz=0.1))
    # tricórnio com debrum de ouro e pena
    pena = fita(hx - 3, hy - 7, 1, 1.4, -9, fase, amp=0.6, fim=0.4) | capsula(hx - 3, hy - 7, hx - 11, hy - 6 + (f % 2), 1.4)
    P.append(Parte(pena, ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=2.4))
    chapeu = poligono([(hx - 8, hy - 4), (hx - 5, hy - 9), (hx + 1, hy - 10), (hx + 7, hy - 6), (hx + 8, hy - 3), (hx, hy - 5)])
    P.append(Parte(chapeu, ROXO_ESC, z=2.5))
    px(P, linha(hx - 8, hy - 4, hx, hy - 5) + linha(hx, hy - 5, hx + 8, hy - 3), '#f9c22b', 2.55)
    # cara: olho, nariz grande, bigode, boca a gritar
    if f == 3:
        olho_fechado(P, hx + 2, hy - 2, 2.6, 2)
    else:
        px(P, [(hx + 2, hy - 2), (hx + 3, hy - 2), (hx + 2, hy - 1), (hx + 3, hy - 1)], OUT, 2.6)
        px(P, [(hx + 3, hy - 1)], '#ffffff', 2.65)
    P.append(Parte(elipse(hx + 6, hy + 1, 1.8, 1.6), VERDE_F, z=2.7))     # nariz
    bigode = capsula(hx + 2, hy + 3, hx + 8, hy + 3, 1.2) | capsula(hx + 2, hy + 3, hx - 1, hy + 5, 1.0)
    P.append(Parte(bigode, ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'], z=2.8))
    px(P, elipse(hx + 5, hy + 6.5, 1.6, 1.4 + toque * 0.3), OUT, 2.75)
    px(P, [(hx + 5, hy + 7)], '#0b5e65', 2.76)
    # braço da frente a tocar o sino de ouro (à frente da barriga)
    P.append(Parte(capsula(29, 23 + o, 34, 27 + o, 2.4), VERDE_F, z=3))
    P.append(Parte(capsula(34, 27 + o, 38, 25 + o, 2.0), VERDE_F, z=3.1))
    sx, sy = 40 + (toque - 1), 27 + o
    P.append(Parte(capsula(39, 24 + o, sx, sy, 1.0), MADEIRA, z=3.2))
    sino = poligono([(sx - 3, sy + 1), (sx + 3, sy + 1), (sx + 4, sy + 6), (sx + 6, sy + 10), (sx - 6, sy + 10), (sx - 4, sy + 6)])
    sino |= elipse(sx, sy + 1.5, 3, 2)
    P.append(Parte(sino, OURO, z=3.3, volume='cilindro_v'))
    px(P, [(x, sy + 8) for x in range(sx - 4, sx + 5)], '#f79617', 3.35)
    px(P, [(sx - 2, sy + 3), (sx - 2, sy + 5)], '#ffffff', 3.35)
    P.append(Parte(elipse(sx + toque - 1, sy + 11.5, 1.4, 1.4), FERRO, z=3.25))   # badalo
    P.append(Parte(elipse(38.5, 24.5 + o, 2.2, 2), VERDE_F, z=3.4))       # mão
    # ondas de som
    for k in range(toque + 1):
        r = 3 + k * 3
        arco = [(sx + 3 + int(math.cos(a) * r), sy + 2 + int(math.sin(a) * r)) for a in [i * 0.2 - 1.5 for i in range(9)]]
        px(P, [p for p in arco if p[0] < 48], '#8ff8e2' if k == toque else '#30e1b9', 9)
    return desenhar(P, 48, 48)


def rainha_das_rosas_negras(f):
    """Espírito de rainha feito de rosas: vestido de rosas negras, ramos com espinhos à volta, coroa de espinhos
    com uma rosa, cabelo escuro comprido e um chicote de silvas na mão; pétalas a cair."""
    P = []
    b = [0, 0, 1, 1][f]
    PELE = ['#9babb2', '#c7dcd0', '#eaaded', '#ffffff', '#ffffff']
    CAB = ['#2e222f', '#45293f', '#45293f', '#831c5d', '#831c5d']
    # cabelo comprido atrás
    cab = fita(20, 6 + b, 22, 3.6, -5, f * 0.6, amp=1.0, ondas=0.7, fim=0.45)
    P.append(Parte(cab, CAB, z=0))
    # vestido em sino
    vest = poligono([(18, 21 + b), (28, 21 + b), (33, 33), (37, 46), (9, 46), (13, 33)])
    P.append(Parte(vest, ROSA_N, z=1, volume='cilindro_v'))
    # rosas no vestido (espiral de 3×3)
    rnd = random.Random(4)
    for y in range(24, 46, 4):
        for x in range(9, 38, 4):
            jx, jy = x + rnd.randint(0, 2), y + rnd.randint(-1, 1)
            if (jx, jy) not in miolo(vest) or (jx + 2, jy + 2) not in vest:
                continue
            cor = rnd.choice(('#c32454', '#831c5d', '#c32454', '#f04f78'))
            px(P, [(jx, jy), (jx + 1, jy), (jx + 2, jy + 1), (jx + 1, jy + 2), (jx, jy + 1)], cor, 1.1)
            px(P, [(jx + 1, jy + 1)], '#2e222f', 1.12)
            if cor == '#f04f78':
                px(P, [(jx, jy)], '#f68181', 1.13)
    # silvas a enrolar o vestido, com espinhos
    for k in range(2):
        pts = [(12 + k * 8 + t * 0.9 + math.sin(t * 0.4 + k) * 3, 26 + t) for t in range(0, 20, 2)]
        cordao = corda(pts, 0.7) & vest
        P.append(Parte(cordao, CAULE, z=1.2, separar=False))
        px(P, [(x + 1, y) for i, (x, y) in enumerate(pts) if i % 2], '#cddf6c', 1.25)
    # bainha em pétalas (recortada)
    px(P, [(x, 46) for x in range(10, 37) if x % 3 == 0], '#831c5d', 1.3)
    # corpete
    corp = poligono([(19, 13 + b), (26, 13 + b), (28.5, 22 + b), (17.5, 22 + b)])
    P.append(Parte(corp, ROSA_N, z=2, volume='cilindro_v'))
    px(P, linha(19, 16 + b, 27, 21 + b), '#239063', 2.05)
    px(P, [(21, 17 + b), (25, 20 + b)], '#cddf6c', 2.06)
    # braço de trás
    P.append(Parte(capsula(19, 14 + b, 16, 21 + b, 1.5), PELE, z=1.5))
    # cabeça pálida
    hx, hy = 25, 8 + b
    P.append(Parte(capsula(hx - 1, hy + 3, hx - 1, hy + 5, 1.4), PELE, z=2.5))
    P.append(Parte(elipse(hx, hy, 4.2, 4.4), PELE, z=3, luz=0.1))
    P.append(Parte({p for p in elipse(hx - 1, hy - 1, 4.7, 4) if p[1] <= hy - 3 or p[0] <= hx - 2}, CAB, z=3.5, separar=False))
    if f == 3:
        olho_fechado(P, hx + 2, hy - 1, 3.6, 2)
    else:
        px(P, [(hx + 2, hy - 1), (hx + 2, hy)], OUT, 3.6)
        px(P, [(hx + 3, hy)], '#e83b3b', 3.6)
        px(P, [(hx + 3, hy - 1)], '#f68181', 3.65)
    px(P, [(hx + 3, hy + 2), (hx + 2, hy + 2)], '#831c5d', 3.6)            # lábios
    px(P, [(hx + 2, hy - 2), (hx + 3, hy - 2)], OUT, 3.6)
    # coroa de espinhos com uma rosa
    for k in range(5):
        x = hx - 4 + k * 2
        P.append(Parte(capsula(x, hy - 4, x + (k % 2) - 0.5, hy - 7 - (k % 2), 0.6), CAULE, z=3.7))
    px(P, [(x, hy - 4) for x in range(hx - 4, hx + 4)], '#165a4c', 3.75)
    P.append(Parte(elipse(hx - 1, hy - 6, 1.8, 1.6), ROSA_N, z=3.8))
    px(P, [(hx - 1, hy - 6)], '#2e222f', 3.85)
    px(P, [(hx - 2, hy - 7)], '#f04f78', 3.85)
    # braço da frente com um chicote de silvas
    P.append(Parte(capsula(24, 14 + b, 29, 19 + b, 1.5), PELE, z=4))
    P.append(Parte(capsula(29, 19 + b, 33, 17 + b, 1.3), PELE, z=4.1))
    chic = [(33, 17 + b)] + [(33 + t * 1.3, 17 + b + math.sin(t * 0.7 + f) * 3 + t * 0.6) for t in range(1, 10)]
    P.append(Parte(corda(chic, 0.7), CAULE, z=4.2))
    px(P, [(x, y - 1) for i, (x, y) in enumerate(chic) if i % 2 == 1], '#cddf6c', 4.25)
    P.append(Parte(elipse(chic[-1][0], chic[-1][1], 1.6, 1.5), ROSA_N, z=4.3))
    # pétalas a cair
    for i in range(4):
        x = 6 + i * 11 + (f + i) % 3
        y = (i * 9 + f * 3) % 40 + 4
        px(P, [(x, y), (x + 1, y)], ['#c32454', '#831c5d'][i % 2], 9)
    return desenhar(P, 48, 48)


def sentinela_da_muralha(f):
    """Fantasma de arqueiro gigante: capuz e capa rasgada verde fantasma, olhos brancos, aljava às costas,
    arco grande com uma flecha de luz, as pernas a desfazerem-se em névoa."""
    P = []
    o = [0, -1, -1, 0][f]
    fase = f * math.pi / 2
    # capa atrás
    capa = poligono([(14, 12 + o), (24, 11 + o), (25, 34 + o), (18, 42 + o), (8, 41 + o), (10, 26 + o)])
    capa = rasgar(capa, 41, prof=4, dens=60)
    P.append(Parte(capa, VERDE_F2, z=0))
    # aljava com flechas
    P.append(Parte(capsula(13, 14 + o, 17, 28 + o, 2.2), MADEIRA, z=0.5))
    for k in range(3):
        P.append(Parte(capsula(12 + k * 1.5, 13 + o - k, 10 + k * 1.5, 8 + o - k, 0.6), ['#c7dcd0'] * 4 + ['#ffffff'], z=0.4))
        px(P, [(10 + k * 1.5, 7 + o - k)], '#e83b3b', 0.45)
    px(P, [(14, 18 + o), (15, 23 + o)], '#f9c22b', 0.55)
    # pernas que se desfazem em névoa
    for (x0, curva, z) in ((19, -3, 0.8), (24, -2, 1.6)):
        m = fita(x0, 30 + o, 15, 2.8, curva, fase + x0, amp=1.2, ondas=1.0, fim=0.15)
        P.append(Parte(m, VERDE_F if z > 1 else VERDE_F2, z=z))
    # braço de trás a puxar a corda
    P.append(Parte(capsula(18, 17 + o, 24, 22 + o, 1.8), VERDE_F2, z=1))
    P.append(Parte(capsula(24, 22 + o, 30, 21 + o, 1.6), VERDE_F2, z=1.1))
    # tronco (gibão de couro fantasma)
    tronco = poligono([(16, 13 + o), (26, 12 + o), (28, 20 + o), (27, 31 + o), (17, 31 + o)])
    P.append(Parte(tronco, VERDE_F, z=2, volume='cilindro_v'))
    px(P, [(x, 27 + o) for x in range(17, 28)], '#0b5e65', 2.05)          # cinto
    px(P, [(22, 27 + o)], '#f9c22b', 2.1)
    px(P, linha(17, 14 + o, 26, 26 + o), '#0b5e65', 2.05)                  # correia da aljava
    # capuz
    hx, hy = 25, 8 + o
    capuz = elipse(hx, hy, 5.2, 5.4) | capsula(hx - 2, hy - 3, hx - 8, hy + 1, 2)
    P.append(Parte(capuz, VERDE_F2, z=3))
    cara = elipse(hx + 2.5, hy + 1, 3, 3.6)
    px(P, cara, '#0b5e65', 3.1)
    px(P, {p for p in cara if p[0] <= hx + 1}, '#2e222f', 3.11)
    if f == 3:
        px(P, [(hx + 2, hy + 1), (hx + 3, hy + 1), (hx + 4, hy + 1)], '#30e1b9', 3.2)
    else:
        px(P, [(hx + 2, hy), (hx + 3, hy), (hx + 2, hy + 1)], '#8ff8e2', 3.2)
        px(P, [(hx + 3, hy)], '#ffffff', 3.25)
    px(P, [(hx + 3, hy + 3), (hx + 4, hy + 3)], '#30e1b9', 3.2)            # barba de névoa
    # arco grande à frente, corda e flecha de luz
    arco = [(36 + math.sin(t / 34 * math.pi) * 5 - 0, 4 + t + o) for t in range(0, 35)]
    P.append(Parte(corda(arco[::3] + [arco[-1]], 1.0), MADEIRA, z=4))
    px(P, [arco[0], arco[-1]], '#f9c22b', 4.05)
    corda_x = [(36 + (30 - 36) * (1 - abs(y - 21) / 17), y + o) for y in range(4, 39)]
    px(P, corda_x, '#c7dcd0', 3.9)
    flecha = linha(30, 21 + o, 45, 21 + o)
    px(P, flecha, '#8ff8e2', 4.1)
    px(P, [(46, 21 + o), (45, 20 + o), (45, 22 + o)], '#ffffff', 4.15)
    px(P, [(30, 20 + o), (31, 22 + o)], '#30e1b9', 4.15)
    # braço da frente a segurar o arco
    P.append(Parte(capsula(24, 15 + o, 30, 20 + o, 1.8), VERDE_F, z=5))
    P.append(Parte(capsula(30, 20 + o, 39, 21 + o, 1.6), VERDE_F, z=5.1))
    P.append(Parte(elipse(40.5, 21 + o, 1.8, 2), VERDE_F, z=5.2))
    # névoa a soltar-se
    particulas(P, 22, 30, 14, f, ['#8ff8e2', '#30e1b9'], 6, 13)
    return desenhar(P, 48, 48)


# ================================================================ lista e saída

CRIATURAS = [
    # (pasta, id, função)
    ('monstros', 'fantasma', fantasma),
    ('monstros', 'zombie', zombie),
    ('monstros', 'cavaleiro_esqueleto', cavaleiro_esqueleto),
    ('monstros', 'condessa_sangria', condessa_sangria),
    ('monstros', 'livro_possuido', livro_possuido),
    ('monstros', 'vampiro', vampiro),
    ('monstros', 'banshee', banshee),
    ('monstros', 'armadura_viva', armadura_viva),
    ('monstros', 'gargula', gargula),
    ('monstros', 'o_jardineiro', o_jardineiro),
    ('guardioes', 'sentinela_da_muralha', sentinela_da_muralha),
    ('guardioes', 'o_pregoeiro_fantasma', o_pregoeiro_fantasma),
    ('guardioes', 'coveiro_ghoul', coveiro_ghoul),
    ('guardioes', 'rainha_das_rosas_negras', rainha_das_rosas_negras),
    ('guardioes', 'anjo_caido_de_vitral', anjo_caido_de_vitral),
    ('guardioes', 'carcereiro', carcereiro),
    ('guardioes', 'comandante_dos_cavaleiros_caidos', comandante_dos_cavaleiros_caidos),
]


def antigo(pasta, ident):
    im = Image.open(os.path.join(ORIGEM, pasta, f'{ident}_parado_lado.png')).convert('RGBA')
    h = im.height
    return [im.crop((i * h, 0, i * h + h, h)) for i in range(im.width // h)], h


def nomes():
    n = {}
    for fch in ('monstros.json', 'bosses.json'):
        try:
            for e in json.load(open(os.path.join(RAIZ, 'dados', fch), encoding='utf-8')):
                if e.get('nome_pt'):
                    n[e['id']] = e['nome_pt']
        except (OSError, ValueError):
            pass
    return n


def verificar_paleta(img, ident):
    ok = {tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) for c in RESURRECT64}
    fora = {p[:3] for p in img.getdata() if p[3] and p[:3] not in ok}
    if fora:
        print(f'  !! {ident}: cores fora da paleta: {sorted(fora)[:6]}')
    meio = {p[3] for p in img.getdata()} - {0, 255}
    if meio:
        print(f'  !! {ident}: transparência a meio')


def escala_de(h):
    return {32: 3, 48: 2, 64: 2}.get(h, 1)


def grelha(itens, titulo, caminho, com_antes=True):
    """itens: (nome, antes_frames, depois_frames, lado). GIF animado em grelha (8 quadros, 160 ms)."""
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
    ft = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    pad = 10
    cel = []
    for nome, antes, depois, h in itens:
        s = escala_de(h)
        w = h * s * (2 if com_antes else 1) + (6 if com_antes else 0)
        tw = int(fonte.getlength(nome)) + 4
        cel.append((max(w, tw), h * s + 18))
    larg_max = 1200
    linhas, atual, lx = [], [], pad
    for i, (w, hh) in enumerate(cel):
        if atual and lx + w + pad > larg_max:
            linhas.append(atual)
            atual, lx = [], pad
        atual.append(i)
        lx += w + pad
    if atual:
        linhas.append(atual)
    alt_l = [max(cel[i][1] for i in l) for l in linhas]
    W = min(larg_max, max(sum(cel[i][0] + pad for i in l) + pad for l in linhas))
    H = 30 + sum(a + pad for a in alt_l) + pad
    quadros = []
    for t in range(8):
        im = Image.new('RGB', (W, H), (0x26, 0x2b, 0x3a))
        d = ImageDraw.Draw(im)
        d.text((pad, 8), titulo, fill=(230, 230, 240), font=ft)
        y = 30
        for li, l in enumerate(linhas):
            x = pad
            for i in l:
                nome, antes, depois, h = itens[i]
                s = escala_de(h)
                w, _ = cel[i]
                ox = x + (w - (h * s * (2 if com_antes else 1) + (6 if com_antes else 0))) // 2
                imgs = ([antes[t % len(antes)]] if com_antes else []) + [depois[t % len(depois)]]
                for k, fr in enumerate(imgs):
                    g = fr.resize((h * s, h * s), Image.NEAREST)
                    im.paste(g, (ox + k * (h * s + 6), y), g)
                if com_antes:
                    d.line([(ox + h * s + 2, y + 4), (ox + h * s + 2, y + h * s - 4)], fill=(70, 74, 100))
                tw = fonte.getlength(nome)
                d.text((x + (w - tw) / 2, y + h * s + 2), nome, fill=(220, 220, 230), font=fonte)
                x += w + pad
            y += alt_l[li] + pad
        quadros.append(im)
    quadros[0].save(caminho, save_all=True, append_images=quadros[1:], duration=160, loop=0, disposal=2)


def main(so=None):
    os.makedirs(DESTINO, exist_ok=True)
    nm = nomes()
    nm.setdefault('rainha_sem_rei', 'Rainha Sem Rei')
    itens = []
    for pasta, ident, fn in CRIATURAS:
        if so and ident not in so:
            continue
        antes, h = antigo(pasta, ident)
        depois = [fn(i) for i in range(4)]
        assert all(d.size == (h, h) for d in depois), ident
        tira = Image.new('RGBA', (h * 4, h), (0, 0, 0, 0))
        for i, d in enumerate(depois):
            tira.paste(d, (i * h, 0))
        verificar_paleta(tira, ident)
        tira.save(os.path.join(DESTINO, f'{ident}_parado_lado.png'))
        itens.append((nm.get(ident, ident), antes, depois, h))
        print('ok', ident, h)
    if not so:
        titulo = 'Região 8 — Reino Assombrado — antes | depois'
        grelha(itens, titulo, os.path.join(DESTINO, 'comparar.gif'))
        grelha(itens, 'Região 8 — Reino Assombrado — depois', os.path.join(DESTINO, 'depois.gif'), com_antes=False)
    return itens


if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
