# Treść kursu KapiPasta - Python (PL). Format opisany w README.md -> "Edycja treści".
# Po zmianach uruchom: python3 tools/build.py

CH = []

CH.append(dict(
 id='funkcje', icon=dict(rpg='⚙️', space='🤖', neutral='🧩'),
 name=dict(rpg='Kuźnia Funkcji', space='Fabryka Robotów', neutral='Funkcje'),
 topic='def, parametry, return, zasięg',
 lessons=[
 dict(id='def', title='Definicja, parametry, return',
  theory="""<p><b>Funkcja</b> to nazwany kawałek kodu, który można wywoływać wiele razy. Tworzymy ją słowem <code>def</code>:</p>
<pre>def przywitaj(imie):
    print(f"Hej, {imie}!")</pre>
<p><code>imie</code> to <b>parametr</b> – dane wejściowe. <code>return</code> oddaje wynik na zewnątrz i kończy funkcję.</p>""",
  more="""<p>Funkcja bez <code>return</code> zwraca <code>None</code>. Różnica: <code>print</code> tylko pokazuje wynik na ekranie, a <code>return</code> pozwala go dalej użyć, np. <code>x = pole(2, 3) + 1</code>. Funkcja może zwrócić kilka wartości jako krotkę: <code>return a, b</code>.</p>""",
  ex=[
   dict(code='''def pole(a, b):
    return a * b

wynik = pole(3, 4)
print("Pole basenu:", wynik)
print(pole(2, 5) + 1)''',
        scene=dict(s='machine', name='pole(a, b)', inp=['3', '4'], out='12', cap='Funkcja to maszyna Kapi: wrzucasz parametry 3 i 4, kręcisz korbką, a return wyrzuca wynik 12.')),
   dict(code='''def przywitaj(imie):
    print(f"Hej, {imie}!")

przywitaj("Bobo")
przywitaj("Lulu")
x = przywitaj("Mimi")
print(x)''', lvl=2,
        scene=dict(s='machine', name='przywitaj(imie)', inp=['"Bobo"'], out='None', cap='Ta maszyna tylko krzyczy na powitanie (print). Niczego nie wyrzuca, więc zwraca None.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''def podwoj(x):
    return x * 2

print(podwoj(5))''', opts=['10', '5', '25', 'None'], a=0, out=True, why='Funkcja zwraca 5 * 2.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''def f(a, b):
    return a - b

print(f(2, 7))''', opts=['-5', '5', '9', '27'], a=0, out=True, why='Argumenty trafiają do parametrów w kolejności: a = 2, b = 7.'),
   dict(t='fill', l=1, q='Uzupełnij słowo kluczowe tworzące funkcję', code='''___ hej():
    print("Hej!")
hej()''', ans=[['def']], expect='Hej!', why='Funkcję tworzymy słowem def.'),
   dict(t='fill', l=1, q='Uzupełnij, aby funkcja oddawała wynik', code='''def suma(a, b):
    ___ a + b
print(suma(2, 3))''', ans=[['return']], expect='5', why='return przekazuje wynik na zewnątrz funkcji.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''def kwadrat(x):
    return x * x

print(kwadrat())''', line=3, fix='print(kwadrat(4))', why='Funkcja wymaga parametru x, a wywołano ją bez argumentu: TypeError.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''def f(x):
    print(x + 1)

y = f(3)
print(y)''', opts=['4\nNone', '4\n4', 'None', '4'], a=0, out=True, why='f wypisuje 4, ale nie ma return – zwraca None.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''def f(n):
    if n > 0:
        return "plus"
    return "nie plus"
    print("koniec")

print(f(3))''', opts=['plus', 'plus\nkoniec', 'nie plus', 'koniec'], a=0, out=True, why='return natychmiast kończy funkcję.'),
   dict(t='code', l=1, q='Napisz funkcję <code>obwod(a, b)</code>, która zwraca obwód prostokąta o bokach a i b.',
        start='def obwod(a, b):\n    \n', tests=[], check="assert obwod(2, 3) == 10, 'obwod(2, 3) powinno dać 10'\nassert obwod(5, 5) == 20, 'obwod(5, 5) powinno dać 20'",
        sol='def obwod(a, b):\n    return 2 * a + 2 * b', hint='return 2 * a + 2 * b'),
   dict(t='code', l=2, q='Napisz funkcję <code>czy_parzysta(n)</code>, która zwraca <code>True</code> dla liczb parzystych i <code>False</code> dla nieparzystych.',
        start='def czy_parzysta(n):\n    \n', tests=[], check="assert czy_parzysta(4) is True, 'czy_parzysta(4) ma zwrócić True'\nassert czy_parzysta(7) is False, 'czy_parzysta(7) ma zwrócić False'\nassert czy_parzysta(0) is True",
        sol='def czy_parzysta(n):\n    return n % 2 == 0', hint='return n % 2 == 0'),
   dict(t='code', l=3, q='Napisz funkcję <code>min_max(t)</code>, która zwraca krotkę (najmniejszy, największy) element listy – bez min() i max().',
        start='def min_max(t):\n    \n', tests=[], check="assert min_max([3, 9, -2, 5]) == (-2, 9), 'Dla [3, 9, -2, 5] wynik to (-2, 9)'\nassert min_max([7]) == (7, 7)\nimport re\nassert not re.search(r'(?<!_)\\b(min|max)\\(', __src), 'Bez min() i max()'",
        sol='def min_max(t):\n    a = b = t[0]\n    for x in t:\n        if x < a:\n            a = x\n        if x > b:\n            b = x\n    return a, b', hint='Zacznij od a = b = t[0] i porównuj w pętli.'),
  ]),
 dict(id='domyslne', title='Parametry domyślne',
  theory="""<p>Parametr może mieć <b>wartość domyślną</b> – używaną, gdy nie podamy argumentu:</p>
<pre>def przywitaj(imie, znak="!"):
    print("Hej, " + imie + znak)</pre>
<p><code>przywitaj("Kapi")</code> → Hej, Kapi! &nbsp; <code>przywitaj("Kapi", "?")</code> → Hej, Kapi?</p>""",
  more="""<p>Parametry z wartością domyślną muszą być <b>na końcu</b>. Argumenty można podawać po nazwie: <code>f(b=2, a=1)</code>. Znasz to już: <code>print(..., sep="-", end="")</code> to właśnie parametry domyślne!</p>""",
  ex=[
   dict(code='''def zamow(owoc, ile=1):
    print(f"Kapi zamawia {ile} x {owoc}")

zamow("arbuz")
zamow("melon", 3)
zamow(ile=2, owoc="jabłko")''',
        scene=dict(s='machine', name='zamow(owoc, ile=1)', inp=['"arbuz"', '(1)'], out='1 x arbuz', cap='Gdy Kapi nie powie, ile chce, kelner przynosi domyślnie 1 sztukę.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''def potega(x, n=2):
    return x ** n

print(potega(3), potega(2, 3))''', opts=['9 8', '9 9', '6 8', '9 6'], a=0, out=True, why='potega(3) używa n = 2, potega(2, 3) to 2 ** 3.'),
   dict(t='fill', l=1, q='Uzupełnij wartość domyślną, aby wywołanie bez argumentu wypisało „Hej, Kapi”', code='''def hej(imie=___):
    print("Hej,", imie)
hej()''', ans=[['"Kapi"', "'Kapi'"]], expect='Hej, Kapi', why='Wartość domyślną podajemy po znaku = w nawiasie.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''def hej(imie, znak="!"):
    print("Hej, " + imie + znak)

hej("Bobo", "?")''', opts=['Hej, Bobo?', 'Hej, Bobo!', 'Hej, Bobo!?', 'Hej, Bobo'], a=0, out=True, why='Podany argument "?" zastępuje wartość domyślną "!".'),
   dict(t='bug', l=2, q='Program zgłasza błąd składni. Kliknij winną linię.', code='''def f(a=1, b):
    return a + b
print(f(2, 3))''', line=0, fix='def f(b, a=1):', why='Parametry z wartością domyślną muszą być po parametrach bez niej.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''def f(a, b=10, c=100):
    return a + b + c

print(f(1, c=5))''', opts=['16', '106', '111', '15'], a=0, out=True, why='a = 1, b domyślnie 10, c podane po nazwie = 5.'),
   dict(t='code', l=2, q='Napisz funkcję <code>linia(n, znak="-")</code>, która <b>zwraca</b> tekst złożony z n znaków.<br><code>linia(3)</code> → <code>"---"</code>, <code>linia(2, "*")</code> → <code>"**"</code>',
        start='def linia(n, znak="-"):\n    \n', tests=[], check="assert linia(3) == '---', 'linia(3) ma dać ---'\nassert linia(2, '*') == '**'\nassert linia(0) == ''",
        sol='def linia(n, znak="-"):\n    return znak * n', hint='return znak * n'),
  ]),
 dict(id='zasieg', title='Zasięg zmiennych',
  theory="""<p>Zmienne utworzone <b>wewnątrz</b> funkcji są <b>lokalne</b> – istnieją tylko podczas jej działania i nie widać ich na zewnątrz.</p>
<p>Zmienne utworzone poza funkcjami są <b>globalne</b> – funkcja może je odczytać.</p>
<p>Jeśli funkcja przypisze coś do zmiennej o tej samej nazwie, tworzy <b>nową, lokalną</b> zmienną – globalna się nie zmienia.</p>""",
  more="""<p>Aby zmienić zmienną globalną w funkcji, trzeba napisać <code>global nazwa</code>. Lepiej jednak przekazywać dane parametrami i oddawać przez <code>return</code> – kod jest wtedy czytelniejszy. Częsty błąd: odczyt zmiennej przed lokalnym przypisaniem → <code>UnboundLocalError</code>.</p>""",
  ex=[
   dict(code='''owoce = 10          # globalna

def piknik():
    owoce = 2       # lokalna – inna zmienna!
    print("w namiocie:", owoce)

piknik()
print("w domu:", owoce)''',
        scene=dict(s='scope', glob=[['owoce', '10']], loc=[['owoce', '2']], fn='piknik()', cap='Kapi ma 10 owoców w domu (globalnie). Na piknik w namiocie (funkcji) bierze osobny koszyk z 2 owocami. Domowy zapas się nie zmienia.')),
   dict(code='''licznik = 0

def dodaj():
    global licznik
    licznik += 1

dodaj()
dodaj()
print(licznik)''', lvl=2,
        scene=dict(s='scope', glob=[['licznik', '0 → 2']], loc=[], fn='dodaj()', cap='Słowo global pozwala Kapi z namiotu sięgnąć do domowego licznika i go zmienić.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 5
def f():
    x = 100
f()
print(x)''', opts=['5', '100', 'Błąd', 'None'], a=0, out=True, why='x = 100 w funkcji tworzy zmienną lokalną. Globalne x nadal wynosi 5.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 5
def f():
    print(x * 2)
f()''', opts=['10', '5', 'Błąd', 'None'], a=0, out=True, why='Funkcja może odczytać zmienną globalną.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''def f():
    tajne = 42
f()
print(tajne)''', line=3, fix='Funkcja powinna zwrócić tajne (return), a wynik f() trzeba zapisać.',
        why='tajne jest zmienną lokalną funkcji f – poza nią nie istnieje: NameError.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''n = 1
def f():
    global n
    n = n + 10
f()
f()
print(n)''', opts=['21', '11', '1', 'Błąd'], a=0, out=True, why='global pozwala zmienić zmienną globalną. Dwa wywołania dodają 10 + 10.'),
   dict(t='bug', l=3, q='Program zgłasza błąd. Kliknij linię, w której Python go wykrył.', code='''punkty = 0
def zdobadz():
    punkty = punkty + 1
zdobadz()''', line=2, fix='    global punkty  (dopisz w funkcji przed tą linią)',
        why='Przypisanie w funkcji sprawia, że punkty jest lokalne – a odczyt następuje przed nadaniem wartości: UnboundLocalError.'),
   dict(t='code', l=2, q='Popraw funkcję tak, by <b>zwracała</b> nowy wynik zamiast zmieniać globalną zmienną. Funkcja <code>dodaj_punkty(p, ile)</code> ma zwracać p + ile.',
        start='def dodaj_punkty(p, ile):\n    \n\nwynik = 0\nwynik = dodaj_punkty(wynik, 5)\nprint(wynik)\n', tests=[dict(i='', o='5')],
        check="assert dodaj_punkty(10, 3) == 13\nassert 'global' not in __src, 'Bez global!'",
        sol='def dodaj_punkty(p, ile):\n    return p + ile\n\nwynik = 0\nwynik = dodaj_punkty(wynik, 5)\nprint(wynik)', hint='return p + ile'),
  ]),
 ]))

CH.append(dict(
 id='rozsz', icon=dict(rpg='🧪', space='🔭', neutral='🧰'),
 name=dict(rpg='Wieża Alchemika', space='Laboratorium', neutral='Rozszerzenia'),
 topic='random, math, try/except, pliki',
 lessons=[
 dict(id='moduly', title='Moduły random i math',
  theory="""<p><b>Moduł</b> to gotowy zestaw funkcji. Wczytujemy go przez <code>import</code>:</p>
<ul><li><code>import random</code> → <code>random.randint(1, 6)</code> – losowa liczba całkowita od 1 do 6 (włącznie!), <code>random.choice(lista)</code> – losowy element, <code>random.shuffle(lista)</code> – tasowanie</li>
<li><code>import math</code> → <code>math.sqrt(16)</code> – pierwiastek, <code>math.pi</code>, <code>math.floor()</code> / <code>math.ceil()</code> – zaokrąglenie w dół / w górę</li></ul>""",
  more="""<p>Można importować wybrane funkcje: <code>from math import sqrt</code> – wtedy piszesz samo <code>sqrt(16)</code>. <code>random.random()</code> daje liczbę z przedziału [0, 1). <code>random.seed(1)</code> sprawia, że „losowanie” jest powtarzalne – przydatne przy testach.</p>""",
  ex=[
   dict(code='''import random
rzut = random.randint(1, 6)
print("Kapi wyrzucił:", rzut)
przekaska = random.choice(["arbuz", "melon", "trawa"])
print("Dziś na obiad:", przekaska)''', rnd=True,
        scene=dict(s='dice', cap='Kapi rzuca kostką i losuje obiad. Każde uruchomienie może dać inny wynik – kliknij kostkę!')),
   dict(code='''import math
print(math.sqrt(49))
print(math.floor(3.7), math.ceil(3.2))
print(round(math.pi, 3))''',
        scene=dict(s='cards', items=[['math.sqrt(49)', '7.0', 'pierwiastek'], ['math.floor(3.7)', '3', 'w dół'], ['math.ceil(3.2)', '4', 'w górę'], ['round(math.pi, 3)', '3.142', 'pi']], cap='Kapi korzysta z kalkulatora naukowego zamiast liczyć na łapkach.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Jakie liczby może zwrócić <code>random.randint(1, 3)</code>?', opts=['1, 2 lub 3', '1 lub 2', '0, 1, 2 lub 3', 'tylko 1 i 3'], a=0,
        why='randint obejmuje oba końce przedziału – inaczej niż range.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''import math
print(math.sqrt(81))''', opts=['9.0', '9', '81', '6561'], a=0, out=True, why='sqrt zawsze zwraca float, więc 9.0.'),
   dict(t='fill', l=1, q='Uzupełnij, aby wczytać moduł', code='''___ random
print(random.randint(5, 5))''', ans=[['import']], expect='5', why='Moduły wczytujemy instrukcją import.'),
   dict(t='bug', l=1, q='Program zgłasza błąd. Kliknij winną linię.', code='''import math
print(sqrt(25))''', line=1, fix='print(math.sqrt(25))', why='Po import math trzeba pisać math.sqrt. Samo sqrt nie jest znane: NameError.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''import math
print(math.ceil(7 / 2), math.floor(-1.5))''', opts=['4 -2', '3 -1', '4 -1', '3 -2'], a=0, out=True, why='ceil(3.5) = 4; floor zaokrągla w dół, więc -1.5 → -2.'),
   dict(t='code', l=1, q='Zasymuluj rzut dwiema kostkami: wylosuj dwie liczby 1–6 i wypisz ich sumę.',
        start='import random\n', tests=[], check="import re\nassert 'randint' in __src, 'Użyj random.randint'\nv = int(__out.strip().split()[-1])\nassert 2 <= v <= 12, 'Suma musi być od 2 do 12'",
        sol='import random\na = random.randint(1, 6)\nb = random.randint(1, 6)\nprint(a + b)', hint='random.randint(1, 6) + random.randint(1, 6)'),
   dict(t='code', l=2, q='Wczytaj przyprostokątne a i b (liczby całkowite). Wypisz długość przeciwprostokątnej zaokrągloną do 2 miejsc (użyj <code>math.sqrt</code>).',
        start='import math\n', tests=[dict(i='3\n4', o='5.0'), dict(i='1\n1', o='1.41')], sol='import math\na = int(input())\nb = int(input())\nprint(round(math.sqrt(a * a + b * b), 2))',
        hint='round(math.sqrt(a**2 + b**2), 2)'),
   dict(t='code', l=3, q='Gra „Zgadnij liczbę”: wylosowano już liczbę <code>tajna</code> (1–100). Wczytuj kolejne próby i wypisuj <code>za mało</code> / <code>za dużo</code>, aż użytkownik trafi – wtedy wypisz <code>Brawo! Próby: N</code>.',
        start='import random\nrandom.seed(7)\ntajna = random.randint(1, 100)\n', tests=[dict(i='50\n25\n42', o='za dużo\nza mało\nBrawo! Próby: 3')],
        setup='', sol='import random\nrandom.seed(7)\ntajna = random.randint(1, 100)\nproby = 0\nwhile True:\n    x = int(input())\n    proby += 1\n    if x < tajna:\n        print("za mało")\n    elif x > tajna:\n        print("za dużo")\n    else:\n        print(f"Brawo! Próby: {proby}")\n        break',
        hint='while True z licznikiem prób i break po trafieniu. (Dzięki seed(7) tajna liczba w teście to zawsze ta sama.)'),
  ]),
 dict(id='try', title='Obsługa błędów: try/except',
  theory="""<p>Gdy coś pójdzie źle (np. ktoś wpisze „abc” zamiast liczby), program się wywraca. <code>try/except</code> pozwala złapać błąd i zareagować:</p>
<pre>try:
    n = int(input())
except ValueError:
    print("To nie liczba!")</pre>
<p>Kod w <code>try</code> jest „próbowany”. Gdy pojawi się błąd, Python skacze do <code>except</code>.</p>""",
  more="""<p>Można łapać kilka typów: <code>except (ValueError, ZeroDivisionError):</code>, a nawet zapisać błąd: <code>except ValueError as e:</code>. Blok <code>else</code> wykona się, gdy błędu nie było, a <code>finally</code> – zawsze. Typowy wzorzec: <code>while True</code> + <code>try</code> + <code>break</code> – pytamy, aż dane będą poprawne.</p>""",
  ex=[
   dict(code='''tekst = input("Ile arbuzów? ")
try:
    n = int(tekst)
    print("Kapi zje", n, "arbuzy")
except ValueError:
    print("Hej, to nie jest liczba! 🙈")''', inp='dużo',
        scene=dict(s='err', err='ValueError: invalid literal for int()', caught=True, cap='Kapi trzyma tarczę try/except. Błąd odbija się od niej zamiast wywrócić program.')),
   dict(code='''while True:
    try:
        x = int(input("Podaj liczbę: "))
        print(10 / x)
        break
    except ValueError:
        print("To nie liczba")
    except ZeroDivisionError:
        print("Nie dziel przez zero!")''', inp='abc\n0\n4', lvl=2,
        scene=dict(s='err', err='ZeroDivisionError: division by zero', caught=True, cap='Kapi pyta do skutku: każdy zły pomysł odbija się od tarczy, aż wreszcie dane są dobre.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''try:
    x = int("12a")
    print("OK")
except ValueError:
    print("Błąd")''', opts=['Błąd', 'OK', 'OK\nBłąd', '12'], a=0, out=True, why='int("12a") zgłasza ValueError, więc print("OK") się nie wykona.'),
   dict(t='quiz', l=1, q='Jaki błąd zgłosi <code>10 / 0</code>?', opts=['ZeroDivisionError', 'ValueError', 'TypeError', 'NameError'], a=0, why='Dzielenie przez zero to ZeroDivisionError.'),
   dict(t='fill', l=1, q='Uzupełnij słowo, które łapie błąd', code='''try:
    print(1 / 0)
___ ZeroDivisionError:
    print("Nie wolno!")''', ans=[['except']], expect='Nie wolno!', why='Błędy łapiemy w bloku except.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''try:
    t = [1, 2]
    print(t[5])
except ValueError:
    print("A")
except IndexError:
    print("B")''', opts=['B', 'A', 'A\nB', 'Błąd'], a=0, out=True, why='t[5] zgłasza IndexError – łapie go drugi except.'),
   dict(t='quiz', l=3, q='Co wypisze program?', code='''try:
    x = 5
except:
    print("A")
else:
    print("B")
finally:
    print("C")''', opts=['B\nC', 'A\nC', 'C', 'A\nB\nC'], a=0, out=True, why='Błędu nie było, więc działa else, a finally działa zawsze.'),
   dict(t='code', l=1, q='Wczytaj tekst. Jeśli to liczba całkowita, wypisz jej podwojenie. Jeśli nie – wypisz <code>To nie liczba</code>.',
        start='s = input()\n', tests=[dict(i='21', o='42'), dict(i='kapi', o='To nie liczba')], sol='s = input()\ntry:\n    print(int(s) * 2)\nexcept ValueError:\n    print("To nie liczba")',
        hint='try: print(int(s) * 2) except ValueError: …'),
   dict(t='code', l=2, q='Wczytuj tekst, dopóki użytkownik nie poda poprawnej liczby całkowitej. Po każdej złej próbie wypisz <code>Spróbuj ponownie</code>. Na końcu wypisz <code>OK: liczba</code>.',
        start='', tests=[dict(i='abc\n3.5\n7', o='Spróbuj ponownie\nSpróbuj ponownie\nOK: 7'), dict(i='5', o='OK: 5')],
        sol='while True:\n    try:\n        n = int(input())\n        break\n    except ValueError:\n        print("Spróbuj ponownie")\nprint(f"OK: {n}")', hint='while True + try + break'),
   dict(t='code', l=3, q='Wczytaj dwie linie: a i b. Wypisz a / b zaokrąglone do 2 miejsc. Gdy dane nie są liczbami, wypisz <code>Złe dane</code>, a przy dzieleniu przez zero – <code>Dzielenie przez zero</code>.',
        start='', tests=[dict(i='7\n2', o='3.5'), dict(i='1\n0', o='Dzielenie przez zero'), dict(i='x\n2', o='Złe dane')],
        sol='try:\n    a = float(input())\n    b = float(input())\n    print(round(a / b, 2))\nexcept ValueError:\n    print("Złe dane")\nexcept ZeroDivisionError:\n    print("Dzielenie przez zero")', hint='Dwa bloki except.'),
  ]),
 dict(id='pliki', title='Pliki: open, with',
  theory="""<p>Plik otwieramy funkcją <code>open(nazwa, tryb)</code>. Tryby: <code>"r"</code> – odczyt, <code>"w"</code> – zapis (kasuje starą treść!), <code>"a"</code> – dopisywanie na końcu.</p>
<p>Najlepiej używać <code>with</code> – plik sam się zamknie:</p>
<pre>with open("dziennik.txt", "w") as f:
    f.write("Kapi pływał\\n")</pre>
<p>💡 W aplikacji pliki są tworzone w wirtualnym folderze przeglądarki.</p>""",
  more="""<p>Odczyt: <code>f.read()</code> – cały tekst, <code>f.readlines()</code> – lista linii, albo <code>for linia in f:</code> – linia po linii (każda kończy się <code>\\n</code>, więc przydaje się <code>strip()</code>). Dla polskich znaków dodaj <code>encoding="utf-8"</code>. Brak pliku przy odczycie → <code>FileNotFoundError</code>.</p>""",
  ex=[
   dict(code='''with open("dziennik.txt", "w", encoding="utf-8") as f:
    f.write("Poniedziałek: kąpiel\\n")
    f.write("Wtorek: arbuz\\n")

with open("dziennik.txt", encoding="utf-8") as f:
    for linia in f:
        print(linia.strip())''',
        scene=dict(s='file', name='dziennik.txt', lines=['Poniedziałek: kąpiel', 'Wtorek: arbuz'], cap='Kapi zapisuje pamiętnik na zwoju (tryb "w"), a potem czyta go linijka po linijce.')),
   dict(code='''with open("wyniki.txt", "w") as f:
    for p in [5, 8, 3]:
        f.write(f"{p}\\n")

suma = 0
with open("wyniki.txt") as f:
    for linia in f:
        suma += int(linia)
print("Suma punktów:", suma)''', lvl=2,
        scene=dict(s='file', name='wyniki.txt', lines=['5', '8', '3'], cap='Kapi zapisuje wyniki z zawodów pływackich, a potem je sumuje.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Który tryb <b>kasuje</b> starą zawartość pliku?', opts=['"w"', '"r"', '"a"', 'żaden'], a=0, why='"w" tworzy plik od nowa. Do dopisywania służy "a".'),
   dict(t='quiz', l=1, q='Po co używamy <code>with open(...) as f:</code>?', opts=['Plik zamknie się sam po wyjściu z bloku', 'Plik otworzy się szybciej', 'Bez with nie da się czytać pliku', 'Żeby zapisać plik w chmurze'], a=0,
        why='with automatycznie zamyka plik, nawet gdy wystąpi błąd.'),
   dict(t='fill', l=1, q='Uzupełnij tryb, aby <b>dopisać</b> linię na końcu pliku', code='''with open("a.txt", "w") as f:
    f.write("1\\n")
with open("a.txt", "___") as f:
    f.write("2\\n")
print(open("a.txt").read().split())''', ans=[['a']], expect="['1', '2']", why='Tryb "a" (append) dopisuje na końcu.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''with open("t.txt", "w") as f:
    f.write("ala\\nma\\nkota\\n")
with open("t.txt") as f:
    print(len(f.readlines()))''', opts=['3', '1', '11', '12'], a=0, out=True, why='Plik ma 3 linie.'),
   dict(t='bug', l=2, q='Program zgłasza błąd. Kliknij winną linię.', code='''with open("plan.txt", "w") as f:
    f.write("kąpiel")
with open("plan.txt", "r") as f:
    f.write("drzemka")''', line=3, fix='with open("plan.txt", "a") as f:  (w linii 3)',
        why='Plik otwarto w trybie "r" (tylko odczyt), więc write zgłasza błąd io.UnsupportedOperation.'),
   dict(t='code', l=1, q='Zapisz do pliku <code>owoce.txt</code> trzy linie: <code>arbuz</code>, <code>melon</code>, <code>jabłko</code>. Potem odczytaj plik i wypisz jego zawartość.',
        start='', tests=[dict(i='', o='arbuz\nmelon\njabłko')], check="assert open('owoce.txt', encoding='utf-8').read().split() == ['arbuz', 'melon', 'jabłko'], 'Plik owoce.txt ma złą zawartość'",
        sol='with open("owoce.txt", "w", encoding="utf-8") as f:\n    f.write("arbuz\\nmelon\\njabłko\\n")\nwith open("owoce.txt", encoding="utf-8") as f:\n    print(f.read().strip())',
        hint='Najpierw with open(..., "w"), potem with open(...) i print(f.read()).'),
   dict(t='code', l=2, q='Plik <code>liczby.txt</code> już istnieje – w każdej linii jest liczba całkowita. Wypisz największą z nich.',
        setup="open('liczby.txt','w').write('4\\n17\\n-3\\n9\\n')", start='', tests=[dict(i='', o='17')],
        sol='with open("liczby.txt") as f:\n    t = [int(l) for l in f]\nprint(max(t))', hint='Wczytaj linie, zamień na int, znajdź największą.'),
   dict(t='code', l=3, q='Plik <code>oceny.txt</code> ma linie <code>imię ocena</code>. Zapisz do pliku <code>srednie.txt</code> i wypisz na ekran średnią każdej osoby (2 miejsca), w kolejności pierwszego pojawienia się: <code>Kapi 4.50</code>.',
        setup="open('oceny.txt','w').write('Kapi 5\\nBobo 3\\nKapi 4\\nBobo 4\\nLulu 6\\n')", start='',
        tests=[dict(i='', o='Kapi 4.50\nBobo 3.50\nLulu 6.00')], check="assert open('srednie.txt').read().split() == ['Kapi', '4.50', 'Bobo', '3.50', 'Lulu', '6.00'], 'Sprawdź plik srednie.txt'",
        sol='d = {}\nwith open("oceny.txt") as f:\n    for l in f:\n        im, o = l.split()\n        d.setdefault(im, []).append(int(o))\nwith open("srednie.txt", "w") as f:\n    for im, t in d.items():\n        w = f"{im} {sum(t) / len(t):.2f}"\n        print(w)\n        f.write(w + "\\n")',
        hint='Słownik imię → lista ocen.'),
  ]),
 ]))

CH.append(dict(
 id='algorytmy', icon=dict(rpg='🐉', space='🌠', neutral='🏆'),
 name=dict(rpg='Smocza Góra Algorytmów', space='Czarna Dziura Algorytmów', neutral='Algorytmy'),
 topic='klasyczne algorytmy, błędy, rekurencja',
 lessons=[
 dict(id='suma', title='Suma, średnia, min/max',
  theory="""<p>Klasyczne algorytmy „ręcznie”, bez gotowych funkcji <code>sum</code>, <code>min</code>, <code>max</code>:</p>
<ul><li><b>Suma</b>: zacznij od <code>s = 0</code>, w pętli dodawaj elementy.</li><li><b>Średnia</b>: suma / liczba elementów.</li><li><b>Maksimum</b>: załóż, że największy jest pierwszy element, potem porównuj z każdym kolejnym.</li></ul>""",
  more="""<p>Przy maksimum nie zaczynaj od <code>m = 0</code> – dla samych ujemnych liczb wynik byłby zły! Zaczynaj od pierwszego elementu. Można jednocześnie zapamiętać pozycję (indeks) maksimum.</p>""",
  ex=[
   dict(code='''arbuzy = [4, 9, 2, 7]
s = 0
for x in arbuzy:
    s += x
print("Suma:", s)
print("Średnia:", s / len(arbuzy))''',
        scene=dict(s='loop', items=['4', '9', '2', '7'], acc='s', accv=[4, 13, 15, 22], cap='Kapi waży arbuzy i dorzuca każdy na wagę zbiorczą.')),
   dict(code='''t = [4, 9, 2, 7]
m = t[0]
for x in t:
    if x > m:
        m = x
print("Największy:", m)''',
        scene=dict(s='loop', items=['4', '9', '2', '7'], acc='m', accv=[4, 9, 9, 9], cap='Kapi trzyma w łapkach najcięższy do tej pory arbuz. Gdy znajdzie cięższy – wymienia.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [3, 5, 2]
s = 0
for x in t:
    s += x
print(s / len(t))''', opts=['3.3333333333333335', '10', '3', '3.33'], a=0, out=True, why='Suma 10, podzielona przez 3 elementy.'),
   dict(t='fill', l=1, q='Uzupełnij warunek szukania minimum', code='''t = [6, 2, 8]
m = t[0]
for x in t:
    if x ___ m:
        m = x
print(m)''', ans=[['<', '<=']], expect='2', why='Szukając minimum, zamieniamy, gdy znajdziemy mniejszy element.'),
   dict(t='bug', l=2, q='Program ma znaleźć największą liczbę, ale dla tej listy wypisuje 0. Kliknij winną linię.', code='''t = [-5, -2, -9]
m = 0
for x in t:
    if x > m:
        m = x
print(m)''', line=1, fix='m = t[0]', noerr=True, why='Startowanie od 0 psuje wynik dla liczb ujemnych. Zacznij od pierwszego elementu.'),
   dict(t='code', l=1, q='Wczytaj liczby w jednej linii. Wypisz ich sumę – <b>bez</b> funkcji <code>sum</code>.',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='1 2 3 4', o='10'), dict(i='-5 5', o='0')],
        check="assert 'sum(' not in __src, 'Bez funkcji sum!'", sol='t = [int(x) for x in input().split()]\ns = 0\nfor x in t:\n    s += x\nprint(s)', hint='s = 0; for x in t: s += x'),
   dict(t='code', l=2, q='Wczytaj liczby w jednej linii. Wypisz najmniejszą i największą (oddzielone spacją) – <b>bez</b> <code>min</code>/<code>max</code>/<code>sort</code>.',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='4 -2 9 0', o='-2 9'), dict(i='-3 -8 -1', o='-8 -1')],
        check="assert 'min(' not in __src and 'max(' not in __src and 'sort' not in __src, 'Bez min, max i sort!'",
        sol='t = [int(x) for x in input().split()]\na = b = t[0]\nfor x in t:\n    if x < a:\n        a = x\n    if x > b:\n        b = x\nprint(a, b)', hint='a = b = t[0]'),
   dict(t='code', l=3, q='Wczytaj liczby. Wypisz <b>indeks</b> pierwszego wystąpienia największej liczby (bez max i index).',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='3 9 2 9', o='1'), dict(i='5', o='0'), dict(i='1 2 3', o='2')],
        check="assert 'max(' not in __src and '.index' not in __src", sol='t = [int(x) for x in input().split()]\nk = 0\nfor i in range(len(t)):\n    if t[i] > t[k]:\n        k = i\nprint(k)',
        hint='Pamiętaj indeks k zamiast wartości.'),
  ]),
 dict(id='szukanie', title='Zliczanie i wyszukiwanie liniowe',
  theory="""<p><b>Zliczanie</b>: licznik <code>ile = 0</code> i <code>ile += 1</code> za każdym razem, gdy element spełnia warunek.</p>
<p><b>Wyszukiwanie liniowe</b>: sprawdzamy elementy po kolei, aż znajdziemy szukany. Jeśli dojdziemy do końca – nie ma go. Zwykle zwracamy indeks albo <code>-1</code>.</p>""",
  more="""<p>W najgorszym przypadku sprawdzamy wszystkie n elementów – to złożoność liniowa O(n). Dla posortowanych danych istnieje szybsze wyszukiwanie binarne. Wbudowane skróty: <code>t.count(x)</code>, <code>x in t</code>, <code>t.index(x)</code>.</p>""",
  ex=[
   dict(code='''def szukaj(t, cel):
    for i in range(len(t)):
        if t[i] == cel:
            return i
    return -1

nory = ["Bobo", "Lulu", "Kapi", "Mimi"]
print(szukaj(nory, "Kapi"))
print(szukaj(nory, "Zuzu"))''',
        scene=dict(s='search', items=['Bobo', 'Lulu', 'Kapi', 'Mimi'], target='Kapi', cap='Szukamy Kapi, zaglądając do nor po kolei. Znaleziony w norze nr 2!')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [3, 7, 3, 1, 3]
ile = 0
for x in t:
    if x == 3:
        ile += 1
print(ile)''', opts=['3', '2', '5', '1'], a=0, out=True, why='Liczba 3 pojawia się trzy razy.'),
   dict(t='quiz', l=1, q='Ile porównań wykona wyszukiwanie liniowe w najgorszym przypadku dla listy 100 elementów?', opts=['100', '50', '10', '1'], a=0,
        why='W najgorszym razie sprawdzamy wszystkie elementy.'),
   dict(t='bug', l=2, q='Funkcja ma zwrócić indeks albo -1, ale dla [5, 8, 2] i cel = 2 zwraca -1. Kliknij winną linię.', code='''def szukaj(t, cel):
    for i in range(len(t)):
        if t[i] == cel:
            return i
        return -1''', line=4, fix='    return -1  (wcięte na poziomie pętli for, nie if)', noerr=True,
        why='return -1 jest wewnątrz pętli, więc funkcja kończy się już po pierwszym elemencie.'),
   dict(t='code', l=1, q='Wczytaj liczby w jednej linii. Wypisz, ile z nich jest parzystych.',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='1 2 3 4 6', o='3'), dict(i='1 3', o='0')],
        sol='t = [int(x) for x in input().split()]\nile = 0\nfor x in t:\n    if x % 2 == 0:\n        ile += 1\nprint(ile)', hint='if x % 2 == 0: ile += 1'),
   dict(t='code', l=2, q='Napisz funkcję <code>szukaj(t, cel)</code>, zwracającą indeks pierwszego wystąpienia cel albo -1 (bez <code>index</code> i <code>in</code> w warunku).',
        start='def szukaj(t, cel):\n    \n', tests=[], check="assert szukaj([4, 2, 7, 2], 2) == 1\nassert szukaj([4, 2], 9) == -1, 'Dla braku elementu zwróć -1'\nassert szukaj([], 1) == -1\nassert '.index' not in __src",
        sol='def szukaj(t, cel):\n    for i in range(len(t)):\n        if t[i] == cel:\n            return i\n    return -1', hint='return -1 dopiero po pętli!'),
   dict(t='code', l=3, q='Wczytaj liczby. Wypisz długość najdłuższego ciągu kolejnych <b>takich samych</b> liczb. Np. <code>1 1 2 2 2 1</code> → <code>3</code>.',
        start='t = input().split()\n', tests=[dict(i='1 1 2 2 2 1', o='3'), dict(i='5', o='1'), dict(i='1 2 3', o='1'), dict(i='4 4 4 4', o='4')],
        sol='t = input().split()\nbest = cur = 1\nfor i in range(1, len(t)):\n    if t[i] == t[i - 1]:\n        cur += 1\n    else:\n        cur = 1\n    if cur > best:\n        best = cur\nprint(best)',
        hint='Licznik bieżącej serii i najlepszej serii.'),
  ]),
 dict(id='babel', title='Sortowanie bąbelkowe',
  theory="""<p>Sortowanie bąbelkowe porównuje <b>sąsiednie</b> elementy i zamienia je, jeśli są w złej kolejności. Po każdym przejściu największy element „wypływa” na koniec – jak bąbelek!</p>
<pre>for i in range(n - 1):
    for j in range(n - 1 - i):
        if t[j] > t[j + 1]:
            t[j], t[j + 1] = t[j + 1], t[j]</pre>""",
  more="""<p>Złożoność: około n² porównań – dla dużych danych wolne. Usprawnienie: jeśli w przejściu nie było żadnej zamiany, lista jest posortowana i można przerwać (<code>break</code>). Zmiana <code>&gt;</code> na <code>&lt;</code> sortuje malejąco.</p>""",
  ex=[
   dict(code='''t = [5, 3, 8, 1]
n = len(t)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if t[j] > t[j + 1]:
            t[j], t[j + 1] = t[j + 1], t[j]
    print(t)''',
        scene=dict(s='sort', arr=[5, 3, 8, 1], cap='Kapibary różnego wzrostu stają w szeregu. Kapi porównuje sąsiadów i zamienia ich miejscami. Naciśnij ▶!')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co porównuje sortowanie bąbelkowe?', opts=['Sąsiednie elementy', 'Pierwszy z ostatnim', 'Każdy element ze średnią', 'Losowe pary'], a=0,
        why='Zawsze porównujemy t[j] z t[j + 1].'),
   dict(t='quiz', l=2, q='Jak wygląda lista <code>[4, 1, 3, 2]</code> po <b>pierwszym</b> przejściu sortowania bąbelkowego?', code='''t = [4, 1, 3, 2]
for j in range(3):
    if t[j] > t[j + 1]:
        t[j], t[j + 1] = t[j + 1], t[j]
print(t)''', opts=['[1, 3, 2, 4]', '[1, 2, 3, 4]', '[1, 4, 3, 2]', '[4, 3, 2, 1]'], a=0, out=True, why='Czwórka „wypływa” na koniec, reszta przesuwa się o jedno miejsce.'),
   dict(t='quiz', l=1, q='Gdzie trafia największy element po pierwszym przejściu sortowania bąbelkowego (rosnąco)?', opts=['Na koniec listy', 'Na początek listy', 'Na środek listy', 'Zostaje na miejscu'], a=0,
        why='Największy element jest przepychany przy każdym porównaniu, aż „wypłynie” na koniec.'),
   dict(t='fill', l=1, q='Uzupełnij zamianę dwóch elementów', code='''t = [9, 4]
t[0], t[1] = ___
print(t)''', ans=[['t[1],t[0]', 't[1], t[0]']], expect='[4, 9]', why='W Pythonie zamiana to a, b = b, a.'),
   dict(t='bug', l=2, q='Program zgłasza błąd. Kliknij winną linię.', code='''t = [3, 1, 2]
for i in range(len(t)):
    for j in range(len(t) - i):
        if t[j] > t[j + 1]:
            t[j], t[j + 1] = t[j + 1], t[j]
print(t)''', line=3, fix='    for j in range(len(t) - 1 - i):  (zakres w linii 3)', cause=True,
        why='Gdy j dojdzie do ostatniego indeksu, t[j + 1] wychodzi poza listę: IndexError. Zakres pętli j powinien być mniejszy o 1.'),
   dict(t='code', l=2, q='Wczytaj liczby i posortuj je bąbelkowo <b>rosnąco</b> (bez <code>sort</code>/<code>sorted</code>). Wypisz oddzielone spacją.',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='5 3 8 1', o='1 3 5 8'), dict(i='2 2 1', o='1 2 2'), dict(i='7', o='7')],
        check="assert 'sort' not in __src, 'Bez sort i sorted!'",
        sol='t = [int(x) for x in input().split()]\nn = len(t)\nfor i in range(n - 1):\n    for j in range(n - 1 - i):\n        if t[j] > t[j + 1]:\n            t[j], t[j + 1] = t[j + 1], t[j]\nprint(*t)', hint='Dwie pętle i zamiana sąsiadów.'),
   dict(t='code', l=3, q='Posortuj bąbelkowo <b>malejąco</b> i wypisz, ile zamian wykonano.<br>Wejście: liczby w linii. Wyjście: posortowane liczby, w drugiej linii liczba zamian.',
        start='t = [int(x) for x in input().split()]\n', tests=[dict(i='1 2 3', o='3 2 1\n3'), dict(i='3 1 2', o='3 2 1\n1')],
        check="assert 'sort' not in __src",
        sol='t = [int(x) for x in input().split()]\nn = len(t)\nz = 0\nfor i in range(n - 1):\n    for j in range(n - 1 - i):\n        if t[j] < t[j + 1]:\n            t[j], t[j + 1] = t[j + 1], t[j]\n            z += 1\nprint(*t)\nprint(z)',
        hint='Odwróć znak porównania i licz zamiany.'),
  ]),
 dict(id='nwd', title='NWD, liczby pierwsze, palindromy',
  theory="""<p><b>NWD</b> (algorytm Euklidesa): dopóki b ≠ 0, zamieniaj <code>a, b = b, a % b</code>. Na końcu a to NWD.</p>
<p><b>Liczba pierwsza</b> ma dokładnie dwa dzielniki: 1 i siebie. Sprawdzamy dzielniki od 2 do √n.</p>
<p><b>Palindrom</b> czyta się tak samo od przodu i od tyłu: <code>s == s[::-1]</code>.</p>""",
  more="""<p>NWW liczymy z NWD: <code>nww = a * b // nwd(a, b)</code>. Do sprawdzania pierwszości wystarczą dzielniki d, dla których <code>d * d &lt;= n</code> – gdyby n miało większy dzielnik, miałoby też mniejszy. Dla palindromów zdaniowych najpierw usuń spacje i zamień litery na małe.</p>""",
  ex=[
   dict(code='''def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(nwd(48, 18))''',
        scene=dict(s='cards', items=[['a=48, b=18', '48 % 18 = 12', ''], ['a=18, b=12', '18 % 12 = 6', ''], ['a=12, b=6', '12 % 6 = 0', ''], ['a=6, b=0', 'NWD = 6', 'koniec!']], cap='Kapi ma 48 arbuzów i 18 melonów i chce ułożyć jednakowe koszyki. Euklides mówi: 6 koszyków!')),
   dict(code='''def pierwsza(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print([x for x in range(2, 30) if pierwsza(x)])''',
        scene=dict(s='row', items=['2', '3', '5', '7', '11', '13', '17', '19', '23', '29'], label='liczby pierwsze < 30', cap='Kapi sprawdza, czy da się podzielić stosik owoców na równe kupki. Dla liczb pierwszych się nie da!')),
   dict(code='''for s in ["kajak", "kapi", "potop"]:
    print(s, s == s[::-1])''',
        scene=dict(s='row', items=list('KAJAK'), label='kajak = kajak[::-1]', cap='Kapi płynie kajakiem: od przodu i od tyłu ta sama nazwa!')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Która liczba jest pierwsza?', opts=['13', '15', '21', '1'], a=0, why='13 dzieli się tylko przez 1 i 13. Liczba 1 nie jest pierwsza.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''s = "level"
print(s == s[::-1])''', opts=['True', 'False', 'level', 'leveL'], a=0, out=True, why='"level" od tyłu to nadal "level".'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''a, b = 20, 8
while b != 0:
    a, b = b, a % b
print(a)''', opts=['4', '8', '2', '160'], a=0, out=True, why='(20, 8) → (8, 4) → (4, 0). NWD = 4.'),
   dict(t='fill', l=1, q='Uzupełnij krok algorytmu Euklidesa', code='''a, b = 12, 18
while b != 0:
    a, b = b, ___
print(a)''', ans=[['a%b', 'a % b']], expect='6', why='Nowe b to reszta z dzielenia a przez b.'),
   dict(t='bug', l=2, q='Funkcja uznaje 9 za liczbę pierwszą. Kliknij winną linię.', code='''def pierwsza(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return False
        d += 1
    return True''', line=2, fix='    while d * d <= n:', noerr=True, why='Dla n = 9 warunek 3 * 3 < 9 jest fałszywy, więc dzielnik 3 nie zostaje sprawdzony. Potrzeba <=.'),
   dict(t='code', l=1, q='Wczytaj słowo i wypisz <code>TAK</code>, jeśli jest palindromem, w przeciwnym razie <code>NIE</code>.',
        start='s = input()\n', tests=[dict(i='kajak', o='TAK'), dict(i='kapi', o='NIE'), dict(i='a', o='TAK')],
        sol='s = input()\nif s == s[::-1]:\n    print("TAK")\nelse:\n    print("NIE")', hint='s == s[::-1]'),
   dict(t='code', l=2, q='Napisz funkcję <code>nwd(a, b)</code> algorytmem Euklidesa (bez modułu math).',
        start='def nwd(a, b):\n    \n', tests=[], check="assert nwd(48, 18) == 6\nassert nwd(7, 5) == 1\nassert nwd(10, 100) == 10\nassert 'gcd' not in __src, 'Bez math.gcd!'",
        sol='def nwd(a, b):\n    while b != 0:\n        a, b = b, a % b\n    return a', hint='while b != 0: a, b = b, a % b'),
   dict(t='code', l=2, q='Napisz funkcję <code>pierwsza(n)</code> zwracającą True/False. Uwaga na 0, 1 i 2!',
        start='def pierwsza(n):\n    \n', tests=[], check="assert [x for x in range(30) if pierwsza(x)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Sprawdź liczby 0–29'\nassert pierwsza(97) and not pierwsza(91)",
        sol='def pierwsza(n):\n    if n < 2:\n        return False\n    d = 2\n    while d * d <= n:\n        if n % d == 0:\n            return False\n        d += 1\n    return True', hint='n < 2 → False; dzielniki od 2 dopóki d*d <= n.'),
   dict(t='code', l=3, q='Wczytaj zdanie. Sprawdź, czy jest palindromem, ignorując spacje i wielkość liter. Wypisz <code>TAK</code>/<code>NIE</code>.<br>Np. <code>Kobyła ma mały bok</code> → TAK',
        start='s = input()\n', tests=[dict(i='Kobyła ma mały bok', o='TAK'), dict(i='Kapi lubi wodę', o='NIE'), dict(i='Ile Roman ładny dyndał na moreli', o='TAK')],
        sol='s = input().replace(" ", "").lower()\nprint("TAK" if s == s[::-1] else "NIE")', hint='Usuń spacje: replace(" ", ""), potem lower().'),
  ]),
 dict(id='bledy', title='Czytanie komunikatów błędów',
  theory="""<p>Błąd to nie porażka – to <b>wskazówka</b>! Komunikat Pythona mówi:</p>
<ul><li><b>gdzie</b>: <code>line 3</code> – numer linii</li><li><b>co</b>: typ błędu, np. <code>NameError</code></li><li><b>dlaczego</b>: opis, np. <code>name 'x' is not defined</code></li></ul>
<p>Najczęstsze:</p><ul><li><code>SyntaxError</code> – literówka w składni (brak <code>:</code>, nawiasu, cudzysłowu)</li><li><code>IndentationError</code> – złe wcięcie</li><li><code>NameError</code> – nieznana nazwa (literówka?)</li><li><code>TypeError</code> – złe typy, np. <code>"2" + 2</code></li><li><code>ValueError</code> – zła wartość, np. <code>int("abc")</code></li><li><code>IndexError</code> – indeks poza listą</li><li><code>KeyError</code> – brak klucza w słowniku</li><li><code>ZeroDivisionError</code> – dzielenie przez 0</li></ul>""",
  more="""<p>Traceback czytaj <b>od dołu</b>: ostatnia linia to typ i opis błędu, a nad nią – miejsce, gdzie wystąpił. Przy <code>SyntaxError</code> prawdziwy błąd bywa linię <b>wyżej</b> (np. niezamknięty nawias). Błędy logiczne nie dają komunikatu – wtedy pomagają <code>print</code>-y kontrolne.</p>""",
  ex=[
   dict(code='''wiek = 4
print("Kapi ma " + wiek + " lata")''',
        scene=dict(s='err', err='TypeError: can only concatenate str (not "int") to str', caught=False, cap='Kapi próbuje skleić tekst z liczbą – i wszystko się rozsypuje. Komunikat mówi: można łączyć tylko str ze str. Rozwiązanie: str(wiek) albo f-string.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Jaki błąd zgłosi kod <code>print("a" + 1)</code>?', code='print("a" + 1)', opts=['TypeError', 'ValueError', 'SyntaxError', 'NameError'], a=0, err=True,
        why='Nie można dodać tekstu i liczby – to błąd typów.'),
   dict(t='quiz', l=1, q='Jaki błąd zgłosi kod?', code='''imie = "Kapi"
print(imei)''', opts=['NameError', 'TypeError', 'SyntaxError', 'KeyError'], a=0, err=True, why='Literówka: imei nie istnieje.'),
   dict(t='quiz', l=1, q='Jaki błąd zgłosi kod?', code='''t = [1, 2, 3]
print(t[3])''', opts=['IndexError', 'KeyError', 'ValueError', 'TypeError'], a=0, err=True, why='Lista ma indeksy 0–2.'),
   dict(t='quiz', l=1, q='Jaki błąd zgłosi kod?', code='''d = {"a": 1}
print(d["b"])''', opts=['KeyError', 'IndexError', 'NameError', 'ValueError'], a=0, err=True, why='Brak klucza w słowniku to KeyError.'),
   dict(t='quiz', l=3, q='Jaki błąd zgłosi kod?', code='''def f():
return 5''', opts=['IndentationError', 'SyntaxError: brak dwukropka', 'NameError', 'TypeError'], a=0, err=True, why='Ciało funkcji musi być wcięte.'),
   dict(t='bug', l=1, q='Przeczytaj komunikat błędu i kliknij winną linię.', code='''a = 5
b = 0
c = a + 2
print(a / b)''', line=3, fix='Sprawdź, czy b != 0 przed dzieleniem.', why='ZeroDivisionError – dzielenie przez b, które wynosi 0.'),
   dict(t='bug', l=2, q='Przeczytaj komunikat błędu i kliknij linię, którą trzeba poprawić.', code='''t = [4, 5, 6]
print(sum(t)
print("koniec")''', line=1, fix='print(sum(t))', cause=True,
        why='Niezamknięty nawias w linii 2. Python zauważa problem dopiero dalej – dlatego przy SyntaxError zawsze patrz też linię wyżej.'),
   dict(t='code', l=1, q='Ten program ma błąd. Uruchom go, przeczytaj komunikat i popraw, aby wypisał <code>Kapi ma 4 lata</code>.',
        start='wiek = 4\nprint("Kapi ma " + wiek + " lata")\n', tests=[dict(i='', o='Kapi ma 4 lata')],
        sol='wiek = 4\nprint("Kapi ma " + str(wiek) + " lata")', hint='Zamień liczbę na tekst: str(wiek), albo użyj f-stringa.'),
   dict(t='code', l=2, q='Ten program ma 3 błędy. Popraw je, aby wypisał sumę liczb od 1 do 5: <code>15</code>.',
        start='suma = 0\nfor i in range(1, 6)\n    suma = suma + I\nprint(Suma)\n', tests=[dict(i='', o='15')],
        sol='suma = 0\nfor i in range(1, 6):\n    suma = suma + i\nprint(suma)', hint='Dwukropek, wielkość liter, wielkość liter.'),
  ]),
 dict(id='rekur', title='Rekurencja',
  theory="""<p><b>Rekurencja</b> to funkcja, która wywołuje <b>samą siebie</b> dla mniejszego problemu. Każda funkcja rekurencyjna potrzebuje:</p>
<ul><li><b>warunku stopu</b> (przypadek bazowy) – kiedy kończymy,</li><li><b>kroku rekurencyjnego</b> – wywołania dla mniejszych danych.</li></ul>
<pre>def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)</pre>""",
  more="""<p>Bez warunku stopu funkcja wywołuje się w nieskończoność → <code>RecursionError</code>. Fibonacci rekurencyjnie: <code>fib(n) = fib(n-1) + fib(n-2)</code> – pięknie, ale wolno, bo te same wartości liczą się wiele razy. Rekurencyjnie można też liczyć NWD: <code>nwd(a, b) = nwd(b, a % b)</code>.</p>""",
  ex=[
   dict(code='''def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)

print(silnia(4))''',
        scene=dict(s='stack', frames=['silnia(4)', 'silnia(3)', 'silnia(2)', 'silnia(1)', 'silnia(0)'], rets=['24', '6', '2', '1', '1'], cap='Kapi otwiera matrioszki: każda kryje mniejszą. Najmniejsza (silnia(0)) zwraca 1, a wyniki wracają w górę: 1, 1, 2, 6, 24.')),
   dict(code='''def odliczaj(n):
    if n == 0:
        print("Plusk! 💦")
        return
    print(n)
    odliczaj(n - 1)

odliczaj(3)''',
        scene=dict(s='stack', frames=['odliczaj(3)', 'odliczaj(2)', 'odliczaj(1)', 'odliczaj(0)'], rets=['', '', '', 'Plusk!'], cap='Kapi schodzi po schodkach do basenu, aż dotrze do wody – to warunek stopu.')),
  ],
  tasks=[
   dict(t='quiz', l=1, q='Co musi mieć każda funkcja rekurencyjna?', opts=['Warunek stopu', 'Pętlę while', 'Zmienną globalną', 'Parametr domyślny'], a=0,
        why='Bez warunku stopu rekurencja trwałaby w nieskończoność.'),
   dict(t='quiz', l=1, q='Co wypisze program?', code='''def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)

print(f(4))''', opts=['10', '4', '24', '0'], a=0, out=True, why='4 + 3 + 2 + 1 + 0 = 10.'),
   dict(t='quiz', l=2, q='Co wypisze program?', code='''def f(n):
    if n == 0:
        return
    f(n - 1)
    print(n, end=" ")

f(3)''', opts=['1 2 3 ', '3 2 1 ', '0 1 2 3 ', '3 '], a=0, out=True,
        why='print jest PO wywołaniu rekurencyjnym, więc liczby wypisują się podczas „powrotu” – od najmniejszej.'),
   dict(t='bug', l=2, q='Program zgłasza błąd. Kliknij linię, którą trzeba poprawić.', code='''def silnia(n):
    if n == 1:
        return 1
    return n * silnia(n - 1)
print(silnia(0))''', line=1, fix='    if n <= 1:', cause=True,
        why='Dla n = 0 warunek n == 1 nigdy nie zachodzi – n schodzi do -1, -2, … aż do RecursionError.'),
   dict(t='fill', l=1, q='Uzupełnij krok rekurencyjny potęgi', code='''def potega(a, n):
    if n == 0:
        return 1
    return a * ___
print(potega(2, 5))''', ans=[['potega(a,n-1)', 'potega(a, n - 1)', 'potega(a, n-1)']], expect='32', why='aⁿ = a · aⁿ⁻¹'),
   dict(t='code', l=2, q='Napisz rekurencyjną funkcję <code>suma_cyfr(n)</code> (bez pętli i bez zamiany na tekst).',
        start='def suma_cyfr(n):\n    \n', tests=[], check="assert suma_cyfr(472) == 13\nassert suma_cyfr(0) == 0\nassert suma_cyfr(9) == 9\nassert 'for' not in __src and 'while' not in __src and 'str(' not in __src, 'Bez pętli i str!'",
        sol='def suma_cyfr(n):\n    if n == 0:\n        return 0\n    return n % 10 + suma_cyfr(n // 10)', hint='ostatnia cyfra n % 10 + suma_cyfr(n // 10)'),
   dict(t='code', l=3, q='Napisz rekurencyjną funkcję <code>fib(n)</code>: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).',
        start='def fib(n):\n    \n', tests=[], check="assert [fib(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Sprawdź pierwsze 10 wyrazów'",
        sol='def fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)', hint='if n < 2: return n'),
   dict(t='code', l=3, q='Napisz rekurencyjną funkcję <code>odwroc(s)</code> zwracającą tekst od tyłu (bez <code>[::-1]</code> i bez pętli).',
        start='def odwroc(s):\n    \n', tests=[], check="assert odwroc('kapi') == 'ipak'\nassert odwroc('') == ''\nassert '::-1' not in __src and 'for' not in __src and 'while' not in __src",
        sol='def odwroc(s):\n    if s == "":\n        return ""\n    return odwroc(s[1:]) + s[0]', hint='odwroc(s[1:]) + s[0]'),
  ]),
 ]))
