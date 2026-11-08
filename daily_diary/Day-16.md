# Day 16 – Seaborn

## Topics Covered
- Introduction to Seaborn
- Seaborn vs Matplotlib
- Seaborn functions and their purpose
- Styling charts in Seaborn

## Introduction to Seaborn
**Seaborn** is a Python data visualisation library **built on top of Matplotlib**.
It makes it easier to create **attractive statistical charts** with less code, and it works directly with **Pandas DataFrames**.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```

`sns` is the common short name for Seaborn. We still use `plt` for titles, labels and `plt.show()`.

### Sample Data Used Below
```python
data = {
    "category": ["Fashion", "Travel", "Grocery", "Fashion", "Travel", "Grocery", "Fashion", "Travel"],
    "amount":   [500, 900, 300, 650, 1200, 250, 700, 1000],
    "age":      [22, 35, 45, 28, 40, 50, 25, 38],
    "gender":   ["F", "M", "F", "M", "F", "M", "F", "M"]
}
df = pd.DataFrame(data)
```

## Seaborn vs Matplotlib
| Matplotlib | Seaborn |
|---|---|
| Basic, low-level plotting library | High-level library built on Matplotlib |
| More code needed for good-looking charts | Attractive charts with less code |
| Works mainly with lists and arrays | Works directly with DataFrames using column names |
| Manual statistics | Built-in statistics (averages, distributions, regression lines) |

## Seaborn Functions and Their Purpose

| Function | Chart Type | Purpose |
|---|---|---|
| `sns.countplot()` | Count plot | Count of each category |
| `sns.barplot()` | Bar plot | Average (mean) of a numeric value per category |
| `sns.histplot()` | Histogram | Distribution of a numeric column |
| `sns.kdeplot()` | KDE plot | Smooth curve of a distribution |
| `sns.boxplot()` | Box plot | Spread, median and outliers |
| `sns.violinplot()` | Violin plot | Box plot + distribution shape |
| `sns.scatterplot()` | Scatter plot | Relationship between two numeric columns |
| `sns.lineplot()` | Line plot | Trend over time or order |
| `sns.regplot()` | Regression plot | Scatter plot with a best-fit line |
| `sns.heatmap()` | Heatmap | Values in a grid with colours (e.g. correlation) |
| `sns.pairplot()` | Pair plot | Relationships between all numeric columns at once |

### 1. Count Plot – `sns.countplot()`
Counts how many times each category appears.
```python
sns.countplot(data=df, x="category")
plt.title("Number of Transactions by Category")
plt.show()
```

### 2. Bar Plot – `sns.barplot()`
Shows the **average** of a numeric column for each category (with an error bar by default).
```python
sns.barplot(data=df, x="category", y="amount")
plt.title("Average Amount by Category")
plt.show()
```

### 3. Histogram – `sns.histplot()`
Shows how numeric values are distributed. `kde=True` adds a smooth curve.
```python
sns.histplot(data=df, x="amount", bins=5, kde=True)
plt.title("Distribution of Amount")
plt.show()
```

### 4. KDE Plot – `sns.kdeplot()`
Shows the distribution as a smooth curve.
```python
sns.kdeplot(data=df, x="amount", fill=True)
plt.title("Amount Density")
plt.show()
```

### 5. Box Plot – `sns.boxplot()`
Shows the median, spread and outliers, and can compare groups.
```python
sns.boxplot(data=df, x="category", y="amount")
plt.title("Amount Spread by Category")
plt.show()
```

### 6. Violin Plot – `sns.violinplot()`
Like a box plot, but also shows the shape of the distribution.
```python
sns.violinplot(data=df, x="category", y="amount")
plt.title("Amount Distribution by Category")
plt.show()
```

### 7. Scatter Plot – `sns.scatterplot()`
Shows the relationship between two numeric columns. `hue` colours points by a category.
```python
sns.scatterplot(data=df, x="age", y="amount", hue="gender")
plt.title("Age vs Amount")
plt.show()
```

### 8. Line Plot – `sns.lineplot()`
Shows a trend.
```python
sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": [200, 250, 180, 300, 350]
})

sns.lineplot(data=sales, x="month", y="sales", marker="o")
plt.title("Monthly Sales Trend")
plt.show()
```

### 9. Regression Plot – `sns.regplot()`
Scatter plot with a **best-fit line**, to see if two values increase or decrease together.
```python
sns.regplot(data=df, x="age", y="amount")
plt.title("Age vs Amount with Trend Line")
plt.show()
```

### 10. Heatmap – `sns.heatmap()`
Shows values in a grid using colours. Commonly used for a **correlation matrix**.
```python
corr = df[["amount", "age"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

`annot=True` shows the numbers inside each box.

### 11. Pair Plot – `sns.pairplot()`
Creates scatter plots for **every pair of numeric columns**, plus histograms on the diagonal.
```python
sns.pairplot(df, hue="gender")
plt.show()
```

## Common Parameters
| Parameter | Purpose | Example |
|---|---|---|
| `data` | DataFrame to use | `data=df` |
| `x`, `y` | Column names for the axes | `x="category"`, `y="amount"` |
| `hue` | Colour by a category column | `hue="gender"` |
| `palette` | Colour theme | `palette="viridis"` |
| `color` | Single colour | `color="orange"` |
| `bins` | Number of bars in a histogram | `bins=10` |
| `kde` | Add a smooth curve to a histogram | `kde=True` |
| `annot` | Show values on a heatmap | `annot=True` |
| `cmap` | Colour map for a heatmap | `cmap="coolwarm"` |

## Styling Charts
| Function | Purpose |
|---|---|
| `sns.set_theme()` | Apply Seaborn's default style |
| `sns.set_style("whitegrid")` | Background style: `white`, `dark`, `whitegrid`, `darkgrid`, `ticks` |
| `sns.set_palette("pastel")` | Set the default colour palette |

```python
sns.set_style("whitegrid")
sns.barplot(data=df, x="category", y="amount", hue="category", palette="viridis", legend=False)
plt.title("Average Amount by Category")
plt.show()
```

## Summary
| Goal | Seaborn Function |
|---|---|
| Count categories | `countplot()` |
| Compare averages | `barplot()` |
| See distribution | `histplot()`, `kdeplot()` |
| Find spread and outliers | `boxplot()`, `violinplot()` |
| See relationships | `scatterplot()`, `regplot()`, `pairplot()` |
| Show trends | `lineplot()` |
| Show correlation | `heatmap()` |


## Key Takeaway
Seaborn is built on Matplotlib and makes good-looking statistical charts with less code. It works directly with DataFrame columns, and functions like `countplot()`, `barplot()`, `histplot()`, `boxplot()`, `scatterplot()` and `heatmap()` make it easy to explore distributions, comparisons and relationships in data. I used Seaborn for the histogram and box plot in my banking transaction analysis project.
