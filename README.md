# 🏦 Banking Transaction Pattern Analysis

A data analytics training project that studies **customer spending patterns** and **fraud trends** in banking transactions, with an interactive **Streamlit dashboard**.

## Problem Statement
Banks process many card transactions every day, and a small share are fraudulent. This project explores how customers spend money and whether fraud follows any pattern by merchant category, time, or amount.

## Dataset
- `transactions.csv`: 1,000,000 transactions from 2023
- Columns: `transaction_id`, `customer_id`, `transaction_timestamp`, `amount`, `merchant_category`, `is_fraud`, `year`, `month`
- A **random sample of 100,000 rows** (`random_state=42`) is used for the analysis and dashboard.

## Project Files
| File | Description |
|---|---|
| `main.ipynb` | Data cleaning, exploratory analysis, fraud analysis, findings and conclusion |
| `dash.py` | Interactive Streamlit dashboard |
| `transactions.csv` | Original dataset (1M rows) |
| `transactions_sample.csv` | Random 100k sample (created by the notebook) |
| `cleaned_transactions.csv` | Cleaned data with extra columns, used by the dashboard (created by the notebook) |
| `.streamlit/config.toml` | Dashboard theme (dark, orange/red) |

## Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit, Jupyter Notebook

## How to Run
```bash
pip install -r requirements.txt

# 1. run the analysis (creates the sample and cleaned CSV files)
jupyter notebook main.ipynb

# 2. launch the dashboard
streamlit run dash.py
```

## Key Findings
- **2,994 of 100,000 transactions (2.99%) are fraud.**
- The 5 merchant categories (electronics, fashion, gaming, groceries, travel) each have about 20% of transactions and an average transaction of about $500.
- **Groceries has the highest fraud rate (3.24%)** and travel the lowest (2.81%), but the gap is small.
- The fraud rate stays between about 2.8% and 3.4% for every month, weekday and amount range, and fraud and legitimate transactions have almost the same average amount (\$501.60 vs \$500.40).
- 62% of customers made more than one transaction, and the top spenders are the most frequent customers.

## Recommendations
1. Simple rules (e.g. "flag large payments") would not catch fraud well in this data.
2. Monitor each customer against their own normal behaviour.
3. Add extra checks for the highest-risk category (groceries) as a starting point.
4. Collect richer data (time of day, location, device) to build a fraud prediction model.

## Limitations
- The data appears synthetic (amounts are spread evenly from \$0 to \$1,000).
- Every timestamp is at 00:00, so time-of-day patterns cannot be studied.
- Only one year (2023) of data.
- The analysis uses a 10% random sample.

## Dashboard Features
- KPI cards: transactions, customers, total and average amount, fraud cases, fraud rate
- Filters: merchant category, fraud status, month, amount range
- Charts: category distribution, fraud split, fraud rate by category, amount range and month, top customers, amount distribution, monthly and weekday trends
- Business insights, recommendations, filtered data table and CSV download
