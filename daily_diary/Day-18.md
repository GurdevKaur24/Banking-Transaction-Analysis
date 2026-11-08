# Day 18 – SQL Joins

## Topics Covered
- Joins: definition
- Types of joins and what they return

## Joins

### Definition
A **JOIN** is used to **combine rows from two or more tables** based on a **related column** between them, usually a primary key in one table and a foreign key in the other.

Joins are needed because data is usually split into separate tables to avoid repeating it.

### Syntax
```sql
SELECT columns
FROM table1
JOIN_TYPE table2
ON table1.common_column = table2.common_column;
```

## Sample Tables

**students**
| id | name | course_id |
|---|---|---|
| 1 | Gurdev | 101 |
| 2 | Ravi | 102 |
| 3 | Simran | 104 |
| 4 | Aman | NULL |

**courses**
| course_id | course_name |
|---|---|
| 101 | Python |
| 102 | SQL |
| 103 | Power BI |

Note: Simran's `course_id` 104 does not exist in `courses`, Aman has no course, and no student has taken Power BI (103).

## Types of Joins

| Join | What It Returns |
|---|---|
| **INNER JOIN** | Only rows that have a **match in both** tables |
| **LEFT JOIN** | **All rows from the left** table + matching rows from the right (NULL if no match) |
| **RIGHT JOIN** | **All rows from the right** table + matching rows from the left (NULL if no match) |
| **FULL OUTER JOIN** | **All rows from both** tables (NULL where there is no match) |
| **CROSS JOIN** | **Every row of one table combined with every row** of the other |
| **SELF JOIN** | A table **joined with itself** |

### 1. INNER JOIN
Returns only the rows where the value matches in **both** tables.

```sql
SELECT s.name, c.course_name
FROM students s
INNER JOIN courses c
ON s.course_id = c.course_id;
```

| name | course_name |
|---|---|
| Gurdev | Python |
| Ravi | SQL |

> `JOIN` written alone means `INNER JOIN`. `s` and `c` are **aliases** (short names) for the tables.

### 2. LEFT JOIN (LEFT OUTER JOIN)
Returns **all rows from the left table**, and the matching rows from the right table. If there is no match, the right side shows `NULL`.

```sql
SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c
ON s.course_id = c.course_id;
```

| name | course_name |
|---|---|
| Gurdev | Python |
| Ravi | SQL |
| Simran | NULL |
| Aman | NULL |

**Use:** find students who are **not enrolled** in any valid course.
```sql
SELECT s.name
FROM students s
LEFT JOIN courses c
ON s.course_id = c.course_id
WHERE c.course_id IS NULL;
```
Result: `Simran`, `Aman`

### 3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns **all rows from the right table**, and the matching rows from the left table. If there is no match, the left side shows `NULL`.

```sql
SELECT s.name, c.course_name
FROM students s
RIGHT JOIN courses c
ON s.course_id = c.course_id;
```

| name | course_name |
|---|---|
| Gurdev | Python |
| Ravi | SQL |
| NULL | Power BI |

### 4. FULL OUTER JOIN
Returns **all rows from both tables**. Where there is no match, the missing side shows `NULL`.

MySQL does **not** support `FULL OUTER JOIN` directly, so we combine a LEFT JOIN and a RIGHT JOIN using `UNION`:
```sql
SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.course_id

UNION

SELECT s.name, c.course_name
FROM students s
RIGHT JOIN courses c ON s.course_id = c.course_id;
```

| name | course_name |
|---|---|
| Gurdev | Python |
| Ravi | SQL |
| Simran | NULL |
| Aman | NULL |
| NULL | Power BI |

### 5. CROSS JOIN
Returns **every possible combination** of rows from both tables (Cartesian product). No `ON` condition is needed.

```sql
SELECT s.name, c.course_name
FROM students s
CROSS JOIN courses c;
```

Number of rows = rows in table 1 × rows in table 2 = **4 × 3 = 12 rows**

| name | course_name |
|---|---|
| Gurdev | Python |
| Gurdev | SQL |
| Gurdev | Power BI |
| Ravi | Python |
| ... | ... |

### 6. SELF JOIN
A table is **joined with itself**. Used when rows in a table are related to other rows in the **same** table, e.g. an employee and their manager.

**employees**
| emp_id | emp_name | manager_id |
|---|---|---|
| 1 | Harpreet | NULL |
| 2 | Gurdev | 1 |
| 3 | Ravi | 1 |
| 4 | Simran | 2 |

```sql
SELECT e.emp_name AS employee, m.emp_name AS manager
FROM employees e
JOIN employees m
ON e.manager_id = m.emp_id;
```

| employee | manager |
|---|---|
| Gurdev | Harpreet |
| Ravi | Harpreet |
| Simran | Gurdev |

> The same table is used twice with different aliases (`e` for employee, `m` for manager).

## Summary
| Join | Left Table Rows | Right Table Rows | Result in Example |
|---|---|---|---|
| INNER JOIN | Only matching | Only matching | 2 rows |
| LEFT JOIN | All | Only matching | 4 rows |
| RIGHT JOIN | Only matching | All | 3 rows |
| FULL OUTER JOIN | All | All | 5 rows |
| CROSS JOIN | Every combination | Every combination | 12 rows |
| SELF JOIN | Same table used twice | – | 3 rows |


## Key Takeaway
Joins combine data from multiple tables using a common column. INNER JOIN returns only matches, LEFT and RIGHT JOIN keep all rows from one side, FULL OUTER JOIN keeps all rows from both sides (using `UNION` in MySQL), CROSS JOIN returns every combination, and SELF JOIN connects a table to itself. Joins are one of the most important SQL skills for data analysis.
