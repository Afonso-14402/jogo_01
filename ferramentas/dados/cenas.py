"""As cenas da história (docs/guiao/cap01_floresta.md … cap10_abismo.md e finais.md) -> dados/cenas.json.

Cada cena fica assim:
  {"id": "cena_c2_01_mina", "capitulo": 2, "titulo_pt": "A Boca da Mina", "quando_pt": "...",
   "gatilho": {"tipo": "andar", "andar": 11, "zona": "..."} ,   tipo: andar · vencer · cidade · falar · interior · manual
   "cond": "...",                                               condição extra (ver scripts/sistemas/condicoes.gd)
   "falas": [...]}                                              como em ferramentas/dados/dialogos.py, mais:
     {"quem": "Sistema", "texto": "..."}                          as linhas `[Sistema] …`
     {"efeito": "...", "missao_aceitar": "H_06", "missao_concluir": "H_05", "missao_passo": "H_06",
      "amizade": 30, "npc": "kai", "flags": [...], "titulo": "...", "itens": [...], "sistema": [...], "capitulo_pt": "..."}

Uso: python3 ferramentas/dados/cenas.py
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, ascii_
from dialogos import guiao

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')


def _json(nome):
    d = json.load(open(os.path.join(RAIZ, 'dados', nome), encoding='utf-8'))
    return list(d.values()) if isinstance(d, dict) else d


NPCS = _json('npcs.json') + _json('npcs_povoacoes.json')
MONSTROS = _json('monstros.json')
BOSSES = _json('bosses.json')
ITENS = _json('itens.json')


def norm(t):
    return ascii_(t or '').lower().replace('-', ' ').strip()


def npc_id(nome):
    """O id do NPC pelo nome ("Velho Fausto", "Kai", "Hilda")."""
    n = norm(re.sub(r'^(o|a|os|as)\s+', '', nome.strip(), flags=re.I))
    for x in NPCS:
        if norm(x['nome_pt']) == n:
            return x['id']
    for x in NPCS:
        nx = norm(x['nome_pt'])
        if nx.startswith(n + ' ') or nx.endswith(' ' + n) or n.endswith(' ' + nx):
            return x['id']
    return ''


def monstro_id(nome):
    n = norm(re.sub(r'^(o|a)\s+', '', nome.strip(), flags=re.I))
    for lista in (BOSSES, MONSTROS):
        for x in lista:
            if norm(x.get('nome_pt', '')) == n:
                return x['id']
    for lista in (BOSSES, MONSTROS):
        for x in lista:
            if norm(x.get('nome_pt', '')).startswith(n):
                return x['id']
    return ''


def item_id(nome):
    n = norm(nome)
    for x in ITENS:
        if norm(x.get('nome_pt', '')) == n:
            return x['id']
    return ''


RE_ANDAR = re.compile(r'andar (\d+)')


def gatilho(quando):
    """O que faz a cena começar (o texto do campo "Quando") -> {tipo, ...} e uma condição extra."""
    q = limpar(quando)
    ql = q.lower()
    cond = []
    if 'noite' in ql:
        cond.append('(hora >= 21 || hora < 5)')
    for c in re.findall(r'`([^`]+)`', q):
        if re.search(r'[<>=]', c):
            cond.append(c.strip())
    g = {'tipo': 'manual'}
    m = re.match(r'^vencer (?:o |a )?(.+?)(?: \(andar \d+\))?$', q)
    if m and ' e ' not in m.group(1):
        mid = monstro_id(m.group(1))
        if mid:
            g = {'tipo': 'vencer', 'monstro': mid}
    elif ql.startswith('voltar a ascendia'):
        g = {'tipo': 'cidade'}
        m = re.search(r'depois d[oa] (.+?)(?:[;(]|$)', q)
        if m:
            mid = monstro_id(m.group(1).strip())
            if mid:
                cond.append('boss_derrotado(%s)' % mid)
    elif ql.startswith(('falar com', 'entregar')):
        m = re.search(r'(?:falar com|ao|à) ((?:o |a )?[A-ZÁÉÍÓÚ][\w\-]*(?: [A-ZÁÉÍÓÚ][\w\-]*)*)', q)
        nid = npc_id(m.group(1)) if m else ''
        if nid:
            g = {'tipo': 'falar', 'npc': nid}
            h = re.search(r'(H_\d+)', q)
            if h:
                cond.append('missao(%s) == %s' % (h.group(1), 'pronta' if 'pronta' in ql else 'ativa'))
    elif re.match(r'^(entrar|chegar|subir|1\.ª noite)', ql) and RE_ANDAR.search(ql):
        g = {'tipo': 'andar', 'andar': int(RE_ANDAR.search(ql).group(1))}
        m = re.search(r"(?:no|na|em|ao|à|n')\s*(?:\*\*)?([A-ZÁÉÍÓÚ][^(*]+?)(?:\*\*)?\s*\(andar", q)
        if m:
            g['zona'] = m.group(1).strip()
        elif not re.search(r'(primeira vez no|entrar no) andar \d+$', ql):
            m = re.search(r"(?:no|na|ao|à|n')\s+(?:\*\*)?([A-ZÁÉÍÓÚ][^(*]+?)(?:\*\*)? do andar", q)
            if m:
                g['zona'] = m.group(1).strip()
    elif ql.startswith('entrar n'):
        m = re.search(r"entrar n[oa]s? (.+?)(?: à noite| depois|$)", q)
        if m and 'estalagem' in m.group(1).lower():
            g = {'tipo': 'interior', 'interior': 'estalagem'}
            m2 = re.search(r'depois d[oa] (.+)$', q)
            if m2 and monstro_id(m2.group(1)):
                cond.append('boss_derrotado(%s)' % monstro_id(m2.group(1)))
    return g, ' && '.join(cond)


def efeito(f, ultimo):
    """Lê o texto de um ⚙ e junta o que o jogo sabe fazer."""
    t = f['efeito']
    for h in re.findall(r'Missão \*?\*?(H_\d+)[^.·]*?\*?\*? ativa', t):
        f['missao_aceitar'] = h
    for h in re.findall(r'Missão \*?\*?(H_\d+)\*?\*? concluída', t):
        f['missao_concluir'] = h
    m = re.search(r'(H_\d+): `?\[Sistema\]', t)
    if m:
        f['missao_passo'] = m.group(1)
    m = re.search(r'([+−-]\d+) amizade com (?:o |a )?([A-ZÁÉÍÓÚ][\w\-]*(?: [A-ZÁÉÍÓÚ][\w\-]*)*)', t)
    if m and not m.group(2).lower().startswith('todos') and npc_id(m.group(2)):
        f['amizade'] = int(m.group(1).replace('−', '-'))
        f['npc'] = npc_id(m.group(2))
    elif 'amizade' in f and ultimo and 'todos' not in t:
        f['npc'] = ultimo
    flags = re.findall(r'flag `([\w]+)`', t)
    if flags:
        f['flags'] = flags
    m = re.search(r'Título \*([^*]+)\*', t)
    if m:
        f['titulo'] = m.group(1)
    sis = [x.strip() for x in re.findall(r'\[Sistema\] (.+?)(?=\s*·|\s*\[Sistema\]|$)', t)]
    for s in sis:
        m = re.match(r'Obtiveste: (.+?)\.?$', s)
        if m and item_id(m.group(1)):
            f.setdefault('itens', []).append(item_id(m.group(1)))
        m = re.match(r'Capítulo (\d+): (.+?)\.?$', s)
        if m:
            f['capitulo_pt'] = 'Capítulo %s: %s' % m.groups()
    if sis:
        f['sistema'] = sis
    return f


def sistema_para_fala(corpo):
    """As linhas `[Sistema] …` (fora dos ⚙) passam a falas do Sistema, para o guião as ler pela ordem."""
    out = []
    for l in corpo.split('\n'):
        s = l.strip()
        if '`[Sistema]' in s and not s.lstrip('- ').startswith('⚙'):
            for txt in re.findall(r'`\[Sistema\] ([^`]+)`', s):
                out.append('- **Sistema**: "%s"' % txt.replace('"', "'"))
            continue
        out.append(l)
    return '\n'.join(out)


def cenas_de(caminho, capitulo):
    texto = open(caminho, encoding='utf-8').read()
    r = []
    for bloco in re.split(r'^#{2,3} ', texto, flags=re.M)[1:]:
        titulo, _, corpo = bloco.partition('\n')
        m = re.match(r'^(C\d+-\d+\w?|F[\w-]*|E[\w-]*)\s*[—-]\s*(.+)$', titulo.strip())
        if not m:
            continue
        ficha = {}
        for _, ls in tabelas(corpo):
            for l in ls:
                vals = [limpar(v) for v in l.values()]
                if len(vals) >= 2:
                    ficha[vals[0]] = vals[1]
            break
        cid = ficha.get('ID', '').strip('`')
        if not cid:
            continue
        g, cond = gatilho(ficha.get('Quando', ''))
        falas = guiao(sistema_para_fala(corpo))
        ultimo = ''
        for f in falas:
            if 'quem' in f and f['quem'] != 'Sistema':
                ultimo = npc_id(f['quem']) or ultimo
            if 'efeito' in f:
                efeito(f, ultimo)
        r.append({'id': cid, 'codigo': m.group(1), 'capitulo': capitulo, 'titulo_pt': m.group(2).strip(),
                  'quando_pt': limpar(ficha.get('Quando', '')), 'onde_pt': limpar(ficha.get('Onde', '')),
                  'gatilho': g, 'cond': cond, 'falas': falas})
    return r


def gerar():
    todas = []
    for c in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'guiao', 'cap*.md'))):
        todas += cenas_de(c, int(re.search(r'cap(\d+)', c).group(1)))
    todas += cenas_de(os.path.join(RAIZ, 'docs', 'guiao', 'finais.md'), 11)
    return todas


if __name__ == '__main__':
    cs = gerar()
    with open(os.path.join(RAIZ, 'dados', 'cenas.json'), 'w', encoding='utf-8') as f:
        json.dump({c['id']: c for c in cs}, f, ensure_ascii=False, indent=1)
    tipos = {}
    for c in cs:
        tipos[c['gatilho']['tipo']] = tipos.get(c['gatilho']['tipo'], 0) + 1
    print('cenas:', len(cs), tipos)
