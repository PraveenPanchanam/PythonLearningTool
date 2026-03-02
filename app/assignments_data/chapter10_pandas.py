CHAPTER_INFO = {
    'title': 'Pandas for Data Analysis',
    'description': (
        'Learn to use pandas, the most popular Python library for data '
        'analysis. Master Series and DataFrame creation, data selection '
        'with loc/iloc, filtering, sorting, groupby aggregation, merging '
        'DataFrames, and handling missing data -- all essential skills '
        'for working with real-world datasets.'
    ),
    'difficulty_level': 'advanced',
    'order': 10,
    'learning_objectives': [
        'Create Series and DataFrames from dictionaries and lists',
        'Explore DataFrames with shape, dtypes, head, and describe',
        'Select data using loc (label-based) and iloc (position-based)',
        'Filter rows with boolean conditions and the query method',
        'Sort DataFrames by one or more columns',
        'Group data with groupby and compute aggregations (mean, sum, count)',
        'Merge and join DataFrames using inner, left, and outer joins',
        'Detect, fill, and drop missing (NaN) values',
        'Apply custom functions to columns with apply()',
        'Create new computed columns from existing data',
    ],
    'estimated_time_minutes': 70,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1 -- DataFrame Creation & Exploration
    # ------------------------------------------------------------------ #
    {
        'title': 'DataFrame Creation & Exploration',
        'description': '''## DataFrame Creation & Exploration

Learn to create a pandas DataFrame from user-supplied data and explore
its structure using built-in inspection methods.

### Requirements

1. Read an integer **n** from the first line of input -- the number of
   people.
2. Read **n** subsequent lines, each containing **comma-separated**
   values: `name,age,score` (age is int, score is float).
3. Build a DataFrame with columns `Name`, `Age`, and `Score`.
4. Print the following, each section separated by a blank line:
   - `Shape: (rows, cols)` -- e.g. `Shape: (3, 3)`
   - `Columns: Name, Age, Score` -- column names joined by `, `
   - `Dtypes:` followed by one line per column in the format
     `  <col>: <dtype>` (two-space indent). Use `object` for strings,
     `int64` for integers, `float64` for floats.
   - `Oldest: <name>` -- the name of the person with the highest age.
   - `Average Score: <value>` -- mean score rounded to **2 decimal
     places**.

### Example

**Input:**
```
3
Alice,30,85.50
Bob,25,90.00
Carol,35,78.25
```

**Output:**
```
Shape: (3, 3)
Columns: Name, Age, Score

Dtypes:
  Name: object
  Age: int64
  Score: float64

Oldest: Carol
Average Score: 84.58
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            'import pandas as pd\n'
            '\n'
            '# TODO: Read the number of records\n'
            'n = int(input())\n'
            '\n'
            '# TODO: Read n lines of comma-separated data (name,age,score)\n'
            'names, ages, scores = [], [], []\n'
            'for _ in range(n):\n'
            '    parts = input().split(",")\n'
            '    names.append(parts[0])\n'
            '    ages.append(int(parts[1]))\n'
            '    scores.append(float(parts[2]))\n'
            '\n'
            '# TODO: Create a DataFrame with columns Name, Age, Score\n'
            '\n'
            '# TODO: Print Shape, Columns, Dtypes, Oldest, Average Score\n'
        ),
        'hints': [
            'Create the DataFrame with pd.DataFrame({"Name": names, "Age": ages, "Score": scores}).',
            'Use df.shape to get (rows, cols) and ", ".join(df.columns) for column names.',
            'Loop over df.dtypes.items() to print each column\'s dtype.',
            'Use df.loc[df["Age"].idxmax(), "Name"] to find the oldest person\'s name.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': (
                    '3\n'
                    'Alice,30,85.50\n'
                    'Bob,25,90.00\n'
                    'Carol,35,78.25\n'
                ),
                'expected_output': (
                    'Shape: (3, 3)\n'
                    'Columns: Name, Age, Score\n'
                    '\n'
                    'Dtypes:\n'
                    '  Name: object\n'
                    '  Age: int64\n'
                    '  Score: float64\n'
                    '\n'
                    'Oldest: Carol\n'
                    'Average Score: 84.58'
                ),
            },
            {
                'input': (
                    '2\n'
                    'Dan,40,72.00\n'
                    'Eve,28,95.50\n'
                ),
                'expected_output': (
                    'Shape: (2, 3)\n'
                    'Columns: Name, Age, Score\n'
                    '\n'
                    'Dtypes:\n'
                    '  Name: object\n'
                    '  Age: int64\n'
                    '  Score: float64\n'
                    '\n'
                    'Oldest: Dan\n'
                    'Average Score: 83.75'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestDataFrameCreation(unittest.TestCase):

    def test_shape(self):
        out = run_student("3\\nAlice,30,85.50\\nBob,25,90.00\\nCarol,35,78.25\\n")
        self.assertIn("Shape: (3, 3)", out)

    def test_columns(self):
        out = run_student("3\\nAlice,30,85.50\\nBob,25,90.00\\nCarol,35,78.25\\n")
        self.assertIn("Columns: Name, Age, Score", out)

    def test_dtypes(self):
        out = run_student("3\\nAlice,30,85.50\\nBob,25,90.00\\nCarol,35,78.25\\n")
        self.assertIn("Name: object", out)
        self.assertIn("Age: int64", out)
        self.assertIn("Score: float64", out)

    def test_oldest(self):
        out = run_student("3\\nAlice,30,85.50\\nBob,25,90.00\\nCarol,35,78.25\\n")
        self.assertIn("Oldest: Carol", out)

    def test_average_score(self):
        out = run_student("3\\nAlice,30,85.50\\nBob,25,90.00\\nCarol,35,78.25\\n")
        self.assertIn("Average Score: 84.58", out)

    def test_two_records(self):
        out = run_student("2\\nDan,40,72.00\\nEve,28,95.50\\n")
        self.assertIn("Shape: (2, 3)", out)
        self.assertIn("Oldest: Dan", out)
        self.assertIn("Average Score: 83.75", out)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2 -- Filtering & Selection
    # ------------------------------------------------------------------ #
    {
        'title': 'Filtering & Selection',
        'description': '''## Filtering & Selection

Learn to select and filter rows from a DataFrame using `loc`, `iloc`,
and boolean conditions.

### Requirements

1. Read an integer **n** (number of employees).
2. Read **n** lines of comma-separated data: `name,department,salary`
   (salary is an integer).
3. Build a DataFrame with columns `Name`, `Department`, `Salary`.
4. Read a **filter threshold** (integer) from the next input line.
5. Print the following sections, each separated by a blank line:

   - `== First two rows (iloc) ==`
     For each of the first two rows print: `<Name> | <Department> | <Salary>`
   - `== High earners (Salary >= threshold) ==`
     For each matching row: `<Name> | <Department> | <Salary>`
     If none match, print `No matches found.`
   - `== Department counts ==`
     For each unique department (sorted alphabetically):
     `<Department>: <count>`

### Example

**Input:**
```
5
Alice,Engineering,95000
Bob,Marketing,60000
Carol,Engineering,110000
Dan,Marketing,75000
Eve,Engineering,85000
80000
```

**Output:**
```
== First two rows (iloc) ==
Alice | Engineering | 95000
Bob | Marketing | 60000

== High earners (Salary >= 80000) ==
Alice | Engineering | 95000
Carol | Engineering | 110000
Eve | Engineering | 85000

== Department counts ==
Engineering: 3
Marketing: 2
```
''',
        'difficulty': 'easy',
        'order': 2,
        'item_order': 4,
        'starter_code': (
            'import pandas as pd\n'
            '\n'
            '# TODO: Read n, then n lines of name,department,salary\n'
            'n = int(input())\n'
            'names, departments, salaries = [], [], []\n'
            'for _ in range(n):\n'
            '    parts = input().split(",")\n'
            '    names.append(parts[0])\n'
            '    departments.append(parts[1])\n'
            '    salaries.append(int(parts[2]))\n'
            '\n'
            '# TODO: Create DataFrame with columns Name, Department, Salary\n'
            '\n'
            '# TODO: Read the filter threshold\n'
            'threshold = int(input())\n'
            '\n'
            '# TODO: Print first two rows using iloc\n'
            '\n'
            '# TODO: Filter and print rows where Salary >= threshold\n'
            '\n'
            '# TODO: Print department counts (sorted alphabetically)\n'
        ),
        'hints': [
            'Use df.iloc[:2] to select the first two rows.',
            'Boolean filter: df[df["Salary"] >= threshold] gives rows meeting the condition.',
            'Use df["Department"].value_counts().sort_index() to get alphabetically sorted counts.',
            'Iterate over filtered rows with for _, row in filtered.iterrows(): print(f"{row.Name} | ...").',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': (
                    '5\n'
                    'Alice,Engineering,95000\n'
                    'Bob,Marketing,60000\n'
                    'Carol,Engineering,110000\n'
                    'Dan,Marketing,75000\n'
                    'Eve,Engineering,85000\n'
                    '80000\n'
                ),
                'expected_output': (
                    '== First two rows (iloc) ==\n'
                    'Alice | Engineering | 95000\n'
                    'Bob | Marketing | 60000\n'
                    '\n'
                    '== High earners (Salary >= 80000) ==\n'
                    'Alice | Engineering | 95000\n'
                    'Carol | Engineering | 110000\n'
                    'Eve | Engineering | 85000\n'
                    '\n'
                    '== Department counts ==\n'
                    'Engineering: 3\n'
                    'Marketing: 2'
                ),
            },
            {
                'input': (
                    '3\n'
                    'Zara,Sales,50000\n'
                    'Yuki,Sales,55000\n'
                    'Xander,HR,48000\n'
                    '60000\n'
                ),
                'expected_output': (
                    '== First two rows (iloc) ==\n'
                    'Zara | Sales | 50000\n'
                    'Yuki | Sales | 55000\n'
                    '\n'
                    '== High earners (Salary >= 60000) ==\n'
                    'No matches found.\n'
                    '\n'
                    '== Department counts ==\n'
                    'HR: 1\n'
                    'Sales: 2'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestFilteringSelection(unittest.TestCase):

    def _input1(self):
        return (
            "5\\nAlice,Engineering,95000\\nBob,Marketing,60000\\n"
            "Carol,Engineering,110000\\nDan,Marketing,75000\\n"
            "Eve,Engineering,85000\\n80000\\n"
        )

    def test_first_two_rows(self):
        out = run_student(self._input1())
        self.assertIn("Alice | Engineering | 95000", out)
        self.assertIn("Bob | Marketing | 60000", out)

    def test_high_earners(self):
        out = run_student(self._input1())
        self.assertIn("Alice | Engineering | 95000", out)
        self.assertIn("Carol | Engineering | 110000", out)
        self.assertIn("Eve | Engineering | 85000", out)
        # Bob and Dan should NOT appear in high earners
        lines = out.split("== High earners")[1].split("== Department counts")[0]
        self.assertNotIn("Bob", lines)
        self.assertNotIn("Dan", lines)

    def test_department_counts(self):
        out = run_student(self._input1())
        self.assertIn("Engineering: 3", out)
        self.assertIn("Marketing: 2", out)

    def test_no_matches(self):
        inp = "3\\nZara,Sales,50000\\nYuki,Sales,55000\\nXander,HR,48000\\n60000\\n"
        out = run_student(inp)
        self.assertIn("No matches found.", out)

    def test_department_counts_sorted(self):
        inp = "3\\nZara,Sales,50000\\nYuki,Sales,55000\\nXander,HR,48000\\n60000\\n"
        out = run_student(inp)
        hr_pos = out.index("HR:")
        sales_pos = out.index("Sales:")
        self.assertLess(hr_pos, sales_pos, "Departments should be sorted alphabetically")

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3 -- GroupBy & Aggregation
    # ------------------------------------------------------------------ #
    {
        'title': 'GroupBy & Aggregation',
        'description': '''## GroupBy & Aggregation

Learn to group rows by a categorical column and compute summary
statistics using pandas `groupby`.

### Requirements

1. Read an integer **n** (number of records).
2. Read **n** lines of comma-separated data:
   `product,category,quantity,price`
   (quantity is int, price is float).
3. Build a DataFrame with columns `Product`, `Category`, `Quantity`,
   `Price`.
4. Compute a **Revenue** column: `Quantity * Price`.
5. Print the following sections, each separated by a blank line:

   - `== Revenue by Category ==`
     Group by `Category` (sorted alphabetically). For each group print:
     `<Category>: <total_revenue>` (revenue rounded to **2 decimal
     places**).

   - `== Category Statistics ==`
     For each category (sorted alphabetically) print:
     `<Category> -> count: <n>, avg_price: <mean_price>, total_qty: <sum_qty>`
     (avg_price rounded to **2 decimal places**).

   - `== Top Product ==`
     Print the product with the highest single-row revenue:
     `<Product> (Revenue: <value>)` (revenue rounded to **2 decimal
     places**).

### Example

**Input:**
```
5
Widget,Electronics,10,29.99
Gadget,Electronics,5,49.99
Shirt,Clothing,20,15.00
Pants,Clothing,8,35.50
Charger,Electronics,15,12.99
```

**Output:**
```
== Revenue by Category ==
Clothing: 584.00
Electronics: 744.75

== Category Statistics ==
Clothing -> count: 2, avg_price: 25.25, total_qty: 28
Electronics -> count: 3, avg_price: 30.99, total_qty: 30

== Top Product ==
Shirt (Revenue: 300.00)
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            'import pandas as pd\n'
            '\n'
            '# TODO: Read n records of product,category,quantity,price\n'
            'n = int(input())\n'
            'products, categories, quantities, prices = [], [], [], []\n'
            'for _ in range(n):\n'
            '    parts = input().split(",")\n'
            '    products.append(parts[0])\n'
            '    categories.append(parts[1])\n'
            '    quantities.append(int(parts[2]))\n'
            '    prices.append(float(parts[3]))\n'
            '\n'
            '# TODO: Create DataFrame with columns Product, Category, Quantity, Price\n'
            '\n'
            '# TODO: Add a Revenue column (Quantity * Price)\n'
            '\n'
            '# TODO: Group by Category and print total revenue per category\n'
            '\n'
            '# TODO: Print category statistics (count, avg_price, total_qty)\n'
            '\n'
            '# TODO: Find and print the top product by revenue\n'
        ),
        'hints': [
            'Add Revenue column: df["Revenue"] = df["Quantity"] * df["Price"].',
            'Group revenue: df.groupby("Category")["Revenue"].sum().sort_index().',
            'For statistics, use df.groupby("Category").agg({"Price": "mean", "Quantity": "sum", "Product": "count"}).',
            'Top product: df.loc[df["Revenue"].idxmax()] gives the row with the highest revenue.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': (
                    '5\n'
                    'Widget,Electronics,10,29.99\n'
                    'Gadget,Electronics,5,49.99\n'
                    'Shirt,Clothing,20,15.00\n'
                    'Pants,Clothing,8,35.50\n'
                    'Charger,Electronics,15,12.99\n'
                ),
                'expected_output': (
                    '== Revenue by Category ==\n'
                    'Clothing: 584.00\n'
                    'Electronics: 744.75\n'
                    '\n'
                    '== Category Statistics ==\n'
                    'Clothing -> count: 2, avg_price: 25.25, total_qty: 28\n'
                    'Electronics -> count: 3, avg_price: 30.99, total_qty: 30\n'
                    '\n'
                    '== Top Product ==\n'
                    'Shirt (Revenue: 300.00)'
                ),
            },
            {
                'input': (
                    '4\n'
                    'Apple,Fruit,50,1.20\n'
                    'Banana,Fruit,30,0.80\n'
                    'Milk,Dairy,20,3.50\n'
                    'Cheese,Dairy,10,5.00\n'
                ),
                'expected_output': (
                    '== Revenue by Category ==\n'
                    'Dairy: 120.00\n'
                    'Fruit: 84.00\n'
                    '\n'
                    '== Category Statistics ==\n'
                    'Dairy -> count: 2, avg_price: 4.25, total_qty: 30\n'
                    'Fruit -> count: 2, avg_price: 1.00, total_qty: 80\n'
                    '\n'
                    '== Top Product ==\n'
                    'Milk (Revenue: 70.00)'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestGroupByAggregation(unittest.TestCase):

    def _input1(self):
        return (
            "5\\nWidget,Electronics,10,29.99\\nGadget,Electronics,5,49.99\\n"
            "Shirt,Clothing,20,15.00\\nPants,Clothing,8,35.50\\n"
            "Charger,Electronics,15,12.99\\n"
        )

    def test_revenue_by_category(self):
        out = run_student(self._input1())
        self.assertIn("Clothing: 584.00", out)
        self.assertIn("Electronics: 744.75", out)

    def test_category_stats_clothing(self):
        out = run_student(self._input1())
        self.assertIn("Clothing -> count: 2, avg_price: 25.25, total_qty: 28", out)

    def test_category_stats_electronics(self):
        out = run_student(self._input1())
        self.assertIn("Electronics -> count: 3, avg_price: 30.99, total_qty: 30", out)

    def test_top_product(self):
        out = run_student(self._input1())
        self.assertIn("Shirt (Revenue: 300.00)", out)

    def test_second_dataset(self):
        inp = (
            "4\\nApple,Fruit,50,1.20\\nBanana,Fruit,30,0.80\\n"
            "Milk,Dairy,20,3.50\\nCheese,Dairy,10,5.00\\n"
        )
        out = run_student(inp)
        self.assertIn("Dairy: 120.00", out)
        self.assertIn("Fruit: 84.00", out)
        self.assertIn("Milk (Revenue: 70.00)", out)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4 -- Handling Missing Data
    # ------------------------------------------------------------------ #
    {
        'title': 'Handling Missing Data',
        'description': '''## Handling Missing Data

Learn to detect, report, fill, and drop missing values in a pandas
DataFrame -- a critical skill for real-world data cleaning.

### Requirements

1. Read an integer **n** (number of records).
2. Read **n** lines of comma-separated data: `name,city,salary`
   - If any field is the string `NA` or `NaN`, treat it as missing.
3. Build a DataFrame with columns `Name`, `City`, `Salary`.
   - Convert `Salary` to float (missing values become `NaN`).
   - Convert `NA`/`NaN` strings in `Name` and `City` to actual `NaN`.
4. Print the following sections, each separated by a blank line:

   - `== Missing Value Report ==`
     For each column print: `<Column>: <count> missing`
     Then print: `Total cells: <total>, Missing: <total_missing>`

   - `== After Filling ==`
     Fill missing cities with `"Unknown"` and missing salaries with the
     **mean** of non-missing salaries (rounded to **2 decimal places**
     before filling).
     Print each row as: `<Name> | <City> | <Salary>`
     (Salary formatted to **2 decimal places**.)
     **Skip rows where Name is still missing after this step** (drop
     them).

   - `== Clean Row Count ==`
     Print: `Rows after cleaning: <count>`

### Example

**Input:**
```
5
Alice,London,50000
Bob,NA,60000
NA,Paris,55000
Carol,Berlin,NA
Dan,London,70000
```

**Output:**
```
== Missing Value Report ==
Name: 1 missing
City: 1 missing
Salary: 1 missing
Total cells: 15, Missing: 3

== After Filling ==
Alice | London | 50000.00
Bob | Unknown | 60000.00
Carol | Berlin | 58750.00
Dan | London | 70000.00

== Clean Row Count ==
Rows after cleaning: 4
```
''',
        'difficulty': 'medium',
        'order': 4,
        'item_order': 7,
        'starter_code': (
            'import pandas as pd\n'
            'import numpy as np\n'
            '\n'
            '# TODO: Read n records of name,city,salary\n'
            'n = int(input())\n'
            'data = []\n'
            'for _ in range(n):\n'
            '    data.append(input().split(","))\n'
            '\n'
            '# TODO: Create DataFrame with columns Name, City, Salary\n'
            '# Replace "NA" and "NaN" strings with actual NaN values\n'
            '# Convert Salary column to float\n'
            '\n'
            '# TODO: Print missing value report\n'
            '#   - Count missing per column\n'
            '#   - Total cells and total missing\n'
            '\n'
            '# TODO: Fill missing City with "Unknown"\n'
            '# TODO: Fill missing Salary with the mean of non-missing salaries\n'
            '#        (round the mean to 2 decimal places before filling)\n'
            '# TODO: Drop rows where Name is still missing\n'
            '\n'
            '# TODO: Print cleaned rows and final count\n'
        ),
        'hints': [
            'Replace NA/NaN strings: df.replace(["NA", "NaN"], np.nan, inplace=True), then convert Salary with pd.to_numeric(df["Salary"], errors="coerce").',
            'Count missing per column: df.isna().sum(). Total missing: df.isna().sum().sum(). Total cells: df.size.',
            'Compute mean before filling: mean_sal = round(df["Salary"].mean(), 2), then df["Salary"].fillna(mean_sal).',
            'Drop rows with missing Name: df.dropna(subset=["Name"]).',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': (
                    '5\n'
                    'Alice,London,50000\n'
                    'Bob,NA,60000\n'
                    'NA,Paris,55000\n'
                    'Carol,Berlin,NA\n'
                    'Dan,London,70000\n'
                ),
                'expected_output': (
                    '== Missing Value Report ==\n'
                    'Name: 1 missing\n'
                    'City: 1 missing\n'
                    'Salary: 1 missing\n'
                    'Total cells: 15, Missing: 3\n'
                    '\n'
                    '== After Filling ==\n'
                    'Alice | London | 50000.00\n'
                    'Bob | Unknown | 60000.00\n'
                    'Carol | Berlin | 58750.00\n'
                    'Dan | London | 70000.00\n'
                    '\n'
                    '== Clean Row Count ==\n'
                    'Rows after cleaning: 4'
                ),
            },
            {
                'input': (
                    '4\n'
                    'Alice,Tokyo,80000\n'
                    'Bob,NaN,NaN\n'
                    'Carol,Tokyo,90000\n'
                    'NaN,NaN,70000\n'
                ),
                'expected_output': (
                    '== Missing Value Report ==\n'
                    'Name: 1 missing\n'
                    'City: 2 missing\n'
                    'Salary: 1 missing\n'
                    'Total cells: 12, Missing: 4\n'
                    '\n'
                    '== After Filling ==\n'
                    'Alice | Tokyo | 80000.00\n'
                    'Bob | Unknown | 80000.00\n'
                    'Carol | Tokyo | 90000.00\n'
                    '\n'
                    '== Clean Row Count ==\n'
                    'Rows after cleaning: 3'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestHandlingMissingData(unittest.TestCase):

    def _input1(self):
        return (
            "5\\nAlice,London,50000\\nBob,NA,60000\\n"
            "NA,Paris,55000\\nCarol,Berlin,NA\\nDan,London,70000\\n"
        )

    def test_missing_report(self):
        out = run_student(self._input1())
        self.assertIn("Name: 1 missing", out)
        self.assertIn("City: 1 missing", out)
        self.assertIn("Salary: 1 missing", out)
        self.assertIn("Total cells: 15, Missing: 3", out)

    def test_filled_unknown_city(self):
        out = run_student(self._input1())
        self.assertIn("Bob | Unknown | 60000.00", out)

    def test_filled_salary_mean(self):
        out = run_student(self._input1())
        # Mean of 50000, 60000, 55000, 70000 = 58750.00
        self.assertIn("Carol | Berlin | 58750.00", out)

    def test_dropped_missing_name(self):
        out = run_student(self._input1())
        after_filling = out.split("== After Filling ==")[1].split("== Clean Row Count ==")[0]
        self.assertNotIn("Paris", after_filling,
            "Row with missing Name (NA,Paris,...) should be dropped")

    def test_clean_row_count(self):
        out = run_student(self._input1())
        self.assertIn("Rows after cleaning: 4", out)

    def test_second_dataset(self):
        inp = (
            "4\\nAlice,Tokyo,80000\\nBob,NaN,NaN\\n"
            "Carol,Tokyo,90000\\nNaN,NaN,70000\\n"
        )
        out = run_student(inp)
        self.assertIn("Total cells: 12, Missing: 4", out)
        self.assertIn("Rows after cleaning: 3", out)
        self.assertIn("Bob | Unknown | 80000.00", out)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 5 -- Data Merging & Transformation
    # ------------------------------------------------------------------ #
    {
        'title': 'Data Merging & Transformation',
        'description': '''## Data Merging & Transformation

Learn to merge two DataFrames using different join strategies and
transform data by applying custom functions and creating new columns.

### Requirements

1. **Read the first dataset** (employees):
   - Read an integer **n1**.
   - Read **n1** lines: `emp_id,name,dept_id` (emp_id and dept_id are
     integers).
   - Build DataFrame `employees` with columns `EmpID`, `Name`,
     `DeptID`.

2. **Read the second dataset** (departments):
   - Read an integer **n2**.
   - Read **n2** lines: `dept_id,dept_name,budget` (dept_id is int,
     budget is float).
   - Build DataFrame `departments` with columns `DeptID`, `DeptName`,
     `Budget`.

3. **Merge and transform**:
   - Perform a **left join** of `employees` onto `departments` using
     `DeptID` as the key.
   - Add a new column `BudgetPerHead`: for each employee, compute
     `Budget / (number of employees in that department)`. Round to
     **2 decimal places**. If budget is missing (unmatched dept), use
     `0.00`.
   - Add a new column `NameUpper`: the employee `Name` in uppercase.

4. **Output** the following sections separated by a blank line:

   - `== Merged Data ==`
     For each row: `<EmpID> | <Name> | <DeptName> | <Budget>`
     (Budget formatted to 2 decimals. If DeptName is missing, print
     `N/A`. If Budget is missing, print `0.00`.)

   - `== Budget Per Head ==`
     For each row: `<Name>: <BudgetPerHead>`

   - `== Uppercase Names ==`
     Print all uppercase names separated by `, `.

### Example

**Input:**
```
4
1,Alice,10
2,Bob,20
3,Carol,10
4,Dan,30
2
10,Engineering,500000
20,Marketing,200000
```

**Output:**
```
== Merged Data ==
1 | Alice | Engineering | 500000.00
2 | Bob | Marketing | 200000.00
3 | Carol | Engineering | 500000.00
4 | Dan | N/A | 0.00

== Budget Per Head ==
Alice: 250000.00
Bob: 200000.00
Carol: 250000.00
Dan: 0.00

== Uppercase Names ==
ALICE, BOB, CAROL, DAN
```
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 8,
        'starter_code': (
            'import pandas as pd\n'
            'import numpy as np\n'
            '\n'
            '# --- Read employees ---\n'
            'n1 = int(input())\n'
            'emp_ids, names, dept_ids_emp = [], [], []\n'
            'for _ in range(n1):\n'
            '    parts = input().split(",")\n'
            '    emp_ids.append(int(parts[0]))\n'
            '    names.append(parts[1])\n'
            '    dept_ids_emp.append(int(parts[2]))\n'
            '\n'
            'employees = pd.DataFrame({\n'
            '    "EmpID": emp_ids,\n'
            '    "Name": names,\n'
            '    "DeptID": dept_ids_emp,\n'
            '})\n'
            '\n'
            '# --- Read departments ---\n'
            'n2 = int(input())\n'
            'dept_ids, dept_names, budgets = [], [], []\n'
            'for _ in range(n2):\n'
            '    parts = input().split(",")\n'
            '    dept_ids.append(int(parts[0]))\n'
            '    dept_names.append(parts[1])\n'
            '    budgets.append(float(parts[2]))\n'
            '\n'
            'departments = pd.DataFrame({\n'
            '    "DeptID": dept_ids,\n'
            '    "DeptName": dept_names,\n'
            '    "Budget": budgets,\n'
            '})\n'
            '\n'
            '# TODO: Left-join employees with departments on DeptID\n'
            '\n'
            '# TODO: Compute BudgetPerHead = Budget / (count of employees in dept)\n'
            '#        Fill NaN budgets with 0. Round to 2 decimal places.\n'
            '\n'
            '# TODO: Add NameUpper column using apply()\n'
            '\n'
            '# TODO: Print Merged Data section\n'
            '\n'
            '# TODO: Print Budget Per Head section\n'
            '\n'
            '# TODO: Print Uppercase Names section\n'
        ),
        'hints': [
            'Merge: merged = employees.merge(departments, on="DeptID", how="left").',
            'Count employees per dept: dept_counts = employees.groupby("DeptID")["EmpID"].count(). Then merge or map this back.',
            'BudgetPerHead: merged["Budget"].fillna(0) / merged["DeptID"].map(dept_counts).fillna(1), then round to 2.',
            'NameUpper: merged["Name"].apply(str.upper) or merged["Name"].str.upper().',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': (
                    '4\n'
                    '1,Alice,10\n'
                    '2,Bob,20\n'
                    '3,Carol,10\n'
                    '4,Dan,30\n'
                    '2\n'
                    '10,Engineering,500000\n'
                    '20,Marketing,200000\n'
                ),
                'expected_output': (
                    '== Merged Data ==\n'
                    '1 | Alice | Engineering | 500000.00\n'
                    '2 | Bob | Marketing | 200000.00\n'
                    '3 | Carol | Engineering | 500000.00\n'
                    '4 | Dan | N/A | 0.00\n'
                    '\n'
                    '== Budget Per Head ==\n'
                    'Alice: 250000.00\n'
                    'Bob: 200000.00\n'
                    'Carol: 250000.00\n'
                    'Dan: 0.00\n'
                    '\n'
                    '== Uppercase Names ==\n'
                    'ALICE, BOB, CAROL, DAN'
                ),
            },
            {
                'input': (
                    '3\n'
                    '1,Xena,100\n'
                    '2,Yuri,100\n'
                    '3,Zack,200\n'
                    '2\n'
                    '100,Research,300000\n'
                    '200,Sales,150000\n'
                ),
                'expected_output': (
                    '== Merged Data ==\n'
                    '1 | Xena | Research | 300000.00\n'
                    '2 | Yuri | Research | 300000.00\n'
                    '3 | Zack | Sales | 150000.00\n'
                    '\n'
                    '== Budget Per Head ==\n'
                    'Xena: 150000.00\n'
                    'Yuri: 150000.00\n'
                    'Zack: 150000.00\n'
                    '\n'
                    '== Uppercase Names ==\n'
                    'XENA, YURI, ZACK'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import subprocess, os, sys

def run_student(input_data):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'student_code.py')],
        input=input_data, capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(__file__),
    )
    return result.stdout.strip()

class TestDataMerging(unittest.TestCase):

    def _input1(self):
        return (
            "4\\n1,Alice,10\\n2,Bob,20\\n3,Carol,10\\n4,Dan,30\\n"
            "2\\n10,Engineering,500000\\n20,Marketing,200000\\n"
        )

    def test_merged_data(self):
        out = run_student(self._input1())
        self.assertIn("1 | Alice | Engineering | 500000.00", out)
        self.assertIn("2 | Bob | Marketing | 200000.00", out)
        self.assertIn("3 | Carol | Engineering | 500000.00", out)
        self.assertIn("4 | Dan | N/A | 0.00", out)

    def test_budget_per_head(self):
        out = run_student(self._input1())
        self.assertIn("Alice: 250000.00", out)
        self.assertIn("Bob: 200000.00", out)
        self.assertIn("Carol: 250000.00", out)
        self.assertIn("Dan: 0.00", out)

    def test_uppercase_names(self):
        out = run_student(self._input1())
        self.assertIn("ALICE, BOB, CAROL, DAN", out)

    def test_all_matched(self):
        inp = (
            "3\\n1,Xena,100\\n2,Yuri,100\\n3,Zack,200\\n"
            "2\\n100,Research,300000\\n200,Sales,150000\\n"
        )
        out = run_student(inp)
        self.assertIn("Xena: 150000.00", out)
        self.assertIn("Yuri: 150000.00", out)
        self.assertIn("Zack: 150000.00", out)
        self.assertIn("XENA, YURI, ZACK", out)

    def test_no_na_when_all_match(self):
        inp = (
            "3\\n1,Xena,100\\n2,Yuri,100\\n3,Zack,200\\n"
            "2\\n100,Research,300000\\n200,Sales,150000\\n"
        )
        out = run_student(inp)
        self.assertNotIn("N/A", out)

if __name__ == "__main__":
    unittest.main()
''',
    },
]
