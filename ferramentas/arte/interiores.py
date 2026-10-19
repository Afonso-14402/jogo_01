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


def soalho(c, rnd, T=32):
    """Tábuas compridas (4 px de largura, 1 px de junta escura), com as pontas desencontradas e veios."""
    from PIL import Image
    im = Image.new('RGB', (T, T))
    px = im.load()
    h = lambda k: tuple(int(c[k][i:i + 2], 16) for i in (1, 3, 5))
    for fila in range(T // 4):
        y0 = fila * 4
        corte = rnd.randrange(T)                 # onde acaba uma tábua e começa a outra
        tom = [rnd.choice([2, 2, 3]), rnd.choice([2, 2, 3])]
        for y in range(y0, y0 + 4):
            for x in range(T):
                k = tom[0] if (x - corte) % T < T // 2 + 4 else tom[1]
                if y == y0 + 3:
                    k = 0                          # junta entre tábuas
                elif y == y0:
                    k = min(3, k + 1)              # beira de cima com luz
                elif (x - corte) % T in (0, T // 2 + 4):
                    k = 1                          # junta de topo
                elif rnd.random() < 0.06:
                    k = max(1, k - 1)              # veio
                px[x, y] = h(k)
    return im


def lajes(c, rnd, T=32):
    """Lajes de 8x8 desencontradas, com aresta clara em cima-esquerda e escura em baixo-direita."""
    from PIL import Image
    im = Image.new('RGB', (T, T))
    px = im.load()
    h = lambda k: tuple(int(c[k][i:i + 2], 16) for i in (1, 3, 5))
    tons = {}
    for y in range(T):
        fila = y // 8
        off = 4 if fila % 2 else 0
        for x in range(T):
            col = ((x + off) % T) // 8
            if (fila, col) not in tons:
                tons[(fila, col)] = rnd.choice([1, 2, 2, 2, 3])
            k = tons[(fila, col)]
            lx, ly = (x + off) % 8, y % 8
            if lx == 7 or ly == 7:
                k = 0
            elif lx == 0 or ly == 0:
                k = min(4, k + 1)
            elif lx == 6 or ly == 6:
                k = max(1, k - 1)
            elif rnd.random() < 0.03:
                k = max(1, k - 1)
            px[x, y] = h(k)
    return im


def reboco(c, rnd, T=32):
    from PIL import Image
    im = Image.new('RGB', (T, T))
    px = im.load()
    h = lambda k: tuple(int(c[k][i:i + 2], 16) for i in (1, 3, 5))
    for y in range(T):
        for x in range(T):
            r = rnd.random()
            px[x, y] = h(1 if r < 0.015 else (3 if r > 0.97 else 2))
    return im


def main():
    os.makedirs(PASTA, exist_ok=True)
    rnd = random.Random(5)
    for nome, cores in CORES.items():
        tipo = nome.split('_', 1)[1]
        if nome == 'chao_madeira':
            img = soalho(cores, rnd)
        elif nome == 'chao_pedra':
            img = lajes(cores, rnd)
        elif nome == 'parede_reboco':
            img = reboco(cores, rnd)
        else:
            material = {'madeira': 'tabua', 'pedra': 'pedra', 'reboco': 'parede', 'tijolo': 'tijolo'}[tipo]
            ctx = 'casa' if nome.startswith('parede') else ''
            img = X.padrao(material, cores, 32, 3, ctx).convert('RGB')
        img.save(os.path.join(PASTA, nome + '.png'))


if __name__ == '__main__':
    main()
