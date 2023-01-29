import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Google!

""")

tickerSymbol = 'GOOGL'

# to get data
tickerData = yf.Ticker(tickerSymbol)

# to get historical prices
# save in the data frame
# data frame context: Open, High, Low, Close, Volume, Dividends, Stock & Splits
tickerDf = tickerData.history(period='1d', start='2010-1-31', end='2022-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

# To get streamlit url in terminal: python -m streamlit run stock_price.py