# Warstwy / Layers

Strony w tym samym miejscu mają w 100% to samo tło. / Pages in the same place have a 100% identical background.

- `zrodla/plansza_schody.png` — tło „pod schodami” dla stron 19–24 (Midjourney 44370eb9-9dcb-4097-9df3-b5a49e6f94a6, index 0). / Stairs plate for pages 19–24.
- `zrodla/sNN_*.png` — postacie na gładkim tle (Leo 23: cf59e6e0-b1fd-4066-b060-a64851b090c2/0, Amelia+Lumi 23: 89fd2d35-d256-414b-b2d7-98ddb2550420/2). / Characters on a plain background.
- `sNN.json` — skala i położenie każdej warstwy. / Scale and position of each layer.
- `sklej.py` — wycina postacie (rembg, isnet-anime) i nakłada je na tło: `python3 sklej.py s23.json`. / Cuts out the characters and places them on the plate.

Teraz pliki to podglądy ze zrzutu ekranu (700 px). Przy składaniu do druku podmienimy je na pełną jakość z Midjourney i uruchomimy ten sam skrypt. / These are 700 px screenshot previews; for print we swap in full-quality files and rerun the script.
