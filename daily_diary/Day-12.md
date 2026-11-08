# Day 12 – Object-Oriented Programming (OOP)

## Topics Covered
- Introduction to OOP
- Classes and objects
- Attributes: class attributes and instance attributes
- Methods and the `__init__()` method
- The `self` parameter

## Introduction to OOP
**Object-Oriented Programming (OOP)** is a way of writing programs using **classes** and **objects**.
It groups related **data (attributes)** and **actions (methods)** together, which makes code organised, reusable and easier to manage.

Real-life example:
- **Class** = Car (blueprint)
- **Objects** = a red Honda, a black BMW
- **Attributes** = colour, brand, speed
- **Methods** = start(), brake()

## Class

### Definition
A **class** is a **blueprint or template** for creating objects. It defines what attributes and methods the objects will have.

### Syntax
```python
class ClassName:
    # attributes and methods
    pass
```

```python
class Student:
    pass
```

## Object

### Definition
An **object** is an **instance of a class**. It is a real item created from the class blueprint.
One class can create many objects.

```python
class Student:
    pass

s1 = Student()   # object 1
s2 = Student()   # object 2

print(type(s1))  # <class '__main__.Student'>
```

## The `__init__()` Method

### Definition
`__init__()` is a special method called a **constructor**. It runs **automatically** when a new object is created, and is used to **give initial values** to the object's attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Gurdev", 21)
print(s1.name)   # Gurdev
print(s1.age)    # 21
```

## The `self` Parameter

### Definition
`self` refers to the **current object** of the class.
- It is used to access the object's own attributes and methods.
- It must be the **first parameter** of every method in a class.
- We do **not** pass `self` when calling a method. Python passes it automatically.

```python
class Student:
    def __init__(self, name):
        self.name = name     # self.name belongs to this object

s1 = Student("Gurdev")
s2 = Student("Ravi")

print(s1.name)   # Gurdev
print(s2.name)   # Ravi
```

Here, `self` is `s1` in the first call and `s2` in the second, so each object keeps its own `name`.

> **Note:** `self` is just a naming convention. Any name would work, but `self` is always used by Python programmers.

## Attributes
**Attributes** are variables that store data related to a class or object.

### 1. Class Attributes
- Defined **inside the class but outside all methods**
- **Shared by all objects** of the class

### 2. Instance Attributes
- Defined **inside `__init__()` using `self`**
- **Different for each object**

```python
class Student:
    college = "GNDEC"            # class attribute (shared)

    def __init__(self, name, age):
        self.name = name         # instance attribute
        self.age = age           # instance attribute

s1 = Student("Gurdev", 21)
s2 = Student("Ravi", 22)

print(s1.name, s1.college)   # Gurdev GNDEC
print(s2.name, s2.college)   # Ravi GNDEC
print(Student.college)       # GNDEC
```

| Class Attribute | Instance Attribute |
|---|---|
| Defined outside methods, inside class | Defined inside `__init__()` using `self` |
| Same for all objects | Different for each object |
| Accessed by `ClassName.attr` or `object.attr` | Accessed by `object.attr` |
| Example: `college` | Example: `name`, `age` |

## Methods

### Definition
**Methods** are functions defined **inside a class**. They describe the actions an object can perform.
The first parameter of every method is `self`.

```python
class Student:
    college = "GNDEC"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, College: {self.college}")

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Gurdev", 85)
s1.display()          # Name: Gurdev, Marks: 85, College: GNDEC
print(s1.result())    # Pass

s2 = Student("Ravi", 35)
print(s2.result())    # Fail
```

## Summary
| Term | Meaning |
|---|---|
| Class | Blueprint for creating objects |
| Object | Instance of a class |
| Class attribute | Variable shared by all objects |
| Instance attribute | Variable unique to each object |
| Method | Function inside a class |
| `__init__()` | Constructor, runs automatically when an object is created |
| `self` | Refers to the current object |


## Key Takeaway
OOP organises code using classes and objects. A class is a blueprint, and objects are created from it. `__init__()` sets up each object's starting values, `self` refers to the current object, class attributes are shared by all objects, and instance attributes are unique to each object. In data analysis, a Pandas DataFrame is itself an object with attributes (like `shape`) and methods (like `head()`).
