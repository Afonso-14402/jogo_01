"""Povoações dentro da torre (docs/CIDADES.md secção 4 e docs/regioes/rXX_*.md secção 7) -> dados/povoacoes.json,
dados/npcs_povoacoes.json, dados/lojas_povoacoes.json e dados/dialogos/<npc>.json (falas: docs/dialogos/povoacoes.md).

Cada povoação: andar, nome, descrição, serviços (cama, loja, forja...), NPCs (com o sprite que já existe em arte/npcs)
e as peças de arte: edifícios e decoração (arte/regioes/rXX/povoacoes/<povoação>_*.glb, ou sprites de
arte/regioes/rXX/natureza para as povoações que não têm peças 3D).

Uso: python3 ferramentas/dados/povoacoes.py
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from tabelas import ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
REGIOES = {1: 'r01_floresta', 2: 'r02_cavernas', 3: 'r03_pantano', 4: 'r04_deserto', 5: 'r05_gelo', 6: 'r06_oceano',
           7: 'r07_vulcao', 8: 'r08_reino_assombrado', 9: 'r09_ceu', 10: 'r10_abismo'}
EDIFICIO = ('casa', 'cabana', 'salao', 'palacio', 'estalagem', 'mosteiro', 'torre', 'taberna', 'forja', 'capela', 'observatorio',
            'cantina', 'tenda', 'cupula', 'sauna', 'banhos', 'cela', 'portao', 'fornalha', 'cabana_arvore')
PALAVRAS_FRACAS = {'de', 'do', 'da', 'dos', 'das', 'a', 'o'}
# peças de arte para as povoações sem peças 3D (sprites desenhados em ferramentas/arte/objetos.py)
SPRITES = {
    'acampamento_dos_lenhadores': {'edificios': ['cabana', 'tenda', 'cabana'], 'decoracao': ['pilha_troncos', 'pilha_troncos', 'barril', 'caixote', 'cerca']},
    'folhalta': {'edificios': ['casa_arvore', 'casa_arvore', 'casa_arvore', 'cabana_elfica'], 'decoracao': ['lanterna_seiva', 'lanterna_seiva', 'banca_elfica']},
}
COMIDA = {1: ['maca_selvagem', 'espetada_coelho', 'sopa_legumes'], 2: ['pao_fungo', 'sopa_mineiro', 'batatas_roxas_assadas'],
          3: ['caril_selva', 'banana_frita', 'agua_coco'], 4: ['tamaras_mel', 'cuscuz_oasis', 'sumo_cacto', 'pao_acafrao'],
          5: ['cha_quente', 'sopa_couve_norte', 'chocolate_quente', 'pocao_quente'], 6: ['sushi_recife', 'caldeirada_porto', 'ananas_grelhado', 'pocao_respirar'],
          7: ['ovos_geiser', 'batata_vulcanica_assada', 'pao_cinzas', 'pocao_fresca'], 8: ['pao_fantasma', 'sopa_abobora', 'agua_benta'],
          9: ['tarte_celeste', 'sumo_uva_celeste', 'pessego_celeste', 'pocao_leveza'], 10: ['pocao_regeneracao', 'pocao_purificadora']}


def slug(t):
    t = re.split(r',| — | \(', t)[0]
    return re.sub(r'[^a-z0-9]+', '_', ascii_(t).lower()).strip('_')


def fichas_regiao(regiao):
    texto = open(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r%02d_*.md' % regiao))[0], encoding='utf-8').read()
    m = re.search(r'^## 7\. Povoações\n(.*?)(?=^## \d)', texto, re.S | re.M)
    if not m:
        return []
    out = []
    for bloco in re.split(r'^### ', m.group(1), flags=re.M)[1:]:
        cab, _, resto = bloco.partition('\n')
        ma = re.search(r'\(andar (\d+)\)', cab)
        if not ma:
            continue
        nome = re.sub(r'\s*\(andar \d+\).*$', '', re.sub(r'^7\.\d+\s+', '', cab)).strip()
        desc = ' '.join(l.strip() for l in resto.split('\n') if l.strip() and not l.startswith('|') and not l.startswith('Loja')).strip()
        npcs = []
        for l in resto.split('\n'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) >= 3 and c[0].startswith('**'):
                npcs.append({'nome_pt': c[0].strip('*').strip(), 'quem_pt': c[1], 'faz_pt': c[2]})
        out.append({'id': slug(nome), 'nome_pt': nome, 'andar': int(ma.group(1)), 'regiao': regiao, 'descricao_pt': desc, 'npcs': npcs})
    return out


NOMES = {'Doutor': 'doutor_perdido', 'Coro dos Sapos': 'sapo_cantor'}


def sprite_id(nome, ids):
    nome = re.sub(r'\(.*?\)', '', nome.replace('"', '').replace('*', '')).strip()
    if nome in NOMES and NOMES[nome] in ids:
        return NOMES[nome]
    candidatos = [slug(nome), re.sub(r'[^a-z0-9]+', '_', ascii_(nome).lower()).strip('_')]
    candidatos += ['_'.join(t for t in c.split('_') if t not in PALAVRAS_FRACAS) for c in candidatos]
    for s in candidatos:
        if s in ids:
            return s
    for s in candidatos:
        partes = s.split('_')
        for k in range(1, len(partes)):           # sem o título no início ("Anciã Lothiel" -> lothiel)
            if '_'.join(partes[k:]) in ids:
                return '_'.join(partes[k:])
        for k in range(len(partes) - 1, 0, -1):   # só o primeiro nome ("Bruno Machadão" -> bruno)
            if '_'.join(partes[:k]) in ids:
                return '_'.join(partes[:k])
        perto = [i for i in ids if i.startswith(s + '_') or i.endswith('_' + s)]
        if len(perto) == 1:                       # "Ssark" -> chefe_ssark, "Rosa" -> rosa_taberna
            return perto[0]
    return ''


ALIAS = {'a_arquivista': 'biblioteca_arquivista'}


def pecas_3d(p):
    pasta = os.path.join(RAIZ, 'arte', 'regioes', REGIOES[p['regiao']], 'povoacoes')
    fichas = sorted(glob.glob(os.path.join(pasta, '*.glb')))
    toks = set(p['id'].split('_')) - PALAVRAS_FRACAS
    if p['id'] in ALIAS:
        toks = set(ALIAS[p['id']].split('_'))
    edif, deco = [], []
    for f in fichas:
        b = os.path.basename(f)[:-4]
        t = b.split('_')
        k = 0
        while k < len(t) and (t[k] in toks or t[k] in PALAVRAS_FRACAS):
            k += 1
        if k == 0 or not (set(t[:k]) - PALAVRAS_FRACAS) or k == len(t):
            continue
        resto = '_'.join(t[k:])
        caminho = 'res://arte/regioes/%s/povoacoes/%s.glb' % (REGIOES[p['regiao']], b)
        (edif if any(resto.startswith(e) for e in EDIFICIO) else deco).append(caminho)
    return edif, deco


def servicos(p):
    d = ascii_(p['descricao_pt']).lower()
    s = []
    if any(k in d for k in ('cama', 'estalagem', 'cabana', 'tenda', 'celas', 'salao', 'hotel', 'casa')):
        s.append('quarto')
    if any(k in d for k in ('loja', 'bazar', 'mercado', 'lojas')):
        s.append('loja')
    if 'forja' in d:
        s.append('forja')
    return s


def dono(p, servico):
    """Quem trata do serviço: o NPC cuja ficha fala dele; senão o primeiro."""
    chaves = {'loja': ('loja', 'vende', 'mercador', 'comerciante', 'bazar'), 'quarto': ('estalagem', 'cama', 'quarto', 'hotel', 'taberna', 'chefe', 'anfitri'),
              'forja': ('forja', 'ferreir', 'bigorna')}[servico]
    for n in p['npcs']:
        t = ascii_(n['quem_pt'] + ' ' + n['faz_pt']).lower()
        if n.get('id') and any(k in t for k in chaves):
            return n['id']
    return next((n['id'] for n in p['npcs'] if n.get('id')), '')


# ------------------------------------------------------------------ falas ------------------------------------------------------------------

def ler_falas():
    caminho = os.path.join(RAIZ, 'docs', 'dialogos', 'povoacoes.md')
    if not os.path.exists(caminho):
        return {}
    falas = {}
    atual = None
    for l in open(caminho, encoding='utf-8'):
        l = l.rstrip('\n')
        m = re.match(r'^### ([a-z0-9_]+) — (.+)$', l)
        if m:
            atual = falas.setdefault(m.group(1), {'nome': m.group(2).strip()})
            continue
        m = re.match(r'^- (primeira|dia|curta|rumor|andar|vida): (.+)$', l)
        if m and atual is not None:
            atual.setdefault(m.group(1), []).append(m.group(2).strip())
    return falas


def fala(texto, fid=None):
    emocao = 'normal'
    cond = ''
    m = re.match(r'^\((feliz|triste|zangado|surpreso|normal)\)\s*', texto)
    if m:
        emocao = m.group(1)
        texto = texto[m.end():]
    m = re.match(r'^\[(hora entre \d+ e \d+|chuva)\]\s*', texto)
    if m:
        cond = m.group(1) if m.group(1) != 'chuva' else 'clima == chuva'
        texto = texto[m.end():]
    f = {'emocao': emocao, 'texto': texto}
    if fid:
        f['id'] = fid
        f['cond'] = cond
    return f


def dialogo(npc, f, regiao):
    nome = npc['nome_pt']
    if not f:   # sem falas escritas: o mínimo, a partir da ficha
        quem = re.split(r'[;,(]', npc['quem_pt'])[0].strip()
        f = {'primeira': ['Olá! Chamo-me %s — %s.' % (nome, quem)], 'dia': ['Bem-vind{o/a}! Fica à vontade.'], 'curta': ['Até já!']}
    prim = [fala(t) for t in ' | '.join(f.get('primeira', [])).split(' | ') if t.strip()]
    d = {'id': npc['id'], 'voz': 'normal',
         'primeira': [{**x, 'quem': nome} for x in prim],
         'dia': [fala(t, '%s_dia_%02d' % (npc['id'], i + 1)) for i, t in enumerate(f.get('dia', []))],
         'curtas': [fala(t, '%s_curta_%d' % (npc['id'], i + 1)) for i, t in enumerate(f.get('curta', []))],
         'perguntar': {'rumores': [fala(t, '%s_rumor_%d' % (npc['id'], i + 1)) for i, t in enumerate(f.get('rumor', []))],
                       'andar': {str(regiao): fala(f['andar'][0])['texto']} if f.get('andar') else {},
                       'vida': {'0': fala(f['vida'][0])['texto']} if f.get('vida') else {},
                       'torre': []},
         'presentes': {}, 'aniversario': {}, 'festivais': {}, 'bosses': {}, 'cenas': [], 'missoes': [], 'estados': []}
    return d


def transeuntes():
    """docs/CIDADES.md, secção 4.1: as frases da gente na rua, por sítio."""
    texto = open(os.path.join(RAIZ, 'docs', 'CIDADES.md'), encoding='utf-8').read()
    m = re.search(r'^### 4\.1 .*?\n(.*?)(?=^---|^## )', texto, re.S | re.M)
    out = {}
    if not m:
        return out
    itens = re.split(r'^- ', m.group(1), flags=re.M)[1:]
    for it in itens:
        mm = re.match(r'\*\*(\w+)\*\*(?: \([^)]*\))?:\s*(.*)', ' '.join(l.strip() for l in it.split('\n')), re.S)
        if mm:
            out[mm.group(1)] = [f.strip() for f in mm.group(2).split(' · ') if f.strip()]
    return out


def main():
    ids = {os.path.basename(f)[:-len('_parado_baixo.png')] for f in glob.glob(os.path.join(RAIZ, 'arte', 'npcs', '*_parado_baixo.png'))}
    ascendia = {n['id'] for n in json.load(open(os.path.join(RAIZ, 'dados', 'npcs.json'), encoding='utf-8'))}
    falas = ler_falas()
    povs, npcs, lojas = [], [], []
    sem = []
    for r in REGIOES:
        for p in fichas_regiao(r):
            for n in p['npcs']:
                n['id'] = sprite_id(n['nome_pt'], ids)
                if not n['id']:
                    sem.append('%s (%s)' % (n['nome_pt'], p['nome_pt']))
            p['npcs'] = [n for n in p['npcs'] if n['id'] and n['id'] not in ascendia]
            edif, deco = pecas_3d(p)
            if p['id'] in SPRITES:
                pasta = 'res://arte/regioes/%s/natureza/' % REGIOES[r]
                edif = [pasta + x + '.png' for x in SPRITES[p['id']]['edificios']]
                deco = [pasta + x + '.png' for x in SPRITES[p['id']]['decoracao']]
            deco = [d for d in deco if not any(k in d for k in ('lagoa', 'lago_', 'piscina'))]
            # comum a todas: lanternas, barris, caixotes e (com loja) bancas do mercado
            r1 = 'res://arte/regioes/r01_floresta/natureza/'
            extra = ['lanterna_quente', 'barril_2', 'caixote_2', 'lanterna_quente', 'caixote']
            if 'loja' in servicos(p):
                extra += ['banca_vermelha', 'banca_azul']
            deco = deco + [r1 + x + '.png' for x in extra]
            p['edificios'] = edif
            p['decoracao'] = deco
            p['servicos'] = servicos(p)
            p['donos'] = {s: dono(p, s) for s in p['servicos']}
            povs.append(p)
            for n in p['npcs']:
                serv = [s for s, quem in p['donos'].items() if quem == n['id']]
                npcs.append({'id': n['id'], 'nome_pt': n['nome_pt'], 'titulo_pt': re.split(r'[;,(]', n['quem_pt'])[0].strip(),
                             'quem_pt': n['quem_pt'], 'faz_pt': n['faz_pt'], 'sprite': 'res://arte/npcs/' + n['id'],
                             'retrato': 'res://arte/retratos/%s_' % n['id'], 'povoacao': p['id'], 'andar': p['andar'], 'regiao': r,
                             'servicos': serv, 'adora': [], 'gosta': [], 'detesta': []})
                d = dialogo(n, falas.get(n['id']), r)
                with open(os.path.join(RAIZ, 'dados', 'dialogos', n['id'] + '.json'), 'w', encoding='utf-8') as fh:
                    json.dump(d, fh, ensure_ascii=False, indent=1)
            if 'loja' in p['servicos'] and p['donos'].get('loja'):
                base = ['pocao_vida_p', 'pocao_mana_p', 'antidoto', 'ligadura', 'tocha', 'isco'] if r <= 3 else \
                       ['pocao_vida_m', 'pocao_mana_p', 'antidoto', 'ligadura', 'pedra_regresso', 'isco']
                precos = {'pocao_vida_p': 30, 'pocao_mana_p': 40, 'antidoto': 25, 'ligadura': 20, 'tocha': 10, 'isco': 5,
                          'pocao_vida_m': 150, 'pedra_regresso': 50}
                itens = [{'item': i, 'preco': precos[i], 'stock': -1, 'quando_pt': 'início', 'cond': ''} for i in base]
                itens += [{'item': i, 'preco': 30 + 12 * r, 'stock': 5, 'quando_pt': 'início', 'cond': ''} for i in COMIDA.get(r, [])]
                lojas.append({'id': 'loja_' + p['id'], 'auto': [], 'dono': p['donos']['loja'], 'nome_pt': 'Loja de ' + p['nome_pt'],
                              'horario': [7, 21] if p['id'] != 'mercado_fantasma' else [20, 5], 'horario_pt': '',
                              'compra': True, 'itens': itens})
    for p in povs:   # quantas pessoas na rua (docs/CIDADES.md 4.1): povoação grande 6, pequena 3
        p['transeuntes'] = 6 if len(p['npcs']) >= 4 or len(p['edificios']) >= 4 else 3
    with open(os.path.join(RAIZ, 'dados', 'transeuntes.json'), 'w', encoding='utf-8') as fh:
        json.dump(transeuntes(), fh, ensure_ascii=False, indent=1)
    for nome, dados in (('povoacoes', povs), ('npcs_povoacoes', npcs), ('lojas_povoacoes', lojas)):
        with open(os.path.join(RAIZ, 'dados', nome + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(dados, fh, ensure_ascii=False, indent=1)
    print('povoações: %d · NPCs: %d · lojas: %d · com falas: %d' % (len(povs), len(npcs), len(lojas), sum(1 for n in npcs if n['id'] in falas)))
    for p in povs:
        print('  %3d %-32s edif %2d deco %2d  npcs %d  %s' % (p['andar'], p['id'], len(p['edificios']), len(p['decoracao']), len(p['npcs']), p['servicos']))
    if sem:
        print('sem sprite:', ', '.join(sem))


if __name__ == '__main__':
    main()
