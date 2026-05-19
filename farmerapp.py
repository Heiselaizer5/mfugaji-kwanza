import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# 2. Session State
if "view" not in st.session_state:
    st.session_state.view = "login"

# 3. CSS
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }
    .brand-top { position: fixed; top: 10px; left: 20px; color: #00E676; font-size: 30px; font-weight: 900; z-index: 1000; }
    .white-board { background: white; padding: 30px; border-radius: 15px; color: black; }
    div.stButton > button { background-color: #00E676 !important; color: black !important; font-weight: bold; border-radius: 10px; }
    </style>
    <div class="brand-top">MFUGAJI KWANZA</div>
""", unsafe_allow_html=True)

# 4. Logic
lang = st.selectbox("Language / Lugha", ["English", "Swahili"])

_, col, _ = st.columns([1, 2, 1])
with col:
    st.markdown('<div class="white-board">', unsafe_allow_html=True)
    if st.session_state.view == "login":
        st.header("Login" if lang == "English" else "Ingia")
        st.text_input("Username")
        st.text_input("Password", type="password")
        if st.button("Login"):
            st.session_state.view = "dashboard"
            st.rerun()
    elif st.session_state.view == "dashboard":
        st.header("Dashboard")
        if st.button("Logout"):
            st.session_state.view = "login"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
