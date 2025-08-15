import streamlit as st
import numpy as np
import joblib

model=joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write("With this app after using the calculation button when you entered the values of processor speed,ram size and storage capacity you can get a price estimation for the laptop you want.")

st.divider()

processor_speed=st.number_input("Enter Processor Speed",value=2.5,step=0.50)
ram_size=st.number_input("Enter Ram Size",value=16,step=8)
storage_capacity=st.number_input("Enter Storage Capacity",value=512,step=256)

x=[processor_speed,ram_size,storage_capacity]

st.divider()

prediction=st.button("Price Estimatin button!")

st.divider()

if prediction:
    st.balloons()

    x1=np.array(x)

    prediction=model.predict([x1])[0]

    st.write(f"Price estimation for the laptop is {prediction:,.2f}")

else:
    st.write("Pleas use the button for getting a prediction")