# credit-card-fraud-detection

# 💳 Credit Card Fraud Detection

This is a Flask-based web application that predicts whether a given credit card transaction is **legitimate** or **fraudulent** using a pre-trained machine learning model.

---

## 🚀 Features

- Built with **Flask** (Python backend)
- Simple, clean **HTML/CSS** frontend
- Takes user input for `Time` and `Amount`
- Randomly fetches real `V1–V28` features from actual data samples
- Displays whether the transaction is **Fraud** or **Legit**

---

## 🧠 Model Info

- Machine Learning Model: `RandomForestClassifier`, `XGB`, `GB`
- Input Features: `Time`, `V1` through `V28`, `Amount`
- Trained on: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)

---