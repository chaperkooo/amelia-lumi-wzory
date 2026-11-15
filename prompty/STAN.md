# STAN PRAC — czytaj najpierw / WORK STATUS — read first
Ostatnia aktualizacja / last update: 15.11.2026, 19:15

## Gdzie jesteśmy / Where we are
- Strony 3–25 i 28 zaakceptowane (folder MJ „KSIAZKA strony gotowe”). / Pages 3–25 and 28 approved.
- 15.11: ZAAKCEPTOWANE strony 26, 27, 29, 30 i przód okładki. Dodane do folderu MJ „KSIAZKA strony gotowe”: c3cb5766/0, aa753681/0, 47839ddb/1, 649eacce/0, c935a72c/0, 8ec79ce1/2, fe3196a4/0, 0a8fefbd/0. Zbiorczy podgląd: `warstwy/strony_26-30_okladka.jpg`. / Pages 26, 27, 29, 30 and front cover approved and added to the MJ folder (plates and characters too).
- Wszystkie strony z ilustracjami 3–30 są zaakceptowane. / All illustrated pages 3–30 are approved.
- Zasada: to samo miejsce = w 100% to samo tło (metoda WARSTW). / Rule: same place = 100% identical background (LAYER method).

## Plansze (tła) / Plates
| Miejsce / Place | Plik | Job MJ | Strony / Pages |
|---|---|---|---|
| schody / stairs | `warstwy/zrodla/plansza_schody.png` | 44370eb9-9dcb-4097-9df3-b5a49e6f94a6/0 | 19–24 |
| podwórko / playground | `warstwy/zrodla/plansza_podworko.png` | b4633e1c-3a6b-4568-95ed-bb836275d3cf/0 | 28 (17) |
| ogród ze strony 3 / garden | `warstwy/zrodla/plansza_ogrod.png` | 649eacce-628e-4193-8f2d-026f76e316d4/0 | 29, 30 (wieczór), okładka |
| sypialnia ze strony 7 / bedroom | `warstwy/zrodla/plansza_sypialnia.png` | aa753681-839b-47b6-9d96-c472043cb4a9/0 | 27 (noc) |
| łóżko ze strony 8 / bed | (bez planszy — edycja strony 8) | 61abad49-3a5a-4e8e-9138-459f490f01e4/0 | 26 = c3cb5766-2ded-48fe-be21-508b060ad7cf/0 |

## Pliki / Files
- `warstwy/sklej.py` + `warstwy/sNN.json` → `cd warstwy && python3 sklej.py sNN.json` (`pip install --break-system-packages "rembg[cpu]" scipy`).
- Nowe w JSON / new keys: `"wieczor": true` (zmierzch, gwiazdki), `"noc": [okno x0,y0,x1,y1]` (noc w pokoju), `"blask": [[x,y,r]]` (poświata gwiazdki), `"wytnij"` może być wielokątem `[[x,y],...]`, `"usun_biale": [[x0,y0,x1,y1]]` (biała szpara między postaciami).

## Jak robić warstwy w Midjourney / How to make layers in MJ
- Postać na „plain flat solid white background, nothing else in the picture” (+ --no grass, ground, floor, shadow, wall, chair). Leo siedzący na ziemi: tylko „sitting cross-legged”, bez klocka.
- Biblioteka (panel 248,41): rząd 1 y≈226: x 1148 = amelia_08_spokoj; rząd 2 y≈322: 957 leo_01, 1050 amelia_01_WZOR, 1148 lumi_01_WZOR. Kłódka zostawia załączniki po wysłaniu.
- Zrzut warstwy: job → najedź na (1100,630) → zoom [402,105,962,667] (okno 703 wys.) albo [430,106,934,610] (okno 647 wys.) z save_to_disk.
- Długi prompt: „type” zgłasza timeout, ale się wpisuje — odczekaj 30 s i sprawdź zrzutem.

## Następne kroki / Next steps
1. (zrobione 15.11) akceptacja 26–30 i okładki. / done.
2. Pytanie do użytkownika: strona 8 i 26 mają mało miejsca na tekst (wąski granatowy pas). Czy zmniejszyć obie w edytorze (Scale ~72%), żeby było więcej granatu u góry? Obie zostaną identyczne.
3. Porządki w MJ: z folderu „KSIAZKA strony gotowe” usunąć stare strony 19–21 (stare schody).
4. Potem: strony 1–2 (tytułowa, prawa autorskie), 32 (Lumi — emocje), cała okładka (przód + grzbiet + tył, wymiary z KDP), składanie PDF.
5. Druk: podmienić zrzuty na pełną jakość z MJ (pobiera użytkownik) i uruchomić sklej.py ponownie.
