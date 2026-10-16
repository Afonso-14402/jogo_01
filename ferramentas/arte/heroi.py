"""Gera todas as animações do herói (32x32 por frame) em arte/heroi/, com o motor de desenho (motor.py).

O herói é desenhado a partir de POSES: onde estão as mãos, os pés, o corpo e que cara faz.
A cabeça é desenhada à mão (píxel a píxel); o corpo é feito pelo motor (volume, luz e contornos).
O herói desenha-se SEM arma (a arma é um sprite à parte que o jogo põe na mão).

Uso (a partir da raiz do repositório):  python3 ferramentas/arte/heroi.py [previa.gif]
"""
import os
import sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, tira, previa_gif, desenho_a_mao

T = 32
FIVELA = '#f9c22b'
CALCAS_LONGE = ['#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2']
AZUL_LONGE = ['#323353', '#323353', '#484a77', '#4d65b4', '#4d65b4']

# ---------- cabeças desenhadas à mão (14 de largura) ----------
#  o contorno · 1-5 cabelo (escuro -> brilho) · a-d pele (claro -> escuro) · e olho · k bochecha
MAPA = {'o': '#2e222f', '1': '#45293f', '2': '#7a3045', '3': '#9e4539', '4': '#cd683d', '5': '#e6904e',
        'a': '#fdcbb0', 'b': '#fca790', 'c': '#e6904e', 'd': '#cd683d', 'e': '#2e222f', 'k': '#f68181'}

CABECA_FRENTE = [
    "....oooooo....",
    "..oo455443oo..",
    ".o4554444332o.",
    "o455444433322o",
    "o445443443322o",
    "o443aa4aa3322o",
    "o32aaaaaaab32o",
    "o3baeaaaaeab2o",
    "o2baeaaaaeab2o",
    "o1bkaaaaaakb1o",
    ".obbbaaaabbbo.",
    "..oocbbbbcoo..",
    "....oooooo....",
]

CABECA_COSTAS = [
    "....oooooo....",
    "..oo455443oo..",
    ".o4554444332o.",
    "o455444433322o",
    "o445444433322o",
    "o344443333221o",
    "o334433332221o",
    "o233333322211o",
    "o233332322211o",
    "o122322322111o",
    ".o1221212211o.",
    "..oooooooooo..",
]

CABECA_LADO = [
    "...oooooo.....",
    ".oo4554433oo..",
    "o455444443332o",
    "o45544444433o.",
    "o4444443aa43o.",
    "o3444aaaaaaao.",
    "o3343aaaaeaao.",
    "o2333aaaaeaaao",
    "o2232baakaabo.",
    "o1222bbaaabo..",
    ".o11obbbbco...",
    "..oo.oooooo...",
]


def _muda(linhas, trocas):
    l = [list(x) for x in linhas]
    for (y, x), ch in trocas.items():
        l[y][x] = ch
    return [''.join(x) for x in l]


CARAS_FRENTE = {
    'normal': CABECA_FRENTE,
    'fechado': _muda(CABECA_FRENTE, {(7, 4): 'a', (7, 9): 'a', (8, 3): 'e', (8, 10): 'e'}),
    'dor': _muda(CABECA_FRENTE, {(7, 4): 'a', (7, 3): 'e', (9, 3): 'e', (7, 9): 'a', (7, 10): 'e', (9, 10): 'e'}),
    'feliz': _muda(CABECA_FRENTE, {(8, 4): 'a', (8, 3): 'e', (8, 5): 'e', (8, 9): 'a', (8, 8): 'e', (8, 10): 'e'}),
}
CARAS_LADO = {
    'normal': CABECA_LADO,
    'fechado': _muda(CABECA_LADO, {(6, 9): 'a', (7, 10): 'e'}),
    'dor': _muda(CABECA_LADO, {(6, 9): 'a', (6, 10): 'e', (8, 10): 'e'}),
    'feliz': _muda(CABECA_LADO, {(7, 9): 'a', (7, 8): 'e', (7, 10): 'e'}),
}


# ---------- poses ----------

def pose(**k):
    p = dict(y=0, q=24, dx=0, me=(0, 0), md=(0, 0), pe=(0, 0), pd=(0, 0), frente=(), cara='normal',
             cauda=0, pernas=True, capa=False, bola=None)
    p.update(k)
    return p


def _capa_frente(P, y):
    P.append(Parte(poligono([(10, 16 + y), (22, 16 + y), (30, 13 + y), (27, 22 + y), (16, 25 + y), (5, 22 + y), (2, 13 + y)]),
                   'lilas', z=0))


def _bola(P, rodar):
    P.append(Parte(elipse(16, 24.5, 6.5, 6.0), 'azul', z=4))
    cab = {(15, 19), (16, 19), (17, 19), (14, 20), (15, 20), (16, 20), (17, 20), (18, 20), (14, 21), (15, 21), (16, 21), (17, 21)}
    if rodar:
        cab = {(31 - x, 48 - y) for x, y in cab}
        bota = elipse(11.5, 21.5, 2.2, 1.8)
    else:
        bota = elipse(20.5, 28, 2.2, 1.8)
    P.append(Parte(cab, 'cabelo', z=5))
    P.append(Parte(bota, 'couro', z=6))
    P.append(Parte(capsula(10, 26 if not rodar else 23, 13, 25 if not rodar else 24, 1.0), 'vermelho', z=7))


def frente(p, costas=False):
    P = []
    if p['bola'] is not None:
        _bola(P, p['bola'])
        return desenhar(P, T, T)
    y, q, dx = p['y'], p['q'], p['dx']
    if p['capa']:
        _capa_frente(P, y)
    if p['pernas']:
        for x, (fx, fy) in ((13.5, p['pe']), (18.5, p['pd'])):
            P.append(Parte(capsula(x + dx * .5, q, x + fx, 28.2 + fy, 1.7), 'cinza', z=1, volume='cilindro_v'))
            bx = x + fx + (-0.6 if x < 16 else 0.6)
            P.append(Parte(elipse(bx, 29.6 + fy, 2.4, 1.9), 'couro', z=2))
    P.append(Parte(retangulo(11 + dx, 16 + y, 20 + dx, q, canto=1), 'azul', z=4, volume='cilindro_v'))
    P.append(Parte(retangulo(11 + dx, q - 1, 20 + dx, q - 1), 'castanho', z=5, plano=True, separar=False))
    if not costas:
        P.append(Parte({(15 + dx, q - 1), (16 + dx, q - 1)}, None, z=6, separar=False, cor=FIVELA))
        P.append(Parte({(15 + dx, 19 + y), (15 + dx, 20 + y), (16 + dx, 21 + y)}, None, z=6, separar=False, cor='#484a77'))
    for lado, (ox, oy), base in (('e', p['me'], 9.6), ('d', p['md'], 22.4)):
        z = 14 if lado in p['frente'] else 3
        ombro = (base + dx + (0.3 if lado == 'e' else -0.3), 17.5 + y)
        mao = (base + dx + ox, 22.0 + y + oy)
        meio = (ombro[0] + (mao[0] - ombro[0]) * 0.75, ombro[1] + (mao[1] - ombro[1]) * 0.75)
        P.append(Parte(capsula(ombro[0], ombro[1], meio[0], meio[1], 1.45), 'azul', z=z, volume='cilindro_v'))
        P.append(Parte(elipse(mao[0], mao[1], 1.5, 1.4), 'pele', z=z + 0.5))
    linhas = CABECA_COSTAS if costas else CARAS_FRENTE[p['cara']]
    P.append(desenho_a_mao(linhas, 9 + dx, 4 + y, MAPA, z=9))
    P.append(Parte(elipse(16 + dx, 17.0 + y, 5.0, 1.5), 'vermelho', z=12, separar=False))
    if costas:
        P.append(Parte(capsula(16 + dx, 18 + y, 15.5 + dx + p['cauda'] * .5, 20.5 + y, 1.1), 'vermelho', z=13))
    else:
        P.append(Parte(capsula(18 + dx, 18 + y, 18.5 + dx, 19.5 + y, 1.0), 'vermelho', z=13))
    return desenhar(P, T, T)


def lado(p):
    """Virado para a direita. me = mão de longe, md = mão de perto; pe = pé de longe, pd = pé de perto."""
    P = []
    if p['bola'] is not None:
        _bola(P, p['bola'])
        return desenhar(P, T, T)
    y, q, dx = p['y'], p['q'], p['dx']
    if p['capa']:
        P.append(Parte(poligono([(15 + dx, 16 + y), (4 + dx, 9 + y), (1 + dx, 14 + y), (8 + dx, 20 + y), (15 + dx, 22 + y)]),
                       'lilas', z=0))
    ombro = (16 + dx, 17.5 + y)
    ox, oy = p['me']
    mao = (16 + dx + ox, 21.5 + y + oy)
    z = 14 if 'e' in p['frente'] else 0
    P.append(Parte(capsula(ombro[0], ombro[1], mao[0], mao[1], 1.3), AZUL_LONGE if z == 0 else 'azul', z=z, volume='cilindro_v', brilho=False))
    P.append(Parte(elipse(mao[0], mao[1] + 0.5, 1.4, 1.3), 'pele', z=z + 0.5))
    if p['pernas']:
        for (fx, fy), zz, rampa in ((p['pe'], 1, CALCAS_LONGE), (p['pd'], 2, 'cinza')):
            P.append(Parte(capsula(16 + dx * .5, q, 16 + fx, 28.2 + fy, 1.7), rampa, z=zz, volume='cilindro_v'))
            P.append(Parte(elipse(17.2 + fx, 29.6 + fy, 2.6, 1.9), 'couro', z=zz + 0.5))
    P.append(Parte(retangulo(13 + dx, 16 + y, 19 + dx, q, canto=1), 'azul', z=4, volume='cilindro_v'))
    P.append(Parte(retangulo(13 + dx, q - 1, 19 + dx, q - 1), 'castanho', z=5, plano=True, separar=False))
    P.append(desenho_a_mao(CARAS_LADO[p['cara']], 10 + dx, 4 + y, MAPA, z=9))
    P.append(Parte(elipse(16 + dx, 17.0 + y, 4.2, 1.5), 'vermelho', z=12, separar=False))
    P.append(Parte(capsula(12.5 + dx, 17.5 + y, 9.0 + dx, 18.0 + y + p['cauda'], 1.1), 'vermelho', z=11.5))
    ox, oy = p['md']
    mao = (16 + dx + ox, 22.0 + y + oy)
    P.append(Parte(capsula(ombro[0], ombro[1], mao[0], mao[1], 1.45), 'azul', z=13, volume='cilindro_v'))
    P.append(Parte(elipse(mao[0], mao[1], 1.5, 1.4), 'pele', z=13.5))
    return desenhar(P, T, T)


def deitar(img, sentido=-1, centro_y=None):
    """Roda 90° (para morrer, nadar) e volta a pôr o boneco no fundo do quadro (ou à altura centro_y)."""
    r = img.transpose(Image.ROTATE_270 if sentido < 0 else Image.ROTATE_90)
    peca = r.crop(r.getbbox())
    out = Image.new('RGBA', (T, T), (0, 0, 0, 0))
    x = (T - peca.width) // 2
    y = T - peca.height if centro_y is None else centro_y - peca.height // 2
    out.paste(peca, (x, y), peca)
    return out


# ---------- as animações ----------

def anim_frente():
    A = {}
    A['parado'] = [pose(y=b) for b in (0, 0, 1, 1)]
    A['andar'] = [pose(y=1), pose(pe=(0, -1), md=(0, -1)), pose(pe=(0, -2), md=(0, -1)),
                  pose(y=1), pose(pd=(0, -1), me=(0, -1)), pose(pd=(0, -2), me=(0, -1))]
    A['esquiva'] = [pose(y=2, q=25, me=(1, -1), md=(-1, -1)), pose(bola=False), pose(bola=True), pose(y=1, q=25)]
    A['dano'] = [pose(y=-1, cara='dor', me=(-1, -3), md=(1, -3)), pose(cara='dor')]
    A['morrer'] = [pose(cara='dor', me=(-1, -3), md=(1, -3)),
                   pose(y=3, q=26, cara='fechado', pe=(-1, -1), pd=(1, -1), me=(1, 1), md=(-1, 1)),
                   pose(y=5, q=27, cara='fechado', pe=(-2, -1), pd=(2, -1), me=(2, 2), md=(-2, 2)),
                   'deitado', 'deitado']
    A['recolher'] = [pose(y=2, q=25), pose(y=3, q=26, md=(-1, 5), frente='d'), pose(y=3, q=26, md=(-2, 6), frente='d'),
                     pose(y=1, md=(-3, -4), frente='d')]
    A['ataque_corte'] = [pose(md=(2, -10)), pose(y=1, md=(-8, 0), frente='d'),
                         pose(y=1, md=(-11, 1), frente='d'), pose()]
    A['ataque_pesado'] = [pose(y=1, me=(6, -15), md=(-6, -15), frente='ed'), pose(y=0, me=(6, -17), md=(-6, -17), frente='ed'),
                          pose(y=2, q=25, me=(5, 2), md=(-5, 2), frente='ed'), pose(y=2, q=25, me=(5, 3), md=(-5, 3), frente='ed'),
                          pose(y=1)]
    A['ataque_estocada'] = [pose(md=(-1, -3)), pose(y=1, md=(-6, 1), frente='d'), pose(y=1, md=(-6, 2), frente='d'), pose()]
    A['ataque_disparo'] = [pose(me=(5, -4), md=(-5, -4), frente='ed'), pose(me=(6, -5), md=(-3, -5), frente='ed'),
                           pose(me=(6, -5), md=(-1, -4), frente='ed'), pose()]
    A['ataque_magia'] = [pose(me=(4, -3), md=(-4, -3), frente='ed'), pose(md=(0, -14), frente='d', cara='fechado'),
                         pose(y=1, me=(5, -2), md=(-5, -2), frente='ed'), pose()]
    A['ataque_soco'] = [pose(me=(4, -3), md=(-4, -3), frente='ed'), pose(y=1, me=(4, -3), md=(-6, 0), frente='ed'),
                        pose(y=1, me=(6, 0), md=(-4, -3), frente='ed'), pose(me=(4, -3), md=(-4, -3), frente='ed')]
    A['nadar'] = [pose(y=6, pernas=False, me=(0, -12), frente='e'), pose(y=7, pernas=False, me=(2, -6), md=(0, -2), frente='e'),
                  pose(y=7, pernas=False, md=(0, -6)), pose(y=6, pernas=False, md=(0, -12), frente='d'),
                  pose(y=7, pernas=False, md=(-2, -6), me=(0, -2), frente='d'), pose(y=7, pernas=False, me=(0, -6))]
    A['planar'] = [pose(capa=True, me=(-4, -8), md=(4, -8), pe=(-1, 0), pd=(1, 0)),
                   pose(capa=True, y=1, me=(-4, -7), md=(4, -7), pe=(-1, -1), pd=(1, -1))]
    A['montar'] = [pose(y=1, pe=(-3, -3), pd=(3, -3), me=(2, -2), md=(-2, -2)), pose(y=2, pe=(-3, -2), pd=(3, -2), me=(2, -1), md=(-2, -1))]
    A['pescar'] = [pose(me=(6, -12), md=(-6, -12), frente='ed'), pose(me=(5, -3), md=(-5, -3), frente='ed'),
                   pose(me=(4, -2), md=(-4, -2), frente='ed'), pose(me=(5, -10), md=(-5, -10), frente='ed', cara='fechado')]
    A['beber'] = [pose(md=(-5, -6), frente='d'), pose(y=-1, md=(-5, -8), frente='d', cara='fechado'), pose(md=(-3, -4), frente='d', cara='feliz')]
    A['celebrar'] = [pose(y=1, me=(0, -12), md=(0, -12), frente='ed', cara='feliz'),
                     pose(y=-2, q=22, pe=(0, -2), pd=(0, -2), me=(-2, -15), md=(2, -15), frente='ed', cara='feliz'),
                     pose(y=-1, q=23, pe=(0, -1), pd=(0, -1), me=(-1, -14), md=(1, -14), frente='ed', cara='feliz'),
                     pose(me=(0, -12), md=(0, -12), frente='ed', cara='feliz')]
    A['sentar'] = [pose(y=4, q=27, pe=(-2, -1), pd=(2, -1), me=(2, 2), md=(-2, 2))]
    return A


def anim_lado():
    A = {}
    A['parado'] = [pose(y=b, cauda=b) for b in (0, 0, 1, 1)]
    A['andar'] = [pose(y=1, pd=(2, 0), pe=(-2, 0), md=(-1.2, 0), me=(1.2, 0)),
                  pose(pd=(1, -1), pe=(-1, 0), md=(-0.6, 0), me=(0.6, 0), cauda=1),
                  pose(pd=(0, -2), pe=(0, 0)),
                  pose(y=1, pd=(-2, 0), pe=(2, 0), md=(1.2, 0), me=(-1.2, 0)),
                  pose(pd=(-1, 0), pe=(1, -1), md=(0.6, 0), me=(-0.6, 0), cauda=1),
                  pose(pd=(0, 0), pe=(0, -2))]
    A['esquiva'] = [pose(y=2, q=25, dx=1, md=(2, -2), pd=(2, 0), pe=(-2, 0)), pose(bola=False), pose(bola=True),
                    pose(y=1, q=25, pd=(1, 0), pe=(-1, 0))]
    A['dano'] = [pose(dx=-1, y=-1, cara='dor', md=(-3, -3), me=(-3, -2), cauda=-1), pose(cara='dor')]
    A['morrer'] = [pose(dx=-1, cara='dor', md=(-3, -3)), pose(y=3, q=26, cara='fechado', pd=(2, -1), pe=(-1, -1), md=(2, 2)),
                   pose(y=5, q=27, dx=1, cara='fechado', pd=(3, -1), pe=(-2, -1), md=(3, 3)), 'deitado', 'deitado']
    A['recolher'] = [pose(y=2, q=25, md=(2, 0)), pose(y=3, q=26, dx=1, md=(5, 5), pd=(2, 0)), pose(y=3, q=26, dx=1, md=(6, 6), pd=(2, 0)),
                     pose(y=1, md=(2, -5))]
    A['ataque_corte'] = [pose(md=(-4, -11), me=(-2, -1)), pose(dx=1, md=(7, -4), pd=(2, 0), pe=(-2, 0)),
                         pose(dx=1, y=1, md=(7, 1), pd=(2, 0), pe=(-2, 0)), pose()]
    A['ataque_pesado'] = [pose(y=1, md=(-3, -14), me=(-1, -14)), pose(dx=-1, md=(-5, -15), me=(-3, -15)),
                          pose(y=2, q=25, dx=2, md=(8, 1), me=(7, 2), pd=(3, 0), pe=(-2, 0)),
                          pose(y=2, q=25, dx=2, md=(8, 2), me=(7, 3), pd=(3, 0), pe=(-2, 0)), pose(y=1)]
    A['ataque_estocada'] = [pose(dx=-1, md=(-3, -2), me=(-1, -2)), pose(dx=2, md=(9, -3), me=(6, -3), pd=(3, 0), pe=(-3, 0)),
                            pose(dx=2, md=(10, -3), me=(7, -3), pd=(3, 0), pe=(-3, 0)), pose()]
    A['ataque_disparo'] = [pose(me=(7, -5), md=(3, -5), frente='e'), pose(me=(8, -5), md=(-2, -5), frente='e'),
                           pose(me=(8, -5), md=(-4, -6), frente='e'), pose()]
    A['ataque_magia'] = [pose(md=(3, -3), me=(2, -3)), pose(md=(2, -14), cara='fechado'), pose(dx=1, md=(8, -5), me=(7, -4)), pose()]
    A['ataque_soco'] = [pose(md=(3, -4), me=(4, -3)), pose(dx=1, md=(9, -4), me=(3, -3), pd=(2, 0), pe=(-2, 0)),
                        pose(dx=1, md=(2, -4), me=(9, -4), frente='e', pd=(2, 0), pe=(-2, 0)), pose(md=(3, -4), me=(4, -3))]
    A['nadar'] = [pose(md=(8, -6), me=(-4, 2), pd=(-1, 0), pe=(1, 0)), pose(md=(5, 0), me=(0, 0)),
                  pose(md=(-3, 2), me=(5, -4), pd=(1, 0), pe=(-1, 0)), pose(md=(-4, 2), me=(8, -6), pd=(1, 0), pe=(-1, 0)),
                  pose(md=(0, 0), me=(5, 0)), pose(md=(5, -4), me=(-3, 2), pd=(-1, 0), pe=(1, 0))]
    A['planar'] = [pose(capa=True, md=(3, -9), me=(1, -9), pd=(-1, 0), pe=(-3, -1), cauda=-1),
                   pose(capa=True, y=1, md=(3, -8), me=(1, -8), pd=(-1, -1), pe=(-3, -2))]
    A['montar'] = [pose(y=1, pd=(4, -3), pe=(3, -3), md=(3, -2)), pose(y=2, pd=(4, -2), pe=(3, -2), md=(3, -1))]
    A['pescar'] = [pose(md=(-3, -12), me=(-2, -12)), pose(dx=1, md=(8, -6), me=(7, -6)), pose(md=(6, -3), me=(5, -3)),
                   pose(dx=-1, md=(0, -10), me=(1, -10), cara='fechado')]
    A['beber'] = [pose(md=(4, -6)), pose(y=-1, md=(5, -9), cara='fechado'), pose(md=(3, -4), cara='feliz')]
    A['celebrar'] = [pose(y=1, md=(1, -13), me=(1, -12), cara='feliz'),
                     pose(y=-2, q=22, pd=(1, -2), pe=(-1, -2), md=(2, -15), me=(2, -14), cara='feliz'),
                     pose(y=-1, q=23, pd=(0, -1), pe=(0, -1), md=(1, -14), me=(1, -13), cara='feliz'),
                     pose(md=(1, -13), me=(1, -12), cara='feliz')]
    A['sentar'] = [pose(y=4, q=27, pd=(4, -1), pe=(3, -1), md=(3, 2))]
    return A


def gerar():
    out = {}
    AF, AL = anim_frente(), anim_lado()
    for nome in AF:
        fr, co, la = [], [], []
        for pf, pl in zip(AF[nome], AL[nome]):
            if pf == 'deitado':
                img = deitar(lado(pose(cara='fechado')), -1)
                fr.append(img)
                co.append(img)
                la.append(img)
                continue
            fr.append(frente(pf))
            co.append(frente(pf, costas=True))
            la.append(lado(pl))
        if nome == 'nadar':
            la = [deitar(f, -1, centro_y=20) for f in la]
        out[nome + '_baixo'] = fr
        out[nome + '_cima'] = co
        out[nome + '_lado'] = la
    return out


if __name__ == '__main__':
    pasta = os.path.join('arte', 'heroi')
    os.makedirs(pasta, exist_ok=True)
    an = gerar()
    for nome, frames in an.items():
        tira(frames).save(os.path.join(pasta, f'heroi_{nome}.png'))
    if len(sys.argv) > 1:
        nomes = sorted({n.rsplit('_', 1)[0] for n in an})
        previa_gif([[an[n + '_baixo'], an[n + '_lado'], an[n + '_cima']] for n in nomes], sys.argv[1], escala=4, ms=140)
    print('ok', len(an), 'tiras')
