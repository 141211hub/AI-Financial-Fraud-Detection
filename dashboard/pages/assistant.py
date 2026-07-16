import streamlit as st
import requests

from config import API_URL

# ==========================================
# API ENDPOINTS
# ==========================================

ASSISTANT_API = API_URL.replace("/predict", "/assistant")
REPORT_API = API_URL.replace("/predict", "/report")


def show():

    # ==========================================
    # HERO
    # ==========================================

    st.markdown("""
    <div class="hero">
        <h1>🤖 AI Fraud Investigation Assistant</h1>
        <p>
        Generate an AI-powered investigation report for the latest transaction.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # CHECK PREDICTION
    # ==========================================

    if "last_prediction" not in st.session_state:

        st.warning("⚠️ Please make a prediction first.")

        return

    prediction = st.session_state["last_prediction"]
    transaction = st.session_state["last_transaction"]

    # ==========================================
    # TRANSACTION SUMMARY
    # ==========================================

    st.subheader("📋 Transaction Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Prediction",
            prediction["prediction"]
        )

        st.metric(
            "Risk Level",
            prediction["risk_level"]
        )

    with col2:

        st.metric(
            "Fraud Probability",
            f"{prediction['fraud_probability']}%"
        )

        st.metric(
            "Amount",
            f"${transaction['Amount']:.2f}"
        )

    st.divider()

    with st.expander("📄 View Transaction Details"):

        st.json(transaction)

    st.divider()

    # ==========================================
    # GENERATE AI REPORT
    # ==========================================

    if st.button(
        "🤖 Generate AI Investigation Report",
        use_container_width=True
    ):

        payload = {

            "transaction": transaction,

            "prediction": prediction["prediction"],

            "fraud_probability": prediction["fraud_probability"],

            "risk_level": prediction["risk_level"]

        }

        with st.spinner("Generating AI Investigation Report..."):

            try:

                response = requests.post(
                    ASSISTANT_API,
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.session_state["ai_summary"] = result["summary"]

                    st.success("✅ AI Investigation Report Generated")

                else:

                    st.error(
                        f"Server Error ({response.status_code})"
                    )

                    st.code(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to the FastAPI backend."
                )

            except Exception as e:

                st.error(f"Unexpected Error:\n\n{e}")

    # ==========================================
    # SHOW AI REPORT
    # ==========================================

    if "ai_summary" in st.session_state:

        st.subheader("📝 AI Investigation Report")

        st.markdown(st.session_state["ai_summary"])

        st.divider()

        # ==========================================
        # PDF REPORT
        # ==========================================

        if st.button(
            "📄 Generate PDF Report",
            use_container_width=True
        ):

            pdf_payload = {

                "transaction": transaction,

                "prediction": prediction["prediction"],

                "fraud_probability": prediction["fraud_probability"],

                "risk_level": prediction["risk_level"],

                "summary": st.session_state["ai_summary"]

            }

            with st.spinner("Generating PDF Report..."):

                try:

                    response = requests.post(
                        REPORT_API,
                        json=pdf_payload,
                        timeout=60
                    )

                    if response.status_code == 200:

                        st.success("✅ PDF Generated Successfully")

                        st.download_button(
                            label="⬇️ Download Investigation Report",
                            data=response.content,
                            file_name="SecureBank_AI_Report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                    else:

                        st.error(
                            f"PDF Generation Failed ({response.status_code})"
                        )

                        st.code(response.text)

                except requests.exceptions.ConnectionError:

                    st.error(
                        "❌ Could not connect to the FastAPI backend."
                    )

                except Exception as e:

                    st.error(f"Unexpected Error:\n\n{e}")