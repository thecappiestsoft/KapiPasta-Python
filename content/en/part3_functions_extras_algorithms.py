# KapiPasta - Python: English overrides merged onto content/pl (same order of examples/tasks).
# After editing run: python3 tools/build.py

CHAPTERS = {
 'funkcje': dict(name=dict(rpg='Forge of Functions', space='Robot Factory', neutral='Functions'), topic='def, parameters, return, scope'),
 'rozsz': dict(name=dict(rpg="Alchemist's Tower", space='Laboratory', neutral='Extras'), topic='random, math, try/except, files'),
 'algorytmy': dict(name=dict(rpg='Dragon Mountain of Algorithms', space='Black Hole of Algorithms', neutral='Algorithms'), topic='classic algorithms, errors, recursion'),
}
LESSONS = {}

LESSONS['def'] = dict(title='Definition, parameters, return',
 theory="""<p>A <b>function</b> is a named piece of code you can call many times. Create it with <code>def</code>:</p>
<pre>def greet(name):
    print(f"Hey, {name}!")</pre>
<p><code>name</code> is a <b>parameter</b> – the input data. <code>return</code> hands the result back and ends the function.</p>""",
 more="""<p>A function without <code>return</code> returns <code>None</code>. The difference: <code>print</code> only shows the result on screen, while <code>return</code> lets you use it further, e.g. <code>x = area(2, 3) + 1</code>. A function can return several values as a tuple: <code>return a, b</code>.</p>""",
 ex=[
  dict(code='''def area(a, b):
    return a * b

result = area(3, 4)
print("Pool area:", result)
print(area(2, 5) + 1)''',
       scene=dict(s='machine', name='area(a, b)', inp=['3', '4'], out='12', cap="A function is Kapi's machine: you drop in the parameters 3 and 4, turn the crank, and return spits out 12.")),
  dict(code='''def greet(name):
    print(f"Hey, {name}!")

greet("Bobo")
greet("Lulu")
x = greet("Mimi")
print(x)''',
       scene=dict(s='machine', name='greet(name)', inp=['"Bobo"'], out='None', cap="This machine only shouts a greeting (print). It doesn't spit anything out, so it returns None.")),
 ],
 tasks=[
  dict(q='What will the program print?', code='''def double(x):
    return x * 2

print(double(5))''', why='The function returns 5 * 2.'),
  dict(q='What will the program print?', why='Arguments go into the parameters in order: a = 2, b = 7.'),
  dict(q='Fill in the keyword that creates a function', code='''___ hey():
    print("Hey!")
hey()''', expect='Hey!', why='A function is created with the keyword def.'),
  dict(q='Fill in the gap so the function hands back the result', code='''def add(a, b):
    ___ a + b
print(add(2, 3))''', why='return passes the result out of the function.'),
  dict(q='The program raises an error. Click the buggy line.', code='''def square(x):
    return x * x

print(square())''', fix='print(square(4))', why='The function needs the parameter x, but it was called without an argument: TypeError.'),
  dict(q='What will the program print?', why='f prints 4, but has no return – it returns None.'),
  dict(q='What will the program print?', code='''def f(n):
    if n > 0:
        return "plus"
    return "not plus"
    print("end")

print(f(3))''', opts=['plus', 'plus\nend', 'not plus', 'end'], why='return ends the function immediately.'),
  dict(q='Write a function <code>perimeter(a, b)</code> that returns the perimeter of a rectangle with sides a and b.',
       start='def perimeter(a, b):\n    \n', check="assert perimeter(2, 3) == 10, 'perimeter(2, 3) should give 10'\nassert perimeter(5, 5) == 20, 'perimeter(5, 5) should give 20'",
       sol='def perimeter(a, b):\n    return 2 * a + 2 * b'),
  dict(q='Write a function <code>is_even(n)</code> that returns <code>True</code> for even numbers and <code>False</code> for odd ones.',
       start='def is_even(n):\n    \n', check="assert is_even(4) is True, 'is_even(4) should return True'\nassert is_even(7) is False, 'is_even(7) should return False'\nassert is_even(0) is True",
       sol='def is_even(n):\n    return n % 2 == 0'),
  dict(q='Write a function <code>min_max(t)</code> that returns a tuple (smallest, largest) element of a list – without min() and max().',
       check="assert min_max([3, 9, -2, 5]) == (-2, 9), 'For [3, 9, -2, 5] the result is (-2, 9)'\nassert min_max([7]) == (7, 7)\nimport re\nassert not re.search(r'(?<!_)\\b(min|max)\\(', __src), 'No min() or max()'",
       hint='Start with a = b = t[0] and compare in a loop.'),
 ])

LESSONS['domyslne'] = dict(title='Default parameters',
 theory="""<p>A parameter can have a <b>default value</b> – used when no argument is given:</p>
<pre>def greet(name, mark="!"):
    print("Hey, " + name + mark)</pre>
<p><code>greet("Kapi")</code> → Hey, Kapi! &nbsp; <code>greet("Kapi", "?")</code> → Hey, Kapi?</p>""",
 more="""<p>Parameters with default values must come <b>last</b>. Arguments can be given by name: <code>f(b=2, a=1)</code>. You already know this: <code>print(..., sep="-", end="")</code> uses default parameters!</p>""",
 ex=[
  dict(code='''def order(fruit, n=1):
    print(f"Kapi orders {n} x {fruit}")

order("melon")
order("pear", 3)
order(n=2, fruit="apple")''',
       scene=dict(s='machine', name='order(fruit, n=1)', inp=['"melon"', '(1)'], out='1 x melon', cap="When Kapi doesn't say how many he wants, the waiter brings 1 by default.")),
 ],
 tasks=[
  dict(q='What will the program print?', code='''def power(x, n=2):
    return x ** n

print(power(3), power(2, 3))''', why='power(3) uses n = 2, power(2, 3) is 2 ** 3.'),
  dict(q='Fill in the default value so calling without an argument prints “Hey, Kapi”', code='''def hey(name=___):
    print("Hey,", name)
hey()''', expect='Hey, Kapi', why='The default value goes after the = sign in the brackets.'),
  dict(q='What will the program print?', code='''def hey(name, mark="!"):
    print("Hey, " + name + mark)

hey("Bobo", "?")''', opts=['Hey, Bobo?', 'Hey, Bobo!', 'Hey, Bobo!?', 'Hey, Bobo'], why='The given argument "?" replaces the default value "!".'),
  dict(q='The program raises a syntax error. Click the buggy line.', why='Parameters with a default value must come after those without one.'),
  dict(q='What will the program print?', why='a = 1, b defaults to 10, c given by name = 5.'),
  dict(q='Write a function <code>line(n, char="-")</code> that <b>returns</b> a string of n characters.<br><code>line(3)</code> → <code>"---"</code>, <code>line(2, "*")</code> → <code>"**"</code>',
       start='def line(n, char="-"):\n    \n', check="assert line(3) == '---', 'line(3) should give ---'\nassert line(2, '*') == '**'\nassert line(0) == ''",
       sol='def line(n, char="-"):\n    return char * n', hint='return char * n'),
 ])

LESSONS['zasieg'] = dict(title='Variable scope',
 theory="""<p>Variables created <b>inside</b> a function are <b>local</b> – they exist only while it runs and can't be seen outside.</p>
<p>Variables created outside functions are <b>global</b> – a function can read them.</p>
<p>If a function assigns to a variable with the same name, it creates a <b>new, local</b> variable – the global one doesn't change.</p>""",
 more="""<p>To change a global variable inside a function, you must write <code>global name</code>. It's better, though, to pass data through parameters and give it back with <code>return</code> – the code is clearer. A common error: reading a variable before its local assignment → <code>UnboundLocalError</code>.</p>""",
 ex=[
  dict(code='''fruits = 10          # global

def picnic():
    fruits = 2       # local – a different variable!
    print("in the tent:", fruits)

picnic()
print("at home:", fruits)''',
       scene=dict(s='scope', glob=[['fruits', '10']], loc=[['fruits', '2']], fn='picnic()', cap="Kapi has 10 fruits at home (global). For the picnic in the tent (function) he takes a separate basket with 2 fruits. The home supply doesn't change.")),
  dict(code='''counter = 0

def add():
    global counter
    counter += 1

add()
add()
print(counter)''',
       scene=dict(s='scope', glob=[['counter', '0 → 2']], loc=[], fn='add()', cap='The global keyword lets Kapi reach from the tent to the counter at home and change it.')),
 ],
 tasks=[
  dict(q='What will the program print?', opts=['5', '100', 'Error', 'None'], why='x = 100 in the function creates a local variable. The global x is still 5.'),
  dict(q='What will the program print?', opts=['10', '5', 'Error', 'None'], why='A function can read a global variable.'),
  dict(q='The program raises an error. Click the buggy line.', code='''def f():
    secret = 42
f()
print(secret)''', fix='The function should return secret (return), and the result of f() should be saved.',
       why="secret is a local variable of f – it doesn't exist outside: NameError."),
  dict(q='What will the program print?', opts=['21', '11', '1', 'Error'], why='global lets you change a global variable. Two calls add 10 + 10.'),
  dict(q='The program raises an error. Click the line where Python detected it.', code='''points = 0
def score():
    points = points + 1
score()''', fix='    global points  (add it in the function before this line)',
       why='Assigning in the function makes points local – and it is read before it gets a value: UnboundLocalError.'),
  dict(q='Fix the function so that it <b>returns</b> the new score instead of changing a global variable. The function <code>add_points(p, n)</code> should return p + n.',
       start='def add_points(p, n):\n    \n\nscore = 0\nscore = add_points(score, 5)\nprint(score)\n', check="assert add_points(10, 3) == 13\nassert 'global' not in __src, 'No global!'",
       sol='def add_points(p, n):\n    return p + n\n\nscore = 0\nscore = add_points(score, 5)\nprint(score)', hint='return p + n'),
 ])

LESSONS['moduly'] = dict(title='The random and math modules',
 theory="""<p>A <b>module</b> is a ready-made set of functions. Load it with <code>import</code>:</p>
<ul><li><code>import random</code> → <code>random.randint(1, 6)</code> – a random whole number from 1 to 6 (inclusive!), <code>random.choice(list)</code> – a random element, <code>random.shuffle(list)</code> – shuffling</li>
<li><code>import math</code> → <code>math.sqrt(16)</code> – square root, <code>math.pi</code>, <code>math.floor()</code> / <code>math.ceil()</code> – round down / up</li></ul>""",
 more="""<p>You can import chosen functions: <code>from math import sqrt</code> – then you just write <code>sqrt(16)</code>. <code>random.random()</code> gives a number in [0, 1). <code>random.seed(1)</code> makes the “random” draw repeatable – handy for testing.</p>""",
 ex=[
  dict(code='''import random
roll = random.randint(1, 6)
print("Kapi rolled:", roll)
snack = random.choice(["melon", "pear", "grass"])
print("Today's lunch:", snack)''',
       scene=dict(s='dice', cap='Kapi rolls a die and draws his lunch. Each run may give a different result – click the die!')),
  dict(code='''import math
print(math.sqrt(49))
print(math.floor(3.7), math.ceil(3.2))
print(round(math.pi, 3))''',
       scene=dict(s='cards', items=[['math.sqrt(49)', '7.0', 'square root'], ['math.floor(3.7)', '3', 'down'], ['math.ceil(3.2)', '4', 'up'], ['round(math.pi, 3)', '3.142', 'pi']], cap='Kapi uses a scientific calculator instead of counting on his paws.')),
 ],
 tasks=[
  dict(q='Which numbers can <code>random.randint(1, 3)</code> return?', opts=['1, 2 or 3', '1 or 2', '0, 1, 2 or 3', 'only 1 and 3'], why='randint includes both ends of the range – unlike range.'),
  dict(q='What will the program print?', why='sqrt always returns a float, so 9.0.'),
  dict(q='Fill in the gap to load the module', why='Modules are loaded with the import statement.'),
  dict(q='The program raises an error. Click the buggy line.', why='After import math you must write math.sqrt. Plain sqrt is unknown: NameError.'),
  dict(q='What will the program print?', why='ceil(3.5) = 4; floor rounds down, so -1.5 → -2.'),
  dict(q='Simulate rolling two dice: draw two numbers 1–6 and print their sum.',
       check="import re\nassert 'randint' in __src, 'Use random.randint'\nv = int(__out.strip().split()[-1])\nassert 2 <= v <= 12, 'The sum must be between 2 and 12'"),
  dict(q='Read the legs a and b of a right triangle (whole numbers). Print the length of the hypotenuse rounded to 2 places (use <code>math.sqrt</code>).'),
  dict(q='“Guess the number” game: the number <code>secret</code> (1–100) has already been drawn. Keep reading guesses and print <code>too low</code> / <code>too high</code> until the user guesses it – then print <code>Bravo! Guesses: N</code>.',
       start='import random\nrandom.seed(7)\nsecret = random.randint(1, 100)\n', tests=[dict(i='50\n25\n42', o='too high\ntoo low\nBravo! Guesses: 3')],
       sol='import random\nrandom.seed(7)\nsecret = random.randint(1, 100)\nguesses = 0\nwhile True:\n    x = int(input())\n    guesses += 1\n    if x < secret:\n        print("too low")\n    elif x > secret:\n        print("too high")\n    else:\n        print(f"Bravo! Guesses: {guesses}")\n        break',
       hint='while True with a guess counter and break after a hit. (Thanks to seed(7) the secret number in the test is always the same.)'),
 ])

LESSONS['try'] = dict(title='Error handling: try/except',
 theory="""<p>When something goes wrong (e.g. someone types “abc” instead of a number), the program crashes. <code>try/except</code> lets you catch the error and react:</p>
<pre>try:
    n = int(input())
except ValueError:
    print("That's not a number!")</pre>
<p>The code in <code>try</code> is “attempted”. If an error appears, Python jumps to <code>except</code>.</p>""",
 more="""<p>You can catch several types: <code>except (ValueError, ZeroDivisionError):</code>, and even keep the error: <code>except ValueError as e:</code>. The <code>else</code> block runs if there was no error, and <code>finally</code> – always. A typical pattern: <code>while True</code> + <code>try</code> + <code>break</code> – keep asking until the data is correct.</p>""",
 ex=[
  dict(code='''text = input("How many melons? ")
try:
    n = int(text)
    print("Kapi will eat", n, "melons")
except ValueError:
    print("Hey, that's not a number! 🙈")''', inp='lots',
       scene=dict(s='err', err='ValueError: invalid literal for int()', caught=True, cap='Kapi holds the try/except shield. The error bounces off it instead of crashing the program.')),
  dict(code='''while True:
    try:
        x = int(input("Enter a number: "))
        print(10 / x)
        break
    except ValueError:
        print("Not a number")
    except ZeroDivisionError:
        print("Don't divide by zero!")''', inp='abc\n0\n4',
       scene=dict(s='err', err='ZeroDivisionError: division by zero', caught=True, cap='Kapi keeps asking: each bad idea bounces off the shield until the data is finally good.')),
 ],
 tasks=[
  dict(q='What will the program print?', code='''try:
    x = int("12a")
    print("OK")
except ValueError:
    print("Error")''', opts=['Error', 'OK', 'OK\nError', '12'], why='int("12a") raises ValueError, so print("OK") does not run.'),
  dict(q='Which error does <code>10 / 0</code> raise?', why='Division by zero is ZeroDivisionError.'),
  dict(q='Fill in the word that catches the error', code='''try:
    print(1 / 0)
___ ZeroDivisionError:
    print("Not allowed!")''', expect='Not allowed!', why='Errors are caught in the except block.'),
  dict(q='What will the program print?', opts=['B', 'A', 'A\nB', 'Error'], why='t[5] raises IndexError – the second except catches it.'),
  dict(q='What will the program print?', why='There was no error, so else runs, and finally always runs.'),
  dict(q='Read some text. If it is a whole number, print it doubled. If not – print <code>Not a number</code>.',
       tests=[dict(i='21', o='42'), dict(i='kapi', o='Not a number')], sol='s = input()\ntry:\n    print(int(s) * 2)\nexcept ValueError:\n    print("Not a number")', hint='try: print(int(s) * 2) except ValueError: …'),
  dict(q='Keep reading text until the user gives a correct whole number. After each bad attempt print <code>Try again</code>. At the end print <code>OK: number</code>.',
       tests=[dict(i='abc\n3.5\n7', o='Try again\nTry again\nOK: 7'), dict(i='5', o='OK: 5')], sol='while True:\n    try:\n        n = int(input())\n        break\n    except ValueError:\n        print("Try again")\nprint(f"OK: {n}")'),
  dict(q='Read two lines: a and b. Print a / b rounded to 2 places. If the data is not numbers, print <code>Bad data</code>, and for division by zero – <code>Division by zero</code>.',
       tests=[dict(i='7\n2', o='3.5'), dict(i='1\n0', o='Division by zero'), dict(i='x\n2', o='Bad data')],
       sol='try:\n    a = float(input())\n    b = float(input())\n    print(round(a / b, 2))\nexcept ValueError:\n    print("Bad data")\nexcept ZeroDivisionError:\n    print("Division by zero")', hint='Two except blocks.'),
 ])

LESSONS['pliki'] = dict(title='Files: open, with',
 theory="""<p>Open a file with <code>open(name, mode)</code>. Modes: <code>"r"</code> – read, <code>"w"</code> – write (erases the old content!), <code>"a"</code> – append at the end.</p>
<p>It's best to use <code>with</code> – the file closes itself:</p>
<pre>with open("diary.txt", "w") as f:
    f.write("Kapi went swimming\\n")</pre>
<p>💡 In this app files are created in a virtual folder in the browser.</p>""",
 more="""<p>Reading: <code>f.read()</code> – the whole text, <code>f.readlines()</code> – a list of lines, or <code>for line in f:</code> – line by line (each ends with <code>\\n</code>, so <code>strip()</code> comes in handy). For special characters add <code>encoding="utf-8"</code>. A missing file when reading → <code>FileNotFoundError</code>.</p>""",
 ex=[
  dict(code='''with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("Monday: swimming\\n")
    f.write("Tuesday: melon\\n")

with open("diary.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())''',
       scene=dict(s='file', name='diary.txt', lines=['Monday: swimming', 'Tuesday: melon'], cap='Kapi writes a diary on a scroll (mode "w"), then reads it line by line.')),
  dict(code='''with open("scores.txt", "w") as f:
    for p in [5, 8, 3]:
        f.write(f"{p}\\n")

total = 0
with open("scores.txt") as f:
    for line in f:
        total += int(line)
print("Total points:", total)''',
       scene=dict(s='file', name='scores.txt', lines=['5', '8', '3'], cap='Kapi writes down his swimming contest scores and then adds them up.')),
 ],
 tasks=[
  dict(q='Which mode <b>erases</b> the old content of a file?', opts=['"w"', '"r"', '"a"', 'none'], why='"w" creates the file from scratch. "a" is for appending.'),
  dict(q='Why do we use <code>with open(...) as f:</code>?', opts=['The file closes itself after leaving the block', 'The file opens faster', 'Without with you cannot read a file', 'To save the file in the cloud'],
       why='with closes the file automatically, even when an error occurs.'),
  dict(q='Fill in the mode to <b>append</b> a line at the end of the file', why='Mode "a" (append) adds at the end.'),
  dict(q='What will the program print?', code='''with open("t.txt", "w") as f:
    f.write("anna\\nhas\\ncats\\n")
with open("t.txt") as f:
    print(len(f.readlines()))''', opts=['3', '1', '13', '14'], why='The file has 3 lines.'),
  dict(q='The program raises an error. Click the buggy line.', code='''with open("plan.txt", "w") as f:
    f.write("swimming")
with open("plan.txt", "r") as f:
    f.write("nap")''', fix='with open("plan.txt", "a") as f:  (on line 3)',
       why='The file was opened in mode "r" (read only), so write raises io.UnsupportedOperation.'),
  dict(q='Write three lines to the file <code>fruits.txt</code>: <code>melon</code>, <code>pear</code>, <code>apple</code>. Then read the file and print its contents.',
       tests=[dict(i='', o='melon\npear\napple')], check="assert open('fruits.txt', encoding='utf-8').read().split() == ['melon', 'pear', 'apple'], 'fruits.txt has the wrong contents'",
       sol='with open("fruits.txt", "w", encoding="utf-8") as f:\n    f.write("melon\\npear\\napple\\n")\nwith open("fruits.txt", encoding="utf-8") as f:\n    print(f.read().strip())',
       hint='First with open(..., "w"), then with open(...) and print(f.read()).'),
  dict(q='The file <code>numbers.txt</code> already exists – each line holds a whole number. Print the largest of them.',
       setup="open('numbers.txt','w').write('4\\n17\\n-3\\n9\\n')", sol='with open("numbers.txt") as f:\n    t = [int(l) for l in f]\nprint(max(t))', hint='Read the lines, convert to int, find the largest.'),
  dict(q='The file <code>grades.txt</code> has lines <code>name grade</code>. Write to <code>averages.txt</code> and print on screen the average of each person (2 places), in order of first appearance: <code>Kapi 4.50</code>.',
       setup="open('grades.txt','w').write('Kapi 5\\nBobo 3\\nKapi 4\\nBobo 4\\nLulu 6\\n')",
       check="assert open('averages.txt').read().split() == ['Kapi', '4.50', 'Bobo', '3.50', 'Lulu', '6.00'], 'Check averages.txt'",
       sol='d = {}\nwith open("grades.txt") as f:\n    for l in f:\n        name, g = l.split()\n        d.setdefault(name, []).append(int(g))\nwith open("averages.txt", "w") as f:\n    for name, t in d.items():\n        w = f"{name} {sum(t) / len(t):.2f}"\n        print(w)\n        f.write(w + "\\n")',
       hint='A dictionary name → list of grades.'),
 ])

LESSONS['suma'] = dict(title='Sum, average, min/max',
 theory="""<p>Classic algorithms “by hand”, without the built-in <code>sum</code>, <code>min</code>, <code>max</code>:</p>
<ul><li><b>Sum</b>: start with <code>s = 0</code>, add the elements in a loop.</li><li><b>Average</b>: sum / number of elements.</li><li><b>Maximum</b>: assume the first element is the largest, then compare it with each next one.</li></ul>""",
 more="""<p>For the maximum, don't start with <code>m = 0</code> – with only negative numbers the result would be wrong! Start with the first element. You can also remember the position (index) of the maximum at the same time.</p>""",
 ex=[
  dict(code='''melons = [4, 9, 2, 7]
s = 0
for x in melons:
    s += x
print("Sum:", s)
print("Average:", s / len(melons))''',
       scene=dict(s='loop', items=['4', '9', '2', '7'], acc='s', accv=[4, 13, 15, 22], cap='Kapi weighs the melons and puts each one on the big scale.')),
  dict(code='''t = [4, 9, 2, 7]
m = t[0]
for x in t:
    if x > m:
        m = x
print("Largest:", m)''',
       scene=dict(s='loop', items=['4', '9', '2', '7'], acc='m', accv=[4, 9, 9, 9], cap='Kapi holds the heaviest melon so far. When he finds a heavier one – he swaps.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='The sum is 10, divided by 3 elements.'),
  dict(q='Fill in the condition for finding the minimum', why='When looking for the minimum, we swap when we find a smaller element.'),
  dict(q='The program should find the largest number, but for this list it prints 0. Click the buggy line.', why='Starting from 0 breaks the result for negative numbers. Start with the first element.'),
  dict(q='Read numbers on one line. Print their sum – <b>without</b> the <code>sum</code> function.', check="assert 'sum(' not in __src, 'No sum function!'"),
  dict(q='Read numbers on one line. Print the smallest and the largest (separated by a space) – <b>without</b> <code>min</code>/<code>max</code>/<code>sort</code>.',
       check="assert 'min(' not in __src and 'max(' not in __src and 'sort' not in __src, 'No min, max or sort!'"),
  dict(q='Read numbers. Print the <b>index</b> of the first occurrence of the largest number (without max and index).', hint='Remember the index k instead of the value.'),
 ])

LESSONS['szukanie'] = dict(title='Counting and linear search',
 theory="""<p><b>Counting</b>: a counter <code>count = 0</code> and <code>count += 1</code> every time an element meets the condition.</p>
<p><b>Linear search</b>: we check the elements one by one until we find the one we want. If we reach the end – it isn't there. We usually return the index or <code>-1</code>.</p>""",
 more="""<p>In the worst case we check all n elements – that's linear complexity O(n). For sorted data there is the faster binary search. Built-in shortcuts: <code>t.count(x)</code>, <code>x in t</code>, <code>t.index(x)</code>.</p>""",
 ex=[
  dict(code='''def search(t, target):
    for i in range(len(t)):
        if t[i] == target:
            return i
    return -1

burrows = ["Bobo", "Lulu", "Kapi", "Mimi"]
print(search(burrows, "Kapi"))
print(search(burrows, "Zuzu"))''',
       scene=dict(s='search', items=['Bobo', 'Lulu', 'Kapi', 'Mimi'], target='Kapi', cap='We look for Kapi by peeking into the burrows one by one. Found in burrow no. 2!')),
 ],
 tasks=[
  dict(q='What will the program print?', code='''t = [3, 7, 3, 1, 3]
count = 0
for x in t:
    if x == 3:
        count += 1
print(count)''', why='The number 3 appears three times.'),
  dict(q='How many comparisons will linear search make in the worst case for a list of 100 elements?', why='In the worst case we check all the elements.'),
  dict(q='The function should return the index or -1, but for [5, 8, 2] and target = 2 it returns -1. Click the buggy line.', code='''def search(t, target):
    for i in range(len(t)):
        if t[i] == target:
            return i
        return -1''', fix='    return -1  (indented at the level of the for loop, not the if)',
       why='return -1 is inside the loop, so the function ends after the first element.'),
  dict(q='Read numbers on one line. Print how many of them are even.', sol='t = [int(x) for x in input().split()]\ncount = 0\nfor x in t:\n    if x % 2 == 0:\n        count += 1\nprint(count)', hint='if x % 2 == 0: count += 1'),
  dict(q='Write a function <code>search(t, target)</code> returning the index of the first occurrence of target, or -1 (without <code>index</code>).',
       start='def search(t, target):\n    \n', check="assert search([4, 2, 7, 2], 2) == 1\nassert search([4, 2], 9) == -1, 'Return -1 when the element is missing'\nassert search([], 1) == -1\nassert '.index' not in __src",
       sol='def search(t, target):\n    for i in range(len(t)):\n        if t[i] == target:\n            return i\n    return -1', hint='return -1 only after the loop!'),
  dict(q='Read numbers. Print the length of the longest run of consecutive <b>equal</b> numbers. E.g. <code>1 1 2 2 2 1</code> → <code>3</code>.', hint='A counter for the current run and the best run.'),
 ])

LESSONS['babel'] = dict(title='Bubble sort',
 theory="""<p>Bubble sort compares <b>neighbouring</b> elements and swaps them if they are in the wrong order. After each pass the largest element “floats up” to the end – like a bubble!</p>
<pre>for i in range(n - 1):
    for j in range(n - 1 - i):
        if t[j] > t[j + 1]:
            t[j], t[j + 1] = t[j + 1], t[j]</pre>""",
 more="""<p>Complexity: about n² comparisons – slow for big data. Improvement: if a pass made no swaps, the list is sorted and you can stop (<code>break</code>). Changing <code>&gt;</code> to <code>&lt;</code> sorts in descending order.</p>""",
 ex=[
  dict(scene=dict(s='sort', arr=[5, 3, 8, 1], cap='Capybaras of different heights line up. Kapi compares neighbours and swaps them. Press ▶!')),
 ],
 tasks=[
  dict(q='What does bubble sort compare?', opts=['Neighbouring elements', 'The first with the last', 'Each element with the average', 'Random pairs'], why='We always compare t[j] with t[j + 1].'),
  dict(q='What does the list <code>[4, 1, 3, 2]</code> look like after the <b>first</b> pass of bubble sort?', why='The four “floats” to the end, the rest move one place.'),
  dict(q='Where does the largest element end up after the first pass of bubble sort (ascending)?', opts=['At the end of the list', 'At the start of the list', 'In the middle of the list', 'It stays in place'],
       why='The largest element gets pushed along at every comparison until it “floats up” to the end.'),
  dict(q='Fill in the swap of two elements', why='In Python a swap is a, b = b, a.'),
  dict(q='The program raises an error. Click the buggy line.', fix='    for j in range(len(t) - 1 - i):  (the range on line 3)',
       why='When j reaches the last index, t[j + 1] goes outside the list: IndexError. The range of the j loop should be 1 smaller.'),
  dict(q='Read numbers and bubble sort them in <b>ascending</b> order (no <code>sort</code>/<code>sorted</code>). Print them separated by spaces.',
       check="assert 'sort' not in __src, 'No sort or sorted!'", hint='Two loops and swapping neighbours.'),
  dict(q='Bubble sort in <b>descending</b> order and print how many swaps were made.<br>Input: numbers on one line. Output: the sorted numbers, and the number of swaps on the second line.',
       hint='Flip the comparison sign and count the swaps.'),
 ])

LESSONS['nwd'] = dict(title='GCD, primes, palindromes',
 theory="""<p><b>GCD</b> (Euclid's algorithm): while b ≠ 0, do <code>a, b = b, a % b</code>. At the end, a is the GCD.</p>
<p>A <b>prime number</b> has exactly two divisors: 1 and itself. We check divisors from 2 to √n.</p>
<p>A <b>palindrome</b> reads the same forwards and backwards: <code>s == s[::-1]</code>.</p>""",
 more="""<p>The LCM comes from the GCD: <code>lcm = a * b // gcd(a, b)</code>. For primality it's enough to check divisors d with <code>d * d &lt;= n</code> – if n had a bigger divisor, it would also have a smaller one. For sentence palindromes, first remove spaces and make letters lowercase.</p>""",
 ex=[
  dict(code='''def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))''',
       scene=dict(s='cards', items=[['a=48, b=18', '48 % 18 = 12', ''], ['a=18, b=12', '18 % 12 = 6', ''], ['a=12, b=6', '12 % 6 = 0', ''], ['a=6, b=0', 'GCD = 6', 'done!']], cap='Kapi has 48 melons and 18 pears and wants to pack identical baskets. Euclid says: 6 baskets!')),
  dict(code='''def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print([x for x in range(2, 30) if is_prime(x)])''',
       scene=dict(s='row', items=['2', '3', '5', '7', '11', '13', '17', '19', '23', '29'], label='primes < 30', cap="Kapi checks whether a pile of fruit can be split into equal heaps. For primes it can't!")),
  dict(code='''for s in ["kayak", "kapi", "level"]:
    print(s, s == s[::-1])''',
       scene=dict(s='row', items=list('KAYAK'), label='kayak = kayak[::-1]', cap='Kapi paddles a kayak: the same name from the front and from the back!')),
 ],
 tasks=[
  dict(q='Which number is prime?', why='13 is divisible only by 1 and 13. The number 1 is not prime.'),
  dict(q='What will the program print?', why='"level" backwards is still "level".'),
  dict(q='What will the program print?', why='(20, 8) → (8, 4) → (4, 0). GCD = 4.'),
  dict(q="Fill in the step of Euclid's algorithm", why='The new b is the remainder of a divided by b.'),
  dict(q='The function thinks 9 is a prime. Click the buggy line.', code='''def is_prime(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return False
        d += 1
    return True''', fix='    while d * d <= n:', why='For n = 9 the condition 3 * 3 < 9 is false, so the divisor 3 is never checked. We need <=.'),
  dict(q='Read a word and print <code>YES</code> if it is a palindrome, otherwise <code>NO</code>.',
       tests=[dict(i='kayak', o='YES'), dict(i='kapi', o='NO'), dict(i='a', o='YES')], sol='s = input()\nif s == s[::-1]:\n    print("YES")\nelse:\n    print("NO")'),
  dict(q="Write a function <code>gcd(a, b)</code> using Euclid's algorithm (without the math module).",
       start='def gcd(a, b):\n    \n', check="assert gcd(48, 18) == 6\nassert gcd(7, 5) == 1\nassert gcd(10, 100) == 10\nassert 'math' not in __src, 'No math.gcd!'",
       sol='def gcd(a, b):\n    while b != 0:\n        a, b = b, a % b\n    return a'),
  dict(q='Write a function <code>is_prime(n)</code> returning True/False. Watch out for 0, 1 and 2!',
       start='def is_prime(n):\n    \n', check="assert [x for x in range(30) if is_prime(x)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Check the numbers 0–29'\nassert is_prime(97) and not is_prime(91)",
       sol='def is_prime(n):\n    if n < 2:\n        return False\n    d = 2\n    while d * d <= n:\n        if n % d == 0:\n            return False\n        d += 1\n    return True', hint='n < 2 → False; divisors from 2 while d*d <= n.'),
  dict(q='Read a sentence. Check whether it is a palindrome, ignoring spaces and letter case. Print <code>YES</code>/<code>NO</code>.<br>E.g. <code>Never odd or even</code> → YES',
       tests=[dict(i='Never odd or even', o='YES'), dict(i='Kapi loves water', o='NO'), dict(i='Step on no pets', o='YES')],
       sol='s = input().replace(" ", "").lower()\nprint("YES" if s == s[::-1] else "NO")', hint='Remove spaces: replace(" ", ""), then lower().'),
 ])

LESSONS['bledy'] = dict(title='Reading error messages',
 theory="""<p>An error isn't a failure – it's a <b>clue</b>! Python's message tells you:</p>
<ul><li><b>where</b>: <code>line 3</code> – the line number</li><li><b>what</b>: the error type, e.g. <code>NameError</code></li><li><b>why</b>: a description, e.g. <code>name 'x' is not defined</code></li></ul>
<p>The most common ones:</p><ul><li><code>SyntaxError</code> – a typo in the syntax (missing <code>:</code>, bracket, quote)</li><li><code>IndentationError</code> – wrong indentation</li><li><code>NameError</code> – unknown name (a typo?)</li><li><code>TypeError</code> – wrong types, e.g. <code>"2" + 2</code></li><li><code>ValueError</code> – wrong value, e.g. <code>int("abc")</code></li><li><code>IndexError</code> – index outside the list</li><li><code>KeyError</code> – missing dictionary key</li><li><code>ZeroDivisionError</code> – division by 0</li></ul>""",
 more="""<p>Read a traceback <b>from the bottom</b>: the last line is the error type and description, and above it – where it happened. With <code>SyntaxError</code> the real mistake is often one line <b>above</b> (e.g. an unclosed bracket). Logic errors give no message – then control <code>print</code>s help.</p>""",
 ex=[
  dict(code='''age = 4
print("Kapi is " + age + " years old")''',
       scene=dict(s='err', err='TypeError: can only concatenate str (not "int") to str', caught=False, cap='Kapi tries to glue text to a number – and everything falls apart. The message says: you can only join str with str. Fix: str(age) or an f-string.')),
 ],
 tasks=[
  dict(q='Which error does <code>print("a" + 1)</code> raise?', why="You can't add text and a number – that's a type error."),
  dict(q='Which error will this code raise?', code='''name = "Kapi"
print(nmae)''', why='A typo: nmae does not exist.'),
  dict(q='Which error will this code raise?', why='The list has indexes 0–2.'),
  dict(q='Which error will this code raise?', why='A missing dictionary key is a KeyError.'),
  dict(q='Which error will this code raise?', opts=['IndentationError', 'SyntaxError: missing colon', 'NameError', 'TypeError'], why='The function body must be indented.'),
  dict(q='Read the error message and click the buggy line.', fix='Check that b != 0 before dividing.', why='ZeroDivisionError – division by b, which is 0.'),
  dict(q='Read the error message and click the line that needs fixing.', code='''t = [4, 5, 6]
print(sum(t)
print("done")''', why='Unclosed bracket on line 2. Python notices the problem only later – so with a SyntaxError always look at the line above too.'),
  dict(q='This program has an error. Run it, read the message and fix it so it prints <code>Kapi is 4 years old</code>.',
       start='age = 4\nprint("Kapi is " + age + " years old")\n', tests=[dict(i='', o='Kapi is 4 years old')], sol='age = 4\nprint("Kapi is " + str(age) + " years old")',
       hint='Turn the number into text: str(age), or use an f-string.'),
  dict(q='This program has 3 errors. Fix them so it prints the sum of the numbers from 1 to 5: <code>15</code>.',
       start='total = 0\nfor i in range(1, 6)\n    total = total + I\nprint(Total)\n', sol='total = 0\nfor i in range(1, 6):\n    total = total + i\nprint(total)', hint='A colon, letter case, letter case.'),
 ])

LESSONS['rekur'] = dict(title='Recursion',
 theory="""<p><b>Recursion</b> is a function that calls <b>itself</b> for a smaller problem. Every recursive function needs:</p>
<ul><li>a <b>base case</b> – when to stop,</li><li>a <b>recursive step</b> – a call for smaller data.</li></ul>
<pre>def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)</pre>""",
 more="""<p>Without a base case the function calls itself forever → <code>RecursionError</code>. Fibonacci recursively: <code>fib(n) = fib(n-1) + fib(n-2)</code> – beautiful but slow, because the same values are calculated many times. GCD can be recursive too: <code>gcd(a, b) = gcd(b, a % b)</code>.</p>""",
 ex=[
  dict(code='''def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))''',
       scene=dict(s='stack', frames=['factorial(4)', 'factorial(3)', 'factorial(2)', 'factorial(1)', 'factorial(0)'], rets=['24', '6', '2', '1', '1'], cap='Kapi opens nesting dolls: each hides a smaller one. The smallest (factorial(0)) returns 1, and the results travel back up: 1, 1, 2, 6, 24.')),
  dict(code='''def countdown(n):
    if n == 0:
        print("Splash! 💦")
        return
    print(n)
    countdown(n - 1)

countdown(3)''',
       scene=dict(s='stack', frames=['countdown(3)', 'countdown(2)', 'countdown(1)', 'countdown(0)'], rets=['', '', '', 'Splash!'], cap='Kapi walks down the steps into the pool until he reaches the water – that is the base case.')),
 ],
 tasks=[
  dict(q='What must every recursive function have?', opts=['A base case', 'A while loop', 'A global variable', 'A default parameter'], why='Without a base case, recursion would go on forever.'),
  dict(q='What will the program print?', why='4 + 3 + 2 + 1 + 0 = 10.'),
  dict(q='What will the program print?', why='print comes AFTER the recursive call, so the numbers are printed on the way “back” – from the smallest.'),
  dict(q='The program raises an error. Click the line that needs fixing.', code='''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(0))''', why='For n = 0 the condition n == 1 never holds – n goes down to -1, -2, … until RecursionError.'),
  dict(q='Fill in the recursive step of the power function', code='''def power(a, n):
    if n == 0:
        return 1
    return a * ___
print(power(2, 5))''', ans=[['power(a,n-1)', 'power(a, n - 1)', 'power(a, n-1)']], why='aⁿ = a · aⁿ⁻¹'),
  dict(q='Write a recursive function <code>digit_sum(n)</code> (no loops and no converting to text).',
       start='def digit_sum(n):\n    \n', check="assert digit_sum(472) == 13\nassert digit_sum(0) == 0\nassert digit_sum(9) == 9\nassert 'for' not in __src and 'while' not in __src and 'str(' not in __src, 'No loops or str!'",
       sol='def digit_sum(n):\n    if n == 0:\n        return 0\n    return n % 10 + digit_sum(n // 10)', hint='last digit n % 10 + digit_sum(n // 10)'),
  dict(q='Write a recursive function <code>fib(n)</code>: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).', check="assert [fib(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Check the first 10 terms'"),
  dict(q='Write a recursive function <code>reverse(s)</code> that returns the string backwards (without <code>[::-1]</code> and without loops).',
       start='def reverse(s):\n    \n', check="assert reverse('kapi') == 'ipak'\nassert reverse('') == ''\nassert '::-1' not in __src and 'for' not in __src and 'while' not in __src",
       sol='def reverse(s):\n    if s == "":\n        return ""\n    return reverse(s[1:]) + s[0]', hint='reverse(s[1:]) + s[0]'),
 ])
