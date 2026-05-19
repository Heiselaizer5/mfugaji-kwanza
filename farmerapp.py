import streamlit as st
from datetime import date

# --- Page Config ---
st.set_page_config(page_title="Mfugaji Kwanza", layout="wide")

# --- Initialize Session ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "users" not in st.session_state: st.session_state.users = {"admin": "admin123"} # Database ya users
if "sub_view" not in st.session_state: st.session_state.sub_view = "dashboard"
if "farm_database" not in st.session_state: st.session_state.farm_database = {}

# --- CSS ya Kisasa (Dark Mode) ---
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: white; }
    div[data-testid="stForm"] { background-color: #1E1E1E; padding: 20px; border-radius: 15px; border: 1px solid #333; }
    input { background-color: white !important; color: black !important; }
    .stButton > button { background-color: #00E676; color: black; font-weight: bold; width: 100%; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 1. LOGIN NA SIGN UP LOGIC ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center;'>🐔 MFUGAJI KWANZA</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🔐 INGIA (LOGIN)", "📝 JISAJILI (SIGN UP)"])
    
    with tab1:
        with st.form("login_form"):
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.form_submit_button("Ingia"):
                if st.session_state.users.get(user) == pw:
                    st.session_state.logged_in = True
                    st.rerun()
                else: st.error("Taarifa si sahihi!")
                
    with tab2:
        with st.form("signup_form"):
            new_user = st.text_input("Username Mpya")
            new_pw = st.text_input("Password Mpya", type="password")
            if st.form_submit_button("Jisajili"):
                if new_user in st.session_state.users: st.warning("User huyu yupo tayari!")
                else:
                    st.session_state.users[new_user] = new_pw
                    st.success("Akaunti imetengenezwa! Sasa Ingia.")

# --- 2. DASHBOARD (Baada ya Login) ---
else:
    st.sidebar.button("Toka (Log Out)", on_click=lambda: st.session_state.update({"logged_in": False}))
    
    st.title("📊 Dashibodi ya Shamba")
    
    # Navigation ndani ya dashboard
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛒 Rekodi Gharama"): st.session_state.sub_view = "inputs"
    with col2:
        if st.button("💰 Rekodi Mauzo"): st.session_state.sub_view = "sales"
        
    # --- FOMU YA GHARAMA ---
    if st.session_state.sub_view == "inputs":
        with st.form("expenses"):
            st.subheader("Gharama za Vifaranga")
            d = st.date_input("Tarehe")
            chicks = st.number_input("Gharama Vifaranga", 0.0)
            feed = st.number_input("Gharama Chakula", 0.0)
            if st.form_submit_button("Hifadhi"):
                st.session_state.farm_database[str(d)] = {"cost": chicks + feed, "revenue": 0}
                st.success("Imehifadhiwa!")
                
    # --- FOMU YA MAUZO ---
    elif st.session_state.sub_view == "sales":
        with st.form("sales"):
            st.subheader("Mauzo ya Kuku")
            d = st.date_input("Tarehe")
            rev = st.number_input("Mapato ya Mauzo", 0.0)
            if st.form_submit_button("Hifadhi"):
                if str(d) in st.session_state.farm_database:
                    st.session_state.farm_database[str(d)]["revenue"] = rev
                    st.success("Mauzo Yamehifadhiwa!")
                else: st.error("Rekodi gharama za tarehe hii kwanza!")

    # --- MUHTASARI ---
    st.divider()
    st.subheader("Muhtasari wa Data")
    st.write(st.session_state.farm_database)
