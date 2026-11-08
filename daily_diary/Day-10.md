# Day 10 – Lambda Functions

## Topics Covered
- Lambda functions: definition and syntax
- Using lambda with `map()`
- Using lambda with `filter()`
- Using lambda with `sorted()`

## Lambda Function

### Definition
A **lambda function** is a small, **anonymous (nameless) function** written in **one line** using the `lambda` keyword.
It can take any number of arguments but can have **only one expression**, and the result of that expression is returned automatically.

### Syntax
```python
lambda arguments: expression
```

### Example
Normal function:
```python
def square(x):
    return x * x

print(square(5))   # 25
```

Same function using lambda:
```python
square = lambda x: x * x
print(square(5))   # 25
```

With multiple arguments:
```python
add = lambda a, b: a + b
print(add(10, 5))   # 15
```

### Normal Function vs Lambda Function
| Normal Function (`def`) | Lambda Function |
|---|---|
| Has a name | Anonymous (no name) |
| Can have many lines and statements | Only one expression |
| Uses `return` | Returns the result automatically |
| Used for bigger, reusable tasks | Used for small, short tasks |

Lambda functions are mostly used **inside other functions** like `map()`, `filter()` and `sorted()`.

## 1. `map()`
`map()` applies a function to **every item** in a list (or other iterable) and returns the results.

### Syntax
```python
map(function, iterable)
```

### Example
```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print(squares)   # [1, 4, 9, 16, 25]
```

```python
names = ["gurdev", "ravi", "simran"]

upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)   # ['GURDEV', 'RAVI', 'SIMRAN']
```

> **Note:** `map()` returns a map object, so we use `list()` to see the result.

## 2. `filter()`
`filter()` keeps only the items for which the function returns **True**.

### Syntax
```python
filter(function, iterable)
```

### Example
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)   # [2, 4, 6, 8]
```

```python
marks = [45, 78, 32, 90, 60]

passed = list(filter(lambda m: m >= 50, marks))
print(passed)   # [78, 90, 60]
```

## 3. `sorted()`
`sorted()` returns a **new sorted list**. With the `key` parameter and a lambda, we can choose **how** to sort.

### Syntax
```python
sorted(iterable, key=function, reverse=False)
```

### Example
Sort words by length:
```python
words = ["banana", "kiwi", "apple", "fig"]

result = sorted(words, key=lambda w: len(w))
print(result)   # ['fig', 'kiwi', 'apple', 'banana']
```

Sort a list of tuples by the second value:
```python
students = [("Gurdev", 85), ("Ravi", 72), ("Simran", 91)]

by_marks = sorted(students, key=lambda s: s[1])
print(by_marks)   # [('Ravi', 72), ('Gurdev', 85), ('Simran', 91)]

by_marks_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks_desc)   # [('Simran', 91), ('Gurdev', 85), ('Ravi', 72)]
```

## Summary
| Function | What it does | Example | Result |
|---|---|---|---|
| `map()` | Applies a function to every item | `map(lambda x: x*2, [1,2,3])` | `[2, 4, 6]` |
| `filter()` | Keeps items where the condition is True | `filter(lambda x: x>2, [1,2,3,4])` | `[3, 4]` |
| `sorted()` | Sorts items using a custom key | `sorted(["bb","a","ccc"], key=lambda w: len(w))` | `['a', 'bb', 'ccc']` |


## Key Takeaway
Lambda functions are short, one-line, nameless functions. They are most useful with `map()` to transform data, `filter()` to select data and `sorted()` to sort data in a custom way. The same idea is used in Pandas, for example with `df["column"].apply(lambda x: ...)`.
