import streamlit as st

st.title('Layouts with Columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("This is column 1")

with col2:
    st.header("Column 2")
    st.write("This is column 2")

with col3:
    st.header("Column 3")
    st.write("Here's column 3 where you can add more content.")