CHAPTER_ORDER = 6

LESSONS = [
    {
        'title': 'Reading Files in Python',
        'description': 'Learn how to open and read files using Python, including different read modes and techniques for processing text data line by line.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'why-file-io-matters',
                'title': 'Why File I/O Matters',
                'diagram': {
                    'id': 'ch6-file-io-flow',
                    'title': 'File I/O: Reading & Writing Files',
                    'file': 'diagrams/ch6-file-io-flow.svg',
                    'data_file': 'diagrams/excalidraw-data/ch6-file-io-flow.json',
                },
                'content': """## Why File I/O Matters

Almost every real-world program needs to read data from files or write data to them. Consider these everyday scenarios:

- A **weather app** reads temperature data from CSV files collected by sensors.
- A **web server** reads log files to track errors and usage patterns.
- A **payroll system** reads employee records from a file to calculate salaries.
- A **game** reads a saved progress file so players can continue where they left off.

File I/O (Input/Output) is how your program communicates with the file system. Python makes this remarkably straightforward with built-in functions that handle the low-level details for you.

### The Basic Concept

Working with files always follows a three-step pattern:

1. **Open** the file - establish a connection to the file on disk.
2. **Read or Write** - perform the operation you need.
3. **Close** the file - release the connection so other programs can use it.

```python
# The basic pattern
file = open("data.txt", "r")   # Step 1: Open for reading
content = file.read()           # Step 2: Read the content
file.close()                    # Step 3: Close the file
```

### File Modes

When you open a file, you specify a **mode** that tells Python what you intend to do:

| Mode | Description                        |
|------|------------------------------------|
| `"r"` | Read (default) - file must exist  |
| `"w"` | Write - creates or overwrites     |
| `"a"` | Append - adds to the end          |
| `"x"` | Create - fails if file exists     |
| `"rb"` | Read binary (images, PDFs)       |
| `"wb"` | Write binary                     |

For this lesson, we will focus on reading with `"r"` mode.""",
                'exercise': None,
            },
            {
                'id': 'reading-with-stringio',
                'title': 'Simulating File Reading with io.StringIO',
                'content': """## Simulating File Reading with io.StringIO

Before we dive into reading real files, let us learn a powerful trick. Python's `io.StringIO` class lets you create an **in-memory file object** from a string. It behaves exactly like a file opened for reading, which makes it perfect for practicing and testing file operations without needing actual files on disk.

Think of `io.StringIO` as creating a virtual file that lives in your program's memory:

```python
import io

# Create a virtual file from a string
virtual_file = io.StringIO("Hello, World!\\nThis is line 2.\\nThis is line 3.")

# Read the entire content - just like reading a real file
content = virtual_file.read()
print(content)
```

### Real-Life Analogy

Imagine you are a librarian. A real file is like a book on a shelf - you walk over, pick it up, and read it. `StringIO` is like someone reading the book aloud to you - the content is the same, but it comes from a different source. Your reading skills work the same way regardless.

### The Three Read Methods

Python provides three ways to read from a file (or StringIO):

**1. `read()` - Read everything at once**

```python
import io

# Simulating a server log file
log_data = io.StringIO("2024-01-15 ERROR: Connection timeout\\n2024-01-15 INFO: Server restarted\\n2024-01-15 INFO: All systems normal")

all_text = log_data.read()
print(all_text)
```

**2. `readline()` - Read one line at a time**

```python
import io

sensor_data = io.StringIO("Temperature: 72.5\\nHumidity: 45.2\\nPressure: 1013.25")

first_line = sensor_data.readline()
print(first_line.strip())  # Temperature: 72.5

second_line = sensor_data.readline()
print(second_line.strip())  # Humidity: 45.2
```

**3. `readlines()` - Read all lines into a list**

```python
import io

grocery_file = io.StringIO("Milk\\nEggs\\nBread\\nButter")

items = grocery_file.readlines()
print(items)  # ['Milk\\n', 'Eggs\\n', 'Bread\\n', 'Butter']
```

Notice that `readlines()` keeps the newline characters (`\\n`). You typically use `.strip()` to remove them.""",
                'exercise': {
                    'instructions': 'Use io.StringIO to simulate reading a file containing student grades. Create a StringIO object with three lines of grade data, then use readlines() to get all lines as a list. Loop through the list and print each line stripped of whitespace.',
                    'starter_code': 'import io\n\n# Simulate a grades file with three student records\ngrades_file = io.StringIO("Alice: 92\\nBob: 85\\nCharlie: 78")\n\n# Read all lines into a list\nlines = grades_file.readlines()\n\n# Loop through and print each line (stripped)\nfor line in lines:\n    print(line.strip())\n',
                    'expected_output': 'Alice: 92\nBob: 85\nCharlie: 78',
                    'hint': 'The readlines() method returns a list of strings. Use a for loop with .strip() on each line to remove trailing newline characters.',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Look at this code and pick the correct answer:',
                    'code_snippet': 'import io\nf = io.StringIO("Line 1\\nLine 2\\nLine 3")\nresult = f.readline()\nprint(result.strip())',
                    'question': 'What will this code print?',
                    'options': [
                        {'text': 'Line 1', 'correct': True},
                        {'text': 'Line 1\\nLine 2\\nLine 3', 'correct': False},
                        {'text': "['Line 1\\n', 'Line 2\\n', 'Line 3']", 'correct': False},
                        {'text': 'Line 3', 'correct': False},
                    ],
                    'explanation': 'readline() reads only ONE line at a time! It returns the first line "Line 1\\n", and .strip() removes the newline character, leaving just "Line 1".',
                },
            },
            {
                'id': 'iterating-over-files',
                'title': 'Iterating Over File Lines',
                'content': """## Iterating Over File Lines

One of the most common patterns in file processing is reading a file **line by line**. This is especially important for large files because it does not load the entire file into memory at once.

### The `for` Loop Approach

File objects (and StringIO objects) are **iterable**, meaning you can loop over them directly:

```python
import io

# Simulating a sales report file
sales_file = io.StringIO("Monday: $1200\\nTuesday: $980\\nWednesday: $1550\\nThursday: $1100\\nFriday: $2100")

for line in sales_file:
    print(line.strip())
```

This is the **recommended approach** for reading files line by line because:
- It is memory-efficient (only one line is in memory at a time).
- It is clean and Pythonic.
- It works with files of any size.

### Real-Life Example: Processing CSV Data

CSV (Comma-Separated Values) files are everywhere in business. Here is how you might process one:

```python
import io

# Simulating an employee CSV file
csv_data = io.StringIO("Name,Department,Salary\\nAlice,Engineering,95000\\nBob,Marketing,78000\\nCharlie,Sales,82000")

header = csv_data.readline().strip()  # Read the header line first
print(f"Columns: {header}")

for line in csv_data:
    fields = line.strip().split(",")
    name, dept, salary = fields
    print(f"{name} works in {dept} and earns ${salary}")
```

### Real-Life Example: Counting Words in a Document

```python
import io

document = io.StringIO("Python is a great language\\nIt is easy to learn\\nMany companies use Python")

total_words = 0
for line in document:
    words = line.strip().split()
    total_words += len(words)

print(f"Total words: {total_words}")
```

### Resetting the File Position

After reading a file or StringIO object, the reading position moves to the end. To read it again, use `seek(0)` to go back to the beginning:

```python
import io

data = io.StringIO("Line 1\\nLine 2")
content = data.read()
print(content)

# Position is now at the end; reading again gives empty string
print(data.read())  # prints nothing

# Reset to beginning
data.seek(0)
print(data.read())  # prints content again
```""",
                'exercise': {
                    'instructions': 'Simulate processing a CSV inventory file. Read the header line separately, then iterate through the remaining lines. For each item, split by comma, extract the product name and quantity, and print a formatted message. Finally, print the total number of items in stock.',
                    'starter_code': 'import io\n\n# Simulating an inventory CSV file\ninventory_file = io.StringIO("Product,Quantity,Price\\nLaptop,50,999.99\\nMouse,200,29.99\\nKeyboard,150,79.99")\n\n# Read and skip the header line\nheader = inventory_file.readline()\n\n# Track total quantity\ntotal_quantity = 0\n\n# Process each line\nfor line in inventory_file:\n    fields = line.strip().split(",")\n    product = fields[0]\n    quantity = int(fields[1])\n    total_quantity += quantity\n    print(f"{product}: {quantity} units")\n\nprint(f"Total items in stock: {total_quantity}")\n',
                    'expected_output': 'Laptop: 50 units\nMouse: 200 units\nKeyboard: 150 units\nTotal items in stock: 400',
                    'hint': 'Use readline() to skip the header. Then use a for loop to iterate over the remaining lines. Split each line by comma and convert the quantity to an integer with int().',
                },
            },
            {
                'id': 'the-with-statement',
                'title': 'The with Statement (Context Manager)',
                'content': """## The `with` Statement (Context Manager)

When working with real files, forgetting to close a file can lead to problems: data corruption, memory leaks, or other programs being unable to access the file. Python's `with` statement solves this elegantly.

### The Problem with Manual Closing

```python
# Risky approach - what if an error occurs before close()?
file = open("data.txt", "r")
content = file.read()
# If an error occurs here, file.close() never runs!
file.close()
```

### The `with` Statement Solution

The `with` statement automatically closes the file when the block ends, even if an error occurs:

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here - no need to call close()
```

Think of it like a hotel room: when you check in (enter the `with` block), you get the key (the file handle). When you check out (leave the block), the key is returned automatically. You never have to worry about forgetting to return it.

### How It Works with StringIO

The `with` statement also works with StringIO:

```python
import io

with io.StringIO("Hello from a virtual file!") as f:
    content = f.read()
    print(content)
# StringIO is properly closed here
```

### Real-Life Example: Reading a Configuration File

Applications often store settings in configuration files:

```python
import io

# Simulating a config file
config_text = "username=admin\\nhost=localhost\\nport=8080\\ndebug=true"

settings = {}
with io.StringIO(config_text) as config_file:
    for line in config_file:
        key, value = line.strip().split("=")
        settings[key] = value

print(f"Server: {settings['host']}:{settings['port']}")
print(f"User: {settings['username']}")
print(f"Debug mode: {settings['debug']}")
```

### Best Practice

**Always use the `with` statement** when working with files. It is the standard in professional Python code:

```python
# GOOD - always use with
with open("report.txt", "r") as f:
    data = f.read()

# AVOID - manual open/close
f = open("report.txt", "r")
data = f.read()
f.close()
```""",
                'exercise': {
                    'instructions': 'Use a with statement with io.StringIO to simulate reading a configuration file. Parse each line into key-value pairs, store them in a dictionary, and then print the application name, version, and author from the config.',
                    'starter_code': 'import io\n\n# Simulating an app configuration file\nconfig_data = "app_name=WeatherTracker\\nversion=2.5\\nauthor=Jane Smith\\nlanguage=Python"\n\n# Parse config into a dictionary using with statement\nconfig = {}\nwith io.StringIO(config_data) as config_file:\n    for line in config_file:\n        key, value = line.strip().split("=")\n        config[key] = value\n\n# Print the configuration values\nprint(f"Application: {config[\'app_name\']}")\nprint(f"Version: {config[\'version\']}")\nprint(f"Author: {config[\'author\']}")\n',
                    'expected_output': 'Application: WeatherTracker\nVersion: 2.5\nAuthor: Jane Smith',
                    'hint': 'Use io.StringIO inside a with statement. Split each line by "=" to separate the key and value, then store them in a dictionary.',
                },
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange these code blocks in the correct order to read a file safely using a with statement:',
                    'code_blocks': [
                        'import io',
                        'with io.StringIO("Hello World") as f:',
                        '    content = f.read()',
                        'print(content)',
                    ],
                    'explanation': 'First we import io, then open the file with a "with" statement (which closes it automatically), read inside the block, and print after!',
                },
            },
            {
                'id': 'practical-file-reading-patterns',
                'title': 'Practical File Reading Patterns',
                'content': """## Practical File Reading Patterns

Let us look at common real-world patterns for reading and processing data from files. These patterns come up again and again in professional Python development.

### Pattern 1: Filtering Lines

Often you only want lines that match a certain condition, like filtering error messages from a log file:

```python
import io

# Simulating a server log
log = io.StringIO("INFO: User logged in\\nERROR: Database timeout\\nINFO: Page loaded\\nERROR: File not found\\nINFO: User logged out")

errors = []
with io.StringIO(log.read()) as f:
    for line in f:
        if line.strip().startswith("ERROR"):
            errors.append(line.strip())

for error in errors:
    print(error)
```

### Pattern 2: Accumulating Data

Reading numeric data and computing statistics, like a fitness tracker reading daily step counts:

```python
import io

step_data = io.StringIO("8500\\n12000\\n6700\\n9200\\n11500")

steps = []
for line in step_data:
    steps.append(int(line.strip()))

print(f"Total steps: {sum(steps)}")
print(f"Average: {sum(steps) // len(steps)}")
print(f"Best day: {max(steps)}")
```

### Pattern 3: Building Structured Data

Parsing tabular data into a list of dictionaries - a very common pattern for data processing:

```python
import io

csv_text = "title,genre,rating\\nInception,Sci-Fi,8.8\\nThe Matrix,Sci-Fi,8.7\\nAmelie,Romance,8.3"
csv_file = io.StringIO(csv_text)

headers = csv_file.readline().strip().split(",")
movies = []

for line in csv_file:
    values = line.strip().split(",")
    movie = dict(zip(headers, values))
    movies.append(movie)

for movie in movies:
    print(f"{movie['title']} ({movie['genre']}) - {movie['rating']}/10")
```

### Pattern 4: Multi-File Processing Concept

In real applications, you might read from multiple files. Here is the concept demonstrated with StringIO:

```python
import io

# Simulating reading sales data from different quarters
q1 = io.StringIO("15000\\n18000\\n22000")
q2 = io.StringIO("19000\\n21000\\n25000")

yearly_sales = []
for quarter_file in [q1, q2]:
    for line in quarter_file:
        yearly_sales.append(int(line.strip()))

print(f"Total yearly sales: ${sum(yearly_sales):,}")
print(f"Number of months: {len(yearly_sales)}")
```

### Summary of Read Methods

| Method          | Returns           | Best For                      |
|-----------------|-------------------|-------------------------------|
| `read()`        | Entire content    | Small files, full text needed |
| `readline()`    | One line          | Processing header separately  |
| `readlines()`   | List of lines     | When you need a list          |
| `for line in f` | One line per loop | Large files, line-by-line     |""",
                'exercise': None,
            },
        ],
    },
    {
        'title': 'Writing Files and Context Managers',
        'description': 'Learn how to write data to files, append content, and use context managers effectively for robust file operations.',
        'order': 2,
        'item_order': 4,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'writing-basics',
                'title': 'Writing Data with io.StringIO',
                'content': """## Writing Data with io.StringIO

Just as we used `io.StringIO` to simulate reading files, we can use it to simulate **writing** to files. This lets us practice write operations and verify what would be written, all without touching the file system.

### Real Files vs. StringIO for Writing

When writing to a real file, you would use:

```python
# Real file writing (for reference)
with open("report.txt", "w") as f:
    f.write("Sales Report 2024\\n")
    f.write("Total Revenue: $150,000\\n")
```

With StringIO, we capture the written content in memory:

```python
import io

# Create a writable in-memory file
output = io.StringIO()

# Write to it just like a real file
output.write("Sales Report 2024\\n")
output.write("Total Revenue: $150,000\\n")

# Retrieve what was written
result = output.getvalue()
print(result)
```

### The `write()` Method

The `write()` method writes a string to the file. Unlike `print()`, it does **not** automatically add a newline:

```python
import io

report = io.StringIO()
report.write("Line 1")
report.write("Line 2")  # This will be on the SAME line!
print(report.getvalue())  # Line 1Line 2

# You must add newlines explicitly
report2 = io.StringIO()
report2.write("Line 1\\n")
report2.write("Line 2\\n")
print(report2.getvalue())
```

### The `writelines()` Method

`writelines()` writes a list of strings (also without adding newlines):

```python
import io

output = io.StringIO()
lines = ["First line\\n", "Second line\\n", "Third line\\n"]
output.writelines(lines)

print(output.getvalue())
```

### Real-Life Analogy

Think of writing to a file like writing in a notebook:
- `write()` is like writing with your pen - the pen stays where it left off, and you must manually move to the next line.
- `writelines()` is like copying a list of notes into your notebook one after another.
- `getvalue()` is like reading back everything you wrote.""",
                'exercise': {
                    'instructions': 'Use io.StringIO to simulate creating a simple report. Write a title line, a separator line of dashes, and three lines of data. Then use getvalue() to retrieve and print the complete report.',
                    'starter_code': 'import io\n\n# Create an in-memory file for our report\nreport = io.StringIO()\n\n# Write the report header\nreport.write("Monthly Sales Report\\n")\nreport.write("-" * 25 + "\\n")\n\n# Write sales data\nreport.write("Week 1: $12,500\\n")\nreport.write("Week 2: $15,300\\n")\nreport.write("Week 3: $11,800\\n")\n\n# Retrieve and print the full report\nprint(report.getvalue())\n',
                    'expected_output': 'Monthly Sales Report\n-------------------------\nWeek 1: $12,500\nWeek 2: $15,300\nWeek 3: $11,800\n',
                    'hint': 'Use the write() method on the StringIO object. Remember to add "\\n" at the end of each line. Use getvalue() to retrieve everything that was written.',
                },
                'game': {
                    'type': 'fill_blank',
                    'instructions': 'Fill in the blanks to write text to a StringIO object and read it back:',
                    'code_template': 'import io\noutput = io.{0}()\noutput.{1}("Hello!\\n")\nprint(output.{2}())',
                    'blanks': [
                        {'id': 0, 'answer': 'StringIO', 'hint': 'What class creates an in-memory file?'},
                        {'id': 1, 'answer': 'write', 'hint': 'What method sends text to a file?'},
                        {'id': 2, 'answer': 'getvalue', 'hint': 'What method reads back everything written?'},
                    ],
                    'explanation': 'io.StringIO() creates an in-memory file, .write() adds text to it, and .getvalue() retrieves all the text that was written!',
                },
            },
            {
                'id': 'write-modes-explained',
                'title': 'Write Modes: Write vs. Append',
                'content': """## Write Modes: Write vs. Append

When working with real files, the mode you choose determines how Python handles existing content.

### Write Mode (`"w"`) - Overwrite

Write mode creates a new file or **completely replaces** existing content:

```python
# First write creates the file
with open("notes.txt", "w") as f:
    f.write("Original content\\n")

# Second write REPLACES everything
with open("notes.txt", "w") as f:
    f.write("New content\\n")
# notes.txt now contains ONLY "New content"
```

Think of write mode like erasing a whiteboard before writing. Everything that was there before is gone.

### Append Mode (`"a"`) - Add to End

Append mode adds new content **after** existing content:

```python
# Creates the file with initial content
with open("log.txt", "w") as f:
    f.write("Application started\\n")

# Append adds to the end without erasing
with open("log.txt", "a") as f:
    f.write("User logged in\\n")
    f.write("Data processed\\n")
# log.txt now has all three lines
```

Think of append mode like adding entries to a diary - you never erase previous entries, you just keep writing on the next empty page.

### Demonstrating the Difference with StringIO

We can illustrate the concept of overwriting vs. appending:

```python
import io

# Simulating "write mode" - start fresh each time
output = io.StringIO()
output.write("First batch of data\\n")

# To simulate "overwrite", we create a new StringIO
output = io.StringIO()  # old content is gone
output.write("Second batch of data\\n")
print("After overwrite:")
print(output.getvalue())

# Simulating "append mode" - keep adding
log = io.StringIO()
log.write("Event 1: Server started\\n")
log.write("Event 2: User connected\\n")  # appending
log.write("Event 3: Data saved\\n")       # appending
print("After appending:")
print(log.getvalue())
```

### Real-Life Use Cases

| Mode | Use Case                                              |
|------|-------------------------------------------------------|
| `"w"` | Generating a fresh report every time the program runs |
| `"a"` | Adding entries to a log file throughout the day       |
| `"w"` | Saving user preferences (overwrite old settings)      |
| `"a"` | Recording transactions in a ledger                    |""",
                'exercise': None,
            },
            {
                'id': 'building-reports',
                'title': 'Building Reports from Data',
                'content': """## Building Reports from Data

One of the most common real-world uses of file writing is generating reports. Let us build a complete report from structured data.

### Real-Life Example: Generating an Invoice

Imagine you run an online store and need to create invoice summaries:

```python
import io

# Order data
items = [
    ("Widget A", 3, 12.99),
    ("Gadget B", 1, 45.50),
    ("Tool C", 2, 8.75),
]
customer = "Acme Corporation"

# Build the invoice in memory
invoice = io.StringIO()
invoice.write(f"INVOICE - {customer}\\n")
invoice.write("=" * 40 + "\\n")

total = 0
for name, qty, price in items:
    line_total = qty * price
    total += line_total
    invoice.write(f"  {name:15s}  {qty:3d} x ${price:6.2f} = ${line_total:8.2f}\\n")

invoice.write("-" * 40 + "\\n")
invoice.write(f"  {'TOTAL':15s}{'':14s}${total:8.2f}\\n")

print(invoice.getvalue())
```

### Real-Life Example: Student Grade Report

A teacher generating a summary of student performance:

```python
import io

students = [
    ("Alice", [92, 88, 95, 90]),
    ("Bob", [78, 82, 75, 80]),
    ("Charlie", [95, 98, 92, 97]),
]

report = io.StringIO()
report.write("CLASS PERFORMANCE REPORT\\n")
report.write("-" * 35 + "\\n")

class_total = 0
for name, grades in students:
    avg = sum(grades) / len(grades)
    class_total += avg
    status = "Pass" if avg >= 80 else "Needs Improvement"
    report.write(f"{name:10s} | Avg: {avg:5.1f} | {status}\\n")

class_avg = class_total / len(students)
report.write("-" * 35 + "\\n")
report.write(f"Class Average: {class_avg:.1f}\\n")

print(report.getvalue())
```

### Combining Reading and Writing

In real applications, you often read data from one source and write processed results to another:

```python
import io

# Read raw data
raw_data = io.StringIO("apple,3,1.50\\nbanana,5,0.75\\norange,2,2.00")

# Process and write to a report
report = io.StringIO()
report.write("Grocery Receipt\\n")
report.write("-" * 30 + "\\n")

grand_total = 0
for line in raw_data:
    item, qty, price = line.strip().split(",")
    qty = int(qty)
    price = float(price)
    subtotal = qty * price
    grand_total += subtotal
    report.write(f"{item}: {qty} x ${price:.2f} = ${subtotal:.2f}\\n")

report.write("-" * 30 + "\\n")
report.write(f"Grand Total: ${grand_total:.2f}\\n")

print(report.getvalue())
```""",
                'exercise': {
                    'instructions': 'Build a temperature report. Read temperature data from a StringIO source, then write a formatted report to another StringIO. The report should list each city with its temperature, then show the hottest city and the average temperature.',
                    'starter_code': 'import io\n\n# Simulated temperature data file (city,temp_fahrenheit)\ntemp_data = io.StringIO("New York,82\\nLos Angeles,95\\nChicago,78\\nMiami,91")\n\n# Build the report\nreport = io.StringIO()\nreport.write("Daily Temperature Report\\n")\nreport.write("=" * 30 + "\\n")\n\ncities = []\ntemps = []\n\nfor line in temp_data:\n    city, temp = line.strip().split(",")\n    temp = int(temp)\n    cities.append(city)\n    temps.append(temp)\n    report.write(f"{city}: {temp}F\\n")\n\nreport.write("=" * 30 + "\\n")\n\n# Find hottest city\nmax_temp = max(temps)\nhottest_city = cities[temps.index(max_temp)]\nreport.write(f"Hottest: {hottest_city} at {max_temp}F\\n")\n\n# Calculate average\navg_temp = sum(temps) / len(temps)\nreport.write(f"Average: {avg_temp:.1f}F\\n")\n\nprint(report.getvalue())\n',
                    'expected_output': 'Daily Temperature Report\n==============================\nNew York: 82F\nLos Angeles: 95F\nChicago: 78F\nMiami: 91F\n==============================\nHottest: Los Angeles at 95F\nAverage: 86.5F\n',
                    'hint': 'Read each line from the data source, split by comma, and convert temperature to int. Track cities and temperatures in lists. Use max() to find the hottest and sum()/len() for the average.',
                },
            },
            {
                'id': 'context-managers-in-depth',
                'title': 'Context Managers in Depth',
                'content': """## Context Managers in Depth

The `with` statement is Python's way of ensuring resources are properly managed. It works through a mechanism called **context managers**.

### Why Context Managers Exist

Resources like files, network connections, and database connections need to be properly released when you are done with them. Forgetting to do so leads to:

- **Resource leaks** - your program holds onto resources it no longer needs.
- **Data loss** - written data might not be saved (flushed) to disk.
- **Locked files** - other programs cannot access files your program forgot to close.

### How `with` Works Behind the Scenes

When you use `with`, Python calls two special methods:

1. `__enter__()` - called when entering the block (like opening a file).
2. `__exit__()` - called when leaving the block (like closing a file), **even if an error occurs**.

```python
# These two are equivalent:

# Using with (preferred)
with open("data.txt", "r") as f:
    content = f.read()

# Manual approach (error-prone)
f = open("data.txt", "r")
try:
    content = f.read()
finally:
    f.close()
```

### Multiple Context Managers

You can manage multiple resources in a single `with` statement:

```python
# Reading from one file and writing to another
with open("input.txt", "r") as source, open("output.txt", "w") as dest:
    for line in source:
        dest.write(line.upper())
```

### Context Managers with StringIO

```python
import io

# StringIO also supports the context manager protocol
with io.StringIO() as output:
    output.write("Managed by context manager\\n")
    output.write("Resources cleaned up automatically\\n")
    result = output.getvalue()

print(result)
```

### Real-Life Analogy

A context manager is like a responsible assistant:
- **Hotel checkout**: The `with` block is your stay. You do not have to worry about returning the room key; it happens automatically when you leave.
- **Library borrowing**: The book is returned when your borrowing period ends, regardless of whether you finished it or lost interest halfway through.
- **Restaurant reservation**: Your table is released when you leave, whether you ate a full course or left after appetizers due to an emergency.

### Best Practices

1. **Always use `with`** for file operations.
2. **Keep the block small** - only include code that needs the resource.
3. **Process data outside the block** when possible to release the resource quickly.

```python
import io

# Good: Read data inside, process outside
with io.StringIO("100\\n200\\n300") as f:
    lines = f.readlines()

# Processing happens after the resource is released
total = sum(int(line.strip()) for line in lines)
print(f"Total: {total}")
```""",
                'exercise': {
                    'instructions': 'Demonstrate the read-inside, process-outside pattern. Use a with statement to read numeric data from a StringIO object into a list. After the with block ends, calculate and print the count, sum, and average of the numbers.',
                    'starter_code': 'import io\n\n# Simulated daily sales data file\nsales_data = "1250\\n1480\\n1100\\n1350\\n1600"\n\n# Read data inside the with block\nwith io.StringIO(sales_data) as f:\n    lines = f.readlines()\n\n# Process data outside the with block (resource is released)\nnumbers = [int(line.strip()) for line in lines]\n\nprint(f"Days: {len(numbers)}")\nprint(f"Total Sales: ${sum(numbers)}")\nprint(f"Average: ${sum(numbers) / len(numbers):.0f}")\n',
                    'expected_output': 'Days: 5\nTotal Sales: $6780\nAverage: $1356',
                    'hint': 'Use readlines() inside the with block to capture all lines. After the with block, convert each line to an integer. Use len(), sum(), and division for the statistics.',
                },
            },
        ],
    },
]
