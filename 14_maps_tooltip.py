import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'lat': [28.6139, 19.0760, 12.9716, 17.3850],
    'lon': [77.2090, 72.8777, 77.5946, 78.4867],
    'name': ['Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad']
})

# Tooltips are not directly supported in st.map, but we can use st.pydeck_chart for more customization
import pydeck as pdk

layer = pdk.Layer(
    'ScatterplotLayer',
    data,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=100000,
    pickable=True
)

view_state = pdk.ViewState(latitude=20, longitude=77, zoom=4)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"}))
