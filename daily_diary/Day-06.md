# Day 06 – Data Structures: Sets

## Topics Covered
- Sets: definition and features
- Set methods: `add()`, `remove()`, `discard()`
- Set operations: union, intersection, difference, symmetric difference
- Frozen set

## Set

### Definition
A **set** is an unordered collection of **unique** items written inside **curly braces `{ }`**.
- `{}` creates an empty **dictionary**, not a set. Use `set()` to create an empty set.

```python
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "mango"}
```

Duplicates are removed automatically:
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)   # {1, 2, 3}
```

> ```python
> empty = set()
> print(type(empty))   # <class 'set'>
> ```

### Features of a Set
| Feature | Meaning |
|---|---|
| **Unordered** | Items have no fixed order, so the printed order may change |
| **Unique items** | No duplicate values are allowed |
| **Not indexed** | Items cannot be accessed using an index |
| **Mutable** | Items can be added or removed |
| **Only unchangeable items** | Can hold int, float, str, tuple, but not lists or dictionaries |

**Common use:** removing duplicates from a list.
```python
marks = [80, 90, 80, 70, 90]
unique_marks = set(marks)
print(unique_marks)   # {80, 90, 70}
```

## Set Methods

### `add()` – Add One Item
```python
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)   # {1, 2, 3, 4}

numbers.add(2)   # already present, so nothing changes
print(numbers)   # {1, 2, 3, 4}
```

### `remove()` – Remove an Item
Gives an **error** if the item is not found.
```python
numbers = {1, 2, 3, 4}
numbers.remove(3)
print(numbers)   # {1, 2, 4}

numbers.remove(10)   # KeyError: 10
```

### `discard()` – Remove an Item Safely
Gives **no error** if the item is not found.
```python
numbers = {1, 2, 3, 4}
numbers.discard(3)
print(numbers)   # {1, 2, 4}

numbers.discard(10)   # no error
print(numbers)        # {1, 2, 4}
```

| `remove()` | `discard()` |
|---|---|
| Error if item is not present | No error if item is not present |

## Set Operations

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

| Operation | Meaning | Method | Operator | Result |
|---|---|---|---|---|
| **Union** | All items from both sets | `A.union(B)` | `A \| B` | `{1, 2, 3, 4, 5, 6}` |
| **Intersection** | Items common to both sets | `A.intersection(B)` | `A & B` | `{3, 4}` |
| **Difference** | Items in A but not in B | `A.difference(B)` | `A - B` | `{1, 2}` |
| **Symmetric Difference** | Items in A or B, but not in both | `A.symmetric_difference(B)` | `A ^ B` | `{1, 2, 5, 6}` |

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # {1, 2, 3, 4, 5, 6}
print(A & B)   # {3, 4}
print(A - B)   # {1, 2}
print(B - A)   # {5, 6}
print(A ^ B)   # {1, 2, 5, 6}
```

## Frozen Set

### Definition
A **frozen set** is an **unchangeable (immutable)** version of a set. It is created using `frozenset()`.

```python
fs = frozenset([1, 2, 3, 3])
print(fs)   # frozenset({1, 2, 3})

fs.add(4)   # AttributeError: 'frozenset' object has no attribute 'add'
```

Set operations still work on frozen sets:
```python
A = frozenset([1, 2, 3])
B = frozenset([3, 4])
print(A | B)   # frozenset({1, 2, 3, 4})
print(A & B)   # frozenset({3})
```

| Set | Frozen Set |
|---|---|
| Mutable (can add/remove) | Immutable (cannot change) |
| Created with `{ }` or `set()` | Created with `frozenset()` |
| Cannot be used as a dictionary key | Can be used as a dictionary key |


## Key Takeaway
A set stores only unique values with no order or index. `add()`, `remove()` and `discard()` change a set, and union, intersection, difference and symmetric difference make it easy to compare groups of data. A frozen set is the unchangeable version of a set.
