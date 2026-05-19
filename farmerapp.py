import streamlit as st

# 1. Page Config (Lazima iwe mstari wa kwanza)
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# 2. State management
if "view" not in st.session_state: st.session_state.view = "landing"
if "lang" not in st.session_state: st.session_state.lang = "English"

# 3. Content dictionary
content = {
    "English": {"title": "MFUGAJI KWANZA", "sub": "Unlock your farm's true profit potential", "btn1": "Log In", "btn2": "Sign Up", "dash": "Dashboard"},
    "Swahili": {"title": "MFUGAJI KWANZA", "sub": "Fungua uwezo halisi wa faida wa shamba lako", "btn1": "Ingia", "btn2": "Jisajili", "dash": "Dashibodi"}
}

# 4. Styling (CSS)
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }
    .white-board { background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 15px; color: black; }
    div.stButton > button { background-color: #1a4d1a !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# 5. UI Layout
# Translator juu kushoto au kulia
st.session_state.lang = st.selectbox("Language / Lugha", ["English", "Swahili"])

if st.session_state.view == "landing":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.title(content[st.session_state.lang]["title"])
    with col2:
        # Hii ni ile "white board" unayoitaka
        with st.container():
            st.markdown(f'<div class="white-board"><h2>{content[st.session_state.lang]["sub"]}</h2>', unsafe_allow_html=True)
            if st.button(content[st.session_state.lang]["btn1"]): st.session_state.view = "dashboard"; st.rerun()
            if st.button(content[st.session_state.lang]["btn2"]): st.session_state.view = "dashboard"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.view == "dashboard":
    # Hapa ndipo dashboard yako itakapokaa ndani ya ile ile board
    st.markdown(f'<div class="white-board"><h1>{content[st.session_state.lang]["dash"]}</h1>', unsafe_allow_html=True)
    st.write("Transactions zitaonekana hapa...")
    if st.button("Back"): st.session_state.view = "landing"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
