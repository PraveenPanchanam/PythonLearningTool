CHAPTER_ORDER = 10

LESSONS = [
    {
        'title': 'Introduction to Series and DataFrames',
        'description': 'Learn the core data structures of pandas - Series and DataFrames - the essential tools for working with structured data in Python, just like spreadsheets but with superpowers.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'what-is-pandas',
                'title': 'What is Pandas?',
                'content': """## What is Pandas?

**Pandas** is Python's most popular library for data analysis and manipulation. If you have ever worked with spreadsheets like Excel or Google Sheets, pandas gives you the same power (and much more) directly in Python.

### Why Pandas Matters in the Real World

Every organization deals with data. Consider these everyday scenarios:

- A **teacher** tracking student grades across multiple subjects and semesters
- A **store manager** analyzing daily sales to decide what to restock
- A **doctor** reviewing patient records to spot health trends
- A **marketer** examining website traffic to plan campaigns

Pandas makes all of these tasks efficient and repeatable with code.

### Importing Pandas

By convention, pandas is imported with the alias `pd`:

```python
import pandas as pd
```

This is a universal convention in the Python community - you will see `pd` used in virtually every tutorial, documentation page, and production codebase.

### The Two Core Data Structures

Pandas provides two primary data structures:

| Structure     | Description                          | Real-World Analogy            |
|---------------|--------------------------------------|-------------------------------|
| **Series**    | A single column of data with labels  | One column in a spreadsheet   |
| **DataFrame** | A table of data with rows and columns| An entire spreadsheet or table|

Think of a **Series** as a single list of values (like one column of student grades), and a **DataFrame** as a full table (like an entire gradebook with names, subjects, and scores).""",
                'exercise': None,
            },
            {
                'id': 'pandas-series',
                'title': 'Creating and Using Series',
                'content': """## Creating and Using Series

A **Series** is a one-dimensional labeled array. It is like a Python list, but each element has an associated label called an **index**.

### Creating a Series from a List

```python
import pandas as pd

# Daily temperatures for a week (in Fahrenheit)
temps = pd.Series([72, 75, 68, 71, 80])
print(temps)
```

Output:
```
0    72
1    75
2    68
3    71
4    80
dtype: int64
```

Notice that pandas automatically assigns numeric indices (0, 1, 2, ...) when you don't specify them.

### Creating a Series with Custom Index

In real life, data usually has meaningful labels. Imagine tracking daily temperatures for a workweek:

```python
temps = pd.Series([72, 75, 68, 71, 80],
                  index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(temps)
```

Output:
```
Mon    72
Tue    75
Wed    68
Thu    71
Fri    80
dtype: int64
```

### Creating a Series from a Dictionary

Dictionaries naturally map to Series since they already have key-value pairs:

```python
# Student grades in a class
grades = pd.Series({'Alice': 92, 'Bob': 85, 'Charlie': 78, 'Diana': 95})
print(grades)
```

### Basic Series Attributes and Methods

```python
temps = pd.Series([72, 75, 68, 71, 80],
                  index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])

print(temps.mean())    # 73.2 - average temperature
print(temps.max())     # 80 - hottest day
print(temps.min())     # 68 - coldest day
print(temps.sum())     # 366 - total of all temps
```

These simple methods save you from writing loops to calculate statistics - pandas does it in a single call.""",
                'exercise': {
                    'instructions': 'Create a pandas Series called `temps` from the given dictionary of daily temperatures. Then print the Series, its mean value, and its maximum value - each on a separate line.',
                    'starter_code': 'import pandas as pd\n\n# Daily temperatures (Fahrenheit) for a workweek\ntemp_data = {\'Mon\': 72, \'Tue\': 75, \'Wed\': 68, \'Thu\': 71, \'Fri\': 80}\n\n# Create a Series from the dictionary\ntemps = pd.Series(temp_data)\n\n# Print the Series\nprint(temps)\n\n# Print the mean temperature\nprint(temps.mean())\n\n# Print the maximum temperature\nprint(temps.max())\n',
                    'expected_output': 'Mon    72\nTue    75\nWed    68\nThu    71\nFri    80\ndtype: int64\n73.2\n80',
                    'hint': 'Pass the dictionary directly to pd.Series(). Use .mean() and .max() methods on the Series to compute statistics.',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this code will print? Type your guess!',
                    'code_snippet': 'import pandas as pd\ngrades = pd.Series({"Math": 90, "Science": 85, "Art": 95})\nprint(grades.max())',
                    'expected_output': '95',
                    'explanation': 'The .max() method finds the largest value in the Series. Among 90, 85, and 95, the maximum is 95 (the Art grade)!',
                },
            },
            {
                'id': 'creating-dataframes',
                'title': 'Creating DataFrames',
                'content': """## Creating DataFrames

A **DataFrame** is a two-dimensional table with labeled rows and columns - the primary data structure you will use in pandas. Think of it as a spreadsheet in code form.

### Creating a DataFrame from a Dictionary

The most common way to create a DataFrame is from a dictionary where each key becomes a column name and each value is a list of column data:

```python
import pandas as pd

# Employee records at a company
employees = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['Engineering', 'Marketing', 'Engineering'],
    'Salary': [75000, 65000, 80000]
})
print(employees)
```

Output:
```
      Name   Department  Salary
0    Alice  Engineering   75000
1      Bob    Marketing   65000
2  Charlie  Engineering   80000
```

### Real-Life Example: Sales Records

Imagine you manage a small online store and want to track recent orders:

```python
orders = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [999.99, 29.99, 79.99, 349.99],
    'Quantity': [5, 50, 30, 15]
})
print(orders)
```

Each row represents one product, and each column represents an attribute of that product - just like a row in your inventory spreadsheet.

### Key DataFrame Attributes

DataFrames have several useful attributes that tell you about your data at a glance:

```python
print(employees.shape)    # (3, 3) - 3 rows, 3 columns
print(employees.columns)  # Index(['Name', 'Department', 'Salary'], ...)
print(employees.dtypes)   # data type of each column
```

| Attribute   | Returns                              | Example Output       |
|-------------|--------------------------------------|----------------------|
| `.shape`    | Tuple of (rows, columns)             | `(3, 3)`             |
| `.columns`  | Column names                         | `Index(['Name', ...])` |
| `.dtypes`   | Data type of each column             | `Name object, ...`   |
| `.head(n)`  | First n rows (default 5)             | First 5 rows         |
| `.tail(n)`  | Last n rows (default 5)              | Last 5 rows          |
| `.info()`   | Summary of DataFrame                 | Types, non-null counts|""",
                'exercise': {
                    'instructions': 'Create a DataFrame called `employees` from the given dictionary. Print the DataFrame, then print the number of rows and columns using the `.shape` attribute with formatted output.',
                    'starter_code': 'import pandas as pd\n\n# Employee data\ndata = {\n    \'Name\': [\'Alice\', \'Bob\', \'Charlie\'],\n    \'Department\': [\'Engineering\', \'Marketing\', \'Engineering\'],\n    \'Salary\': [75000, 65000, 80000]\n}\n\n# Create the DataFrame\nemployees = pd.DataFrame(data)\n\n# Print the DataFrame\nprint(employees)\nprint()\n\n# Print the number of rows and columns\nprint(f"Rows: {employees.shape[0]}")\nprint(f"Columns: {employees.shape[1]}")\n',
                    'expected_output': '      Name   Department  Salary\n0    Alice  Engineering   75000\n1      Bob    Marketing   65000\n2  Charlie  Engineering   80000\n\nRows: 3\nColumns: 3',
                    'hint': 'Use pd.DataFrame(data) to create the DataFrame. Access .shape[0] for rows and .shape[1] for columns.',
                },
            },
            {
                'id': 'accessing-data',
                'title': 'Accessing Data in DataFrames',
                'content': """## Accessing Data in DataFrames

Once you have data in a DataFrame, you need to know how to access specific parts of it - just like looking up a particular cell, row, or column in a spreadsheet.

### Selecting Columns

Use bracket notation to select one or more columns:

```python
import pandas as pd

students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Grade': [92, 85, 78, 95],
    'Subject': ['Math', 'Science', 'Math', 'Science']
})

# Select a single column (returns a Series)
names = students['Name']
print(names)

# Select multiple columns (returns a DataFrame)
subset = students[['Name', 'Grade']]
print(subset)
```

### Selecting Rows by Index Position

Use `.iloc[]` (integer location) to select rows by their position number:

```python
# First row (index 0)
print(students.iloc[0])

# First two rows
print(students.iloc[0:2])
```

### Selecting Rows by Label

Use `.loc[]` to select rows by their label (index value):

```python
# If the index is meaningful (like student IDs)
students.index = ['S001', 'S002', 'S003', 'S004']
print(students.loc['S001'])
```

### Real-Life Analogy

Think of accessing DataFrame data like looking up information in a phone book:
- **Column selection** is like choosing which field you want (name, phone, address)
- **Row selection** is like finding a specific person's entry
- **Cell selection** is like finding one specific person's phone number

### Selecting Specific Cells

Combine row and column selection:

```python
# Get Bob's grade using iloc (row 1, column 1)
print(students.iloc[1, 1])  # 85

# Get Alice's subject using loc
print(students.loc['S001', 'Subject'])  # Math
```""",
                'exercise': None,
            },
            {
                'id': 'basic-dataframe-operations',
                'title': 'Basic DataFrame Operations',
                'content': """## Basic DataFrame Operations

Pandas makes it easy to add new columns, perform calculations across entire columns, and get quick summaries of your data.

### Adding New Columns

You can create a new column by assigning values to a new column name - just like adding a new column to a spreadsheet:

```python
import pandas as pd

# Product inventory
products = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [999, 29, 79],
    'Quantity': [10, 100, 50]
})

# Add a column calculated from existing columns
products['Total_Value'] = products['Price'] * products['Quantity']
print(products)
```

### Descriptive Statistics

The `.describe()` method gives you a statistical summary of all numeric columns at once:

```python
print(products.describe())
```

This instantly tells you the count, mean, standard deviation, min, max, and quartiles - statistics that would take many lines of manual code to compute.

### Sorting Data

Sort your data by any column, just like sorting a spreadsheet:

```python
# Sort by price (ascending by default)
sorted_products = products.sort_values('Price')

# Sort by price descending (most expensive first)
sorted_products = products.sort_values('Price', ascending=False)
print(sorted_products)
```

### Real-Life Example: Student Gradebook

Imagine you are a teacher computing final grades:

```python
gradebook = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Midterm': [88, 75, 92],
    'Final': [90, 82, 88]
})

# Compute weighted average (40% midterm, 60% final)
gradebook['Weighted_Avg'] = (gradebook['Midterm'] * 0.4 +
                              gradebook['Final'] * 0.6)
print(gradebook)
```

This kind of column-wise calculation is where pandas truly shines compared to writing manual loops.""",
                'exercise': {
                    'instructions': 'Create a DataFrame of products with Price and Quantity columns. Add a new column called "Revenue" that equals Price times Quantity. Then sort the DataFrame by Revenue in descending order and print the sorted result.',
                    'starter_code': 'import pandas as pd\n\n# Product sales data\nproducts = pd.DataFrame({\n    \'Product\': [\'Laptop\', \'Mouse\', \'Keyboard\', \'Monitor\'],\n    \'Price\': [999, 29, 79, 349],\n    \'Quantity\': [5, 50, 30, 15]\n})\n\n# Add a Revenue column (Price * Quantity)\nproducts[\'Revenue\'] = products[\'Price\'] * products[\'Quantity\']\n\n# Sort by Revenue in descending order\nsorted_products = products.sort_values(\'Revenue\', ascending=False)\n\n# Print the sorted DataFrame\nprint(sorted_products)\n',
                    'expected_output': '   Product  Price  Quantity  Revenue\n0   Laptop    999         5     4995\n3  Monitor    349        15     5235\n2  Keyboard     79        30     2370\n1    Mouse     29        50     1450',
                    'hint': 'Multiply the Price and Quantity columns using products[\'Price\'] * products[\'Quantity\']. Use sort_values(\'Revenue\', ascending=False) to sort from highest to lowest.',
                },
                'game': {
                    'type': 'fill_blank',
                    'instructions': 'Fill in the blanks to create a DataFrame and add a new column:',
                    'code_template': 'import {0} as pd\ndf = pd.{1}({{"Name": ["Alice", "Bob"], "Score": [90, 85]}})\ndf["Grade"] = df["{2}"].apply(lambda x: "A" if x >= 90 else "B")\nprint(df)',
                    'blanks': [
                        {'id': 0, 'answer': 'pandas', 'hint': 'What library do we import for DataFrames?'},
                        {'id': 1, 'answer': 'DataFrame', 'hint': 'What class creates a table from a dictionary?'},
                        {'id': 2, 'answer': 'Score', 'hint': 'Which column do we use to calculate grades?'},
                    ],
                    'explanation': 'We import pandas as pd, use pd.DataFrame() to create a table, and then add a new "Grade" column based on the "Score" column!',
                },
            },
        ],
    },
    {
        'title': 'Data Selection, Filtering, and Cleaning',
        'description': 'Master the art of selecting specific data with loc and iloc, filtering rows based on conditions, and handling missing data - essential skills for any real-world dataset.',
        'order': 2,
        'item_order': 3,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'loc-and-iloc',
                'title': 'Selecting Data with loc and iloc',
                'content': """## Selecting Data with loc and iloc

When working with real datasets, you rarely need every single row and column. Pandas provides two powerful tools for precise data selection: **`loc`** (label-based) and **`iloc`** (integer position-based).

### iloc: Integer-Based Selection

Use `iloc` when you know the position (row number, column number) of the data you want. This is like saying "give me row 2, column 3" in a spreadsheet:

```python
import pandas as pd

products = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [999, 699, 399, 299],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories']
})

# Single value: row 0, column 1
print(products.iloc[0, 1])  # 999

# Slice of rows
print(products.iloc[0:2])   # first two rows

# Specific rows and columns
print(products.iloc[[0, 3], [0, 1]])  # rows 0 and 3, columns 0 and 1
```

### loc: Label-Based Selection

Use `loc` when you want to select by column names and index labels. This is more readable and less error-prone:

```python
# Select specific columns for specific rows
print(products.loc[0:1, ['Product', 'Price']])

# Select a single value
print(products.loc[1, 'Product'])  # Phone
```

### Real-Life Example: Employee Directory

Imagine an HR system where you need to look up specific employee records:

```python
employees = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['Engineering', 'Marketing', 'Engineering', 'Sales'],
    'Salary': [95000, 72000, 88000, 78000]
})

# Get the first two employees' names and departments
print(employees.loc[0:1, ['Name', 'Department']])
```

### When to Use Which?

| Method | Best For                                    | Example                       |
|--------|---------------------------------------------|-------------------------------|
| `iloc` | Selecting by position (first 5 rows, etc.)  | `df.iloc[0:5]`               |
| `loc`  | Selecting by column names and labels         | `df.loc[0:5, ['Name', 'Age']]`|

**Tip:** When in doubt, use `loc` because it makes your code more readable by using column names instead of numbers.""",
                'exercise': {
                    'instructions': 'Use iloc to select the first two rows of the products DataFrame and print them. Then use boolean filtering to find products with Price greater than 500, and print only the Product and Price columns of those results.',
                    'starter_code': 'import pandas as pd\n\nproducts = pd.DataFrame({\n    \'Product\': [\'Laptop\', \'Phone\', \'Tablet\', \'Monitor\'],\n    \'Price\': [999, 699, 399, 299],\n    \'Category\': [\'Electronics\', \'Electronics\', \'Electronics\', \'Accessories\']\n})\n\n# Select first two rows using iloc\nfirst_two = products.iloc[0:2]\nprint(first_two)\nprint()\n\n# Filter products with Price > 500 and show only Product and Price\nexpensive = products[products[\'Price\'] > 500]\nprint(expensive[[\'Product\', \'Price\']])\n',
                    'expected_output': '  Product  Price     Category\n0  Laptop    999  Electronics\n1   Phone    699  Electronics\n\n  Product  Price\n0  Laptop    999\n1   Phone    699',
                    'hint': 'Use products.iloc[0:2] for the first two rows. For filtering, use products[products[\'Price\'] > 500] and then select only the columns you need with [[\'Product\', \'Price\']].',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Think about the difference between loc and iloc:',
                    'code_snippet': 'import pandas as pd\ndf = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})\n# Using iloc vs loc',
                    'question': 'What does df.iloc[0, 1] return?',
                    'options': [
                        {'text': '25 (first row, second column by position)', 'correct': True},
                        {'text': 'Alice (first row, first column)', 'correct': False},
                        {'text': 'Error (iloc needs column names)', 'correct': False},
                        {'text': '30 (second row, first column)', 'correct': False},
                    ],
                    'explanation': 'iloc uses integer positions! Row 0 is Alice\'s row, column 1 is Age. So df.iloc[0, 1] returns 25 (Alice\'s age).',
                },
            },
            {
                'id': 'boolean-filtering',
                'title': 'Boolean Filtering and Conditions',
                'content': """## Boolean Filtering and Conditions

**Boolean filtering** is one of the most powerful features in pandas. It lets you ask questions about your data and get back only the rows that match - like applying a filter in a spreadsheet, but much more flexible.

### How Boolean Filtering Works

When you write a condition on a DataFrame column, pandas creates a Series of `True`/`False` values:

```python
import pandas as pd

sales = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'Price': [999, 29, 79, 349, 59],
    'Units_Sold': [10, 200, 80, 25, 150]
})

# This creates a boolean Series
mask = sales['Price'] > 100
print(mask)
# 0     True
# 1    False
# 2    False
# 3     True
# 4    False
```

When you pass this boolean Series back into the DataFrame, it returns only the rows where the condition is `True`:

```python
expensive = sales[sales['Price'] > 100]
print(expensive)
```

### Combining Multiple Conditions

Use `&` (and) and `|` (or) to combine conditions. **Important:** Each condition must be in parentheses:

```python
# Products that are expensive AND sold well
hot_sellers = sales[(sales['Price'] > 50) & (sales['Units_Sold'] > 50)]

# Products that are cheap OR sold many units
popular = sales[(sales['Price'] < 100) | (sales['Units_Sold'] > 100)]
```

### Real-Life Example: Filtering a Customer Database

Imagine you run an online store and want to find your best customers:

```python
customers = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Total_Spent': [1200, 450, 3000, 780, 5500],
    'Orders': [15, 5, 40, 10, 60]
})

# Find VIP customers (spent over $1000)
vips = customers[customers['Total_Spent'] > 1000]
print(vips[['Name', 'Total_Spent']])
```

### String Filtering

You can also filter by string content:

```python
# Find products that contain 'board' in the name
boards = sales[sales['Product'].str.contains('board')]

# Find products starting with 'M'
m_products = sales[sales['Product'].str.startswith('M')]
```""",
                'exercise': {
                    'instructions': 'Filter the sales DataFrame to find products where the Price is less than 100 AND Units_Sold is greater than 100. Print the filtered result showing all columns.',
                    'starter_code': 'import pandas as pd\n\nsales = pd.DataFrame({\n    \'Product\': [\'Laptop\', \'Mouse\', \'Keyboard\', \'Monitor\', \'Webcam\'],\n    \'Price\': [999, 29, 79, 349, 59],\n    \'Units_Sold\': [10, 200, 80, 25, 150]\n})\n\n# Filter: Price < 100 AND Units_Sold > 100\nresult = sales[(sales[\'Price\'] < 100) & (sales[\'Units_Sold\'] > 100)]\n\n# Print the filtered result\nprint(result)\n',
                    'expected_output': '  Product  Price  Units_Sold\n1   Mouse     29         200\n4  Webcam     59         150',
                    'hint': 'Use the & operator to combine two conditions. Remember to wrap each condition in parentheses: (sales[\'Price\'] < 100) & (sales[\'Units_Sold\'] > 100).',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'How many rows will the filter return? Type just the number!',
                    'code_snippet': 'import pandas as pd\ndf = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Score": [90, 60, 85, 45]})\nresult = df[df["Score"] > 70]\nprint(len(result))',
                    'expected_output': '2',
                    'explanation': 'df["Score"] > 70 checks each score: 90>70 (True), 60>70 (False), 85>70 (True), 45>70 (False). Only 2 rows pass the filter (A and C)!',
                },
            },
            {
                'id': 'handling-missing-data',
                'title': 'Handling Missing Data',
                'content': """## Handling Missing Data

In the real world, data is almost never perfect. Survey respondents skip questions, sensors malfunction, and databases have gaps. Pandas represents missing data as **`NaN`** (Not a Number) and provides powerful tools to deal with it.

### Why Missing Data Matters

Consider a teacher collecting exam scores. Some students were absent for certain exams:

```python
import pandas as pd
import numpy as np

scores = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Math': [85, np.nan, 92, 78],
    'Science': [90, 88, np.nan, 95]
})
print(scores)
```

Output:
```
   Student  Math  Science
0    Alice  85.0     90.0
1      Bob   NaN     88.0
2  Charlie  92.0      NaN
3    Diana  78.0     95.0
```

Notice that `NaN` appears where data is missing. The other values become `float` because `NaN` is technically a float value.

### Detecting Missing Data

```python
# Check for missing values (True where data is missing)
print(scores.isnull())

# Count missing values per column
print(scores.isnull().sum())
```

### Strategies for Handling Missing Data

You have three main options:

**1. Drop rows with missing data (`dropna`)**

This is the simplest approach, but you lose data:

```python
clean = scores.dropna()
print(clean)  # Only Alice and Diana remain
```

**2. Fill missing values with a specific value (`fillna`)**

Replace NaN with zero, the mean, or another sensible default:

```python
# Fill with zero
filled = scores.fillna(0)

# Fill with column mean (smarter default)
scores['Math'] = scores['Math'].fillna(scores['Math'].mean())
```

**3. Forward/backward fill**

Use the previous or next valid value:

```python
# Forward fill: use previous row's value
scores.fillna(method='ffill')
```

### Choosing the Right Strategy

| Strategy     | When to Use                                | Trade-off            |
|-------------|---------------------------------------------|----------------------|
| `dropna()`  | Few missing values, large dataset           | Loses rows           |
| `fillna(0)` | Missing means "none" (e.g., no sales = 0)   | May skew statistics  |
| `fillna(mean)` | Missing is unknown, want neutral impact | Reduces variance     |""",
                'exercise': {
                    'instructions': 'Count the missing values per column in the survey DataFrame and print the result. Then drop all rows that contain any missing values and print the cleaned DataFrame.',
                    'starter_code': 'import pandas as pd\nimport numpy as np\n\n# Survey responses with missing data\nsurvey = pd.DataFrame({\n    \'Student\': [\'Alice\', \'Bob\', \'Charlie\', \'Diana\'],\n    \'Math\': [85.0, np.nan, 92.0, 78.0],\n    \'Science\': [90.0, 88.0, np.nan, 95.0]\n})\n\n# Count missing values per column\nprint(survey.isnull().sum())\nprint()\n\n# Drop rows with any missing values\nsurvey_clean = survey.dropna()\nprint(survey_clean)\n',
                    'expected_output': 'Student    0\nMath       1\nScience    1\ndtype: int64\n\n  Student  Math  Science\n0   Alice  85.0     90.0\n3   Diana  78.0     95.0',
                    'hint': 'Use .isnull().sum() to count missing values per column. Use .dropna() to remove rows that have any NaN values.',
                },
            },
            {
                'id': 'adding-and-removing-columns',
                'title': 'Adding and Removing Columns',
                'content': """## Adding and Removing Columns

As you work with data, you often need to reshape it - adding calculated fields, renaming columns for clarity, or dropping columns you no longer need.

### Adding Columns

You have already seen how to add a calculated column. Here are more patterns:

```python
import pandas as pd

orders = pd.DataFrame({
    'Item': ['Widget', 'Gadget', 'Doohickey'],
    'Price': [10.00, 25.50, 7.99],
    'Quantity': [100, 50, 200]
})

# Calculated column
orders['Total'] = orders['Price'] * orders['Quantity']

# Constant column (same value for all rows)
orders['Currency'] = 'USD'

# Conditional column using apply
orders['Size'] = orders['Quantity'].apply(
    lambda q: 'Large' if q >= 100 else 'Small'
)
print(orders)
```

### Removing Columns

Use the `.drop()` method to remove columns:

```python
# Drop a single column
orders = orders.drop('Currency', axis=1)

# Drop multiple columns
orders = orders.drop(['Size', 'Total'], axis=1)
```

**Note:** `axis=1` means "operate on columns." `axis=0` means "operate on rows."

### Renaming Columns

Rename columns for clarity - especially useful when column names come from messy data sources:

```python
orders = orders.rename(columns={
    'Item': 'Product_Name',
    'Price': 'Unit_Price'
})
```

### Real-Life Example: Cleaning Sales Data

When you receive data from a database or CSV file, columns often have unfriendly names:

```python
raw_data = pd.DataFrame({
    'cust_nm': ['Alice', 'Bob'],
    'ord_amt': [150.00, 89.50],
    'ord_dt': ['2024-01-15', '2024-01-16']
})

# Make column names human-readable
clean_data = raw_data.rename(columns={
    'cust_nm': 'Customer_Name',
    'ord_amt': 'Order_Amount',
    'ord_dt': 'Order_Date'
})
print(clean_data)
```""",
                'exercise': None,
            },
            {
                'id': 'practical-data-cleaning',
                'title': 'Practical Data Cleaning Workflow',
                'content': """## Practical Data Cleaning Workflow

In real-world data analysis, data cleaning often involves multiple steps performed in sequence. Let us walk through a realistic scenario.

### Scenario: Cleaning Customer Order Data

Imagine you received a spreadsheet of customer orders that has messy column names, missing values, and needs a calculated field:

```python
import pandas as pd
import numpy as np

orders = pd.DataFrame({
    'cust': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'product': ['Laptop', 'Phone', np.nan, 'Tablet', 'Laptop'],
    'price': [999.0, 699.0, np.nan, 399.0, 999.0],
    'qty': [1, 2, 1, np.nan, 1]
})
```

### Step-by-Step Cleaning Process

```python
# Step 1: Rename columns for clarity
orders = orders.rename(columns={
    'cust': 'Customer',
    'product': 'Product',
    'price': 'Price',
    'qty': 'Quantity'
})

# Step 2: Check for missing data
print(orders.isnull().sum())

# Step 3: Drop rows where essential data is missing
orders = orders.dropna(subset=['Product', 'Price'])

# Step 4: Fill remaining missing values
orders['Quantity'] = orders['Quantity'].fillna(1)

# Step 5: Add calculated column
orders['Total'] = orders['Price'] * orders['Quantity']

print(orders)
```

### Key Takeaways

1. **Always inspect your data first** - use `.info()`, `.isnull().sum()`, and `.head()` before doing anything
2. **Clean in stages** - rename, handle missing data, then calculate
3. **Document your decisions** - why did you drop rows vs. fill values?
4. **Keep a copy of the original** - in case you need to go back

Data cleaning is often called the "80/20 rule" of data science: 80% of your time is spent cleaning data, and only 20% on actual analysis. Mastering these pandas tools will save you enormous amounts of time.""",
                'exercise': None,
            },
        ],
    },
    {
        'title': 'GroupBy and Aggregation',
        'description': 'Learn to group data by categories and compute summary statistics - the pandas equivalent of pivot tables that let you answer questions like "what are total sales by region?"',
        'order': 3,
        'item_order': 6,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'intro-to-groupby',
                'title': 'Introduction to GroupBy',
                'content': """## Introduction to GroupBy

The **`groupby()`** operation is one of the most powerful features in pandas. It lets you split your data into groups based on a column, apply a calculation to each group, and combine the results.

### The Split-Apply-Combine Pattern

Every groupby operation follows three steps:

1. **Split** - Divide the data into groups based on one or more columns
2. **Apply** - Perform a calculation (sum, mean, count, etc.) on each group
3. **Combine** - Merge the results back into a single output

### Real-Life Example: Sales by Region

Imagine you are a sales manager reviewing quarterly performance across regions:

```python
import pandas as pd

sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Product': ['Widget', 'Widget', 'Gadget', 'Gadget', 'Widget'],
    'Sales': [200, 150, 300, 250, 180]
})

# Total sales by region
region_totals = sales.groupby('Region')['Sales'].sum()
print(region_totals)
```

Output:
```
Region
East    680
West    400
Name: Sales, dtype: int64
```

This instantly tells you that the East region has higher total sales ($680) compared to the West ($400).

### Common Aggregation Functions

After grouping, you can apply various aggregate functions:

```python
# Average sales per region
print(sales.groupby('Region')['Sales'].mean())

# Count of transactions per region
print(sales.groupby('Region')['Sales'].count())

# Maximum single sale per region
print(sales.groupby('Region')['Sales'].max())
```

### Analogy: GroupBy is Like Sorting Papers into Folders

Think of groupby like an office worker sorting invoices:
1. **Split**: Sort all invoices into folders by department
2. **Apply**: Calculate the total for each folder
3. **Combine**: Create a summary sheet with one row per department

This is exactly what `groupby().sum()` does with your data.""",
                'exercise': {
                    'instructions': 'Use groupby to calculate the total Sales by Region and print the result. Then calculate the average Sales by Region and print that result.',
                    'starter_code': 'import pandas as pd\n\nsales = pd.DataFrame({\n    \'Region\': [\'East\', \'West\', \'East\', \'West\', \'East\'],\n    \'Product\': [\'Widget\', \'Widget\', \'Gadget\', \'Gadget\', \'Widget\'],\n    \'Sales\': [200, 150, 300, 250, 180]\n})\n\n# Total sales by region\nregion_totals = sales.groupby(\'Region\')[\'Sales\'].sum()\nprint(region_totals)\nprint()\n\n# Average sales by region\nregion_avg = sales.groupby(\'Region\')[\'Sales\'].mean()\nprint(region_avg)\n',
                    'expected_output': 'Region\nEast    680\nWest    400\nName: Sales, dtype: int64\n\nRegion\nEast    226.666667\nWest    200.000000\nName: Sales, dtype: float64',
                    'hint': 'Use sales.groupby(\'Region\')[\'Sales\'].sum() for totals and .mean() for averages.',
                },
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange these steps in the correct order to group data and calculate totals:',
                    'code_blocks': [
                        'import pandas as pd',
                        'sales = pd.DataFrame({"Region": ["East", "West", "East"], "Amount": [100, 200, 150]})',
                        'totals = sales.groupby("Region")["Amount"].sum()',
                        'print(totals)',
                    ],
                    'explanation': 'First import pandas, then create the DataFrame, use groupby() to group by Region and sum the amounts, then print the result!',
                },
            },
            {
                'id': 'multiple-aggregations',
                'title': 'Multiple Aggregations with agg()',
                'content': """## Multiple Aggregations with agg()

Often you need more than one statistic per group. The **`agg()`** method lets you apply multiple aggregate functions at once.

### Using agg() with a List

```python
import pandas as pd

orders = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Charlie'],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Laptop', 'Phone'],
    'Amount': [999, 699, 399, 999, 999, 699]
})

# Multiple stats for each customer
summary = orders.groupby('Customer')['Amount'].agg(['sum', 'count'])
print(summary)
```

Output:
```
           sum  count
Customer
Alice     1398      2
Bob       1698      2
Charlie   1698      2
```

This tells you at a glance how much each customer spent and how many orders they placed.

### Using agg() with a Dictionary

Apply different aggregations to different columns:

```python
sales = pd.DataFrame({
    'Store': ['Downtown', 'Mall', 'Downtown', 'Mall', 'Downtown'],
    'Revenue': [500, 300, 450, 600, 550],
    'Customers': [50, 30, 45, 60, 55]
})

result = sales.groupby('Store').agg({
    'Revenue': 'sum',
    'Customers': 'mean'
})
print(result)
```

### Real-Life Example: Student Performance Report

A principal wants to see how each subject is performing across the school:

```python
grades = pd.DataFrame({
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math'],
    'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie'],
    'Score': [92, 78, 85, 90, 88]
})

report = grades.groupby('Subject')['Score'].agg(['mean', 'min', 'max'])
print(report)
```

This creates a quick report card for each subject showing the class average, lowest, and highest scores.

### Named Aggregations (Cleaner Output)

For cleaner column names in the result, use named aggregations:

```python
result = grades.groupby('Subject')['Score'].agg(
    Average='mean',
    Lowest='min',
    Highest='max'
)
print(result)
```""",
                'exercise': {
                    'instructions': 'Group the orders by Customer and use agg() to calculate both the sum and count of the Amount column. Print the resulting summary table.',
                    'starter_code': 'import pandas as pd\n\norders = pd.DataFrame({\n    \'Customer\': [\'Alice\', \'Bob\', \'Alice\', \'Charlie\', \'Bob\', \'Charlie\'],\n    \'Product\': [\'Laptop\', \'Phone\', \'Tablet\', \'Laptop\', \'Laptop\', \'Phone\'],\n    \'Amount\': [999, 699, 399, 999, 999, 699]\n})\n\n# Group by Customer and aggregate Amount with sum and count\nsummary = orders.groupby(\'Customer\')[\'Amount\'].agg([\'sum\', \'count\'])\n\n# Print the summary\nprint(summary)\n',
                    'expected_output': '           sum  count\nCustomer             \nAlice     1398      2\nBob       1698      2\nCharlie   1698      2',
                    'hint': 'Use .groupby(\'Customer\')[\'Amount\'].agg([\'sum\', \'count\']) to calculate multiple statistics at once.',
                },
            },
            {
                'id': 'groupby-multiple-columns',
                'title': 'Grouping by Multiple Columns',
                'content': """## Grouping by Multiple Columns

You can group by more than one column to get more granular insights. This is like creating a pivot table with multiple row headers in a spreadsheet.

### Example: Sales by Region AND Product

```python
import pandas as pd

sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'Product': ['Widget', 'Widget', 'Gadget', 'Widget', 'Widget', 'Gadget'],
    'Revenue': [200, 150, 300, 180, 220, 250]
})

# Group by both Region and Product
breakdown = sales.groupby(['Region', 'Product'])['Revenue'].sum()
print(breakdown)
```

This creates a hierarchical index showing revenue for every region-product combination.

### Using reset_index()

The result of groupby has the grouped columns as the index. Use `reset_index()` to turn them back into regular columns:

```python
breakdown = sales.groupby(['Region', 'Product'])['Revenue'].sum().reset_index()
print(breakdown)
```

### Real-Life Example: Average Grades by Student and Subject

A school administrator wants to see each student's average per subject:

```python
grades = pd.DataFrame({
    'Student': ['Alice', 'Alice', 'Bob', 'Bob'],
    'Subject': ['Math', 'Science', 'Math', 'Science'],
    'Grade': [90, 85, 78, 92]
})

avg_grades = grades.groupby('Subject')['Grade'].mean()
print(avg_grades)
```

This quickly answers questions like "which subject has the highest average grade?" without writing complex loops.""",
                'exercise': None,
            },
            {
                'id': 'basic-merging',
                'title': 'Basic DataFrame Merging',
                'content': """## Basic DataFrame Merging

In real-world projects, data is often stored across multiple tables or files. **Merging** (also called **joining**) combines two DataFrames based on a shared column - similar to the VLOOKUP function in Excel.

### Why Merge?

Consider an e-commerce system:
- One table has **customer information** (name, city)
- Another table has **order totals** per customer

You need to combine them to answer questions like "which city has the highest total orders?"

### pd.merge() Basics

```python
import pandas as pd

customers = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie'],
    'City': ['New York', 'Chicago', 'Houston']
})

orders = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie'],
    'Total': [1398, 1698, 1698]
})

# Merge on the shared 'Customer' column
merged = pd.merge(customers, orders, on='Customer')
print(merged)
```

Output:
```
  Customer      City  Total
0    Alice  New York   1398
1      Bob   Chicago   1698
2  Charlie   Houston   1698
```

### Types of Merges

Pandas supports different merge types, similar to SQL joins:

| Type     | Keeps                                    | Use When                          |
|----------|------------------------------------------|-----------------------------------|
| `inner`  | Only matching rows (default)             | You want complete records only    |
| `left`   | All rows from left DataFrame             | Left table is your primary data   |
| `right`  | All rows from right DataFrame            | Right table is your primary data  |
| `outer`  | All rows from both DataFrames            | You want everything, gaps are OK  |

```python
# Left merge - keep all customers even if they have no orders
merged = pd.merge(customers, orders, on='Customer', how='left')
```

### Real-Life Example: Combining Student Info with Grades

A school might have student contact info in one file and grades in another:

```python
students = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [20, 21]
})

scores = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'GPA': [3.8, 3.5]
})

combined = pd.merge(students, scores, on='Name')
print(combined)
```""",
                'exercise': {
                    'instructions': 'Merge the customers DataFrame with the total_by_customer DataFrame on the Customer column. Print the merged result.',
                    'starter_code': 'import pandas as pd\n\ncustomers = pd.DataFrame({\n    \'Customer\': [\'Alice\', \'Bob\', \'Charlie\'],\n    \'City\': [\'New York\', \'Chicago\', \'Houston\']\n})\n\ntotal_by_customer = pd.DataFrame({\n    \'Customer\': [\'Alice\', \'Bob\', \'Charlie\'],\n    \'Total\': [1398, 1698, 1698]\n})\n\n# Merge the two DataFrames on Customer\nmerged = pd.merge(customers, total_by_customer, on=\'Customer\')\n\n# Print the merged result\nprint(merged)\n',
                    'expected_output': '  Customer      City  Total\n0    Alice  New York   1398\n1      Bob   Chicago   1698\n2  Charlie   Houston   1698',
                    'hint': 'Use pd.merge(customers, total_by_customer, on=\'Customer\') to join the two DataFrames on their shared column.',
                },
            },
            {
                'id': 'groupby-and-merge-workflow',
                'title': 'Putting It All Together: GroupBy + Merge',
                'content': """## Putting It All Together: GroupBy + Merge

Real data analysis often requires chaining multiple pandas operations. Let us walk through a complete example that combines groupby, aggregation, and merging.

### Scenario: Monthly Sales Report

You are a business analyst preparing a report. You have order data and need to create a summary by customer, then combine it with customer location data.

```python
import pandas as pd

# Order records
orders = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Product': ['Laptop', 'Phone', 'Mouse', 'Laptop', 'Tablet'],
    'Amount': [999, 699, 29, 999, 399]
})

# Step 1: Group by customer and get total + count
customer_summary = orders.groupby('Customer')['Amount'].agg(
    Total_Spent='sum',
    Num_Orders='count'
).reset_index()

print("Customer Summary:")
print(customer_summary)
```

```python
# Customer locations
locations = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie'],
    'City': ['New York', 'Chicago', 'Houston']
})

# Step 2: Merge summary with locations
report = pd.merge(customer_summary, locations, on='Customer')
print("\\nFull Report:")
print(report)
```

### The Power of Chaining

Notice how each step builds on the previous one:
1. Raw data -> GroupBy -> Summary statistics
2. Summary + Location -> Merge -> Complete report

This is the typical workflow in data analysis: **transform, aggregate, combine, and present**.

### Key Takeaways

- `groupby()` splits data into groups and applies calculations
- `agg()` lets you compute multiple statistics at once
- `pd.merge()` combines DataFrames on shared columns
- These three operations together can answer almost any business question about structured data
- Always use `reset_index()` after groupby if you want a clean DataFrame for merging""",
                'exercise': None,
            },
        ],
    },
]
