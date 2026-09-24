import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="🛒",
    layout="wide"
)

# Load dataset
df = pd.read_csv("Superstore.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Title
st.title("🛒 E-Commerce Sales Analytics Dashboard")
st.write("Analyze sales, customers, products, profit, and business performance.")

# Sidebar
st.sidebar.header("Filters")

# Region filter
regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

# Category filter
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

# Apply filters
filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# Basic KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_quantity = filtered_df["Quantity"].sum()
total_orders = filtered_df["Order ID"].nunique()

# KPI display
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("📦 Total Quantity", f"{total_quantity:,.0f}")
col4.metric("🧾 Total Orders", f"{total_orders:,}")

st.divider()

st.subheader("📊 Sales by Category")

category_sales = (
    filtered_df.groupby("Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category",
    text_auto=".2s"
)

st.plotly_chart(fig, use_container_width=True)
# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")

filtered_df["Month"] = filtered_df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
    filtered_df.groupby("Month", as_index=False)["Sales"]
    .sum()
)

fig_monthly = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig_monthly, use_container_width=True)


# Sales by Region
st.subheader("🌍 Sales by Region")

region_sales = (
    filtered_df.groupby("Region", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region",
    text_auto=".2s"
)

st.plotly_chart(fig_region, use_container_width=True)
# Product Analysis
st.subheader("📦 Product Analysis")

# Sales by Sub-Category
subcategory_sales = (
    filtered_df.groupby("Sub-Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig_subcategory = px.bar(
    subcategory_sales,
    x="Sub-Category",
    y="Sales",
    title="Sales by Sub-Category",
    text_auto=".2s"
)

st.plotly_chart(fig_subcategory, use_container_width=True)


# Top 10 Products
st.subheader("🏆 Top 10 Products by Sales")

top_products = (
    filtered_df.groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

fig_products = px.bar(
    top_products.sort_values("Sales"),
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales",
    text_auto=".2s"
)

st.plotly_chart(fig_products, use_container_width=True)
# Customer & Segment Analysis
st.subheader("👥 Customer & Segment Analysis")

# Sales by Customer Segment
segment_sales = (
    filtered_df.groupby("Segment", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig_segment = px.pie(
    segment_sales,
    names="Segment",
    values="Sales",
    title="Sales Distribution by Customer Segment"
)

st.plotly_chart(fig_segment, use_container_width=True)


# Customers by Region
customer_region = (
    filtered_df.groupby("Region")["Customer ID"]
    .nunique()
    .reset_index(name="Customers")
)

fig_customers = px.bar(
    customer_region,
    x="Region",
    y="Customers",
    title="Number of Customers by Region",
    text_auto=True
)

st.plotly_chart(fig_customers, use_container_width=True)
# Profit & Risk Analysis
st.subheader("⚠️ Profit & Risk Analysis")

# Profit by Category
category_profit = (
    filtered_df.groupby("Category", as_index=False)["Profit"]
    .sum()
    .sort_values("Profit", ascending=False)
)

fig_profit_category = px.bar(
    category_profit,
    x="Category",
    y="Profit",
    title="Profit by Category",
    text_auto=".2s"
)

st.plotly_chart(fig_profit_category, use_container_width=True)


# Loss-Making Sub-Categories
subcategory_profit = (
    filtered_df.groupby("Sub-Category", as_index=False)["Profit"]
    .sum()
    .sort_values("Profit")
)

loss_making = subcategory_profit[subcategory_profit["Profit"] < 0]

fig_loss = px.bar(
    loss_making,
    x="Sub-Category",
    y="Profit",
    title="Loss-Making Sub-Categories",
    text_auto=".2s"
)

st.plotly_chart(fig_loss, use_container_width=True)


# Discount vs Profit
st.subheader("💸 Discount vs Profit")

# Remove rows with missing values needed for the scatter plot
discount_data = filtered_df.dropna(
    subset=["Discount", "Profit", "Sales"]
).copy()

fig_discount = px.scatter(
    discount_data,
    x="Discount",
    y="Profit",
    size="Sales",
    hover_data=["Category", "Sub-Category"],
    title="Relationship Between Discount and Profit"
)
st.plotly_chart(fig_discount, use_container_width=True)
# Business Insights
st.subheader("💡 Business Insights & Recommendations")

# Calculate key insights
best_category = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

best_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

best_segment = (
    filtered_df.groupby("Segment")["Sales"]
    .sum()
    .idxmax()
)

most_profitable_category = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
    .idxmax()
)

# Display insights
st.markdown(f"""
### 📌 Key Insights

- **Top Sales Category:** {best_category}
- **Top Sales Region:** {best_region}
- **Top Customer Segment:** {best_segment}
- **Most Profitable Category:** {most_profitable_category}

### 🎯 Recommended Actions

- Focus marketing efforts on high-performing categories and regions.
- Review loss-making sub-categories and products.
- Monitor discounts carefully because excessive discounts can reduce profitability.
- Study high-value customer segments and develop strategies to retain them.
- Use monthly sales trends to plan inventory and promotional activities.
""")