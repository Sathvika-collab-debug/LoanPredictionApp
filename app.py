import streamlit as st

st.set_page_config(page_title="Loan App", layout="wide")

st.title("🏦 Loan Approval System")

income = st.number_input("Applicant Income", 0)
loan_amount = st.number_input("Loan Amount", 0)

if st.button("Check Eligibility"):

    if income >= loan_amount:
        st.success("✅ APPROVED")
    else:
        st.error("❌ REJECTED")
