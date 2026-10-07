import sys
from pathlib import Path
import json

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def apply_history_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background: #07111f;
            color: #f8fafc;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .history-subtitle {
            color: #94a3b8;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }

        .section-label {
            color: #60a5fa;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-top: 1rem;
        }

        .empty-box {
            background: #0d1b2e;
            border: 1px solid #1e3a5f;
            border-radius: 14px;
            padding: 1.5rem;
            text-align: center;
        }

        .history-note {
            color: #94a3b8;
            font-size: 0.85rem;
        }

        .footer-note {
            color: #64748b;
            text-align: center;
            margin-top: 2rem;
            font-size: 0.8rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_history():
    apply_history_styles()

    if st.button(
        "← Back to Dashboard",
        key="history_back",
        width="content",
    ):
        st.session_state.page = "dashboard"
        st.rerun()

    st.markdown(
        '<div class="section-label">Analysis Records</div>',
        unsafe_allow_html=True,
    )

    st.title("Detection History")

    st.markdown(
        """
        <div class="history-subtitle">
        Review your previous network traffic analyses and detection results.
        </div>
        """,
        unsafe_allow_html=True,
    )

    user_id = st.session_state.get("user_id")

    if user_id is None:
        st.warning("Please sign in to view your detection history.")

        if st.button(
            "Go to Sign In",
            key="history_login",
        ):
            st.session_state.page = "login"
            st.rerun()

        return

    from src.database import get_user_analyses

    analyses = get_user_analyses(user_id)

    if not analyses:
        st.markdown(
            """
            <div class="empty-box">
                <h3>No analysis history yet</h3>
                <p class="history-note">
                    Upload a traffic CSV and run an intrusion detection
                    analysis to see your results here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Analyze Traffic",
            key="history_analyze",
        ):
            st.session_state.page = "analyze"
            st.rerun()

        st.markdown(
            """
            <div class="footer-note">
                SecureNet AI • Your analysis history is private to your account
            </div>
            """,
            unsafe_allow_html=True,
        )

        return

    st.markdown(
        '<div class="section-label">Your Analysis Summary</div>',
        unsafe_allow_html=True,
    )

    history_df = pd.DataFrame(analyses)

    total_analyses = len(history_df)
    total_records = int(history_df["total_records"].sum())
    total_attacks = int(history_df["attack_count"].sum())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Analyses",
            total_analyses,
        )

    with col2:
        st.metric(
            "Records Analyzed",
            f"{total_records:,}",
        )

    with col3:
        st.metric(
            "Attacks Detected",
            f"{total_attacks:,}",
        )

    st.markdown(
        '<div class="section-label">Analysis History</div>',
        unsafe_allow_html=True,
    )

    display_rows = []

    for analysis in analyses:
        category_counts = {}

        if analysis["category_counts"]:
            try:
                category_counts = json.loads(
                    analysis["category_counts"]
                )
            except (json.JSONDecodeError, TypeError):
                category_counts = {}

        display_rows.append(
            {
                "Date & Time": analysis["analyzed_at"],
                "File": analysis["filename"],
                "Records": f"{analysis['total_records']:,}",
                "Normal": f"{analysis['normal_count']:,}",
                "Attacks": f"{analysis['attack_count']:,}",
                "Intrusion Rate": (
                    f"{analysis['intrusion_rate']:.2f}%"
                ),
                "Attack Categories": ", ".join(
                    f"{category}: {count}"
                    for category, count in category_counts.items()
                    if count > 0
                )
                or "None",
            }
        )

    display_df = pd.DataFrame(display_rows)

    st.table(display_df)

    st.markdown(
        '<div class="section-label">Detection Breakdown</div>',
        unsafe_allow_html=True,
    )

    category_totals = {}

    for analysis in analyses:
        if analysis["category_counts"]:
            try:
                category_counts = json.loads(
                    analysis["category_counts"]
                )
            except (json.JSONDecodeError, TypeError):
                category_counts = {}

            for category, count in category_counts.items():
                category_totals[category] = (
                    category_totals.get(category, 0)
                    + int(count)
                )

    if category_totals:
        category_df = pd.DataFrame(
            {
                "Attack Category": list(
                    category_totals.keys()
                ),
                "Detected Records": list(
                    category_totals.values()
                ),
            }
        )

        category_df = category_df.set_index(
            "Attack Category"
        )

        st.bar_chart(category_df)

    st.markdown(
        """
        <div class="footer-note">
            SecureNet AI • Your analysis history is private to your account
        </div>
        """,
        unsafe_allow_html=True,
    )