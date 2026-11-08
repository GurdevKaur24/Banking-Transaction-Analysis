import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Banking Transaction Dashboard",
    page_icon="🏦",
    layout="wide"
)

# ------------------------------------------------------------------
# theme
# ------------------------------------------------------------------
ORANGE = "#FF8C00"
RED_ORANGE = "#FF4B1F"
AMBER = "#FFB347"
RED = "#E63946"
DARK_RED = "#B71C1C"

CATEGORICAL = [RED_ORANGE, ORANGE, AMBER, RED, DARK_RED]

MONTH_ORDER = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
AMOUNT_RANGE_ORDER = ["$0-100", "$100-250", "$250-500", "$500-750", "$750-1000"]
CONTINUOUS = ["#8E1414", RED, RED_ORANGE, ORANGE, AMBER]

st.markdown(
"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800;900&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"], .stApp, .stMarkdown, p, label {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(1200px 500px at 85% -10%, rgba(255,75,31,0.18), transparent 60%),
        radial-gradient(900px 400px at -10% 30%, rgba(230,57,70,0.10), transparent 60%),
        #0A0A0A;
}

[data-testid="stHeader"] { background: transparent; }
footer, #MainMenu { visibility: hidden; }

.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1500px; }

/* sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #121212 0%, #0A0A0A 100%);
    border-right: 1px solid rgba(255,75,31,0.35);
}
[data-testid="stSidebar"] label p {
    font-weight: 600; text-transform: uppercase; letter-spacing: .08em;
    font-size: .72rem !important; color: #bbb;
}
.brand {
    font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 1.5rem;
    letter-spacing: .02em; margin-bottom: .2rem;
    background: linear-gradient(90deg, #FF4B1F, #FF8C00);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.brand-sub { color: #888; font-size: .78rem; margin-bottom: 1.2rem; }
.side-count {
    margin-top: 1.4rem; padding: 14px 16px; border-radius: 14px;
    background: rgba(255,75,31,0.08); border: 1px solid rgba(255,75,31,0.35);
}
.side-count .n { font-family: 'Outfit'; font-size: 1.6rem; font-weight: 800; color: #FF8C00; }
.side-count .l { font-size: .72rem; color: #aaa; text-transform: uppercase; letter-spacing: .08em; }

/* hero */
.hero {
    position: relative; overflow: hidden;
    padding: 34px 38px; border-radius: 24px; margin-bottom: 26px;
    background: linear-gradient(135deg, #1a0a04 0%, #0d0d0d 55%, #1a0505 100%);
    border: 1px solid rgba(255,75,31,0.35);
    box-shadow: 0 20px 60px -20px rgba(255,75,31,0.35);
}
.hero::after {
    content: ""; position: absolute; right: -80px; top: -80px; width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(255,140,0,0.35), transparent 70%);
}
.hero h1 {
    font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 2.8rem; line-height: 1.05;
    margin: 0 0 10px 0; padding: 0;
    background: linear-gradient(90deg, #FFFFFF 0%, #FFB347 35%, #FF4B1F 70%, #E63946 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero p { color: #b5b5b5; font-size: 1.02rem; max-width: 760px; margin: 0; }
.pills { margin-top: 18px; display: flex; gap: 10px; flex-wrap: wrap; }
.pill {
    font-size: .72rem; font-weight: 600; letter-spacing: .1em; text-transform: uppercase;
    padding: 6px 12px; border-radius: 999px; color: #FFB347;
    border: 1px solid rgba(255,140,0,0.45); background: rgba(255,140,0,0.08);
}
.pill.live { color: #fff; background: linear-gradient(90deg, #FF4B1F, #E63946); border: none; }

/* kpi cards */
.kpi-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; margin-bottom: 30px; }
@media (max-width: 1200px) { .kpi-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 700px)  { .kpi-grid { grid-template-columns: repeat(2, 1fr); } }
.kpi {
    position: relative; padding: 20px 20px 18px; border-radius: 18px;
    background: linear-gradient(180deg, #161616, #0f0f0f);
    border: 1px solid #222; overflow: hidden;
    transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.kpi::before {
    content: ""; position: absolute; left: 0; top: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, var(--a1), var(--a2));
}
.kpi:hover { transform: translateY(-4px); border-color: var(--a1); box-shadow: 0 14px 34px -14px var(--a1); }
.kpi .icon { font-size: 1.3rem; margin-bottom: 8px; }
.kpi .label { font-size: .72rem; color: #999; text-transform: uppercase; letter-spacing: .1em; font-weight: 600; }
.kpi .value { font-family: 'Outfit', sans-serif; font-size: 1.85rem; font-weight: 800; color: #fff; margin-top: 4px; white-space: nowrap; }

/* section header */
.section { display: flex; align-items: center; gap: 14px; margin: 26px 0 14px; }
.section .bar { width: 6px; height: 34px; border-radius: 4px; background: linear-gradient(180deg, #FF8C00, #E63946); }
.section .t { font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.35rem; color: #fff; letter-spacing: .01em; }
.section .s { font-size: .82rem; color: #888; }

/* chart cards (bordered containers) */
[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stVerticalBlock"]:has(> div > .chart-title) {
    background: linear-gradient(180deg, rgba(22,22,22,0.9), rgba(12,12,12,0.9));
    border: 1px solid #222 !important; border-radius: 20px !important;
}
.chart-title { font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.05rem; color: #f5f5f5; }
.chart-title span { color: #FF8C00; margin-right: 6px; }

/* insights */
.ins-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; }
@media (max-width: 1200px) { .ins-grid { grid-template-columns: repeat(2, 1fr); } }
.ins {
    padding: 18px; border-radius: 16px; background: #121212;
    border: 1px solid #222; border-left: 4px solid #FF4B1F;
}
.ins .l { font-size: .72rem; color: #999; text-transform: uppercase; letter-spacing: .1em; font-weight: 600; }
.ins .v { font-family: 'Outfit'; font-size: 1.35rem; font-weight: 800; color: #FFB347; margin-top: 6px; text-transform: capitalize; }

.reco {
    margin-top: 16px; padding: 20px 24px; border-radius: 16px;
    background: linear-gradient(135deg, rgba(255,75,31,0.10), rgba(18,18,18,0.9));
    border: 1px solid rgba(255,75,31,0.35);
}
.reco-t { font-family: 'Outfit'; font-weight: 800; font-size: 1.1rem; color: #fff; margin-bottom: 8px; }
.reco ul { margin: 0; padding-left: 20px; color: #ccc; }
.reco li { margin: 6px 0; }
.reco b { color: #FFB347; text-transform: capitalize; }

/* buttons */
.stDownloadButton button {
    background: linear-gradient(90deg, #FF4B1F, #E63946) !important; color: #fff !important;
    border: none !important; border-radius: 12px !important; font-weight: 700 !important;
    padding: .6rem 1.4rem !important;
}
.stDownloadButton button:hover { box-shadow: 0 10px 28px -8px rgba(255,75,31,0.7); }

/* let sidebar multiselects grow so all 12 months are visible */
[data-testid="stSidebar"] [data-baseweb="select"] > div { max-height: none !important; }
[data-testid="stSidebar"] [data-baseweb="select"] > div > div { overflow: visible !important; }

/* multiselect chips */
[data-baseweb="tag"] { background: linear-gradient(90deg, #FF4B1F, #E63946) !important; border-radius: 8px !important; }

.footer {
    margin-top: 40px; padding: 22px; text-align: center; color: #777; font-size: .85rem;
    border-top: 1px solid #222;
}
.footer b { color: #FF8C00; }
</style>
""",
    unsafe_allow_html=True,
)


def html(s):
    st.markdown(s, unsafe_allow_html=True)


def section(title, subtitle=""):
    html(
        f'<div class="section"><div class="bar"></div><div>'
        f'<div class="t">{title}</div><div class="s">{subtitle}</div></div></div>'
    )


def kpi_card(label, value, icon, a1=RED_ORANGE, a2=ORANGE):
    return (
        f'<div class="kpi" style="--a1:{a1};--a2:{a2}">'
        f'<div class="icon">{icon}</div><div class="label">{label}</div>'
        f'<div class="value">{value}</div></div>'
    )


def style_fig(fig, height=420):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#d0d0d0", size=12),
        margin=dict(l=10, r=10, t=20, b=10),
        colorway=CATEGORICAL,
        hoverlabel=dict(bgcolor="#1a1a1a", bordercolor=RED_ORANGE, font_color="#fff"),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        coloraxis_colorbar=dict(outlinewidth=0, thickness=10),
    )
    fig.update_xaxes(showgrid=False, linecolor="#333", title_font_color="#999")
    fig.update_yaxes(gridcolor="rgba(255,255,255,0.06)", zeroline=False, linecolor="#333", title_font_color="#999")
    return fig


def show(fig, height=420):
    st.plotly_chart(style_fig(fig, height), width="stretch", config={"displayModeBar": False})


def chart_title(icon, text):
    html(f'<div class="chart-title"><span>{icon}</span>{text}</div>')


# ------------------------------------------------------------------
# load data
# ------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_transactions.csv")
    return df

df = load_data()

# ------------------------------------------------------------------
# sidebar filters
# ------------------------------------------------------------------
with st.sidebar:
    html('<div class="brand"><span style="-webkit-text-fill-color:initial">🏦</span> TXN ANALYTICS</div><div class="brand-sub">Filter the dashboard</div>')

    category = st.multiselect(
        "Merchant Category",
        options=sorted(df["merchant_category"].unique()),
        default=sorted(df["merchant_category"].unique())
    )

    fraud = st.multiselect(
        "Fraud Status",
        options=sorted(df["fraud_status"].unique()),
        default=sorted(df["fraud_status"].unique())
    )

    # months in calendar order (not alphabetical)
    month_options = [m for m in MONTH_ORDER if m in df["month_name"].unique()]
    month = st.multiselect(
        "Month",
        options=month_options,
        default=month_options
    )

    amount_range = st.slider(
        "Transaction Amount",
        float(df["amount"].min()),
        float(df["amount"].max()),
        (
            float(df["amount"].min()),
            float(df["amount"].max())
        )
    )

# filter data
filtered_df = df[
    (df["merchant_category"].isin(category)) &
    (df["fraud_status"].isin(fraud)) &
    (df["month_name"].isin(month)) &
    (df["amount"] >= amount_range[0]) &
    (df["amount"] <= amount_range[1])
]

with st.sidebar:
    html(
        f'<div class="side-count"><div class="l">Rows in view</div>'
        f'<div class="n">{len(filtered_df):,}</div>'
        f'<div class="l">of {len(df):,} transactions</div></div>'
    )

# ------------------------------------------------------------------
# hero
# ------------------------------------------------------------------
html(
    f"""<div class="hero">
<h1>Banking Transaction<br>Pattern Analysis</h1>
<p>Analyze banking transactions, customer spending patterns, merchant categories and fraud trends using interactive visualizations.</p>
<div class="pills"><span class="pill live">● Live</span><span class="pill">{len(df):,} transactions</span><span class="pill">{df['customer_id'].nunique():,} customers</span><span class="pill">{df['merchant_category'].nunique()} categories</span></div>
</div>"""
)

# ------------------------------------------------------------------
# KPIs
# ------------------------------------------------------------------
total_transactions = len(filtered_df)
unique_customers = filtered_df["customer_id"].nunique()
total_amount = filtered_df["amount"].sum()
average_amount = filtered_df["amount"].mean() if total_transactions > 0 else 0
fraud_transactions = (
    filtered_df["fraud_status"] == "Fraud"
).sum()
fraud_percentage = (
    fraud_transactions / total_transactions * 100
    if total_transactions > 0 else 0
)


def short_money(x):
    if x >= 1e9:
        return f"${x/1e9:.2f}B"
    if x >= 1e6:
        return f"${x/1e6:.2f}M"
    if x >= 1e3:
        return f"${x/1e3:.1f}K"
    return f"${x:,.2f}"


html(
    '<div class="kpi-grid">'
    + kpi_card("Transactions", f"{total_transactions:,}", "💳")
    + kpi_card("Customers", f"{unique_customers:,}", "👥")
    + kpi_card("Total Amount", short_money(total_amount), "💰", ORANGE, AMBER)
    + kpi_card("Average Amount", f"${average_amount:,.2f}", "📊", ORANGE, AMBER)
    + kpi_card("Fraud Cases", f"{fraud_transactions:,}", "🚨", RED, DARK_RED)
    + kpi_card("Fraud Rate", f"{fraud_percentage:.2f}%", "⚠️", RED, DARK_RED)
    + "</div>"
)

# ------------------------------------------------------------------
# row 1 - categories & fraud split
# ------------------------------------------------------------------
section("Category & Fraud Overview", "How transactions are spread across merchants and fraud status")
left, right = st.columns(2)

with left:
    with st.container(border=True):
        chart_title("📊", "Merchant Category Distribution")
        fig = px.bar(
            filtered_df["merchant_category"]
            .value_counts()
            .reset_index(),
            x="merchant_category",
            y="count",
            color="merchant_category",
            color_discrete_sequence=CATEGORICAL,
            text_auto=True
        )
        fig.update_traces(marker_line_width=0, textposition="outside", cliponaxis=False)
        fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title="Transactions")
        show(fig)

with right:
    with st.container(border=True):
        chart_title("🕵️", "Fraud Distribution")
        fig = px.pie(
            filtered_df,
            names="fraud_status",
            hole=0.62,
            color="fraud_status",
            color_discrete_map={"Fraud": RED, "Legitimate": ORANGE}
        )
        fig.update_traces(
            marker=dict(line=dict(color="#0A0A0A", width=3)),
            textinfo="percent+label",
            pull=[0.04 if n == "Fraud" else 0 for n in sorted(filtered_df["fraud_status"].unique())]
        )
        fig.update_layout(
            legend=dict(orientation="h", y=-0.08, x=0.5, xanchor="center"),
            annotations=[dict(
                text=f"<b>{fraud_percentage:.2f}%</b><br><span style='font-size:11px;color:#999'>fraud rate</span>",
                showarrow=False, font=dict(size=22, color="#fff")
            )]
        )
        show(fig)

# ------------------------------------------------------------------
# row 2 - fraud by category & top customers
# ------------------------------------------------------------------
section("Risk & Top Spenders", "Where fraud concentrates and who spends the most")
left, right = st.columns(2)

with left:
    with st.container(border=True):
        chart_title("🚨", "Fraud Rate by Merchant Category")
        # fraud rate % = share of transactions in the category that are fraud
        fraud_rate_cat = filtered_df.groupby("merchant_category")["is_fraud"].mean() * 100
        fraud_rate_cat = fraud_rate_cat.sort_values().reset_index(name="Fraud Rate (%)")
        fig = px.bar(
            fraud_rate_cat,
            x="Fraud Rate (%)",
            y="merchant_category",
            orientation="h",
            color="Fraud Rate (%)",
            color_continuous_scale=CONTINUOUS,
            text_auto=".2f"
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.add_vline(x=fraud_percentage, line_dash="dash", line_color="#888",
                      annotation_text="overall", annotation_font_color="#aaa")
        fig.update_layout(yaxis_title=None, xaxis_title="Fraud Rate (%)", coloraxis_showscale=False)
        show(fig)

with right:
    with st.container(border=True):
        chart_title("👑", "Top 10 Customers by Spend")
        top = (
            filtered_df
            .groupby("customer_id")["amount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        top["customer_id"] = top["customer_id"].astype(str)
        fig = px.bar(
            top,
            x="customer_id",
            y="amount",
            color="amount",
            color_continuous_scale=CONTINUOUS,
            text_auto=".2s"
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.update_layout(
            xaxis_title="Customer ID", yaxis_title="Total Amount ($)",
            xaxis_type="category", coloraxis_showscale=False
        )
        show(fig)

# ------------------------------------------------------------------
# row 3 - amounts
# ------------------------------------------------------------------
section("Transaction Amounts", "Distribution and average ticket size")
left, right = st.columns(2)

with left:
    with st.container(border=True):
        chart_title("💰", "Transaction Amount Distribution")
        fig = px.histogram(
            filtered_df,
            x="amount",
            nbins=30,
            marginal="box",
            color_discrete_sequence=[RED_ORANGE]
        )
        fig.update_traces(marker_line_color="#0A0A0A", marker_line_width=1, selector=dict(type="histogram"))
        fig.update_traces(marker_color=AMBER, selector=dict(type="box"))
        fig.update_layout(xaxis_title="Amount ($)", yaxis_title="Count", bargap=0.05)
        show(fig)

with right:
    with st.container(border=True):
        chart_title("📈", "Average Transaction Amount")
        avg = (
            filtered_df
            .groupby("merchant_category")["amount"]
            .mean()
            .reset_index()
        )
        fig = px.bar(
            avg,
            x="merchant_category",
            y="amount",
            color="amount",
            color_continuous_scale=CONTINUOUS,
            text_auto=".2f"
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis_title=None, yaxis_title="Average Amount ($)", coloraxis_showscale=False)
        show(fig)

# ------------------------------------------------------------------
# row 4 - time trends
# ------------------------------------------------------------------
section("Time Trends", "Activity across months and weekdays")
left, right = st.columns(2)

with left:
    with st.container(border=True):
        chart_title("📅", "Monthly Transaction Trend")
        month_order = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        monthly = (
            filtered_df.groupby("month_name")
            .size()
            .reset_index(name="Transactions")
        )

        monthly["month_name"] = pd.Categorical(
            monthly["month_name"],
            categories=month_order,
            ordered=True
        )

        monthly = monthly.sort_values("month_name")

        fig = px.line(
            monthly,
            x="month_name",
            y="Transactions",
            markers=True
        )
        fig.update_traces(
            line=dict(color=RED_ORANGE, width=4),
            marker=dict(size=12, color=AMBER, line=dict(color="#0A0A0A", width=2)),
            fill="tozeroy",
            fillcolor="rgba(255,75,31,0.15)"
        )
        fig.update_layout(xaxis_title=None)
        show(fig)

with right:
    with st.container(border=True):
        chart_title("📆", "Transactions by Day")
        day_order = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]

        day = (
            filtered_df.groupby("day_name")
            .size()
            .reset_index(name="Transactions")
        )

        day["day_name"] = pd.Categorical(
            day["day_name"],
            categories=day_order,
            ordered=True
        )

        day = day.sort_values("day_name")

        fig = px.bar(
            day,
            x="day_name",
            y="Transactions",
            color="Transactions",
            color_continuous_scale=CONTINUOUS,
            text_auto=True
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis_title=None, coloraxis_showscale=False)
        show(fig)

# ------------------------------------------------------------------
# row 5 - fraud patterns
# ------------------------------------------------------------------
section("Fraud Patterns", "Does fraud depend on the transaction amount or the month?")
left, right = st.columns(2)

with left:
    with st.container(border=True):
        chart_title("💸", "Fraud Rate by Amount Range")
        fraud_rate_amount = filtered_df.groupby("amount_range")["is_fraud"].mean() * 100
        fraud_rate_amount = fraud_rate_amount.reindex(AMOUNT_RANGE_ORDER).dropna()
        fraud_rate_amount = fraud_rate_amount.reset_index(name="Fraud Rate (%)")
        fig = px.bar(
            fraud_rate_amount,
            x="amount_range",
            y="Fraud Rate (%)",
            color="Fraud Rate (%)",
            color_continuous_scale=CONTINUOUS,
            text_auto=".2f"
        )
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.add_hline(y=fraud_percentage, line_dash="dash", line_color="#888")
        fig.update_layout(xaxis_title="Amount Range", coloraxis_showscale=False)
        show(fig)

with right:
    with st.container(border=True):
        chart_title("📉", "Fraud Rate by Month")
        fraud_rate_month = filtered_df.groupby("month_name")["is_fraud"].mean() * 100
        fraud_rate_month = fraud_rate_month.reindex(MONTH_ORDER).dropna()
        fraud_rate_month = fraud_rate_month.reset_index(name="Fraud Rate (%)")
        fig = px.line(
            fraud_rate_month,
            x="month_name",
            y="Fraud Rate (%)",
            markers=True
        )
        fig.update_traces(
            line=dict(color=RED, width=4),
            marker=dict(size=10, color=AMBER, line=dict(color="#0A0A0A", width=2))
        )
        fig.add_hline(y=fraud_percentage, line_dash="dash", line_color="#888")
        fig.update_layout(xaxis_title=None)
        show(fig)

# ------------------------------------------------------------------
# business insights
# ------------------------------------------------------------------
section("Business Insights", "Key findings for the current filter selection")

if len(filtered_df) > 0:

    # category with the highest fraud rate
    fraud_rate_by_cat = filtered_df.groupby("merchant_category")["is_fraud"].mean() * 100
    riskiest_category = fraud_rate_by_cat.idxmax()
    riskiest_rate = fraud_rate_by_cat.max()

    # busiest month and day
    busiest_month = filtered_df["month_name"].value_counts().idxmax()
    busiest_day = filtered_df["day_name"].value_counts().idxmax()

    # average amount of fraud vs legitimate transactions
    avg_by_status = filtered_df.groupby("fraud_status")["amount"].mean()
    avg_fraud = avg_by_status.get("Fraud", 0)
    avg_legit = avg_by_status.get("Legitimate", 0)

    # share of customers with more than one transaction
    tx_per_customer = filtered_df["customer_id"].value_counts()
    repeat_percent = (tx_per_customer > 1).mean() * 100

    insights = [
        ("Riskiest Category", f"{riskiest_category} ({riskiest_rate:.2f}%)"),
        ("Busiest Month", busiest_month),
        ("Busiest Day", busiest_day),
        ("Avg Amount: Fraud / Legit", f"${avg_fraud:,.0f} / ${avg_legit:,.0f}"),
        ("Repeat Customers", f"{repeat_percent:.1f}%"),
    ]
    html(
        '<div class="ins-grid">'
        + "".join(f'<div class="ins"><div class="l">{l}</div><div class="v">{v}</div></div>' for l, v in insights)
        + "</div>"
    )

    html(
        '<div class="reco"><div class="reco-t">🎯 Recommendations</div><ul>'
        '<li>Fraud rate stays close to ~3% for every category, month and amount range, so simple rules '
        '(e.g. "flag large payments") would not catch fraud well.</li>'
        '<li>Monitor each customer against their own normal behaviour (sudden changes in frequency, category or amount).</li>'
        f'<li>Start with extra checks on <b>{riskiest_category}</b>, the category with the highest fraud rate.</li>'
        '<li>Collect richer data (time of day, location, device) to build a fraud prediction model.</li>'
        '</ul></div>'
    )

else:
    st.warning("No data available for selected filters.")

# ------------------------------------------------------------------
# dataset preview
# ------------------------------------------------------------------
section("Filtered Dataset", f"{len(filtered_df):,} rows match your filters")

st.dataframe(
    filtered_df,
    width="stretch",
    height=350
)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_transactions.csv",
    mime="text/csv"
)

# ------------------------------------------------------------------
# footer
# ------------------------------------------------------------------
html(
    '<div class="footer">🏦 <b>Banking Transaction Analytics</b> · '
    'A Data Analytics Project built with Python, Pandas, Plotly &amp; Streamlit</div>'
)
