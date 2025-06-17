
# 📄 Project Report: Term Deposit Subscription Predictor

## 🔍 Project Overview

This project implements a machine learning-powered web application that predicts whether a bank client will subscribe to a term deposit. The application, built using **Streamlit**, utilizes a trained **Logistic Regression pipeline** based on the **UCI Bank Marketing Dataset**.

---

## 🎯 Objective

To assist financial institutions in identifying clients who are likely to subscribe to a term deposit product. This can enhance targeted marketing efforts, reduce operational costs, and improve campaign conversion rates.

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Streamlit** – Web interface for the prediction app
- **Scikit-learn** – For model building and preprocessing
- **Imbalanced-learn** – To apply SMOTE for class balancing
- **Pandas / Numpy** – Data manipulation
- **Joblib** – Model persistence (serialization)

---

## 📊 Model Summary

- **Algorithm**: Logistic Regression (with pipeline)
- **Training Accuracy**: **84.51%**
- **Test Accuracy**: **83.57%**

### 📈 Training Performance
| Metric     | Class 0 (Not Subscribed) | Class 1 (Subscribed) |
|------------|--------------------------|------------------------|
| Precision  | 0.97                     | 0.42                   |
| Recall     | 0.85                     | 0.82                   |
| F1-score   | 0.91                     | 0.55                   |

> **Confusion Matrix (Train)**  
> [[33866  6056]  
>  [  948  4341]]

### 📈 Test Performance
| Metric     | Class 0 (Not Subscribed) | Class 1 (Subscribed) |
|------------|--------------------------|------------------------|
| Precision  | 0.97                     | 0.39                   |
| Recall     | 0.84                     | 0.79                   |
| F1-score   | 0.90                     | 0.53                   |

> **Confusion Matrix (Test)**  
> [[3365  635]  
>  [ 108  413]]

🔎 **Insights**:
- The model performs very well for the majority class (clients who do not subscribe).
- Despite class imbalance, it achieves **high recall (~79–82%) for subscribed clients**, making it suitable for identifying potential conversions.
- Moderate precision on the positive class means some false positives remain, but this can be improved with advanced modeling techniques.

---

## 📥 User Inputs

Users enter information through a form including:

- **Demographics**: `age`, `job`, `marital`, `education`
- **Financial details**: `default`, `balance`, `housing`, `loan`
- **Contact & Campaign**: `contact`, `day`, `month`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`

---

## 📈 Prediction Output

Upon form submission:
- The model calculates the **probability** of the client subscribing.
- A threshold of 0.5 is used:
  - ✅ If probability ≥ 0.5 → "**Client is likely to subscribe**"
  - ❌ If probability < 0.5 → "**Client is unlikely to subscribe**"
- The actual probability is also displayed for user insight.

---

## 🧪 Model Deployment

- The trained model is saved as `bank_model.pkl` using `joblib`.
- `app2.py` handles model loading and prediction logic.
- Deployed locally and optionally on **Streamlit Cloud** for online access.

---

## ✅ Future Improvements

- **Improve Precision (Class 1)**:
  - Tune the classification threshold.
  - Implement advanced models such as **XGBoost** or **Random Forest**.
  - Combine **SMOTE** with **Tomek Links** to reduce noise and improve balance.

- **Model Explainability**:
  - Use **SHAP** or **LIME** for better transparency in predictions.

- **Scalability & Access**:
  - Deploy on **Streamlit Cloud**, **AWS**, or **Heroku** to make the app available to a broader audience.
