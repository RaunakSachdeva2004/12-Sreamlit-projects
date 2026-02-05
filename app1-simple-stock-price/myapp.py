import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
        # Simple Stock Price App
        
        Shown are the stock **closing price** and **volume** of Google!!
""")

tickerSymbol = "GOOGL"


tickerData = yf.Ticker(tickerSymbol)
start = '2020-01-01'
end = '2023-01-01'
tickerDf = tickerData.history(period= '2mo')

## OR

# tickerDf = tickerData.history(
#     start='2020-01-01',
#     end='2023-01-01'
# )

st.line_chart(tickerDf['Close'])
st.line_chart(tickerDf['Volume'])