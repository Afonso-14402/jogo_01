"""Objetos pequenos dos andares em pixel art (16 px = 1 m), para os mapas não ficarem vazios:
- detalhes da natureza: troncos caídos, tocos, cogumelos, erva alta, cristais, ossos, conchas...
- objetos feitos por gente: cercas, placas, barris, caixotes, carroças, pilares partidos, menires, tendas...
- cenários: pequenos grupos destes objetos que contam uma história (acampamento abandonado, ruína, círculo de
  cogumelos...). O andar espalha-os pelos prados (scripts/mundo/andar.gd, _decorar).

Chamado por natureza.py (que grava os PNG e o dados/natureza.json).
"""
import math
import random

from PIL import Image

import motor as M
from motor import Parte, elipse, capsula, poligono, retangulo, desenhar, hexrgb
import natureza as N

R = M.RAMPAS
R.update({
    'tecido_verm': ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fca790'],
    'tecido_azul': ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
    'tecido_bege': ['#694f62', '#966c6c', '#ab947a', '#c7dcd0', '#ffffff'],
    'osso':        ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'abobora':     ['#9e4539', '#cd683d', '#fb6b1d', '#f79617', '#fbb954'],
    'cristal_r':   ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
    'cristal_v':   ['#165a4c', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'],
    'cristal_a':   ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff'],
    'cristal_f':   ['#6e2727', '#b33831', '#ea4f36', '#f79617', '#fbff86'],
    'barro':       ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'],
})


def ret(x1, y1, x2, y2):
    return retangulo(int(round(x1)), int(round(y1)), int(round(x2)), int(round(y2)))


def _img(P, w, h):
    return desenhar(P, w, h)


# ---------------------------------------------------------------- natureza ----------------------------------------------------------------

def tronco_caido(rnd, w=48, h=18, casca='tronco', cobertura=None):
    """Tronco deitado: cilindro com o corte visível (anéis) numa ponta e musgo/neve por cima."""
    P = []
    y = h - 8
    P.append(Parte(capsula(6, y, w - 9, y, 5.5), casca, z=1, volume='cilindro_h'))
    P.append(Parte(elipse(w - 8, y, 4, 5.5), 'madeira', z=2))
    P.append(Parte({(w - 8, y), (w - 9, y), (w - 8, y - 1)}, None, z=3, cor='#694f62', separar=False))
    P.append(Parte(capsula(18, y - 4, 22, y - 9, 1.3), casca, z=0, volume='cilindro_v'))   # um galho partido
    if cobertura:
        m = {(x, yy) for (x, yy) in capsula(6, y, w - 9, y, 5.5) if yy <= y - 4 and (x * 5) % 7 < 5}
        P.append(Parte(m, cobertura, z=4, separar=False))
    return _img(P, w, h)


def toco(rnd, w=20, h=16, casca='tronco', cogumelos=None):
    P = []
    base = h - 2
    P.append(Parte(poligono([(3, base), (5, base - 8), (w - 6, base - 8), (w - 4, base)]), casca, z=1, volume='cilindro_v'))
    P.append(Parte(elipse(w / 2 - 0.5, base - 8, w / 2 - 4.5, 2.5), 'madeira', z=2, plano=True))
    P.append(Parte(poligono([(1, base + 1), (4, base - 3), (6, base + 1)]), casca, z=3, volume='cilindro_v'))
    if cogumelos:
        P.append(Parte(elipse(w - 5, base - 3, 2.5, 1.6), cogumelos, z=5))
        P.append(Parte({(w - 5, base - 1), (w - 5, base)}, 'branco', z=4, plano=True, separar=False))
    return _img(P, w, h)


def cogumelos(rnd, w=20, h=16, chapeu='vermelho', pintas=True):
    P = []
    for k, (dx, alt, r) in enumerate([(-4, 6, 3.5), (3, 9, 4.5), (6, 4, 2.5), (-1, 3, 2.2)]):
        x = w / 2 + dx
        P.append(Parte(capsula(x, h - 2, x, h - 2 - alt, 1.0), 'branco', z=k * 3, volume='cilindro_v'))
        P.append(Parte(elipse(x, h - 2 - alt, r, r * 0.65), chapeu, z=k * 3 + 1))
    img = _img(P, w, h)
    if pintas:
        px = img.load()
        for _ in range(7):
            x, y = rnd.randrange(w), rnd.randrange(h // 2)
            if px[x, y][3] and px[x, y][:3] in [hexrgb(c) for c in R[chapeu][1:4]]:
                px[x, y] = hexrgb('#ffffff') + (255,)
    return img


def erva_alta(rnd, rampa='folha', w=22, h=24):
    return N.tufo(rnd, w, h, rampa, 13)


def cristais(rnd, rampa, w=20, h=24):
    P = []
    for k, (dx, alt, larg, inc) in enumerate([(-4, 14, 3.5, -0.25), (4, 11, 3, 0.3), (0, 20, 4.5, 0.0), (7, 6, 2.5, 0.5)]):
        x0 = w / 2 + dx
        topo = (x0 + inc * alt, h - 2 - alt)
        pts = [(x0 - larg, h - 2), (x0 - larg + inc * alt * 0.8, h - 2 - alt * 0.8), topo,
               (x0 + larg + inc * alt * 0.8, h - 2 - alt * 0.8), (x0 + larg, h - 2)]
        P.append(Parte(poligono(pts), rampa, z=k, plano=True))
    return _img(P, w, h)


def ossos(rnd, w=22, h=12):
    P = [Parte(elipse(6, h - 6, 4.5, 3.8), 'osso', z=2),   # caveira de bicho
         Parte(capsula(9, h - 4, 18, h - 3, 1.3), 'osso', z=1, volume='cilindro_h'),
         Parte(elipse(18, h - 3, 2, 1.6), 'osso', z=1),
         Parte(capsula(12, h - 7, 19, h - 8, 1.0), 'osso', z=0, volume='cilindro_h')]
    img = _img(P, w, h)
    px = img.load()
    for x, y in ((4, h - 7), (7, h - 7)):
        px[x, y] = hexrgb('#2e222f') + (255,)
    return img


def concha(rnd, w=10, h=8, rampa='rosa'):
    P = [Parte(elipse(w / 2, h - 3, 3.5, 2.5), rampa, z=1)]
    img = _img(P, w, h)
    px = img.load()
    for x in range(2, w - 2, 2):
        for y in range(1, h - 1):
            if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                px[x, y] = hexrgb(R[rampa][1]) + (255,)
    return img


def estrela_mar(rnd, w=12, h=10):
    m = set()
    for k in range(5):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        m |= capsula(w / 2, h / 2, w / 2 + math.cos(a) * 4.5, h / 2 + math.sin(a) * 3.5, 1.2)
    return _img([Parte(m, 'laranja', z=1)], w, h)


def abobora(rnd, w=18, h=14):
    P = [Parte(elipse(5, h - 6, 4.5, 4.5), 'abobora', z=1), Parte(elipse(w - 6, h - 6, 4.5, 4.5), 'abobora', z=1),
         Parte(elipse(w / 2, h - 6, 5, 5), 'abobora', z=2), Parte(capsula(w / 2, h - 11, w / 2 + 2, h - 13, 1.0), 'verde', z=3)]
    return _img(P, w, h)


def boneco_neve(rnd, w=20, h=30):
    P = [Parte(elipse(w / 2, h - 7, 7, 6), 'branco', z=1), Parte(elipse(w / 2, h - 17, 5, 4.5), 'branco', z=2),
         Parte(elipse(w / 2, h - 24, 4, 3.6), 'branco', z=3),
         Parte({(w // 2 + 1, h - 24), (w // 2 + 2, h - 24), (w // 2 + 3, h - 24)}, None, z=5, cor='#fb6b1d', separar=False),
         Parte({(w // 2 - 1, h - 26), (w // 2 + 2, h - 26)}, None, z=5, cor='#2e222f', separar=False),
         Parte(ret(w / 2 - 5, h - 21, w / 2 + 4, h - 20), 'tecido_verm', z=4),
         Parte(capsula(w / 2 - 5, h - 17, 1, h - 21, 0.7), 'madeira', z=0)]
    return _img(P, w, h)


def minerio(rnd, rocha='pedra', cores=('#cd683d', '#f57d4a', '#fbb954'), w=36, h=28, cristal=None):
    """Rocha com veios de minério a brilhar (pedaços em losango com brilho em cima à esquerda) ou com cristais."""
    img = N.rocha(rnd, w, h, rocha)
    if cristal:
        cr = cristais(rnd, cristal, 20, 22)
        img.paste(cr, (w // 2 - 10, 0), cr)
        return img
    px = img.load()
    esc, med, claro = (hexrgb(c) + (255,) for c in cores)
    feitos = 0
    for _t in range(200):
        if feitos >= 10:
            break
        x, y = rnd.randrange(3, w - 4), rnd.randrange(h // 3, h - 4)
        pts = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1), (x, y - 1), (x + 2, y), (x - 1, y + 1), (x + 2, y + 1)]
        if all(px[a, b][3] and px[a, b][:3] != hexrgb(M.OUT) for a, b in pts):
            for a, b in pts:
                px[a, b] = med
            px[x, y - 1] = claro
            px[x, y] = claro
            px[x + 1, y + 1] = esc
            feitos += 1
    return img


def cogumelo_gigante(rnd, w=56, h=64, chapeu='vermelho'):
    P = [Parte(poligono([(w / 2 - 6, h - 1), (w / 2 - 4, h - 30), (w / 2 + 4, h - 30), (w / 2 + 7, h - 1)]), 'branco', z=1, volume='cilindro_v'),
         Parte(elipse(w / 2, h - 34, w / 2 - 2, 15) - {(x, y) for x in range(w) for y in range(h - 30, h)}, chapeu, z=3),
         Parte(elipse(w / 2, h - 30, w / 2 - 8, 3), 'castanho', z=2, plano=True)]
    img = _img(P, w, h)
    px = img.load()
    for cx, cy, r in ((w / 2 - 12, h - 40, 3), (w / 2 + 6, h - 44, 4), (w / 2 + 16, h - 36, 2.5), (w / 2 - 2, h - 36, 2), (w / 2 - 20, h - 34, 2)):
        for (x, y) in elipse(cx, cy, r, r * 0.8):
            if 0 <= x < w and 0 <= y < h and px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                px[x, y] = hexrgb('#ffffff' if (x + y) % 5 else '#c7dcd0') + (255,)
    return img


# ---------------------------------------------------------------- feitos por gente ----------------------------------------------------------------

def cerca(rnd, w=36, h=20, madeira='madeira', partida=False):
    P = []
    for k, x in enumerate((3, w // 2, w - 4)):
        if partida and k == 2:
            P.append(Parte(ret(x - 1.5, h - 9, x + 1.5, h - 1), madeira, z=2, volume='cilindro_v'))
            continue
        P.append(Parte(poligono([(x - 2, h - 1), (x - 2, h - 15), (x, h - 17), (x + 2, h - 15), (x + 2, h - 1)]), madeira, z=2, volume='cilindro_v'))
    fim = w - 2 if not partida else w * 0.7
    P.append(Parte(ret(1, h - 13, fim, h - 11), madeira, z=1, volume='cilindro_h'))
    P.append(Parte(ret(1, h - 7, w - 2, h - 5), madeira, z=1, volume='cilindro_h'))
    return _img(P, w, h)


def placa(rnd, w=20, h=26, madeira='madeira'):
    P = [Parte(ret(w / 2 - 1, 8, w / 2 + 1, h - 1), madeira, z=1, volume='cilindro_v'),
         Parte(poligono([(2, 4), (w - 5, 4), (w - 2, 7.5), (w - 5, 11), (2, 11)]), madeira, z=2, plano=True)]
    img = _img(P, w, h)
    px = img.load()
    for x in range(5, w - 7, 2):   # letras riscadas
        px[x, 7] = hexrgb('#45293f') + (255,)
        px[x, 8] = hexrgb('#45293f') + (255,)
    return img


def barril(rnd, w=16, h=20, madeira='madeira'):
    P = [Parte(poligono([(3, h - 1), (2, h - 9), (3, 2), (w - 4, 2), (w - 3, h - 9), (w - 4, h - 1)]), madeira, z=1, volume='cilindro_v'),
         Parte(ret(2, 5, w - 3, 6), 'ferro', z=2, volume='cilindro_v'), Parte(ret(2, h - 6, w - 3, h - 5), 'ferro', z=2, volume='cilindro_v'),
         Parte(elipse(w / 2 - 0.5, 2.5, w / 2 - 3.5, 1.5), madeira, z=3, plano=True)]
    return _img(P, w, h)


def caixote(rnd, w=18, h=18, madeira='madeira'):
    P = [Parte(ret(1, 4, w - 2, h - 1), madeira, z=1, plano=True),
         Parte(poligono([(1, 4), (5, 1), (w - 2, 1), (w - 2, 4)]), madeira, z=2, plano=True, luz=0.4)]
    img = _img(P, w, h)
    px = img.load()
    esc = hexrgb(R[madeira][0]) + (255,)
    for i in range(5, h - 2):   # tábuas cruzadas
        x = 2 + int((i - 5) * (w - 5) / (h - 7))
        px[x, i] = esc
        px[w - 3 - (x - 2), i] = esc
    return img


def carroca(rnd, w=52, h=34, madeira='madeira'):
    P = [Parte(poligono([(4, 10), (w - 10, 10), (w - 8, 22), (6, 22)]), madeira, z=2, plano=True),
         Parte(ret(6, 22, w - 10, 24), madeira, z=3, volume='cilindro_h'),
         Parte(capsula(w - 9, 20, w - 1, 26, 1.2), madeira, z=1, volume='cilindro_v'),
         Parte(elipse(14, h - 6, 5.5, 5.5), madeira, z=4),
         Parte(elipse(14, h - 6, 1.6, 1.6), 'ferro', z=5),
         # a outra roda está partida, caída ao lado
         Parte(elipse(w - 14, h - 3, 6, 2.2), madeira, z=0, plano=True)]
    img = _img(P, w, h)
    px = img.load()
    for x in range(6, w - 10, 6):   # tábuas
        for y in range(11, 22):
            if px[x, y][3]:
                px[x, y] = hexrgb(R[madeira][1]) + (255,)
    return img


def pilar(rnd, w=18, h=44, rampa='pedra', partido=True, musgo='musgo'):
    topo = 10 if partido else 4
    P = [Parte(ret(1, h - 5, w - 2, h - 1), rampa, z=1, plano=True),
         Parte(poligono([(3, h - 5), (3, topo + 3), (6, topo), (9, topo + 4), (w - 4, topo - (2 if partido else 0)), (w - 4, h - 5)]), rampa, z=2, volume='cilindro_v')]
    if not partido:
        P.append(Parte(ret(1, 1, w - 2, 4), rampa, z=3, plano=True))
    if musgo:
        P.append(Parte({(x, y) for x in range(3, w - 3) for y in range(h - 9, h - 5) if (x * 3 + y) % 4}, musgo, z=4, separar=False))
    img = _img(P, w, h)
    px = img.load()
    for y in range(topo + 6, h - 6, 3):   # caneluras
        for x in (6, 10):
            if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                px[x, y] = hexrgb(R[rampa][1]) + (255,)
    if partido:   # pedaço caído
        pass
    return img


def menir(rnd, w=18, h=36, rampa='pedra', runa='#4d9be6'):
    P = [Parte(poligono([(3, h - 1), (2, h - 16), (5, 3), (10, 1), (w - 4, 6), (w - 3, h - 1)]), rampa, z=1)]
    img = _img(P, w, h)
    px = img.load()
    for x, y in ((8, 12), (9, 13), (10, 12), (9, 14), (9, 15), (8, 16), (10, 16), (9, 18), (8, 19), (10, 19)):
        px[x, y] = hexrgb(runa) + (255,)
    return img


def fogueira_apagada(rnd, w=28, h=16):
    """Cinza escura no meio, lenha queimada cruzada (com uma brasa) e um anel de pedras."""
    P = [Parte(elipse(w / 2, h - 6, 9, 4), 'preto', z=0, plano=True)]
    P.append(Parte(capsula(w / 2 - 6, h - 8, w / 2 + 5, h - 5, 1.6), 'queimado', z=2, volume='cilindro_h'))
    P.append(Parte(capsula(w / 2 - 5, h - 4, w / 2 + 6, h - 8, 1.6), 'queimado', z=3, volume='cilindro_h'))
    P.append(Parte({(w // 2, h - 6), (w // 2 + 1, h - 6)}, None, z=4, cor='#ea4f36', separar=False))
    for k in range(8):
        a = k * 2 * math.pi / 8 + 0.2
        z = 5 if math.sin(a) > 0 else 1
        P.append(Parte(elipse(w / 2 + math.cos(a) * 11, h - 6 + math.sin(a) * 5, 2.6, 2.1), 'pedra', z=z))
    return _img(P, w, h)


def tenda(rnd, w=44, h=34, tecido='tecido_bege', madeira='madeira'):
    P = [Parte(poligono([(2, h - 1), (w / 2, 3), (w - 3, h - 1)]), tecido, z=1, plano=True),
         Parte(poligono([(w / 2 - 6, h - 1), (w / 2, h - 16), (w / 2 + 6, h - 1)]), 'preto', z=2, plano=True),
         Parte(capsula(w / 2, 1, w / 2, 5, 0.8), madeira, z=3, volume='cilindro_v'),
         Parte(poligono([(w / 2 + 1, h - 15), (w / 2 + 9, h - 1), (w / 2 + 6, h - 1)]), tecido, z=3, plano=True, luz=0.3)]
    return _img(P, w, h)


def anfora(rnd, w=14, h=20, rampa='barro', partida=False):
    P = [Parte(elipse(w / 2, h - 7, 5, 6), rampa, z=1), Parte(ret(w / 2 - 2, 3, w / 2 + 1, 8), rampa, z=2, volume='cilindro_v'),
         Parte(ret(w / 2 - 3, 2, w / 2 + 2, 3), rampa, z=3, plano=True)]
    img = _img(P, w, h)
    if partida:
        img = M.deitar(img)
    return img


def ancora(rnd, w=22, h=26):
    P = [Parte(ret(w / 2 - 1, 5, w / 2 + 1, h - 4), 'ferro', z=2, volume='cilindro_v'),
         Parte(elipse(w / 2, 3, 2.5, 2.5) - elipse(w / 2, 3, 1, 1), 'ferro', z=3),
         Parte(ret(w / 2 - 6, 8, w / 2 + 5, 9), 'ferro', z=3, volume='cilindro_h')]
    arco = {(x, y) for x in range(2, w - 2) for y in range(h - 9, h) if abs(math.hypot(x + .5 - w / 2, (y + .5 - (h - 11)) * 1.0) - 8.5) < 1.2 and y > h - 9}
    P.append(Parte(arco, 'ferro', z=1, plano=True))
    return _img(P, w, h)


def campa(rnd, w=16, h=22, rampa='pedra', cruz=False):
    if cruz:
        P = [Parte(ret(w / 2 - 1.5, 2, w / 2 + 1.5, h - 1), rampa, z=1, volume='cilindro_v'),
             Parte(ret(2, 6, w - 3, 8), rampa, z=2, volume='cilindro_h')]
    else:
        P = [Parte(ret(2, 6, w - 3, h - 1) | elipse(w / 2 - 0.5, 7, w / 2 - 2.5, 5), rampa, z=1, plano=True)]
        P.append(Parte({(x, y) for x in range(5, w - 5) for y in range(9, h - 4) if (x + y) % 3 == 0 and y % 3 != 1}, None, z=2,
                       cor=R[rampa][1], separar=False))
    P.append(Parte(elipse(w / 2, h - 1, w / 2 - 1, 1.5), 'musgo', z=3, separar=False))
    return _img(P, w, h)


# ---------------------------------------------------------------- edifícios em sprite (povoações sem peças 3D)

def cabana(rnd, w=88, h=80, madeira='madeira', telhado='tecido_verm', chamine=True):
    """Cabana de troncos: paredes de troncos deitados, telhado de duas águas, porta, janela com luz e chaminé."""
    base = h - 1
    topo_parede = h - 34
    P = [Parte(ret(6, topo_parede, w - 7, base), madeira, z=1, plano=True)]
    P.append(Parte(poligono([(1, topo_parede + 2), (w / 2, 6), (w - 2, topo_parede + 2)]), telhado, z=3, plano=True))
    P.append(Parte(ret(w / 2 - 6, base - 18, w / 2 + 5, base), 'castanho', z=4, plano=True))           # porta
    P.append(Parte(ret(14, topo_parede + 8, 25, topo_parede + 17), 'amarelo', z=4, plano=True))       # janela acesa
    P.append(Parte(ret(w - 26, topo_parede + 8, w - 15, topo_parede + 17), 'amarelo', z=4, plano=True))
    if chamine:
        P.append(Parte(ret(w - 26, 8, w - 18, 26), 'pedra', z=2, plano=True))
    img = _img(P, w, h)
    px = img.load()
    esc = hexrgb(R[madeira][0]) + (255,)
    for y in range(topo_parede + 3, base, 5):    # troncos deitados
        for x in range(7, w - 7):
            if px[x, y][3] and px[x, y][:3] in [hexrgb(c) for c in R[madeira][1:4]]:
                px[x, y] = esc
    for y in range(12, topo_parede, 4):          # telhas
        for x in range(2, w - 2):
            if px[x, y][3] and px[x, y][:3] in [hexrgb(c) for c in R[telhado][1:4]]:
                px[x, y] = hexrgb(R[telhado][1]) + (255,)
    for (x0, y0) in ((14, topo_parede + 8), (w - 26, topo_parede + 8)):   # caixilho em cruz
        for k in range(12):
            if 0 <= x0 + 5 < w:
                px[x0 + 5, y0 + min(k, 9)] = hexrgb('#694f62') + (255,)
            px[x0 + min(k, 11), y0 + 4] = hexrgb('#694f62') + (255,)
    return img


def casa_arvore(rnd, w=104, h=136):
    """Casa élfica redonda no cimo de uma árvore gigante, com escada de corda e uma lanterna de seiva."""
    arvore = N.copa(rnd, w, h, 'folha_esc', 'tronco', raio=(10, 14), n=16, larg_tronco=14)
    img = arvore.copy()
    P = [Parte(elipse(w / 2, 50, 22, 16), 'madeira', z=1),
         Parte(poligono([(w / 2 - 26, 46), (w / 2, 22), (w / 2 + 26, 46)]), 'verde', z=2, plano=True),
         Parte(ret(w / 2 - 4, 52, w / 2 + 4, 64), 'castanho', z=3, plano=True),
         Parte(elipse(w / 2 - 12, 52, 3, 3), 'amarelo', z=3),
         Parte(ret(w / 2 - 28, 64, w / 2 + 28, 67), 'madeira', z=2, plano=True)]
    casa = _img(P, w, h)
    img.paste(casa, (0, 0), casa)
    px = img.load()
    for y in range(68, h - 4, 3):     # escada de corda
        for x in (w // 2 + 12, w // 2 + 18):
            px[x, y] = hexrgb('#ab947a') + (255,)
        for x in range(w // 2 + 12, w // 2 + 19):
            if y % 6 == 2:
                px[x, y] = hexrgb('#966c6c') + (255,)
    return img


def pilha_troncos(rnd, w=44, h=26):
    P = []
    k = 0
    for fila, n in ((0, 4), (1, 3), (2, 2)):
        for i in range(n):
            x = 8 + i * 9 + fila * 4.5
            y = h - 6 - fila * 7
            P.append(Parte(elipse(x, y, 4.6, 4.6), 'madeira', z=k))
            P.append(Parte(elipse(x, y, 2, 2), 'castanho', z=k + 1, plano=True))
            k += 2
    return _img(P, w, h)


def lanterna(rnd, w=12, h=34, luz='agua'):
    P = [Parte(ret(w / 2 - 1, 10, w / 2, h - 1), 'madeira', z=1, volume='cilindro_v'),
         Parte(elipse(w / 2 - 0.5, 7, 4, 5), luz, z=2),
         Parte(ret(w / 2 - 3, 1, w / 2 + 2, 2), 'madeira', z=3, plano=True)]
    return _img(P, w, h)


def estalagmite(rnd, w=14, h=30, rampa='pedra', n=1, musgo=None):
    """Estalagmites (cones de pedra com anéis de calcário); n > 1 faz um grupo, a maior atrás."""
    P = []
    cones = [(w / 2, h - 1, w / 2 - 1)] if n == 1 else []
    for k in range(n if n > 1 else 0):
        alt = h * rnd.uniform(0.45, 0.95) if k else h - 1
        larg = max(3.0, alt * rnd.uniform(0.18, 0.26))
        cones.append((rnd.uniform(larg + 1, w - larg - 1) if k else w / 2, alt, larg))
    cones.sort(key=lambda c: -c[1])
    for k, (cx, alt, larg) in enumerate(cones):
        topo = h - 1 - alt
        pts = [(cx - larg, h - 1), (cx - larg * 0.55, h - 1 - alt * 0.45), (cx - 1.0, topo + 1), (cx + 0.5, topo),
               (cx + larg * 0.5, h - 1 - alt * 0.5), (cx + larg, h - 1)]
        P.append(Parte(poligono(pts), rampa, z=k * 2, volume='cilindro_v'))
        if musgo:
            P.append(Parte({(int(cx + dx), h - 2 - dy) for dx in range(-int(larg), int(larg) + 1) for dy in range(2)}, musgo, z=k * 2 + 1,
                           separar=False))
    img = _img(P, w, h)
    px = img.load()
    r = N.R[rampa]
    for y in range(3, h - 2, 4):   # anéis do calcário
        for x in range(w):
            if px[x, y][3] and px[x, y][:3] != hexrgb('#2e222f') and rnd.random() < 0.8:
                px[x, y] = hexrgb(r[1]) + (255,)
    return img


def teia(rnd, w=34, h=30):
    """Teia de aranha esticada entre duas pedras (fios brancos finos, sem contorno)."""
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    px = img.load()
    cx, cy = w / 2, h * 0.45
    branco, cinza = hexrgb('#c7dcd0') + (255,), hexrgb('#9babb2') + (255,)
    raios = 9
    for k in range(raios):   # fios do centro para fora
        a = k * 2 * math.pi / raios + rnd.uniform(-0.1, 0.1)
        for t in range(0, 40):
            x, y = int(round(cx + math.cos(a) * t * 0.5)), int(round(cy + math.sin(a) * t * 0.42))
            if 0 <= x < w and 0 <= y < h:
                px[x, y] = branco
    for anel in range(2, 9, 2):   # espiral
        for k in range(raios * 6):
            a = k * 2 * math.pi / (raios * 6)
            x, y = int(round(cx + math.cos(a) * anel * 2.0)), int(round(cy + math.sin(a) * anel * 1.65))
            if 0 <= x < w and 0 <= y < h and rnd.random() < 0.8:
                px[x, y] = cinza
    return img


def casulo(rnd, w=12, h=20):
    P = [Parte(elipse(w / 2, h / 2 + 1, w / 2 - 1.5, h / 2 - 2), 'branco', z=1),
         Parte({(w // 2, y) for y in range(0, 4)}, 'branco', z=0, plano=True, separar=False)]
    img = _img(P, w, h)
    px = img.load()
    for y in range(4, h - 2, 3):   # voltas do fio
        for x in range(w):
            if px[x, y][3] and px[x, y][:3] != hexrgb('#2e222f'):
                px[x, y] = hexrgb('#9babb2') + (255,)
    return img


def bigorna(rnd, w=24, h=18):
    P = [Parte(ret(8, 10, 15, h - 2), 'ferro', z=1, volume='cilindro_v'),
         Parte(ret(5, h - 3, 18, h - 1), 'pedra', z=0, plano=True),
         Parte(poligono([(2, 6), (21, 6), (21, 10), (6, 10), (2, 8)]), 'ferro', z=2, volume='cilindro_h')]
    return _img(P, w, h)


def brasas(rnd, w=20, h=10):
    """Monte de carvão a arder (brilha no escuro)."""
    P = [Parte(elipse(w / 2, h - 4, w / 2 - 1, 3.5), 'preto', z=1)]
    img = _img(P, w, h)
    px = img.load()
    for _ in range(14):
        x, y = rnd.randrange(3, w - 3), rnd.randrange(h - 7, h - 2)
        if px[x, y][3]:
            px[x, y] = hexrgb(rnd.choice(['#ea4f36', '#f79617', '#f9c22b'])) + (255,)
    return img


def camelo(rnd, w=36, h=32):
    """Camelo de lado (virado para a direita), com uma bossa e uma manta às riscas."""
    P = [Parte(capsula(8, 24, 8, 31, 1.4), 'castanho', z=0, volume='cilindro_v'), Parte(capsula(13, 24, 13, 31, 1.4), 'castanho', z=2, volume='cilindro_v'),
         Parte(capsula(22, 24, 22, 31, 1.4), 'castanho', z=0, volume='cilindro_v'), Parte(capsula(27, 24, 27, 31, 1.4), 'castanho', z=2, volume='cilindro_v'),
         Parte(elipse(17, 20, 11, 5.5), 'castanho', z=3), Parte(elipse(16, 13, 5, 4.5), 'castanho', z=4),
         Parte(capsula(26, 18, 30, 8, 2), 'castanho', z=5), Parte(elipse(32, 7, 3.5, 2.6), 'castanho', z=6),
         Parte(ret(12, 16, 21, 19), 'tecido_verm', z=7, plano=True)]
    img = _img(P, w, h)
    px = img.load()
    px[33, 6] = hexrgb('#2e222f') + (255,)
    for x in range(12, 22, 2):
        px[x, 17] = hexrgb('#f9c22b') + (255,)
    return img


def escora_mina(rnd, w=44, h=46, madeira='madeira'):
    """Escora de mina: dois postes e uma trave por cima, com uma lanterna pendurada."""
    P = [Parte(ret(4, 8, 8, h - 1), madeira, z=1, volume='cilindro_v'),
         Parte(ret(w - 9, 8, w - 5, h - 1), madeira, z=1, volume='cilindro_v'),
         Parte(ret(1, 4, w - 2, 9), madeira, z=2, volume='cilindro_h'),
         Parte(ret(8, 9, 12, 12), madeira, z=3, plano=True), Parte(ret(w - 13, 9, w - 9, 12), madeira, z=3, plano=True),
         Parte({(w // 2, y) for y in range(10, 15)}, 'preto', z=4, plano=True, separar=False),
         Parte(elipse(w / 2, 18, 3, 3.6), 'laranja', z=5)]
    return _img(P, w, h)


def banca(rnd, w=52, h=44, toldo='tecido_verm', madeira='madeira', bens=('vermelho', 'amarelo', 'verde')):
    P = [Parte(ret(4, 10, 6, h - 1), madeira, z=1, volume='cilindro_v'), Parte(ret(w - 7, 10, w - 5, h - 1), madeira, z=1, volume='cilindro_v'),
         Parte(ret(2, h - 16, w - 3, h - 10), madeira, z=2, plano=True),
         Parte(poligono([(0, 14), (6, 2), (w - 7, 2), (w - 1, 14)]), toldo, z=3, plano=True)]
    for i, b in enumerate(bens * 3):
        P.append(Parte(elipse(9 + i * 4.5, h - 18, 2.2, 2.2), b, z=4))
    img = _img(P, w, h)
    px = img.load()
    for x in range(1, w - 1):    # riscas do toldo
        if (x // 5) % 2:
            for y in range(3, 14):
                if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                    px[x, y] = hexrgb('#ffffff') + (255,)
    return img


def chama(fases=6, w=20, h=26):
    """Chama de fogueira animada (sem contorno: o fogo não tem linha à volta). Devolve a tira de frames."""
    frames = []
    for f in range(fases):
        P = []
        for k, (rampa, esc) in enumerate((('vermelho', 1.0), ('laranja', 0.72), ('amarelo', 0.45))):
            topo = 3 + (f * 3 + k * 2) % 5 + k * 5
            balanco = math.sin(f * 2 * math.pi / fases + k) * 2
            pts = [(w / 2 - 8 * esc, h - 1), (w / 2 - 6 * esc + balanco * 0.3, h - 9), (w / 2 + balanco, topo),
                   (w / 2 + 5 * esc + balanco * 0.5, h - 10), (w / 2 + 8 * esc, h - 1)]
            P.append(Parte(poligono(pts), rampa, z=k, plano=True, separar=False))
        img = desenhar(P, w, h, contorno_fora=False)
        px = img.load()
        for _ in range(2):   # faúlhas
            x, y = (f * 7 + _ * 11) % (w - 4) + 2, (f * 5 + _ * 3) % 6 + 1
            px[x, y] = hexrgb('#fbff86') + (255,)
        frames.append(img)
    return M.tira(frames)


# ---------------------------------------------------------------- por região ----------------------------------------------------------------

def por_regiao():
    """{região: {'detalhes': [(nome, img)], 'objetos': [(nome, img)]}}"""
    rnd = random.Random(11)
    comum = {'barril': barril(rnd), 'caixote': caixote(rnd), 'cerca': cerca(rnd), 'cerca_partida': cerca(rnd, partida=True),
             'placa': placa(rnd), 'fogueira_apagada': fogueira_apagada(rnd)}
    out = {}
    povoacao_r1 = [('cabana', cabana(rnd)), ('cabana_elfica', cabana(rnd, 72, 70, telhado='verde', chamine=False)),
                   ('casa_arvore', casa_arvore(rnd)), ('pilha_troncos', pilha_troncos(rnd)), ('lanterna_seiva', lanterna(rnd)),
                   ('banca_elfica', banca(rnd, toldo='verde')),
                   # para todas as povoações
                   ('lanterna_quente', lanterna(rnd, luz='amarelo')), ('banca_vermelha', banca(rnd)),
                   ('banca_azul', banca(rnd, toldo='tecido_azul', bens=('laranja', 'rosa', 'branco'))),
                   ('estendal', cerca(rnd, 44, 22, partida=False)), ('barril_2', barril(rnd)), ('caixote_2', caixote(rnd))]
    out[1] = {'povoacao': povoacao_r1, 'detalhes': [('tronco_caido', tronco_caido(rnd, cobertura='musgo')), ('toco', toco(rnd, cogumelos='vermelho')), ('toco_2', toco(rnd)),
                           ('cogumelos', cogumelos(rnd)), ('cogumelos_castanhos', cogumelos(rnd, chapeu='castanho', pintas=False)),
                           ('erva_alta_1', erva_alta(rnd)), ('erva_alta_2', erva_alta(rnd, 'folha_esc', 18, 20)),
                           ('juncos', N.tufo(rnd, 14, 26, 'musgo', 8, False))],
              'objetos': list(comum.items()) + [('carroca', carroca(rnd)), ('pilar_partido', pilar(rnd)), ('menir', menir(rnd)),
                                                ('tenda', tenda(rnd))]}
    out[2] = {'detalhes': [('cristais_azuis', cristais(rnd, 'cristal_a')), ('cristais_rosa', cristais(rnd, 'cristal_r')),
                           ('cristais_verdes', cristais(rnd, 'cristal_v', 16, 18)), ('ossos', ossos(rnd)),
                           ('cogumelos_cave', cogumelos(rnd, chapeu='lilas', pintas=False)),
                           ('estalagmites_grupo', estalagmite(rnd, 34, 36, n=4)), ('estalagmite_baixa', estalagmite(rnd, 12, 18)),
                           ('teia', teia(rnd)), ('casulo', casulo(rnd)), ('bigorna', bigorna(rnd)), ('brasas_forja', brasas(rnd)),
                           ('cristal_alto_azul', cristais(rnd, 'cristal_a', 22, 44)), ('cristal_alto_rosa', cristais(rnd, 'cristal_r', 22, 44)),
                           ('cristais_negros', cristais(rnd, 'roxo', 20, 26))],
              'objetos': [('barril', comum['barril']), ('caixote', comum['caixote']), ('placa', comum['placa']),
                          ('fogueira_apagada', comum['fogueira_apagada']), ('pilar_partido', pilar(rnd, musgo=None)),
                          ('escora_mina', escora_mina(rnd)), ('lanterna_mina', lanterna(rnd, luz='laranja'))]}
    out[3] = {'detalhes': [('tronco_caido', tronco_caido(rnd, casca='tronco', cobertura='folha')), ('toco', toco(rnd, cogumelos='laranja')),
                           ('cogumelos', cogumelos(rnd, chapeu='laranja')), ('erva_alta', erva_alta(rnd, 'selva')),
                           ('juncos', N.tufo(rnd, 14, 26, 'musgo', 8, False))],
              'objetos': [('barril', comum['barril']), ('caixote', comum['caixote']), ('placa', comum['placa']),
                          ('pilar_musgo', pilar(rnd, rampa='verde_esc', musgo='folha')), ('menir', menir(rnd, rampa='verde_esc', runa='#30e1b9'))]}
    out[4] = {'detalhes': [('ossos', ossos(rnd)), ('cranio_grande', ossos(rnd, 30, 16)), ('erva_seca_alta', erva_alta(rnd, 'seco', 18, 18)),
                           ('anfora_partida', anfora(rnd, partida=True))],
              'objetos': [('anfora', anfora(rnd)), ('barril', comum['barril']), ('caixote', comum['caixote']),
                          ('pilar_areia', pilar(rnd, rampa='seco', musgo=None)), ('tenda_deserto', tenda(rnd, tecido='tecido_verm')),
                          ('camelo', camelo(rnd)), ('pedra_enigma', menir(rnd, rampa='seco', runa='#4d9be6')),
                          ('fogueira_apagada', comum['fogueira_apagada'])]}
    out[5] = {'detalhes': [('tronco_nevado', tronco_caido(rnd, cobertura='neve')), ('toco_nevado', toco(rnd)),
                           ('cristais_gelo', cristais(rnd, 'cristal_a', 18, 20))],
              'objetos': [('boneco_neve', boneco_neve(rnd)), ('tenda_azul', tenda(rnd, tecido='tecido_azul')), ('caixote', comum['caixote']),
                          ('fogueira_apagada', comum['fogueira_apagada']), ('placa', comum['placa'])]}
    out[6] = {'detalhes': [('concha_rosa', concha(rnd)), ('concha_azul', concha(rnd, rampa='azul')), ('estrela_mar', estrela_mar(rnd)),
                           ('tronco_deriva', tronco_caido(rnd, casca='palma'))],
              'objetos': [('ancora', ancora(rnd)), ('barril', comum['barril']), ('caixote', comum['caixote']), ('placa', comum['placa'])]}
    out[7] = {'detalhes': [('cristais_fogo', cristais(rnd, 'cristal_f')), ('ossos', ossos(rnd)), ('tronco_queimado', tronco_caido(rnd, casca='queimado'))],
              'objetos': [('pilar_negro', pilar(rnd, rampa='queimado', musgo=None)), ('menir_fogo', menir(rnd, rampa='queimado', runa='#f79617'))]}
    out[8] = {'detalhes': [('ossos', ossos(rnd)), ('abobora', abobora(rnd)), ('cogumelos_roxos', cogumelos(rnd, chapeu='roxo')),
                           ('toco_negro', toco(rnd, casca='negra'))],
              'objetos': [('campa', campa(rnd)), ('campa_2', campa(rnd, 14, 18)), ('cruz', campa(rnd, cruz=True)),
                          ('cerca_partida', cerca(rnd, madeira='negra', partida=True)), ('pilar_partido', pilar(rnd, rampa='preto', musgo='verde_esc'))]}
    out[9] = {'detalhes': [('cristais_ceu', cristais(rnd, 'cristal_a', 16, 18))],
              'objetos': [('pilar_branco', pilar(rnd, rampa='branco', musgo=None)), ('pilar_inteiro', pilar(rnd, rampa='branco', partido=False, musgo=None))]}
    out[10] = {'detalhes': [('cristais_vazio', cristais(rnd, 'roxo'))], 'objetos': []}
    # minério (pontos de recolha com picareta)
    minerios = {1: [('minerio_cobre', minerio(rnd))],
                2: [('minerio_ferro', minerio(rnd, cores=('#625565', '#c7dcd0', '#ffffff'))), ('veio_carvao', minerio(rnd, cores=('#2e222f', '#3e3546', '#9babb2')))],
                3: [('minerio_ferro_negro', minerio(rnd, 'verde_esc', ('#2e222f', '#3e3546', '#9babb2')))],
                4: [('minerio_prata', minerio(rnd, 'seco', ('#7f708a', '#c7dcd0', '#ffffff')))],
                5: [('gelo_eterno', minerio(rnd, cristal='cristal_a'))],
                6: [('minerio_coral', minerio(rnd, 'castanho', cristal='coral'))],
                7: [('obsidiana', minerio(rnd, 'queimado', cristal='negra'))],
                8: [('minerio_mitril', minerio(rnd, 'preto', ('#4d65b4', '#8fd3ff', '#ffffff')))],
                9: [('minerio_oricalco', minerio(rnd, 'branco', ('#f79617', '#f9c22b', '#fbff86')))],
                10: [('fragmento_estelar', minerio(rnd, 'preto', cristal='roxo'))]}
    for r, lista in minerios.items():
        out[r]['minerio'] = lista
    out[2]['gigante'] = [('coluna_gruta', estalagmite(rnd, 30, 78)), ('cogumelo_gigante_luz', cogumelo_gigante(rnd, chapeu='agua'))]
    out[3]['gigante'] = [('tronco_grande', tronco_caido(rnd, 72, 24, cobertura='folha')), ('cogumelo_gigante', cogumelo_gigante(rnd, chapeu='laranja'))]
    out[8]['gigante'] = [('pilar_grande', pilar(rnd, 22, 56, rampa='preto', musgo='verde_esc')), ('cogumelo_gigante', cogumelo_gigante(rnd, chapeu='roxo'))]
    out[1]['gigante'] = [('cogumelo_gigante', cogumelo_gigante(rnd)), ('tronco_grande', tronco_caido(rnd, 72, 24, cobertura='musgo'))]
    return out


# Temas de cada andar (gruta): [peça, quantas por célula aberta] — em molhos, onde o ruído do andar deixa.
TEMAS = {
    11: [['lanterna_mina', 0.12], ['escora_mina', 0.1], ['caixote', 0.08], ['cristais_azuis', 0.08]],
    12: [['escora_mina', 0.16], ['ossos', 0.12], ['caixote', 0.06], ['lanterna_mina', 0.06], ['estalagmite_baixa', 0.3]],
    13: [['cristais_azuis', 0.7], ['cristais_rosa', 0.5], ['cristais_verdes', 0.4], ['cristal_alto_azul', 0.18], ['cristal_alto_rosa', 0.14]],
    14: [['estalagmites_grupo', 0.3], ['estalagmite_baixa', 0.4], ['musgo_gruta_2', 1.5], ['cogumelo_luz_3', 0.4]],
    15: [['teia', 0.5], ['casulo', 0.3], ['ossos', 0.3], ['estalagmite_baixa', 0.2]],
    16: [['cogumelo_luz_1', 1.6], ['cogumelo_luz_2', 1.0], ['cogumelo_luz_3', 1.0], ['cogumelos_cave', 0.8], ['cogumelo_gigante_luz', 0.1]],
    17: [['estalagmites_grupo', 0.35], ['estalagmite_baixa', 0.5], ['ossos', 0.15], ['cristais_azuis', 0.1]],
    18: [['bigorna', 0.12], ['brasas_forja', 0.2], ['pilar_partido', 0.12], ['caixote', 0.05], ['lanterna_mina', 0.06]],
    19: [['cristais_negros', 0.5], ['cristais_azuis', 0.25], ['estalagmite_baixa', 0.3], ['cristal_alto_azul', 0.06]],
    20: [['cristal_alto_azul', 0.2], ['cristal_alto_rosa', 0.2], ['cristais_negros', 0.3], ['coluna_gruta', 0.06]],
}


# Cenários: [nome, [[peça, dx (m), dz (m), raio de colisão (m)], ...]] — as peças são nomes de detalhes/objetos/plantas da região
CENARIOS = {
    1: [['acampamento', [['tenda', 0, -1.5, 1.3], ['fogueira_apagada', 0, 1.2, 0], ['tronco_caido', -2.6, 1.3, 0.8], ['caixote', 2.4, -0.4, 0.5],
                         ['barril', 2.9, 0.4, 0.4]]],
        ['ruina', [['pilar_partido', -2, -1.5, 0.5], ['pilar_partido', 2, -1.6, 0.5], ['pilar_partido', -2.2, 1.6, 0.5], ['pedra_1', 1.6, 1.2, 0],
                   ['pedra_2', 0.3, 0.2, 0], ['erva_alta_1', 2.4, 1.8, 0], ['erva_alta_2', -1, -2, 0]]],
        ['circulo_cogumelos', [['cogumelos', 0, -1.8, 0], ['cogumelos', 1.7, -0.6, 0], ['cogumelos_castanhos', 1.1, 1.4, 0],
                               ['cogumelos', -1.1, 1.4, 0], ['cogumelos_castanhos', -1.7, -0.6, 0], ['flor_branca', 0, 0, 0]]],
        ['cerca_velha', [['cerca', -1.1, 0, 0.3], ['cerca_partida', 1.2, 0, 0.3], ['placa', 3, 0.5, 0.2], ['erva_alta_1', -2.6, 0.6, 0]]],
        ['carroca_partida', [['carroca', 0, 0, 1.4], ['barril', -2.4, 0.8, 0.4], ['caixote', 2.4, 1.2, 0.5], ['caixote', 2.9, 0.4, 0.5]]],
        ['pedras_antigas', [['menir', 0, -1.6, 0.5], ['menir', 1.8, 0.4, 0.5], ['menir', -1.8, 0.4, 0.5], ['pedra_3', 0, 1, 0]]],
        ['clareira_tocos', [['toco', -1, 0, 0.4], ['toco_2', 1.2, -0.8, 0.4], ['toco', 0.6, 1.4, 0.4], ['tronco_caido', -1.5, -1.8, 0.8]]]],
    2: [['mina_velha', [['caixote', 0, 0, 0.5], ['barril', 1, 0.6, 0.4], ['placa', -1.5, -0.5, 0.2], ['cristais_azuis', 2.2, -1, 0.3]]],
        ['escoramento', [['escora_mina', 0, -0.5, 0.4], ['caixote', 2.4, 0.4, 0.5], ['lanterna_mina', -2.4, 0.3, 0.2], ['pedra_2', 1.0, 1.2, 0]]],
        ['acampamento_mineiro', [['fogueira_apagada', 0, 0.6, 0], ['caixote', 2, -0.8, 0.5], ['barril', 2.6, 0.2, 0.4], ['lanterna_mina', -2.2, -0.6, 0.2],
                                 ['ossos', -1.2, 1.6, 0]]],
        ['bosque_estalagmites', [['estalagmites_grupo', 0, 0, 0.8], ['estalagmite_baixa', 1.8, 1.0, 0.3], ['estalagmite_baixa', -1.7, 0.7, 0.3],
                                 ['pedra_1', 0.6, 1.8, 0]]],
        ['cogumelal', [['cogumelo_luz_1', 0, 0, 0], ['cogumelo_luz_2', 1.2, 0.6, 0], ['cogumelos_cave', -1.1, 0.5, 0], ['cogumelo_luz_3', 0.4, -1.2, 0],
                       ['cogumelo_luz_1', -0.6, 1.5, 0], ['cogumelo_luz_2', 1.8, -0.6, 0]]],
        ['jardim_cristal', [['cristais_azuis', 0, 0, 0.4], ['cristais_rosa', 1.5, 0.8, 0.4], ['cristais_verdes', -1.4, 0.6, 0.3], ['cristais_azuis', 0.4, -1.6, 0.4]]],
        ['acampamento', [['fogueira_apagada', 0, 0, 0], ['caixote', 1.8, -0.8, 0.5], ['ossos', -1.6, 0.8, 0]]]],
    3: [['ruina_musgo', [['pilar_musgo', -1.5, -1, 0.5], ['pilar_musgo', 1.6, -1.2, 0.5], ['juncos', 0, 1, 0], ['tronco_caido', 0.5, 1.8, 0.8]]],
        ['circulo_cogumelos', [['cogumelos', 0, -1.6, 0], ['cogumelos', 1.5, 0, 0], ['cogumelos', 0, 1.6, 0], ['cogumelos', -1.5, 0, 0]]],
        ['pedras_antigas', [['menir', 0, 0, 0.5], ['menir', 1.8, 0.8, 0.5], ['juncos', -1.3, 1, 0]]]],
    4: [['caravana', [['tenda_deserto', 0, -1.4, 1.3], ['fogueira_apagada', 0, 1.2, 0], ['anfora', 2.2, 0, 0.3], ['anfora_partida', 2.6, 1, 0],
                      ['caixote', -2.4, 0.3, 0.5]]],
        ['templo_enterrado', [['pilar_areia', -2, -1, 0.5], ['pilar_areia', 2, -1, 0.5], ['anfora_partida', 0, 1, 0], ['cranio_grande', 1.5, 1.8, 0]]],
        ['ossada', [['cranio_grande', 0, 0, 0], ['ossos', 1.5, 0.8, 0], ['ossos', -1.4, 0.6, 0]]]],
    5: [['acampamento_neve', [['tenda_azul', 0, -1.4, 1.3], ['fogueira_apagada', 0, 1.2, 0], ['caixote', 2.2, 0, 0.5], ['tronco_nevado', -2.6, 1, 0.8]]],
        ['bonecos', [['boneco_neve', 0, 0, 0.4], ['boneco_neve', 1.8, 0.8, 0.4], ['placa', -1.5, 0.4, 0.2]]],
        ['gelo', [['cristais_gelo', 0, 0, 0.3], ['cristais_gelo', 1.2, 0.9, 0.3], ['cristais_gelo', -1.1, 0.7, 0.3]]]],
    6: [['naufragio', [['ancora', 0, 0, 0.4], ['barril', 1.6, 0.6, 0.4], ['caixote', -1.6, 0.5, 0.5], ['tronco_deriva', 0.5, 1.8, 0.8]]],
        ['praia', [['concha_rosa', 0, 0, 0], ['estrela_mar', 1, 0.6, 0], ['concha_azul', -0.8, 0.9, 0], ['estrela_mar', -1.4, -0.5, 0]]]],
    7: [['altar_fogo', [['menir_fogo', 0, -1, 0.5], ['pilar_negro', -1.8, 0.4, 0.5], ['pilar_negro', 1.8, 0.4, 0.5], ['cristais_fogo', 0, 1, 0.3]]],
        ['ossada', [['ossos', 0, 0, 0], ['ossos', 1.3, 0.7, 0], ['cristais_fogo', -1.3, 0.4, 0.3]]]],
    8: [['cemiterio', [['campa', -1.6, -1, 0.4], ['campa_2', 0, -1.2, 0.4], ['cruz', 1.6, -1, 0.3], ['campa', -0.8, 1, 0.4], ['cruz', 1, 1, 0.3],
                       ['abobora', 2.4, 1.6, 0]]],
        ['horta_abandonada', [['abobora', 0, 0, 0], ['abobora', 1.2, 0.6, 0], ['abobora', -1, 0.8, 0], ['cerca_partida', 0, -1.5, 0.3]]],
        ['ruina', [['pilar_partido', -1.6, 0, 0.5], ['pilar_partido', 1.6, -0.3, 0.5], ['ossos', 0, 1, 0]]]],
    9: [['templo_ceu', [['pilar_inteiro', -2, -1, 0.5], ['pilar_branco', 2, -1, 0.5], ['pilar_inteiro', -2, 1.5, 0.5], ['cristais_ceu', 0.5, 0.4, 0.3]]]],
    10: [],
}
