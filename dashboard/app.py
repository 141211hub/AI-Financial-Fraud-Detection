import streamlit as st
from pathlib import Path

from config import (
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


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)

# ======================================================
# LOAD CSS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent
css_file = BASE_DIR / "assets" / "style.css"

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
else:
    st.warning(f"CSS file not found: {css_file}")

# ======================================================
# HEADER
# ======================================================

show_header()

# ======================================================
# SIDEBAR
# ======================================================

page = show_sidebar()

# ======================================================
# PAGE ROUTING
# ======================================================

if page == "Home":
    show_home()

elif page == "Single Prediction":
    show_single_prediction()

elif page == "Batch Prediction":
    show_batch_prediction()

elif page == "History":
    show_history()

elif page == "Analytics":
    show_analytics()

elif page == "Explainability":
    show_explainability()

elif page == "AI Assistant":
    show_assistant()

else:
    show_home()