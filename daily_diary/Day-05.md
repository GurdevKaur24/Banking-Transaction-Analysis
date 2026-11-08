# Day 05 – Data Structures: Tuples

## Topics Covered
- Tuples: definition and features
- `sorted()` on a tuple
- Sum of all tuple elements
- Iterating through tuple elements
- `index()` (and indexing)

## Tuple

### Definition
A **tuple** is an ordered collection of items written inside **parentheses `( )`**, with items separated by commas.
Once a tuple is created, its items **cannot be changed**.
- A tuple with one item needs a comma: `single = (5,)`. Without the comma, `(5)` is just an integer.


```python
colors = ("red", "green", "blue")
numbers = (10, 20, 30, 40)
mixed = (1, "Python", 3.5, True)
```

### Features of a Tuple
| Feature | Meaning |
|---|---|
| **Ordered** | Items keep their order |
| **Immutable (unchangeable)** | Items cannot be added, removed or changed after creation |
| **Allows duplicates** | The same value can appear more than once |
| **Indexed** | Each item has an index starting from 0 (negative indexing also works) |
| **Different data types** | One tuple can hold int, float, str, bool and more |
| **Faster than lists** | Because they are fixed, tuples are slightly faster and use less memory |

```python
colors = ("red", "green", "blue")
colors[0] = "yellow"   # TypeError: 'tuple' object does not support item assignment
```

## Examples

### Accessing Elements (Indexing)
```python
colors = ("red", "green", "blue")
print(colors[0])    # red
print(colors[-1])   # blue
print(colors[0:2])  # ('red', 'green')
print(len(colors))  # 3
```

### `index()` – Find the Position of an Item
```python
numbers = (10, 20, 30, 20)
print(numbers.index(30))   # 2
print(numbers.count(20))   # 2
```

### `sorted()` – Sort a Tuple
Tuples do not have a `sort()` method because they cannot be changed.
`sorted()` returns a **new sorted list**, and the original tuple stays the same.

```python
numbers = (40, 10, 30, 20)

print(sorted(numbers))                 # [10, 20, 30, 40]
print(sorted(numbers, reverse=True))   # [40, 30, 20, 10]
print(tuple(sorted(numbers)))          # (10, 20, 30, 40)  → convert back to tuple
print(numbers)                         # (40, 10, 30, 20)  → original unchanged
```


### Iterating Through Tuple Elements
Using a `for` loop:
```python
colors = ("red", "green", "blue")

for color in colors:
    print(color)
```
Output:
```
red
green
blue
```

With index using `range()`:
```python
for i in range(len(colors)):
    print(i, colors[i])
```
Output:
```
0 red
1 green
2 blue
```

## List vs Tuple
| List | Tuple |
|---|---|
| Written in `[ ]` | Written in `( )` |
| Mutable (can change) | Immutable (cannot change) |
| Many methods (`append`, `remove`, `sort`…) | Only 2 methods: `count()` and `index()` |
| Slightly slower | Slightly faster |
| Used when data needs to change | Used for fixed data (e.g. days of the week, coordinates) |


## Key Takeaway
A tuple is an ordered, unchangeable collection. We can access items with indexing, find positions with `index()`, sort with `sorted()`, add all values with `sum()`, and loop through items with `for`. Tuples are best for data that should stay fixed.
