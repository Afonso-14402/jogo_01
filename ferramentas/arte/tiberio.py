"""Tibério, o mercador das Zonas Seguras (docs/dialogos/povoacoes_r01.md, secção 1): o irmão gémeo do Tobias,
igual a ele mas com uma mochila do tamanho de um armário (com um cobertor enrolado por cima).
Faz-se a partir dos desenhos do Tobias: a mochila vai atrás (de frente e de lado) ou por cima (de costas).

Uso: python3 ferramentas/arte/tiberio.py
"""
import glob
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, retangulo, elipse, desenhar


def mochila(w, h, cobertor=True):
    P = [Parte(retangulo(1, 4, w - 2, h - 2, 1), 'couro', z=1, plano=True),
         Parte(retangulo(3, h // 2, w - 4, h - 4), 'castanho', z=2, plano=True),           # bolso
         Parte(retangulo(w // 2 - 1, h // 2 - 1, w // 2, h // 2), 'ouro', z=3, plano=True)]  # fivela
    if cobertor:
        P.append(Parte(retangulo(0, 0, w - 1, 4, 2), 'vermelho', z=4, volume='cilindro_h'))
    return desenhar(P, w, h)


def frames_com_mochila(img, direcao):
    lado = img.height
    out = Image.new('RGBA', img.size, (0, 0, 0, 0))
    for i in range(img.width // lado):
        f = img.crop((i * lado, 0, (i + 1) * lado, lado))
        bb = f.getbbox()
        if not bb:
            out.paste(f, (i * lado, 0))
            continue
        x0, y0, x1, y1 = bb
        cx = (x0 + x1) // 2
        nova = Image.new('RGBA', f.size, (0, 0, 0, 0))
        if direcao == 'cima':        # de costas: a mochila tapa as costas
            m = mochila(16, 18)
            nova.paste(f, (0, 0), f)
            nova.paste(m, (cx - 8, max(0, y0 + 6)), m)
        elif direcao == 'baixo':     # de frente: espreita por cima dos ombros
            m = mochila(18, 18)
            nova.paste(m, (cx - 9, max(0, y0 - 4)), m)
            nova.paste(f, (0, 0), f)
        else:                        # de lado (virado para a direita): atrás, à esquerda
            m = mochila(12, 18)
            nova.paste(m, (max(0, x0 - 6), max(0, y0 + 4)), m)
            nova.paste(f, (0, 0), f)
        out.paste(nova, (i * lado, 0))
    return out


def main():
    n = 0
    for f in glob.glob('arte/npcs/tobias_*.png'):
        base = os.path.basename(f)
        direcao = base[:-4].split('_')[-1]
        img = Image.open(f).convert('RGBA')
        frames_com_mochila(img, direcao).save(os.path.join('arte', 'npcs', base.replace('tobias_', 'tiberio_', 1)))
        n += 1
    print('tibério: %d folhas' % n)


if __name__ == '__main__':
    main()
