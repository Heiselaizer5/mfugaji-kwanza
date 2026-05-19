import streamlit as st
from datetime import date

# --- Config ---
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide", initial_sidebar_state="collapsed")

# --- Initialize ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "lang" not in st.session_state: st.session_state.lang = "Swahili"
if "view" not in st.session_state: st.session_state.view = "landing" # landing, login, signup, dashboard

# --- Translations ---
t = {
    "English": {"title": "MFUGAJI KWANZA", "login": "Login", "signup": "Sign Up", "dash": "Dashboard", "logout": "Logout", "welcome": "Welcome back, Farmer!"},
    "Swahili": {"title": "MFUGAJI KWANZA", "login": "Ingia", "signup": "Jisajili", "dash": "Dashibodi", "logout": "Toka", "welcome": "Karibu Mfugaji!"}
}

# --- CSS (Electric Green & Branding) ---
st.markdown(f"""
    <style>
    .brand-top-left {{ position: fixed; top: 15px; left: 20px; z-index: 999; color: #00E676; font-size: 28px; font-weight: 900; text-shadow: 2px 2px 4px #000; }}
    .stApp {{ background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600&auto=format&fit=crop"); background-size: cover; background-attachment: fixed; }}
    .stApp::before {{ content: ""; position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.7); }}
    div.stButton > button {{ background-color: #00E676 !important; color: #000 !important; font-weight: bold; border-radius: 10px; }}
    .main {{ z-index: 1; }}
    </style>
    <div class="brand-top-left">{t[st.session_state.lang]['title']}</div>
""", unsafe_allow_html=True)

# --- Translator (Juu kulia) ---
col_lang, _ = st.columns([8, 1])
with col_lang:
    lang_choice = st.selectbox("", ["Swahili", "English"], index=0 if st.session_state.lang == "Swahili" else 1)
    st.session_state.lang = lang_choice

# --- Main App Logic ---
if not st.session_state.logged_in:
    # LANDING PAGE
    st.markdown("<br><br><br><h1 style='color:white; text-align:center;'>Welcome to Mfugaji Kwanza</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button(t[st.session_state.lang]['login']): st.session_state.view = "login"; st.rerun()
        if st.button(t[st.session_state.lang]['signup']): st.session_state.view = "signup"; st.rerun()
    
    # Hapa weka forms za login/signup kulingana na view
else:
    # DASHBOARD
    st.markdown(f"<h2 style='color:#00E676;'>{t[st.session_state.lang]['dash']}</h2>", unsafe_allow_html=True)
    st.write(f"### {t[st.session_state.lang]['welcome']}")
    
    # Hapa weka zile transactions zako
    if st.button(t[st.session_state.lang]['logout']): 
        st.session_state.logged_in = False
        st.session_state.view = "landing"
        st.rerun()
