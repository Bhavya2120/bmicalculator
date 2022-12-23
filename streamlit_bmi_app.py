import streamlit as st
import numpy as np
st.write("""
#BMI Calculator""")
st.header('User Input Parameters')
height=1.00
weight=40.00
height=st.number_input('Enter the height in metres')
weight=st.number_input('Enter the weight in kilograms')
#Find a way to accept different input - cm/feet instead of metres
height=height**2
bmi=weight/height
st.header('BMI is')
st.write(bmi)
