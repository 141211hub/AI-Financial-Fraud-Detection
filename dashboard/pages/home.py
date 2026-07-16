import streamlit as st


def show():

    # ==================================================
    # HERO SECTION
    # ==================================================

    st.markdown("""
    <div class="hero">
        <h1>🏦 SecureBank AI</h1>
        <p>
            Enterprise Financial Fraud Detection Platform powered by
            Machine Learning, Explainable AI and Intelligent Investigation Reports.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ==================================================
    # KPI CARDS
    # ==================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">99.94%</div>
            <div class="kpi-title">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">91%</div>
            <div class="kpi-title">Recall</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">Real-Time</div>
            <div class="kpi-title">Detection</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">AI</div>
            <div class="kpi-title">Risk Engine</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ==================================================
    # PLATFORM FEATURES
    # ==================================================

    st.header("🚀 Platform Features")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class="feature-card">
        <h4>🔍 Single Prediction</h4>
        <p>Predict fraud for a single financial transaction instantly.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>📂 Batch Prediction</h4>
        <p>Upload CSV files and detect fraud in thousands of transactions.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>📊 Analytics Dashboard</h4>
        <p>Interactive charts, KPIs and fraud insights.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>📜 Prediction History</h4>
        <p>View every prediction stored in the database.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="feature-card">
        <h4>🧠 Explainable AI (SHAP)</h4>
        <p>Understand why the model predicted fraud.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>🤖 AI Investigation Assistant</h4>
        <p>Generate intelligent investigation summaries.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>📄 PDF Report Generation</h4>
        <p>Create professional fraud investigation reports.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>💾 SQLite Database</h4>
        <p>Securely store predictions and investigation history.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ==================================================
    # WORKFLOW
    # ==================================================

    st.header("🔄 Fraud Detection Workflow")

    st.code(
"""
Transaction
      │
      ▼
Machine Learning Model
      │
      ▼
Fraud Prediction
      │
      ▼
Explainable AI (SHAP)
      │
      ▼
AI Investigation
      │
      ▼
PDF Report
""",
language="text"
    )

    st.divider()

    # ==================================================
    # MODEL INFORMATION
    # ==================================================

    st.header("🧠 Model Information")

    left, right = st.columns(2)

    with left:
        st.write("**Algorithm:** XGBoost")
        st.write("**Backend:** FastAPI")
        st.write("**Frontend:** Streamlit")
        st.write("**Database:** SQLite")

    with right:
        st.write("**Accuracy:** 99.94%")
        st.write("**Recall:** 91%")
        st.write("**Explainability:** SHAP")
        st.write("**Reports:** AI Generated PDF")

    st.divider()

    # ==================================================
    # ABOUT PROJECT
    # ==================================================

    st.header("📌 About This Project")

    st.write("""
This enterprise-level application detects fraudulent financial
transactions using Machine Learning and Explainable AI.

### Key Capabilities

- ✅ Real-time Fraud Detection
- ✅ Batch Transaction Processing
- ✅ Interactive Analytics Dashboard
- ✅ Historical Prediction Tracking
- ✅ Explainable AI (SHAP)
- ✅ AI Investigation Assistant
- ✅ Automated PDF Report Generation
- ✅ SQLite Database Integration

### Technology Stack

- Python
- FastAPI
- Streamlit
- XGBoost
- SHAP
- Plotly
- SQLite
""")

    st.divider()

    # ==================================================
    # FOOTER
    # ==================================================

    st.markdown(
    """
    <div style="text-align:center;color:gray;padding:25px;">
        <h4>🏦 SecureBank AI</h4>

        Enterprise Financial Fraud Detection Platform<br><br>

        <b>Version 1.0</b><br><br>

        Built using Python • FastAPI • Streamlit • XGBoost • SHAP • SQLite
    </div>
    """,
    unsafe_allow_html=True
    )