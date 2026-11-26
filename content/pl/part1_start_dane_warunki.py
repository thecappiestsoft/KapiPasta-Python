# Treść kursu KapiPasta - Python (PL). Format opisany w README.md -> "Edycja treści".
# Po zmianach uruchom: python3 tools/build.py

CH = []

CH.append(dict(
 id='start', icon=dict(rpg='🏡', space='🛰️', neutral='▶️'),
 name=dict(rpg='Wioska Startowa', space='Stacja Orbitalna', neutral='Start'),
 topic='print, komentarze, f-stringi',
 lessons=[
 dict(id='print', title='print i komentarze',
  theory="""<p><code>print()</code> to głos programu – wypisuje na ekran to, co dostanie w nawiasie. Tekst zapisujemy w cudzysłowie: <code>"..."</code> albo <code>'...'</code>.</p>
<p>Kilka wartości oddzielamy przecinkiem – Python wstawi między nie spację.</p>
<p>Wszystko po znaku <code>#</code> to <b>komentarz</b> – notatka dla człowieka. Python ją ignoruje.</p>""",
  more="""<p><code>print</code> ma dwa przydatne parametry: <code>sep</code> – czym oddzielić wartości (domyślnie spacja) i <code>end</code> – co dopisać na końcu (domyślnie znak nowej linii <code>\\n</code>).</p>""",
  ex=[
   dict(code='''# Kapi wita się ze światem
print("Cześć, jestem Kapi!")
print("Mam", 3, "pomarańcze")  # przecinki dają spacje''',
        scene=dict(s='say', cap='Kapi trzyma tabliczkę i pokazuje wszystko, co wypisał print.')),
   dict(code='''print("ko", "ko", "ko", sep="-")
print("Kapi", end=" ")
print("pływa")''', lvl=2,
        scene=dict(s='say', cap='sep klei słowa myślnikiem, a end sprawia, że drugi print pisze w tej samej linii.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='print("Kapi", "lubi", "arbuzy")',
        opts=['Kapi lubi arbuzy', 'Kapilubiarbuzy', '"Kapi" "lubi" "arbuzy"', 'Kapi, lubi, arbuzy'], a=0, out=True,
        why='Przecinki w print wstawiają pojedynczą spację między wartościami.'),
   dict(t='quiz', l=1, q='Co zrobi Python z tą linią?', code='# print("Ukryta wiadomość")',
        opts=['Nic nie wypisze – to komentarz', 'Wypisze: Ukryta wiadomość', 'Zgłosi błąd', 'Wypisze: # print("Ukryta wiadomość")'], a=0,
        why='Znak # zaczyna komentarz – Python pomija resztę linii.'),
   dict(t='fill', l=1, q='Uzupełnij, aby program wypisał: Hej!', code='___("Hej!")', ans=[['print']],
        why='Do wypisywania służy funkcja print.'),
   dict(t='bug', l=1, q='Program miał się przywitać, ale Python zgłasza błąd. Kliknij linię z błędem.',
        code='''print("Dzień dobry")
print("Jestem Kapi)
print("Do zobaczenia")''', line=1, fix='print("Jestem Kapi")',
        why='Brakuje zamykającego cudzysłowu – tekst musi być zamknięty z obu stron.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''print("A", "B", "C", sep="")
print(1, 2, end="!")
print(3)''', opts=['ABC\n1 2!3', 'A B C\n1 2!\n3', 'ABC\n1 2\n!3', 'ABC\n12!3'], a=0, out=True,
        why='sep="" skleja litery, a end="!" zamienia nową linię na wykrzyknik – więc 3 trafia tuż za nim.'),
   dict(t='code', l=1, q='Napisz program, który wypisze w dwóch liniach:<br><code>Kapi</code><br><code>kocha kąpiele</code>',
        start='# Twój kod\n', tests=[dict(i='', o='Kapi\nkocha kąpiele')], sol='print("Kapi")\nprint("kocha kąpiele")',
        hint='Użyj dwóch poleceń print.'),
   dict(t='code', l=3, q='Używając <b>jednego</b> print i parametru <code>sep</code>, wypisz datę <code>20.11.2026</code> z liczb 20, 11 i 2026.',
        start='print(20, 11, 2026)\n', tests=[dict(i='', o='20.11.2026')], check="assert __src.count('print') == 1, 'Użyj tylko jednego print'",
        sol='print(20, 11, 2026, sep=".")', hint='sep="." wstawia kropkę między wartościami.'),
  ]),
 dict(id='fstr', title='f-stringi i formatowanie',
  theory="""<p><b>f-string</b> to tekst z literą <code>f</code> przed cudzysłowem. W nawiasach klamrowych <code>{}</code> wstawiamy zmienne albo całe wyrażenia – Python podmieni je na wartości.</p>
<p><code>f"Mam {ile} lat"</code> – zamiast <code>{ile}</code> pojawi się liczba.</p>""",
  more="""<p>Po dwukropku można dodać format: <code>{x:.2f}</code> – 2 miejsca po przecinku, <code>{x:5}</code> – szerokość 5 znaków, <code>{x:>5}</code>/<code>{x:<5}</code>/<code>{x:^5}</code> – do prawej, lewej, środka.</p>""",
  ex=[
   dict(code='''imie = "Kapi"
wiek = 4
print(f"{imie} ma {wiek} lata")
print(f"Za rok będzie mieć {wiek + 1}")''',
        scene=dict(s='say', cap='Kapi wkłada wartości zmiennych w puste {} na tabliczce.')),
   dict(code='''cena = 3.14159
print(f"Arbuz kosztuje {cena:.2f} zł")
print(f"[{'Kapi':^8}]")''', lvl=2,
        scene=dict(s='say', cap=':.2f zaokrągla do 2 miejsc, a :^8 ustawia napis na środku pola o szerokości 8.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 7
print(f"Kapi zjadł {x} jabłek")''',
        opts=['Kapi zjadł 7 jabłek', 'Kapi zjadł {x} jabłek', 'Kapi zjadł x jabłek', 'f"Kapi zjadł 7 jabłek"'], a=0, out=True,
        why='W f-stringu {x} zostaje zamienione na wartość zmiennej x.'),
   dict(t='quiz', l=1, q='Co wypisze program (bez litery f)?', code='''x = 7
print("Mam {x} kaczek")''',
        opts=['Mam {x} kaczek', 'Mam 7 kaczek', 'Błąd', 'Mam x kaczek'], a=0, out=True,
        why='Bez litery f nawiasy klamrowe są zwykłymi znakami – nic nie jest podmieniane.'),
   dict(t='fill', l=1, q='Uzupełnij, żeby wypisało: Kapi ma 5 lat', code='''wiek = 5
print(___"Kapi ma {wiek} lat")''', ans=[['f']], why='Litera f przed cudzysłowem włącza podmianę {}.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''a = 2
b = 3
print(f"{a} * {b} = {a * b}")''', opts=['2 * 3 = 6', 'a * b = 6', '2 * 3 = a * b', '6 = 6'], a=0, out=True,
        why='W {} można wpisać całe wyrażenie – Python je obliczy.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''x = 2 / 3
print(f"{x:.3f}")''', opts=['0.667', '0.666', '0.67', '0.6666666666666666'], a=0, out=True,
        why='.3f oznacza 3 miejsca po przecinku z zaokrągleniem.'),
   dict(t='bug', l=2, q='Program powinien wypisać cenę z 2 miejscami po przecinku. Która linia psuje wynik?',
        code='''cena = 4.5
ile = 3
print(f"Razem: {cena * ile:.2f}")
print(f"Średnio: {cena:2f}")''', line=3, noerr=True, fix='print(f"Średnio: {cena:.2f}")',
        why='Brakuje kropki: :2f to szerokość 2, a nie 2 miejsca po przecinku. Program nie zgłasza błędu, ale wypisuje 4.500000.'),
   dict(t='code', l=1, q='Zmienne <code>imie = "Kapi"</code> i <code>owoc = "mandarynki"</code> już są. Wypisz f-stringiem:<br><code>Kapi lubi mandarynki</code>',
        start='imie = "Kapi"\nowoc = "mandarynki"\n', tests=[dict(i='', o='Kapi lubi mandarynki')],
        check="assert 'f\"' in __src or \"f'\" in __src, 'Użyj f-stringa'",
        sol='imie = "Kapi"\nowoc = "mandarynki"\nprint(f"{imie} lubi {owoc}")', hint='print(f"{imie} lubi ...")'),
   dict(t='code', l=3, q='Mając <code>r = 2.5</code>, wypisz pole koła (pi przyjmij 3.14159) z dokładnością do 2 miejsc:<br><code>Pole: 19.63</code>',
        start='r = 2.5\n', tests=[dict(i='', o='Pole: 19.63')], sol='r = 2.5\nprint(f"Pole: {3.14159 * r ** 2:.2f}")',
        hint='Pole = pi * r ** 2, format :.2f'),
  ]),
 ]))

CH.append(dict(
 id='dane', icon=dict(rpg='🌲', space='🪐', neutral='📦'),
 name=dict(rpg='Las Danych', space='Planeta Danych', neutral='Dane'),
 topic='zmienne, typy, input, operatory',
 lessons=[
 dict(id='zmienne', title='Zmienne i typy',
  theory="""<p><b>Zmienna</b> to pudełko z nazwą, w którym trzymamy wartość: <code>owoce = 5</code>. Znak <code>=</code> znaczy „włóż do pudełka”, a nie „równa się”.</p>
<p>Podstawowe typy:</p><ul><li><code>int</code> – liczba całkowita: <code>5</code></li><li><code>float</code> – liczba z kropką: <code>2.5</code></li><li><code>str</code> – tekst: <code>"Kapi"</code></li><li><code>bool</code> – prawda/fałsz: <code>True</code>, <code>False</code></li></ul>
<p>Typ sprawdzisz funkcją <code>type()</code>.</p>""",
  more="""<p>Nazwy zmiennych: litery, cyfry i <code>_</code>, nie mogą zaczynać się cyfrą. Wielkość liter ma znaczenie: <code>kapi</code> i <code>Kapi</code> to dwie różne zmienne. Można przypisać kilka naraz: <code>a, b = 1, 2</code>, a zamiana miejscami to <code>a, b = b, a</code>.</p>""",
  ex=[
   dict(code='''imie = "Kapi"
wiek = 4
waga = 55.5
glodny = True
print(type(imie), type(wiek))
print(type(waga), type(glodny))''',
        scene=dict(s='boxes', vars=[['imie', '"Kapi"', 'str'], ['wiek', '4', 'int'], ['waga', '55.5', 'float'], ['glodny', 'True', 'bool']],
                   cap='Kapi chowa wartości do pudełek. Kolor pudełka to typ danych.')),
   dict(code='''owoce = 3
owoce = owoce + 2
print(owoce)''',
        scene=dict(s='boxes', vars=[['owoce', '3 → 5', 'int']], cap='Kapi wyjmuje 3 owoce, dokłada 2 i wkłada z powrotem 5. Stara wartość znika.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Jakiego typu jest wartość <code>3.0</code>?', opts=['float', 'int', 'str', 'bool'], a=0,
        why='Kropka dziesiętna oznacza float, nawet gdy po niej jest 0.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 10
x = x - 4
print(x)''', opts=['6', '10', '-4', 'x - 4'], a=0, out=True, why='Najpierw x = 10, potem nowa wartość 10 - 4 = 6 zastępuje starą.'),
   dict(t='quiz', l=1, q='Jakiego typu jest <code>"42"</code>?', opts=['str', 'int', 'float', 'bool'], a=0,
        why='Cudzysłów oznacza tekst – nawet gdy w środku są cyfry.'),
   dict(t='fill', l=1, q='Uzupełnij wartością logiczną „prawda”', code='''kapi_lubi_wode = ___
print(kapi_lubi_wode)''', ans=[['True']], why='Wartości logiczne w Pythonie piszemy wielką literą: True i False.'),
   dict(t='bug', l=1, q='Python zgłasza błąd. Która linia jest winna?', code='''owoce = 5
print(Owoce)''', line=1, fix='print(owoce)',
        why='Python rozróżnia wielkość liter. Zmienna Owoce nie istnieje – stąd NameError.'),
   dict(t='quiz', l=3, q='Co wypisze program?', code='''a = 1
b = 2
a, b = b, a
print(a, b)''', opts=['2 1', '1 2', '2 2', '1 1'], a=0, out=True, why='a, b = b, a zamienia wartości miejscami w jednym kroku.'),
   dict(t='code', l=1, q='Utwórz zmienną <code>zwierze</code> z tekstem <code>kapibara</code> i zmienną <code>nogi</code> z liczbą 4. Wypisz je jednym print.',
        start='', tests=[dict(i='', o='kapibara 4')], check="assert zwierze == 'kapibara' and nogi == 4, 'Sprawdź wartości zmiennych'",
        sol='zwierze = "kapibara"\nnogi = 4\nprint(zwierze, nogi)', hint='print(zwierze, nogi)'),
  ]),
 dict(id='input', title='input i konwersja typów',
  theory="""<p><code>input()</code> zatrzymuje program i czeka, aż użytkownik coś wpisze. <b>Zawsze</b> zwraca tekst (<code>str</code>)!</p>
<p>Żeby liczyć, zamieniamy tekst na liczbę: <code>int("5")</code> → <code>5</code>, <code>float("2.5")</code> → <code>2.5</code>. W drugą stronę: <code>str(5)</code> → <code>"5"</code>.</p>
<p>💡 W aplikacji dane do <code>input()</code> wpisujesz w polu <b>Dane wejściowe</b> – każda linia to jedna odpowiedź.</p>""",
  more="""<p>Częsty schemat: <code>n = int(input("Podaj liczbę: "))</code>. Uwaga: <code>"2" + "3"</code> to <code>"23"</code> (sklejanie tekstów), a <code>int("2.5")</code> zgłosi <code>ValueError</code> – do liczb z kropką używaj <code>float</code>.</p>""",
  ex=[
   dict(code='''imie = input("Jak masz na imię? ")
print(f"Cześć, {imie}!")''', inp='Ola',
        scene=dict(s='say', cap='Kapi pyta, czeka na odpowiedź i wita gościa po imieniu.')),
   dict(code='''a = input()
b = input()
print(a + b)
print(int(a) + int(b))''', inp='2\n3',
        scene=dict(s='cards', items=[['"2" + "3"', '"23"', 'teksty się sklejają'], ['int("2") + int("3")', '5', 'liczby się dodają']],
                   cap='Kapi skleja dwie karteczki z cyframi, a potem zamienia je na liczby i dodaje.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Jakiego typu jest wynik <code>input()</code>, gdy użytkownik wpisze 7?', opts=['str', 'int', 'float', 'bool'], a=0,
        why='input() zawsze zwraca tekst. Aby liczyć, użyj int() lub float().'),
   dict(t='quiz', l=1, q='Co wypisze program, gdy użytkownik wpisze kolejno 4 i 4?', code='''a = input()
b = input()
print(a + b)''', inp='4\n4', opts=['44', '8', '4 4', 'Błąd'], a=0, out=True, why='Dodawanie tekstów to sklejanie: "4" + "4" = "44".'),
   dict(t='fill', l=1, q='Uzupełnij, aby program dodawał liczby, a nie sklejał teksty', code='''x = ___(input())
print(x + 1)''', ans=[['int', 'float']], run=False, why='int() zamienia tekst na liczbę całkowitą.'),
   dict(t='bug', l=2, q='Użytkownik wpisuje 2.5. Która linia zgłasza błąd?', code='''t = input()
cena = int(t)
print(cena * 2)''', inp='2.5', line=1, fix='cena = float(t)',
        why='int("2.5") nie zadziała – tekst z kropką zamieniamy przez float().'),
   dict(t='quiz', l=1, q='Co wypisze <code>print(str(3) * 3)</code>?', code='print(str(3) * 3)', opts=['333', '9', '3 3 3', 'Błąd'], a=0, out=True,
        why='str(3) to "3", a tekst razy liczba to powtórzenie: "333".'),
   dict(t='code', l=1, q='Wczytaj imię i wypisz <code>Witaj, IMIĘ!</code><br>Np. dla <code>Ola</code> → <code>Witaj, Ola!</code>',
        start='imie = input()\n', tests=[dict(i='Ola', o='Witaj, Ola!'), dict(i='Kapi', o='Witaj, Kapi!')],
        sol='imie = input()\nprint(f"Witaj, {imie}!")', hint='print(f"Witaj, {imie}!")'),
   dict(t='code', l=2, q='Wczytaj dwie liczby całkowite (każda w osobnej linii) i wypisz ich sumę.',
        start='', tests=[dict(i='3\n4', o='7'), dict(i='10\n-2', o='8')], sol='a = int(input())\nb = int(input())\nprint(a + b)',
        hint='a = int(input())'),
   dict(t='code', l=3, q='Wczytaj wzrost w cm (liczba całkowita) i wagę w kg (może mieć kropkę). Wypisz BMI z 1 miejscem po przecinku: <code>BMI: 22.9</code><br>BMI = waga / (wzrost w metrach)²',
        start='', tests=[dict(i='175\n70', o='BMI: 22.9'), dict(i='160\n50.5', o='BMI: 19.7')],
        sol='w = int(input()) / 100\nm = float(input())\nprint(f"BMI: {m / w ** 2:.1f}")', hint='Zamień cm na metry dzieląc przez 100.'),
  ]),
 dict(id='oper', title='Operatory arytmetyczne',
  theory="""<p>Działania: <code>+</code> <code>-</code> <code>*</code> <code>/</code> oraz trzy specjalne:</p>
<ul><li><code>//</code> – dzielenie całkowite (ile pełnych grup): <code>7 // 2</code> → <code>3</code></li><li><code>%</code> – reszta z dzielenia: <code>7 % 2</code> → <code>1</code></li><li><code>**</code> – potęga: <code>2 ** 3</code> → <code>8</code></li></ul>
<p>Zwykłe <code>/</code> zawsze daje float: <code>6 / 2</code> → <code>3.0</code>.</p>""",
  more="""<p>Kolejność działań: najpierw <code>**</code>, potem <code>* / // %</code>, na końcu <code>+ -</code>. Nawiasy zmieniają kolejność. Skróty: <code>x += 1</code> to <code>x = x + 1</code> (działa też <code>-= *= //= %=</code>). Sztuczka: <code>n % 10</code> to ostatnia cyfra liczby, a <code>n // 10</code> obcina ostatnią cyfrę.</p>""",
  ex=[
   dict(code='''mandarynki = 7
print(mandarynki // 2)  # każda z 2 kapibar dostaje
print(mandarynki % 2)   # zostaje
print(2 ** 3)''',
        scene=dict(s='share', n=7, k=2, cap='Kapi dzieli 7 mandarynek między 2 kapibary: każda dostaje po 3 (//), a 1 zostaje (%).')),
   dict(code='''print(6 / 2)
print(2 + 3 * 4)
print((2 + 3) * 4)
n = 1234
print(n % 10, n // 10)''', lvl=2,
        scene=dict(s='cards', items=[['6 / 2', '3.0', '/ daje float'], ['2 + 3 * 4', '14', 'najpierw mnożenie'], ['(2 + 3) * 4', '20', 'nawias pierwszy'], ['1234 % 10', '4', 'ostatnia cyfra'], ['1234 // 10', '123', 'bez ostatniej cyfry']],
                   cap='Kapi liczy na liczydle – kolejność działań ma znaczenie!')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Ile to <code>17 // 5</code>?', code='print(17 // 5)', opts=['3', '2', '3.4', '4'], a=0, out=True,
        why='17 // 5 to liczba pełnych piątek w 17, czyli 3.'),
   dict(t='quiz', l=1, q='Ile to <code>17 % 5</code>?', code='print(17 % 5)', opts=['2', '3', '3.4', '0'], a=0, out=True,
        why='17 = 3 · 5 + 2, więc reszta to 2.'),
   dict(t='quiz', l=1, q='Ile to <code>3 ** 2</code>?', code='print(3 ** 2)', opts=['9', '6', '5', '32'], a=0, out=True, why='3 do potęgi 2 to 3 · 3 = 9.'),
   dict(t='quiz', l=1, q='Co wypisze <code>print(8 / 2)</code>?', code='print(8 / 2)', opts=['4.0', '4', '4.00', '8/2'], a=0, out=True,
        why='Zwykłe dzielenie / zawsze daje liczbę float.'),
   dict(t='fill', l=1, q='Uzupełnij operator, aby sprawdzić resztę z dzielenia przez 2', code='''n = 9
print(n ___ 2)''', ans=[['%']], expect='1', why='% daje resztę. 9 % 2 = 1, więc 9 jest nieparzyste.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''x = 10
x += 5
x //= 4
print(x)''', opts=['3', '3.75', '15', '4'], a=0, out=True, why='10 + 5 = 15, a 15 // 4 = 3.'),
   dict(t='quiz', l=3, q='Co wypisze <code>print(-7 // 2)</code>?', code='print(-7 // 2)', opts=['-4', '-3', '-3.5', '3'], a=0, out=True,
        why='// zaokrągla zawsze w dół (do mniejszej liczby): -3.5 → -4.'),
   dict(t='code', l=1, q='Kapi ma 23 mandarynki i pakuje je po 5 do koszyka. Wypisz w dwóch liniach: liczbę pełnych koszyków i liczbę mandarynek, które zostały.',
        start='m = 23\n', tests=[dict(i='', o='4\n3')], sol='m = 23\nprint(m // 5)\nprint(m % 5)', hint='Użyj // oraz %.'),
   dict(t='code', l=2, q='Wczytaj liczbę sekund i wypisz ją w formacie <code>M min S s</code>.<br>Np. 135 → <code>2 min 15 s</code>',
        start='s = int(input())\n', tests=[dict(i='135', o='2 min 15 s'), dict(i='59', o='0 min 59 s'), dict(i='600', o='10 min 0 s')],
        sol='s = int(input())\nprint(f"{s // 60} min {s % 60} s")', hint='Minuty to s // 60, sekundy to s % 60.'),
   dict(t='code', l=3, q='Wczytaj liczbę trzycyfrową i wypisz sumę jej cyfr (bez zamiany na tekst!). Np. 472 → <code>13</code>',
        start='n = int(input())\n', tests=[dict(i='472', o='13'), dict(i='100', o='1'), dict(i='999', o='27')],
        check="assert 'str(' not in __src and '[' not in __src, 'Użyj tylko // i %'",
        sol='n = int(input())\nprint(n % 10 + n // 10 % 10 + n // 100)', hint='Ostatnia cyfra: n % 10, środkowa: n // 10 % 10, pierwsza: n // 100.'),
  ]),
 ]))

CH.append(dict(
 id='warunki', icon=dict(rpg='🌉', space='☄️', neutral='🔀'),
 name=dict(rpg='Most Decyzji', space='Pas Asteroid', neutral='Warunki'),
 topic='porównania, and/or/not, if/elif/else',
 lessons=[
 dict(id='logika', title='Porównania i logika',
  theory="""<p>Porównania dają <code>True</code> lub <code>False</code>: <code>==</code> równe, <code>!=</code> różne, <code>&lt;</code> <code>&gt;</code> <code>&lt;=</code> <code>&gt;=</code>.</p>
<p>⚠️ <code>=</code> to przypisanie, <code>==</code> to porównanie!</p>
<p>Łączenie warunków:</p><ul><li><code>and</code> – oba muszą być prawdziwe</li><li><code>or</code> – wystarczy jeden</li><li><code>not</code> – odwraca wartość</li></ul>""",
  more="""<p>Python pozwala łączyć porównania: <code>0 &lt; x &lt; 10</code>. Kolejność: najpierw <code>not</code>, potem <code>and</code>, na końcu <code>or</code>. Teksty porównywane są alfabetycznie: <code>"ala" &lt; "kot"</code> → <code>True</code>.</p>""",
  ex=[
   dict(code='''slonce = True
woda_ciepla = False
print(slonce and woda_ciepla)
print(slonce or woda_ciepla)
print(not woda_ciepla)''',
        scene=dict(s='cards', items=[['True and False', 'False', 'oba muszą być ✔'], ['True or False', 'True', 'wystarczy jeden ✔'], ['not False', 'True', 'odwrócenie']],
                   cap='Kapi kąpie się tylko, gdy świeci słońce I woda jest ciepła. Na spacer idzie, gdy jest słońce LUB ciepło.')),
   dict(code='''temp = 24
print(temp > 20)
print(temp == 25)
print(18 <= temp <= 26)''',
        scene=dict(s='cards', items=[['24 > 20', 'True', ''], ['24 == 25', 'False', ''], ['18 <= 24 <= 26', 'True', 'w przedziale']], cap='Kapi sprawdza termometr przy basenie.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze <code>print(5 == 5.0)</code>?', code='print(5 == 5.0)', opts=['True', 'False', 'Błąd', '5'], a=0, out=True,
        why='Wartości liczbowe są równe, więc wynik to True.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='print(3 > 2 and 1 > 4)', opts=['False', 'True', '1', 'Błąd'], a=0, out=True,
        why='and wymaga, by oba warunki były prawdziwe. 1 > 4 to False.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='print(not (2 > 1) or 3 == 3)', opts=['True', 'False', 'Błąd', 'None'], a=0, out=True,
        why='not True to False, ale 3 == 3 to True, a False or True = True.'),
   dict(t='fill', l=1, q='Uzupełnij operator „różne od”', code='''x = 4
print(x ___ 5)''', ans=[['!=']], expect='True', why='!= oznacza „różne od”.'),
   dict(t='bug', l=1, q='Python zgłasza błąd składni. Kliknij winną linię.', code='''x = 7
if x = 7:
    print("siedem")''', line=1, fix='if x == 7:',
        why='Pojedyncze = to przypisanie. Do porównania potrzeba ==.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''x = 15
print(10 < x < 20, x % 2 == 0)''', opts=['True False', 'True True', 'False False', 'False True'], a=0, out=True,
        why='15 leży między 10 a 20, ale nie jest parzyste.'),
   dict(t='quiz', l=3, q='Co wypisze program?', code='print(True or False and False)', opts=['True', 'False', 'Błąd', 'None'], a=0, out=True,
        why='and ma pierwszeństwo: False and False = False, potem True or False = True.'),
   dict(t='code', l=2, q='Wczytaj liczbę i wypisz <code>True</code>, jeśli jest parzysta i większa od 10, w przeciwnym razie <code>False</code> (bez if!).',
        start='n = int(input())\n', tests=[dict(i='12', o='True'), dict(i='8', o='False'), dict(i='13', o='False')],
        sol='n = int(input())\nprint(n % 2 == 0 and n > 10)', hint='print(warunek1 and warunek2)'),
  ]),
 dict(id='if', title='if, elif, else',
  theory="""<p><code>if</code> wykonuje kod tylko, gdy warunek jest prawdziwy. Po warunku stawiamy <b>dwukropek</b>, a kod w środku <b>wcinamy</b> (4 spacje).</p>
<pre>if warunek:
    zrób_to
elif inny_warunek:
    zrób_tamto
else:
    w_każdym_innym_przypadku</pre>
<p>Python sprawdza warunki od góry i wykonuje <b>tylko pierwszy</b> pasujący blok.</p>""",
  more="""<p>Warunki można zagnieżdżać – <code>if</code> wewnątrz <code>if</code>. Każdy poziom to kolejne 4 spacje wcięcia. Często zagnieżdżenie da się zastąpić <code>and</code>.</p>""",
  ex=[
   dict(code='''temp = 28
if temp > 25:
    print("Kapi idzie się kąpać 🏊")
else:
    print("Kapi zostaje w norce 🏠")''',
        scene=dict(s='fork', cond='temp > 25', val='True', yes='kąpiel 🏊', no='norka 🏠', cap='Kapi stoi na rozwidleniu. Warunek jest prawdziwy, więc idzie w lewo – do wody.')),
   dict(code='''punkty = 72
if punkty >= 90:
    print("celujący")
elif punkty >= 70:
    print("dobry")
elif punkty >= 50:
    print("dostateczny")
else:
    print("spróbuj jeszcze raz")''',
        scene=dict(s='ladder', steps=[['punkty >= 90', False], ['punkty >= 70', True], ['punkty >= 50', None]], res='dobry',
                   cap='Kapi sprawdza drzwi po kolei. Otwiera pierwsze pasujące – kolejnych już nie sprawdza.')),
   dict(code='''glodny = True
pora = "rano"
if glodny:
    if pora == "rano":
        print("owsianka")
    else:
        print("arbuz")''', lvl=2,
        scene=dict(s='fork', cond='pora == "rano"', val='True', yes='owsianka 🥣', no='arbuz 🍉', cap='Najpierw Kapi sprawdza, czy jest głodny, a dopiero potem wybiera posiłek – to warunek zagnieżdżony.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 3
if x > 5:
    print("duże")
else:
    print("małe")''', opts=['małe', 'duże', 'duże\nmałe', 'nic'], a=0, out=True, why='3 > 5 to False, więc wykonuje się else.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 95
if x > 50:
    print("A")
elif x > 90:
    print("B")
else:
    print("C")''', opts=['A', 'B', 'A\nB', 'C'], a=0, out=True,
        why='Wykonuje się tylko pierwszy prawdziwy warunek. x > 50 pasuje, więc elif nie jest sprawdzany.'),
   dict(t='fill', l=1, q='Uzupełnij brakujące słowo', code='''wiek = 12
if wiek >= 18:
    print("dorosły")
___:
    print("niepełnoletni")''', ans=[['else']], expect='niepełnoletni', why='else wykonuje się, gdy żaden warunek nie był prawdziwy.'),
   dict(t='bug', l=1, q='Python zgłasza błąd. Kliknij winną linię.', code='''x = 10
if x > 5
    print("Więcej niż 5")''', line=1, fix='if x > 5:', why='Po warunku if zawsze musi być dwukropek.'),
   dict(t='bug', l=1, q='Python zgłasza błąd wcięcia. Kliknij winną linię.', code='''x = 10
if x > 5:
print("Więcej niż 5")''', line=2, fix='    print("Więcej niż 5")', why='Kod wewnątrz if musi być wcięty (4 spacje).'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''a = 4
b = 7
if a > 3:
    if b > 10:
        print("X")
    else:
        print("Y")
else:
    print("Z")''', opts=['Y', 'X', 'Z', 'X\nY'], a=0, out=True, why='a > 3 jest prawdą, więc wchodzimy do środka. b > 10 to fałsz – wykonuje się wewnętrzne else.'),
   dict(t='code', l=1, q='Wczytaj liczbę. Wypisz <code>parzysta</code> lub <code>nieparzysta</code>.',
        start='n = int(input())\n', tests=[dict(i='4', o='parzysta'), dict(i='7', o='nieparzysta'), dict(i='0', o='parzysta')],
        sol='n = int(input())\nif n % 2 == 0:\n    print("parzysta")\nelse:\n    print("nieparzysta")', hint='Sprawdź n % 2 == 0.'),
   dict(t='code', l=3, q='Wczytaj temperaturę wody. Wypisz: <code>lód</code> (≤ 0), <code>zimna</code> (1–15), <code>idealna</code> (16–30), <code>gorąca</code> (> 30).',
        start='t = int(input())\n', tests=[dict(i='-3', o='lód'), dict(i='0', o='lód'), dict(i='10', o='zimna'), dict(i='16', o='idealna'), dict(i='30', o='idealna'), dict(i='31', o='gorąca')],
        sol='t = int(input())\nif t <= 0:\n    print("lód")\nelif t <= 15:\n    print("zimna")\nelif t <= 30:\n    print("idealna")\nelse:\n    print("gorąca")',
        hint='Użyj if, elif, elif, else – od najmniejszej temperatury.'),
   dict(t='code', l=3, q='Wczytaj rok. Wypisz <code>przestępny</code> lub <code>zwykły</code>.<br>Rok jest przestępny, gdy dzieli się przez 4 i nie przez 100, albo dzieli się przez 400.',
        start='rok = int(input())\n', tests=[dict(i='2024', o='przestępny'), dict(i='1900', o='zwykły'), dict(i='2000', o='przestępny'), dict(i='2023', o='zwykły')],
        sol='rok = int(input())\nif rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:\n    print("przestępny")\nelse:\n    print("zwykły")',
        hint='(rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0'),
  ]),
 ]))
