import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'lat': [28.6139, 19.0760, 12.9716, 17.3850],
    'lon': [77.2090, 72.8777, 77.5946, 78.4867],
    'name': ['Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad']
})

for index, city in data.iterrows():
    st.write(f"{city['name']}: {city['lat']}, {city['lon']}")

st.map(data)
