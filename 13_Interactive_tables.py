import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np

st.title('Interactive Tables with Streamlit AgGrid')

# Create a sample DataFrame
data = pd.DataFrame(
    np.random.rand(10, 5),
    columns=['A', 'B', 'C', 'D', 'E'])

# Display interactive grid
AgGrid(data)
