# 💳 Smart Lender – Loan Approval Prediction System

## 📌 Overview

Smart Lender is a machine learning-based web application that predicts whether a loan application is likely to be approved or rejected based on applicant details. The system helps financial institutions make faster and more accurate loan approval decisions by analyzing applicant information using machine learning algorithms.

The application processes details such as gender, marital status, education, employment status, applicant income, co-applicant income, loan amount, loan term, credit history, and property area. Multiple machine learning models were trained and evaluated, including Decision Tree, Random Forest, K-Nearest Neighbors (KNN), and XGBoost. Among these, the **Random Forest Classifier** achieved the best performance and was selected for deployment.

The application is built using **Python**, **Flask**, **Scikit-learn**, and is deployed on **Render** for real-time loan prediction.

---

## 🚀 Features

- Predicts loan approval instantly
- User-friendly web interface
- Multiple machine learning model comparison
- High prediction accuracy using Random Forest
- Real-time prediction through Flask
- Cloud deployment on Render

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Pickle
- HTML
- Render

---

## 📂 Project Structure

```
Smart_Lender_project/
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
├── codely.ipynb
└── README.md
```

---

## 🤖 Machine Learning Models

- Decision Tree
- Random Forest ✅ (Selected)
- K-Nearest Neighbors (KNN)
- XGBoost

Random Forest achieved the highest performance and was selected as the final model for deployment.

---

## ⚙️ Workflow

1. Load Dataset
2. Data Cleaning
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature Encoding
6. Train-Test Split
7. Train Multiple Models
8. Compare Model Performance
9. Select Random Forest
10. Save Model using Pickle
11. Integrate with Flask
12. Deploy on Render

---

## 🌐 Live Demo

https://smart-lender-app-e7x5.onrender.com

---

## ▶️ Installation

```bash
git clone https://github.com/your-username/Smart-Lender.git
cd Smart-Lender
pip install -r requirements.txt
python app.py
```

---

## 📄 License

This project is intended for educational and learning purposes.
