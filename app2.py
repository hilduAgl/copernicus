import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")

# Sample transaction data (for net worth calculation)
data = {
    "Date": pd.date_range(start="2024-03-01", periods=15, freq="D"),
    "Category": ["Food", "Mortgage", "Utilities", "Transport", "Entertainment", "Shopping", "Healthcare", "Savings", "Insurance", "Misc", "Investment"],
    "Amount": [-50, -800, -100, -30, -60, -120, -70, -500, -90, -40, -1000, 3000, 500, 200, 800],  # Negative = expenses
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])  # Ensure Date is in datetime format

# Sample asset data (Initial assets)
assets = {
    "Asset": ["Savings Account", "Stocks", "Real Estate", "Car", "Pension Fund"],
    "Value": [5000, 12000, 250000, 15000, 30000],
}

assets_df = pd.DataFrame(assets)

# Streamlit App UI
st.title("💰 Personal Financial Dashboard")

# Sidebar: Set Monthly Budget Limits
st.sidebar.header("📊 Set Monthly Budget Limits")
categories = df["Category"].unique()
budget_limits = {}

for category in categories:
    budget_limits[category] = st.sidebar.number_input(f"{category} Budget Limit", min_value=0, value=500)

# Date Filter
st.sidebar.header("📅 Select Date Range")
start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

# Filter transactions based on selected date range
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# Spending Breakdown (Includes Savings & Investments)
st.header("📊 Spending Breakdown")
spending_df = filtered_df[filtered_df["Amount"] < 0]  # Includes all expenses (Savings & Investments too)

if not spending_df.empty:
    fig = px.pie(spending_df, names="Category", values=spending_df["Amount"].abs(), title="Expenses by Category (Including Savings & Investments)")
    st.plotly_chart(fig)
else:
    st.warning("⚠️ No expenses found in the selected date range.")

budget_status = {}

# Budget Tracking Section
st.header("📏 Budget Tracking")

for category in categories:
    spent = abs(spending_df[spending_df["Category"] == category]["Amount"].sum())
    limit = budget_limits.get(category, 0)
    percent_used = (spent / limit) * 100 if limit > 0 else 0

    # Determine color based on percentage used
    if percent_used < 50:
        bar_color = "#4CAF50"  # Green
    elif percent_used < 80:
        bar_color = "#FFC107"  # Yellow
    else:
        bar_color = "#F44336"  # Red

    # Display category title and amount spent with smaller font size and black text
    st.markdown(f'<p style="font-size: 12px; color: #000000;">{category}: ${spent} / ${limit}</p>', unsafe_allow_html=True)

    # Custom HTML for color-changing progress bar with smaller height and reduced margin
    progress_html = f"""
    <div style="background-color: #ddd; border-radius: 10px; width: 100%; height: 3px; margin-bottom: 4px;">
        <div style="width: {min(percent_used, 100)}%; height: 100%; background-color: {bar_color}; border-radius: 10px;"></div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)



# Sample Loan & Debt Data
loans_data = {
    "Loan Type": ["Student Loan", "Car Loan", "Mortgage", "Credit Card"],
    "Total Amount": [20000, 15000, 250000, 5000],
    "Remaining Balance": [12000, 8000, 200000, 3500],
    "Interest Rate (%)": [4.5, 3.2, 2.8, 19.9],
    "Monthly Payment": [200, 250, 1200, 150]
}

loans_df = pd.DataFrame(loans_data)

st.header("📉 Loans & Debts Status")

for index, row in loans_df.iterrows():
    paid_off_percentage = ((row["Total Amount"] - row["Remaining Balance"]) / row["Total Amount"]) * 100

    # Determine color based on how much has been paid off
    if paid_off_percentage < 25:
        bar_color = "#F44336"  # Red (high debt)
    elif paid_off_percentage < 75:
        bar_color = "#FFC107"  # Yellow (moderate progress)
    else:
        bar_color = "#4CAF50"  # Green (almost paid off)

    # Display loan details with smaller font size and black text
    st.markdown(
        f'<p style="font-size: 12px; color: #000000;">{row["Loan Type"]}: ${row["Remaining Balance"]:,} / ${row["Total Amount"]:,}</p>',
        unsafe_allow_html=True
    )

    # Custom HTML progress bar for loan repayment (smaller height, reduced margin)
    progress_html = f"""
    <div style="background-color: #ddd; border-radius: 10px; width: 100%; height: 3px; margin-bottom: 4px;">
        <div style="width: {paid_off_percentage}%; height: 100%; background-color: {bar_color}; border-radius: 10px;"></div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)


# Sample Loan & Debt Data
loans_data = {
    "Loan Type": ["Student Loan", "Car Loan", "Mortgage", "Credit Card"],
    "Total Amount": [20000, 15000, 250000, 5000],
    "Remaining Balance": [12000, 8000, 200000, 3500],
    "Interest Rate (%)": [4.5, 3.2, 2.8, 19.9],
    "Monthly Payment": [200, 250, 1200, 150]
}

loans_df = pd.DataFrame(loans_data)

# Sample Bank Account Data
bank_data = {
    "Date": pd.date_range(start="2024-01-01", periods=15, freq="D"),
    "Checking Account": [1200, 1150, 1100, 1000, 900, 800, 1500, 1600, 1700, 2000, 2200, 2500, 2700, 2900, 3100],
    "Savings Account": [5000, 5050, 5100, 5200, 5250, 5300, 5350, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100]
}

bank_df = pd.DataFrame(bank_data)

# Convert Date column to datetime format
bank_df["Date"] = pd.to_datetime(bank_df["Date"])

# Filter bank data by selected date range
bank_df_filtered = bank_df[(bank_df["Date"] >= pd.to_datetime(start_date)) & (bank_df["Date"] <= pd.to_datetime(end_date))]

# Transaction History
st.subheader("📄 Recent Transactions")
st.dataframe(filtered_df)

# Asset & Ownership Breakdown (Pie Chart)
st.header("🏠 Asset & Ownership Breakdown")
fig_assets = px.pie(assets_df, names="Asset", values="Value", title="Assets Breakdown")
st.plotly_chart(fig_assets)

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

# Net Worth Over Time Calculation
st.header("📉 Net Worth Over Time")
net_worth_data = df.copy()
net_worth_data["Net Worth"] = total_assets + net_worth_data["Amount"].cumsum()  # Cumulative net worth

# Filter net worth data by selected date range
net_worth_data = net_worth_data[(net_worth_data["Date"] >= pd.to_datetime(start_date)) & (net_worth_data["Date"] <= pd.to_datetime(end_date))]

# Line Chart for Net Worth Growth
fig_net_worth = px.line(net_worth_data, x="Date", y="Net Worth", title="Net Worth Over Time", markers=True)
st.plotly_chart(fig_net_worth)

st.success("🚀 More features like predictive analytics can be added!")
