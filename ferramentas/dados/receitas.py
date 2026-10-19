"""Receitas e recursos dos documentos -> dados/receitas.json e dados/recursos.json; também põe os valores das
armaduras (DEF, RES, espaço, conjunto, tier) em dados/itens.json.

Receitas (docs/SISTEMAS.md, secção 11):
  armas (docs/ARMAS.md, forja, +20% do preço em ouro) · armaduras (docs/EQUIPAMENTO.md, forja ou tear)
  poções e bombas (docs/ITENS.md, alquimia) · comida (docs/ITENS.md, fogão; 🔥 também na fogueira)
  lingotes (docs/regioes/rXX, secção 2: "3 minérios + 1 Carvalho, na forja") · ferramentas (docs/ARMAS.md, secção 10)
Recursos (docs/SISTEMAS.md, secção 12): os nós de recolha de cada região, com a ferramenta e os andares.

Uso: python3 ferramentas/dados/receitas.py   (depois de armas.py e itens.py)
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, slug, ascii_, numero

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
INICIO = {'pocao_vida_p', 'antidoto', 'ligadura', 'colirio', 'espetada_coelho', 'lingote_cobre', 'picareta_cobre',
          'machado_lenhador_cobre', 'espada_cobre', 'adaga_cobre', 'arco_cobre'}
SLOTS = {'cabeca': 'cabeca', 'corpo': 'corpo', 'maos': 'maos', 'pes': 'pes', 'capa': 'capa'}
FALTAM = set()


def indice():
    it = json.load(open(os.path.join(RAIZ, 'dados', 'itens.json'), encoding='utf-8'))
    ar = json.load(open(os.path.join(RAIZ, 'dados', 'armas.json'), encoding='utf-8'))
    ind = {}
    for x in it + ar:
        for k in (x['id'], slug(x['nome_pt']), re.sub(r'_(de|do|da|dos|das)_', '_', slug(x['nome_pt']))):
            ind.setdefault(k, x['id'])
    return it, ar, ind


def achar(nome, ind):
    s = slug(nome)
    for cand in (s, re.sub(r'_(de|do|da|dos|das)_', '_', s), re.sub(r'^(madeira|minerio)_(de_)?', '', s),
                 re.sub(r's$', '', s), re.sub(r'_(de|do|da)_.*', '', s), 'madeira_' + s):
        if cand in ind:
            return ind[cand]
    FALTAM.add(nome)
    return None


def ingredientes(texto, ind):
    """'2 Erva Verde + 1 Água Limpa' -> [['erva_verde', 2], ['agua_limpa', 1]] (None se não der para ler)"""
    t = limpar(re.sub(r'\(.*?\)', '', texto))
    if not re.match(r'\s*\d', t):
        return None
    out = []
    for parte in re.split(r'\s\+\s', t):
        m = re.match(r'\s*(\d+)\s+(.+?)\s*$', parte)
        if not m:
            return None
        i = achar(m.group(2), ind)
        if not i:
            return None
        out.append([i, int(m.group(1))])
    return out


def gerar():
    itens, armas, ind = indice()
    por_id = {x['id']: x for x in itens}
    receitas = []

    def junta(rid, resultado, ingr, estacao, skill, ouro=0, qtd=1, onde='', extra=None):
        if not ingr:
            return
        if not resultado:   # o item ainda não existe em docs/textos/itens.md: sem receita (senão fica uma receita sem id)
            FALTAM.add('resultado de %s' % ' + '.join('%s ×%s' % (i[0], i[1]) for i in ingr))
            return
        r = {'id': rid, 'resultado': resultado, 'qtd': qtd, 'estacao': estacao, 'ingredientes': ingr, 'ouro': ouro,
             'skill': skill, 'skill_min': 1, 'inicio': resultado in INICIO or 'início' in onde, 'onde_pt': onde}
        if extra:
            r.update(extra)
        receitas.append(r)

    # armas
    texto = open(os.path.join(RAIZ, 'docs', 'ARMAS.md'), encoding='utf-8').read()
    for titulo, linhas in tabelas(texto):
        for l in linhas:
            rc = next((v for k, v in l.items() if k.startswith('Receita')), None)
            if 'ID' in l and rc:
                aid = limpar(l['ID'])
                tier = next((a.get('tier', 1) for a in armas if a['id'] == aid), 1)
                junta(aid, aid, ingredientes(rc, ind), 'forja', 'ferraria', int(numero(l.get('Preço', '0')) * 0.2),
                      extra={'skill_min': max(1, (tier - 1) * 5)})
            elif 'Ferramenta' in l and 'Picareta' in l['Ferramenta'] or 'Machado de lenhador' in l.get('Ferramenta', ''):
                pass
    # ferramentas: 3 lingotes + 1 madeira (picareta) · 3 lingotes + 2 madeira (machado), por tier
    metais = [('cobre', 'lingote_cobre', 'carvalho'), ('ferro', 'lingote_ferro', 'escora_velha'), ('aco', 'lingote_aco', 'madeira_mangue'),
              ('prata', 'lingote_prata', 'acacia'), ('gelo_eterno', 'barra_gelo_eterno', 'pinheiro_nevado'),
              ('coral_abissal', 'barra_coral_abissal', 'madeira_naufragio'), ('obsidiana', 'barra_obsidiana', 'madeira_carbonizada'),
              ('mitril', 'lingote_mitril', 'madeira_sagrada'), ('oricalco', 'lingote_oricalco', 'madeira_celeste'),
              ('estelar', 'lingote_estelar', 'madeira_estelar')]
    for tier, (nome, lingote, madeira) in enumerate(metais, 1):
        l_id = achar(lingote, ind) or lingote
        m_id = achar(madeira, ind)
        for ferr, nmad in (('picareta', 1), ('machado_lenhador', 2)):
            fid = f'{ferr}_{nome}'
            if fid in por_id:
                ingr = [[l_id, 3]] + ([[m_id, nmad]] if m_id else [])
                junta(fid, fid, ingr, 'forja', 'ferraria', 18 * tier * tier, extra={'skill_min': max(1, (tier - 1) * 5)})
                por_id[fid].update({'ferramenta': ferr.replace('_lenhador', ''), 'tier': tier})
    # armaduras
    texto = open(os.path.join(RAIZ, 'docs', 'EQUIPAMENTO.md'), encoding='utf-8').read()
    for titulo, linhas in tabelas(texto):
        m = re.match(r'Tier (\d+) — Conjunto (.+?) \(', titulo)
        if not m:
            continue
        tier = int(m.group(1))
        conj = re.sub(r'_(de|do|da|dos|das)_', '_', slug(m.group(2)))
        for l in linhas:
            slot = SLOTS.get(slug(l['Peça']))
            # o id da peça usa parte do nome do conjunto (pele_crocodilo -> crocodilo, couro_deserto -> deserto)
            p = conj.split('_')
            cands = [conj] + ['_'.join(p[i:j]) for i in range(len(p)) for j in range(len(p), i, -1)]
            pid = next((f'{c}_{slot}' for c in cands if f'{c}_{slot}' in por_id), None)
            if not pid:
                FALTAM.add('armadura %s_%s' % (conj, slot))
                continue
            por_id[pid].update({'def': int(numero(l['DEF'])), 'res': int(numero(l['RES'])), 'peso': numero(l['Peso']),
                                'preco': int(numero(l['Preço'])), 'espaco': slot, 'conjunto': conj, 'tier': tier})
            ingr = ingredientes(l['Receita'], ind)
            metal = any('lingote' in i[0] or 'barra' in i[0] for i in ingr or [])
            junta(pid, pid, ingr, 'forja' if metal else 'tear', 'ferraria' if metal else 'costura',
                  int(numero(l['Preço']) * 0.2), extra={'skill_min': max(1, (tier - 1) * 5)})
    # poções, bombas e comida
    texto = open(os.path.join(RAIZ, 'docs', 'ITENS.md'), encoding='utf-8').read()
    for titulo, linhas in tabelas(texto):
        for l in linhas:
            if 'Poção' in l and 'Receita (mesa de alquimia)' in l:
                nome = l['Poção']
                if '/' in nome:
                    continue
                pid = achar(nome, ind)
                junta(pid, pid, ingredientes(l['Receita (mesa de alquimia)'], ind), 'alquimia', 'alquimia',
                      onde=limpar(l.get('Disponível', '')))
            elif 'Bomba' in l and 'Receita' in l:
                pid = achar(l['Bomba'], ind)
                junta(pid, pid, ingredientes(l['Receita'], ind), 'alquimia', 'alquimia')
            elif 'Prato' in l and 'Ingredientes' in l:
                nome = limpar(l['Prato']).replace('🔥', '').strip()
                pid = achar(nome, ind)
                if not pid:
                    continue
                fog = '🔥' in l['Prato']
                cura = numero(l.get('Cura', '0'))
                if pid in por_id and cura and not por_id[pid].get('efeito'):
                    por_id[pid]['efeito'] = {'curar_hp_percent': cura}
                junta(pid, pid, ingredientes(l['Ingredientes'], ind), 'fogueira' if fog else 'fogao', 'cozinha',
                      onde=limpar(l.get('Onde se aprende', '')))
    # lingotes e recursos das regiões
    recursos = []
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r*.md'))):
        regiao = int(os.path.basename(f)[1:3])
        texto = open(f, encoding='utf-8').read()
        sec = texto.split('## 2. Materiais', 1)[1].split('\n---', 1)[0] if '## 2. Materiais' in texto else ''
        for _, linhas in tabelas(sec):
            for l in linhas:
                if 'Recurso' not in l:
                    continue
                rid = achar(l['Recurso'], ind)
                como = ascii_(limpar(l.get('Como', '')))
                andares = [int(n) for n in re.findall(r'\b(\d{1,3})\b', l.get('Onde', '')) if (regiao - 1) * 10 < int(n) <= regiao * 10]
                ferr = 'picareta' if 'picareta' in como else ('machado' if 'machado' in como else ('mao' if 'mao' in como or 'lamina' in como else None))
                if rid and ferr:
                    m = re.search(r'picareta de (\w+)', como)
                    recursos.append({'item': rid, 'regiao': regiao, 'ferramenta': ferr, 'andares': andares or list(range((regiao - 1) * 10 + 1, regiao * 10 + 1)),
                                     'raro': 'raro' in ascii_(l.get('Onde', '')) or '%' in l.get('Onde', ''), 'tier': regiao,
                                     'onde_pt': limpar(l.get('Onde', ''))})
                u = re.search(r'(Lingote|Barra) de ([^(]+?) \((\d+) [^+]+\+ (\d+) ([^,)]+)', l.get('Usos', ''))
                if rid and u:
                    lid = achar(f'{u.group(1)} de {u.group(2)}', ind)
                    comb = achar(u.group(5), ind)
                    if lid and comb:
                        junta(lid, lid, [[rid, int(u.group(3))], [comb, int(u.group(4))]], 'forja', 'ferraria', 5 * regiao,
                              onde='região %d' % regiao)
    # materiais de cada tier (docs/ITENS.md, 6): para as melhorias +1…+10
    tiers = []
    for _, linhas in tabelas(open(os.path.join(RAIZ, 'docs', 'ITENS.md'), encoding='utf-8').read()):
        for l in linhas:
            if 'Lingote / barra' in l and 'Cristal' in l:
                tiers.append({'lingote': achar(re.sub(r'\(.*', '', l['Lingote / barra']).strip(), ind),
                              'cristal': achar(limpar(l['Cristal']), ind),
                              'gema': achar(limpar(l['Gema']).split(',')[0].strip(), ind) if '—' not in l['Gema'] else None})
    for i, t in enumerate(tiers):
        t['gema'] = t['gema'] or tiers[i - 1]['gema']
    with open(os.path.join(RAIZ, 'dados', 'materiais_tier.json'), 'w', encoding='utf-8') as fo:
        json.dump(tiers, fo, ensure_ascii=False, indent=1)
    with open(os.path.join(RAIZ, 'dados', 'receitas.json'), 'w', encoding='utf-8') as fo:
        json.dump(receitas, fo, ensure_ascii=False, indent=1)
    with open(os.path.join(RAIZ, 'dados', 'recursos.json'), 'w', encoding='utf-8') as fo:
        json.dump(recursos, fo, ensure_ascii=False, indent=1)
    with open(os.path.join(RAIZ, 'dados', 'itens.json'), 'w', encoding='utf-8') as fo:
        json.dump(itens, fo, ensure_ascii=False, indent=1)
    from collections import Counter
    print('ok', len(receitas), 'receitas', dict(Counter(r['estacao'] for r in receitas)), ';', len(recursos), 'recursos;',
          'armaduras com DEF:', sum(1 for x in itens if x.get('espaco')), '; nomes por ligar:', len(FALTAM))
    print(sorted(FALTAM)[:60])


if __name__ == '__main__':
    gerar()
