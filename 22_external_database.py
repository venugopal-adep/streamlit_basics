import streamlit as st
import sqlite3
import pandas as pd

st.title('Database Example')

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2022-01-01','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Perform a query
c.execute('SELECT * FROM stocks')
rows = c.fetchall()

st.write('Data from database:', pd.DataFrame(rows, columns=['Date', 'Transaction', 'Symbol', 'Quantity', 'Price']))

conn.close()
