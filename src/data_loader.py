# Downloads stock prices from Yahoo using yfinance. Saves them to csv file. Return as data frame.
import yfinance as yf
import pandas as pd

def fetch_data(ticker, start, end):
  df = yf.download(ticker, start=start, end=end)
  df.to_csv(f"data/{ticker}.csv")
  return df
