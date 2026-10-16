"""Monstros com DESENHO DE REFERÊNCIA feito à mão (arte/referencia/<nome>/): usa-se o desenho original
e as animações que faltam são feitas a partir dele (mover, dano, morrer, especiais com efeitos por cima).

Uso: python3 ferramentas/arte/referencias.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from motor import guardar, dissolver
from criaturas import ESPECIAIS, Tela, efeito

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte')

# nome: (pasta de saída, cfg dos efeitos, especiais)
REFERENCIAS = {
    'aranha_mae': ('regioes/r02_cavernas/bosses', dict(k=2.0, W=64, fx_cor='verde'),
                   ['golpe', 'sopro', 'descer', 'invocar', 'area', 'salto']),
}


def _frames(nome, anim):
    im = Image.open(os.path.join(RAIZ, 'referencia', nome, f'{nome}_{anim}_lado.png')).convert('RGBA')
    h = im.height
    return [im.crop((i * h, 0, i * h + h, h)) for i in range(im.width // h)]


def _mexer(im, dx=0, dy=0):
    out = Image.new('RGBA', im.size)
    out.paste(im, (dx, dy), im)
    return out


def _pose(P, A, cfg, p):
    """Uma pose genérica (como em criaturas.ESPECIAIS) feita com os frames de referência."""
    at = p.get('at', 0)
    base = A[min(len(A) - 1, int(round(at * (len(A) - 1))))] if at else (A[1] if p.get('boca') else P[0])
    k = cfg['k']
    im = _mexer(base, int(p.get('dx', 0) * k), int((p.get('dy', 0) + p.get('baixo', 0)) * k))
    if p.get('fx') or p.get('_estrelas') is not None:
        t = Tela(cfg, p)
        efeito(t, cfg, p, 24, 16)
        if t.P or p.get('_estrelas') is not None:
            im.alpha_composite(t.imagem())
    if p.get('_dissolver'):
        im = dissolver(im, p['_dissolver'])
    return im


def anims(nome, cfg, especiais):
    P, A = _frames(nome, 'parado'), _frames(nome, 'atacar')
    k = int(cfg['k'])
    an = {
        'parado': P,
        'mover': [_mexer(P[i % len(P)], dx * k, -(i % 2) * k) for i, dx in enumerate((0, 1, 2, 1))],
        'atacar': A,
        'dano': [_mexer(P[0], -2 * k, k)],
    }
    de_costas = P[0].transpose(Image.FLIP_TOP_BOTTOM)
    de_costas = _mexer(de_costas, 0, P[0].height - de_costas.getbbox()[3])
    an['morrer'] = [_mexer(P[0], -k, k), de_costas, dissolver(de_costas, 0.45), dissolver(de_costas, 0.8)]
    for i, esp in enumerate(especiais):
        an[f'especial_{i + 1}'] = [_pose(P, A, cfg, pp) for pp in ESPECIAIS[esp]]
    an['mudar_fase'] = [_pose(P, A, cfg, pp) for pp in
                        (dict(), dict(fx='magia', fn=2, boca=True), dict(fx='magia', fn=3, dy=-1, boca=True), dict())]
    an['atordoado'] = [_pose(P, A, cfg, dict(baixo=1, _estrelas=i)) for i in range(4)]
    return an


if __name__ == '__main__':
    for nome, (pasta, cfg, esp) in REFERENCIAS.items():
        guardar(os.path.join(RAIZ, pasta), nome, anims(nome, cfg, esp))
        print('ok', nome)
