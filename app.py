import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained pipeline
model = joblib.load("best_taxi_pipeline.joblib")

st.title("🚖 Taxi Fare Predictor")
st.write("Enter trip details:")

# -------------------------------
# 1️⃣ User Inputs
# -------------------------------
passenger_count = st.number_input("Passenger count", 1, 6, 1)
pickup_hour = st.slider("Pickup hour (0-23)", 0, 23, 12)
pickup_dayofweek = st.slider("Pickup day of week (0=Mon)", 0, 6, 3)
trip_distance = st.number_input("Trip distance (miles)", 0.0, 50.0, 2.5)
trip_duration = st.number_input("Trip duration (minutes)", 0.0, 180.0, 15.0)

VendorID = st.selectbox("VendorID", ["1", "2"])
RatecodeID = st.selectbox("RatecodeID", ["1", "2", "3", "4", "5", "6"])
store_flag = st.selectbox("store_and_fwd_flag", ["N", "Y"])
payment_type = st.selectbox("payment_type", ["CRD", "CSH"])
pickup_am_pm = "AM" if pickup_hour < 12 else "PM"
pickup_is_weekend = 1 if pickup_dayofweek in [5, 6] else 0
pickup_is_night = 1 if (pickup_hour >= 22 or pickup_hour < 6) else 0

# -------------------------------
# 2️⃣ Map categorical columns to numeric
# -------------------------------
VendorID_num = {"1": 1, "2": 2}[VendorID]
RatecodeID_num = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6}[RatecodeID]
store_flag_num = {"N":0, "Y":1}[store_flag]
payment_type_num = {"CRD":0, "CSH":1}[payment_type]
pickup_am_pm_num = {"AM":0, "PM":1}[pickup_am_pm]

# -------------------------------
# 3️⃣ Prepare input DataFrame (all numeric)
# -------------------------------
row = pd.DataFrame([{
    "passenger_count": float(passenger_count),
    "trip_distance_hav": float(trip_distance),
    "trip_duration_mins": float(trip_duration),
    "pickup_hour": int(pickup_hour),
    "pickup_dayofweek": int(pickup_dayofweek),
    "pickup_is_weekend": int(pickup_is_weekend),
    "pickup_is_night": int(pickup_is_night),
    "pickup_am_pm": int(pickup_am_pm_num),
    "VendorID": int(VendorID_num),
    "RatecodeID": int(RatecodeID_num),
    "store_and_fwd_flag": int(store_flag_num),
    "payment_type": int(payment_type_num)
}])

# -------------------------------
# 4️⃣ Predict Fare
# -------------------------------
if st.button("Predict Fare"):
    pred = model.predict(row)[0]
    st.success(f"Predicted total fare: ${pred:.2f}")
