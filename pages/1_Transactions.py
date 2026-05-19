import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="Mfugeji Kwanza - Options",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- High-Quality White Broiler Background Image Link ---
broiler_bg_url = "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600&auto=format&fit=crop"

# --- Frontend CSS Layout Engine ---
st.markdown(f"""
    <style>
    /* Full-screen layout background */
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

    /* Transparent top header bar */
    [data-testid="stHeader"] {{
        background-color: transparent !important;
        z-index: 10;
    }}

    .main .block-container {{
        z-index: 1;
        padding-top: 3rem !important;
    }}

    /* Top-Left App Title styling */
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

    /* Enforce rigid solid white form card layout */
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

    /* Premium Black Heading Styles */
    .black-heading {{
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 24px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        text-align: center !important;
        margin-bottom: 25px !important;
        line-height: 1.3 !important;
        text-transform: uppercase; /* Forces uppercase style matching your message */
        letter-spacing: 0.5px;
    }}

    /* Sleek Solid Black Buttons */
    div.stButton > button {{
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 15px 20px !important; /* Slightly taller for distinct choices */
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
    # Rigid container form block
    with st.form(key="options_container_form"):
        
        # Heading prompt inside the card wrapper
        st.markdown('<div class="black-heading">CHOOSE WHAT YOU WANT TO DO</div>', unsafe_allow_html=True)
        
        # Dual column split for the layout buttons
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.form_submit_button("Input Data", use_container_width=True):
                st.toast("Redirecting to Input Ledger...")
                # Later you will route: st.switch_page("pages/2_Input_Data.py")
                
        with btn_col2:
            if st.form_submit_button("Withdraw", use_container_width=True):
                st.toast("Opening Withdrawal menu...")
                # Later you will route: st.switch_page("pages/3_Withdraw.py")
