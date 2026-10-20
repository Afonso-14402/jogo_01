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
        elif tam == 3:
            pix[(x + 2, y + 1)] = OUT
            pix[(x + 2, y + 2)] = OUT
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
    PAPO = ['#676633', '#a2a947', '#d5e04b', '#fbff86', '#fbff86']
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
    P.append(Parte(elipse(25, 25.2 + papo * 0.25, 2.2 + papo * 0.6, 1.4 + papo * 0.45), PAPO, z=3.5))
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
    P.append(parte(tronco, VERDE_ESC, 3, tex=[escamas(4, 3)], s=2))
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
    cab = elipse(20, 8 + b, 4.2, 3.6) | capsula(20, 9 + b, 26, 9.6 + b, 2.2)
    P.append(parte(cab, VERDE_ESC, 6, luz=0.18, tex=[salpicos(9, -1)], s=5))
    px(P, recortar(capsula(20, 11 + b, 26, 11 + b, 1.0), y_min=int(11 + b)), '#b2ba90', 6.1)   # queixo claro
    px(P, [(x, int(10 + b)) for x in range(21, 27)] + [(20, int(9 + b))], OUT, 6.2)              # boca
    px(P, [(23, int(11 + b)), (25, int(11 + b))], '#ffffff', 6.3)                                # dentinhos
    px(P, [(26, int(8 + b))], OUT, 6.3)                                                          # narina
    # crista vermelha (espinhos)
    for (cx, cy, h) in ((16.5, 7, 4), (18.5, 5, 4), (21, 4.5, 3)):
        P.append(Parte(poligono([(cx - 1.4, cy + b + 1), (cx - 1.6, cy - h + b), (cx + 1.6, cy + b + 0.5)]), VERMELHO, z=5.5))
    olho(P, 20, 6 + b, '#f9c22b', z=7, tam=2, pupila='fenda')
    px(P, [(22, 5 + b), (23, 4 + b)], '#fca790', 7.1)                                            # cicatriz
    # língua bífida (só num quadro)
    if t == 2:
        px(P, [(27, 10 + b), (28, 10 + b), (29, 9 + b), (29, 11 + b)], '#e83b3b', 7)
    # lança de aço (haste de madeira) e o braço da frente a segurá-la
    P.append(Parte(linha(29, 4 + b, 28, 31), None, z=8, separar=True, cor='#966c6c'))
    P.append(Parte(poligono([(27.5, 4.5 + b), (29, -0.5 + b), (30.5, 4.5 + b), (29, 6 + b)]), ACO, z=8.1))
    px(P, [(28, 6 + b), (30, 6 + b)], '#b33831', 8.2)                                            # fita
    P.append(parte(capsula(17, 14 + b, 21, 19 + b, 1.4), VERDE_ESC, 9))
    P.append(parte(capsula(21, 19 + b, 26.5, 17 + b, 1.2), VERDE_ESC, 9.1))
    P.append(parte(elipse(27.5, 17 + b, 1.5, 1.5), VERDE_ESC, 9.2))
    px(P, [(17, 13 + b), (16, 13 + b)], '#c7dcd0', 9.3)                                          # dente ao pescoço
    return desenhar(P, 32, 32)


PELO_MAC = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
SACO = ['#45293f', '#6e2727', '#b33831', '#ea4f36', '#f57d4a']


def _macaco(t, rei=False):
    P = []
    b = ONDA[t]
    a = VAI[t]
    # cauda comprida enrolada atrás
    pts = curva([(11, 27), (1, 31), (-1 + a, 20), (4 + a, 18), (4 + a, 22)], 10)
    P.append(parte(tubo(pts, 1.4, 1.0), PELO_MAC, 0, luz=0.05))
    if rei:   # capa de folhas (atrás do corpo), com a borda recortada em folhas
        capa = poligono([(12, 14 + b), (17, 14 + b), (16, 27), (12, 29.5), (7, 29), (6, 24), (8, 18 + b)])
        P.append(parte(capa, VERDE, 1, tex=[pintas(4, 2, -1)], s=11))
        for i, (fx, fy) in enumerate(((6, 27), (9, 29), (13, 29), (6, 22))):
            P.append(Parte(poligono([(fx - 2, fy - 2), (fx + 2, fy - 2), (fx, fy + 2)]), VERDE, z=1.1 + i * 0.01))
        px(P, linha(10, 17 + b, 9, 27), '#165a4c', 1.2)
        px(P, [(13, 15 + b), (14, 15 + b)], '#f9c22b', 1.3)            # o alfinete da capa
    else:     # saco do roubo às costas, com moedas a espreitar
        P.append(parte(elipse(8.5, 18.5 + b, 4.4, 4.6), SACO, 1, tex=[pintas(4, 2, -1)], s=12))
        px(P, [(7, 21 + b), (6, 18 + b), (9, 22 + b)], '#6e2727', 1.1)
        P.append(Parte(elipse(9, 13.8 + b, 2.6, 1.5), OURO, z=0.9))
        px(P, [(8 + (t % 2) * 2, 13 + b)], BRANCO, 0.95)
        P.append(Parte(capsula(11, 15 + b, 15, 17 + b, 0.8), MADEIRA, z=1.2))
    # perna (de cócoras) e pé
    P.append(parte(elipse(15, 26.5, 4.6, 3.2), PELO_MAC, 2, tex=[pelo(7)], s=3))
    P.append(parte(capsula(14, 30, 20, 30, 1.1), CARA, 2.1, luz=-0.2))
    px(P, [(20, 31), (18, 31)], '#9e4539', 2.2)
    # corpo com a barriga clara
    corpo = elipse(15.5, 21 + b * 0.5, 5.2, 6.2)
    P.append(parte(corpo, PELO_MAC, 3, tex=[pelo(7)], s=1))
    P.append(Parte(elipse(18.5, 22 + b * 0.5, 2.4, 4.0) & corpo, CARA, z=3.1, separar=False, luz=-0.2))
    # cabeça grande, orelha, cara clara e focinho
    cab = elipse(18.5, 11 + b, 6.0, 5.4)
    P.append(parte(cab, PELO_MAC, 4, tex=[pelo(7)], s=2, luz=0.05))
    P.append(parte(elipse(13, 11.5 + b, 2.0, 2.3), CARA, 4.1, luz=-0.2))
    px(P, [(13, 12 + b)], '#9e4539', 4.15)
    cara = elipse(21.3, 12 + b, 3.6, 3.8) | elipse(23.5, 14.5 + b, 2.7, 2.1)
    P.append(Parte(cara, CARA, z=4.2))
    px(P, [(25, 13 + b)], '#9e4539', 4.3)                                         # narina
    if rei:   # sorriso pateta, dente de fora e língua; olhos tontos
        px(P, [(20, 15 + b), (21, 16 + b), (22, 16 + b), (23, 16 + b), (24, 16 + b), (25, 15 + b)], OUT, 4.4)
        px(P, [(22, 17 + b)], '#ffffff', 4.5)
        px(P, [(23, 17 + b)], '#f04f78', 4.5)
        px(P, [(19, 9 + b), (20, 9 + b), (22, 9 + b), (23, 9 + b), (19, 10 + b), (20, 10 + b), (22, 10 + b), (23, 10 + b)], '#ffffff', 5)
        px(P, [(20, 10 + b), (22, 10 + b)] if t != 2 else [(20, 9 + b), (23, 10 + b)], OUT, 5.1)   # vesgo
        px(P, [(18, 8 + b), (19, 7 + b)], '#4c3e24', 5.1)
    else:     # máscara de ladrão por cima dos olhos e sorriso matreiro
        mascara = retangulo(16, 9 + b, 25, 11 + b) - {(25, 11 + b), (16, 11 + b), (25, 9 + b)}
        mao(P, {q: '#3e3546' for q in mascara}, 4.6, separar=False)
        px(P, [(15, 9 + b), (14, 8 + b), (14, 10 + b), (13, 9 + b)], '#3e3546', 4.6)       # nó da máscara
        px(P, [(17, 9 + b), (18, 9 + b)], '#625565', 4.65)
        if t == 3:
            px(P, [(21, 10 + b), (22, 10 + b), (23, 10 + b)], OUT, 5)
        else:
            px(P, [(21, 10 + b), (22, 10 + b), (23, 10 + b)], '#ffffff', 5)
            px(P, [(23, 10 + b)], OUT, 5.1)
        px(P, [(21, 16 + b), (22, 16 + b), (23, 16 + b), (24, 15 + b)], OUT, 4.4)
    # braço da frente com uma moeda (ou uma banana, o rei)
    P.append(parte(capsula(17, 18 + b, 20, 22 + b, 1.4), PELO_MAC, 6))
    P.append(parte(capsula(20, 22 + b, 23, 20 + b, 1.2), PELO_MAC, 6.1))
    P.append(parte(elipse(24, 20 + b, 1.4, 1.3), CARA, 6.2))
    if rei:
        P.append(Parte(tubo(curva([(23, 20 + b), (27, 18 + b), (27.5, 13 + b)], 5), 1.4, 0.9), OURO, z=6.3))
        px(P, [(27, 12 + b)], '#4c3e24', 6.4)
    else:
        P.append(Parte(elipse(26, 18.5 + b, 1.7, 1.7), OURO, z=6.3))
        if t in (1, 2):
            px(P, [(28, 16 + b), (29, 15 + b), (27, 15 + b), (28, 14 + b)] if t == 1 else [(28, 16 + b)], '#fbff86', 6.4)
    if rei:   # coroa de cascas de banana a cair para os lados
        P.append(Parte(capsula(14, 6 + b, 22, 6 + b, 1.3), OURO, z=7))
        for i, (cx, ty, dx) in enumerate(((15, 1, -3), (18, 0, 0), (21, 1, 3))):
            casca = (capsula(cx, 5 + b, cx + dx * 0.3, ty + b, 1.1)
                     | capsula(cx + dx * 0.3, ty + b, cx + dx + (a if i != 1 else 0), ty + 3 + b, 0.8))
            P.append(Parte(casca, ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#fbff86'], z=7.1 + i * 0.01))
        px(P, [(18, 0 + b)], '#4c3e24', 7.2)
        px(P, [(16, 6 + b), (20, 6 + b)], '#4c3e24', 7.2)
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
    """Bruxa do pântano a mexer o caldeirão: pele verde, nariz adunco com verruga, cabelo cinzento em fios,
    chapéu torto com fivela, vestido remendado, poção verde a borbulhar e fogo por baixo."""
    P = []
    m = [0, 1, 2, 1][t]     # a mão a mexer a colher
    b = ONDA[t]
    VESTIDO = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#a884f3']
    # vestido roxo (corcunda) com remendo e bainha rasgada
    vest = poligono([(8, 15 + b), (14, 14 + b), (17, 22), (18, 30.5), (3.5, 30.5), (5.5, 21)])
    P.append(parte(vest, VESTIDO, 1, volume='cilindro_v', tex=[pintas(6, 2, -1)], s=5))
    P.append(Parte(retangulo(6, 24, 8, 26), None, z=1.1, separar=True, cor='#547e64'))
    px(P, [(6, 24), (8, 26)], '#374e4a', 1.2)
    px(P, [(x, 30) for x in range(5, 18) if x % 3 == 0], '#2e222f', 1.2)
    # cabelo cinzento em fios por cima dos ombros
    for (x0, x1, c) in ((10, 7, 18), (11, 9, 17), (12, 11, 16)):
        P.append(parte(capsula(x0, 9 + b, x1, c + b, 0.9), CINZA, 1.5))
    # fogo e lenha debaixo do caldeirão
    P.append(Parte(capsula(18, 31, 30, 31, 0.7), MADEIRA, z=1.8))
    for i, fx in enumerate((19.5, 22.5, 25.5, 28.5)):
        h = 2 + (i + t) % 3
        P.append(Parte(poligono([(fx - 1.6, 31), (fx + (t + i) % 2 - 0.5, 30 - h), (fx + 1.6, 31)]), LARANJA, z=2))
    # caldeirão de ferro e a poção verde
    cald = elipse(24, 24.5, 6.2, 4.4)
    P.append(Parte(cald, FERRO, z=3))
    P.append(Parte(capsula(17.5, 21, 30.5, 21, 1.2), FERRO, z=3.1, volume='cilindro_h'))
    P.append(Parte(elipse(24, 21, 5.6, 1.1), TOXICO, z=3.2, separar=False))
    px(P, [(20, 24), (21, 23)], '#9babb2', 3.3)      # brilho do ferro
    px(P, [(23, 26), (24, 26), (25, 26), (24, 25)], '#3e3546', 3.3)   # caveirinha gravada
    for i in range(3):   # bolhas a subir
        k = (t + i * 2) % 4
        bx, by = 21 + i * 3, 19 - k * 2
        if k == 3:
            px(P, [(bx - 1, by), (bx + 1, by), (bx, by - 1)], '#91db69', 4)     # a rebentar
        else:
            px(P, [(bx, by)], '#d5e04b' if k else '#fbff86', 4)
    # cabeça verde, queixo bicudo, nariz comprido e adunco com verruga
    cab = elipse(13.5, 11 + b, 3.8, 3.8) | capsula(14, 13 + b, 15.5, 15.5 + b, 1)
    P.append(parte(cab, VERDE, 4, luz=-0.12))
    P.append(parte(capsula(16, 10.5 + b, 20.5, 13.5 + b, 1.1), VERDE, 4.1, luz=-0.1))
    px(P, [(18, 11 + b)], '#165a4c', 4.2)
    px(P, [(15, 14 + b), (16, 14 + b)], OUT, 4.2)
    px(P, [(16, 15 + b)], '#ffffff', 4.25)
    px(P, [(14, 10 + b)], '#f9c22b', 4.3)
    px(P, [(15, 10 + b)], OUT, 4.3)
    px(P, [(13, 9 + b), (14, 9 + b), (15, 9 + b)] if t != 3 else [(14, 10 + b), (15, 10 + b)], '#165a4c', 4.35)
    # chapéu preto torto, com fita roxa e fivela
    P.append(Parte(capsula(7, 7.5 + b, 19, 7.5 + b, 1.1), PEDRA, z=5, volume='cilindro_h'))
    cone = poligono([(9.5, 7.5 + b), (17.5, 7.5 + b), (14, 1.5 + b), (11, -0.5 + b), (7, 0.5 + b), (11, 2.5 + b)])
    P.append(Parte(cone, PEDRA, z=5.1))
    px(P, [(x, int(6 + b)) for x in range(10, 17)], '#6b3e75', 5.2)
    px(P, [(13, int(6 + b))], '#f9c22b', 5.3)
    # braço a mexer a colher de pau (a colher entra na poção)
    hx, hy = 17 + m, 19 + b
    P.append(Parte(linha(hx + 1, hy - 3, hx + 3 - m, 21), None, z=3.25, separar=True, cor='#966c6c'))
    P.append(parte(capsula(12, 18 + b, hx, hy, 1.3), VESTIDO, 6))
    P.append(parte(elipse(hx + 0.8, hy, 1.3, 1.2), VERDE, 6.1))
    return desenhar(P, 32, 32)


# ====================================================================== 48×48 (e a Mãe-Crocodilo, 64×64)
def _croc(t, S=48, velha=False):
    """Crocodilo de lado, baixo e comprido: focinho com dentes de fora, olho na bossa, fila de escudos nas costas.
    velha=True: a Mãe-Crocodilo (algas penduradas, conchas, cracas, cicatrizes e um dente partido)."""
    P = []
    k = S / 48
    b = ONDA[t] * 0.6
    a = VAI[t]

    def Q(x, y):
        return (x * k, y * k)

    def C(x1, y1, x2, y2, r):
        return capsula(x1 * k, y1 * k, x2 * k, y2 * k, r * k)

    def E(x, y, rx, ry):
        return elipse(x * k, y * k, rx * k, ry * k)

    ESC = VERDE_ESC
    if velha:
        ESC = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']
    tex = [escamas(4, 3), pintas(8, 3, -1)]
    # patas de longe
    P.append(parte(C(14, 41, 11, 45.5, 2.2), ESC, 0, luz=-0.35))
    P.append(parte(C(31, 41, 34, 45.5, 2.0), ESC, 0, luz=-0.35))
    # cauda (abana a ponta)
    cauda = tubo([Q(15, 37 + b), Q(8, 39), Q(3, 41 + a * 0.5), Q(-1, 42 + a)], 4.6 * k, 1.2 * k)
    P.append(parte(cauda, ESC, 1, tex=tex, s=1))
    # corpo
    corpo = E(23, 37.4 + b, 12.5, 7.2)
    P.append(parte(corpo, ESC, 2, tex=tex, s=2, luz=0.12))
    barriga = recortar(E(24, 42 + b, 11.5, 3.6), y_min=int(41.2 * k + b))
    P.append(parte(barriga & corpo, BARRIGA, 2.1, separar=False, tex=[riscas(3, 'x', -1)], s=1))
    # escudos (osteodermos) em fila nas costas e na cauda: pequenos dentes de serra em cima do contorno
    for i, x in enumerate(range(4, 34, 3)):
        if x >= 11:
            yb = 37.4 + b - 7.2 * math.sqrt(max(0.0, 1 - ((x - 23) / 12.5) ** 2))
        else:
            yb = 37 - 4.6 + (11 - x) * 0.55 + (a * 0.5 if x < 5 else 0)
        esc = poligono([((x - 1.4) * k, (yb + 1.6) * k), (x * k, (yb - 1.8) * k), ((x + 1.4) * k, (yb + 1.6) * k)])
        P.append(Parte(esc, ESC, z=2.05 + i * 0.001))
    # cabeça: crânio, bossa do olho, maxila com dentes e mandíbula
    boca = 1 if t == 2 else 0
    P.append(parte(E(37.5, 36.5 + b, 5.6, 4.8), ESC, 3, tex=[escamas(3, 2)], s=3, luz=0.1))
    P.append(parte(C(38, 38.3 + b, 46.5, 38.8 + b, 2.6), ESC, 3.2, luz=0.15, tex=[salpicos(7, -1)], s=4))
    P.append(parte(C(37, 42 + b + boca, 45, 41.8 + b + boca, 1.5), ESC, 3.1, luz=-0.15))
    px(P, [Q(46, 37.2 + b)], OUT, 3.3)                                                # narina
    px(P, [(x, int(40.6 * k + b)) for x in range(int(36 * k), int(47 * k))], OUT, 3.3)   # boca
    dentes = [Q(x, 40.6 + b + (0 if i % 2 else 1)) for i, x in enumerate(range(37, 47, 2))]
    if velha:
        dentes = dentes[:2] + dentes[3:]
    px(P, dentes, '#ffffff', 3.4)
    px(P, [Q(x, 41.6 + b + boca) for x in range(38, 46, 3)], '#c7dcd0', 3.4)
    P.append(parte(E(37, 32.6 + b, 2.8, 2.3), ESC, 3.5, luz=0.1))
    olho(P, 35.5 * k, 31 * k + b, '#f9c22b', z=3.6, tam=3, pupila='redonda', fechado=(t == 3))
    # patas de perto, com garras claras
    P.append(parte(E(16, 41.5 + b, 3.8, 3.0), ESC, 4, tex=tex, s=5))
    P.append(parte(C(16, 42, 18, 45.5, 2.0), ESC, 4.1))
    P.append(parte(C(16, 46, 21, 46, 1.1), ESC, 4.2))
    P.append(parte(C(31, 41 + b, 30, 45.5, 1.9), ESC, 4.3))
    P.append(parte(C(30, 46, 35, 46, 1.1), ESC, 4.4))
    px(P, [Q(21.5, 46.4), Q(35.5, 46.4)], '#c7dcd0', 4.5)
    if velha:
        # musgo nas costas e algas compridas penduradas a abanar
        musgo = {q for q in recortar(corpo, y_max=int(33.5 * k)) if _h(q[0], q[1], 5) % 3}
        P.append(Parte(musgo, ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#d5e04b'], z=4.9, separar=False))
        for i, (x, comp) in enumerate(((11, 6), (19, 9), (27, 5))):
            ox = (a if i % 2 else -a) * 0.7
            yt = 37.4 - 7.2 * math.sqrt(max(0.0, 1 - ((x - 23) / 12.5) ** 2)) + 1
            alga = tubo([Q(x, yt + b), Q(x - 1 + ox * 0.5, yt + comp * 0.5 + b), Q(x + ox, yt + comp + b)], 1.1 * k, 0.6 * k)
            P.append(Parte(alga, ['#165a4c', '#239063', '#1ebc73', '#91db69', '#91db69'], z=5 + i * 0.01))
        for (cx, cy) in ((21, 36), (14, 38.5)):
            P.append(Parte(E(cx, cy + b, 1.2, 1.0), ['#7f708a', '#9babb2', '#fdcbb0', '#ffffff', '#ffffff'], z=5.5))
            px(P, [Q(cx + 0.5, cy + 0.5 + b)], '#cf657f', 5.6)
        for (cx, cy) in ((30, 34.5), (33, 36), (23, 34)):
            px(P, [Q(cx, cy + b), Q(cx + 1 / k, cy + b)], '#c7dcd0', 5.6)
            px(P, [Q(cx, cy + 1 / k + b)], '#625565', 5.6)
        px(P, linha(*Q(39, 35.5 + b), *Q(43, 38.5 + b)), '#966c6c', 5.7)              # cicatriz no focinho
        px(P, linha(*Q(20, 37 + b), *Q(23, 41 + b)), '#625565', 5.7)
    return desenhar(P, S, S)


def crocodilo(t):
    """Crocodilo do pântano: verde-acinzentado, barriga amarelada às riscas, escudos nas costas, dentes de fora."""
    return _croc(t)


def mae_crocodilo_mandibula(t):
    """Mãe-Crocodilo Mandíbula: crocodilo velho e enorme coberto de algas e conchas, cicatrizes, dente partido."""
    return _croc(t, S=64, velha=True)


def flor_carnivora(t):
    """Flor carnívora: roseta de folhas, caule grosso com espinhos, coroa de pétalas e boca de dentes que baba."""
    P = []
    a = VAI[t]
    ab = [0, 1, 1, 0][t]              # abre um bocadinho a boca
    hx, hy = 27 + a * 0.6, 19         # centro da cabeça
    # folhas no chão (roseta)
    for i, (x1, y1, x2, y2, w) in enumerate(((22, 45, 7, 41, 3.2), (22, 45, 37, 42, 3.0), (21, 45, 12, 36, 2.6), (23, 45, 32, 37, 2.4))):
        folha = capsula(x1, y1, (x1 + x2) / 2, (y1 + y2) / 2 - 1, w) | capsula((x1 + x2) / 2, (y1 + y2) / 2 - 1, x2, y2, w * 0.45)
        P.append(parte(folha, VERDE, 0 + i * 0.01, luz=-0.1 if i < 2 else 0.05))
        px(P, linha(x1, y1 - 1, x2, y2), '#165a4c', 0.005 + i * 0.01)
    P.append(parte(elipse(22, 46, 6, 1.6), LAMA, 0.5, plano=True))
    # caule em curva com espinhos e uma folhinha
    caule = curva([(22, 45), (17, 35), (24, 30), (hx - 4, hy + 4)], 8)
    P.append(parte(tubo(caule, 2.6, 2.0), VERDE, 1, volume='cilindro_v', tex=[riscas(4, 'y', -1)], s=2))
    for (sx, sy, dx) in ((18, 38, -2), (20, 32, -2), (22, 35, 2)):
        px(P, [(sx + dx, sy), (sx + dx + (1 if dx > 0 else -1), sy - 1)], '#cddf6c', 1.1)
    folha = capsula(19, 33, 12, 29, 1.8)
    P.append(parte(folha, VERDE, 1.2))
    # coroa de pétalas atrás da cabeça
    for i, ang in enumerate((150, 190, 230, 270, 110)):
        r = math.radians(ang)
        px_, py_ = hx - 2 + math.cos(r) * 9, hy + math.sin(r) * 8
        pet = capsula(hx - 2, hy, px_, py_, 3.3 if i % 2 == 0 else 2.6)
        P.append(parte(pet, ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'], 2 + i * 0.01, luz=0.05))
        px(P, [(hx - 2 + math.cos(r) * 7, hy + math.sin(r) * 6)], '#fdcbb0', 2.05 + i * 0.01)
    # cabeça: maxila de cima (vermelha com pintas), boca escura com dentes, maxila de baixo
    cima = recortar(elipse(hx + 4, hy, 10, 6.5), y_max=int(hy))
    baixo = recortar(elipse(hx + 3.5, hy + 1 + ab, 9, 4.5), y_min=int(hy + 1 + ab))
    dentro = elipse(hx + 5, hy + 0.5 + ab * 0.5, 8, 1.6 + ab * 0.6)
    P.append(Parte(dentro, ['#2e222f', '#6e2727', '#831c5d', '#c32454', '#c32454'], z=3))
    P.append(parte(baixo, VERMELHO, 3.2, tex=[pintas(5, 2, +1)], s=7))
    P.append(parte(cima, VERMELHO, 3.4, tex=[pintas(4, 2, +1)], s=8))
    for x in range(int(hx - 3), int(hx + 13), 3):           # dentes de cima e de baixo
        px(P, [(x, hy + 1), (x + 1, hy + 1), (x, hy + 2)], '#ffffff', 3.5)
        px(P, [(x + 1, hy + 2 + ab), (x + 1, hy + 1 + ab)], '#c7dcd0', 3.1)
    px(P, [(hx + 2, hy - 4), (hx + 6, hy - 5), (hx + 9, hy - 3), (hx - 1, hy - 2)], '#fca790', 3.6)   # pintas claras
    # baba (néctar) a pingar
    px(P, [(hx + 10, hy + 3 + ab), (hx + 10, hy + 4 + ab + t)], '#d5e04b', 3.7)
    if t == 3:
        px(P, [(hx + 10, hy + 9)], '#91db69', 3.7)
    return desenhar(P, 48, 48)


def garca_lanca(t):
    """Garça-Lança: garça cinzenta gigante de pé, pescoço branco em S, poupa preta, bico comprido como uma lança
    (base amarela e ponta de aço a brilhar), asa dobrada com as pontas escuras e patas amarelas."""
    P = []
    b = ONDA[t]
    a = VAI[t]
    PATA = ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#f9c22b']
    BRANCA = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
    # patas compridas (a de trás mais escura) e dedos abertos
    P.append(Parte(capsula(18, 30, 17, 45.5, 0.8), PATA, z=0, luz=-0.3))
    P.append(Parte(linha(14, 46, 20, 46), None, z=0.1, separar=False, cor='#9e4539'))
    P.append(Parte(capsula(22, 30, 23, 45.5, 0.9), PATA, z=3))
    px(P, [(23, 37), (22, 37)], '#cd683d', 3.1)                       # joelho
    P.append(Parte(linha(19, 46, 28, 46) | linha(23, 46, 21, 44), None, z=3.1, separar=True, cor='#cd683d'))
    # cauda de penas e corpo
    for i, (x2, y2) in enumerate(((6, 33), (7, 30), (8, 35))):
        P.append(parte(capsula(14, 28 + b, x2, y2 + b, 1.6), CINZA, 0.5 + i * 0.01, luz=-0.15))
    corpo = elipse(19, 25.5 + b, 9.5, 6.2)
    P.append(parte(corpo, CINZA, 1, tex=[escamas(3, 2)], s=3))
    P.append(Parte(recortar(elipse(22, 28 + b, 6, 3.2), y_min=int(28 + b)) & corpo, BRANCA, z=1.1, separar=False))
    # penas do peito penduradas
    for i, x in enumerate((24, 26, 28)):
        px(P, linha(x, 21 + b, x - 1 + (a if i == 1 else 0), 28 + b), '#c7dcd0', 1.2)
    # pescoço branco em S e cabeça
    pesc = curva([(24, 22 + b), (30, 17 + b), (23, 12 + b), (27, 7 + b)], 9)
    P.append(parte(tubo(pesc, 2.4, 1.8), BRANCA, 2, tex=[riscas(3, 'y', -1)], s=1))
    px(P, [(26 + (i % 2), 13 + i + b) for i in range(0, 6, 2)], '#3e3546', 2.1)    # risca preta do pescoço
    cab = elipse(28, 6.5 + b, 3.4, 2.8)
    P.append(parte(cab, BRANCA, 3))
    px(P, [(26, 5 + b), (27, 5 + b), (28, 5 + b), (29, 5 + b)], '#3e3546', 3.1)   # risca preta por cima do olho
    # poupa preta comprida (abana)
    for i, (dx, dy) in enumerate(((-9, -2), (-11, 1))):
        P.append(Parte(capsula(26, 5 + b, 26 + dx, 5 + dy + b + a * 0.6, 0.7 + i * 0.2), PEDRA, z=2.5 + i * 0.01))
    olho(P, 28, 6 + b, '#f9c22b', z=3.2, tam=2, fechado=(t == 3))
    # bico-lança: base amarela, lâmina de aço, fio de brilho que corre
    base = poligono([(30, 5 + b), (35, 6 + b), (35, 8.5 + b), (30, 8.5 + b)])
    P.append(Parte(base, PATA, z=3.3))
    lamina = poligono([(35, 5.8 + b), (47.5, 7.3 + b), (35, 8.6 + b)])
    P.append(Parte(lamina, ACO, z=3.4))
    gx = 36 + t * 3
    px(P, [(gx, 7 + b), (gx + 1, 7 + b)], BRANCO, 3.5)
    px(P, linha(35, 7.4 + b, 46, 7.4 + b), '#7f708a', 3.45)
    # asa dobrada por cima do corpo, com as pontas pretas para trás
    asa = elipse(17, 24.5 + b, 8, 4.4) | capsula(12, 25 + b, 6, 29 + b, 2.2)
    P.append(parte(asa, CINZA, 4, tex=[escamas(4, 2)], s=7, luz=-0.05))
    for i in range(3):
        px(P, linha(9 + i * 2, 27 + b - i, 5 + i * 2, 30 + b - i * 0.5), '#3e3546', 4.1)
    px(P, [(14, 21 + b), (17, 21 + b), (20, 21 + b)], '#c7dcd0', 4.2)
    return desenhar(P, 48, 48)


def driade_corrompida(t):
    """Dríade corrompida: mulher-planta de pele verde com veios roxos, uma flor carnívora no lugar do cabelo,
    saia de raízes e vinhas, olhos roxos a brilhar, chicote de espinhos na mão e esporos roxos no ar."""
    P = []
    b = ONDA[t]
    a = VAI[t]
    PELE = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
    RAIZ = ['#2e222f', '#45293f', '#6b3e75', '#694f62', '#966c6c']
    FLOR = ['#6e2727', '#ae2334', '#e83b3b', '#f68181', '#fdcbb0']
    # saia de raízes/vinhas até ao chão
    for i, (x2, y2) in enumerate(((13, 46), (18, 46), (23, 46), (28, 46), (32, 45))):
        pts = curva([(22, 29 + b), ((22 + x2) / 2 + (2 if i % 2 else -2), 38), (x2, y2)], 6)
        P.append(parte(tubo(pts, 2.4, 1.1), VERDE_ESC, 0.5 + i * 0.01, luz=0.0 if i % 2 else -0.15))
    px(P, [(14, 45), (31, 44), (19, 40), (26, 41)], '#a884f3', 0.6)              # botões roxos
    for (x, y) in ((16, 42), (28, 40), (22, 44)):
        px(P, [(x, y), (x + 1, y - 1)], '#6b3e75', 0.7)                           # veios da corrupção
    # tronco esguio
    tronco = elipse(22, 25 + b, 3.6, 6.2)
    P.append(parte(tronco, PELE, 2, luz=0.05))
    px(P, (linha(20, 21 + b, 22, 30 + b) | linha(24, 22 + b, 23, 27 + b)) & tronco, '#6b3e75', 2.1)
    P.append(Parte(capsula(19, 22 + b, 25, 22 + b, 1.0), VERDE, z=2.2))           # folhas ao peito
    # cabelo-flor carnívora: pétalas atrás da cabeça e uma boca de dentes no alto
    for i, ang in enumerate((200, 235, 270, 160, 305)):
        r = math.radians(ang + a * 4)
        pet = capsula(22, 13 + b, 22 + math.cos(r) * 9.5, 13 + b + math.sin(r) * 8.5, 3.0 if i % 2 == 0 else 2.4)
        P.append(parte(pet, FLOR, 3 + i * 0.01, tex=[pintas(4, 1, +1)], s=i))
    # boca da flor (por cima da cabeça, virada para cima/trás)
    boca_c = recortar(elipse(17, 6 + b, 5.5, 3.6), y_max=int(6 + b))
    boca_b = recortar(elipse(17, 7.5 + b, 5, 2.6), y_min=int(7.5 + b))
    P.append(Parte(elipse(17, 7 + b, 4.5, 1.4), ['#2e222f', '#6e2727', '#831c5d', '#831c5d', '#831c5d'], z=3.4))
    P.append(parte(boca_b, FLOR, 3.5))
    P.append(parte(boca_c, FLOR, 3.6))
    px(P, [(13 + i * 2, 7 + b) for i in range(5)], '#ffffff', 3.7)
    # cabeça (cara de perfil, virada para a direita)
    cab = elipse(24, 14 + b, 3.8, 4.2)
    P.append(parte(cab, PELE, 4, luz=0.1))
    px(P, [(27, 16 + b), (26, 17 + b)], '#165a4c', 4.1)                          # boca
    olho(P, 25, 12 + b, '#a884f3', z=4.2, tam=2)
    px(P, [(24, 11 + b), (25, 10 + b)] if t != 3 else [(24, 11 + b)], '#6b3e75', 4.3)   # sobrancelha / veio
    px(P, [(21, 15 + b), (22, 16 + b)], '#6b3e75', 4.3)
    # braço com o chicote de espinhos
    P.append(parte(capsula(23, 20 + b, 28, 25 + b, 1.3), PELE, 5))
    P.append(parte(capsula(28, 25 + b, 32, 22 + b, 1.1), PELE, 5.1))
    for i, (dx, dy) in enumerate(((2, -2), (2, 1), (1, 2))):
        px(P, linha(32, 22 + b, 32 + dx, 22 + b + dy), '#239063', 5.2)
    chic = curva([(33, 22 + b), (40 + a, 18 + b), (43, 28), (37 - a, 38), (40, 45)], 12)
    P.append(parte(tubo(chic, 1.2, 0.8), VERDE_ESC, 5.3))
    for i, (x, y) in enumerate(chic[1:-1:2]):
        px(P, [(x + 1.5, y - 1)], '#c7dcd0', 5.4)
    # esporos roxos no ar
    for i, (x, y) in enumerate(((8, 20), (36, 9), (11, 32), (40, 34), (30, 4))):
        yy = y - ((t + i) % 4)
        px(P, [(x, yy)], '#a884f3' if (t + i) % 2 else '#eaaded', 6)
    return desenhar(P, 48, 48)


def ninfa_da_cascata(t):
    """Ninfa da cascata: espírito de água; o cabelo é uma cascata que cai até ao chão (riscas a descer),
    vestido que se desfaz em água, olhos brancos a brilhar, flor de lótus no cabelo e uma bola de água na mão."""
    P = []
    b = ONDA[t]
    PELE = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
    CASC = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
    # cascata do cabelo: sai da cabeça para trás e cai a direito até ao chão
    cab_x, cab_y = 25, 9 + b
    cascata = (tubo(curva([(cab_x - 1, cab_y - 3), (14, cab_y - 3), (11, cab_y + 8)], 6), 3.4, 3.8)
               | poligono([(7.5, cab_y + 8), (14.5, cab_y + 6), (16, 44), (6, 44)]))
    P.append(parte(cascata, CASC, 0, volume='cilindro_v'))
    for (x, y) in cascata:              # riscas de espuma a descer
        if y > cab_y + 4 and (y - t * 2 + x * 3) % 7 == 0 and (x + 1, y) in cascata and (x - 1, y) in cascata:
            px(P, [(x, y)], '#8fd3ff' if (x + y) % 2 else '#ffffff', 0.1)
    # salpicos e espuma no chão
    P.append(Parte(elipse(17, 45.5, 13, 2.2), AGUA, z=0.2, plano=True))
    for i, (x, y) in enumerate(((5, 41), (9, 39), (27, 42), (31, 40))):
        yy = y - (t + i) % 3
        px(P, [(x, yy)], '#8ff8e2', 0.3)
    # vestido que se desfaz em água
    vest = poligono([(20, 22 + b), (26, 22 + b), (29, 36), (31, 44), (15, 44), (18, 34)])
    P.append(parte(vest, AGUA, 1, volume='cilindro_v', tex=[riscas(4, 'y', +1, fase=t)], s=2))
    for i, x in enumerate(range(16, 31, 3)):
        px(P, [(x, 44 + (i + t) % 2)], '#8ff8e2', 1.1)
    # tronco e cabeça
    P.append(parte(elipse(23, 19 + b, 3.2, 4.5), PELE, 2))
    P.append(parte(elipse(cab_x, cab_y, 3.8, 4.1), PELE, 3, luz=0.1))
    olho(P, 26, 8 + b, '#ffffff', z=3.2, tam=2, brilho=False)
    px(P, [(27, 9 + b)], '#4d9be6', 3.3)
    px(P, [(27, 12 + b), (28, 12 + b)], '#0b5e65', 3.3)                          # boca
    # franja e lótus
    P.append(parte(capsula(22, 6 + b, 28, 5.5 + b, 1.6), CASC, 3.4))
    P.append(Parte(elipse(21, 5 + b, 2.2, 1.6), ['#753c54', '#cf657f', '#ed8099', '#fdcbb0', '#ffffff'], z=3.5))
    px(P, [(21, 4 + b)], '#f9c22b', 3.6)
    # braço levantado com a bola de água
    P.append(parte(capsula(24, 17 + b, 29, 20 + b, 1.2), PELE, 4))
    P.append(parte(capsula(29, 20 + b, 32, 15 + b, 1.0), PELE, 4.1))
    bola = elipse(33, 11 + b - (t % 2), 3.2, 3.2)
    P.append(Parte(bola, AGUA, z=4.2))
    px(P, [(32, 9 + b - (t % 2)), (33, 9 + b - (t % 2))], '#ffffff', 4.3)
    for i in range(2):
        ang = (t * 90 + i * 180) * math.pi / 180
        px(P, [(33 + math.cos(ang) * 5, 11 + b + math.sin(ang) * 3)], '#8ff8e2', 4.4)
    return desenhar(P, 48, 48)


def pantera_de_jade(t):
    """Pantera de jade: felino verde-escuro, comprido e baixo, com rosetas que brilham (pulsam), olhos de jade,
    orelhas pequenas, bigodes, presas brancas e a cauda comprida a abanar a ponta."""
    P = []
    b = ONDA[t] * 0.6
    a = VAI[t]
    JADE = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']
    LONGE = ['#2e222f', '#2e222f', '#313638', '#374e4a', '#547e64']
    luzm = '#30e1b9' if t % 2 == 0 else '#8ff8e2'
    # patas de longe
    P.append(parte(capsula(13, 36, 15, 45.5, 2.0), LONGE, 0))
    P.append(parte(capsula(34, 35, 36, 45.5, 1.8), LONGE, 0))
    # cauda comprida em curva, a ponta abana
    cauda = curva([(10, 31 + b), (3, 35), (1, 26), (4 + a, 19), (7 + a * 2, 18)], 10)
    P.append(parte(tubo(cauda, 1.9, 1.3), JADE, 1, luz=0.05))
    # corpo comprido
    corpo = elipse(22, 32 + b, 12, 5.8)
    P.append(parte(corpo, JADE, 2, tex=[pelo(6)], s=1, luz=0.1))
    P.append(Parte(recortar(elipse(23, 36 + b, 9, 2.4), y_min=int(36 + b)) & corpo, ['#313638', '#374e4a', '#547e64', '#92a984', '#92a984'], z=2.1, separar=False))
    # rosetas que brilham (anel de jade com o centro escuro)
    for (rx, ry) in ((13, 30), (18, 28.5), (24, 29), (29, 31), (16, 34), (22, 33.5)):
        anel = {(rx + dx, int(ry + b) + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))}
        px(P, anel & corpo, luzm, 2.2)
        px(P, [(rx, int(ry + b))], '#0b5e65', 2.21)
    # cabeça: crânio, focinho, orelha
    P.append(parte(poligono([(34, 25 + b), (35, 20 + b), (38.5, 23.5 + b)]), JADE, 2.9))
    px(P, [(35, 22 + b), (35, 23 + b), (36, 23 + b)], '#0b8a8f', 2.95)
    cab = elipse(38, 27.5 + b, 5.6, 5.0)
    P.append(parte(cab, JADE, 3, luz=0.05, tex=[pelo(6)], s=9))
    focinho = elipse(42.5, 29.8 + b, 3.0, 2.4)
    P.append(parte(focinho, JADE, 3.1, luz=0.1))
    px(P, [(45, 28 + b), (46, 29 + b)], '#2e222f', 3.2)                           # nariz
    px(P, [(41, 32 + b), (42, 32 + b), (43, 32 + b), (44, 31 + b)], OUT, 3.2)       # boca
    px(P, [(43, 33 + b), (44, 32 + b)], '#ffffff', 3.3)                            # presa
    px(P, [(43, 30 + b), (46, 31 + b), (45, 32 + b)], '#92a984', 3.3)               # bigodes
    olho(P, 39, 25.5 + b, '#30e1b9', z=3.4, tam=2, pupila='fenda', fechado=(t == 3))
    px(P, [(38, 24 + b), (39, 24 + b), (40, 24 + b)], '#2e222f', 3.45)            # sobrolho
    px(P, [(35, 28 + b), (37, 30 + b)], luzm, 3.5)                                 # manchas na cara
    # patas de perto
    P.append(parte(elipse(14, 33.5 + b, 4.2, 4.4), JADE, 4, tex=[pelo(6)], s=4, luz=-0.1))
    P.append(parte(capsula(12, 37, 11, 45.5, 2.1), JADE, 4.1))
    P.append(parte(capsula(31, 34 + b, 32, 45.5, 2.1), JADE, 4.2))
    P.append(parte(capsula(11, 46, 14, 46, 1.2), JADE, 4.3))
    P.append(parte(capsula(32, 46, 35, 46, 1.2), JADE, 4.4))
    px(P, [(15, 46), (36, 46)], '#c7dcd0', 4.5)                                    # garras
    px(P, [(13, 36 + b), (31, 38)], luzm, 4.6)
    return desenhar(P, 48, 48)


# ====================================================================== 64×64
def caranguejo_violinista_gigante(t):
    """Caranguejo-violinista gigante: carapaça laranja com pintas, olhos em pedúnculos, UMA pinça enorme
    amarela (que abre e fecha), uma pinça pequena, patas às riscas e bolhas a sair da boca."""
    P = []
    b = ONDA[t]
    a = VAI[t]
    CARAP = ['#6e2727', '#9e4539', '#cd683d', '#fb6b1d', '#f79617']
    PINCA = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
    LONGE = ['#45293f', '#6e2727', '#9e4539', '#cd683d', '#cd683d']
    # patas de longe (atrás)
    for i, (x0, x1, x2) in enumerate(((20, 14, 10), (25, 21, 18), (31, 30, 29), (36, 39, 42))):
        P.append(parte(capsula(x0 + 1, 44 + b, x1 + 1, 50 + b, 1.8) | capsula(x1 + 1, 50 + b, x2 + 2, 61, 1.3), LONGE, 0 + i * 0.01))
    # carapaça
    corpo = elipse(28, 43 + b, 15, 9)
    P.append(parte(corpo, CARAP, 1, tex=[pintas(5, 2, +1), salpicos(9, -1)], s=3, luz=0.05))
    px(P, [(x, 43 + b + (1 if x % 4 < 2 else 0)) for x in range(15, 42)], '#6e2727', 1.1)   # sulco da carapaça
    for x in range(16, 41, 4):                                                                 # serrilha da borda
        px(P, [(x, 51 + b)], '#fbb954', 1.2)
    px(P, [(21, 37 + b), (22, 37 + b), (26, 36 + b)], '#fbb954', 1.3)
    # pedúnculos dos olhos (abanam) e olhos pretos com brilho
    for i, (x0, x1, y1) in enumerate(((34, 33, 27), (38, 39, 28))):
        dx = a if i == 0 else -a
        P.append(parte(capsula(x0, 37 + b, x1 + dx * 0.5, y1 + b, 1.2), CARAP, 2 + i * 0.01))
        P.append(Parte(elipse(x1 + dx * 0.5, y1 - 1.5 + b, 2.2, 2.2), ['#2e222f', '#2e222f', '#3e3546', '#625565', '#625565'], z=2.1 + i * 0.01))
        px(P, [(x1 - 1 + dx * 0.5, y1 - 3 + b)], BRANCO, 2.2 + i * 0.01)
    # boca e bolhas
    px(P, [(42, 45 + b), (43, 46 + b), (42, 47 + b)], '#45293f', 2.5)
    for i in range(3):
        k = (t + i * 2) % 4
        bx, by = 45 + i * 2 - (k // 2), 44 - k * 3 - i * 2 + b
        anel = {(bx - 1, by), (bx + 1, by), (bx, by - 1), (bx, by + 1)}
        px(P, anel, '#8fd3ff' if k < 3 else '#ffffff', 6)
    # patas de perto, às riscas, com pontas claras
    for i, (x0, x1, x2) in enumerate(((19, 12, 7), (24, 19, 15), (30, 30, 28), (35, 40, 41))):
        perna = capsula(x0, 46 + b, x1, 52 + b, 2.1) | capsula(x1, 52 + b, x2, 61.5, 1.5)
        P.append(parte(perna, CARAP, 3 + i * 0.01, tex=[riscas(3, 'y', -1)], s=i))
        px(P, [(x2, 62)], '#fbb954', 3.05 + i * 0.01)
    # pinça pequena
    P.append(parte(capsula(38, 49 + b, 43, 52 + b, 1.4), CARAP, 4))
    P.append(Parte(elipse(45, 52 + b, 2.4, 1.7), PINCA, z=4.1))
    # PINÇA ENORME: braço, "mão" com dedo fixo e dedo que abre/fecha
    ab = [0, 1, 2, 1][t]
    P.append(parte(capsula(37, 45 + b, 44, 41 + b - a * 0.5, 2.8), CARAP, 5, tex=[riscas(3, 'x', -1)], s=5))
    mx, my = 50, 36 + b - a * 0.5
    mao_p = elipse(mx, my, 8, 6.4)
    P.append(parte(mao_p, PINCA, 5.2, tex=[salpicos(6, -1)], s=6, luz=0.1))
    fixo = capsula(mx + 5, my + 3, mx + 13, my + 1, 2.3)
    P.append(parte(fixo, PINCA, 5.1))
    dedo = capsula(mx + 4, my - 3, mx + 13, my - 4 + ab * 1.6, 2.0)
    P.append(parte(dedo, PINCA, 5.3))
    for i in range(3):   # dentinhos da pinça
        px(P, [(mx + 7 + i * 2, my + 1)], '#ffffff', 5.4)
    px(P, [(mx - 4, my - 3), (mx - 3, my - 4), (mx - 1, my - 5)], '#ffffff', 5.4)
    px(P, [(mx - 2, my + 2), (mx + 1, my + 3)], '#f79617', 5.4)
    return desenhar(P, 64, 64)


def grande_bugio(t):
    """Grande Bugio: macaco gigante curvado, pelo castanho com barba, cara vermelha, olhos vermelhos, braços enormes
    apoiados nos nós dos dedos e cauda preênsil enrolada. Num quadro abre a boca a uivar."""
    P = []
    b = ONDA[t]
    a = VAI[t]
    PELO_B = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
    LONGE = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
    CARA_V = ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790']
    uivo = t == 2
    # cauda preênsil enrolada atrás
    pts = curva([(16, 40 + b), (4, 42), (2, 22), (10 + a, 14), (14 + a, 20), (10 + a, 22)], 12)
    P.append(parte(tubo(pts, 2.4, 1.5), PELO_B, 0, luz=0.05))
    # braço de longe
    P.append(parte(capsula(22, 32 + b, 18, 47 + b, 4.0), LONGE, 0.5))
    P.append(parte(capsula(18, 47 + b, 18, 60, 3.4), LONGE, 0.6))
    P.append(parte(elipse(19, 61, 3.6, 2.0), LONGE, 0.7))
    # pernas curtas e grossas
    P.append(parte(elipse(22, 50, 7, 6.5), PELO_B, 1, tex=[pelo(5)], s=1, luz=-0.05))
    P.append(parte(capsula(24, 54, 27, 61, 3.0), PELO_B, 1.1))
    P.append(parte(capsula(25, 62, 32, 62, 1.6), CARA_V, 1.2, luz=-0.3))
    # tronco curvado (costas em arco)
    tronco = elipse(30, 38 + b, 13.5, 13) | elipse(36, 33 + b, 10, 9)
    P.append(parte(tronco, PELO_B, 2, tex=[pelo(4)], s=2))
    P.append(parte(elipse(38, 41 + b, 5.5, 8), ['#45293f', '#694f62', '#966c6c', '#ab947a', '#ab947a'], 2.1, separar=False, luz=-0.2))
    # cabeça baixa e para a frente: cara vermelha, sobrolho, barba
    cab = elipse(44, 24 + b, 7.5, 7)
    P.append(parte(cab, PELO_B, 3, tex=[pelo(4)], s=3))
    barba = poligono([(40, 27 + b), (51, 27 + b), (49, 37 + b + a * 0.5), (45, 39 + b), (41, 35 + b)])
    P.append(parte(barba, PELO_B, 3.1, tex=[pelo(3)], s=4))
    cara = elipse(48, 25 + b, 4.6, 5.2)
    P.append(parte(cara, CARA_V, 3.2, luz=0.05))
    P.append(parte(capsula(44, 21 + b, 52, 21 + b, 1.6), PELO_B, 3.3, volume='cilindro_h'))     # sobrolho
    olho(P, 48, 22 + b, '#e83b3b', z=3.4, tam=2, fechado=(t == 3))
    px(P, [(51, 25 + b), (52, 25 + b)], '#6e2727', 3.5)                                       # narinas
    if uivo:
        P.append(Parte(elipse(50, 29.5 + b, 2.2, 2.6), ['#2e222f', '#2e222f', '#6e2727', '#6e2727', '#6e2727'], z=3.6))
        px(P, [(49, 27 + b), (51, 27 + b)], '#ffffff', 3.7)
        for i in range(3):
            px(P, [(56 + i * 2, 24 + b - i * 2), (56 + i * 2, 30 + b + i)], '#fca790', 6)
    else:
        px(P, [(47, 29 + b), (48, 29 + b), (49, 29 + b), (50, 28 + b)], '#6e2727', 3.6)
    # braço de perto: ombro largo, antebraço e mão nos nós dos dedos
    P.append(parte(capsula(38, 32 + b, 44, 46 + b, 4.6), PELO_B, 4, tex=[pelo(4)], s=5))
    P.append(parte(capsula(44, 46 + b, 45, 58, 3.8), PELO_B, 4.1, tex=[pelo(4)], s=6))
    P.append(parte(elipse(46, 60, 4.2, 2.6), CARA_V, 4.2, luz=-0.3))
    px(P, [(44, 61), (46, 61), (48, 61)], '#6e2727', 4.3)
    px(P, [(37, 34 + b), (39, 33 + b), (41, 35 + b)], '#ab947a', 4.4)
    return desenhar(P, 64, 64)


def lodo_toxico(t):
    """Lodo tóxico: slime gigante verde fluorescente, meio transparente, com uma caveira, costelas e um osso a boiar
    lá dentro, bolhas a subir, olhos grandes, boca a babar e uma poça à volta. Abana (estica e encolhe)."""
    P = []
    sq = [0, 1, 0, -1][t]
    LODO = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
    OSSO_V = ['#547e64', '#92a984', '#b2ba90', '#c7dcd0', '#c7dcd0']
    rx, ry = 23 + sq, 17 - sq
    cy = 61 - ry
    # poça no chão
    P.append(Parte(elipse(32, 61.5, 29, 2.4), ['#165a4c', '#239063', '#1ebc73', '#91db69', '#91db69'], z=0, plano=True))
    corpo = elipse(32, cy, rx, ry) | elipse(30, cy - ry * 0.55, rx * 0.6, ry * 0.6)
    corpo = recortar(corpo, y_max=61)
    # pingos a escorrer pelos lados
    for (x, c) in ((12, 4), (18, 6), (47, 5), (53, 3)):
        corpo |= capsula(x, 56, x, 56 + c + (t % 2), 1.4)
    corpo = recortar(corpo, y_max=61)
    P.append(parte(corpo, LODO, 1, luz=0.05))
    # o "dentro" mais claro (parece transparente)
    dentro = elipse(31, cy + 2, rx - 6, ry - 5)
    P.append(Parte(dentro & corpo, ['#239063', '#1ebc73', '#1ebc73', '#91db69', '#91db69'], z=1.1, separar=False, plano=True))
    # ossos a boiar lá dentro
    oy = cy + 3 + [0, 1, 1, 0][t]
    caveira = elipse(23, oy, 4.2, 3.6) | retangulo(21, int(oy) + 2, 25, int(oy) + 4)
    P.append(Parte(caveira, OSSO_V, z=1.2))
    px(P, [(22, oy), (23, oy), (25, oy)], '#165a4c', 1.3)
    px(P, [(22, oy + 3), (24, oy + 3)], '#165a4c', 1.3)
    for i in range(3):
        P.append(Parte(capsula(32 + i * 3, oy - 2 + i, 34 + i * 3, oy + 5 + i, 0.8), OSSO_V, z=1.2 + i * 0.01))
    osso = capsula(30, oy + 9, 42, oy + 6, 0.9) | elipse(30, oy + 9, 1.6, 1.6) | elipse(42, oy + 6, 1.6, 1.6)
    P.append(Parte(osso, OSSO_V, z=1.25))
    # bolhas a subir
    for i, (bx, by0) in enumerate(((17, 54), (40, 52), (28, 50), (45, 44))):
        by = by0 - ((t + i) % 4) * 3
        if (bx, int(by)) in corpo:
            px(P, [(bx, by), (bx + 1, by - 1)], '#cddf6c', 1.4)
    # brilho do lado da luz
    px(P, [(14, cy - 3), (15, cy - 5), (16, cy - 7), (18, cy - 9), (20, cy - 12)], '#fbff86', 1.5)
    # olhos grandes e boca a babar
    for ex in (35, 44):
        mao(P, {(ex + i, int(cy - 6) + j): '#2e222f' for i in range(3) for j in range(4)}, 2, separar=False)
        px(P, [(ex, cy - 6)], BRANCO, 2.1)
    boca = [(x, int(cy + 1 + (1 if x in (37, 44) else 0))) for x in range(36, 46)] + [(38, int(cy + 2)), (42, int(cy + 2)), (40, int(cy + 3))]
    px(P, boca, '#165a4c', 2)
    px(P, [(41, cy + 3 + t % 2), (41, cy + 4 + t % 2)], '#d5e04b', 2.1)
    return desenhar(P, 64, 64)


def totem_vivo_de_sssar(t):
    """Totem vivo de Sssar: três cabeças esculpidas em madeira (crocodilo em baixo, serpente pintada de verde
    ao meio, ave pintada de vermelho em cima com penas), olhos a brilhar verde, entalhes, musgo e espíritos verdes."""
    P = []
    pul = '#d5e04b' if t % 2 else '#91db69'
    MAD = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
    VERD = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
    VERM = ['#6e2727', '#9e4539', '#b33831', '#ea4f36', '#f57d4a']
    gir = [VAI[t], VAI[(t + 1) % 4], VAI[(t + 2) % 4]]   # cada cabeça "roda" um bocadinho
    # raízes da base
    for (x1, x2) in ((22, 15), (28, 26), (40, 47), (36, 38)):
        P.append(parte(capsula(x1, 56, x2, 61.5, 1.8), MAD, 0))
    # bloco de baixo: cabeça de crocodilo
    g = gir[0]
    P.append(parte(retangulo(20, 44, 42, 61, canto=1), MAD, 1, volume='cilindro_v', tex=[riscas(4, 'y', -1)], s=1))
    P.append(parte(retangulo(40, 47, 49 + g, 52, canto=1), MAD, 1.1))
    px(P, [(x, 50) for x in range(40, 49 + g)], OUT, 1.2)
    px(P, [(41 + i * 2 + g, 51) for i in range(4)], '#c7dcd0', 1.3)
    px(P, [(42 + i * 2 + g, 49) for i in range(3)], '#c7dcd0', 1.3)
    mao(P, {(36 + g + i, 46 + j): pul for i in range(3) for j in range(2)}, 1.4)
    px(P, [(x, 57) for x in range(21, 42) if x % 3 == 0], '#f9c22b', 1.4)            # entalhe pintado
    px(P, [(x, 58) for x in range(21, 42) if x % 3 == 1], '#f9c22b', 1.4)
    # bloco do meio: serpente pintada de verde
    g = gir[1]
    P.append(parte(retangulo(21, 28, 41, 44, canto=1), VERD, 2, volume='cilindro_v', tex=[escamas(4, 3)], s=2))
    P.append(parte(poligono([(40, 31), (51 + g, 35), (51 + g, 38), (40, 41)]), VERD, 2.1))
    px(P, [(x, 37) for x in range(41, 51 + g)], OUT, 2.2)
    px(P, [(44 + g, 38), (48 + g, 38)], '#ffffff', 2.3)
    if t == 1:
        px(P, [(52 + g, 37), (53 + g, 37), (54 + g, 36), (54 + g, 38)], '#e83b3b', 2.3)
    mao(P, {(35 + g + i, 32 + j): pul for i in range(3) for j in range(2)}, 2.4)
    px(P, [(23, 31), (24, 32), (25, 31), (26, 32), (27, 31)], '#f9c22b', 2.4)        # zigue-zague
    # bloco de cima: ave pintada de vermelho, bico curvo, penas no alto
    g = gir[2]
    for i, (fx, fy, c) in enumerate(((24, 4, '#4d9be6'), (29, 2, '#f9c22b'), (34, 3, '#1ebc73'), (38, 6, '#4d9be6'))):
        rampa = {'#4d9be6': AZUL, '#f9c22b': OURO, '#1ebc73': VERDE}[c]
        P.append(parte(capsula(31, 14, fx + (VAI[t] if i % 2 else 0), fy, 1.7), rampa, 2.9 + i * 0.01))
    P.append(parte(retangulo(22, 12, 40, 28, canto=1), VERM, 3, volume='cilindro_v', tex=[pintas(5, 2, -1)], s=3))
    bico = poligono([(39, 15), (47 + g, 17), (49 + g, 21), (46 + g, 24), (45 + g, 21), (39, 23)])
    P.append(parte(bico, OURO, 3.1))
    mao(P, {(34 + g + i, 16 + j): pul for i in range(3) for j in range(3)}, 3.2)
    px(P, [(34 + g, 16)], BRANCO, 3.3)
    px(P, [(x, 26) for x in range(23, 40) if x % 2 == 0], '#f9c22b', 3.3)
    # rachas e musgo
    px(P, linha(27, 46, 25, 53), '#2e222f', 4)
    px(P, linha(31, 13, 29, 20), '#6e2727', 4)
    musgo = {(x, y) for x in range(20, 30) for y in range(54, 62) if _h(x, y, 3) % 3 == 0}
    P.append(Parte(musgo, ['#374e4a', '#547e64', '#92a984', '#92a984', '#92a984'], z=4.1, separar=False))
    # espíritos verdes à volta
    for i, (sx, sy) in enumerate(((12, 30), (54, 10), (10, 14), (55, 46))):
        yy = sy - (t + i) % 4
        px(P, [(sx, yy), (sx + 1, yy), (sx, yy + 1)], '#91db69', 5)
        px(P, [(sx + 1, yy + 1 + (t % 2))], '#d5e04b', 5)
    return desenhar(P, 64, 64)


def serpente_do_lodo(t):
    """Serpente do Lodo: serpente gigante verde-acastanhada a sair da água, coberta de lodo e algas, placas da
    barriga claras, olhos amarelos de fenda, coroa de pedra antiga com uma pedra verde e língua bífida."""
    P = []
    a = VAI[t]
    b = ONDA[t]
    COBRA = ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#fbff86']
    COBRA2 = ['#2e222f', '#4c3e24', '#676633', '#a2a947', '#d5e04b']
    # água
    P.append(Parte(retangulo(0, 58, 63, 63), AGUA, z=0, plano=True))
    for x in range(0, 64):
        if (x + t * 3) % 9 < 2:
            px(P, [(x, 58)], '#8ff8e2', 0.1)
        if (x * 3 + t * 2) % 13 == 0:
            px(P, [(x, 61)], '#30e1b9', 0.1)
    # bossa do corpo de trás (a cauda a sair e a entrar na água)
    volta = curva([(30, 61), (34, 46), (50, 45), (56, 61)], 9)
    P.append(parte(recortar(tubo(volta, 4.6, 3.4), y_max=58), COBRA2, 1, tex=[escamas(4, 3)], s=1))
    px(P, [(56 + (t % 2), 57), (58, 56 - t % 2), (59, 55)], '#4c3e24', 1.1)
    # pescoço que sobe em arco até à cabeça
    hx, hy = 45 + a, 17 + b
    pesc = curva([(16, 61), (12, 36), (30, 18), (hx - 7, hy + 3)], 14)
    corpo = recortar(tubo(pesc, 7.0, 4.6), y_max=58)
    P.append(parte(corpo, COBRA, 2, tex=[escamas(4, 3), pintas(6, 3, -1)], s=2, luz=0.05))
    # placas da barriga (do lado de baixo/dentro da curva)
    for i, (x, y) in enumerate(pesc[1:-1]):
        nx, ny = 30 - x, 40 - y
        n = math.hypot(nx, ny) or 1
        r = 6.2 - 2.2 * i / 12
        qx, qy = x + nx / n * (r - 1.5), y + ny / n * (r - 1.5)
        if qy < 57:
            px(P, [(qx, qy), (qx + 1, qy)], '#b2ba90' if i % 2 else '#92a984', 2.1)
    # lodo a escorrer e algas penduradas
    for i, (x, y) in enumerate(pesc[3:12:2]):
        px(P, [(x - 2, y), (x - 2, y + 1), (x - 1, y + 2), (x - 2, y + 3 + (t + i) % 2)], '#4c3e24', 2.2)
    for i, (x, y) in enumerate(pesc[5:12:3]):
        alga = capsula(x, y, x - 1 + (a if i % 2 else -a), y + 6, 0.8)
        P.append(Parte(alga, ['#165a4c', '#239063', '#1ebc73', '#91db69', '#91db69'], z=2.3 + i * 0.01))
    # cabeça em losango, focinho, mandíbula
    cab = elipse(hx, hy, 8.5, 6) | capsula(hx, hy + 1, hx + 11, hy + 2, 3.4)
    P.append(parte(cab, COBRA, 3, tex=[escamas(3, 2)], s=3, luz=0.15))
    P.append(parte(capsula(hx - 2, hy + 4.5, hx + 9, hy + 5, 2.0), COBRA2, 2.9))
    px(P, [(x, int(hy + 3.6)) for x in range(hx - 3, hx + 12)], OUT, 3.1)
    px(P, [(hx + 9, int(hy + 4.6)), (hx + 5, int(hy + 4.6))], '#ffffff', 3.2)          # presas
    px(P, [(hx + 11, int(hy))], OUT, 3.2)                                                # narina
    P.append(parte(capsula(hx - 3, hy - 3.5, hx + 6, hy - 2.5, 1.6), COBRA, 3.3, volume='cilindro_h'))   # sobrolho
    olho(P, hx + 2, hy - 2, '#f9c22b', z=3.4, tam=3, pupila='redonda')
    if t in (1, 2):
        px(P, [(hx + 13, hy + 4), (hx + 14, hy + 4), (hx + 15, hy + 3), (hx + 15, hy + 5)] + ([(hx + 16, hy + 2), (hx + 16, hy + 6)] if t == 2 else []), '#e83b3b', 3.5)
    # coroa de pedra antiga com pedra verde
    coroa = (retangulo(hx - 6, int(hy - 7), hx + 3, int(hy - 5))
             | poligono([(hx - 6.5, hy - 6), (hx - 5, hy - 11), (hx - 3.5, hy - 6)])
             | poligono([(hx - 3, hy - 6), (hx - 1.5, hy - 12), (hx, hy - 6)])
             | poligono([(hx + 0.5, hy - 6), (hx + 2, hy - 10), (hx + 3.5, hy - 6)]))
    P.append(parte(coroa, PEDRA, 3.6, tex=[salpicos(5, -1)], s=4))
    P.append(Parte(elipse(hx - 1.5, hy - 6, 1.3, 1.1), VERDE, z=3.7))
    px(P, [(hx - 2, int(hy - 7))], BRANCO, 3.8)
    px(P, [(hx + 2, int(hy - 6)), (hx - 5, int(hy - 5))], '#547e64', 3.8)               # musgo na coroa
    # bolhas à volta do corpo na água
    for i, x in enumerate((24, 33, 12)):
        px(P, [(x + (t + i) % 3, 56)], '#8ff8e2', 4)
    return desenhar(P, 64, 64)


def jaguar_de_pedra_solar(t):
    """Jaguar de Pedra Solar: estátua de jaguar em pedra dourada, rosetas entalhadas, rachas, colar de pedras
    turquesa, disco do sol na testa (brilha) e olhos de rubi. Faíscas de luz à volta."""
    P = []
    b = ONDA[t] * 0.6
    a = VAI[t]
    PED = ['#9e4539', '#cd683d', '#f79617', '#f9c22b', '#fbff86']
    LONGE = ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#f79617']
    # patas de longe
    P.append(parte(capsula(15, 48, 16, 61.5, 2.6), LONGE, 0))
    P.append(parte(capsula(44, 47, 46, 61.5, 2.4), LONGE, 0))
    # cauda em pedra (curva para cima, a ponta abana)
    cauda = curva([(12, 41 + b), (4, 46), (2, 34), (6 + a, 27), (9 + a * 2, 27)], 10)
    P.append(parte(tubo(cauda, 2.4, 1.6), PED, 1, tex=[riscas(3, 'y', -1)], s=1))
    # corpo
    corpo = elipse(29, 43 + b, 16, 7.6)
    P.append(parte(corpo, PED, 2, tex=[salpicos(7, -1)], s=2))
    # rosetas entalhadas
    for (rx, ry) in ((17, 40), (23, 38), (30, 38.5), (37, 40), (20, 46), (27, 45), (34, 46)):
        anel = {(rx + dx, int(ry + b) + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1))}
        px(P, anel & corpo, '#9e4539', 2.2)
        px(P, [(rx, int(ry + b))], '#cd683d', 2.21)
    # rachas
    px(P, linha(22, 37 + b, 25, 43 + b) | linha(25, 43 + b, 24, 47 + b), '#6e2727', 2.3)
    # cabeça
    P.append(parte(poligono([(44, 32 + b), (45.5, 26 + b), (49, 31 + b)]), PED, 2.9))
    px(P, [(45, 29 + b), (46, 30 + b)], '#9e4539', 2.95)
    cab = elipse(50, 35 + b, 7, 6.4)
    P.append(parte(cab, PED, 3, tex=[salpicos(7, -1)], s=3, luz=0.05))
    P.append(parte(elipse(56, 37.5 + b, 4, 3.2), PED, 3.1, luz=0.1))
    px(P, [(59, 35 + b), (60, 36 + b)], '#6e2727', 3.2)
    px(P, [(53, 40 + b), (54, 40 + b), (55, 40 + b), (56, 40 + b), (57, 39 + b)], '#6e2727', 3.2)
    px(P, [(56, 41 + b), (54, 41 + b)], '#ffffff', 3.3)
    mao(P, {(51, int(33 + b)): '#e83b3b', (52, int(33 + b)): '#e83b3b', (51, int(34 + b)): '#ae2334', (52, int(34 + b)): '#6e2727'}, 3.4)
    px(P, [(51, 33 + b)], '#fca790', 3.5)
    # disco do sol na testa (com raios que brilham)
    sx, sy = 47, 30 + b
    P.append(Parte(elipse(sx, sy, 2.2, 2.2), OURO, z=3.6))
    if t % 2 == 0:
        px(P, [(sx - 3, sy), (sx + 2, sy), (sx, sy - 3), (sx, sy + 2)], '#fbff86', 3.7)
    else:
        px(P, [(sx - 3, sy - 3), (sx + 2, sy - 3), (sx - 3, sy + 2), (sx + 2, sy + 2)], '#ffffff', 3.7)
    # colar de pedras turquesa
    for i, (cx, cy) in enumerate(((43, 39), (44, 42), (45, 45), (47, 47))):
        P.append(Parte(elipse(cx, cy + b, 1.4, 1.3), AGUA, z=3.8 + i * 0.01))
    # patas de perto
    P.append(parte(elipse(17, 46 + b, 5.5, 5.5), PED, 4, luz=-0.1))
    P.append(parte(capsula(16, 49, 15, 61.5, 2.9), PED, 4.1, tex=[riscas(4, 'y', -1)], s=5))
    P.append(parte(capsula(41, 46 + b, 42, 61.5, 2.9), PED, 4.2, tex=[riscas(4, 'y', -1)], s=6))
    P.append(parte(capsula(14, 62, 19, 62, 1.6), PED, 4.3))
    P.append(parte(capsula(41, 62, 46, 62, 1.6), PED, 4.4))
    px(P, [(20, 62), (47, 62)], '#ffffff', 4.5)
    # faíscas de luz
    for i, (x, y) in enumerate(((8, 18), (30, 24), (58, 22), (24, 30))):
        if (t + i) % 2 == 0:
            px(P, [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], '#fbff86', 5)
            px(P, [(x, y)], BRANCO, 5.1)
    return desenhar(P, 64, 64)


# ====================================================================== 128×128
def hidra_do_pantano(t):
    """Hidra do Pântano: corpo enorme de lagarto do pântano coberto de musgo, cauda grossa, quatro patas com garras,
    espinhos nas costas e TRÊS cabeças de serpente (verde, roxa, amarela) com chifres, olhos e dentes;
    cada pescoço abana com o seu ritmo e as línguas saem à vez. Pés dentro da água rasa do lago ritual."""
    P = []
    b = ONDA[t]
    CORPO = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']
    LONGE = ['#2e222f', '#313638', '#374e4a', '#547e64', '#547e64']
    AMAR = ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff']
    VERDE_H = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
    ROXO_H = ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded']
    tex_c = [escamas(5, 4), pintas(7, 4, -1)]
    # patas de longe
    P.append(parte(capsula(36, 98, 32, 118, 6), LONGE, 0))
    P.append(parte(capsula(80, 96, 84, 118, 6), LONGE, 0))
    # cauda grossa
    cauda = tubo(curva([(30, 92 + b), (12, 100), (4, 112), (0, 116)], 8), 12, 3)
    P.append(parte(cauda, CORPO, 1, tex=tex_c, s=1))
    # corpo
    corpo = elipse(55, 90 + b, 32, 20)
    P.append(parte(corpo, CORPO, 2, tex=tex_c, s=2, luz=0.08))
    barriga = recortar(elipse(56, 100 + b, 28, 9), y_min=int(102 + b))
    P.append(parte(barriga & corpo, BARRIGA, 2.1, separar=False, tex=[riscas(4, 'x', -1)], s=1))
    # musgo nas costas
    musgo = {q for q in recortar(corpo, y_max=int(80 + b)) if _h(q[0] // 2, q[1] // 2, 8) % 3 == 0}
    P.append(Parte(musgo, ['#4c3e24', '#676633', '#a2a947', '#d5e04b', '#d5e04b'], z=2.2, separar=False))
    # espinhos nas costas e na cauda
    for i, x in enumerate(range(14, 80, 6)):
        if x < 26:
            yb = 92 + b - 11 + (26 - x) * 0.6
        else:
            yb = 90 + b - 20 * math.sqrt(max(0.0, 1 - ((x - 55) / 32) ** 2))
        P.append(Parte(poligono([(x - 2.4, yb + 2), (x - 0.5, yb - 5), (x + 2.4, yb + 2)]), VERDE_H, z=1.8 + i * 0.001))
    # três pescoços com cabeças; cada um abana com o seu ritmo
    cabecas = (('roxa', ROXO_H, (66, 78), (56, 50), (74, 22), (t + 0) % 4, '#f9c22b'),
               ('verde', VERDE_H, (74, 80), (92, 60), (100, 42), (t + 1) % 4, '#e83b3b'),
               ('amarela', AMAR, (80, 86), (100, 92), (108, 70), (t + 2) % 4, '#a884f3'))
    for j, (nome, R, base, meio, cab, fase, cor_olho) in enumerate(cabecas):
        dx = VAI[fase] * 1.5
        dy = ONDA[fase]
        hx, hy = cab[0] + dx, cab[1] + dy + b
        pesc = curva([(base[0], base[1] + b), (meio[0] + dx * 0.5, meio[1] + b), (hx - 8, hy + 4)], 10)
        z = 3 + j
        P.append(parte(tubo(pesc, 7, 4.8), R, z, tex=[escamas(4, 3)], s=10 + j))
        for i, (x, y) in enumerate(pesc[1:-1]):     # placas claras do pescoço (do lado da frente)
            px(P, [(x + 4, y), (x + 4, y + 1), (x + 5, y)], R[3], z + 0.05)
        # cabeça de serpente com chifres
        P.append(Parte(capsula(hx - 6, hy - 4, hx - 13, hy - 10, 1.4), CREME, z=z + 0.1))
        P.append(Parte(capsula(hx - 3, hy - 5, hx - 7, hy - 12, 1.2), CREME, z=z + 0.11))
        crane = elipse(hx, hy, 9, 6) | capsula(hx, hy + 1, hx + 12, hy + 2.5, 3.6)
        P.append(parte(crane, R, z + 0.2, tex=[escamas(3, 2)], s=20 + j, luz=0.12))
        P.append(parte(capsula(hx - 3, hy + 5, hx + 10, hy + 6, 2.4), R, z + 0.15, luz=-0.2))
        px(P, [(x, int(hy + 4)) for x in range(int(hx - 5), int(hx + 14))], OUT, z + 0.3)
        px(P, [(hx + i, hy + 5) for i in range(-2, 12, 3)], '#ffffff', z + 0.31)
        px(P, [(hx + 1 + i, hy + 3) for i in range(-2, 12, 3)], '#ffffff', z + 0.31)
        px(P, [(hx + 13, hy)], OUT, z + 0.31)
        P.append(parte(capsula(hx - 4, hy - 3.5, hx + 5, hy - 3, 1.8), R, z + 0.32, volume='cilindro_h'))
        olho(P, hx + 1, hy - 2, cor_olho, z=z + 0.4, tam=3, pupila='redonda')
        if (t + j) % 3 == 0:   # língua bífida
            px(P, [(hx + 14 + i, hy + 4) for i in range(4)] + [(hx + 18, hy + 3), (hx + 18, hy + 5)], '#e83b3b', z + 0.5)
    # patas de perto com garras
    for (x0, y0, x1) in ((34, 98, 36), (76, 98, 78)):
        P.append(parte(elipse(x0, y0 + b, 9, 8), CORPO, 7, tex=tex_c, s=x0))
        P.append(parte(capsula(x0 + 1, y0 + 4, x1, 117, 6), CORPO, 7.1, tex=tex_c, s=x0 + 1))
        P.append(parte(elipse(x1 + 3, 119, 8, 3.6), CORPO, 7.2))
        px(P, [(x1 + 9, 120), (x1 + 6, 121), (x1 + 3, 121)], '#c7dcd0', 7.3)
    # água rasa do lago ritual por cima dos pés
    agua = retangulo(0, 121, 127, 127)
    P.append(Parte(agua, AGUA, z=8, plano=True))
    for x in range(128):
        if (x + t * 4) % 11 < 3:
            px(P, [(x, 121)], '#8ff8e2', 8.1)
        if (x * 7 + t * 3) % 17 == 0:
            px(P, [(x, 124)], '#30e1b9', 8.1)
    return desenhar(P, 128, 128)


# ====================================================================== lista, gravar e comparar
CRIATURAS = [
    # (id, pasta da arte antiga, função)
    ('sapo_venenoso', 'monstros', sapo_venenoso),
    ('homem_lagarto_renegado', 'monstros', homem_lagarto_renegado),
    ('mosquito_gigante', 'monstros', mosquito_gigante),
    ('macaco_ladrao', 'monstros', macaco_ladrao),
    ('sanguessuga_gigante', 'monstros', sanguessuga_gigante),
    ('bruxa_do_pantano', 'monstros', bruxa_do_pantano),
    ('rei_macaco_bobo', 'monstros', rei_macaco_bobo),
    ('flor_carnivora', 'monstros', flor_carnivora),
    ('crocodilo', 'monstros', crocodilo),
    ('mae_crocodilo_mandibula', 'monstros', mae_crocodilo_mandibula),
    ('garca_lanca', 'guardioes', garca_lanca),
    ('pantera_de_jade', 'guardioes', pantera_de_jade),
    ('ninfa_da_cascata', 'guardioes', ninfa_da_cascata),
    ('driade_corrompida', 'guardioes', driade_corrompida),
    ('lodo_toxico', 'guardioes', lodo_toxico),
    ('totem_vivo_de_sssar', 'guardioes', totem_vivo_de_sssar),
    ('caranguejo_violinista_gigante', 'guardioes', caranguejo_violinista_gigante),
    ('grande_bugio', 'guardioes', grande_bugio),
    ('serpente_do_lodo', 'bosses', serpente_do_lodo),
    ('jaguar_de_pedra_solar', 'bosses', jaguar_de_pedra_solar),
    ('hidra_do_pantano', 'bosses', hidra_do_pantano),
]

PALETA = set(c for r in RAMPAS.values() for c in r) | {
    '#ae2334', '#e83b3b', '#fb6b1d', '#831c5d', '#0b5e65', '#4c3e24', '#313638'}


def _nomes():
    import json
    nomes = {}
    for f in ('monstros.json', 'bosses.json', 'masmorras.json'):
        try:
            d = json.load(open(os.path.join(RAIZ, 'dados', f), encoding='utf-8'))
        except (OSError, ValueError):
            continue
        pilha = [d]
        while pilha:                      # procura em todos os níveis (masmorras.json tem bosses lá dentro)
            e = pilha.pop()
            if isinstance(e, dict):
                if isinstance(e.get('id'), str) and e.get('nome_pt'):
                    nomes.setdefault(e['id'], e['nome_pt'])
                pilha.extend(e.values())
            elif isinstance(e, list):
                pilha.extend(e)
    return nomes


def _verificar(img, nome):
    cores = [c for _, c in img.getcolors(1 << 16)]
    usadas = {'#%02x%02x%02x' % c[:3] for c in cores if c[3]}
    fora = usadas - PALETA
    if fora:
        print('  AVISO: cores fora da paleta em', nome, sorted(fora))
    if any(c[3] not in (0, 255) for c in cores):
        print('  AVISO: transparência parcial em', nome)


def _grelha(celulas, titulo, caminho, ntiques=8, ms=160):
    """celulas: lista de (nome, [listas de quadros por coluna], escala). Monta um GIF em grelha (largura máx. 1200)."""
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
    ftit = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    FUNDO = (0x26, 0x2b, 0x3a)
    M = 10
    caixas = []
    for nome, colunas, k in celulas:
        lado = colunas[0][0].width * k
        w = len(colunas) * lado + (len(colunas) - 1) * 6
        w = max(w, int(fonte.getlength(nome)) + 4)
        caixas.append((nome, colunas, k, lado, w, lado + 18))
    # distribuir em linhas
    linhas, atual, larg = [], [], M
    for c in caixas:
        if atual and larg + c[4] + M > 1200:
            linhas.append(atual)
            atual, larg = [], M
        atual.append(c)
        larg += c[4] + M
    if atual:
        linhas.append(atual)
    W = max(M + sum(c[4] + M for c in l) for l in linhas)
    W = max(W, int(ftit.getlength(titulo)) + 2 * M)
    H = 34 + sum(max(c[5] for c in l) + M for l in linhas)
    quadros = []
    for q in range(ntiques):
        im = Image.new('RGB', (W, H), FUNDO)
        d = ImageDraw.Draw(im)
        d.text((M, 8), titulo, font=ftit, fill=(255, 255, 255))
        y = 34
        for l in linhas:
            x = M
            alt = max(c[5] for c in l)
            for nome, colunas, k, lado, w, h in l:
                ox = x + (w - (len(colunas) * lado + (len(colunas) - 1) * 6)) // 2
                for j, fr in enumerate(colunas):
                    f = fr[q % len(fr)]
                    f = f.resize((f.width * k, f.height * k), Image.NEAREST)
                    im.paste(f, (ox + j * (lado + 6), y + (alt - 18 - lado)), f)
                tw = fonte.getlength(nome)
                d.text((x + (w - tw) / 2, y + alt - 15), nome, font=fonte, fill=(199, 220, 208))
                x += w + M
            y += alt + M
        quadros.append(im)
    quadros[0].save(caminho, save_all=True, append_images=quadros[1:], duration=ms, loop=0, disposal=1)


def main():
    os.makedirs(SAIDA, exist_ok=True)
    nomes = _nomes()
    comp, dep = [], []
    for cid, pasta, f in CRIATURAS:
        quadros = [f(t) for t in range(4)]
        tira = Image.new('RGBA', (quadros[0].width * 4, quadros[0].height), (0, 0, 0, 0))
        for i, q in enumerate(quadros):
            tira.paste(q, (i * q.width, 0))
            _verificar(q, cid)
        tira.save(os.path.join(SAIDA, f'{cid}_parado_lado.png'))
        antiga = Image.open(os.path.join(ANTIGA, pasta, f'{cid}_parado_lado.png')).convert('RGBA')
        h = antiga.height
        assert h == quadros[0].height, (cid, h, quadros[0].height)
        velhos = [antiga.crop((i * h, 0, i * h + h, h)) for i in range(antiga.width // h)]
        k = {32: 3, 48: 2, 64: 2}.get(h, 1)
        nome = nomes.get(cid, cid)
        comp.append((nome, [velhos, quadros], k))
        dep.append((nome, [quadros], k))
        print('ok', cid, h)
    _grelha(comp, 'Região 3 — Pântano e Selva — antes | depois', os.path.join(SAIDA, 'comparar.gif'))
    _grelha(dep, 'Região 3 — Pântano e Selva — depois (proposta)', os.path.join(SAIDA, 'depois.gif'))
    print('gravado em', SAIDA)


if __name__ == '__main__':
    main()
