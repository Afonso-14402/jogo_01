"""Guardiões (8), mini-boss Javali-Rei, boss Ent Ancião e boss da masmorra Larva Ancestral da Região 1.
Fichas: docs/regioes/r01_floresta.md (secções 6 e 9) e docs/BOSSES.md (secções 1 e 2).
Saída: arte/regioes/r01_floresta/guardioes/ e .../bosses/.

Uso: python3 ferramentas/arte/guardioes_r01.py
"""
import os
import sys
import random
sys.path.insert(0, os.path.dirname(__file__))
from motor import (Parte, elipse, retangulo, capsula, poligono, desenhar, deitar, dissolver, estrelas, guardar)

BASE = os.path.join('arte', 'regioes', 'r01_floresta')
OLHO = '#2e222f'
BRANCO = '#ffffff'
MAD = ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a']
PEDRA = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']


def ponto(P, x, y, cor, z=40):
    P.append(Parte({(int(x), int(y))}, None, z=z, separar=False, cor=cor))


def quad(P, x, y, w, h, cor, z=40):
    P.append(Parte(retangulo(int(x), int(y), int(x) + w - 1, int(y) + h - 1), None, z=z, separar=False, cor=cor))


def xis(P, x, y, z=40):
    x, y = int(x), int(y)
    P.append(Parte({(x - 1, y - 1), (x + 1, y - 1), (x, y), (x - 1, y + 1), (x + 1, y + 1)}, None, z=z, separar=False, cor=OLHO))


def morte(dano, ultima):
    return [dano, deitar(ultima), dissolver(deitar(ultima), 0.45), dissolver(deitar(ultima), 0.8)]


def faiscas(P, cx, cy, raio, semente, cor='#fbff86', n=8):
    rnd = random.Random(semente)
    pts = {(int(cx + rnd.uniform(-raio, raio)), int(cy + rnd.uniform(-raio * .6, raio * .6))) for _ in range(n)}
    P.append(Parte(pts, None, z=60, separar=False, cor=cor))


# ================= 1. Coelho-Chifre Ancião (48) =================

def coelho_anciao(dx=0, dy=0, orelha=0, cab=(0, 0), cara='normal', salto=False, est=None):
    P = []
    hx, hy = 31 + dx + cab[0], 27 + dy + cab[1]
    P.append(Parte(elipse(21 + dx, 35 + dy, 10, 7), 'cinza', z=2))
    P.append(Parte(elipse(11.5 + dx, 32 + dy, 2.5, 2.5), 'branco', z=1))
    if salto:
        P.append(Parte(capsula(15 + dx, 39 + dy, 9 + dx, 41 + dy, 2.4), 'cinza', z=3))
        P.append(Parte(capsula(27 + dx, 39 + dy, 32 + dx, 41 + dy, 1.9), 'cinza', z=3))
    else:
        P.append(Parte(capsula(16 + dx, 39 + dy, 14 + dx, 43.5, 2.5), 'cinza', z=3))
        P.append(Parte(capsula(27 + dx, 39 + dy, 28 + dx, 43.5, 1.9), 'cinza', z=3))
    P.append(Parte(capsula(hx - 4, hy - 4, hx - 8 + orelha, hy - 15, 1.8), 'cinza', z=1.5))
    P.append(Parte(capsula(hx - 1, hy - 4, hx - 1 + orelha * 1.5, hy - 15.5, 1.8), 'cinza', z=4))
    P.append(Parte(elipse(hx, hy, 6, 5.2), 'cinza', z=5))
    P.append(Parte(poligono([(hx + 1.5, hy - 4), (hx + 4.5, hy - 4.2), (hx + 4, hy - 9), (hx + 3, hy - 8), (hx + 2.5, hy - 9.5)]), 'branco', z=6))
    ponto(P, hx + 6, hy + 1, '#f68181')
    for (a, b) in ((18, 31), (19, 32), (20, 33), (24, 30), (25, 31)):
        ponto(P, a + dx, b + dy, '#c7dcd0', z=20)
    if cara == 'x':
        xis(P, hx + 2, hy - 1)
    else:
        quad(P, hx + 2, hy - 2, 1, 2, '#e83b3b' if cara == 'furia' else OLHO)
    if est is not None:
        estrelas(P, hx, hy - 12, est)
    return desenhar(P, 48, 48)


def anims_coelho_anciao():
    f = coelho_anciao
    A = {'parado': [f(), f(orelha=1), f(dy=1), f(orelha=-1)],
         'mover': [f(), f(dy=-3, salto=True, orelha=-1), f(dx=1, dy=-4, salto=True, orelha=-2), f(dx=1, dy=-1)],
         'atacar': [f(cab=(1, 4), orelha=-2, cara='furia'), f(dx=-1, cab=(1, 4), orelha=-2, cara='furia'), f(dx=4, cab=(2, 3), salto=True, orelha=-3), f(dx=2)],
         'dano': [f(dx=-1, cara='x', orelha=2)]}
    # ataque_1 Salto Esmagador · ataque_2 Chifrada tripla · ataque_3 Bater o pé (chama coelhos)
    A['ataque_1'] = [f(dy=2, cara='furia'), f(dy=-6, salto=True, orelha=-2), f(dy=-8, salto=True, orelha=-3), f(dy=1, cara='furia', orelha=2), f()]
    A['ataque_2'] = [f(cab=(1, 4), cara='furia'), f(dx=3, cab=(2, 3), salto=True), f(cab=(1, 4), cara='furia'), f(dx=3, cab=(2, 3), salto=True),
                     f(cab=(1, 4), cara='furia'), f(dx=4, cab=(2, 3), salto=True)]
    A['ataque_3'] = [f(), f(dy=-2, salto=True, cara='furia'), f(dy=1, cara='furia', orelha=2), f(dy=1, cara='furia', orelha=2)]
    A['morrer'] = morte(f(dx=-1, cara='x', orelha=2), f(cara='x'))
    return A


# ================= 2. Coruja Sombria (48) =================

CORUJA = ['#2e222f', '#2e222f', '#45293f', '#6b3e75', '#905ea9']


def coruja(dy=0, asa=0, dx=0, cara='normal', mergulho=0, penas=0):
    P = []
    cx, cy = 24 + dx, 24 + dy
    up = {0: (-14, -10), 1: (-14, 2), 2: (-10, 8)}[asa]
    P.append(Parte(poligono([(cx - 3, cy - 4), (cx + up[0], cy + up[1]), (cx - 6, cy + 8)]), CORUJA, z=1))
    P.append(Parte(elipse(cx, cy + 2 + mergulho, 8, 10 - mergulho), CORUJA, z=2))
    P.append(Parte(elipse(cx + 1, cy + 5, 5, 6), ['#45293f', '#6b3e75', '#905ea9', '#a884f3', '#a884f3'], z=3, brilho=False))
    P.append(Parte(poligono([(cx - 6, cy - 6), (cx - 5, cy - 12), (cx - 2, cy - 8), (cx + 2, cy - 8), (cx + 5, cy - 12), (cx + 6, cy - 6)]), CORUJA, z=4))
    P.append(Parte(elipse(cx, cy - 4, 7, 5.5), CORUJA, z=4.5))
    for ex in (-3, 3):
        P.append(Parte(elipse(cx + ex, cy - 4, 2.6, 2.6), 'amarelo', z=5, plano=True))
        if cara == 'x':
            xis(P, cx + ex, cy - 4)
        else:
            quad(P, cx + ex, cy - 4, 1, 2 if cara == 'normal' else 1, OLHO)
    P.append(Parte(poligono([(cx - 1, cy - 2), (cx + 1, cy - 2), (cx, cy + 1)]), 'laranja', z=6))
    P.append(Parte(poligono([(cx + 3, cy - 4), (cx - up[0], cy + up[1]), (cx + 6, cy + 8)]), CORUJA, z=7))
    for tx in (-3, 2):
        P.append(Parte(capsula(cx + tx, cy + 11, cx + tx, cy + 14, 1.0), 'laranja', z=1.5))
    for i in range(penas):
        P.append(Parte(poligono([(cx + 10 + i * 4, cy - 6 + i * 4), (cx + 13 + i * 4, cy - 5 + i * 4), (cx + 11 + i * 4, cy - 3 + i * 4)]), CORUJA, z=20))
    return desenhar(P, 48, 48)


def anims_coruja():
    f = coruja
    A = {'parado': [f(asa=0), f(asa=1, dy=1), f(asa=2, dy=2), f(asa=1, dy=1)],
         'mover': [f(asa=0, dx=0), f(asa=1, dx=1), f(asa=2, dx=2, dy=1), f(asa=1, dx=1)],
         'atacar': [f(asa=0, dy=-2), f(asa=0, dy=-3, mergulho=3, dx=2), f(asa=2, dy=4, mergulho=3, dx=4), f(asa=1)],
         'dano': [f(asa=2, cara='x', dx=-1)]}
    A['ataque_1'] = A['atacar']
    A['ataque_2'] = [f(asa=0, cara='fechado'), f(asa=0, dy=-1, cara='normal'), f(asa=0, dy=-1), f(asa=1)]
    A['ataque_3'] = [f(asa=0), f(asa=2, penas=1), f(asa=0, penas=2), f(asa=2, penas=3), f(asa=1)]
    A['morrer'] = morte(f(asa=2, cara='x'), f(asa=2, cara='x'))
    return A


# ================= 3. Lagostim Couraçado (48) =================

LAG = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']


def lagostim(dx=0, dy=0, pinca=0, cara='normal', fechado=False, jato=0, a=0):
    P = []
    cx, cy = 22 + dx, 32 + dy
    for i in range(3):
        P.append(Parte(capsula(cx - 4 + i * 4, cy + 4, cx - 6 + i * 4 + (a if i % 2 else -a), cy + 11, 0.9), LAG, z=0))
    P.append(Parte(poligono([(cx - 16, cy - 4), (cx - 20, cy - 8), (cx - 21, cy), (cx - 20, cy + 6), (cx - 16, cy + 3)]), LAG, z=1))
    for i, r in enumerate((3.5, 4, 4.6)):
        P.append(Parte(elipse(cx - 13 + i * 3.5, cy, r, r), LAG, z=1.5 + i * .1))
    P.append(Parte(elipse(cx + 2, cy - 1, 9, 6.5), LAG, z=2))
    P.append(Parte(capsula(cx + 9, cy - 5, cx + 13, cy - 10, 0.8), LAG, z=2.5))
    ponto(P, cx + 13, cy - 11, OLHO, 30)
    if not fechado:
        if cara == 'x':
            xis(P, cx + 9, cy - 4)
        else:
            quad(P, cx + 9, cy - 4, 1, 2, OLHO)
    ang = pinca
    braco = [(cx + 6, cy + 2), (cx + 13, cy + 1 - ang)]
    P.append(Parte(capsula(*braco[0], *braco[1], 2.0), LAG, z=3))
    px, py = braco[1]
    if fechado:
        P.append(Parte(elipse(cx + 8, cy - 4, 7, 6), LAG, z=6))
        P.append(Parte(elipse(cx + 2, cy - 2, 7, 6), LAG, z=5))
    else:
        P.append(Parte(poligono([(px - 1, py - 3), (px + 9, py - 6 - ang), (px + 10, py - 2 - ang), (px + 3, py)]), LAG, z=4))
        P.append(Parte(poligono([(px - 1, py + 1), (px + 9, py + 4), (px + 8, py + 6), (px, py + 4)]), LAG, z=4))
    if jato:
        for i in range(jato):
            P.append(Parte(elipse(cx + 16 + i * 6, cy - 6, 2.5, 1.6), 'agua', z=20))
    return desenhar(P, 48, 48)


def anims_lagostim():
    f = lagostim
    A = {'parado': [f(), f(pinca=1), f(dy=1, pinca=1), f()],
         'mover': [f(a=1), f(dx=1, a=-1), f(dx=2, a=1), f(dx=1, a=-1)],
         'atacar': [f(pinca=3), f(pinca=4, dx=-1), f(pinca=-2, dx=3), f()],
         'dano': [f(dx=-1, cara='x')]}
    A['ataque_1'] = [f(pinca=3), f(pinca=-2, dx=3), f(pinca=3, dx=1), f(pinca=-2, dx=3), f()]
    A['ataque_2'] = [f(dy=1), f(jato=1), f(jato=2), f(jato=3), f()]
    A['ataque_3'] = [f(), f(fechado=True, dy=1), f(fechado=True, dy=1), f()]
    A['morrer'] = morte(f(dx=-1, cara='x'), f(cara='x'))
    return A


# ================= 4. Rainha dos Esporos (64) =================

def rainha_esporos(dy=0, inchar=0, cara='normal', braco=0, esporos=0, salto=0):
    P = []
    cx = 32
    base = 60
    P.append(Parte(poligono([(cx - 13, base - 2 + dy), (cx - 8, base - 22 + dy), (cx + 8, base - 22 + dy), (cx + 13, base - 2 + dy)]), 'lilas', z=1))
    for i in range(-10, 12, 4):
        P.append(Parte(capsula(cx + i * .6, base - 20 + dy, cx + i, base - 3 + dy, 0.5), ['#753c54'] * 5, z=1.5, separar=False))
    P.append(Parte(elipse(cx, base - 26 + dy - salto, 7, 7.5), 'branco', z=2))
    P.append(Parte(capsula(cx + 5, base - 24 + dy - salto, cx + 11 + braco, base - 28 + dy - salto - braco, 1.6), 'branco', z=2.5))
    ch = {p for p in elipse(cx, base - 36 + dy - salto, 18 + inchar, 11 + inchar * .5) if p[1] <= base - 32 + dy - salto}
    P.append(Parte(ch, 'roxo', z=3))
    for sx, sy, r in ((-9, -6, 2.4), (2, -8, 2.0), (10, -3, 2.3), (-2, -2, 1.6), (-14, -1, 1.5)):
        P.append(Parte(elipse(cx + sx, base - 36 + dy - salto + sy, r, r), 'lilas', z=4, separar=False, brilho=False))
    for i, xx in enumerate((-6, 0, 6)):
        P.append(Parte(poligono([(cx + xx - 2, base - 46 + dy - salto), (cx + xx, base - 52 + dy - salto - (i % 2) * 2), (cx + xx + 2, base - 46 + dy - salto)]), 'musgo', z=5))
    oy = base - 27 + dy - salto
    for ex in (cx + 1, cx + 5):
        if cara == 'x':
            xis(P, ex, oy)
        else:
            quad(P, ex, oy, 1, 2, OLHO)
    if esporos:
        faiscas(P, cx, base - 25, 14 + esporos * 6, esporos, '#d5e04b', 10 + esporos * 6)
    return desenhar(P, 64, 64)


def anims_rainha():
    f = rainha_esporos
    A = {'parado': [f(), f(dy=1), f(dy=1, inchar=1), f()],
         'mover': [f(), f(salto=2), f(salto=1), f()],
         'atacar': [f(braco=-3), f(braco=4), f(braco=6), f()],
         'dano': [f(cara='x')]}
    A['ataque_1'] = [f(inchar=1, cara='normal'), f(inchar=3), f(inchar=0, esporos=1), f(esporos=2), f(esporos=3)]
    A['ataque_2'] = [f(braco=6), f(braco=8, inchar=1), f(braco=6, esporos=1), f()]
    A['ataque_3'] = [f(dy=2), f(salto=8), f(salto=10), f(dy=2, esporos=1), f()]
    A['morrer'] = [f(cara='x'), f(cara='x', dy=3), dissolver(f(cara='x', dy=5), 0.4), dissolver(f(cara='x', dy=6), 0.8)]
    return A


# ================= 5. Abelha-Rainha Melífera (48) =================

def abelha_rainha(dy=0, asa=0, dx=0, ferrao=0, cara='normal', mel=0):
    P = []
    cx, cy = 21 + dx, 26 + dy
    P.append(Parte(elipse(cx + 1, cy - 10, 6, 4.5 if asa == 0 else 2), 'branco', z=0, plano=True))
    P.append(Parte(poligono([(cx - 8, cy - 1 + ferrao * .5), (cx - 14, cy + 2 + ferrao), (cx - 8, cy + 3 + ferrao * .5)]), 'azul', z=1))
    corpo = elipse(cx, cy, 10, 7)
    P.append(Parte(corpo, 'ouro', z=2))
    for sx in (-5, -4, 1, 2):
        P.append(Parte({p for p in corpo if p[0] == int(cx + sx)}, 'azul', z=3, separar=False, plano=True))
    for lx in (-3, 2, 6):
        P.append(Parte(capsula(cx + lx, cy + 6, cx + lx - 1, cy + 10, 0.8), 'azul', z=1.5))
    P.append(Parte(elipse(cx + 12, cy - 1, 5, 4.6), 'azul', z=4))
    P.append(Parte(poligono([(cx + 8, cy - 5), (cx + 9, cy - 10), (cx + 11, cy - 7), (cx + 13, cy - 11), (cx + 15, cy - 7), (cx + 17, cy - 10), (cx + 16, cy - 4)]), 'amarelo', z=5))
    P.append(Parte(elipse(cx + 3, cy - 9, 5.5, 4 if asa == 0 else 1.8), 'branco', z=6, plano=True))
    if cara == 'x':
        xis(P, cx + 14, cy - 1)
    else:
        quad(P, cx + 14, cy - 2, 2, 2, '#e83b3b' if cara == 'furia' else BRANCO)
    for i in range(mel):
        P.append(Parte(elipse(cx - 6 + i * 9, 44 - (i % 2) * 2, 3, 1.5), 'ouro', z=20))
    return desenhar(P, 48, 48)


def anims_abelha_rainha():
    f = abelha_rainha
    A = {'parado': [f(asa=0), f(asa=1, dy=-1), f(asa=0, dy=-1), f(asa=1)],
         'mover': [f(asa=0), f(asa=1, dx=1, dy=-1), f(asa=0, dx=2), f(asa=1, dx=1, dy=1)],
         'atacar': [f(asa=0, dx=-2, ferrao=-2, cara='furia'), f(asa=1, dx=-3, ferrao=3, cara='furia'), f(asa=0, dx=3, ferrao=4, cara='furia'), f(asa=1)],
         'dano': [f(asa=1, dx=-1, cara='x')]}
    A['ataque_1'] = A['atacar']
    A['ataque_2'] = [f(asa=0, dy=-2, cara='furia'), f(asa=1, dy=-3, cara='furia'), f(asa=0, dy=-2, cara='furia'), f(asa=1)]
    A['ataque_3'] = [f(asa=0), f(asa=1, mel=1), f(asa=0, mel=2), f(asa=1, mel=3), f(asa=0, mel=3)]
    A['morrer'] = morte(f(asa=1, cara='x'), f(asa=1, cara='x'))
    return A


# ================= 6. Guardião de Musgo (64) =================

def guardiao_musgo(dy=0, a=0, braco=(0, 0), cara='normal', regenera=0, raizes=0):
    P = []
    cx = 30
    P.append(Parte(capsula(cx - 8, 46 + dy, cx - 10 - a, 60, 4), MAD, z=0))
    P.append(Parte(capsula(cx - 12, 30 + dy, cx - 20, 44 + dy, 3.5), MAD, z=0.5))
    P.append(Parte(elipse(cx, 36 + dy, 16, 15), PEDRA, z=2))
    P.append(Parte({p for p in elipse(cx - 1, 27 + dy, 17, 9) if p[1] <= 29 + dy}, 'verde', z=3))
    for (sx, sy) in ((-8, 4), (6, 8), (-2, 12)):
        P.append(Parte(elipse(cx + sx, 36 + dy + sy, 2.5, 2), 'verde', z=3.5, separar=False))
    P.append(Parte(capsula(cx + 8, 46 + dy, cx + 10 + a, 60, 4), MAD, z=4))
    for ex in (cx + 4, cx + 11):
        if cara == 'x':
            xis(P, ex, 33 + dy)
        else:
            quad(P, ex, 32 + dy, 2, 3, '#91db69' if cara != 'furia' else '#d5e04b')
    bx, by = cx + 22 + braco[0], 42 + dy + braco[1]
    P.append(Parte(capsula(cx + 12, 30 + dy, bx, by, 4), MAD, z=5))
    P.append(Parte(elipse(bx + 1, by + 2, 4.5, 4), PEDRA, z=5.5))
    if regenera:
        faiscas(P, cx, 30, 18, regenera, '#91db69', 12)
    for i in range(raizes):
        P.append(Parte(capsula(46 + i * 5, 62, 47 + i * 5, 57 - (i % 2) * 2, 1.4), MAD, z=20))
    return desenhar(P, 64, 64)


def anims_guardiao_musgo():
    f = guardiao_musgo
    A = {'parado': [f(), f(dy=1), f(dy=1, braco=(0, 1)), f()],
         'mover': [f(a=2), f(a=1, dy=-1), f(a=-2), f(a=-1, dy=-1)],
         'atacar': [f(braco=(-6, -14)), f(braco=(-4, -18), dy=-1), f(braco=(4, 6), dy=1), f()],
         'dano': [f(cara='x', dy=1)]}
    A['ataque_1'] = [f(braco=(-2, 8), dy=2), f(braco=(-2, 10), dy=2, raizes=1), f(braco=(-2, 10), dy=2, raizes=2), f(braco=(-2, 10), dy=2, raizes=3), f()]
    A['ataque_2'] = [f(braco=(-8, -6), cara='furia'), f(braco=(4, -4), cara='furia'), f(braco=(0, -2), cara='furia'), f(braco=(0, -2), cara='furia'), f()]
    A['ataque_3'] = [f(regenera=1), f(regenera=2, dy=1), f(regenera=3), f(regenera=4, dy=1)]
    A['morrer'] = [f(cara='x'), f(cara='x', dy=3), dissolver(f(cara='x', dy=4), 0.4), dissolver(f(cara='x', dy=5), 0.8)]
    return A


# ================= 7. Cavaleiro de Pedra Musgosa (48) =================

def cavaleiro(dx=0, dy=0, espada=(0, 0), escudo=0, a=0, cara='normal', gira=0):
    P = []
    cx = 22 + dx
    P.append(Parte(capsula(cx - 3, 34 + dy, cx - 4 - a, 44, 2.6), PEDRA, z=0))
    P.append(Parte(capsula(cx + 3, 34 + dy, cx + 4 + a, 44, 2.6), PEDRA, z=1))
    P.append(Parte(retangulo(cx - 7, 20 + dy, cx + 7, 35 + dy, canto=1), PEDRA, z=2, volume='cilindro_v'))
    for (sx, sy) in ((-5, 2), (3, 8), (-2, 12)):
        P.append(Parte(elipse(cx + sx, 20 + dy + sy, 2, 1.5), 'verde_esc', z=2.5, separar=False))
    P.append(Parte(elipse(cx + 1, 14 + dy, 6, 6.5), PEDRA, z=3))
    P.append(Parte(poligono([(cx - 1, 8 + dy), (cx + 1, 2 + dy), (cx + 3, 8 + dy)]), 'verde_esc', z=3.5))
    P.append(Parte(retangulo(cx + 1, 13 + dy, cx + 6, 14 + dy), None, z=4, separar=False, cor=OLHO))
    if cara != 'x':
        quad(P, cx + 4, 13 + dy, 2, 1, '#91db69', z=5)
    else:
        xis(P, cx + 4, 13 + dy, z=5)
    ex, ey = cx + 12 + espada[0], 26 + dy + espada[1]
    P.append(Parte(capsula(cx + 5, 22 + dy, ex - 2, ey, 2.0), PEDRA, z=5))
    P.append(Parte(poligono([(ex - 1, ey - 1), (ex + 1, ey - 1), (ex + 1.5, ey - 13), (ex - 1.5, ey - 10)]), 'ferro', z=6))
    P.append(Parte(retangulo(int(ex) - 3, int(ey), int(ex) + 3, int(ey)), 'castanho', z=6.5))
    sx = cx - 10 + escudo
    P.append(Parte(poligono([(sx - 4, 20 + dy), (sx + 4, 20 + dy), (sx + 4, 32 + dy), (sx, 36 + dy), (sx - 4, 32 + dy)]), 'cobre' if not escudo else 'cobre', z=7 if escudo else 1.5))
    P.append(Parte(elipse(sx, 26 + dy, 1.6, 1.6), 'verde_esc', z=7.5 if escudo else 1.6, separar=False))
    if gira:
        P.append(Parte({p for p in elipse(24, 30, 22, 8) if p not in elipse(24, 30, 20, 6.5) and (p[0] > 24) == (gira % 2 == 1)}, 'branco', z=0, plano=True))
    return desenhar(P, 48, 48)


def anims_cavaleiro():
    f = cavaleiro
    A = {'parado': [f(), f(dy=1), f(dy=1), f()],
         'mover': [f(a=2), f(a=1, dy=-1), f(a=-2), f(a=-1, dy=-1)],
         'atacar': [f(espada=(-8, -8)), f(espada=(-6, -12), dy=-1), f(espada=(6, 4), dx=1), f()],
         'dano': [f(cara='x', dx=-1)]}
    A['ataque_1'] = [f(espada=(-6, -2)), f(espada=(6, 0), gira=1), f(espada=(-14, 0), gira=2), f(espada=(6, 0), gira=1), f()]
    A['ataque_2'] = [f(escudo=12), f(escudo=12, dy=1), f(escudo=12, dy=1), f(escudo=12)]
    A['ataque_3'] = [f(escudo=12, dx=-1), f(escudo=13, dx=3, a=2), f(escudo=13, dx=5, a=-2), f(escudo=12, dx=2)]
    A['morrer'] = [f(cara='x'), f(cara='x', dy=2, espada=(4, 8)), dissolver(f(cara='x', dy=3, espada=(4, 10)), 0.4),
                   dissolver(f(cara='x', dy=4, espada=(4, 10)), 0.8)]
    return A


# ================= 8. Serpente da Névoa (64) =================

def serpente(sobe=0, cab=(0, 0), cara='normal', boca=False, nevoa=0, cuspe=0):
    P = []
    pts = [(22, 58), (20, 50 - sobe * .3), (26, 42 - sobe * .6), (34, 36 - sobe), (36 + cab[0] * .5, 28 - sobe + cab[1] * .5)]
    for i in range(len(pts) - 1):
        r = 5.5 - i * 0.6
        P.append(Parte(capsula(*pts[i], *pts[i + 1], r), 'branco', z=1 + i * .1))
    hx, hy = 40 + cab[0], 24 - sobe + cab[1]
    P.append(Parte(elipse(hx, hy, 6.5, 4.5), 'branco', z=3))
    P.append(Parte(poligono([(hx - 3, hy - 3), (hx - 7, hy - 8), (hx - 1, hy - 4)]), 'agua', z=2.5))
    if boca:
        P.append(Parte(poligono([(hx + 1, hy + 2), (hx + 8, hy + 5), (hx + 2, hy + 4)]), 'branco', z=3.5))
        ponto(P, hx + 4, hy + 2, '#e83b3b')
    if cara == 'x':
        xis(P, hx + 2, hy - 1)
    else:
        quad(P, hx + 2, hy - 2, 2, 1, '#30e1b9')
    P.append(Parte({p for p in elipse(24, 60, 18, 3.5) if p not in elipse(24, 60, 15, 2)}, 'agua', z=10, plano=True))
    for i in range(cuspe):
        P.append(Parte(elipse(hx + 10 + i * 6, hy + 2 + i * 2, 2.4, 1.6), 'agua', z=20))
    img = desenhar(P, 64, 64)
    if nevoa:
        img = dissolver(img, nevoa)
    return img


def anims_serpente():
    f = serpente
    A = {'parado': [f(), f(sobe=1), f(sobe=2), f(sobe=1)],
         'mover': [f(sobe=-6), f(sobe=-12), f(sobe=-6), f()],
         'atacar': [f(cab=(-3, -3)), f(cab=(-4, -4), boca=True), f(cab=(6, 3), boca=True), f()],
         'dano': [f(cara='x', cab=(-2, -1))]}
    A['ataque_1'] = A['atacar']
    A['ataque_2'] = [f(), f(nevoa=0.4), f(nevoa=0.8), f(nevoa=0.97), f(nevoa=0.5), f()]
    A['ataque_3'] = [f(cab=(-2, -2)), f(boca=True, cuspe=1), f(boca=True, cuspe=2), f(boca=True, cuspe=3), f()]
    A['morrer'] = [f(cara='x'), f(cara='x', sobe=-8), dissolver(f(cara='x', sobe=-16), 0.4), dissolver(f(cara='x', sobe=-24), 0.8)]
    return A


# ================= Javali-Rei (64, mini-boss) =================

COURO_REI = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']


def javali_rei(dx=0, dy=0, a=0, cab=0, cara='normal', est=None, vapor=0, onda=0):
    P = []
    k = 1.33

    def S(x, y):
        return x * k + dx, y * k + dy

    for (x1, x2) in ((15, 15 + a), (31, 31 - a)):
        P.append(Parte(capsula(*S(x1, 36), x2 * k + dx, 60, 3.0), ['#2e222f', '#2e222f', '#45293f', '#694f62', '#694f62'], z=0))
    P.append(Parte(elipse(*S(21, 32), 14 * k, 10 * k), COURO_REI, z=2))
    juba = [(9, 25), (11, 19), (14, 23), (17, 18), (19, 22.5), (22, 17.5), (24, 22.5), (27, 18.5), (29, 23.5), (31, 21), (31, 27), (9, 27)]
    P.append(Parte(poligono([S(x, y) for x, y in juba]), ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c'], z=3))
    for (a1, b1, a2, b2) in ((14, 30, 18, 34), (20, 34, 24, 31)):
        P.append(Parte(capsula(*S(a1, b1), *S(a2, b2), 0.5), None, z=3.5, separar=False, cor='#c7dcd0'))
    for (x1, x2) in ((18, 18 - a), (34, 34 + a)):
        P.append(Parte(capsula(*S(x1, 37), x2 * k + dx, 60, 3.2), COURO_REI, z=4))
    hx, hy = S(36, 31 + cab)
    P.append(Parte(elipse(hx, hy, 9.5, 8.5), COURO_REI, z=6))
    P.append(Parte(elipse(hx + 8.5, hy + 3.5, 4, 3.4), 'lilas', z=7))
    quad(P, hx + 11, hy + 2, 1, 2, OLHO)
    P.append(Parte(capsula(hx + 5, hy + 7, hx + 9, hy + 1, 1.3), 'branco', z=8))
    P.append(Parte(capsula(hx + 3, hy + 7, hx + 5, hy + 3, 1.0), 'branco', z=5.5))
    coroa = [(hx - 7, hy - 6), (hx - 8, hy - 13), (hx - 5, hy - 9), (hx - 3, hy - 15), (hx - 1, hy - 9), (hx + 2, hy - 14), (hx + 3, hy - 7)]
    P.append(Parte(poligono(coroa), MAD, z=9))
    P.append(Parte(elipse(hx - 3, hy - 9, 1.2, 1.2), 'verde', z=9.5, separar=False))
    if cara == 'x':
        xis(P, hx + 3, hy - 3)
    else:
        quad(P, hx + 2, hy - 3, 2, 2, '#e83b3b' if cara == 'furia' else OLHO)
    if est is not None:
        estrelas(P, hx, hy - 17, est)
    if vapor:
        faiscas(P, hx + 14, hy + 2, 3, vapor, '#c7dcd0', 5)
    if onda:
        P.append(Parte({p for p in elipse(32, 61, 10 + onda * 8, 2.5) if p not in elipse(32, 61, 8 + onda * 8, 1.5)}, 'castanho', z=0, plano=True))
    return desenhar(P, 64, 64)


def anims_javali_rei():
    f = javali_rei
    A = {'parado': [f(), f(cab=1), f(dy=1, cab=1), f()],
         'mover': [f(a=2), f(a=1, dy=-1), f(a=-2), f(a=-1, dy=-1)],
         'dano': [f(dx=-1, cara='x')]}
    # especial_1 Carga Real (com aviso: raspa a pata e bufa) · especial_2 Cabeçada · especial_3 Chamar Javalis
    # especial_4 Carga Tripla · especial_5 Terramoto · atordoado · mudar_fase
    A['especial_1'] = [f(a=-3, vapor=1, cara='furia'), f(a=3, vapor=2, cara='furia'), f(a=-3, vapor=3, cara='furia'),
                       f(cab=3, a=4, cara='furia'), f(cab=3, a=-4, dy=-1, cara='furia'), f(cab=3, a=4, cara='furia')]
    A['especial_2'] = [f(cab=2, dx=-1), f(cab=-3, dx=3, dy=-1), f(cab=-4, dx=4, dy=-1), f()]
    A['especial_3'] = [f(cab=-3), f(cab=-5, cara='furia', vapor=4), f(cab=-5, cara='furia', vapor=5), f()]
    A['especial_4'] = [f(cab=3, a=4, cara='furia'), f(cab=3, a=-4, dx=2, cara='furia'), f(cab=1, cara='furia'),
                       f(cab=3, a=4, dx=2, cara='furia'), f(cab=1, cara='furia'), f(cab=3, a=-4, dx=2, cara='furia')]
    A['especial_5'] = [f(dy=2, cara='furia'), f(dy=-6, a=3), f(dy=-8, a=3), f(dy=1, onda=1, cara='furia'), f(onda=2), f(onda=3)]
    A['atordoado'] = [f(cab=3, cara='x', est=0), f(cab=3, cara='x', est=1), f(cab=3, cara='x', est=2), f(cab=3, cara='x', est=3)]
    A['mudar_fase'] = [f(), f(cab=-4, cara='furia', vapor=6), f(cab=-5, cara='furia', vapor=7, dy=-1), f(cab=-4, cara='furia', vapor=8), f(cara='furia')]
    A['morrer'] = [f(cara='x'), f(cara='x', dy=2), f(cara='x', dy=3, cab=3), deitar(f(cara='x')), dissolver(deitar(f(cara='x')), 0.3),
                   dissolver(deitar(f(cara='x')), 0.6), dissolver(deitar(f(cara='x')), 0.85)]
    return A


# ================= Ent Ancião (128, boss) =================

SECO = ['#2e222f', '#4c3e24', '#676633', '#a2a947', '#d5e04b']


def ent(dy=0, braco=(0, 0), braco2=(0, 0), perna=0, cara='normal', abanar=0, bolotas=0, raizes=0, folhas=0, seiva=False, grito=False):
    P = []
    cx = 60
    # pernas-raiz
    P.append(Parte(capsula(cx - 14, 96 + dy, cx - 24, 124, 7), MAD, z=0))
    P.append(Parte(capsula(cx + 14, 96 + dy, cx + 22, 124 - perna, 7), MAD, z=4))
    # braço de longe
    b2 = (cx - 46 + braco2[0], 66 + dy + braco2[1])
    P.append(Parte(capsula(cx - 18, 52 + dy, *b2, 6), MAD, z=1))
    P.append(Parte(elipse(b2[0] - 4, b2[1] - 4, 9, 7), 'verde_esc', z=1.5))
    # tronco (metade seca à esquerda)
    tronco = retangulo(cx - 22, 40 + dy, cx + 22, 100 + dy, canto=1)
    P.append(Parte(tronco, MAD, z=2, volume='cilindro_v'))
    P.append(Parte({p for p in tronco if p[0] < cx - 6 and (p[0] + p[1]) % 7 == 0}, ['#4c3e24'] * 5, z=2.2, separar=False, plano=True))
    # copa (verde) e lado seco
    copa = elipse(cx + 8 + abanar, 26 + dy, 36, 22) | elipse(cx + 34 + abanar, 38 + dy, 14, 10)
    P.append(Parte(copa, 'verde', z=3))
    seca = elipse(cx - 22 + abanar, 30 + dy, 20, 15)
    P.append(Parte(seca, SECO, z=3.2))
    for i in range(6):
        P.append(Parte(capsula(cx - 30 + i * 4, 22 + dy, cx - 40 + i * 2, 10 + dy - (i % 3) * 3, 1.0), MAD, z=3.1))
    # cara
    if not grito:
        olhos = '#91db69' if cara != 'furia' else '#d5e04b'
        for ex in (cx + 2, cx + 14):
            if cara == 'x':
                xis(P, ex + 2, 62 + dy)
            else:
                P.append(Parte(elipse(ex + 2, 62 + dy, 3.2, 2.6), None, z=40, separar=False, cor=olhos))
                ponto(P, ex + 1, 61 + dy, BRANCO, 41)
        P.append(Parte(retangulo(cx + 2, 54 + dy, cx + 20, 55 + dy), None, z=39, separar=False, cor='#2e222f'))
        P.append(Parte(retangulo(cx + 6, 74 + dy, cx + 14, 76 + dy), None, z=39, separar=False, cor=OLHO))
    else:
        for ex in (cx + 2, cx + 14):
            P.append(Parte(elipse(ex + 2, 62 + dy, 3.2, 3.2), None, z=40, separar=False, cor='#fbff86'))
        P.append(Parte(elipse(cx + 10, 78 + dy, 6, 6), None, z=40, separar=False, cor=OLHO))
    # barba de musgo
    barba = poligono([(cx - 2, 70 + dy), (cx + 22, 70 + dy), (cx + 18, 92 + dy), (cx + 12, 86 + dy), (cx + 8, 96 + dy), (cx + 4, 86 + dy), (cx, 92 + dy)])
    if grito:
        barba = {p for p in barba if p not in elipse(cx + 10, 78 + dy, 7, 7)}
    P.append(Parte(barba, 'verde_esc', z=38))
    if seiva:
        for (sx, sy) in ((-10, 66), (6, 88), (-14, 84)):
            P.append(Parte(elipse(cx + sx, sy + dy, 2.5, 2.5), 'ouro', z=41))
    # braço de perto
    b = (cx + 46 + braco[0], 66 + dy + braco[1])
    P.append(Parte(capsula(cx + 18, 52 + dy, *b, 6.5), MAD, z=42))
    P.append(Parte(elipse(b[0] + 4, b[1] - 4, 9, 7), 'verde', z=42.5))
    for i in range(bolotas):
        P.append(Parte(elipse(20 + i * 22, 40 + (i % 2) * 14, 3, 3.5), 'castanho', z=60))
    for i in range(raizes):
        for lx in (30, 64, 98):
            P.append(Parte(capsula(lx + i * 2, 127, lx + i * 3, 116 - i * 3, 2.5), MAD, z=60))
    if folhas:
        faiscas(P, 64, 70, 40, folhas, '#91db69', 30)
    return desenhar(P, 128, 128)


def anims_ent():
    f = ent
    A = {'parado': [f(), f(abanar=1), f(dy=1, abanar=1), f(abanar=-1)],
         'mover': [f(perna=6), f(perna=3, dy=-1), f(perna=0), f(perna=3, dy=-1)],
         'dano': [f(cara='x', abanar=-3)]}
    # fase 1
    A['especial_1'] = [f(braco=(-10, -40)), f(braco=(-8, -46), dy=-1), f(braco=(8, 30)), f(braco=(10, 36), dy=1), f()]       # Varrer com o Braço
    A['especial_2'] = [f(braco=(-6, 20), dy=2), f(braco=(-6, 26), dy=2, raizes=1), f(braco=(-6, 26), dy=2, raizes=2), f(braco=(-6, 26), dy=2, raizes=3), f()]  # Raízes em Linha
    A['especial_3'] = [f(abanar=3), f(abanar=-3), f(abanar=3, bolotas=2), f(abanar=-3, bolotas=4), f(bolotas=5)]           # Chuva de Bolotas
    # fase 2
    A['especial_4'] = [f(braco=(-10, -30), braco2=(10, -30), cara='furia'), f(braco=(-12, -40), braco2=(12, -40), cara='furia'),
                       f(braco=(0, 30), braco2=(0, 30), dy=2, cara='furia'), f()]                                                 # Chamar Treants
    A['especial_5'] = [f(braco=(-20, 10), braco2=(20, 10)), f(braco=(-26, 20), braco2=(26, 20), raizes=2), f(braco=(-26, 20), braco2=(26, 20), raizes=4), f()]  # Prisão de Raízes
    A['especial_6'] = [f(folhas=1, abanar=2), f(folhas=2, abanar=-2), f(folhas=3, abanar=2), f(folhas=4, abanar=-2)]       # Folhas Cortantes
    # fase 3
    A['especial_7'] = [f(cara='furia', raizes=1), f(cara='furia', raizes=3, dy=1), f(cara='furia', raizes=4, dy=1), f(cara='furia', raizes=4)]  # Fúria da Floresta
    A['especial_8'] = [f(perna=14), f(perna=20, dy=-2), f(perna=0, dy=2, cara='furia'), f(perna=0, dy=1)]                     # Pisão Gigante
    A['especial_9'] = [f(), f(grito=True), f(grito=True, abanar=3), f(grito=True, abanar=-3), f()]                            # Grito da Árvore
    A['mudar_fase'] = [f(), f(seiva=True, cara='furia'), f(seiva=True, cara='furia', abanar=2), f(seiva=True, cara='furia', abanar=-2), f(seiva=True)]
    A['morrer'] = [f(cara='x'), f(cara='x', dy=2, braco=(0, 20), braco2=(0, 20)), f(cara='x', dy=4, braco=(0, 30), braco2=(0, 30)),
                   dissolver(f(cara='x', dy=6, braco=(0, 34), braco2=(0, 34)), 0.25), dissolver(f(cara='x', dy=8, braco=(0, 36), braco2=(0, 36)), 0.5),
                   dissolver(f(cara='x', dy=8, braco=(0, 36), braco2=(0, 36)), 0.75), dissolver(f(cara='x', dy=8, braco=(0, 36), braco2=(0, 36)), 0.92)]
    return A


# ================= Larva Ancestral (64, boss da masmorra) =================

def larva(sobe=20, cab=(0, 0), cara='normal', boca=False, acido=0, buraco=True):
    P = []
    base = 60
    n = 6
    for i in range(n):
        t = i / (n - 1)
        x = 22 + t * 14 + cab[0] * t
        y = base + 4 - t * sobe + cab[1] * t
        P.append(Parte(elipse(x, y, 7 - t * 1.2, 6 - t * 0.8), MAD, z=1 + i * .1))
        if i < n - 1:
            ponto(P, x - 3, y - 2, '#d5e04b', 2 + i * .1)
    hx, hy = 36 + cab[0], base + 4 - sobe + cab[1]
    if boca:
        P.append(Parte(elipse(hx + 5, hy, 3, 3.5), None, z=4, separar=False, cor='#45293f'))
        for d in (-2, 0, 2):
            ponto(P, hx + 4, hy + d, BRANCO, 5)
    if cara == 'x':
        xis(P, hx + 1, hy - 3)
    else:
        quad(P, hx + 1, hy - 4, 2, 2, '#d5e04b')
    if buraco:
        P.append(Parte(elipse(24, base + 1, 13, 3), ['#2e222f'] * 5, z=0.5, plano=True))
        P.append(Parte({p for p in elipse(24, base, 15, 4) if p[1] < base - 1}, 'castanho', z=9, plano=True))
    for i in range(acido):
        P.append(Parte(elipse(hx + 10 + i * 6, hy + 2 + i * 3, 2.2, 1.8), 'musgo', z=20))
    return desenhar(P, 64, 64)


def anims_larva():
    f = larva
    A = {'parado': [f(), f(sobe=21), f(sobe=22, cab=(1, 0)), f(sobe=21)],
         'mover': [f(sobe=20), f(sobe=12), f(sobe=4), f(sobe=0, buraco=True)],
         'atacar': [f(cab=(-3, -3)), f(cab=(-4, -4), boca=True), f(cab=(6, 3), boca=True), f()],
         'dano': [f(cara='x', cab=(-2, 0))]}
    A['especial_1'] = [f(sobe=0), f(sobe=8), f(sobe=26, boca=True), f(sobe=30, boca=True), f(sobe=24)]   # escavar e sair do chão
    A['especial_2'] = [f(cab=(-2, -2)), f(boca=True, acido=1), f(boca=True, acido=2), f(boca=True, acido=3), f()]  # cuspir ácido
    A['especial_3'] = [f(), f(sobe=24, boca=True), f(sobe=26, boca=True, cab=(2, -2)), f()]                 # chamar larvas
    A['mudar_fase'] = [f(), f(boca=True, cara='normal', sobe=24), f(boca=True, sobe=26), f(sobe=22)]
    A['morrer'] = [f(cara='x'), f(cara='x', sobe=12), dissolver(f(cara='x', sobe=6), 0.4), dissolver(f(cara='x', sobe=2), 0.8)]
    return A


GUARDIOES = {
    'coelho_chifre_anciao': anims_coelho_anciao,
    'coruja_sombria': anims_coruja,
    'lagostim_couracado': anims_lagostim,
    'rainha_dos_esporos': anims_rainha,
    'abelha_rainha_melifera': anims_abelha_rainha,
    'guardiao_de_musgo': anims_guardiao_musgo,
    'cavaleiro_de_pedra_musgosa': anims_cavaleiro,
    'serpente_da_nevoa': anims_serpente,
}
BOSSES = {
    'javali_rei': anims_javali_rei,
    'ent_anciao': anims_ent,
    'larva_ancestral': anims_larva,
}

if __name__ == '__main__':
    for grupo, pasta in ((GUARDIOES, 'guardioes'), (BOSSES, 'bosses')):
        for nome, f in grupo.items():
            A = f()
            guardar(os.path.join(BASE, pasta), nome, A)
            print('ok', nome, ', '.join(f'{k}({len(v)})' for k, v in A.items()))
