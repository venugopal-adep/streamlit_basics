import streamlit as st

# Define a function for each page
def page_one():
    st.title('Page One')
    st.write('Welcome to page one!')

def page_two():
    st.title('Page Two')
    st.write('Welcome to page two!')

# Setup sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Choose a page:', ['Page One', 'Page Two'])

if page == 'Page One':
    page_one()
elif page == 'Page Two':
    page_two()
