# Day 04 – Data Structures: Lists

## Topics Covered
- Introduction to data structures
- Lists: definition and features
- List methods: adding, deleting, updating, index, count, sort, copy

## Data Structures
A **data structure** is a way of storing and organising data so it can be used efficiently.
Python has four main built-in data structures: **List**, **Tuple**, **Set** and **Dictionary**.

## List

### Definition
A **list** is an ordered collection of items written inside **square brackets `[ ]`**, with items separated by commas.

```python
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = [1, "Python", 3.5, True]
```

### Features of a List
| Feature | Meaning |
|---|---|
| **Ordered** | Items keep the order in which they are added |
| **Mutable (changeable)** | Items can be added, removed or changed after creation |
| **Allows duplicates** | The same value can appear more than once |
| **Indexed** | Each item has an index starting from 0 (negative indexing also works) |
| **Different data types** | One list can hold int, float, str, bool and more |

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])    # apple
print(fruits[-1])   # mango
print(len(fruits))  # 3
```

## List Methods

### 1. Adding Items
| Method | Use |
|---|---|
| `append()` | Adds one item at the **end** |
| `insert()` | Adds an item at a **specific position** |
| `extend()` | Adds **multiple items** (from another list) at the end |

```python
fruits = ["apple", "banana"]

fruits.append("mango")
print(fruits)   # ['apple', 'banana', 'mango']

fruits.insert(1, "orange")
print(fruits)   # ['apple', 'orange', 'banana', 'mango']

fruits.extend(["grapes", "kiwi"])
print(fruits)   # ['apple', 'orange', 'banana', 'mango', 'grapes', 'kiwi']
```

### 2. Deleting Items
| Method | Use |
|---|---|
| `remove()` | Removes the item by **value** (first match) |
| `pop()` | Removes the item by **index** (last item if no index given) and returns it |
| `clear()` | Removes **all items**, leaving an empty list |
| `del` | Keyword to delete an item by index, or delete the whole list |

```python
fruits = ["apple", "banana", "mango", "kiwi"]

fruits.remove("banana")
print(fruits)   # ['apple', 'mango', 'kiwi']

fruits.pop()
print(fruits)   # ['apple', 'mango']

fruits.pop(0)
print(fruits)   # ['mango']

fruits.clear()
print(fruits)   # []

numbers = [10, 20, 30]
del numbers[1]
print(numbers)  # [10, 30]
del numbers     # deletes the whole list
```

### 3. Updating Items
Lists are mutable, so an item can be changed using its index.

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)   # ['apple', 'orange', 'mango']
```

### 4. Other Methods
| Method | Use |
|---|---|
| `index()` | Returns the index of the first matching item |
| `count()` | Counts how many times an item appears |
| `sort()` | Sorts the list (ascending by default) |
| `copy()` | Returns a copy of the list |

```python
numbers = [40, 10, 30, 10, 20]

print(numbers.index(30))   # 2
print(numbers.count(10))   # 2

numbers.sort()
print(numbers)             # [10, 10, 20, 30, 40]

numbers.sort(reverse=True)
print(numbers)             # [40, 30, 20, 10, 10]

new_list = numbers.copy()
print(new_list)            # [40, 30, 20, 10, 10]
```

## Summary of List Methods
| Category | Methods |
|---|---|
| Adding | `append()`, `insert()`, `extend()` |
| Deleting | `remove()`, `pop()`, `clear()`, `del` |
| Updating | `list[index] = new_value` |
| Searching | `index()`, `count()` |
| Others | `sort()`, `copy()` |


## Key Takeaway
A list is an ordered, changeable collection that allows duplicates. With methods to add, delete, update, search, sort and copy items, lists are one of the most useful data structures in Python and are used a lot when handling data.
