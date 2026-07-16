import streamlit as st
import pandas as pd
import requests
import plotly.express as px

from config import API_URL


def show():

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""
    <div class="hero">
        <h1>📊 Enterprise Fraud Analytics Dashboard</h1>
        <p>
        Monitor fraud trends, investigate high-risk transactions and
        visualize prediction insights using SecureBank AI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:

        response = requests.get(
            API_URL.replace("/predict", "/history"),
            timeout=30
        )

        if response.status_code != 200:
            st.error("Unable to load analytics.")
            return

        df = pd.DataFrame(response.json())

        if df.empty:
            st.info("No prediction history available.")
            return

        # =====================================================
        # SIDEBAR FILTERS
        # =====================================================

        st.sidebar.header("Analytics Filters")

        prediction_filter = st.sidebar.multiselect(
            "Prediction",
            options=df["prediction"].unique(),
            default=df["prediction"].unique()
        )

        risk_filter = st.sidebar.multiselect(
            "Risk Level",
            options=df["risk"].unique(),
            default=df["risk"].unique()
        )

        df = df[
            (df["prediction"].isin(prediction_filter))
            &
            (df["risk"].isin(risk_filter))
        ]

        if df.empty:
            st.warning("No data available for selected filters.")
            return

        # =====================================================
        # KPI
        # =====================================================

        total = len(df)
        fraud = len(df[df["prediction"] == "Fraud"])
        genuine = len(df[df["prediction"] == "Genuine"])
        high = len(df[df["risk"] == "High"])
        avg_prob = df["probability"].mean()

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{total}</div>
                <div class="kpi-title">Transactions</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{fraud}</div>
                <div class="kpi-title">Fraud</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{genuine}</div>
                <div class="kpi-title">Genuine</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{high}</div>
                <div class="kpi-title">High Risk</div>
            </div>
            """, unsafe_allow_html=True)

        with col5:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{avg_prob:.1f}%</div>
                <div class="kpi-title">Avg Probability</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # =====================================================
        # EXECUTIVE SUMMARY
        # =====================================================

        st.success(f"""
### 📋 Executive Summary

- **Total Transactions:** {total}
- **Fraud Detected:** {fraud}
- **Genuine Transactions:** {genuine}
- **High Risk Transactions:** {high}
- **Average Fraud Probability:** {avg_prob:.2f}%
""")

        st.divider()

        # =====================================================
        # CHARTS
        # =====================================================

        left, right = st.columns(2)

        with left:

            pie = px.pie(
                df,
                names="prediction",
                hole=0.45,
                title="Fraud vs Genuine Transactions"
            )

            st.plotly_chart(
                pie,
                use_container_width=True
            )

        with right:

            risk_df = (
                df["risk"]
                .value_counts()
                .reset_index()
            )

            risk_df.columns = [
                "Risk Level",
                "Count"
            ]

            bar = px.bar(
                risk_df,
                x="Risk Level",
                y="Count",
                text="Count",
                title="Risk Distribution"
            )

            st.plotly_chart(
                bar,
                use_container_width=True
            )

        st.divider()

        # =====================================================
        # FRAUD PROBABILITY TREND
        # =====================================================

        line = px.line(
            df.reset_index(),
            x="index",
            y="probability",
            markers=True,
            title="Fraud Probability Trend"
        )

        st.plotly_chart(
            line,
            use_container_width=True
        )

        st.divider()

        # =====================================================
        # FRAUD DETECTION OVERVIEW
        # =====================================================

        trend = (
            df.groupby("prediction")
            .size()
            .reset_index(name="Count")
        )

        area = px.area(
            trend,
            x="prediction",
            y="Count",
            title="Fraud Detection Overview"
        )

        st.plotly_chart(
            area,
            use_container_width=True
        )

        st.divider()

        # =====================================================
        # AMOUNT DISTRIBUTION
        # =====================================================

        amount_chart = px.box(
            df,
            y="amount",
            color="prediction",
            title="Transaction Amount Distribution"
        )

        st.plotly_chart(
            amount_chart,
            use_container_width=True
        )

        st.divider()

        # =====================================================
        # SCATTER
        # =====================================================

        scatter = px.scatter(
            df,
            x="amount",
            y="probability",
            color="prediction",
            size="probability",
            hover_data=["risk"],
            title="Transaction Amount vs Fraud Probability"
        )

        st.plotly_chart(
            scatter,
            use_container_width=True
        )

        st.divider()

        # =====================================================
        # RISK SUMMARY
        # =====================================================

        st.subheader("🚨 Risk Summary")

        risk_counts = df["risk"].value_counts()

        for level, count in risk_counts.items():
            st.write(f"**{level} Risk:** {count} transactions")

        st.divider()

        # =====================================================
        # RISK TABLE
        # =====================================================

        st.subheader("📈 Risk Breakdown")

        risk_table = (
            df["risk"]
            .value_counts()
            .reset_index()
        )

        risk_table.columns = [
            "Risk Level",
            "Transactions"
        ]

        st.table(risk_table)

        st.divider()

        # =====================================================
        # HISTORY
        # =====================================================

        st.subheader("📜 Prediction History")

        st.dataframe(
            df,
            use_container_width=True,
            height=450
        )

        st.divider()

        # =====================================================
        # TOP FRAUD
        # =====================================================

        st.subheader("🚨 Top 10 Highest Risk Transactions")

        top = df.sort_values(
            by="probability",
            ascending=False
        ).head(10)

        st.dataframe(
            top,
            use_container_width=True
        )

        st.divider()

        # =====================================================
        # DOWNLOAD
        # =====================================================

        csv = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "📥 Download Analytics CSV",
            csv,
            "fraud_analytics.csv",
            "text/csv",
            use_container_width=True
        )

        st.markdown("""
        <div class="footer">
        SecureBank AI • Enterprise Fraud Analytics Dashboard
        </div>
        """, unsafe_allow_html=True)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Unable to connect to FastAPI backend."
        )

    except Exception as e:

        st.error(f"Unexpected Error:\n\n{e}")