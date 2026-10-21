"""Põe no jogo os monstros redesenhados (arte/propostas/monstros/, aprovados pelo utilizador): a partir da animação
"parado" nova de cada criatura faz TODAS as animações que o jogo usa, com os mesmos nomes, o mesmo tamanho de quadro
e o mesmo número de quadros das antigas (assim o código do jogo não muda).

As animações saem do próprio desenho, só com movimentos de píxeis inteiros (nunca desfoca):
  mover        sobe e desce e inclina-se para a frente e para trás (passos, asas, rastejar)
  atacar       prepara-se (inclina-se para trás) e avança com o golpe no meio
  ataque_1..3  como atacar: 2 = avanço maior, 3 = com salto
  dano         recua inclinado para trás
  morrer       recua, cai de lado (deitar) e desfaz-se (dissolver)
  atordoado    abana com estrelinhas por cima da cabeça
  mudar_fase   pulsa com um contorno da cor principal da criatura
  especiais    pelo nome: investida/carga/salto (avanço grande), grito/uivo (ondas), esporos/fogo/veneno/magia
               (partículas da cor da criatura), acordar/disfarce/teletransporte/enterrar (aparece ou desaparece)
Ficam de fora o Ent Ancião (desenhado à mão em ent_anciao.py) e as personagens da história que também são NPC
(o Kai e O Desistente).

Uso: python3 ferramentas/arte/animar_monstros.py [região ...]     (sem nada: todas)
"""
import glob
import os
import random
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from motor import deitar, dissolver  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PROPOSTAS = os.path.join(RAIZ, 'arte', 'propostas', 'monstros')
FORA = {'ent_anciao', 'kai', 'kai_duelo_da_historia', 'o_desistente'}
ESTRELA = (251, 255, 134, 255)
OUT = (46, 34, 47, 255)


def quadros(tira):
    h = tira.height
    return [tira.crop((i * h, 0, (i + 1) * h, h)) for i in range(max(1, tira.width // h))]


def inclinar(img, k, dx=0, dy=0):
    """Desloca cada fila de píxeis: as de cima k píxeis (as de baixo 0), mais dx/dy para tudo."""
    w, h = img.size
    bb = img.getbbox()
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    if not bb:
        return out
    topo, base = bb[1], bb[3]
    alt = max(1, base - topo)
    for y in range(topo, base):
        off = round(k * (base - y) / alt) + dx
        linha = img.crop((0, y, w, y + 1))
        out.paste(linha, (off, y + dy), linha)
    return out


def cor_principal(img):
    """A cor mais viva e mais usada do desenho (para partículas e contornos)."""
    conta = {}
    for (r, g, b, a) in img.getdata():
        if a and (r, g, b) != OUT[:3]:
            viva = max(r, g, b) - min(r, g, b)
            conta[(r, g, b)] = conta.get((r, g, b), 0) + 1 + viva / 40
    if not conta:
        return (255, 255, 255, 255)
    return max(conta, key=conta.get) + (255,)


def estrelas(img, fase):
    out = img.copy()
    bb = img.getbbox()
    if not bb:
        return out
    cx, y = (bb[0] + bb[2]) // 2, max(2, bb[1] - 3)
    r = max(3, (bb[2] - bb[0]) // 5)
    for i in range(2):
        a = fase + i * 2
        x = cx + [-r, 0, r, 0][a % 4]
        yy = y + [0, -1, 0, 1][a % 4]
        for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + dx < img.width and 0 <= yy + dy < img.height:
                out.putpixel((x + dx, yy + dy), ESTRELA)
    return out


def particulas(img, cor, fase, n=10, semente=1):
    """Pontinhos da cor da criatura a sair para a frente (direita) e para cima."""
    out = img.copy()
    bb = img.getbbox()
    if not bb:
        return out
    rnd = random.Random(semente)
    w, h = img.size
    for _ in range(n):
        x0 = rnd.randint((bb[0] + bb[2]) // 2, bb[2])
        y0 = rnd.randint(bb[1], (bb[1] + bb[3]) // 2)
        x = x0 + fase * rnd.randint(1, 3)
        y = y0 - fase * rnd.randint(0, 2)
        if 0 <= x < w - 1 and 0 <= y < h:
            out.putpixel((x, y), cor)
            if rnd.random() < 0.4:
                out.putpixel((x + 1, y), cor)
    return out


def ondas(img, fase):
    """Arcos a sair da frente da cabeça (grito, uivo, rugido)."""
    out = img.copy()
    bb = img.getbbox()
    if not bb:
        return out
    cx, cy = bb[2], bb[1] + (bb[3] - bb[1]) // 3
    for k in range(fase % 3 + 1):
        r = 3 + k * 3 + fase
        for dy in range(-r, r + 1):
            x = cx + int((r * r - dy * dy) ** 0.5 * 0.6)
            if 0 <= x < img.width and 0 <= cy + dy < img.height and abs(dy) < r * 0.8:
                out.putpixel((x, cy + dy), ESTRELA if k == 0 else (199, 220, 208, 255))
    return out


def contorno(img, cor):
    out = img.copy()
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if px[x, y][3] == 0 and any(0 <= x + dx < w and 0 <= y + dy < h and px[x + dx, y + dy][3]
                                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                out.putpixel((x, y), cor)
    return out


def amostrar(seq, n):
    """Escolhe n passos de uma sequência (mantém o primeiro e o do meio)."""
    if n >= len(seq):
        return seq + [seq[-1]] * (n - len(seq))
    return [seq[round(i * (len(seq) - 1) / max(1, n - 1))] for i in range(n)]


def anim(nome, P, n):
    """As n imagens da animação 'nome' a partir dos quadros parado P."""
    cor = cor_principal(P[0])
    f = lambda i: P[i % len(P)]  # noqa: E731
    golpe = [(-1, -1, 0), (-2, -2, 0), (-3, -2, 0), (3, 2, 0), (4, 3, 0), (2, 1, 0), (0, 0, 0)]
    if nome == 'parado':
        return [f(round(i * len(P) / n)) for i in range(n)]
    if nome == 'mover':
        passos = [(1, 0, 0), (0, 0, -1), (-1, 0, 0), (0, 0, -1)]
        return [inclinar(f(i), *passos[i % 4]) for i in range(n)]
    if nome in ('atacar', 'ataque_1'):
        return [inclinar(f(i), *p) for i, p in enumerate(amostrar(golpe, n))]
    if nome == 'ataque_2':
        g = [(-2, -2, 0), (-3, -3, 0), (4, 4, 0), (5, 6, 0), (3, 3, 0), (0, 0, 0)]
        return [inclinar(f(i), *p) for i, p in enumerate(amostrar(g, n))]
    if nome == 'ataque_3':
        g = [(-2, -1, 0), (-1, 0, -3), (2, 2, -5), (4, 4, -2), (3, 3, 0), (0, 0, 0)]
        return [inclinar(f(i), *p) for i, p in enumerate(amostrar(g, n))]
    if nome == 'dano':
        g = [(-3, -2, 0), (-2, -1, 0), (-1, 0, 0)]
        return [inclinar(f(0), *p) for p in amostrar(g, n)]
    if nome == 'morrer':
        cai = deitar(f(0))
        seq = [inclinar(f(0), -3, -2), inclinar(f(0), -5, -3, 1), cai, dissolver(cai, 0.3), dissolver(cai, 0.55),
               dissolver(cai, 0.8), dissolver(cai, 0.93)]
        return amostrar(seq, n)
    if nome == 'atordoado':
        return [estrelas(inclinar(f(i), (-1, 1)[i % 2]), i) for i in range(n)]
    if nome == 'mudar_fase':
        return [contorno(f(i), cor) if i % 2 else inclinar(f(i), 0, 0, -1) for i in range(n)]
    # especiais e ataques com nome próprio
    k = nome.lower()
    if any(p in k for p in ('acordar', 'surgir', 'emergir', 'aparecer', 'levantar')):
        return [dissolver(f(i), max(0.0, 0.9 - i * 0.9 / max(1, n - 1))) for i in range(n)]
    if any(p in k for p in ('disfarce', 'teletransporte', 'enterrar', 'esconder', 'mergulho', 'desaparecer', 'invisivel', 'fugir')):
        return [dissolver(f(i), min(0.95, i * 0.95 / max(1, n - 1))) for i in range(n)]
    if any(p in k for p in ('uivar', 'grito', 'rugido', 'rugir', 'chamar', 'canto', 'sino', 'apito')):
        return [ondas(inclinar(f(i), -2 if i % 2 else -1), i) for i in range(n)]
    if any(p in k for p in ('carga', 'investida', 'salto', 'pisao', 'galopar', 'atropelar', 'rolar', 'cabecada', 'mergulhar', 'voo')):
        g = [(-2, -3, 0), (-1, -2, -1), (4, 5, -2), (5, 8, 0), (3, 5, 0), (0, 0, 0)]
        return [inclinar(f(i), *p) for i, p in enumerate(amostrar(g, n))]
    if k.startswith('especial') or any(p in k for p in ('esporo', 'fogo', 'chama', 'veneno', 'cuspir', 'sopro', 'magia', 'raio',
                                                        'gelo', 'acido', 'chuva', 'bolota', 'roubar', 'tinta', 'lanca', 'flecha',
                                                        'galhada', 'raizes', 'folha', 'bola', 'onda', 'feitico', 'luz', 'sombra')):
        g = amostrar([(-1, -1, 0), (-2, -1, -1), (2, 1, 0), (3, 2, 0), (1, 1, 0), (0, 0, 0)], n)
        return [particulas(inclinar(f(i), *p), cor, i, semente=len(k) + i) if i >= n // 3 else inclinar(f(i), *p)
                for i, p in enumerate(g)]
    return [inclinar(f(i), *p) for i, p in enumerate(amostrar(golpe, n))]


def tira(fs):
    h = fs[0].height
    out = Image.new('RGBA', (h * len(fs), h), (0, 0, 0, 0))
    for i, q in enumerate(fs):
        out.paste(q, (i * h, 0))
    return out


def dono(ficheiro, ids):
    """De que criatura é este ficheiro? (o id mais comprido que serve: javali_rei_mover é do javali_rei, não do javali)"""
    base = os.path.basename(ficheiro)
    bons = [i for i in ids if base.startswith(i + '_')]
    return max(bons, key=len) if bons else None


def regiao(reg):
    feitos, ficheiros = 0, 0
    props = sorted(glob.glob(os.path.join(PROPOSTAS, reg, '*_parado_lado.png')))
    ids = [os.path.basename(p)[:-len('_parado_lado.png')] for p in props]
    todos = [p for pasta in ('monstros', 'guardioes', 'bosses')
             for p in glob.glob(os.path.join(RAIZ, 'arte', 'regioes', reg, pasta, '*_lado.png'))]
    for prop, cid in zip(props, ids):
        if cid in FORA:
            continue
        antigos = [p for p in todos if dono(p, ids) == cid]
        if cid == 'mimico':
            antigos = glob.glob(os.path.join(RAIZ, 'arte', 'monstros_comuns', 'mimico_*_lado.png'))
        if not antigos:
            print('  (sem animações no jogo:', cid, ')')
            continue
        P = quadros(Image.open(prop).convert('RGBA'))
        for velho in sorted(antigos):
            nome = os.path.basename(velho)[len(cid) + 1:-len('_lado.png')]
            v = Image.open(velho)
            h, n = v.height, max(1, v.width // v.height)
            if P[0].height != h:
                print('  ! tamanho diferente:', cid, nome, P[0].height, h)
                continue
            tira(anim(nome, P, n)).save(velho)
            ficheiros += 1
        feitos += 1
    print(reg, feitos, 'criaturas,', ficheiros, 'ficheiros')


if __name__ == '__main__':
    regs = sys.argv[1:] or sorted(os.listdir(PROPOSTAS))
    for r in regs:
        if os.path.isdir(os.path.join(PROPOSTAS, r)):
            regiao(r)
