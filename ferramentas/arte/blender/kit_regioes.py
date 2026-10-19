"""Kits de peças 3D das regiões 2 a 10 (lista na secção 12 de cada docs/regioes/rXX_*.md).

Cada peça é feita com um MOLDE (chão, parede, rocha, árvore, palmeira, cacto, coral, nuvem, ilha, campa, casa...)
e as TEXTURAS da região (pixel art 32x32, só cores da Resurrect 64). Regras: docs/ARTE.md, secção 6.
Saída: arte/regioes/rXX_*/kit/ (um .glb por peça + rXX_kit.blend + texturas/).

Uso: blenv/bin/python ferramentas/arte/blender/kit_regioes.py [região ...] [--previa]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B

PASTAS = {2: 'r02_cavernas', 3: 'r03_pantano', 4: 'r04_deserto', 5: 'r05_gelo', 6: 'r06_oceano', 7: 'r07_vulcao',
          8: 'r08_reino_assombrado', 9: 'r09_ceu', 10: 'r10_abismo'}

# ------------------------------------------------------------------ moldes ------------------------------------------------------------------


def chao(p, M, m='chao_a', alto=0.2):
    p.caixa(M[m], 0, 0, 0, 2, 2, alto)


def agua(p, M, m='agua', fundo=None):
    if fundo:
        p.caixa(M[fundo], 0, 0, -0.6, 2, 2, 0.5)
    p.caixa(M[m], 0, 0, -0.1, 2, 2, 0.15)


def parede(p, M, m='pedra', topo=None, alto=3.0):
    p.caixa(M[m], 0, 0, 0, 2, 0.8, alto)
    if topo:
        p.caixa(M[topo], 0, 0, alto, 2.1, 0.9, 0.2)


def falesia(p, M, m='pedra', riscas=None):
    for i, (w, d, h) in enumerate(((2, 1.2, 1.4), (1.8, 1.0, 1.2), (1.5, 0.8, 1.0))):
        p.caixa(M[riscas if (riscas and i == 1) else m], 0.1 * i, 0.1 * i, sum((1.4, 1.2, 1.0)[:i]), w, d, h)


def tunel(p, M, m='pedra', forma='reto'):
    """Túnel de 2 m: paredes de lado, teto e uma viga de madeira à entrada."""
    p.caixa(M[m], -1.0, 0, 0, 0.5, 2, 3)
    if forma == 'reto':
        p.caixa(M[m], 1.0, 0, 0, 0.5, 2, 3)
    else:   # curva e T fecham o fundo
        p.caixa(M[m], 0, 1.0, 0, 2, 0.5, 3)
    p.caixa(M[m], 0, 0, 3, 2.4, 2.4, 0.5)
    p.caixa(M['madeira'], 0, -0.9, 2.6, 2.2, 0.25, 0.25)


def viga(p, M):
    for x in (-0.9, 0.9):
        p.caixa(M['madeira'], x, 0, 0, 0.25, 0.25, 2.8)
    p.caixa(M['madeira'], 0, 0, 2.8, 2.2, 0.3, 0.3)


def carris(p, M, forma='reto'):
    p.caixa(M['chao_a'], 0, 0, 0, 2, 2, 0.1)
    if forma in ('reto', 'cruz'):
        for x in (-0.4, 0.4):
            p.caixa(M['metal'], x, 0, 0.1, 0.08, 2, 0.08)
        for y in (-0.7, 0, 0.7):
            p.caixa(M['madeira'], 0, y, 0.1, 1.1, 0.2, 0.05)
    if forma == 'cruz':
        for y in (-0.4, 0.4):
            p.caixa(M['metal'], 0, y, 0.12, 2, 0.08, 0.08)
    if forma == 'curva':
        for r in (0.6, 1.4):
            for i in range(6):
                a = i / 6 * math.pi / 2
                p.caixa(M['metal'], -1 + math.cos(a) * r, -1 + math.sin(a) * r, 0.1, 0.1, 0.3, 0.08, rot_z=a)


def pico(p, M, m='pedra', baixo=False, alto=1.6):
    if baixo:   # estalagmite (do chão)
        p.cilindro(M[m], 0, 0, 0, 0.45, 0.02, alto, 6)
    else:       # estalactite (pendurada no teto, a 3 m)
        p.cilindro(M[m], 0, 0, 3.0 - alto, 0.02, 0.45, alto, 6)


def rocha(p, M, m='pedra', r=0.8, h=0.6, s=1, topo=None):
    p.bola(M[m], 0, 0, h * 0.8, r, r * 0.85, h, 1, semente=s, irregular=0.18)
    if topo:
        p.bola(M[topo], 0.05, 0, h * 1.5, r * 0.8, r * 0.7, h * 0.35, 1, semente=s + 1, irregular=0.1)


def arvore(p, M, casca='casca', folhas='folhas', esc=1.0, s=1, forma='redonda'):
    p.cilindro(M[casca], 0, 0, 0, 0.42 * esc, 0.3 * esc, 2.6 * esc, 7)
    if forma == 'cone':
        for r, z in ((1.6, 1.0), (1.25, 2.2), (0.85, 3.3)):
            p.cilindro(M[folhas], 0, 0, z * esc, r * esc, 0.05, 1.7 * esc, 7)
    elif forma == 'nua':
        for a in (0.5, 2.4, 4.2):
            p.cilindro(M[casca], math.cos(a) * 0.2, math.sin(a) * 0.2, 2.2 * esc, 0.12, 0.03, 1.4 * esc, 5,
                       rot=(math.cos(a) * 0.7, math.sin(a) * 0.7, 0))
    else:
        for (x, y, z, r) in ((0, 0, 3.3, 1.5), (0.8, 0.4, 2.9, 1.0), (-0.8, -0.3, 3.0, 1.1)):
            p.bola(M[folhas], x * esc, y * esc, z * esc, r * esc, r * esc, r * 0.85 * esc, 1, semente=s + int(x * 10), irregular=0.12)


def palmeira(p, M, casca='casca', folhas='folhas'):
    for i in range(5):
        p.cilindro(M[casca], i * 0.12, 0, i * 0.8, 0.22 - i * 0.02, 0.2 - i * 0.02, 0.85, 6, rot=(0, 0.12, 0))
    for k in range(6):
        a = k / 6 * math.tau
        p.bola(M[folhas], 0.6 + math.cos(a) * 0.9, math.sin(a) * 0.9, 4.0 - 0.2 * (k % 2), 1.1, 0.35, 0.12, 0,
               semente=k)


def cacto(p, M, m='folhas', bracos=2):
    p.cilindro(M[m], 0, 0, 0, 0.3, 0.28, 2.2, 8)
    p.bola(M[m], 0, 0, 2.2, 0.28, 0.28, 0.2, 0)
    for i in range(bracos):
        s = 1 if i == 0 else -1
        p.cilindro(M[m], s * 0.45, 0, 0.9 + i * 0.3, 0.16, 0.16, 0.25, 6, rot=(0, math.radians(90) * s, 0))
        p.cilindro(M[m], s * 0.6, 0, 1.0 + i * 0.3, 0.16, 0.15, 0.8, 6)


def arbusto(p, M, m='folhas', r=0.7, s=1, frutos=None):
    p.bola(M[m], 0, 0, r * 0.7, r, r, r * 0.75, 1, semente=s, irregular=0.15)
    p.bola(M[m], r * 0.6, 0.2, r * 0.5, r * 0.6, r * 0.6, r * 0.5, 1, semente=s + 3, irregular=0.15)
    if frutos:
        for i in range(5):
            a = i * 1.3
            p.bola(M[frutos], math.cos(a) * r * 0.8, math.sin(a) * r * 0.8, r * (0.7 + 0.1 * (i % 2)), 0.1, 0.1, 0.1, 0)


def erva(p, M, m='folhas', n=5, alto=0.45, flor=None):
    for i in range(n):
        a = i * 1.25
        p.cilindro(M[m], math.cos(a) * 0.15, math.sin(a) * 0.15, 0, 0.06, 0.01, alto, 3,
                   rot=(math.cos(a) * 0.3, math.sin(a) * 0.3, 0))
    if flor:
        p.bola(M[flor], 0, 0, alto, 0.12, 0.12, 0.08, 0)


def junco(p, M, m='folhas'):
    for i in range(7):
        a = i * 0.9
        p.cilindro(M[m], math.cos(a) * 0.25, math.sin(a) * 0.25, 0, 0.04, 0.02, 1.2 + 0.2 * (i % 3), 3)
        p.cilindro(M['casca'], math.cos(a) * 0.25, math.sin(a) * 0.25, 1.0 + 0.2 * (i % 3), 0.06, 0.06, 0.25, 4)


def minerio(p, M, m='minerio', s=80):
    p.bola(M[m], 0, 0, 0.45, 0.75, 0.65, 0.6, 1, semente=s, irregular=0.2)


def cristais(p, M, m='cristal_luz'):
    for i, (x, y, h, inc) in enumerate(((0, 0, 1.4, 0), (0.35, 0.1, 0.9, 0.35), (-0.3, -0.15, 1.0, -0.3), (0.05, 0.35, 0.7, 0.2))):
        p.cilindro(M[m], x, y, 0, 0.18, 0.0, h, 5, rot=(inc, inc * 0.5, 0))


def arvore_cortavel(p, M, casca='casca', folhas='folhas'):
    p.cilindro(M[casca], 0, 0, 0, 0.3, 0.22, 1.8, 7)
    p.bola(M[folhas], 0, 0, 2.4, 1.1, 1.1, 0.95, 1, semente=81, irregular=0.12)


def bau(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 0.9, 0.6, 0.5)
    p.caixa(M['madeira'], 0, 0, 0.5, 0.92, 0.62, 0.22)
    for x in (-0.3, 0.3):
        p.caixa(M['metal'], x, 0, 0, 0.08, 0.64, 0.74)
    p.caixa(M['metal'], 0, -0.31, 0.38, 0.12, 0.04, 0.15)


def fogueira(p, M, fogo='fogo_luz'):
    for i in range(7):
        a = i / 7 * math.tau
        p.bola(M['pedra'], math.cos(a) * 0.55, math.sin(a) * 0.55, 0.1, 0.18, 0.15, 0.13, 0, semente=90 + i)
    p.cilindro(M['madeira'], 0, 0, 0.08, 0.08, 0.08, 0.9, 5, rot=(0, math.radians(90), 0.6))
    p.cilindro(M['madeira'], 0, 0, 0.08, 0.08, 0.08, 0.9, 5, rot=(0, math.radians(90), -0.6))
    p.cilindro(M[fogo], 0, 0, 0.1, 0.3, 0.02, 0.7, 6)


def braseiro(p, M, fogo='fogo_luz', m='metal'):
    p.cilindro(M[m], 0, 0, 0, 0.12, 0.12, 0.9, 6)
    p.cilindro(M[m], 0, 0, 0.9, 0.2, 0.45, 0.3, 8)
    p.cilindro(M[fogo], 0, 0, 1.15, 0.35, 0.02, 0.6, 6)


def cristal_teletransporte(p, M):
    p.cilindro(M['pedra'], 0, 0, 0, 0.7, 0.6, 0.3, 8)
    p.cilindro(M['cristal_luz'], 0, 0, 0.3, 0.35, 0.0, 1.6, 6)
    p.cilindro(M['cristal_luz'], 0, 0, 0.3, 0.35, 0.35, 0.25, 6)


def tocha(p, M):
    p.caixa(M['pedra'], 0, 0.35, 0, 0.6, 0.1, 2.4)
    p.cilindro(M['madeira'], 0, 0.15, 1.5, 0.06, 0.08, 0.5, 5, rot=(-0.4, 0, 0))
    p.cilindro(M['fogo_luz'], 0, 0.0, 1.95, 0.12, 0.01, 0.35, 5)


def lanterna(p, M, luz='luz'):
    p.cilindro(M['metal'], 0, 0, 0, 0.06, 0.06, 1.6, 5)
    p.caixa(M['metal'], 0, 0, 1.6, 0.35, 0.35, 0.06)
    p.caixa(M[luz], 0, 0, 1.66, 0.25, 0.25, 0.3)
    p.cilindro(M['metal'], 0, 0, 1.96, 0.25, 0.02, 0.2, 4)


def ponte(p, M, m='madeira', corda='casca'):
    p.caixa(M[m], 0, 0, 0.3, 2, 4, 0.15)
    for x in (-0.9, 0.9):
        for y in (-1.8, 0, 1.8):
            p.cilindro(M[corda], x, y, 0, 0.1, 0.1, 1.2, 6)
        p.caixa(M[corda], x, 0, 1.05, 0.12, 4, 0.12)


def escada(p, M, m='madeira'):
    for i in range(4):
        p.caixa(M[m], 0, -0.75 + i * 0.5, 0, 2, 0.5, 0.25 * (i + 1))


def coluna(p, M, m='pedra', partida=False):
    p.caixa(M[m], 0, 0, 0, 0.9, 0.9, 0.3)
    p.cilindro(M[m], 0, 0, 0.3, 0.35, 0.32, 1.4 if partida else 3.0, 8)
    if not partida:
        p.caixa(M[m], 0, 0, 3.3, 0.9, 0.9, 0.3)


def tenda(p, M, tecido='tecido'):
    p.prisma(M[tecido], [(-1.2, -1.0), (1.2, -1.0), (0, 0.0)], 0, 0.01)
    p.telhado(M[tecido], 0, 0, 0, 2.2, 2.4, 2.0, beiral=0.05)
    p.cilindro(M['madeira'], 0, -1.2, 0, 0.05, 0.05, 2.2, 4)


def casa(p, M, parede='madeira', telhado='telhado', palafita=False):
    z = 1.2 if palafita else 0
    if palafita:
        for x in (-1.3, 1.3):
            for y in (-1.3, 1.3):
                p.cilindro(M['madeira'], x, y, 0, 0.1, 0.1, 1.2, 5)
    p.caixa(M[parede], 0, 0, z, 3, 3, 2.2)
    p.telhado(M[telhado], 0, 0, z + 2.2, 3.2, 3.4, 1.4)
    p.caixa(M['madeira'], 0, -1.52, z, 0.8, 0.06, 1.6)


def campa(p, M, m='pedra', tipo=1):
    if tipo == 1:
        p.caixa(M[m], 0, 0, 0, 0.7, 0.2, 0.9)
        p.cilindro(M[m], 0, 0, 0.9, 0.35, 0.35, 0.2, 8, rot=(math.radians(90), 0, 0))
    elif tipo == 2:
        p.caixa(M[m], 0, 0, 0, 0.15, 0.15, 1.3)
        p.caixa(M[m], 0, 0, 0.8, 0.7, 0.15, 0.15)
    else:
        p.caixa(M[m], 0, 0, 0, 1.0, 2.0, 0.5)
        p.caixa(M[m], 0, 0.85, 0.5, 0.9, 0.2, 0.7)
    p.caixa(M['chao_b'], 0, -0.6, 0, 0.8, 1.1, 0.05)


def osso(p, M, m='osso', grande=False):
    k = 2.0 if grande else 1.0
    p.cilindro(M[m], 0, 0, 0.1 * k, 0.07 * k, 0.07 * k, 1.0 * k, 5, rot=(0, math.radians(90), 0.4))
    for dx in (-0.5, 0.5):
        p.bola(M[m], dx * k * 0.92, dx * k * 0.39, 0.1 * k, 0.14 * k, 0.14 * k, 0.12 * k, 0)


def coral(p, M, m='coral', s=1):
    p.cilindro(M[m], 0, 0, 0, 0.18, 0.12, 0.9, 5)
    for i in range(5):
        a = i * 1.3 + s
        p.cilindro(M[m], math.cos(a) * 0.15, math.sin(a) * 0.15, 0.5 + 0.12 * i, 0.09, 0.03, 0.7, 4,
                   rot=(math.cos(a) * 0.6, math.sin(a) * 0.6, 0))
        p.bola(M[m], math.cos(a) * 0.5, math.sin(a) * 0.5, 1.0 + 0.12 * i, 0.12, 0.12, 0.12, 0)


def alga(p, M, m='alga', alto=1.2):
    for i in range(4):
        a = i * 1.6
        for k in range(int(alto / 0.4)):
            p.cilindro(M[m], math.cos(a) * 0.2 + 0.08 * math.sin(k), math.sin(a) * 0.2, k * 0.4, 0.07, 0.06, 0.42, 4)


def nuvem(p, M, m='nuvem', alto=0.5, fraca=False):
    for i, (x, y, r) in enumerate(((0, 0, 1.0), (0.7, 0.3, 0.7), (-0.6, -0.3, 0.75), (0.2, -0.7, 0.6))):
        p.bola(M[m], x, y, alto, r, r, r * (0.35 if fraca else 0.55), 1, semente=i)


def ilha(p, M, topo='chao_a', m='pedra', r=1.0, s=1):
    p.cilindro(M[m], 0, 0, -1.6 * r, 0.1, r, 1.6 * r, 7)
    p.cilindro(M[topo], 0, 0, 0, r, r * 0.95, 0.2, 7)
    p.bola(M[m], 0.2, 0.1, -1.0 * r, r * 0.5, r * 0.5, r * 0.6, 1, semente=s, irregular=0.2)


def placa_luz(p, M, m='luz_azul'):
    p.caixa(M[m], 0, 0, 0, 2, 2, 0.1)


def moldura(p, M, m='madeira', vidro='vidro', alto=2.4, larg=1.2):
    p.caixa(M[m], 0, 0, 0, larg + 0.2, 0.2, alto + 0.2)
    p.caixa(M[vidro], 0, -0.06, 0.1, larg, 0.12, alto)


def estante(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 1.6, 0.5, 2.4)
    for z in (0.5, 1.1, 1.7):
        p.caixa(M['livros'], 0, -0.05, z, 1.4, 0.45, 0.45)


def grade(p, M, m='metal'):
    for i in range(7):
        p.cilindro(M[m], -0.9 + i * 0.3, 0, 0, 0.04, 0.04, 2.0, 4)
    for z in (0.2, 1.8):
        p.caixa(M[m], 0, 0, z, 2, 0.06, 0.08)


def vela(p, M):
    p.cilindro(M['cera'], 0, 0, 0, 0.18, 0.16, 1.2, 8)
    p.cilindro(M['fogo_luz'], 0, 0, 1.2, 0.07, 0.01, 0.25, 4)


def objeto(p, M, m='pedra', r=0.6, s=1):
    p.bola(M[m], 0, 0, r, r, r, r, 1, semente=s, irregular=0.1)


def balao(p, M):
    p.bola(M['tecido'], 0, 0, 3.0, 1.2, 1.2, 1.4, 1)
    p.caixa(M['madeira'], 0, 0, 0, 0.9, 0.9, 0.6)
    for x in (-0.4, 0.4):
        p.cilindro(M['corda'], x, 0, 0.6, 0.02, 0.02, 1.4, 3)


def relogio_sol(p, M):
    p.cilindro(M['pedra'], 0, 0, 0, 0.9, 0.9, 0.2, 12)
    p.prisma(M['metal'], [(0, 0), (0.6, 0), (0, 0.05)], 0.2, 0.8)


def ancora(p, M):
    p.cilindro(M['luz_azul'], 0, 0, 0, 0.1, 0.1, 1.8, 6)
    p.cilindro(M['luz_azul'], 0, 0, 1.4, 0.06, 0.06, 0.9, 5, rot=(0, math.radians(90), 0))
    p.bola(M['luz_azul'], 0, 0, 2.0, 0.2, 0.2, 0.2, 0)


def portal(p, M, m='luz_roxa'):
    p.cilindro(M['pedra'], 0, 0, 0, 1.0, 1.0, 0.2, 10)
    for i in range(12):
        a = i / 12 * math.tau
        p.bola(M[m], math.cos(a) * 0.9, 0, 1.2 + math.sin(a) * 0.9, 0.15, 0.15, 0.15, 0)


def janela_sistema(p, M):
    p.caixa(M['luz_azul'], 0, 0, 0.8, 1.6, 0.05, 1.0)
    p.caixa(M['metal'], 0, 0.02, 0.75, 1.7, 0.03, 0.05)


def geiser(p, M):
    p.cilindro(M['pedra'], 0, 0, 0, 0.8, 0.4, 0.4, 8)
    p.cilindro(M['vapor'], 0, 0, 0.4, 0.25, 0.5, 2.5, 6)


def ostra(p, M):
    p.bola(M['pedra'], 0, 0, 0.15, 0.45, 0.35, 0.15, 0)
    p.bola(M['pedra'], 0, 0.15, 0.35, 0.45, 0.35, 0.12, 0)
    p.bola(M['branco'], 0, 0, 0.27, 0.1, 0.1, 0.1, 0)


def cupula(p, M):
    p.bola(M['bolha'], 0, 0, 0, 2.0, 2.0, 2.0, 2)


def igloo(p, M):
    p.bola(M['neve'], 0, 0, 0, 1.4, 1.4, 1.2, 1)


MOLDES = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k not in ('B',)}

# ------------------------------------------------------------------ regiões ------------------------------------------------------------------
# texturas: nome -> (cores, extras)  ·  peças: (nome, molde, parâmetros)

def T(*cores, **kw):
    return (list(cores), kw)


BASE_TEX = {
    'madeira': T('#966c6c', '#ab947a', '#694f62', tabuas=('#45293f', 6)),
    'metal': T('#7f708a', '#9babb2', '#625565'),
    'fogo': T('#f79617', '#fb6b1d', '#f9c22b', '#fbff86'),
    'cristal': T('#4d9be6', '#8fd3ff', '#4d65b4', '#ffffff'),
    'tecido': T('#ab947a', '#c7dcd0', '#966c6c'),
    'branco': T('#c7dcd0', '#ffffff', '#9babb2'),
    'corda': T('#ab947a', '#966c6c'),
    'livros': T('#b33831', '#4d65b4', '#239063', '#f9c22b', tabuas=('#2e222f', 4)),
    'cera': T('#c7dcd0', '#ffffff', '#fdcbb0'),
    'osso': T('#c7dcd0', '#ffffff', '#9babb2', '#ab947a'),
    'telhado': T('#b33831', '#6e2727', '#ea4f36', tabuas=('#45293f', 4)),
}
LUZES = {'fogo_luz': ('fogo', 3.0), 'cristal_luz': ('cristal', 1.5)}
CORES_LUZ = {'luz': ('#fbff86', 2.0), 'luz_azul': ('#4d9be6', 1.8), 'luz_roxa': ('#a884f3', 2.0), 'vapor': ('#c7dcd0', 0.6),
             'bolha': ('#8ff8e2', 0.4), 'vidro': ('#8fd3ff', 0.8)}

REGIOES = {
    2: dict(tex={
        'chao_a': T('#625565', '#7f708a', '#3e3546'), 'chao_b': T('#694f62', '#625565', '#45293f', manchas=[('#9babb2', 6, 1)]),
        'chao_c': T('#3e3546', '#625565', '#2e222f'), 'pedra': T('#625565', '#7f708a', '#3e3546', '#9babb2'),
        'minerio': T('#7f708a', '#625565', manchas=[('#c7dcd0', 6, 1), ('#9babb2', 6, 0)]),
        'carvao': T('#3e3546', '#2e222f', '#625565'), 'casca': T('#694f62', '#4c3e24'),
        'cristal_v': T('#1ebc73', '#91db69', '#239063'), 'cristal_r': T('#c32454', '#f04f78', '#831c5d'),
    }, pecas=[
        ('parede_rocha', 'parede', {}), ('chao_1', 'chao', {}), ('chao_2', 'chao', dict(m='chao_b')), ('chao_3', 'chao', dict(m='chao_c')),
        ('tunel_reto', 'tunel', {}), ('tunel_curva', 'tunel', dict(forma='curva')), ('tunel_t', 'tunel', dict(forma='T')),
        ('viga_mina', 'viga', {}), ('carris_reto', 'carris', {}), ('carris_curva', 'carris', dict(forma='curva')),
        ('carris_cruzamento', 'carris', dict(forma='cruz')), ('estalactite', 'pico', {}), ('estalagmite', 'pico', dict(baixo=True)),
        ('rocha_1', 'rocha', {}), ('rocha_2', 'rocha', dict(r=0.6, h=0.45, s=2)), ('rocha_3', 'rocha', dict(r=1.0, h=0.8, s=3)),
        ('minerio_ferro', 'minerio', {}), ('veio_carvao', 'minerio', dict(m='carvao', s=81)), ('escora', 'viga', {}),
        ('cristal_azul', 'cristais', {}), ('cristal_verde', 'cristais', dict(m='cristal_v_luz')),
        ('cristal_rosa', 'cristais', dict(m='cristal_r_luz')), ('bau', 'bau', {}), ('fogueira', 'fogueira', {}),
        ('cristal_teletransporte', 'cristal_teletransporte', {}), ('tocha_parede', 'tocha', {}), ('lanterna', 'lanterna', {}),
        ('ponte_corda', 'ponte', {}), ('escada_madeira', 'escada', {}),
    ]),
    3: dict(tex={
        'agua': T('#374e4a', '#547e64', '#313638'), 'lama': T('#4c3e24', '#694f62', '#45293f'),
        'chao_a': T('#374e4a', '#547e64', '#4c3e24'), 'chao_b': T('#165a4c', '#239063', '#374e4a'),
        'pedra': T('#547e64', '#374e4a', '#7f708a'), 'casca': T('#4c3e24', '#694f62'), 'folhas': T('#239063', '#165a4c', '#1ebc73'),
        'folhas_b': T('#547e64', '#92a984', '#374e4a'), 'minerio': T('#3e3546', '#2e222f', manchas=[('#625565', 6, 1)]),
        'nenufar': T('#239063', '#1ebc73', manchas=[('#ed8099', 3, 0)]),
    }, pecas=[
        ('agua_pantano', 'agua', dict(fundo='lama')), ('lama', 'chao', dict(m='lama')), ('chao_selva_1', 'chao', {}),
        ('chao_selva_2', 'chao', dict(m='chao_b')), ('passadico', 'ponte', dict(corda='madeira')), ('raiz', 'osso', dict(m='casca', grande=True)),
        ('arvore_mangue', 'arvore', dict(folhas='folhas_b', esc=1.1)), ('palmeira', 'palmeira', {}),
        ('arvore_selva_1', 'arvore', dict(esc=1.3, s=5)), ('arvore_selva_2', 'arvore', dict(esc=1.0, s=9)),
        ('folhas_gigantes', 'arbusto', dict(r=1.1, s=4)), ('lianas', 'alga', dict(m='folhas', alto=2.4)), ('juncos', 'junco', {}),
        ('nenufar', 'chao', dict(m='nenufar', alto=0.05)), ('rocha_musgo_1', 'rocha', dict(topo='folhas_b')),
        ('rocha_musgo_2', 'rocha', dict(r=0.6, h=0.5, s=5, topo='folhas_b')), ('minerio_ferro_negro', 'minerio', {}),
        ('arvore_cortavel', 'arvore_cortavel', {}), ('erva', 'erva', {}), ('bau', 'bau', {}), ('fogueira', 'fogueira', {}),
        ('cristal', 'cristal_teletransporte', {}), ('ponte_corda', 'ponte', {}), ('vegetacao_cortavel', 'arbusto', dict(r=0.6, s=8)),
    ]),
    4: dict(tex={
        'chao_a': T('#fbb954', '#f9c22b', '#f79617'), 'chao_b': T('#f79617', '#fbb954', '#cd683d'),
        'chao_c': T('#e6904e', '#fbb954', '#cd683d', manchas=[('#ab947a', 5, 0)]),
        'pedra': T('#cd683d', '#9e4539', '#e6904e'), 'riscas': T('#e6904e', '#cd683d', riscas=('#9e4539', 6)),
        'casca': T('#966c6c', '#694f62'), 'folhas': T('#a2a947', '#676633', '#d5e04b'), 'cacto': T('#239063', '#1ebc73', '#165a4c'),
        'minerio': T('#cd683d', '#9e4539', manchas=[('#c7dcd0', 6, 1), ('#ffffff', 3, 0)]), 'adobe': T('#e6904e', '#cd683d', '#fbb954'),
        'tecido': T('#ea4f36', '#f9c22b', '#b33831', riscas=('#ffffff', 5)), 'movedica': T('#f79617', '#cd683d', '#fbb954'),
    }, pecas=[
        ('areia_1', 'chao', {}), ('areia_2', 'chao', dict(m='chao_b')), ('areia_3', 'chao', dict(m='chao_c')),
        ('duna_pequena', 'rocha', dict(m='chao_a', r=1.0, h=0.4)), ('duna_media', 'rocha', dict(m='chao_a', r=1.6, h=0.7, s=4)),
        ('duna_grande', 'rocha', dict(m='chao_b', r=2.2, h=1.0, s=6)), ('rocha_vermelha_1', 'rocha', {}),
        ('rocha_vermelha_2', 'rocha', dict(r=0.6, h=0.9, s=7)), ('rocha_vermelha_3', 'rocha', dict(r=1.1, h=0.5, s=8)),
        ('falesia_riscas', 'falesia', dict(riscas='riscas')), ('palmeira', 'palmeira', {}),
        ('acacia', 'arvore', dict(esc=0.9, s=3)), ('cacto_1', 'cacto', dict(m='cacto')), ('cacto_2', 'cacto', dict(m='cacto', bracos=1)),
        ('osso_1', 'osso', {}), ('osso_2', 'osso', dict(grande=True)), ('minerio_prata', 'minerio', {}),
        ('arvore_cortavel', 'arvore_cortavel', {}), ('erva_seca', 'erva', dict(m='folhas')), ('bau', 'bau', {}),
        ('fogueira', 'fogueira', {}), ('cristal', 'cristal_teletransporte', {}), ('tenda', 'tenda', {}),
        ('parede_adobe', 'parede', dict(m='adobe')), ('escadas_pedra', 'escada', dict(m='pedra')), ('coluna_antiga', 'coluna', dict(m='adobe')),
        ('areia_movedica', 'chao', dict(m='movedica', alto=0.05)),
    ]),
    5: dict(tex={
        'chao_a': T('#ffffff', '#c7dcd0', '#9babb2'), 'chao_b': T('#c7dcd0', '#ffffff', '#8fd3ff'), 'chao_c': T('#c7dcd0', '#9babb2'),
        'gelo': T('#8fd3ff', '#c7dcd0', '#4d9be6'), 'gelo_fino': T('#c7dcd0', '#8fd3ff', riscas=('#ffffff', 5)),
        'pedra': T('#7f708a', '#625565', '#9babb2'), 'neve': T('#ffffff', '#c7dcd0'), 'casca': T('#694f62', '#45293f'),
        'folhas': T('#374e4a', '#165a4c', manchas=[('#ffffff', 8, 1)]), 'bagas': T('#e83b3b', '#b33831'),
        'gelo_eterno': T('#4d9be6', '#8fd3ff', '#ffffff', '#4d65b4'), 'troncos': T('#966c6c', '#694f62', riscas=('#45293f', 4)),
        'telhado': T('#ffffff', '#c7dcd0', '#9babb2'),
    }, pecas=[
        ('neve_1', 'chao', {}), ('neve_2', 'chao', dict(m='chao_b')), ('neve_3', 'chao', dict(m='chao_c')), ('gelo_liso', 'chao', dict(m='gelo')),
        ('gelo_fino', 'chao', dict(m='gelo_fino', alto=0.08)), ('neve_funda', 'chao', dict(alto=0.6)),
        ('rocha_neve_1', 'rocha', dict(topo='neve')), ('rocha_neve_2', 'rocha', dict(r=0.6, h=0.5, s=5, topo='neve')),
        ('rocha_neve_3', 'rocha', dict(r=1.1, h=0.8, s=6, topo='neve')), ('falesia_gelo', 'falesia', dict(m='gelo')),
        ('pinheiro_nevado_1', 'arvore', dict(forma='cone')), ('pinheiro_nevado_2', 'arvore', dict(forma='cone', esc=1.3)),
        ('arbusto_bagas', 'arbusto', dict(frutos='bagas')), ('bloco_gelo_eterno', 'rocha', dict(m='gelo_eterno', r=0.7, h=0.7)),
        ('arvore_cortavel', 'arvore_cortavel', {}), ('flor_de_neve', 'erva', dict(flor='neve')), ('bau', 'bau', {}),
        ('fogueira', 'fogueira', {}), ('cristal', 'cristal_teletransporte', {}), ('casa_troncos', 'casa', dict(parede='troncos')),
        ('ponte_gelo', 'ponte', dict(m='gelo', corda='gelo')), ('estaca_gelo', 'pico', dict(m='gelo', baixo=True)),
        ('banco_neve', 'rocha', dict(m='neve', r=1.0, h=0.4, s=9)),
    ]),
    6: dict(tex={
        'chao_a': T('#fdcbb0', '#ffffff', '#fca790'), 'chao_b': T('#fca790', '#fdcbb0', manchas=[('#c7dcd0', 6, 0)]),
        'agua': T('#0eaf9b', '#30e1b9', '#0b8a8f'), 'agua_funda': T('#0b5e65', '#0b8a8f', '#323353'),
        'pedra': T('#7f708a', '#625565', '#0b8a8f'), 'casca': T('#966c6c', '#694f62'), 'folhas': T('#1ebc73', '#239063'),
        'coral': T('#f04f78', '#ed8099', '#c32454'), 'coral_b': T('#f79617', '#fbb954'), 'coral_c': T('#a884f3', '#905ea9'),
        'alga': T('#239063', '#165a4c', '#1ebc73'), 'fundo': T('#0b5e65', '#0b8a8f', manchas=[('#fdcbb0', 4, 0)]),
        'fundo_b': T('#323353', '#0b5e65'), 'minerio': T('#f04f78', '#c32454', manchas=[('#ffffff', 4, 0)]),
        'naufragio': T('#694f62', '#45293f', tabuas=('#2e222f', 5)), 'telhado': T('#a2a947', '#676633', tabuas=('#4c3e24', 4)),
    }, pecas=[
        ('areia_branca_1', 'chao', {}), ('areia_branca_2', 'chao', dict(m='chao_b')), ('mar_raso', 'agua', dict(fundo='chao_a')),
        ('mar_fundo', 'agua', dict(m='agua_funda', fundo='fundo_b')), ('rocha_mare_1', 'rocha', {}),
        ('rocha_mare_2', 'rocha', dict(r=0.6, h=0.5, s=4)), ('rocha_mare_3', 'rocha', dict(r=1.1, h=0.7, s=6)),
        ('palmeira', 'palmeira', {}), ('recife_1', 'coral', {}), ('recife_2', 'coral', dict(m='coral_b', s=2)),
        ('recife_3', 'coral', dict(m='coral_c', s=4)), ('alga_pequena', 'alga', {}), ('alga_gigante', 'alga', dict(alto=3.2)),
        ('fundo_mar_1', 'chao', dict(m='fundo')), ('fundo_mar_2', 'chao', dict(m='fundo_b')), ('minerio_coral', 'minerio', {}),
        ('madeira_naufragio', 'osso', dict(m='naufragio', grande=True)), ('ostra', 'ostra', {}), ('bau', 'bau', {}),
        ('fogueira', 'fogueira', {}), ('cristal', 'cristal_teletransporte', {}), ('casa_palafita', 'casa', dict(palafita=True)),
        ('cais', 'ponte', {}), ('bolha_ar', 'objeto', dict(m='bolha', r=0.4)), ('cupula_ar', 'cupula', {}),
    ]),
    7: dict(tex={
        'chao_a': T('#3e3546', '#2e222f', '#625565'), 'chao_b': T('#2e222f', '#3e3546', manchas=[('#ea4f36', 3, 0)]),
        'chao_c': T('#45293f', '#3e3546'), 'cinza': T('#7f708a', '#625565', '#9babb2'), 'cinza_b': T('#625565', '#7f708a'),
        'lava': T('#ea4f36', '#f79617', '#f9c22b', '#b33831'), 'pedra': T('#3e3546', '#45293f', '#625565'),
        'casca': T('#45293f', '#2e222f', '#625565'), 'petrificado': T('#7f708a', '#625565'),
        'minerio': T('#2e222f', '#45293f', manchas=[('#6b3e75', 6, 1), ('#a884f3', 3, 0)]), 'brasa': T('#45293f', manchas=[('#ea4f36', 6, 1)]),
        'folhas': T('#9babb2', '#7f708a'), 'obsidiana': T('#2e222f', '#45293f', '#6b3e75'),
    }, pecas=[
        ('basalto_1', 'chao', {}), ('basalto_2', 'chao', dict(m='chao_b')), ('basalto_3', 'chao', dict(m='chao_c')),
        ('cinza_1', 'chao', dict(m='cinza')), ('cinza_2', 'chao', dict(m='cinza_b')), ('lava', 'agua', dict(m='lava_luz', fundo='pedra')),
        ('rocha_vulcanica_1', 'rocha', {}), ('rocha_vulcanica_2', 'rocha', dict(r=0.6, h=0.6, s=5)),
        ('rocha_vulcanica_3', 'rocha', dict(r=1.1, h=0.8, s=7)), ('falesia_negra', 'falesia', {}),
        ('arvore_petrificada', 'arvore', dict(casca='petrificado', forma='nua')), ('tronco_queimado_1', 'arvore', dict(forma='nua', esc=0.7)),
        ('tronco_queimado_2', 'osso', dict(m='casca', grande=True)), ('obsidiana', 'minerio', {}),
        ('lenho_brasa', 'arvore_cortavel', dict(casca='brasa', folhas='cinza')), ('flor_de_cinza', 'erva', dict(m='folhas', flor='lava_luz')),
        ('bau', 'bau', {}), ('fogueira', 'fogueira', {}), ('cristal', 'cristal_teletransporte', {}),
        ('ponte_pedra', 'ponte', dict(m='pedra', corda='pedra')), ('pedra_flutuante', 'ilha', dict(topo='chao_a', r=0.9)),
        ('geiser', 'geiser', {}), ('braseiro', 'braseiro', {}), ('parede_obsidiana', 'parede', dict(m='obsidiana')),
    ]),
    8: dict(tex={
        'chao_a': T('#7f708a', '#625565', '#9babb2', tabuas=('#3e3546', 4)), 'chao_b': T('#45293f', '#4c3e24', '#3e3546'),
        'chao_c': T('#625565', '#7f708a', tabuas=('#3e3546', 8)), 'chao_d': T('#3e3546', '#625565', manchas=[('#6b3e75', 4, 0)]),
        'pedra': T('#625565', '#3e3546', '#7f708a'), 'pedra_b': T('#7f708a', '#625565', manchas=[('#547e64', 6, 1)]),
        'casca': T('#2e222f', '#3e3546', '#45293f'), 'minerio': T('#625565', '#3e3546', manchas=[('#a884f3', 6, 1), ('#eaaded', 3, 0)]),
        'ebano': T('#2e222f', '#45293f'), 'rosa': T('#2e222f', '#45293f', manchas=[('#831c5d', 5, 0)]),
        'telhado': T('#3e3546', '#2e222f', tabuas=('#45293f', 4)),
    }, pecas=[
        ('calcada', 'chao', {}), ('terra_cemiterio', 'chao', dict(m='chao_b')), ('chao_castelo_1', 'chao', dict(m='chao_c')),
        ('chao_castelo_2', 'chao', dict(m='chao_d')), ('muralha', 'parede', dict(alto=4.0, topo='pedra')),
        ('parede_pedra_1', 'parede', {}), ('parede_pedra_2', 'parede', dict(m='pedra_b')),
        ('arvore_negra_1', 'arvore', dict(forma='nua')), ('arvore_negra_2', 'arvore', dict(forma='nua', esc=1.3)),
        ('campa_1', 'campa', {}), ('campa_2', 'campa', dict(tipo=2)), ('campa_3', 'campa', dict(tipo=3)),
        ('minerio_mitril', 'minerio', {}), ('ebano', 'arvore_cortavel', dict(casca='ebano', folhas='casca')),
        ('rosa_negra', 'erva', dict(m='casca', flor='rosa')), ('bau', 'bau', {}), ('lanterna_sagrada', 'lanterna', {}),
        ('cristal', 'cristal_teletransporte', {}), ('porta_medieval', 'moldura', dict(vidro='madeira', alto=2.6, larg=1.4)),
        ('janela_gotica', 'moldura', dict(m='pedra', vidro='vidro_roxo', alto=2.0, larg=0.8)), ('coluna', 'coluna', {}),
        ('grade', 'grade', {}), ('vela_grande', 'vela', {}),
    ]),
    9: dict(tex={
        'nuvem': T('#ffffff', '#c7dcd0'), 'nuvem_b': T('#c7dcd0', '#ffffff', '#8fd3ff'), 'pedra': T('#9babb2', '#7f708a', '#c7dcd0'),
        'chao_a': T('#ffffff', '#c7dcd0', tabuas=('#9babb2', 8)), 'chao_b': T('#c7dcd0', '#ffffff', manchas=[('#f9c22b', 3, 0)]),
        'relva': T('#91db69', '#cddf6c', '#1ebc73'), 'casca': T('#c7dcd0', '#9babb2'), 'folhas': T('#ffffff', '#c7dcd0', '#8fd3ff'),
        'minerio': T('#9babb2', '#c7dcd0', manchas=[('#f9c22b', 6, 1), ('#fbff86', 3, 0)]), 'ouro': T('#f9c22b', '#f79617', '#fbff86'),
        'tecido': T('#ea4f36', '#f9c22b', riscas=('#ffffff', 4)), 'corrente': T('#9babb2', '#625565'),
    }, pecas=[
        ('nuvem_solida', 'nuvem', {}), ('nuvem_fraca', 'nuvem', dict(m='nuvem_b', fraca=True)),
        ('rocha_flutuante_1', 'ilha', dict(topo='relva')), ('rocha_flutuante_2', 'ilha', dict(topo='relva', r=0.7, s=3)),
        ('rocha_flutuante_3', 'ilha', dict(topo='chao_a', r=1.3, s=5)), ('marmore_1', 'chao', {}), ('marmore_2', 'chao', dict(m='chao_b')),
        ('relva_celeste', 'chao', dict(m='relva')), ('coluna_branca_1', 'coluna', {}), ('coluna_branca_2', 'coluna', dict(partida=True)),
        ('arvore_nuvem_1', 'arvore', {}), ('arvore_nuvem_2', 'arvore', dict(esc=1.3, s=7)), ('minerio_oricalco', 'minerio', {}),
        ('madeira_nuvem', 'arvore_cortavel', {}), ('flor_do_vento', 'erva', dict(m='relva', flor='ouro')), ('bau', 'bau', {}),
        ('braseiro_dourado', 'braseiro', dict(m='ouro')), ('cristal', 'cristal_teletransporte', {}),
        ('ponte_corrente', 'ponte', dict(m='pedra', corda='corrente')), ('ponte_luz', 'ponte', dict(m='luz', corda='luz')),
        ('balao', 'balao', {}), ('corrente_ar', 'pico', dict(m='nuvem_b', baixo=True, alto=2.5)),
    ]),
    10: dict(tex={
        'pedra': T('#2e222f', '#45293f', '#3e3546'), 'chao_a': T('#323353', '#2e222f', manchas=[('#ffffff', 4, 0), ('#a884f3', 3, 0)]),
        'vidro_chao': T('#8fd3ff', '#4d9be6', '#c7dcd0'), 'chao_b': T('#3e3546', '#2e222f'),
        'casca': T('#6b3e75', '#45293f'), 'folhas': T('#a884f3', '#905ea9', '#eaaded'),
        'minerio': T('#323353', '#2e222f', manchas=[('#ffffff', 5, 0), ('#8fd3ff', 4, 1)]), 'lotus': T('#eaaded', '#a884f3'),
    }, pecas=[
        ('ilha_vazio_1', 'ilha', dict(topo='chao_b')), ('ilha_vazio_2', 'ilha', dict(topo='chao_b', r=0.7, s=3)),
        ('ilha_vazio_3', 'ilha', dict(topo='chao_b', r=1.3, s=5)), ('caminho_estrelas', 'chao', dict(m='chao_a', alto=0.1)),
        ('chao_vidro', 'chao', dict(m='vidro_chao', alto=0.1)), ('chao_luz_azul', 'placa_luz', {}),
        ('espelho', 'moldura', dict(m='metal', vidro='vidro')), ('estante', 'estante', {}), ('relogio_sol', 'relogio_sol', {}),
        ('ancora_luz', 'ancora', {}), ('fragmento_estelar', 'minerio', {}), ('madeira_tempo', 'arvore_cortavel', {}),
        ('lotus', 'erva', dict(m='folhas', flor='lotus')), ('bau', 'bau', {}), ('cristal', 'cristal_teletransporte', {}),
        ('ponte_luz', 'ponte', dict(m='luz_azul', corda='luz_azul')), ('portal_gravidade', 'portal', {}),
        ('janela_sistema', 'janela_sistema', {}),
    ]),
}


def materiais(n, pasta_tex):
    spec = dict(BASE_TEX)
    spec.update(REGIOES[n]['tex'])
    M = {}
    for i, (nome, (cores, kw)) in enumerate(spec.items()):
        M[nome] = B.material(f'r{n:02d}_{nome}', B.textura_ruido(f'r{n:02d}_{nome}', cores, pasta_tex, 100 * n + i, **kw))
    for nome, (base, em) in LUZES.items():
        M[nome] = B.material(f'r{n:02d}_{nome}', os.path.join(pasta_tex, f'r{n:02d}_{base}.png'), emissao=em)
    for nome, (cor, em) in CORES_LUZ.items():
        M[nome] = B.material(f'r{n:02d}_{nome}', cor=cor, emissao=em)
    M['vidro_roxo'] = B.material(f'r{n:02d}_vidro_roxo', cor='#a884f3', emissao=0.8)
    # luzes a partir de texturas da região (cristais coloridos, lava)
    for nome in ('cristal_v', 'cristal_r', 'lava'):
        if nome in M:
            M[nome + '_luz'] = B.material(f'r{n:02d}_{nome}_luz', os.path.join(pasta_tex, f'r{n:02d}_{nome}.png'), emissao=1.6)
    for chave in ('chao_b', 'chao_c', 'folhas', 'casca', 'gelo', 'neve', 'coral', 'alga', 'agua', 'osso'):
        M.setdefault(chave, M.get('chao_a', M['pedra']) if chave.startswith('chao') else M['pedra'])
    return M


def gerar(n, previa=False):
    B.limpar()
    pasta = os.path.join('arte', 'regioes', PASTAS[n], 'kit')
    M = materiais(n, os.path.join(pasta, 'texturas'))
    objetos = []
    for i, (nome, molde, kw) in enumerate(REGIOES[n]['pecas']):
        p = B.Peca(f'r{n:02d}_{nome}')
        MOLDES[molde](p, M, **kw)
        objetos.append(p.criar((i % 8) * 5.0 - 17.5, (i // 8) * 5.0 - 7.5))
    B.exportar(objetos, pasta, f'r{n:02d}_kit.blend')
    if previa:
        B.previa(os.path.join(pasta, f'r{n:02d}_kit.png'), distancia=42, alvo=(0, 0, 0))
    print('ok', PASTAS[n], len(objetos), 'peças')


if __name__ == '__main__':
    regs = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(REGIOES)
    for n in regs:
        gerar(n, '--previa' in sys.argv)
