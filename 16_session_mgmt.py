import streamlit as st

st.title('Session State Management')

# Define a key for session state
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1

st.write('Count:', st.session_state.count)
