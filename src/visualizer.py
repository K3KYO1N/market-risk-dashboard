import plotly.graph_objs as go

def plot_returns(returns):
  # Ensure datetime index and sort just in case
  returns.index = pd.to_datetime(returns.index)
  returns = returns.sort_index()
  
  # Convert to percent
  returns_percent = returns * 100
  
  # Get date range and y-range
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
      xaxis=dict(
          range=[x_min, x_max],  # show full year
          rangeslider_visible=False
      ),
      yaxis=dict(
          range=[y_min, y_max]  # show full % return range
      )
  )
  
  fig.show()

# def plot_returns(returns):
#   returns_percent = returns * 100  # Convert to percentage
#   fig = go.Figure([go.Scatter(x=returns.index, y=returns_percent, name="Daily Returns")])
#   fig.update_layout(
#       title="Daily Returns",
#       xaxis_title="Date",
#       yaxis_title="Return in %"
#   )
#   fig.show()

# def plot_returns(returns):
#   returns_percent = returns * 100  # Convert to percentage
#   fig = go.Figure([go.Scatter(y=returns_percent, name="Daily Returns")])
#   fig.update_layout(title="Daily Returns", xaxis_title="Date", yaxis_title="Return in %")
#   fig.show()
#   # fig = go.Figure([go.Scatter(y=returns, name="Daily Returns")])
#   # fig.update_layout(title="Daily Returns", xaxis_title="Date", yaxis_title="Return in %")
#   # fig.show()
#   #Creates an interactive line chart of the daily returns using Plotly.
