# Day 25 – Data Cleaning

## Topics Covered
- Importance of data cleaning
- Checking data overview (`info()`, `describe()`)
- Missing values
- Duplicate rows and duplicate IDs
- Invalid values
- Converting data types (datetime)
- Creating new columns (feature engineering)
- Saving the cleaned data

## Why Data Cleaning?
Raw data can contain missing values, duplicates, wrong data types or invalid values.
If these are not fixed, the analysis can give **wrong results**. Data cleaning makes sure the data is **correct, consistent and ready for analysis**.

> Even when the data is already clean, **checking** it and writing down the results is part of data cleaning.

## 1. Data Overview
```python
print("Rows and Columns:", df.shape)   # (100000, 8)
df.info()
df.describe()
```

**Findings:**
- 100,000 rows and 8 columns
- `transaction_timestamp` was stored as **text (str)**, not as a date
- `amount` ranges from almost $0 to about $1,000, with mean ≈ median ≈ $500

## 2. Missing Values
```python
df.isnull().sum()
```
**Result:** 0 missing values in every column, so no action was needed.

## 3. Duplicates
```python
# completely identical rows
duplicate_rows = df.duplicated().sum()

# the same transaction_id used more than once
duplicate_ids = df["transaction_id"].duplicated().sum()

print("Duplicate rows           :", duplicate_rows)
print("Duplicate transaction IDs:", duplicate_ids)
```
Output:
```
Duplicate rows           : 0
Duplicate transaction IDs: 0
```

> `df.duplicated()` only finds rows where **every** column is the same. Checking `transaction_id` separately is important, because two rows with the same ID but different values would not be caught otherwise.

## 4. Invalid Values
```python
# an amount of 0 or less is not a valid transaction
invalid_amounts = (df["amount"] <= 0).sum()

print("Amounts <= 0:", invalid_amounts)
print("Smallest amount:", round(df["amount"].min(), 4))
print("Largest amount :", round(df["amount"].max(), 2))
```
Output:
```
Amounts <= 0: 0
Smallest amount: 0.0019
Largest amount : 999.99
```

```python
print("Merchant categories:", df["merchant_category"].unique())
print("is_fraud values:", df["is_fraud"].unique())
print("Customer ID range:", df["customer_id"].min(), "to", df["customer_id"].max())
print("Years:", df["year"].unique())
```
**Results:**
- 5 clean category names with no spelling mistakes or extra spaces: electronics, fashion, gaming, groceries, travel
- `is_fraud` has only 0 and 1
- Customer IDs range from 2 to 59999
- `year` is always **2023**, so the column is constant and not useful for analysis

## 5. Converting Data Types
The timestamp column was converted from text to **datetime**, so dates can be used for analysis.
```python
df["transaction_timestamp"] = pd.to_datetime(df["transaction_timestamp"])

print(df["transaction_timestamp"].dtype)
print("First date:", df["transaction_timestamp"].min())
print("Last date :", df["transaction_timestamp"].max())
```
Output:
```
datetime64[us, UTC+02:00]
First date: 2023-01-01 00:00:00+02:00
Last date : 2023-12-31 00:00:00+02:00
```

### Checking Time of Day
```python
hours = df["transaction_timestamp"].dt.hour.unique()
print("Hours found in the data:", hours)   # [0]
```
**Finding:** every transaction is at **00:00**, so the data has only the **date**, not the time. Hour-of-day analysis is not possible.

## 6. Creating New Columns
New columns were created to make analysis easier.

```python
# day number, month name and weekday name from the date
df["day"] = df["transaction_timestamp"].dt.day
df["month_name"] = df["transaction_timestamp"].dt.month_name()
df["day_name"] = df["transaction_timestamp"].dt.day_name()

# readable fraud label
df["fraud_status"] = df["is_fraud"].map({0: "Legitimate", 1: "Fraud"})

# group amounts into ranges
bins = [0, 100, 250, 500, 750, 1000]
labels = ["$0-100", "$100-250", "$250-500", "$500-750", "$750-1000"]
df["amount_range"] = pd.cut(df["amount"], bins=bins, labels=labels)
```

| New Column | Created From | Purpose |
|---|---|---|
| `day` | timestamp | Day of the month |
| `month_name` | timestamp | Monthly analysis (January, February, ...) |
| `day_name` | timestamp | Weekday analysis (Monday, Tuesday, ...) |
| `fraud_status` | `is_fraud` | Readable labels for charts |
| `amount_range` | `amount` | Compare small vs large transactions |

> `pd.cut()` divides numbers into ranges (bins). Here, an amount of 274 goes into `$250-500`.

## 7. Saving the Cleaned Data
```python
df.to_csv("cleaned_transactions.csv", index=False)
print("Cleaned data saved:", df.shape)   # (100000, 13)
```
The cleaned file is used by the Streamlit dashboard.

## Cleaning Summary
| Check | Result | Action |
|---|---|---|
| Missing values | None | No action needed |
| Duplicate rows / transaction IDs | 0 / 0 | No action needed |
| Amounts ≤ 0 | 0 | No action needed |
| Category spelling | 5 clean categories | No action needed |
| `is_fraud` values | Only 0 and 1 | No action needed |
| Timestamp type | Text | Converted to datetime |
| Time of day | Every transaction at 00:00 | Only the date is usable |
| `year` | Always 2023 | Kept, but not useful |
| New columns | – | Added 5 columns (8 → 13 columns) |


## Key Takeaway
Data cleaning means checking for missing values, duplicates, invalid values and wrong data types, then fixing what is needed. My data was already quite clean, so most of the work was **verifying** it and **adding useful columns** like month name, day name, fraud label and amount range. I also learned to check duplicate IDs separately and to notice limitations, such as all timestamps being at midnight.
