import streamlit as st

st.set_page_config(page_title="Bank Loan Dashboard", layout="wide")

st.title("🏦 Bank Loan Approval Dashboard")
st.subheader("Smart Loan Eligibility Checker")

st.markdown("---")

# Inputs (ONLY ONCE)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])

income = st.number_input("Applicant Income", 0)
loan_amount = st.number_input("Loan Amount", 0)
interest = st.number_input("Rate of Interest (%)", value=8.5)

st.markdown("---")

# Logic (same rule)
if st.button("Check Eligibility"):

    if income >= loan_amount:
        st.success("✅ LOAN APPROVED")
    else:
        st.error("❌ LOAN REJECTED")
