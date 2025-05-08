import plotly.graph_objs as go

def plot_returns(returns):
  returns_percent = returns * 100  # Convert to percentage
    fig = go.Figure([go.Scatter(y=returns_percent, name="Daily Returns")])
    fig.update_layout(title="Daily Returns", xaxis_title="Date", yaxis_title="Return in %")
    fig.show()
  # fig = go.Figure([go.Scatter(y=returns, name="Daily Returns")])
  # fig.update_layout(title="Daily Returns", xaxis_title="Date", yaxis_title="Return in %")
  # fig.show()
  #Creates an interactive line chart of the daily returns using Plotly.
