"""As masmorras escondidas (docs/regioes/rNN_*.md, secção 9; armas: docs/ARMAS.md, secção 6) -> dados/masmorras.json.

Cada masmorra: região, andar, nome, entrada, 3 salas (com o tipo de sala que o jogo monta: combate, armadilhas ou
puzzle, pelo que o texto descreve), o boss extra (com fases e ataques tirados da descrição, no formato de
dados/bosses.json) e a recompensa (arma secreta, baú de ouro, página de lore extra).

Uso: python3 ferramentas/dados/masmorras.py
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
PASTAS = {1: 'r01_floresta', 2: 'r02_cavernas', 3: 'r03_pantano', 4: 'r04_deserto', 5: 'r05_gelo', 6: 'r06_oceano',
          7: 'r07_vulcao', 8: 'r08_reino_assombrado', 9: 'r09_ceu', 10: 'r10_abismo'}

# palavras que dizem o tipo de sala
COMBATE = ['larvas', 'golens', 'guerreiros', 'treants', 'monstros', 'fantasmas dançam', 'guardam']
PUZZLE = ['puzzle', 'rodar', 'espelhos', 'pôr ', 'corrigir', 'verter', 'balança', 'cavidades', 'sombras', 'bloquear',
          'esfera', 'estátuas pequenas', 'mostram o reino', 'asas de metal']


# A mecânica de cada sala (o que o texto de docs/regioes/rNN, secção 9, descreve), pelo nome da sala.
#   linhas      faixas que avisam e ferem (raízes, lâminas, dardos, fogo das escamas, retratos, canhões)
#   ponte       pedras sobre o vazio que caem 1 s depois de as pisares (ou baloiçam / flutuam)
#   agua        a sala enche-se: subir a rampa até à plataforma antes de a água te cobrir
#   pedra       apanhar o ídolo solta uma pedra gigante que rola atrás de ti
#   labirinto   paredes que se mexem
#   vento       rajadas que empurram (abrigos atrás das colunas)
#   ar          sala inundada: o Ar acaba; bolhas enchem-no
#   despertar   monstros parados que acordam quando passas perto
#   espelhos    rodar espelhos para levar a luz (ou a sombra) até ao selo
#   cavidades   pôr a coisa certa em cada sítio (pedras-coração, moldes, código)
#   balanca     equilibrar o peso escrito na porta
#   lore        ver/ler as coisas da sala (espelhos da rainha, estátuas dos Jogadores, o Núcleo)
MECANICAS = {
    'corredor_das_raizes': {'tipo': 'linhas', 'padrao': 'onda', 'visual': 'raiz'},
    'ninho_de_larvas': {'tipo': 'combate', 'filtro': ['larva', 'treant', 'verme'], 'n': 7},
    'camara_do_ambar': {'tipo': 'espelhos', 'n': 3, 'cor': 'f79617'},
    'ponte_que_cai': {'tipo': 'ponte', 'cai': 1.0},
    'corredor_das_laminas': {'tipo': 'linhas', 'padrao': 'ritmo', 'visual': 'lamina'},
    'camara_do_ouro': {'tipo': 'despertar', 'filtro': ['golem'], 'n': 4, 'ouro': True},
    'corredor_dos_dardos': {'tipo': 'linhas', 'padrao': 'placas', 'visual': 'dardo'},
    'sala_da_agua_que_sobe': {'tipo': 'agua'},
    'sala_do_idolo': {'tipo': 'pedra'},
    'labirinto_de_costelas': {'tipo': 'labirinto', 'visual': 'osso'},
    'coracao_fossilizado': {'tipo': 'cavidades', 'conjunto': 'coracao'},
    'camara_das_escamas': {'tipo': 'linhas', 'padrao': 'aleatorio', 'visual': 'fogo'},
    'corredor_do_vento_uivante': {'tipo': 'vento', 'abrigos': True},
    'salao_dos_guerreiros_congelados': {'tipo': 'despertar', 'filtro': ['congelad', 'guerreir', 'esquelet', 'cacador'], 'n': 12},
    'espelhos_de_gelo': {'tipo': 'espelhos', 'n': 3, 'cor': '8fd3ff'},
    'corredores_inundados': {'tipo': 'ar'},
    'sala_dos_canhoes': {'tipo': 'linhas', 'padrao': 'canhoes', 'visual': 'bala'},
    'o_cofre': {'tipo': 'balanca'},
    'ponte_de_correntes': {'tipo': 'ponte', 'cai': 0, 'baloica': True},
    'sala_dos_moldes': {'tipo': 'cavidades', 'conjunto': 'moldes'},
    'camara_do_fole': {'tipo': 'vento', 'rajadas': True},
    'corredor_dos_retratos': {'tipo': 'linhas', 'padrao': 'retratos', 'visual': 'olhos'},
    'salao_de_baile_fantasma': {'tipo': 'ritmo'},
    'camara_da_rainha': {'tipo': 'lore', 'conjunto': 'rainha'},
    'corredor_da_gravidade_invertida': {'tipo': 'ponte', 'cai': 0, 'invertido': True},
    'sala_das_sombras': {'tipo': 'espelhos', 'n': 3, 'cor': '45293f', 'sombras': True},
    'camara_das_asas': {'tipo': 'vento', 'rajadas': True, 'lado': True},
    'sala_de_codigo': {'tipo': 'cavidades', 'conjunto': 'codigo'},
    'sala_dos_jogadores': {'tipo': 'lore', 'conjunto': 'jogadores'},
    'o_nucleo': {'tipo': 'lore', 'conjunto': 'nucleo'},
}


def slug(t):
    return re.sub(r'[^a-z0-9]+', '_', ascii_(t).lower()).strip('_')


def tipo_sala(texto):
    t = texto.lower()
    if 'dançar' in t or 'ao ritmo' in t:
        return 'ritmo'
    if any(k in t for k in COMBATE):
        return 'combate'
    if any(k in t for k in PUZZLE):
        return 'puzzle'
    return 'armadilhas'


def armas_secretas():
    texto = open(os.path.join(RAIZ, 'docs', 'ARMAS.md'), encoding='utf-8').read()
    sec = re.search(r'^## 6\. Armas secretas.*?\n(.*?)(?=^## )', texto, re.S | re.M).group(1)
    armas = json.load(open(os.path.join(RAIZ, 'dados', 'armas.json'), encoding='utf-8'))
    armas = armas.values() if isinstance(armas, dict) else armas
    por_nome = {ascii_(a['nome_pt']).lower(): a['id'] for a in armas if a.get('categoria') == 'secreta'}
    out = {}
    for _, ls in tabelas(sec):
        for l in ls:
            nome = limpar(l['Arma']).strip('*')
            out[int(limpar(l['Região']))] = {'arma': por_nome.get(ascii_(nome).lower(), ''), 'arma_pt': nome,
                                              'efeito_pt': limpar(l.get('Efeito', ''))}
    return out


def boss(regiao, andar, texto):
    """'**Larva Ancestral**: verme gigante (64×64) que escava…; cospe ácido (veneno); aos 50% chama larvas'."""
    m = re.match(r'\*\*(.+?)\*\*\s*(?:\(([^)]*)\))?\s*:?\s*(.*)$', texto.strip())
    nome = limpar(m.group(1))
    resto = limpar(m.group(3) or '')
    bid = slug(nome)
    desc, _, golpes = resto.partition(';') if ';' in resto else (resto, '', resto)
    partes = [p.strip(' .') for p in re.split(r';|, e |, ', golpes) if p.strip(' .')]
    fase1, fase2 = [], []
    for p in partes:
        mm = re.match(r'(?:aos|na) (\d+)%\s*(.*)', p)
        if mm or p.startswith('na 2.ª fase'):
            fase2.append(p)
        else:
            fase1.append(p)
    if not fase1:
        fase1 = ['golpe']

    def ataque(p):
        return {'id': slug(p)[:24] or 'golpe', 'nome_pt': p[:1].upper() + p[1:], 'mult': 1.3, 'aviso': 0.7, 'alcance': 2.2,
                'recarga': 2.0, 'texto': p, 'estados': []}
    fases = [{'fase': 1, 'vida': '100–50%', 'ataques': [ataque(p) for p in fase1[:4]]},
             {'fase': 2, 'vida': '50–0%', 'ataques': [ataque(p) for p in (fase1[:2] + fase2)[:4] or fase1[:3]]}]
    return {'id': bid, 'nome': 'BOSS_' + bid.upper(), 'nome_pt': nome, 'andar': andar, 'tipo': 'boss', 'epiteto': 'Boss da masmorra escondida',
            'nivel': andar + 6, 'tamanho_px': 64, 'fraquezas': [], 'resistencias': [], 'imunidades': [],
            'arena': 'sala do boss da masmorra', 'mecanica': resto, 'fases': fases,
            'sprite': 'res://arte/regioes/%s/bosses/%s' % (PASTAS[regiao], bid), 'masmorra': True}


def gerar():
    secretas = armas_secretas()
    masmorras, bosses = [], {}
    for r, pasta in PASTAS.items():
        texto = open(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', pasta + '.md'))[0], encoding='utf-8').read()
        m = re.search(r'^## 9\. Masmorra escondida — (.+?) \((?:pela [^,]+, )?andar (\d+)\)\n(.*?)(?=^---|^## )', texto, re.S | re.M)
        if not m:
            continue
        nome, andar, corpo = m.group(1).strip(), int(m.group(2)), m.group(3)
        ficha = {}
        for _, ls in tabelas(corpo):
            for l in ls:
                v = list(l.values())
                if len(v) >= 2:
                    ficha[limpar(v[0])] = v[1]
        salas = []
        for k in (1, 2, 3):
            t = ficha.get('Sala %d' % k, '')
            mm = re.match(r'\s*\*\*(.+?)\*\*\s*:?\s*(.*)$', t)
            nome_sala = limpar(mm.group(1)) if mm else 'Sala %d' % k
            mec = MECANICAS.get(slug(nome_sala), {'tipo': tipo_sala(t)})
            salas.append({'nome_pt': nome_sala, 'texto_pt': limpar(mm.group(2) if mm else t), 'tipo': mec['tipo'], 'mecanica': mec})
        b = boss(r, andar, ficha.get('Boss extra', '**Guardião**: golpe'))
        bosses[b['id']] = b
        rec = limpar(ficha.get('Recompensa', ''))
        lore = re.search(r'página de lore extra "([^"]+)"', rec)
        masmorras.append({'id': slug(nome), 'regiao': r, 'andar': andar, 'nome_pt': nome,
                          'entrada_pt': limpar(ficha.get('Entrada', '')), 'salas': salas, 'boss': b['id'],
                          'arma': secretas.get(r, {}).get('arma', ''), 'arma_pt': secretas.get(r, {}).get('arma_pt', ''),
                          'recompensa_pt': rec, 'lore_pt': lore.group(1) if lore else ''})
    return {'masmorras': {str(x['regiao']): x for x in masmorras}, 'bosses': bosses}


if __name__ == '__main__':
    d = gerar()
    with open(os.path.join(RAIZ, 'dados', 'masmorras.json'), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    for x in d['masmorras'].values():
        print('%2d %-28s %s  boss %-28s %s' % (x['regiao'], x['nome_pt'], [s['tipo'][:4] for s in x['salas']], x['boss'], x['arma']))
