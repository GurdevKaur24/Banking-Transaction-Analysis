# Day 11 – Recursion

## Topics Covered
- Recursion: definition
- Two parts of a recursive function: base case and recursive case
- Examples of recursion

## Recursion

### Definition
**Recursion** is when a **function calls itself** to solve a problem.
The big problem is broken into **smaller versions of the same problem** until it becomes simple enough to solve directly.

A function that calls itself is called a **recursive function**.

### Syntax
```python
def function_name(parameters):
    if condition:              # base case
        return value
    else:                      # recursive case
        return function_name(smaller_input)
```

## Two Parts of a Recursive Function

### 1. Base Case
- The condition where the function **stops calling itself**.
- It gives a direct answer without further recursion.
- Without a base case, the function would call itself forever and Python gives an error:
  `RecursionError: maximum recursion depth exceeded`

### 2. Recursive Case
- The part where the function **calls itself** with a **smaller or simpler input**.
- Each call moves closer to the base case.

| Part | Role |
|---|---|
| Base case | Stops the recursion |
| Recursive case | Calls the function again with a smaller problem |

## Examples

### Example 1: Factorial
Factorial of a number `n` is `n! = n × (n-1) × (n-2) × ... × 1`
For example, `5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    else:                     # recursive case
        return n * factorial(n - 1)

print(factorial(5))   # 120
```

How it works:
```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1          ← base case reached
= 120
```

### Example 2: Sum of Numbers from 1 to n
```python
def sum_numbers(n):
    if n == 0:                # base case
        return 0
    else:                     # recursive case
        return n + sum_numbers(n - 1)

print(sum_numbers(5))   # 15  (5 + 4 + 3 + 2 + 1)
```

### Example 3: Fibonacci Series
Each number is the sum of the previous two: `0, 1, 1, 2, 3, 5, 8, 13, ...`

```python
def fibonacci(n):
    if n <= 1:                # base case
        return n
    else:                     # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")   # 0 1 1 2 3 5 8 13
```

### Example 4: Countdown
```python
def countdown(n):
    if n == 0:                # base case
        print("Done!")
    else:                     # recursive case
        print(n)
        countdown(n - 1)

countdown(3)
```
Output:
```
3
2
1
Done!
```

## Recursion vs Loop
| Recursion | Loop |
|---|---|
| Function calls itself | Repeats code using `for` / `while` |
| Needs a base case to stop | Needs a condition to stop |
| Code is often shorter and cleaner | Usually faster and uses less memory |
| Can cause `RecursionError` if too deep | No such limit |


## Key Takeaway
Recursion solves a problem by making a function call itself with smaller inputs. Every recursive function needs a **base case** to stop and a **recursive case** that moves towards the base case. Factorial, sum of numbers and Fibonacci are common examples.
