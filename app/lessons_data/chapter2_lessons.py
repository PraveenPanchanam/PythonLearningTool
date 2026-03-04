CHAPTER_ORDER = 2

LESSONS = [
    {
        'title': 'Introduction to if/elif/else',
        'description': 'Learn how to make decisions in your programs using if, elif, and else statements - the foundation of all program logic.',
        'order': 1,
        'item_order': 1,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'why-conditions-matter',
                'title': 'Why Conditions Matter',
                'diagram': {
                    'id': 'ch2-conditionals-flow',
                    'title': 'if / elif / else Flowchart',
                    'file': 'diagrams/ch2-conditionals-flow.svg',
                    'data_file': 'diagrams/excalidraw-data/ch2-conditionals-flow.json',
                },
                'content': """## Why Conditions Matter

Every day, you make hundreds of decisions without even thinking about it:

- *"If it's raining, I'll take an umbrella. Otherwise, I'll wear sunglasses."*
- *"If my bank balance is above $50, I can go out for dinner. Otherwise, I'll cook at home."*
- *"If the traffic light is green, I go. If it's yellow, I slow down. If it's red, I stop."*

Programs need to make decisions too. **Conditional statements** let your code choose different paths based on whether something is `True` or `False`.

### The `if` Statement

The simplest conditional is the `if` statement. It runs a block of code only when a condition is `True`:

```python
temperature = 35

if temperature > 30:
    print("It's a hot day!")
    print("Stay hydrated.")
```

**Key rules:**

1. The condition must be followed by a **colon** (`:`).
2. The code block underneath must be **indented** (4 spaces is standard).
3. The indented block only runs when the condition evaluates to `True`.

### Real-Life Example: Age Verification

Imagine you are building a website that sells age-restricted products:

```python
customer_age = 20

if customer_age >= 18:
    print("Access granted. Welcome to the store!")
```

If `customer_age` is less than 18, nothing happens -- the program simply skips the indented block and moves on.

### What Counts as True or False?

Remember from Chapter 1 that Python has "truthy" and "falsy" values. Conditions are not limited to comparison operators:

```python
name = "Alice"

if name:
    print("Name is not empty")

items_in_cart = 0

if not items_in_cart:
    print("Your cart is empty")
```""",
                'exercise': None,
                'game': {
                    'type': 'predict_output',
                    'instructions': 'What do you think this code will print? Type your guess!',
                    'code_snippet': 'age = 15\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")',
                    'expected_output': 'Minor',
                    'explanation': 'Since age is 15, and 15 is NOT greater than or equal to 18, the else block runs and prints "Minor"!',
                },
            },
            {
                'id': 'if-else-statements',
                'title': 'The if/else Statement',
                'content': """## The if/else Statement

An `if` statement alone handles only one scenario. But most real decisions have two outcomes: **do this** or **do that**. The `else` clause handles the alternative path.

```python
temperature = 15

if temperature > 25:
    print("Wear a t-shirt.")
else:
    print("Bring a jacket.")
```

### Real-Life Example: Pass or Fail

In a school grading system, a student either passes or fails:

```python
score = 72
passing_mark = 60

if score >= passing_mark:
    print("Congratulations! You passed.")
else:
    print("Sorry, you did not pass. Keep studying!")
```

### Real-Life Example: Even or Odd

Determining whether a number is even or odd is a classic programming task that uses the modulus operator (`%`):

```python
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

The modulus operator returns the remainder after division. If dividing by 2 leaves a remainder of 0, the number is even.

### Real-Life Example: Discount Eligibility

An online store gives a discount to members:

```python
is_member = True
price = 100.00

if is_member:
    final_price = price * 0.9  # 10% discount
    print(f"Member price: ${final_price:.2f}")
else:
    print(f"Regular price: ${price:.2f}")
```""",
                'exercise': {
                    'instructions': 'A bank requires a minimum balance of $1000 to avoid a monthly fee. Write a program that checks the account balance. If the balance is at least 1000, print "No monthly fee". Otherwise, print "Monthly fee of $25 applied" and then print the new balance after deducting 25.',
                    'starter_code': '# Bank account balance\nbalance = 750.00\nminimum_balance = 1000.00\nmonthly_fee = 25.00\n\n# Check if balance meets the minimum\nif balance >= minimum_balance:\n    print("No monthly fee")\nelse:\n    print("Monthly fee of $25 applied")\n    balance = balance - monthly_fee\n    print(f"New balance: ${balance:.2f}")\n',
                    'expected_output': 'Monthly fee of $25 applied\nNew balance: $725.00',
                    'hint': 'Compare balance to minimum_balance using >=. In the else block, subtract the monthly_fee from balance and print the result with 2 decimal places.',
                },
            },
            {
                'id': 'elif-chains',
                'title': 'The elif Chain',
                'content': """## The elif Chain

Many real-world decisions have more than two outcomes. Think of a traffic light: green means go, yellow means slow down, and red means stop. The `elif` (short for "else if") keyword lets you check multiple conditions in sequence.

```python
light = "yellow"

if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down.")
elif light == "red":
    print("Stop!")
else:
    print("Invalid light color.")
```

**How it works:**

1. Python checks the `if` condition first.
2. If that is `False`, it moves to the first `elif`.
3. It keeps checking each `elif` in order until one is `True`.
4. If none match, the `else` block runs (if present).
5. **Only one block executes** -- once a match is found, the rest are skipped.

### Real-Life Example: Student Grade Calculator

Schools assign letter grades based on numeric scores:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")
```

Notice that order matters! Since we check `>= 90` first, a score of 85 skips that check and falls into `>= 80`, which is correct.

### Real-Life Example: Shipping Cost Calculator

An online store charges shipping based on the order total:

```python
order_total = 45.00

if order_total >= 100:
    shipping = 0.00
    message = "Free shipping!"
elif order_total >= 50:
    shipping = 5.99
    message = "Standard shipping: $5.99"
else:
    shipping = 9.99
    message = "Shipping: $9.99"

print(message)
print(f"Order total with shipping: ${order_total + shipping:.2f}")
```

### Real-Life Example: BMI Category

Body Mass Index (BMI) categories are a great example of range-based conditions:

```python
bmi = 24.5

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25.0:
    category = "Normal weight"
elif bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi} -> Category: {category}")
```""",
                'exercise': {
                    'instructions': 'Write a program that determines the day type based on a day number (1=Monday through 7=Sunday). If the day is 1-5, print "Weekday". If it is 6, print "Saturday". If it is 7, print "Sunday". For any other number, print "Invalid day number". Use the given day_number variable set to 6.',
                    'starter_code': '# Day number (1=Monday, 7=Sunday)\nday_number = 6\n\n# Determine the day type\nif day_number >= 1 and day_number <= 5:\n    print("Weekday")\nelif day_number == 6:\n    print("Saturday")\nelif day_number == 7:\n    print("Sunday")\nelse:\n    print("Invalid day number")\n',
                    'expected_output': 'Saturday',
                    'hint': 'Check if the day is between 1 and 5 (inclusive) for weekdays, then check for 6 and 7 separately. Use else for any other value.',
                },
                'game': {
                    'type': 'quiz',
                    'instructions': 'Look at this code and pick the correct answer:',
                    'code_snippet': 'temperature = 35\nif temperature > 30:\n    print("Hot!")\nelif temperature > 20:\n    print("Warm")\nelse:\n    print("Cool")',
                    'question': 'What will this code print?',
                    'options': [
                        {'text': 'Hot!', 'correct': True},
                        {'text': 'Warm', 'correct': False},
                        {'text': 'Cool', 'correct': False},
                        {'text': 'Hot! Warm', 'correct': False},
                    ],
                    'explanation': 'temperature is 35, which IS greater than 30, so the first if block runs and prints "Hot!". Python skips the elif and else because the first condition was True!',
                },
            },
            {
                'id': 'grading-system-exercise',
                'title': 'Putting It All Together: Grading System',
                'content': """## Putting It All Together

Let's combine everything you have learned so far by building a more complete grading system. This is a common real-world task that teachers and school software must handle.

### Requirements for a Grade Report

A complete grade report needs to:
1. Determine the letter grade from the numeric score.
2. Decide if the student passed or failed (passing is 60 or above).
3. Print a summary with all the information.

```python
student_name = "Maria"
score = 78

# Determine letter grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Determine pass/fail
if score >= 60:
    status = "PASSED"
else:
    status = "FAILED"

print(f"Student: {student_name}")
print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Status: {status}")
```

### Multiple Independent Conditions

Sometimes you need to check several unrelated conditions. Use separate `if` statements (not elif) when the checks are independent:

```python
temperature = 32
humidity = 85

if temperature > 30:
    print("High temperature alert!")

if humidity > 80:
    print("High humidity alert!")
```

Both messages print because these are separate, independent checks. With `elif`, only the first matching condition would execute.""",
                'exercise': {
                    'instructions': 'Build a movie ticket pricing system. The base ticket price is $12.00. Children (age under 12) get 50% off. Seniors (age 65 and over) get 30% off. Everyone else pays full price. Calculate and print the ticket category and the final price for a person who is 8 years old.',
                    'starter_code': '# Ticket pricing system\nage = 8\nbase_price = 12.00\n\n# Determine discount based on age\nif age < 12:\n    category = "Child"\n    discount = 0.50\nelif age >= 65:\n    category = "Senior"\n    discount = 0.30\nelse:\n    category = "Adult"\n    discount = 0.00\n\n# Calculate final price\nfinal_price = base_price * (1 - discount)\n\n# Print the results\nprint(f"Category: {category}")\nprint(f"Ticket price: ${final_price:.2f}")\n',
                    'expected_output': 'Category: Child\nTicket price: $6.00',
                    'hint': 'Check age < 12 for children, age >= 65 for seniors, and else for adults. Multiply the base price by (1 - discount) to get the final price.',
                },
            },
        ],
    },
    {
        'title': 'Logical Operators and Nested Conditions',
        'description': 'Combine multiple conditions using and, or, and not operators. Learn to build nested decision trees for complex real-world logic like loan approvals and access control.',
        'order': 2,
        'item_order': 4,
        'estimated_time_minutes': 20,
        'sections': [
            {
                'id': 'logical-operators',
                'title': 'Logical Operators: and, or, not',
                'content': """## Logical Operators: and, or, not

Real-world decisions often depend on **multiple factors at once**. Think about getting a loan: the bank checks your credit score AND your income AND your employment status -- all at the same time. Python's logical operators let you combine conditions just like that.

### The `and` Operator

`and` returns `True` only when **both** conditions are `True`:

```python
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("You meet the basic requirements.")
```

| Condition A | Condition B | A and B |
|:-----------:|:-----------:|:-------:|
| True        | True        | True    |
| True        | False       | False   |
| False       | True        | False   |
| False       | False       | False   |

### Real-Life Example: Amusement Park Ride

Many rides have both a height AND an age requirement:

```python
height_cm = 140
age = 10

if height_cm >= 130 and age >= 8:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you don't meet the requirements.")
```

### The `or` Operator

`or` returns `True` when **at least one** condition is `True`:

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No alarm clock today!")
else:
    print("Time to wake up for work.")
```

| Condition A | Condition B | A or B |
|:-----------:|:-----------:|:------:|
| True        | True        | True   |
| True        | False       | True   |
| False       | True        | True   |
| False       | False       | False  |

### The `not` Operator

`not` flips a boolean value -- `True` becomes `False` and vice versa:

```python
is_raining = False

if not is_raining:
    print("Let's go for a walk!")
```

### Combining Operators

You can combine multiple logical operators. Use parentheses for clarity:

```python
age = 25
has_license = True
is_insured = True

if age >= 16 and has_license and is_insured:
    print("You are cleared to drive.")
```""",
                'exercise': {
                    'instructions': 'A theme park has a water slide with these rules: riders must be at least 120 cm tall AND at least 6 years old. However, anyone 18 or older can ride regardless of height. Write a program that checks if a person (height=115, age=19) can ride. Print "Welcome to the water slide!" if they can, or "Sorry, you cannot ride." if they cannot.',
                    'starter_code': '# Rider information\nheight_cm = 115\nage = 19\n\n# Check eligibility\n# Rule: (height >= 120 AND age >= 6) OR age >= 18\nif (height_cm >= 120 and age >= 6) or age >= 18:\n    print("Welcome to the water slide!")\nelse:\n    print("Sorry, you cannot ride.")\n',
                    'expected_output': 'Welcome to the water slide!',
                    'hint': 'Combine the conditions: (height >= 120 and age >= 6) covers the standard rule, and "or age >= 18" covers the adult override. Use parentheses to group the first condition.',
                },
            },
            {
                'id': 'nested-conditions',
                'title': 'Nested Conditions',
                'content': """## Nested Conditions

Sometimes a decision depends on a **previous decision**. You check one thing first, and based on the result, you check something else. This is called **nesting** -- placing one `if` statement inside another.

### Real-Life Analogy

Think about ordering food at a restaurant:
1. First: "Do they have vegetarian options?"
2. If yes: "Do they have vegan options?"
3. If no: "Do they have a fish dish?"

Each question depends on the answer to the previous one.

### Syntax

```python
has_ticket = True
is_vip = False

if has_ticket:
    print("Welcome to the event!")
    if is_vip:
        print("Please proceed to the VIP area.")
    else:
        print("Please take a general admission seat.")
else:
    print("You need a ticket to enter.")
```

### Real-Life Example: ATM Withdrawal

An ATM must check several things before dispensing cash:

```python
pin_correct = True
balance = 500
withdrawal_amount = 200

if pin_correct:
    print("PIN accepted.")
    if withdrawal_amount <= balance:
        new_balance = balance - withdrawal_amount
        print(f"Dispensing ${withdrawal_amount}")
        print(f"Remaining balance: ${new_balance}")
    else:
        print("Insufficient funds.")
else:
    print("Incorrect PIN. Access denied.")
```

### Real-Life Example: Online Order Processing

```python
item_in_stock = True
payment_verified = True
address_valid = True

if item_in_stock:
    if payment_verified:
        if address_valid:
            print("Order confirmed! Shipping soon.")
        else:
            print("Please update your shipping address.")
    else:
        print("Payment could not be verified.")
else:
    print("Item is out of stock.")
```

### When to Flatten Nested Conditions

Deeply nested code can be hard to read. You can often flatten it using `and`:

```python
# Nested version
if item_in_stock:
    if payment_verified:
        if address_valid:
            print("Order confirmed!")

# Flattened version (cleaner)
if item_in_stock and payment_verified and address_valid:
    print("Order confirmed!")
```

Use nesting when you need **different error messages** at each level. Use flattening when you just need to know if **all conditions** pass.""",
                'exercise': {
                    'instructions': 'Write a login system that first checks if the username is correct ("admin"), then checks if the password is correct ("secret123"). Print appropriate messages at each stage: "Invalid username." if the username is wrong, "Invalid password." if the password is wrong, or "Login successful! Welcome, admin." if both are correct.',
                    'starter_code': '# Login credentials\nusername = "admin"\npassword = "secret123"\n\n# Correct credentials\ncorrect_username = "admin"\ncorrect_password = "secret123"\n\n# Nested login check\nif username == correct_username:\n    if password == correct_password:\n        print("Login successful! Welcome, admin.")\n    else:\n        print("Invalid password.")\nelse:\n    print("Invalid username.")\n',
                    'expected_output': 'Login successful! Welcome, admin.',
                    'hint': 'First check if username matches correct_username. Inside that block, check if password matches correct_password. Use else blocks for the failure messages.',
                },
            },
            {
                'id': 'compound-conditions',
                'title': 'Compound Conditions in Practice',
                'content': """## Compound Conditions in Practice

Let's look at how real-world applications combine everything we have learned -- logical operators, elif chains, and nesting -- to solve practical problems.

### Real-Life Example: Loan Approval System

Banks evaluate loan applications using multiple criteria:

```python
credit_score = 720
annual_income = 65000
existing_debt = 10000
loan_amount = 25000

# Calculate debt-to-income ratio
debt_ratio = (existing_debt + loan_amount) / annual_income

print(f"Credit Score: {credit_score}")
print(f"Debt-to-Income Ratio: {debt_ratio:.2f}")

if credit_score >= 750 and debt_ratio < 0.4:
    print("Status: APPROVED - Excellent terms")
elif credit_score >= 650 and debt_ratio < 0.5:
    print("Status: APPROVED - Standard terms")
elif credit_score >= 550:
    print("Status: REVIEW REQUIRED - Higher risk")
else:
    print("Status: DENIED - Does not meet minimum criteria")
```

### Real-Life Example: Discount System

An e-commerce platform applies discounts based on multiple factors:

```python
is_member = True
order_total = 85.00
has_coupon = False
items_count = 5

# Start with no discount
discount_percent = 0

# Member discount
if is_member:
    discount_percent += 10

# Bulk purchase discount
if items_count >= 5:
    discount_percent += 5

# Large order discount
if order_total >= 100:
    discount_percent += 10

# Coupon discount
if has_coupon:
    discount_percent += 15

discount_amount = order_total * (discount_percent / 100)
final_total = order_total - discount_amount

print(f"Original total: ${order_total:.2f}")
print(f"Discount: {discount_percent}% (-${discount_amount:.2f})")
print(f"Final total: ${final_total:.2f}")
```

Notice how this uses **separate if statements** (not elif) because discounts can **stack** -- a customer can be a member AND buy in bulk AND use a coupon.

### The Ternary Expression (Conditional Expression)

For simple if/else assignments, Python offers a one-line shorthand:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Same as:
# if age >= 18:
#     status = "adult"
# else:
#     status = "minor"
```

This is useful for quick assignments but should not be used for complex logic.""",
                'exercise': None,
                'game': {
                    'type': 'drag_order',
                    'instructions': 'Arrange these code blocks to make a correct if/elif/else statement:',
                    'code_blocks': [
                        'score = 85',
                        'if score >= 90:',
                        '    print("A")',
                        'elif score >= 80:',
                        '    print("B")',
                        'else:',
                        '    print("C")',
                    ],
                    'explanation': 'First we set the variable, then check the highest condition first (>=90), then the next one (>=80), and else catches everything else!',
                },
            },
            {
                'id': 'access-control-exercise',
                'title': 'Building an Access Control System',
                'content': """## Building an Access Control System

Access control is everywhere: buildings, websites, apps, and even your phone. Let's build a system that determines what level of access a user gets.

### Access Levels

| Level   | Requirements                                     |
|---------|--------------------------------------------------|
| Full    | Admin role OR (Manager role AND in IT dept)      |
| Limited | Any authenticated employee                       |
| None    | Not authenticated                                |

### How It Works

```python
is_authenticated = True
role = "manager"
department = "IT"

if not is_authenticated:
    print("Access Level: NONE")
    print("Please log in to continue.")
elif role == "admin" or (role == "manager" and department == "IT"):
    print("Access Level: FULL")
    print("You have access to all systems.")
else:
    print("Access Level: LIMITED")
    print("You can access standard employee resources.")
```

This combines:
- `not` to check if someone is NOT logged in
- `or` to allow multiple paths to full access
- `and` (with parentheses) to require both role AND department
- `elif`/`else` for the three access tiers""",
                'exercise': {
                    'instructions': 'Build a shipping cost calculator. The rules are: (1) If the package weighs over 50 kg, print "Package too heavy for standard shipping." (2) Otherwise, if the destination is "domestic" and weight is under 5 kg, shipping costs $5.00. (3) If destination is "domestic" and weight is 5 kg or more, shipping costs $10.00. (4) If destination is "international" and weight is under 5 kg, shipping costs $15.00. (5) If destination is "international" and weight is 5 kg or more, shipping costs $25.00. Use weight=3 and destination="international".',
                    'starter_code': '# Package details\nweight = 3\ndestination = "international"\n\n# Calculate shipping cost\nif weight > 50:\n    print("Package too heavy for standard shipping.")\nelse:\n    if destination == "domestic" and weight < 5:\n        shipping_cost = 5.00\n    elif destination == "domestic" and weight >= 5:\n        shipping_cost = 10.00\n    elif destination == "international" and weight < 5:\n        shipping_cost = 15.00\n    elif destination == "international" and weight >= 5:\n        shipping_cost = 25.00\n\n    print(f"Destination: {destination}")\n    print(f"Weight: {weight} kg")\n    print(f"Shipping cost: ${shipping_cost:.2f}")\n',
                    'expected_output': 'Destination: international\nWeight: 3 kg\nShipping cost: $15.00',
                    'hint': 'First check if the weight exceeds 50 kg. Inside the else block, use elif chains combining destination and weight conditions with the "and" operator.',
                },
            },
        ],
    },
]
