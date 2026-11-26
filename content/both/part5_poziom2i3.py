# KapiPasta - Python – DWUJĘZYCZNE zadania poziomu 2 i 3 (po 3 + 3 w każdej lekcji).
# Bilingual tasks: every text field may be a tuple ('polski', 'English').
# Testy z o='@' – oczekiwany wynik jest liczony z rozwiązania wzorcowego (osobno dla PL i EN).
# Po zmianach uruchom: python3 tools/build.py

T2 = ('Co wypisze program?', 'What will the program print?')
BUGQ = ('Program zgłasza błąd. Kliknij winną linię.', 'The program raises an error. Click the buggy line.')
ERRQ = ('Jaki błąd zgłosi kod?', 'Which error will this code raise?')
ERR = ('Błąd', 'Error')


def Q(l, code, opts, why, q=T2, inp=None):
    d = dict(t='quiz', l=l, q=q, code=code, opts=opts, a=0, out=True, why=why)
    if inp: d['inp'] = inp
    return d


def QN(l, q, opts, why):
    return dict(t='quiz', l=l, q=q, opts=opts, a=0, why=why)


def QE(l, code, opts, why):
    return dict(t='quiz', l=l, q=ERRQ, code=code, opts=opts, a=0, err=True, why=why)


def F(l, q, code, ans, why, expect=None, inp=None):
    d = dict(t='fill', l=l, q=q, code=code, ans=ans, why=why)
    if expect is not None: d['expect'] = expect
    if inp: d['inp'] = inp
    return d


def B(l, code, line, fix, why, q=BUGQ, noerr=False, cause=False, inp=None):
    d = dict(t='bug', l=l, q=q, code=code, line=line, fix=fix, why=why)
    if noerr: d['noerr'] = True
    if cause: d['cause'] = True
    if inp: d['inp'] = inp
    return d


def C(l, q, start, inputs, sol, hint, check=None, setup=None):
    d = dict(t='code', l=l, q=q, start=start, tests=[dict(i=i, o='@') for i in inputs], sol=sol, hint=hint)
    if check: d['check'] = check
    if setup: d['setup'] = setup
    return d


EXTRA2 = {}

EXTRA2['print'] = [
 Q(2, 'print(1, 2, 3, sep="")', ['123', '1 2 3', '6', '1,2,3'], ('sep="" usuwa odstępy między wartościami.', 'sep="" removes the spaces between values.')),
 Q(2, 'print("Ka" + "pi")', ['Kapi', 'Ka pi', 'Ka+pi', ERR], ('+ skleja teksty bez spacji.', '+ joins strings without a space.')),
 B(2, 'print("A")\nprint("B", sep=-)', 1, 'print("B", sep="-")', ('Wartość sep to tekst – musi być w cudzysłowie.', 'The sep value is text – it must be in quotes.')),
 Q(3, 'print("a", "b", sep="", end="!")\nprint()', ['ab!', 'a b!', 'ab\n!', 'ab'], ('sep="" skleja litery, end="!" kończy linię wykrzyknikiem, a pusty print() przechodzi do nowej linii.', 'sep="" glues the letters, end="!" ends the line with “!”, and an empty print() moves to a new line.')),
 Q(3, 'print(print("x"))', ['x\nNone', 'x\nx', 'None', 'x'], ('Wewnętrzny print wypisuje x i zwraca None – to None wypisuje zewnętrzny print.', 'The inner print prints x and returns None – which the outer print prints.')),
 C(3, ('Wczytaj n i wypisz n gwiazdek oddzielonych spacjami – <b>jednym</b> print, bez pętli.<br>3 → <code>* * *</code>', 'Read n and print n stars separated by spaces – with <b>one</b> print, no loop.<br>3 → <code>* * *</code>'),
   'n = int(input())\n', ['3', '1', '6'], 'n = int(input())\nprint(*["*"] * n)', ('["*"] * n tworzy listę n gwiazdek, a * ją rozpakowuje.', '["*"] * n makes a list of n stars, and * unpacks it.'),
   check=("assert __src.count('print') == 1 and 'for' not in __src and 'while' not in __src, 'Jeden print, bez pętli'", "assert __src.count('print') == 1 and 'for' not in __src and 'while' not in __src, 'One print, no loop'")),
]
EXTRA2['fstr'] = [
 Q(2, 'x = 3.14159\nprint(f"{x:.1f}")', ['3.1', '3.14', '3', '3.2'], ('.1f – jedno miejsce po przecinku.', '.1f – one decimal place.')),
 Q(2, 'n = 42\nprint(f"[{n:5}]")', ['[   42]', '[42   ]', '[42]', '[00042]'], ('Liczby są domyślnie wyrównane do prawej w polu o szerokości 5.', 'Numbers are right-aligned by default in a field 5 wide.')),
 F(2, ('Uzupełnij format, aby wypisało <code>007</code>', 'Fill in the format so it prints <code>007</code>'), 'n = 7\nprint(f"{n:___}")', [['03', '03d']], ('03 – szerokość 3, dopełnienie zerami.', '03 – width 3, padded with zeros.'), expect='007'),
 Q(3, 'print(f"{\'ab\':*^6}")', ['**ab**', 'ab****', '****ab', '*ab*'], ('*^6 – wyśrodkuj w polu 6 znaków i dopełnij gwiazdkami.', '*^6 – centre in a 6-character field and pad with stars.')),
 Q(3, 'x = 1234567\nprint(f"{x:,}")', ['1,234,567', '1234567', '1.234.567', '1 234 567'], ('Format , dodaje separator tysięcy.', 'The , format adds a thousands separator.')),
 C(3, ('Wczytaj n i wypisz tabelę: w każdym wierszu i, i² i i³, wyrównane do prawej na 2, 5 i 6 znaków (<code>f"{i:>2}{i**2:>5}{i**3:>6}"</code>).', 'Read n and print a table: in each row i, i² and i³, right-aligned in 2, 5 and 6 characters (<code>f"{i:>2}{i**2:>5}{i**3:>6}"</code>).'),
   'n = int(input())\n', ['3', '10'], 'n = int(input())\nfor i in range(1, n + 1):\n    print(f"{i:>2}{i ** 2:>5}{i ** 3:>6}")', ('Pętla od 1 do n i jeden f-string w każdym wierszu.', 'A loop from 1 to n and one f-string per row.')),
]
EXTRA2['zmienne'] = [
 Q(2, 'a = b = 4\nb = 5\nprint(a, b)', ['4 5', '5 5', '4 4', ERR], ('a = b = 4 przypisuje 4 obu zmiennym; potem zmieniamy tylko b.', 'a = b = 4 assigns 4 to both; then only b changes.')),
 Q(2, 'x = "7"\nprint(x + x, int(x) + int(x))', ['77 14', '14 14', '77 77', ERR], ('Teksty się sklejają, liczby dodają.', 'Strings are joined, numbers are added.')),
 B(2, '2x = 5\nprint(2x)', 0, 'x2 = 5', ('Nazwa zmiennej nie może zaczynać się cyfrą.', 'A variable name cannot start with a digit.')),
 Q(3, 'x = 5\nx = x * 2 + x\nprint(x)', ['15', '20', '10', '25'], ('Prawa strona jest liczona ze starym x = 5: 10 + 5.', 'The right side uses the old x = 5: 10 + 5.')),
 Q(3, 'print(type(True + 1).__name__, True + True)', ['int 2', 'bool 2', 'int True', ERR], ('True zachowuje się jak 1 w działaniach.', 'True behaves like 1 in arithmetic.')),
 C(3, ('Wczytaj temperaturę w °C (float). Wypisz ją w kelwinach (2 miejsca) i w °F (1 miejsce): <code>K, F</code>, np. <code>309.75 K, 97.9 F</code>.', 'Read a temperature in °C (float). Print it in kelvins (2 places) and °F (1 place): e.g. <code>309.75 K, 97.9 F</code>.'),
   'c = float(input())\n', ['36.6', '-40', '0'], 'c = float(input())\nprint(f"{c + 273.15:.2f} K, {c * 9 / 5 + 32:.1f} F")', ('K = C + 273.15, F = C · 9/5 + 32', 'K = C + 273.15, F = C · 9/5 + 32')),
]
EXTRA2['input'] = [
 Q(2, 'a = input()\nb = int(input())\nprint(a * b)', ['3333', '12', '34', ERR], ('a to tekst "3", a tekst razy 4 to powtórzenie.', 'a is the text "3", and text times 4 is repetition.'), q=('Użytkownik wpisuje 3, potem 4. Co wypisze program?', 'The user types 3, then 4. What will the program print?'), inp='3\n4'),
 F(2, ('Uzupełnij, aby dla danych 5 wynik był <code>2.5</code>', 'Fill in so that for input 5 the result is <code>2.5</code>'), 'x = ___(input())\nprint(x / 2)', [['float', 'int']], ('Trzeba zamienić tekst na liczbę.', 'The text must be turned into a number.'), expect='2.5', inp='5'),
 C(2, ('Wczytaj imię i wypisz je 3 razy, oddzielone myślnikiem: <code>Kapi-Kapi-Kapi</code>.', 'Read a name and print it 3 times separated by dashes: <code>Kapi-Kapi-Kapi</code>.'),
   'name = input()\n', ['Kapi', 'Ola'], 'name = input()\nprint(name, name, name, sep="-")', ('print(..., sep="-") albo "-".join([...])', 'print(..., sep="-") or "-".join([...])')),
 Q(3, 'a, b = input().split()\nprint(a + b, int(a) * int(b))', ['23 6', '5 6', '23 23', ERR], ('split() daje dwa teksty "2" i "3".', 'split() gives two strings "2" and "3".'), q=('Użytkownik wpisuje <code>2 3</code>. Co wypisze program?', 'The user types <code>2 3</code>. What will the program print?'), inp='2 3'),
 C(3, ('Wczytaj liczbę sekund od północy i wypisz godzinę <code>HH:MM:SS</code>.<br>3661 → <code>01:01:01</code>', 'Read the number of seconds since midnight and print the time <code>HH:MM:SS</code>.<br>3661 → <code>01:01:01</code>'),
   's = int(input())\n', ['3661', '0', '86399'], 's = int(input())\nprint(f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}")', ('Godziny s // 3600, minuty s % 3600 // 60, sekundy s % 60.', 'Hours s // 3600, minutes s % 3600 // 60, seconds s % 60.')),
 C(3, ('Wczytaj wagę w kg zapisaną z przecinkiem (np. <code>2,5</code>) i wypisz ją w gramach jako liczbę całkowitą.', 'Read a weight in kg written with a decimal comma (e.g. <code>2,5</code>) and print it in grams as a whole number.'),
   '', ['2,5', '0,125', '3'], 'print(round(float(input().replace(",", ".")) * 1000))', ('Zamień przecinek na kropkę: replace(",", "."), potem float.', 'Replace the comma with a dot: replace(",", "."), then float.')),
]
EXTRA2['oper'] = [
 Q(2, 'print(10 - 2 * 3 ** 2)', ['-8', '72', '64', '4'], ('Najpierw potęga (9), potem mnożenie (18), na końcu odejmowanie.', 'Power first (9), then multiplication (18), subtraction last.')),
 Q(2, 'print(17 // 5 * 5 + 17 % 5)', ['17', '15', '2', '20'], ('(a // b) · b + a % b zawsze daje a.', '(a // b) · b + a % b always gives a.')),
 B(2, 'x = 10\ny = 0\nprint(x // y)', 2, 'if y != 0: print(x // y)', ('Dzielenie całkowite przez zero też zgłasza ZeroDivisionError.', 'Floor division by zero also raises ZeroDivisionError.')),
 Q(3, 'print(round(2.5), round(3.5))', ['2 4', '3 4', '2 3', '3 3'], ('round zaokrągla „do parzystej”, gdy liczba jest dokładnie w połowie.', 'round rounds “to even” when a number is exactly halfway.')),
 Q(3, 'print(0.1 + 0.2 == 0.3)', ['False', 'True', '0.3', ERR], ('Liczby float są przybliżone: 0.1 + 0.2 = 0.30000000000000004.', 'Floats are approximate: 0.1 + 0.2 = 0.30000000000000004.')),
 C(3, ('Wczytaj liczbę całkowitą (może być ujemna) i wypisz, ile ma cyfr – bez zamiany na tekst. Liczba 0 ma 1 cyfrę.', 'Read a whole number (it may be negative) and print how many digits it has – without converting to text. 0 has 1 digit.'),
   'n = int(input())\n', ['12345', '-907', '0'], 'n = abs(int(input()))\nk = 1\nwhile n >= 10:\n    n //= 10\n    k += 1\nprint(k)', ('Dziel przez 10, dopóki liczba ma więcej niż jedną cyfrę. abs() usuwa minus.', 'Divide by 10 while the number has more than one digit. abs() removes the minus.'),
   check=("assert 'str(' not in __src and 'len(' not in __src, 'Bez str i len!'", "assert 'str(' not in __src and 'len(' not in __src, 'No str or len!'")),
]
EXTRA2['logika'] = [
 Q(2, 'print(3 < 5 < 4)', ['False', 'True', ERR, '4'], ('To skrót od 3 < 5 and 5 < 4.', 'It is short for 3 < 5 and 5 < 4.')),
 Q(2, 'print("abc" < "abd", "Z" < "a")', ['True True', 'True False', 'False True', 'False False'], ('Teksty porównuje się znak po znaku; wielkie litery są „przed” małymi.', 'Strings are compared character by character; capitals come “before” lowercase.')),
 F(2, ('Uzupełnij operator, aby wypisało <code>True</code>', 'Fill in the operator so it prints <code>True</code>'), 'x = 15\nprint(x % 3 == 0 ___ x % 5 == 0)', [['and', 'or']], ('15 dzieli się przez 3 i przez 5.', '15 is divisible by both 3 and 5.'), expect='True'),
 Q(3, 'print(not 0, not "", not "0")', ['True True False', 'True True True', 'False False False', 'True False False'], ('0 i pusty tekst są „fałszywe”, ale "0" to niepusty tekst.', '0 and empty text are “falsy”, but "0" is non-empty text.')),
 Q(3, 'x = None\nprint(x is None, x == 0)', ['True False', 'True True', 'False False', ERR], ('None to osobna wartość – nie jest równa 0.', 'None is a separate value – it is not equal to 0.')),
 C(3, ('Wczytaj rok i miesiąc (dwie linie). Wypisz liczbę dni w tym miesiącu (uwzględnij lata przestępne).', 'Read a year and a month (two lines). Print the number of days in that month (include leap years).'),
   '', ['2024\n2', '2023\n2', '2026\n11', '1900\n2', '2000\n2'],
   'r = int(input())\nm = int(input())\nleap = r % 4 == 0 and r % 100 != 0 or r % 400 == 0\nd = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\nprint(d[m - 1])',
   ('Lista dni miesięcy i warunek roku przestępnego dla lutego.', 'A list of month lengths and the leap-year condition for February.')),
]
EXTRA2['if'] = [
 Q(2, 'x = 5\nif x > 3:\n    print("A")\nif x > 4:\n    print("B")\nelse:\n    print("C")', ['A\nB', 'A', 'B', 'A\nC'], ('To dwa niezależne if-y – oba warunki są prawdziwe.', 'These are two independent ifs – both conditions are true.')),
 B(2, 'if True:\n    print("a")\n  print("b")', 2, '    print("b")', ('Wcięcia w jednym bloku muszą być takie same.', 'Indentation in one block must be the same.')),
 C(2, ('Wczytaj liczbę. Wypisz <code>dodatnia</code>, <code>ujemna</code> lub <code>zero</code>.', 'Read a number. Print <code>positive</code>, <code>negative</code> or <code>zero</code>.'),
   'n = int(input())\n', ['5', '-3', '0'], ('n = int(input())\nif n > 0:\n    print("dodatnia")\nelif n < 0:\n    print("ujemna")\nelse:\n    print("zero")', 'n = int(input())\nif n > 0:\n    print("positive")\nelif n < 0:\n    print("negative")\nelse:\n    print("zero")'),
   ('if / elif / else', 'if / elif / else')),
 Q(3, 'x = 7\nprint("A" if x % 2 == 0 else "B")', ['B', 'A', 'AB', ERR], ('Wyrażenie warunkowe: wartość1 if warunek else wartość2.', 'Conditional expression: value1 if condition else value2.')),
 C(3, ('Kalkulator: wczytaj a, operator (+ - * /) i b w osobnych liniach (a, b całkowite). Wypisz wynik, a przy dzieleniu przez zero – <code>błąd</code>.', 'Calculator: read a, an operator (+ - * /) and b on separate lines (a, b whole numbers). Print the result, and for division by zero – <code>error</code>.'),
   '', ['6\n*\n7', '1\n/\n0', '7\n/\n2', '3\n-\n10', '2\n+\n2'],
   ('a = int(input())\nop = input()\nb = int(input())\nif op == "+":\n    print(a + b)\nelif op == "-":\n    print(a - b)\nelif op == "*":\n    print(a * b)\nelif b == 0:\n    print("błąd")\nelse:\n    print(a / b)',
    'a = int(input())\nop = input()\nb = int(input())\nif op == "+":\n    print(a + b)\nelif op == "-":\n    print(a - b)\nelif op == "*":\n    print(a * b)\nelif b == 0:\n    print("error")\nelse:\n    print(a / b)'),
   ('Sprawdzaj operator w if/elif; przy / najpierw sprawdź b == 0.', 'Check the operator with if/elif; for / check b == 0 first.')),
 C(3, ('Wczytaj trzy boki. Wypisz <code>równoboczny</code>, <code>równoramienny</code>, <code>różnoboczny</code> albo <code>brak</code>, jeśli trójkąta nie da się zbudować.', 'Read three sides. Print <code>equilateral</code>, <code>isosceles</code>, <code>scalene</code> or <code>none</code> if no triangle can be built.'),
   '', ['3\n3\n3', '3\n3\n5', '3\n4\n5', '1\n2\n3'],
   ('a = int(input())\nb = int(input())\nc = int(input())\nif a + b <= c or a + c <= b or b + c <= a:\n    print("brak")\nelif a == b == c:\n    print("równoboczny")\nelif a == b or b == c or a == c:\n    print("równoramienny")\nelse:\n    print("różnoboczny")',
    'a = int(input())\nb = int(input())\nc = int(input())\nif a + b <= c or a + c <= b or b + c <= a:\n    print("none")\nelif a == b == c:\n    print("equilateral")\nelif a == b or b == c or a == c:\n    print("isosceles")\nelse:\n    print("scalene")'),
   ('Najpierw sprawdź, czy trójkąt istnieje.', 'First check whether the triangle exists.')),
]
EXTRA2['for'] = [
 Q(2, 's = 0\nfor i in range(5):\n    s += i\nprint(s)', ['10', '15', '5', '4'], ('0 + 1 + 2 + 3 + 4 = 10', '0 + 1 + 2 + 3 + 4 = 10')),
 Q(2, 'for i in range(3, 0, -1):\n    print(i, end="")\nprint()', ['321', '3210', '123', '3 2 1'], ('Od 3 w dół, bez 0.', 'From 3 down, without 0.')),
 B(2, 'for i in range(5)\n    print(i)', 0, 'for i in range(5):', ('Po for brakuje dwukropka.', 'The colon after for is missing.')),
 Q(3, 'for i in range(2, 20, 5):\n    pass\nprint(i)', ['17', '20', '22', '15'], ('i przyjmuje 2, 7, 12, 17 – po pętli zostaje ostatnia wartość.', 'i takes 2, 7, 12, 17 – the last value stays after the loop.')),
 C(3, ('Wczytaj n i wypisz sumę cyfr wszystkich liczb od 1 do n.<br>12 → <code>51</code>', 'Read n and print the sum of the digits of all numbers from 1 to n.<br>12 → <code>51</code>'),
   'n = int(input())\n', ['12', '9', '100'], 'n = int(input())\ns = 0\nfor i in range(1, n + 1):\n    for c in str(i):\n        s += int(c)\nprint(s)', ('Dla każdej liczby zsumuj jej cyfry.', 'For each number add up its digits.')),
 C(3, ('Wczytaj n i wypisz n wierszy: w wierszu i liczby od 1 do i oddzielone spacją.', 'Read n and print n rows: row i holds the numbers 1 to i separated by spaces.'),
   'n = int(input())\n', ['4', '1'], 'n = int(input())\nfor i in range(1, n + 1):\n    print(*range(1, i + 1))', ('print(*range(1, i + 1))', 'print(*range(1, i + 1))')),
]
EXTRA2['while'] = [
 Q(2, 'n = 100\nk = 0\nwhile n > 1:\n    n //= 10\n    k += 1\nprint(k)', ['2', '3', '1', '100'], ('100 → 10 → 1: dwa kroki.', '100 → 10 → 1: two steps.')),
 F(2, ('Uzupełnij warunek, aby wypisało liczby 1–5', 'Fill in the condition to print the numbers 1–5'), 'i = 1\nwhile i ___ 5:\n    print(i, end=" ")\n    i += 1', [['<=']], ('<= 5 obejmuje też 5.', '<= 5 includes 5.'), expect='1 2 3 4 5'),
 C(2, ('Wczytuj liczby, aż pojawi się pusta linia. Wypisz ich sumę.', 'Keep reading numbers until an empty line appears. Print their sum.'),
   '', ['3\n4\n', '10\n-2\n5\n'], 's = 0\nwhile True:\n    x = input()\n    if x == "":\n        break\n    s += int(x)\nprint(s)', ('while True + break, gdy x == "".', 'while True + break when x == "".')),
 Q(3, 'x = 5\nwhile x:\n    x -= 2\n    if x < 0:\n        break\nprint(x)', ['-1', '0', '1', '3'], ('5 → 3 → 1 → -1 i break.', '5 → 3 → 1 → -1 and break.')),
 C(3, ('Wczytaj n > 0 i wypisz liczbę o odwróconych cyfrach – bez zamiany na tekst.<br>1230 → <code>321</code>', 'Read n > 0 and print the number with its digits reversed – without converting to text.<br>1230 → <code>321</code>'),
   'n = int(input())\n', ['1230', '5', '9081'], 'n = int(input())\nw = 0\nwhile n > 0:\n    w = w * 10 + n % 10\n    n //= 10\nprint(w)', ('w = w * 10 + n % 10, n //= 10', 'w = w * 10 + n % 10, n //= 10'),
   check=("assert 'str(' not in __src and '[::-1]' not in __src, 'Bez zamiany na tekst!'", "assert 'str(' not in __src and '[::-1]' not in __src, 'No converting to text!'")),
 C(3, ('Wczytaj n ≥ 1 i wypisz najmniejszą potęgę dwójki, która jest ≥ n.', 'Read n ≥ 1 and print the smallest power of two that is ≥ n.'),
   'n = int(input())\n', ['5', '1', '16', '1000'], 'n = int(input())\np = 1\nwhile p < n:\n    p *= 2\nprint(p)', ('Zacznij od p = 1 i podwajaj.', 'Start with p = 1 and keep doubling.')),
]
EXTRA2['zagn'] = [
 Q(2, 'for i in range(3):\n    for j in range(3):\n        if i == j:\n            print(i, end="")', ['012', '000111222', '0', '123'], ('Wypisujemy tylko „przekątną”, gdy i == j.', 'Only the “diagonal” is printed, when i == j.')),
 Q(2, 'n = 0\nfor i in range(4):\n    for j in range(i, 4):\n        n += 1\nprint(n)', ['10', '16', '6', '4'], ('4 + 3 + 2 + 1 = 10', '4 + 3 + 2 + 1 = 10')),
 B(2, 'for i in range(3):\n    for j in range(4):\n        print("#", end="")\nprint()', 3, ('    print()  (wcięte w pierwszej pętli)', '    print()  (indented inside the first loop)'), ('print() kończący wiersz musi być wewnątrz zewnętrznej pętli – inaczej wszystko trafia do jednej linii.', 'The print() ending a row must be inside the outer loop – otherwise everything goes on one line.'),
   q=('Program miał narysować prostokąt 3 × 4, a rysuje jedną długą linię. Kliknij linię do poprawy.', 'The program should draw a 3 × 4 rectangle, but it draws one long line. Click the line to fix.'), noerr=True),
 Q(3, 'for i in range(3):\n    for j in range(3):\n        if j == 1:\n            break\n        print(i, j)', ['0 0\n1 0\n2 0', '0 0', '0 0\n0 1', '0 0\n1 1\n2 2'], ('break przerywa tylko wewnętrzną pętlę.', 'break stops only the inner loop.')),
 C(3, ('Wczytaj n i wypisz szachownicę n × n z <code>#</code> i <code>.</code>, zaczynając od <code>#</code>.', 'Read n and print an n × n chessboard of <code>#</code> and <code>.</code>, starting with <code>#</code>.'),
   'n = int(input())\n', ['3', '4'], 'n = int(input())\nfor i in range(n):\n    print("".join("#" if (i + j) % 2 == 0 else "." for j in range(n)))', ('Pole jest #, gdy (i + j) jest parzyste.', 'A square is # when (i + j) is even.')),
 C(3, ('Wczytaj n i wypisz wszystkie trójki pitagorejskie a &lt; b &lt; c ≤ n (a² + b² = c²), każdą jako <code>a b c</code>, rosnąco według a, potem b.', 'Read n and print all Pythagorean triples a &lt; b &lt; c ≤ n (a² + b² = c²), each as <code>a b c</code>, ordered by a, then b.'),
   'n = int(input())\n', ['13', '20'], 'n = int(input())\nfor a in range(1, n + 1):\n    for b in range(a + 1, n + 1):\n        for c in range(b + 1, n + 1):\n            if a * a + b * b == c * c:\n                print(a, b, c)', ('Trzy zagnieżdżone pętle.', 'Three nested loops.')),
]
EXTRA2['slice'] = [
 Q(2, 's = "kapibara"\nprint(s[::2])', ['kpbr', 'aiaa', 'kapi', 'kpba'], ('Co drugi znak od początku.', 'Every second character from the start.')),
 Q(2, 's = "kapibara"\nprint(s[1:-1])', ['apibar', 'apibara', 'kapibar', 'pibar'], ('Bez pierwszego i ostatniego znaku.', 'Without the first and last character.')),
 F(2, ('Uzupełnij, aby wypisać <code>pyt</code>', 'Fill in to print <code>pyt</code>'), 's = "python"\nprint(s[___])', [[':3', '0:3']], ('Pierwsze trzy znaki to s[:3].', 'The first three characters are s[:3].'), expect='pyt'),
 Q(3, 's = "abcdef"\nprint(s[-2:-5:-1])', ['edc', 'cde', 'fed', 'dcb'], ('Od indeksu -2 (e) wstecz, do -5 (b) bez niego.', 'From index -2 (e) backwards, to -5 (b) excluded.')),
 Q(3, 's = "abc"\nprint(s[10:] == "")', ['True', 'False', ERR, 'None'], ('Wycinek poza zakresem nie zgłasza błędu – daje pusty tekst.', 'A slice out of range raises no error – it gives empty text.')),
 C(3, ('Wczytaj słowo i wypisz wszystkie jego przedrostki od najkrótszego, każdy w nowej linii.', 'Read a word and print all its prefixes from the shortest, each on a new line.'),
   's = input()\n', ['kot', 'a'], 's = input()\nfor i in range(1, len(s) + 1):\n    print(s[:i])', ('s[:i] dla i od 1 do len(s).', 's[:i] for i from 1 to len(s).')),
]
EXTRA2['metody'] = [
 Q(2, 'print("kapibara".find("b"), "kapibara".find("z"))', ['4 -1', '4 0', '5 -1', '4 None'], ('find zwraca indeks albo -1, gdy nie znajdzie.', 'find returns the index, or -1 when not found.')),
 Q(2, 'print("banana".replace("a", "o", 1))', ['bonana', 'bonono', 'banana', 'banano'], ('Trzeci argument ogranicza liczbę zamian.', 'The third argument limits the number of replacements.')),
 B(2, 's = "kapi"\ns[0] = "K"\nprint(s)', 1, 's = "K" + s[1:]', ('Tekstów nie można zmieniać – TypeError. Trzeba zbudować nowy tekst.', "Strings can't be changed – TypeError. Build a new string.")),
 Q(3, 'print("-".join("abc"))', ['a-b-c', '-abc-', 'abc', '-a-b-c-'], ('join traktuje tekst jak listę znaków.', 'join treats a string like a list of characters.')),
 Q(3, 'print("  x  ".strip() + "|" + "xxhixx".strip("x"))', ['x|hi', 'x|xxhixx', '  x  |hi', 'x|hixx'], ('strip("x") usuwa znaki x z obu końców.', 'strip("x") removes x characters from both ends.')),
 C(3, ('Wczytaj zdanie i wypisz słowa od najdłuższego; przy równej długości – alfabetycznie. Oddziel spacją.', 'Read a sentence and print the words from the longest; with equal length – alphabetically. Separate with spaces.'),
   's = input()\n', [('ala ma kota i psa', 'a cat is on my bed'), 'bb a ccc aa'], 's = input()\nprint(" ".join(sorted(s.split(), key=lambda w: (-len(w), w))))', ('sorted(..., key=lambda w: (-len(w), w))', 'sorted(..., key=lambda w: (-len(w), w))')),
]
EXTRA2['znaki'] = [
 Q(2, 'n = 0\nfor z in "a1b2c3":\n    if z.isdigit():\n        n += int(z)\nprint(n)', ['6', '3', '123', '0'], ('Sumujemy cyfry 1, 2, 3.', 'We add the digits 1, 2, 3.')),
 Q(2, 'w = ""\nfor z in "kapi":\n    w += z * 2\nprint(w)', ['kkaappii', 'kapikapi', 'kapi', 'kkaapp'], ('Każda litera zostaje podwojona.', 'Each letter is doubled.')),
 F(2, ('Uzupełnij, aby wypisać samogłoski słowa', 'Fill in to print the vowels of the word'), 's = "Kapi"\nfor z in s:\n    if z ___ "aeiou":\n        print(z)', [['in']], ('in sprawdza, czy znak jest w tekście.', 'in checks whether a character is in a string.'), expect='a\ni'),
 Q(3, 's = "abc"\nprint([ord(z) - ord("a") for z in s])', ['[0, 1, 2]', '[1, 2, 3]', '[97, 98, 99]', "['a', 'b', 'c']"], ('ord daje kod znaku; różnica od "a" to pozycja w alfabecie.', 'ord gives the character code; the difference from "a" is the alphabet position.')),
 C(3, ('Wczytaj słowo i wypisz <code>True</code>, jeśli wszystkie jego litery są różne (bez zbiorów), inaczej <code>False</code>.', 'Read a word and print <code>True</code> if all its letters are different (without sets), otherwise <code>False</code>.'),
   's = input()\n', ['kapi', 'kapibara', 'x'], 's = input()\nok = True\nfor i in range(len(s)):\n    if s[i] in s[i + 1:]:\n        ok = False\nprint(ok)', ('Sprawdź, czy litera pojawia się dalej w słowie.', 'Check whether a letter appears later in the word.'),
   check=("assert 'set(' not in __src, 'Bez set!'", "assert 'set(' not in __src, 'No set!'")),
 C(3, ('Wczytaj tekst. Zamień każdą cyfrę na <code>#</code> i wypisz wynik, a w drugiej linii liczbę zamian.', 'Read some text. Replace every digit with <code>#</code> and print the result, and on the second line the number of replacements.'),
   's = input()\n', ['pin 1234 ok', ('brak', 'none')], 's = input()\nw = ""\nn = 0\nfor z in s:\n    if z.isdigit():\n        w += "#"\n        n += 1\n    else:\n        w += z\nprint(w)\nprint(n)', ('Buduj nowy tekst znak po znaku.', 'Build a new string character by character.')),
]
EXTRA2['listy'] = [
 Q(2, 't = [1, 2, 3]\nt[1] = t[0] + t[2]\nprint(t)', ['[1, 4, 3]', '[1, 3, 3]', '[4, 2, 3]', '[1, 2, 3]'], ('t[1] = 1 + 3', 't[1] = 1 + 3')),
 Q(2, 't = [4, 5, 6]\nprint(t[::-1], len(t[1:]))', ['[6, 5, 4] 2', '[6, 5, 4] 3', '[4, 5, 6] 2', '[6, 5] 2'], ('[::-1] odwraca listę, t[1:] ma 2 elementy.', '[::-1] reverses the list, t[1:] has 2 elements.')),
 B(2, 't = [1, 2, 3]\nprint(t[1.0])', 1, 'print(t[1])', ('Indeks listy musi być liczbą całkowitą – TypeError.', 'A list index must be a whole number – TypeError.')),
 Q(3, 'a = [1, 2]\nb = a[:]\nb.append(3)\nprint(a, b)', ['[1, 2] [1, 2, 3]', '[1, 2, 3] [1, 2, 3]', '[1, 2] [1, 2]', ERR], ('a[:] tworzy kopię – zmiana b nie zmienia a.', 'a[:] makes a copy – changing b does not change a.')),
 Q(3, 't = [[0] * 2] * 2\nt[0][0] = 1\nprint(t)', ['[[1, 0], [1, 0]]', '[[1, 0], [0, 0]]', '[[1, 1], [0, 0]]', ERR], ('Pułapka! * 2 kopiuje odwołanie do tej samej listy wewnętrznej.', 'A trap! * 2 copies a reference to the same inner list.')),
 C(3, ('Wczytaj dwie posortowane listy (dwie linie) i połącz je w jedną posortowaną – bez sort/sorted. Wypisz oddzielone spacją.', 'Read two sorted lists (two lines) and merge them into one sorted list – without sort/sorted. Print separated by spaces.'),
   'a = [int(x) for x in input().split()]\nb = [int(x) for x in input().split()]\n', ['1 4 9\n2 3 10', '5\n1 2 3'],
   'a = [int(x) for x in input().split()]\nb = [int(x) for x in input().split()]\ni = j = 0\nw = []\nwhile i < len(a) and j < len(b):\n    if a[i] <= b[j]:\n        w.append(a[i])\n        i += 1\n    else:\n        w.append(b[j])\n        j += 1\nw += a[i:] + b[j:]\nprint(*w)',
   ('Dwa wskaźniki i, j – dokładaj mniejszy element.', 'Two pointers i, j – always add the smaller element.'),
   check=("assert 'sort' not in __src, 'Bez sort!'", "assert 'sort' not in __src, 'No sort!'")),
]
EXTRA2['metodylist'] = [
 Q(2, 't = [3, 1, 2]\nt.append(t.pop(0))\nprint(t)', ['[1, 2, 3]', '[3, 1, 2]', '[1, 2]', '[2, 3, 1]'], ('pop(0) wyjmuje 3, append dokłada je na koniec.', 'pop(0) takes out 3, append puts it at the end.')),
 Q(2, 't = [1, 2, 3, 2]\nprint(t.count(2), t.index(2))', ['2 1', '2 3', '1 1', '2 2'], ('count liczy wystąpienia, index zwraca pierwszą pozycję.', 'count counts occurrences, index returns the first position.')),
 F(2, ('Uzupełnij, aby posortować listę', 'Fill in to sort the list'), 't = [5, 2, 9]\nt.___()\nprint(t)', [['sort']], ('sort() sortuje listę w miejscu.', 'sort() sorts the list in place.'), expect='[2, 5, 9]'),
 Q(3, 't = [1, 2, 3]\nt.extend([4, 5])\nt.append([6])\nprint(len(t))', ['6', '7', '5', '3'], ('extend dodaje 2 elementy, append – jeden (listę).', 'extend adds 2 elements, append – one (a list).')),
 Q(3, 't = [3, 1, 2]\nt.reverse()\nprint(t, sorted(t, reverse=True))', ['[2, 1, 3] [3, 2, 1]', '[1, 2, 3] [3, 2, 1]', '[2, 1, 3] [1, 2, 3]', '[3, 2, 1] [3, 2, 1]'], ('reverse() tylko odwraca kolejność, nie sortuje.', 'reverse() only flips the order, it does not sort.')),
 C(3, ('Stos: wczytuj polecenia <code>push X</code> i <code>pop</code>, aż pojawi się <code>end</code>. Na końcu wypisz stos jako listę liczb.', 'Stack: read commands <code>push X</code> and <code>pop</code> until <code>end</code> appears. At the end print the stack as a list of numbers.'),
   '', ['push 1\npush 2\npop\npush 5\nend', 'pop\npush 7\nend'],
   's = []\nwhile True:\n    c = input().split()\n    if c[0] == "end":\n        break\n    if c[0] == "push":\n        s.append(int(c[1]))\n    elif s:\n        s.pop()\nprint(s)', ('append = push, pop() = pop. Uważaj na pop z pustego stosu.', 'append = push, pop() = pop. Watch out for pop on an empty stack.')),
]
EXTRA2['krotki'] = [
 Q(2, 't = (1, 2) + (3,)\nprint(t)', ['(1, 2, 3)', '(1, 2, (3,))', '(4, 2)', ERR], ('Krotki można łączyć znakiem +. (3,) to krotka jednoelementowa.', 'Tuples can be joined with +. (3,) is a one-element tuple.')),
 Q(2, 's = set("kapibara")\nprint(len(s))', ['6', '8', '4', '5'], ('Różne litery: k, a, p, i, b, r.', 'Distinct letters: k, a, p, i, b, r.')),
 B(2, 's = {1, 2, 3}\nprint(s[0])', 1, 'print(list(s)[0])', ('Zbiór nie ma indeksów – TypeError.', 'A set has no indexes – TypeError.')),
 Q(3, 'a, *b = (1, 2, 3)\nprint(a, b)', ['1 [2, 3]', '1 (2, 3)', '1 2', ERR], ('*b zbiera resztę elementów w listę.', '*b collects the remaining elements into a list.')),
 Q(3, 'print({1, 2} == {2, 1}, (1, 2) == (2, 1))', ['True False', 'True True', 'False False', 'False True'], ('W zbiorach kolejność nie ma znaczenia, w krotkach – ma.', 'Order does not matter in sets, but it does in tuples.')),
 C(3, ('Wczytaj słowa w jednej linii. Wypisz alfabetycznie słowa występujące więcej niż raz (każde raz), a gdy takich nie ma – <code>-</code>.', 'Read words on one line. Print, alphabetically, the words that appear more than once (each once), or <code>-</code> if there are none.'),
   'words = input().split()\n', ['b a b c a b', 'x y z'], 'words = input().split()\nseen = set()\nrep = set()\nfor w in words:\n    if w in seen:\n        rep.add(w)\n    seen.add(w)\nprint(" ".join(sorted(rep)) if rep else "-")', ('Dwa zbiory: widziane i powtórzone.', 'Two sets: seen and repeated.')),
]
EXTRA2['slowniki'] = [
 Q(2, 'd = {"a": 1, "b": 2}\nd["c"] = d["a"] + d["b"]\nprint(len(d), d["c"])', ['3 3', '2 3', '3 12', ERR], ('Dodaliśmy trzeci klucz o wartości 1 + 2.', 'We added a third key with the value 1 + 2.')),
 Q(2, 'd = {"x": 1}\nprint(d.get("y"), "x" in d)', ['None True', '0 True', 'None False', ERR], ('get bez wartości domyślnej zwraca None; in sprawdza klucze.', 'get without a default returns None; in checks keys.')),
 F(2, ('Uzupełnij, aby zsumować wartości słownika', 'Fill in to add up the dictionary values'), 'd = {"a": 1, "b": 2}\nprint(sum(d.___()))', [['values']], ('values() zwraca wartości.', 'values() returns the values.'), expect='3'),
 Q(3, 'd = {}\nfor z in "abca":\n    d[z] = d.get(z, 0) + 1\nprint(d)', ["{'a': 2, 'b': 1, 'c': 1}", "{'a': 1, 'b': 1, 'c': 1}", "{'a': 2, 'b': 1, 'c': 1, 'a': 1}", '{}'], ('Klasyczne zliczanie z get(z, 0).', 'Classic counting with get(z, 0).')),
 Q(3, 'd = {1: "a", 2: "b"}\nprint({v: k for k, v in d.items()})', ["{'a': 1, 'b': 2}", "{1: 'a', 2: 'b'}", "{'a': 'b'}", ERR], ('Wyrażenie słownikowe zamienia klucze z wartościami.', 'The dict comprehension swaps keys and values.')),
 C(3, ('Wczytaj n, potem n linii <code>słowo tłumaczenie</code>, a na końcu zdanie. Przetłumacz słowa ze słownika, pozostałe zostaw.', 'Read n, then n lines <code>word translation</code>, and finally a sentence. Translate the words found in the dictionary, leave the others.'),
   'n = int(input())\n', ['2\nkot cat\npies dog\nkot i pies', '1\na b\nc a a'], 'n = int(input())\nd = {}\nfor i in range(n):\n    k, v = input().split()\n    d[k] = v\nprint(" ".join(d.get(w, w) for w in input().split()))', ('d.get(w, w) zwraca tłumaczenie albo samo słowo.', 'd.get(w, w) returns the translation or the word itself.')),
]
EXTRA2['def'] = [
 Q(2, 'def f(x):\n    return x * x\n\nprint(f(f(2)))', ['16', '8', '4', '256'], ('f(2) = 4, f(4) = 16', 'f(2) = 4, f(4) = 16')),
 Q(2, 'def f():\n    return 1\n    return 2\n\nprint(f())', ['1', '2', '1\n2', 'None'], ('Pierwszy return kończy funkcję.', 'The first return ends the function.')),
 B(2, 'def f(a, b):\n    return a + b\nprint(f(1))', 2, 'print(f(1, 2))', ('Funkcja wymaga dwóch argumentów – TypeError.', 'The function needs two arguments – TypeError.')),
 Q(3, 'def f(*args):\n    return len(args)\n\nprint(f(1, 2, 3))', ['3', '1', '6', ERR], ('*args zbiera dowolną liczbę argumentów w krotkę.', '*args collects any number of arguments into a tuple.')),
 Q(3, 'def f(a, b):\n    return a // b, a % b\n\nq, r = f(17, 5)\nprint(q, r)', ['3 2', '(3, 2)', '2 3', ERR], ('Funkcja zwraca krotkę, którą rozpakowujemy.', 'The function returns a tuple, which we unpack.')),
 C(3, ('Napisz funkcję <code>doskonala(n)</code>: True, gdy n jest równe sumie swoich dzielników mniejszych od n (np. 6 = 1 + 2 + 3).', 'Write a function <code>is_perfect(n)</code>: True when n equals the sum of its divisors smaller than n (e.g. 6 = 1 + 2 + 3).'),
   ('def doskonala(n):\n    \n', 'def is_perfect(n):\n    \n'), [''], ('def doskonala(n):\n    return n > 1 and sum(d for d in range(1, n) if n % d == 0) == n', 'def is_perfect(n):\n    return n > 1 and sum(d for d in range(1, n) if n % d == 0) == n'),
   ('Zsumuj d od 1 do n-1, gdy n % d == 0.', 'Add up d from 1 to n-1 when n % d == 0.'),
   check=("assert [x for x in range(1, 1000) if doskonala(x)] == [6, 28, 496], 'Liczby doskonałe < 1000 to 6, 28, 496'", "assert [x for x in range(1, 1000) if is_perfect(x)] == [6, 28, 496], 'Perfect numbers < 1000 are 6, 28, 496'")),
]
EXTRA2['domyslne'] = [
 Q(2, 'def f(a, b=2, c=3):\n    return a * b * c\n\nprint(f(1, c=10))', ['20', '6', '30', ERR], ('a = 1, b = 2 (domyślne), c = 10.', 'a = 1, b = 2 (default), c = 10.')),
 Q(2, 'def f(x, n=2):\n    return x ** n\n\nprint(f(n=3, x=2))', ['8', '9', '6', ERR], ('Argumenty nazwane mogą być w dowolnej kolejności.', 'Keyword arguments can be in any order.')),
 B(2, 'def f(a, b=1):\n    return a - b\nprint(f(b=5))', 2, 'print(f(10, b=5))', ('Brakuje wymaganego argumentu a – TypeError.', 'The required argument a is missing – TypeError.')),
 Q(3, 'def f(t=None):\n    if t is None:\n        t = []\n    t.append(1)\n    return t\n\nf()\nprint(f())', ['[1]', '[1, 1]', '[]', 'None'], ('Bezpieczny wzorzec: nowa lista przy każdym wywołaniu.', 'The safe pattern: a new list on every call.')),
 Q(3, 'def f(a, b=5):\n    return a + b\n\nb = 10\nprint(f(1))', ['6', '11', '15', ERR], ('Wartość domyślna parametru nie ma nic wspólnego ze zmienną globalną b.', 'The default parameter value has nothing to do with the global variable b.')),
 C(3, ('Napisz funkcję <code>kwota(x, waluta="zł", miejsca=2)</code> zwracającą tekst, np. <code>kwota(12.5)</code> → <code>"12.50 zł"</code>, <code>kwota(3, "EUR", 0)</code> → <code>"3 EUR"</code>.', 'Write a function <code>money(x, currency="$", places=2)</code> returning text, e.g. <code>money(12.5)</code> → <code>"12.50 $"</code>, <code>money(3, "EUR", 0)</code> → <code>"3 EUR"</code>.'),
   ('def kwota(x, waluta="zł", miejsca=2):\n    \n', 'def money(x, currency="$", places=2):\n    \n'), [''],
   ('def kwota(x, waluta="zł", miejsca=2):\n    return f"{x:.{miejsca}f} {waluta}"', 'def money(x, currency="$", places=2):\n    return f"{x:.{places}f} {currency}"'),
   ('Format może być zmienną: f"{x:.{miejsca}f}"', 'The format can be a variable: f"{x:.{places}f}"'),
   check=("assert kwota(12.5) == '12.50 zł'\nassert kwota(3, 'EUR', 0) == '3 EUR'\nassert kwota(1, miejsca=1) == '1.0 zł'", "assert money(12.5) == '12.50 $'\nassert money(3, 'EUR', 0) == '3 EUR'\nassert money(1, places=1) == '1.0 $'")),
]
EXTRA2['zasieg'] = [
 Q(2, 'x = 5\ndef f(x):\n    x = x + 1\n    return x\n\nprint(f(x), x)', ['6 5', '6 6', '5 5', ERR], ('Parametr x to zmienna lokalna – globalne x się nie zmienia.', 'The parameter x is a local variable – the global x does not change.')),
 Q(2, 'def f():\n    a = 1\n\nf()\nprint("a" in globals())', ['False', 'True', ERR, 'None'], ('a istniało tylko wewnątrz f.', 'a existed only inside f.')),
 B(2, 'def f():\n    print(y)\nf()\ny = 3', 1, ('Przypisz y = 3 przed wywołaniem f()', 'Assign y = 3 before calling f()'), ('W chwili wywołania f() zmienna y jeszcze nie istnieje – NameError.', 'When f() is called, y does not exist yet – NameError.')),
 Q(3, 'x = 0\ndef f():\n    global x\n    x += 5\n    return x\n\nprint(f() + f(), x)', ['15 10', '10 10', '10 5', '15 5'], ('Pierwsze f() daje 5, drugie 10; razem 15, a x = 10.', 'The first f() gives 5, the second 10; together 15, and x = 10.')),
 Q(3, 'def f():\n    n = 0\n    def g():\n        nonlocal n\n        n += 1\n        return n\n    g()\n    return g()\n\nprint(f())', ['2', '1', '0', ERR], ('nonlocal pozwala g zmieniać n z funkcji otaczającej.', 'nonlocal lets g change n from the enclosing function.')),
 C(3, ('Napisz funkcję <code>przesun(t, k)</code>, która zwraca <b>nową</b> listę z każdą liczbą powiększoną o k i <b>nie zmienia</b> listy t.', 'Write a function <code>shift(t, k)</code> that returns a <b>new</b> list with every number increased by k and <b>does not change</b> t.'),
   ('def przesun(t, k):\n    \n', 'def shift(t, k):\n    \n'), [''], ('def przesun(t, k):\n    return [x + k for x in t]', 'def shift(t, k):\n    return [x + k for x in t]'),
   ('[x + k for x in t]', '[x + k for x in t]'),
   check=("a = [1, 2, 3]\nb = przesun(a, 10)\nassert b == [11, 12, 13], 'Zły wynik'\nassert a == [1, 2, 3], 'Lista t nie może się zmienić!'", "a = [1, 2, 3]\nb = shift(a, 10)\nassert b == [11, 12, 13], 'Wrong result'\nassert a == [1, 2, 3], 'The list t must not change!'")),
]
EXTRA2['moduly'] = [
 Q(2, 'import math\nprint(math.floor(-2.5), math.ceil(-2.5))', ['-3 -2', '-2 -3', '-2 -2', '-3 -3'], ('floor zaokrągla w dół (do mniejszej), ceil w górę.', 'floor rounds down (to the smaller), ceil rounds up.')),
 Q(2, 'import math\nprint(math.gcd(12, 18), math.factorial(4))', ['6 24', '6 10', '3 24', '36 24'], ('gcd = NWD, factorial = silnia.', 'gcd = greatest common divisor, factorial = 4!.')),
 B(2, 'import random\nprint(random.randint(1))', 1, 'print(random.randint(1, 6))', ('randint potrzebuje dwóch argumentów: początku i końca – TypeError.', 'randint needs two arguments: start and end – TypeError.')),
 Q(3, 'import random\nrandom.seed(5)\na = random.randint(1, 6)\nrandom.seed(5)\nb = random.randint(1, 6)\nprint(a == b)', ['True', 'False', ERR, 'None'], ('To samo ziarno daje tę samą sekwencję liczb.', 'The same seed gives the same sequence of numbers.')),
 Q(3, 'from math import sqrt as r\nprint(r(9))', ['3.0', '3', '81', ERR], ('as nadaje funkcji nową nazwę.', 'as gives the function a new name.')),
 C(3, ('Wczytaj dwa punkty (<code>x y</code> w dwóch liniach) i wypisz odległość między nimi z 2 miejscami po przecinku (<code>math.sqrt</code> lub <code>math.hypot</code>).', 'Read two points (<code>x y</code> on two lines) and print the distance between them to 2 decimal places (<code>math.sqrt</code> or <code>math.hypot</code>).'),
   'import math\n', ['0 0\n3 4', '1 1\n4 5', '-2 3\n2 -1'], 'import math\nx1, y1 = map(float, input().split())\nx2, y2 = map(float, input().split())\nprint(f"{math.hypot(x2 - x1, y2 - y1):.2f}")', ('√((x2-x1)² + (y2-y1)²)', '√((x2-x1)² + (y2-y1)²)')),
]
EXTRA2['try'] = [
 Q(2, 'try:\n    x = [1, 2][5]\nexcept IndexError:\n    x = -1\nprint(x)', ['-1', '2', ERR, 'None'], ('Błąd indeksu został złapany, więc x = -1.', 'The index error was caught, so x = -1.')),
 Q(2, 'def f():\n    try:\n        return "A"\n    finally:\n        print("B")\n\nprint(f())', ['B\nA', 'A\nB', 'A', 'B'], ('finally wykonuje się przed opuszczeniem funkcji – nawet przy return.', 'finally runs before leaving the function – even with return.')),
 F(2, ('Uzupełnij typ błędu', 'Fill in the error type'), 'try:\n    print(int("x"))\nexcept ___:\n    print("!")', [['ValueError', 'Exception']], ('int("x") zgłasza ValueError.', 'int("x") raises ValueError.'), expect='!'),
 Q(3, 'try:\n    1 / 0\nexcept Exception as e:\n    print(type(e).__name__)', ['ZeroDivisionError', 'Exception', 'ValueError', 'e'], ('as e daje dostęp do obiektu błędu.', 'as e gives access to the error object.')),
 Q(3, 'try:\n    print("1")\n    raise ValueError\n    print("2")\nexcept ValueError:\n    print("3")', ['1\n3', '1\n2\n3', '3', '1\n2'], ('raise zgłasza błąd samodzielnie – reszta bloku try jest pomijana.', 'raise throws an error yourself – the rest of the try block is skipped.')),
 C(3, ('Napisz funkcję <code>dziel(a, b)</code>, która zwraca a / b, a przy dzieleniu przez zero lub złych typach danych zwraca <code>None</code>.', 'Write a function <code>safe_div(a, b)</code> that returns a / b, and returns <code>None</code> for division by zero or wrong data types.'),
   ('def dziel(a, b):\n    \n', 'def safe_div(a, b):\n    \n'), [''],
   ('def dziel(a, b):\n    try:\n        return a / b\n    except (ZeroDivisionError, TypeError):\n        return None', 'def safe_div(a, b):\n    try:\n        return a / b\n    except (ZeroDivisionError, TypeError):\n        return None'),
   ('except (ZeroDivisionError, TypeError):', 'except (ZeroDivisionError, TypeError):'),
   check=("assert dziel(7, 2) == 3.5\nassert dziel(1, 0) is None\nassert dziel('a', 2) is None", "assert safe_div(7, 2) == 3.5\nassert safe_div(1, 0) is None\nassert safe_div('a', 2) is None")),
]
EXTRA2['pliki'] = [
 Q(2, 'with open("x.txt", "w") as f:\n    print("hej", file=f)\nprint(open("x.txt").read().strip())', ['hej', '', 'None', ERR], ('print(..., file=f) pisze do pliku.', 'print(..., file=f) writes to a file.')),
 Q(2, 'with open("x.txt", "w") as f:\n    f.write("a\\nb")\nprint(open("x.txt").read().split("\\n"))', ["['a', 'b']", "['a\\\\nb']", "['ab']", "['a', 'b', '']"], ('\\n to znak nowej linii – split dzieli po nim.', '\\n is the newline character – split splits on it.')),
 B(2, ('f = open("brak.txt")\nprint(f.read())', 'f = open("missing.txt")\nprint(f.read())'), 0, ('Sprawdź nazwę pliku albo utwórz go trybem "w".', 'Check the file name or create it with mode "w".'), ('Plik nie istnieje – FileNotFoundError.', 'The file does not exist – FileNotFoundError.')),
 Q(3, 'with open("x.txt", "w") as f:\n    f.write("abc")\nwith open("x.txt") as f:\n    print(f.read(2), f.read())', ['ab c', 'ab abc', 'abc', 'a bc'], ('read(2) czyta 2 znaki, kolejne read() – resztę.', 'read(2) reads 2 characters, the next read() – the rest.')),
 Q(3, 'f = open("y.txt", "w")\nf.write("1")\nprint(f.closed)\nf.close()\nprint(f.closed)', ['False\nTrue', 'True\nTrue', 'False\nFalse', ERR], ('Bez with plik trzeba zamknąć samemu.', 'Without with you must close the file yourself.')),
 C(3, ('Plik <code>wyniki.txt</code> ma linie <code>imię p1 p2 …</code>. Wypisz imię osoby z najwyższą średnią i tę średnią z 2 miejscami.', 'The file <code>wyniki.txt</code> has lines <code>name p1 p2 …</code>. Print the name of the person with the highest average and that average to 2 places.'),
   '', [''], 'best = None\nwith open("wyniki.txt") as f:\n    for l in f:\n        p = l.split()\n        s = sum(int(x) for x in p[1:]) / len(p[1:])\n        if best is None or s > best[1]:\n            best = (p[0], s)\nprint(f"{best[0]} {best[1]:.2f}")',
   ('Dla każdej linii policz średnią i zapamiętaj najlepszą.', 'For each line compute the average and remember the best.'),
   setup="open('wyniki.txt','w').write('Kapi 5 4 6\\nBobo 6 6 3\\nLulu 5 5 6 6\\n')"),
]
EXTRA2['suma'] = [
 Q(2, 't = [3, 8, 1]\nm = t[0]\nfor x in t[1:]:\n    if x > m:\n        m = x\nprint(m)', ['8', '3', '1', '12'], ('To szukanie maksimum.', 'This finds the maximum.')),
 Q(2, 't = [2, 3]\ns = 1\nfor x in t:\n    s *= x\nprint(s)', ['6', '5', '1', '0'], ('Iloczyn zaczynamy od 1, nie od 0.', 'A product starts from 1, not 0.')),
 B(2, 't = [4, 6, 8]\ns = 0\nfor x in t:\n    s += x\nprint(s / 2)', 4, 'print(s / len(t))', ('Średnia to suma podzielona przez liczbę elementów, a nie przez 2.', 'The average is the sum divided by the number of elements, not by 2.'),
   q=('Program miał wypisać średnią (6), a wypisuje 9.0. Kliknij linię do poprawy.', 'The program should print the average (6), but prints 9.0. Click the line to fix.'), noerr=True),
 Q(3, 't = [4, -2, 7, -5]\ns = 0\nfor x in t:\n    if x > 0:\n        s += x\nprint(s)', ['11', '4', '18', '-7'], ('Sumujemy tylko dodatnie: 4 + 7.', 'Only positives are added: 4 + 7.')),
 C(3, ('Wczytaj liczby. Wypisz średnią bez jednej najmniejszej i jednej największej wartości (2 miejsca), bez sort, min, max, sum.', 'Read numbers. Print the average without one smallest and one largest value (2 places), without sort, min, max, sum.'),
   't = [int(x) for x in input().split()]\n', ['1 5 3 9', '4 4 4', '10 0 5 5 7'],
   't = [int(x) for x in input().split()]\nmn = mx = t[0]\ns = 0\nfor x in t:\n    s += x\n    if x < mn:\n        mn = x\n    if x > mx:\n        mx = x\nprint(f"{(s - mn - mx) / (len(t) - 2):.2f}")',
   ('Policz sumę, minimum i maksimum w jednej pętli.', 'Compute the sum, minimum and maximum in one loop.'),
   check=("assert 'sort' not in __src and 'min(' not in __src and 'max(' not in __src and 'sum(' not in __src, 'Bez sort, min, max, sum!'", "assert 'sort' not in __src and 'min(' not in __src and 'max(' not in __src and 'sum(' not in __src, 'No sort, min, max, sum!'")),
 C(3, ('Wczytaj liczby. Wypisz, ile z nich jest większych od średniej.', 'Read numbers. Print how many of them are greater than the average.'),
   't = [int(x) for x in input().split()]\n', ['1 2 3 4 10', '5 5 5'], 't = [int(x) for x in input().split()]\nsr = sum(t) / len(t)\nprint(len([x for x in t if x > sr]))', ('Najpierw średnia, potem zliczanie.', 'First the average, then counting.')),
]
EXTRA2['szukanie'] = [
 Q(2, 't = [4, 8, 15, 16]\ni = 0\nwhile t[i] != 15:\n    i += 1\nprint(i)', ['2', '3', '15', '1'], ('Wyszukiwanie liniowe zatrzymuje się na indeksie 2.', 'Linear search stops at index 2.')),
 Q(2, 't = [1, 3, 5, 7]\nprint(len([x for x in t if x > 2]))', ['3', '4', '2', '15'], ('Liczby większe od 2: 3, 5, 7.', 'Numbers greater than 2: 3, 5, 7.')),
 B(2, 't = [1, 2, 3]\ni = 0\nwhile t[i] != 9:\n    i += 1', 2, 'while i < len(t) and t[i] != 9:', ('Liczby 9 nie ma, więc i wychodzi poza listę – IndexError.', '9 is not in the list, so i goes past the end – IndexError.')),
 QN(3, ('Ile porównań wykona w najgorszym razie wyszukiwanie binarne w posortowanej liście 1000 elementów?', 'How many comparisons does binary search make in the worst case in a sorted list of 1000 elements?'), ['10', '1000', '500', '100'], ('Każde porównanie dzieli zakres na pół: 2¹⁰ = 1024 ≥ 1000.', 'Each comparison halves the range: 2¹⁰ = 1024 ≥ 1000.')),
 C(3, ('Wczytaj liczby. Wypisz pierwszą liczbę, która wcześniej już wystąpiła, albo <code>-</code>.', 'Read numbers. Print the first number that has already appeared before, or <code>-</code>.'),
   't = input().split()\n', ['3 1 4 1 5 3', '1 2 3'], 't = input().split()\nseen = set()\nw = "-"\nfor x in t:\n    if x in seen:\n        w = x\n        break\n    seen.add(x)\nprint(w)', ('Zbiór widzianych liczb i break.', 'A set of seen numbers and break.')),
 C(3, ('Wczytaj liczby. Wypisz najdłuższy fragment ściśle rosnących kolejnych liczb (przy remisie – pierwszy).', 'Read numbers. Print the longest run of strictly increasing consecutive numbers (on a tie – the first).'),
   't = [int(x) for x in input().split()]\n', ['1 2 0 3 4 5 1', '5 4 3', '1 2 1 2'],
   't = [int(x) for x in input().split()]\nbs, bl = 0, 1\ns = 0\nfor i in range(1, len(t) + 1):\n    if i == len(t) or t[i] <= t[i - 1]:\n        if i - s > bl:\n            bs, bl = s, i - s\n        s = i\nprint(*t[bs:bs + bl])',
   ('Pamiętaj początek bieżącego fragmentu i najlepszy fragment.', 'Remember the start of the current run and the best run.')),
]
EXTRA2['babel'] = [
 Q(2, 't = [2, 1]\nif t[0] > t[1]:\n    t[0], t[1] = t[1], t[0]\nprint(t)', ['[1, 2]', '[2, 1]', '[1, 1]', ERR], ('Jedna zamiana sąsiadów.', 'One swap of neighbours.')),
 QN(2, ('Ile porównań wykona sortowanie bąbelkowe (bez wczesnego przerwania) dla 5 elementów?', 'How many comparisons does bubble sort (without early exit) make for 5 elements?'), ['10', '25', '5', '20'], ('4 + 3 + 2 + 1 = 10', '4 + 3 + 2 + 1 = 10')),
 F(2, ('Uzupełnij porównanie, aby sortować <b>malejąco</b>', 'Fill in the comparison to sort in <b>descending</b> order'), 't = [1, 3, 2]\nfor i in range(2):\n    for j in range(2 - i):\n        if t[j] ___ t[j + 1]:\n            t[j], t[j + 1] = t[j + 1], t[j]\nprint(t)', [['<']], ('Zamieniamy, gdy lewy jest mniejszy.', 'Swap when the left one is smaller.'), expect='[3, 2, 1]'),
 Q(3, 't = [4, 3, 2, 1]\nfor i in range(2):\n    for j in range(3 - i):\n        if t[j] > t[j + 1]:\n            t[j], t[j + 1] = t[j + 1], t[j]\nprint(t)', ['[2, 1, 3, 4]', '[1, 2, 3, 4]', '[3, 2, 1, 4]', '[3, 4, 2, 1]'], ('Po dwóch przejściach dwie największe liczby są już na końcu.', 'After two passes the two largest numbers are already at the end.')),
 C(3, ('Sortowanie przez wybieranie: w każdym kroku znajdź najmniejszy element z nieposortowanej części i zamień go z pierwszym. Bez sort, min. Wypisz wynik.', 'Selection sort: at each step find the smallest element in the unsorted part and swap it with the first one. No sort, min. Print the result.'),
   't = [int(x) for x in input().split()]\n', ['5 3 8 1', '2 2 1'],
   't = [int(x) for x in input().split()]\nfor i in range(len(t)):\n    k = i\n    for j in range(i + 1, len(t)):\n        if t[j] < t[k]:\n            k = j\n    t[i], t[k] = t[k], t[i]\nprint(*t)',
   ('Indeks k najmniejszego, potem zamiana t[i] z t[k].', 'Index k of the smallest, then swap t[i] with t[k].'),
   check=("assert 'sort' not in __src and 'min(' not in __src, 'Bez sort i min!'", "assert 'sort' not in __src and 'min(' not in __src, 'No sort or min!'")),
 C(3, ('Wczytaj słowa i posortuj je bąbelkowo według długości (słowa równej długości zostają w kolejności wejścia). Bez sort.', 'Read words and bubble sort them by length (words of equal length keep their input order). No sort.'),
   't = input().split()\n', [('kapibara ma dwa kolorowe kapelusze', 'capybara has two colourful hats'), 'ccc a bb aa'],
   't = input().split()\nn = len(t)\nfor i in range(n - 1):\n    for j in range(n - 1 - i):\n        if len(t[j]) > len(t[j + 1]):\n            t[j], t[j + 1] = t[j + 1], t[j]\nprint(*t)',
   ('Porównuj len(t[j]) > len(t[j + 1]) – ostre > zachowuje kolejność równych.', 'Compare len(t[j]) > len(t[j + 1]) – strict > keeps equal ones in order.'),
   check=("assert 'sort' not in __src, 'Bez sort!'", "assert 'sort' not in __src, 'No sort!'")),
]
EXTRA2['nwd'] = [
 Q(2, 'a, b = 21, 14\nwhile b:\n    a, b = b, a % b\nprint(a)', ['7', '14', '21', '1'], ('NWD(21, 14) = 7.', 'GCD(21, 14) = 7.')),
 Q(2, 'n = 29\nprint(all(n % d for d in range(2, n)))', ['True', 'False', '29', ERR], ('29 nie dzieli się przez żadną liczbę od 2 do 28 – jest pierwsza.', '29 is not divisible by any number from 2 to 28 – it is prime.')),
 F(2, ('Uzupełnij sprawdzenie palindromu', 'Fill in the palindrome check'), 's = "potop"\nprint(s == s[___])', [['::-1']], ('s[::-1] to tekst od tyłu.', 's[::-1] is the string backwards.'), expect='True'),
 Q(3, 'def p(n):\n    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))\n\nprint([x for x in range(20, 30) if p(x)])', ['[23, 29]', '[21, 23, 29]', '[23]', '[]'], ('Między 20 a 29 pierwsze są tylko 23 i 29.', 'Between 20 and 29 only 23 and 29 are prime.')),
 C(3, ('Wczytaj dwie liczby i wypisz ich NWW (najmniejszą wspólną wielokrotność), korzystając z NWD.', 'Read two numbers and print their LCM (least common multiple), using the GCD.'),
   '', ['4\n6', '21\n6', '7\n13'], 'a = int(input())\nb = int(input())\nx, y = a, b\nwhile y:\n    x, y = y, x % y\nprint(a * b // x)', ('NWW = a · b / NWD(a, b)', 'LCM = a · b / GCD(a, b)')),
 C(3, ('Liczby bliźniacze: wczytaj n i wypisz wszystkie pary liczb pierwszych (p, p + 2), gdzie p + 2 ≤ n, każdą jako <code>p q</code>.', 'Twin primes: read n and print all pairs of primes (p, p + 2) where p + 2 ≤ n, each as <code>p q</code>.'),
   'n = int(input())\n', ['20', '5'], 'n = int(input())\ndef is_p(k):\n    return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))\nfor p in range(2, n - 1):\n    if is_p(p) and is_p(p + 2):\n        print(p, p + 2)',
   ('Napisz pomocniczą funkcję sprawdzającą pierwszość.', 'Write a helper function that checks primality.')),
]
EXTRA2['bledy'] = [
 QE(2, 'print(len(5))', ['TypeError', 'ValueError', 'NameError', 'SyntaxError'], ('Liczba nie ma długości – len działa dla tekstów i kolekcji.', 'A number has no length – len works for strings and collections.')),
 QE(2, 'x = [1, 2]\nx.push(3)', ['AttributeError', 'NameError', 'TypeError', 'IndexError'], ('Lista nie ma metody push – tylko append.', 'A list has no push method – only append.')),
 B(2, 'd = {"a": 1}\nprint(d["A"])', 1, 'print(d["a"])', ('Klucze rozróżniają wielkość liter – KeyError.', 'Keys are case-sensitive – KeyError.')),
 QE(3, 'import maths', ['ModuleNotFoundError', 'NameError', 'SyntaxError', 'AttributeError'], ('Nie ma modułu maths (literówka – math).', 'There is no module maths (a typo – math).')),
 QE(3, 'def f():\n    return f()\n\nf()', ['RecursionError', 'TypeError', 'ZeroDivisionError', 'SyntaxError'], ('Funkcja wywołuje samą siebie bez końca.', 'The function calls itself forever.')),
 dict(t='code', l=3, q=('Ten program ma 3 błędy. Popraw je, aby wypisał:<br><code>Najmniejsza: 1</code><br><code>Największa: 3</code>', 'This program has 3 errors. Fix them so it prints:<br><code>Smallest: 1</code><br><code>Largest: 3</code>'),
      start=('t = [3, 1, 2]\nt.sort\nprint("Najmniejsza: " + t[0])\nprint("Największa: " + t[3])\n', 't = [3, 1, 2]\nt.sort\nprint("Smallest: " + t[0])\nprint("Largest: " + t[3])\n'),
      tests=[dict(i='', o='@')], sol=('t = [3, 1, 2]\nt.sort()\nprint("Najmniejsza: " + str(t[0]))\nprint("Największa: " + str(t[2]))', 't = [3, 1, 2]\nt.sort()\nprint("Smallest: " + str(t[0]))\nprint("Largest: " + str(t[2]))'),
      hint=('Brakujące nawiasy przy sort, zamiana liczby na tekst i zły indeks.', 'Missing brackets after sort, converting a number to text and a wrong index.')),
]
EXTRA2['rekur'] = [
 Q(2, 'def f(n):\n    if n == 0:\n        return ""\n    return f(n - 1) + str(n)\n\nprint(f(4))', ['1234', '4321', '10', '4'], ('Najpierw schodzimy do 0, a liczby doklejamy w drodze powrotnej.', 'We go down to 0 first, and append the numbers on the way back.')),
 Q(2, 'def f(n):\n    if n < 10:\n        return n\n    return f(n // 10)\n\nprint(f(4821))', ['4', '1', '15', '482'], ('Funkcja zwraca pierwszą cyfrę liczby.', 'The function returns the first digit of the number.')),
 B(2, 'def f(n):\n    return n * f(n - 1)\nprint(f(3))', 1, ('Dodaj warunek stopu: if n <= 1: return 1', 'Add a base case: if n <= 1: return 1'), ('Brakuje warunku stopu, więc wywołania nigdy się nie kończą – RecursionError.', 'The base case is missing, so the calls never end – RecursionError.'), cause=True),
 Q(3, 'def f(t):\n    if not t:\n        return 0\n    return t[0] + f(t[1:])\n\nprint(f([1, 2, 3, 4]))', ['10', '4', '1', '24'], ('Suma listy: pierwszy element + suma reszty.', 'Sum of a list: the first element + the sum of the rest.')),
 C(3, ('Napisz rekurencyjną funkcję <code>binarnie(n)</code> zwracającą zapis dwójkowy liczby n ≥ 0 jako tekst – bez bin() i bez pętli.', 'Write a recursive function <code>binary(n)</code> that returns the binary form of n ≥ 0 as text – without bin() and without loops.'),
   ('def binarnie(n):\n    \n', 'def binary(n):\n    \n'), [''], ('def binarnie(n):\n    if n < 2:\n        return str(n)\n    return binarnie(n // 2) + str(n % 2)', 'def binary(n):\n    if n < 2:\n        return str(n)\n    return binary(n // 2) + str(n % 2)'),
   ('binarnie(n // 2) + str(n % 2)', 'binary(n // 2) + str(n % 2)'),
   check=("assert [binarnie(x) for x in (0, 1, 2, 5, 10, 255)] == ['0', '1', '10', '101', '1010', '11111111']\nassert 'bin(' not in __src and 'for' not in __src and 'while' not in __src", "assert [binary(x) for x in (0, 1, 2, 5, 10, 255)] == ['0', '1', '10', '101', '1010', '11111111']\nassert 'bin(' not in __src and 'for' not in __src and 'while' not in __src")),
 C(3, ('Napisz rekurencyjną funkcję <code>permutacje(s)</code> zwracającą listę wszystkich ułożeń liter tekstu s (bez itertools).', 'Write a recursive function <code>perms(s)</code> returning a list of all arrangements of the letters of s (without itertools).'),
   ('def permutacje(s):\n    \n', 'def perms(s):\n    \n'), [''],
   ('def permutacje(s):\n    if len(s) <= 1:\n        return [s]\n    w = []\n    for i in range(len(s)):\n        for p in permutacje(s[:i] + s[i + 1:]):\n            w.append(s[i] + p)\n    return w', 'def perms(s):\n    if len(s) <= 1:\n        return [s]\n    w = []\n    for i in range(len(s)):\n        for p in perms(s[:i] + s[i + 1:]):\n            w.append(s[i] + p)\n    return w'),
   ('Dla każdej litery: ta litera + permutacje pozostałych.', 'For each letter: that letter + the permutations of the rest.'),
   check=("assert sorted(permutacje('abc')) == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']\nassert permutacje('x') == ['x']\nassert 'itertools' not in __src", "assert sorted(perms('abc')) == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']\nassert perms('x') == ['x']\nassert 'itertools' not in __src")),
]
