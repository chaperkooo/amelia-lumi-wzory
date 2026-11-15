# Składa stronę z planszy tła i wyciętych postaci. / Composes a page from a background plate and cut-out characters.
import json, sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw
from rembg import remove, new_session
from scipy import ndimage
S = new_session('isnet-anime')

def load(p, crop=6):
    im = Image.open(p).convert('RGB'); w, h = im.size
    return im.crop((crop, crop, w - crop, min(h, w) - crop)).resize((700, 700), Image.LANCZOS)

def cutout(p, key=None, min_px=800, biale=False, usun=(), usun_biale=()):
    im = load(p)
    a = np.array(remove(im, session=S))[..., 3].astype(float) / 255
    rgb = np.array(im).astype(int)
    m = a > 0.5
    if biale:  # na białym tle: wszystko, co nie jest białe, też jest postacią / on white: non-white is character too
        nw = np.abs(rgb - 255).sum(-1) > 100
        m = ndimage.binary_fill_holes(m | nw); a = np.maximum(a, m.astype(float))
    for x0, y0, x1, y1 in usun: m[y0:y1, x0:x1] = False  # usuń resztki klocka / remove block leftovers
    for x0, y0, x1, y1 in usun_biale:  # usuń białą szparę między postaciami / remove white gap between characters
        z = np.zeros(m.shape, bool); z[y0:y1, x0:x1] = True; z &= rgb.min(-1) > 225
        m &= ~z; a = np.where(z, 0, a)
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

def wieczor(img, gwiazdy=14, seed=7):
    # Ta sama plansza wieczorem: niebo -> gradient z gwiazdkami, reszta przyciemniona.
    # Same plate in the evening: sky -> gradient with small stars, the rest darkened.
    a = np.array(img.convert('RGB')).astype(float); h, w, _ = a.shape
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    sky = (b > r + 25) & (b > 150) & (b >= g)
    lab, _ = ndimage.label(sky)
    sky = np.isin(lab, [i for i in np.unique(lab[0]) if i > 0])
    hz = np.where(sky.any(1))[0].max()
    t = np.clip(np.arange(h) / hz, 0, 1)[:, None, None]
    top, mid, low = np.array([28, 36, 92]), np.array([92, 72, 150]), np.array([226, 160, 170])
    grad = np.where(t < 0.6, top + (mid - top) * (t / 0.6), mid + (low - mid) * ((t - 0.6) / 0.4))
    dusk = a * np.array([0.55, 0.58, 0.82]) + np.array([10, 8, 25])
    out = Image.fromarray(np.where(sky[..., None], grad, dusk).clip(0, 255).astype(np.uint8)).convert('RGBA')
    rng = np.random.default_rng(seed); d = ImageDraw.Draw(out)
    for _ in range(gwiazdy):
        x, y, s = rng.integers(20, w - 20), rng.integers(15, int(hz * 0.7)), rng.integers(3, 7)
        pts = [(x + s * (1 if k % 2 == 0 else 0.45) * np.sin(k * np.pi / 5), y - s * (1 if k % 2 == 0 else 0.45) * np.cos(k * np.pi / 5)) for k in range(10)]
        d.polygon(pts, fill=(255, 244, 200, 255))
    return out

def noc(img, okno, gwiazdy=5, seed=3):
    # Ten sam pokój nocą: wszystko przyciemnione na granatowo, w oknie nocne niebo.
    # Same room at night: everything darkened to navy, night sky in the window.
    a = np.array(img.convert('RGB')).astype(float)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    x0, y0, x1, y1 = okno
    glass = np.zeros(r.shape, bool); glass[y0:y1, x0:x1] = True
    glass &= (b > r + 10) & (b > 160)
    dark = a * np.array([0.42, 0.45, 0.72]) + np.array([8, 8, 22])
    out = np.where(glass[..., None], np.array([30, 38, 90]), dark)
    out = Image.fromarray(out.clip(0, 255).astype(np.uint8)).convert('RGBA')
    ys, xs = np.where(glass); rng = np.random.default_rng(seed); d = ImageDraw.Draw(out)
    for i in rng.choice(len(xs), gwiazdy, replace=False):
        x, y, s = xs[i], ys[i], 3
        d.polygon([(x + s * (1 if k % 2 == 0 else 0.45) * np.sin(k * np.pi / 5), y - s * (1 if k % 2 == 0 else 0.45) * np.cos(k * np.pi / 5)) for k in range(10)], fill=(255, 244, 200, 255))
    return out

def blask(base, x, y, r):  # miękka poświata gwiazdki Lumi / soft glow of Lumi's star
    m = Image.new('L', base.size, 0); ImageDraw.Draw(m).ellipse((x - r, y - r, x + r, y + r), fill=120)
    m = m.filter(ImageFilter.GaussianBlur(r / 2))
    glow = Image.new('RGBA', base.size, (255, 250, 220, 0)); glow.putalpha(m)
    base.alpha_composite(glow)

cfg = json.load(open(sys.argv[1]))
page = load(cfg['plansza']).convert('RGBA')
if cfg.get('wieczor'): page = wieczor(page)
if cfg.get('noc'): page = noc(page, cfg['noc'])
ciemno = np.array([0.86, 0.84, 0.95]) if cfg.get('wieczor') else np.array([0.8, 0.8, 0.92]) if cfg.get('noc') else None
for L in cfg['warstwy']:
    c = cutout(L['plik'], L.get('klucz'), biale=L.get('biale', False), usun=L.get('usun', ()), usun_biale=L.get('usun_biale', ()))
    if ciemno is not None:  # postacie lekko przyciemnione wieczorem i nocą / characters slightly dimmed at dusk and night
        arr = np.array(c).astype(float); arr[..., :3] *= ciemno
        c = Image.fromarray(arr.clip(0, 255).astype(np.uint8), 'RGBA')
    if 'wytnij' in L:  # weź tylko część warstwy (np. samą Amelię) / keep only part of the layer
        box = Image.new('L', c.size, 0)
        w0 = L['wytnij']
        if not isinstance(w0[0], list): rects = [w0]  # jeden prostokąt / one rectangle
        elif not isinstance(w0[0][0], list) and len(w0[0]) == 2: rects = [w0]  # jeden wielokąt / one polygon
        else: rects = w0  # lista kształtów / list of shapes
        for r in rects:  # prostokąt [x0,y0,x1,y1] albo wielokąt [[x,y],...] / rectangle or polygon
            if isinstance(r[0], list): ImageDraw.Draw(box).polygon([tuple(p) for p in r], fill=255)
            else: ImageDraw.Draw(box).rectangle(r, fill=255)
        a = np.minimum(np.array(c)[..., 3], np.array(box)); c.putalpha(Image.fromarray(a))
    c = c.resize((int(700 * L['skala']), int(700 * L['skala'])), Image.LANCZOS)
    if 'cien' in L: shadow(page, *L['cien'])
    page.alpha_composite(c, (L['x'], L['y']))
for g in cfg.get('blask', []): blask(page, *g)
page.convert('RGB').save(cfg['wynik'])
print('ok', cfg['wynik'])
