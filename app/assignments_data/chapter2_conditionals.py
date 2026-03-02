"""
Chapter 2: Conditional Statements
Assignment data for the Python Learning Tool.
"""

CHAPTER_INFO = {
    'title': 'Conditional Statements',
    'description': (
        'Learn how to make decisions in your programs using conditional statements. '
        'This chapter covers if/elif/else blocks, comparison operators, logical operators '
        '(and, or, not), nested conditionals, and the ternary (conditional) expression. '
        'These constructs allow your code to respond differently based on varying inputs.'
    ),
    'difficulty_level': 'beginner',
    'order': 2,
    'learning_objectives': [
        'Write if, elif, and else statements to control program flow',
        'Use comparison operators (==, !=, <, >, <=, >=)',
        'Combine conditions with logical operators (and, or, not)',
        'Build nested conditional structures for complex logic',
        'Use the ternary (conditional) expression for concise assignments',
    ],
    'estimated_time_minutes': 50,
}

ASSIGNMENTS = [
    # ----------------------------------------------------------------
    # Assignment 1: Grade Calculator
    # ----------------------------------------------------------------
    {
        'title': 'Grade Calculator',
        'description': '''## Grade Calculator

Write a program that converts a **numeric score** into a **letter grade**.

### Requirements

1. Read a score from the user with the prompt `Enter your score: `.
2. Convert the score to an **integer**.
3. Determine the letter grade using this scale:
   - **A**: 90 -- 100
   - **B**: 80 -- 89
   - **C**: 70 -- 79
   - **D**: 60 -- 69
   - **F**: below 60
4. If the score is **less than 0 or greater than 100**, print `Invalid score` instead.
5. Print the result as:

```
Grade: <letter>
```

### Example

**Input:**
```
85
```

**Output:**
```
Grade: B
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            '# Assignment 1: Grade Calculator\n'
            '# Convert a numeric score to a letter grade.\n\n'
            'score = int(input("Enter your score: "))\n\n'
            '# Determine the letter grade using if/elif/else\n'
            '# ...\n\n'
            '# Print the grade\n'
            '# print(...)\n'
        ),
        'hints': [
            'Start by checking for invalid scores (less than 0 or greater than 100).',
            'Use if/elif/else to check ranges from highest to lowest.',
            'Remember that range 90-100 means score >= 90 and score <= 100.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '85',
                'expected_output': 'Grade: B',
            },
            {
                'input': '95',
                'expected_output': 'Grade: A',
            },
            {
                'input': '45',
                'expected_output': 'Grade: F',
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestGradeCalculator(unittest.TestCase):
    """Tests for Assignment 1: Grade Calculator."""

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

    def test_grade_a(self):
        output = self._run_student_code(['95'])
        self.assertIn('Grade: A', output)

    def test_grade_b(self):
        output = self._run_student_code(['85'])
        self.assertIn('Grade: B', output)

    def test_grade_c(self):
        output = self._run_student_code(['75'])
        self.assertIn('Grade: C', output)

    def test_grade_d(self):
        output = self._run_student_code(['65'])
        self.assertIn('Grade: D', output)

    def test_grade_f(self):
        output = self._run_student_code(['45'])
        self.assertIn('Grade: F', output)

    def test_boundary_a(self):
        output = self._run_student_code(['90'])
        self.assertIn('Grade: A', output)

    def test_boundary_b(self):
        output = self._run_student_code(['80'])
        self.assertIn('Grade: B', output)

    def test_perfect_score(self):
        output = self._run_student_code(['100'])
        self.assertIn('Grade: A', output)

    def test_zero_score(self):
        output = self._run_student_code(['0'])
        self.assertIn('Grade: F', output)

    def test_invalid_high(self):
        output = self._run_student_code(['105'])
        self.assertIn('Invalid score', output)

    def test_invalid_negative(self):
        output = self._run_student_code(['-5'])
        self.assertIn('Invalid score', output)


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ----------------------------------------------------------------
    # Assignment 2: Number Classifier
    # ----------------------------------------------------------------
    {
        'title': 'Number Classifier',
        'description': '''## Number Classifier

Write a program that **classifies a number** along two dimensions: its sign and its parity (even/odd).

### Requirements

1. Read a number from the user with the prompt `Enter a number: `.
2. Convert it to an **integer**.
3. Determine whether the number is **Positive**, **Negative**, or **Zero**.
4. Determine whether the number is **Even** or **Odd**.
5. Print two lines:

```
Sign: <Positive/Negative/Zero>
Parity: <Even/Odd>
```

> **Note:** Zero is considered **Even**.

### Example

**Input:**
```
-7
```

**Output:**
```
Sign: Negative
Parity: Odd
```
''',
        'difficulty': 'easy',
        'order': 2,
        'item_order': 3,
        'starter_code': (
            '# Assignment 2: Number Classifier\n'
            '# Classify a number by sign and parity.\n\n'
            'num = int(input("Enter a number: "))\n\n'
            '# Determine sign: Positive, Negative, or Zero\n'
            '# ...\n\n'
            '# Determine parity: Even or Odd\n'
            '# ...\n\n'
            '# Print results\n'
            '# print(...)\n'
        ),
        'hints': [
            'Use if/elif/else to check > 0, < 0, or == 0 for the sign.',
            'Use the modulo operator (%) to check even or odd: num % 2 == 0 means even.',
            'Zero is even because 0 % 2 == 0.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '-7',
                'expected_output': 'Sign: Negative\nParity: Odd',
            },
            {
                'input': '4',
                'expected_output': 'Sign: Positive\nParity: Even',
            },
            {
                'input': '0',
                'expected_output': 'Sign: Zero\nParity: Even',
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestNumberClassifier(unittest.TestCase):
    """Tests for Assignment 2: Number Classifier."""

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

    def test_negative_odd(self):
        output = self._run_student_code(['-7'])
        self.assertIn('Sign: Negative', output)
        self.assertIn('Parity: Odd', output)

    def test_positive_even(self):
        output = self._run_student_code(['4'])
        self.assertIn('Sign: Positive', output)
        self.assertIn('Parity: Even', output)

    def test_zero(self):
        output = self._run_student_code(['0'])
        self.assertIn('Sign: Zero', output)
        self.assertIn('Parity: Even', output)

    def test_positive_odd(self):
        output = self._run_student_code(['13'])
        self.assertIn('Sign: Positive', output)
        self.assertIn('Parity: Odd', output)

    def test_negative_even(self):
        output = self._run_student_code(['-8'])
        self.assertIn('Sign: Negative', output)
        self.assertIn('Parity: Even', output)

    def test_one(self):
        output = self._run_student_code(['1'])
        self.assertIn('Sign: Positive', output)
        self.assertIn('Parity: Odd', output)

    def test_output_line_count(self):
        output = self._run_student_code(['5'])
        lines = output.strip().split('\\n')
        self.assertEqual(len(lines), 2, 'Expected exactly 2 lines of output')


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ----------------------------------------------------------------
    # Assignment 3: Leap Year Checker
    # ----------------------------------------------------------------
    {
        'title': 'Leap Year Checker',
        'description': '''## Leap Year Checker

Write a program that determines whether a given year is a **leap year**.

### Rules for Leap Years

A year is a leap year if:
1. It is divisible by **4**, **AND**
2. It is **not** divisible by **100**, **UNLESS** it is also divisible by **400**.

In simpler terms:
- Divisible by 400 --> **leap year**
- Divisible by 100 but not 400 --> **not a leap year**
- Divisible by 4 but not 100 --> **leap year**
- Not divisible by 4 --> **not a leap year**

### Requirements

1. Read a year from the user with the prompt `Enter a year: `.
2. Convert it to an **integer**.
3. Print one of:

```
<year> is a leap year
```
or
```
<year> is not a leap year
```

### Example

**Input:**
```
2024
```

**Output:**
```
2024 is a leap year
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            '# Assignment 3: Leap Year Checker\n'
            '# Determine if a given year is a leap year.\n\n'
            'year = int(input("Enter a year: "))\n\n'
            '# Apply the leap year rules\n'
            '# A year is a leap year if:\n'
            '#   - divisible by 4 AND not divisible by 100\n'
            '#   - OR divisible by 400\n'
            '# ...\n\n'
            '# Print the result\n'
            '# print(...)\n'
        ),
        'hints': [
            'Check divisibility using the modulo operator: year % 4 == 0.',
            'Order matters: check divisibility by 400 first, then by 100, then by 4.',
            'You can combine conditions: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0).',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '2024',
                'expected_output': '2024 is a leap year',
            },
            {
                'input': '1900',
                'expected_output': '1900 is not a leap year',
            },
            {
                'input': '2000',
                'expected_output': '2000 is a leap year',
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestLeapYearChecker(unittest.TestCase):
    """Tests for Assignment 3: Leap Year Checker."""

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

    def test_divisible_by_4(self):
        output = self._run_student_code(['2024'])
        self.assertIn('2024 is a leap year', output)

    def test_divisible_by_100_not_400(self):
        output = self._run_student_code(['1900'])
        self.assertIn('1900 is not a leap year', output)

    def test_divisible_by_400(self):
        output = self._run_student_code(['2000'])
        self.assertIn('2000 is a leap year', output)

    def test_not_divisible_by_4(self):
        output = self._run_student_code(['2023'])
        self.assertIn('2023 is not a leap year', output)

    def test_another_leap_year(self):
        output = self._run_student_code(['2020'])
        self.assertIn('2020 is a leap year', output)

    def test_century_not_leap(self):
        output = self._run_student_code(['1800'])
        self.assertIn('1800 is not a leap year', output)

    def test_century_leap(self):
        output = self._run_student_code(['1600'])
        self.assertIn('1600 is a leap year', output)

    def test_odd_year(self):
        output = self._run_student_code(['2019'])
        self.assertIn('2019 is not a leap year', output)


if __name__ == '__main__':
    unittest.main()
''',
    },

    # ----------------------------------------------------------------
    # Assignment 4: Triangle Validator
    # ----------------------------------------------------------------
    {
        'title': 'Triangle Validator',
        'description': '''## Triangle Validator

Write a program that checks whether three side lengths can form a **valid triangle** and, if so, classifies it.

### Triangle Inequality Rule

Three sides **a**, **b**, and **c** can form a valid triangle if and only if:
- a + b > c
- a + c > b
- b + c > a

All three conditions must hold. Additionally, all sides must be **positive** numbers.

### Triangle Classification

- **Equilateral**: all three sides are equal.
- **Isosceles**: exactly two sides are equal.
- **Scalene**: no sides are equal.

### Requirements

1. Read three side lengths from the user with the prompts:
   - `Enter side a: `
   - `Enter side b: `
   - `Enter side c: `
2. Convert each to a **float**.
3. First, check if all sides are positive. If any side is <= 0, print `Invalid: sides must be positive`.
4. Then, check the triangle inequality. If it fails, print `Not a valid triangle`.
5. If valid, classify and print:

```
Valid triangle: <Equilateral/Isosceles/Scalene>
```

### Example

**Input:**
```
3
4
5
```

**Output:**
```
Valid triangle: Scalene
```
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 6,
        'starter_code': (
            '# Assignment 4: Triangle Validator\n'
            '# Check if three sides form a valid triangle and classify it.\n\n'
            'a = float(input("Enter side a: "))\n'
            'b = float(input("Enter side b: "))\n'
            'c = float(input("Enter side c: "))\n\n'
            '# Step 1: Check if all sides are positive\n'
            '# ...\n\n'
            '# Step 2: Check the triangle inequality\n'
            '# ...\n\n'
            '# Step 3: Classify the triangle\n'
            '# ...\n\n'
            '# Step 4: Print the result\n'
            '# print(...)\n'
        ),
        'hints': [
            'Check all three sides are > 0 first.',
            'The triangle inequality requires all three pair-sums to be greater than the third side.',
            'For classification: if a == b == c it is equilateral; if a == b or b == c or a == c it is isosceles; otherwise scalene.',
            'Use and/or to combine multiple conditions in a single if statement.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '3\n4\n5',
                'expected_output': 'Valid triangle: Scalene',
            },
            {
                'input': '5\n5\n5',
                'expected_output': 'Valid triangle: Equilateral',
            },
            {
                'input': '1\n2\n10',
                'expected_output': 'Not a valid triangle',
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch


class TestTriangleValidator(unittest.TestCase):
    """Tests for Assignment 4: Triangle Validator."""

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

    def test_scalene(self):
        output = self._run_student_code(['3', '4', '5'])
        self.assertIn('Valid triangle: Scalene', output)

    def test_equilateral(self):
        output = self._run_student_code(['5', '5', '5'])
        self.assertIn('Valid triangle: Equilateral', output)

    def test_isosceles(self):
        output = self._run_student_code(['5', '5', '3'])
        self.assertIn('Valid triangle: Isosceles', output)

    def test_invalid_triangle(self):
        output = self._run_student_code(['1', '2', '10'])
        self.assertIn('Not a valid triangle', output)

    def test_negative_side(self):
        output = self._run_student_code(['-1', '3', '4'])
        self.assertIn('Invalid: sides must be positive', output)

    def test_zero_side(self):
        output = self._run_student_code(['0', '5', '5'])
        self.assertIn('Invalid: sides must be positive', output)

    def test_isosceles_second_pair(self):
        output = self._run_student_code(['3', '5', '5'])
        self.assertIn('Valid triangle: Isosceles', output)

    def test_isosceles_first_last(self):
        output = self._run_student_code(['7', '5', '7'])
        self.assertIn('Valid triangle: Isosceles', output)

    def test_barely_invalid(self):
        """1 + 2 = 3, which is NOT greater than 3."""
        output = self._run_student_code(['1', '2', '3'])
        self.assertIn('Not a valid triangle', output)

    def test_decimal_sides(self):
        output = self._run_student_code(['3.5', '4.5', '5.5'])
        self.assertIn('Valid triangle: Scalene', output)


if __name__ == '__main__':
    unittest.main()
''',
    },
]
