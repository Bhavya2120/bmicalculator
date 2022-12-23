import streamlit as st
import numpy as np
st.write("""
#BMI Calculator""")
st.header('User Input Parameters')
height=st.number_input('Enter the height in metres',value=1.00)
weight=st.number_input('Enter the weight in kilograms',value=40)
#Find a way to accept different input - cm/feet instead of metres
height=height**2
bmi=weight/height
st.header('BMI is')
st.write(bmi)
