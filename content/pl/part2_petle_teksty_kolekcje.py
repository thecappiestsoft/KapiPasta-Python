# Treść kursu KapiPasta - Python (PL). Format opisany w README.md -> "Edycja treści".
# Po zmianach uruchom: python3 tools/build.py

CH = []

CH.append(dict(
 id='petle', icon=dict(rpg='🌀', space='🌌', neutral='🔁'),
 name=dict(rpg='Wir Powtórzeń', space='Mgławica Pętli', neutral='Pętle'),
 topic='for, range, while, break, continue',
 lessons=[
 dict(id='for', title='for i range()',
  theory="""<p>Pętla <code>for</code> powtarza kod dla każdego elementu po kolei.</p>
<p><code>range(n)</code> daje liczby od <b>0 do n-1</b>: <code>range(4)</code> → 0, 1, 2, 3.</p>
<ul><li><code>range(a, b)</code> – od a do b-1</li><li><code>range(a, b, krok)</code> – co krok, np. <code>range(0, 10, 2)</code> → 0, 2, 4, 6, 8</li></ul>""",
  more="""<p>Krok może być ujemny: <code>range(5, 0, -1)</code> → 5, 4, 3, 2, 1. Pętlą <code>for</code> przejdziesz też po tekście i liście. Gdy zmienna pętli nie jest potrzebna, nazywa się ją <code>_</code>.</p>""",
  ex=[
   dict(code='''for i in range(4):
    print(f"Kapi zjada mandarynkę nr {i}")''',
        scene=dict(s='loop', items=['🍊', '🍊', '🍊', '🍊'], cap='Kapi przechodzi wzdłuż rzędu mandarynek. Licznik i rośnie od 0 do 3. Naciśnij ▶, by zobaczyć krok po kroku.')),
   dict(code='''for x in range(2, 11, 3):
    print(x)''',
        scene=dict(s='loop', items=['2', '5', '8'], cap='Kapi skacze po kamieniach co 3 – od 2, ale 11 już nie wlicza się do zakresu.')),
   dict(code='''suma = 0
for i in range(1, 6):
    suma += i
print("Suma:", suma)''', lvl=2,
        scene=dict(s='loop', items=['1', '2', '3', '4', '5'], acc='suma', accv=[1, 3, 6, 10, 15], cap='Kapi wrzuca kolejne liczby do koszyka „suma”.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Ile razy wypisze się „Hop”?', code='''for i in range(5):
    print("Hop")''', opts=['5', '4', '6', '0'], a=0, why='range(5) to 0, 1, 2, 3, 4 – pięć liczb.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''for i in range(1, 4):
    print(i)''', opts=['1\n2\n3', '1\n2\n3\n4', '0\n1\n2\n3', '1 2 3'], a=0, out=True, why='range(1, 4) zaczyna od 1, kończy przed 4.'),
   dict(t='fill', l=1, q='Uzupełnij, aby wypisać liczby 0, 1, 2', code='''for i in ___(3):
    print(i)''', ans=[['range']], expect='0\n1\n2', why='range(3) daje 0, 1, 2.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''for i in range(10, 0, -3):
    print(i, end=" ")''', opts=['10 7 4 1 ', '10 7 4 ', '10 7 4 1 -2 ', '9 6 3 '], a=0, out=True,
        why='Startujemy od 10 i odejmujemy 3, dopóki jesteśmy powyżej 0.'),
   dict(t='bug', l=2, q='Program miał wypisać liczby od 1 do 5, ale wypisuje 1–4. Kliknij winną linię.', code='''for i in range(1, 5):
    print(i)''', line=0, noerr=True, fix='for i in range(1, 6):', why='Koniec zakresu w range nie jest wliczany – trzeba podać 6.'),
   dict(t='code', l=1, q='Wypisz 3 razy w osobnych liniach: <code>Kapi pływa</code>',
        start='', tests=[dict(i='', o='Kapi pływa\nKapi pływa\nKapi pływa')], check="assert __src.count('print') == 1, 'Użyj pętli i jednego print'",
        sol='for i in range(3):\n    print("Kapi pływa")', hint='for i in range(3):'),
   dict(t='code', l=2, q='Wczytaj n i wypisz tabliczkę mnożenia przez n od 1 do 5 w formacie <code>1 x n = wynik</code>.',
        start='n = int(input())\n', tests=[dict(i='3', o='1 x 3 = 3\n2 x 3 = 6\n3 x 3 = 9\n4 x 3 = 12\n5 x 3 = 15')],
        sol='n = int(input())\nfor i in range(1, 6):\n    print(f"{i} x {n} = {i * n}")', hint='for i in range(1, 6): print(f"{i} x {n} = {i*n}")'),
   dict(t='code', l=3, q='Wczytaj n i wypisz sumę kwadratów liczb od 1 do n (1² + 2² + … + n²).',
        start='n = int(input())\n', tests=[dict(i='3', o='14'), dict(i='10', o='385'), dict(i='1', o='1')],
        sol='n = int(input())\ns = 0\nfor i in range(1, n + 1):\n    s += i ** 2\nprint(s)', hint='Zacznij od s = 0 i dodawaj i ** 2.'),
  ]),
 dict(id='while', title='while, break, continue',
  theory="""<p><code>while</code> powtarza kod, <b>dopóki</b> warunek jest prawdziwy. Używamy jej, gdy nie wiemy z góry, ile będzie powtórzeń.</p>
<p>⚠️ Pamiętaj, by coś w pętli zmieniało warunek – inaczej pętla będzie nieskończona!</p>
<ul><li><code>break</code> – natychmiast przerywa całą pętlę</li><li><code>continue</code> – pomija resztę obrotu i przechodzi do następnego</li></ul>""",
  more="""<p>Typowy wzorzec: <code>while True:</code> z <code>break</code> w środku – np. pytamy, aż użytkownik poda poprawną odpowiedź. Pętla <code>for</code> może mieć <code>else</code>, które wykona się, jeśli nie było <code>break</code>.</p>""",
  ex=[
   dict(code='''energia = 3
while energia > 0:
    print(f"Kapi pływa, energia: {energia}")
    energia -= 1
print("Kapi odpoczywa 😴")''',
        scene=dict(s='loop', items=['⚡3', '⚡2', '⚡1'], cap='Kapi pływa, dopóki ma energię. Gdy energia spada do 0, warunek jest fałszywy i pętla się kończy.')),
   dict(code='''for i in range(1, 8):
    if i == 3:
        continue  # pomiń 3
    if i == 6:
        break     # stop przy 6
    print(i)''',
        scene=dict(s='loop', items=['1', '2', '3⏭', '4', '5', '6🛑'], cap='Kapi przeskakuje kamień nr 3 (continue), a przy 6 zawraca do domu (break).')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 1
while x < 10:
    x = x * 2
print(x)''', opts=['16', '8', '10', '32'], a=0, out=True, why='x: 1 → 2 → 4 → 8 → 16. Przy 16 warunek x < 10 jest fałszywy.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''for i in range(5):
    if i == 2:
        break
    print(i)''', opts=['0\n1', '0\n1\n2', '0\n1\n3\n4', '2'], a=0, out=True, why='break kończy pętlę, zanim 2 zostanie wypisane.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''for i in range(5):
    if i == 2:
        continue
    print(i)''', opts=['0\n1\n3\n4', '0\n1', '0\n1\n2\n3\n4', '2'], a=0, out=True, why='continue pomija tylko obrót dla i = 2.'),
   dict(t='bug', l=2, q='Ten program nigdy się nie kończy (pętla nieskończona). Kliknij linię, którą trzeba poprawić.', code='''n = 5
while n > 0:
    print(n)
    n += 1''', line=3, fix='    n -= 1', noerr=True,
        why='n rośnie zamiast maleć, więc n > 0 jest zawsze prawdą. Trzeba zmniejszać n.'),
   dict(t='fill', l=2, q='Uzupełnij, aby pętla zakończyła się, gdy użytkownik wpisze „stop”', code='''while True:
    s = input()
    if s == "stop":
        ___
    print(s)''', ans=[['break']], inp='a\nb\nstop', expect='a\nb', why='break wychodzi z pętli while True.'),
   dict(t='code', l=1, q='Za pomocą pętli <code>while</code> wypisz odliczanie 5, 4, 3, 2, 1 (każda liczba w nowej linii), a na końcu <code>Start!</code>',
        start='n = 5\n', tests=[dict(i='', o='5\n4\n3\n2\n1\nStart!')], check="assert 'while' in __src, 'Użyj pętli while'",
        sol='n = 5\nwhile n > 0:\n    print(n)\n    n -= 1\nprint("Start!")', hint='while n > 0: … n -= 1'),
   dict(t='code', l=2, q='Wczytuj liczby, aż pojawi się 0. Wypisz ich sumę (bez zera).',
        start='', tests=[dict(i='3\n5\n2\n0', o='10'), dict(i='0', o='0'), dict(i='-4\n4\n7\n0', o='7')],
        sol='s = 0\nwhile True:\n    x = int(input())\n    if x == 0:\n        break\n    s += x\nprint(s)', hint='while True: … if x == 0: break'),
   dict(t='code', l=3, q='Wczytaj n > 0. Ile razy trzeba podzielić n całkowicie przez 2 (n //= 2), żeby dostać 1? Wypisz liczbę kroków.',
        start='n = int(input())\n', tests=[dict(i='8', o='3'), dict(i='1', o='0'), dict(i='100', o='6')],
        sol='n = int(input())\nk = 0\nwhile n > 1:\n    n //= 2\n    k += 1\nprint(k)', hint='while n > 1: n //= 2; k += 1'),
  ]),
 dict(id='zagn', title='Pętle zagnieżdżone',
  theory="""<p>Pętla w pętli: wewnętrzna wykonuje się <b>w całości</b> przy każdym obrocie zewnętrznej. Dla 3 obrotów zewnętrznej i 4 wewnętrznej kod w środku wykona się 3 · 4 = 12 razy.</p>
<p>Przydaje się do tabel, siatek i rysowania wzorów.</p>""",
  more="""<p>Wewnętrzna pętla może zależeć od zmiennej zewnętrznej, np. <code>for j in range(i)</code> – tak powstają trójkąty. <code>break</code> przerywa tylko tę pętlę, w której się znajduje.</p>""",
  ex=[
   dict(code='''for rzad in range(3):
    for kol in range(4):
        print("🍉", end="")
    print()''',
        scene=dict(s='grid', rows=3, cols=4, emo='🍉', cap='Kapi sadzi arbuzy na grządkach: rząd po rzędzie, w każdym 4 arbuzy.')),
   dict(code='''for i in range(1, 5):
    print("*" * i)''', lvl=2,
        scene=dict(s='grid', rows=4, cols=4, tri=True, emo='⭐', cap='Kapi buduje schodki: w rzędzie i układa i gwiazdek.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Ile razy wypisze się „Kapi”?', code='''for a in range(3):
    for b in range(2):
        print("Kapi")''', opts=['6', '5', '3', '2'], a=0, why='3 obroty zewnętrzne × 2 wewnętrzne = 6.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''for i in range(2):
    print("🍉" * 3)''', opts=['🍉🍉🍉\n🍉🍉🍉', '🍉🍉🍉', '🍉🍉\n🍉🍉\n🍉🍉', '🍉🍉🍉🍉🍉🍉'], a=0, out=True, why='Pętla wykonuje się 2 razy, a za każdym razem wypisuje 3 arbuzy.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''for i in range(1, 3):
    for j in range(1, 3):
        print(i * j, end=" ")
    print()''', opts=['1 2 \n2 4', '1 2 2 4', '1 1 \n2 2', '1 2 \n3 4'], a=0, out=True,
        why='Dla i = 1: 1, 2; dla i = 2: 2, 4. print() kończy linię.'),
   dict(t='fill', l=2, q='Uzupełnij, aby powstał trójkąt z gwiazdek o 3 wierszach (1, 2, 3 gwiazdki)', code='''for i in range(1, 4):
    for j in range(___):
        print("*", end="")
    print()''', ans=[['i']], expect='*\n**\n***', why='W wierszu i ma być i gwiazdek, więc wewnętrzna pętla to range(i).'),
   dict(t='code', l=1, q='Wypisz prostokąt z <code>#</code>: 2 wiersze po 5 znaków. Użyj dwóch pętli.',
        start='', tests=[dict(i='', o='#####\n#####')], check="assert __src.count('for') >= 2, 'Użyj dwóch pętli for'",
        sol='for i in range(2):\n    for j in range(5):\n        print("#", end="")\n    print()', hint='Wewnątrz print("#", end=""), po pętli wewnętrznej print().'),
   dict(t='code', l=2, q='Wczytaj n i wypisz tabliczkę mnożenia n × n. Liczby w wierszu oddziel spacją.<br>Dla 3:<br><code>1 2 3<br>2 4 6<br>3 6 9</code>',
        start='n = int(input())\n', tests=[dict(i='3', o='1 2 3\n2 4 6\n3 6 9'), dict(i='1', o='1')],
        sol='n = int(input())\nfor i in range(1, n + 1):\n    w = []\n    for j in range(1, n + 1):\n        w.append(str(i * j))\n    print(" ".join(w))',
        hint='Zbieraj wiersz w liście albo używaj end=" " i uważaj na spację na końcu (końcowe spacje są ignorowane).'),
   dict(t='code', l=3, q='Wczytaj n i wypisz choinkę o n poziomach wyśrodkowaną spacjami. Dla 3:<br><code>&nbsp;&nbsp;*<br>&nbsp;***<br>*****</code>',
        start='n = int(input())\n', tests=[dict(i='3', o='  *\n ***\n*****'), dict(i='1', o='*')],
        sol='n = int(input())\nfor i in range(n):\n    print(" " * (n - 1 - i) + "*" * (2 * i + 1))', hint='W wierszu i: n-1-i spacji i 2i+1 gwiazdek.'),
  ]),
 ]))

CH.append(dict(
 id='teksty', icon=dict(rpg='📜', space='📡', neutral='🔤'),
 name=dict(rpg='Biblioteka Zwojów', space='Radar Sygnałów', neutral='Teksty'),
 topic='indeksy, wycinki, metody tekstów',
 lessons=[
 dict(id='slice', title='Indeksy, wycinki, len()',
  theory="""<p>Tekst to ciąg znaków. Każdy znak ma <b>indeks</b> – numer liczony od <b>0</b>. <code>s[0]</code> to pierwszy znak, <code>s[-1]</code> – ostatni.</p>
<p><b>Wycinek</b> <code>s[a:b]</code> to znaki od indeksu a do b-1. <code>len(s)</code> zwraca długość.</p>""",
  more="""<p>Pominięty początek to 0, pominięty koniec – do końca: <code>s[:3]</code>, <code>s[3:]</code>. Trzeci parametr to krok: <code>s[::2]</code> co drugi znak, <code>s[::-1]</code> – tekst od tyłu. Tekstów nie można zmieniać: <code>s[0] = "X"</code> zgłosi <code>TypeError</code>.</p>""",
  ex=[
   dict(code='''s = "KAPIBARA"
print(s[0], s[3], s[-1])
print(s[1:4])
print(len(s))''',
        scene=dict(s='row', items=list('KAPIBARA'), hl=[1, 4], label='s[1:4]', cap='Kapi wskazuje literki 1, 2 i 3 – wycinek kończy się PRZED indeksem 4.')),
   dict(code='''s = "KAPIBARA"
print(s[:4])
print(s[4:])
print(s[::-1])''', lvl=2,
        scene=dict(s='row', items=list('KAPIBARA'), hl=[0, 4], label='s[:4]', cap='s[:4] to początek aż do indeksu 4, a s[::-1] to Kapi czytający od tyłu.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''s = "python"
print(s[0])''', opts=['p', 'y', 'n', 'python'], a=0, out=True, why='Indeksy zaczynają się od 0, więc s[0] to pierwsza litera.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''s = "python"
print(s[-1], len(s))''', opts=['n 6', 'n 5', 'p 6', 'o 6'], a=0, out=True, why='-1 to ostatni znak, a słowo ma 6 liter.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''s = "mandarynka"
print(s[0:5])''', opts=['manda', 'mandar', 'andar', 'mand'], a=0, out=True, why='Znaki o indeksach 0–4, czyli 5 pierwszych.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''s = "Kapi"
print(s[0])
print(s[4])''', line=2, fix='print(s[3])', why='Słowo ma 4 znaki o indeksach 0–3. s[4] wychodzi poza tekst: IndexError.'),
   dict(t='fill', l=2, q='Uzupełnij, aby wypisać tekst od tyłu', code='''s = "kajak2"
print(s[___])''', ans=[['::-1']], expect='2kajak', why='Krok -1 czyta tekst od końca.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''s = "abcdefgh"
print(s[1::3])''', opts=['beh', 'adg', 'bdf', 'bcd'], a=0, out=True, why='Start od indeksu 1 (b), potem co 3: e, h.'),
   dict(t='code', l=1, q='Wczytaj słowo i wypisz jego pierwszą i ostatnią literę oddzielone spacją.',
        start='s = input()\n', tests=[dict(i='kapibara', o='k a'), dict(i='python', o='p n')], sol='s = input()\nprint(s[0], s[-1])', hint='s[0] i s[-1]'),
   dict(t='code', l=2, q='Wczytaj słowo i wypisz jego środkowy znak (słowo ma nieparzystą długość).',
        start='s = input()\n', tests=[dict(i='kajak', o='j'), dict(i='abc', o='b'), dict(i='x', o='x')], sol='s = input()\nprint(s[len(s) // 2])',
        hint='Indeks środka to len(s) // 2.'),
  ]),
 dict(id='metody', title='Metody tekstów',
  theory="""<p>Metody wywołujemy po kropce: <code>tekst.metoda()</code>. Zwracają <b>nowy</b> tekst.</p>
<ul><li><code>upper()</code> / <code>lower()</code> – WIELKIE / małe litery</li><li><code>strip()</code> – usuwa spacje z początku i końca</li><li><code>replace(a, b)</code> – zamienia a na b</li><li><code>split()</code> – dzieli tekst na listę słów</li><li><code>" ".join(lista)</code> – skleja listę w tekst</li></ul>""",
  more="""<p><code>split(",")</code> dzieli po przecinku. <code>"-".join(...)</code> skleja myślnikiem. Przydatne też: <code>count()</code>, <code>find()</code>, <code>startswith()</code>, <code>isdigit()</code>. Metody można łączyć: <code>s.strip().lower()</code>.</p>""",
  ex=[
   dict(code='''s = "  Kapi lubi Wodę  "
print(s.strip())
print(s.upper())
print(s.replace("Wodę", "arbuzy"))''',
        scene=dict(s='cards', items=[['strip()', '"Kapi lubi Wodę"', 'bez spacji z brzegów'], ['upper()', '"  KAPI LUBI WODĘ  "', 'WIELKIE'], ['replace()', '"  Kapi lubi arbuzy  "', 'podmiana']], cap='Kapi pracuje w drukarni: myje, powiększa i podmienia literki.')),
   dict(code='''zdanie = "kapi lubi kąpiele"
slowa = zdanie.split()
print(slowa)
print("-".join(slowa))''',
        scene=dict(s='row', items=['"kapi"', '"lubi"', '"kąpiele"'], label='split()', cap='Kapi tnie zdanie nożyczkami na słowa, a join skleja je z powrotem taśmą „-”.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='print("Kapi".upper())', opts=['KAPI', 'kapi', 'Kapi', 'KAPi'], a=0, out=True, why='upper() zamienia wszystkie litery na wielkie.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='print("a b c".split())', opts=["['a', 'b', 'c']", 'abc', "['a b c']", 'a, b, c'], a=0, out=True,
        why='split() dzieli po spacjach i zwraca listę.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='print("kot".replace("k", "r"))', opts=['rot', 'kot', 'kor', 'rrot'], a=0, out=True, why='Każde „k” zostaje zamienione na „r”.'),
   dict(t='fill', l=1, q='Uzupełnij, aby usunąć spacje z brzegów', code='''s = "   hej   "
print(s.___())''', ans=[['strip']], expect='hej', why='strip() usuwa białe znaki z obu końców.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='print("+".join(["1", "2", "3"]))', opts=['1+2+3', '6', '+1+2+3', '123'], a=0, out=True,
        why='join wstawia separator między elementy.'),
   dict(t='bug', l=2, q='Program miał wypisać KAPI, ale wypisuje Kapi. Kliknij winną linię.', code='''s = "Kapi"
s.upper()
print(s)''', line=1, fix='s = s.upper()', noerr=True, why='Teksty są niezmienne – upper() zwraca nowy tekst, który trzeba zapisać do zmiennej.'),
   dict(t='code', l=1, q='Wczytaj imię (może mieć spacje na brzegach i dowolną wielkość liter). Wypisz je WIELKIMI literami bez spacji z brzegów.',
        start='s = input()\n', tests=[dict(i='  kapi  ', o='KAPI'), dict(i='Ola', o='OLA')], sol='s = input()\nprint(s.strip().upper())', hint='s.strip().upper()'),
   dict(t='code', l=2, q='Wczytaj zdanie i wypisz liczbę słów.',
        start='s = input()\n', tests=[dict(i='kapi lubi kąpiele', o='3'), dict(i='hej', o='1'), dict(i='  dużo   spacji  tu ', o='3')],
        sol='s = input()\nprint(len(s.split()))', hint='len(s.split())'),
   dict(t='code', l=3, q='Wczytaj imię i nazwisko (np. <code>jan kowalski</code>) i wypisz inicjały wielkimi literami z kropkami: <code>J.K.</code>',
        start='s = input()\n', tests=[dict(i='jan kowalski', o='J.K.'), dict(i='Ola Nowak', o='O.N.')],
        sol='s = input()\nim, naz = s.split()\nprint(f"{im[0].upper()}.{naz[0].upper()}.")', hint='Użyj split(), a potem [0] i upper().'),
  ]),
 dict(id='znaki', title='Iterowanie po znakach',
  theory="""<p>Pętla <code>for</code> może chodzić po tekście znak po znaku:</p>
<pre>for znak in "Kapi":
    print(znak)</pre>
<p>Dzięki temu policzymy np. samogłoski albo zbudujemy nowy tekst, dodając znaki jeden po drugim.</p>""",
  more="""<p>Gdy potrzebny jest też indeks, użyj <code>for i in range(len(s))</code> albo <code>for i, z in enumerate(s)</code>. Operator <code>in</code> sprawdza, czy znak jest w tekście: <code>"a" in "kapi"</code> → <code>True</code>.</p>""",
  ex=[
   dict(code='''for z in "KAPI":
    print(z * 2)''',
        scene=dict(s='loop', items=['K', 'A', 'P', 'I'], cap='Kapi podskakuje po literkach i każdą wypowiada dwa razy.')),
   dict(code='''s = "kapibara"
ile = 0
for z in s:
    if z in "aeiouy":
        ile += 1
print("Samogłoski:", ile)''',
        scene=dict(s='loop', items=list('kapibara'), acc='ile', accv=[0, 1, 1, 2, 2, 3, 3, 4], cap='Kapi zbiera do koszyka tylko samogłoski.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Ile linii wypisze program?', code='''for z in "kot":
    print(z)''', opts=['3', '1', '2', '4'], a=0, why='Pętla wykonuje się raz dla każdej z 3 liter.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''w = ""
for z in "abc":
    w = z + w
print(w)''', opts=['cba', 'abc', 'a', 'bca'], a=0, out=True, why='Każdą literę dokładamy na początek, więc tekst się odwraca.'),
   dict(t='fill', l=1, q='Uzupełnij, aby pętla przeszła po każdym znaku tekstu s', code='''s = "kapi"
for z ___ s:
    print(z.upper(), end="")''', ans=[['in']], expect='KAPI', why='Składnia pętli: for zmienna in kolekcja.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''n = 0
for z in "Ala ma kota":
    if z == "a":
        n += 1
print(n)''', opts=['3', '4', '2', '5'], a=0, out=True, why='Python rozróżnia wielkość liter – wielkie A nie jest liczone. Małe „a” są 3.'),
   dict(t='code', l=1, q='Wczytaj słowo i wypisz każdą jego literę w osobnej linii.',
        start='s = input()\n', tests=[dict(i='kapi', o='k\na\np\ni')], sol='s = input()\nfor z in s:\n    print(z)', hint='for z in s: print(z)'),
   dict(t='code', l=2, q='Wczytaj tekst i wypisz, ile jest w nim cyfr (użyj pętli i <code>isdigit()</code> lub <code>in "0123456789"</code>).',
        start='s = input()\n', tests=[dict(i='Kapi ma 2 lata i 15 kuzynów', o='3'), dict(i='brak', o='0')],
        sol='s = input()\nn = 0\nfor z in s:\n    if z.isdigit():\n        n += 1\nprint(n)', hint='if z.isdigit(): n += 1'),
   dict(t='code', l=3, q='Szyfr Cezara: wczytaj słowo z małych liter a–z i przesuń każdą literę o 3 dalej w alfabecie (x→a, y→b, z→c).',
        start='s = input()\n', tests=[dict(i='kapi', o='ndsl'), dict(i='xyz', o='abc')],
        sol='s = input()\nw = ""\nfor z in s:\n    w += chr((ord(z) - ord("a") + 3) % 26 + ord("a"))\nprint(w)',
        hint='ord("a") to kod litery a, chr(kod) zamienia kod na znak. Użyj % 26.'),
  ]),
 ]))

CH.append(dict(
 id='kolekcje', icon=dict(rpg='💰', space='📦', neutral='🗂️'),
 name=dict(rpg='Skarbiec Kolekcji', space='Ładownia Kolekcji', neutral='Kolekcje'),
 topic='listy, krotki, zbiory, słowniki',
 lessons=[
 dict(id='listy', title='Listy',
  theory="""<p><b>Lista</b> to uporządkowany zbiór wartości w nawiasach kwadratowych: <code>owoce = ["jabłko", "arbuz", "melon"]</code>.</p>
<p>Indeksy i wycinki działają jak w tekstach: <code>owoce[0]</code>, <code>owoce[-1]</code>, <code>owoce[1:3]</code>. Długość: <code>len(owoce)</code>.</p>
<p>W przeciwieństwie do tekstu listę <b>można zmieniać</b>: <code>owoce[0] = "gruszka"</code>.</p>""",
  more="""<p>Lista może mieć elementy różnych typów, a nawet inne listy: <code>[[1, 2], [3, 4]]</code> – wtedy <code>t[1][0]</code> to 3. Uwaga: <code>b = a</code> nie kopiuje listy – obie nazwy wskazują tę samą listę. Kopia to <code>a[:]</code> lub <code>a.copy()</code>.</p>""",
  ex=[
   dict(code='''plecak = ["🍉", "🍊", "🥕", "🍎"]
print(plecak[0], plecak[-1])
print(plecak[1:3])
plecak[2] = "🍐"
print(plecak)''',
        scene=dict(s='row', items=['🍉', '🍊', '🥕', '🍎'], hl=[1, 3], label='plecak[1:3]', cap='Kapi pakuje plecak z przegródkami numerowanymi od 0. Marchewkę wymienia na gruszkę.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [10, 20, 30, 40]
print(t[2])''', opts=['30', '20', '40', '[30]'], a=0, out=True, why='Indeks 2 to trzeci element (liczymy od 0).'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [5, 6, 7]
t[0] = 9
print(t)''', opts=['[9, 6, 7]', '[5, 6, 7]', '[9, 5, 6, 7]', 'Błąd'], a=0, out=True, why='Listy można zmieniać – element 0 został zastąpiony.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = ["a", "b", "c", "d", "e"]
print(t[1:4], len(t))''', opts=["['b', 'c', 'd'] 5", "['b', 'c', 'd', 'e'] 5", "['a', 'b', 'c'] 4", "['b', 'c'] 5"], a=0, out=True, why='Wycinek od 1 do 3; lista ma 5 elementów.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''t = [1, 2, 3]
print(t[len(t)])''', line=1, fix='print(t[len(t) - 1])', why='Ostatni indeks to len(t) - 1. t[3] nie istnieje: IndexError.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''a = [1, 2]
b = a
b[0] = 99
print(a)''', opts=['[99, 2]', '[1, 2]', '[99]', 'Błąd'], a=0, out=True, why='b = a nie tworzy kopii – obie nazwy to ta sama lista.'),
   dict(t='code', l=1, q='Utwórz listę <code>owoce</code> z trzema tekstami: <code>jabłko</code>, <code>arbuz</code>, <code>melon</code>. Wypisz drugi element.',
        start='', tests=[dict(i='', o='arbuz')], check="assert owoce == ['jabłko', 'arbuz', 'melon'], 'Lista ma złą zawartość'",
        sol='owoce = ["jabłko", "arbuz", "melon"]\nprint(owoce[1])', hint='Drugi element ma indeks 1.'),
   dict(t='code', l=2, q='Wczytaj liczby w jednej linii oddzielone spacjami. Wypisz pierwszą i ostatnią.',
        start='t = input().split()\n', tests=[dict(i='4 8 15 16 23 42', o='4 42'), dict(i='7', o='7 7')], sol='t = input().split()\nprint(t[0], t[-1])', hint='t[0] i t[-1]'),
  ]),
 dict(id='metodylist', title='Metody list',
  theory="""<ul><li><code>append(x)</code> – dodaje x na koniec</li><li><code>insert(i, x)</code> – wstawia x na pozycję i</li><li><code>remove(x)</code> – usuwa pierwsze x</li><li><code>pop()</code> – wyjmuje i zwraca ostatni element (<code>pop(i)</code> – element i)</li><li><code>sort()</code> – sortuje listę rosnąco</li><li><code>x in lista</code> – czy x jest w liście?</li></ul>""",
  more="""<p><code>sort(reverse=True)</code> sortuje malejąco. <code>sorted(lista)</code> zwraca nową, posortowaną listę, nie zmieniając starej. <code>sort()</code> zwraca <code>None</code> – nie pisz <code>t = t.sort()</code>! Przydatne: <code>count(x)</code>, <code>index(x)</code>, <code>reverse()</code>.</p>""",
  ex=[
   dict(code='''kolejka = ["Kapi", "Bobo"]
kolejka.append("Lulu")
kolejka.insert(0, "Mimi")
kolejka.remove("Bobo")
print(kolejka)
ostatni = kolejka.pop()
print(ostatni, kolejka)
print("Kapi" in kolejka)''',
        scene=dict(s='row', items=['Mimi', 'Kapi', 'Lulu'], label='kolejka do basenu', cap='Kapibary stoją w kolejce do basenu: append dopisuje na końcu, insert wpycha na przód, pop wyjmuje ostatnią.')),
   dict(code='''wagi = [55, 48, 61, 50]
wagi.sort()
print(wagi)
wagi.sort(reverse=True)
print(wagi)''',
        scene=dict(s='row', items=['48', '50', '55', '61'], label='po sort()', cap='Kapibary ustawiają się od najlżejszej do najcięższej.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [1, 2]
t.append(3)
print(t)''', opts=['[1, 2, 3]', '[3, 1, 2]', '[1, 2]', '[1, 2, [3]]'], a=0, out=True, why='append dodaje na koniec.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [3, 1, 2]
t.sort()
print(t)''', opts=['[1, 2, 3]', '[3, 2, 1]', '[3, 1, 2]', 'None'], a=0, out=True, why='sort() układa rosnąco.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = ["a", "b", "c"]
x = t.pop()
print(x, t)''', opts=["c ['a', 'b']", "a ['b', 'c']", "c ['a', 'b', 'c']", "['a', 'b']"], a=0, out=True, why='pop() wyjmuje i zwraca ostatni element.'),
   dict(t='fill', l=1, q='Uzupełnij, by dodać „melon” na koniec listy', code='''t = ["arbuz"]
t.___("melon")
print(t)''', ans=[['append']], expect="['arbuz', 'melon']", why='append dodaje element na koniec.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''t = [5, 3, 5, 1]
t.remove(5)
t.insert(1, 0)
print(t)''', opts=['[3, 0, 5, 1]', '[3, 1, 0]', '[0, 3, 5, 1]', '[3, 5, 0, 1]'], a=0, out=True,
        why='remove usuwa tylko pierwsze 5 → [3, 5, 1]; insert(1, 0) wstawia 0 na pozycję 1.'),
   dict(t='bug', l=2, q='Program zgłasza błąd przy wypisywaniu. Która linia go powoduje?', code='''t = [4, 2, 9]
t = t.sort()
print(t[0])''', line=1, cause=True, fix='t.sort()', why='sort() zmienia listę i zwraca None. Po t = t.sort() zmienna t to None, więc t[0] zgłasza TypeError w linii 3 – ale przyczyna jest w linii 2.'),
   dict(t='code', l=1, q='Zacznij od pustej listy. Wczytaj 3 imiona (każde w nowej linii), dodaj je do listy przez <code>append</code> i wypisz listę.',
        start='imiona = []\n', tests=[dict(i='Kapi\nBobo\nLulu', o="['Kapi', 'Bobo', 'Lulu']")],
        sol='imiona = []\nfor i in range(3):\n    imiona.append(input())\nprint(imiona)', hint='for i in range(3): imiona.append(input())'),
   dict(t='code', l=2, q='Wczytaj liczby w jednej linii. Wypisz je posortowane malejąco, oddzielone spacjami.',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='3 10 -1 7', o='10 7 3 -1'), dict(i='5', o='5')],
        sol='t = [int(x) for x in input().split()]\nt.sort(reverse=True)\nprint(*t)', hint='t.sort(reverse=True), a potem print(*t) wypisze elementy po spacji.'),
   dict(t='code', l=3, q='Wczytaj słowa w jednej linii. Wypisz je bez powtórzeń, w kolejności pierwszego wystąpienia, oddzielone spacją.',
        start='slowa = input().split()\n', tests=[dict(i='kapi lubi kapi i lubi wodę', o='kapi lubi i wodę'), dict(i='a a a', o='a')],
        sol='slowa = input().split()\nw = []\nfor s in slowa:\n    if s not in w:\n        w.append(s)\nprint(" ".join(w))', hint='Dodawaj słowo do nowej listy tylko, jeśli go tam nie ma (not in).'),
  ]),
 dict(id='krotki', title='Krotki i zbiory',
  theory="""<p><b>Krotka</b> (tuple) to lista, której nie można zmienić: <code>punkt = (3, 5)</code>. Dobra na stałe dane, np. współrzędne.</p>
<p><b>Zbiór</b> (set) przechowuje elementy <b>bez powtórzeń</b> i bez kolejności: <code>{1, 2, 3}</code>. <code>set(lista)</code> usuwa duplikaty.</p>""",
  more="""<p>Rozpakowanie krotki: <code>x, y = punkt</code>. Działania na zbiorach: <code>a | b</code> suma, <code>a &amp; b</code> część wspólna, <code>a - b</code> różnica. Pusty zbiór to <code>set()</code> – bo <code>{}</code> to pusty słownik!</p>""",
  ex=[
   dict(code='''norka = (12, 7)
x, y = norka
print(f"Norka Kapi: x={x}, y={y}")
goscie = ["Bobo", "Lulu", "Bobo", "Mimi", "Lulu"]
print(len(set(goscie)))''',
        scene=dict(s='cards', items=[['(12, 7)', 'krotka', 'nie zmienisz jej'], ['set(goscie)', "{'Bobo', 'Lulu', 'Mimi'}", 'każdy gość raz']], cap='Współrzędne norki są stałe jak skała. A na liście gości każda kapibara liczy się tylko raz.')),
   dict(code='''kapi = {"arbuz", "melon", "trawa"}
bobo = {"trawa", "jabłko", "melon"}
print(sorted(kapi & bobo))
print(sorted(kapi | bobo))''', lvl=2,
        scene=dict(s='venn', a=['arbuz'], both=['melon', 'trawa'], b=['jabłko'], la='Kapi', lb='Bobo', cap='Co lubią obie kapibary? Część wspólna to melon i trawa.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='print(len(set([1, 2, 2, 3, 3, 3])))', opts=['3', '6', '1', '2'], a=0, out=True, why='Zbiór usuwa powtórzenia: {1, 2, 3}.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''p = (3, 8)
print(p[1])''', opts=['8', '3', '(3, 8)', 'Błąd'], a=0, out=True, why='Krotki mają indeksy jak listy: p[1] to drugi element.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''punkt = (2, 3)
punkt[0] = 5
print(punkt)''', line=1, fix='punkt = (5, 3)', why='Krotek nie można zmieniać: TypeError.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''a = {1, 2, 3}
b = {2, 3, 4}
print(sorted(a & b), sorted(a - b))''', opts=['[2, 3] [1]', '[1, 2, 3, 4] [1]', '[2, 3] [4]', '[1] [2, 3]'], a=0, out=True,
        why='& to część wspólna, a - b to elementy z a, których nie ma w b.'),
   dict(t='fill', l=2, q='Uzupełnij, aby rozpakować krotkę', code='''p = (4, 9)
___, y = p
print(x + y)''', ans=[['x']], expect='13', why='Rozpakowanie: x, y = p.'),
   dict(t='code', l=2, q='Wczytaj słowa w jednej linii i wypisz, ile jest różnych słów.',
        start='', tests=[dict(i='kapi lubi kapi i lubi wodę', o='4'), dict(i='a', o='1')], sol='print(len(set(input().split())))', hint='len(set(...))'),
  ]),
 dict(id='slowniki', title='Słowniki',
  theory="""<p><b>Słownik</b> (dict) przechowuje pary <b>klucz: wartość</b> – jak szafka z podpisanymi szufladami:</p>
<pre>kapi = {"imie": "Kapi", "wiek": 4}</pre>
<p>Odczyt: <code>kapi["imie"]</code>. Zmiana lub dodanie: <code>kapi["waga"] = 55</code>.</p>
<p>Bezpieczny odczyt: <code>kapi.get("kolor", "brak")</code> – nie zgłasza błędu, gdy klucza nie ma.</p>""",
  more="""<p>Iterowanie: <code>for k in d.keys()</code> – klucze, <code>d.values()</code> – wartości, <code>for k, v in d.items()</code> – pary. Klasyczny wzorzec zliczania: <code>licznik[x] = licznik.get(x, 0) + 1</code>. Usuwanie: <code>del d[k]</code> lub <code>d.pop(k)</code>.</p>""",
  ex=[
   dict(code='''spizarnia = {"arbuz": 2, "melon": 5, "trawa": 30}
print(spizarnia["melon"])
spizarnia["jabłko"] = 4
print(spizarnia.get("banan", 0))
for owoc, ile in spizarnia.items():
    print(f"{owoc}: {ile}")''',
        scene=dict(s='dict', pairs=[['arbuz', '2'], ['melon', '5'], ['trawa', '30'], ['jabłko', '4']], hl='melon', cap='Kapi prowadzi spiżarnię: na każdej szufladzie jest etykieta (klucz), a w środku liczba zapasów (wartość).')),
   dict(code='''tekst = "kapi lubi kapi"
licznik = {}
for s in tekst.split():
    licznik[s] = licznik.get(s, 0) + 1
print(licznik)''', lvl=2,
        scene=dict(s='dict', pairs=[['kapi', '2'], ['lubi', '1']], hl='kapi', cap='Kapi liczy słowa: przy każdym spotkaniu wrzuca żeton do odpowiedniej szuflady.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''d = {"a": 1, "b": 2}
print(d["b"])''', opts=['2', '1', 'b', 'Błąd'], a=0, out=True, why='Klucz "b" ma wartość 2.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''d = {"kot": 4}
print(d.get("pies", 0))''', opts=['0', '4', 'None', 'Błąd'], a=0, out=True, why='get zwraca wartość domyślną 0, gdy klucza nie ma.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''wiek = {"Kapi": 4, "Bobo": 2}
print(wiek["Kapi"])
print(wiek["Lulu"])''', line=2, fix='print(wiek.get("Lulu", "brak"))', why='Klucza "Lulu" nie ma w słowniku – KeyError. Pomoże get().'),
   dict(t='fill', l=2, q='Uzupełnij, aby pętla dostawała klucz i wartość', code='''d = {"x": 1, "y": 2}
for k, v in d.___():
    print(k, v)''', ans=[['items']], expect='x 1\ny 2', why='items() zwraca pary (klucz, wartość).'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''d = {"a": 3, "b": 5}
d["a"] = d["a"] + d["b"]
print(sum(d.values()))''', opts=['13', '8', '10', '16'], a=0, out=True, why='d["a"] staje się 8, więc suma wartości to 8 + 5 = 13.'),
   dict(t='code', l=1, q='Mając słownik cen, wczytaj nazwę owocu i wypisz jego cenę albo <code>brak</code>, gdy go nie ma.',
        start='ceny = {"arbuz": 12, "melon": 8, "jabłko": 3}\nowoc = input()\n', tests=[dict(i='melon', o='8'), dict(i='banan', o='brak')],
        sol='ceny = {"arbuz": 12, "melon": 8, "jabłko": 3}\nowoc = input()\nprint(ceny.get(owoc, "brak"))', hint='ceny.get(owoc, "brak")'),
   dict(t='code', l=2, q='Wczytaj słowo i wypisz, ile razy występuje każda litera, w kolejności pierwszego pojawienia się, w formacie <code>litera:ile</code> (każda w nowej linii).',
        start='s = input()\n', tests=[dict(i='kapibara', o='k:1\na:3\np:1\ni:1\nb:1\nr:1')],
        sol='s = input()\nd = {}\nfor z in s:\n    d[z] = d.get(z, 0) + 1\nfor k, v in d.items():\n    print(f"{k}:{v}")', hint='d[z] = d.get(z, 0) + 1'),
   dict(t='code', l=3, q='Wczytaj n, potem n linii <code>imię punkty</code>. Wypisz imię osoby z największą liczbą punktów (jedno imię może pojawić się kilka razy – sumuj punkty).',
        start='n = int(input())\n', tests=[dict(i='4\nKapi 5\nBobo 7\nKapi 4\nLulu 8', o='Kapi'), dict(i='1\nOla 1', o='Ola')],
        sol='n = int(input())\nd = {}\nfor i in range(n):\n    im, p = input().split()\n    d[im] = d.get(im, 0) + int(p)\nbest = None\nfor k, v in d.items():\n    if best is None or v > d[best]:\n        best = k\nprint(best)',
        hint='Sumuj w słowniku, potem znajdź klucz z największą wartością.'),
  ]),
 ]))
