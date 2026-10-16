"""Edifícios e objetos de Ascendia (docs/CIDADES.md): pedra clara e telhados vermelhos, à volta da base da torre.
Saída: arte/cidade/ (um .glb por peça + cidade.blend + texturas/).

Uso: blenv/bin/python ferramentas/arte/blender/cidade.py [previa.png]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B

PASTA = os.path.join('arte', 'cidade')
TEX = os.path.join(PASTA, 'texturas')


def texturas():
    t = {}
    t['parede'] = B.textura_ruido('cid_parede', ['#c7dcd0', '#9babb2', '#ab947a', '#ffffff'], TEX, 1, tabuas=('#9babb2', 8))
    t['parede_madeira'] = B.textura_ruido('cid_parede_madeira', ['#ab947a', '#966c6c', '#c7dcd0'], TEX, 2, tabuas=('#694f62', 5))
    t['telhado'] = B.textura_ruido('cid_telhado', ['#b33831', '#ea4f36', '#6e2727', '#f57d4a'], TEX, 3, tabuas=('#6e2727', 4))
    t['telhado_azul'] = B.textura_ruido('cid_telhado_azul', ['#4d65b4', '#4d9be6', '#323353'], TEX, 4, tabuas=('#323353', 4))
    t['telhado_verde'] = B.textura_ruido('cid_telhado_verde', ['#239063', '#1ebc73', '#165a4c'], TEX, 5, tabuas=('#165a4c', 4))
    t['madeira'] = B.textura_ruido('cid_madeira', ['#966c6c', '#ab947a', '#694f62'], TEX, 6, tabuas=('#45293f', 6))
    t['porta'] = B.textura_ruido('cid_porta', ['#694f62', '#4c3e24', '#966c6c'], TEX, 7, tabuas=('#2e222f', 4))
    t['janela'] = B.textura_ruido('cid_janela', ['#4d9be6', '#8fd3ff', '#4d65b4'], TEX, 8)
    t['pedra'] = B.textura_ruido('cid_pedra', ['#9babb2', '#7f708a', '#c7dcd0', '#625565'], TEX, 9)
    t['calcada'] = B.textura_ruido('cid_calcada', ['#9babb2', '#c7dcd0', '#7f708a'], TEX, 10, tabuas=('#625565', 4))
    t['torre'] = B.textura_ruido('cid_torre', ['#7f708a', '#625565', '#9babb2', '#484a77'], TEX, 11, tabuas=('#3e3546', 8))
    t['agua'] = B.textura_ruido('cid_agua', ['#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2'], TEX, 12)
    t['toldo_vermelho'] = B.textura_ruido('cid_toldo_vermelho', ['#ea4f36', '#ffffff'], TEX, 13, tabuas=('#ffffff', 4))
    t['toldo_azul'] = B.textura_ruido('cid_toldo_azul', ['#4d9be6', '#ffffff'], TEX, 14, tabuas=('#ffffff', 4))
    t['toldo_verde'] = B.textura_ruido('cid_toldo_verde', ['#1ebc73', '#fbff86'], TEX, 15, tabuas=('#fbff86', 4))
    t['tenda_roxa'] = B.textura_ruido('cid_tenda_roxa', ['#6b3e75', '#905ea9', '#45293f'], TEX, 16, manchas=[('#fbff86', 6, 0)])
    t['metal'] = B.textura_ruido('cid_metal', ['#625565', '#3e3546', '#9babb2'], TEX, 17)
    t['relva'] = B.textura_ruido('cid_relva', ['#239063', '#1ebc73', '#165a4c'], TEX, 18)
    t['folhas'] = B.textura_ruido('cid_folhas', ['#1ebc73', '#239063', '#91db69'], TEX, 19)
    t['casca'] = B.textura_ruido('cid_casca', ['#694f62', '#4c3e24', '#966c6c'], TEX, 20, riscas=('#45293f', 10))
    t['ouro'] = B.textura_ruido('cid_ouro', ['#f9c22b', '#f79617', '#fbff86'], TEX, 21)
    t['vitral'] = B.textura_ruido('cid_vitral', ['#4d9be6', '#f9c22b', '#ea4f36', '#1ebc73'], TEX, 22, tabuas=('#2e222f', 4))
    m = {k: B.material('cid_' + k, v) for k, v in t.items()}
    m['cristal'] = B.material('cid_cristal', B.textura_ruido('cid_cristal', ['#4d9be6', '#8fd3ff', '#ffffff'], TEX, 23), emissao=2.0)
    m['luz'] = B.material('cid_luz', cor='#fbff86', emissao=3.0)
    return m


def casa(p, M, sx, sy, andares=1, parede='parede', telhado='telhado', chamine=False, porta_x=0.0, janelas=True, alt=3.0):
    h = andares * alt
    p.caixa(M['pedra'], 0, 0, 0, sx + 0.2, sy + 0.2, 0.4)
    p.caixa(M[parede], 0, 0, 0.4, sx, sy, h)
    p.telhado(M[telhado], 0, 0, 0.4 + h, sx, sy, min(sx, sy) * 0.45)
    p.caixa(M['porta'], porta_x, -sy / 2 - 0.05, 0.4, 1.1, 0.12, 2.1)
    if janelas:
        for a in range(andares):
            z = 0.4 + a * alt + 1.2
            for x in [i for i in (-sx / 2 + 1.2, sx / 2 - 1.2) if abs(i - porta_x) > 1.2] + ([porta_x] if a > 0 else []):
                p.caixa(M['janela'], x, -sy / 2 - 0.05, z, 0.9, 0.1, 1.0)
                p.caixa(M['madeira'], x, -sy / 2 - 0.12, z - 0.1, 1.1, 0.25, 0.12)
    if chamine:
        p.caixa(M['pedra'], sx / 4, sy / 4, 0.4 + h, 0.7, 0.7, min(sx, sy) * 0.6)


def pecas(M):
    P = []

    def nova(nome):
        p = B.Peca(nome)
        P.append(p)
        return p

    # --- edifícios principais ---
    p = nova('guilda')
    casa(p, M, 10, 8, andares=2, telhado='telhado_azul', alt=3.2)
    p.caixa(M['madeira'], 0, -4.3, 4.8, 3.0, 0.15, 1.0)          # placa
    p.caixa(M['ouro'], 0, -4.4, 5.0, 0.6, 0.1, 0.6)
    for x in (-2.5, 2.5):
        p.cilindro(M['pedra'], x, -4.6, 0, 0.3, 0.3, 3.0, 8)
    p.caixa(M['telhado_azul'], 0, -4.6, 3.0, 6.0, 1.4, 0.2)
    p = nova('forja_brom')
    casa(p, M, 7, 6, telhado='telhado', chamine=True, parede='parede')
    p.caixa(M['metal'], 3.0, -4.2, 0, 1.0, 0.5, 0.8)              # bigorna
    p.caixa(M['metal'], 3.0, -4.2, 0.8, 1.3, 0.6, 0.25)
    p.cilindro(M['madeira'], -3.0, -4.0, 0, 0.5, 0.5, 0.9, 8)      # barril de água
    p = nova('alquimia_selene')
    casa(p, M, 6, 6, telhado='telhado_verde', chamine=False)
    p.cilindro(M['parede'], 3.2, 2.2, 0, 1.4, 1.4, 6.5, 8)        # torrezinha
    p.cilindro(M['telhado_verde'], 3.2, 2.2, 6.5, 1.8, 0.05, 2.5, 8)
    p = nova('estalagem')
    casa(p, M, 9, 7, andares=2, parede='parede_madeira', chamine=True)
    p.caixa(M['madeira'], 3.0, -3.9, 2.8, 0.15, 0.8, 0.15)
    p.caixa(M['madeira'], 3.0, -4.3, 2.0, 1.2, 0.1, 0.8)          # placa do Ninho do Viajante
    p = nova('taberna')
    casa(p, M, 8, 7, parede='parede_madeira', chamine=True)
    for x in (-2.5, 2.5):
        p.cilindro(M['madeira'], x, -4.2, 0, 0.45, 0.45, 0.9, 8)
    for i, nome in enumerate(('casa_1', 'casa_2', 'casa_3')):
        p = nova(nome)
        casa(p, M, [5, 6, 5][i], [5, 5, 6][i], andares=[1, 2, 1][i], parede=['parede', 'parede', 'parede_madeira'][i],
             chamine=i != 1)
    p = nova('igreja')
    casa(p, M, 8, 12, telhado='telhado', alt=5.0, janelas=False)
    p.caixa(M['vitral'], 0, -6.1, 3.0, 2.0, 0.1, 2.0)
    p.caixa(M['parede'], 0, 6.5, 0, 3, 3, 10)
    p.cilindro(M['telhado'], 0, 6.5, 10, 2.2, 0.05, 3.0, 4, rot=(0, 0, math.radians(45)))
    p = nova('biblioteca')
    casa(p, M, 9, 7, andares=2, telhado='telhado_azul')
    for x in (-3, -1, 1, 3):
        p.cilindro(M['pedra'], x, -3.9, 0.4, 0.25, 0.25, 3.0, 8)
    p = nova('camara_governador')
    casa(p, M, 10, 8, andares=2, telhado='telhado')
    p.cilindro(M['madeira'], 0, 0, 7.5, 0.06, 0.06, 2.5, 4)
    p.caixa(M['toldo_azul'], 0.6, 0, 9.3, 1.2, 0.05, 0.7)          # bandeira
    p = nova('tenda_vidente')
    p.cilindro(M['tenda_roxa'], 0, 0, 0, 2.5, 0.2, 3.5, 8)
    p.cilindro(M['ouro'], 0, 0, 3.4, 0.15, 0.15, 0.5, 6)
    p = nova('casa_heroi')
    casa(p, M, 6, 6, telhado='telhado', chamine=True)
    p.caixa(M['madeira'], -4, -1, 0, 0.15, 6, 1.0)                 # cerca do quintal
    # --- a torre e a praça ---
    p = nova('base_torre')
    p.cilindro(M['torre'], 0, 0, 0, 12, 11, 30, 16)
    p.cilindro(M['torre'], 0, 0, 0, 13, 13, 1.5, 16)
    p.caixa(M['porta'], 0, -11.2, 1.5, 4.0, 0.8, 6.0)
    p.caixa(M['torre'], 0, -11.3, 7.5, 5.0, 1.0, 1.0)
    p = nova('cristal_mestre')
    p.cilindro(M['pedra'], 0, 0, 0, 1.6, 1.4, 0.6, 8)
    p.cilindro(M['cristal'], 0, 0, 0.6, 0.8, 0.0, 3.6, 6)
    p.cilindro(M['cristal'], 0, 0, 0.6, 0.8, 0.8, 0.6, 6)
    p = nova('fonte')
    p.cilindro(M['pedra'], 0, 0, 0, 2.5, 2.5, 0.7, 12)
    p.cilindro(M['agua'], 0, 0, 0.5, 2.2, 2.2, 0.25, 12)
    p.cilindro(M['pedra'], 0, 0, 0.6, 0.4, 0.4, 1.6, 8)
    p.cilindro(M['pedra'], 0, 0, 2.1, 1.0, 0.6, 0.3, 8)
    p.bola(M['agua'], 0, 0, 2.5, 0.3, 0.3, 0.4, 0)
    p = nova('quadro_avisos')
    for x in (-1.0, 1.0):
        p.cilindro(M['madeira'], x, 0, 0, 0.1, 0.1, 2.2, 6)
    p.caixa(M['madeira'], 0, 0, 1.0, 2.2, 0.1, 1.2)
    p.caixa(M['parede'], -0.4, -0.08, 1.3, 0.5, 0.05, 0.6)
    p.caixa(M['parede'], 0.4, -0.08, 1.4, 0.5, 0.05, 0.5)
    p.telhado(M['telhado'], 0, 0, 2.2, 2.2, 0.2, 0.4)
    p = nova('palco')
    p.caixa(M['madeira'], 0, 0, 0, 8, 5, 1.0)
    for x in (-3.8, 3.8):
        p.cilindro(M['madeira'], x, 2.3, 1.0, 0.15, 0.15, 3.5, 6)
    p.caixa(M['toldo_vermelho'], 0, 2.3, 4.3, 8, 0.15, 0.6)
    p = nova('pedestal_estatua')
    p.caixa(M['pedra'], 0, 0, 0, 2.0, 2.0, 1.0)
    p.caixa(M['ouro'], 0, -1.02, 0.4, 1.0, 0.05, 0.3)
    # --- mercado e rua ---
    for i, cor in enumerate(('toldo_vermelho', 'toldo_azul', 'toldo_verde')):
        p = nova(f'banca_{i + 1}')
        p.caixa(M['madeira'], 0, 0, 0, 2.4, 1.2, 1.0)
        for x in (-1.1, 1.1):
            p.cilindro(M['madeira'], x, 0.5, 0, 0.07, 0.07, 2.4, 5)
            p.cilindro(M['madeira'], x, -0.6, 0, 0.07, 0.07, 2.0, 5)
        p.prisma(M[cor], [(-1.4, -0.9), (1.4, -0.9), (1.4, 0.7), (-1.4, 0.7)], 2.0, 2.15)
        for j in range(3):
            p.bola(M[['ouro', 'toldo_vermelho', 'folhas'][(i + j) % 3]], -0.7 + j * 0.7, -0.2, 1.1, 0.25, 0.25, 0.2, 0)
    p = nova('candeeiro')
    p.cilindro(M['metal'], 0, 0, 0, 0.12, 0.08, 3.2, 6)
    p.caixa(M['metal'], 0, 0, 3.2, 0.5, 0.5, 0.1)
    p.bola(M['luz'], 0, 0, 3.5, 0.2, 0.2, 0.25, 0)
    p.cilindro(M['metal'], 0, 0, 3.75, 0.35, 0.05, 0.3, 4)
    p = nova('barril')
    p.cilindro(M['madeira'], 0, 0, 0, 0.45, 0.45, 1.0, 10)
    p = nova('caixotes')
    p.caixa(M['madeira'], 0, 0, 0, 0.9, 0.9, 0.9)
    p.caixa(M['madeira'], 0.5, 0.5, 0, 0.7, 0.7, 0.7)
    p.caixa(M['madeira'], 0.2, 0.2, 0.9, 0.7, 0.7, 0.7, rot_z=0.4)
    p = nova('banco')
    p.caixa(M['madeira'], 0, 0, 0.45, 2.0, 0.5, 0.1)
    for x in (-0.8, 0.8):
        p.caixa(M['pedra'], x, 0, 0, 0.2, 0.45, 0.45)
    p = nova('arvore_cidade')
    p.cilindro(M['casca'], 0, 0, 0, 0.3, 0.25, 2.0, 7)
    p.bola(M['folhas'], 0, 0, 2.8, 1.4, 1.4, 1.2, 1, semente=5, irregular=0.1)
    p.cilindro(M['pedra'], 0, 0, 0, 1.0, 1.0, 0.35, 8)
    p = nova('chao_calcada')
    p.caixa(M['calcada'], 0, 0, 0, 2, 2, 0.2)
    p = nova('chao_relva')
    p.caixa(M['relva'], 0, 0, 0, 2, 2, 0.2)
    # --- muralha ---
    p = nova('muralha')
    p.caixa(M['pedra'], 0, 0, 0, 4, 1.5, 6)
    for x in (-1.5, -0.5, 0.5, 1.5):
        p.caixa(M['pedra'], x, -0.5, 6, 0.6, 0.5, 0.7)
    p = nova('torre_muralha')
    p.cilindro(M['pedra'], 0, 0, 0, 2.2, 2.0, 9, 10)
    p.cilindro(M['telhado'], 0, 0, 9, 2.7, 0.05, 3.5, 10)
    p = nova('portao')
    p.caixa(M['pedra'], -2.5, 0, 0, 1.5, 2, 7)
    p.caixa(M['pedra'], 2.5, 0, 0, 1.5, 2, 7)
    p.caixa(M['pedra'], 0, 0, 5, 3.5, 2, 2)
    p.caixa(M['porta'], -0.9, 0, 0, 1.6, 0.2, 5, rot_z=0.5)
    p.caixa(M['porta'], 0.9, 0, 0, 1.6, 0.2, 5, rot_z=-0.5)
    p = nova('cais')
    p.caixa(M['madeira'], 0, 0, 0.5, 3, 8, 0.2)
    for x in (-1.3, 1.3):
        for y in (-3.5, 0, 3.5):
            p.cilindro(M['casca'], x, y, -1.0, 0.15, 0.15, 1.8, 6)
    p = nova('barco_pesca')
    p.prisma(M['madeira'], [(0, 2.2), (0.9, 1.2), (0.9, -1.8), (-0.9, -1.8), (-0.9, 1.2)], 0, 0.7)
    p.caixa(M['madeira'], 0, -0.2, 0.7, 1.4, 0.3, 0.1)
    return P


if __name__ == '__main__':
    B.limpar()
    M = texturas()
    lista = pecas(M)
    objetos = []
    xs = 0.0
    linha_y = 0.0
    larg_linha = 0.0
    for i, p in enumerate(lista):
        ob = p.criar(0, 0)
        objetos.append(ob)
    # arrumar para a pré-visualização (em grelha, com espaço conforme o tamanho)
    x, y, alt_linha = -40.0, -30.0, 0.0
    for ob in objetos:
        w = ob.dimensions.x + 3
        d = ob.dimensions.y + 3
        if x + w > 45:
            x, y = -40.0, y + alt_linha
            alt_linha = 0.0
        ob.location = (x + w / 2, y + d / 2, 0)
        x += w
        alt_linha = max(alt_linha, d)
    B.exportar(objetos, PASTA, 'cidade.blend')
    print('ok', len(objetos), 'peças')
    if len(sys.argv) > 1:
        B.previa(sys.argv[1], distancia=95, alvo=(3, 5, 0), amostras=16)
