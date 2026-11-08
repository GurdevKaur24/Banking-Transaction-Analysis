# Day 26 – Exploratory Data Analysis (EDA)

## Topics Covered
- What is EDA
- Key numbers (KPIs)
- Spending patterns by merchant category
- Transaction amount distribution
- Time patterns (month and weekday)
- Customer behaviour (transactions per customer, top spenders)
- Writing observations under each chart

## What is EDA?
**Exploratory Data Analysis (EDA)** is the process of **exploring data using statistics and charts** to understand its main features, find patterns and spot anything unusual, before drawing conclusions.

In my project, every chart is followed by an **Observation**, a short note explaining what the chart shows.

## 1. Key Numbers
```python
total_transactions = len(df)
unique_customers = df["customer_id"].nunique()
total_amount = df["amount"].sum()
average_amount = df["amount"].mean()
fraud_count = df["is_fraud"].sum()
fraud_rate = df["is_fraud"].mean() * 100
```

| KPI | Value |
|---|---|
| Total transactions | 100,000 |
| Unique customers | 48,630 |
| Total transaction amount | $50,043,351 |
| Average transaction amount | $500.43 |
| Fraud transactions | 2,994 |
| Fraud rate | 2.99% |

## 2. Merchant Categories

### Transactions by Category
```python
category_count = df["merchant_category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_count.index, category_count.values, color=COLORS)
plt.title("Number of Transactions by Merchant Category")
plt.xlabel("Merchant Category")
plt.ylabel("Transaction Count")
plt.show()
```

| Category | Transactions | Total Amount | Average Amount |
|---|---|---|---|
| electronics | 20,079 | $10,004,588 | $498.26 |
| fashion | 19,995 | $9,996,709 | $499.96 |
| gaming | 19,999 | $10,066,655 | $503.36 |
| groceries | 19,966 | $9,940,813 | $497.89 |
| travel | 19,961 | $10,034,587 | $502.71 |

**Observations:**
- All 5 categories have almost the same number of transactions (about 20% each).
- Total spending is about **$10 million per category**. Gaming is slightly highest and groceries slightly lowest, but the difference is less than 1.5%.
- The average transaction is about **$500 in every category**.

## 3. Transaction Amounts
```python
plt.figure(figsize=(8, 5))
sns.histplot(df["amount"], bins=30, color=ORANGE)
plt.title("Distribution of Transaction Amount")
plt.show()

plt.figure(figsize=(8, 3))
sns.boxplot(x=df["amount"], color=ORANGE)
plt.title("Boxplot of Transaction Amount")
plt.show()
```

**Observations:**
- The histogram is almost **flat**: every amount between $0 and $1,000 is about equally common.
- Real banking data usually has many small payments and few large ones, so this flat shape suggests the dataset is **synthetic (computer-generated)**.
- The box plot shows **no outliers**, so no amounts needed to be removed.

## 4. Time Patterns

### Transactions per Month
```python
month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

monthly = df["month_name"].value_counts()
monthly = monthly.reindex(month_order)

plt.figure(figsize=(11, 5))
plt.bar(monthly.index, monthly.values, color=ORANGE)
plt.title("Transactions per Month")
plt.xticks(rotation=45)
plt.show()
```

> `reindex(month_order)` puts the months in **calendar order**. Without it, they would be sorted by count or alphabetically.

**Observation:** Activity is steady all year (about 8,100–8,600 per month). **February is lowest (7,678)** mainly because it has only 28 days, while 31-day months like May (8,614) and October (8,573) are among the highest.

### Transactions by Day of Week
```python
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_count = df["day_name"].value_counts()
day_count = day_count.reindex(day_order)
```

| Day | Transactions |
|---|---|
| Monday | 14,077 |
| Tuesday | 14,179 |
| Wednesday | 14,076 |
| Thursday | 14,377 |
| Friday | 14,221 |
| Saturday | 14,373 |
| Sunday | 14,697 |

**Observation:** **Sunday is the busiest day (14,697)**, but only about 4% above the quietest days (Monday and Wednesday). There is no strong weekday vs weekend difference.

## 5. Customer Behaviour

### Transactions per Customer
```python
# how many transactions does each customer have?
transactions_per_customer = df["customer_id"].value_counts()

# how many customers have 1 transaction, 2 transactions, ...
customer_groups = transactions_per_customer.value_counts().sort_index()

repeat_customers = (transactions_per_customer > 1).sum()
repeat_percent = repeat_customers / len(transactions_per_customer) * 100
print("Customers with more than 1 transaction:", repeat_customers, f"({repeat_percent:.1f}%)")
```
Output:
```
Customers with more than 1 transaction: 29934 (61.6%)
```

| Transactions per customer | Number of customers |
|---|---|
| 1 | 18,696 |
| 2 | 15,955 |
| 3 | 8,704 |
| 4 | 3,655 |
| 5 | 1,186 |
| 6+ | 434 |

**Observation:** Most customers have **1–3 transactions** in the sample, and about **62% are repeat customers**. (In the full 1M-row data, each customer has about 17 transactions on average. The sample shows fewer because it keeps only 10% of rows.)

### Top 10 Customers by Spending
```python
customer_total = df.groupby("customer_id")["amount"].sum()
top_customers = customer_total.sort_values(ascending=False).head(10)

top_table = pd.DataFrame({
    "total_amount": top_customers.round(2),
    "transactions": transactions_per_customer[top_customers.index]
})
```

**Observation:** The top 10 customers each spent about **$4,700–$5,600**, and they all have **6–8 transactions**, compared to 1–3 for a typical customer. So top spenders are mainly the **most frequent** customers, not people making unusually large purchases.

## Pandas Methods Used for EDA
| Method | Used For |
|---|---|
| `value_counts()` | Count of each category, month, day |
| `groupby().sum()` / `.mean()` | Total and average per group |
| `nunique()` | Number of unique customers |
| `reindex()` | Put months and days in the correct order |
| `sort_values().head(10)` | Top 10 customers |


## Key Takeaway
EDA helped me understand the data before drawing conclusions. Spending is evenly spread across categories, months and weekdays; amounts are spread evenly from $0 to $1,000 (a sign of synthetic data); and top spenders are the most frequent customers. I learned that writing an **observation under every chart** turns charts into actual insights.
