import streamlit as st
import time

st.title('Progress Bar and Spinners Example')

# Progress bar
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i+1)

st.success('Load complete!')

# Spinner
with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')