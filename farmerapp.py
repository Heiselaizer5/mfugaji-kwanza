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

    /* Make Streamlit's native header transparent so icons float on the image */
    [data-testid="stHeader"] {{
        background-color: transparent !important;
        z-index: 10;
    }}

    /* Keeps elements above the dark overlay */
    .main .block-container {{
        z-index: 1;
        padding-top: 3rem !important;
    }}

    /* 2. Brand Title locked to the Top-LEFT Corner */
    .brand-title {{
        position: absolute;
        top: 25px;
        left: 40px;
        text-align: left;
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

    /* 3. The Custom White Card Box (Guaranteed Solid Box) */
    .custom-card-wrapper {{
        background-color: rgb(255, 255, 255) !important; /* Forced solid white */
        padding: 40px !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6) !important;
        max-width: 480px;
        margin: auto;
        margin-top: 20vh;
        text-align: center;
    }}

    /* Bold Black Text styling inside the card */
    .login-heading {{
        color: #000000 !important; /* Premium Bold Black */
        font-weight: 800 !important;
        font-size: 26px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        margin-bottom: 8px !important;
        line-height: 1.3 !important;
    }}
    
    .login-subtext {{
        color: #444444 !important; /* Charcoal for readability */
        font-size: 15px !important;
        margin-bottom: 25px !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }}

    /* Sleek Solid Black Buttons */
    div.stButton > button {{
        background-color: #000000 !important; /* Solid Black */
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
        background-color: #222222 !important; /* Soft dark gray on hover */
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Render Elements ---

# 1. Brand Logo on Top LEFT
st.markdown("""
    <div class="brand-title">
        MFUGAJI KWANZA
        <span class="brand-subtitle">Modern Solutions for Every Poultry Farmer</span>
    </div>
""", unsafe_allow_html=True)

# 2. Centered Layout Column
_, center_col, _ = st.columns([1, 1.3, 1])

with center_col:
    # Custom HTML container div block that forces the solid white box color
    st.markdown('<div class="custom-card-wrapper">', unsafe_allow_html=True)
    
    st.markdown('<div class="login-heading">Unlock your farm\'s true profit potential</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtext">Log in or sign up to get started</div>', unsafe_allow_html=True)
    
    # Grid layout for buttons sitting inside the card
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        if st.button("Log In", key="login_btn", use_container_width=True):
            st.toast("Opening Login form...")
            
    with btn_col2:
        if st.button("Sign Up", key="signup_btn", use_container_width=True):
            st.toast("Opening Sign Up form...")
            
    # Close the custom HTML container block
    st.markdown('</div>', unsafe_allow_html=True)