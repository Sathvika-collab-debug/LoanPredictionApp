import streamlit as st

st.set_page_config(
    page_title="Bank Loan Dashboard",
    page_icon="🏦",
    layout="wide"
)

# TITLE

st.title("🏦 Bank Loan Approval Dashboard")
st.subheader("Smart Loan Eligibility Checker")

st.markdown("---")

# INPUT SECTION

st.header("📋 Applicant Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "Married",
        ["Yes", "No"]
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

with col2:

    income = st.number_input(
        "Applicant Income",
        min_value=0,
        value=0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=0
    )

    interest_rate = st.number_input(
        "Rate of Interest (%)",
        min_value=1.0,
        max_value=25.0,
        value=8.5
    )

st.markdown("---")

# DASHBOARD METRICS

c1, c2, c3 = st.columns(3)

c1.metric(
    "Applicant Income",
    f"₹ {income}"
)

c2.metric(
    "Loan Amount",
    f"₹ {loan_amount}"
)

c3.metric(
    "Interest Rate",
    f"{interest_rate}%"
)

st.markdown("---")

# PREDICTION

if st.button("Predict Loan Status"):

    score = 0

    # SCORE CALCULATION

    if income > loan_amount:
        score += 2

    if income > 5000:
        score += 1

    if education == "Graduate":
        score += 1

    if interest_rate < 12:
        score += 1

    st.header("🏦 Decision Result")

    # APPROVAL LOGIC

    if income >= loan_amount:

        st.success(
            "✅ LOAN APPROVED"
        )

        st.write(
            "Status: Low Risk Applicant"
        )

    else:

        st.error(
            "❌ LOAN REJECTED"
        )

        st.write(
            "Status: High Risk Applicant"
        )

    st.subheader(
        f"📊 Score: {score}/5"
    )
