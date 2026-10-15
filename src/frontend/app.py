import streamlit as st

st.set_page_config(
    page_title="AugurHealth",
    page_icon="🩺",
    layout="centered"
)

st.title("🧠 AugurHealth - Multi-Disease Predictor")

st.write(
    """
Use the left sidebar to navigate:
- 🩺 Diabetes Risk Predictor
- ❤️ Heart Disease Risk Predictor
"""
)

st.info("Make sure the FastAPI backend is running before using predictions.")