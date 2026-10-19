"""Monstros da Região 1 (Floresta): os 8 normais e os 2 com nome.
Fichas: docs/regioes/r01_floresta.md, secções 3 e 4. Saída: arte/regioes/r01_floresta/monstros/.

Uso (a partir da raiz do repositório):  python3 ferramentas/arte/monstros_r01.py [previa.gif]
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import (Parte, elipse, retangulo, capsula, poligono, desenhar, previa_gif,
                   deitar, dissolver, deslocar, estrelas, guardar)

PASTA = os.path.join('arte', 'regioes', 'r01_floresta', 'monstros')
OLHO = '#2e222f'
BRANCO = '#ffffff'


def olhos(P, pts, z=30, branco=True):
    for x, y in pts:
        x, y = int(x), int(y)
        P.append(Parte({(x, y), (x, y + 1)}, None, z=z, separar=False, cor=OLHO))
        if branco:
            P.append(Parte({(x - 1, y)}, None, z=z, separar=False, cor=BRANCO))


def olhos_x(P, pts, z=30):
    for x, y in pts:
        x, y = int(x), int(y)
        P.append(Parte({(x - 1, y - 1), (x + 1, y - 1), (x, y), (x - 1, y + 1), (x + 1, y + 1)}, None, z=z, separar=False, cor=OLHO))


def morte(frames_base, ultima):
    """dano -> cair -> deitado -> desfazer-se."""
    return [frames_base, deitar(ultima), dissolver(deitar(ultima), 0.45), dissolver(deitar(ultima), 0.8)]


# =============== Slime Verde (32) e Slime Rei (64) ===============

def slime(rx, ry, dx=0, dy=0, cara='normal', W=32, k=1.0, coroa=False, peixe=False, rampa='verde', partido=0):
    P = []
    base = W - 2
    cx = W / 2 + dx * k
    rx, ry = rx * k, ry * k
    cy = base - ry + dy * k
    if partido:
        for s in (-1, 1):
            P.append(Parte(elipse(cx + s * (rx * 0.55 + partido * k), cy + ry * 0.2, rx * 0.55, ry * 0.8), rampa, z=1))
    else:
        P.append(Parte(elipse(cx, cy, rx, ry), rampa, z=1))
    if peixe and not partido:
        fx, fy = cx - rx * 0.2, cy + ry * 0.25
        corpo = elipse(fx, fy, 3 * k / 2.2 * 2.2, 1.6 * k / 2.2 * 2.2)
        cauda = poligono([(fx - 3.2 * k, fy), (fx - 5 * k, fy - 2 * k), (fx - 5 * k, fy + 2 * k)])
        P.append(Parte(corpo | cauda, 'laranja', z=2, separar=False))
    ex = [cx + rx * 0.15, cx + rx * 0.55]
    ey = cy - ry * 0.2
    if partido:
        pass
    elif cara == 'x':
        olhos_x(P, [(x, ey) for x in ex])
    elif cara == 'fechado':
        for x in ex:
            P.append(Parte({(int(x), int(ey) + 1), (int(x) + 1, int(ey) + 1)}, None, z=30, separar=False, cor=OLHO))
    elif k > 1.5:
        for x in ex:
            x, y = int(x), int(ey)
            P.append(Parte(retangulo(x, y, x + 1, y + 3), None, z=30, separar=False, cor=OLHO))
            P.append(Parte({(x, y)}, None, z=31, separar=False, cor=BRANCO))
    else:
        olhos(P, [(x, ey) for x in ex])
    if coroa and not partido:
        top = cy - ry
        P.append(Parte(poligono([(cx - 9, top + 3), (cx - 9, top - 6), (cx - 5, top - 2), (cx, top - 9), (cx + 5, top - 2),
                                 (cx + 9, top - 6), (cx + 9, top + 3)]), 'ouro', z=5))
        P.append(Parte({(int(cx), int(top - 4)), (int(cx) - 6, int(top - 2)), (int(cx) + 6, int(top - 2))}, None, z=6, separar=False, cor='#e83b3b'))
    return desenhar(P, W, W)


def anims_slime():
    A = {}
    A['parado'] = [slime(9, 7), slime(9.3, 6.7), slime(9.6, 6.4), slime(9.3, 6.7)]
    A['mover'] = [slime(10.5, 5.5), slime(8, 8.5, dy=-2), slime(8.5, 8, dx=1, dy=-3), slime(9.5, 6.5, dx=1)]
    A['atacar'] = [slime(10.5, 5.2, cara='fechado'), slime(8, 9, dx=1, dy=-5), slime(8.5, 8, dx=4, dy=-6), slime(10.5, 5.5, dx=5)]
    A['dano'] = [slime(10.5, 5.8, dx=-1, cara='x')]
    A['morrer'] = [slime(10.5, 6, cara='x'), slime(12, 4.5, cara='x'), dissolver(slime(13.5, 3.2, cara='x'), 0.3),
                   dissolver(slime(14.5, 2.2, cara='x'), 0.7)]
    return A


def slime_rei(**kw):
    return slime(W=64, k=2.3, coroa=True, peixe=True, **kw)


def anims_slime_rei():
    A = {}
    A['parado'] = [slime_rei(rx=9, ry=7), slime_rei(rx=9.3, ry=6.7), slime_rei(rx=9.6, ry=6.4), slime_rei(rx=9.3, ry=6.7)]
    A['mover'] = [slime_rei(rx=10.5, ry=5.5), slime_rei(rx=8, ry=8.5, dy=-1), slime_rei(rx=8.5, ry=8, dx=1, dy=-1.5), slime_rei(rx=9.5, ry=6.5, dx=1)]
    A['atacar'] = [slime_rei(rx=10.5, ry=5.2, cara='fechado'), slime_rei(rx=8, ry=9, dy=-2), slime_rei(rx=8.5, ry=8, dx=2, dy=-2.5), slime_rei(rx=11, ry=5, dx=3)]
    A['dano'] = [slime_rei(rx=10.5, ry=5.8, dx=-1, cara='x')]
    A['morrer'] = [slime_rei(rx=10.5, ry=6, cara='x'), slime_rei(rx=12, ry=4.5, cara='x'),
                   dissolver(slime_rei(rx=13.5, ry=3.2, cara='x'), 0.3), dissolver(slime_rei(rx=14, ry=2.4, cara='x'), 0.7)]
    # ataque_1: salto alto que cai com uma onda de choque
    onda = []
    for r in (6, 11, 16):
        P = []
        P.append(Parte({p for p in elipse(32, 61, 20 + r, 3) if p not in elipse(32, 61, 17 + r, 2)}, 'verde', z=0, plano=True))
        onda.append(P)
    base = slime_rei(rx=11.5, ry=4.8)
    ondas = [desenhar(o, 64, 64) for o in onda]
    A['ataque_1'] = [slime_rei(rx=11, ry=5, cara='fechado'), slime_rei(rx=7.5, ry=9.5, dy=-2.5), slime_rei(rx=8, ry=9, dy=-3.5),
                     _sobrepor(base, ondas[0]), _sobrepor(base, ondas[1]), _sobrepor(slime_rei(rx=10, ry=6.2), ondas[2])]
    # ataque_2: dividir-se em 4 (abre ao meio)
    A['ataque_2'] = [slime_rei(rx=10, ry=6.5, cara='fechado'), slime_rei(rx=11.5, ry=6, cara='x'),
                     slime_rei(rx=9, ry=7, partido=1), slime_rei(rx=9, ry=7, partido=3)]
    # ataque_3: rolar contra o herói (estica para a frente)
    A['ataque_3'] = [slime_rei(rx=9, ry=7.5, dx=-1), slime_rei(rx=11.5, ry=6, dx=2), slime_rei(rx=12.5, ry=5.5, dx=4), slime_rei(rx=9.5, ry=7, dx=4)]
    return A


def _sobrepor(a, b):
    out = a.copy()
    out.paste(b, (0, 0), b)
    return out


# =============== Coelho-Chifre (32) ===============

def coelho(dx=0, dy=0, orelha=0, cab=(0, 0), cara='normal', pernas='parado', esticado=0):
    P = []
    hx, hy = 21 + dx + cab[0], 19 + dy + cab[1]
    P.append(Parte(elipse(14 + dx - esticado * .5, 24 + dy, 6 + esticado, 4.5 - esticado * .3), 'castanho', z=2))
    P.append(Parte(elipse(8.5 + dx - esticado, 22 + dy, 1.8, 1.8), 'branco', z=1))
    if pernas == 'salto':
        P.append(Parte(capsula(10 + dx, 26 + dy, 6 + dx, 27 + dy, 1.5), 'castanho', z=3))
        P.append(Parte(capsula(18 + dx, 26 + dy, 21 + dx, 27 + dy, 1.2), 'castanho', z=3))
    else:
        P.append(Parte(capsula(11 + dx, 26 + dy, 10 + dx, 28.5 + dy, 1.6), 'castanho', z=3))
        P.append(Parte(capsula(18 + dx, 26 + dy, 19 + dx, 28.5 + dy, 1.2), 'castanho', z=3))
    P.append(Parte(capsula(hx - 3, hy - 3, hx - 5 + orelha, hy - 10, 1.2), 'castanho', z=1.5))
    P.append(Parte(capsula(hx - 1, hy - 3, hx - 1 + orelha * 1.5, hy - 10.5, 1.2), 'castanho', z=4))
    P.append(Parte(elipse(hx, hy, 4, 3.5), 'castanho', z=5))
    P.append(Parte(poligono([(hx + 1, hy - 2.5), (hx + 3, hy - 2.8), (hx + 2.5, hy - 8.5)]), 'branco', z=6))
    P.append(Parte({(int(hx + 4), int(hy + 1))}, None, z=30, separar=False, cor='#f68181'))
    if cara == 'x':
        olhos_x(P, [(hx + 1, hy)])
    else:
        olhos(P, [(hx + 1.5, hy - 1)], branco=False)
    return desenhar(P, 32, 32)


def anims_coelho():
    A = {}
    A['parado'] = [coelho(orelha=0), coelho(orelha=1), coelho(orelha=0, dy=0), coelho(orelha=-1)]
    A['mover'] = [coelho(), coelho(dy=-2, pernas='salto', orelha=-1), coelho(dx=1, dy=-3, pernas='salto', orelha=-2), coelho(dx=1, dy=-1, orelha=-1)]
    A['atacar'] = [coelho(cab=(1, 3), orelha=-2), coelho(cab=(1, 3), dx=-1, orelha=-2), coelho(dx=4, cab=(2, 2), esticado=2, pernas='salto', orelha=-3),
                   coelho(dx=2, orelha=-1)]
    A['dano'] = [coelho(dx=-1, cara='x', orelha=2)]
    A['morrer'] = morte(coelho(dx=-1, cara='x', orelha=2), coelho(cara='x'))
    return A


# =============== Lobo Cinzento (32) e Lobo Cicatriz (48) ===============

def lobo(dx=0, dy=0, a=0, t=0, cabeca='normal', W=32, k=1.0, rampa='cinza', cicatriz=False, olho='#f9c22b', baixo=0):
    P = []

    def S(x, y):
        return (x + dx - 2.5) * k, (y + dy) * k

    longe = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#7f708a'] if rampa == 'cinza' else ['#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565']
    # pernas de longe
    for (x1, y1, x2, y2) in ((10, 22, 9 + a, 28), (19, 22, 20 - a, 28)):
        p1, p2 = S(x1, y1 + baixo), S(x2, y2)
        P.append(Parte(capsula(*p1, *p2, 1.3 * k), longe, z=0, volume='cilindro_v'))
    # cauda
    p1, p2 = S(9, 18 + baixo), S(4, 15 + t)
    P.append(Parte(capsula(*p1, *p2, 1.6 * k), rampa, z=1))
    # corpo
    p1, p2 = S(10, 20 + baixo), S(19, 19.5 + baixo)
    P.append(Parte(capsula(*p1, *p2, 4.0 * k), rampa, z=2))
    # pernas de perto
    for (x1, y1, x2, y2) in ((12, 22, 12 - a, 28), (21, 22, 21 + a, 28)):
        p1, p2 = S(x1, y1 + baixo), S(x2, y2)
        P.append(Parte(capsula(*p1, *p2, 1.4 * k), rampa, z=3, volume='cilindro_v'))
    # cabeça
    if cabeca == 'uivar':
        hx, hy, fx, fy = 23, 12, 24.5, 7.5
    elif cabeca == 'baixa':
        hx, hy, fx, fy = 24, 19, 28, 21
    elif cabeca == 'morde':
        hx, hy, fx, fy = 26, 16, 30, 17
    else:
        hx, hy, fx, fy = 24, 15.5 + baixo * .5, 28, 17 + baixo * .5
    n1, n2 = S(19, 18 + baixo), S(hx - 1, hy + 0.5)
    P.append(Parte(capsula(*n1, *n2, 2.8 * k), rampa, z=3.5))
    P.append(Parte(poligono([S(hx - 2, hy - 2), S(hx - 1, hy - 6.5), S(hx + 1, hy - 2.5)]), rampa, z=4))
    P.append(Parte(poligono([S(hx + 0.5, hy - 2.5), S(hx + 2, hy - 6.5), S(hx + 2.8, hy - 1.5)]), rampa, z=6))
    P.append(Parte(elipse(*S(hx, hy), 4 * k, 3.5 * k), rampa, z=5))
    P.append(Parte(elipse(*S(fx, fy), 2.6 * k, 1.8 * k), rampa, z=6))
    nx, ny = S(fx + 2.2, fy - 0.8)
    P.append(Parte({(int(nx), int(ny))}, None, z=30, separar=False, cor=OLHO))
    if cabeca == 'morde':
        jx, jy = S(fx, fy + 2.3)
        P.append(Parte(capsula(jx - 2 * k, jy, jx + 2 * k, jy + 1 * k, 0.9 * k), rampa, z=6.5))
        P.append(Parte({(int(nx - 1), int(ny + 2 * k)), (int(nx - 3), int(ny + 2 * k))}, None, z=31, separar=False, cor=BRANCO))
    ex, ey = S(hx + 1.2, hy - 1)
    if cabeca == 'x':
        olhos_x(P, [(ex, ey)])
    else:
        P.append(Parte({(int(ex), int(ey)), (int(ex) + 1, int(ey))}, None, z=30, separar=False, cor=olho))
    if cicatriz:
        P.append(Parte({(int(ex) - 1, int(ey) - 2), (int(ex), int(ey) - 1), (int(ex) + 2, int(ey) + 1), (int(ex) + 3, int(ey) + 2)},
                       None, z=31, separar=False, cor='#c7dcd0'))
    return desenhar(P, W, W)


def anims_lobo(**kw):
    A = {}
    A['parado'] = [lobo(t=0, **kw), lobo(t=1, **kw), lobo(t=1, baixo=1, **kw), lobo(t=0, **kw)]
    A['mover'] = [lobo(a=2, t=1, **kw), lobo(a=1, dy=-1, t=0, **kw), lobo(a=0, dy=-1, t=-1, **kw),
                  lobo(a=-2, t=1, **kw), lobo(a=-1, dy=-1, t=0, **kw), lobo(a=0, t=-1, **kw)]
    A['atacar'] = [lobo(cabeca='baixa', baixo=2, a=1, **kw), lobo(cabeca='baixa', baixo=2, dx=-1, a=1, **kw),
                   lobo(cabeca='morde', dx=3, dy=-1, a=3, t=-2, **kw), lobo(cabeca='morde', dx=3, a=2, **kw)]
    A['uivar'] = [lobo(cabeca='normal', **kw), lobo(cabeca='uivar', baixo=1, **kw), lobo(cabeca='uivar', baixo=1, t=2, **kw), lobo(**kw)]
    A['dano'] = [lobo(dx=-1, cabeca='x', t=2, **kw)]
    A['morrer'] = morte(lobo(dx=-1, cabeca='x', t=2, **kw), lobo(cabeca='x', **kw))
    return A


def anims_cicatriz():
    kw = dict(W=48, k=1.5, rampa='preto', cicatriz=True, olho='#e83b3b')
    A = anims_lobo(**kw)
    A['ataque_1'] = [lobo(cabeca='baixa', baixo=2, **kw), lobo(cabeca='morde', dx=2, a=3, **kw), lobo(cabeca='baixa', baixo=1, **kw),
                     lobo(cabeca='morde', dx=2, a=-3, **kw), lobo(cabeca='baixa', baixo=1, **kw), lobo(cabeca='morde', dx=2, a=3, **kw)]
    A['ataque_2'] = A['uivar']
    A['ataque_3'] = A['atacar']
    return A


# =============== Javali (48) ===============

COURO_JAVALI = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']


def javali(dx=0, dy=0, a=0, cab=0, cara='normal', est=None):
    P = []
    for (x1, x2) in ((15, 15 + a), (31, 31 - a)):
        P.append(Parte(capsula(x1 + dx, 36 + dy, x2 + dx, 44, 2.2), ['#2e222f', '#2e222f', '#4c3e24', '#694f62', '#694f62'], z=0, volume='cilindro_v'))
    P.append(Parte(capsula(8 + dx, 27 + dy, 5 + dx, 25 + dy, 1.0), COURO_JAVALI, z=1))
    P.append(Parte(elipse(21 + dx, 32 + dy, 14, 10), COURO_JAVALI, z=2))
    juba = [(9, 25), (11, 19), (14, 23), (17, 18), (19, 22.5), (22, 17.5), (24, 22.5), (27, 18.5), (29, 23.5), (31, 21), (31, 27), (9, 27)]
    P.append(Parte(poligono([(x + dx, y + dy) for x, y in juba]), ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c'], z=3))
    for (x1, x2) in ((18, 18 - a), (34, 34 + a)):
        P.append(Parte(capsula(x1 + dx, 37 + dy, x2 + dx, 44, 2.4), COURO_JAVALI, z=4, volume='cilindro_v'))
    hx, hy = 36 + dx, 32 + dy + cab
    P.append(Parte(poligono([(hx - 3, hy - 4), (hx - 2, hy - 9), (hx + 1, hy - 5)]), COURO_JAVALI, z=5))
    P.append(Parte(elipse(hx, hy, 7, 6.5), COURO_JAVALI, z=6))
    P.append(Parte(elipse(hx + 6.5, hy + 2.5, 3, 2.6), 'lilas', z=7))
    P.append(Parte({(int(hx + 8), int(hy + 2)), (int(hx + 8), int(hy + 3))}, None, z=30, separar=False, cor=OLHO))
    P.append(Parte(capsula(hx + 4, hy + 5, hx + 6.5, hy + 1.5, 0.9), 'branco', z=8))
    if cara == 'x':
        olhos_x(P, [(hx + 2, hy - 2)])
    else:
        P.append(Parte({(int(hx + 2), int(hy - 2)), (int(hx + 3), int(hy - 2))}, None, z=30, separar=False, cor='#e83b3b' if cara == 'furia' else OLHO))
    if est is not None:
        estrelas(P, hx, hy - 10, est)
    return desenhar(P, 48, 48)


def anims_javali():
    A = {}
    A['parado'] = [javali(), javali(dy=0, cab=1), javali(dy=1, cab=1), javali(cab=0)]
    A['mover'] = [javali(a=2), javali(a=1, dy=-1), javali(a=-2), javali(a=-1, dy=-1)]
    A['carga'] = [javali(cab=3, a=3, cara='furia'), javali(cab=3, a=-3, dy=-1, cara='furia'), javali(cab=3, a=3, cara='furia'), javali(cab=3, a=-3, dy=-1, cara='furia')]
    A['cabecada'] = [javali(cab=2, dx=-1), javali(cab=-3, dx=2, dy=-1), javali(cab=-4, dx=3, dy=-1), javali(cab=0)]
    A['atordoado'] = [javali(cab=2, cara='x', est=0), javali(cab=2, cara='x', est=1)]
    A['dano'] = [javali(dx=-1, cara='x')]
    A['morrer'] = morte(javali(dx=-1, cara='x'), javali(cara='x'))
    return A


# =============== Cogumelo Andante (32) ===============

def cogumelo(dy=0, cara='normal', pes=True, inchar=0, dx=0, a=0, braco=0, esporos=0):
    P = []
    cx = 16 + dx
    if pes:
        P.append(Parte(capsula(cx - 3 + a, 28, cx - 3 + a, 29.5, 1.4), 'branco', z=0))
        P.append(Parte(capsula(cx + 3 - a, 28, cx + 3 - a, 29.5, 1.4), 'branco', z=0))
    P.append(Parte(elipse(cx, 23 + dy, 5, 5.5), 'branco', z=1))
    if braco:
        P.append(Parte(capsula(cx + 3, 23 + dy, cx + 3 + braco, 21 + dy, 1.2), 'branco', z=2))
    chapeu = {p for p in elipse(cx, 16 + dy, 10 + inchar, 6.5 + inchar * .5) if p[1] <= 18 + dy}
    P.append(Parte(chapeu, 'vermelho', z=3))
    for (sx, sy, r) in ((-5, -3, 1.6), (1, -4.5, 1.3), (5, -1, 1.5), (-1, 0, 1.0)):
        P.append(Parte(elipse(cx + sx * (1 + inchar * .08), 15 + dy + sy, r, r), 'branco', z=4, separar=False, brilho=False))
    if cara == 'normal':
        olhos(P, [(cx + 0, 22 + dy), (cx + 3, 22 + dy)])
    elif cara == 'fechado':
        P.append(Parte({(int(cx), int(23 + dy)), (int(cx + 3), int(23 + dy))}, None, z=30, separar=False, cor=OLHO))
    elif cara == 'x':
        olhos_x(P, [(cx, 22 + dy), (cx + 3, 22 + dy)])
    if esporos:
        import random
        rnd = random.Random(esporos)
        pts = {(int(16 + rnd.uniform(-1, 1) * (6 + esporos * 3)), int(20 + rnd.uniform(-1, 1) * (4 + esporos * 2))) for _ in range(6 + esporos * 4)}
        P.append(Parte(pts, 'musgo', z=40, plano=True, separar=False))
    return desenhar(P, 32, 32)


def anims_cogumelo():
    A = {}
    A['disfarce'] = [cogumelo(dy=3, cara=None, pes=False)]
    A['acordar'] = [cogumelo(dy=3, cara=None, pes=False), cogumelo(dy=2, cara='fechado', pes=False),
                    cogumelo(dy=1, cara='fechado'), cogumelo(dy=-1, cara='normal')]
    A['parado'] = [cogumelo(), cogumelo(dy=0.5), cogumelo(dy=1), cogumelo(dy=0.5)]
    A['mover'] = [cogumelo(a=1), cogumelo(a=0, dy=-1, dx=1), cogumelo(a=-1, dx=1), cogumelo(a=0, dy=-1)]
    A['atacar'] = [cogumelo(braco=-2, dx=-1), cogumelo(braco=4, dx=1), cogumelo(braco=5, dx=2), cogumelo()]
    A['esporos'] = [cogumelo(inchar=1, cara='fechado'), cogumelo(inchar=2, cara='fechado'), cogumelo(inchar=0, esporos=1), cogumelo(esporos=2)]
    A['dano'] = [cogumelo(cara='x', dx=-1)]
    A['morrer'] = morte(cogumelo(cara='x', dx=-1), cogumelo(cara='x'))
    return A


# =============== Fada Travessa (32) ===============

def fada(dy=0, asa=0, dx=0, braco=0, brilho=0, so_brilho=False, cara='normal', escala=1.0):
    P = []
    import random
    rnd = random.Random(brilho)
    pts = {(int(16 + dx + rnd.uniform(-8, 8)), int(15 + dy + rnd.uniform(-8, 8))) for _ in range(7 if not so_brilho else 12)}
    P.append(Parte(pts, None, z=0, separar=False, cor='#fbff86'))
    if so_brilho:
        return desenhar(P, 32, 32, contorno_fora=False)
    cx, cy = 16 + dx, 15 + dy
    asa_ry = 4.5 if asa == 0 else 2
    P.append(Parte(elipse(cx - 4, cy - 2, 3.5, asa_ry), 'agua', z=1, plano=True))
    P.append(Parte(elipse(cx - 2, cy - 3, 3, asa_ry - 0.5), 'agua', z=6, plano=True))
    P.append(Parte(poligono([(cx - 2.5, cy + 1), (cx + 2.5, cy + 1), (cx + 3.5, cy + 7), (cx - 3.5, cy + 7)]), 'verde', z=3))
    P.append(Parte(capsula(cx + 1.5, cy + 2, cx + 3 + braco, cy + 3 - braco * .5, 0.8), 'pele', z=4))
    P.append(Parte(elipse(cx, cy - 1.5, 2.8, 2.6), 'pele', z=5, luz=0.3))
    P.append(Parte({p for p in elipse(cx - 0.5, cy - 2.8, 3.3, 2.2) if p[1] <= cy - 2} | {(int(cx - 3), int(cy - 1)), (int(cx - 3), int(cy))}, 'musgo', z=6))
    if cara == 'x':
        olhos_x(P, [(cx + 1, cy - 1)])
    else:
        P.append(Parte({(int(cx + 1), int(cy - 1))}, None, z=30, separar=False, cor=OLHO))
    if braco > 2:
        P.append(Parte(elipse(cx + 6, cy + 1, 1.5, 1.5), 'amarelo', z=20))
    return desenhar(P, 32, 32)


def anims_fada():
    A = {}
    A['parado'] = [fada(asa=0, brilho=1), fada(asa=1, dy=-1, brilho=2), fada(asa=0, dy=-1, brilho=3), fada(asa=1, brilho=4)]
    A['mover'] = [fada(asa=0, dx=0, brilho=5), fada(asa=1, dx=1, dy=-1, brilho=6), fada(asa=0, dx=2, brilho=7), fada(asa=1, dx=1, dy=1, brilho=8)]
    A['atacar'] = [fada(asa=0, braco=-1, brilho=9), fada(asa=1, braco=1, brilho=10), fada(asa=0, braco=4, brilho=11), fada(asa=1, brilho=12)]
    A['roubar'] = [fada(asa=1, dy=-2, brilho=13), fada(asa=0, dx=4, dy=4, braco=2, brilho=14), fada(asa=1, dx=2, dy=1, brilho=15), fada(asa=0, dx=-2, dy=-3, brilho=16)]
    A['teletransporte'] = [fada(asa=0, brilho=17), dissolver(fada(asa=1, brilho=18), 0.5), fada(so_brilho=True, brilho=19), fada(so_brilho=True, brilho=20)]
    A['dano'] = [fada(cara='x', dx=-1, asa=1, brilho=21)]
    A['morrer'] = [fada(cara='x', asa=1, brilho=22), fada(cara='x', dy=5, asa=1, brilho=23),
                   dissolver(fada(cara='x', dy=9, asa=1, brilho=24), 0.4), dissolver(fada(cara='x', dy=12, asa=1, brilho=25), 0.8)]
    return A


# =============== Abelha-Gigante (32) ===============

def abelha(dy=0, asa=0, dx=0, ferrao=0, cara='normal', rot=0):
    P = []
    cx, cy = 14 + dx, 18 + dy
    P.append(Parte(elipse(cx + 1, cy - 6, 4, 3 if asa == 0 else 1.5), 'branco', z=0, plano=True))
    P.append(Parte(poligono([(cx - 5, cy - 1 + ferrao * .5), (cx - 9, cy + 1 + ferrao), (cx - 5, cy + 2 + ferrao * .5)]), 'preto', z=1))
    corpo = elipse(cx, cy, 6.5, 4.6)
    P.append(Parte(corpo, 'amarelo', z=2))
    for sx in (-3, -2, 1, 2):
        P.append(Parte({p for p in corpo if p[0] == int(cx + sx)}, 'preto', z=3, separar=False, plano=True))
    for lx in (-2, 1, 4):
        P.append(Parte(capsula(cx + lx, cy + 4, cx + lx - 1, cy + 6.5, 0.6), 'preto', z=1.5))
    P.append(Parte(elipse(cx + 7.5, cy - 0.5, 3.4, 3.2), 'preto', z=4))
    P.append(Parte(capsula(cx + 8, cy - 3, cx + 10, cy - 6, 0.5), 'preto', z=4.5))
    P.append(Parte(elipse(cx + 2, cy - 5.5, 3.5, 2.6 if asa == 0 else 1.2), 'branco', z=6, plano=True))
    if cara == 'x':
        olhos_x(P, [(cx + 9, cy - 1)])
    else:
        P.append(Parte({(int(cx + 9), int(cy - 1)), (int(cx + 9), int(cy))}, None, z=30, separar=False, cor='#e83b3b' if cara == 'furia' else BRANCO))
    return desenhar(P, 32, 32)


def anims_abelha():
    A = {}
    A['parado'] = [abelha(asa=0), abelha(asa=1, dy=-1)]
    A['mover'] = [abelha(asa=0), abelha(asa=1, dx=1, dy=-1), abelha(asa=0, dx=2), abelha(asa=1, dx=1, dy=1)]
    A['atacar'] = [abelha(asa=0, dx=-1, ferrao=-1, cara='furia'), abelha(asa=1, dx=-2, ferrao=2, cara='furia'),
                   abelha(asa=0, dx=3, ferrao=3, cara='furia'), abelha(asa=1, dx=1, cara='furia')]
    A['dano'] = [abelha(asa=1, dx=-1, cara='x')]
    A['morrer'] = morte(abelha(asa=1, cara='x'), abelha(asa=1, cara='x'))
    return A


# =============== Treant Jovem (48) ===============

def treant(cara='normal', braco_p=(37, 20), braco_l=(12, 20), dy=0, a=0, abanar=0, bolotas=0, raizes=0):
    P = []
    MAD = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
    P.append(Parte(capsula(20, 38 + dy, 17 - a, 45, 2.2), MAD, z=0))
    P.append(Parte(capsula(19, 27 + dy, *braco_l, 1.8), MAD, z=1))
    P.append(Parte(elipse(braco_l[0] - 1, braco_l[1] - 2, 3.5, 3), 'verde_esc', z=1.5))
    P.append(Parte(retangulo(17, 20 + dy, 30, 40 + dy, canto=1), MAD, z=2, volume='cilindro_v'))
    P.append(Parte(capsula(28, 38 + dy, 31 + a, 45, 2.2), MAD, z=3))
    copa = elipse(24 + abanar, 13 + dy, 13, 9) | elipse(16 + abanar, 16 + dy, 6, 5) | elipse(32 + abanar, 16 + dy, 6, 5)
    P.append(Parte(copa, 'verde_esc', z=4))
    P.append(Parte({(18 + abanar, 10 + dy), (24 + abanar, 8 + dy), (29 + abanar, 12 + dy), (21 + abanar, 14 + dy)}, None, z=5, separar=False, cor='#91db69'))
    if cara != 'disfarce':
        cor = '#d5e04b' if cara != 'x' else OLHO
        for ex in (24, 28):
            if cara == 'x':
                olhos_x(P, [(ex, 27 + dy)])
            else:
                P.append(Parte(retangulo(ex, 25 + dy, ex + 1, 27 + dy), None, z=30, separar=False, cor=cor))
        P.append(Parte(retangulo(25, 32 + dy, 27, 33 + dy), None, z=30, separar=False, cor=OLHO))
    P.append(Parte(capsula(29, 27 + dy, *braco_p, 2.0), MAD, z=6))
    P.append(Parte(elipse(braco_p[0] + 1, braco_p[1] - 2, 3.5, 3), 'verde_esc', z=6.5))
    for i in range(bolotas):
        bx, by = 32 + i * 5, 14 + (i % 2) * 4
        P.append(Parte(elipse(bx, by, 1.6, 1.8), 'castanho', z=20))
    for i in range(raizes):
        P.append(Parte(capsula(36 + i * 4, 46, 37 + i * 4, 43, 1.0), MAD, z=20))
    return desenhar(P, 48, 48)


def anims_treant():
    A = {}
    dis = dict(cara='disfarce', braco_p=(36, 10), braco_l=(12, 10))
    A['disfarce'] = [treant(**dis)]
    A['acordar'] = [treant(**dis), treant(cara='disfarce', braco_p=(37, 14), braco_l=(11, 14), abanar=1),
                    treant(cara='normal', braco_p=(37, 17), braco_l=(12, 17), abanar=-1), treant(cara='normal', braco_p=(37, 19), braco_l=(12, 19)),
                    treant(dy=-1), treant()]
    A['parado'] = [treant(), treant(abanar=1), treant(dy=1), treant(abanar=-1)]
    A['mover'] = [treant(a=2), treant(a=1, dy=-1), treant(a=-2), treant(a=-1, dy=-1)]
    A['galhada'] = [treant(braco_p=(33, 10)), treant(braco_p=(34, 8), dy=-1), treant(braco_p=(43, 30)), treant(braco_p=(44, 36), dy=1), treant()]
    A['raizes'] = [treant(braco_p=(36, 30)), treant(braco_p=(35, 40), dy=1), treant(braco_p=(35, 41), dy=1, raizes=1), treant(braco_p=(35, 41), dy=1, raizes=3)]
    A['bolotas'] = [treant(abanar=2), treant(abanar=-2), treant(abanar=2, bolotas=1), treant(abanar=0, bolotas=3)]
    A['dano'] = [treant(cara='x', abanar=-2)]
    A['morrer'] = [treant(cara='x', abanar=-2), treant(cara='x', dy=2, braco_p=(38, 30), braco_l=(11, 30)),
                   dissolver(treant(cara='x', dy=4, braco_p=(38, 34), braco_l=(11, 34)), 0.25),
                   dissolver(treant(cara='x', dy=5, braco_p=(38, 36), braco_l=(11, 36)), 0.5),
                   dissolver(treant(cara='x', dy=6, braco_p=(38, 37), braco_l=(11, 37)), 0.75),
                   dissolver(treant(cara='x', dy=6, braco_p=(38, 37), braco_l=(11, 37)), 0.92)]
    return A


TODOS = {
    'slime_verde': anims_slime,
    'coelho_chifre': anims_coelho,
    'lobo_cinzento': anims_lobo,
    'javali': anims_javali,
    'cogumelo_andante': anims_cogumelo,
    'fada_travessa': anims_fada,
    'abelha_gigante': anims_abelha,
    'treant_jovem': anims_treant,
    'slime_rei': anims_slime_rei,
    'lobo_cicatriz': anims_cicatriz,
}


if __name__ == '__main__':
    tudo = {}
    for nome, f in TODOS.items():
        A = f()
        guardar(PASTA, nome, A)
        tudo[nome] = A
        print('ok', nome, ', '.join(f'{k}({len(v)})' for k, v in A.items()))
    if len(sys.argv) > 1:
        for nome, A in tudo.items():
            previa_gif([list(A.values())], sys.argv[1].replace('.gif', f'_{nome}.gif'), escala=4 if A['parado'][0].width <= 32 else 3, ms=150)
