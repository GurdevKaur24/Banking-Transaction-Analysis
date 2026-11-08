# Day 03 – Python Strings

## Topics Covered
- Strings: definition and examples
- String slicing
- Negative indexing
- String methods
- Format strings

## Strings

### Definition
A **string** is a sequence of characters (letters, numbers, symbols or spaces) written inside **single quotes (`' '`)**, **double quotes (`" "`)** or **triple quotes (`''' '''` / `""" """`)** for multi-line text.

### Examples
```python
name = 'Python'
city = "Ludhiana"
message = """This is a
multi-line string"""

print(name)
print(type(city))   # <class 'str'>
```

## Indexing
Each character in a string has a position number called an **index**. Indexing starts from **0**.

```
 P   y   t   h   o   n
 0   1   2   3   4   5     ← positive index
-6  -5  -4  -3  -2  -1     ← negative index
```

```python
text = "Python"
print(text[0])    # P
print(text[3])    # h
```

### Negative Indexing
Negative indexing counts from the **end** of the string. `-1` is the last character.

```python
text = "Python"
print(text[-1])   # n
print(text[-3])   # h
```

## String Slicing
Slicing takes a **part of a string** using `string[start : end : step]`.
- `start` is included, `end` is **not** included.
- If `start` is left out, it begins from the start. If `end` is left out, it goes to the end.

```python
text = "Python"
print(text[0:4])    # Pyth
print(text[2:])     # thon
print(text[:3])     # Pyt
print(text[-4:-1])  # tho
print(text[::2])    # Pto   (every 2nd character)
print(text[::-1])   # nohtyP (reverse string)
```

## String Methods
String methods are built-in functions used to work with strings. They return a **new** string, because strings cannot be changed (they are immutable).

| Method | Use | Example | Output |
|---|---|---|---|
| `upper()` | Converts to uppercase | `"hello".upper()` | `HELLO` |
| `lower()` | Converts to lowercase | `"HELLO".lower()` | `hello` |
| `title()` | First letter of each word capital | `"data analysis".title()` | `Data Analysis` |
| `capitalize()` | First letter of the string capital | `"python".capitalize()` | `Python` |
| `strip()` | Removes spaces from both ends | `"  hi  ".strip()` | `hi` |
| `replace()` | Replaces text | `"I like Java".replace("Java", "Python")` | `I like Python` |
| `split()` | Splits a string into a list | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `find()` | Returns the index of text (-1 if not found) | `"Python".find("h")` | `3` |
| `count()` | Counts how many times text appears | `"banana".count("a")` | `3` |
| `startswith()` | Checks the start of a string | `"Python".startswith("Py")` | `True` |
| `endswith()` | Checks the end of a string | `"data.csv".endswith(".csv")` | `True` |
| `len()` | Length of a string (built-in function) | `len("Python")` | `6` |

## Format Strings
Format strings are used to put variable values inside a string.

### 1. f-strings (most common)
```python
name = "Gurdev"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

### 2. format() method
```python
print("My name is {} and I am {} years old.".format(name, age))
```

### Formatting numbers
```python
price = 499.5678
print(f"Price: {price:.2f}")   # Price: 499.57
```

## Key Takeaway
Strings store text in Python. Indexing and slicing (including negative indexing) let us pick any part of a string, string methods help clean and change text, and f-strings make it easy to combine text with variables. These are very useful in data cleaning.
