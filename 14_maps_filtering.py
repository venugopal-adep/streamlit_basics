import streamlit as st
import pandas as pd

st.title('Interactive Map Filter')

# Data preparation
data = pd.DataFrame({
    'lat': [28.6139, 19.0760, 12.9716, 17.3850, 22.5726],
    'lon': [77.2090, 72.8777, 77.5946, 78.4867, 88.3639],
    'name': ['Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata']
})

selected_city = st.selectbox('Select a city to display:', data['name'])
filtered_data = data[data['name'] == selected_city]

st.map(filtered_data)
