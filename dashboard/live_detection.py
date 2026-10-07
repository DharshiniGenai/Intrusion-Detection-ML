import streamlit as st

from src.live_detector import analyze_live_traffic


def show_live_detection():

    # ============================================================
    # PAGE STYLING
    # ============================================================

    st.markdown(
        """
        <style>

        .live-kicker {
            color: #31b8ff;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1.8px;
            margin-bottom: 12px;
        }

        .live-heading {
            font-size: 46px;
            font-weight: 800;
            color: #f4f7fb;
            line-height: 1.1;
            margin-bottom: 12px;
        }

        .live-description {
            color: #9caec2;
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 24px;
            max-width: 900px;
        }

        .ready-pill {
            background: #123f37;
            color: #b7e7d7;
            border-radius: 8px;
            padding: 15px 20px;
            font-size: 14px;
            font-weight: 700;
            text-align: center;
            margin-top: 4px;
        }

        .live-info {
            background: #132f4d;
            border: 1px solid rgba(80, 160, 230, 0.15);
            border-radius: 10px;
            padding: 16px 20px;
            color: #b8c9db;
            font-size: 14px;
            line-height: 1.6;
            margin: 18px 0 30px 0;
        }

        .capture-card {
            background: #0d1b2d;
            border: 1px solid #29415c;
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 22px;
        }

        .capture-title {
            color: #f1f5f9;
            font-size: 22px;
            font-weight: 750;
            margin-bottom: 6px;
        }

        .capture-description {
            color: #8fa2b8;
            font-size: 14px;
            margin-bottom: 20px;
        }

        .results-header {
            color: #f1f5f9;
            font-size: 28px;
            font-weight: 750;
            margin-top: 34px;
            margin-bottom: 5px;
        }

        .results-description {
            color: #8799ad;
            font-size: 14px;
            margin-bottom: 16px;
        }

        .metric-box {
            background: #0d1b2d;
            border: 1px solid #29415c;
            border-radius: 14px;
            padding: 20px;
            min-height: 110px;
        }

        .metric-label {
            color: #9aacc0;
            font-size: 13px;
            font-weight: 650;
            margin-bottom: 8px;
        }

        .metric-value {
            color: #eef4fa;
            font-size: 32px;
            font-weight: 800;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ============================================================
    # BACK TO DASHBOARD
    # ============================================================

    if st.button(
        "←  Back to Dashboard",
        key="live_back_dashboard",
        width="content",
    ):
        st.session_state.page = "dashboard"
        st.rerun()

    st.write("")

    # ============================================================
    # HEADER
    # ============================================================

    header_left, header_right = st.columns(
        [4, 1],
        vertical_alignment="center",
    )

    with header_left:

        st.markdown(
            '<div class="live-kicker">NETWORK TRAFFIC MONITORING</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="live-heading">Live Network Detection</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="live-description">
                Capture live network traffic and use the trained
                machine-learning IDS model to identify normal and
                potentially suspicious network flows.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with header_right:

        st.markdown(
            '<div class="ready-pill">● IDS SYSTEM READY</div>',
            unsafe_allow_html=True,
        )

    # ============================================================
    # INFORMATION BAR
    # ============================================================

    st.markdown(
        """
        <div class="live-info">
            <strong>🔒 Live traffic analysis</strong>
            &nbsp;•&nbsp;
            Packet capture
            &nbsp;•&nbsp;
            Flow feature extraction
            &nbsp;•&nbsp;
            Machine-learning classification
            &nbsp;•&nbsp;
            Normal / Attack detection
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ============================================================
    # CAPTURE CONFIGURATION
    # ============================================================

    st.markdown(
        '<div class="capture-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="capture-title">📡 Live Capture Configuration</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="capture-description">
            Configure how much live network traffic should be captured
            before the IDS performs its analysis.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        packet_count = st.number_input(
            "Packets to capture",
            min_value=5,
            max_value=200,
            value=30,
            step=5,
        )

    with col2:

        timeout = st.number_input(
            "Capture timeout (seconds)",
            min_value=5,
            max_value=60,
            value=15,
            step=5,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ============================================================
    # START DETECTION
    # ============================================================

    if st.button(
        "▶  Start Live Detection",
        key="start_live_detection",
        type="primary",
        width="stretch",
    ):

        with st.spinner(
            "Capturing packets and analyzing network flows..."
        ):

            results = analyze_live_traffic(
                count=int(packet_count),
                timeout=int(timeout),
            )

        # ========================================================
        # NO RESULTS
        # ========================================================

        if not results:

            st.warning(
                "No network flows were captured during this detection window."
            )

            return

        # ========================================================
        # RESULT COUNTS
        # ========================================================

        attacks = sum(
            1
            for result in results
            if result["prediction"] == "Attack"
        )

        normal = len(results) - attacks

        st.success(
            f"Live analysis complete — {len(results)} flows analyzed."
        )

        # ========================================================
        # METRICS
        # ========================================================

        metric_1, metric_2, metric_3 = st.columns(3)

        with metric_1:

            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">
                        FLOWS ANALYZED
                    </div>
                    <div class="metric-value">
                        {len(results)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with metric_2:

            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">
                        NORMAL FLOWS
                    </div>
                    <div class="metric-value">
                        {normal}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with metric_3:

            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">
                        ATTACKS DETECTED
                    </div>
                    <div class="metric-value">
                        {attacks}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ========================================================
        # DETECTION RESULTS
        # ========================================================

        st.markdown(
            '<div class="results-header">Detection Results</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="results-description">
                Flow-level predictions generated from the captured
                network traffic.
            </div>
            """,
            unsafe_allow_html=True,
        )

        table_rows = []

        for index, result in enumerate(results, start=1):

            table_rows.append(
                {
                    "Flow": index,
                    "Source": (
                        f"{result['src_ip']}:{result['src_port']}"
                    ),
                    "Destination": (
                        f"{result['dst_ip']}:{result['dst_port']}"
                    ),
                    "Protocol": result["protocol"].upper(),
                    "Packets": result["packet_count"],
                    "Source Bytes": result["src_bytes"],
                    "Destination Bytes": result["dst_bytes"],
                    "Prediction": result["prediction"],
                    "Confidence": f"{result['confidence']:.2f}%",
                }
            )

        st.dataframe(
            table_rows,
            width="stretch",
            hide_index=True,
        )

        # ========================================================
        # DETECTION SUMMARY
        # ========================================================

        if attacks == 0:

            st.info(
                "No attack flows were detected during this capture window."
            )

        else:

            st.warning(
                f"{attacks} suspicious flow(s) were detected. "
                "Review the detection results above."
            )