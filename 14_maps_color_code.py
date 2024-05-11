import streamlit as st
import pandas as pd
import pydeck as pdk

# Data
data = pd.DataFrame({
    'lat': [28.7041, 22.2587, 15.9129, 31.1471],
    'lon': [77.1025, 71.1924, 79.7400, 75.3412],
    'category': ['Historical', 'Cultural', 'Beach', 'Religious']
})

# Color mapping
color_map = {'Historical': [255, 165, 0, 140], 'Cultural': [255, 0, 0, 140], 'Beach': [0, 0, 255, 140], 'Religious': [0, 255, 0, 140]}
data['color'] = data['category'].map(color_map)

# Map
layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position="[lon, lat]",
    get_color="color",
    get_radius=50000,
    pickable=True
)

view_state = pdk.ViewState(latitude=22, longitude=79, zoom=4)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{category}"}))
