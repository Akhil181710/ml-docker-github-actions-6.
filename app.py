
import streamlit as st

st.title("House Price Prediction - Version 2")

st.success("Welcome to the Updated Application!")

st.write("Application successfully updated using Direct Deployment.")

area = st.number_input("Enter house area (sq. ft.)", min_value=100)

bedrooms = st.number_input("Enter number of bedrooms", min_value=1)

if st.button("Predict Price"):
    price = area * 3000 + bedrooms * 50000
    st.success(f"Estimated House Price: ₹{price:,.2f}")

st.info("Version 2 - Updated Deployment")
