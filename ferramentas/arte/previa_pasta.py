"""Faz um GIF animado com todas as criaturas de uma ou mais pastas (cada célula passa por todas as animações).

Uso: python3 ferramentas/arte/previa_pasta.py saida.gif pasta1 [pasta2 ...] [--so nome1,nome2] [--escala 3]
"""
import glob
import os
import sys
from PIL import Image

ORDEM = ['parado', 'mover', 'atacar', 'ataque', 'especial', 'mudar_fase', 'atordoado', 'dano', 'morrer']


def chave(an):
    for i, o in enumerate(ORDEM):
        if an.startswith(o):
            return (i, an)
    return (3, an)


def criaturas(pastas, so=None):
    grupos = {}
    for pasta in pastas:
        for f in sorted(glob.glob(os.path.join(pasta, '*_lado.png'))):
            base = os.path.basename(f)[:-9]
            grupos.setdefault(pasta, []).append((base, f))
    res = {}
    for pasta, itens in grupos.items():
        nomes = sorted({b for b, _ in itens}, key=len)
        for b, f in itens:
            # nome da criatura = o prefixo mais comprido partilhado; usa a imagem "parado" como âncora
            pass
        ancoras = [b[:-7] for b, _ in itens if b.endswith('_parado')]
        for a in ancoras:
            if so and a not in so:
                continue
            anims = [(b[len(a) + 1:], f) for b, f in itens if b.startswith(a + '_') and not any(
                b.startswith(o + '_') and len(o) > len(a) and o.startswith(a) for o in ancoras)]
            res[a] = sorted(anims, key=lambda x: chave(x[0]))
    return res


def frames_de(f):
    im = Image.open(f).convert('RGBA')
    h = im.height
    return [im.crop((i * h, 0, (i + 1) * h, h)) for i in range(im.width // h)]


def main():
    args = sys.argv[1:]
    so, escala = None, 3
    if '--so' in args:
        i = args.index('--so'); so = set(args[i + 1].split(',')); del args[i:i + 2]
    if '--escala' in args:
        i = args.index('--escala'); escala = int(args[i + 1]); del args[i:i + 2]
    saida, pastas = args[0], args[1:]
    cr = criaturas(pastas, so)
    seqs = []
    for nome, anims in cr.items():
        seq = []
        for an, f in anims:
            fr = frames_de(f)
            rep = 2 if len(fr) <= 2 else 1
            seq += [x for x in fr for _ in range(rep)]
        seqs.append(seq)
    cel = max(s[0].width for s in seqs)
    cols = min(6, len(seqs))
    linhas = (len(seqs) + cols - 1) // cols
    n = min(max(len(s) for s in seqs), 120)
    out = []
    for k in range(n):
        im = Image.new('RGBA', (cols * cel, linhas * cel), (50, 51, 83, 255))
        for i, s in enumerate(seqs):
            f = s[k % len(s)]
            x, y = (i % cols) * cel + (cel - f.width) // 2, (i // cols) * cel + cel - f.height
            im.alpha_composite(f, (x, y))
        out.append(im.resize((im.width * escala, im.height * escala), Image.NEAREST).convert('P', palette=Image.ADAPTIVE))
    out[0].save(saida, save_all=True, append_images=out[1:], duration=120, loop=0, disposal=2)
    print(saida, len(seqs), 'criaturas,', n, 'frames')


if __name__ == '__main__':
    main()
