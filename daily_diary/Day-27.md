# Day 27 – Fraud Analysis, Findings and Recommendations

## Topics Covered
- Fraud count vs fraud rate
- Fraud rate by merchant category, month, weekday and amount range
- Average amount: fraud vs legitimate
- Key findings
- Recommendations
- Limitations and conclusion

## Fraud Count vs Fraud Rate
At first, I compared fraud using **counts** (number of fraud transactions in each group).
But a group with more transactions will naturally have more fraud, so counts can be misleading.

**Fraud rate** is the fairer measure:

```
Fraud rate (%) = fraud transactions ÷ all transactions in the group × 100
```

In Pandas, the **mean of a 0/1 column** gives the share of 1s, so:
```python
fraud_rate = df["is_fraud"].mean() * 100
```

## 1. Overall Fraud
```python
fraud = df["fraud_status"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(fraud, labels=fraud.index, autopct="%1.2f%%", startangle=90, colors=[ORANGE, RED])
plt.title("Fraud vs Legitimate Transactions")
plt.show()
```

| Status | Transactions | Share |
|---|---|---|
| Legitimate | 97,006 | 97.01% |
| Fraud | 2,994 | 2.99% |

**Observation:** About **3 in every 100 transactions** are fraud. Fraud is rare, but at bank scale this is still a large number of cases.

## 2. Fraud Rate by Merchant Category
```python
fraud_rate_category = df.groupby("merchant_category")["is_fraud"].mean() * 100
fraud_rate_category = fraud_rate_category.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(fraud_rate_category.index, fraud_rate_category.values, color=RED)
plt.axhline(fraud_rate, color="black", linestyle="--", label=f"Overall rate ({fraud_rate:.2f}%)")
plt.title("Fraud Rate by Merchant Category")
plt.ylabel("Fraud Rate (%)")
plt.legend()
plt.show()
```

| Category | Fraud Rate |
|---|---|
| groceries | 3.24% |
| electronics | 2.98% |
| fashion | 2.98% |
| gaming | 2.96% |
| travel | 2.81% |

> `plt.axhline()` draws a dashed line at the overall rate, which makes it easy to see which groups are above or below average.

**Observation:** **Groceries has the highest fraud rate (3.24%)** and **travel the lowest (2.81%)**. All categories are close to the overall 2.99%, so category alone is only a **weak** fraud signal.

## 3. Fraud Rate by Month
```python
fraud_rate_month = df.groupby("month_name")["is_fraud"].mean() * 100
fraud_rate_month = fraud_rate_month.reindex(month_order)
```

**Observation:** The fraud rate moves between **2.76% (May)** and **3.39% (March)**. There is no steady rise or fall and no clear "fraud season".

## 4. Fraud Rate by Day of Week
```python
fraud_rate_day = df.groupby("day_name")["is_fraud"].mean() * 100
fraud_rate_day = fraud_rate_day.reindex(day_order)
```

| Day | Fraud Rate |
|---|---|
| Monday | 2.91% |
| Tuesday | 3.29% |
| Wednesday | 2.82% |
| Thursday | 3.11% |
| Friday | 3.02% |
| Saturday | 2.96% |
| Sunday | 2.86% |

**Observation:** **Tuesday has the highest fraud rate (3.29%)** and Wednesday the lowest (2.82%). Weekends are not riskier than weekdays.

## 5. Fraud Rate by Amount Range
```python
fraud_rate_amount = df.groupby("amount_range", observed=True)["is_fraud"].mean() * 100
```

| Amount Range | Fraud Rate |
|---|---|
| $0-100 | 2.91% |
| $100-250 | 2.99% |
| $250-500 | 3.00% |
| $500-750 | 2.98% |
| $750-1000 | 3.03% |

**Observation:** The fraud rate is almost the same for small and large payments. Large transactions are **not** more likely to be fraud in this data.

## 6. Average Amount: Fraud vs Legitimate
```python
avg_by_status = df.groupby("fraud_status")["amount"].mean()
```

| Status | Average Amount |
|---|---|
| Fraud | $501.60 |
| Legitimate | $500.40 |

**Observation:** Practically the same. Fraudsters in this data do not use unusually large or small amounts.

## Key Findings
1. **Balanced spending:** The 5 categories each have ~20% of transactions and ~$10M in spending, with an average of ~$500.
2. **Steady over time:** Transactions are spread evenly across the year; February is lowest only because it is shorter. Sunday is the busiest day, but only slightly.
3. **Frequent customers = top spenders:** 62% of customers are repeat customers, and the top spenders are those with the most transactions.
4. **Fraud rate is about 3%:** 2,994 of 100,000 transactions are fraud.
5. **Groceries is the riskiest category (3.24%)**, travel the safest (2.81%), but the gap is small.
6. **Fraud does not depend strongly on time or amount:** the fraud rate stays between ~2.8% and ~3.4% for every month, weekday and amount range.

## Recommendations
1. **Don't rely on simple rules** like "flag large transactions" or "flag one category". In this data they would miss most fraud and flag many honest customers.
2. **Monitor customer behaviour:** compare each transaction with that customer's own normal pattern (sudden change in frequency, category or amount).
3. **Give slightly more attention to groceries** and to higher-fraud periods (March, Tuesdays) as a starting point.
4. **Collect richer data** such as time of day, location, device and merchant ID, which are usually strong fraud signals.
5. **Build a fraud prediction model** as a next step once richer features are available.

## Limitations
- The data looks **synthetic**: amounts are spread evenly and all groups look very similar, so real-world patterns may be stronger.
- **No time of day:** every timestamp is 00:00, so hourly patterns (e.g. night-time fraud) cannot be studied.
- Only **one year (2023)** of data, so year-over-year trends cannot be checked.
- The analysis uses a **random 10% sample** (100,000 of 1,000,000 rows). Overall rates are reliable, but per-customer counts are lower than in the full data.
- Only 5 merchant categories, and no location or device information.

## Conclusion
About **3% of transactions are fraud**, and the fraud rate is similar across categories, time and amount. Groceries is slightly higher, but no single factor clearly identifies fraud. This shows that fraud detection needs **customer-level behaviour analysis and richer data**, not just simple rules.


## Key Takeaway
I learned to compare groups using **rates instead of counts**, and to use a reference line for the overall rate to judge each group fairly. Even when the result is "no strong pattern", that is still a valid finding. Writing honest findings, practical recommendations and clear limitations is what turns analysis into useful business insight.
