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
        <h1>📜 Prediction History</h1>
        <p>
        Review previously analyzed transactions and monitor fraud detection history.
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:

        response = requests.get(
            API_URL.replace("/predict", "/history"),
            timeout=30
        )

        if response.status_code != 200:

            st.error("Unable to load history.")
            return

        df = pd.DataFrame(response.json())

        if df.empty:

            st.info("No prediction history found.")
            return

        # ==================================================
        # FILTERS
        # ==================================================

        col1, col2 = st.columns(2)

        with col1:

            search = st.text_input(
                "🔍 Search Prediction"
            )

        with col2:

            risk = st.selectbox(
                "Risk Level",
                ["All"] + list(df["risk"].unique())
            )

        if search:

            df = df[
                df["prediction"]
                .str.contains(search, case=False)
            ]

        if risk != "All":

            df = df[
                df["risk"] == risk
            ]

        # ==================================================
        # KPI
        # ==================================================

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Transactions",
            len(df)
        )

        c2.metric(
            "Fraud",
            len(df[df["prediction"] == "Fraud"])
        )

        c3.metric(
            "High Risk",
            len(df[df["risk"] == "High"])
        )

        st.divider()

        # ==================================================
        # TABLE
        # ==================================================

        st.subheader("Prediction History")

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
            "📥 Download History",
            csv,
            "prediction_history.csv",
            "text/csv",
            use_container_width=True
        )

    except Exception as e:

        st.error(e)