# Składa stronę z planszy tła i wyciętych postaci. / Composes a page from a background plate and cut-out characters.
import json, sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw
from rembg import remove, new_session
from scipy import ndimage
S = new_session('isnet-anime')

def load(p, crop=6):
    im = Image.open(p).convert('RGB'); w, h = im.size
    return im.crop((crop, crop, w - crop, min(h, w) - crop)).resize((700, 700), Image.LANCZOS)

def cutout(p, key=None, min_px=800):
    im = load(p)
    a = np.array(remove(im, session=S))[..., 3].astype(float) / 255
    rgb = np.array(im).astype(int)
    m = a > 0.5
    if key:  # usuń kolor tła/klocka / remove background/block colour
        k = np.array(key); m &= np.abs(rgb - k).sum(-1) > 45
    m = ndimage.binary_opening(m, np.ones((5, 5)))
    lab, n = ndimage.label(m)
    sizes = ndimage.sum(m, lab, range(1, n + 1))
    keep = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s >= min_px])
    keep = ndimage.binary_dilation(keep, np.ones((3, 3))) & (a > 0.15)
    alpha = (np.minimum(a, 1) * keep * 255).astype(np.uint8)
    out = im.convert('RGBA'); out.putalpha(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.6)))
    return out

def shadow(base, cx, cy, rx, ry, op=70):
    sh = Image.new('L', base.size, 0); ImageDraw.Draw(sh).ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=op)
    sh = sh.filter(ImageFilter.GaussianBlur(6))
    dark = Image.new('RGBA', base.size, (90, 60, 30, 0)); dark.putalpha(sh)
    base.alpha_composite(dark)

cfg = json.load(open(sys.argv[1]))
page = load(cfg['plansza']).convert('RGBA')
for L in cfg['warstwy']:
    c = cutout(L['plik'], L.get('klucz'))
    if 'wytnij' in L:  # weź tylko część warstwy (np. samą Amelię) / keep only part of the layer
        box = Image.new('L', c.size, 0); ImageDraw.Draw(box).rectangle(L['wytnij'], fill=255)
        a = np.minimum(np.array(c)[..., 3], np.array(box)); c.putalpha(Image.fromarray(a))
    c = c.resize((int(700 * L['skala']), int(700 * L['skala'])), Image.LANCZOS)
    if 'cien' in L: shadow(page, *L['cien'])
    page.alpha_composite(c, (L['x'], L['y']))
page.convert('RGB').save(cfg['wynik'])
print('ok', cfg['wynik'])
