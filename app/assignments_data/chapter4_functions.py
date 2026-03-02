"""
Chapter 4: Functions
Covers function definition, parameters, return values, default arguments,
*args/**kwargs, lambda functions, and recursion.
"""

CHAPTER_INFO = {
    'title': 'Functions',
    'description': (
        'Master the art of writing reusable code with Python functions. '
        'This chapter covers function definition, parameters and return values, '
        'default arguments, variable-length arguments (*args/**kwargs), '
        'lambda functions, and recursion.'
    ),
    'difficulty_level': 'intermediate',
    'order': 4,
    'learning_objectives': [
        'Define and call functions with parameters and return values',
        'Use default arguments and keyword arguments effectively',
        'Work with variable-length arguments using *args and **kwargs',
        'Write concise functions using lambda expressions',
        'Understand and implement recursive functions',
        'Create higher-order functions that accept or return other functions',
    ],
    'estimated_time_minutes': 60,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1: Basic Calculator Functions
    # ------------------------------------------------------------------ #
    {
        'title': 'Basic Calculator Functions',
        'description': '''## Basic Calculator Functions

Create a simple calculator by writing four functions: `add`, `subtract`, `multiply`, and `divide`.

### Requirements

Define the following functions:

1. **`add(a, b)`** -- Returns the sum of `a` and `b`.
2. **`subtract(a, b)`** -- Returns the difference `a - b`.
3. **`multiply(a, b)`** -- Returns the product of `a` and `b`.
4. **`divide(a, b)`** -- Returns the result of `a / b`.
   - If `b` is `0`, return the string `"Error: Division by zero"` instead of performing the division.

After defining the functions, read **three values** from standard input (one per line):
1. The operation as a string: `"add"`, `"subtract"`, `"multiply"`, or `"divide"`.
2. The first number (float).
3. The second number (float).

Call the appropriate function and **print the result**. For non-division results, if the result is a whole number, print it as an integer (e.g., `10` not `10.0`).

### Examples
```
Input:
add
10
5
Output: 15

Input:
divide
10
0
Output: Error: Division by zero

Input:
multiply
3.5
2
Output: 7.0
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            '# Define your calculator functions here\n\n'
            'def add(a, b):\n'
            '    # TODO: return the sum\n'
            '    pass\n\n'
            'def subtract(a, b):\n'
            '    # TODO: return the difference\n'
            '    pass\n\n'
            'def multiply(a, b):\n'
            '    # TODO: return the product\n'
            '    pass\n\n'
            'def divide(a, b):\n'
            '    # TODO: return the quotient, handle division by zero\n'
            '    pass\n\n\n'
            '# Read inputs\n'
            'operation = input()\n'
            'a = float(input())\n'
            'b = float(input())\n\n'
            '# TODO: Call the correct function based on operation and print the result\n'
        ),
        'hints': [
            'Use if/elif statements to select the correct function based on the operation string.',
            'For divide, check if b == 0 before performing the division.',
            'To print a whole number without the decimal, check: if result == int(result): print(int(result))',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': 'add\n10\n5', 'expected_output': '15'},
            {'input': 'divide\n10\n0', 'expected_output': 'Error: Division by zero'},
            {'input': 'multiply\n3.5\n2', 'expected_output': '7.0'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestBasicCalculatorFunctions(unittest.TestCase):
    """Tests for the Basic Calculator Functions assignment."""

    def _run_program(self, input_value):
        captured = io.StringIO()
        with patch('sys.stdin', io.StringIO(input_value)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def _load_functions(self):
        """Load student module and return the four functions."""
        ns = {}
        exec(open('student_code.py').read(), ns)
        return ns.get('add'), ns.get('subtract'), ns.get('multiply'), ns.get('divide')

    def test_add(self):
        result = self._run_program('add\n10\n5')
        self.assertEqual(result, '15')

    def test_subtract(self):
        result = self._run_program('subtract\n20\n8')
        self.assertEqual(result, '12')

    def test_multiply(self):
        result = self._run_program('multiply\n3.5\n2')
        self.assertEqual(result, '7.0')

    def test_divide(self):
        result = self._run_program('divide\n20\n4')
        self.assertEqual(result, '5.0')

    def test_divide_by_zero(self):
        result = self._run_program('divide\n10\n0')
        self.assertEqual(result, 'Error: Division by zero')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2: String Utility Functions
    # ------------------------------------------------------------------ #
    {
        'title': 'String Utility Functions',
        'description': '''## String Utility Functions

Write three useful string utility functions and use them based on user input.

### Requirements

Define the following functions:

1. **`is_palindrome(s)`** -- Returns `True` if the string `s` reads the same forwards and backwards (case-insensitive, ignoring spaces), `False` otherwise.
2. **`count_vowels(s)`** -- Returns the count of vowels (`a, e, i, o, u`, case-insensitive) in the string `s`.
3. **`reverse_words(s)`** -- Returns a new string with the **order of words reversed** (not the characters). Words are separated by spaces.

After defining the functions, read **two values** from standard input:
1. The function name: `"is_palindrome"`, `"count_vowels"`, or `"reverse_words"`.
2. The input string.

Call the appropriate function and print the result.

### Examples
```
Input:
is_palindrome
Race Car
Output: True

Input:
count_vowels
Hello World
Output: 3

Input:
reverse_words
Hello World Python
Output: Python World Hello
```
''',
        'difficulty': 'medium',
        'order': 2,
        'item_order': 3,
        'starter_code': (
            'def is_palindrome(s):\n'
            '    """Return True if s is a palindrome (case-insensitive, ignore spaces)."""\n'
            '    # TODO: implement\n'
            '    pass\n\n'
            'def count_vowels(s):\n'
            '    """Return the number of vowels in s."""\n'
            '    # TODO: implement\n'
            '    pass\n\n'
            'def reverse_words(s):\n'
            '    """Return s with the word order reversed."""\n'
            '    # TODO: implement\n'
            '    pass\n\n\n'
            '# Read inputs\n'
            'func_name = input()\n'
            'text = input()\n\n'
            '# TODO: Call the appropriate function and print the result\n'
        ),
        'hints': [
            'For is_palindrome, convert to lowercase and remove spaces, then compare the string to its reverse (s[::-1]).',
            'For count_vowels, iterate through each character and check if it is in "aeiouAEIOU".',
            'For reverse_words, use s.split() to get a list of words, reverse it, and join with " ".',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': 'is_palindrome\nRace Car', 'expected_output': 'True'},
            {'input': 'count_vowels\nHello World', 'expected_output': '3'},
            {'input': 'reverse_words\nHello World Python', 'expected_output': 'Python World Hello'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestStringUtilityFunctions(unittest.TestCase):
    """Tests for the String Utility Functions assignment."""

    def _run_program(self, input_value):
        captured = io.StringIO()
        with patch('sys.stdin', io.StringIO(input_value)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_palindrome_true(self):
        result = self._run_program('is_palindrome\nRace Car')
        self.assertEqual(result, 'True')

    def test_palindrome_false(self):
        result = self._run_program('is_palindrome\nHello')
        self.assertEqual(result, 'False')

    def test_count_vowels(self):
        result = self._run_program('count_vowels\nHello World')
        self.assertEqual(result, '3')

    def test_count_vowels_all(self):
        result = self._run_program('count_vowels\naeiou')
        self.assertEqual(result, '5')

    def test_reverse_words(self):
        result = self._run_program('reverse_words\nHello World Python')
        self.assertEqual(result, 'Python World Hello')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3: Recursive Functions
    # ------------------------------------------------------------------ #
    {
        'title': 'Recursive Functions',
        'description': '''## Recursive Functions

Learn recursion by implementing two classic mathematical functions **without using loops**.

### Requirements

Define the following functions using **recursion only** (no for/while loops):

1. **`factorial(n)`** -- Returns `n!` (n factorial).
   - `factorial(0) = 1`
   - `factorial(n) = n * factorial(n - 1)` for n > 0

2. **`power(base, exp)`** -- Returns `base` raised to the power `exp`.
   - `power(base, 0) = 1`
   - `power(base, exp) = base * power(base, exp - 1)` for exp > 0

After defining the functions, read **three values** from standard input:
1. The function name: `"factorial"` or `"power"`.
2. For `factorial`: a single integer `n`. For `power`: two integers `base` and `exp` (on the same line, space-separated).

Call the appropriate function and **print the result**.

### Examples
```
Input:
factorial
5
Output: 120

Input:
power
2 10
Output: 1024

Input:
factorial
0
Output: 1
```

### Constraints
- For factorial: `0 <= n <= 20`
- For power: `exp >= 0`
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            'def factorial(n):\n'
            '    """Return n! using recursion."""\n'
            '    # TODO: implement with recursion (no loops)\n'
            '    # Base case: factorial(0) = 1\n'
            '    pass\n\n'
            'def power(base, exp):\n'
            '    """Return base ** exp using recursion."""\n'
            '    # TODO: implement with recursion (no loops)\n'
            '    # Base case: power(base, 0) = 1\n'
            '    pass\n\n\n'
            '# Read inputs\n'
            'func_name = input()\n\n'
            '# TODO: Read the appropriate arguments and call the function\n'
            '# Print the result\n'
        ),
        'hints': [
            'Every recursive function needs a base case (when to stop) and a recursive case.',
            'For factorial: if n == 0, return 1. Otherwise return n * factorial(n - 1).',
            'For power: if exp == 0, return 1. Otherwise return base * power(base, exp - 1).',
            'Use input().split() to read base and exp on the same line for the power function.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': 'factorial\n5', 'expected_output': '120'},
            {'input': 'power\n2 10', 'expected_output': '1024'},
            {'input': 'factorial\n0', 'expected_output': '1'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
import inspect
from unittest.mock import patch


class TestRecursiveFunctions(unittest.TestCase):
    """Tests for the Recursive Functions assignment."""

    def _run_program(self, input_value):
        captured = io.StringIO()
        with patch('sys.stdin', io.StringIO(input_value)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def _load_functions(self):
        ns = {}
        with patch('sys.stdin', io.StringIO('factorial\n1')):
            exec(open('student_code.py').read(), ns)
        return ns.get('factorial'), ns.get('power')

    def test_factorial_5(self):
        result = self._run_program('factorial\n5')
        self.assertEqual(result, '120')

    def test_factorial_0(self):
        result = self._run_program('factorial\n0')
        self.assertEqual(result, '1')

    def test_power_2_10(self):
        result = self._run_program('power\n2 10')
        self.assertEqual(result, '1024')

    def test_power_base_0(self):
        result = self._run_program('power\n5 0')
        self.assertEqual(result, '1')

    def test_factorial_is_recursive(self):
        """Check that the factorial function actually uses recursion."""
        factorial_fn, _ = self._load_functions()
        if factorial_fn is not None:
            source = inspect.getsource(factorial_fn)
            self.assertIn('factorial', source.split('\n', 1)[-1],
                          'factorial should call itself recursively')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4: Higher-Order Functions
    # ------------------------------------------------------------------ #
    {
        'title': 'Higher-Order Functions',
        'description': '''## Higher-Order Functions

Explore the power of functions that **accept other functions as arguments** or **return new functions**.

### Requirements

Define the following:

1. **`apply_operation(func, a, b)`** -- Takes a function `func` and two numbers `a`, `b`. Returns the result of calling `func(a, b)`.

2. **`create_multiplier(factor)`** -- Returns a **new function** that multiplies its single argument by `factor`.
   - For example, `double = create_multiplier(2)` creates a function where `double(5)` returns `10`.

After defining the functions, read input to demonstrate them:

**Line 1**: The command -- `"apply"` or `"multiplier"`.

If `"apply"`:
- **Line 2**: Operation name -- `"add"`, `"subtract"`, `"multiply"`.
- **Line 3**: Two space-separated numbers.
- Use a lambda or a simple function for the operation, pass it to `apply_operation`, and print the result.

If `"multiplier"`:
- **Line 2**: The factor (integer).
- **Line 3**: The value to multiply (integer).
- Create a multiplier function using `create_multiplier(factor)`, call it with the value, and print the result.

Print the result as an integer if it is a whole number.

### Examples
```
Input:
apply
add
10 5
Output: 15

Input:
multiplier
3
7
Output: 21

Input:
apply
multiply
4 5
Output: 20
```
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 6,
        'starter_code': (
            'def apply_operation(func, a, b):\n'
            '    """Apply func to a and b, return the result."""\n'
            '    # TODO: implement\n'
            '    pass\n\n'
            'def create_multiplier(factor):\n'
            '    """Return a new function that multiplies its argument by factor."""\n'
            '    # TODO: implement -- return a lambda or inner function\n'
            '    pass\n\n\n'
            '# Read command\n'
            'command = input()\n\n'
            '# TODO: Based on command, read remaining input, call the right function,\n'
            '#       and print the result.\n'
        ),
        'hints': [
            'apply_operation simply returns func(a, b).',
            'create_multiplier should define an inner function or lambda that captures factor via closure.',
            'For the "apply" command, map operation names to lambdas: {"add": lambda a, b: a + b, ...}.',
            'A closure is a function that remembers variables from the scope where it was created.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': 'apply\nadd\n10 5', 'expected_output': '15'},
            {'input': 'multiplier\n3\n7', 'expected_output': '21'},
            {'input': 'apply\nmultiply\n4 5', 'expected_output': '20'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestHigherOrderFunctions(unittest.TestCase):
    """Tests for the Higher-Order Functions assignment."""

    def _run_program(self, input_value):
        captured = io.StringIO()
        with patch('sys.stdin', io.StringIO(input_value)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def _load_functions(self):
        ns = {}
        with patch('sys.stdin', io.StringIO('apply\nadd\n1 1')):
            exec(open('student_code.py').read(), ns)
        return ns.get('apply_operation'), ns.get('create_multiplier')

    def test_apply_add(self):
        result = self._run_program('apply\nadd\n10 5')
        self.assertEqual(result, '15')

    def test_apply_multiply(self):
        result = self._run_program('apply\nmultiply\n4 5')
        self.assertEqual(result, '20')

    def test_apply_subtract(self):
        result = self._run_program('apply\nsubtract\n20 8')
        self.assertEqual(result, '12')

    def test_multiplier(self):
        result = self._run_program('multiplier\n3\n7')
        self.assertEqual(result, '21')

    def test_create_multiplier_returns_function(self):
        """Verify create_multiplier returns a callable."""
        _, create_multiplier = self._load_functions()
        if create_multiplier is not None:
            fn = create_multiplier(5)
            self.assertTrue(callable(fn), 'create_multiplier should return a callable')
            self.assertEqual(fn(4), 20, 'create_multiplier(5)(4) should be 20')


if __name__ == '__main__':
    unittest.main()
''',
    },
]
