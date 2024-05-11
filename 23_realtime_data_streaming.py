import streamlit as st
import time
import random

st.title('Real-Time Data Streaming')

data = []
chart = st.line_chart(data)

for _ in range(100):
    data.append(random.random())
    chart.add_rows([data[-1]])
    time.sleep(0.1)
