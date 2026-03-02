CHAPTER_INFO = {
    'title': 'Data Structures',
    'description': (
        'Master Python\'s built-in data structures including lists, tuples, '
        'dictionaries, and sets. Learn powerful techniques like list comprehensions, '
        'dictionary comprehensions, sorting, slicing, and common methods that '
        'make working with collections efficient and Pythonic.'
    ),
    'difficulty_level': 'intermediate',
    'order': 5,
    'learning_objectives': [
        'Create and manipulate lists using indexing, slicing, and built-in methods',
        'Understand tuples and when to use them over lists',
        'Build and query dictionaries for key-value storage',
        'Use sets for membership testing and mathematical set operations',
        'Write list comprehensions to filter and transform data concisely',
        'Write dictionary comprehensions to build dicts from iterables',
        'Sort collections with sorted() and custom key functions',
        'Combine and nest data structures for complex data modeling',
    ],
    'estimated_time_minutes': 65,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------
    # Assignment 1: List Operations
    # ------------------------------------------------------------------
    {
        'title': 'List Operations',
        'description': '''## List Operations

Write a program that reads a list of integers from the user and performs several common operations on it.

### Requirements

1. Read a single line of **space-separated integers** from standard input.
2. Print the following statistics, each on its own line and **exactly** in this order:
   - `Min: <value>`
   - `Max: <value>`
   - `Sum: <value>`
   - `Average: <value>` (formatted to **2 decimal places**)
   - `Sorted: <space-separated sorted list>`
   - `Reversed: <space-separated reverse-sorted list>`

### Example

**Input:**
```
5 3 8 1 9 2
```

**Output:**
```
Min: 1
Max: 9
Sum: 28
Average: 4.67
Sorted: 1 2 3 5 8 9
Reversed: 9 8 5 3 2 1
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            '# Read space-separated integers from input\n'
            'numbers = list(map(int, input().split()))\n\n'
            '# TODO: Find and print Min, Max, Sum, Average\n\n'
            '# TODO: Print the sorted list and the reversed sorted list\n'
        ),
        'hints': [
            'Use the built-in functions min(), max(), and sum().',
            'Average is sum divided by len. Use f-string formatting like f"{avg:.2f}" for 2 decimal places.',
            'sorted() returns a new sorted list. You can reverse it with sorted(numbers, reverse=True) or slicing [::-1].',
            'Use " ".join(map(str, some_list)) to print a list as space-separated values.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '5 3 8 1 9 2\n',
                'expected_output': (
                    'Min: 1\n'
                    'Max: 9\n'
                    'Sum: 28\n'
                    'Average: 4.67\n'
                    'Sorted: 1 2 3 5 8 9\n'
                    'Reversed: 9 8 5 3 2 1'
                ),
            },
            {
                'input': '10 20 30\n',
                'expected_output': (
                    'Min: 10\n'
                    'Max: 30\n'
                    'Sum: 60\n'
                    'Average: 20.00\n'
                    'Sorted: 10 20 30\n'
                    'Reversed: 30 20 10'
                ),
            },
            {
                'input': '42\n',
                'expected_output': (
                    'Min: 42\n'
                    'Max: 42\n'
                    'Sum: 42\n'
                    'Average: 42.00\n'
                    'Sorted: 42\n'
                    'Reversed: 42'
                ),
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestListOperations:
    def test_basic_list(self):
        out = run_student("5 3 8 1 9 2\\n")
        lines = out.split("\\n")
        assert lines[0] == "Min: 1"
        assert lines[1] == "Max: 9"
        assert lines[2] == "Sum: 28"
        assert lines[3] == "Average: 4.67"

    def test_sorted_and_reversed(self):
        out = run_student("5 3 8 1 9 2\\n")
        lines = out.split("\\n")
        assert lines[4] == "Sorted: 1 2 3 5 8 9"
        assert lines[5] == "Reversed: 9 8 5 3 2 1"

    def test_single_element(self):
        out = run_student("42\\n")
        lines = out.split("\\n")
        assert lines[0] == "Min: 42"
        assert lines[1] == "Max: 42"
        assert "Average: 42.00" in out

    def test_negative_numbers(self):
        out = run_student("-5 -1 -10 -3\\n")
        lines = out.split("\\n")
        assert lines[0] == "Min: -10"
        assert lines[1] == "Max: -1"
        assert lines[2] == "Sum: -19"

    def test_all_same(self):
        out = run_student("7 7 7 7\\n")
        assert "Min: 7" in out
        assert "Max: 7" in out
        assert "Average: 7.00" in out
''',
    },
    # ------------------------------------------------------------------
    # Assignment 2: Dictionary Word Counter
    # ------------------------------------------------------------------
    {
        'title': 'Dictionary Word Counter',
        'description': '''## Dictionary Word Counter

Write a program that counts the frequency of each word in a sentence.

### Requirements

1. Read a single line of text from standard input.
2. Convert all words to **lowercase** before counting.
3. Print each word and its count in **alphabetical order**, one per line, in the format:
   ```
   <word>: <count>
   ```

### Example

**Input:**
```
the cat sat on the mat the cat
```

**Output:**
```
cat: 2
mat: 1
on: 1
sat: 1
the: 3
```

### Notes
- Words are separated by spaces.
- You do not need to handle punctuation for this assignment.
''',
        'difficulty': 'medium',
        'order': 2,
        'item_order': 4,
        'starter_code': (
            '# Read a sentence from input\n'
            'sentence = input().strip()\n\n'
            '# TODO: Split into words, convert to lowercase\n\n'
            '# TODO: Count each word using a dictionary\n\n'
            '# TODO: Print words and counts in alphabetical order\n'
        ),
        'hints': [
            'Use str.lower() to convert the sentence to lowercase, then str.split() to get words.',
            'Create an empty dictionary. Loop through words; for each word, increment its count (use dict.get(word, 0) + 1).',
            'Use sorted() on the dictionary keys to iterate in alphabetical order.',
            'Alternatively, you can use collections.Counter, but try the manual approach first.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': 'the cat sat on the mat the cat\n',
                'expected_output': (
                    'cat: 2\n'
                    'mat: 1\n'
                    'on: 1\n'
                    'sat: 1\n'
                    'the: 3'
                ),
            },
            {
                'input': 'hello world hello\n',
                'expected_output': (
                    'hello: 2\n'
                    'world: 1'
                ),
            },
            {
                'input': 'Python python PYTHON\n',
                'expected_output': 'python: 3',
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestWordCounter:
    def test_basic_sentence(self):
        out = run_student("the cat sat on the mat the cat\\n")
        lines = out.split("\\n")
        assert "cat: 2" in lines
        assert "the: 3" in lines

    def test_alphabetical_order(self):
        out = run_student("banana apple cherry apple\\n")
        lines = out.split("\\n")
        words = [line.split(":")[0] for line in lines]
        assert words == sorted(words)

    def test_case_insensitive(self):
        out = run_student("Python python PYTHON\\n")
        assert out.strip() == "python: 3"

    def test_single_word(self):
        out = run_student("hello\\n")
        assert out.strip() == "hello: 1"

    def test_all_unique(self):
        out = run_student("a b c d\\n")
        lines = out.strip().split("\\n")
        assert len(lines) == 4
        assert lines[0] == "a: 1"
        assert lines[3] == "d: 1"
''',
    },
    # ------------------------------------------------------------------
    # Assignment 3: Set Operations
    # ------------------------------------------------------------------
    {
        'title': 'Set Operations',
        'description': '''## Set Operations

Write a program that performs common set operations on two sets of integers.

### Requirements

1. Read **two lines** from standard input. Each line contains space-separated integers.
2. Create a set from each line.
3. Print the following, each on its own line:
   - `Set A: <sorted elements, space-separated>`
   - `Set B: <sorted elements, space-separated>`
   - `Union: <sorted elements>`
   - `Intersection: <sorted elements>`
   - `Difference (A-B): <sorted elements>`
   - `Symmetric Difference: <sorted elements>`

If a result is empty, print the label followed by nothing (e.g., `Intersection: `).

### Example

**Input:**
```
1 2 3 4 5
3 4 5 6 7
```

**Output:**
```
Set A: 1 2 3 4 5
Set B: 3 4 5 6 7
Union: 1 2 3 4 5 6 7
Intersection: 3 4 5
Difference (A-B): 1 2
Symmetric Difference: 1 2 6 7
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            '# Read two lines of space-separated integers\n'
            'set_a = set(map(int, input().split()))\n'
            'set_b = set(map(int, input().split()))\n\n'
            '# TODO: Print Set A and Set B (sorted)\n\n'
            '# TODO: Compute and print union, intersection, difference, symmetric difference\n'
        ),
        'hints': [
            'Use set operators: | for union, & for intersection, - for difference, ^ for symmetric difference.',
            'When printing, sort the set first: sorted(my_set) returns a sorted list.',
            'Use " ".join(map(str, sorted(result))) to format the output.',
            'Difference (A-B) means elements in A that are NOT in B.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '1 2 3 4 5\n3 4 5 6 7\n',
                'expected_output': (
                    'Set A: 1 2 3 4 5\n'
                    'Set B: 3 4 5 6 7\n'
                    'Union: 1 2 3 4 5 6 7\n'
                    'Intersection: 3 4 5\n'
                    'Difference (A-B): 1 2\n'
                    'Symmetric Difference: 1 2 6 7'
                ),
            },
            {
                'input': '10 20 30\n30 40 50\n',
                'expected_output': (
                    'Set A: 10 20 30\n'
                    'Set B: 30 40 50\n'
                    'Union: 10 20 30 40 50\n'
                    'Intersection: 30\n'
                    'Difference (A-B): 10 20\n'
                    'Symmetric Difference: 10 20 40 50'
                ),
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestSetOperations:
    def test_basic_sets(self):
        out = run_student("1 2 3 4 5\\n3 4 5 6 7\\n")
        assert "Union: 1 2 3 4 5 6 7" in out
        assert "Intersection: 3 4 5" in out

    def test_difference(self):
        out = run_student("1 2 3 4 5\\n3 4 5 6 7\\n")
        assert "Difference (A-B): 1 2" in out

    def test_symmetric_difference(self):
        out = run_student("1 2 3 4 5\\n3 4 5 6 7\\n")
        assert "Symmetric Difference: 1 2 6 7" in out

    def test_no_overlap(self):
        out = run_student("1 2 3\\n4 5 6\\n")
        lines = out.split("\\n")
        inter_line = [l for l in lines if l.startswith("Intersection:")][0]
        assert inter_line.strip() == "Intersection:"

    def test_duplicate_input(self):
        out = run_student("1 1 2 2 3\\n3 3 4 4 5\\n")
        assert "Set A: 1 2 3" in out
        assert "Set B: 3 4 5" in out
''',
    },
    # ------------------------------------------------------------------
    # Assignment 4: List Comprehensions
    # ------------------------------------------------------------------
    {
        'title': 'List Comprehensions',
        'description': '''## List Comprehensions

Write a program that uses **list comprehensions** (and optionally dict comprehensions) to process data.

### Requirements

Read a single line of **space-separated integers** from standard input. Then print the following, each on its own line:

1. `Evens: <space-separated even numbers in original order>`
2. `Squares: <space-separated squares of all numbers>`
3. `Positive Evens Doubled: <space-separated values where even positive numbers are doubled>`
4. `Digit Map: <dict mapping each number to its digit count>`

For **Digit Map**, print the dictionary directly using `print(...)` on the dict. The keys should be the original integers and values should be the number of digits (e.g., `{5: 1, 300: 3}`).

### Example

**Input:**
```
5 12 -3 8 100 7
```

**Output:**
```
Evens: 12 8 100
Squares: 25 144 9 64 10000 49
Positive Evens Doubled: 24 16 200
Digit Map: {5: 1, 12: 2, -3: 2, 8: 1, 100: 3, 7: 1}
```

### Notes
- For digit count, count the digits of the **absolute value** (so -3 has 1 digit). *However*, to match the expected output format, use `len(str(n))` which counts the minus sign. Follow the example output.
- Actually, looking at the example: `-3` maps to `2`. So use `len(str(n))` which includes the minus sign for negative numbers.
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 7,
        'starter_code': (
            '# Read space-separated integers\n'
            'numbers = list(map(int, input().split()))\n\n'
            '# TODO: Use a list comprehension to get even numbers\n'
            'evens = []  # replace with comprehension\n\n'
            '# TODO: Use a list comprehension to get squares\n'
            'squares = []  # replace with comprehension\n\n'
            '# TODO: Use a list comprehension for positive evens doubled\n'
            'pos_evens_doubled = []  # replace with comprehension\n\n'
            '# TODO: Use a dict comprehension for digit map\n'
            'digit_map = {}  # replace with comprehension\n\n'
            '# Print results\n'
            'print("Evens:", " ".join(map(str, evens)))\n'
            'print("Squares:", " ".join(map(str, squares)))\n'
            'print("Positive Evens Doubled:", " ".join(map(str, pos_evens_doubled)))\n'
            'print("Digit Map:", digit_map)\n'
        ),
        'hints': [
            'Even numbers: [n for n in numbers if n % 2 == 0]',
            'Squares: [n**2 for n in numbers]',
            'Positive evens doubled: [n*2 for n in numbers if n > 0 and n % 2 == 0]',
            'Dict comprehension: {n: len(str(n)) for n in numbers}',
            'Make sure the order is preserved from the original input.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '5 12 -3 8 100 7\n',
                'expected_output': (
                    'Evens: 12 8 100\n'
                    'Squares: 25 144 9 64 10000 49\n'
                    'Positive Evens Doubled: 24 16 200\n'
                    'Digit Map: {5: 1, 12: 2, -3: 2, 8: 1, 100: 3, 7: 1}'
                ),
            },
            {
                'input': '1 2 3 4 5\n',
                'expected_output': (
                    'Evens: 2 4\n'
                    'Squares: 1 4 9 16 25\n'
                    'Positive Evens Doubled: 4 8\n'
                    'Digit Map: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}'
                ),
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestListComprehensions:
    def test_evens(self):
        out = run_student("5 12 -3 8 100 7\\n")
        lines = out.split("\\n")
        assert lines[0] == "Evens: 12 8 100"

    def test_squares(self):
        out = run_student("5 12 -3 8 100 7\\n")
        lines = out.split("\\n")
        assert lines[1] == "Squares: 25 144 9 64 10000 49"

    def test_positive_evens_doubled(self):
        out = run_student("5 12 -3 8 100 7\\n")
        lines = out.split("\\n")
        assert lines[2] == "Positive Evens Doubled: 24 16 200"

    def test_digit_map(self):
        out = run_student("1 2 3 4 5\\n")
        lines = out.split("\\n")
        assert lines[3] == "Digit Map: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}"

    def test_all_negative(self):
        out = run_student("-2 -4 -6\\n")
        lines = out.split("\\n")
        assert lines[0] == "Evens: -2 -4 -6"
        assert lines[2] == "Positive Evens Doubled:"
''',
    },
    # ------------------------------------------------------------------
    # Assignment 5: Nested Data Structures
    # ------------------------------------------------------------------
    {
        'title': 'Nested Data Structures',
        'description': '''## Nested Data Structures

Write a program that works with a list of student records (dictionaries) and computes statistics.

### Requirements

1. Read an integer **N** (number of students) from the first line.
2. For each student, read a line in the format: `name grade1 grade2 grade3`
   - `name` is a string (no spaces)
   - `grade1`, `grade2`, `grade3` are integers
3. Store each student as a dictionary: `{"name": ..., "grades": [g1, g2, g3]}` in a list.
4. Print the following:
   - `Class Average: <average of ALL grades, 2 decimal places>`
   - `Top Student: <name of student with highest average>`
   - `Students above average:` followed by the names of students whose individual average is **above** the class average, one per line, in the order they were entered.

### Example

**Input:**
```
3
Alice 85 90 78
Bob 92 88 95
Charlie 70 65 80
```

**Output:**
```
Class Average: 82.56
Top Student: Bob
Students above average:
Alice
Bob
```
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 8,
        'starter_code': (
            '# Read number of students\n'
            'n = int(input())\n\n'
            '# Read student records\n'
            'students = []\n'
            'for _ in range(n):\n'
            '    parts = input().split()\n'
            '    name = parts[0]\n'
            '    grades = list(map(int, parts[1:]))\n'
            '    # TODO: Create a dict and append to students list\n\n'
            '# TODO: Calculate class average (average of ALL grades)\n\n'
            '# TODO: Find the top student (highest individual average)\n\n'
            '# TODO: Find students above the class average\n\n'
            '# Print results\n'
        ),
        'hints': [
            'Store each student as {"name": name, "grades": grades} and append to the students list.',
            'For class average, collect ALL grades into one list and compute the mean.',
            'For each student, compute their own average with sum(s["grades"]) / len(s["grades"]).',
            'Top student: use max() with a key function, or loop and track the best.',
            'Students above average: loop through students, compare their average to the class average.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '3\nAlice 85 90 78\nBob 92 88 95\nCharlie 70 65 80\n',
                'expected_output': (
                    'Class Average: 82.56\n'
                    'Top Student: Bob\n'
                    'Students above average:\n'
                    'Alice\n'
                    'Bob'
                ),
            },
            {
                'input': '2\nEve 100 100 100\nMallory 50 50 50\n',
                'expected_output': (
                    'Class Average: 75.00\n'
                    'Top Student: Eve\n'
                    'Students above average:\n'
                    'Eve'
                ),
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestNestedDataStructures:
    def test_class_average(self):
        inp = "3\\nAlice 85 90 78\\nBob 92 88 95\\nCharlie 70 65 80\\n"
        out = run_student(inp)
        assert "Class Average: 82.56" in out

    def test_top_student(self):
        inp = "3\\nAlice 85 90 78\\nBob 92 88 95\\nCharlie 70 65 80\\n"
        out = run_student(inp)
        assert "Top Student: Bob" in out

    def test_above_average(self):
        inp = "3\\nAlice 85 90 78\\nBob 92 88 95\\nCharlie 70 65 80\\n"
        out = run_student(inp)
        lines = out.split("\\n")
        idx = lines.index("Students above average:")
        above = lines[idx+1:]
        assert "Alice" in above
        assert "Bob" in above
        assert "Charlie" not in above

    def test_two_students(self):
        inp = "2\\nEve 100 100 100\\nMallory 50 50 50\\n"
        out = run_student(inp)
        assert "Class Average: 75.00" in out
        assert "Top Student: Eve" in out

    def test_single_student(self):
        inp = "1\\nSolo 80 90 70\\n"
        out = run_student(inp)
        assert "Class Average: 80.00" in out
        assert "Top Student: Solo" in out
''',
    },
]
