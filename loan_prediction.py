import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ---------------- Data ----------------

loan_data = pd.read_csv("loan_data.csv")

loan_data.replace({
    'Gender': {'Male':1,'Female':0},
    'Married': {'Yes':1,'No':0},
    'Education': {'Graduate':1,'Not Graduate':0},
    'Loan_Status': {'Y':1,'N':0}
}, inplace=True)

loan_data = loan_data.infer_objects(copy=False)

X = loan_data.drop(columns='Loan_Status')
y = loan_data['Loan_Status'].astype(int)

# ---------------- Train Model ----------------

model = LogisticRegression(max_iter=1000)

model.fit(X,y)

# ---------------- Background Design ----------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(to right,#4facfe,#00f2fe);
}

.title{
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
}

.result{
text-align:center;
font-size:30px;
font-weight:bold;
padding:20px;
border-radius:15px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------

st.markdown(
'<p class="title">🏦 Loan Prediction App</p>',
unsafe_allow_html=True
)

# ---------------- Sidebar Inputs ----------------

st.sidebar.title("Enter Details")

gender = st.sidebar.selectbox(
    "Gender",
    ["Male","Female"]
)

married = st.sidebar.selectbox(
    "Married",
    ["Yes","No"]
)

education = st.sidebar.selectbox(
    "Education",
    ["Graduate","Not Graduate"]
)

income = st.sidebar.number_input(
    "Applicant Income",
    min_value=0
)

loan_amount = st.sidebar.number_input(
    "Loan Amount",
    min_value=0
)

# ---------------- Convert Inputs ----------------

gender = 1 if gender=="Male" else 0
married = 1 if married=="Yes" else 0
education = 1 if education=="Graduate" else 0

# ---------------- Prediction ----------------

if st.sidebar.button("Predict Loan Status"):

    prediction = model.predict([[
        gender,
        married,
        education,
        income,
        loan_amount
    ]])

    if prediction[0]==1:

        st.balloons()

        st.markdown(
        '<div class="result">✅ LOAN APPROVED</div>',
        unsafe_allow_html=True
        )

        st.success("Congratulations! Loan Approved")

    else:

        st.markdown(
        '<div class="result">❌ LOAN REJECTED</div>',
        unsafe_allow_html=True
        )

        st.error("Sorry! Loan Rejected")