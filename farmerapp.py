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

# --- Complete Frontend CSS Layout Engine ---
st.markdown(f"""
    <style>
    /* 1. Full-screen layout background */
    .stApp {{
        background-image: url("{broiler_bg_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Dark background filter overlay */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 0;
    }}

    /* Make top app options bar transparent */
    [data-testid="stHeader"] {{
        background-color: transparent !important;
        z-index: 10;
    }}

    .main .block-container {{
        z-index: 1;
        padding-top: 3rem !important;
    }}

    /* 2. Top-Left App Title styling */
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

    /* 3. Bulletproof Container Override */
    /* This targets Streamlit's container block directly and forces it to be a solid white card box */
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stNotification"]) {{
        background-color: #FFFFFF !important;
    }}
    
    /* Global fallback layout logic for central box wrapper */
    .st-emotion-cache-12m0g85, [data-testid="stForm"], .stForm, div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: #FFFFFF !important;
        border: none !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6) !important;
        padding: 40px !important;
        max-width: 480px !important;
        margin: auto !important;
        margin-top: 18vh !important;
    }}

    /* Premium Black Typography Elements */
    .black-heading {{
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 26px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        text-align: center !important;
        margin-bottom: 8px !important;
        line-height: 1.3 !important;
    }}
    
    .black-subtext {{
        color: #444444 !important;
        font-size: 15px !important;
        text-align: center !important;
        margin-bottom: 25px !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }}

    /* Sleek Solid Black Buttons */
    div.stButton > button {{
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        transition: all 0.2s ease-in-out;
    }}
    
    div.stButton > button:hover {{
        background-color: #222222 !important;
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Render Page Elements ---

# 1. Brand Logo on Top LEFT
st.markdown("""
    <div class="brand-title">
        MFUGAJI KWANZA
        <span class="brand-subtitle">Modern Solutions for Every Poultry Farmer</span>
    </div>
""", unsafe_allow_html=True)

# 2. Central Layout Grid
_, center_col, _ = st.columns([1, 1.3, 1])

with center_col:
    # Wrapping everything directly inside a Streamlit form layout.
    # Streamlit natively forces forms to have a rigid container box structure, 
    # ensuring the background can NEVER strip out or turn transparent!
    with st.form(key="login_container_form", clear_on_submit=False):
        
        # Native black text injection inside the card box boundary
        st.markdown('<div class="black-heading">Unlock your farm\'s true profit potential</div>', unsafe_allow_html=True)
        st.markdown('<div class="black-subtext">Log in or sign up to get started</div>', unsafe_allow_html=True)
        
        # Button split row
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.form_submit_button("Log In", use_container_width=True):
                st.toast("Opening Login form...")
                
        with btn_col2:
            # We use an alternate key identifier so the engine builds two separate button endpoints
            if st.form_submit_button("Sign Up", use_container_width=True):
                st.toast("Opening Sign Up form...")