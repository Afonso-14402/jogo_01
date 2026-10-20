"""docs/NPCS.md + docs/dialogos/<npc>.md -> dados/npcs.json e dados/dialogos/<npc>.json (docs/dialogos/README.md).

Cada fala de um "guião" (primeira conversa, cenas de coração, missões, perguntar sobre a torre) fica assim:
  {"quem": "Lyra", "emocao": "feliz", "texto": "..."}       fala (emoção: normal, feliz, zangado, triste)
  {"acao": "..."}  /  {"camara": "..."}                       🎬 / 🎥 (texto de cena)
  {"escolhas": ["Lamento muito.", ...]}                      ▶ escolhas do jogador
  {"ramo": 0, ...}                                            esta fala só aparece depois da escolha 0
  {"efeito": "...", "amizade": 30}                           ⚙ efeito (o texto e o que o jogo já sabe fazer)
As falas do dia a dia, rumores, estados, presentes e bosses ficam em tabelas com id, condição, emoção e texto.

Uso: python3 ferramentas/dados/dialogos.py
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
EMOCOES = {'normal': 'normal', 'feliz': 'feliz', 'zangado': 'zangado', 'zangada': 'zangado', 'triste': 'triste',
           'surpresa': 'feliz', 'surpreso': 'feliz', 'surpresa!': 'feliz', 'nervoso': 'triste', 'nervosa': 'triste',
           'seria': 'normal', 'serio': 'normal', 'a ler': 'normal', 'a chorar': 'triste', 'orgulhoso': 'feliz',
           'orgulhosa': 'feliz', 'envergonhado': 'triste', 'envergonhada': 'triste', 'pensativo': 'normal', 'pensativa': 'normal'}
NPCS = ['lyra', 'gorvan', 'brom', 'selene', 'tobias', 'marta', 'kai', 'mia', 'celia', 'fausto', 'rook', 'freya', 'pip',
        'hana', 'zed', 'oriel', 'lucien', 'gizmo', 'elva', 'aldric']
ESTACOES = {'primavera': 'primavera', 'verao': 'verao', 'outono': 'outono', 'inverno': 'inverno'}


def emocao(t):
    a = ascii_(t or '').strip()
    for parte in [a] + [p.strip() for p in re.split(r'[,;]', a)]:
        if parte in EMOCOES:
            return EMOCOES[parte]
    return 'normal'


def texto_fala(t):
    t = limpar(t).strip()
    m = re.match(r'^"(.*)"$', t, re.S)
    return m.group(1) if m else t.strip('"')


RE_FALA = re.compile(r'^\*\*(?P<quem>[^*]+?)\*\*\s*(?:\*\((?P<emo>[^)]*)\)\*)?\s*:\s*(?P<txt>.+)$')
RE_QUEM = re.compile(r'^(?:(?P<quem>[A-ZÀ-Ý][\w\-ºª{}/ ]{0,30}?)\s*)?(?:\*\((?P<emo>[^)]*)\)\*)?\s*:?$')


def partir_fala(quem, emo, txt):
    """Uma fala do guião com notas pelo meio ('"Olá." 🎬 levanta-se. *(feliz)* "Adeus."', ou 'Lyra *(baixinho)*: "…"')
    -> várias falas e ações, para o jogador nunca ver as notas de realização nem as aspas soltas."""
    t = limpar(txt).strip()
    falas = []
    if t.count('"') < 2 or (t.startswith('"') and t.endswith('"') and t.count('"') == 2 and '🎬' not in t):
        if '🎬' in t:   # fala sem aspas e uma ação no fim
            fala, _, acao = t.partition('🎬')
            falas.append({'quem': quem, 'emocao': emo, 'texto': _sem_notas(fala.strip().strip('"'))})
            falas.append({'acao': _acao(acao)})
            return [f for f in falas if f.get('texto', f.get('acao'))]
        return [{'quem': quem, 'emocao': emo, 'texto': _sem_notas(texto_fala(txt))}]
    pos = 0
    for m in re.finditer(r'"([^"]*)"', t):
        _entre(t[pos:m.start()], falas)
        q, e = quem, emo
        for f in reversed(falas):   # a nota antes pode ter mudado quem fala ou a emoção
            if '_quem' in f:
                q, e = f['_quem'] or quem, f['_emo'] or emo
                break
        quem, emo = q, e
        if m.group(1).strip():
            falas.append({'quem': quem, 'emocao': emo, 'texto': _sem_notas(m.group(1).strip())})
        pos = m.end()
    _entre(t[pos:], falas)
    return [f for f in falas if '_quem' not in f]


def _sem_notas(t):
    return re.sub(r'\*\(([^)]*)\)\*', r'(\1)', t).replace('*', '').strip()


def _acao(t):
    t = re.sub(r'\*\(([^)]*)\)\*', r'(\1)', t).replace('🎬', '').replace('*', '').strip(' .:') + '.'
    return t[0].upper() + t[1:]


def _entre(g, falas):
    """O que fica entre duas falas entre aspas: uma ação (🎬 …), a emoção nova (*(feliz)*) ou quem fala a seguir (Lyra:)."""
    g = g.strip()
    if not g:
        return
    quem = re.search(r'(?:^|[.!?…]\s+|🎬\s*)((?:[A-ZÀ-Ý][\w\-ºª ]{0,30}?\s*)?(?:\*\([^)]*\)\*)?\s*:)\s*$', g)
    troca = None
    if quem and quem.group(1).strip(' :'):
        troca = RE_QUEM.match(quem.group(1).strip())
        g = g[:quem.start(1)].strip()
    else:   # a emoção nova no fim da nota: "🎬 Pausa. *(triste)*"
        fim = re.search(r'\*\((?P<emo>[^)]*)\)\*\s*$', g)
        if fim:
            troca = fim
            g = g[:fim.start()].strip()
    if g.replace('🎬', '').strip(' .'):
        falas.append({'acao': _acao(g)})
    if troca:
        q = troca.groupdict().get('quem')
        falas.append({'_quem': limpar(q).strip() if q else None, '_emo': emocao(troca.group('emo')) if troca.group('emo') else None})


def linha_guiao(l):
    """Uma linha de guião -> lista de falas (uma linha pode ter fala + ⚙ efeito)."""
    s = l.strip()
    s = re.sub(r'^[-*]\s+', '', s)
    out = []
    ramo = None
    m = re.match(r'^\*\((?P<r>[^)]*)\)\*\s*(?P<resto>.*)$', s)
    if m and m.group('resto').startswith('**'):
        ramo, s = m.group('r'), m.group('resto')
    m = re.match(r'^\((?P<r>[^)]*)\)\s*(?P<resto>\*\*.*)$', s)   # "(de dia, na Guilda) **Lyra** ..."
    if m:
        s = m.group('resto')
    efeito = None
    if '⚙' in s and not s.startswith('⚙'):
        s, efeito = s.split('⚙', 1)
        s = s.strip()
    if s.startswith('▶'):
        opcoes = [limpar(re.sub(r'→.*', '', o)).strip(' "*()').strip('"') for o in s.split('▶') if o.strip()]
        out.append({'escolhas': [o for o in opcoes if o]})
    elif s.startswith('🎬'):
        out.append({'acao': limpar(s[1:]).strip()})
    elif s.startswith('🎥'):
        out.append({'camara': limpar(s[1:]).strip()})
    elif s.startswith('⚙'):
        efeito = s[1:]
    else:
        m = RE_FALA.match(s)
        if m:
            for f in partir_fala(limpar(m.group('quem')), emocao(m.group('emo')), m.group('txt')):
                if ramo is not None:
                    f['ramo_txt'] = ramo
                out.append(f)
    if efeito:
        e = {'efeito': limpar(efeito).strip()}
        a = re.search(r'([+−-]\d+)(?:\s*amizade)?', e['efeito'])
        if a and ('amizade' in e['efeito'] or re.fullmatch(r'\s*[+−-]\d+\s*', e['efeito'])):
            e['amizade'] = int(a.group(1).replace('−', '-'))
        if ramo is not None:
            e['ramo_txt'] = ramo
        out.append(e)
    return out


def guiao(texto):
    """Linhas soltas de um guião -> lista de falas, com os ramos ligados às escolhas (pela ordem)."""
    falas = []
    for l in texto.split('\n'):
        if l.strip().startswith(('-', '▶', '🎬', '🎥', '⚙', '*(')) or RE_FALA.match(l.strip()):
            falas.extend(linha_guiao(l))
    # vários ▶ seguidos (um por linha) são um só bloco de escolhas
    juntas = []
    for f in falas:
        if 'escolhas' in f and juntas and 'escolhas' in juntas[-1]:
            juntas[-1]['escolhas'].extend(f['escolhas'])
        else:
            juntas.append(f)
    falas = juntas
    # ligar ramos às escolhas: depois de um bloco de escolhas, os ramos diferentes são 0, 1, 2… pela ordem
    ultimo = None
    vistos = []
    for f in falas:
        if 'escolhas' in f:
            ultimo, vistos = f, []
        elif 'ramo_txt' in f and ultimo is not None:
            r = f.pop('ramo_txt')
            if r not in vistos:
                vistos.append(r)
            f['ramo'] = min(vistos.index(r), len(ultimo['escolhas']) - 1)
        else:
            f.pop('ramo_txt', None)
    return falas


def seccoes(texto, nivel='## '):
    partes = re.split(r'^' + re.escape(nivel) + r'(?:\d+(?:\.\d+)?\.?\s*)?', texto, flags=re.M)
    out = {}
    for p in partes[1:]:
        titulo, _, corpo = p.partition('\n')
        out[slug(titulo)] = corpo
    return out


def tabela_falas(corpo, npc):
    out = []
    for _, linhas in tabelas(corpo):
        for l in linhas:
            fid = limpar(l.get('ID', '')).strip('`')
            txt = l.get('Fala') or l.get('Rumor') or ''
            if not fid or not txt:
                continue
            cond = limpar(l.get('Condição', '—')).strip('`')
            out.append({'id': fid, 'cond': '' if cond in ('—', '-', '') else cond,
                        'emocao': emocao(l.get('Emoção', 'normal')), 'texto': texto_fala(txt)})
    return out


def npc_dialogo(npc, texto, itens_ind):
    s = seccoes(texto)
    d = {'id': npc}
    for k, corpo in s.items():
        if k.startswith('ficha_de_voz'):
            d['voz'] = {limpar(l.get('_0', '')): limpar(l.get('_1', '')) for _, ls in tabelas(corpo) for l in ls}
        elif k.startswith('primeira_conversa'):
            d['primeira'] = guiao(corpo)
        elif k.startswith('falas_do_dia'):
            todas = tabela_falas(corpo, npc)
            d['dia'] = [f for f in todas if '_curta_' not in f['id']]
            d['curtas'] = [f for f in todas if '_curta_' in f['id']]
        elif k.startswith('perguntar_sobre'):
            sub = seccoes(corpo, '### ')
            p = {}
            for sk, sc in sub.items():
                if 'torre' in sk:
                    p['torre'] = guiao(sc)
                elif 'andar' in sk:
                    p['andar'] = {re.match(r'\d+', limpar(l.get('Região', '0'))).group(0): texto_fala(l.get('Fala', ''))
                                  for _, ls in tabelas(sc) for l in ls if re.match(r'\d+', limpar(l.get('Região', '')))}
                elif 'rumor' in sk:
                    p['rumores'] = tabela_falas(sc, npc)
                else:
                    p['vida'] = {re.sub(r'\D', '', limpar(l.get('Corações', '0'))) or '0': texto_fala(l.get('Fala', ''))
                                 for _, ls in tabelas(sc) for l in ls if 'Corações' in l}
            d['perguntar'] = p
        elif k.startswith('presentes'):
            reac, esp = {}, {}
            for _, ls in tabelas(corpo):
                for l in ls:
                    if 'Reação' in l:
                        chave = slug(l['Reação']).replace('nao_gosta', 'nao_gosta')
                        reac[chave] = [texto_fala(x) for x in re.findall(r'"[^"]+"', l.get('Falas (escolhe uma)', l.get('Falas', '')))]
                    elif 'Item' in l:
                        nome = limpar(l['Item'])
                        iid = itens_ind.get(slug(nome)) or slug(nome)
                        esp[iid] = texto_fala(l.get('Fala', ''))
            d['presentes'] = {'reacoes': reac, 'especiais': esp}
        elif k.startswith('aniversario'):
            an = {}
            for l in corpo.split('\n'):
                m = re.match(r'-\s*(Sem presente|Com presente que adora|Com outro presente)\s*:\s*(.*)', l.strip())
                if m:
                    f = linha_guiao(m.group(2))
                    an[{'Sem presente': 'sem', 'Com presente que adora': 'adora', 'Com outro presente': 'outro'}[m.group(1)]] = f[0] if f else {}
            fest = {}
            for _, ls in tabelas(corpo):
                for l in ls:
                    if 'Festival' in l:
                        m = re.match(r'(F_\d+)', limpar(l['Festival']))
                        if m and '(' not in l['Festival']:
                            q = re.findall(r'"[^"]+"', l.get('Fala', ''))
                            fest[m.group(1)] = texto_fala(q[0]) if q else limpar(l.get('Fala', ''))
            d['aniversario'] = an
            d['festivais'] = fest
        elif k.startswith('depois_dos_bosses'):
            b = {}
            for _, ls in tabelas(corpo):
                for l in ls:
                    fid = limpar(l.get('ID', '')).strip('`')
                    if fid.startswith(npc + '_boss_'):
                        b[fid[len(npc) + 6:]] = texto_fala(l.get('Fala', ''))
            d['bosses'] = b
        elif k.startswith('cenas_de_coracao'):
            cenas = []
            for bloco in re.split(r'^### ', corpo, flags=re.M)[1:]:
                t, _, resto = bloco.partition('\n')
                m = re.search(r'(\d+)', t)
                kv = {limpar(l.get('_0', '')): limpar(l.get('_1', '')) for _, ls in tabelas(resto) for l in ls}
                quando = kv.get('Quando', '')
                cond = ' && '.join(c.strip('` ') for c in re.findall(r'`[^`]+`', quando))
                cenas.append({'id': kv.get('ID', '').strip('`') or f'cena_{npc}_{m.group(1) if m else 0}',
                              'coracoes': int(m.group(1)) if m else 0, 'titulo': limpar(re.sub(r'^[^—]*—\s*', '', t)),
                              'quando_pt': quando, 'cond': cond, 'onde_pt': kv.get('Onde', ''), 'musica': kv.get('Música', ''),
                              'falas': guiao(resto)})
            d['cenas'] = cenas
        elif k.startswith('missoes'):
            ms = []
            for bloco in re.split(r'^### ', corpo, flags=re.M)[1:]:
                t, _, resto = bloco.partition('\n')
                m = re.match(r'(\S+)\s*—\s*([^(]+)', t)
                partes, atual = {}, None
                for l in resto.split('\n'):
                    mm = re.match(r'^-\s*\*\*(Pedir|Durante|Entregar|Passos)\*\*[^—]*—?\s*(.*)$', l.strip())
                    if mm:
                        atual = slug(mm.group(1))
                        partes[atual] = []
                        if mm.group(2):
                            partes[atual].extend(linha_guiao(mm.group(2)))
                    elif atual and l.strip():
                        partes[atual].extend(linha_guiao(l))
                ms.append({'id': m.group(1) if m else slug(t), 'titulo': limpar(m.group(2)).strip() if m else t,
                           'cabecalho_pt': limpar(t), 'partes': partes})
            d['missoes'] = ms
        elif k.startswith('estados'):
            d['estados'] = tabela_falas(corpo, npc)
    return d


def perfis(itens, nomes_ind):
    texto = open(os.path.join(RAIZ, 'docs', 'NPCS.md'), encoding='utf-8').read()
    sec = texto.split('## 3. Os 20 NPCs de Ascendia', 1)[1].split('\n## 4.', 1)[0]
    out = []
    for bloco in re.split(r'^### ', sec, flags=re.M)[1:]:
        t, _, resto = bloco.partition('\n')
        m = re.match(r'[\d.]+\s+(.+?)\s+—\s+(.+)', t)
        nome = m.group(1)
        nid = next((n for n in NPCS if n in slug(nome)), slug(nome))
        kv = {limpar(l.get('_0', '')): l.get('_1', '') for _, ls in tabelas(resto) for l in ls}
        an = re.search(r'(Primavera|Verão|Outono|Inverno),\s*dia\s*(\d+)', kv.get('Aniversário', ''))
        gostos = kv.get('Adora', '')
        adora_txt, _, resto_g = gostos.partition('·')
        gosta = re.search(r'\*\*Gosta\*\*\s*(?:de)?\s*([^·]*)', gostos)
        detesta = re.search(r'\*\*Detesta\*\*\s*([^·]*)', gostos)
        rotina = []
        for lugar, de, ate in re.findall(r'([^·(]+?)\s*\((\d+):00[–-](\d+):00\)', kv.get('Onde está', '')):
            rotina.append({'local': slug(lugar), 'local_pt': limpar(lugar).strip(), 'de': int(de), 'ate': int(ate)})
        out.append({
            'id': nid, 'nome_pt': nome, 'titulo_pt': limpar(m.group(2)),
            'retrato': f'res://arte/retratos/{nid}_', 'sprite': f'res://arte/npcs/{nid}',
            'onde_pt': limpar(kv.get('Onde está', '')), 'rotina': rotina,
            'aniversario': {'estacao': ESTACOES.get(ascii_(an.group(1)), 'primavera'), 'dia': int(an.group(2))} if an else None,
            'servicos_pt': limpar(kv.get('Serviços', '')),
            'adora': [i for i in (nomes_ind.get(slug(x.strip())) for x in limpar(adora_txt).split(',')) if i],
            'gosta_pt': limpar(gosta.group(1)).strip() if gosta else '', 'detesta_pt': limpar(detesta.group(1)).strip() if detesta else '',
            'gosta': categorias(gosta.group(1) if gosta else '', itens, nomes_ind),
            'detesta': categorias(detesta.group(1) if detesta else '', itens, nomes_ind),
            'recompensa_10_pt': limpar(kv.get('Recompensa (10 ❤️)', '')),
        })
    return out


def categorias(texto, itens, nomes_ind):
    """'flores, doces' -> ids dos itens dessas categorias (ou o item com esse nome)."""
    ids = set()
    for parte in limpar(texto).split(','):
        p = ascii_(parte.strip())
        if not p:
            continue
        if slug(p) in nomes_ind:
            ids.add(nomes_ind[slug(p)])
            continue
        for it in itens:
            n = ascii_(it['nome_pt'])
            cat = it['categoria']
            if cat in ('arma', 'missao', 'armadura', 'ferramenta'):
                continue
            if (('flor' in p and re.search(r'\b(flor|rosa|lirio|lotus|tulipa|petala|girassol)\b', n)) or
                    ('doce' in p and cat in ('comida', 'consumivel') and re.search(r'mel|bolo|torta|tarte|panqueca|chocolate|doce|tamara|morango', n)) or
                    ('monstro' in p and cat == 'material' and re.search(r'\b(gel|presa|chifre|ferrao|asa|garra|escama|osso|olho|pelo|pele)\b', n)) or
                    ('lingote' in p and n.startswith('lingote')) or ('minerio' in p and n.startswith('minerio')) or
                    ('carne' in p and 'carne' in n) or ('peixe' in p and cat == 'peixe') or
                    ('gema' in p and re.search(r'rubi|safira|topazio|esmeralda|diamante|onix', n)) or
                    ('livro' in p and 'livro' in n) or ('comida' in p and cat == 'comida') or
                    ('cogumelo' in p and 'cogumelo' in n) or ('erva' in p and 'erva' in n) or
                    ('madeira' in p and re.search(r'madeira|carvalho|pinheiro', n)) or ('cha' == p and 'cha' in n.split())):
                ids.add(it['id'])
    return sorted(ids)


def gerar():
    itens = json.load(open(os.path.join(RAIZ, 'dados', 'itens.json'), encoding='utf-8'))
    armas = json.load(open(os.path.join(RAIZ, 'dados', 'armas.json'), encoding='utf-8'))
    ind = {}
    for x in itens + armas:
        ind.setdefault(slug(x['nome_pt']), x['id'])
    npcs = perfis(itens, ind)
    with open(os.path.join(RAIZ, 'dados', 'npcs.json'), 'w', encoding='utf-8') as f:
        json.dump(npcs, f, ensure_ascii=False, indent=1)
    pasta = os.path.join(RAIZ, 'dados', 'dialogos')
    os.makedirs(pasta, exist_ok=True)
    total = {}
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'dialogos', '*.md'))):
        npc = os.path.basename(f)[:-3]
        if npc not in NPCS:
            continue
        d = npc_dialogo(npc, open(f, encoding='utf-8').read(), ind)
        with open(os.path.join(pasta, npc + '.json'), 'w', encoding='utf-8') as fo:
            json.dump(d, fo, ensure_ascii=False, indent=1)
        total[npc] = (len(d.get('dia', [])), len(d.get('cenas', [])), len(d.get('missoes', [])))
    print('ok', len(npcs), 'NPCs;', 'diálogos (falas, cenas, missões):', total)


if __name__ == '__main__':
    gerar()
