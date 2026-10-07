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
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background-color: #f7faf8;
        color: #17231d;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1rem;
        padding-bottom: 2rem;
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

    [data-testid="stToolbar"] {
        display: none;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        border-radius: 10px;
        min-height: 46px;
        border: 1px solid #d9e5df;
        background-color: #ffffff;
        color: #183127;
        font-weight: 600;
        font-size: 14px;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #145c45;
        color: #145c45;
        background-color: #f1f8f4;
    }


    /* ========================================================
       PRIMARY BUTTON
       ======================================================== */

    .primary-button .stButton > button {
        background-color: #145c45;
        color: white;
        border-color: #145c45;
    }

    .primary-button .stButton > button:hover {
        background-color: #0f4d39;
        color: white;
        border-color: #0f4d39;
    }


    /* ========================================================
       NAVIGATION
       ======================================================== */

    .nav-brand {
        font-size: 21px;
        font-weight: 750;
        color: #17231d;
        padding-top: 7px;
    }

    .nav-icon {
        background-color: #145c45;
        color: white;
        padding: 8px 10px;
        border-radius: 10px;
        margin-right: 7px;
    }

    .nav-link-button .stButton > button {
        border: none;
        background: transparent;
        color: #68766f;
        min-height: 40px;
        padding: 0;
    }

    .nav-link-button .stButton > button:hover {
        background: transparent;
        color: #145c45;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero-badge {
        display: inline-block;
        background-color: #e8f4ed;
        color: #145c45;
        border-radius: 30px;
        padding: 8px 15px;
        font-size: 12px;
        font-weight: 650;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 62px;
        line-height: 1.04;
        letter-spacing: -2.5px;
        font-weight: 760;
        color: #17231d;
        margin-bottom: 20px;
    }

    .hero-accent {
        color: #145c45;
    }

    .hero-description {
        color: #64736b;
        font-size: 17px;
        line-height: 1.75;
        max-width: 650px;
        margin-bottom: 22px;
    }

    .hero-feature {
        color: #617068;
        font-size: 13px;
        margin-top: 13px;
    }

    .hero-feature-mark {
        color: #145c45;
        font-weight: bold;
        margin-right: 7px;
    }


    /* ========================================================
       ANALYSIS PREVIEW
       ======================================================== */

    .analysis-header {
        font-size: 17px;
        font-weight: 700;
        color: #17231d;
    }

    .analysis-subtitle {
        font-size: 12px;
        color: #77847e;
        margin-top: 3px;
    }

    .ready-badge {
        background-color: #e9f7ef;
        color: #198754;
        border-radius: 20px;
        padding: 5px 9px;
        font-size: 9px;
        font-weight: 750;
        text-align: center;
    }

    .analysis-number {
        font-size: 30px;
        font-weight: 760;
        color: #17231d;
    }

    .analysis-caption {
        font-size: 10px;
        color: #98a49e;
    }

    .result-title {
        font-size: 11px;
        color: #7b8982;
    }

    .result-normal {
        font-size: 18px;
        font-weight: 720;
        color: #17231d;
    }

    .result-confidence {
        font-size: 18px;
        font-weight: 720;
        color: #145c45;
    }

    .result-caption {
        font-size: 9px;
        color: #9aa49f;
    }


    /* ========================================================
       SECTION HEADINGS
       ======================================================== */

    .section-kicker {
        color: #145c45;
        font-size: 11px;
        font-weight: 750;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        text-align: center;
    }

    .section-title {
        color: #17231d;
        font-size: 38px;
        font-weight: 750;
        letter-spacing: -1px;
        text-align: center;
        margin-top: 7px;
    }

    .section-description {
        color: #718078;
        font-size: 14px;
        line-height: 1.7;
        text-align: center;
        max-width: 690px;
        margin: 8px auto 30px auto;
    }


    /* ========================================================
       CARD TITLES
       ======================================================== */

    .card-title {
        font-size: 16px;
        font-weight: 700;
        color: #17231d;
    }

    .card-description {
        color: #718078;
        font-size: 12px;
        line-height: 1.7;
        margin-top: 8px;
    }

    .card-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }


    /* ========================================================
       PROCESS
       ======================================================== */

    .step-number {
        color: #145c45;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    .step-title {
        color: #17231d;
        font-size: 17px;
        font-weight: 700;
        margin-top: 13px;
    }

    .step-description {
        color: #718078;
        font-size: 12px;
        line-height: 1.7;
        margin-top: 7px;
    }


    /* ========================================================
       THREAT
       ======================================================== */

    .threat-icon {
        font-size: 25px;
        text-align: center;
    }

    .threat-name {
        color: #17231d;
        font-weight: 700;
        font-size: 15px;
        text-align: center;
        margin-top: 8px;
    }

    .threat-description {
        color: #78857f;
        font-size: 10px;
        text-align: center;
        margin-top: 5px;
    }


    /* ========================================================
       ABOUT
       ======================================================== */

    .about-title {
        color: white;
        font-size: 38px;
        font-weight: 750;
        line-height: 1.15;
    }

    .about-kicker {
        color: #8bd0af;
        font-size: 11px;
        font-weight: 750;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .about-text {
        color: #c3d7ce;
        font-size: 14px;
        line-height: 1.8;
    }

    .about-note {
        color: #91b1a4;
        font-size: 11px;
        line-height: 1.7;
    }


    /* ========================================================
       CTA
       ======================================================== */

    .cta-title {
        color: #17231d;
        font-size: 38px;
        line-height: 1.15;
        font-weight: 750;
        letter-spacing: -1px;
        text-align: center;
    }

    .cta-description {
        color: #718078;
        font-size: 14px;
        line-height: 1.7;
        text-align: center;
        max-width: 620px;
        margin: 10px auto 25px auto;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer-title {
        color: #17231d;
        font-size: 17px;
        font-weight: 720;
    }

    .footer-text {
        color: #78857f;
        font-size: 11px;
        line-height: 1.7;
    }

    .footer-heading {
        color: #17231d;
        font-size: 12px;
        font-weight: 700;
    }

    .footer-item {
        color: #78857f;
        font-size: 11px;
        margin-top: 6px;
    }

    .copyright {
        color: #98a49e;
        font-size: 10px;
        text-align: center;
        padding-top: 18px;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 900px) {

        .hero-title {
            font-size: 43px;
        }

        .section-title {
            font-size: 31px;
        }

        .cta-title {
            font-size: 31px;
        }

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


with nav_features:

    st.markdown(
        '<div class="nav-link-button">',
        unsafe_allow_html=True,
    )

    if st.button(
        "Features",
        key="nav_features",
        use_container_width=True,
    ):
        st.session_state.page = "landing"

    st.markdown("</div>", unsafe_allow_html=True)


with nav_how:

    if st.button(
        "How It Works",
        key="nav_how",
        use_container_width=True,
    ):
        st.session_state.page = "landing"


with nav_detection:

    if st.button(
        "Detection",
        key="nav_detection",
        use_container_width=True,
    ):
        st.session_state.page = "analyze"


with nav_about:

    if st.button(
        "About",
        key="nav_about",
        use_container_width=True,
    ):
        st.session_state.page = "landing"


with nav_signin:

    if st.button(
        "Sign In",
        key="nav_signin",
        use_container_width=True,
    ):
        st.session_state.page = "login"
        st.rerun()


with nav_start:

    st.markdown(
        '<div class="primary-button">',
        unsafe_allow_html=True,
    )

    if st.button(
        "Get Started",
        key="nav_get_started",
        use_container_width=True,
    ):
        st.session_state.page = "register"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


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

    with button_one:

        st.markdown(
            '<div class="primary-button">',
            unsafe_allow_html=True,
        )

        if st.button(
            "Start Detection  →",
            key="hero_start",
            use_container_width=True,
        ):
            st.session_state.page = "register"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with button_two:

        if st.button(
            "Explore Platform",
            key="hero_explore",
            use_container_width=True,
        ):
            st.session_state.page = "login"
            st.rerun()

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
                '<div class="analysis-subtitle">Machine learning intrusion detection</div>',
                unsafe_allow_html=True,
            )

        with header_right:

            st.markdown(
                '<div class="ready-badge">SYSTEM READY</div>',
                unsafe_allow_html=True,
            )

        st.write("")

        with st.container(border=True):

            st.markdown(
                '<div class="analysis-caption">Training Traffic Records</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="analysis-number">125,973</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="analysis-caption">NSL-KDD training records</div>',
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
                use_container_width=True,
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

st.write("")
st.write("")

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

st.write("")
st.write("")
st.write("")

st.markdown(
    '<div class="section-kicker">Platform Features</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Intelligent Tools for Safer Networks</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-description">
        Machine-learning-powered capabilities designed to
        analyze network traffic, identify suspicious activity,
        and support faster security decisions.
    </div>
    """,
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

st.write("")
st.write("")
st.write("")

st.markdown(
    '<div class="section-kicker">Simple Process</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">How It Works</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-description">
        From network traffic data to an actionable intrusion
        detection result in four simple steps.
    </div>
    """,
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

st.write("")
st.write("")
st.write("")

st.markdown(
    '<div class="section-kicker">Detection Coverage</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Network Threat Categories</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-description">
        The current system uses the NSL-KDD dataset to
        classify traffic into normal traffic and four
        major attack categories.
    </div>
    """,
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
# ABOUT
# ============================================================

st.write("")
st.write("")
st.write("")


with st.container(border=True):

    st.markdown(
        '<div class="about-kicker">About SecureNet AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="about-title">Machine Learning for Network Security</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    about_left, about_right = st.columns(
        [1.5, 1],
        gap="large",
    )

    with about_left:

        st.markdown(
            """
            <div class="about-text">
                SecureNet AI is a machine-learning-based
                intrusion detection system designed to analyze
                network traffic and identify potentially malicious
                activity.
            </div>

            <br>

            <div class="about-text">
                The system uses Python and Scikit-learn to
                preprocess network traffic data, train
                classification models, and predict whether
                unseen traffic is normal or potentially intrusive.
            </div>

            <br>

            <div class="about-note">
                Current implementation performs dataset-based
                analysis. It does not perform continuous
                real-time packet monitoring.
            </div>
            """,
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

st.write("")
st.write("")
st.write("")

st.markdown(
    """
    <div class="cta-title">
        Your Network Security Starts<br>
        with Better Detection.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cta-description">
        Analyze network traffic and explore
        machine-learning-powered intrusion detection
        with SecureNet AI.
    </div>
    """,
    unsafe_allow_html=True,
)


cta_left, cta_middle, cta_right = st.columns(
    [1, 1, 1]
)


with cta_middle:

    st.markdown(
        '<div class="primary-button">',
        unsafe_allow_html=True,
    )

    if st.button(
        "Start Network Analysis  →",
        key="final_start",
        use_container_width=True,
    ):
        st.session_state.page = "register"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

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
        """
        <div class="footer-text">
            Machine-learning-powered network intrusion detection
            designed to identify suspicious traffic and provide
            actionable security insights.
        </div>
        """,
        unsafe_allow_html=True,
    )


with footer_2:

    st.markdown(
        '<div class="footer-heading">Product</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Features</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">How It Works</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Detection</div>',
        unsafe_allow_html=True,
    )


with footer_3:

    st.markdown(
        '<div class="footer-heading">Resources</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">About SecureNet AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Model Performance</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Detection History</div>',
        unsafe_allow_html=True,
    )


with footer_4:

    st.markdown(
        '<div class="footer-heading">Security</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Network Analysis</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Attack Detection</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-item">Security Insights</div>',
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="copyright">
        © 2026 SecureNet AI. All rights reserved.
        Machine Learning Based Intrusion Detection System.
    </div>
    """,
    unsafe_allow_html=True,
)