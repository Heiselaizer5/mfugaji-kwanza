import streamlit as st

# Configure the page
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# CSS to fix layout, styling, and branding
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600"); background-size: cover; }
    .white-board { background: white; padding: 40px; border-radius: 25px; color: black; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-top: 50px; }
    .brand-title { font-size: 28px; font-weight: 900; text-align: center; color: #333; }
    .sub-text { text-align: center; color: #666; margin-bottom: 20px; }
    div.stButton > button { background-color: #008000 !important; color: white !important; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# Layout container
_, col_main, _ = st.columns([1, 1.2, 1])

with col_main:
    st.markdown('<div class="white-board">', unsafe_allow_html=True)
    st.markdown('<p class="brand-title">MFUGAJI KWANZA</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Modern Poultry Management Solutions</p>', unsafe_allow_html=True)
    
    # Use tabs to isolate elements, preventing DuplicateElementId errors
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.text_input("Username", key="login_user")
        st.text_input("Password", type="password", key="login_pass")
        if st.button("Login", key="login_btn"):
            st.success("Accessing Dashboard...")
            
    with tab2:
        st.text_input("Full Name", key="signup_name")
        st.text_input("Phone Number", key="signup_phone")
        st.text_input("Password", type="password", key="signup_pass")
        if st.button("Register", key="signup_btn"):
            st.success("Account Created!")
            
    st.markdown('</div>', unsafe_allow_html=True)
