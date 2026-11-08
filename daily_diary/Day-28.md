# Day 28 – Plotly and Streamlit Dashboard

## Topics Covered
- Introduction to Streamlit
- Introduction to Plotly Express
- Page setup and loading data with caching
- Sidebar filters
- Filtering data based on user selection
- KPI metrics
- Layout with columns
- Interactive charts
- Data table and CSV download

## Introduction to Streamlit
**Streamlit** is a Python library used to build **interactive web apps and dashboards** using only Python, with no HTML, CSS or JavaScript needed.
Every time the user changes a filter, Streamlit **re-runs the script from top to bottom** and updates the page.

```bash
pip install streamlit
streamlit run dash.py
```
The dashboard opens in the browser at `http://localhost:8501`.

## Introduction to Plotly Express
**Plotly Express** creates **interactive charts**: hover to see values, zoom, and click legends to hide or show data.
It works directly with DataFrame column names, like Seaborn.

```python
import plotly.express as px
```

| Matplotlib / Seaborn | Plotly |
|---|---|
| Static images | Interactive charts (hover, zoom) |
| Best for notebooks and reports | Best for dashboards and web apps |

## 1. Page Setup and Loading Data
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Banking Transaction Dashboard",
    page_icon="🏦",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_transactions.csv")
    return df

df = load_data()

st.title("Banking Transaction Pattern Analysis Dashboard")
```

| Code | Purpose |
|---|---|
| `st.set_page_config()` | Sets page title, icon and wide layout |
| `@st.cache_data` | Loads the CSV **only once** and reuses it, so the app stays fast when filters change |
| `st.title()` | Main heading of the page |

## 2. Sidebar Filters
Widgets placed in `st.sidebar` appear in a panel on the left.

```python
st.sidebar.header("Dashboard Filters")

category = st.sidebar.multiselect(
    "Merchant Category",
    options=sorted(df["merchant_category"].unique()),
    default=sorted(df["merchant_category"].unique())
)

fraud = st.sidebar.multiselect(
    "Fraud Status",
    options=sorted(df["fraud_status"].unique()),
    default=sorted(df["fraud_status"].unique())
)

amount_range = st.sidebar.slider(
    "Transaction Amount",
    float(df["amount"].min()),
    float(df["amount"].max()),
    (float(df["amount"].min()), float(df["amount"].max()))
)
```

| Widget | Purpose |
|---|---|
| `st.multiselect()` | Choose one or more options from a list |
| `st.slider()` | Choose a number or a range of numbers |
| `st.selectbox()` | Choose a single option |

## 3. Filtering the Data
The user's choices are used to filter the DataFrame. All KPIs and charts use `filtered_df`.

```python
filtered_df = df[
    (df["merchant_category"].isin(category)) &
    (df["fraud_status"].isin(fraud)) &
    (df["amount"] >= amount_range[0]) &
    (df["amount"] <= amount_range[1])
]
```

## 4. KPI Metrics
```python
total_transactions = len(filtered_df)
total_amount = filtered_df["amount"].sum()
fraud_transactions = (filtered_df["fraud_status"] == "Fraud").sum()

if total_transactions > 0:
    fraud_percentage = fraud_transactions / total_transactions * 100
else:
    fraud_percentage = 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Transactions", f"{total_transactions:,}")
c2.metric("Total Amount", f"${total_amount:,.2f}")
c3.metric("Fraud", f"{fraud_transactions:,}")
c4.metric("Fraud %", f"{fraud_percentage:.2f}%")
```

> The `if` check avoids a **division by zero** error when the filters leave no rows.

## 5. Layout with Columns
`st.columns()` splits the page into side-by-side sections.

```python
left, right = st.columns(2)

with left:
    st.subheader("Merchant Category Distribution")
    # chart here

with right:
    st.subheader("Fraud Distribution")
    # chart here
```

## 6. Interactive Charts

### Bar Chart
```python
category_counts = filtered_df["merchant_category"].value_counts().reset_index()

fig = px.bar(
    category_counts,
    x="merchant_category",
    y="count",
    color="merchant_category",
    text_auto=True
)
st.plotly_chart(fig)
```

### Donut Chart
```python
fig = px.pie(filtered_df, names="fraud_status", hole=0.45)
st.plotly_chart(fig)
```

### Line Chart (Monthly Trend)
```python
monthly = filtered_df.groupby("month_name").size().reset_index(name="Transactions")
monthly["month_name"] = pd.Categorical(monthly["month_name"], categories=month_order, ordered=True)
monthly = monthly.sort_values("month_name")

fig = px.line(monthly, x="month_name", y="Transactions", markers=True)
st.plotly_chart(fig)
```

> `pd.Categorical(..., ordered=True)` keeps months in **calendar order** in the chart.

### Plotly Express Functions Used
| Function | Chart |
|---|---|
| `px.bar()` | Bar chart (vertical or horizontal with `orientation="h"`) |
| `px.pie()` | Pie / donut chart (`hole=` for donut) |
| `px.line()` | Line chart |
| `px.histogram()` | Histogram (`marginal="box"` adds a box plot on top) |

## 7. Data Table and CSV Download
```python
st.subheader("Filtered Dataset")
st.dataframe(filtered_df, height=350)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_transactions.csv",
    mime="text/csv"
)
```

## Dashboard Structure
```
Sidebar: filters (category, fraud status, month, amount)
Main page:
  Title
  KPI cards (transactions, customers, total, average, fraud, fraud %)
  Row 1: category distribution | fraud distribution
  Row 2: fraud by category     | top 10 customers
  Row 3: amount distribution   | average amount by category
  Row 4: monthly trend         | transactions by day
  Business insights
  Filtered data table + download button
```

## Common Streamlit Functions
| Function | Purpose |
|---|---|
| `st.title()`, `st.header()`, `st.subheader()` | Headings |
| `st.markdown()` / `st.write()` | Text |
| `st.metric()` | KPI value |
| `st.columns()` | Side-by-side layout |
| `st.sidebar` | Left panel for filters |
| `st.plotly_chart()` | Show a Plotly chart |
| `st.dataframe()` | Interactive table |
| `st.download_button()` | Download a file |
| `st.success()`, `st.warning()` | Coloured message boxes |


## Key Takeaway
Streamlit turns a Python script into an interactive web dashboard, and Plotly Express adds charts that users can hover over and zoom into. With sidebar filters, a filtered DataFrame, KPI metrics, column layouts and charts, I built a dashboard where anyone can explore the banking data without writing code. `@st.cache_data` keeps it fast by loading the data only once.
