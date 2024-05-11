import streamlit as st
import requests

st.title('Weather API Integration')

city = st.text_input('Enter your city:')
api_key = 'your_api_key_here'  # Replace with your actual API key

if city:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data:
        st.write('Temperature:', weather_data['main']['temp'])
        st.write('Weather:', weather_data['weather'][0]['description'])
        st.write('Wind Speed:', weather_data['wind']['speed'], 'm/s')
