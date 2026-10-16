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


# ---------- corpo: o do herói (desenhado à mão), com as cores de cada NPC ----------
import heroi as H
from PIL import Image

_HEROI = {  # cor do herói -> (parte, índice na rampa)
    '#323353': ('roupa', 0), '#484a77': ('roupa', 1), '#4d65b4': ('roupa', 2), '#4d9be6': ('roupa', 3), '#8fd3ff': ('roupa', 4),
    '#6e2727': ('lenco', 0), '#b33831': ('lenco', 1), '#ea4f36': ('lenco', 2), '#f57d4a': ('lenco', 3),
    '#3e3546': ('calcas', 1), '#625565': ('calcas', 2), '#7f708a': ('calcas', 3),
    '#45293f': ('botas', 0), '#694f62': ('botas', 1), '#966c6c': ('botas', 2), '#ab947a': ('botas', 3),
    '#cd683d': ('pele', 1), '#e6904e': ('pele', 2), '#fca790': ('pele', 3), '#fdcbb0': ('pele', 4),
}


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _cores(estilo):
    r = {'roupa': _r(estilo.get('roupa', 'azul')), 'calcas': _r(estilo.get('calcas', 'cinza')),
         'botas': _r(estilo.get('botas', 'couro')), 'pele': PELES[estilo.get('pele', 'clara')]}
    r['lenco'] = _r(estilo['lenco']) if estilo.get('lenco') else r['roupa']
    return {_hex(h): _hex(r[parte][i]) for h, (parte, i) in _HEROI.items()}


def _recolorir(im, tabela):
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            c = px[x, y]
            if c[3] and c in tabela:
                px[x, y] = tabela[c]
    return im


def _grelha_px(im, pts, rampa, z_luz=True):
    """Pinta um conjunto de píxeis com sombra (claro em cima à esquerda) e contorno."""
    cores = _shade(pts, rampa)
    borda = {(x + vx, y + vy) for (x, y) in pts for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1))} - set(pts)
    for (x, y) in borda:
        if 0 <= x < T and 0 <= y < T:
            im.putpixel((x, y), _hex(OUT))
    for (x, y), c in cores.items():
        if 0 <= x < T and 0 <= y < T:
            im.putpixel((x, y), _hex(c))


def _boneco(estilo, d, pose):
    baixo = estilo.get('baixo', 0)
    cab = pose.get('cab', 0) + baixo
    tr = pose.get('tr', 0) + min(baixo, 3)
    sem = estilo.get('sem_braco')
    extra = {}
    if sem:
        if d == 'lado':
            extra['s'] = 'nenhum' if sem == 'd' else pose.get('s', 'meio')
        else:
            extra['f' if (sem == 'e') == (d == 'baixo') else 'o'] = 'nenhum'
    p = dict(pose, cab=cab, tr=tr, cabeca=False, lenco=bool(estilo.get('lenco')),
             k=min(2, max(0, tr - 1)), **extra)
    base = Image.new('RGBA', (T, T))
    if estilo.get('capa'):   # capa por trás do corpo
        x1, x2 = (10, 21) if d != 'lado' else (11, 16)
        _grelha_px(base, {(x, y) for x in range(x1, x2 + 1) for y in range(18 + tr, 29)}, _r(estilo['capa']))
    im = _recolorir(H.compor(d, **p), _cores(estilo))
    base.alpha_composite(im)
    im = base
    if estilo.get('saia'):
        q = 25 + tr
        pts = {(x, y) for y in range(q, 30) for x in range((11 if d != 'lado' else 12) - (y - q) // 2,
                                                          (21 if d != 'lado' else 20) + (y - q) // 2)}
        _grelha_px(im, pts, _r(estilo['saia']))
    if estilo.get('avental') and d == 'baixo':
        _grelha_px(im, {(x, y) for x in range(14, 18) for y in range(20 + tr, 28)}, _r(estilo['avental']))
    if estilo.get('cinto') and d != 'cima':
        c = _hex(_r(estilo['cinto'])[1])
        for x in range(12, 20):
            if im.getpixel((x, 23 + tr))[3] and im.getpixel((x, 23 + tr))[:3] != _hex(OUT)[:3]:
                im.putpixel((x, 23 + tr), c)
    # a cabeça do NPC (desenhada à mão, com penteado, barba e acessórios)
    dirc = {'baixo': 'frente', 'cima': 'costas', 'lado': 'lado'}[d]
    olhos = 'fechado' if pose.get('cara') == 'fechado' else 'normal'
    x0 = 10 if d == 'lado' else 9
    for (x, y), c in cabeca(estilo, dirc, olhos).items():
        X, Y = x + x0, y + 4 + cab
        if 0 <= X < T and 0 <= Y < T:
            im.putpixel((X, Y), _hex(c))
    if d == 'lado' and pose.get('s', 'meio') != 'nenhum' and sem != 'd':
        # o braço de cá passa à frente da cabeça/barba
        y, g = H.LADO_BRACO_EXTRA[p.get('s', 'meio')]
        braco = Image.new('RGBA', (T, T))
        H.carimbar(braco, g, H.X0, H.Y0 + y + tr)
        braco = _recolorir(braco, _cores(estilo))
        im.alpha_composite(braco)
    return im


PARADO = [dict(), dict(l=1), dict(cab=1, tr=1, l=2), dict(cab=1, tr=1, l=1)]
ANDAR_L = [dict(pl=pl, cab=s, tr=s, s=b, l=l) for pl, s, b, l in
           (('passo_a', 1, 'tras', 1), ('desce_a', 1, 'meio', 2), ('passa_a', 0, 'frente', 3),
            ('passo_b', 1, 'frente', 1), ('desce_b', 1, 'meio', 2), ('passa_b', 0, 'tras', 3))]
ANDAR_F = [dict(pf=pf, cab=s, tr=s) for pf, s in
           (('normal', 0), ('e', 0), ('e', -1), ('normal', 0), ('d', 0), ('d', -1))]


def frente(estilo, costas=False, **pose):
    return _boneco(estilo, 'cima' if costas else 'baixo', pose)


def lado(estilo, **pose):
    return _boneco(estilo, 'lado', pose)


def animacoes(estilo):
    A = {}
    for d in ('baixo', 'cima', 'lado'):
        A['parado_' + d] = [_boneco(estilo, d, p) for p in PARADO]
        A['andar_' + d] = [_boneco(estilo, d, p) for p in (ANDAR_L if d == 'lado' else ANDAR_F)]
    return A
