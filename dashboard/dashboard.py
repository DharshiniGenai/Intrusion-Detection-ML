import json
import streamlit as st
from src.database import get_latest_analysis


def show_dashboard():

    user_id = st.session_state.get("user_id")

    if st.button(
        "← Back to SecureNet AI",
        key="dashboard_back",
        width="content",
    ):
        st.session_state.page = "landing"
        st.rerun()

    if user_id is not None:
        latest_analysis = get_latest_analysis(user_id)

        if latest_analysis is not None:
            st.session_state.analysis_total = latest_analysis["total_records"]
            st.session_state.analysis_normal = latest_analysis["normal_count"]
            st.session_state.analysis_attacks = latest_analysis["attack_count"]
            st.session_state.analysis_rate = latest_analysis["intrusion_rate"]

            

            category_counts = json.loads(
                latest_analysis["category_counts"]
            )

            if isinstance(category_counts, str):
                category_counts = json.loads(category_counts)

            st.session_state.analysis_categories = category_counts
    # ============================================================
    # PAGE STYLE
    # ============================================================

    st.markdown(
        """
        <style>

        .stApp {
            background:
                radial-gradient(
                    circle at 85% 10%,
                    rgba(56, 189, 248, 0.10),
                    transparent 28%
                ),
                radial-gradient(
                    circle at 10% 30%,
                    rgba(99, 102, 241, 0.08),
                    transparent 25%
                ),
                #07111f;
            color: #e5eef7;
        }

        .block-container {
            max-width: 1380px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            background: transparent !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #0b1728 0%,
                    #0a1423 100%
                );
            border-right: 1px solid #1d334b;
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 2rem;
        }

        .stButton > button {
            border-radius: 12px;
            min-height: 44px;
            border: 1px solid #263d56;
            background: #0e1d30;
            color: #dce8f3;
            font-weight: 600;
        }

        .stButton > button:hover {
            border-color: #38bdf8;
            background: #122940;
            color: #ffffff;
        }

        [data-testid="stMetric"] {
            background:
                linear-gradient(
                    145deg,
                    #0e1d30,
                    #0b1727
                );
            border: 1px solid #1d334b;
            border-radius: 18px;
            padding: 18px;
        }

        [data-testid="stMetricLabel"] {
            color: #8195aa !important;
        }

        [data-testid="stMetricValue"] {
            color: #f8fbff !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ============================================================
    # SIDEBAR
    # ============================================================

    with st.sidebar:

        st.markdown(
            "## 🛡️ SecureNet AI"
        )

        st.caption(
            "Machine Learning Intrusion Detection"
        )

        st.divider()

        st.caption(
            "SECURITY CENTER"
        )

        if st.button(
            "🏠  Dashboard",
            key="dashboard_nav",
            width="stretch",
        ):
            st.session_state.page = "dashboard"
            st.rerun()

        if st.button(
            "🔍  Analyze Traffic",
            key="analyze_nav",
            width="stretch",
        ):
            st.session_state.page = "analyze"
            st.rerun()
            
        if st.button(
            "📡  Live Detection",
            key="live_detection_nav",
            width="stretch",
        ):
            st.session_state.page = "live_detection"
            st.rerun()

        if st.button(
            "📊  Model Performance",
            key="performance_nav",
            width="stretch",
        ):
            st.session_state.page = "performance"
            st.rerun()

        if st.button(
            "📋  Detection History",
            key="history_nav",
            width="stretch",
        ):
            st.session_state.page = "history"
            st.rerun()

        st.divider()

        if st.button(
            "🚪  Logout",
            key="logout_nav",
            width="stretch",
        ):
            st.session_state.page = "landing"
            st.rerun()

    # ============================================================
    # HEADER
    # ============================================================

    st.caption(
        "🛡️ SECURENET AI SECURITY CENTER"
    )

    st.title(
        "Network Security Dashboard"
    )

    st.write(
        "Monitor network traffic, review machine-learning "
        "predictions, and identify suspicious activity."
    )

    st.success(
        "● IDS SYSTEM READY"
    )

    st.write("")

    # ============================================================
    # CURRENT ANALYSIS DATA
    # ============================================================

    total_records = st.session_state.get(
        "analysis_total",
        0,
    )

    normal_count = st.session_state.get(
        "analysis_normal",
        0,
    )

    attack_count = st.session_state.get(
        "analysis_attacks",
        0,
    )

    intrusion_rate = st.session_state.get(
        "analysis_rate",
        0.0,
    )

    attack_categories = st.session_state.get(
        "analysis_categories",
        {},
    )

    has_analysis = total_records > 0

    # ============================================================
    # METRICS
    # ============================================================

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "📡 Traffic Analyzed",
            f"{total_records:,}",
            "Current analysis"
            if has_analysis
            else "No analysis yet",
        )

    with metric2:
        st.metric(
            "🟢 Normal Traffic",
            f"{normal_count:,}",
            "Legitimate traffic",
        )

    with metric3:
        st.metric(
            "🚨 Attacks Detected",
            f"{attack_count:,}",
            "Suspicious records",
        )

    with metric4:
        st.metric(
            "⚡ Intrusion Rate",
            f"{intrusion_rate:.2f}%",
            "Current analysis",
        )

    st.write("")

    # ============================================================
    # CURRENT DETECTION
    # ============================================================

    result_col, attack_col = st.columns(
        [1.25, 1],
        gap="large",
    )

    with result_col:

        st.subheader(
            "Current Detection"
        )

        st.caption(
            "Latest machine-learning analysis result."
        )

        if has_analysis:

            if attack_count > 0:

                st.error(
                    f"🚨 Intrusion Detected\n\n"
                    f"{attack_count:,} suspicious network traffic "
                    f"record(s) were identified from the latest analysis."
                )

                st.warning(
                    f"⚠️ Detection complete — "
                    f"{intrusion_rate:.2f}% intrusion rate."
                )

            else:

                st.success(
                    "🟢 Normal Traffic\n\n"
                    "All uploaded network traffic records were "
                    "classified as normal."
                )

                st.info(
                    "✓ Detection complete — "
                    "no suspicious traffic found."
                )

        else:

            st.info(
                "🔎 Waiting for Traffic Analysis\n\n"
                "Upload a network traffic CSV from Analyze Traffic "
                "to generate detection results."
            )

            st.caption(
                "ℹ️ No traffic has been analyzed yet."
            )

    # ============================================================
    # ATTACK CATEGORY BREAKDOWN
    # ============================================================

    with attack_col:

        st.subheader(
            "Attack Category Breakdown"
        )

        st.caption(
            "Distribution of detected intrusion types."
        )

        if attack_categories:

            category_data = {
                "Attack Category": list(
                    attack_categories.keys()
                ),
                "Records": list(
                    attack_categories.values()
                ),
            }

            st.bar_chart(
                category_data,
                x="Attack Category",
                y="Records",
                height=250,
                width="stretch",
            )

        else:

            st.info(
                "🛡️ No intrusion categories yet.\n\n"
                "Upload traffic to begin detection."
            )

    st.write("")

    # ============================================================
    # ACTIVE ML MODELS
    # ============================================================

    st.subheader(
        "Active ML Models"
    )

    st.caption(
        "Models available in the IDS system."
    )

    model_col1, model_col2 = st.columns(2)

    models = [
        (
            "🌳 Decision Tree",
            "Primary IDS Model",
        ),
        (
            "🌲 Random Forest",
            "Comparison Model",
        ),
        (
            "📈 Logistic Regression",
            "Comparison Model",
        ),
        (
            "⚙️ Linear SVM",
            "Comparison Model",
        ),
    ]

    for index, (name, role) in enumerate(models):

        target_column = (
            model_col1
            if index % 2 == 0
            else model_col2
        )

        with target_column:

            with st.container(border=True):

                st.markdown(
                    f"**{name}**"
                )

                st.caption(
                    role
                )

    # ============================================================
    # QUICK ACTIONS
    # ============================================================

    st.write("")

    st.subheader(
        "Quick Actions"
    )

    st.caption(
        "Continue working with SecureNet AI."
    )

    action1, action2, action3 = st.columns(3)

    with action1:

        if st.button(
            "🔍 Analyze New Traffic",
            key="quick_analyze",
            width="stretch",
        ):
            st.session_state.page = "analyze"
            st.rerun()

    with action2:

        if st.button(
            "📊 View Model Performance",
            key="quick_performance",
            width="stretch",
        ):
            st.session_state.page = "performance"
            st.rerun()

    with action3:

        if st.button(
            "📋 View Detection History",
            key="quick_history",
            width="stretch",
        ):
            st.session_state.page = "history"
            st.rerun()

    # ============================================================
    # FOOTER
    # ============================================================

    st.divider()

    st.caption(
        "🛡️ SecureNet AI · Machine Learning Based "
        "Intrusion Detection System"
    )