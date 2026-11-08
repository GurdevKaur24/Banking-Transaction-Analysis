# Day 02 – Variables and Data Types

## Topics Covered
- Variables: definition and rules
- Data types: definition and types

## Variables

### Definition
A **variable** is a name that stores a value in memory. We use it to save data and use it later in the program.

```python
name = "Gurdev"
age = 21
```

### Rules for Naming Variables
1. A variable name can contain **letters, numbers and underscore (`_`)** only.
2. It must **start with a letter or underscore**, not a number.
3. **No spaces** are allowed.
4. Variable names are **case-sensitive** (`Age` and `age` are different).
5. **Keywords cannot be used** as variable names.

## Data Types

### Definition
A **data type** tells what kind of value a variable holds, for example a number, text or a list. Python sets the data type automatically. We can check it using `type()`.

```python
x = 10
print(type(x))   # <class 'int'>
```

### Types of Data Types

| Category | Data Type | Description | Example |
|---|---|---|---|
| **Numeric** | `int` | Whole numbers | `10`, `-5` |
| | `float` | Decimal numbers | `3.14`, `-0.5` |
| | `complex` | Numbers with a real and an imaginary part | `2 + 3j` |
| **Sequence** | `str` | Text, written in quotes | `"Hello"` |
| | `list` | Ordered, changeable collection, in `[ ]` | `[1, 2, 3]` |
| | `tuple` | Ordered, unchangeable collection, in `( )` | `(1, 2, 3)` |
| **Mapping** | `dict` | Key–value pairs, in `{ }` | `{"name": "Ravi", "age": 20}` |
| **Set** | `set` | Unordered collection of unique values, in `{ }` | `{1, 2, 3}` |
| **Boolean** | `bool` | Only two values | `True`, `False` |


## Key Takeaway
Variables store data, and every value in Python has a data type. Python decides the type automatically, and choosing the right data type (list, tuple, dict, set and so on) depends on how the data needs to be stored and used.
