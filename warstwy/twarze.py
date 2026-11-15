# Strona z nowymi twarzami na planszy innej strony. / A page with new faces on another page's plate.
# Przykład: strona 26 = pomniejszona strona 8 (nowa plansza) + twarze ze strony 26.
# Example: page 26 = shrunken page 8 (new plate) + faces from page 26.
# Użycie / usage: python3 twarze.py s26.json
import json, sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw

def load(p, crop=6):
    im = Image.open(p).convert('RGB'); w, h = im.size
    return im.crop((crop, crop, w - crop, min(h, w) - crop)).resize((700, 700), Image.LANCZOS)

def dopasuj(plate, orig, s0, box):
    # Szuka skali i położenia oryginału w planszy. / Finds the scale and position of the original in the plate.
    P = np.array(plate.convert('L')).astype(float)
    best = None
    for s in np.arange(s0 - 0.02, s0 + 0.0201, 0.002):
        n = int(round(700 * s))
        O = np.array(orig.convert('L').resize((n, n), Image.LANCZOS)).astype(float)
        x0, y0, x1, y1 = [int(v * s) for v in box]
        patch = O[y0:y1, x0:x1]
        ex, ey = (700 - n) // 2, 700 - n
        for dx in range(ex - 12, ex + 13):
            for dy in range(ey - 12, ey + 13):
                if dy + y1 > 700 or dx + x1 > 700 or dy + y0 < 0 or dx + x0 < 0: continue
                d = np.abs(P[dy + y0:dy + y1, dx + x0:dx + x1] - patch).mean()
                if best is None or d < best[0]: best = (d, round(float(s), 3), dx, dy)
    return best

cfg = json.load(open(sys.argv[1]))
plate = load(cfg['plansza']); orig = load(cfg['oryginal']); faces = load(cfg['twarze'])
if 'dopasowanie' in cfg:
    s, dx, dy = cfg['dopasowanie']
else:
    d, s, dx, dy = dopasuj(plate, orig, cfg.get('skala', 0.72), cfg.get('porownaj', [100, 150, 600, 650]))
    print('dopasowanie / match:', s, dx, dy, 'błąd / error %.2f' % d)
n = int(round(700 * s))
F = faces.resize((n, n), Image.LANCZOS)
m = Image.new('L', (700, 700), 0)
ImageDraw.Draw(m).rectangle(cfg['obszar'], fill=255)  # obszar twarzy w oryginale / face area in the original
m = m.filter(ImageFilter.GaussianBlur(cfg.get('miekkosc', 10))).resize((n, n), Image.LANCZOS)
out = plate.copy(); out.paste(F, (dx, dy), m)
out.save(cfg['wynik'])
print('ok', cfg['wynik'])
