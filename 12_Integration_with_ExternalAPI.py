import streamlit as st
import requests

st.title('External API Integration')

url = "https://api.agify.io?name=michael"
if st.button('Get Age Prediction'):
    response = requests.get(url)
    age_data = response.json()
    st.write('Predicted age for Michael:', age_data['age'])