"""Arte dos monstros, guardiões, bosses e animais das regiões 2–10 (usa os moldes de criaturas.py).

Cada entrada: (nome, molde, configuração, ataques[, 'especial' para bosses]).
Os ataques podem ter nome próprio: ('teia', 'sopro') grava "nome_teia_lado.png" com a pose-tipo "sopro".

Uso:  python3 ferramentas/arte/bestiario_arte.py 2            (região 2 inteira)
      python3 ferramentas/arte/bestiario_arte.py 2 morcego    (só algumas)
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from criaturas import lote

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte')
G48 = dict(k=1.5, W=48)
G64 = dict(k=2.0, W=64)
G128 = dict(k=4.0, W=128)
BOSS9 = ['golpe', 'magia', 'pancada_chao', 'area', 'investida', 'invocar', 'sopro', 'onda', 'rugido']

REGIOES = {}

# ======================= Região 2 — Cavernas e Minas =======================
REGIOES[2] = dict(
    pasta='r02_cavernas',
    monstros=[
        ('morcego', 'voador', dict(cor='roxo', asa='membrana', orelhas=True, olho='#e83b3b'),
         [('dormir', 'dormir'), ('acordar', 'levantar'), ('voo_rasante', 'investida')]),
        ('goblin_mineiro', 'bipede', dict(cor='verde', roupa='couro', pernas='castanho', orelhas_longas=True, arma='picareta',
                                          chapeu='ferro', olho='#f9c22b', k=0.9),
         [('trabalhar', 'golpe'), ('picaretada', 'golpe'), ('atirar', 'atirar')]),
        ('golem_de_pedra', 'bipede', dict(G48, cor='cinza', cabeca='bloco', corpulento=2, olho='#f9c22b', mao='cinza'),
         [('levantar', 'levantar'), ('murro', 'golpe'), ('pisao', 'pancada_chao'), ('atirar', 'atirar')]),
        ('toupeira_gigante', 'quadrupede', dict(cor='castanho', cabeca='toupeira', pata=1.1, cauda='curta', orelhas=None,
                                                cor_focinho='rosa', comprimento=1.1, olho='#2e222f'),
         [('monticulo', 'enterrar'), ('sair', 'levantar'), ('garras', 'golpe'), ('enterrar', 'enterrar')]),
        ('aranha_da_caverna', 'aracnideo', dict(tipo='aranha', cor='castanho', marca='amarelo', olhos=4),
         [('descer', 'descer'), ('morder', 'golpe'), ('teia', 'sopro'), ('saltar', 'salto')]),
        ('kobold', 'bipede', dict(cor='laranja', cabeca='focinho', cauda=True, roupa='couro', arma='lanca', k=0.75, olho='#2e222f'),
         [('estocada', 'golpe'), ('por_armadilha', 'golpe'), ('soprar', 'sopro')]),
        ('lagarta_de_cristal', 'serpente', dict(G48, cor='verde', segmentos=6, grossura=4.2, cristais=['agua', 'lilas', 'branco'], fx_cor='branco'),
         [('enrolar', 'escudo'), ('rolar', 'investida'), ('espinhos', 'area'), ('brilho', 'magia')]),
        ('fantasma_mineiro', 'amorfo', dict(tipo='fantasma', cor='agua', fx_cor='agua', olho='#2e222f'),
         [('aparecer', 'aparecer'), ('lamento', 'rugido'), ('desaparecer', 'desaparecer')]),
        # com nome
        ('rei_goblin_gruk', 'bipede', dict(G48, cor='verde', roupa='vermelho', pernas='castanho', corpulento=2, orelhas_longas=True,
                                            coroa='ouro', arma='clava', arma_cor='ferro', olho='#f9c22b'),
         ['pancada_chao', 'invocar', 'atirar']),
        ('toupeira_dourada', 'quadrupede', dict(cor='ouro', cabeca='toupeira', pata=1.0, cauda='curta', orelhas=None, cor_focinho='rosa'),
         [('fugir', 'enterrar'), ('sair', 'levantar')]),
    ],
    guardioes=[
        ('vagoneta_assombrada', 'objeto', dict(G48, tipo='vagoneta', cor='ferro', olho='#fb6b1d', fx_cor='preto'), ['investida', 'sopro', 'rugido']),
        ('touro_das_galerias', 'bipede', dict(G64, cor='castanho', cabeca='focinho', chifres='branco', chapeu='amarelo', roupa='couro',
                                              corpulento=2, arma='picareta', olho='#e83b3b'), ['investida', 'golpe', 'rugido']),
        ('prisma_vivo', 'objeto', dict(G48, tipo='prisma', cor='agua', cor2='lilas', fx_cor='lilas'), ['sopro', 'area', 'magia']),
        ('barqueiro_afogado', 'bipede', dict(G48, cor='branco', cabeca='caveira', roupa='verde_esc', capa='verde_esc', costelas=True,
                                             arma='cajado', fx_cor='verde', pernas='verde_esc'), ['golpe', 'magia', 'invocar']),
        ('agua_viva_fungica', 'aquatico', dict(G64, tipo='alforreca', cor='rosa', olho='#d5e04b', fx_cor='amarelo'), ['golpe', 'area', 'onda']),
        ('morcego_rei_dos_ecos', 'voador', dict(G64, cor='roxo', asa='membrana', orelhas=True, cabeca_r=4, olho='#e83b3b', fx_cor='lilas'),
         ['onda', 'magia', 'investida']),
        ('sentinela_ana', 'bipede', dict(G48, cor='cobre', cabeca='bloco', corpulento=1, armadura='laranja', arma='clava', arma_cor='cobre',
                                         olho='#f9c22b', fx_cor='laranja'), ['golpe', 'sopro', 'magia']),
    ],
    bosses=[
        ('aranha_mae', 'aracnideo', dict(G64, tipo='aranha', cor='roxo', marca='vermelho', olhos=4, olho='#e83b3b', fx_cor='verde'),
         ['golpe', 'sopro', 'descer', 'invocar', 'area', 'salto'], 'especial'),
        ('golem_de_cristal', 'bipede', dict(G128, cor='cinza', cabeca='bloco', corpulento=3, cristais=['agua', 'lilas', 'verde'],
                                            armadura='agua', olho='#30e1b9', fx_cor='agua', mao='cinza'), BOSS9, 'especial'),
        ('rei_anao_esquecido', 'bipede', dict(G64, cor='agua', roupa='agua', cabelo='branco', coroa='ouro', corpulento=1, arma='machado',
                                              arma_cor='agua', fx_cor='agua', olho='#ffffff', desfaz=True),
         ['golpe', 'pancada_chao', 'invocar', 'desaparecer'], 'especial'),
    ],
    animais=[
        ('morceguinho', 'voador', dict(cor='lilas', asa='membrana', orelhas=True, k=0.7), []),
        ('aranha_de_seda', 'aracnideo', dict(tipo='aranha', cor='branco', olhos=2, k=0.7, olho='#e83b3b'), []),
    ],
)


def gerar(n, ver=None):
    r = REGIOES[n]
    base = os.path.join(RAIZ, 'regioes', r['pasta'])
    for grupo in ('monstros', 'guardioes', 'bosses'):
        print(grupo)
        lote(os.path.join(base, grupo), r.get(grupo, []), ver)
    print('animais')
    lote(os.path.join(RAIZ, 'animais'), r.get('animais', []), ver)


if __name__ == '__main__':
    gerar(int(sys.argv[1]), sys.argv[2:] or None)
