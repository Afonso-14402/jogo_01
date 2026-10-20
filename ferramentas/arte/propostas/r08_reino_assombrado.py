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
VERDE_F = ['#0b5e65', '#0b8a8f', '#30e1b9', '#8ff8e2', '#ffffff']       # verde fantasma (#8ff8e2)
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
