# Day 08 – Operators in Python

## Topics Covered
- Operators: definition
- Types of operators: arithmetic, comparison, logical, assignment, membership, identity, bitwise

## Operators

### Definition
**Operators** are special symbols used to perform operations on values and variables.
The values an operator works on are called **operands**.

```python
result = 10 + 5
# 10 and 5 are operands, + is the operator
```

### Types of Operators
1. Arithmetic operators
2. Comparison operators
3. Logical operators
4. Assignment operators
5. Membership operators
6. Identity operators
7. Bitwise operators

## 1. Arithmetic Operators
Used for mathematical calculations.

| Operator | Name | Example (`a = 10`, `b = 3`) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | Division | `a / b` | `3.333...` |
| `//` | Floor division (removes decimal part) | `a // b` | `3` |
| `%` | Modulus (remainder) | `a % b` | `1` |
| `**` | Exponent (power) | `a ** b` | `1000` |

```python
a = 10
b = 3
print(a + b)    # 13
print(a / b)    # 3.3333333333333335
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

## 2. Comparison Operators
Used to compare two values. The result is always `True` or `False`.

| Operator | Meaning | Example (`a = 10`, `b = 3`) | Result |
|---|---|---|---|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>` | Greater than | `a > b` | `True` |
| `<` | Less than | `a < b` | `False` |
| `>=` | Greater than or equal to | `a >= 10` | `True` |
| `<=` | Less than or equal to | `b <= 2` | `False` |

## 3. Logical Operators
Used to combine conditions.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | True if **both** conditions are true | `5 > 3 and 10 > 5` | `True` |
| `or` | True if **at least one** condition is true | `5 > 3 or 10 < 5` | `True` |
| `not` | Reverses the result | `not(5 > 3)` | `False` |

```python
age = 21
print(age > 18 and age < 30)   # True
print(age < 18 or age > 60)    # False
print(not(age > 18))           # False
```

## 4. Assignment Operators
Used to assign values to variables.

| Operator | Example | Same as |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

```python
x = 10
x += 5
print(x)   # 15
x *= 2
print(x)   # 30
```

## 5. Membership Operators
Used to check if a value is **present in** a sequence (string, list, tuple, set or dictionary).

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `in` | True if the value is present | `"apple" in ["apple", "mango"]` | `True` |
| `not in` | True if the value is not present | `"kiwi" not in ["apple", "mango"]` | `True` |

```python
text = "Python"
print("Py" in text)       # True
print("Java" in text)     # False

student = {"name": "Gurdev", "age": 21}
print("name" in student)  # True  (checks keys)
```

## 6. Identity Operators
Used to check if two variables point to the **same object in memory**, not just equal values.

| Operator | Meaning |
|---|---|
| `is` | True if both refer to the same object |
| `is not` | True if they refer to different objects |

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)       # True   (same object)
print(x is z)       # False  (different objects)
print(x == z)       # True   (same values)
print(x is not z)   # True
```

| `==` | `is` |
|---|---|
| Compares **values** | Compares **memory location (identity)** |

## 7. Bitwise Operators
Work on numbers at the **binary (bit) level**.

Example: `a = 6` (binary `110`), `b = 3` (binary `011`)

| Operator | Name | Example | Binary | Result |
|---|---|---|---|---|
| `&` | AND | `a & b` | `110 & 011 = 010` | `2` |
| `\|` | OR | `a \| b` | `110 \| 011 = 111` | `7` |
| `^` | XOR | `a ^ b` | `110 ^ 011 = 101` | `5` |
| `~` | NOT | `~a` | `-(a + 1)` | `-7` |
| `<<` | Left shift | `a << 1` | `110 → 1100` | `12` |
| `>>` | Right shift | `a >> 1` | `110 → 11` | `3` |

```python
a = 6
b = 3
print(a & b)    # 2
print(a | b)    # 7
print(a ^ b)    # 5
print(~a)       # -7
print(a << 1)   # 12
print(a >> 1)   # 3
```

## Summary
| Type | Operators |
|---|---|
| Arithmetic | `+  -  *  /  //  %  **` |
| Comparison | `==  !=  >  <  >=  <=` |
| Logical | `and  or  not` |
| Assignment | `=  +=  -=  *=  /=  //=  %=  **=` |
| Membership | `in  not in` |
| Identity | `is  is not` |
| Bitwise | `&  \|  ^  ~  <<  >>` |


## Key Takeaway
Operators let us calculate, compare, combine conditions, assign values, check membership and identity, and work with bits. Comparison and logical operators are especially important in data analysis for filtering data with conditions.
