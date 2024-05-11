import streamlit as st

st.title('Advanced Interactivity with Callbacks')

# Simple counter using callback
def increment_counter():
    st.session_state.counter += 1

def decrement_counter():
    st.session_state.counter -= 1

if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.button('Increment', on_click=increment_counter)
st.button('Decrement', on_click=decrement_counter)

st.write('Counter:', st.session_state.counter)
