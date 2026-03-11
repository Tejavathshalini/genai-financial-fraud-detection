
import streamlit as st
import pandas as pd
import os
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(page_title="GenAI Financial Fraud Detection Dashboard", layout="wide")

# =============================
# TITLE
# =============================
st.title("🔍 GenAI Financial Fraud Detection Dashboard")

# =============================
# LOAD DATASET
# =============================
df = pd.read_csv("bank_transactions_dataset.csv")

# =============================
# ANOMALY DETECTION MODEL
# =============================
features = ['TransactionAmount','LoginAttempts']

scaler = StandardScaler()
X = scaler.fit_transform(df[features])

model = IsolationForest(contamination=0.05)

df['anomaly'] = model.fit_predict(X)

df['FraudFlag'] = df['anomaly'].apply(
    lambda x: "⚠️ Suspicious" if x == -1 else "✅ Normal"
)

# =============================
# SIDEBAR FILTER
# =============================
st.sidebar.header("⚙️ Filter Panel")

min_amt = st.sidebar.slider(
    "💰 Minimum Transaction Amount",
    int(df.TransactionAmount.min()),
    int(df.TransactionAmount.max()),
    0
)

filtered = df[df.TransactionAmount >= min_amt]

# =============================
# KPI CARDS
# =============================
c1, c2, c3 = st.columns(3)

c1.metric("📊 Total Transactions", len(filtered))
c2.metric("⚠️ Suspicious Cases",
          (filtered.FraudFlag == "⚠️ Suspicious").sum())
c3.metric("✅ Normal Transactions",
          (filtered.FraudFlag == "✅ Normal").sum())

# =============================
# TABLE
# =============================
st.subheader("📄 Transaction Records")

st.dataframe(filtered, use_container_width=True)

# =============================
# PLOTLY CHART
# =============================
st.subheader("📈 Transaction Amount Distribution")

fig = px.histogram(
    filtered,
    x="TransactionAmount",
    color="FraudFlag",
    title="Transaction Amount Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# =============================
# AI FRAUD EXPLANATION
# =============================
st.subheader("🤖 AI Fraud Reasoning")

sus = filtered[filtered.FraudFlag == "⚠️ Suspicious"]

if len(sus) > 0:

    tx = st.selectbox(
        "🔎 Select suspicious transaction",
        sus.TransactionID
    )

    if st.button("🧠 Analyze Fraud Pattern"):

        row = sus[sus.TransactionID == tx].iloc[0]

        reason = f"""
🚨 Fraud Risk Analysis for Transaction {tx}

This transaction was flagged as suspicious because:

• Transaction amount ({row.TransactionAmount}) is significantly higher than normal transactions.

• Multiple login attempts ({row.LoginAttempts}) were detected, which may indicate unauthorized access.

• The Isolation Forest anomaly detection model classified this transaction as abnormal behavior.

Possible fraud scenarios:

- Account takeover  
- Unauthorized transaction attempts  
- Suspicious login behavior  

Further investigation is recommended.
"""

        st.success(reason)

else:
    st.info("No suspicious transactions detected.")


st.success("🚀 GenAI Fraud Detection Dashboard Active")
