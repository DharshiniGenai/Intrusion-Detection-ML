import sys
from pathlib import Path
import hashlib

import pandas as pd
import streamlit as st


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


from predict import load_models
from preprocess import COLUMNS


# ============================================================
# REQUIRED FEATURES
# ============================================================

FEATURE_COLUMNS = [
    column
    for column in COLUMNS
    if column not in ["attack", "difficulty"]
]


# ============================================================
# INITIALIZE ANALYSIS STATE
# ============================================================

if "last_analysis" not in st.session_state:
    st.session_state.last_analysis = None

if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []

if "last_analysis_signature" not in st.session_state:
    st.session_state.last_analysis_signature = None


# ============================================================
# ANALYZE TRAFFIC
# ============================================================

def show_analyze():

    st.title("🔍 Analyze Network Traffic")

    st.write(
        "Upload network traffic data to detect normal traffic "
        "and potential intrusions using the trained IDS model."
    )

    st.divider()

    st.subheader("Upload Traffic Dataset")

    uploaded_file = st.file_uploader(
        "Upload a CSV file",
        type=["csv"],
        help=(
            "Upload network traffic records containing "
            "the required 41 network features."
        ),
    )

    if uploaded_file is None:

        st.info(
            "Upload a CSV file containing network traffic records "
            "to start intrusion detection."
        )

        return

    # ========================================================
    # 1. READ CSV
    # ========================================================

    try:

        file_bytes = uploaded_file.getvalue()

        traffic_data = pd.read_csv(
            uploaded_file
        )

    except Exception as error:

        st.error(
            f"Unable to read the CSV file: {error}"
        )

        return

    st.success(
        f"File uploaded successfully: {uploaded_file.name}"
    )

    st.write(
        f"**Records found:** {len(traffic_data):,}"
    )

    # ========================================================
    # 2. VALIDATE FEATURES
    # ========================================================

    missing_columns = [
        column
        for column in FEATURE_COLUMNS
        if column not in traffic_data.columns
    ]

    if missing_columns:

        st.error(
            "The uploaded CSV is missing required "
            "network traffic features."
        )

        st.write("### Missing columns")

        st.code(
            "\n".join(missing_columns)
        )

        st.info(
            "Please upload a CSV containing the "
            "41 NSL-KDD network traffic features."
        )

        return

    traffic_features = traffic_data[
        FEATURE_COLUMNS
    ].copy()

    st.success(
        f"CSV validation successful — all "
        f"{len(FEATURE_COLUMNS)} required features are available."
    )

    # ========================================================
    # 3. LOAD MODELS
    # ========================================================

    try:

        primary_model, attack_model = load_models()

    except Exception as error:

        st.error(
            f"Unable to load the trained models: {error}"
        )

        return

    # ========================================================
    # 4. PRIMARY PREDICTION
    # ========================================================

    try:

        primary_predictions = primary_model.predict(
            traffic_features
        )

        primary_probabilities = (
            primary_model.predict_proba(
                traffic_features
            )
        )

        primary_confidences = (
            primary_probabilities.max(axis=1) * 100
        )

    except Exception as error:

        st.error(
            f"Prediction failed: {error}"
        )

        return

    # ========================================================
    # 5. ATTACK TYPE PREDICTION
    # ========================================================

    attack_mask = (
        primary_predictions == "Attack"
    )

    attack_types = [
        "Normal"
    ] * len(traffic_features)

    attack_type_confidences = [
        None
    ] * len(traffic_features)

    if attack_mask.any():

        attack_rows = traffic_features.loc[
            attack_mask
        ]

        try:

            attack_predictions = attack_model.predict(
                attack_rows
            )

            attack_probabilities = (
                attack_model.predict_proba(
                    attack_rows
                )
            )

            attack_confidences = (
                attack_probabilities.max(axis=1)
                * 100
            )

            attack_positions = [
                index
                for index, is_attack
                in enumerate(attack_mask)
                if is_attack
            ]

            for position, attack_prediction, confidence in zip(
                attack_positions,
                attack_predictions,
                attack_confidences,
            ):

                attack_types[position] = (
                    attack_prediction
                )

                attack_type_confidences[position] = round(
                    float(confidence),
                    2,
                )

        except Exception as error:

            st.error(
                f"Attack-type prediction failed: {error}"
            )

            return

    # ========================================================
    # 6. CREATE RESULTS
    # ========================================================

    results = pd.DataFrame(
        {
            "Prediction": primary_predictions,
            "Attack Type": attack_types,
            "Model Confidence (%)": [
                round(float(confidence), 2)
                for confidence in primary_confidences
            ],
            "Attack Type Confidence (%)":
                attack_type_confidences,
        }
    )

    # ========================================================
    # 7. SUMMARY
    # ========================================================

    total_records = len(results)

    normal_count = int(
        (
            results["Prediction"]
            == "Normal"
        ).sum()
    )

    attack_count = int(
        (
            results["Prediction"]
            == "Attack"
        ).sum()
    )

    detection_rate = (
        attack_count
        / total_records
        * 100
        if total_records > 0
        else 0
    )

    # ========================================================
    # 8. ATTACK CATEGORY COUNTS
    # ========================================================

    attack_results = results[
        results["Prediction"] == "Attack"
    ]

    if not attack_results.empty:

        category_counts = (
            attack_results["Attack Type"]
            .value_counts()
            .to_dict()
        )

    else:

        category_counts = {}

    # ========================================================
    # 9. SAVE LATEST ANALYSIS
    # ========================================================

    file_signature = hashlib.md5(
        file_bytes
    ).hexdigest()

    analysis_data = {
        "filename": uploaded_file.name,
        "signature": file_signature,
        "records_analyzed": total_records,
        "normal_count": normal_count,
        "attack_count": attack_count,
        "intrusion_rate": round(
            detection_rate,
            2,
        ),
        "attack_categories": category_counts,
        "results": results.copy(),
    }

    st.session_state.last_analysis = analysis_data

    # ========================================================
    # 10. SAVE HISTORY ONLY FOR NEW FILE
    # ========================================================

    if (
        st.session_state.last_analysis_signature
        != file_signature
    ):

        history_entry = {
            "filename": uploaded_file.name,
            "records_analyzed": total_records,
            "normal_count": normal_count,
            "attack_count": attack_count,
            "intrusion_rate": round(
                detection_rate,
                2,
            ),
            "attack_categories": category_counts,
        }

        st.session_state.analysis_history.append(
            history_entry
        )

        st.session_state.last_analysis_signature = (
            file_signature
        )

    # ========================================================
    # 11. DETECTION SUMMARY
    # ========================================================

    st.divider()

    st.subheader("Detection Summary")

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:

        st.metric(
            "Records Analyzed",
            f"{total_records:,}",
        )

    with metric2:

        st.metric(
            "Normal Traffic",
            f"{normal_count:,}",
        )

    with metric3:

        st.metric(
            "Intrusions Detected",
            f"{attack_count:,}",
        )

    with metric4:

        st.metric(
            "Intrusion Rate",
            f"{detection_rate:.2f}%",
        )

    # ========================================================
    # 12. OVERALL RESULT
    # ========================================================

    st.divider()

    if attack_count > 0:

        st.error(
            f"🚨 Intrusion Detected — "
            f"{attack_count:,} suspicious record(s) found."
        )

    else:

        st.success(
            "🟢 No Intrusion Detected — "
            "All uploaded traffic was classified as Normal."
        )

    # ========================================================
    # 13. ATTACK CATEGORY SUMMARY
    # ========================================================

    if attack_count > 0:

        st.subheader(
            "Attack Category Summary"
        )

        category_series = pd.Series(
            category_counts
        )

        st.bar_chart(
            category_series,
            width="stretch",
        )

    # ========================================================
    # 14. DETAILED RESULTS
    # ========================================================

    st.divider()

    st.subheader(
        "Detailed Detection Results"
    )

    st.dataframe(
        results,
        width="stretch",
        hide_index=True,
    )

    # ========================================================
    # 15. DOWNLOAD RESULTS
    # ========================================================

    csv_results = results.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Detection Results",
        data=csv_results,
        file_name=(
            "intrusion_detection_results.csv"
        ),
        mime="text/csv",
        width="stretch",
    )