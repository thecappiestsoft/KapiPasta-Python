# KapiPasta - Python: English overrides merged onto content/pl (same order of examples/tasks).
# After editing run: python3 tools/build.py

CHAPTERS = {
 'start': dict(name=dict(rpg='Starter Village', space='Orbital Station', neutral='Start'), topic='print, comments, f-strings'),
 'dane': dict(name=dict(rpg='Data Forest', space='Planet Data', neutral='Data'), topic='variables, types, input, operators'),
 'warunki': dict(name=dict(rpg='Bridge of Decisions', space='Asteroid Belt', neutral='Conditions'), topic='comparisons, and/or/not, if/elif/else'),
}
LESSONS = {}

LESSONS['print'] = dict(title='print and comments',
 theory="""<p><code>print()</code> is the voice of the program – it shows on screen whatever you put in the brackets. Text is written in quotes: <code>"..."</code> or <code>'...'</code>.</p>
<p>Separate several values with commas – Python puts a space between them.</p>
<p>Everything after <code>#</code> is a <b>comment</b> – a note for humans. Python ignores it.</p>""",
 more="""<p><code>print</code> has two handy parameters: <code>sep</code> – what to put between values (a space by default) and <code>end</code> – what to add at the end (a newline <code>\\n</code> by default).</p>""",
 ex=[
  dict(code='''# Kapi says hello to the world
print("Hi, I'm Kapi!")
print("I have", 3, "oranges")  # commas give spaces''',
       scene=dict(s='say', cap='Kapi holds up a sign showing everything print wrote.')),
  dict(code='''print("ho", "ho", "ho", sep="-")
print("Kapi", end=" ")
print("swims")''',
       scene=dict(s='say', cap='sep glues the words with a dash, and end makes the second print write on the same line.')),
 ],
 tasks=[
  dict(q='What will the program print?', code='print("Kapi", "likes", "melons")',
       opts=['Kapi likes melons', 'Kapilikesmelons', '"Kapi" "likes" "melons"', 'Kapi, likes, melons'], why='Commas in print insert a single space between values.'),
  dict(q='What will Python do with this line?', code='# print("Secret message")',
       opts=['Print nothing – it is a comment', 'Print: Secret message', 'Raise an error', 'Print: # print("Secret message")'], why='The # sign starts a comment – Python skips the rest of the line.'),
  dict(q='Fill in the gap so the program prints: Hey!', code='___("Hey!")', why='The print function is used for printing.'),
  dict(q='The program should greet us, but Python reports an error. Click the buggy line.',
       code='''print("Good morning")
print("I am Kapi)
print("See you")''', fix='print("I am Kapi")', why='The closing quote is missing – text must be closed on both sides.'),
  dict(q='What will the program print?', why='sep="" glues the letters together, and end="!" replaces the newline with an exclamation mark – so 3 lands right after it.'),
  dict(q='Write a program that prints on two lines:<br><code>Kapi</code><br><code>loves baths</code>',
       start='# Your code\n', tests=[dict(i='', o='Kapi\nloves baths')], sol='print("Kapi")\nprint("loves baths")', hint='Use two print commands.'),
  dict(q='Using <b>one</b> print and the <code>sep</code> parameter, print the date <code>20.11.2026</code> from the numbers 20, 11 and 2026.',
       check="assert __src.count('print') == 1, 'Use only one print'", hint='sep="." puts a dot between values.'),
 ])

LESSONS['fstr'] = dict(title='f-strings and formatting',
 theory="""<p>An <b>f-string</b> is text with the letter <code>f</code> before the quote. Inside curly braces <code>{}</code> you put variables or whole expressions – Python replaces them with their values.</p>
<p><code>f"I am {age} years old"</code> – instead of <code>{age}</code> you'll see the number.</p>""",
 more="""<p>After a colon you can add a format: <code>{x:.2f}</code> – 2 decimal places, <code>{x:5}</code> – width of 5 characters, <code>{x:>5}</code>/<code>{x:<5}</code>/<code>{x:^5}</code> – right, left, centre.</p>""",
 ex=[
  dict(code='''name = "Kapi"
age = 4
print(f"{name} is {age} years old")
print(f"Next year {name} will be {age + 1}")''',
       scene=dict(s='say', cap='Kapi puts the values of the variables into the empty {} on the sign.')),
  dict(code='''price = 3.14159
print(f"A melon costs ${price:.2f}")
print(f"[{'Kapi':^8}]")''',
       scene=dict(s='say', cap=':.2f rounds to 2 decimal places, and :^8 centres the text in a field 8 characters wide.')),
 ],
 tasks=[
  dict(q='What will the program print?', code='''x = 7
print(f"Kapi ate {x} apples")''', opts=['Kapi ate 7 apples', 'Kapi ate {x} apples', 'Kapi ate x apples', 'f"Kapi ate 7 apples"'],
       why='In an f-string, {x} is replaced with the value of x.'),
  dict(q='What will the program print (without the letter f)?', code='''x = 7
print("I have {x} ducks")''', opts=['I have {x} ducks', 'I have 7 ducks', 'Error', 'I have x ducks'],
       why='Without the f, curly braces are ordinary characters – nothing is replaced.'),
  dict(q='Fill in the gap so it prints: Kapi is 5', code='''age = 5
print(___"Kapi is {age}")''', why='The letter f before the quote switches on the {} replacement.'),
  dict(q='What will the program print?', why='You can put a whole expression inside {} – Python will calculate it.'),
  dict(q='What will the program print?', why='.3f means 3 decimal places, rounded.'),
  dict(q='The program should print the price with 2 decimal places. Which line spoils the output?',
       code='''price = 4.5
count = 3
print(f"Total: {price * count:.2f}")
print(f"Average: {price:2f}")''', fix='print(f"Average: {price:.2f}")',
       why='The dot is missing: :2f means width 2, not 2 decimal places. There is no error, but it prints 4.500000.'),
  dict(q='The variables <code>name = "Kapi"</code> and <code>fruit = "tangerines"</code> already exist. Use an f-string to print:<br><code>Kapi likes tangerines</code>',
       start='name = "Kapi"\nfruit = "tangerines"\n', tests=[dict(i='', o='Kapi likes tangerines')],
       check="assert 'f\"' in __src or \"f'\" in __src, 'Use an f-string'", sol='name = "Kapi"\nfruit = "tangerines"\nprint(f"{name} likes {fruit}")', hint='print(f"{name} likes ...")'),
  dict(q='Given <code>r = 2.5</code>, print the area of a circle (use pi = 3.14159) to 2 decimal places:<br><code>Area: 19.63</code>',
       tests=[dict(i='', o='Area: 19.63')], sol='r = 2.5\nprint(f"Area: {3.14159 * r ** 2:.2f}")', hint='Area = pi * r ** 2, format :.2f'),
 ])

LESSONS['zmienne'] = dict(title='Variables and types',
 theory="""<p>A <b>variable</b> is a labelled box where we keep a value: <code>fruits = 5</code>. The <code>=</code> sign means “put into the box”, not “equals”.</p>
<p>Basic types:</p><ul><li><code>int</code> – whole number: <code>5</code></li><li><code>float</code> – number with a decimal point: <code>2.5</code></li><li><code>str</code> – text: <code>"Kapi"</code></li><li><code>bool</code> – true/false: <code>True</code>, <code>False</code></li></ul>
<p>Check a type with <code>type()</code>.</p>""",
 more="""<p>Variable names: letters, digits and <code>_</code>, they can't start with a digit. Case matters: <code>kapi</code> and <code>Kapi</code> are two different variables. You can assign several at once: <code>a, b = 1, 2</code>, and swapping is <code>a, b = b, a</code>.</p>""",
 ex=[
  dict(code='''name = "Kapi"
age = 4
weight = 55.5
hungry = True
print(type(name), type(age))
print(type(weight), type(hungry))''',
       scene=dict(s='boxes', vars=[['name', '"Kapi"', 'str'], ['age', '4', 'int'], ['weight', '55.5', 'float'], ['hungry', 'True', 'bool']], cap='Kapi puts values into boxes. The colour of a box is its data type.')),
  dict(code='''fruits = 3
fruits = fruits + 2
print(fruits)''',
       scene=dict(s='boxes', vars=[['fruits', '3 → 5', 'int']], cap='Kapi takes out 3 fruits, adds 2 and puts 5 back. The old value disappears.')),
 ],
 tasks=[
  dict(q='What type is the value <code>3.0</code>?', why='A decimal point means float, even if it is followed by 0.'),
  dict(q='What will the program print?', why='First x = 10, then the new value 10 - 4 = 6 replaces the old one.'),
  dict(q='What type is <code>"42"</code>?', why='Quotes mean text – even when there are digits inside.'),
  dict(q='Fill in the logical value “true”', code='''kapi_likes_water = ___
print(kapi_likes_water)''', why='Logical values in Python start with a capital letter: True and False.'),
  dict(q='Python reports an error. Which line is to blame?', code='''fruits = 5
print(Fruits)''', fix='print(fruits)', why='Python is case-sensitive. The variable Fruits does not exist – hence NameError.'),
  dict(q='What will the program print?', why='a, b = b, a swaps the values in one step.'),
  dict(q='Create a variable <code>animal</code> with the text <code>capybara</code> and a variable <code>legs</code> with the number 4. Print them with one print.',
       tests=[dict(i='', o='capybara 4')], check="assert animal == 'capybara' and legs == 4, 'Check the values of the variables'",
       sol='animal = "capybara"\nlegs = 4\nprint(animal, legs)', hint='print(animal, legs)'),
 ])

LESSONS['input'] = dict(title='input and type conversion',
 theory="""<p><code>input()</code> pauses the program and waits for the user to type something. It <b>always</b> returns text (<code>str</code>)!</p>
<p>To do maths, turn text into a number: <code>int("5")</code> → <code>5</code>, <code>float("2.5")</code> → <code>2.5</code>. The other way round: <code>str(5)</code> → <code>"5"</code>.</p>
<p>💡 In this app you type the data for <code>input()</code> in the <b>Input data</b> field – each line is one answer.</p>""",
 more="""<p>A common pattern: <code>n = int(input("Enter a number: "))</code>. Note: <code>"2" + "3"</code> is <code>"23"</code> (joining texts), and <code>int("2.5")</code> raises <code>ValueError</code> – use <code>float</code> for numbers with a decimal point.</p>""",
 ex=[
  dict(code='''name = input("What's your name? ")
print(f"Hi, {name}!")''', inp='Alex',
       scene=dict(s='say', cap='Kapi asks, waits for the answer and greets the guest by name.')),
  dict(code='''a = input()
b = input()
print(a + b)
print(int(a) + int(b))''', inp='2\n3',
       scene=dict(s='cards', items=[['"2" + "3"', '"23"', 'texts are joined'], ['int("2") + int("3")', '5', 'numbers are added']], cap='Kapi sticks two notes with digits together, then turns them into numbers and adds them.')),
 ],
 tasks=[
  dict(q='What type is the result of <code>input()</code> when the user types 7?', why='input() always returns text. Use int() or float() to calculate.'),
  dict(q='What will the program print if the user types 4 and then 4?', opts=['44', '8', '4 4', 'Error'], why='Adding texts joins them: "4" + "4" = "44".'),
  dict(q='Fill in the gap so the program adds numbers instead of joining texts', why='int() turns text into a whole number.'),
  dict(q='The user types 2.5. Which line raises an error?', code='''t = input()
price = int(t)
print(price * 2)''', fix='price = float(t)', why='int("2.5") will not work – text with a decimal point is converted with float().'),
  dict(q='What does <code>print(str(3) * 3)</code> print?', opts=['333', '9', '3 3 3', 'Error'], why='str(3) is "3", and text times a number means repetition: "333".'),
  dict(q='Read a name and print <code>Welcome, NAME!</code><br>E.g. for <code>Alex</code> → <code>Welcome, Alex!</code>',
       start='name = input()\n', tests=[dict(i='Alex', o='Welcome, Alex!'), dict(i='Kapi', o='Welcome, Kapi!')],
       sol='name = input()\nprint(f"Welcome, {name}!")', hint='print(f"Welcome, {name}!")'),
  dict(q='Read two whole numbers (each on its own line) and print their sum.', hint='a = int(input())'),
  dict(q='Read the height in cm (a whole number) and the weight in kg (may have a decimal point). Print the BMI to 1 decimal place: <code>BMI: 22.9</code><br>BMI = weight / (height in metres)²',
       sol='h = int(input()) / 100\nm = float(input())\nprint(f"BMI: {m / h ** 2:.1f}")', hint='Convert cm to metres by dividing by 100.'),
 ])

LESSONS['oper'] = dict(title='Arithmetic operators',
 theory="""<p>Operations: <code>+</code> <code>-</code> <code>*</code> <code>/</code> and three special ones:</p>
<ul><li><code>//</code> – floor division (how many full groups): <code>7 // 2</code> → <code>3</code></li><li><code>%</code> – remainder: <code>7 % 2</code> → <code>1</code></li><li><code>**</code> – power: <code>2 ** 3</code> → <code>8</code></li></ul>
<p>Ordinary <code>/</code> always gives a float: <code>6 / 2</code> → <code>3.0</code>.</p>""",
 more="""<p>Order of operations: first <code>**</code>, then <code>* / // %</code>, finally <code>+ -</code>. Brackets change the order. Shortcuts: <code>x += 1</code> means <code>x = x + 1</code> (also <code>-= *= //= %=</code>). Trick: <code>n % 10</code> is the last digit of a number, and <code>n // 10</code> cuts off the last digit.</p>""",
 ex=[
  dict(code='''tangerines = 7
print(tangerines // 2)  # each of 2 capybaras gets
print(tangerines % 2)   # left over
print(2 ** 3)''',
       scene=dict(s='share', n=7, k=2, cap='Kapi shares 7 tangerines between 2 capybaras: each gets 3 (//), and 1 is left over (%).')),
  dict(code='''print(6 / 2)
print(2 + 3 * 4)
print((2 + 3) * 4)
n = 1234
print(n % 10, n // 10)''',
       scene=dict(s='cards', items=[['6 / 2', '3.0', '/ gives a float'], ['2 + 3 * 4', '14', 'multiplication first'], ['(2 + 3) * 4', '20', 'brackets first'], ['1234 % 10', '4', 'last digit'], ['1234 // 10', '123', 'without the last digit']],
                  cap='Kapi counts on an abacus – the order of operations matters!')),
 ],
 tasks=[
  dict(q='What is <code>17 // 5</code>?', why='17 // 5 is the number of full fives in 17, i.e. 3.'),
  dict(q='What is <code>17 % 5</code>?', why='17 = 3 · 5 + 2, so the remainder is 2.'),
  dict(q='What is <code>3 ** 2</code>?', why='3 to the power of 2 is 3 · 3 = 9.'),
  dict(q='What does <code>print(8 / 2)</code> print?', why='Ordinary division / always gives a float.'),
  dict(q='Fill in the operator to get the remainder of dividing by 2', why='% gives the remainder. 9 % 2 = 1, so 9 is odd.'),
  dict(q='What will the program print?', why='10 + 5 = 15, and 15 // 4 = 3.'),
  dict(q='What does <code>print(-7 // 2)</code> print?', why='// always rounds down (towards the smaller number): -3.5 → -4.'),
  dict(q='Kapi has 23 tangerines and packs them 5 per basket. Print on two lines: the number of full baskets and the number of tangerines left over.',
       hint='Use // and %.'),
  dict(q='Read a number of seconds and print it as <code>M min S s</code>.<br>E.g. 135 → <code>2 min 15 s</code>', hint='Minutes are s // 60, seconds are s % 60.'),
  dict(q='Read a three-digit number and print the sum of its digits (without converting to text!). E.g. 472 → <code>13</code>',
       check="assert 'str(' not in __src and '[' not in __src, 'Use only // and %'", hint='Last digit: n % 10, middle: n // 10 % 10, first: n // 100.'),
 ])

LESSONS['logika'] = dict(title='Comparisons and logic',
 theory="""<p>Comparisons give <code>True</code> or <code>False</code>: <code>==</code> equal, <code>!=</code> not equal, <code>&lt;</code> <code>&gt;</code> <code>&lt;=</code> <code>&gt;=</code>.</p>
<p>⚠️ <code>=</code> is assignment, <code>==</code> is comparison!</p>
<p>Combining conditions:</p><ul><li><code>and</code> – both must be true</li><li><code>or</code> – one is enough</li><li><code>not</code> – flips the value</li></ul>""",
 more="""<p>Python lets you chain comparisons: <code>0 &lt; x &lt; 10</code>. Order: first <code>not</code>, then <code>and</code>, finally <code>or</code>. Texts are compared alphabetically: <code>"cat" &lt; "dog"</code> → <code>True</code>.</p>""",
 ex=[
  dict(code='''sunny = True
warm_water = False
print(sunny and warm_water)
print(sunny or warm_water)
print(not warm_water)''',
       scene=dict(s='cards', items=[['True and False', 'False', 'both must be ✔'], ['True or False', 'True', 'one ✔ is enough'], ['not False', 'True', 'flipped']],
                  cap='Kapi swims only when it is sunny AND the water is warm. Kapi goes for a walk when it is sunny OR warm.')),
  dict(code='''temp = 24
print(temp > 20)
print(temp == 25)
print(18 <= temp <= 26)''',
       scene=dict(s='cards', items=[['24 > 20', 'True', ''], ['24 == 25', 'False', ''], ['18 <= 24 <= 26', 'True', 'in range']], cap='Kapi checks the thermometer by the pool.')),
 ],
 tasks=[
  dict(q='What does <code>print(5 == 5.0)</code> print?', opts=['True', 'False', 'Error', '5'], why='The numeric values are equal, so the result is True.'),
  dict(q='What will the program print?', opts=['False', 'True', '1', 'Error'], why='and needs both conditions to be true. 1 > 4 is False.'),
  dict(q='What will the program print?', opts=['True', 'False', 'Error', 'None'], why='not True is False, but 3 == 3 is True, and False or True = True.'),
  dict(q='Fill in the “not equal” operator', why='!= means “not equal to”.'),
  dict(q='Python reports a syntax error. Click the buggy line.', code='''x = 7
if x = 7:
    print("seven")''', why='A single = is assignment. Comparison needs ==.'),
  dict(q='What will the program print?', why='15 lies between 10 and 20, but it is not even.'),
  dict(q='What will the program print?', opts=['True', 'False', 'Error', 'None'], why='and goes first: False and False = False, then True or False = True.'),
  dict(q='Read a number and print <code>True</code> if it is even and greater than 10, otherwise <code>False</code> (no if!).', hint='print(condition1 and condition2)'),
 ])

LESSONS['if'] = dict(title='if, elif, else',
 theory="""<p><code>if</code> runs code only when a condition is true. After the condition put a <b>colon</b>, and <b>indent</b> the code inside (4 spaces).</p>
<pre>if condition:
    do_this
elif other_condition:
    do_that
else:
    in_every_other_case</pre>
<p>Python checks conditions from the top and runs <b>only the first</b> matching block.</p>""",
 more="""<p>Conditions can be nested – an <code>if</code> inside an <code>if</code>. Each level adds 4 more spaces of indentation. Nesting can often be replaced with <code>and</code>.</p>""",
 ex=[
  dict(code='''temp = 28
if temp > 25:
    print("Kapi goes for a swim 🏊")
else:
    print("Kapi stays in the burrow 🏠")''',
       scene=dict(s='fork', cond='temp > 25', val='True', yes='swim 🏊', no='burrow 🏠', cap='Kapi stands at a fork in the road. The condition is true, so Kapi turns left – into the water.')),
  dict(code='''points = 72
if points >= 90:
    print("excellent")
elif points >= 70:
    print("good")
elif points >= 50:
    print("satisfactory")
else:
    print("try again")''',
       scene=dict(s='ladder', steps=[['points >= 90', False], ['points >= 70', True], ['points >= 50', None]], res='good', cap='Kapi checks the doors one by one and opens the first that fits – the rest are not checked.')),
  dict(code='''hungry = True
time = "morning"
if hungry:
    if time == "morning":
        print("porridge")
    else:
        print("melon")''',
       scene=dict(s='fork', cond='time == "morning"', val='True', yes='porridge 🥣', no='melon 🍉', cap='First Kapi checks if he is hungry, and only then picks a meal – that is a nested condition.')),
 ],
 tasks=[
  dict(q='What will the program print?', code='''x = 3
if x > 5:
    print("big")
else:
    print("small")''', opts=['small', 'big', 'big\nsmall', 'nothing'], why='3 > 5 is False, so else runs.'),
  dict(q='What will the program print?', why='Only the first true condition runs. x > 50 matches, so elif is not checked.'),
  dict(q='Fill in the missing word', code='''age = 12
if age >= 18:
    print("adult")
___:
    print("minor")''', expect='minor', why='else runs when no condition was true.'),
  dict(q='Python reports an error. Click the buggy line.', code='''x = 10
if x > 5
    print("More than 5")''', why='An if condition must always be followed by a colon.'),
  dict(q='Python reports an indentation error. Click the buggy line.', code='''x = 10
if x > 5:
print("More than 5")''', fix='    print("More than 5")', why='Code inside if must be indented (4 spaces).'),
  dict(q='What will the program print?', why='a > 3 is true, so we go inside. b > 10 is false – the inner else runs.'),
  dict(q='Read a number. Print <code>even</code> or <code>odd</code>.',
       tests=[dict(i='4', o='even'), dict(i='7', o='odd'), dict(i='0', o='even')], sol='n = int(input())\nif n % 2 == 0:\n    print("even")\nelse:\n    print("odd")', hint='Check n % 2 == 0.'),
  dict(q='Read the water temperature. Print: <code>ice</code> (≤ 0), <code>cold</code> (1–15), <code>perfect</code> (16–30), <code>hot</code> (> 30).',
       tests=[dict(i='-3', o='ice'), dict(i='0', o='ice'), dict(i='10', o='cold'), dict(i='16', o='perfect'), dict(i='30', o='perfect'), dict(i='31', o='hot')],
       sol='t = int(input())\nif t <= 0:\n    print("ice")\nelif t <= 15:\n    print("cold")\nelif t <= 30:\n    print("perfect")\nelse:\n    print("hot")', hint='Use if, elif, elif, else – starting from the lowest temperature.'),
  dict(q='Read a year. Print <code>leap</code> or <code>common</code>.<br>A year is a leap year if it is divisible by 4 and not by 100, or divisible by 400.',
       start='year = int(input())\n', tests=[dict(i='2024', o='leap'), dict(i='1900', o='common'), dict(i='2000', o='leap'), dict(i='2023', o='common')],
       sol='year = int(input())\nif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:\n    print("leap")\nelse:\n    print("common")', hint='(year % 4 == 0 and year % 100 != 0) or year % 400 == 0'),
 ])
