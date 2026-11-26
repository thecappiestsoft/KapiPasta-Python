# KapiPasta - Python: English overrides for content/pl/part4_dodatkowe.py (same lessons, same order).
# After editing run: python3 tools/build.py

EXTRA = {}

EXTRA['print'] = [
 dict(q='What will the program print?', opts=['2 + 3\n5', '5\n5', '2 + 3\n2 + 3', 'Error'], why='Text in quotes is printed literally, while an expression without quotes is calculated.'),
 dict(q='Fill in the gap so it prints: <code>A-B</code>', why='The sep parameter decides what goes between the values.'),
 dict(q='Using <b>one</b> print, print a frame on three lines:<br><code>+------+<br>| Kapi |<br>+------+</code>', check="assert __src.count('print') == 1, 'Use only one print'",
      hint='sep="\\n" puts a newline between the values.'),
]
EXTRA['fstr'] = [
 dict(why='.0f rounds to a whole number (3.5 → 4).'),
 dict(why='The = sign in an f-string prints the variable name and its value – great for debugging.'),
 dict(q='Read a product name, a price (float) and a quantity (int). Print a receipt line:<br>name left-aligned in 10 characters, quantity right-aligned in 3, price and total right-aligned with 2 decimals (width 6 and 7).<br>For <code>melon / 4.5 / 3</code>: <code>melon       3 x   4.50 =   13.50</code>',
      tests=[dict(i='melon\n4.5\n3', o='melon       3 x   4.50 =   13.50'), dict(i='pear\n12\n1', o='pear        1 x  12.00 =   12.00')]),
]
EXTRA['zmienne'] = [
 dict(opts=['55 10', '10 10', '55 55', 'Error'], why='Text times 2 is repetition, a number times 2 is multiplication.'),
 dict(why='Division / always gives a float, even when the result is “round”.'),
 dict(q='The program raises an error. Click the buggy line.', why="You can't add a number and text – TypeError. y must be turned into a number."),
 dict(q='Swap the values of a and b <b>without</b> writing <code>a, b = b, a</code> and without a third variable – use addition and subtraction.',
      start='a = int(input())\nb = int(input())\n# swap a and b\n\nprint(a, b)\n', check="assert 'b, a' not in __src, 'No a, b = b, a!'", hint='a = a + b, then b = a - b, then a = a - b.'),
]
EXTRA['input'] = [
 dict(q='The user types 5. What will the program print?', opts=['555', '15', '5 5 5', 'Error'], why='input() returns the text "5", and text times 3 is "555".'),
 dict(q='The user types 12. Which line raises an error?', code='''age = input("Age: ")
print(age + 1)''', fix='print(int(age) + 1)', why='age is text. Text cannot be added to a number – TypeError.'),
 dict(q='Read three numbers on <b>one</b> line separated by spaces (e.g. <code>3 4 5</code>) and print their average to 2 decimal places.'),
]
EXTRA['oper'] = [
 dict(opts=['512', '64', '36', 'Error'], why='Powers are calculated from the right: 3 ** 2 = 9, and 2 ** 9 = 512.'),
 dict(q='Read a number of minutes (it may be more than a day). Print the clock time as <code>HH:MM</code> with leading zeros.<br>E.g. 1505 → <code>01:05</code>',
      hint='Hour: m // 60 % 24, the :02d format adds a leading zero.'),
]
EXTRA['logika'] = [
 dict(opts=['True', 'False', 'Error', 'None'], why='The comparison goes first: True == False is False, and not False is True.'),
 dict(why='or returns the first “truthy” value, and and returns the first “falsy” one (or the last).'),
 dict(q='Read three side lengths (each on a new line). Print <code>True</code> if they can form a triangle (each side shorter than the sum of the other two), otherwise <code>False</code> – no if.',
      check="assert 'if' not in __src, 'No if!'", hint='Join three conditions with and.'),
]
EXTRA['if'] = [
 dict(opts=['B', 'A', 'A\nB', 'Error'], why='The number 0 is treated as False.'),
 dict(q='For 95 points the program prints “satisfactory”. Click the line that needs changing.', code='''points = 95
if points >= 50:
    print("satisfactory")
elif points >= 90:
    print("excellent")''', fix='if points >= 90:  (check from the highest threshold)',
      why='The first matching condition wins – 95 >= 50 is true, so elif is never checked.'),
 dict(q='Read three numbers (each on a new line) and print them in ascending order separated by spaces – using only if (no sort, min, max).',
      check="assert 'sort' not in __src and 'min(' not in __src and 'max(' not in __src, 'No sort, min or max!'", hint='Swap neighbouring pairs: (a, b), (b, c), then (a, b) again.'),
]
EXTRA['for'] = [
 dict(why='i takes 0, 1, 2, and we print the doubled values.'),
 dict(q='Fill in the step to add up the even numbers from 0 to 10', why='Step 2 gives 0, 2, 4, 6, 8, 10 – their sum is 30.'),
 dict(q='Read n and print the n-th Fibonacci number (F0 = 0, F1 = 1, each next one is the sum of the previous two). Use a for loop.', hint='Keep the last two values: a, b = b, a + b.'),
 dict(q='Read n and print all divisors of n in ascending order, separated by spaces.', sol='n = int(input())\nd = []\nfor i in range(1, n + 1):\n    if n % i == 0:\n        d.append(str(i))\nprint(" ".join(d))',
      hint='Check every i from 1 to n: n % i == 0.'),
]
EXTRA['while'] = [
 dict(why='i: 0 → 3 → 6 → 9 → 12. At 12 the condition i < 10 is false.'),
 dict(code='''for i in range(3):
    if i == 5:
        break
else:
    print("none")''', opts=['none', 'nothing', '0 1 2', 'Error'], why='The else of a for loop runs when the loop was not stopped by break.'),
 dict(q='The Collatz problem: read n. While n ≠ 1: if n is even – n = n // 2, otherwise n = 3n + 1. Print the number of steps.'),
]
EXTRA['zagn'] = [
 dict(q='How many stars will the program print?', why='For i = 0, 1, 2 the inner loop runs 0 + 1 + 2 = 3 times.'),
 dict(q='Fill in the gap to build steps out of #', why='Text times a number repeats the text.'),
 dict(q='Read n. Print all pairs <code>a b</code> where 1 ≤ a &lt; b ≤ n and a + b is even (each pair on a new line, ascending).', hint='The inner loop starts at a + 1.'),
]
EXTRA['slice'] = [
 dict(why='From index 2 to the end.'),
 dict(why='The last three characters.'),
 dict(q='Read a word and print it with the first and last letters swapped (a one-letter word stays the same).',
      tests=[dict(i='capybara', o='aapybarc'), dict(i='ab', o='ba'), dict(i='x', o='x')]),
]
EXTRA['metody'] = [
 dict(code='print("Anna".lower().count("a"))', why='"Anna".lower() is "anna" – it contains two “a”.'),
 dict(why='There is empty text between the two commas.'),
 dict(q='Read a sentence and print it so that every word starts with a capital letter and the rest is lowercase – <b>without</b> the title() method.',
      tests=[dict(i='kAPI loves WATER', o='Kapi Loves Water'), dict(i='a', o='A')], check="assert 'title' not in __src, 'No title()!'", hint='For each word: w[0].upper() + w[1:].lower()'),
]
EXTRA['znaki'] = [
 dict(code='''for ch in "abc":
    print(ch, end="-")''', why='A dash is printed after each letter.'),
 dict(code='''w = ""
for ch in "Kapi":
    if ch.isupper():
        w += ch.lower()
    else:
        w += ch.upper()
print(w)''', why='Capitals become lowercase and lowercase letters become capitals.'),
 dict(q='RLE compression: read a word and write each run of identical letters as the letter and the number of repeats.<br><code>aaabccdddd</code> → <code>a3b1c2d4</code>',
      hint='Count repeats; when the letter changes, add the letter and the counter.'),
]
EXTRA['listy'] = [
 dict(why='-1 is the last element, -2 – the one before it.'),
 dict(why='t[1] is [3, 4], and its element 0 is 3.'),
 dict(q='Read numbers on one line. Print them without the first and last elements, in reverse order, separated by spaces (use slices).'),
]
EXTRA['metodylist'] = [
 dict(why='insert(0, x) puts x at the front.'),
 dict(why='sorted() creates a new list and does not change the original.'),
 dict(q='Read numbers on one line. Remove all zeros from the list (use while and remove) and print the list.', check="assert 'remove' in __src and 'while' in __src, 'Use while and remove'"),
]
EXTRA['krotki'] = [
 dict(opts=['3', '1', '6', 'Error'], why='The tuple has 3 elements.'),
 dict(why='2 is already in the set, so only 4 gets added.'),
 dict(q='Read two sentences (two lines). Print, in alphabetical order, the words that appear in both, separated by spaces.',
      tests=[dict(i='kapi loves water\nbobo loves water', o='loves water'), dict(i='a b c\nc b x', o='b c')]),
]
EXTRA['slowniki'] = [
 dict(opts=["{'a': 5}", "{'a': 1}", "{'a': 1, 'a': 5}", 'Error'], why='Keys are unique – assignment overwrites the value.'),
 dict(why='keys() returns the keys.'),
 dict(q='The program raises an error. Click the buggy line.', why="The variable v doesn't exist – NameError. The loop uses k."),
 dict(q='Read a sentence. Group the words by length and print the groups in ascending order of length as <code>length: words</code> (words in order of appearance).',
      tests=[dict(i='a cat is on my bed', o='1: a\n2: is on my\n3: cat bed')], hint='A dictionary length → list of words, then sorted(d).'),
]
EXTRA['def'] = [
 dict(why='return a, b returns a tuple.'),
 dict(q='Write a function <code>is_anagram(a, b)</code> that returns True when the words are made of the same letters (ignore letter case).',
      start='def is_anagram(a, b):\n    \n', check="assert is_anagram('Cat', 'act') is True\nassert is_anagram('kapi', 'pika') is True\nassert is_anagram('kapi', 'kapa') is False\nassert is_anagram('ab', 'abb') is False",
      sol='def is_anagram(a, b):\n    return sorted(a.lower()) == sorted(b.lower())', hint='sorted("cat") gives a list of sorted letters.'),
]
EXTRA['domyslne'] = [
 dict(q='Fill in the gap so it prints: <code>Hey, Kapi?</code>', code='''def greet(name, mark="!"):
    print("Hey, " + name + mark)
greet("Kapi", mark=___)''', expect='Hey, Kapi?', why='An argument can be given by the parameter name.'),
 dict(code='''def add(x, t=[]):
    t.append(x)
    return t

add(1)
print(add(2))''', opts=['[1, 2]', '[2]', '[1]', 'Error'], why='A trap! The default list is created once and shared between calls. Better write t=None.'),
 dict(q='Write a function <code>rnd(x, places=0)</code>: returns x rounded to the given number of places; when places == 0 – returns a whole number (int).',
      start='def rnd(x, places=0):\n    \n', check="assert rnd(2.567, 2) == 2.57\nassert rnd(2.6) == 3 and type(rnd(2.6)) is int, 'rnd(2.6) should return the int 3'\nassert rnd(1.25, 1) == 1.2",
      sol='def rnd(x, places=0):\n    if places == 0:\n        return int(round(x))\n    return round(x, places)', hint='round(x, places); for 0 use int(round(x)).'),
]
EXTRA['zasieg'] = [
 dict(opts=['3', 'Error', 'None', 'y'], why='The function returns the value of the local variable y.'),
 dict(opts=['2 1', '1 1', '2 2', 'Error'], why='g sees x from the enclosing function (2), and the global x stays 1.'),
 dict(q='Write a function <code>counter()</code> that increases the global variable <code>calls</code> by 1 and returns its new value.',
      start='calls = 0\n\ndef counter():\n    \n', check="a = counter()\nb = counter()\nassert (a, b) == (1, 2), 'The first call should give 1, the second 2'\nassert calls == 2",
      sol='calls = 0\n\ndef counter():\n    global calls\n    calls += 1\n    return calls', hint='global calls'),
]
EXTRA['moduly'] = [
 dict(opts=['True', 'False', '3.14', 'Error'], why='pi ≈ 3.14159 > 3.'),
 dict(opts=['5.0', '5', '17', 'Error'], why='After from math import sqrt you can write plain sqrt. The result is a float.'),
 dict(q='Toss a coin 10 times: <code>random.choice(["H", "T"])</code>. Print the number of heads (H). The random seed is already set, so the result is repeatable.',
      check="assert 'choice' in __src, 'Use random.choice'", sol='import random\nrandom.seed(1)\nn = 0\nfor i in range(10):\n    if random.choice(["H", "T"]) == "H":\n        n += 1\nprint(n)',
      hint='A loop 10 times and a counter of heads.'),
]
EXTRA['try'] = [
 dict(why='int("5") works, but dividing by 0 raises ZeroDivisionError.'),
 dict(q='The user types “abc”. Where does Python raise an error?', code='''try:
    x = int(input())
except ValueError:
    print("bad number")
print(x * 2)''', fix='Move print(x * 2) into the try block, or give x a value in except.',
      why="After the error is caught, x doesn't exist, so print(x * 2) raises NameError."),
 dict(q='Read n, then n lines. Add up only the whole numbers and count the rest as invalid. Print <code>sum: S, invalid: B</code>.',
      tests=[dict(i='4\n5\nkapi\n-2\n3.5', o='sum: 3, invalid: 2'), dict(i='1\n7', o='sum: 7, invalid: 0')],
      sol='n = int(input())\ns = 0\nb = 0\nfor i in range(n):\n    try:\n        s += int(input())\n    except ValueError:\n        b += 1\nprint(f"sum: {s}, invalid: {b}")', hint='try/except inside a loop.'),
]
EXTRA['pliki'] = [
 dict(q='What does <code>f.read()</code> return?', opts=['The whole file text as a str', 'A list of lines', 'The first line', 'The number of characters'],
      why='read() returns the whole content as one string; readlines() gives a list of lines.'),
 dict(why='Mode "a" appends at the end, without a new line.'),
 dict(q='The file <code>text.txt</code> already exists. Print the number of lines, words and characters (without newline characters) as <code>lines: L, words: S, chars: Z</code>.',
      setup="open('text.txt','w',encoding='utf-8').write('Kapi loves water\\nBobo loves melons\\n')", tests=[dict(i='', o='lines: 2, words: 6, chars: 33')],
      sol='with open("text.txt", encoding="utf-8") as f:\n    lines = f.read().splitlines()\nprint(f"lines: {len(lines)}, words: {sum(len(l.split()) for l in lines)}, chars: {sum(len(l) for l in lines)}")',
      hint='splitlines() removes the \\n characters.'),
]
EXTRA['suma'] = [
 dict(why='12 / 3 = 4.0 (division / gives a float).'),
 dict(q='How many comparisons does finding the largest element in a list of n elements take (starting from t[0])?', why='The first element is the starting point, so we compare with the other n - 1.'),
 dict(q='Read numbers. Print the second largest <b>distinct</b> value (no sort or max). If it does not exist – print <code>none</code>.',
      tests=[dict(i='4 9 2 9 7', o='7'), dict(i='5 5', o='none'), dict(i='1 2', o='1')], check="assert 'sort' not in __src and 'max(' not in __src, 'No sort or max!'",
      sol='t = [int(x) for x in input().split()]\na = b = None\nfor x in t:\n    if a is None or x > a:\n        if a is not None:\n            b = a\n        a = x\n    elif x != a and (b is None or x > b):\n        b = x\nprint("none" if b is None else b)',
      hint='Keep two values: the largest and the second.'),
]
EXTRA['szukanie'] = [
 dict(why='The number 3 appears twice.'),
 dict(q='Fill in the counting step', code='''def how_many(t, x):
    n = 0
    for e in t:
        if e == x:
            n ___ 1
    return n
print(how_many([1, 2, 1], 1))''', why='n += 1 increases the counter.'),
 dict(q='Binary search: write a function <code>binary(t, x)</code> for a <b>sorted</b> list that returns the index of x or -1 (without in or index). Split the range in half.',
      start='def binary(t, x):\n    \n', check="t = list(range(0, 1000, 3))\nassert binary(t, 300) == 100\nassert binary(t, 301) == -1\nassert binary([], 1) == -1\nassert binary([5], 5) == 0\nassert '.index' not in __src and ' in t' not in __src",
      sol='def binary(t, x):\n    a, b = 0, len(t) - 1\n    while a <= b:\n        s = (a + b) // 2\n        if t[s] == x:\n            return s\n        if t[s] < x:\n            a = s + 1\n        else:\n            b = s - 1\n    return -1',
      hint='a, b = 0, len(t) - 1; middle s = (a + b) // 2.'),
]
EXTRA['babel'] = [
 dict(q='How many swaps will bubble sort make for the list <code>[3, 2, 1]</code>?', why='(3,2)→[2,3,1], (3,1)→[2,1,3], (2,1)→[1,2,3] – three swaps.'),
 dict(q='After how many passes will the list <code>[1, 2, 3, 5, 4]</code> be sorted?', why='One swap (5, 4) in the first pass is enough.'),
 dict(q='Bubble sort with early exit: stop when a pass makes no swaps. Print the sorted numbers, and on the second line the number of passes made (a pass with no swaps also counts).',
      sol='t = [int(x) for x in input().split()]\nn = len(t)\np = 0\nfor i in range(n - 1):\n    p += 1\n    swapped = False\n    for j in range(n - 1 - i):\n        if t[j] > t[j + 1]:\n            t[j], t[j + 1] = t[j + 1], t[j]\n            swapped = True\n    if not swapped:\n        break\nprint(*t)\nprint(p)',
      hint='Set swapped = False at the start of a pass; after the pass: if not swapped: break.'),
]
EXTRA['nwd'] = [
 dict(q='Which word is a palindrome?', opts=['kayak', 'capybara', 'python', 'melon'], why='“kayak” read backwards is still “kayak”.'),
 dict(q='Sieve of Eratosthenes: read n and print all primes ≤ n, separated by spaces.', hint='A list of True/False; for each prime i, cross out its multiples.'),
 dict(q='Factorise a number into primes. Print the factors in ascending order separated by spaces.<br><code>360</code> → <code>2 2 2 3 3 5</code>', hint='Divide by d as long as you can, then d += 1.'),
]
EXTRA['bledy'] = [
 dict(q='Which error will this code raise?', why='The text "3.5" is not a valid whole number.'),
 dict(q='Read the message and click the buggy line.', code='''numbers = [1, 2, 3]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers[3])''', fix='print(numbers[2])  (or numbers[-1])', why='The list has indexes 0–2 – IndexError.'),
 dict(q='This program has 2 errors. Fix them so it prints <code>Area: 12</code>.', start='def area(a, b)\n    return a * b\nprint("Area: " + area(3, 4))\n',
      tests=[dict(i='', o='Area: 12')], sol='def area(a, b):\n    return a * b\nprint("Area: " + str(area(3, 4)))', hint='A missing colon and turning a number into text.'),
]
EXTRA['rekur'] = [
 dict(why='f: 1, 1, 2, 3, 5, 8 for n = 0…5.'),
 dict(q='Fill in the recursive GCD', code='''def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, ___)
print(gcd(12, 18))''', why='gcd(a, b) = gcd(b, a % b).'),
 dict(q='Towers of Hanoi: write a recursive function <code>hanoi(n, src, aux, dst)</code> that prints the moves as <code>src -> dst</code> to move n disks.',
      start='def hanoi(n, src, aux, dst):\n    \n\nhanoi(2, "A", "B", "C")\n',
      check="import io, sys\n_b = io.StringIO(); _o = sys.stdout; sys.stdout = _b\nhanoi(3, 'A', 'B', 'C')\nsys.stdout = _o\nassert len(_b.getvalue().split(chr(10))) - 1 == 7, '3 disks = 7 moves'\nassert 'for' not in __src and 'while' not in __src",
      sol='def hanoi(n, src, aux, dst):\n    if n == 0:\n        return\n    hanoi(n - 1, src, dst, aux)\n    print(f"{src} -> {dst}")\n    hanoi(n - 1, aux, src, dst)\n\nhanoi(2, "A", "B", "C")',
      hint='Move n-1 to the auxiliary peg, the largest to the target, then n-1 from the auxiliary to the target.'),
]

# --- Top-up so every lesson has exactly 12 tasks (6 × level 1, 3 × level 2, 3 × level 3) ---
def add(lid, *tasks):
    EXTRA.setdefault(lid, []).extend(tasks)

add('print',
 dict(why='end="" joins a and b, and end="\\n\\n" adds an empty line.'),
 dict(q='Read n and, with one print, print the numbers 1 to n separated by a comma and a space. Use <code>*range(...)</code> and <code>sep</code>.<br>4 → <code>1, 2, 3, 4</code>',
      check="assert __src.count('print') == 1 and 'for' not in __src, 'One print, no loop'"))
add('fstr',
 dict(code='''name = "Bobo"
print(f"Hi, {name}!")''', opts=['Hi, Bobo!', 'Hi, {name}!', 'Hi, name!', 'f"Hi, Bobo!"'], why='{name} is replaced with the value of the variable.'))
add('zmienne',
 dict(q='Read a decimal number (e.g. <code>3.75</code>). Print its whole part (int) and its fractional part rounded to 2 places, separated by a space.', hint='int(x) cuts off the fractional part.'))
add('input',
 dict(q='Read a name and a birth year on one line, e.g. <code>Alex 2012</code>. Print <code>Alex is 14 years old in 2026</code>.',
      tests=[dict(i='Alex 2012', o='Alex is 14 years old in 2026'), dict(i='Kapi 2020', o='Kapi is 6 years old in 2026')],
      sol='name, year = input().split()\nprint(f"{name} is {2026 - int(year)} years old in 2026")', hint='name, year = input().split()'))
add('logika',
 dict(opts=['True', 'False', '7', 'Error'], why='(True and False) or True = True.'))
add('while',
 dict(why='The loop runs for n = 3, 2, 1. At 0 the condition is false.'))
add('zagn',
 dict(why='For each i the inner loop goes through all j.'),
 dict(q='Read n and print an n × n multiplication table where each number takes 4 characters, right-aligned (<code>f"{x:4}"</code>).<br>For 2:<br><code>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;2<br>&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;4</code>',
      hint='print(f"{i * j:4}", end="") and print() after each row.'))
add('slice',
 dict(q='Read a date in the format <code>YYYY-MM-DD</code> and print it as <code>DD.MM.YYYY</code> – using slices (no split).', check="assert 'split' not in __src, 'Use slices, no split'",
      hint='Year: d[:4], month: d[5:7], day: d[8:]'))
add('znaki',
 dict(code='''for ch in "cat":
    print(ch.upper())''', opts=['C\nA\nT', 'CAT', 'c\na\nt', 'C A T'], why='Each letter is printed as a capital on a separate line.'),
 dict(q='Read a sentence. Count the vowels (<code>aeiou</code>, any case) and the consonants (other letters). Print <code>vowels: S, consonants: P</code>.',
      tests=[dict(i='Kapi loves water', o='vowels: 6, consonants: 8'), dict(i='Ann', o='vowels: 1, consonants: 2')],
      sol='s = input()\nv = c = 0\nfor ch in s.lower():\n    if ch in "aeiou":\n        v += 1\n    elif ch.isalpha():\n        c += 1\nprint(f"vowels: {v}, consonants: {c}")', hint='isalpha() checks whether a character is a letter.'))
add('listy',
 dict(q='Read numbers. Print the list of running totals: element i is the sum of the first i+1 numbers.<br><code>1 2 3 4</code> → <code>[1, 3, 6, 10]</code>', hint='Keep a running sum and append it to a new list.'),
 dict(q='Rotate a list k places to the right. First line: the numbers, second: k (it may be larger than the list length).<br><code>1 2 3 4 5</code>, k=2 → <code>4 5 1 2 3</code>',
      hint='k %= len(t), then slices t[n-k:] + t[:n-k].'))
add('krotki',
 dict(code='''point = (2, 5)
x, y = point
print(y)''', opts=['5', '2', '(2, 5)', 'Error'], why='Unpacking: x = 2, y = 5.'),
 dict(q='Read two lines of numbers. Print, in ascending order, the numbers that appear in only one of them (symmetric difference <code>^</code>).'),
 dict(q='Read n, then n points <code>x y</code>. Print the point closest to (0, 0) as a tuple.', hint='Compare x*x + y*y – no square root needed.'))
add('domyslne',
 dict(opts=['6', '1', '5', 'Error'], why='b takes its default value 5.'),
 dict(why='Without an argument the default value is used.'),
 dict(q='Write a function <code>column(n, width=3, fill=" ")</code> that returns the numbers 1..n joined into one string, each right-aligned in <code>width</code> characters and padded with <code>fill</code>.<br><code>column(3)</code> → <code>"  1  2  3"</code>, <code>column(3, 2, "0")</code> → <code>"010203"</code>',
      start='def column(n, width=3, fill=" "):\n    \n', check="assert column(3) == '  1  2  3'\nassert column(3, 2, '0') == '010203'\nassert column(1, 1) == '1'",
      sol='def column(n, width=3, fill=" "):\n    return "".join(str(i).rjust(width, fill) for i in range(1, n + 1))', hint='str(i).rjust(width, fill)'))
add('zasieg',
 dict(code='''x = 10
def show():
    print(x)
show()''', opts=['10', 'Error', 'None', 'x'], why='A function can read a global variable.'),
 dict(q='Where can you use a variable created inside a function?', opts=['Only inside that function', 'In the whole program', 'In every function', 'Nowhere'],
      why='A local variable exists only while the function runs.'),
 dict(opts=['5', '6', 'Error', 'None'], why='The function changes its local copy of n, and the returned result was not saved.'))
add('moduly',
 dict(q='Read the radius r (float). Print the circumference and the area of the circle (use <code>math.pi</code>) rounded up (<code>math.ceil</code>): <code>circumference: X, area: Y</code>.',
      tests=[dict(i='1', o='circumference: 7, area: 4'), dict(i='2.5', o='circumference: 16, area: 20')],
      sol='import math\nr = float(input())\nprint(f"circumference: {math.ceil(2 * math.pi * r)}, area: {math.ceil(math.pi * r * r)}")', hint='math.ceil(2 * math.pi * r)'))
add('try',
 dict(opts=['A', 'B', 'A\nB', 'nothing'], why='There was no error, so except does not run.'))
add('pliki',
 dict(q='The file <code>data.txt</code> contains numbers separated by spaces on several lines. Write the sum of each line (one per line) to <code>sums.txt</code> and print the contents of <code>sums.txt</code>.',
      setup="open('data.txt','w').write('1 2 3\\n10 20\\n5\\n')", check="assert open('sums.txt').read().split() == ['6', '30', '5'], 'Check sums.txt'",
      sol='with open("data.txt") as f, open("sums.txt", "w") as g:\n    for l in f:\n        g.write(str(sum(int(x) for x in l.split())) + "\\n")\nprint(open("sums.txt").read().strip())',
      hint='Read line by line, write the sum to the second file.'))
add('suma',
 dict(why='This is finding the minimum.'),
 dict(q='Fill in the summing step', why='s += x adds x to the sum.'),
 dict(q='Read grades (1–6) on one line. Print <code>average: X.XX, most common: Y</code> (on a tie – the higher grade). No sum() or count().',
      tests=[dict(i='5 4 5 3 6 4', o='average: 4.50, most common: 5'), dict(i='2', o='average: 2.00, most common: 2')], check="assert 'sum(' not in __src and 'count(' not in __src, 'No sum() or count()'",
      sol='t = [int(x) for x in input().split()]\ns = 0\nn = [0] * 7\nfor x in t:\n    s += x\n    n[x] += 1\nbest = 1\nfor g in range(1, 7):\n    if n[g] >= n[best]:\n        best = g\nprint(f"average: {s / len(t):.2f}, most common: {best}")',
      hint='A list of counters n[grade] and a loop over grades 1–6.'))
add('szukanie',
 dict(why='index returns the position of the first occurrence.'),
 dict(opts=['False', 'True', '1', 'Error'], why='Letter case matters – "Kapi" ≠ "kapi".'),
 dict(q='Read numbers. Print the indexes of <b>all</b> occurrences of the largest number, separated by spaces (no max or index).', hint='First find the maximum, then collect its indexes.'))
add('babel',
 dict(q='What does the line <code>t[j], t[j + 1] = t[j + 1], t[j]</code> do?', opts=['Swaps neighbouring elements', 'Removes an element', 'Sorts the whole list', 'Copies the list'],
      why='It swaps two values in one step.'),
 dict(q='The list <code>[1, 2, 3]</code> is already sorted. How many swaps will bubble sort make?', why='No pair of neighbours is in the wrong order.'))
add('rekur',
 dict(why='Each call adds 1: f(3) = 1 + 1 + 1 + 0.'))
