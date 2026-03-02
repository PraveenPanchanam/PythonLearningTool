CHAPTER_INFO = {
    'title': 'Modules, Packages & Advanced Concepts',
    'description': (
        'Explore advanced Python concepts including decorators, generators, '
        'iterators, context managers, and powerful built-in functions like '
        'map, filter, reduce, enumerate, and zip. This chapter also '
        'introduces the collections module and itertools for efficient '
        'data processing.'
    ),
    'difficulty_level': 'advanced',
    'order': 8,
    'learning_objectives': [
        'Use map, filter, and reduce to transform data',
        'Write and apply decorators to functions',
        'Create generator functions using yield',
        'Understand iterators and the iterator protocol',
        'Use enumerate, zip, and the collections module',
        'Apply itertools for advanced iteration patterns',
        'Combine multiple concepts to build data pipelines',
    ],
    'estimated_time_minutes': 75,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1 – Map, Filter, Reduce
    # ------------------------------------------------------------------ #
    {
        'title': 'Map, Filter, Reduce',
        'description': '''## Map, Filter, Reduce

Learn to use Python's functional programming tools: `map`, `filter`,
and `reduce`.

### Requirements

Write the following **functions** (each must use `map`, `filter`, or
`reduce` as indicated):

1. **`square_all(numbers)`** – Use **`map`** to return a list of the
   squares of all numbers in the input list.

2. **`filter_evens(numbers)`** – Use **`filter`** to return a list
   containing only the even numbers from the input list.

3. **`sum_all(numbers)`** – Use **`reduce`** (from `functools`) to
   compute the sum of all numbers in the list. Return `0` for an
   empty list.

4. **`to_upper(strings)`** – Use **`map`** to return a list of all
   strings converted to uppercase.

5. **`filter_long_words(words, min_length)`** – Use **`filter`** to
   return a list of words whose length is **>= min_length**.

### Example

```python
print(square_all([1, 2, 3, 4]))       # [1, 4, 9, 16]
print(filter_evens([1, 2, 3, 4, 5]))  # [2, 4]
print(sum_all([1, 2, 3, 4]))          # 10
print(to_upper(["hi", "world"]))       # ['HI', 'WORLD']
print(filter_long_words(["hi", "hello", "world"], 4))  # ['hello', 'world']
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            'from functools import reduce\n'
            '\n'
            '\n'
            'def square_all(numbers):\n'
            '    """Use map to square all numbers."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def filter_evens(numbers):\n'
            '    """Use filter to keep only even numbers."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def sum_all(numbers):\n'
            '    """Use reduce to sum all numbers. Return 0 for empty list."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def to_upper(strings):\n'
            '    """Use map to convert all strings to uppercase."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def filter_long_words(words, min_length):\n'
            '    """Use filter to keep words with length >= min_length."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'print(square_all([1, 2, 3, 4]))\n'
            'print(filter_evens([1, 2, 3, 4, 5]))\n'
            'print(sum_all([1, 2, 3, 4]))\n'
            'print(to_upper(["hi", "world"]))\n'
            'print(filter_long_words(["hi", "hello", "world"], 4))\n'
        ),
        'hints': [
            'square_all: list(map(lambda x: x ** 2, numbers))',
            'filter_evens: list(filter(lambda x: x % 2 == 0, numbers))',
            'For sum_all on an empty list, use the initializer argument of reduce: reduce(func, numbers, 0).',
            'to_upper: list(map(str.upper, strings))',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    '[1, 4, 9, 16]\n'
                    '[2, 4]\n'
                    '10\n'
                    "['HI', 'WORLD']\n"
                    "['hello', 'world']"
                ),
            },
        ],
        'test_cases_code': '''
import unittest

class TestMapFilterReduce(unittest.TestCase):

    def setUp(self):
        exec(open("student_code.py").read(), globals())
        self.square_all = globals()["square_all"]
        self.filter_evens = globals()["filter_evens"]
        self.sum_all = globals()["sum_all"]
        self.to_upper = globals()["to_upper"]
        self.filter_long_words = globals()["filter_long_words"]

    def test_square_all(self):
        self.assertEqual(self.square_all([1, 2, 3, 4]), [1, 4, 9, 16])

    def test_filter_evens(self):
        self.assertEqual(self.filter_evens([1, 2, 3, 4, 5]), [2, 4])

    def test_sum_all(self):
        self.assertEqual(self.sum_all([1, 2, 3, 4]), 10)

    def test_sum_all_empty(self):
        self.assertEqual(self.sum_all([]), 0)

    def test_to_upper(self):
        self.assertEqual(self.to_upper(["hi", "world"]), ["HI", "WORLD"])

    def test_filter_long_words(self):
        result = self.filter_long_words(["hi", "hello", "world"], 4)
        self.assertEqual(result, ["hello", "world"])

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2 – Decorators
    # ------------------------------------------------------------------ #
    {
        'title': 'Decorators',
        'description': '''## Decorators

Learn to write and use Python decorators -- functions that wrap other
functions to add behaviour.

### Requirements

1. **`timer(func)`** decorator
   - Wrap any function so that it prints the execution time **after**
     calling it.
   - Format: `"<func_name> took <seconds:.4f> seconds"`
   - Return the original function's result.
   - Use `time.time()` to measure elapsed time.

2. **`logger(func)`** decorator
   - Before calling the function, print:
     `"Calling <func_name> with args=<args>, kwargs=<kwargs>"`
   - After calling, print:
     `"<func_name> returned <result>"`
   - Return the original function's result.

3. **`repeat(n)`** decorator **factory** (takes an argument)
   - Return a decorator that calls the wrapped function **n** times.
   - Return the result of the **last** call.

### Example

```python
@timer
def slow_add(a, b):
    import time; time.sleep(0.1)
    return a + b

result = slow_add(2, 3)
# prints: slow_add took 0.10xx seconds
print(result)  # 5

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return name

greet("Alice")
# prints Hello, Alice! three times
```
''',
        'difficulty': 'medium',
        'order': 2,
        'item_order': 4,
        'starter_code': (
            'import time\n'
            'from functools import wraps\n'
            '\n'
            '\n'
            'def timer(func):\n'
            '    """Decorator that prints the execution time of a function."""\n'
            '    @wraps(func)\n'
            '    def wrapper(*args, **kwargs):\n'
            '        # TODO: record start, call func, record end, print time\n'
            '        pass\n'
            '    return wrapper\n'
            '\n'
            '\n'
            'def logger(func):\n'
            '    """Decorator that logs function calls and return values."""\n'
            '    @wraps(func)\n'
            '    def wrapper(*args, **kwargs):\n'
            '        # TODO: print before call, call func, print after call\n'
            '        pass\n'
            '    return wrapper\n'
            '\n'
            '\n'
            'def repeat(n):\n'
            '    """Decorator factory that repeats a function n times."""\n'
            '    def decorator(func):\n'
            '        @wraps(func)\n'
            '        def wrapper(*args, **kwargs):\n'
            '            # TODO: call func n times, return last result\n'
            '            pass\n'
            '        return wrapper\n'
            '    return decorator\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            '@logger\n'
            'def add(a, b):\n'
            '    return a + b\n'
            '\n'
            'result = add(2, 3)\n'
            'print(result)\n'
            '\n'
            '@repeat(3)\n'
            'def greet(name):\n'
            '    print(f"Hello, {name}!")\n'
            '    return name\n'
            '\n'
            'greet("Alice")\n'
        ),
        'hints': [
            'In timer: start = time.time(), call func, end = time.time(), then print the difference.',
            'In logger: use func.__name__ to get the function name.',
            'repeat(n) returns a decorator, which returns a wrapper -- three nested functions.',
            'In repeat wrapper, use a for loop: for _ in range(n): result = func(*args, **kwargs)',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    "Calling add with args=(2, 3), kwargs={}\n"
                    "add returned 5\n"
                    "5\n"
                    "Hello, Alice!\n"
                    "Hello, Alice!\n"
                    "Hello, Alice!"
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import time

class TestDecorators(unittest.TestCase):

    def setUp(self):
        env = {}
        exec(open("student_code.py").read(), env)
        self.timer = env["timer"]
        self.logger = env["logger"]
        self.repeat = env["repeat"]

    def test_timer_returns_result(self):
        @self.timer
        def add(a, b):
            return a + b
        self.assertEqual(add(1, 2), 3)

    def test_logger_returns_result(self):
        @self.logger
        def multiply(a, b):
            return a * b
        self.assertEqual(multiply(3, 4), 12)

    def test_repeat_calls_n_times(self):
        call_count = {"n": 0}
        @self.repeat(4)
        def counter():
            call_count["n"] += 1
            return call_count["n"]
        result = counter()
        self.assertEqual(call_count["n"], 4)
        self.assertEqual(result, 4)

    def test_timer_preserves_name(self):
        @self.timer
        def my_func():
            pass
        self.assertEqual(my_func.__name__, "my_func")

    def test_logger_preserves_name(self):
        @self.logger
        def my_func():
            pass
        self.assertEqual(my_func.__name__, "my_func")

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3 – Generators
    # ------------------------------------------------------------------ #
    {
        'title': 'Generators',
        'description': '''## Generators

Learn to create generator functions using `yield` to produce values
lazily, saving memory and enabling elegant data pipelines.

### Requirements

1. **`countdown(n)`** – Yield numbers from `n` down to `1`
   (inclusive).

2. **`fibonacci(limit)`** – Yield Fibonacci numbers that are
   **less than** `limit`. Start with 0, 1, 1, 2, 3, 5, ...

3. **`chunk_list(lst, chunk_size)`** – Yield successive chunks
   (as lists) of size `chunk_size` from `lst`. The last chunk may
   be smaller.

4. **`flatten(nested)`** – Yield individual elements from a
   nested list (lists within lists, only **one** level deep).
   For example `[[1,2],[3],[4,5]]` yields `1, 2, 3, 4, 5`.

### Example

```python
print(list(countdown(5)))          # [5, 4, 3, 2, 1]
print(list(fibonacci(20)))         # [0, 1, 1, 2, 3, 5, 8, 13]
print(list(chunk_list([1,2,3,4,5], 2)))  # [[1,2], [3,4], [5]]
print(list(flatten([[1,2],[3],[4,5]])))   # [1, 2, 3, 4, 5]
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            'def countdown(n):\n'
            '    """Yield numbers from n down to 1."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def fibonacci(limit):\n'
            '    """Yield Fibonacci numbers less than limit."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def chunk_list(lst, chunk_size):\n'
            '    """Yield successive chunks of chunk_size from lst."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def flatten(nested):\n'
            '    """Yield elements from a nested list (one level deep)."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'print(list(countdown(5)))\n'
            'print(list(fibonacci(20)))\n'
            'print(list(chunk_list([1, 2, 3, 4, 5], 2)))\n'
            'print(list(flatten([[1, 2], [3], [4, 5]])))\n'
        ),
        'hints': [
            'In countdown, use a while loop: while n >= 1: yield n; n -= 1.',
            'For fibonacci, keep two variables a, b = 0, 1 and yield a while a < limit.',
            'For chunk_list, use a for loop with range(0, len(lst), chunk_size) and yield lst[i:i+chunk_size].',
            'For flatten, iterate over each sublist and yield each element: for sub in nested: for item in sub: yield item.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    '[5, 4, 3, 2, 1]\n'
                    '[0, 1, 1, 2, 3, 5, 8, 13]\n'
                    '[[1, 2], [3, 4], [5]]\n'
                    '[1, 2, 3, 4, 5]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import types

class TestGenerators(unittest.TestCase):

    def setUp(self):
        env = {}
        exec(open("student_code.py").read(), env)
        self.countdown = env["countdown"]
        self.fibonacci = env["fibonacci"]
        self.chunk_list = env["chunk_list"]
        self.flatten = env["flatten"]

    def test_countdown(self):
        self.assertEqual(list(self.countdown(5)), [5, 4, 3, 2, 1])

    def test_countdown_is_generator(self):
        self.assertIsInstance(self.countdown(3), types.GeneratorType)

    def test_fibonacci(self):
        self.assertEqual(list(self.fibonacci(20)), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_fibonacci_small(self):
        self.assertEqual(list(self.fibonacci(2)), [0, 1, 1])

    def test_chunk_list(self):
        result = list(self.chunk_list([1, 2, 3, 4, 5], 2))
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_chunk_list_exact(self):
        result = list(self.chunk_list([1, 2, 3, 4], 2))
        self.assertEqual(result, [[1, 2], [3, 4]])

    def test_flatten(self):
        result = list(self.flatten([[1, 2], [3], [4, 5]]))
        self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4 – Advanced Comprehensions & Itertools
    # ------------------------------------------------------------------ #
    {
        'title': 'Advanced Comprehensions & Itertools',
        'description': '''## Advanced Comprehensions & Itertools

Push your Python skills further with complex comprehensions and the
powerful `itertools` module.

### Requirements

1. **`matrix_transpose(matrix)`** – Given a list of lists (matrix),
   return its transpose using a **list comprehension**.
   Example: `[[1,2],[3,4],[5,6]]` -> `[[1,3,5],[2,4,6]]`.

2. **`word_lengths(sentence)`** – Return a **dictionary comprehension**
   mapping each unique word (lowercased) in the sentence to its length.
   Example: `"Hello World hello"` -> `{"hello": 5, "world": 5}`.

3. **`unique_pairs(lst)`** – Use `itertools.combinations` to return a
   list of all unique pairs `(a, b)` where `a < b` from the input list.

4. **`grouped_by_key(pairs)`** – Given a list of `(key, value)` tuples
   **sorted by key**, use `itertools.groupby` to return a dictionary
   mapping each key to a list of its values.
   Example: `[("a",1),("a",2),("b",3)]` -> `{"a":[1,2], "b":[3]}`.

5. **`running_totals(numbers)`** – Use `itertools.accumulate` to return
   a list of running totals.
   Example: `[1,2,3,4]` -> `[1,3,6,10]`.

### Example

```python
print(matrix_transpose([[1,2],[3,4],[5,6]]))
# [[1, 3, 5], [2, 4, 6]]
print(word_lengths("Hello World hello"))
# {'hello': 5, 'world': 5}
print(unique_pairs([1, 2, 3, 4]))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(grouped_by_key([("a", 1), ("a", 2), ("b", 3)]))
# {'a': [1, 2], 'b': [3]}
print(running_totals([1, 2, 3, 4]))
# [1, 3, 6, 10]
```
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 7,
        'starter_code': (
            'import itertools\n'
            '\n'
            '\n'
            'def matrix_transpose(matrix):\n'
            '    """Transpose a matrix using a list comprehension."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def word_lengths(sentence):\n'
            '    """Return dict mapping unique lowercased words to their lengths."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def unique_pairs(lst):\n'
            '    """Return all unique pairs (a, b) where a < b using itertools."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def grouped_by_key(pairs):\n'
            '    """Group sorted (key, value) pairs into a dict using itertools.groupby."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            'def running_totals(numbers):\n'
            '    """Return running totals using itertools.accumulate."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'print(matrix_transpose([[1, 2], [3, 4], [5, 6]]))\n'
            'print(word_lengths("Hello World hello"))\n'
            'print(unique_pairs([1, 2, 3, 4]))\n'
            'print(grouped_by_key([("a", 1), ("a", 2), ("b", 3)]))\n'
            'print(running_totals([1, 2, 3, 4]))\n'
        ),
        'hints': [
            'Transpose: [[row[i] for row in matrix] for i in range(len(matrix[0]))]',
            'word_lengths: {w: len(w) for w in set(sentence.lower().split())}',
            'unique_pairs: list(itertools.combinations(sorted(lst), 2))',
            'groupby: {k: [v for _, v in g] for k, g in itertools.groupby(pairs, key=lambda x: x[0])}',
            'running_totals: list(itertools.accumulate(numbers))',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    '[[1, 3, 5], [2, 4, 6]]\n'
                    "{'hello': 5, 'world': 5}\n"
                    '[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]\n'
                    "{'a': [1, 2], 'b': [3]}\n"
                    '[1, 3, 6, 10]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest

class TestAdvancedComprehensions(unittest.TestCase):

    def setUp(self):
        env = {}
        exec(open("student_code.py").read(), env)
        self.matrix_transpose = env["matrix_transpose"]
        self.word_lengths = env["word_lengths"]
        self.unique_pairs = env["unique_pairs"]
        self.grouped_by_key = env["grouped_by_key"]
        self.running_totals = env["running_totals"]

    def test_transpose(self):
        result = self.matrix_transpose([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(result, [[1, 3, 5], [2, 4, 6]])

    def test_transpose_square(self):
        result = self.matrix_transpose([[1, 2], [3, 4]])
        self.assertEqual(result, [[1, 3], [2, 4]])

    def test_word_lengths(self):
        result = self.word_lengths("Hello World hello")
        self.assertEqual(result, {"hello": 5, "world": 5})

    def test_unique_pairs(self):
        result = self.unique_pairs([1, 2, 3, 4])
        self.assertEqual(result, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

    def test_grouped_by_key(self):
        result = self.grouped_by_key([("a", 1), ("a", 2), ("b", 3)])
        self.assertEqual(result, {"a": [1, 2], "b": [3]})

    def test_running_totals(self):
        result = self.running_totals([1, 2, 3, 4])
        self.assertEqual(result, [1, 3, 6, 10])

    def test_running_totals_single(self):
        result = self.running_totals([5])
        self.assertEqual(result, [5])

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 5 – Putting It All Together (Capstone)
    # ------------------------------------------------------------------ #
    {
        'title': 'Putting It All Together',
        'description': '''## Putting It All Together -- Mini Data Pipeline

This capstone assignment combines classes, generators, decorators,
and functional tools into a small data-processing pipeline.

### Scenario

You are processing student exam records. Each record is a dictionary:
```python
{"name": "Alice", "subject": "Math", "score": 85}
```

### Requirements

1. **`@validate_data` decorator** – Wraps a generator function.
   Before yielding each record, check that it has the keys `"name"`,
   `"subject"`, and `"score"`. Skip (do not yield) any record that is
   missing a key or where `score` is not an `int` or `float`.

2. **`class StudentRecord`**
   - `__init__(self, name, subject, score)`
   - `grade` property: returns `"A"` if score >= 90, `"B"` if >= 80,
     `"C"` if >= 70, `"D"` if >= 60, else `"F"`.
   - `__str__` returns `"<name> - <subject>: <score> (<grade>)"`.

3. **`read_records(data)` generator** (decorated with `@validate_data`)
   - Accepts a list of dicts, yields `StudentRecord` objects.

4. **`process_pipeline(data)`** function:
   - Use `read_records` to get `StudentRecord` objects.
   - Use `filter` to keep only passing records (grade != `"F"`).
   - Use `map` to get the string representation of each record.
   - Return the resulting **list of strings**.

### Example

```python
data = [
    {"name": "Alice", "subject": "Math", "score": 85},
    {"name": "Bob", "subject": "Math", "score": 55},
    {"name": "Carol", "subject": "Math", "score": 92},
    {"name": "Invalid"},
]
for line in process_pipeline(data):
    print(line)
# Alice - Math: 85 (B)
# Carol - Math: 92 (A)
```
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 8,
        'starter_code': (
            'from functools import wraps\n'
            '\n'
            '\n'
            'def validate_data(gen_func):\n'
            '    """Decorator for generators: skip records missing required keys\n'
            '    or with non-numeric scores."""\n'
            '    @wraps(gen_func)\n'
            '    def wrapper(data):\n'
            '        # TODO: iterate, validate, yield valid records\n'
            '        pass\n'
            '    return wrapper\n'
            '\n'
            '\n'
            'class StudentRecord:\n'
            '    """Represents a single student exam record."""\n'
            '\n'
            '    def __init__(self, name, subject, score):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    @property\n'
            '    def grade(self):\n'
            '        # TODO: return letter grade\n'
            '        pass\n'
            '\n'
            '    def __str__(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '\n'
            '@validate_data\n'
            'def read_records(data):\n'
            '    """Generator that yields StudentRecord objects from dicts."""\n'
            '    for record in data:\n'
            '        yield StudentRecord(record["name"], record["subject"], record["score"])\n'
            '\n'
            '\n'
            'def process_pipeline(data):\n'
            '    """Full pipeline: read -> filter passing -> map to strings."""\n'
            '    # TODO\n'
            '    pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'data = [\n'
            '    {"name": "Alice", "subject": "Math", "score": 85},\n'
            '    {"name": "Bob", "subject": "Math", "score": 55},\n'
            '    {"name": "Carol", "subject": "Math", "score": 92},\n'
            '    {"name": "Invalid"},\n'
            ']\n'
            'for line in process_pipeline(data):\n'
            '    print(line)\n'
        ),
        'hints': [
            'In validate_data wrapper, iterate over data and check each dict for required keys before calling the original generator.',
            'Use all(k in record for k in ("name", "subject", "score")) to check keys.',
            'Check isinstance(record["score"], (int, float)) for numeric score.',
            'In process_pipeline: records = read_records(data), then filter and map.',
            'Filter: filter(lambda r: r.grade != "F", records). Map: map(str, ...).',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': 'Alice - Math: 85 (B)\nCarol - Math: 92 (A)',
            },
        ],
        'test_cases_code': '''
import unittest

class TestDataPipeline(unittest.TestCase):

    def setUp(self):
        env = {}
        exec(open("student_code.py").read(), env)
        self.StudentRecord = env["StudentRecord"]
        self.read_records = env["read_records"]
        self.process_pipeline = env["process_pipeline"]

    def test_student_record_grade_a(self):
        r = self.StudentRecord("X", "Y", 95)
        self.assertEqual(r.grade, "A")

    def test_student_record_grade_b(self):
        r = self.StudentRecord("X", "Y", 85)
        self.assertEqual(r.grade, "B")

    def test_student_record_grade_f(self):
        r = self.StudentRecord("X", "Y", 50)
        self.assertEqual(r.grade, "F")

    def test_student_record_str(self):
        r = self.StudentRecord("Alice", "Math", 85)
        self.assertEqual(str(r), "Alice - Math: 85 (B)")

    def test_pipeline_filters_failing(self):
        data = [
            {"name": "A", "subject": "S", "score": 85},
            {"name": "B", "subject": "S", "score": 40},
        ]
        result = self.process_pipeline(data)
        self.assertEqual(len(result), 1)
        self.assertIn("A - S: 85 (B)", result)

    def test_pipeline_skips_invalid(self):
        data = [
            {"name": "A", "subject": "S", "score": 90},
            {"name": "Bad"},
            {"name": "C", "subject": "S", "score": "not_a_number"},
        ]
        result = self.process_pipeline(data)
        self.assertEqual(len(result), 1)
        self.assertIn("A - S: 90 (A)", result)

    def test_read_records_yields_student_records(self):
        data = [{"name": "A", "subject": "S", "score": 70}]
        records = list(self.read_records(data))
        self.assertEqual(len(records), 1)
        self.assertIsInstance(records[0], self.StudentRecord)

if __name__ == "__main__":
    unittest.main()
''',
    },
]
