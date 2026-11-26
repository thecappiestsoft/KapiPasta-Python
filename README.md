# KapiPasta - Python 🐍

Aplikacja do nauki Pythona z grywalizacją i kapibarą Kapi. Wygląda jak IDE (w stylu PyCharm), ma 9 rozdziałów, 29 lekcji i 522 zadania (PL + EN), po 18 w każdej lekcji. Kod uczniów uruchamia się naprawdę, w przeglądarce, przez [Pyodide](https://pyodide.org).

To statyczna strona: bez serwera, bez bazy i bez kroku budowania w przeglądarce. Wystarczy GitHub Pages.

© 2026 CappySoft.pl

---

## Struktura projektu

```
index.html                  ← strona startowa (GitHub Pages serwuje ją z katalogu głównego)
.nojekyll                   ← wyłącza Jekylla na GitHub Pages
css/
  styles.css                ← cały wygląd: motywy (zmienne CSS), układ IDE, sceny
js/
  data/course.js            ← WYGENEROWANE przez tools/build.py (lekcje PL+EN + runner) – nie edytuj ręcznie
  i18n.js                   ← teksty interfejsu PL/EN, nazwy poziomów, odznaki
  scenes.js                 ← rysunek kapibary (SVG) i animowane sceny do przykładów
  app.js                    ← stan, XP/poziomy/odznaki, Pyodide, widoki, zadania, eksport postępu
  teacher.js                ← panel nauczyciela (PIN, import plików, tabela klasy, CSV)
python/
  runner.py                 ← „piaskownica”: uruchamia kod ucznia, łapie input/print/błędy
content/
  pl/part1_….py             ← PEŁNA treść kursu po polsku (rozdziały 1–3)
  pl/part2_….py             ← rozdziały 4–6
  pl/part3_….py             ← rozdziały 7–9
  pl/part4_dodatkowe.py     ← zadania dopisywane na końcu lekcji (słownik EXTRA)
  en/part*.py               ← tłumaczenie EN (nadpisuje pola wersji PL)
  both/part5_poziom2i3.py   ← zadania DWUJĘZYCZNE poziomu 2 i 3: pola jako krotki ('polski', 'English')
tools/
  build.py                  ← sprawdza CAŁĄ treść (uruchamia każdy przykład i rozwiązanie) i generuje js/data/course.js
  bundle.py                 ← skleja wszystko w jeden plik dist/kapipasta.html (opcjonalnie)
.github/workflows/verify.yml ← CI: przy każdym pushu sprawdza treść kursu
```

## Uruchomienie lokalne

```bash
python3 -m http.server 8000
# otwórz http://localhost:8000
```

Strona działa też po zwykłym otwarciu `index.html`, ale Pyodide (uruchamianie kodu) wymaga serwera http(s).

## Publikacja na GitHub Pages

1. Utwórz repozytorium i wrzuć do niego zawartość tego folderu (`index.html` musi być w katalogu głównym).
2. **Settings → Pages → Build and deployment → Source: „Deploy from a branch”**, gałąź `main`, folder `/ (root)`.
3. Po chwili aplikacja będzie pod adresem `https://<login>.github.io/<repo>/`.

## Edycja treści (lekcje i zadania)

Treść jest w plikach Pythona w `content/`. Po każdej zmianie uruchom:

```bash
python3 tools/build.py          # sprawdza + generuje js/data/course.js
python3 tools/build.py --check  # tylko sprawdza (tego używa CI)
```

`build.py` **uruchamia** każdy przykład i każde zadanie. Sprawdza, czy:
- poprawna odpowiedź quizu to faktycznie wynik programu (i czy inna opcja nie jest przypadkiem też poprawna),
- kod z uzupełnionymi lukami działa i daje oczekiwany wynik,
- błąd w zadaniu „znajdź błąd” występuje w zaznaczonej linii,
- rozwiązanie wzorcowe przechodzi wszystkie testy, a kod startowy ich NIE przechodzi.

Wyniki przykładów i komunikaty błędów są dopisywane automatycznie, więc nie trzeba ich wpisywać ręcznie.

### Rozdział

```python
CH.append(dict(
  id='petle',                                   # stałe ID (używane w postępie uczniów!)
  icon=dict(rpg='🌀', space='🌌', neutral='🔁'), # ikona w każdym motywie
  name=dict(rpg='Wir Powtórzeń', space='Mgławica Pętli', neutral='Pętle'),
  topic='for, range, while, break, continue',
  lessons=[ ... ]))
```

### Lekcja

```python
dict(id='for', title='for i range()',
     theory="""<p>HTML z teorią…</p>""",
     more="""<p>Dodatkowe treści – rozwinięte od etapu „Praktyk”</p>""",
     ex=[ dict(code='''for i in range(3):\n    print(i)''',
               inp='',            # opcjonalne dane do input()
               lvl=2,             # opcjonalnie: przykład tylko od etapu 2
               scene=dict(s='loop', items=['🍊','🍊','🍊'], cap='Podpis sceny')) ],
     tasks=[ ... ])
```

### Zadania

Każde zadanie ma `t` (typ), `l` (poziom 1–3: Odkrywca / Praktyk / Mistrz) i `q` (treść, HTML). Uczeń widzi zadania o poziomie ≤ wybranego etapu.

**Reguła (pilnowana przez `build.py`):** każda lekcja ma dokładnie **18 zadań = 6 × poziom 1 + 6 × poziom 2 + 6 × poziom 3**. Dzięki temu Odkrywca ma 6 zadań w lekcji, Praktyk 12, a Mistrz 18.

Zadania w `content/both/` piszesz raz, w dwóch językach naraz, np. `q=('Co wypisze program?', 'What will the program print?')`. Kod bez polskich słów może być zwykłym tekstem. Testy z `o='@'` mają oczekiwany wynik liczony automatycznie z rozwiązania wzorcowego.

| typ | pola | opis |
|---|---|---|
| `quiz` | `code?`, `opts`, `a` (indeks poprawnej), `out=True` (opcje to wynik programu), `err=True` (opcje to typ błędu), `inp?`, `why` | kolejność opcji jest losowana w aplikacji |
| `fill` | `code` z `___` jako lukami, `ans=[[warianty luki 1], …]`, `expect?`, `run=False?`, `why` | porównanie ignoruje spacje i rodzaj cudzysłowu |
| `bug` | `code`, `line` (0-indeksowana), `fix`, `why`, `noerr=True` (błąd logiczny), `cause=True` (Python zgłasza błąd w innej linii niż przyczyna) | komunikat błędu Pythona generuje się sam |
| `code` | `start`, `tests=[dict(i='wejście', o='oczekiwane wyjście')]`, `check?` (asserty po kodzie), `setup?` (np. tworzy plik), `sol`, `hint` | w `check` dostępne są `__src` (kod ucznia) i `__out` (jego wyjście) |

⚠️ **Nie zmieniaj kolejności zadań w opublikowanej lekcji.** ID zadania to `idLekcji-indeks`, więc postęp uczniów jest przypisany do pozycji. Nowe zadania najlepiej dopisywać na końcu lekcji.

### Sceny z kapibarą (`scene=dict(s=…)`)

`say` (tabliczka z wynikiem) · `boxes` (zmienne jako pudełka) · `cards` (wyrażenie → wynik) · `share` (dzielenie // i %) · `fork` (if/else) · `ladder` (if/elif) · `row` (indeksy, wycinki) · `loop` (animacja pętli, opcjonalnie `acc`/`accv`) · `grid` (pętle zagnieżdżone) · `venn` (zbiory) · `dict` (szuflady słownika) · `machine` (funkcja) · `scope` (zasięg) · `dice` (random) · `file` (plik) · `err` (try/except) · `search` (wyszukiwanie) · `sort` (bąbelkowe) · `stack` (rekurencja).

Każda scena przyjmuje `cap` (podpis). Pozostałe pola zależą od typu; najlepiej skopiować istniejący przykład. Nowy typ sceny dodajesz jako kolejny `case` w `renderScene()` w `js/scenes.js`.

### Tłumaczenie (EN)

`content/en/*.py` zawiera `CHAPTERS` i `LESSONS` w tej samej kolejności co wersja PL. Wpisujesz tylko pola, które się zmieniają (np. `q`, `why`, `code`, `opts`). Reszta (`a`, `line`, `l`…) jest brana z wersji polskiej. Liczba przykładów i zadań musi się zgadzać, inaczej `build.py` zgłosi błąd.

Kolejny język: dodaj `content/<kod>/`, rozszerz `tools/build.py` (słownik `CHS`) i dopisz teksty w `js/i18n.js` (`UI.<kod>`, `WORDS`, `BADGES`).

## Interfejs, motywy, grywalizacja

- **Teksty UI** → `js/i18n.js` (`UI.pl`, `UI.en`). W kodzie używaj `tr('klucz')`.
- **Motywy** → `css/styles.css`, sekcja „themes”: klasy `.rpg/.space/.neutral` × `.light/.dark` definiują zmienne CSS (kolory IDE i kolorowania składni).
- **Nazwy poziomów i rozdziałów w motywach** → `WORDS` w `js/i18n.js`.
- **Odznaki** → `BADGES` w `js/i18n.js` (warunek `f` dostaje statystyki ucznia).
- **XP** → `BASE` i `award()` w `js/app.js`. Progi poziomów → `LVT()`.
- **Cel dnia** (50 XP) → `addXP()` w `js/app.js`.

## Skala ocen 1–6

Liczona w `gradeOf()` w `js/app.js` dla lekcji, rozdziału i całego kursu, zawsze z zadań etapu ucznia.

**Ustawienia** (Panel nauczyciela → ⚙️ Ustawienia oceniania):

| ustawienie | domyślnie | do wyboru |
|---|---|---|
| progi % dla ocen 2 / 3 / 4 / 5 | 30 / 50 / 75 / 90 | dowolne rosnące 1–100 |
| ocena 6 | 100% zadań, wszystkie za 1. razem | 100% zadań i min. 90% za 1. razem |
| zadanie rozwiązane po podejrzeniu rozwiązania | ½ pkt | 0 / ½ / 1 pkt |

W tym samym miejscu nauczyciel może **odblokować wybrane działy** (🔓 Odblokowane działy). Uczniowie z kodem klasy mają je dostępne od razu, bez kończenia poprzedniego działu. Domyślnie kolejny dział odblokowuje się po zrobieniu 50% poprzedniego.

Nauczyciel generuje z tych ustawień **kod klasy** (`KAPICFG.…`). Uczeń wkleja go w Ustawienia → Mój postęp → Kod klasy, żeby u siebie widzieć oceny według tej samej skali.

Gwiazdki: ★★★ = 100% zadań wykonanych, ★★★ + kapibara w biretce = ocena 6, ★★½ = 5, ★★ = 4, ★½ = 3, ★ = 2, ½★ = rozpoczęte.

**Progi domyślne w zadaniach (½ pkt za podgląd):**

| ocena | próg | Odkrywca (6) | Praktyk (12) | Mistrz (18) |
|---|---|---|---|---|
| 6 | 100% + bezbłędnie | 6 bezbłędnie | 12 bezbłędnie | 18 bezbłędnie |
| 5 | ≥ 90% | 5,5 | 11 | 16,5 |
| 4 | ≥ 75% | 4,5 | 9 | 13,5 |
| 3 | ≥ 50% | 3 | 6 | 9 |
| 2 | ≥ 30% | 2 | 4 | 5,5 |
| 1 | < 30% | mniej | mniej | mniej |

## Czas i wychodzenie z aplikacji

- Czas jest liczony osobno dla każdego zadania: od pokazania do poprawnej odpowiedzi, bez czasu spędzonego poza aplikacją. Jeden ciągły odcinek liczy się maksymalnie przez 15 min.
- Wyjście z okna lub przełączenie karty (`blur` / `visibilitychange`) trwające ≥ 2 s jest liczone. Zapisywane są łączna liczba i czas, a także liczba i czas w każdej lekcji. Uczeń widzi komunikat, że nauczyciel to zobaczy.
- Dane trafiają do pliku postępu (`time`, `away`, `awayL`). Panel nauczyciela pokazuje je w tabeli, w szczegółach ucznia i w eksporcie CSV.

## Uruchamianie Pythona

`js/app.js` → obiekt `Py`: ładuje Pyodide z CDN w Web Workerze (z limitem czasu). Jeśli worker nie zadziała, ładuje go w głównym wątku. Kod ucznia wykonuje `python/runner.py`: podstawia `input()` danymi z pola „Dane wejściowe”, przechwytuje `print`, ogranicza liczbę wykonanych linii (ochrona przed nieskończonymi pętlami) i zwraca numer linii błędu. Ten sam runner wykorzystuje `tools/build.py`, więc testy lokalne i w przeglądarce działają identycznie.

## Postęp ucznia i panel nauczyciela

- Postęp zapisuje się w `localStorage` przeglądarki (klucz `pykapi-v1`, panel nauczyciela `pykapi-teacher-v1`).
- **Mój postęp** eksportuje zakodowany plik `.txt` (format `PYKAPI1.<z|p>.<suma>.<dane>`): JSON → deflate → XOR → base64url + suma kontrolna FNV. Chroni to przed przypadkową lub ręczną edycją, ale nie jest kryptograficznym zabezpieczeniem.
- **Panel nauczyciela** (PIN zapisany lokalnie jako skrót): import wielu plików lub kodów, tabela klasy, mapa postępu w rozdziałach, najtrudniejsze zadania, szczegóły ucznia, eksport CSV.
- ⚠️ Nie zmieniaj `SALT` ani formatu `payload()` w `js/app.js`, bo stare pliki uczniów przestaną się wczytywać. Nowe pola dodawaj tak, żeby stare pliki nadal działały.

## Licencja

MIT – zob. plik [LICENSE](LICENSE). © 2026 CappySoft.pl
