CHAPTER_ORDER = 4

LESSONS = [
    {
        'title': 'Defining and Calling Functions',
        'description': 'Learn how to create reusable blocks of code with functions using the def keyword, pass data with parameters, and get results back with return values.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'why-functions',
                'title': 'Why Functions? A Real-World Perspective',
                'content': """## Why Functions? A Real-World Perspective

Imagine you run a bakery and every morning you follow the same steps to make bread: measure flour, add water, knead the dough, let it rise, and bake. You don't reinvent the process each day -- you follow a **recipe**. In programming, a **function** is exactly like a recipe: a named set of instructions you can reuse whenever you need them.

### The Problem Without Functions

Without functions, you end up repeating the same code over and over:

```python
# Greeting customer 1
print("=" * 30)
print("Welcome to Python Bakery!")
print("We are glad to have you.")
print("=" * 30)

# Greeting customer 2 - same code again!
print("=" * 30)
print("Welcome to Python Bakery!")
print("We are glad to have you.")
print("=" * 30)
```

This violates the **DRY principle** (Don't Repeat Yourself). If you want to change the greeting, you must update it everywhere.

### The Solution: Functions

A function lets you write the logic once and call it as many times as you need:

```python
def greet_customer():
    print("=" * 30)
    print("Welcome to Python Bakery!")
    print("We are glad to have you.")
    print("=" * 30)

greet_customer()  # Call it for customer 1
greet_customer()  # Call it for customer 2
```

### Benefits of Functions

1. **Reusability** -- Write once, use many times (like a recipe card you pull out each morning).
2. **Organization** -- Break large programs into manageable pieces (like chapters in a book).
3. **Maintainability** -- Fix a bug in one place instead of hunting through repeated code.
4. **Abstraction** -- Use a function without knowing its internal details (like pressing a microwave button without understanding the electronics).""",
                'exercise': None,
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange these code blocks to define a function and call it:',
                    'code_blocks': [
                        'def say_hello():',
                        '    print("Hello!")',
                        '',
                        'say_hello()',
                    ],
                    'explanation': 'First we define the function with def and its body (indented). Then we leave a blank line, and call the function by writing its name with parentheses!',
                },
            },
            {
                'id': 'defining-functions',
                'title': 'Defining Functions with def',
                'content': """## Defining Functions with `def`

You create a function using the `def` keyword, followed by the function name, parentheses, and a colon. The indented block below is the **function body**:

```python
def function_name():
    # function body - indented code
    statement_1
    statement_2
```

### Anatomy of a Function

Think of it like writing a recipe card:

- **`def`** -- announces "I am defining a recipe."
- **Function name** -- the label on the card (e.g., `make_coffee`).
- **Parentheses `()`** -- the list of ingredients (parameters) needed.
- **Colon `:`** -- marks the start of the instructions.
- **Indented body** -- the step-by-step instructions.

```python
def make_coffee():
    print("1. Boil water")
    print("2. Add coffee grounds to filter")
    print("3. Pour hot water over grounds")
    print("4. Wait 4 minutes")
    print("5. Pour and enjoy!")
```

### Calling a Function

Defining a function does **not** run it. You must **call** it by writing its name followed by parentheses:

```python
def say_hello():
    print("Hello there!")

# Nothing happens until we call it:
say_hello()   # Hello there!
say_hello()   # Hello there!
```

### Naming Conventions

Function names follow the same rules as variables:

- Use **snake_case** (lowercase with underscores): `calculate_tax`, `send_email`
- Choose **descriptive verb-based names** that say what the function does
- Avoid single letters or vague names like `do_stuff`

```python
# Good names - clear about what they do
def calculate_area():
    pass

def send_welcome_email():
    pass

# Bad names - vague or unclear
def thing():
    pass

def x():
    pass
```""",
                'exercise': {
                    'instructions': 'Define a function called `print_receipt_header` that prints three lines: a line of 30 dashes, the text "PYTHON GROCERY STORE", and another line of 30 dashes. Then call the function once.',
                    'starter_code': '# Define the function\ndef print_receipt_header():\n    print("-" * 30)\n    print("PYTHON GROCERY STORE")\n    print("-" * 30)\n\n# Call the function\nprint_receipt_header()\n',
                    'expected_output': '------------------------------\nPYTHON GROCERY STORE\n------------------------------',
                    'hint': 'Use print("-" * 30) to print 30 dashes. Define the function with def, then call it by writing its name with parentheses.',
                },
            },
            {
                'id': 'parameters-and-arguments',
                'title': 'Parameters and Arguments',
                'content': """## Parameters and Arguments

Functions become truly powerful when they accept **input**. Think of a vending machine: you select a drink (input), the machine processes your choice, and out comes your beverage (output). The selection button is like a **parameter**.

### Defining Parameters

**Parameters** are variables listed inside the parentheses of a function definition. They act as placeholders for the values you will pass in:

```python
def greet(name):
    print(f"Hello, {name}! Welcome aboard.")

greet("Alice")   # Hello, Alice! Welcome aboard.
greet("Bob")     # Hello, Bob! Welcome aboard.
```

- **Parameter** -- the variable name in the definition (`name`).
- **Argument** -- the actual value passed when calling the function (`"Alice"`).

### Multiple Parameters

Just like a recipe might require multiple ingredients, a function can accept multiple parameters separated by commas:

```python
def describe_pet(pet_name, pet_type):
    print(f"{pet_name} is a {pet_type}.")

describe_pet("Buddy", "dog")     # Buddy is a dog.
describe_pet("Whiskers", "cat")  # Whiskers is a cat.
```

### Real-Life Example: Restaurant Bill Calculator

Imagine a restaurant tip calculator. It needs the bill amount and the tip percentage:

```python
def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    print(f"Bill: ${bill_amount:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip:.2f}")
    print(f"Total: ${total:.2f}")

calculate_tip(50.00, 20)
# Bill: $50.00
# Tip (20%): $10.00
# Total: $60.00
```

### Positional vs. Keyword Arguments

By default, arguments are matched by **position**. You can also pass them by **name** for clarity:

```python
def create_profile(name, age, city):
    print(f"{name}, age {age}, from {city}")

# Positional - order matters
create_profile("Alice", 30, "New York")

# Keyword - order does not matter
create_profile(city="Boston", name="Bob", age=25)
```""",
                'exercise': {
                    'instructions': 'Define a function called `calculate_rectangle_area` that takes two parameters: `length` and `width`. It should print a message in the format "A rectangle of 8 x 5 has an area of 40". Call the function twice: once with length=8, width=5, and once with length=12, width=3.',
                    'starter_code': '# Define the function\ndef calculate_rectangle_area(length, width):\n    area = length * width\n    print(f"A rectangle of {length} x {width} has an area of {area}")\n\n# Call with length=8, width=5\ncalculate_rectangle_area(8, 5)\n\n# Call with length=12, width=3\ncalculate_rectangle_area(12, 3)\n',
                    'expected_output': 'A rectangle of 8 x 5 has an area of 40\nA rectangle of 12 x 3 has an area of 36',
                    'hint': 'Multiply length by width to get the area. Use an f-string to format the output message with the values.',
                },
            },
            {
                'id': 'return-values',
                'title': 'Return Values',
                'content': """## Return Values

So far our functions have only printed output. But in real programs, you usually want a function to **give back a result** that you can store, combine, or use elsewhere. This is what the `return` statement does.

Think of it this way: when you ask a cashier "How much do I owe?", you don't want them to shout the answer into the void -- you want the **value back** so you can decide what to do with it.

### The `return` Statement

```python
def add(a, b):
    return a + b

result = add(3, 7)
print(result)  # 10
```

When Python hits a `return` statement, it:
1. Evaluates the expression after `return`.
2. Sends that value back to wherever the function was called.
3. **Exits the function immediately** -- any code after `return` is not executed.

```python
def check_age(age):
    if age >= 18:
        return "adult"
    return "minor"
    print("This line never runs")  # unreachable code

status = check_age(21)
print(status)  # adult
```

### Functions Without `return`

If a function has no `return` statement (or just `return` with no value), it returns `None`:

```python
def say_hi():
    print("Hi!")

result = say_hi()  # prints Hi!
print(result)       # None
```

### Real-Life Example: Unit Price Calculator

Imagine you are building a shopping app. You need a function that computes the unit price so you can compare deals:

```python
def unit_price(total_price, quantity):
    if quantity == 0:
        return 0.0
    return total_price / quantity

# Compare two products
price_a = unit_price(5.99, 6)   # $0.998 per unit
price_b = unit_price(8.49, 12)  # $0.7075 per unit

print(f"Product A: ${price_a:.2f} per unit")
print(f"Product B: ${price_b:.2f} per unit")

if price_b < price_a:
    print("Product B is the better deal!")
```

### Using Return Values in Expressions

Because a function call evaluates to its return value, you can use it anywhere you would use a value:

```python
def square(n):
    return n * n

# Use directly in expressions
total = square(3) + square(4)
print(total)  # 25

# Use in f-strings
print(f"5 squared is {square(5)}")  # 5 squared is 25

# Use in conditions
if square(6) > 30:
    print("That is a big number!")
```""",
                'exercise': {
                    'instructions': 'Define a function called `celsius_to_fahrenheit` that takes a `celsius` parameter and returns the Fahrenheit value using the formula: F = C * 9/5 + 32. Then call the function for 0, 100, and 37 degrees Celsius and print each result.',
                    'starter_code': '# Define the conversion function\ndef celsius_to_fahrenheit(celsius):\n    fahrenheit = celsius * 9/5 + 32\n    return fahrenheit\n\n# Convert and print three temperatures\nprint(celsius_to_fahrenheit(0))\nprint(celsius_to_fahrenheit(100))\nprint(celsius_to_fahrenheit(37))\n',
                    'expected_output': '32.0\n212.0\n98.60000000000001',
                    'hint': 'Use the formula celsius * 9/5 + 32. The function should return the result, not print it. Use print() when calling the function.',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Look at this code and pick the correct answer:',
                    'code_snippet': 'def double(x):\n    return x * 2\n\nprint(double(5))',
                    'question': 'What will this code print?',
                    'options': [
                        {'text': '10', 'correct': True},
                        {'text': '5', 'correct': False},
                        {'text': '25', 'correct': False},
                        {'text': 'double(5)', 'correct': False},
                    ],
                    'explanation': 'The function double() takes a number and returns it multiplied by 2. double(5) calculates 5 * 2 = 10 and returns it, which gets printed!',
                },
            },
            {
                'id': 'putting-it-together',
                'title': 'Putting It All Together: A Grade Calculator',
                'content': """## Putting It All Together: A Grade Calculator

Let's combine everything we have learned to build a small but realistic program. Imagine you are a teacher who needs to calculate letter grades from numeric scores.

### Breaking Down the Problem

A good approach is to split the problem into small, focused functions -- like having separate workers on an assembly line, each responsible for one task:

```python
def calculate_average(scores):
    \"\"\"Calculate the average of a list of scores.\"\"\"
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def get_letter_grade(average):
    \"\"\"Convert a numeric average to a letter grade.\"\"\"
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def print_report(student_name, scores):
    \"\"\"Print a full grade report for a student.\"\"\"
    avg = calculate_average(scores)
    grade = get_letter_grade(avg)
    print(f"Student: {student_name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
```

### Why Multiple Small Functions?

Think of it like a restaurant kitchen:

- **`calculate_average`** is like the prep cook -- handles one specific job (averaging numbers).
- **`get_letter_grade`** is like the quality inspector -- takes a number and classifies it.
- **`print_report`** is like the head chef -- orchestrates the other functions to produce the final dish.

Each function is:
- **Easy to test** -- you can verify `get_letter_grade(85)` returns `"B"` without running the whole program.
- **Easy to reuse** -- `calculate_average` works for any list of numbers, not just grades.
- **Easy to modify** -- changing the grade thresholds only requires editing one function.

### Docstrings

Notice the triple-quoted strings right after each `def` line. These are **docstrings** -- documentation that explains what the function does:

```python
def calculate_area(radius):
    \"\"\"Calculate the area of a circle given its radius.\"\"\"
    return 3.14159 * radius ** 2

# Access the docstring
print(calculate_area.__doc__)
# Calculate the area of a circle given its radius.
```

Docstrings are a best practice that makes your code self-documenting.""",
                'exercise': {
                    'instructions': 'Create two functions: `calculate_average` that takes three scores as parameters and returns their average, and `get_letter_grade` that takes a numeric average and returns "A" for 90+, "B" for 80+, "C" for 70+, "D" for 60+, or "F" otherwise. Use them together to print the average and grade for scores 85, 92, and 78.',
                    'starter_code': '# Function to calculate the average of three scores\ndef calculate_average(score1, score2, score3):\n    return (score1 + score2 + score3) / 3\n\n# Function to determine the letter grade\ndef get_letter_grade(average):\n    if average >= 90:\n        return "A"\n    elif average >= 80:\n        return "B"\n    elif average >= 70:\n        return "C"\n    elif average >= 60:\n        return "D"\n    else:\n        return "F"\n\n# Calculate and display results for scores 85, 92, 78\navg = calculate_average(85, 92, 78)\ngrade = get_letter_grade(avg)\nprint(f"Average: {avg:.1f}")\nprint(f"Grade: {grade}")\n',
                    'expected_output': 'Average: 85.0\nGrade: B',
                    'hint': 'The average of 85, 92, and 78 is 85.0. Since 85 is >= 80 but < 90, the letter grade is "B". Use :.1f to format the average to one decimal place.',
                },
            },
        ],
    },
    {
        'title': 'Parameters, Return Values, and Scope',
        'description': 'Explore default parameters, flexible argument packing with *args and **kwargs, returning multiple values, and understand how variable scope works in Python.',
        'order': 2,
        'item_order': 4,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'default-parameters',
                'title': 'Default Parameters',
                'content': """## Default Parameters

Sometimes a function parameter has a value that is used most of the time. Instead of forcing the caller to always supply it, you can set a **default value**. Think of ordering coffee: if you don't specify a size, the barista gives you a medium. That medium is the **default parameter**.

### Syntax

Place an `=` after the parameter name to assign a default:

```python
def order_coffee(size="medium", sugar=2):
    print(f"One {size} coffee with {sugar} sugar(s).")

order_coffee()                      # One medium coffee with 2 sugar(s).
order_coffee("large")               # One large coffee with 2 sugar(s).
order_coffee("small", 0)            # One small coffee with 0 sugar(s).
order_coffee(sugar=3)               # One medium coffee with 3 sugar(s).
```

### Rules for Default Parameters

1. **Parameters with defaults must come after parameters without defaults:**

```python
def greet(name, greeting="Hello"):   # Valid
    print(f"{greeting}, {name}!")

# def greet(greeting="Hello", name):  # SyntaxError!
```

2. **Default values are evaluated once** when the function is defined, not each time it is called. Be careful with mutable defaults like lists:

```python
# Dangerous - the same list is shared across calls
def add_item_bad(item, items=[]):
    items.append(item)
    return items

# Safe pattern - use None and create a new list inside
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Real-Life Example: Shipping Cost Calculator

An online store might calculate shipping with a default rate that can be overridden for express delivery:

```python
def calculate_shipping(weight, rate_per_kg=5.00, handling_fee=2.50):
    cost = weight * rate_per_kg + handling_fee
    return cost

# Standard shipping
standard = calculate_shipping(3)
print(f"Standard: ${standard:.2f}")   # Standard: $17.50

# Express shipping (higher rate)
express = calculate_shipping(3, rate_per_kg=9.00)
print(f"Express: ${express:.2f}")     # Express: $29.50
```""",
                'exercise': {
                    'instructions': 'Define a function called `make_sandwich` that takes a `bread` parameter (no default) and two optional parameters: `filling` with default "turkey" and `condiment` with default "mustard". It should print "bread bread sandwich with filling and condiment". Call it three times: with just "wheat", with "rye" and filling="ham", and with "white", "tuna", "mayo".',
                    'starter_code': '# Define the function with default parameters\ndef make_sandwich(bread, filling="turkey", condiment="mustard"):\n    print(f"{bread} bread sandwich with {filling} and {condiment}")\n\n# Call with just bread type\nmake_sandwich("wheat")\n\n# Call with bread and custom filling\nmake_sandwich("rye", filling="ham")\n\n# Call with all three specified\nmake_sandwich("white", "tuna", "mayo")\n',
                    'expected_output': 'wheat bread sandwich with turkey and mustard\nrye bread sandwich with ham and mustard\nwhite bread sandwich with tuna and mayo',
                    'hint': 'Parameters with defaults are optional when calling the function. You can override defaults by passing values positionally or using keyword arguments like filling="ham".',
                },
            },
            {
                'id': 'args-and-kwargs',
                'title': 'Flexible Arguments: *args and **kwargs',
                'content': """## Flexible Arguments: `*args` and `**kwargs`

Sometimes you don't know in advance how many arguments a function will receive. Think of a restaurant that takes group orders -- some tables have 2 guests, others have 10. You need a flexible way to handle any number of orders.

### `*args` -- Variable Positional Arguments

The `*args` syntax collects any number of positional arguments into a **tuple**:

```python
def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print(calculate_total(9.99, 14.50))            # 24.49
print(calculate_total(5.00, 12.00, 8.50, 3.25))  # 28.75
print(calculate_total(42.00))                   # 42.0
```

The name `args` is a convention -- you could use any name after the `*`, but `args` is standard.

### Real-Life Example: Restaurant Order System

```python
def take_order(table_number, *items):
    print(f"Order for Table {table_number}:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")
    print(f"  Total items: {len(items)}")

take_order(5, "Burger", "Fries", "Cola")
```

### `**kwargs` -- Variable Keyword Arguments

The `**kwargs` syntax collects any number of keyword arguments into a **dictionary**:

```python
def build_profile(name, **details):
    print(f"Profile for {name}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

build_profile("Alice", age=30, city="New York", role="Engineer")
```

### Combining All Parameter Types

The order must be: regular parameters, `*args`, keyword-only parameters, `**kwargs`:

```python
def full_example(required, *args, default="yes", **kwargs):
    print(f"Required: {required}")
    print(f"Extra args: {args}")
    print(f"Default: {default}")
    print(f"Keyword args: {kwargs}")
```

### Practical Example: Flexible Logger

```python
def log_message(level, *messages, separator=" | "):
    combined = separator.join(messages)
    print(f"[{level.upper()}] {combined}")

log_message("info", "Server started", "Port 8080")
# [INFO] Server started | Port 8080

log_message("error", "File not found", "config.yaml", separator=" -> ")
# [ERROR] File not found -> config.yaml
```""",
                'exercise': {
                    'instructions': 'Define a function called `print_shopping_list` that takes a `store_name` parameter followed by `*items`. It should print the store name as a header, then each item numbered starting from 1, then the total count. Call it with "SuperMart" and items "Milk", "Bread", "Eggs".',
                    'starter_code': '# Define function with *args\ndef print_shopping_list(store_name, *items):\n    print(f"Shopping list for {store_name}:")\n    for i, item in enumerate(items, 1):\n        print(f"  {i}. {item}")\n    print(f"Total: {len(items)} items")\n\n# Call the function\nprint_shopping_list("SuperMart", "Milk", "Bread", "Eggs")\n',
                    'expected_output': 'Shopping list for SuperMart:\n  1. Milk\n  2. Bread\n  3. Eggs\nTotal: 3 items',
                    'hint': 'Use *items to accept any number of arguments. Use enumerate(items, 1) to number them starting from 1. Use len(items) for the count.',
                },
            },
            {
                'id': 'multiple-return-values',
                'title': 'Returning Multiple Values',
                'content': """## Returning Multiple Values

Python functions can return more than one value by using a **tuple**. This is like getting a full report back from a doctor visit -- not just one measurement, but your blood pressure, heart rate, and temperature all at once.

### Returning a Tuple

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

# The function returns a tuple
result = get_min_max([4, 1, 8, 2, 9])
print(result)        # (1, 9)
print(type(result))  # <class 'tuple'>
```

### Tuple Unpacking

The most common pattern is to **unpack** the returned values directly into separate variables:

```python
lowest, highest = get_min_max([4, 1, 8, 2, 9])
print(f"Lowest: {lowest}")    # Lowest: 1
print(f"Highest: {highest}")  # Highest: 9
```

### Real-Life Example: Tax Calculator

When you calculate a purchase total, you often need both the tax amount and the final total:

```python
def calculate_bill(subtotal, tax_rate=8.5):
    tax = subtotal * (tax_rate / 100)
    total = subtotal + tax
    return tax, total

tax_amount, final_total = calculate_bill(75.00)
print(f"Tax: ${tax_amount:.2f}")
print(f"Total: ${final_total:.2f}")
# Tax: $6.38
# Total: $81.38
```

### Returning Dictionaries for Named Results

When you have many values to return, a dictionary can be clearer than a long tuple:

```python
def analyze_text(text):
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text),
        "average_word_length": sum(len(w) for w in words) / len(words)
    }

stats = analyze_text("Python is a great programming language")
print(f"Words: {stats['word_count']}")
print(f"Characters: {stats['char_count']}")
```

### Real-Life Example: Divmod -- Quotient and Remainder

Python's built-in `divmod()` function is a perfect example of returning two values:

```python
# How many full hours and remaining minutes in 135 minutes?
hours, minutes = divmod(135, 60)
print(f"{hours} hours and {minutes} minutes")  # 2 hours and 15 minutes
```""",
                'exercise': None,
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this code will print? Type your guess!',
                    'code_snippet': 'def add(a, b):\n    return a + b\n\nresult = add(3, 7)\nprint(result)',
                    'expected_output': '10',
                    'explanation': 'The function add() takes two numbers, adds them with +, and returns the result. add(3, 7) returns 10, which gets stored in result and printed!',
                },
            },
            {
                'id': 'variable-scope',
                'title': 'Variable Scope: Local vs. Global',
                'content': """## Variable Scope: Local vs. Global

**Scope** determines where a variable can be accessed. Think of it like rooms in a house: a lamp (variable) inside your bedroom (function) is only usable in that room. A lamp in the hallway (global scope) is visible from anywhere.

### Local Scope

Variables created inside a function are **local** -- they exist only while the function runs and cannot be accessed outside:

```python
def make_greeting():
    message = "Hello!"   # local variable
    print(message)

make_greeting()    # Hello!
# print(message)   # NameError: 'message' is not defined
```

Each function call creates **its own** local scope:

```python
def count_up():
    counter = 0
    counter += 1
    print(counter)

count_up()  # 1
count_up()  # 1 - counter starts fresh each time
```

### Global Scope

Variables created outside any function are **global** -- they can be read from anywhere:

```python
app_name = "My Calculator"   # global variable

def show_header():
    print(f"=== {app_name} ===")  # reading global is fine

show_header()  # === My Calculator ===
```

### Modifying Global Variables

To **modify** a global variable inside a function, you must use the `global` keyword:

```python
total_sales = 0

def record_sale(amount):
    global total_sales
    total_sales += amount

record_sale(50)
record_sale(30)
print(total_sales)  # 80
```

**However**, using `global` is generally discouraged. A better approach is to use parameters and return values:

```python
def record_sale(current_total, amount):
    return current_total + amount

total_sales = 0
total_sales = record_sale(total_sales, 50)
total_sales = record_sale(total_sales, 30)
print(total_sales)  # 80
```

### The LEGB Rule

Python looks up variable names in this order:

1. **L**ocal -- inside the current function
2. **E**nclosing -- in any enclosing (outer) function
3. **G**lobal -- at the module level
4. **B**uilt-in -- Python's built-in names (`print`, `len`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # local

    inner()
    print(x)        # enclosing

outer()
print(x)            # global
```""",
                'exercise': {
                    'instructions': 'Study the code below that demonstrates local vs. global scope. A global variable `app_name` is defined, and two functions interact with it. Fill in the missing parts so the output matches exactly. The function `display_info` should read the global `app_name`, and `process_score` should compute and return the result.',
                    'starter_code': '# Global variable\napp_name = "Grade Tracker"\n\ndef display_info():\n    version = "1.0"\n    print(f"{app_name} v{version}")\n\ndef process_score(score, bonus):\n    adjusted = score + bonus\n    return adjusted\n\n# Call display_info\ndisplay_info()\n\n# Use process_score and print the result\nfinal_score = process_score(85, 5)\nprint(f"Final score: {final_score}")\n',
                    'expected_output': 'Grade Tracker v1.0\nFinal score: 90',
                    'hint': 'display_info reads the global app_name and a local version. process_score adds score and bonus together and returns the result.',
                },
            },
            {
                'id': 'scope-best-practices',
                'title': 'Best Practices and Common Patterns',
                'content': """## Best Practices and Common Patterns

### 1. Keep Functions Focused

Each function should do **one thing well** -- like workers on an assembly line. If a function is getting long or doing multiple unrelated tasks, split it up:

```python
# Instead of one giant function...
def process_order_bad(items, customer, address):
    # validate items... calculate total... apply discount...
    # format address... send confirmation... update inventory...
    pass

# Break it into focused functions
def calculate_order_total(items):
    return sum(item["price"] * item["qty"] for item in items)

def apply_discount(total, discount_percent):
    return total * (1 - discount_percent / 100)

def format_address(street, city, state, zip_code):
    return f"{street}, {city}, {state} {zip_code}"
```

### 2. Prefer Return Values Over Global Variables

Functions that take input and return output are easier to understand, test, and debug:

```python
# Bad - relies on and modifies global state
balance = 1000
def withdraw_bad(amount):
    global balance
    balance -= amount

# Good - pure function with no side effects
def withdraw_good(balance, amount):
    return balance - amount

my_balance = 1000
my_balance = withdraw_good(my_balance, 200)
print(my_balance)  # 800
```

### 3. Use Docstrings

Always document what your function does, its parameters, and what it returns:

```python
def calculate_bmi(weight_kg, height_m):
    \"\"\"Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:
        The BMI as a float.
    \"\"\"
    return weight_kg / (height_m ** 2)
```

### 4. Reasonable Number of Parameters

If a function needs more than 4-5 parameters, consider grouping related data into a dictionary or using default parameters to simplify calls:

```python
# Too many parameters
def create_user(name, age, email, phone, street, city, state, zip_code):
    pass

# Better - group related data
def create_user(name, age, email, contact_info):
    pass
```

### Summary of Chapter 4

| Concept | Description |
|---------|-------------|
| `def` | Defines a new function |
| Parameters | Variables in the function definition |
| Arguments | Values passed when calling the function |
| `return` | Sends a value back to the caller |
| Default parameters | Provide fallback values for optional arguments |
| `*args` | Collects extra positional arguments into a tuple |
| `**kwargs` | Collects extra keyword arguments into a dictionary |
| Local scope | Variables inside a function, not accessible outside |
| Global scope | Variables outside functions, readable everywhere |""",
                'exercise': {
                    'instructions': 'Create a function called `calculate_total_price` that takes a `base_price`, an optional `tax_rate` (default 8.5), and an optional `discount_percent` (default 0). It should calculate the discounted price first (base_price minus the discount), then add tax, and return both the tax amount and final total. Use tuple unpacking to capture the results and print them formatted to 2 decimal places.',
                    'starter_code': '# Define the function\ndef calculate_total_price(base_price, tax_rate=8.5, discount_percent=0):\n    discounted = base_price * (1 - discount_percent / 100)\n    tax = discounted * (tax_rate / 100)\n    total = discounted + tax\n    return tax, total\n\n# Call without discount\ntax1, total1 = calculate_total_price(100.00)\nprint(f"Tax: ${tax1:.2f}, Total: ${total1:.2f}")\n\n# Call with 20% discount\ntax2, total2 = calculate_total_price(100.00, discount_percent=20)\nprint(f"Tax: ${tax2:.2f}, Total: ${total2:.2f}")\n',
                    'expected_output': 'Tax: $8.50, Total: $108.50\nTax: $6.80, Total: $86.80',
                    'hint': 'First apply the discount: base_price * (1 - discount_percent/100). Then calculate tax on the discounted price. Return both the tax and the total (discounted + tax).',
                },
            },
        ],
    },
]
