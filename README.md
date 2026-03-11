# GenAI Financial Fraud Detection System

This project implements an AI-powered financial fraud detection system using anomaly detection and an interactive dashboard.

The system analyzes financial transaction patterns and identifies suspicious activities using a machine learning model and provides intelligent reasoning for flagged transactions.

---

## 🚀 Live Dashboard

Click below to explore the interactive fraud detection dashboard.

🔗 https://genai-financial-fraud-detection-khhkus8zmwetscgvfzzjeg.streamlit.app/

---

## 📌 Project Overview

Financial institutions process thousands of transactions daily. Detecting fraudulent activity in real time is a major challenge.

This project builds a **machine learning based fraud detection system** that:

- Detects abnormal transaction behavior
- Classifies suspicious transactions
- Visualizes data using an interactive dashboard
- Explains fraud patterns using AI-generated reasoning

---

## ⚡ Features

- Financial transaction anomaly detection
- Isolation Forest machine learning model
- Interactive Streamlit dashboard
- Fraud pattern analysis
- AI-powered reasoning explanations
- Real-time transaction filtering
- Visual transaction analytics

---

## 🧠 Workflow Architecture

![Workflow](images/workflow.png)

The system follows a structured fraud detection pipeline:

1. Transaction dataset loading
2. Data preprocessing and cleaning
3. Feature selection
4. StandardScaler normalization
5. Isolation Forest anomaly detection
6. Fraud classification
7. Interactive dashboard visualization
8. GenAI fraud reasoning

---

## 📊 Dashboard Preview

### Fraud Monitoring Dashboard

![Dashboard](images/dashboard.png)

### Transaction Amount Visualization

![Chart](images/chart.png)

### AI Fraud Reasoning

![Reasoning](images/reasoning.png)

---

## 🛠 Technology Stack

Python  
Pandas  
NumPy  
Scikit-learn  
Streamlit  
Plotly  
Generative AI  

---

## 🤖 Machine Learning Model

The system uses **Isolation Forest**, an unsupervised anomaly detection algorithm designed to detect rare and unusual patterns in large datasets.

Isolation Forest works by isolating anomalies instead of profiling normal data points.

Transactions predicted as anomalies are labeled as:

- **Suspicious** → Potential fraud detected
- **Normal** → Regular transaction pattern

---

## 📂 Project Structure
genai-financial-fraud-detection
│
├── app.py
├── bank_transactions_dataset.csv
├── requirements.txt
├── GenAI_Fraud_Detection.ipynb
├── README.md
│
└── images
├── workflow.png
├── dashboard.png
├── chart.png
└── reasoning.png


---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
git clone https://github.com/Tejavathshalini/genai-financial-fraud-detection.git


### 2️⃣ Navigate to the Project Folder
cd genai-financial-fraud-detection


### 3️⃣ Install Dependencies
pip install -r requirements.txt


### 4️⃣ Run the Dashboard
streamlit run app.py

The dashboard will open in your browser at:
http://localhost:8501


---

## 📁 Dataset

The dataset contains financial transaction records with the following features:

- TransactionID
- TransactionAmount
- LoginAttempts

These features are used to detect abnormal transaction behavior.

---

## 📈 Applications

This system can be used for:

- Banking fraud detection
- Financial transaction monitoring
- Cybersecurity threat detection
- Risk analysis systems
- Real-time fraud monitoring dashboards

---

## 👩‍💻 Author

**Tejavath Shalini**

Artificial Intelligence & Machine Learning Student

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

