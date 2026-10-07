import sys
from pathlib import Path
import hashlib
from io import BytesIO
import json

import pandas as pd
import streamlit as st


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


from src.database import save_analysis
from predict import load_models
from preprocess import COLUMNS


# ============================================================
# PAGE CONFIGURATION
# ============================================================

def apply_analyze_styles():
    st.markdown(
        """
        <style>

        /* =====================================================
           PAGE
           ===================================================== */

        .stApp {
            background: #07111f;
            color: #edf5ff;
        }

        .block-container {
            max-width: 1320px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        footer {
            visibility: hidden;
        }

        #MainMenu {
            visibility: hidden;
        }


        /* =====================================================
           BUTTONS
           ===================================================== */

        .stButton > button {
            border-radius: 10px;
            min-height: 44px;
            font-weight: 600;
            border: 1px solid #29425e;
            background: #102137;
            color: #dcecff;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            border-color: #35b9ff;
            color: #ffffff;
            background: #142b44;
        }


        /* =====================================================
           FILE UPLOADER
           ===================================================== */

        [data-testid="stFileUploader"] {
            background: #0c1a2b;
            border: 1px dashed #31506e;
            border-radius: 14px;
            padding: 12px;
        }

        [data-testid="stFileUploaderDropzone"] {
            background: #0c1a2b;
            border: none;
        }


        /* =====================================================
           CONTAINERS
           ===================================================== */

        [data-testid="stVerticalBlockBorderWrapper"] {
            border-color: #203b57 !important;
            border-radius: 16px !important;
            background: #0b1929;
        }


        /* =====================================================
           METRICS
           ===================================================== */

        [data-testid="stMetric"] {
            background: #0c1a2b;
            border: 1px solid #203b57;
            border-radius: 14px;
            padding: 18px;
        }

        [data-testid="stMetricLabel"] {
            color: #829bb1;
        }

        [data-testid="stMetricValue"] {
            color: #f4f8fc;
        }


        /* =====================================================
           DATAFRAME
           ===================================================== */

        [data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }


        /* =====================================================
           HEADINGS
           ===================================================== */

        .analyze-kicker {
            color: #35b9ff;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .analyze-description {
            color: #8da4ba;
            font-size: 15px;
            line-height: 1.7;
        }

        .section-kicker {
            color: #35b9ff;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }


        /* =====================================================
           SMALL TEXT
           ===================================================== */

        .muted {
            color: #829bb1;
            font-size: 13px;
        }

        .success-text {
            color: #35e58a;
            font-weight: 700;
        }

        .danger-text {
            color: #ff6b7a;
            font-weight: 700;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SESSION STATE
# ============================================================

def initialize_session_state():

    if "last_analysis" not in st.session_state:
        st.session_state.last_analysis = None

    if "analysis_history" not in st.session_state:
        st.session_state.analysis_history = []

    if "last_analysis_signature" not in st.session_state:
        st.session_state.last_analysis_signature = None

    if "analysis_total" not in st.session_state:
        st.session_state.analysis_total = 0

    if "analysis_normal" not in st.session_state:
        st.session_state.analysis_normal = 0

    if "analysis_attacks" not in st.session_state:
        st.session_state.analysis_attacks = 0

    if "analysis_rate" not in st.session_state:
        st.session_state.analysis_rate = 0.0

    if "analysis_categories" not in st.session_state:
        st.session_state.analysis_categories = {}


# ============================================================
# FEATURE COLUMNS
# ============================================================

FEATURE_COLUMNS = [
    column
    for column in COLUMNS
    if column not in ["attack", "difficulty"]
]


# ============================================================
# RESULT COLOR / MESSAGE
# ============================================================

def show_detection_summary(
    total_records,
    normal_count,
    attack_count,
    intrusion_rate,
):

    st.write("")

    st.subheader("Detection Summary")

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)

    with metric_1:
        st.metric(
            "Records Analyzed",
            f"{total_records:,}",
        )

    with metric_2:
        st.metric(
            "Normal Traffic",
            f"{normal_count:,}",
        )

    with metric_3:
        st.metric(
            "Intrusions",
            f"{attack_count:,}",
        )

    with metric_4:
        st.metric(
            "Intrusion Rate",
            f"{intrusion_rate:.2f}%",
        )


# ============================================================
# MAIN PAGE
# ============================================================

def show_analyze():

    apply_analyze_styles()
    initialize_session_state()

    # ========================================================
    # BACK TO DASHBOARD
    # ========================================================

    if st.button(
        "← Back to Dashboard",
        key="analyze_back_dashboard",
        width="content",
    ):
        st.session_state.page = "dashboard"
        st.rerun()

    st.write("")


    # ========================================================
    # TOP STATUS
    # ========================================================

    top_left, top_right = st.columns(
        [3, 1],
        vertical_alignment="center",
    )

    with top_left:

        st.markdown(
            '<div class="analyze-kicker">Network Traffic Analysis</div>',
            unsafe_allow_html=True,
        )

        st.title("Analyze Your Network Traffic with AI")

        st.markdown(
            """
            <div class="analyze-description">
                Upload a network traffic dataset and let the trained
                machine-learning models identify normal traffic and
                potential intrusions.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with top_right:

        st.success(
            "● IDS SYSTEM READY"
        )


    st.write("")

    st.info(
        "🔒 Dataset-based intrusion detection   •   "
        "🤖 Decision Tree primary model   •   "
        "📊 Attack classification"
    )


    # ========================================================
    # UPLOAD SECTION
    # ========================================================

    st.write("")

    st.subheader("📡 Upload Traffic Dataset")

    st.caption(
        "Provide a CSV file containing the required network "
        "traffic features for intrusion detection."
    )

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"],
        accept_multiple_files=False,
        key="traffic_dataset",
        help="Maximum file size: 200 MB",
    )



    # ========================================================
    # ANALYSIS PIPELINE
    # ========================================================

    st.write("")

    st.subheader("🔍 Analysis Pipeline")

    pipeline_columns = st.columns(4)

    pipeline_steps = [
        (
            "01",
            "Upload Traffic",
            "Provide network traffic records.",
        ),
        (
            "02",
            "Preprocess Data",
            "Validate and prepare traffic features.",
        ),
        (
            "03",
            "Run AI Analysis",
            "Apply the trained Decision Tree model.",
        ),
        (
            "04",
            "View Detection",
            "Review normal and attack predictions.",
        ),
    ]

    for index, step in enumerate(pipeline_steps):

        number, title, description = step

        with pipeline_columns[index]:

            with st.container(border=True):

                st.markdown(
                    f"**STEP {number}**"
                )

                st.write(title)

                st.caption(description)


    # ========================================================
    # MODEL CAPABILITIES
    # ========================================================

    st.write("")

    st.subheader("🧠 Detection Capabilities")

    capability_columns = st.columns(3)

    capabilities = [
        (
            "Normal / Attack",
            "Primary model classifies each network record "
            "as normal traffic or intrusion.",
        ),
        (
            "Attack Categories",
            "Attack traffic is further classified into "
            "DoS, Probe, R2L, or U2R.",
        ),
        (
            "Confidence Score",
            "The system reports the model prediction score "
            "for each analyzed record.",
        ),
    ]

    for index, capability in enumerate(capabilities):

        title, description = capability

        with capability_columns[index]:

            with st.container(border=True):

                st.markdown(
                    f"### {title}"
                )

                st.caption(description)


    # ========================================================
    # WAIT FOR FILE
    # ========================================================

    if uploaded_file is None:

        st.write("")

        st.info(
            "Upload a CSV file above to start intrusion detection."
        )

        return


    # ========================================================
    # READ FILE
    # ========================================================

    try:

        file_bytes = uploaded_file.getvalue()

        if not file_bytes:

            st.error(
                "The uploaded file is empty."
            )

            return

        traffic_data = pd.read_csv(
            BytesIO(file_bytes)
        )

    except Exception as error:

        st.error(
            f"Unable to read the CSV file: {error}"
        )

        return


    # ========================================================
    # FILE INFORMATION
    # ========================================================

    st.write("")

    file_info_left, file_info_right = st.columns(2)

    with file_info_left:

        st.write(
            f"**File:** `{uploaded_file.name}`"
        )

    with file_info_right:

        st.write(
            f"**Records:** `{len(traffic_data):,}`"
        )


    # ========================================================
    # VALIDATE FEATURES
    # ========================================================

    missing_columns = [
        column
        for column in FEATURE_COLUMNS
        if column not in traffic_data.columns
    ]

    if missing_columns:

        st.error(
            "The uploaded CSV is missing required network "
            "traffic features."
        )

        st.write(
            "### Missing Features"
        )

        st.code(
            "\n".join(missing_columns)
        )

        st.info(
            f"The system expects {len(FEATURE_COLUMNS)} "
            "network traffic features."
        )

        return


    # ========================================================
    # SELECT MODEL INPUT
    # ========================================================

    model_input = traffic_data[
        FEATURE_COLUMNS
    ].copy()


    # ========================================================
    # LOAD MODELS
    # ========================================================

    try:

        primary_model, attack_model = load_models()

    except Exception as error:

        st.error(
            "Unable to load the trained machine-learning models."
        )

        st.exception(error)

        return


    # ========================================================
    # RUN PRIMARY MODEL
    # ========================================================

    with st.spinner(
        "Analyzing network traffic..."
    ):

        try:

            primary_predictions = primary_model.predict(
                model_input
            )

            primary_probabilities = (
                primary_model.predict_proba(
                    model_input
                )
            )

            primary_confidence = (
                primary_probabilities.max(axis=1) * 100
            )

        except Exception as error:

            st.error(
                "The primary intrusion detection model "
                "could not analyze this dataset."
            )

            st.exception(error)

            return


    # ========================================================
    # NORMALIZE PRIMARY PREDICTIONS
    # ========================================================

    primary_predictions = [
        str(prediction)
        for prediction in primary_predictions
    ]

    normalized_predictions = []

    for prediction in primary_predictions:

        prediction_lower = prediction.strip().lower()

        if prediction_lower in [
            "normal",
            "normal traffic",
            "0",
        ]:
            normalized_predictions.append(
                "Normal Traffic"
            )

        else:
            normalized_predictions.append(
                "Attack"
            )


    # ========================================================
    # ATTACK TYPE CLASSIFICATION
    # ========================================================

    attack_types = [
        "Normal"
        if prediction == "Normal Traffic"
        else "Attack"
        for prediction in normalized_predictions
    ]

    attack_type_confidence = [
        0.0
        for _ in range(len(model_input))
    ]

    attack_indices = [
        index
        for index, prediction in enumerate(
            normalized_predictions
        )
        if prediction == "Attack"
    ]


    if attack_indices:

        attack_input = model_input.iloc[
            attack_indices
        ]

        try:

            secondary_predictions = attack_model.predict(
                attack_input
            )

            secondary_probabilities = (
                attack_model.predict_proba(
                    attack_input
                )
            )

            secondary_confidence = (
                secondary_probabilities.max(axis=1) * 100
            )

            for position, row_index in enumerate(
                attack_indices
            ):

                attack_types[row_index] = str(
                    secondary_predictions[position]
                )

                attack_type_confidence[row_index] = float(
                    secondary_confidence[position]
                )

        except Exception as error:

            st.warning(
                "Primary intrusion detection completed, "
                "but attack-category classification could "
                "not be completed."
            )

            st.caption(
                str(error)
            )


    # ========================================================
    # BUILD RESULT DATAFRAME
    # ========================================================

    results = traffic_data.copy()

    results["Prediction"] = normalized_predictions

    results["Prediction Confidence"] = [
        round(float(value), 2)
        for value in primary_confidence
    ]

    results["Attack Type"] = attack_types

    results["Attack Type Confidence"] = [
        round(float(value), 2)
        for value in attack_type_confidence
    ]


    # ========================================================
    # SUMMARY COUNTS
    # ========================================================

    total_records = len(results)

    normal_count = sum(
        prediction == "Normal Traffic"
        for prediction in normalized_predictions
    )

    attack_count = sum(
        prediction == "Attack"
        for prediction in normalized_predictions
    )

    intrusion_rate = (
        (attack_count / total_records) * 100
        if total_records > 0
        else 0.0
    )


    # ========================================================
    # ATTACK CATEGORY COUNTS
    # ========================================================

    category_counts = {}

    for attack_type in attack_types:

        if attack_type != "Normal":

            category_counts[attack_type] = (
                category_counts.get(
                    attack_type,
                    0,
                )
                + 1
            )


    # ========================================================
    # FILE SIGNATURE
    # ========================================================

    file_signature = hashlib.sha256(
        file_bytes
    ).hexdigest()


    # ========================================================
    # SAVE ANALYSIS ONLY ONCE
    # ========================================================

    is_new_analysis = (
        st.session_state.last_analysis_signature
        != file_signature
    )


    if is_new_analysis:

        st.session_state.analysis_total = (
            total_records
        )

        st.session_state.analysis_normal = (
            normal_count
        )

        st.session_state.analysis_attacks = (
            attack_count
        )

        st.session_state.analysis_rate = (
            intrusion_rate
        )

        st.session_state.analysis_categories = (
            category_counts
        )

        st.session_state.last_analysis = {
            "filename": uploaded_file.name,
            "total_records": total_records,
            "normal_count": normal_count,
            "attack_count": attack_count,
            "intrusion_rate": intrusion_rate,
            "category_counts": category_counts,
        }

        # ----------------------------------------------------
        # USER-SPECIFIC DATABASE HISTORY
        # ----------------------------------------------------

        user_id = st.session_state.get(
            "user_id"
        )

        if user_id is not None:

            try:

                save_analysis(
                    user_id=user_id,
                    filename=uploaded_file.name,
                    total_records=total_records,
                    normal_count=normal_count,
                    attack_count=attack_count,
                    intrusion_rate=intrusion_rate,
                    category_counts=json.dumps(
                        category_counts
                    ),
                )

            except TypeError:

                # Compatibility fallback if the existing
                # database function accepts positional values.
                try:

                    save_analysis(
                        user_id,
                        uploaded_file.name,
                        total_records,
                        normal_count,
                        attack_count,
                        intrusion_rate,
                        json.dumps(
                            category_counts
                        ),
                    )

                except Exception as error:

                    st.warning(
                        "Analysis completed, but the result "
                        "could not be saved to history."
                    )

                    st.caption(
                        str(error)
                    )

            except Exception as error:

                st.warning(
                    "Analysis completed, but the result "
                    "could not be saved to history."
                )

                st.caption(
                    str(error)
                )


        # ----------------------------------------------------
        # SESSION HISTORY
        # ----------------------------------------------------

        history_record = {
            "filename": uploaded_file.name,
            "total_records": total_records,
            "normal_count": normal_count,
            "attack_count": attack_count,
            "intrusion_rate": intrusion_rate,
            "category_counts": category_counts,
        }

        st.session_state.analysis_history.append(
            history_record
        )

        st.session_state.last_analysis_signature = (
            file_signature
        )


    # ========================================================
    # DETECTION COMPLETE
    # ========================================================

    st.write("")

    if attack_count > 0:

        st.warning(
            f"⚠️ Analysis Complete — "
            f"{attack_count:,} potentially malicious "
            f"records detected."
        )

    else:

        st.success(
            "✓ Analysis Complete — "
            "No attack records were detected."
        )


    # ========================================================
    # SUMMARY
    # ========================================================

    show_detection_summary(
        total_records=total_records,
        normal_count=normal_count,
        attack_count=attack_count,
        intrusion_rate=intrusion_rate,
    )


    # ========================================================
    # DETECTION RESULT
    # ========================================================

    st.write("")

    st.subheader("🎯 Detection Result")

    result_left, result_right = st.columns(
        [2, 1],
        vertical_alignment="center",
    )

    with result_left:

        if attack_count > 0:

            st.error(
                f"Attack Detected\n\n"
                f"{attack_count:,} of "
                f"{total_records:,} records were classified "
                f"as potentially malicious."
            )

        else:

            st.success(
                "Normal Traffic\n\n"
                "The analyzed dataset contains no "
                "records classified as attacks."
            )

    with result_right:

        st.metric(
            "Intrusion Rate",
            f"{intrusion_rate:.2f}%",
        )


    # ========================================================
    # ATTACK CATEGORY BREAKDOWN
    # ========================================================

    if category_counts:

        st.write("")

        st.subheader(
            "📊 Attack Category Breakdown"
        )

        category_dataframe = pd.DataFrame(
            {
                "Attack Type": list(
                    category_counts.keys()
                ),
                "Records": list(
                    category_counts.values()
                ),
            }
        )

        category_dataframe = (
            category_dataframe.sort_values(
                "Records",
                ascending=False,
            )
        )

        st.bar_chart(
            category_dataframe.set_index(
                "Attack Type"
            )
        )


    # ========================================================
    # RESULTS TABLE
    # ========================================================

    st.write("")

    st.subheader(
        "📋 Traffic Detection Results"
    )

    st.caption(
        f"Showing {len(results):,} analyzed records."
    )

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True,
    )


    # ========================================================
    # DOWNLOAD RESULTS
    # ========================================================

    st.write("")

    output_csv = results.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Detection Results",
        data=output_csv,
        file_name="securenet_detection_results.csv",
        mime="text/csv",
        use_container_width=False,
    )


    # ========================================================
    # MODEL INFORMATION
    # ========================================================

    st.write("")

    with st.container(border=True):

        st.subheader(
            "🤖 Model Information"
        )

        model_col_1, model_col_2, model_col_3 = st.columns(
            3
        )

        with model_col_1:

            st.write(
                "**Primary Model**"
            )

            st.caption(
                "Decision Tree"
            )

        with model_col_2:

            st.write(
                "**Secondary Model**"
            )

            st.caption(
                "Decision Tree Attack Classifier"
            )

        with model_col_3:

            st.write(
                "**Analysis Type**"
            )

            st.caption(
                "Dataset-based intrusion detection"
            )


    # ========================================================
    # SUPPORTED ATTACK TYPES
    # ========================================================

    st.write("")

    st.subheader(
        "🛡️ Detection Coverage"
    )

    coverage_columns = st.columns(5)

    coverage = [
        (
            "🟢",
            "Normal",
            "Legitimate traffic",
        ),
        (
            "🔴",
            "DoS",
            "Denial-of-Service",
        ),
        (
            "🟠",
            "Probe",
            "Network reconnaissance",
        ),
        (
            "🟣",
            "R2L",
            "Remote-to-local",
        ),
        (
            "⚠️",
            "U2R",
            "User-to-root",
        ),
    ]

    for index, item in enumerate(coverage):

        icon, name, description = item

        with coverage_columns[index]:

            with st.container(border=True):

                st.markdown(
                    f"### {icon} {name}"
                )

                st.caption(
                    description
                )


    # ========================================================
    # FOOTER NOTE
    # ========================================================

    st.write("")
    st.divider()

    st.caption(
        "SecureNet AI • Machine-learning-based "
        "network intrusion detection • "
        "Dataset-based analysis"
    )