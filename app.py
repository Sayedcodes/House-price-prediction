import streamlit as st
import pandas as pd
import pickle

# Load pipeline (preprocessor + model)
model = pickle.load(open("pipe.pkl", "rb"))

st.title("🏠 House Price Prediction")

# Take input from user
location = st.text_input("Enter location: ")
area_type = st.text_input("Enter area type: ")
total_sqft = st.number_input("Enter total square feet: ", min_value=0.0)
bath = st.number_input("Enter number of bathrooms: ", min_value=0)
bhk = st.number_input("Enter number of bedrooms (BHK): ", min_value=0)

# Create DataFrame
user_input = pd.DataFrame([[location, area_type, total_sqft, bath, bhk]],
                          columns=['location', 'area_type', 'total_sqft', 'bath', 'bhk'])

if st.button("Predict Price"):
    predicted_price = model.predict(user_input)
    st.success(f"The predicted price is: {predicted_price[0]:.2f} Lakhs")