CHAPTER_INFO = {
    'title': 'NumPy Fundamentals',
    'description': (
        'Learn the fundamentals of NumPy, Python\'s powerful library for '
        'numerical computing. This chapter covers array creation, indexing, '
        'slicing, reshaping, mathematical operations, broadcasting, '
        'aggregation functions, and basic linear algebra.'
    ),
    'difficulty_level': 'advanced',
    'order': 9,
    'learning_objectives': [
        'Create NumPy arrays using various methods (lists, arange, linspace, zeros, ones)',
        'Perform element-wise arithmetic operations on arrays',
        'Use indexing, slicing, and boolean indexing on 1D and 2D arrays',
        'Reshape, transpose, flatten, stack, and split arrays',
        'Compute statistical aggregations (mean, median, std, var) along axes',
        'Use np.percentile and np.corrcoef for advanced statistics',
        'Perform linear algebra operations: matrix multiplication, determinant, inverse, eigenvalues',
        'Solve systems of linear equations with np.linalg.solve',
    ],
    'estimated_time_minutes': 65,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1 -- Array Creation & Basic Operations
    # ------------------------------------------------------------------ #
    {
        'title': 'Array Creation & Basic Operations',
        'description': '''## Array Creation & Basic Operations

Learn to create NumPy arrays using different methods and perform
basic element-wise operations on them.

### Requirements

Write a program that:

1. **Reads** a line of space-separated integers from stdin.
2. **Creates** a NumPy array from those integers.
3. **Prints** the following information, each on its own line:
   - `Array: <array>` -- the array printed with `np.array2string`
     using default formatting.
   - `Shape: <shape>` -- the shape tuple.
   - `Dtype: <dtype>` -- the data type.
   - `Sum: <sum>` -- the sum of all elements.
   - `Mean: <mean>` -- the mean rounded to 2 decimal places.
4. **Creates** these additional arrays and prints them:
   - `Arange: <array>` -- `np.arange(1, 6)` (i.e. `[1 2 3 4 5]`).
   - `Linspace: <array>` -- `np.linspace(0, 1, 5)` with values rounded
     to 2 decimal places.
   - `Zeros: <array>` -- `np.zeros(3, dtype=int)`.
   - `Ones: <array>` -- `np.ones(3, dtype=int)`.
5. **Performs** element-wise operations on the original array and
   prints:
   - `Add 10: <array>` -- every element plus 10.
   - `Multiply 2: <array>` -- every element times 2.
   - `Squared: <array>` -- every element squared.

### Example

**Input:**
```
1 2 3 4 5
```

**Output:**
```
Array: [1 2 3 4 5]
Shape: (5,)
Dtype: int64
Sum: 15
Mean: 3.0
Arange: [1 2 3 4 5]
Linspace: [0.   0.25 0.5  0.75 1.  ]
Zeros: [0 0 0]
Ones: [1 1 1]
Add 10: [11 12 13 14 15]
Multiply 2: [ 2  4  6  8 10]
Squared: [ 1  4  9 16 25]
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            'import numpy as np\n'
            '\n'
            '# TODO: Read space-separated integers from stdin\n'
            'numbers = input().split()\n'
            '\n'
            '# TODO: Create a NumPy array from the input\n'
            '\n'
            '# TODO: Print Array, Shape, Dtype, Sum, Mean\n'
            '\n'
            '# TODO: Create and print arrays using arange, linspace, zeros, ones\n'
            '\n'
            '# TODO: Perform and print element-wise operations (add 10, multiply 2, squared)\n'
        ),
        'hints': [
            'Use np.array([int(x) for x in numbers]) to create the array from input.',
            'Use arr.shape, arr.dtype, arr.sum(), and round(arr.mean(), 2) for array info.',
            'np.linspace(0, 1, 5) creates 5 evenly spaced values from 0 to 1.',
            'Element-wise operations: arr + 10, arr * 2, arr ** 2.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '1 2 3 4 5',
                'expected_output': (
                    'Array: [1 2 3 4 5]\n'
                    'Shape: (5,)\n'
                    'Dtype: int64\n'
                    'Sum: 15\n'
                    'Mean: 3.0\n'
                    'Arange: [1 2 3 4 5]\n'
                    'Linspace: [0.   0.25 0.5  0.75 1.  ]\n'
                    'Zeros: [0 0 0]\n'
                    'Ones: [1 1 1]\n'
                    'Add 10: [11 12 13 14 15]\n'
                    'Multiply 2: [ 2  4  6  8 10]\n'
                    'Squared: [ 1  4  9 16 25]'
                ),
            },
            {
                'input': '10 20 30',
                'expected_output': (
                    'Array: [10 20 30]\n'
                    'Shape: (3,)\n'
                    'Dtype: int64\n'
                    'Sum: 60\n'
                    'Mean: 20.0\n'
                    'Arange: [1 2 3 4 5]\n'
                    'Linspace: [0.   0.25 0.5  0.75 1.  ]\n'
                    'Zeros: [0 0 0]\n'
                    'Ones: [1 1 1]\n'
                    'Add 10: [20 30 40]\n'
                    'Multiply 2: [20 40 60]\n'
                    'Squared: [100 400 900]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch
import numpy as np

class TestArrayCreation(unittest.TestCase):

    def run_student_code(self, input_str):
        """Run the student code with the given input and capture stdout."""
        captured = io.StringIO()
        with patch("sys.stdin", io.StringIO(input_str)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open("student_code.py").read(), {"__builtins__": __builtins__})
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_array_creation_basic(self):
        output = self.run_student_code("1 2 3 4 5")
        self.assertIn("Array: [1 2 3 4 5]", output)

    def test_shape_output(self):
        output = self.run_student_code("1 2 3 4 5")
        self.assertIn("Shape: (5,)", output)

    def test_dtype_output(self):
        output = self.run_student_code("1 2 3 4 5")
        self.assertIn("Dtype: int64", output)

    def test_sum_and_mean(self):
        output = self.run_student_code("1 2 3 4 5")
        self.assertIn("Sum: 15", output)
        self.assertIn("Mean: 3.0", output)

    def test_element_wise_operations(self):
        output = self.run_student_code("1 2 3 4 5")
        self.assertIn("Add 10: [11 12 13 14 15]", output)
        self.assertIn("Multiply 2: [ 2  4  6  8 10]", output)
        self.assertIn("Squared: [ 1  4  9 16 25]", output)

    def test_utility_arrays(self):
        output = self.run_student_code("1 2 3")
        self.assertIn("Arange: [1 2 3 4 5]", output)
        self.assertIn("Zeros: [0 0 0]", output)
        self.assertIn("Ones: [1 1 1]", output)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2 -- Array Indexing & Slicing
    # ------------------------------------------------------------------ #
    {
        'title': 'Array Indexing & Slicing',
        'description': '''## Array Indexing & Slicing

Master NumPy array indexing, slicing, and boolean indexing to
efficiently access and filter data.

### Requirements

Write a program that:

1. **Reads** the first line: comma-separated integers (the data).
2. **Reads** the second line: a single integer (the threshold).
3. **Creates** a 1D NumPy array from the data.
4. **Prints** the following:
   - `Array: <array>`
   - `First: <value>` -- the first element.
   - `Last: <value>` -- the last element.
   - `Slice [1:4]: <array>` -- elements at index 1, 2, 3.
   - `Reversed: <array>` -- the array in reverse order.
5. **Reshapes** the array into a 2D array with 2 rows (only if the
   length is even; otherwise skip reshape lines and print
   `Reshape: skipped (odd length)`).  When reshaped, print:
   - `Reshaped:\\n<2d_array>` -- the 2D array.
   - `Row 0: <array>` -- the first row.
   - `Col 0: <array>` -- the first column.
6. **Boolean indexing**: print elements greater than the threshold:
   - `Above <threshold>: <array>`

### Example

**Input:**
```
2,7,1,8,3,6
4
```

**Output:**
```
Array: [2 7 1 8 3 6]
First: 2
Last: 6
Slice [1:4]: [7 1 8]
Reversed: [6 3 8 1 7 2]
Reshaped:
[[2 7 1]
 [8 3 6]]
Row 0: [2 7 1]
Col 0: [2 8]
Above 4: [7 8 6]
```
''',
        'difficulty': 'easy',
        'order': 2,
        'item_order': 3,
        'starter_code': (
            'import numpy as np\n'
            '\n'
            '# TODO: Read comma-separated integers from stdin\n'
            'data_line = input()\n'
            'threshold = int(input())\n'
            '\n'
            '# TODO: Create a NumPy array from the comma-separated data\n'
            '\n'
            '# TODO: Print Array, First, Last, Slice [1:4], Reversed\n'
            '\n'
            '# TODO: Reshape into 2 rows if length is even, print Reshaped, Row 0, Col 0\n'
            '#       Otherwise print "Reshape: skipped (odd length)"\n'
            '\n'
            '# TODO: Boolean indexing -- print elements above the threshold\n'
        ),
        'hints': [
            'Parse input: np.array([int(x) for x in data_line.split(",")])',
            'Use arr[0] for first, arr[-1] for last, arr[1:4] for slice, arr[::-1] for reversed.',
            'Reshape: arr.reshape(2, -1) gives 2 rows with auto-calculated columns.',
            'Boolean indexing: arr[arr > threshold] returns elements above the threshold.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '2,7,1,8,3,6\n4',
                'expected_output': (
                    'Array: [2 7 1 8 3 6]\n'
                    'First: 2\n'
                    'Last: 6\n'
                    'Slice [1:4]: [7 1 8]\n'
                    'Reversed: [6 3 8 1 7 2]\n'
                    'Reshaped:\n'
                    '[[2 7 1]\n'
                    ' [8 3 6]]\n'
                    'Row 0: [2 7 1]\n'
                    'Col 0: [2 8]\n'
                    'Above 4: [7 8 6]'
                ),
            },
            {
                'input': '5,10,15,20,25\n12',
                'expected_output': (
                    'Array: [ 5 10 15 20 25]\n'
                    'First: 5\n'
                    'Last: 25\n'
                    'Slice [1:4]: [10 15 20]\n'
                    'Reversed: [25 20 15 10  5]\n'
                    'Reshape: skipped (odd length)\n'
                    'Above 12: [15 20 25]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch
import numpy as np

class TestArrayIndexing(unittest.TestCase):

    def run_student_code(self, input_str):
        captured = io.StringIO()
        with patch("sys.stdin", io.StringIO(input_str)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open("student_code.py").read(), {"__builtins__": __builtins__})
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_basic_output(self):
        output = self.run_student_code("2,7,1,8,3,6\\n4")
        self.assertIn("Array: [2 7 1 8 3 6]", output)
        self.assertIn("First: 2", output)
        self.assertIn("Last: 6", output)

    def test_slicing(self):
        output = self.run_student_code("2,7,1,8,3,6\\n4")
        self.assertIn("Slice [1:4]: [7 1 8]", output)
        self.assertIn("Reversed: [6 3 8 1 7 2]", output)

    def test_reshape_even(self):
        output = self.run_student_code("2,7,1,8,3,6\\n4")
        self.assertIn("Row 0: [2 7 1]", output)
        self.assertIn("Col 0: [2 8]", output)

    def test_reshape_odd_skipped(self):
        output = self.run_student_code("5,10,15,20,25\\n12")
        self.assertIn("Reshape: skipped (odd length)", output)

    def test_boolean_indexing(self):
        output = self.run_student_code("2,7,1,8,3,6\\n4")
        self.assertIn("Above 4: [7 8 6]", output)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3 -- Array Reshaping & Manipulation
    # ------------------------------------------------------------------ #
    {
        'title': 'Array Reshaping & Manipulation',
        'description': '''## Array Reshaping & Manipulation

Learn to reshape, transpose, flatten, stack, and split NumPy arrays
to transform data into the structure you need.

### Requirements

Write a program that:

1. **Reads** the first line: space-separated integers (the data).
2. **Reads** the second line: two integers `rows cols` (target shape).
3. **Creates** a 1D NumPy array from the data.
4. **Reshapes** it to the given shape and prints:
   - `Original: <1d_array>`
   - `Reshaped (<rows>x<cols>):\\n<2d_array>`
5. **Prints** transformations of the reshaped array:
   - `Transposed:\\n<array>` -- the transpose.
   - `Flattened: <array>` -- flattened back to 1D.
6. **Stacks** the first and last row:
   - `VStack:\\n<array>` -- vertically stacked (2 rows).
   - `HStack: <array>` -- horizontally stacked (1 row).
7. **Splits** the reshaped array into individual rows:
   - `Split: [<row1_as_1d>, <row2_as_1d>, ...]`
     Print each row separated by `", "`, each row shown as a 1D array
     string.

### Example

**Input:**
```
1 2 3 4 5 6
2 3
```

**Output:**
```
Original: [1 2 3 4 5 6]
Reshaped (2x3):
[[1 2 3]
 [4 5 6]]
Transposed:
[[1 4]
 [2 5]
 [3 6]]
Flattened: [1 2 3 4 5 6]
VStack:
[[1 2 3]
 [4 5 6]]
HStack: [1 2 3 4 5 6]
Split: [array([1, 2, 3]), array([4, 5, 6])]
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            'import numpy as np\n'
            '\n'
            '# TODO: Read space-separated integers (data) from first line\n'
            'data_line = input()\n'
            '# TODO: Read rows and cols from second line\n'
            'shape_line = input()\n'
            '\n'
            '# TODO: Create 1D array and print Original\n'
            '\n'
            '# TODO: Reshape to (rows, cols) and print Reshaped\n'
            '\n'
            '# TODO: Print Transposed, Flattened\n'
            '\n'
            '# TODO: Stack first and last row (VStack, HStack)\n'
            '\n'
            '# TODO: Split the reshaped array into rows and print Split\n'
        ),
        'hints': [
            'Use arr.reshape(rows, cols) to reshape the 1D array.',
            'Use reshaped.T for transpose and reshaped.flatten() for flattening.',
            'np.vstack([first_row, last_row]) and np.hstack([first_row, last_row]) for stacking.',
            'np.split(reshaped, rows) splits into a list of sub-arrays along axis 0.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '1 2 3 4 5 6\n2 3',
                'expected_output': (
                    'Original: [1 2 3 4 5 6]\n'
                    'Reshaped (2x3):\n'
                    '[[1 2 3]\n'
                    ' [4 5 6]]\n'
                    'Transposed:\n'
                    '[[1 4]\n'
                    ' [2 5]\n'
                    ' [3 6]]\n'
                    'Flattened: [1 2 3 4 5 6]\n'
                    'VStack:\n'
                    '[[1 2 3]\n'
                    ' [4 5 6]]\n'
                    'HStack: [1 2 3 4 5 6]\n'
                    'Split: [array([1, 2, 3]), array([4, 5, 6])]'
                ),
            },
            {
                'input': '1 2 3 4 5 6 7 8 9\n3 3',
                'expected_output': (
                    'Original: [1 2 3 4 5 6 7 8 9]\n'
                    'Reshaped (3x3):\n'
                    '[[1 2 3]\n'
                    ' [4 5 6]\n'
                    ' [7 8 9]]\n'
                    'Transposed:\n'
                    '[[1 4 7]\n'
                    ' [2 5 8]\n'
                    ' [3 6 9]]\n'
                    'Flattened: [1 2 3 4 5 6 7 8 9]\n'
                    'VStack:\n'
                    '[[1 2 3]\n'
                    ' [7 8 9]]\n'
                    'HStack: [1 2 3 7 8 9]\n'
                    'Split: [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch
import numpy as np

class TestArrayReshaping(unittest.TestCase):

    def run_student_code(self, input_str):
        captured = io.StringIO()
        with patch("sys.stdin", io.StringIO(input_str)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open("student_code.py").read(), {"__builtins__": __builtins__})
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_original_and_reshaped(self):
        output = self.run_student_code("1 2 3 4 5 6\\n2 3")
        self.assertIn("Original: [1 2 3 4 5 6]", output)
        self.assertIn("Reshaped (2x3):", output)

    def test_transpose(self):
        output = self.run_student_code("1 2 3 4 5 6\\n2 3")
        self.assertIn("Transposed:", output)
        self.assertIn("[1 4]", output)

    def test_flatten(self):
        output = self.run_student_code("1 2 3 4 5 6\\n2 3")
        self.assertIn("Flattened: [1 2 3 4 5 6]", output)

    def test_stacking(self):
        output = self.run_student_code("1 2 3 4 5 6\\n2 3")
        self.assertIn("VStack:", output)
        self.assertIn("HStack: [1 2 3 4 5 6]", output)

    def test_split(self):
        output = self.run_student_code("1 2 3 4 5 6\\n2 3")
        self.assertIn("Split: [array([1, 2, 3]), array([4, 5, 6])]", output)

    def test_3x3_reshape(self):
        output = self.run_student_code("1 2 3 4 5 6 7 8 9\\n3 3")
        self.assertIn("Reshaped (3x3):", output)
        self.assertIn("Split: [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]", output)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4 -- Statistical Operations
    # ------------------------------------------------------------------ #
    {
        'title': 'Statistical Operations',
        'description': '''## Statistical Operations

Use NumPy's powerful aggregation and statistical functions to
analyze data across different axes.

### Requirements

Write a program that:

1. **Reads** the first line: an integer `n` (number of rows).
2. **Reads** the next `n` lines: each line contains space-separated
   floats (one row of data). All rows have the same number of columns.
3. **Creates** a 2D NumPy array from the data.
4. **Prints** overall statistics (all values rounded to 2 decimals):
   - `Data:\\n<array>`
   - `Overall Mean: <value>`
   - `Overall Std: <value>`
5. **Prints** per-column statistics (axis=0), rounded to 2 decimals:
   - `Column Means: <array>`
   - `Column Medians: <array>`
   - `Column Std: <array>`
   - `Column Min: <array>`
   - `Column Max: <array>`
6. **Prints** per-row statistics (axis=1), rounded to 2 decimals:
   - `Row Means: <array>`
7. **Prints** the 25th and 75th percentiles per column:
   - `25th Percentile: <array>`
   - `75th Percentile: <array>`

Round all float output to 2 decimal places for consistent display.
Use `np.round(value, 2)` before printing.

### Example

**Input:**
```
3
10.0 20.0 30.0
40.0 50.0 60.0
70.0 80.0 90.0
```

**Output:**
```
Data:
[[10. 20. 30.]
 [40. 50. 60.]
 [70. 80. 90.]]
Overall Mean: 50.0
Overall Std: 25.82
Column Means: [40. 50. 60.]
Column Medians: [40. 50. 60.]
Column Std: [24.49 24.49 24.49]
Column Min: [10. 20. 30.]
Column Max: [70. 80. 90.]
Row Means: [20. 50. 80.]
25th Percentile: [25. 35. 45.]
75th Percentile: [55. 65. 75.]
```
''',
        'difficulty': 'medium',
        'order': 4,
        'item_order': 6,
        'starter_code': (
            'import numpy as np\n'
            '\n'
            '# TODO: Read number of rows\n'
            'n = int(input())\n'
            '\n'
            '# TODO: Read n rows of space-separated floats\n'
            'rows = []\n'
            'for _ in range(n):\n'
            '    row = list(map(float, input().split()))\n'
            '    rows.append(row)\n'
            '\n'
            '# TODO: Create 2D NumPy array\n'
            '\n'
            '# TODO: Print Data, Overall Mean, Overall Std\n'
            '\n'
            '# TODO: Print Column Means, Medians, Std, Min, Max (axis=0)\n'
            '\n'
            '# TODO: Print Row Means (axis=1)\n'
            '\n'
            '# TODO: Print 25th and 75th Percentiles per column\n'
        ),
        'hints': [
            'Use np.array(rows) to create the 2D array from the list of lists.',
            'np.mean(arr), np.std(arr) give overall stats; add axis=0 for column-wise.',
            'np.median(arr, axis=0) gives the median per column.',
            'np.percentile(arr, 25, axis=0) gives the 25th percentile per column.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '3\n10.0 20.0 30.0\n40.0 50.0 60.0\n70.0 80.0 90.0',
                'expected_output': (
                    'Data:\n'
                    '[[10. 20. 30.]\n'
                    ' [40. 50. 60.]\n'
                    ' [70. 80. 90.]]\n'
                    'Overall Mean: 50.0\n'
                    'Overall Std: 25.82\n'
                    'Column Means: [40. 50. 60.]\n'
                    'Column Medians: [40. 50. 60.]\n'
                    'Column Std: [24.49 24.49 24.49]\n'
                    'Column Min: [10. 20. 30.]\n'
                    'Column Max: [70. 80. 90.]\n'
                    'Row Means: [20. 50. 80.]\n'
                    '25th Percentile: [25. 35. 45.]\n'
                    '75th Percentile: [55. 65. 75.]'
                ),
            },
            {
                'input': '2\n1.0 2.0\n3.0 4.0',
                'expected_output': (
                    'Data:\n'
                    '[[1. 2.]\n'
                    ' [3. 4.]]\n'
                    'Overall Mean: 2.5\n'
                    'Overall Std: 1.12\n'
                    'Column Means: [2. 3.]\n'
                    'Column Medians: [2. 3.]\n'
                    'Column Std: [1. 1.]\n'
                    'Column Min: [1. 2.]\n'
                    'Column Max: [3. 4.]\n'
                    'Row Means: [1.5 3.5]\n'
                    '25th Percentile: [1.5 2.5]\n'
                    '75th Percentile: [2.5 3.5]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch
import numpy as np

class TestStatisticalOperations(unittest.TestCase):

    def run_student_code(self, input_str):
        captured = io.StringIO()
        with patch("sys.stdin", io.StringIO(input_str)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open("student_code.py").read(), {"__builtins__": __builtins__})
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_overall_mean(self):
        output = self.run_student_code("3\\n10.0 20.0 30.0\\n40.0 50.0 60.0\\n70.0 80.0 90.0")
        self.assertIn("Overall Mean: 50.0", output)

    def test_overall_std(self):
        output = self.run_student_code("3\\n10.0 20.0 30.0\\n40.0 50.0 60.0\\n70.0 80.0 90.0")
        self.assertIn("Overall Std: 25.82", output)

    def test_column_means(self):
        output = self.run_student_code("3\\n10.0 20.0 30.0\\n40.0 50.0 60.0\\n70.0 80.0 90.0")
        self.assertIn("Column Means: [40. 50. 60.]", output)

    def test_column_medians(self):
        output = self.run_student_code("3\\n10.0 20.0 30.0\\n40.0 50.0 60.0\\n70.0 80.0 90.0")
        self.assertIn("Column Medians: [40. 50. 60.]", output)

    def test_row_means(self):
        output = self.run_student_code("3\\n10.0 20.0 30.0\\n40.0 50.0 60.0\\n70.0 80.0 90.0")
        self.assertIn("Row Means: [20. 50. 80.]", output)

    def test_percentiles(self):
        output = self.run_student_code("3\\n10.0 20.0 30.0\\n40.0 50.0 60.0\\n70.0 80.0 90.0")
        self.assertIn("25th Percentile: [25. 35. 45.]", output)
        self.assertIn("75th Percentile: [55. 65. 75.]", output)

    def test_2x2_data(self):
        output = self.run_student_code("2\\n1.0 2.0\\n3.0 4.0")
        self.assertIn("Overall Mean: 2.5", output)
        self.assertIn("Column Means: [2. 3.]", output)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 5 -- Linear Algebra with NumPy
    # ------------------------------------------------------------------ #
    {
        'title': 'Linear Algebra with NumPy',
        'description': '''## Linear Algebra with NumPy

Use NumPy's linear algebra module (`np.linalg`) to perform matrix
operations and solve systems of linear equations.

### Requirements

Write a program that:

1. **Reads** the first line: an integer `n` (the size of the square
   matrix, i.e. n x n).
2. **Reads** the next `n` lines: each contains `n` space-separated
   floats (the matrix A).
3. **Reads** the next line: `n` space-separated floats (the vector b).
4. **Prints** the following (all floats rounded to 2 decimal places):
   - `Matrix A:\\n<array>`
   - `Vector b: <array>`
   - `Determinant: <value>`
   - `Inverse:\\n<array>`  (skip if determinant is 0; print
     `Inverse: singular matrix` instead)
   - `Eigenvalues: <array>`
   - `A @ b: <array>` -- matrix-vector product.
   - `Solution (Ax=b): <array>` -- solve Ax = b using
     `np.linalg.solve`. Skip if singular; print
     `Solution: singular matrix` instead.

Use `np.round(value, 2)` before printing arrays and floats to
ensure consistent 2-decimal output.

### Example

**Input:**
```
2
2.0 1.0
5.0 3.0
4.0 7.0
```

**Output:**
```
Matrix A:
[[2. 1.]
 [5. 3.]]
Vector b: [4. 7.]
Determinant: 1.0
Inverse:
[[ 3. -1.]
 [-5.  2.]]
Eigenvalues: [0.21 4.79]
A @ b: [15. 41.]
Solution (Ax=b): [ 5. -6.]
```
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 7,
        'starter_code': (
            'import numpy as np\n'
            '\n'
            '# TODO: Read matrix size n\n'
            'n = int(input())\n'
            '\n'
            '# TODO: Read n x n matrix A\n'
            'A_rows = []\n'
            'for _ in range(n):\n'
            '    row = list(map(float, input().split()))\n'
            '    A_rows.append(row)\n'
            '\n'
            '# TODO: Read vector b\n'
            'b = list(map(float, input().split()))\n'
            '\n'
            '# TODO: Create numpy arrays for A and b\n'
            '\n'
            '# TODO: Print Matrix A and Vector b\n'
            '\n'
            '# TODO: Compute and print Determinant (rounded to 2 decimals)\n'
            '\n'
            '# TODO: Compute and print Inverse (or "singular matrix" if det is 0)\n'
            '\n'
            '# TODO: Compute and print Eigenvalues (rounded to 2 decimals, sorted)\n'
            '\n'
            '# TODO: Compute and print A @ b (matrix-vector product)\n'
            '\n'
            '# TODO: Solve Ax = b and print Solution (or "singular matrix")\n'
        ),
        'hints': [
            'Use np.linalg.det(A) for the determinant and np.linalg.inv(A) for the inverse.',
            'Use np.linalg.eig(A)[0] for eigenvalues; sort them with np.sort().',
            'Use A @ b or np.dot(A, b) for matrix-vector multiplication.',
            'Use np.linalg.solve(A, b) to solve Ax = b. Wrap in try/except for singular matrices.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '2\n2.0 1.0\n5.0 3.0\n4.0 7.0',
                'expected_output': (
                    'Matrix A:\n'
                    '[[2. 1.]\n'
                    ' [5. 3.]]\n'
                    'Vector b: [4. 7.]\n'
                    'Determinant: 1.0\n'
                    'Inverse:\n'
                    '[[ 3. -1.]\n'
                    ' [-5.  2.]]\n'
                    'Eigenvalues: [0.21 4.79]\n'
                    'A @ b: [15. 41.]\n'
                    'Solution (Ax=b): [ 5. -6.]'
                ),
            },
            {
                'input': '3\n1.0 0.0 0.0\n0.0 2.0 0.0\n0.0 0.0 3.0\n1.0 2.0 3.0',
                'expected_output': (
                    'Matrix A:\n'
                    '[[1. 0. 0.]\n'
                    ' [0. 2. 0.]\n'
                    ' [0. 0. 3.]]\n'
                    'Vector b: [1. 2. 3.]\n'
                    'Determinant: 6.0\n'
                    'Inverse:\n'
                    '[[1.   0.   0.  ]\n'
                    ' [0.   0.5  0.  ]\n'
                    ' [0.   0.   0.33]]\n'
                    'Eigenvalues: [1. 2. 3.]\n'
                    'A @ b: [1. 4. 9.]\n'
                    'Solution (Ax=b): [1. 1. 1.]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import io
import sys
from unittest.mock import patch
import numpy as np

class TestLinearAlgebra(unittest.TestCase):

    def run_student_code(self, input_str):
        captured = io.StringIO()
        with patch("sys.stdin", io.StringIO(input_str)):
            old_stdout = sys.stdout
            sys.stdout = captured
            try:
                exec(open("student_code.py").read(), {"__builtins__": __builtins__})
            finally:
                sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_determinant(self):
        output = self.run_student_code("2\\n2.0 1.0\\n5.0 3.0\\n4.0 7.0")
        self.assertIn("Determinant: 1.0", output)

    def test_inverse(self):
        output = self.run_student_code("2\\n2.0 1.0\\n5.0 3.0\\n4.0 7.0")
        self.assertIn("Inverse:", output)
        self.assertIn("3.", output)
        self.assertIn("-1.", output)

    def test_eigenvalues(self):
        output = self.run_student_code("2\\n2.0 1.0\\n5.0 3.0\\n4.0 7.0")
        self.assertIn("Eigenvalues:", output)
        self.assertIn("0.21", output)
        self.assertIn("4.79", output)

    def test_matrix_vector_product(self):
        output = self.run_student_code("2\\n2.0 1.0\\n5.0 3.0\\n4.0 7.0")
        self.assertIn("A @ b: [15. 41.]", output)

    def test_solution(self):
        output = self.run_student_code("2\\n2.0 1.0\\n5.0 3.0\\n4.0 7.0")
        self.assertIn("Solution (Ax=b): [5. -6.]", output)

    def test_identity_like_diagonal(self):
        output = self.run_student_code("3\\n1.0 0.0 0.0\\n0.0 2.0 0.0\\n0.0 0.0 3.0\\n1.0 2.0 3.0")
        self.assertIn("Determinant: 6.0", output)
        self.assertIn("Solution (Ax=b): [1. 1. 1.]", output)

if __name__ == "__main__":
    unittest.main()
''',
    },
]
