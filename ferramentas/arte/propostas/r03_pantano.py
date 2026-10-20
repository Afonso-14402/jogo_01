"""PROPOSTA (ainda não aprovada): monstros, guardiões e bosses da Região 3 — Pântano e Selva, desenhados de novo.

Fichas: docs/regioes/r03_pantano.md (secções 3, 4, 6 e 9) e docs/BOSSES.md (secções 5 e 6).
Exemplo de qualidade seguido: ferramentas/arte/ent_anciao.py (formas orgânicas em várias partes, textura,
olhos com brilho, pormenores próprios em cada criatura).

Só desenha a animação "parado" (4 quadros), com o MESMO tamanho de quadro da arte atual do jogo.
NÃO mexe no jogo: grava só em arte/propostas/monstros/r03_pantano/
  <id>_parado_lado.png   (tira de 4 quadros)
  comparar.gif           (antes | depois, animado)
  depois.gif             (só os novos)

Uso (na raiz do repositório): python3 ferramentas/arte/propostas/r03_pantano.py
"""
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'arte'))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, dissolver, RAMPAS, _tom  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

OUT = '#2e222f'
BRANCO = '#ffffff'
SAIDA = os.path.join(RAIZ, 'arte', 'propostas', 'monstros', 'r03_pantano')
ANTIGA = os.path.join(RAIZ, 'arte', 'regioes', 'r03_pantano')

# ---------------------------------------------------------------- rampas (só cores da Resurrect 64)
VERDE = RAMPAS['verde']
VERDE_ESC = RAMPAS['verde_esc']
MUSGO = RAMPAS['musgo']
LAMA = ['#2e222f', '#4c3e24', '#676633', '#a2a947', '#d5e04b']
TOXICO = ['#165a4c', '#239063', '#91db69', '#d5e04b', '#fbff86']
BARRIGA = ['#676633', '#a2a947', '#b2ba90', '#d5e04b', '#fbff86']
CREME = ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff']
OSSO = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
PELO = ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']
PELO_RUIVO = ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e']
CARA = ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0']
FERRO = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
ACO = ['#3e3546', '#625565', '#9babb2', '#c7dcd0', '#ffffff']
MADEIRA = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
PEDRA = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
ROSA = RAMPAS['rosa']
VERMELHO = ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790']
ROXO = RAMPAS['roxo']
AGUA = RAMPAS['agua']
AZUL = RAMPAS['azul']
OURO = RAMPAS['ouro']
LARANJA = ['#6e2727', '#9e4539', '#fb6b1d', '#f79617', '#fbb954']
SANGUE = ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a']
CINZA = RAMPAS['cinza']
ASA = ['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2', '#ffffff']


# ---------------------------------------------------------------- ajudas
def px(P, pts, cor, z):
    """Píxeis soltos de uma cor (olhos, marcas, brilhos). Sem contorno."""
    m = {(int(math.floor(x)), int(math.floor(y))) for x, y in pts}
    if m:
        P.append(Parte(m, None, z=z, separar=False, cor=cor))


def mao(P, pix, z, separar=True):
    """Uma parte feita píxel a píxel {(x, y): cor}; com separar=True ganha um aro escuro à volta."""
    if not pix:
        return
    p = Parte(set(pix), None, z=z, separar=separar)
    p.pixels = dict(pix)
    P.append(p)


def _h(x, y, s):
    """Um número "ao calhas" fixo para cada píxel (a textura não treme entre quadros)."""
    n = (x * 374761393 + y * 668265263 + s * 2147483647) & 0xffffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0xffffffff
    return (n ^ (n >> 16)) & 0xffff


def parte(m, rampa, z, volume='esfera', tex=None, o=(0, 0), s=0, luz=0.0, brilho=True, separar=True, plano=False):
    """Uma parte com sombra do motor e depois TEXTURA (escamas, pelo, pintas...) que só sobe/desce um tom na rampa.

    tex: lista de funções f(pix, rampa, ox, oy, s) que mudam os tons; o = deslocamento do boneco nesse quadro
    (para a textura andar com o corpo e não "ferver")."""
    r = RAMPAS[rampa] if isinstance(rampa, str) else rampa
    p = Parte(m, r, z=z, volume=volume, luz=luz, brilho=brilho, separar=separar, plano=plano)
    if not m or not tex:
        return p
    xs = [q[0] for q in m]
    ys = [q[1] for q in m]
    bbox = (min(xs), min(ys), max(xs), max(ys))
    pix = {q: _tom(p, q[0], q[1], bbox) for q in m}
    for f in (tex if isinstance(tex, (list, tuple)) else [tex]):
        f(pix, r, o[0], o[1], s, m)
    p.pixels = pix
    return p


def _passo(pix, r, q, d):
    c = pix[q]
    if c not in r:
        return
    i = r.index(c)
    if d < 0 and i == 4 and r[3] == r[4]:
        i = 3
    pix[q] = r[max(0, min(4, i + d))]


def escamas(larg=4, alt=3, claro=True):
    """Escamas em arco desencontradas: um risco escuro em baixo de cada escama e um ponto claro em cima."""
    def f(pix, r, ox, oy, s, m):
        for (x, y) in list(pix):
            lx, ly = x - ox, y - oy
            fila = ly // alt
            cx = (lx + (fila % 2) * (larg // 2)) % larg
            cy = ly % alt
            borda = (x - 1, y) not in m or (x + 1, y) not in m or (x, y - 1) not in m or (x, y + 1) not in m
            if borda:
                continue
            if cy == alt - 1 and cx != 0:
                _passo(pix, r, (x, y), -1)
            elif claro and cy == 0 and cx == 1 and pix[(x, y)] in r and r.index(pix[(x, y)]) >= 2:
                _passo(pix, r, (x, y), +1)
    return f


def pelo(dens=5, comp=2):
    """Pelo: risquinhos inclinados mais escuros e alguns fios claros do lado da luz."""
    def f(pix, r, ox, oy, s, m):
        for (x, y) in list(pix):
            lx, ly = x - ox, y - oy
            k = _h((lx - ly // comp) // 1, ly // comp, s)
            if (x, y + 1) not in m or (x - 1, y) not in m or (x + 1, y) not in m:
                continue
            if k % dens == 0:
                _passo(pix, r, (x, y), -1)
            elif k % (dens * 3) == 1 and pix[(x, y)] in r and r.index(pix[(x, y)]) >= 2:
                _passo(pix, r, (x, y), +1)
    return f


def pintas(dens=7, cel=3, d=-1, limiar=None):
    """Manchas (pele de sapo, lama, pedra): blocos de cel×cel escolhidos ao calhas, um tom abaixo (d=-1) ou acima."""
    def f(pix, r, ox, oy, s, m):
        for (x, y) in list(pix):
            lx, ly = x - ox, y - oy
            k = _h(lx // cel, ly // cel, s)
            if k % dens == 0 and _h(lx, ly, s + 1) % 4 != 0:
                if (x, y + 1) in m and (x - 1, y) in m:
                    _passo(pix, r, (x, y), d)
    return f


def salpicos(dens=13, d=-1):
    """Píxeis soltos um tom abaixo/acima (grão de pedra, poros)."""
    def f(pix, r, ox, oy, s, m):
        for (x, y) in list(pix):
            if _h(x - ox, y - oy, s + 7) % dens == 0 and (x + 1, y) in m and (x, y + 1) in m:
                _passo(pix, r, (x, y), d)
    return f


def riscas(passo=3, eixo='x', d=-1, fase=0):
    """Anéis/riscas regulares (abdómen de inseto, anéis da sanguessuga)."""
    def f(pix, r, ox, oy, s, m):
        for (x, y) in list(pix):
            v = (x - ox) if eixo == 'x' else (y - oy)
            if (v + fase) % passo == 0:
                _passo(pix, r, (x, y), d)
    return f


def olho(P, x, y, iris, z=60, tam=2, pupila='redonda', fechado=False, aro=True, brilho=True):
    """Olho a olhar para a direita: íris de cor viva, pupila escura e um ponto branco de brilho."""
    x, y = int(x), int(y)
    if fechado:
        px(P, [(x + i, y + tam // 2) for i in range(tam)], OUT, z)
        return
    pix = {}
    if tam == 1:
        pix[(x, y)] = iris
    elif tam == 2:
        pix = {(x, y): BRANCO if brilho else iris, (x + 1, y): iris, (x, y + 1): iris, (x + 1, y + 1): OUT}
        if pupila == 'fenda':
            pix[(x + 1, y)] = OUT
    else:
        for i in range(tam):
            for j in range(tam):
                pix[(x + i, y + j)] = iris
        if pupila == 'fenda':
            for j in range(tam):
                pix[(x + tam // 2, y + j)] = OUT
        elif pupila == 'deitada':
            for i in range(tam):
                pix[(x + i, y + tam // 2)] = OUT
        else:
            for i in range(tam // 2, tam):
                for j in range(tam // 2, tam):
                    pix[(x + i, y + j)] = OUT
        if tam >= 4:
            for cx, cy in ((x, y), (x + tam - 1, y), (x, y + tam - 1), (x + tam - 1, y + tam - 1)):
                pix.pop((cx, cy), None)
            if brilho:
                pix[(x + 1, y)] = BRANCO
                pix[(x + 1, y + 1)] = BRANCO
        elif brilho:
            pix[(x, y)] = BRANCO
    mao(P, pix, z, separar=aro)


def curva(pts, n):
    """Pontos ao longo de uma curva de Bézier (lista de pontos de controlo)."""
    res = []
    for i in range(n):
        t = i / (n - 1)
        q = list(pts)
        while len(q) > 1:
            q = [(a[0] * (1 - t) + b[0] * t, a[1] * (1 - t) + b[1] * t) for a, b in zip(q, q[1:])]
        res.append(q[0])
    return res


def linha(x1, y1, x2, y2):
    """Uma linha de 1 píxel (Bresenham)."""
    x1, y1, x2, y2 = int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2))
    m = set()
    dx, dy = abs(x2 - x1), -abs(y2 - y1)
    sx, sy = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
    e = dx + dy
    while True:
        m.add((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * e
        if e2 >= dy:
            e += dy
            x1 += sx
        if e2 <= dx:
            e += dx
            y1 += sy
    return m


def tubo(pts, r0, r1, n=None):
    """Um corpo comprido (pescoço, cauda, serpente) que vai de raio r0 a r1 ao longo dos pontos."""
    m = set()
    for i, (a, b) in enumerate(zip(pts, pts[1:])):
        t = i / max(1, len(pts) - 2)
        m |= capsula(a[0], a[1], b[0], b[1], r0 + (r1 - r0) * t)
    return m


def recortar(m, y_max=None, y_min=None, x_max=None, x_min=None):
    return {(x, y) for (x, y) in m if (y_max is None or y <= y_max) and (y_min is None or y >= y_min)
            and (x_max is None or x <= x_max) and (x_min is None or x >= x_min)}


ONDA = [0, 1, 1, 0]          # respirar (sobe e desce devagar)
VAI = [0, 1, 0, -1]          # abanar para um lado e para o outro


# ====================================================================== 32×32
def sapo_venenoso(t):
    """Sapo-flecha venenoso: verde vivo com manchas azul-escuras de aviso, barriga amarela, olho dourado saliente,
    perna dobrada às riscas e o papo que incha (a animação parado). Baba de veneno a pingar."""
    P = []
    papo = [0, 1, 2, 1][t]
    PAPO = ['#a2a947', '#d5e04b', '#fbff86', '#ffffff', '#ffffff']
    # perna de trás de longe (só o pé)
    P.append(parte(capsula(13, 30, 18, 30, 0.9), VERDE, 0, luz=-0.4))
    # corpo, cabeça, focinho e a bossa do olho numa só peça (costas em rampa até à cabeça)
    corpo = (elipse(12.5, 24.2, 8.8, 5.6) | elipse(19.5, 20.5, 6.4, 5.0) | elipse(24.5, 21.4, 4.9, 3.3)
             | elipse(21.5, 16.3, 3.9, 3.7))
    P.append(parte(corpo, VERDE, 1, tex=[salpicos(13, +1)], s=3, luz=0.12))
    P.append(Parte(recortar(elipse(15, 28.5, 9, 3), y_min=27) & corpo, BARRIGA, z=1.1, separar=False))
    # manchas de aviso (azul muito escuro, com um ponto de brilho)
    for (sx, sy, rx, ry) in ((8.5, 21.5, 2.2, 1.6), (14, 19.6, 1.9, 1.4), (12, 25, 1.5, 1.1), (17.5, 23, 1.2, 1.0)):
        mm = elipse(sx, sy, rx, ry) & corpo
        px(P, mm, '#323353', 1.8)
        px(P, [(int(sx - rx * 0.4), int(sy - ry * 0.3))], '#484a77', 1.81)
    # olho grande e saliente (pupila deitada)
    olho(P, 20, 14, '#f9c22b', z=3, tam=4, pupila='deitada')
    # boca comprida e narina
    px(P, [(20, 21), (21, 22), (22, 22), (23, 22), (24, 22), (25, 22), (26, 22), (27, 22), (28, 21)], OUT, 3)
    px(P, [(27, 19)], OUT, 3)
    # papo a inchar debaixo do queixo
    P.append(Parte(elipse(25, 25.2 + papo * 0.25, 2.2 + papo * 0.8, 1.4 + papo * 0.55), PAPO, z=3.5))
    # coxa (perna de trás dobrada) às riscas, canela e pé comprido com dedos de ventosa
    coxa = elipse(10, 25.2, 5.0, 3.5)
    P.append(parte(coxa, VERDE, 4, luz=0.05))
    px(P, (linha(7, 22, 9, 28) | linha(11, 22, 13, 27)) & coxa, '#323353', 4.1)
    P.append(parte(capsula(14, 28.2, 6, 29.5, 1.4), VERDE, 4.2, luz=-0.1))
    P.append(parte(capsula(6, 30, 16, 30, 0.9), VERDE, 4.3, luz=-0.1))
    px(P, [(17, 30), (16, 29)], '#cddf6c', 4.4)
    # braço da frente com mão de ventosas
    P.append(parte(capsula(20.5, 25, 21.5, 29, 1.4), VERDE, 3.2))
    P.append(parte(capsula(19, 30, 24, 30, 0.9), VERDE, 3.3))
    px(P, [(19, 30), (24, 30)], '#cddf6c', 3.4)
    # baba de veneno a pingar do canto da boca
    if t >= 1:
        px(P, [(28, 22 + t)], '#d5e04b', 6)
    return desenhar(P, 32, 32)


def homem_lagarto_renegado(t):
    """Exilado da Aldeia Sssar: de pé, lança de aço, escudo de carapaça às costas, crista vermelha e cicatriz."""
    P = []
    b = ONDA[t]
    cauda = VAI[t]
    # cauda (sai de trás, assenta no chão)
    P.append(parte(tubo([(12, 21), (7, 25), (4 + cauda * 0.5, 28), (1 + cauda, 29)], 2.6, 1.0), VERDE_ESC, 0,
                   tex=[escamas(3, 2)], s=1))
    # perna de trás (longe)
    P.append(parte(capsula(13, 23, 11, 27, 1.8), VERDE_ESC, 1, luz=-0.25))
    P.append(parte(capsula(11, 27, 12, 30, 1.2), VERDE_ESC, 1.1, luz=-0.25))
    P.append(parte(capsula(12, 30, 15, 30, 0.8), VERDE_ESC, 1.2, luz=-0.25))
    # escudo de carapaça de tartaruga às costas
    esc = elipse(10, 16 + b, 4.2, 6.2)
    P.append(parte(esc, MADEIRA, 2, tex=[escamas(4, 4, claro=True)], s=4))
    px(P, [(10, 12 + b), (10, 20 + b), (8, 16 + b), (12, 16 + b)], '#c7dcd0', 2.1)
    # tronco com tiras de couro e saiote
    tronco = elipse(15.5, 17 + b, 4.3, 5.8)
    P.append(parte(tronco, VERDE_ESC, 3, tex=[escamas(3, 2)], s=2))
    P.append(Parte(recortar(elipse(17.5, 18 + b, 2.2, 4.2), x_min=17) & tronco, BARRIGA, z=3.1, separar=False))
    px(P, linha(12, 13 + b, 19, 21 + b) & tronco, '#694f62', 3.2)
    px(P, [(x, 22 + b) for x in range(12, 20)], '#45293f', 3.3)
    P.append(parte(poligono([(11.5, 21 + b), (20, 21 + b), (21, 25 + b), (11, 25 + b)]), MADEIRA, 3.4, plano=True))
    px(P, [(13, 24 + b), (16, 24 + b), (19, 24 + b)], '#4c3e24', 3.5)
    # perna da frente (dobrada, de lagarto) e pé com garras
    P.append(parte(capsula(17, 23, 19, 27, 2.0), VERDE_ESC, 4))
    P.append(parte(capsula(19, 27, 17, 30, 1.3), VERDE_ESC, 4.1))
    P.append(parte(capsula(17, 30, 21, 30, 0.9), VERDE_ESC, 4.2))
    px(P, [(22, 30)], '#c7dcd0', 4.3)
    # pescoço e cabeça (focinho comprido para a direita)
    P.append(parte(capsula(16.5, 12 + b, 18.5, 9 + b, 2.2), VERDE_ESC, 5))
    cab = elipse(20.5, 7.8 + b, 3.8, 3.2) | capsula(20, 8.5 + b, 27.5, 9.5 + b, 2.1)
    P.append(parte(cab, VERDE_ESC, 6, luz=0.1, tex=[escamas(3, 2)], s=5))
    px(P, recortar(capsula(21, 10.5 + b, 27.5, 10.5 + b, 1.0), y_min=int(10.5 + b)), '#b2ba90', 6.1)   # queixo claro
    px(P, [(x, int(10 + b)) for x in range(22, 28)], OUT, 6.2)                                         # boca
    px(P, [(24, int(11 + b)), (26, int(11 + b))], '#ffffff', 6.3)                                       # dentinhos
    px(P, [(27, int(8 + b))], OUT, 6.3)                                                                 # narina
    # crista vermelha (espinhos)
    for (cx, cy, h) in ((17, 7, 4), (19, 5, 4), (21.5, 4.5, 3)):
        P.append(Parte(poligono([(cx - 1.4, cy + b + 1), (cx - 1.6, cy - h + b), (cx + 1.6, cy + b + 0.5)]), VERMELHO, z=5.5))
    olho(P, 21, 6 + b, '#f9c22b', z=7, tam=2, pupila='fenda')
    px(P, [(23, 5 + b), (22, 6 + b) if False else (24, 4 + b)], '#fca790', 7.1)   # cicatriz por cima do olho
    # língua bífida (só num quadro)
    if t == 2:
        px(P, [(28, 10 + b), (29, 10 + b), (30, 9 + b), (30, 11 + b)], '#e83b3b', 7)
    # lança de aço (haste de madeira) e o braço da frente a segurá-la
    P.append(Parte(linha(26, 3 + b, 22, 31), None, z=8, separar=True, cor='#966c6c'))
    px(P, [(26, 6 + b), (25, 9 + b)], '#ab947a', 8.05)
    P.append(Parte(poligono([(25, 4 + b), (26.5, -0.5 + b), (28, 4 + b), (26.5, 5.5 + b)]), ACO, z=8.1))
    px(P, [(25, 5 + b), (27, 5 + b)], '#b33831', 8.2)                                                    # fita
    P.append(parte(capsula(17, 14 + b, 20, 17 + b, 1.4), VERDE_ESC, 9))
    P.append(parte(capsula(20, 17 + b, 23.5, 15 + b, 1.2), VERDE_ESC, 9.1))
    P.append(parte(elipse(24, 15 + b, 1.5, 1.5), VERDE_ESC, 9.2))
    px(P, [(18, 13 + b), (17, 13 + b)], '#c7dcd0', 9.3)                                                # dente ao pescoço
    return desenhar(P, 32, 32)


def _macaco(t, rei=False):
    P = []
    b = ONDA[t]
    a = VAI[t]
    # cauda enrolada atrás
    pts = curva([(11, 23), (2, 24), (1 + a, 12), (7 + a, 10), (8 + a, 14)], 9)
    P.append(parte(tubo(pts, 1.5, 1.1), PELO, 0, luz=-0.1))
    if rei:   # capa de folhas (atrás do corpo)
        capa = poligono([(10, 12 + b), (17, 12 + b), (17, 27), (13, 29), (9, 28), (6, 26), (7, 18)])
        P.append(parte(capa, VERDE, 1, tex=[pintas(4, 2, -1)], s=11))
        for i, (fx, fy) in enumerate(((6, 26), (9, 28), (13, 29), (7, 21))):
            P.append(Parte(poligono([(fx - 1.5, fy - 2), (fx + 2, fy - 2), (fx, fy + 2)]), VERDE, z=1.1 + i * 0.01))
        px(P, linha(9, 16 + b, 8, 25), '#165a4c', 1.2)
    else:     # saco do roubo às costas, com moedas a espreitar
        P.append(parte(elipse(8, 16 + b, 4.4, 4.6), PELO_RUIVO, 1, tex=[pintas(4, 2, -1)], s=12))
        px(P, [(6, 18 + b), (7, 19 + b), (10, 17 + b)], '#45293f', 1.1)
        P.append(Parte(elipse(8, 11.5 + b, 2.6, 1.5), OURO, z=0.9))
        px(P, [(7 + t % 2 * 2, 11 + b)], BRANCO, 0.95)
        P.append(Parte(capsula(10, 12 + b, 13, 14 + b, 0.8), MADEIRA, z=1.2))
    # pernas (de cócoras) e pés
    P.append(parte(elipse(12.5, 25.5, 4.4, 3.4), PELO, 2, luz=-0.15, tex=[pelo(5)], s=3))
    P.append(parte(capsula(12, 29.5, 18, 30, 1.2), CARA, 2.1, luz=-0.2))
    px(P, [(18, 31), (16, 31)], '#9e4539', 2.2)
    # corpo
    corpo = elipse(14.5, 19.5 + b * 0.5, 5.2, 6.4 if not rei else 6.8)
    P.append(parte(corpo, PELO, 3, tex=[pelo(4)], s=1))
    P.append(Parte(elipse(17, 21 + b * 0.5, 2.6, 4.2) & corpo, CARA, z=3.1, separar=False, luz=-0.1))
    # cabeça
    cab = elipse(17, 10.5 + b, 5.6, 5.2)
    P.append(parte(cab, PELO, 4, tex=[pelo(4)], s=2))
    P.append(parte(elipse(12.5, 10 + b, 2.1, 2.4), CARA, 4.1, luz=-0.2))                     # orelha
    px(P, [(12, 10 + b), (12, 11 + b)], '#9e4539', 4.15)
    cara = elipse(19.5, 10.5 + b, 3.7, 3.6) | elipse(21.5, 13 + b, 3.2, 2.4)
    P.append(Parte(cara, CARA, z=4.2))
    px(P, [(23, 12 + b), (24, 12 + b)], '#9e4539', 4.3)                                         # narinas
    if rei:   # sorriso bobo, dente de fora e língua
        px(P, [(19, 14 + b), (20, 15 + b), (21, 15 + b), (22, 15 + b), (23, 14 + b)], OUT, 4.4)
        px(P, [(21, 16 + b)], '#ffffff', 4.5)
        px(P, [(22, 16 + b), (22, 17 + b)], '#f04f78', 4.5)
        olho(P, 18, 8 + b, '#7a3045', z=5, tam=2)
        olho(P, 21, 8 + b, '#7a3045', z=5, tam=2)
        px(P, [(17, 7 + b), (18, 6 + b)] if t != 2 else [(17, 6 + b), (18, 6 + b)], '#45293f', 5.1)   # sobrancelha
    else:     # máscara de ladrão por cima dos olhos e sorriso matreiro
        mascara = retangulo(15, 8 + b, 23, 10 + b) - {(23, 10 + b), (15, 10 + b)}
        mao(P, {q: '#3e3546' for q in mascara}, 4.6, separar=False)
        px(P, [(14, 8 + b), (13, 9 + b), (13, 7 + b)], '#3e3546', 4.6)                          # nó da máscara
        if t == 3:
            olho(P, 19, 9 + b, '#ffffff', z=5, tam=2, fechado=True)
        else:
            px(P, [(19, 9 + b), (20, 9 + b), (21, 9 + b)], '#ffffff', 5)
            px(P, [(21, 9 + b)], OUT, 5.1)
        px(P, [(20, 14 + b), (21, 15 + b), (22, 15 + b), (23, 14 + b)], OUT, 4.4)
    # braço da frente com uma moeda (ou uma banana, o rei)
    P.append(parte(capsula(16, 16 + b, 19, 20 + b, 1.4), PELO, 6, tex=[pelo(4)], s=4))
    P.append(parte(capsula(19, 20 + b, 22, 18 + b, 1.2), PELO, 6.1))
    P.append(parte(elipse(23, 18 + b, 1.4, 1.3), CARA, 6.2))
    if rei:
        P.append(Parte(tubo(curva([(22, 18 + b), (25, 15 + b), (25, 11 + b)], 5), 1.3, 0.9), OURO, z=6.3))
        px(P, [(25, 10 + b)], '#4c3e24', 6.4)
    else:
        P.append(Parte(elipse(24.5, 16.5 + b, 1.6, 1.6), OURO, z=6.3))
        if t in (1, 2):
            px(P, [(26, 14 + b), (27, 13 + b), (25, 13 + b), (26, 12 + b) if t == 1 else (26, 13 + b)], '#fbff86', 6.4)
    if rei:   # coroa de cascas de banana a cair para os lados
        P.append(Parte(capsula(13, 6 + b, 21, 6 + b, 1.3), OURO, z=7))
        for i, (cx, ty, dx) in enumerate(((14, 1, -2), (17, 0, 0), (20, 1, 2))):
            casca = capsula(cx, 5 + b, cx + dx * 0.4, ty + b, 1.1) | capsula(cx + dx * 0.4, ty + b, cx + dx + (a if i != 1 else 0), ty + 3 + b, 0.8)
            P.append(Parte(casca, ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'], z=7.1 + i * 0.01))
        px(P, [(17, 0 + b)], '#4c3e24', 7.2)
        px(P, [(15, 6 + b), (19, 6 + b)], '#4c3e24', 7.2)
    return desenhar(P, 32, 32)


def macaco_ladrao(t):
    """Macaco ladrão: pelo castanho, máscara de bandido, saco de ouro às costas e uma moeda a brilhar na mão."""
    return _macaco(t)


def rei_macaco_bobo(t):
    """Rei Macaco Bobo: coroa de cascas de banana, capa de folhas, sorriso pateta com o dente de fora."""
    return _macaco(t, rei=True)


def mosquito_gigante(t):
    """Mosquito gigante a pairar: olhos vermelhos, tromba comprida, barriga cheia de sangue, asas que batem."""
    P = []
    dy = [0, -1, 0, 1][t]
    cima = t % 2 == 0
    # asa de longe (atrás)
    if cima:
        asa2 = poligono([(14, 9 + dy), (8, 1 + dy), (12, 0 + dy), (16, 7 + dy)])
    else:
        asa2 = poligono([(14, 10 + dy), (3, 8 + dy), (3, 10 + dy), (12, 12 + dy)])
    P.append(Parte(asa2, ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#30e1b9'], z=0, plano=True))
    # patas finas a pender (3 de cada lado; as de longe mais escuras)
    for i, (ax, kx, ky, fx, fy) in enumerate(((13, 10, 19, 7, 27), (15, 15, 21, 12, 29), (17, 20, 20, 23, 28))):
        cor = '#3e3546'
        P.append(Parte(linha(ax + 1, 14 + dy, kx + 2, ky + dy) | linha(kx + 2, ky + dy, fx + 2, fy + dy), None, z=0.5, separar=False, cor=cor))
        cor = '#625565'
        P.append(Parte(linha(ax, 14 + dy, kx, ky + dy) | linha(kx, ky + dy, fx, fy + dy), None, z=4, separar=False, cor=cor))
        px(P, [(fx, fy + dy)], '#9babb2', 4.1)
    # abdómen às riscas com a barriga vermelha de sangue
    abd = tubo([(13, 12 + dy), (8, 15 + dy), (3, 18 + dy)], 3.3, 2.0)
    P.append(parte(abd, SANGUE, 1, tex=[riscas(3, 'x', -1)], s=1))
    sangue = recortar(abd, y_min=15 + dy) & elipse(8, 18 + dy, 5.5, 2.6)
    P.append(Parte(sangue, VERMELHO, z=1.2, separar=False))
    px(P, [(6, 17 + dy), (9, 16 + dy)], '#fca790', 1.3)
    # tórax corcunda e cabeça
    P.append(parte(elipse(15.5, 11.5 + dy, 3.8, 3.4), PELO, 2, tex=[pelo(3)], s=2))
    px(P, [(14, 9 + dy), (16, 9 + dy), (15, 10 + dy)], '#c7dcd0', 2.1)
    P.append(parte(elipse(20.5, 12.5 + dy, 2.6, 2.4), SANGUE, 3))
    P.append(Parte(elipse(21, 12 + dy, 1.9, 1.9), VERMELHO, z=3.1))
    px(P, [(20, 11 + dy)], BRANCO, 3.2)
    px(P, [(22, 13 + dy)], '#6e2727', 3.2)
    # antenas de penugem
    P.append(Parte(linha(22, 10 + dy, 25, 6 + dy), None, z=3.3, separar=False, cor='#625565'))
    px(P, [(24, 7 + dy), (25, 8 + dy), (23, 7 + dy)], '#9babb2', 3.4)
    # tromba comprida (a picada)
    P.append(Parte(linha(23, 14 + dy, 30, 20 + dy), None, z=3.5, separar=True, cor='#3e3546'))
    px(P, [(30, 20 + dy)], '#e83b3b', 3.6)
    # asa de perto (translúcida, com nervuras)
    if cima:
        asa = poligono([(15, 9 + dy), (10, 0 + dy), (15, -1 + dy), (19, 7 + dy)])
    else:
        asa = poligono([(15, 10 + dy), (4, 11 + dy), (4, 14 + dy), (13, 13 + dy)])
    P.append(Parte(asa, ASA, z=5, plano=True))
    nerv = linha(15, 9 + dy, 12, 1 + dy) if cima else linha(15, 11 + dy, 5, 12 + dy)
    px(P, nerv & asa, '#0eaf9b', 5.1)
    return desenhar(P, 32, 32)


def sanguessuga_gigante(t):
    """Sanguessuga gigante a sair da água em arco: anéis escuros, risca vermelha, ventosa com dentinhos."""
    P = []
    a = [0, 1, 2, 1][t]
    # água e ondinhas
    agua = elipse(16, 29.5, 15.5, 2.2)
    P.append(Parte(agua, AGUA, z=0, plano=True))
    r1 = 6 + t
    px(P, [(16 - r1 * 2, 29), (16 + r1 * 2 - 1, 29)], '#8ff8e2', 0.1)
    px(P, [(x, 30) for x in range(3, 29) if (x + t * 2) % 7 == 0], '#30e1b9', 0.1)
    # corpo em arco (segmentos alternados: os aros escuros entre eles são os anéis)
    pts = curva([(5, 30), (6, 13 - a), (24 + a, 7 - a), (26 + a, 22 + a)], 14)
    for i in range(len(pts) - 1):
        r = 3.1 - 0.9 * abs(i - 6) / 7
        seg = capsula(*pts[i], *pts[i + 1], r)
        seg = recortar(seg, y_max=29)
        P.append(parte(seg, SANGUE, 1 + (i % 2) * 0.5 + i * 0.01, s=i, tex=[salpicos(9, +1)]))
        # risca vermelha e pintas laranja por cima (lado de fora do arco)
        cx, cy = pts[i]
        nx, ny = cx - 15, cy - 20
        n = math.hypot(nx, ny) or 1
        px(P, [(cx + nx / n * (r - 1), cy + ny / n * (r - 1))], '#b33831', 2.5 + i * 0.01)
        if i % 3 == 1:
            px(P, [(cx + nx / n * (r - 2.2), cy + ny / n * (r - 2.2))], '#f79617', 2.6)
    # brilho molhado
    px(P, [(6, 18 - a), (8, 13 - a), (12, 10 - a), (17, 8 - a)], '#9babb2', 2.7)
    # ventosa (boca redonda com dentinhos) virada para a frente/baixo
    hx, hy = pts[-1]
    boca = elipse(hx + 0.5, hy + 0.5, 2.6, 2.6)
    P.append(Parte(boca, VERMELHO, z=3))
    px(P, elipse(hx + 0.5, hy + 0.5, 1.2, 1.2), '#2e222f', 3.1)
    for (dx, dy) in ((-2, 0), (2, 0), (0, -2), (0, 2)):
        px(P, [(hx + dx + 0.5, hy + dy + 0.5)], '#fdcbb0', 3.2)
    # gotas a cair
    px(P, [(hx + 1, hy + 4 + t), (8, 24 + t % 2)], '#30e1b9', 3.3)
    return desenhar(P, 32, 32)


def bruxa_do_pantano(t):
    """Bruxa do pântano a mexer o caldeirão: pele verde, nariz com verruga, chapéu torto, poção a borbulhar."""
    P = []
    m = [0, 1, 2, 1][t]     # a mão a mexer a colher
    b = ONDA[t]
    # cabelo cinzento por trás
    for (x0, x1, c) in ((9, 7, 17), (10, 9, 18), (11, 10, 16)):
        P.append(parte(capsula(x0, 8 + b, x1, c + b, 1.1), CINZA, 0, luz=-0.1))
    # vestido roxo (corcunda) com remendo
    vest = poligono([(9, 13 + b), (15, 12 + b), (17, 22), (18, 30), (4, 30), (6, 22)])
    P.append(parte(vest, ROXO, 1, volume='cilindro_v', tex=[pintas(6, 2, -1)], s=5))
    P.append(Parte(retangulo(7, 24, 9, 26), None, z=1.1, separar=True, cor='#547e64'))
    px(P, [(7, 24), (9, 26), (8, 25)], '#374e4a', 1.2)
    px(P, [(x, 30) for x in range(5, 18) if x % 3 == 0], '#45293f', 1.2)     # bainha rasgada
    # caldeirão de ferro, fogo debaixo e a poção verde
    fogo = [(19, 29), (22, 30), (25, 29), (28, 30)]
    for i, (fx, fy) in enumerate(fogo):
        h = 2 + (i + t) % 3
        P.append(Parte(poligono([(fx - 1.5, fy + 1), (fx + (t % 2) - 0.5, fy - h), (fx + 1.5, fy + 1)]), LARANJA, z=2))
    cald = elipse(24, 25, 6.3, 4.6)
    P.append(Parte(cald, FERRO, z=3))
    px(P, [(19, 29), (29, 29)], '#3e3546', 3.05)
    P.append(Parte(capsula(17.5, 21, 30.5, 21, 1.2), FERRO, z=3.1, volume='cilindro_h'))
    P.append(Parte(elipse(24, 21, 5.6, 1.1), TOXICO, z=3.2, separar=False))
    for i in range(3):   # bolhas a subir
        k = (t + i * 2) % 4
        bx, by = 21 + i * 3, 20 - k * 2
        if k == 3:
            px(P, [(bx - 1, by), (bx + 1, by), (bx, by - 1)], '#91db69', 4)     # a rebentar
        else:
            px(P, [(bx, by)], '#d5e04b' if k else '#fbff86', 4)
    px(P, [(20, 24), (21, 23)], '#9babb2', 3.3)      # brilho do ferro
    # cabeça verde, queixo bicudo, nariz comprido com verruga
    cab = elipse(13.5, 10.5 + b, 3.6, 3.6) | capsula(14, 12 + b, 16, 14.5 + b, 1)
    P.append(parte(cab, VERDE, 4, luz=0.05))
    P.append(parte(capsula(16, 10 + b, 20, 12.5 + b, 1.0), VERDE, 4.1))
    px(P, [(18, 10 + b)], '#165a4c', 4.2)
    px(P, [(15, 13 + b), (16, 13 + b)], OUT, 4.2)
    px(P, [(16, 14 + b)], '#ffffff', 4.25)
    olho(P, 14, 9 + b, '#f9c22b', z=4.3, tam=1, aro=False)
    px(P, [(15, 9 + b)], OUT, 4.3)
    # chapéu preto torto, com fita roxa e fivela
    P.append(Parte(capsula(7, 7 + b, 19, 7 + b, 1.1), PEDRA, z=5, volume='cilindro_h'))
    cone = poligono([(9.5, 7 + b), (17.5, 7 + b), (14, 1 + b), (11, -1 + b), (8, 0 + b), (11, 2 + b)])
    P.append(Parte(cone, PEDRA, z=5.1))
    px(P, [(x, 6 + b) for x in range(10, 17)], '#6b3e75', 5.2)
    px(P, [(13, 6 + b)], '#f9c22b', 5.3)
    # braço a mexer a colher de pau
    hx, hy = 18 + m, 16 + b
    P.append(parte(capsula(14, 14 + b, hx, hy, 1.3), ROXO, 6))
    P.append(parte(elipse(hx + 0.5, hy, 1.3, 1.2), VERDE, 6.1))
    P.append(Parte(linha(hx + 1, hy - 3, hx + 3 - m, 22), None, z=2.9, separar=True, cor='#966c6c'))
    return desenhar(P, 32, 32)
