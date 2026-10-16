"""docs/mapas/ascendia.md + rotinas de docs/NPCS.md + docs/LOJAS.md -> dados/cidade.json e dados/lojas.json.

cidade.json: a grelha (30×22 células de 10 m), os edifícios (código, células, centro, modelo), e a rotina de cada NPC
(onde está a cada hora, com o código do edifício). lojas.json: o que cada loja de Ascendia vende, a que preço,
com que stock (-1 = ∞) e a partir de quando.

Uso: python3 ferramentas/dados/cidade.py
"""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, slug, ascii_, numero

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
MODELOS = {'Gu': 'guilda', 'Qu': 'quartel', 'Ar': 'arena', 'ca': 'casa_1', 'TC': 'casa_heroi', 'Fo': 'forja_brom',
           'Al': 'alquimia_selene', 'Gi': 'oficina_gizmo', 'Co': 'costura_elva', 'Me': 'banca_1', 'Ta': 'taberna',
           'Es': 'estalagem', 'Go': 'camara_governador', 'Ig': 'igreja', 'Bi': 'biblioteca', 'Vi': 'tenda_vidente',
           'cb': 'casa_pobre', 'Ro': 'esconderijo_rook', 'Mi': 'banca_3', 'Ha': 'quinta_hana', 'Ze': 'rancho_zed',
           'Qt': 'campo_trigo', 'Pi': 'barco_pesca', 'Ca': 'cais', 'Fn': 'fonte', 'Pa': 'palco', 'Qa': 'quadro_avisos',
           'Eb': 'pedestal_estatua', 'Tr': 'boneco_treino', 'Cr': 'cristal_mestre', '▓▓': 'base_torre'}
# cada NPC: onde costuma estar quando o texto não diz (o "balcão" dele)
CASA_NPC = {'lyra': 'Gu', 'gorvan': 'Gu', 'brom': 'Fo', 'selene': 'Al', 'tobias': 'Me', 'marta': 'Es', 'kai': 'Tr',
            'mia': 'Mi', 'celia': 'Ig', 'fausto': 'Bi', 'rook': 'Ro', 'freya': 'Qu', 'pip': 'Pi', 'hana': 'Ha', 'zed': 'Ze',
            'oriel': 'Vi', 'lucien': 'Ta', 'gizmo': 'Gi', 'elva': 'Co', 'aldric': 'Go'}
LOCAIS = [('campo de treino', 'Tr'), ('guilda', 'Gu'), ('mercado', 'Me'), ('banca do mercado', 'Me'), ('forja', 'Fo'),
          ('alquimia', 'Al'), ('estalagem', 'Es'), ('taberna', 'Ta'), ('igreja', 'Ig'), ('biblioteca', 'Bi'),
          ('praca', 'Fn'), ('banco da praca', 'Fn'), ('rio', 'Pi'), ('cais', 'Pi'), ('quinta', 'Ha'), ('rancho', 'Ze'),
          ('quartel', 'Qu'), ('arena', 'Ar'), ('camara', 'Go'), ('tenda', 'Vi'), ('oficina', 'Gi'), ('costura', 'Co'),
          ('esquina do bairro baixo', 'Mi'), ('bairro baixo', 'Ro'), ('muralha', 'Gu'), ('casa', 'ca')]


def grelha():
    t = open(os.path.join(RAIZ, 'docs', 'mapas', 'ascendia.md'), encoding='utf-8').read()
    g = re.search(r'```\n(.*?)```', t, re.S).group(1).split('\n')
    linhas = []
    for l in g[1:]:
        m = re.match(r'\s*(\d+)\s\s?(.*)$', l)
        if m:
            corpo = m.group(2)
            linhas.append([corpo[i:i + 2] for i in range(0, len(corpo) - 1, 2)])
    larg = max(len(r) for r in linhas)
    return [r + ['tt'] * (larg - len(r)) for r in linhas]


def edificios(g):
    """Junta as células vizinhas com o mesmo código (cada grupo é um edifício)."""
    vistos, out = set(), []
    for y in range(len(g)):
        for x in range(len(g[0])):
            c = g[y][x]
            if c not in MODELOS or (x, y) in vistos:
                continue
            grupo, pilha = [], [(x, y)]
            while pilha:
                px, py = pilha.pop()
                if (px, py) in vistos or not (0 <= py < len(g) and 0 <= px < len(g[0])) or g[py][px] != c:
                    continue
                vistos.add((px, py))
                grupo.append([px, py])
                pilha += [(px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)]
            cx = sum(p[0] for p in grupo) / len(grupo)
            cy = sum(p[1] for p in grupo) / len(grupo)
            out.append({'codigo': c, 'modelo': MODELOS[c], 'celulas': grupo, 'centro': [cx, cy]})
    return out


def local(texto):
    a = ascii_(texto)
    for k, c in LOCAIS:
        if k in a:
            return c
    return None


def rotinas():
    npcs = json.load(open(os.path.join(RAIZ, 'dados', 'npcs.json'), encoding='utf-8'))
    out = {}
    for n in npcs:
        r = []
        for parte in n['onde_pt'].split('·'):
            p = parte.strip()
            dom = 'domingo' in ascii_(p)
            m = re.search(r'(\d+):00[–-](\d+):00', p)
            cod = local(re.sub(r'\(.*?\)', '', p)) or local(p)
            if not cod:
                continue
            if m:
                r.append({'local': cod, 'de': int(m.group(1)), 'ate': int(m.group(2)), 'domingo': dom})
            elif 'sempre' in ascii_(p):
                r.append({'local': cod, 'de': 0, 'ate': 24, 'domingo': dom})
            elif 'noite' in ascii_(p):
                r.append({'local': cod, 'de': 20, 'ate': 24, 'domingo': dom})
            elif 'tarde' in ascii_(p):
                r.append({'local': cod, 'de': 13, 'ate': 19, 'domingo': dom})
            elif 'manha' in ascii_(p) or 'cedo' in ascii_(p):
                r.append({'local': cod, 'de': 6, 'ate': 12, 'domingo': dom})
        out[n['id']] = {'rotina': r, 'balcao': CASA_NPC.get(n['id'], 'Fn')}
    return out


def lojas():
    t = open(os.path.join(RAIZ, 'docs', 'LOJAS.md'), encoding='utf-8').read()
    itens = json.load(open(os.path.join(RAIZ, 'dados', 'itens.json'), encoding='utf-8'))
    armas = json.load(open(os.path.join(RAIZ, 'dados', 'armas.json'), encoding='utf-8'))
    ind = {}
    for x in itens + armas:
        for k in (slug(x['nome_pt']), re.sub(r'_(de|do|da|dos|das)_', '_', slug(x['nome_pt']))):
            ind.setdefault(k, x['id'])
    sec = t.split('## 2. Lojas de Ascendia', 1)[1].split('\n## 3.', 1)[0]
    out = []
    for bloco in re.split(r'^### ', sec, flags=re.M)[1:]:
        tit, _, resto = bloco.partition('\n')
        m = re.match(r'[\d.]+\s+(.+?)\s+—\s+(.+)', tit)
        if not m:
            continue
        dono_txt = ascii_(m.group(1))
        dono = next((v for k, v in [('tobias', 'tobias'), ('brom', 'brom'), ('selene', 'selene'), ('marta', 'marta'),
                                    ('pip', 'pip'), ('mia', 'mia'), ('hana', 'hana'), ('zed', 'zed'), ('elva', 'elva'),
                                    ('gizmo', 'gizmo'), ('celia', 'celia'), ('fausto', 'fausto'), ('oriel', 'oriel'),
                                    ('taberna', 'lucien'), ('rook', 'rook')] if k in dono_txt), None)
        if not dono:
            continue
        kv = {}
        lista = []
        for _, linhas in tabelas(resto):
            for l in linhas:
                if '_0' in l and '_1' in l and len(l) == 2:
                    kv[limpar(l['_0'])] = limpar(l['_1'])
                    continue
                nome = l.get('Item') or l.get('Arma') or l.get('Peça') or ''
                preco = next((v for k, v in l.items() if k.startswith('Preço')), '')
                if not nome or not re.search(r'\d', preco):
                    continue
                # "Poção de Vida P / M / G" com "30 / 150 / 600" e "início / região 3 / região 5"; ou "A · B" com "60 · 70"
                sep = r'\s*/\s*' if '/' in nome else r'\s*·\s*'
                nomes = re.split(sep, limpar(nome))
                if len(nomes) > 1 and len(nomes[1].split()) == 1 and len(nomes[0].split()) > 1:   # "Poção de Vida P / M"
                    base = nomes[0].rsplit(' ', 1)[0]
                    nomes = [nomes[0]] + [base + ' ' + n for n in nomes[1:]]
                precos = [x for x in re.split(sep, preco) if re.search(r'\d', x)]
                quandos = re.split(r'\s*/\s*', limpar(next((v for k, v in l.items() if k.startswith('A partir')), 'início')))
                for k, n in enumerate(nomes):
                    iid = ind.get(slug(n)) or ind.get(re.sub(r'_(de|do|da|dos|das)_', '_', slug(n)))
                    if not iid:
                        continue
                    preco_k = precos[k] if k < len(precos) else precos[0]
                    quando = quandos[k] if k < len(quandos) else quandos[0]
                    stock = -1
                    q = next((v for k, v in l.items() if k.startswith(('Stock', 'Quantidade'))), '')
                    if q and re.search(r'\d', q) and '∞' not in q:
                        stock = int(re.search(r'\d+', q).group(0))
                    lista.append({'item': iid, 'preco': int(numero(preco_k.replace(' ', ''))), 'stock': stock,
                                  'quando_pt': quando, 'cond': cond_de(quando, dono)})
        h = re.search(r'(\d+):00[–-](\d+):00', kv.get('Horário', ''))
        auto = []   # linhas genéricas: "as armas Comuns de cada tier desbloqueado" etc.
        a = ascii_(resto)
        if 'armas **comuns**' in a or 'armas comuns' in a:
            auto.append('armas')
        if 'pecas do conjunto de armadura' in a:
            auto.append('armaduras')
        if 'picareta e machado de lenhador do tier' in a:
            auto.append('ferramentas')
        if 'lingotes do tier' in a:
            auto.append('lingotes')
        out.append({'id': 'loja_' + dono, 'auto': auto, 'dono': dono, 'nome_pt': limpar(m.group(2)), 'horario': [int(h.group(1)), int(h.group(2))] if h else [0, 24],
                    'horario_pt': kv.get('Horário', ''), 'compra': 'nada' not in ascii_(kv.get('Compra', '')), 'itens': lista})
    return out


def cond_de(q, dono):
    a = ascii_(q)
    m = re.search(r'andar\s+(\d+)', a)
    if m:
        return 'andar_maximo >= %s' % m.group(1)
    m = re.search(r'regiao\s+(\d+)', a)
    if m:
        return 'andar_maximo >= %d' % ((int(m.group(1)) - 1) * 10 + 1)
    m = re.search(r'rank\s+(\w+)', a)
    if m:
        return 'rank >= %s' % m.group(1).upper()
    m = re.search(r'(\d+)\s*❤', q)
    if m:
        return 'coracoes(%s) >= %s' % (dono, m.group(1))
    return ''


def gerar():
    g = grelha()
    cid = {'largura': len(g[0]), 'altura': len(g), 'celula_m': 10, 'grelha': g, 'edificios': edificios(g), 'npcs': rotinas()}
    with open(os.path.join(RAIZ, 'dados', 'cidade.json'), 'w', encoding='utf-8') as f:
        json.dump(cid, f, ensure_ascii=False, indent=1)
    lj = lojas()
    with open(os.path.join(RAIZ, 'dados', 'lojas.json'), 'w', encoding='utf-8') as f:
        json.dump(lj, f, ensure_ascii=False, indent=1)
    print('ok cidade %dx%d, %d edifícios; %d lojas: %s' % (len(g[0]), len(g), len(cid['edificios']), len(lj),
          {l['dono']: len(l['itens']) for l in lj}))


if __name__ == '__main__':
    gerar()
