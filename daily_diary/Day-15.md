# Day 15 – Matplotlib

## Topics Covered
- Introduction to Matplotlib
- Basic steps to create a chart
- Matplotlib functions and their chart types
- Customising charts (title, labels, legend, colours, size)

## Introduction to Matplotlib
**Matplotlib** is a Python library used for **data visualisation**, which means showing data as charts and graphs.
Charts make it easier to understand patterns, trends and comparisons in data.

```python
import matplotlib.pyplot as plt
```

`pyplot` is the Matplotlib module used to make charts, and `plt` is its common short name.

## Basic Steps to Create a Chart
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)                 # 1. create the chart
plt.title("Simple Line Chart") # 2. add title
plt.xlabel("X Axis")           # 3. add axis labels
plt.ylabel("Y Axis")
plt.show()                     # 4. display the chart
```

## Functions and Their Chart Types

| Function | Chart Type | Used For |
|---|---|---|
| `plt.plot()` | Line chart | Trends over time |
| `plt.bar()` | Vertical bar chart | Comparing categories |
| `plt.barh()` | Horizontal bar chart | Comparing categories with long names |
| `plt.hist()` | Histogram | Distribution of numeric data |
| `plt.pie()` | Pie chart | Share / percentage of a whole |
| `plt.scatter()` | Scatter plot | Relationship between two numeric variables |
| `plt.boxplot()` | Box plot | Spread of data and outliers |
| `plt.stackplot()` | Area / stack plot | Change in totals and parts over time |
| `plt.subplot()` / `plt.subplots()` | Multiple charts | Showing several charts in one figure |

### 1. Line Chart – `plt.plot()`
```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 250, 180, 300, 350]

plt.plot(months, sales, marker="o", color="orange", linewidth=2)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

### 2. Bar Chart – `plt.bar()`
```python
categories = ["Fashion", "Electronics", "Travel", "Grocery"]
amount = [500, 800, 650, 400]

plt.bar(categories, amount, color="steelblue")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()
```

### 3. Horizontal Bar Chart – `plt.barh()`
```python
plt.barh(categories, amount, color="crimson")
plt.title("Spending by Category")
plt.xlabel("Amount")
plt.show()
```

### 4. Histogram – `plt.hist()`
```python
marks = [45, 56, 67, 70, 72, 75, 78, 80, 85, 88, 90, 95]

plt.hist(marks, bins=5, color="purple", edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
```

### 5. Pie Chart – `plt.pie()`
```python
labels = ["Legitimate", "Fraud"]
values = [97, 3]

plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Fraud vs Legitimate Transactions")
plt.show()
```

### 6. Scatter Plot – `plt.scatter()`
```python
hours = [1, 2, 3, 4, 5, 6, 7]
scores = [35, 45, 50, 60, 70, 78, 88]

plt.scatter(hours, scores, color="green")
plt.title("Study Hours vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()
```

### 7. Box Plot – `plt.boxplot()`
```python
data = [12, 15, 14, 18, 20, 22, 25, 60]

plt.boxplot(data)
plt.title("Box Plot")
plt.show()
```

The point at 60 appears separately as an **outlier**.

### 8. Multiple Charts – `plt.subplot()`
```python
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)          # 1 row, 2 columns, chart 1
plt.plot(months, sales)
plt.title("Line Chart")

plt.subplot(1, 2, 2)          # chart 2
plt.bar(categories, amount)
plt.title("Bar Chart")

plt.tight_layout()
plt.show()
```

## Customising Charts
| Function | Purpose |
|---|---|
| `plt.figure(figsize=(w, h))` | Set chart size |
| `plt.title()` | Add a chart title |
| `plt.xlabel()` / `plt.ylabel()` | Add axis labels |
| `plt.legend()` | Show a legend (needs `label=` in the chart function) |
| `plt.grid(True)` | Show grid lines |
| `plt.xticks(rotation=45)` | Rotate x-axis labels |
| `plt.xlim()` / `plt.ylim()` | Set axis range |
| `plt.tight_layout()` | Adjust spacing so labels don't overlap |
| `plt.savefig("chart.png")` | Save the chart as an image |
| `plt.show()` | Display the chart |

### Common Parameters
| Parameter | Purpose | Example |
|---|---|---|
| `color` | Colour of the chart | `color="red"` |
| `marker` | Point shape in line/scatter charts | `marker="o"` |
| `linestyle` | Line style | `linestyle="--"` |
| `linewidth` | Line thickness | `linewidth=2` |
| `label` | Name shown in the legend | `label="2024"` |
| `bins` | Number of bars in a histogram | `bins=10` |
| `autopct` | Show percentages on a pie chart | `autopct="%1.1f%%"` |

```python
sales_2024 = [200, 250, 180, 300, 350]
sales_2025 = [220, 270, 210, 320, 400]

plt.plot(months, sales_2024, label="2024", marker="o")
plt.plot(months, sales_2025, label="2025", marker="s", linestyle="--")
plt.title("Sales Comparison")
plt.legend()
plt.grid(True)
plt.show()
```

## Choosing the Right Chart
| Goal | Chart |
|---|---|
| Show a trend over time | Line chart |
| Compare categories | Bar chart |
| Show distribution of values | Histogram, box plot |
| Show parts of a whole | Pie chart |
| Show relationship between two variables | Scatter plot |
| Find outliers | Box plot |


## Key Takeaway
Matplotlib is used to create charts in Python. Each function makes a different chart type: `plot()` for lines, `bar()` for bars, `hist()` for histograms, `pie()` for pie charts, `scatter()` for scatter plots and `boxplot()` for box plots. Choosing the right chart and adding titles, labels and legends makes data easy to understand. I used these charts in my banking transaction analysis project.
