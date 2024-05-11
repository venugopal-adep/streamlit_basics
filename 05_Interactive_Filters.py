import streamlit as st
import pandas as pd
import numpy as np

# Create a random DataFrame
data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=list('AB')
)

st.title('Interactive Filters')
st.write('Use the slider to filter the dataframe.')

# Slider for filtering data
x = st.slider('Select a range of values', 0, 100, (10, 90))
filtered_data = data[(data['A'] > x[0]) & (data['A'] < x[1])]
st.write(filtered_data)