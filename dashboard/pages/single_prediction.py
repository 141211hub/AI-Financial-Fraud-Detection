import streamlit as st
import requests

from config import API_URL


def show():

    # ==================================================
    # HERO
    # ==================================================

    st.markdown("""
    <div class="hero">
        <h1>🔍 Single Fraud Prediction</h1>
        <p>
            Analyze a single financial transaction using our AI-powered
            fraud detection model.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ==================================================
    # BASIC INFORMATION
    # ==================================================

    st.markdown("""
    <div class="input-card">
        <h3>💳 Transaction Information</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        time = st.number_input(
            "⏱ Time",
            value=0.0,
            format="%.6f"
        )

    with col2:
        amount = st.number_input(
            "💰 Amount",
            value=0.0,
            format="%.2f"
        )

    transaction = {}

    transaction["Time"] = time

    st.divider()

    # ==================================================
    # PRINCIPAL COMPONENTS
    # ==================================================

    st.subheader("🧮 Principal Components")

    left, right = st.columns(2)

    for i in range(1, 29):

        if i % 2 != 0:

            with left:

                transaction[f"V{i}"] = st.number_input(
                    f"V{i}",
                    value=0.0,
                    format="%.6f",
                    key=f"V{i}"
                )

        else:

            with right:

                transaction[f"V{i}"] = st.number_input(
                    f"V{i}",
                    value=0.0,
                    format="%.6f",
                    key=f"V{i}"
                )

    transaction["Amount"] = amount

    st.divider()

    # ==================================================
    # PREDICT BUTTON
    # ==================================================

    predict = st.button(
        "🚀 Predict Fraud",
        use_container_width=True
    )

    if predict:

        with st.spinner("Analyzing transaction..."):

            try:

                response = requests.post(
                    API_URL,
                    json=transaction,
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.session_state["last_transaction"] = transaction
                    st.session_state["last_prediction"] = result

                    prediction = result["prediction"]
                    probability = result["fraud_probability"]
                    risk = result["risk_level"]

                    st.success("Prediction Completed Successfully")

                    st.divider()

                    # ==========================================
                    # RESULT CARD
                    # ==========================================

                    color = "#DC2626" if prediction == "Fraud" else "#16A34A"

                    st.markdown(
                        f"""
                        <div style="
                            background:{color};
                            color:white;
                            padding:25px;
                            border-radius:18px;
                            text-align:center;
                            margin-bottom:20px;
                        ">
                            <h2>{prediction}</h2>
                            <h3>Fraud Probability: {probability:.2f}%</h3>
                            <h3>Risk Level: {risk}</h3>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # ==========================================
                    # KPI CARDS
                    # ==========================================

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "Prediction",
                        prediction
                    )

                    c2.metric(
                        "Probability",
                        f"{probability:.2f}%"
                    )

                    c3.metric(
                        "Risk",
                        risk
                    )

                    st.divider()

                    # ==========================================
                    # TRANSACTION DETAILS
                    # ==========================================

                    with st.expander("📋 View Transaction Details"):

                        st.json(transaction)

                    # ==========================================
                    # ALERT
                    # ==========================================

                    if prediction == "Fraud":

                        st.error(
                            "🚨 High-risk transaction detected. Manual investigation is recommended."
                        )

                    else:

                        st.success(
                            "✅ Transaction appears to be genuine."
                        )

                else:

                    st.error(
                        f"Server Error ({response.status_code})"
                    )

                    st.write(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Unable to connect to FastAPI backend.\n\n"
                    "Please make sure the backend server is running."
                )

            except Exception as e:

                st.error(f"Unexpected Error: {e}")