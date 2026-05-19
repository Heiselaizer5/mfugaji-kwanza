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
    /* 1. Sets full-screen broiler background */
    .stApp {{
        background-image: url("{broiler_bg_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Dark overlay to make everything highly readable */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.45);
        z-index: 0;
    }}

    /* Keeps all app text and buttons sitting on top of the background overlay */
    [data-testid="stHeader"], .main .block-container {{
        z-index: 1;
    }}

    /* 2. Top-Left Title "MFUGAJI KWANZA" */
    .brand-title {{
        position: absolute;
        top: 30px;
        left: 40px;
        color: #FFFFFF;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-weight: 900;
        font-size: 38px;
        letter-spacing: 2px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
    }}
    
    .brand-subtitle {{
        font-size: 14px;
        font-family: Arial, sans-serif;
        font-weight: normal;
        color: #F0F0F0;
        display: block;
        margin-top: -5px;
    }}

    /* 3. Central Login Card (Holds all text and buttons neatly inside) */
    .login-box {{
        background-color: rgba(255, 255, 255, 0.96);
        padding: 45px 40px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        text-align: center;
        max-width: 500px;
        margin: auto;
        margin-top: 18vh;
    }}

    .login-heading {{
        color: #16300B; /* Premium Dark Green */
        font-weight: 700;
        font-size: 28px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 10px;
        line-height: 1.2;
    }}
    
    .login-subtext {{
        color: #555555;
        font-size: 15px;
        margin-bottom: 35px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}

    /* Premium Green Buttons */
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
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Render Elements On-Screen ---

# 1. Brand Logo on Top Left
st.markdown("""
    <div class="brand-title">
        MFUGAJI KWANZA
        <span class="brand-subtitle">Modern Solutions for Every Poultry Farmer</span>
    </div>
""", unsafe_allow_html=True)

# 2. Centered Layout Structure
_, center_col, _ = st.columns([1, 1.6, 1])

with center_col:
    # Opening HTML Container for the Card
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    
    # Texts inside the white popup box
    st.markdown('<div class="login-heading">Unlock your farm\'s true profit potential</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtext">Log in or sign up to get started</div>', unsafe_allow_html=True)
    
    # Side-by-Side Grid Layout for buttons
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        if st.button("Log In", key="login_btn", use_container_width=True):
            st.toast("Opening Login form...")
            
    with btn_col2:
        if st.button("Sign Up", key="signup_btn", use_container_width=True):
            st.toast("Opening Sign Up form...")

    # Closing HTML Container
    st.markdown('</div>', unsafe_allow_html=True)