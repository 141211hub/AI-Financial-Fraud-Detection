import streamlit as st
from pathlib import Path

from config import (
    API_URL,
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE
)

from components.sidebar import show_sidebar
from components.header import show_header

from pages.home import show as show_home
from pages.single_prediction import show as show_single_prediction
from pages.batch_prediction import show as show_batch_prediction
from pages.history import show as show_history
from pages.analytics import show as show_analytics
from pages.explainability import show as show_explainability
from pages.assistant import show as show_assistant
from pages.history import show as show_history
from pathlib import Path



# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)

# ---------------- LOAD CSS ---------------- #

css_file = Path(__file__).parent / "style.css"

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- HEADER ---------------- #

show_header()

css_file = Path("assets/style.css")

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- SIDEBAR ---------------- #

page = show_sidebar()

# ---------------- ROUTING ---------------- #

if page == "Home":

    show_home()

elif page == "Single Prediction":

    show_single_prediction()

elif page == "Batch Prediction":

    show_batch_prediction()

elif page == "Analytics":

    show_analytics()

elif page == "History":

    show_history()

elif page == "Explainability":

    show_explainability()

elif page == "Assistant":

    show_assistant()