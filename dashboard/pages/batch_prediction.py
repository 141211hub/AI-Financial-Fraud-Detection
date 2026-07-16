import streamlit as st
import pandas as pd
import requests

from config import API_URL


def show():

    # ==================================================
    # HERO
    # ==================================================

    st.markdown("""
    <div class="hero">
        <h1>📂 Batch Fraud Prediction</h1>
        <p>
            Upload a CSV file containing multiple transactions and let
            SecureBank AI analyze them automatically.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ==================================================
    # UPLOAD
    # ==================================================

    st.markdown("""
    <div class="input-card">
        <h3>📁 Upload Transaction Dataset</h3>
        <p>Supported format: CSV</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a CSV File",
        type=["csv"]
    )

    if uploaded_file is None:

        st.info("👆 Upload a CSV file to begin.")

        return

    try:

        df = pd.read_csv(uploaded_file)

    except Exception:

        st.error("Unable to read the uploaded CSV.")

        return

    st.success("✅ Dataset Uploaded Successfully")

    st.divider()

    # ==================================================
    # DATA PREVIEW
    # ==================================================

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.write(f"**Total Transactions:** {len(df)}")

    st.divider()

    # ==================================================
    # PREDICT BUTTON
    # ==================================================

    predict = st.button(
        "🚀 Predict All Transactions",
        use_container_width=True
    )

    if not predict:
        return

    predictions = []
    probabilities = []
    risks = []

    progress_bar = st.progress(0)

    status = st.empty()

    total = len(df)

    # ==================================================
    # PREDICTION LOOP
    # ==================================================

    for index, row in df.iterrows():

        status.write(
            f"Analyzing transaction {index+1} of {total}"
        )

        try:

            response = requests.post(
                API_URL,
                json=row.to_dict(),
                timeout=60
            )

            if response.status_code == 200:

                result = response.json()

                predictions.append(
                    result["prediction"]
                )

                probabilities.append(
                    result["fraud_probability"]
                )

                risks.append(
                    result["risk_level"]
                )

            else:

                predictions.append("Error")
                probabilities.append(None)
                risks.append(None)

        except Exception:

            predictions.append("Error")
            probabilities.append(None)
            risks.append(None)

        progress_bar.progress(
            (index + 1) / total
        )

    status.empty()

    # ==================================================
    # RESULTS
    # ==================================================

    df["Prediction"] = predictions
    df["Fraud Probability"] = probabilities
    df["Risk Level"] = risks

    fraud_count = len(
        df[df["Prediction"] == "Fraud"]
    )

    genuine_count = len(
        df[df["Prediction"] == "Genuine"]
    )

    high_risk = len(
        df[df["Risk Level"] == "High"]
    )

    st.success("✅ Batch Prediction Completed")

    st.divider()

    # ==================================================
    # SUMMARY
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Transactions",
        len(df)
    )

    c2.metric(
        "Fraud",
        fraud_count
    )

    c3.metric(
        "Genuine",
        genuine_count
    )

    c4.metric(
        "High Risk",
        high_risk
    )

    st.divider()

    # ==================================================
    # RESULT TABLE
    # ==================================================

    st.subheader("📊 Prediction Results")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ==================================================
    # DOWNLOAD
    # ==================================================

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction Results",
        data=csv,
        file_name="fraud_predictions.csv",
        mime="text/csv",
        use_container_width=True
    )