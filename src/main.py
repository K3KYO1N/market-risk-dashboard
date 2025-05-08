from data_loader import fetch_data
from risk_metrics import calculate_daily_returns, calculate_volatility, calculate_var
from visualizer import plot_returns

if __name__ == "__main__":
  df = fetch_data("AAPL", "2024-01-01", "2025-01-01")
  returns = calculate_daily_returns(df)
  print(returns)
  print("Volatility:", calculate_volatility(returns))
  print("VaR:", calculate_var(returns))
  plot_returns(returns)
