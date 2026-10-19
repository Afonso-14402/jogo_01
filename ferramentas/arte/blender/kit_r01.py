"""Kit de peças 3D da Região 1 (Floresta): chão, paredes, passagens, natureza, recolha, objetos e decoração.
Lista: docs/ARTE.md (secção 6) e docs/regioes/r01_floresta.md (secção 12).
Saída: arte/regioes/r01_floresta/kit/ (um .glb por peça + r01_kit.blend + texturas/).

Uso: blenv/bin/python ferramentas/arte/blender/kit_r01.py [previa.png]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B

PASTA = os.path.join('arte', 'regioes', 'r01_floresta', 'kit')
TEX = os.path.join(PASTA, 'texturas')


def texturas():
    t = {}
    t['relva'] = B.textura_ruido('r01_relva', ['#239063', '#1ebc73', '#165a4c', '#91db69'], TEX, 1)
    t['relva_flores'] = B.textura_ruido('r01_relva_flores', ['#239063', '#1ebc73', '#165a4c', '#91db69'], TEX, 2,
                                        manchas=[('#f9c22b', 4, 0), ('#ffffff', 4, 0), ('#ed8099', 3, 0), ('#4d9be6', 2, 0)])
    t['terra'] = B.textura_ruido('r01_terra', ['#694f62', '#966c6c', '#4c3e24', '#ab947a'], TEX, 3)
    t['caminho'] = B.textura_ruido('r01_caminho', ['#966c6c', '#ab947a', '#694f62'], TEX, 4, manchas=[('#9babb2', 10, 1), ('#7f708a', 6, 1)])
    t['pedra'] = B.textura_ruido('r01_pedra', ['#7f708a', '#625565', '#9babb2', '#3e3546'], TEX, 5, manchas=[('#547e64', 5, 1)])
    t['casca'] = B.textura_ruido('r01_casca', ['#694f62', '#4c3e24', '#966c6c'], TEX, 6, riscas=('#45293f', 14))
    t['folhas'] = B.textura_ruido('r01_folhas', ['#1ebc73', '#239063', '#91db69', '#165a4c'], TEX, 7, manchas=[('#cddf6c', 6, 0)])
    t['pinho'] = B.textura_ruido('r01_pinho', ['#239063', '#165a4c', '#374e4a', '#1ebc73'], TEX, 8)
    t['madeira'] = B.textura_ruido('r01_madeira', ['#966c6c', '#ab947a', '#694f62'], TEX, 9, tabuas=('#45293f', 6))
    t['minerio'] = B.textura_ruido('r01_minerio_cobre', ['#7f708a', '#625565', '#9babb2'], TEX, 10, manchas=[('#cd683d', 6, 1), ('#f57d4a', 4, 0)])
    t['cogumelo'] = B.textura_ruido('r01_cogumelo', ['#b33831', '#ea4f36', '#6e2727'], TEX, 11, manchas=[('#ffffff', 5, 2)])
    t['branco'] = B.textura_ruido('r01_branco', ['#c7dcd0', '#ffffff', '#9babb2'], TEX, 12)
    t['cristal'] = B.textura_ruido('r01_cristal', ['#4d9be6', '#8fd3ff', '#4d65b4', '#ffffff'], TEX, 13)
    t['fogo'] = B.textura_ruido('r01_fogo', ['#f79617', '#fb6b1d', '#f9c22b', '#fbff86'], TEX, 14)
    t['metal'] = B.textura_ruido('r01_metal', ['#cd683d', '#9e4539', '#f57d4a'], TEX, 15)
    t['colmeia'] = B.textura_ruido('r01_colmeia', ['#f9c22b', '#f79617', '#fbb954'], TEX, 16, tabuas=('#9e4539', 4))
    t['musgo'] = B.textura_ruido('r01_musgo', ['#547e64', '#374e4a', '#92a984'], TEX, 17)
    return {k: B.material('r01_' + k, v) for k, v in t.items()}


def pecas(M):
    P = []

    def nova(nome):
        p = B.Peca('r01_' + nome)
        P.append(p)
        return p

    # ---- chão (2x2 m, 0,2 m de espessura) ----
    for nome, m in (('chao_1', 'relva'), ('chao_2', 'relva_flores'), ('chao_3', 'terra'), ('caminho', 'caminho')):
        p = nova(nome)
        p.caixa(M[m], 0, 0, 0, 2, 2, 0.2)
    p = nova('borda')
    p.caixa(M['terra'], 0, 0, -1.0, 2, 2, 1.0)
    p.caixa(M['relva'], 0, 0, 0, 2, 2, 0.2)
    # ---- paredes, rampas e escadas ----
    p = nova('parede')
    p.caixa(M['pedra'], 0, 0, 0, 2, 0.8, 3)
    p.caixa(M['musgo'], 0, 0, 3, 2.1, 0.9, 0.2)
    p = nova('canto')
    p.caixa(M['pedra'], -0.6, 0, 0, 0.8, 2, 3)
    p.caixa(M['pedra'], 0.2, -0.6, 0, 1.6, 0.8, 3)
    p.caixa(M['musgo'], -0.2, -0.2, 3, 1.7, 1.7, 0.2)
    p = nova('rampa')
    p.rampa(M['relva'], 2, 2, 1.0)
    p = nova('escada')
    for i in range(4):
        p.caixa(M['pedra'], 0, -0.75 + i * 0.5, 0, 2, 0.5, 0.25 * (i + 1))
    # ---- passagens ----
    p = nova('ponte')
    p.caixa(M['madeira'], 0, 0, 0.3, 2, 4, 0.15)
    for x in (-0.9, 0.9):
        for y in (-1.8, 0, 1.8):
            p.cilindro(M['casca'], x, y, 0, 0.1, 0.1, 1.2, 6)
        p.caixa(M['casca'], x, 0, 1.05, 0.12, 4, 0.12)
    p = nova('arco')
    p.caixa(M['pedra'], -1.0, 0, 0, 0.6, 0.8, 2.6)
    p.caixa(M['pedra'], 1.0, 0, 0, 0.6, 0.8, 2.6)
    p.caixa(M['pedra'], 0, 0, 2.6, 2.6, 0.8, 0.6)
    p.caixa(M['musgo'], -0.4, 0, 3.2, 1.2, 0.9, 0.15)
    p = nova('escada_andar')
    for i in range(5):
        p.caixa(M['pedra'], 0, -1 + i * 0.5, 0, 2.4 - i * 0.2, 0.5, 0.3 * (i + 1))
    for x in (-1.5, 1.5):
        p.cilindro(M['pedra'], x, 1.2, 0, 0.35, 0.3, 2.8, 8)
        p.bola(M['cristal'], x, 1.2, 3.1, 0.25, 0.25, 0.4, 0)
    # ---- natureza ----
    p = nova('arvore_1')   # carvalho
    p.cilindro(M['casca'], 0, 0, 0, 0.45, 0.32, 2.6, 7)
    for (x, y, z, r) in ((0, 0, 3.4, 1.6), (0.9, 0.4, 2.9, 1.1), (-0.9, -0.3, 3.0, 1.2), (0.2, -0.8, 3.9, 1.0)):
        p.bola(M['folhas'], x, y, z, r, r, r * 0.85, 1, semente=int(x * 10 + y * 7), irregular=0.12)
    p = nova('arvore_2')   # pinheiro
    p.cilindro(M['casca'], 0, 0, 0, 0.3, 0.2, 1.4, 6)
    for i, (r, z) in enumerate(((1.6, 1.0), (1.25, 2.2), (0.85, 3.3))):
        p.cilindro(M['pinho'], 0, 0, z, r, 0.05, 1.7, 7)
    p = nova('arvore_3')   # árvore grande redonda
    p.cilindro(M['casca'], 0, 0, 0, 0.7, 0.45, 3.4, 8)
    p.cilindro(M['casca'], 0.6, 0, 0, 0.35, 0.05, 0.6, 5, rot=(0, 0.6, 0))
    p.bola(M['folhas'], 0, 0, 4.6, 2.4, 2.2, 1.8, 1, semente=33, irregular=0.1)
    for i, (r, h) in enumerate(((0.9, 0.6), (0.7, 0.45), (0.5, 0.35))):
        p = nova(f'rocha_{i + 1}')
        p.bola(M['pedra'], 0, 0, h * 0.8, r, r * 0.85, h, 1, semente=50 + i, irregular=0.18)
    for i, r in enumerate((0.7, 0.5)):
        p = nova(f'arbusto_{i + 1}')
        p.bola(M['folhas'], 0, 0, r * 0.7, r, r, r * 0.75, 1, semente=60 + i, irregular=0.15)
        p.bola(M['folhas'], r * 0.6, 0.2, r * 0.5, r * 0.6, r * 0.6, r * 0.5, 1, semente=70 + i, irregular=0.15)
    # ---- recolha ----
    p = nova('minerio_cobre')
    p.bola(M['minerio'], 0, 0, 0.45, 0.75, 0.65, 0.6, 1, semente=80, irregular=0.2)
    p = nova('arvore_cortavel')
    p.cilindro(M['casca'], 0, 0, 0, 0.3, 0.22, 1.8, 7)
    p.bola(M['folhas'], 0, 0, 2.4, 1.1, 1.1, 0.95, 1, semente=81, irregular=0.12)
    p = nova('toco')
    p.cilindro(M['casca'], 0, 0, 0, 0.35, 0.3, 0.4, 7)
    p = nova('erva')
    for i in range(5):
        a = i * 1.25
        p.cilindro(M['folhas'], math.cos(a) * 0.15, math.sin(a) * 0.15, 0, 0.06, 0.01, 0.45, 3, rot=(math.cos(a) * 0.3, math.sin(a) * 0.3, 0))
    # ---- objetos ----
    p = nova('bau')
    p.caixa(M['madeira'], 0, 0, 0, 0.9, 0.6, 0.5)
    p.caixa(M['madeira'], 0, 0, 0.5, 0.92, 0.62, 0.22)
    for x in (-0.3, 0.3):
        p.caixa(M['metal'], x, 0, 0, 0.08, 0.64, 0.74)
    p.caixa(M['metal'], 0, -0.31, 0.38, 0.12, 0.04, 0.15)
    p = nova('fogueira')
    for i in range(7):
        a = i / 7 * math.tau
        p.bola(M['pedra'], math.cos(a) * 0.55, math.sin(a) * 0.55, 0.1, 0.18, 0.15, 0.13, 0, semente=90 + i)
    p.cilindro(M['casca'], 0, 0, 0.08, 0.08, 0.08, 0.9, 5, rot=(0, math.radians(90), 0.6))
    p.cilindro(M['casca'], 0, 0, 0.08, 0.08, 0.08, 0.9, 5, rot=(0, math.radians(90), -0.6))
    M['fogo_luz'] = B.material('r01_fogo_luz', os.path.join(TEX, 'r01_fogo.png'), emissao=3.0)
    p.cilindro(M['fogo_luz'], 0, 0, 0.1, 0.3, 0.02, 0.7, 6)
    p = nova('cristal_teletransporte')
    p.cilindro(M['pedra'], 0, 0, 0, 0.7, 0.6, 0.3, 8)
    M['cristal_luz'] = B.material('r01_cristal_luz', os.path.join(TEX, 'r01_cristal.png'), emissao=1.5)
    p.cilindro(M['cristal_luz'], 0, 0, 0.3, 0.35, 0.0, 1.6, 6)
    p.cilindro(M['cristal_luz'], 0, 0, 0.3, 0.35, 0.35, 0.25, 6)
    # ---- decoração ----
    p = nova('cogumelo_gigante')
    p.cilindro(M['branco'], 0, 0, 0, 0.45, 0.35, 2.2, 8)
    p.bola(M['cogumelo'], 0, 0, 2.3, 1.8, 1.8, 0.8, 1, semente=100)
    p = nova('tronco_caido')
    p.cilindro(M['casca'], 0, 0, 0.45, 0.45, 0.4, 3.2, 8, rot=(0, math.radians(90), 0.2))
    p.bola(M['musgo'], 0.4, 0.1, 0.85, 0.6, 0.4, 0.2, 0, semente=101)
    p = nova('flores')
    for i, (x, y, c) in enumerate(((-0.3, 0.1, '#f9c22b'), (0.25, -0.2, '#ed8099'), (0.05, 0.3, '#ffffff'), (0.3, 0.25, '#4d9be6'))):
        p.cilindro(M['folhas'], x, y, 0, 0.03, 0.03, 0.35, 4)
        p.bola(B.material('r01_flor_' + c, cor=c), x, y, 0.4, 0.1, 0.1, 0.07, 0)
    p = nova('colmeia')
    p.cilindro(M['casca'], 0, 0, 0, 0.12, 0.12, 1.2, 5)
    p.bola(M['colmeia'], 0, 0, 1.5, 0.45, 0.45, 0.55, 1, semente=102)
    p = nova('lanterna_pedra')
    p.cilindro(M['pedra'], 0, 0, 0, 0.25, 0.2, 1.0, 6)
    p.caixa(M['pedra'], 0, 0, 1.0, 0.5, 0.5, 0.1)
    p.bola(B.material('r01_lume', cor='#fbff86', emissao=2.0), 0, 0, 1.25, 0.15, 0.15, 0.15, 0)
    p.caixa(M['pedra'], 0, 0, 1.45, 0.55, 0.55, 0.12)
    return P


if __name__ == '__main__':
    B.limpar()
    M = texturas()
    lista = pecas(M)
    objetos = []
    cols = 8
    for i, p in enumerate(lista):
        x = (i % cols) * 5.0 - 17.5
        y = (i // cols) * 5.0 - 7.5
        objetos.append(p.criar(x, y))
    B.exportar(objetos, PASTA, 'r01_kit.blend')
    print('ok', len(objetos), 'peças')
    if len(sys.argv) > 1:
        B.previa(sys.argv[1], distancia=42, alvo=(0, 0, 0))
