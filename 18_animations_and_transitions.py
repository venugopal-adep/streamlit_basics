import streamlit as st
import numpy as np
import time

st.title('Animation Example')

# Generate some random data
data = np.random.randn(10, 2)

progress_bar = st.progress(0)
chart = st.line_chart(data)

for i in range(1, 101):
    # Update progress bar
    progress_bar.progress(i)
    new_row = np.random.randn(1, 2)
    # Update chart with new row of data
    chart.add_rows(new_row)
    time.sleep(0.05)

st.button('Re-run')
