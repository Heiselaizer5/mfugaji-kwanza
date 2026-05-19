import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide", initial_sidebar_state="collapsed")

# --- Initialize Session State ---
if "language" not in st.session_state:
    st.session_state.language = "English"

# --- Translations Dictionary ---
translations = {
    "English": {
        "title": "MFUGAJI KWANZA",
        "subtitle": "Modern Solutions for Every Poultry Farmer",
        "heading": "Unlock your farm's true profit potential",
        "subtext": "Log in or sign up to get started",
        "lang_label": "Select Language / Chagua Lugha"
    },
    "Swahili": {
        "title": "MFUGAJI KWANZA",
        "subtitle": "Ufumbuzi wa Kisasa kwa Kila Mfugaji",
        "heading": "Fungua uwezo halisi wa faida wa shamba lako",
        "subtext": "Ingia au jisajili ili kuanza",
        "lang_label": "Select Language / Chagua Lugha"
    }
}

# --- Background Image (Kuku) ---
bg_url = "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600&auto=format&fit=crop"

# --- CSS Styling ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
    }}
    .overlay {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        color: white;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Logic ya Lugha ---
lang = st.selectbox(translations[st.session_state.language]["lang_label"], ["English", "Swahili"])
st.session_state.language = lang
t = translations[st.session_state.language]

# --- UI Layout ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    st.markdown(f"""
        <div class="overlay">
            <h1>{t['title']}</h1>
            <h4>{t['subtitle']}</h4>
            <br>
            <h2>{t['heading']}</h2>
            <p>{t['subtext']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Hapa ndipo utaweka form yako ya Login
    with st.form("login_form"):
        st.text_input("Username")
        st.text_input("Password", type="password")
        if st.form_submit_button("Submit"):
            st.success("Redirecting...")
