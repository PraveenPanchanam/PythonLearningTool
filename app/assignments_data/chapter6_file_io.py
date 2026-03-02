CHAPTER_INFO = {
    'title': 'File I/O & Error Handling',
    'description': (
        'Learn to read from and write to files, handle errors gracefully with '
        'try/except/finally blocks, create custom exception classes, and use '
        'context managers (the with statement). These skills are essential for '
        'building robust programs that interact with the file system and handle '
        'unexpected situations.'
    ),
    'difficulty_level': 'intermediate',
    'order': 6,
    'learning_objectives': [
        'Read text files line by line and process their contents',
        'Write data to files using the open() function and with statement',
        'Handle exceptions using try, except, else, and finally blocks',
        'Catch specific exception types for targeted error handling',
        'Create custom exception classes by inheriting from Exception',
        'Use context managers (with statement) for safe resource management',
        'Parse and process CSV-like data from files',
        'Build validation systems with meaningful error messages',
    ],
    'estimated_time_minutes': 55,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------
    # Assignment 1: Read and Process File
    # ------------------------------------------------------------------
    {
        'title': 'Read and Process File',
        'description': '''## Read and Process File

Write a program that reads the contents of a text file and reports basic statistics.

### Requirements

1. Read the filename from standard input (first line).
2. Open and read the file.
3. Print the following statistics:
   - `Lines: <number of lines>`
   - `Words: <total number of words>`
   - `Characters: <total number of characters including spaces and newlines>`

A **word** is defined as any whitespace-separated token (use `split()`).
**Characters** means the total length of the file content (including newline characters).

### Example

If the file `sample.txt` contains:
```
Hello World
Python is great
```

**Input:**
```
sample.txt
```

**Output:**
```
Lines: 2
Words: 5
Characters: 28
```

### Notes
- Use the `with` statement to open files.
- The file will exist in the working directory.
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'allow_file_io': True,
        'starter_code': (
            '# Read the filename from input\n'
            'filename = input().strip()\n\n'
            '# TODO: Open the file using a with statement\n'
            '# TODO: Count lines, words, and characters\n\n'
            '# TODO: Print the results\n'
        ),
        'hints': [
            'Use with open(filename, "r") as f: to safely open the file.',
            'Read the entire content with f.read(). Then use len(content) for characters.',
            'Split content by newlines (content.split("\\n") or content.splitlines()) for lines.',
            'Use content.split() (no arguments) to split by any whitespace for word count.',
            'Be careful: an empty trailing newline can affect line count. Use splitlines() for accuracy.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': 'sample.txt\n',
                'expected_output': (
                    'Lines: 2\n'
                    'Words: 5\n'
                    'Characters: 28'
                ),
            },
            {
                'input': 'single.txt\n',
                'expected_output': (
                    'Lines: 1\n'
                    'Words: 3\n'
                    'Characters: 11'
                ),
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data, files=None):
    cwd = os.path.dirname(__file__)
    if files:
        for fname, content in files.items():
            with open(os.path.join(cwd, fname), "w") as f:
                f.write(content)
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(cwd, 'student_code.py')],
            input=input_data, capture_output=True, text=True, timeout=10,
            cwd=cwd,
        )
        return result.stdout.strip()
    finally:
        if files:
            for fname in files:
                path = os.path.join(cwd, fname)
                if os.path.exists(path):
                    os.remove(path)

class TestReadFile:
    def test_basic_file(self):
        out = run_student("sample.txt\\n", {"sample.txt": "Hello World\\nPython is great\\n"})
        assert "Lines: 2" in out
        assert "Words: 5" in out
        assert "Characters: 28" in out

    def test_single_line(self):
        out = run_student("single.txt\\n", {"single.txt": "Hello World!"})
        assert "Lines: 1" in out
        assert "Words: 2" in out

    def test_empty_file(self):
        out = run_student("empty.txt\\n", {"empty.txt": ""})
        assert "Lines: 0" in out or "Lines: 1" in out
        assert "Words: 0" in out
        assert "Characters: 0" in out

    def test_multiline(self):
        content = "line one\\nline two\\nline three\\n"
        out = run_student("multi.txt\\n", {"multi.txt": content})
        assert "Lines: 3" in out
        assert "Words: 6" in out
''',
    },
    # ------------------------------------------------------------------
    # Assignment 2: Exception Handling
    # ------------------------------------------------------------------
    {
        'title': 'Exception Handling',
        'description': '''## Exception Handling

Write a program that performs **safe division** and **safe type conversion** using try/except blocks.

### Requirements

Your program should read commands from standard input, one per line, until it reads `done`.

Each command is one of:
- `divide <a> <b>` -- Divide a by b (both are numbers, may be int or float).
- `convert <value> <type>` -- Convert value to the given type (`int` or `float`).

For each command, print the result or an error message:

- **divide**: Print `Result: <value>` (use default Python float formatting). If `b` is zero, print `Error: Division by zero`.
- **convert**: Print `Converted: <value>`. If conversion fails, print `Error: Cannot convert '<value>' to <type>`.

### Example

**Input:**
```
divide 10 3
divide 5 0
convert 42 int
convert hello int
convert 3.14 float
done
```

**Output:**
```
Result: 3.3333333333333335
Error: Division by zero
Converted: 42
Error: Cannot convert 'hello' to int
Converted: 3.14
```
''',
        'difficulty': 'medium',
        'order': 2,
        'item_order': 3,
        'starter_code': (
            '# Process commands until "done"\n'
            'while True:\n'
            '    line = input().strip()\n'
            '    if line == "done":\n'
            '        break\n\n'
            '    parts = line.split()\n'
            '    command = parts[0]\n\n'
            '    if command == "divide":\n'
            '        a = float(parts[1])\n'
            '        b = float(parts[2])\n'
            '        # TODO: Try dividing a by b, handle ZeroDivisionError\n'
            '        pass\n\n'
            '    elif command == "convert":\n'
            '        value = parts[1]\n'
            '        target_type = parts[2]\n'
            '        # TODO: Try converting value to target_type, handle ValueError\n'
            '        pass\n'
        ),
        'hints': [
            'Wrap the division in a try/except ZeroDivisionError block.',
            'For convert, use int() or float() based on target_type. Catch ValueError.',
            'Use an if/elif to choose between int() and float() based on the target_type string.',
            'Remember to format the error message exactly: Error: Cannot convert \'<value>\' to <type>',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': 'divide 10 3\ndivide 5 0\nconvert 42 int\nconvert hello int\nconvert 3.14 float\ndone\n',
                'expected_output': (
                    'Result: 3.3333333333333335\n'
                    'Error: Division by zero\n'
                    'Converted: 42\n'
                    "Error: Cannot convert 'hello' to int\n"
                    'Converted: 3.14'
                ),
            },
            {
                'input': 'divide 100 4\nconvert 99.9 int\ndone\n',
                'expected_output': (
                    'Result: 25.0\n'
                    "Error: Cannot convert '99.9' to int"
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

class TestExceptionHandling:
    def test_normal_division(self):
        out = run_student("divide 10 2\\ndone\\n")
        assert "Result: 5.0" in out

    def test_division_by_zero(self):
        out = run_student("divide 5 0\\ndone\\n")
        assert "Error: Division by zero" in out

    def test_valid_conversion(self):
        out = run_student("convert 42 int\\ndone\\n")
        assert "Converted: 42" in out

    def test_invalid_conversion(self):
        out = run_student("convert hello int\\ndone\\n")
        assert "Error: Cannot convert 'hello' to int" in out

    def test_float_to_int_fails(self):
        out = run_student("convert 3.14 int\\ndone\\n")
        assert "Error: Cannot convert '3.14' to int" in out

    def test_valid_float_conversion(self):
        out = run_student("convert 3.14 float\\ndone\\n")
        assert "Converted: 3.14" in out
''',
    },
    # ------------------------------------------------------------------
    # Assignment 3: File Word Frequency
    # ------------------------------------------------------------------
    {
        'title': 'File Word Frequency',
        'description': '''## File Word Frequency

Write a program that reads a text file and outputs the frequency of each word, sorted alphabetically.

### Requirements

1. Read the filename from standard input.
2. Open and read the file.
3. Convert all text to **lowercase**.
4. Remove basic punctuation: strip `.,!?;:"'()` from each word.
5. Count the frequency of each word.
6. Print each word and its frequency in **alphabetical order**, one per line:
   ```
   <word>: <count>
   ```

### Example

If the file `story.txt` contains:
```
The cat sat on the mat.
The cat was happy, very happy!
```

**Input:**
```
story.txt
```

**Output:**
```
cat: 2
happy: 2
mat: 1
on: 1
sat: 1
the: 3
very: 1
was: 1
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'allow_file_io': True,
        'starter_code': (
            'import string\n\n'
            '# Read filename from input\n'
            'filename = input().strip()\n\n'
            '# TODO: Open and read the file\n\n'
            '# TODO: Convert to lowercase and split into words\n\n'
            '# TODO: Strip punctuation from each word\n'
            '# Hint: use word.strip(string.punctuation) or similar\n\n'
            '# TODO: Count word frequencies using a dictionary\n\n'
            '# TODO: Print in alphabetical order\n'
        ),
        'hints': [
            'Use with open(filename) as f: content = f.read()',
            'Convert to lowercase with .lower(), then split() to get words.',
            "Strip punctuation from each word using string.punctuation or a manual strip call.",
            'Skip empty strings after stripping punctuation.',
            'Sort the dictionary keys with sorted() before printing.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': 'story.txt\n',
                'expected_output': (
                    'cat: 2\n'
                    'happy: 2\n'
                    'mat: 1\n'
                    'on: 1\n'
                    'sat: 1\n'
                    'the: 3\n'
                    'very: 1\n'
                    'was: 1'
                ),
            },
            {
                'input': 'simple.txt\n',
                'expected_output': (
                    'hello: 2\n'
                    'world: 1'
                ),
            },
        ],
        'test_cases_code': '''
import subprocess, os, sys

def run_student(input_data, files=None):
    cwd = os.path.dirname(__file__)
    if files:
        for fname, content in files.items():
            with open(os.path.join(cwd, fname), "w") as f:
                f.write(content)
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(cwd, 'student_code.py')],
            input=input_data, capture_output=True, text=True, timeout=10,
            cwd=cwd,
        )
        return result.stdout.strip()
    finally:
        if files:
            for fname in files:
                path = os.path.join(cwd, fname)
                if os.path.exists(path):
                    os.remove(path)

class TestFileWordFrequency:
    def test_basic_story(self):
        content = "The cat sat on the mat.\\nThe cat was happy, very happy!\\n"
        out = run_student("story.txt\\n", {"story.txt": content})
        assert "cat: 2" in out
        assert "the: 3" in out
        assert "happy: 2" in out

    def test_alphabetical_order(self):
        content = "banana apple cherry apple\\n"
        out = run_student("fruits.txt\\n", {"fruits.txt": content})
        lines = out.strip().split("\\n")
        words = [line.split(":")[0] for line in lines]
        assert words == sorted(words)

    def test_punctuation_removal(self):
        content = "Hello! Hello? Hello.\\n"
        out = run_student("punct.txt\\n", {"punct.txt": content})
        assert "hello: 3" in out

    def test_case_insensitive(self):
        content = "Python PYTHON python\\n"
        out = run_student("case.txt\\n", {"case.txt": content})
        assert "python: 3" in out

    def test_simple(self):
        content = "hello world hello\\n"
        out = run_student("simple.txt\\n", {"simple.txt": content})
        assert "hello: 2" in out
        assert "world: 1" in out
''',
    },
    # ------------------------------------------------------------------
    # Assignment 4: Custom Exception Classes
    # ------------------------------------------------------------------
    {
        'title': 'Custom Exception Classes',
        'description': '''## Custom Exception Classes

Create a validation system using custom exception classes.

### Requirements

Define the following custom exceptions (all should inherit from a base `ValidationError` which inherits from `Exception`):

- `ValidationError(Exception)` -- base class with a `message` attribute.
- `AgeError(ValidationError)` -- raised when age is invalid.
- `EmailError(ValidationError)` -- raised when email is invalid.
- `PasswordError(ValidationError)` -- raised when password is invalid.

Write three validation functions:

1. **`validate_age(age_str)`**: Convert to int. Raise `AgeError` if:
   - Not a valid integer: message `"Invalid age: not a number"`
   - Less than 0 or greater than 150: message `"Invalid age: out of range (0-150)"`

2. **`validate_email(email)`**: Raise `EmailError` if:
   - Does not contain exactly one `@`: message `"Invalid email: must contain exactly one @"`
   - The part after `@` does not contain a `.`: message `"Invalid email: domain must contain a dot"`

3. **`validate_password(password)`**: Raise `PasswordError` if:
   - Length is less than 8: message `"Invalid password: must be at least 8 characters"`
   - Does not contain at least one digit: message `"Invalid password: must contain a digit"`

### Main Program

Read commands from stdin until `done`:
- `age <value>` -- validate the age
- `email <value>` -- validate the email
- `password <value>` -- validate the password

For each command, print either `Valid` or `Error: <exception_message>`.

### Example

**Input:**
```
age 25
age -5
email user@example.com
email userexample.com
password Secure123
password short
done
```

**Output:**
```
Valid
Error: Invalid age: out of range (0-150)
Valid
Error: Invalid email: must contain exactly one @
Valid
Error: Invalid password: must be at least 8 characters
```
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 6,
        'starter_code': (
            '# Define custom exception classes\n'
            'class ValidationError(Exception):\n'
            '    def __init__(self, message):\n'
            '        self.message = message\n'
            '        super().__init__(self.message)\n\n'
            '# TODO: Define AgeError, EmailError, PasswordError inheriting from ValidationError\n\n\n'
            '# Validation functions\n'
            'def validate_age(age_str):\n'
            '    # TODO: Implement age validation\n'
            '    pass\n\n'
            'def validate_email(email):\n'
            '    # TODO: Implement email validation\n'
            '    pass\n\n'
            'def validate_password(password):\n'
            '    # TODO: Implement password validation\n'
            '    pass\n\n\n'
            '# Main loop\n'
            'while True:\n'
            '    line = input().strip()\n'
            '    if line == "done":\n'
            '        break\n'
            '    parts = line.split(maxsplit=1)\n'
            '    command = parts[0]\n'
            '    value = parts[1] if len(parts) > 1 else ""\n\n'
            '    try:\n'
            '        if command == "age":\n'
            '            validate_age(value)\n'
            '        elif command == "email":\n'
            '            validate_email(value)\n'
            '        elif command == "password":\n'
            '            validate_password(value)\n'
            '        print("Valid")\n'
            '    except ValidationError as e:\n'
            '        print(f"Error: {e.message}")\n'
        ),
        'hints': [
            'Each custom exception should call super().__init__(message) and store self.message = message.',
            'In validate_age, use try/except ValueError to catch non-integer input.',
            'For email validation, use email.count("@") to check for exactly one @. Then split on @ and check if "." is in the domain part.',
            'For password validation, use len(password) and any(c.isdigit() for c in password).',
            'Raise the exception as soon as a validation rule fails; check rules in the order listed.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': (
                    'age 25\n'
                    'age -5\n'
                    'email user@example.com\n'
                    'email userexample.com\n'
                    'password Secure123\n'
                    'password short\n'
                    'done\n'
                ),
                'expected_output': (
                    'Valid\n'
                    'Error: Invalid age: out of range (0-150)\n'
                    'Valid\n'
                    'Error: Invalid email: must contain exactly one @\n'
                    'Valid\n'
                    'Error: Invalid password: must be at least 8 characters'
                ),
            },
            {
                'input': (
                    'age abc\n'
                    'email a@b\n'
                    'password 12345678\n'
                    'done\n'
                ),
                'expected_output': (
                    'Error: Invalid age: not a number\n'
                    'Error: Invalid email: domain must contain a dot\n'
                    'Valid'
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

class TestCustomExceptions:
    def test_valid_age(self):
        out = run_student("age 25\\ndone\\n")
        assert out.strip() == "Valid"

    def test_negative_age(self):
        out = run_student("age -5\\ndone\\n")
        assert "Error: Invalid age: out of range (0-150)" in out

    def test_non_numeric_age(self):
        out = run_student("age abc\\ndone\\n")
        assert "Error: Invalid age: not a number" in out

    def test_valid_email(self):
        out = run_student("email user@example.com\\ndone\\n")
        assert out.strip() == "Valid"

    def test_email_no_at(self):
        out = run_student("email userexample.com\\ndone\\n")
        assert "Error: Invalid email: must contain exactly one @" in out

    def test_email_no_dot_in_domain(self):
        out = run_student("email user@localhost\\ndone\\n")
        assert "Error: Invalid email: domain must contain a dot" in out

    def test_valid_password(self):
        out = run_student("password Secure123\\ndone\\n")
        assert out.strip() == "Valid"

    def test_short_password(self):
        out = run_student("password short\\ndone\\n")
        assert "Error: Invalid password: must be at least 8 characters" in out

    def test_password_no_digit(self):
        out = run_student("password abcdefgh\\ndone\\n")
        assert "Error: Invalid password: must contain a digit" in out
''',
    },
]
