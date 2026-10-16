"""Missões (docs/MISSOES.md, docs/regioes/rXX secção 8, docs/NPCS.md coluna "Missões") -> dados/missoes.json
(formato de docs/PROGRAMACAO.md, secção 5.6).

O objetivo em texto passa a passos que o jogo sabe contar:
  matar (monstro, qtd, andar?, noite?) · derrotar (monstro ou boss) · apanhar (item, qtd: tê-los na mochila) ·
  pescar (qtd) · ir_a (andar) · explorar (andar, percent) · livre (texto: a história/um evento marca-o como feito)
As recompensas: ouro, xp, pontos_guilda, itens, amizade, receitas, titulo e o texto original.

Uso: python3 ferramentas/dados/missoes.py   (depois de itens, armas, monstros e dialogos)
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, slug, ascii_, numero

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
PONTOS = {'F': 10, 'E': 20, 'D': 40, 'C': 80, 'B': 150, 'A': 300, 'S': 600, 'SS': 1200, 'SSS': 2400}


def carregar():
    j = lambda n: json.load(open(os.path.join(RAIZ, 'dados', n), encoding='utf-8'))
    itens, armas, monstros, bosses, npcs = j('itens.json'), j('armas.json'), j('monstros.json'), j('bosses.json'), j('npcs.json')
    ind_i, ind_m, ind_n = {}, {}, {}
    for x in itens + armas:
        for k in (slug(x['nome_pt']), re.sub(r'_(de|do|da|dos|das)_', '_', slug(x['nome_pt'])), x['id']):
            ind_i.setdefault(k, x['id'])
    for x in monstros + bosses:
        for k in (slug(x['nome_pt']), re.sub(r'_(de|do|da|dos|das)_', '_', slug(x['nome_pt'])), x['id']):
            ind_m.setdefault(k, x['id'])
    for x in npcs:
        ind_n[slug(x['nome_pt'])] = x['id']
        ind_n[x['id']] = x['id']
    return ind_i, ind_m, ind_n


def achar(nome, ind):
    s = slug(re.sub(r'^(o|a|os|as)\s+', '', ascii_(nome.strip())))
    cands = [s, re.sub(r'_(de|do|da|dos|das)_', '_', s), re.sub(r's$', '', s), re.sub(r'es$', '', s),
             re.sub(r'(\w+?)s_', r'\1_', s), re.sub(r'(\w+?)s(_|$)', r'\1\2', s)]
    for c in cands:
        if c in ind:
            return ind[c]
    for c in cands:   # o início do nome ("Lobos Cinzentos" -> lobo_cinzento)
        for k in ind:
            if k.startswith(c + '_') or c.startswith(k + '_'):
                return ind[k]
    return None


def passos(obj, ind_i, ind_m, ind_n):
    t = limpar(obj)
    a = ascii_(t)
    out = []
    for parte in re.split(r'\s+·\s+|;\s+', t):
        p = ascii_(parte).strip()
        m = re.match(r'(matar|vencer|derrotar)\s+(\d+)\s+(.+?)(\s+a noite)?(?:\s+(?:no|nos)\s+andar(?:es)?\s+(\d+))?$', p)
        if m:
            mid = achar(re.sub(r'\s+(no|na|do|da)\s+.*$', '', m.group(3)), ind_m)
            if mid:
                s = {'tipo': 'matar', 'monstro': mid, 'qtd': int(m.group(2))}
                if m.group(4):
                    s['noite'] = True
                if m.group(5):
                    s['andar'] = int(m.group(5))
                out.append(s)
                continue
        m = re.match(r'(?:vencer|derrotar)(?: o| a| os| as)?\s+(.+?)(?:\s+\(\d+\))?$', p)
        if m:
            mid = achar(m.group(1), ind_m)
            if mid:
                out.append({'tipo': 'derrotar', 'monstro': mid})
                continue
        m = re.match(r'(?:entregar|trazer|apanhar|recolher)?\s*(\d+)\s+(.+?)(?:\s+(?:para|ao|a|do|da)\s+.+)?$', p)
        if m and not p.startswith(('pescar', 'explorar', 'matar')):
            iid = achar(m.group(2), ind_i)
            if iid:
                out.append({'tipo': 'apanhar', 'item': iid, 'qtd': int(m.group(1))})
                continue
        m = re.match(r'pescar\s+(\d+)\s+peixes?', p)
        if m:
            out.append({'tipo': 'pescar', 'qtd': int(m.group(1))})
            continue
        m = re.match(r'(?:chegar|subir)\s+ao\s+andar\s+(\d+)', p)
        if m:
            out.append({'tipo': 'ir_a', 'andar': int(m.group(1))})
            continue
        m = re.match(r'explorar\s+(\d+)\s*%\s+do\s+andar\s+(\d+)', p)
        if m:
            out.append({'tipo': 'explorar', 'andar': int(m.group(2)), 'percent': int(m.group(1)) / 100})
            continue
        m = re.match(r'falar com (?:a |o )?(.+)', p)
        if m and achar(m.group(1), ind_n):
            out.append({'tipo': 'falar', 'npc': achar(m.group(1), ind_n)})
            continue
        out.append({'tipo': 'livre', 'texto': limpar(parte).strip()})
    return out


def recompensas(texto, rank, ind_i, ind_n):
    t = limpar(texto)
    r = {'texto': t}
    m = re.search(r'(\d[\d ]*)\s*ouro', t)
    if m:
        r['ouro'] = int(m.group(1).replace(' ', ''))
    m = re.search(r'(\d+)\s*pontos', t)
    r['pontos_guilda'] = int(m.group(1)) if m else (PONTOS.get(rank, 0) if rank else 0)
    itens, amiz, receitas = [], {}, []
    for parte in re.split(r'\s+·\s+|,\s+|\s+e\s+', t):
        p = parte.strip()
        if re.search(r'ouro|pontos', p):
            continue
        m = re.match(r'(?:❤️)+\s*(.+)', p)
        if m:
            nid = ind_n.get(slug(m.group(1))) or next((v for k, v in ind_n.items() if slug(m.group(1)).endswith(k)), None)
            if nid:
                amiz[nid] = 100 * max(1, p.count('❤️'))
            continue
        m = re.match(r'[Rr]eceita\s+(.+)', p)
        if m:
            rid = achar(m.group(1), ind_i)
            if rid:
                receitas.append(rid)
            continue
        m = re.match(r'(\d+)\s+(.+)', p)
        qtd, nome = (int(m.group(1)), m.group(2)) if m else (1, p)
        m = re.match(r'(.+?)\s*×\s*(\d+)', nome)
        if m:
            nome, qtd = m.group(1), int(m.group(2))
        nome = re.sub(r'\s*\(.*\)$', '', nome)
        iid = achar(nome, ind_i)
        if iid:
            itens.append([iid, qtd])
    if itens:
        r['itens'] = itens
    if amiz:
        r['amizade'] = amiz
    if receitas:
        r['receitas'] = receitas
    m = re.search(r'[Tt]ítulo \*?([^*·]+)', texto)
    if m:
        r['titulo'] = limpar(m.group(1)).strip()
    return r


def gerar():
    ind_i, ind_m, ind_n = carregar()
    missoes = []
    texto = open(os.path.join(RAIZ, 'docs', 'MISSOES.md'), encoding='utf-8').read()
    capitulo = 0
    for titulo, linhas in tabelas(texto):
        m = re.match(r'Capítulo (\d+)', titulo)
        if m:
            capitulo = int(m.group(1))
        elif titulo.startswith('Prólogo'):
            capitulo = 0
        for l in linhas:
            mid = limpar(l.get('ID', ''))
            if mid.startswith('H_'):
                missoes.append({'id': mid, 'nome_pt': limpar(l['Nome']), 'tipo': 'historia', 'capitulo': capitulo,
                                'descricao_pt': limpar(l.get('O que acontece', '')), 'dada_por': '',
                                'passos': passos(l.get('Passos', ''), ind_i, ind_m, ind_n),
                                'recompensas': recompensas(l.get('Recompensa', ''), '', ind_i, ind_n), 'rank': ''})
            elif mid.startswith('G_'):
                rank = limpar(l.get('Rank', 'F'))
                missoes.append({'id': mid, 'nome_pt': re.sub(r'\s*\(R\d+_\d+\)', '', limpar(l['Nome'])), 'tipo': 'guilda',
                                'rank': rank, 'dada_por': 'lyra', 'descricao_pt': limpar(l.get('Objetivo', '')),
                                'passos': passos(l.get('Objetivo', ''), ind_i, ind_m, ind_n),
                                'recompensas': recompensas(l.get('Recompensa', ''), rank, ind_i, ind_n)})
            elif mid.startswith('F_'):
                missoes.append({'id': mid, 'nome_pt': limpar(l.get('Festival', mid)), 'tipo': 'festival',
                                'quando_pt': limpar(l.get('Quando', '')), 'descricao_pt': limpar(l.get('Missão', '')),
                                'dada_por': 'aldric', 'passos': [{'tipo': 'livre', 'texto': limpar(l.get('Missão', ''))}],
                                'recompensas': recompensas(l.get('Recompensa', ''), '', ind_i, ind_n), 'rank': ''})
    # regiões
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r*.md'))):
        regiao = int(os.path.basename(f)[1:3])
        t = open(f, encoding='utf-8').read()
        sec = t.split('## 8. Missões da região', 1)[1].split('\n---', 1)[0] if '## 8. Missões da região' in t else ''
        for _, linhas in tabelas(sec):
            for l in linhas:
                mid = limpar(l.get('ID', ''))
                if not mid:
                    continue
                quem = limpar(l.get('Quem dá', ''))
                rank = re.search(r'rank\s+(\w+)', quem)
                missoes.append({'id': mid, 'nome_pt': limpar(l['Nome']), 'tipo': 'regiao', 'regiao': regiao,
                                'dada_por': achar(re.sub(r'\s*\(.*', '', quem), ind_n) or slug(re.sub(r'\s*\(.*', '', quem)),
                                'dada_por_pt': quem, 'rank': rank.group(1) if rank else '',
                                'descricao_pt': limpar(l.get('Objetivo', '')),
                                'passos': passos(l.get('Objetivo', ''), ind_i, ind_m, ind_n),
                                'recompensas': recompensas(l.get('Recompensa', ''), '', ind_i, ind_n)})
    # NPCs de Ascendia (coluna "Missões" de docs/NPCS.md)
    npcs_md = open(os.path.join(RAIZ, 'docs', 'NPCS.md'), encoding='utf-8').read()
    ja = {m['id'] for m in missoes}
    for bloco in re.split(r'^### ', npcs_md, flags=re.M)[1:]:
        t, _, resto = bloco.partition('\n')
        nome = re.match(r'[\d.]+\s+(.+?)\s+—', t)
        if not nome:
            continue
        nid = achar(nome.group(1), ind_n) or slug(nome.group(1))
        for _, linhas in tabelas(resto):
            for l in linhas:
                if limpar(l.get('_0', '')) != 'Missões':
                    continue
                for mm in re.finditer(r'\*\*(N_\w+)\*\*\s*\*([^*]+)\*\s*:\s*([^·]+?)(?:→\s*([^·]+))?(?=\s*·\s*\*\*[A-Z]\w*_|\s*$)', l.get('_1', '')):
                    if mm.group(1) in ja:
                        continue
                    missoes.append({'id': mm.group(1), 'nome_pt': limpar(mm.group(2)), 'tipo': 'npc', 'dada_por': nid,
                                    'rank': '', 'descricao_pt': limpar(mm.group(3)).strip(),
                                    'passos': passos(mm.group(3), ind_i, ind_m, ind_n),
                                    'recompensas': recompensas(mm.group(4) or '', '', ind_i, ind_n)})
    with open(os.path.join(RAIZ, 'dados', 'missoes.json'), 'w', encoding='utf-8') as fo:
        json.dump(missoes, fo, ensure_ascii=False, indent=1)
    from collections import Counter
    tipos = Counter(p['tipo'] for m in missoes for p in m['passos'])
    print('ok', len(missoes), 'missões', dict(Counter(m['tipo'] for m in missoes)), '; passos:', dict(tipos))


if __name__ == '__main__':
    gerar()
