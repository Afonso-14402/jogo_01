"""Edifícios das povoações das regiões 2–10 (docs/regioes/rXX_*.md, secção 7), no estilo de cada região.
Usa as texturas da região (kit_regioes.py) e os moldes do kit e dos andares.
Saída: arte/regioes/rXX_*/povoacoes/<povoação>_<peça>.glb

Uso: blenv/bin/python ferramentas/arte/blender/povoacoes.py [região ...] [--previa]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import base3d as B
import kit_regioes as K
import andares_regioes as A


# ---------------- moldes de edifícios ----------------

def casa_plana(p, M, parede='adobe', larg=3.0):
    """Casa de telhado plano (deserto, céu), com parapeito."""
    p.caixa(M[parede], 0, 0, 0, larg, larg, 2.4)
    p.caixa(M[parede], 0, 0, 2.4, larg + 0.2, larg + 0.2, 0.25)
    p.caixa(M['madeira'], 0, -larg / 2 - 0.02, 0, 0.8, 0.06, 1.6)


def casa_cupula(p, M, parede='branco', cupula='cupula_azul'):
    casa_plana(p, M, parede)
    p.bola(M[cupula], 0, 0, 2.6, 1.1, 1.1, 0.9, 1)


def casa_cogumelo(p, M, chapeu='cogumelo', esc=1.6):
    p.cilindro(M['branco'], 0, 0, 0, 0.9 * esc, 0.75 * esc, 2.0 * esc, 10)
    p.bola(M[chapeu], 0, 0, 2.0 * esc, 2.0 * esc, 2.0 * esc, 0.9 * esc, 1, semente=7)
    p.caixa(M['madeira'], 0, -0.85 * esc, 0, 0.7, 0.1, 1.4)
    p.bola(M['luz'], 0.5 * esc, -0.75 * esc, 1.4 * esc, 0.15, 0.1, 0.15, 0)


def casa_coral(p, M):
    p.bola(M['coral'], 0, 0, 1.3, 1.6, 1.6, 1.5, 1, semente=3, irregular=0.12)
    p.caixa(M['madeira'], 0, -1.5, 0, 0.7, 0.2, 1.4)
    for i in range(4):
        a = i * 1.6
        p.cilindro(M['coral'], math.cos(a) * 1.2, math.sin(a) * 1.2, 2.2, 0.15, 0.04, 1.0, 5)


def salao(p, M, parede='troncos', telhado='telhado'):
    """Salão comprido (salão comunal, cantina, estalagem)."""
    p.caixa(M[parede], 0, 0, 0, 4.0, 7.0, 2.6)
    p.telhado(M[telhado], 0, 0, 2.6, 4.4, 7.4, 2.0)
    p.caixa(M['madeira'], 0, -3.52, 0, 1.2, 0.06, 1.9)


def banca(p, M, toldo='tecido'):
    A.mesa(p, M)
    for x in (-0.8, 0.8):
        p.cilindro(M['madeira'], x, 0.4, 0, 0.05, 0.05, 2.2, 4)
    p.caixa(M[toldo], 0, 0.1, 2.2, 1.9, 1.3, 0.08)
    for i in range(3):
        p.caixa(M['destaque'], -0.5 + i * 0.5, 0, 0.85, 0.3, 0.3, 0.2)


def forja(p, M):
    K.braseiro(p, M)
    p.caixa(M['metal'], 1.3, 0, 0, 0.8, 0.5, 0.75)
    p.caixa(M['pedra'], -1.4, 0, 0, 0.9, 0.9, 2.4)


def muralha_portao(p, M, m='pedra'):
    for x in (-2.2, 2.2):
        p.caixa(M[m], x, 0, 0, 2.4, 1.0, 4.0)
    p.caixa(M[m], 0, 0, 3.0, 2.2, 1.0, 1.0)
    p.caixa(M['madeira'], 0, 0.1, 0, 2.0, 0.2, 3.0)


def poco_vila(p, M):
    A.poco(p, M)
    for x in (-0.8, 0.8):
        p.caixa(M['madeira'], x, 0, 0.7, 0.12, 0.12, 1.2)
    p.telhado(M['telhado'], 0, 0, 1.9, 2.0, 1.2, 0.5)


EXTRA = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_')}

# povoação: [(peça, molde, parâmetros)]
POVOACOES = {
    2: {
        'posto_fundo_rocha': [('casa_1', 'casa', {}), ('casa_2', 'casa', dict(parede='pedra')), ('cantina', 'salao', dict(parede='madeira')),
                              ('forja', 'forja', {}), ('monte_minerio', 'rocha', dict(m='minerio', r=1.2, h=0.8))],
        'mycelia': [('casa_cogumelo_1', 'casa_cogumelo', {}), ('casa_cogumelo_2', 'casa_cogumelo', dict(chapeu='cristal_luz', esc=1.2)),
                    ('estalagem_cogumelo', 'casa_cogumelo', dict(esc=2.4)), ('ponte_lamela', 'ponte', dict(m='branco')),
                    ('lago_luminoso', 'agua', dict(m='luz_azul')), ('banca', 'banca', {})],
        'forja_ana': [('fornalha_ana', 'forja', {}), ('coluna_rosto', 'estatua', {}), ('bigorna', 'altar', dict(m='metal', luz='fogo_luz'))],
    },
    3: {
        'aldeia_sssar': [('cabana_1', 'casa', dict(palafita=True, telhado='folhas')), ('cabana_2', 'casa', dict(palafita=True, parede='casca', telhado='folhas_b')),
                         ('totem', 'coluna', dict(m='madeira')), ('canoa', 'barco', {}), ('passadico', 'ponte', dict(corda='madeira'))],
        'vila_coaxa': [('casa_nenufar_1', 'casa_cogumelo', dict(chapeu='nenufar', esc=1.3)), ('casa_nenufar_2', 'casa_cogumelo', dict(chapeu='folhas', esc=1.1)),
                       ('ponte_juncos', 'ponte', dict(m='folhas_b', corda='casca')), ('palco_coro', 'plataforma', {}), ('banca', 'banca', {})],
        'refugio_copas': [('plataforma', 'plataforma', {}), ('cabana_arvore', 'casa', dict(palafita=True)), ('telescopio', 'estatua', dict(m='metal')),
                          ('rede', 'ponte', dict(m='tecido'))],
    },
    4: {
        'oasis_zahra': [('casa_1', 'casa_plana', {}), ('casa_2', 'casa_plana', dict(larg=2.4)), ('palacio', 'casa_cupula', dict(parede='adobe', cupula='ouro')),
                        ('tenda_bazar_1', 'banca', {}), ('tenda_bazar_2', 'tenda', {}), ('banhos', 'salao', dict(parede='adobe', telhado='adobe')),
                        ('palmeira', 'palmeira', {}), ('lagoa', 'agua', dict(m='luz_azul'))],
        'acampamento_escavadores': [('tenda_1', 'tenda', {}), ('tenda_2', 'tenda', dict(tecido='branco')), ('andaime', 'plataforma', {}),
                                    ('mesa_mapas', 'mesa', {})],
        'nomadas_vento': [('tenda_nomada', 'tenda', {}), ('fogueira', 'fogueira', {}), ('cerca_lagartos', 'grade', dict(m='madeira'))],
    },
    5: {
        'pinhal_do_norte': [('casa_troncos_1', 'casa', dict(parede='troncos')), ('casa_troncos_2', 'casa', dict(parede='troncos', telhado='neve')),
                            ('salao_comunal', 'salao', {}), ('sauna', 'casa', dict(parede='troncos', telhado='troncos')),
                            ('treno', 'vagoneta', {})],
        'aldeia_cacadores': [('casa_ruina', 'coluna', dict(m='troncos', partida=True)), ('casa_reconstruida', 'casa', dict(parede='troncos')),
                             ('torre_vigia', 'torre', dict(m='troncos')), ('secador_peles', 'grade', dict(m='madeira'))],
        'mosteiro_aurora': [('mosteiro', 'salao', dict(parede='pedra', telhado='telhado')), ('torre_sino', 'torre', {}),
                            ('cela', 'casa', dict(parede='pedra')), ('sino', 'sino', {})],
    },
    6: {
        'porto_arquipelago': [('casa_palafita_1', 'casa', dict(palafita=True)), ('casa_palafita_2', 'casa', dict(palafita=True, parede='coral_b')),
                              ('taberna', 'salao', dict(parede='naufragio')), ('cais', 'ponte', {}), ('barco', 'barco', {}),
                              ('farol', 'torre', dict(m='branco'))],
        'vila_perolas': [('cabana_palha', 'casa', dict(palafita=True)), ('barco_pequeno', 'barco', {}), ('estendal_colares', 'grade', dict(m='madeira'))],
        'coralina': [('casa_coral_1', 'casa_coral', {}), ('casa_coral_2', 'casa_coral', {}), ('palacio_perola', 'casa_cupula', dict(parede='coral', cupula='branco')),
                     ('cupula', 'cupula', {}), ('forja_abissal', 'forja', {})],
    },
    7: {
        'acampamento_cinzas': [('tenda_cinza_1', 'tenda', dict(tecido='cinza')), ('tenda_cinza_2', 'tenda', dict(tecido='cinza_b')),
                               ('fogueira_grande', 'fogueira', {}), ('mesa_curandeiro', 'mesa', {})],
        'bastiao_obsidiana': [('portao', 'muralha_portao', dict(m='obsidiana')), ('torre', 'torre', dict(m='obsidiana', telhado='obsidiana')),
                              ('salao', 'salao', dict(parede='obsidiana', telhado='obsidiana')), ('forja', 'forja', {})],
        'termas_geiseres': [('piscina', 'poco', {}), ('casa_banhos', 'casa', dict(parede='pedra')), ('geiser', 'geiser', {}),
                            ('espreguicadeira', 'mesa', {})],
    },
    8: {
        'mercado_fantasma': [('banca_1', 'banca', dict(toldo='chao_d')), ('banca_2', 'banca', dict(toldo='telhado')), ('casa_1', 'casa', dict(parede='pedra')),
                             ('casa_2', 'casa', dict(parede='pedra_b')), ('candeeiro', 'lanterna', {})],
        'mosteiro_ordem_luz': [('mosteiro', 'salao', dict(parede='pedra', telhado='telhado')), ('capela', 'casa', dict(parede='pedra')),
                               ('torre', 'torre', {}), ('janela_vitral', 'moldura', dict(m='pedra', vidro='vidro_roxo'))],
    },
    9: {
        'aeropolis': [('casa_1', 'casa_cupula', dict(parede='chao_a', cupula='cupula_azul')), ('casa_2', 'casa_cupula', dict(parede='chao_b', cupula='cupula_azul')),
                      ('palacio', 'casa_cupula', dict(parede='chao_a', cupula='ouro')), ('ilha', 'ilha', dict(topo='relva', r=2.5)),
                      ('ponte_luz', 'ponte', dict(m='luz', corda='luz')), ('forja_oricalco', 'forja', {})],
        'observatorio_celeste': [('observatorio', 'casa_cupula', dict(parede='pedra', cupula='ouro')), ('telescopio', 'estatua', dict(m='ouro')),
                                 ('torre', 'torre', dict(m='pedra', telhado='ouro'))],
    },
    10: {
        'ultimo_posto': [('tenda', 'tenda', {}), ('casa_abandonada', 'casa', dict(parede='pedra')), ('fogueira', 'fogueira', {}),
                         ('bandeira_guilda', 'bandeira', {})],
        'cidade_perdidos': [('casa_numero_1', 'casa', dict(parede='chao_b')), ('casa_numero_2', 'casa', dict(parede='chao_b')),
                            ('relogio_sem_ponteiros', 'relogio_sol', {}), ('praca', 'chao', dict(m='vidro_chao'))],
        'biblioteca_arquivista': [('estante_1', 'estante', {}), ('estante_2', 'estante', {}), ('mesa_leitura', 'mesa', {})],
    },
}


def gerar(n, previa=False):
    B.limpar()
    pasta = os.path.join('arte', 'regioes', K.PASTAS[n], 'povoacoes')
    M = K.materiais(n, os.path.join('arte', 'regioes', K.PASTAS[n], 'kit', 'texturas'))
    M.setdefault('cupula_azul', B.material(f'r{n:02d}_cupula_azul', cor='#4d65b4'))
    M.setdefault('destaque', B.material(f'r{n:02d}_destaque', cor='#f9c22b'))
    M.setdefault('teia', M['branco'])
    M['cogumelo'] = B.material(f'r{n:02d}_cogumelo_casa', B.textura_ruido(f'r{n:02d}_cogumelo_casa', ['#4d65b4', '#4d9be6', '#323353'],
                                                                         os.path.join('arte', 'regioes', K.PASTAS[n], 'kit', 'texturas'),
                                                                         77, manchas=[('#8fd3ff', 5, 1)]))
    for chave in ('adobe', 'troncos', 'obsidiana', 'coral', 'coral_b', 'naufragio', 'relva', 'nenufar', 'folhas_b', 'cinza',
                  'cinza_b', 'chao_d', 'pedra_b', 'vidro_chao', 'ouro', 'minerio'):
        M.setdefault(chave, M.get('pedra'))
    moldes = dict(K.MOLDES, **A.EXTRA, **EXTRA)
    objetos = []
    for pov, pecas in POVOACOES[n].items():
        for nome, molde, kw in pecas:
            p = B.Peca(f'{pov}_{nome}')
            moldes[molde](p, M, **kw)
            i = len(objetos)
            objetos.append(p.criar((i % 6) * 9.0 - 22, (i // 6) * 9.0 - 9))
    B.exportar(objetos, pasta, f'r{n:02d}_povoacoes.blend')
    if previa:
        B.previa(os.path.join(pasta, f'r{n:02d}_povoacoes.png'), distancia=60, alvo=(0, 0, 0))
    print('ok', K.PASTAS[n], len(objetos), 'peças')


if __name__ == '__main__':
    regs = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(POVOACOES)
    for r in regs:
        gerar(r, '--previa' in sys.argv)
