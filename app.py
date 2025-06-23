import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("stress_predictor_model.pkl")

# App title
st.title("🧠 Stress Level Predictor")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
sleep_duration = st.slider("Sleep Duration (in hours)", 0.0, 12.0, 6.0)
quality_of_sleep = st.slider("Quality of Sleep (1-10)", 1, 10, 7)
heart_rate = st.number_input("Heart Rate (BPM)", 40, 200, 72)
bmi_simple = st.selectbox("BMI Category", ["Normal", "High"])

# Convert input
gender_val = 0 if gender == "Male" else 1
bmi_val = 0 if bmi_simple == "Normal" else 1
input_data = np.array([[gender_val, sleep_duration, quality_of_sleep, heart_rate, bmi_val]])

# Prediction
if st.button("Predict Stress Level"):
    pred = model.predict(input_data)[0]
    levels = {0: "🟢 Low", 1: "🟡 Moderate", 2: "🔴 High"}
    st.success(f"Predicted Stress Level: {levels[pred]}")

    # Optional: Video recommendation
    videos = {
        0: "https://www.youtube.com/embed/hlWiI4xVXKY",  # calming wellness
        1: "https://www.youtube.com/embed/inpok4MKVLM",

        2: "https://www.youtube.com/embed/MIr3RsUWrdo"   # meditation
    }
    st.subheader("🎥 Recommended Video:")
    st.video(videos[pred])
