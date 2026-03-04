"""
Content pipeline — 15 pre-written data-science blog posts and publishing logic.

Posts are stored as Python dicts and inserted into the database on demand.
The growth engine publishes them on a schedule (one every few days) to keep
the blog fresh and drive organic search traffic.
"""

from datetime import datetime
from app.extensions import db
from app.models.blog_post import BlogPost

# ──────────────────────────────────────────────────────────
# Pre-written blog posts
# ──────────────────────────────────────────────────────────

GROWTH_POSTS = [
    {
        'title': '10 Pandas Functions Every Data Analyst Uses Daily',
        'slug': '10-pandas-functions-every-analyst-uses',
        'category': 'pandas',
        'tags': 'pandas, data-analysis, python, functions',
        'meta_description': 'Master the 10 most-used Pandas functions that professional data analysts rely on every single day.',
        'content': """Data analysts spend most of their time wrangling data, and Pandas makes that work manageable. Here are the 10 functions you will use most often in real-world projects.

## 1. read_csv() — Loading Data

Every analysis starts with loading data. `pd.read_csv()` handles file paths, URLs, and dozens of parsing options like `dtype`, `parse_dates`, and `na_values`.

## 2. head() and tail() — Quick Inspection

Before diving in, always inspect your data. `df.head(10)` shows the first 10 rows, while `df.tail()` shows the last 5.

## 3. info() — Data Overview

`df.info()` gives you column names, data types, and non-null counts in one call. It is the fastest way to understand what you are working with.

## 4. describe() — Summary Statistics

`df.describe()` computes count, mean, standard deviation, min, max, and quartiles for every numeric column instantly.

## 5. value_counts() — Frequency Analysis

Need to know how many times each value appears? `df['column'].value_counts()` is your go-to for categorical data exploration.

## 6. groupby() — Aggregation

Grouping data by categories and computing aggregates is bread and butter for analysts. `df.groupby('category')['sales'].sum()` is clean and powerful.

## 7. merge() — Combining DataFrames

Real projects involve multiple tables. `pd.merge(df1, df2, on='key')` works like SQL JOINs and supports left, right, inner, and outer joins.

## 8. fillna() and dropna() — Missing Data

Missing values are inevitable. `df.fillna(0)` replaces them, while `df.dropna()` removes rows with missing values entirely.

## 9. apply() — Custom Transformations

When built-in functions are not enough, `df['col'].apply(my_function)` lets you apply any Python function element-wise.

## 10. to_csv() — Saving Results

After analysis, save your results with `df.to_csv('output.csv', index=False)`. Simple and reliable.

## Practice These Skills

Our **Chapter 10: Pandas for Data Analysis** lets you practice all 10 of these functions with hands-on, auto-graded assignments that mirror real data projects. [Start learning now](/register).
""",
    },
    {
        'title': 'Understanding NumPy Broadcasting — A Visual Guide',
        'slug': 'numpy-broadcasting-visual-guide',
        'category': 'numpy',
        'tags': 'numpy, broadcasting, arrays, python',
        'meta_description': 'Learn how NumPy broadcasting works with clear visual examples and practical code snippets.',
        'content': """Broadcasting is one of NumPy's most powerful features, but it confuses many beginners. This guide explains it visually so you will never struggle with it again.

## What Is Broadcasting?

Broadcasting is NumPy's way of performing operations on arrays with different shapes. Instead of requiring arrays to be the same size, NumPy automatically "broadcasts" the smaller array across the larger one.

## The Rules

NumPy compares shapes element-wise, starting from the trailing dimensions:

1. **Dimensions are compatible** if they are equal, or one of them is 1
2. **Arrays with fewer dimensions** are padded with 1s on the left

## Example 1: Scalar + Array

```python
import numpy as np
a = np.array([1, 2, 3])
result = a + 10  # [11, 12, 13]
```

The scalar 10 is broadcast to `[10, 10, 10]` to match the array shape.

## Example 2: Column + Row

```python
col = np.array([[1], [2], [3]])  # Shape: (3, 1)
row = np.array([10, 20, 30])     # Shape: (3,)
result = col + row
# [[11, 21, 31],
#  [12, 22, 32],
#  [13, 23, 33]]
```

The column is broadcast across columns, and the row is broadcast across rows.

## Example 3: Centering Data

Broadcasting shines in data science. To center a dataset (subtract the mean of each column):

```python
data = np.random.randn(100, 3)
centered = data - data.mean(axis=0)  # (100, 3) - (3,) = (100, 3)
```

## Common Mistake

Shapes `(3, 4)` and `(3,)` are **not compatible** for broadcasting. You would need shape `(3, 1)` or `(1, 4)`. Use `reshape()` to fix this.

## Learn More

Our **Chapter 9: NumPy Fundamentals** covers broadcasting, indexing, and vectorized operations with interactive assignments. [Start learning](/register).
""",
    },
    {
        'title': 'Your First Machine Learning Model with Scikit-Learn',
        'slug': 'first-ml-model-scikit-learn',
        'category': 'scikit-learn',
        'tags': 'scikit-learn, machine-learning, classification, python',
        'meta_description': 'Build your first machine learning classifier in under 20 lines of Python using Scikit-Learn.',
        'content': """Machine learning does not have to be intimidating. With Scikit-Learn, you can build a working classifier in under 20 lines of code. Here is exactly how.

## The Dataset

We will use the Iris dataset, which contains measurements of 150 flowers from 3 species. The goal: predict the species from the measurements.

## Step 1: Load the Data

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)
```

## Step 2: Choose a Model

Start with a Decision Tree — it is simple and interpretable:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
```

## Step 3: Train the Model

```python
model.fit(X_train, y_train)
```

That is it. One line to train.

## Step 4: Evaluate

```python
from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")  # ~97%
```

## What Just Happened?

1. We split data into training and testing sets (70/30)
2. The model learned patterns from training data
3. We tested it on unseen data to measure real performance

## Next Steps

Try different models: `RandomForestClassifier`, `KNeighborsClassifier`, `SVC`. Scikit-Learn makes switching models a one-line change.

## Hands-On Practice

Our **Chapter 11: Scikit-Learn for Machine Learning** guides you through classification, regression, and model evaluation with auto-graded assignments. [Start your ML journey](/register).
""",
    },
    {
        'title': 'Python Data Types Every Data Scientist Must Know',
        'slug': 'python-data-types-for-data-science',
        'category': 'python-tips',
        'tags': 'python, data-types, beginners, fundamentals',
        'meta_description': 'A data scientist guide to Python data types — when to use lists, tuples, dicts, sets, and how they connect to NumPy and Pandas.',
        'content': """Choosing the right data type is a fundamental skill that separates beginners from professionals. Here is what every data scientist needs to know about Python's core data types.

## Lists — Your General-Purpose Container

Lists are ordered, mutable, and can hold mixed types. They are perfect for small collections and quick scripting.

```python
measurements = [1.5, 2.3, 4.1, 3.7]
measurements.append(5.2)
```

**Data science use:** Loading and preprocessing small datasets before converting to NumPy arrays or Pandas DataFrames.

## Tuples — Immutable Records

Tuples cannot be changed after creation. Use them for fixed records like coordinates or database rows.

```python
point = (3.5, 7.2)
dimensions = (1920, 1080)
```

**Data science use:** Function return values, dictionary keys, and data that should not be accidentally modified.

## Dictionaries — Key-Value Pairs

Dictionaries provide O(1) lookup by key. They are everywhere in data science.

```python
metrics = {'accuracy': 0.95, 'precision': 0.92, 'recall': 0.89}
```

**Data science use:** Configuration, hyperparameters, JSON parsing, creating DataFrames from records.

## Sets — Unique Collections

Sets automatically remove duplicates and support fast membership testing.

```python
unique_categories = {'cat', 'dog', 'bird', 'cat'}  # Only 3 elements
```

**Data science use:** Finding unique values, set operations (intersection, union, difference) for data cleaning.

## Strings — Text Data

Strings are immutable sequences of characters. Text processing is a core data science skill.

```python
name = "Machine Learning"
tokens = name.lower().split()  # ['machine', 'learning']
```

## When to Use What

| Need | Use |
|------|-----|
| Ordered, changeable collection | List |
| Fixed record | Tuple |
| Fast lookup by key | Dictionary |
| Unique values | Set |
| Text processing | String |
| Large numeric data | NumPy array |
| Tabular data | Pandas DataFrame |

## Build Your Foundation

Our **Chapters 1-6** cover all Python fundamentals with hands-on practice. Master these before moving to NumPy and Pandas. [Start learning](/register).
""",
    },
    {
        'title': 'How to Clean Messy Data with Pandas',
        'slug': 'clean-messy-data-with-pandas',
        'category': 'pandas',
        'tags': 'pandas, data-cleaning, data-quality, python',
        'meta_description': 'Learn the essential Pandas techniques for cleaning messy real-world data — handling missing values, duplicates, and inconsistent formats.',
        'content': """Real-world data is messy. Surveys have blank fields, databases have duplicates, and spreadsheets have inconsistent formatting. Learning to clean data is the most valuable skill a data analyst can have.

## The 80/20 Rule

Data scientists spend roughly 80 percent of their time cleaning and preparing data. Mastering these techniques will save you hours on every project.

## Handling Missing Values

```python
# See what is missing
df.isnull().sum()

# Drop rows with any missing values
df_clean = df.dropna()

# Fill missing values with a default
df['age'].fillna(df['age'].median(), inplace=True)

# Forward fill (useful for time series)
df['price'].fillna(method='ffill', inplace=True)
```

## Removing Duplicates

```python
# Check for duplicates
df.duplicated().sum()

# Remove exact duplicates
df = df.drop_duplicates()

# Remove duplicates based on specific columns
df = df.drop_duplicates(subset=['email'], keep='first')
```

## Fixing Data Types

```python
# Convert string dates to datetime
df['date'] = pd.to_datetime(df['date'])

# Convert string numbers
df['price'] = df['price'].str.replace('$', '').astype(float)
```

## Standardizing Text

```python
# Consistent casing
df['name'] = df['name'].str.strip().str.title()

# Replace variations
df['country'] = df['country'].replace({
    'US': 'United States',
    'USA': 'United States',
    'U.S.A.': 'United States',
})
```

## Handling Outliers

```python
# Remove values beyond 3 standard deviations
mean = df['salary'].mean()
std = df['salary'].std()
df = df[(df['salary'] > mean - 3*std) & (df['salary'] < mean + 3*std)]
```

## Practice with Real Scenarios

Our **Chapter 10: Pandas** includes data cleaning assignments with messy datasets that mirror what you will encounter in real jobs. [Start practicing](/register).
""",
    },
    {
        'title': 'NumPy Array Slicing — The Complete Guide',
        'slug': 'numpy-array-slicing-complete-guide',
        'category': 'numpy',
        'tags': 'numpy, arrays, slicing, indexing, python',
        'meta_description': 'Master NumPy array slicing and indexing with this complete guide covering 1D, 2D, and advanced techniques.',
        'content': """Array slicing is how you extract, modify, and manipulate specific parts of your data in NumPy. Mastering it is essential for any data science work.

## 1D Array Slicing

The syntax is `array[start:stop:step]`. Like Python lists, the stop index is exclusive.

```python
import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70])

a[2:5]    # [30, 40, 50]
a[:3]     # [10, 20, 30]
a[4:]     # [50, 60, 70]
a[::2]    # [10, 30, 50, 70] — every other element
a[::-1]   # [70, 60, 50, 40, 30, 20, 10] — reversed
```

## 2D Array Slicing

For 2D arrays, use `array[row_slice, col_slice]`:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

matrix[0, :]    # [1, 2, 3] — first row
matrix[:, 1]    # [2, 5, 8] — second column
matrix[0:2, 1:] # [[2, 3], [5, 6]] — submatrix
```

## Boolean Indexing

Filter arrays with conditions — incredibly powerful for data science:

```python
data = np.array([15, 22, 8, 42, 33, 5])

data[data > 20]        # [22, 42, 33]
data[data % 2 == 0]    # [22, 8, 42]
data[(data > 10) & (data < 40)]  # [15, 22, 33]
```

## Fancy Indexing

Select specific elements by index:

```python
a = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
a[indices]  # [10, 30, 50]
```

## Views vs. Copies

NumPy slices return **views**, not copies. Modifying a slice modifies the original:

```python
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
view[0] = 99
print(original)  # [1, 99, 3, 4, 5] — original changed!
```

Use `.copy()` when you need an independent copy.

## Hands-On Practice

Our **Chapter 9: NumPy Fundamentals** includes assignments on slicing, indexing, and boolean filtering with real numerical datasets. [Start learning](/register).
""",
    },
    {
        'title': 'Classification vs Regression: When to Use Which',
        'slug': 'classification-vs-regression-guide',
        'category': 'scikit-learn',
        'tags': 'machine-learning, classification, regression, scikit-learn',
        'meta_description': 'Understand the key differences between classification and regression in machine learning and when to use each approach.',
        'content': """One of the first decisions in any machine learning project is: classification or regression? Choosing wrong can lead to poor results or wasted effort.

## The Core Difference

**Classification** predicts a category (discrete label). **Regression** predicts a number (continuous value).

| Question | Type | Example Output |
|----------|------|----------------|
| Will it rain tomorrow? | Classification | Yes / No |
| How much will it rain? | Regression | 2.5 inches |
| Is this email spam? | Classification | Spam / Not Spam |
| What is this house worth? | Regression | $350,000 |
| Which species is this flower? | Classification | Setosa / Versicolor / Virginica |
| What will sales be next month? | Regression | $45,200 |

## Classification Algorithms

Popular classifiers in Scikit-Learn:

- **Logistic Regression** — Despite the name, it is a classifier. Fast and interpretable.
- **Decision Tree** — Easy to understand, handles non-linear boundaries.
- **Random Forest** — Ensemble of trees, very robust.
- **K-Nearest Neighbors** — Simple concept, works well with small datasets.
- **SVM** — Powerful for high-dimensional data.

## Regression Algorithms

Popular regressors:

- **Linear Regression** — The baseline for any regression task.
- **Ridge / Lasso** — Linear regression with regularization to prevent overfitting.
- **Decision Tree Regressor** — Handles non-linear relationships.
- **Random Forest Regressor** — Robust ensemble method.
- **Gradient Boosting** — Often the best performer for tabular data.

## How to Decide

Ask yourself: **Is the target a category or a number?**

- Predicting labels, classes, or categories: **Classification**
- Predicting amounts, prices, or quantities: **Regression**

Sometimes it is not obvious. "How many stars will this user give?" could be regression (1.0-5.0) or classification (1, 2, 3, 4, or 5).

## Evaluation Metrics

- **Classification:** accuracy, precision, recall, F1-score, confusion matrix
- **Regression:** MSE, RMSE, MAE, R-squared

## Learn Both

Our **Chapter 11: Scikit-Learn** covers both classification and regression with hands-on projects. Build real models and learn to evaluate them properly. [Start learning](/register).
""",
    },
    {
        'title': '5 Common Pandas Mistakes Beginners Make',
        'slug': '5-common-pandas-mistakes-beginners',
        'category': 'pandas',
        'tags': 'pandas, mistakes, debugging, python, beginners',
        'meta_description': 'Avoid these 5 common Pandas mistakes that trip up beginners and learn the correct approaches.',
        'content': """Pandas is powerful but has quirks that catch beginners off guard. Here are the 5 most common mistakes and how to avoid them.

## Mistake 1: Chained Indexing

This looks fine but creates a hidden copy:

```python
# Wrong — may not modify original DataFrame
df[df['age'] > 25]['salary'] = 50000

# Correct — use .loc for guaranteed modification
df.loc[df['age'] > 25, 'salary'] = 50000
```

Pandas will warn you with `SettingWithCopyWarning`. Always use `.loc[]` or `.iloc[]` for assignment.

## Mistake 2: Ignoring inplace=True Behavior

Many beginners forget that most Pandas operations return a new DataFrame:

```python
# Wrong — df is unchanged
df.dropna()
df.sort_values('date')

# Correct — assign the result
df = df.dropna()
df = df.sort_values('date')
```

## Mistake 3: Using Loops Instead of Vectorized Operations

Python loops on DataFrames are 10-100x slower than vectorized operations:

```python
# Wrong — very slow
for i in range(len(df)):
    df.loc[i, 'total'] = df.loc[i, 'price'] * df.loc[i, 'quantity']

# Correct — vectorized, fast
df['total'] = df['price'] * df['quantity']
```

## Mistake 4: Not Checking Data Types

Loading data from CSV often gives you strings when you expect numbers:

```python
# Check types first
print(df.dtypes)

# Convert as needed
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['date'] = pd.to_datetime(df['date'])
```

## Mistake 5: Forgetting axis Parameter

Many functions work on rows by default when you wanted columns:

```python
# Drops rows with any NaN (axis=0, default)
df.dropna()

# Drops columns with any NaN
df.dropna(axis=1)

# Sum per column (axis=0, default)
df.sum()

# Sum per row
df.sum(axis=1)
```

## Master Pandas Properly

Our **Chapter 10** teaches Pandas the right way from the start, with auto-graded assignments that catch these mistakes. [Learn Pandas correctly](/register).
""",
    },
    {
        'title': 'Building a Data Pipeline with Python',
        'slug': 'building-data-pipeline-python',
        'category': 'career',
        'tags': 'data-pipeline, python, etl, career, pandas',
        'meta_description': 'Learn how to build a simple but effective data pipeline using Python, Pandas, and standard libraries.',
        'content': """Data pipelines are the backbone of data engineering. They extract data from sources, transform it, and load it into destinations. Here is how to build one with pure Python.

## What Is a Data Pipeline?

A pipeline is an automated workflow that moves data from point A to point B, transforming it along the way. The classic pattern is **ETL**: Extract, Transform, Load.

## Step 1: Extract

Pull data from your source — CSV files, APIs, or databases:

```python
import pandas as pd

# From CSV
raw_data = pd.read_csv('sales_data.csv')

# From API (using requests)
import requests
response = requests.get('https://api.example.com/data')
api_data = pd.DataFrame(response.json())
```

## Step 2: Transform

Clean and reshape the data:

```python
# Remove duplicates
df = raw_data.drop_duplicates()

# Fix data types
df['date'] = pd.to_datetime(df['date'])
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Filter relevant data
df = df[df['amount'] > 0]

# Create derived columns
df['month'] = df['date'].dt.to_period('M')
df['year'] = df['date'].dt.year
```

## Step 3: Load

Save the processed data to its destination:

```python
# To CSV
df.to_csv('processed_sales.csv', index=False)

# To database (using SQLAlchemy)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///analytics.db')
df.to_sql('monthly_sales', engine, if_exists='replace', index=False)
```

## Adding Error Handling

Real pipelines need to handle failures gracefully:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    try:
        logger.info("Extracting data...")
        raw = extract()
        logger.info(f"Extracted {len(raw)} records")

        logger.info("Transforming...")
        clean = transform(raw)
        logger.info(f"Transformed to {len(clean)} records")

        logger.info("Loading...")
        load(clean)
        logger.info("Pipeline complete!")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise
```

## Build Your Skills

Our curriculum covers the full stack for data pipelines: **Python fundamentals** (Chapters 1-8), **NumPy** for computation (Chapter 9), and **Pandas** for data manipulation (Chapter 10). [Start your data engineering journey](/register).
""",
    },
    {
        'title': 'Feature Engineering with Scikit-Learn Transformers',
        'slug': 'feature-engineering-scikit-learn-transformers',
        'category': 'scikit-learn',
        'tags': 'scikit-learn, feature-engineering, machine-learning, transformers',
        'meta_description': 'Learn how to use Scikit-Learn transformers and pipelines for effective feature engineering in machine learning projects.',
        'content': """Feature engineering — creating and transforming input features — often matters more than the choice of algorithm. Scikit-Learn provides powerful tools to make this systematic.

## Why Feature Engineering?

Raw data rarely feeds directly into a model. You need to:
- Scale numeric features to similar ranges
- Encode categorical variables as numbers
- Handle missing values consistently
- Create new features from existing ones

## StandardScaler — Normalizing Numbers

Many algorithms assume features have similar scales:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
```

This centers each feature to mean=0 and std=1.

## OneHotEncoder — Categorical Variables

Convert categories like "red", "blue", "green" to binary columns:

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_encoded = encoder.fit_transform(X_train[['color', 'size']])
```

## SimpleImputer — Missing Values

Fill missing values consistently across train and test sets:

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X_train)
```

## ColumnTransformer — Different Transforms Per Column

Real datasets have mixed types. Apply different transforms to different columns:

```python
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), ['age', 'salary']),
    ('cat', OneHotEncoder(), ['department', 'city']),
])
```

## Pipeline — Chain Everything

Combine preprocessing and model into one pipeline:

```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
    ('preprocess', preprocessor),
    ('classifier', RandomForestClassifier()),
])

pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
```

Pipelines prevent data leakage and simplify deployment.

## Learn Feature Engineering

Our **Chapter 11: Scikit-Learn** covers transformers, pipelines, and feature engineering patterns with real datasets. [Start building better models](/register).
""",
    },
    {
        'title': 'Python List Comprehensions for Data Work',
        'slug': 'python-list-comprehensions-data-work',
        'category': 'python-tips',
        'tags': 'python, list-comprehensions, fundamentals, performance',
        'meta_description': 'Master Python list comprehensions with practical examples for data processing, filtering, and transformation.',
        'content': """List comprehensions are one of Python's most elegant features. They let you create, filter, and transform data in a single readable line.

## Basic Syntax

```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension — same result
squares = [x ** 2 for x in range(10)]
```

## Filtering with Conditions

Add an `if` clause to filter elements:

```python
# Only even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Filter a list of names
short_names = [name for name in names if len(name) <= 5]
```

## Transform and Filter

Combine transformation and filtering:

```python
# Uppercase names that start with 'A'
result = [name.upper() for name in names if name.startswith('A')]

# Convert strings to integers, skip non-numeric
numbers = [int(s) for s in strings if s.isdigit()]
```

## Nested Comprehensions

Flatten a list of lists:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Dictionary Comprehensions

Create dictionaries the same way:

```python
# Word lengths
lengths = {word: len(word) for word in words}

# Invert a dictionary
inverted = {v: k for k, v in original.items()}
```

## Set Comprehensions

Create sets to automatically remove duplicates:

```python
unique_lengths = {len(word) for word in words}
```

## When NOT to Use Comprehensions

Avoid comprehensions when:
- The logic is complex (use a regular loop for readability)
- You need side effects (printing, writing files)
- The result would be enormous (use a generator expression instead)

```python
# Generator expression — uses no memory
total = sum(x ** 2 for x in range(1_000_000))
```

## Build Your Python Skills

List comprehensions are covered in our **Chapter 3: Data Structures** with practice assignments that build your fluency. [Start learning Python](/register).
""",
    },
    {
        'title': 'Exploratory Data Analysis with Pandas and NumPy',
        'slug': 'exploratory-data-analysis-pandas-numpy',
        'category': 'pandas',
        'tags': 'pandas, numpy, eda, data-analysis, visualization',
        'meta_description': 'A step-by-step guide to exploratory data analysis using Pandas and NumPy for uncovering patterns in data.',
        'content': """Exploratory Data Analysis (EDA) is the first step in any data project. It helps you understand your data, find patterns, and identify issues before modeling.

## Step 1: Load and Inspect

```python
import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')

# Basic info
print(df.shape)     # (rows, columns)
print(df.dtypes)    # Column types
print(df.head())    # First 5 rows
df.info()           # Non-null counts and types
```

## Step 2: Summary Statistics

```python
# Numeric columns
df.describe()

# Include categorical columns
df.describe(include='all')

# Specific statistics
df['salary'].median()
df['department'].value_counts()
```

## Step 3: Missing Value Analysis

```python
# Count missing values per column
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
print(missing_pct[missing_pct > 0])
```

## Step 4: Distribution Analysis

```python
# Numeric distributions
for col in df.select_dtypes(include=[np.number]).columns:
    print(f"{col}: mean={df[col].mean():.2f}, "
          f"std={df[col].std():.2f}, "
          f"skew={df[col].skew():.2f}")
```

## Step 5: Correlation Analysis

```python
# Correlation matrix
corr = df.select_dtypes(include=[np.number]).corr()

# Find strong correlations
for i in range(len(corr.columns)):
    for j in range(i+1, len(corr.columns)):
        if abs(corr.iloc[i, j]) > 0.7:
            print(f"{corr.columns[i]} <-> {corr.columns[j]}: "
                  f"{corr.iloc[i, j]:.2f}")
```

## Step 6: Categorical Analysis

```python
# Value counts for each categorical column
for col in df.select_dtypes(include=['object']).columns:
    print(f"\\n{col}:")
    print(df[col].value_counts().head())
```

## Step 7: Outlier Detection

```python
# IQR method
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['salary'] < Q1 - 1.5*IQR) | (df['salary'] > Q3 + 1.5*IQR)]
print(f"Found {len(outliers)} outliers in salary")
```

## Master EDA Skills

Our **Chapters 9 and 10** cover NumPy and Pandas with EDA-focused assignments using real datasets. [Start your data analysis journey](/register).
""",
    },
    {
        'title': 'Cross-Validation Explained Simply',
        'slug': 'cross-validation-explained-simply',
        'category': 'scikit-learn',
        'tags': 'scikit-learn, cross-validation, model-evaluation, machine-learning',
        'meta_description': 'Understand cross-validation in machine learning — why it matters, how it works, and how to use it in Scikit-Learn.',
        'content': """Evaluating your model on one train-test split can be misleading. Cross-validation gives you a more reliable estimate of how your model will perform on unseen data.

## Why Not Just Train-Test Split?

A single 70/30 split has a problem: your results depend on which data ended up in which split. Change the random seed and you might get very different accuracy.

## What Is Cross-Validation?

K-Fold cross-validation splits your data into K equal parts (folds). It then trains and tests K times, each time using a different fold as the test set:

1. Train on folds 2,3,4,5 — test on fold 1
2. Train on folds 1,3,4,5 — test on fold 2
3. Train on folds 1,2,4,5 — test on fold 3
4. Train on folds 1,2,3,5 — test on fold 4
5. Train on folds 1,2,3,4 — test on fold 5

The final score is the **average** across all K tests.

## Scikit-Learn Implementation

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"Mean accuracy: {scores.mean():.3f}")
print(f"Std deviation: {scores.std():.3f}")
print(f"All scores: {scores}")
```

## Choosing K

- **K=5** — Most common, good default
- **K=10** — More reliable but slower
- **K=len(data)** — Leave-One-Out, very slow but maximum data usage

## Stratified K-Fold

For classification, use stratified folds to maintain class proportions:

```python
from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv)
```

## Cross-Validation for Model Selection

Compare models fairly:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)
    print(f"{name}: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

## Learn Model Evaluation

Our **Chapter 11: Scikit-Learn** covers cross-validation, model selection, and evaluation metrics in depth. [Build reliable models](/register).
""",
    },
    {
        'title': 'Working with CSV and Excel Files in Python',
        'slug': 'working-with-csv-excel-python',
        'category': 'python-tips',
        'tags': 'python, csv, excel, pandas, file-handling',
        'meta_description': 'Learn how to read, write, and manipulate CSV and Excel files in Python using both the standard library and Pandas.',
        'content': """CSV and Excel files are the most common data formats you will encounter. Python makes working with both formats straightforward.

## Reading CSV with Python's csv Module

For simple tasks, the built-in `csv` module works fine:

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)
```

## Reading CSV with Pandas

For analysis, Pandas is far more powerful:

```python
import pandas as pd

df = pd.read_csv('data.csv')

# Useful parameters
df = pd.read_csv('data.csv',
    sep=';',                  # Different delimiter
    encoding='utf-8',         # Character encoding
    parse_dates=['date'],     # Auto-parse date columns
    na_values=['N/A', ''],    # Treat these as missing
    usecols=['name', 'age'],  # Only load specific columns
    nrows=1000,               # Load first 1000 rows only
)
```

## Writing CSV Files

```python
# With Pandas
df.to_csv('output.csv', index=False)

# With csv module
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'London'])
```

## Reading Excel Files

Pandas handles Excel files with `openpyxl` as a backend:

```python
# Read default sheet
df = pd.read_excel('report.xlsx')

# Read specific sheet
df = pd.read_excel('report.xlsx', sheet_name='Sales')

# Read all sheets
all_sheets = pd.read_excel('report.xlsx', sheet_name=None)
# Returns a dict: {'Sheet1': df1, 'Sheet2': df2, ...}
```

## Writing Excel Files

```python
# Simple export
df.to_excel('output.xlsx', index=False)

# Multiple sheets
with pd.ExcelWriter('report.xlsx') as writer:
    df_sales.to_excel(writer, sheet_name='Sales', index=False)
    df_costs.to_excel(writer, sheet_name='Costs', index=False)
```

## Large Files

For files that do not fit in memory, process in chunks:

```python
chunks = pd.read_csv('huge_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)
```

## Start Working with Data

Our **Chapter 10: Pandas** includes file I/O assignments with CSV and structured data. [Begin your data journey](/register).
""",
    },
    {
        'title': 'The Data Science Career Roadmap for 2025',
        'slug': 'data-science-career-roadmap-2025',
        'category': 'career',
        'tags': 'career, data-science, roadmap, skills, jobs',
        'meta_description': 'A practical roadmap for breaking into data science in 2025 — the skills, tools, and projects that actually get you hired.',
        'content': """The data science job market is competitive but full of opportunity. Here is a practical, no-nonsense roadmap for getting hired in 2025.

## Stage 1: Python Fundamentals (Weeks 1-4)

You need solid Python before anything else:
- Variables, data types, and operators
- Control flow (if/else, loops)
- Functions and modules
- Data structures (lists, dicts, tuples, sets)
- File I/O and error handling
- Object-oriented basics

Do not rush this stage. Weak fundamentals will slow you down later.

## Stage 2: NumPy and Pandas (Weeks 5-8)

These two libraries are non-negotiable:
- **NumPy:** arrays, vectorized operations, broadcasting, linear algebra basics
- **Pandas:** DataFrames, reading/writing data, cleaning, grouping, merging, pivoting

After this stage, you should be able to load a messy CSV, clean it, and produce summary statistics.

## Stage 3: Data Visualization (Weeks 9-10)

Learn at least one plotting library:
- **Matplotlib** for basic plots
- **Seaborn** for statistical visualizations
- Understand when to use bar charts, histograms, scatter plots, and heatmaps

## Stage 4: Machine Learning (Weeks 11-14)

Scikit-Learn is your entry point:
- Supervised learning (classification and regression)
- Model evaluation (cross-validation, metrics)
- Feature engineering and pipelines
- Common algorithms (Random Forest, Logistic Regression, KNN)

## Stage 5: SQL (Weeks 15-16)

Most data science jobs require SQL:
- SELECT, WHERE, GROUP BY, HAVING
- JOINs (INNER, LEFT, RIGHT)
- Subqueries and CTEs
- Window functions

## Stage 6: Projects (Weeks 17-20)

Build 2-3 portfolio projects:
1. **Data Cleaning + EDA** project (show Pandas skills)
2. **ML Classification** project (show modeling skills)
3. **End-to-end** project (data pipeline + model + insights)

## What Employers Actually Look For

Based on job postings:
1. Python (100% of listings)
2. SQL (90%)
3. Pandas (85%)
4. Scikit-Learn (70%)
5. Communication skills (70%)
6. NumPy (60%)

## Start Your Journey

Our structured curriculum covers Stages 1-4 completely, with auto-graded assignments at every step. [Create your free account](/register) and start building toward your data science career.
""",
    },
]


def get_pending_posts():
    """Return posts whose slugs do not exist in the database yet."""
    existing_slugs = {p.slug for p in BlogPost.query.with_entities(BlogPost.slug).all()}
    return [p for p in GROWTH_POSTS if p['slug'] not in existing_slugs]


def publish_next_post(author_id=None):
    """Insert and publish the next pending blog post.

    Returns the BlogPost instance or None if all posts are already published.
    """
    pending = get_pending_posts()
    if not pending:
        return None

    post_data = pending[0]
    post = BlogPost(
        title=post_data['title'],
        slug=post_data['slug'],
        content=post_data['content'],
        meta_description=post_data['meta_description'],
        tags=post_data['tags'],
        category=post_data.get('category'),
        author_id=author_id,
        is_published=True,
        published_at=datetime.utcnow(),
    )
    db.session.add(post)
    db.session.commit()
    return post


def publish_scheduled_posts():
    """Publish all posts where scheduled_at <= now and is_published is False.

    Returns the number of posts published.
    """
    now = datetime.utcnow()
    posts = BlogPost.query.filter(
        BlogPost.scheduled_at <= now,
        BlogPost.is_published == False  # noqa: E712
    ).all()

    count = 0
    for post in posts:
        post.is_published = True
        post.published_at = now
        count += 1

    if count:
        db.session.commit()
    return count


def seed_scheduled_posts(author_id=None, interval_days=3):
    """Insert all pending posts as scheduled drafts (not yet published).

    Posts are scheduled at intervals of `interval_days` starting from now.
    Returns the number of posts seeded.
    """
    from datetime import timedelta
    pending = get_pending_posts()
    if not pending:
        return 0

    now = datetime.utcnow()
    count = 0
    for i, post_data in enumerate(pending):
        post = BlogPost(
            title=post_data['title'],
            slug=post_data['slug'],
            content=post_data['content'],
            meta_description=post_data['meta_description'],
            tags=post_data['tags'],
            category=post_data.get('category'),
            author_id=author_id,
            is_published=False,
            scheduled_at=now + timedelta(days=i * interval_days),
        )
        db.session.add(post)
        count += 1

    db.session.commit()
    return count
