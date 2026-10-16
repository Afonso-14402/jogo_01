"""Criação de personagem (docs/INTERFACE.md, secção 6): 8 penteados + trocas de cor.

Para cada penteado gera todas as animações do herói com CORES-ÍNDICE: cada parte (pele, cabelo, íris, roupa)
usa cores que só ela tem, e o jogo troca-as com um shader de paleta (arte/heroi/paletas.json):
  tom de pele (6) · cor do cabelo (10) · cor dos olhos (6) · roupa do mundo real (4, só no prólogo).
Saída: arte/heroi/aparencia/heroi_<anim>_<dir>_<penteado>.png + arte/heroi/paletas.json

Uso: python3 ferramentas/arte/heroi_aparencia.py [previa.gif]
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
import heroi as H
from heroi_cabelos import PENTEADOS

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'heroi')

# cores-índice (cores que o herói não usa noutro sítio)
INDICE_CABELO = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']   # H h r R Y
INDICE_IRIS = '#0b5e65'
PELE_BASE = ['#cd683d', '#e6904e', '#fca790', '#fdcbb0', '#f68181']       # K D S L P
ROUPA_BASE = {'tunica': ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
              'lenco': ['#6e2727', '#b33831', '#ea4f36', '#f57d4a'],
              'calcas': ['#3e3546', '#625565', '#7f708a'],
              'botas': ['#45293f', '#694f62', '#966c6c', '#ab947a']}

PALETAS = {
    'pele': {
        'clara': PELE_BASE,
        'rosada': ['#cf657f', '#f68181', '#fdcbb0', '#ffffff', '#ed8099'],
        'morena': ['#9e4539', '#cd683d', '#e6904e', '#fca790', '#ea4f36'],
        'castanha': ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#b33831'],
        'escura': ['#45293f', '#7a3045', '#9e4539', '#cd683d', '#6e2727'],
        'muito_escura': ['#2e222f', '#45293f', '#7a3045', '#9e4539', '#6e2727'],
    },
    'cabelo': {
        'castanho_avermelhado': ['#7a3045', '#9e4539', '#cd683d', '#e6904e', '#fbb954'],
        'castanho': ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'],
        'preto': ['#2e222f', '#2e222f', '#3e3546', '#484a77', '#625565'],
        'loiro': ['#9e4539', '#f79617', '#f9c22b', '#fbff86', '#ffffff'],
        'ruivo': ['#6e2727', '#b33831', '#ea4f36', '#f57d4a', '#fbb954'],
        'branco': ['#625565', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff'],
        'cinzento': ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
        'azul': ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff'],
        'rosa': ['#831c5d', '#c32454', '#f04f78', '#f68181', '#fdcbb0'],
        'verde': ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c'],
    },
    'olhos': {'preto': '#2e222f', 'castanho': '#7a3045', 'azul': '#4d65b4', 'verde': '#239063', 'cinzento': '#7f708a',
              'ambar': '#f79617'},
    'roupa': {
        'aventureiro': ROUPA_BASE,
        'camisola_capuz': {'tunica': ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
                           'lenco': ['#3e3546', '#625565', '#7f708a', '#9babb2'],
                           'calcas': ['#323353', '#484a77', '#4d65b4'], 'botas': ['#2e222f', '#c7dcd0', '#ffffff', '#ffffff']},
        'uniforme_escolar': {'tunica': ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'],
                             'lenco': ['#323353', '#484a77', '#4d65b4', '#4d9be6'],
                             'calcas': ['#2e222f', '#323353', '#484a77'], 'botas': ['#2e222f', '#2e222f', '#3e3546', '#625565']},
        'fato_treino': {'tunica': ['#6e2727', '#b33831', '#e83b3b', '#f68181', '#ffffff'],
                        'lenco': ['#c7dcd0', '#ffffff', '#ffffff', '#ffffff'],
                        'calcas': ['#6e2727', '#b33831', '#e83b3b'], 'botas': ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff']},
        'escritorio': {'tunica': ['#2e222f', '#3e3546', '#484a77', '#625565', '#7f708a'],
                       'lenco': ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff'],
                       'calcas': ['#2e222f', '#3e3546', '#484a77'], 'botas': ['#2e222f', '#2e222f', '#45293f', '#694f62']},
    },
}


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def gerar_folhas():
    pasta = os.path.join(RAIZ, 'aparencia')
    os.makedirs(pasta, exist_ok=True)
    original = dict(H.PAL)
    for letra, cor in zip('HhrRY', INDICE_CABELO):
        H.PAL[letra] = cor
    H.PAL['e'] = INDICE_IRIS
    n = 0
    try:
        for estilo in PENTEADOS:
            H.POSE['estilo'] = estilo
            for nome, fn in H.ANIMS.items():
                for d, frames in fn().items():
                    H.tira(frames).save(os.path.join(pasta, f'heroi_{nome}_{d}_{estilo}.png'))
                    n += 1
    finally:
        H.PAL.clear()
        H.PAL.update(original)
        H.POSE['estilo'] = 'espetado'
    dados = {'indices': {'pele': PELE_BASE, 'cabelo': INDICE_CABELO, 'olhos': INDICE_IRIS, 'roupa': ROUPA_BASE},
             'penteados': list(PENTEADOS), **PALETAS}
    with open(os.path.join(RAIZ, 'paletas.json'), 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=1)
    return n


def aplicar(im, pele='clara', cabelo='castanho_avermelhado', olhos='preto', roupa='aventureiro'):
    """Faz em Python o que o shader do jogo faz: troca as cores-índice pelas escolhidas."""
    t = {}
    for a, b in zip(PELE_BASE, PALETAS['pele'][pele]):
        t[_hex(a)] = _hex(b)
    for a, b in zip(INDICE_CABELO, PALETAS['cabelo'][cabelo]):
        t[_hex(a)] = _hex(b)
    t[_hex(INDICE_IRIS)] = _hex(PALETAS['olhos'][olhos])
    for parte, cores in ROUPA_BASE.items():
        for a, b in zip(cores, PALETAS['roupa'][roupa][parte]):
            t[_hex(a)] = _hex(b)
    out = im.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            if px[x, y][3] and px[x, y] in t:
                px[x, y] = t[px[x, y]]
    return out


if __name__ == '__main__':
    print('ok', gerar_folhas(), 'folhas (8 penteados) + paletas.json')
    if len(sys.argv) > 1:   # amostra: 8 combinações a andar
        combos = [('espetado', 'clara', 'castanho_avermelhado', 'preto', 'aventureiro'),
                  ('comprido', 'morena', 'preto', 'castanho', 'aventureiro'),
                  ('curto', 'escura', 'branco', 'ambar', 'aventureiro'),
                  ('rabo', 'clara', 'loiro', 'azul', 'uniforme_escolar'),
                  ('carrapito', 'rosada', 'rosa', 'verde', 'aventureiro'),
                  ('rapado', 'muito_escura', 'preto', 'castanho', 'fato_treino'),
                  ('tranca', 'castanha', 'ruivo', 'verde', 'camisola_capuz'),
                  ('caracois', 'clara', 'azul', 'cinzento', 'escritorio')]
        tiras = []
        for est, *pal in combos:
            for d in ('baixo', 'lado'):
                im = Image.open(os.path.join(RAIZ, 'aparencia', f'heroi_andar_{d}_{est}.png')).convert('RGBA')
                tiras.append(aplicar(im, *pal))
        quadros = []
        for k in range(6):
            fr = Image.new('RGB', (8 * 2 * 100, 100), (96, 120, 96))
            for i, t in enumerate(tiras):
                f = t.crop((k * 32, 0, k * 32 + 32, 32)).resize((96, 96), Image.NEAREST)
                fr.paste(f, (i * 100, 2), f)
            quadros.append(fr)
        quadros[0].save(sys.argv[1], save_all=True, append_images=quadros[1:], duration=130, loop=0)
