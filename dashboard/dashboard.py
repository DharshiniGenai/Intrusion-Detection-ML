import streamlit as st
import pandas as pd


def show_dashboard():

    # ============================================================
    # SIDEBAR NAVIGATION
    # ============================================================

    with st.sidebar:

        st.markdown("## 🛡️ SecureNet AI")

        st.caption("Machine Learning Intrusion Detection")

        st.divider()

        st.markdown("### Navigation")

        if st.button("🏠  Dashboard", width="stretch"):
            st.session_state.page = "dashboard"
            st.rerun()

        if st.button("🔍  Analyze Traffic", width="stretch"):
            st.session_state.page = "analyze"
            st.rerun()

        if st.button("📊  Model Performance", width="stretch"):
            st.session_state.page = "model_performance"
            st.rerun()

        if st.button("📋  Detection History", width="stretch"):
            st.session_state.page = "history"
            st.rerun()

        st.divider()

        if st.button("🚪  Logout", width="stretch"):
            st.session_state.page = "landing"
            st.rerun()

    # ============================================================
    # DASHBOARD HEADER
    # ============================================================

    title_col, status_col = st.columns([4, 1])

    with title_col:

        st.markdown(
            '<div class="dashboard-title">Security Dashboard</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="dashboard-subtitle">
                Monitor network traffic and machine learning based
                intrusion detection results.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with status_col:

        st.markdown(
            """
            <div class="status-badge">
                ● IDS SYSTEM READY
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ============================================================
    # METRICS
    # ============================================================

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">📡</div>
                <div class="metric-label">Traffic Analyzed</div>
                <div class="metric-value">0</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">🟢</div>
                <div class="metric-label">Normal Traffic</div>
                <div class="metric-value">0</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">🚨</div>
                <div class="metric-label">Attacks Detected</div>
                <div class="metric-value">0</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">🎯</div>
                <div class="metric-label">Detection Model</div>
                <div class="metric-value">DT</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ============================================================
    # NETWORK SECURITY OVERVIEW
    # ============================================================

    st.markdown("### Network Security Overview")

    st.caption(
        "Upload network traffic from the Analyze Traffic section "
        "to generate real detection results."
    )

    st.divider()

    # ============================================================
    # TRAFFIC CLASSIFICATION + ACTIVE MODELS
    # ============================================================

    chart_col, model_col = st.columns([1.5, 1])

    # ------------------------------------------------------------
    # TRAFFIC CLASSIFICATION
    # ------------------------------------------------------------

    with chart_col:

        st.markdown("### Traffic Classification")

        st.caption(
            "Detection results will appear here after traffic analysis."
        )

        empty_data = pd.DataFrame(
            {
                "Traffic": ["No analysis yet"],
                "Count": [0],
            }
        )

        st.bar_chart(
            empty_data.set_index("Traffic"),
            height=280,
            width="stretch",
        )

    # ------------------------------------------------------------
    # ACTIVE ML MODELS
    # ------------------------------------------------------------

    with model_col:

        st.markdown("### Active ML Models")

        st.caption(
            "Models available in the IDS system."
        )

        models = [
            ("Decision Tree", "Primary IDS Model"),
            ("Random Forest", "Comparison Model"),
            ("Logistic Regression", "Comparison Model"),
            ("Linear SVM", "Comparison Model"),
        ]

        for name, description in models:

            col1, col2 = st.columns([0.15, 0.85])

            with col1:
                st.markdown("🟢")

            with col2:
                st.markdown(f"**{name}**")
                st.caption(description)