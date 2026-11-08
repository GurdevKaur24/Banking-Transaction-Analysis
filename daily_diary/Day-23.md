# Day 23 – Excel Pivot Tables, Charts and Conditional Formatting

## Topics Covered
- Pivot tables: definition and creation
- Pivot table areas (Rows, Columns, Values, Filters)
- Value field settings (Sum, Count, Average, % of total)
- Slicers
- Pivot charts and normal Excel charts
- Conditional formatting
- Practice on the banking transaction data

## Pivot Tables

### Definition
A **pivot table** is an Excel tool that **summarises large data quickly** by grouping, counting, adding or averaging values, without writing formulas.
It works like `GROUP BY` in SQL and `groupby()` in Pandas.

### Creating a Pivot Table
1. Click any cell inside the data.
2. Go to **Insert → PivotTable**.
3. Check the data range and choose **New Worksheet**.
4. Click **OK**. The **PivotTable Fields** panel opens.
5. Drag fields into the four areas.

### Pivot Table Areas
| Area | Purpose | Example |
|---|---|---|
| **Rows** | Groups shown as rows | `merchant_category` |
| **Columns** | Groups shown as columns | `fraud_status` |
| **Values** | Numbers to calculate (Sum, Count, Average) | `amount` |
| **Filters** | Filter the whole pivot table | `month_name` |

### Value Field Settings
Right-click a value → **Value Field Settings** to change the calculation.

| Setting | Use |
|---|---|
| **Sum** | Total amount |
| **Count** | Number of transactions |
| **Average** | Average amount |
| **Min / Max** | Smallest / largest value |
| **Show Values As → % of Grand Total** | Share of each group in the total |
| **Show Values As → % of Row Total** | Share within each row |

## Practice: Banking Transaction Data
I used the `cleaned_transactions.csv` file from my project (100,000 transactions).

### Pivot 1: Transactions and Amount by Category
- **Rows:** `merchant_category`
- **Values:** Count of `transaction_id`, Sum of `amount`

| merchant_category | Count of transactions | Sum of amount |
|---|---|---|
| electronics | 20,079 | 10,004,588 |
| fashion | 19,995 | 9,996,709 |
| gaming | 19,999 | 10,066,655 |
| groceries | 19,966 | 9,940,813 |
| travel | 19,961 | 10,034,587 |
| **Grand Total** | **100,000** | **50,043,351** |

### Pivot 2: Fraud Rate by Category
- **Rows:** `merchant_category`
- **Values:** Average of `is_fraud` (formatted as **Percentage**)

Since `is_fraud` is 1 for fraud and 0 for legitimate, its **average = fraud rate**.

| merchant_category | Fraud Rate |
|---|---|
| electronics | 2.98% |
| fashion | 2.98% |
| gaming | 2.96% |
| groceries | 3.24% |
| travel | 2.81% |
| **Grand Total** | **2.99%** |

### Pivot 3: Fraud vs Legitimate
- **Rows:** `fraud_status`
- **Values:** Count of `transaction_id`, and the same field again with **Show Values As → % of Grand Total**

| fraud_status | Count | % of Total |
|---|---|---|
| Fraud | 2,994 | 2.99% |
| Legitimate | 97,006 | 97.01% |

### Refreshing a Pivot Table
If the source data changes, right-click the pivot table → **Refresh** (or **Data → Refresh All**).

## Slicers
**Slicers** are buttons that filter a pivot table (and pivot charts) with one click.
- Click the pivot table → **PivotTable Analyze → Insert Slicer**
- Choose fields such as `merchant_category` or `month_name`
- Clicking a button filters the data; hold **Ctrl** to select multiple values

Slicers make pivot tables work like a simple interactive dashboard.

## Charts in Excel

### Pivot Charts
A **pivot chart** is a chart connected to a pivot table. It updates automatically when the pivot table or slicer changes.
- Click the pivot table → **PivotTable Analyze → PivotChart**

### Normal Charts
Select the data → **Insert →** choose a chart.

| Chart | Best Used For |
|---|---|
| **Column / Bar chart** | Comparing categories (e.g. amount by category) |
| **Line chart** | Trends over time (e.g. transactions per month) |
| **Pie / Doughnut chart** | Share of a whole (e.g. fraud vs legitimate) |
| **Histogram** | Distribution of values (e.g. transaction amounts) |
| **Scatter chart** | Relationship between two numbers |
| **Combo chart** | Two types together (e.g. count as bars + fraud rate as line) |

### Chart Elements
Click the chart → **+ (Chart Elements)** to add or remove:
- Chart title
- Axis titles
- Data labels
- Legend
- Gridlines

## Conditional Formatting
**Conditional formatting** changes the look of cells automatically based on their values, so patterns stand out.
- Select the cells → **Home → Conditional Formatting**

| Type | Use | Example |
|---|---|---|
| **Highlight Cells Rules** | Colour cells meeting a rule | Highlight amounts greater than 900 in red |
| **Top/Bottom Rules** | Highlight top or bottom values | Top 10 transaction amounts |
| **Data Bars** | Bars inside cells showing size | Amount column |
| **Color Scales** | Colour gradient from low to high | Fraud rate column in the pivot table |
| **Icon Sets** | Arrows or symbols based on value | Up/down arrows for amounts |
| **New Rule → Use a formula** | Custom rules | Highlight the whole row where `fraud_status` is "Fraud" |

**Formula rule to highlight fraud rows** (select A2:F100 first):
```
=$E2="Fraud"
```
The `$` fixes column E, so the whole row is coloured when that row's status is Fraud.


## Key Takeaway
Pivot tables summarise thousands of rows in seconds by grouping and calculating values, slicers make them interactive, and pivot charts turn them into visuals. Conditional formatting highlights important values automatically. Using the banking data, a pivot table gave the same results as my Python analysis: groceries has the highest fraud rate (3.24%) and the overall fraud rate is 2.99%.
