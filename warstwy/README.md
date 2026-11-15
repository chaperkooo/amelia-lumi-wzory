# Warstwy / Layers

Strony w tym samym miejscu mają w 100% to samo tło. / Pages in the same place have a 100% identical background.

- `zrodla/plansza_schody.png` — tło „pod schodami” dla stron 19–24 (Midjourney 44370eb9-9dcb-4097-9df3-b5a49e6f94a6, index 0). / Stairs plate for pages 19–24.
- `zrodla/sNN_*.png` — postacie na gładkim tle (Leo 23: cf59e6e0-b1fd-4066-b060-a64851b090c2/0, Amelia+Lumi 23: 89fd2d35-d256-414b-b2d7-98ddb2550420/2). / Characters on a plain background.
- `sNN.json` — skala i położenie każdej warstwy. / Scale and position of each layer.
- `zrodla/plansza_ogrod.png` — ogród ze strony 3 bez postaci (649eacce-628e-4193-8f2d-026f76e316d4/0): strony 29, 30 i okładka. / Garden plate from page 3.
- `zrodla/plansza_sypialnia.png` — pokój ze strony 7 bez postaci (aa753681-839b-47b6-9d96-c472043cb4a9/0): strona 27. / Bedroom plate from page 7.
- `"wieczor": true` i `"noc": [okno]` w JSON zmieniają porę dnia skryptem, więc tło zostaje to samo. / Dusk and night are made by the script, so the plate stays the same.
- `sklej.py` — wycina postacie (rembg, isnet-anime) i nakłada je na tło: `python3 sklej.py s23.json`. / Cuts out the characters and places them on the plate.

Teraz pliki to podglądy ze zrzutu ekranu (700 px). Przy składaniu do druku podmienimy je na pełną jakość z Midjourney i uruchomimy ten sam skrypt. / These are 700 px screenshot previews; for print we swap in full-quality files and rerun the script.
