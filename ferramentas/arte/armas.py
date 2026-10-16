"""Armas: sprite vertical (a apontar para cima, punho no centro em baixo) + ícone 16x16 na diagonal.
Regras: docs/ARTE.md, secção 4. Tipos e tamanhos: docs/ARMAS.md.

Cada TIPO de arma é uma lista de formas ao longo de um eixo (t = distância desde o fundo do punho,
w = meia-largura). O mesmo desenho serve para o sprite (vertical) e para o ícone (diagonal, mais pequeno).
Os materiais (rampas do motor) mudam as cores: o mesmo gerador faz as armas de todas as regiões.

Uso: python3 ferramentas/arte/armas.py [regiao] [previa.png]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, poligono, elipse, desenhar, RAMPAS

TAM = {'espada': 32, 'espada_grande': 48, 'adaga': 32, 'katana': 48, 'machado': 32, 'martelo': 48,
       'lanca': 48, 'foice': 48, 'arco': 32, 'besta': 32, 'cajado': 48, 'manoplas': 32}


# ---------- formas ao longo do eixo ----------
# ('seg', t0, t1, w0, w1, rampa, z, desvio0, desvio1)  -> trapézio
# ('poli', [(t, w), ...], rampa, z)                      -> polígono livre no espaço (t, w)
# ('circ', t, w, r, rampa, z)                            -> círculo

def seg(t0, t1, w0, w1, r, z=1, d0=0, d1=0):
    return ('seg', t0, t1, w0, w1, r, z, d0, d1)


def poli(pts, r, z=2):
    return ('poli', pts, r, z)


def circ(t, r, rampa, z=3, w=0):
    return ('circ', t, w, r, rampa, z)


def lamina_ponta(t0, t1, w, ponta, r, z=2):
    return poli([(t0, -w), (t1, -w * 0.9), (t1 + ponta, 0), (t1, w * 0.9), (t0, w)], r, z)


def tipo_formas(tipo, m):
    """m: dict com 'metal', 'cabo', 'punho', 'enfeite' (rampas)."""
    M, C, P, E = m['metal'], m['cabo'], m['punho'], m['enfeite']
    if tipo == 'espada':
        return [circ(1.2, 1.5, E), seg(1.5, 7.5, 1.0, 1.0, P), seg(7.5, 9, 4.2, 4.2, E, 3),
                lamina_ponta(9, 27, 1.9, 3.5, M)]
    if tipo == 'espada_grande':
        return [circ(1.6, 2.2, E), seg(2, 11, 1.4, 1.4, P), seg(11, 13.5, 6.5, 6.5, E, 3),
                lamina_ponta(13.5, 40, 3.2, 5, M), seg(16, 36, 0.5, 0.5, ['#2e222f'] * 5, 4)]
    if tipo == 'adaga':
        return [circ(2.2, 1.4, E), seg(2.5, 8.5, 1.0, 1.0, P), seg(8.5, 9.8, 2.8, 2.8, E, 3), lamina_ponta(9.8, 19, 1.5, 3, M)]
    if tipo == 'katana':
        return [seg(1, 13, 1.2, 1.2, P), circ(13.5, 3.0, E, 3), seg(15, 40, 1.4, 1.2, M, 2, 0, 1.8),
                poli([(40, 0.6), (40, 3.0), (44.5, 3.4)], M, 2)]
    if tipo == 'machado':
        return [seg(0.5, 27, 1.1, 1.1, C), poli([(17, 1), (14.5, 7.5), (19, 9.5), (25, 9.5), (29.5, 7.5), (27, 1)], M, 3),
                poli([(19, -1), (21, -4.5), (23, -1)], M, 3), circ(27.5, 1.4, E, 4)]
    if tipo == 'martelo':
        return [seg(0.5, 33, 1.3, 1.3, C), seg(2, 9, 1.6, 1.6, P, 2), seg(31, 43, 7.5, 7.5, M, 3),
                seg(31, 43, 1.0, 1.0, E, 4)]
    if tipo == 'lanca':
        return [seg(0.5, 36, 0.9, 0.9, C), seg(10, 15, 1.3, 1.3, P, 2), seg(35, 37.5, 1.9, 1.9, E, 3),
                poli([(37.5, -2.6), (41, -2.8), (46.5, 0), (41, 2.8), (37.5, 2.6)], M, 3)]
    if tipo == 'foice':
        return [seg(0.5, 39, 1.0, 1.0, C), seg(4, 10, 1.4, 1.4, P, 2), circ(38.5, 2.0, E, 4),
                poli([(36, 0), (41, -1), (44, -6), (43, -13), (39, -18), (38, -14), (40, -8), (38, -3)], M, 3)]
    if tipo == 'arco':
        pts = []
        for i in range(0, 15):
            a = i / 14
            t = 2 + a * 28
            w = -3 + math.sin(a * math.pi) * 7
            pts.append((t, w))
        braco = [(t, w + 0.9) for t, w in pts] + [(t, w - 0.9) for t, w in reversed(pts)]
        return [poli(braco, C, 2), seg(2, 30, 0.35, 0.35, ['#c7dcd0'] * 5, 1, -3, -3), seg(13, 19, 1.6, 1.6, P, 3, 3.9, 3.9)]
    if tipo == 'besta':
        pts = [(19 + math.sin(i / 12 * math.pi) * 3, -12 + i * 2) for i in range(13)]
        arc = [(t + 0.9, w) for t, w in pts] + [(t - 0.9, w) for t, w in reversed(pts)]
        return [seg(1, 24, 1.8, 1.4, C), poli(arc, M, 3), seg(19.2, 19.8, 12, 12, ['#c7dcd0'] * 5, 2), circ(21.5, 1.6, E, 4),
                seg(10, 26, 0.6, 0.6, ['#625565', '#7f708a', '#9babb2', '#c7dcd0', '#c7dcd0'], 5)]
    if tipo == 'cajado':
        return [seg(0.5, 37, 1.2, 1.0, C), seg(14, 20, 1.6, 1.6, P, 2),
                poli([(36, -1), (38, -4.5), (42, -4), (40, -1.5), (40, 1.5), (42, 4), (38, 4.5), (36, 1)], M, 3),
                circ(41.5, 3.2, E, 4)]
    raise ValueError(tipo)


def _pixel(t, w, ori, eixo, perp, k):
    return (ori[0] + (eixo[0] * t + perp[0] * w) * k, ori[1] + (eixo[1] * t + perp[1] * w) * k)


def _rampa(r):
    return RAMPAS[r] if isinstance(r, str) else r


def render(formas, W, ori, eixo, perp, k):
    partes = []
    for f in formas:
        if f[0] == 'seg':
            _, t0, t1, w0, w1, r, z, d0, d1 = f
            pts = [(t0, -w0 + d0), (t1, -w1 + d1), (t1, w1 + d1), (t0, w0 + d0)]
            m = poligono([_pixel(t, w, ori, eixo, perp, k) for t, w in pts])
            vol = 'cilindro_v'
        elif f[0] == 'poli':
            _, pts, r, z = f
            m = poligono([_pixel(t, w, ori, eixo, perp, k) for t, w in pts])
            vol = 'esfera'
        else:
            _, t, w, rad, r, z = f
            cx, cy = _pixel(t, w, ori, eixo, perp, k)
            m = elipse(cx, cy, rad * k, rad * k)
            vol = 'esfera'
        if not m:
            cx, cy = _pixel((f[1] if f[0] != 'poli' else f[1][0][0]), 0, ori, eixo, perp, k)
            m = {(int(cx), int(cy))}
        partes.append(Parte(m, _rampa(r), z=z, volume=vol if eixo == (0, -1) else 'esfera'))
    return desenhar(partes, W, W)


def sprite(tipo, m):
    W = TAM[tipo]
    formas = tipo_formas(tipo, m)
    if tipo == 'arco' or tipo == 'besta':
        ori = (W / 2, W - 0.5) if tipo == 'besta' else (W / 2 + 0.5, W - 0.5)
    else:
        ori = (W / 2, W - 0.5)
    return render(formas, W, ori, (0, -1), (1, 0), 1.0)


def icone(tipo, m):
    formas = tipo_formas(tipo, m)
    comprimento = max(max(p[0] for p in f[1]) if f[0] == 'poli' else (f[2] if f[0] == 'seg' else f[1]) for f in formas)
    k = 18.5 / comprimento
    s = math.sqrt(0.5)
    return render(formas, 16, (1.5, 14.5), (s, -s), (s, s), k)


def manoplas(m, W=32, ic=False):
    """As manoplas não têm eixo: desenha-se o punho fechado."""
    k = 1.0 if not ic else 0.5
    o = 0 if not ic else -0.5
    P = [Parte(elipse((16 + o) * k, (24 + o) * k, 7 * k, 5 * k), _rampa(m['punho']), z=1),
         Parte(elipse((16 + o) * k, (15 + o) * k, 8.5 * k, 7.5 * k), _rampa(m['metal']), z=2)]
    for dx in (-5, -1.7, 1.7, 5):
        P.append(Parte(elipse((16 + dx + o) * k, (9.5 + o) * k, 1.9 * k, 1.9 * k), _rampa(m['enfeite']), z=3))
    P.append(Parte(elipse((22.5 + o) * k, (17 + o) * k, 2.4 * k, 3.5 * k), _rampa(m['metal']), z=3))
    return desenhar(P, W if not ic else 16, W if not ic else 16)


def fazer(tipo, m):
    if tipo == 'manoplas':
        return manoplas(m), manoplas(m, ic=True)
    return sprite(tipo, m), icone(tipo, m)


# ---------- as armas de cada região ----------

def mat(metal, cabo='madeira', punho='couro', enfeite=None):
    return {'metal': metal, 'cabo': cabo, 'punho': punho, 'enfeite': enfeite or metal}


TIPOS_NORMAIS = ['espada', 'espada_grande', 'adaga', 'katana', 'machado', 'martelo', 'lanca', 'foice', 'arco', 'besta', 'cajado', 'manoplas']


def normais(material_id, metal, gema='verde'):
    out = {}
    for t in TIPOS_NORMAIS:
        m = mat(metal)
        if t == 'cajado':
            m['enfeite'] = gema
        if t in ('arco',):
            m['cabo'] = 'madeira'
        out[f'{t}_{material_id}'] = (t, m)
    return out


REGIOES = {
    1: dict(pasta='r01', normais=('cobre', 'cobre', 'verde'), especiais={
        # únicas dos bosses
        'presa_javali_rei': ('machado', mat('branco', 'madeira', 'couro', 'castanho')),
        'raiz_ancestral': ('cajado', mat('madeira', ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], 'verde_esc', 'verde')),
        # dos guardiões
        'chifre_partido': ('adaga', mat('branco', 'madeira', 'couro', 'castanho')),
        'pena_noturna': ('arco', mat('preto', 'preto', 'roxo', 'roxo')),
        'martelo_pinca': ('martelo', mat('vermelho', 'madeira', 'couro', 'laranja')),
        'esporo_luz': ('cajado', mat('vermelho', 'branco', 'branco', 'musgo')),
        'ferrao_de_mel': ('lanca', mat('amarelo', 'madeira', 'castanho', 'preto')),
        'tronco_velho': ('espada_grande', mat('madeira', 'madeira', 'verde_esc', 'verde_esc')),
        'lamina_cavaleiro_esquecido': ('espada', mat('ferro', 'madeira', 'couro', 'verde_esc')),
        'foice_bruma': ('foice', mat('branco', 'cinza', 'agua', 'agua')),
        # secreta
        'arco_raiz_viva': ('arco', mat('verde', ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], 'verde', 'verde')),
    }),
}


def gerar(regiao):
    R = REGIOES[regiao]
    pasta = os.path.join('arte', 'armas')
    os.makedirs(pasta, exist_ok=True)
    lista = dict(normais(*R['normais']))
    lista.update(R['especiais'])
    feitos = {}
    for nome, (tipo, m) in lista.items():
        s, i = fazer(tipo, m)
        s.save(os.path.join(pasta, f'{nome}.png'))
        i.save(os.path.join(pasta, f'{nome}_icone.png'))
        feitos[nome] = (s, i)
    return feitos


if __name__ == '__main__':
    reg = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    feitos = gerar(reg)
    print('ok', len(feitos), 'armas')
    if len(sys.argv) > 2:
        from PIL import Image
        n = len(feitos)
        E = 4
        folha = Image.new('RGBA', (8 * 52 * E, ((n + 7) // 8) * 70 * E), (50, 51, 83, 255))
        for idx, (nome, (s, i)) in enumerate(feitos.items()):
            x, y = (idx % 8) * 52 * E, (idx // 8) * 70 * E
            ss = s.resize((s.width * E, s.height * E), Image.NEAREST)
            folha.paste(ss, (x, y), ss)
            ii = i.resize((16 * E, 16 * E), Image.NEAREST)
            folha.paste(ii, (x, y + 50 * E), ii)
        folha.save(sys.argv[2])
