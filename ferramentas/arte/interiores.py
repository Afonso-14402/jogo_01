"""Chão e paredes das divisões por dentro (docs/CIDADES.md 1.6), em pixel art 32x32 (2 m por textura):
madeira, pedra, reboco, tijolo. Usa os desenhos de texturas3d.py.

Uso: python3 ferramentas/arte/interiores.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(__file__))
import texturas3d as X

PASTA = os.path.join('arte', 'interiores')
CORES = {
    'chao_madeira': ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'chao_pedra': ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'parede_reboco': ['#966c6c', '#ab947a', '#c7dcd0', '#ffffff', '#ffffff'],
    'parede_madeira': ['#45293f', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'],
    'parede_pedra': ['#3e3546', '#625565', '#7f708a', '#9babb2', '#c7dcd0'],
    'parede_tijolo': ['#45293f', '#6e2727', '#9e4539', '#cd683d', '#e6904e'],
}


def main():
    os.makedirs(PASTA, exist_ok=True)
    for nome, cores in CORES.items():
        tipo = nome.split('_', 1)[1]
        material = {'madeira': 'tabua', 'pedra': 'pedra', 'reboco': 'parede', 'tijolo': 'tijolo'}[tipo]
        ctx = 'casa' if nome.startswith('parede') else ''
        X.padrao(material, cores, 32, 3, ctx).convert('RGB').save(os.path.join(PASTA, nome + '.png'))
    print('interiores: %d texturas' % len(CORES))


if __name__ == '__main__':
    main()
