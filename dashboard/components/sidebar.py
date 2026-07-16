import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/bank-building.png",
            width=70
        )

        st.title("SecureBank AI")

        st.markdown("---")

        page = st.radio(
    "Navigation",
    [
        "Home",
        "Single Prediction",
        "Batch Prediction",
        "Analytics",
        "History",
        "Explainability",
        "Assistant"
    ],
    format_func=lambda x: {
        "Home": "🏠 Home",
        "Single Prediction": "🔍 Single Prediction",
        "Batch Prediction": "📂 Batch Prediction",
        "Analytics": "📊 Analytics",
        "History": "📜 History",
        "Explainability": "🧠 Explainable AI",
        "Assistant": "🤖 AI Assistant"
    }[x]
)
        st.markdown("---")

        st.success("🟢 Backend Connected")

        return page