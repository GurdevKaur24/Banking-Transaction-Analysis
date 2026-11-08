# Day 19 – Aggregate Functions and GROUP BY

## Topics Covered
- Aggregate functions: definition and types
- GROUP BY
- HAVING

## Aggregate Functions

### Definition
**Aggregate functions** perform a calculation on **a set of values (many rows)** and return **a single value**.
They are used to summarise data, for example total sales, average salary or number of customers.

## Sample Table

**employees**
| emp_id | name | department | salary |
|---|---|---|---|
| 1 | Janvi | IT | 50000 |
| 2 | Ravi | HR | 40000 |
| 3 | Simran | IT | 60000 |
| 4 | Aman | Sales | 35000 |
| 5 | Priya | HR | 45000 |
| 6 | Karan | IT | NULL |

## Types of Aggregate Functions

| Function | Purpose | Example | Result |
|---|---|---|---|
| `COUNT()` | Counts rows or values | `COUNT(*)` | `6` |
| `SUM()` | Total of values | `SUM(salary)` | `230000` |
| `AVG()` | Average of values | `AVG(salary)` | `46000` |
| `MIN()` | Smallest value | `MIN(salary)` | `35000` |
| `MAX()` | Largest value | `MAX(salary)` | `60000` |

### 1. COUNT()
```sql
SELECT COUNT(*) FROM employees;                    -- 6  (all rows)
SELECT COUNT(salary) FROM employees;               -- 5  (ignores NULL)
SELECT COUNT(DISTINCT department) FROM employees;  -- 3  (unique departments)
```

| `COUNT(*)` | `COUNT(column)` |
|---|---|
| Counts all rows, including NULL values | Counts only non-NULL values in that column |

### 2. SUM()
```sql
SELECT SUM(salary) AS total_salary FROM employees;   -- 230000
```

### 3. AVG()
```sql
SELECT AVG(salary) AS average_salary FROM employees;   -- 46000
```

> `AVG()` ignores NULL values: 230000 ÷ 5 = 46000 (not ÷ 6).

### 4. MIN() and MAX()
```sql
SELECT MIN(salary) AS lowest, MAX(salary) AS highest
FROM employees;
```

| lowest | highest |
|---|---|
| 35000 | 60000 |

> All aggregate functions except `COUNT(*)` **ignore NULL values**.

## GROUP BY

### Definition
`GROUP BY` **groups rows that have the same value** in a column, so an aggregate function can be calculated **for each group** separately.

### Syntax
```sql
SELECT column, AGGREGATE_FUNCTION(column)
FROM table_name
GROUP BY column;
```

### Example
```sql
SELECT department,
       COUNT(*) AS employees,
       SUM(salary) AS total_salary,
       AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

| department | employees | total_salary | avg_salary |
|---|---|---|---|
| HR | 2 | 85000 | 42500 |
| IT | 3 | 110000 | 55000 |
| Sales | 1 | 35000 | 35000 |

> **Rule:** Every column in `SELECT` that is **not** inside an aggregate function must be written in `GROUP BY`.

### GROUP BY with ORDER BY
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

| department | avg_salary |
|---|---|
| IT | 55000 |
| HR | 42500 |
| Sales | 35000 |

## HAVING

### Definition
`HAVING` is used to **filter groups** after `GROUP BY`, using aggregate functions.
`WHERE` cannot be used with aggregate functions, so `HAVING` is used instead.

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 40000;
```

| department | avg_salary |
|---|---|
| HR | 42500 |
| IT | 55000 |

### WHERE vs HAVING
| `WHERE` | `HAVING` |
|---|---|
| Filters **rows** before grouping | Filters **groups** after grouping |
| Cannot use aggregate functions | Used with aggregate functions |
| Written before `GROUP BY` | Written after `GROUP BY` |

```sql
SELECT department, COUNT(*) AS employees
FROM employees
WHERE salary > 36000          -- filter rows first
GROUP BY department
HAVING COUNT(*) >= 2;         -- then filter groups
```

| department | employees |
|---|---|
| HR | 2 |
| IT | 2 |

## Order of Clauses in a Query
```sql
SELECT     column, AGGREGATE(column)
FROM       table
WHERE      condition          -- filter rows
GROUP BY   column             -- make groups
HAVING     condition          -- filter groups
ORDER BY   column;            -- sort result
```

## Summary
| Concept | Purpose |
|---|---|
| `COUNT()` | Number of rows / values |
| `SUM()` | Total |
| `AVG()` | Average |
| `MIN()` / `MAX()` | Smallest / largest value |
| `GROUP BY` | Calculate aggregates for each group |
| `HAVING` | Filter groups using aggregate conditions |


## Key Takeaway
Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) summarise many rows into one value. `GROUP BY` applies them to each group, such as each department, and `HAVING` filters those groups. This is the SQL version of `groupby()` in Pandas, which I used in my project to find fraud rate and spending by merchant category.
