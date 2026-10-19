"""Guardiões feitos a partir de outros desenhos:
- Reflexo Negro (andar 19): silhueta negra do herói com olhos roxos; usa as animações do próprio herói.
- Eco dos Guardiões (andar 94): fantasma que muda de forma (é um guardião antigo diferente a cada 20% de vida).
Fichas: docs/regioes/r02_cavernas.md e r10_abismo.md (secção 6). Saída: arte/regioes/.../guardioes/

Uso: python3 ferramentas/arte/guardioes_especiais.py
"""
import glob
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
import heroi as H
from motor import guardar, dissolver

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte')
SOMBRA = ['#2e222f', '#2e222f', '#45293f', '#6b3e75']   # do escuro ao claro


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def _tingir(im, rampa, alpha=255, olhos=None):
    """Troca cada cor pela da rampa com o mesmo brilho (silhueta); a íris fica a brilhar."""
    out = im.copy()
    px = out.load()
    iris = _hex(H.PAL['e'])
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if not a:
                continue
            if olhos and (r, g, b) == _hex('#ffffff'):
                px[x, y] = _hex(olhos) + (255,)
                continue
            lum = (0.3 * r + 0.59 * g + 0.11 * b) / 255
            c = rampa[min(len(rampa) - 1, int(lum * len(rampa)))]
            px[x, y] = _hex(c) + (min(a, alpha),)
    return out


def reflexo_negro():
    A = {n: f() for n, f in H.ANIMS.items()}
    lado = lambda nome: [_tingir(f, SOMBRA, olhos='#a884f3') for f in A[nome]['lado']]
    an = {'parado': lado('parado'), 'mover': lado('andar'), 'atacar': lado('ataque_corte'), 'dano': lado('dano')[:1],
          'morrer': lado('morrer')[:4], 'ataque_1': lado('ataque_estocada'), 'ataque_2': lado('ataque_pesado')}
    p = an['parado'][0]
    an['ataque_3'] = [p, dissolver(p, 0.5), dissolver(p, 0.9), dissolver(p, 0.5), p]   # troca de lugar contigo
    guardar(os.path.join(RAIZ, 'regioes', 'r02_cavernas', 'guardioes'), 'reflexo_negro', an)


def _frames(caminho, W):
    im = Image.open(caminho).convert('RGBA')
    h = im.height
    out = []
    for i in range(im.width // h):
        f = im.crop((i * h, 0, i * h + h, h))
        if h != W:
            if h > W:   # maior do que o quadro: encolhe (só acontece com bosses)
                f = f.resize((W, W), Image.NEAREST)
            q = Image.new('RGBA', (W, W))
            q.paste(f, ((W - f.width) // 2, W - f.height), f)
            f = q
        out.append(f)
    return out


def eco_guardioes():
    W = 64
    fontes = []
    for reg in ('r01_floresta', 'r03_pantano', 'r05_gelo', 'r07_vulcao', 'r09_ceu'):
        g = sorted(glob.glob(os.path.join(RAIZ, 'regioes', reg, 'guardioes', '*_parado_lado.png')))
        if g:
            fontes.append(g[0][:-len('_parado_lado.png')])
    azul = ['#323353', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff']
    fan = lambda base, anim: [_tingir(f, azul, alpha=200) for f in _frames(f'{base}_{anim}_lado.png', W)]
    um = fontes[0]
    an = {'parado': fan(um, 'parado'), 'mover': fan(um, 'mover'), 'atacar': fan(um, 'atacar'),
          'dano': fan(um, 'dano')[:1], 'morrer': [dissolver(fan(um, 'parado')[0], d) for d in (0.2, 0.45, 0.7, 0.92)]}
    for i, base in enumerate(fontes[1:4]):
        an[f'ataque_{i + 1}'] = fan(base, 'atacar')
    # mudar de forma: a forma atual desfaz-se e aparece a seguinte (5 formas)
    trans = []
    for a, b in zip(fontes, fontes[1:] + fontes[:1]):
        fa, fb = fan(a, 'parado')[0], fan(b, 'parado')[0]
        trans += [dissolver(fa, 0.5), dissolver(fb, 0.5)]
    an['transformar'] = trans
    guardar(os.path.join(RAIZ, 'regioes', 'r10_abismo', 'guardioes'), 'eco_dos_guardioes', an)
    return [os.path.basename(f) for f in fontes]


if __name__ == '__main__':
    reflexo_negro()
    print('ok reflexo_negro; eco_dos_guardioes com as formas de', eco_guardioes())
