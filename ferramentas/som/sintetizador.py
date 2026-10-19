"""Sintetizador chiptune simples (numpy): ondas, envelopes, deslizes de tom, filtros e eco. Grava .ogg (ffmpeg).

Usado por efeitos.py (efeitos sonoros) e musica.py (músicas). Estilo do docs/AUDIO.md: chiptune com
instrumentos "reais" por cima (flauta, cordas, piano imitados com ondas suaves).
"""
import os
import subprocess
import tempfile
import wave

import numpy as np

SR = 22050   # amostras por segundo (chega para chiptune e poupa espaço)


def t_de(dur):
    return np.arange(int(SR * dur)) / SR


def nota_hz(n):
    """n: número MIDI (60 = Dó central)."""
    return 440.0 * 2 ** ((n - 69) / 12)


def onda(tipo, freq, dur, duty=0.5, fase=0.0, semente=1):
    """freq: número ou array (Hz por amostra)."""
    n = int(SR * dur)
    if n <= 0:
        return np.zeros(0)
    f = np.full(n, float(freq)) if np.isscalar(freq) else np.asarray(freq, dtype=float)[:n]
    ph = (np.cumsum(f) / SR + fase) % 1.0
    if tipo == 'quadrada':
        return np.where(ph < duty, 1.0, -1.0)
    if tipo == 'triangulo':
        return 4 * np.abs(ph - 0.5) - 1
    if tipo == 'triangulo_nes':   # triângulo em degraus (como o NES)
        return np.round((4 * np.abs(ph - 0.5) - 1) * 7.5) / 7.5
    if tipo == 'serra':
        return 2 * ph - 1
    if tipo == 'seno':
        return np.sin(2 * np.pi * ph)
    if tipo == 'ruido':
        rnd = np.random.default_rng(semente)
        # ruído "segurado" ao ritmo da frequência (mais grave = mais áspero)
        passo = np.maximum(1.0, SR / np.maximum(f, 1))
        k = np.floor(np.cumsum(1.0 / passo)).astype(int)   # muda de valor ao ritmo da frequência
        v = rnd.uniform(-1, 1, k[-1] + 2)
        idx = k
        return v[idx]
    raise ValueError(tipo)


def env(n, a=0.005, d=0.05, s=0.6, r=0.08, dur=None):
    """Envelope ADSR com n amostras; dur = tempo até largar a nota (por omissão: n − r)."""
    t = np.arange(n) / SR
    total = n / SR
    solta = (total - r) if dur is None else min(dur, total)
    e = np.where(t < a, t / max(a, 1e-6), np.where(t < a + d, 1 - (1 - s) * (t - a) / max(d, 1e-6), s))
    e = np.where(t >= solta, e * np.maximum(0.0, 1 - (t - solta) / max(r, 1e-6)), e)
    return e


def env_rapido(n, a=0.003, queda=8.0):
    """Ataque curto e queda exponencial (percussão, pings)."""
    t = np.arange(n) / SR
    e = np.exp(-t * queda)
    k = int(SR * a)
    if k > 0:
        e[:k] *= np.linspace(0, 1, k)
    return e


def deslize(f0, f1, dur, curva=1.0):
    n = int(SR * dur)
    u = np.linspace(0, 1, n) ** curva
    return f0 * (f1 / f0) ** u if f0 > 0 and f1 > 0 else f0 + (f1 - f0) * u


def vibrato(freq, dur, prof=0.006, vel=5.5, atraso=0.15):
    t = t_de(dur)
    k = np.clip((t - atraso) / 0.2, 0, 1)
    return freq * (1 + prof * k * np.sin(2 * np.pi * vel * t))


def passa_baixo(x, corte):
    """Filtro de 1 polo (corte em Hz; pode ser array)."""
    c = np.asarray(corte, dtype=float)
    a = 1 - np.exp(-2 * np.pi * (c if c.ndim else np.full(len(x), c)) / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def passa_alto(x, corte):
    return x - passa_baixo(x, corte)


def eco(x, atraso=0.18, ganho=0.35, vezes=3):
    k = int(SR * atraso)
    y = np.concatenate([x, np.zeros(k * vezes)])
    for i in range(1, vezes + 1):
        y[i * k: i * k + len(x)] += x * (ganho ** i)
    return y


def misturar(*partes):
    n = max(len(p) for p in partes)
    y = np.zeros(n)
    for p in partes:
        y[:len(p)] += p
    return y


def colocar(buf, som, inicio):
    i = int(inicio * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(som))
    buf[i:j] += som[:j - i]


def normalizar(x, pico=0.9):
    m = np.max(np.abs(x)) if len(x) else 0
    return x * (pico / m) if m > 1e-9 else x


def gravar_ogg(x, caminho, qualidade=3, ciclo=False):
    """Grava em .ogg (Vorbis, mono). qualidade 0–10 (3 ≈ 80 kbps a 22 kHz, chega e sobra)."""
    os.makedirs(os.path.dirname(caminho) or '.', exist_ok=True)
    x = np.clip(x, -1, 1)
    if not ciclo:   # tira o clique no fim
        k = min(len(x), int(SR * 0.004))
        if k:
            x[-k:] *= np.linspace(1, 0, k)
    pcm = (x * 32767).astype('<i2').tobytes()
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        nome = tmp.name
    with wave.open(nome, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', nome, '-c:a', 'libvorbis', '-q:a', str(qualidade), caminho],
                   check=True)
    os.remove(nome)
