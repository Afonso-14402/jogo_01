"""Ícones 16×16 das regiões 2–10, feitos a partir da lista de itens de docs/textos/itens.md.

Cada item recebe um molde (minério, frasco, peixe, armadura...) e uma cor, escolhidos pelas palavras do ID e do nome.
Se um ícone ficar mal, acrescenta o ID a AJUSTES com o molde e a cor certos.
As armas não estão aqui (os ícones delas saem de armas.py).

Uso: python3 ferramentas/arte/icones_auto.py [região ...]     (sem argumentos: 2 a 10)
"""
import os
import re
import sys
import unicodedata
sys.path.insert(0, os.path.dirname(__file__))
import icones as I
from motor import Parte, retangulo, RAMPAS

ITENS = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'textos', 'itens.md')
PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'icones')

TIER = {'ferro': 'ferro', 'aco': 'cinza', 'prata': 'branco', 'gelo_eterno': 'agua', 'coral': 'rosa', 'obsidiana': 'preto',
        'mitril': 'lilas', 'oricalco': 'ouro', 'estelar': 'roxo'}
PALETA_REGIAO = {2: ['cinza', 'castanho', 'agua', 'lilas'], 3: ['verde', 'verde_esc', 'castanho', 'musgo'],
                 4: ['amarelo', 'laranja', 'castanho', 'ouro'], 5: ['agua', 'branco', 'azul', 'cinza'],
                 6: ['azul', 'agua', 'rosa', 'branco'], 7: ['laranja', 'vermelho', 'preto', 'cinza'],
                 8: ['roxo', 'lilas', 'cinza', 'preto'], 9: ['branco', 'ouro', 'agua', 'amarelo'],
                 10: ['roxo', 'preto', 'azul', 'lilas']}

# palavra (no ID ou no nome) -> cor
CORES = [
    ('vermelh', 'vermelho'), ('rubi', 'vermelho'), ('sangue', 'vermelho'), ('azul', 'azul'), ('safira', 'azul'),
    ('verde', 'verde'), ('esmeralda', 'verde'), ('jade', 'verde'), ('dourad', 'ouro'), ('ouro', 'ouro'), ('oricalco', 'ouro'),
    ('prata', 'branco'), ('perola', 'branco'), ('diamante', 'branco'), ('osso', 'branco'), ('neve', 'branco'), ('nuvem', 'branco'),
    ('negr', 'preto'), ('preto', 'preto'), ('sombra', 'preto'), ('obsidiana', 'preto'), ('carvao', 'preto'), ('tinta', 'preto'),
    ('roxo', 'roxo'), ('roxa', 'roxo'), ('ametista', 'roxo'), ('vazio', 'roxo'), ('estel', 'roxo'),
    ('gelo', 'agua'), ('cristal', 'agua'), ('vidro', 'agua'), ('agua', 'agua'), ('mar', 'agua'),
    ('fogo', 'laranja'), ('lava', 'laranja'), ('magma', 'laranja'), ('brasa', 'laranja'), ('chama', 'laranja'), ('enxofre', 'amarelo'),
    ('rosa', 'rosa'), ('coral', 'rosa'), ('amarel', 'amarelo'), ('sol', 'amarelo'), ('topazio', 'amarelo'), ('mel', 'ouro'),
    ('castanh', 'castanho'), ('couro', 'castanho'), ('toupeira', 'castanho'), ('madeira', 'madeira'),
    ('lilas', 'lilas'), ('fantasma', 'lilas'), ('ecto', 'lilas'), ('alma', 'lilas'), ('ferro', 'ferro'), ('pedra', 'cinza'),
    ('cinza', 'cinza'), ('lodo', 'musgo'), ('veneno', 'verde'), ('fungo', 'azul'), ('cobre', 'cobre'), ('bronze', 'cobre'), ('latao', 'ouro'),
]

GEMAS = {'topazio': 'amarelo', 'rubi': 'vermelho', 'ametista': 'roxo', 'safira': 'azul', 'esmeralda': 'verde', 'diamante': 'branco',
         'perola': 'branco', 'opala': 'rosa', 'onix': 'preto', 'ambar': 'laranja', 'jade': 'verde', 'granada': 'vermelho'}

# ajustes à mão: id -> (molde, argumentos)
AJUSTES = {
    'carvao': ('pedra', ('preto',)), 'pedra': ('pedra', ('cinza',)), 'guano': ('po', ('castanho',)),
    'engrenagem': ('engrenagem', ('ferro',)), 'bomba': ('bomba', ()), 'giz_mineiro': ('lingote', ('branco',)),
}


def slug(s):
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '_', s).strip('_')


def ler_itens():
    """Devolve {região: [(id, nome, secção)]} sem as armas."""
    txt = open(ITENS, encoding='utf-8').read()
    out = {}
    for bloco in re.split(r'\n## ', txt):
        m = re.match(r'Região (\d+)', bloco)
        if not m:
            continue
        n = int(m.group(1))
        for sec in re.split(r'\n### ', bloco)[1:]:
            titulo = sec.split('\n', 1)[0].strip()
            if titulo.startswith('Armas'):
                continue
            for it in re.finditer(r'^\| `([a-z0-9_]+)` \| ([^|]+)\|', sec, re.M):
                out.setdefault(n, []).append((it.group(1), it.group(2).strip(), titulo))
    return out


def cor_de(texto, regiao, iid):
    for k, c in CORES:
        if k in texto:
            return c
    pal = PALETA_REGIAO.get(regiao, ['cinza'])
    return pal[sum(map(ord, iid)) % len(pal)]


def tem(texto, *palavras):
    return any(p in texto for p in palavras)


# --- moldes que faltavam ---
def caixa(c):
    return [Parte(retangulo(2, 4, 13, 13, canto=1), RAMPAS[c] if isinstance(c, str) else c, z=1),
            Parte(retangulo(2, 7, 13, 8), RAMPAS['ferro'], z=2, plano=True),
            Parte(retangulo(7, 6, 8, 9), RAMPAS['ouro'], z=3, plano=True)]


def engrenagem(c):
    from motor import elipse
    m = set(elipse(8, 8, 5, 5))
    for dx, dy in ((0, -6), (0, 6), (-6, 0), (6, 0), (-4, -4), (4, 4), (-4, 4), (4, -4)):
        m |= set(elipse(8 + dx * 0.95, 8 + dy * 0.95, 1.4, 1.4))
    m -= set(elipse(8, 8, 1.5, 1.5))
    return [Parte(m, RAMPAS[c], z=1)]


def bomba():
    from motor import elipse, capsula
    return [Parte(elipse(7, 10, 5, 5), RAMPAS['preto'], z=1), Parte(capsula(10, 5, 12, 2, 0.6), RAMPAS['castanho'], z=0),
            Parte({(12, 1), (13, 1), (13, 2)}, None, z=3, separar=False, cor='#f9c22b')]


EXTRA = {'caixa': caixa, 'engrenagem': engrenagem, 'bomba': bomba}


def escolher(iid, nome, sec, regiao):
    t = iid + ' ' + slug(nome)
    if iid in AJUSTES:
        f, a = AJUSTES[iid]
        return (EXTRA.get(f) or getattr(I, f))(*a)
    c = cor_de(t, regiao, iid)
    # armaduras de conjunto
    for peca in ('cabeca', 'corpo', 'maos', 'pes', 'capa'):
        if iid.endswith('_' + peca):
            base = iid[:-len(peca) - 1]
            return I.armadura(peca, TIER.get(base, c))
    if tem(t, 'coroa', 'tiara'):
        return I.coroa(c)
    if tem(t, 'anel'):
        return I.anel(c if c != 'cinza' else 'ferro', 'agua')
    if tem(t, 'amuleto', 'colar', 'medalha', 'pendente', 'talisma', 'bussola', 'relogio'):
        return I.amuleto('ouro' if c in ('cinza',) else c, 'agua')
    if tem(t, 'capacete', 'elmo', 'chapeu', 'mascara', 'gorro', 'turbante', 'oculos'):
        return I.armadura('cabeca', c)
    if tem(t, 'botas'):
        return I.armadura('pes', c)
    if tem(t, 'luvas'):
        return I.armadura('maos', c)
    if tem(t, 'capa', 'manto', 'cachecol', 'xaile', 'vestido', 'tunica', 'casaco'):
        return I.armadura('capa', c)
    if tem(t, 'bolsa', 'mochila', 'saco_de', 'cantil'):
        return I.bolsa(c if c != 'cinza' else 'couro')
    if tem(t, 'picareta'):
        return I.ferramenta('picareta', c)
    if tem(t, 'machado'):
        return I.ferramenta('machado', c)
    if tem(t, 'cana_'):
        return I.ferramenta('cana', c)
    if tem(t, 'semente', 'esporos_de', 'muda_', 'bolbo'):
        return I.saco('madeira', c)
    if tem(t, 'minerio'):
        return I.minerio(c)
    if tem(t, 'lingote', 'barra_'):
        return I.lingote(c)
    for g, gc in GEMAS.items():
        if g in t:
            return I.gema(gc)
    if tem(t, 'cristal', 'prisma', 'fragmento', 'nucleo', 'estilhaco', 'vidro', 'gelo_', 'estrela', 'essencia'):
        return I.cristal(c)
    if tem(t, 'pocao', 'elixir', 'tonico', 'antidoto', 'frasco', 'remedio', 'oleo'):
        return I.frasco(c, ['redondo', 'alto', 'cone'][len(iid) % 3])
    if tem(t, 'bomba', 'granada'):
        return bomba()
    if sec.startswith('Consum') and tem(t, 'sopa', 'assad', 'pao', 'bolo', 'torta', 'prato', 'grelhad', 'ensopado', 'caril', 'salada',
                                         'guisado', 'frito', 'cozid', 'panqueca', 'sushi', 'gelado', 'estufad', 'tarte', 'banquete', 'cha_', 'cafe'):
        forma = 'sopa' if tem(t, 'sopa', 'caldo', 'ensopado', 'caril', 'guisado', 'cha_', 'cafe', 'estufad') else \
            'torta' if tem(t, 'torta', 'tarte', 'bolo') else 'panquecas' if tem(t, 'panqueca') else 'monte'
        return I.prato(c, forma)
    if tem(t, 'espetada', 'espeto'):
        return I.espeto(c)
    if sec.startswith('Peixes') and not tem(t, 'semente') and (tem(t, 'peixe', 'carpa', 'truta', 'enguia', 'salmao', 'atum', 'perca', 'raia',
                                                                    'bacalhau', 'tubarao', 'lula', 'polvo', 'peixe', 'baiacu', 'sardinha',
                                                                    'caranguejo', 'lagost', 'camarao', 'piranha', 'bagre', 'linguado')
                                                               or 'fase' not in t and not tem(t, 'flor', 'fruto', 'erva', 'cogumelo', 'fungo',
                                                                                              'batata', 'baga', 'raiz', 'cacto', 'lotus',
                                                                                              'arroz', 'cana', 'abobora', 'trigo', 'milho', 'alga',
                                                                                              'nenufar', 'tamara', 'coco', 'pimento', 'malagueta',
                                                                                              'uva', 'melao', 'feijao', 'chá', 'cha', 'rosa',
                                                                                              'lirio', 'beterraba', 'cenoura', 'couve', 'nabo',
                                                                                              'cebola', 'alho', 'pera', 'figo', 'ameixa', 'manga',
                                                                                              'ananas', 'banana', 'pinha', 'cereja', 'morango',
                                                                                              'algodao', 'tomate', 'tremoco', 'semente'))):
        return I.peixe(c, None)
    if tem(t, 'cogumelo', 'fungo', 'trufa'):
        return I.cogumelo(c, 'branco', 'lumin' in t)
    if tem(t, 'flor', 'lotus', 'lirio', 'rosa_', 'nenufar', 'orquidea', 'petala'):
        return I.flor(c)
    if tem(t, 'erva', 'alga', 'musgo', 'junco', 'trevo', 'hortela', 'liquen', 'feno', 'cha'):
        return I.erva('verde' if c in ('cinza', 'castanho') else c)
    if tem(t, 'batata', 'raiz', 'nabo', 'cenoura', 'beterraba'):
        return I.fruto(c, False, 'batata')
    if tem(t, 'fruto', 'fruta', 'baga', 'maca', 'coco', 'tamara', 'cacto', 'abobora', 'uva', 'melao', 'pera', 'figo', 'manga',
           'ananas', 'banana', 'cereja', 'morango', 'tomate', 'pimento', 'malagueta', 'romã', 'roma', 'laranja', 'limao', 'noz', 'bolota'):
        return I.fruto(c, True)
    if tem(t, 'trigo', 'arroz', 'milho', 'cana', 'algodao', 'feijao'):
        return I.erva('amarelo')
    if tem(t, 'mel', 'geleia', 'pote', 'compota', 'iogurte', 'leite', 'queijo', 'manteiga'):
        return I.pote(c)
    if tem(t, 'carne', 'bife', 'coxa', 'presunto', 'lombo', 'salsicha'):
        return I.carne(c if c != 'cinza' else 'rosa')
    if tem(t, 'ovo'):
        return I.ovo(c)
    if tem(t, 'pena', 'asa_', 'asa'):
        return I.pena(c)
    if tem(t, 'chifre', 'corno', 'haste'):
        return I.chifre(c if c != 'cinza' else 'branco')
    if tem(t, 'presa', 'dente', 'garra', 'ferrao', 'espinho', 'osso', 'costela', 'cranio', 'unha', 'bico', 'pinca', 'tentaculo'):
        return I.presa(c if c not in ('cinza', 'castanho') else 'branco')
    if tem(t, 'gel', 'gosma', 'ecto', 'veneno', 'glandula', 'tinta', 'lagrima', 'sangue', 'lava', 'magma', 'agua', 'orvalho', 'seiva',
           'lodo', 'resina', 'mercurio', 'gota'):
        return I.gota(c)
    if tem(t, 'po_', '_po', 'cinza', 'areia', 'sal', 'enxofre', 'polen', 'guano', 'farinha', 'acucar', 'especiaria', 'pimenta', 'poeira'):
        return I.po(c)
    if tem(t, 'folha'):
        return I.folha(c)
    if tem(t, 'chave'):
        return I.chave(c if c not in ('cinza',) else 'ferro')
    if tem(t, 'tocha', 'lanterna', 'vela', 'lampiao'):
        return I.tocha()
    if tem(t, 'papel', 'carta', 'diario', 'pagina', 'mapa', 'livro', 'pergaminho', 'contrato', 'nota', 'bilhete', 'receita', 'partitura',
           'convite', 'runas', 'grimorio', 'registo', 'certificado', 'poema', 'desenho', 'foto', 'retrato'):
        return I.papel('branco', c)
    if tem(t, 'madeira', 'tronco', 'pinheiro', 'escora', 'tabua', 'ramo', 'bambu', 'mogno', 'ebano', 'carvalho', 'cedro', 'remo'):
        return I.madeira('madeira' if c in ('cinza', 'castanho') else c)
    if tem(t, 'couro', 'pele', 'pelo', 'la_', '_la', 'escama', 'pelagem'):
        return I.couro(c)
    if tem(t, 'seda', 'fio', 'linho', 'pano', 'tecido', 'corda', 'teia', 'fita', 'rede', 'ligadura', 'trapo'):
        return I.fio(c)
    if tem(t, 'concha', 'carapaca', 'casca', 'pedra', 'rocha', 'tijolo', 'lingote', 'calhau', 'marmore', 'basalto', 'pedaco', 'carvao'):
        return I.pedra(c)
    if tem(t, 'engrenagem', 'parafuso', 'mola', 'peca', 'mecanismo', 'roda'):
        return engrenagem('ferro' if c == 'cinza' else c)
    if tem(t, 'trofeu', 'estatua', 'medalhao'):
        return I.amuleto('ouro', c)
    return caixa(c if c not in ('cinza',) else 'madeira')


PLANTA_ALTA = ('arvore', 'macieira', 'palmeira', 'coqueiro', 'cacto', 'girassol', 'milho', 'cana', 'bambu', 'videira', 'pimenteira',
               'tamareira', 'trigo', 'algodao')


def gerar(regioes):
    itens = ler_itens()
    os.makedirs(os.path.join(PASTA, 'plantas'), exist_ok=True)
    total = plantas = 0
    for n in regioes:
        lista = itens.get(n, [])
        ids = {i for i, _, _ in lista}
        for iid, nome, sec in lista:
            I.icone(escolher(iid, nome, sec, n)).save(os.path.join(PASTA, f'{iid}.png'))
            total += 1
            # plantas: para cada semente, as 4 fases da colheita
            if iid.startswith('semente_'):
                colheita = iid[len('semente_'):]
                if colheita not in ids:
                    continue
                cn = dict((i, (nm, s)) for i, nm, s in lista)[colheita]
                c = cor_de(colheita + ' ' + slug(cn[0]), n, colheita)
                tipo = 'alta' if any(p in colheita for p in PLANTA_ALTA) else 'baixa'
                for f in range(1, 5):
                    I.planta(f, c, tipo=tipo).save(os.path.join(PASTA, 'plantas', f'{colheita}_fase_{f}.png'))
                plantas += 1
    print('ok', total, 'ícones,', plantas, 'plantas x 4 fases')


if __name__ == '__main__':
    gerar([int(a) for a in sys.argv[1:]] or range(2, 11))
