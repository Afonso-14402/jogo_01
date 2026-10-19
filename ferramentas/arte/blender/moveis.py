"""Móveis e decorações da casa (docs/textos/moveis.md): das regiões, básicos, troféus, cartazes de caça,
decorações de missões e de festivais. A forma escolhe-se pelo nome (cadeira, mesa, cama, tapete, candeeiro...)
e as cores pela região. Saída: arte/moveis/<id>.glb (+ moveis.blend + texturas/).

Uso: blenv/bin/python ferramentas/arte/blender/moveis.py [--previa]
"""
import math
import os
import re
import sys
import unicodedata
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B
import andares_regioes as A
import kit_regioes as K

DOC = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs', 'textos', 'moveis.md')
PASTA = os.path.join('arte', 'moveis')
TEX = os.path.join(PASTA, 'texturas')

# cor de destaque de cada região (tecidos, almofadas, enfeites)
DESTAQUE = {0: ['#4d9be6', '#8fd3ff', '#4d65b4'], 1: ['#239063', '#1ebc73', '#91db69'], 2: ['#7f708a', '#9babb2', '#4d9be6'],
            3: ['#547e64', '#92a984', '#ed8099'], 4: ['#f9c22b', '#ea4f36', '#fbb954'], 5: ['#c7dcd0', '#ffffff', '#8fd3ff'],
            6: ['#0eaf9b', '#30e1b9', '#f04f78'], 7: ['#ea4f36', '#f79617', '#3e3546'], 8: ['#6b3e75', '#905ea9', '#2e222f'],
            9: ['#ffffff', '#f9c22b', '#8fd3ff'], 10: ['#a884f3', '#323353', '#eaaded']}


def _ascii(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')


def _slug(t):
    return re.sub(r'[^a-z0-9]+', '_', _ascii(t)).strip('_')[:48]


# ---------------- moldes de móveis (tamanho de casa: ~1 m) ----------------

def cadeira(p, M):
    p.caixa(M['madeira'], 0, 0, 0.45, 0.5, 0.5, 0.08)
    for x in (-0.2, 0.2):
        for y in (-0.2, 0.2):
            p.caixa(M['madeira'], x, y, 0, 0.06, 0.06, 0.45)
    p.caixa(M['madeira'], 0, 0.22, 0.53, 0.5, 0.06, 0.55)
    p.caixa(M['tecido'], 0, 0, 0.53, 0.42, 0.42, 0.05)


def cama(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 1.0, 2.0, 0.35)
    p.caixa(M['branco'], 0, 0.05, 0.35, 0.95, 1.85, 0.15)
    p.caixa(M['tecido'], 0, -0.25, 0.5, 0.97, 1.3, 0.06)
    p.caixa(M['branco'], 0, 0.75, 0.5, 0.7, 0.3, 0.1)
    p.caixa(M['madeira'], 0, 0.98, 0, 1.0, 0.08, 0.9)


def tapete(p, M):
    p.caixa(M['tecido'], 0, 0, 0, 1.6, 1.1, 0.03)
    p.caixa(M['destaque'], 0, 0, 0.005, 1.2, 0.7, 0.03)


def candeeiro(p, M):
    p.cilindro(M['madeira'], 0, 0, 0, 0.18, 0.15, 0.08, 8)
    p.cilindro(M['metal'], 0, 0, 0.08, 0.03, 0.03, 1.1, 5)
    p.cilindro(M['luz'], 0, 0, 1.15, 0.25, 0.12, 0.3, 8)


def armario(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 1.1, 0.55, 1.8)
    p.caixa(M['destaque'], -0.27, -0.28, 0.1, 0.5, 0.02, 1.55)
    p.caixa(M['destaque'], 0.27, -0.28, 0.1, 0.5, 0.02, 1.55)
    p.caixa(M['metal'], 0, -0.3, 0.9, 0.08, 0.04, 0.12)


def quadro(p, M):
    p.caixa(M['madeira'], 0, 0, 1.2, 0.9, 0.06, 0.7)
    p.caixa(M['destaque'], 0, -0.02, 1.27, 0.75, 0.05, 0.56)
    p.caixa(M['branco'], 0.1, -0.03, 1.4, 0.3, 0.05, 0.2)


def vaso(p, M):
    p.cilindro(M['destaque'], 0, 0, 0, 0.18, 0.24, 0.4, 8)
    p.bola(M['folhas'], 0, 0, 0.6, 0.3, 0.3, 0.3, 1)
    p.bola(M['luz'], 0.12, -0.12, 0.75, 0.07, 0.07, 0.07, 0)


def trofeu(p, M):
    p.caixa(M['madeira'], 0, 0, 1.0, 0.7, 0.08, 0.8)
    p.bola(M['destaque'], 0, -0.15, 1.4, 0.28, 0.25, 0.28, 1)
    p.caixa(M['ouro'], 0, -0.05, 1.05, 0.3, 0.04, 0.08)


def cartaz(p, M):
    p.caixa(M['madeira'], 0, 0, 1.1, 0.7, 0.05, 0.9)
    p.caixa(M['papel'], 0, -0.02, 1.15, 0.6, 0.05, 0.8)
    p.cilindro(M['carimbo'], 0.15, -0.05, 1.25, 0.12, 0.12, 0.02, 8, rot=(math.radians(90), 0, 0))


def relogio(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 0.5, 0.35, 1.9)
    p.cilindro(M['branco'], 0, -0.18, 1.55, 0.18, 0.18, 0.03, 10, rot=(math.radians(90), 0, 0))
    p.cilindro(M['ouro'], 0, -0.18, 0.7, 0.08, 0.08, 0.03, 8, rot=(math.radians(90), 0, 0))


def lareira(p, M):
    p.caixa(M['pedra'], 0, 0, 0, 1.6, 0.6, 1.2)
    p.caixa(M['escuro'], 0, -0.25, 0.1, 0.9, 0.2, 0.7)
    p.cilindro(M['fogo'], 0, -0.25, 0.1, 0.25, 0.02, 0.45, 6)
    p.caixa(M['madeira'], 0, 0, 1.2, 1.8, 0.7, 0.1)


def sofa(p, M):
    p.caixa(M['tecido'], 0, 0, 0, 1.8, 0.8, 0.45)
    p.caixa(M['tecido'], 0, 0.3, 0.45, 1.8, 0.2, 0.45)
    for x in (-0.85, 0.85):
        p.caixa(M['destaque'], x, 0, 0.45, 0.15, 0.8, 0.25)


def aquario(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 1.0, 0.45, 0.7)
    p.caixa(M['vidro'], 0, 0, 0.7, 0.9, 0.4, 0.55)
    p.bola(M['laranja'], 0.1, 0, 0.95, 0.08, 0.04, 0.05, 0)


def estatueta(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 0.4, 0.4, 0.8)
    p.bola(M['destaque'], 0, 0, 1.0, 0.18, 0.18, 0.22, 1)


def caixa_musica(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 0.5, 0.35, 0.3)
    p.caixa(M['ouro'], 0, 0, 0.3, 0.52, 0.37, 0.04)


def objeto_casa(p, M):
    p.caixa(M['madeira'], 0, 0, 0, 0.6, 0.6, 0.5)
    p.bola(M['destaque'], 0, 0, 0.7, 0.22, 0.22, 0.22, 1)


MOVEIS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_')}

REGRAS = [
    ('bigorna', 'estatueta'), ('cristal', 'estatueta'), ('ancora', 'estatueta'), ('armadura', 'estatueta'),
    ('manequim', 'estatueta'), ('cata-vento', 'estatueta'), ('globo', 'estatueta'), ('telescopio', 'estatueta'),
    ('balao', 'estatueta'), ('cabide', 'estatueta'), ('idolo', 'estatueta'), ('tambor', 'caixa_musica'),
    ('corneta', 'caixa_musica'), ('orgao', 'caixa_musica'), ('coaxofono', 'caixa_musica'), ('gira-discos', 'caixa_musica'),
    ('concha', 'caixa_musica'), ('almofad', 'tapete'), ('toalha', 'tapete'), ('cachecol', 'tapete'), ('candelabro', 'candeeiro'),
    ('vitral', 'quadro'), ('placa', 'quadro'), ('baralho', 'quadro'), ('museu', 'estante'), ('cronica', 'estante'),
    ('objetos', 'estante'), ('caderno', 'estante'), ('ramo', 'trofeu'), ('teia', 'trofeu'), ('janela', 'trofeu'),
    ('remo', 'trofeu'), ('machado', 'trofeu'), ('espada', 'trofeu'), ('calice', 'trofeu'), ('escultura', 'estatueta'),
    ('fantasma', 'estatueta'), ('meias', 'quadro'), ('estrela', 'estatueta'), ('fogo de artificio', 'quadro'),
    ('cartaz', 'cartaz'), ('trofeu', 'trofeu'), ('cabeca', 'trofeu'), ('mascara', 'trofeu'), ('coroa', 'trofeu'),
    ('escama', 'trofeu'), ('dente', 'trofeu'), ('carapaca', 'trofeu'), ('chapeu', 'trofeu'), ('pena', 'trofeu'),
    ('colar', 'trofeu'), ('asa', 'trofeu'), ('fragmento', 'trofeu'), ('pedra-coracao', 'trofeu'), ('oculos', 'trofeu'),
    ('premio', 'trofeu'), ('cadeira', 'cadeira'), ('banco', 'cadeira'), ('banquinho', 'cadeira'), ('trono', 'trono'),
    ('poltrona', 'sofa'), ('sofa', 'sofa'), ('diva', 'sofa'), ('cama', 'cama'), ('beliche', 'cama'), ('berco', 'cama'),
    ('rede', 'cama'), ('tapete', 'tapete'), ('manta', 'tapete'), ('candeeiro', 'candeeiro'), ('lanterna', 'candeeiro'),
    ('lampada', 'candeeiro'), ('lustre', 'candeeiro'), ('vela', 'candeeiro'), ('luz', 'candeeiro'), ('estante', 'estante'),
    ('prateleira', 'estante'), ('livr', 'estante'), ('bau', 'bau'), ('arca', 'bau'), ('armario', 'armario'),
    ('comoda', 'armario'), ('guarda-roupa', 'armario'), ('cofre', 'armario'), ('quadro', 'quadro'), ('pintura', 'quadro'),
    ('retrato', 'quadro'), ('fotografia', 'quadro'), ('mapa', 'quadro'), ('tapecaria', 'quadro'), ('cortina', 'quadro'),
    ('relogio', 'relogio'), ('ampulheta', 'estatueta'), ('lareira', 'lareira'), ('fogao', 'lareira'), ('forno', 'lareira'),
    ('aquario', 'aquario'), ('espelho', 'moldura'), ('estatua', 'estatueta'), ('estatueta', 'estatueta'), ('busto', 'estatueta'),
    ('boneco', 'estatueta'), ('vaso', 'vaso'), ('planta', 'vaso'), ('flor', 'vaso'), ('arvore', 'vaso'), ('cacto', 'vaso'),
    ('mesa', 'mesa'), ('bancada', 'mesa'), ('secretaria', 'mesa'), ('sino', 'sino'), ('gongo', 'sino'), ('bandeir', 'bandeira'),
    ('estandarte', 'bandeira'), ('fonte', 'poco'), ('barril', 'barril'), ('pipa', 'barril'), ('caixa', 'caixa_musica'),
    ('gramofone', 'caixa_musica'), ('instrumento', 'caixa_musica'), ('harpa', 'estatueta'), ('arco', 'arco'),
]


def _molde(nome):
    t = _ascii(nome)
    for chave, molde in REGRAS:
        if chave in t:
            return molde
    return 'objeto_casa'


def ler():
    """[(id, nome, região)]"""
    txt = open(DOC, encoding='utf-8').read()
    out, vistos = [], set()

    def add(i, nome, reg):
        if i not in vistos:
            vistos.add(i)
            out.append((i, nome.strip(), reg))
    for i, nome in re.findall(r'\| `([a-z0-9_]+)` \| ([^|]+?) \|', txt):
        m = re.match(r'movel_r(\d\d)_', i)
        add(i, nome, int(m.group(1)) if m else 0)
    sec41 = txt.split('### 4.1')[1].split('###')[0]
    lista = sec41.split(':', 1)[1].split('Os **Bosses')[0]
    for nome in [x.strip(' .\n') for x in lista.replace('\n', ' ').split('·')]:
        if nome:
            add('trofeu_' + _slug(nome), nome, 0)
    sec42 = txt.split('### 4.2')[1].split('\n## ')[0]
    for linha in re.findall(r'^\| \d+ \| ([^|]+) \|', sec42, re.M):
        for nome in linha.split('·'):
            nome = re.sub(r'\(.*?\)', '', nome).strip()
            add('trofeu_cartaz_' + _slug(nome), 'Cartaz ' + nome, 0)
    sec5 = txt.split('## 5.')[1].split('\n## ')[0]
    for nome in re.findall(r'^\| (?!Decoração)([^|-][^|]+?) \|', sec5, re.M):
        add('decoracao_' + _slug(nome), nome, 0)
    sec6 = txt.split('## 6.')[1].split('\n## ')[0]
    for linha in re.findall(r'^\| (?!Festival \|)[^|]+\| ([^|]+) \|', sec6, re.M):
        for nome in linha.split('·'):
            nome = re.sub(r'\(.*?\)', '', nome).strip()
            if nome:
                add('festival_' + _slug(nome), nome, 0)
    return out


def materiais():
    m = {}
    t = lambda n, cores, **kw: B.material('mv_' + n, B.textura_ruido('mv_' + n, cores, TEX, len(m) + 1, **kw))
    m['madeira'] = t('madeira', ['#966c6c', '#ab947a', '#694f62'], tabuas=('#45293f', 6))
    m['pedra'] = t('pedra', ['#9babb2', '#7f708a', '#c7dcd0'])
    m['metal'] = t('metal', ['#7f708a', '#9babb2', '#625565'])
    m['branco'] = t('branco', ['#c7dcd0', '#ffffff', '#9babb2'])
    m['papel'] = t('papel', ['#fdcbb0', '#c7dcd0', '#ab947a'])
    m['folhas'] = t('folhas', ['#1ebc73', '#239063', '#91db69'])
    m['ouro'] = t('ouro', ['#f9c22b', '#f79617', '#fbff86'])
    m['livros'] = t('livros', ['#b33831', '#4d65b4', '#239063', '#f9c22b'], tabuas=('#2e222f', 4))
    m['escuro'] = B.material('mv_escuro', cor='#2e222f')
    m['carimbo'] = B.material('mv_carimbo', cor='#e83b3b')
    m['laranja'] = B.material('mv_laranja', cor='#f79617')
    m['luz'] = B.material('mv_luz', cor='#fbff86', emissao=2.0)
    m['fogo'] = B.material('mv_fogo', cor='#f79617', emissao=3.0)
    m['vidro'] = B.material('mv_vidro', cor='#8fd3ff', emissao=0.5)
    return m


def gerar(previa=False):
    B.limpar()
    base = materiais()
    por_regiao = {}
    for r, cores in DESTAQUE.items():
        por_regiao[r] = dict(base,
                             tecido=B.material(f'mv_tecido_{r}', B.textura_ruido(f'mv_tecido_{r}', cores, TEX, 100 + r)),
                             destaque=B.material(f'mv_destaque_{r}', cor=cores[0]))
    moldes = dict(K.MOLDES, **A.EXTRA, **MOVEIS)
    objetos = []
    for i, (mid, nome, reg) in enumerate(ler()):
        M = dict(por_regiao[reg])
        M.update({k: M['madeira'] for k in ('chao_a', 'chao_b', 'casca') if k not in M})
        M.setdefault('agua', M['vidro'])
        M.setdefault('tecido', M['tecido'])
        p = B.Peca(mid)
        molde = _molde(nome)
        try:
            moldes[molde](p, M)
        except KeyError:
            p = B.Peca(mid)
            objeto_casa(p, M)
        objetos.append(p.criar((i % 16) * 2.5 - 19, (i // 16) * 2.5 - 10))
    B.exportar(objetos, PASTA, 'moveis.blend')
    if previa:
        B.previa(os.path.join(PASTA, 'moveis.png'), distancia=40, alvo=(0, 0, 0))
    print('ok', len(objetos), 'móveis')


if __name__ == '__main__':
    gerar('--previa' in sys.argv)
