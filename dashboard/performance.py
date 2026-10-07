from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_PATH = PROJECT_ROOT / "results" / "model_comparison.csv"


def apply_performance_styles():
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

        .performance-subtitle {
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

        .metric-note {
            color: #94a3b8;
            font-size: 0.82rem;
        }

        .model-card {
            background: #0d1b2e;
            border: 1px solid #1e3a5f;
            border-radius: 14px;
            padding: 1rem 1.1rem;
            margin-bottom: 0.7rem;
        }

        .model-name {
            color: #f8fafc;
            font-size: 1rem;
            font-weight: 700;
        }

        .best-model {
            color: #4ade80;
            font-size: 0.78rem;
            font-weight: 700;
            margin-top: 0.25rem;
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


def show_performance():
    apply_performance_styles()

    if st.button(
        "← Back to Dashboard",
        key="performance_back",
        width="content",
    ):
        st.session_state.page = "dashboard"
        st.rerun()

    st.markdown(
        '<div class="section-label">Model Evaluation</div>',
        unsafe_allow_html=True,
    )

    st.title("Model Performance")

    st.markdown(
        """
        <div class="performance-subtitle">
        Compare the machine learning models used for intrusion detection
        and identify the best-performing model.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not RESULTS_PATH.exists():
        st.error(
            "Model comparison results were not found. "
            "Please run the model comparison script first."
        )
        return

    results = pd.read_csv(RESULTS_PATH)

    required_columns = {
        "Model",
        "Accuracy",
        "Macro F1",
        "Weighted F1",
        "Attack Recall",
    }

    missing_columns = required_columns - set(results.columns)

    if missing_columns:
        st.error(
            "The model comparison file is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )
        return

    results = results.copy()

    st.markdown(
        '<div class="section-label">Overall Comparison</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    best_accuracy = results.loc[
        results["Accuracy"].idxmax()
    ]

    best_f1 = results.loc[
        results["Macro F1"].idxmax()
    ]

    best_recall = results.loc[
        results["Attack Recall"].idxmax()
    ]

    with col1:
        st.metric(
            "Best Accuracy",
            f"{best_accuracy['Accuracy'] * 100:.2f}%",
        )

    with col2:
        st.metric(
            "Best Macro F1",
            f"{best_f1['Macro F1'] * 100:.2f}%",
        )

    with col3:
        st.metric(
            "Best Attack Recall",
            f"{best_recall['Attack Recall'] * 100:.2f}%",
        )

    with col4:
        st.metric(
            "Models Evaluated",
            len(results),
        )

    st.markdown(
        '<div class="section-label">Accuracy Comparison</div>',
        unsafe_allow_html=True,
    )

    accuracy_chart = results.set_index("Model")[["Accuracy"]].copy()
    accuracy_chart["Accuracy"] = accuracy_chart["Accuracy"] * 100

    st.bar_chart(accuracy_chart)

    st.caption(
        "Accuracy shows the percentage of test records classified correctly."
    )

    st.markdown(
        '<div class="section-label">F1 Score Comparison</div>',
        unsafe_allow_html=True,
    )

    f1_chart = results.set_index("Model")[["Macro F1"]].copy()
    f1_chart["Macro F1"] = f1_chart["Macro F1"] * 100

    st.bar_chart(f1_chart)

    st.caption(
        "Macro F1 gives equal importance to each classification class."
    )

    st.markdown(
        '<div class="section-label">Attack Detection</div>',
        unsafe_allow_html=True,
    )

    recall_chart = results.set_index("Model")[["Attack Recall"]].copy()
    recall_chart["Attack Recall"] = recall_chart["Attack Recall"] * 100

    st.bar_chart(recall_chart)

    st.caption(
        "Attack recall measures how many actual attacks were correctly detected."
    )

    st.markdown(
        '<div class="section-label">Detailed Results</div>',
        unsafe_allow_html=True,
    )

    display_results = results.copy()

    percentage_columns = [
        "Accuracy",
        "Macro F1",
        "Weighted F1",
        "Attack Recall",
    ]

    for column in percentage_columns:
        display_results[column] = (
            display_results[column] * 100
        ).round(2).astype(str) + "%"

    st.table(display_results)

    st.markdown(
        '<div class="section-label">Selected Model</div>',
        unsafe_allow_html=True,
    )

    best_model = results.loc[
        results["Accuracy"].idxmax()
    ]

    st.success(
        f"Decision Tree is the selected primary IDS model "
        f"with an accuracy of {best_model['Accuracy'] * 100:.2f}%."
    )

    st.markdown(
        """
        <div class="model-card">
            <div class="model-name">Why this model is selected</div>
            <div class="metric-note">
                The Decision Tree achieved the highest accuracy among the
                evaluated models and provides a strong balance between
                detecting normal traffic and intrusion traffic.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="footer-note">
            SecureNet AI • Machine Learning Intrusion Detection System
        </div>
        """,
        unsafe_allow_html=True,
    )