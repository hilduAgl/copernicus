import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Sample transaction data
data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "Category": ["Food", "Rent", "Utilities", "Transport", "Entertainment", "Shopping", "Healthcare", "Savings", "Insurance", "Misc"],
    "Amount": [-50, -800, -100, -30, -60, -120, -70, 200, -90, -40],
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])  # Ensure Date is datetime format

# Sample asset data
assets = {
    "Asset": ["Savings Account", "Stocks", "Real Estate", "Car", "Pension Fund"],
    "Value": [5000, 12000, 250000, 15000, 30000],
}

assets_df = pd.DataFrame(assets)

# Streamlit App UI
st.title("💰 Personal Financial Dashboard")

# Date Filter
st.sidebar.header("📅 Select Date Range")
start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

# Convert to datetime for filtering
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# Spending Breakdown
st.header("📊 Spending Breakdown")
spending_df = filtered_df[filtered_df["Amount"] < 0]

# st.write(spending_df)  # Check if the DataFrame is empty

if not spending_df.empty:
    fig = px.pie(spending_df, names="Category", values=spending_df["Amount"].abs(), title="Expenses by Category")
    st.plotly_chart(fig)
else:
    st.write("No expenses in the selected date range.")

# Transaction History
st.subheader("📄 Recent Transactions")
st.dataframe(filtered_df)

# Asset & Ownership Breakdown
st.header("🏠 Asset & Ownership Breakdown")
st.dataframe(assets_df)

# Financial Summary
total_assets = assets_df["Value"].sum()
total_income = filtered_df[filtered_df["Amount"] > 0]["Amount"].sum()
total_expenses = filtered_df[filtered_df["Amount"] < 0]["Amount"].sum()
net_worth = total_assets + total_income + total_expenses

st.header("📈 Financial Outlook Summary")
st.metric("Total Assets", f"${total_assets:,}")
st.metric("Total Income", f"${total_income:,}")
st.metric("Total Expenses", f"${total_expenses:,}")
st.metric("Net Worth", f"${net_worth:,}")

# Conclusion
st.success("🚀 This is just a demo! More features like predictive analytics can be added.")
