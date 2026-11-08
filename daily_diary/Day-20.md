# Day 20 – Connecting MySQL with Python

## Topics Covered
- Why connect MySQL with Python
- Installing the MySQL connector
- Connecting Python to a MySQL database
- Running MySQL queries in Python (CREATE, INSERT, SELECT, UPDATE, DELETE)
- Loading SQL data into Pandas

## Why Connect MySQL with Python?
- Databases store large amounts of data, and Python is used to **analyse** it.
- Connecting them lets us **run SQL queries from Python**, get the results, and then analyse or visualise them with **Pandas, Matplotlib and Seaborn**.
- It also lets programs **insert or update data** in the database automatically.

## Step 1: Install the MySQL Connector
```bash
pip install mysql-connector-python
```

## Step 2: Connect to MySQL
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

if conn.is_connected():
    print("Connected to MySQL")
```

| Parameter | Meaning |
|---|---|
| `host` | Where the MySQL server is running (`localhost` = own computer) |
| `user` | MySQL username |
| `password` | MySQL password |
| `database` | Name of the database to use (optional) |

## Step 3: Create a Cursor
A **cursor** is an object used to **execute SQL queries** and **fetch results**.
```python
cursor = conn.cursor()
```

## Step 4: Run Queries

### Create a Database and Table
```python
cursor.execute("CREATE DATABASE IF NOT EXISTS college")
cursor.execute("USE college")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        city VARCHAR(50)
    )
""")
print("Table created")
```

### Insert Data
```python
query = "INSERT INTO students (id, name, age, city) VALUES (%s, %s, %s, %s)"
values = (1, "Gurdev", 21, "Ludhiana")

cursor.execute(query, values)
conn.commit()      # save changes
print(cursor.rowcount, "row inserted")
```

Insert many rows at once with `executemany()`:
```python
query = "INSERT INTO students (id, name, age, city) VALUES (%s, %s, %s, %s)"
values = [
    (2, "Ravi", 22, "Amritsar"),
    (3, "Simran", 20, "Jalandhar"),
    (4, "Aman", 23, "Ludhiana")
]

cursor.executemany(query, values)
conn.commit()
print(cursor.rowcount, "rows inserted")   # 3 rows inserted
```

> `%s` are **placeholders**. Values are passed separately, which is safer than joining them into the query string, because it protects against **SQL injection**.

### Select (Fetch) Data
```python
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()
for row in rows:
    print(row)
```
Output:
```
(1, 'Gurdev', 21, 'Ludhiana')
(2, 'Ravi', 22, 'Amritsar')
(3, 'Simran', 20, 'Jalandhar')
(4, 'Aman', 23, 'Ludhiana')
```

| Method | Returns |
|---|---|
| `fetchall()` | All rows (list of tuples) |
| `fetchone()` | Only the next one row |
| `fetchmany(n)` | Next `n` rows |

With a condition:
```python
cursor.execute("SELECT name, age FROM students WHERE city = %s", ("Ludhiana",))
print(cursor.fetchall())   # [('Gurdev', 21), ('Aman', 23)]
```

> A single value must still be passed as a tuple, so it needs a comma: `("Ludhiana",)`.

### Update Data
```python
cursor.execute("UPDATE students SET city = %s WHERE id = %s", ("Patiala", 2))
conn.commit()
print(cursor.rowcount, "row updated")
```

### Delete Data
```python
cursor.execute("DELETE FROM students WHERE id = %s", (4,))
conn.commit()
print(cursor.rowcount, "row deleted")
```

### Aggregate Query
```python
cursor.execute("SELECT city, COUNT(*) FROM students GROUP BY city")
for city, total in cursor.fetchall():
    print(city, total)
```

## Step 5: Close the Connection
```python
cursor.close()
conn.close()
print("Connection closed")
```

## Loading SQL Data into Pandas
Query results can be loaded straight into a DataFrame for analysis.
```python
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

df = pd.read_sql("SELECT * FROM students", conn)
print(df)

conn.close()
```

> Pandas may show a warning recommending SQLAlchemy for connections, but `read_sql()` still works with `mysql.connector`.

## Important Points
| Point | Reason |
|---|---|
| Use `conn.commit()` after `INSERT`, `UPDATE`, `DELETE` | Otherwise changes are not saved |
| Use `%s` placeholders | Safer (prevents SQL injection) and handles quotes correctly |
| Always close the cursor and connection | Frees database resources |
| `SELECT` does not need `commit()` | It only reads data |

## Full Workflow
```
Install connector → Connect → Create cursor → Execute query → Commit / Fetch results → Close
```

## Key Takeaway
Using `mysql-connector-python`, Python can connect to a MySQL database, run any SQL query through a cursor, save changes with `commit()`, and fetch results with `fetchall()`. Loading the results into Pandas with `read_sql()` joins the power of SQL for storing data with Python for analysing and visualising it.
