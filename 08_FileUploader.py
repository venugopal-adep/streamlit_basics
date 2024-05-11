import streamlit as st

st.title('File Uploader Example')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Assuming the uploaded file is a CSV
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write(df)