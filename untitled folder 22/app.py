import streamlit as st
import numpy as np
import joblib

model = joblib.load("lr_model.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write("This app allows you to estimate the price of a laptop. Just enter the brand, processor speed, RAM size, storage capacity, screen size, and weight, then click the calculation button to get your price estimate")

st.divider()

brand_mapping = {"Asus": 0, "Acer": 1, "Lenovo": 2, "HP": 3,"Dell":4}

brand = st.selectbox("Select Brand", options=list(brand_mapping.keys()))

#brand = st.number_input("Brand", value = 0, step= 1)
processor_speed = st.number_input("Enter processor speed (GHz)", value = 2.5, step= 0.50)
ram_size = st.number_input("Enter ram size (GB)", value = 16, step= 8)
storage_capacity = st.number_input("Enter storage capacity (GB)", value= 512, step=256)
screen_size = st.number_input("Enter screen size (inches)", value= 15.6, step=0.50)
weight = st.number_input("Enter weight (kg)", value= 2.5, step=0.50)

X =['Brand','Processor_Speed','RAM_Size','Storage_Capacity','Screen_Size','Weight']

st.divider()

prediction = st.button("Price Estimation Button!")

st.divider()

if prediction:

       brand_numeric = brand_mapping[brand]

       input_data = np.array([brand_numeric, processor_speed, ram_size, storage_capacity, screen_size, weight]).reshape(1, -1)
       
       st.balloons()
       
       x1 = np.array(X)
       prediction = model.predict([x1])[0]

       st.write(f"Price Estimation for the laptop is **${prediction:,.2f}**")


else:
       st.write("Please click the button to get the price prediction")