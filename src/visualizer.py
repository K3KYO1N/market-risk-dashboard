import plotly.graph_objs as go
import pandas as pd

def plot_returns(returns):
  # If returns is a DataFrame, select the correct column
  if isinstance(returns, pd.DataFrame):
      returns = returns.iloc[:, 0]  # or returns['AAPL'] if you know the column name
  
  returns.index = pd.to_datetime(returns.index)
  returns = returns.sort_index()
  returns_percent = returns * 100
  
  x_min, x_max = returns.index.min(), returns.index.max()
  y_min, y_max = returns_percent.min(), returns_percent.max()
  
  fig = go.Figure([
      go.Scatter(
          x=returns.index,
          y=returns_percent,
          name="Daily Returns",
          hovertemplate='%{x|%b %d, %Y}<br>%{y:.2f}%'
      )
  ])
  
  fig.update_layout(
      title="Daily Returns",
      xaxis_title="Date",
      yaxis_title="Return in %",
      xaxis=dict(range=[x_min, x_max], rangeslider_visible=False),
      yaxis=dict(range=[y_min, y_max])
  )
  
  fig.show()
#   #Creates an interactive line chart of the daily returns using Plotly.
