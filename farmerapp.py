import streamlit as st

# --- Must be the first Streamlit command ---
st.set_page_config(
    page_title="Mfugaji Kwanza - Login",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- High-Quality White Broiler Background Image Link ---
broiler_bg_url = "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600&auto=format&fit=crop"

# --- Custom CSS Styling ---
st.markdown(f"""
    <style>
    /* 1. Full-screen background layout */
    .stApp {{
        background-image: url("{broiler_bg_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Dark overlay to make everything readable */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 0;
    }}

    /* 2. Modifying Streamlit's native header to sit nicely INSIDE the background */
    [data-testid="stHeader"] {{
        background-color: transparent !important; /* Removes the solid dark bar */
        z-index: 10;
        top: 45px !important; /* Pushes the pencil and 3 dots down below your brand title */
    }}

    /* Keeps elements above the dark overlay */
    .main .block-container {{
        z-index: 1;
        padding-top: 3rem !important;
    }}

    /* 3. Brand Title shifted to the Top-RIGHT Corner */
    .brand-title {{
        position: absolute;
        top: 25px;
        right: 40px; /* Aligned to the right */
        text-align: right; /* Text flushes to the right edge */
        color: #FFFFFF;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-weight: 900;
        font-size: 38px;
        letter-spacing: 2px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
        z-index: 100;
    }}
    
    .brand-subtitle {{
        font-size: 14px;
        font-family: Arial, sans-serif;
        font-weight: normal;
        color: #F0F0F0;
        display: block;
        margin-top: -5px;
    }}

    /* 4. Custom Login Card */
    .custom-login-card {{
        background-color: #FFFFFF !important; /* Pure, solid white */
        padding: 40px 35px 85px 35px !important; /* Added bottom padding to accommodate buttons */
        border-radius: 20px !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6) !important;
        text-align: center !important;
        margin-top: 20vh;
        border: 1px solid #E0E0E0;
    }}

    /* Text styling inside the card */
    .login-heading {{
        color: #16300B !important; 
        font-weight: 700 !important;
        font-size: 26px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        margin-bottom: 12px !important;
        line-height: 1.3 !important;
    }}
    
    .login-subtext {{
        color: #555555 !important;
        font-size: 15px !important;
        margin-bottom: 30px !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }}

    /* Custom Premium Green Buttons */
    div.stButton > button {{
        background-color: #16300B !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        transition: all 0.2s ease-in-out;
    }}
    
    div.stButton > button:hover {{
        background-color: #244C13 !important;
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Render Elements ---

# 1. Brand Logo on Top RIGHT
st.markdown("""
    <div class="brand-title">
        MFUGAJI KWANZA
        <span class="brand-subtitle">Modern Solutions for Every Poultry Farmer</span>
    </div>
""", unsafe_allow_html=True)

# 2. Centered Layout Column
_, center_col, _ = st.columns([1, 1.4, 1])

with center_col:
    with st.container():
        st.markdown('''
            <div class="custom-login-card">
                <div class="login-heading">Unlock your farm's true profit potential</div>
                <div class="login-subtext">Log in or sign up to get started</div>
            </div>
        ''', unsafe_allow_html=True)
        
        # Pull the buttons neatly inside the white card container boundary
        st.markdown('<div style="margin-top: -75px; padding: 0px 35px 35px 35px;">', unsafe_allow_html=True)
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.button("Log In", key="login_btn", use_container_width=True):
                st.toast("Opening Login form...")
                
        with btn_col2:
            if st.button("Sign Up", key="signup_btn", use_container_width=True):
                st.toast("Opening Sign Up form...")
        st.markdown('</div>', unsafe_allow_html=True)