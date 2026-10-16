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


# ---------------------------------------------------------------- por região ----------------------------------------------------------------

def por_regiao():
    """{região: {'detalhes': [(nome, img)], 'objetos': [(nome, img)]}}"""
    rnd = random.Random(11)
    comum = {'barril': barril(rnd), 'caixote': caixote(rnd), 'cerca': cerca(rnd), 'cerca_partida': cerca(rnd, partida=True),
             'placa': placa(rnd), 'fogueira_apagada': fogueira_apagada(rnd)}
    out = {}
    out[1] = {'detalhes': [('tronco_caido', tronco_caido(rnd, cobertura='musgo')), ('toco', toco(rnd, cogumelos='vermelho')), ('toco_2', toco(rnd)),
                           ('cogumelos', cogumelos(rnd)), ('cogumelos_castanhos', cogumelos(rnd, chapeu='castanho', pintas=False)),
                           ('erva_alta_1', erva_alta(rnd)), ('erva_alta_2', erva_alta(rnd, 'folha_esc', 18, 20)),
                           ('juncos', N.tufo(rnd, 14, 26, 'musgo', 8, False))],
              'objetos': list(comum.items()) + [('carroca', carroca(rnd)), ('pilar_partido', pilar(rnd)), ('menir', menir(rnd)),
                                                ('tenda', tenda(rnd))]}
    out[2] = {'detalhes': [('cristais_azuis', cristais(rnd, 'cristal_a')), ('cristais_rosa', cristais(rnd, 'cristal_r')),
                           ('cristais_verdes', cristais(rnd, 'cristal_v', 16, 18)), ('ossos', ossos(rnd)),
                           ('cogumelos_cave', cogumelos(rnd, chapeu='lilas', pintas=False))],
              'objetos': [('barril', comum['barril']), ('caixote', comum['caixote']), ('placa', comum['placa']),
                          ('fogueira_apagada', comum['fogueira_apagada']), ('pilar_partido', pilar(rnd, musgo=None))]}
    out[3] = {'detalhes': [('tronco_caido', tronco_caido(rnd, casca='tronco', cobertura='folha')), ('toco', toco(rnd, cogumelos='laranja')),
                           ('cogumelos', cogumelos(rnd, chapeu='laranja')), ('erva_alta', erva_alta(rnd, 'selva')),
                           ('juncos', N.tufo(rnd, 14, 26, 'musgo', 8, False))],
              'objetos': [('barril', comum['barril']), ('caixote', comum['caixote']), ('placa', comum['placa']),
                          ('pilar_musgo', pilar(rnd, rampa='verde_esc', musgo='folha')), ('menir', menir(rnd, rampa='verde_esc', runa='#30e1b9'))]}
    out[4] = {'detalhes': [('ossos', ossos(rnd)), ('cranio_grande', ossos(rnd, 30, 16)), ('erva_seca_alta', erva_alta(rnd, 'seco', 18, 18)),
                           ('anfora_partida', anfora(rnd, partida=True))],
              'objetos': [('anfora', anfora(rnd)), ('barril', comum['barril']), ('caixote', comum['caixote']),
                          ('pilar_areia', pilar(rnd, rampa='seco', musgo=None)), ('tenda_deserto', tenda(rnd, tecido='tecido_verm')),
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
    return out


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
