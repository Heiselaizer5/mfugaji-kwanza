import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# 2. CSS - Nimepunguza ukubwa wa translator na kuweka layout safi
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }
    .brand-top { position: fixed; top: 10px; left: 20px; color: #00E676; font-size: 30px; font-weight: 900; z-index: 1000; }
    .white-board { background: white; padding: 30px; border-radius: 20px; color: black; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .poultry-text { font-size: 18px; color: #333; margin-bottom: 20px; font-style: italic; text-align: center; }
    div.stButton > button { background-color: #00E676 !important; color: black !important; font-weight: bold; border-radius: 10px; width: 100%; }
    /* Kupunguza size ya translator */
    .stSelectbox { max-width: 200px; margin-left: auto; }
    </style>
    <div class="brand-top">MFUGAJI KWANZA</div>
""", unsafe_allow_html=True)

# 3. Translator iliyopunguzwa size
col_lang1, col_lang2 = st.columns([6, 1])
with col_lang2:
    lang = st.selectbox("", ["EN", "SW"], index=1)

# 4. Main Layout
_, col_main, _ = st.columns([1, 1.5, 1])
with col_main:
    st.markdown('<div class="white-board">', unsafe_allow_html=True)
    
    # Maelezo kuhusu Poultry juu ya Login/Signup
    st.markdown('<div class="poultry-text">' + 
                ("Modern Poultry Management Solutions" if lang == "EN" else "Suluhisho za Kisasa za Ufugaji wa Kuku") + 
                '</div>', unsafe_allow_html=True)
    
    # Tabs za Login na Signup
    tab1, tab2 = st.tabs(["Login" if lang == "EN" else "Ingia", "Sign Up" if lang == "EN" else "Jisajili"])
    
    with tab1:
        st.text_input("Username" if lang == "EN" else "Jina la Mtumiaji")
        st.text_input("Password" if lang == "EN" else "Nenosiri", type="password")
        st.button("Login" if lang == "EN" else "Ingia")
            
    with tab2:
        st.text_input("Full Name" if lang == "EN" else "Jina Kamili")
        st.text_input("Phone Number" if lang == "EN" else "Namba ya Simu")
        st.text_input("Create Password" if lang == "EN" else "Nenosiri jipya", type="password")
        st.button("Register" if lang == "EN" else "Jisajili")
            
    st.markdown('</div>', unsafe_allow_html=True)
