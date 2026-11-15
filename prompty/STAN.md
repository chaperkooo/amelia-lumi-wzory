# STAN PRAC — czytaj najpierw / WORK STATUS — read first
Ostatnia aktualizacja / last update: 15.11.2026, 19:05

## Gdzie jesteśmy / Where we are
- Wszystkie strony z ilustracjami 3–30 i przód okładki mają ilustracje. / All illustrated pages 3–30 and the front cover have pictures.
- Zaakceptowane / approved: 3–30 i przód okładki (stara wersja strony 8 też). / 3–30 and the front cover.
- CZEKAJĄ na ocenę (15.11) / WAITING for review: nowe wersje stron 8 i 26 z miejscem na tekst (granatowa podłoga u góry ~1/3). Pierwsza rzecz w nowym wątku: zapytać o akceptację. / New versions of pages 8 and 26 with text space — ask for approval first.
- Zasada: to samo miejsce = w 100% to samo tło (metoda WARSTW i twarze.py). / Rule: same place = 100% identical background.

## Lista stron / Page list (szczegóły: `strony/GOTOWE.md`)
| Strona | Jak powstała / How made | Źródło w MJ / MJ source |
|---|---|---|
| 3–7 | zwykłe obrazki / plain images | 3 = 4a1312f2/1, 7 = 2d8601d8/3 (reszta w Organize) |
| 8 | NOWA (czeka): pomniejszona w edytorze / NEW (waiting) | 264cb94e-df21-420b-958a-6038f8dfe847/1 (stara: 61abad49/0) |
| 9–18 | zwykłe obrazki | GOTOWE.md |
| 19–24 | warstwy na planszy schodów | 44370eb9/0 + postacie (warstwy/s19–s24.json) |
| 25 | zwykły obrazek | 6c2cf30e/2 |
| 26 | NOWA (czeka): nowa strona 8 + twarze (`warstwy/twarze.py s26.json`) | 264cb94e/1 + 61abad49/0 + c3cb5766/0 |
| 27 | warstwy, pokój ze strony 7 nocą | aa753681/0 + 47839ddb/1 |
| 28 | warstwy, podwórko ze strony 17 | b4633e1c/0 + postacie (s28.json) |
| 29 | warstwy, ogród ze strony 3 | 649eacce/0 + c935a72c/0 |
| 30 | warstwy, ten sam ogród wieczorem | 649eacce/0 + 8ec79ce1/2 + fe3196a4/0 |
| okładka (przód) | warstwy, ogród ze strony 3 | 649eacce/0 + 0a8fefbd/0 |

Folder MJ „KSIAZKA strony gotowe”: zaakceptowane strony + źródła warstw (plansze i postacie). Po akceptacji nowej strony 8 dodać tam 264cb94e/1. Stare strony 19–21 (stare schody) trzeba stamtąd usunąć. / MJ folder holds approved pages and layer sources.

## Plansze (tła) / Plates
| Miejsce / Place | Plik | Job MJ | Strony / Pages |
|---|---|---|---|
| schody / stairs | `warstwy/zrodla/plansza_schody.png` | 44370eb9-9dcb-4097-9df3-b5a49e6f94a6/0 | 19–24 |
| podwórko / playground | `warstwy/zrodla/plansza_podworko.png` | b4633e1c-3a6b-4568-95ed-bb836275d3cf/0 | 28 (17) |
| ogród ze strony 3 / garden | `warstwy/zrodla/plansza_ogrod.png` | 649eacce-628e-4193-8f2d-026f76e316d4/0 | 29, 30 (wieczór), okładka |
| sypialnia ze strony 7 / bedroom | `warstwy/zrodla/plansza_sypialnia.png` | aa753681-839b-47b6-9d96-c472043cb4a9/0 | 27 (noc) |
| łóżko ze strony 8 / bed | `warstwy/zrodla/plansza_lozko.png` | 264cb94e-df21-420b-958a-6038f8dfe847/1 | 8, 26 |

## Skrypty / Scripts (w folderze `warstwy/`)
- `pip install --break-system-packages "rembg[cpu]" scipy`
- `python3 sklej.py sNN.json` — postacie na planszy. Klucze: `skala`, `x`, `y`, `cien`, `biale`, `wytnij` (prostokąt albo wielokąt), `usun_biale`, `wieczor`, `noc`, `blask`.
- `python3 twarze.py s26.json` — nowe twarze na planszy innej strony; sam dopasowuje skalę i położenie.
- Teraz pliki to podglądy ze zrzutów (700 px). Do druku: podmienić na pełną jakość z MJ i uruchomić skrypty jeszcze raz. / Previews from screenshots; rerun with full-quality files for print.

## Jak robić warstwy w Midjourney / How to make layers in MJ
- Postać na „plain flat solid white background, nothing else in the picture” (+ --no grass, ground, floor, shadow, wall, chair).
- Biblioteka (panel 248,41): rząd 1 y≈226: x 1148 = amelia_08_spokoj; rząd 2 y≈322: 957 leo_01, 1050 amelia_01_WZOR, 1148 lumi_01_WZOR. Kłódka zostawia załączniki po wysłaniu.
- Zrzut: job → najedź na (1100,690) → zoom [402,105,962,667] (okno 703 wys.) albo [430,106,934,610] (okno 647 wys.) z save_to_disk.
- Dodawanie do folderu: na stronie joba przycisk „Add to folder” → „KSIAZKA strony gotowe” (działa też przez JavaScript).
- Długi prompt: „type” zgłasza timeout, ale się wpisuje — odczekaj 30 s i sprawdź zrzutem.

## Następne kroki / Next steps
1. Akceptacja nowych stron 8 i 26 → dodać 264cb94e/1 do folderu MJ, status w GOTOWE.md. / Approve new 8 and 26.
2. Strony 1–2: tytułowa (tytuł i autor do ustalenia) i prawa autorskie / dedykacja. / Pages 1–2.
3. Strona 31 (dla dorosłych, sam tekst) i 32 (pięć obrazków Lumi z emocjami — wzory lumi_01, lumi_02, lumi_03). / Pages 31–32.
4. Pełna okładka: przód + grzbiet + tył. Wymiary, spad (bleed) i grzbiet sprawdzić na stronie KDP. / Full cover; check KDP specs online.
5. Składanie PDF wnętrza (PL i EN osobno), tekst z `tekst/tekst_PL.md` i `tekst/tekst_EN.md`. / Build interior PDFs.
6. Druk: pobrać folder „KSIAZKA strony gotowe” w pełnej jakości (robi użytkownik) i złożyć strony z warstw jeszcze raz. / Download full quality and rebuild layered pages.
7. Potem: tytuł, opis, słowa kluczowe i kategorie na KDP; kolorowanki. / Then: KDP listing, colouring books.
