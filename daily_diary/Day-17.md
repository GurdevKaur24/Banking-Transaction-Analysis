# Day 17 – SQL: Types of SQL Commands

## Topics Covered
- Introduction to SQL
- Types of SQL commands: DDL, DML, DQL, DCL, TCL

## Introduction to SQL
**SQL (Structured Query Language)** is a language used to **store, manage and retrieve data** in a **relational database**.
In a relational database, data is stored in **tables** made of **rows (records)** and **columns (fields)**.

**MySQL** is a popular database management system that uses SQL.

> SQL keywords are not case-sensitive (`SELECT` and `select` both work), but writing keywords in CAPITAL letters makes queries easier to read. Each query ends with a semicolon `;`.

## Types of SQL Commands

| Type | Full Form | Purpose | Commands |
|---|---|---|---|
| **DDL** | Data Definition Language | Create and change the **structure** of database objects | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML** | Data Manipulation Language | Add, change and delete **data** in tables | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | **Retrieve** data from tables | `SELECT` |
| **DCL** | Data Control Language | Control **access and permissions** | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manage **transactions** (save or undo changes) | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

## 1. DDL – Data Definition Language
DDL commands define and change the **structure** of the database (databases, tables, columns).
DDL changes are **saved automatically (auto-commit)** and cannot be undone with `ROLLBACK`.

| Command | Purpose |
|---|---|
| `CREATE` | Create a database or table |
| `ALTER` | Change table structure (add, modify or drop a column) |
| `DROP` | Delete a whole database or table (structure + data) |
| `TRUNCATE` | Delete all rows but keep the table structure |
| `RENAME` | Rename a table |

```sql
CREATE DATABASE college;
USE college;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

ALTER TABLE students ADD email VARCHAR(100);
ALTER TABLE students MODIFY name VARCHAR(100);
ALTER TABLE students DROP COLUMN email;

RENAME TABLE students TO student_details;

TRUNCATE TABLE student_details;

DROP TABLE student_details;
```

## 2. DML – Data Manipulation Language
DML commands work with the **data inside tables**.

| Command | Purpose |
|---|---|
| `INSERT` | Add new rows |
| `UPDATE` | Change existing data |
| `DELETE` | Remove rows |

```sql
INSERT INTO students (id, name, age, city)
VALUES (1, 'Gurdev', 21, 'Ludhiana');

INSERT INTO students VALUES
(2, 'Ravi', 22, 'Amritsar'),
(3, 'Simran', 20, 'Jalandhar');

UPDATE students
SET city = 'Patiala'
WHERE id = 2;

DELETE FROM students
WHERE id = 3;
```

> **Important:** Always use `WHERE` with `UPDATE` and `DELETE`. Without it, **every row** in the table is changed or deleted.

## 3. DQL – Data Query Language
DQL is used to **fetch data** from tables using `SELECT`.

```sql
SELECT * FROM students;

SELECT name, city FROM students;

SELECT * FROM students
WHERE age > 20;

SELECT * FROM students
ORDER BY age DESC;
```

> Some books include `SELECT` under DML, but it is commonly treated as a separate category, DQL.

## 4. DCL – Data Control Language
DCL commands give or remove **permissions** for database users.

| Command | Purpose |
|---|---|
| `GRANT` | Give permissions to a user |
| `REVOKE` | Take back permissions from a user |

```sql
GRANT SELECT, INSERT ON college.students TO 'analyst'@'localhost';

REVOKE INSERT ON college.students FROM 'analyst'@'localhost';
```

## 5. TCL – Transaction Control Language
A **transaction** is a group of SQL statements that should be completed together as one unit.
TCL commands control whether changes are **saved** or **undone**.

| Command | Purpose |
|---|---|
| `START TRANSACTION` | Begin a transaction |
| `COMMIT` | Save all changes permanently |
| `ROLLBACK` | Undo changes since the last commit (or savepoint) |
| `SAVEPOINT` | Create a point inside a transaction to roll back to |

```sql
START TRANSACTION;

UPDATE students SET age = 23 WHERE id = 1;
SAVEPOINT sp1;

DELETE FROM students WHERE id = 2;

ROLLBACK TO sp1;   -- undoes the DELETE, keeps the UPDATE

COMMIT;            -- saves the UPDATE permanently
```

**Real-life example:** In a bank transfer, money is taken from one account and added to another. Both steps must succeed together. If one fails, `ROLLBACK` undoes everything so no money is lost.

## DELETE vs TRUNCATE vs DROP
| | `DELETE` | `TRUNCATE` | `DROP` |
|---|---|---|---|
| Type | DML | DDL | DDL |
| What it removes | Selected rows (with `WHERE`) or all rows | All rows | Whole table (data + structure) |
| Table structure | Kept | Kept | Removed |
| `WHERE` allowed | Yes | No | No |
| Can be rolled back | Yes (inside a transaction) | No | No |
| Speed | Slower | Faster | Fastest |

## Summary
| Type | Works On | Commands |
|---|---|---|
| DDL | Structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| DML | Data | `INSERT`, `UPDATE`, `DELETE` |
| DQL | Fetching data | `SELECT` |
| DCL | Permissions | `GRANT`, `REVOKE` |
| TCL | Transactions | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |


## Key Takeaway
SQL commands are grouped into five types: DDL defines table structure, DML changes data, DQL fetches data, DCL controls permissions and TCL manages transactions. Knowing which type a command belongs to helps in understanding what it does and whether its changes can be undone.
