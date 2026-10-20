"""Retratos para quem fala nas cenas mas não tem ficha de NPC.
- Os de cara humana (o Administrador, o Serafim, o Rei Sem Coroa...) desenham-se como os outros retratos
  (retratos.py), com o estilo em dados/retratos.json ("humanos").
- Os bichos e as coisas (o Dragão, o Ent, o Guardião do Tempo...) usam o busto do próprio boneco (1.º frame de
  "parado" de lado), ampliado só por números inteiros (pixel art certa), num medalhão escuro.
Os nomes das cenas que usam estes retratos estão em dados/retratos.json.
Saída: arte/retratos/{id}_{normal,feliz,zangado,triste}.png (64×64; a mesma cara nas 4 emoções)

Uso: python3 ferramentas/arte/retratos_bonecos.py
"""
import json
import os

from PIL import Image

W = 64
FUNDO = (0x2e, 0x22, 0x2f, 255)
EMOCOES = ['normal', 'feliz', 'zangado', 'triste']


def busto(caminho, recorte=None):
    folha = Image.open(caminho).convert('RGBA')
    h = folha.height
    f = folha.crop((0, 0, h, h))
    x0, y0, x1, y1 = f.getbbox()
    if recorte:                       # [x, y, lado] à mão (frações do boneco), para os que não são de pé
        rx, ry, rl = recorte
        lado = min(W - 6, int(rl * h))   # boneco grande: só a cara, sem reduzir
        cx, cy = int(rx * h), int(ry * h)
    else:                             # de pé: a cabeça e os ombros (o cimo do boneco)
        lado = max(8, min(x1 - x0, int((y1 - y0) * 0.5)))
        cy = y0 + lado // 2 - 1
        topo = f.crop((x0, y0, x1, y0 + lado))
        tx0, _, tx1, _ = topo.getbbox()
        cx = x0 + (tx0 + tx1) // 2
    b = f.crop((cx - lado // 2, cy - lado // 2, cx - lado // 2 + lado, cy - lado // 2 + lado))
    k = max(1, (W - 6) // lado)
    b = b.resize((b.width * k, b.height * k), Image.NEAREST)
    out = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    for y in range(W):                # fundo redondo (como uma moldura de medalhão)
        for x in range(W):
            if (x - 31.5) ** 2 + (y - 31.5) ** 2 < 31 ** 2:
                out.putpixel((x, y), FUNDO)
    out.alpha_composite(b, ((W - b.width) // 2, (W - b.height) // 2 if recorte else W - b.height))
    # o busto não passa do círculo
    for y in range(W):
        for x in range(W):
            if (x - 31.5) ** 2 + (y - 31.5) ** 2 >= 31 ** 2 and y < W - 12:
                out.putpixel((x, y), (0, 0, 0, 0))
    return out


if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import retratos
    d = json.load(open(os.path.join('dados', 'retratos.json')))
    for rid, est in d['humanos'].items():
        est = dict(est)
        est['acessorios'] = [a if isinstance(a, str) else tuple(a) for a in est.get('acessorios', [])]
        for em in EMOCOES:
            retratos.retrato(est, em).save(os.path.join('arte', 'retratos', f'{rid}_{em}.png'))
    for rid, info in d['bonecos'].items():
        img = busto(info['sprite'], info.get('recorte'))
        for em in EMOCOES:
            img.save(os.path.join('arte', 'retratos', f'{rid}_{em}.png'))
    print('ok', len(d['humanos']), 'retratos desenhados +', len(d['bonecos']), 'de bonecos')
