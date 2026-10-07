import streamlit as st


def show_register():

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

        .register-space {
            padding-top: 35px;
        }

        /* ---------- BRAND ---------- */

        .register-logo {
            font-size: 29px;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 35px;
        }

        .register-logo span {
            color: #38bdf8;
        }

        /* ---------- CREATIVE VISUAL ---------- */

        .visual-title {
            color: #f8fafc;
            font-size: 38px;
            font-weight: 800;
            line-height: 1.2;
            margin-top: 20px;
        }

        .visual-title span {
            color: #38bdf8;
        }

        .visual-description {
            color: #94a3b8;
            font-size: 15px;
            line-height: 1.8;
            max-width: 480px;
            margin-top: 18px;
        }

        /* ---------- SECURITY CARD ---------- */

        .feature-card {
            background: #0b1726;
            border: 1px solid #1b344b;
            border-radius: 12px;
            padding: 15px 17px;
            margin-top: 12px;
        }

        .feature-title {
            color: #e2e8f0;
            font-size: 14px;
            font-weight: 600;
        }

        .feature-description {
            color: #64748b;
            font-size: 12px;
            margin-top: 4px;
        }

        /* ---------- RIGHT SIDE ---------- */

        .create-title {
            color: #f8fafc;
            font-size: 31px;
            font-weight: 750;
            margin-bottom: 8px;
        }

        .create-description {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 25px;
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
            height: 46px !important;
        }

        .stTextInput input:focus {
            border-color: #38bdf8 !important;
            box-shadow: 0 0 0 1px #38bdf8 !important;
        }

        .stCheckbox label {
            color: #94a3b8 !important;
            font-size: 12px !important;
        }

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
            margin-top: 12px;
        }

        .signin-text {
            text-align: center;
            color: #64748b;
            font-size: 14px;
            margin-top: 20px;
        }

        .signin-button button {
            color: #38bdf8 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="register-space"></div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.1, 0.9], gap="large")

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        st.markdown(
            '<div class="register-logo">🛡️ SecureNet <span>AI</span></div>',
            unsafe_allow_html=True,
        )

        # Native Streamlit creative visual
        visual_col1, visual_col2, visual_col3 = st.columns([1, 2, 1])

        with visual_col2:
            st.markdown(
                """
                <div style="
                    text-align:center;
                    font-size:70px;
                    padding:25px;
                    border-radius:25px;
                    background:linear-gradient(
                        135deg,
                        #102a54,
                        #0b506f
                    );
                    box-shadow:0 0 45px rgba(14,165,233,0.22);
                    border:1px solid #1d5270;
                ">
                    🛡️
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div class="visual-title">
                Build a Safer<br>
                <span>Digital Network.</span>
            </div>

            <div class="visual-description">
                Create your SecureNet AI account and get access
                to intelligent network traffic analysis,
                intrusion detection, threat classification,
                and security insights.
            </div>
            """,
            unsafe_allow_html=True,
        )

        feature1, feature2 = st.columns(2)

        with feature1:
            st.markdown(
                """
                <div class="feature-card">
                    <div class="feature-title">
                        🛡️ AI Detection
                    </div>
                    <div class="feature-description">
                        Intelligent traffic analysis
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with feature2:
            st.markdown(
                """
                <div class="feature-card">
                    <div class="feature-title">
                        ⚡ Threat Analysis
                    </div>
                    <div class="feature-description">
                        Identify suspicious activity
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">
                    📊 Security Insights
                </div>
                <div class="feature-description">
                    Understand network behavior through
                    meaningful security analytics.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right:

        st.markdown(
            """
            <div class="create-title">
                Create your account
            </div>

            <div class="create-description">
                Join SecureNet AI and start protecting your
                network with intelligent threat detection.
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("register_form"):

            full_name = st.text_input(
                "Full Name",
                placeholder="Enter your full name",
            )

            email = st.text_input(
                "Email Address",
                placeholder="Enter your email address",
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Create a password",
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Confirm your password",
            )

            terms = st.checkbox(
                "I agree to the Terms of Service and Privacy Policy"
            )

            submitted = st.form_submit_button(
                "Create Account",
                use_container_width=True,
            )

        if submitted:

            full_name = full_name.strip()
            email = email.strip()
            password = password.strip()
            confirm_password = confirm_password.strip()

            if not full_name:
                st.error("Please enter your full name.")

            elif not email:
                st.error("Please enter your email address.")

            elif not password:
                st.error("Please create a password.")

            elif password != confirm_password:
                st.error("Passwords do not match.")

            elif not terms:
                st.error("Please accept the Terms of Service.")

            else:
                st.success("Account created successfully.")

        st.markdown(
            '<div class="signin-text">Already have an account?</div>',
            unsafe_allow_html=True,
        )

        if st.button("Sign in", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()