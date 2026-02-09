import streamlit as st

# --- पेज सेटिंग ---
st.set_page_config(
    page_title="Land Calculator",
    page_icon="🌾",
    layout="centered"
)

# --- CUSTOM CSS (नई और बेहतर सजावट) ---
st.markdown("""
    <style>
    /* 1. मुख्य बैकग्राउंड (Main Background - Colorful) */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(to bottom right, #e8f5e9, #fffde7);
        color: #1b5e20;
    }

    /* 2. साइडबार का बैकग्राउंड (Sidebar - Light Green) */
    [data-testid="stSidebar"] {
        background-color: #f1f8e9;
        border-right: 2px solid #a5d6a7;
    }
    
    /* 3. हेडर और टाइटल (Header Styling) */
    h1 {
        color: #1b5e20;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        text-shadow: 2px 2px 4px #a5d6a7;
    }
    
    /* 4. सब-टेक्स्ट (Sub-text) */
    .stMarkdown p {
        font-size: 18px;
        color: #2e7d32;
    }
    
    /* 5. इनपुट बॉक्स (Input Fields) */
    .stNumberInput > div > div > input {
        background-color: #ffffff;
        border: 1px solid #81c784;
        color: #1b5e20;
    }
    
    /* 6. बटन (Button Styling) */
    div.stButton > button {
        background-color: #2e7d32;
        color: white;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        border: 2px solid #1b5e20;
    }
    div.stButton > button:hover {
        background-color: #43a047;
        color: white;
        border-color: #66bb6a;
    }

    /* 7. रिजल्ट बॉक्स (Result Box) */
    .result-box {
        background-color: #dcedc8; /* गहरा हरा बॉक्स */
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #33691e;
        text-align: center;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .result-title {
        color: #1b5e20;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* 8. लेबल्स (Labels) */
    label {
        color: #1b5e20 !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- टाइटल ---
st.title("🌾 जमीन नापने का कैलकुलेटर")
st.markdown("<h3 style='text-align: center; color: #558b2f;'>📍 👨‍🌾उत्तर प्रदेश (सरकारी पक्का बीघा)</h3>", unsafe_allow_html=True)
st.write("---")

# --- साइडबार (Menu) ---
st.sidebar.markdown("### 🛠️ सेटिंग्स")
option = st.sidebar.radio(
    "नापने का तरीका चुनें:",
    ("फीट (Feet) से नापें", "लाठा (Latha) से नापें","मीटर (Meter) से नापें")
)
st.sidebar.info("ℹ️ **पैमाना:**\n\n- 1 लाठा = 99 इंच\n- 1 बीघा = 20 बिस्वा\n- 1 बिस्वा = 20 धुर")

# --- फंक्शन: रिजल्ट दिखाने के लिए (Stylish Dashboard) ---
def show_stylish_result(bigha, biswa, dhur, total_area, unit_name):
    st.markdown("---")
    
    # 1. कुल क्षेत्रफल का बड़ा बॉक्स
    st.markdown(f"""
        <div class="result-box">
            <div class="result-title">✅ कुल क्षेत्रफल</div>
            <div style="font-size: 30px; color: #1b5e20; font-weight: bold;">
                {total_area:.2f} <span style="font-size: 20px;">{unit_name}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. बीघा, बिस्वा, धुर के लिए मेट्रिक्स (Dashboard Style)
    st.markdown("<h4 style='text-align: center; color: #1b5e20;'>🎉 आपका पैमाइश रिजल्ट:</h4>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🌳 बीघा (Bigha)", value=f"{bigha}")
    with col2:
        st.metric(label="🌱 बिस्वा (Biswa)", value=f"{biswa}")
    with col3:
        st.metric(label="📏 धुर (Dhur)", value=f"{dhur:.2f}")

# ==========================================
# 1. फीट (Feet) कैलकुलेटर
# ==========================================
if option == "फीट (Feet) से नापें":
    st.header("📏 फीट (Feet) मोड")
    st.markdown("खेत की चारों भुजाओं (Sides) की लंबाई **फीट** में डालें:")

    col1, col2 = st.columns(2)
    with col1:
        l1 = st.number_input("पूर्व (East) की लंबाई - फीट में", min_value=0.0, format="%.2f")
        w1 = st.number_input("उत्तर (North) की चौड़ाई - फीट में", min_value=0.0, format="%.2f")
    with col2:
        l2 = st.number_input("पश्चिम (West) की लंबाई - फीट में", min_value=0.0, format="%.2f")
        w2 = st.number_input("दक्षिण (South) की चौड़ाई - फीट में", min_value=0.0, format="%.2f")

    if st.button("कैलकुलेट करें (Calculate Feet)"):
        if l1 > 0 and l2 > 0 and w1 > 0 and w2 > 0:
            avg_len = (l1 + l2) / 2
            avg_wid = (w1 + w2) / 2
            total_sq_ft = avg_len * avg_wid

            # उत्तर प्रदेश स्टैंडर्ड (Feet)
            bigha = int(total_sq_ft // 27225)
            rem = total_sq_ft % 27225
            biswa = int(rem // 1361.25)
            rem = rem % 1361.25
            dhur = rem / 68.0625

            show_stylish_result(bigha, biswa, dhur, total_sq_ft, "वर्ग फीट")
        else:
            st.error("❌ कृपया नंबर सही से भरें (0 से ज्यादा)")

# ==========================================
# 2. लाठा (Latha) कैलकुलेटर
# ==========================================
elif option == "लाठा (Latha) से नापें":
    st.header("🎋 लाठा (Latha) मोड")
    st.markdown("खेत की चारों भुजाओं की लंबाई **लाठा** में डालें:")

    col1, col2 = st.columns(2)
    with col1:
        l1 = st.number_input("पूर्व (East) की लंबाई - लाठा में", min_value=0.0, format="%.2f")
        w1 = st.number_input("उत्तर (North) की चौड़ाई - लाठा में", min_value=0.0, format="%.2f")
    with col2:
        l2 = st.number_input("पश्चिम (West) की लंबाई - लाठा में", min_value=0.0, format="%.2f")
        w2 = st.number_input("दक्षिण (South) की चौड़ाई - लाठा में", min_value=0.0, format="%.2f")

    if st.button("कैलकुलेट करें (Calculate Latha)"):
        if l1 > 0 and l2 > 0 and w1 > 0 and w2 > 0:
            avg_len = (l1 + l2) / 2
            avg_wid = (w1 + w2) / 2
            total_sq_latha = avg_len * avg_wid

            #  उत्तर प्रदेश स्टैंडर्ड (Latha)
            bigha = int(total_sq_latha // 400)
            rem = total_sq_latha % 400
            biswa = int(rem // 20)
            dhur = rem % 20

            show_stylish_result(bigha, biswa, dhur, total_sq_latha, "वर्ग लाठा")
        else:
            st.error("❌ कृपया नंबर सही से भरें (0 से ज्यादा)")

# ==========================================
# 3. मीटर (Meter) कैलकुलेटर
# ==========================================
elif option == "मीटर (Meter) से नापें":
    st.header("📏 मीटर (Meter) मोड")

    col1, col2 = st.columns(2)
    with col1:
        l1 = st.number_input("पूर्व (East) की लंबाई - मीटर में", min_value=0.0, format="%.2f")
        w1 = st.number_input("उत्तर (North) की चौड़ाई - मीटर में", min_value=0.0, format="%.2f")
    with col2:
        l2 = st.number_input("पश्चिम (West) की लंबाई - मीटर में", min_value=0.0, format="%.2f")
        w2 = st.number_input("दक्षिण (South) की चौड़ाई - मीटर में", min_value=0.0, format="%.2f")

    if st.button("कैलकुलेट करें (Calculate Meter)"):
        if l1 > 0 and l2 > 0 and w1 > 0 and w2 > 0:
            avg_len = (l1 + l2) / 2
            avg_wid = (w1 + w2) / 2
            total_sq_meter = avg_len * avg_wid

            # --- उत्तर प्रदेश स्टैंडर्ड (Meter) ---
            # 1 Bigha = 2529.3 Sq Meter
            # 1 Biswa = 126.46 Sq Meter
            
            bigha = int(total_sq_meter // 2529.3)
            rem = total_sq_meter % 2529.3
            biswa = int(rem // 126.46)
            rem = rem % 126.46
            dhur = rem / 6.323

            show_stylish_result(bigha, biswa, dhur, total_sq_meter, "वर्ग मीटर")
        else:
            st.error("❌ कृपया नंबर सही से भरें")

# फुटर
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Developed by AKS | Special for Uttar Pradesh Region 🌾</p>", unsafe_allow_html=True)


