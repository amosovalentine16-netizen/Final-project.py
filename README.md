# Customer Churn Prediction Using Machine Learning

# Project Overview

Customer churn is a significant challenge for telecommunications companies because losing customers directly affects revenue and profitability. Predicting which customers are likely to leave enables companies to implement targeted retention strategies and improve customer satisfaction.

This project develops and evaluates machine learning models to predict customer churn using customer demographics, account information, billing details, and subscribed services.



# Problem Statement

Telecommunication companies face increasing customer attrition due to competition and changing customer preferences.

The objective of this project is to build a predictive model capable of identifying customers who are likely to churn, allowing the company to take proactive measures to retain them.



# Project Objectives

- Analyze customer behavior and churn patterns.
- Identify factors influencing customer churn.
- Build predictive machine learning models.
- Compare model performance using multiple evaluation metrics.
- Generate actionable business recommendations.



# Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains information on:

- Customer demographics
- Account information
- Services subscribed
- Billing details
- Customer churn status

# Features

Some important variables include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Internet Service
- Online Security
- Tech Support
- Contract Type
- Monthly Charges
- Total Charges
- Churn



# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook



# Project Workflow

# 1. Data Collection and Exploration

- Loaded and inspected the dataset.
- Explored data structure and feature distributions.
- Identified potential data quality issues.

# 2. Data Cleaning and Preprocessing

- Converted TotalCharges to numeric format.
- Removed missing values.
- Removed unnecessary identifiers.
- Encoded categorical variables.
- Scaled numerical features.

# 3. Exploratory Data Analysis

Key visualizations included:

- Churn distribution
- Contract type vs churn
- Monthly charges distribution
- Monthly charges by churn status
- Tenure by churn status
- Correlation heatmap
- Feature importance analysis

# 4. Feature Engineering

Created additional features:

- Tenure Group
- Revenue Per Month

These features improved understanding of customer behavior and churn patterns.

# 5. Model Development

Three machine learning models were trained:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier



# Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---------|---------|---------|---------|---------|---------|
| Logistic Regression | 79.53% | 63.87% | 52.94% | 57.89% | 83.47% |
| Decision Tree | 71.71% | 46.88% | 48.13% | 47.49% | 64.16% |
| Random Forest | 78.96% | 63.00% | 50.53% | 56.08% | 81.83% |



# Best Model

# Logistic Regression

Performance:

- Accuracy: 79.53%
- Precision: 63.87%
- Recall: 52.94%
- F1 Score: 57.89%
- ROC-AUC: 83.47%

The Logistic Regression model achieved the highest overall performance and was selected as the final model.


# Key Findings

Feature importance analysis revealed that the strongest predictors of churn are:

1. Total Charges
2. Customer Tenure
3. Revenue Per Month
4. Monthly Charges
5. Electronic Check Payment Method
6. Fiber Optic Internet Service
7. Contract Type

### Insights

- Customers with shorter tenure are more likely to churn.
- Month-to-month contracts have higher churn rates.
- Higher monthly charges increase churn risk.
- Long-term contracts improve retention.
- Customers with Online Security and Tech Support are less likely to churn.



# Business Recommendations

# Strengthen Customer Onboarding

Focus retention efforts on new customers during their first year.

# Promote Long-Term Contracts

Provide incentives for customers to switch to annual contracts.

# Improve Customer Value

Review pricing strategies and service offerings for high-risk customers.

# Increase Adoption of Support Services

Encourage subscriptions to Online Security and Tech Support services.

# Target High-Risk Payment Groups

Develop retention campaigns for customers using electronic check payment methods.



## Future Improvements

Potential enhancements include:

- Hyperparameter tuning using GridSearchCV
- XGBoost implementation
- LightGBM implementation
- Streamlit dashboard deployment
- Real-time churn prediction system


# Author

Valentine Amoso


# Skills

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Data Analysis
- Data Visualization
- Machine Learning
