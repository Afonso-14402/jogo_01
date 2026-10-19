"""Retratos 64x64 para a caixa de diálogo: normal, feliz, zangado, triste.
Usam os mesmos estilos dos sprites (humano.py / npcs_ascendia.py). Saída: arte/retratos/{nome}_{emocao}.png

Uso: python3 ferramentas/arte/retratos.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, RAMPAS
from humano import PELES, CABELOS
from npcs_ascendia import ESTILOS

W = 64
OUT = '#2e222f'
EMOCOES = ['normal', 'feliz', 'zangado', 'triste']


def _r(n):
    return RAMPAS[n] if isinstance(n, str) else n


def px(P, pts, cor, z=50):
    P.append(Parte({(int(x), int(y)) for x, y in pts}, None, z=z, separar=False, cor=cor))


def retrato(e, emocao):
    P = []
    pele = PELES[e.get('pele', 'clara')]
    cab = CABELOS[e.get('cor_cabelo', 'castanho')]
    estilo = e.get('cabelo', 'curto')
    ac = [a if isinstance(a, str) else a[0] for a in e.get('acessorios', [])]
    acor = {a[0]: a[1] for a in e.get('acessorios', []) if not isinstance(a, str)}
    cx, cy = 32, 28
    larg = e.get('largo', 0) * 2
    # ombros e roupa
    P.append(Parte(elipse(cx, 66, 24 + larg, 16), _r(e.get('roupa', 'azul')), z=1))
    if e.get('capa'):
        P.append(Parte(elipse(cx, 68, 28 + larg, 16), _r(e['capa']), z=0.5))
    if e.get('avental'):
        P.append(Parte(retangulo(cx - 9, 54, cx + 9, 64), _r(e['avental']), z=1.5, plano=True))
    if e.get('lenco'):
        P.append(Parte(elipse(cx, 50, 12, 4), _r(e['lenco']), z=6))
    # cabelo de trás (comprido, rabo, carrapito)
    if estilo == 'comprido':
        P.append(Parte(retangulo(cx - 16, 20, cx + 16, 52, canto=1), cab, z=1.8))
    if estilo == 'rabo':
        P.append(Parte(capsula(cx + 14, 18, cx + 20, 40, 4), cab, z=1.8))
    if estilo == 'carrapito':
        P.append(Parte(elipse(cx, 8, 7, 6), cab, z=1.8))
    if 'capuz' in ac:
        P.append(Parte(elipse(cx, 30, 21, 23), _r(acor.get('capuz', 'preto')), z=1.9))
    # pescoço e cabeça
    P.append(Parte(retangulo(cx - 5, 40, cx + 5, 50), pele, z=2, volume='cilindro_v', luz=0.3, brilho=False))
    if 'orelha_elfo' in ac:
        P.append(Parte(poligono([(cx - 13, 28), (cx - 22, 20), (cx - 13, 33)]), pele, z=2.5, luz=0.3))
        P.append(Parte(poligono([(cx + 13, 28), (cx + 22, 20), (cx + 13, 33)]), pele, z=2.5, luz=0.3))
    else:
        for s in (-1, 1):
            P.append(Parte(elipse(cx + s * 15, 31, 2.5, 3.5), pele, z=2.5, luz=0.3))
    P.append(Parte(elipse(cx, cy + 1, 14.5, 16), pele, z=3, luz=0.8, brilho=False))
    # cabelo da frente
    topo = {p for p in elipse(cx, cy - 2, 16, 15.5) if p[1] <= cy - 7}
    if estilo == 'careca':
        cabelo = set()
    elif estilo == 'tapado':
        cabelo = topo | poligono([(cx - 16, cy - 8), (cx + 4, cy - 8), (cx - 2, cy + 8), (cx - 16, cy + 12)])
    else:
        franja = poligono([(cx - 16, cy - 9), (cx + 16, cy - 9), (cx + 15, cy - 1), (cx + 10, cy - 5), (cx + 6, cy - 2),
                           (cx + 2, cy - 6), (cx - 3, cy - 1), (cx - 7, cy - 5), (cx - 12, cy), (cx - 16, cy - 2)])
        lados = capsula(cx - 15, cy - 8, cx - 15, cy + 6, 2.5) | capsula(cx + 15, cy - 8, cx + 15, cy + 6, 2.5)
        cabelo = topo | franja | lados
        if estilo == 'espetado':
            for i, sx in enumerate((-12, -5, 2, 9)):
                cabelo |= poligono([(cx + sx - 4, cy - 12), (cx + sx + 1, cy - 24 - (i % 2) * 3), (cx + sx + 4, cy - 12)])
        if estilo == 'carrapito':
            cabelo = topo | capsula(cx - 15, cy - 8, cx - 15, cy, 2) | capsula(cx + 15, cy - 8, cx + 15, cy, 2)
        if estilo == 'comprido':
            cabelo |= capsula(cx - 15, cy - 6, cx - 16, cy + 22, 3) | capsula(cx + 15, cy - 6, cx + 16, cy + 22, 3)
    if cabelo:
        P.append(Parte(cabelo, cab, z=4))
    # barba
    barba = e.get('barba')
    cbarba = CABELOS[e.get('cor_barba', e.get('cor_cabelo', 'castanho'))]
    if barba == 'curta':
        P.append(Parte({p for p in elipse(cx, cy + 9, 15, 10) if p[1] >= cy + 6} - elipse(cx, cy + 9, 4, 2.5), cbarba, z=5))
    elif barba == 'longa':
        P.append(Parte(({p for p in elipse(cx, cy + 12, 15, 14) if p[1] >= cy + 6} | poligono([(cx - 10, cy + 20), (cx + 10, cy + 20), (cx, cy + 34)]))
                       - elipse(cx, cy + 9, 4, 2.5), cbarba, z=5))
    elif barba == 'trancas':
        b = {p for p in elipse(cx, cy + 12, 16, 13) if p[1] >= cy + 5} - elipse(cx, cy + 9, 4, 2.5)
        for sx in (-6, 0, 6):
            b |= capsula(cx + sx, cy + 20, cx + sx, cy + 31, 2)
        P.append(Parte(b, cbarba, z=5))
        for sx in (-6, 0, 6):
            px(P, [(cx + sx, cy + 26), (cx + sx - 1, cy + 26), (cx + sx + 1, cy + 26)], '#9babb2', 55)
    elif barba == 'bigode':
        P.append(Parte(capsula(cx - 7, cy + 8, cx - 1, cy + 7, 1.6) | capsula(cx + 1, cy + 7, cx + 7, cy + 8, 1.6), cbarba, z=5))
    # olhos, sobrancelhas, boca
    olho_cor = e.get('olhos_cor', '#45293f')
    ey = cy + 1
    for s in (-1, 1):
        ex = cx + s * 6
        if emocao == 'feliz':
            px(P, [(ex - 2, ey + 1), (ex - 1, ey), (ex, ey), (ex + 1, ey), (ex + 2, ey + 1)], OUT)
        elif emocao == 'triste':
            px(P, [(ex - 2, ey + 1), (ex - 1, ey + 1), (ex, ey + 1), (ex + 1, ey + 1), (ex + 2, ey + 1)], OUT)
            px(P, [(ex - 1, ey + 2), (ex, ey + 2), (ex + 1, ey + 2), (ex - 1, ey + 3), (ex, ey + 3), (ex + 1, ey + 3)], olho_cor)
        else:
            px(P, [(ex + a, ey + b) for a in (-1, 0, 1) for b in (0, 1, 2, 3)], olho_cor)
            px(P, [(ex - 2, ey + b) for b in (1, 2)] + [(ex + 2, ey + b) for b in (1, 2)] + [(ex + a, ey - 1) for a in (-1, 0, 1)], OUT)
            px(P, [(ex - 1, ey), (ex - 1, ey + 1)], '#ffffff', 51)
        # sobrancelhas
        if emocao == 'zangado':
            sb = [(ex - 2 * s, ey - 5), (ex - s, ey - 4), (ex, ey - 4), (ex + s, ey - 3), (ex + 2 * s, ey - 3)]
            sb = [(ex + (a - ex) * -1, b) for a, b in sb]
        elif emocao == 'triste':
            sb = [(ex - 2 * s, ey - 3), (ex - s, ey - 3), (ex, ey - 4), (ex + s, ey - 4), (ex + 2 * s, ey - 5)]
            sb = [(ex + (a - ex) * -1, b) for a, b in sb]
        else:
            sb = [(ex - 2, ey - 4), (ex - 1, ey - 5), (ex, ey - 5), (ex + 1, ey - 5), (ex + 2, ey - 4)]
        px(P, sb, cab[1] if estilo != 'careca' else pele[1], 52)
        px(P, [(ex + 2 * s + s, ey + 5), (ex + 3 * s + s, ey + 5)], '#f68181', 49)
    # boca
    my = cy + 9
    if barba in ('curta', 'longa', 'trancas'):
        my += 0
    if emocao == 'normal':
        px(P, [(cx - 1, my), (cx, my), (cx + 1, my)], pele[0], 53)
    elif emocao == 'feliz':
        px(P, [(cx - 3, my - 1), (cx + 3, my - 1)], pele[0], 53)
        px(P, [(cx - 2, my), (cx - 1, my), (cx, my), (cx + 1, my), (cx + 2, my), (cx - 1, my + 1), (cx, my + 1), (cx + 1, my + 1)], '#7a3045', 53)
        px(P, [(cx - 1, my), (cx, my), (cx + 1, my)], '#ffffff', 54)
    elif emocao == 'zangado':
        px(P, [(cx - 3, my + 1), (cx - 2, my), (cx - 1, my), (cx, my), (cx + 1, my), (cx + 2, my), (cx + 3, my + 1)], pele[0], 53)
    elif emocao == 'triste':
        px(P, [(cx - 2, my + 1), (cx - 1, my), (cx, my), (cx + 1, my), (cx + 2, my + 1)], pele[0], 53)
        px(P, [(cx - 7, ey + 5), (cx - 7, ey + 6)], '#8fd3ff', 55)
    # acessórios
    if 'oculos' in ac:
        c = acor.get('oculos', '#9babb2')
        for s in (-1, 1):
            ex = cx + s * 6
            anel = {p for p in elipse(ex + 0.5, ey + 1.5, 4.2, 3.8) if p not in elipse(ex + 0.5, ey + 1.5, 3.2, 2.8)}
            px(P, anel, c, 56)
        px(P, [(cx - 1, ey + 1), (cx, ey + 1), (cx + 1, ey + 1)], c, 56)
    if 'oculos_testa' in ac:
        for s in (-1, 1):
            P.append(Parte(elipse(cx + s * 6, cy - 9, 4, 3), 'agua', z=57))
        px(P, [(x, cy - 9) for x in range(cx - 16, cx + 17) if abs(x - cx) > 9 or abs(x - cx) < 2], '#3e3546', 56)
    if 'cicatriz' in ac:
        px(P, [(cx + 6 + i % 2, ey - 4 + i) for i in range(10)], '#cf657f', 58)
    if 'sardas' in ac:
        px(P, [(cx - 9, ey + 6), (cx - 7, ey + 7), (cx + 7, ey + 7), (cx + 9, ey + 6)], pele[1], 49)
    if 'fita' in ac:
        c = _r('amarelo')
        P.append(Parte(poligono([(cx + 10, cy - 12), (cx + 18, cy - 17), (cx + 18, cy - 7)]) | poligono([(cx + 10, cy - 12), (cx + 4, cy - 18), (cx + 4, cy - 7)]), c, z=60))
    if 'chapeu_pena' in ac or 'chapeu_palha' in ac:
        palha = 'chapeu_palha' in ac
        rampa = _r(acor.get('chapeu_pena', 'castanho')) if not palha else _r('amarelo')
        P.append(Parte(elipse(cx, cy - 11, 22 if palha else 19, 4), rampa, z=60))
        P.append(Parte(retangulo(cx - 11, cy - 24, cx + 11, cy - 11, canto=1), rampa, z=61))
        if palha:
            for x in (cx - 6, cx, cx + 6):
                P.append(Parte(elipse(x, cy - 13, 1.8, 1.8), 'rosa', z=62))
        else:
            P.append(Parte(capsula(cx + 8, cy - 14, cx + 20, cy - 30, 1.8), 'vermelho', z=62))
    if 'lenco_cabeca' in ac:
        rampa = _r(acor.get('lenco_cabeca', 'azul'))
        P.append(Parte({p for p in elipse(cx, cy - 3, 17, 15) if p[1] <= cy - 6} | capsula(cx + 14, cy - 6, cx + 18, cy + 4, 2.5), rampa, z=63))
    if 'capuz' in ac:
        rampa = _r(acor.get('capuz', 'preto'))
        P.append(Parte({p for p in elipse(cx, cy - 1, 19, 19) if p[1] <= cy - 8}, rampa, z=63))
    if 'coroa' in ac:
        P.append(Parte(poligono([(cx - 10, cy - 13), (cx - 10, cy - 22), (cx - 5, cy - 17), (cx, cy - 25), (cx + 5, cy - 17), (cx + 10, cy - 22), (cx + 10, cy - 13)]), 'ouro', z=63))
    if 'lapis' in ac:
        P.append(Parte(capsula(cx + 10, cy - 14, cx + 18, cy - 22, 1.2), 'amarelo', z=59))
    if 'chapeu_cogumelo' in ac:   # fungoides
        m = {q for q in elipse(cx, cy - 6, 27, 18) if q[1] <= cy - 4}
        P.append(Parte(m, _r(acor.get('chapeu_cogumelo', 'vermelho')), z=60))
        for x, y in ((cx - 14, cy - 14), (cx + 6, cy - 19), (cx + 16, cy - 9), (cx - 3, cy - 8)):
            P.append(Parte(elipse(x, y, 2.5, 2), 'branco', z=61, separar=False))
    if 'sapo' in ac:              # homens-sapo: olhos saltados
        for s in (-1, 1):
            P.append(Parte(elipse(cx + s * 9, cy - 14, 5, 4.5), PELES['verde'], z=58))
            P.append(Parte(elipse(cx + s * 9, cy - 15, 1.6, 2), ['#2e222f'] * 5, z=59, separar=False))
    if e.get('asas'):             # alados
        for s in (-1, 1):
            P.append(Parte(elipse(cx + s * 26, 50, 9, 14), _r(e['asas']), z=0.2))
    im = desenhar(P, W, W)
    if e.get('fantasma'):
        pix = im.load()
        for y in range(W):
            for x in range(W):
                if pix[x, y][3]:
                    pix[x, y] = pix[x, y][:3] + (180,)
    return im


HEROI = dict(cabelo='curto', cor_cabelo='castanho', roupa='azul', lenco='vermelho')

if __name__ == '__main__':
    pasta = os.path.join('arte', 'retratos')
    os.makedirs(pasta, exist_ok=True)
    todos = dict(ESTILOS)
    todos['heroi'] = HEROI
    for nome, e in todos.items():
        for em in EMOCOES:
            retrato(e, em).save(os.path.join(pasta, f'{nome}_{em}.png'))
    print('ok', len(todos), 'retratos x 4')
