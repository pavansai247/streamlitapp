import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import numpy as np

st.write(f"## Disease Prediction Application")
st.write("Auther: Pavan Sai Kundum")

heart_disease_model = pickle.load(open("heart_disease_model1.sav", "rb"))

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

if selected == "Parkinsons Preciction":
    st.write(f"## Parkinsons Preciction")
    # Take User inputs
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('Fo(Hz)')
        RAP = st.text_input('RAP')
        APQ3 = st.text_input('APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('Fhi(Hz)')
        PPQ = st.text_input('PPQ')
        APQ5 = st.text_input('APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')

    with col3:
        flo = st.text_input('Flo(Hz)')
        DDP = st.text_input('DDP')
        APQ = st.text_input('APQ')
        DFA = st.text_input('DFA')

    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
        Shimmer = st.text_input('Shimmer')
        DDA = st.text_input('DDA')
        spread1 = st.text_input('spread1')

    with col5:
        Jitter_Abs = st.text_input('Jitter(Abs)')
        Shimmer_dB = st.text_input('Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')
    
    if st.button("Predict"):
        data = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        data_array = np.array(data, dtype=float).reshape(1,-1)
        prediction = parkinsons_model.predict(data_array)
        st.write(f"## Prediction: {prediction}")