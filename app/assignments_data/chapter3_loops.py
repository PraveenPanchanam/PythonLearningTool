"""
Chapter 3: Loops
Covers for loops, while loops, range(), break/continue, nested loops, and loop patterns.
"""

CHAPTER_INFO = {
    'title': 'Loops',
    'description': (
        'Learn how to repeat actions using loops in Python. '
        'This chapter covers for loops, while loops, the range() function, '
        'break and continue statements, nested loops, and common loop patterns.'
    ),
    'difficulty_level': 'beginner',
    'order': 3,
    'learning_objectives': [
        'Understand and use for loops to iterate over sequences',
        'Understand and use while loops for conditional repetition',
        'Use the range() function to generate number sequences',
        'Control loop execution with break and continue statements',
        'Write nested loops for multi-dimensional patterns',
        'Apply common loop patterns to solve problems',
    ],
    'estimated_time_minutes': 55,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1: Sum of Numbers
    # ------------------------------------------------------------------ #
    {
        'title': 'Sum of Numbers',
        'description': '''## Sum of Numbers

Write a program that reads an integer **n** from the user and computes the **sum of all integers from 1 to n** (inclusive).

### Requirements
- Read a single integer `n` from standard input.
- Use a **loop** (for or while) to calculate the sum `1 + 2 + 3 + ... + n`.
- Print **only** the resulting sum.

### Example
```
Input:  5
Output: 15
```
Because `1 + 2 + 3 + 4 + 5 = 15`.

### Constraints
- `n` will be a positive integer (n >= 1).
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            '# Read an integer n from the user\n'
            'n = int(input())\n\n'
            '# TODO: Use a loop to compute the sum of 1 to n\n'
            'total = 0\n\n'
            '# Print the result\n'
            'print(total)\n'
        ),
        'hints': [
            'Use a for loop with range(1, n + 1) to iterate from 1 to n.',
            'Keep a running total by adding each number in the loop.',
            'Remember that range(1, n+1) includes 1 but excludes n+1.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': '5', 'expected_output': '15'},
            {'input': '10', 'expected_output': '55'},
            {'input': '1', 'expected_output': '1'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestSumOfNumbers(unittest.TestCase):
    """Tests for the Sum of Numbers assignment."""

    def _run_program(self, input_value):
        """Helper: execute student_code.py with the given stdin and return stdout."""
        captured = io.StringIO()
        with patch('sys.stdin', io.StringIO(input_value)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open('student_code.py').read())
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_sum_of_5(self):
        result = self._run_program('5')
        self.assertEqual(result, '15', 'Sum of 1 to 5 should be 15')

    def test_sum_of_10(self):
        result = self._run_program('10')
        self.assertEqual(result, '55', 'Sum of 1 to 10 should be 55')

    def test_sum_of_1(self):
        result = self._run_program('1')
        self.assertEqual(result, '1', 'Sum of 1 to 1 should be 1')

    def test_sum_of_100(self):
        result = self._run_program('100')
        self.assertEqual(result, '5050', 'Sum of 1 to 100 should be 5050')

    def test_sum_of_20(self):
        result = self._run_program('20')
        self.assertEqual(result, '210', 'Sum of 1 to 20 should be 210')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2: Multiplication Table
    # ------------------------------------------------------------------ #
    {
        'title': 'Multiplication Table',
        'description': '''## Multiplication Table

Write a program that reads an integer **n** and prints its **multiplication table** from 1 to 10.

### Requirements
- Read a single integer `n` from standard input.
- Use a loop to print the multiplication table in the exact format shown below.
- Each line should follow the format: `n x i = result`

### Example
```
Input: 5
Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Constraints
- `n` will be a positive integer.
''',
        'difficulty': 'easy',
        'order': 2,
        'item_order': 4,
        'starter_code': (
            '# Read an integer n from the user\n'
            'n = int(input())\n\n'
            '# TODO: Print the multiplication table for n (1 through 10)\n'
            '# Format: n x i = result\n'
        ),
        'hints': [
            'Use a for loop with range(1, 11) to iterate from 1 to 10.',
            'Use an f-string like f"{n} x {i} = {n * i}" to format each line.',
            'Make sure there is exactly one space around "x" and "=".',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '5',
                'expected_output': (
                    '5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n'
                    '5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n'
                    '5 x 9 = 45\n5 x 10 = 50'
                ),
            },
            {
                'input': '3',
                'expected_output': (
                    '3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n'
                    '3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n'
                    '3 x 9 = 27\n3 x 10 = 30'
                ),
            },
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestMultiplicationTable(unittest.TestCase):
    """Tests for the Multiplication Table assignment."""

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

    def test_table_of_5(self):
        result = self._run_program('5')
        lines = result.split('\n')
        self.assertEqual(len(lines), 10, 'Table should have exactly 10 lines')
        self.assertEqual(lines[0], '5 x 1 = 5')
        self.assertEqual(lines[9], '5 x 10 = 50')

    def test_table_of_3(self):
        result = self._run_program('3')
        lines = result.split('\n')
        self.assertEqual(lines[0], '3 x 1 = 3')
        self.assertEqual(lines[4], '3 x 5 = 15')

    def test_table_of_1(self):
        result = self._run_program('1')
        lines = result.split('\n')
        self.assertEqual(len(lines), 10)
        self.assertEqual(lines[0], '1 x 1 = 1')
        self.assertEqual(lines[9], '1 x 10 = 10')

    def test_table_of_12(self):
        result = self._run_program('12')
        lines = result.split('\n')
        self.assertEqual(lines[0], '12 x 1 = 12')
        self.assertEqual(lines[9], '12 x 10 = 120')

    def test_format_correctness(self):
        result = self._run_program('7')
        lines = result.split('\n')
        for i, line in enumerate(lines, start=1):
            expected = f'7 x {i} = {7 * i}'
            self.assertEqual(line, expected, f'Line {i} format mismatch')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3: Pattern Printing
    # ------------------------------------------------------------------ #
    {
        'title': 'Pattern Printing',
        'description': '''## Pattern Printing

Write a program that reads an integer **n** (the height) and prints a **right-aligned triangle** made of `*` characters.

### Requirements
- Read a single integer `n` from standard input.
- Use **nested loops** to print a right triangle of height `n`.
- Row `i` (1-indexed) should contain exactly `i` asterisks (`*`), with **no leading spaces** and no trailing spaces.

### Example
```
Input: 5
Output:
*
**
***
****
*****
```

### Another Example
```
Input: 3
Output:
*
**
***
```

### Constraints
- `n` will be a positive integer (n >= 1).
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            '# Read the height of the triangle\n'
            'n = int(input())\n\n'
            '# TODO: Use nested loops (or string multiplication) to print the pattern\n'
            '# Row i should have i asterisks\n'
        ),
        'hints': [
            'Use an outer loop for each row (1 to n) and an inner loop or string multiplication for the stars.',
            'You can print i stars on row i with print("*" * i).',
            'Make sure there are no leading or trailing spaces on each line.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '5',
                'expected_output': '*\n**\n***\n****\n*****',
            },
            {
                'input': '3',
                'expected_output': '*\n**\n***',
            },
            {
                'input': '1',
                'expected_output': '*',
            },
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestPatternPrinting(unittest.TestCase):
    """Tests for the Pattern Printing assignment."""

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

    def test_height_5(self):
        result = self._run_program('5')
        lines = result.split('\n')
        self.assertEqual(len(lines), 5, 'Should have 5 rows')
        for i, line in enumerate(lines, start=1):
            self.assertEqual(line, '*' * i, f'Row {i} should have {i} stars')

    def test_height_3(self):
        result = self._run_program('3')
        lines = result.split('\n')
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0], '*')
        self.assertEqual(lines[2], '***')

    def test_height_1(self):
        result = self._run_program('1')
        self.assertEqual(result, '*', 'Single row should be one star')

    def test_height_8(self):
        result = self._run_program('8')
        lines = result.split('\n')
        self.assertEqual(len(lines), 8)
        self.assertEqual(lines[7], '********')

    def test_no_trailing_spaces(self):
        result = self._run_program('4')
        for line in result.split('\n'):
            self.assertEqual(line, line.rstrip(), 'Lines should have no trailing spaces')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4: Prime Number Checker
    # ------------------------------------------------------------------ #
    {
        'title': 'Prime Number Checker',
        'description': '''## Prime Number Checker

Write a program that reads an integer **n** and determines whether it is a **prime number**.

### Requirements
- Read a single integer `n` from standard input.
- Use a loop to check divisibility.
- Print `Prime` if the number is prime, or `Not Prime` otherwise.

### What is a prime number?
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers.

### Examples
```
Input: 7
Output: Prime

Input: 12
Output: Not Prime

Input: 2
Output: Prime

Input: 1
Output: Not Prime
```

### Constraints
- `n` will be a positive integer (n >= 1).
''',
        'difficulty': 'medium',
        'order': 4,
        'item_order': 7,
        'starter_code': (
            '# Read an integer n\n'
            'n = int(input())\n\n'
            '# TODO: Determine if n is prime\n'
            '# A prime number is greater than 1 and divisible only by 1 and itself\n'
            '# Hint: you only need to check divisors up to the square root of n\n\n'
            '# Print "Prime" or "Not Prime"\n'
        ),
        'hints': [
            'Numbers less than 2 are not prime.',
            'You only need to check divisors from 2 up to the square root of n (use int(n**0.5) + 1).',
            'If any number in that range divides n evenly (n % i == 0), then n is not prime.',
            'Use a boolean flag or the break statement to exit the loop early.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': '7', 'expected_output': 'Prime'},
            {'input': '12', 'expected_output': 'Not Prime'},
            {'input': '2', 'expected_output': 'Prime'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestPrimeNumberChecker(unittest.TestCase):
    """Tests for the Prime Number Checker assignment."""

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

    def test_prime_7(self):
        result = self._run_program('7')
        self.assertEqual(result, 'Prime')

    def test_not_prime_12(self):
        result = self._run_program('12')
        self.assertEqual(result, 'Not Prime')

    def test_prime_2(self):
        result = self._run_program('2')
        self.assertEqual(result, 'Prime', '2 is the smallest prime number')

    def test_not_prime_1(self):
        result = self._run_program('1')
        self.assertEqual(result, 'Not Prime', '1 is not a prime number')

    def test_large_prime_97(self):
        result = self._run_program('97')
        self.assertEqual(result, 'Prime', '97 is a prime number')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 5: Fibonacci Sequence
    # ------------------------------------------------------------------ #
    {
        'title': 'Fibonacci Sequence',
        'description': '''## Fibonacci Sequence

Write a program that reads an integer **n** and prints the **first n Fibonacci numbers**, separated by spaces on a single line.

### What is the Fibonacci Sequence?
The Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the two preceding numbers:

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

### Requirements
- Read a single integer `n` from standard input.
- Use a loop to generate the first `n` Fibonacci numbers.
- Print all `n` numbers on **one line**, separated by **spaces**.

### Examples
```
Input: 5
Output: 0 1 1 2 3

Input: 8
Output: 0 1 1 2 3 5 8 13

Input: 1
Output: 0
```

### Constraints
- `n` will be a positive integer (n >= 1).
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 8,
        'starter_code': (
            '# Read the number of Fibonacci numbers to generate\n'
            'n = int(input())\n\n'
            '# TODO: Generate the first n Fibonacci numbers\n'
            '# The sequence starts: 0, 1, 1, 2, 3, 5, 8, ...\n'
            '# Each number is the sum of the two preceding numbers\n\n'
            '# Print the numbers separated by spaces on one line\n'
        ),
        'hints': [
            'Start with two variables: a = 0 and b = 1.',
            'In each iteration, the next Fibonacci number is a + b. Then shift: a becomes b, and b becomes the new sum.',
            'Collect the numbers in a list and use " ".join() or print with end=" " to output them on one line.',
            'Handle the edge case where n is 1 (output should be just "0").',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {'input': '5', 'expected_output': '0 1 1 2 3'},
            {'input': '8', 'expected_output': '0 1 1 2 3 5 8 13'},
            {'input': '1', 'expected_output': '0'},
        ],
        'test_cases_code': r'''
import unittest
import sys
import io
from unittest.mock import patch


class TestFibonacciSequence(unittest.TestCase):
    """Tests for the Fibonacci Sequence assignment."""

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

    def test_first_5(self):
        result = self._run_program('5')
        self.assertEqual(result, '0 1 1 2 3')

    def test_first_8(self):
        result = self._run_program('8')
        self.assertEqual(result, '0 1 1 2 3 5 8 13')

    def test_first_1(self):
        result = self._run_program('1')
        self.assertEqual(result, '0', 'First Fibonacci number is 0')

    def test_first_2(self):
        result = self._run_program('2')
        self.assertEqual(result, '0 1', 'First two Fibonacci numbers are 0 and 1')

    def test_first_10(self):
        result = self._run_program('10')
        self.assertEqual(result, '0 1 1 2 3 5 8 13 21 34')


if __name__ == '__main__':
    unittest.main()
''',
    },
]
