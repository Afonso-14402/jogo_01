"""Ajuda a ler as tabelas Markdown dos documentos (docs/) para passar o conteúdo para JSON (dados/)."""
import re
import unicodedata


def ascii_(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')


def slug(t):
    return re.sub(r'[^a-z0-9]+', '_', ascii_(t)).strip('_')


def limpar(t):
    return re.sub(r'\*\*|`', '', t).strip()


def numero(t, padrao=0.0):
    """'1,8 m' -> 1.8 · '5%' -> 0.05 · '12 mág.' -> 12.0"""
    t = limpar(t).replace(' ', ' ')
    m = re.search(r'-?\d+(?:[.,]\d+)?', t.replace(' ', '') if re.match(r'^[\d ]+$', t) else t)
    if not m:
        return padrao
    v = float(m.group(0).replace(',', '.'))
    return v / 100.0 if '%' in t else v


def tabelas(texto):
    """Devolve [(titulo_da_seccao, [ {coluna: valor} ])] de todas as tabelas do texto."""
    out, titulo, cab, linhas = [], '', None, []
    for l in texto.split('\n'):
        if l.startswith('#'):
            titulo = l.lstrip('#').strip()
        if l.startswith('|'):
            cel = [c.strip() for c in l.strip().strip('|').split('|')]
            if cab is None:
                cab = [limpar(c) for c in cel]
            elif set(''.join(cel)) <= set('-: '):
                continue
            else:
                linhas.append(dict(zip(cab, cel)))
        elif cab is not None:
            out.append((titulo, linhas))
            cab, linhas = None, []
    if cab is not None:
        out.append((titulo, linhas))
    return out


def seccao(texto, inicio, fim=None):
    """O texto entre o título que começa por `inicio` e o seguinte do mesmo nível (ou `fim`)."""
    i = texto.find(inicio)
    if i < 0:
        return ''
    nivel = len(inicio) - len(inicio.lstrip('#'))
    resto = texto[i + len(inicio):]
    if fim:
        j = resto.find(fim)
        return resto[:j] if j >= 0 else resto
    m = re.search(r'^#{1,%d} ' % nivel, resto, re.M)
    return resto[:m.start()] if m else resto
