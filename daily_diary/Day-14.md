# Day 14 – Pandas

## Topics Covered
- Introduction to Pandas
- Series and DataFrame
- Common Pandas functions and methods and their purpose

## Introduction to Pandas
**Pandas** is a Python library used for **data analysis and data manipulation**.
It makes it easy to load, clean, explore, filter and summarise data in table form.

```python
import pandas as pd
```

`pd` is the short name (alias) commonly used for Pandas.

### Data Structures in Pandas
| Structure | Meaning | Example |
|---|---|---|
| **Series** | One-dimensional (a single column) with an index | `pd.Series([10, 20, 30])` |
| **DataFrame** | Two-dimensional table with rows and columns | `pd.DataFrame(data)` |

```python
s = pd.Series([10, 20, 30])
print(s)

data = {
    "name": ["Gurdev", "Ravi", "Simran", "Aman"],
    "age": [21, 22, 20, 23],
    "city": ["Ludhiana", "Amritsar", "Ludhiana", "Jalandhar"],
    "marks": [85, 72, 91, 60]
}
df = pd.DataFrame(data)
print(df)
```

## Pandas Functions / Methods and Their Purpose

### 1. Reading and Writing Data
| Function / Method | Purpose |
|---|---|
| `pd.read_csv("file.csv")` | Read data from a CSV file |
| `pd.read_excel("file.xlsx")` | Read data from an Excel file |
| `pd.read_json("file.json")` | Read data from a JSON file |
| `df.to_csv("file.csv", index=False)` | Save a DataFrame to a CSV file |
| `df.to_excel("file.xlsx", index=False)` | Save a DataFrame to an Excel file |

### 2. Viewing and Understanding Data
| Function / Method | Purpose |
|---|---|
| `df.head(n)` | Show the first `n` rows (default 5) |
| `df.tail(n)` | Show the last `n` rows (default 5) |
| `df.shape` | Number of rows and columns |
| `df.columns` | Names of all columns |
| `df.dtypes` | Data type of each column |
| `df.info()` | Summary: columns, data types, non-null counts, memory |
| `df.describe()` | Statistics for numeric columns (count, mean, std, min, max, quartiles) |
| `df.sample(n)` | Random `n` rows |

```python
print(df.head(2))
print(df.shape)       # (4, 4)
print(df.columns)
df.info()
print(df.describe())
```

### 3. Selecting Data
| Function / Method | Purpose |
|---|---|
| `df["col"]` | Select one column |
| `df[["col1", "col2"]]` | Select multiple columns |
| `df.loc[row, col]` | Select by **labels** (row index names, column names) |
| `df.iloc[row, col]` | Select by **position numbers** |

```python
print(df["name"])
print(df[["name", "marks"]])
print(df.loc[0, "name"])     # Gurdev
print(df.iloc[1, 0])         # Ravi
print(df.iloc[0:2])          # first two rows
```

### 4. Filtering Data
| Syntax | Purpose |
|---|---|
| `df[df["col"] > value]` | Rows that match a condition |
| `df[(cond1) & (cond2)]` | Rows matching both conditions (AND) |
| `df[(cond1) \| (cond2)]` | Rows matching either condition (OR) |
| `df[df["col"].isin([...])]` | Rows where the value is in a list |

```python
print(df[df["marks"] > 70])
print(df[(df["city"] == "Ludhiana") & (df["marks"] > 80)])
print(df[df["city"].isin(["Amritsar", "Jalandhar"])])
```

### 5. Handling Missing Values
| Function / Method | Purpose |
|---|---|
| `df.isnull()` / `df.isna()` | Shows True where values are missing |
| `df.isnull().sum()` | Count missing values in each column |
| `df.dropna()` | Remove rows with missing values |
| `df.fillna(value)` | Replace missing values with a given value |

```python
print(df.isnull().sum())
df["marks"] = df["marks"].fillna(df["marks"].mean())
```

### 6. Handling Duplicates
| Function / Method | Purpose |
|---|---|
| `df.duplicated()` | Shows True for duplicate rows |
| `df.duplicated().sum()` | Count duplicate rows |
| `df.drop_duplicates()` | Remove duplicate rows |

### 7. Modifying Data
| Function / Method | Purpose |
|---|---|
| `df["new_col"] = ...` | Add a new column |
| `df.drop(columns=["col"])` | Remove a column |
| `df.drop(index=[0])` | Remove a row |
| `df.rename(columns={"old": "new"})` | Rename columns |
| `df["col"].astype(type)` | Change the data type of a column |
| `df["col"].replace(old, new)` | Replace values |
| `df["col"].apply(function)` | Apply a function to every value in a column |
| `df["col"].map(dict)` | Replace values using a dictionary |
| `pd.to_datetime(df["col"])` | Convert a column to date/time type |

```python
df["grade"] = df["marks"].apply(lambda m: "Pass" if m >= 65 else "Fail")
df = df.rename(columns={"marks": "score"})
df = df.drop(columns=["grade"])
```

### 8. Sorting
| Function / Method | Purpose |
|---|---|
| `df.sort_values("col")` | Sort by a column (ascending) |
| `df.sort_values("col", ascending=False)` | Sort in descending order |
| `df.sort_index()` | Sort by index |

```python
print(df.sort_values("score", ascending=False))
```

### 9. Aggregation and Statistics
| Function / Method | Purpose |
|---|---|
| `sum()`, `mean()`, `median()` | Total, average, middle value |
| `min()`, `max()` | Smallest and largest value |
| `count()` | Number of non-missing values |
| `std()` | Standard deviation |
| `df["col"].unique()` | List of unique values |
| `df["col"].nunique()` | Number of unique values |
| `df["col"].value_counts()` | Count of each unique value |

```python
print(df["score"].mean())
print(df["city"].value_counts())
print(df["city"].nunique())   # 3
```

### 10. Grouping
| Function / Method | Purpose |
|---|---|
| `df.groupby("col")["col2"].mean()` | Group rows and calculate a value for each group |
| `df.groupby("col").agg({...})` | Apply different calculations to different columns |
| `pd.pivot_table(...)` | Create a summary table like Excel pivot tables |

```python
print(df.groupby("city")["score"].mean())
print(df.groupby("city").agg({"score": "mean", "age": "max"}))
```

### 11. Combining DataFrames
| Function / Method | Purpose |
|---|---|
| `pd.concat([df1, df2])` | Join DataFrames one below another (or side by side) |
| `pd.merge(df1, df2, on="col")` | Join two DataFrames using a common column (like SQL JOIN) |

## Summary
| Task | Common Functions |
|---|---|
| Load / save data | `read_csv()`, `read_excel()`, `to_csv()` |
| Explore | `head()`, `tail()`, `shape`, `info()`, `describe()` |
| Select | `df["col"]`, `loc[]`, `iloc[]` |
| Filter | Conditions with `&`, `\|`, `isin()` |
| Clean | `isnull()`, `dropna()`, `fillna()`, `drop_duplicates()` |
| Modify | `rename()`, `drop()`, `astype()`, `apply()`, `to_datetime()` |
| Sort | `sort_values()`, `sort_index()` |
| Summarise | `mean()`, `sum()`, `value_counts()`, `groupby()`, `pivot_table()` |
| Combine | `concat()`, `merge()` |


## Key Takeaway
Pandas is the main Python library for data analysis. With Series and DataFrames, and functions to load, explore, select, filter, clean, modify, sort, group and combine data, almost every step of a data analysis project can be done in Pandas. I used many of these functions in my banking transaction analysis project.
