CHAPTER_INFO = {
    'title': 'Scikit-learn for Machine Learning',
    'description': (
        'Learn the fundamentals of machine learning using scikit-learn, '
        "Python's most popular ML library. This chapter covers the full "
        'ML workflow: splitting data, scaling features, training models '
        '(linear regression, logistic regression, decision trees), and '
        'evaluating performance with metrics like accuracy, precision, '
        'recall, F1 score, MSE, and R-squared.'
    ),
    'difficulty_level': 'advanced',
    'order': 11,
    'learning_objectives': [
        'Split datasets into training and testing sets with train_test_split',
        'Scale features using StandardScaler for better model performance',
        'Fit and predict with LinearRegression and evaluate using R2 and MSE',
        'Perform binary classification with LogisticRegression',
        'Build and interpret DecisionTreeClassifier with feature importances',
        'Evaluate models using accuracy, precision, recall, and F1 score',
        'Compare multiple models using classification_report and confusion_matrix',
    ],
    'estimated_time_minutes': 75,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1 - Train-Test Split & Data Preparation
    # ------------------------------------------------------------------ #
    {
        'title': 'Train-Test Split & Data Preparation',
        'description': '''## Train-Test Split & Data Preparation

Learn the essential first step of any ML workflow: splitting your data
into training and testing sets, and scaling features for better model
performance.

### Requirements

1. **Create the dataset** using the NumPy arrays provided in the
   starter code.

2. **Split the data** using `train_test_split` with `test_size=0.3`
   and `random_state=42`.

3. **Print the shapes** of `X_train`, `X_test`, `y_train`, and
   `y_test` in the format: `"X_train shape: (rows, cols)"`.

4. **Scale the training features** using `StandardScaler`. Fit the
   scaler on `X_train` only, then transform `X_train`.

5. **Print the scaled statistics**: the mean and standard deviation
   of each feature in the scaled training data, rounded to 2 decimal
   places. Use `abs()` on mean values to avoid `-0.0`.

### Example

```python
# With 10 samples, 2 features, test_size=0.3:
X_train shape: (7, 2)
X_test shape: (3, 2)
y_train shape: (7,)
y_test shape: (3,)
Scaled mean: [0.0, 0.0]
Scaled std: [1.0, 1.0]
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            'import numpy as np\n'
            'from sklearn.model_selection import train_test_split\n'
            'from sklearn.preprocessing import StandardScaler\n'
            '\n'
            '\n'
            '# Dataset: 10 samples, 2 features\n'
            'X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10],\n'
            '              [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])\n'
            'y = np.array([0, 0, 0, 1, 1, 1, 0, 1, 1, 0])\n'
            '\n'
            '# TODO: Split the data using train_test_split\n'
            '# Use test_size=0.3 and random_state=42\n'
            '\n'
            '# TODO: Print the shapes of X_train, X_test, y_train, y_test\n'
            '# Format: "X_train shape: (rows, cols)"\n'
            '\n'
            '# TODO: Create a StandardScaler, fit on X_train, transform X_train\n'
            '\n'
            '# TODO: Print scaled mean and std (rounded to 2 decimal places)\n'
            '# Use abs() on each mean value to avoid -0.0:\n'
            '# mean_clean = [round(abs(float(v)), 2) for v in mean_vals]\n'
            '# Format: "Scaled mean: [val1, val2]"\n'
            '# Format: "Scaled std: [val1, val2]"\n'
        ),
        'hints': [
            'Use: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)',
            'Print shape with f-string: print(f"X_train shape: {X_train.shape}")',
            'Create scaler: scaler = StandardScaler(); X_train_scaled = scaler.fit_transform(X_train)',
            'For clean mean: [round(abs(float(v)), 2) for v in mean_vals] -- abs() prevents -0.0',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    'X_train shape: (7, 2)\n'
                    'X_test shape: (3, 2)\n'
                    'y_train shape: (7,)\n'
                    'y_test shape: (3,)\n'
                    'Scaled mean: [0.0, 0.0]\n'
                    'Scaled std: [1.0, 1.0]'
                ),
            },
            {
                'input': '',
                'expected_output': (
                    'X_train shape: (7, 2)\n'
                    'X_test shape: (3, 2)\n'
                    'y_train shape: (7,)\n'
                    'y_test shape: (3,)\n'
                    'Scaled mean: [0.0, 0.0]\n'
                    'Scaled std: [1.0, 1.0]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import numpy as np

class TestTrainTestSplit(unittest.TestCase):

    def setUp(self):
        import io, sys
        self.held_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = self.held_output
        env = {}
        exec(open("student_code.py").read(), env)
        sys.stdout = old_stdout
        self.env = env
        self.output = self.held_output.getvalue().strip()

    def test_output_contains_shapes(self):
        self.assertIn("X_train shape: (7, 2)", self.output)
        self.assertIn("X_test shape: (3, 2)", self.output)
        self.assertIn("y_train shape: (7,)", self.output)
        self.assertIn("y_test shape: (3,)", self.output)

    def test_output_contains_scaled_mean(self):
        self.assertIn("Scaled mean: [0.0, 0.0]", self.output)

    def test_output_contains_scaled_std(self):
        self.assertIn("Scaled std: [1.0, 1.0]", self.output)

    def test_split_uses_correct_random_state(self):
        from sklearn.model_selection import train_test_split
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
                      [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
        y = np.array([0, 0, 0, 1, 1, 1, 0, 1, 1, 0])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)
        self.assertEqual(X_train.shape, (7, 2))
        self.assertEqual(X_test.shape, (3, 2))

    def test_scaler_fit_on_train_only(self):
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
                      [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
        y = np.array([0, 0, 0, 1, 1, 1, 0, 1, 1, 0])
        X_train, X_test, _, _ = train_test_split(
            X, y, test_size=0.3, random_state=42)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_train)
        mean_vals = X_scaled.mean(axis=0)
        for v in mean_vals:
            self.assertAlmostEqual(abs(float(v)), 0.0, places=2)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2 - Linear Regression
    # ------------------------------------------------------------------ #
    {
        'title': 'Linear Regression',
        'description': '''## Linear Regression

Fit a simple linear regression model to predict a continuous target
variable and evaluate its performance.

### Requirements

1. **Create the dataset** from the arrays in the starter code:
   `X` contains single-feature values, `y` contains target values.

2. **Fit a `LinearRegression`** model on the data.

3. **Print the model parameters**:
   - `Coefficient: <value>` (rounded to 4 decimal places)
   - `Intercept: <value>` (rounded to 4 decimal places)

4. **Evaluate the model**:
   - Print `R2 Score: <value>` (rounded to 4 decimal places)

5. **Make a prediction**:
   - Predict the value for `x=11`
   - Print `Prediction for x=11: <value>` (rounded to 4 decimal places)

### Example

```python
# With the provided dataset:
Coefficient: 2.0
Intercept: 0.04
R2 Score: 0.9996
Prediction for x=11: 22.04
```
''',
        'difficulty': 'easy',
        'order': 2,
        'item_order': 4,
        'starter_code': (
            'import numpy as np\n'
            'from sklearn.linear_model import LinearRegression\n'
            '\n'
            '\n'
            '# Dataset: 10 x,y pairs with a roughly linear relationship\n'
            'X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])\n'
            'y = np.array([2.1, 4.0, 6.2, 7.9, 10.1, 12.0, 13.8, 16.1, 18.0, 20.2])\n'
            '\n'
            '# TODO: Create and fit a LinearRegression model\n'
            '\n'
            '# TODO: Print coefficient (rounded to 4 decimal places)\n'
            '# Format: "Coefficient: <value>"\n'
            '\n'
            '# TODO: Print intercept (rounded to 4 decimal places)\n'
            '# Format: "Intercept: <value>"\n'
            '\n'
            '# TODO: Calculate and print R2 score (rounded to 4 decimal places)\n'
            '# Format: "R2 Score: <value>"\n'
            '\n'
            '# TODO: Predict for x=11 and print (rounded to 4 decimal places)\n'
            '# Format: "Prediction for x=11: <value>"\n'
        ),
        'hints': [
            'Create and fit: model = LinearRegression(); model.fit(X, y)',
            'Coefficient is model.coef_[0], intercept is model.intercept_',
            'R2 score: model.score(X, y)',
            'Predict: model.predict(np.array([[11]]))[0]',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    'Coefficient: 2.0\n'
                    'Intercept: 0.04\n'
                    'R2 Score: 0.9996\n'
                    'Prediction for x=11: 22.04'
                ),
            },
            {
                'input': '',
                'expected_output': (
                    'Coefficient: 2.0\n'
                    'Intercept: 0.04\n'
                    'R2 Score: 0.9996\n'
                    'Prediction for x=11: 22.04'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import numpy as np

class TestLinearRegression(unittest.TestCase):

    def setUp(self):
        import io, sys
        self.held_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = self.held_output
        env = {}
        exec(open("student_code.py").read(), env)
        sys.stdout = old_stdout
        self.env = env
        self.output = self.held_output.getvalue().strip()

    def test_coefficient(self):
        self.assertIn("Coefficient: 2.0", self.output)

    def test_intercept(self):
        self.assertIn("Intercept: 0.04", self.output)

    def test_r2_score(self):
        self.assertIn("R2 Score: 0.9996", self.output)

    def test_prediction(self):
        self.assertIn("Prediction for x=11: 22.04", self.output)

    def test_model_accuracy(self):
        from sklearn.linear_model import LinearRegression
        X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
        y = np.array([2.1, 4.0, 6.2, 7.9, 10.1, 12.0, 13.8, 16.1, 18.0, 20.2])
        model = LinearRegression()
        model.fit(X, y)
        self.assertAlmostEqual(round(model.coef_[0], 4), 2.0, places=2)
        self.assertAlmostEqual(round(model.intercept_, 4), 0.04, places=2)
        pred = model.predict(np.array([[11]]))[0]
        self.assertAlmostEqual(round(pred, 4), 22.04, places=2)

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3 - Classification with Logistic Regression
    # ------------------------------------------------------------------ #
    {
        'title': 'Classification with Logistic Regression',
        'description': '''## Classification with Logistic Regression

Perform binary classification using Logistic Regression. Learn to
split data, train a classifier, and evaluate with accuracy.

### Requirements

1. **Create the dataset** from the arrays in the starter code:
   20 samples with 2 features, binary labels (0 or 1).

2. **Split the data** using `train_test_split` with `test_size=0.3`
   and `random_state=42`.

3. **Train a `LogisticRegression`** model with `random_state=42`
   and `max_iter=1000`.

4. **Evaluate and print**:
   - `Accuracy: <value>` (rounded to 4 decimal places)
   - `Predictions: <list>` (as a Python list of ints)
   - `Actual: <list>` (as a Python list of ints)

### Example

```python
# Output with the provided dataset:
Accuracy: 1.0
Predictions: [0, 1, 1, 0, 1, 1]
Actual: [0, 1, 1, 0, 1, 1]
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            'import numpy as np\n'
            'from sklearn.linear_model import LogisticRegression\n'
            'from sklearn.model_selection import train_test_split\n'
            '\n'
            '\n'
            '# Dataset: 20 samples, 2 features, binary classification\n'
            'X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6],\n'
            '              [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],\n'
            '              [2, 1], [3, 2], [4, 3], [7, 6], [8, 7],\n'
            '              [9, 8], [10, 9], [11, 10], [5, 4], [6, 5]])\n'
            'y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1,\n'
            '              0, 0, 0, 1, 1, 1, 1, 1, 0, 1])\n'
            '\n'
            '# TODO: Split data with test_size=0.3, random_state=42\n'
            '\n'
            '# TODO: Create LogisticRegression with random_state=42, max_iter=1000\n'
            '# Fit on training data\n'
            '\n'
            '# TODO: Calculate accuracy on test set (rounded to 4 decimal places)\n'
            '# Print: "Accuracy: <value>"\n'
            '\n'
            '# TODO: Get predictions on test set\n'
            '# Print: "Predictions: <list>" (as Python list of ints)\n'
            '\n'
            '# TODO: Print actual test labels\n'
            '# Print: "Actual: <list>" (as Python list of ints)\n'
        ),
        'hints': [
            'Split: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)',
            'Model: model = LogisticRegression(random_state=42, max_iter=1000); model.fit(X_train, y_train)',
            'Accuracy: round(float(model.score(X_test, y_test)), 4)',
            'Predictions: model.predict(X_test).tolist()',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    'Accuracy: 1.0\n'
                    'Predictions: [0, 1, 1, 0, 1, 1]\n'
                    'Actual: [0, 1, 1, 0, 1, 1]'
                ),
            },
            {
                'input': '',
                'expected_output': (
                    'Accuracy: 1.0\n'
                    'Predictions: [0, 1, 1, 0, 1, 1]\n'
                    'Actual: [0, 1, 1, 0, 1, 1]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import numpy as np

class TestLogisticRegression(unittest.TestCase):

    def setUp(self):
        import io, sys
        self.held_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = self.held_output
        env = {}
        exec(open("student_code.py").read(), env)
        sys.stdout = old_stdout
        self.env = env
        self.output = self.held_output.getvalue().strip()

    def test_accuracy_present(self):
        self.assertIn("Accuracy: 1.0", self.output)

    def test_predictions_present(self):
        self.assertIn("Predictions: [0, 1, 1, 0, 1, 1]", self.output)

    def test_actual_present(self):
        self.assertIn("Actual: [0, 1, 1, 0, 1, 1]", self.output)

    def test_model_with_fresh_data(self):
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
                      [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],
                      [2, 1], [3, 2], [4, 3], [7, 6], [8, 7],
                      [9, 8], [10, 9], [11, 10], [5, 4], [6, 5]])
        y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                      0, 0, 0, 1, 1, 1, 1, 1, 0, 1])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)
        model = LogisticRegression(random_state=42, max_iter=1000)
        model.fit(X_train, y_train)
        acc = round(float(model.score(X_test, y_test)), 4)
        self.assertEqual(acc, 1.0)

    def test_uses_random_state(self):
        lines = self.output.split("\\n")
        self.assertTrue(len(lines) >= 3,
                        "Output should have at least 3 lines")

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4 - Decision Tree Classifier
    # ------------------------------------------------------------------ #
    {
        'title': 'Decision Tree Classifier',
        'description': '''## Decision Tree Classifier

Build a Decision Tree classifier, examine feature importances, and
make predictions on test data.

### Requirements

1. **Create the dataset** from the arrays in the starter code:
   20 samples with 3 features, binary labels.

2. **Split the data** using `train_test_split` with `test_size=0.3`
   and `random_state=42`.

3. **Train a `DecisionTreeClassifier`** with `random_state=42`.

4. **Evaluate and print**:
   - `Accuracy: <value>` (rounded to 4 decimal places, cast to float)
   - `Feature Importances: <list>` (each value rounded to 4 decimal
     places, cast to float)
   - `Predictions: <list>` (as a Python list of ints)
   - `Actual: <list>` (as a Python list of ints)

### Example

```python
# Output with the provided dataset:
Accuracy: 1.0
Feature Importances: [1.0, 0.0, 0.0]
Predictions: [0, 1, 0, 0, 1, 1]
Actual: [0, 1, 0, 0, 1, 1]
```
''',
        'difficulty': 'medium',
        'order': 4,
        'item_order': 7,
        'starter_code': (
            'import numpy as np\n'
            'from sklearn.tree import DecisionTreeClassifier\n'
            'from sklearn.model_selection import train_test_split\n'
            '\n'
            '\n'
            '# Dataset: 20 samples, 3 features, binary classification\n'
            'X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7],\n'
            '              [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12],\n'
            '              [2, 1, 3], [3, 2, 4], [7, 6, 8], [8, 7, 9], [9, 8, 10],\n'
            '              [1, 3, 2], [4, 6, 5], [6, 8, 7], [10, 12, 11], [5, 7, 6]])\n'
            'y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1,\n'
            '              0, 0, 1, 1, 1, 0, 0, 1, 1, 1])\n'
            '\n'
            '# TODO: Split data with test_size=0.3, random_state=42\n'
            '\n'
            '# TODO: Create DecisionTreeClassifier with random_state=42\n'
            '# Fit on training data\n'
            '\n'
            '# TODO: Calculate and print accuracy (rounded to 4 decimal places)\n'
            '# Use float() to convert: round(float(model.score(...)), 4)\n'
            '# Print: "Accuracy: <value>"\n'
            '\n'
            '# TODO: Get and print feature importances\n'
            '# Convert each to float and round to 4 places\n'
            '# Print: "Feature Importances: <list>"\n'
            '\n'
            '# TODO: Get predictions and print\n'
            '# Print: "Predictions: <list>" (as Python list of ints)\n'
            '\n'
            '# TODO: Print actual test labels\n'
            '# Print: "Actual: <list>" (as Python list of ints)\n'
        ),
        'hints': [
            'Split: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)',
            'Model: model = DecisionTreeClassifier(random_state=42); model.fit(X_train, y_train)',
            'Feature importances: [round(float(x), 4) for x in model.feature_importances_]',
            'Convert predictions to list: model.predict(X_test).tolist()',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    'Accuracy: 1.0\n'
                    'Feature Importances: [1.0, 0.0, 0.0]\n'
                    'Predictions: [0, 1, 0, 0, 1, 1]\n'
                    'Actual: [0, 1, 0, 0, 1, 1]'
                ),
            },
            {
                'input': '',
                'expected_output': (
                    'Accuracy: 1.0\n'
                    'Feature Importances: [1.0, 0.0, 0.0]\n'
                    'Predictions: [0, 1, 0, 0, 1, 1]\n'
                    'Actual: [0, 1, 0, 0, 1, 1]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import numpy as np

class TestDecisionTree(unittest.TestCase):

    def setUp(self):
        import io, sys
        self.held_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = self.held_output
        env = {}
        exec(open("student_code.py").read(), env)
        sys.stdout = old_stdout
        self.env = env
        self.output = self.held_output.getvalue().strip()

    def test_accuracy_present(self):
        self.assertIn("Accuracy: 1.0", self.output)

    def test_feature_importances_present(self):
        self.assertIn("Feature Importances: [1.0, 0.0, 0.0]", self.output)

    def test_predictions_present(self):
        self.assertIn("Predictions: [0, 1, 0, 0, 1, 1]", self.output)

    def test_actual_present(self):
        self.assertIn("Actual: [0, 1, 0, 0, 1, 1]", self.output)

    def test_model_reproducibility(self):
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7],
                      [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12],
                      [2, 1, 3], [3, 2, 4], [7, 6, 8], [8, 7, 9], [9, 8, 10],
                      [1, 3, 2], [4, 6, 5], [6, 8, 7], [10, 12, 11], [5, 7, 6]])
        y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                      0, 0, 1, 1, 1, 0, 0, 1, 1, 1])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)
        acc = round(float(model.score(X_test, y_test)), 4)
        self.assertEqual(acc, 1.0)
        preds = model.predict(X_test).tolist()
        self.assertEqual(preds, [0, 1, 0, 0, 1, 1])

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 5 - Model Evaluation & Comparison
    # ------------------------------------------------------------------ #
    {
        'title': 'Model Evaluation & Comparison',
        'description': '''## Model Evaluation & Comparison

Train multiple classification models, evaluate each using standard
metrics, and compare their performance side by side.

### Requirements

1. **Create the dataset** from the arrays in the starter code:
   20 samples with 2 features and noisy binary labels.

2. **Split the data** using `train_test_split` with `test_size=0.3`
   and `random_state=42`.

3. **Train two models**:
   - `LogisticRegression(random_state=42, max_iter=1000)`
   - `DecisionTreeClassifier(random_state=42)`

4. **For each model, compute** (all rounded to 4 decimal places,
   cast to float):
   - Accuracy (using `accuracy_score`)
   - Precision (using `precision_score`)
   - Recall (using `recall_score`)
   - F1 Score (using `f1_score`)

5. **Print the comparison** in this exact format:
```
Model Comparison:
Logistic Regression - Accuracy: <v>, Precision: <v>, Recall: <v>, F1: <v>
Decision Tree       - Accuracy: <v>, Precision: <v>, Recall: <v>, F1: <v>
```

6. **Print confusion matrices** for each model:
```
Confusion Matrix (Logistic Regression):
<matrix as nested list>
Confusion Matrix (Decision Tree):
<matrix as nested list>
```

### Example

```python
Model Comparison:
Logistic Regression - Accuracy: 0.8333, Precision: 1.0, Recall: 0.6667, F1: 0.8
Decision Tree       - Accuracy: 0.6667, Precision: 1.0, Recall: 0.3333, F1: 0.5
Confusion Matrix (Logistic Regression):
[[3, 0], [1, 2]]
Confusion Matrix (Decision Tree):
[[3, 0], [2, 1]]
```
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 8,
        'starter_code': (
            'import numpy as np\n'
            'from sklearn.linear_model import LogisticRegression\n'
            'from sklearn.tree import DecisionTreeClassifier\n'
            'from sklearn.model_selection import train_test_split\n'
            'from sklearn.metrics import (accuracy_score, precision_score,\n'
            '                             recall_score, f1_score, confusion_matrix)\n'
            '\n'
            '\n'
            '# Dataset: 20 samples, 2 features, noisy binary labels\n'
            'X = np.array([[1, 2], [2, 1], [3, 5], [4, 3], [5, 7],\n'
            '              [6, 4], [7, 8], [8, 6], [9, 9], [10, 5],\n'
            '              [1, 5], [3, 1], [5, 3], [7, 2], [8, 8],\n'
            '              [2, 4], [4, 6], [6, 1], [9, 3], [10, 10]])\n'
            'y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1,\n'
            '              0, 0, 0, 1, 1, 0, 0, 1, 1, 1])\n'
            '\n'
            '# TODO: Split data with test_size=0.3, random_state=42\n'
            '\n'
            '# TODO: Train LogisticRegression (random_state=42, max_iter=1000)\n'
            '\n'
            '# TODO: Train DecisionTreeClassifier (random_state=42)\n'
            '\n'
            '# TODO: For each model, compute accuracy, precision, recall, f1\n'
            '# Round all to 4 decimal places, use float() to convert\n'
            '\n'
            '# TODO: Print model comparison in the required format\n'
            '# "Model Comparison:"\n'
            '# "Logistic Regression - Accuracy: <v>, Precision: <v>, Recall: <v>, F1: <v>"\n'
            '# "Decision Tree       - Accuracy: <v>, Precision: <v>, Recall: <v>, F1: <v>"\n'
            '\n'
            '# TODO: Print confusion matrices\n'
            '# "Confusion Matrix (Logistic Regression):"\n'
            '# <matrix.tolist()>\n'
            '# "Confusion Matrix (Decision Tree):"\n'
            '# <matrix.tolist()>\n'
        ),
        'hints': [
            'Use accuracy_score(y_test, preds), precision_score(y_test, preds), etc.',
            'Round each metric: round(float(accuracy_score(y_test, lr_preds)), 4)',
            'Confusion matrix: confusion_matrix(y_test, preds).tolist() for clean output',
            'Make sure spacing in "Decision Tree       -" uses 7 spaces after "Tree" to align with "Logistic Regression -"',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': (
                    'Model Comparison:\n'
                    'Logistic Regression - Accuracy: 0.8333, Precision: 1.0, Recall: 0.6667, F1: 0.8\n'
                    'Decision Tree       - Accuracy: 0.6667, Precision: 1.0, Recall: 0.3333, F1: 0.5\n'
                    'Confusion Matrix (Logistic Regression):\n'
                    '[[3, 0], [1, 2]]\n'
                    'Confusion Matrix (Decision Tree):\n'
                    '[[3, 0], [2, 1]]'
                ),
            },
            {
                'input': '',
                'expected_output': (
                    'Model Comparison:\n'
                    'Logistic Regression - Accuracy: 0.8333, Precision: 1.0, Recall: 0.6667, F1: 0.8\n'
                    'Decision Tree       - Accuracy: 0.6667, Precision: 1.0, Recall: 0.3333, F1: 0.5\n'
                    'Confusion Matrix (Logistic Regression):\n'
                    '[[3, 0], [1, 2]]\n'
                    'Confusion Matrix (Decision Tree):\n'
                    '[[3, 0], [2, 1]]'
                ),
            },
        ],
        'test_cases_code': '''
import unittest
import numpy as np

class TestModelComparison(unittest.TestCase):

    def setUp(self):
        import io, sys
        self.held_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = self.held_output
        env = {}
        exec(open("student_code.py").read(), env)
        sys.stdout = old_stdout
        self.env = env
        self.output = self.held_output.getvalue().strip()

    def test_header_present(self):
        self.assertIn("Model Comparison:", self.output)

    def test_logistic_regression_metrics(self):
        self.assertIn(
            "Logistic Regression - Accuracy: 0.8333, Precision: 1.0, "
            "Recall: 0.6667, F1: 0.8",
            self.output)

    def test_decision_tree_metrics(self):
        self.assertIn(
            "Decision Tree       - Accuracy: 0.6667, Precision: 1.0, "
            "Recall: 0.3333, F1: 0.5",
            self.output)

    def test_confusion_matrix_lr(self):
        self.assertIn("Confusion Matrix (Logistic Regression):", self.output)
        self.assertIn("[[3, 0], [1, 2]]", self.output)

    def test_confusion_matrix_dt(self):
        self.assertIn("Confusion Matrix (Decision Tree):", self.output)
        self.assertIn("[[3, 0], [2, 1]]", self.output)

    def test_reproducibility(self):
        from sklearn.linear_model import LogisticRegression
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score
        X = np.array([[1, 2], [2, 1], [3, 5], [4, 3], [5, 7],
                      [6, 4], [7, 8], [8, 6], [9, 9], [10, 5],
                      [1, 5], [3, 1], [5, 3], [7, 2], [8, 8],
                      [2, 4], [4, 6], [6, 1], [9, 3], [10, 10]])
        y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                      0, 0, 0, 1, 1, 0, 0, 1, 1, 1])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)
        lr = LogisticRegression(random_state=42, max_iter=1000)
        lr.fit(X_train, y_train)
        lr_acc = round(float(accuracy_score(y_test, lr.predict(X_test))), 4)
        self.assertAlmostEqual(lr_acc, 0.8333, places=4)
        dt = DecisionTreeClassifier(random_state=42)
        dt.fit(X_train, y_train)
        dt_acc = round(float(accuracy_score(y_test, dt.predict(X_test))), 4)
        self.assertAlmostEqual(dt_acc, 0.6667, places=4)

if __name__ == "__main__":
    unittest.main()
''',
    },
]
