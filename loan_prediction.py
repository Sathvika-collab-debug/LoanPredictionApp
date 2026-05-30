import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pyttsx3

# ---------------- Voice Function ----------------

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------------- Dataset ----------------

data = {
'Gender':['Male','Male','Female','Male','Female','Male','Female','Male','Female','Male'],
'Married':['Yes','Yes','No','Yes','No','Yes','No','Yes','No','Yes'],
'Education':['Graduate','Graduate','Graduate','Not Graduate','Graduate','Graduate','Not Graduate','Graduate','Graduate','Graduate'],
'ApplicantIncome':[5000,3000,2500,4000,1500,6000,2000,7000,1800,6500],
'LoanAmount':[100,80,60,120,50,150,70,200,55,170],
'Loan_Status':['Y','Y','N','Y','N','Y','N','Y','N','Y']
}

loan_data = pd.DataFrame(data)

loan_data.replace({
'Gender':{'Male':1,'Female':0},
'Married':{'Yes':1,'No':0},
'Education':{'Graduate':1,'Not Graduate':0},
'Loan_Status':{'Y':1,'N':0}
}, inplace=True)

X = loan_data.drop(columns='Loan_Status')
Y = loan_data['Loan_Status']

model = LogisticRegression(max_iter=1000)
model.fit(X,Y)

# ---------------- Page Design ----------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(to right,#4facfe,#00f2fe);
}

.title{
text-align:center;
font-size:42px;
font-weight:bold;
color:white;
}

.result{
padding:20px;
border-radius:15px;
font-size:35px;
font-weight:bold;
text-align:center;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"<div class='title'>🏦 Loan Prediction System</div>",
unsafe_allow_html=True)

# ---------------- Sidebar Inputs ----------------

st.sidebar.header("Enter Details")

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

loan = st.sidebar.number_input(
"Loan Amount",
min_value=0
)

predict = st.sidebar.button(
"Predict Loan Status"
)

# ---------------- Prediction ----------------

if predict:

    g = 1 if gender=="Male" else 0
    m = 1 if married=="Yes" else 0
    e = 1 if education=="Graduate" else 0

    prediction = model.predict(
        [[g,m,e,income,loan]]
    )

    if prediction[0]==1:

        st.markdown(
        """
        <div class='result'
        style='background:green;color:white'>
        ✅ LOAN APPROVED
        </div>
        """,
        unsafe_allow_html=True)

        speak(
        "Congratulations. Your loan is approved"
        )

    else:

        st.markdown(
        """
        <div class='result'
        style='background:red;color:white'>
        ❌ LOAN REJECTED
        </div>
        """,
        unsafe_allow_html=True)

        speak(
        "Sorry. Your loan application is rejected"
        )