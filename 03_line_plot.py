import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(56)

x = np.linspace(0, 1., 100)
y = np.random.randn(100)

trace0 = go.Scatter(x=x, y=y, mode="lines", name="line")
trace1 = go.Scatter(x=x, y=y+5, mode="lines+markers", name="my favourite")
trace2 = go.Scatter(x=x, y=y-5, mode="markers", name="scatter")

data = [trace0, trace1, trace2]

layout = go.Layout(title="Line plot",
                   xaxis=dict(title="time"),
                   yaxis=dict(title="observation"))

fig = go.Figure(layout=layout, data=data)

pyo.plot(fig, filename="line_plot.html")