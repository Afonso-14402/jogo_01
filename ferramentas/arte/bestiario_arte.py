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
        ('rei_anao_esquecido', 'bipede', dict(G64, cor='agua', roupa='agua', cabelo='branco', barba='branco', coroa='ouro', corpulento=2, arma='machado',
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

# ======================= Região 6 — Oceano e Ilhas =======================
REGIOES[6] = dict(
    pasta='r06_oceano',
    monstros=[
        ('caranguejo_gigante', 'aracnideo', dict(G48, tipo='caranguejo', cor='vermelho', pincas=True, pernas=6, fx_cor='agua'),
         [('andar_de_lado', 'investida'), ('pinca', 'golpe'), ('bolhas', 'sopro'), ('esconder', 'escudo')]),
        ('sereia_sombria', 'bipede', dict(cor='lilas', roupa='roxo', cauda_peixe='verde_esc', cabelo='preto', fx_cor='lilas', olho='#e83b3b'),
         [('cantar', 'magia'), ('mergulhar', 'enterrar')]),
        ('homem_tubarao', 'bipede', dict(cor='azul', cabeca='tubarao', roupa='azul', pernas='azul', olho='#2e222f'),
         [('saltar', 'salto'), ('dentada', 'golpe'), ('investida', 'investida')]),
        ('pirata_esqueleto', 'bipede', dict(cor='branco', cabeca='caveira', costelas=True, roupa='vermelho', chapeu='preto', arma='espada'),
         [('sabre', 'golpe'), ('pistola', 'atirar'), ('atirar_bomba', 'atirar')]),
        ('polvo', 'aquatico', dict(G48, tipo='polvo', cor='roxo', olho='#f9c22b', fx_cor='preto'),
         [('camuflado', 'desaparecer'), ('tentaculos', 'golpe'), ('tinta', 'sopro')]),
        ('alforreca_eletrica', 'aquatico', dict(tipo='alforreca', cor='amarelo', fx_cor='amarelo'), [('brilhar', 'magia'), ('choque', 'area')]),
        ('peixe_lanterna', 'aquatico', dict(tipo='peixe', cor='preto', lanterna='amarelo', dentes=True, olho='#f9c22b'), [('isca', 'magia'), ('dentada', 'golpe')]),
        ('serpente_marinha_jovem', 'serpente', dict(G64, cor='azul', segmentos=7, asas='agua', agua=True, olho='#f9c22b', fx_cor='agua'),
         [('emergir', 'levantar'), ('mordida', 'golpe'), ('constricao', 'area'), ('jato', 'sopro')]),
        ('caranguejo_rei_pinca_de_ouro', 'aracnideo', dict(G64, tipo='caranguejo', cor='ouro', pincas=True, pinca_cor='amarelo', pernas=6),
         ['golpe', 'escudo', 'investida']),
        ('barba_lodo', 'bipede', dict(cor='agua', roupa='verde_esc', cabelo='verde', chapeu='preto', arma='espada', desfaz=True, olho='#30e1b9'),
         ['golpe', 'invocar', 'desaparecer']),
    ],
    guardioes=[
        ('tartaruga_marinha_ancia', 'quadrupede', dict(G64, cor='verde', cabeca='reptil', grossura=5.5, pata=1.6, altura=0.7, cauda='curta', orelhas=None,
                                                       cristais=['verde', 'amarelo']), ['escudo', 'onda', 'invocar']),
        ('gaivota_gigante_ladra', 'voador', dict(G48, cor='branco', asa='penas', asa_cor='cinza', bico='amarelo', crista='vermelho', pernas='amarelo'),
         ['investida', 'atirar', 'rugido']),
        ('o_imediato_fantasma', 'bipede', dict(G64, cor='agua', roupa='azul', corpulento=2, chapeu='preto', arma='clava', arma_cor='ferro', desfaz=True,
                                               olho='#30e1b9'), ['pancada_chao', 'golpe', 'invocar']),
        ('peixe_leao_rei', 'aquatico', dict(G48, tipo='peixe', cor='laranja', barbatana='vermelho', espinhos='branco'), ['golpe', 'area', 'investida']),
        ('dragao_marinho_folhado', 'serpente', dict(G64, cor='amarelo', segmentos=6, asas='verde', chifres='verde', agua=True), ['sopro', 'desaparecer', 'onda']),
        ('golem_de_coral', 'bipede', dict(G64, cor='rosa', cabeca='bloco', corpulento=2, cristais=['branco', 'rosa'], olho='#30e1b9', mao='rosa'),
         ['golpe', 'pancada_chao', 'escudo']),
        ('tamboril_abissal', 'aquatico', dict(G64, tipo='peixe', cor='preto', lanterna='agua', dentes=True, olho='#30e1b9'), ['magia', 'golpe', 'investida']),
        ('guardiao_das_mares', 'bipede', dict(G48, cor='branco', roupa='branco', cauda_peixe='branco', coroa='agua', arma='tridente', arma_cor='agua',
                                              fx_cor='agua', olho='#30e1b9'), ['golpe', 'onda', 'magia']),
    ],
    bosses=[
        ('capitao_esqueleto', 'bipede', dict(G64, cor='branco', cabeca='caveira', costelas=True, roupa='vermelho', chapeu='preto', arma='espada',
                                             fx_cor='laranja'), BOSS6, 'especial'),
        ('leviata', 'serpente', dict(G128, cor='azul', segmentos=8, grossura=3.8, asas='agua', agua=True, olho='#30e1b9', fx_cor='agua'), BOSS9, 'especial'),
        ('almirante_afogado', 'bipede', dict(G64, cor='agua', roupa='azul', chapeu='preto', capa='azul', arma='espada', mao='vermelho', desfaz=True,
                                             fx_cor='agua', olho='#30e1b9'), ['golpe', 'onda', 'invocar', 'area'], 'especial'),
    ],
    animais=[
        ('polvo_bebe', 'aquatico', dict(tipo='polvo', cor='rosa', k=0.6), []),
        ('cavalo_marinho_gigante', 'serpente', dict(G48, cor='amarelo', segmentos=5, grossura=3.0, asas='laranja', chifres='laranja'), []),
    ],
)

# ======================= Região 7 — Vulcão =======================
REGIOES[7] = dict(
    pasta='r07_vulcao',
    monstros=[
        ('salamandra', 'quadrupede', dict(cor='laranja', cabeca='reptil', manchas='preto', pata=1.0, altura=0.6, comprimento=1.1, orelhas=None,
                                          olho='#f9c22b', fx_cor='laranja'),
         [('sair', 'levantar'), ('cuspir', 'sopro'), ('cauda', 'golpe'), ('mergulhar', 'enterrar')]),
        ('elemental_de_fogo', 'amorfo', dict(tipo='elemental', cor='laranja', cor2='amarelo', fx_cor='laranja', olho='#2e222f'),
         [('bola_de_fogo', 'sopro'), ('anel', 'area'), ('apagado', 'dormir'), ('explodir', 'area')]),
        ('diabrete', 'bipede', dict(cor='vermelho', chifres='preto', cauda=True, asas='preto', roupa='vermelho', arma='tridente', k=0.7, olho='#f9c22b',
                                    fx_cor='laranja'),
         [('tridente', 'golpe'), ('atirar', 'atirar'), ('estalar_dedos', 'magia'), ('rir', 'rugido')]),
        ('golem_de_magma', 'bipede', dict(G48, cor='preto', cabeca='bloco', corpulento=2, armadura='laranja', cristais=['laranja'], olho='#f9c22b',
                                          mao='preto', fx_cor='laranja'),
         [('murro', 'golpe'), ('pisada', 'pancada_chao'), ('arrefecer', 'escudo')]),
        ('cao_infernal', 'quadrupede', dict(cor='preto', cabeca='lobo', manchas='laranja', olho='#e83b3b', fx_cor='laranja'),
         [('mordida', 'golpe'), ('sopro', 'sopro')]),
        ('morcego_de_cinza', 'voador', dict(cor='cinza', asa='membrana', orelhas=True, olho='#fb6b1d'), [('mordida', 'investida')]),
        ('escorpiao_de_lava', 'aracnideo', dict(tipo='escorpiao', cor='preto', ferrao='laranja', pincas=True, pinca_cor='laranja', pernas=6),
         [('pincas', 'golpe'), ('ferrao', 'investida'), ('enterrar', 'enterrar')]),
        ('cultista_do_fogo', 'bipede', dict(cor='pele', cabeca='capuz', capuz='vermelho', roupa='vermelho', pernas='preto', arma='cajado', fx_cor='laranja'),
         [('chama', 'sopro'), ('ritual', 'invocar'), ('escudo', 'escudo')]),
        ('tricefalo', 'quadrupede', dict(G64, cor='preto', cabeca='lobo', cabecas=3, cores_cabecas=['laranja', 'cinza', 'vermelho'], manchas='laranja',
                                         olho='#f9c22b', fx_cor='laranja'), ['sopro', 'golpe', 'rugido']),
        ('golem_forjado_n7', 'bipede', dict(G64, cor='preto', cabeca='bloco', corpulento=2, armadura='cinza', olho='#30e1b9', mao='preto'),
         ['golpe', 'pancada_chao', 'escudo']),
        # o Kai no duelo da história (andar 68): o NPC com o corpo de combate
        ('kai_duelo_da_historia', 'bipede', dict(cor='pele', cabelo='preto', roupa='azul', pernas='cinza', pes='preto', arma='espada',
                                                 arma_cor='ferro', capa='azul'), ['golpe', 'investida', 'salto']),
    ],
    guardioes=[
        ('fenix_de_cinza', 'voador', dict(G48, cor='cinza', asa='penas', asa_cor='laranja', cauda_penas='laranja', crista='laranja', bico='amarelo',
                                          fx_cor='laranja'), ['sopro', 'investida', 'levantar']),
        ('serpente_de_lava', 'serpente', dict(G64, cor='preto', segmentos=7, aneis='laranja', chifres='laranja', olho='#f9c22b', fx_cor='laranja'),
         ['sopro', 'enterrar', 'golpe']),
        ('ent_carbonizado', 'planta', dict(G64, tipo='arvore', cor='laranja', caule='preto', olho='#f9c22b', fx_cor='laranja'), ['golpe', 'area', 'invocar']),
        ('escavadora_ana_possuida', 'objeto', dict(G64, tipo='vagoneta', cor='cobre', olho='#e83b3b', fx_cor='laranja'), ['investida', 'sopro', 'enterrar']),
        ('sapo_vulcao', 'quadrupede', dict(G48, cor='vermelho', cabeca='reptil', comprimento=0.7, altura=0.6, pata=1.6, cauda=None, orelhas=None,
                                           cristais=['laranja', 'amarelo'], olho='#f9c22b', fx_cor='laranja'), ['salto', 'sopro', 'area']),
        ('golem_portao_de_obsidiana', 'objeto', dict(G64, tipo='totem', blocos=['preto', 'preto', 'roxo'], olho='#b5a5d5', fx_cor='roxo'),
         ['escudo', 'magia', 'pancada_chao']),
        ('sumo_sacerdote_das_chamas', 'bipede', dict(G48, cor='ouro', cabeca='capuz', capuz='vermelho', roupa='vermelho', coroa='ouro', arma='cajado',
                                                     fx_cor='laranja'), ['magia', 'invocar', 'area']),
    ],
    bosses=[
        ('ferreiro_infernal', 'bipede', dict(G64, cor='vermelho', chifres='cinza', corpulento=2, roupa='couro', armadura='laranja', arma='clava',
                                             arma_cor='ferro', olho='#f9c22b', fx_cor='laranja'), BOSS6, 'especial'),
        ('kai', 'bipede', dict(cor='pele', cabelo='preto', roupa='preto', armadura='azul', pernas='preto', arma='espada', olho='#30e1b9', fx_cor='agua'),
         BOSS6, 'especial'),
        ('tita_de_magma', 'bipede', dict(G128, cor='preto', cabeca='bloco', corpulento=3, coroa='laranja', cristais=['laranja', 'amarelo'],
                                         armadura='laranja', olho='#ffffff', mao='preto', fx_cor='laranja'), BOSS9, 'especial'),
        ('automato_da_forja_primordial', 'bipede', dict(G64, cor='cobre', cabeca='bloco', corpulento=1, armadura='laranja', arma='clava', arma_cor='ferro',
                                                        olho='#f9c22b', fx_cor='laranja'), ['golpe', 'sopro', 'pancada_chao', 'magia'], 'especial'),
    ],
    animais=[
        ('salamandra_estimacao', 'quadrupede', dict(cor='laranja', cabeca='reptil', manchas='preto', pata=1.0, altura=0.6, orelhas=None, k=0.6), []),
        ('salamandra_gigante', 'quadrupede', dict(G48, cor='laranja', cabeca='reptil', manchas='preto', pata=1.2, altura=0.7, comprimento=1.3,
                                                  orelhas=None, cauda='grossa'), []),
    ],
)

# ======================= Região 8 — Reino Assombrado =======================
REGIOES[8] = dict(
    pasta='r08_reino_assombrado',
    monstros=[
        ('fantasma', 'amorfo', dict(tipo='fantasma', cor='branco', fx_cor='lilas'),
         [('gritar', 'rugido'), ('entrar_num_objeto', 'desaparecer')]),
        ('zombie', 'bipede', dict(cor='verde', roupa='castanho', pernas='castanho', cabelo='preto', olho='#e83b3b'),
         [('sair_da_terra', 'levantar'), ('agarrar', 'golpe'), ('morder', 'investida')]),
        ('cavaleiro_esqueleto', 'bipede', dict(cor='branco', cabeca='caveira', roupa='preto', armadura='ferro', arma='espada', escudo='ferro'),
         [('espada', 'golpe'), ('escudo', 'escudo'), ('carga', 'investida'), ('remontar', 'levantar')]),
        ('gargula', 'bipede', dict(G48, cor='cinza', cabeca='focinho', chifres='cinza', asas='cinza', cauda=True, olho='#e83b3b', mao='cinza'),
         [('acordar', 'levantar'), ('mergulho', 'investida'), ('garras', 'golpe'), ('petrificar', 'escudo')]),
        ('vampiro', 'bipede', dict(cor='branco', roupa='preto', pernas='preto', capa='vermelho', cabelo='preto', olho='#e83b3b', fx_cor='vermelho'),
         [('mordida', 'golpe'), ('morcegos', 'invocar'), ('hipnose', 'magia')]),
        ('livro_possuido', 'objeto', dict(tipo='livro', cor='roxo', fx_cor='lilas'), [('morder', 'golpe'), ('feitico', 'magia')]),
        ('banshee', 'amorfo', dict(tipo='fantasma', cor='lilas', fx_cor='lilas', olho='#ffffff'), [('chorar', 'magia'), ('gritar', 'rugido')]),
        ('armadura_viva', 'objeto', dict(G48, tipo='armadura', cor='ferro', arma='lanca', olho='#e83b3b'),
         [('acordar', 'levantar'), ('alabarda', 'golpe'), ('investida', 'investida'), ('escudo', 'escudo')]),
        ('condessa_sangria', 'bipede', dict(cor='branco', roupa='vermelho', pernas='vermelho', cabelo='preto', capa='preto', olho='#e83b3b',
                                            fx_cor='vermelho'), ['magia', 'invocar', 'golpe']),
        ('o_jardineiro', 'bipede', dict(G48, cor='verde', roupa='castanho', chapeu='amarelo', corpulento=2, arma='foice', olho='#e83b3b'),
         ['golpe', 'investida', 'levantar']),
    ],
    guardioes=[
        ('sentinela_da_muralha', 'bipede', dict(G48, cor='agua', roupa='agua', arma='arco', desfaz=True, olho='#ffffff', fx_cor='agua'),
         ['atirar', 'area', 'desaparecer']),
        ('o_pregoeiro_fantasma', 'bipede', dict(G48, cor='agua', roupa='agua', corpulento=3, arma='clava', arma_cor='ouro', desfaz=True, olho='#ffffff',
                                                fx_cor='amarelo'), ['onda', 'rugido', 'golpe']),
        ('coveiro_ghoul', 'bipede', dict(G48, cor='cinza', cabeca='focinho', roupa='castanho', arma='picareta', olho='#f9c22b'), ['golpe', 'enterrar', 'invocar']),
        ('colosso_de_ossos', 'bipede', dict(G64, cor='branco', cabeca='caveira', costelas=True, corpulento=3, roupa='branco'), ['pancada_chao', 'golpe', 'invocar']),
        ('rainha_das_rosas_negras', 'planta', dict(G48, tipo='driade', pele='preto', cor='vermelho', cabelo='vermelho', fx_cor='vermelho'),
         ['magia', 'golpe', 'area']),
        ('anjo_caido_de_vitral', 'bipede', dict(G48, cor='lilas', roupa='azul', asas='amarelo', cristais=['vermelho', 'azul', 'amarelo'], fx_cor='lilas'),
         ['magia', 'area', 'investida']),
        ('carcereiro', 'bipede', dict(G48, cor='pele', cabeca='capuz', capuz='preto', roupa='couro', corpulento=2, arma='clava', arma_cor='ferro'),
         ['golpe', 'pancada_chao', 'atirar']),
        ('comandante_dos_cavaleiros_caidos', 'bipede', dict(G48, cor='preto', cabeca='bloco', roupa='preto', capa='vermelho', arma='espada', escudo='preto',
                                                            olho='#e83b3b'), ['golpe', 'invocar', 'investida']),
    ],
    bosses=[
        ('lich_bibliotecario', 'bipede', dict(G64, cor='branco', cabeca='caveira', roupa='roxo', pernas='roxo', coroa='amarelo', arma='cajado',
                                              fx_cor='lilas'), BOSS6, 'especial'),
        ('rei_sem_coroa', 'bipede', dict(G96, cor='preto', cabeca='bloco', roupa='preto', armadura='ouro', capa='vermelho', arma='espada', olho='#e83b3b',
                                         fx_cor='roxo'), BOSS9, 'especial'),
        ('rainha_sem_rei', 'bipede', dict(G64, cor='agua', roupa='agua', pernas='agua', cabelo='branco', desfaz=True, olho='#ffffff', fx_cor='agua'),
         ['magia', 'invocar', 'onda', 'desaparecer'], 'especial'),
    ],
    animais=[
        ('gato_fantasma', 'quadrupede', dict(cor='lilas', cabeca='felino', k=0.6, desfaz=True), []),
    ],
)

# ======================= Região 9 — Reino do Céu =======================
REGIOES[9] = dict(
    pasta='r09_ceu',
    monstros=[
        ('harpia', 'voador', dict(cor='castanho', asa='penas', cabeca_cor='pele', cauda_penas='castanho', pernas='amarelo'),
         [('garras', 'golpe'), ('penas', 'atirar'), ('agarrar', 'investida')]),
        ('elemental_de_ar', 'amorfo', dict(tipo='nuvem', cor='branco', fx_cor='agua'),
         [('rajada', 'sopro'), ('tornado', 'area'), ('lamina', 'atirar')]),
        ('passaro_trovao', 'voador', dict(G48, cor='azul', asa='penas', crista='amarelo', bico='amarelo', cauda_penas='azul', fx_cor='amarelo'),
         [('ericar', 'escudo'), ('raio', 'magia'), ('mergulho', 'investida')]),
        ('golem_celeste', 'bipede', dict(G48, cor='branco', cabeca='bloco', corpulento=2, armadura='ouro', olho='#30e1b9', mao='branco', fx_cor='agua'),
         [('murro', 'golpe'), ('laser', 'sopro'), ('escudo', 'escudo')]),
        ('anjo_guardiao', 'bipede', dict(cor='pele', roupa='branco', pernas='branco', asas='branco', cabelo='amarelo', arma='lanca', fx_cor='amarelo'),
         [('lanca', 'golpe'), ('curar', 'magia'), ('escudo', 'escudo')]),
        ('valquiria', 'bipede', dict(cor='pele', roupa='ferro', pernas='azul', asas='branco', cabelo='amarelo', arma='lanca', escudo='madeira'),
         [('lanca', 'golpe'), ('subir', 'salto'), ('cair', 'pancada_chao'), ('grito', 'rugido')]),
        ('nuvem_viva', 'amorfo', dict(tipo='nuvem', cor='cinza', fx_cor='agua'), [('chuva', 'area'), ('abraco', 'golpe'), ('trovao', 'magia')]),
        ('serpente_alada', 'serpente', dict(G48, cor='branco', segmentos=6, asas='branco', olho='#30e1b9', fx_cor='branco'),
         [('mordida', 'golpe'), ('constricao', 'area'), ('vento', 'sopro')]),
        ('valquiria_sigrun', 'bipede', dict(cor='pele', roupa='ouro', pernas='azul', asas='ouro', cabelo='amarelo', arma='lanca', arma_cor='amarelo',
                                            fx_cor='amarelo'), ['magia', 'investida', 'pancada_chao']),
        ('tempestade_viva', 'amorfo', dict(G128, tipo='nuvem', cor='cinza', fx_cor='amarelo'), ['area', 'magia', 'sopro']),
    ],
    guardioes=[
        ('baleia_das_nuvens', 'aquatico', dict(G64, tipo='baleia', cor='branco', barriga='agua'), ['onda', 'sopro', 'investida']),
        ('golem_ilha', 'bipede', dict(G64, cor='castanho', cabeca='bloco', corpulento=2, cristais=['verde', 'verde_esc'], olho='#30e1b9', mao='castanho'),
         ['pancada_chao', 'golpe', 'invocar']),
        ('cavaleiro_de_luz_solida', 'objeto', dict(G48, tipo='armadura', cor='amarelo', arma='espada', olho='#ffffff', fx_cor='amarelo'),
         ['golpe', 'magia', 'escudo']),
        ('jardineira_celeste', 'bipede', dict(G48, cor='cobre', cabeca='bloco', roupa='verde', arma='foice', olho='#30e1b9', fx_cor='agua'),
         ['golpe', 'sopro', 'invocar']),
        ('leao_alado_de_marmore', 'quadrupede', dict(G64, cor='branco', cabeca='felino', juba='cinza', asas='branco', olho='#30e1b9'), ['investida', 'rugido', 'salto']),
        ('senhor_dos_trovoes', 'bipede', dict(G48, cor='pele', cabelo='branco', roupa='azul', corpulento=1, arma='clava', arma_cor='amarelo', fx_cor='amarelo'),
         ['pancada_chao', 'magia', 'area']),
        ('monge_do_vento', 'bipede', dict(G48, cor='pele', roupa='laranja', asas='branco', arma='cajado', fx_cor='branco'), ['golpe', 'investida', 'sopro']),
        ('carruagem_do_sol', 'objeto', dict(G64, tipo='carruagem', cor='ouro', cor2='laranja', fx_cor='laranja'), ['investida', 'sopro', 'area']),
    ],
    bosses=[
        ('grifo_real', 'quadrupede', dict(G64, cor='ouro', cabeca='felino', bico='amarelo', asas='ouro', orelhas=None, olho='#f9c22b'), BOSS6, 'especial'),
        ('serafim_caido', 'bipede', dict(G128, cor='branco', roupa='preto', pernas='preto', asas='branco', cabelo='branco', arma='foice', arma_cor='lilas',
                                         olho='#30e1b9', fx_cor='lilas'), BOSS9, 'especial'),
        ('arcanjo_de_bronze', 'bipede', dict(G64, cor='cobre', cabeca='bloco', asas='cobre', arma='lanca', arma_cor='cobre', olho='#30e1b9'),
         ['atirar', 'investida', 'golpe', 'pancada_chao'], 'especial'),
    ],
    animais=[
        ('grifo_bebe', 'quadrupede', dict(cor='ouro', cabeca='felino', bico='amarelo', asas='branco', orelhas=None, k=0.6), []),
        ('grifo', 'quadrupede', dict(G48, cor='ouro', cabeca='felino', bico='amarelo', asas='branco', orelhas=None), []),
    ],
)

# ======================= Região 10 — O Abismo =======================
REGIOES[10] = dict(
    pasta='r10_abismo',
    monstros=[
        ('sombra', 'amorfo', dict(tipo='sombra', cor='preto', olho='#b5a5d5', fx_cor='roxo'),
         [('golpe', 'golpe'), ('afundar_na_sombra', 'enterrar'), ('sair', 'levantar')]),
        ('olho_do_vazio', 'objeto', dict(tipo='olho', cor='roxo', cor2='preto', iris='roxo', fx_cor='roxo'),
         [('olhar', 'sopro'), ('piscar', 'dormir'), ('hipnose', 'magia')]),
        ('devorador_de_estrelas', 'aquatico', dict(G64, tipo='baleia', cor='preto', barriga='roxo', estrelas=True, fx_cor='lilas'),
         [('sugar', 'invocar'), ('mordida', 'golpe')]),
        ('relogio_vivo', 'objeto', dict(tipo='relogio', cor='cobre', fx_cor='agua'),
         [('ponteiros', 'golpe'), ('parar_o_tempo', 'magia'), ('rebobinar', 'desaparecer')]),
        ('anjo_do_vazio', 'bipede', dict(cor='preto', roupa='roxo', pernas='roxo', asas='roxo', arma='lanca', arma_cor='lilas', olho='#ffffff', fx_cor='roxo'),
         [('lanca', 'golpe'), ('buraco_negro', 'invocar'), ('selo', 'magia')]),
        ('fragmento_de_mundo', 'bipede', dict(G64, cor='verde', cabeca='bloco', corpulento=2, cristais=['agua', 'amarelo', 'branco'], olho='#ffffff', mao='castanho'),
         [('pisao', 'pancada_chao'), ('lancar', 'atirar'), ('trocar', 'desaparecer')]),
        ('devorador_ancestral', 'aquatico', dict(G128, tipo='baleia', cor='preto', barriga='roxo', estrelas=True, fx_cor='lilas'), ['invocar', 'golpe', 'area']),
        ('jogador_sem_numero', 'bipede', dict(cor='branco', roupa='cinza', pernas='preto', capa='azul', arma='espada', olho='#2e222f'),
         ['golpe', 'desaparecer', 'magia']),
    ],
    guardioes=[
        ('porteiro_do_vazio', 'bipede', dict(G48, cor='preto', cabeca='capuz', capuz='roxo', roupa='roxo', arma='cajado', fx_cor='lilas'),
         ['magia', 'invocar', 'desaparecer']),
        ('baleia_estelar', 'aquatico', dict(G64, tipo='baleia', cor='azul', barriga='lilas', estrelas=True), ['onda', 'sopro', 'investida']),
        ('rainha_dos_espelhos', 'bipede', dict(G48, cor='agua', roupa='agua', coroa='branco', cristais=['branco', 'agua'], olho='#ffffff', fx_cor='branco'),
         ['magia', 'desaparecer', 'invocar']),
        ('gigante_invertido', 'bipede', dict(G64, cor='pele', cabelo='castanho', roupa='azul', corpulento=2, invertido=True), ['pancada_chao', 'golpe', 'atirar']),
        ('o_desistente', 'bipede', dict(G48, cor='pele', cabelo='castanho', roupa='ferro', armadura='cinza', arma='espada', escudo='madeira'),
         ['golpe', 'investida', 'escudo']),
        ('indice_vivo', 'objeto', dict(G48, tipo='livro', cor='azul', fx_cor='agua'), ['magia', 'invocar', 'area']),
        ('o_guardiao_da_escada', 'bipede', dict(G64, cor='preto', roupa='roxo', asas='roxo', arma='espada', arma_cor='amarelo', olho='#ffffff', fx_cor='amarelo'),
         ['golpe', 'magia', 'investida']),
    ],
    bosses=[
        ('guardiao_do_tempo', 'objeto', dict(G64, tipo='relogio', cor='cobre', fx_cor='agua'), BOSS6, 'especial'),
        ('administrador', 'bipede', dict(cor='pele', cabelo='branco', roupa='branco', pernas='cinza', olho='#30e1b9', fx_cor='agua'),
         ['magia', 'desaparecer', 'escudo'], 'especial'),
        ('administrador_gigante', 'amorfo', dict(G128, tipo='elemental', cor='azul', cor2='agua', olho='#ffffff', fx_cor='agua'), BOSS9, 'especial'),
        ('o_primeiro_erro', 'amorfo', dict(G64, tipo='sombra', cor='roxo', olho='#30e1b9', fx_cor='lilas'),
         ['desaparecer', 'magia', 'area', 'investida'], 'especial'),
    ],
    animais=[
        ('mini_estrela', 'amorfo', dict(tipo='elemental', cor='amarelo', cor2='branco', k=0.5), []),
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
