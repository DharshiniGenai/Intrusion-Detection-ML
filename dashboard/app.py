import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SecureNet AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "landing"

# ============================================================
# DATABASE INITIALIZATION
# ============================================================

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import initialize_database

initialize_database()

# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =========================================================
       SECURENET AI — DARK CYBERSECURITY THEME
       ========================================================= */

    html {
        scroll-behavior: smooth;
    }

    .stApp {
        background: #071525;
        color: #f4f8fc;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    header,
    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* =========================================================
       GENERAL TEXT
       ========================================================= */

    p {
        color: #b8c9d9;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #f4f8fc;
    }

    label {
        color: #d7e3ef !important;
    }

    /* =========================================================
       NAVIGATION
       ========================================================= */

    .nav-brand {
        color: #f4f8fc;
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .nav-icon {
        margin-right: 5px;
    }

    .nav-anchor {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 46px;
        padding: 0 12px;
        border-radius: 10px;
        border: 1px solid transparent;
        color: #dce8f3 !important;
        background: transparent;
        text-decoration: none !important;
        font-size: 14px;
        font-weight: 600;
        white-space: nowrap;
        transition: all 0.2s ease;
    }

    .nav-anchor:hover {
        background: #10243a;
        border-color: #294966;
        color: #ffffff !important;
        text-decoration: none !important;
    }

    /* =========================================================
       HERO
       ========================================================= */

    .hero-badge {
        display: inline-block;
        padding: 9px 16px;
        border-radius: 999px;
        background: #102b43;
        border: 1px solid #214968;
        color: #48c7ff;
        font-size: 13px;
        font-weight: 700;
    }

    .hero-title {
        color: #f4f8fc;
        font-size: 64px;
        line-height: 1.03;
        font-weight: 800;
        letter-spacing: -2px;
        margin-top: 20px;
    }

    .hero-accent {
        color: #35b9ff;
    }

    .hero-description {
        color: #a9bdd0;
        font-size: 18px;
        line-height: 1.7;
        max-width: 680px;
        margin-top: 22px;
    }

    .hero-feature {
        color: #c5d5e3;
        font-size: 15px;
        margin-top: 13px;
    }

    .hero-feature-mark {
        color: #35e58a;
        font-weight: 700;
        margin-right: 8px;
    }

    /* =========================================================
       BUTTONS
       ========================================================= */

    .stButton > button {
        min-height: 46px;
        border-radius: 10px;
        border: 1px solid #294966;
        background: #10243a;
        color: #f4f8fc;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #163653;
        border-color: #35b9ff;
        color: #ffffff;
    }

    /* =========================================================
       HERO ANALYSIS CARD
       ========================================================= */

    .analysis-header {
        color: #f4f8fc;
        font-size: 20px;
        font-weight: 750;
    }

    .analysis-subtitle {
        color: #829bb1;
        font-size: 13px;
        margin-top: 5px;
    }

    .ready-badge {
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(53, 229, 138, 0.10);
        border: 1px solid rgba(53, 229, 138, 0.30);
        color: #35e58a;
        font-size: 11px;
        font-weight: 700;
    }

    .analysis-caption {
        color: #8ca5ba;
        font-size: 12px;
    }

    .analysis-number {
        color: #ffffff;
        font-size: 36px;
        font-weight: 800;
        margin-top: 4px;
    }

    .result-title {
        color: #f4f8fc;
        font-size: 13px;
        font-weight: 600;
    }

    .result-normal {
        color: #35e58a;
        font-size: 19px;
        font-weight: 800;
        margin-top: 4px;
    }

    .result-caption {
        color: #8ca5ba;
        font-size: 11px;
    }

    .result-confidence {
        color: #35e58a;
        font-size: 22px;
        font-weight: 800;
        margin-top: 3px;
    }

    /* =========================================================
       HERO LINK BUTTONS
       ========================================================= */

    .hero-link {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 46px;
        padding: 0 16px;
        border-radius: 10px;
        border: 1px solid #294966;
        background: #10243a;
        color: #f4f8fc !important;
        text-decoration: none !important;
        font-size: 14px;
        font-weight: 650;
        transition: all 0.2s ease;
    }

    .hero-link:hover {
        background: #163653;
        border-color: #35b9ff;
        color: #ffffff !important;
        text-decoration: none !important;
    }

    .hero-link-primary {
        background: #0e4d70;
        border-color: #35b9ff;
        color: #ffffff !important;
    }

    .hero-link-primary:hover {
        background: #12658e;
        border-color: #63d0ff;
    }

    /* =========================================================
       SECTION SPACING
       ========================================================= */

    .section-gap {
        height: 82px;
    }

    .section-heading-wrapper {
        text-align: center;
        margin-bottom: 42px;
    }

    .section-kicker {
        color: #35b9ff;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        text-align: center;
    }

    .section-title {
        color: #f4f8fc;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        text-align: center;
        margin-top: 8px;
    }

    .section-description {
        color: #9db2c5;
        font-size: 16px;
        line-height: 1.7;
        max-width: 760px;
        margin: 12px auto 0 auto;
        text-align: center;
    }

    /* =========================================================
       FEATURE CARDS
       ========================================================= */

    .card-icon {
        font-size: 28px;
        margin-bottom: 14px;
    }

    .card-title {
        color: #f4f8fc;
        font-size: 18px;
        font-weight: 750;
    }

    .card-description {
        color: #91a7ba;
        font-size: 14px;
        line-height: 1.6;
        margin-top: 8px;
    }

    .feature-link {
        color: #35b9ff !important;
        text-decoration: none !important;
        font-weight: 750;
    }

    .feature-link:hover {
        color: #70d4ff !important;
        text-decoration: underline !important;
    }

    /* =========================================================
       HOW IT WORKS
       ========================================================= */

    .step-number {
        color: #35b9ff;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    .step-title {
        color: #f4f8fc;
        font-size: 19px;
        font-weight: 750;
        margin-top: 8px;
    }

    .step-description {
        color: #91a7ba;
        font-size: 14px;
        line-height: 1.6;
        margin-top: 7px;
    }

    /* =========================================================
       THREAT CATEGORY CARDS
       ========================================================= */

    .threat-icon {
        font-size: 28px;
    }

    .threat-name {
        color: #f4f8fc;
        font-size: 18px;
        font-weight: 750;
        margin-top: 10px;
    }

    .threat-description {
        color: #91a7ba;
        font-size: 13px;
        margin-top: 5px;
    }

    /* =========================================================
       PERFORMANCE / HISTORY
       ========================================================= */

    .resource-card {
        background: #0d1d31;
        border: 1px solid #213c58;
        border-radius: 16px;
        padding: 24px;
        height: 100%;
    }

    .resource-icon {
        font-size: 30px;
        margin-bottom: 12px;
    }

    .resource-title {
        color: #f4f8fc;
        font-size: 20px;
        font-weight: 750;
    }

    .resource-text {
        color: #91a7ba;
        font-size: 14px;
        line-height: 1.65;
        margin-top: 8px;
    }

    .resource-link {
        display: inline-block;
        margin-top: 15px;
        color: #35b9ff !important;
        font-size: 13px;
        font-weight: 700;
        text-decoration: none !important;
    }

    .resource-link:hover {
        color: #70d4ff !important;
        text-decoration: underline !important;
    }

    /* =========================================================
       ABOUT
       ========================================================= */

    .about-kicker {
        color: #35b9ff;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        text-align: center;
    }

    .about-title {
        color: #f4f8fc;
        font-size: 30px;
        font-weight: 800;
        text-align: center;
        margin-top: 8px;
    }

    .about-text {
        color: #9db2c5;
        font-size: 15px;
        line-height: 1.75;
    }

    .about-note {
        color: #7f9ab2;
        font-size: 14px;
        line-height: 1.7;
        padding: 14px;
        border-left: 3px solid #35b9ff;
        background: #0a1c2e;
        border-radius: 8px;
    }

    /* =========================================================
       CTA
       ========================================================= */

    .cta-title {
        color: #ffffff;
        font-size: 40px;
        font-weight: 800;
        text-align: center;
        line-height: 1.15;
    }

    .cta-description {
        color: #a9bdd0;
        font-size: 16px;
        line-height: 1.6;
        margin: 12px auto 0 auto;
        max-width: 700px;
        text-align: center;
    }

    /* =========================================================
       FOOTER
       ========================================================= */

    .footer-title {
        color: #f4f8fc;
        font-size: 18px;
        font-weight: 800;
    }

    .footer-text {
        color: #71889d;
        font-size: 13px;
        line-height: 1.6;
        margin-top: 10px;
    }

    .footer-heading {
        color: #dce8f3;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .footer-link {
        display: block;
        color: #8098ac !important;
        font-size: 13px;
        margin-top: 7px;
        text-decoration: none !important;
    }

    .footer-link:hover {
        color: #35b9ff !important;
        text-decoration: none !important;
    }

    .copyright {
        color: #60778c;
        font-size: 12px;
        text-align: center;
        margin-top: 30px;
        padding-bottom: 15px;
    }

    hr {
        border-color: #20384f !important;
    }

    /* =========================================================
       ANCHORS
       ========================================================= */

    #platform-features,
    #how-it-works,
    #detection-coverage,
    #model-performance-section,
    #detection-history-section,
    #about-securenet {
        scroll-margin-top: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ROUTING
# ============================================================

if st.session_state.page == "login":
    from login import show_login

    show_login()
    st.stop()
    
if st.session_state.page == "forgot_password":
    from forgot_password import show_forgot_password

    show_forgot_password()
    st.stop()

if st.session_state.page == "register":
    from register import show_register

    show_register()
    st.stop()


if st.session_state.page == "dashboard":
    from dashboard import show_dashboard

    show_dashboard()
    st.stop()


if st.session_state.page == "analyze":
    from analyze import show_analyze

    show_analyze()
    st.stop()

if st.session_state.page == "live_detection":
    from live_detection import show_live_detection

    show_live_detection()
    st.stop()

if st.session_state.page == "performance":
    from performance import show_performance

    show_performance()
    st.stop()


if st.session_state.page == "history":
    from history import show_history

    show_history()
    st.stop()


# ============================================================
# NAVBAR
# ============================================================

nav_logo, nav_features, nav_how, nav_detection, nav_about, nav_signin, nav_start = st.columns(
    [2.8, 0.9, 1.1, 0.95, 0.75, 0.8, 1.0],
    vertical_alignment="center",
)


with nav_logo:

    st.markdown(
        """
        <div class="nav-brand">
            <span class="nav-icon">🛡️</span>
            SecureNet AI
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------- SECTION NAVIGATION --------------------

with nav_features:

    st.markdown(
        '<a class="nav-anchor" href="#platform-features">Features</a>',
        unsafe_allow_html=True,
    )


with nav_how:

    st.markdown(
        '<a class="nav-anchor" href="#how-it-works">How It Works</a>',
        unsafe_allow_html=True,
    )


with nav_detection:

    st.markdown(
        '<a class="nav-anchor" href="#detection-coverage">Detection</a>',
        unsafe_allow_html=True,
    )


with nav_about:

    st.markdown(
        '<a class="nav-anchor" href="#about-securenet">About</a>',
        unsafe_allow_html=True,
    )


# -------------------- ACTUAL PAGE NAVIGATION --------------------

with nav_signin:

    if st.button(
        "Sign In",
        key="nav_signin",
        width="stretch",
    ):
        st.session_state.page = "login"
        st.rerun()


with nav_start:

    if st.button(
        "Get Started",
        key="nav_get_started",
        width="stretch",
    ):
        st.session_state.page = "register"
        st.rerun()


st.divider()


# ============================================================
# HERO
# ============================================================

hero_left, hero_right = st.columns(
    [1.05, 0.95],
    gap="large",
)


with hero_left:

    st.markdown(
        '<div class="hero-badge">🛡️ AI-Powered Cybersecurity</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-title">
            Protect Every Network.<br>
            <span class="hero-accent">
                Detect Threats Earlier.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-description">
            Detect suspicious network activity with
            AI-powered machine learning. Analyze traffic,
            identify attacks, and gain actionable security
            insights from network data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    button_one, button_two = st.columns([1, 1])

    # ========================================================
    # START DETECTION → REGISTER PAGE
    # ========================================================

    with button_one:

        if st.button(
            "Start Detection  →",
            key="hero_start",
            width="stretch",
        ):
            st.session_state.page = "register"
            st.rerun()

    # ========================================================
    # EXPLORE PLATFORM → SCROLL
    # ========================================================

    with button_two:

        st.markdown(
            '<a class="hero-link" href="#platform-features">'
            'Explore Platform'
            '</a>',
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="hero-feature">
            <span class="hero-feature-mark">✓</span>
            AI-powered intrusion detection
        </div>

        <div class="hero-feature">
            <span class="hero-feature-mark">✓</span>
            Machine learning traffic analysis
        </div>

        <div class="hero-feature">
            <span class="hero-feature-mark">✓</span>
            Threat identification and reporting
        </div>

        <div class="hero-feature">
            <span class="hero-feature-mark">✓</span>
            Detection history
        </div>
        """,
        unsafe_allow_html=True,
    )


with hero_right:

    with st.container(border=True):

        header_left, header_right = st.columns(
            [4, 1],
            vertical_alignment="center",
        )

        with header_left:

            st.markdown(
                '<div class="analysis-header">🛡️ Network Traffic Analysis</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="analysis-subtitle">'
                'Machine learning intrusion detection'
                '</div>',
                unsafe_allow_html=True,
            )

        with header_right:

            st.markdown(
                '<div class="ready-badge">SYSTEM READY</div>',
                unsafe_allow_html=True,
            )

        with st.container(border=True):

            st.markdown(
                '<div class="analysis-caption">'
                'Training Traffic Records'
                '</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="analysis-number">125,973</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="analysis-caption">'
                'NSL-KDD training records'
                '</div>',
                unsafe_allow_html=True,
            )

            chart_data = {
                "Traffic": [
                    32,
                    55,
                    43,
                    72,
                    58,
                    86,
                    67,
                    94,
                    78,
                    88,
                    62,
                    76,
                ]
            }

            st.bar_chart(
                chart_data,
                height=150,
                width="stretch",
            )

        result_left, result_right = st.columns(
            [2, 1],
            vertical_alignment="center",
        )

        with result_left:

            st.markdown(
                '<div class="result-title">Example Detection</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="result-normal">Normal Traffic</div>',
                unsafe_allow_html=True,
            )

        with result_right:

            st.markdown(
                '<div class="result-caption">Model confidence</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="result-confidence">94.2%</div>',
                unsafe_allow_html=True,
            )

        st.success(
            "✓ Analysis Complete — Traffic classification ready"
        )


# ============================================================
# PROJECT STATISTICS
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

stat_1, stat_2, stat_3, stat_4 = st.columns(4)

with stat_1:

    st.metric(
        "Training Records",
        "125,973",
    )

with stat_2:

    st.metric(
        "Test Records",
        "22,544",
    )

with stat_3:

    st.metric(
        "Traffic Categories",
        "5",
    )

with stat_4:

    st.metric(
        "ML Algorithms",
        "4",
    )


# ============================================================
# PLATFORM FEATURES
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div id="platform-features"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading-wrapper">'
    '<div class="section-kicker">Platform Features</div>'
    '<div class="section-title">Intelligent Tools for Safer Networks</div>'
    '<div class="section-description">'
    'Machine-learning-powered capabilities designed to analyze network traffic, '
    'identify suspicious activity, and support faster security decisions.'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


features = [
    (
        "🧠",
        "AI Intrusion Detection",
        "Classify network traffic as normal or potentially malicious using trained machine learning models.",
    ),
    (
        "📊",
        "Intelligent Traffic Analysis",
        "Process network traffic features through preprocessing and machine learning pipelines.",
    ),
    (
        "🎯",
        "Attack Identification",
        "Identify major attack categories including DoS, Probe, R2L, and U2R.",
    ),
    (
        "⚡",
        "Early Warning",
        "Highlight suspicious traffic so potential threats can be reviewed earlier.",
    ),
    (
        "📋",
        "Detection History",
        "Review previous traffic analysis results and detection outcomes.",
    ),
    (
        "📈",
        "Model Performance",
        "Compare accuracy, precision, recall, F1-score, and confusion matrices.",
    ),
]


for row_start in [0, 3]:

    columns = st.columns(3)

    for index in range(3):

        icon, title, description = features[row_start + index]

        with columns[index]:

            with st.container(border=True):

                st.markdown(
                    f'<div class="card-icon">{icon}</div>',
                    unsafe_allow_html=True,
                )

                # ====================================================
                # DETECTION HISTORY → UNIQUE SECTION
                # ====================================================

                if title == "Detection History":

                    if st.button(
                        "📋  Detection History",
                        key="landing_detection_history",
                        width="content",
                    ):
                        st.session_state.page = "history"
                        st.rerun()

                # ====================================================
                # MODEL PERFORMANCE → UNIQUE SECTION
                # ====================================================

                elif title == "Model Performance":

                    if st.button(
                        "📈  Model Performance",
                        key="landing_model_performance",
                        width="content",
                    ):
                        st.session_state.page = "performance"
                        st.rerun()

                else:

                    st.markdown(
                        f'<div class="card-title">{title}</div>',
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    f'<div class="card-description">{description}</div>',
                    unsafe_allow_html=True,
                )


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div id="how-it-works"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading-wrapper">'
    '<div class="section-kicker">Simple Process</div>'
    '<div class="section-title">How It Works</div>'
    '<div class="section-description">'
    'From network traffic data to an actionable intrusion detection '
    'result in four simple steps.'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


steps = [
    (
        "01",
        "Upload Traffic",
        "Provide network traffic data containing the required features.",
    ),
    (
        "02",
        "Preprocess Data",
        "Encode categorical values and scale numerical traffic features.",
    ),
    (
        "03",
        "Run AI Analysis",
        "The trained model evaluates unseen network traffic records.",
    ),
    (
        "04",
        "View Detection",
        "Receive the prediction, attack category, and confidence score.",
    ),
]


step_columns = st.columns(4)

for index, step in enumerate(steps):

    number, title, description = step

    with step_columns[index]:

        with st.container(border=True):

            st.markdown(
                f'<div class="step-number">STEP {number}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="step-title">{title}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="step-description">{description}</div>',
                unsafe_allow_html=True,
            )


# ============================================================
# DETECTION COVERAGE
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div id="detection-coverage"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading-wrapper">'
    '<div class="section-kicker">Detection Coverage</div>'
    '<div class="section-title">Network Threat Categories</div>'
    '<div class="section-description">'
    'The current system uses the NSL-KDD dataset to classify traffic '
    'into normal traffic and four major attack categories.'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


threats = [
    ("🟢", "Normal", "Legitimate network traffic"),
    ("🔴", "DoS", "Denial-of-Service attacks"),
    ("🟠", "Probe", "Network reconnaissance"),
    ("🟣", "R2L", "Remote-to-local attacks"),
    ("⚠️", "U2R", "User-to-root attacks"),
]


threat_columns = st.columns(5)

for index, threat in enumerate(threats):

    icon, name, description = threat

    with threat_columns[index]:

        with st.container(border=True):

            st.markdown(
                f'<div class="threat-icon">{icon}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="threat-name">{name}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="threat-description">{description}</div>',
                unsafe_allow_html=True,
            )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

# IMPORTANT:
# Unique ID used only for Model Performance navigation.
st.markdown(
    '<div id="model-performance-section"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading-wrapper">'
    '<div class="section-kicker">Model Performance</div>'
    '<div class="section-title">Machine Learning Results</div>'
    '<div class="section-description">'
    'Compare the trained classification models using accuracy, F1-score, '
    'and attack detection performance.'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


performance_left, performance_right = st.columns(2)


with performance_left:

    with st.container(border=True):

        st.markdown(
            '<div class="resource-icon">📈</div>'
            '<div class="resource-title">Best Performing Model</div>'
            '<div class="resource-text">'
            'The Decision Tree model achieved the strongest overall result '
            'among the four evaluated models, with approximately 79.27% accuracy '
            'and 79.24% macro F1-score on the test data.'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<a class="resource-link" href="#platform-features">'
            '← Back to Platform Features'
            '</a>',
            unsafe_allow_html=True,
        )


with performance_right:

    with st.container(border=True):

        st.markdown(
            '<div class="resource-icon">🎯</div>'
            '<div class="resource-title">Evaluated Algorithms</div>'
            '<div class="resource-text">'
            'Random Forest, Decision Tree, Logistic Regression, and Linear SVM '
            'were evaluated for binary normal-versus-attack classification.'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<a class="resource-link" href="#detection-coverage">'
            'View Detection Coverage →'
            '</a>',
            unsafe_allow_html=True,
        )


# ============================================================
# DETECTION HISTORY
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

# IMPORTANT:
# Unique ID used only for Detection History navigation.
st.markdown(
    '<div id="detection-history-section"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading-wrapper">'
    '<div class="section-kicker">Detection History</div>'
    '<div class="section-title">Previous Analysis Overview</div>'
    '<div class="section-description">'
    'A summary area for previously analyzed network traffic and detection outcomes.'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


history_left, history_right = st.columns(2)


with history_left:

    with st.container(border=True):

        st.markdown(
            '<div class="resource-icon">📋</div>'
            '<div class="resource-title">Analysis Records</div>'
            '<div class="resource-text">'
            'The detection workflow can record analyzed traffic, predicted '
            'classification, attack category, and model confidence for review.'
            '</div>',
            unsafe_allow_html=True,
        )


with history_right:

    with st.container(border=True):

        st.markdown(
            '<div class="resource-icon">🛡️</div>'
            '<div class="resource-title">Detection Status</div>'
            '<div class="resource-text">'
            'Normal traffic and detected attack traffic can be reviewed as '
            'separate outcomes to support security analysis and reporting.'
            '</div>',
            unsafe_allow_html=True,
        )


st.markdown(
    '<div style="text-align:center; margin-top:22px;">'
    '<a class="resource-link" href="#platform-features">'
    '← Back to Platform Features'
    '</a>'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# ABOUT
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div id="about-securenet"></div>',
    unsafe_allow_html=True,
)

with st.container(border=True):

    st.markdown(
        '<div class="about-kicker">About SecureNet AI</div>'
        '<div class="about-title">Machine Learning for Network Security</div>',
        unsafe_allow_html=True,
    )

    about_left, about_right = st.columns(
        [1.5, 1],
        gap="large",
    )

    with about_left:

        st.markdown(
            '<div class="about-text">'
            'SecureNet AI is a machine-learning-based intrusion detection '
            'system designed to analyze network traffic and identify '
            'potentially malicious activity.'
            '</div>'
            '<br>'
            '<div class="about-text">'
            'The system uses Python and Scikit-learn to preprocess network '
            'traffic data, train classification models, and predict whether '
            'unseen traffic is normal or potentially intrusive.'
            '</div>'
            '<br>'
            '<div class="about-note">'
            'Current implementation performs dataset-based analysis. '
            'It does not perform continuous real-time packet monitoring.'
            '</div>',
            unsafe_allow_html=True,
        )

    with about_right:

        st.info(
            "Current System\n\n"
            "Dataset-based network traffic analysis"
        )

        st.info(
            "Machine Learning\n\n"
            "Scikit-learn classification models"
        )

        st.info(
            "Output\n\n"
            "Normal or Attack prediction"
        )

        st.info(
            "Attack Categories\n\n"
            "DoS, Probe, R2L, U2R"
        )


# ============================================================
# FINAL CTA
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="cta-title">'
    'Your Network Security Starts<br>'
    'with Better Detection.'
    '</div>'
    '<div class="cta-description">'
    'Analyze network traffic and explore machine-learning-powered '
    'intrusion detection with SecureNet AI.'
    '</div>',
    unsafe_allow_html=True,
)


st.markdown(
    "<br>",
    unsafe_allow_html=True,
)


cta_left, cta_middle, cta_right = st.columns(
    [1, 1, 1]
)


# ============================================================
# FINAL CTA → REGISTER PAGE
# ============================================================

with cta_middle:

    if st.button(
        "Start Network Analysis  →",
        key="final_start",
        width="stretch",
    ):
        st.session_state.page = "register"
        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="section-gap"></div>',
    unsafe_allow_html=True,
)

st.divider()


footer_1, footer_2, footer_3, footer_4 = st.columns(
    [2, 1, 1, 1]
)


with footer_1:

    st.markdown(
        '<div class="footer-title">🛡️ SecureNet AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-text">'
        'Machine-learning-powered network intrusion detection designed '
        'to identify suspicious traffic and provide actionable security insights.'
        '</div>',
        unsafe_allow_html=True,
    )


with footer_2:

    st.markdown(
        '<div class="footer-heading">Product</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#platform-features">Features</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#how-it-works">How It Works</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#detection-coverage">Detection</a>',
        unsafe_allow_html=True,
    )


with footer_3:

    st.markdown(
        '<div class="footer-heading">Resources</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#about-securenet">'
        'About SecureNet AI'
        '</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#model-performance-section">'
        'Model Performance'
        '</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#detection-history-section">'
        'Detection History'
        '</a>',
        unsafe_allow_html=True,
    )


with footer_4:

    st.markdown(
        '<div class="footer-heading">Security</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#detection-coverage">'
        'Network Analysis'
        '</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#detection-coverage">'
        'Attack Detection'
        '</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<a class="footer-link" href="#model-performance-section">'
        'Security Insights'
        '</a>',
        unsafe_allow_html=True,
    )


st.markdown(
    '<div class="copyright">'
    '© 2026 SecureNet AI. All rights reserved. '
    'Machine Learning Based Intrusion Detection System.'
    '</div>',
    unsafe_allow_html=True,
)