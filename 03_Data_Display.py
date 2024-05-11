import streamlit as st
import pandas as pd
import numpy as np

# Create a random DataFrame
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.title('Displaying Data')
st.write('Here is a random DataFrame:')
st.write(data)
