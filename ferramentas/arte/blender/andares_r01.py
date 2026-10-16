"""Peças especiais dos andares 1–10 (linha "Peças especiais" de cada andar em docs/regioes/r01_floresta.md).
Saída: arte/regioes/r01_floresta/andares/ (a01_moinho.glb, ...).

Uso: blenv/bin/python ferramentas/arte/blender/andares_r01.py [previa.png]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B
import kit_r01 as K

PASTA = os.path.join('arte', 'regioes', 'r01_floresta', 'andares')


def mats():
    M = K.texturas()
    tex = os.path.join(K.TEX)
    M['agua'] = B.material('r01_agua', B.textura_ruido('r01_agua', ['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'], tex, 30))
    M['lama'] = B.material('r01_lama', B.textura_ruido('r01_lama', ['#4c3e24', '#694f62', '#45293f'], tex, 31))
    M['tecido'] = B.material('r01_tecido', B.textura_ruido('r01_tecido', ['#ab947a', '#c7dcd0', '#966c6c'], tex, 32))
    M['favo'] = B.material('r01_favo', B.textura_ruido('r01_favo', ['#f9c22b', '#f79617', '#fbff86'], tex, 33, manchas=[('#9e4539', 10, 0)]))
    M['marmore'] = B.material('r01_marmore', B.textura_ruido('r01_marmore', ['#ffffff', '#c7dcd0', '#9babb2'], tex, 34))
    M['casca_branca'] = B.material('r01_casca_branca', B.textura_ruido('r01_casca_branca', ['#c7dcd0', '#ffffff', '#9babb2'], tex, 35, riscas=('#7f708a', 8)))
    M['folhas_brancas'] = B.material('r01_folhas_brancas', B.textura_ruido('r01_folhas_brancas', ['#c7dcd0', '#ffffff', '#8ff8e2'], tex, 36))
    M['simbolos'] = B.material('r01_simbolos', B.textura_ruido('r01_simbolos', ['#7f708a', '#625565', '#9babb2'], tex, 37, manchas=[('#4d9be6', 6, 0)]), emissao=0.4)
    M['salgueiro'] = B.material('r01_salgueiro', B.textura_ruido('r01_salgueiro', ['#92a984', '#547e64', '#b2ba90'], tex, 38))
    M['luz'] = B.material('r01_luz_lanterna', cor='#fbff86', emissao=3.0)
    M['luz_azul'] = B.material('r01_luz_azul', cor='#8fd3ff', emissao=2.5)
    for c in ('#ea4f36', '#f9c22b', '#4d9be6', '#ed8099', '#a884f3'):
        M['flor' + c] = B.material('r01_petala' + c, cor=c)
    return M


def pecas(M):
    P = []

    def nova(nome):
        p = B.Peca(nome)
        P.append(p)
        return p

    # ---------- Andar 1 — Prado do Despertar ----------
    p = nova('a01_moinho')
    p.cilindro(M['pedra'], 0, 0, 0, 2.0, 1.5, 7, 8)
    p.cilindro(M['madeira'], 0, 0, 7, 2.2, 0.05, 2.5, 8)
    p.caixa(M['madeira'], 0, -2.2, 5.5, 0.4, 0.6, 0.4)
    for a in range(4):          # pás (no jogo rodam à volta do eixo y)
        ang = a * math.pi / 2 + 0.3
        p.caixa(M['tecido'], math.cos(ang) * 2.4, -2.5, 5.7 + math.sin(ang) * 2.4 - 0.1, 0.9 if a % 2 == 0 else 4.0, 0.08, 4.0 if a % 2 == 0 else 0.9)
    p.caixa(M['porta'] if 'porta' in M else M['madeira'], 0, -1.9, 0, 1.0, 0.2, 2.0)
    p = nova('a01_circulo_pedras')
    for i in range(8):
        a = i / 8 * math.tau
        p.caixa(M['pedra'], math.cos(a) * 4, math.sin(a) * 4, 0, 0.8, 0.6, 2.2 + (i % 3) * 0.5, rot_z=a)
    p.bola(M['pedra'], 0, 0, 0.2, 1.2, 1.2, 0.35, 1, semente=3)
    p = nova('a01_erva_alta')
    for i in range(12):
        a = i * 2.4
        r = 0.2 + (i % 4) * 0.12
        p.cilindro(M['folhas'], math.cos(a) * r, math.sin(a) * r, 0, 0.07, 0.01, 1.0 + (i % 3) * 0.3, 3, rot=(math.cos(a) * 0.25, math.sin(a) * 0.25, 0))
    # ---------- Andar 2 — Bosque dos Sussurros ----------
    p = nova('a02_arvore_oca')
    p.cilindro(M['casca'], 0, 0, 0, 1.4, 1.0, 5, 9)
    p.caixa(M['lama'], 0, -1.3, 0, 1.0, 0.4, 1.6)
    p.bola(M['folhas'], 0, 0, 6.0, 2.6, 2.4, 2.0, 1, semente=4, irregular=0.12)
    p = nova('a02_arvore_sussurrante')
    p.cilindro(M['casca'], 0, 0, 0, 1.0, 0.8, 5, 8)
    for x in (-0.35, 0.35):
        p.bola(M['luz'], x, -0.85, 3.2, 0.15, 0.08, 0.2, 0)
    p.caixa(M['lama'], 0, -0.85, 2.4, 0.5, 0.1, 0.15)
    p.bola(M['folhas'], 0, 0, 5.8, 2.4, 2.4, 1.8, 1, semente=5, irregular=0.12)
    p = nova('a02_tenda')
    p.telhado(M['tecido'], 0, 0, 0, 3.0, 4.0, 2.4, beiral=0.0)
    p.caixa(M['casca'], 0, -2.0, 0, 0.1, 0.1, 2.6)
    p.caixa(M['casca'], 0, 2.0, 0, 0.1, 0.1, 2.6)
    p = nova('a02_serracao')
    p.caixa(M['madeira'], 0, 0, 0, 5, 3, 0.9)
    p.cilindro(M['metal'], 0, -0.5, 1.4, 0.9, 0.9, 0.08, 12, rot=(math.radians(90), 0, 0))
    p.cilindro(M['casca'], -1.8, 1.0, 0.9, 0.35, 0.35, 3.5, 7, rot=(0, math.radians(90), 0))
    for x, y in ((-2.4, -1.4), (2.4, -1.4), (-2.4, 1.4), (2.4, 1.4)):
        p.cilindro(M['casca'], x, y, 0, 0.15, 0.15, 2.5, 6)
    p.telhado(M['madeira'], 0, 0, 2.5, 5.0, 3.0, 1.0)
    # ---------- Andar 3 — Ribeiro Cristalino ----------
    p = nova('a03_cascata')
    p.caixa(M['pedra'], 0, 0.8, 0, 6, 2.0, 5)
    p.caixa(M['agua'], 0, -0.3, 0, 2.6, 0.3, 5.1)
    p.cilindro(M['agua'], 0, -1.5, 0, 2.5, 2.5, 0.2, 10)
    p = nova('a03_comporta')
    p.caixa(M['pedra'], -1.6, 0, 0, 0.6, 1.2, 2.5)
    p.caixa(M['pedra'], 1.6, 0, 0, 0.6, 1.2, 2.5)
    p.caixa(M['madeira'], 0, 0, 0.3, 2.6, 0.25, 1.8)
    p.cilindro(M['madeira'], 2.4, -0.7, 1.4, 0.6, 0.6, 0.15, 8, rot=(math.radians(90), 0, 0))
    p = nova('a03_ponte_tabuas')
    for i in range(7):
        p.caixa(M['madeira'], 0, -1.8 + i * 0.6, 0.25, 1.6, 0.5, 0.1, rot_z=(i % 2) * 0.05)
    for y in (-1.8, 1.8):
        for x in (-0.8, 0.8):
            p.cilindro(M['casca'], x, y, -0.5, 0.1, 0.1, 0.9, 5)
    p = nova('a03_rocha_rio')
    p.bola(M['pedra'], 0, 0, 0.25, 1.0, 0.8, 0.4, 1, semente=7, irregular=0.1)
    p.bola(M['musgo'], -0.2, 0.1, 0.55, 0.5, 0.4, 0.12, 0, semente=8)
    # ---------- Andar 4 — Clareira dos Cogumelos ----------
    for i, (h, r, cor) in enumerate(((3.5, 2.4, 'cogumelo'), (5.0, 3.0, 'cogumelo'), (2.5, 1.8, 'folhas'))):
        p = nova(f'a04_cogumelo_gigante_{i + 1}')
        p.cilindro(M['branco'], 0, 0, 0, 0.5 + i * 0.1, 0.4, h, 8)
        p.bola(M[cor], 0, 0, h, r, r, r * 0.4, 1, semente=10 + i)
    p = nova('a04_cogumelo_trampolim')
    p.cilindro(M['branco'], 0, 0, 0, 0.4, 0.35, 1.0, 8)
    p.bola(B.material('r01_trampolim', cor='#ed8099'), 0, 0, 1.0, 1.4, 1.4, 0.45, 1, semente=13)
    p = nova('a04_anel_cogumelos')
    for i in range(10):
        a = i / 10 * math.tau
        x, y = math.cos(a) * 2.5, math.sin(a) * 2.5
        p.cilindro(M['branco'], x, y, 0, 0.08, 0.08, 0.3, 5)
        p.bola(M['cogumelo'], x, y, 0.32, 0.22, 0.22, 0.12, 0)
    p = nova('a04_cogumelo_oco')
    p.cilindro(M['branco'], 0, 0, 0, 1.6, 1.4, 3.0, 10)
    p.caixa(M['lama'], 0, -1.45, 0, 1.0, 0.4, 1.8)
    p.bola(M['cogumelo'], 0, 0, 3.0, 3.0, 3.0, 1.2, 1, semente=14)
    # ---------- Andar 5 — Toca do Javali-Rei ----------
    p = nova('a05_toca')
    p.bola(M['terra'], 0, 0, 0, 2.0, 1.6, 1.4, 1, semente=15, irregular=0.1)
    p.caixa(M['lama'], 0, -1.4, 0, 1.4, 0.6, 1.0)
    p = nova('a05_arvore_fruto')
    p.cilindro(M['casca'], 0, 0, 0, 0.3, 0.25, 2.0, 7)
    p.bola(M['folhas'], 0, 0, 2.7, 1.4, 1.4, 1.1, 1, semente=16, irregular=0.1)
    for (x, y, z) in ((0.8, -0.8, 2.4), (-0.9, -0.5, 2.8), (0.2, -1.2, 3.0)):
        p.bola(M['flor#ea4f36'], x, y, z, 0.15, 0.15, 0.15, 0)
    p = nova('a05_lamacal')
    p.cilindro(M['lama'], 0, 0, 0, 3.0, 3.0, 0.08, 12)
    p = nova('a05_cerca_arena')
    for i in range(5):
        p.cilindro(M['casca'], -2 + i, 0, 0, 0.18, 0.15, 1.6 + (i % 2) * 0.2, 6)
    p.caixa(M['casca'], 0, 0, 0.9, 4.4, 0.15, 0.15)
    # ---------- Andar 6 — Colinas Floridas ----------
    p = nova('a06_colmeia_gigante')
    p.bola(M['colmeia'], 0, 0, 1.6, 1.4, 1.4, 1.7, 1, semente=17)
    p.caixa(M['lama'], 0, -1.3, 1.0, 0.5, 0.3, 0.5)
    p = nova('a06_favo')
    p.cilindro(M['favo'], 0, 0, 0, 1.0, 1.0, 0.3, 6)
    p = nova('a06_estatua_jardim')
    p.caixa(M['marmore'], 0, 0, 0, 1.0, 1.0, 0.6)
    p.cilindro(M['marmore'], 0, 0, 0.6, 0.35, 0.3, 1.2, 8)
    p.bola(M['marmore'], 0, 0, 2.05, 0.3, 0.3, 0.32, 1)
    for i, c in enumerate(('#ea4f36', '#f9c22b', '#4d9be6')):
        p = nova(f'a06_flor_grande_{i + 1}')
        p.cilindro(M['folhas'], 0, 0, 0, 0.1, 0.08, 2.0, 5)
        for k in range(5):
            a = k / 5 * math.tau
            p.bola(M['flor' + c], math.cos(a) * 0.5, math.sin(a) * 0.5, 2.05, 0.4, 0.4, 0.12, 0)
        p.bola(M['flor#f9c22b' if c != '#f9c22b' else 'flor#ea4f36'], 0, 0, 2.1, 0.25, 0.25, 0.15, 0)
    # ---------- Andar 7 — Floresta Antiga ----------
    p = nova('a07_tronco_gigante')
    p.cilindro(M['casca'], 0, 0, 0, 4.0, 3.2, 14, 12)
    for a in range(5):
        ang = a / 5 * math.tau
        p.cilindro(M['casca'], math.cos(ang) * 3.5, math.sin(ang) * 3.5, 0, 0.9, 0.3, 2.5, 6, rot=(math.sin(ang) * 0.6, -math.cos(ang) * 0.6, 0))
    p.bola(M['folhas'], 0, 0, 16, 7, 7, 4, 1, semente=18, irregular=0.08)
    p = nova('a07_raiz_ponte')
    p.cilindro(M['casca'], 0, 0, 1.2, 0.7, 0.6, 8, 8, rot=(math.radians(90), 0, 0))
    p.caixa(M['musgo'], 0, 0, 1.8, 0.8, 7, 0.1)
    p = nova('a07_casa_arvore')
    p.caixa(M['madeira'], 0, 0, 0, 3.5, 3.5, 0.3)
    p.caixa(M['madeira'], 0, 0, 0.3, 3.0, 3.0, 2.4)
    p.telhado(M['folhas'], 0, 0, 2.7, 3.0, 3.0, 1.6)
    p.caixa(M['lama'], 0, -1.55, 0.3, 0.9, 0.1, 1.8)
    p = nova('a07_elevador_cesto')
    p.cilindro(M['madeira'], 0, 0, 0, 0.9, 1.0, 1.0, 8)
    for a in range(4):
        ang = a * math.pi / 2
        p.cilindro(M['tecido'], math.cos(ang) * 0.8, math.sin(ang) * 0.8, 1.0, 0.03, 0.03, 4.0, 3)
    p = nova('a07_poco_luz')
    p.cilindro(M['pedra'], 0, 0, 0, 1.2, 1.2, 0.9, 10)
    p.cilindro(M['luz_azul'], 0, 0, 0.6, 0.95, 0.95, 0.35, 10)
    # ---------- Andar 8 — Ruínas Cobertas de Musgo ----------
    p = nova('a08_coluna_partida')
    p.cilindro(M['pedra'], 0, 0, 0, 0.6, 0.55, 3.2, 8)
    p.caixa(M['pedra'], 0, 0, 0, 1.4, 1.4, 0.4)
    p.bola(M['musgo'], 0, 0, 3.2, 0.6, 0.6, 0.25, 0, semente=19)
    p.cilindro(M['pedra'], 1.4, 0.3, 0.55, 0.55, 0.5, 2.0, 8, rot=(0, math.radians(85), 0.4))
    p = nova('a08_estatua_cavaleiro')
    p.caixa(M['pedra'], 0, 0, 0, 1.6, 1.6, 0.8)
    p.caixa(M['pedra'], 0, 0, 0.8, 0.9, 0.6, 1.6)
    p.bola(M['pedra'], 0, 0, 2.7, 0.4, 0.4, 0.45, 1)
    p.caixa(M['pedra'], 0.6, -0.4, 1.2, 0.15, 0.1, 1.8)
    p.caixa(M['pedra'], -0.6, -0.35, 1.0, 0.7, 0.15, 1.0)
    p.bola(M['musgo'], -0.2, 0, 2.9, 0.4, 0.4, 0.15, 0)
    p = nova('a08_portao_ruinas')
    p.caixa(M['pedra'], -2.0, 0, 0, 1.0, 1.0, 4.0)
    p.caixa(M['pedra'], 2.0, 0, 0, 1.0, 1.0, 2.6)
    p.caixa(M['pedra'], -0.8, 0, 3.4, 3.4, 1.0, 0.8, rot_z=0.0)
    p.bola(M['musgo'], -1.5, 0, 4.2, 1.0, 0.6, 0.25, 0)
    p = nova('a08_torre_vigia')
    p.cilindro(M['pedra'], 0, 0, 0, 2.0, 1.8, 8, 8)
    for a in range(8):
        ang = a / 8 * math.tau
        if a % 2 == 0:
            p.caixa(M['pedra'], math.cos(ang) * 1.7, math.sin(ang) * 1.7, 8, 0.6, 0.6, 0.7, rot_z=ang)
    p.caixa(M['lama'], 0, -1.85, 0, 1.0, 0.3, 2.0)
    p = nova('a08_pedra_simbolos')
    p.caixa(M['simbolos'], 0, 0, 0, 1.4, 0.5, 2.2, rot_z=0.1)
    # ---------- Andar 9 — Lago da Névoa ----------
    p = nova('a09_barco_remos')
    p.prisma(M['madeira'], [(0, 1.8), (0.8, 1.0), (0.8, -1.5), (-0.8, -1.5), (-0.8, 1.0)], 0, 0.6)
    p.caixa(M['madeira'], 0, 0, 0.6, 1.4, 0.3, 0.08)
    for s in (-1, 1):
        p.cilindro(M['madeira'], s * 1.1, 0, 0.5, 0.05, 0.05, 2.2, 4, rot=(0, math.radians(70) * s, 0))
    p = nova('a09_cais')
    p.caixa(M['madeira'], 0, 0, 0.6, 2.4, 6, 0.15)
    for x in (-1.1, 1.1):
        for y in (-2.8, 0, 2.8):
            p.cilindro(M['casca'], x, y, -0.8, 0.12, 0.12, 1.6, 6)
    p = nova('a09_salgueiro')
    p.cilindro(M['casca'], 0, 0, 0, 0.6, 0.4, 3.5, 8)
    p.bola(M['salgueiro'], 0, 0, 4.0, 2.8, 2.8, 1.2, 1, semente=20)
    for a in range(10):
        ang = a / 10 * math.tau
        p.cilindro(M['salgueiro'], math.cos(ang) * 2.4, math.sin(ang) * 2.4, 1.2, 0.18, 0.1, 2.8, 4)
    p = nova('a09_sino_barco')
    p.cilindro(M['madeira'], 0, 0, 0, 0.08, 0.08, 2.4, 5)
    p.caixa(M['madeira'], 0.3, 0, 2.3, 0.7, 0.1, 0.1)
    p.cilindro(M['metal'], 0.55, 0, 1.75, 0.25, 0.12, 0.4, 8)
    p = nova('a09_templo')
    p.caixa(M['marmore'], 0, 0, 0, 5, 5, 0.6)
    for x in (-1.8, 1.8):
        for y in (-1.8, 1.8):
            p.cilindro(M['marmore'], x, y, 0.6, 0.3, 0.3, 3.0, 8)
    p.caixa(M['marmore'], 0, 0, 3.6, 4.6, 4.6, 0.4)
    p.cilindro(M['marmore'], 0, 0, 4.0, 2.6, 0.2, 1.6, 4, rot=(0, 0, math.radians(45)))
    # ---------- Andar 10 — Coração da Floresta ----------
    p = nova('a10_arvore_mae')
    p.cilindro(M['casca'], 0, 0, 0, 6.0, 4.5, 18, 14)
    for a in range(7):
        ang = a / 7 * math.tau
        p.cilindro(M['casca'], math.cos(ang) * 5.5, math.sin(ang) * 5.5, 0, 1.4, 0.4, 3.5, 6, rot=(math.sin(ang) * 0.7, -math.cos(ang) * 0.7, 0))
    for (x, y, z, r) in ((0, 0, 22, 9), (6, 2, 19, 6), (-6, -1, 19.5, 6.5), (1, -6, 20, 5.5), (-1, 6, 20, 5.5)):
        p.bola(M['folhas'], x, y, z, r, r, r * 0.7, 1, semente=int(x + y + z), irregular=0.08)
    for (x, y, z) in ((3, -5.5, 8), (-2.5, -5.2, 12), (0, -5.0, 5)):
        p.bola(M['luz'], x, y, z, 0.35, 0.2, 0.35, 0)
    p = nova('a10_lanterna_pedra')
    p.cilindro(M['pedra'], 0, 0, 0, 0.3, 0.25, 1.2, 6)
    p.caixa(M['pedra'], 0, 0, 1.2, 0.7, 0.7, 0.12)
    p.bola(M['luz'], 0, 0, 1.5, 0.18, 0.18, 0.2, 0)
    p.cilindro(M['pedra'], 0, 0, 1.7, 0.55, 0.05, 0.6, 4, rot=(0, 0, math.radians(45)))
    p = nova('a10_arvore_branca')
    p.cilindro(M['casca_branca'], 0, 0, 0, 0.4, 0.3, 3.5, 7)
    p.bola(M['folhas_brancas'], 0, 0, 4.3, 1.8, 1.8, 1.5, 1, semente=21, irregular=0.1)
    p = nova('a10_altar_raizes')
    p.cilindro(M['casca'], 0, 0, 0, 1.6, 1.3, 1.1, 8)
    for a in range(5):
        ang = a / 5 * math.tau
        p.cilindro(M['casca'], math.cos(ang) * 1.6, math.sin(ang) * 1.6, 0, 0.3, 0.15, 2.4, 5, rot=(-math.sin(ang) * 0.4, math.cos(ang) * 0.4, 0))
    p.bola(M['luz_azul'], 0, 0, 1.4, 0.3, 0.3, 0.3, 0)
    return P


if __name__ == '__main__':
    B.limpar()
    M = mats()
    lista = pecas(M)
    objetos = [p.criar(0, 0) for p in lista]
    x, y, alt = -40.0, -30.0, 0.0
    for ob in objetos:
        w, d = ob.dimensions.x + 2, ob.dimensions.y + 2
        if x + w > 45:
            x, y, alt = -40.0, y + alt, 0.0
        ob.location = (x + w / 2, y + d / 2, 0)
        x += w
        alt = max(alt, d)
    B.exportar(objetos, PASTA, 'r01_andares.blend')
    print('ok', len(objetos), 'peças especiais')
    if len(sys.argv) > 1:
        B.previa(sys.argv[1], distancia=100, alvo=(2, 10, 0), amostras=16)
