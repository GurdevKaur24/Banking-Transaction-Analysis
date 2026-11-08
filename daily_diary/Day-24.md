# Day 24 – Project Introduction and Data Sampling

## Topics Covered
- Project: Banking Transaction Pattern Analysis
- Problem statement and objectives
- Understanding the dataset
- Tools used
- Data sampling: first-N rows vs random sampling

## Project Introduction
For the final project of the training, I worked on **Banking Transaction Pattern Analysis**.
The aim is to study **how customers spend money** and **whether fraud follows any pattern**, using Python for analysis and Streamlit for an interactive dashboard.

## Problem Statement
Banks process a very large number of card transactions every day, and a small share of them are fraudulent.
The bank wants to understand spending behaviour and find out whether fraud is linked to **merchant category, time or transaction amount**, so it can improve monitoring and decision-making.

## Objectives
1. Clean and prepare the transaction data.
2. Understand spending patterns by merchant category, month and day of week.
3. Understand customer behaviour (how often customers transact, who spends the most).
4. Analyse fraud: how common it is and whether it is higher in any group.
5. Share findings, recommendations and limitations.
6. Build an interactive dashboard to explore the data.

## Dataset
**File:** `transactions.csv`
**Size:** 1,000,000 rows and 8 columns (about 79 MB)
**Period:** January to December 2023

| Column | Meaning |
|---|---|
| `transaction_id` | Unique ID of the transaction |
| `customer_id` | ID of the customer |
| `transaction_timestamp` | Date of the transaction |
| `amount` | Transaction amount ($) |
| `merchant_category` | electronics, fashion, gaming, groceries, travel |
| `is_fraud` | 1 = fraud, 0 = legitimate |
| `year`, `month` | Year and month of the transaction |

```python
import pandas as pd

full_df = pd.read_csv("transactions.csv")
print(full_df.shape)   # (1000000, 8)
full_df.head()
```

## Tools Used
| Tool | Purpose |
|---|---|
| **Python** | Main programming language |
| **Pandas, NumPy** | Loading, cleaning and analysing data |
| **Matplotlib, Seaborn** | Charts in the notebook |
| **Jupyter Notebook** | Step-by-step analysis (`main.ipynb`) |
| **Plotly, Streamlit** | Interactive dashboard (`dash.py`) |
| **Git, GitHub** | Version control and sharing the project |

## Data Sampling

### Why Sample?
The full dataset has 1 million rows. Working with a **sample of 100,000 rows** keeps the analysis and dashboard fast, while still giving reliable results.

### First Attempt: First 100,000 Rows
At first, I loaded only the first 100,000 rows:
```python
df = pd.read_csv("transactions.csv", nrows=100000)
```

**Problem found:** this sample only contained **May, October and December**.
The file is **not stored in date order**, so the first rows do not represent the whole year.

```python
print(full_df["month"].value_counts().sort_index())
```
The full dataset has **all 12 months** (about 77,000–85,000 transactions each), so the first-100k sample was **biased**. Any monthly trend from it would have been wrong.

### Solution: Random Sampling
A **random sample** picks rows from the whole file, so every month, category and customer group is fairly represented.

```python
# read the full dataset
full_df = pd.read_csv("transactions.csv")

# take a random sample of 100,000 rows
df = full_df.sample(n=100000, random_state=42)

# reset the row numbers to 0, 1, 2, ...
df = df.reset_index(drop=True)

print("Months in full data:", sorted(full_df["month"].unique().tolist()))
print("Months in sample   :", sorted(df["month"].unique().tolist()))
```
Output:
```
Months in full data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Months in sample   : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

- `n=100000` → number of rows to pick
- `random_state=42` → gives the **same sample every time** the code runs, so results can be repeated

```python
df.to_csv("transactions_sample.csv", index=False)
```

### First-N Rows vs Random Sample
| First-N rows (`nrows`) | Random sample (`sample()`) |
|---|---|
| Takes rows from the top of the file only | Takes rows from the whole file |
| Can be biased if the file is ordered or grouped | Represents the full data fairly |
| Only 3 months in this dataset | All 12 months |
| Faster to load | Needs the full file to be loaded first |


## Key Takeaway
A data project starts with a clear problem statement, objectives and an understanding of the dataset. While sampling, I learned that taking the first N rows can give a **biased sample**: my first sample had only 3 of the 12 months. Using a **random sample with a fixed `random_state`** fixed this and made the analysis represent the whole year.
