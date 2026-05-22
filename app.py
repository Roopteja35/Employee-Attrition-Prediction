import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Title
st.title("Employee Attrition Prediction App")

# Input fields
age = st.number_input("Age", 18, 60)
monthly_income = st.number_input("Monthly Income", 1000, 100000)
years_at_company = st.number_input("Years at Company", 0, 40)
job_satisfaction = st.slider("Job Satisfaction", 1, 4)
work_life_balance = st.slider("Work Life Balance", 1, 4)
performance_rating = st.slider("Performance Rating", 1, 5)
projects = st.number_input("Project Count", 1, 10)
hours = st.number_input("Hours per Week", 20, 80)

# Feature engineering (same as model)
income_per_year = monthly_income / (years_at_company + 1)
work_stress = hours * projects
promotion_gap = years_at_company / (years_at_company + 1)

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Prediction button
if st.button("Predict"):
    
    data = np.array([[age, monthly_income, years_at_company,
                      job_satisfaction, work_life_balance,
                      performance_rating, projects, hours,
                      income_per_year, work_stress, promotion_gap]])
    
    data = scaler.transform(data)
    
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error("Employee is likely to leave")
    else:
        st.success("Employee is likely to stay")

prob = model.predict_proba(data)[0][1]

st.write(f"Attrition Probability: {prob:.2f}")