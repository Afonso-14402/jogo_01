"""Natureza dos andares em pixel art: texturas do chão (64x64, sem costuras) e plantas em sprite (árvores, arbustos,
erva e flores) para as 10 regiões. No jogo, as plantas ficam de frente para a câmara (como os bonecos) e abanam
com o vento (shader em scripts/mundo/natureza.gd); o chão mistura as texturas com bordas recortadas.

Estilo: o da referência Aranha-Mãe (luz de cima à esquerda, brilho forte, contorno #2e222f), 16 px = 1 m.
Saída: arte/regioes/<região>/natureza/*.png e dados/natureza.json (que plantas e que chão usa cada região).

Uso: python3 ferramentas/arte/natureza.py [--previa]
"""
import json
import math
import os
import random
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
import motor as M
from motor import Parte, elipse, capsula, poligono, desenhar, hexrgb

REGIOES = {1: 'r01_floresta', 2: 'r02_cavernas', 3: 'r03_pantano', 4: 'r04_deserto', 5: 'r05_gelo', 6: 'r06_oceano',
           7: 'r07_vulcao', 8: 'r08_reino_assombrado', 9: 'r09_ceu', 10: 'r10_abismo'}
T = 64   # lado das texturas do chão

R = M.RAMPAS   # as rampas novas ficam também no motor (as Partes procuram-nas lá)
R.update({
    'folha':      ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    'folha_esc':  ['#313638', '#165a4c', '#239063', '#1ebc73', '#91db69'],
    'pinho':      ['#313638', '#165a4c', '#239063', '#1ebc73', '#91db69'],
    'selva':      ['#313638', '#374e4a', '#547e64', '#239063', '#91db69'],
    'betula':     ['#3e3546', '#7f708a', '#c7dcd0', '#ffffff', '#ffffff'],
    'tronco':     ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a'],
    'palma':      ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'cacto':      ['#165a4c', '#239063', '#547e64', '#91db69', '#cddf6c'],
    'acacia':     ['#4c3e24', '#676633', '#a2a947', '#cddf6c', '#fbff86'],
    'seco':       ['#4c3e24', '#9e4539', '#cd683d', '#e6904e', '#fbb954'],
    'neve':       ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'],
    'alga':       ['#313638', '#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9'],
    'coral':      ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
    'pedra':      ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'queimado':   ['#2e222f', '#3e3546', '#45293f', '#625565', '#7f708a'],
    'negra':      ['#2e222f', '#45293f', '#6b3e75', '#905ea9', '#a884f3'],
    'nuvem':      ['#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'],
    'tronco_ceu': ['#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fbff86'],
    'luz':        ['#4d65b4', '#4d9be6', '#8fd3ff', '#c7dcd0', '#ffffff'],
    'noite':      ['#323353', '#484a77', '#4d65b4', '#905ea9', '#a884f3'],
})


def tom(rampa, i):
    return R[rampa][max(0, min(4, i))]


# ====================================================================================================================
# texturas do chão
# ====================================================================================================================

def ruido_ciclico(rnd, n=5, f_max=4):
    """Ruído suave que se repete a cada T píxeis (soma de ondas com frequências inteiras)."""
    ondas = [(rnd.randint(1, f_max), rnd.randint(-f_max, f_max), rnd.random() * 6.28, rnd.random()) for _ in range(n)]

    def f(x, y):
        v = sum(a * math.sin(6.2832 * (fx * x + fy * y) / T + ph) for fx, fy, ph, a in ondas)
        return v / sum(o[3] for o in ondas)
    return f


class Tela:
    def __init__(self, fundo):
        self.img = Image.new('RGB', (T, T), hexrgb(fundo))
        self.px = self.img.load()

    def p(self, x, y, cor):
        self.px[x % T, y % T] = hexrgb(cor)

    def g(self, x, y):
        return '#%02x%02x%02x' % self.px[x % T, y % T]


def base_manchas(tela, rnd, cores, n_ondas=6):
    """Fundo com manchas suaves (cores: do mais escuro para o mais claro). As cores das pontas (a mais escura e a
    mais clara) só aparecem nos extremos do ruído: manchas pequenas e raras; o meio fica calmo."""
    f = ruido_ciclico(rnd, n_ondas)
    k = len(cores)
    meio = cores[1:-1] or cores
    for y in range(T):
        for x in range(T):
            v = (f(x, y) + 1) / 2 + (rnd.random() - 0.5) * 0.04
            if v < 0.1:
                c = cores[0]
            elif v > 0.9:
                c = cores[-1]
            else:
                c = meio[max(0, min(len(meio) - 1, int((v - 0.1) / 0.8 * len(meio))))]
            tela.p(x, y, c)


def chao_erva(rnd, r, flores=None, seca=False):
    """r: 5 tons (escuro -> claro). Tufos em forma de V com a ponta clara e uma sombra por baixo."""
    t = Tela(r[2])
    base_manchas(t, rnd, [r[2], r[2], r[2], r[2], r[3]] if not seca else [r[1], r[2], r[2], r[3]])
    for _ in range(55):
        x, y = rnd.randrange(T), rnd.randrange(T)
        claro = r[3] if t.g(x, y) != r[3] else r[4]
        t.p(x, y + 1, r[1])
        t.p(x, y, claro)
        if rnd.random() < 0.6:
            t.p(x - 1, y - 1, claro)
            t.p(x + 1, y - 1, claro)
            t.p(x - 1, y, r[2])
        if rnd.random() < 0.3:
            t.p(x, y - 2, r[4])
    for _ in range(10):   # pontinhos escuros (terra entre a erva)
        x, y = rnd.randrange(T), rnd.randrange(T)
        t.p(x, y, r[0])
    for cor, centro in (flores or []):
        for _ in range(2):
            x, y = rnd.randrange(T), rnd.randrange(T)
            for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                t.p(x + dx, y + dy, cor)
            t.p(x, y, centro)
            t.p(x + 1, y + 1, r[0])
    return t.img


def chao_terra(rnd, r, pedras=None, n_pedras=14, torroes=60):
    """Terra batida: torrões com luz em cima à esquerda e pedrinhas com contorno."""
    t = Tela(r[2])
    base_manchas(t, rnd, [r[2], r[2], r[2], r[3]])
    torroes = torroes // 3
    n_pedras = max(3, n_pedras // 2)
    for _ in range(torroes):
        x, y = rnd.randrange(T), rnd.randrange(T)
        t.p(x, y, r[3])
        t.p(x + 1, y, r[3])
        t.p(x + 1, y + 1, r[1])
        t.p(x, y + 1, r[2])
    pr = pedras or R['pedra']
    for _ in range(n_pedras):
        x, y = rnd.randrange(T), rnd.randrange(T)
        w, h = rnd.choice([(2, 1), (2, 2), (3, 2), (1, 1)])
        for i in range(w):
            for j in range(h):
                t.p(x + i, y + j, pr[3] if (i == 0 and j == 0) else pr[2])
            t.p(x + i, y + h, r[0])
        t.p(x + w, y + h - 1, r[0])
    return t.img


def chao_lajes(rnd, r, juntas=None, n=11, musgo=None, brasas=None):
    """Lajes / calçada arrumadas em fiadas (como pedreiros a sério): cada pedra é um retângulo de cantos
    redondos, com aresta de cima-esquerda clara, de baixo-direita escura e junta escura à volta.
    n = quantas pedras numa textura (mais = pedras mais pequenas). Repete-se sem costuras."""
    t = Tela(juntas or r[0])
    junta = juntas or r[0]
    lado = max(6, int(T / math.sqrt(max(4, n)) + 0.5))   # tamanho médio de uma pedra
    redondas = n >= 40   # muitas pedras pequenas = calçada de pedras redondas (não tijolos)
    # alturas das fiadas que somam T
    alturas = []
    while sum(alturas) < T:
        alturas.append(max(4, lado - 2 + rnd.randint(-1, 2)))
    alturas[-1] -= sum(alturas) - T
    if alturas[-1] < 4:
        alturas[-2] += alturas.pop()
    dono = {}
    pedras = []
    y0 = 0
    for h in alturas:
        larguras = []
        while sum(larguras) < T:
            larguras.append(max(5, int(lado * (rnd.uniform(0.8, 1.15) if redondas else rnd.uniform(0.8, 1.5)))))
        larguras[-1] -= sum(larguras) - T
        if larguras[-1] < 5:
            larguras[-2] += larguras.pop()
        x0 = rnd.randrange(T)   # desencontro das juntas entre fiadas
        for w in larguras:
            pedras.append((x0, y0, w, h, rnd.choice([r[1], r[2], r[2], r[2], r[3]])))
            x0 += w
        y0 += h
    for i, (x0, y0, w, h, cor) in enumerate(pedras):
        for j in range(h - 1):            # 1 px de junta em baixo e à direita
            for k in range(w - 1):
                canto = (k in (0, w - 2)) and (j in (0, h - 2))
                if redondas:   # calçada: cantos bem redondos (2 px)
                    canto = canto or ((k in (0, 1, w - 3, w - 2)) and (j in (0, h - 2))) or \
                        ((k in (0, w - 2)) and (j in (0, 1, h - 3, h - 2)))
                if canto:
                    continue              # cantos redondos
                c = cor
                if j == 0 or k == 0:
                    c = r[3] if cor != r[3] else r[4]
                elif j == h - 2 or k == w - 2:
                    c = r[1] if cor != r[1] else r[0]
                elif rnd.random() < 0.03:
                    c = r[1]
                t.p(x0 + k, y0 + j, c)
                dono[((x0 + k) % T, (y0 + j) % T)] = i
    if musgo:   # musgo nas juntas
        for _ in range(30):
            x, y = rnd.randrange(T), rnd.randrange(T)
            if (x, y) not in dono:
                t.p(x, y, musgo[rnd.randrange(2)])
    if brasas:   # algumas juntas a brilhar (poucas: a pedra é que manda)
        for y in range(T):
            for x in range(T):
                if (x, y) not in dono and rnd.random() < 0.12:
                    t.p(x, y, rnd.choice(brasas))
    return t.img


def chao_gruta(rnd, r, cascalho=None, n_cascalho=34, rachas=7, lajes=3, brilhos=None, humido=False, rachas_cor=None):
    """Chão de gruta natural: rocha e terra escura com pouco contraste, cascalho com luz em cima à esquerda,
    rachas finas e algumas lajes lisas meio enterradas (para não parecer calçada)."""
    t = Tela(r[2])
    base_manchas(t, rnd, [r[1], r[2], r[2], r[2], r[2]], 7)
    rachas = (rachas + 1) // 3
    n_cascalho = n_cascalho // 2
    for _ in range(lajes * 2):   # pedras meio enterradas (3-5 px, redondas, luz em cima à esquerda)
        cx, cy = rnd.randrange(T), rnd.randrange(T)
        rx, ry = rnd.uniform(1.6, 2.8), rnd.uniform(1.2, 2.0)
        for y in range(-2, 3):
            for x in range(-3, 4):
                d = (x / rx) ** 2 + (y / ry) ** 2
                if d <= 1.0:
                    t.p(cx + x, cy + y, r[3] if (x + y < -1) else r[2] if d < 0.6 else r[1])
        t.p(cx + 1, cy + int(ry) + 1, r[0])
        t.p(cx, cy + int(ry) + 1, r[0])
    for _ in range(rachas):   # rachas finas que serpenteiam
        x, y = rnd.randrange(T), rnd.randrange(T)
        dx = rnd.choice([-1, 1])
        for k in range(rnd.randint(4, 10)):
            t.p(x, y, rachas_cor[k % len(rachas_cor)] if rachas_cor else r[0])
            t.p(x + 1, y, r[0] if rachas_cor else r[1])
            x += dx if rnd.random() < 0.6 else 0
            y += 1
    pr = cascalho or r
    for _ in range(n_cascalho):   # cascalho: pedrinhas de 1-3 px com luz e sombra
        x, y = rnd.randrange(T), rnd.randrange(T)
        w = rnd.choice([1, 1, 2, 2, 3])
        for i in range(w):
            t.p(x + i, y, pr[3] if i == 0 else pr[2])
        t.p(x, y - 1, pr[4] if w > 1 and rnd.random() < 0.5 else t.g(x, y - 1))
        for i in range(w):
            t.p(x + i, y + 1, r[0])
    if humido:   # poças pequenas e brilho de humidade
        for _ in range(4):
            cx, cy = rnd.randrange(T), rnd.randrange(T)
            for x in range(-2, 3):
                t.p(cx + x, cy, '#323353')
                if abs(x) < 2:
                    t.p(cx + x, cy + 1, '#323353')
            t.p(cx - 1, cy, '#4d65b4')
    for cor in (brilhos or []):   # esporos e pontinhos que brilham
        for _ in range(5):
            x, y = rnd.randrange(T), rnd.randrange(T)
            t.p(x, y, cor)
    return t.img


def chao_areia(rnd, r, conchas=None):
    """Areia: ondulações do vento (riscas onduladas claras com sombra) e grãos."""
    t = Tela(r[2])
    base_manchas(t, rnd, [r[2], r[2], r[2], r[3]], 4)
    for k in range(3):   # poucas ondulações, em bocados (não riscas de ponta a ponta)
        y0 = k * T // 3 + rnd.randrange(8)
        fase = rnd.random() * 6.28
        x0 = rnd.randrange(T)
        for x in range(x0, x0 + rnd.randint(20, 34)):
            y = y0 + int(round(2.0 * math.sin(6.2832 * x / T + fase)))
            t.p(x, y, r[3])
            t.p(x, y + 1, r[1])
    for _ in range(18):
        x, y = rnd.randrange(T), rnd.randrange(T)
        t.p(x, y, rnd.choice([r[4], r[1]]))
    for cor in (conchas or []):
        for _ in range(3):
            x, y = rnd.randrange(T), rnd.randrange(T)
            t.p(x, y, cor)
            t.p(x + 1, y, cor)
            t.p(x, y - 1, '#ffffff')
            t.p(x + 1, y + 1, r[0])
    return t.img


def chao_neve(rnd, r, gelo=False):
    """Neve: montinhos suaves (sombra azulada em baixo à direita) e brilhos."""
    t = Tela(r[2])
    base_manchas(t, rnd, [r[2], r[2], r[2], r[3]], 5)
    for _ in range(9):
        x, y = rnd.randrange(T), rnd.randrange(T)
        w = rnd.randint(3, 6)
        for i in range(w):
            t.p(x + i, y, r[4])
            t.p(x + i + 1, y + 1, r[1])
    for _ in range(8):
        x, y = rnd.randrange(T), rnd.randrange(T)
        t.p(x, y, '#ffffff')
    if gelo:
        for _ in range(3):
            x, y = rnd.randrange(T), rnd.randrange(T)
            for i in range(rnd.randint(4, 9)):
                t.p(x + i, y + (i // 3), '#8fd3ff')
                t.p(x + i, y + (i // 3) + 1, '#4d9be6')
    return t.img


def chao_tabuas(rnd, r):
    """Passadiço de tábuas (pântano)."""
    t = Tela(r[2])
    for y in range(T):
        for x in range(T):
            j = y % 8
            c = r[0] if j == 0 else (r[3] if j == 1 else (r[1] if j == 7 else r[2]))
            if rnd.random() < 0.06 and 1 < j < 7:
                c = r[1]
            t.p(x, y, c)
    for k in range(8):
        x = rnd.randrange(T)
        for j in range(1, 8):
            t.p(x, k * 8 + j, r[0])
        t.p(rnd.randrange(T), k * 8 + 4, r[0])   # pregos
    return t.img


def chao_estrelas(rnd, r):
    """Abismo: escuro com estrelas que parecem cair para longe."""
    t = Tela(r[0])
    base_manchas(t, rnd, [r[0], r[0], r[1]], 4)
    for _ in range(16):
        x, y = rnd.randrange(T), rnd.randrange(T)
        t.p(x, y, rnd.choice([r[3], r[4], '#a884f3']))
        if rnd.random() < 0.25:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                t.p(x + dx, y + dy, r[2])
    return t.img


def texturas_chao():
    """Quatro texturas por região: base, variante (manchas), terra (clareiras) e caminho."""
    rr = lambda *c: list(c)
    G = R['folha']
    terra = rr('#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0')
    pedra = R['pedra']
    out = {}
    rnd = random.Random(7)
    out[1] = {'base': chao_erva(rnd, G), 'variante': chao_erva(rnd, G, [('#f9c22b', '#fbff86'), ('#ffffff', '#f9c22b'), ('#ed8099', '#ffffff'), ('#4d9be6', '#ffffff')]),
              'terra': chao_terra(rnd, terra), 'caminho': chao_terra(rnd, rr('#694f62', '#966c6c', '#ab947a', '#ab947a', '#c7dcd0'), n_pedras=24, torroes=30)}
    gr = rr('#2e222f', '#313638', '#3e3546', '#625565', '#7f708a')
    out[2] = {'base': chao_gruta(rnd, gr, cascalho=rr('#2e222f', '#45293f', '#625565', '#7f708a', '#9babb2')),
              'variante': chao_gruta(rnd, rr('#2e222f', '#323353', '#3e3546', '#484a77', '#625565'), n_cascalho=14, lajes=1, humido=True,
                                     brilhos=['#30e1b9', '#8fd3ff']),
              'terra': chao_gruta(rnd, rr('#2e222f', '#45293f', '#625565', '#7f708a', '#9babb2'), n_cascalho=70, rachas=2, lajes=0),
              'caminho': chao_gruta(rnd, rr('#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a'), cascalho=gr, n_cascalho=40, rachas=0, lajes=2)}
    out[1]['calcada'] = chao_lajes(rnd, rr('#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'), n=52, musgo=['#547e64', '#92a984'])   # Ascendia (pedras pequenas)
    S = R['selva']
    out[3] = {'base': chao_erva(rnd, S), 'variante': chao_erva(rnd, rr('#313638', '#165a4c', '#374e4a', '#547e64', '#92a984'), [('#f57d4a', '#f9c22b')]),
              'terra': chao_terra(rnd, rr('#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'), pedras=R['verde_esc'], n_pedras=8),
              'caminho': chao_tabuas(rnd, R['palma'])}
    A = rr('#694f62', '#966c6c', '#ab947a', '#e6904e', '#fbb954')
    out[4] = {'base': chao_areia(rnd, rr('#cd683d', '#e6904e', '#fbb954', '#fdcbb0', '#fbff86')),   # areia clara ao sol
              'variante': chao_areia(rnd, rr('#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fdcbb0')),
              'terra': chao_terra(rnd, rr('#6e2727', '#9e4539', '#cd683d', '#e6904e', '#fbb954'), pedras=rr('#45293f', '#6e2727', '#9e4539', '#cd683d', '#e6904e')),
              'caminho': chao_lajes(rnd, rr('#9e4539', '#cd683d', '#e6904e', '#fbb954', '#fbff86'), n=10)}
    N = rr('#4d65b4', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff')
    out[5] = {'base': chao_neve(rnd, N), 'variante': chao_neve(rnd, N, gelo=True),
              'terra': chao_lajes(rnd, rr('#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff'), n=8),
              'caminho': chao_terra(rnd, rr('#625565', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff'), n_pedras=10)}
    B = rr('#cd683d', '#e6904e', '#fbb954', '#fdcbb0', '#ffffff')
    out[6] = {'base': chao_areia(rnd, B), 'variante': chao_areia(rnd, B, conchas=['#f04f78', '#ffffff', '#8fd3ff']),
              'terra': chao_areia(rnd, rr('#694f62', '#966c6c', '#ab947a', '#fca790', '#fdcbb0')),   # areia molhada
              'caminho': chao_tabuas(rnd, R['palma'])}
    V = rr('#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565')
    out[7] = {'base': chao_gruta(rnd, rr('#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565'), cascalho=rr('#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'),
                                 n_cascalho=40, rachas=9, brilhos=['#ea4f36', '#f79617', '#b33831']), 'variante': chao_gruta(rnd, rr('#2e222f', '#2e222f', '#3e3546', '#45293f', '#625565'), n_cascalho=20, rachas=12, lajes=1, brilhos=['#ea4f36', '#f79617'], rachas_cor=['#b33831', '#ea4f36', '#f79617', '#ea4f36']),
              'terra': chao_terra(rnd, rr('#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'), pedras=V),
              'caminho': chao_terra(rnd, rr('#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'), pedras=V)}
    out[8] = {'base': chao_erva(rnd, rr('#2e222f', '#313638', '#374e4a', '#676633', '#a2a947'), seca=True),
              'variante': chao_terra(rnd, rr('#2e222f', '#3e3546', '#4c3e24', '#694f62', '#966c6c'), pedras=pedra),
              'terra': chao_lajes(rnd, rr('#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2'), n=10, musgo=['#374e4a', '#547e64']),
              'caminho': chao_lajes(rnd, rr('#2e222f', '#625565', '#7f708a', '#9babb2', '#c7dcd0'), n=16)}
    out[9] = {'base': chao_erva(rnd, rr('#374e4a', '#547e64', '#92a984', '#b2ba90', '#ffffff'), [('#ffffff', '#8fd3ff'), ('#fbff86', '#ffffff')]),   # erva clara e fresca (lá em cima)
              'variante': chao_neve(rnd, rr('#8fd3ff', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff')),
              'terra': chao_lajes(rnd, rr('#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'), juntas='#f9c22b', n=6),
              'caminho': chao_lajes(rnd, rr('#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'), juntas='#9babb2', n=6)}
    E = rr('#2e222f', '#323353', '#484a77', '#c7dcd0', '#ffffff')
    out[10] = {'base': chao_estrelas(rnd, E), 'variante': chao_lajes(rnd, rr('#2e222f', '#323353', '#484a77', '#4d65b4', '#8fd3ff'), juntas='#2e222f', n=24),
               'terra': chao_estrelas(rnd, rr('#2e222f', '#45293f', '#6b3e75', '#a884f3', '#ffffff')),
               'caminho': chao_lajes(rnd, rr('#323353', '#484a77', '#4d65b4', '#8fd3ff', '#ffffff'), juntas='#a884f3', n=6)}
    return out


# ====================================================================================================================
# plantas (sprites)
# ====================================================================================================================

def textura_folhas(img, rampa, rnd, dens=0.07):
    """Pinceladas de folhas: pares claro/escuro espalhados no meio da copa (fica com ar de folhagem)."""
    r = [hexrgb(c) + (255,) for c in R[rampa]]
    px = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            c = px[x, y]
            if c[3] == 0 or rnd.random() > dens:
                continue
            if c == r[2] and px[x, y + 1] == r[2]:
                px[x, y] = r[3]
                px[x, y + 1] = r[1]
            elif c == r[3] and px[x + 1, y] == r[3]:
                px[x, y] = r[4]
            elif c == r[1] and px[x, y - 1] == r[1]:
                px[x, y] = r[0]
    return img


def tronco_partes(P, x, y0, y1, larg, rampa, z=5, raizes=True):
    P.append(Parte(poligono([(x - larg / 2, y1), (x + larg / 2, y1), (x + larg / 2 - 1, y0), (x - larg / 2 + 1, y0)]), rampa, z=z, volume='cilindro_v'))
    if raizes:
        P.append(Parte(poligono([(x - larg / 2 - 3, y1), (x - larg / 2 + 1, y1 - 5), (x - larg / 2 + 2, y1)]), rampa, z=z + 1, volume='cilindro_v'))
        P.append(Parte(poligono([(x + larg / 2 + 3, y1), (x + larg / 2 - 1, y1 - 5), (x + larg / 2 - 2, y1)]), rampa, z=z + 1, volume='cilindro_v'))


def massa_folhas(tufos, folhas, w, h, rnd, sombra_atras=True):
    """Copa como UMA massa com volume: luz geral de cima-esquerda (esfera grande) + volume de cada tufo,
    arestas de baixo-direita de cada tufo mais escuras (lobos), pinceladas de folhas. Devolve {(x, y): cor}."""
    r = R[folhas]
    dono = {}
    for k, (x, y, rr) in enumerate(tufos):
        for p in elipse(x, y, rr, rr * 0.9):
            dono[p] = k
    if not dono:
        return {}
    xs = [p[0] for p in dono]
    ys = [p[1] for p in dono]
    gx, gy = (min(xs) + max(xs) + 1) / 2, (min(ys) + max(ys) + 1) / 2
    grx, gry = (max(xs) - min(xs) + 1) / 2, (max(ys) - min(ys) + 1) / 2
    L = M.LUZ
    px = {}
    for (x, y), k in dono.items():
        tx, ty, tr = tufos[k]
        nx, ny = (x + .5 - tx) / tr, (y + .5 - ty) / (tr * 0.9)
        nz = math.sqrt(max(0.0, 1 - min(1.0, nx * nx + ny * ny)))
        loc = nx * L[0] + ny * L[1] + nz * L[2]
        Gx, Gy = (x + .5 - gx) / grx, (y + .5 - gy) / gry
        Gz = math.sqrt(max(0.0, 1 - min(1.0, Gx * Gx + Gy * Gy)))
        glo = Gx * L[0] + Gy * L[1] + Gz * L[2]
        i = 0.55 * glo + 0.6 * loc + (rnd.random() - 0.5) * 0.08
        c = r[4] if i > 0.95 else r[3] if i > 0.6 else r[2] if i > 0.22 else r[1] if i > -0.25 else r[0]
        # lobos: onde um tufo da frente acaba por cima de outro, fica uma linha escura (a sombra do tufo)
        for vx, vy in ((1, 0), (0, 1), (1, 1)):
            v = (x + vx, y + vy)
            if v in dono and dono[v] < k - 0 and dono[v] != k:
                pass
        px[(x, y)] = c
    for (x, y), k in dono.items():
        for vx, vy in ((0, 1), (1, 0)):
            v = (x + vx, y + vy)
            if v in dono and dono[v] != k and dono[v] < k:
                px[v] = r[1] if px[v] not in (r[0],) else r[0]
    return px


def copa(rnd, w, h, folhas, tronco, raio=(8, 12), n=14, topo=0.0, larg_tronco=7, frutos=None, achatada=False, galhos=True):
    """Árvore de copa redonda: tronco com raízes e galhos e uma copa feita de tufos que se sobrepõem."""
    P = []
    cx = w / 2
    base = h - 1
    alt_tronco = int(h * (0.36 if not achatada else 0.5))
    rx = w / 2 - raio[1] - 1
    topo_copa = raio[1] + 1 + topo
    fundo_copa = base - alt_tronco
    ccy = (topo_copa + fundo_copa) / 2 if not achatada else fundo_copa - raio[1]
    ry = (fundo_copa - topo_copa) / 2 if not achatada else raio[1] * 0.5
    tronco_partes(P, cx, ccy, base, larg_tronco, tronco, z=5)
    if galhos:
        for sx in (-1, 1):
            P.append(Parte(capsula(cx, fundo_copa + 4, cx + sx * rx * 0.55, fundo_copa - 4, 1.3), tronco, z=6, volume='cilindro_v'))
    tufos = []
    # tufos à volta da borda (silhueta com lobos) + alguns no meio
    for i in range(n):
        a = -math.pi / 2 + (i / n) * 6.2832 + rnd.uniform(-0.2, 0.2)
        tufos.append((cx + math.cos(a) * rx * rnd.uniform(0.75, 1.0), ccy + math.sin(a) * ry * rnd.uniform(0.75, 1.0), rnd.uniform(*raio)))
    for i in range(max(3, n // 3)):
        tufos.append((cx + rnd.uniform(-0.45, 0.45) * rx, ccy + rnd.uniform(-0.4, 0.4) * ry, raio[1] * rnd.uniform(1.0, 1.3)))
    # os de cima primeiro; os de baixo ficam por cima (a copa vê-se um pouco de baixo)
    tufos.sort(key=lambda t: t[1])
    img = desenhar(P, w, h, contorno_fora=False)
    px = img.load()
    for (x, y), c in massa_folhas(tufos, folhas, w, h, rnd).items():
        # os galhos de baixo espreitam por buracos na parte de baixo da copa
        if 0 <= x < w and 0 <= y < h:
            px[x, y] = hexrgb(c) + (255,)
    tapar_buracos(img, R[folhas][0])
    contorno(img)
    textura_folhas(img, folhas, rnd)
    if frutos:
        for _ in range(frutos[1]):
            for _t in range(40):
                x, y = rnd.randrange(2, w - 2), rnd.randrange(2, int(fundo_copa))
                if all(px[x + a, y + b][3] and px[x + a, y + b][:3] != hexrgb(M.OUT) for a in (-1, 0, 1, 2) for b in (-1, 0, 1, 2)):
                    px[x, y] = hexrgb(frutos[0]) + (255,)
                    px[x + 1, y] = hexrgb(frutos[0]) + (255,)
                    px[x, y + 1] = hexrgb(frutos[2]) + (255,)
                    px[x + 1, y + 1] = hexrgb(frutos[2]) + (255,)
                    px[x, y - 1] = hexrgb('#ffffff') + (255,)
                    break
    return img


def tapar_buracos(img, cor):
    """Buracos fechados no meio da copa ficam escuros (folhagem funda), em vez de transparentes."""
    px = img.load()
    w, h = img.size
    fora = set()
    pilha = [(x, y) for x in range(w) for y in (0, h - 1)] + [(x, y) for y in range(h) for x in (0, w - 1)]
    while pilha:
        x, y = pilha.pop()
        if (x, y) in fora or not (0 <= x < w and 0 <= y < h) or px[x, y][3]:
            continue
        fora.add((x, y))
        pilha += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for y in range(h):
        for x in range(w):
            if px[x, y][3] == 0 and (x, y) not in fora:
                px[x, y] = hexrgb(cor) + (255,)


def contorno(img):
    """Contorno escuro à volta de tudo (como no motor)."""
    px = img.load()
    w, h = img.size
    borda = []
    for y in range(h):
        for x in range(w):
            if px[x, y][3] == 0 and any(0 <= x + a < w and 0 <= y + b < h and px[x + a, y + b][3] and px[x + a, y + b][:3] != hexrgb(M.OUT)
                                        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                borda.append((x, y))
    for x, y in borda:
        px[x, y] = hexrgb(M.OUT) + (255,)
    return img


def pinheiro(rnd, w, h, folhas, tronco='tronco', camadas=5, neve=False):
    P = []
    cx = w / 2
    base = h - 1
    tronco_partes(P, cx, base - 14, base, 5, tronco, z=1, raizes=False)
    topo = 2
    fundo = base - 8
    for i in range(camadas):
        f = i / (camadas - 1)
        yb = fundo - (fundo - topo - 10) * f
        larg = (w / 2 - 1) * (1 - f * 0.72)
        alt = (fundo - topo) / camadas * 1.9
        yt = yb - alt
        pts = [(cx, max(topo, yt)), (cx + larg, yb), (cx + larg * 0.35, yb - 3), (cx, yb + 1), (cx - larg * 0.35, yb - 3), (cx - larg, yb)]
        P.append(Parte(poligono(pts), folhas, z=10 + i))
        if neve:
            m = {(x, y) for (x, y) in poligono(pts) if y < yt + (yb - yt) * 0.35 or (rnd.random() < 0.3 and y < yb - 2 and (x + y) % 3 == 0)}
            P.append(Parte(m, 'neve', z=10 + i, separar=False, plano=True))
    img = desenhar(P, w, h)
    return textura_folhas(img, folhas, rnd, 0.06)


def palmeira(rnd, w, h, folhas='folha', tronco='palma', curva=1, cocos=True):
    P = []
    base = h - 1
    topo_y = 27
    x0 = w / 2 - curva * 6
    pts = []
    n = 12
    for i in range(n + 1):
        f = i / n
        x = x0 + curva * 12 * f * f
        y = base - (base - topo_y) * f
        pts.append((x, y))
    for i in range(n):
        (xa, ya), (xb, yb) = pts[i], pts[i + 1]
        P.append(Parte(elipse((xa + xb) / 2, (ya + yb) / 2, 3.2 - i * 0.08, 3.4), tronco, z=i, volume='cilindro_v', luz=0.15 if i % 2 else -0.1))
    tx, ty = pts[-1]
    for k in range(7):
        ang = -2.9 + k * (2.6 / 6) + rnd.uniform(-0.12, 0.12)
        comp = rnd.uniform(18, 25)
        m = set()
        for s in range(18):
            f = s / 17
            x = tx + math.cos(ang) * comp * f
            y = ty + math.sin(ang) * comp * f + 14 * f * f   # caem com o peso
            r = 3.0 * (1 - f) + 1.0
            m |= elipse(x, y, r, r * 0.7)
        P.append(Parte(m, folhas, z=30 + (k % 3)))
    if cocos:
        for dx in (-2, 2, 0):
            P.append(Parte(elipse(tx + dx, ty + 4 - abs(dx) * 0.5, 2.2, 2.2), 'castanho', z=29))
    img = desenhar(P, w, h)
    return textura_folhas(img, folhas, rnd, 0.05)


def cacto(rnd, w, h, rampa='cacto', bracos=2, flor=True):
    P = []
    cx = w / 2
    base = h - 1
    P.append(Parte(capsula(cx, 6, cx, base, 4.5), rampa, z=10, volume='cilindro_v'))
    lados = [-1, 1] if bracos == 2 else [rnd.choice([-1, 1])]
    for s in lados:
        yb = rnd.randint(int(h * 0.45), int(h * 0.65))
        xb = cx + s * 9
        yt = yb - rnd.randint(9, 14)
        P.append(Parte(capsula(cx, yb, xb, yb, 2.8), rampa, z=8, volume='cilindro_v'))
        P.append(Parte(capsula(xb, yb, xb, yt, 3.0), rampa, z=9, volume='cilindro_v'))
        if flor:
            P.append(Parte(elipse(xb, yt - 3, 2, 1.6), 'rosa', z=12))
    if flor:
        P.append(Parte(elipse(cx, 3, 2.6, 2), 'rosa', z=12))
    img = desenhar(P, w, h)
    px = img.load()
    for y in range(4, h - 2, 3):   # espinhos
        for x in range(w):
            if px[x, y][3] and px[x, y][:3] == hexrgb(R[rampa][2]) and (x + y) % 4 == 0:
                px[x, y] = hexrgb('#ffffff') + (255,)
    return img


def morta(rnd, w, h, rampa, niveis=4, brasas=None, folhas=None, n_folhas=8):
    """Árvore sem folhas (negra, queimada, petrificada): galhos que se dividem para cima."""
    P = []
    base = h - 1
    galhos = []

    def ramo(x, y, ang, comp, larg, nivel):
        x2 = x + math.cos(ang) * comp
        y2 = y + math.sin(ang) * comp
        galhos.append((x, y, x2, y2, larg))
        if nivel <= 0:
            return
        for d in (-0.5, 0.45):
            ramo(x2, y2, ang + d + rnd.uniform(-0.25, 0.25), comp * rnd.uniform(0.62, 0.78), max(0.8, larg * 0.62), nivel - 1)
    ramo(w / 2, base, -math.pi / 2 + rnd.uniform(-0.1, 0.1), h * 0.36, 3.6, niveis)
    for i, (x1, y1, x2, y2, l) in enumerate(galhos):
        P.append(Parte(capsula(x1, y1, x2, y2, l), rampa, z=i, volume='cilindro_v', separar=False))
    P.append(Parte(poligono([(w / 2 - 7, base), (w / 2 - 1, base - 7), (w / 2 + 1, base - 7), (w / 2 + 7, base)]), rampa, z=0, volume='cilindro_v'))
    if folhas:
        for (x1, y1, x2, y2, l) in galhos[-n_folhas:]:
            P.append(Parte(elipse(x2, y2, 3, 2.5), folhas, z=99))
    img = desenhar(P, w, h)
    if brasas:
        px = img.load()
        for _ in range(16):
            x, y = rnd.randrange(w), rnd.randrange(h)
            if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                px[x, y] = hexrgb(rnd.choice(brasas)) + (255,)
    return img


def alga(rnd, w, h, rampa='alga', hastes=3):
    P = []
    base = h - 1
    for k in range(hastes):
        x0 = w / 2 + (k - (hastes - 1) / 2) * 6
        fase = rnd.random() * 6
        alt = rnd.uniform(0.7, 1.0) * (h - 4)
        ant = (x0, base)
        for s in range(1, 13):
            f = s / 12
            y = base - alt * f
            x = x0 + math.sin(f * 6 + fase) * 3
            P.append(Parte(capsula(ant[0], ant[1], x, y, 1.2), rampa, z=k * 20 + s, volume='cilindro_v', separar=False))
            if s % 2 == 0:
                sx = 1 if s % 4 == 0 else -1
                P.append(Parte(elipse(x + sx * 3, y, 3, 1.5), rampa, z=k * 20 + s))
            ant = (x, y)
    return desenhar(P, w, h)


def coral(rnd, w, h, rampa='coral'):
    P = []
    base = h - 1
    k = [0]

    def ramo(x, y, ang, comp, nivel):
        x2, y2 = x + math.cos(ang) * comp, y + math.sin(ang) * comp
        k[0] += 1
        P.append(Parte(capsula(x, y, x2, y2, 2.0), rampa, z=k[0], volume='cilindro_v', separar=False))
        if nivel <= 0:
            P.append(Parte(elipse(x2, y2, 2.4, 2.4), rampa, z=50 + k[0]))
            return
        for d in (-0.55, 0.5):
            ramo(x2, y2, ang + d, comp * 0.75, nivel - 1)
    ramo(w / 2, base, -math.pi / 2, h * 0.32, 3)
    return desenhar(P, w, h)


def arbusto(rnd, w, h, folhas, flores=None, n=7):
    P = []
    cx = w / 2
    base = h - 2
    tufos = []
    for i in range(n):
        x = cx + rnd.uniform(-w / 2 + 6, w / 2 - 6)
        y = base - rnd.uniform(4, h - 9)
        tufos.append((x, y, rnd.uniform(4.5, 6.5)))
    tufos.sort(key=lambda t: t[1])
    for i, (x, y, r) in enumerate(tufos):
        P.append(Parte(elipse(x, y, r, r * 0.85), folhas, z=i, luz=-0.25 if i < 2 else 0.0))
    P.append(Parte(elipse(cx, base - 4, w / 2 - 2, 5), folhas, z=50))
    img = desenhar(P, w, h)
    textura_folhas(img, folhas, rnd, 0.08)
    if flores:
        px = img.load()
        for _ in range(7):
            for _t in range(30):
                x, y = rnd.randrange(1, w - 1), rnd.randrange(1, h - 3)
                if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT) and px[x + 1, y][3] and px[x, y + 1][3]:
                    px[x, y] = hexrgb(flores[0]) + (255,)
                    px[x + 1, y] = hexrgb(flores[1]) + (255,)
                    px[x, y + 1] = hexrgb(flores[1]) + (255,)
                    break
    return img


def tufo(rnd, w, h, rampa, laminas=7, curvas=True):
    """Tufo de erva: lâminas finas em leque, mais claras na ponta."""
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    px = img.load()
    r = [hexrgb(c) + (255,) for c in R[rampa]]
    out = hexrgb(M.OUT) + (255,)
    cx = w / 2
    for i in range(laminas):
        ang = -math.pi / 2 + (i - (laminas - 1) / 2) * (1.6 / laminas) + rnd.uniform(-0.12, 0.12)
        comp = rnd.uniform(h * 0.55, h - 1)
        dobra = rnd.uniform(-0.4, 0.4) if curvas else 0
        for s in range(int(comp)):
            f = s / comp
            a = ang + dobra * f * f
            x = int(round(cx + math.cos(a) * s * 0.9 + (i - laminas / 2) * 0.6))
            y = int(round(h - 1 + math.sin(a) * s))
            if 0 <= x < w and 0 <= y < h:
                px[x, y] = r[1] if f < 0.3 else (r[2] if f < 0.65 else (r[3] if f < 0.9 else r[4]))
    # contorno só por baixo/lados (fica leve)
    pts = [(x, y) for y in range(h) for x in range(w) if px[x, y][3] and px[x, y] != out]
    for x, y in pts:
        for dx, dy in ((1, 0), (-1, 0)):
            if 0 <= x + dx < w and px[x + dx, y][3] == 0 and y > h * 0.5:
                px[x + dx, y] = out
    return img


def flor(rnd, w, h, petalas, centro='#f9c22b', caule='folha'):
    P = []
    cx = w // 2
    P.append(Parte({(cx, y) for y in range(4, h)}, caule, z=0, plano=True, separar=False))
    P.append(Parte({(cx + 1, h - 3), (cx + 2, h - 4), (cx - 1, h - 4), (cx - 2, h - 5)}, caule, z=1, plano=True, separar=False))
    m = {(cx + dx, 3 + dy) for dx, dy in ((0, -2), (-2, 0), (2, 0), (0, 2), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, -1), (-1, 0), (1, 0), (0, 1))}
    P.append(Parte(m, petalas, z=5))
    P.append(Parte({(cx, 3)}, None, z=6, cor=centro, separar=False))
    return desenhar(P, w, h)


def nenufar(rnd, w=18, h=9, flor=None, rampa='folha'):
    """Folha de nenúfar a boiar (vista de lado-cima: uma elipse com um corte), às vezes com flor."""
    m = elipse(w / 2, h / 2 + 1, w / 2 - 1, h / 2 - 1.2)
    corte = {(x, y) for (x, y) in m if x > w / 2 and abs(y - (h / 2 + 1)) < (x - w / 2) * 0.35}
    P = [Parte(m - corte, rampa, z=1, volume='cilindro_h')]
    if flor:
        P.append(Parte(elipse(w / 2 - 2, h / 2 - 0.5, 2.6, 2.2), flor, z=3))
        P.append(Parte({(int(w / 2 - 2), int(h / 2 - 1))}, None, z=4, cor='#f9c22b', separar=False))
    return desenhar(P, w, h + 2)


def cogumelo_luz(rnd, w, h, rampa='luz'):
    P = []
    for k, (dx, alt, r) in enumerate([(-3, 7, 3.5), (3, 10, 4.5), (0, 4, 2.5)]):
        x = w / 2 + dx
        P.append(Parte(capsula(x, h - 1, x, h - 1 - alt, 1.0), 'branco', z=k * 3, volume='cilindro_v'))
        P.append(Parte(elipse(x, h - 1 - alt, r, r * 0.6), rampa, z=k * 3 + 1))
    return desenhar(P, w, h)


def rocha(rnd, w, h, rampa, musgo=None, neve=False, brasas=None, cracas=None):
    """Rocha em pedaços (2-4 blocos facetados), luz de cima à esquerda, rachas e (às vezes) musgo/neve por cima."""
    P = []
    base = h - 1
    n = 1 if w < 16 else (2 if w < 32 else 3)
    blocos = []
    for i in range(n):
        bw = w * rnd.uniform(0.5, 0.75) if n > 1 else w - 3
        bh = h * rnd.uniform(0.65, 0.95) if n > 1 else h - 3
        bx = rnd.uniform(1 + bw / 2, w - 1 - bw / 2) if n > 1 else w / 2
        blocos.append((bx, bw, bh))
    blocos.sort(key=lambda b: -b[2])
    for i, (bx, bw, bh) in enumerate(blocos):
        topo = base - bh
        pts = [(bx - bw / 2, base), (bx - bw / 2 + rnd.uniform(0, 3), topo + bh * 0.35), (bx - bw * 0.15, topo + rnd.uniform(0, 2)),
               (bx + bw * 0.25, topo + rnd.uniform(0, 3)), (bx + bw / 2 - rnd.uniform(0, 2), topo + bh * 0.4), (bx + bw / 2, base)]
        P.append(Parte(poligono(pts), rampa, z=i * 2))
        if musgo or neve:
            m = {(x, y) for (x, y) in poligono(pts) if y < topo + bh * 0.22 + (1 if (x * 7) % 3 == 0 else 0)}
            P.append(Parte(m, musgo or 'neve', z=i * 2 + 1, separar=False))
    img = desenhar(P, w, h)
    px = img.load()
    r = R[rampa]
    for _ in range(max(1, w // 10)):   # rachas
        x, y = rnd.randrange(3, w - 3), rnd.randrange(h // 3, h - 3)
        for k in range(rnd.randint(2, 5)):
            if not (0 <= x < w - 1 and 0 <= y < h):
                break
            if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                px[x, y] = hexrgb(r[0]) + (255,)
                if px[x + 1, y][3] and px[x + 1, y][:3] != hexrgb(M.OUT):
                    px[x + 1, y] = hexrgb(r[3]) + (255,)
            x += rnd.choice([-1, 0, 1])
            y += 1
    for cor in (brasas or []) + (cracas or []):
        for _ in range(w // 8):
            x, y = rnd.randrange(w), rnd.randrange(h // 2, h)
            if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
                px[x, y] = hexrgb(cor) + (255,)
    return img


def cristais_grandes(rnd, rampa, w, h):
    """Um molho de cristais que enche a imagem (o do objetos.py tem tamanho fixo): o do meio alto, os outros à volta."""
    P = []
    k = h / 24.0
    for i, (dx, alt, larg, inc) in enumerate([(-0.22, 0.6, 0.12, -0.22), (0.24, 0.48, 0.11, 0.28), (0.0, 0.92, 0.16, 0.0),
                                               (0.36, 0.26, 0.08, 0.5), (-0.38, 0.3, 0.08, -0.45)]):
        x0 = w / 2 + dx * w
        a = alt * (h - 3)
        lg = max(2.0, larg * w)
        topo = (x0 + inc * a * 0.5, h - 2 - a)
        pts = [(x0 - lg, h - 2), (x0 - lg + inc * a * 0.4, h - 2 - a * 0.8), topo, (x0 + lg + inc * a * 0.4, h - 2 - a * 0.8), (x0 + lg, h - 2)]
        P.append(Parte(poligono(pts), rampa, z=(5 if i == 2 else i), plano=True))
    img = desenhar(P, w, h)
    px = img.load()
    for _ in range(int(3 * k)):   # brilhos
        x, y = rnd.randrange(w), rnd.randrange(h)
        if px[x, y][3] and px[x, y][:3] != hexrgb(M.OUT):
            px[x, y] = (255, 255, 255, 255)
    return img


def balao(rnd, w=40, h=78, cores=('vermelho', 'amarelo')):
    """Balão de ar quente preso ao chão (Região 9): a bola às riscas, as cordas e o cesto pousado."""
    P = []
    cx = w / 2
    cy, r = 17, 16
    bola = elipse(cx, cy, r, r) | poligono([(cx - r + 1, cy + 4), (cx + r - 1, cy + 4), (cx + 6, cy + 23), (cx - 6, cy + 23)])
    P.append(Parte(bola, cores[0], z=1))

    def meia(y):   # meia largura da bola nessa linha
        xs = [x for (x, yy) in bola if yy == y]
        return (max(xs) - min(xs)) / 2 + 0.5 if xs else 1

    riscas = {(x, y) for (x, y) in bola if int(((x - cx) / meia(y) + 1) * 2.5) % 2 == 1}
    P.append(Parte(riscas, cores[1], z=2, separar=False))
    base_bola = cy + 23
    cesto = h - 10
    P.append(Parte(poligono([(cx - 6, cesto), (cx + 6, cesto), (cx + 5, h - 2), (cx - 5, h - 2)]), 'madeira', z=3, plano=True))
    P.append(Parte({(int(cx) + dx, cesto + 1) for dx in range(-5, 6)}, None, z=4, cor='#4c3e24', separar=False))
    img = desenhar(P, w, h)
    px = img.load()
    corda = hexrgb('#694f62') + (255,)
    for x0, x1 in ((cx - 5, cx - 5), (cx + 4, cx + 4)):   # duas cordas finas, da bola ao cesto
        for y in range(base_bola + 1, cesto):
            x = int(round(x0 + (x1 - x0) * (y - base_bola) / max(1, cesto - base_bola)))
            if px[x, y][3] == 0:
                px[x, y] = corda
    return img


def rochas(rnd, rampa, **kw):
    """Grandes (paredes '##' e decoração) e pedrinhas soltas."""
    return ([('rocha_%d' % (i + 1), rocha(rnd, w, h, rampa, **kw)) for i, (w, h) in enumerate([(56, 44), (44, 34), (64, 52)])],
            [('pedra_%d' % (i + 1), rocha(rnd, w, h, rampa, **kw)) for i, (w, h) in enumerate([(10, 7), (14, 9), (8, 6)])])


def plantas():
    """{região: {grupo: [(nome, imagem), ...]}} — grupos: arvore, limite, mato, erva, flores."""
    rnd = random.Random(3)
    out = {}
    carvalhos = [('carvalho_1', copa(rnd, 80, 96, 'folha', 'tronco')),
                 ('carvalho_2', copa(rnd, 72, 88, 'folha', 'tronco', raio=(7, 11), n=12, frutos=('#ea4f36', 5, '#b33831'))),
                 ('carvalho_3', copa(rnd, 88, 104, 'folha_esc', 'tronco', raio=(9, 13), n=16))]
    pinhos = [('pinheiro_1', pinheiro(rnd, 52, 104, 'pinho')), ('pinheiro_2', pinheiro(rnd, 44, 84, 'pinho', camadas=4))]
    betula = ('betula', copa(rnd, 56, 96, 'folha', 'betula', raio=(6, 9), n=12, larg_tronco=5))
    out[1] = {'arvore': carvalhos + pinhos[:1] + [betula],
              'limite': carvalhos + pinhos,
              'mato': [('arbusto_1', arbusto(rnd, 36, 26, 'folha')), ('arbusto_flores', arbusto(rnd, 34, 24, 'folha', ('#ed8099', '#ffffff'))),
                       ('arbusto_bagas', arbusto(rnd, 30, 22, 'folha_esc', ('#4d65b4', '#8fd3ff')))],
              'erva': [('tufo_1', tufo(rnd, 14, 12, 'folha')), ('tufo_2', tufo(rnd, 12, 10, 'folha', 6)), ('tufo_3', tufo(rnd, 16, 14, 'folha', 9))],
              'flores': [('flor_amarela', flor(rnd, 7, 10, 'amarelo', '#ea4f36')), ('flor_branca', flor(rnd, 7, 9, 'branco')),
                         ('flor_rosa', flor(rnd, 7, 11, 'lilas', '#ffffff')), ('flor_azul', flor(rnd, 7, 9, 'azul', '#ffffff'))],
              'na_agua': [('nenufar_1', nenufar(rnd)), ('nenufar_flor_branca', nenufar(rnd, 16, 8, flor='branco'))]}
    import objetos as O   # (aqui dentro: o objetos.py também usa este ficheiro)
    out[2] = {'erva': [('musgo_gruta_1', tufo(rnd, 10, 6, 'verde_esc', 7)), ('musgo_gruta_2', tufo(rnd, 12, 7, 'agua', 8)),
                       ('liquen', tufo(rnd, 8, 5, 'cinza', 5, False))],
              'flores': [('cogumelo_luz_1', cogumelo_luz(rnd, 14, 14)), ('cogumelo_luz_2', cogumelo_luz(rnd, 14, 14, 'lilas')),
                         ('cogumelo_luz_3', cogumelo_luz(rnd, 12, 12, 'agua'))],
              'mato': [('estalagmite_1', O.estalagmite(rnd, 14, 30)), ('estalagmite_2', O.estalagmite(rnd, 18, 42)),
                       ('estalagmites_3', O.estalagmite(rnd, 30, 34, n=3))]}
    selva = [('selva_1', copa(rnd, 88, 112, 'selva', 'tronco', raio=(9, 13), n=16)),
             ('selva_2', copa(rnd, 76, 96, 'selva', 'tronco', raio=(8, 12), n=13, frutos=('#f79617', 4, '#9e4539')))]
    out[3] = {'arvore': selva + [('palmeira_selva', palmeira(rnd, 64, 96, 'selva')), ('mangue', copa(rnd, 72, 80, 'folha_esc', 'tronco', achatada=True, raio=(7, 10)))],
              'limite': selva,
              'mato': [('feto_1', palmeira(rnd, 40, 30, 'selva', 'tronco', 0, False)), ('arbusto_selva', arbusto(rnd, 36, 26, 'selva', ('#f57d4a', '#f9c22b')))],
              'erva': [('junco_1', tufo(rnd, 12, 22, 'musgo', 6, False)), ('tufo_selva', tufo(rnd, 14, 12, 'selva'))],
              'flores': [('flor_selva', flor(rnd, 7, 11, 'laranja', '#fbff86', 'selva'))],
              'na_agua': [('nenufar_1', nenufar(rnd)), ('nenufar_2', nenufar(rnd, 14, 7)), ('nenufar_flor', nenufar(rnd, flor='rosa')),
                       ('nenufar_flor_branca', nenufar(rnd, 16, 8, flor='branco'))]}
    out[4] = {'arvore': [('palmeira_1', palmeira(rnd, 64, 104)), ('palmeira_2', palmeira(rnd, 60, 92, curva=-1)),
                         ('acacia', copa(rnd, 96, 80, 'acacia', 'tronco', raio=(7, 10), n=14, achatada=True, larg_tronco=5)),
                         ('cacto_1', cacto(rnd, 32, 56)), ('cacto_2', cacto(rnd, 28, 44, bracos=1, flor=False))],
              'mato': [('cacto_pequeno', cacto(rnd, 18, 22, bracos=1)), ('arbusto_seco', morta(rnd, 32, 28, 'seco', 3))],
              'erva': [('erva_seca_1', tufo(rnd, 14, 12, 'seco')), ('erva_seca_2', tufo(rnd, 12, 10, 'acacia', 6))],
              'flores': [('flor_deserto', flor(rnd, 7, 9, 'rosa', '#fbff86', 'cacto'))]}
    neve = [('pinheiro_neve_1', pinheiro(rnd, 56, 108, 'pinho', neve=True)), ('pinheiro_neve_2', pinheiro(rnd, 46, 88, 'pinho', camadas=4, neve=True))]
    out[5] = {'arvore': neve, 'limite': neve,
              'mato': [('arbusto_neve', arbusto(rnd, 32, 22, 'pinho', ('#ea4f36', '#ffffff')))],
              'erva': [('tufo_neve', tufo(rnd, 12, 10, 'verde_esc', 6))],
              'flores': [('flor_de_neve', flor(rnd, 7, 9, 'branco', '#8fd3ff', 'pinho'))]}
    out[6] = {'arvore': [('palmeira_praia', palmeira(rnd, 64, 104)), ('alga_gigante', alga(rnd, 30, 72)), ('coral_grande', coral(rnd, 48, 48))],
              'mato': [('alga_pequena', alga(rnd, 18, 30, hastes=2))],
              'erva': [('alga_tufo', tufo(rnd, 12, 12, 'alga'))],
              'flores': [('coral_pequeno', coral(rnd, 18, 18)), ('coral_azul', coral(rnd, 16, 16, 'azul'))]}
    out[7] = {'arvore': [('arvore_petrificada', morta(rnd, 64, 88, 'pedra', 4)), ('tronco_queimado', morta(rnd, 56, 72, 'queimado', 3, brasas=['#ea4f36', '#f79617']))],
              'mato': [('arbusto_queimado', morta(rnd, 28, 24, 'queimado', 2, brasas=['#ea4f36']))],
              'erva': [('flor_cinza', flor(rnd, 7, 9, 'cinza', '#ea4f36', 'queimado'))],
              'flores': [('flor_brasa', flor(rnd, 7, 10, 'vermelho', '#f9c22b', 'queimado'))]}
    negras = [('arvore_negra_1', morta(rnd, 72, 96, 'negra', 4)), ('arvore_negra_2', morta(rnd, 64, 84, 'negra', 4, folhas='rosa'))]
    out[8] = {'arvore': negras, 'limite': negras[:1],
              'mato': [('arbusto_espinhos', morta(rnd, 30, 24, 'negra', 3))],
              'erva': [('tufo_morto', tufo(rnd, 12, 10, 'musgo', 6))],
              'flores': [('rosa_negra', flor(rnd, 7, 10, 'vermelho', '#2e222f', 'verde_esc'))]}
    nuvens = [('arvore_nuvem_1', copa(rnd, 80, 96, 'nuvem', 'tronco_ceu', raio=(9, 12))), ('arvore_nuvem_2', copa(rnd, 64, 80, 'nuvem', 'tronco_ceu', raio=(7, 10), n=11))]
    out[9] = {'arvore': nuvens, 'mato': [('arbusto_nuvem', arbusto(rnd, 32, 22, 'nuvem', ('#fbff86', '#f9c22b')))],
              'erva': [('tufo_celeste', tufo(rnd, 12, 10, 'verde'))],
              'flores': [('flor_do_vento', flor(rnd, 7, 11, 'azul', '#ffffff', 'verde'))]}
    out[10] = {}
    estilos = {1: ('pedra', {'musgo': 'musgo'}), 2: ('pedra', {}), 3: ('verde_esc', {'musgo': 'folha'}),
               4: ('seco', {}), 5: ('pedra', {'neve': True}), 6: ('castanho', {'musgo': 'alga', 'cracas': ['#ffffff']}),
               7: ('queimado', {'brasas': ['#ea4f36', '#f79617']}), 8: ('preto', {'musgo': 'verde_esc'})}
    for reg, (rampa, kw) in estilos.items():
        grandes, pequenas = rochas(rnd, rampa, **kw)
        out[reg]['rocha'] = grandes
        out[reg]['pedras'] = pequenas
    # (daqui para baixo com outro gerador: os desenhos de cima ficam iguais)
    rnd = random.Random(97)
    # Região 2: estalagmites altas e cristais grandes (em vez das peças 3D)
    altas = [('estalagmite_alta', O.estalagmite(rnd, 18, 50)), ('estalagmites_altas', O.estalagmite(rnd, 34, 54, n=3)),
             ('cristal_grande_azul', cristais_grandes(rnd, 'cristal_a', 30, 48)), ('cristal_grande_rosa', cristais_grandes(rnd, 'cristal_r', 26, 40))]
    out[2]['arvore'] = altas
    out[2]['limite'] = altas[:2]
    # Regiões 4–7: o que ainda eram peças 3D (as bordas do mapa e as peças gigantes)
    out[4]['limite'] = out[4]['rocha'] + out[4]['arvore'][:2]
    out[4]['gigante'] = [('cacto_gigante', cacto(rnd, 40, 76)), ('pilar_grande_areia', O.pilar(rnd, 24, 62, rampa='seco', musgo=None)),
                         ('rocha_gigante_deserto', rocha(rnd, 80, 60, 'seco'))]
    out[5]['gigante'] = [('bloco_gelo', cristais_grandes(rnd, 'cristal_a', 44, 56)), ('estaca_gelo', O.estalagmite(rnd, 22, 60, rampa='cristal_a'))]
    out[6]['gigante'] = [('coral_gigante', coral(rnd, 64, 60)), ('coral_gigante_azul', coral(rnd, 56, 52, 'azul')),
                         ('mastro_naufragio', O.tronco_caido(rnd, 76, 24, casca='palma', cobertura='alga'))]
    out[7]['limite'] = out[7]['rocha'] + out[7]['arvore'][:1]
    out[7]['gigante'] = [('rocha_vulcanica_gigante', rocha(rnd, 80, 62, 'queimado', brasas=['#ea4f36', '#f79617'])),
                         ('arvore_petrificada_grande', morta(rnd, 84, 108, 'pedra', 5))]
    # Região 9: rochas de mármore com relva por cima e veios de ouro, o balão e a coluna grande
    grandes, pequenas = rochas(rnd, 'branco', musgo='verde', brasas=['#f9c22b'])
    out[9]['rocha'] = grandes
    out[9]['pedras'] = pequenas
    out[9]['limite'] = nuvens
    out[9]['gigante'] = [('balao', balao(rnd)), ('balao_azul', balao(rnd, 36, 70, ('azul', 'branco'))),
                         ('coluna_grande', O.pilar(rnd, 22, 60, rampa='branco', partido=False, musgo=None))]
    # Região 10 (o Abismo): árvores negras com folhas de luz, copas da cor da noite com estrelas, cristais roxos
    vazio = [('arvore_luz', morta(rnd, 64, 88, 'preto', 4, folhas='luz', n_folhas=24)),
             ('arvore_estrelas', copa(rnd, 72, 88, 'noite', 'preto', raio=(8, 11), n=13, frutos=('#ffffff', 7, '#8fd3ff'))),
             ('arvore_luz_2', morta(rnd, 56, 76, 'preto', 3, folhas='lilas', n_folhas=14))]
    grandes, pequenas = rochas(rnd, 'preto', brasas=['#a884f3', '#eaaded'])
    out[10] = {'arvore': vazio, 'limite': vazio[:2],
               'mato': [('arbusto_noite', arbusto(rnd, 32, 22, 'noite', ('#ffffff', '#8fd3ff'))),
                        ('cristal_vazio', cristais_grandes(rnd, 'roxo', 22, 28))],
               'erva': [('tufo_noite', tufo(rnd, 10, 8, 'noite', 5))],
               'flores': [('lotus', flor(rnd, 7, 10, 'lilas', '#ffffff', 'noite')), ('flor_estrela', flor(rnd, 7, 9, 'luz', '#ffffff', 'noite'))],
               'rocha': grandes, 'pedras': pequenas,
               'gigante': [('arvore_luz_grande', morta(rnd, 88, 116, 'preto', 5, folhas='luz', n_folhas=48)),
                           ('cristal_gigante', cristais_grandes(rnd, 'roxo', 44, 68))]}
    return out


def main():
    previa = '--previa' in sys.argv
    indice = {}
    chaos = texturas_chao()
    todas = plantas()
    import objetos
    for r, grupos in objetos.por_regiao().items():
        todas.setdefault(r, {}).update(grupos)
    for r, nome in REGIOES.items():
        pasta = os.path.join('arte', 'regioes', nome, 'natureza')
        os.makedirs(pasta, exist_ok=True)
        ent = {'chao': {}, 'plantas': {}, 'fora': {6: 'agua', 9: 'nada', 10: 'nada'}.get(r, 'chao')}
        for k, img in chaos[r].items():
            img.save(os.path.join(pasta, f'chao_{k}.png'))
            ent['chao'][k] = f'res://arte/regioes/{nome}/natureza/chao_{k}.png'
        for grupo, lista in todas.get(r, {}).items():
            ent['plantas'][grupo] = []
            for n, img in lista:
                img.save(os.path.join(pasta, f'{n}.png'))
                ent['plantas'][grupo].append(f'res://arte/regioes/{nome}/natureza/{n}.png')
        # cenários: grupos de peças com posição (m) e raio de colisão; o nome da peça vira o caminho do PNG
        nomes = {n for lista in todas.get(r, {}).values() for n, _ in lista}
        ent['cenarios'] = []
        for nome_c, pecas in objetos.CENARIOS.get(r, []):
            falta = [p[0] for p in pecas if p[0] not in nomes]
            if falta:
                raise SystemExit('cenário %s (região %d): peças que não existem: %s' % (nome_c, r, falta))
            ent['cenarios'].append({'nome': nome_c, 'pecas': [[f'res://arte/regioes/{nome}/natureza/{p[0]}.png'] + p[1:] for p in pecas]})
        # temas de cada andar desta região (peças a mais, em molhos)
        ent['andares'] = {}
        for andar, lista in objetos.TEMAS.items():
            if (andar - 1) // 10 + 1 != r:
                continue
            falta = [p[0] for p in lista if p[0] not in nomes]
            if falta:
                raise SystemExit('tema do andar %d: peças que não existem: %s' % (andar, falta))
            ent['andares'][str(andar)] = [[f'res://arte/regioes/{nome}/natureza/{p[0]}.png', p[1]] for p in lista]
        indice[str(r)] = ent
    os.makedirs(os.path.join('arte', 'efeitos'), exist_ok=True)
    objetos.chama().save(os.path.join('arte', 'efeitos', 'fogueira_chama.png'))   # 6 frames de 20x26
    with open(os.path.join('dados', 'natureza.json'), 'w', encoding='utf-8') as f:
        json.dump(indice, f, ensure_ascii=False, indent=1)
    if previa:
        fazer_previa(chaos, todas)
    print('natureza: %d regiões' % len(indice))


def fazer_previa(chaos, todas, pasta=None):
    pasta = pasta or os.environ.get('PREVIA', '.')
    for r in REGIOES:
        sprites = [img for g in ('arvore', 'limite', 'mato', 'erva', 'flores', 'rocha', 'pedras', 'detalhes', 'objetos') for _, img in todas.get(r, {}).get(g, [])]
        vistos = []
        for s in sprites:
            if all(s is not v for v in vistos):
                vistos.append(s)
        chao = chaos[r]['base']
        W = 4 * T * 2
        alt = max([s.height for s in vistos] + [0]) + 8
        im = Image.new('RGB', (W, T * 2 + alt), (50, 51, 83))
        for i, k in enumerate(('base', 'variante', 'terra', 'caminho')):
            im.paste(chaos[r][k].resize((T, T)), (i * T, 0))
            im.paste(chaos[r][k], (i * T, T))
        x = 4
        for s in vistos:
            if x + s.width > W:
                break
            fundo = Image.new('RGBA', s.size)
            for yy in range(0, s.height, T):
                for xx in range(0, s.width, T):
                    fundo.paste(chao, (xx, yy))
            im.paste(s, (x, T * 2 + alt - s.height - 4), s)
            x += s.width + 4
        im = im.resize((im.width * 3, im.height * 3), Image.NEAREST)
        im.save(os.path.join(pasta, f'natureza_r{r:02d}.png'))


if __name__ == '__main__':
    main()
