import streamlit as st
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Mfugaji Kwanza - Broiler Manager",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Initialize Session States kwa ajili ya kuhifadhi data ---
if "language" not in st.session_state:
    st.session_state.language = "Swahili"

if "sub_view" not in st.session_state:
    st.session_state.sub_view = "dashboard"

if "profit_calculated" not in st.session_state:
    st.session_state.profit_calculated = False

# Kuhifadhi kumbukumbu za mahesabu
if "input_chicks_cost" not in st.session_state: st.session_state.input_chicks_cost = 0.0
if "input_feed_cost" not in st.session_state: st.session_state.input_feed_cost = 0.0
if "input_med_cost" not in st.session_state: st.session_state.input_med_cost = 0.0
if "input_other_cost" not in st.session_state: st.session_state.input_other_cost = 0.0

if "sales_qty" not in st.session_state: st.session_state.sales_qty = 0
if "sales_price" not in st.session_state: st.session_state.sales_price = 0.0
if "sales_revenue" not in st.session_state: st.session_state.sales_revenue = 0.0

# Kuhifadhi tarehe za matukio
if "inputs_date" not in st.session_state: st.session_state.inputs_date = "-"
if "sales_date" not in st.session_state: st.session_state.sales_date = "-"

# --- Background Image ---
broiler_bg_url = "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?q=80&w=1600&auto=format&fit=crop"

# --- Kamusi ya Lugha (Translations) ---
translations = {
    "English": {
        "subtitle": "Modern Solutions for Every Poultry Farmer",
        "welcome": "Broiler Batch Manager",
        "instruction": "Select an option below to manage development, expenditure, or broiler sales.",
        "choice_inputs": "🛒 Development & Expenditure of Chicks",
        "choice_withdraw": "💰 Broiler Sales",
        "desc_inputs": "Record expenses for chicks, feeds, medications, and other general farm production costs.",
        "desc_withdraw": "Record number of mature chickens sold, selling price, and calculate harvest return.",
        "back_btn": "← Back to Dashboard",
        
        # Inputs Form
        "input_header": "Development & Expenditure of Chicks",
        "label_chicks": "Total Cost of Vifaranga (TSH)",
        "label_feed": "Total Cost of Chakula/Feeds (TSH)",
        "label_med": "Total Cost of Meds & Vaccines (TSH)",
        "label_other": "Total Cost of Other Expenses (TSH)",
        "finish_inputs_btn": "🏁 Finish & Calculate Expenses",
        
        # Sales Form
        "sales_header": "Broiler Sales (Harvest Details)",
        "label_qty": "Number of Chickens Sold",
        "label_price": "Price per Chicken (TSH)",
        "finish_sales_btn": "🏁 Finish & Calculate Sales",
        
        # Financial Summary Card
        "summary_header": "📊 Financial Performance Summary",
        "total_expenses": "Total Expenses (Expenditures):",
        "total_revenue": "Total Sales Revenue:",
        "calc_profit_btn": "📈 Calculate Net Profit",
        "net_profit": "Net Profit:",
        "record_date": "Recorded on:",
        "profit_msg": "🎉 Congratulations! Your batch made a PROFIT of",
        "loss_msg": "⚠️ Attention! Your batch made a LOSS of"
    },
    "Swahili": {
        "subtitle": "Ufumbuzi wa Kisasa kwa Kila Mfugaji wa Kuku",
        "welcome": "Usimamizi wa Kuku wa Nyama (Broiler)",
        "instruction": "Chagua hatua hapa chini kusimajili maendeleo, gharama, au mauzo ya broiler.",
        "choice_inputs": "🛒 Maendeleo na Gharama za Vifaranga",
        "choice_withdraw": "💰 Mauzo ya Kuku (Broiler Sales)",
        "desc_inputs": "Sajili gharama za vifaranga, chakula, madawa, na gharama nyinginezo za uzalishaji.",
        "desc_withdraw": "Sajili idadi ya kuku waliokomaa waliouzwa, bei ya kuuzia, na kukokotoa mapato ya jumla.",
        "back_btn": "← Rudi Kwenye Dashibodi",
        
        # Inputs Form
        "input_header": "Maendeleo na Gharama za Vifaranga (Development & Expenditure)",
        "label_chicks": "Gharama Kamili ya Vifaranga (TSH)",
        "label_feed": "Gharama Kamili ya Chakula (TSH)",
        "label_med": "Gharama Kamili ya Chanjo na Dawa (TSH)",
        "label_other": "Gharama za Vikorokoro Nyinginezo (TSH)",
        "finish_inputs_btn": "🏁 Maliza na Ukokotoe Gharama (Finish)",
        
        # Sales Form
        "sales_header": "Mauzo ya Kuku (Broiler Sales)",
        "label_qty": "Idadi ya Kuku Waliouzwa",
        "label_price": "Bei kwa Kila Kuku mmoja (TSH)",
        "finish_sales_btn": "🏁 Maliza na Ukokotoe Mauzo (Finish)",
        
        # Financial Summary Card
        "summary_header": "📊 Muhtasari wa Mapato na Faida",
        "total_expenses": "Jumla ya Matumizi (Expenditure):",
        "total_revenue": "Jumla ya Mapato ya Mauzo:",
        "calc_profit_btn": "📈 Piga Hesabu ya Net Profit",
        "net_profit": "Faida Net (Net Profit):",
        "record_date": "Tarehe ya kurekodi:",
        "profit_msg": "🎉 Hongera! Batch hii imeingiza FAIDA ya",
        "loss_msg": "⚠️ Angalizo! Batch hii imeingiza HASARA ya"
    }
}

lang = st.session_state.language
t = translations[lang]

# --- CSS Styling (PREMIUM DARK BOARDS + SOLID WHITE FORMS + STABILITY FIX) ---
st.markdown(f"""
    <style>
    /* Full screen setup with locked height constraints to prevent jumping */
    .stApp {{
        background-image: url("{broiler_bg_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6); z-index: 0;
    }}
    [data-testid="stHeader"] {{ background-color: transparent !important; z-index: 10; }}
    
    /* Optimized padding to keep components mathematically centered and stable */
    .main .block-container {{ 
        z-index: 1; 
        padding-top: 1.5rem !important; 
        padding-bottom: 1.5rem !important; 
    }}

    .brand-title {{
        color: #FFFFFF; font-family: 'Arial Black', sans-serif; font-weight: 900;
        font-size: 38px; letter-spacing: 2px; text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
    }}
    .brand-subtitle {{ font-size: 14px; font-family: Arial, sans-serif; color: #F0F0F0; display: block; margin-top: -5px; }}

    /* MABADILIKO: Dashboard Cards sasa ni NYEUSI TAJIRI (Premium Dark Theme) */
    .dashboard-card {{
        background-color: #1A1A1A !important; 
        border: 2px solid #2D2D2D !important;
        border-radius: 16px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.6) !important; 
        padding: 25px !important;
        text-align: center; 
        margin-top: 10px;
        min-height: 200px; /* Locked height stabilizes layout changes */
    }}
    
    /* Muhtasari wa Fedha (Financial Summary) Card - NYEUSI */
    .summary-card-dark {{
        background-color: #1A1A1A !important; 
        border-radius: 20px !important; 
        padding: 30px !important; 
        box-shadow: 0 12px 35px rgba(0,0,0,0.7) !important; 
        border-left: 10px solid #00E676 !important;
        margin-top: 15px;
    }}

    .white-card-heading {{ color: #FFFFFF !important; font-weight: 700; font-size: 22px; margin-bottom: 10px; }}
    .card-body-text-white {{ color: #DDDDDD !important; font-size: 14px; margin-bottom: 20px; line-height: 1.5; }}

    /* MABADILIKO: Form Backdrop sasa ni NYEUPE SAFHI KABISA (Solid Light Mode Form) */
    [data-testid="stForm"], .stForm {{
        background-color: #FFFFFF !important; 
        border-radius: 20px !important;
        padding: 35px !important; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.6) !important;
        margin-top: 10px;
    }}

    /* High legibility dark headers for the inside of light forms */
    .form-dark-heading {{
        color: #16300B !important; 
        font-weight: 800 !important; 
        font-size: 24px !important;
        margin-bottom: 20px !important;
    }}

    /* Labels Ndani ya Fomu ziwe za Kijani ya Giza ili zisomeke vizuri */
    label[data-testid="stWidgetLabel"] p {{
        color: #16300B !important; font-weight: 700 !important; font-size: 15px !important;
    }}

    /* VIBRANT ELECTRIC GREEN BUTTONS (Sharp Black Text - Hazijabadilika) */
    div.stButton > button {{
        background-color: #00E676 !important; color: #000000 !important;          
        border-radius: 12px !important; border: none !important;
        padding: 12px 24px !important; font-size: 16px !important; font-weight: 700 !important;
        box-shadow: 0 4px 12px rgba(0, 230, 118, 0.3) !important;
        transition: all 0.2s ease-in-out; width: 100%;
    }}
    div.stButton > button:hover {{
        background-color: #00C853 !important; box-shadow: 0 6px 16px rgba(0, 230, 118, 0.5) !important;
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
row_top1, row_top2 = st.columns([4, 1])
with row_top1:
    st.markdown(f'<div class="brand-title">MFUGAJI KWANZA <span class="brand-subtitle">{t["subtitle"]}</span></div>', unsafe_allow_html=True)
with row_top2:
    chosen_lang = st.selectbox("", ["Swahili", "English"], index=0 if lang == "Swahili" else 1, key="app_lang_select")
    if chosen_lang != st.session_state.language:
        st.session_state.language = chosen_lang
        st.rerun()

st.write("<br>", unsafe_allow_html=True)

# ==========================================
# VIEW 1: MAIN DASHBOARD VIEW (PREMIUM BLACK BOARDS)
# ==========================================
if st.session_state.sub_view == "dashboard":
    st.markdown(f'<h2 style="text-align:center; color:white; text-shadow:2px 2px 4px #000; margin-top:0;">{t["welcome"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; color:#E0E0E0; font-size:16px; margin-bottom:20px;">{t["instruction"]}</p>', unsafe_allow_html=True)
    
    col_dash1, _, col_dash2 = st.columns([2, 0.4, 2])
    
    with col_dash1:
        st.markdown(f'<div class="dashboard-card"><div class="white-card-heading">{t["choice_inputs"]}</div><div class="card-body-text-white">{t["desc_inputs"]}</div></div>', unsafe_allow_html=True)
        if st.button(t["choice_inputs"], key="go_to_inputs"):
            st.session_state.sub_view = "inputs"
            st.session_state.profit_calculated = False 
            st.rerun()
            
    with col_dash2:
        st.markdown(f'<div class="dashboard-card"><div class="white-card-heading">{t["choice_withdraw"]}</div><div class="card-body-text-white">{t["desc_withdraw"]}</div></div>', unsafe_allow_html=True)
        if st.button(t["choice_withdraw"], key="go_to_sales"):
            st.session_state.sub_view = "withdraw"
            st.session_state.profit_calculated = False 
            st.rerun()

    # --- LIVE NET PROFIT FINANCIAL CALCULATOR CARD (BLACK BOARD) ---
    st.write("<br>", unsafe_allow_html=True)
    _, center_calc_col, _ = st.columns([0.5, 3, 0.5])
    
    with center_calc_col:
        total_costs = (st.session_state.input_chicks_cost + 
                       st.session_state.input_feed_cost + 
                       st.session_state.input_med_cost + 
                       st.session_state.input_other_cost)
        total_rev = st.session_state.sales_revenue
        
        st.markdown(f"""
        <div class="summary-card-dark">
            <h3 style="color: #00E676; margin-top:0; font-weight:800;">{t['summary_header']}</h3>
            <hr style="border-color: #333333;">
            <p style="color:#FFF; font-size:16px; margin: 8px 0;">
                <b>{t['total_expenses']}</b> <span style="color:#FF5252; font-weight:700;">{total_costs:,.2f} TSH</span> 
                <br><small style="color:#BBB;"><i>{t['record_date']} {st.session_state.inputs_date}</i></small>
            </p>
            <p style="color:#FFF; font-size:16px; margin: 15px 0 8px 0;">
                <b>{t['total_revenue']}</b> <span style="color:#00E676; font-weight:700;">{total_rev:,.2f} TSH</span>
                <br><small style="color:#BBB;"><i>{t['record_date']} {st.session_state.sales_date}</i></small>
            </p>
            <hr style="border-color: #333333;">
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(t["calc_profit_btn"], key="calc_profit_dashboard"):
            st.session_state.profit_calculated = True
            st.rerun()

        if st.session_state.profit_calculated:
            net_profit = total_rev - total_costs
            if net_profit > 0:
                st.success(f"{t['profit_msg']} {net_profit:,.2f} TSH")
            elif net_profit < 0:
                st.error(f"{t['loss_msg']} {abs(net_profit):,.2f} TSH")

# ==========================================
# VIEW 2: DEVELOPMENT & EXPENDITURE VIEW (SOLID WHITE FORM)
# ==========================================
elif st.session_state.sub_view == "inputs":
    _, center_form, _ = st.columns([1, 2, 1])
    with center_form:
        if st.button(t["back_btn"], key="back_from_inputs"):
            st.session_state.sub_view = "dashboard"
            st.rerun()
            
        with st.form(key="inputs_data_capture"):
            st.markdown(f'<div class="form-dark-heading">{t["input_header"]}</div>', unsafe_allow_html=True)
            
            chicks = st.number_input(t["label_chicks"], min_value=0.0, value=st.session_state.input_chicks_cost, step=500.0)
            feeds = st.number_input(t["label_feed"], min_value=0.0, value=st.session_state.input_feed_cost, step=1000.0)
            meds = st.number_input(t["label_med"], min_value=0.0, value=st.session_state.input_med_cost, step=500.0)
            other = st.number_input(t["label_other"], min_value=0.0, value=st.session_state.input_other_cost, step=500.0)
            
            if st.form_submit_button(t["finish_inputs_btn"]):
                st.session_state.input_chicks_cost = chicks
                st.session_state.input_feed_cost = feeds
                st.session_state.input_med_cost = meds
                st.session_state.input_other_cost = other
                
                now = datetime.now()
                st.session_state.inputs_date = now.strftime("%Y-%m-%d %H:%M:%S")
                
                st.session_state.sub_view = "dashboard"
                st.rerun()

# ==========================================
# VIEW 3: BROILER SALES VIEW (SOLID WHITE FORM)
# ==========================================
elif st.session_state.sub_view == "withdraw":
    _, center_form, _ = st.columns([1, 2, 1])
    with center_form:
        if st.button(t["back_btn"], key="back_from_sales"):
            st.session_state.sub_view = "dashboard"
            st.rerun()
            
        with st.form(key="sales_data_capture"):
            st.markdown(f'<div class="form-dark-heading">{t["sales_header"]}</div>', unsafe_allow_html=True)
            
            qty = st.number_input(t["label_qty"], min_value=0, value=st.session_state.sales_qty, step=1)
            price = st.number_input(t["label_price"], min_value=0.0, value=6500.0 if st.session_state.sales_price == 0.0 else st.session_state.sales_price, step=500.0)
            
            if st.form_submit_button(t["finish_sales_btn"]):
                st.session_state.sales_qty = qty
                st.session_state.sales_price = price
                st.session_state.sales_revenue = float(qty * price)
                
                now = datetime.now()
                st.session_state.sales_date = now.strftime("%Y-%m-%d %H:%M:%S")
                
                st.session_state.sub_view = "dashboard"
                st.rerun()
