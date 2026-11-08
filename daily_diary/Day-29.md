# Day 29 – Dashboard Design and Testing

## Topics Covered
- Custom theme using `.streamlit/config.toml`
- Custom CSS in Streamlit
- Custom KPI cards and section headers
- Consistent chart styling in Plotly
- New fraud pattern charts with reference lines
- Calculated business insights and recommendations
- Testing the dashboard with different filters
- Problems faced and fixes

## 1. Custom Theme (config.toml)
Streamlit's default look is plain and light. A theme file changes colours for the whole app, including sliders, filter tags, tables and buttons.

File: `.streamlit/config.toml`
```toml
[theme]
base = "dark"
primaryColor = "#FF4B1F"
backgroundColor = "#0A0A0A"
secondaryBackgroundColor = "#141414"
textColor = "#F5F5F5"
font = "sans serif"
```

| Setting | Purpose |
|---|---|
| `base` | Light or dark starting theme |
| `primaryColor` | Accent colour for sliders, selected tags, buttons |
| `backgroundColor` | Main page background |
| `secondaryBackgroundColor` | Sidebar and widget background |
| `textColor` | Text colour |

**Theme chosen:** bold **black with orange/red** accents.

## 2. Custom CSS
CSS can be added with `st.markdown()` and `unsafe_allow_html=True` to style things the theme does not cover, such as fonts, background glow, sidebar border and card design.

```python
st.markdown("""
<style>
.stApp {
    background: radial-gradient(1200px 500px at 85% -10%, rgba(255,75,31,0.18), transparent 60%), #0A0A0A;
}
[data-testid="stSidebar"] {
    border-right: 1px solid rgba(255,75,31,0.35);
}
</style>
""", unsafe_allow_html=True)
```

## 3. Helper Functions for Reusable Design
Instead of repeating the same HTML many times, I wrote small helper functions.

### KPI Card
```python
def kpi_card(label, value, icon, a1="#FF4B1F", a2="#FF8C00"):
    return (
        f'<div class="kpi" style="--a1:{a1};--a2:{a2}">'
        f'<div class="icon">{icon}</div><div class="label">{label}</div>'
        f'<div class="value">{value}</div></div>'
    )
```
- Six KPI cards with a coloured strip on top: orange for money values, **red for fraud values**.
- Cards lift slightly when the mouse hovers over them.
- Large totals are shortened, e.g. **$50.04M** instead of $50,043,351.10.

### Section Header
```python
def section(title, subtitle=""):
    st.markdown(
        f'<div class="section"><div class="bar"></div><div>'
        f'<div class="t">{title}</div><div class="s">{subtitle}</div></div></div>',
        unsafe_allow_html=True
    )
```
Charts are grouped into sections: Category & Fraud Overview, Risk & Top Spenders, Transaction Amounts, Time Trends, Fraud Patterns.

### Chart Styling
One function styles every Plotly chart the same way.
```python
def style_fig(fig, height=420):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#d0d0d0", size=12),
        colorway=CATEGORICAL,
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="rgba(255,255,255,0.06)")
    return fig
```

### Colour Palette
```python
CATEGORICAL = ["#FF4B1F", "#FF8C00", "#FFB347", "#E63946", "#B71C1C"]
CONTINUOUS = ["#8E1414", "#E63946", "#FF4B1F", "#FF8C00", "#FFB347"]
```
- **Categorical:** different colours for different categories
- **Continuous:** dark red (low) to amber (high) for bars coloured by value
- **Fraud = red, Legitimate = orange** in every chart

### Chart Cards
Each chart is placed inside a bordered container, styled as a dark rounded card:
```python
with st.container(border=True):
    chart_title("📊", "Merchant Category Distribution")
    show(fig)
```

## 4. Improved Analysis in the Dashboard

### Fraud Rate Instead of Fraud Count
```python
fraud_rate_cat = filtered_df.groupby("merchant_category")["is_fraud"].mean() * 100
fig = px.bar(fraud_rate_cat.sort_values().reset_index(name="Fraud Rate (%)"),
             x="Fraud Rate (%)", y="merchant_category", orientation="h", text_auto=".2f")
fig.add_vline(x=fraud_percentage, line_dash="dash", annotation_text="overall")
```
The dashed line shows the **overall fraud rate**, so it is easy to see which categories are above average.

### New Fraud Patterns Section
- **Fraud rate by amount range** (bar chart with an overall-rate line)
- **Fraud rate by month** (line chart with an overall-rate line)

### Month Filter in Calendar Order
```python
month_options = [m for m in MONTH_ORDER if m in df["month_name"].unique()]
```
Before this, months were sorted alphabetically (April, August, December, ...).

### Calculated Business Insights
The insight cards now calculate findings from the **filtered data**, so they change with the filters:

| Insight | Calculation |
|---|---|
| Riskiest category | Category with the highest fraud rate |
| Busiest month / day | `value_counts().idxmax()` |
| Avg amount: fraud / legit | `groupby("fraud_status")["amount"].mean()` |
| Repeat customers | Share of customers with more than 1 transaction |

A **Recommendations** box below the insights suggests actions based on the findings.

## 5. Testing the Dashboard
I tested the dashboard with different filter combinations to make sure nothing breaks.

| Test | Expected Result | Result |
|---|---|---|
| All filters selected (default) | Full dashboard, 100,000 rows | Passed |
| Only "Fraud" selected | Fraud rate 100%, charts update | Passed |
| Only "Legitimate" selected | Fraud cases 0, fraud rate 0.00% | Passed |
| All categories removed | "No data available" message, no crash | Passed |
| One category + one month | Small filtered result | Passed |
| Very small amount range | Few rows, charts still work | Passed |

Streamlit also has a testing tool that runs the app without a browser:
```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("dash.py", default_timeout=120)
at.run()
at.multiselect[1].set_value(["Fraud"])   # select only Fraud
at.run()
print(at.exception)   # empty list = no errors
```

## 6. Problems Faced and Fixes
| Problem | Cause | Fix |
|---|---|---|
| Logo emoji showed as an orange box | The gradient text style also coloured the emoji | Put the emoji in a separate `<span>` without the gradient |
| Curved line chart went above the real highest value | `shape="spline"` smoothing overshoots | Used a straight line instead |
| Dark bars looked muddy on black background | Colour scale started almost at black | Started the scale at a brighter dark red |
| 12 month tags were cut off in the sidebar | Filter box had a fixed maximum height | CSS to let the box grow |
| "vs" showed as "Vs" in an insight card | CSS `text-transform: capitalize` | Changed the text to use "/" instead |
| Dashboard showed old data after updating the CSV | `@st.cache_data` kept the old file in memory | Restarted the Streamlit server |
| Deprecation warning for `use_container_width` | Changed in newer Streamlit versions | Used `width="stretch"` |


## Key Takeaway
A good dashboard needs both good design and correct analysis. A theme file and custom CSS gave the dashboard a bold black and orange/red look, helper functions kept the design consistent, and fraud rate charts with reference lines made comparisons fair. Testing with unusual filter choices, like selecting nothing, made sure the dashboard never crashes.
