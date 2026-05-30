import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Page settings
st.set_page_config(page_title="Loan Prediction App", layout="wide")

# Background and text styling
st.markdown("""
<style>
.stApp {
background: linear-gradient(to right, #141E30, #243B55);
color: white;
}
h1,h2,h3,label,p{
color:white !important;
}
</style>
""", unsafe_allow_html=True)

# Sample dataset
loan_data = pd.DataFrame({
'Gender':['Male','Male','Female','Male','Female','Male','Female','Male','Female','Male'],
'Married':['Yes','Yes','No','Yes','No','Yes','No','Yes','No','Yes'],
'Education':['Graduate','Graduate','Graduate','Not Graduate','Graduate','Graduate','Not Graduate','Graduate','Graduate','Graduate'],
'ApplicantIncome':[5000,3000,2500,4000,1500,6000,2000,7000,1800,6500],
'LoanAmount':[100,80,60,120,50,150,70,200,55,170],
'Loan_Status':['Y','Y','N','Y','N','Y','N','Y','N','Y']
})

# Convert text to numbers
loan_data.replace({
'Gender': {'Male':1,'Female':0},
'Married': {'Yes':1,'No':0},
'Education': {'Graduate':1,'Not Graduate':0},
'Loan_Status': {'Y':1,'N':0}
}, inplace=True)

# Features and target
X = loan_data.drop(columns=['Loan_Status'])
y = loan_data['Loan_Status']

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X,y)

# Sidebar inputs
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
1000,
10000,
5000
)

loan_amount = st.sidebar.number_input(
"Loan Amount",
10,
300,
100
)

# Convert inputs
gender = 1 if gender=="Male" else 0
married = 1 if married=="Yes" else 0
education = 1 if education=="Graduate" else 0

# Main title
st.title("🏦 Loan Prediction System")

st.write("Fill details from left side panel")

# Predict button
if st.button("Predict Loan Status"):

    prediction = model.predict(
        [[gender,
          married,
          education,
          income,
          loan_amount]]
    )

    if prediction[0]==1:

        st.success("✅ Loan Approved")

        st.markdown(
        "<h2 style='text-align:center;'>Congratulations 🎉</h2>",
        unsafe_allow_html=True)

        st.snow()

    else:

        st.error("❌ Loan Rejected")

        st.markdown(
        "<h2 style='text-align:center;'>Sorry, Loan Rejected</h2>",
        unsafe_allow_html=True)