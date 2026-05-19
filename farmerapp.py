import streamlit as st

# --- Must be the first Streamlit command ---
st.set_page_config(
    page_title="Mfugeji Kwanza - Login",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="collapsed" # Hides the sidebar for a clean landing page
)

# --- Background Image Link ---
# Using a high-quality online poultry farm image so it works instantly on Streamlit Cloud
bg_image_url = "https://images.unsplash.com/photo-1516467508483-a7212febe31a?q=80&w=1600&auto=format&fit=crop"

# --- Custom CSS Styling ---
st.markdown(f"""
    <style>
    /* 1. Sets full-screen background */
    .stApp {{
        background-image: url("{bg_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Dark overlay to make text pop and look professional */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
        z-index: 0;
    }}

    /* Ensures content stays above the dark overlay */
    [data-testid="stHeader"], .main .block-container {{
        z-index: 1;
    }}

    /* 2. Top-Left Brand Title */
    .brand-title {{
        position: absolute;
        top: 30px;
        left: 40px;
        color: #FFFFFF;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-weight: 900;
        font-size: 38px;
        letter-spacing: 2px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
    }}
    
    .brand-subtitle {{
        font-size: 14px;
        font-family: Arial, sans-serif;
        font-weight: normal;
        color: #E0E0E0;
        display: block;
        margin-top: -5px;
    }}

    /* 3. Central Login Card */
    .login-box {{
        background-color: rgba(255, 255, 255, 0.95);
        padding: 40px 50px;
        border-radius: 16px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.4);
        text-align: center;
        max-width: 450px;
        margin: auto;
        margin-top: 18vh;
    }}

    .login-heading {{
        color: #1A330E; /* Deep farm green */
        font-weight: 700;
        font-size: 26px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 8px;
    }}
    
    .login-subtext {{
        color: #666666;
        font-size: 14px;
        margin-bottom: 30px;
    }}

    /* Style adjustment for Streamlit buttons inside the card */
    div.stButton > button {{
        background-color: #1A330E !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
    }}
    
    div.stButton > button:hover {{
        background-color: #2D541B !important;
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Render the Elements ---

# 1. Top Left App Title
st.markdown("""
    <div class="brand-title">
        MFUGAJI KWANZA
        <span class="brand-subtitle">Modern Solutions for Every Poultry Farmer</span>
    </div>
""", unsafe_allow_html=True)

# 2. Centering Layout for the Card
_, center_col, _ = st.columns([1, 1.8, 1])

with center_col:
    # Open our stylized box HTML container
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-heading">Secure Access to Your Farm\'s Future</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtext">Connecting farmers to profit</div>', unsafe_allow_html=True)
    
    # Grid for Side-by-Side Buttons
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        if st.button("Log In", key="login_btn", use_container_width=True):
            st.toast("Logging you in...") # Dynamic temporary notification
            
    with btn_col2:
        if st.button("Sign Up", key="signup_btn", use_container_width=True):
            st.toast("Opening registration...")

    # Close the HTML container
    st.markdown('</div>', unsafe_allow_html=True)