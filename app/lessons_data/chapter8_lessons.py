CHAPTER_ORDER = 8

LESSONS = [
    # ------------------------------------------------------------------ #
    # Lesson 1 -- Decorators and Generators
    # ------------------------------------------------------------------ #
    {
        'title': 'Decorators and Generators',
        'description': 'Understand function decorators with the @syntax and generator functions using yield - powerful patterns for writing clean, efficient Python code.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'understanding-decorators',
                'title': 'Understanding Decorators',
                'content': """## Understanding Decorators

A **decorator** is a function that takes another function as input and returns a new function that usually extends or modifies the original function's behaviour. Decorators are used everywhere in real-world Python -- web frameworks, logging systems, access control, and performance monitoring all rely on them.

### Real-Life Analogy

Think of a decorator like a gift wrapper at a store. You hand over a plain item (your function), and the wrapper adds a decorative layer around it (extra behaviour) without changing the item itself. The result is still your item -- it just comes with something extra on the outside.

### Functions Are Objects

In Python, functions are **first-class objects**. This means you can assign them to variables, pass them as arguments, and return them from other functions:

```python
def greet(name):
    return f"Hello, {name}!"

# Assign function to a variable
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Pass a function as an argument
def call_twice(func, arg):
    print(func(arg))
    print(func(arg))

call_twice(greet, "Bob")
# Hello, Bob!
# Hello, Bob!
```

### Writing Your First Decorator

A decorator is a function that wraps another function:

```python
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # HELLO, ALICE
```

Without the `@shout` syntax, this is equivalent to:

```python
greet = shout(greet)
```

### The `@` Syntax

The `@decorator` placed above a function definition is syntactic sugar. It is the standard way to apply decorators in Python:

```python
@decorator
def my_function():
    pass

# Same as:
# my_function = decorator(my_function)
```""",
                'exercise': None,
            },
            {
                'id': 'practical-decorators',
                'title': 'Practical Decorators',
                'content': """## Practical Decorators

Decorators become truly powerful when you apply them to real-world tasks. Let us look at some common patterns you will encounter in professional Python code.

### Timing Functions -- Performance Monitoring

Imagine you are a web developer and you need to find out which of your functions are slow. A timer decorator lets you measure execution time without cluttering every function with timing code:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def process_order(items):
    # Simulate processing an e-commerce order
    total = sum(item['price'] * item['qty'] for item in items)
    time.sleep(0.1)  # Simulate database write
    return total
```

### Logging Decorator -- Audit Trail

In banking or healthcare software, every function call may need to be logged for auditing:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def transfer_funds(from_acct, to_acct, amount):
    # Simulate a bank transfer
    return f"Transferred ${amount} from {from_acct} to {to_acct}"
```

### Preserving Function Metadata with `functools.wraps`

When you wrap a function, the wrapper replaces the original function's name and docstring. Use `functools.wraps` to preserve them:

```python
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper
```

### Decorator with Arguments (Decorator Factory)

Sometimes you need to pass configuration to a decorator. This requires an extra layer of nesting -- a function that returns a decorator:

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")
    return name

say_hello("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```""",
                'exercise': {
                    'instructions': 'Create a decorator called `bold` that wraps the return value of a function in HTML bold tags. Then apply it to the `greet` function. The decorator should take the string returned by the function and return it wrapped like `<b>original string</b>`.',
                    'starter_code': 'from functools import wraps\n\n\ndef bold(func):\n    """Decorator that wraps the return value in <b> tags."""\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        result = func(*args, **kwargs)\n        return f"<b>{result}</b>"\n    return wrapper\n\n\n@bold\ndef greet(name):\n    return f"Hello, {name}"\n\n\n# Test the decorator\nprint(greet("Alice"))\nprint(greet("Bob"))\nprint(greet.__name__)\n',
                    'expected_output': '<b>Hello, Alice</b>\n<b>Hello, Bob</b>\ngreet',
                    'hint': 'The wrapper function should call the original function, capture its return value, and return that value wrapped in <b> tags using an f-string.',
                },
            },
            {
                'id': 'generator-functions',
                'title': 'Generator Functions and yield',
                'content': """## Generator Functions and `yield`

A **generator function** is a special kind of function that produces a sequence of values lazily -- one at a time, on demand -- instead of computing them all at once and storing them in memory.

### Real-Life Analogy

Think of a generator like a ticket machine at a deli counter. It does not print all 500 tickets at once. Instead, each customer presses a button and gets the next number. The machine only produces one ticket at a time, saving paper and space.

### Regular Function vs Generator

```python
# Regular function -- builds entire list in memory
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator function -- produces one value at a time
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2
```

The key difference is `yield` instead of `return`. When Python encounters `yield`, it **pauses** the function and remembers its state. The next time you ask for a value, it **resumes** from where it left off.

### Using Generators

```python
# Create the generator object
squares = get_squares_gen(5)

# Iterate one at a time
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4

# Or use a for loop (most common)
for sq in get_squares_gen(5):
    print(sq)
# 0, 1, 4, 9, 16
```

### Why Generators Matter -- Lazy Loading Large Datasets

Imagine you need to process a 10 GB log file. Loading it all into memory would crash your program. A generator reads one line at a time:

```python
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

# Process millions of lines without running out of memory
for line in read_large_file("server.log"):
    if "ERROR" in line:
        print(line)
```

### Generator Expressions

Just like list comprehensions, you can create generators with a compact syntax using parentheses instead of brackets:

```python
# List comprehension -- stores all values in memory
squares_list = [x ** 2 for x in range(1000000)]

# Generator expression -- produces values on demand
squares_gen = (x ** 2 for x in range(1000000))

# The generator uses almost no memory
print(sum(squares_gen))  # Computes sum without storing all values
```""",
                'exercise': {
                    'instructions': 'Create a generator function called `countdown` that takes a number `n` and yields numbers from `n` down to 1. Then create another generator called `even_numbers` that takes a limit and yields even numbers from 2 up to (and including) that limit. Test both generators by converting them to lists.',
                    'starter_code': 'def countdown(n):\n    """Yield numbers from n down to 1."""\n    while n >= 1:\n        yield n\n        n -= 1\n\n\ndef even_numbers(limit):\n    """Yield even numbers from 2 up to and including limit."""\n    num = 2\n    while num <= limit:\n        yield num\n        num += 2\n\n\n# Test countdown\nprint(list(countdown(5)))\n\n# Test even_numbers\nprint(list(even_numbers(10)))\n\n# Show that generators are lazy -- use next()\ngen = countdown(3)\nprint(next(gen))\nprint(next(gen))\nprint(next(gen))\n',
                    'expected_output': '[5, 4, 3, 2, 1]\n[2, 4, 6, 8, 10]\n3\n2\n1',
                    'hint': 'Use a while loop with yield. For countdown, start at n and decrement. For even_numbers, start at 2 and increment by 2 while the number is less than or equal to the limit.',
                },
            },
            {
                'id': 'chaining-generators-and-decorators',
                'title': 'Combining Generators and Decorators',
                'content': """## Combining Generators and Decorators

In professional Python code, generators and decorators are often used together to build elegant data processing pipelines.

### Real-Life Example: E-Commerce Order Processing

Imagine an online store that needs to process thousands of orders. Each step in the pipeline handles one concern:

```python
def read_orders(order_list):
    \"\"\"Generator: yield each order one at a time.\"\"\"
    for order in order_list:
        yield order

def filter_valid(orders):
    \"\"\"Generator: only yield orders with positive totals.\"\"\"
    for order in orders:
        if order['total'] > 0:
            yield order

def apply_discount(orders, rate):
    \"\"\"Generator: apply a discount to each order.\"\"\"
    for order in orders:
        order['total'] = round(order['total'] * (1 - rate), 2)
        yield order

# Build the pipeline
raw_orders = [
    {'id': 1, 'total': 100.00},
    {'id': 2, 'total': -5.00},    # invalid
    {'id': 3, 'total': 250.00},
]

pipeline = apply_discount(filter_valid(read_orders(raw_orders)), 0.10)

for order in pipeline:
    print(f"Order {order['id']}: ${order['total']}")
# Order 1: $90.0
# Order 3: $225.0
```

Each generator only processes one item at a time. Even with millions of orders, memory usage stays constant.

### Fibonacci Sequence Generator

The Fibonacci sequence appears in nature (flower petals, pinecone spirals) and in computer science (algorithms, dynamic programming):

```python
def fibonacci(limit):
    \"\"\"Yield Fibonacci numbers less than limit.\"\"\"
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(list(fibonacci(50)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Infinite Generators

Generators can produce values forever -- just use an infinite loop with `yield`:

```python
def id_generator(prefix="ID"):
    \"\"\"Generate unique IDs forever.\"\"\"
    counter = 1
    while True:
        yield f"{prefix}-{counter:04d}"
        counter += 1

gen = id_generator("ORD")
print(next(gen))  # ORD-0001
print(next(gen))  # ORD-0002
print(next(gen))  # ORD-0003
```

This is perfect for generating unique order IDs, user IDs, or ticket numbers in production systems.""",
                'exercise': {
                    'instructions': 'Create a generator called `fibonacci` that yields Fibonacci numbers less than a given limit (starting with 0, 1, 1, 2, ...). Then create a generator called `id_maker` that takes a prefix string and yields IDs in the format "PREFIX-0001", "PREFIX-0002", etc. Test both as shown.',
                    'starter_code': 'def fibonacci(limit):\n    """Yield Fibonacci numbers less than limit."""\n    a, b = 0, 1\n    while a < limit:\n        yield a\n        a, b = b, a + b\n\n\ndef id_maker(prefix):\n    """Yield sequential IDs like PREFIX-0001, PREFIX-0002, etc."""\n    counter = 1\n    while True:\n        yield f"{prefix}-{counter:04d}"\n        counter += 1\n\n\n# Test fibonacci\nprint(list(fibonacci(30)))\n\n# Test id_maker\ngen = id_maker("TKT")\nprint(next(gen))\nprint(next(gen))\nprint(next(gen))\n',
                    'expected_output': '[0, 1, 1, 2, 3, 5, 8, 13, 21]\nTKT-0001\nTKT-0002\nTKT-0003',
                    'hint': 'For fibonacci, use two variables a and b. Start with a=0, b=1. In each iteration, yield a, then update: a, b = b, a + b. For id_maker, use an infinite while True loop with a counter, formatting with :04d for zero-padded numbers.',
                },
            },
            {
                'id': 'summary-best-practices',
                'title': 'Summary and Best Practices',
                'content': """## Summary and Best Practices

### Decorators -- Key Takeaways

1. **A decorator is a function that wraps another function** to add behaviour before, after, or around the original call.
2. **Use `@decorator` syntax** for clean, readable code.
3. **Always use `functools.wraps`** to preserve the wrapped function's `__name__` and `__doc__`.
4. **Decorator factories** (decorators that accept arguments) require an extra level of nesting.

### Common Decorator Use Cases in Industry

| Use Case | Example |
|---|---|
| Performance monitoring | `@timer` to measure function speed |
| Logging and auditing | `@logger` to record function calls |
| Access control | `@login_required` in web frameworks |
| Caching | `@lru_cache` to cache function results |
| Input validation | `@validate` to check function arguments |
| Retry logic | `@retry(max_attempts=3)` for API calls |

### Generators -- Key Takeaways

1. **Use `yield` instead of `return`** to create a generator function.
2. **Generators are lazy** -- they produce values one at a time, saving memory.
3. **Use generators for large datasets** -- files, database results, API responses.
4. **Generator expressions** `(x for x in iterable)` are compact alternatives.
5. **Chain generators** to build efficient data pipelines.

### When to Use Each

- **Decorators:** When you want to add the same behaviour to multiple functions without modifying them (cross-cutting concerns).
- **Generators:** When you are working with sequences that are large, expensive to compute, or potentially infinite.

### Built-in Decorators You Should Know

```python
# @property -- makes a method act like an attribute
# @staticmethod -- method that does not need self
# @classmethod -- method that receives the class, not the instance
# @functools.lru_cache -- automatic memoization
# @functools.wraps -- preserve wrapped function metadata
```""",
                'exercise': None,
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # Lesson 2 -- Lambda Functions, Map, and Filter
    # ------------------------------------------------------------------ #
    {
        'title': 'Lambda Functions, Map, and Filter',
        'description': 'Master anonymous lambda functions and functional programming tools like map(), filter(), and sorted() with key functions for concise data transformation.',
        'order': 2,
        'item_order': 3,
        'estimated_time_minutes': 18,
        'sections': [
            {
                'id': 'lambda-functions',
                'title': 'Lambda Functions',
                'content': """## Lambda Functions

A **lambda function** is a small, anonymous (unnamed) function defined in a single line using the `lambda` keyword. Lambda functions are perfect for short, throwaway operations where defining a full function with `def` would be overkill.

### Real-Life Analogy

Think of a lambda function like a sticky note with a quick instruction: "add 10% tip" or "convert to uppercase." You do not need a whole instruction manual for such a simple task -- a sticky note is enough.

### Syntax

```python
lambda parameters: expression
```

The lambda takes parameters and returns the result of the expression. There is no `return` keyword -- the expression is automatically returned.

### Examples

```python
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

print(square(5))  # 25
```

### Multiple Parameters

```python
# Calculate tip for a restaurant bill
calculate_tip = lambda bill, tip_rate: round(bill * tip_rate, 2)
print(calculate_tip(85.50, 0.18))  # 15.39

# Full name formatter
full_name = lambda first, last: f"{first} {last}"
print(full_name("Jane", "Doe"))  # Jane Doe
```

### When to Use Lambda

Lambda functions shine when used **inline** as arguments to other functions:

```python
# Sorting a list of tuples by the second element
students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
sorted_students = sorted(students, key=lambda s: s[1])
print(sorted_students)
# [('Carol', 78), ('Alice', 85), ('Bob', 92)]
```

### When NOT to Use Lambda

- If the logic is complex, use a regular `def` function for readability.
- If you need to reuse the function in multiple places, give it a proper name.
- Lambda functions cannot contain statements (no `if/else` blocks, `for` loops, or assignments as statements). However, they can use conditional expressions: `lambda x: "even" if x % 2 == 0 else "odd"`.""",
                'exercise': None,
            },
            {
                'id': 'map-function',
                'title': 'The map() Function',
                'content': """## The `map()` Function

The `map()` function applies a function to **every item** in an iterable (like a list) and returns a map object (which you can convert to a list).

### Real-Life Analogy

Imagine a factory assembly line where every product goes through the same station. A raw material goes in, and a finished product comes out. `map()` is that assembly line -- it transforms every input item using the same function.

### Syntax

```python
map(function, iterable)
```

### Basic Examples

```python
# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0]

# Calculate prices after 10% tax
prices = [10.00, 25.50, 8.99, 42.00]
with_tax = list(map(lambda p: round(p * 1.10, 2), prices))
print(with_tax)  # [11.0, 28.05, 9.89, 46.2]
```

### Using map() with Built-in Functions

You do not always need a lambda -- built-in functions and methods work too:

```python
# Convert list of strings to integers
str_numbers = ["1", "2", "3", "4", "5"]
numbers = list(map(int, str_numbers))
print(numbers)  # [1, 2, 3, 4, 5]

# Convert all names to uppercase
names = ["alice", "bob", "carol"]
upper_names = list(map(str.upper, names))
print(upper_names)  # ['ALICE', 'BOB', 'CAROL']
```

### map() with Multiple Iterables

```python
# Calculate total cost: price * quantity for each item
prices = [10.00, 25.00, 5.00]
quantities = [2, 1, 4]
totals = list(map(lambda p, q: p * q, prices, quantities))
print(totals)  # [20.0, 25.0, 20.0]
```

### map() vs List Comprehension

Both achieve the same result. Choose whichever is more readable:

```python
# map approach
result = list(map(lambda x: x ** 2, range(5)))

# List comprehension approach (often preferred in Python)
result = [x ** 2 for x in range(5)]
```""",
                'exercise': {
                    'instructions': 'Use map() to convert a list of product prices from USD to EUR using an exchange rate of 0.85. Then use map() with a built-in function to convert a list of string numbers to integers. Print both results.',
                    'starter_code': '# Product prices in USD\nusd_prices = [29.99, 49.99, 9.99, 99.99]\n\n# Convert to EUR (rate: 1 USD = 0.85 EUR), rounded to 2 decimals\neur_prices = list(map(lambda p: round(p * 0.85, 2), usd_prices))\nprint(eur_prices)\n\n# String numbers to convert\nstr_nums = ["10", "20", "30", "40", "50"]\n\n# Convert to integers using map with int\nnumbers = list(map(int, str_nums))\nprint(numbers)\n\n# Bonus: calculate squares of the numbers\nsquares = list(map(lambda x: x ** 2, numbers))\nprint(squares)\n',
                    'expected_output': '[25.49, 42.49, 8.49, 84.99]\n[10, 20, 30, 40, 50]\n[100, 400, 900, 1600, 2500]',
                    'hint': 'Use lambda p: round(p * 0.85, 2) inside map() for the currency conversion. Use map(int, str_nums) to convert strings to integers.',
                },
            },
            {
                'id': 'filter-function',
                'title': 'The filter() Function',
                'content': """## The `filter()` Function

The `filter()` function selects items from an iterable that satisfy a condition. It returns only the items for which the provided function returns `True`.

### Real-Life Analogy

Think of `filter()` like a security checkpoint at an airport. Every passenger (item) is checked against a condition (valid ticket, proper ID). Only those who pass the check get through; the rest are turned away.

### Syntax

```python
filter(function, iterable)
```

The function must return `True` or `False` for each item.

### Basic Examples

```python
# Filter products that are in stock
products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Phone", "stock": 0},
    {"name": "Tablet", "stock": 12},
    {"name": "Watch", "stock": 0},
]

in_stock = list(filter(lambda p: p["stock"] > 0, products))
print([p["name"] for p in in_stock])  # ['Laptop', 'Tablet']
```

### Filtering Numbers

```python
# Find all even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Find numbers greater than the average
scores = [72, 85, 91, 68, 88, 95, 76]
avg = sum(scores) / len(scores)
above_avg = list(filter(lambda s: s > avg, scores))
print(above_avg)  # [85, 91, 88, 95]
```

### Filtering Strings

```python
# Filter valid email addresses (simple check)
emails = ["alice@mail.com", "invalid", "bob@work.org", "@broken", "carol@site.net"]
valid = list(filter(lambda e: "@" in e and "." in e.split("@")[-1], emails))
print(valid)  # ['alice@mail.com', 'bob@work.org', 'carol@site.net']
```

### Combining filter() and map()

A common pattern is to filter data first, then transform it:

```python
# Get discounted prices for expensive items only
prices = [5.99, 29.99, 12.50, 89.99, 3.49, 45.00]

# Step 1: Filter items over $20
# Step 2: Apply 15% discount
result = list(map(
    lambda p: round(p * 0.85, 2),
    filter(lambda p: p > 20, prices)
))
print(result)  # [25.49, 76.49, 38.25]
```""",
                'exercise': {
                    'instructions': 'Use filter() to find all employees whose salary is above 50000 from the given list. Then use filter() to find all words longer than 4 characters from a sentence. Print both results.',
                    'starter_code': '# Employee salaries\nemployees = [\n    {"name": "Alice", "salary": 72000},\n    {"name": "Bob", "salary": 45000},\n    {"name": "Carol", "salary": 88000},\n    {"name": "Dave", "salary": 51000},\n    {"name": "Eve", "salary": 39000},\n]\n\n# Filter employees with salary > 50000\nhigh_earners = list(filter(lambda e: e["salary"] > 50000, employees))\nprint([e["name"] for e in high_earners])\n\n# Filter long words from a sentence\nsentence = "The quick brown fox jumps over the lazy dog"\nwords = sentence.split()\nlong_words = list(filter(lambda w: len(w) > 4, words))\nprint(long_words)\n',
                    'expected_output': "['Alice', 'Carol', 'Dave']\n['quick', 'brown', 'jumps']",
                    'hint': 'Use lambda e: e["salary"] > 50000 to filter employees. Use lambda w: len(w) > 4 to filter words. Remember filter() returns a filter object, so wrap it in list().',
                },
            },
            {
                'id': 'sorted-with-key',
                'title': 'Sorting with sorted() and Key Functions',
                'content': """## Sorting with `sorted()` and Key Functions

The `sorted()` function returns a new sorted list from any iterable. The `key` parameter lets you specify a function that extracts a comparison value from each element -- this is where lambda functions truly shine.

### Real-Life Analogy

Imagine sorting a stack of employee files. You could sort them by name, by hire date, by salary, or by department. The `key` function tells Python which "field" to sort by.

### Basic Sorting

```python
# Sort numbers (default: ascending)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))          # [1, 1, 2, 3, 4, 5, 6, 9]
print(sorted(numbers, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]
```

### Sorting with a Key Function

```python
# Sort employees by salary
employees = [
    {"name": "Alice", "salary": 72000},
    {"name": "Bob", "salary": 45000},
    {"name": "Carol", "salary": 88000},
]

by_salary = sorted(employees, key=lambda e: e["salary"])
print([f"{e['name']}: ${e['salary']}" for e in by_salary])
# ['Bob: $45000', 'Alice: $72000', 'Carol: $88000']

# Sort by name (alphabetically)
by_name = sorted(employees, key=lambda e: e["name"])
print([e["name"] for e in by_name])
# ['Alice', 'Bob', 'Carol']
```

### Sorting Strings Case-Insensitively

```python
fruits = ["banana", "Apple", "cherry", "Date"]
# Default sort (uppercase letters come first in ASCII)
print(sorted(fruits))
# ['Apple', 'Date', 'banana', 'cherry']

# Case-insensitive sort
print(sorted(fruits, key=str.lower))
# ['Apple', 'banana', 'cherry', 'Date']
```

### Sorting by Multiple Criteria

```python
students = [
    ("Alice", "A", 90),
    ("Bob", "B", 90),
    ("Carol", "A", 95),
    ("Dave", "B", 85),
]

# Sort by grade first, then by score (descending)
result = sorted(students, key=lambda s: (s[1], -s[2]))
for name, grade, score in result:
    print(f"{name}: Grade {grade}, Score {score}")
# Carol: Grade A, Score 95
# Alice: Grade A, Score 90
# Bob: Grade B, Score 90
# Dave: Grade B, Score 85
```""",
                'exercise': {
                    'instructions': 'Sort the list of products by price (ascending) using sorted() with a lambda key. Then sort them by name length (shortest first). Print both results showing the product names.',
                    'starter_code': '# Product catalog\nproducts = [\n    {"name": "Wireless Mouse", "price": 29.99},\n    {"name": "USB Cable", "price": 8.99},\n    {"name": "Mechanical Keyboard", "price": 79.99},\n    {"name": "Monitor Stand", "price": 45.00},\n    {"name": "Webcam", "price": 59.99},\n]\n\n# Sort by price (ascending)\nby_price = sorted(products, key=lambda p: p["price"])\nprint([p["name"] for p in by_price])\n\n# Sort by name length (shortest first)\nby_name_len = sorted(products, key=lambda p: len(p["name"]))\nprint([p["name"] for p in by_name_len])\n',
                    'expected_output': "['USB Cable', 'Wireless Mouse', 'Monitor Stand', 'Webcam', 'Mechanical Keyboard']\n['Webcam', 'USB Cable', 'Monitor Stand', 'Wireless Mouse', 'Mechanical Keyboard']",
                    'hint': 'Use key=lambda p: p["price"] to sort by price. Use key=lambda p: len(p["name"]) to sort by name length. The sorted() function returns a new list without modifying the original.',
                },
            },
            {
                'id': 'functional-programming-summary',
                'title': 'Putting It All Together',
                'content': """## Putting It All Together

### Real-World Data Pipeline

Here is how `lambda`, `map()`, `filter()`, and `sorted()` work together in a realistic scenario -- processing product data for an e-commerce dashboard:

```python
products = [
    {"name": "Laptop", "price": 999.99, "rating": 4.5, "in_stock": True},
    {"name": "Phone", "price": 699.99, "rating": 4.8, "in_stock": True},
    {"name": "Tablet", "price": 449.99, "rating": 3.9, "in_stock": False},
    {"name": "Watch", "price": 299.99, "rating": 4.2, "in_stock": True},
    {"name": "Earbuds", "price": 149.99, "rating": 4.6, "in_stock": True},
]

# Pipeline: in-stock -> well-rated -> sorted by price -> formatted
result = list(map(
    lambda p: f"{p['name']}: ${p['price']:.2f}",
    sorted(
        filter(lambda p: p["in_stock"] and p["rating"] >= 4.0, products),
        key=lambda p: p["price"]
    )
))

for item in result:
    print(item)
# Watch: $299.99
# Earbuds: $149.99  -- wait, sorted by price!
# Actually: Earbuds: $149.99, Watch: $299.99, Phone: $699.99, Laptop: $999.99
```

### Quick Reference

| Tool | Purpose | Returns |
|------|---------|---------|
| `lambda` | Create small anonymous functions | Function object |
| `map(func, iterable)` | Transform every item | Map object (lazy) |
| `filter(func, iterable)` | Keep items where func is True | Filter object (lazy) |
| `sorted(iterable, key=func)` | Sort by a computed key | New list |

### Best Practices

1. **Use lambda for simple, one-line operations.** If it is complex, use `def`.
2. **Use list comprehensions** when the equivalent `map()`/`filter()` is harder to read.
3. **Chain operations** for clean data pipelines: `filter -> map -> sorted`.
4. **Remember that map() and filter() are lazy** -- convert to `list()` when you need all results at once.""",
                'exercise': None,
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # Lesson 3 -- Error Handling and Exceptions
    # ------------------------------------------------------------------ #
    {
        'title': 'Error Handling and Exceptions',
        'description': 'Learn to handle errors gracefully with try/except/else/finally, raise custom exceptions, and build robust programs that do not crash unexpectedly.',
        'order': 3,
        'item_order': 6,
        'estimated_time_minutes': 18,
        'sections': [
            {
                'id': 'why-error-handling',
                'title': 'Why Error Handling Matters',
                'content': """## Why Error Handling Matters

Every real-world program encounters errors. Users enter invalid data, files go missing, network connections drop, and databases time out. Without proper error handling, your program crashes and your users lose their work.

### Real-Life Analogy

Think of error handling like the safety systems in a car. The car does not just stop working if something goes wrong. The ABS prevents skidding, airbags deploy on impact, and warning lights alert the driver. Error handling is your program's safety system.

### Common Python Exceptions

Python has many built-in exception types:

| Exception | When It Happens |
|-----------|----------------|
| `ValueError` | Wrong value type (e.g., `int("hello")`) |
| `TypeError` | Wrong data type in operation (e.g., `"3" + 5`) |
| `KeyError` | Dictionary key does not exist |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File does not exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Object does not have the attribute |
| `ImportError` | Module not found |

### What Happens Without Error Handling

```python
# This crashes the entire program!
numbers = [1, 2, 3]
print(numbers[10])  # IndexError: list index out of range
print("This line never runs")
```

### The try/except Block

The `try/except` block lets you catch errors and handle them gracefully:

```python
numbers = [1, 2, 3]

try:
    print(numbers[10])
except IndexError:
    print("That index does not exist!")

print("Program continues normally")
```

Output:
```
That index does not exist!
Program continues normally
```

The program does not crash. It catches the error, handles it, and keeps running.""",
                'exercise': None,
            },
            {
                'id': 'try-except-patterns',
                'title': 'try/except/else/finally Patterns',
                'content': """## try/except/else/finally Patterns

Python provides four blocks for comprehensive error handling:

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except SomeError as e:
    # Code that runs if that specific error occurs
    print(f"Error: {e}")
else:
    # Code that runs ONLY if no exception occurred
    print(f"Success: {result}")
finally:
    # Code that ALWAYS runs, error or not
    print("Cleanup complete")
```

### Catching Specific Exceptions

Always catch specific exceptions rather than using a bare `except`:

```python
# Real-life example: Processing a user registration form
def validate_age(age_str):
    try:
        age = int(age_str)
    except ValueError:
        return "Please enter a valid number for age."

    if age < 0 or age > 150:
        return "Age must be between 0 and 150."

    return f"Age accepted: {age}"

print(validate_age("25"))       # Age accepted: 25
print(validate_age("abc"))      # Please enter a valid number for age.
print(validate_age("-5"))       # Age must be between 0 and 150.
```

### Catching Multiple Exception Types

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Both arguments must be numbers!"
    else:
        return f"Result: {result}"
    finally:
        print("Division operation attempted.")

print(safe_divide(10, 3))
# Division operation attempted.
# Result: 3.3333333333333335

print(safe_divide(10, 0))
# Division operation attempted.
# Cannot divide by zero!

print(safe_divide("10", 3))
# Division operation attempted.
# Both arguments must be numbers!
```

### The else Block

The `else` block runs only when no exception was raised. It is useful for code that should only execute on success:

```python
# API error handling pattern
def fetch_user_data(user_id):
    users = {1: "Alice", 2: "Bob", 3: "Carol"}

    try:
        name = users[user_id]
    except KeyError:
        print(f"User {user_id} not found.")
        name = "Unknown"
    else:
        print(f"Successfully retrieved user: {name}")
    finally:
        print("Database connection closed.")

    return name
```

### The finally Block

The `finally` block ALWAYS runs, whether an exception occurred or not. It is perfect for cleanup operations like closing files or database connections:

```python
# File handling with finally
def read_config(filename):
    f = None
    try:
        f = open(filename, 'r')
        data = f.read()
        return data
    except FileNotFoundError:
        print(f"Config file '{filename}' not found. Using defaults.")
        return "{}"
    finally:
        if f is not None:
            f.close()
            print("File handle closed.")
```""",
                'exercise': {
                    'instructions': 'Write a function called `safe_calculator` that takes two numbers and an operator string (+, -, *, /). Use try/except to handle ZeroDivisionError and return "Error: Division by zero". For invalid operators, return "Error: Invalid operator". For valid operations, return the result. Test it with the provided calls.',
                    'starter_code': 'def safe_calculator(a, b, operator):\n    """Perform a calculation with error handling."""\n    try:\n        if operator == "+":\n            result = a + b\n        elif operator == "-":\n            result = a - b\n        elif operator == "*":\n            result = a * b\n        elif operator == "/":\n            result = a / b\n        else:\n            return "Error: Invalid operator"\n    except ZeroDivisionError:\n        return "Error: Division by zero"\n    else:\n        return result\n\n\n# Test the calculator\nprint(safe_calculator(10, 3, "+"))\nprint(safe_calculator(10, 3, "-"))\nprint(safe_calculator(10, 3, "*"))\nprint(safe_calculator(10, 3, "/"))\nprint(safe_calculator(10, 0, "/"))\nprint(safe_calculator(10, 3, "%"))\n',
                    'expected_output': '13\n7\n30\n3.3333333333333335\nError: Division by zero\nError: Invalid operator',
                    'hint': 'Use if/elif/else inside the try block to check the operator. The ZeroDivisionError will be raised automatically when dividing by zero. Return the error message string for each error case.',
                },
            },
            {
                'id': 'raising-exceptions',
                'title': 'Raising Exceptions',
                'content': """## Raising Exceptions

Sometimes your code needs to signal that something has gone wrong. The `raise` statement lets you create and throw exceptions intentionally.

### Real-Life Analogy

Raising an exception is like a quality control inspector rejecting a product. The inspector (your code) checks if something is wrong and actively flags the problem rather than letting a defective product through.

### The raise Statement

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot exceed 150")
    return age

# Valid
print(set_age(25))  # 25

# Invalid -- these raise exceptions
try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")
# Caught: Age cannot be negative
```

### Validating Function Input

```python
def create_user(username, email):
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    if "@" not in email:
        raise ValueError(f"Invalid email address: {email}")
    return {"username": username, "email": email}

try:
    user = create_user("ab", "not-an-email")
except ValueError as e:
    print(f"Validation Error: {e}")
# Validation Error: Username must be at least 3 characters
```

### Re-raising Exceptions

Sometimes you want to catch an exception, log it, and then re-raise it:

```python
def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        # Process the payment ...
        return True
    except ValueError:
        print("LOG: Invalid payment amount attempted")
        raise  # Re-raise the same exception
```

### Exception Chaining

Use `raise ... from ...` to chain exceptions, showing the original cause:

```python
def parse_config(text):
    try:
        value = int(text)
    except ValueError as original:
        raise RuntimeError("Failed to parse config") from original
```""",
                'exercise': {
                    'instructions': 'Write a function `validate_password` that takes a password string and raises a ValueError with a descriptive message if the password does not meet the requirements: at least 8 characters and must contain at least one digit. If valid, return "Password accepted". Test it with the provided calls.',
                    'starter_code': 'def validate_password(password):\n    """Validate password strength. Raise ValueError if invalid."""\n    if len(password) < 8:\n        raise ValueError("Password must be at least 8 characters")\n    if not any(c.isdigit() for c in password):\n        raise ValueError("Password must contain at least one digit")\n    return "Password accepted"\n\n\n# Test with valid password\ntry:\n    print(validate_password("secure123"))\nexcept ValueError as e:\n    print(f"Error: {e}")\n\n# Test with short password\ntry:\n    print(validate_password("short"))\nexcept ValueError as e:\n    print(f"Error: {e}")\n\n# Test with no digits\ntry:\n    print(validate_password("nodigitshere"))\nexcept ValueError as e:\n    print(f"Error: {e}")\n',
                    'expected_output': 'Password accepted\nError: Password must be at least 8 characters\nError: Password must contain at least one digit',
                    'hint': 'Check len(password) < 8 first. Then check if any character is a digit using any(c.isdigit() for c in password). If either check fails, raise ValueError with a descriptive message.',
                },
            },
            {
                'id': 'custom-exceptions',
                'title': 'Custom Exceptions',
                'content': """## Custom Exceptions

Python lets you define your own exception classes by inheriting from the built-in `Exception` class (or its subclasses). Custom exceptions make your code more readable and your error handling more precise.

### Real-Life Analogy

Think of custom exceptions like specific warning labels. A generic "Warning" sticker is not very helpful. But "Warning: High Voltage" or "Warning: Fragile" immediately tells you what the problem is and how to handle it.

### Creating Custom Exceptions

```python
class InsufficientFundsError(Exception):
    \"\"\"Raised when a bank account has insufficient funds.\"\"\"
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. "
            f"Available balance: ${balance:.2f}"
        )


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


# Using the custom exception
account = BankAccount("Alice", 100.00)

try:
    account.withdraw(150.00)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
# Transaction failed: Cannot withdraw $150.00. Available balance: $100.00
```

### Exception Hierarchy for an Application

Well-designed applications create a hierarchy of exceptions:

```python
class AppError(Exception):
    \"\"\"Base exception for our application.\"\"\"
    pass

class ValidationError(AppError):
    \"\"\"Raised when input validation fails.\"\"\"
    pass

class AuthenticationError(AppError):
    \"\"\"Raised when authentication fails.\"\"\"
    pass

class NotFoundError(AppError):
    \"\"\"Raised when a resource is not found.\"\"\"
    pass
```

This lets you catch all application errors with `except AppError` or handle specific ones individually.

### API Error Handling Pattern

A common real-world pattern for handling API responses:

```python
class APIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")

def handle_response(status_code, data):
    if status_code == 404:
        raise APIError(404, "Resource not found")
    elif status_code == 401:
        raise APIError(401, "Unauthorized access")
    elif status_code >= 500:
        raise APIError(status_code, "Server error")
    return data
```""",
                'exercise': {
                    'instructions': 'Create a custom exception called `InvalidAgeError` that stores the invalid age value. Then write a function `register_user` that takes a name and age, and raises InvalidAgeError if the age is not between 0 and 120. Test it with the calls provided.',
                    'starter_code': 'class InvalidAgeError(Exception):\n    """Raised when an invalid age is provided."""\n    def __init__(self, age):\n        self.age = age\n        super().__init__(f"Invalid age: {age}. Must be between 0 and 120.")\n\n\ndef register_user(name, age):\n    """Register a user after validating their age."""\n    if not isinstance(age, int) or age < 0 or age > 120:\n        raise InvalidAgeError(age)\n    return f"User {name} (age {age}) registered successfully"\n\n\n# Test with valid age\ntry:\n    print(register_user("Alice", 30))\nexcept InvalidAgeError as e:\n    print(f"Error: {e}")\n\n# Test with negative age\ntry:\n    print(register_user("Bob", -5))\nexcept InvalidAgeError as e:\n    print(f"Error: {e}")\n\n# Test with age too high\ntry:\n    print(register_user("Carol", 200))\nexcept InvalidAgeError as e:\n    print(f"Error: {e}")\n',
                    'expected_output': 'User Alice (age 30) registered successfully\nError: Invalid age: -5. Must be between 0 and 120.\nError: Invalid age: 200. Must be between 0 and 120.',
                    'hint': 'Create InvalidAgeError by inheriting from Exception. Store the age in self.age and call super().__init__() with a descriptive message. In register_user, check if age is outside 0-120 range and raise the custom exception.',
                },
            },
            {
                'id': 'error-handling-best-practices',
                'title': 'Best Practices and Summary',
                'content': """## Best Practices and Summary

### The Golden Rules of Error Handling

1. **Catch specific exceptions** -- never use bare `except:` without a type.
2. **Handle errors at the right level** -- catch errors where you can do something useful about them.
3. **Use else for success logic** -- code in the `else` block only runs when no exception occurred.
4. **Use finally for cleanup** -- close files, database connections, and release resources.
5. **Raise exceptions for invalid input** -- do not return error codes; raise descriptive exceptions.
6. **Create custom exceptions** for your application's specific error conditions.

### Anti-Patterns to Avoid

```python
# BAD: Catching everything silently
try:
    do_something()
except:
    pass  # This hides ALL errors, including bugs!

# BAD: Catching too broadly
try:
    result = complex_operation()
except Exception:
    print("Something went wrong")  # Not helpful!

# GOOD: Specific exceptions with useful messages
try:
    result = complex_operation()
except ValueError as e:
    print(f"Invalid value: {e}")
except ConnectionError as e:
    print(f"Network issue: {e}. Retrying...")
```

### Common Patterns in Professional Code

```python
# Pattern 1: Try/except with default value
def get_setting(config, key, default=None):
    try:
        return config[key]
    except KeyError:
        return default

# Pattern 2: EAFP (Easier to Ask Forgiveness than Permission)
# Pythonic way -- try first, handle error if it happens
try:
    value = my_dict[key]
except KeyError:
    value = compute_default()

# vs LBYL (Look Before You Leap) -- less Pythonic
if key in my_dict:
    value = my_dict[key]
else:
    value = compute_default()
```

### Summary

| Feature | Purpose |
|---------|---------|
| `try` | Wrap code that might fail |
| `except ErrorType` | Handle a specific error |
| `except ErrorType as e` | Handle and access the error details |
| `else` | Runs only if no error occurred |
| `finally` | Runs always (cleanup) |
| `raise` | Throw an exception intentionally |
| `raise ... from ...` | Chain exceptions |
| Custom exceptions | Domain-specific error types |""",
                'exercise': None,
            },
        ],
    },
]
