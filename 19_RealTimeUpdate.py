import streamlit as st
import requests
import time

st.title('Real-Time External Updates')

def get_latest_crypto_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    return data['bpi']['USD']['rate']

latest_price = st.empty()

while True:
    price = get_latest_crypto_price()
    latest_price.text(f"The current price of Bitcoin is: ${price}")
    time.sleep(60)  # Update every minute
