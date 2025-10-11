import streamlit as st
import numpy as np
import joblib
import pandas as pd

# --------------------
# Load Model
# --------------------
@st.cache_resource
def load_model():
    return joblib.load("random_forest_model.pkl")

model = load_model()

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Gold Price Predictor",
    page_icon="🪙",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --------------------
# Dark Theme CSS
# --------------------
st.markdown("""
<style>
body {
    background-color: #1E1E2F;
    color: white;
}
.stSlider > div[data-baseweb="slider"] > div > div {
    background: #6B5B95 !important;
}
.css-1aumxhk {
    background-color: #2E2E3F !important;
}
.css-1d391kg {
    background-color: #2E2E3F !important;
}
.st-bx {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🌌 Gold Price Prediction")
st.markdown("Adjust the inputs below to predict gold price using Random Forest model.")

# --------------------
# Sidebar / Inputs
# --------------------
st.sidebar.header("Input Features")

# Function to get input values
def get_inputs():
    SP_close = st.sidebar.slider("S&P 500 Closing Price", float(3000), float(5000), 4000.0)
    DJ_close = st.sidebar.slider("Dow Jones Closing Price", float(25000), float(35000), 30000.0)
    USDI_Price = st.sidebar.slider("U.S. Dollar Index", float(90), float(120), 100.0)
    EU_Price = st.sidebar.slider("Euro Price Level", float(70), float(90), 80.0)
    PLT_Price = st.sidebar.slider("Platinum Price", float(500), float(1500), 1000.0)
    USO_Close = st.sidebar.slider("Crude Oil ETF Price", float(30), float(80), 50.0)
    Volume = st.sidebar.slider("Gold Volume Traded", int(10000), int(50000000), 1000000)

    data = {
        "SP_close": SP_close,
        "DJ_close": DJ_close,
        "USDI_Price": USDI_Price,
        "EU_Price": EU_Price,
        "PLT_Price": PLT_Price,
        "USO_Close": USO_Close,
        "Volume": Volume
    }
    return pd.DataFrame([data])

# Get input values as dataframe
input_df = get_inputs()

# --------------------
# Prediction
# --------------------
if st.button("🔮 Predict Gold Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Gold Price: ${prediction:,.2f}")

# Optional: show user input table
with st.expander("Show Input Values"):
    st.dataframe(input_df.style.set_properties(**{'background-color': '#2E2E3F',
                                                   'color': 'white',
                                                   'border-color': 'white'}))

st.markdown("<br><br>Created by **Siddiqa Ali**", unsafe_allow_html=True)