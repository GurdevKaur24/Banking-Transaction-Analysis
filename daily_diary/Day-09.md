# Day 09 – Functions in Python

## Topics Covered
- Functions: definition and syntax
- Types of arguments: positional, keyword, default, arbitrary (`*args`, `**kwargs`)

## Functions

### Definition
A **function** is a block of reusable code that performs a specific task. It runs only when it is **called**.

Functions help to:
- Avoid writing the same code again and again
- Break a program into small, manageable parts
- Make code easier to read and maintain

There are two kinds of functions:
- **Built-in functions**: already available in Python, e.g. `print()`, `len()`, `type()`, `sum()`
- **User-defined functions**: created by us using the `def` keyword

### Syntax
```python
def function_name(parameters):
    # body of the function
    return value
```

- `def`: keyword used to define a function
- `function_name`: name of the function (follows variable naming rules)
- `parameters`: inputs the function receives (optional)
- `return`: sends a result back (optional)

### Example
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Gurdev")
print(message)   # Hello, Gurdev!
```

```python
def add(a, b):
    return a + b

print(add(10, 5))   # 15
```

### Parameters vs Arguments
| Parameter | Argument |
|---|---|
| Variable written in the function **definition** | Actual value passed when **calling** the function |
| `def add(a, b):` → `a`, `b` | `add(10, 5)` → `10`, `5` |

## Types of Arguments

### 1. Positional Arguments
Values are matched to parameters **by their position (order)**.
```python
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student("Gurdev", 21)   # Name: Gurdev, Age: 21
student(21, "Gurdev")   # Name: 21, Age: Gurdev   → wrong order gives wrong result
```

### 2. Keyword Arguments
Values are passed using the **parameter name**, so the order does not matter.
```python
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Gurdev")   # Name: Gurdev, Age: 21
```

### 3. Default Arguments
A parameter is given a **default value**. If no value is passed, the default is used.
```python
def student(name, course="Data Analytics"):
    print(f"{name} is studying {course}")

student("Gurdev")              # Gurdev is studying Data Analytics
student("Ravi", "Python")      # Ravi is studying Python
```

> **Note:** Default parameters must come **after** non-default parameters.
> `def student(course="DA", name):` gives an error.

### 4. Arbitrary Arguments
Used when we **don't know how many arguments** will be passed.

#### `*args` (Arbitrary Positional Arguments)
- Accepts **any number of positional arguments**
- Inside the function, `args` is a **tuple**

```python
def total(*args):
    print(args)
    return sum(args)

print(total(10, 20))           # (10, 20) → 30
print(total(5, 10, 15, 20))    # (5, 10, 15, 20) → 50
```

#### `**kwargs` (Arbitrary Keyword Arguments)
- Accepts **any number of keyword arguments**
- Inside the function, `kwargs` is a **dictionary**

```python
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(name="Gurdev", age=21, course="Data Analytics")
```
Output:
```
name: Gurdev
age: 21
course: Data Analytics
```

#### Using Both Together
```python
def show(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show(1, 2, 3, name="Gurdev", city="Ludhiana")
```
Output:
```
args: (1, 2, 3)
kwargs: {'name': 'Gurdev', 'city': 'Ludhiana'}
```

## Summary of Argument Types
| Type | How values are passed | Example call |
|---|---|---|
| Positional | By order | `add(10, 5)` |
| Keyword | By parameter name | `add(b=5, a=10)` |
| Default | Uses default value if not given | `student("Gurdev")` |
| `*args` | Any number of values, stored as a tuple | `total(1, 2, 3)` |
| `**kwargs` | Any number of name=value pairs, stored as a dictionary | `details(name="Ravi", age=20)` |


## Key Takeaway
Functions make code reusable and organised. Arguments can be passed by position, by keyword or with default values, and `*args` and `**kwargs` let a function accept any number of inputs. Functions are used everywhere in data analysis, for example to clean or transform data in the same way many times.
