import streamlit as st

st.title('Dynamic Form Input')

with st.form(key='my_form'):
    username = st.text_input(label='Enter your username')
    password = st.text_input(label='Enter your password', type='password')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write('Hello, ', username)
