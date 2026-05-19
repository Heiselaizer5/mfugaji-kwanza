import streamlit as st
from datetime import date

# --- Page Config ---
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide", initial_sidebar_state="collapsed")

# --- Session States ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "lang" not in st.session_state: st.session_state.lang = "Swahili"
if "view" not in st.session_state: st.session_state.view = "landing" # landing, login, signup, dashboard
if "sub_view" not in st.session_state: st.session_state.sub_view = "main"
if "farm_database" not in st.session_state: st.session_state.farm_database = {}

# --- Translation Engine ---
t = {
    "English": {
        "title": "MFUGAJI KWANZA", "sub": "Modern Poultry Management", 
        "login": "Log In", "signup": "Sign Up", "dash": "Dashboard", 
        "logout": "Logout", "expenses": "Expenses", "sales": "Sales"
    },
    "Swahili": {
        "title": "MFUGAJI KWANZA", "sub": "Mfumo wa Kisasa wa Kuku", 
        "login": "Ingia", "signup": "Jisajili", "dash": "Dashibodi", 
        "logout": "Toka", "expenses": "Gharama", "sales": "Mauzo"
    }
}

# --- CSS (Electric Green & Black Boards) ---
st.markdown(f"""
    <style>
    .brand-top {{ position: fixed; top: 15px; left: 20px; z-index: 999; color: #00E676; font-size: 28px; font-weight: 900; }}
    .stApp {{ background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }}
    .stApp::before {{ content: ""; position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.7); }}
    .board {{ background: #1A1A1A; padding: 30px; border-radius: 20px; border: 2px solid #333; }}
    div.stButton > button {{ background-color: #00E676 !important; color: black !important; font-weight: bold; border-radius: 10px; width: 100%; }}
    </style>
    <div class="brand-top">{t[st.session_state.lang]['title']}</div>
""", unsafe_allow_html=True)

# --- Translator (Juu kulia) ---
_, col_lang = st.columns([8, 1])
with col_lang:
    st.session_state.lang = st.selectbox("", ["Swahili", "English"], index=0 if st.session_state.lang == "Swahili" else 1)

# --- APP ROUTER ---
if not st.session_state.logged_in:
    # LANDING/LOGIN/SIGNUP VIEW
    _, center, _ = st.columns([1, 1.5, 1])
    with center:
        st.markdown("<div class='board'>", unsafe_allow_html=True)
        if st.session_state.view == "landing":
            st.markdown(f"<h1 style='color:white;'>{t[st.session_state.lang]['sub']}</h1>", unsafe_allow_html=True)
            if st.button(t[st.session_state.lang]['login']): st.session_state.view = "login"; st.rerun()
            if st.button(t[st.session_state.lang]['signup']): st.session_state.view = "signup"; st.rerun()
        elif st.session_state.view == "login":
            st.text_input("Username")
            st.text_input("Password", type="password")
            if st.button("Submit"): st.session_state.logged_in = True; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # DASHBOARD VIEW
    st.markdown(f"<div class='board'><h2>{t[st.session_state.lang]['dash']}</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.button(t[st.session_state.lang]['expenses'])
    with col2: st.button(t[st.session_state.lang]['sales'])
    
    if st.button(t[st.session_state.lang]['logout']):
        st.session_state.logged_in = False
        st.session_state.view = "landing"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
