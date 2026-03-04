CHAPTER_ORDER = 5

LESSONS = [
    {
        'title': 'Lists and Tuples',
        'description': 'Learn how to store and manipulate ordered collections of data using lists and tuples -- from to-do lists and student rosters to GPS coordinates.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'introduction-to-lists',
                'title': 'Introduction to Lists',
                'diagram': {
                    'id': 'ch5-data-structures',
                    'title': 'Python Data Structures Comparison',
                    'file': 'diagrams/ch5-data-structures.svg',
                    'data_file': 'diagrams/excalidraw-data/ch5-data-structures.json',
                },
                'content': """## Introduction to Lists

In everyday life, you make lists all the time: a grocery list, a to-do list, a playlist of songs. A Python **list** works the same way -- it is an ordered collection of items stored under a single name.

### Creating Lists

Use square brackets `[]` with items separated by commas:

```python
# A grocery list
groceries = ["milk", "eggs", "bread", "butter"]

# A list of test scores
scores = [85, 92, 78, 95, 88]

# A list with mixed types (valid but less common)
mixed = ["Alice", 25, True, 3.14]

# An empty list
empty = []
```

### Accessing Items by Index

Like seats in a movie theater, every item in a list has a numbered position (index) starting from 0:

```python
fruits = ["apple", "banana", "cherry", "date"]
#          0        1         2        3
#         -4       -3        -2       -1

print(fruits[0])    # apple   (first item)
print(fruits[2])    # cherry  (third item)
print(fruits[-1])   # date    (last item)
print(fruits[-2])   # cherry  (second to last)
```

### Real-Life Example: Student Roster

Imagine you are a teacher tracking your class:

```python
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")
print(f"Class size: {len(students)}")
```

### List Length

Use `len()` to find how many items are in a list, just like counting people in a line:

```python
tasks = ["email boss", "fix bug", "write tests", "code review"]
print(len(tasks))  # 4
```

### Checking Membership

Use the `in` operator to check if an item exists in a list -- like scanning a guest list at a party:

```python
vip_list = ["Alice", "Bob", "Charlie"]

print("Alice" in vip_list)    # True
print("Zara" in vip_list)     # False
print("Zara" not in vip_list) # True
```""",
                'exercise': {
                    'instructions': 'Create a list called `weekdays` containing "Monday" through "Friday". Print the first day, the last day, the total number of days, and whether "Wednesday" is in the list.',
                    'starter_code': '# Create the weekdays list\nweekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]\n\n# Print the first day\nprint(weekdays[0])\n\n# Print the last day\nprint(weekdays[-1])\n\n# Print the total number of days\nprint(len(weekdays))\n\n# Check if Wednesday is in the list\nprint("Wednesday" in weekdays)\n',
                    'expected_output': 'Monday\nFriday\n5\nTrue',
                    'hint': 'Use index [0] for the first item, [-1] for the last, len() for the count, and the "in" operator to check membership.',
                },
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange these code blocks in the correct order to create a list, add an item, and print the length:',
                    'code_blocks': [
                        'fruits = ["apple", "banana"]',
                        'fruits.append("cherry")',
                        'print(len(fruits))',
                    ],
                    'explanation': 'First we create the list with two items, then we use append() to add a third, and finally we print the length which is 3!',
                },
            },
            {
                'id': 'list-slicing-and-modification',
                'title': 'Slicing and Modifying Lists',
                'content': """## Slicing and Modifying Lists

### Slicing

Slicing works the same way as with strings. Think of slicing a loaf of bread -- you pick the start slice and end slice to take a portion:

```python
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

print(colors[1:4])    # ['orange', 'yellow', 'green']
print(colors[:3])     # ['red', 'orange', 'yellow']
print(colors[3:])     # ['green', 'blue', 'purple']
print(colors[::2])    # ['red', 'yellow', 'blue']   (every other)
print(colors[::-1])   # ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
```

### Modifying Items

Unlike strings, lists are **mutable** -- you can change their contents. Think of a whiteboard where you can erase and rewrite entries:

```python
# Change a single item
temperatures = [72, 75, 68, 71, 80]
temperatures[2] = 70   # fix the third reading
print(temperatures)    # [72, 75, 70, 71, 80]

# Change a slice
temperatures[1:3] = [74, 69]
print(temperatures)    # [72, 74, 69, 71, 80]
```

### Adding Items

```python
# append() - add one item to the end (like adding to the bottom of a to-do list)
tasks = ["email boss", "fix bug"]
tasks.append("write tests")
print(tasks)  # ['email boss', 'fix bug', 'write tests']

# insert() - add at a specific position (like cutting in line)
tasks.insert(1, "urgent meeting")
print(tasks)  # ['email boss', 'urgent meeting', 'fix bug', 'write tests']

# extend() - add multiple items (like merging two lists)
more_tasks = ["code review", "deploy"]
tasks.extend(more_tasks)
print(tasks)
# ['email boss', 'urgent meeting', 'fix bug', 'write tests', 'code review', 'deploy']
```

### Removing Items

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - removes the FIRST occurrence (like crossing off a name from a list)
fruits.remove("banana")
print(fruits)   # ['apple', 'cherry', 'banana', 'date']

# pop() - removes and returns an item by index (like drawing a card from a deck)
last = fruits.pop()        # removes last item
print(last)                # date
print(fruits)              # ['apple', 'cherry', 'banana']

second = fruits.pop(1)     # removes item at index 1
print(second)              # cherry
print(fruits)              # ['apple', 'banana']

# del - delete by index or slice
del fruits[0]
print(fruits)              # ['banana']
```""",
                'exercise': {
                    'instructions': 'Start with the list `inventory = ["sword", "shield", "potion", "map", "key"]`. Remove "map" using remove(), add "armor" to the end using append(), insert "bow" at index 2, and pop the last item (storing it in a variable called `removed`). Print the final inventory list and the removed item.',
                    'starter_code': '# Starting inventory\ninventory = ["sword", "shield", "potion", "map", "key"]\n\n# Remove "map"\ninventory.remove("map")\n\n# Add "armor" to the end\ninventory.append("armor")\n\n# Insert "bow" at index 2\ninventory.insert(2, "bow")\n\n# Pop the last item\nremoved = inventory.pop()\n\n# Print the results\nprint(inventory)\nprint(f"Removed: {removed}")\n',
                    'expected_output': "['sword', 'shield', 'bow', 'potion', 'key']\nRemoved: armor",
                    'hint': 'After removing "map": [sword, shield, potion, key]. After appending "armor": [sword, shield, potion, key, armor]. After inserting "bow" at index 2: [sword, shield, bow, potion, key, armor]. After popping last: [sword, shield, bow, potion, key] and removed is "armor".',
                },
            },
            {
                'id': 'list-methods-and-sorting',
                'title': 'List Methods and Sorting',
                'content': """## List Methods and Sorting

### Sorting

Sorting a list is like organizing books on a shelf -- alphabetically, by size, or by some other rule.

```python
# sort() - sorts the list IN PLACE (modifies the original)
numbers = [42, 8, 15, 23, 4, 16]
numbers.sort()
print(numbers)  # [4, 8, 15, 16, 23, 42]

# Reverse sort
numbers.sort(reverse=True)
print(numbers)  # [42, 23, 16, 15, 8, 4]

# sorted() - returns a NEW sorted list (original unchanged)
names = ["Charlie", "Alice", "Bob"]
ordered = sorted(names)
print(ordered)  # ['Alice', 'Bob', 'Charlie']
print(names)    # ['Charlie', 'Alice', 'Bob']  - unchanged
```

### Other Useful Methods

```python
scores = [85, 92, 78, 92, 95, 88, 92]

# count() - how many times a value appears
print(scores.count(92))    # 3

# index() - position of first occurrence
print(scores.index(92))    # 1

# reverse() - reverses the list in place
scores.reverse()
print(scores)  # [92, 88, 95, 92, 78, 92, 85]

# copy() - creates a shallow copy
backup = scores.copy()
```

### Useful Built-in Functions with Lists

```python
grades = [85, 92, 78, 95, 88]

print(min(grades))   # 78  - lowest grade
print(max(grades))   # 95  - highest grade
print(sum(grades))   # 438 - total of all grades

# Average
average = sum(grades) / len(grades)
print(average)        # 87.6
```

### Real-Life Example: Leaderboard

Imagine building a game leaderboard where you need to rank players by score:

```python
player_scores = [
    ("Alice", 2500),
    ("Bob", 3100),
    ("Charlie", 1800),
    ("Diana", 2900)
]

# Sort by score (second element), highest first
player_scores.sort(key=lambda x: x[1], reverse=True)

print("=== LEADERBOARD ===")
for rank, (name, score) in enumerate(player_scores, 1):
    print(f"  {rank}. {name}: {score}")
```""",
                'exercise': None,
            },
            {
                'id': 'tuples',
                'title': 'Tuples: Immutable Sequences',
                'content': """## Tuples: Immutable Sequences

A **tuple** is like a list, but it **cannot be changed** after creation. Think of a tuple as data written in permanent ink versus a list written in pencil.

### Why Tuples?

Tuples are perfect for data that should not change:

- **GPS coordinates** -- a location like (40.7128, -74.0060) should stay fixed.
- **RGB colors** -- red is always (255, 0, 0).
- **Database records** -- a row of data returned from a query.
- **Function return values** -- when a function returns multiple values, they come as a tuple.

### Creating Tuples

```python
# Using parentheses
coordinates = (40.7128, -74.0060)
rgb_red = (255, 0, 0)
person = ("Alice", 30, "Engineer")

# Single-item tuple needs a trailing comma
single = (42,)       # this is a tuple
not_tuple = (42)     # this is just the integer 42

# Tuple without parentheses (packing)
point = 3, 7
print(type(point))   # <class 'tuple'>
```

### Accessing Tuple Elements

Indexing and slicing work exactly like lists:

```python
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")

print(months[0])     # Jan
print(months[-1])    # Jun
print(months[1:4])   # ('Feb', 'Mar', 'Apr')
print(len(months))   # 6
```

### Tuples Are Immutable

```python
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # TypeError: 'tuple' object does not support item assignment
```

### Tuple Unpacking

Unpacking is one of the most useful features. It is like opening a package and placing each item in a labeled spot:

```python
# Unpack coordinates
latitude, longitude = (40.7128, -74.0060)
print(f"Lat: {latitude}, Long: {longitude}")

# Unpack in a loop
students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
for name, score in students:
    print(f"{name}: {score}")
```

### When to Use Tuples vs. Lists

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Yes | No |
| Use case | Data that changes | Data that stays fixed |
| Example | Shopping cart items | GPS coordinates |
| Can be dict key | No | Yes |""",
                'exercise': {
                    'instructions': 'Create a tuple called `rgb_blue` with values (0, 0, 255). Unpack it into three variables: `red`, `green`, `blue`. Print each component labeled. Then create a list of 3 color tuples and loop through them, printing each color name and its RGB values.',
                    'starter_code': '# Create and unpack an RGB tuple\nrgb_blue = (0, 0, 255)\nred, green, blue = rgb_blue\n\nprint(f"Red: {red}")\nprint(f"Green: {green}")\nprint(f"Blue: {blue}")\n\n# List of color tuples\ncolors = [\n    ("Red", (255, 0, 0)),\n    ("Green", (0, 128, 0)),\n    ("White", (255, 255, 255))\n]\n\nfor name, (r, g, b) in colors:\n    print(f"{name}: rgb({r}, {g}, {b})")\n',
                    'expected_output': 'Red: 0\nGreen: 0\nBlue: 255\nRed: rgb(255, 0, 0)\nGreen: rgb(0, 128, 0)\nWhite: rgb(255, 255, 255)',
                    'hint': 'Unpack the tuple with red, green, blue = rgb_blue. For the loop, use nested unpacking: for name, (r, g, b) in colors.',
                },
            },
        ],
    },
    {
        'title': 'Dictionaries',
        'description': 'Master Python dictionaries -- the key-value data structure that works like a phone book, letting you store and look up data by meaningful labels instead of positions.',
        'order': 2,
        'item_order': 3,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'introduction-to-dictionaries',
                'title': 'Introduction to Dictionaries',
                'content': """## Introduction to Dictionaries

A **dictionary** is a collection of **key-value pairs**. While a list is like a numbered row of lockers, a dictionary is like a **phone book** -- you look up information by a name (key), not by a position number.

### Creating Dictionaries

Use curly braces `{}` with `key: value` pairs:

```python
# A contact in a phone book
contact = {
    "name": "Alice Johnson",
    "phone": "555-0101",
    "email": "alice@example.com"
}

# A product in a store
product = {
    "name": "Wireless Mouse",
    "price": 29.99,
    "in_stock": True,
    "quantity": 150
}

# An empty dictionary
empty = {}
```

### Accessing Values

Use the key inside square brackets or the `.get()` method:

```python
student = {
    "name": "Bob",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.7
}

# Square bracket access
print(student["name"])    # Bob
print(student["gpa"])     # 3.7

# .get() method - returns None (or a default) if key not found
print(student.get("name"))         # Bob
print(student.get("phone"))        # None
print(student.get("phone", "N/A")) # N/A - custom default
```

The difference matters: `student["phone"]` would raise a **KeyError**, while `student.get("phone")` safely returns `None`.

### Real-Life Example: Movie Information

```python
movie = {
    "title": "The Matrix",
    "year": 1999,
    "director": "Wachowskis",
    "genres": ["Sci-Fi", "Action"],
    "rating": 8.7
}

print(f"{movie['title']} ({movie['year']})")
print(f"Director: {movie['director']}")
print(f"Rating: {movie['rating']}/10")
```

### Dictionary Length and Membership

```python
settings = {"theme": "dark", "font_size": 14, "language": "en"}

print(len(settings))            # 3
print("theme" in settings)      # True  - checks KEYS, not values
print("dark" in settings)       # False - "dark" is a value, not a key
```""",
                'exercise': {
                    'instructions': 'Create a dictionary called `book` with keys "title" (value "Python Crash Course"), "author" (value "Eric Matthes"), "year" (value 2019), and "pages" (value 544). Print the title, author, and whether the key "isbn" exists in the dictionary. Use .get() to print the isbn with a default of "Not Available".',
                    'starter_code': '# Create the book dictionary\nbook = {\n    "title": "Python Crash Course",\n    "author": "Eric Matthes",\n    "year": 2019,\n    "pages": 544\n}\n\n# Print title and author\nprint(f"Title: {book[\'title\']}")\nprint(f"Author: {book[\'author\']}")\n\n# Check if "isbn" key exists\nprint(f"Has ISBN: {\'isbn\' in book}")\n\n# Use .get() with a default value\nprint(f"ISBN: {book.get(\'isbn\', \'Not Available\')}")\n',
                    'expected_output': 'Title: Python Crash Course\nAuthor: Eric Matthes\nHas ISBN: False\nISBN: Not Available',
                    'hint': 'Use square brackets to access existing keys. Use the "in" operator to check key existence. Use .get(key, default) to safely access a key that might not exist.',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Look at this code and pick the correct answer:',
                    'code_snippet': 'settings = {"theme": "dark", "font_size": 14}\nprint("dark" in settings)',
                    'question': 'What will this code print?',
                    'options': [
                        {'text': 'False', 'correct': True},
                        {'text': 'True', 'correct': False},
                        {'text': 'Error', 'correct': False},
                        {'text': 'None', 'correct': False},
                    ],
                    'explanation': 'The "in" operator checks KEYS, not values! "dark" is a value in the dictionary, not a key. The keys are "theme" and "font_size".',
                },
            },
            {
                'id': 'modifying-dictionaries',
                'title': 'Adding, Updating, and Removing Entries',
                'content': """## Adding, Updating, and Removing Entries

Dictionaries are **mutable**, so you can freely add, change, and remove entries -- like updating a contact list on your phone.

### Adding and Updating

Assign a value to a key. If the key exists, the value is updated. If it doesn't, a new entry is created:

```python
profile = {"name": "Alice", "age": 25}

# Update an existing key
profile["age"] = 26
print(profile)  # {'name': 'Alice', 'age': 26}

# Add a new key
profile["city"] = "New York"
print(profile)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

### The `update()` Method

Merge another dictionary (or key-value pairs) into the current one -- like merging two contact cards for the same person:

```python
defaults = {"theme": "light", "font_size": 12, "language": "en"}
user_prefs = {"theme": "dark", "font_size": 16}

defaults.update(user_prefs)
print(defaults)
# {'theme': 'dark', 'font_size': 16, 'language': 'en'}
```

### Removing Entries

```python
inventory = {
    "apples": 50,
    "bananas": 30,
    "cherries": 100,
    "dates": 25
}

# pop() - removes and returns the value (like taking an item off a shelf)
banana_count = inventory.pop("bananas")
print(f"Removed {banana_count} bananas")   # Removed 30 bananas
print(inventory)
# {'apples': 50, 'cherries': 100, 'dates': 25}

# pop() with default - avoids KeyError if key missing
mango_count = inventory.pop("mangoes", 0)
print(f"Mangoes: {mango_count}")  # Mangoes: 0

# del - delete a key-value pair
del inventory["dates"]
print(inventory)  # {'apples': 50, 'cherries': 100}

# clear() - remove ALL entries
# inventory.clear()  # {}
```

### Real-Life Example: Inventory Management System

```python
warehouse = {}

# Receiving shipments
warehouse["laptop"] = 50
warehouse["mouse"] = 200
warehouse["keyboard"] = 150

# Selling items (reduce count)
warehouse["laptop"] -= 3
warehouse["mouse"] -= 10

# Check stock
for item, count in warehouse.items():
    status = "LOW" if count < 20 else "OK"
    print(f"  {item}: {count} [{status}]")
```""",
                'exercise': {
                    'instructions': 'Start with a dictionary `cart = {"apple": 3, "banana": 5, "milk": 1}`. Add "bread" with value 2. Update "apple" to 6. Remove "banana" using pop() and store the count. Print the final cart and the removed banana count.',
                    'starter_code': '# Starting shopping cart\ncart = {"apple": 3, "banana": 5, "milk": 1}\n\n# Add bread\ncart["bread"] = 2\n\n# Update apple count\ncart["apple"] = 6\n\n# Remove banana and store count\nbanana_count = cart.pop("banana")\n\n# Print results\nprint(cart)\nprint(f"Removed {banana_count} bananas")\n',
                    'expected_output': "{'apple': 6, 'milk': 1, 'bread': 2}\nRemoved 5 bananas",
                    'hint': 'Use cart["bread"] = 2 to add a new item. Use cart["apple"] = 6 to update. Use cart.pop("banana") to remove and capture the value.',
                },
            },
            {
                'id': 'iterating-over-dictionaries',
                'title': 'Iterating Over Dictionaries',
                'content': """## Iterating Over Dictionaries

Dictionaries provide three views for iteration, each useful in different situations -- like reading a phone book by names only, numbers only, or both.

### Iterating Over Keys

```python
student_grades = {"Alice": 92, "Bob": 85, "Charlie": 78}

# Default iteration gives keys
for name in student_grades:
    print(name)
# Alice
# Bob
# Charlie

# Explicit .keys() method
for name in student_grades.keys():
    print(name)
```

### Iterating Over Values

```python
# .values() - just the values
for grade in student_grades.values():
    print(grade)
# 92
# 85
# 78
```

### Iterating Over Key-Value Pairs

The `.items()` method returns pairs you can unpack -- this is the most common pattern:

```python
# .items() - both key and value
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
# Alice: 92
# Bob: 85
# Charlie: 78
```

### Real-Life Example: Student Grade Report

```python
grades = {
    "Alice": [90, 85, 92, 88],
    "Bob": [78, 82, 75, 80],
    "Charlie": [95, 98, 92, 97]
}

print("=== Grade Report ===")
for student, scores in grades.items():
    avg = sum(scores) / len(scores)
    print(f"{student}: avg = {avg:.1f}")
```

### Useful Dictionary Patterns

```python
# Building a word frequency counter
sentence = "the cat sat on the mat the cat"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
```""",
                'exercise': None,
            },
            {
                'id': 'nested-dictionaries',
                'title': 'Nested Dictionaries',
                'content': """## Nested Dictionaries

Real-world data is often layered. A school doesn't just have student names -- each student has grades, contact info, and enrollment data. **Nested dictionaries** let you model this hierarchy naturally.

### Creating Nested Dictionaries

```python
school = {
    "Alice": {
        "age": 20,
        "major": "Computer Science",
        "grades": {"math": 95, "english": 88, "science": 92}
    },
    "Bob": {
        "age": 22,
        "major": "Mathematics",
        "grades": {"math": 98, "english": 75, "science": 85}
    }
}
```

### Accessing Nested Data

Chain the keys together to drill down through layers:

```python
# Get Alice's age
print(school["Alice"]["age"])          # 20

# Get Bob's math grade
print(school["Bob"]["grades"]["math"]) # 98

# Safe access with .get()
eve_age = school.get("Eve", {}).get("age", "Unknown")
print(eve_age)  # Unknown
```

### Modifying Nested Data

```python
# Update Alice's English grade
school["Alice"]["grades"]["english"] = 91

# Add a new student
school["Charlie"] = {
    "age": 21,
    "major": "Physics",
    "grades": {"math": 88, "english": 82, "science": 94}
}
```

### Real-Life Example: Restaurant Menu

```python
menu = {
    "appetizers": {
        "soup": 5.99,
        "salad": 7.49,
        "bruschetta": 8.99
    },
    "main_courses": {
        "steak": 24.99,
        "salmon": 19.99,
        "pasta": 14.99
    },
    "desserts": {
        "cake": 6.99,
        "ice_cream": 4.99
    }
}

# Print the full menu
for category, items in menu.items():
    print(f"\\n--- {category.upper()} ---")
    for dish, price in items.items():
        print(f"  {dish}: ${price:.2f}")
```

### Practical Tip: When to Nest

- **1-2 levels** of nesting is common and readable.
- **3+ levels** can become hard to work with -- consider using classes or flattening the data.
- Always provide **safe access** with `.get()` to avoid crashes when keys might be missing.""",
                'exercise': {
                    'instructions': 'Create a nested dictionary called `employees` with two employees: "E001" maps to {"name": "Alice", "department": "Engineering", "salary": 85000} and "E002" maps to {"name": "Bob", "department": "Marketing", "salary": 72000}. Loop through and print each employee ID, name, and department. Then print the total salary budget.',
                    'starter_code': '# Create nested employee dictionary\nemployees = {\n    "E001": {"name": "Alice", "department": "Engineering", "salary": 85000},\n    "E002": {"name": "Bob", "department": "Marketing", "salary": 72000}\n}\n\n# Loop and print each employee\nfor emp_id, info in employees.items():\n    print(f"{emp_id}: {info[\'name\']} - {info[\'department\']}")\n\n# Calculate and print total salary\ntotal_salary = 0\nfor info in employees.values():\n    total_salary += info["salary"]\nprint(f"Total salary budget: ${total_salary}")\n',
                    'expected_output': 'E001: Alice - Engineering\nE002: Bob - Marketing\nTotal salary budget: $157000',
                    'hint': 'Use employees.items() to get both the ID and info dictionary. Access nested values with info["name"]. Sum salaries by looping through employees.values().',
                },
            },
        ],
    },
    {
        'title': 'Sets and Comprehensions',
        'description': 'Discover sets for managing unique collections and master comprehensions -- a concise, Pythonic way to create lists, dictionaries, and sets from existing data.',
        'order': 3,
        'item_order': 6,
        'estimated_time_minutes': 18,
        'sections': [
            {
                'id': 'introduction-to-sets',
                'title': 'Introduction to Sets',
                'content': """## Introduction to Sets

A **set** is an unordered collection of **unique items**. Think of a guest list where each name can appear only once -- even if someone RSVPs twice, they only get one spot.

### Creating Sets

```python
# Using curly braces
fruits = {"apple", "banana", "cherry"}

# From a list (duplicates removed automatically)
numbers = set([1, 2, 2, 3, 3, 3, 4])
print(numbers)  # {1, 2, 3, 4}

# Empty set (NOT {} -- that creates a dictionary!)
empty = set()
```

### Key Properties of Sets

1. **No duplicates** -- adding an existing item does nothing.
2. **Unordered** -- items have no index; you cannot do `my_set[0]`.
3. **Fast membership testing** -- checking `x in my_set` is much faster than `x in my_list` for large collections.

### Real-Life Example: Unique Website Visitors

Imagine tracking unique visitors to your website:

```python
visitors = set()

# Visitors log in throughout the day (some visit more than once)
visitors.add("alice@mail.com")
visitors.add("bob@mail.com")
visitors.add("alice@mail.com")   # duplicate -- ignored
visitors.add("charlie@mail.com")
visitors.add("bob@mail.com")     # duplicate -- ignored

print(f"Unique visitors: {len(visitors)}")  # 3
print(visitors)
# {'alice@mail.com', 'bob@mail.com', 'charlie@mail.com'}
```

### Adding and Removing

```python
tags = {"python", "coding", "tutorial"}

# Add a single item
tags.add("beginner")

# Add multiple items
tags.update(["tips", "python"])  # "python" already exists -- ignored
print(tags)

# Remove an item (raises KeyError if not found)
tags.remove("tutorial")

# discard() - remove without error if missing
tags.discard("nonexistent")   # no error

# pop() - remove and return an arbitrary item
removed = tags.pop()
print(f"Removed: {removed}")
```""",
                'exercise': {
                    'instructions': 'Create a list called `raw_emails` with these values: "alice@mail.com", "bob@mail.com", "alice@mail.com", "charlie@mail.com", "bob@mail.com", "diana@mail.com". Convert it to a set called `unique_emails`. Print the number of unique emails and whether "eve@mail.com" is in the set.',
                    'starter_code': '# Raw email list with duplicates\nraw_emails = [\n    "alice@mail.com", "bob@mail.com", "alice@mail.com",\n    "charlie@mail.com", "bob@mail.com", "diana@mail.com"\n]\n\n# Convert to a set to remove duplicates\nunique_emails = set(raw_emails)\n\n# Print the count of unique emails\nprint(f"Unique emails: {len(unique_emails)}")\n\n# Check membership\nprint(f"Eve signed up: {\'eve@mail.com\' in unique_emails}")\n',
                    'expected_output': 'Unique emails: 4\nEve signed up: False',
                    'hint': 'Use set() to convert a list to a set, which automatically removes duplicates. Use len() for the count and "in" to check membership.',
                },
            },
            {
                'id': 'set-operations',
                'title': 'Set Operations',
                'content': """## Set Operations

Sets support mathematical operations that are incredibly useful for comparing groups of data. Think of Venn diagrams from math class -- sets let you compute unions, intersections, and differences directly.

### Union -- Combine All Items

The union of two sets includes every item from both (no duplicates). Like merging two departments' employee lists:

```python
frontend_team = {"Alice", "Bob", "Charlie"}
backend_team = {"Charlie", "Diana", "Eve"}

# All team members (union)
all_members = frontend_team | backend_team
# OR: all_members = frontend_team.union(backend_team)
print(all_members)  # {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
```

### Intersection -- Common Items

Items that appear in both sets. Like finding friends you and your buddy have in common:

```python
my_friends = {"Alice", "Bob", "Charlie", "Diana"}
your_friends = {"Charlie", "Diana", "Eve", "Frank"}

common_friends = my_friends & your_friends
# OR: common_friends = my_friends.intersection(your_friends)
print(common_friends)  # {'Charlie', 'Diana'}
```

### Difference -- Items in One but Not the Other

```python
all_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
passed_exam = {"Alice", "Charlie", "Eve"}

# Students who did NOT pass
failed = all_students - passed_exam
# OR: failed = all_students.difference(passed_exam)
print(failed)  # {'Bob', 'Diana'}
```

### Symmetric Difference -- Items in Either but Not Both

```python
group_a = {"Alice", "Bob", "Charlie"}
group_b = {"Bob", "Diana", "Eve"}

# Members exclusive to one group
exclusive = group_a ^ group_b
print(exclusive)  # {'Alice', 'Charlie', 'Diana', 'Eve'}
```

### Subset and Superset

```python
required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "Docker", "AWS"}

# Is required a subset of candidate?
print(required_skills <= candidate_skills)  # True - candidate has all required skills

# Is candidate a superset of required?
print(candidate_skills >= required_skills)  # True
```

### Real-Life Example: Course Enrollment Analysis

```python
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Diana", "Eve", "Frank"}
art_students = {"Charlie", "Eve", "Grace"}

# Students taking both math AND science
both = math_students & science_students
print(f"Math and Science: {both}")

# Students in math but not science
math_only = math_students - science_students
print(f"Math only: {math_only}")

# All unique students across all courses
all_students = math_students | science_students | art_students
print(f"Total unique students: {len(all_students)}")
```""",
                'exercise': None,
            },
            {
                'id': 'list-comprehensions',
                'title': 'List Comprehensions',
                'content': """## List Comprehensions

A **list comprehension** is a concise way to create a new list by transforming or filtering an existing one. Think of it as an assembly line: raw materials go in, and finished products come out in one smooth operation.

### Basic Syntax

```python
new_list = [expression for item in iterable]
```

This is equivalent to:

```python
new_list = []
for item in iterable:
    new_list.append(expression)
```

### Examples

```python
# Squares of numbers 1-5
squares = [n ** 2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Uppercase names
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Prices with tax
prices = [10.00, 25.50, 8.99, 42.00]
with_tax = [round(p * 1.08, 2) for p in prices]
print(with_tax)  # [10.8, 27.54, 9.71, 45.36]
```

### Adding a Condition (Filter)

```python
new_list = [expression for item in iterable if condition]
```

This filters items before including them -- like a quality control step on the assembly line:

```python
# Only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Words longer than 3 characters
words = ["hi", "hello", "hey", "greetings", "yo"]
long_words = [w for w in words if len(w) > 3]
print(long_words)  # ['hello', 'greetings']
```

### Real-Life Example: Data Filtering

Imagine you are building a store app and need to filter products:

```python
products = [
    {"name": "Laptop", "price": 999, "in_stock": True},
    {"name": "Phone", "price": 699, "in_stock": False},
    {"name": "Tablet", "price": 449, "in_stock": True},
    {"name": "Monitor", "price": 299, "in_stock": True},
]

# Names of in-stock products under $500
affordable = [
    p["name"] for p in products
    if p["in_stock"] and p["price"] < 500
]
print(affordable)  # ['Tablet', 'Monitor']
```

### When to Use Comprehensions

- **Use them** for simple transformations and filters (1-2 operations).
- **Avoid them** when the logic is complex -- a regular `for` loop is more readable.

```python
# Good - simple and clear
squares = [n ** 2 for n in range(10)]

# Bad - too complex, use a regular loop instead
# result = [x.strip().lower() for x in data if x and len(x.strip()) > 3 and x[0] != '#']
```""",
                'exercise': {
                    'instructions': 'Use list comprehensions to: (1) create a list of squares of numbers from 1 to 8, (2) create a list of only the even numbers from 1 to 15, and (3) create a list of the lengths of the given words. Print each resulting list.',
                    'starter_code': '# 1. Squares of 1 through 8\nsquares = [n ** 2 for n in range(1, 9)]\nprint(squares)\n\n# 2. Even numbers from 1 to 15\nevens = [n for n in range(1, 16) if n % 2 == 0]\nprint(evens)\n\n# 3. Lengths of words\nwords = ["Python", "is", "absolutely", "wonderful"]\nlengths = [len(w) for w in words]\nprint(lengths)\n',
                    'expected_output': '[1, 4, 9, 16, 25, 36, 49, 64]\n[2, 4, 6, 8, 10, 12, 14]\n[6, 2, 10, 9]',
                    'hint': 'Use [expression for item in range()] syntax. Add an if clause to filter. Use len(word) to get the length of each word.',
                },
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this list comprehension will print? Type your guess!',
                    'code_snippet': 'numbers = [1, 2, 3, 4, 5, 6]\nresult = [n * 2 for n in numbers if n > 3]\nprint(result)',
                    'expected_output': '[8, 10, 12]',
                    'explanation': 'The comprehension first filters numbers greater than 3 (keeping 4, 5, 6), then multiplies each by 2. So we get [8, 10, 12]!',
                },
            },
            {
                'id': 'dict-and-set-comprehensions',
                'title': 'Dictionary and Set Comprehensions',
                'content': """## Dictionary and Set Comprehensions

The comprehension pattern extends beyond lists. You can also build dictionaries and sets in one concise expression.

### Dictionary Comprehensions

```python
{key_expr: value_expr for item in iterable}
```

#### Examples

```python
# Square mapping: {1: 1, 2: 4, 3: 9, ...}
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Word lengths
words = ["hello", "world", "python"]
word_lengths = {w: len(w) for w in words}
print(word_lengths)  # {'hello': 5, 'world': 5, 'python': 6}
```

### Real-Life Example: Price Conversion

Converting prices from dollars to euros for an international store:

```python
usd_prices = {"laptop": 999, "phone": 699, "tablet": 449}
exchange_rate = 0.92

eur_prices = {item: round(price * exchange_rate, 2) for item, price in usd_prices.items()}
print(eur_prices)
# {'laptop': 919.08, 'phone': 643.08, 'tablet': 413.08}
```

### Filtering with Dictionary Comprehensions

```python
scores = {"Alice": 92, "Bob": 65, "Charlie": 78, "Diana": 88, "Eve": 55}

# Only passing students (70+)
passing = {name: score for name, score in scores.items() if score >= 70}
print(passing)  # {'Alice': 92, 'Charlie': 78, 'Diana': 88}
```

### Set Comprehensions

Same syntax as dict comprehensions but without the colon:

```python
{expression for item in iterable}
```

```python
# Unique first letters from a list of names
names = ["Alice", "Anna", "Bob", "Bella", "Charlie"]
first_letters = {name[0] for name in names}
print(first_letters)  # {'A', 'B', 'C'}

# Unique word lengths in a sentence
sentence = "the quick brown fox jumps over the lazy dog"
unique_lengths = {len(word) for word in sentence.split()}
print(sorted(unique_lengths))  # [3, 4, 5]
```

### Real-Life Example: Unique Categories from Products

```python
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Pants", "category": "Clothing"},
    {"name": "Blender", "category": "Kitchen"},
]

categories = {p["category"] for p in products}
print(f"We sell: {sorted(categories)}")
# We sell: ['Clothing', 'Electronics', 'Kitchen']
```

### Summary: Choosing the Right Data Structure

| Structure | Ordered | Mutable | Duplicates | Access By |
|-----------|---------|---------|------------|-----------|
| List | Yes | Yes | Yes | Index |
| Tuple | Yes | No | Yes | Index |
| Dictionary | Insertion order | Yes | Keys: No, Values: Yes | Key |
| Set | No | Yes | No | N/A |""",
                'exercise': {
                    'instructions': 'Use comprehensions to: (1) create a dictionary mapping each number from 1 to 5 to its cube (n**3), (2) create a filtered dictionary from the given `scores` dict keeping only scores above 80, and (3) create a set of unique first characters from the given `cities` list. Print each result.',
                    'starter_code': '# 1. Number to cube mapping\ncubes = {n: n ** 3 for n in range(1, 6)}\nprint(cubes)\n\n# 2. Filter scores above 80\nscores = {"Alice": 92, "Bob": 67, "Charlie": 85, "Diana": 73, "Eve": 95}\nhigh_scores = {name: score for name, score in scores.items() if score > 80}\nprint(high_scores)\n\n# 3. Unique first characters from cities\ncities = ["Paris", "London", "Prague", "Lima", "Berlin", "Barcelona"]\nfirst_chars = {city[0] for city in cities}\nprint(sorted(first_chars))\n',
                    'expected_output': "{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}\n{'Alice': 92, 'Charlie': 85, 'Eve': 95}\n['B', 'L', 'P']",
                    'hint': 'For dict comprehension use {key: value for ...}. Add "if condition" to filter. For set comprehension use {expression for ...}. Use sorted() to print the set in alphabetical order.',
                },
            },
        ],
    },
]
