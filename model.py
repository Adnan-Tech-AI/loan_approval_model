import streamlit as st
import joblib



st.markdown("<h1 style='text-align:center;'>Loan Approval Prediction</h1>",unsafe_allow_html=True)

st.markdown("<i><h3 style='text-align:center;color:red'>To check whether a person is eligible for a loan<h3><i>",unsafe_allow_html=True)

dependents = st.number_input("Enter No.of Dependents",min_value=0)

education = st.selectbox("Select Your Education",["Graduate","Non Graduate"])

if education=="Graduate":
    education = 1
else: 
    education = 0 

self_employed = st.radio("Are you self employed?",["Yes","No"],horizontal=True)

if self_employed == "Yes":
    self_employed = 1
else:
    self_employed = 0

income = st.number_input("Enter your annual income",min_value=0)

loan_amount = st.number_input("Enter your loan amount",min_value=0)

loan_term = st.number_input("Enter your loan term",min_value=0)

cibil_score = st.slider("Select your cibil score",min_value = 300,max_value=700)

if st.button("Predict"):
    model = joblib.load("loan_model.h5")
    prediction= model.predict([[dependents,education,self_employed,income,loan_amount,loan_term,cibil_score]])
    st.success(prediction)