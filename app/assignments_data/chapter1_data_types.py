"""
Chapter 1: Data Types & Variables
Assignment data for the Python Learning Tool.
"""

CHAPTER_INFO = {
    'title': 'Data Types & Variables',
    'description': (
        'Learn the fundamental building blocks of Python programming. '
        'This chapter covers the core data types — integers, floats, strings, and booleans — '
        'along with variable assignment, type conversion, and basic string operations. '
        'Mastering these concepts is essential before moving on to more advanced topics.'
    ),
    'difficulty_level': 'beginner',
    'order': 1,
    'learning_objectives': [
        'Understand and use integer and float numeric types',
        'Create and manipulate strings',
        'Work with boolean values and truthiness',
        'Assign values to variables using proper naming conventions',
        'Convert between data types using int(), float(), str(), and bool()',
        'Perform basic string operations such as slicing, concatenation, and methods',
    ],
    'estimated_time_minutes': 45,
}

ASSIGNMENTS = [
    # ----------------------------------------------------------------
    # Assignment 1: Variable Assignment & Printing
    # ----------------------------------------------------------------
    {
        'title': 'Variable Assignment & Printing',
        'description': '''## Variable Assignment & Printing

In this assignment you will practice **reading user input**, **storing values in variables**, and **printing formatted output**.

### Requirements

1. Read the user's **name** (a string) from input with the prompt `Enter your name: `.
2. Read the user's **age** (an integer) from input with the prompt `Enter your age: `.
3. Read the user's **height in meters** (a float) from input with the prompt `Enter your height in meters: `.
4. Print the following three lines **exactly** (replace the placeholders with actual values):

```
Name: <name>
Age: <age>
Height: <height> meters
```

### Example

**Input:**
```
Alice
25
1.65
```

**Output:**
```
Name: Alice
Age: 25
Height: 1.65 meters
```

> **Tip:** Remember to convert input strings to the correct type using `int()` and `float()`.
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            '# Assignment 1: Variable Assignment & Printing\n'
            '# Read name, age, and height from the user, then print them.\n\n'
            '# Step 1: Read the name\n'
            'name = input("Enter your name: ")\n\n'
            '# Step 2: Read the age (convert to int)\n'
            '# age = ...\n\n'
            '# Step 3: Read the height (convert to float)\n'
            '# height = ...\n\n'
            '# Step 4: Print the results\n'
            '# print(...)\n'
        ),
        'hints': [
            'Use input() to read from the user and int() or float() to convert the string.',
            'Use f-strings like f"Name: {name}" for clean formatting.',
            'Make sure you print exactly three lines in the required format.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': 'Alice\n25\n1.65',
                'expected_output': 'Name: Alice\nAge: 25\nHeight: 1.65 meters',
            },
            {
                'input': 'Bob\n30\n1.80',
                'expected_output': 'Name: Bob\nAge: 30\nHeight: 1.8 meters',
            },
            {
                'input': 'Charlie\n18\n1.75',
                'expected_output': 'Name: Charlie\nAge: 18\nHeight: 1.75 meters',
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestVariableAssignment(unittest.TestCase):
    """Tests for Assignment 1: Variable Assignment & Printing."""

    def _run_student_code(self, inputs):
        """Run student_code.py with mocked input and captured stdout."""
        input_gen = iter(inputs)
        captured = io.StringIO()
        with patch('builtins.input', side_effect=input_gen):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_basic_output(self):
        output = self._run_student_code(['Alice', '25', '1.65'])
        self.assertIn('Name: Alice', output)
        self.assertIn('Age: 25', output)
        self.assertIn('Height: 1.65 meters', output)

    def test_different_values(self):
        output = self._run_student_code(['Bob', '30', '1.80'])
        self.assertIn('Name: Bob', output)
        self.assertIn('Age: 30', output)
        self.assertIn('1.8 meters', output)

    def test_output_line_count(self):
        output = self._run_student_code(['Charlie', '18', '1.75'])
        lines = output.strip().split('\\n')
        self.assertEqual(len(lines), 3, 'Expected exactly 3 lines of output')

    def test_integer_age(self):
        """Age should be printed as an integer, not a float."""
        output = self._run_student_code(['Dana', '22', '1.60'])
        self.assertIn('Age: 22', output)
        self.assertNotIn('22.0', output)

    def test_float_height(self):
        """Height should be printed as a float."""
        output = self._run_student_code(['Eve', '28', '1.70'])
        self.assertIn('Height: 1.7 meters', output)


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ----------------------------------------------------------------
    # Assignment 2: Type Conversion Calculator
    # ----------------------------------------------------------------
    {
        'title': 'Type Conversion Calculator',
        'description': '''## Type Conversion Calculator

Practice **reading numeric input**, **converting types**, and **performing arithmetic** operations.

### Requirements

1. Read two numbers from the user with the prompts `Enter first number: ` and `Enter second number: `.
   - The numbers may be integers or decimals, so treat them as **floats**.
2. Compute and print the following (each on its own line):

```
Sum: <result>
Difference: <result>
Product: <result>
Quotient: <result>
```

- **Sum** = first + second
- **Difference** = first - second
- **Product** = first * second
- **Quotient** = first / second (if second is 0, print `Quotient: undefined`)

### Example

**Input:**
```
10
3
```

**Output:**
```
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.3333333333333335
```
''',
        'difficulty': 'easy',
        'order': 2,
        'item_order': 3,
        'starter_code': (
            '# Assignment 2: Type Conversion Calculator\n'
            '# Read two numbers and perform arithmetic operations.\n\n'
            '# Step 1: Read the two numbers as floats\n'
            'num1 = float(input("Enter first number: "))\n'
            'num2 = float(input("Enter second number: "))\n\n'
            '# Step 2: Compute sum, difference, product, quotient\n'
            '# ...\n\n'
            '# Step 3: Print the results\n'
            '# print(...)\n'
        ),
        'hints': [
            'Convert both inputs to float using float(input(...)).',
            'Check if the second number is zero before dividing.',
            'Use f-strings or format() for clean output.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '10\n3',
                'expected_output': (
                    'Sum: 13.0\n'
                    'Difference: 7.0\n'
                    'Product: 30.0\n'
                    'Quotient: 3.3333333333333335'
                ),
            },
            {
                'input': '5\n0',
                'expected_output': (
                    'Sum: 5.0\n'
                    'Difference: 5.0\n'
                    'Product: 0.0\n'
                    'Quotient: undefined'
                ),
            },
            {
                'input': '-4\n2',
                'expected_output': (
                    'Sum: -2.0\n'
                    'Difference: -6.0\n'
                    'Product: -8.0\n'
                    'Quotient: -2.0'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestTypeConversionCalculator(unittest.TestCase):
    """Tests for Assignment 2: Type Conversion Calculator."""

    def _run_student_code(self, inputs):
        input_gen = iter(inputs)
        captured = io.StringIO()
        with patch('builtins.input', side_effect=input_gen):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_positive_numbers(self):
        output = self._run_student_code(['10', '3'])
        self.assertIn('Sum: 13.0', output)
        self.assertIn('Difference: 7.0', output)
        self.assertIn('Product: 30.0', output)
        self.assertIn('Quotient: 3.333333333333333', output)

    def test_division_by_zero(self):
        output = self._run_student_code(['5', '0'])
        self.assertIn('Sum: 5.0', output)
        self.assertIn('Product: 0.0', output)
        self.assertIn('Quotient: undefined', output)

    def test_negative_numbers(self):
        output = self._run_student_code(['-4', '2'])
        self.assertIn('Sum: -2.0', output)
        self.assertIn('Difference: -6.0', output)
        self.assertIn('Product: -8.0', output)
        self.assertIn('Quotient: -2.0', output)

    def test_decimal_inputs(self):
        output = self._run_student_code(['2.5', '1.5'])
        self.assertIn('Sum: 4.0', output)
        self.assertIn('Difference: 1.0', output)
        self.assertIn('Product: 3.75', output)

    def test_output_line_count(self):
        output = self._run_student_code(['6', '3'])
        lines = output.strip().split('\\n')
        self.assertEqual(len(lines), 4, 'Expected exactly 4 lines of output')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ----------------------------------------------------------------
    # Assignment 3: String Operations
    # ----------------------------------------------------------------
    {
        'title': 'String Operations',
        'description': '''## String Operations

Explore Python's rich set of **string methods and operations**.

### Requirements

1. Read a string from the user with the prompt `Enter a string: `.
2. Print **each of the following on its own line**, labelled exactly as shown:

```
Uppercase: <string in uppercase>
Lowercase: <string in lowercase>
Length: <length of string>
First 3 chars: <first three characters>
Last 3 chars: <last three characters>
Replaced spaces: <string with all spaces replaced by underscores>
Word count: <number of words>
```

### Example

**Input:**
```
Hello World
```

**Output:**
```
Uppercase: HELLO WORLD
Lowercase: hello world
Length: 11
First 3 chars: Hel
Last 3 chars: rld
Replaced spaces: Hello_World
Word count: 2
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            '# Assignment 3: String Operations\n'
            '# Perform various string manipulations.\n\n'
            'text = input("Enter a string: ")\n\n'
            '# Print uppercase version\n'
            '# print(...)\n\n'
            '# Print lowercase version\n'
            '# print(...)\n\n'
            '# Print string length\n'
            '# print(...)\n\n'
            '# Print first 3 characters\n'
            '# print(...)\n\n'
            '# Print last 3 characters\n'
            '# print(...)\n\n'
            '# Print string with spaces replaced by underscores\n'
            '# print(...)\n\n'
            '# Print word count\n'
            '# print(...)\n'
        ),
        'hints': [
            'Use .upper(), .lower(), len(), slicing ([:3] and [-3:]), and .replace().',
            'To count words, use .split() which splits on whitespace by default, then use len().',
            'Slicing with [-3:] gives the last three characters of a string.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': 'Hello World',
                'expected_output': (
                    'Uppercase: HELLO WORLD\n'
                    'Lowercase: hello world\n'
                    'Length: 11\n'
                    'First 3 chars: Hel\n'
                    'Last 3 chars: rld\n'
                    'Replaced spaces: Hello_World\n'
                    'Word count: 2'
                ),
            },
            {
                'input': 'Python is Fun',
                'expected_output': (
                    'Uppercase: PYTHON IS FUN\n'
                    'Lowercase: python is fun\n'
                    'Length: 13\n'
                    'First 3 chars: Pyt\n'
                    'Last 3 chars: Fun\n'
                    'Replaced spaces: Python_is_Fun\n'
                    'Word count: 3'
                ),
            },
            {
                'input': 'abc',
                'expected_output': (
                    'Uppercase: ABC\n'
                    'Lowercase: abc\n'
                    'Length: 3\n'
                    'First 3 chars: abc\n'
                    'Last 3 chars: abc\n'
                    'Replaced spaces: abc\n'
                    'Word count: 1'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestStringOperations(unittest.TestCase):
    """Tests for Assignment 3: String Operations."""

    def _run_student_code(self, inputs):
        input_gen = iter(inputs)
        captured = io.StringIO()
        with patch('builtins.input', side_effect=input_gen):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_hello_world(self):
        output = self._run_student_code(['Hello World'])
        self.assertIn('Uppercase: HELLO WORLD', output)
        self.assertIn('Lowercase: hello world', output)
        self.assertIn('Length: 11', output)
        self.assertIn('First 3 chars: Hel', output)
        self.assertIn('Last 3 chars: rld', output)
        self.assertIn('Replaced spaces: Hello_World', output)
        self.assertIn('Word count: 2', output)

    def test_multiple_words(self):
        output = self._run_student_code(['Python is Fun'])
        self.assertIn('Word count: 3', output)
        self.assertIn('Length: 13', output)
        self.assertIn('Replaced spaces: Python_is_Fun', output)

    def test_short_string(self):
        output = self._run_student_code(['abc'])
        self.assertIn('First 3 chars: abc', output)
        self.assertIn('Last 3 chars: abc', output)
        self.assertIn('Word count: 1', output)

    def test_single_character(self):
        output = self._run_student_code(['X'])
        self.assertIn('Uppercase: X', output)
        self.assertIn('Lowercase: x', output)
        self.assertIn('Length: 1', output)

    def test_output_line_count(self):
        output = self._run_student_code(['test string'])
        lines = output.strip().split('\\n')
        self.assertEqual(len(lines), 7, 'Expected exactly 7 lines of output')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ----------------------------------------------------------------
    # Assignment 4: Boolean Logic & Type Checking
    # ----------------------------------------------------------------
    {
        'title': 'Boolean Logic & Type Checking',
        'description': '''## Boolean Logic & Type Checking

Dive deeper into **boolean values**, **type checking**, and **comparison operators**.

### Requirements

1. Read a value from the user with the prompt `Enter a value: `.
2. Try to interpret the value in this order:
   - If it can be converted to an **int**, treat it as an integer.
   - Otherwise, if it can be converted to a **float**, treat it as a float.
   - Otherwise, keep it as a **string**.
3. Print the following lines:

```
Value: <value>
Type: <type name>  (one of: int, float, str)
Is integer: <True/False>
Is numeric: <True/False>
Is positive: <True/False or N/A>
Boolean value: <bool(value)>
```

- **Is integer**: True if the final type is `int`.
- **Is numeric**: True if the final type is `int` or `float`.
- **Is positive**: True if numeric and > 0, False if numeric and <= 0, `N/A` if it is a string.
- **Boolean value**: The result of `bool()` on the converted value. (Note: `bool(0)` is `False`, `bool("")` is `False`, etc.)

### Example

**Input:**
```
42
```

**Output:**
```
Value: 42
Type: int
Is integer: True
Is numeric: True
Is positive: True
Boolean value: True
```
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 6,
        'starter_code': (
            '# Assignment 4: Boolean Logic & Type Checking\n'
            '# Determine the type of a user-provided value and print boolean properties.\n\n'
            'raw = input("Enter a value: ")\n\n'
            '# Step 1: Try to convert to int, then float, else keep as str\n'
            '# value = ...\n\n'
            '# Step 2: Determine the type name\n'
            '# type_name = ...\n\n'
            '# Step 3: Compute boolean properties\n'
            '# is_integer = ...\n'
            '# is_numeric = ...\n'
            '# is_positive = ...\n\n'
            '# Step 4: Print all results\n'
            '# print(...)\n'
        ),
        'hints': [
            'Use try/except to attempt int() conversion first, then float().',
            'isinstance(value, int) checks if value is an integer.',
            'bool(0) is False, bool(0.0) is False, bool("") is False — everything else is True.',
            'For Is positive, check if the type is numeric first; if not, print N/A.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '42',
                'expected_output': (
                    'Value: 42\n'
                    'Type: int\n'
                    'Is integer: True\n'
                    'Is numeric: True\n'
                    'Is positive: True\n'
                    'Boolean value: True'
                ),
            },
            {
                'input': '3.14',
                'expected_output': (
                    'Value: 3.14\n'
                    'Type: float\n'
                    'Is integer: False\n'
                    'Is numeric: True\n'
                    'Is positive: True\n'
                    'Boolean value: True'
                ),
            },
            {
                'input': 'hello',
                'expected_output': (
                    'Value: hello\n'
                    'Type: str\n'
                    'Is integer: False\n'
                    'Is numeric: False\n'
                    'Is positive: N/A\n'
                    'Boolean value: True'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestBooleanLogic(unittest.TestCase):
    """Tests for Assignment 4: Boolean Logic & Type Checking."""

    def _run_student_code(self, inputs):
        input_gen = iter(inputs)
        captured = io.StringIO()
        with patch('builtins.input', side_effect=input_gen):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_integer_input(self):
        output = self._run_student_code(['42'])
        self.assertIn('Value: 42', output)
        self.assertIn('Type: int', output)
        self.assertIn('Is integer: True', output)
        self.assertIn('Is numeric: True', output)
        self.assertIn('Is positive: True', output)
        self.assertIn('Boolean value: True', output)

    def test_float_input(self):
        output = self._run_student_code(['3.14'])
        self.assertIn('Type: float', output)
        self.assertIn('Is integer: False', output)
        self.assertIn('Is numeric: True', output)
        self.assertIn('Is positive: True', output)

    def test_string_input(self):
        output = self._run_student_code(['hello'])
        self.assertIn('Type: str', output)
        self.assertIn('Is integer: False', output)
        self.assertIn('Is numeric: False', output)
        self.assertIn('Is positive: N/A', output)

    def test_zero_input(self):
        output = self._run_student_code(['0'])
        self.assertIn('Type: int', output)
        self.assertIn('Is positive: False', output)
        self.assertIn('Boolean value: False', output)

    def test_negative_float(self):
        output = self._run_student_code(['-2.5'])
        self.assertIn('Type: float', output)
        self.assertIn('Is positive: False', output)
        self.assertIn('Boolean value: True', output)


if __name__ == '__main__':
    unittest.main()
''',
    },
]
