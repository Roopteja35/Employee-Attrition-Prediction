# Employee Attrition Prediction Using Machine Learning

## Overview
This project focuses on predicting employee attrition using Machine Learning techniques. The system analyzes employee-related features such as job satisfaction, monthly income, work-life balance, project count, and working hours to determine whether an employee is likely to leave the organization.

The project includes:
  * Data preprocessing
  * Exploratory Data Analysis (EDA)
  * Feature engineering
  * SMOTE-based class balancing
  * Machine learning model training
  * Streamlit deployment for real-time prediction

## Features
  * Employee attrition prediction
  * Real-time prediction using Streamlit
  * Feature engineering for better performance
  * Class imbalance handling using SMOTE
  * Model comparison and evaluation
  * Confusion matrix and feature importance analysis

## Machine Learning Models Used
  * Logistic Regression
  * Random Forest
  * XGBoost
Among all models, XGBoost achieved the best accuracy.

## Technologies Used
  * Python
  * Pandas
  * NumPy
  * Scikit-learn
  * XGBoost
  * Matplotlib
  * Seaborn
  * Streamlit
  * Imbalanced-learn (SMOTE)

## Dataset
The dataset contains 10,000 employee records with attributes related to:
  * Age
  * Monthly Income
  * Job Satisfaction
  * Work-Life Balance
  * Project Count
  * Performance Rating
  * Years at Company
  * Working Hours
  * Attrition Status

## Feature Engineering
Additional features created:
  * Income per Year
  * Work Stress
  * Promotion Gap
These features improved prediction capability by capturing employee behavioral patterns.

## Project Workflow
  1. Data Collection
  2. Data Preprocessing
  3. Exploratory Data Analysis
  4. Feature Engineering
  5. SMOTE Class Balancing
  6. Model Training
  7. Model Evaluation
  8. Streamlit Deployment

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 49.05%   |
| Random Forest       | 77.65%   |
| XGBoost             | 79.60%   |


## Streamlit Application
The Streamlit web application allows users to:
  * Enter employee details
  * Predict employee attrition
  * View attrition probability in real time

## Future Improvements
  * SHAP Explainable AI integration
  * Deep Learning models
  * Cloud deployment
  * Real-time HR database integration
