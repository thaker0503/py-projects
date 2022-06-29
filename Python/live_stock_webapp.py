import streamlit as st
import yfinance as finance


def get_ticker(name):
	company = finance.Ticker(name) # google
	return company


# Project Details
st.title("Live Stock Details.")
st.header("A Basic Data Science Web Application")
st.sidebar.header("Yatharth Thaker \n Python Web App to see live stock values.")

company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")

# fetches the data: Open, Close, High, Low and Volume
google = finance.download("GOOGL", start="2022-06-26", end="2022-06-26")
microsoft = finance.download("MSFT", start="2022-06-26", end="2022-06-26")

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="5d")
data2 = company2.history(period="5d")

# markdown syntax
st.write("""
### Google
""")

# detailed summary on Google
# st.write(company1.info['longBusinessSummary'])
st.write(google)

# plots the graph
st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(microsoft)
# st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)
