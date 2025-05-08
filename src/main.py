from data_loader import fetch_data
import risk_metrics
from visualizer import plot_returns

if __name__ == "__main__":
  df = fetch_data("AAPL", "2024-01-01", "2025-01-01")
  returns = calculate_daily_returns(df)
  print("Volatility:", calculate_volatility(returns))
  print("VaR:", calculate_var(returns))
  plot_returns(returns)
