CHAPTER_ORDER = 3

LESSONS = [
    {
        'title': 'For Loops and the range() Function',
        'description': 'Learn how to repeat actions using for loops, iterate over sequences, and generate number ranges -- the most common way to automate repetitive tasks.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'why-loops',
                'title': 'Why Loops?',
                'content': """## Why Loops?

Imagine you are a teacher and you need to calculate the final grade for every student in a class of 30. Without loops, you would write the same calculation 30 times:

```python
grade_1 = (85 + 90 + 78) / 3
grade_2 = (92 + 88 + 95) / 3
grade_3 = (70 + 65 + 80) / 3
# ... 27 more times!
```

That is tedious, error-prone, and impractical. **Loops** solve this by letting you write the instruction once and repeat it automatically.

Real-life situations that need loops are everywhere:

- A cashier scanning every item in your shopping cart.
- A teacher recording attendance for each student.
- A weather app displaying the forecast for each day of the week.
- A music player going through every song in a playlist.

### The `for` Loop

The `for` loop iterates over a **sequence** (a list, string, range, or any iterable) and executes a block of code once for each item:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

**How it works:**

1. Python picks the first item from the sequence and assigns it to the loop variable (`fruit`).
2. It executes the indented code block.
3. It picks the next item and repeats.
4. When there are no more items, the loop ends.

### Iterating Over a String

Since a string is a sequence of characters, you can loop through it:

```python
for letter in "Hello":
    print(letter)
```

Output:
```
H
e
l
l
o
```""",
                'exercise': None,
            },
            {
                'id': 'the-range-function',
                'title': 'The range() Function',
                'content': """## The range() Function

The `range()` function generates a sequence of numbers. It is one of the most commonly used tools with `for` loops.

### Three Forms of range()

```python
# range(stop) -- from 0 up to (but not including) stop
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4

print()  # newline

# range(start, stop) -- from start up to (but not including) stop
for i in range(2, 6):
    print(i, end=" ")
# Output: 2 3 4 5

print()

# range(start, stop, step) -- with a custom step size
for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8
```

**Key points:**
- `range()` always **excludes** the stop value.
- The default start is `0` and the default step is `1`.
- The step can be negative to count down.

### Counting Down

```python
for i in range(5, 0, -1):
    print(i)
```

Output:
```
5
4
3
2
1
```

Think of a rocket launch countdown!

### Real-Life Example: Processing Student Grades

A teacher wants to print the rank and grade for each student:

```python
grades = [88, 92, 75, 95, 68]

for i in range(len(grades)):
    rank = i + 1
    print(f"Student {rank}: {grades[i]} points")
```

### Using `enumerate()` (a Better Alternative)

Python's `enumerate()` gives you both the index and the value:

```python
grades = [88, 92, 75, 95, 68]

for index, grade in enumerate(grades):
    rank = index + 1
    print(f"Student {rank}: {grade} points")
```

Both produce the same result, but `enumerate()` is considered more "Pythonic".""",
                'exercise': {
                    'instructions': 'Use a for loop with range() to print the first 5 multiples of 3 (starting from 3). Each multiple should be on its own line in the format "3 x 1 = 3", "3 x 2 = 6", etc.',
                    'starter_code': '# Print the first 5 multiples of 3\nfor i in range(1, 6):\n    result = 3 * i\n    print(f"3 x {i} = {result}")\n',
                    'expected_output': '3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15',
                    'hint': 'Use range(1, 6) to get numbers 1 through 5. Multiply each number by 3 and print using an f-string.',
                },
            },
            {
                'id': 'loop-accumulator-pattern',
                'title': 'The Accumulator Pattern',
                'content': """## The Accumulator Pattern

One of the most useful loop patterns is the **accumulator**: you start with an initial value and update it in every iteration. This is how you calculate totals, averages, maximums, and more.

### Real-Life Example: Shopping Cart Total

Imagine scanning items at a grocery store checkout:

```python
prices = [2.50, 1.99, 4.75, 3.25, 0.99]

total = 0  # accumulator starts at 0
for price in prices:
    total = total + price  # same as: total += price

print(f"Subtotal: ${total:.2f}")
```

### Real-Life Example: Counting Passing Grades

A teacher wants to know how many students passed (scored 60 or above):

```python
scores = [85, 42, 91, 58, 73, 66, 39, 88]

pass_count = 0
for score in scores:
    if score >= 60:
        pass_count += 1

total_students = len(scores)
print(f"Passed: {pass_count} out of {total_students}")
```

### Real-Life Example: Finding the Maximum

Suppose you want to find the hottest day of the week:

```python
temperatures = [72, 75, 68, 80, 77, 85, 73]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

max_temp = temperatures[0]
max_day = days[0]

for i in range(1, len(temperatures)):
    if temperatures[i] > max_temp:
        max_temp = temperatures[i]
        max_day = days[i]

print(f"Hottest day: {max_day} at {max_temp}°F")
```

### Building a String with a Loop

You can accumulate strings too:

```python
words = ["Python", "is", "fun"]
sentence = ""

for word in words:
    sentence = sentence + word + " "

print(sentence.strip())  # "Python is fun"
```""",
                'exercise': {
                    'instructions': 'Calculate the total cost of items in a shopping cart and the number of items that cost more than $5.00. Print the total cost (formatted to 2 decimal places) and the count of expensive items, each on its own line.',
                    'starter_code': '# Shopping cart prices\nprices = [3.99, 7.50, 2.25, 8.99, 1.50, 12.00, 4.75]\n\n# Accumulators\ntotal_cost = 0\nexpensive_count = 0\n\n# Process each item\nfor price in prices:\n    total_cost += price\n    if price > 5.00:\n        expensive_count += 1\n\n# Print results\nprint(f"Total cost: ${total_cost:.2f}")\nprint(f"Items over $5.00: {expensive_count}")\n',
                    'expected_output': 'Total cost: $40.98\nItems over $5.00: 3',
                    'hint': 'Start total_cost and expensive_count at 0. Inside the loop, add each price to total_cost. Use an if statement inside the loop to check if price > 5.00 and increment expensive_count.',
                },
            },
            {
                'id': 'looping-with-lists',
                'title': 'Practical Loop Patterns',
                'content': """## Practical Loop Patterns

Let's explore several common patterns you will use regularly.

### Building a New List from an Old One

Suppose you have prices in dollars and need to convert them to euros:

```python
usd_prices = [10.00, 25.50, 7.99, 42.00]
exchange_rate = 0.92

eur_prices = []
for price in usd_prices:
    eur_prices.append(price * exchange_rate)

for i in range(len(usd_prices)):
    print(f"${usd_prices[i]:.2f} -> EUR {eur_prices[i]:.2f}")
```

### Summing with a Running Total

Track how a balance changes over time:

```python
transactions = [100, -30, -15, 50, -45, 200]
balance = 0

for transaction in transactions:
    balance += transaction
    if transaction >= 0:
        print(f"  Deposit: +${transaction} -> Balance: ${balance}")
    else:
        print(f"  Withdrawal: -${abs(transaction)} -> Balance: ${balance}")
```

### Iterating Over Multiple Lists with zip()

`zip()` lets you loop over two or more lists in parallel:

```python
students = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]

for student, score in zip(students, scores):
    print(f"{student}: {score}")
```""",
                'exercise': {
                    'instructions': 'Given a list of student names and a list of their scores, use zip() to loop through both lists and print each student\'s name and whether they passed (score >= 70) or failed. Format: "Alice: 85 - Pass" or "Bob: 55 - Fail".',
                    'starter_code': '# Student data\nstudents = ["Alice", "Bob", "Charlie", "Diana"]\nscores = [85, 55, 72, 90]\n\n# Loop through both lists together\nfor student, score in zip(students, scores):\n    if score >= 70:\n        status = "Pass"\n    else:\n        status = "Fail"\n    print(f"{student}: {score} - {status}")\n',
                    'expected_output': 'Alice: 85 - Pass\nBob: 55 - Fail\nCharlie: 72 - Pass\nDiana: 90 - Pass',
                    'hint': 'Use zip(students, scores) to pair each student with their score. Inside the loop, use an if/else to set status to "Pass" or "Fail" based on whether the score is >= 70.',
                },
            },
        ],
    },
    {
        'title': 'While Loops',
        'description': 'Learn how to repeat actions using while loops when the number of iterations is unknown. Master input validation, sentinel values, and controlled repetition.',
        'order': 2,
        'item_order': 3,
        'estimated_time_minutes': 18,
        'sections': [
            {
                'id': 'while-loop-basics',
                'title': 'While Loop Basics',
                'content': """## While Loop Basics

A `for` loop is perfect when you know **how many times** to repeat. But what about situations where you do **not** know in advance?

- An ATM lets you keep withdrawing money until your balance hits zero.
- A password prompt keeps asking until you type the correct password (or run out of attempts).
- A countdown timer runs until it reaches zero.
- A game continues until the player loses all their lives.

The `while` loop repeats a block of code **as long as a condition is True**:

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1
```

Output:
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

**How it works:**

1. Python checks the condition (`count <= 5`).
2. If `True`, it runs the indented block.
3. It goes back to step 1 and checks again.
4. When the condition becomes `False`, the loop stops.

### Critical Rule: Avoid Infinite Loops

If the condition never becomes `False`, the loop runs forever:

```python
# DANGER - infinite loop!
# x = 1
# while x > 0:
#     print(x)
#     x += 1  # x keeps growing, condition is always True
```

Always make sure something inside the loop **changes the condition** so it eventually becomes `False`.

### Real-Life Example: Countdown Timer

```python
seconds = 5

print("Countdown started!")
while seconds > 0:
    print(f"  {seconds}...")
    seconds -= 1

print("Liftoff!")
```""",
                'exercise': {
                    'instructions': 'Write a while loop that doubles a number starting from 1 until it exceeds 100. Print each value on its own line. After the loop, print "Final value: X" where X is the value that exceeded 100.',
                    'starter_code': '# Start with 1 and keep doubling\nnumber = 1\n\nwhile number <= 100:\n    print(number)\n    number = number * 2\n\nprint(f"Final value: {number}")\n',
                    'expected_output': '1\n2\n4\n8\n16\n32\n64\nFinal value: 128',
                    'hint': 'Start number at 1. Inside the while loop, print the current number first, then double it. The loop condition is checked BEFORE each iteration, so when number becomes 128 (which is > 100), the loop does not execute again. The final value printed after the loop is 128.',
                },
            },
            {
                'id': 'sentinel-values',
                'title': 'Sentinel Values and Controlled Loops',
                'content': """## Sentinel Values and Controlled Loops

A **sentinel value** is a special value that signals the loop to stop. This pattern is common in programs that process data until a termination signal is received.

### Real-Life Example: Cash Register

A cashier scans items until they press "Total" (represented by a price of 0):

```python
# Simulating a cash register (prices pre-defined for demonstration)
prices = [4.99, 2.50, 8.75, 1.25, 0]  # 0 is the sentinel

total = 0.00
index = 0

while prices[index] != 0:
    total += prices[index]
    print(f"  Scanned: ${prices[index]:.2f}")
    index += 1

print(f"Total: ${total:.2f}")
```

### Loop with a Counter (Password Retry)

A login system gives the user a limited number of attempts:

```python
# Simulating password attempts
correct_password = "python123"
attempts = ["wrongpass", "letmein", "python123"]
max_attempts = 3

attempt_number = 0
logged_in = False

while attempt_number < max_attempts and not logged_in:
    current_attempt = attempts[attempt_number]
    attempt_number += 1
    print(f"Attempt {attempt_number}: Trying '{current_attempt}'...")

    if current_attempt == correct_password:
        logged_in = True

if logged_in:
    print("Login successful!")
else:
    print("Account locked after 3 failed attempts.")
```

### Flag-Controlled Loops

A **flag** is a boolean variable that controls whether the loop continues:

```python
found = False
numbers = [4, 7, 2, 9, 1, 5, 8]
target = 9
index = 0

while not found and index < len(numbers):
    if numbers[index] == target:
        found = True
    else:
        index += 1

if found:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found")
```""",
                'exercise': {
                    'instructions': 'Simulate an ATM withdrawal system. The starting balance is $500. Process a list of withdrawal requests: [100, 200, 150, 100]. For each withdrawal, check if there are sufficient funds. If yes, subtract the amount and print "Withdrew $X. Balance: $Y". If not, print "Insufficient funds for $X. Balance: $Y" and stop processing (break out of the loop).',
                    'starter_code': '# ATM Simulation\nbalance = 500\nwithdrawals = [100, 200, 150, 100]\n\nindex = 0\nwhile index < len(withdrawals):\n    amount = withdrawals[index]\n    if amount <= balance:\n        balance -= amount\n        print(f"Withdrew ${amount}. Balance: ${balance}")\n    else:\n        print(f"Insufficient funds for ${amount}. Balance: ${balance}")\n        break\n    index += 1\n',
                    'expected_output': 'Withdrew $100. Balance: $400\nWithdrew $200. Balance: $200\nWithdrew $150. Balance: $50\nInsufficient funds for $100. Balance: $50',
                    'hint': 'Use a while loop with an index. For each withdrawal, check if the amount is less than or equal to the balance. If yes, subtract and print. If not, print the insufficient funds message and use break to exit the loop.',
                },
            },
            {
                'id': 'while-vs-for',
                'title': 'Choosing Between for and while',
                'content': """## Choosing Between for and while

Knowing when to use `for` versus `while` is an important skill:

### Use a `for` loop when:

- You know the number of iterations in advance.
- You are iterating over a collection (list, string, range).
- You want cleaner, more readable code for counted loops.

```python
# Perfect for 'for': iterate over a known collection
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```

### Use a `while` loop when:

- You do not know how many iterations you need.
- The loop depends on a condition that changes unpredictably.
- You need more control over when to stop.

```python
# Perfect for 'while': keep going until a condition is met
balance = 1000
year = 0
while balance < 2000:
    balance *= 1.05  # 5% annual interest
    year += 1
print(f"Balance doubles in {year} years")
```

### Comparison Table

| Feature                   | `for` loop           | `while` loop           |
|---------------------------|----------------------|------------------------|
| Number of iterations      | Known                | Unknown                |
| Iterates over             | Sequences/ranges     | Until condition is met |
| Risk of infinite loop     | Very low             | Higher                 |
| Common use case           | Process each item    | Wait for condition     |

### Converting Between for and while

Any `for` loop can be written as a `while` loop (but not always vice versa):

```python
# for loop version
for i in range(5):
    print(i)

# Equivalent while loop version
i = 0
while i < 5:
    print(i)
    i += 1
```

The `for` version is preferred here because it is shorter and cannot accidentally become infinite.""",
                'exercise': None,
            },
            {
                'id': 'investment-growth-exercise',
                'title': 'Practical Exercise: Investment Growth',
                'content': """## Practical Exercise: Investment Growth

One of the most practical uses of while loops is financial calculations where you repeat a process until a target is reached.

### Compound Interest

When you invest money, you earn interest on your initial amount AND on the interest you have already earned. This is called **compound interest** and it is why savings grow faster over time.

The formula for one year of growth:

```python
balance = balance * (1 + annual_rate)
```

For example, with a 7% annual return:

```python
balance = 1000
rate = 0.07

# After year 1:
balance = balance * (1 + rate)  # 1000 * 1.07 = 1070.00

# After year 2:
balance = balance * (1 + rate)  # 1070 * 1.07 = 1144.90
```

A `while` loop is ideal here because we do not know ahead of time how many years it takes to reach a target.

### Example: How Long to Become a Millionaire?

```python
balance = 10000
annual_rate = 0.08
target = 1000000
years = 0

while balance < target:
    balance *= (1 + annual_rate)
    years += 1

print(f"Starting with $10,000 at 8% annual return:")
print(f"You reach ${target:,} in {years} years")
print(f"Final balance: ${balance:,.2f}")
```""",
                'exercise': {
                    'instructions': 'Calculate how many years it takes for an investment of $5,000 to double at an annual interest rate of 6%. Use a while loop. Print the year number and balance (formatted to 2 decimal places) for each year. After the loop, print "Investment doubled in X years!".',
                    'starter_code': '# Investment parameters\nbalance = 5000.00\nannual_rate = 0.06\ntarget = balance * 2  # double the initial investment\nyears = 0\n\n# Grow until doubled\nwhile balance < target:\n    balance = balance * (1 + annual_rate)\n    years += 1\n    print(f"Year {years}: ${balance:.2f}")\n\nprint(f"Investment doubled in {years} years!")\n',
                    'expected_output': 'Year 1: $5300.00\nYear 2: $5618.00\nYear 3: $5955.08\nYear 4: $6312.38\nYear 5: $6691.13\nYear 6: $7092.60\nYear 7: $7518.15\nYear 8: $7969.24\nYear 9: $8447.39\nYear 10: $8954.24\nYear 11: $9491.49\nYear 12: $10060.98\nInvestment doubled in 12 years!',
                    'hint': 'Start with balance = 5000 and target = 10000. In each iteration, multiply balance by (1 + annual_rate), increment years, and print. The loop runs while balance < target.',
                },
            },
        ],
    },
    {
        'title': 'Nested Loops and Loop Control',
        'description': 'Master nested loops for working with grids and tables. Learn break, continue, and the else clause to control loop flow with precision.',
        'order': 3,
        'item_order': 6,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'nested-loops',
                'title': 'Nested Loops',
                'content': """## Nested Loops

A **nested loop** is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop. This pattern is essential for working with grids, tables, and two-dimensional data.

### Real-Life Analogy

Think about a school building with classrooms:
- The **outer loop** goes through each floor (Floor 1, Floor 2, Floor 3).
- The **inner loop** goes through each room on that floor (Room A, Room B, Room C).

For every floor, you visit ALL the rooms before moving to the next floor.

```python
floors = [1, 2, 3]
rooms = ["A", "B", "C"]

for floor in floors:
    for room in rooms:
        print(f"Floor {floor}, Room {room}")
```

Output:
```
Floor 1, Room A
Floor 1, Room B
Floor 1, Room C
Floor 2, Room A
Floor 2, Room B
Floor 2, Room C
Floor 3, Room A
Floor 3, Room B
Floor 3, Room C
```

The inner loop runs 3 times for EACH of the 3 outer iterations, giving 3 x 3 = 9 total print statements.

### Real-Life Example: Multiplication Table

A multiplication table is a classic example of nested loops:

```python
# 3x3 multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # blank line between rows
```

### Understanding the Flow

It helps to trace through the execution step by step:

```
Outer loop: i = 1
    Inner loop: j = 1 -> print "1 x 1 = 1"
    Inner loop: j = 2 -> print "1 x 2 = 2"
    Inner loop: j = 3 -> print "1 x 3 = 3"
Outer loop: i = 2
    Inner loop: j = 1 -> print "2 x 1 = 2"
    Inner loop: j = 2 -> print "2 x 2 = 4"
    ... and so on
```""",
                'exercise': {
                    'instructions': 'Create a 4x4 multiplication table. For each row i (1 to 4) and column j (1 to 4), print the product formatted as a right-aligned 4-character wide number. Print each row on one line with products separated by spaces. Use the format specifier :4d for alignment.',
                    'starter_code': '# 4x4 Multiplication Table\nprint("  4x4 Multiplication Table")\nprint("-" * 25)\n\nfor i in range(1, 5):\n    row = ""\n    for j in range(1, 5):\n        row += f"{i * j:4d}"\n    print(row)\n',
                    'expected_output': '  4x4 Multiplication Table\n-------------------------\n   1   2   3   4\n   2   4   6   8\n   3   6   9  12\n   4   8  12  16',
                    'hint': 'The outer loop goes from 1 to 4 (rows). The inner loop also goes from 1 to 4 (columns). Use f"{i * j:4d}" to format each product as a 4-character wide integer. Build each row as a string, then print it.',
                },
            },
            {
                'id': 'break-statement',
                'title': 'The break Statement',
                'content': """## The break Statement

The `break` statement immediately **exits** the loop, skipping any remaining iterations. It is like an emergency exit door -- when you hit it, you are out.

### Real-Life Analogy

Imagine you are looking for your keys. You check your pockets, your bag, the kitchen counter, and the table. The moment you **find** them, you stop searching. You do not keep checking every remaining location.

```python
locations = ["pockets", "bag", "kitchen counter", "table", "coat"]
keys_location = "kitchen counter"

for location in locations:
    print(f"Checking {location}...")
    if location == keys_location:
        print(f"Found keys in {location}!")
        break
```

Output:
```
Checking pockets...
Checking bag...
Checking kitchen counter...
Found keys in kitchen counter!
```

Notice that "table" and "coat" were never checked because `break` exited the loop early.

### Real-Life Example: Finding the First Failing Grade

A teacher wants to find if any student is failing:

```python
scores = [88, 92, 75, 45, 91, 83]

for i in range(len(scores)):
    if scores[i] < 60:
        print(f"Alert: Student {i + 1} is failing with a score of {scores[i]}")
        break
else:
    print("All students are passing!")
```

### break in while Loops

`break` is especially useful in while loops to exit when a specific condition is met:

```python
# Find the first number divisible by both 3 and 7
number = 1
while True:  # this would be infinite without break
    if number % 3 == 0 and number % 7 == 0:
        print(f"Found it: {number}")
        break
    number += 1
```

### break Only Exits the Innermost Loop

In nested loops, `break` exits only the loop it is directly inside:

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # exits inner loop only
        print(f"i={i}, j={j}")
```

Output:
```
i=0, j=0
i=1, j=0
i=2, j=0
```""",
                'exercise': {
                    'instructions': 'Search through a list of daily temperatures to find the first day that exceeded 100 degrees. Print "Day X: Y degrees - Heat warning!" for that day (where X is the day number starting from 1). If no day exceeded 100, print "No extreme heat this week." Use break to stop searching after finding the first hot day.',
                    'starter_code': '# Daily temperatures for a week\ntemperatures = [85, 92, 98, 103, 95, 88, 91]\n\nfound_hot_day = False\nfor i in range(len(temperatures)):\n    if temperatures[i] > 100:\n        day = i + 1\n        print(f"Day {day}: {temperatures[i]} degrees - Heat warning!")\n        found_hot_day = True\n        break\n\nif not found_hot_day:\n    print("No extreme heat this week.")\n',
                    'expected_output': 'Day 4: 103 degrees - Heat warning!',
                    'hint': 'Loop through the temperatures list using range(len(temperatures)). Check if each temperature is greater than 100. When found, print the message with day number (index + 1) and temperature, set a flag, and break.',
                },
            },
            {
                'id': 'continue-statement',
                'title': 'The continue Statement',
                'content': """## The continue Statement

The `continue` statement **skips the rest of the current iteration** and jumps to the next one. Unlike `break`, it does not exit the loop -- it just says "skip this one and move on."

### Real-Life Analogy

You are reviewing job applications. When you see that an applicant does not have the required degree, you skip their application and move to the next one. You do not stop reviewing -- you just skip the ones that do not qualify.

```python
applicants = [
    {"name": "Alice", "has_degree": True, "years_exp": 5},
    {"name": "Bob", "has_degree": False, "years_exp": 3},
    {"name": "Charlie", "has_degree": True, "years_exp": 2},
    {"name": "Diana", "has_degree": False, "years_exp": 7},
]

print("Qualified applicants:")
for applicant in applicants:
    if not applicant["has_degree"]:
        continue  # skip this applicant
    print(f"  {applicant['name']} - {applicant['years_exp']} years experience")
```

Output:
```
Qualified applicants:
  Alice - 5 years experience
  Charlie - 2 years experience
```

### Skipping Specific Values

`continue` is handy when you want to process most items but skip a few:

```python
# Print only positive numbers
numbers = [3, -1, 4, -5, 2, -8, 6]

for num in numbers:
    if num < 0:
        continue
    print(num)
```

### continue vs. if/else

You could always rewrite `continue` using an `if/else`, but `continue` can make code cleaner by avoiding deep nesting:

```python
# With continue (flat, clean)
for item in items:
    if not item.is_valid:
        continue
    # process the item (no extra indentation)
    step_one(item)
    step_two(item)
    step_three(item)

# Without continue (nested)
for item in items:
    if item.is_valid:
        # process the item (extra indentation)
        step_one(item)
        step_two(item)
        step_three(item)
```""",
                'exercise': {
                    'instructions': 'Process a list of transactions. Skip any negative transactions (refunds) and calculate the total of only the positive transactions (sales). Print "Skipping refund: $X.XX" for each negative amount, and "Processing sale: $X.XX" for each positive amount. At the end, print the total sales.',
                    'starter_code': '# Transaction amounts (negative = refund)\ntransactions = [45.00, -12.50, 89.99, -5.00, 32.50, 15.75]\n\ntotal_sales = 0\n\nfor amount in transactions:\n    if amount < 0:\n        print(f"Skipping refund: ${abs(amount):.2f}")\n        continue\n    print(f"Processing sale: ${amount:.2f}")\n    total_sales += amount\n\nprint(f"Total sales: ${total_sales:.2f}")\n',
                    'expected_output': 'Processing sale: $45.00\nSkipping refund: $12.50\nProcessing sale: $89.99\nSkipping refund: $5.00\nProcessing sale: $32.50\nProcessing sale: $15.75\nTotal sales: $183.24',
                    'hint': 'For each transaction, check if the amount is negative. If it is, print the refund message using abs() to show the positive value, then use continue to skip to the next iteration. Otherwise, print the sale message and add the amount to total_sales.',
                },
            },
            {
                'id': 'loop-else-clause',
                'title': 'The Loop else Clause',
                'content': """## The Loop else Clause

Python has a unique feature that most other languages do not: the `else` clause on loops. The `else` block runs **only if the loop completed without hitting a break**.

### How It Works

```python
# Case 1: Loop completes normally -> else runs
for i in range(3):
    print(i)
else:
    print("Loop completed without break")

# Case 2: Loop exits via break -> else does NOT run
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will NOT print")
```

### Real-Life Example: Searching for a Product

Think of this like checking every shelf in a store:

```python
products = ["bread", "milk", "eggs", "cheese"]
search_for = "butter"

for product in products:
    if product == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"Sorry, {search_for} is not in stock.")
```

Since "butter" is not in the list, the loop completes without breaking, so the `else` block runs.

### Real-Life Example: Prime Number Check

A prime number is only divisible by 1 and itself:

```python
number = 17

if number < 2:
    print(f"{number} is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime (divisible by {i})")
            break
    else:
        print(f"{number} is prime!")
```

The `else` on the `for` loop says: "If we checked every possible divisor and never found one (never hit break), the number is prime."

### When to Use Loop else

The loop `else` clause is most useful when you are **searching** for something:
- If you find it, you `break`.
- If you do not find it, the `else` block handles that case.

It is equivalent to using a flag variable, but more concise:

```python
# With loop else (Pythonic)
for item in items:
    if matches(item):
        handle_found(item)
        break
else:
    handle_not_found()

# Without loop else (flag variable)
found = False
for item in items:
    if matches(item):
        handle_found(item)
        found = True
        break
if not found:
    handle_not_found()
```""",
                'exercise': None,
            },
            {
                'id': 'seating-chart-exercise',
                'title': 'Practical Exercise: Seating Chart Generator',
                'content': """## Practical Exercise: Seating Chart Generator

Let's combine nested loops with everything you have learned to build a practical tool.

### Seating Chart

Think about a classroom or a theater. Seats are arranged in rows and columns. A seating chart generator needs to:
1. Loop through each row (outer loop).
2. Loop through each seat in that row (inner loop).
3. Format the output neatly.

```python
rows = 3
seats_per_row = 4

print("Seating Chart")
print("=" * 30)

total_seats = 0
for row in range(1, rows + 1):
    print(f"Row {row}: ", end="")
    for seat in range(1, seats_per_row + 1):
        seat_label = f"R{row}S{seat}"
        print(f" {seat_label}", end="")
        total_seats += 1
    print()  # new line after each row

print("=" * 30)
print(f"Total seats: {total_seats}")
```

### Pattern Building with Nested Loops

Nested loops are great for building text patterns:

```python
# Right triangle
height = 5
for i in range(1, height + 1):
    print("*" * i)
```

Output:
```
*
**
***
****
*****
```""",
                'exercise': {
                    'instructions': 'Build a simple seating chart for a small theater with 3 rows and 5 seats per row. Print a header, then for each row print the row number followed by the seat labels (format: R1S1, R1S2, etc.). After all rows, print the total number of seats. Match the exact output format shown.',
                    'starter_code': '# Theater seating chart\nrows = 3\nseats_per_row = 5\n\nprint("Theater Seating Chart")\nprint("-" * 35)\n\ntotal_seats = 0\nfor row in range(1, rows + 1):\n    seat_labels = []\n    for seat in range(1, seats_per_row + 1):\n        seat_labels.append(f"R{row}S{seat}")\n        total_seats += 1\n    print(f"Row {row}: {\'  \'.join(seat_labels)}")\n\nprint("-" * 35)\nprint(f"Total seats: {total_seats}")\n',
                    'expected_output': 'Theater Seating Chart\n-----------------------------------\nRow 1: R1S1  R1S2  R1S3  R1S4  R1S5\nRow 2: R2S1  R2S2  R2S3  R2S4  R2S5\nRow 3: R3S1  R3S2  R3S3  R3S4  R3S5\n-----------------------------------\nTotal seats: 15',
                    'hint': 'Use an outer loop for rows (1 to 3) and an inner loop for seats (1 to 5). Build a list of seat labels for each row using append(), then join them with two spaces using "  ".join(seat_labels).',
                },
            },
        ],
    },
]
