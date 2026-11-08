# Day 07 – Data Structures: Dictionaries

## Topics Covered
- Dictionaries: definition and features
- Accessing, modifying, removing, updating and clearing items
- Accessing all keys, all values and key:value pairs

## Dictionary

### Definition
A **dictionary** is a collection of **key : value pairs** written inside **curly braces `{ }`**.
Each **key** is linked to a **value**, and we use the key to get the value.

```python
student = {
    "name": "Gurdev",
    "age": 21,
    "course": "Data Analytics"
}
```

### Features of a Dictionary
| Feature | Meaning |
|---|---|
| **Key : value pairs** | Data is stored as pairs, e.g. `"name": "Gurdev"` |
| **Ordered** | Items keep the order in which they were added (Python 3.7+) |
| **Mutable** | Items can be added, changed or removed |
| **Unique keys** | Keys cannot repeat. If a key is repeated, the last value is kept. Values can repeat. |
| **Keys must be immutable** | Keys can be str, int or tuple, but not lists |
| **Accessed by key** | Items are accessed using keys, not index numbers |

```python
data = {"a": 1, "a": 2}
print(data)   # {'a': 2}   → duplicate key, last value kept
```

## Dictionary Operations

### 1. Access
```python
student = {"name": "Gurdev", "age": 21, "course": "Data Analytics"}

print(student["name"])        # Gurdev
print(student.get("age"))     # 21

print(student.get("city"))    # None  , no error
print(student["city"])        # Error: KeyError: 'city'
```

| `dict[key]` | `dict.get(key)` |
|---|---|
| Error if key does not exist | Returns `None` (no error) if key does not exist |

### 2. Modify (Change a Value / Add New Item)
```python
student = {"name": "Gurdev", "age": 21}

student["age"] = 22          # change existing value
student["city"] = "Ludhiana" # add new key:value pair

print(student)   # {'name': 'Gurdev', 'age': 22, 'city': 'Ludhiana'}
```

### 3. Remove
| Method | Use |
|---|---|
| `pop(key)` | Removes the item with the given key and returns its value |
| `popitem()` | Removes the **last added** item |
| `del dict[key]` | Deletes the item with the given key |
| `del dict` | Deletes the whole dictionary |

```python
student = {"name": "Gurdev", "age": 21, "course": "DA", "city": "Ludhiana"}

student.pop("age")
print(student)   # {'name': 'Gurdev', 'course': 'DA', 'city': 'Ludhiana'}

student.popitem()
print(student)   # {'name': 'Gurdev', 'course': 'DA'}

del student["course"]
print(student)   # {'name': 'Gurdev'}
```

### 4. Update
`update()` adds or changes **multiple items at once**.
```python
student = {"name": "Gurdev", "age": 21}

student.update({"age": 22, "course": "Data Analytics"})
print(student)   # {'name': 'Gurdev', 'age': 22, 'course': 'Data Analytics'}
```

### 5. Clear
`clear()` removes **all items**, leaving an empty dictionary.
```python
student = {"name": "Gurdev", "age": 21}
student.clear()
print(student)   # {}
```

## Accessing All Keys, Values and Pairs

| Method | Returns |
|---|---|
| `keys()` | All keys |
| `values()` | All values |
| `items()` | All key:value pairs (as tuples) |

```python
student = {"name": "Gurdev", "age": 21, "course": "Data Analytics"}

print(student.keys())     # dict_keys(['name', 'age', 'course'])
print(student.values())   # dict_values(['Gurdev', 21, 'Data Analytics'])
print(student.items())    # dict_items([('name', 'Gurdev'), ('age', 21), ('course', 'Data Analytics')])
```

### Looping Through a Dictionary
```python
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, ":", value)
```
Output of the last loop:
```
name : Gurdev
age : 21
course : Data Analytics
```

## Comparison of Data Structures
| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Brackets | `[ ]` | `( )` | `{ }` | `{key: value}` |
| Ordered | Yes | Yes | No | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No / Values: Yes |
| Access by | Index | Index | Loop only | Key |


## Key Takeaway
A dictionary stores data as key:value pairs, which makes finding data by key fast and easy. We can access, modify, remove, update and clear items, and use `keys()`, `values()` and `items()` to work with all the data. Dictionaries are similar to how data is stored in JSON and in table rows.
