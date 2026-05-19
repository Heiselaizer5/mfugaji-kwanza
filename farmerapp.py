import streamlit as st

# Page Config
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# CSS ya White Board na Styling
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }
    .white-board { background: white; padding: 40px; border-radius: 25px; color: black; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-top: 50px; }
    .title-text { font-size: 24px; font-weight: bold; margin-bottom: 5px; color: #333; text-align: center; }
    .desc-text { font-size: 16px; color: #666; margin-bottom: 30px; text-align: center; }
    div.stButton > button { background-color: #008000 !important; color: white !important; font-weight: bold; border-radius: 10px; width: 100%; }
    .stSelectbox { width: 200px !important; margin-left: auto; }
    </style>
""", unsafe_allow_html=True)

# Translator
lang = st.selectbox("Language / Lugha", ["English", "Swahili"])

# Layout
_, col_main, _ = st.columns([1, 1.2, 1])

with col_main:
    st.markdown('<div class="white-board">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">MFUGAJI KWANZA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-text">' + 
                ("Modern Poultry Management Solutions" if lang == "English" else "Suluhisho za Kisasa za Ufugaji wa Kuku") + 
                '</p>', unsafe_allow_html=True)
    
    # Tabs za Login na Signup
    tab1, tab2 = st.tabs(["Login" if lang == "English" else "Ingia", "Sign Up" if lang == "English" else "Jisajili"])
    
    with tab1:
        st.text_input("Username" if lang == "English" else "Jina la Mtumiaji")
        st.text_input("Password" if lang == "English" else "Nenosiri", type="password")
        st.button("Login" if lang == "English" else "Ingia")
            
    with tab2:
        st.text_input("Full Name" if lang == "English" else "Jina Kamili")
        st.text_input("Phone Number" if lang == "English" else "Namba ya Simu")
        st.text_input("Password" if lang == "English" else "Nenosiri", type="password")
        st.button("Register" if lang == "English" else "Jisajili")
            
    st.markdown('</div>', unsafe_allow_html=True)
