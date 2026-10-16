"""Bonecos humanos (NPCs) de 32x32: parado e andar, nas 3 direções.

Cada NPC é um ESTILO: penteado, barba, acessórios, cores (pele, cabelo, roupa, calças, botas), altura e largura.
As cabeças são montadas a partir de uma cabeça careca desenhada à mão + máscaras de cabelo/barba (também à mão);
a luz do cabelo é calculada (claro em cima à esquerda). O corpo usa o motor (como o herói).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, RAMPAS

T = 32
OUT = '#2e222f'
PELES = {
    'clara': ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#fdcbb0'],
    'morena': ['#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fca790'],
    'escura': ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e'],
    'palida': ['#9babb2', '#c7dcd0', '#fdcbb0', '#fdcbb0', '#ffffff'],
    'verde': ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
}
CABELOS = {
    'castanho': ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#e6904e'],
    'ruivo': ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fbb954'],
    'preto': ['#2e222f', '#2e222f', '#3e3546', '#484a77', '#625565'],
    'loiro': ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
    'branco': ['#625565', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
    'cinzento': ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'prateado': ['#484a77', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff'],
    'roxo': ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#eaaded'],
    'verde': ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'azul': ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
}

# ---------- cabeça careca (14x13), à mão: a = pele clara, b = pele média, c = sombra, e = olho, k = bochecha ----------
CARECA = {
    'frente': ["..............",
               "....aaaaaa....",
               "..aaaaaaaaab..",
               ".aaaaaaaaaabb.",
               ".aaaaaaaaaabb.",
               ".aaaaaaaaaabb.",
               ".baaaaaaaaabb.",
               ".bbaeaaaaeabb.",
               ".bbaeaaaaeabb.",
               ".bbkaaaaaakbb.",
               "..bbbaaaabbb..",
               "....cbbbbc....",
               ".............."],
    'costas': ["..............",
               "....aaaaaa....",
               "..aaaaaaaaab..",
               ".aaaaaaaaaabb.",
               ".aaaaaaaaaabb.",
               ".aaaaaaaaaabb.",
               ".baaaaaaaaabb.",
               ".bbaaaaaaaabb.",
               ".bbaaaaaaaabb.",
               ".bbbaaaaaabbb.",
               "..bbbbbbbbbb..",
               ".............",
               ".............."],
    'lado': ["..............",
             "...aaaaaaa....",
             ".aaaaaaaaaab..",
             ".aaaaaaaaaab..",
             ".aaaaaaaaaab..",
             ".aaaaaaaaaab..",
             ".baaaaaaaeab..",
             ".bbaaaaaaeaaa.",
             ".bbbbbaakaab..",
             ".bbbbbbaaab...",
             "..bbbbbbbc....",
             "..............",
             ".............."],
}

# ---------- penteados ('#' = cabelo), na mesma grelha 14x13 ----------
P_CURTO = {
    'frente': ["", "....######....", "..##########..", ".############.", ".############.", ".###..#..####.", ".##........##.",
               ".#..........#.", ".#..........#.", ".#..........#."],
    'costas': ["", "....######....", "..##########..", ".############.", ".############.", ".############.", ".############.",
               ".############.", ".############.", ".############.", "..##########.."],
    'lado': ["", "...#######....", ".############.", ".###########..", ".#######..##..", ".####.........", ".####.........",
             ".####.........", ".####.........", ".####.........", "..##.........."],
}


def _junta(base, extra):
    out = {}
    for d in ('frente', 'costas', 'lado'):
        a = list(base.get(d, [])) + [''] * 14
        b = list(extra.get(d, [])) + [''] * 14
        linhas = []
        for i in range(-1, 14):
            la = a[i] if i >= 0 else ''
            lb = b[i] if i >= 0 else ''
            la, lb = la.ljust(16, '.'), lb.ljust(16, '.')
            linhas.append(''.join('#' if (x == '#' or y == '#') else '.' for x, y in zip(la, lb)))
        out[d] = linhas[1:]
    return out


PENTEADOS = {
    'careca': {'frente': [], 'costas': [], 'lado': []},
    'curto': P_CURTO,
    'espetado': _junta(P_CURTO, {'frente': ["..#..#..#..#..", "..##########.."], 'costas': ["..#..#..#..#..", "..##########.."],
                                 'lado': ["#..#..#..#....", "..##########.."]}),
    'rabo': _junta(P_CURTO, {'costas': ["", "", "", "", "", "", "", "", "", "", "......##......", "......##......", ".....####....."],
                             'lado': ["", "", "", "", "#.............", "##............", "##............", "##............", "#..............."],
                             'frente': ["", "", "", "............##", "............##"]}),
    'comprido': _junta(P_CURTO, {'frente': ["", "", "", "", "", "", ".##........##.", ".##........##.", ".##........##.", ".##........##.",
                                            ".##........##.", ".##........##.", ".##........##."],
                                 'costas': ["", "", "", "", "", "", "", "", "", "", ".############.", ".############.", "..##########.."],
                                 'lado': ["", "", "", "", "", "", "", "", "", ".#####........", ".#####........", ".####.........", "..##.........."]}),
    'carrapito': _junta({'frente': ["", "....######....", "..##########..", ".############.", ".##........##.", ".#..........#."],
                         'costas': P_CURTO['costas'], 'lado': ["", "...#######....", ".############.", ".###########..", ".####.........",
                                                               ".####.........", ".###.........."]},
                        {'frente': ["....######....", ".....####....."], 'costas': ["....######....", ".....####....."],
                         'lado': ["..####........", ".#####........"]}),
    'tapado': _junta(P_CURTO, {'frente': ["", "", "", "", ".######..####.", ".######....##.", ".######.....#.", ".#####......#."],
                               'lado': ["", "", "", ".############.", ".##########...", ".####.........", ".####........."]}),
}

BARBAS = {
    'curta': {'frente': ["", "", "", "", "", "", "", "", "", ".#..........#.", "..###....###..", "...########...", ".....####....."],
              'lado': ["", "", "", "", "", "", "", "", ".....##.......", "....######....", "...#######....", ".....###......"]},
    'longa': {'frente': ["", "", "", "", "", "", "", "", "", ".#..........#.", "..##########..", "..##########..", "...########...",
                         "....######....", ".....####....."],
              'lado': ["", "", "", "", "", "", "", "", ".....###......", "....#######...", "....#######...", ".....#####....",
                       "......###....."]},
    'trancas': {'frente': ["", "", "", "", "", "", "", "", "", ".#..........#.", ".############.", ".############.", "..##########..",
                           "...##.##.##...", "...##.##.##..."],
                'lado': ["", "", "", "", "", "", "", "", "....####......", "...########...", "...########...", "....######....",
                         "....##.##....."]},
    'bigode': {'frente': ["", "", "", "", "", "", "", "", "", "", "...########...", "...#......#..."],
               'lado': ["", "", "", "", "", "", "", "", "", ".........####.", ".........#...."]},
}


def _shade(mascara, rampa):
    if not mascara:
        return {}
    xs = [p[0] for p in mascara]
    ys = [p[1] for p in mascara]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    w, h = max(1, (max(xs) - min(xs)) / 2), max(1, (max(ys) - min(ys)) / 2)
    out = {}
    for x, y in mascara:
        i = -0.6 * (x - cx) / w - 0.8 * (y - cy) / h
        if (x - 1, y) not in mascara or (x, y - 1) not in mascara:
            i += 0.3
        if (x + 1, y) not in mascara or (x, y + 1) not in mascara:
            i -= 0.5
        idx = 4 if i > 0.9 else 3 if i > 0.35 else 2 if i > -0.25 else 1 if i > -0.8 else 0
        out[(x, y)] = rampa[idx]
    return out


def _mascara(linhas, ox=0, oy=0):
    s = set()
    for y, l in enumerate(linhas):
        for x, ch in enumerate(l):
            if ch == '#':
                s.add((x + ox, y + oy))
    return s


def cabeca(estilo, direcao, olhos='normal'):
    """Devolve {(x,y): cor} da cabeça (com contorno), na grelha local (pode ir de -1 a 15)."""
    pele = PELES[estilo.get('pele', 'clara')]
    tom = {'a': pele[4], 'b': pele[3], 'c': pele[2], 'k': '#f68181', 'e': OUT}
    px = {}
    for y, l in enumerate(CARECA[direcao]):
        for x, ch in enumerate(l):
            if ch in tom:
                px[(x, y)] = tom[ch]
    if olhos == 'fechado':
        for (x, y), c in list(px.items()):
            if c == OUT and (x, y - 1) in px and px[(x, y - 1)] != OUT and (x, y + 1) in px and px.get((x, y + 1)) == OUT:
                px[(x, y)] = tom['a']
    if direcao == 'frente' and estilo.get('olhos_cor'):
        for (x, y), c in list(px.items()):
            if c == OUT and y == 8:
                px[(x, y)] = estilo['olhos_cor']
    pent = PENTEADOS[estilo.get('cabelo', 'curto')][direcao]
    cab = _shade(_mascara(pent), CABELOS[estilo.get('cor_cabelo', 'castanho')])
    px.update(cab)
    if estilo.get('barba') and direcao in BARBAS[estilo['barba']]:
        cor = estilo.get('cor_barba', estilo.get('cor_cabelo', 'castanho'))
        px.update(_shade(_mascara(BARBAS[estilo['barba']][direcao]), CABELOS[cor]))
    # acessórios
    for ac in estilo.get('acessorios', []):
        _acessorio(px, ac, direcao)
    # contorno de fora
    borda = set()
    for (x, y) in px:
        for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (x + vx, y + vy)
            if v not in px:
                borda.add(v)
    for v in borda:
        px[v] = OUT
    return px


def _acessorio(px, ac, d):
    nome = ac if isinstance(ac, str) else ac[0]
    cor = None if isinstance(ac, str) else ac[1]
    if nome == 'oculos' and d in ('frente', 'lado'):
        c = cor or '#9babb2'
        pts = [(3, 6), (4, 6), (5, 6), (3, 7), (5, 7), (8, 6), (9, 6), (10, 6), (8, 7), (10, 7), (6, 7), (7, 7)] if d == 'frente' else \
            [(8, 6), (9, 6), (10, 6), (8, 7), (10, 7), (11, 7)]
        for p in pts:
            px[p] = c
    elif nome == 'fita':
        c = cor or '#f9c22b'
        pts = {'frente': [(11, 2), (12, 2), (12, 3), (13, 1)], 'costas': [(2, 2), (1, 2), (1, 3), (0, 1)],
               'lado': [(3, 1), (2, 1), (2, 2), (1, 0)]}[d]
        for p in pts:
            px[p] = c
    elif nome in ('chapeu_pena', 'chapeu_palha'):
        rampa = RAMPAS['castanho'] if nome == 'chapeu_pena' else RAMPAS['amarelo']
        if cor:
            rampa = RAMPAS[cor]
        aba = 0 if nome == 'chapeu_pena' else 1
        copa = {(x, y) for x in range(3, 11) for y in range(-1, 3)}
        aba_px = {(x, 3) for x in range(-aba, 14 + aba)}
        px.update(_shade(copa | aba_px, rampa))
        if nome == 'chapeu_pena':
            for p in [(10, -2), (11, -3), (12, -4), (11, -2), (12, -3)]:
                px[p] = '#e83b3b'
        else:
            for p in [(4, 2), (6, 2), (8, 2)]:
                px[p] = '#ed8099'
    elif nome == 'capuz':
        rampa = RAMPAS[cor or 'preto']
        m = {(x, y) for x in range(0, 14) for y in range(0, 6)} | {(x, y) for x in (0, 1, 12, 13) for y in range(6, 11)}
        if d == 'costas':
            m |= {(x, y) for x in range(0, 14) for y in range(6, 11)}
        if d == 'lado':
            m = {(x, y) for x in range(0, 12) for y in range(0, 5)} | {(x, y) for x in range(0, 6) for y in range(5, 11)}
        m = {p for p in m if not (p[1] == 0 and (p[0] < 3 or p[0] > 10))}
        px.update(_shade(m, rampa))
    elif nome == 'lenco_cabeca':
        rampa = RAMPAS[cor or 'azul']
        m = {(x, y) for x in range(1, 13) for y in range(1, 5)}
        m -= {(1, 1), (2, 1), (11, 1), (12, 1)}
        if d == 'costas':
            m |= {(x, y) for x in range(2, 12) for y in range(5, 9)}
        if d == 'lado':
            m = {(x, y) for x in range(1, 12) for y in range(1, 5)} | {(x, y) for x in range(0, 4) for y in range(5, 9)}
        px.update(_shade(m, rampa))
    elif nome == 'orelha_elfo':
        pts = {'frente': [(0, 6), (-1, 5), (13, 6), (14, 5)], 'costas': [(0, 6), (-1, 5), (13, 6), (14, 5)], 'lado': [(5, 6), (4, 5), (3, 4)]}[d]
        for p in pts:
            px[p] = '#fca790'
    elif nome == 'oculos_testa':
        if d != 'costas':
            pts = [(3, 3), (4, 3), (5, 3), (8, 3), (9, 3), (10, 3)] if d == 'frente' else [(7, 3), (8, 3), (9, 3), (10, 3)]
            for p in pts:
                px[p] = cor or '#8fd3ff'
            for p in ([(2, 3), (6, 3), (7, 3), (11, 3)] if d == 'frente' else [(6, 3), (11, 3)]):
                px[p] = '#3e3546'
    elif nome == 'cicatriz' and d != 'costas':
        pts = [(9, 5), (10, 6), (9, 7), (10, 8)] if d == 'frente' else [(9, 5), (10, 6), (10, 8)]
        for p in pts:
            px[p] = '#cf657f'
    elif nome == 'sardas' and d == 'frente':
        for p in [(3, 9), (5, 9), (8, 9), (10, 9)]:
            px[p] = '#e6904e'
    elif nome == 'lapis' and d != 'frente':
        for p in ([(11, 0), (12, -1), (13, -2)] if d == 'costas' else [(2, 0), (1, -1), (0, -2)]):
            px[p] = '#f9c22b'
    elif nome == 'coroa':
        rampa = RAMPAS[cor or 'ouro']
        m = {(x, 0) for x in range(3, 11)} | {(3, -1), (6, -1), (7, -1), (10, -1), (6, -2), (7, -2)}
        px.update(_shade(m, rampa))


def _cab_parte(estilo, direcao, x0, y0, z, olhos='normal'):
    px = cabeca(estilo, direcao, olhos)
    pix = {(x + x0, y + y0): c for (x, y), c in px.items()}
    p = Parte(set(pix), None, z=z, separar=False)
    p.pixels = pix
    return p


def _r(nome):
    return RAMPAS[nome] if isinstance(nome, str) else nome


def frente(estilo, y=0, pe=(0, 0), pd=(0, 0), me=(0, 0), md=(0, 0), costas=False):
    P = []
    alt = estilo.get('baixo', 0)          # quantos píxeis mais baixo (crianças, anões)
    larg = estilo.get('largo', 0)         # tronco mais largo
    y += alt
    q = 24 + estilo.get('quadril', 0)
    perna = estilo.get('perna', 1.7)
    if estilo.get('saia'):
        P.append(Parte(poligono([(11 - larg, q - 2), (20 + larg, q - 2), (22 + larg, 28.5), (9 - larg, 28.5)]), _r(estilo['saia']), z=3.8))
    for x, (fx, fy) in ((13.5, pe), (18.5, pd)):
        P.append(Parte(capsula(x, q, x + fx, 28.2 + fy, perna), _r(estilo.get('calcas', 'cinza')), z=1, volume='cilindro_v'))
        bx = x + fx + (-0.6 if x < 16 else 0.6)
        P.append(Parte(elipse(bx, 29.6 + fy, 2.4, 1.9), _r(estilo.get('botas', 'couro')), z=2))
    if estilo.get('capa'):
        P.append(Parte(retangulo(9 - larg, 16 + y, 22 + larg, 27), _r(estilo['capa']), z=0.5, volume='cilindro_v'))
    P.append(Parte(retangulo(11 - larg, 16 + y, 20 + larg, q, canto=1), _r(estilo.get('roupa', 'azul')), z=4, volume='cilindro_v'))
    if estilo.get('cinto'):
        P.append(Parte(retangulo(11 - larg, q - 1, 20 + larg, q - 1), _r(estilo['cinto']), z=5, plano=True, separar=False))
    if estilo.get('avental') and not costas:
        P.append(Parte(retangulo(12 - larg, 19 + y, 19 + larg, min(28, q + 3)), _r(estilo['avental']), z=5.5, plano=True))
    bracos = (('e', me, 9.6 - larg), ('d', md, 22.4 + larg))
    for lado, (ox, oy), base in bracos:
        if lado == estilo.get('sem_braco'):
            continue
        ombro = (base + (0.3 if lado == 'e' else -0.3), 17.5 + y)
        mao = (base + ox, 22.0 + y + oy)
        rampa_braco = _r(estilo.get('braco_ferro', estilo.get('mangas', estilo.get('roupa', 'azul')))) if lado == estilo.get('lado_ferro') else _r(estilo.get('mangas', estilo.get('roupa', 'azul')))
        P.append(Parte(capsula(*ombro, *mao, 1.45 + estilo.get('bracos', 0)), rampa_braco, z=3, volume='cilindro_v'))
        P.append(Parte(elipse(mao[0], mao[1], 1.5, 1.4), PELES[estilo.get('pele', 'clara')], z=3.5))
    P.append(_cab_parte(estilo, 'costas' if costas else 'frente', 9, 4 + y, 9))
    if estilo.get('lenco'):
        P.append(Parte(elipse(16, 17.0 + y, 5.0 + larg, 1.5), _r(estilo['lenco']), z=12, separar=False))
    return desenhar(P, T, T)


def lado(estilo, y=0, pe=(0, 0), pd=(0, 0), me=(0, 0), md=(0, 0)):
    P = []
    alt = estilo.get('baixo', 0)
    larg = estilo.get('largo', 0)
    y += alt
    q = 24 + estilo.get('quadril', 0)
    perna = estilo.get('perna', 1.7)
    roupa = _r(estilo.get('roupa', 'azul'))
    mangas = _r(estilo.get('mangas', estilo.get('roupa', 'azul')))
    escuro = [roupa[0], roupa[0], roupa[1], roupa[2], roupa[2]]
    if estilo.get('capa'):
        P.append(Parte(retangulo(11 - larg, 16 + y, 15, 27), _r(estilo['capa']), z=0.2))
    ombro = (16, 17.5 + y)
    if estilo.get('sem_braco') != 'e':
        mao = (16 + me[0], 21.5 + y + me[1])
        P.append(Parte(capsula(*ombro, *mao, 1.3), escuro, z=0, volume='cilindro_v', brilho=False))
    calcas = _r(estilo.get('calcas', 'cinza'))
    for (fx, fy), zz, rampa in ((pe, 1, [calcas[0], calcas[0], calcas[1], calcas[2], calcas[3]]), (pd, 2, calcas)):
        P.append(Parte(capsula(16, q, 16 + fx, 28.2 + fy, perna), rampa, z=zz, volume='cilindro_v'))
        P.append(Parte(elipse(17.2 + fx, 29.6 + fy, 2.6, 1.9), _r(estilo.get('botas', 'couro')), z=zz + 0.5))
    if estilo.get('saia'):
        P.append(Parte(poligono([(13 - larg, q - 2), (19 + larg, q - 2), (21 + larg, 28.5), (11 - larg, 28.5)]), _r(estilo['saia']), z=3.8))
    P.append(Parte(retangulo(13 - larg, 16 + y, 19 + larg, q, canto=1), roupa, z=4, volume='cilindro_v'))
    if estilo.get('cinto'):
        P.append(Parte(retangulo(13 - larg, q - 1, 19 + larg, q - 1), _r(estilo['cinto']), z=5, plano=True, separar=False))
    if estilo.get('avental'):
        P.append(Parte(retangulo(18 + larg, 19 + y, 19 + larg, min(28, q + 3)), _r(estilo['avental']), z=5.5, plano=True))
    P.append(_cab_parte(estilo, 'lado', 10, 4 + y, 9))
    if estilo.get('lenco'):
        P.append(Parte(elipse(16, 17.0 + y, 4.2, 1.5), _r(estilo['lenco']), z=12, separar=False))
    if estilo.get('sem_braco') != 'd':
        mao = (16 + md[0], 22.0 + y + md[1])
        rampa = _r(estilo.get('braco_ferro')) if estilo.get('lado_ferro') == 'd' else mangas
        P.append(Parte(capsula(*ombro, *mao, 1.45 + estilo.get('bracos', 0)), rampa, z=13, volume='cilindro_v'))
        P.append(Parte(elipse(mao[0], mao[1], 1.5, 1.4), PELES[estilo.get('pele', 'clara')], z=13.5))
    return desenhar(P, T, T)


ANDAR_F = [dict(y=1), dict(pe=(0, -1), md=(0, -1)), dict(pe=(0, -2), md=(0, -1)), dict(y=1), dict(pd=(0, -1), me=(0, -1)), dict(pd=(0, -2), me=(0, -1))]
ANDAR_L = [dict(y=1, pd=(2, 0), pe=(-2, 0), md=(-1.2, 0), me=(1.2, 0)), dict(pd=(1, -1), pe=(-1, 0), md=(-0.6, 0), me=(0.6, 0)),
           dict(pd=(0, -2)), dict(y=1, pd=(-2, 0), pe=(2, 0), md=(1.2, 0), me=(-1.2, 0)), dict(pd=(-1, 0), pe=(1, -1), md=(0.6, 0), me=(-0.6, 0)),
           dict(pe=(0, -2))]


def animacoes(estilo):
    A = {}
    A['parado_baixo'] = [frente(estilo, y=b) for b in (0, 0, 1, 1)]
    A['parado_cima'] = [frente(estilo, y=b, costas=True) for b in (0, 0, 1, 1)]
    A['parado_lado'] = [lado(estilo, y=b) for b in (0, 0, 1, 1)]
    A['andar_baixo'] = [frente(estilo, **p) for p in ANDAR_F]
    A['andar_cima'] = [frente(estilo, costas=True, **p) for p in ANDAR_F]
    A['andar_lado'] = [lado(estilo, **p) for p in ANDAR_L]
    return A
