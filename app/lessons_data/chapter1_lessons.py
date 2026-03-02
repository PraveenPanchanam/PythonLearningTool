CHAPTER_ORDER = 1

LESSONS = [
    {
        'title': 'Introduction to Variables and Data Types',
        'description': 'Learn about variables, integers, floats, strings, and booleans - the fundamental building blocks of every Python program.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'what-are-variables',
                'title': 'What Are Variables?',
                'content': """## What Are Variables?

A **variable** is a named container that stores a value in your computer's memory. Think of it as a labeled box where you can put data and retrieve it later by referring to its label.

In Python, you create a variable by using the **assignment operator** (`=`):

```python
message = "Hello, World!"
age = 21
temperature = 98.6
is_student = True
```

### Naming Rules

Python variable names must follow these rules:

1. **Must start with a letter or underscore** - not a digit.
2. **Can contain letters, digits, and underscores** - no spaces or special characters.
3. **Case-sensitive** - `Name` and `name` are different variables.
4. **Cannot be a Python keyword** - words like `if`, `for`, `class`, `return` are reserved.

### Naming Conventions

By convention, Python programmers use **snake_case** for variable names:

```python
# Good (snake_case)
first_name = "Alice"
total_score = 95

# Avoid (other styles)
firstName = "Alice"    # camelCase - used in other languages
TotalScore = 95        # PascalCase - reserved for class names
```

### Dynamic Typing

Python is **dynamically typed**, which means you do not need to declare the type of a variable before using it. The interpreter figures out the type automatically based on the value you assign:

```python
x = 10          # x is an integer
x = "hello"     # now x is a string - perfectly valid in Python
```

This is different from statically typed languages like Java or C++, where you must declare the type up front.

### Multiple Assignment

Python lets you assign values to multiple variables in a single line:

```python
# Assign different values
x, y, z = 1, 2, 3

# Assign the same value
a = b = c = 0
```""",
                'exercise': None,
            },
            {
                'id': 'integers-and-floats',
                'title': 'Integers and Floats',
                'content': """## Numeric Data Types

Python has two primary numeric types: **integers** and **floats**.

### Integers (`int`)

Integers are whole numbers - positive, negative, or zero - with no decimal point:

```python
count = 42
negative_number = -7
zero = 0
large_number = 1_000_000  # underscores improve readability
```

Python integers have **unlimited precision** - they can be as large as your memory allows:

```python
huge = 10 ** 100  # a googol - 1 followed by 100 zeros
print(type(huge))  # <class 'int'>
```

### Floats (`float`)

Floats (floating-point numbers) represent decimal values:

```python
price = 19.99
pi = 3.14159
negative_float = -0.5
scientific = 2.5e3   # 2500.0 - scientific notation
```

### Arithmetic Operators

Python supports all standard arithmetic operations:

| Operator | Description         | Example      | Result  |
|----------|---------------------|-------------|---------|
| `+`      | Addition            | `7 + 3`     | `10`    |
| `-`      | Subtraction         | `7 - 3`     | `4`     |
| `*`      | Multiplication      | `7 * 3`     | `21`    |
| `/`      | Division            | `7 / 3`     | `2.333` |
| `//`     | Floor Division      | `7 // 3`    | `2`     |
| `%`      | Modulus (remainder)  | `7 % 3`     | `1`     |
| `**`     | Exponentiation      | `2 ** 3`    | `8`     |

**Important:** The `/` operator always returns a float, even when dividing two integers evenly:

```python
result = 10 / 2
print(result)       # 5.0 - a float, not an integer
print(type(result)) # <class 'float'>
```

Use `//` for integer (floor) division:

```python
result = 10 // 3
print(result)  # 3 - rounds down to nearest integer
```

### Operator Precedence

Python follows standard mathematical order of operations (PEMDAS):

```python
result = 2 + 3 * 4      # 14, not 20 - multiplication first
result = (2 + 3) * 4     # 20 - parentheses override precedence
```""",
                'exercise': {
                    'instructions': 'Create two variables: `length` set to 12 and `width` set to 5. Calculate the area (length times width) and the perimeter (2 times the sum of length and width). Print both results on separate lines.',
                    'starter_code': '# Create the variables\nlength = 12\nwidth = 5\n\n# Calculate area (length * width)\narea = \n\n# Calculate perimeter (2 * (length + width))\nperimeter = \n\n# Print the results\nprint(area)\nprint(perimeter)\n',
                    'expected_output': '60\n34',
                    'hint': 'Multiply length by width for area. For perimeter, add length and width first, then multiply by 2.',
                },
            },
            {
                'id': 'strings-and-booleans',
                'title': 'Strings and Booleans',
                'content': """## Strings (`str`)

A **string** is a sequence of characters enclosed in quotes. You can use single quotes or double quotes:

```python
single = 'Hello'
double = "Hello"
```

### Common String Operations

```python
first = "Hello"
second = "World"

# Concatenation - joining strings with +
greeting = first + " " + second
print(greeting)  # Hello World

# Repetition - repeating strings with *
line = "-" * 20
print(line)  # --------------------

# Length - counting characters
print(len(greeting))  # 11

# Indexing - accessing individual characters (0-based)
print(first[0])   # H
print(first[-1])  # o - negative index counts from the end
```

### Escape Characters

Use backslash for special characters inside strings:

```python
print("She said \\"hello\\"")    # She said "hello"
print("Line 1\\nLine 2")         # prints on two lines
print("Tab\\there")               # Tab    here
```

## Booleans (`bool`)

Booleans represent truth values and can only be `True` or `False` (note the capital letters):

```python
is_active = True
is_deleted = False
```

### Comparison Operators

Comparison operators always produce boolean results:

| Operator | Meaning                  | Example    | Result  |
|----------|--------------------------|-----------|---------|
| `==`     | Equal to                 | `5 == 5`  | `True`  |
| `!=`     | Not equal to             | `5 != 3`  | `True`  |
| `>`      | Greater than             | `5 > 3`   | `True`  |
| `<`      | Less than                | `5 < 3`   | `False` |
| `>=`     | Greater than or equal to | `5 >= 5`  | `True`  |
| `<=`     | Less than or equal to    | `5 <= 3`  | `False` |

```python
x = 10
print(x > 5)      # True
print(x == 10)     # True
print(x != 10)     # False
print(x <= 3)      # False
```

### Truthiness

In Python, many values can be evaluated as booleans:

- **Falsy values:** `0`, `0.0`, `""` (empty string), `None`, `False`
- **Truthy values:** everything else

```python
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("Hi"))   # True
```""",
                'exercise': {
                    'instructions': 'Create a variable `name` with the value "Python" and a variable `version` with the integer value 3. Print the name, its length, and whether the version is greater than 2, each on a separate line.',
                    'starter_code': '# Create the variables\nname = "Python"\nversion = 3\n\n# Print the name\nprint(name)\n\n# Print the length of the name\nprint(len(name))\n\n# Print whether version is greater than 2\nprint(version > 2)\n',
                    'expected_output': 'Python\n6\nTrue',
                    'hint': 'Use len() to get the length of a string. Use the > operator to compare version with 2.',
                },
            },
            {
                'id': 'the-type-function',
                'title': 'Checking Types with type()',
                'content': """## The `type()` Function

Python provides the built-in `type()` function to check the data type of any value or variable:

```python
age = 25
price = 9.99
name = "Alice"
is_valid = True

print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_valid))  # <class 'bool'>
```

### Why Types Matter

Understanding types is essential because:

1. **Operations depend on type** - the `+` operator adds numbers but concatenates strings.
2. **Type mismatches cause errors** - you cannot add a string to an integer directly.
3. **Functions may require specific types** - `len()` works on strings but not integers.

```python
# This causes a TypeError:
# result = "Age: " + 25  # ERROR!

# Fix it with str() conversion:
result = "Age: " + str(25)
print(result)  # Age: 25
```

### `isinstance()` for Type Checking

For more robust type checking, use `isinstance()`:

```python
x = 42
print(isinstance(x, int))     # True
print(isinstance(x, float))   # False
print(isinstance(x, str))     # False
```

You can also check against multiple types using a tuple:

```python
value = 3.14
print(isinstance(value, (int, float)))  # True - it is one of those types
```""",
                'exercise': {
                    'instructions': 'Create four variables with different types: an integer, a float, a string, and a boolean. Print the type of each variable. Then print the result of isinstance() to check if the integer variable is an int.',
                    'starter_code': '# Create four variables of different types\nmy_int = 42\nmy_float = 3.14\nmy_str = "hello"\nmy_bool = False\n\n# Print the type of each variable\nprint(type(my_int))\nprint(type(my_float))\nprint(type(my_str))\nprint(type(my_bool))\n\n# Check if my_int is an instance of int\nprint(isinstance(my_int, int))\n',
                    'expected_output': "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>\nTrue",
                    'hint': 'The starter code is already complete. Run it to see the output and make sure you understand what each line does.',
                },
            },
        ],
    },
    {
        'title': 'Type Conversion and String Operations',
        'description': 'Master type conversion between data types, explore powerful string methods, and learn to format output with f-strings.',
        'order': 2,
        'item_order': 4,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'type-conversion',
                'title': 'Type Conversion (Casting)',
                'content': """## Type Conversion (Casting)

**Type conversion** (also called **casting**) is the process of converting a value from one data type to another. Python provides built-in functions for this purpose.

### Explicit Conversion Functions

| Function  | Converts to | Example                    | Result     |
|-----------|-------------|----------------------------|------------|
| `int()`   | Integer     | `int("42")`                | `42`       |
| `float()` | Float       | `float("3.14")`            | `3.14`     |
| `str()`   | String      | `str(100)`                 | `"100"`    |
| `bool()`  | Boolean     | `bool(1)`                  | `True`     |

### Converting Strings to Numbers

```python
# String to integer
user_input = "25"
age = int(user_input)
print(age + 5)  # 30

# String to float
price_text = "19.99"
price = float(price_text)
print(price * 2)  # 39.98
```

**Warning:** Converting an invalid string raises a `ValueError`:

```python
# int("hello")  # ValueError: invalid literal for int()
# int("3.14")   # ValueError - use float() first, then int()
```

### Converting Numbers to Strings

This is essential when you need to concatenate numbers with text:

```python
score = 95
message = "Your score is " + str(score)
print(message)  # Your score is 95
```

### Converting Between int and float

```python
# Float to int - truncates toward zero, does NOT round
x = int(3.9)
print(x)  # 3

x = int(-3.9)
print(x)  # -3

# Int to float
y = float(7)
print(y)  # 7.0
```

### Implicit (Automatic) Conversion

Python automatically converts types in some situations:

```python
# int + float = float (automatic promotion)
result = 5 + 2.0
print(result)       # 7.0
print(type(result)) # <class 'float'>

# bool in arithmetic (True=1, False=0)
total = 10 + True
print(total)  # 11
```""",
                'exercise': {
                    'instructions': 'Convert the string variables to numbers, perform the calculation, and print the results. Calculate the total price (quantity times price_per_item) and print it. Then print the total as an integer (truncated).',
                    'starter_code': '# String values (simulating user input)\nquantity_str = "4"\nprice_str = "12.50"\n\n# Convert to appropriate numeric types\nquantity = int(quantity_str)\nprice_per_item = float(price_str)\n\n# Calculate total\ntotal = quantity * price_per_item\n\n# Print the float total\nprint(total)\n\n# Print the total truncated to an integer\nprint(int(total))\n',
                    'expected_output': '50.0\n50',
                    'hint': 'Use int() to convert the quantity string and float() to convert the price string. Multiply them for the total. Use int() to truncate the float result.',
                },
            },
            {
                'id': 'string-methods',
                'title': 'String Methods',
                'content': """## String Methods

Strings in Python come with many built-in **methods** - functions that belong to the string object. You call them using dot notation: `string.method()`.

### Case Methods

```python
text = "Hello, World!"

print(text.upper())    # HELLO, WORLD!
print(text.lower())    # hello, world!
print(text.title())    # Hello, World!
print(text.swapcase()) # hELLO, wORLD!
print(text.capitalize())  # Hello, world!
```

**Important:** String methods return a *new* string. The original string is unchanged because strings are **immutable**:

```python
name = "alice"
name.upper()       # returns "ALICE" but doesn't change name
print(name)        # alice - still lowercase!

name = name.upper()  # reassign to keep the change
print(name)          # ALICE
```

### Search and Check Methods

```python
sentence = "Python is fun and Python is powerful"

# find() - returns index of first occurrence (-1 if not found)
print(sentence.find("Python"))      # 0
print(sentence.find("Java"))        # -1

# count() - counts non-overlapping occurrences
print(sentence.count("Python"))     # 2
print(sentence.count("is"))         # 2

# startswith() / endswith()
print(sentence.startswith("Python"))  # True
print(sentence.endswith("powerful"))  # True

# in operator - checks if substring exists
print("fun" in sentence)    # True
print("boring" in sentence) # False
```

### Modification Methods

```python
text = "  Hello, World!  "

# strip() - removes leading/trailing whitespace
print(text.strip())    # "Hello, World!"

# replace() - replaces all occurrences
message = "I like cats and cats like me"
new_message = message.replace("cats", "dogs")
print(new_message)  # I like dogs and dogs like me

# split() - breaks string into a list
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# join() - combines a list into a string
words = ["Python", "is", "great"]
sentence = " ".join(words)
print(sentence)  # Python is great
```

### Checking String Content

```python
print("hello123".isalnum())    # True - letters and digits only
print("hello".isalpha())       # True - letters only
print("12345".isdigit())       # True - digits only
print("hello".islower())       # True - all lowercase
print("HELLO".isupper())       # True - all uppercase
```""",
                'exercise': {
                    'instructions': 'Use string methods to process the given text. Convert it to uppercase, count how many times the letter "o" appears in the original text, and check if it starts with "the". Print each result on a separate line.',
                    'starter_code': '# Given text\ntext = "the quick brown fox jumps over the lazy dog"\n\n# Convert to uppercase and print\nprint(text.upper())\n\n# Count occurrences of the letter "o" and print\nprint(text.count("o"))\n\n# Check if the text starts with "the" and print\nprint(text.startswith("the"))\n',
                    'expected_output': 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG\n4\nTrue',
                    'hint': 'Use .upper() to convert to uppercase, .count("o") to count occurrences, and .startswith("the") to check the beginning.',
                },
            },
            {
                'id': 'f-strings',
                'title': 'String Formatting with f-strings',
                'content': """## String Formatting with f-strings

**f-strings** (formatted string literals) are the modern and preferred way to embed expressions inside strings in Python 3.6+. Prefix the string with `f` and place expressions inside curly braces `{}`:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# My name is Alice and I am 25 years old.
```

### Expressions Inside f-strings

You can put any valid Python expression inside the braces:

```python
x = 10
y = 3
print(f"{x} + {y} = {x + y}")       # 10 + 3 = 13
print(f"{x} * {y} = {x * y}")       # 10 * 3 = 30
```

You can even call functions and methods:

```python
name = "alice"
print(f"Hello, {name.title()}!")  # Hello, Alice!
print(f"Name length: {len(name)}")  # Name length: 5
```

### Format Specifiers

Use `:` after the expression to control formatting:

```python
pi = 3.14159265

# Fixed decimal places
print(f"Pi is approximately {pi:.2f}")    # Pi is approximately 3.14
print(f"Pi is approximately {pi:.4f}")    # Pi is approximately 3.1416

# Thousands separator
big = 1000000
print(f"{big:,}")         # 1,000,000

# Percentage
ratio = 0.856
print(f"{ratio:.1%}")    # 85.6%
```

### Older Formatting Methods (for reference)

You may encounter these in existing code:

```python
# .format() method
print("Hello, {}!".format("World"))

# % operator (oldest style)
print("Hello, %s!" % "World")
```

f-strings are generally preferred for readability and performance.""",
                'exercise': {
                    'instructions': 'Use f-strings to create formatted output. Create variables for a product name, price, and quantity. Then print a formatted receipt line and a total line as shown in the expected output.',
                    'starter_code': '# Product information\nproduct = "Widget"\nprice = 9.99\nquantity = 3\n\n# Calculate total\ntotal = price * quantity\n\n# Print formatted receipt line\nprint(f"Product: {product}")\nprint(f"Price: ${price:.2f} x {quantity}")\nprint(f"Total: ${total:.2f}")\n',
                    'expected_output': 'Product: Widget\nPrice: $9.99 x 3\nTotal: $29.97',
                    'hint': 'Use f-strings with :.2f format specifier to show exactly 2 decimal places for currency values.',
                },
            },
            {
                'id': 'string-slicing',
                'title': 'String Slicing and Indexing',
                'content': """## String Slicing and Indexing

### Indexing Review

Every character in a string has a position number (index), starting from 0:

```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
word = "Python"
print(word[0])    # P
print(word[5])    # n
print(word[-1])   # n - last character
print(word[-2])   # o - second to last
```

### Slicing

**Slicing** extracts a substring using the syntax `string[start:stop:step]`:

- `start` - index where the slice begins (inclusive, default 0)
- `stop` - index where the slice ends (exclusive, default end of string)
- `step` - how many characters to skip (default 1)

```python
text = "Hello, World!"

print(text[0:5])     # Hello
print(text[7:12])    # World
print(text[:5])      # Hello - from beginning
print(text[7:])      # World! - to end
print(text[:])       # Hello, World! - full copy
```

### Step Parameter

The third value controls the step size:

```python
text = "Hello, World!"
print(text[::2])     # Hlo ol!
print(text[::-1])    # !dlroW ,olleH - reversed

numbers = "0123456789"
print(numbers[::3])  # 0369
print(numbers[1::2]) # 13579
```

### Strings Are Immutable

You cannot modify individual characters in a string:

```python
word = "Python"
# word[0] = "J"  # TypeError! Strings are immutable

# Instead, create a new string:
new_word = "J" + word[1:]
print(new_word)  # Jython
```""",
                'exercise': None,
            },
        ],
    },
]
