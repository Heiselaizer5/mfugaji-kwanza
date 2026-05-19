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

    /* Keeps elements above the dark overlay */
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

    /* 3. Target the Streamlit Container block to act as our card */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: rgba(255, 255, 255, 0.96) !important;
        padding: 40px !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5) !important;
        max-width: 500px;
        margin: auto;
        margin-top: 15vh;
    }}

    /* Text styling inside the card */
    .login-heading {{
        color: #16300B; 
        font-weight: 700;
        font-size: 28px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        margin-bottom: 10px;
        line-height: 1.2;
    }}
    
    .login-subtext {{
        color: #555555;
        font-size: 15px;
        text-align: center;
        margin-bottom: 25px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}

    /* Custom Green Buttons */
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

# 1. Title on top-left
st.markdown("""
    <div class="brand-title">
        MFUGAJI KWANZA
        <span class="brand-subtitle">Modern Solutions for Every Poultry Farmer</span>
    </div>
""", unsafe_allow_html=True)

# 2. Centered Layout Column
_, center_col, _ = st.columns([1, 1.5, 1])

with center_col:
    # Creating a native Streamlit container with a border. 
    # Our CSS target above overrides this border to turn it into a beautiful white card.
    with st.container(border=True):
        st.markdown('<div class="login-heading">Unlock your farm\'s true profit potential</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtext">Log in or sign up to get started</div>', unsafe_allow_html=True)
        
        # Grid layout for buttons right inside the container
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.button("Log In", key="login_btn", use_container_width=True):
                st.toast("Opening Login form...")
                
        with btn_col2:
            if st.button("Sign Up", key="signup_btn", use_container_width=True):
                st.toast("Opening Sign Up form...")