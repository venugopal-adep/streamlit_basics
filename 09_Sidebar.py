import streamlit as st

st.title('Using the Sidebar')

option = st.sidebar.selectbox(
    'Select a number:',
    [10, 20, 30, 40, 50])

st.write('The selected number is:', option)