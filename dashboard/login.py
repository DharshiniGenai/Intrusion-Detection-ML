import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def show_login():

    st.markdown(
        """
        <style>

        /* ---------- PAGE ---------- */

        .stApp {
            background: #050b14;
        }

        #MainMenu {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        /* ---------- MAIN LOGIN AREA ---------- */

        .login-space {
            padding-top: 45px;
        }

        /* ---------- LEFT BRANDING ---------- */

        .brand-logo {
            font-size: 30px;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 55px;
        }

        .brand-logo span {
            color: #38bdf8;
        }

        .shield-box {
            width: 82px;
            height: 82px;
            border-radius: 22px;
            background: linear-gradient(135deg, #2563eb, #0ea5e9);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            margin-bottom: 28px;
            box-shadow: 0 0 35px rgba(14, 165, 233, 0.25);
        }

        .brand-heading {
            font-size: 42px;
            line-height: 1.15;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 20px;
        }

        .brand-heading span {
            color: #38bdf8;
        }

        .brand-description {
            color: #94a3b8;
            font-size: 15px;
            line-height: 1.8;
            max-width: 470px;
            margin-bottom: 35px;
        }

        /* ---------- SECURITY FEATURES ---------- */

        .security-box {
            background: #0b1726;
            border: 1px solid #1b344b;
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 12px;
        }

        .security-title {
            color: #e2e8f0;
            font-size: 14px;
            font-weight: 600;
        }

        .security-text {
            color: #64748b;
            font-size: 12px;
            margin-top: 3px;
        }

        .security-dot {
            color: #22c55e;
            margin-right: 8px;
        }

        /* ---------- RIGHT LOGIN CARD ---------- */

        .login-card-title {
            color: #f8fafc;
            font-size: 31px;
            font-weight: 750;
            margin-bottom: 8px;
        }

        .login-card-description {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        /* ---------- INPUTS ---------- */

        .stTextInput label {
            color: #cbd5e1 !important;
            font-size: 14px !important;
            font-weight: 600 !important;
        }

        .stTextInput input {
            background: #071321 !important;
            color: #f8fafc !important;
            border: 1px solid #29445c !important;
            border-radius: 9px !important;
            height: 48px !important;
        }

        .stTextInput input:focus {
            border-color: #38bdf8 !important;
            box-shadow: 0 0 0 1px #38bdf8 !important;
        }

        /* ---------- CHECKBOX ---------- */

        .stCheckbox label {
            color: #94a3b8 !important;
            font-size: 13px !important;
        }

        /* ---------- FORGOT PASSWORD ---------- */

        .forgot-link {
            text-align: right;
            padding-top: 8px;
        }

        .forgot-link a {
            color: #38bdf8;
            font-size: 13px;
            text-decoration: none;
        }

        /* ---------- SIGN IN ---------- */

        .stFormSubmitButton button {
            height: 48px;
            background: linear-gradient(
                90deg,
                #2563eb,
                #0284c7
            ) !important;
            color: white !important;
            border: none !important;
            border-radius: 9px !important;
            font-size: 15px !important;
            font-weight: 700 !important;
            margin-top: 15px;
        }

        .stFormSubmitButton button:hover {
            box-shadow: 0 0 25px rgba(37, 99, 235, 0.35);
        }

        /* ---------- REGISTER ---------- */

        .register-text {
            text-align: center;
            color: #64748b;
            font-size: 14px;
            margin-top: 25px;
        }

        .register-text span {
            color: #38bdf8;
            font-weight: 600;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "← Back to SecureNet AI",
        key="login_back",
        width="content",
    ):
        st.session_state.page = "landing"
        st.rerun()

    st.markdown(
        '<div class="login-space"></div>',
        unsafe_allow_html=True,
    )

    # Two-column login layout
    left, right = st.columns([1.1, 0.9], gap="large")

    # =========================================================
    # LEFT SIDE
    # =========================================================

    with left:

        st.markdown(
            """
            <div class="brand-logo">
                🛡️ SecureNet <span>AI</span>
            </div>

            <div class="shield-box">
                🛡️
            </div>

            <div class="brand-heading">
                Intelligent Security<br>
                <span>Starts Here.</span>
            </div>

            <div class="brand-description">
                Protect your network with AI-powered intrusion
                detection. Analyze traffic, identify threats,
                and monitor suspicious activity using machine
                learning.
            </div>

            <div class="security-box">
                <div class="security-title">
                    <span class="security-dot">●</span>
                    AI-Powered Detection
                </div>
                <div class="security-text">
                    Machine learning analyzes network traffic
                    for suspicious patterns.
                </div>
            </div>

            <div class="security-box">
                <div class="security-title">
                    <span class="security-dot">●</span>
                    Threat Classification
                </div>
                <div class="security-text">
                    Identify normal traffic and multiple
                    attack categories.
                </div>
            </div>

            <div class="security-box">
                <div class="security-title">
                    <span class="security-dot">●</span>
                    Network Insights
                </div>
                <div class="security-text">
                    Understand your network security through
                    meaningful analysis and reports.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # RIGHT SIDE
    # =========================================================

    with right:

        st.markdown(
            """
            <div class="login-card-title">
                Welcome back
            </div>

            <div class="login-card-description">
                Sign in to your account to continue monitoring
                your network security.
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("login_form"):

            email = st.text_input(
                "Email Address",
                placeholder="Enter your email address",
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
            )

            check_col, forgot_col = st.columns([1, 1])

            with check_col:
                remember_me = st.checkbox("Remember me")

            with forgot_col:
                st.markdown(
                    """
                    <div class="forgot-link">
                        <a href="#">Forgot password?</a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            submitted = st.form_submit_button(
                "Sign In",
                use_container_width=True,
            )

        if submitted:

            email = email.strip()
            password = password.strip()

            if not email:
                st.error("Please enter your email address.")

            elif not password:
                st.error("Please enter your password.")

            else:

                from src.database import verify_user

                user = verify_user(
                    email,
                    password,
                )

                if user is None:
                    st.error(
                        "Invalid email address or password."
                    )

                else:
                    st.session_state.user_id = user["id"]
                    st.session_state.user_name = user["full_name"]
                    st.session_state.user_email = user["email"]

                    st.session_state.page = "dashboard"
                    st.rerun()

        st.markdown(
            '<div class="register-text">Don\'t have an account?</div>',
            unsafe_allow_html=True,
        )

        if st.button("Create account", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()