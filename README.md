# 🛒 E-Commerce Sales Analytics Dashboard

## 📌 Project Overview

The E-Commerce Sales Analytics Dashboard is a Python-based business intelligence project developed to analyze e-commerce sales data and generate meaningful business insights.

The project uses data analysis and visualization techniques to understand sales performance, customer behavior, product performance, profitability, regional trends, and discount impact.

The dashboard is developed using Python, Pandas, Plotly, and Streamlit.

---

## 🎯 Project Objectives

* Analyze overall sales and profit performance.
* Identify high-performing product categories and products.
* Analyze monthly sales trends.
* Understand customer segments and regional performance.
* Identify loss-making sub-categories.
* Analyze the relationship between discounts and profit.
* Generate useful business insights and recommendations.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* OpenPyXL
* Git and GitHub
* VS Code

---

## 📊 Dataset

The project uses a Superstore sales dataset containing information about:

* Orders
* Customers
* Products
* Categories
* Sales
* Quantity
* Discounts
* Profit
* Regions
* Order and shipping dates

**Dataset file:** `Superstore.csv`

The dataset contains **10,800 records and 21 columns**.

---

## 📈 Dashboard Features

### 1. Executive Overview

Displays important business KPIs such as:

* Total Sales
* Total Profit
* Total Quantity
* Total Orders

### 2. Sales Analysis

* Sales by Category
* Monthly Sales Trend
* Sales by Region

### 3. Product Analysis

* Sales by Sub-Category
* Top 10 Products by Sales

### 4. Customer Analysis

* Sales by Customer Segment
* Number of Customers by Region

### 5. Profit & Risk Analysis

* Profit by Category
* Loss-Making Sub-Categories
* Discount vs Profit Analysis

### 6. Interactive Filters

Users can filter the dashboard based on:

* Region
* Category

All charts and KPIs update according to the selected filters.

### 7. Business Insights

The dashboard automatically identifies:

* Top sales category
* Top sales region
* Top customer segment
* Most profitable category

It also provides business recommendations based on the analysis.

---

## 🔍 Key Business Insights

The dashboard helps businesses understand:

* Which categories generate the highest sales.
* Which regions contribute significantly to revenue.
* Which customer segments generate more sales.
* Which products and sub-categories perform well.
* Which sub-categories generate losses.
* How discounts are associated with profitability.
* Where businesses can improve their sales and profit strategies.

---

## ▶️ How to Run the Project

### Step 1: Clone or Download the Repository

Download the repository to your computer and open the project folder in VS Code.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit Dashboard

```bash
streamlit run app.py
```

### Step 6: Open the Dashboard

Streamlit will display a local URL in the terminal.

Open that URL in your web browser to view the dashboard.

---

## 📁 Project Structure

```text
E-Commerce-Sales-Analytics/
│
├── app.py
├── Superstore.csv
├── requirements.txt
└── README.md
```

**Note:** The `.venv` folder is used only on the local computer and is not uploaded to GitHub.

---

## 💡 Business Recommendations

* Focus marketing efforts on high-performing categories and regions.
* Review loss-making sub-categories and products.
* Monitor discounts to maintain profitability.
* Understand high-value customer segments.
* Use monthly sales trends for inventory and promotional planning.

---

## 🚀 Future Enhancements

* Add date-based filters.
* Add sales forecasting.
* Add advanced customer analysis.
* Add downloadable reports.
* Connect the dashboard to a live database.
* Deploy the dashboard online.

---

## 🎓 Internship Project

**IBM SkillsBuild Academic Internship**

**Domain:** Data Analytics with AI

---

## 👩‍💻 Author

**Vavilala Bhargavi**

B.Tech – Data Science

Siddhartha Institute of Engineering and Technology
