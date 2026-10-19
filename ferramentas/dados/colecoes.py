"""Coleções (docs/ATIVIDADES.md, secções 5–7; docs/lore/diario_aren.md; peixes das regiões) ->
dados/paginas.json (100 páginas do diário do Aren), dados/peixes.json (60 peixes), dados/titulos.json e
dados/conquistas.json (100), com regras simples que o jogo sabe verificar.

Uso: python3 ferramentas/dados/colecoes.py   (depois de itens, monstros e missões)
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, slug, ascii_, numero

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')


def paginas():
    t = open(os.path.join(RAIZ, 'docs', 'lore', 'diario_aren.md'), encoding='utf-8').read()
    corpo = t.split('## 4. Texto completo das páginas', 1)[1].split('\n## 5.', 1)[0]
    out = []
    for bloco in re.split(r'^#### ', corpo, flags=re.M)[1:]:
        cab, _, resto = bloco.partition('\n')
        m = re.match(r'Página (\d+)\s*—\s*(.+)', cab)
        if not m:
            continue
        kv = {limpar(l.get('_0', '')): limpar(l.get('_1', '')) for _, ls in tabelas(resto) for l in ls}
        linhas = []
        for l in resto.split('\n'):
            if l.startswith('>'):
                linhas.append(re.sub(r'^\*|\*$', '', l[1:].strip()))
        texto = '\n'.join(linhas).strip()
        texto = re.sub(r'\n{3,}', '\n\n', texto)
        out.append({'numero': int(m.group(1)), 'titulo': limpar(re.sub(r'\*\(.*?\)\*', '', m.group(2))).strip(),
                    'onde_pt': kv.get('Onde', ''), 'desenho_pt': kv.get('Desenho', ''),
                    'tinta': ascii_(kv.get('Tinta', 'castanha')).split()[0] if kv.get('Tinta') else 'castanha',
                    'andar': int(m.group(1)), 'texto': texto})
    return out


def peixes(itens_ind):
    out = []
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r*.md'))):
        regiao = int(os.path.basename(f)[1:3])
        t = open(f, encoding='utf-8').read()
        if '### Peixes' not in t:
            continue
        sec = t.split('### Peixes', 1)[1].split('\n### ', 1)[0]
        for _, linhas in tabelas(sec):
            for l in linhas:
                if 'Peixe' not in l:
                    continue
                nome = limpar(re.sub(r'\(lendário\)', '', l['Peixe'])).strip()
                onde = limpar(l.get('Onde', ''))
                quando = ascii_(limpar(l.get('Quando', 'sempre')))
                andares = [int(x) for x in re.findall(r'\b(\d{1,3})\b', onde) if (regiao - 1) * 10 < int(x) <= regiao * 10]
                cond = []
                if 'dia' == quando.strip() or quando.startswith('dia'):
                    cond.append('hora entre 6 e 19')
                if 'noite' in quando:
                    cond.append('hora entre 20 e 23 || hora entre 0 e 4')
                m = re.search(r'(\d+):00[–-](\d+):00', l.get('Quando', ''))
                if m:
                    cond = ['hora entre %s e %d' % (m.group(1), int(m.group(2)) - 1)]
                if 'manha' in quando and not m:
                    cond.append('hora entre 6 e 10')
                for c in ('chuva', 'nevoeiro', 'neve', 'trovoada'):
                    if c in quando:
                        cond.append('clima == ' + c)
                for e in ('primavera', 'verao', 'outono', 'inverno'):
                    if e in quando:
                        cond.append('estacao == ' + e)
                rar = ascii_(limpar(l.get('Raridade', 'comum')))
                iid = itens_ind.get(slug(nome)) or slug(nome)
                out.append({'id': iid, 'nome_pt': nome, 'regiao': regiao, 'andares': andares, 'onde_pt': onde,
                            'quando_pt': limpar(l.get('Quando', '')), 'cond': ' && '.join(cond), 'raridade': rar,
                            'preco': int(numero(l.get('Preço', '0').replace(' ', ''))),
                            'cidade': 'ascendia' in ascii_(onde),
                            'estilo': {'comum': 'preguicoso', 'incomum': 'normal', 'raro': 'saltitao', 'lendario': 'rapido'}.get(rar, 'normal')})
    return out


def titulos(boss_ind):
    t = open(os.path.join(RAIZ, 'docs', 'ATIVIDADES.md'), encoding='utf-8').read()
    sec = t.split('## 6. Títulos', 1)[1].split('\n## 7.', 1)[0]
    out = []
    for _, linhas in tabelas(sec):
        for l in linhas:
            nome = limpar(l.get('Título', '')).strip('*')
            como = limpar(l.get('Como', ''))
            regra = ''
            a = ascii_(como)
            if slug(como) in boss_ind:
                regra = 'flag(boss_%s)' % boss_ind[slug(como)]
            elif re.match(r'^[a-z]\w*_\d+$', a.strip()):
                regra = 'flag(missao_%s)' % como.strip()
            elif a.startswith('comecar o jogo'):
                regra = '—'
            out.append({'id': slug(nome), 'nome_pt': nome, 'como_pt': como, 'bonus_pt': limpar(l.get('Bónus', '')), 'regra': regra})
    return out


def conquistas():
    t = open(os.path.join(RAIZ, 'docs', 'ATIVIDADES.md'), encoding='utf-8').read()
    sec = t.split('## 7. Conquistas', 1)[1].split('\n## 8.', 1)[0]
    out = []
    regras = [(r'^primeiro monstro$', 'contador(monstros) >= 1'), (r'^(\d[\d ]*) monstros$', 'contador(monstros) >= {0}'),
              (r'^primeiro critico$', 'contador(criticos) >= 1'), (r'^vencer um elite$', 'contador(elites) >= 1'),
              (r'^(\d+) elites$', 'contador(elites) >= {0}'), (r'chegar aos andares', None),
              (r'^(\d+) / (\d+) paginas', None), (r'^(\d+) baus de ouro$', 'contador(baus_ouro) >= {0}'),
              (r'^(\d+) mimicos$', 'contador(mimicos) >= {0}'), (r'^primeiro coracao$', 'max_coracoes >= 1'),
              (r'^(\d+) coracoes com alguem$', 'max_coracoes >= {0}'), (r'^(\d+) presentes$', 'contador(presentes) >= {0}'),
              (r'^primeira arma$', 'contador(armas_feitas) >= 1'), (r'^\+(\d+)$', 'contador(melhor_melhoria) >= {0}'),
              (r'^(\d+) pocoes$', 'contador(pocoes_feitas) >= {0}'), (r'^(\d+) pratos$', 'contador(pratos_feitos) >= {0}'),
              (r'^excelente$', 'contador(excelentes) >= 1'), (r'^rank sss$', 'rank >= SSS'),
              (r'^1 000 000 de ouro$', 'contador(ouro_total) >= 1000000'), (r'^acabar o prologo$', 'flag(missao_H_03)')]
    for _, linhas in tabelas(sec):
        for l in linhas:
            grupo = limpar(l.get('Grupo', ''))
            itens = [limpar(x).strip() for x in l.get('Conquistas (10 por grupo)', '').split('·')]
            for it in itens:
                if not it:
                    continue
                lista = [it]
                m = re.match(r'chegar aos andares ([\d, e]+)', ascii_(it))
                if m:
                    lista = ['chegar ao andar %s' % n for n in re.findall(r'\d+', m.group(1))]
                m = re.match(r'(\d+) / (\d+)(?: / (\d+))? (.+)', it)
                if m:
                    lista = ['%s %s' % (n, m.group(4)) for n in m.groups()[:3] if n]
                m = re.match(r'cada um dos 10 bosses', ascii_(it))
                for x in lista:
                    a = ascii_(x).strip()
                    regra = ''
                    for pad, r in regras:
                        mm = re.match(pad, a)
                        if mm and r:
                            regra = r.format(*[g.replace(' ', '') for g in mm.groups()])
                            break
                    mm = re.match(r'chegar ao andar (\d+)', a)
                    if mm:
                        regra = 'andar_maximo >= ' + mm.group(1)
                    mm = re.match(r'(\d+) paginas de lore', a)
                    if mm:
                        regra = 'contador(paginas) >= ' + mm.group(1)
                    mm = re.match(r'(\d+) peixes', a)
                    if mm:
                        regra = 'contador(especies_peixe) >= ' + mm.group(1)
                    out.append({'id': slug(grupo + '_' + x)[:60], 'grupo': grupo, 'nome_pt': x[0].upper() + x[1:], 'regra': regra})
    # os 10 bosses de região
    bosses = json.load(open(os.path.join(RAIZ, 'dados', 'bosses.json'), encoding='utf-8'))
    for b in bosses:
        if b['tipo'] == 'boss' and b['andar'] % 10 == 0:
            out.append({'id': 'boss_' + b['id'], 'grupo': 'Bosses', 'nome_pt': 'Vencer: ' + b['nome_pt'], 'regra': 'flag(boss_%s)' % b['id']})
    out = [o for o in out if not o['nome_pt'].lower().startswith('cada um dos')]
    return out


def gerar():
    itens = json.load(open(os.path.join(RAIZ, 'dados', 'itens.json'), encoding='utf-8'))
    bosses = json.load(open(os.path.join(RAIZ, 'dados', 'bosses.json'), encoding='utf-8'))
    ind = {slug(x['nome_pt']): x['id'] for x in itens}
    boss_ind = {slug(b['nome_pt']): b['id'] for b in bosses}
    boss_ind.update({slug(re.sub(r'^(o|a) ', '', b['nome_pt'].lower())): b['id'] for b in bosses})
    pg, px, ti, co = paginas(), peixes(ind), titulos(boss_ind), conquistas()
    for nome, d in (('paginas', pg), ('peixes', px), ('titulos', ti), ('conquistas', co)):
        with open(os.path.join(RAIZ, 'dados', nome + '.json'), 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
    print('ok', len(pg), 'páginas,', len(px), 'peixes,', len(ti), 'títulos (%d com regra),' % sum(1 for t in ti if t['regra']),
          len(co), 'conquistas (%d com regra)' % sum(1 for c in co if c['regra']))


if __name__ == '__main__':
    gerar()
