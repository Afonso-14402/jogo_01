"""Desenha as peças 3D (.glb) em pixel art para a vista 2D, sem as fotografar: lê os triângulos (glb_ler.py) e pinta
cada face à mão (por código), no estilo da referência Aranha-Mãe (docs/ARTE.md):
  - paleta Resurrect 64, rampas de 5 tons; luz de cima à esquerda, um pouco de frente;
  - padrões pelo nome do material: telhas em fiadas, tijolos e lajes, tábuas, troncos, folhagem, neve, cristal...;
  - aresta clara no cimo das paredes; contorno escuro (#2e222f) à volta e onde uma coisa fica à frente de outra.

A projeção é a do jogo (docs/PROGRAMACAO.md, 4A): 1 m = 16 px, o ponto (x, y, z) fica em (x, z − 0,8·y) no ecrã.
O tamanho da imagem e a âncora seguem as mesmas contas de glb_sprites.gd, por isso as peças ficam no mesmo sítio.
Saída: arte/sprites2d/<caminho sem .glb>_r<rotação>.png e dados/sprites2d.json (substitui as fotografias).

Uso: python3 ferramentas/arte/glb2d.py [ficheiro.glb | pasta ...] [--previa saida.png]
     (sem argumentos: todas as peças que estão em dados/sprites2d.json)
"""
import glob
import json
import math
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from glb_ler import ler_glb

PX = 16.0
SOBE = 0.8
RAIZ = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = (0x2e, 0x22, 0x2f)
LUZ = np.array([-0.55, 0.75, 0.45])
LUZ = LUZ / np.linalg.norm(LUZ)
UMA_ROTACAO = ['/kit/']
QUATRO = ['ponte', 'passadico', 'cais', 'escadas', 'chao_castelo']

# rampas da paleta Resurrect 64 (do escuro para o claro)
CADEIAS = [
    '2e222f 3e3546 625565 7f708a 9babb2 c7dcd0 ffffff',
    '2e222f 45293f 694f62 966c6c ab947a c7dcd0',
    '2e222f 4c3e24 676633 a2a947 d5e04b fbff86',
    '313638 374e4a 547e64 92a984 b2ba90 c7dcd0',
    '2e222f 165a4c 239063 1ebc73 91db69 cddf6c',
    '0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 ffffff',
    '2e222f 323353 484a77 4d65b4 4d9be6 8fd3ff ffffff',
    '2e222f 45293f 6b3e75 905ea9 a884f3 eaaded',
    '45293f 753c54 a24b6f cf657f ed8099 fca790',
    '45293f 831c5d c32454 f04f78 f68181 fca790',
    '2e222f 6e2727 b33831 ea4f36 f57d4a fca790',
    '45293f 7a3045 9e4539 cd683d e6904e fbb954 fbff86',
    '6e2727 ae2334 e83b3b fb6b1d f79617 f9c22b fbff86',
    '313638 0b5e65 0b8a8f 4d9be6 8fd3ff ffffff',
]
CADEIAS = [[tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) for c in s.split()] for s in CADEIAS]


def _dist(a, b):
    return 3 * (a[0] - b[0]) ** 2 + 4 * (a[1] - b[1]) ** 2 + 2 * (a[2] - b[2]) ** 2


def rampa_de(cor):
    """Devolve (cadeia, índice do tom do meio) para uma cor."""
    melhor = None
    for c in CADEIAS:
        for i, t in enumerate(c):
            d = _dist(t, cor)
            if melhor is None or d < melhor[0] or (d == melhor[0] and melhor[2] in (0, len(melhor[1]) - 1) and 0 < i < len(c) - 1):
                melhor = (d, c, i)
    return melhor[1], melhor[2]


def lum(c):
    return 0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2]


# --------------------------------------------------------------------------------------------------------------
# estilo de cada material (pelo nome do material e da peça)
# --------------------------------------------------------------------------------------------------------------

NATURAL = ('rocha', 'pedra_', 'pedregulho', 'calhau', 'minerio', 'estalag', 'basalto', 'obsidiana', 'rochedo', 'penedo',
           'veio', 'monte_minerio', 'meteoro', 'fragmento', 'ilha', 'falesia')


def estilo(nome_mat, nome_peca):
    n = nome_mat.lower()
    p = nome_peca.lower()
    tem = lambda *ks: any(k in n for k in ks)
    if tem('janela', 'vitral'):
        return 'janela'
    if tem('telhado', 'telha', 'ardosia', 'cupula'):
        if tem('neve'):
            return 'neve_plana'
        return 'telhas' if not tem('folha', 'colmo', 'palha') else 'colmo'
    if tem('colmo', 'palha'):
        return 'colmo'
    if tem('folha', 'copa', 'arbusto', 'relva', 'erva', 'alga', 'musgo', 'liana', 'hera', 'sebe'):
        return 'folhagem'
    if tem('neve', 'nuvem', 'algodao'):
        if any(k in p for k in ('casa', 'salao', 'sauna', 'cabana', 'torre', 'mosteiro', 'telhado', 'capela', 'forja')):
            return 'neve_plana'   # neve em cima de telhados: faces planas (vê-se a forma do telhado)
        return 'neve'
    if tem('cristal', 'gelo', 'vidro', 'luz', 'prisma', 'diamante', 'gema'):
        return 'cristal'
    if tem('metal', 'ferro', 'ouro', 'cobre', 'prata', 'bronze', 'latao', 'aco', 'mitril', 'oricalco'):
        return 'metal'
    if tem('tronco', 'casca'):
        return 'troncos'
    if tem('madeira', 'tabua', 'porta', 'ponte', 'cais', 'naufragio', 'passadico', 'barco', 'remo', 'mesa', 'banco',
           'caixote', 'barril', 'estante', 'ebano', 'carvalho', 'pinho', 'bambu', 'palma'):
        return 'tabuas'
    if tem('toldo', 'tecido', 'pano', 'tapete', 'bandeira', 'vela_', 'cortina', 'tenda', 'lona'):
        return 'tecido'
    if any(k in p for k in NATURAL) and not tem('parede', 'muralha', 'tijolo', 'coluna', 'lajes', 'calcada'):
        return 'rocha'
    if tem('tijolo', 'muralha', 'castelo', 'calcada', 'lajes', 'marmore', 'pedra', 'coluna', 'torre', 'escada', 'arenito',
           'templo', 'ruina', 'adobe_bloco', 'obsidiana', 'granito'):
        return 'tijolos'
    if tem('parede', 'reboco', 'adobe', 'branco', 'cal', 'estuque'):
        return 'reboco'
    if tem('lava', 'fogo', 'brasa', 'chama', 'magma'):
        return 'brilho'
    if tem('agua', 'mar', 'lago'):
        return 'agua'
    if tem('cogumelo', 'coral', 'carne', 'osso', 'concha', 'ovo', 'bola'):
        return 'liso'
    return 'liso'


SUAVE = ('folhagem', 'neve', 'liso', 'agua', 'rocha')   # normais suavizadas (formas redondas, sem facetas)


def h2(x, y, s=0):
    """Hash inteiro determinista (para padrões)."""
    v = (int(x) * 374761393 + int(y) * 668265263 + s * 2246822519) & 0xffffffff
    v = ((v ^ (v >> 13)) * 1274126177) & 0xffffffff
    return (v ^ (v >> 16)) & 0xffff


def padrao(est, px, py, wpos, n):
    """Ajuste de tom (-2..+1) por píxel, conforme o padrão do material. wpos: posição no mundo (m); n: normal."""
    x, y, z = wpos
    vertical = abs(n[1]) < 0.5
    em_x = abs(n[0]) < abs(n[2])            # a face corre ao longo de x (de frente para sul/norte)
    u = (x if em_x else z) * PX              # coordenada ao longo da face (px)
    v = y * PX if vertical else (z if em_x else x) * PX
    ui, vi = math.floor(u), math.floor(v)
    if est == 'telhas':
        # fiadas largas (4 px) ao longo da descida: cada fiada clara em cima e com sombra na beira de baixo;
        # juntas curtas a cada 8 px, desencontradas de fiada para fiada
        ao_longo = x if abs(n[0]) < 0.5 else z
        desce = (y * PX) * 1.3
        fila = math.floor(desce / 4.0)
        dentro = desce / 4.0 - fila
        if dentro < 0.25:
            return -1
        pos = ao_longo * PX + (fila % 2) * 4.0
        if pos % 8.0 < 1.0 and dentro < 0.75:
            return -1
        frente = abs(n[2]) > abs(n[0])
        return 1 if frente and dentro > 0.8 and h2(math.floor(pos / 8), fila) % 3 == 0 else 0
    if est == 'colmo':
        if h2(math.floor(u / 1), math.floor((y * PX) / 3)) % 4 == 0:
            return -1
        if h2(math.floor(u), math.floor(y * PX)) % 11 == 0:
            return 1
        return 0
    if est == 'tijolos':
        if vertical:
            fila = math.floor(v / 4.0)
            off = 4 if fila % 2 else 0
            if v - fila * 4.0 < 1.0:
                return -1
            if (u + off) % 8.0 < 1.0:
                return -1
            if h2(math.floor((u + off) / 8), fila) % 5 == 0:
                return -1 if h2(ui, vi) % 3 == 0 else 0
            return 0
        # chão / topo: lajes 8x8 desencontradas
        fila = math.floor(z * PX / 8.0)
        off = 4 if fila % 2 else 0
        if (z * PX) % 8.0 < 1.0 or (x * PX + off) % 8.0 < 1.0:
            return -1
        return 0
    if est == 'reboco':
        k = h2(ui, vi, 3) % 97
        return -1 if k < 2 else 0
    if est == 'tabuas':
        if vertical:   # tábuas ao alto nas paredes e portas
            if u % 4.0 < 1.0:
                return -1
            if h2(math.floor(u / 4), math.floor(v / 9)) % 7 == 0 and h2(ui, vi) % 5 == 0:
                return -1
            return 0
        k = (z if abs(n[0]) < 0.3 else x) * PX
        if k % 4.0 < 1.0:
            return -1
        return 1 if h2(ui, vi, 5) % 29 == 0 else 0
    if est == 'troncos':
        if vertical and (abs(n[0]) + abs(n[2])) > 0.9 and abs(n[1]) < 0.2 and (x, y) == (x, y):
            fila = v % 5.0
            if fila < 1.0:
                return -1   # junta escura entre troncos
            if fila < 2.0:
                return 1    # o lado de cima do tronco apanha luz
            return 0
        return -1 if h2(ui, vi, 7) % 6 == 0 else 0
    if est == 'folhagem':
        # tufos de folhas em grelha "tremida" de 5 px: cada tufo tem um centro claro (do lado da luz) e uma
        # sombra em baixo à direita; entre tufos fica o tom de base
        cx, cy = px // 5, py // 5
        best = None
        for gx in (cx - 1, cx, cx + 1):
            for gy in (cy - 1, cy, cy + 1):
                ox = gx * 5 + h2(gx, gy, 11) % 5
                oy = gy * 5 + h2(gx, gy, 12) % 5
                d = (px - ox) ** 2 + (py - oy) ** 2
                if best is None or d < best[0]:
                    best = (d, px - ox, py - oy)
        d, dx, dy = best
        if dx in (-1, 0) and dy in (-1, 0):
            return 1
        if d <= 5 and dx >= 1 and dy >= 1:
            return -1
        return 0
    if est == 'neve_plana':
        # camadas de neve ao longo da descida do telhado (montinhos com sombra por baixo) e brilhos
        desce = y * PX * 1.3
        fila = math.floor(desce / 6.0)
        onda = math.sin((x + z) * PX * 0.35 + fila * 1.7) * 1.2
        d = desce - fila * 6.0 + onda
        if 0.0 <= d < 1.0 and h2(math.floor((x + z) * PX / 7), fila) % 3:
            return -1
        return 1 if h2(px, py, 13) % 47 == 0 else 0
    if est == 'neve':
        return 1 if h2(px, py, 13) % 61 == 0 else 0
    if est == 'rocha':
        # fissuras curtas (riscos escuros de 3-4 px em diagonal) e pintas claras raras
        cx, cy = math.floor(px / 7), math.floor(py / 7)
        if h2(cx, cy, 19) % 5 == 0:
            ox, oy = h2(cx, cy, 23) % 4, h2(cx, cy, 29) % 4
            dxp, dyp = px - cx * 7 - ox, py - cy * 7 - oy
            if 0 <= dxp < 4 and dyp == dxp // 2:
                return -1
        k = h2(px, py, 17) % 53
        return 1 if k == 52 else 0
    if est == 'tecido':
        return -1 if (u % 6.0) < 3.0 and abs(n[1]) < 0.9 else 0
    if est == 'metal':
        return 0
    return 0


# --------------------------------------------------------------------------------------------------------------
# desenhar uma peça
# --------------------------------------------------------------------------------------------------------------

def rodar(p, r):
    a = r * math.pi / 2
    c, s = math.cos(a), math.sin(a)
    # rotação à volta de y (como rotation.y no Godot): x' = x·c + z·s ; z' = −x·s + z·c
    return np.array([p[0] * c + p[2] * s, p[1], -p[0] * s + p[2] * c])


def desenhar(caminho, r=0):
    tris, mats = ler_glb(caminho)
    nome_peca = os.path.basename(caminho)
    if not tris:
        return None
    # triângulos rodados e normais (de face; e suaves por posição para os materiais redondos)
    T = []
    for (a, b, c, mi, na, nb, nc) in tris:
        a, b, c = rodar(a, r), rodar(b, r), rodar(c, r)
        nf = np.cross(b - a, c - a)
        ln = np.linalg.norm(nf)
        if ln < 1e-9:
            continue
        nf = nf / ln
        T.append([a, b, c, mi, nf])
    ests = [estilo(m['nome'], nome_peca) for m in mats]
    for i, m in enumerate(mats):   # telhado coberto de neve (cor quase branca): desenha-se como neve
        base = m['cores'][0] if m['cores'] else m['cor']
        if ests[i] == 'telhas' and lum(base) > 200:
            ests[i] = 'neve_plana'
    # normais suaves: média das normais das faces que partilham a posição (por material)
    acum = {}   # posição -> normais das faces que lá se tocam (para suavizar só entre faces parecidas)
    for t in T:
        if ests[t[3]] in SUAVE:
            for v in t[:3]:
                k = (t[3], round(v[0], 3), round(v[1], 3), round(v[2], 3))
                acum.setdefault(k, []).append(t[4])
    # caixa e tamanho da imagem (as mesmas contas de glb_sprites.gd)
    pts = np.array([v for t in T for v in t[:3]])
    x0, x1 = pts[:, 0].min(), pts[:, 0].max()
    s = pts[:, 2] - SOBE * pts[:, 1]
    s0, s1 = s.min(), s.max()
    w = int(min(1024, max(4, math.ceil((x1 - x0) * PX) + 4)))
    h = int(min(1024, max(4, math.ceil((s1 - s0) * PX) + 4)))
    cx, cs = (x0 + x1) / 2, (s0 + s1) / 2
    ax = (0 - cx) * PX + w / 2
    ay = (0 - cs) * PX + h / 2

    def ecra(p):
        return np.array([(p[0] - cx) * PX + w / 2, (p[2] - SOBE * p[1] - cs) * PX + h / 2])

    prof = np.full((h, w), -np.inf)
    idm = np.full((h, w), -1, dtype=int)
    nor = np.zeros((h, w, 3))
    mundo = np.zeros((h, w, 3))
    peca_id = np.full((h, w), -1, dtype=int)
    gy, gx = np.mgrid[0:h, 0:w]
    gx = gx + 0.5
    gy = gy + 0.5
    for ti, (a, b, c, mi, nf) in enumerate(T):
        pa, pb, pc = ecra(a), ecra(b), ecra(c)
        bx0 = max(0, int(math.floor(min(pa[0], pb[0], pc[0]))))
        bx1 = min(w - 1, int(math.ceil(max(pa[0], pb[0], pc[0]))))
        by0 = max(0, int(math.floor(min(pa[1], pb[1], pc[1]))))
        by1 = min(h - 1, int(math.ceil(max(pa[1], pb[1], pc[1]))))
        if bx1 < bx0 or by1 < by0:
            continue
        X = gx[by0:by1 + 1, bx0:bx1 + 1]
        Y = gy[by0:by1 + 1, bx0:bx1 + 1]
        den = (pb[1] - pc[1]) * (pa[0] - pc[0]) + (pc[0] - pb[0]) * (pa[1] - pc[1])
        if abs(den) < 1e-9:
            continue   # face de lado (não se vê nesta projeção)
        l0 = ((pb[1] - pc[1]) * (X - pc[0]) + (pc[0] - pb[0]) * (Y - pc[1])) / den
        l1 = ((pc[1] - pa[1]) * (X - pc[0]) + (pa[0] - pc[0]) * (Y - pc[1])) / den
        l2 = 1 - l0 - l1
        dentro = (l0 >= -1e-4) & (l1 >= -1e-4) & (l2 >= -1e-4)
        if not dentro.any():
            continue
        W3 = l0[..., None] * a + l1[..., None] * b + l2[..., None] * c   # posição no mundo
        d = W3[..., 1] + SOBE * W3[..., 2]                                  # mais = mais perto de quem vê
        zona = prof[by0:by1 + 1, bx0:bx1 + 1]
        ganha = dentro & (d > zona + 1e-6)
        if not ganha.any():
            continue
        zona[ganha] = d[ganha]
        idm[by0:by1 + 1, bx0:bx1 + 1][ganha] = mi
        peca_id[by0:by1 + 1, bx0:bx1 + 1][ganha] = ti
        mundo[by0:by1 + 1, bx0:bx1 + 1][ganha] = W3[ganha]
        if ests[mi] in SUAVE:
            ns = []
            for v in (a, b, c):
                k = (mi, round(v[0], 3), round(v[1], 3), round(v[2], 3))
                viz = [q for q in acum.get(k, [nf]) if float(q @ nf) > 0.3]   # "auto-smooth" a ~70°: caixas ficam com esquinas
                nv = np.sum(viz, axis=0) if viz else nf
                ns.append(nv / max(1e-9, np.linalg.norm(nv)))
            N = l0[..., None] * ns[0] + l1[..., None] * ns[1] + l2[..., None] * ns[2]
            N = N / np.maximum(np.linalg.norm(N, axis=-1, keepdims=True), 1e-9)
            nor[by0:by1 + 1, bx0:bx1 + 1][ganha] = N[ganha]
        else:
            nor[by0:by1 + 1, bx0:bx1 + 1][ganha] = nf
    # rampas dos materiais
    rampas = []
    acentos = []
    for m in mats:
        base = m['cores'][0] if m['cores'] else m['cor']
        if m['cores'] and len(m['cores']) > 1:   # o tom do meio: a cor mais frequente
            base = m['cores'][0]
        cad, im = rampa_de(base)
        if ests[len(rampas)] == 'folhagem':
            im -= 1   # folhagem: o meio um tom mais escuro (o claro fica para os tufos ao sol)
        rampas.append((cad, max(1, min(len(cad) - 2, im))))   # o meio tem sempre um tom mais claro e um mais escuro
        # cor de destaque da textura (pintas de minério, manchas, pedras preciosas): muito diferente da dominante
        ac = None
        for c, f in zip(m['cores'][1:], m.get('freq', [])[1:]):
            if f > 0.012 and _dist(c, base) > 9000 and rampa_de(c)[0] is not cad:
                taxa = 0.2 if any(k in m['nome'] for k in ('minerio', 'veio', 'cristal')) else min(0.22, max(f * 2.5, 0.05))
                ac = (rampa_de(c), taxa)
                break
        acentos.append(ac)
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    P = img.load()
    cheio = idm >= 0
    for yy in range(h):
        for xx in range(w):
            mi = idm[yy, xx]
            if mi < 0:
                continue
            n = nor[yy, xx]
            est = ests[mi]
            dl = float(n @ LUZ)
            if est in ('brilho',) or mats[mi]['emissao']:
                k = 1 if dl > 0.3 else 0
            else:
                k = 1 if dl > 0.80 else (0 if dl > 0.42 else (-1 if dl > 0.12 else -2))
                if n[1] > 0.3:
                    k = max(k, -1)   # o que olha para cima (telhados, topos) nunca fica quase preto
                if est in ('cristal', 'metal') and dl > 0.9:
                    k = 2
            # aresta clara no cimo das paredes (uma face vertical com uma face de cima logo acima)
            if abs(n[1]) < 0.5 and yy > 0 and idm[yy - 1, xx] >= 0 and nor[yy - 1, xx][1] > 0.6 and \
                    abs(prof[yy - 1, xx] - prof[yy, xx]) < 0.3:
                k = max(k, 0) + 1
            else:
                k += padrao(est, xx, yy, mundo[yy, xx], n)
            if est == 'janela':
                k = 1 if (xx + yy) % 5 == 0 else 0
            cad, im = rampas[mi]
            ac = acentos[mi]
            if ac and est in ('rocha', 'liso', 'cristal', 'folhagem', 'neve'):
                # pintas de 2x2 nas células de 4x4 (quantas: conforme a cor aparece na textura)
                cx4, cy4 = xx // 4, yy // 4
                if (h2(cx4, cy4, 31) % 1000) / 1000.0 < ac[1] * 1.6 and (xx % 4) < 2 and (yy % 4) < 2:
                    cad, im = ac[0]
                    k = max(-1, min(1, k))
            P[xx, yy] = cad[max(0, min(len(cad) - 1, im + k))] + (255,)
    # contorno de dentro: onde uma coisa fica à frente de outra (salto de profundidade) ou muda o material
    for yy in range(h):
        for xx in range(w):
            if not cheio[yy, xx]:
                continue
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                vx, vy = xx + dx, yy + dy
                if not (0 <= vx < w and 0 <= vy < h) or not cheio[vy, vx]:
                    continue
                if prof[vy, vx] > prof[yy, xx] + 0.45 and peca_id[vy, vx] != peca_id[yy, xx]:
                    P[xx, yy] = OUT + (255,)   # este píxel está atrás do vizinho: linha escura na beira de trás
                    break
                if idm[vy, vx] != idm[yy, xx] and prof[vy, vx] > prof[yy, xx] + 0.02:
                    cad, im = rampas[idm[yy, xx]]
                    P[xx, yy] = cad[max(0, im - 2)] + (255,)
                    break
                # dobra entre duas faces do mesmo material (cumeeira, esquinas): linha suave no lado mais escuro
                if idm[vy, vx] == idm[yy, xx] and ests[idm[yy, xx]] not in SUAVE and \
                        float(nor[vy, vx] @ nor[yy, xx]) < 0.75 and float(nor[yy, xx] @ LUZ) < float(nor[vy, vx] @ LUZ):
                    cad, im = rampas[idm[yy, xx]]
                    P[xx, yy] = cad[max(0, im - 2)] + (255,)
                    break
    # contorno de fora
    borda = set()
    for yy in range(h):
        for xx in range(w):
            if cheio[yy, xx]:
                continue
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                vx, vy = xx + dx, yy + dy
                if 0 <= vx < w and 0 <= vy < h and cheio[vy, vx]:
                    borda.add((xx, yy))
                    break
    for (xx, yy) in borda:
        P[xx, yy] = OUT + (255,)
    return img, [w, h, round(ax * 2) / 2, round(ay * 2) / 2]


def rotacoes(caminho):
    c = caminho.replace('\\', '/')
    if any(k in c for k in UMA_ROTACAO) and not any(k in os.path.basename(c) for k in QUATRO):
        return 1
    return 4


# peças do kit que passam a usar os desenhos à mão da natureza da região (dados/natureza.json)
TROCA_NATUREZA = [
    (('cogumelo_gigante',), 'cogumelo_gigante'),
    (('arvore', 'palmeira', 'pinheiro', 'acacia', 'cacto', 'mangue', 'ebano'), 'arvore'),
    (('arbusto', 'folhas_gigantes', 'vegetacao', 'feto'), 'mato'),
    (('rocha_1', 'rocha_2', 'rocha_3', 'rocha_musgo', 'rocha_neve', 'rocha_vermelha', 'rocha_vulcanica', 'rocha_mare'), 'rocha'),
    (('erva', 'juncos'), 'erva'),
    (('flores', 'flor_'), 'flores'),
]
_natureza = None


def natureza_para(caminho):
    """Se a peça do kit tiver um desenho à mão na natureza da região, devolve o caminho do PNG; senão None."""
    global _natureza
    c = caminho.replace('\\', '/')
    if '/kit/' not in c:
        return None
    nome = os.path.basename(c)[4:-4]   # sem "rNN_" nem ".glb"
    if 'flutuante' in nome or 'cortavel' in nome and 'arvore' not in nome:
        return None
    if _natureza is None:
        _natureza = json.load(open(os.path.join(RAIZ, 'dados', 'natureza.json'), encoding='utf-8'))
    try:
        reg = str(int(os.path.basename(c)[1:3]))
    except ValueError:
        return None
    plantas = _natureza.get(reg, {}).get('plantas', {})
    for chaves, grupo in TROCA_NATUREZA:
        if any(k in nome for k in chaves):
            if grupo == 'cogumelo_gigante':
                f = os.path.join(RAIZ, 'arte', 'regioes', os.path.basename(os.path.dirname(os.path.dirname(c))), 'natureza', 'cogumelo_gigante.png')
                return f if os.path.exists(f) else None
            lista = plantas.get(grupo, [])
            if not lista:
                return None
            parecidos = [x for x in lista if any(w in os.path.basename(x) for w in nome.split('_') if len(w) > 3)]
            lista = parecidos or lista   # (a palmeira prefere o desenho da palmeira, o cacto o do cacto...)
            n = nome.rsplit('_', 1)[-1]
            i = (int(n) - 1) if n.isdigit() else sum(map(ord, nome))
            return os.path.join(RAIZ, lista[i % len(lista)][len('res://'):])
    return None


CHAO_KIT = ('chao', 'lama', 'areia', 'neve', 'relva', 'terra', 'cinza', 'agua_pantano', 'fundo_mar', 'mar_raso', 'gelo_liso',
            'gelo_fino', 'erva_seca', 'musgo')


def chao_plano(caminho):
    c = caminho.replace('\\', '/')
    nome = os.path.basename(c)
    fora = ('falesia', 'parede', 'rocha', 'flor', 'castelo', 'vidro', 'luz', 'banco', 'erva')
    return '/kit/' in c and any(k in nome for k in CHAO_KIT) and not any(k in nome for k in fora)


def suavizar_chao(img):
    """Uma peça plana de chão (manchas de lama, relva, areia...): sem contorno e com as beiras tremidas, para se
    misturar com o chão à volta em vez de parecer um ladrilho."""
    w, h = img.size
    P = img.load()
    out = img.copy()
    Q = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = P[x, y]
            if a == 0:
                continue
            if (r, g, b) == OUT:   # tira o contorno
                Q[x, y] = (0, 0, 0, 0)
                continue
            d = min(x, y, w - 1 - x, h - 1 - y)   # distância à beira
            if d < 4 and h2(x, y, 41) % 4 >= d:  # beira tremida (pontilhado que desaparece para fora)
                Q[x, y] = (0, 0, 0, 0)
    return out


def fazer(caminho, mapa):
    rel = os.path.relpath(caminho, os.path.join(RAIZ, 'arte')).replace('\\', '/')
    chave = 'res://arte/' + rel
    e = mapa.get(chave, {})
    feito_mao = natureza_para(caminho)
    for r in range(rotacoes(caminho)):
        if feito_mao:   # o desenho à mão: a âncora (a origem da peça) fica no meio, em baixo
            im = Image.open(feito_mao).convert('RGBA')
            res = (im, [im.width, im.height, im.width / 2, im.height - 2])
        else:
            res = desenhar(caminho, r)
            if res and chao_plano(caminho):
                res = (suavizar_chao(res[0]), res[1])
        if res is None:
            continue
        img, info = res
        destino = os.path.join(RAIZ, 'arte', 'sprites2d', rel[:-4] + f'_r{r}.png')
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        img.save(destino)
        e[f'r{r}'] = info
    mapa[chave] = e
    return e


def main():
    args = [a for a in sys.argv[1:]]
    previa = None
    if '--previa' in args:
        i = args.index('--previa')
        previa = args[i + 1]
        del args[i:i + 2]
    caminho_mapa = os.path.join(RAIZ, 'dados', 'sprites2d.json')
    mapa = json.load(open(caminho_mapa, encoding='utf-8'))
    ficheiros = []
    for a in args:
        if a.endswith('.glb'):
            ficheiros.append(a)
        else:
            ficheiros += sorted(glob.glob(os.path.join(a, '**', '*.glb'), recursive=True))
    if not args:
        ficheiros = [os.path.join(RAIZ, k[len('res://'):]) for k in mapa]
    feitos = []
    for i, f in enumerate(ficheiros):
        try:
            fazer(f, mapa)
            feitos.append(f)
        except Exception as ex:
            print('ERRO', f, ex)
        if (i + 1) % 50 == 0:
            print(i + 1, '/', len(ficheiros))
    json.dump(mapa, open(caminho_mapa, 'w', encoding='utf-8'), separators=(',', ':'), ensure_ascii=False)
    print('ok', len(feitos), 'peças')
    if previa:
        ims = []
        for f in feitos[:60]:
            rel = os.path.relpath(f, os.path.join(RAIZ, 'arte'))[:-4]
            ims.append(Image.open(os.path.join(RAIZ, 'arte', 'sprites2d', rel + '_r0.png')))
        cel = min(220, max(max(i.size) for i in ims))
        cols = 8
        folha = Image.new('RGBA', (cols * cel, ((len(ims) + cols - 1) // cols) * cel), (70, 100, 70, 255))
        for k, im in enumerate(ims):
            im = im.copy()
            im.thumbnail((cel, cel), Image.NEAREST)
            folha.alpha_composite(im, ((k % cols) * cel + (cel - im.width) // 2, (k // cols) * cel + cel - im.height))
        e = max(1, 1600 // folha.width)
        folha.resize((folha.width * e, folha.height * e), Image.NEAREST).save(previa)


if __name__ == '__main__':
    main()
