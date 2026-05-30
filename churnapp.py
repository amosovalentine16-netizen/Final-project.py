import streamlit as st
import pandas as pd
import joblib

st.title("Customer Churn Prediction App")

st.write("This app predicts whether a telecom customer is likely to churn.")

model = joblib.load("logistic_churn_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("model_columns.pkl")

tenure = st.number_input("Tenure in months", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=800.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

if st.button("Predict Churn"):
    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Revenue_Per_Month": [total_charges / tenure if tenure != 0 else 0],
        "Contract_One year": [1 if contract == "One year" else 0],
        "Contract_Two year": [1 if contract == "Two year" else 0],
        "InternetService_Fiber optic": [1 if internet == "Fiber optic" else 0],
        "InternetService_No": [1 if internet == "No" else 0],
        "PaymentMethod_Electronic check": [1 if payment == "Electronic check" else 0],
        "PaymentMethod_Mailed check": [1 if payment == "Mailed check" else 0],})

    input_data = input_data.reindex(columns=columns, fill_value=0)
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"Customer is likely to churn. Probability: {probability:.2%}")
    else:
        st.success(f"Customer is unlikely to churn. Probability: {probability:.2%}")
