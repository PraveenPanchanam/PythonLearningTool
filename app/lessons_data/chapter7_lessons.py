CHAPTER_ORDER = 7

LESSONS = [
    {
        'title': 'Classes and Objects',
        'description': 'Understand the fundamentals of object-oriented programming by learning how to define classes, create objects, and work with instance variables and methods.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'what-is-oop',
                'title': 'What Is Object-Oriented Programming?',
                'diagram': {
                    'id': 'ch7-inheritance',
                    'title': 'Class Inheritance Hierarchy',
                    'file': 'diagrams/ch7-inheritance.svg',
                    'data_file': 'diagrams/excalidraw-data/ch7-inheritance.json',
                },
                'content': """## What Is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a way of organizing code around **objects** - bundles of related data and behavior. Instead of writing a long sequence of instructions, you model your program after real-world things.

### Real-Life Analogy

Think about a **bank account** in the real world:

- It has **data** (attributes): account number, owner name, balance.
- It has **behaviors** (actions): deposit money, withdraw money, check balance.

In OOP, we represent this as a **class** - a blueprint that defines what data and behavior a bank account should have. Each actual account (yours, mine, your neighbor's) is an **object** - a specific instance created from that blueprint.

```
Class: BankAccount (the blueprint)
    - Data: account_number, owner, balance
    - Behavior: deposit(), withdraw(), get_balance()

Objects (specific instances):
    - Alice's account: #1001, Alice, $5000
    - Bob's account:   #1002, Bob,   $3200
```

### Why OOP?

OOP helps you:

1. **Organize code** - related data and functions are grouped together.
2. **Reuse code** - create many objects from one class.
3. **Model real things** - your code mirrors how you think about the world.
4. **Manage complexity** - large programs become collections of interacting objects.

### Classes vs. Objects

| Concept | Analogy              | Example                  |
|---------|----------------------|--------------------------|
| Class   | Cookie cutter        | `Car` class definition   |
| Object  | An actual cookie     | `my_car = Car("Toyota")` |
| Class   | Architectural plan   | `House` class            |
| Object  | A built house        | `my_house = House(3, 2)` |

A class is defined once but can create unlimited objects.""",
                'exercise': None,
            },
            {
                'id': 'defining-a-class',
                'title': 'Defining Your First Class',
                'content': """## Defining Your First Class

In Python, you define a class using the `class` keyword. The `__init__` method (called the **constructor** or **initializer**) runs automatically when you create a new object.

### Basic Syntax

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def some_method(self):
        # method body
        pass
```

### The `self` Parameter

Every method in a class receives `self` as its first parameter. `self` refers to the **specific object** that the method is being called on. It is how an object accesses its own data.

Think of `self` like the word "my" in everyday language:
- When Alice says "my balance", she means *her* balance.
- When Bob says "my balance", he means *his* balance.
- `self` is how each object refers to "my data".

### Real-Life Example: Student Class

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")

# Creating objects (instances)
alice = Student("Alice", 10)
bob = Student("Bob", 11)

# Each object has its own data
alice.enroll("Math")
alice.enroll("Science")
bob.enroll("English")

alice.display()
bob.display()
```

### Real-Life Example: Car Class

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def drive(self, miles):
        self.odometer += miles

    def describe(self):
        return f"{self.year} {self.make} {self.model} ({self.odometer} miles)"

my_car = Car("Toyota", "Camry", 2022)
my_car.drive(150)
my_car.drive(75)
print(my_car.describe())  # 2022 Toyota Camry (225 miles)
```

### Accessing Attributes Directly

You can read and modify object attributes using dot notation:

```python
student = Student("Charlie", 12)
print(student.name)    # Charlie
student.grade = 11     # modify the attribute directly
print(student.grade)   # 11
```""",
                'exercise': {
                    'instructions': 'Create a BankAccount class with __init__ that accepts owner and initial balance. Add a deposit method that increases the balance and a display method that prints the owner and balance. Create an account, make two deposits, and display the result.',
                    'starter_code': 'class BankAccount:\n    def __init__(self, owner, balance):\n        self.owner = owner\n        self.balance = balance\n\n    def deposit(self, amount):\n        self.balance += amount\n\n    def display(self):\n        print(f"Owner: {self.owner}")\n        print(f"Balance: ${self.balance:.2f}")\n\n\n# Create an account for Alice with $1000\naccount = BankAccount("Alice", 1000)\n\n# Deposit $500 and then $250\naccount.deposit(500)\naccount.deposit(250)\n\n# Display account details\naccount.display()\n',
                    'expected_output': 'Owner: Alice\nBalance: $1750.00',
                    'hint': 'In __init__, store the owner and balance as self.owner and self.balance. The deposit method adds amount to self.balance. The display method uses f-strings with :.2f formatting.',
                },
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange these code blocks to define a Dog class and create an object:',
                    'code_blocks': [
                        'class Dog:',
                        '    def __init__(self, name):',
                        '        self.name = name',
                        'my_dog = Dog("Buddy")',
                        'print(my_dog.name)',
                    ],
                    'explanation': 'First we define the class with "class Dog:", then the __init__ method with self and name, store the name with self.name, create an object, and finally print its name!',
                },
            },
            {
                'id': 'methods-and-behavior',
                'title': 'Methods: Giving Objects Behavior',
                'content': """## Methods: Giving Objects Behavior

**Methods** are functions defined inside a class that operate on the object's data. They give objects their behavior - the ability to do things.

### Types of Methods

**1. Instance Methods** - the most common type, they access and modify the object's data through `self`:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height
```

### Methods That Return Values vs. Print Values

Methods can either return a value (for use in expressions) or print directly. Returning is generally more flexible:

```python
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def summary(self):
        f = self.to_fahrenheit()
        k = self.to_kelvin()
        return f"{self.celsius}C = {f:.1f}F = {k:.1f}K"

temp = TemperatureConverter(100)
print(temp.summary())  # 100C = 212.0F = 373.1K
```

### Real-Life Example: Shopping Cart

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "qty": quantity})

    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["qty"]
        return total

    def item_count(self):
        count = 0
        for item in self.items:
            count += item["qty"]
        return count

cart = ShoppingCart()
cart.add_item("Notebook", 4.99, 3)
cart.add_item("Pen", 1.50, 5)
cart.add_item("Eraser", 0.75, 2)

print(f"Items: {cart.item_count()}")
print(f"Total: ${cart.get_total():.2f}")
```

### Methods Calling Other Methods

Methods can call other methods on the same object using `self`:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False
```""",
                'exercise': {
                    'instructions': 'Create a ShoppingCart class with methods to add items, calculate the total cost, and display a summary. Add three items to the cart and print the item count and total.',
                    'starter_code': 'class ShoppingCart:\n    def __init__(self):\n        self.items = []\n\n    def add_item(self, name, price, quantity):\n        self.items.append({"name": name, "price": price, "qty": quantity})\n\n    def get_total(self):\n        total = 0\n        for item in self.items:\n            total += item["price"] * item["qty"]\n        return total\n\n    def item_count(self):\n        count = 0\n        for item in self.items:\n            count += item["qty"]\n        return count\n\n\n# Create a cart and add items\ncart = ShoppingCart()\ncart.add_item("Book", 12.99, 2)\ncart.add_item("Pen", 1.50, 5)\ncart.add_item("Folder", 3.25, 1)\n\n# Print summary\nprint(f"Items in cart: {cart.item_count()}")\nprint(f"Total: ${cart.get_total():.2f}")\n',
                    'expected_output': 'Items in cart: 8\nTotal: $36.73',
                    'hint': 'The add_item method appends a dictionary to self.items. get_total loops through items and sums price * qty. item_count sums all quantities.',
                },
            },
            {
                'id': 'class-vs-instance-variables',
                'title': 'Class Variables vs. Instance Variables',
                'content': """## Class Variables vs. Instance Variables

Python classes have two types of variables with different scopes and purposes.

### Instance Variables (per object)

**Instance variables** belong to a specific object. Each object has its own copy. They are defined using `self.variable_name` inside methods:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name     # instance variable
        self.breed = breed   # instance variable

dog1 = Dog("Max", "Labrador")
dog2 = Dog("Bella", "Poodle")

# Each dog has its own name and breed
print(dog1.name)  # Max
print(dog2.name)  # Bella
```

### Class Variables (shared by all objects)

**Class variables** are defined directly in the class body (outside any method). They are shared by ALL instances:

```python
class Employee:
    company = "TechCorp"    # class variable - shared by all
    employee_count = 0       # class variable - tracks total

    def __init__(self, name, role):
        self.name = name     # instance variable - unique per employee
        self.role = role     # instance variable
        Employee.employee_count += 1

    def display(self):
        print(f"{self.name} ({self.role}) at {Employee.company}")

emp1 = Employee("Alice", "Engineer")
emp2 = Employee("Bob", "Designer")
emp3 = Employee("Charlie", "Manager")

emp1.display()
emp2.display()
print(f"Total employees: {Employee.employee_count}")
```

### Real-Life Analogy

Think of a **university**:

- **Class variable**: The university name (all students share the same university).
- **Instance variable**: Each student's name, ID, and GPA (unique to each student).

```python
class UniversityStudent:
    university = "State University"  # same for all students
    total_students = 0

    def __init__(self, name, major):
        self.name = name              # unique per student
        self.major = major            # unique per student
        self.gpa = 0.0               # unique per student
        UniversityStudent.total_students += 1

    def info(self):
        return f"{self.name} - {self.major} at {UniversityStudent.university}"
```

### When to Use Each

| Use Case                          | Variable Type    |
|-----------------------------------|------------------|
| Data unique to each object        | Instance variable |
| Data shared across all objects    | Class variable    |
| Tracking count of all objects     | Class variable    |
| Constants for the class           | Class variable    |
| Object's state or properties      | Instance variable |""",
                'exercise': {
                    'instructions': 'Create a Product class with a class variable to track the total number of products created. Each product should have a name and price. Create three products, print each product info, and then print the total number of products.',
                    'starter_code': 'class Product:\n    total_products = 0  # class variable\n\n    def __init__(self, name, price):\n        self.name = name\n        self.price = price\n        Product.total_products += 1\n\n    def info(self):\n        return f"{self.name}: ${self.price:.2f}"\n\n\n# Create three products\np1 = Product("Laptop", 999.99)\np2 = Product("Mouse", 29.99)\np3 = Product("Keyboard", 79.99)\n\n# Print each product\nprint(p1.info())\nprint(p2.info())\nprint(p3.info())\n\n# Print total count\nprint(f"Total products: {Product.total_products}")\n',
                    'expected_output': 'Laptop: $999.99\nMouse: $29.99\nKeyboard: $79.99\nTotal products: 3',
                    'hint': 'Define total_products = 0 at the class level. In __init__, increment Product.total_products (not self.total_products). The info method returns a formatted string.',
                },
            },
            {
                'id': 'practical-oop-example',
                'title': 'Putting It All Together: A Library System',
                'content': """## Putting It All Together: A Library System

Let us build a small library management system that demonstrates all the OOP concepts from this lesson. This is the kind of problem you might encounter in a real software project.

### The Book Class

```python
class Book:
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = False
        Book.total_books += 1

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def status(self):
        state = "Checked Out" if self.is_checked_out else "Available"
        return f'"{self.title}" by {self.author} - {state}'
```

### Using the Book Class

```python
# Create books
book1 = Book("Python Basics", "J. Smith", 350)
book2 = Book("Data Science 101", "A. Johnson", 420)
book3 = Book("Web Development", "M. Brown", 280)

# Check out a book
book1.check_out()

# Print status of all books
for book in [book1, book2, book3]:
    print(book.status())

print(f"\\nTotal books in library: {Book.total_books}")
```

### Design Principles

When designing classes, think about:

1. **What data does this thing have?** These become your instance variables.
2. **What can this thing do?** These become your methods.
3. **What is shared across all instances?** These become class variables.

### Common Mistakes to Avoid

```python
# MISTAKE 1: Forgetting self
class Bad:
    def __init__(self, value):
        value = value  # This does NOT save it to the object!
        # Should be: self.value = value

# MISTAKE 2: Mutable default class variable
class AlsoBad:
    items = []  # DANGER: This list is shared by ALL instances!

    def add(self, item):
        self.items.append(item)  # Modifies the shared list

# FIX: Use instance variable instead
class Good:
    def __init__(self):
        self.items = []  # Each object gets its own list

    def add(self, item):
        self.items.append(item)
```

### Summary

| Concept            | Purpose                              | Syntax                        |
|--------------------|--------------------------------------|-------------------------------|
| `class`            | Define a blueprint                   | `class MyClass:`              |
| `__init__`         | Initialize new objects               | `def __init__(self, ...):`    |
| `self`             | Reference to the current object      | `self.attribute = value`      |
| Instance variable  | Data unique to each object           | `self.name = name`            |
| Class variable     | Data shared by all objects           | `count = 0` (at class level)  |
| Method             | Function that belongs to the class   | `def method(self):`           |""",
                'exercise': None,
            },
        ],
    },
    {
        'title': 'Inheritance and Polymorphism',
        'description': 'Learn how to create class hierarchies using inheritance, override methods in child classes, and leverage polymorphism to write flexible code.',
        'order': 2,
        'item_order': 4,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'what-is-inheritance',
                'title': 'What Is Inheritance?',
                'content': """## What Is Inheritance?

**Inheritance** allows a new class (called the **child** or **subclass**) to inherit attributes and methods from an existing class (called the **parent** or **base class**). The child class can then add new features or modify inherited ones.

### Real-Life Analogy

Think of biological inheritance:
- A **Vehicle** is a general concept with properties like speed, fuel type, and number of wheels.
- A **Car** is a specific type of Vehicle that inherits all vehicle properties but adds features like number of doors and trunk size.
- A **Truck** is another type of Vehicle that adds cargo capacity and towing power.

The child does not need to redefine everything from scratch. It starts with everything the parent has and builds on top of it.

### Basic Syntax

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Child(Parent):  # Child inherits from Parent
    pass               # Has everything Parent has, no additions yet

obj = Child("Alice")
obj.greet()  # Hello, I am Alice - inherited from Parent
```

### The `super()` Function

`super()` lets a child class call methods from its parent. This is most commonly used in `__init__` to reuse the parent's initialization:

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # Call parent's __init__
        self.breed = breed               # Add new attribute

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

rex = Dog("Rex", "German Shepherd")
print(rex.speak())             # Rex says Woof! (inherited)
print(rex.fetch("ball"))       # Rex fetches the ball! (new method)
print(f"Breed: {rex.breed}")   # Breed: German Shepherd (new attribute)
```

### Why Use Inheritance?

1. **Code reuse** - write common functionality once in the parent class.
2. **Logical organization** - mirror real-world relationships (a Dog IS an Animal).
3. **Easy maintenance** - fix a bug in the parent and all children benefit.
4. **Extensibility** - add new types without changing existing code.""",
                'exercise': {
                    'instructions': 'Create an Animal base class with a name and sound. Then create Dog and Cat child classes that set their own default sounds using super(). Create one of each and print their speak() output.',
                    'starter_code': 'class Animal:\n    def __init__(self, name, sound):\n        self.name = name\n        self.sound = sound\n\n    def speak(self):\n        return f"{self.name} says {self.sound}!"\n\n\nclass Dog(Animal):\n    def __init__(self, name):\n        super().__init__(name, "Woof")\n\n\nclass Cat(Animal):\n    def __init__(self, name):\n        super().__init__(name, "Meow")\n\n\n# Create animals\ndog = Dog("Buddy")\ncat = Cat("Whiskers")\n\n# Print their sounds\nprint(dog.speak())\nprint(cat.speak())\n',
                    'expected_output': 'Buddy says Woof!\nWhiskers says Meow!',
                    'hint': 'Each child class __init__ should call super().__init__(name, sound) with the appropriate default sound for that animal type.',
                },
            },
            {
                'id': 'method-overriding',
                'title': 'Method Overriding',
                'content': """## Method Overriding

A child class can **override** (replace) a method inherited from its parent by defining a method with the same name. This lets the child customize behavior while keeping the same interface.

### Basic Example

```python
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0  # Base shape has no specific area

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):  # Override parent's area method
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):  # Override parent's area method
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)
print(c.describe())  # Circle with area 78.54
print(r.describe())  # Rectangle with area 24.00
```

Notice how `describe()` calls `self.area()`, and each class uses its own version of `area()`. The parent class defines the template; the children fill in the details.

### Real-Life Example: Employee Types

A company has different types of employees with different pay structures:

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def summary(self):
        return f"{self.name}: ${self.calculate_pay():,.2f}"


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name, annual_salary)

    def calculate_pay(self):
        return self.base_salary / 12  # Monthly pay


class CommissionEmployee(Employee):
    def __init__(self, name, base_salary, sales, commission_rate):
        super().__init__(name, base_salary)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_pay(self):
        commission = self.sales * self.commission_rate
        return self.base_salary / 12 + commission
```

### Extending (Not Just Replacing) Parent Methods

Sometimes you want to add to the parent's behavior rather than completely replacing it. Use `super()` inside the overridden method:

```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        super().log(f"2024-01-15 | {message}")  # Extends parent behavior

logger = TimestampLogger()
logger.log("Server started")  # [LOG] 2024-01-15 | Server started
```""",
                'exercise': {
                    'instructions': 'Create a base Employee class and two child classes: SalariedEmployee (monthly pay = annual salary / 12) and HourlyEmployee (monthly pay = hourly rate * hours per week * 4). Override the calculate_monthly_pay method in each. Create one of each and print their summaries.',
                    'starter_code': 'class Employee:\n    def __init__(self, name):\n        self.name = name\n\n    def calculate_monthly_pay(self):\n        return 0\n\n    def summary(self):\n        pay = self.calculate_monthly_pay()\n        return f"{self.name}: ${pay:,.2f}/month"\n\n\nclass SalariedEmployee(Employee):\n    def __init__(self, name, annual_salary):\n        super().__init__(name)\n        self.annual_salary = annual_salary\n\n    def calculate_monthly_pay(self):\n        return self.annual_salary / 12\n\n\nclass HourlyEmployee(Employee):\n    def __init__(self, name, hourly_rate, hours_per_week):\n        super().__init__(name)\n        self.hourly_rate = hourly_rate\n        self.hours_per_week = hours_per_week\n\n    def calculate_monthly_pay(self):\n        return self.hourly_rate * self.hours_per_week * 4\n\n\n# Create employees\nmanager = SalariedEmployee("Alice", 96000)\nworker = HourlyEmployee("Bob", 25, 40)\n\n# Print summaries\nprint(manager.summary())\nprint(worker.summary())\n',
                    'expected_output': 'Alice: $8,000.00/month\nBob: $4,000.00/month',
                    'hint': 'SalariedEmployee overrides calculate_monthly_pay to return annual_salary / 12. HourlyEmployee overrides it to return hourly_rate * hours_per_week * 4 (weeks in a month).',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Look at this code and pick the correct answer:',
                    'code_snippet': 'class Animal:\n    def speak(self):\n        return "..."\n\nclass Cat(Animal):\n    def speak(self):\n        return "Meow!"\n\nmy_cat = Cat()\nprint(my_cat.speak())',
                    'question': 'What will this code print?',
                    'options': [
                        {'text': 'Meow!', 'correct': True},
                        {'text': '...', 'correct': False},
                        {'text': 'Error', 'correct': False},
                        {'text': 'None', 'correct': False},
                    ],
                    'explanation': 'Cat overrides the speak() method from Animal. When we call speak() on a Cat object, it uses the Cat version which returns "Meow!" — this is called method overriding!',
                },
            },
            {
                'id': 'polymorphism',
                'title': 'Polymorphism: One Interface, Many Forms',
                'content': """## Polymorphism: One Interface, Many Forms

**Polymorphism** means "many forms." In programming, it means that objects of different classes can be used through the same interface. You can call the same method on different objects, and each one responds in its own way.

### Real-Life Analogy

Think of a **remote control**. The "play" button works on:
- A **DVD player** - it plays a movie.
- A **music system** - it plays a song.
- A **game console** - it resumes the game.

Same button (interface), different behavior (implementation). That is polymorphism.

### Polymorphism in Action

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: Meow!"

class Duck:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: Quack!"

# Polymorphism - same method call, different behavior
animals = [Dog("Rex"), Cat("Whiskers"), Duck("Donald")]

for animal in animals:
    print(animal.speak())  # Each animal responds differently
```

### Real-Life Example: Payment Processing

An e-commerce system might accept different payment methods:

```python
class CreditCard:
    def __init__(self, last_four):
        self.last_four = last_four

    def process_payment(self, amount):
        return f"Charged ${amount:.2f} to card ending in {self.last_four}"

class PayPal:
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Sent ${amount:.2f} via PayPal to {self.email}"

class BankTransfer:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def process_payment(self, amount):
        return f"Transferred ${amount:.2f} via {self.bank_name}"

# Process payments polymorphically
payments = [
    CreditCard("4242"),
    PayPal("user@email.com"),
    BankTransfer("First National"),
]

order_total = 49.99
for method in payments:
    print(method.process_payment(order_total))
```

### Polymorphism with Inheritance

Polymorphism works naturally with inheritance because child classes can override parent methods:

```python
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Notification: {self.message}"

class EmailNotification(Notification):
    def send(self):
        return f"Email sent: {self.message}"

class SMSNotification(Notification):
    def send(self):
        return f"SMS sent: {self.message}"

class PushNotification(Notification):
    def send(self):
        return f"Push alert: {self.message}"

notifications = [
    EmailNotification("Your order shipped!"),
    SMSNotification("Verification code: 1234"),
    PushNotification("New message from Alice"),
]

for notif in notifications:
    print(notif.send())
```

### The `isinstance()` Function

Sometimes you need to check what type an object is:

```python
dog = Dog("Rex")
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Cat))     # False
```""",
                'exercise': {
                    'instructions': 'Create three notification classes (EmailNotification, SMSNotification, PushNotification) that all have a send() method but with different output formats. Loop through a list of notifications and call send() on each one.',
                    'starter_code': 'class EmailNotification:\n    def __init__(self, message):\n        self.message = message\n\n    def send(self):\n        return f"Email: {self.message}"\n\n\nclass SMSNotification:\n    def __init__(self, message):\n        self.message = message\n\n    def send(self):\n        return f"SMS: {self.message}"\n\n\nclass PushNotification:\n    def __init__(self, message):\n        self.message = message\n\n    def send(self):\n        return f"Push: {self.message}"\n\n\n# Create a list of different notifications\nnotifications = [\n    EmailNotification("Your order has shipped!"),\n    SMSNotification("Code: 5678"),\n    PushNotification("New follower!"),\n]\n\n# Send each notification using polymorphism\nfor notif in notifications:\n    print(notif.send())\n',
                    'expected_output': 'Email: Your order has shipped!\nSMS: Code: 5678\nPush: New follower!',
                    'hint': 'Each class has the same send() method signature but returns a differently formatted string. The loop works because Python does not care about the type - it just calls send() on whatever object it finds.',
                },
            },
            {
                'id': 'isinstance-and-class-hierarchies',
                'title': 'Checking Types and Building Hierarchies',
                'content': """## Checking Types and Building Hierarchies

As your class hierarchies grow, you need tools to understand relationships between objects and design clean inheritance trees.

### The `isinstance()` Function with Inheritance

`isinstance()` returns `True` for parent classes too, reflecting the "is-a" relationship:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

my_tesla = ElectricCar("Tesla")

print(isinstance(my_tesla, ElectricCar))  # True - it IS an ElectricCar
print(isinstance(my_tesla, Car))          # True - it IS a Car
print(isinstance(my_tesla, Vehicle))      # True - it IS a Vehicle
```

### Multi-Level Inheritance

Classes can inherit through multiple levels, forming a hierarchy:

```python
class LivingThing:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

class Animal(LivingThing):
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs

class Pet(Animal):
    def __init__(self, name, legs, owner):
        super().__init__(name, legs)
        self.owner = owner

    def info(self):
        return f"{self.name} ({self.legs} legs) - Owner: {self.owner}"

my_pet = Pet("Max", 4, "Alice")
print(my_pet.info())
print(f"Is alive: {my_pet.is_alive}")  # Inherited from LivingThing
```

### The `issubclass()` Function

Check if one class is a subclass of another:

```python
print(issubclass(Car, Vehicle))        # True
print(issubclass(ElectricCar, Vehicle)) # True
print(issubclass(Vehicle, Car))         # False - Vehicle is the PARENT
```

### Design Tips for Inheritance

1. **"Is-a" relationship**: Use inheritance when the child IS A type of the parent (a Dog IS an Animal).
2. **Keep hierarchies shallow**: Deep inheritance (5+ levels) becomes hard to maintain.
3. **Prefer composition over deep inheritance**: Sometimes it is better to have a class CONTAIN another class rather than inherit from it.

```python
# Composition example (HAS-A relationship)
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Car HAS an Engine

    def describe(self):
        return f"{self.brand} with {self.engine.horsepower}hp engine"

v8 = Engine(450)
mustang = Car("Ford Mustang", v8)
print(mustang.describe())
```""",
                'exercise': None,
            },
        ],
    },
    {
        'title': 'Special Methods and Properties',
        'description': 'Master Python special (dunder) methods like __str__, __repr__, __len__, and __eq__, and learn to use the @property decorator to create clean interfaces.',
        'order': 3,
        'item_order': 6,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'intro-to-special-methods',
                'title': 'Introduction to Special Methods',
                'content': """## Introduction to Special Methods

**Special methods** (also called **dunder methods** because they have **d**ouble **under**scores) are methods with names like `__init__`, `__str__`, `__len__`, etc. They let your objects work with Python's built-in operations and syntax.

You have already used one: `__init__` runs automatically when you create an object. There are many more that let your objects behave like built-in Python types.

### Why Special Methods Matter

Without special methods, your objects are opaque to Python:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p)  # <__main__.Point object at 0x...> - not very helpful!
```

With special methods, your objects become first-class citizens:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p)  # Point(3, 4) - much better!
```

### Real-Life Analogy

Think of special methods as teaching your objects how to respond to everyday actions:

- `__str__` teaches your object how to introduce itself ("Hi, I am Point(3, 4)").
- `__len__` teaches your object how to answer "how big are you?"
- `__eq__` teaches your object how to answer "are you equal to this other thing?"
- `__add__` teaches your object how to add itself to another object.

It is like giving a robot instructions for common social situations.

### Common Special Methods Overview

| Method       | Triggered By          | Purpose                          |
|-------------|----------------------|----------------------------------|
| `__init__`  | `MyClass()`          | Initialize a new object          |
| `__str__`   | `print(obj)`, `str(obj)` | Human-readable string        |
| `__repr__`  | `repr(obj)`          | Developer-readable string        |
| `__len__`   | `len(obj)`           | Return the length                |
| `__eq__`    | `obj1 == obj2`       | Equality comparison              |
| `__lt__`    | `obj1 < obj2`        | Less-than comparison             |
| `__add__`   | `obj1 + obj2`        | Addition                         |
| `__contains__` | `x in obj`       | Membership testing               |""",
                'exercise': None,
            },
            {
                'id': 'str-and-repr',
                'title': '__str__ and __repr__: String Representations',
                'content': """## __str__ and __repr__: String Representations

These two methods control how your object is displayed as a string. They serve different audiences.

### `__str__` - For End Users

`__str__` returns a **human-readable** string. It is called by `print()` and `str()`:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

item = Product("Wireless Mouse", 29.99)
print(item)           # Wireless Mouse - $29.99
print(f"Item: {item}")  # Item: Wireless Mouse - $29.99
```

### `__repr__` - For Developers

`__repr__` returns a **developer-oriented** string, ideally one that could recreate the object. It is what you see in the interactive console:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

item = Product("Wireless Mouse", 29.99)
print(str(item))    # Wireless Mouse - $29.99  (user-friendly)
print(repr(item))   # Product('Wireless Mouse', 29.99)  (developer-friendly)
```

### Real-Life Example: Temperature Class

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __repr__(self):
        return f"Temperature({self.celsius})"

    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

temp = Temperature(100)
print(temp)            # 100°C (for users)
print(repr(temp))      # Temperature(100) (for developers)
print(f"Boiling point: {temp}")  # Boiling point: 100°C
```

### Real-Life Example: Contact Card

```python
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email})"

    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}', '{self.phone}')"

alice = Contact("Alice Smith", "alice@email.com", "555-1234")
print(alice)        # Alice Smith (alice@email.com)
print(repr(alice))  # Contact('Alice Smith', 'alice@email.com', '555-1234')
```

### Best Practice

- Always implement at least `__repr__`. If `__str__` is not defined, Python falls back to `__repr__`.
- `__str__` should be readable by anyone; `__repr__` should be useful for debugging.""",
                'exercise': {
                    'instructions': 'Create a Book class with title, author, and pages. Implement __str__ to return a user-friendly format and __repr__ to return a developer format. Create two books and print both their str and repr representations.',
                    'starter_code': 'class Book:\n    def __init__(self, title, author, pages):\n        self.title = title\n        self.author = author\n        self.pages = pages\n\n    def __str__(self):\n        return f"{self.title} by {self.author}"\n\n    def __repr__(self):\n        return f"Book(\'{self.title}\', \'{self.author}\', {self.pages})"\n\n\n# Create two books\nbook1 = Book("Python Crash Course", "Eric Matthes", 544)\nbook2 = Book("Clean Code", "Robert Martin", 464)\n\n# Print user-friendly format (uses __str__)\nprint(book1)\nprint(book2)\n\n# Print developer format (uses __repr__)\nprint(repr(book1))\nprint(repr(book2))\n',
                    'expected_output': "Python Crash Course by Eric Matthes\nClean Code by Robert Martin\nBook('Python Crash Course', 'Eric Matthes', 544)\nBook('Clean Code', 'Robert Martin', 464)",
                    'hint': '__str__ should return a user-friendly string like "Title by Author". __repr__ should return a string that looks like the constructor call: Book(\'title\', \'author\', pages).',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this code will print? Type your guess!',
                    'code_snippet': 'class Pet:\n    def __init__(self, name, kind):\n        self.name = name\n        self.kind = kind\n    def __str__(self):\n        return f"{self.name} the {self.kind}"\n\nmy_pet = Pet("Buddy", "Dog")\nprint(my_pet)',
                    'expected_output': 'Buddy the Dog',
                    'explanation': 'When you print() an object, Python calls its __str__ method. Our __str__ returns an f-string combining name and kind, so we get "Buddy the Dog"!',
                },
            },
            {
                'id': 'len-eq-and-comparison',
                'title': '__len__, __eq__, and Comparisons',
                'content': """## __len__, __eq__, and Comparisons

These special methods let your objects work with Python's built-in operators and functions.

### `__len__` - Support for `len()`

Make `len()` work with your objects:

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

rock = Playlist("Classic Rock")
rock.add_song("Bohemian Rhapsody")
rock.add_song("Stairway to Heaven")
rock.add_song("Hotel California")

print(len(rock))  # 3
print(rock)        # Playlist 'Classic Rock' (3 songs)
```

### `__eq__` - Support for `==`

By default, `==` checks if two variables refer to the **same object in memory**. Override `__eq__` to compare by **value** instead:

```python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        if not isinstance(other, Color):
            return False
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __str__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

red1 = Color(255, 0, 0)
red2 = Color(255, 0, 0)
blue = Color(0, 0, 255)

print(red1 == red2)  # True - same values
print(red1 == blue)  # False - different values
```

### `__lt__` - Support for `<` (and sorting)

Implementing `__lt__` allows your objects to be sorted:

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __str__(self):
        return f"{self.name} (GPA: {self.gpa})"

students = [
    Student("Alice", 3.8),
    Student("Bob", 3.5),
    Student("Charlie", 3.9),
]

# sorted() uses __lt__ to compare
for s in sorted(students):
    print(s)
```

### Real-Life Example: Money Class

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

price = Money(29.99)
tax = Money(2.40)
total = price + tax
print(total)           # $32.39 USD
print(price == tax)    # False
print(price < total)   # True
```""",
                'exercise': {
                    'instructions': 'Create a Playlist class that supports len() and equality comparison. Two playlists are equal if they have the same songs (regardless of name). Add songs, print the length, and test equality between two playlists.',
                    'starter_code': 'class Playlist:\n    def __init__(self, name):\n        self.name = name\n        self.songs = []\n\n    def add_song(self, song):\n        self.songs.append(song)\n\n    def __len__(self):\n        return len(self.songs)\n\n    def __eq__(self, other):\n        if not isinstance(other, Playlist):\n            return False\n        return self.songs == other.songs\n\n    def __str__(self):\n        return f"{self.name}: {len(self)} songs"\n\n\n# Create two playlists with the same songs\nrock = Playlist("Rock Classics")\nrock.add_song("Bohemian Rhapsody")\nrock.add_song("Stairway to Heaven")\n\nfavorites = Playlist("My Favorites")\nfavorites.add_song("Bohemian Rhapsody")\nfavorites.add_song("Stairway to Heaven")\n\n# Create a different playlist\npop = Playlist("Pop Hits")\npop.add_song("Shape of You")\n\nprint(rock)\nprint(f"Songs in rock: {len(rock)}")\nprint(f"rock == favorites: {rock == favorites}")\nprint(f"rock == pop: {rock == pop}")\n',
                    'expected_output': 'Rock Classics: 2 songs\nSongs in rock: 2\nrock == favorites: True\nrock == pop: False',
                    'hint': '__len__ should return len(self.songs). __eq__ should compare self.songs with other.songs. Use isinstance() to handle the case where other is not a Playlist.',
                },
            },
            {
                'id': 'property-decorator',
                'title': 'The @property Decorator',
                'content': """## The @property Decorator

The `@property` decorator lets you define methods that are accessed like attributes. This gives you the simplicity of attribute access with the power of method logic.

### The Problem: Direct Attribute Access

With direct attribute access, anyone can set invalid values:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius  # No validation!

c = Circle(5)
c.radius = -10  # This makes no sense but Python allows it
```

### The Solution: @property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Convention: _ prefix for "private"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.radius)          # 5 - looks like attribute access
print(c.area)            # 78.53975 - calculated on the fly
print(c.circumference)   # 31.4159 - also calculated
```

### Real-Life Example: Temperature Converter

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(0)
print(f"{temp.celsius}C = {temp.fahrenheit}F")    # 0C = 32.0F

temp.celsius = 100
print(f"{temp.celsius}C = {temp.fahrenheit}F")    # 100C = 212.0F
```

### Read-Only Properties (Computed Attributes)

Sometimes you want properties that are calculated but cannot be set directly:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def is_square(self):
        return self.width == self.height

r = Rectangle(5, 5)
print(r.area)       # 25
print(r.is_square)  # True
# r.area = 30       # AttributeError - it is read-only
```

### Real-Life Example: Product with Discount

```python
class Product:
    def __init__(self, name, base_price, discount_percent=0):
        self.name = name
        self.base_price = base_price
        self.discount_percent = discount_percent

    @property
    def discount_amount(self):
        return self.base_price * (self.discount_percent / 100)

    @property
    def final_price(self):
        return self.base_price - self.discount_amount

    def __str__(self):
        if self.discount_percent > 0:
            return f"{self.name}: ${self.final_price:.2f} (was ${self.base_price:.2f})"
        return f"{self.name}: ${self.base_price:.2f}"
```

### When to Use @property

| Situation                                   | Use @property? |
|---------------------------------------------|----------------|
| Value is computed from other attributes     | Yes            |
| You need validation on setting a value      | Yes            |
| You want a read-only computed attribute     | Yes            |
| Simple data storage, no logic needed        | No, use a regular attribute |""",
                'exercise': {
                    'instructions': 'Create a Product class with a base price and discount percentage. Use @property to create a computed final_price attribute that applies the discount. Create two products and print their details.',
                    'starter_code': 'class Product:\n    def __init__(self, name, base_price, discount_percent=0):\n        self.name = name\n        self.base_price = base_price\n        self.discount_percent = discount_percent\n\n    @property\n    def discount_amount(self):\n        return self.base_price * (self.discount_percent / 100)\n\n    @property\n    def final_price(self):\n        return self.base_price - self.discount_amount\n\n    def __str__(self):\n        if self.discount_percent > 0:\n            return f"{self.name}: ${self.final_price:.2f} ({self.discount_percent}% off ${self.base_price:.2f})"\n        return f"{self.name}: ${self.base_price:.2f}"\n\n\n# Create products\nlaptop = Product("Laptop", 999.99, 15)\nmouse = Product("Mouse", 29.99)\n\n# Print product details\nprint(laptop)\nprint(mouse)\nprint(f"Laptop savings: ${laptop.discount_amount:.2f}")\n',
                    'expected_output': 'Laptop: $849.99 (15% off $999.99)\nMouse: $29.99\nLaptop savings: $150.00',
                    'hint': 'The discount_amount property calculates base_price * (discount_percent / 100). The final_price property subtracts discount_amount from base_price. The __str__ method formats the output differently based on whether there is a discount.',
                },
            },
            {
                'id': 'putting-it-all-together',
                'title': 'Putting It All Together: A Complete Class',
                'content': """## Putting It All Together: A Complete Class

Let us build a complete, well-designed class that uses all the special methods and properties we have learned. This demonstrates how professional Python classes are structured.

### Real-Life Example: Library Book Tracker

```python
class LibraryBook:
    total_books = 0

    def __init__(self, title, author, isbn, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self._times_borrowed = 0
        LibraryBook.total_books += 1

    @property
    def times_borrowed(self):
        return self._times_borrowed

    @property
    def popularity(self):
        if self._times_borrowed > 10:
            return "Bestseller"
        elif self._times_borrowed > 5:
            return "Popular"
        elif self._times_borrowed > 0:
            return "Moderate"
        return "New"

    def borrow(self):
        self._times_borrowed += 1

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        return f"LibraryBook('{self.title}', '{self.author}', '{self.isbn}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, LibraryBook):
            return False
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.pages < other.pages
```

### Using the Complete Class

```python
book1 = LibraryBook("Python Basics", "J. Smith", "978-1", 350)
book2 = LibraryBook("Data Science", "A. Jones", "978-2", 420)
book3 = LibraryBook("Python Basics", "J. Smith", "978-1", 350)  # same ISBN

# String representations
print(book1)            # "Python Basics" by J. Smith
print(repr(book2))      # LibraryBook('Data Science', 'A. Jones', '978-2', 420)

# Length (pages)
print(f"Pages: {len(book1)}")  # Pages: 350

# Equality (by ISBN)
print(f"Same book? {book1 == book3}")  # True (same ISBN)
print(f"Same book? {book1 == book2}")  # False (different ISBN)

# Sorting (by pages)
books = [book2, book1]
for b in sorted(books):
    print(f"  {b} - {len(b)} pages")

# Properties
for _ in range(7):
    book1.borrow()
print(f"Popularity: {book1.popularity}")  # Popular
```

### Design Checklist for a Well-Designed Class

When creating a class, consider implementing:

1. **`__init__`** - Always. Set up the object's initial state.
2. **`__str__`** - Almost always. Make printing meaningful.
3. **`__repr__`** - Recommended. Help with debugging.
4. **`__eq__`** - When you need value-based equality.
5. **`__len__`** - When "size" makes sense for your object.
6. **`__lt__`** - When your objects should be sortable.
7. **`@property`** - For computed values and validation.

### Summary Table

| Feature              | Benefit                                        |
|----------------------|------------------------------------------------|
| `__str__`            | User-friendly display with `print()`           |
| `__repr__`           | Developer-friendly display for debugging       |
| `__len__`            | Support `len()` for your objects               |
| `__eq__`             | Compare objects by value with `==`             |
| `__lt__`             | Sort objects with `sorted()`                   |
| `@property`          | Computed attributes and validation             |
| Class variables      | Shared data across all instances               |""",
                'exercise': None,
            },
        ],
    },
]
