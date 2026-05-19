import streamlit as st

# Config ya msingi
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# Styling ya kuzuia error za layout
st.markdown("""
    <style>
    .stApp { background: #f0f2f6; }
    .main-box { background: white; padding: 30px; border-radius: 20px; max-width: 500px; margin: auto; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("MFUGAJI KWANZA")
st.write("Karibu - Ingia au Jisajili")

# Kutumia 'tabs' moja kwa moja bila kurudia elements
tab_login, tab_signup = st.tabs(["Ingia", "Jisajili"])

with tab_login:
    st.text_input("Jina la mtumiaji")
    st.text_input("Nenosiri", type="password")
    if st.button("Ingia Sasa"):
        st.success("Unaingia...")

with tab_signup:
    st.text_input("Jina kamili")
    st.text_input("Namba ya simu")
    st.button("Jisajili Sasa")

st.markdown('</div>', unsafe_allow_html=True)
