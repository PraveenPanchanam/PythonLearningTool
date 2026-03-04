CHAPTER_ORDER = 11

LESSONS = [
    {
        'title': 'Introduction to Machine Learning with Scikit-learn',
        'description': 'Discover the fundamentals of machine learning and learn the standard scikit-learn workflow - from preparing data to training your first model, using real-world examples like predicting house prices and detecting spam.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'what-is-machine-learning',
                'title': 'What is Machine Learning?',
                'diagram': {
                    'id': 'ch11-ml-pipeline',
                    'title': 'Machine Learning Pipeline with Scikit-Learn',
                    'file': 'diagrams/ch11-ml-pipeline.svg',
                    'data_file': 'diagrams/excalidraw-data/ch11-ml-pipeline.json',
                },
                'content': """## What is Machine Learning?

**Machine learning (ML)** is a way to teach computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every scenario.

### How ML Differs from Traditional Programming

In traditional programming, you write exact rules:

```
IF email contains "free money" AND sender is unknown THEN mark as spam
```

In machine learning, you show the computer thousands of examples of spam and non-spam emails, and it **learns the rules on its own**.

| Traditional Programming      | Machine Learning               |
|------------------------------|--------------------------------|
| You write the rules          | The computer learns the rules  |
| Rules are fixed              | Rules improve with more data   |
| Works for simple patterns    | Works for complex patterns     |

### Real-World ML Applications

Machine learning is everywhere in daily life:

- **Email spam filters** - Gmail learns which emails are spam based on millions of examples
- **House price prediction** - Zillow estimates home values from features like square footage, bedrooms, location
- **Medical diagnosis** - Algorithms help doctors detect diseases from X-rays and blood tests
- **Recommendation systems** - Netflix and Spotify suggest content based on your past behavior
- **Self-driving cars** - Vehicles learn to recognize pedestrians, traffic signs, and road lanes

### The Two Main Types of ML

| Type              | What It Does                           | Example                          |
|-------------------|----------------------------------------|----------------------------------|
| **Regression**    | Predicts a continuous number           | House price, salary, temperature |
| **Classification**| Predicts a category or label           | Spam/not spam, cat/dog, pass/fail|

### What is Scikit-learn?

**Scikit-learn** (often written as `sklearn`) is Python's most popular machine learning library. It provides a consistent, clean API for:

- Splitting data into training and testing sets
- Training models (linear regression, decision trees, etc.)
- Evaluating model performance
- Making predictions on new data

```python
# The standard import
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```""",
                'exercise': None,
            },
            {
                'id': 'sklearn-workflow',
                'title': 'The Scikit-learn Workflow',
                'content': """## The Scikit-learn Workflow

Every scikit-learn project follows the same five-step workflow. Once you learn this pattern, you can apply it to any ML algorithm.

### The 5 Steps

```
1. Prepare Data  -->  2. Split Data  -->  3. Create Model
       |                                        |
       v                                        v
  (Features X,        4. Train Model  <--  (Choose algorithm)
   Labels y)                |
                            v
                     5. Evaluate & Predict
```

### Step 1: Prepare Your Data

ML models need numeric input organized into:
- **X** (Features): The input data the model learns from (like square footage, number of bedrooms)
- **y** (Target/Labels): What you want to predict (like house price)

```python
import numpy as np

# House sizes (sq ft) as features
X = np.array([[850], [1200], [1500], [1800], [2200]])

# House prices as targets
y = np.array([150000, 210000, 260000, 310000, 380000])
```

### Step 2: Split into Training and Testing Sets

You never test a model on the same data it learned from. That would be like giving a student the exact same questions from the study guide on the exam - it doesn't tell you if they truly understand.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

- **`test_size=0.3`** means 30% of data goes to testing, 70% to training
- **`random_state=42`** ensures the split is the same every time you run the code

### Step 3: Create the Model

Choose an algorithm and create an instance:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

### Step 4: Train (Fit) the Model

The `.fit()` method teaches the model patterns from the training data:

```python
model.fit(X_train, y_train)
```

### Step 5: Evaluate and Predict

Check how well the model performs on unseen test data:

```python
score = model.score(X_test, y_test)  # R-squared score
predictions = model.predict(X_test)   # Predict test values
```""",
                'exercise': {
                    'instructions': 'Follow the scikit-learn workflow: split the given data into training and testing sets (test_size=0.25, random_state=42), then print the number of training samples and testing samples.',
                    'starter_code': 'import numpy as np\nfrom sklearn.model_selection import train_test_split\n\n# Study hours -> exam scores\nX = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])\ny = np.array([45, 55, 60, 68, 75, 80, 88, 92])\n\n# Split into training and testing sets\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.25, random_state=42\n)\n\n# Print the sizes\nprint(f"Training set size: {len(X_train)}")\nprint(f"Test set size: {len(X_test)}")\n',
                    'expected_output': 'Training set size: 6\nTest set size: 2',
                    'hint': 'Use train_test_split(X, y, test_size=0.25, random_state=42). The function returns four arrays: X_train, X_test, y_train, y_test. Use len() to count samples.',
                },
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange the machine learning workflow steps in the correct order:',
                    'code_blocks': [
                        '# Step 1: Prepare data (X features, y target)',
                        '# Step 2: Split into train and test sets',
                        '# Step 3: Create and train the model',
                        '# Step 4: Make predictions',
                        '# Step 5: Evaluate the results',
                    ],
                    'explanation': 'The ML workflow always follows this order: prepare your data, split it for honest testing, train your model, make predictions, and then evaluate how well it did!',
                },
            },
            {
                'id': 'train-test-split-depth',
                'title': 'Understanding train_test_split',
                'content': """## Understanding train_test_split

The `train_test_split` function is arguably the most important utility in scikit-learn. It ensures your model evaluation is honest and reliable.

### Why Split Data?

Imagine a student who memorizes every answer in a textbook. They score 100% on questions from that textbook but fail when asked new questions. This is called **overfitting** - the model memorizes training data instead of learning general patterns.

By holding out test data that the model never sees during training, we get an honest estimate of how well it will perform on real, new data.

### Parameters Explained

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,      # 30% for testing
    random_state=42,     # reproducible results
    shuffle=True         # shuffle before splitting (default)
)
```

| Parameter      | Default   | Description                                    |
|----------------|-----------|------------------------------------------------|
| `test_size`    | 0.25      | Fraction of data for testing (0.0 to 1.0)     |
| `train_size`   | complement| Fraction for training (usually inferred)       |
| `random_state` | None      | Seed for reproducibility                       |
| `shuffle`      | True      | Shuffle data before splitting                  |

### The Importance of random_state

Without `random_state`, each run produces a different split:

```python
# Run 1: Alice in training, Bob in testing
# Run 2: Bob in training, Alice in testing
# Results change every time!
```

With `random_state=42`, the split is identical every time. This is crucial for:
- **Debugging** - reproducing the exact same results
- **Comparing models** - ensuring fair comparisons on the same data split
- **Sharing results** - others can verify your work

### Real-World Split Ratios

| Dataset Size  | Typical Split        | Reason                              |
|---------------|----------------------|-------------------------------------|
| Small (<1000) | 70/30 or 75/25       | Need enough test data for evaluation|
| Medium         | 80/20                | Standard practice                   |
| Large (>100K) | 90/10 or 95/5        | Even 5% is thousands of test samples|

### What train_test_split Returns

The function always returns four arrays in this order:

```python
X_train  # Features for training
X_test   # Features for testing
y_train  # Labels for training
y_test   # Labels for testing (the "answers" for evaluation)
```""",
                'exercise': None,
                'game': {
                    'type': 'fill_blank',
                    'instructions': 'Fill in the blanks to split data into training and testing sets:',
                    'code_template': 'from sklearn.model_selection import {0}\n\nX_train, X_test, y_train, y_test = {1}(\n    X, y, test_size={2}, random_state=42\n)',
                    'blanks': [
                        {'id': 0, 'answer': 'train_test_split', 'hint': 'What function splits data into train and test?'},
                        {'id': 1, 'answer': 'train_test_split', 'hint': 'Call the same function we imported!'},
                        {'id': 2, 'answer': '0.3', 'hint': 'What decimal means 30% for testing?'},
                    ],
                    'explanation': 'We import train_test_split from sklearn, then call it with our data. test_size=0.3 means 30% goes to testing and 70% to training. The random_state ensures the same split every time!',
                },
            },
            {
                'id': 'first-model-complete',
                'title': 'Your First Complete ML Model',
                'content': """## Your First Complete ML Model

Let us put together the complete workflow with a realistic example: predicting exam scores from study hours.

### The Full Pipeline

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Prepare data
# Study hours as features, exam scores as targets
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([45, 55, 60, 68, 75, 80, 88, 92])

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 3: Create model
model = LinearRegression()

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Evaluate
score = model.score(X_test, y_test)
print(f"Model R-squared: {score:.2f}")

# Step 6: Predict for new data
new_hours = np.array([[5]])
predicted = model.predict(new_hours)
print(f"Predicted score for 5 hours: {predicted[0]:.1f}")
```

### Understanding the Output

- **R-squared (R2)** measures how well the model fits the data, from 0 to 1
  - 1.0 = perfect predictions
  - 0.5 = model explains 50% of the variation
  - 0.0 = model is no better than predicting the average every time

### The Consistent API

Every scikit-learn model follows the same pattern:

```python
model = SomeAlgorithm()     # Create
model.fit(X_train, y_train) # Train
model.predict(X_new)        # Predict
model.score(X_test, y_test) # Evaluate
```

Whether you use LinearRegression, DecisionTreeClassifier, or any other algorithm, the methods are the same. Learn the pattern once, use it everywhere.""",
                'exercise': {
                    'instructions': 'Complete the full ML pipeline: split the data, train a LinearRegression model, and print the R-squared score and a prediction for a student who studies 12 hours.',
                    'starter_code': 'import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\n\n# Study hours -> exam scores\nX = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])\ny = np.array([45, 55, 60, 68, 75, 80, 88, 92])\n\n# Split data (25% test, random_state=42)\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.25, random_state=42\n)\n\n# Create and train the model\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\n\n# Evaluate the model\nscore = model.score(X_test, y_test)\nprint(f"R-squared: {score:.2f}")\n\n# Predict score for a student who studies 12 hours\nnew_student = np.array([[12]])\npredicted = model.predict(new_student)\nprint(f"Predicted score for 12 hours: {predicted[0]:.1f}")\n',
                    'expected_output': 'R-squared: 0.99\nPredicted score for 12 hours: 112.7',
                    'hint': 'Follow the standard sklearn workflow: train_test_split() to split, model.fit() to train, model.score() to evaluate, and model.predict() for new predictions.',
                },
            },
            {
                'id': 'features-and-targets',
                'title': 'Features vs. Targets in Real Life',
                'content': """## Features vs. Targets in Real Life

Understanding how to identify **features** (input) and **targets** (output) is the most important conceptual skill in machine learning.

### The Key Question

Always ask yourself: **"What do I know, and what do I want to predict?"**

- What you **know** = Features (X)
- What you want to **predict** = Target (y)

### Real-World Examples

| Scenario               | Features (X)                            | Target (y)             |
|------------------------|-----------------------------------------|------------------------|
| House pricing          | Sq ft, bedrooms, location, age          | Sale price             |
| Spam detection         | Word count, links, caps, sender         | Spam or not spam       |
| Medical diagnosis      | Age, blood pressure, cholesterol, BMI   | Disease present or not |
| Salary prediction      | Years experience, education, skills     | Annual salary          |
| Customer churn         | Usage, complaints, contract length      | Will leave or stay     |
| Crop yield             | Rainfall, temperature, soil type        | Harvest amount         |

### Feature Engineering

In practice, choosing and creating the right features is often more important than choosing the right algorithm. This process is called **feature engineering**:

```python
import numpy as np

# Raw data: house info
square_feet = [1200, 1500, 1800]
bedrooms = [2, 3, 4]
year_built = [1990, 2005, 2020]

# Create feature matrix (each row = one house, each column = one feature)
X = np.array([
    [1200, 2, 1990],
    [1500, 3, 2005],
    [1800, 4, 2020]
])

# Target: house prices
y = np.array([200000, 280000, 360000])
```

### Key Takeaways

1. **More features is not always better** - irrelevant features can confuse the model
2. **Features must be numeric** for most algorithms - text and categories need conversion
3. **Feature scale matters** - a feature ranging from 0-1000000 (like salary) can dominate one ranging from 0-5 (like bedrooms)
4. **Domain knowledge helps** - understanding the problem helps you pick the best features""",
                'exercise': None,
            },
        ],
    },
    {
        'title': 'Regression Models',
        'description': 'Learn to build and evaluate Linear Regression models for predicting continuous values like salaries and house prices, using key metrics like MSE and R-squared.',
        'order': 2,
        'item_order': 3,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'linear-regression-explained',
                'title': 'Linear Regression Explained',
                'content': """## Linear Regression Explained

**Linear Regression** is the most fundamental ML algorithm. It finds the best straight line through your data to make predictions.

### The Intuition

Imagine plotting house sizes (x-axis) against prices (y-axis) on a graph. You can see that bigger houses cost more - there is a clear upward trend. Linear regression finds the **best-fit line** through these points.

The equation of this line is:

```
y = coefficient * X + intercept
```

- **Coefficient (slope)**: How much y changes for each unit increase in X
- **Intercept**: The value of y when X is zero

### Real-Life Example: House Price Prediction

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# House sizes (sq ft) and their sale prices
X = np.array([[850], [900], [1100], [1200], [1400],
              [1500], [1700], [1800], [2000], [2200],
              [2400], [2500]])
y = np.array([150000, 170000, 200000, 215000, 250000,
              260000, 300000, 310000, 350000, 370000,
              410000, 420000])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Coefficient: {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
```

### Interpreting the Results

If the coefficient is 158.93, it means:
- **For every additional square foot, the price increases by about $158.93**

If the intercept is 26011.90, it means:
- **The base price (for a theoretical 0 sq ft house) would be $26,011.90**

So for a 1600 sq ft house: `158.93 * 1600 + 26011.90 = $280,299.90`

### When to Use Linear Regression

Linear regression works best when:
- The relationship between features and target is roughly **linear** (a straight line)
- You want to predict a **continuous number** (price, temperature, score)
- You want an **interpretable** model (easy to explain why the prediction was made)""",
                'exercise': None,
            },
            {
                'id': 'evaluation-metrics',
                'title': 'Evaluation Metrics: MSE and R-squared',
                'content': """## Evaluation Metrics: MSE and R-squared

After training a model, you need to measure how good its predictions are. Two key metrics for regression are **Mean Squared Error (MSE)** and **R-squared (R2)**.

### Mean Squared Error (MSE)

MSE measures the average squared difference between predicted and actual values:

```
MSE = average of (predicted - actual)^2
```

- **Lower is better** - zero means perfect predictions
- Squaring penalizes large errors more than small ones
- Units are squared (e.g., dollars-squared for price prediction)

```python
from sklearn.metrics import mean_squared_error

# If actual prices are [200000, 300000]
# And predictions are [210000, 290000]
# MSE = ((210000-200000)^2 + (290000-300000)^2) / 2 = 100,000,000
```

### R-squared (R2 Score)

R-squared tells you what fraction of the target's variation your model explains:

- **R2 = 1.0** - Perfect predictions
- **R2 = 0.5** - Model explains 50% of the variation
- **R2 = 0.0** - Model is no better than always predicting the average
- **R2 < 0** - Model is worse than predicting the average (very bad)

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2:.2f}")
```

### Real-Life Analogy

Think of R-squared like a weather forecast accuracy:
- R2 = 0.90 means the model predicts 90% of the variation correctly - like a reliable weather app
- R2 = 0.50 means it gets it right about half the time - unreliable
- R2 = 0.10 means almost useless - might as well flip a coin

### Comparing Metrics

| Metric    | Range          | Good Value    | What It Tells You                    |
|-----------|----------------|---------------|--------------------------------------|
| MSE       | 0 to infinity  | Close to 0    | Average prediction error (squared)   |
| R-squared | -inf to 1.0    | Close to 1.0  | How much variation the model explains|

### Which to Use?

- **R-squared** is better for comparing models across different datasets (it is normalized)
- **MSE** is better for understanding the actual magnitude of errors in your data's units""",
                'exercise': None,
            },
            {
                'id': 'salary-prediction',
                'title': 'Building a Salary Prediction Model',
                'content': """## Building a Salary Prediction Model

Let us build a complete regression model for a classic real-world problem: predicting salary based on years of experience.

### The Scenario

You work in HR and want to build a tool that estimates fair salaries based on experience level. You have historical data:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Years of experience -> Annual salary
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([30000, 35000, 42000, 48000, 55000,
              60000, 68000, 73000, 80000, 88000])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Salary increase per year: ${model.coef_[0]:,.2f}")
print(f"Starting salary (0 years): ${model.intercept_:,.2f}")
print(f"R-squared: {r2_score(y_test, y_pred):.2f}")
```

### Interpreting the Coefficients

The coefficient tells you the **salary increase per additional year of experience**. If it is $6,396.55, you can tell a hiring manager:

> "On average, each additional year of experience adds about $6,400 to the salary."

### Making Predictions

Once trained, the model can predict salaries for any experience level:

```python
# What should someone with 12 years experience earn?
new_exp = np.array([[12]])
predicted = model.predict(new_exp)
print(f"Predicted salary for 12 years: ${predicted[0]:,.2f}")
```

### Limitations of Simple Linear Regression

Real salary data has complications:
- Salary growth often **levels off** at senior levels (not perfectly linear)
- **Education, location, and industry** also matter
- A single feature (years) cannot capture the full picture

This is why more advanced models and multiple features exist - topics we build toward in later lessons.""",
                'exercise': {
                    'instructions': 'Build a salary prediction model using the given data. Print the coefficient (salary increase per year), intercept (base salary), R-squared score, and a prediction for someone with 12 years of experience.',
                    'starter_code': 'import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import r2_score\n\n# Years of experience -> Annual salary\nX = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])\ny = np.array([30000, 35000, 42000, 48000, 55000,\n              60000, 68000, 73000, 80000, 88000])\n\n# Split data (20% test, random_state=42)\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42\n)\n\n# Create and train the model\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\ny_pred = model.predict(X_test)\n\n# Print results\nprint(f"Coefficient (salary increase per year): {model.coef_[0]:.2f}")\nprint(f"Intercept (base salary): {model.intercept_:.2f}")\nprint(f"R-squared: {r2_score(y_test, y_pred):.2f}")\n\n# Predict salary for 12 years experience\nnew_exp = np.array([[12]])\npredicted = model.predict(new_exp)\nprint(f"Predicted salary for 12 years: {predicted[0]:.2f}")\n',
                    'expected_output': 'Coefficient (salary increase per year): 6396.55\nIntercept (base salary): 22818.97\nR-squared: 1.00\nPredicted salary for 12 years: 99577.59',
                    'hint': 'Follow the standard workflow: train_test_split, fit the model, then access model.coef_[0] for the slope, model.intercept_ for the intercept, and r2_score() for evaluation.',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Think about what type of problem this is:',
                    'code_snippet': 'Predicting the price of a house\nbased on its size, bedrooms,\nand location.',
                    'question': 'What type of machine learning task is this?',
                    'options': [
                        {'text': 'Regression (predicting a number)', 'correct': True},
                        {'text': 'Classification (predicting a category)', 'correct': False},
                        {'text': 'Clustering (grouping similar items)', 'correct': False},
                        {'text': 'None of the above', 'correct': False},
                    ],
                    'explanation': 'Since we are predicting a continuous number (price in dollars), this is a regression task. Classification would be predicting categories like "expensive" vs "affordable".',
                },
            },
            {
                'id': 'house-price-model',
                'title': 'House Price Prediction with Evaluation',
                'content': """## House Price Prediction with Evaluation

Let us build a more complete example with thorough evaluation - predicting house prices from square footage.

### The Dataset

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# House sizes (sq ft) and prices
X = np.array([[850], [900], [1100], [1200], [1400],
              [1500], [1700], [1800], [2000], [2200],
              [2400], [2500]])
y = np.array([150000, 170000, 200000, 215000, 250000,
              260000, 300000, 310000, 350000, 370000,
              410000, 420000])
```

### Training and Evaluating

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:,.2f}")
print(f"R-squared: {r2:.4f}")
```

### Making a Business Decision

A real estate agent asks: "What should a 1600 sq ft house be listed for?"

```python
new_house = np.array([[1600]])
predicted_price = model.predict(new_house)
print(f"Suggested listing price: ${predicted_price[0]:,.2f}")
```

### Understanding the Error

The MSE tells you about prediction uncertainty. If MSE is 53,921,308, the root mean squared error (RMSE) is:

```python
import math
rmse = math.sqrt(mse)
print(f"RMSE: ${rmse:,.2f}")
```

RMSE is in the same units as your target (dollars), making it easier to interpret: "On average, our predictions are off by about $X."

### Best Practices for Regression

1. **Always plot your data first** if possible - to check if a linear model makes sense
2. **Check R-squared** - values above 0.8 are generally considered good
3. **Look at residuals** - the differences between predicted and actual values should be random
4. **Do not extrapolate too far** - predicting for a 10,000 sq ft house when your data only goes to 2,500 is risky""",
                'exercise': {
                    'instructions': 'Build a house price prediction model. Print the coefficient, intercept, R-squared score, and a predicted price for a 1600 sq ft house.',
                    'starter_code': 'import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import r2_score\n\n# House sizes (sq ft) and prices\nX = np.array([[850], [900], [1100], [1200], [1400],\n              [1500], [1700], [1800], [2000], [2200],\n              [2400], [2500]])\ny = np.array([150000, 170000, 200000, 215000, 250000,\n              260000, 300000, 310000, 350000, 370000,\n              410000, 420000])\n\n# Split data (25% test, random_state=42)\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.25, random_state=42\n)\n\n# Train the model\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\ny_pred = model.predict(X_test)\n\n# Print evaluation\nprint(f"Coefficient (price per sq ft): {model.coef_[0]:.2f}")\nprint(f"Intercept: {model.intercept_:.2f}")\nprint(f"R-squared: {r2_score(y_test, y_pred):.4f}")\n\n# Predict price for a 1600 sq ft house\nnew_house = np.array([[1600]])\npredicted = model.predict(new_house)\nprint(f"Predicted price for 1600 sq ft: {predicted[0]:.2f}")\n',
                    'expected_output': 'Coefficient (price per sq ft): 158.93\nIntercept: 26011.90\nR-squared: 0.9959\nPredicted price for 1600 sq ft: 280297.62',
                    'hint': 'Follow the standard workflow. Access model.coef_[0] for the slope (price per sq ft) and model.intercept_ for the base price. Use r2_score(y_test, y_pred) with :.4f format.',
                },
            },
            {
                'id': 'regression-pitfalls',
                'title': 'Common Regression Pitfalls',
                'content': """## Common Regression Pitfalls

Understanding what can go wrong is just as important as knowing how to build a model.

### Pitfall 1: Forgetting to Reshape Data

Scikit-learn expects 2D arrays for features (X). A common mistake:

```python
import numpy as np

# WRONG - 1D array
X = np.array([1, 2, 3, 4, 5])  # shape: (5,)

# CORRECT - 2D array (each sample is a row)
X = np.array([[1], [2], [3], [4], [5]])  # shape: (5, 1)

# Quick fix: reshape
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
```

### Pitfall 2: Data Leakage

Never include future information in your features. For example, if predicting monthly sales, do not include "total yearly sales" as a feature - that number is not available at prediction time.

### Pitfall 3: Overfitting vs. Underfitting

| Problem        | Symptoms                              | Solution                     |
|----------------|---------------------------------------|------------------------------|
| **Overfitting** | High training score, low test score  | Simpler model, more data     |
| **Underfitting**| Low training score, low test score   | More complex model, better features|

```python
# Check for overfitting
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training R2: {train_score:.2f}")
print(f"Testing R2: {test_score:.2f}")
# Big gap = overfitting
```

### Pitfall 4: Not Using random_state

Without `random_state`, your results change every run, making debugging and comparison impossible:

```python
# BAD - different results each run
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# GOOD - reproducible results
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Key Takeaways

1. Always use `random_state` for reproducibility
2. Check both training and testing scores to detect overfitting
3. Make sure your features are 2D arrays
4. Do not include information that would not be available at prediction time
5. Start simple (LinearRegression) and add complexity only if needed""",
                'exercise': None,
            },
        ],
    },
    {
        'title': 'Classification Models',
        'description': 'Learn to build classification models that predict categories like spam/not spam and pass/fail, using Logistic Regression and Decision Trees with real-world examples.',
        'order': 3,
        'item_order': 6,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'classification-vs-regression',
                'title': 'Classification vs. Regression',
                'content': """## Classification vs. Regression

While regression predicts a **continuous number** (like price or temperature), classification predicts a **category** or **class label**.

### Real-World Classification Examples

| Problem                    | Classes                  | Features Used                    |
|----------------------------|--------------------------|----------------------------------|
| Email spam detection       | Spam / Not Spam          | Word count, links, caps words    |
| Medical diagnosis          | Sick / Healthy           | Age, temperature, heart rate     |
| Loan approval              | Approve / Reject         | Income, credit score, debt       |
| Student exam result        | Pass / Fail              | Study hours, attendance          |
| Image recognition          | Cat / Dog / Bird         | Pixel values                     |
| Customer churn             | Stay / Leave             | Usage, complaints, tenure        |

### Binary vs. Multi-class Classification

- **Binary classification**: Two possible outcomes (spam/not spam, pass/fail)
- **Multi-class classification**: Three or more outcomes (cat/dog/bird, A/B/C/D/F grade)

### How Classification Works

Instead of drawing a line through data points (regression), classification finds a **decision boundary** that separates different classes:

```
Spam emails: X X X X
                        --- decision boundary ---
Not spam:    O O O O O
```

The model learns where this boundary should be from the training data, then uses it to classify new data points.

### Classification in Scikit-learn

The workflow is identical to regression - only the algorithm changes:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Same pattern: create, fit, predict, evaluate
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)
```

Notice how scikit-learn's consistent API means you already know how to use classification models.""",
                'exercise': None,
            },
            {
                'id': 'logistic-regression',
                'title': 'Logistic Regression for Classification',
                'content': """## Logistic Regression for Classification

Despite its name, **Logistic Regression** is a **classification** algorithm. It predicts the probability that a data point belongs to a particular class.

### How It Works

Logistic Regression applies a special function (the sigmoid/logistic function) that converts any number into a probability between 0 and 1:

- If probability >= 0.5, predict class 1 (e.g., "spam")
- If probability < 0.5, predict class 0 (e.g., "not spam")

### Real-Life Example: Exam Pass/Fail

Imagine predicting whether students will pass an exam based on their study hours and attendance percentage:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Features: [study_hours, attendance_percentage]
X = np.array([
    [2, 60], [5, 90], [1, 40], [4, 85], [6, 95],
    [3, 70], [7, 92], [2, 50], [5, 80], [1, 30],
    [4, 75], [6, 88], [3, 65], [8, 98], [2, 55]
])
# Target: 0 = Fail, 1 = Pass
y = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
```

### Understanding Accuracy

**Accuracy** is the simplest classification metric:

```
Accuracy = correct predictions / total predictions
```

An accuracy of 0.80 means the model correctly predicted 80% of the test cases.

### Making Predictions

```python
# Will a student with 4 hours study and 80% attendance pass?
new_student = np.array([[4, 80]])
prediction = model.predict(new_student)
print("Pass" if prediction[0] == 1 else "Fail")
```

### When to Use Logistic Regression

- When you need a **fast, interpretable** classification model
- When the relationship between features and the outcome is roughly **linear**
- When you want **probability estimates** (not just class labels)
- As a **baseline model** to compare more complex algorithms against""",
                'exercise': {
                    'instructions': 'Build a Logistic Regression model to predict exam pass/fail. Print the predictions array, actual values array, accuracy score, and a prediction for a new student with 4 study hours and 80% attendance.',
                    'starter_code': 'import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\n\n# Features: [study_hours, attendance_pct]\nX = np.array([\n    [2, 60], [5, 90], [1, 40], [4, 85], [6, 95],\n    [3, 70], [7, 92], [2, 50], [5, 80], [1, 30],\n    [4, 75], [6, 88], [3, 65], [8, 98], [2, 55]\n])\ny = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0])\n\n# Split data (30% test, random_state=42)\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.3, random_state=42\n)\n\n# Train Logistic Regression\nmodel = LogisticRegression(random_state=42)\nmodel.fit(X_train, y_train)\ny_pred = model.predict(X_test)\n\n# Print results\nprint(f"Predictions: {y_pred}")\nprint(f"Actual:      {y_test}")\nprint(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")\n\n# Predict for new student\nnew_student = np.array([[4, 80]])\nresult = model.predict(new_student)\nprint(f"Student with 4 hrs study, 80% attendance: {\'Pass\' if result[0] == 1 else \'Fail\'}")\n',
                    'expected_output': 'Predictions: [0 1 0 1 1]\nActual:      [0 1 0 1 0]\nAccuracy: 0.80\nStudent with 4 hrs study, 80% attendance: Pass',
                    'hint': 'Follow the standard sklearn workflow with LogisticRegression(random_state=42). Use accuracy_score(y_test, y_pred) to measure performance.',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'If a model correctly predicted 8 out of 10 test cases, what is the accuracy? Type just the number!',
                    'code_snippet': 'correct = 8\ntotal = 10\naccuracy = correct / total\nprint(accuracy)',
                    'expected_output': '0.8',
                    'explanation': 'Accuracy = correct predictions / total predictions. So 8 / 10 = 0.8, which means the model is 80% accurate!',
                },
            },
            {
                'id': 'decision-tree-classifier',
                'title': 'Decision Tree Classifier',
                'content': """## Decision Tree Classifier

A **Decision Tree** makes predictions by asking a series of yes/no questions about the features, like a flowchart.

### How It Works

Think of how a doctor diagnoses an illness:

```
Is temperature > 100.5F?
├── Yes: Is heart rate > 85?
│   ├── Yes: Likely sick
│   └── No: Monitor closely
└── No: Is cough present?
    ├── Yes: Possible cold
    └── No: Likely healthy
```

A Decision Tree classifier learns these rules automatically from the training data.

### Building a Decision Tree

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42, max_depth=3)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Key Parameters

| Parameter   | Description                                      | Default |
|-------------|--------------------------------------------------|---------|
| `max_depth` | Maximum depth of the tree                        | None    |
| `min_samples_split` | Minimum samples to split a node          | 2       |
| `random_state` | Seed for reproducibility                      | None    |

### Advantages of Decision Trees

1. **Easy to understand** - you can visualize the decision process
2. **No feature scaling needed** - unlike many other algorithms
3. **Handles both numeric and categorical features**
4. **Captures non-linear patterns** - unlike logistic regression

### Disadvantages

1. **Prone to overfitting** - can memorize training data
2. **Unstable** - small data changes can produce very different trees
3. **Biased** - can favor features with many possible values

### max_depth Controls Complexity

Setting `max_depth` limits how deep the tree can grow, preventing overfitting:

```python
# Simple tree (less overfitting, might underfit)
simple_model = DecisionTreeClassifier(random_state=42, max_depth=2)

# Complex tree (might overfit)
complex_model = DecisionTreeClassifier(random_state=42, max_depth=10)
```

Think of `max_depth` like the number of questions in a game of 20 Questions - too few and you cannot narrow down the answer, too many and you are overthinking it.""",
                'exercise': None,
                'game': {
                    'type': 'quiz',
                    'instructions': 'Think about how Decision Trees work:',
                    'code_snippet': 'model = DecisionTreeClassifier(\n    random_state=42,\n    max_depth=3\n)',
                    'question': 'What does setting max_depth=3 do?',
                    'options': [
                        {'text': 'Limits the tree to 3 levels of yes/no questions', 'correct': True},
                        {'text': 'Uses only the 3 best features', 'correct': False},
                        {'text': 'Trains the model 3 times', 'correct': False},
                        {'text': 'Splits data into 3 groups', 'correct': False},
                    ],
                    'explanation': 'max_depth=3 means the tree can ask at most 3 levels of yes/no questions. This prevents overfitting — like limiting a game of 20 Questions to just 3 questions, keeping the model simple and general!',
                },
            },
            {
                'id': 'comparing-classifiers',
                'title': 'Comparing Classification Models',
                'content': """## Comparing Classification Models

In practice, you often try multiple algorithms on the same data and compare their performance. Let us build both Logistic Regression and Decision Tree models on the same dataset.

### Real-Life Example: Fruit Classification

A sorting machine at a fruit packaging plant needs to distinguish apples from oranges based on weight and diameter:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Features: [weight_grams, diameter_cm]
X = np.array([
    [150, 7.0], [160, 7.5], [170, 8.0], [140, 6.5], [180, 8.5],
    [130, 6.0], [200, 9.0], [190, 8.8], [155, 7.2], [175, 8.2],
    [145, 6.8], [210, 9.5], [165, 7.6], [185, 8.6], [135, 6.2],
    [195, 9.2], [152, 7.1], [172, 8.1], [142, 6.6], [205, 9.3]
])
# 0 = Apple, 1 = Orange
y = np.array([0, 0, 0, 0, 1, 0, 1, 1, 0, 1,
              0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model 1: Logistic Regression
lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)
lr_acc = accuracy_score(y_test, lr.predict(X_test))

# Model 2: Decision Tree
dt = DecisionTreeClassifier(random_state=42, max_depth=3)
dt.fit(X_train, y_train)
dt_acc = accuracy_score(y_test, dt.predict(X_test))

print(f"Logistic Regression: {lr_acc:.2f}")
print(f"Decision Tree: {dt_acc:.2f}")
```

### How to Choose Between Models

| Consideration          | Logistic Regression           | Decision Tree              |
|------------------------|-------------------------------|----------------------------|
| Interpretability       | Moderate (coefficients)       | High (flowchart-like)      |
| Speed                  | Very fast                     | Fast                       |
| Non-linear patterns    | Cannot capture                | Can capture                |
| Overfitting risk       | Low                           | Higher                     |
| Feature scaling needed | Yes (recommended)             | No                         |

### General Advice

1. **Start with Logistic Regression** as a baseline - it is fast and robust
2. **Try Decision Tree** if you suspect non-linear patterns
3. **Compare on the same test set** for fair comparison
4. **Always use random_state** for reproducibility""",
                'exercise': {
                    'instructions': 'Train both Logistic Regression and Decision Tree classifiers on the fruit data. Print each model\'s accuracy and make a prediction for a new fruit weighing 168g with 7.8cm diameter using the Decision Tree.',
                    'starter_code': 'import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score\n\n# Fruit data: [weight_grams, diameter_cm]\nX = np.array([\n    [150, 7.0], [160, 7.5], [170, 8.0], [140, 6.5], [180, 8.5],\n    [130, 6.0], [200, 9.0], [190, 8.8], [155, 7.2], [175, 8.2],\n    [145, 6.8], [210, 9.5], [165, 7.6], [185, 8.6], [135, 6.2],\n    [195, 9.2], [152, 7.1], [172, 8.1], [142, 6.6], [205, 9.3]\n])\ny = np.array([0, 0, 0, 0, 1, 0, 1, 1, 0, 1,\n              0, 1, 0, 1, 0, 1, 0, 1, 0, 1])\n\n# Split data\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.3, random_state=42\n)\n\n# Train Logistic Regression\nlr = LogisticRegression(random_state=42)\nlr.fit(X_train, y_train)\nlr_acc = accuracy_score(y_test, lr.predict(X_test))\n\n# Train Decision Tree\ndt = DecisionTreeClassifier(random_state=42, max_depth=3)\ndt.fit(X_train, y_train)\ndt_acc = accuracy_score(y_test, dt.predict(X_test))\n\n# Print comparison\nprint(f"Logistic Regression Accuracy: {lr_acc:.2f}")\nprint(f"Decision Tree Accuracy: {dt_acc:.2f}")\n\n# Predict new fruit using Decision Tree\nnew_fruit = np.array([[168, 7.8]])\nprediction = dt.predict(new_fruit)\nprint(f"Prediction for 168g, 7.8cm fruit: {\'Orange\' if prediction[0] == 1 else \'Apple\'}")\n',
                    'expected_output': 'Logistic Regression Accuracy: 0.83\nDecision Tree Accuracy: 0.83\nPrediction for 168g, 7.8cm fruit: Apple',
                    'hint': 'Train both models using the same X_train, y_train data. Use accuracy_score(y_test, model.predict(X_test)) for each model. Use dt.predict() for the new fruit prediction.',
                },
            },
            {
                'id': 'classification-best-practices',
                'title': 'Classification Best Practices',
                'content': """## Classification Best Practices

As you build more classification models, keep these guidelines in mind to avoid common mistakes and produce reliable results.

### 1. Check Class Balance

If 95% of your emails are not spam, a model that always predicts "not spam" gets 95% accuracy - but it is useless. Always check:

```python
import numpy as np

# Check how balanced the classes are
unique, counts = np.unique(y, return_counts=True)
for label, count in zip(unique, counts):
    print(f"Class {label}: {count} samples ({count/len(y)*100:.1f}%)")
```

### 2. Look Beyond Accuracy

For imbalanced datasets, consider these additional metrics:

- **Precision**: Of all predicted positives, how many were actually positive?
- **Recall**: Of all actual positives, how many did we catch?
- **F1-score**: Harmonic mean of precision and recall

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

### 3. Use Consistent random_state

Always set `random_state` in both `train_test_split` and the model:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = LogisticRegression(random_state=42)
```

### 4. Start Simple, Then Add Complexity

```
Logistic Regression  -->  Decision Tree  -->  Random Forest  -->  ...
    (baseline)          (if non-linear)      (if overfitting)
```

### 5. Real-World Deployment Considerations

| Consideration       | Question to Ask                                    |
|--------------------|----------------------------------------------------|
| Cost of errors     | Is a false positive or false negative worse?       |
| Data freshness     | Does the model need retraining as data changes?    |
| Interpretability   | Does the stakeholder need to understand why?       |
| Speed              | Does the model need to predict in real-time?       |

### Summary

In this chapter, you have learned:
- The difference between regression and classification
- How to build Logistic Regression and Decision Tree classifiers
- How to evaluate models using accuracy
- How to compare multiple models on the same dataset
- Best practices for building reliable classification systems

These foundations apply to every ML project you will encounter, from school assignments to production systems.""",
                'exercise': None,
            },
        ],
    },
]
