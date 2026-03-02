CHAPTER_INFO = {
    'title': 'Object-Oriented Programming',
    'description': (
        'Learn the fundamentals of Object-Oriented Programming (OOP) in Python. '
        'This chapter covers classes, objects, inheritance, polymorphism, '
        'encapsulation, and special methods that let you write clean, '
        'reusable, and well-structured code.'
    ),
    'difficulty_level': 'advanced',
    'order': 7,
    'learning_objectives': [
        'Define classes and create objects using __init__',
        'Write instance methods and use self',
        'Implement inheritance and method overriding',
        'Apply polymorphism to write flexible code',
        'Use encapsulation and @property decorators',
        'Implement __str__ and __repr__ special methods',
        'Create class methods and static methods',
    ],
    'estimated_time_minutes': 70,
}

ASSIGNMENTS = [
    # ------------------------------------------------------------------ #
    # Assignment 1 – Basic Class Creation
    # ------------------------------------------------------------------ #
    {
        'title': 'Basic Class Creation',
        'description': '''## Basic Class Creation

In this assignment you will create your first Python class from scratch.

### Requirements

1. Define a class called **`Student`** with the following attributes set in `__init__`:
   - `name` (str) – the student's full name
   - `age` (int) – the student's age
   - `grade` (str) – the student's letter grade (e.g. `"A"`, `"B+"`)

2. Implement the **`__str__`** method so that printing a `Student` produces:
   ```
   Student: <name>, Age: <age>, Grade: <grade>
   ```

3. Implement a method **`is_passing`** that returns `True` if the grade does
   **not** start with `"F"`, and `False` otherwise.

### Example

```python
s = Student("Alice", 20, "A")
print(s)           # Student: Alice, Age: 20, Grade: A
print(s.is_passing())  # True
```
''',
        'difficulty': 'easy',
        'order': 1,
        'item_order': 2,
        'starter_code': (
            'class Student:\n'
            '    """A class representing a student."""\n'
            '\n'
            '    def __init__(self, name, age, grade):\n'
            '        # TODO: store attributes\n'
            '        pass\n'
            '\n'
            '    def __str__(self):\n'
            '        # TODO: return formatted string\n'
            '        pass\n'
            '\n'
            '    def is_passing(self):\n'
            '        # TODO: return True if grade does not start with "F"\n'
            '        pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            's = Student("Alice", 20, "A")\n'
            'print(s)\n'
            'print(s.is_passing())\n'
        ),
        'hints': [
            'Use self.name, self.age, self.grade inside __init__ to store the values.',
            'In __str__, use an f-string: f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"',
            'For is_passing, check self.grade.startswith("F") and negate it.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': 'Student: Alice, Age: 20, Grade: A\nTrue',
            },
        ],
        'test_cases_code': '''
import unittest

class TestStudentClass(unittest.TestCase):

    def setUp(self):
        exec(open("student_code.py").read(), globals())
        self.Student = globals()["Student"]

    def test_attributes(self):
        s = self.Student("Bob", 18, "B+")
        self.assertEqual(s.name, "Bob")
        self.assertEqual(s.age, 18)
        self.assertEqual(s.grade, "B+")

    def test_str(self):
        s = self.Student("Alice", 20, "A")
        self.assertEqual(str(s), "Student: Alice, Age: 20, Grade: A")

    def test_is_passing_true(self):
        s = self.Student("Carol", 22, "C")
        self.assertTrue(s.is_passing())

    def test_is_passing_false(self):
        s = self.Student("Dave", 19, "F")
        self.assertFalse(s.is_passing())

    def test_str_different_values(self):
        s = self.Student("Eve", 25, "B-")
        self.assertEqual(str(s), "Student: Eve, Age: 25, Grade: B-")

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 2 – Bank Account Class
    # ------------------------------------------------------------------ #
    {
        'title': 'Bank Account Class',
        'description': '''## Bank Account Class

Build a `BankAccount` class that models a simple bank account with
deposit, withdrawal, and balance-inquiry features.

### Requirements

1. **`__init__(self, owner, balance=0)`** – set `owner` (str) and
   `balance` (float, default `0`).

2. **`deposit(self, amount)`** – add `amount` to `balance`.
   - If `amount <= 0`, print `"Deposit amount must be positive"` and
     do **not** change the balance.

3. **`withdraw(self, amount)`** – subtract `amount` from `balance`.
   - If `amount <= 0`, print `"Withdrawal amount must be positive"`.
   - If `amount > balance`, print `"Insufficient funds"`.
   - In either error case do **not** change the balance.

4. **`get_balance(self)`** – return the current balance.

5. **`__str__(self)`** – return
   `"Account owner: <owner>, Balance: $<balance>"` where balance is
   formatted to **two decimal places**.

### Example

```python
acc = BankAccount("Alice", 100)
acc.deposit(50)
print(acc.get_balance())  # 150
acc.withdraw(30)
print(acc)                # Account owner: Alice, Balance: $120.00
```
''',
        'difficulty': 'medium',
        'order': 2,
        'item_order': 3,
        'starter_code': (
            'class BankAccount:\n'
            '    """A simple bank account with overdraft protection."""\n'
            '\n'
            '    def __init__(self, owner, balance=0):\n'
            '        # TODO: initialize owner and balance\n'
            '        pass\n'
            '\n'
            '    def deposit(self, amount):\n'
            '        # TODO: add amount if positive\n'
            '        pass\n'
            '\n'
            '    def withdraw(self, amount):\n'
            '        # TODO: subtract amount with overdraft protection\n'
            '        pass\n'
            '\n'
            '    def get_balance(self):\n'
            '        # TODO: return current balance\n'
            '        pass\n'
            '\n'
            '    def __str__(self):\n'
            '        # TODO: formatted string\n'
            '        pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'acc = BankAccount("Alice", 100)\n'
            'acc.deposit(50)\n'
            'print(acc.get_balance())\n'
            'acc.withdraw(30)\n'
            'print(acc)\n'
        ),
        'hints': [
            'Store owner and balance in __init__ using self.',
            'In deposit, check `if amount <= 0` before adding.',
            'In withdraw, first check positivity, then check if amount > self.balance.',
            'Use f"Account owner: {self.owner}, Balance: ${self.balance:.2f}" for __str__.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': '150\nAccount owner: Alice, Balance: $120.00',
            },
        ],
        'test_cases_code': '''
import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        exec(open("student_code.py").read(), globals())
        self.BankAccount = globals()["BankAccount"]

    def test_initial_balance(self):
        acc = self.BankAccount("Test", 200)
        self.assertEqual(acc.get_balance(), 200)

    def test_default_balance(self):
        acc = self.BankAccount("Test")
        self.assertEqual(acc.get_balance(), 0)

    def test_deposit(self):
        acc = self.BankAccount("Test", 100)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)

    def test_withdraw(self):
        acc = self.BankAccount("Test", 100)
        acc.withdraw(40)
        self.assertEqual(acc.get_balance(), 60)

    def test_overdraft_protection(self):
        acc = self.BankAccount("Test", 50)
        acc.withdraw(100)
        self.assertEqual(acc.get_balance(), 50)

    def test_negative_deposit(self):
        acc = self.BankAccount("Test", 100)
        acc.deposit(-10)
        self.assertEqual(acc.get_balance(), 100)

    def test_str(self):
        acc = self.BankAccount("Alice", 120)
        self.assertEqual(str(acc), "Account owner: Alice, Balance: $120.00")

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 3 – Inheritance & Polymorphism
    # ------------------------------------------------------------------ #
    {
        'title': 'Inheritance & Polymorphism',
        'description': '''## Inheritance & Polymorphism

Practice inheritance and polymorphism by building a small shape
hierarchy.

### Requirements

1. **`Shape`** (base class)
   - `__init__(self, name)` – stores the shape name.
   - `area(self)` – returns `0` (to be overridden).
   - `perimeter(self)` – returns `0` (to be overridden).
   - `__str__(self)` – returns `"<name>: area=<area>, perimeter=<perimeter>"`
     with area and perimeter rounded to **two decimal places**.

2. **`Circle(Shape)`**
   - `__init__(self, radius)` – set name to `"Circle"` and store `radius`.
   - Override `area` → `pi * r^2` and `perimeter` → `2 * pi * r`.
   - Use `math.pi`.

3. **`Rectangle(Shape)`**
   - `__init__(self, width, height)` – set name to `"Rectangle"` and
     store `width` and `height`.
   - Override `area` → `width * height` and `perimeter` → `2*(width+height)`.

### Example

```python
c = Circle(5)
r = Rectangle(4, 6)
print(c)  # Circle: area=78.54, perimeter=31.42
print(r)  # Rectangle: area=24.00, perimeter=20.00
```
''',
        'difficulty': 'medium',
        'order': 3,
        'item_order': 5,
        'starter_code': (
            'import math\n'
            '\n'
            '\n'
            'class Shape:\n'
            '    """Base class for shapes."""\n'
            '\n'
            '    def __init__(self, name):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def area(self):\n'
            '        return 0\n'
            '\n'
            '    def perimeter(self):\n'
            '        return 0\n'
            '\n'
            '    def __str__(self):\n'
            '        # TODO: return formatted string\n'
            '        pass\n'
            '\n'
            '\n'
            'class Circle(Shape):\n'
            '    """A circle shape."""\n'
            '\n'
            '    def __init__(self, radius):\n'
            '        # TODO: call super().__init__ and store radius\n'
            '        pass\n'
            '\n'
            '    def area(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def perimeter(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '\n'
            'class Rectangle(Shape):\n'
            '    """A rectangle shape."""\n'
            '\n'
            '    def __init__(self, width, height):\n'
            '        # TODO: call super().__init__ and store dimensions\n'
            '        pass\n'
            '\n'
            '    def area(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def perimeter(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'c = Circle(5)\n'
            'r = Rectangle(4, 6)\n'
            'print(c)\n'
            'print(r)\n'
        ),
        'hints': [
            'Call super().__init__("Circle") inside Circle.__init__.',
            'Area of a circle: math.pi * self.radius ** 2',
            'In Shape.__str__, use f"{self.name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"',
            'Make sure Rectangle stores both width and height as attributes.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': 'Circle: area=78.54, perimeter=31.42\nRectangle: area=24.00, perimeter=20.00',
            },
        ],
        'test_cases_code': '''
import unittest
import math

class TestShapes(unittest.TestCase):

    def setUp(self):
        exec(open("student_code.py").read(), globals())
        self.Shape = globals()["Shape"]
        self.Circle = globals()["Circle"]
        self.Rectangle = globals()["Rectangle"]

    def test_circle_area(self):
        c = self.Circle(5)
        self.assertAlmostEqual(c.area(), math.pi * 25, places=2)

    def test_circle_perimeter(self):
        c = self.Circle(5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 5, places=2)

    def test_rectangle_area(self):
        r = self.Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

    def test_rectangle_perimeter(self):
        r = self.Rectangle(4, 6)
        self.assertEqual(r.perimeter(), 20)

    def test_circle_inheritance(self):
        c = self.Circle(1)
        self.assertIsInstance(c, self.Shape)

    def test_str_circle(self):
        c = self.Circle(5)
        self.assertEqual(str(c), "Circle: area=78.54, perimeter=31.42")

    def test_str_rectangle(self):
        r = self.Rectangle(4, 6)
        self.assertEqual(str(r), "Rectangle: area=24.00, perimeter=20.00")

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 4 – Class Properties & Encapsulation
    # ------------------------------------------------------------------ #
    {
        'title': 'Class Properties & Encapsulation',
        'description': '''## Class Properties & Encapsulation

Learn to use Python's `@property` decorator and encapsulation
conventions by building a `Temperature` class.

### Requirements

1. **`Temperature`** class:
   - `__init__(self, celsius=0)` – store the temperature internally
     in Celsius using a **private** attribute `_celsius`.
   - **`celsius`** property (getter + setter):
     - Getter returns `_celsius`.
     - Setter validates: if the new value is below **-273.15**
       (absolute zero), raise a `ValueError` with the message
       `"Temperature below absolute zero is not possible"`.
   - **`fahrenheit`** property (getter + setter):
     - Getter returns the Fahrenheit equivalent: `celsius * 9/5 + 32`.
     - Setter converts the given Fahrenheit value to Celsius and
       stores it (also validate against absolute zero).
   - **`__str__`** – returns
     `"<celsius>°C / <fahrenheit>°F"` with both values rounded to
     **two decimal places**.

### Example

```python
t = Temperature(100)
print(t)              # 100.00°C / 212.00°F
t.fahrenheit = 32
print(t.celsius)      # 0.0
print(t)              # 0.00°C / 32.00°F
```
''',
        'difficulty': 'hard',
        'order': 4,
        'item_order': 7,
        'starter_code': (
            'class Temperature:\n'
            '    """Temperature with Celsius/Fahrenheit conversion using @property."""\n'
            '\n'
            '    def __init__(self, celsius=0):\n'
            '        # TODO: store celsius using the property setter for validation\n'
            '        pass\n'
            '\n'
            '    @property\n'
            '    def celsius(self):\n'
            '        # TODO: return _celsius\n'
            '        pass\n'
            '\n'
            '    @celsius.setter\n'
            '    def celsius(self, value):\n'
            '        # TODO: validate and set _celsius\n'
            '        pass\n'
            '\n'
            '    @property\n'
            '    def fahrenheit(self):\n'
            '        # TODO: convert and return\n'
            '        pass\n'
            '\n'
            '    @fahrenheit.setter\n'
            '    def fahrenheit(self, value):\n'
            '        # TODO: convert to celsius and store\n'
            '        pass\n'
            '\n'
            '    def __str__(self):\n'
            '        # TODO: formatted string\n'
            '        pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            't = Temperature(100)\n'
            'print(t)\n'
            't.fahrenheit = 32\n'
            'print(t.celsius)\n'
            'print(t)\n'
        ),
        'hints': [
            'In __init__, use self.celsius = celsius to trigger the property setter.',
            'Fahrenheit to Celsius: (fahrenheit - 32) * 5 / 9',
            'Absolute zero in Celsius is -273.15. Raise ValueError if value < -273.15.',
            'Use f"{self.celsius:.2f}°C / {self.fahrenheit:.2f}°F" in __str__.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': '100.00°C / 212.00°F\n0.0\n0.00°C / 32.00°F',
            },
        ],
        'test_cases_code': '''
import unittest

class TestTemperature(unittest.TestCase):

    def setUp(self):
        exec(open("student_code.py").read(), globals())
        self.Temperature = globals()["Temperature"]

    def test_initial_celsius(self):
        t = self.Temperature(100)
        self.assertEqual(t.celsius, 100)

    def test_fahrenheit_getter(self):
        t = self.Temperature(100)
        self.assertAlmostEqual(t.fahrenheit, 212.0, places=2)

    def test_fahrenheit_setter(self):
        t = self.Temperature()
        t.fahrenheit = 32
        self.assertAlmostEqual(t.celsius, 0.0, places=2)

    def test_absolute_zero_validation(self):
        with self.assertRaises(ValueError):
            self.Temperature(-300)

    def test_str(self):
        t = self.Temperature(0)
        self.assertEqual(str(t), "0.00°C / 32.00°F")

    def test_fahrenheit_setter_validation(self):
        t = self.Temperature()
        with self.assertRaises(ValueError):
            t.fahrenheit = -500

if __name__ == "__main__":
    unittest.main()
''',
    },

    # ------------------------------------------------------------------ #
    # Assignment 5 – Class Hierarchy
    # ------------------------------------------------------------------ #
    {
        'title': 'Class Hierarchy',
        'description': '''## Class Hierarchy – Vehicles

Design a vehicle class hierarchy that demonstrates inheritance,
method overriding, and real-world modelling.

### Requirements

1. **`Vehicle`** (base class)
   - `__init__(self, make, model, year, fuel_capacity, fuel_level=0)`
   - `refuel(self, amount)` – add fuel up to `fuel_capacity`; print
     `"Tank is full"` if you try to overfill.
   - `fuel_efficiency(self)` – return `0` (override in subclasses).
   - `range(self)` – return `fuel_level * fuel_efficiency()` (how far
     the vehicle can go on current fuel).
   - `__str__(self)` – `"<year> <make> <model>"`.

2. **`Car(Vehicle)`**
   - `__init__(self, make, model, year, fuel_capacity, fuel_level=0, mpg=30)`
   - `fuel_efficiency` returns `mpg`.

3. **`Truck(Vehicle)`**
   - `__init__(self, make, model, year, fuel_capacity, fuel_level=0, mpg=18, cargo_weight=0)`
   - `fuel_efficiency` returns `mpg - (cargo_weight / 500)` (heavier
     cargo reduces efficiency) but **never less than 5**.

4. **`Motorcycle(Vehicle)`**
   - `__init__(self, make, model, year, fuel_capacity, fuel_level=0, mpg=50)`
   - `fuel_efficiency` returns `mpg`.

### Example

```python
car = Car("Toyota", "Camry", 2023, 15, 10)
truck = Truck("Ford", "F-150", 2023, 30, 20, mpg=20, cargo_weight=2000)
print(car)              # 2023 Toyota Camry
print(car.range())      # 300
print(truck.fuel_efficiency())  # 16.0
```
''',
        'difficulty': 'hard',
        'order': 5,
        'item_order': 8,
        'starter_code': (
            'class Vehicle:\n'
            '    """Base class for all vehicles."""\n'
            '\n'
            '    def __init__(self, make, model, year, fuel_capacity, fuel_level=0):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def refuel(self, amount):\n'
            '        # TODO: add fuel up to capacity\n'
            '        pass\n'
            '\n'
            '    def fuel_efficiency(self):\n'
            '        return 0\n'
            '\n'
            '    def range(self):\n'
            '        # TODO: fuel_level * fuel_efficiency\n'
            '        pass\n'
            '\n'
            '    def __str__(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '\n'
            'class Car(Vehicle):\n'
            '    def __init__(self, make, model, year, fuel_capacity, fuel_level=0, mpg=30):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def fuel_efficiency(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '\n'
            'class Truck(Vehicle):\n'
            '    def __init__(self, make, model, year, fuel_capacity, fuel_level=0, mpg=18, cargo_weight=0):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def fuel_efficiency(self):\n'
            '        # TODO: mpg - cargo_weight/500, minimum 5\n'
            '        pass\n'
            '\n'
            '\n'
            'class Motorcycle(Vehicle):\n'
            '    def __init__(self, make, model, year, fuel_capacity, fuel_level=0, mpg=50):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '    def fuel_efficiency(self):\n'
            '        # TODO\n'
            '        pass\n'
            '\n'
            '\n'
            '# --- Demo ---\n'
            'car = Car("Toyota", "Camry", 2023, 15, 10)\n'
            'truck = Truck("Ford", "F-150", 2023, 30, 20, mpg=20, cargo_weight=2000)\n'
            'moto = Motorcycle("Harley", "Sportster", 2023, 5, 5)\n'
            'print(car)\n'
            'print(car.range())\n'
            'print(truck.fuel_efficiency())\n'
            'print(moto.range())\n'
        ),
        'hints': [
            'Call super().__init__(make, model, year, fuel_capacity, fuel_level) in each subclass.',
            'In refuel, cap the total at fuel_capacity: self.fuel_level = min(self.fuel_level + amount, self.fuel_capacity).',
            'For Truck efficiency, use max(self.mpg - self.cargo_weight / 500, 5).',
            'range() simply multiplies fuel_level by the fuel_efficiency() return value.',
        ],
        'max_score': 100,
        'test_weight': 0.6,
        'output_weight': 0.4,
        'input_output_pairs': [
            {
                'input': '',
                'expected_output': '2023 Toyota Camry\n300\n16.0\n250',
            },
        ],
        'test_cases_code': '''
import unittest

class TestVehicles(unittest.TestCase):

    def setUp(self):
        exec(open("student_code.py").read(), globals())
        self.Vehicle = globals()["Vehicle"]
        self.Car = globals()["Car"]
        self.Truck = globals()["Truck"]
        self.Motorcycle = globals()["Motorcycle"]

    def test_car_str(self):
        car = self.Car("Toyota", "Camry", 2023, 15, 10)
        self.assertEqual(str(car), "2023 Toyota Camry")

    def test_car_range(self):
        car = self.Car("Toyota", "Camry", 2023, 15, 10, mpg=30)
        self.assertEqual(car.range(), 300)

    def test_truck_efficiency_with_cargo(self):
        truck = self.Truck("Ford", "F-150", 2023, 30, 20, mpg=20, cargo_weight=2000)
        self.assertAlmostEqual(truck.fuel_efficiency(), 16.0)

    def test_truck_efficiency_minimum(self):
        truck = self.Truck("Ford", "F-150", 2023, 30, 20, mpg=10, cargo_weight=5000)
        self.assertEqual(truck.fuel_efficiency(), 5)

    def test_motorcycle_range(self):
        moto = self.Motorcycle("Harley", "Sportster", 2023, 5, 5, mpg=50)
        self.assertEqual(moto.range(), 250)

    def test_refuel_cap(self):
        car = self.Car("Toyota", "Camry", 2023, 15, 10)
        car.refuel(100)
        self.assertEqual(car.fuel_level, 15)

    def test_inheritance(self):
        car = self.Car("Toyota", "Camry", 2023, 15)
        self.assertIsInstance(car, self.Vehicle)

if __name__ == "__main__":
    unittest.main()
''',
    },
]
