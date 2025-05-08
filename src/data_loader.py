# Downloads stock prices from Yahoo using yfinance. Saves them to csv file. Return as data frame.
import yfinance as yf
import pandas as pd

def fetch_data(ticker, start, end):
  ticker_obj = yf.Ticker(ticker)
  df = ticker_obj.history(start=start, end=end)
  print(df.columns)
  df.to_csv(f"data/{ticker}.csv")
  return df
  # df = yf.download(ticker, start=start, end=end)
  # df.to_csv(f"data/{ticker}.csv")
  # return df
