import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import numpy as np

st.write(f"## Disease Prediction Application")
st.write("Auther: Pavan Sai Kundum")

heart_disease_model = pickle.load(open("C:\Users\pavan\OneDrive\Desktop\ICBP\heart_disease_model1.sav", "rb"))

col1, col2 = st.columns(2)

with st.sidebar:
    selected = option_menu("Choose the Disease", ["Haert Disease Prediction", "Diabetes Prediction"])

if selected == "Haert Disease Prediction":
    st.write(f"## Heart Disease Prediction")
    
    with col1:
        age = st.text_input("Type your age")
        sex = st.text_input("Type your sex")
        cp = st.text_input("Type your cp")
        testbps = st.text_input("Type your testbps")
        chol = st.text_input("Type your chol")
        fbs = st.text_input("Type your fbs")
        restecg = st.text_input("Type your restecg")
    with col2:
        thalach = st.text_input("Type your thalach")
        exang = st.text_input("Type your exang")
        oldpeak = st.text_input("Type your oldpeak")
        slope = st.text_input("Type your slope")
        ca = st.text_input("Type your ca")
        thal = st.text_input("Type your thal")


    if st.button("Predict"):
        data = [[age, sex, cp, testbps, chol, fbs, restecg,thalach, exang, oldpeak, slope, ca, thal]]
        prediction = heart_disease_model.predict(data)
        st.write(f"## Prediction: {prediction}")

if selected == "Diabetes Prediction":
    st.write(f"## Diabetes Prediction")