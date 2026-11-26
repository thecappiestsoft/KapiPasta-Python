# Treść kursu KapiPasta - Python (PL) – DODATKOWE zadania, dopisywane NA KOŃCU lekcji.
# Klucz = id lekcji. Kolejność ma znaczenie (postęp uczniów jest przypisany do pozycji).
# Po zmianach uruchom: python3 tools/build.py

EXTRA = {}

EXTRA['print'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''print("2 + 3")
print(2 + 3)''', opts=['2 + 3\n5', '5\n5', '2 + 3\n2 + 3', 'Błąd'], a=0, out=True,
      why='Tekst w cudzysłowie jest wypisywany dosłownie, a działanie bez cudzysłowu jest obliczane.'),
 dict(t='fill', l=2, q='Uzupełnij, aby wypisało: <code>A-B</code>', code='print("A", "B", ___="-")', ans=[['sep']], expect='A-B',
      why='Parametr sep określa, czym oddzielić wartości.'),
 dict(t='code', l=3, q='Używając <b>jednego</b> print, wypisz ramkę w trzech liniach:<br><code>+------+<br>| Kapi |<br>+------+</code>',
      start='', tests=[dict(i='', o='+------+\n| Kapi |\n+------+')], check="assert __src.count('print') == 1, 'Użyj tylko jednego print'",
      sol='print("+------+", "| Kapi |", "+------+", sep="\\n")', hint='sep="\\n" wstawia znak nowej linii między wartości.'),
]
EXTRA['fstr'] = [
 dict(t='quiz', l=2, q='Co wypisze program?', code='print(f"{7 / 2:.0f}")', opts=['4', '3', '3.5', '3.50'], a=0, out=True,
      why='.0f zaokrągla do liczby całkowitej (3.5 → 4).'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='''x = 5
print(f"{x=}")''', opts=['x=5', '5', '{x=}', 'x = 5'], a=0, out=True,
      why='Znak = w f-stringu wypisuje nazwę zmiennej i jej wartość – świetne do debugowania.'),
 dict(t='code', l=3, q='Wczytaj nazwę produktu, cenę (float) i ilość (int). Wypisz linię paragonu:<br>nazwa wyrównana do lewej na 10 znaków, ilość do prawej na 3, cena i wartość do prawej z 2 miejscami (szerokość 6 i 7).<br>Dla <code>melon / 4.5 / 3</code>: <code>melon       3 x   4.50 =   13.50</code>',
      start='', tests=[dict(i='melon\n4.5\n3', o='melon       3 x   4.50 =   13.50'), dict(i='arbuz\n12\n1', o='arbuz       1 x  12.00 =   12.00')],
      sol='n = input()\nc = float(input())\ni = int(input())\nprint(f"{n:<10}{i:>3} x {c:>6.2f} = {i * c:>7.2f}")', hint='f"{n:<10}{i:>3} x {c:>6.2f} = {i * c:>7.2f}"'),
]
EXTRA['zmienne'] = [
 dict(t='quiz', l=2, q='Co wypisze program?', code='''a = "5"
b = 5
print(a * 2, b * 2)''', opts=['55 10', '10 10', '55 55', 'Błąd'], a=0, out=True, why='Tekst razy 2 to powtórzenie, liczba razy 2 to mnożenie.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='print(type(10 / 2))', opts=["<class 'float'>", "<class 'int'>", '5.0', '5'], a=0, out=True,
      why='Dzielenie / zawsze daje float, nawet gdy wynik jest „okrągły”.'),
 dict(t='bug', l=2, q='Program zgłasza błąd. Kliknij winną linię.', code='''x = 5
y = "3"
print(x + y)''', line=2, fix='print(x + int(y))', why='Nie można dodać liczby i tekstu – TypeError. Trzeba zamienić y na liczbę.'),
 dict(t='code', l=3, q='Zamień wartości a i b miejscami <b>bez</b> zapisu <code>a, b = b, a</code> i bez trzeciej zmiennej – użyj dodawania i odejmowania.',
      start='a = int(input())\nb = int(input())\n# zamień a i b\n\nprint(a, b)\n', tests=[dict(i='3\n8', o='8 3'), dict(i='-2\n5', o='5 -2')],
      check="assert 'b, a' not in __src, 'Bez a, b = b, a!'", sol='a = int(input())\nb = int(input())\na = a + b\nb = a - b\na = a - b\nprint(a, b)',
      hint='a = a + b, potem b = a - b, potem a = a - b.'),
]
EXTRA['input'] = [
 dict(t='quiz', l=1, q='Użytkownik wpisuje 5. Co wypisze program?', code='''x = input()
print(x * 3)''', inp='5', opts=['555', '15', '5 5 5', 'Błąd'], a=0, out=True, why='input() zwraca tekst "5", a tekst razy 3 to "555".'),
 dict(t='bug', l=2, q='Użytkownik wpisuje 12. Który wiersz zgłasza błąd?', code='''wiek = input("Wiek: ")
print(wiek + 1)''', inp='12', line=1, fix='print(int(wiek) + 1)', why='wiek to tekst. Tekstu nie można dodać do liczby – TypeError.'),
 dict(t='code', l=3, q='Wczytaj trzy liczby w <b>jednej</b> linii oddzielone spacjami (np. <code>3 4 5</code>) i wypisz ich średnią z 2 miejscami po przecinku.',
      start='', tests=[dict(i='3 4 5', o='4.00'), dict(i='1 2 2', o='1.67')], sol='a, b, c = map(float, input().split())\nprint(f"{(a + b + c) / 3:.2f}")',
      hint='a, b, c = map(float, input().split())'),
]
EXTRA['oper'] = [
 dict(t='quiz', l=2, q='Co wypisze program?', code='print(2 ** 3 ** 2)', opts=['512', '64', '36', 'Błąd'], a=0, out=True,
      why='Potęgowanie liczy się od prawej: 3 ** 2 = 9, a 2 ** 9 = 512.'),
 dict(t='code', l=3, q='Wczytaj liczbę minut (może przekraczać dobę). Wypisz godzinę na zegarze w formacie <code>HH:MM</code> z zerami wiodącymi.<br>Np. 1505 → <code>01:05</code>',
      start='m = int(input())\n', tests=[dict(i='1505', o='01:05'), dict(i='59', o='00:59'), dict(i='1440', o='00:00')],
      sol='m = int(input())\nprint(f"{m // 60 % 24:02d}:{m % 60:02d}")', hint='Godzina: m // 60 % 24, format :02d dodaje zero wiodące.'),
]
EXTRA['logika'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='print(not True == False)', opts=['True', 'False', 'Błąd', 'None'], a=0, out=True,
      why='Najpierw porównanie: True == False to False, a not False to True.'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='''print(0 or "Kapi")
print(3 and 0)''', opts=['Kapi\n0', 'True\nFalse', '0\n3', 'Kapi\nFalse'], a=0, out=True,
      why='or zwraca pierwszą „prawdziwą” wartość, a and – pierwszą „fałszywą” (albo ostatnią).'),
 dict(t='code', l=3, q='Wczytaj trzy długości boków (każda w nowej linii). Wypisz <code>True</code>, jeśli da się z nich zbudować trójkąt (każdy bok krótszy od sumy dwóch pozostałych), inaczej <code>False</code> – bez if.',
      start='', tests=[dict(i='3\n4\n5', o='True'), dict(i='1\n2\n3', o='False'), dict(i='5\n1\n1', o='False')], check="assert 'if' not in __src, 'Bez if!'",
      sol='a = int(input())\nb = int(input())\nc = int(input())\nprint(a < b + c and b < a + c and c < a + b)', hint='Połącz trzy warunki przez and.'),
]
EXTRA['if'] = [
 dict(t='quiz', l=2, q='Co wypisze program?', code='''x = 0
if x:
    print("A")
else:
    print("B")''', opts=['B', 'A', 'A\nB', 'Błąd'], a=0, out=True, why='Liczba 0 jest traktowana jak False.'),
 dict(t='bug', l=2, q='Dla 95 punktów program wypisuje „dostateczny”. Kliknij linię, którą trzeba zmienić.', code='''punkty = 95
if punkty >= 50:
    print("dostateczny")
elif punkty >= 90:
    print("celujący")''', line=1, noerr=True, fix='if punkty >= 90:  (sprawdzaj od najwyższego progu)',
      why='Pierwszy pasujący warunek wygrywa – 95 >= 50 jest prawdą, więc elif nie jest sprawdzany.'),
 dict(t='code', l=3, q='Wczytaj trzy liczby (każda w nowej linii) i wypisz je rosnąco, oddzielone spacją – tylko za pomocą if (bez sort, min, max).',
      start='', tests=[dict(i='3\n1\n2', o='1 2 3'), dict(i='5\n5\n1', o='1 5 5'), dict(i='-1\n0\n-2', o='-2 -1 0')],
      check="assert 'sort' not in __src and 'min(' not in __src and 'max(' not in __src, 'Bez sort, min i max!'",
      sol='a = int(input())\nb = int(input())\nc = int(input())\nif a > b:\n    a, b = b, a\nif b > c:\n    b, c = c, b\nif a > b:\n    a, b = b, a\nprint(a, b, c)',
      hint='Zamieniaj sąsiednie pary: (a, b), (b, c), znowu (a, b).'),
]
EXTRA['for'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''for i in range(3):
    print(i * 2, end=" ")''', opts=['0 2 4 ', '2 4 6 ', '0 1 2 ', '0 2 4 6 '], a=0, out=True, why='i przyjmuje 0, 1, 2, a wypisujemy podwojone wartości.'),
 dict(t='fill', l=2, q='Uzupełnij krok, aby zsumować liczby parzyste od 0 do 10', code='''s = 0
for i in range(0, 11, ___):
    s += i
print(s)''', ans=[['2']], expect='30', why='Krok 2 daje 0, 2, 4, 6, 8, 10 – ich suma to 30.'),
 dict(t='code', l=3, q='Wczytaj n i wypisz n-ty wyraz ciągu Fibonacciego (F0 = 0, F1 = 1, każdy kolejny to suma dwóch poprzednich). Użyj pętli for.',
      start='n = int(input())\n', tests=[dict(i='0', o='0'), dict(i='1', o='1'), dict(i='10', o='55'), dict(i='30', o='832040')],
      sol='n = int(input())\na, b = 0, 1\nfor i in range(n):\n    a, b = b, a + b\nprint(a)', hint='Trzymaj dwie ostatnie wartości: a, b = b, a + b.'),
 dict(t='code', l=3, q='Wczytaj n i wypisz wszystkie dzielniki n rosnąco, oddzielone spacją.',
      start='n = int(input())\n', tests=[dict(i='12', o='1 2 3 4 6 12'), dict(i='7', o='1 7'), dict(i='1', o='1')],
      sol='n = int(input())\nd = []\nfor i in range(1, n + 1):\n    if n % i == 0:\n        d.append(str(i))\nprint(" ".join(d))', hint='Sprawdź każde i od 1 do n: n % i == 0.'),
]
EXTRA['while'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''i = 0
while i < 10:
    i += 3
print(i)''', opts=['12', '9', '10', '3'], a=0, out=True, why='i: 0 → 3 → 6 → 9 → 12. Przy 12 warunek i < 10 jest fałszywy.'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='''for i in range(3):
    if i == 5:
        break
else:
    print("brak")''', opts=['brak', 'nic', '0 1 2', 'Błąd'], a=0, out=True, why='else przy pętli for wykonuje się, gdy pętla nie została przerwana przez break.'),
 dict(t='code', l=3, q='Problem Collatza: wczytaj n. Dopóki n ≠ 1: gdy n parzyste – n = n // 2, w przeciwnym razie n = 3n + 1. Wypisz liczbę kroków.',
      start='n = int(input())\n', tests=[dict(i='6', o='8'), dict(i='1', o='0'), dict(i='27', o='111')],
      sol='n = int(input())\nk = 0\nwhile n != 1:\n    if n % 2 == 0:\n        n //= 2\n    else:\n        n = 3 * n + 1\n    k += 1\nprint(k)', hint='while n != 1: … k += 1'),
]
EXTRA['zagn'] = [
 dict(t='quiz', l=1, q='Ile gwiazdek wypisze program?', code='''for i in range(3):
    for j in range(i):
        print("*")''', opts=['3', '6', '9', '2'], a=0, why='Dla i = 0, 1, 2 wewnętrzna pętla wykonuje się 0 + 1 + 2 = 3 razy.'),
 dict(t='fill', l=1, q='Uzupełnij, aby powstały schodki z #', code='''for i in range(1, 4):
    print(___ * i)''', ans=[['"#"', "'#'"]], expect='#\n##\n###', why='Tekst razy liczba powtarza tekst.'),
 dict(t='code', l=3, q='Wczytaj n. Wypisz wszystkie pary <code>a b</code>, gdzie 1 ≤ a &lt; b ≤ n i a + b jest parzyste (każda para w nowej linii, rosnąco).',
      start='n = int(input())\n', tests=[dict(i='4', o='1 3\n2 4'), dict(i='5', o='1 3\n1 5\n2 4\n3 5')],
      sol='n = int(input())\nfor a in range(1, n + 1):\n    for b in range(a + 1, n + 1):\n        if (a + b) % 2 == 0:\n            print(a, b)', hint='Wewnętrzna pętla od a + 1.'),
]
EXTRA['slice'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''s = "python"
print(s[2:])''', opts=['thon', 'ython', 'pyt', 'hon'], a=0, out=True, why='Od indeksu 2 do końca.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''s = "python"
print(s[-3:])''', opts=['hon', 'pyt', 'tho', 'noh'], a=0, out=True, why='Trzy ostatnie znaki.'),
 dict(t='code', l=3, q='Wczytaj słowo i wypisz je z zamienioną pierwszą i ostatnią literą (słowo jednoliterowe bez zmian).',
      start='s = input()\n', tests=[dict(i='kapibara', o='aapibark'), dict(i='ab', o='ba'), dict(i='x', o='x')],
      sol='s = input()\nif len(s) < 2:\n    print(s)\nelse:\n    print(s[-1] + s[1:-1] + s[0])', hint='s[-1] + s[1:-1] + s[0]'),
]
EXTRA['metody'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='print("Ala".lower().count("a"))', opts=['2', '1', '3', '0'], a=0, out=True, why='"Ala".lower() to "ala" – są w nim dwa „a”.'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='print("a,b,,c".split(","))', opts=["['a', 'b', '', 'c']", "['a', 'b', 'c']", "['a,b,,c']", 'a b c'], a=0, out=True,
      why='Między dwoma przecinkami jest pusty tekst.'),
 dict(t='code', l=3, q='Wczytaj zdanie i wypisz je tak, by każde słowo zaczynało się wielką literą, a reszta była mała – <b>bez</b> metody title().',
      start='s = input()\n', tests=[dict(i='kAPI lubi WODĘ', o='Kapi Lubi Wodę'), dict(i='a', o='A')], check="assert 'title' not in __src, 'Bez title()!'",
      sol='s = input()\nprint(" ".join(w[0].upper() + w[1:].lower() for w in s.split()))', hint='Dla każdego słowa: w[0].upper() + w[1:].lower()'),
]
EXTRA['znaki'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''for z in "abc":
    print(z, end="-")''', opts=['a-b-c-', 'abc', 'a-b-c', '-a-b-c'], a=0, out=True, why='Po każdej literze wypisywany jest myślnik.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''w = ""
for z in "Kapi":
    if z.isupper():
        w += z.lower()
    else:
        w += z.upper()
print(w)''', opts=['kAPI', 'KAPI', 'kapi', 'Kapi'], a=0, out=True, why='Wielkie litery stają się małe, a małe – wielkie.'),
 dict(t='code', l=3, q='Kompresja RLE: wczytaj słowo i zapisz każdy ciąg tych samych liter jako literę i liczbę powtórzeń.<br><code>aaabccdddd</code> → <code>a3b1c2d4</code>',
      start='s = input()\n', tests=[dict(i='aaabccdddd', o='a3b1c2d4'), dict(i='x', o='x1'), dict(i='abab', o='a1b1a1b1')],
      sol='s = input()\nw = ""\nn = 1\nfor i in range(1, len(s) + 1):\n    if i < len(s) and s[i] == s[i - 1]:\n        n += 1\n    else:\n        w += s[i - 1] + str(n)\n        n = 1\nprint(w)',
      hint='Licz powtórzenia; gdy litera się zmienia, dopisz literę i licznik.'),
]
EXTRA['listy'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [1, 2, 3]
print(t[-2])''', opts=['2', '3', '1', '-2'], a=0, out=True, why='-1 to ostatni element, -2 – przedostatni.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''t = [[1, 2], [3, 4]]
print(t[1][0])''', opts=['3', '2', '[3, 4]', '1'], a=0, out=True, why='t[1] to [3, 4], a jego element 0 to 3.'),
 dict(t='code', l=3, q='Wczytaj liczby w jednej linii. Wypisz je bez pierwszego i ostatniego elementu, w odwrotnej kolejności, oddzielone spacją (użyj wycinków).',
      start='t = input().split()\n', tests=[dict(i='1 2 3 4 5', o='4 3 2'), dict(i='7 8 9', o='8'), dict(i='10 20 30 40', o='30 20')],
      sol='t = input().split()\nprint(" ".join(t[1:-1][::-1]))', hint='t[1:-1][::-1]'),
]
EXTRA['metodylist'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''t = ["a"]
t.insert(0, "b")
print(t)''', opts=["['b', 'a']", "['a', 'b']", "['b']", "['a']"], a=0, out=True, why='insert(0, x) wstawia na początek.'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='''t = [3, 1, 2]
s = sorted(t)
print(t, s)''', opts=['[3, 1, 2] [1, 2, 3]', '[1, 2, 3] [1, 2, 3]', '[3, 1, 2] None', 'None [1, 2, 3]'], a=0, out=True,
      why='sorted() tworzy nową listę i nie zmienia oryginału.'),
 dict(t='code', l=3, q='Wczytaj liczby w jednej linii. Usuń z listy wszystkie zera (użyj while i remove) i wypisz listę.',
      start='t = [int(x) for x in input().split()]\n', tests=[dict(i='0 1 0 2 0', o='[1, 2]'), dict(i='0', o='[]'), dict(i='5', o='[5]')],
      check="assert 'remove' in __src and 'while' in __src, 'Użyj while i remove'", sol='t = [int(x) for x in input().split()]\nwhile 0 in t:\n    t.remove(0)\nprint(t)',
      hint='while 0 in t: t.remove(0)'),
]
EXTRA['krotki'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='print(len((1, 2, 3)))', opts=['3', '1', '6', 'Błąd'], a=0, out=True, why='Krotka ma 3 elementy.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''a = {1, 2, 3}
a.add(2)
a.add(4)
print(len(a))''', opts=['4', '5', '3', '2'], a=0, out=True, why='2 już jest w zbiorze, więc zostaje dodane tylko 4.'),
 dict(t='code', l=3, q='Wczytaj dwa zdania (dwie linie). Wypisz alfabetycznie słowa występujące w obu, oddzielone spacją.',
      start='', tests=[dict(i='kapi lubi wodę\nbobo lubi wodę', o='lubi wodę'), dict(i='a b c\nc b x', o='b c')],
      sol='a = set(input().split())\nb = set(input().split())\nprint(" ".join(sorted(a & b)))', hint='sorted(a & b)'),
]
EXTRA['slowniki'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''d = {"a": 1}
d["a"] = 5
print(d)''', opts=["{'a': 5}", "{'a': 1}", "{'a': 1, 'a': 5}", 'Błąd'], a=0, out=True, why='Klucze są unikalne – przypisanie nadpisuje wartość.'),
 dict(t='quiz', l=1, q='Co wypisze program?', code='''d = {"x": 1, "y": 2}
print(list(d.keys()))''', opts=["['x', 'y']", '[1, 2]', "[('x', 1), ('y', 2)]", "{'x', 'y'}"], a=0, out=True, why='keys() zwraca klucze.'),
 dict(t='bug', l=2, q='Program zgłasza błąd. Kliknij winną linię.', code='''d = {"a": 1}
for k in d:
    print(k, d[v])''', line=2, fix='    print(k, d[k])', why='Zmienna v nie istnieje – NameError. W pętli używamy k.'),
 dict(t='code', l=3, q='Wczytaj zdanie. Pogrupuj słowa według długości i wypisz grupy rosnąco wg długości w formacie <code>długość: słowa</code> (słowa w kolejności pojawienia się).',
      start='s = input()\n', tests=[dict(i='ala ma kota i psa', o='1: i\n2: ma\n3: ala psa\n4: kota')],
      sol='s = input()\nd = {}\nfor w in s.split():\n    d.setdefault(len(w), []).append(w)\nfor k in sorted(d):\n    print(f"{k}: {\' \'.join(d[k])}")', hint='Słownik długość → lista słów, potem sorted(d).'),
]
EXTRA['def'] = [
 dict(t='quiz', l=3, q='Co wypisze program?', code='''def f(a, b):
    return a, b

x = f(1, 2)
print(x)''', opts=['(1, 2)', '1 2', '[1, 2]', '1'], a=0, out=True, why='return a, b zwraca krotkę.'),
 dict(t='code', l=3, q='Napisz funkcję <code>czy_anagram(a, b)</code> zwracającą True, gdy słowa składają się z tych samych liter (ignoruj wielkość liter).',
      start='def czy_anagram(a, b):\n    \n', tests=[], check="assert czy_anagram('Kot', 'tok') is True\nassert czy_anagram('kapi', 'pika') is True\nassert czy_anagram('kapi', 'kapa') is False\nassert czy_anagram('ab', 'abb') is False",
      sol='def czy_anagram(a, b):\n    return sorted(a.lower()) == sorted(b.lower())', hint='sorted("kot") daje listę posortowanych liter.'),
]
EXTRA['domyslne'] = [
 dict(t='fill', l=1, q='Uzupełnij, aby wypisało: <code>Hej, Kapi?</code>', code='''def powitaj(imie, znak="!"):
    print("Hej, " + imie + znak)
powitaj("Kapi", znak=___)''', ans=[['"?"', "'?'"]], expect='Hej, Kapi?', why='Argument można podać po nazwie parametru.'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='''def dodaj(x, t=[]):
    t.append(x)
    return t

dodaj(1)
print(dodaj(2))''', opts=['[1, 2]', '[2]', '[1]', 'Błąd'], a=0, out=True,
      why='Pułapka! Domyślna lista tworzy się raz i jest wspólna dla wywołań. Lepiej pisać t=None.'),
 dict(t='code', l=3, q='Napisz funkcję <code>zaokr(x, miejsca=0)</code>: zwraca x zaokrąglone do podanej liczby miejsc; gdy miejsca == 0 – zwraca liczbę całkowitą (int).',
      start='def zaokr(x, miejsca=0):\n    \n', tests=[], check="assert zaokr(2.567, 2) == 2.57\nassert zaokr(2.6) == 3 and type(zaokr(2.6)) is int, 'zaokr(2.6) ma zwrócić int 3'\nassert zaokr(1.25, 1) == 1.2",
      sol='def zaokr(x, miejsca=0):\n    if miejsca == 0:\n        return int(round(x))\n    return round(x, miejsca)', hint='round(x, miejsca); dla 0 użyj int(round(x)).'),
]
EXTRA['zasieg'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''def f():
    y = 3
    return y

print(f())''', opts=['3', 'Błąd', 'None', 'y'], a=0, out=True, why='Funkcja zwraca wartość lokalnej zmiennej y.'),
 dict(t='quiz', l=3, q='Co wypisze program?', code='''x = 1
def f():
    x = 2
    def g():
        return x
    return g()

print(f(), x)''', opts=['2 1', '1 1', '2 2', 'Błąd'], a=0, out=True, why='g widzi x z funkcji otaczającej (2), a globalne x zostaje 1.'),
 dict(t='code', l=3, q='Napisz funkcję <code>licznik()</code>, która zwiększa globalną zmienną <code>wywolania</code> o 1 i zwraca jej nową wartość.',
      start='wywolania = 0\n\ndef licznik():\n    \n', tests=[], check="a = licznik()\nb = licznik()\nassert (a, b) == (1, 2), 'Pierwsze wywołanie ma dać 1, drugie 2'\nassert wywolania == 2",
      sol='wywolania = 0\n\ndef licznik():\n    global wywolania\n    wywolania += 1\n    return wywolania', hint='global wywolania'),
]
EXTRA['moduly'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''import math
print(math.pi > 3)''', opts=['True', 'False', '3.14', 'Błąd'], a=0, out=True, why='pi ≈ 3.14159 > 3.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''from math import sqrt
print(sqrt(16) + 1)''', opts=['5.0', '5', '17', 'Błąd'], a=0, out=True, why='Po from math import sqrt można pisać samo sqrt. Wynik jest float.'),
 dict(t='code', l=3, q='Rzuć monetą 10 razy: <code>random.choice(["O", "R"])</code>. Wypisz liczbę orłów (O). Ziarno losowania jest już ustawione, więc wynik jest powtarzalny.',
      start='import random\nrandom.seed(1)\n', tests=[dict(i='', o='5')], check="assert 'choice' in __src, 'Użyj random.choice'",
      sol='import random\nrandom.seed(1)\nn = 0\nfor i in range(10):\n    if random.choice(["O", "R"]) == "O":\n        n += 1\nprint(n)', hint='Pętla 10 razy i licznik orłów.'),
]
EXTRA['try'] = [
 dict(t='quiz', l=2, q='Co wypisze program?', code='''try:
    print(int("5") / 0)
except ValueError:
    print("V")
except ZeroDivisionError:
    print("Z")''', opts=['Z', 'V', '5', 'V\nZ'], a=0, out=True, why='int("5") działa, ale dzielenie przez 0 zgłasza ZeroDivisionError.'),
 dict(t='bug', l=2, q='Użytkownik wpisuje „abc”. Gdzie Python zgłasza błąd?', code='''try:
    x = int(input())
except ValueError:
    print("zła liczba")
print(x * 2)''', inp='abc', line=4, fix='Przenieś print(x * 2) do bloku try albo nadaj x wartość w except.',
      why='Po złapaniu błędu x nie istnieje, więc print(x * 2) zgłasza NameError.'),
 dict(t='code', l=3, q='Wczytaj n, potem n linii. Zsumuj tylko liczby całkowite, a resztę policz jako błędne. Wypisz <code>suma: S, błędne: B</code>.',
      start='n = int(input())\n', tests=[dict(i='4\n5\nkapi\n-2\n3.5', o='suma: 3, błędne: 2'), dict(i='1\n7', o='suma: 7, błędne: 0')],
      sol='n = int(input())\ns = 0\nb = 0\nfor i in range(n):\n    try:\n        s += int(input())\n    except ValueError:\n        b += 1\nprint(f"suma: {s}, błędne: {b}")', hint='try/except w pętli.'),
]
EXTRA['pliki'] = [
 dict(t='quiz', l=1, q='Co zwraca <code>f.read()</code>?', opts=['Cały tekst pliku jako str', 'Listę linii', 'Pierwszą linię', 'Liczbę znaków'], a=0,
      why='read() zwraca całą zawartość jako jeden tekst; listę linii daje readlines().'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''with open("a.txt", "w") as f:
    f.write("x")
with open("a.txt", "a") as f:
    f.write("y")
print(open("a.txt").read())''', opts=['xy', 'y', 'x', 'x\ny'], a=0, out=True, why='Tryb "a" dopisuje na końcu, bez nowej linii.'),
 dict(t='code', l=3, q='Plik <code>tekst.txt</code> już istnieje. Wypisz liczbę linii, słów i znaków (bez znaków nowej linii) w formacie <code>linie: L, słowa: S, znaki: Z</code>.',
      setup="open('tekst.txt','w',encoding='utf-8').write('Kapi lubi wodę\\nBobo lubi melony\\n')", start='', tests=[dict(i='', o='linie: 2, słowa: 6, znaki: 30')],
      sol='with open("tekst.txt", encoding="utf-8") as f:\n    linie = f.read().splitlines()\nprint(f"linie: {len(linie)}, słowa: {sum(len(l.split()) for l in linie)}, znaki: {sum(len(l) for l in linie)}")',
      hint='splitlines() usuwa znaki \\n.'),
]
EXTRA['suma'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [2, 4, 6]
s = 0
for x in t:
    s += x
print(s / len(t))''', opts=['4.0', '12', '4', '6.0'], a=0, out=True, why='12 / 3 = 4.0 (dzielenie / daje float).'),
 dict(t='quiz', l=2, q='Ile porównań wykonuje szukanie największego elementu w liście n elementów (start od t[0])?', opts=['n - 1', 'n', 'n²', '2n'], a=0,
      why='Pierwszy element jest punktem startu, więc porównujemy z pozostałymi n - 1.'),
 dict(t='code', l=3, q='Wczytaj liczby. Wypisz drugą największą <b>różną</b> wartość (bez sort i max). Gdy nie istnieje – wypisz <code>brak</code>.',
      start='t = [int(x) for x in input().split()]\n', tests=[dict(i='4 9 2 9 7', o='7'), dict(i='5 5', o='brak'), dict(i='1 2', o='1')],
      check="assert 'sort' not in __src and 'max(' not in __src, 'Bez sort i max!'",
      sol='t = [int(x) for x in input().split()]\na = b = None\nfor x in t:\n    if a is None or x > a:\n        if a is not None:\n            b = a\n        a = x\n    elif x != a and (b is None or x > b):\n        b = x\nprint("brak" if b is None else b)',
      hint='Pamiętaj dwie wartości: największą i drugą.'),
]
EXTRA['szukanie'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='print([3, 5, 3].count(3))', opts=['2', '1', '3', '0'], a=0, out=True, why='Liczba 3 występuje dwa razy.'),
 dict(t='fill', l=2, q='Uzupełnij zliczanie', code='''def ile(t, x):
    n = 0
    for e in t:
        if e == x:
            n ___ 1
    return n
print(ile([1, 2, 1], 1))''', ans=[['+=']], expect='2', why='n += 1 zwiększa licznik.'),
 dict(t='code', l=3, q='Wyszukiwanie binarne: napisz funkcję <code>binarne(t, x)</code> dla <b>posortowanej</b> listy, zwracającą indeks x albo -1 (bez in i index). Dziel zakres na pół.',
      start='def binarne(t, x):\n    \n', tests=[],
      check="t = list(range(0, 1000, 3))\nassert binarne(t, 300) == 100\nassert binarne(t, 301) == -1\nassert binarne([], 1) == -1\nassert binarne([5], 5) == 0\nassert '.index' not in __src and ' in t' not in __src",
      sol='def binarne(t, x):\n    a, b = 0, len(t) - 1\n    while a <= b:\n        s = (a + b) // 2\n        if t[s] == x:\n            return s\n        if t[s] < x:\n            a = s + 1\n        else:\n            b = s - 1\n    return -1',
      hint='a, b = 0, len(t) - 1; środek s = (a + b) // 2.'),
]
EXTRA['babel'] = [
 dict(t='quiz', l=1, q='Ile zamian wykona sortowanie bąbelkowe dla listy <code>[3, 2, 1]</code>?', opts=['3', '2', '1', '6'], a=0,
      why='(3,2)→[2,3,1], (3,1)→[2,1,3], (2,1)→[1,2,3] – trzy zamiany.'),
 dict(t='quiz', l=3, q='Po ilu przejściach lista <code>[1, 2, 3, 5, 4]</code> będzie posortowana?', opts=['1', '4', '2', '0'], a=0,
      why='Wystarczy jedna zamiana (5, 4) w pierwszym przejściu.'),
 dict(t='code', l=3, q='Sortowanie bąbelkowe z wczesnym przerwaniem: przerwij, gdy w przejściu nie było zamian. Wypisz posortowane liczby, a w drugiej linii liczbę wykonanych przejść (przejście bez zamian też się liczy).',
      start='t = [int(x) for x in input().split()]\n', tests=[dict(i='1 2 3', o='1 2 3\n1'), dict(i='3 1 2', o='1 2 3\n2'), dict(i='5 4 3 2 1', o='1 2 3 4 5\n4')],
      check="assert 'sort' not in __src",
      sol='t = [int(x) for x in input().split()]\nn = len(t)\np = 0\nfor i in range(n - 1):\n    p += 1\n    zam = False\n    for j in range(n - 1 - i):\n        if t[j] > t[j + 1]:\n            t[j], t[j + 1] = t[j + 1], t[j]\n            zam = True\n    if not zam:\n        break\nprint(*t)\nprint(p)',
      hint='Zmienna zam = False na początku przejścia; po przejściu: if not zam: break.'),
]
EXTRA['nwd'] = [
 dict(t='quiz', l=1, q='Które słowo jest palindromem?', opts=['kajak', 'kapibara', 'python', 'melon'], a=0, why='„kajak” czytany od tyłu to nadal „kajak”.'),
 dict(t='code', l=3, q='Sito Eratostenesa: wczytaj n i wypisz wszystkie liczby pierwsze ≤ n, oddzielone spacją.',
      start='n = int(input())\n', tests=[dict(i='20', o='2 3 5 7 11 13 17 19'), dict(i='2', o='2')],
      sol='n = int(input())\np = [True] * (n + 1)\nw = []\nfor i in range(2, n + 1):\n    if p[i]:\n        w.append(str(i))\n        for k in range(i * i, n + 1, i):\n            p[k] = False\nprint(" ".join(w))',
      hint='Lista True/False; dla każdej pierwszej i wykreśl jej wielokrotności.'),
 dict(t='code', l=3, q='Rozłóż liczbę na czynniki pierwsze. Wypisz je rosnąco oddzielone spacją.<br><code>360</code> → <code>2 2 2 3 3 5</code>',
      start='n = int(input())\n', tests=[dict(i='360', o='2 2 2 3 3 5'), dict(i='13', o='13'), dict(i='97', o='97')],
      sol='n = int(input())\nw = []\nd = 2\nwhile n > 1:\n    while n % d == 0:\n        w.append(str(d))\n        n //= d\n    d += 1\nprint(" ".join(w))', hint='Dziel przez d, dopóki się da, potem d += 1.'),
]
EXTRA['bledy'] = [
 dict(t='quiz', l=2, q='Jaki błąd zgłosi kod?', code='print(int("3.5"))', opts=['ValueError', 'TypeError', 'SyntaxError', 'NameError'], a=0, err=True,
      why='Tekst "3.5" nie jest poprawną liczbą całkowitą.'),
 dict(t='bug', l=3, q='Przeczytaj komunikat i kliknij winną linię.', code='''liczby = [1, 2, 3]
for i in range(len(liczby)):
    liczby[i] = liczby[i] * 2
print(liczby[3])''', line=3, fix='print(liczby[2])  (lub liczby[-1])', why='Lista ma indeksy 0–2 – IndexError.'),
 dict(t='code', l=3, q='Ten program ma 2 błędy. Popraw je, aby wypisał <code>Pole: 12</code>.',
      start='def pole(a, b)\n    return a * b\nprint("Pole: " + pole(3, 4))\n', tests=[dict(i='', o='Pole: 12')],
      sol='def pole(a, b):\n    return a * b\nprint("Pole: " + str(pole(3, 4)))', hint='Brakujący dwukropek i zamiana liczby na tekst.'),
]
EXTRA['rekur'] = [
 dict(t='quiz', l=1, q='Co wypisze program?', code='''def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 2)

print(f(5))''', opts=['8', '5', '13', '15'], a=0, out=True, why='f: 1, 1, 2, 3, 5, 8 dla n = 0…5.'),
 dict(t='fill', l=1, q='Uzupełnij rekurencyjne NWD', code='''def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, ___)
print(nwd(12, 18))''', ans=[['a%b', 'a % b']], expect='6', why='nwd(a, b) = nwd(b, a % b).'),
 dict(t='code', l=3, q='Wieże Hanoi: napisz rekurencyjną funkcję <code>hanoi(n, z, pom, do)</code>, która wypisuje ruchy w formacie <code>z -> do</code>, przenosząc n krążków.',
      start='def hanoi(n, z, pom, do):\n    \n\nhanoi(2, "A", "B", "C")\n', tests=[dict(i='', o='A -> B\nA -> C\nB -> C')],
      check="import io, sys\n_b = io.StringIO(); _o = sys.stdout; sys.stdout = _b\nhanoi(3, 'A', 'B', 'C')\nsys.stdout = _o\nassert len(_b.getvalue().split(chr(10))) - 1 == 7, '3 krążki = 7 ruchów'\nassert 'for' not in __src and 'while' not in __src",
      sol='def hanoi(n, z, pom, do):\n    if n == 0:\n        return\n    hanoi(n - 1, z, do, pom)\n    print(f"{z} -> {do}")\n    hanoi(n - 1, pom, z, do)\n\nhanoi(2, "A", "B", "C")',
      hint='Przenieś n-1 na pomocniczy, największy na docelowy, potem n-1 z pomocniczego na docelowy.'),
]

# ---------------------------------------------------------------------------
# Uzupełnienie: każda lekcja ma dokładnie 12 zadań = 6 × poziom 1, 3 × poziom 2, 3 × poziom 3
# (Odkrywca: 6 zadań, Praktyk: 9, Mistrz: 12 – łatwe przeliczanie na oceny 1–6).
# ---------------------------------------------------------------------------
def add(lid, *tasks):
    EXTRA.setdefault(lid, []).extend(tasks)

add('print',
 dict(t='quiz', l=2, q='Co wypisze program?', code='''print("a", end="")
print("b", end="\\n\\n")
print("c")''', opts=['ab\n\nc', 'ab\nc', 'a\nb\nc', 'abc'], a=0, out=True, why='end="" skleja a i b, a end="\\n\\n" dodaje pustą linię.'),
 dict(t='code', l=3, q='Wczytaj n i jednym print wypisz liczby od 1 do n oddzielone przecinkiem i spacją. Użyj <code>*range(...)</code> i <code>sep</code>.<br>4 → <code>1, 2, 3, 4</code>',
      start='n = int(input())\n', tests=[dict(i='4', o='1, 2, 3, 4'), dict(i='1', o='1')], check="assert __src.count('print') == 1 and 'for' not in __src, 'Jeden print, bez pętli'",
      sol='n = int(input())\nprint(*range(1, n + 1), sep=", ")', hint='print(*range(1, n + 1), sep=", ")'))
add('fstr',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''imie = "Bobo"
print(f"Cześć, {imie}!")''', opts=['Cześć, Bobo!', 'Cześć, {imie}!', 'Cześć, imie!', 'f"Cześć, Bobo!"'], a=0, out=True, why='{imie} zostaje zastąpione wartością zmiennej.'))
add('zmienne',
 dict(t='code', l=3, q='Wczytaj liczbę z kropką (np. <code>3.75</code>). Wypisz jej część całkowitą (int) i ułamkową zaokrągloną do 2 miejsc, oddzielone spacją.',
      start='x = float(input())\n', tests=[dict(i='3.75', o='3 0.75'), dict(i='10.5', o='10 0.5')], sol='x = float(input())\nc = int(x)\nprint(c, round(x - c, 2))',
      hint='int(x) obcina część ułamkową.'))
add('input',
 dict(t='code', l=3, q='Wczytaj w jednej linii imię i rok urodzenia, np. <code>Ola 2012</code>. Wypisz <code>Ola ma w 2026 roku 14 lat</code>.',
      start='', tests=[dict(i='Ola 2012', o='Ola ma w 2026 roku 14 lat'), dict(i='Kapi 2020', o='Kapi ma w 2026 roku 6 lat')],
      sol='imie, rok = input().split()\nprint(f"{imie} ma w 2026 roku {2026 - int(rok)} lat")', hint='imie, rok = input().split()'))
add('logika',
 dict(t='quiz', l=2, q='Co wypisze program?', code='''x = 7
print(x > 5 and x % 2 == 0 or x == 7)''', opts=['True', 'False', '7', 'Błąd'], a=0, out=True, why='(True and False) or True = True.'))
add('while',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''n = 3
while n > 0:
    print(n)
    n -= 1''', opts=['3\n2\n1', '3\n2\n1\n0', '2\n1\n0', '3'], a=0, out=True, why='Pętla działa dla n = 3, 2, 1. Przy 0 warunek jest fałszywy.'))
add('zagn',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''for i in range(2):
    for j in range(2):
        print(i, j)''', opts=['0 0\n0 1\n1 0\n1 1', '0 0\n1 1', '0 1\n1 0', '0 0\n1 0\n0 1\n1 1'], a=0, out=True,
      why='Dla każdego i wewnętrzna pętla przechodzi wszystkie j.'),
 dict(t='code', l=3, q='Wczytaj n i wypisz tabliczkę mnożenia n × n, w której każda liczba zajmuje 4 znaki wyrównane do prawej (<code>f"{x:4}"</code>).<br>Dla 2:<br><code>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;2<br>&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;4</code>',
      start='n = int(input())\n', tests=[dict(i='2', o='   1   2\n   2   4'), dict(i='3', o='   1   2   3\n   2   4   6\n   3   6   9')],
      sol='n = int(input())\nfor i in range(1, n + 1):\n    for j in range(1, n + 1):\n        print(f"{i * j:4}", end="")\n    print()', hint='print(f"{i * j:4}", end="") i print() po wierszu.'))
add('slice',
 dict(t='code', l=3, q='Wczytaj datę w formacie <code>RRRR-MM-DD</code> i wypisz ją jako <code>DD.MM.RRRR</code> – używając wycinków (bez split).',
      start='d = input()\n', tests=[dict(i='2026-11-26', o='26.11.2026'), dict(i='2000-01-05', o='05.01.2000')], check="assert 'split' not in __src, 'Użyj wycinków, bez split'",
      sol='d = input()\nprint(d[8:] + "." + d[5:7] + "." + d[:4])', hint='Rok: d[:4], miesiąc: d[5:7], dzień: d[8:]'))
add('znaki',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''for z in "kot":
    print(z.upper())''', opts=['K\nO\nT', 'KOT', 'k\no\nt', 'K O T'], a=0, out=True, why='Każda litera jest wypisywana wielką literą w osobnej linii.'),
 dict(t='code', l=3, q='Wczytaj zdanie. Policz samogłoski (<code>aeiouyąęó</code>, bez względu na wielkość) i spółgłoski (pozostałe litery). Wypisz <code>samogłoski: S, spółgłoski: P</code>.',
      start='s = input()\n', tests=[dict(i='Kapi lubi wodę', o='samogłoski: 6, spółgłoski: 6'), dict(i='Ala', o='samogłoski: 2, spółgłoski: 1')],
      sol='s = input()\nsa = sp = 0\nfor z in s.lower():\n    if z in "aeiouyąęó":\n        sa += 1\n    elif z.isalpha():\n        sp += 1\nprint(f"samogłoski: {sa}, spółgłoski: {sp}")', hint='isalpha() sprawdza, czy znak jest literą.'))
add('listy',
 dict(t='code', l=3, q='Wczytaj liczby. Wypisz listę sum częściowych: element i to suma pierwszych i+1 liczb.<br><code>1 2 3 4</code> → <code>[1, 3, 6, 10]</code>',
      start='t = [int(x) for x in input().split()]\n', tests=[dict(i='1 2 3 4', o='[1, 3, 6, 10]'), dict(i='5', o='[5]')],
      sol='t = [int(x) for x in input().split()]\nw = []\ns = 0\nfor x in t:\n    s += x\n    w.append(s)\nprint(w)', hint='Trzymaj bieżącą sumę i dopisuj ją do nowej listy.'),
 dict(t='code', l=3, q='Obróć listę o k miejsc w prawo. Pierwsza linia: liczby, druga: k (może być większe niż długość listy).<br><code>1 2 3 4 5</code>, k=2 → <code>4 5 1 2 3</code>',
      start='t = input().split()\nk = int(input())\n', tests=[dict(i='1 2 3 4 5\n2', o='4 5 1 2 3'), dict(i='1 2 3\n4', o='3 1 2'), dict(i='7 8\n0', o='7 8')],
      sol='t = input().split()\nk = int(input())\nn = len(t)\nk %= n\nt = t[n - k:] + t[:n - k]\nprint(" ".join(t))', hint='k %= len(t), potem wycinki t[n-k:] + t[:n-k].'))
add('krotki',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''punkt = (2, 5)
x, y = punkt
print(y)''', opts=['5', '2', '(2, 5)', 'Błąd'], a=0, out=True, why='Rozpakowanie: x = 2, y = 5.'),
 dict(t='code', l=3, q='Wczytaj dwie linie liczb. Wypisz rosnąco liczby, które występują tylko w jednej z nich (różnica symetryczna <code>^</code>).',
      start='', tests=[dict(i='1 2 3\n2 3 4', o='1 4'), dict(i='5 6\n5 6', o='')],
      sol='a = set(map(int, input().split()))\nb = set(map(int, input().split()))\nprint(*sorted(a ^ b))', hint='sorted(a ^ b)'),
 dict(t='code', l=3, q='Wczytaj n, potem n punktów <code>x y</code>. Wypisz jako krotkę punkt leżący najbliżej (0, 0).',
      start='n = int(input())\n', tests=[dict(i='3\n3 4\n1 1\n-2 0', o='(1, 1)'), dict(i='1\n-5 2', o='(-5, 2)')],
      sol='n = int(input())\nbest = None\nfor i in range(n):\n    x, y = map(int, input().split())\n    if best is None or x * x + y * y < best[0] ** 2 + best[1] ** 2:\n        best = (x, y)\nprint(best)',
      hint='Porównuj x*x + y*y – pierwiastek nie jest potrzebny.'))
add('domyslne',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''def f(a, b=5):
    return a + b

print(f(1))''', opts=['6', '1', '5', 'Błąd'], a=0, out=True, why='b przyjmuje wartość domyślną 5.'),
 dict(t='quiz', l=1, q='Co wypisze program?', code='''def f(x="Kapi"):
    print(x)

f()
f("Bobo")''', opts=['Kapi\nBobo', 'Bobo\nBobo', 'Kapi\nKapi', 'Bobo\nKapi'], a=0, out=True, why='Bez argumentu używana jest wartość domyślna.'),
 dict(t='code', l=3, q='Napisz funkcję <code>kolumna(n, szer=3, znak=" ")</code> zwracającą liczby 1..n sklejone w jeden tekst, każda wyrównana do prawej na <code>szer</code> znakach i dopełniona znakiem <code>znak</code>.<br><code>kolumna(3)</code> → <code>"  1  2  3"</code>, <code>kolumna(3, 2, "0")</code> → <code>"010203"</code>',
      start='def kolumna(n, szer=3, znak=" "):\n    \n', tests=[], check="assert kolumna(3) == '  1  2  3'\nassert kolumna(3, 2, '0') == '010203'\nassert kolumna(1, 1) == '1'",
      sol='def kolumna(n, szer=3, znak=" "):\n    return "".join(str(i).rjust(szer, znak) for i in range(1, n + 1))', hint='str(i).rjust(szer, znak)'))
add('zasieg',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''x = 10
def pokaz():
    print(x)
pokaz()''', opts=['10', 'Błąd', 'None', 'x'], a=0, out=True, why='Funkcja może odczytać zmienną globalną.'),
 dict(t='quiz', l=1, q='Gdzie można używać zmiennej utworzonej wewnątrz funkcji?', opts=['Tylko w tej funkcji', 'W całym programie', 'W każdej funkcji', 'Nigdzie'], a=0,
      why='Zmienna lokalna istnieje tylko podczas działania funkcji.'),
 dict(t='quiz', l=2, q='Co wypisze program?', code='''def f(n):
    n = n + 1
    return n

n = 5
f(n)
print(n)''', opts=['5', '6', 'Błąd', 'None'], a=0, out=True, why='Funkcja zmienia swoją lokalną kopię n, a wynik return nie został zapisany.'))
add('moduly',
 dict(t='code', l=3, q='Wczytaj promień r (float). Wypisz obwód i pole koła (użyj <code>math.pi</code>) zaokrąglone w górę (<code>math.ceil</code>): <code>obwód: X, pole: Y</code>.',
      start='import math\nr = float(input())\n', tests=[dict(i='1', o='obwód: 7, pole: 4'), dict(i='2.5', o='obwód: 16, pole: 20')],
      sol='import math\nr = float(input())\nprint(f"obwód: {math.ceil(2 * math.pi * r)}, pole: {math.ceil(math.pi * r * r)}")', hint='math.ceil(2 * math.pi * r)'))
add('try',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''try:
    print("A")
except:
    print("B")''', opts=['A', 'B', 'A\nB', 'nic'], a=0, out=True, why='Błąd nie wystąpił, więc except się nie wykonuje.'))
add('pliki',
 dict(t='code', l=3, q='Plik <code>dane.txt</code> zawiera liczby oddzielone spacjami w kilku liniach. Zapisz do pliku <code>sumy.txt</code> sumę każdej linii (jedna w linii) i wypisz zawartość <code>sumy.txt</code>.',
      setup="open('dane.txt','w').write('1 2 3\\n10 20\\n5\\n')", start='', tests=[dict(i='', o='6\n30\n5')],
      check="assert open('sumy.txt').read().split() == ['6', '30', '5'], 'Sprawdź plik sumy.txt'",
      sol='with open("dane.txt") as f, open("sumy.txt", "w") as g:\n    for l in f:\n        g.write(str(sum(int(x) for x in l.split())) + "\\n")\nprint(open("sumy.txt").read().strip())',
      hint='Czytaj linia po linii, zapisuj sumę do drugiego pliku.'))
add('suma',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''t = [5, 1, 8]
m = t[0]
for x in t:
    if x < m:
        m = x
print(m)''', opts=['1', '5', '8', '0'], a=0, out=True, why='To szukanie minimum.'),
 dict(t='fill', l=1, q='Uzupełnij sumowanie', code='''s = 0
for x in [1, 2, 3]:
    s ___ x
print(s)''', ans=[['+=']], expect='6', why='s += x dodaje x do sumy.'),
 dict(t='code', l=3, q='Wczytaj oceny (1–6) w jednej linii. Wypisz <code>średnia: X.XX, najczęstsza: Y</code> (przy remisie – wyższa ocena). Bez sum() i count().',
      start='t = [int(x) for x in input().split()]\n', tests=[dict(i='5 4 5 3 6 4', o='średnia: 4.50, najczęstsza: 5'), dict(i='2', o='średnia: 2.00, najczęstsza: 2')],
      check="assert 'sum(' not in __src and 'count(' not in __src, 'Bez sum() i count()'",
      sol='t = [int(x) for x in input().split()]\ns = 0\nile = [0] * 7\nfor x in t:\n    s += x\n    ile[x] += 1\nnaj = 1\nfor o in range(1, 7):\n    if ile[o] >= ile[naj]:\n        naj = o\nprint(f"średnia: {s / len(t):.2f}, najczęstsza: {naj}")',
      hint='Lista liczników ile[ocena] i pętla po ocenach 1–6.'))
add('szukanie',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''t = ["Bobo", "Kapi", "Lulu"]
print(t.index("Kapi"))''', opts=['1', '2', '0', 'Kapi'], a=0, out=True, why='index zwraca pozycję pierwszego wystąpienia.'),
 dict(t='quiz', l=1, q='Co wypisze program?', code='print("Kapi" in ["kapi", "Bobo"])', opts=['False', 'True', '1', 'Błąd'], a=0, out=True,
      why='Wielkość liter ma znaczenie – "Kapi" ≠ "kapi".'),
 dict(t='code', l=3, q='Wczytaj liczby. Wypisz indeksy <b>wszystkich</b> wystąpień największej liczby, oddzielone spacją (bez max i index).',
      start='t = [int(x) for x in input().split()]\n', tests=[dict(i='3 9 2 9', o='1 3'), dict(i='5', o='0')], check="assert 'max(' not in __src and '.index' not in __src",
      sol='t = [int(x) for x in input().split()]\nm = t[0]\nfor x in t:\n    if x > m:\n        m = x\nprint(*[i for i in range(len(t)) if t[i] == m])', hint='Najpierw znajdź maksimum, potem zbierz jego indeksy.'))
add('babel',
 dict(t='quiz', l=1, q='Co robi linia <code>t[j], t[j + 1] = t[j + 1], t[j]</code>?', opts=['Zamienia sąsiednie elementy miejscami', 'Usuwa element', 'Sortuje całą listę', 'Kopiuje listę'], a=0,
      why='To zamiana dwóch wartości w jednym kroku.'),
 dict(t='quiz', l=1, q='Lista <code>[1, 2, 3]</code> jest już posortowana. Ile zamian wykona sortowanie bąbelkowe?', opts=['0', '3', '1', '2'], a=0,
      why='Żadna para sąsiadów nie jest w złej kolejności.'))
add('rekur',
 dict(t='quiz', l=1, q='Co wypisze program?', code='''def f(n):
    if n == 0:
        return 0
    return 1 + f(n - 1)

print(f(3))''', opts=['3', '0', '6', '4'], a=0, out=True, why='Każde wywołanie dodaje 1: f(3) = 1 + 1 + 1 + 0.'))
