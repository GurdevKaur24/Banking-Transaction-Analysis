# Day 13 – Four Pillars of OOP

## Topics Covered
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

## Introduction
The **four pillars of OOP** are the main principles that make object-oriented programs organised, secure and reusable.

| Pillar | Simple Meaning |
|---|---|
| **Encapsulation** | Wrapping data and methods together and protecting the data |
| **Inheritance** | One class getting the properties of another class |
| **Polymorphism** | One name, many forms |
| **Abstraction** | Showing only the essential details and hiding the rest |

## 1. Encapsulation

### Definition
**Encapsulation** means **wrapping data (attributes) and methods together inside a class** and **restricting direct access** to some of the data.
This protects data from being changed by mistake.

### Access Modifiers in Python
| Type | Syntax | Access |
|---|---|---|
| **Public** | `name` | Can be accessed from anywhere |
| **Protected** | `_name` (single underscore) | Should be used only inside the class and its child classes (a convention) |
| **Private** | `__name` (double underscore) | Cannot be accessed directly from outside the class |

### Example
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):          # getter method
        return self.__balance

acc = BankAccount("Gurdev", 1000)
acc.deposit(500)
print(acc.owner)           # Gurdev
print(acc.get_balance())   # 1500

print(acc.__balance)       # Error: AttributeError
```

The balance can only be changed through `deposit()`, which checks that the amount is valid.

## 2. Inheritance

### Definition
**Inheritance** allows a class (**child / derived class**) to **get the attributes and methods** of another class (**parent / base class**).
It promotes **code reusability**.

### Syntax
```python
class Parent:
    pass

class Child(Parent):
    pass
```

### Example
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Student(Person):              # Student inherits from Person
    def __init__(self, name, course):
        super().__init__(name)      # call parent constructor
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")

s1 = Student("Gurdev", "Data Analytics")
s1.greet()   # Hello, I am Gurdev          (inherited method)
s1.study()   # Gurdev is studying Data Analytics
```

> `super()` is used to call the parent class's methods, such as its `__init__()`.

### Types of Inheritance
| Type | Meaning | Structure |
|---|---|---|
| **Single** | One child inherits from one parent | A → B |
| **Multiple** | One child inherits from more than one parent | A, B → C |
| **Multilevel** | A child inherits from a class that is itself a child | A → B → C |
| **Hierarchical** | Many children inherit from one parent | A → B, A → C |
| **Hybrid** | A combination of two or more types | Mixed |

```python
# Multilevel
class A:
    def show_a(self): print("Class A")

class B(A):
    def show_b(self): print("Class B")

class C(B):
    def show_c(self): print("Class C")

obj = C()
obj.show_a()   # Class A
obj.show_b()   # Class B
obj.show_c()   # Class C
```

## 3. Polymorphism

### Definition
**Polymorphism** means **"many forms"**. The **same function, method or operator** behaves **differently** depending on the object or data it works with.

### Example 1: Built-in Polymorphism
```python
print(len("Python"))        # 6  → length of string
print(len([1, 2, 3]))       # 3  → length of list

print(5 + 10)               # 15          → addition
print("Data " + "Analyst")  # Data Analyst → joining strings
```

### Example 2: Method Overriding
A child class gives its **own version** of a method that already exists in the parent class.
```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.sound()
```
Output:
```
Dog barks
Cat meows
Animal makes a sound
```

The same method name `sound()` gives a different result for each object.

## 4. Abstraction

### Definition
**Abstraction** means **showing only the essential features and hiding the internal details**.
The user knows **what** an object does, not **how** it does it.

Real-life example: when driving a car, we use the steering and brakes without knowing how the engine works inside.

### Abstract Class in Python
Python uses the `abc` module to create abstract classes.
- An **abstract class** cannot be used to create objects directly.
- An **abstract method** is declared in the parent but must be **written (implemented) in the child class**.

```python
from abc import ABC, abstractmethod

class Shape(ABC):                  # abstract class
    @abstractmethod
    def area(self):                # abstract method
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(5, 4)
c = Circle(3)
print(r.area())   # 20
print(c.area())   # 28.26

s = Shape()       # Error: TypeError: Can't instantiate abstract class Shape
```

## Summary
| Pillar | Definition | How in Python | Example |
|---|---|---|---|
| Encapsulation | Wrap data and methods, restrict access | Private (`__`) / protected (`_`) attributes, getter methods | `BankAccount` with private balance |
| Inheritance | Child class reuses parent class code | `class Child(Parent)`, `super()` | `Student` inherits `Person` |
| Polymorphism | Same name, different behaviour | Method overriding, built-in functions | `sound()` for Dog and Cat |
| Abstraction | Hide details, show only essentials | `ABC`, `@abstractmethod` | `Shape` with `area()` |


## Key Takeaway
The four pillars of OOP are encapsulation (protecting data), inheritance (reusing code), polymorphism (one name, many forms) and abstraction (hiding complex details). Together they make code secure, reusable, flexible and easier to maintain.
