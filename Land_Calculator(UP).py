import streamlit as st

# --- पेज सेटिंग ---
st.set_page_config(
    page_title="Land Calculator",
    page_icon="🌾",
    layout="centered"
)

# --- CUSTOM CSS (सजावट के लिए कोड) ---
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
st.title
