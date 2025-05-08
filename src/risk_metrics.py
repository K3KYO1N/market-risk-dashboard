import numpy as np

def calculate_daily_returns(df):
  return df['Adj Close'].pct_change().dropna()
  # Adjusted close price adjusted for splits and dividends and/or capital gain distributions.

def calculate_volatility(returns):
  return np.std(returns)
  #standard deviation: square root of(average of(sum of (the differences of all values and the mean squared)))
  #shows how spread out the numbers are in a list. A large standard deviation means the numbers are very spread out
  #in this case it means the returns are very volatile


def calculate_var(returns, confidence=0.95):
  return np.percentile(returns, (1 - confidence) * 100)
  #expresses with confidence level(95%) that we can expect not to lose more than np.percentile
  #np.percentile is the value at risk
