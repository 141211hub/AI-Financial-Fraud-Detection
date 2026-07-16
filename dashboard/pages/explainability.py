import streamlit as st
import requests
import pandas as pd
import plotly.express as px

from config import API_URL


def show():

    # ==================================================
    # HERO
    # ==================================================

    st.markdown("""
    <div class="hero">
        <h1>🧠 Explainable AI</h1>
        <p>
        Understand why the AI classified this transaction as Fraud or Genuine
        using SHAP feature importance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if "last_prediction" not in st.session_state:

        st.warning("Please make a prediction first.")

        return

    prediction = st.session_state["last_prediction"]

    transaction = st.session_state["last_transaction"]

    st.subheader("Latest Prediction")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Prediction",
        prediction["prediction"]
    )

    c2.metric(
        "Probability",
        f"{prediction['fraud_probability']}%"
    )

    c3.metric(
        "Risk",
        prediction["risk_level"]
    )

    st.divider()

    with st.expander("Transaction Details"):

        st.json(transaction)

    st.divider()

    if st.button(
        "Generate SHAP Explanation",
        use_container_width=True
    ):

        with st.spinner("Generating explanation..."):

            response = requests.post(
                API_URL.replace("/predict", "/explain"),
                json=transaction
            )

            if response.status_code != 200:

                st.error("Unable to generate explanation.")

                return

            result = response.json()

            df = pd.DataFrame(
                result["top_features"]
            )

            st.success("Explanation Generated")

            st.subheader("Top Influential Features")

            chart = px.bar(

                df,

                x="impact",

                y="feature",

                orientation="h",

                title="SHAP Feature Importance"

            )

            st.plotly_chart(

                chart,

                use_container_width=True

            )

            st.divider()

            st.subheader("Feature Importance Table")

            st.dataframe(

                df,

                use_container_width=True

            )

            st.divider()

            positive = df[df["impact"] > 0]

            negative = df[df["impact"] < 0]

            st.subheader("AI Explanation")

            st.write(

                f"""
The model classified this transaction as **{prediction['prediction']}**.

The most influential features increasing fraud probability are:

{', '.join(positive['feature'].head(5).tolist())}

The features reducing fraud probability are:

{', '.join(negative['feature'].head(5).tolist())}
"""
            )