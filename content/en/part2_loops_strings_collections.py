# KapiPasta - Python: English overrides merged onto content/pl (same order of examples/tasks).
# After editing run: python3 tools/build.py

CHAPTERS = {
 'petle': dict(name=dict(rpg='Whirlpool of Repetition', space='Loop Nebula', neutral='Loops'), topic='for, range, while, break, continue'),
 'teksty': dict(name=dict(rpg='Library of Scrolls', space='Signal Radar', neutral='Strings'), topic='indexes, slices, string methods'),
 'kolekcje': dict(name=dict(rpg='Treasury of Collections', space='Collection Cargo Bay', neutral='Collections'), topic='lists, tuples, sets, dictionaries'),
}
LESSONS = {}

LESSONS['for'] = dict(title='for and range()',
 theory="""<p>A <code>for</code> loop repeats code for each element in turn.</p>
<p><code>range(n)</code> gives the numbers from <b>0 to n-1</b>: <code>range(4)</code> → 0, 1, 2, 3.</p>
<ul><li><code>range(a, b)</code> – from a to b-1</li><li><code>range(a, b, step)</code> – every step, e.g. <code>range(0, 10, 2)</code> → 0, 2, 4, 6, 8</li></ul>""",
 more="""<p>The step can be negative: <code>range(5, 0, -1)</code> → 5, 4, 3, 2, 1. A <code>for</code> loop can also walk through a string or a list. When the loop variable isn't needed, it's called <code>_</code>.</p>""",
 ex=[
  dict(code='''for i in range(4):
    print(f"Kapi eats tangerine no. {i}")''',
       scene=dict(s='loop', items=['🍊', '🍊', '🍊', '🍊'], cap='Kapi walks along a row of tangerines. The counter i goes from 0 to 3. Press ▶ to watch step by step.')),
  dict(code='''for x in range(2, 11, 3):
    print(x)''',
       scene=dict(s='loop', items=['2', '5', '8'], cap='Kapi hops across stones every 3 – starting at 2, but 11 is no longer in the range.')),
  dict(code='''total = 0
for i in range(1, 6):
    total += i
print("Total:", total)''',
       scene=dict(s='loop', items=['1', '2', '3', '4', '5'], acc='total', accv=[1, 3, 6, 10, 15], cap='Kapi drops each number into the “total” basket.')),
 ],
 tasks=[
  dict(q='How many times will “Hop” be printed?', why='range(5) is 0, 1, 2, 3, 4 – five numbers.'),
  dict(q='What will the program print?', why='range(1, 4) starts at 1 and stops before 4.'),
  dict(q='Fill in the gap to print the numbers 0, 1, 2', why='range(3) gives 0, 1, 2.'),
  dict(q='What will the program print?', why='We start at 10 and subtract 3 while we are above 0.'),
  dict(q='The program should print the numbers 1 to 5, but it prints 1–4. Click the buggy line.', why='The end of a range is not included – it has to be 6.'),
  dict(q='Print 3 times, each on a new line: <code>Kapi swims</code>', tests=[dict(i='', o='Kapi swims\nKapi swims\nKapi swims')],
       check="assert __src.count('print') == 1, 'Use a loop and one print'", sol='for i in range(3):\n    print("Kapi swims")'),
  dict(q='Read n and print the multiplication table of n from 1 to 5 as <code>1 x n = result</code>.'),
  dict(q='Read n and print the sum of squares of the numbers 1 to n (1² + 2² + … + n²).', hint='Start with s = 0 and add i ** 2.'),
 ])

LESSONS['while'] = dict(title='while, break, continue',
 theory="""<p><code>while</code> repeats code <b>as long as</b> a condition is true. Use it when you don't know in advance how many repetitions there will be.</p>
<p>⚠️ Make sure something in the loop changes the condition – otherwise the loop runs forever!</p>
<ul><li><code>break</code> – stops the whole loop immediately</li><li><code>continue</code> – skips the rest of this round and goes to the next one</li></ul>""",
 more="""<p>A typical pattern: <code>while True:</code> with a <code>break</code> inside – e.g. keep asking until the user gives a correct answer. A <code>for</code> loop can have an <code>else</code>, which runs if there was no <code>break</code>.</p>""",
 ex=[
  dict(code='''energy = 3
while energy > 0:
    print(f"Kapi swims, energy: {energy}")
    energy -= 1
print("Kapi rests 😴")''',
       scene=dict(s='loop', items=['⚡3', '⚡2', '⚡1'], cap='Kapi swims while he has energy. When the energy drops to 0, the condition is false and the loop ends.')),
  dict(code='''for i in range(1, 8):
    if i == 3:
        continue  # skip 3
    if i == 6:
        break     # stop at 6
    print(i)''',
       scene=dict(s='loop', items=['1', '2', '3⏭', '4', '5', '6🛑'], cap='Kapi jumps over stone no. 3 (continue), and at 6 heads back home (break).')),
 ],
 tasks=[
  dict(q='What will the program print?', why='x: 1 → 2 → 4 → 8 → 16. At 16 the condition x < 10 is false.'),
  dict(q='What will the program print?', why='break ends the loop before 2 is printed.'),
  dict(q='What will the program print?', why='continue only skips the round for i = 2.'),
  dict(q='This program never ends (infinite loop). Click the line that needs fixing.', why='n grows instead of shrinking, so n > 0 is always true. n must decrease.'),
  dict(q='Fill in the gap so the loop ends when the user types “stop”', why='break exits the while True loop.'),
  dict(q='Using a <code>while</code> loop, print a countdown 5, 4, 3, 2, 1 (each number on a new line) and then <code>Go!</code>',
       tests=[dict(i='', o='5\n4\n3\n2\n1\nGo!')], check="assert 'while' in __src, 'Use a while loop'", sol='n = 5\nwhile n > 0:\n    print(n)\n    n -= 1\nprint("Go!")'),
  dict(q='Keep reading numbers until 0 appears. Print their sum (without the zero).'),
  dict(q='Read n > 0. How many times do you have to floor-divide n by 2 (n //= 2) to get 1? Print the number of steps.'),
 ])

LESSONS['zagn'] = dict(title='Nested loops',
 theory="""<p>A loop inside a loop: the inner one runs <b>completely</b> on every round of the outer one. With 3 outer rounds and 4 inner ones, the code inside runs 3 · 4 = 12 times.</p>
<p>Useful for tables, grids and drawing patterns.</p>""",
 more="""<p>The inner loop can depend on the outer variable, e.g. <code>for j in range(i)</code> – that's how triangles are made. <code>break</code> stops only the loop it is in.</p>""",
 ex=[
  dict(code='''for row in range(3):
    for col in range(4):
        print("🍉", end="")
    print()''',
       scene=dict(s='grid', rows=3, cols=4, emo='🍉', cap='Kapi plants melons in the garden: row by row, 4 melons in each.')),
  dict(code='''for i in range(1, 5):
    print("*" * i)''',
       scene=dict(s='grid', rows=4, cols=4, tri=True, emo='⭐', cap='Kapi builds stairs: in row i he puts i stars.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='The loop runs 2 times, printing 3 melons each time.'),
  dict(q='How many times will “Kapi” be printed?', why='3 outer rounds × 2 inner = 6.'),
  dict(q='What will the program print?', why='For i = 1: 1, 2; for i = 2: 2, 4. print() ends the line.'),
  dict(q='Fill in the gap to make a triangle of stars with 3 rows (1, 2, 3 stars)', why='Row i needs i stars, so the inner loop is range(i).'),
  dict(q='Print a rectangle of <code>#</code>: 2 rows of 5 characters. Use two loops.', check="assert __src.count('for') >= 2, 'Use two for loops'",
       hint='Inside: print("#", end=""), after the inner loop: print().'),
  dict(q='Read n and print an n × n multiplication table. Separate numbers in a row with a space.<br>For 3:<br><code>1 2 3<br>2 4 6<br>3 6 9</code>',
       sol='n = int(input())\nfor i in range(1, n + 1):\n    row = []\n    for j in range(1, n + 1):\n        row.append(str(i * j))\n    print(" ".join(row))',
       hint='Collect the row in a list, or use end=" " (trailing spaces are ignored).'),
  dict(q='Read n and print a Christmas tree with n levels, centred with spaces. For 3:<br><code>&nbsp;&nbsp;*<br>&nbsp;***<br>*****</code>', hint='In row i: n-1-i spaces and 2i+1 stars.'),
 ])

LESSONS['slice'] = dict(title='Indexes, slices, len()',
 theory="""<p>A string is a sequence of characters. Each character has an <b>index</b> – a number counted from <b>0</b>. <code>s[0]</code> is the first character, <code>s[-1]</code> – the last one.</p>
<p>A <b>slice</b> <code>s[a:b]</code> is the characters from index a to b-1. <code>len(s)</code> returns the length.</p>""",
 more="""<p>A missing start means 0, a missing end means “to the end”: <code>s[:3]</code>, <code>s[3:]</code>. The third parameter is the step: <code>s[::2]</code> every second character, <code>s[::-1]</code> – the string backwards. Strings can't be changed: <code>s[0] = "X"</code> raises <code>TypeError</code>.</p>""",
 ex=[
  dict(code='''s = "CAPYBARA"
print(s[0], s[3], s[-1])
print(s[1:4])
print(len(s))''',
       scene=dict(s='row', items=list('CAPYBARA'), hl=[1, 4], label='s[1:4]', cap='Kapi points at letters 1, 2 and 3 – a slice ends BEFORE index 4.')),
  dict(code='''s = "CAPYBARA"
print(s[:4])
print(s[4:])
print(s[::-1])''',
       scene=dict(s='row', items=list('CAPYBARA'), hl=[0, 4], label='s[:4]', cap='s[:4] is the start up to index 4, and s[::-1] is Kapi reading backwards.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='Indexes start at 0, so s[0] is the first letter.'),
  dict(q='What will the program print?', why='-1 is the last character, and the word has 6 letters.'),
  dict(q='What will the program print?', code='''s = "tangerine"
print(s[0:5])''', opts=['tange', 'tanger', 'anger', 'tang'], why='Characters with indexes 0–4, i.e. the first 5.'),
  dict(q='The program raises an error. Click the buggy line.', fix='print(s[3])', why='The word has 4 characters with indexes 0–3. s[4] is outside the string: IndexError.'),
  dict(q='Fill in the gap to print the string backwards', code='''s = "kayak2"
print(s[___])''', expect='2kayak', why='Step -1 reads the string from the end.'),
  dict(q='What will the program print?', why='Start at index 1 (b), then every 3: e, h.'),
  dict(q='Read a word and print its first and last letter separated by a space.', tests=[dict(i='capybara', o='c a'), dict(i='python', o='p n')]),
  dict(q='Read a word and print its middle character (the word has an odd length).', tests=[dict(i='kayak', o='y'), dict(i='abc', o='b'), dict(i='x', o='x')],
       hint='The middle index is len(s) // 2.'),
 ])

LESSONS['metody'] = dict(title='String methods',
 theory="""<p>Methods are called after a dot: <code>text.method()</code>. They return a <b>new</b> string.</p>
<ul><li><code>upper()</code> / <code>lower()</code> – UPPER / lower case</li><li><code>strip()</code> – removes spaces from the start and end</li><li><code>replace(a, b)</code> – replaces a with b</li><li><code>split()</code> – splits text into a list of words</li><li><code>" ".join(list)</code> – glues a list into text</li></ul>""",
 more="""<p><code>split(",")</code> splits on commas. <code>"-".join(...)</code> glues with a dash. Also useful: <code>count()</code>, <code>find()</code>, <code>startswith()</code>, <code>isdigit()</code>. Methods can be chained: <code>s.strip().lower()</code>.</p>""",
 ex=[
  dict(code='''s = "  Kapi loves Water  "
print(s.strip())
print(s.upper())
print(s.replace("Water", "melons"))''',
       scene=dict(s='cards', items=[['strip()', '"Kapi loves Water"', 'no edge spaces'], ['upper()', '"  KAPI LOVES WATER  "', 'UPPER'], ['replace()', '"  Kapi loves melons  "', 'swap']], cap='Kapi works in a print shop: washing, enlarging and swapping letters.')),
  dict(code='''sentence = "kapi loves baths"
words = sentence.split()
print(words)
print("-".join(words))''',
       scene=dict(s='row', items=['"kapi"', '"loves"', '"baths"'], label='split()', cap='Kapi cuts the sentence into words with scissors, and join tapes them back together with “-”.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='upper() turns all letters into capitals.'),
  dict(q='What will the program print?', why='split() splits on spaces and returns a list.'),
  dict(q='What will the program print?', code='print("cat".replace("c", "r"))', opts=['rat', 'cat', 'car', 'rrat'], why='Every “c” is replaced with “r”.'),
  dict(q='Fill in the gap to remove spaces from the edges', code='''s = "   hey   "
print(s.___())''', expect='hey', why='strip() removes whitespace from both ends.'),
  dict(q='What will the program print?', why='join puts the separator between the elements.'),
  dict(q='The program should print KAPI, but it prints Kapi. Click the buggy line.', why='Strings are immutable – upper() returns a new string that must be saved in the variable.'),
  dict(q='Read a name (it may have spaces at the edges and any letter case). Print it in CAPITAL letters without the edge spaces.', tests=[dict(i='  kapi  ', o='KAPI'), dict(i='Alex', o='ALEX')]),
  dict(q='Read a sentence and print the number of words.', tests=[dict(i='kapi loves baths', o='3'), dict(i='hey', o='1'), dict(i='  lots   of  spaces ', o='3')]),
  dict(q='Read a first and last name (e.g. <code>john smith</code>) and print the initials in capitals with dots: <code>J.S.</code>',
       tests=[dict(i='john smith', o='J.S.'), dict(i='Alex Brown', o='A.B.')], sol='s = input()\nfirst, last = s.split()\nprint(f"{first[0].upper()}.{last[0].upper()}.")', hint='Use split(), then [0] and upper().'),
 ])

LESSONS['znaki'] = dict(title='Looping over characters',
 theory="""<p>A <code>for</code> loop can walk through a string character by character:</p>
<pre>for ch in "Kapi":
    print(ch)</pre>
<p>This lets us count vowels, for example, or build a new string by adding characters one by one.</p>""",
 more="""<p>When you also need the index, use <code>for i in range(len(s))</code> or <code>for i, ch in enumerate(s)</code>. The <code>in</code> operator checks whether a character is in a string: <code>"a" in "kapi"</code> → <code>True</code>.</p>""",
 ex=[
  dict(code='''for ch in "KAPI":
    print(ch * 2)''',
       scene=dict(s='loop', items=['K', 'A', 'P', 'I'], cap='Kapi hops along the letters and says each one twice.')),
  dict(code='''s = "capybara"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)''',
       scene=dict(s='loop', items=list('capybara'), acc='count', accv=[0, 1, 1, 1, 1, 2, 2, 3], cap='Kapi collects only vowels in his basket.')),
 ],
 tasks=[
  dict(q='How many lines will the program print?', code='''for ch in "cat":
    print(ch)''', why='The loop runs once for each of the 3 letters.'),
  dict(q='What will the program print?', code='''w = ""
for ch in "abc":
    w = ch + w
print(w)''', why='Each letter is added at the front, so the string gets reversed.'),
  dict(q='Fill in the gap so the loop goes through each character of s', code='''s = "kapi"
for ch ___ s:
    print(ch.upper(), end="")''', why='Loop syntax: for variable in collection.'),
  dict(q='What will the program print?', code='''n = 0
for ch in "Anna has a cat":
    if ch == "a":
        n += 1
print(n)''', opts=['4', '5', '3', '6'], why='Python is case-sensitive – the capital A is not counted. There are 4 lowercase “a”.'),
  dict(q='Read a word and print each of its letters on a separate line.', sol='s = input()\nfor ch in s:\n    print(ch)', hint='for ch in s: print(ch)'),
  dict(q='Read some text and print how many digits it contains (use a loop and <code>isdigit()</code> or <code>in "0123456789"</code>).',
       tests=[dict(i='Kapi is 2 and has 15 cousins', o='3'), dict(i='none', o='0')], sol='s = input()\nn = 0\nfor ch in s:\n    if ch.isdigit():\n        n += 1\nprint(n)', hint='if ch.isdigit(): n += 1'),
  dict(q='Caesar cipher: read a word made of lowercase letters a–z and shift each letter 3 places forward in the alphabet (x→a, y→b, z→c).',
       sol='s = input()\nw = ""\nfor ch in s:\n    w += chr((ord(ch) - ord("a") + 3) % 26 + ord("a"))\nprint(w)', hint='ord("a") is the code of a, chr(code) turns a code into a character. Use % 26.'),
 ])

LESSONS['listy'] = dict(title='Lists',
 theory="""<p>A <b>list</b> is an ordered collection of values in square brackets: <code>fruits = ["apple", "melon", "pear"]</code>.</p>
<p>Indexes and slices work like in strings: <code>fruits[0]</code>, <code>fruits[-1]</code>, <code>fruits[1:3]</code>. Length: <code>len(fruits)</code>.</p>
<p>Unlike a string, a list <b>can be changed</b>: <code>fruits[0] = "plum"</code>.</p>""",
 more="""<p>A list can hold elements of different types, even other lists: <code>[[1, 2], [3, 4]]</code> – then <code>t[1][0]</code> is 3. Note: <code>b = a</code> does not copy a list – both names point to the same list. A copy is <code>a[:]</code> or <code>a.copy()</code>.</p>""",
 ex=[
  dict(code='''backpack = ["🍉", "🍊", "🥕", "🍎"]
print(backpack[0], backpack[-1])
print(backpack[1:3])
backpack[2] = "🍐"
print(backpack)''',
       scene=dict(s='row', items=['🍉', '🍊', '🥕', '🍎'], hl=[1, 3], label='backpack[1:3]', cap='Kapi packs a backpack with pockets numbered from 0. He swaps the carrot for a pear.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='Index 2 is the third element (we count from 0).'),
  dict(q='What will the program print?', opts=['[9, 6, 7]', '[5, 6, 7]', '[9, 5, 6, 7]', 'Error'], why='Lists can be changed – element 0 was replaced.'),
  dict(q='What will the program print?', why='The slice goes from 1 to 3; the list has 5 elements.'),
  dict(q='The program raises an error. Click the buggy line.', why='The last index is len(t) - 1. t[3] does not exist: IndexError.'),
  dict(q='What will the program print?', opts=['[99, 2]', '[1, 2]', '[99]', 'Error'], why='b = a does not create a copy – both names are the same list.'),
  dict(q='Create a list <code>fruits</code> with three strings: <code>apple</code>, <code>melon</code>, <code>pear</code>. Print the second element.',
       tests=[dict(i='', o='melon')], check="assert fruits == ['apple', 'melon', 'pear'], 'The list has the wrong contents'", sol='fruits = ["apple", "melon", "pear"]\nprint(fruits[1])', hint='The second element has index 1.'),
  dict(q='Read numbers on one line separated by spaces. Print the first and the last.'),
 ])

LESSONS['metodylist'] = dict(title='List methods',
 theory="""<ul><li><code>append(x)</code> – adds x at the end</li><li><code>insert(i, x)</code> – inserts x at position i</li><li><code>remove(x)</code> – removes the first x</li><li><code>pop()</code> – takes out and returns the last element (<code>pop(i)</code> – element i)</li><li><code>sort()</code> – sorts the list in ascending order</li><li><code>x in list</code> – is x in the list?</li></ul>""",
 more="""<p><code>sort(reverse=True)</code> sorts in descending order. <code>sorted(list)</code> returns a new sorted list without changing the old one. <code>sort()</code> returns <code>None</code> – don't write <code>t = t.sort()</code>! Also useful: <code>count(x)</code>, <code>index(x)</code>, <code>reverse()</code>.</p>""",
 ex=[
  dict(code='''queue = ["Kapi", "Bobo"]
queue.append("Lulu")
queue.insert(0, "Mimi")
queue.remove("Bobo")
print(queue)
last = queue.pop()
print(last, queue)
print("Kapi" in queue)''',
       scene=dict(s='row', items=['Mimi', 'Kapi', 'Lulu'], label='pool queue', cap='Capybaras queue for the pool: append adds at the end, insert pushes in at the front, pop takes out the last one.')),
  dict(code='''weights = [55, 48, 61, 50]
weights.sort()
print(weights)
weights.sort(reverse=True)
print(weights)''',
       scene=dict(s='row', items=['48', '50', '55', '61'], label='after sort()', cap='Capybaras line up from the lightest to the heaviest.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='append adds at the end.'),
  dict(q='What will the program print?', why='sort() arranges in ascending order.'),
  dict(q='What will the program print?', why='pop() takes out and returns the last element.'),
  dict(q='Fill in the gap to add “melon” at the end of the list', code='''t = ["apple"]
t.___("melon")
print(t)''', expect="['apple', 'melon']", why='append adds an element at the end.'),
  dict(q='What will the program print?', why='remove deletes only the first 5 → [3, 5, 1]; insert(1, 0) puts 0 at position 1.'),
  dict(q='The program raises an error when printing. Which line causes it?', why='sort() changes the list and returns None. After t = t.sort() the variable t is None, so t[0] raises TypeError on line 3 – but the cause is on line 2.'),
  dict(q='Start with an empty list. Read 3 names (each on a new line), add them to the list with <code>append</code> and print the list.',
       start='names = []\n', sol='names = []\nfor i in range(3):\n    names.append(input())\nprint(names)', hint='for i in range(3): names.append(input())'),
  dict(q='Read numbers on one line. Print them sorted in descending order, separated by spaces.', hint='t.sort(reverse=True), then print(*t) prints the elements separated by spaces.'),
  dict(q='Read words on one line. Print them without repeats, in order of first appearance, separated by spaces.',
       start='words = input().split()\n', tests=[dict(i='kapi loves kapi and loves water', o='kapi loves and water'), dict(i='a a a', o='a')],
       sol='words = input().split()\nw = []\nfor s in words:\n    if s not in w:\n        w.append(s)\nprint(" ".join(w))', hint='Add a word to a new list only if it is not there yet (not in).'),
 ])

LESSONS['krotki'] = dict(title='Tuples and sets',
 theory="""<p>A <b>tuple</b> is a list that can't be changed: <code>point = (3, 5)</code>. Great for fixed data such as coordinates.</p>
<p>A <b>set</b> stores elements <b>without repeats</b> and without order: <code>{1, 2, 3}</code>. <code>set(list)</code> removes duplicates.</p>""",
 more="""<p>Unpacking a tuple: <code>x, y = point</code>. Set operations: <code>a | b</code> union, <code>a &amp; b</code> intersection, <code>a - b</code> difference. An empty set is <code>set()</code> – because <code>{}</code> is an empty dictionary!</p>""",
 ex=[
  dict(code='''burrow = (12, 7)
x, y = burrow
print(f"Kapi's burrow: x={x}, y={y}")
guests = ["Bobo", "Lulu", "Bobo", "Mimi", "Lulu"]
print(len(set(guests)))''',
       scene=dict(s='cards', items=[['(12, 7)', 'tuple', "can't change it"], ['set(guests)', "{'Bobo', 'Lulu', 'Mimi'}", 'each guest once']], cap="The burrow's coordinates are rock-solid. And on the guest list each capybara counts only once.")),
  dict(code='''kapi = {"melon", "pear", "grass"}
bobo = {"grass", "apple", "pear"}
print(sorted(kapi & bobo))
print(sorted(kapi | bobo))''',
       scene=dict(s='venn', a=['melon'], both=['grass', 'pear'], b=['apple'], la='Kapi', lb='Bobo', cap='What do both capybaras like? The intersection is grass and pear.')),
 ],
 tasks=[
  dict(q='What will the program print?', why='A set removes repeats: {1, 2, 3}.'),
  dict(q='What will the program print?', opts=['8', '3', '(3, 8)', 'Error'], why='Tuples have indexes like lists: p[1] is the second element.'),
  dict(q='The program raises an error. Click the buggy line.', code='''point = (2, 3)
point[0] = 5
print(point)''', fix='point = (5, 3)', why="Tuples can't be changed: TypeError."),
  dict(q='What will the program print?', why='& is the intersection, and a - b is the elements of a that are not in b.'),
  dict(q='Fill in the gap to unpack the tuple', why='Unpacking: x, y = p.'),
  dict(q='Read words on one line and print how many different words there are.', tests=[dict(i='kapi loves kapi and loves water', o='4'), dict(i='a', o='1')]),
 ])

LESSONS['slowniki'] = dict(title='Dictionaries',
 theory="""<p>A <b>dictionary</b> (dict) stores <b>key: value</b> pairs – like a cabinet with labelled drawers:</p>
<pre>kapi = {"name": "Kapi", "age": 4}</pre>
<p>Reading: <code>kapi["name"]</code>. Changing or adding: <code>kapi["weight"] = 55</code>.</p>
<p>Safe reading: <code>kapi.get("colour", "none")</code> – no error if the key is missing.</p>""",
 more="""<p>Looping: <code>for k in d.keys()</code> – keys, <code>d.values()</code> – values, <code>for k, v in d.items()</code> – pairs. The classic counting pattern: <code>counter[x] = counter.get(x, 0) + 1</code>. Deleting: <code>del d[k]</code> or <code>d.pop(k)</code>.</p>""",
 ex=[
  dict(code='''pantry = {"melon": 2, "pear": 5, "grass": 30}
print(pantry["pear"])
pantry["apple"] = 4
print(pantry.get("banana", 0))
for fruit, n in pantry.items():
    print(f"{fruit}: {n}")''',
       scene=dict(s='dict', pairs=[['melon', '2'], ['pear', '5'], ['grass', '30'], ['apple', '4']], hl='pear', cap='Kapi runs a pantry: each drawer has a label (key), and inside is the number of supplies (value).')),
  dict(code='''text = "kapi loves kapi"
counter = {}
for w in text.split():
    counter[w] = counter.get(w, 0) + 1
print(counter)''',
       scene=dict(s='dict', pairs=[['kapi', '2'], ['loves', '1']], hl='kapi', cap='Kapi counts words: every time he meets one, he drops a token into the right drawer.')),
 ],
 tasks=[
  dict(q='What will the program print?', opts=['2', '1', 'b', 'Error'], why='The key "b" has the value 2.'),
  dict(q='What will the program print?', code='''d = {"cat": 4}
print(d.get("dog", 0))''', opts=['0', '4', 'None', 'Error'], why='get returns the default value 0 when the key is missing.'),
  dict(q='The program raises an error. Click the buggy line.', code='''age = {"Kapi": 4, "Bobo": 2}
print(age["Kapi"])
print(age["Lulu"])''', fix='print(age.get("Lulu", "none"))', why='There is no "Lulu" key in the dictionary – KeyError. get() will help.'),
  dict(q='Fill in the gap so the loop gets the key and the value', why='items() returns (key, value) pairs.'),
  dict(q='What will the program print?', why='d["a"] becomes 8, so the sum of the values is 8 + 5 = 13.'),
  dict(q='Given a dictionary of prices, read a fruit name and print its price, or <code>none</code> if it is missing.',
       start='prices = {"melon": 12, "pear": 8, "apple": 3}\nfruit = input()\n', tests=[dict(i='pear', o='8'), dict(i='banana', o='none')],
       sol='prices = {"melon": 12, "pear": 8, "apple": 3}\nfruit = input()\nprint(prices.get(fruit, "none"))', hint='prices.get(fruit, "none")'),
  dict(q='Read a word and print how many times each letter occurs, in order of first appearance, as <code>letter:count</code> (each on a new line).',
       tests=[dict(i='capybara', o='c:1\na:3\np:1\ny:1\nb:1\nr:1')]),
  dict(q='Read n, then n lines <code>name points</code>. Print the name of the person with the most points (a name may appear several times – add up the points).',
       tests=[dict(i='4\nKapi 5\nBobo 7\nKapi 4\nLulu 8', o='Kapi'), dict(i='1\nAlex 1', o='Alex')],
       sol='n = int(input())\nd = {}\nfor i in range(n):\n    name, p = input().split()\n    d[name] = d.get(name, 0) + int(p)\nbest = None\nfor k, v in d.items():\n    if best is None or v > d[best]:\n        best = k\nprint(best)',
       hint='Add up in a dictionary, then find the key with the largest value.'),
 ])
