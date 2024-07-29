import streamlit as st
import pandas as pd

# Sample function to test Streamlit setup
def main():
    st.title('Asset Allocation Report Generator')

    age = st.number_input('Enter your age:', min_value=1, max_value=100, value=21)
    annual_salary = st.number_input('Enter your annual salary (₹):', min_value=0, value=1000000)
    monthly_expenses = st.number_input('Enter your monthly expenses (₹):', min_value=0, value=50000)
    monthly_loan = st.number_input('Enter your monthly loan repayment (₹):', min_value=0, value=10000)
    monthly_emergency_fund = st.number_input('Enter your monthly emergency fund contribution (₹):', min_value=0, value=10000)

    if st.button('Generate Report'):
        st.write(f'Age: {age}')
        st.write(f'Annual Salary: ₹{annual_salary}')
        st.write(f'Monthly Expenses: ₹{monthly_expenses}')
        st.write(f'Monthly Loan Repayment: ₹{monthly_loan}')
        st.write(f'Monthly Emergency Fund Contribution: ₹{monthly_emergency_fund}')

if __name__ == '__main__':
    main()
