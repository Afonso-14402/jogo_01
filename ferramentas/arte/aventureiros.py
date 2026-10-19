"""Os companheiros novos (docs/NPCS.md, secções 4.1 e 4.2): os 12 aventureiros da Guilda e os 8 escondidos na torre.
Sprites 32x32 (parado e andar, 3 direções) + retratos. Saída: arte/npcs/ e arte/retratos/.

Uso: python3 ferramentas/arte/aventureiros.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from humano import animacoes
from motor import guardar

ESTILOS = {
    # escudeiro de 19 anos: armadura de ferro curta e capa azul da Guilda
    'duarte': dict(cabelo='curto', cor_cabelo='castanho', roupa='ferro', calcas='cinza', botas='ferro', capa='azul',
                   largo=1, cinto='couro'),
    # caçadora calada: verde-musgo, capuz castanho
    'leonor': dict(cabelo='rabo', cor_cabelo='preto', pele='morena', roupa='musgo', calcas='castanho', botas='couro',
                   acessorios=[('capuz', 'castanho')]),
    # aprendiz da Igreja: túnica branca com saia azul, como a Célia
    'sancha': dict(cabelo='comprido', cor_cabelo='loiro', roupa='branco', saia='azul', calcas='azul', cinto='ouro',
                   acessorios=['sardas']),
    # pescador que pegou na lança: lenço vermelho e chapéu de palha
    'vasco': dict(cabelo='espetado', cor_cabelo='ruivo', pele='clara', roupa='agua', calcas='castanho', lenco='vermelho',
                  barba='curta', acessorios=['cicatriz']),
    # --- os que aparecem na Guilda à medida que sobes ---
    'bruna': dict(cabelo='rabo', cor_cabelo='ruivo', largo=2, bracos=0.6, roupa='couro', calcas='castanho', botas='couro',
                  acessorios=['cicatriz']),
    'simao': dict(cabelo='tapado', acessorios=[('capuz', 'verde_esc')], roupa='verde_esc', calcas='preto', cinto='couro'),
    'ines': dict(cabelo='comprido', cor_cabelo='preto', roupa='vermelho', saia='vermelho', calcas='vermelho', cinto='ouro',
                 acessorios=[('chapeu_pena', 'vermelho')]),
    'gaspar': dict(cabelo='careca', barba='trancas', cor_cabelo='cinzento', baixo=3, largo=2, bracos=0.6, roupa='ferro',
                   calcas='cinza', botas='ferro', cinto='couro'),
    'matilde': dict(cabelo='curto', cor_cabelo='castanho', roupa='castanho', calcas='verde', botas='couro',
                    acessorios=['oculos_testa', 'sardas']),
    'henrique': dict(cabelo='rabo', cor_cabelo='preto', roupa='roxo', calcas='preto', cinto='preto', lenco='roxo'),
    'beatriz': dict(cabelo='tapado', acessorios=[('lenco_cabeca', 'laranja')], pele='morena', roupa='laranja',
                    calcas='laranja', cinto='castanho'),
    'lourenco': dict(cabelo='comprido', cor_cabelo='branco', pele='palida', roupa='preto', capa='preto', calcas='preto'),
    # --- os escondidos (cada um com uma habilidade especial) ---
    'bartolomeu': dict(cabelo='careca', barba='longa', cor_cabelo='branco', roupa='musgo', saia='castanho', calcas='castanho',
                       acessorios=[('chapeu_palha', 'castanho')]),
    'pim': dict(cabelo='espetado', cor_cabelo='ruivo', baixo=4, roupa='preto', calcas='preto', lenco='amarelo',
                olhos_cor='#9cdb43', acessorios=[('capuz', 'laranja')]),
    'ze_sapo': dict(pele='verde', cabelo='careca', acessorios=['sapo', ('fita', '#ea4f36')], largo=1, roupa='branco',
                    calcas='preto', cinto='preto'),
    'golias': dict(cabelo='curto', cor_cabelo='castanho', largo=3, bracos=0.8, perna=2.0, roupa='cinza', calcas='castanho',
                   pele='morena', acessorios=['cicatriz']),
    'cronos': dict(cabelo='curto', cor_cabelo='cinzento', barba='bigode', roupa='azul', calcas='cinza', capa='azul',
                   acessorios=['oculos']),
    'brasa': dict(asas='vermelho', cabelo='comprido', cor_cabelo='ruivo', roupa='laranja', saia='vermelho',
                  olhos_cor='#f9c22b'),
    'kage': dict(fantasma=True, pele='palida', cabelo='tapado', acessorios=[('capuz', 'preto')], roupa='preto',
                 calcas='preto', botas='preto'),
    'estrela': dict(asas='branco', cabelo='curto', cor_cabelo='azul', baixo=5, pele='palida', roupa='branco', saia='azul',
                    olhos_cor='#f9c22b'),
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
    print('ok', len(ESTILOS), 'companheiros + retratos')
