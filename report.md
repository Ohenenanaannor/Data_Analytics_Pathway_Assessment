# 📄 Project Report: Term Deposit Subscription Predictor

## 🔍 Project Overview

This project implements a machine learning-based web application that predicts whether a bank client will subscribe to a term deposit based on their personal, financial, and campaign-related information. The app is deployed using **Streamlit** and leverages a trained **Logistic Regression pipeline** model built on the **UCI Bank Marketing Dataset**.

---

## 🎯 Objective

To assist banks in identifying potential clients who are likely to subscribe to a term deposit product, helping optimize marketing strategies, reduce costs, and increase conversion rates.

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Streamlit** – Web application UI
- **Scikit-learn** – Model training and preprocessing
- **Imbalanced-learn** – SMOTE for class balancing
- **Pandas/Numpy** – Data handling and transformation
- **Joblib** – Model serialization

---

## 📊 Model Summary

- **Algorithm**: Logistic Regression (via a pipeline)
- **Training Accuracy**: ~90.02%
- **Test Accuracy**: ~89.67%
- **Performance for Class 1 (Subscribed Clients)**:
  - **Precision**: ~0.56
  - **Recall**: ~0.49
  - **F1-score**: ~0.52

*Note: While accuracy is high, recall for the positive class (i.e., clients who actually subscribe) is moderate, indicating room for improvement via threshold tuning or advanced models like XGBoost.*

---

## 📥 User Inputs

The app accepts the following client and campaign-related inputs via a form:

- **Demographics**: `age`, `job`, `marital`, `education`
- **Credit info**: `default`, `balance`, `housing`, `loan`
- **Contact/campaign details**: `contact`, `day`, `month`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`

---

## 📈 Prediction Output

Once the user fills in the form and clicks “Predict”:

- The model computes the **probability** of subscription.
- If the probability is above 0.5:
  - ✅ The app returns: “**The client is likely to subscribe**”
- Otherwise:
  - ❌ The app returns: “**The client is unlikely to subscribe**”

Probability is also displayed for transparency.

---

## 🧪 Model Deployment

- The model is saved using `joblib` as `bank_model.pkl`.
- `app2.py` loads the model and runs predictions live.
- The app is deployed locally and optionally to **Streamlit Cloud**.

---

## ✅ Future Improvements

- **Increase Recall**:
  - Tune the classification threshold.
  - Test ensemble models (Random Forest, XGBoost).
  - Use SMOTE + Tomek Links for better balance and noise removal.
- **Explainability**:
  - Integrate SHAP or LIME to explain individual predictions.
- **Deployment**:
  - Host on Streamlit Cloud or AWS for broader access.
