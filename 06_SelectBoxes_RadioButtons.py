import streamlit as st

st.title('Interactive Input: Selectboxes and Radio Buttons')

option = st.selectbox(
    'Choose a number:',
    [1, 2, 3, 4, 5])

st.write('You selected:', option)

choice = st.radio(
    'Choose your favorite color:',
    ['Red', 'Blue', 'Green'])

st.write('Your favorite color is:', choice)