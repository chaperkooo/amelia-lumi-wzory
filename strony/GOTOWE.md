# Strony książki / Book pages
Lista stron: kandydaci (status „czeka”) i strony zaakceptowane (status „zaakceptowana”).
List of pages: candidates (status "czeka" = waiting) and approved pages (status "zaakceptowana" = approved).
## Gdzie są pliki / Where the files are
- **Pełna jakość (do druku)** / **Full quality (for print):** Midjourney → Organize → Folders → **„KSIAZKA strony gotowe”**.
  Każdy obrazek ma swój numer zadania (job ID) i numer wersji (index) w tabeli niżej.
  Each image has its job ID and version number (index) in the table below.
  Link do obrazka / Image link: `https://www.midjourney.com/jobs/<job ID>?index=<index>`
- **Podgląd (mała jakość)** / **Preview (low quality):** folder `strony/gotowe/` w tym repozytorium.
  Podglądy służą tylko do sprawdzania, NIE do druku. / Previews are only for checking, NOT for print.
> Dlaczego pełnej jakości nie ma na GitHubie? / Why is full quality not on GitHub?
> Serwer Claude nie ma dostępu do plików Midjourney (cdn.midjourney.com jest zablokowany).
> Na końcu, przy składaniu książki, pobierzemy cały folder „KSIAZKA strony gotowe” z Midjourney naraz.
> Claude's server can't reach Midjourney files (cdn.midjourney.com is blocked).
> At the end, when building the book, we download the whole "KSIAZKA strony gotowe" folder from Midjourney at once.
## Lista / List
| Strona / Page | Co jest na obrazku / Scene | Job ID | Index | Podgląd / Preview | Status | Uwagi / Notes |
|---|---|---|---|---|---|---|
| 3–8 | (zrobione wcześniej przez użytkownika / made earlier by the user) | — | — | `strony/podglad/strona_03..08_podglad.png` | zaakceptowana | strona 8 = 61abad49-3a5a-4e8e-9138-459f490f01e4/0 (szukaj „pajamas” w Organize); 3–7: szukaj w Organize („blocks” = strona 7, 29.09) / page 8 found; 3–7 search in Organize |
| 9 | Urodziny, Amelia zatyka uszy, pęka balon, kolczasty Lumi / Party, Amelia covers ears, balloon pops, spiky Lumi | 28b911b5-4685-43b0-9b98-815d7156a48a | 0 | `strony/gotowe/strona_09_podglad.png` | zaakceptowana (12.11) | miejsce na tekst u góry ~1/4 / text space at top ~1/4 |
| 10 | Dzieci i mama wołają do zabawy, Amelia zatyka uszy, kolczasty Lumi / Kids and mum call her to play | 603c11f4-577c-4ee0-a512-cdbbf69f8655 | 0 | `strony/gotowe/strona_10_podglad.png` | zaakceptowana (12.11) | dużo miejsca na tekst u góry / lots of text space at top |
| 11 | Kuchnia, zła Amelia tupie, sweter na podłodze, babcia, kolczasty Lumi / Kitchen, angry Amelia stomps | 98320287-ce28-461e-bd0f-34014ee9d1e7 | 1 | `strony/gotowe/strona_11_podglad.png` | zaakceptowana (12.11) | wzór amelia_02_zlosc; miejsce na tekst u góry / text space at top |
| 12 | Okno, deszcz, Amelia płacze, tata klęczy, smutny Lumi / Window, rain, Amelia cries, dad kneels | 5c51fe72-f6e0-4c59-a11e-acdb16d6decd | 1 | `strony/gotowe/strona_12_podglad.png` | zaakceptowana (12.11) | wzór amelia_06_placz_stojac; miejsce u góry / space at top |
| 13 | Kocyk na kanapie jak namiot, Amelia spokojna, Lumi świeci / Blanket tent on sofa, calm | 980e6b1a-c5dd-41c4-b972-1a4c0677e52c | 0 | `strony/gotowe/strona_13_podglad.png` | zaakceptowana (12.11) | dużo miejsca u góry / lots of space at top |
| 14 | Przed szkołą, Amelia niepewna, Lumi wygląda zza ramienia / In front of school, unsure | 40a3b417-5055-4ad7-afef-1db0f47a8fa7 | 0 | `strony/gotowe/strona_14_podglad.png` | zaakceptowana (12.11) | wzór amelia_03_zagubiona; niebo na tekst / sky for text |
| 15 | Hałaśliwy korytarz, dzwonek, dzieci biegną, Amelia zatyka uszy, kolczasty Lumi / Noisy hallway | 72abaa37-7648-4b52-bd94-1b7e57df71ef | 0 | `strony/gotowe/strona_15_podglad.png` | zaakceptowana (13.11) | wzór amelia_04_halas; miejsce u góry / space at top |
| 16 | Klasa widziana od przodu, wszyscy przodem, Amelia zmęczona, Lumi na ławce / Classroom from the front | d56fb3e3-5102-42a3-8a70-ac0041318324 | 2 | `strony/gotowe/strona_16_podglad.png` | zaakceptowana (13.11) | 3. próba wg rygoru twarzy; tekst na żółtej ścianie u góry |
| 17 | Boisko, Amelia sama z kredą i gwiazdkami, troje dzieci biegnie dalej / Playground, alone with chalk | b3374f9c-ef50-430d-8b74-dcdf6150fd4c | 2 | `strony/gotowe/strona_17_podglad.png` | zaakceptowana (13.11) | baza 0232bca0-…(1); niebo na tekst; twarze dzieci w tle małe, ale kompletne |
| 18 | Pusty korytarz, Amelia idzie ze spuszczoną głową, gwiazdka Lumi zgasła / Empty corridor, head down | ab2bf318-2e5e-4ebb-9962-19fae84ce91e | 0 | `strony/gotowe/strona_18_podglad.png` | zaakceptowana (13.11) | baza 409949a8-…(1); twarz większa, Lumi ma oczy i usta |
| 19 | Pod schodami, Amelia skulona płacze, Lumi zwinięty / Under the stairs, crying | WARSTWY: tło 44370eb9-9dcb-4097-9df3-b5a49e6f94a6 + postacie (warstwy/s19.json) | — | `warstwy/strona_19_warstwy.png` | zaakceptowana (13.11, warstwy) | to samo tło schodów co 19–24 / same stairs background |
| 20 | Pod schodami, Amelia smutna, gwiazdka Lumi prawie zgasła / Sad, star almost out | WARSTWY: tło 44370eb9-9dcb-4097-9df3-b5a49e6f94a6 + postacie (warstwy/s20.json) | — | `warstwy/strona_20_warstwy.png` | zaakceptowana (13.11, warstwy) | to samo tło schodów co 19–24 / same stairs background |
| 21 | Deszcz, Amelia sama pod schodami, cisza / Rain, quiet | WARSTWY: tło 44370eb9-9dcb-4097-9df3-b5a49e6f94a6 + postacie (warstwy/s21.json) | — | `warstwy/strona_21_warstwy.png` | zaakceptowana (13.11, warstwy) | bez okna, deszcz tylko w tekście / no window, rain only in text |
| 22 | Leo siada na schodku z zeszytem, Amelia smutna / Leo sits down quietly | WARSTWY: tło 44370eb9-9dcb-4097-9df3-b5a49e6f94a6 + postacie (warstwy/s22.json) | — | `warstwy/strona_22_warstwy.png` | zaakceptowana (13.11, warstwy) | to samo tło schodów co 19–24 / same stairs background |
| 23 | Leo pyta „Czego potrzebujesz?”, Amelia zaskoczona, Lumi otwiera oko / Leo asks | WARSTWY: tło 44370eb9-9dcb-4097-9df3-b5a49e6f94a6 + postacie (warstwy/s23.json) | — | `warstwy/strona_23_warstwy.png` | zaakceptowana (13.11, warstwy) | to samo tło schodów co 19–24 / same stairs background |
| 24 | Leo pokazuje gwiazdkę, Amelia się uśmiecha, Lumi świeci / Leo points at the star | WARSTWY: tło 44370eb9-9dcb-4097-9df3-b5a49e6f94a6 + postacie (warstwy/s24.json) | — | `warstwy/strona_24_warstwy.png` | zaakceptowana (13.11, warstwy) | to samo tło schodów co 19–24 / same stairs background |
| 25 | Cichy kącik z poduszką, obrazkowy plan dnia, Leo i pani obok / Quiet corner, picture plan | 6c2cf30e-10ac-4121-9c43-a1202919eeb8 | 2 | `strony/gotowe/strona_25_podglad.png` | zaakceptowana (13.11) | kolce Lumi już opadły; tekst u góry po lewej |
| 28 | Podwórko jak na stronie 17: Amelia pokazuje gwiazdy, Leo rysuje kredą / Playground, chalk stars | WARSTWY: tło b4633e1c-3a6b-4568-95ed-bb836275d3cf/0 (ze strony 17) + postacie (warstwy/s28.json) | — | `warstwy/strona_28_warstwy.png` | zaakceptowana (13.11, warstwy) | bez biedronki i kosa / no ladybug or blackbird |
