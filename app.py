import streamlit as st
import pickle
import numpy as np

# Model load
model = pickle.load(open('house_model.pkl', 'rb'))

st.title("House Price Prediction App")

# User inputs
area = st.number_input("Area (sq ft)", min_value=1000, max_value=15000, value=4000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=6, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=2)
stories = st.number_input("Stories", min_value=1, max_value=4, value=2)

mainroad = st.selectbox("Mainroad?", ("yes", "no"))
guestroom = st.selectbox("Guestroom?", ("yes", "no"))
basement = st.selectbox("Basement?", ("yes", "no"))
hotwaterheating = st.selectbox("Hot Water Heating?", ("yes", "no"))
airconditioning = st.selectbox("Airconditioning?", ("yes", "no"))
parking = st.number_input("Parking", min_value=0, max_value=3, value=2)
prefarea = st.selectbox("Preferred Area?", ("yes", "no"))
furnishingstatus = st.selectbox("Furnishing Status", ("furnished", "semi-furnished", "unfurnished"))

# Convert to numbers
mainroad_val = 1 if mainroad == "yes" else 0
guestroom_val = 1 if guestroom == "yes" else 0
basement_val = 1 if basement == "yes" else 0
hotwaterheating_val = 1 if hotwaterheating == "yes" else 0
airconditioning_val = 1 if airconditioning == "yes" else 0
prefarea_val = 1 if prefarea == "yes" else 0

furnished = 1 if furnishingstatus == "furnished" else 0
semi_furnished = 1 if furnishingstatus == "semi-furnished" else 0

# Input array (order match notebook se: area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnished, semi_furnished)
input_features = np.array([[area, bedrooms, bathrooms, stories, mainroad_val, guestroom_val, basement_val,
                            hotwaterheating_val, airconditioning_val, parking, prefarea_val, furnished, semi_furnished]])

if st.button("Predict House Price"):
    prediction = model.predict(input_features)
    st.success(f"Estimated House Price: PKR {prediction[0]:,.0f} /-")