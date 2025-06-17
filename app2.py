import streamlit as st
import joblib
import pandas as pd

# Load the trained pipeline
model = joblib.load("Data_Aalytics_pathway_Assessment/bank_model.pkl")  # Ensure this file is in the same folder or provide the correct path

st.title("📊 Term Deposit Subscription Predictor")
st.write("Will a client subscribe to a term deposit based on their profile?")

# Input features from the dataset
age = st.number_input("Age", min_value=18, max_value=100, value=30)
job = st.selectbox("Job", ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
                           'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Default Credit?", ['yes', 'no'])
balance = st.number_input("Account Balance", min_value=-10000, max_value=100000, value=1000)
housing = st.selectbox("Housing Loan?", ['yes', 'no'])
loan = st.selectbox("Personal Loan?", ['yes', 'no'])
contact = st.selectbox("Contact Type", ['cellular', 'telephone', 'unknown'])
day = st.slider("Last Contact Day of the Month", 1, 31, 15)
month = st.selectbox("Last Contact Month", ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                                            'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
duration = st.number_input("Last Contact Duration (seconds)", min_value=0, value=100)
campaign = st.number_input("Number of Contacts During Campaign", min_value=1, value=1)
pdays = st.number_input("Days Since Last Contact (-1 means never)", value=-1)
previous = st.number_input("Number of Previous Contacts", min_value=0, value=0)
poutcome = st.selectbox("Outcome of Previous Campaign", ['success', 'failure', 'other', 'unknown'])

# On submit
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "day": day,
        "month": month,
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome,
    }])

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"✅ The client is likely to **subscribe** to the term deposit. (Probability: {prob:.2f})")
    else:
        st.error(f"❌ The client is unlikely to subscribe. (Probability: {prob:.2f})")
