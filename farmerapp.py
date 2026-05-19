import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# 2. Session State
if "view" not in st.session_state:
    st.session_state.view = "login"

# 3. CSS (Electric Green & Branding)
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }
    .brand-top { position: fixed; top: 10px; left: 20px; color: #00E676; font-size: 30px; font-weight: 900; z-index: 1000; }
    .white-board { background: white; padding: 30px; border-radius: 20px; color: black; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    div.stButton > button { background-color: #00E676 !important; color: black !important; font-weight: bold; border-radius: 10px; width: 100%; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    </style>
    <div class="brand-top">MFUGAJI KWANZA</div>
""", unsafe_allow_html=True)

# 4. Main Layout
lang = st.selectbox("Language / Lugha", ["English", "Swahili"])

_, col, _ = st.columns([1, 1.5, 1])
with col:
    st.markdown('<div class="white-board">', unsafe_allow_html=True)
    
    # Hapa tunaweka Tabs za Login na Signup
    tab1, tab2 = st.tabs(["Login" if lang == "English" else "Ingia", "Sign Up" if lang == "English" else "Jisajili"])
    
    with tab1:
        st.text_input("Username")
        st.text_input("Password", type="password")
        if st.button("Login"):
            st.success("Welcome!")
            
    with tab2:
        st.text_input("Full Name")
        st.text_input("Phone Number")
        st.text_input("Create Password", type="password")
        if st.button("Register"):
            st.success("Account Created!")
            
    st.markdown('</div>', unsafe_allow_html=True)
