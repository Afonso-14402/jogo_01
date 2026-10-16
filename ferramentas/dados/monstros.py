"""Fichas das regiões (docs/regioes/rXX_*.md) e docs/BOSSES.md -> dados/monstros.json e dados/bosses.json
(formato em docs/PROGRAMACAO.md, secção 5.2). O nível, HP e ATQ não vão para aqui: calculam-se no jogo.

Uso: python3 ferramentas/dados/monstros.py
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, seccao, limpar, numero, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
TIPOS = {'fraco': 'fraco', 'normal': 'normal', 'rapido': 'rapido', 'tanque': 'tanque', 'atirador': 'atirador',
         'mago': 'mago', 'voador': 'voador'}
ELEMENTOS = {'fogo': 'fogo', 'gelo': 'gelo', 'raio': 'raio', 'veneno': 'veneno', 'luz': 'luz', 'sombra': 'sombra',
             'agua': 'gelo', 'fisico': 'fisico', 'trevas': 'sombra', 'eletric': 'raio', 'electric': 'raio'}


def _arte():
    """id -> prefixo do sprite (res://...) de todas as criaturas desenhadas."""
    d = {}
    for f in glob.glob(os.path.join(RAIZ, 'arte', 'regioes', '*', '*', '*_parado_lado.png')):
        rel = os.path.relpath(f, RAIZ).replace(os.sep, '/')
        nome = os.path.basename(f)[:-len('_parado_lado.png')]
        d[nome] = 'res://' + rel[:-len('_parado_lado.png')]
    return d


ARTE = _arte()


# criaturas que não têm desenho próprio: usam o de outra com um shader (docs/regioes/r10_abismo.md, secção 12)
ALIAS = {'golem_forjado_n_7': 'golem_forjado_n7'}
SPRITE_EXTRA = {'clone_espelhado': 'res://arte/heroi/heroi', 'eco': 'dinamico'}


def id_de(nome):
    s = slug(nome)
    if s in ALIAS:
        return ALIAS[s]
    for cand in (s, re.sub(r'^(o|a|os|as)_', '', s), re.sub(r'_(de|do|da|dos|das)_', '_', s)):
        if cand in ARTE:
            return cand
    return s


def elementos(texto):
    out = []
    for p in re.split(r'[,·e/]| e ', ascii_(limpar(texto))):
        for k, v in ELEMENTOS.items():
            if k in p and v not in out:
                out.append(v)
    return out


def ataques(texto):
    """'**Mordida** (×1,0; aviso 0,35 s) · **Investida** de 6 m (×1,4; aviso 0,6 s: agacha-se)' -> lista"""
    out = []
    for parte in re.split(r' · ', texto):
        m = re.search(r'\*\*(.+?)\*\*(.*)', parte)
        if not m:
            continue
        nome, resto = m.group(1), m.group(2)
        mult = re.search(r'×\s*(\d+(?:,\d+)?)', resto)
        aviso = re.search(r'aviso\s*(\d+(?:,\d+)?)\s*s', resto)
        alcance = re.search(r'(\d+(?:,\d+)?)\s*m\b', resto)
        a = {'id': slug(nome), 'nome_pt': nome, 'mult': float(mult.group(1).replace(',', '.')) if mult else 1.0,
             'aviso': float(aviso.group(1).replace(',', '.')) if aviso else 0.5,
             'alcance': float(alcance.group(1).replace(',', '.')) if alcance else 1.6, 'recarga': 1.5}
        if a['alcance'] > 3.0:
            a['recarga'] = 5.0
        a['texto'] = limpar(resto).strip(' ()')
        out.append(a)
    return out or [{'id': 'golpe', 'mult': 1.0, 'aviso': 0.4, 'alcance': 1.5, 'recarga': 1.4}]


def drops(texto, itens):
    out = []
    for parte in re.split(r' · |, ', limpar(texto)):
        m = re.match(r'(.+?)\s+(\d+(?:,\d+)?)\s*%(?:\s*\((\d+)\s*[–-]\s*(\d+)\))?', parte.strip())
        if not m:
            continue
        nome = m.group(1).strip()
        iid = itens.get(slug(nome)) or itens.get(re.sub(r'_(de|do|da)_', '_', slug(nome))) or slug(nome)
        q = [int(m.group(3)), int(m.group(4))] if m.group(3) else [1, 1]
        out.append({'item': iid, 'hipotese': float(m.group(2).replace(',', '.')) / 100.0, 'qtd': q})
    return out


def ler_itens():
    """nome (slug) -> id, de docs/textos/itens.md."""
    d = {}
    for i, nome in re.findall(r'^\| `([a-z0-9_]+)` \| ([^|]+?) \|', open(os.path.join(RAIZ, 'docs', 'textos', 'itens.md'),
                                                                     encoding='utf-8').read(), re.M):
        d[slug(limpar(nome))] = i
        d[re.sub(r'_(de|do|da)_', '_', slug(limpar(nome)))] = i
    return d


def ficha(nome, linhas, regiao, itens):
    kv = {}
    for l in linhas:
        vals = list(l.values())
        if len(vals) >= 2:
            kv[limpar(vals[0])] = vals[1]
    tipo_txt = ascii_(limpar(kv.get('Tipo', 'normal')))
    tipo = next((v for k, v in TIPOS.items() if tipo_txt.startswith(k) or f' {k}' in tipo_txt[:12]), 'normal')
    grupo = re.search(r'(\d+)\s*[–-]\s*(\d+)', kv.get('Tipo', ''))
    andares = [int(x) for x in re.findall(r'\d+', kv.get('Andares', ''))]
    fr = kv.get('Fraco / Resiste', '— / —').split('/')
    tam = re.search(r'(\d+)\s*×', kv.get('Tamanho', '32×32'))
    mid = id_de(nome)
    return {'id': mid, 'nome': 'MONSTRO_' + mid.upper(), 'nome_pt': nome, 'regiao': regiao, 'tipo': tipo,
            'fraquezas': elementos(fr[0]) if fr else [], 'resistencias': elementos(fr[1]) if len(fr) > 1 else [],
            'imunidades': [], 'visao': 8, 'cobarde': 'cobarde' in tipo_txt,
            'noturno': 'noite' in ascii_(kv.get('Andares', '') + kv.get('Comportamento', '')),
            'grupo': [int(grupo.group(1)), int(grupo.group(2))] if grupo else [1, 1], 'andares': andares,
            'ataques': ataques(kv.get('Ataques', '')), 'drops': drops(kv.get('Drops', ''), itens),
            'elite': limpar(kv.get('Elite', '')), 'comportamento': limpar(kv.get('Comportamento', '')),
            'sprite': ARTE.get(mid, ''), 'tamanho_px': int(tam.group(1)) if tam else 32}


def gerar():
    itens = ler_itens()
    monstros, falta = [], []
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r*.md'))):
        regiao = int(os.path.basename(f)[1:3])
        texto = open(f, encoding='utf-8').read()
        # 3. monstros (uma ficha por monstro)
        sec3 = seccao(texto, '## 3.')
        for bloco in re.split(r'^### 3\.\d+ ', sec3, flags=re.M)[1:]:
            nome = bloco.split('\n')[0].strip()
            t = tabelas(bloco)
            if t:
                monstros.append(ficha(nome, t[0][1], regiao, itens))
        # 4. monstros com nome
        for _, linhas in tabelas(seccao(texto, '## 4.')):
            for l in linhas:
                nome = limpar(l.get('Nome', ''))
                if not nome:
                    continue
                mid = id_de(nome)
                andares = [int(x) for x in re.findall(r'\b(\d{1,3})\b', l.get('Onde e quando', ''))[:4] if int(x) <= 100]
                monstros.append({'id': mid, 'nome': 'MONSTRO_' + mid.upper(), 'nome_pt': nome, 'regiao': regiao, 'tipo': 'com_nome',
                                 'fraquezas': [], 'resistencias': [], 'imunidades': [], 'cobarde': False, 'noturno': 'noite' in ascii_(l.get('Onde e quando', '')),
                                 'grupo': [1, 1], 'andares': andares, 'ataques': ataques(l.get('Luta', '')),
                                 'drops': drops(l.get('Drops', ''), itens), 'luta': limpar(l.get('Luta', '')),
                                 'sprite': ARTE.get(mid, ''), 'tamanho_px': 48})
        # 6. guardiões
        for _, linhas in tabelas(seccao(texto, '## 6.')):
            for l in linhas:
                if not l.get('Andar', '').strip().isdigit():
                    continue
                nome = limpar(l.get('Guardião', ''))
                mid = id_de(nome)
                monstros.append({'id': mid, 'nome': 'MONSTRO_' + mid.upper(), 'nome_pt': nome, 'regiao': regiao, 'tipo': 'guardiao',
                                 'fraquezas': elementos(l.get('Fraco a', '')), 'resistencias': [], 'imunidades': [],
                                 'cobarde': False, 'noturno': False, 'grupo': [1, 1], 'andares': [int(l['Andar'])],
                                 'ataques': ataques(l.get('Ataques', '')), 'drops': [], 'arma_guardiao': limpar(l.get('Arma de guardião', '')),
                                 'aspeto': limpar(l.get('Aspeto', '')), 'sprite': ARTE.get(mid, ''), 'tamanho_px': 48})
    # bosses
    bosses = []
    texto = open(os.path.join(RAIZ, 'docs', 'BOSSES.md'), encoding='utf-8').read()
    for bloco in re.split(r'^## \d+\. ', texto, flags=re.M)[1:]:
        cab = bloco.split('\n')[0]
        m = re.match(r'(.+?) — andar (\d+)(?: \((.+?)\))?', cab)
        if not m:
            continue
        nome, andar, tipo = m.group(1).strip(), int(m.group(2)), (m.group(3) or 'boss')
        tipo = 'mini_boss' if 'mini' in tipo else 'boss'
        t = tabelas(bloco)
        kv = {}
        fases = []
        for _, linhas in t:
            for l in linhas:
                vals = list(l.values())
                if 'Fase' in l:
                    fases.append({'fase': int(numero(l['Fase'], 1)), 'vida': limpar(l.get('Vida', '')), 'ataques': ataques(l.get('Ataques', ''))})
                elif len(vals) >= 2:
                    kv[limpar(vals[0])] = vals[1]
        mid = id_de(nome)
        nt = re.search(r'(\d+)\s*·\s*(\d+)×', kv.get('Nível / Tamanho', ''))
        bosses.append({'id': mid, 'nome': 'BOSS_' + mid.upper(), 'nome_pt': nome, 'andar': andar, 'tipo': tipo,
                       'titulo': limpar(kv.get('Título', '')).strip('*'), 'nivel': int(nt.group(1)) if nt else andar + 3,
                       'tamanho_px': int(nt.group(2)) if nt else 96, 'fraquezas': elementos(kv.get('Fraco a', '').split('·')[0]),
                       'resistencias': elementos(kv.get('Fraco a', '').split('resiste a')[-1]) if 'resiste' in kv.get('Fraco a', '') else [],
                       'imunidades': [], 'arena': limpar(kv.get('Arena', '')), 'mecanica': limpar(kv.get('Mecânica especial', '')),
                       'fases': fases, 'arma_unica': limpar(kv.get('Arma única', '')), 'trofeu': limpar(kv.get('Troféu', '')),
                       'sprite': ARTE.get(mid, '')})
    for x in monstros + bosses:
        x['sprite'] = x['sprite'] or SPRITE_EXTRA.get(x['id'], '')
        if not x['sprite']:
            falta.append(x['id'])
    # monstros que não estão nas fichas das regiões (docs/SISTEMAS.md, secção 9.3)
    monstros.append({'id': 'mimico', 'nome': 'MONSTRO_MIMICO', 'nome_pt': 'Mímico', 'regiao': 0, 'tipo': 'tanque',
                     'fraquezas': ['fogo'], 'resistencias': [], 'imunidades': ['veneno'], 'cobarde': False, 'noturno': False,
                     'grupo': [1, 1], 'andares': [], 'ataques': [{'id': 'mordida', 'mult': 1.3, 'aviso': 0.5, 'alcance': 1.8, 'recarga': 1.6},
                                                               {'id': 'salto', 'mult': 1.6, 'aviso': 0.8, 'alcance': 4.0, 'recarga': 5.0}],
                     'drops': [], 'drop_bau': 'prata', 'sprite': 'res://arte/monstros_comuns/mimico', 'tamanho_px': 32})
    # sem repetidos (o mesmo monstro pode aparecer em duas secções)
    vistos, unicos = set(), []
    for x in monstros:
        if x['id'] not in vistos:
            vistos.add(x['id'])
            unicos.append(x)
    with open(os.path.join(RAIZ, 'dados', 'monstros.json'), 'w', encoding='utf-8') as f:
        json.dump(unicos, f, ensure_ascii=False, indent=1)
    with open(os.path.join(RAIZ, 'dados', 'bosses.json'), 'w', encoding='utf-8') as f:
        json.dump(bosses, f, ensure_ascii=False, indent=1)
    print('ok', len(unicos), 'monstros,', len(bosses), 'bosses;', len(falta), 'sem sprite:', falta[:20])


if __name__ == '__main__':
    gerar()
