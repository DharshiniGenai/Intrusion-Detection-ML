
import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def show_forgot_password():

    # ========================================================
    # PAGE STYLING
    # ========================================================

    st.markdown(
        """
        <style>

        .stApp {
            background: #050b14;
        }

        #MainMenu,
        header,
        footer {
            visibility: hidden;
        }

        .forgot-space {
            height: 45px;
        }

        .forgot-logo {
            font-size: 29px;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 30px;
        }

        .forgot-logo span {
            color: #38bdf8;
        }

        .forgot-title {
            color: #f8fafc;
            font-size: 34px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .forgot-description {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.7;
            margin-bottom: 24px;
        }

        .security-card {
            background: #0b1726;
            border: 1px solid #1b344b;
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 16px;
        }

        .security-icon {
            font-size: 38px;
            margin-bottom: 12px;
        }

        .security-heading {
            color: #f8fafc;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 7px;
        }

        .security-text {
            color: #94a3b8;
            font-size: 13px;
            line-height: 1.7;
        }

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

        .stFormSubmitButton button {
            height: 48px !important;
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
        }

        .stFormSubmitButton button:hover {
            background: linear-gradient(
                90deg,
                #1d4ed8,
                #0369a1
            ) !important;
        }

        .back-button button {
            background: transparent !important;
            border: none !important;
            color: #38bdf8 !important;
            font-size: 13px !important;
            padding: 4px 0 !important;
        }

        .back-button button:hover {
            color: #7dd3fc !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # TOP SPACING
    # ========================================================

    st.markdown(
        '<div class="forgot-space"></div>',
        unsafe_allow_html=True,
    )

    # ========================================================
    # MAIN LAYOUT
    # ========================================================

    left, right = st.columns(
        [1.05, 0.95],
        gap="large",
    )

    # ========================================================
    # LEFT SIDE
    # ========================================================

    with left:

        st.markdown(
            """
            <div class="forgot-logo">
                🛡️ SecureNet <span>AI</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="security-card">
                <div class="security-icon">🔐</div>
                <div class="security-heading">
                    Account Recovery
                </div>
                <div class="security-text">
                    Reset your SecureNet AI password and regain
                    access to your network security dashboard.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="security-card">
                <div class="security-icon">🛡️</div>
                <div class="security-heading">
                    Secure Access
                </div>
                <div class="security-text">
                    Your new password will replace the existing
                    password for your SecureNet AI account.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ========================================================
    # RIGHT SIDE
    # ========================================================

    with right:

        st.markdown(
            """
            <div class="forgot-title">
                Forgot password?
            </div>

            <div class="forgot-description">
                Enter your registered details and create a new
                password for your account.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ----------------------------------------------------
        # PASSWORD RESET FORM
        # ----------------------------------------------------

        with st.form("forgot_password_form"):

            full_name = st.text_input(
                "Full Name",
                placeholder="Enter your full name",
            )

            email = st.text_input(
                "Email Address",
                placeholder="Enter your registered email",
            )

            new_password = st.text_input(
                "New Password",
                type="password",
                placeholder="Create a new password",
            )

            confirm_password = st.text_input(
                "Confirm New Password",
                type="password",
                placeholder="Confirm your new password",
            )

            submitted = st.form_submit_button(
                "Reset Password",
                use_container_width=True,
            )

        # ----------------------------------------------------
        # RESET LOGIC
        # ----------------------------------------------------

        if submitted:

            full_name = full_name.strip()
            email = email.strip()
            new_password = new_password.strip()
            confirm_password = confirm_password.strip()

            if not full_name:

                st.error(
                    "Please enter your full name."
                )

            elif not email:

                st.error(
                    "Please enter your email address."
                )

            elif not new_password:

                st.error(
                    "Please enter a new password."
                )

            elif len(new_password) < 6:

                st.error(
                    "Password must contain at least 6 characters."
                )

            elif new_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                from src.database import reset_user_password

                success = reset_user_password(
                    full_name,
                    email,
                    new_password,
                )

                if success:

                    st.success(
                        "Password reset successfully. "
                        "You can now sign in with your new password."
                    )


                else:

                    st.error(
                        "We could not verify those account details."
                    )

        # ----------------------------------------------------
        # BACK TO LOGIN
        # ----------------------------------------------------

        st.markdown(
            '<div class="back-button">',
            unsafe_allow_html=True,
        )

        if st.button(
            "← Back to Sign In",
            key="forgot_back_login",
            use_container_width=False,
        ):
            st.session_state.page = "login"
            st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )
