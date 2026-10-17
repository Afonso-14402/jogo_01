"""Mapas (docs/mapas/*.md) + fichas dos andares (docs/regioes/rXX_*.md, secção 5) -> dados/andares/aNNN.json.

Cada andar fica com: a grelha de células de 10 m (2 letras por célula, legenda em docs/mapas/README.md),
os pontos importantes (com a célula), as zonas (retângulos de células, monstros e recursos), e os dados da ficha
(nível, bioma, monstros, recursos, guardião, peças especiais...). O jogo monta o andar a partir disto.

Uso: python3 ferramentas/dados/andares.py
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, numero, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
# ambiente por região (céu, nevoeiro, densidade, luz ambiente, música)
AMBIENTE = {
    1: ('7fa0c8', 'c8e0d0', 0.008, 0.65, 'floresta'), 2: ('2e222f', '3e3546', 0.03, 0.35, 'cavernas'),
    3: ('374e4a', '547e64', 0.015, 0.55, 'pantano'), 4: ('fbb954', 'f9c22b', 0.006, 0.8, 'deserto'),
    5: ('c7dcd0', 'ffffff', 0.02, 0.75, 'gelo'), 6: ('4d9be6', '30e1b9', 0.015, 0.6, 'oceano'),
    7: ('6e2727', '9e4539', 0.014, 0.5, 'vulcao'), 8: ('45293f', '6b3e75', 0.02, 0.4, 'assombrado'),
    9: ('8fd3ff', 'ffffff', 0.004, 0.9, 'ceu'), 10: ('2e222f', '323353', 0.02, 0.4, 'abismo'),
}
COLUNAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def celula(txt):
    """'H3' -> (7, 2)  (coluna, linha a contar de 0)"""
    m = re.match(r'([A-Z])(\d+)', txt.strip())
    if not m:
        return None
    return COLUNAS.index(m.group(1)), int(m.group(2)) - 1


def retangulo(txt):
    """'B9–E13' -> [1, 8, 4, 12] · 'H3' -> [7, 2, 7, 2] · várias partes separadas por vírgula -> a caixa de todas"""
    pts = [celula(p) for p in re.findall(r'[A-Z]\d+', txt)]
    pts = [p for p in pts if p]
    if not pts:
        return None
    return [min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts)]


def nomes_para_ids(texto, indice):
    """'Escorpião (muitos), Verme da Areia' -> ids. Aceita o nome exato, sem 'de/do/da', ou o início do nome."""
    out = []
    for parte in re.split(r',|·|\(|\)| e |/|;', limpar(texto)):
        s = slug(parte)
        if not s or s in ('muitos', 'poucos', 'so', 'raro', 'noite'):
            continue
        achou = None
        for cand in (s, re.sub(r'_(de|do|da|dos|das)_', '_', s)):
            if cand in indice:
                achou = indice[cand]
                break
        if not achou:
            parecidos = sorted(k for k in indice if k.startswith(s + '_') or s.startswith(k + '_'))
            if parecidos:
                achou = indice[parecidos[0]]
        if achou and achou not in out:
            out.append(achou)
    return out


def ler_fichas(indice_monstros):
    fichas = {}
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r*.md'))):
        regiao = int(os.path.basename(f)[1:3])
        texto = open(f, encoding='utf-8').read()
        for bloco in re.split(r'^### Andar ', texto, flags=re.M)[1:]:
            m = re.match(r'(\d+)\s*[—-]\s*(.+)', bloco.split('\n')[0])
            if not m:
                continue
            n = int(m.group(1))
            kv = {}
            for _, linhas in tabelas(bloco):
                for l in linhas:
                    vals = list(l.values())
                    if len(vals) >= 2:
                        kv[limpar(vals[0])] = vals[1]
            tam = re.findall(r'(\d+)\s*×\s*(\d+)', kv.get('Tamanho / Nível', ''))
            niv = re.search(r'nível\s*(\d+)', kv.get('Tamanho / Nível', ''))
            fichas[n] = {
                'nome_pt': limpar(m.group(2)).replace('👑', '').replace('⭐', '').strip(), 'regiao': regiao,
                'tamanho': [int(tam[0][0]), int(tam[0][1])] if tam else [150, 150],
                'nivel': int(niv.group(1)) if niv else n, 'bioma': limpar(kv.get('Bioma', '')),
                'mecanica': limpar(kv.get('Mecânica especial', '')),
                'monstros': nomes_para_ids(kv.get('Monstros', ''), indice_monstros),
                'monstros_pt': limpar(kv.get('Monstros', '')), 'recursos_pt': limpar(kv.get('Recursos', '')),
                'npcs_pt': limpar(kv.get('NPCs', '')),
                'guardiao': (nomes_para_ids(kv.get('Guardião', ''), indice_monstros) or [None])[0],
                'segredo': limpar(kv.get('Segredo', '')), 'puzzle': limpar(kv.get('Puzzle', '')),
                'pecas_especiais': [slug(p) for p in limpar(kv.get('Peças especiais', '')).split(',') if p.strip()],
                'desafios': [limpar(d) for d in kv.get('Desafios', '').split('·') if d.strip()],
            }
    return fichas


def ler_mapas():
    mapas = {}
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'mapas', 'r*.md'))):
        texto = open(f, encoding='utf-8').read()
        for bloco in re.split(r'^## Andar ', texto, flags=re.M)[1:]:
            m = re.match(r'(\d+)', bloco)
            if not m:
                continue
            n = int(m.group(1))
            g = re.search(r'```\n(.*?)```', bloco, re.S)
            grelha = []
            if g:
                linhas = g.group(1).split('\n')
                for l in linhas[1:]:
                    mm = re.match(r'\s*(\d+)\s\s?(.*)$', l)
                    if mm:
                        corpo = mm.group(2)
                        grelha.append([corpo[i:i + 2] for i in range(0, len(corpo) - 1, 2)])
            largura = max((len(r) for r in grelha), default=0)
            grelha = [r + ['TT'] * (largura - len(r)) for r in grelha]
            pontos, zonas = [], []
            for titulo, linhas in tabelas(bloco):
                for l in linhas:
                    if 'Marca' in l and 'Onde' in l:
                        for onde in re.findall(r'[A-Z]\d+', l['Onde']):
                            c = celula(onde)
                            pontos.append({'marca': limpar(l['Marca']), 'celula': onde, 'x': c[0], 'y': c[1],
                                           'texto': limpar(l.get('O que é', ''))})
                    elif 'Zona' in l and 'Células' in l:
                        zonas.append({'nome': limpar(l['Zona']), 'rect': retangulo(l['Células']),
                                      'monstros_pt': limpar(l.get('Monstros', '')), 'recursos_pt': limpar(l.get('Recursos', ''))})
            caminho = re.search(r'\*\*Caminho principal:\*\*(.*)', bloco)
            notas = re.search(r'\*\*Notas para construir:\*\*(.*)', bloco)
            mapas[n] = {'grelha': grelha, 'pontos': pontos, 'zonas': zonas,
                        'caminho_pt': limpar(caminho.group(1)) if caminho else '',
                        'notas_pt': limpar(notas.group(1)) if notas else ''}
    return mapas


def gerar():
    monstros = json.load(open(os.path.join(RAIZ, 'dados', 'monstros.json'), encoding='utf-8'))
    bosses = json.load(open(os.path.join(RAIZ, 'dados', 'bosses.json'), encoding='utf-8'))
    indice = {}
    for mo in monstros + bosses:
        indice[slug(mo['nome_pt'])] = mo['id']
        indice[re.sub(r'_(de|do|da|dos|das)_', '_', slug(mo['nome_pt']))] = mo['id']
    fichas, mapas = ler_fichas(indice), ler_mapas()
    boss_andar = {b['andar']: b['id'] for b in bosses}
    pasta = os.path.join(RAIZ, 'dados', 'andares')
    os.makedirs(pasta, exist_ok=True)
    sem_mapa = []
    for n in range(1, 101):
        fi = fichas.get(n, {'nome_pt': f'Andar {n}', 'regiao': (n - 1) // 10 + 1, 'tamanho': [150, 150], 'nivel': n,
                            'monstros': [], 'guardiao': None, 'pecas_especiais': []})
        ma = mapas.get(n)
        if not ma or not ma['grelha']:
            sem_mapa.append(n)
            ma = {'grelha': [], 'pontos': [], 'zonas': []}
        for z in ma['zonas']:
            z['monstros'] = nomes_para_ids(z.get('monstros_pt', ''), indice)
        ceu, nev, dens, luz, mus = AMBIENTE[fi['regiao']]
        andar = {'numero': n, 'nome': f'ANDAR_{n}_NOME', **fi,
                 'boss': boss_andar.get(n), 'celula_m': 10,
                 'ambiente': {'ceu': '#' + ceu, 'nevoeiro': '#' + nev, 'densidade_nevoeiro': dens, 'luz_ambiente': luz,
                              'musica': f'{mus}_{(n - 1) % 10 // 3 + 1}'},
                 **ma}
        with open(os.path.join(pasta, f'a{n:03d}.json'), 'w', encoding='utf-8') as f:
            json.dump(andar, f, ensure_ascii=False, indent=1)
    print('ok 100 andares;', len(fichas), 'fichas;', 100 - len(sem_mapa), 'com mapa; sem mapa:', sem_mapa[:20])


if __name__ == '__main__':
    gerar()
