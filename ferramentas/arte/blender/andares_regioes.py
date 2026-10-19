"""Peças especiais dos andares 11–100 (linha "Peças especiais" de cada andar em docs/regioes/rXX_*.md).

Lê a lista de cada andar, separa as peças (e as variantes entre parênteses, ex.: "carris (reto, curva)" ou
"cristais gigantes (3 cores)") e escolhe o MOLDE pelas palavras do nome. Usa as texturas da região (kit_regioes.py).
Saída: arte/regioes/rXX_*/andares/aNN_<peça>.glb

Uso: blenv/bin/python ferramentas/arte/blender/andares_regioes.py [região ...] [--previa]
"""
import math
import os
import re
import sys
import unicodedata
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B
import kit_regioes as K

DOCS = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs', 'regioes')


# ---------------- moldes extra (móveis, construções, objetos grandes) ----------------

def mesa(p, M, m='madeira'):
    p.caixa(M[m], 0, 0, 0.75, 1.6, 0.9, 0.1)
    for x in (-0.7, 0.7):
        for y in (-0.35, 0.35):
            p.caixa(M[m], x, y, 0, 0.1, 0.1, 0.75)


def altar(p, M, m='pedra', luz='cristal_luz'):
    p.caixa(M[m], 0, 0, 0, 1.6, 1.0, 0.9)
    p.caixa(M[m], 0, 0, 0.9, 1.8, 1.2, 0.15)
    p.bola(M[luz], 0, 0, 1.25, 0.2, 0.2, 0.2, 0)


def trono(p, M, m='pedra', enfeite='metal'):
    p.caixa(M[m], 0, 0, 0, 1.4, 1.2, 0.6)
    p.caixa(M[m], 0, 0.5, 0.6, 1.4, 0.25, 1.8)
    for x in (-0.6, 0.6):
        p.caixa(M[m], x, 0, 0.6, 0.2, 1.0, 0.5)
    p.caixa(M[enfeite], 0, 0.5, 2.4, 0.6, 0.3, 0.3)


def barco(p, M, m='madeira', grande=False):
    k = 2.2 if grande else 1.0
    p.prisma(M[m], [(-0.8 * k, -1.8 * k), (0.8 * k, -1.8 * k), (0.9 * k, 1.2 * k), (0, 2.2 * k), (-0.9 * k, 1.2 * k)], 0, 0.7 * k)
    p.caixa(M['madeira'], 0, 0, 0.7 * k, 1.4 * k, 0.15, 0.08)
    if grande:
        p.cilindro(M['madeira'], 0, 0, 0.7 * k, 0.12, 0.1, 6.0, 6)
        p.caixa(M['tecido'], 0, 0, 2.5, 2.6, 0.05, 2.6)


def plataforma(p, M, m='madeira'):
    p.caixa(M[m], 0, 0, 1.0, 2, 2, 0.15)
    for x in (-0.9, 0.9):
        p.caixa(M['metal'], x, -0.9, 0, 0.1, 0.1, 3.0)


def cogumelo(p, M, chapeu='cogumelo', pe='branco', esc=1.0):
    p.cilindro(M[pe], 0, 0, 0, 0.45 * esc, 0.35 * esc, 2.2 * esc, 8)
    p.bola(M[chapeu], 0, 0, 2.3 * esc, 1.8 * esc, 1.8 * esc, 0.8 * esc, 1, semente=int(esc * 10))


def torre(p, M, m='pedra', telhado='telhado'):
    p.cilindro(M[m], 0, 0, 0, 1.2, 1.0, 6.0, 10)
    p.cilindro(M[telhado], 0, 0, 6.0, 1.4, 0.0, 2.0, 10)


def estatua(p, M, m='pedra'):
    p.caixa(M[m], 0, 0, 0, 1.0, 1.0, 0.6)
    p.cilindro(M[m], 0, 0, 0.6, 0.35, 0.3, 1.4, 7)
    p.bola(M[m], 0, 0, 2.2, 0.3, 0.3, 0.32, 1)
    p.cilindro(M[m], 0.4, 0, 1.4, 0.1, 0.08, 0.8, 5, rot=(0, 0.6, 0))


def arco(p, M, m='pedra'):
    p.caixa(M[m], -1.0, 0, 0, 0.6, 0.8, 2.6)
    p.caixa(M[m], 1.0, 0, 0, 0.6, 0.8, 2.6)
    p.caixa(M[m], 0, 0, 2.6, 2.6, 0.8, 0.6)


def barril(p, M, m='madeira'):
    p.cilindro(M[m], 0, 0, 0, 0.4, 0.45, 0.5, 10)
    p.cilindro(M[m], 0, 0, 0.5, 0.45, 0.4, 0.5, 10)
    for z in (0.15, 0.85):
        p.cilindro(M['metal'], 0, 0, z, 0.44, 0.44, 0.05, 10)


def poco(p, M, m='pedra', agua='agua'):
    for i in range(10):
        a = i / 10 * math.tau
        p.caixa(M[m], math.cos(a) * 0.8, math.sin(a) * 0.8, 0, 0.5, 0.35, 0.7, rot_z=a)
    p.cilindro(M[agua], 0, 0, 0.3, 0.7, 0.7, 0.05, 10)


def teia(p, M, m='teia'):
    p.caixa(M[m], 0, 0, 0, 2.0, 0.04, 2.0)


def ninho(p, M, m='casca'):
    p.cilindro(M[m], 0, 0, 0, 0.6, 0.9, 0.4, 10)
    for i in range(3):
        p.bola(M['branco'], -0.2 + i * 0.2, 0.1 * (i % 2), 0.35, 0.14, 0.12, 0.17, 0)


def vagoneta(p, M):
    p.caixa(M['metal'], 0, 0, 0.3, 0.9, 1.3, 0.6)
    for x in (-0.4, 0.4):
        for y in (-0.45, 0.45):
            p.cilindro(M['metal'], x, y, 0.15, 0.15, 0.15, 0.1, 8, rot=(0, math.radians(90), 0))
    p.bola(M['minerio'], 0, 0, 0.9, 0.4, 0.6, 0.2, 0)


def ovo(p, M, m='branco', n=3):
    for i in range(n):
        p.bola(M[m], -0.3 + i * 0.3, 0.1 * (i % 2), 0.35, 0.22, 0.22, 0.32, 1)


def casulo(p, M, m='teia'):
    p.bola(M[m], 0, 0, 1.0, 0.4, 0.4, 0.9, 1)


def sino(p, M):
    for x in (-0.8, 0.8):
        p.caixa(M['madeira'], x, 0, 0, 0.15, 0.15, 2.4)
    p.caixa(M['madeira'], 0, 0, 2.4, 1.8, 0.2, 0.15)
    p.cilindro(M['metal'], 0, 0, 1.4, 0.45, 0.2, 0.8, 8)


def bandeira(p, M, m='tecido'):
    p.cilindro(M['madeira'], 0, 0, 0, 0.05, 0.05, 3.0, 5)
    p.caixa(M[m], 0.5, 0, 2.2, 1.0, 0.03, 0.7)


def cascata(p, M, m='agua'):
    p.caixa(M['pedra'], 0, 0.4, 0, 2.2, 0.8, 4.0)
    p.caixa(M[m], 0, -0.05, 0, 1.4, 0.1, 4.0)
    p.caixa(M[m], 0, -1.0, 0, 2.0, 1.8, 0.1)


EXTRA = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_')}

# palavra no nome -> (molde, parâmetros). A primeira que aparecer no nome ganha.
REGRAS = [
    ('ostra', 'ostra', {}), ('sebe', 'arbusto', {}), ('roseira', 'arbusto', dict(frutos='fogo_luz')), ('jardim', 'arbusto', {}),
    ('estufa', 'casa', dict(parede='vidro')), ('orgao', 'estante', {}), ('banco', 'mesa', {}), ('armadura', 'estatua', dict(m='metal')),
    ('pedestal', 'estatua', {}), ('suporte', 'grade', dict(m='madeira')), ('varanda', 'plataforma', dict(m='pedra')),
    ('terraco', 'plataforma', dict(m='pedra')), ('pessegueiro', 'arvore', {}), ('penhasco', 'falesia', {}), ('pico', 'falesia', {}),
    ('anfiteatro', 'arco', {}), ('templo', 'arco', {}), ('cabo', 'ponte', dict(corda='metal')), ('moinho', 'torre', {}),
    ('gongo', 'sino', {}), ('sol ', 'objeto', dict(m='luz', r=1.5)), ('estrela', 'objeto', dict(m='luz', r=1.0)),
    ('planeta', 'objeto', dict(m='luz_roxa', r=1.2)), ('cometa', 'objeto', dict(m='luz_azul', r=0.8)), ('nebulosa', 'nuvem', dict(m='luz_roxa')),
    ('ampulheta', 'coluna', dict(m='vidro')), ('montanha', 'ilha', dict(r=2.0)), ('degrau', 'escada', dict(m='luz_azul')),
    ('caminho', 'chao', dict(m='chao_a')), ('eco', 'estatua', {}),
    ('viga', 'viga', {}), ('cristais', 'cristais', {}), ('boia', 'lanterna', {}), ('trampolim', 'cogumelo', {}),
    ('corrente', 'grade', {}), ('caldeir', 'poco', dict(m='metal')), ('folhas', 'arbusto', dict(r=1.1)),
    ('liana', 'alga', dict(m='folhas', alto=2.4)), ('mural', 'parede', {}), ('painel', 'parede', {}), ('fachada', 'parede', {}),
    ('hieroglif', 'parede', {}), ('ameias', 'parede', {}), ('totem', 'coluna', dict(m='madeira')), ('canoa', 'barco', {}),
    ('naufragio', 'barco', dict(grande=True)), ('palicada', 'grade', dict(m='madeira')), ('nenufar', 'placa_luz', dict(m='folhas')),
    ('miradouro', 'plataforma', {}), ('tirolesa', 'ponte', {}), ('regador', 'barril', dict(m='metal')),
    ('rochedo', 'rocha', dict(r=1.3, h=1.0)), ('carroca', 'vagoneta', {}), ('caravana', 'vagoneta', {}), ('treno', 'vagoneta', {}),
    ('banca', 'mesa', {}), ('piano', 'mesa', dict(m='madeira')), ('palacio', 'casa', {}), ('salao', 'casa', {}), ('sauna', 'casa', {}),
    ('capela', 'casa', {}), ('mausoleu', 'casa', dict(parede='pedra')), ('estaleiro', 'plataforma', {}), ('porao', 'casa', {}),
    ('sala', 'casa', {}), ('telhado', 'casa', {}), ('salina', 'chao', dict(m='branco')), ('carapaca', 'ninho', {}),
    ('concha', 'ostra', {}), ('cratera', 'poco', dict(agua='lava_luz')), ('esfinge', 'estatua', {}), ('piramide', 'pico', dict(baixo=True, alto=4.0)),
    ('corredor', 'tunel', {}), ('ouro', 'minerio', dict(m='minerio')), ('iglu', 'igloo', {}), ('banco de neve', 'rocha', dict(m='neve')),
    ('costa', 'chao', dict(m='gelo')), ('gelo', 'chao', dict(m='gelo')), ('pinheiro', 'arvore', dict(forma='cone')),
    ('pegadas', 'chao', {}), ('gruta', 'arco', {}), ('caverna', 'arco', {}), ('fenda', 'arco', {}), ('entrada', 'arco', {}),
    ('cripta', 'arco', {}), ('balista', 'barril', {}), ('canhao', 'barril', dict(m='metal')), ('garrafa', 'barril', dict(m='vidro')),
    ('leme', 'ancora', {}), ('anemona', 'coral', {}), ('redemoinho', 'portal', dict(m='luz_azul')), ('broto', 'erva', {}),
    ('forno', 'braseiro', {}), ('martelo', 'plataforma', dict(m='metal')), ('canal', 'agua', {}), ('mar ', 'agua', {}),
    ('magma', 'agua', dict(m='lava_luz')), ('nicho', 'estatua', {}), ('cranio', 'estatua', dict(m='osso')), ('ruina', 'coluna', dict(partida=True)),
    ('vagoneta', 'vagoneta', {}), ('carris', 'carris', {}), ('tunel', 'tunel', {}), ('cascata', 'cascata', {}),
    ('galeao', 'barco', dict(grande=True)), ('navio', 'barco', dict(grande=True)), ('barco', 'barco', {}), ('jangada', 'barco', {}),
    ('cais', 'ponte', {}), ('ponte', 'ponte', {}), ('passadico', 'ponte', {}),
    ('elevador', 'plataforma', {}), ('plataforma', 'plataforma', {}), ('degraus', 'escada', dict(m='pedra')),
    ('escada', 'escada', {}), ('trono', 'trono', {}), ('altar', 'altar', {}), ('mesa', 'mesa', {}), ('bancada', 'mesa', {}),
    ('bigorna', 'altar', dict(m='metal', luz='metal')), ('fornalha', 'braseiro', {}), ('forja', 'braseiro', {}),
    ('braseiro', 'braseiro', {}), ('fogueira', 'fogueira', {}), ('lanterna', 'lanterna', {}), ('tocha', 'tocha', {}),
    ('vela', 'vela', {}), ('lampada', 'lanterna', {}), ('farol', 'torre', {}),
    ('torre', 'torre', {}), ('estatua', 'estatua', {}), ('figura', 'estatua', {}), ('coluna', 'coluna', {}), ('pilar', 'coluna', {}),
    ('portao', 'arco', {}), ('arco', 'arco', {}), ('porta', 'moldura', dict(vidro='madeira', alto=2.6, larg=1.4)),
    ('janela', 'moldura', dict(m='pedra', vidro='vidro', alto=2.0, larg=0.8)), ('espelho', 'moldura', dict(m='metal', vidro='vidro')),
    ('vitral', 'moldura', dict(m='pedra', vidro='vidro_roxo')), ('grade', 'grade', {}), ('jaula', 'grade', {}), ('cela', 'grade', {}),
    ('estante', 'estante', {}), ('livr', 'estante', {}), ('relogio', 'relogio_sol', {}), ('portal', 'portal', {}),
    ('ancora', 'ancora', {}), ('balao', 'balao', {}), ('sino', 'sino', {}), ('bandeira', 'bandeira', {}), ('estandarte', 'bandeira', {}),
    ('poco', 'poco', {}), ('buraco', 'poco', {}), ('fonte', 'poco', {}), ('lago', 'agua', {}), ('rio', 'agua', {}), ('poca', 'agua', {}),
    ('lava', 'agua', dict(m='lava_luz')), ('agua', 'agua', {}), ('teia', 'teia', {}), ('casulo', 'casulo', {}), ('ovo', 'ovo', {}),
    ('ninho', 'ninho', {}), ('esqueleto', 'osso', dict(grande=True)), ('osso', 'osso', dict(grande=True)), ('costela', 'osso', dict(grande=True)),
    ('campa', 'campa', {}), ('tumulo', 'campa', dict(tipo=3)), ('sarcofago', 'campa', dict(tipo=3)), ('caixao', 'campa', dict(tipo=3)),
    ('cruz', 'campa', dict(tipo=2)), ('barril', 'barril', {}), ('pipa', 'barril', {}), ('caixote', 'bau', {}), ('bau', 'bau', {}),
    ('casa', 'casa', {}), ('cabana', 'casa', {}), ('palafita', 'casa', dict(palafita=True)), ('tenda', 'tenda', {}),
    ('cogumelo', 'cogumelo', {}), ('fungo', 'cogumelo', {}), ('palmeira', 'palmeira', {}), ('cacto', 'cacto', dict(m='folhas')),
    ('arvore', 'arvore', {}), ('tronco', 'arvore', dict(forma='nua')), ('raiz', 'osso', dict(m='casca', grande=True)),
    ('arbusto', 'arbusto', {}), ('flor', 'erva', dict(flor='fogo_luz')), ('erva', 'erva', {}), ('junco', 'junco', {}),
    ('coral', 'coral', {}), ('alga', 'alga', dict(alto=2.4)), ('nuvem', 'nuvem', {}), ('ilha', 'ilha', {}), ('flutuante', 'ilha', {}),
    ('cristal', 'cristais', {}), ('estalactite', 'pico', {}), ('estalagmite', 'pico', dict(baixo=True)), ('espinho', 'pico', dict(baixo=True)),
    ('estaca', 'pico', dict(baixo=True)), ('obelisco', 'pico', dict(baixo=True, alto=3.5)), ('geiser', 'geiser', {}),
    ('muro', 'parede', {}), ('muralha', 'parede', dict(alto=4.0)), ('parede', 'parede', {}), ('falesia', 'falesia', {}),
    ('duna', 'rocha', dict(m='chao_a', r=1.6, h=0.7)), ('rocha', 'rocha', {}), ('pedra', 'rocha', {}), ('penedo', 'rocha', dict(r=1.2, h=0.9)),
    ('minerio', 'minerio', {}), ('veio', 'minerio', {}), ('janela azul', 'janela_sistema', {}), ('sistema', 'janela_sistema', {}),
    ('chao', 'chao', {}), ('placa', 'placa_luz', {}), ('cupula', 'cupula', {}), ('bolha', 'objeto', dict(m='bolha', r=0.5)),
]


def _ascii(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')


def _slug(t):
    return re.sub(r'[^a-z0-9]+', '_', _ascii(t)).strip('_')[:40]


def _separar(linha):
    """'carris (reto, curva), vagoneta' -> ['carris (reto, curva)', 'vagoneta']"""
    out, nivel, atual = [], 0, ''
    for c in linha:
        if c == '(':
            nivel += 1
        elif c == ')':
            nivel -= 1
        if c == ',' and nivel == 0:
            out.append(atual.strip())
            atual = ''
        else:
            atual += c
    if atual.strip():
        out.append(atual.strip())
    return out


def _expandir(item):
    """Variantes: '(reto, curva, T)' dá 3 peças; '(3 cores)' dá 3 peças; '×2' dá 2."""
    item = re.sub(r'\*\*|`', '', item)
    m = re.match(r'(.*?)\s*\((.*)\)\s*(.*)$', item)
    base, extra = (m.group(1) + ' ' + m.group(3)).strip() if m else item, m.group(2) if m else ''
    n = re.search(r'[×x]\s*(\d+)', base)
    if n:
        base = re.sub(r'\s*[×x]\s*\d+', '', base)
        return [f'{base} {i + 1}' for i in range(int(n.group(1)))]
    num = re.match(r'\s*(\d+)\s', extra)
    if num:
        return [f'{base} {i + 1}' for i in range(min(4, int(num.group(1))))]
    partes = [x.strip() for x in extra.split(',') if x.strip()]
    if extra and len(partes) > 1 and all(len(x) <= 14 for x in partes):
        return [f'{base} {x}' for x in partes]
    return [base]


def lista_andares(n):
    f = [x for x in os.listdir(DOCS) if x.startswith(f'r{n:02d}_')][0]
    linhas = [l for l in open(os.path.join(DOCS, f), encoding='utf-8') if l.startswith('| Peças especiais')]
    andares = {}
    for i, l in enumerate(linhas[:10]):
        texto = l.split('|')[2]
        pecas = []
        for item in _separar(texto):
            pecas += _expandir(item)
        andares[(n - 1) * 10 + i + 1] = pecas
    return andares


def _molde(nome):
    t = _ascii(nome)
    for chave, molde, kw in REGRAS:
        if chave in t:
            kw = dict(kw)
            if molde == 'tunel':
                kw['forma'] = 'curva' if 'curva' in t else 'T' if re.search(r'\bt\b', t) else 'reto'
            if molde == 'carris':
                kw['forma'] = 'curva' if 'curva' in t else 'cruz' if 'cruz' in t else 'reto'
            if 'gigante' in t and molde in ('cogumelo', 'arvore'):
                kw['esc'] = 1.6
            return molde, kw
    return 'objeto', {}


def gerar(n, previa=False):
    B.limpar()
    pasta = os.path.join('arte', 'regioes', K.PASTAS[n], 'andares')
    M = K.materiais(n, os.path.join('arte', 'regioes', K.PASTAS[n], 'kit', 'texturas'))
    M.setdefault('teia', B.material(f'r{n:02d}_teia', cor='#c7dcd0'))
    M.setdefault('cogumelo', M.get('folhas'))
    moldes = dict(K.MOLDES, **EXTRA)
    objetos, usados = [], {}
    for andar, pecas in lista_andares(n).items():
        for nome in pecas:
            slug = f'a{andar:02d}_{_slug(nome)}' if andar < 100 else f'a{andar}_{_slug(nome)}'
            if slug in usados:
                continue
            molde, kw = _molde(nome)
            usados[slug] = molde
            p = B.Peca(slug)
            try:
                moldes[molde](p, M, **kw)
            except KeyError:   # material que esta região não tem: usa-se a pedra
                p = B.Peca(slug)
                moldes['objeto'](p, M)
            i = len(objetos)
            objetos.append(p.criar((i % 10) * 6.0 - 27, (i // 10) * 6.0 - 12))
    B.exportar(objetos, pasta, f'r{n:02d}_andares.blend')
    if previa:
        B.previa(os.path.join(pasta, f'r{n:02d}_andares.png'), distancia=60, alvo=(0, 0, 0))
    soltos = sum(1 for m in usados.values() if m == 'objeto')
    print('ok', K.PASTAS[n], len(objetos), 'peças', f'({soltos} sem molde próprio)')


if __name__ == '__main__':
    regs = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(K.REGIOES)
    for r in regs:
        gerar(r, '--previa' in sys.argv)
