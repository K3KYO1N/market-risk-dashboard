import yfinance as yf
import pandas as pd

def fetch_data(ticker, start, end):
  df = yf.download(ticker, start=start, end=end)
  df.to_csv(f"data/{ticker}.csv")
  return df
