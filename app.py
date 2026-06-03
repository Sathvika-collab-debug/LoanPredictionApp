import streamlit as st

st.set_page_config(page_title="Bank Loan Dashboard", layout="wide")

st.title("🏦 Bank Loan Approval Dashboard")

st.markdown("---")

# Inputs (ONLY ONCE)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])

income = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
interest = st.number_input("Rate of Interest (%)", min_value=0.0, value=8.5)

st.markdown("---")

# Logic (SAME RULE)
if st.button("Check Eligibility"):

    if income >= loan_amount:
        st.success("✅ LOAN APPROVED")
    else:
        st.error("❌ LOAN REJECTED")
