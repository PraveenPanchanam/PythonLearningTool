CHAPTER_ORDER = 9

LESSONS = [
    # ------------------------------------------------------------------ #
    # Lesson 1 -- Introduction to NumPy Arrays
    # ------------------------------------------------------------------ #
    {
        'title': 'Introduction to NumPy Arrays',
        'description': 'Learn the fundamentals of NumPy -- Python\'s powerhouse library for numerical computing. Create arrays, explore their attributes, and use essential creation functions.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'what-is-numpy',
                'title': 'What Is NumPy and Why Use It?',
                'content': """## What Is NumPy and Why Use It?

**NumPy** (Numerical Python) is the foundation of scientific computing in Python. It provides a powerful array object and a collection of mathematical functions that operate on arrays at blazing speed.

### Real-Life Analogy

Think of a Python list as a general-purpose toolbox -- it can hold any mix of items (screwdrivers, hammers, tape, snacks). A NumPy array is like a specialized parts organizer where every slot holds the same type of component. This specialization makes it extremely efficient for bulk operations.

### Why NumPy Over Regular Lists?

1. **Speed:** NumPy operations run 10 to 100 times faster than equivalent Python loops because they are implemented in optimized C code.
2. **Memory efficiency:** NumPy arrays store data in contiguous memory blocks, unlike lists which store pointers to scattered objects.
3. **Vectorized operations:** You can perform math on entire arrays without writing loops.
4. **Industry standard:** Pandas, scikit-learn, TensorFlow, and every major data science library is built on NumPy.

### Real-World Applications

| Domain | NumPy Use Case |
|--------|---------------|
| Finance | Stock price arrays, portfolio calculations |
| Healthcare | Medical image pixel data (MRI, X-ray) |
| Weather | Temperature sensor readings across stations |
| E-commerce | Product rating matrices, recommendation scores |
| Gaming | 3D coordinate transformations |

### Importing NumPy

The universally accepted convention is:

```python
import numpy as np
```

Every NumPy tutorial, textbook, and codebase uses `np` as the alias. Always follow this convention.""",
                'exercise': None,
            },
            {
                'id': 'creating-arrays',
                'title': 'Creating NumPy Arrays',
                'content': """## Creating NumPy Arrays

### From Python Lists

The most common way to create an array is from an existing Python list:

```python
import numpy as np

# 1D array -- like a row of sensor readings
temperatures = np.array([72.5, 68.3, 75.1, 69.8, 71.2])
print(temperatures)
# [72.5 68.3 75.1 69.8 71.2]

# 2D array -- like a spreadsheet or image pixel grid
sales_data = np.array([
    [150, 200, 175],   # Store A: Jan, Feb, Mar
    [180, 160, 210],   # Store B: Jan, Feb, Mar
    [130, 190, 185],   # Store C: Jan, Feb, Mar
])
print(sales_data)
# [[150 200 175]
#  [180 160 210]
#  [130 190 185]]
```

**Important:** Notice that NumPy prints arrays with **spaces between elements, not commas**. This is different from Python lists.

### From Python Lists of Different Types

NumPy arrays hold **one data type** only. If you mix types, NumPy will convert (upcast) them:

```python
# Mixed int and float -- all become float
mixed = np.array([1, 2, 3.5, 4])
print(mixed)        # [1.  2.  3.5 4. ]
print(mixed.dtype)  # float64
```

### Real-Life Example: Stock Prices

```python
import numpy as np

# Daily closing prices for a stock over one week
stock_prices = np.array([142.50, 143.75, 141.20, 145.80, 144.60])
print(stock_prices)
# [142.5  143.75 141.2  145.8  144.6 ]
```""",
                'exercise': {
                    'instructions': 'Create a 1D NumPy array called `scores` from the list [85, 92, 78, 95, 88] representing student test scores. Then create a 2D array called `grid` from a 2x3 nested list [[1, 2, 3], [4, 5, 6]]. Print both arrays.',
                    'starter_code': 'import numpy as np\n\n# Create a 1D array of student test scores\nscores = np.array([85, 92, 78, 95, 88])\nprint(scores)\n\n# Create a 2D array (2 rows, 3 columns)\ngrid = np.array([[1, 2, 3], [4, 5, 6]])\nprint(grid)\n',
                    'expected_output': '[85 92 78 95 88]\n[[1 2 3]\n [4 5 6]]',
                    'hint': 'Use np.array() with a list to create a 1D array. For a 2D array, pass a list of lists where each inner list is a row.',
                },
                'game': {
                    'type': 'fill_blank',
                    'instructions': 'Fill in the blanks to create a NumPy array and print its shape:',
                    'code_template': 'import {0} as np\ndata = np.{1}([10, 20, 30])\nprint(data.{2})',
                    'blanks': [
                        {'id': 0, 'answer': 'numpy', 'hint': 'What library do we import for arrays?'},
                        {'id': 1, 'answer': 'array', 'hint': 'What function creates an array from a list?'},
                        {'id': 2, 'answer': 'shape', 'hint': 'What attribute tells us the array dimensions?'},
                    ],
                    'explanation': 'We import numpy as np, use np.array() to create an array from a list, and .shape tells us the dimensions — (3,) for a 1D array with 3 elements!',
                },
            },
            {
                'id': 'array-attributes',
                'title': 'Array Attributes',
                'content': """## Array Attributes

Every NumPy array carries metadata that describes its structure. Understanding these attributes is essential for working with arrays effectively.

### Key Attributes

```python
import numpy as np

# Imagine this is daily temperature data from 3 weather stations over 4 days
weather_data = np.array([
    [72, 68, 75, 70],  # Station A
    [65, 63, 67, 64],  # Station B
    [80, 78, 82, 79],  # Station C
])

print(f"Shape: {weather_data.shape}")      # (3, 4) -- 3 rows, 4 columns
print(f"Dimensions: {weather_data.ndim}")  # 2 -- it is a 2D array
print(f"Size: {weather_data.size}")        # 12 -- total number of elements
print(f"Data type: {weather_data.dtype}")  # int64 -- 64-bit integers
```

### Shape Tells You the Structure

The `shape` attribute is a tuple describing the array's dimensions:

```python
# 1D array (vector)
prices = np.array([10.5, 20.3, 30.1])
print(prices.shape)  # (3,) -- 3 elements, 1 dimension

# 2D array (matrix)
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix.shape)  # (3, 2) -- 3 rows, 2 columns

# 3D array (e.g., RGB image: height x width x channels)
image = np.zeros((100, 200, 3))
print(image.shape)  # (100, 200, 3) -- 100 pixels tall, 200 wide, 3 color channels
```

### Data Types (dtype)

NumPy arrays are strongly typed. Common types:

| dtype | Description | Example |
|-------|-------------|---------|
| `int64` | 64-bit integer | Counts, IDs |
| `float64` | 64-bit float | Prices, measurements |
| `bool` | Boolean | Flags, masks |
| `str_` | String | Labels (rarely used) |

```python
# Specify dtype explicitly
ids = np.array([101, 102, 103], dtype=np.int32)
prices = np.array([9.99, 19.99, 29.99], dtype=np.float64)

print(ids.dtype)     # int32
print(prices.dtype)  # float64
```""",
                'exercise': {
                    'instructions': 'Create a 2D NumPy array called `data` with 3 rows and 4 columns using the values [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]. Print the shape, number of dimensions, total size, and data type of the array.',
                    'starter_code': 'import numpy as np\n\n# Create a 2D array\ndata = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])\n\n# Print array attributes\nprint(f"Shape: {data.shape}")\nprint(f"Dimensions: {data.ndim}")\nprint(f"Size: {data.size}")\nprint(f"Dtype: {data.dtype}")\n',
                    'expected_output': 'Shape: (3, 4)\nDimensions: 2\nSize: 12\nDtype: int64',
                    'hint': 'Access attributes with dot notation: data.shape, data.ndim, data.size, data.dtype. These are properties, not methods, so do not use parentheses.',
                },
            },
            {
                'id': 'array-creation-functions',
                'title': 'Array Creation Functions',
                'content': """## Array Creation Functions

NumPy provides many convenient functions to create arrays without manually specifying every value.

### np.zeros() and np.ones()

Create arrays filled with zeros or ones -- useful for initializing data structures:

```python
import numpy as np

# Initialize a score tracker for 5 players (all start at zero)
player_scores = np.zeros(5, dtype=int)
print(player_scores)  # [0 0 0 0 0]

# Create a 3x3 grid of ones (e.g., a mask for image processing)
mask = np.ones((3, 3))
print(mask)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
```

### np.arange()

Like Python's `range()`, but returns a NumPy array. Supports float steps:

```python
# Whole numbers from 0 to 9
indices = np.arange(10)
print(indices)  # [0 1 2 3 4 5 6 7 8 9]

# From 1 to 10 (inclusive) with step 2
odd = np.arange(1, 11, 2)
print(odd)  # [1 3 5 7 9]

# Float range -- hours in a workday (8:00 to 17:00 in 0.5-hour steps)
hours = np.arange(8, 17.5, 0.5)
print(hours)
# [ 8.   8.5  9.   9.5 10.  10.5 11.  11.5 12.  12.5 13.  13.5 14.
#  14.5 15.  15.5 16.  16.5 17. ]
```

### np.linspace()

Creates evenly spaced values between a start and end point. You specify **how many values** you want, not the step size:

```python
# 5 evenly spaced points between 0 and 1 (for normalization)
normalized = np.linspace(0, 1, 5)
print(normalized)  # [0.   0.25 0.5  0.75 1.  ]

# 4 measurement points between 0 and 100 (sensor calibration)
calibration = np.linspace(0, 100, 4)
print(calibration)  # [  0.          33.33333333  66.66666667 100.        ]
```

### np.full() and np.eye()

```python
# Array filled with a specific value
default_ratings = np.full(5, 3.0)
print(default_ratings)  # [3. 3. 3. 3. 3.]

# Identity matrix (1s on diagonal, 0s elsewhere) -- used in linear algebra
identity = np.eye(3, dtype=int)
print(identity)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
```

### Real-Life Example: Initializing Sensor Data

```python
# Weather station with 24 hourly readings, initialized to -999 (no data)
sensor_readings = np.full(24, -999.0)
# As data comes in, you update specific positions:
sensor_readings[0] = 72.5   # Midnight reading
sensor_readings[1] = 71.8   # 1 AM reading
```""",
                'exercise': {
                    'instructions': 'Create the following arrays using NumPy creation functions: (1) a 1D array of zeros with 4 elements (integer type), (2) a 1D array using arange from 1 to 5 inclusive, (3) a 1D array using linspace with 5 values from 0 to 1, and (4) a 3x3 identity matrix (integer type). Print each array.',
                    'starter_code': 'import numpy as np\n\n# Create an array of 4 zeros (integer)\nzeros = np.zeros(4, dtype=int)\nprint(zeros)\n\n# Create array [1, 2, 3, 4, 5] using arange\nsequence = np.arange(1, 6)\nprint(sequence)\n\n# Create 5 evenly spaced values from 0 to 1\nspaced = np.linspace(0, 1, 5)\nprint(spaced)\n\n# Create 3x3 identity matrix (integer)\nidentity = np.eye(3, dtype=int)\nprint(identity)\n',
                    'expected_output': '[0 0 0 0]\n[1 2 3 4 5]\n[0.   0.25 0.5  0.75 1.  ]\n[[1 0 0]\n [0 1 0]\n [0 0 1]]',
                    'hint': 'Use np.zeros(4, dtype=int) for integer zeros. Use np.arange(1, 6) to get 1 through 5. Use np.linspace(0, 1, 5) for evenly spaced values. Use np.eye(3, dtype=int) for the identity matrix.',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this code will print? Type your guess!',
                    'code_snippet': 'import numpy as np\narr = np.arange(1, 6)\nprint(arr * 2)',
                    'expected_output': '[ 2  4  6  8 10]',
                    'explanation': 'np.arange(1, 6) creates [1 2 3 4 5]. When you multiply by 2, NumPy does it element-wise: each number gets doubled! This is called vectorized operations.',
                },
            },
            {
                'id': 'basic-array-operations',
                'title': 'Basic Array Operations',
                'content': """## Basic Array Operations

One of NumPy's greatest strengths is **vectorized operations** -- performing math on entire arrays at once without writing loops.

### Real-Life Analogy

Imagine you are a store manager and you need to apply a 10 percent discount to 1000 products. Without NumPy (Python lists), you would walk through the store and change each price tag one by one. With NumPy, you press a button and all 1000 price tags update simultaneously.

### Element-wise Arithmetic

```python
import numpy as np

prices = np.array([29.99, 49.99, 9.99, 99.99])

# Apply 10% discount to all prices at once
discounted = prices * 0.90
print(discounted)  # [26.991 44.991  8.991 89.991]

# Add $5 shipping to all prices
with_shipping = prices + 5
print(with_shipping)  # [34.99 54.99 14.99 104.99]
```

### Operations Between Arrays

When two arrays have the same shape, operations are performed element-by-element:

```python
# Calculate total cost: price * quantity for each product
prices = np.array([10.00, 25.00, 5.00, 15.00])
quantities = np.array([2, 1, 4, 3])

totals = prices * quantities
print(totals)  # [ 20.  25.  20.  45.]
print(f"Grand total: ${totals.sum():.2f}")  # Grand total: $110.00
```

### Aggregation Functions

NumPy provides fast statistical functions:

```python
scores = np.array([85, 92, 78, 95, 88, 76, 91])

print(f"Sum: {scores.sum()}")          # Sum: 605
print(f"Mean: {scores.mean():.1f}")    # Mean: 86.4
print(f"Max: {scores.max()}")          # Max: 95
print(f"Min: {scores.min()}")          # Min: 76
print(f"Std Dev: {scores.std():.2f}")  # Std Dev: 6.73
```

### Comparison Operations

Comparisons produce boolean arrays:

```python
temperatures = np.array([72, 85, 68, 91, 75, 88])

# Which days were above 80 degrees?
hot_days = temperatures > 80
print(hot_days)  # [False  True False  True False  True]

# Count hot days
print(f"Hot days: {hot_days.sum()}")  # Hot days: 3
```

### Universal Functions (ufuncs)

NumPy provides mathematical functions that work on arrays:

```python
# Square root of each element
data = np.array([4, 9, 16, 25])
print(np.sqrt(data))  # [2. 3. 4. 5.]

# Absolute value
changes = np.array([-3.5, 2.1, -0.8, 4.2])
print(np.abs(changes))  # [3.5 2.1 0.8 4.2]
```""",
                'exercise': None,
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # Lesson 2 -- Array Indexing, Slicing, and Broadcasting
    # ------------------------------------------------------------------ #
    {
        'title': 'Array Indexing, Slicing, and Broadcasting',
        'description': 'Master advanced techniques for accessing, filtering, and transforming NumPy arrays including fancy indexing, boolean indexing, broadcasting, and reshaping.',
        'order': 2,
        'item_order': 4,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'indexing-and-slicing',
                'title': 'Array Indexing and Slicing',
                'content': """## Array Indexing and Slicing

Accessing elements in NumPy arrays works similarly to Python lists but extends to multiple dimensions.

### 1D Array Indexing

```python
import numpy as np

# Daily temperatures for a week
temps = np.array([72, 75, 68, 80, 77, 82, 71])

print(temps[0])    # 72 -- Monday
print(temps[-1])   # 71 -- Sunday
print(temps[3])    # 80 -- Thursday
```

### 1D Array Slicing

```python
# Weekday temperatures (Mon-Fri)
weekdays = temps[0:5]
print(weekdays)  # [72 75 68 80 77]

# Weekend temperatures (Sat-Sun)
weekend = temps[5:]
print(weekend)  # [82 71]

# Every other day
alternate = temps[::2]
print(alternate)  # [72 68 77 71]

# Reversed
print(temps[::-1])  # [71 82 77 80 68 75 72]
```

### 2D Array Indexing

For 2D arrays, use `array[row, column]`:

```python
# Sales data: rows = stores, columns = months (Jan, Feb, Mar)
sales = np.array([
    [150, 200, 175],   # Store A
    [180, 160, 210],   # Store B
    [130, 190, 185],   # Store C
])

# Store B, February sales
print(sales[1, 1])  # 160

# Store A, all months
print(sales[0])      # [150 200 175]
print(sales[0, :])   # [150 200 175] -- same thing, explicit

# All stores, March sales
print(sales[:, 2])   # [175 210 185]
```

### 2D Array Slicing

```python
# First two stores, first two months
subset = sales[0:2, 0:2]
print(subset)
# [[150 200]
#  [180 160]]

# Last row, last two columns
print(sales[-1, -2:])  # [190 185]
```

### Key Difference from Python Lists

**NumPy slices are views, not copies.** Modifying a slice modifies the original array:

```python
original = np.array([1, 2, 3, 4, 5])
slice_view = original[1:4]
slice_view[0] = 99
print(original)  # [ 1 99  3  4  5] -- original changed!

# Use .copy() to avoid this
safe_copy = original[1:4].copy()
safe_copy[0] = 0
print(original)  # [ 1 99  3  4  5] -- original unchanged
```""",
                'exercise': {
                    'instructions': 'Create a 2D array representing monthly sales for 3 products over 4 months. Extract and print: (1) the entire first row (Product A), (2) the third column (Month 3 sales for all products), (3) a 2x2 sub-array of the first two products and first two months.',
                    'starter_code': 'import numpy as np\n\n# Monthly sales: rows = products, columns = months\nsales = np.array([\n    [120, 150, 130, 160],  # Product A\n    [200, 180, 210, 195],  # Product B\n    [90, 110, 95, 105],    # Product C\n])\n\n# Product A (entire first row)\nprint(sales[0])\n\n# Month 3 sales for all products (third column, index 2)\nprint(sales[:, 2])\n\n# First 2 products, first 2 months (2x2 sub-array)\nprint(sales[0:2, 0:2])\n',
                    'expected_output': '[120 150 130 160]\n[130 210  95]\n[[120 150]\n [200 180]]',
                    'hint': 'Use sales[0] for the first row. Use sales[:, 2] for the third column (index 2). Use sales[0:2, 0:2] for the top-left 2x2 sub-array.',
                },
                'game': {
                    'type': 'fill_blank',
                    'instructions': 'Fill in the blanks to get a column from a 2D array:',
                    'code_template': 'import numpy as np\ndata = np.array([[1, 2, 3], [4, 5, 6]])\n# Get all rows, second column\nresult = data[{0}, {1}]\nprint(result)',
                    'blanks': [
                        {'id': 0, 'answer': ':', 'hint': 'What symbol selects ALL rows?'},
                        {'id': 1, 'answer': '1', 'hint': 'What index is the second column?'},
                    ],
                    'explanation': 'In 2D arrays, data[:, 1] means "all rows (:), column at index 1". This gives us [2, 5] — the second column!',
                },
            },
            {
                'id': 'fancy-and-boolean-indexing',
                'title': 'Fancy Indexing and Boolean Indexing',
                'content': """## Fancy Indexing and Boolean Indexing

These advanced indexing techniques let you select arbitrary elements and filter data based on conditions -- essential skills for data analysis.

### Fancy Indexing (Integer Array Indexing)

You can use a list or array of indices to select specific elements:

```python
import numpy as np

# Product ratings
ratings = np.array([4.5, 3.2, 4.8, 2.9, 4.1, 3.7, 4.9])
product_names = ["Laptop", "Mouse", "Monitor", "Cable", "Keyboard", "Webcam", "Headset"]

# Select the top-rated products (indices 2, 6, 0)
top_indices = [2, 6, 0]
top_ratings = ratings[top_indices]
print(top_ratings)  # [4.8 4.9 4.5]
```

### Boolean Indexing

Boolean indexing uses a True/False array to select elements. This is one of the most powerful features in NumPy.

### Real-Life Example: Filtering Temperature Data

Imagine you are a meteorologist analyzing a week of temperature readings:

```python
# Daily high temperatures for two weeks (14 days)
temps = np.array([72, 85, 68, 91, 75, 88, 70, 95, 73, 82, 69, 90, 77, 86])

# Find all days above 80 degrees
hot_mask = temps > 80
print(hot_mask)
# [False  True False  True False  True False  True False  True False  True
#  False  True]

# Use the mask to get the actual temperatures
hot_temps = temps[hot_mask]
print(hot_temps)  # [85 91 88 95 82 90 86]

# Count hot days
print(f"Hot days: {hot_mask.sum()}")  # Hot days: 7
```

### Combining Conditions

Use `&` (and), `|` (or), and `~` (not) for compound conditions. **Important:** Use parentheses around each condition:

```python
scores = np.array([72, 85, 91, 68, 88, 95, 76, 60])

# Scores between 70 and 90 (inclusive)
mid_range = scores[(scores >= 70) & (scores <= 90)]
print(mid_range)  # [72 85 88 76]

# Scores below 70 OR above 90
extreme = scores[(scores < 70) | (scores > 90)]
print(extreme)  # [68 91 95 60]
```

### Real-Life Example: E-Commerce Product Filtering

```python
prices = np.array([29.99, 149.99, 9.99, 79.99, 199.99, 49.99])
ratings = np.array([4.5, 4.2, 3.8, 4.7, 3.9, 4.6])

# Find affordable AND highly-rated products
# (price < 100 AND rating >= 4.5)
good_deals = (prices < 100) & (ratings >= 4.5)
print(prices[good_deals])   # [29.99 79.99 49.99]
print(ratings[good_deals])  # [4.5 4.7 4.6]
```

### np.where() -- Conditional Selection

`np.where(condition, value_if_true, value_if_false)` returns an array based on conditions:

```python
scores = np.array([85, 62, 91, 45, 78])
labels = np.where(scores >= 70, "Pass", "Fail")
print(labels)  # ['Pass' 'Fail' 'Pass' 'Fail' 'Pass']
```""",
                'exercise': {
                    'instructions': 'Given an array of daily temperatures, use boolean indexing to find: (1) all temperatures above 75, (2) the count of temperatures between 70 and 80 inclusive, and (3) use np.where to label each temperature as "Hot" if above 80 or "Cool" otherwise.',
                    'starter_code': 'import numpy as np\n\n# Daily temperatures for 10 days\ntemps = np.array([72, 85, 68, 91, 75, 88, 70, 79, 82, 66])\n\n# Temperatures above 75\nabove_75 = temps[temps > 75]\nprint(above_75)\n\n# Count of temperatures between 70 and 80 (inclusive)\nmild_count = ((temps >= 70) & (temps <= 80)).sum()\nprint(mild_count)\n\n# Label as "Hot" (above 80) or "Cool"\nlabels = np.where(temps > 80, "Hot", "Cool")\nprint(labels)\n',
                    'expected_output': "[85 91 88 79 82]\n4\n['Cool' 'Hot' 'Cool' 'Hot' 'Cool' 'Hot' 'Cool' 'Cool' 'Hot' 'Cool']",
                    'hint': 'Use temps[temps > 75] for boolean indexing. Use ((temps >= 70) & (temps <= 80)).sum() to count elements meeting both conditions. Use np.where(temps > 80, "Hot", "Cool") for conditional labeling.',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Look at this code and pick the correct answer:',
                    'code_snippet': 'import numpy as np\nscores = np.array([85, 60, 92, 45, 78])\nmask = scores > 70\nprint(mask.sum())',
                    'question': 'What will this code print?',
                    'options': [
                        {'text': '3', 'correct': True},
                        {'text': '5', 'correct': False},
                        {'text': '255', 'correct': False},
                        {'text': '[True, False, True, False, True]', 'correct': False},
                    ],
                    'explanation': 'scores > 70 creates a boolean array [True, False, True, False, True]. When you call .sum() on booleans, True counts as 1 and False as 0. So 1+0+1+0+1 = 3!',
                },
            },
            {
                'id': 'broadcasting',
                'title': 'Broadcasting',
                'content': """## Broadcasting

**Broadcasting** is NumPy's mechanism for performing operations on arrays with different shapes. It automatically expands smaller arrays to match larger ones, enabling powerful batch calculations without explicit loops.

### Real-Life Analogy

Think of broadcasting like applying a salary raise across an entire company. If you say "give everyone a 5 percent raise," you do not need to specify the raise for each of the 500 employees individually. The single "5 percent" value is broadcast to every employee's salary.

### Scalar Broadcasting

The simplest form: operating on an array with a single number:

```python
import numpy as np

# All product prices
prices = np.array([29.99, 49.99, 9.99, 99.99])

# Apply 10% tax to ALL prices (scalar broadcast)
with_tax = prices * 1.10
print(np.round(with_tax, 2))  # [32.99 54.99 10.99 109.99]
```

The scalar `1.10` is broadcast (stretched) to match the shape of `prices`.

### Broadcasting with Different Shaped Arrays

```python
# Monthly sales for 3 stores (rows) over 4 months (columns)
sales = np.array([
    [100, 120, 110, 130],  # Store A
    [200, 180, 210, 195],  # Store B
    [150, 160, 155, 170],  # Store C
])

# Different tax rate for each month
monthly_tax = np.array([1.08, 1.10, 1.09, 1.07])

# Broadcasting: (3, 4) array * (4,) array
# The 1D array is stretched across all 3 rows
sales_with_tax = sales * monthly_tax
print(np.round(sales_with_tax, 1))
# [[108.  132.  119.9 139.1]
#  [216.  198.  228.9 208.6]
#  [162.  176.  169.  181.9]]
```

### Broadcasting Rules

For broadcasting to work, NumPy compares shapes from right to left:

1. Dimensions are compatible if they are **equal** or one of them is **1**.
2. If a dimension is 1, it is stretched to match the other.

```
Shape (3, 4) and (4,)    -> Compatible: (4,) becomes (1, 4) -> (3, 4)
Shape (3, 4) and (3, 1)  -> Compatible: result is (3, 4)
Shape (3, 4) and (3,)    -> NOT compatible (4 != 3)
```

### Real-Life Example: Batch Grade Calculations

```python
# Scores for 4 students on 3 exams
scores = np.array([
    [85, 90, 78],  # Student A
    [92, 88, 95],  # Student B
    [70, 75, 80],  # Student C
    [88, 82, 91],  # Student D
])

# Different weight for each exam
weights = np.array([0.3, 0.3, 0.4])

# Weighted scores (broadcasting: (4, 3) * (3,))
weighted = scores * weights
print(np.round(weighted, 1))
# [[25.5 27.  31.2]
#  [27.6 26.4 38. ]
#  [21.  22.5 32. ]
#  [26.4 24.6 36.4]]

# Final weighted average per student
final_grades = weighted.sum(axis=1)
print(np.round(final_grades, 1))
# [83.7 92.  75.5 87.4]
```""",
                'exercise': {
                    'instructions': 'A store has 3 products with base prices. Apply a 15% discount to all prices using broadcasting. Then, given a 2D array of quantities sold by 2 cashiers for each product, calculate the revenue (price * quantity) using broadcasting. Print the discounted prices (rounded to 2 decimals) and the revenue matrix.',
                    'starter_code': 'import numpy as np\n\n# Base prices for 3 products\nprices = np.array([25.00, 15.00, 40.00])\n\n# Apply 15% discount using broadcasting\ndiscounted = np.round(prices * 0.85, 2)\nprint(discounted)\n\n# Quantities sold by 2 cashiers for each of the 3 products\nquantities = np.array([\n    [4, 7, 2],  # Cashier 1\n    [3, 5, 6],  # Cashier 2\n])\n\n# Revenue: quantities * discounted prices (broadcasting)\nrevenue = quantities * discounted\nprint(revenue)\n',
                    'expected_output': '[21.25 12.75 34.  ]\n[[ 85.    89.25  68.  ]\n [ 63.75  63.75 204.  ]]',
                    'hint': 'Multiply the prices array by 0.85 for the discount. For revenue, multiply the 2D quantities array (2, 3) by the 1D discounted prices (3,). Broadcasting will stretch the 1D array across each row.',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this broadcasting code will print? Type your guess!',
                    'code_snippet': 'import numpy as np\nprices = np.array([10, 20, 30])\ntax = 1.1\nresult = prices * tax\nprint(result)',
                    'expected_output': '[11. 22. 33.]',
                    'explanation': 'Broadcasting multiplies the single number 1.1 with every element: 10*1.1=11, 20*1.1=22, 30*1.1=33. NumPy shows them as floats because 1.1 is a float!',
                },
            },
            {
                'id': 'reshaping-arrays',
                'title': 'Reshaping Arrays',
                'content': """## Reshaping Arrays

Reshaping lets you change the structure of an array without changing its data. This is essential for preparing data for machine learning models, image processing, and matrix operations.

### Real-Life Analogy

Reshaping is like rearranging books on a shelf. You have 12 books and you can arrange them as: one row of 12, two rows of 6, three rows of 4, four rows of 3, or six rows of 2. The books are the same -- only the arrangement changes.

### The reshape() Method

```python
import numpy as np

# 1D array of 12 monthly sales figures
monthly_sales = np.arange(1, 13)
print(monthly_sales)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Reshape into 4 quarters x 3 months
quarterly = monthly_sales.reshape(4, 3)
print(quarterly)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Reshape into 2 halves x 6 months
semiannual = monthly_sales.reshape(2, 6)
print(semiannual)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]
```

### Using -1 for Automatic Dimension

You can use `-1` for one dimension, and NumPy will calculate it:

```python
data = np.arange(24)

# "I want 4 rows, figure out the columns"
print(data.reshape(4, -1).shape)  # (4, 6)

# "I want 3 columns, figure out the rows"
print(data.reshape(-1, 3).shape)  # (8, 3)
```

### Flatten and Ravel

Convert a multi-dimensional array back to 1D:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# flatten() returns a copy
flat = matrix.flatten()
print(flat)  # [1 2 3 4 5 6]

# ravel() returns a view (more memory efficient)
raveled = matrix.ravel()
print(raveled)  # [1 2 3 4 5 6]
```

### Transpose

Swap rows and columns:

```python
# Student scores: 3 students x 2 exams
scores = np.array([
    [85, 90],
    [78, 82],
    [92, 88],
])

# Transpose: now 2 exams x 3 students
print(scores.T)
# [[85 78 92]
#  [90 82 88]]
```

### Real-Life Example: Image Data

```python
# A tiny 2x3 grayscale image stored as flat data
pixel_data = np.array([128, 200, 50, 75, 255, 100])

# Reshape into 2x3 image
image = pixel_data.reshape(2, 3)
print(image)
# [[128 200  50]
#  [ 75 255 100]]
```""",
                'exercise': None,
            },
            {
                'id': 'numpy-summary',
                'title': 'Summary and Quick Reference',
                'content': """## Summary and Quick Reference

### Array Creation

| Function | Purpose | Example |
|----------|---------|---------|
| `np.array(list)` | Create from list | `np.array([1, 2, 3])` |
| `np.zeros(shape)` | Filled with 0s | `np.zeros((3, 4))` |
| `np.ones(shape)` | Filled with 1s | `np.ones(5)` |
| `np.arange(start, stop, step)` | Range of values | `np.arange(0, 10, 2)` |
| `np.linspace(start, stop, n)` | n evenly spaced | `np.linspace(0, 1, 5)` |
| `np.full(shape, value)` | Filled with value | `np.full(3, 7)` |
| `np.eye(n)` | Identity matrix | `np.eye(3)` |

### Indexing and Slicing

| Operation | 1D Example | 2D Example |
|-----------|------------|------------|
| Single element | `arr[2]` | `arr[1, 3]` |
| Slice | `arr[1:4]` | `arr[0:2, 1:3]` |
| Full row | -- | `arr[0]` or `arr[0, :]` |
| Full column | -- | `arr[:, 2]` |
| Boolean mask | `arr[arr > 5]` | `arr[arr > 5]` |
| Fancy index | `arr[[0, 3, 5]]` | `arr[[0, 2], :]` |

### Broadcasting Rules

1. Compare shapes from right to left.
2. Dimensions must be equal or one must be 1.
3. A dimension of size 1 is stretched to match.

### Reshaping

| Operation | Code |
|-----------|------|
| Reshape | `arr.reshape(rows, cols)` |
| Auto-calculate dim | `arr.reshape(-1, 3)` |
| Flatten (copy) | `arr.flatten()` |
| Ravel (view) | `arr.ravel()` |
| Transpose | `arr.T` |

### Key Aggregation Functions

```python
arr.sum()           # Total of all elements
arr.mean()          # Average
arr.std()           # Standard deviation
arr.min() / arr.max()  # Minimum / Maximum
arr.sum(axis=0)     # Sum along columns
arr.sum(axis=1)     # Sum along rows
```

### Best Practices

1. **Always use `import numpy as np`** -- it is the universal convention.
2. **Prefer vectorized operations** over Python loops for performance.
3. **Use `.copy()` when slicing** if you do not want changes to affect the original.
4. **Check shapes with `.shape`** when operations produce unexpected results.
5. **Use `dtype` parameter** when you need to control memory usage or type precision.""",
                'exercise': None,
            },
        ],
    },
]
