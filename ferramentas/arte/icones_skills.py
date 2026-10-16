"""Ícones das skills (24×24): Skills Únicas, skills das 20 classes, skills de armas e skills de vida.
Lê os nomes de docs/PROGRESSAO.md. Cada ícone = moldura com a cor da família + fundo escuro + um SÍMBOLO
escolhido pelas palavras do nome (espada, escudo, chama, gelo, raio, flecha, caveira, olho, coração...).
As passivas têm a moldura dourada nos cantos. Saída: arte/icones/skills/<id>.png

Uso: python3 ferramentas/arte/icones_skills.py
"""
import math
import os
import re
import unicodedata
from PIL import Image

OUT = '#2e222f'
DOC = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'PROGRESSAO.md')
PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'icones', 'skills')

# família -> (moldura escura, moldura clara, fundo)
FAMILIAS = {
    'unica': ('#9e4539', '#f9c22b', '#45293f'), 'espada': ('#484a77', '#8fd3ff', '#323353'),
    'arco': ('#165a4c', '#91db69', '#313638'), 'magia': ('#6b3e75', '#a884f3', '#2e222f'),
    'tanque': ('#625565', '#c7dcd0', '#3e3546'), 'berserker': ('#6e2727', '#ea4f36', '#2e222f'),
    'arma': ('#694f62', '#ab947a', '#3e3546'), 'vida': ('#239063', '#cddf6c', '#374e4a'),
}
CLASSE_FAMILIA = {'Espadachim': 'espada', 'Cavaleiro': 'espada', 'Paladino': 'espada', 'Mestre de Lâminas': 'espada',
                  'Santo da Espada': 'espada', 'Arqueiro': 'arco', 'Atirador': 'arco', 'Olho de Falcão': 'arco',
                  'Ranger': 'arco', 'Senhor da Floresta': 'arco', 'Mago': 'magia', 'Arquimago': 'magia',
                  'Sábio dos Elementos': 'magia', 'Necromante': 'magia', 'Rei dos Mortos': 'magia', 'Tanque': 'tanque',
                  'Guardião': 'tanque', 'Fortaleza Viva': 'tanque', 'Berserker': 'berserker', 'Senhor da Guerra': 'berserker'}

COR = {  # cores dos símbolos: (principal, clara, escura)
    'metal': ('#9babb2', '#ffffff', '#625565'), 'fogo': ('#f79617', '#fbff86', '#ea4f36'),
    'gelo': ('#8fd3ff', '#ffffff', '#4d9be6'), 'raio': ('#f9c22b', '#ffffff', '#f79617'),
    'veneno': ('#1ebc73', '#cddf6c', '#239063'), 'luz': ('#fbff86', '#ffffff', '#f9c22b'),
    'sombra': ('#a884f3', '#eaaded', '#6b3e75'), 'sangue': ('#e83b3b', '#f68181', '#b33831'),
    'madeira': ('#ab947a', '#c7dcd0', '#966c6c'), 'verde': ('#91db69', '#cddf6c', '#239063'),
    'ouro': ('#f9c22b', '#fbff86', '#f79617'), 'pedra': ('#966c6c', '#ab947a', '#694f62'),
    'agua': ('#4d9be6', '#8fd3ff', '#4d65b4'), 'osso': ('#c7dcd0', '#ffffff', '#9babb2'),
}


def _ascii(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')


def _slug(t):
    return re.sub(r'[^a-z0-9]+', '_', _ascii(t)).strip('_')


# ---------------- desenho ----------------

class G:
    """Símbolo numa grelha 24×24: 0 = cor principal, 1 = clara, 2 = escura."""

    def __init__(self):
        self.p = {}

    def put(self, x, y, t=0):
        x, y = int(round(x)), int(round(y))
        if 3 <= x <= 20 and 3 <= y <= 20:
            self.p[(x, y)] = t

    def linha(self, x0, y0, x1, y1, t=0, larg=1):
        n = int(max(abs(x1 - x0), abs(y1 - y0)) * 2) + 1
        for i in range(n + 1):
            x, y = x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n
            for a in range(larg):
                for b in range(larg):
                    self.put(x + a - larg // 2, y + b - larg // 2, t)

    def disco(self, cx, cy, r, t=0, luz=True):
        for y in range(int(cy - r) - 1, int(cy + r) + 2):
            for x in range(int(cx - r) - 1, int(cx + r) + 2):
                d = math.hypot(x + .5 - cx, y + .5 - cy)
                if d <= r:
                    tt = t
                    if luz and t == 0:
                        tt = 1 if (x - cx) + (y - cy) < -r * 0.6 else 2 if (x - cx) + (y - cy) > r * 0.7 else 0
                    self.put(x, y, tt)

    def poli(self, pts, t=0):
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        for y in range(int(min(ys)), int(max(ys)) + 1):
            for x in range(int(min(xs)), int(max(xs)) + 1):
                px, py = x + .5, y + .5
                dentro = False
                for i in range(len(pts)):
                    (x1, y1), (x2, y2) = pts[i], pts[i - 1]
                    if (y1 > py) != (y2 > py) and px < (x2 - x1) * (py - y1) / (y2 - y1) + x1:
                        dentro = not dentro
                if dentro:
                    self.put(x, y, t)


def s_espada(g):
    g.linha(7, 17, 17, 7, 0, 2); g.linha(8, 15, 16, 7, 1); g.linha(5, 15, 9, 19, 2, 2); g.linha(5, 19, 6, 18, 2, 2)


def s_espadas(g):
    g.linha(5, 18, 18, 5, 0, 2); g.linha(6, 5, 18, 17, 0, 2); g.linha(5, 17, 17, 5, 1)


def s_escudo(g):
    g.poli([(6, 5), (18, 5), (18, 12), (12, 19), (6, 12)], 0); g.linha(12, 6, 12, 17, 1); g.linha(7, 9, 17, 9, 2)


def s_chama(g):
    g.poli([(12, 3), (17, 11), (17, 15), (14, 19), (10, 19), (7, 15), (7, 11), (10, 8)], 0)
    g.poli([(12, 10), (14, 14), (13, 18), (11, 18), (10, 15)], 1)


def s_gelo(g):
    for a in range(3):
        an = a * math.pi / 3
        g.linha(12 - math.cos(an) * 8, 12 - math.sin(an) * 8, 12 + math.cos(an) * 8, 12 + math.sin(an) * 8, 0, 2)
    g.disco(12, 12, 2, 1, luz=False)


def s_raio(g):
    g.poli([(14, 3), (7, 13), (11, 13), (9, 20), (17, 9), (13, 9), (15, 3)], 0); g.linha(13, 5, 9, 12, 1)


def s_flecha(g):
    g.linha(5, 18, 17, 6, 0, 2); g.poli([(18, 5), (13, 6), (17, 10)], 1); g.linha(4, 16, 7, 19, 2); g.linha(6, 16, 4, 18, 2)


def s_flechas(g):
    for d in (-3, 0, 3):
        g.linha(5 + d, 18, 15 + d, 6, 0); g.put(16 + d, 5, 1); g.put(15 + d, 5, 1); g.put(16 + d, 6, 1)


def s_caveira(g):
    g.disco(12, 10, 6, 0); g.poli([(9, 14), (15, 14), (15, 18), (9, 18)], 0)
    for x in (9, 14):
        g.disco(x + 0.5, 10.5, 1.5, 2, luz=False)
    g.put(12, 13, 2); g.put(12, 14, 2)
    for x in (10, 12, 14):
        g.put(x, 17, 2)


def s_olho(g):
    for x in range(4, 21):
        h = 5 * math.sin(math.pi * (x - 4) / 16)
        for y in range(int(12 - h), int(12 + h) + 1):
            g.put(x, y, 1)
    g.disco(12, 12, 3.5, 0); g.disco(12, 12, 1.5, 2, luz=False); g.put(11, 11, 1)


def s_coracao(g):
    g.disco(9, 10, 3.5, 0); g.disco(15, 10, 3.5, 0); g.poli([(5.5, 11), (18.5, 11), (12, 19)], 0); g.put(8, 8, 1); g.put(9, 8, 1)


def s_cruz(g):
    g.poli([(10, 5), (14, 5), (14, 10), (19, 10), (19, 14), (14, 14), (14, 19), (10, 19), (10, 14), (5, 14), (5, 10), (10, 10)], 0)
    g.linha(11, 6, 11, 9, 1)


def s_estrela(g):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = 8 if i % 2 == 0 else 3.5
        pts.append((12 + math.cos(a) * r, 12.5 + math.sin(a) * r))
    g.poli(pts, 0); g.put(11, 9, 1); g.put(12, 8, 1)


def s_lua(g):
    g.disco(12, 12, 7, 0)
    for (x, y) in list(g.p):
        if math.hypot(x + .5 - 15, y + .5 - 10) < 6:
            del g.p[(x, y)]


def s_gota(g):
    g.poli([(12, 4), (17, 13), (7, 13)], 0); g.disco(12, 14, 5, 0); g.put(10, 13, 1); g.put(10, 14, 1)


def s_vento(g):
    for i, (y, l) in enumerate(((8, 12), (12, 15), (16, 10))):
        g.linha(5, y, 5 + l, y, 0 if i != 1 else 1)
        g.put(5 + l + 1, y - 1, 0); g.put(5 + l + 1, y - 2, 0)


def s_rocha(g):
    g.poli([(5, 18), (7, 9), (12, 5), (17, 8), (19, 18)], 0); g.linha(10, 9, 13, 14, 2); g.linha(13, 14, 11, 18, 2); g.linha(8, 10, 11, 7, 1)


def s_martelo(g):
    g.linha(7, 18, 14, 11, 2, 2); g.poli([(11, 4), (19, 12), (16, 15), (8, 7)], 0); g.linha(11, 5, 17, 11, 1)


def s_machado(g):
    g.linha(7, 19, 15, 6, 2, 2); g.poli([(13, 4), (20, 8), (18, 14), (14, 9)], 0); g.linha(15, 5, 19, 8, 1)


def s_lanca(g):
    g.linha(5, 19, 15, 9, 2, 1); g.poli([(14, 8), (19, 4), (17, 11)], 0); g.put(17, 6, 1)


def s_foice(g):
    g.linha(14, 20, 12, 6, 2, 1)
    for k in range(12):
        a = math.pi * (1.0 + k / 16)
        g.put(12 + math.cos(a) * 7 + 6, 7 + math.sin(a) * 3 + (k / 4), 0)
        g.put(12 + math.cos(a) * 7 + 6, 8 + math.sin(a) * 3 + (k / 4), 1)


def s_punho(g):
    g.poli([(7, 8), (17, 8), (18, 15), (15, 19), (8, 19), (6, 14)], 0)
    for x in (9, 12, 15):
        g.linha(x, 8, x, 11, 2)
    g.linha(8, 9, 16, 9, 1)


def s_moeda(g):
    g.disco(12, 12, 7, 0); g.disco(12, 12, 4.5, 2, luz=False); g.disco(12, 12, 3.5, 0); g.put(11, 10, 1)


def s_saco(g):
    g.disco(12, 14, 6, 0); g.poli([(9, 5), (15, 5), (14, 9), (10, 9)], 0); g.linha(9, 8, 15, 8, 2)


def s_bota(g):
    g.poli([(8, 4), (13, 4), (13, 14), (19, 15), (19, 19), (8, 19)], 0); g.linha(9, 5, 9, 14, 1); g.linha(15, 9, 19, 6, 1); g.linha(15, 11, 20, 9, 1)


def s_gema(g):
    g.poli([(7, 9), (10, 5), (14, 5), (17, 9), (12, 19)], 0); g.linha(7, 9, 17, 9, 2); g.poli([(10, 6), (12, 6), (11, 9)], 1)


def s_frasco(g):
    g.poli([(10, 4), (14, 4), (14, 9), (18, 15), (17, 19), (7, 19), (6, 15), (10, 9)], 0)
    g.poli([(7, 14), (17, 14), (17, 18), (7, 18)], 2); g.put(9, 15, 1)


def s_picareta(g):
    g.linha(7, 19, 15, 9, 2, 2)
    for k in range(13):
        a = math.pi * (1.15 + k / 15)
        g.put(14 + math.cos(a) * 7 + 3, 9 + math.sin(a) * 3 + 3, 0)


def s_folha(g):
    g.poli([(5, 18), (8, 9), (14, 5), (19, 5), (18, 11), (14, 16)], 0); g.linha(6, 18, 17, 6, 2)


def s_peixe(g):
    g.disco(11, 12, 5, 0); g.poli([(15, 12), (20, 7), (20, 17)], 0); g.put(8, 11, 2)


def s_tacho(g):
    g.poli([(5, 11), (19, 11), (17, 18), (7, 18)], 0); g.linha(4, 11, 20, 11, 1)
    for x in (9, 12, 15):
        g.linha(x, 4 + (x % 2), x, 8, 1)


def s_bigorna(g):
    g.poli([(4, 8), (19, 8), (17, 11), (14, 11), (15, 16), (18, 18), (6, 18), (9, 16), (10, 11), (6, 11)], 0); g.linha(5, 8, 18, 8, 1)


def s_planta(g):
    g.linha(12, 19, 12, 10, 2); g.poli([(12, 11), (6, 7), (8, 4), (12, 8)], 0); g.poli([(12, 13), (18, 9), (17, 6), (12, 10)], 1)


def s_pata(g):
    g.disco(12, 15, 4, 0)
    for x, y in ((7, 9), (10.5, 6.5), (14, 6.5), (17, 9)):
        g.disco(x, y, 1.8, 0)


def s_engrenagem(g):
    for k in range(8):
        a = k * math.pi / 4
        g.linha(12, 12, 12 + math.cos(a) * 8, 12 + math.sin(a) * 8, 0, 3)
    g.disco(12, 12, 6, 0); g.disco(12, 12, 2, 2, luz=False)


def s_agulha(g):
    g.linha(6, 18, 17, 7, 0, 1); g.put(17, 6, 1); g.put(16, 7, 2)
    for k in range(10):
        g.put(5 + k, 10 + math.sin(k) * 2, 1)


def s_esqueleto_mao(g):
    s_caveira(g)


def s_seta_cima(g):
    g.poli([(12, 4), (19, 11), (15, 11), (15, 19), (9, 19), (9, 11), (5, 11)], 0); g.linha(11, 6, 8, 10, 1)


def s_espiral(g):
    for k in range(60):
        a = k * 0.25
        r = 1 + k * 0.13
        g.put(12 + math.cos(a) * r, 12 + math.sin(a) * r, 0 if k % 6 else 1)


def s_arvore(g):
    g.linha(12, 19, 12, 12, 2, 2); g.disco(12, 9, 6, 0)


SIMBOLOS = [  # (palavras, símbolo, cor) — a primeira que aparecer no nome ganha
    (('lingua', 'conversa'), s_vento, 'ouro'), (('juramento', 'fe ', 'julgamento', 'avatar', 'luz'), s_cruz, 'luz'),
    (('fluxo', 'equilibrio', 'mente', 'concentracao', 'instinto'), s_espiral, 'agua'),
    (('rolar', 'aljava'), s_flecha, 'madeira'), (('ponto fraco', 'sem falhar'), s_olho, 'sangue'),
    (('camuflagem',), s_folha, 'verde'), (('afinidade', 'canalizacao'), s_espiral, 'sombra'),
    (('buraco negro', 'toque sombrio', 'pacto', 'imortal'), s_caveira, 'sombra'),
    (('pele dura', 'corpo de ferro', 'proteger', 'cupula', 'inabalavel', 'bastiao', 'gigante', 'sem dor'), s_escudo, 'metal'),
    (('empurrao', 'contra-ataque', 'imparavel'), s_punho, 'metal'),
    (('fogo', 'ardente', 'meteoro', 'chama', 'brasa', 'inferno', 'queima'), s_chama, 'fogo'),
    (('gelo', 'nevao', 'congel', 'frio', 'geada', 'inverno'), s_gelo, 'gelo'),
    (('raio', 'trovao', 'tempestade', 'relampago', 'eletric'), s_raio, 'raio'),
    (('veneno', 'toxic', 'peste'), s_gota, 'veneno'), (('sangue', 'vampir'), s_gota, 'sangue'),
    (('morte', 'morto', 'necro', 'caveira', 'osso', 'cadaver', 'zombi', 'esquelet', 'alma', 'ceifar', 'decapitar'), s_caveira, 'osso'),
    (('olho', 'visao', 'falcao', 'mira', 'sistema', 'avaliar'), s_olho, 'luz'),
    (('cura', 'vida', 'regener', 'bencao', 'santo', 'sagrad', 'luz divina', 'oracao'), s_cruz, 'luz'),
    (('coracao', 'dragao'), s_coracao, 'sangue'), (('sorte', 'estrela', 'celestial', 'estelar'), s_estrela, 'luz'),
    (('lua',), s_lua, 'luz'), (('vento', 'furacao', 'tornado', 'ciclone'), s_vento, 'gelo'),
    (('terra', 'sismic', 'tremor', 'rocha', 'pedra', 'montanha', 'muralha', 'fortaleza'), s_rocha, 'pedra'),
    (('midas', 'ouro', 'riqueza'), s_moeda, 'ouro'), (('bolsa', 'mochila'), s_saco, 'madeira'),
    (('passo', 'rapid', 'velocidade', 'fantasma', 'esquiv', 'salto', 'corrida', 'teletransport'), s_bota, 'sombra'),
    (('escudo', 'guarda', 'bloque', 'defes', 'protec', 'barreira', 'aguentar', 'firme', 'muro', 'armadura', 'provoc'), s_escudo, 'metal'),
    (('flechas', 'chuva de', 'rajada', 'duplo', 'multipl'), s_flechas, 'madeira'),
    (('flecha', 'tiro', 'disparo', 'arco', 'virote', 'canhao', 'besta', 'atirador', 'cacad', 'emboscada', 'armadilha'), s_flecha, 'madeira'),
    (('martelo',), s_martelo, 'metal'), (('machado', 'arremesso'), s_machado, 'metal'), (('lanca', 'investida'), s_lanca, 'metal'),
    (('foice', 'danca da morte'), s_foice, 'sombra'), (('punho', 'soco', 'combo', 'mil punhos'), s_punho, 'pedra'),
    (('sombra', 'escuro', 'vazio', 'assassin', 'invisiv', 'furtiv'), s_espiral, 'sombra'),
    (('magia', 'arcan', 'mana', 'feitico', 'proibid', 'elementos', 'canalizar', 'invocar', 'portal'), s_espiral, 'sombra'),
    (('furia', 'berserk', 'raiva', 'grito', 'rugido', 'sede', 'massacre', 'guerra'), s_espadas, 'sangue'),
    (('floresta', 'natureza', 'raiz', 'espinho', 'arvore', 'planta'), s_arvore, 'verde'),
    (('companheiro', 'lobo', 'animal', 'besta selvagem', 'domador', 'fera'), s_pata, 'madeira'),
    (('aprendiz', 'mestre', 'maestria', 'treino', 'nivel', 'evolu'), s_seta_cima, 'ouro'),
    (('artesao',), s_bigorna, 'metal'),
    (('espada', 'lamina', 'corte', 'golpe', 'katana', 'iai', 'adaga', 'cortes', 'juizo', 'decisivo'), s_espada, 'metal'),
]
VIDA = {'mineracao': (s_picareta, 'metal'), 'lenhador': (s_machado, 'madeira'), 'herbalismo': (s_folha, 'verde'),
        'pesca': (s_peixe, 'agua'), 'cozinha': (s_tacho, 'metal'), 'ferraria': (s_bigorna, 'metal'),
        'alquimia': (s_frasco, 'veneno'), 'agricultura': (s_planta, 'verde'), 'domar': (s_pata, 'madeira'),
        'joalharia': (s_gema, 'agua'), 'engenharia': (s_engrenagem, 'metal'), 'costura': (s_agulha, 'osso')}


def icone(nome, familia, passiva=False, forcar=None):
    g = G()
    t = _ascii(nome)
    simb, cor = forcar or next(((s, c) for chaves, s, c in SIMBOLOS if any(k in t for k in chaves)), (s_estrela, 'luz'))
    simb(g)
    escura, clara, fundo = FAMILIAS[familia]
    im = Image.new('RGBA', (24, 24))
    hx = lambda c: tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)
    for y in range(24):
        for x in range(24):
            if (x in (0, 23) and y in (0, 23)):
                continue
            borda = x in (0, 23) or y in (0, 23)
            dentro = x in (1, 22) or y in (1, 22)
            if borda:
                im.putpixel((x, y), hx(OUT))
            elif dentro:
                im.putpixel((x, y), hx(clara if (x + y) < 24 else escura))
            else:
                k = (x + y) / 46
                im.putpixel((x, y), hx(fundo if k > 0.35 else escura if (x + y) % 2 else fundo))
    tons = COR[cor]
    for (x, y) in {(x + a, y + b) for (x, y) in g.p for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))} - set(g.p):
        if 2 <= x <= 21 and 2 <= y <= 21:
            im.putpixel((x, y), hx(OUT))
    for (x, y), tt in g.p.items():
        im.putpixel((x, y), hx(tons[tt]))
    if passiva:
        for (x, y) in ((1, 1), (2, 1), (1, 2), (22, 1), (21, 1), (22, 2), (1, 22), (1, 21), (2, 22), (22, 22), (21, 22), (22, 21)):
            im.putpixel((x, y), hx('#f9c22b'))
    return im


def ler_skills():
    txt = open(DOC, encoding='utf-8').read()
    out = []
    sec2 = txt.split('## 2.')[1].split('\n## ')[0]
    for n in re.findall(r'^\| \*\*(.+?)\*\* \|', sec2, re.M):
        out.append((n, 'unica', False, None))
    for bloco in re.split(r'^### 3\.\d+ ', re.split(r'^## 3\. ', txt, flags=re.M)[1].split('\n## 4')[0], flags=re.M)[1:]:
        classe = bloco.split(' (')[0].strip()
        for nivel, nome, tipo in re.findall(r'^\| (\d+) \| (.+?) \| (ativa|passiva)', bloco, re.M):
            out.append((nome, CLASSE_FAMILIA.get(classe, 'espada'), tipo == 'passiva', None))
    sec4 = txt.split('## 4.')[1].split('\n## 5')[0]
    for linha in re.findall(r'^\| (?!Arma)(.+)$', sec4, re.M):
        for n in re.findall(r'\*\*(.+?)\*\*', linha):
            for parte in n.split(' / '):
                out.append((parte, 'arma', False, None))
    sec5 = txt.split('## 5.')[1].split('\n## 6')[0]
    for n in re.findall(r'^\| (?!Skill)([A-ZÀ-Ú][^|]+?) \|', sec5, re.M):
        chave = _ascii(n).strip()
        if chave in VIDA:
            out.append((n.strip(), 'vida', True, VIDA[chave]))
    return out


def gerar():
    os.makedirs(PASTA, exist_ok=True)
    feitos = set()
    for nome, fam, passiva, forcar in ler_skills():
        sid = _slug(nome)
        if sid in feitos:
            continue
        feitos.add(sid)
        icone(nome, fam, passiva, forcar).save(os.path.join(PASTA, f'{sid}.png'))
    print('ok', len(feitos), 'ícones de skills')
    return sorted(feitos)


if __name__ == '__main__':
    gerar()
