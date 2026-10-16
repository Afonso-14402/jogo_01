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
G96 = dict(k=3.0, W=96)
G128 = dict(k=4.0, W=128)
BOSS9 = ['golpe', 'magia', 'pancada_chao', 'area', 'investida', 'invocar', 'sopro', 'onda', 'rugido']
BOSS6 = ['golpe', 'sopro', 'investida', 'area', 'invocar', 'rugido']

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

# ======================= Região 3 — Pântano e Selva =======================
REGIOES[3] = dict(
    pasta='r03_pantano',
    monstros=[
        ('sapo_venenoso', 'quadrupede', dict(cor='verde', cor2='amarelo', cabeca='reptil', comprimento=0.7, altura=0.6, pata=1.6, cauda=None,
                                             orelhas=None, manchas='roxo', olho='#f9c22b', fx_cor='roxo'),
         [('saltar', 'salto'), ('lingua', 'golpe'), ('cuspir', 'sopro')]),
        ('homem_lagarto_renegado', 'bipede', dict(cor='verde_esc', cabeca='focinho', cauda=True, roupa='couro', arma='lanca', escudo='madeira',
                                                  olho='#f9c22b'),
         [('lanca', 'golpe'), ('escudo', 'escudo'), ('grito', 'rugido'), ('arco', 'atirar')]),
        ('flor_carnivora', 'planta', dict(G48, tipo='carnivora', cor='vermelho', caule='verde_esc', fx_cor='amarelo'),
         [('abrir', 'levantar'), ('dentada', 'golpe'), ('sementes', 'atirar'), ('polen', 'area')]),
        ('mosquito_gigante', 'voador', dict(cor='castanho', asa='inseto', asa_cor='agua', bico='preto', riscas='preto', corpo_rx=4, olho='#e83b3b'),
         [('picar', 'investida')]),
        ('crocodilo', 'quadrupede', dict(G48, cor='verde_esc', cor2='musgo', cabeca='reptil', comprimento=1.4, altura=0.6, pata=1.2, cauda='grossa',
                                         orelhas=None, barriga='amarelo', espinhos='verde_esc', olho='#f9c22b'),
         [('emergir', 'levantar'), ('dentada', 'golpe'), ('rodopio', 'area'), ('cauda', 'investida')]),
        ('macaco_ladrao', 'bipede', dict(cor='castanho', cabeca='focinho', cauda=True, roupa='castanho', k=0.85, olho='#2e222f'),
         [('roubar', 'investida'), ('atirar', 'atirar'), ('rir', 'rugido')]),
        ('sanguessuga_gigante', 'serpente', dict(cor='preto', segmentos=5, grossura=2.6, boca_redonda=True, cego=True, aneis='vermelho', agua=True),
         [('saltar', 'salto'), ('agarrada', 'golpe')]),
        ('bruxa_do_pantano', 'bipede', dict(cor='verde', roupa='roxo', pernas='roxo', chapeu='preto', cabelo='cinza', arma='cajado', fx_cor='verde',
                                            olho='#f9c22b'),
         [('maldicao', 'magia'), ('atirar', 'atirar'), ('afundar', 'enterrar'), ('aparecer', 'levantar')]),
        ('mae_crocodilo_mandibula', 'quadrupede', dict(G64, cor='verde_esc', cabeca='reptil', comprimento=1.4, altura=0.6, pata=1.2, cauda='grossa',
                                                       orelhas=None, barriga='amarelo', manchas='musgo', espinhos='musgo', olho='#f9c22b'),
         ['enterrar', 'golpe', 'invocar']),
        ('rei_macaco_bobo', 'bipede', dict(cor='castanho', cabeca='focinho', cauda=True, roupa='castanho', coroa='amarelo', capa='verde', k=0.95),
         ['investida', 'atirar', 'salto']),
    ],
    guardioes=[
        ('garca_lanca', 'voador', dict(G48, cor='cinza', asa='penas', bico='amarelo', cabeca_cor='branco', pernas='amarelo', cauda_penas='cinza'),
         ['investida', 'golpe', 'sopro']),
        ('lodo_toxico', 'amorfo', dict(G64, tipo='lodo', cor='verde', cor2='branco', fx_cor='verde', olho='#2e222f'), ['pancada_chao', 'sopro', 'invocar']),
        ('pantera_de_jade', 'quadrupede', dict(G48, cor='verde_esc', cabeca='felino', manchas='agua', cauda='normal', olho='#30e1b9'),
         ['investida', 'golpe', 'desaparecer']),
        ('totem_vivo_de_sssar', 'objeto', dict(G64, tipo='totem', blocos=['madeira', 'verde_esc', 'vermelho'], fx_cor='verde'), ['magia', 'invocar', 'onda']),
        ('caranguejo_violinista_gigante', 'aracnideo', dict(G64, tipo='caranguejo', cor='laranja', pincas=True, pinca_cor='amarelo', pernas=6),
         ['golpe', 'onda', 'escudo']),
        ('ninfa_da_cascata', 'bipede', dict(G48, cor='agua', roupa='agua', cabelo='azul', pernas='agua', fx_cor='agua', olho='#ffffff'),
         ['magia', 'onda', 'escudo']),
        ('grande_bugio', 'bipede', dict(G64, cor='castanho', cabeca='focinho', corpulento=2, roupa='castanho', olho='#e83b3b'), ['rugido', 'pancada_chao', 'atirar']),
        ('driade_corrompida', 'planta', dict(G48, tipo='driade', pele='verde', cor='verde_esc', cabelo='vermelho', fx_cor='roxo'), ['magia', 'golpe', 'invocar']),
    ],
    bosses=[
        ('serpente_do_lodo', 'serpente', dict(G64, cor='musgo', segmentos=7, grossura=3.8, chifres='cinza', agua=True, olho='#f9c22b', fx_cor='verde'),
         BOSS6, 'especial'),
        ('hidra_do_pantano', 'quadrupede', dict(G128, cor='verde_esc', cores_cabecas=['verde', 'roxo', 'amarelo'], cabeca='reptil', cabecas=3, comprimento=1.2, pata=1.6, cauda='grossa', orelhas=None,
                                                manchas='verde_esc', espinhos='verde', olho='#f9c22b', fx_cor='verde'), BOSS9, 'especial'),
        ('jaguar_de_pedra_solar', 'quadrupede', dict(G64, cor='ouro', cabeca='felino', manchas='laranja', olho='#e83b3b', fx_cor='amarelo'),
         ['investida', 'salto', 'area', 'rugido'], 'especial'),
    ],
    animais=[
        ('sapinho', 'quadrupede', dict(cor='verde', cabeca='reptil', comprimento=0.6, altura=0.6, pata=1.4, cauda=None, orelhas=None, k=0.6), []),
    ],
)

# ======================= Região 4 — Deserto e Pirâmides =======================
REGIOES[4] = dict(
    pasta='r04_deserto',
    monstros=[
        ('escorpiao', 'aracnideo', dict(tipo='escorpiao', cor='castanho', ferrao='vermelho', pincas=True, pernas=6),
         [('sair', 'levantar'), ('pincas', 'golpe'), ('ferrao', 'investida'), ('enterrar', 'enterrar')]),
        ('mumia', 'bipede', dict(cor='branco', roupa='branco', pernas='branco', ligaduras=True, olho='#f9c22b'),
         [('ligaduras', 'sopro'), ('murro', 'golpe'), ('gemer', 'rugido')]),
        ('verme_da_areia', 'serpente', dict(G48, cor='laranja', segmentos=6, grossura=4.0, boca_redonda=True, cego=True, buraco=True, aneis='amarelo'),
         [('sair', 'levantar'), ('cuspir', 'sopro'), ('chicote', 'golpe'), ('afundar', 'enterrar')]),
        ('esqueleto_guerreiro', 'bipede', dict(cor='branco', cabeca='caveira', costelas=True, roupa='branco', arma='espada', escudo='ferro'),
         [('cimitarra', 'golpe'), ('escudo', 'escudo'), ('estocada', 'investida'), ('remontar', 'levantar')]),
        ('chacal', 'quadrupede', dict(cor='laranja', cabeca='lobo', comprimento=0.9, barriga='amarelo', olho='#f9c22b'),
         [('mordida', 'golpe'), ('uivo', 'rugido')]),
        ('espirito_da_areia', 'amorfo', dict(tipo='elemental', cor='amarelo', cor2='laranja', fx_cor='amarelo'),
         [('rodar', 'area'), ('desaparecer', 'desaparecer')]),
        ('bandido_do_deserto', 'bipede', dict(cor='pele', roupa='vermelho', pernas='castanho', cabelo='branco', arma='espada', olho='#2e222f'),
         [('cimitarra', 'golpe'), ('arco', 'atirar'), ('atirar_bomba', 'atirar')]),
        ('escaravelho_de_fogo', 'aracnideo', dict(tipo='escaravelho', cor='vermelho', cabeca_cor='preto', pernas=6, k=0.65, fx_cor='laranja'),
         [('rolar', 'investida'), ('explodir', 'area')]),
        ('sultao_bandido_kasim', 'bipede', dict(cor='pele', roupa='ouro', pernas='vermelho', cabelo='ouro', capa='vermelho', arma='espada', olho='#2e222f'),
         ['invocar', 'desaparecer', 'area']),
        ('verme_colosso', 'serpente', dict(G128, cor='laranja', segmentos=7, grossura=4.4, boca_redonda=True, cego=True, buraco=True, aneis='castanho'),
         ['levantar', 'enterrar', 'area']),
    ],
    guardioes=[
        ('lagarto_duna_gigante', 'quadrupede', dict(G64, cor='amarelo', cabeca='reptil', comprimento=1.3, pata=1.3, cauda='grossa', orelhas=None,
                                                    espinhos='castanho', olho='#e83b3b'), ['investida', 'enterrar', 'sopro']),
        ('a_miragem', 'amorfo', dict(G48, tipo='elemental', cor='agua', cor2='branco', fx_cor='agua'), ['desaparecer', 'magia', 'invocar']),
        ('abutre_rei', 'voador', dict(G48, cor='castanho', asa='penas', cabeca_cor='rosa', bico='amarelo', crista='ouro', cauda_penas='castanho'),
         ['investida', 'sopro', 'invocar']),
        ('golem_de_arenito', 'bipede', dict(G64, cor='amarelo', cabeca='bloco', corpulento=2, armadura='laranja', olho='#30e1b9', mao='amarelo'),
         ['golpe', 'pancada_chao', 'escudo']),
        ('djinn_da_tempestade', 'bipede', dict(G48, cor='azul', roupa='azul', cauda_peixe='lilas', cabelo='branco', fx_cor='agua', olho='#ffffff'),
         ['magia', 'area', 'sopro']),
        ('cavaleiro_de_ossos_montado', 'quadrupede', dict(G64, cor='branco', cabeca='cavalo', espinhos='cinza', altura=1.3, comprimento=1.1,
                                                          orelhas='pontiagudas', olho='#e83b3b', manchas='cinza'), ['investida', 'golpe', 'invocar']),
        ('esfinge_menor', 'quadrupede', dict(G64, cor='amarelo', cabeca='felino', juba='castanho', olho='#30e1b9', fx_cor='agua'), ['magia', 'golpe', 'rugido']),
        ('sacerdote_chacal', 'bipede', dict(G48, cor='preto', cabeca='focinho', roupa='ouro', pernas='branco', arma='cajado', fx_cor='ouro', olho='#f9c22b'),
         ['magia', 'invocar', 'escudo']),
    ],
    bosses=[
        ('escorpiao_imperador', 'aracnideo', dict(G64, tipo='escorpiao', cor='preto', ferrao='ouro', pincas=True, pinca_cor='ouro', marca='azul',
                                                  pernas=6, olho='#30e1b9', fx_cor='agua'), BOSS6, 'especial'),
        ('farao_eterno', 'bipede', dict(G96, cor='ouro', roupa='ouro', pernas='ouro', ligaduras=True, coroa='azul', capa='azul', arma='cajado',
                                        fx_cor='agua', olho='#30e1b9'), BOSS9, 'especial'),
        ('esqueleto_de_dragao_jovem', 'quadrupede', dict(G64, cor='branco', cabeca='reptil', asas='branco', espinhos='cinza', cauda='normal',
                                                         orelhas=None, chifres='cinza', olho='#30e1b9', fx_cor='azul'),
         ['sopro', 'salto', 'golpe', 'rugido'], 'especial'),
    ],
    animais=[
        ('escaravelho_dourado', 'aracnideo', dict(tipo='escaravelho', cor='ouro', pernas=6, k=0.6), []),
        ('lagarto_da_areia', 'quadrupede', dict(G48, cor='amarelo', cabeca='reptil', comprimento=1.3, cauda='grossa', orelhas=None, espinhos='laranja'), []),
    ],
)

# ======================= Região 5 — Montanhas Geladas =======================
REGIOES[5] = dict(
    pasta='r05_gelo',
    monstros=[
        ('lobo_de_gelo', 'quadrupede', dict(cor='branco', cabeca='lobo', barriga='agua', olho='#30e1b9', fx_cor='agua'),
         [('mordida', 'golpe'), ('sopro', 'sopro'), ('uivo', 'rugido')]),
        ('urso_polar', 'quadrupede', dict(G48, cor='branco', cabeca='urso', orelhas='redondas', grossura=5.2, pata=1.6, cauda='curta', olho='#2e222f'),
         [('pescar', 'golpe'), ('patada', 'golpe'), ('abraco', 'investida'), ('rugido_de_pe', 'rugido')]),
        ('golem_de_gelo', 'bipede', dict(G48, cor='agua', cabeca='bloco', corpulento=2, cristais=['branco', 'agua'], olho='#ffffff', mao='agua', fx_cor='agua'),
         [('murro', 'golpe'), ('estacas', 'area')]),
        ('espirito_da_neve', 'amorfo', dict(tipo='fantasma', cor='branco', fx_cor='agua', olho='#30e1b9'),
         [('nevao', 'area'), ('desaparecer', 'desaparecer')]),
        ('harpia_gelida', 'voador', dict(cor='agua', asa='penas', cabeca_cor='pele', cauda_penas='branco', pernas='amarelo', fx_cor='branco'),
         [('mergulho', 'investida'), ('atirar_penas', 'atirar'), ('grito', 'rugido')]),
        ('cacador_congelado', 'bipede', dict(cor='agua', roupa='couro', pernas='castanho', cabelo='branco', arma='arco', olho='#30e1b9'),
         [('arco', 'atirar'), ('lanca', 'golpe'), ('armadilha', 'golpe')]),
        ('pinguim_guerreiro', 'bipede', dict(cor='preto', roupa='branco', pernas='amarelo', arma='lanca', k=0.6, olho='#ffffff'),
         [('deslizar', 'investida'), ('bicada', 'golpe'), ('atirar', 'atirar')]),
        ('mamute_jovem', 'quadrupede', dict(G64, cor='castanho', cabeca='urso', orelhas='redondas', presas='branco', grossura=5.5, pata=1.7, cauda='curta'),
         [('pastar', 'golpe'), ('tromba', 'golpe'), ('carga', 'investida'), ('pisotear', 'pancada_chao')]),
        ('presa_branca', 'quadrupede', dict(G64, cor='branco', cabeca='lobo', manchas='agua', olho='#30e1b9', fx_cor='agua'), ['rugido', 'sopro', 'desaparecer']),
        ('mamute_anciao_tundra', 'quadrupede', dict(G128, cor='castanho', cabeca='urso', orelhas='redondas', presas='branco', grossura=5.8, pata=1.8,
                                                    cauda='curta', manchas='musgo'), ['pancada_chao', 'investida']),
    ],
    guardioes=[
        ('morsa_gigante', 'quadrupede', dict(G64, cor='castanho', cabeca='urso', orelhas=None, presas='branco', grossura=5.5, pata=0.9, altura=0.6, cauda='curta'),
         ['investida', 'pancada_chao', 'golpe']),
        ('alce_fantasma', 'quadrupede', dict(G48, cor='branco', cabeca='cavalo', chifres='agua', altura=1.3, orelhas='pontiagudas', olho='#30e1b9', desfaz=True),
         ['investida', 'desaparecer', 'magia']),
        ('kraken_do_gelo', 'aquatico', dict(G64, tipo='polvo', cor='agua', olho='#f9c22b', fx_cor='branco'), ['golpe', 'area', 'enterrar']),
        ('coracao_de_cristal_azul', 'objeto', dict(G48, tipo='coracao', cor='agua', cor2='branco', fx_cor='agua'), ['area', 'magia', 'escudo']),
        ('wendigo', 'bipede', dict(G48, cor='agua', cabeca='caveira', chifres='branco', roupa='agua', costelas=True, mao='branco', fx_cor='agua'),
         ['golpe', 'rugido', 'desaparecer']),
        ('tartaruga_glaciar', 'quadrupede', dict(G64, cor='verde_esc', cabeca='reptil', grossura=5.2, pata=1.6, altura=0.7, cauda='curta', orelhas=None,
                                                 cristais=['branco', 'agua']), ['escudo', 'pancada_chao', 'sopro']),
        ('raposa_aurora', 'quadrupede', dict(G48, cor='branco', cabeca='lobo', cauda='grossa', barriga='branco', manchas='lilas', olho='#30e1b9', fx_cor='lilas'),
         ['magia', 'desaparecer', 'sopro']),
        ('cavaleiro_de_gelo', 'objeto', dict(G48, tipo='armadura', cor='agua', arma='espada', olho='#ffffff'), ['golpe', 'investida', 'escudo']),
    ],
    bosses=[
        ('yeti_anciao', 'bipede', dict(G64, cor='branco', cabeca='focinho', corpulento=3, roupa='branco', mao='agua', olho='#30e1b9', fx_cor='agua'),
         BOSS6, 'especial'),
        ('dragao_de_gelo', 'quadrupede', dict(G128, cor='agua', cor2='branco', cabeca='reptil', asas='branco', chifres='agua', espinhos='branco',
                                              barriga='branco', cauda='grossa', orelhas=None, olho='#ffffff', fx_cor='agua'), BOSS9, 'especial'),
        ('rei_do_inverno_esquecido', 'bipede', dict(G64, cor='agua', cabeca='caveira', coroa='agua', capa='azul', roupa='azul', arma='espada',
                                                    arma_cor='agua', fx_cor='agua'), ['area', 'invocar', 'golpe', 'onda'], 'especial'),
    ],
    animais=[
        ('pinguim', 'bipede', dict(cor='preto', roupa='branco', pernas='amarelo', k=0.55), []),
        ('lobo_de_gelo_montada', 'quadrupede', dict(G48, cor='branco', cabeca='lobo', barriga='agua', olho='#30e1b9'), []),
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
