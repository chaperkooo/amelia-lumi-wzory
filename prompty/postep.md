# Postęp ilustracji / Illustration progress

Strony 9–19 zrobione przez Ace Data Cloud zostały ODRZUCONE: postacie za bardzo różnią się od wzorów
(twarz, oczy, włosy, wygląd Lumi, styl kreski). Nie używać ich ani tamtych ustawień (`--iw 0.25`, `--sref` ze stron).

Wracamy do sposobu, który zadziałał przy stronach 3–8:
- midjourney.com (V8), Weirdness 0, Relax
- „Attach to prompt”: 1. amelia_01_radosna_WZOR, 2. wzór Lumi (spokojny albo kolczasty)
- prompt: „the girl from the first image… the creature from the second image…” + stałe opisy postaci
- Lumi unosi się obok Amelii, „the size of an apple”
- miejsce na tekst robimy na końcu w edytorze (Scale, przesunięcie w dół, Erase starego tła, zakaz ram)

## Wnioski z 12.11.2026 (strony 9–10) / Lessons
- Amelia SAMA na pierwszym planie = zgodna ze wzorem. Gdy inne dzieci jej dotykają / tłoczą się wokół niej,
  włosy robią się złote/rude i twarz się zmienia. Inne postacie zawsze kilka kroków dalej, w tle.
- Słowo „knot / tangled” robi z Lumi warkocz albo bułkę. Nie używać.
- Kolczasty Lumi wychodzi dobrze tylko z wzorem lumi_03_kolczasty w „Attach to prompt”
  (sam opis daje puszystą kulkę albo „ciastko”). Edytor (Open Editor) też ma „Attach to prompt”.
- W edytorze: Smart Select świetnie zaznacza Lumi i podłogę jednym kliknięciem. Pędzel ~100 px.
  Scale 73% + przesunięcie na dół = ok. 1/3 strony wolne na tekst.

## Jak dodać kolczastego Lumi bez wgrywania pliku / Spiky Lumi without uploading
- Oryginał lumi_03_kolczasty jest w galerii Midjourney: job 2ef3df6f-d611-4f68-a3d8-376ffc7729af (index 0, 24.09.2026,
  folder „Amelia and Lumi”). Organize → szukaj „pinecone”.
- Przeciągnąć obrazek z galerii na pole „Attach to prompt” (najpierw kliknąć Amelię z biblioteki, potem przeciągnąć Lumi).
- Kłódka (lock) przy załącznikach = zostają po wysłaniu, można puścić kilka stron pod rząd.
- Edytor ma osobne załączniki (tylko pliki z biblioteki), więc Lumi trzeba mieć dobrego już w wygenerowanym obrazku.

## Wszystkie wzory są w Midjourney / All references are in Midjourney
- Organize → Folders → „Amelia and Lumi” (28 obrazków): wszystkie emocje Amelii 02–08, sceny razem_01, Lumi kolczasty.
- Biblioteka „Attach to prompt” ma tylko 3: Leo, Amelia WZOR, Lumi spokojny. Resztę przeciągać z folderu na pole „Attach to prompt”.
- Wgrać pliku z GitHuba nie da się (Midjourney wymaga akcji człowieka), ale nie trzeba — oryginały są w folderze.
- UWAGA: generowanie przy otwartym folderze dopisuje nowe obrazki do folderu. Generować ze strony Create.

## Biblioteka wzorów w Midjourney (od 12.11, wgrane przez użytkownika) / Reference library
Panel „Add images” (ikonka po lewej od pola promptu). Kolejność (najnowsze pierwsze, może się przesunąć po nowym wgraniu):
- rząd 1: amelia_02_zlosc, 3× razem_01_ogrod, lumi_03_kolczasty, lumi_02_emocje_sciaga, amelia_07_placz_skulona_a,
  amelia_08_spokoj(?), amelia_06_placz_stojac, amelia_05_smutek_a, amelia_07_placz_skulona_b
- rząd 2: amelia_03_zagubiona_a, amelia_05_smutek_b, amelia_04_halas_a, amelia_04_halas_b, amelia_03_zagubiona_b,
  leo_01_spokojny_WZOR, amelia_01_radosna_WZOR, lumi_01_spokojny_WZOR
- Do każdej strony: wzór Amelii z WŁAŚCIWĄ emocją + właściwy Lumi. Panel zamykać przyciskiem ikonki (nie krzyżykiem — zasłonięty).

## Wnioski cd. / More lessons
- Gdy Lumi „przytula się” do Amelii (snuggled, touching), robi się wielki jak jej tułów. Zawsze „floating in the air beside…”, „the size of the girl's fist”.
- „dim room” przyciemnia włosy Amelii na brązowo. Używać „soft warm light” i --no dark hair, brown hair.
- Złość / emocje: dodać „the girl's hair is neat and smooth, not fluffy” i --no messy hair.
- Edytor: pociągnięcie gumką zaczynać daleko od rogów obrazka — start przy rogu obraca obrazek o 90°.

## GOTOWE KANDYDATY (12.11.2026) / Candidates
- Strona 9: job 28b911b5-4685-43b0-9b98-815d7156a48a, index 0 (baza: 82d1ae9e-0608-425c-9832-2c20f5e64d96 index 0).
  Amelia OK, Lumi kolczasty OK (odrobinę jaśniejszy/złotawy), miejsce na tekst u góry ok. 1/4 strony.
- Strona 10: job 603c11f4-577c-4ee0-a512-cdbbf69f8655, index 0 (baza: d1971cbb-ba4a-4314-a38c-d0290d6cbb03 index 3).
  Amelia OK, Lumi kolczasty OK, dużo miejsca na tekst u góry.
- W obu: delikatna pionowa linia narożnika ściany u góry.

## Stan (wcześniejszy) / Earlier status
- Strona 9: kandydat = job 28f05396-3f97-4a16-8462-ea8af1b44af0, wersja 2 (index=1).
  Amelia OK. Lumi kształt OK, kolor za żółty (ochra) → poprawić w edytorze z wzorem lumi_03.
  Brak jeszcze miejsca na tekst.
- Strona 10: baza = job fb063e67-69e8-46f5-80f6-588a338a9a85, wersja 1 (Amelia sama z przodu, dzieci i mama w tle).
  Edycja 7b1436ea-572a-492a-96b8-b5b29d4aba85: miejsce na tekst + beżowa podłoga OK, ale Lumi wygląda jak ciastko → poprawić z wzorem lumi_03.
- Czekamy, aż użytkownik wgra lumi_03_kolczasty.png do biblioteki Midjourney.

## Wnioski 12.11 popołudnie / Afternoon lessons
- Scena w klasie: NIE pokazywać Amelii twarzą do nas, a reszty klasy tyłem (wygląda, jakby siedziała tyłem do wszystkich).
  Dobrze: „classroom seen from the front, from where the teacher stands, all children facing forward towards the viewer”, nauczyciel z boku.
- Każda strona: wzór Amelii z właściwą emocją z biblioteki + właściwy Lumi (kolczasty przy hałasie/złości, spokojny przy smutku).

## Praktyczne w przeglądarce / Browser practicalities (12.11)
- Pracować partiami: wysłać kilka stron pod rząd (Relax wykonuje po kolei), potem sprawdzić wszystkie.
- Przed wysłaniem powiększyć pole promptu: czy właściwe wzory, w dobrej kolejności, czy prompt wpisał się cały
  (wpisywanie długiego promptu czasem zgłasza błąd „timeout”, a tekst i tak się wpisuje).
- Kolejność miniatur w bibliotece zmienia się po wgraniu nowych — wybierać po wyglądzie.
- Panel biblioteki zamykać klawiszem Escape albo ikonką obrazka (krzyżyk bywa zasłonięty).
- Duży podgląd: strzałki ← → przełączają 4 wersje; ikonka folderu dodaje do folderu (sprawdzić, czy pojawiła się etykieta folderu).
- Edytor ma własne załączniki tylko z biblioteki — obrazków z galerii nie da się tam dołączyć.
- Po wpisaniu promptu w edytorze i „Submit edit” licznik „Create 0/1” przy menu pokazuje, że zadanie ruszyło.
- Do folderu „KSIAZKA strony gotowe” dodawać dopiero po akceptacji (od 12.11; strony 15–19 trafiły tam wcześniej — usunąć, jeśli odrzucone).

## Rygor 95% twarzy i detali (od 12.11, prośba użytkownika) / 95% face and detail rigor
- Każda twarz: oczy, brwi, nos, usta; Lumi: oczy i usta. Brak któregokolwiek = odrzucenie.
- Do promptu dopisywać TWARZE (stały opis w instrukcjach) i konkretną mimikę (brwi, usta, łzy).
- W --no tylko „faceless”; nigdy osobno face, mouth, eyes, nose.
- Amelia ≥ ok. 1/3 wysokości obrazka, żeby mimika była czytelna.
- Ponowne sprawdzenie stron 15–19 tym rygorem: 15 OK; 16 włosy za bujne; 17 dzieci w tle bez czytelnych twarzy;
  18 twarz Amelii i usta Lumi za małe; 19 nie widać szelek (zasłonięte rękami).

## Wnioski 13.11 / Lessons
- Schody: „closed wooden staircase, a solid wooden slope with closed sides, no railing and no balusters” + --no railing, balusters, banister. Poręcze dawały pionowe linie w miejscu na tekst.
- Lumi bez łapek: „a simple round ball with no arms and no legs” + --no paws.
- Szelki przy skulonej pozie: „arms hugging her shins low, so … both dungaree straps are clearly visible”.
- Twarz czytelna: „the girl fills about half of the picture height” albo „medium-wide view”.
- Klasa: wzór amelia_05_smutek (stojąca) daje lepszą twarz niż siedząca; Lumi „on top of her desk” zamiast „next to her hands”.
