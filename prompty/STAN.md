# STAN PRAC — czytaj najpierw / WORK STATUS — read first
Ostatnia aktualizacja / last update: 13.11.2026, 11:50

## Gdzie jesteśmy / Where we are
- Strony 3–21 zaakceptowane (folder MJ „KSIAZKA strony gotowe”). Strony 22–25: kandydaci, NIE akceptowane. / Pages 3–21 approved; 22–25 candidates only.
- NOWA ZASADA użytkownika: strony w tym samym miejscu (schody: 19–24) mają w 100% identyczne tło. Metoda WARSTW zaakceptowana (11:42). / NEW RULE: same place = 100% identical background. LAYER method approved.
- Uwagi użytkownika do próbki strony 23: postacie za małe względem schodów (POPRAWIONE: Leo skala 0.68, Amelia 0.6), dziwna mina Lumi (W TRAKCIE: nowa warstwa Lumi). Skóry/włosów Amelii i spojrzenia Leo NIE kazał poprawiać. / Feedback: characters too small (fixed), Lumi's face odd (in progress).

## Pliki / Files
- `warstwy/sklej.py` + `warstwy/sNN.json` → `python3 sklej.py sNN.json` (rembg isnet-anime: `pip install --break-system-packages "rembg[cpu]"`; uruchamiać w folderze `warstwy/`).
- `warstwy/zrodla/plansza_schody.png` = tło schodów (MJ 44370eb9-9dcb-4097-9df3-b5a49e6f94a6/0).
- Strona 23: Leo cf59e6e0-b1fd-4066-b060-a64851b090c2/0 (różowy klocek, klucz [242,216,214]); Amelia+Lumi 89fd2d35-d256-414b-b2d7-98ddb2550420/2 (bierzemy samą Amelię: „wytnij” [90,80,428,660]); nowy Lumi: najnowszy job w Create („the same creature, now floating… peeking”), wersja 3.
- Pole „wytnij” w JSON = prostokąt w warstwie 700×700, który zostaje. / "wytnij" = box kept from the 700×700 layer.

## Jak robić warstwy w Midjourney / How to make layers in MJ
- Postać na „plain flat solid white background, nothing else in the picture” (+ --no stairs, wall, floor, furniture, shadow). Leo siedzący: „sitting on a low plain light pink block the same color as the background” na różowym tle → klocek usuwa klucz koloru.
- Zrzut warstwy: otwórz job, najedź myszą na (1100,690), zoom regionu [402,105,962,667] z save_to_disk, skala 1 → plik 700×703 w /tmp/claude-tool-results/… (skopiuj do warstwy/zrodla).
- Biblioteka (panel 248,43), rząd y=322: 478 amelia_03_a, 956 leo_01, 1052 amelia_01_WZOR, 1147 lumi_01_WZOR. Długi tekst: „type” może zgłosić timeout, ale się wpisuje — odczekaj 50 s i sprawdź zoomem.
- Przeglądarka czasem zwraca „Couldn't determine which page” — odczekaj 20 s, tabs_context, ponów.

## Następne kroki / Next steps
1. Zrzucić Lumi (wersja 3), dodać warstwę do s23.json obok ramienia Amelii, pokazać stronę 23. / Capture Lumi v3, add to s23.json, show page 23.
2. Po akceptacji: warstwy dla stron 22 i 24 (Leo + Amelia + Lumi) oraz 19, 20, 21 (Amelia + Lumi) na tym samym tle. Tekst stron: tekst/ksiazka_pl_en.md.
3. Potem strony 25–30 i okładka (25: klasa ze strony 16 — to też to samo miejsce!).
4. Druk: podmienić zrzuty na pełną jakość z MJ (pobiera użytkownik) i uruchomić sklej.py ponownie.
