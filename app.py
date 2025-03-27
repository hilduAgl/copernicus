import streamlit as st
import pandas as pd
import plotly.express as px

# Sample transactions data
data = {
    "Date": ["2025-03-01", "2025-03-02", "2025-03-03", "2025-03-04"],
    "Description": ["Groceries", "Rent", "Coffee", "Electricity Bill"],
    "Amount": [-20000, -150000, -600, -12000],
    "Category": ["Food", "Housing", "Entertainment", "Utilities"]
}
df = pd.DataFrame(data)

def main():
    st.set_page_config(page_title="Budgeting App Demo", layout="wide")
    st.title("Financial Overview")
    
    # Summary Metrics
    total_spent = df[df["Amount"] < 0]["Amount"].sum()
    total_income = 500000  # Placeholder for income
    remaining_budget = total_income + total_spent
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"ISK {total_income:,}")
    col2.metric("Total Spent", f"ISK {total_spent:,}")
    col3.metric("Remaining Budget", f"ISK {remaining_budget:,}")
    
    # Spending Breakdown Chart
    category_totals = df.groupby("Category")["Amount"].sum().abs().reset_index()
    fig = px.pie(category_totals, names="Category", values="Amount", title="Spending Breakdown")
    st.plotly_chart(fig, use_container_width=True)
    
    # Transactions Table
    st.subheader("Recent Transactions")
    st.dataframe(df, use_container_width=True)
    
if __name__ == "__main__":
    main()
