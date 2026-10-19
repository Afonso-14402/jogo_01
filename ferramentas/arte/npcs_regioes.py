"""NPCs das povoações das regiões 2 a 10 (sprites 32x32: parado e andar, 3 direções) + retratos.
Fichas: docs/regioes/rXX_*.md, secção 7. Saída: arte/npcs/ e arte/retratos/.

Uso: python3 ferramentas/arte/npcs_regioes.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from humano import animacoes
from motor import guardar


def anao(**k):
    return dict(dict(baixo=3, largo=2, bracos=0.6, cinto='couro'), **k)


def fungoide(cap, **k):
    return dict(dict(cabelo='careca', pele='palida', baixo=5, acessorios=[('chapeu_cogumelo', cap)], roupa='castanho',
                     calcas='castanho'), **k)


def lagarto(**k):
    return dict(dict(pele='verde', cabelo='espetado', cor_cabelo='verde', olhos_cor='#f9c22b', calcas='castanho'), **k)


def sapo(**k):
    return dict(dict(pele='verde', cabelo='careca', acessorios=['sapo'], largo=1, calcas='verde'), **k)


def fantasma(**k):
    return dict(dict(pele='palida', fantasma=True, calcas='branco', botas='branco'), **k)


def sereia(cauda, **k):
    return dict(dict(cauda_peixe=cauda), **k)


def alado(**k):
    return dict(dict(asas='branco'), **k)


ESTILOS = {
    # ---------- Região 2: Cavernas ----------
    'hilda_fundo_rocha': anao(cabelo='rabo', cor_cabelo='ruivo', roupa='castanho', avental='couro', calcas='cinza'),
    'pedrito': dict(cabelo='curto', cor_cabelo='castanho', baixo=1, roupa='cinza', avental='couro', calcas='castanho'),
    'dona_graca': dict(cabelo='carrapito', cor_cabelo='cinzento', largo=1, roupa='rosa', avental='branco', saia='rosa'),
    'senhor_ruivo': dict(cabelo='careca', barba='longa', cor_cabelo='ruivo', roupa='castanho', calcas='cinza',
                         acessorios=['oculos', 'cicatriz']),
    'anciao_gorro_azul': fungoide('azul', barba='longa', cor_cabelo='branco'),
    'pila': fungoide('laranja', roupa='verde'),
    'mestre_lamela': fungoide('lilas', roupa='roxo', acessorios=[('chapeu_cogumelo', 'lilas'), 'oculos']),
    'bolota': fungoide('amarelo', baixo=6, roupa='verde'),
    'grimbold': fantasma(**anao(cabelo='careca', barba='trancas', cor_cabelo='branco', roupa='agua', calcas='agua')),
    'ferreiro_fantasma': fantasma(**anao(cabelo='curto', barba='curta', cor_cabelo='branco', roupa='agua', avental='cinza')),
    # ---------- Região 3: Pântano ----------
    'chefe_ssark': lagarto(largo=1, roupa='couro', acessorios=['cicatriz'], capa='vermelho'),
    'xama_ilssa': lagarto(roupa='roxo', saia='roxo', acessorios=[('fita', '#f9c22b')]),
    'kesh': lagarto(roupa='couro', calcas='castanho'),
    'zith': lagarto(roupa='laranja', saia='castanho', acessorios=[('lenco_cabeca', 'laranja')]),
    'barao_coaxim': sapo(largo=3, roupa='roxo', capa='vermelho', acessorios=['sapo', ('coroa', 'ouro')]),
    'ra_ra': sapo(roupa='agua', acessorios=['sapo', ('chapeu_palha', 'amarelo')]),
    'doutor_girino': sapo(roupa='branco', acessorios=['sapo', 'oculos']),
    'sapo_cantor': sapo(roupa='verde_esc', lenco='vermelho'),
    'vera_liana': dict(cabelo='rabo', cor_cabelo='castanho', roupa='verde_esc', calcas='castanho', cinto='couro',
                       acessorios=['oculos_testa', 'lapis']),
    'tom_tirolesa': dict(cabelo='curto', cor_cabelo='loiro', barba='curta', largo=1, roupa='laranja', calcas='castanho',
                         cinto='couro'),
    'irma_nara': dict(cabelo='tapado', acessorios=[('lenco_cabeca', 'branco')], roupa='branco', saia='azul'),
    # ---------- Região 4: Deserto ----------
    'sultana_amira': dict(pele='morena', cabelo='comprido', cor_cabelo='preto', roupa='ouro', saia='vermelho',
                          acessorios=[('coroa', 'ouro')]),
    'mestre_rahim': dict(pele='morena', cabelo='careca', barba='bigode', cor_cabelo='branco', roupa='castanho',
                         acessorios=[('lenco_cabeca', 'branco')], calcas='branco'),
    'faisal': dict(pele='morena', cabelo='curto', barba='curta', cor_cabelo='preto', roupa='roxo', calcas='amarelo',
                   acessorios=[('lenco_cabeca', 'roxo')], largo=1),
    'layla': dict(pele='morena', cabelo='comprido', cor_cabelo='preto', roupa='rosa', saia='rosa', acessorios=[('fita', '#f9c22b')]),
    'velho_omar': dict(pele='morena', cabelo='careca', barba='longa', cor_cabelo='branco', roupa='castanho', saia='castanho'),
    'ferreira_nadia': dict(pele='morena', cabelo='rabo', cor_cabelo='preto', roupa='vermelho', avental='couro', calcas='castanho'),
    'encarregado_bilal': dict(pele='escura', cabelo='careca', largo=2, roupa='branco', calcas='agua'),
    'professora_iris': dict(cabelo='carrapito', cor_cabelo='cinzento', roupa='castanho', calcas='castanho',
                            acessorios=['oculos', ('chapeu_palha', 'castanho')]),
    'beto': dict(pele='morena', cabelo='curto', cor_cabelo='castanho', roupa='laranja', calcas='castanho', cinto='couro'),
    'guarda_sami': dict(pele='escura', cabelo='curto', cor_cabelo='preto', roupa='ferro', calcas='castanho', capa='amarelo'),
    'ancia_sahra': dict(pele='morena', cabelo='comprido', cor_cabelo='branco', roupa='azul', saia='azul',
                        acessorios=[('lenco_cabeca', 'azul')]),
    'tarik': dict(pele='morena', cabelo='espetado', cor_cabelo='preto', roupa='amarelo', calcas='castanho', lenco='vermelho'),
    'mina': dict(pele='morena', cabelo='rabo', cor_cabelo='castanho', roupa='lilas', saia='laranja'),
    # ---------- Região 5: Gelo ----------
    'ulf_barba_gelo': dict(cabelo='curto', barba='longa', cor_cabelo='branco', largo=2, roupa='cinza', capa='castanho',
                           calcas='castanho'),
    'sigrid': dict(cabelo='rabo', cor_cabelo='loiro', roupa='vermelho', saia='branco'),
    'erik_treno': dict(cabelo='curto', barba='curta', cor_cabelo='ruivo', roupa='azul', calcas='castanho',
                       acessorios=[('capuz', 'castanho')]),
    'velha_astrid': dict(cabelo='carrapito', cor_cabelo='branco', baixo=1, roupa='lilas', saia='roxo', lenco='rosa'),
    'leif': dict(cabelo='curto', cor_cabelo='loiro', baixo=5, roupa='vermelho', calcas='azul', lenco='amarelo'),
    'cacadora_inga': dict(cabelo='rabo', cor_cabelo='prateado', roupa='castanho', calcas='castanho', capa='branco',
                          acessorios=['cicatriz']),
    'gunnar': dict(cabelo='careca', barba='trancas', cor_cabelo='ruivo', largo=2, roupa='couro', calcas='castanho'),
    'helka': dict(cabelo='comprido', cor_cabelo='loiro', roupa='verde_esc', calcas='castanho'),
    'sven': dict(cabelo='espetado', cor_cabelo='loiro', roupa='azul', calcas='cinza', capa='branco'),
    'olaf': dict(cabelo='curto', barba='bigode', cor_cabelo='castanho', largo=1, roupa='vermelho', calcas='castanho'),
    'mestre_kael': dict(cabelo='careca', barba='longa', cor_cabelo='branco', roupa='laranja', saia='laranja'),
    'monge_tenzin': dict(cabelo='careca', baixo=1, roupa='laranja', saia='vermelho'),
    'irma_noor': dict(pele='morena', cabelo='tapado', acessorios=[('lenco_cabeca', 'azul'), 'oculos'], roupa='azul', saia='azul'),
    # ---------- Região 6: Oceano ----------
    'capita_marisa': dict(cabelo='rabo', cor_cabelo='ruivo', roupa='vermelho', calcas='preto', capa='azul', botas='preto',
                          acessorios=['cicatriz', ('chapeu_pena', 'preto')]),
    'joaquim_lobo_do_mar': dict(cabelo='careca', barba='longa', cor_cabelo='cinzento', roupa='azul', calcas='branco',
                                acessorios=['oculos']),
    'tome': dict(pele='morena', cabelo='curto', cor_cabelo='castanho', largo=1, roupa='branco', avental='couro', calcas='castanho'),
    'rosa_taberna': dict(cabelo='carrapito', cor_cabelo='ruivo', largo=1, roupa='rosa', avental='branco', saia='castanho'),
    'tiago': dict(pele='morena', cabelo='espetado', cor_cabelo='preto', baixo=3, roupa='branco', calcas='azul', lenco='vermelho'),
    'ama_kaia': dict(pele='escura', cabelo='comprido', cor_cabelo='preto', roupa='agua', calcas='agua'),
    'ourives_perola': dict(cabelo='carrapito', cor_cabelo='prateado', roupa='rosa', saia='branco', acessorios=['oculos']),
    'velho_nalu': dict(pele='escura', cabelo='careca', barba='longa', cor_cabelo='branco', roupa='verde', saia='verde'),
    'rainha_coralina': sereia('agua', cabelo='comprido', cor_cabelo='azul', roupa='rosa', acessorios=[('coroa', 'rosa')]),
    'principe_mare': sereia('azul', cabelo='curto', cor_cabelo='azul', roupa='agua', acessorios=[('coroa', 'ouro')]),
    'nerissa': sereia('verde', cabelo='rabo', cor_cabelo='verde', roupa='cinza', avental='couro'),
    'lirael': sereia('rosa', cabelo='comprido', cor_cabelo='roxo', roupa='lilas'),
    'oceanus': sereia('azul', cabelo='curto', barba='curta', cor_cabelo='verde', largo=2, roupa='ferro'),
    # ---------- Região 7: Vulcão ----------
    'mae_brasa': dict(pele='morena', cabelo='carrapito', cor_cabelo='cinzento', largo=1, roupa='vermelho', saia='castanho'),
    'fuligem': dict(cabelo='espetado', cor_cabelo='preto', baixo=4, roupa='cinza', calcas='preto', acessorios=['sardas']),
    'curandeiro_carvao': dict(pele='escura', cabelo='curto', cor_cabelo='branco', barba='curta', roupa='branco', calcas='cinza'),
    'lena_cinza': dict(cabelo='rabo', cor_cabelo='cinzento', roupa='laranja', avental='branco', calcas='cinza'),
    'hildur_brasa': anao(cabelo='comprido', cor_cabelo='ruivo', roupa='ferro', capa='vermelho', acessorios=[('coroa', 'ouro')]),
    'ragnar_brasa': anao(cabelo='careca', barba='trancas', cor_cabelo='ruivo', roupa='vermelho', avental='couro'),
    'ruby_brasa': anao(cabelo='rabo', cor_cabelo='ruivo', roupa='rosa', acessorios=['oculos'], largo=1),
    'ash': dict(cabelo='curto', cor_cabelo='preto', roupa='cinza', calcas='castanho', acessorios=['sardas', 'oculos_testa']),
    'senhor_vapor': dict(cabelo='careca', barba='bigode', cor_cabelo='branco', baixo=5, roupa='verde', calcas='castanho',
                         acessorios=['oculos_testa', ('chapeu_pena', 'verde')]),
    'massagista_lava': dict(pele='morena', cabelo='careca', largo=3, bracos=0.8, roupa='branco', calcas='vermelho'),
    'gil': dict(cabelo='curto', cor_cabelo='loiro', roupa='amarelo', calcas='azul', acessorios=['oculos', ('chapeu_palha', 'amarelo')]),
    'cozinheira_fumarola': dict(pele='morena', cabelo='tapado', largo=1, roupa='laranja', avental='branco', saia='castanho',
                                acessorios=[('lenco_cabeca', 'vermelho')]),
    # ---------- Região 8: Reino Assombrado ----------
    'burgomestre_aldous': fantasma(cabelo='careca', barba='bigode', cor_cabelo='cinzento', roupa='roxo', capa='preto',
                                   acessorios=[('chapeu_pena', 'preto')]),
    'mortimer': fantasma(cabelo='curto', cor_cabelo='cinzento', roupa='cinza', avental='lilas', acessorios=['oculos']),
    'elise': fantasma(cabelo='comprido', cor_cabelo='loiro', baixo=5, roupa='lilas', saia='lilas', acessorios=[('fita', '#f04f78')]),
    'hugo': fantasma(cabelo='curto', cor_cabelo='castanho', largo=2, roupa='branco', avental='branco'),
    'abadessa_lumina': dict(cabelo='tapado', acessorios=[('lenco_cabeca', 'branco')], roupa='branco', saia='ouro', capa='amarelo'),
    'irmao_bento': dict(cabelo='careca', barba='curta', cor_cabelo='castanho', largo=1, roupa='castanho', avental='couro'),
    'irma_clara': dict(cabelo='tapado', acessorios=[('lenco_cabeca', 'azul')], roupa='azul', saia='azul'),
    'cacador_van': dict(cabelo='comprido', cor_cabelo='preto', barba='curta', roupa='preto', capa='vermelho', calcas='preto',
                        acessorios=['cicatriz', ('chapeu_palha', 'preto')]),
    # ---------- Região 9: Céu ----------
    'imperatriz_celestia': alado(cabelo='comprido', cor_cabelo='loiro', roupa='branco', saia='ouro', acessorios=[('coroa', 'ouro')]),
    'zefiro': alado(cabelo='espetado', cor_cabelo='prateado', roupa='agua', calcas='branco'),
    'nimbo': alado(cabelo='curto', cor_cabelo='branco', barba='bigode', largo=1, roupa='azul', acessorios=['oculos_testa']),
    'brisa': alado(cabelo='rabo', cor_cabelo='azul', roupa='verde', saia='agua'),
    'cumulo': alado(cabelo='curto', cor_cabelo='cinzento', roupa='branco', avental='cinza'),
    'pena': alado(asas='amarelo', cabelo='curto', cor_cabelo='loiro', baixo=5, roupa='azul', calcas='branco'),
    'ferreira_icara': alado(cabelo='rabo', cor_cabelo='ruivo', roupa='laranja', avental='couro', acessorios=['oculos_testa']),
    'astronoma_vega': dict(cabelo='comprido', cor_cabelo='roxo', roupa='roxo', saia='azul', capa='azul', acessorios=['oculos']),
    'orion': dict(pele='morena', cabelo='curto', cor_cabelo='preto', roupa='azul', calcas='cinza', acessorios=['oculos_testa']),
    'velho_altair': dict(cabelo='careca', barba='longa', cor_cabelo='branco', roupa='roxo', saia='roxo', acessorios=['cicatriz']),
    # ---------- Região 10: Abismo ----------
    'sargento_bruma': dict(cabelo='curto', cor_cabelo='cinzento', roupa='ferro', calcas='cinza', capa='azul', acessorios=['cicatriz']),
    'dorn': dict(cabelo='careca', barba='curta', cor_cabelo='preto', largo=2, roupa='couro', avental='couro', acessorios=['cicatriz']),
    'mae_dois': dict(cabelo='carrapito', cor_cabelo='branco', roupa='cinza', saia='cinza', capa='preto'),
    'rafa': dict(cabelo='espetado', cor_cabelo='castanho', roupa='vermelho', calcas='azul', lenco='preto'),
    'doutor_perdido': dict(cabelo='curto', cor_cabelo='cinzento', roupa='branco', calcas='cinza', acessorios=['oculos']),
    'nina': dict(cabelo='rabo', cor_cabelo='preto', baixo=1, roupa='cinza', calcas='preto'),
    'o_desistente': dict(cabelo='comprido', cor_cabelo='preto', roupa='preto', capa='preto', calcas='preto',
                         acessorios=[('capuz', 'preto')]),
    'bia': dict(cabelo='curto', cor_cabelo='ruivo', roupa='verde', saia='verde'),
    'velho_ulisses': dict(cabelo='careca', barba='longa', cor_cabelo='cinzento', roupa='castanho', calcas='castanho'),
    'lino': dict(cabelo='curto', cor_cabelo='loiro', baixo=5, roupa='azul', calcas='cinza'),
    'lia': dict(cabelo='rabo', cor_cabelo='loiro', baixo=5, roupa='rosa', saia='rosa'),
    'chico_memorias': dict(cabelo='curto', cor_cabelo='castanho', barba='bigode', largo=1, roupa='laranja', capa='castanho',
                           acessorios=[('chapeu_pena', 'castanho')]),
    'arquivista': dict(cabelo='comprido', cor_cabelo='prateado', roupa='roxo', saia='roxo', capa='lilas', acessorios=['oculos']),
}


if __name__ == '__main__':
    pasta = os.path.join('arte', 'npcs')
    for nome, est in ESTILOS.items():
        guardar(pasta, nome, animacoes(est))
    import retratos
    pasta_r = os.path.join('arte', 'retratos')
    for nome, e in ESTILOS.items():
        for em in retratos.EMOCOES:
            retratos.retrato(e, em).save(os.path.join(pasta_r, f'{nome}_{em}.png'))
    print('ok', len(ESTILOS), 'NPCs + retratos')
