# 🏦 AI Financial Fraud Detection System

An AI-powered Financial Fraud Detection System that uses Machine Learning to identify fraudulent financial transactions in real time. The project consists of a FastAPI backend, a Streamlit dashboard, and an XGBoost machine learning model for fraud prediction.

---

## 🚀 Live Demo

### 🌐 Streamlit Dashboard
https://ai-financial-fraud-detection-awsu5jc7zwvygjqusz9qm6.streamlit.app/

### ⚡ FastAPI Backend
https://ai-financial-fraud-detection.onrender.com

---

# 📌 Project Overview

Financial fraud has become one of the biggest challenges in digital banking and online payments. This project leverages Machine Learning to analyze transaction patterns and classify transactions as either legitimate or fraudulent.

The application provides:

- Real-time fraud prediction
- Batch transaction analysis
- Interactive analytics dashboard
- Explainable AI insights
- AI-powered fraud assistant
- REST API for integration

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## Machine Learning
- XGBoost
- Scikit-learn
- SHAP (Explainable AI)

## Database
- SQLite
- SQLAlchemy

## Data Processing
- Pandas
- NumPy

## Visualization
- Plotly

## Deployment
- Render (Backend)
- Streamlit Community Cloud (Frontend)

---

# 📂 Project Structure

```
AI-Financial-Fraud-Detection/
│
├── backend/
│   ├── ai/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── app.py
│   └── requirements.txt
│
├── dashboard/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── config.py
│   └── app.py
│
├── models/
├── notebooks/
├── data/
├── requirements.txt
└── README.md
```

---

# ✨ Features

## ✅ Single Transaction Prediction

Predict whether an individual transaction is fraudulent.

---

## ✅ Batch Prediction

Upload a CSV file containing multiple transactions and receive fraud predictions for all transactions.

---

## ✅ Analytics Dashboard

Visualize:

- Fraud distribution
- Prediction statistics
- Transaction trends
- Model outputs

---

## ✅ Explainable AI

Uses SHAP to explain why a transaction was classified as fraudulent.

---

## ✅ AI Fraud Assistant

Provides AI-generated summaries and explanations for fraud detection results.

---

## ✅ REST API

FastAPI endpoints enable seamless integration with external applications.

Example endpoints:

- `/predict`
- `/report`
- `/docs`

---

# 🧠 Machine Learning Model

Model Used:

- XGBoost Classifier

Dataset:

- Credit Card Fraud Detection Dataset

Techniques Used:

- Data preprocessing
- Feature scaling
- Class imbalance handling
- Model training
- Model evaluation

---

# 📊 Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/141211hub/AI-Financial-Fraud-Detection.git
```

---

## Navigate

```bash
cd AI-Financial-Fraud-Detection
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
cd backend

uvicorn app:app --reload
```

---

## Run Dashboard

```bash
cd dashboard

streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots here after deployment.

Examples:

- Dashboard Home
- Fraud Prediction
- Analytics Page
- Explainability
- Batch Prediction

---

# 📈 Future Enhancements

- Deep Learning models
- Real-time transaction streaming
- Email/SMS fraud alerts
- Cloud database integration
- User authentication
- Role-based access control
- Advanced anomaly detection

---

# 👩‍💻 Developed By

**Janhvi Chaturvedi**

B.Tech Computer Science & Engineering

United University, Prayagraj

GitHub:
https://github.com/141211hub

---

# 📄 License

This project is developed for educational and internship purposes.
